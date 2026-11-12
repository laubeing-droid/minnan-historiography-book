"""Independent recomputation: reads inputs/output, never imports chapter programs.
Run from workspace root. Prints assertion counts; no source writes or network.
"""
import csv, json, math, statistics, itertools
from fractions import Fraction as F
from collections import Counter, defaultdict
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parents[2]
B=ROOT/'revision/附件'; R=Path(__file__).resolve().parent
checks=[]
def j(p): return json.loads(p.read_text(encoding='utf-8'))
def c(p):
    with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def result(ch,s):return j(R/(f'ch{ch}_s{s}_v2' if ch in [13,15] else f'ch{ch}_s{s}')/'result.json')
def inp(ch,s):return j(B/f'ch{ch}/{ch}.{s}/input.json')
def eq(label,actual,expected):
    if isinstance(expected,(float,F)) and actual is not None:
        ok=math.isclose(float(actual),float(expected),rel_tol=1e-11,abs_tol=1e-10)
    else:ok=actual==expected
    checks.append({'check':label,'pass':ok,'actual':actual,'expected':str(expected) if isinstance(expected,F) else expected})
    if not ok:print('FAIL',label,repr(actual),repr(expected))

# 12: original-only parameters, missingness, zeros, late release, ffill provenance.
raw={int(x['period']):x for x in c(B/'ch12/data/demo_annual_observations.csv') if x['series_id']=='DEMO_PORT_A'}
for origin,imp,scale in [(1915,'none','none'),(1915,'ffill1','standard'),(1918,'none','none'),(1919,'none','none'),(1920,'none','none')]:
    out=R/f'ch12_origin{origin}_{imp}_{scale}'; rows=c(out/'train_input.csv'); params=j(out/'transform_params.json')
    vals=[float(x['y']) for y,x in raw.items() if y<=origin and x['y'] and int(x['availability_year'])<=origin]
    eq(f'12/{origin}/{imp}/n',params['n_original_available'],len(vals));eq(f'12/{origin}/{imp}/mean',params['mean'],statistics.mean(vals));eq(f'12/{origin}/{imp}/scale',params['scale'],statistics.pstdev(vals))
    eq(f'12/{origin}/calendar',[int(x['period']) for x in rows],list(range(1900,origin+1)))
    for x in rows:
        y=int(x['period']);rr=raw.get(y); available=bool(rr and rr['y'] and int(rr['availability_year'])<=origin)
        eq(f'12/{origin}/{imp}/{y}/observed',x['observed_mask'],str(int(available)))
        eq(f'12/{origin}/{imp}/{y}/y',x['y'],str(float(rr['y'])) if available else '')
    row={int(x['period']):x for x in rows};eq(f'12/{origin}/{imp}/zero',row[1914]['input_y'],'0.0')
    if imp=='ffill1':
        eq('12/ffill/original_missing',row[1903]['y'],'');eq('12/ffill/value',float(row[1903]['input_y']),float(raw[1902]['y']));eq('12/ffill/mask',row[1903]['imputed_mask'],'1');eq('12/ffill/gap',row[1903]['years_since_last_observed'],'1')
        for y in [1907,1910,1911]:eq(f'12/ffill/no_fill_{y}',row[y]['input_y'],'')
    if origin in [1918,1919]:eq(f'12/{origin}/late',row[1918]['status'],'not_available');eq(f'12/{origin}/late_value',row[1918]['y'],'')
eq('12/ACF_four_values',F(sum((a-5)*(b-5) for a,b in zip([2,4,6],[4,6,8])),20),F(1,4))
adapter=c(R/'ch13_adapter_1915/annual_series.csv')
eq('12-13/calendar',[int(x['period']) for x in adapter],list(range(1900,1916)))
eq('12-13/zero',next(x['value'] for x in adapter if x['period']=='1914'),'0.0')
eq('12-13/missing',next(x['value'] for x in adapter if x['period']=='1903'),'')
fits=j(R/'ch13_annual_model_expected_rejection/fit_records.json')
eq('12-13/model_contract_reject',all(x['status']=='failed' and 'incomplete or unavailable' in x['reason'] for x in fits),True)

# 13.1: task-specific denominators; RNG-generated values only descriptive, not old output recovery.
d=inp(13,1);r=result(13,1)
for row in r['forecast']:
    e=[a-b for a,b in zip(d['forecast']['actual'],row['predictions'])]
    eq('13.1/'+row['method']+'/MAE',row['MAE'],sum(map(abs,e))/len(e))
eq('13.1/class_majority',r['classification_scores']['majority']['accuracy'],F(1,2));eq('13.1/class_nearest',r['classification_scores']['nearest']['accuracy'],1.0)
eq('13.1/fixed_counts',[r['anomaly'][0]['point_scores'][k] for k in ['TP','FP','FN','TN']],[0,1,3,4])
eq('13.1/mad_counts',[r['anomaly'][1]['point_scores'][k] for k in ['TP','FP','FN','TN']],[3,1,0,4])
for z in r['generation']:
    x=z['values'];mu=sum(x)/len(x);eq('13.1/generation/'+z['method']+'/mean',z['mean'],mu);eq('13.1/generation/'+z['method']+'/variance',z['population_variance'],sum((v-mu)**2 for v in x)/len(x))

# 13.2-4: only actually available standard-library baselines; verify per-origin rows.
series={int(x['period']):float(x['value']) for x in c(B/'ch13/teaching_series.csv')}
for phase in ['validation','test']:
    p=R/f'ch13_models_{phase}';preds=c(p/'predictions.csv');summ=c(p/'summary.csv')
    for x in preds:
        if x['candidate'] not in ['last','seasonal']:continue
        o,h=int(x['origin']),int(x['horizon']);expected=series[o] if x['candidate']=='last' else series[o-3+(h-1)%4]
        eq(f'13.models/{phase}/{x["candidate"]}/{o}/{h}',float(x['prediction']),expected)
    for x in summ:
        if x['candidate'] in ['last','seasonal']:
            errors=[abs(series[int(y['target'])]-float(y['prediction'])) for y in preds if y['candidate']==x['candidate']]
            eq('13.models/'+phase+'/'+x['candidate']+'/MAE',float(x['MAE']),sum(errors)/len(errors))
        else:eq('13.models/'+x['candidate']+'/blocked',int(x['failed']),12)

# 13.5 hierarchy and 13.6 every defined metric including partial truth.
r=result(13,5)
for row in r['summary']:
    ex={'X':(F(7,9),F(2,3)),'Y':(F(5,9),F(11,15))}[row['method']]
    eq('13.5/'+row['method']+'/equal',row['equal_node_average'],ex[0]);eq('13.5/'+row['method']+'/weighted',row['teaching_WRMSSE'],ex[1])
d=inp(13,6);r=result(13,6)
for x in r['metrics']:
    s=next(s for s in d['series'] if s['id']==x['series']);a=s['actual'];p=s['predictions'][x['method']];tag='13.6/'+s['id']+'/'+x['method']
    ee=[abs(F(str(y))-F(str(z))) for y,z in zip(a,p) if y is not None];scale=sum(abs(F(s['train'][i])-F(s['train'][i-s['m']])) for i in range(s['m'],len(s['train'])))/(len(s['train'])-s['m'])
    eq(tag+'/scale',x['mase_training_scale'],scale);complete=len(ee)==len(a)
    eq(tag+'/MAE',x['MAE'],sum(ee)/len(ee) if complete else None)
    eq(tag+'/RMSE',x['RMSE'],math.sqrt(float(sum(e*e for e in ee)/len(ee))) if complete else None)
    eq(tag+'/MASE',x['MASE'],sum(ee)/len(ee)/scale if complete and scale else None)
    mp=[100*abs(F(y)-F(z))/abs(F(y)) for y,z in zip(a,p) if y not in [None,0]]
    sm=[200*abs(F(y)-F(z))/(abs(F(y))+abs(F(z))) for y,z in zip(a,p) if y is not None and abs(y)+abs(z)]
    eq(tag+'/MAPE',x['MAPE'],sum(mp)/len(mp) if len(mp)==len(a) else None);eq(tag+'/sMAPE',x['sMAPE'],sum(sm)/len(sm) if len(sm)==len(a) else None)

# Independent direct rolling windows (no chapter function imported).
for s,phase,outname in [(7,'validation','ch13_s7_v2'),(7,'test','ch13_s7_test_v2'),(10,'validation','ch13_s10_v2')]:
    d=inp(13,s);r=j(R/outname/'result.json');cs={x['id']:x for x in d['candidates']};truth={x['period']:x for x in d['truth']}
    for x in r['forecast_rows']:
        cand=cs[x['candidate']];o=x['origin'];lo=1 if cand['window'] is None else o-cand['window']+1;values=[];prev=None;current=None
        for y in sorted(d['history'],key=lambda y:y['period']):
            if not lo<=y['period']<=o or y['available_at']>o:continue
            v=y['value']
            if v is None and cand['fill']=='ffill':v=prev
            elif v is not None:prev=v
            if v is not None:values.append(F(v))
            if y['period']==o:current=v
        expected=None if len(values)<d['min_train'] else (current if cand['method']=='last' else sum(values)/len(values))
        eq(f'13.{s}/{phase}/{x["candidate"]}/{o}/{x["horizon"]}',x['prediction'],expected)
    for x in r['summary']:
        rows=[y for y in r['forecast_rows'] if y['candidate']==x['candidate']];e=[abs(F(str(y['actual']))-F(str(y['prediction']))) for y in rows if y['actual'] is not None and y['prediction'] is not None]
        eq(f'13.{s}/{phase}/{x["candidate"]}/MAE',x['MAE'],sum(e)/len(e));eq(f'13.{s}/{phase}/{x["candidate"]}/planned',x['planned'],8)
r=result(13,8);eq('13.8/pinball',r['mean_pinball'],F(8,15));eq('13.8/CRPS',r['empirical_CRPS'],F(4,3))
for x in r['interval_summary']:
    cov,w,score={'A':(F(4,5),F(16,5),F(36,5)),'B':(1.0,20.0,20.0)}[x['method']]
    eq('13.8/'+x['method']+'/coverage',x['coverage'],cov);eq('13.8/'+x['method']+'/width',x['width'],w);eq('13.8/'+x['method']+'/score',x['interval_score'],score)
d=inp(13,9);r=result(13,9)
for name,n in Counter(x['search'] for x in r['trials']).items():eq('13.9/budget/'+name,n,8)
for row in r['trials']:
    cc=next(c for c in d['candidates'] if c['id']==row['candidate']);ee=[]
    if cc['window']==99:eq('13.9/C7_failed',row['status'],'failed');continue
    for o in d['validation_origins']:
        xx=d['values'][o-cc['window']+1:o+1];p=xx[-1] if cc['method']=='last' else (sum(xx)/len(xx) if cc['transform']=='identity' else math.prod(1+x for x in xx)**(1/len(xx))-1)
        ee.extend(abs(y-p) for y in d['values'][o+1:o+1+d['horizon']])
    eq('13.9/'+row['search']+'/'+str(row['trial']),row['validation_MAE'],sum(ee)/len(ee))

# 14: non-automatic confirmations, independent SVD least squares, geometry/bounds.
r=result(14,1);eq('14.1/summary',r['summary'],{'mentions':7,'candidate_pairs':9,'retained_pairs':6,'confirmed':3});eq('14.1/unresolved',r['unresolved'],['M02','M04','M05','M06'])
d=inp(14,2);r=result(14,2)
for sc,got in zip(d['scenarios'],r['scenarios']):
    A=np.array([[1,p['u'],p['v']] for p in d['control']],float);y=np.array([sc['control_override'].get(p['id'],[p['x'],p['y']]) for p in d['control']],float);coef=np.linalg.lstsq(A,y,rcond=None)[0]
    for k,key in enumerate(['x','y']):
        for i in range(3):eq('14.2/'+sc['name']+'/'+key+str(i),got['coefficients'][key][i],float(coef[i,k]))
    errs=[np.array([1,p['u'],p['v']])@coef-np.array([p['x'],p['y']]) for p in d['check']]
    eq('14.2/'+sc['name']+'/RMSE',got['rmse_check'],math.sqrt(sum(float(e@e) for e in errs)/len(errs)))
r=result(14,3);eq('14.3/distance',r['P1_P2_distance'],5.0);eq('14.3/line',next(x['length'] for x in r['features'] if x['id']=='L1'),7.0);eq('14.3/area',next(x['area'] for x in r['features'] if x['id']=='A1'),12.0);eq('14.3/rejected',sum(x['status']=='rejected' for x in r['features']),5)
r=result(14,4)
for cutoff in [2020,2022]:
    a={x['event']:x for x in r['assignments'] if x['known_at']==cutoff};eq(f'14.4/{cutoff}/boundary_conflict',a['T4']['status'],'conflict');eq(f'14.4/{cutoff}/cross_period',a['T8']['status'],'cross_period');eq(f'14.4/{cutoff}/unknown',a['T9']['status'],'unknown_time')
eq('14.4/late_evidence',[x['status'] for x in r['assignments'] if x['event']=='T10'],['matched','conflict'])
r=result(14,5);bounds={'A_old':(300,800),'A_new':(300,300),'B':(500,500),'C':(350,550),'D':(400,math.sqrt(500000)),'E':(1000,1200),'F':(None,None)}
for x in r['distance_bounds']:
    lo,hi=bounds[x['position']];eq('14.5/'+x['position']+'/min',x['minimum'],lo);eq('14.5/'+x['position']+'/max',x['maximum'],hi)

# 15: denominators, Floyd-Warshall vs chapter Dijkstra, exact spatial permutation.
r=result(15,1)
for x in r['regions']:
    ex={'A':(2,3,4,.5),'B':(2,2,8,.25),'C':(1,1,2,.5),'D':(0,0,0,None),'E':(None,None,None,None)}[x['region']]
    eq('15.1/'+x['region'],[x[k] for k in ['events','valid_records','opportunities','event_per_opportunity']],list(ex))
d=inp(15,2);r=result(15,2);ids=[x['id'] for x in d['nodes']]
for t in d['times']:
    dist={(a,b):0 if a==b else math.inf for a in ids for b in ids}
    for e in d['edges']:
        if e['active'] and e['start']<=t<=e['end'] and e['minutes'] is not None:dist[e['from'],e['to']]=min(dist[e['from'],e['to']],e['minutes'])
    for k in ids:
        for a in ids:
            for b in ids:dist[a,b]=min(dist[a,b],dist[a,k]+dist[k,b])
    for x in r['paths']:
        if x['time']!=t:continue
        expected=min(dist[a,x['target']] for a in d['sources']) if x['source']=='MULTI' else dist[x['source'],x['target']]
        eq(f'15.2/{t}/{x["source"]}/{x["target"]}',x['minutes'],None if expected==math.inf else expected)
d=inp(15,3);r=result(15,3);v=[F(x['events']) for x in d['regions']];names=[x['id'] for x in d['regions']];edges=[(names.index(a),names.index(b)) for a,b in d['edges']]
def moran(v):
    z=[a-sum(v)/len(v) for a in v];return F(len(v),2*len(edges))*sum(2*z[a]*z[b] for a,b in edges)/sum(a*a for a in z)
obs=moran(v);tail=sum(moran(p)>=obs for p in itertools.permutations(v));eq('15.3/I',F(r['global']['I']),F(3,5));eq('15.3/tail',r['global']['exact_upper_tail'],F(tail,math.factorial(len(v))));eq('15.3/rate_constant',r['global']['opportunity_status'],'constant_attribute');eq('15.3/group_tail',r['global']['within_group_upper_tail'],1.0)
d=inp(15,4);r=result(15,4)
for x in r['regional']:
    rows=[y for y in d['cells'] if (y['region'],y['period'])==(x['region'],x['period'])]
    eq('15.4/'+x['region']+'/'+x['period']+'/raw',x['raw_rate'],F(sum(y['events'] for y in rows),sum(y['opportunities'] for y in rows)));eq('15.4/'+x['region']+'/'+x['period']+'/standard',x['standardized_rate'],sum(F(str(d['weights'][y['stratum']]))*F(y['events'],y['opportunities']) for y in rows))
d=inp(15,5);r=result(15,5);groups=defaultdict(list)
for x in r['joint_configurations']:groups[x['partition'],x['window'],x['location_version'],x['configuration']].append(x)
for key,rows in groups.items():eq('15.5/conserve/'+str(key),sum(x['observed_located_count'] for x in rows),6 if key[1]=='early' else 9);eq('15.5/unlocated/'+str(key),rows[0]['unlocated'],['U'])
eq('15.5/configuration_groups',len(groups),48)
r=result(15,6);eq('15.6/M5_root',next(x['source_roots'] for x in r['timeline'] if x['id']=='M5'),['M2']);eq('15.6/no_causal_score',all(x['causal_score'] is None for x in r['interpretations']),True)

# 16: classify original assertions independently, preserve duplicates as evidence.
nodes={x['entity_id']:x for x in c(B/'ch16/entities.csv')};statements=c(B/'ch16/assertions.csv');rules=j(B/'ch16/rules.json')
for name,assume,defer,end in [('base',set(),set(),rules['end_year']),('identity',{'P3'},set(),rules['end_year']),('deferred',set(),{'R2'},rules['end_year']),('window',set(),set(),1709)]:
    chosen=[]
    for x in statements:
        ok=all(nodes[x[k]]['identity_status']=='confirmed' or x[k] in assume for k in ['subject','object']) and x['layer']=='statement' and x['judgment']=='accepted' and bool(x['start_year']) and int(x['start_year'] or 99999)<=end and int(x['end_year'] or -99999)>=rules['start_year'] and x['instance_id'] not in defer
        if ok:chosen.append(x)
    actual=c(R/f'ch16_{name}/confirmed_instances.csv');eq('16/'+name+'/instances',set(x['instance_id'] for x in actual),set(x['instance_id'] for x in chosen));eq('16/'+name+'/assertions',j(R/f'ch16_{name}/provenance.json')['counts']['included_assertions'],len(chosen))
texts={x['source_id']:x['text'] for x in j(B/'ch16/candidate_sources.json')}
for x in j(R/'ch16_base/candidate_evidence.json'):
    if x['selected_span']:a,b=x['selected_span'];eq('16/candidate/'+x['candidate_id'],texts[x['source_id']][a:b],x['quote'])

# 17: enumerate all simple paths rather than reuse Brandes; independent set assignments.
events=c(B/'ch17/events.csv');nodes=sorted(x['node_id'] for x in c(B/'ch17/nodes.csv'));edges={tuple(sorted([x['sender'],x['recipient']])) for x in events}
def exhaustive_between(nodes,edges):
    adj={a:set() for a in nodes};raw={a:F(0) for a in nodes}
    for a,b in edges:adj[a].add(b);adj[b].add(a)
    def paths(a,b,visited):
        if a==b:yield visited;return
        for v in adj[a]-set(visited):yield from paths(v,b,visited+[v])
    for a,b in itertools.combinations(nodes,2):
        pp=list(paths(a,b,[a]))
        if not pp:continue
        shortest=min(map(len,pp));pp=[p for p in pp if len(p)==shortest]
        for n in nodes:raw[n]+=F(sum(n in p[1:-1] for p in pp),len(pp))
    return raw
raw=exhaustive_between(nodes,edges)
for x in c(R/'ch17_base/centralities.csv'):eq('17/base/betweenness/'+x['node_id'],F(x['raw_betweenness_fraction']),raw[x['node_id']])
plus=exhaustive_between(nodes,edges|{('B','E')});sens=j(R/'ch17_base/sensitivity.json')
for x in sens['assume_BE']['centralities']:eq('17/BE/betweenness/'+x['node_id'],F(x['raw_betweenness_fraction']),plus[x['node_id']])
eq('17/BE/D',plus['D'],F(7,2));eq('17/BE/Fnorm',plus['F']/21,F(5,21))
active=nodes[:-1];degrees=Counter(n for e in edges for n in e);opts={g:[] for g in [F(1,10),F(1,2),F(1),F(2)]};best={g:None for g in opts};count=0
for labels in itertools.product(range(len(active)),repeat=len(active)-1):
    lab=(0,)+labels
    if any(lab[i]>max(lab[:i])+1 for i in range(1,len(lab))):continue
    count+=1;part=[tuple(active[i] for i in range(len(active)) if lab[i]==k) for k in range(max(lab)+1)]
    for g in opts:
        q=sum(F(sum(a in block and b in block for a,b in edges),len(edges))-g*F(sum(degrees[a] for a in block),2*len(edges))**2 for block in part)
        canonical=';'.join(','.join(b) for b in part)
        if best[g] is None or q>best[g]:best[g]=q;opts[g]=[canonical]
        elif q==best[g]:opts[g].append(canonical)
eq('17/community/partition_count',count,877)
actual=c(R/'ch17_base/communities.csv')
for g in opts:rows=[x for x in actual if F(x['gamma'])==g];eq('17/community/'+str(g)+'/partitions',sorted(x['active_partition'] for x in rows),sorted(opts[g]));eq('17/community/'+str(g)+'/Q',F(rows[0]['Q_fraction']),best[g])

print(json.dumps({'checks':len(checks),'passed':sum(x['pass'] for x in checks),'failed':[x for x in checks if not x['pass']]},ensure_ascii=False,indent=2,default=str))
with (R/'independent_results_after.json').open('x',encoding='utf-8') as f:json.dump(checks,f,ensure_ascii=False,indent=2,default=str)
raise SystemExit(1 if any(not x['pass'] for x in checks) else 0)

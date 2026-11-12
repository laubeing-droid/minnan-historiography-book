"""Post-fix contract checks. No source writes, only this run's fresh report."""
import sys, json, math, csv, copy, importlib.util
from pathlib import Path
from types import SimpleNamespace
from fractions import Fraction
sys.dont_write_bytecode=True
R=Path(__file__).resolve().parent;B=R.parents[1]/'revision/附件'
tests=[]
def check(name,value):tests.append({'check':name,'pass':bool(value)})
def j(name):return json.loads((R/name/'result.json').read_text())
def module(ch,file):
    s=importlib.util.spec_from_file_location(f'review_ch{ch}',B/f'ch{ch}'/file);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def raises(name,fn):
    try:fn()
    except ValueError:check(name,True)
    else:check(name,False)
m12=module(12,'preprocess_annual.py')
records=m12.read_selected(B/'ch12/data/demo_annual_observations.csv','DEMO_PORT_A')
args=SimpleNamespace(train_start=1900,origin=1915,series_id='DEMO_PORT_A',impute='none',scale='standard')
constant=copy.deepcopy(records)
for x in constant.values():
    if x['y'] is not None:x['y']=5
rows,params=m12.prepare_train(constant,args)
check('12/constant_scale_one',params['constant_train'] and params['scale']==1 and all(x['z'] in (0,None) for x in rows))
empty=copy.deepcopy(records)
for x in empty.values():x.update(y=None,availability_year=None,status='source_missing')
raises('12/no_original_observations',lambda:m12.prepare_train(empty,args))
m13=module(13,'workflow.py');d=json.loads((B/'ch13/13.7/input.json').read_text());c=d['candidates'][0]
a=m13.rolling_predict(d['history'],c,d['validation_origins'],d['horizons'],d['min_train'])
changed=copy.deepcopy(d['history'])
for x in changed:
    if x['period']>max(d['validation_origins']):x['value']=1000000
b=m13.rolling_predict(changed,c,d['validation_origins'],d['horizons'],d['min_train'])
check('13.7/future_values_do_not_change_validation',a==b)
raises('13.7/duplicate_history',lambda:m13.rolling_predict(d['history']+[d['history'][0]],c,[4],[1],3))
raises('13.7/duplicate_truth',lambda:m13.rolling_score(a[1],d['truth']+[d['truth'][0]],10))
raises('13.6/invalid_season',lambda:m13.metrics([1],[1],[1,2],0))
for name,status,rate_status in [('bug_after_ch15_missing','missing_attribute','missing_attribute'),('edge_ch15_missing_opportunities','defined','missing_attribute'),('edge_ch15_zero_opportunities','defined','missing_attribute'),('edge_ch15_constant','constant_attribute','defined'),('edge_ch15_no_weights','no_weights_or_too_few_regions','no_weights_or_too_few_regions')]:
    x=j(name);check('15.3/'+name+'/status',x['global']['status']==status);check('15.3/'+name+'/opportunity_status',x['global']['opportunity_status']==rate_status);check('15.3/'+name+'/preserve_six_regions',len(x['regions'])==6)
    if status!='defined':check('15.3/'+name+'/no_permutations',x['permutations']==[] and x['global']['exact_upper_tail'] is None)
x=j('edge_ch15_standardization_missing');a=next(x for x in x['regional'] if x['region']=='A' and x['period']=='T1');check('15.4/no_weight_renormalization',a['raw_rate'] is None and a['standardized_rate'] is None)
x=j('edge_ch15_zero_cycle');data=json.loads((R/'fixtures/edge_ch15_zero_cycle.json').read_text());edge={e['id']:e for e in data['edges']}
for p in x['paths']:
    if p['source']=='MULTI':continue
    node=p['source'];seen={node};cost=0
    for eid in p['path']:
        e=edge[eid];check('15.2/path_endpoint/'+eid,e['from']==node);node=e['to'];cost+=e['minutes'];check('15.2/no_zero_cycle/'+eid,node not in seen);seen.add(node)
    if p['minutes'] is not None:check('15.2/path_cost/'+p['source']+'/'+p['target'],node==p['target'] and cost==p['minutes'])
    if {p['source'],p['target']}=={'A','B'}:check('15.2/zero_AB',p['minutes']==0)
m16=module(16,'relations.py');check('16/all_overlapping_quote_positions',m16.all_positions('aaaa','aa')==[[0,2],[1,3],[2,4]])
raises('16/empty_quote_refused',lambda:m16.all_positions('abc',''))
check('16/unknown_year_none',m16.integer_year('') is None)
m17=module(17,'network_analysis.py')
for nodes in [set(),{'H'},{'A','H'}]:
    z=m17.graph_metrics(nodes,set());check('17/isolates_preserved/'+str(len(nodes)),len(z['summary']['isolates'])==len(nodes));check('17/density_empty_or_small/'+str(len(nodes)),z['summary']['density_fraction']==(None if len(nodes)<2 else '0'))
raises('17/self_loop_refused',lambda:m17.adjacency({'A'},{('A','A')}))
raises('17/absent_endpoint_refused',lambda:m17.adjacency({'A'},{('A','B')}))
raises('17/community_limit',lambda:m17.community_analysis(set('ABCDEFGHI'),{(a,b) for a,b in zip('ABCDEFGH','BCDEFGHI')},[Fraction(1)],8))
print(json.dumps({'checks':len(tests),'passed':sum(x['pass'] for x in tests),'failed':[x for x in tests if not x['pass']]},ensure_ascii=False,indent=2))
with (R/'independent_edge_results.json').open('x') as f:json.dump(tests,f,indent=2)
raise SystemExit(any(not x['pass'] for x in tests))

#!/usr/bin/env python3
"""新编教材标准库工作流 NOT_RUN。无网络，输入只读，输出目录必须不存在。"""
import argparse,csv,hashlib,json,math,platform,random,statistics,time
from fractions import Fraction as F
from pathlib import Path

def finite(x):
 if isinstance(x,bool) or not isinstance(x,(int,float)) or not math.isfinite(x):raise ValueError('finite number required')
 return float(x)
def avg(x):return sum(x)/len(x) if x else None
def metrics(actual,pred,train=None,m=1):
 if len(actual)!=len(pred) or not actual:raise ValueError('nonempty equal lengths required')
 pairs=[(F(str(y)),F(str(p))) for y,p in zip(actual,pred) if y is not None and p is not None]
 complete=len(pairs)==len(actual);errors=[abs(y-p) for y,p in pairs];mae=sum(errors)/len(errors) if errors else None
 mapes=[100*abs(y-p)/abs(y) for y,p in pairs if y!=0];smapes=[200*abs(y-p)/(abs(y)+abs(p)) for y,p in pairs if abs(y)+abs(p)!=0]
 scale=None
 if train is not None:
  if type(m)!=int or m<1:raise ValueError('invalid period')
  if len(train)>m and all(v is not None for v in train):scale=sum(abs(F(str(train[i]))-F(str(train[i-m]))) for i in range(m,len(train)))/(len(train)-m)
 result={'planned':len(actual),'paired':len(pairs),'MAE':float(mae) if complete else None,'RMSE':math.sqrt(float(sum(e*e for e in errors)/len(errors))) if complete else None,'MAPE':float(sum(mapes)/len(mapes)) if len(mapes)==len(actual) else None,'sMAPE':float(sum(smapes)/len(smapes)) if len(smapes)==len(actual) else None,'MASE':float(mae/scale) if complete and scale not in (None,0) else None,'mape_defined_rows':len(mapes),'smape_defined_rows':len(smapes),'mase_training_scale':float(scale) if scale is not None else None,'status':'complete' if complete else 'incomplete_targets'}
 for k,v in result.items():
  if isinstance(v,float) and not math.isfinite(v):raise ValueError('metric outside float range')
 return result

def binary_scores(y,p):
 tp=sum(a==b==1 for a,b in zip(y,p));fp=sum(a==0 and b==1 for a,b in zip(y,p));fn=sum(a==1 and b==0 for a,b in zip(y,p));tn=sum(a==b==0 for a,b in zip(y,p))
 return {'TP':tp,'FP':fp,'FN':fn,'TN':tn,'accuracy':(tp+tn)/len(y),'precision':tp/(tp+fp) if tp+fp else None,'recall':tp/(tp+fn) if tp+fn else None,'false_alarms_per_100_normal':100*fp/(fp+tn) if fp+tn else None}
def intervals(labels):
 out=[];start=None
 for i,x in enumerate(labels+[0]):
  if x and start is None:start=i
  if not x and start is not None:out.append((start,i-1));start=None
 return out
def task_baselines(d):
 f=d['forecast'];tr=f['train'];truth=f['actual'];m=f['season'];last=[tr[-1]]*len(truth);season=[tr[-m+(i%m)] for i in range(len(truth))]
 forecast=[dict(method=n,predictions=p,**metrics(truth,p,tr,m)) for n,p in [('last',last),('seasonal',season)]]
 c=d['classification'];counts={k:sum(r['label']==k for r in c['train']) for k in [0,1]};majority=min(counts,key=lambda k:(-counts[k],k));cp=[]
 def center(v):return [x-avg(v) for x in v]
 for r in c['test']:
  q=center(r['values']);rank=[]
  for t in c['train']:
   v=center(t['values'])
   if len(v)!=len(q):raise ValueError('unequal fragment lengths')
   rank.append((sum((x-y)**2 for x,y in zip(q,v)),t['id'],t['label']))
  best=min(rank);cp.append({'id':r['id'],'actual':r['label'],'majority':majority,'nearest':best[2],'nearest_id':best[1]})
 an=d['anomaly'];med=statistics.median(an['train']);mad=statistics.median([abs(x-med) for x in an['train']])
 if mad==0:raise ValueError('MAD zero')
 anomaly=[];real=intervals(an['labels'])
 for name,flags in [('fixed',[int(v>an['fixed_threshold']) for v in an['test']]),('mad',[int(abs(v-med)>an['mad_multiplier']*mad) for v in an['test']])]:
  alarms=intervals(flags);used=set();hits=0
  for lo,hi in alarms:
   hit=next((i for i,(a,b) in enumerate(real) if i not in used and lo<=b and hi>=a),None)
   if hit is not None:used.add(hit);hits+=1
  anomaly.append({'method':name,'flags':flags,'point_scores':binary_scores(an['labels'],flags),'alarm_events':alarms,'event_hits':hits,'event_missed':len(real)-hits,'false_alarm_events':len(alarms)-hits})
 g=d['generation'];mu=statistics.mean(g['train']);sigma=statistics.pstdev(g['train']);rng=random.Random(g['seed']);emp=[rng.choice(g['train']) for _ in range(g['count'])];rng=random.Random(g['seed']);normal=[rng.gauss(mu,sigma) for _ in range(g['count'])]
 generated=[]
 for name,x in [('empirical',emp),('normal',normal),('reference',g['reference'])]:
  mean=statistics.mean(x);z=[v-mean for v in x];den=sum(v*v for v in z)
  generated.append({'method':name,'values':x,'mean':mean,'population_variance':statistics.pvariance(x),'lag1_summary':sum(a*b for a,b in zip(z,z[1:]))/den if den else None})
 return {'forecast':forecast,'classification_rows':cp,'classification_scores':{k:binary_scores([r['actual'] for r in cp],[r[k] for r in cp]) for k in ['majority','nearest']},'anomaly':anomaly,'generation':generated}

def hierarchy(d):
 ids=list(d['train']);train={k:d['train'][k][:] for k in ids};actual={k:d['actual'][k][:] for k in ids}
 for x in [train,actual]:
  if len({len(v) for v in x.values()})!=1:raise ValueError('length mismatch')
  x['TOTAL']=[sum(vals) for vals in zip(*(x[k] for k in ids))]
 scales={}
 for k,x in train.items():
  first=next((i for i,v in enumerate(x) if v!=0),len(x));xx=x[first:]
  scales[k]=sum((b-a)**2 for a,b in zip(xx,xx[1:]))/(len(xx)-1) if len(xx)>1 else None
 money={k:sum(train[k][-d['weight_window']:])*d['prices'][k] for k in ids};totalmoney=sum(money.values())
 if totalmoney<=0:raise ValueError('invalid training amount weight')
 weights={k:d['layer_weights']['bottom']*money[k]/totalmoney for k in ids};weights['TOTAL']=d['layer_weights']['total'];rows=[];summary=[]
 for name,forecasts in d['forecasts'].items():
  p={k:forecasts[k][:] for k in ids};p['TOTAL']=[sum(v) for v in zip(*(p[k] for k in ids))];scores=[]
  for k in train:
   if len(p[k])!=len(actual[k]):raise ValueError('target length mismatch')
   mse=avg([(a-b)**2 for a,b in zip(actual[k],p[k])]);score=math.sqrt(mse/scales[k]) if scales[k] not in (None,0) else None;scores.append((k,score));rows.append({'method':name,'series':k,'scale':scales[k],'prediction':p[k],'MSE':mse,'RMSSE':score,'weight':weights[k],'training_amount':money.get(k,totalmoney)})
  summary.append({'method':name,'equal_node_average':avg([v for k,v in scores]) if all(v is not None for k,v in scores) else None,'teaching_WRMSSE':sum(weights[k]*v for k,v in scores) if all(v is not None for k,v in scores) else None})
 return {'series_scores':rows,'summary':summary,'official_competition_score':False}

def point_metrics(d):
 rows=[];details=[]
 for s in d['series']:
  for name,p in s['predictions'].items():
   actual=[y if t<=d['score_cutoff'] else None for y,t in zip(s['actual'],s['available_at'])]
   rows.append(dict(series=s['id'],method=name,unit=s['unit'],**metrics(actual,p,s['train'],s['m'])))
   for i,(y,yhat) in enumerate(zip(actual,p)):details.append({'series':s['id'],'method':name,'origin':d['origin'],'horizon':i+1,'target':d['origin']+i+1,'actual':y,'prediction':yhat,'available_at':s['available_at'][i],'error':y-yhat if y is not None else None})
 ag=[];ids=d['aggregation']['ids'];units={s['unit'] for s in d['series'] if s['id'] in ids}
 if len(units)!=1:raise ValueError('cannot aggregate unlike units')
 for name in sorted({r['method'] for r in rows}):
  rs=[r for r in rows if r['series'] in ids and r['method']==name];es=[r['error'] for r in details if r['series'] in ids and r['method']==name];ws=d['aggregation']['weights']
  ag.append({'method':name,'macro_MAE':avg([r['MAE'] for r in rs]),'pooled_MAE':avg([abs(e) for e in es]),'weighted_MAE':sum(ws[r['series']]*r['MAE'] for r in rs)/sum(ws.values())})
 return {'metrics':rows,'prediction_rows':details,'declared_aggregation':ag}

def rolling_predict(history,candidate,origins,horizons,min_train):
 # Truth is deliberately not an argument.
 periods=[r['period'] for r in history]
 if len(periods)!=len(set(periods)):raise ValueError('duplicate historical period')
 fits=[];pred=[]
 for origin in origins:
  lower=min(periods) if candidate['window'] is None else origin-candidate['window']+1
  selected=[];excluded=[];previous=None
  for r in sorted(history,key=lambda r:r['period']):
   if not lower<=r['period']<=origin:continue
   if r['available_at']>origin:excluded.append({'id':r['id'],'reason':'not_available'});continue
   if r['value'] is None:
    if candidate['fill']=='ffill' and previous is not None:selected.append(dict(r,value=previous['value'],imputed_from=previous['id']))
    else:excluded.append({'id':r['id'],'reason':'missing_no_legal_fill'})
   else:selected.append(dict(r,imputed_from=None));previous=r
  values=[r['value'] for r in selected];status='success';why=None;estimate=None
  if len(values)<min_train:status='failed';why='insufficient_training'
  elif candidate['method']=='last':
   current=next((r for r in selected if r['period']==origin),None)
   if current is None:status='failed';why='origin_value_unavailable'
   else:estimate=current['value']
  elif candidate['method']=='mean':estimate=avg(values)
  else:raise ValueError('unknown candidate method')
  fit_id=f"{candidate['id']}_o{origin}";fits.append({'fit_id':fit_id,'candidate':candidate['id'],'origin':origin,'window_start':lower,'window_end':origin,'training':selected,'excluded':excluded,'effective_count':len(values),'status':status,'reason':why})
  for h in horizons:pred.append({'fit_id':fit_id,'candidate':candidate['id'],'origin':origin,'horizon':h,'target':origin+h,'prediction':estimate,'status':status,'reason':why})
 return fits,pred

def rolling_score(pred,truth,cutoff):
 td={r['period']:r for r in truth}
 if len(td)!=len(truth):raise ValueError('duplicate truth period')
 out=[]
 for p in pred:
  y=td.get(p['target']);r=dict(p);r['actual']=y['value'] if y and y['available_at'] is not None and y['available_at']<=cutoff else None;r['error']=None;r['score_status']='prediction_failed' if p['prediction'] is None else ('missing_or_late_truth' if r['actual'] is None else 'scored')
  if r['score_status']=='scored':r['error']=r['actual']-p['prediction']
  out.append(r)
 return out

def rolling_summary(rows):
 ids=sorted({r['candidate'] for r in rows});out=[]
 for c in ids:
  rs=[r for r in rows if r['candidate']==c];errors=[r['error'] for r in rs if r['error'] is not None];success=sum(r['prediction'] is not None for r in rs)
  out.append({'candidate':c,'planned':len(rs),'predicted':success,'failed':len(rs)-success,'scored':len(errors),'coverage':success/len(rs),'MAE':avg([abs(e) for e in errors]),'RMSE':math.sqrt(avg([e*e for e in errors])) if errors else None,'eligible':success==len(rs) and bool(errors)})
 return out

def backtest(d,section,out,phase,selection):
 candidates=d['candidates'];origins=d['validation_origins'];cutoff=d['validation_cutoff']
 if phase=='test':
  if section==10:raise ValueError('ablation test is intentionally NOT_RUN; old test cannot be a new blind test')
  if not selection:raise ValueError('--selection required')
  lock=json.loads(Path(selection).read_text());candidates=[c for c in candidates if c['id']==lock['selected']]
  if not candidates:raise ValueError('selected candidate absent')
  if lock['history_sha256']!=hashlib.sha256(json.dumps(d['history'],sort_keys=True).encode()).hexdigest():raise ValueError('history changed after selection')
  origins=d['test_origins'];cutoff=d['test_cutoff']
 fits=[];rows=[]
 for c in candidates:
  fs,ps=rolling_predict(d['history'],c,origins,d['horizons'],d['min_train']);fits+=fs;rows+=rolling_score(ps,d['truth'],cutoff)
 summary=rolling_summary(rows);result={'fit_records':fits,'forecast_rows':rows,'summary':summary,'phase':phase}
 if phase=='validation':
  eligible=[r for r in summary if r['eligible']]
  selected=min(eligible,key=lambda r:(r['MAE'],r['candidate']))['candidate'] if eligible else None
  lock={'selected':selected,'selection_basis':'validation only','history_sha256':hashlib.sha256(json.dumps(d['history'],sort_keys=True).encode()).hexdigest()}
  (out/'selection.json').write_text(json.dumps(lock,indent=2),encoding='utf8');result['selection']=lock
 if section==10:
  keys=set.intersection(*[{(r['origin'],r['horizon']) for r in rows if r['candidate']==c['id'] and r['error'] is not None} for c in candidates])
  result['common_task_summary']=rolling_summary([r for r in rows if (r['origin'],r['horizon']) in keys]);m={r['candidate']:r['MAE'] for r in summary};result['interaction']=(m['C4']-m['C2'])-(m['C3']-m['C1']) if all(m.get(k) is not None for k in ['C1','C2','C3','C4']) else None;result['test_status']='NOT_RUN_NO_NEW_INDEPENDENT_TEST'
 return result

def probability(d):
 q=d['quantile_case'];levels=q['levels'];pred=q['predictions']
 if len(levels)!=len(pred) or any(not 0<p<1 for p in levels) or sorted(levels)!=levels or sorted(pred)!=pred:raise ValueError('invalid/crossing quantiles')
 quantiles=[]
 for p,x in zip(levels,pred):
  error=q['actual']-x;quantiles.append({'level':p,'prediction':x,'actual':q['actual'],'pinball_loss':p*error if error>=0 else (1-p)*(-error)})
 e=d['ensemble_case'];xs=e['members'];M=len(xs)
 if not M:raise ValueError('empty ensemble')
 crps=sum(abs(x-e['actual']) for x in xs)/M-sum(abs(x-y) for x in xs for y in xs)/(2*M*M)
 i=d['interval_case'];alpha=1-i['nominal'];rows=[];summary=[]
 if not 0<alpha<1:raise ValueError('invalid nominal level')
 for name,ints in i['forecasts'].items():
  if len(ints)!=len(i['actual']):raise ValueError('length mismatch')
  rs=[]
  for k,(y,(lo,hi)) in enumerate(zip(i['actual'],ints)):
   if lo>hi:raise ValueError('reversed interval')
   r={'method':name,'row':k,'actual':y,'lower':lo,'upper':hi,'hit':lo<=y<=hi,'width':hi-lo,'interval_score':hi-lo+2/alpha*(max(lo-y,0)+max(y-hi,0))};rs.append(r);rows.append(r)
  summary.append({'method':name,'n':len(rs),'coverage':avg([r['hit'] for r in rs]),'width':avg([r['width'] for r in rs]),'interval_score':avg([r['interval_score'] for r in rs])})
 return {'quantile_losses':quantiles,'mean_pinball':avg([r['pinball_loss'] for r in quantiles]),'empirical_CRPS':crps,'interval_rows':rows,'interval_summary':summary,'PIT':'NOT_COMPUTED: finite quantiles do not specify full continuous CDF'}

def search_prediction(prefix,c,h):
 w=c['window']
 if len(prefix)<w:raise ValueError('window exceeds available history')
 x=prefix[-w:]
 if c['method']=='last':v=x[-1]
 elif c['transform']=='identity':v=avg(x)
 elif c['transform']=='log1p':
  if any(z<=-1 for z in x):raise ValueError('log1p domain')
  v=math.expm1(avg([math.log1p(z) for z in x]))
 else:raise ValueError('unknown transformation')
 return [v]*h

def search_evaluate(development,c,origins,h):
 errors=[]
 for o in origins:
  p=search_prediction(development[:o+1],c,h);y=development[o+1:o+1+h]
  if len(y)!=h:raise ValueError('missing validation target')
  errors += [abs(a-b) for a,b in zip(y,p)]
 return avg(errors)

def searches(d,out):
 cutoff=max(d['validation_origins'])+d['horizon'];dev=d['values'][:cutoff+1];candidates=d['candidates'];trials=[];locks=[];tests=[]
 plans=[('grid',None,list(range(len(candidates))))]
 for seed in d['seeds']:
  rng=random.Random(seed);plans.append((f'random_{seed}',seed,[rng.randrange(len(candidates)) for _ in range(d['budget'])]))
 for name,seed,indices in plans:
  if len(indices)!=d['budget']:raise ValueError('budget mismatch')
  current=[]
  for trial,idx in enumerate(indices):
   c=candidates[idx];start=time.perf_counter()
   try:value=search_evaluate(dev,c,d['validation_origins'],d['horizon']);status='complete';error=None
   except ValueError as e:value=None;status='failed';error=str(e)
   row={'search':name,'seed':seed,'trial':trial,'candidate':c['id'],'validation_MAE':value,'status':status,'error':error,'elapsed_seconds':time.perf_counter()-start};current.append(row);trials.append(row)
  success=[r for r in current if r['status']=='complete'];best=min(success,key=lambda r:(r['validation_MAE'],r['candidate'],r['trial'])) if success else None
  lock={'search':name,'selected':best['candidate'] if best else None,'all_trials':current,'development_sha256':hashlib.sha256(json.dumps(dev).encode()).hexdigest()};locks.append(lock)
  # Save the development-only choice before reading the final test slice.
  (out/(name+'_selection.json')).write_text(json.dumps(lock,ensure_ascii=False,indent=2),encoding='utf8')
  if best:
   c=next(c for c in candidates if c['id']==best['candidate']);o=d['test_origin'];p=search_prediction(d['values'][:o+1],c,d['horizon']);y=d['values'][o+1:o+1+d['horizon']];tests.append({'search':name,'selected':c['id'],'prediction':p,'actual':y,'test_MAE':avg([abs(a-b) for a,b in zip(y,p)])})
 return {'trials':trials,'selections':locks,'tests':tests,'budget_unit':'one search, not best across all seeds'}

def main():
 p=argparse.ArgumentParser();p.add_argument('--section',type=int,choices=[1,5,6,7,8,9,10],required=True);p.add_argument('--input',default='input.json');p.add_argument('--out',required=True);p.add_argument('--phase',choices=['validation','test'],default='validation');p.add_argument('--selection');a=p.parse_args();raw=Path(a.input).read_bytes();d=json.loads(raw);out=Path(a.out);out.mkdir(parents=True,exist_ok=False)
 try:
  if not d.get('fiction'):raise ValueError('explicit fiction flag required')
  fn={1:task_baselines,5:hierarchy,6:point_metrics,8:probability}
  result=fn[a.section](d) if a.section in fn else (backtest(d,a.section,out,a.phase,a.selection) if a.section in (7,10) else searches(d,out))
  (out/'result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2,allow_nan=False),encoding='utf8')
  for name,rows in result.items():
   if isinstance(rows,list) and rows and all(isinstance(r,dict) for r in rows):
    fields=sorted(set().union(*(r.keys() for r in rows)))
    with (out/(name+'.csv')).open('x',encoding='utf-8-sig',newline='') as f:
     w=csv.DictWriter(f,fields);w.writeheader();w.writerows({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(list,dict)) else v for k,v in r.items()} for r in rows)
  (out/'run_manifest.json').write_text(json.dumps({'status':'EXECUTED_BY_READER','section':a.section,'python':platform.python_version(),'input_sha256':hashlib.sha256(raw).hexdigest()},indent=2),encoding='utf8')
 except Exception as e:
  (out/'failure.json').write_text(json.dumps({'status':'FAILED','error':repr(e)},ensure_ascii=False),encoding='utf8');raise
if __name__=='__main__':main()

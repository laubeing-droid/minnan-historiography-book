#!/usr/bin/env python3
"""ARIMA/SARIMA/Holt-Winters reader workflow. NOT_RUN. Never installs dependencies."""
import argparse,csv,hashlib,json,math,platform,warnings
from pathlib import Path
from workflow import rolling_score,rolling_summary

def read_series(path):
 rows=[]
 with Path(path).open(encoding='utf-8-sig',newline='') as f:
  for r in csv.DictReader(f):
   rows.append({'id':r.get('source_id') or f"row:{r['period']}",'period':int(r['period']),'available_at':int(r['available_at']) if r['available_at'] else None,'value':None if r['value']=='' else float(r['value'])})
 if not rows or len({r['period'] for r in rows})!=len(rows):raise ValueError('empty or duplicate periods')
 rows.sort(key=lambda r:r['period'])
 if [r['period'] for r in rows]!=list(range(rows[0]['period'],rows[-1]['period']+1)):raise ValueError('calendar axis must remain contiguous')
 if any(r['value'] is not None and not math.isfinite(r['value']) for r in rows):raise ValueError('nonfinite value')
 return rows

def fitted_forecast(train,name,h,m):
 # Only the legal training prefix enters this function; truth is not available here.
 if name=='last':return [train[-1]]*h,None,{'library':'stdlib','residuals':[],'diagnostic_status':'not_applicable'}
 if name=='seasonal':
  if m<=1 or len(train)<m:raise ValueError('seasonal naive not applicable')
  return [train[-m+(i%m)] for i in range(h)],None,{'library':'stdlib','residuals':[],'diagnostic_status':'not_applicable'}
 try:
  import statsmodels
  from statsmodels.tsa.arima.model import ARIMA
  from statsmodels.tsa.statespace.sarimax import SARIMAX
  from statsmodels.tsa.holtwinters import ExponentialSmoothing
  from statsmodels.stats.diagnostic import acorr_ljungbox
 except ImportError as e:raise RuntimeError('DEPENDENCY_MISSING: statsmodels; no automatic installation') from e
 with warnings.catch_warnings(record=True) as caught:
  warnings.simplefilter('always')
  if name=='arima':res=ARIMA(train,order=(1,1,0),trend='n',enforce_stationarity=True,enforce_invertibility=True,missing='raise').fit();df=1
  elif name=='sarima':
   if m<=1:raise ValueError('SARIMA requires justified m>1')
   res=SARIMAX(train,order=(1,0,0),seasonal_order=(0,1,1,m),trend='n',simple_differencing=False,enforce_stationarity=True,enforce_invertibility=True,missing='raise').fit(disp=False);df=2
  elif name=='holt_winters':
   if m<=1:raise ValueError('seasonal Holt-Winters requires justified m>1')
   res=ExponentialSmoothing(train,trend='add',seasonal='add',damped_trend=True,seasonal_periods=m,initialization_method='estimated',use_boxcox=False,missing='raise').fit(optimized=True);df=None
  else:raise ValueError('unknown model')
  ret=getattr(res,'mle_retvals',None)
  if isinstance(ret,dict) and ret.get('converged') is False:raise ValueError('optimizer did not converge')
  if ret is not None and hasattr(ret,'success') and not bool(ret.success):raise ValueError('optimizer did not succeed')
  if name=='holt_winters':pred=[float(v) for v in res.forecast(h)];interval=None
  else:
   forecast=res.get_forecast(steps=h);pred=[float(v) for v in forecast.predicted_mean];interval=[[float(a),float(b)] for a,b in forecast.conf_int(alpha=0.05)]
  burn=max(int(getattr(res,'loglikelihood_burn',0)),int(getattr(res,'nobs_diffuse',0)))
  raw=[float(v) for v in res.resid];residuals=raw[burn:]
  diag={'library':'statsmodels','version':statsmodels.__version__,'warnings':[str(w.message) for w in caught],'residuals':residuals,'burn':burn,'ljung_box':None,'diagnostic_status':'not_applicable_hw' if df is None else 'insufficient_length'}
  if name!='holt_winters':
   standardized=getattr(res.filter_results,'standardized_forecasts_error',None)
   diag['standardized_innovations']=[float(v) if math.isfinite(float(v)) else None for v in standardized[0][burn:]] if standardized is not None else None
  lag=min(8,len(residuals)//5)
  if df is not None and lag>df and all(math.isfinite(v) for v in residuals):
   lb=acorr_ljungbox(residuals,lags=[lag],model_df=df,return_df=True)
   diag['ljung_box']={'lag':lag,'model_df':df,'statistic':float(lb['lb_stat'].iloc[0]),'pvalue':float(lb['lb_pvalue'].iloc[0])};diag['diagnostic_status']='computed_not_interpreted'
 if len(pred)!=h or not all(math.isfinite(v) for v in pred):raise ValueError('invalid forecast')
 if interval and (len(interval)!=h or any(not all(math.isfinite(v) for v in z) or z[0]>z[1] for z in interval)):raise ValueError('invalid interval')
 return pred,interval,diag

def main():
 p=argparse.ArgumentParser();p.add_argument('--input',default='teaching_series.csv');p.add_argument('--protocol',default='model_protocol.json');p.add_argument('--out',required=True);p.add_argument('--phase',choices=['validation','test'],default='validation');p.add_argument('--selection');a=p.parse_args();out=Path(a.out);out.mkdir(parents=True,exist_ok=False)
 try:
  raw=Path(a.input).read_bytes();pr=Path(a.protocol).read_bytes();config=json.loads(pr);rows=read_series(a.input);models=config['models'];origins=config[a.phase+'_origins'];h=config['horizon'];m=config['seasonal_period'];input_hash=hashlib.sha256(raw).hexdigest();protocol_hash=hashlib.sha256(pr).hexdigest()
  if a.phase=='test':
   if not a.selection:raise ValueError('--selection required')
   lock=json.loads(Path(a.selection).read_text())
   if lock['input_sha256']!=input_hash or lock['protocol_sha256']!=protocol_hash:raise ValueError('input/protocol changed since lock')
   models=[lock['selected']]
   if not models[0]:raise ValueError('no eligible selected model')
  fits=[];predictions=[]
  for name in models:
   for origin in origins:
    fitid=f'{name}_o{origin}';prefix=[r for r in rows if r['period']<=origin];train=[r for r in prefix if r['available_at'] is not None and r['available_at']<=origin];record={'fit_id':fitid,'candidate':name,'origin':origin,'training_ids':[r['id'] for r in train]};point=[None]*h;interval=None
    try:
     if not prefix or prefix[-1]['period']!=origin or len(train)!=len(prefix) or any(r['value'] is None for r in train):raise ValueError('incomplete or unavailable training prefix; do not compress calendar')
     point,interval,diag=fitted_forecast([r['value'] for r in train],name,h,m);record.update(status='success',diagnostics=diag)
    except Exception as e:record.update(status='failed',reason=repr(e))
    fits.append(record)
    for i,v in enumerate(point):predictions.append({'fit_id':fitid,'candidate':name,'origin':origin,'horizon':i+1,'target':origin+i+1,'prediction':v,'lower95':interval[i][0] if interval else None,'upper95':interval[i][1] if interval else None,'interval_status':'model_conditional_95' if interval else ('point_only' if v is not None else 'failed'),'status':record['status'],'reason':record.get('reason')})
  scored=rolling_score(predictions,rows,config[a.phase+'_score_cutoff']);summary=rolling_summary(scored)
  if a.phase=='validation':
   eligible=[r for r in summary if r['eligible']];chosen=min(eligible,key=lambda r:(r['MAE'],models.index(r['candidate'])))['candidate'] if eligible else None
   (out/'selection.json').write_text(json.dumps({'selected':chosen,'input_sha256':input_hash,'protocol_sha256':protocol_hash,'criterion':'full forecast coverage then validation MAE then declared order'},indent=2),encoding='utf8')
  (out/'fit_records.json').write_text(json.dumps(fits,ensure_ascii=False,indent=2,allow_nan=False),encoding='utf8')
  for filename,data in [('predictions.csv',scored),('summary.csv',summary)]:
   with (out/filename).open('x',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,sorted(set().union(*(r.keys() for r in data))));w.writeheader();w.writerows(data)
  (out/'run_manifest.json').write_text(json.dumps({'status':'EXECUTED_BY_READER','phase':a.phase,'python':platform.python_version(),'input_sha256':input_hash,'protocol_sha256':protocol_hash,'plots':'NOT_GENERATED; diagnostics require human interpretation'},indent=2),encoding='utf8')
 except Exception as e:
  (out/'failure.json').write_text(json.dumps({'status':'FAILED','error':repr(e)},ensure_ascii=False),encoding='utf8');raise
if __name__=='__main__':main()

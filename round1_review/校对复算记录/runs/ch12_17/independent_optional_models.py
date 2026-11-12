"""Audit new statsmodels/Optuna runs without importing chapter programs.
Optimizer refits use the same installed estimator library (not an independent
optimizer). Forecast propagation, loss aggregation, interval coverage and
Ljung-Box sums are independently implemented and explicitly distinguished.
"""
import csv,json,math,warnings
from pathlib import Path
import numpy as np
from scipy.stats import norm,chi2
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.holtwinters import ExponentialSmoothing
R=Path(__file__).resolve().parent;B=R.parents[1]/'revision/附件/ch13'
tests=[];summaries=[];refits=[]
def csvread(p):
    with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def check(name,actual,expected,tol=1e-9):
    ok=math.isclose(float(actual),float(expected),rel_tol=tol,abs_tol=tol) if isinstance(expected,(int,float,np.floating)) and not isinstance(expected,bool) else actual==expected
    tests.append({'check':name,'pass':ok,'actual':actual,'expected':expected})
    if not ok:print('FAIL',name,actual,expected)
data=csvread(B/'teaching_series.csv');series={int(x['period']):float(x['value']) for x in data};rows_by_id={x['source_id']:x for x in data};z=norm.ppf(.975)
for phase in ['validation','test']:
    out=R/f'ch13_models_{phase}_with_dependencies';pred=csvread(out/'predictions.csv');fits=json.loads((out/'fit_records.json').read_text());summary=csvread(out/'summary.csv')
    for f in fits:
        check(phase+'/'+f['fit_id']+'/success',f['status'],'success')
        check(phase+'/'+f['fit_id']+'/training_origin_safe',all(int(rows_by_id[i]['period'])<=f['origin'] and int(rows_by_id[i]['available_at'])<=f['origin'] for i in f['training_ids']),True)
        diag=f['diagnostics'];lb=diag.get('ljung_box')
        if lb:
            residuals=diag['residuals'];n=len(residuals);mu=sum(residuals)/n;dev=[v-mu for v in residuals];den=sum(v*v for v in dev)
            acf=[sum(dev[t]*dev[t-k] for t in range(k,n))/den for k in range(1,lb['lag']+1)]
            q=n*(n+2)*sum(a*a/(n-k) for k,a in enumerate(acf,1));p=float(chi2.sf(q,lb['lag']-lb['model_df']))
            check(phase+'/'+f['fit_id']+'/LB_Q',lb['statistic'],q);check(phase+'/'+f['fit_id']+'/LB_p',lb['pvalue'],p)
        name=f['candidate'];o=f['origin'];y=[series[i] for i in range(1,o+1)];pts=sorted([x for x in pred if x['fit_id']==f['fit_id']],key=lambda x:int(x['horizon']))
        if name in ['last','seasonal']:continue
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter('always')
            if name=='arima':res=ARIMA(y,order=(1,1,0),trend='n',enforce_stationarity=True,enforce_invertibility=True,missing='raise').fit()
            elif name=='sarima':res=SARIMAX(y,order=(1,0,0),seasonal_order=(0,1,1,4),trend='n',simple_differencing=False,enforce_stationarity=True,enforce_invertibility=True,missing='raise').fit(disp=False)
            else:res=ExponentialSmoothing(y,trend='add',seasonal='add',damped_trend=True,seasonal_periods=4,initialization_method='estimated',use_boxcox=False,missing='raise').fit(optimized=True)
        if name=='holt_winters':
            phi=float(res.params['damping_trend']);level=float(res.level[-1]);trend=float(res.trend[-1]);season=[float(v) for v in res.season[-4:]]
            expected=[level+sum(phi**k for k in range(1,h+1))*trend+season[(h-1)%4] for h in range(1,5)]
            for row,mu in zip(pts,expected):check(phase+'/'+f['fit_id']+'/HW_recurrence_h'+row['horizon'],float(row['prediction']),mu)
            details={'level':level,'trend':trend,'phi':phi,'seasonal_tail':season}
        else:
            # Reimplement state-space moments from the one-step predicted final
            # state. Do not call forecast/get_forecast/conf_int in this audit.
            ssm=res.model.ssm;T=np.asarray(ssm['transition']);Z=np.asarray(ssm['design']);Q=np.asarray(ssm['state_cov']);select=np.asarray(ssm['selection']);H=np.asarray(ssm['obs_cov']);c=np.asarray(ssm['state_intercept']);d=np.asarray(ssm['obs_intercept']);state=res.predicted_state[:,-1].copy();P=res.predicted_state_cov[:,:,-1].copy()
            for row in pts:
                mu=float((Z@state+d).item());variance=float((Z@P@Z.T+H).item());sd=math.sqrt(variance)
                check(phase+'/'+f['fit_id']+'/state_mean_h'+row['horizon'],float(row['prediction']),mu);check(phase+'/'+f['fit_id']+'/lower95_h'+row['horizon'],float(row['lower95']),mu-z*sd);check(phase+'/'+f['fit_id']+'/upper95_h'+row['horizon'],float(row['upper95']),mu+z*sd)
                state=T@state+c;P=T@P@T.T+select@Q@select.T
            details={'parameters':dict(zip(res.param_names,map(float,res.params))),'mle_retvals':{k:bool(v) if isinstance(v,(bool,np.bool_)) else str(v) for k,v in res.mle_retvals.items()}}
        refits.append({'phase':phase,'fit_id':f['fit_id'],'method':'same-library optimizer refit plus independent forecast recursion','warnings':[str(w.message) for w in caught],**details})
    for row in summary:
        name=row['candidate'];rr=[p for p in pred if p['candidate']==name];errors=[series[int(p['target'])]-float(p['prediction']) for p in rr];mae=sum(map(abs,errors))/len(errors);rmse=math.sqrt(sum(e*e for e in errors)/len(errors));interval=[p for p in rr if p['lower95'] and p['upper95']]
        check(phase+'/'+name+'/MAE',float(row['MAE']),mae);check(phase+'/'+name+'/RMSE',float(row['RMSE']),rmse);check(phase+'/'+name+'/all_planned',int(row['planned']),len(rr));check(phase+'/'+name+'/scored',int(row['scored']),len(rr))
        covered=sum(float(p['lower95'])<=series[int(p['target'])]<=float(p['upper95']) for p in interval)
        summaries.append({'phase':phase,'candidate':name,'planned':len(rr),'predicted':len(rr),'scored':len(errors),'MAE':mae,'RMSE':rmse,'interval_denominator':len(interval),'interval_hits':covered,'empirical_95_coverage':covered/len(interval) if interval else None,'mean_interval_width':sum(float(p['upper95'])-float(p['lower95']) for p in interval)/len(interval) if interval else None,'interpretation':'conditional intervals; not historical uncertainty; small overlapping sample'})
study=json.loads((R/'ch13_optuna_with_dependencies/study.json').read_text());d=json.loads((B/'13.9/input.json').read_text());candidates={c['id']:c for c in d['candidates']}
check('Optuna/budget',len(study['trials']),d['budget']);check('Optuna/no_test',study['test_status'],'NOT_EVALUATED')
for t in study['trials']:
    c=candidates[t['params']['candidate']];errors=[]
    for o in d['validation_origins']:
        xx=d['values'][o-c['window']+1:o+1]
        mu=xx[-1] if c['method']=='last' else (sum(xx)/len(xx) if c['transform']=='identity' else math.prod(1+x for x in xx)**(1/len(xx))-1)
        errors.extend(abs(mu-y) for y in d['values'][o+1:o+1+d['horizon']])
    check('Optuna/trial_'+str(t['number']),t['value'],sum(errors)/len(errors))
best=min(study['trials'],key=lambda t:(t['value'],t['params']['candidate'],t['number']));check('Optuna/selection',study['selected'],best)
print(json.dumps({'checks':len(tests),'passed':sum(t['pass'] for t in tests),'failed':[t for t in tests if not t['pass']],'metrics':summaries},ensure_ascii=False,indent=2))
with (R/'independent_optional_results.json').open('x') as f:json.dump({'checks':tests,'metrics':summaries,'refit_details':refits},f,indent=2,default=lambda x:float(x))
raise SystemExit(any(not t['pass'] for t in tests))

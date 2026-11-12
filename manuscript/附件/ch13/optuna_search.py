#!/usr/bin/env python3
"""NOT_RUN. Optional Optuna orchestration; no install and no final-test evaluation."""
import argparse,json,platform
from pathlib import Path
from workflow import search_evaluate

def main():
 p=argparse.ArgumentParser();p.add_argument('--input',default='13.9/input.json');p.add_argument('--out',required=True);p.add_argument('--seed',type=int,default=139);a=p.parse_args();out=Path(a.out);out.mkdir(parents=True,exist_ok=False)
 try:
  import optuna
  d=json.loads(Path(a.input).read_text());last=max(d['validation_origins'])+d['horizon'];development=d['values'][:last+1];candidates={c['id']:c for c in d['candidates']}
  study=optuna.create_study(direction='minimize',sampler=optuna.samplers.RandomSampler(seed=a.seed),pruner=optuna.pruners.NopPruner())
  def objective(trial):
   key=trial.suggest_categorical('candidate',list(candidates));return search_evaluate(development,candidates[key],d['validation_origins'],d['horizon'])
  study.optimize(objective,n_trials=d['budget'],n_jobs=1,catch=(ValueError,))
  rows=[{'number':t.number,'params':t.params,'state':t.state.name,'value':t.value} for t in study.trials]
  complete=[t for t in rows if t['state']=='COMPLETE'];best=min(complete,key=lambda t:(t['value'],t['params']['candidate'],t['number'])) if complete else None
  (out/'study.json').write_text(json.dumps({'status':'EXECUTED_BY_READER','optuna_version':optuna.__version__,'python':platform.python_version(),'seed':a.seed,'budget':d['budget'],'trials':rows,'selected':best,'test_status':'NOT_EVALUATED'},indent=2),encoding='utf8')
 except Exception as e:
  (out/'failure.json').write_text(json.dumps({'status':'FAILED','error':repr(e),'installation':'never automatic'},indent=2),encoding='utf8');raise
if __name__=='__main__':main()

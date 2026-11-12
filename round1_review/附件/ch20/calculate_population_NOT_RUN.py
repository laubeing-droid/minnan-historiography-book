#!/usr/bin/env python3
"""NOT_RUN. Standard-library arithmetic only; print a NEW result, do not alter input."""
from pathlib import Path
import csv,json
from decimal import Decimal
root=Path(__file__).resolve().parent
with (root/'population_values.csv').open(encoding='utf-8',newline='') as f: rows=list(csv.DictReader(f))
expected={'Q2010','Q2020','F2010','F2020'}
if len(rows)!=4 or {r['id'] for r in rows}!=expected: raise SystemExit('four unique input IDs required')
if any(r['unit']!='人' for r in rows): raise SystemExit('unit must be 人')
v={r['id']:Decimal(r['value']) for r in rows}
if any(x<=0 for x in v.values()): raise SystemExit('positive denominator inputs required')
out={'input_identity':'inherited published values; new calculation not historical observation'}
for key in ('Q','F'):
    old,new=v[key+'2010'],v[key+'2020']
    out[key]={'increase':str(new-old),'growth_pct':str((new-old)/old*100)}
shares={str(y):v['Q'+str(y)]/v['F'+str(y)]*100 for y in (2010,2020)}
out['calculated_shares_pct']={k:str(x) for k,x in shares.items()}
out['calculated_change_percentage_points']=str(shares['2020']-shares['2010'])
with (root/'published_shares.csv').open(encoding='utf-8',newline='') as f: published=list(csv.DictReader(f))
if len(published)!=2 or {r['statistical_year'] for r in published}!={'2010','2020'}: raise SystemExit('two unique published years required')
p={r['statistical_year']:Decimal(r['share_pct']) for r in published}
out['published_change_percentage_points']=str(p['2020']-p['2010'])
rest0=v['F2010']-v['Q2010'];rest1=v['F2020']-v['Q2020']
if rest0<=0: raise SystemExit('rest-of-province baseline must be positive')
out['rest_of_province']={'2010':str(rest0),'2020':str(rest1),'growth_pct':str((rest1-rest0)/rest0*100)}
out['interpretation_limit']='No migration, causal, annual-trend or culture conclusion follows from this arithmetic.'
print(json.dumps(out,ensure_ascii=False,indent=2))

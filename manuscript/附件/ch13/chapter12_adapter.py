#!/usr/bin/env python3
"""NOT_RUN. Preserve annual calendar, missingness and availability; never invent seasonality."""
import argparse,csv,json
from pathlib import Path

def main():
 p=argparse.ArgumentParser();p.add_argument('--input',required=True);p.add_argument('--series-id',required=True);p.add_argument('--origin',type=int,required=True);p.add_argument('--out',required=True);a=p.parse_args();out=Path(a.out);out.mkdir(parents=True,exist_ok=False)
 with Path(a.input).open(encoding='utf-8-sig',newline='') as f:rows=[r for r in csv.DictReader(f) if r['series_id']==a.series_id]
 if not rows:raise ValueError('series_id absent')
 periods=[int(r['period']) for r in rows]
 if len(set(periods))!=len(periods):raise ValueError('duplicate annual period')
 converted=[];audit=[]
 for r in sorted(rows,key=lambda r:int(r['period'])):
  year=int(r['period']);available=int(r['availability_year']) if r['availability_year'] else None;observed=str(r['observed_mask'])=='1';imputed=str(r['imputed_mask'])=='1';eligible=str(r['eligible_target'])=='1'
  # Imputed values never masquerade as raw observations. Empty cells remain empty.
  value=r['y'] if observed and not imputed and r['y']!='' else ''
  status='available_observation' if value and available is not None and available<=a.origin and year<=a.origin else ('future_period' if year>a.origin else ('not_yet_available' if available is not None and available>a.origin else 'missing_or_imputed_or_unavailable'))
  converted.append({'series_id':r['series_id'],'period':year,'available_at':available,'value':value,'unit':r['unit'],'source_id':r['source_id']})
  audit.append({'period':year,'status_at_origin':status,'observed_mask':observed,'imputed_mask':imputed,'eligible_target':eligible,'measure':r['measure'],'boundary_version':r['boundary_version']})
 with (out/'annual_series.csv').open('x',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,list(converted[0]));w.writeheader();w.writerows(converted)
 (out/'adapter_audit.json').write_text(json.dumps({'status':'EXECUTED_BY_READER','origin':a.origin,'frequency':'annual','seasonal_period':1,'compatible_models':['last','arima'],'rows':audit,'warning':'models.py requires complete contiguous training; missing/unavailable values stop fitting. Establish a separate authorized preprocessing protocol before proceeding.'},ensure_ascii=False,indent=2),encoding='utf8')
if __name__=='__main__':main()

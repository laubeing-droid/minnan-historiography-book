#!/usr/bin/env python3
"""NOT_RUN. CSV structural checks only. Output is exclusive-create, never overwrite."""
import argparse, csv, json
from collections import Counter
from pathlib import Path
FIELDS=['item_id','title_raw','pub_raw','source_url','locator']
p=argparse.ArgumentParser();p.add_argument('--input',required=True);p.add_argument('--output',required=True);a=p.parse_args()
with Path(a.input).open(encoding='utf-8-sig',newline='') as f:
    r=csv.DictReader(f)
    if r.fieldnames!=FIELDS: raise SystemExit('input_error: exact columns required '+str(FIELDS))
    rows=list(r)
if not rows: raise SystemExit('input_error: no rows')
ids=Counter((r.get('item_id') or '').strip() for r in rows)
result=[]
for line,row in enumerate(rows,2):
    errors=[]
    if None in row or any(row.get(k) is None for k in FIELDS): errors.append('field_count')
    for key in FIELDS:
        if not (row.get(key) or '').strip(): errors.append('missing:'+key)
    if row.get('item_id') and ids[row['item_id'].strip()]>1: errors.append('duplicate_id')
    result.append({'csv_line':line,'input':row,'status':'input_error' if errors else 'pending_review','errors':errors})
with Path(a.output).open('x',encoding='utf-8') as f:
    json.dump({'scope':'structure only; not source verification','rows':result},f,ensure_ascii=False,indent=2)
print('Created new review file:',a.output)

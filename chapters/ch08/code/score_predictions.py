#!/usr/bin/env python3
"""Promoted 2026-11-12 from manuscript/附件/ch08/8.8/score_predictions.py.
Synthetic regression tested; no independent historical validation.
"""
import argparse,csv,json
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--predictions',required=True);p.add_argument('--reference',default='reference.csv');a=p.parse_args()
payload=json.loads(Path(a.predictions).read_text(encoding='utf-8'));rows=payload['result']['predictions']
reference=list(csv.DictReader(Path(a.reference).open(encoding='utf-8',newline='')))
def index(items,key):
    result={}
    for r in items:
        if r['id'] in result:raise ValueError('duplicate id')
        value=r[key]
        if not ((type(value) is int and value in (0,1)) or (type(value) is str and value in ('0','1'))):
            raise ValueError('binary integer or exact CSV 0/1 required')
        result[r['id']]=int(value)
    return result
pred=index(rows,'prediction');gold=index(reference,'gold')
if pred.keys()!=gold.keys():raise ValueError('id sets differ')
if not all(x in (0,1) for x in list(pred.values())+list(gold.values())):raise ValueError('binary values required')
cells={str(g)+str(q):sum(gold[k]==g and pred[k]==q for k in gold) for g in (0,1) for q in (0,1)}
print(json.dumps({'n':len(gold),'confusion_gold_prediction':cells,'errors':[k for k in gold if pred[k]!=gold[k]],'provenance':'synthetic teaching reference; not independent historical test'},ensure_ascii=False,indent=2))

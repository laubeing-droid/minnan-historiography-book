#!/usr/bin/env python3
"""NOT_RUN. Score reader-generated predictions against the provided teaching reference."""
import argparse,csv,json
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--predictions',required=True);p.add_argument('--reference',default='reference.csv');a=p.parse_args()
payload=json.loads(Path(a.predictions).read_text(encoding='utf-8'));rows=payload['result']['predictions']
reference=list(csv.DictReader(Path(a.reference).open(encoding='utf-8',newline='')))
def index(items,key):
    result={}
    for r in items:
        if r['id'] in result:raise ValueError('duplicate id')
        result[r['id']]=int(r[key])
    return result
pred=index(rows,'prediction');gold=index(reference,'gold')
if pred.keys()!=gold.keys():raise ValueError('id sets differ')
if not all(x in (0,1) for x in list(pred.values())+list(gold.values())):raise ValueError('binary values required')
cells={str(g)+str(q):sum(gold[k]==g and pred[k]==q for k in gold) for g in (0,1) for q in (0,1)}
print(json.dumps({'n':len(gold),'confusion_gold_prediction':cells,'errors':[k for k in gold if pred[k]!=gold[k]],'provenance':'synthetic teaching reference; not independent historical test'},ensure_ascii=False,indent=2))

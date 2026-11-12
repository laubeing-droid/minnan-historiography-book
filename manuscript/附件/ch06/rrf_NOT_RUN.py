#!/usr/bin/env python3
"""NOT_RUN. Fuse rank lists, retaining each run's contribution; no model execution."""
from pathlib import Path
import argparse,json,math
root=Path(__file__).resolve().parent
p=argparse.ArgumentParser();p.add_argument('--input',default=str(root/'rrf_teaching_input.json'));a=p.parse_args()
x=json.loads(Path(a.input).read_text(encoding='utf-8'))
M=x['M'];k=x['k'];c=x['c'];allowed=set(x['allowed_ids'])
if not isinstance(M,int) or M<1 or not isinstance(k,int) or k<1 or not isinstance(c,(int,float)) or not math.isfinite(c) or c<0:raise SystemExit('invalid M, k or c')
if len(allowed)!=len(x['allowed_ids']):raise SystemExit('duplicate allowed ID')
if x['kind']=='ACTUAL_OUTPUT_TEMPLATE_NOT_RUN':raise SystemExit('template is unfilled; save actual outputs to a NEW file with kind ACTUAL_RETRIEVAL_OUTPUT')
corpus=json.loads((root/'corpus.json').read_text(encoding='utf-8'));by={d['id']:d for d in corpus['documents']}
if x['corpus_version']!=corpus['corpus_version'] or not allowed<=set(by):raise SystemExit('corpus or scope mismatch')
rankings=[];contributions={}
for run in x['runs']:
    if run['question_id']!=x['question_id'] or run['corpus_version']!=x['corpus_version'] or set(run['allowed_ids'])!=allowed:raise SystemExit('run comparison conditions differ')
    best={}
    for r in run['ranking']:
        if r['id'] not in allowed or not isinstance(r['score'],(int,float)) or not math.isfinite(r['score']):raise SystemExit('invalid ranked item')
        best[r['id']]=max(best.get(r['id'],-math.inf),r['score'])
    ordered=sorted(best.items(),key=lambda z:(-z[1],z[0]))[:M]
    ranking=[]
    for rank,(i,score) in enumerate(ordered,1):
        value=1/(c+rank);contributions.setdefault(i,[]).append({'run':run['name'],'rank':rank,'contribution':value})
        ranking.append({'id':i,'score':score,'rank':rank})
    rankings.append({'run':run['name'],'ranking':ranking})
fused=[{'id':i,'score':sum(p['contribution'] for p in parts),'contributions':parts,'locator':by[i]['locator']} for i,parts in contributions.items()]
fused.sort(key=lambda z:(-z['score'],z['id']))
print(json.dumps({'identity':x['kind'],'status':'ok' if fused else 'empty_results','rankings':rankings,'fused':fused,'read_top_k':fused[:k],'tie_rule':'ID order for display, not superiority','c':c,'M':M,'k':k},ensure_ascii=False,indent=2))

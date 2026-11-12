#!/usr/bin/env python3
"""NOT_RUN. Evaluate NEW teaching corpus; chapter's inherited numbers are not loaded."""
from pathlib import Path
import argparse,json
from bm25_NOT_RUN import read_corpus,rank
root=Path(__file__).resolve().parent
p=argparse.ArgumentParser();p.add_argument('--split',choices=['development','holdout_exercise'],required=True);a=p.parse_args()
corpus=read_corpus(root/'corpus.json')
x=json.loads((root/'evaluation_input.json').read_text(encoding='utf-8'))
queries=json.loads((root/'query_plan.json').read_text(encoding='utf-8'))['queries'];qmap={q['id']:q['tokens'] for q in queries}
k=x['k'];all_ids={d['id'] for d in corpus['documents']}
rows=[]
for question in x['questions']:
    if question['split']!=a.split:continue
    if not set(question['relevant_ids'])<=all_ids:raise SystemExit('unknown reference block')
    docs=[d for d in corpus['documents'] if d['statistical_year']==question['statistical_year']]
    for method in ('baseline','changed'):
        specs=question[method];paths=[];merged=[];seen=set()
        for query in specs:
            tokens=qmap[query] if query in qmap else query.split()
            result=rank(docs,tokens);paths.append({'query':query,'raw':result})
            # Multiple subqueries contribute their first candidate; a single query contributes all candidates.
            candidates=result['results'][:1] if len(specs)>1 else result['results']
            for r in candidates:
                group=r['evidence_group']
                if group not in seen:seen.add(group);merged.append(r['id'])
        selected=merged[:k];relevant=set(question['relevant_ids']);hits=len(set(selected)&relevant)
        if relevant:
            recall=hits/len(relevant);rr=next((1/i for i,b in enumerate(selected,1) if b in relevant),0)
        else:recall=None;rr=None
        rows.append({'question_id':question['id'],'method':method,'returned_ids':selected,'actual_returned_count':len(selected),'p_at_k':hits/k,'r_at_k':recall,'rr_at_k':rr,'zero_relevant':not bool(relevant),'reference':question['reference'],'paths':paths})
summary={}
for method in ('baseline','changed'):
    answerable=[r for r in rows if r['method']==method and not r['zero_relevant']]
    summary[method]={'answerable_questions':len(answerable),'mean_precision':sum(r['p_at_k'] for r in answerable)/len(answerable) if answerable else None,'mean_recall':sum(r['r_at_k'] for r in answerable)/len(answerable) if answerable else None,'mrr':sum(r['rr_at_k'] for r in answerable)/len(answerable) if answerable else None,'unanswerable_ids':[r['question_id'] for r in rows if r['method']==method and r['zero_relevant']]}
print(json.dumps({'corpus_version':corpus['corpus_version'],'split':a.split,'k':k,'warning':x['notice'],'rows':rows,'summary':summary},ensure_ascii=False,indent=2))

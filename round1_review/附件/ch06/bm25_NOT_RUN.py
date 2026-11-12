#!/usr/bin/env python3
"""NOT_RUN. Manual-token BM25 baseline; standard library, no network or writes."""
from pathlib import Path
from collections import Counter
import argparse,json,math
ROOT=Path(__file__).resolve().parent

def read_corpus(path):
    obj=json.loads(Path(path).read_text(encoding='utf-8'))
    docs=obj['documents'];ids=[d['id'] for d in docs]
    if len(ids)!=len(set(ids)):raise ValueError('duplicate block ID')
    for d in docs:
        if not isinstance(d.get('tokens'),list) or any(not isinstance(t,str) or not t for t in d['tokens']):
            raise ValueError('manual tokens required for '+d['id'])
    return obj

def rank(docs,query_tokens,k1=1.2,b=0.75):
    if not math.isfinite(k1) or k1<0 or not math.isfinite(b) or not 0<=b<=1:
        raise ValueError('k1 >= 0 and 0 <= b <= 1 required')
    query=list(dict.fromkeys(t for t in query_tokens if t))
    empty=[d['id'] for d in docs if not d['tokens']]
    eligible=[d for d in docs if d['tokens']]
    if not query:return {'status':'empty_query','results':[],'empty_blocks':empty}
    if not eligible:return {'status':'empty_index','results':[],'empty_blocks':empty}
    counts={d['id']:Counter(d['tokens']) for d in eligible}
    df=Counter(t for c in counts.values() for t in c)
    N=len(eligible);avgdl=sum(len(d['tokens']) for d in eligible)/N
    results=[]
    for d in eligible:
        c=counts[d['id']];length=len(d['tokens']);parts=[]
        for term in query:
            freq=c[term]
            if not freq:continue
            idf=math.log(1+(N-df[term]+0.5)/(df[term]+0.5))
            contribution=idf*freq*(k1+1)/(freq+k1*(1-b+b*length/avgdl))
            parts.append({'term':term,'tf':freq,'df':df[term],'idf':idf,'contribution':contribution})
        if parts:results.append({'id':d['id'],'score':sum(x['contribution'] for x in parts),'matched_terms':parts,'locator':d['locator'],'source_id':d['source_id'],'evidence_group':d['evidence_group']})
    results.sort(key=lambda x:(-x['score'],x['id']))
    for i,r in enumerate(results,1):r['rank']=i
    return {'status':'ok' if results else 'no_matching_term','query_tokens':query,'N':N,'avgdl':avgdl,'empty_blocks':empty,'unmatched_terms':[t for t in query if not df[t]],'results':results}

def main():
    p=argparse.ArgumentParser();p.add_argument('--input',default=str(ROOT/'corpus.json'))
    group=p.add_mutually_exclusive_group();group.add_argument('--query');group.add_argument('--queries')
    p.add_argument('--k1',type=float,default=1.2);p.add_argument('--b',type=float,default=.75)
    p.add_argument('--year',type=int);a=p.parse_args()
    corpus=read_corpus(a.input);docs=corpus['documents']
    if a.year is not None:docs=[d for d in docs if d['statistical_year']==a.year]
    if a.queries:queries=json.loads(Path(a.queries).read_text(encoding='utf-8'))['queries']
    else:queries=[{'id':'USER','tokens':(a.query if a.query is not None else '泉州 人口 增加').split()}]
    out={'corpus_version':corpus['corpus_version'],'allowed_ids':[d['id'] for d in docs],'k1':a.k1,'b':a.b,'queries':[]}
    for q in queries:out['queries'].append({'id':q['id'],**rank(docs,q['tokens'],a.k1,a.b)})
    print(json.dumps(out,ensure_ascii=False,indent=2))
if __name__=='__main__':main()

#!/usr/bin/env python3
"""NOT_RUN. ID and directed-cycle inspection; not an independence or truth certificate."""
from pathlib import Path
import json
root=Path(__file__).resolve().parent
obj=json.loads((root/'source_chain.json').read_text(encoding='utf-8'))
nodes=obj['nodes'];ids=[n['id'] for n in nodes]
if len(ids)!=len(set(ids)):raise SystemExit('duplicate IDs')
by={n['id']:n for n in nodes}
missing=[{'node':n['id'],'parent':p} for n in nodes for p in n['parents'] if p not in by]
state={};stack=[];cycles=[]
def visit(i):
    if state.get(i)==1:
        cycles.append(stack[stack.index(i):]+[i]);return
    if state.get(i)==2:return
    state[i]=1;stack.append(i)
    for p in by[i]['parents']:
        if p in by:visit(p)
    stack.pop();state[i]=2
for i in ids:visit(i)
print(json.dumps({'scope':'structural only; shared ancestry is not automatically independent evidence','identity':obj['identity'],'missing_references':missing,'cycles':cycles},ensure_ascii=False,indent=2))

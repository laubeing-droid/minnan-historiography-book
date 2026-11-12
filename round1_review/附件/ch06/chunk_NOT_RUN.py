#!/usr/bin/env python3
"""NOT_RUN. Four character-based chunking plans, no output file or model call."""
from pathlib import Path
import json
root=Path(__file__).resolve().parent
x=json.loads((root/'table_input.json').read_text(encoding='utf-8'))
rows=['|'.join(row) for row in x['rows']]
context=x['context'];head=x['header'];notes=x['notes']
body='\n'.join([context,head,*rows,notes])

def fixed(text,size,overlap):
    if size<=0 or not 0<=overlap<size:raise ValueError('bad size/overlap')
    out=[];start=0
    while start<len(text):
        end=min(start+size,len(text));out.append(text[start:end])
        if end==len(text):break
        start=end-overlap
    return out

def structured(size):
    prefix=context+'\n'+head+'\n';suffix='\n'+notes;blocks=[];current=[]
    for row in rows:
        if len(prefix+row+suffix)>size:raise ValueError('one complete row plus conditions exceeds limit')
        candidate=prefix+'\n'.join(current+[row])+suffix
        if current and len(candidate)>size:
            blocks.append(prefix+'\n'.join(current)+suffix);current=[]
        current.append(row)
    if current:blocks.append(prefix+'\n'.join(current)+suffix)
    return blocks

plans={'fixed_120':fixed(body,120,0),'overlap_120_30':fixed(body,120,30),'structure_600':structured(600),'fixed_600':fixed(body,600,0)}
tests=[('漳州',['常住人口数','单位：人、%','2020年11月1日零时']),('泉州',['占全省常住人口比重2010年','单位：人、%']),('厦门',['占全省常住人口比重2020年','占全省常住人口比重2010年','单位：人、%'])]
output=[]
for name,blocks in plans.items():
    checks=[]
    for place,required in tests:
        row=next(r for r in rows if r.split('|')[0]==place)
        containing=[i+1 for i,b in enumerate(blocks) if row in b]
        sufficient=[i+1 for i,b in enumerate(blocks) if row in b and all(s in b for s in required)]
        checks.append({'place':place,'complete_row_blocks':containing,'row_and_required_conditions_blocks':sufficient})
    output.append({'plan':name,'block_count':len(blocks),'total_characters':sum(map(len,blocks)),'checks':checks,'blocks':[{'id':f'{name}/{i:03d}','text':b,'source_id':'S1','source_locator':x['locator']} for i,b in enumerate(blocks,1)]})
print(json.dumps({'scope':'string checks only; not transcription or definition verification','input_identity':x['status'],'plans':output},ensure_ascii=False,indent=2))

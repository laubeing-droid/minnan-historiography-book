#!/usr/bin/env python3
"""NOT_RUN. Optional LOCAL encoder. No dependency install, model download, or remote code."""
from pathlib import Path
import argparse,json,os,importlib.util
root=Path(__file__).resolve().parent
p=argparse.ArgumentParser();p.add_argument('--model',required=True);p.add_argument('--family',choices=['bge','e5'],required=True)
p.add_argument('--input',default=str(root/'model_input.json'));p.add_argument('--revision-label',default='LOCAL_VERSION_NOT_RECORDED');a=p.parse_args()
model_path=Path(a.model).expanduser().resolve()
if not model_path.is_dir():raise SystemExit('local model directory missing; NOT_RUN, do not download automatically')
if importlib.util.find_spec('sentence_transformers') is None:raise SystemExit('existing sentence-transformers environment missing; NOT_RUN, no installation performed')
os.environ['HF_HUB_OFFLINE']='1';os.environ['TRANSFORMERS_OFFLINE']='1'
from sentence_transformers import SentenceTransformer
import numpy as np
x=json.loads(Path(a.input).read_text(encoding='utf-8'));docs=x['documents']
if len({d['id'] for d in docs})!=len(docs):raise SystemExit('duplicate block IDs')
model=SentenceTransformer(str(model_path),local_files_only=True,trust_remote_code=False,device='cpu')
qprefix='为这个句子生成表示以用于检索相关文章：' if a.family=='bge' else 'query: '
dprefix='' if a.family=='bge' else 'passage: '
query=qprefix+x['query']
scope='2020年数据统计时点为11月1日零时；初步汇总常住人口；完整定义见原公报注[3]。'
texts=[dprefix+scope+f"统计年份：{d['statistical_year']}；文字性质：{d['kind']}；"+d['text'] for d in docs]
inputs=[query,*texts]
lengths=[len(model.tokenizer(t,add_special_tokens=True,truncation=False)['input_ids']) for t in inputs]
limit=min(int(model.max_seq_length),int(model.tokenizer.model_max_length))
if limit<=0:raise SystemExit('invalid configured input limit')
if any(n>limit for n in lengths):raise SystemExit('input exceeds model limit; regroup complete text before encoding: '+str(lengths))
vectors=model.encode(inputs,prompt='',normalize_embeddings=True,convert_to_numpy=True,show_progress_bar=False)
if vectors.ndim!=2 or vectors.shape[0]!=len(inputs) or not np.isfinite(vectors).all():raise SystemExit('unexpected or non-finite output')
if np.any(np.linalg.norm(vectors,axis=1)==0):raise SystemExit('zero vector')
scores=vectors[1:]@vectors[0]
ranked=sorted([{'id':d['id'],'score':float(score),'locator':d['locator'],'source_id':d['source_id']} for d,score in zip(docs,scores)],key=lambda r:(-r['score'],r['id']))
print(json.dumps({'input_version':x['corpus_version'],'model_directory':str(model_path),'revision_label':a.revision_label,'family':a.family,'max_input_tokens':limit,'actual_inputs':inputs,'actual_token_counts':lengths,'dimensions':int(vectors.shape[1]),'normalized_vectors':vectors.tolist(),'ranking':ranked,'interpretation':'Similarity is ranking, not historical truth.'},ensure_ascii=False,indent=2))

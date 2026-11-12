#!/usr/bin/env python3
"""Local-only EmbeddingGemma 2 adapter for the chapter 6 teaching input.
This is the current embedding route; the original attachment is archival only.
No installation, download, API call or source-file write is performed here.
"""
from pathlib import Path
import argparse,hashlib,json,os

def main():
 p=argparse.ArgumentParser();p.add_argument('--model',required=True);p.add_argument('--input',required=True);p.add_argument('--revision',required=True);a=p.parse_args()
 local=Path(a.model).resolve()
 if not local.is_dir():raise SystemExit('local model directory missing')
 os.environ['HF_HUB_OFFLINE']='1';os.environ['TRANSFORMERS_OFFLINE']='1'
 import torch,numpy as np
 from sentence_transformers import SentenceTransformer
 torch.set_num_threads(2)
 raw=Path(a.input).read_bytes();x=json.loads(raw);docs=x['documents']
 if not docs or len({d['id'] for d in docs})!=len(docs):raise SystemExit('empty or duplicate document IDs')
 model=SentenceTransformer(str(local),device='cpu',local_files_only=True,trust_remote_code=False,config_kwargs={'vision_config':None,'audio_config':None},model_kwargs={'torch_dtype':torch.float32})
 if not {'SearchQuery','Document'}<=model.prompts.keys():raise SystemExit('required official retrieval prompts missing')
 scope='2020年数据统计时点为11月1日零时；初步汇总常住人口；完整定义见原公报注[3]。'
 texts=[scope+f"统计年份：{d['statistical_year']}；文字性质：{d['kind']}；"+d['text'] for d in docs]
 actual=[model.prompts['SearchQuery']+x['query']]+[model.prompts['Document']+t for t in texts]
 lengths=[len(model.tokenizer(t,add_special_tokens=True,truncation=False)['input_ids']) for t in actual]
 limit=min(8192,int(model.max_seq_length),int(model.tokenizer.model_max_length))
 if limit<=0 or any(n>limit for n in lengths):raise SystemExit('input exceeds checked context limit; no silent truncation')
 query=model.encode([x['query']],prompt_name='SearchQuery',normalize_embeddings=True,convert_to_numpy=True,show_progress_bar=False,batch_size=1)
 vectors=model.encode(texts,prompt_name='Document',normalize_embeddings=True,convert_to_numpy=True,show_progress_bar=False,batch_size=1)
 all_vectors=np.vstack([query,vectors]);norms=np.linalg.norm(all_vectors,axis=1)
 if all_vectors.shape!=(len(docs)+1,768) or not np.isfinite(all_vectors).all() or not np.allclose(norms,1,atol=1e-5):raise SystemExit('invalid embedding shape, finiteness, or unit norm')
 scores=vectors@query[0]
 ranked=sorted([{'id':d['id'],'score':float(v),'source_id':d['source_id'],'locator':d['locator']} for d,v in zip(docs,scores)],key=lambda r:(-r['score'],r['id']))
 print(json.dumps({'model_id':'google/embeddinggemma-2','revision':a.revision,'input_sha256':hashlib.sha256(raw).hexdigest(),'input_version':x['corpus_version'],'runtime':{'device':'cpu','dtype':'float32','vision':False,'audio':False,'trust_remote_code':False,'local_files_only':True},'actual_inputs':actual,'token_counts':lengths,'context_limit':limit,'dimensions':768,'vector_norms':norms.tolist(),'normalized_vectors':all_vectors.tolist(),'ranking':ranked,'interpretation':'Three-document teaching retrieval only; similarity is not historical truth or a general retrieval benchmark.'},ensure_ascii=False,indent=2,allow_nan=False))
if __name__=='__main__':main()

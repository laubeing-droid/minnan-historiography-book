from pathlib import Path
import subprocess,json,sys,importlib.util
ROOT=Path('/workspace/scratch/b06bda80e898/book_review_20261030');A=ROOT/'revision/附件';R=ROOT/'runs/ch05_06_19_23';results=[]
def run(name,chapter,script,args=(),expected=0):
 cmd=[sys.executable,'-B',str(A/chapter/script),*map(str,args)]
 p=subprocess.run(cmd,cwd=A/chapter,text=True,capture_output=True,timeout=60)
 (R/(name+'.stdout')).write_text(p.stdout);(R/(name+'.stderr')).write_text(p.stderr)
 entry={'name':name,'chapter':chapter,'script':script,'command':cmd,'exit_code':p.returncode,'expected_exit':expected,'status':'EXECUTED_PASS' if p.returncode==expected else 'FAIL','stdout':name+'.stdout','stderr':name+'.stderr'};results.append(entry)
 return p
run('links','ch05','check_links_NOT_RUN.py')
run('chunk','ch06','chunk_NOT_RUN.py')
run('bm25_default','ch06','bm25_NOT_RUN.py')
run('bm25_queries','ch06','bm25_NOT_RUN.py',['--queries','query_plan.json'])
run('bm25_empty_query','ch06','bm25_NOT_RUN.py',['--query',''])
run('bm25_no_term','ch06','bm25_NOT_RUN.py',['--query','不存在词项'])
run('bm25_empty_scope','ch06','bm25_NOT_RUN.py',['--year','1800'])
run('bm25_invalid_parameter','ch06','bm25_NOT_RUN.py',['--k1','-1'],1)
run('rrf','ch06','rrf_NOT_RUN.py')
run('rrf_unfilled','ch06','rrf_NOT_RUN.py',['--input','rankings_template.json'],1)
run('eval_dev','ch06','evaluate_NOT_RUN.py',['--split','development'])
run('eval_holdout','ch06','evaluate_NOT_RUN.py',['--split','holdout_exercise'])
run('catalog_normal','ch19','check_catalog_NOT_RUN.py',['--input','catalog_input.csv','--output',R/'catalog_normal.json'])
run('catalog_anomalies','ch19','check_catalog_NOT_RUN.py',['--input','catalog_anomalies.csv','--output',R/'catalog_anomalies.json'])
run('catalog_no_overwrite','ch19','check_catalog_NOT_RUN.py',['--input','catalog_input.csv','--output',R/'catalog_normal.json'],1)
run('population','ch20','calculate_population_NOT_RUN.py')
run('responses','ch21','check_response_NOT_RUN.py')
run('question_cards','ch22','inspect_question_cards_NOT_RUN.py')
run('source_chain','ch23','inspect_source_chain_NOT_RUN.py')
results.append({'name':'embedding_models','chapter':'ch06','script':'embedding_compare_NOT_RUN.py','status':'BLOCKED','reason':'No supplied local e5/bge model directory. No installation or model download authorized/performed.','sentence_transformers_installed':importlib.util.find_spec('sentence_transformers') is not None})
(R/'execution_results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2));print(json.dumps(results,ensure_ascii=False,indent=2))

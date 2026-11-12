from pathlib import Path
import json,csv,math
from fractions import Fraction
from collections import Counter,defaultdict
B=Path('/workspace/scratch/b06bda80e898/book_review_20261030');A=B/'revision/附件';R=B/'runs/ch05_06_19_23';checks=[]
def check(name,ok,detail):
 checks.append({'name':name,'pass':bool(ok),'detail':detail})
# Population rederived with rational arithmetic, independently of the Decimal program.
v={r['id']:int(r['value']) for r in csv.DictReader((A/'ch20/population_values.csv').open())}
pop=json.loads((R/'population.stdout').read_text())
exp={'Q_growth':Fraction(v['Q2020']-v['Q2010'],v['Q2010'])*100,'F_growth':Fraction(v['F2020']-v['F2010'],v['F2010'])*100,'share_change':(Fraction(v['Q2020'],v['F2020'])-Fraction(v['Q2010'],v['F2010']))*100,'rest_growth':Fraction((v['F2020']-v['Q2020'])-(v['F2010']-v['Q2010']),v['F2010']-v['Q2010'])*100}
actual=[pop['Q']['growth_pct'],pop['F']['growth_pct'],pop['calculated_change_percentage_points'],pop['rest_of_province']['growth_pct']]
check('population_rational',all(abs(float(a)-float(b))<1e-12 for a,b in zip(actual,exp.values())),{k:{'exact':str(v),'decimal':float(v)} for k,v in exp.items()})
# Recompute all BM25 query scores directly using corpus term counts.
corpus=json.loads((A/'ch06/corpus.json').read_text())['documents'];docs=[d for d in corpus if d['tokens']]
N=len(docs);mean=sum(len(d['tokens']) for d in docs)/N
out=json.loads((R/'bm25_queries.stdout').read_text());details=[]
for q in out['queries']:
 independent={}
 for d in docs:
  total=0
  for word in set(q['query_tokens']):
   tf=d['tokens'].count(word);df=sum(word in c['tokens'] for c in docs)
   if tf:total+=math.log((N+1)/(df+.5))*tf*2.2/(tf+1.2*(.25+.75*len(d['tokens'])/mean))
  if total:independent[d['id']]=total
 got={r['id']:r['score'] for r in q['results']}
 details.append({'query':q['id'],'pass':set(got)==set(independent) and all(abs(got[k]-independent[k])<1e-12 for k in got),'scores':independent})
check('bm25_independent_scores',all(x['pass'] for x in details),details)
# RRF using exact rationals on the set teaching rankings.
x=json.loads((A/'ch06/rrf_teaching_input.json').read_text());totals=defaultdict(Fraction)
for run in x['runs']:
 best={}
 for r in run['ranking']:best[r['id']]=max(best.get(r['id'],-float('inf')),r['score'])
 for i,(k,vv) in enumerate(sorted(best.items(),key=lambda r:(-r[1],r[0]))[:x['M']],1):totals[k]+=Fraction(1,x['c']+i)
r=json.loads((R/'rrf.stdout').read_text());check('rrf_exact',all(abs(z['score']-float(totals[z['id']]))<1e-15 for z in r['fused']),{k:str(v) for k,v in totals.items()})
# Metrics independently rederived from each returned list and source qrels.
qrels={q['id']:set(q['relevant_ids']) for q in json.loads((A/'ch06/evaluation_input.json').read_text())['questions']}
for split in ['dev','holdout']:
 z=json.loads((R/('eval_'+split+'.stdout')).read_text());calc=defaultdict(list)
 for row in z['rows']:
  rel=qrels[row['question_id']];hits=len(set(row['returned_ids'])&rel)
  if not rel:check(split+'_'+row['question_id']+'_'+row['method']+'_no_reference',row['r_at_k'] is None and row['rr_at_k'] is None,'No gold entries remain separate');continue
  p=Fraction(hits,z['k']);rc=Fraction(hits,len(rel));rr=next((Fraction(1,i) for i,key in enumerate(row['returned_ids'],1) if key in rel),Fraction(0))
  calc[row['method']].append((p,rc,rr))
 for method,rows in calc.items():
  means=[sum((r[j] for r in rows),Fraction(0))/len(rows) for j in range(3)]
  got=z['summary'][method]
  check(split+'_'+method+'_metrics',all(abs(float(v)-got[k])<1e-15 for v,k in zip(means,['mean_precision','mean_recall','mrr'])),[str(v) for v in means])
# Structural outputs must be inspected, not merely exit=0.
links=json.loads((R/'links.stdout').read_text());check('link_targets',all(x['exists'] for x in links['links']),len(links['links']))
normal=json.loads((R/'catalog_normal.json').read_text());check('catalog_normal',len(normal['rows'])==2 and all(not r['errors'] for r in normal['rows']),normal)
anom=json.loads((R/'catalog_anomalies.json').read_text());expected=[['duplicate_id'],['duplicate_id'],['missing:title_raw'],[]];check('catalog_anomalies',sorted(sorted(r['errors']) for r in anom['rows'])==sorted(expected),anom)
for name in ['responses_after','question_cards','source_chain']:
 z=json.loads((R/(name+'.stdout')).read_text()); ok= not any(r['structural_errors'] for r in z['rows']) if name=='responses_after' else not any(r['missing'] or r['duplicate_id'] for r in z['cards']) if name=='question_cards' else not z['cycles'] and not z['missing_references'];check(name,ok,z)
(R/'independent_checks.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2));print(json.dumps({'checks':len(checks),'failures':[x for x in checks if not x['pass']]},ensure_ascii=False))

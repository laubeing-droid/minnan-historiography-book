"""Standard-library regressions for the three 2026-11-12 promotions.
Run: python -B chapters/_shared/test_promoted.py
Only synthetic fixtures and a temporary directory; no manuscript writes.
"""
from pathlib import Path
import unittest,tempfile,subprocess,sys,json,importlib.util,copy
ROOT=Path(__file__).resolve().parents[2]
class PromotionTests(unittest.TestCase):
 def score(self,value):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d);(p/'p.json').write_text(json.dumps({'result':{'predictions':[{'id':'A','prediction':value}]}}));(p/'r.csv').write_text('id,gold\nA,1\n')
   return subprocess.run([sys.executable,'-B',str(ROOT/'chapters/ch08/code/score_predictions.py'),'--predictions',str(p/'p.json'),'--reference',str(p/'r.csv')],capture_output=True,text=True)
 def test_score_valid(self):
  for value in [1,'1']:self.assertEqual(self.score(value).returncode,0)
 def test_score_rejects_coercion(self):
  for value in [1.9,0.9,1.0,True,None,'01','1.0']:self.assertNotEqual(self.score(value).returncode,0)
 def test_cards(self):
  required=['id','question','materials','expected_gain','risk','evidence_that_changes_choice','next_step','decision']
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/'cards.json';cards=[]
   for i,v in enumerate([None,[],{},False,0,' ','valid']):
    c={k:'text' for k in required};c.update(id=str(i),question=v);cards.append(c)
   p.write_text(json.dumps({'cards':cards}));x=subprocess.run([sys.executable,'-B',str(ROOT/'chapters/ch22/code/inspect_question_cards.py'),'--input',str(p)],capture_output=True,text=True)
   self.assertEqual(x.returncode,0);out=json.loads(x.stdout)['cards']
   for row in out[:-1]:self.assertIn('question',row['missing'])
   self.assertEqual(out[-1]['missing'],[])
 def base(self):
  return {'sources':[{'id':'S'}],'names':[{'id':'N','name':'X','entity':'E','source':'S','start':1,'end':3,'parent':'P'}],'mentions':[{'id':'M','name':'X','year':2,'parent':'P'},{'id':'M2','name':'X','year':2,'parent':'P'}],'decisions':[{'id':'D','mention':'M','status':'confirmed','entity':'E'}]}
 def reconcile(self,d):
  spec=importlib.util.spec_from_file_location('promoted14',ROOT/'chapters/ch14/code/workflow.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m.reconcile(d)
 def test_current(self):self.assertEqual(len(self.reconcile(self.base())['current_decisions']),1)
 def test_valid_supersession(self):
  d=self.base();d['decisions'].append({'id':'D2','mention':'M','status':'confirmed','entity':'E','supersedes':'D'});self.assertEqual(self.reconcile(d)['current_decisions'][0]['id'],'D2')
 def test_reject_supersession(self):
  for variant in ['self','cross','cycle','missing']:
   d=self.base()
   if variant=='self':d['decisions'][0]['supersedes']='D'
   elif variant=='missing':d['decisions'][0]['supersedes']='absent'
   else:
    d['decisions'].append({'id':'D2','mention':'M2' if variant=='cross' else 'M','status':'confirmed','entity':'E','supersedes':'D'})
    if variant=='cycle':d['decisions'][0]['supersedes']='D2'
   with self.assertRaises(ValueError,msg=variant):self.reconcile(d)
if __name__=='__main__':unittest.main(verbosity=2)

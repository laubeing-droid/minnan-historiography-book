import csv, importlib.util, tempfile, unittest
from pathlib import Path
p=Path(__file__).with_name('reproduce_population.py')
spec=importlib.util.spec_from_file_location('population',p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
DATA=p.parents[1]/'data'
class PopulationTest(unittest.TestCase):
 def test_published_values(self):
  r=m.compute(m.read_population(DATA/'population.csv'))
  self.assertEqual(len(m.verify(r,DATA/'checks.csv')),4)
  self.assertGreater(m.D(r['Q']['increase']),0)
  self.assertLess(m.D(r['share_change_percentage_points']),0)
 def test_district_totals_without_double_counting(self):
  with (DATA/'district_checks.csv').open(encoding='utf-8',newline='') as f: rows=list(csv.DictReader(f))
  self.assertEqual(len(rows),11)
  self.assertEqual(len({r['region'] for r in rows}),11)
  v=m.read_population(DATA/'population.csv')
  for year in ('2010','2020'):
   self.assertEqual(sum(int(r['population_'+year]) for r in rows),v['Q'+year])
 def test_wrong_unit_rejected(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/'input.csv';p.write_text((DATA/'population.csv').read_text().replace(',人,',',万人,',1))
   with self.assertRaises(ValueError):m.read_population(p)
 def test_fractional_count_rejected(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/'input.csv';p.write_text((DATA/'population.csv').read_text().replace('8128530','8128530.9'))
   with self.assertRaises(ValueError):m.read_population(p)
 def test_duplicate_identity_rejected(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/'input.csv';p.write_text((DATA/'population.csv').read_text().replace('Q2020,2020,泉州','Q2010,2010,泉州'))
   with self.assertRaises(ValueError):m.read_population(p)
 def test_changed_input_fails_published_crosscheck(self):
  v=m.read_population(DATA/'population.csv');v['Q2020']+=1
  with self.assertRaises(ValueError):m.verify(m.compute(v),DATA/'checks.csv')
if __name__=='__main__':unittest.main()

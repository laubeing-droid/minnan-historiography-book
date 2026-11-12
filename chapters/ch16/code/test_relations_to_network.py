"""教学桥接边界测试；不改动源材料。"""
import csv
import shutil
import tempfile
import unittest
from pathlib import Path
from relations_to_network import ROOT, bridge

DATA = ROOT/'manuscript/附件/ch16'


class BridgeTests(unittest.TestCase):
    def test_duplicate_sources_count_one_event(self):
        r = bridge(DATA)
        self.assertEqual(r['roster'], ['P1', 'P2', 'P4'])
        self.assertEqual(len(r['events']), 1)
        self.assertEqual(r['events'][0]['event_id'], 'V2')
        evidence = next(x['evidence'] for x in r['lineage'] if x['instance_id'] == 'R5')
        self.assertEqual([x['assertion_id'] for x in evidence], ['C5', 'C11'])
        self.assertEqual(len({x['independent_group'] for x in evidence}), 1)
        self.assertEqual(r['metrics']['summary']['M'], 1)
        self.assertEqual(r['metrics']['summary']['isolates'], ['P4'])

    def test_no_coattendance_or_kinship_as_correspondence(self):
        r = bridge(DATA)
        self.assertEqual([x['instance_id'] for x in r['audit'] if x['included']], ['R5'])
        self.assertEqual(len(r['audit']), 12)

    def test_empty_window_preserves_roster(self):
        r = bridge(DATA, 1800, 1810)
        self.assertEqual(r['events'], [])
        self.assertEqual(r['metrics']['summary']['N'], 3)
        self.assertEqual(r['metrics']['summary']['M'], 0)

    def mutate(self, action):
        with tempfile.TemporaryDirectory() as d:
            target = Path(d)/'data'
            shutil.copytree(DATA, target)
            path = target/'assertions.csv'
            with path.open(encoding='utf-8', newline='') as f:
                reader = csv.DictReader(f); fields = reader.fieldnames; rows = list(reader)
            action(rows)
            with path.open('w', encoding='utf-8', newline='') as f:
                writer=csv.DictWriter(f, fieldnames=fields); writer.writeheader(); writer.writerows(rows)
            return bridge(target)

    def test_pending_cannot_be_promoted(self):
        def action(rows):
            for r in rows:
                if r['instance_id']=='R5': r['judgment']='pending'
        self.assertEqual(self.mutate(action)['events'], [])

    def test_unknown_endpoint_rejected(self):
        def action(rows): rows[0]['subject']='MISSING'
        with self.assertRaises(ValueError): self.mutate(action)

    def test_two_instances_same_event_rejected(self):
        def action(rows): rows[-3]['instance_id']='R5_duplicate'
        with self.assertRaises(ValueError): self.mutate(action)

    def test_reversed_window_rejected(self):
        with self.assertRaises(ValueError): bridge(DATA, 1800, 1700)


if __name__ == '__main__': unittest.main()

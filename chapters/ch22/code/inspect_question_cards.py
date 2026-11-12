#!/usr/bin/env python3
"""Promoted 2026-11-12 from manuscript/附件/ch22/inspect_question_cards_NOT_RUN.py.
Text schema checked on synthetic regression cases; not research value.
"""
from pathlib import Path
import json,argparse
parser=argparse.ArgumentParser();parser.add_argument('--input',required=True);args=parser.parse_args()
p=Path(args.input)
data=json.loads(p.read_text(encoding='utf-8'))
required=['id','question','materials','expected_gain','risk','evidence_that_changes_choice','next_step','decision']
seen=set();rows=[]
for card in data['cards']:
    missing=[k for k in required if not isinstance(card.get(k),str) or not card[k].strip()]
    key=card.get('id');duplicate=isinstance(key,str) and key in seen
    if isinstance(key,str):seen.add(key)
    rows.append({'id':card.get('id'),'missing':missing,'duplicate_id':duplicate})
print(json.dumps({'scope':'completeness only; no score or recommendation','cards':rows},ensure_ascii=False,indent=2))

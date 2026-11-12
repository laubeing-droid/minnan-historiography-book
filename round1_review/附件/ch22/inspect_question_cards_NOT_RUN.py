#!/usr/bin/env python3
"""NOT_RUN. Inspect card completeness, not research value."""
from pathlib import Path
import json
p=Path(__file__).resolve().parent/'question_cards.json'
data=json.loads(p.read_text(encoding='utf-8'))
required=['id','question','materials','expected_gain','risk','evidence_that_changes_choice','next_step','decision']
seen=set();rows=[]
for card in data['cards']:
    missing=[k for k in required if card.get(k) is None or (isinstance(card.get(k),str) and not card[k].strip()) or (isinstance(card.get(k),(list,dict)) and not card[k])]
    duplicate=card.get('id') in seen;seen.add(card.get('id'))
    rows.append({'id':card.get('id'),'missing':missing,'duplicate_id':duplicate})
print(json.dumps({'scope':'completeness only; no score or recommendation','cards':rows},ensure_ascii=False,indent=2))

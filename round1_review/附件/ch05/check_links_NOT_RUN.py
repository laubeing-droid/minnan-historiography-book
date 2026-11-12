#!/usr/bin/env python3
"""NOT_RUN. Check local Markdown links; never mutate or access the network."""
from pathlib import Path
from urllib.parse import unquote
import re, json
ROOT=Path(__file__).resolve().parent
reports=[]
for p in sorted(ROOT.glob('*.md')):
    for target in re.findall(r'\]\(([^)]+)\)',p.read_text(encoding='utf-8')):
        if re.match(r'^[a-zA-Z]+:', target) or target.startswith('#'): continue
        dest=(p.parent/unquote(target.split('#')[0])).resolve()
        reports.append({'file':p.name,'target':target,'exists':dest.exists()})
print(json.dumps({'scope':'file existence only','links':reports},ensure_ascii=False,indent=2))

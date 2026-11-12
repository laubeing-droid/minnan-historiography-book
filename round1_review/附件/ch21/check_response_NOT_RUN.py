#!/usr/bin/env python3
"""NOT_RUN. Check response IDs and file references only; no submission or substantive judgment."""
from pathlib import Path
import csv,json,re
root=Path(__file__).resolve().parent
with (root/'response_matrix.csv').open(encoding='utf-8',newline='') as f:rows=list(csv.DictReader(f))
seen=set();out=[]
for row in rows:
    errors=[];key=row['comment_id']
    if key in seen:errors.append('duplicate_comment_id')
    seen.add(key)
    for column in ('response_file','manuscript_file'):
        p=(root/row[column]).resolve()
        if p.parent!=root:errors.append('outside_package');continue
        if not p.is_file():errors.append('missing:'+column);continue
        if not re.search(r'(?<![A-Za-z0-9_])'+re.escape(row['change_id'])+r'(?![A-Za-z0-9_])',p.read_text(encoding='utf-8')):errors.append('missing_change_id:'+column)
    out.append({'comment_id':key,'change_id':row['change_id'],'structural_errors':errors})
print(json.dumps({'scope':'ID and path checks only','rows':out},ensure_ascii=False,indent=2))

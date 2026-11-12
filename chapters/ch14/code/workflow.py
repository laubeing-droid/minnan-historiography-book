#!/usr/bin/env python3
"""Promoted 2026-11-12 from manuscript/附件/ch14/workflow.py; synthetic tests only. Inputs read-only, fresh output directory required."""
import argparse, csv, hashlib, json, math
from pathlib import Path

def unique(rows):
 d={}
 for r in rows:
  if r['id'] in d: raise ValueError('duplicate id: '+r['id'])
  d[r['id']]=r
 return d

def number(x):
 if isinstance(x,bool) or not isinstance(x,(int,float)) or not math.isfinite(x): raise ValueError('nonfinite/non-numeric input')
 return x

def reconcile(d):
 names=unique(d['names']); mentions=unique(d['mentions']); decisions=unique(d['decisions']); sources=unique(d['sources'])
 rows=[]
 for m in mentions.values():
  for eid in sorted({n['entity'] for n in names.values() if n['name']==m['name']}):
   ns=[n for n in names.values() if n['name']==m['name'] and n['entity']==eid]
   checks=[]
   for n in ns:
    if n['source'] not in sources: raise ValueError('source reference')
    ts='unknown' if None in (m['year'],n['start'],n['end']) else ('pass' if n['start']<=m['year']<=n['end'] else 'conflict')
    ps='unknown' if m['parent'] is None or n['parent'] is None else ('pass' if m['parent']==n['parent'] else 'conflict')
    checks.append({'name_row':n['id'],'time':ts,'parent':ps,'retain':ts!='conflict' and ps!='conflict','source':n['source']})
   rows.append({'mention':m['id'],'entity':eid,'retained':any(c['retain'] for c in checks),'checks':checks})
 # Validate the supersession graph before any decision is suppressed.
 for j in decisions.values():
  if j['mention'] not in mentions: raise ValueError('unknown mention')
  target=j.get('supersedes')
  if target:
   if target not in decisions: raise ValueError('unknown superseded decision')
   if target==j['id']: raise ValueError('self supersession')
   if decisions[target]['mention']!=j['mention']: raise ValueError('cross-mention supersession')
 for start in decisions:
  seen=set(); cursor=start
  while cursor:
   if cursor in seen: raise ValueError('supersession cycle')
   seen.add(cursor); cursor=decisions[cursor].get('supersedes')
 current=[]
 superseded={j['supersedes'] for j in decisions.values() if j.get('supersedes')}
 for j in decisions.values():
  if j.get('supersedes') and j['supersedes'] not in decisions: raise ValueError('unknown superseded decision')
  if j['mention'] not in mentions: raise ValueError('unknown mention')
  if j['status']=='confirmed' and j['id'] not in superseded:
   if not any(r['mention']==j['mention'] and r['entity']==j['entity'] and r['retained'] for r in rows): raise ValueError('confirmation conflicts with candidates')
   if any(r['mention']==j['mention'] for r in current): raise ValueError('two current confirmations')
   current.append(j)
 return {'candidates':rows,'current_decisions':current,'unresolved':[m for m in mentions if not any(j['mention']==m for j in current)],'summary':{'mentions':len(mentions),'candidate_pairs':len(rows),'retained_pairs':sum(r['retained'] for r in rows),'confirmed':len(current)}}

def solve(A,b):
 a=[list(map(float,row))+[float(y)] for row,y in zip(A,b)];n=len(b)
 for i in range(n):
  p=max(range(i,n),key=lambda k:abs(a[k][i]))
  if abs(a[p][i])<1e-12:raise ValueError('singular normal matrix / collinear controls')
  a[i],a[p]=a[p],a[i];z=a[i][i];a[i]=[v/z for v in a[i]]
  for k in range(n):
   if k!=i:
    z=a[k][i];a[k]=[v-z*w for v,w in zip(a[k],a[i])]
 return [r[-1] for r in a]

def affine(d):
 if d['crs']!='LOCAL_TEACHING_METRE':raise ValueError('wrong CRS')
 unique(d['control']);unique(d['check']);out=[]
 for sc in d['scenarios']:
  ctrl=[dict(p) for p in d['control']]
  for p in ctrl:
   if p['id'] in sc['control_override']:p['x'],p['y']=sc['control_override'][p['id']]
  mu=sum(p['u'] for p in ctrl)/len(ctrl);mv=sum(p['v'] for p in ctrl)/len(ctrl)
  scale=max(max(p['u'] for p in ctrl)-min(p['u'] for p in ctrl),max(p['v'] for p in ctrl)-min(p['v'] for p in ctrl))
  if len(ctrl)<3 or scale<=0:raise ValueError('insufficient controls')
  design=[[1,(p['u']-mu)/scale,(p['v']-mv)/scale] for p in ctrl]
  A=[[sum(r[i]*r[j] for r in design) for j in range(3)] for i in range(3)]
  coef={}
  for key in ['x','y']:
   b=[sum(r[i]*p[key] for r,p in zip(design,ctrl)) for i in range(3)]
   q=solve(A,b);coef[key]=[q[0]-q[1]*mu/scale-q[2]*mv/scale,q[1]/scale,q[2]/scale]
  inv_cols=[solve(A,[int(i==j) for i in range(3)]) for j in range(3)]
  normA=max(sum(abs(v) for v in r) for r in A)
  norminv=max(sum(abs(inv_cols[j][i]) for j in range(3)) for i in range(3))
  errors=[]
  for kind,points in [('fit',ctrl),('check',d['check'])]:
   for p in points:
    x=sum(v*w for v,w in zip(coef['x'],[1,p['u'],p['v']]));y=sum(v*w for v,w in zip(coef['y'],[1,p['u'],p['v']]))
    errors.append({'id':p['id'],'role':kind,'pred_x':x,'pred_y':y,'dx':x-p['x'],'dy':y-p['y'],'distance':math.hypot(x-p['x'],y-p['y'])})
  out.append({'scenario':sc['name'],'coefficients':coef,'normal_matrix_condition_inf':normA*norminv,'errors':errors,'rmse_check':math.sqrt(sum(p['distance']**2 for p in errors if p['role']=='check')/len(d['check']))})
 return {'scenarios':out,'method':'centered-scaled normal equations; small teaching example only, not general GIS raster georeferencing'}

def cross(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def on(a,b,p):return cross(a,b,p)==0 and min(a[0],b[0])<=p[0]<=max(a[0],b[0]) and min(a[1],b[1])<=p[1]<=max(a[1],b[1])
def intersect(a,b,c,e):
 x,y,z,w=cross(a,b,c),cross(a,b,e),cross(c,e,a),cross(c,e,b)
 return (x*y<0 and z*w<0) or on(a,b,c) or on(a,b,e) or on(c,e,a) or on(c,e,b)
def geometry(d):
 if d['crs']!='LOCAL_TEACHING_METRE' or d['unit']!='metre':raise ValueError('CRS/unit mismatch')
 unique(d['features']);out=[]
 for f in d['features']:
  r={'id':f['id'],'type':f['type'],'status':'accepted','length':None,'area':None}
  try:
   c=f['coordinates'];typ=f['type']
   if c is None:raise ValueError('unknown geometry')
   pts=[c] if typ=='Point' else c
   if not pts:raise ValueError('empty geometry')
   for p in pts:
    if len(p)!=2 or any(type(v)!=int or not d['limit'][0]<=v<=d['limit'][1] for v in p):raise ValueError('requires bounded integer 2D coordinates')
   if typ not in ('Point','LineString','Polygon'):raise ValueError('unsupported type')
   if typ!='Point':
    closed=typ=='Polygon'
    if len(pts)<(4 if closed else 2):raise ValueError('too few points')
    if closed and pts[0]!=pts[-1]:raise ValueError('unclosed ring')
    core=pts[:-1] if closed else pts
    if len({tuple(p) for p in core})!=len(core):raise ValueError('repeated node')
    seg=list(zip(pts,pts[1:]))
    for i,(a,b) in enumerate(seg):
     if a==b:raise ValueError('zero length edge')
     for j,(c,e) in enumerate(seg):
      if j<=i:continue
      adjacent=j==i+1 or (closed and i==0 and j==len(seg)-1)
      if not adjacent and intersect(a,b,c,e):raise ValueError('self intersection/contact')
      if adjacent:
       shared=set(map(tuple,[a,b])) & set(map(tuple,[c,e]))
       if len(shared)!=1:raise ValueError('invalid adjacent edges')
       shared=list(shared)[0];other1=a if tuple(a)!=shared else b;other2=c if tuple(c)!=shared else e
       if cross(shared,other1,other2)==0 and sum((other1[k]-shared[k])*(other2[k]-shared[k]) for k in (0,1))>0:raise ValueError('backtracking edge')
    if closed:
     r['area']=abs(sum(a[0]*b[1]-b[0]*a[1] for a,b in seg))/2
     if r['area']==0:raise ValueError('zero area')
    else:r['length']=sum(math.dist(a,b) for a,b in seg)
  except (ValueError,TypeError) as e:r.update(status='rejected',reason=str(e),length=None,area=None)
  out.append(r)
 points={f['id']:f['coordinates'] for f in d['features'] if f['type']=='Point' and any(r['id']==f['id'] and r['status']=='accepted' for r in out)}
 return {'features':out,'P1_P2_distance':math.dist(points['P1'],points['P2']) if {'P1','P2'}<=points.keys() else None}

def contains(rect,x,y):return rect[0]<=x<=rect[2] and rect[1]<=y<=rect[3]
def boundaries(d):
 ps=unique(d['periods']);vs=unique(d['versions']);es=unique(d['events']);rows=[];layers=[]
 for v in vs.values():
  if v['start']>=v['end'] or v['rect'][0]>=v['rect'][2] or v['rect'][1]>=v['rect'][3]:raise ValueError('invalid interval/rectangle')
 for cutoff in d['cutoffs']:
  for p in ps.values():
   eligible=[v for v in vs.values() if v['known_at']<=cutoff and v['start']<=p['start'] and v['end']>=p['end']]
   layers.append({'known_at':cutoff,'period':p['id'],'versions':eligible})
  for e in es.values():
   r={'event':e['id'],'known_at':cutoff,'periods':[],'versions':[]}
   if e['start'] is None or e['end'] is None:r['status']='unknown_time'
   else:
    if e['start']>=e['end']:raise ValueError('invalid event interval')
    overlaps=[p['id'] for p in ps.values() if e['start']<p['end'] and e['end']>p['start']]
    full=[p for p in ps.values() if p['start']<=e['start'] and e['end']<=p['end']]
    r['periods']=overlaps
    if len(full)!=1:r['status']='cross_period' if overlaps else 'outside_periods'
    else:
     p=full[0];r['versions']=[v['id'] for v in vs.values() if v['known_at']<=cutoff and v['start']<=p['start'] and v['end']>=p['end'] and contains(v['rect'],e['x'],e['y'])]
     r['status']='matched' if len(r['versions'])==1 else ('conflict' if r['versions'] else 'unknown_space')
   # Incorrect last-period assignment is retained separately, never used as result.
   last=max(ps.values(),key=lambda p:p['start'])
   r['wrong_last_period_versions']=[v['id'] for v in vs.values() if e['start'] is not None and v['known_at']<=cutoff and v['start']<=last['start'] and v['end']>=last['end'] and contains(v['rect'],e['x'],e['y'])]
   rows.append(r)
 return {'assignments':rows,'period_layers':layers}

def uncertainty(d):
 ps=unique(d['positions']);ref=d['reference'];rows=[]
 for p in ps.values():
  chain=set();q=p
  while q.get('supersedes'):
   if q['id'] in chain:raise ValueError('revision cycle')
   chain.add(q['id']);q=ps[q['supersedes']]
  kind=p['kind'];lo=hi=None
  if kind in ('point','circle'):
   dis=math.dist(ref,p['point']);r=number(p.get('radius',0))
   if r<0:raise ValueError('negative radius')
   lo=max(0,dis-r);hi=dis+r
  elif kind=='candidates':
   if not p['points']:raise ValueError('empty candidate set')
   ds=[math.dist(ref,z) for z in p['points']];lo=min(ds);hi=max(ds)
  elif kind=='rectangle':
   x1,y1,x2,y2=p['rect'];x,y=ref
   if x1>x2 or y1>y2:raise ValueError('reversed rectangle')
   lo=math.hypot(max(x1-x,0,x-x2),max(y1-y,0,y-y2));hi=max(math.dist(ref,z) for z in [(x1,y1),(x1,y2),(x2,y1),(x2,y2)])
  elif kind!='unknown':raise ValueError('unknown position kind')
  for t in d['thresholds']:
   rows.append({'position':p['id'],'place':p['place'],'threshold':t,'minimum':lo,'maximum':hi,'status':'unknown' if lo is None else ('all_inside' if hi<=t else ('all_outside' if lo>t else 'mixed')),'evidence':p['evidence']})
 return {'distance_bounds':rows,'probabilities_assumed':False}

def main():
 a=argparse.ArgumentParser();a.add_argument('--section',type=int,choices=range(1,6),required=True);a.add_argument('--input',default='input.json');a.add_argument('--out',required=True);args=a.parse_args()
 raw=Path(args.input).read_bytes();d=json.loads(raw);out=Path(args.out);out.mkdir(parents=True,exist_ok=False)
 try:
  if not d.get('fiction'):raise ValueError('this teaching workflow requires explicit fiction flag')
  result=[reconcile,affine,geometry,boundaries,uncertainty][args.section-1](d)
  (out/'result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2,allow_nan=False),encoding='utf8')
  for name,rows in result.items():
   if isinstance(rows,list) and rows and all(isinstance(r,dict) for r in rows):
    keys=sorted(set().union(*(r.keys() for r in rows)))
    with (out/(name+'.csv')).open('x',encoding='utf-8-sig',newline='') as f:
     w=csv.DictWriter(f,keys);w.writeheader();w.writerows({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(list,dict)) else v for k,v in r.items()} for r in rows)
  status={'status':'EXECUTED_BY_READER','input_sha256':hashlib.sha256(raw).hexdigest(),'section':args.section}
 except Exception as e:
  (out/'failure.json').write_text(json.dumps({'status':'FAILED','error':repr(e)},ensure_ascii=False),encoding='utf8');raise
 (out/'run_manifest.json').write_text(json.dumps(status,indent=2),encoding='utf8')
if __name__=='__main__':main()

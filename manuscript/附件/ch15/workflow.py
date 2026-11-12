#!/usr/bin/env python3
"""新编教学附件 NOT_RUN；标准库；只读输入，拒绝覆盖输出目录。"""
import argparse,csv,hashlib,heapq,itertools,json,math
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path

def unique(rows):
 d={}
 for r in rows:
  if r['id'] in d:raise ValueError('duplicate id '+r['id'])
  d[r['id']]=r
 return d

def ratio(a,b):return a/b if a is not None and b is not None and b>0 else None
def distribution(d):
 regions=unique(d['regions']);sites=unique(d['sites']);records=unique(d['records']);a,b=d['window'];ev={};logs=[]
 for r in records.values():
  if r['site'] not in sites:raise ValueError('missing site')
  if r['status']=='confirmed':
   if not r['event'] or r['year'] is None:raise ValueError('confirmed event missing identity/year')
   identity=(r['site'],r['year'])
   if r['event'] in ev and ev[r['event']]!=identity:raise ValueError('conflicting testimony for event')
   ev[r['event']]=identity
 accepted=defaultdict(set);recnum=defaultdict(int);unresolved=defaultdict(int);site_ids=defaultdict(set)
 for r in records.values():
  s=sites[r['site']];rs=[x for x in regions.values() if x['rect'][0]<=s['x']<x['rect'][2] and x['rect'][1]<=s['y']<x['rect'][3]]
  if len(rs)!=1:reason='ambiguous_or_outside_region'
  elif r['year'] is None:reason='unknown_date'
  elif not a<=r['year']<=b:reason='outside_window'
  elif not(s['start']<=a and s['end']>=b):reason='invalid_site_period'
  elif not(rs[0]['start']<=a and rs[0]['end']>=b):reason='invalid_region_period'
  elif not rs[0]['covered']:reason='no_coverage'
  elif r['status']!='confirmed':reason='unresolved';unresolved[rs[0]['id']]+=1
  else:
   reason='accepted';rid=rs[0]['id'];accepted[rid].add(r['event']);site_ids[rid].add(r['site']);recnum[rid]+=1
  logs.append({'record':r['id'],'event':r['event'],'status':reason,'regions':[x['id'] for x in rs]})
 rows=[]
 for r in regions.values():
  n=len(accepted[r['id']]) if r['covered'] else None;o=r['opportunities']
  if o is not None and (isinstance(o,bool) or o<0):raise ValueError('invalid opportunity denominator')
  rows.append({'region':r['id'],'covered':r['covered'],'events':n,'valid_records':recnum[r['id']] if r['covered'] else None,'sites':len(site_ids[r['id']]) if r['covered'] else None,'opportunities':o,'event_per_opportunity':ratio(n,o),'unresolved':unresolved[r['id']]})
 return {'regions':rows,'audit_log':logs,'distinct_events':[{'event':e,'site':s,'year':y} for e,(s,y) in ev.items()]}

def access(d):
 ns=unique(d['nodes']);es=unique(d['edges']);rows=[];excluded=[]
 if d['crs']!='LOCAL_METRE_PLANE':raise ValueError('unsupported CRS')
 for n in ns.values():
  if any(not isinstance(n[k],(float,int)) or not math.isfinite(n[k]) or abs(n[k])>10000 for k in ('x','y')):raise ValueError('coordinate range')
 for e in es.values():
  if e['from'] not in ns or e['to'] not in ns:raise ValueError('missing endpoint')
  if e['minutes'] is not None and (type(e['minutes'])!=int or not 0<=e['minutes']<=1000000):raise ValueError('bounded nonnegative integer cost required')
 def shortest(source,valid):
  # Fixed settled nodes and strictly better updates guarantee termination even with zero-cost cycles.
  dist={source:0};paths={source:[]};visited=set();heap=[(0,source)]
  while heap:
   cost,u=heapq.heappop(heap)
   if u in visited:continue
   visited.add(u)
   for e in sorted((e for e in valid if e['from']==u),key=lambda e:e['id']):
    v=e['to'];nd=cost+e['minutes']
    if v not in visited and (v not in dist or nd<dist[v]):dist[v]=nd;paths[v]=paths[u]+[e['id']];heapq.heappush(heap,(nd,v))
  return dist,paths
 for t in d['times']:
  valid=[]
  for e in es.values():
   reason='inactive' if not e['active'] else ('outside_period' if not e['start']<=t<=e['end'] else ('unknown_cost' if e['minutes'] is None else None))
   if reason:excluded.append({'time':t,'edge':e['id'],'reason':reason})
   else:valid.append(e)
  cache={s:shortest(s,valid) for s in ns}
  for source in ns:
   dist,paths=cache[source]
   for target,n in ns.items():
    dis=math.hypot(ns[source]['x']-n['x'],ns[source]['y']-n['y']);r=ns[source]['radius']+n['radius'];lo=max(0,dis-r);hi=dis+r
    rows.append({'time':t,'source':source,'target':target,'straight_metres':dis,'minutes':dist.get(target),'path':paths.get(target,[]),'status':'reachable' if target in dist else 'unreachable_in_known_edges','distance_min':lo,'distance_max':hi,'threshold_status':'inside' if hi<=d['threshold'] else ('outside' if lo>d['threshold'] else 'uncertain')})
  for target in ns:
   choices=[(cache[s][0][target],s,cache[s][1][target]) for s in d['sources'] if target in cache[s][0]]
   best=min(choices) if choices else (None,None,[])
   rows.append({'time':t,'source':'MULTI','target':target,'minutes':best[0],'selected_source':best[1],'path':best[2]})
 adj=[]
 for a,b in itertools.combinations(sorted(d['rectangles']),2):
  x=d['rectangles'][a];y=d['rectangles'][b];dx=min(x[2],y[2])-max(x[0],y[0]);dy=min(x[3],y[3])-max(x[1],y[1])
  if dx>0 and dy>0:raise ValueError('overlapping rectangles not supported')
  queen=dx>=0 and dy>=0;rook=queen and ((dx>0 and dy==0) or (dy>0 and dx==0));adj.append({'a':a,'b':b,'rook':rook,'queen':queen})
 return {'paths':rows,'excluded_edges':excluded,'adjacency':adj,'tie_rule':'strictly better distance; heap by node id; outgoing edges by edge id; one representative only'}

def moran_values(vals,edges):
 n=len(vals)
 if n<2 or not edges:return None,'no_weights_or_too_few_regions'
 if any(v is None for v in vals):return None,'missing_attribute'
 vals=list(map(F,vals));mean=sum(vals)/n;z=[v-mean for v in vals];den=sum(v*v for v in z)
 if den==0:return None,'constant_attribute'
 return F(n,2*len(edges))*sum(2*z[i]*z[j] for i,j in edges)/den,'defined'
def spatial(d):
 rs=unique(d['regions']);ids=list(rs);n=len(ids)
 if not 2<=n<=8:raise ValueError('requires 2..8 regions for exact enumeration')
 edges=[];seen=set()
 for a,b in d['edges']:
  if a not in rs or b not in rs or a==b:raise ValueError('bad neighbor reference')
  key=tuple(sorted((a,b)))
  if key in seen:raise ValueError('duplicate edge')
  seen.add(key);edges.append((ids.index(a),ids.index(b)))
 rows=[]
 for r in rs.values():
  x1,y1,x2,y2=r['rect'];area=(x2-x1)*(y2-y1)/1000000
  if area<=0 or r['events']<0 or r['opportunities']<0:raise ValueError('invalid denominator or counts')
  rows.append({'id':r['id'],'area_km2':area,'events':r['events'],'density':r['events']/area,'opportunities':r['opportunities'],'rate':ratio(r['events'],r['opportunities'])})
 vals=[r['events'] for r in rs.values()];obs,status=moran_values(vals,edges);perms=[];group_perms=[]
 if obs is not None:
  for perm in itertools.permutations(range(n)):
   v,_=moran_values([vals[i] for i in perm],edges);perms.append({'permutation':perm,'I':str(v),'at_least_observed':v>=obs})
  groups=defaultdict(list)
  for i,r in enumerate(rs.values()):groups[r['group']].append(i)
  for gp in itertools.product(*(list(itertools.permutations(indices)) for indices in groups.values())):
   new=vals[:]
   for indices,perm in zip(groups.values(),gp):
    for i,j in zip(indices,perm):new[i]=vals[j]
   v,_=moran_values(new,edges);group_perms.append({'values':new,'I':str(v),'at_least_observed':v>=obs})
 rate,rate_status=moran_values([F(r['events'],r['opportunities']) if r['opportunities'] else None for r in rs.values()],edges)
 return {'regions':rows,'global':{'I':str(obs) if obs is not None else None,'status':status,'exact_upper_tail':sum(x['at_least_observed'] for x in perms)/len(perms) if perms else None,'opportunity_I':str(rate) if rate is not None else None,'opportunity_status':rate_status,'within_group_upper_tail':sum(x['at_least_observed'] for x in group_perms)/len(group_perms) if group_perms else None,'group_reference_degenerate':len({p['I'] for p in group_perms})==1 if group_perms else None},'permutations':perms,'within_group_permutations':group_perms}

def compare(d):
 if any(w<0 for w in d['weights'].values()) or abs(sum(d['weights'].values())-1)>1e-12:raise ValueError('weights must sum to 1')
 index={};cells=[]
 for c in d['cells']:
  key=(c['region'],c['period'],c['stratum'])
  if key in index or c['period'] not in d['windows'] or c['stratum'] not in d['weights']:raise ValueError('duplicate or undefined cell')
  if c['events'] is not None and c['events']<0:raise ValueError('negative count')
  rate=ratio(c['events'],c['opportunities']) if c['covered'] else None;index[key]=dict(c,rate=rate);cells.append(index[key])
 rows=[]
 for r,t in sorted({(c['region'],c['period']) for c in cells}):
  group=[index.get((r,t,s)) for s in d['weights']]
  full=all(c and c['covered'] and c['events'] is not None and c['opportunities'] is not None for c in group)
  weighted=all(index.get((r,t,s)) and index[(r,t,s)]['rate'] is not None for s,w in d['weights'].items() if w>0)
  rows.append({'region':r,'period':t,'events':sum(c['events'] for c in group) if full else None,'opportunities':sum(c['opportunities'] for c in group) if full else None,'raw_rate':ratio(sum(c['events'] for c in group),sum(c['opportunities'] for c in group)) if full else None,'standardized_rate':sum(w*index[(r,t,s)]['rate'] for s,w in d['weights'].items() if w>0) if weighted else None})
 changes=[]
 periods=sorted(d['windows'],key=lambda t:d['windows'][t][0])
 for r in sorted({c['region'] for c in cells}):
  if len(periods)!=2:continue
  old=next(x for x in rows if x['region']==r and x['period']==periods[0]);new=next(x for x in rows if x['region']==r and x['period']==periods[1]);z={'region':r}
  for k in ['raw_rate','standardized_rate']:z[k+'_change']=new[k]-old[k] if old[k] is not None and new[k] is not None else None
  changes.append(z)
 return {'strata':cells,'regional':rows,'changes':changes,'causal_estimate':None}

def sensitivity(d):
 unique(d['events']);joint=[];ranges=[]
 def cell(p):
  x,y=p
  if not(0<=x<2000 and 0<=y<2000):raise ValueError('point outside half-open frame')
  return ('A' if x<1000 else 'B') if y<1000 else ('C' if x<1000 else 'D')
 for zname,zones in d['zones'].items():
  flattened=[c for cs in zones.values() for c in cs]
  if sorted(flattened)!=['A','B','C','D']:raise ValueError('partition must contain every cell exactly once')
  lookup={c:z for z,cs in zones.items() for c in cs}
  for w,(a,b) in d['windows'].items():
   events=[e for e in d['events'] if a<=e['year']<=b]
   for version in ['fine','coarse']:
    known=[e for e in events if e[version]];unknown=[e['id'] for e in events if not e[version]]
    configs=list(itertools.product(*(e[version] for e in known)))
    if len(configs)>10000:raise ValueError('teaching enumeration limit')
    collected=defaultdict(list)
    for k,positions in enumerate(configs):
     counts={z:0 for z in zones};assignment={}
     for e,p in zip(known,positions):zone=lookup[cell(p)];counts[zone]+=1;assignment[e['id']]=zone
     for z,cs in zones.items():
      covered=all(d['covered'][c] for c in cs);opp=sum(d['opportunities'][w][c] for c in cs);value=counts[z] if covered else None;rate=ratio(value,opp)
      row={'partition':zname,'window':w,'location_version':version,'configuration':k,'zone':z,'observed_located_count':counts[z],'complete_count':value,'opportunities':opp,'covered':covered,'rate':rate,'unlocated':unknown,'assignment':assignment};joint.append(row);collected[z].append(row)
    for z,rows in collected.items():
     vals=[r['complete_count'] for r in rows];rates=[r['rate'] for r in rows]
     ranges.append({'partition':zname,'window':w,'location_version':version,'zone':z,'configurations':len(configs),'count_min':min(vals) if all(v is not None for v in vals) else None,'count_max':max(vals) if all(v is not None for v in vals) else None,'rate_min':min(rates) if all(v is not None for v in rates) else None,'rate_max':max(rates) if all(v is not None for v in rates) else None,'unlocated':unknown})
 return {'sensitivity_ranges':ranges,'joint_configurations':joint,'probabilities_assumed':False}

def interpretation(d):
 cards=unique(d['cards']);hs=unique(d['hypotheses']);roots={}
 def root(i,path=()):
  if i in path:raise ValueError('source dependency cycle')
  if i not in cards:raise ValueError('unknown source')
  c=cards[i]
  if not c['depends_on']:return {i}
  return set().union(*(root(j,path+(i,)) for j in c['depends_on']))
 for c in cards.values():
  if c['written'] not in (0,1,2) or c['narrated'] not in (0,1,2) or not c['text'] or not c['locator']:raise ValueError('invalid teaching time or missing evidence')
  roots[c['id']]=sorted(root(c['id']))
 rows=[]
 for h in hs.values():
  if not h['needed']:raise ValueError('record unanswered questions explicitly')
  families=sorted(set().union(*(set(roots[i]) for i in h['cards'])))
  rows.append(dict(h,source_families=families,family_count=len(families),causal_score=None))
 return {'timeline':[dict(c,source_roots=roots[c['id']]) for c in sorted(cards.values(),key=lambda c:(c['narrated'],c['written'],c['id']))],'interpretations':rows,'warning':'family count is not credibility or independent probability'}

def main():
 p=argparse.ArgumentParser();p.add_argument('--section',type=int,choices=range(1,7),required=True);p.add_argument('--input',default='input.json');p.add_argument('--out',required=True);a=p.parse_args();raw=Path(a.input).read_bytes();d=json.loads(raw);out=Path(a.out);out.mkdir(parents=True,exist_ok=False)
 try:
  if not d.get('fiction'):raise ValueError('explicit fiction flag required')
  result=[distribution,access,spatial,compare,sensitivity,interpretation][a.section-1](d)
  (out/'result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2,allow_nan=False),encoding='utf8')
  for name,rows in result.items():
   if isinstance(rows,list) and rows and all(isinstance(r,dict) for r in rows):
    keys=sorted(set().union(*(r.keys() for r in rows)))
    with (out/(name+'.csv')).open('x',encoding='utf-8-sig',newline='') as f:
     w=csv.DictWriter(f,keys);w.writeheader();w.writerows({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(list,dict)) else v for k,v in r.items()} for r in rows)
  (out/'run_manifest.json').write_text(json.dumps({'status':'EXECUTED_BY_READER','section':a.section,'input_sha256':hashlib.sha256(raw).hexdigest()},indent=2),encoding='utf8')
 except Exception as e:
  (out/'failure.json').write_text(json.dumps({'status':'FAILED','error':repr(e)},ensure_ascii=False),encoding='utf8');raise
if __name__=='__main__':main()

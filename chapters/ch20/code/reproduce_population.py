#!/usr/bin/env python3
"""Reproduce a bounded public-census comparison; no network or third-party packages."""
import argparse, csv, hashlib, json
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

D=Decimal

def read_population(path):
    with path.open(encoding='utf-8',newline='') as f: rows=list(csv.DictReader(f))
    expected={'Q2010':('2010','泉州'),'Q2020':('2020','泉州'),
              'F2010':('2010','福建'),'F2020':('2020','福建')}
    if len(rows)!=4 or {r['id'] for r in rows}!=set(expected):
        raise ValueError('exactly four unique observations are required')
    values={}
    for row in rows:
        if (row['year'],row['region'])!=expected[row['id']] or row['unit']!='人':
            raise ValueError('identity or unit mismatch')
        raw=row['population']
        if not raw.isascii() or not raw.isdigit() or int(raw)<=0:
            raise ValueError('population must be a positive integer')
        values[row['id']]=D(raw)
    if any(values[f'Q{y}']>=values[f'F{y}'] for y in (2010,2020)):
        raise ValueError('city must be smaller than province')
    return values

def compute(v):
    def row(a,b):return {'increase':str(b-a),'growth_pct':str((b-a)/a*100)}
    shares={str(y):v[f'Q{y}']/v[f'F{y}']*100 for y in (2010,2020)}
    return {'Q':row(v['Q2010'],v['Q2020']),'F':row(v['F2010'],v['F2020']),
            'shares_pct':{k:str(n) for k,n in shares.items()},
            'share_change_percentage_points':str(shares['2020']-shares['2010']),
            'rest_of_province':row(v['F2010']-v['Q2010'],v['F2020']-v['Q2020'])}

def verify(result,path):
    with path.open(encoding='utf-8',newline='') as f: rows=list(csv.DictReader(f))
    if len(rows)!=4 or {r['id'] for r in rows}!={'Q_increase','F_increase','Q_share_2010','Q_share_2020'}:
        raise ValueError('four published cross-checks required')
    if any(r['unit'] != ('人' if r['id'].endswith('increase') else '百分比') for r in rows):
        raise ValueError('published cross-check unit mismatch')
    checks={r['id']:D(r['value']) for r in rows}
    passed=[]
    for region in ('Q','F'):
        key=region+'_increase'
        if D(result[region]['increase'])!=checks[key]:raise ValueError(key+' disagrees with bulletin')
        passed.append(key)
    for year in ('2010','2020'):
        key='Q_share_'+year
        if D(result['shares_pct'][year]).quantize(D('.01'),rounding=ROUND_HALF_UP)!=checks[key]:
            raise ValueError(key+' rounding disagrees with bulletin')
        passed.append(key)
    return passed

def svg(v,out):
    # Two independent zero-based panels; there are no invented annual observations.
    bars=[]
    for panel,(title,unit,nums,maximum) in enumerate([
        ('Quanzhou resident population','million persons',[v['Q2010']/1000000,v['Q2020']/1000000],10),
        ('Quanzhou share of Fujian','percent',[v['Q2010']/v['F2010']*100,v['Q2020']/v['F2020']*100],25)]):
        x0=35+panel*410
        bars.append(f'<text x="{x0}" y="30">{title}</text><text x="{x0}" y="53" font-size="12">{unit}; zero baseline</text>')
        for tick in range(6):
            y=270-tick*36; label=maximum*tick/5
            bars.append(f'<line x1="{x0+30}" x2="{x0+355}" y1="{y}" y2="{y}" stroke="#ddd"/><text x="{x0}" y="{y+4}" font-size="12">{label:g}</text>')
        for i,n in enumerate(nums):
            h=float(n)/maximum*180;x=x0+85+i*135
            bars.append(f'<rect x="{x}" y="{270-h}" width="65" height="{h}" fill="#284b63"/><text x="{x}" y="{260-h}" font-size="12">{n:.4f}</text><text x="{x}" y="295">{2010+i*10}</text>')
    out.write_text('<svg xmlns="http://www.w3.org/2000/svg" width="850" height="355" viewBox="0 0 850 355"><rect width="850" height="355" fill="white"/><g font-family="sans-serif" font-size="15">'+''.join(bars)+'<text x="35" y="330" font-size="12">Sources: Quanzhou 2010 and Fujian 2020 census bulletins. Two endpoints, not an annual trend.</text></g></svg>\n',encoding='utf-8')

def main():
    root=Path(__file__).resolve().parents[1]
    p=argparse.ArgumentParser();p.add_argument('--data',type=Path,default=root/'data');p.add_argument('--out',type=Path,required=True);a=p.parse_args()
    # Read and validate all inputs before creating outputs.
    v=read_population(a.data/'population.csv');result=compute(v);passed=verify(result,a.data/'checks.csv')
    result['checks_passed']=passed
    result['limits']='Published counts comparison; no annual path, migration decomposition, or cultural-change conclusion.'
    result['inputs_sha256']={name:hashlib.sha256((a.data/name).read_bytes()).hexdigest() for name in ('population.csv','checks.csv','sources.json')}
    a.out.mkdir(parents=True,exist_ok=True)
    (a.out/'calculation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    svg(v,a.out/'population.svg')
    print('PASS: four bulletin cross-checks; calculation.json and population.svg written')

if __name__=='__main__':main()

#!/usr/bin/env python3
"""Locally exercised teaching implementation; see EXECUTION_STATUS.json.
Execution checks do not validate historical claims or execute model calls.
Only reads the requested local JSON and PGM files and prints JSON to stdout.
No model, network, dependency install, external command, deletion or overwrite.
Examples are synthetic. Do not cite outputs as historical findings.
"""
import argparse, collections, csv, json, math, random, sys
from pathlib import Path


def div(a,b):
    return a/b if b else None


def unique(rows,key):
    vals=[r[key] for r in rows]
    if len(vals)!=len(set(vals)):
        raise ValueError('duplicate '+key)
    return vals


def binary_metrics(gold,pred):
    if len(gold)!=len(pred): raise ValueError('unaligned rows')
    if not set(gold+pred)<= {0,1}: raise ValueError('binary values must be 0 or 1')
    tp=sum(g==1 and p==1 for g,p in zip(gold,pred))
    fp=sum(g==0 and p==1 for g,p in zip(gold,pred))
    fn=sum(g==1 and p==0 for g,p in zip(gold,pred))
    tn=sum(g==0 and p==0 for g,p in zip(gold,pred))
    return dict(n=len(gold),tp=tp,fp=fp,fn=fn,tn=tn,accuracy=div(tp+tn,len(gold)),precision=div(tp,tp+fp),recall=div(tp,tp+fn),f1=div(2*tp,2*tp+fp+fn))


def rule(text,expand=False,negate=False):
    words=['停讲']+(['罢讲'] if expand else [])
    hit=any(w in text for w in words)
    # A literal teaching rule, not a general Chinese negation parser.
    excluded=negate and any(w in text for w in ['未停讲','拟停讲','议停讲'])
    return int(hit and not excluded)


def rule_result(rows,expand=False,negate=False):
    pred=[rule(r['text'],expand,negate) for r in rows]
    return {'rows':[dict(id=r['id'],prediction=p,gold=r['gold']) for r,p in zip(rows,pred)],'metrics':binary_metrics([r['gold'] for r in rows],pred)}


def agreement(rows):
    n=len(rows)
    if not n: return {'n':0,'agreement':None,'kappa':None}
    a=collections.Counter(r['a'] for r in rows); b=collections.Counter(r['b'] for r in rows)
    po=sum(r['a']==r['b'] for r in rows)/n
    pe=sum(a[x]*b[x] for x in a.keys()|b.keys())/(n*n)
    return {'n':n,'agreement':po,'expected_agreement':pe,'kappa':div(po-pe,1-pe),'disagreements':[r for r in rows if r['a']!=r['b']]}


def coverage(rows):
    result=[]
    for r in rows:
        if not 0<=r['correct']<=r['evaluated']<=r['readable']<=r['available']: raise ValueError('invalid coverage funnel')
        result.append(dict(r,readable_fraction=div(r['readable'],r['available']),evaluation_coverage=div(r['evaluated'],r['available']),accuracy=div(r['correct'],r['evaluated'])))
    return result


def split_groups(rows,keys):
    parent=list(range(len(rows)))
    def root(i):
        while parent[i]!=i:
            parent[i]=parent[parent[i]];i=parent[i]
        return i
    for key in keys:
        seen={}
        for i,r in enumerate(rows):
            value=r.get(key)
            if value in (None,''): continue
            if key=='page':
                source=r.get('source_id') or r.get('source')
                if source in (None,''): continue  # Unknown provenance cannot identify a shared page.
                value=(source,value)
            if value in seen: parent[root(i)]=root(seen[value])
            else: seen[value]=i
    groups=collections.defaultdict(list)
    for i,r in enumerate(rows): groups[root(i)].append(r)
    return [{'ids':[r['id'] for r in group],'splits':sorted({r['split'] for r in group}),'crosses_split':len({r['split'] for r in group})>1} for group in groups.values()]


def cosine(a,b):
    if len(a)!=len(b): raise ValueError('vector dimensions differ')
    return div(sum(x*y for x,y in zip(a,b)),math.sqrt(sum(x*x for x in a)*sum(y*y for y in b)))


def quantile(values,p):
    x=sorted(values)
    if not x:return None
    position=(len(x)-1)*p;lo=int(position);hi=min(lo+1,len(x)-1)
    return x[lo]+(x[hi]-x[lo])*(position-lo)


def bootstrap(rows,cfg):
    if not rows: raise ValueError('empty bootstrap sample')
    unit=cfg.get('unit','row')
    if unit not in ('row','source'): raise ValueError('bootstrap unit must be row or source')
    if type(cfg['resamples']) is not int or cfg['resamples']<=0: raise ValueError('resamples must be a positive integer')
    if not 0<cfg['confidence']<1: raise ValueError('confidence must be between 0 and 1')
    rng=random.Random(cfg['seed'])
    groups=collections.defaultdict(list)
    for r in rows:groups[r['source'] if unit=='source' else r['id']].append(r)
    groups=list(groups.values());values=[]
    for _ in range(cfg['resamples']):
        sample=[r for group in rng.choices(groups,k=len(groups)) for r in group]
        values.append(sum(r['b']-r['a'] for r in sample)/len(sample))
    alpha=1-cfg['confidence']
    return {'n_rows':len(rows),'n_sampling_units':len(groups),'unit':unit,'method':'percentile linear quantiles','difference_b_minus_a':sum(r['b']-r['a'] for r in rows)/len(rows),'interval':[quantile(values,alpha/2),quantile(values,1-alpha/2)],'resamples':cfg['resamples'],'seed':cfg['seed']}


def mcnemar(rows):
    if any(r['a'] not in (0,1) or r['b'] not in (0,1) for r in rows):raise ValueError('McNemar requires binary correctness')
    cells=collections.Counter((r['a'],r['b']) for r in rows)
    b=cells[(1,0)];c=cells[(0,1)];n=b+c
    p=1.0 if not n else min(1.0,2*sum(math.comb(n,k) for k in range(min(b,c)+1))/(2**n))
    return {'both_correct':cells[(1,1)],'only_a':b,'only_b':c,'both_wrong':cells[(0,0)],'discordant':n,'two_sided_exact_p':p,'assumption':'Independent paired units required; this six-row fixture shares sources.'}


def lcs(a,b):
    previous=[0]*(len(b)+1)
    for x in a:
        current=[0]
        for j,y in enumerate(b):current.append(previous[j]+1 if x==y else max(previous[j+1],current[-1]))
        previous=current
    return previous[-1]


def overlap(rows,cfg):
    result=[]
    if type(cfg['bleu_order']) is not int or cfg['bleu_order']<1: raise ValueError('bleu order must be a positive integer')
    for r in rows:
        ref=r['reference'].split();cand=r['candidate'].split();prec=[]
        if not ref: raise ValueError('empty reference')
        for n in range(1,cfg['bleu_order']+1):
            rc=collections.Counter(tuple(ref[i:i+n]) for i in range(len(ref)-n+1))
            cc=collections.Counter(tuple(cand[i:i+n]) for i in range(len(cand)-n+1))
            prec.append(div(sum(min(v,rc[k]) for k,v in cc.items()),sum(cc.values())))
        bp=0 if not cand else min(1,math.exp(1-len(ref)/len(cand)))
        bleu=0 if not cand else None if any(p is None for p in prec) else 0 if any(p==0 for p in prec) else bp*math.exp(sum(math.log(p) for p in prec)/len(prec))
        common=sum((collections.Counter(ref)&collections.Counter(cand)).values())
        longest=lcs(ref,cand)
        def prf(hit):return {'precision':div(hit,len(cand)),'recall':div(hit,len(ref)),'f1':div(2*hit,len(ref)+len(cand))}
        result.append({'id':r['id'],'bleu_sentence_unsmoothed':bleu,'ngram_precisions':prec,'brevity_penalty':bp,'rouge1':prf(common),'rougeL':prf(longest)})
    return result


def pgm(path):
    lines=path.read_text(encoding='ascii').splitlines()
    values=' '.join(line.split('#')[0] for line in lines).split()
    if not values or values[0]!='P2':raise ValueError('only ASCII P2 PGM accepted')
    w,h,maxval=map(int,values[1:4]);pixels=list(map(int,values[4:]))
    if len(pixels)!=w*h or maxval<=0 or any(v<0 or v>maxval for v in pixels):raise ValueError('invalid PGM')
    return [pixels[y*w:(y+1)*w] for y in range(h)]


def image_features(matrix,threshold,include_fill=True):
    points=[(x,y) for y,row in enumerate(matrix) for x,v in enumerate(row) if v<threshold]
    if not points:return None
    width=max(x for x,y in points)-min(x for x,y in points)+1
    height=max(y for x,y in points)-min(y for x,y in points)+1
    return ([len(points)/(width*height)] if include_fill else [])+[width/height]


def nearest_centroid(rows):
    train=[r for r in rows if r['split']=='train'];dev=[r for r in rows if r['split']!='train']
    labels=sorted({r['label'] for r in train});centroids={}
    for label in labels:
        vectors=[r['vector'] for r in train if r['label']==label]
        if not vectors or not vectors[0]:raise ValueError('missing training vector')
        if len({len(v) for v in vectors})!=1:raise ValueError('dimensions differ')
        centroids[label]=[sum(v[j] for v in vectors)/len(vectors) for j in range(len(vectors[0]))]
    result=[]
    for r in dev:
        if r['vector'] is None:
            result.append({'id':r['id'],'label':r['label'],'prediction':None,'scores':{},'accepted':False});continue
        distances={k:sum((x-y)**2 for x,y in zip(r['vector'],v)) for k,v in centroids.items()}
        if any(len(r['vector'])!=len(v) for v in centroids.values()):raise ValueError('dimensions differ')
        smallest=min(distances.values());weight={k:math.exp(-(d-smallest)) for k,d in distances.items()};total=sum(weight.values())
        scores={k:v/total for k,v in weight.items()};pred=max(labels,key=lambda k:scores[k])
        result.append({'id':r['id'],'label':r['label'],'prediction':pred,'scores':scores,'max_score':scores[pred]})
    return {'centroids':centroids,'rows':result}


def vision_class(rows,cfg,base,include_fill=True,accept=None):
    vectors=[dict(r,vector=image_features(pgm(base/r['file']),cfg['threshold'],include_fill)) for r in rows]
    if any(r['vector'] is None for r in vectors if r['split']=='train'):raise ValueError('empty training foreground')
    result=nearest_centroid(vectors);accept=cfg.get('accept',0.6) if accept is None else accept
    for r in result['rows']:r['accepted']=r.get('max_score',0)>=accept
    accepted=[r for r in result['rows'] if r['accepted']]
    correct=sum(r['prediction']==r['label'] for r in accepted)
    result['metrics']={'n':len(result['rows']),'accepted':len(accepted),'correct_accepted':correct,'coverage':div(len(accepted),len(result['rows'])),'accepted_accuracy':div(correct,len(accepted)),'utility':div(2*correct-len(accepted),len(result['rows']))}
    return result


def iou(a,b):
    if len(a)!=4 or len(b)!=4 or a[0]>=a[2] or a[1]>=a[3] or b[0]>=b[2] or b[1]>=b[3]:raise ValueError('bad xyxy box')
    intersection=max(0,min(a[2],b[2])-max(a[0],b[0]))*max(0,min(a[3],b[3])-max(a[1],b[1]))
    union=(a[2]-a[0])*(a[3]-a[1])+(b[2]-b[0])*(b[3]-b[1])-intersection
    return intersection/union


def detection(rows,threshold):
    unique(rows,'id')
    refs=[r for r in rows if r['kind']=='reference'];preds=sorted([r for r in rows if r['kind']=='prediction'],key=lambda r:(-r['score'],r['id']))
    used=set();out=[]
    for r in preds:
        candidates=[g for g in refs if g['id'] not in used and g['label']==r['label'] and g['image']==r['image']]
        best=max(candidates,key=lambda g:iou(r['box'],g['box'])) if candidates else None
        score=iou(r['box'],best['box']) if best else 0
        match=best if best and score>=threshold else None
        if match:used.add(match['id'])
        out.append({'id':r['id'],'label':r['label'],'score':r['score'],'matched_id':match['id'] if match else None,'best_iou':score,'tp':int(bool(match))})
    ap={}
    for label in sorted({r['label'] for r in refs}):
        n=sum(r['label']==label for r in refs);selected=[r for r in out if r['label']==label]
        tp=0;area=0
        for rank,r in enumerate(selected,1):
            tp+=r['tp']
            if r['tp']:area+=(tp/rank)/n
        ap[label]=area
    return {'matches':out,'missed_ids':[r['id'] for r in refs if r['id'] not in used],'ap_noninterpolated_per_class':ap,'mean_ap_at_one_threshold':sum(ap.values())/len(ap) if ap else None,'protocol':'teaching non-interpolated AP at a single IoU threshold; not COCO AP'}


def segmentation(rows):
    unique(rows,'id')
    out=[]
    for r in rows:
        g=r['reference'];p=r['prediction']
        if len(g)!=len(p) or any(len(a)!=len(b) for a,b in zip(g,p)):raise ValueError('mask shape mismatch')
        flat=[(a,b) for ga,pa in zip(g,p) for a,b in zip(ga,pa)]
        if any(a not in (0,1) or b not in (0,1) for a,b in flat):raise ValueError('binary masks required')
        classes={}
        for c in (0,1):
            intersection=sum(a==c and b==c for a,b in flat);union=sum(a==c or b==c for a,b in flat)
            classes[str(c)]={'intersection':intersection,'union':union,'iou':div(intersection,union)}
        available=[x['iou'] for x in classes.values() if x['iou'] is not None]
        out.append({'id':r['id'],'classes':classes,'miou_including_background':sum(available)/len(available) if available else None,'foreground_iou':classes['1']['iou']})
    return out


def run(data,base):
    rows=data.get('rows',[]);cfg=data.get('config',{});mode=data['mode']
    if rows:unique(rows,'id')
    if mode=='units':return {'rows':len(rows),'entities':len({r['entity'] for r in rows}),'source_pages':len({(r['source_id'],r['page']) for r in rows}),'missing_required':[{ 'id':r['id'],'fields':[k for k in cfg['required'] if r.get(k) in ('',None)]} for r in rows]}
    if mode=='derive':return {'selected':[r for r in rows if r['event']==cfg['select_event']],'mapping':[{'id':r['id'],'included':r['event']==cfg['select_event'],'reason':'event matches' if r['event']==cfg['select_event'] else 'different event state'} for r in rows]}
    if mode=='missing':
        observed=[r for r in rows if r['state']=='observed'];return {'states':dict(collections.Counter(r['state'] for r in rows)),'total_rows':len(rows),'observed_rows':len(observed),'observed_sum':sum(float(r['amount']) for r in observed),'unresolved_ids':[r['id'] for r in rows if r['state']!='observed']}
    if mode=='agreement':return agreement(rows)
    if mode=='coverage':return coverage(rows)
    if mode=='split':return split_groups(rows,cfg['group_keys'])
    if mode=='card':return {'card':cfg['card'],'rows':len(rows),'required_missing':[k for k in ['name','unit','source','version','status'] if not cfg['card'].get(k)],'note':'Checks presence only, not truth or historical validity.'}
    if mode=='baseline':return {'all_negative':binary_metrics([r['gold'] for r in rows],[0]*len(rows)),'literal':rule_result(rows)}
    if mode in ('matrix','ablation'):
        combos=[(False,False),(True,False),(False,True),(True,True)] if mode=='matrix' else [(True,True),(False,True),(True,False),(False,False)]
        return [{'expand':a,'negation':b,**rule_result(rows,a,b)} for a,b in combos]
    if mode=='config':
        if type(cfg['seed']) is not int or type(cfg['sample_size']) is not int:raise ValueError('seed and sample size must be integers')
        ordered=list(reversed(rows)) if cfg['input_order']=='reversed' else list(rows)
        if cfg['population_order']=='id_ascending':ordered.sort(key=lambda r:r['id'])
        elif cfg['population_order']!='as_read':raise ValueError('unknown ordering')
        if not 0<=cfg['sample_size']<=len(ordered):raise ValueError('sample size out of range')
        sample=random.Random(cfg['seed']).sample(ordered,cfg['sample_size'])
        return {'configuration':cfg,'sample_ids':[r['id'] for r in sample],'sample_rows':sample,'environment_observed':{'python':sys.version,'platform':sys.platform},'note':'JSON configuration; no YAML parser or environment change.'}
    if mode=='tracking':return {'records':rows,'ineligible_ids':[r['id'] for r in rows if r['status']!='COMPLETED'],'invalid_unrun_scores':[r['id'] for r in rows if r['status'] in ('NOT_RUN','FAILED') and r['metric']!='']}
    if mode=='literal':
        result=[]
        for r in rows:
            s=r['text'];q=r['needle'];spans=[]
            if q:
                start=0
                while True:
                    i=s.find(q,start)
                    if i<0:break
                    spans.append([i,i+len(q)]);start=i+1
            result.append({'id':r['id'],'spans':spans})
        return result
    if mode=='join':
        unique(rows,'prediction_id');pred={r['prediction_id']:r['prediction'] for r in rows}
        if set(pred)!={r['id'] for r in rows}:raise ValueError('prediction id set differs')
        return {'by_id':[{'id':r['id'],'gold':r['gold'],'prediction':pred[r['id']]} for r in rows],'metrics':binary_metrics([r['gold'] for r in rows],[pred[r['id']] for r in rows])}
    if mode=='independent':
        blind=list(csv.DictReader((base/'input_blind.csv').open(encoding='utf-8',newline='')))
        unique(blind,'id');return {'predictions':[{'id':r['id'],'prediction':rule(r['text'],True,True)} for r in blind],'note':'Predict-only stage. Reference is not opened here.'}
    if mode=='tasks':return {'tasks':[{'id':r['id'],'task':r['task'],'expected_output':r['output']} for r in rows],'note':'Human-authored task specification, not an NLP model.'}
    if mode=='tensor':
        chars=sorted(set(''.join(r['text'] for r in rows)));vocab={c:i+1 for i,c in enumerate(chars)};width=min(max(len(r['text']) for r in rows),cfg['max_length']);out=[]
        for r in rows:
            s=r['text'][:width];out.append({'id':r['id'],'input_ids':[vocab[c] for c in s]+[0]*(width-len(s)),'attention_mask':[1]*len(s)+[0]*(width-len(s)),'label':r['label'],'truncated':len(r['text'])>width})
        return {'pad_id':0,'vocabulary':vocab,'shape':[len(rows),width],'rows':out,'note':'Character teaching encoding, not a pretrained tokenizer.'}
    if mode=='vectors':return [{'left':a['id'],'right':b['id'],'cosine':cosine(a['vector'],b['vector'])} for i,a in enumerate(rows) for b in rows[i+1:]]
    if mode=='benchmark':return {'specifications':rows,'required_human_action':'Check version, task, labels, split, metrics and local validity before comparing.'}
    if mode=='multilingual':
        groups=collections.defaultdict(list)
        for r in rows:groups[r['language']].append(r)
        return {k:{'n':len(v),'correct':sum(r['pred']==r['gold'] for r in v),'accuracy':sum(r['pred']==r['gold'] for r in v)/len(v),'errors':[r['id'] for r in v if r['pred']!=r['gold']]} for k,v in groups.items()}
    if mode=='prompt':return [{'id':r['id'],'prompt':cfg['template'].format(id=r['id'],text=r['text']),'response_status':'NOT_RUN'} for r in rows]
    if mode=='fewshot':
        examples=sorted([r for r in rows if r['split']=='example'],key=lambda r:r['id']);tests=[r for r in rows if r['split']=='test'];out=[]
        if {r['source'] for r in examples}&{r['source'] for r in tests}:raise ValueError('example/test source overlap')
        for k in cfg['k']:
            if k>len(examples):raise ValueError('not enough eligible examples')
            for t in tests:out.append({'k':k,'example_ids':[r['id'] for r in examples[:k]],'test_id':t['id'],'prompt':'\n'.join(r['text']+' => '+r['answer'] for r in examples[:k])+'\n待判断：'+t['text'],'response_status':'NOT_RUN'})
        return out
    if mode=='sensitivity':
        group=collections.defaultdict(list)
        for r in rows:group[r['variant']].append(r)
        return {'variant_scores':{k:sum(r['answer']==r['gold'] for r in v)/len(v) for k,v in group.items()},'items':{item:sorted({r['answer'] for r in rows if r['item']==item}) for item in {r['item'] for r in rows}},'provenance':'Prewritten teaching answers, not model outputs.'}
    if mode=='overlap':return overlap(rows,cfg)
    if mode=='ratings':
        out=[]
        for item in sorted({r['item'] for r in rows}):
            rr=[r for r in rows if r['item']==item];out.append({'item':item,'ratings':rr,'disputed_dimensions':[d for d in ['supported','complete','readable'] if len({r[d] for r in rr})>1]})
        return out
    if mode=='judge':return {'agreement':div(sum(r['human']==r['judge'] for r in rows),len(rows)),'disagreements':[r for r in rows if r['human']!=r['judge']],'note':'Judge identities are candidate identities, not display positions. Prewritten fixture.'}
    if mode=='bootstrap':return bootstrap(rows,cfg)
    if mode=='mcnemar':return mcnemar(rows)
    if mode=='claims':return {'n':len(rows),'verdicts':dict(collections.Counter(r['verdict'] for r in rows)),'needs_revision':[r['id'] for r in rows if r['verdict']!='supported'],'note':'Counts supplied human judgments; does not establish truth.'}
    if mode=='vision_class':return vision_class(rows,cfg,base)
    if mode=='detection':return detection(rows,cfg['iou_threshold'])
    if mode=='segmentation':return segmentation(rows)
    if mode=='architecture':
        out=[]
        for r in rows:
            if r['height']%r['patch'] or r['width']%r['patch']:raise ValueError('fixture requires exact patch grid')
            n=(r['height']//r['patch'])*(r['width']//r['patch']);out.append({'id':r['id'],'patch_tokens_excluding_cls':n,'token_pairs_excluding_cls':n*n})
        return out
    if mode=='feature_eval':return nearest_centroid(rows)
    if mode=='vision_metrics':return {'classification':{'n':len(rows),'top1':div(sum(max(r['scores'],key=r['scores'].get)==r['label'] for r in rows),len(rows))},'detection':detection(cfg['boxes'],cfg['iou_threshold']),'segmentation':segmentation(cfg['masks'])}
    if mode=='longtail':
        per=[]
        for label in sorted({r['label'] for r in rows}):
            subset=[r for r in rows if r['label']==label];per.append({'label':label,'support':len(subset),'recall':sum(r['pred']==r['label'] for r in subset)/len(subset),'sources':sorted({r['source'] for r in subset})})
        return {'per_class':per,'macro_recall':div(sum(r['recall'] for r in per),len(per)),'micro_accuracy':div(sum(r['label']==r['pred'] for r in rows),len(rows))}
    if mode=='shift':
        out=[]
        for source in sorted({r['source'] for r in rows}):
            group=[r for r in rows if r['source']==source];accepted=[r for r in group if r['accepted']];correct=sum(r['pred']==r['label'] for r in accepted)
            out.append({'source':source,'n':len(group),'accepted':len(accepted),'correct_accepted':correct,'coverage':div(len(accepted),len(group)),'accepted_accuracy':div(correct,len(accepted)),'correct_accepted_per_all':div(correct,len(group))})
        return out
    if mode=='vision_ablation':return [{'include_fill':f,'accept':a,**vision_class(rows,cfg,base,f,a)} for f in (False,True) for a in cfg['accept_values']]
    raise ValueError('unknown mode '+mode)


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--input',required=True)
    args=parser.parse_args();path=Path(args.input).resolve();data=json.loads(path.read_text(encoding='utf-8'))
    result=run(data,path.parent)
    print(json.dumps({'execution':'reader_invoked','input_provenance':data['provenance'],'section':data['section'],'result':result},ensure_ascii=False,indent=2,allow_nan=False))

if __name__=='__main__':main()

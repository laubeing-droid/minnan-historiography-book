#!/usr/bin/env python3
"""Local audit probes; only subprocess audited local workbook/scorer, save new logs.
No network, installation, model calls, deletion, or input-file overwrite.
Usage: python -B check_boundaries.py before|after
"""
from pathlib import Path
import copy, csv, json, subprocess, sys
ROOT=Path(__file__).resolve().parents[2]
ATT=ROOT/'revision/附件'
OUT=Path(__file__).resolve().parent
phase=sys.argv[1]
dest=OUT/(phase+'_boundaries');dest.mkdir(exist_ok=False)
records=[]
def probe(name,section,transform,predicate,why):
    source=ATT/('ch'+section.split('.')[0].zfill(2))/section/'input.json'
    data=json.loads(source.read_text());transform(data)
    p=dest/(name+'.input.json');p.write_text(json.dumps(data,ensure_ascii=False,indent=2))
    command=[sys.executable,'-B',str(source.parent.parent/'workbook.py'),'--input',str(p)]
    result=subprocess.run(command,capture_output=True,text=True)
    (dest/(name+'.stdout.json')).write_text(result.stdout)
    (dest/(name+'.stderr.txt')).write_text(result.stderr)
    value=json.loads(result.stdout).get('result') if result.returncode==0 else None
    okay=predicate(result.returncode,value,result.stderr)
    records.append(dict(name=name,section=section,command=command,exit_code=result.returncode,status='EXECUTED_PASS' if okay else 'FAIL',reason=why,result=value,stderr=result.stderr))
def rows(value):return lambda d:d.update(rows=copy.deepcopy(value))
def err(rc,v,s):return rc!=0 and 'ValueError' in s
def blank(rc,v,s):return rc==0
probe('empty_binary','8.1',rows([]),lambda rc,v,s:rc==0 and all(v['literal']['metrics'][k] is None for k in ('precision','recall','f1','accuracy')),'空二分类分母不得虚构零分。')
probe('invalid_binary','8.1',lambda d:d['rows'][0].update(gold=.5),err,'非0/1标签必须拒绝。')
probe('zero_coverage','7.5',rows([dict(id='zero',available=0,readable=0,evaluated=0,correct=0)]),lambda rc,v,s:rc==0 and all(v[0][k] is None for k in ('accuracy','evaluation_coverage','readable_fraction')),'覆盖和准确率零分母应为null。')
probe('invalid_coverage','7.5',lambda d:d['rows'][0].update(correct=7),err,'correct不得超过evaluated。')
probe('empty_agreement','7.4',rows([]),lambda rc,v,s:rc==0 and v['agreement'] is None and v['kappa'] is None,'无记录一致率及kappa未定义。')
probe('constant_agreement','7.4',rows([dict(id='a',a='same',b='same'),dict(id='b',a='same',b='same')]),lambda rc,v,s:rc==0 and v['agreement']==1 and v['kappa'] is None,'完全同类机会一致=1时kappa未定义。')
probe('missing_observed_amount','7.3',lambda d:d['rows'][0].update(amount=''),err,'observed缺值不得按零处理。')
probe('transitive_split','7.6',rows([dict(id='a',person='x',source='A',page='A1',split='train'),dict(id='b',person='x',source='B',page='B1',split='dev'),dict(id='c',person='y',source='B',page='B2',split='test')]),lambda rc,v,s:rc==0 and len(v)==1 and v[0]['crosses_split'],'关联图传递闭包必须跨person/source检测。')
probe('page_number_scoped_by_source','7.6',rows([dict(id='a',person='x',source='A',page='1',split='train'),dict(id='b',person='y',source='B',page='1',split='test')]),lambda rc,v,s:rc==0 and len(v)==2 and not any(x['crosses_split'] for x in v),'正文明确要求页号连同书号核对，不得把不同书第一页连成同页。')
probe('duplicate_prediction_id','8.7',lambda d:d['rows'][1].update(prediction_id='J02'),err,'预测编号重复必须报错，不覆盖字典。')
probe('overlapping_literal','8.6',rows([dict(id='a',text='aaa',needle='aa')]),lambda rc,v,s:rc==0 and v[0]['spans']==[[0,2],[1,3]],'重叠字面命中、左闭右开位置。')
probe('missing_literal','8.6',rows([dict(id='a',text=None,needle='aa')]),lambda rc,v,s:rc!=0,'缺文字显式失败，不能补成空或零。')
probe('invalid_sampling_size','8.4',lambda d:d['config'].update(sample_size=7),err,'样本量超过总体需明确拒绝。')
probe('zero_cosine','9.4',lambda d:d['rows'][0].update(vector=[0,0,0]),lambda rc,v,s:rc==0 and v[0]['cosine'] is None and v[1]['cosine'] is None,'零向量余弦未定义。')
probe('dimension_mismatch','9.4',lambda d:d['rows'][0].update(vector=[1]),err,'向量维数不符不得zip静默截断。')
probe('truncated_tensor','9.2',lambda d:d['config'].update(max_length=3),lambda rc,v,s:rc==0 and v['shape']==[3,3] and all(r['truncated'] for r in v['rows']),'截断必须保留标记与张量长度。')
probe('fewshot_source_overlap','10.2',lambda d:d['rows'][2].update(source='demo_A'),err,'示例与测试来源重叠必须报错。')
probe('fewshot_excess_k','10.2',lambda d:d['config'].update(k=[3]),err,'k不可超过示例池。')
probe('overlap_insufficient_order','10.4',rows([dict(id='x',reference='甲 渡',candidate='甲')]),lambda rc,v,s:rc==0 and v[0]['ngram_precisions']==[1,None] and v[0]['bleu_sentence_unsmoothed'] is None,'非空候选缺少二元项时分母为零须为null，而非零匹配。')
probe('overlap_empty_reference','10.4',rows([dict(id='x',reference='',candidate='甲')]),err,'空参考不能被作为有效摘要评价输入。')
probe('overlap_empty_candidate','10.4',rows([dict(id='x',reference='甲 渡',candidate='')]),lambda rc,v,s:rc==0 and v[0]['bleu_sentence_unsmoothed']==0,'空候选按明示口径BLEU=0，与不足阶数区分。')
probe('bootstrap_empty','10.7',rows([]),err,'空bootstrap样本明确拒绝。')
probe('bootstrap_unknown_unit','10.7',lambda d:d['config'].update(unit='soruce'),err,'拼错重采样单位不得静默退回逐行，避免违反来源相关性口径。')
probe('bootstrap_zero_resamples','10.7',lambda d:d['config'].update(resamples=0),err,'零次重采样不应冒充完成区间。')
probe('mcnemar_no_discordance','10.8',rows([dict(id='x',a=1,b=1)]),lambda rc,v,s:rc==0 and v['discordant']==0 and v['two_sided_exact_p']==1,'无不一致对精确p=1。')
probe('empty_foreground','11.3',rows([dict(id='x',reference=[[0,0]],prediction=[[0,0]])]),lambda rc,v,s:rc==0 and v[0]['foreground_iou'] is None and v[0]['miou_including_background']==1,'空前景并集=0排除而非伪造前景满分。')
probe('mask_shape_mismatch','11.3',rows([dict(id='x',reference=[[0,0]],prediction=[[0]])]),err,'掩膜shape不一致显式报错。')
probe('duplicate_nested_detection_id','11.7',lambda d:d['config']['boxes'][1].update(id='D01'),err,'嵌套指标输入也应遵守本节编号唯一。')
probe('empty_longtail','11.8',rows([]),lambda rc,v,s:rc==0 and v['macro_recall'] is None and v['micro_accuracy'] is None,'README通用承诺：零分母输出null。')
probe('all_rejected','11.9',lambda d:[r.update(accepted=0) for r in d['rows']],lambda rc,v,s:rc==0 and all(r['coverage']==0 and r['accepted_accuracy'] is None for r in v),'全拒识时覆盖为0，接受准确率未定义。')
# Scorer binary validation: copied predictions are review-owned, not input edits.
payload=json.loads((OUT/'before/8.8__input.stdout.json').read_text());payload['result']['predictions'][0]['prediction']=1.7
p=dest/'score_fractional_prediction.input.json';p.write_text(json.dumps(payload))
command=[sys.executable,'-B',str(ATT/'ch08/8.8/score_predictions.py'),'--predictions',str(p),'--reference',str(ATT/'ch08/8.8/reference.csv')]
r=subprocess.run(command,capture_output=True,text=True)
(dest/'score_fractional_prediction.stdout.json').write_text(r.stdout);(dest/'score_fractional_prediction.stderr.txt').write_text(r.stderr)
records.append(dict(name='score_fractional_prediction',section='8.8',command=command,exit_code=r.returncode,status='EXECUTED_PASS' if r.returncode!=0 and 'ValueError' in r.stderr else 'FAIL',reason='非二值1.7不得先int截断为1再判合法。',stderr=r.stderr))
report={'phase':phase,'tests':records,'passed':sum(r['status']=='EXECUTED_PASS' for r in records),'failed':sum(r['status']=='FAIL' for r in records)}
(dest/'manifest.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps({'phase':phase,'passed':report['passed'],'failed':[r['name'] for r in records if r['status']=='FAIL']},ensure_ascii=False))

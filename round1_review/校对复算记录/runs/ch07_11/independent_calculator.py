#!/usr/bin/env python3
"""Independent arithmetic against saved outputs. Does not import any workbook.
Expected counts were read directly from fixtures / displayed body tables.
This is not empirical or historical validation, and it makes no model call.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from collections import Counter
import csv, json, math, re, sys
BASE=Path(__file__).resolve().parent
ATT=BASE.parents[1]/'revision/附件'
phase=sys.argv[1] if len(sys.argv)>1 else 'after'
records=[]
def result(sec,stem='input'):
    return json.loads((BASE/phase/(sec+'__'+stem+'.stdout.json')).read_text())['result']
def equal(a,b):
    if isinstance(a,(int,float)) and isinstance(b,(int,float)):
        return math.isclose(a,b,rel_tol=1e-11,abs_tol=1e-12)
    if isinstance(a,list) and isinstance(b,list):return len(a)==len(b) and all(equal(x,y) for x,y in zip(a,b))
    if isinstance(a,dict) and isinstance(b,dict):return a.keys()==b.keys() and all(equal(a[k],b[k]) for k in a)
    return a==b
def check(sec,name,actual,expected,basis,kind='独立手计/公式'):
    records.append(dict(section=sec,name=name,status='EXECUTED_PASS' if equal(actual,expected) else 'FAIL',observed=actual,expected=expected,basis=basis,kind=kind))
def values(d,keys):return [d[k] for k in keys.split()]
r=result('7.1');check('7.1','单位与必填项',values(r,'rows entities source_pages')+[sum(bool(x['fields']) for x in r['missing_required'])],[3,2,2,0],'E01/E02同机构同页、不同事件；E03另机构另页。')
for stem,expected in [('input',['E01']),('input_v2',['E02'])]:
    check('7.2','派生选择/'+stem,[r['id'] for r in result('7.2',stem)['selected']],expected,'只改变select_event；原始三行不变。')
r=result('7.3');check('7.3','明确零与缺失',values(r,'total_rows observed_rows observed_sum unresolved_ids'),[4,2,3.0,['U02','U03']],'U01=0、U04=3，只有两条可计；未载、难辨不填零。')
for sec in ['7.4','9.6']:
    r=result(sec);check(sec,'四条双人标签',values(r,'n agreement expected_agreement kappa'),[4,.5,5/16,3/11],'同判2/4；边际(3,1,0)和(1,2,1)，Pe=(3+2)/16，kappa=(8-5)/(16-5)=3/11。')
for sec in ['7.5','9.8']:
    check(sec,'覆盖漏斗',[[r[k] for k in ('readable_fraction','evaluation_coverage','accuracy')] for r in result(sec)],[[10/12,6/12,5/6],[4/6,3/6,1/3],[4/4,2/4,1/2]],'直接按每行correct/evaluated、evaluated/available、readable/available；三种分母不混用。')
r=result('7.6');check('7.6','关联组闭包',[(r['ids'],r['crosses_split']) for r in r],[(['R01','R02','R03'],True),(['R04','R06'],True),(['R05'],False)],'R01-03由书A连通，R04/06由人物丙连通；两个组跨split。')
for sec in ['7.7','10.10']:
    r=result(sec);check(sec,'卡片结构',values(r,'rows required_missing'),[6,[]],'只查五个必要字段的存在；不证明数据/模型有效。',kind='模板结构')
metric_keys='tp fp fn tn accuracy precision recall f1'
expected_base=[2,2,1,1,.5,.5,2/3,4/7]
for sec in ['8.1','9.3']:
    r=result(sec);check(sec,'关键词基线',values(r['literal']['metrics'],metric_keys),expected_base,'逐句手判T01,T02,T03,T06命中，T04漏；TP=2 FP=2 FN=1 TN=1。')
    check(sec,'全负类基线',values(r['all_negative'],metric_keys),[0,0,3,3,.5,None,0,0],'零候选精确率未定义，不得记满分。')
combo={(False,False):expected_base,(True,False):[3,2,0,1,4/6,3/5,1,3/4],(False,True):[2,0,1,3,5/6,1,2/3,4/5],(True,True):[3,0,0,3,1,1,1,1]}
for sec in ['8.2','8.3']:
    for r in result(sec):
        k=(r['expand'],r['negation']);check(sec,'组件'+str(k),values(r['metrics'],metric_keys),combo[k],'扩词只修T04；否定只排T02/T03。六句均为已见教学开发样本。')
samples={stem:result('8.4',stem)['sample_ids'] for stem in ['input','input_seed29','input_reverse_sort','input_reverse_unsorted']}
check('8.4','顺序控制不变量',[samples['input']==samples['input_reverse_sort'],samples['input']!=samples['input_reverse_unsorted'],len(set(samples['input'])),len(samples['input'])],[True,True,3,3],'固定排序消除反转；不排序时相同随机位置对应不同编号。此项是重现性检查，不是历史结果。',kind='确定性不变量')
r=result('8.5');check('8.5','运行登记排除',values(r,'ineligible_ids invalid_unrun_scores'),[['E01','E02','E03'],[]],'NOT_RUN、FAILED、ILLUSTRATIVE均不得作为COMPLETED结果；原教学状态不因本次运行检查器而改写。',kind='预置状态检查')
check('8.6','字面位置',[r['spans'] for r in result('8.6')],[[[2,4],[6,8]],[[0,2],[2,4]],[],[]],'从0数Unicode字符，左闭右开；字面命中不处理否定。')
r=result('8.7');check('8.7','按编号而非行序',values(r['metrics'],metric_keys),[1,0,0,1,1,1,1,1],'J01连接prediction_id=J01的1，J02连接0。')
check('8.8','盲预测六句',[r['prediction'] for r in result('8.8')['predictions']],[1,0,0,1,0,1],'直接依固定词表/否定短语手判；预测入口不含gold。')
score=json.loads((BASE/phase/'8.8__score.stdout.json').read_text());check('8.8','独立评分计数',[score['n'],score['confusion_gold_prediction'],score['errors']],[6,{'00':3,'01':0,'10':0,'11':3},[]],'reference.csv六项与手判一致；不是独立历史测试。')
r=result('9.1');check('9.1','四类任务规格',[x['task'] for x in r['tasks']],['understanding','retrieval','generation','reasoning'],'仅转写人工任务说明，未执行NLP模型。',kind='非运行型任务模板的结构检查')
r=result('9.2');check('9.2','张量长度/掩码',[r['shape'],[sum(x['attention_mask']) for x in r['rows']],[x['truncated'] for x in r['rows']]],[[3,7],[5,7,5],[False]*3],'三条原文字符数5、7、5，最长7，分别补2、0、2。')
check('9.2','字表回取',[''.join(next(c for c,i in r['vocabulary'].items() if i==token) for token in row['input_ids'] if token) for row in r['rows']],['甲埠议迁。','乙埠迁至东岸。','丙埠未迁。'],'逆查字表必须无损恢复原文。')
check('9.4','三组余弦',[r['cosine'] for r in result('9.4')],[1.8/math.sqrt(2*1.64),.1/math.sqrt(2*1.01),.08/math.sqrt(1.64*1.01)],'手算点积1.8、0.1、0.08；平方范数2、1.64、1.01。')
for sec,n in [('9.5',4),('11.6',3)]:
    check(sec,'基准审读行数',len(result(sec)['specifications']),n,'只展示人工规格；没有下载基准或执行基准模型。',kind='非运行型基准模板的结构检查')
r=result('9.7');check('9.7','分语言正确数',[r['中文']['correct'],r['English']['correct'],r['中文']['accuracy'],r['English']['accuracy']],[2,1,1,.5],'中文两题均对；英文P02将拟议误判已迁，不能把两语言当四个独立事件。')
r=result('10.1');check('10.1','提示渲染',[len(r),all('gold' not in x['prompt'] for x in r),[x['response_status'] for x in r]],[2,True,['NOT_RUN']*2],'两条完整提示仅含id/text；没有模型回答。',kind='非运行型提示模板的渲染检查')
r=result('10.2');check('10.2','示例数与测试答案隔离',[[x['k'],len(x['example_ids']),x['test_id'],x['response_status']] for x in r],[[0,0,'S03','NOT_RUN'],[2,2,'S03','NOT_RUN']],'只渲染k=0和k=2提示，S03参考answer未拼入提示。',kind='非运行型提示模板的渲染检查')
r=result('10.3');check('10.3','预置敏感度计数',r['variant_scores'],{'V1':1,'V2':.5},'V1二次均对，V2两次一对；不是新模型运行。')
r=result('10.4')
check('10.4','G01重叠', [r[0]['ngram_precisions'],r[0]['bleu_sentence_unsmoothed'],r[0]['rouge1']['f1'],r[0]['rougeL']['f1']],[[3/5,1/4],math.sqrt(3/20),3/5,3/5],'5词候选，命中甲/渡/迁3词，二元仅甲渡1项；LCS=3，BP=1。')
check('10.4','G02重叠', [r[1]['ngram_precisions'],r[1]['bleu_sentence_unsmoothed'],r[1]['rouge1']['f1'],r[1]['rougeL']['f1']],[[6/7,4/6],math.sqrt(4/7),12/13,12/13],'7词候选多一个已，参考6词全保留；二元4/6、LCS=6，BP=1。')
check('10.5','人工分维度争议',[x['disputed_dimensions'] for x in result('10.5')],[['supported'],[]],'Q1只supported不同；Q2三维全同。预置评分不等于真人实验。')
check('10.6','预置judge一致率',result('10.6')['agreement'],2/3,'J1不一致，J2/J3一致；没有LLM-as-Judge调用。')
r=result('10.7');check('10.7','来源组点估计',values(r,'n_rows n_sampling_units difference_b_minus_a'),[6,3,1/6],'A组差+1，B/C组总差0，六行合计差+1；来源抽样单位3而非6。')
distribution=Counter(sum(seq)/6 for seq in product([1,0,0],repeat=3))
check('10.7','独立枚举来源重采样分布',[[x,distribution[x]] for x in sorted(distribution)],[[0,8],[1/6,12],[1/3,6],[1/2,1]],'3^3有序来源抽样=27种；总体经验CDF在1/3为26/27<.975，.975阶梯分位点为.5。')
check('10.7','已运行2000次区间',r['interval'],[0,.5],'独立枚举证实两尾支撑；本次2000次线性分位区间端点为0,.5。27行枚举本身的线性插值不等于总体阶梯分位，不能混用。')
r=result('10.8');check('10.8','不一致对与精确p',values(r,'both_correct only_a only_b both_wrong discordant two_sided_exact_p'),[2,1,2,1,3,1],'两个同对、一个A独对、两个B独对、一个同错；p=min(1,2*(1+3)/8)=1；共有来源，不能作普通独立对推断。')
r=result('10.9');check('10.9','断言预置裁决',values(r,'n verdicts needs_revision'),[3,{'supported':1,'contradicted':1,'not_in_evidence':1},['F02','F03']],'仅计数已给人工裁决，不自动证明历史真伪。')
# Direct pixel counts, independent of workbook.pgm/image_features.
pixel_counts={}
for name in ['square','bar','square_shift','bar_shift']:
    lines=(ATT/'ch11/11.1/images'/f'{name}.pgm').read_text().splitlines()
    matrix=[list(map(int,line.split())) for line in lines[4:]]
    blacks=[(i,j) for i,row in enumerate(matrix) for j,v in enumerate(row) if v==0]
    pixel_counts[name]=[len(blacks),len({i for i,j in blacks}),len({j for i,j in blacks})]
check('11.1','像素直接计数',pixel_counts,{'square':[16,4,4],'bar':[12,2,6],'square_shift':[16,4,4],'bar_shift':[12,2,6]},'逐格计黑色像素及非空行列；方形16/(4*4)=1，条形12/(2*6)=1，宽高比1与3。')
r=result('11.1');check('11.1','距离分数与评价',[[x['prediction'],x['max_score']] for x in r['rows']],[['square',1/(1+math.exp(-4))],['bar',1/(1+math.exp(-4))]],'正确类距离0、另一类平方距离(3-1)^2=4，得分1/(1+e^-4)，两张开发图全对。')
for sec in ['11.2','11.7']:
    r=result(sec);r=r['detection'] if sec=='11.7' else r
    check(sec,'检测匹配与AP',[[x['id'],x['tp'],x['matched_id']] for x in r['matches']], [['D02',1,'D01'],['D04',0,None],['D03',0,None]],'D02占用唯一seal参考；D03重复不能再记TP；D04类别错误，不能匹配seal。')
    check(sec,'参考支持类AP',r['ap_noninterpolated_per_class'],{'seal':1},'唯一有参考的类seal的第1名已召回全部；text无参考，不进入AP宏平均。两个FP仍列出，不得把AP=1解释为无误检。')
for sec in ['11.3','11.7']:
    r=result(sec);r=r['segmentation'] if sec=='11.7' else r
    check(sec,'二值像素交并',[[r[0]['classes'][c]['intersection'],r[0]['classes'][c]['union'],r[0]['classes'][c]['iou']] for c in ['0','1']],[[12,13,12/13],[3,4,3/4]],'16格：前景3个交集、4个并集，背景12交13并。')
    check(sec,'含背景mIoU',r[0]['miou_including_background'],87/104,'(12/13+3/4)/2=87/104，非单独前景0.75。')
check('11.4','patch与配对数',[[x['patch_tokens_excluding_cls'],x['token_pairs_excluding_cls']] for x in result('11.4')],[[14**2,196**2],[28**2,784**2]],'新版明确不含CLS；不能拿旧文含CLS的197²/785²混比。')
r=result('11.5');check('11.5','手设特征最近质心',[[x['prediction'],x['max_score']] for x in r['rows']],[['seal',1/(1+math.exp(-1.2))],['photo',1/(1+math.exp(-1.2))]],'两距离分别.08和1.28，差1.2；只有两个训练向量，未提取DINOv2。')
check('11.7','Top1',result('11.7')['classification'],{'n':2,'top1':.5},'K1对、K2错，1/2。')
r=result('11.8');check('11.8','宏微分母',values(r,'macro_recall micro_accuracy'),[2/3,4/5],'photo3/3、map1/1、seal0/1；宏召回(1+1+0)/3，微正确4/5。')
r=result('11.9');check('11.9','分组拒识',[[x['source'],x['coverage'],x['accepted_accuracy'],x['correct_accepted_per_all']] for x in r],[['blur',.5,0,0],['clean',1,1,1]],'模糊组1接受0对、另1拒识；清晰2接受2对。拒识不算正确。')
check('11.10','四格零差异',[[r['metrics']['coverage'],r['metrics']['accepted_accuracy'],r['metrics']['utility']] for r in result('11.10')],[[1,1,1]]*4,'四张均为实心矩形，填充率相同；max_score≈.982高于.60和.85。无差异也是有效演示结果，不套旧12图结论。')
# Mirror integrity checks do not transform the fixture data.
for chapter in range(7,12):
    for p in sorted((ATT/f'ch{chapter:02}').glob('*/input.json')):
        d=json.loads(p.read_text());rows=d['rows'];csv_rows=list(csv.DictReader((p.parent/'input.csv').open(newline='')))
        canonical=lambda v:json.dumps(v,ensure_ascii=False) if isinstance(v,(dict,list)) else str(v)
        mirror=[{k:canonical(v) for k,v in r.items()} for r in rows]
        check(d['section'],'JSON/CSV阅读副本',csv_rows,mirror,'确认本节实际JSON与CSV阅读副本同值。',kind='输入一致性')
output={'scope':'新版43节独立计算和结构检查，非模型/历史有效性验证','checks':records,'passed':sum(r['status']=='EXECUTED_PASS' for r in records),'failed':sum(r['status']=='FAIL' for r in records)}
p=BASE/('independent_'+phase+'.json')
with p.open('x') as f:json.dump(output,f,ensure_ascii=False,indent=2)
print(json.dumps({'passed':output['passed'],'failed':[r['section']+':'+r['name'] for r in records if r['status']=='FAIL']},ensure_ascii=False))

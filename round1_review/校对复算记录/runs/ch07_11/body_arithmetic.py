#!/usr/bin/env python3
"""Recalculate exposed body examples only; never reconstruct missing run logs.
Numbers and literal text are taken from the body tables, not workbook outputs.
"""
from pathlib import Path
from itertools import product
from collections import Counter
from fractions import Fraction as F
import json,math,unicodedata
OUT=Path(__file__).resolve().parent
records=[]
def same(a,b,tol):
    if isinstance(a,(int,float)) and isinstance(b,(int,float)):return abs(a-b)<=tol
    if isinstance(a,(list,tuple)) and isinstance(b,(list,tuple)):return len(a)==len(b) and all(same(x,y,tol) for x,y in zip(a,b))
    return a==b
def test(s,name,derived,printed,basis,tol=1e-12):
    records.append(dict(section=s,name=name,status='EXECUTED_PASS' if same(derived,printed,tol) else 'FAIL',derived=derived,printed=printed,basis=basis,tolerance=tol,scope='正文公开数据的算术复核；非原实验复现'))
test('7.1','任职单位',[4,len(set(['朱','朱','傅','傅'])),len(set(['教育部','教育部','北京大学','台湾大学']))],[4,2,3],'正文R01—R04四行。')
test('7.2','职务细分总数',[2+2,2+1+1],[4,4],'部长2；原校长2拆成正式1/代理1。')
test('7.3','零与缺失均值',[sum([2,0])/2,sum([2,0,0,0,0])/5],[1,.4],'D1=2,D2=0，其余缺失不可计。')
a=['已','未','待','未','已','已','待','已','已','未'];b=['已','未','已','未','待','未','待','已','已','未']
ca,cb=Counter(a),Counter(b);po=sum(x==y for x,y in zip(a,b))/10;pe=sum(ca[k]*cb[k] for k in ca)/100
test('7.4','十条Cohen kappa',[po,pe,(po-pe)/(1-pe)],[.7,.36,.53125],'重新逐行读T01—T10，两列边际5/3/2与4/4/2。')
test('7.5','微宏平均和补充难例',[18/20,(1+.5+.5)/3,18/24],[.9,2/3,.75],'中文16/16、日英各1/2；增四个失败后18/24。')
groups=[['R01','R02','R03','R04','R11','R12'],['R05','R06'],['R07','R08'],['R09','R10']]
test('7.6','分组/去重/时间计数',[[len(groups[0])+len(groups[1]),len(groups[2]),len(groups[3])],[7,2,2],[sum(y<=1904 for y in [1900,1900,1901,1902,1903,1904,1905,1906,1907,1908,1909,1910]),2,4]],[[8,2,2],[7,2,2],[6,2,4]],'按正文关系链闭包；仅剔除重复对应R02于派生计数，未删除文件。')
def binary(tp,fp,fn,tn):return [(tp+tn)/(tp+fp+fn+tn),tp/(tp+fp) if tp+fp else None,tp/(tp+fn),2*tp/(2*tp+fp+fn),tp+fp]
test('8.1','二十句基线指标',[binary(0,0,4,16),binary(3,3,1,13)],[[.8,None,0,0,0],[.8,.5,.75,.6,6]],'正文公开四格计数直接代公式；缺原句全集，不声称重跑原预测。')
for label,cells,expected in [('M1',[3,3,1,13],[.8,.75,6]),('M2',[3,0,1,16],[.95,.75,3]),('M3',[2,3,2,13],[.75,.5,5]),('M4',[2,1,2,15],[.85,.5,3])]:
    v=binary(*cells);test('8.2',label,[v[0],v[2],v[4]],expected,'正文实验矩阵四格计数，不补造20句输入。')
test('8.3','组件联合收益',[.95-.8,.95-.8,.95-.8],[.15,.15,.15],'C/E两组件同依赖，不把两次单删下降相加。')
test('8.5','已列计数',[19/20,17/20,20/20],[.95,.85,1],'原始E02=19/20，E05=17/20，人工修订后20/20另列；非重跑旧预测。')
text='停办后复办，又停办。';hits=[[i,i+2] for i in range(len(text)-1) if text[i:i+2]=='停办'];test('8.6','字符跨度',hits,[[0,2],[7,9]],'逐字符索引，无strip。')
test('8.7','回归表计数',[10+3,6+3,10+6],[13,9,16],'仅复核表内加总；旧十例内容缺失，不能证明全部原断言。')
gold=[1,1,1,1,0,0,0,0];pred=[1,0,0,1,1,0,0,0]
test('8.8','八条旧例',[sum(x==y for x,y in zip(gold,pred))/8,2/3,2/4],[5/8,2/3,.5],'正文U01—U08直接计数，误判U02/U03/U05。')
texts=['1946年，臺灣省立師範學院成立。','1955年，臺灣省立師範學院改制為臺灣省立師範大學。','1967年，臺灣省立師範大學升格為國立臺灣師範大學。','2022年11月18日，學校網站刊載介紹校史影片的新聞。']
test('9.2','原文长度和字表',[list(map(len,texts)),len(set(''.join(texts))),sum(map(len,texts))],[[17,26,26,28],43,97],'正文9.1四条整理句逐字拷出，码位计数。')
test('9.2','截断填充',[[sum(min(len(s),w) for s in texts),4*w-sum(min(len(s),w) for s in texts)] for w in [20,28]],[[77,3],[97,15]],'按正文长度上限20、28独立计数。')
test('9.2','名称跨度',[texts[0][6:14],texts[1][17:25],texts[2][17:25],texts[1][14:26][3:11]],['臺灣省立師範學院','臺灣省立師範大學','國立臺灣師範大學','臺灣省立師範大學'],'左闭右开范围；窗口起点14加局部[3,11]。')
test('9.3','开发表分母',[6/8,7/8],[.75,.875],'仅表内比例；129维TF-IDF词表及相似度因旧输入/实现缺失不能复现。')
test('9.4','六维向量',[2/math.sqrt(2*3),0,1/math.sqrt(2*2)],[.816497,0,.5],'C01·C02=2、平方范数2/3；C03·C04=1、范数sqrt2各。',tol=.0000005)
test('9.5','证据与类别比率',[5/6,4/6],[.8333333333333334,.6666666666666666],'仅6条分母的算术；原回答/引文完整项未附，不能重新判语义。')
a=['支持','支持','支持','矛盾','矛盾','不足','不足','不足'];b=['支持','支持','支持','矛盾','支持','矛盾','不足','不足'];ca,cb=Counter(a),Counter(b)
po=sum(x==y for x,y in zip(a,b))/8;pe=sum(ca[k]*cb[k] for k in ca)/64
test('9.6','待判排除后的kappa',[po,pe,(po-pe)/(1-pe)],[.75,.34375,13/21],'正文D01—D08逐行计算；D09有待判，不参与此旧例一致率。')
g=['支持','矛盾','不足','支持','矛盾','不足'];a=['支持','矛盾','支持','支持','矛盾','不足'];b=['支持','支持','支持','支持','不足','不足']
test('9.7','跨语言配对',[sum(x==y for x,y in zip(g,a)),sum(x==y for x,y in zip(g,b)),sum(x==y for x,y in zip(a,b)),sum(x==y==z for x,y,z in zip(g,a,b))],[5,3,4,3],'Q01—Q06直接数中文/英文正确、同答、双侧正确。')
test('9.8','覆盖与分组计分',[8+3+3,8+2+2,(8+1+0)/12,(6+2+1)/12,(1+.5+0)/3,(.75+1+.5)/3],[14,12,.75,.75,.5,.75],'公开三组目录/结果表；不是16个独立事件。')
test('10.3','同分不等同答案',[7/8,7/8,2/8],[.875,.875,.25],'假设A仅D04错，B仅D05错；差两项。')
# Independent n-grams and LCS via exhaustive subsequences (short body strings).
clean=lambda s:''.join(c for c in unicodedata.normalize('NFC',s) if not c.isspace() and not unicodedata.category(c).startswith('P'))
def overlaps(ref,cand,n):
    rg=[ref[i:i+n] for i in range(len(ref)-n+1)];cg=[cand[i:i+n] for i in range(len(cand)-n+1)]
    return sum(min(rg.count(t),cg.count(t)) for t in set(cg)),len(cg),len(rg)
ref=clean('甲渡未迁至城北，仍在南岸开渡。')
for name,cand,target in [('B','甲渡已迁至城北，仍在南岸开渡',[.877058,.791067,.923077]),('C','甲渡照旧在南岸渡运，北迁没有实行',[.338062,0,.615385])]:
    cand=clean(cand);prec=[overlaps(ref,cand,n)[0]/overlaps(ref,cand,n)[1] for n in range(1,5)];bp=min(1,math.exp(1-len(ref)/len(cand)))
    derived=[bp*math.sqrt(prec[0]*prec[1]),bp*math.prod(prec)**.25,overlaps(ref,cand,1)[0]/len(ref)]
    test('10.4','正文候选'+name,derived,target,'独立列出字符n-gram多重集合计数；NFC及去标点按原口径。',tol=.0000005)
test('10.4','短句手算',[math.exp(-.2),math.exp(-.2)*math.sqrt(3/4),10/11,2/3],[.818731,.709042,10/11,2/3],'候选5字、参考6字；一元5/5，二元3/4，ROUGE按各自分母。',tol=.0000005)
test('10.4','极短BP及语料级',[math.exp(1-13/2),math.exp(1-10/9)*math.sqrt(6/7),(math.exp(-.2)*math.sqrt(3/4)+1)/2],[.004087,.828460,.854521],'极短D长度2；语料级先合并匹配数，不平均句BLEU。',tol=.0000005)
test('10.5','人工分维度一致率',[6/7,7/8],[.8571428571428571,.875],'正文已列相同数6/7、7/8；不能据此证实真人实验。')
n=20;p=.8;z=1.96;den=1+z*z/n;center=(p+z*z/(2*n))/den;half=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))/den
test('10.7','Wilson参数',[den,center,half],[1.19208,.75166,.16768],'n=20,p=.8,z=1.96直接代式。',tol=.000005)
test('10.7','Wilson全合格下限',1/(1+z*z/20),.839,'p=1时下限n/(n+z²)。',tol=.0005)
dist=sorted(sum(x)/6 for x in product([1,.5,.5,0,0,-.5],repeat=6))
def linear(q):
    h=(len(dist)-1)*q;lo=int(h);return dist[lo]+(dist[min(lo+1,len(dist)-1)]-dist[lo])*(h-lo)
test('10.7','六来源完全枚举',[len(dist),(len(dist)-1)*.025,(len(dist)-1)*.975,linear(.025),linear(.975),min(dist),max(dist)],[46656,1166.375,45488.625,-1/6,2/3,-.5,1],'独立枚举6^6，差值取正文六个来源1,.5,.5,0,0,-.5，不导入workbook。')
test('10.7','配对点估计与指定抽样',[6/12,9/12,(9-6)/12,(1+1+.5+0+0-.5)/6],[.5,.75,.25,1/3],'全部12片段与正文指定一次六来源有放回抽样。')
for b,c,p in [(2,10,79/2048),(0,4,.125),(0,6,.03125),(3,3,1)]:
    outcomes=sum(sum(t)<=min(b,c) for t in product([0,1],repeat=b+c))
    test('10.8',f'精确McNemar({b},{c})',min(1,2*outcomes/2**(b+c)),p,'枚举全部二元序列计数，不调用原函数的组合数公式。')
test('10.9','断言/引用/遗漏分母',[3/6,2/6,5/8,2/8,1/4],[.5,1/3,.625,.25,.25],'只核正文汇总比率，原断言来源包缺失不能重裁全部项。')
test('10.10','继承配对表',[18/30,26/30,(26-18)/30],[.6,26/30,8/30],'不把此30条与新版6条相混。')
scores=[math.exp(-x/.02) for x in [.000011,.044048,.072110]];test('11.1','给定距离的归一化分数',[x/sum(scores) for x in scores],[.8789,.0972,.0239],'只从正文已舍入距离验证softmax，旧17张PGM不在新版包。',tol=.0001)
test('11.1','闭集混淆矩阵',(2+1+2)/6,.8333,'正文3×3矩阵对角线5，分母6。',tol=.00005)
test('11.2','检测计数与阈值',[[3/4,3/6],[3/5,3/6],[2/4,2/6]],[[.75,.5],[.6,.5],[.5,1/3]],'TP/FP/FN公开计数3/1/3、重复探针3/2/3、高IoU2/2/4；不重造旧像素。')
test('11.3','掩膜IoU/Dice',[[12/16,24/28],[8/16,16/24],[16/32,32/48]],[[.75,6/7],[.5,2/3],[.5,2/3]],'正文明确给出的交并/面积直接代式。')
test('11.4','含CLS注意力规模',[14**2+1,28**2+1,197**2,785**2,785**2/197**2],[197,785,38809,616225,15.88],'旧例含CLS；新版输出不含CLS，二者非数值错误。',tol=.005)
test('11.7','Top1/Top5',[2/4,3/4],[.5,.75],'正文给定参考排名1、2、6、1。')
test('11.7','AP积分',[F(1,2)*1+F(1,2)*F(2,3),F(1,2),(F(5,6)+F(1,2))/2],[F(5,6),F(1,2),F(2,3)],'按正文精确率包络，不套新版非插值输入。')
test('11.7','公开像素矩阵',[95/100,(88/93+4/7+3/5)/3,(4/7+3/5)/2],[.95,.7059,.5857],'3×3矩阵行90/5/5，对角88/4/3；排ignore后100像素。',tol=.00005)
for label,matrix,expected in [('A',[[90,0,0],[6,0,0],[4,0,0]],[.9,.3,1/3,.3158]),('B',[[78,8,4],[1,5,0],[1,0,3]],[.86,.5961,.8167,.6631])]:
    support=[sum(row) for row in matrix];pred=[sum(row[c] for row in matrix) for c in range(3)];tp=[matrix[i][i] for i in range(3)]
    precision=[tp[i]/pred[i] if pred[i] else 0 for i in range(3)];recall=[tp[i]/support[i] for i in range(3)];f1=[2*tp[i]/(support[i]+pred[i]) for i in range(3)]
    test('11.8','三类矩阵'+label,[sum(tp)/100,sum(precision)/3,sum(recall)/3,sum(f1)/3],expected,'从正文两张完整混淆矩阵重算；A零预测类按原例约定填零并保留未定义说明。',tol=.00005)
test('11.9','变化百分点',[5/6-2/6,12/16,13/64,(.4+.6)/2*100],[.5,.75,.203125,50],'只算公开数，不复原旧噪声变换图或宣称标准mCE。')
test('11.10','四格效用',[(2-2)/12,(1-2)/12,(10-2)/12,(8-1)/12],[0,-1/12,8/12,7/12],'正文旧12图表；不是新版四张图片。')
test('11.10','交互差中之差',[(7/12-(-1/12))-(8/12-0),(9/12-3/12)-(12/12-4/12)],[0,-2/12],'分别计算效用与覆盖，不混指标。')
for r in records:
    # Fractions are exact audit intermediates; serialize to standard numeric JSON.
    def convert(x):
        if isinstance(x,F):return float(x)
        if isinstance(x,(tuple,list)):return [convert(y) for y in x]
        return x
    r['derived']=convert(r['derived']);r['printed']=convert(r['printed'])
payload={'scope':'旧正文可见数字与字串的独立算术复核；未伪造旧脚本或模型输出','checks':records,'passed':sum(r['status']=='EXECUTED_PASS' for r in records),'failed':sum(r['status']=='FAIL' for r in records),'blocked':'旧版完整输入/逐项输出/运行环境不在本交付包：旧模型调用、TF-IDF129维词表/旧向量相似度、旧图像全链路及没有逐项材料的汇总，只能验证已公开算术，不能声称原实验复现。'}
with (OUT/'body_arithmetic.json').open('x') as f:json.dump(payload,f,ensure_ascii=False,indent=2)
print(json.dumps({'passed':payload['passed'],'failed':[(r['section'],r['name'],r['derived'],r['printed']) for r in records if r['status']=='FAIL']},ensure_ascii=False))

# 第10—11章全部引用URL台账

共76个不同URL（第10章28、第11章48；跨章去重后计），全部已核相关段落，未核0；不代表旧执行记录已经复算。
ImageNet直连超时但原站索引/官方同文相关段落可读，方式单列，不计为直接页面成功。

## S1011-01｜已核相关段落
- 引用URL：https://arxiv.org/html/2107.13586v1
- 实际核读：https://arxiv.org/html/2107.13586v1
- 位置与主张：§2.2、表2与§2.2.1：模板输入槽与答案槽、填入材料后的prompt、answer及answered prompt区分。
- 书稿：10.1 Prompt模板设计，基线L112；[1] Liu等，2021，[Pre-train, Prompt, and Predict](https://arxiv.org/html/2107.13586v1)，第2.2.1节与表2：模板、填入材料后的Prompt及回答的区分。

## S1011-02｜已核相关段落
- 引用URL：https://arxiv.org/pdf/2005.14165
- 实际核读：https://arxiv.org/pdf/2005.14165
- 位置与主张：原论文PDF6—7页§2：K个context/completion示范，无权重更新；zero-shot无示范但可含任务指令。
- 书稿：10.1 Prompt模板设计，基线L114；[2] Brown等，2020，[Language Models are Few-Shot Learners](https://arxiv.org/pdf/2005.14165)，第2节、PDF第7页：零样本设置不提供已作答示范。本节未运行论文模型或复用其实验材料。
- 书稿：10.2 Few-shot示例选择与k-shot评测协议，基线L207；[1] Brown等，2020，[Language Models are Few-Shot Learners](https://arxiv.org/pdf/2005.14165)，第2节、PDF第6—7页：上下文示范、k的含义及不更新参数的设置。

## S1011-03｜已核相关段落
- 引用URL：https://proceedings.mlr.press/v139/zhao21c/zhao21c.pdf
- 实际核读：https://proceedings.mlr.press/v139/zhao21c/zhao21c.pdf
- 位置与主张：原论文§2及图2：format、示例集合、排列三组件；固定集合换排列的区别，与本章说明相符。
- 书稿：10.2 Few-shot示例选择与k-shot评测协议，基线L209；[2] Zhao等，2021，[Calibrate Before Use](https://proceedings.mlr.press/v139/zhao21c/zhao21c.pdf)，第2节与图2：示例集合、排列及选择变化。本节未复跑其模型或校准方法。
- 书稿：10.3 Prompt敏感度分析，基线L307；[1] Zhao等，2021，[Calibrate Before Use](https://proceedings.mlr.press/v139/zhao21c/zhao21c.pdf)，第2节：模板、示例集合与排列的区分。

## S1011-04｜已核相关段落
- 引用URL：https://proceedings.neurips.cc/paper/2021/file/5c04925674920eb58467fb52ce4ef728-Paper.pdf
- 实际核读：https://proceedings.neurips.cc/paper/2021/file/5c04925674920eb58467fb52ce4ef728-Paper.pdf
- 位置与主张：§1—2：额外held-out数据用于选择与true few-shot仅给定少量例的区别。
- 书稿：10.2 Few-shot示例选择与k-shot评测协议，基线L211；[3] Perez等，2021，[True Few-Shot Learning with Language Models](https://proceedings.neurips.cc/paper/2021/file/5c04925674920eb58467fb52ce4ef728-Paper.pdf)，第1—2节：使用额外开发材料选择方案与仅依赖少量示例的区别。

## S1011-05｜已核相关段落
- 引用URL：https://aclanthology.org/2022.acl-long.556.pdf
- 实际核读：https://aclanthology.org/2022.acl-long.556.pdf
- 位置与主张：原论文PDF第2页§2：固定四例、24种排列，支持示例集合不变的换序检验。
- 书稿：10.3 Prompt敏感度分析，基线L309；[2] Lu等，2022，[Fantastically Ordered Prompts and Where to Find Them](https://aclanthology.org/2022.acl-long.556.pdf)，第2节、PDF第2页：固定示例集合后比较排列。未复跑论文模型、排列全集或性能数字。

## S1011-06｜已核相关段落
- 引用URL：https://aclanthology.org/2020.acl-main.442.pdf
- 实际核读：https://aclanthology.org/2020.acl-main.442.pdf
- 位置与主张：§2.1—2.2不变性、最小功能及方向性测试；正文只借任务相关扰动思路。本人已读引言与示例，精确§2.2同时复核父校对员本轮sources_ch09.json S09-33证据。
- 书稿：10.3 Prompt敏感度分析，基线L311；[3] Ribeiro等，2020，[Beyond Accuracy](https://aclanthology.org/2020.acl-main.442.pdf)，第2.2节、PDF第3页：保持标签的扰动与预测不变检查。本节借用检查思路，没有运行CheckList软件。

## S1011-07｜已核相关段落
- 引用URL：https://aclanthology.org/P02-1040.pdf
- 实际核读：https://aclanthology.org/P02-1040.pdf
- 位置与主张：§2.1截断匹配计数、§2.3语料级长度惩罚与加权几何平均；正文字符化和短句null为明示的教学约定。
- 书稿：10.4 n-gram评测：BLEU与ROUGE，基线L407；[1] Papineni等，2002，[BLEU: a Method for Automatic Evaluation of Machine Translation](https://aclanthology.org/P02-1040.pdf)，第2.1、2.2、2.3节：截断计数、语料汇总、长度惩罚与等权几何平均。

## S1011-08｜已核相关段落
- 引用URL：https://aclanthology.org/W04-1013.pdf
- 实际核读：https://aclanthology.org/W04-1013.pdf
- 位置与主张：§2 ROUGE-N召回分母，§3.1 LCS定义、P/R与F；摘要级与单序列区别另核官方实现README。本书F1不冒充原论文所有beta设置。
- 书稿：10.4 n-gram评测：BLEU与ROUGE，基线L409；[2] Lin，2004，[ROUGE: A Package for Automatic Evaluation of Summaries](https://aclanthology.org/W04-1013.pdf)，第2、3.1、3.2节：ROUGE-N、LCS及句级与摘要级的区别。

## S1011-09｜已核相关段落
- 引用URL：https://aclanthology.org/W14-3346.pdf
- 实际核读：https://aclanthology.org/W14-3346.pdf
- 位置与主张：§1—2：高阶匹配为0使无平滑几何平均为0；不同平滑会改变句级BLEU。
- 书稿：10.4 n-gram评测：BLEU与ROUGE，基线L411；[3] Chen与Cherry，2014，[A Systematic Comparison of Smoothing Techniques for Sentence-Level BLEU](https://aclanthology.org/W14-3346.pdf)，第1、2节：高阶零匹配及平滑方法。

## S1011-10｜已核相关段落
- 引用URL：https://github.com/mjpost/sacrebleu/blob/master/sacrebleu/metrics/bleu.py
- 实际核读：https://raw.githubusercontent.com/mjpost/sacrebleu/master/sacrebleu/metrics/bleu.py
- 位置与主张：compute_bleu官方代码229—267行：短候选BP、无匹配返回0、total=0截断、effective_order选择有效阶数与平滑；本节null是自定约定。
- 书稿：10.4 n-gram评测：BLEU与ROUGE，基线L413；[4] SacreBLEU官方实现，[BLEU.compute_bleu](https://github.com/mjpost/sacrebleu/blob/master/sacrebleu/metrics/bleu.py)，`effective_order`与零计数处理，核读于2026年10月25日；本节没有运行该库。

## S1011-11｜已核相关段落
- 引用URL：https://github.com/google-research/google-research/blob/master/rouge/README.md
- 实际核读：https://raw.githubusercontent.com/google-research/google-research/master/rouge/README.md
- 位置与主张：Two flavors of ROUGE-L：rougeL忽略换行，rougeLsum按句界计算union-LCS；支持正文自定单序列与标准摘要口径区别。
- 书稿：10.4 n-gram评测：BLEU与ROUGE，基线L415；[5] Google Research，[ROUGE说明](https://github.com/google-research/google-research/blob/master/rouge/README.md)，两种ROUGE-L计算方式；本节未运行该软件包。

## S1011-12｜已核相关段落
- 引用URL：https://aclanthology.org/2021.tacl-1.24.pdf
- 实际核读：https://aclanthology.org/2021.tacl-1.24.pdf
- 位置与主张：§4.3：coherence/consistency/fluency/relevance四维、给评员来源与候选、随机排列，支持分维度及来源依据；本书三维量表为自编非照搬。
- 书稿：10.5 人工评估金标准与质量控制，基线L505；[1] Fabbri等，2021，[SummEval](https://aclanthology.org/2021.tacl-1.24.pdf)，第4.3节及附录数据采集说明：区分评价维度，先读来源再评摘要。本节三维度和刻度为教学设计，并非照搬论文量表。

## S1011-13｜已核相关段落
- 引用URL：https://aclanthology.org/2021.tacl-1.87.pdf
- 实际核读：https://aclanthology.org/2021.tacl-1.87.pdf
- 位置与主张：§3.3、表1—2及§3.4末段：具体错误位置、全文上下文、评阅者能力、匿名系统和随机顺序；不照搬其加权分数。
- 书稿：10.5 人工评估金标准与质量控制，基线L507；[2] Freitag等，2021，[Experts, Errors, and Context](https://aclanthology.org/2021.tacl-1.87.pdf)，第3.3节、表1及第3.4节：错误位置、上下文、评阅能力、匿名化和呈现安排；不复用其评分权重或研究数据。

## S1011-14｜已核相关段落
- 引用URL：https://aclanthology.org/2020.inlg-1.23.pdf
- 实际核读：https://aclanthology.org/2020.inlg-1.23.pdf
- 位置与主张：§4.2.3及§5：问题可能混入多个维度，定义与操作说明需明确；支持分别报告评价问题和指令。
- 书稿：10.5 人工评估金标准与质量控制，基线L509；[3] Howcroft等，2020，[Twenty Years of Confusion in Human Evaluation](https://aclanthology.org/2020.inlg-1.23.pdf)，第4.2.3、5节及表7：维度定义、实际问题、指令与报告信息。

## S1011-15｜已核相关段落
- 引用URL：https://aclanthology.org/W19-8643.pdf
- 实际核读：https://aclanthology.org/W19-8643.pdf
- 位置与主张：§4.4与表3 Design行：固定呈现顺序可造成疲劳/练习等效应，建议随机化/平衡并报告。
- 书稿：10.5 人工评估金标准与质量控制，基线L511；[4] van der Lee等，2019，[Best Practices for the Human Evaluation of Automatically Generated Text](https://aclanthology.org/W19-8643.pdf)，第4节、表3的Design项：呈现顺序及其报告。

## S1011-16｜已核相关段落
- 引用URL：https://arxiv.org/html/2306.05685v4
- 实际核读：https://arxiv.org/html/2306.05685v4
- 位置与主张：§3.1—3.4：单答评分、成对比较、参考引导；位置/冗长偏好与自偏好须区别，原文不确认普遍自偏好。正文亦保留此限。
- 书稿：10.6 LLM-as-Judge协议，基线L592；[1] Zheng et al. (2023), *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena*，§3.1–3.4。参见[原论文](https://arxiv.org/html/2306.05685v4)。

## S1011-17｜已核相关段落
- 引用URL：https://aclanthology.org/2023.emnlp-main.153.pdf
- 实际核读：https://aclanthology.org/2023.emnlp-main.153.pdf
- 位置与主张：§2 Method及图1：任务定义、评价标准、步骤与评分函数分开；正文自编协议不是复刻概率加权G-Eval。
- 书稿：10.6 LLM-as-Judge协议，基线L594；[2] Liu et al. (2023), *G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment*，§2。参见[原论文](https://aclanthology.org/2023.emnlp-main.153.pdf)。

## S1011-18｜已核相关段落
- 引用URL：https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm
- 实际核读：https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm
- 位置与主张：NIST公式段及Terminology Note：Wilson分母、中心与半宽公式相符；与精确二项区间不同。
- 书稿：10.7 Bootstrap置信区间，基线L694；[1] [NIST 比例置信区间](https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm)。

## S1011-19｜已核相关段落
- 引用URL：https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bootstrap.html
- 实际核读：https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bootstrap.html
- 位置与主张：官方文档percentile步骤、paired参数与method：同索引成对抽样、百分位/basic/BCa区别；不保证本文少量来源穷举区间覆盖率。
- 书稿：10.7 Bootstrap置信区间，基线L696；[2] [SciPy bootstrap官方文档](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bootstrap.html)。

## S1011-20｜已核相关段落
- 引用URL：https://cameron.econ.ucdavis.edu/research/Cameron_Miller_JHR_2015_February.pdf
- 实际核读：https://cameron.econ.ucdavis.edu/research/Cameron_Miller_JHR_2015_February.pdf
- 位置与主张：摘要与II.D/VI.C相关段：组内相关、整组有放回抽样、小组数bootstrap风险；支持本文整组抽样且不将6组穷举冒称精确覆盖保证。
- 书稿：10.7 Bootstrap置信区间，基线L698；[3] [Cameron与Miller 聚类稳健推断作者稿](https://cameron.econ.ucdavis.edu/research/Cameron_Miller_JHR_2015_February.pdf)。

## S1011-21｜已核相关段落
- 引用URL：https://itl.nist.gov/div898/software/dataplot/refman1/auxillar/mcnemar.htm
- 实际核读：https://itl.nist.gov/div898/software/dataplot/refman1/auxillar/mcnemar.htm
- 位置与主张：Description及assumptions：二元配对、配对单位独立、比较两种不一致对概率；列出小样本二项与大样本近似。
- 书稿：10.8 McNemar检验，基线L788；[1] NIST Dataplot，McNemar Test。核对配对二元变量、配对单位相互独立及精确／近似检验的区分。https://itl.nist.gov/div898/software/dataplot/refman1/auxillar/mcnemar.htm

## S1011-22｜已核相关段落
- 引用URL：https://www.statsmodels.org/stable/_modules/statsmodels/stats/contingency_tables.html
- 实际核读：https://www.statsmodels.org/stable/_modules/statsmodels/stats/contingency_tables.html
- 位置与主张：mcnemar函数1638—1709行：exact用min(n1,n2)、二项CDF乘2截1，correction仅近似分支。
- 书稿：10.8 McNemar检验，基线L790；[2] statsmodels官方源码，`mcnemar`函数。核对二项分布双侧计算、乘2后截到1及连续性校正仅用于近似版本。https://www.statsmodels.org/stable/_modules/statsmodels/stats/contingency_tables.html

## S1011-23｜已核相关段落
- 引用URL：https://aclanthology.org/2023.emnlp-main.741/
- 实际核读：https://aclanthology.org/2023.emnlp-main.741/
- 位置与主张：ACL原论文摘要：将长文本拆为atomic facts，并求可靠知识来源支持的比例；只支持方法定义，不为本章虚构渡口背书。
- 书稿：10.9 幻觉的评测与缓解，基线L873；[1] Min, S. 等，2023，FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation，EMNLP，12076–12100。https://aclanthology.org/2023.emnlp-main.741/

## S1011-24｜已核相关段落
- 引用URL：https://aclanthology.org/2023.emnlp-main.398/
- 实际核读：https://aclanthology.org/2023.emnlp-main.398.pdf
- 位置与主张：原论文PDF§3.3 Citation Quality及图3已在同一校对轮6—8来源S16核读：引文位置与实质支持区分；无关引文与覆盖分别评价。
- 书稿：10.9 幻觉的评测与缓解，基线L875；[2] Gao, T. 等，2023，Enabling Large Language Models to Generate Text with Citations，EMNLP，6465–6488。https://aclanthology.org/2023.emnlp-main.398/

## S1011-25｜已核相关段落
- 引用URL：https://arxiv.org/html/1810.03993v2
- 实际核读：https://arxiv.org/html/1810.03993v2
- 位置与主张：§4.3.4—4.7：评价因素、阈值、变异和置信区间、评价数据预处理、分组结果；支持正文卡片条件，不证明教学数据真实性。
- 书稿：10.10 Model Card与Datasheet for Datasets，基线L945；[1] Mitchell等，Model Cards for Model Reporting，2019，§4。https://arxiv.org/html/1810.03993v2

## S1011-26｜已核相关段落
- 引用URL：https://arxiv.org/html/1803.09010v8
- 实际核读：https://arxiv.org/pdf/1803.09010v8
- 位置与主张：原论文PDF§1.1、§3.4、§3.7和§4同一轮已核：可按领域调整、原始处理记录、维护更新；不把填表当认证。
- 书稿：10.10 Model Card与Datasheet for Datasets，基线L947；[2] Gebru等，Datasheets for Datasets，2021版本，§1.1、§3、§4。https://arxiv.org/html/1803.09010v8

## S1011-27｜已核相关段落
- 引用URL：https://huggingface.co/docs/hub/model-cards
- 实际核读：https://huggingface.co/docs/hub/model-cards
- 位置与主张：What are Model Cards：README形式、用途限制、训练参数/数据/评价结果，支持作为官方实现入口。
- 书稿：10.10 Model Card与Datasheet for Datasets，基线L949；[3] Hugging Face，Model Cards，官方实现说明。https://huggingface.co/docs/hub/model-cards

## S1011-28｜已核相关段落
- 引用URL：https://huggingface.co/docs/hub/datasets-cards
- 实际核读：https://huggingface.co/docs/hub/datasets-cards
- 位置与主张：What are Dataset Cards及metadata：README描述内容/用途背景/偏差、许可语言大小；支持官方数据卡入口，不产生新的使用许可。
- 书稿：10.10 Model Card与Datasheet for Datasets，基线L951；[4] Hugging Face，Dataset Cards，官方实现说明。https://huggingface.co/docs/hub/datasets-cards

## S1011-29｜已核相关段落
- 引用URL：https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation-iterators-for-grouped-data
- 实际核读：https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation-iterators-for-grouped-data
- 位置与主张：§3.1首段/开发集段及§3.1.2.4：训练测试分开，调参可泄漏测试；相关组会破坏iid，验证组不得在训练中出现，GroupKFold保证组不跨界。
- 书稿：11.1 分类：从图片到类别概率向量，基线L85；[1] scikit-learn，Cross-validation，§3.1.2.4，分组材料的评价划分。https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation-iterators-for-grouped-data

## S1011-30｜已核相关段落
- 引用URL：https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestCentroid.html
- 实际核读：https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestCentroid.html
- 位置与主张：方法定义L638—650：每类由质心代表，测试样本归最近质心；欧氏质心为算术平均。正文只借思想，不称复刻软件所有先验/收缩细节。
- 书稿：11.1 分类：从图片到类别概率向量，基线L87；[2] scikit-learn，NearestCentroid，方法定义。本节仅采用最近质心思想，不复刻该软件全部实现。https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestCentroid.html

## S1011-31｜已核相关段落
- 引用URL：https://proceedings.mlr.press/v70/guo17a.html
- 实际核读：https://proceedings.mlr.press/v70/guo17a/guo17a.pdf
- 位置与主张：原论文摘要：概率校准定义及现代神经网络可能未校准；网页入口访问失败，官方原论文PDF可读。
- 书稿：11.1 分类：从图片到类别概率向量，基线L89；[3] Guo等，On Calibration of Modern Neural Networks，2017，摘要与论文。https://proceedings.mlr.press/v70/guo17a.html

## S1011-32｜已核相关段落
- 引用URL：https://scikit-learn.org/stable/modules/model_evaluation.html#confusion-matrix
- 实际核读：https://scikit-learn.org/stable/modules/model_evaluation.html#confusion-matrix
- 位置与主张：§3.4.4.6：混淆矩阵按真实类为行；正文已注明参考行/预测列，与表格一致。
- 书稿：11.1 分类：从图片到类别概率向量，基线L91；[4] scikit-learn，Metrics and scoring，§3.4.4.6，Confusion matrix。https://scikit-learn.org/stable/modules/model_evaluation.html#confusion-matrix

## S1011-33｜已核相关段落
- 引用URL：https://guides.loc.gov/migrant-mother
- 实际核读：https://guides.loc.gov/migrant-mother
- 位置与主张：Introduction第2段及rights入口：1936年3月系列照片、Lange、Florence Owens Thompson及无已知使用限制；未据此新授许可。
- 书稿：11.1 分类：从图片到类别概率向量，基线L93；[5] Library of Congress，Dorothea Lange's “Migrant Mother” Photographs，Introduction。馆方写无已知使用限制，不是本书新授予的许可；本包只提供链接，不收录照片。https://guides.loc.gov/migrant-mother

## S1011-34｜已核相关段落
- 引用URL：https://github.com/cocodataset/cocoapi/blob/master/PythonAPI/pycocotools/cocoeval.py
- 实际核读：https://raw.githubusercontent.com/cocodataset/cocoapi/master/PythonAPI/pycocotools/cocoeval.py
- 位置与主张：Params.setDetParams：十IoU及101召回点、maxDets/areaRng；_prepare与evaluateImg核ignore/crowd及普通框不重复匹配；accumulate L377—387右侧最大包络后在recThrs采样。正文明确教学全点面积不是完整COCO。
- 书稿：11.2 检测：bbox回归与分类的联合任务，基线L171；[1] COCO官方工具，cocoeval.py，参数说明与检测评价实现。https://github.com/cocodataset/cocoapi/blob/master/PythonAPI/pycocotools/cocoeval.py
- 书稿：11.7 Top-1/mAP/mIoU指标族，基线L610；[2] COCO官方工具，cocoeval.py，Params.setDetParams、evaluateImg、accumulate及_summarizeDets。https://github.com/cocodataset/cocoapi/blob/master/PythonAPI/pycocotools/cocoeval.py

## S1011-35｜已核相关段落
- 引用URL：https://arxiv.org/abs/2005.12872
- 实际核读：https://arxiv.org/html/2005.12872v3
- 位置与主张：摘要、图1、§3.1及3.2预测FFN：二分匹配、固定查询、不匹配槽用no-object；无需NMS不等于没有匹配评价。
- 书稿：11.2 检测：bbox回归与分类的联合任务，基线L173；[2] Carion等，End-to-End Object Detection with Transformers，2020。https://arxiv.org/abs/2005.12872

## S1011-36｜已核相关段落
- 引用URL：https://arxiv.org/abs/2010.04159
- 实际核读：https://arxiv.org/html/2010.04159v4
- 位置与主张：摘要及§4.1式3：参考点附近稀疏采样、跨多尺度LK点聚合，慢收敛与小对象动机；不是简单名称扩写。
- 书稿：11.2 检测：bbox回归与分类的联合任务，基线L175；[3] Zhu等，Deformable DETR: Deformable Transformers for End-to-End Object Detection，2020／ICLR 2021。https://arxiv.org/abs/2010.04159

## S1011-37｜已核相关段落
- 引用URL：https://arxiv.org/abs/2203.03605
- 实际核读：https://arxiv.org/abs/2203.03605
- 位置与主张：作者原摘要：contrastive denoising、mixed query selection、look-forward-twice box prediction；不把论文排名推及历史图像。
- 书稿：11.2 检测：bbox回归与分类的联合任务，基线L177；[4] Zhang等，DINO: DETR with Improved DeNoising Anchor Boxes for End-to-End Object Detection，2022。https://arxiv.org/abs/2203.03605

## S1011-38｜已核相关段落
- 引用URL：https://arxiv.org/abs/2304.07193
- 实际核读：https://arxiv.org/html/2304.07193v2
- 位置与主张：§4图像/patch自监督目标、EMA教师；§7冻结特征分类/分割评估（表10），与表征提取及任务头区分相符。
- 书稿：11.2 检测：bbox回归与分类的联合任务，基线L179；[5] Oquab等，DINOv2: Learning Robust Visual Features without Supervision，2023。https://arxiv.org/abs/2304.07193

## S1011-39｜已核相关段落
- 引用URL：https://arxiv.org/abs/2304.02643
- 实际核读：https://arxiv.org/abs/2304.02643
- 位置与主张：作者原摘要与2023投稿日期：SAM为promptable segmentation；具体点/框/掩膜接口另核官方代码。
- 书稿：11.3 分割：像素级分类与SAM提示分割，基线L253；[1] Kirillov等，Segment Anything，2023。https://arxiv.org/abs/2304.02643

## S1011-40｜已核相关段落
- 引用URL：https://github.com/facebookresearch/segment-anything
- 实际核读：https://raw.githubusercontent.com/facebookresearch/segment-anything/main/README.md
- 位置与主张：官方README首段与Getting Started：点/框可提示掩码、可自动全图生成；与原模型接口说明相符，不支撑本地连通域算法等于SAM。
- 书稿：11.3 分割：像素级分类与SAM提示分割，基线L255；[2] Meta官方SAM仓库与提示接口。https://github.com/facebookresearch/segment-anything ；https://github.com/facebookresearch/segment-anything/blob/main/segment_anything/predictor.py

## S1011-41｜已核相关段落
- 引用URL：https://github.com/facebookresearch/segment-anything/blob/main/segment_anything/predictor.py
- 实际核读：https://raw.githubusercontent.com/facebookresearch/segment-anything/main/segment_anything/predictor.py
- 位置与主张：predict参数文档L82—107：点XY、1前景/0背景标签、框XYXY、可选低分辨率掩码；multimask_output为真时输出3个歧义候选。
- 书稿：11.3 分割：像素级分类与SAM提示分割，基线L255；[2] Meta官方SAM仓库与提示接口。https://github.com/facebookresearch/segment-anything ；https://github.com/facebookresearch/segment-anything/blob/main/segment_anything/predictor.py

## S1011-42｜已核相关段落
- 引用URL：https://arxiv.org/abs/2408.00714
- 实际核读：https://arxiv.org/abs/2408.00714
- 位置与主张：作者原摘要：图像与视频可提示分割、streaming memory；不把性能百分数转入本章。
- 书稿：11.3 分割：像素级分类与SAM提示分割，基线L257；[3] Ravi等，SAM 2: Segment Anything in Images and Videos，2024。https://arxiv.org/abs/2408.00714

## S1011-43｜已核相关段落
- 引用URL：https://github.com/facebookresearch/sam2
- 实际核读：https://raw.githubusercontent.com/facebookresearch/sam2/main/README.md
- 位置与主张：官方README Image prediction与Video prediction：图像predictor与视频state、add_new_points_or_box及propagate接口；与视频扩展说明相符。
- 书稿：11.3 分割：像素级分类与SAM提示分割，基线L259；[4] Meta官方SAM 2仓库，Image prediction及Video prediction部分。https://github.com/facebookresearch/sam2

## S1011-44｜已核相关段落
- 引用URL：https://arxiv.org/abs/1512.03385
- 实际核读：https://arxiv.org/html/1512.03385v1
- 位置与主张：§3.2式1—2及图2：F(x)+x逐元素加法，维度不同时用投影Ws；支持残差连接解释。
- 书稿：11.4 从CNN到ViT：架构与迁移路线，基线L338；[1] He等，Deep Residual Learning for Image Recognition，2015，摘要及3.2节。https://arxiv.org/abs/1512.03385

## S1011-45｜已核相关段落
- 引用URL：https://arxiv.org/html/2010.11929v2
- 实际核读：https://arxiv.org/html/2010.11929v2
- 位置与主张：§3.1与图1、式1：P×P块、N=HW/P²、训练线性投影、CLS与位置嵌入；支持正文token和注意力长度口径，不证明总显存按L²增长。
- 书稿：11.4 从CNN到ViT：架构与迁移路线，基线L340；[2] Dosovitskiy等，An Image is Worth 16x16 Words，2021年v2，3.1、3.2节及附录A。https://arxiv.org/html/2010.11929v2

## S1011-46｜已核相关段落
- 引用URL：https://docs.pytorch.org/tutorials/beginner/transfer_learning_tutorial.html
- 实际核读：https://docs.pytorch.org/tutorials/beginner/transfer_learning_tutorial.html
- 位置与主张：Two major transfer learning scenarios及ConvNet as fixed feature extractor：预训练初始化微调，与冻结网络仅训末层区分；requires_grad=False不省前向计算。
- 书稿：11.4 从CNN到ViT：架构与迁移路线，基线L342；[3] PyTorch，Transfer Learning for Computer Vision Tutorial，固定特征提取与微调说明。https://docs.pytorch.org/tutorials/beginner/transfer_learning_tutorial.html

## S1011-47｜已核相关段落
- 引用URL：https://keras.io/guides/transfer_learning/
- 实际核读：https://keras.io/guides/transfer_learning/
- 位置与主张：Important notes about BatchNormalization：非训练权重均值方差、trainable=False与推断模式特例；微调应保持BN推断；小学习率及改trainable后重compile。
- 书稿：11.4 从CNN到ViT：架构与迁移路线，基线L344；[4] Keras，Transfer learning & fine-tuning，冻结、解冻及BatchNormalization注意事项。https://keras.io/guides/transfer_learning/

## S1011-48｜已核相关段落
- 引用URL：https://arxiv.org/html/2304.07193v2
- 实际核读：https://arxiv.org/html/2304.07193v2
- 位置与主张：§4图像/patch自监督目标、EMA教师；§7冻结特征分类/分割评估（表10），与表征提取及任务头区分相符。
- 书稿：11.5 DINOv2与特征质量评估，基线L418；[1] Oquab等，DINOv2原论文v2，2024，§4、§7.1、附录B.3：[论文全文](https://arxiv.org/html/2304.07193v2)。用于自监督、冻结评价概念；本文没有复现论文基准分数。

## S1011-49｜已核相关段落
- 引用URL：https://github.com/facebookresearch/dinov2
- 实际核读：https://raw.githubusercontent.com/facebookresearch/dinov2/main/README.md
- 位置与主张：README Pretrained backbones、Pretrained heads与语义分割：无标签142M预训练、ViT特征及另接任务头；不与检测DINO混同。
- 书稿：11.5 DINOv2与特征质量评估，基线L420；[2] Meta官方仓库README，Pretrained backbones与Pretrained heads：[仓库](https://github.com/facebookresearch/dinov2)。用于骨干、任务头和模型命名区分。

## S1011-50｜已核相关段落
- 引用URL：https://github.com/facebookresearch/dinov2/blob/main/dinov2/models/vision_transformer.py
- 实际核读：https://github.com/facebookresearch/dinov2/blob/main/dinov2/models/vision_transformer.py
- 位置与主张：forward_features返回CLS和patch键；vit_small定义embed_dim=384；self.norm是网络归一化，不能推出单位L2长度。
- 书稿：11.5 DINOv2与特征质量评估，基线L422；[3] Meta官方“旧例中的vision_transformer.py”，`forward_features`；“旧例中的hub/backbones.py”；“旧例中的data/transforms.py”：[特征接口](https://github.com/facebookresearch/dinov2/blob/main/dinov2/models/vision_transformer.py)、[骨干参数](https://github.com/facebookresearch/dinov2/blob/main/dinov2/hub/backbones.py)、[预处理](https://github.com/facebookresearch/dinov2/blob/main/dinov2/data/transforms.py)。用于提取示例的接口和形状核对。

## S1011-51｜已核相关段落
- 引用URL：https://github.com/facebookresearch/dinov2/blob/main/dinov2/hub/backbones.py
- 实际核读：https://raw.githubusercontent.com/facebookresearch/dinov2/main/dinov2/hub/backbones.py
- 位置与主张：L27—41默认patch_size14、num_register_tokens0；dinov2_vits14使用vit_small；reg版另设4个register。
- 书稿：11.5 DINOv2与特征质量评估，基线L422；[3] Meta官方“旧例中的vision_transformer.py”，`forward_features`；“旧例中的hub/backbones.py”；“旧例中的data/transforms.py”：[特征接口](https://github.com/facebookresearch/dinov2/blob/main/dinov2/models/vision_transformer.py)、[骨干参数](https://github.com/facebookresearch/dinov2/blob/main/dinov2/hub/backbones.py)、[预处理](https://github.com/facebookresearch/dinov2/blob/main/dinov2/data/transforms.py)。用于提取示例的接口和形状核对。

## S1011-52｜已核相关段落
- 引用URL：https://github.com/facebookresearch/dinov2/blob/main/dinov2/data/transforms.py
- 实际核读：https://raw.githubusercontent.com/facebookresearch/dinov2/main/dinov2/data/transforms.py
- 位置与主张：make_classification_eval_transform：默认resize256、bicubic、center_crop224、ToTensor及Normalize。仅核实现，不证明旧例实际执行。
- 书稿：11.5 DINOv2与特征质量评估，基线L422；[3] Meta官方“旧例中的vision_transformer.py”，`forward_features`；“旧例中的hub/backbones.py”；“旧例中的data/transforms.py”：[特征接口](https://github.com/facebookresearch/dinov2/blob/main/dinov2/models/vision_transformer.py)、[骨干参数](https://github.com/facebookresearch/dinov2/blob/main/dinov2/hub/backbones.py)、[预处理](https://github.com/facebookresearch/dinov2/blob/main/dinov2/data/transforms.py)。用于提取示例的接口和形状核对。

## S1011-53｜已核相关段落
- 引用URL：https://github.com/facebookresearch/dinov2/blob/main/MODEL_CARD.md
- 实际核读：https://raw.githubusercontent.com/facebookresearch/dinov2/main/MODEL_CARD.md
- 位置与主张：模型描述与Uses/Bias：CLS与patch特征，ViT-S384维、patch14、224输入256patch，register版另有4；卡片指出西方及富裕家庭偏差。
- 书稿：11.5 DINOv2与特征质量评估，基线L424；[4] Meta官方MODEL_CARD，Bias, Risks, and Limitations：[模型卡](https://github.com/facebookresearch/dinov2/blob/main/MODEL_CARD.md)。公开来源查阅于2026年10月25日。

## S1011-54｜已核相关段落
- 引用URL：https://www.image-net.org/challenges/LSVRC/2012/
- 实际核读：https://ftp.image-net.org/challenges/LSVRC/2012/index.php
- 位置与主张：原URL两次直连超时；官方同页ftp主机索引正文Data与Task1完整可读：1000类、约1.2m训练、50k验证及剩余100k测试、最多5个排序标签。核验方式为官方同文搜索索引，非第三方转述。
- 书稿：11.6 ImageNet/COCO/ADE20K：三大benchmark，基线L510；[1] ImageNet，ILSVRC2012，Data与Task 1。https://www.image-net.org/challenges/LSVRC/2012/ ；类别组织见官方介绍 https://www.image-net.org/about.php

## S1011-55｜已核相关段落
- 引用URL：https://www.image-net.org/about.php
- 实际核读：https://www.image-net.org/about.php
- 位置与主张：直连超时；原URL的搜索索引完整正文What is ImageNet/Does ImageNet own images段可读：WordNet层级与synset、项目不拥有图片版权。核验方式为原站索引文本，不宣称直接页面成功。
- 书稿：11.6 ImageNet/COCO/ADE20K：三大benchmark，基线L510；[1] ImageNet，ILSVRC2012，Data与Task 1。https://www.image-net.org/challenges/LSVRC/2012/ ；类别组织见官方介绍 https://www.image-net.org/about.php

## S1011-56｜已核相关段落
- 引用URL：https://raw.githubusercontent.com/cocodataset/cocodataset.github.io/master/dataset/download.htm
- 实际核读：https://raw.githubusercontent.com/cocodataset/cocodataset.github.io/master/dataset/download.htm
- 位置与主张：Images表2017 Train118K、Val5K、Test41K；Overview指出split年份是划分发布年份、不是标注年份。
- 书稿：11.6 ImageNet/COCO/ADE20K：三大benchmark，基线L512；[2] COCO官方网页源，download的2017 Update及detection-2017。https://raw.githubusercontent.com/cocodataset/cocodataset.github.io/master/dataset/download.htm ；https://raw.githubusercontent.com/cocodataset/cocodataset.github.io/master/dataset/detection-2017.htm

## S1011-57｜已核相关段落
- 引用URL：https://raw.githubusercontent.com/cocodataset/cocodataset.github.io/master/dataset/detection-2017.htm
- 实际核读：https://raw.githubusercontent.com/cocodataset/cocodataset.github.io/master/dataset/detection-2017.htm
- 位置与主张：§1 Overview：80对象类；bounding box与object segmentation两项挑战；训练验证标注可取得、2017重新安排train/val。
- 书稿：11.6 ImageNet/COCO/ADE20K：三大benchmark，基线L512；[2] COCO官方网页源，download的2017 Update及detection-2017。https://raw.githubusercontent.com/cocodataset/cocodataset.github.io/master/dataset/download.htm ；https://raw.githubusercontent.com/cocodataset/cocodataset.github.io/master/dataset/detection-2017.htm

## S1011-58｜已核相关段落
- 引用URL：https://raw.githubusercontent.com/cocodataset/cocodataset.github.io/master/dataset/format-data.htm
- 实际核读：https://raw.githubusercontent.com/cocodataset/cocodataset.github.io/master/dataset/format-data.htm
- 位置与主张：§1 Object Detection与annotation结构：左上角0索引、bbox[x,y,width,height]、category_id与iscrowd，区别多边形和RLE。
- 书稿：11.6 ImageNet/COCO/ADE20K：三大benchmark，基线L514；[3] COCO官方Data format，Object Detection。https://raw.githubusercontent.com/cocodataset/cocodataset.github.io/master/dataset/format-data.htm

## S1011-59｜已核相关段落
- 引用URL：https://cocodataset.org/dataset/detection-eval.htm
- 实际核读：https://cocodataset.org/dataset/detection-eval.htm
- 位置与主张：§2 Metrics及说明1—7：AP跨.50:.05:.95十IoU与80类平均，AP50/AP75区分、最多100检测、box/mask仅IoU不同；不把本地全点插值例称标准COCO。
- 书稿：11.6 ImageNet/COCO/ADE20K：三大benchmark，基线L516；[4] COCO，Detection Evaluation。https://cocodataset.org/dataset/detection-eval.htm

## S1011-60｜已核相关段落
- 引用URL：https://raw.githubusercontent.com/cocodataset/cocodataset.github.io/master/dataset/keypoints-eval.htm
- 实际核读：https://raw.githubusercontent.com/cocodataset/cocodataset.github.io/master/dataset/keypoints-eval.htm
- 位置与主张：§1.1—1.2：关键点评价以OKS作对象相似度、构成AP/AR；与box IoU不能混用。
- 书稿：11.6 ImageNet/COCO/ADE20K：三大benchmark，基线L518；[5] COCO官方Keypoint Evaluation与Caption Evaluation。https://raw.githubusercontent.com/cocodataset/cocodataset.github.io/master/dataset/keypoints-eval.htm ；https://raw.githubusercontent.com/cocodataset/cocodataset.github.io/master/dataset/captions-eval.htm

## S1011-61｜已核相关段落
- 引用URL：https://raw.githubusercontent.com/cocodataset/cocodataset.github.io/master/dataset/captions-eval.htm
- 实际核读：https://raw.githubusercontent.com/cocodataset/cocodataset.github.io/master/dataset/captions-eval.htm
- 位置与主张：§1 Caption Evaluation：BLEU、METEOR、ROUGE-L、CIDEr等描述指标，不是检测AP；逐图与全数据结果分开。
- 书稿：11.6 ImageNet/COCO/ADE20K：三大benchmark，基线L518；[5] COCO官方Keypoint Evaluation与Caption Evaluation。https://raw.githubusercontent.com/cocodataset/cocodataset.github.io/master/dataset/keypoints-eval.htm ；https://raw.githubusercontent.com/cocodataset/cocodataset.github.io/master/dataset/captions-eval.htm

## S1011-62｜已核相关段落
- 引用URL：https://github.com/CSAILVision/sceneparsing
- 实际核读：https://raw.githubusercontent.com/CSAILVision/sceneparsing/master/README.md
- 位置与主张：官方README Data与Evaluation routines：20210/2000训练验证、150类、原标签0忽略、最终分数为pixel accuracy与mIoU均值。
- 书稿：11.6 ImageNet/COCO/ADE20K：三大benchmark，基线L520；[6] MIT官方Scene Parsing开发包，Overview、Data及Evaluation routines。https://github.com/CSAILVision/sceneparsing ；完整数据集入口 https://ade20k.csail.mit.edu/

## S1011-63｜已核相关段落
- 引用URL：https://ade20k.csail.mit.edu/
- 实际核读：https://ade20k.csail.mit.edu/
- 位置与主张：Full Dataset与Scene Parsing Benchmark入口明确分开，完整集首页列25574训练与2000验证；正文20210/2000专指Scene150开发包，未将两版混同。
- 书稿：11.6 ImageNet/COCO/ADE20K：三大benchmark，基线L520；[6] MIT官方Scene Parsing开发包，Overview、Data及Evaluation routines。https://github.com/CSAILVision/sceneparsing ；完整数据集入口 https://ade20k.csail.mit.edu/

## S1011-64｜已核相关段落
- 引用URL：https://raw.githubusercontent.com/cocodataset/cocodataset.github.io/master/dataset/termsofuse.htm
- 实际核读：https://raw.githubusercontent.com/cocodataset/cocodataset.github.io/master/dataset/termsofuse.htm
- 位置与主张：Annotations & Website为CC BY4.0；Images明确COCO不拥有版权、图片须按原条款；支持正文分开数据标注/图片权利而非代授许可。
- 书稿：11.6 ImageNet/COCO/ADE20K：三大benchmark，基线L522；[7] COCO官方Terms of Use。https://raw.githubusercontent.com/cocodataset/cocodataset.github.io/master/dataset/termsofuse.htm

## S1011-65｜已核相关段落
- 引用URL：https://scikit-learn.org/stable/modules/generated/sklearn.metrics.top_k_accuracy_score.html
- 实际核读：https://scikit-learn.org/stable/modules/generated/sklearn.metrics.top_k_accuracy_score.html
- 位置与主张：函数定义Top-k及Notes：真实类落前k即正确；并列分数优先较大索引。正文小编号优先明确为自定义，未假托库默认。
- 书稿：11.7 Top-1/mAP/mIoU指标族，基线L608；[1] scikit-learn，top_k_accuracy_score，定义及Notes并列规则。https://scikit-learn.org/stable/modules/generated/sklearn.metrics.top_k_accuracy_score.html

## S1011-66｜已核相关段落
- 引用URL：https://lightning.ai/docs/torchmetrics/stable/segmentation/mean_iou.html
- 实际核读：https://lightning.ai/docs/torchmetrics/stable/segmentation/mean_iou.html
- 位置与主张：Module Interface定义IoU、include_background默认true；双方都缺席返回-1。支持空类处理有实现约定差异，不要求本地空值与库相同。
- 书稿：11.7 Top-1/mAP/mIoU指标族，基线L612；[3] TorchMetrics，Mean Intersection over Union，include_background及双方均缺席类别的返回说明。https://lightning.ai/docs/torchmetrics/stable/segmentation/mean_iou.html

## S1011-67｜已核相关段落
- 引用URL：https://arxiv.org/abs/1901.05555
- 实际核读：https://arxiv.org/abs/1901.05555
- 位置与主张：作者原摘要：少数类占多数数据/多数类欠代表的长尾定义，重采样/重加权路线；不声称本章三类构成幂律。
- 书稿：11.8 长尾分布与类别不平衡评测，基线L699；[1] Cui等，Class-Balanced Loss Based on Effective Number of Samples，2019，摘要中的长尾定义与重采样、重加权路线。https://arxiv.org/abs/1901.05555

## S1011-68｜已核相关段落
- 引用URL：https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_fscore_support.html
- 实际核读：https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_fscore_support.html
- 位置与主张：定义、binary及zero_division/Notes：TP/(TP+FP)、TP/(TP+FN)和无正预测时精确率未定义相符。 边界：核定义及零分母说明，不代表已执行软件。
- 书稿：11.8 长尾分布与类别不平衡评测，基线L701；[2] scikit-learn官方precision_recall_fscore_support文档，指标定义、average、support及zero_division。https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_fscore_support.html

## S1011-69｜已核相关段落
- 引用URL：https://scikit-learn.org/stable/modules/generated/sklearn.metrics.balanced_accuracy_score.html
- 实际核读：https://scikit-learn.org/stable/modules/generated/sklearn.metrics.balanced_accuracy_score.html
- 位置与主张：定义为逐类召回均值；adjusted=False默认0—1，True为机会校正。与正文采用未调整概念相符。
- 书稿：11.8 长尾分布与类别不平衡评测，基线L703；[3] scikit-learn官方balanced_accuracy_score文档，定义及adjusted参数。本节采用adjusted=False的概念，不调用该库。https://scikit-learn.org/stable/modules/generated/sklearn.metrics.balanced_accuracy_score.html

## S1011-70｜已核相关段落
- 引用URL：https://imbalanced-learn.org/stable/common_pitfalls.html
- 实际核读：https://imbalanced-learn.org/stable/common_pitfalls.html
- 位置与主张：§9.1：分割前全数据重采样造成泄漏并改变测试类分布；正确流程以pipeline在训练折中采样。
- 书稿：11.8 长尾分布与类别不平衡评测，基线L705；[4] imbalanced-learn官方Common pitfalls，9.1 Data leakage。https://imbalanced-learn.org/stable/common_pitfalls.html

## S1011-71｜已核相关段落
- 引用URL：https://arxiv.org/html/1903.12261v1
- 实际核读：https://arxiv.org/html/1903.12261v1
- 位置与主张：§4.1图1与§4.2：15腐蚀类型×5强度，CE用对应AlexNet五级错误和归一化、mCE再平均15类；不是普通正确率下降。
- 书稿：11.9 分布偏移与鲁棒性评测，基线L783；[1] Hendrycks与Dietterich，Benchmarking Neural Network Robustness to Common Corruptions and Perturbations，2019，§4.1–4.2。https://arxiv.org/html/1903.12261v1

## S1011-72｜已核相关段落
- 引用URL：https://arxiv.org/html/1610.02136v3
- 实际核读：https://arxiv.org/html/1610.02136v3
- 位置与主张：§1—3：误分与类外检测是相关但不同问题，最高softmax分数可作基线；单个高分不等于可靠信心，§3.1表1—2显示高分错误/类外。
- 书稿：11.9 分布偏移与鲁棒性评测，基线L785；[2] Hendrycks与Gimpel，A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks，ICLR 2017，2018修订版，§1–3。https://arxiv.org/html/1610.02136v3

## S1011-73｜已核相关段落
- 引用URL：https://arxiv.org/html/2007.01434v1
- 实际核读：https://arxiv.org/html/2007.01434v1
- 位置与主张：§3及§3.1三选择方法：调参策略必须说明、oracle测试域访问受限且不可和无oracle直接比；§4初版9算法7数据3方法、§5.1同条件ERM比较。正文仅借划分与公平比较原则。
- 书稿：11.9 分布偏移与鲁棒性评测，基线L787；[3] Gulrajani与Lopez-Paz，In Search of Lost Domain Generalization，2020，§3–5。https://arxiv.org/html/2007.01434v1

## S1011-74｜已核相关段落
- 引用URL：https://www.jmlr.org/papers/v11/cawley10a.html
- 实际核读：https://www.jmlr.org/papers/v11/cawley10a.html
- 位置与主张：期刊原文摘要：有限样本模型选择指标的方差可导致选择过拟合，随后性能评价有选择偏差；直接支持开发阶段反复选取适应偶然差异。
- 书稿：11.10 消融协议与控制变量，基线L872；[1] Cawley与Talbot，2010，On Over-fitting in Model Selection and Subsequent Selection Bias in Performance Evaluation，JMLR。https://www.jmlr.org/papers/v11/cawley10a.html

## S1011-75｜已核相关段落
- 引用URL：https://jmlr.org/papers/v13/bergstra12a.html
- 实际核读：https://jmlr.org/papers/v13/bergstra12a.html
- 位置与主张：期刊原文摘要：同搜索域与计算预算比较随机/网格搜索，所找到方案随预算/重要参数覆盖改变；支持说明搜索预算，不推出次数相同=耗时相同。
- 书稿：11.10 消融协议与控制变量，基线L874；[2] Bergstra与Bengio，2012，Random Search for Hyper-Parameter Optimization，JMLR。https://jmlr.org/papers/v13/bergstra12a.html

## S1011-76｜已核相关段落
- 引用URL：https://www.itl.nist.gov/div898/handbook/pri/section3/pri333.htm
- 实际核读：https://www.itl.nist.gov/div898/handbook/pri/section3/pri333.htm
- 位置与主张：Full factorial designs定义：每因素每取值与其余因素所有取值组合，k个二水平因素需2^k次；两因素四格是全因子结构而非自然史因果证明。
- 书稿：11.10 消融协议与控制变量，基线L876；[3] NIST/SEMATECH，e-Handbook of Statistical Methods，5.3.3.3 Full factorial designs。https://www.itl.nist.gov/div898/handbook/pri/section3/pri333.htm


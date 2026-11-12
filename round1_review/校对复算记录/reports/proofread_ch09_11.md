# 第9—11章独立校对报告

## 结论

28节全部逐节通读；确定性修订15项（第9章3项，第10章7项，第11章5项），仅写入revision。来源共108个不同URL，均核到相关原文；无未核项。基线未改，附件未由校对员执行。

重点是旧案例与当前新练习的对象边界、9.7否定已保留但答案分类错误、失效操作参数及文件名。11.10新四图的零差异不构成旧十二图结果的反证；两例分开说明。

---

## 分组原始报告：proofread_ch09.md

# 第9章独立校对报告

## 主要结果

8节全文及全部注释逐节通读完成，最后一条[3]在底本第737行（文件无末尾换行），未漏读。修订副本改3处；底本未动，附件未执行。

最重要发现是9.7新版P1英文保留未实施信息，错误在预置答案，不应归因为译文漏否定。另消除9.2把当前CSV误指为旧四句校史数据的操作指示，以及9.3新六句/旧八句的衔接歧义。

## 已修问题

| ID | 节与底本行 | 原文与修正理由 |
|---|---|---|
| PR09-01 | 9.2，L115 | 原文：先打开配套的CSV…编号S01至S04。改为先看旧例记录，明确当前N01—N03迁埠句不是旧CSV。 理由：当前配套仅三条新句，按原指令找不到四条校史记录，不能将新输入冒充旧例。 |
| PR09-02 | 9.3，L281 | 原文：先在已有六句上建立字面基线。先交代新版改用六句书院停讲材料，不沿用上文八条校史开发句。 理由：样本量及任务突然切换，已有的指代不准确。 |
| PR09-03 | 9.7，L634 | 原文：这两对…pred列也是预置计数…应定位英语是否丢了未实施信息。明确新两对独立例，pred为预置答案；P1英文已含not carried out，错误在答案判为已迁，非译文漏否定。 理由：直接只读输入可证英文保留否定，原诊断把分类错误与翻译错误混淆。 |

## 逐节阅读与数据解释证据

| 节 | 底本行范围 | 阅读证据 |
|---|---|---|
| 9.1 | L7—104 | 四句校史整理同时包含三件沿革与一项网页发布；2022不是沿革发生年。；改制/升格字面检索、固定模板摘要和年份比较均与模型推理分开，唯一原因断言属材料不足。 |
| 9.2 | L105—205 | S02八字校名[17,25)，窗口[14:26]换算[3,11]+14成立；位置对应整理句而非网页原件。；17+26+26+28=97有效字符，4×28=112含15补齐；20长的77/3及截断目标分母解释一致。；当前CSV实际为N01—N03三迁埠句，不是旧S01—S04，已修错误打开指示。 |
| 9.3 | L206—300 | 旧例四条参考/八条开发，规则6对2待核、TF-IDF7对1待核；D02全零不能取第一个最大值。；D08词项冲突与整体字面近邻不同；129维是旧例权重，当前六句停讲练习仅词项基线，已明示切换。 |
| 9.4 | L301—390 | CBOW、Skip-gram、BERT及GPT目标分别解释；输入嵌入不等于语境隐状态。；五句六维手设特征C01/C05同向量却相反事件状态，.816497、0、.5对应给定向量；新三维“港”练习另案。 |
| 9.5 | L391—476 | GLUE9、SuperGLUE8、MMLU57和HumanEval164的任务范围与通用能力不混同。；A类别6/6、引用字面5/6、联合4/6；B类别5/6、字面6/6、联合5/6，预置答案不是模型排名。 |
| 9.6 | L477—562 | 九记录中D9未决，八对六同判为75%；Pe=22/64、κ=13/21约.619048。；D3共同把提议当完成仍然错误；证据边界6/8与标签κ不同，协商后2/2/4及未决单列。 |
| 9.7 | L563—645 | 旧六对中文5/6、英文3/6、同答4/6、双侧正确3/6；Q03共同错误不成双侧正确。；当前新两对P1英文保留not carried out，但pred为已迁；已把诊断从翻译丢否定改为答案误判。 |
| 9.8 | L646—737 | 十六目录、十四可读、十二可评分；两组各缺一正文一参考，null不当中立或错。；A/B总体9/12相同而等权组平均50%/75%；配对版本非独立事件，代表性与准确率不能互相保证。；从覆盖缺口转向历史叙述位置有具体论证，不把语言组等同历史人群；最后[3]在无末尾换行第737行。 |

## 来源段落核对

以下33项是具体引用段检查，不是33部作品全文审核；没有执行来源中的模型代码。台师大网页只作为机构后编校史记述的直接来源，不等同1946/1955/1967原始行政文书。

| ID | 原文 | 本轮读核位置与结果 |
|---|---|---|
| S09-01 | [原文](https://pr.ntnu.edu.tw/news/index.php?id=21193&mode=data) | 页首2022-11-18、正文第二段及末尾署源：1946成立、1955改制、1967升格及图书馆校史特藏组来源相符。 |
| S09-02 | [原文](https://huggingface.co/tasks/text-classification) | 开头任务定义：分类为给文本赋类别；未采用网页后文NLI过简化说明。 |
| S09-03 | [原文](https://www.sbert.net/examples/sentence_transformer/applications/semantic-search/README.html) | 开头及Background：字面匹配与向量语义检索分开，句向量近邻是方法而非真实性保证。 |
| S09-04 | [原文](https://huggingface.co/tasks/summarization) | 开头任务定义：摘要压缩重要信息，抽取与生成表达有别。 |
| S09-05 | [原文](https://aclanthology.org/D15-1075.pdf) | 刊页632—634，第1节、表1及2.1：SNLI三类、前提与假设有原文依据；未把中立标签等同历史虚假。 |
| S09-06 | [原文](https://jsonlines.org/) | 三项格式要求：UTF-8、每行有效JSON值、换行规则相合。 |
| S09-07 | [原文](https://numpy.org/doc/2.3/reference/generated/numpy.asarray.html) | 定义、a与dtype参数：输入转数组、数据类型说明相符。 |
| S09-08 | [原文](https://numpy.org/doc/2.3/reference/generated/numpy.ndarray.shape.html) | shape定义：形状为各轴维度元组。 |
| S09-09 | [原文](https://huggingface.co/docs/transformers/v4.57.1/main_classes/tokenizer) | 开头Fast映射说明及return_offsets_mapping参数：快速分词器的字符起止映射有据；未测试任何模型接口。 |
| S09-10 | [原文](https://huggingface.co/docs/transformers/main/pad_truncation) | 开头及padding/max_length参数：补齐与截断区分正确。 |
| S09-11 | [原文](https://huggingface.co/docs/transformers/main_classes/output) | BaseModelOutput.last_hidden_state及SequenceClassifierOutput.logits：隐状态三轴与分类分数两轴相符，logits未误称概率。 |
| S09-12 | [原文](https://github.com/huggingface/transformers/blob/main/docs/source/en/tasks/token_classification.md) | 标签对齐三步及代码说明：-100为所引损失函数忽略标签的约定，和本例位置占位分开。 |
| S09-13 | [原文](https://scikit-learn.org/1.8/modules/generated/sklearn.feature_extraction.text.TfidfTransformer.html) | TF-IDF定义、smooth_idf与norm：词频及逆文档频率解释相符。 |
| S09-14 | [原文](https://scikit-learn.org/1.8/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html) | analyzer、ngram_range、fit_transform及transform：字符n元组和先拟合后转换的区别相符。 |
| S09-15 | [原文](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html) | 定义、公式、返回形状：归一化点积及两批向量的比较矩阵相符。 |
| S09-16 | [原文](https://sbert.net/docs/sentence_transformer/usage/semantic_textual_similarity.html) | 开头、encode/similarity示例及默认指标：先编码再比较相似度有据，没有把候选模型视为已跑。 |
| S09-17 | [原文](https://arxiv.org/abs/2005.14165) | 作者原摘要：以文本说明/示例、无任务内梯度更新的设置得到支持。 |
| S09-18 | [原文](https://arxiv.org/pdf/1301.3781) | 3.1—3.2：CBOW以语境预测中心词、Skip-gram以中心词预测附近词相符。 |
| S09-19 | [原文](https://aclanthology.org/N19-1423.pdf) | 摘要、第3节输入表示、3.1遮蔽语言模型：输入嵌入与上下文化隐状态、双向条件及训练遮蔽区别相符。 |
| S09-20 | [原文](https://aclanthology.org/D19-1410/) | 作者摘要：SBERT以句表示支持余弦相似比较的目标相符。 |
| S09-21 | [原文](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf) | 3.1公式1及架构说明：按此前单元预测当前单元的目标相符。 |
| S09-22 | [原文](https://arxiv.org/pdf/1804.07461) | 摘要、3节开头、3.4：九项英文任务和分任务指标汇总相符。 |
| S09-23 | [原文](https://arxiv.org/pdf/1905.00537) | 第1节及3.2开头：八项英语理解任务及多类任务形式相符。 |
| S09-24 | [原文](https://arxiv.org/pdf/2009.03300) | 摘要、第3节与选择题示例：57学科/任务和选择题评价相符。 |
| S09-25 | [原文](https://arxiv.org/pdf/2107.03374) | 2.1—2.2及3.3相关说明：HumanEval164手写题；pass@k至少一份通过测试，不是第一份答案必正确。 |
| S09-26 | [原文](https://github.com/openai/human-eval) | Usage首段：生成代码属于不可信代码，需隔离的提示与书中相合。 |
| S09-27 | [原文](https://aclanthology.org/J08-4004.pdf) | 2.1、2.3、2.4.3及4.3.2相应段：一致不能保证有效；κ逐标注者边际；单位识别另需评价。 |
| S09-28 | [原文](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.cohen_kappa_score.html) | 定义、公式及weights：κ公式、逐标注者分布和None不加权相符。 |
| S09-29 | [原文](https://aclanthology.org/D18-1269.pdf) | 1、3.2及4.1—4.2：源语言训练/目标语言测试、译文标签核查及翻译/直接编码路线相符。 |
| S09-30 | [原文](https://aclanthology.org/2020.emnlp-main.618.pdf) | 摘要与第1节：翻译可改变词语重叠等表面特征，原生/翻译材料区别有据。 |
| S09-31 | [原文](https://aclanthology.org/2020.acl-main.485.pdf) | 第4节三项建议：偏见分析应交代何种行为造成何种伤害、影响谁及理由；不由数值差异直接下歧视判断。 |
| S09-32 | [原文](https://arxiv.org/pdf/1810.03993) | 4.3相关因素及4.7：按相关因素与交叉因素分解评价相符。 |
| S09-33 | [原文](https://aclanthology.org/2020.acl-main.442.pdf) | 2.1与2.2：按任务能力设计最小功能、不变性与方向性测试；本书对照句借鉴合理。 |

## 保留事项

- 旧例和本版小型练习已在章首注明独立。本次修正具体错指和诊断错位，没有擅自抹去旧运行叙述；旧程序与原字节恢复仍需复算/来源负责人交代。
- 新版附件README已出现本轮标准库实跑说明，但正文章首和八节末NOT_RUN/“本次不执行复算”仍待root按真实覆盖统一同步。模型未运行与标准库已运行必须分开。
- 八节开头与末尾模板重复较多。可由总编合并统一状态说明，具体案例切换处则仍须保留数量、编号、任务变化。没有为减少防御性文字而删掉史料层级和译文局限等必要限定。
- 9.8对材料代表性、语言组不等于人群和有限阅读时间的论证是作者有依据的研究取向，未把观点当事实，也未因不能普遍证明而删除。
- 本章本地相对链接17处均存在，存在性不等于运行通过；未做整书10/75/15量化判定。

详细覆盖见 `coverage_ch09.json`，修改见 `proofread_ch09.diff`。


---

## 分组原始报告：proofread_ch10_11.md

# 第10—11章独立校对报告

## 实质结果

- 20节全部逐节通读（第10章10节、第11章10节）；非原作者；正文修改12处（10章7处、11章5处）。
- 主要问题是旧案例与新版附件混读、已失效的入口/命令、官方代码文件名被机械加前缀，以及11.10新旧样本分母混淆。均只改授权副本，未改或运行附件。
- 11.10新版为四图两类、2训练+2开发；复算员报告四格指标全1，不能套用旧三类12开发图结果。本报告不声称本人实跑。
- 来源：第10章28项、第11章48项URL全部核到相关原文段落；跨章去重共76项，未核0。台账见 `sources_ch10_11.json/md`；ImageNet两项明确标注直连超时、核读原站/同文索引的方式。

## 逐项修正（行号指基线）

### PR1011-01｜10.引言｜L5｜P1
- 原文：正文只保留章—节这一层目录，节内小标题帮助按步骤阅读。
- 修订：旧案例中所称的配套、读者包及结果文件不随本版交付；本版可取得的文件以各节末尾链接为准，不能用新输入复现旧记录。正文只保留章—节这一层目录，节内小标题帮助按步骤阅读。
- 理由：现有入口只区分执行时间，没有说明旧附件不随新包交付；用一处交付边界解释全章遗留称谓，不逐段添加重复提示。

### PR1011-02｜11.引言｜L5｜P1
- 原文：正文只保留章—节这一层目录，节内小标题帮助按步骤阅读。
- 修订：旧案例中所称的配套、读者包及结果文件不随本版交付；本版可取得的文件以各节末尾链接为准，不能用新输入复现旧记录。正文只保留章—节这一层目录，节内小标题帮助按步骤阅读。
- 理由：现有入口只区分执行时间，没有说明旧附件不随新包交付；用一处交付边界解释全章遗留称谓，不逐段添加重复提示。

### PR1011-03｜10.1｜L69｜P2
- 原文：本例是当前环境的一次生成示范
- 修订：本例是原稿编写环境中的一次生成示范
- 理由：“当前环境”会将继承的旧调用记录误指本次独立校对。

### PR1011-04｜10.5｜L487｜P1
- 原文：执行`--reference`汇总教学整理参考：
- 修订：旧稿的教学整理参考汇总如下：
- 理由：本版workbook.py仅接受--input，没有--reference；保留旧表计数但撤销失效命令。

### PR1011-05｜10.6｜L570｜P2
- 原文：只改简繁表达
- 修订：只改表达长短
- 理由：此处检验篇幅偏好，不是简繁字转换；改用不歧义的普通本科书面语。

### PR1011-06｜10.6｜L596｜P1
- 原文：从“旧例中的README.md”进入。输入与真实输出原样保存；`复用10.5/`中的三件附件为前节原字节复用，合订时不另计新语料或新成果。
- 修订：上文八份候选的AB／BA评分属于旧稿记录；本版练习另见[10.6操作说明](../../附件/ch10/10.6/README.md)，采用预置的成对候选判断，不调用评判模型。两例不合并计算样本数。
- 理由：实际目录无“旧例中的README.md”及复用10.5/；新版是另设的成对比较，不能保证旧输入输出原字节交付。

### PR1011-07｜10.7｜L700｜P2
- 原文：核读位置与方法适用边界见配套《公开来源与定位》。
- 修订：[1]给出Wilson比例区间；[2]说明成对重采样及百分位区间等方法；[3]讨论组内相关与聚类推断。本文的六组穷举例不等于这些文献对任意小样本区间覆盖率的保证。
- 理由：当前附件无《公开来源与定位》，改为本节已有公开引用的作用定位；保持方法适用边界。

### PR1011-08｜10.9｜L824｜P2
- 原文：材料编号和句号位置定位
- 修订：材料编号和句子序号定位
- 理由：D2第1句/第2句是句子编号，不是标点句号的位置。

### PR1011-09｜11.5｜L422｜P2
- 原文：Meta官方“旧例中的vision_transformer.py”，`forward_features`；“旧例中的hub/backbones.py”；“旧例中的data/transforms.py”
- 修订：Meta官方`vision_transformer.py`，`forward_features`；`hub/backbones.py`；`data/transforms.py`
- 理由：旧例替换前缀误入官方文件名；保留原有链接和接口定位。

### PR1011-10｜11.8｜L687｜P2
- 原文：原稿提出运行后，请先从输入数出频数，再独立复算B的地图精确率和宏F1，最后解释为什么来源甲的印章召回率不是零。
- 修订：阅读旧稿结果时，可先从本节矩阵数出频数，再独立复算B的地图精确率和宏F1，最后解释为什么来源甲的印章召回率不是零。
- 理由：原句语病且指向未交付旧输入；矩阵已在正文完整展示，足以进行所述手工核对。

### PR1011-11｜11.10｜L823｜P2
- 原文：下表由旧稿记录的教学演算，
- 修订：下表列出旧稿记录的教学演算结果，
- 理由：补足谓语，明确是继承旧记录而非本轮实跑。

### PR1011-12｜11.10｜L864｜P1
- 原文：固定四张教学像素图与两类定义，把是否使用填充率和接受阈值组成四格。每一格重新按自己的特征集合建立训练质心，不能把完整方案分数删一列冒充消融。候选比较只在dev图上进行，结果栏保持NOT_RUN直到实际执行。随后为真正独立的图录页写测试条件，不把这四张合成图重新随机分半当作外部测试。
- 修订：本版另用四张教学像素图、两类定义，其中两张用于训练，两张用于开发；不是上文三类、十二张开发图的旧例。把是否使用填充率和接受阈值组成四格，每一格按自己的特征集合建立训练质心，不能把完整方案分数删一列冒充消融。候选比较只在两张dev图上进行，实际执行状态与逐格结果见本版操作说明。比较没有出现差异时，也应保留这一结果，不能据此证明某项特征或门槛在其他材料上无用。随后为真正独立的图录页写测试条件，不把这四张合成图重新随机分半当作外部测试。
- 理由：只读input.json确认2train+2dev，避免四张都当开发分母；不把复算员报告的新版四格全1套成旧12图值，也不冒称本人运行。

## 全量阅读证据

### 10.1 Prompt模板设计（L7—117；READ_COMPLETE）
- 四条仿作渡口记录分已实施、拟增、撤销、轮值不足；四次输出不是历史史实材料。
- 旧稿4/4结构与引文通过，不提供可归属到本次环境的模型权重版本。
### 10.2 Few-shot示例选择与k-shot评测协议（L118—214；READ_COMPLETE）
- k按每次请求提供的完整示范对总数计；旧例8个示范及8条开发题，四条件均8/8。
- 输入字符891/1601/1619/2329；本版k=0/2另例不能冒充旧模型调用。
### 10.3 Prompt敏感度分析（L215—314；READ_COMPLETE）
- B/W/O六次调用均8/8、输入字符1601/1596/1601；零差异未被改写为无效。
- D04/D05各错一条而同为7/8的说明是假设例，用于区分总分相同与逐题一致。
### 10.4 n-gram评测：BLEU与ROUGE（L315—418；READ_COMPLETE）
- 仿作未改已的事实错误仍有高BLEU；字符归一化与空白分词的新练习分开。
- 手算p1=1、p2=.75、BP=exp(-.2)，BLEU2=.709042；两个字符的BLEU4为空是局部契约。
### 10.5 人工评估金标准与质量控制（L419—514；READ_COMPLETE）
- 八候选的支持/冲突/未支持/待定为5/1/1/1，确定项一致6/7，覆盖12/14。
- T06因果缺证据；T07原字缺损仍待定；旧--reference命令未在新版入口实现。
### 10.6 LLM-as-Judge协议（L515—599；READ_COMPLETE）
- 八候选AB/BA翻转对照与新版预置成对判断不同，不能合并样本数。
- 七项确定标签一致；16处引用、评分不变但八理由改写，不据此建立普遍模型不偏结论。
### 10.7 Bootstrap置信区间（L600—703；READ_COMPLETE）
- 16/20 Wilson约58.4%—91.9%，20/20下界约83.9%；全1重采样可能退化。
- 六来源差值1,.5,.5,0,0,-.5，平均.25；旧6^6枚举46656与新版三来源六行不同。
### 10.8 McNemar检验（L704—793；READ_COMPLETE）
- 30条仿作配对a16/b2/c10/d2，精确双侧p=2*(1+12+66)/4096=.03857421875。
- m=0返回1为实现约定；0/4=.125与0/6=.03125；不得将10.7相关片段当独立对。
### 10.9 幻觉的评测与缓解（L794—878；READ_COMPLETE）
- 修屋、次年货增及因果为三项声明，前两项支持不推出第三项。
- 前后支持3/6与6/6；固定八个必要事实的遗漏5/8→2/8；拒答不当作满分事实支持。
### 10.10 Model Card与Datasheet for Datasets（L879—951；READ_COMPLETE）
- 旧30条预设判断，A18/30、B26/30与McNemar .03857不是新模型实测优越性。
- 数据卡与应用卡分开；M17/18只B错，M29/30都错；新版六行不同于旧30行。
### 11.1 分类：从图片到类别概率向量（L7—96；READ_COMPLETE）
- 旧17图=9训练+6测试+2探针，fill/aspect与exp(-d/.02)不是校准概率。
- 旧5/6正确，遮挡方块误三角且.8303；类外菱形.9421仍被接受；新版四图8×8另例。
### 11.2 检测：bbox回归与分类的联合任务（L97—182；READ_COMPLETE）
- 旧四图六对象：TP3 FP1 FN3，P=.75 R=.5；提高IoU=.75得TP2 FP2 FN4。
- 新版一页一参考、三预测中重复框与错类分别受罚；半开边框12×12，与COCO多阈值AP区分。
### 11.3 分割：像素级分类与SAM提示分割（L183—262；READ_COMPLETE）
- 旧16像素目标、三个预测12/8/32像素，对应IoU .75/.5/.5，Dice6/7与2/3。
- 负点删除整连通块是教学算法，不是SAM通用行为；新版4×4预置掩码不称运行SAM。
### 11.4 从CNN到ViT：架构与迁移路线（L263—347；READ_COMPLETE）
- 两层3×3局部感受野5×5；旧8×8块16×64只是分块表，不是学习到的token。
- 224/P16得N196与L197，448得N784与L785；注意力矩阵约15.88倍不是总显存；600照片分配是假设。
### 11.5 DINOv2与特征质量评估（L348—427；READ_COMPLETE）
- DINOv2 ViT-S/14 CLS384，224输入256个patch；x_norm不自动等于单位L2长度。
- 同源泄漏假向量8/8、排除来源0/8；旧PGM像素试验不同于新版手设向量；官方文件名误插旧例前缀已修。
### 11.6 ImageNet/COCO/ADE20K：三大benchmark（L428—527；READ_COMPLETE）
- ImageNet2012千类，COCO2017约118k/5k及80类，Scene150的20210/2000与忽略0按各自单位说明。
- 旧八条映射审计四条测试中三可映射一阻塞，不是图像准确率；许可证与图片权利不能混同。
### 11.7 Top-1/mAP/mIoU指标族（L528—615；READ_COMPLETE）
- 四图六类Top1=2/4、Top5=3/4，升序ID并列规则是局部自定。
- 教学两类AP5/6与1/2、mAP2/3不是COCO101点；像素全背景准确率.9但mIoU.3、前景IoU0。
### 11.8 长尾分布与类别不平衡评测（L616—710；READ_COMPLETE）
- 训练180/12/8、开发45/3/2、测试90/6/4；全猜多数类准确率.90却macroF1约.3158。
- B准确率.86、macroF1约.6631；来源甲无印章真实样本时召回不可定义而非零，仍可有四个假阳性。
### 11.9 分布偏移与鲁棒性评测（L711—790；READ_COMPLETE）
- 旧6原图、6亮度图、6噪声图不是18个独立单位；亮度仍过阈值，噪声扩边框改变填充率。
- 5/6→2/6是降50个百分点；新版R4预测正确但被拒绝，不误记为错误或已处理。
### 11.10 消融协议与控制变量（L791—878；READ_COMPLETE）
- 旧9训练/12开发三类四格；U分别0、-1/12、8/12、7/12，按预定效用选fill+.60而非最高接受内准确率。
- 本版四图=2训练+2开发、两类；复算员报告四格指标全1，本人只读输入与README，未运行；保留零差异。

## 保留及未决事项

- PR1011-U01：旧例附件未随本版交付：保留为旧记录，不可由新版不同输入独立复现。章首及具体失效入口已界定。
- PR1011-U02：新版附件状态已由复算员更新；各节正文模板中NOT_RUN／实际运行后等表述需全书统一决定是保留空白教学表还是据实更新，不由本校对员冒充实跑。
- PR1011-U03：章内重复的旧例/教学/不可推广边界较密，但含不同实质用途；未大删价值与方法观点。

## 权限、核验与交付边界

- 未新增史学事实；保留作者评价立场，仿作、模型方法、历史材料分别说明。
- 数学核对限正文公式、分母、百分点与语义；旧数表保留其旧记录身份，独立复算由复算员完成。
- 附件目录、README和少量入口文件仅只读核对；未安装、未外发、未删除；baseline不变。
- 变更精确见 `proofread_ch10_11.diff`；逐节机器可读证据见 `coverage_ch10_11.json`。

## 来源终核补记

- 逐项核对后未发现新增必须更改正文的来源—主张错配；摘要级主张只计已核摘要，不冒称读全论文。
- 作者假设、教学约定、具体旧数值未因来源存在而升级为真实运行或史学事实。


---

## 全部引用URL台账

同一URL如有不同引用主张，逐项保留检查；直连或索引获取的限界见JSON。

### S0911-001 · 已核相关段落
- URL：https://pr.ntnu.edu.tw/news/index.php?id=21193&mode=data
- 位置：页首2022-11-18、正文第二段及末尾署源；判断：1946成立、1955改制、1967升格及图书馆校史特藏组来源相符。（记录：sources_ch09.json / S09-01）。

### S0911-002 · 已核相关段落
- URL：https://huggingface.co/tasks/text-classification
- 位置：开头任务定义；判断：分类为给文本赋类别；未采用网页后文NLI过简化说明。（记录：sources_ch09.json / S09-02）。

### S0911-003 · 已核相关段落
- URL：https://www.sbert.net/examples/sentence_transformer/applications/semantic-search/README.html
- 位置：开头及Background；判断：字面匹配与向量语义检索分开，句向量近邻是方法而非真实性保证。（记录：sources_ch09.json / S09-03）。

### S0911-004 · 已核相关段落
- URL：https://huggingface.co/tasks/summarization
- 位置：开头任务定义；判断：摘要压缩重要信息，抽取与生成表达有别。（记录：sources_ch09.json / S09-04）。

### S0911-005 · 已核相关段落
- URL：https://aclanthology.org/D15-1075.pdf
- 位置：刊页632—634，第1节、表1及2.1；判断：SNLI三类、前提与假设有原文依据；未把中立标签等同历史虚假。（记录：sources_ch09.json / S09-05）。

### S0911-006 · 已核相关段落
- URL：https://jsonlines.org/
- 位置：三项格式要求；判断：UTF-8、每行有效JSON值、换行规则相合。（记录：sources_ch09.json / S09-06）。

### S0911-007 · 已核相关段落
- URL：https://numpy.org/doc/2.3/reference/generated/numpy.asarray.html
- 位置：定义、a与dtype参数；判断：输入转数组、数据类型说明相符。（记录：sources_ch09.json / S09-07）。

### S0911-008 · 已核相关段落
- URL：https://numpy.org/doc/2.3/reference/generated/numpy.ndarray.shape.html
- 位置：shape定义；判断：形状为各轴维度元组。（记录：sources_ch09.json / S09-08）。

### S0911-009 · 已核相关段落
- URL：https://huggingface.co/docs/transformers/v4.57.1/main_classes/tokenizer
- 位置：开头Fast映射说明及return_offsets_mapping参数；判断：快速分词器的字符起止映射有据；未测试任何模型接口。（记录：sources_ch09.json / S09-09）。

### S0911-010 · 已核相关段落
- URL：https://huggingface.co/docs/transformers/main/pad_truncation
- 位置：开头及padding/max_length参数；判断：补齐与截断区分正确。（记录：sources_ch09.json / S09-10）。

### S0911-011 · 已核相关段落
- URL：https://huggingface.co/docs/transformers/main_classes/output
- 位置：BaseModelOutput.last_hidden_state及SequenceClassifierOutput.logits；判断：隐状态三轴与分类分数两轴相符，logits未误称概率。（记录：sources_ch09.json / S09-11）。

### S0911-012 · 已核相关段落
- URL：https://github.com/huggingface/transformers/blob/main/docs/source/en/tasks/token_classification.md
- 位置：标签对齐三步及代码说明；判断：-100为所引损失函数忽略标签的约定，和本例位置占位分开。（记录：sources_ch09.json / S09-12）。

### S0911-013 · 已核相关段落
- URL：https://scikit-learn.org/1.8/modules/generated/sklearn.feature_extraction.text.TfidfTransformer.html
- 位置：TF-IDF定义、smooth_idf与norm；判断：词频及逆文档频率解释相符。（记录：sources_ch09.json / S09-13）。

### S0911-014 · 已核相关段落
- URL：https://scikit-learn.org/1.8/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html
- 位置：analyzer、ngram_range、fit_transform及transform；判断：字符n元组和先拟合后转换的区别相符。（记录：sources_ch09.json / S09-14）。

### S0911-015 · 已核相关段落
- URL：https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html
- 位置：定义、公式、返回形状；判断：归一化点积及两批向量的比较矩阵相符。（记录：sources_ch09.json / S09-15）。

### S0911-016 · 已核相关段落
- URL：https://sbert.net/docs/sentence_transformer/usage/semantic_textual_similarity.html
- 位置：开头、encode/similarity示例及默认指标；判断：先编码再比较相似度有据，没有把候选模型视为已跑。（记录：sources_ch09.json / S09-16）。

### S0911-017 · 已核相关段落
- URL：https://arxiv.org/abs/2005.14165
- 位置：作者原摘要；判断：以文本说明/示例、无任务内梯度更新的设置得到支持。（记录：sources_ch09.json / S09-17）。

### S0911-018 · 已核相关段落
- URL：https://arxiv.org/pdf/1301.3781
- 位置：3.1—3.2；判断：CBOW以语境预测中心词、Skip-gram以中心词预测附近词相符。（记录：sources_ch09.json / S09-18）。

### S0911-019 · 已核相关段落
- URL：https://aclanthology.org/N19-1423.pdf
- 位置：摘要、第3节输入表示、3.1遮蔽语言模型；判断：输入嵌入与上下文化隐状态、双向条件及训练遮蔽区别相符。（记录：sources_ch09.json / S09-19）。

### S0911-020 · 已核相关段落
- URL：https://aclanthology.org/D19-1410/
- 位置：作者摘要；判断：SBERT以句表示支持余弦相似比较的目标相符。（记录：sources_ch09.json / S09-20）。

### S0911-021 · 已核相关段落
- URL：https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf
- 位置：3.1公式1及架构说明；判断：按此前单元预测当前单元的目标相符。（记录：sources_ch09.json / S09-21）。

### S0911-022 · 已核相关段落
- URL：https://arxiv.org/pdf/1804.07461
- 位置：摘要、3节开头、3.4；判断：九项英文任务和分任务指标汇总相符。（记录：sources_ch09.json / S09-22）。

### S0911-023 · 已核相关段落
- URL：https://arxiv.org/pdf/1905.00537
- 位置：第1节及3.2开头；判断：八项英语理解任务及多类任务形式相符。（记录：sources_ch09.json / S09-23）。

### S0911-024 · 已核相关段落
- URL：https://arxiv.org/pdf/2009.03300
- 位置：摘要、第3节与选择题示例；判断：57学科/任务和选择题评价相符。（记录：sources_ch09.json / S09-24）。

### S0911-025 · 已核相关段落
- URL：https://arxiv.org/pdf/2107.03374
- 位置：2.1—2.2及3.3相关说明；判断：HumanEval164手写题；pass@k至少一份通过测试，不是第一份答案必正确。（记录：sources_ch09.json / S09-25）。

### S0911-026 · 已核相关段落
- URL：https://github.com/openai/human-eval
- 位置：Usage首段；判断：生成代码属于不可信代码，需隔离的提示与书中相合。（记录：sources_ch09.json / S09-26）。

### S0911-027 · 已核相关段落
- URL：https://aclanthology.org/J08-4004.pdf
- 位置：2.1、2.3、2.4.3及4.3.2相应段；判断：一致不能保证有效；κ逐标注者边际；单位识别另需评价。（记录：sources_ch09.json / S09-27）。

### S0911-028 · 已核相关段落
- URL：https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.cohen_kappa_score.html
- 位置：定义、公式及weights；判断：κ公式、逐标注者分布和None不加权相符。（记录：sources_ch09.json / S09-28）。

### S0911-029 · 已核相关段落
- URL：https://aclanthology.org/D18-1269.pdf
- 位置：1、3.2及4.1—4.2；判断：源语言训练/目标语言测试、译文标签核查及翻译/直接编码路线相符。（记录：sources_ch09.json / S09-29）。

### S0911-030 · 已核相关段落
- URL：https://aclanthology.org/2020.emnlp-main.618.pdf
- 位置：摘要与第1节；判断：翻译可改变词语重叠等表面特征，原生/翻译材料区别有据。（记录：sources_ch09.json / S09-30）。

### S0911-031 · 已核相关段落
- URL：https://aclanthology.org/2020.acl-main.485.pdf
- 位置：第4节三项建议；判断：偏见分析应交代何种行为造成何种伤害、影响谁及理由；不由数值差异直接下歧视判断。（记录：sources_ch09.json / S09-31）。

### S0911-032 · 已核相关段落
- URL：https://arxiv.org/pdf/1810.03993
- 位置：4.3相关因素及4.7；判断：按相关因素与交叉因素分解评价相符。（记录：sources_ch09.json / S09-32）。

### S0911-033 · 已核相关段落
- URL：https://aclanthology.org/2020.acl-main.442.pdf
- 位置：2.1与2.2；判断：按任务能力设计最小功能、不变性与方向性测试；本书对照句借鉴合理。（记录：sources_ch09.json / S09-33）。
- 位置：§2.1—2.2不变性、最小功能及方向性测试；正文只借任务相关扰动思路。本人已读引言与示例，精确§2.2同时复核父校对员本轮sources_ch09.json S09-33证据。；判断：§2.1—2.2不变性、最小功能及方向性测试；正文只借任务相关扰动思路。本人已读引言与示例，精确§2.2同时复核父校对员本轮sources_ch09.json S09-33证据。（记录：sources_ch10_11.json / S1011-06）。

### S0911-034 · 已核相关段落
- URL：https://arxiv.org/html/2107.13586v1
- 位置：§2.2、表2与§2.2.1：模板输入槽与答案槽、填入材料后的prompt、answer及answered prompt区分。；判断：§2.2、表2与§2.2.1：模板输入槽与答案槽、填入材料后的prompt、answer及answered prompt区分。（记录：sources_ch10_11.json / S1011-01）。

### S0911-035 · 已核相关段落
- URL：https://arxiv.org/pdf/2005.14165
- 位置：原论文PDF6—7页§2：K个context/completion示范，无权重更新；zero-shot无示范但可含任务指令。；判断：原论文PDF6—7页§2：K个context/completion示范，无权重更新；zero-shot无示范但可含任务指令。（记录：sources_ch10_11.json / S1011-02）。

### S0911-036 · 已核相关段落
- URL：https://proceedings.mlr.press/v139/zhao21c/zhao21c.pdf
- 位置：原论文§2及图2：format、示例集合、排列三组件；固定集合换排列的区别，与本章说明相符。；判断：原论文§2及图2：format、示例集合、排列三组件；固定集合换排列的区别，与本章说明相符。（记录：sources_ch10_11.json / S1011-03）。

### S0911-037 · 已核相关段落
- URL：https://proceedings.neurips.cc/paper/2021/file/5c04925674920eb58467fb52ce4ef728-Paper.pdf
- 位置：§1—2：额外held-out数据用于选择与true few-shot仅给定少量例的区别。；判断：§1—2：额外held-out数据用于选择与true few-shot仅给定少量例的区别。（记录：sources_ch10_11.json / S1011-04）。

### S0911-038 · 已核相关段落
- URL：https://aclanthology.org/2022.acl-long.556.pdf
- 位置：原论文PDF第2页§2：固定四例、24种排列，支持示例集合不变的换序检验。；判断：原论文PDF第2页§2：固定四例、24种排列，支持示例集合不变的换序检验。（记录：sources_ch10_11.json / S1011-05）。

### S0911-039 · 已核相关段落
- URL：https://aclanthology.org/P02-1040.pdf
- 位置：§2.1截断匹配计数、§2.3语料级长度惩罚与加权几何平均；正文字符化和短句null为明示的教学约定。；判断：§2.1截断匹配计数、§2.3语料级长度惩罚与加权几何平均；正文字符化和短句null为明示的教学约定。（记录：sources_ch10_11.json / S1011-07）。

### S0911-040 · 已核相关段落
- URL：https://aclanthology.org/W04-1013.pdf
- 位置：§2 ROUGE-N召回分母，§3.1 LCS定义、P/R与F；摘要级与单序列区别另核官方实现README。本书F1不冒充原论文所有beta设置。；判断：§2 ROUGE-N召回分母，§3.1 LCS定义、P/R与F；摘要级与单序列区别另核官方实现README。本书F1不冒充原论文所有beta设置。（记录：sources_ch10_11.json / S1011-08）。

### S0911-041 · 已核相关段落
- URL：https://aclanthology.org/W14-3346.pdf
- 位置：§1—2：高阶匹配为0使无平滑几何平均为0；不同平滑会改变句级BLEU。；判断：§1—2：高阶匹配为0使无平滑几何平均为0；不同平滑会改变句级BLEU。（记录：sources_ch10_11.json / S1011-09）。

### S0911-042 · 已核相关段落
- URL：https://github.com/mjpost/sacrebleu/blob/master/sacrebleu/metrics/bleu.py
- 位置：compute_bleu官方代码229—267行：短候选BP、无匹配返回0、total=0截断、effective_order选择有效阶数与平滑；本节null是自定约定。；判断：compute_bleu官方代码229—267行：短候选BP、无匹配返回0、total=0截断、effective_order选择有效阶数与平滑；本节null是自定约定。（记录：sources_ch10_11.json / S1011-10）。

### S0911-043 · 已核相关段落
- URL：https://github.com/google-research/google-research/blob/master/rouge/README.md
- 位置：Two flavors of ROUGE-L：rougeL忽略换行，rougeLsum按句界计算union-LCS；支持正文自定单序列与标准摘要口径区别。；判断：Two flavors of ROUGE-L：rougeL忽略换行，rougeLsum按句界计算union-LCS；支持正文自定单序列与标准摘要口径区别。（记录：sources_ch10_11.json / S1011-11）。

### S0911-044 · 已核相关段落
- URL：https://aclanthology.org/2021.tacl-1.24.pdf
- 位置：§4.3：coherence/consistency/fluency/relevance四维、给评员来源与候选、随机排列，支持分维度及来源依据；本书三维量表为自编非照搬。；判断：§4.3：coherence/consistency/fluency/relevance四维、给评员来源与候选、随机排列，支持分维度及来源依据；本书三维量表为自编非照搬。（记录：sources_ch10_11.json / S1011-12）。

### S0911-045 · 已核相关段落
- URL：https://aclanthology.org/2021.tacl-1.87.pdf
- 位置：§3.3、表1—2及§3.4末段：具体错误位置、全文上下文、评阅者能力、匿名系统和随机顺序；不照搬其加权分数。；判断：§3.3、表1—2及§3.4末段：具体错误位置、全文上下文、评阅者能力、匿名系统和随机顺序；不照搬其加权分数。（记录：sources_ch10_11.json / S1011-13）。

### S0911-046 · 已核相关段落
- URL：https://aclanthology.org/2020.inlg-1.23.pdf
- 位置：§4.2.3及§5：问题可能混入多个维度，定义与操作说明需明确；支持分别报告评价问题和指令。；判断：§4.2.3及§5：问题可能混入多个维度，定义与操作说明需明确；支持分别报告评价问题和指令。（记录：sources_ch10_11.json / S1011-14）。

### S0911-047 · 已核相关段落
- URL：https://aclanthology.org/W19-8643.pdf
- 位置：§4.4与表3 Design行：固定呈现顺序可造成疲劳/练习等效应，建议随机化/平衡并报告。；判断：§4.4与表3 Design行：固定呈现顺序可造成疲劳/练习等效应，建议随机化/平衡并报告。（记录：sources_ch10_11.json / S1011-15）。

### S0911-048 · 已核相关段落
- URL：https://arxiv.org/html/2306.05685v4
- 位置：§3.1—3.4：单答评分、成对比较、参考引导；位置/冗长偏好与自偏好须区别，原文不确认普遍自偏好。正文亦保留此限。；判断：§3.1—3.4：单答评分、成对比较、参考引导；位置/冗长偏好与自偏好须区别，原文不确认普遍自偏好。正文亦保留此限。（记录：sources_ch10_11.json / S1011-16）。

### S0911-049 · 已核相关段落
- URL：https://aclanthology.org/2023.emnlp-main.153.pdf
- 位置：§2 Method及图1：任务定义、评价标准、步骤与评分函数分开；正文自编协议不是复刻概率加权G-Eval。；判断：§2 Method及图1：任务定义、评价标准、步骤与评分函数分开；正文自编协议不是复刻概率加权G-Eval。（记录：sources_ch10_11.json / S1011-17）。

### S0911-050 · 已核相关段落
- URL：https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm
- 位置：NIST公式段及Terminology Note：Wilson分母、中心与半宽公式相符；与精确二项区间不同。；判断：NIST公式段及Terminology Note：Wilson分母、中心与半宽公式相符；与精确二项区间不同。（记录：sources_ch10_11.json / S1011-18）。

### S0911-051 · 已核相关段落
- URL：https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bootstrap.html
- 位置：官方文档percentile步骤、paired参数与method：同索引成对抽样、百分位/basic/BCa区别；不保证本文少量来源穷举区间覆盖率。；判断：官方文档percentile步骤、paired参数与method：同索引成对抽样、百分位/basic/BCa区别；不保证本文少量来源穷举区间覆盖率。（记录：sources_ch10_11.json / S1011-19）。

### S0911-052 · 已核相关段落
- URL：https://cameron.econ.ucdavis.edu/research/Cameron_Miller_JHR_2015_February.pdf
- 位置：摘要与II.D/VI.C相关段：组内相关、整组有放回抽样、小组数bootstrap风险；支持本文整组抽样且不将6组穷举冒称精确覆盖保证。；判断：摘要与II.D/VI.C相关段：组内相关、整组有放回抽样、小组数bootstrap风险；支持本文整组抽样且不将6组穷举冒称精确覆盖保证。（记录：sources_ch10_11.json / S1011-20）。

### S0911-053 · 已核相关段落
- URL：https://itl.nist.gov/div898/software/dataplot/refman1/auxillar/mcnemar.htm
- 位置：Description及assumptions：二元配对、配对单位独立、比较两种不一致对概率；列出小样本二项与大样本近似。；判断：Description及assumptions：二元配对、配对单位独立、比较两种不一致对概率；列出小样本二项与大样本近似。（记录：sources_ch10_11.json / S1011-21）。

### S0911-054 · 已核相关段落
- URL：https://www.statsmodels.org/stable/_modules/statsmodels/stats/contingency_tables.html
- 位置：mcnemar函数1638—1709行：exact用min(n1,n2)、二项CDF乘2截1，correction仅近似分支。；判断：mcnemar函数1638—1709行：exact用min(n1,n2)、二项CDF乘2截1，correction仅近似分支。（记录：sources_ch10_11.json / S1011-22）。

### S0911-055 · 已核相关段落
- URL：https://aclanthology.org/2023.emnlp-main.741/
- 位置：ACL原论文摘要：将长文本拆为atomic facts，并求可靠知识来源支持的比例；只支持方法定义，不为本章虚构渡口背书。；判断：ACL原论文摘要：将长文本拆为atomic facts，并求可靠知识来源支持的比例；只支持方法定义，不为本章虚构渡口背书。（记录：sources_ch10_11.json / S1011-23）。

### S0911-056 · 已核相关段落
- URL：https://aclanthology.org/2023.emnlp-main.398/
- 位置：原论文PDF§3.3 Citation Quality及图3已在同一校对轮6—8来源S16核读：引文位置与实质支持区分；无关引文与覆盖分别评价。；判断：原论文PDF§3.3 Citation Quality及图3已在同一校对轮6—8来源S16核读：引文位置与实质支持区分；无关引文与覆盖分别评价。（记录：sources_ch10_11.json / S1011-24）。

### S0911-057 · 已核相关段落
- URL：https://arxiv.org/html/1810.03993v2
- 位置：§4.3.4—4.7：评价因素、阈值、变异和置信区间、评价数据预处理、分组结果；支持正文卡片条件，不证明教学数据真实性。；判断：§4.3.4—4.7：评价因素、阈值、变异和置信区间、评价数据预处理、分组结果；支持正文卡片条件，不证明教学数据真实性。（记录：sources_ch10_11.json / S1011-25）。

### S0911-058 · 已核相关段落
- URL：https://arxiv.org/html/1803.09010v8
- 位置：原论文PDF§1.1、§3.4、§3.7和§4同一轮已核：可按领域调整、原始处理记录、维护更新；不把填表当认证。；判断：原论文PDF§1.1、§3.4、§3.7和§4同一轮已核：可按领域调整、原始处理记录、维护更新；不把填表当认证。（记录：sources_ch10_11.json / S1011-26）。

### S0911-059 · 已核相关段落
- URL：https://huggingface.co/docs/hub/model-cards
- 位置：What are Model Cards：README形式、用途限制、训练参数/数据/评价结果，支持作为官方实现入口。；判断：What are Model Cards：README形式、用途限制、训练参数/数据/评价结果，支持作为官方实现入口。（记录：sources_ch10_11.json / S1011-27）。

### S0911-060 · 已核相关段落
- URL：https://huggingface.co/docs/hub/datasets-cards
- 位置：What are Dataset Cards及metadata：README描述内容/用途背景/偏差、许可语言大小；支持官方数据卡入口，不产生新的使用许可。；判断：What are Dataset Cards及metadata：README描述内容/用途背景/偏差、许可语言大小；支持官方数据卡入口，不产生新的使用许可。（记录：sources_ch10_11.json / S1011-28）。

### S0911-061 · 已核相关段落
- URL：https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation-iterators-for-grouped-data
- 位置：§3.1首段/开发集段及§3.1.2.4：训练测试分开，调参可泄漏测试；相关组会破坏iid，验证组不得在训练中出现，GroupKFold保证组不跨界。；判断：§3.1首段/开发集段及§3.1.2.4：训练测试分开，调参可泄漏测试；相关组会破坏iid，验证组不得在训练中出现，GroupKFold保证组不跨界。（记录：sources_ch10_11.json / S1011-29）。

### S0911-062 · 已核相关段落
- URL：https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestCentroid.html
- 位置：方法定义L638—650：每类由质心代表，测试样本归最近质心；欧氏质心为算术平均。正文只借思想，不称复刻软件所有先验/收缩细节。；判断：方法定义L638—650：每类由质心代表，测试样本归最近质心；欧氏质心为算术平均。正文只借思想，不称复刻软件所有先验/收缩细节。（记录：sources_ch10_11.json / S1011-30）。

### S0911-063 · 已核相关段落
- URL：https://proceedings.mlr.press/v70/guo17a.html
- 位置：原论文摘要：概率校准定义及现代神经网络可能未校准；网页入口访问失败，官方原论文PDF可读。；判断：原论文摘要：概率校准定义及现代神经网络可能未校准；网页入口访问失败，官方原论文PDF可读。（记录：sources_ch10_11.json / S1011-31）。

### S0911-064 · 已核相关段落
- URL：https://scikit-learn.org/stable/modules/model_evaluation.html#confusion-matrix
- 位置：§3.4.4.6：混淆矩阵按真实类为行；正文已注明参考行/预测列，与表格一致。；判断：§3.4.4.6：混淆矩阵按真实类为行；正文已注明参考行/预测列，与表格一致。（记录：sources_ch10_11.json / S1011-32）。

### S0911-065 · 已核相关段落
- URL：https://guides.loc.gov/migrant-mother
- 位置：Introduction第2段及rights入口：1936年3月系列照片、Lange、Florence Owens Thompson及无已知使用限制；未据此新授许可。；判断：Introduction第2段及rights入口：1936年3月系列照片、Lange、Florence Owens Thompson及无已知使用限制；未据此新授许可。（记录：sources_ch10_11.json / S1011-33）。

### S0911-066 · 已核相关段落
- URL：https://github.com/cocodataset/cocoapi/blob/master/PythonAPI/pycocotools/cocoeval.py
- 位置：Params.setDetParams：十IoU及101召回点、maxDets/areaRng；_prepare与evaluateImg核ignore/crowd及普通框不重复匹配；accumulate L377—387右侧最大包络后在recThrs采样。正文明确教学全点面积不是完整COCO。；判断：Params.setDetParams：十IoU及101召回点、maxDets/areaRng；_prepare与evaluateImg核ignore/crowd及普通框不重复匹配；accumulate L377—387右侧最大包络后在recThrs采样。正文明确教学全点面积不是完整COCO。（记录：sources_ch10_11.json / S1011-34）。

### S0911-067 · 已核相关段落
- URL：https://arxiv.org/abs/2005.12872
- 位置：摘要、图1、§3.1及3.2预测FFN：二分匹配、固定查询、不匹配槽用no-object；无需NMS不等于没有匹配评价。；判断：摘要、图1、§3.1及3.2预测FFN：二分匹配、固定查询、不匹配槽用no-object；无需NMS不等于没有匹配评价。（记录：sources_ch10_11.json / S1011-35）。

### S0911-068 · 已核相关段落
- URL：https://arxiv.org/abs/2010.04159
- 位置：摘要及§4.1式3：参考点附近稀疏采样、跨多尺度LK点聚合，慢收敛与小对象动机；不是简单名称扩写。；判断：摘要及§4.1式3：参考点附近稀疏采样、跨多尺度LK点聚合，慢收敛与小对象动机；不是简单名称扩写。（记录：sources_ch10_11.json / S1011-36）。

### S0911-069 · 已核相关段落
- URL：https://arxiv.org/abs/2203.03605
- 位置：作者原摘要：contrastive denoising、mixed query selection、look-forward-twice box prediction；不把论文排名推及历史图像。；判断：作者原摘要：contrastive denoising、mixed query selection、look-forward-twice box prediction；不把论文排名推及历史图像。（记录：sources_ch10_11.json / S1011-37）。

### S0911-070 · 已核相关段落
- URL：https://arxiv.org/abs/2304.07193
- 位置：§4图像/patch自监督目标、EMA教师；§7冻结特征分类/分割评估（表10），与表征提取及任务头区分相符。；判断：§4图像/patch自监督目标、EMA教师；§7冻结特征分类/分割评估（表10），与表征提取及任务头区分相符。（记录：sources_ch10_11.json / S1011-38）。

### S0911-071 · 已核相关段落
- URL：https://arxiv.org/abs/2304.02643
- 位置：作者原摘要与2023投稿日期：SAM为promptable segmentation；具体点/框/掩膜接口另核官方代码。；判断：作者原摘要与2023投稿日期：SAM为promptable segmentation；具体点/框/掩膜接口另核官方代码。（记录：sources_ch10_11.json / S1011-39）。

### S0911-072 · 已核相关段落
- URL：https://github.com/facebookresearch/segment-anything
- 位置：官方README首段与Getting Started：点/框可提示掩码、可自动全图生成；与原模型接口说明相符，不支撑本地连通域算法等于SAM。；判断：官方README首段与Getting Started：点/框可提示掩码、可自动全图生成；与原模型接口说明相符，不支撑本地连通域算法等于SAM。（记录：sources_ch10_11.json / S1011-40）。

### S0911-073 · 已核相关段落
- URL：https://github.com/facebookresearch/segment-anything/blob/main/segment_anything/predictor.py
- 位置：predict参数文档L82—107：点XY、1前景/0背景标签、框XYXY、可选低分辨率掩码；multimask_output为真时输出3个歧义候选。；判断：predict参数文档L82—107：点XY、1前景/0背景标签、框XYXY、可选低分辨率掩码；multimask_output为真时输出3个歧义候选。（记录：sources_ch10_11.json / S1011-41）。

### S0911-074 · 已核相关段落
- URL：https://arxiv.org/abs/2408.00714
- 位置：作者原摘要：图像与视频可提示分割、streaming memory；不把性能百分数转入本章。；判断：作者原摘要：图像与视频可提示分割、streaming memory；不把性能百分数转入本章。（记录：sources_ch10_11.json / S1011-42）。

### S0911-075 · 已核相关段落
- URL：https://github.com/facebookresearch/sam2
- 位置：官方README Image prediction与Video prediction：图像predictor与视频state、add_new_points_or_box及propagate接口；与视频扩展说明相符。；判断：官方README Image prediction与Video prediction：图像predictor与视频state、add_new_points_or_box及propagate接口；与视频扩展说明相符。（记录：sources_ch10_11.json / S1011-43）。

### S0911-076 · 已核相关段落
- URL：https://arxiv.org/abs/1512.03385
- 位置：§3.2式1—2及图2：F(x)+x逐元素加法，维度不同时用投影Ws；支持残差连接解释。；判断：§3.2式1—2及图2：F(x)+x逐元素加法，维度不同时用投影Ws；支持残差连接解释。（记录：sources_ch10_11.json / S1011-44）。

### S0911-077 · 已核相关段落
- URL：https://arxiv.org/html/2010.11929v2
- 位置：§3.1与图1、式1：P×P块、N=HW/P²、训练线性投影、CLS与位置嵌入；支持正文token和注意力长度口径，不证明总显存按L²增长。；判断：§3.1与图1、式1：P×P块、N=HW/P²、训练线性投影、CLS与位置嵌入；支持正文token和注意力长度口径，不证明总显存按L²增长。（记录：sources_ch10_11.json / S1011-45）。

### S0911-078 · 已核相关段落
- URL：https://docs.pytorch.org/tutorials/beginner/transfer_learning_tutorial.html
- 位置：Two major transfer learning scenarios及ConvNet as fixed feature extractor：预训练初始化微调，与冻结网络仅训末层区分；requires_grad=False不省前向计算。；判断：Two major transfer learning scenarios及ConvNet as fixed feature extractor：预训练初始化微调，与冻结网络仅训末层区分；requires_grad=False不省前向计算。（记录：sources_ch10_11.json / S1011-46）。

### S0911-079 · 已核相关段落
- URL：https://keras.io/guides/transfer_learning/
- 位置：Important notes about BatchNormalization：非训练权重均值方差、trainable=False与推断模式特例；微调应保持BN推断；小学习率及改trainable后重compile。；判断：Important notes about BatchNormalization：非训练权重均值方差、trainable=False与推断模式特例；微调应保持BN推断；小学习率及改trainable后重compile。（记录：sources_ch10_11.json / S1011-47）。

### S0911-080 · 已核相关段落
- URL：https://arxiv.org/html/2304.07193v2
- 位置：§4图像/patch自监督目标、EMA教师；§7冻结特征分类/分割评估（表10），与表征提取及任务头区分相符。；判断：§4图像/patch自监督目标、EMA教师；§7冻结特征分类/分割评估（表10），与表征提取及任务头区分相符。（记录：sources_ch10_11.json / S1011-48）。

### S0911-081 · 已核相关段落
- URL：https://github.com/facebookresearch/dinov2
- 位置：README Pretrained backbones、Pretrained heads与语义分割：无标签142M预训练、ViT特征及另接任务头；不与检测DINO混同。；判断：README Pretrained backbones、Pretrained heads与语义分割：无标签142M预训练、ViT特征及另接任务头；不与检测DINO混同。（记录：sources_ch10_11.json / S1011-49）。

### S0911-082 · 已核相关段落
- URL：https://github.com/facebookresearch/dinov2/blob/main/dinov2/models/vision_transformer.py
- 位置：forward_features返回CLS和patch键；vit_small定义embed_dim=384；self.norm是网络归一化，不能推出单位L2长度。；判断：forward_features返回CLS和patch键；vit_small定义embed_dim=384；self.norm是网络归一化，不能推出单位L2长度。（记录：sources_ch10_11.json / S1011-50）。

### S0911-083 · 已核相关段落
- URL：https://github.com/facebookresearch/dinov2/blob/main/dinov2/hub/backbones.py
- 位置：L27—41默认patch_size14、num_register_tokens0；dinov2_vits14使用vit_small；reg版另设4个register。；判断：L27—41默认patch_size14、num_register_tokens0；dinov2_vits14使用vit_small；reg版另设4个register。（记录：sources_ch10_11.json / S1011-51）。

### S0911-084 · 已核相关段落
- URL：https://github.com/facebookresearch/dinov2/blob/main/dinov2/data/transforms.py
- 位置：make_classification_eval_transform：默认resize256、bicubic、center_crop224、ToTensor及Normalize。仅核实现，不证明旧例实际执行。；判断：make_classification_eval_transform：默认resize256、bicubic、center_crop224、ToTensor及Normalize。仅核实现，不证明旧例实际执行。（记录：sources_ch10_11.json / S1011-52）。

### S0911-085 · 已核相关段落
- URL：https://github.com/facebookresearch/dinov2/blob/main/MODEL_CARD.md
- 位置：模型描述与Uses/Bias：CLS与patch特征，ViT-S384维、patch14、224输入256patch，register版另有4；卡片指出西方及富裕家庭偏差。；判断：模型描述与Uses/Bias：CLS与patch特征，ViT-S384维、patch14、224输入256patch，register版另有4；卡片指出西方及富裕家庭偏差。（记录：sources_ch10_11.json / S1011-53）。

### S0911-086 · 已核相关段落
- URL：https://www.image-net.org/challenges/LSVRC/2012/
- 位置：原URL两次直连超时；官方同页ftp主机索引正文Data与Task1完整可读：1000类、约1.2m训练、50k验证及剩余100k测试、最多5个排序标签。核验方式为官方同文搜索索引，非第三方转述。；判断：原URL两次直连超时；官方同页ftp主机索引正文Data与Task1完整可读：1000类、约1.2m训练、50k验证及剩余100k测试、最多5个排序标签。核验方式为官方同文搜索索引，非第三方转述。（记录：sources_ch10_11.json / S1011-54）。

### S0911-087 · 已核相关段落
- URL：https://www.image-net.org/about.php
- 位置：直连超时；原URL的搜索索引完整正文What is ImageNet/Does ImageNet own images段可读：WordNet层级与synset、项目不拥有图片版权。核验方式为原站索引文本，不宣称直接页面成功。；判断：直连超时；原URL的搜索索引完整正文What is ImageNet/Does ImageNet own images段可读：WordNet层级与synset、项目不拥有图片版权。核验方式为原站索引文本，不宣称直接页面成功。（记录：sources_ch10_11.json / S1011-55）。

### S0911-088 · 已核相关段落
- URL：https://raw.githubusercontent.com/cocodataset/cocodataset.github.io/master/dataset/download.htm
- 位置：Images表2017 Train118K、Val5K、Test41K；Overview指出split年份是划分发布年份、不是标注年份。；判断：Images表2017 Train118K、Val5K、Test41K；Overview指出split年份是划分发布年份、不是标注年份。（记录：sources_ch10_11.json / S1011-56）。

### S0911-089 · 已核相关段落
- URL：https://raw.githubusercontent.com/cocodataset/cocodataset.github.io/master/dataset/detection-2017.htm
- 位置：§1 Overview：80对象类；bounding box与object segmentation两项挑战；训练验证标注可取得、2017重新安排train/val。；判断：§1 Overview：80对象类；bounding box与object segmentation两项挑战；训练验证标注可取得、2017重新安排train/val。（记录：sources_ch10_11.json / S1011-57）。

### S0911-090 · 已核相关段落
- URL：https://raw.githubusercontent.com/cocodataset/cocodataset.github.io/master/dataset/format-data.htm
- 位置：§1 Object Detection与annotation结构：左上角0索引、bbox[x,y,width,height]、category_id与iscrowd，区别多边形和RLE。；判断：§1 Object Detection与annotation结构：左上角0索引、bbox[x,y,width,height]、category_id与iscrowd，区别多边形和RLE。（记录：sources_ch10_11.json / S1011-58）。

### S0911-091 · 已核相关段落
- URL：https://cocodataset.org/dataset/detection-eval.htm
- 位置：§2 Metrics及说明1—7：AP跨.50:.05:.95十IoU与80类平均，AP50/AP75区分、最多100检测、box/mask仅IoU不同；不把本地全点插值例称标准COCO。；判断：§2 Metrics及说明1—7：AP跨.50:.05:.95十IoU与80类平均，AP50/AP75区分、最多100检测、box/mask仅IoU不同；不把本地全点插值例称标准COCO。（记录：sources_ch10_11.json / S1011-59）。

### S0911-092 · 已核相关段落
- URL：https://raw.githubusercontent.com/cocodataset/cocodataset.github.io/master/dataset/keypoints-eval.htm
- 位置：§1.1—1.2：关键点评价以OKS作对象相似度、构成AP/AR；与box IoU不能混用。；判断：§1.1—1.2：关键点评价以OKS作对象相似度、构成AP/AR；与box IoU不能混用。（记录：sources_ch10_11.json / S1011-60）。

### S0911-093 · 已核相关段落
- URL：https://raw.githubusercontent.com/cocodataset/cocodataset.github.io/master/dataset/captions-eval.htm
- 位置：§1 Caption Evaluation：BLEU、METEOR、ROUGE-L、CIDEr等描述指标，不是检测AP；逐图与全数据结果分开。；判断：§1 Caption Evaluation：BLEU、METEOR、ROUGE-L、CIDEr等描述指标，不是检测AP；逐图与全数据结果分开。（记录：sources_ch10_11.json / S1011-61）。

### S0911-094 · 已核相关段落
- URL：https://github.com/CSAILVision/sceneparsing
- 位置：官方README Data与Evaluation routines：20210/2000训练验证、150类、原标签0忽略、最终分数为pixel accuracy与mIoU均值。；判断：官方README Data与Evaluation routines：20210/2000训练验证、150类、原标签0忽略、最终分数为pixel accuracy与mIoU均值。（记录：sources_ch10_11.json / S1011-62）。

### S0911-095 · 已核相关段落
- URL：https://ade20k.csail.mit.edu/
- 位置：Full Dataset与Scene Parsing Benchmark入口明确分开，完整集首页列25574训练与2000验证；正文20210/2000专指Scene150开发包，未将两版混同。；判断：Full Dataset与Scene Parsing Benchmark入口明确分开，完整集首页列25574训练与2000验证；正文20210/2000专指Scene150开发包，未将两版混同。（记录：sources_ch10_11.json / S1011-63）。

### S0911-096 · 已核相关段落
- URL：https://raw.githubusercontent.com/cocodataset/cocodataset.github.io/master/dataset/termsofuse.htm
- 位置：Annotations & Website为CC BY4.0；Images明确COCO不拥有版权、图片须按原条款；支持正文分开数据标注/图片权利而非代授许可。；判断：Annotations & Website为CC BY4.0；Images明确COCO不拥有版权、图片须按原条款；支持正文分开数据标注/图片权利而非代授许可。（记录：sources_ch10_11.json / S1011-64）。

### S0911-097 · 已核相关段落
- URL：https://scikit-learn.org/stable/modules/generated/sklearn.metrics.top_k_accuracy_score.html
- 位置：函数定义Top-k及Notes：真实类落前k即正确；并列分数优先较大索引。正文小编号优先明确为自定义，未假托库默认。；判断：函数定义Top-k及Notes：真实类落前k即正确；并列分数优先较大索引。正文小编号优先明确为自定义，未假托库默认。（记录：sources_ch10_11.json / S1011-65）。

### S0911-098 · 已核相关段落
- URL：https://lightning.ai/docs/torchmetrics/stable/segmentation/mean_iou.html
- 位置：Module Interface定义IoU、include_background默认true；双方都缺席返回-1。支持空类处理有实现约定差异，不要求本地空值与库相同。；判断：Module Interface定义IoU、include_background默认true；双方都缺席返回-1。支持空类处理有实现约定差异，不要求本地空值与库相同。（记录：sources_ch10_11.json / S1011-66）。

### S0911-099 · 已核相关段落
- URL：https://arxiv.org/abs/1901.05555
- 位置：作者原摘要：少数类占多数数据/多数类欠代表的长尾定义，重采样/重加权路线；不声称本章三类构成幂律。；判断：作者原摘要：少数类占多数数据/多数类欠代表的长尾定义，重采样/重加权路线；不声称本章三类构成幂律。（记录：sources_ch10_11.json / S1011-67）。

### S0911-100 · 已核相关段落
- URL：https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_fscore_support.html
- 位置：定义、binary及zero_division/Notes：TP/(TP+FP)、TP/(TP+FN)和无正预测时精确率未定义相符。 边界：核定义及零分母说明，不代表已执行软件。；判断：定义、binary及zero_division/Notes：TP/(TP+FP)、TP/(TP+FN)和无正预测时精确率未定义相符。 边界：核定义及零分母说明，不代表已执行软件。（记录：sources_ch10_11.json / S1011-68）。

### S0911-101 · 已核相关段落
- URL：https://scikit-learn.org/stable/modules/generated/sklearn.metrics.balanced_accuracy_score.html
- 位置：定义为逐类召回均值；adjusted=False默认0—1，True为机会校正。与正文采用未调整概念相符。；判断：定义为逐类召回均值；adjusted=False默认0—1，True为机会校正。与正文采用未调整概念相符。（记录：sources_ch10_11.json / S1011-69）。

### S0911-102 · 已核相关段落
- URL：https://imbalanced-learn.org/stable/common_pitfalls.html
- 位置：§9.1：分割前全数据重采样造成泄漏并改变测试类分布；正确流程以pipeline在训练折中采样。；判断：§9.1：分割前全数据重采样造成泄漏并改变测试类分布；正确流程以pipeline在训练折中采样。（记录：sources_ch10_11.json / S1011-70）。

### S0911-103 · 已核相关段落
- URL：https://arxiv.org/html/1903.12261v1
- 位置：§4.1图1与§4.2：15腐蚀类型×5强度，CE用对应AlexNet五级错误和归一化、mCE再平均15类；不是普通正确率下降。；判断：§4.1图1与§4.2：15腐蚀类型×5强度，CE用对应AlexNet五级错误和归一化、mCE再平均15类；不是普通正确率下降。（记录：sources_ch10_11.json / S1011-71）。

### S0911-104 · 已核相关段落
- URL：https://arxiv.org/html/1610.02136v3
- 位置：§1—3：误分与类外检测是相关但不同问题，最高softmax分数可作基线；单个高分不等于可靠信心，§3.1表1—2显示高分错误/类外。；判断：§1—3：误分与类外检测是相关但不同问题，最高softmax分数可作基线；单个高分不等于可靠信心，§3.1表1—2显示高分错误/类外。（记录：sources_ch10_11.json / S1011-72）。

### S0911-105 · 已核相关段落
- URL：https://arxiv.org/html/2007.01434v1
- 位置：§3及§3.1三选择方法：调参策略必须说明、oracle测试域访问受限且不可和无oracle直接比；§4初版9算法7数据3方法、§5.1同条件ERM比较。正文仅借划分与公平比较原则。；判断：§3及§3.1三选择方法：调参策略必须说明、oracle测试域访问受限且不可和无oracle直接比；§4初版9算法7数据3方法、§5.1同条件ERM比较。正文仅借划分与公平比较原则。（记录：sources_ch10_11.json / S1011-73）。

### S0911-106 · 已核相关段落
- URL：https://www.jmlr.org/papers/v11/cawley10a.html
- 位置：期刊原文摘要：有限样本模型选择指标的方差可导致选择过拟合，随后性能评价有选择偏差；直接支持开发阶段反复选取适应偶然差异。；判断：期刊原文摘要：有限样本模型选择指标的方差可导致选择过拟合，随后性能评价有选择偏差；直接支持开发阶段反复选取适应偶然差异。（记录：sources_ch10_11.json / S1011-74）。

### S0911-107 · 已核相关段落
- URL：https://jmlr.org/papers/v13/bergstra12a.html
- 位置：期刊原文摘要：同搜索域与计算预算比较随机/网格搜索，所找到方案随预算/重要参数覆盖改变；支持说明搜索预算，不推出次数相同=耗时相同。；判断：期刊原文摘要：同搜索域与计算预算比较随机/网格搜索，所找到方案随预算/重要参数覆盖改变；支持说明搜索预算，不推出次数相同=耗时相同。（记录：sources_ch10_11.json / S1011-75）。

### S0911-108 · 已核相关段落
- URL：https://www.itl.nist.gov/div898/handbook/pri/section3/pri333.htm
- 位置：Full factorial designs定义：每因素每取值与其余因素所有取值组合，k个二水平因素需2^k次；两因素四格是全因子结构而非自然史因果证明。；判断：Full factorial designs定义：每因素每取值与其余因素所有取值组合，k个二水平因素需2^k次；两因素四格是全因子结构而非自然史因果证明。（记录：sources_ch10_11.json / S1011-76）。

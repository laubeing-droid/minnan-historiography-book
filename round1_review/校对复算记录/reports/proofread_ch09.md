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

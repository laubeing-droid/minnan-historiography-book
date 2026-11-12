# 第6—8章全部原引用URL，按完整URL去重

计数：{"CHECKED_SUPPORTS_CITED_CLAIM": 83, "ACCESS_BLOCKED": 1}。

### S0608-001 · 已核相关段落
- URL：https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview
- 位置：Classic RAG／Content preparation and ingestion；判断：经典流程先取材料，再交生成模型；切块和向量化属于资料准备。（记录：sources_ch06.json / S06-01）。

### S0608-002 · 已核相关段落
- URL：https://tjj.fujian.gov.cn/xxgk/tjgb/202105/t20210520_5598804.htm
- 位置：开头、第一部分第二段、表2-1、表2-2及注1—3；判断：2020统计时点、2021发布日期及初步汇总边界；泉州人数8782285、增量653755、份额22.03至21.14、女性47.78、性别比109.31及不含金门马祖相符。（记录：sources_ch06.json / S06-02）。

### S0608-003 · 已核相关段落
- URL：https://tjj.fujian.gov.cn/tongjinianjian/rk2020/html/fu0202.pdf
- 位置：PDF第1—4页（印刷2887—2890），表2-1／2-2及注1—3；判断：年鉴PDF与网页统计数字和表头一致；表2-1的2010列是比重而非2010人数。（记录：sources_ch06.json / S06-03）。

### S0608-004 · 已核相关段落
- URL：https://aclanthology.org/2020.emnlp-main.550/
- 位置：ACL论文页面Abstract与书目信息；判断：2020年论文及双编码器稠密段落检索摘要相符。（记录：sources_ch06.json / S06-04）。

### S0608-005 · 已核相关段落
- URL：https://aclanthology.org/2020.emnlp-main.550.pdf
- 位置：§3.1，印刷6770—6771，公式1；判断：问题与段落分别编码；以内积比较向量，段落可预先编码。（记录：sources_ch06.json / S06-05）。

### S0608-006 · 已核相关段落
- URL：https://arxiv.org/html/2005.11401v4
- 位置：§2.1 RAG-Sequence／§2.2 Retriever／§2.4 Training；判断：原论文有检索加生成、top-k边缘化与联合微调；不能把所有RAG都定义为不更新参数。（记录：sources_ch06.json / S06-06）。

### S0608-007 · 已核相关段落
- URL：https://arxiv.org/html/2005.14165v4
- 位置：Abstract及§1对few-shot/in-context learning的说明；判断：文中few-shot以文字示范和交互指定任务，不在该任务适配中更新梯度。（记录：sources_ch06.json / S06-07）。

### S0608-008 · 已核相关段落
- URL：https://learn.microsoft.com/en-us/azure/search/vector-search-how-to-chunk-documents
- 位置：Common chunking patterns／Content overlap considerations；判断：固定、结构与语义切块以及重叠的连贯性／成本权衡相符。（记录：sources_ch06.json / S06-08）。

### S0608-009 · 已核相关段落
- URL：https://huggingface.co/docs/transformers/main/tokenizer_summary
- 位置：Subword tokenization／SentencePiece；判断：子词词元并不等于汉字数，中文等无空格文本仍须由各模型词元器处理。（记录：sources_ch06.json / S06-09）。

### S0608-010 · 已核相关段落
- URL：https://aclanthology.org/D19-1410.pdf
- 位置：§3 Model，印刷3984；判断：SBERT把输出汇聚成定长句向量；CLS、平均与最大汇聚均为论文比较项。（记录：sources_ch06.json / S06-10）。

### S0608-011 · 已核相关段落
- URL：https://sbert.net/examples/sentence_transformer/applications/semantic-search/README.html
- 位置：Background／Symmetric vs. Asymmetric Semantic Search／Manual Implementation；判断：问题与长段落是非对称检索；查询和语料进入同一向量空间比较。（记录：sources_ch06.json / S06-11）。

### S0608-012 · 已核相关段落
- URL：https://huggingface.co/BAAI/bge-small-zh-v1.5
- 位置：Model List及脚注1／Usage；判断：bge-small-zh-v1.5为中文型号，检索查询指令见型号表；正文不加同一查询指令。（记录：sources_ch06.json / S06-12）。

### S0608-013 · 已核相关段落
- URL：https://huggingface.co/BAAI/bge-small-zh-v1.5/raw/main/config.json
- 位置：config.json：hidden_size、max_position_embeddings；判断：隐藏向量维度512，位置上限512；与正文型号表相符。（记录：sources_ch06.json / S06-13）。

### S0608-014 · 已核相关段落
- URL：https://huggingface.co/BAAI/bge-small-zh-v1.5/blob/main/sentence_bert_config.json
- 位置：sentence_bert_config.json：max_seq_length；判断：句向量封装的最大序列长度512。（记录：sources_ch06.json / S06-14）。

### S0608-015 · 已核相关段落
- URL：https://huggingface.co/BAAI/bge-small-zh-v1.5/blob/main/1_Pooling/config.json
- 位置：1_Pooling/config.json；判断：word_embedding_dimension=512，CLS汇聚为true、均值与最大汇聚为false。（记录：sources_ch06.json / S06-15）。

### S0608-016 · 已核相关段落
- URL：https://huggingface.co/intfloat/multilingual-e5-small/raw/main/README.md
- 位置：模型概要／Usage／Supported Languages／Limitations；判断：e5-small向量384维；query:/passage:前缀适用于非英语；attention_mask均值汇聚、L2归一化、512截断；100种语言并不保证低资源语表现相同。（记录：sources_ch06.json / S06-16）。

### S0608-017 · 已核相关段落
- URL：https://github.com/facebookresearch/faiss/wiki/MetricType-and-distances
- 位置：How can I index vectors for cosine similarity?；判断：查询和语料均归一化后，最大内积排序等价于余弦排序。（记录：sources_ch06.json / S06-17）。

### S0608-018 · 已核相关段落
- URL：https://sbert.net/docs/package_reference/sentence_transformer/model.html
- 位置：构造函数local_files_only/token；encode的prompt、convert_to_numpy、normalize_embeddings；tokenizer属性；判断：限定本地读取、认证token、前缀、归一化与数组返回的参数含义相符；tokenizer属性仍可获取所用词元器。（记录：sources_ch06.json / S06-18）。

### S0608-019 · 已核相关段落
- URL：https://huggingface.co/docs/transformers/main_classes/tokenizer
- 位置：__call__参数表及Returns: BatchEncoding；判断：特殊词元、截断、补齐分开控制；input_ids是模型输入的词元ID而非字符位置。（记录：sources_ch06.json / S06-19）。

### S0608-020 · 已核相关段落
- URL：https://www.elastic.co/docs/solutions/search/full-text/how-full-text-works
- 位置：开头Text analysis／Inverted index creation／Relevance scoring；判断：倒排索引由词项指向文档；BM25使用词频、文档频率和长度。（记录：sources_ch06.json / S06-20）。

### S0608-021 · 已核相关段落
- URL：https://nlp.stanford.edu/IR-book/html/htmledition/tokenization-1.html
- 位置：§2.2.1：定义、O’Neill例后查询处理段、中文分词末段（同URL索引正文）；判断：查询和文档须一致词元化；中文词界存在歧义，词项不应机械等于逐字。（记录：sources_ch06.json / S06-21）。
- 获取情况：原URL直接open两次超时；站内精准搜索返回同URL完整相关段落，已核其索引正文。

### S0608-022 · 已核相关段落
- URL：https://lucene.apache.org/__root/docs.lucene.apache.org/core/9_12_0/core/org/apache/lucene/search/similarities/BM25Similarity.html
- 位置：BM25Similarity构造函数、idf、avgFieldLength；判断：默认k1=1.2、b=.75；Lucene的带1对数idf及平均长度说明相符。（记录：sources_ch06.json / S06-22）。

### S0608-023 · 访问阻塞
- URL：https://www.staff.city.ac.uk/~sbrp622/papers/foundations_bm25_review.pdf
- 位置：未取得作者原PDF；判断：待核原论文§3.1公式3.3、§3.4.5—3.5.1及分子k1+1变体；不能把Lucene接口页等同原论文该页已核。（记录：sources_ch06.json / S06-23）。
- 获取情况：HTTPS两次及HTTP转HTTPS一次均Timeout fetching；精准搜索未返回原论文可核正文。
- 限界：该原论文所引页与公式本轮未独立核到；不据访问失败认定正文错误。

### S0608-024 · 已核相关段落
- URL：https://learn.microsoft.com/en-us/azure/search/hybrid-search-overview
- 位置：Why use hybrid search?／How does hybrid search work?；判断：精确人名数字等可受益于关键词；向量匹配概念相关材料；并行结果用RRF融合。（记录：sources_ch06.json / S06-24）。

### S0608-025 · 已核相关段落
- URL：https://learn.microsoft.com/en-us/azure/search/vector-search-filters
- 位置：How filtering works／Set the filter mode；判断：后过滤与先取全库top-k后过滤均有漏掉范围内候选的风险；筛选字段来自非向量元数据。（记录：sources_ch06.json / S06-25）。

### S0608-026 · 已核相关段落
- URL：https://www.elastic.co/docs/reference/elasticsearch/rest-apis/reciprocal-rank-fusion
- 位置：开头公式／rank_constant／rank_window_size；判断：RRF按各榜名次加1/(常数+名次)，未入榜贡献0；名次自1、默认常数60；窗口可截断。（记录：sources_ch06.json / S06-26）。

### S0608-027 · 已核相关段落
- URL：https://plg.uwaterloo.ca/~gvcormac/cormacksigir09-rrf.pdf
- 位置：§1公式及k=60说明；判断：原RRF公式与本书教学融合式相符，常数60不是取前60条的k。（记录：sources_ch06.json / S06-27）。

### S0608-028 · 已核相关段落
- URL：https://learn.microsoft.com/en-us/azure/search/hybrid-search-ranking
- 位置：How RRF ranking works／Scores in hybrid search results；判断：融合常数与近邻数不同；BM25、向量、RRF计分尺度不同，不能直接当同一概率。（记录：sources_ch06.json / S06-28）。

### S0608-029 · 已核相关段落
- URL：https://www.elastic.co/docs/reference/elasticsearch/rest-apis/search-rank-eval
- 位置：Precision at K／Recall at K／Mean reciprocal rank；判断：三种指标分别关注前k相关比例、全部相关召回和首个相关位置；本书短返回、重复证据和零相关约定另行明示。（记录：sources_ch06.json / S06-29）。

### S0608-030 · 已核相关段落
- URL：https://learn.microsoft.com/en-us/azure/search/semantic-how-to-query-rewrite
- 位置：开头、精确词项警示、Test query rewrites with debug；判断：保留原问并共同检索；改写可能丢失精确词；debug可查看改写，须评估是否保持任务含义。（记录：sources_ch06.json / S06-30）。

### S0608-031 · 已核相关段落
- URL：https://whc.unesco.org/en/list/1561/
- 位置：英文Description末句；判断：Zayton的历史用法限于10—14世纪阿拉伯与西方文本，不等同现代地域范围。（记录：sources_ch06.json / S06-31）。

### S0608-032 · 已核相关段落
- URL：https://aclanthology.org/2023.emnlp-main.322.pdf
- 位置：§3.1，印刷5306；§6.2—6.3，5310—5311；判断：重写—检索—阅读流程；案例和检索指标表明命中改善与回答改善需分别看，改写可产生错误理解。（记录：sources_ch06.json / S06-32）。

### S0608-033 · 已核相关段落
- URL：https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- 位置：Be clear and direct／Structure prompts with XML tags；判断：明确输出要求、分开指令/上下文/输入的建议确有依据；不代表本书人工拟答由模型产生。（记录：sources_ch06.json / S06-33）。

### S0608-034 · 已核相关段落
- URL：https://aclanthology.org/2023.emnlp-main.398.pdf
- 位置：§3.2—3.3，印刷6467—6469；判断：回答正确与覆盖、引文支持覆盖和无关引文分开评价；引用数量不能替代支持关系。（记录：sources_ch06.json / S06-34）。

### S0608-035 · 已核相关段落
- URL：https://nlp.stanford.edu/IR-book/html/htmledition/information-retrieval-system-evaluation-1.html
- 位置：§8.1全节（同URL索引正文）；判断：测试集合含文档、信息需要及相关性判断；按信息需要判定而非机械同词；开发集调参后在独立测试集评价。（记录：sources_ch06.json / S06-35）。
- 获取情况：原URL直接open两次超时；站内精准搜索返回同URL完整相关段落，已核其索引正文。

### S0608-036 · 已核相关段落
- URL：https://nlp.stanford.edu/IR-book/html/htmledition/assessing-relevance-1.html
- 位置：§8.5第1—3段及分歧讨论（同URL索引正文）；判断：小型集合可穷尽判定，较大集合用pooling；评阅者有分歧，需记录和核对。（记录：sources_ch06.json / S06-36）。
- 获取情况：原URL直接open两次超时；站内精准搜索返回同URL完整相关段落，已核其索引正文。

### S0608-037 · 已核相关段落
- URL：https://nlp.stanford.edu/IR-book/html/htmledition/critiques-and-justifications-of-the-concept-of-relevance-1.html
- 位置：§8.5.1：marginal relevance段（同URL索引正文）；判断：高度相关但重复的信息可能无新增效用；不同事实可作评价单位，不等于史学上多个独立来源。（记录：sources_ch06.json / S06-37）。
- 获取情况：原URL直接open两次超时；站内精准搜索返回同URL完整相关段落，已核其索引正文。

### S0608-038 · 已核相关段落
- URL：https://archives.sinica.edu.tw/collectionDetail/25/69
- 位置：本筆檔案說明首段；判断：本筆檔案說明首段：该页确记1932、1944两度出任教育部长。 边界：核的是馆方后编说明文字，不是任命文书，不裁决1931/1932孰为就任年。（记录：sources_ch07.json / S07-01）。

### S0608-039 · 已核相关段落
- URL：https://lib.ihp.sinica.edu.tw/03-rare/MWSP/01/a.htm
- 位置：1945年秋句、1949年首句、文末来源说明；判断：1945年秋句、1949年首句、文末来源说明：1945年秋代理北京大学校长、1949年一月二十日就任国立台湾大学校长；1995年专刊19—37页摘编说明与正文相符。 边界：核的是后编传略，未核原始任命档案。（记录：sources_ch07.json / S07-02）。

### S0608-040 · 已核相关段落
- URL：https://www.lib.nthu.edu.tw/library/project/jigang/dictionary/dictionary15.htm
- 位置：傳略段；判断：傳略段：该页确写1931年出任教育部长，支持正文保留两来源差异。 边界：未据此裁定哪一记载为最终史实。（记录：sources_ch07.json / S07-03）。

### S0608-041 · 已核相关段落
- URL：https://www.icpsr.umich.edu/sites/ICPSR/manage-data/prepare-deposit/guide
- 位置：Missing Data／Selecting Missing Data Codes；判断：缺失原因须分别编码；拒答、不知、不适用、无匹配等不能合并成无意义空格；标识变量可保留缺失状态。（记录：sources_ch07.json / S07-04）。

### S0608-042 · 已核相关段落
- URL：https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CE.html
- 位置：§22.1 Levels of Certainty；§22.2 Indications of Precision及上下限实例；判断：不确定性与数值精度不同；可把起讫和上下限分开表达，保留各自精度。（记录：sources_ch07.json / S07-05）。

### S0608-043 · 已核相关段落
- URL：https://www.loc.gov/standards/datetime/
- 位置：Level 0 Date／Level 1 Seasons／Level 2 Set representation；判断：年、月、日精度不同；季节有独立写法；单选集合与全包含集合分别表达，不把年份冲突改成连续区间。（记录：sources_ch07.json / S07-06）。

### S0608-044 · 已核相关段落
- URL：https://chgis.fas.harvard.edu/pages/database/
- 位置：§2 Overview、§2.2 Boundary Changes、§2.3 Point Location Changes；判断：同名行政单位随时间可改边界或治所；历史面对象与点对象不是同一项，不能用现今地点直接替代。（记录：sources_ch07.json / S07-07）。

### S0608-045 · 已核相关段落
- URL：https://aclanthology.org/2024.cl-3.1/
- 位置：原论文PDF§3.1，印刷823—825（由ACL页面进入）；判断：指南是迭代文件；试标、批次评价及修订相互衔接；标签定义与何时使用标签的指南作用不同。（记录：sources_ch07.json / S07-08）。

### S0608-046 · 已核相关段落
- URL：https://projects.csail.mit.edu/workbench/update/guides/00%20-%20Adjudicator%27s%20Guide_v1.2.0.pdf
- 位置：PDF第1页What is Adjudication?及下方双人标注说明；判断：双人独立标注，合并前计算一致性；低一致可能促使修订指南而非强制只保留多数意见。（记录：sources_ch07.json / S07-09）。

### S0608-047 · 已核相关段落
- URL：https://sklearn.org/stable/modules/generated/sklearn.metrics.cohen_kappa_score.html
- 位置：定义、weights与未定义值说明；判断：定义、weights与未定义值说明：(po-pe)/(1-pe)、每位标注者类别先验及不加权解释相符。 边界：sklearn.org原域一次429；scikit-learn.org官方同页成功。（记录：sources_ch07.json / S07-10）。

### S0608-048 · 已核相关段落
- URL：https://aclanthology.org/J08-4004/
- 位置：所链接原论文PDF§2.1，印刷556—557；复用本轮S09-27原文记录；判断：一致与可靠性是有效性的必要条件，不保证标注捕捉真正目标；不能将高κ直接当正确率。（记录：sources_ch07.json / S07-11）。

### S0608-049 · 已核相关段落
- URL：https://aclanthology.org/2020.acl-main.560/
- 位置：所链接原论文PDF§2.1 Features，印刷6283；判断：语言资源分布按已标注与未标注资源两轴观察；使用者规模不直接代表机器学习资源规模。（记录：sources_ch07.json / S07-12）。

### S0608-050 · 已核相关段落
- URL：https://www.rfc-editor.org/rfc/rfc6365.html
- 位置：§2 Fundamental Terms，印刷5—6：language/script/writing system；判断：语言、字符体系与书写体系不是同一对象；一个语言可用不同script，一套script可写多语言。（记录：sources_ch07.json / S07-13）。

### S0608-051 · 已核相关段落
- URL：https://sutian.moe.edu.tw/zh-hant/su/6117/
- 位置：词目及音读；判断：词目及音读：校長与hāu-tiúnn相符。 边界：仅核词条；台罗体例链接未另读。（记录：sources_ch07.json / S07-14）。

### S0608-052 · 已核相关段落
- URL：https://sutian.moe.edu.tw/zh-hant/piantsip/tailo-phiautsu-suatbing/
- 位置：页首说明、一般声调表、变调末段；判断：采用台罗；表中带调符号与数字版有对应，词典标本调而非逐句连读变调，支持把罗马字记为文字形式而不是另造语言。（记录：sources_ch07.json / S07-15）。

### S0608-053 · 已核相关段落
- URL：https://tul.blog.ntu.edu.tw/archives/14535
- 位置：更新日期及开头两项介绍；判断：更新日期及开头两项介绍：2026-03-16更新；日文1898—1944、汉文1905—1911及同界面说明相符。 边界：资源说明，不等于逐篇报纸内容已核。（记录：sources_ch07.json / S07-16）。

### S0608-054 · 已核相关段落
- URL：https://aclanthology.org/2020.emnlp-main.618/
- 位置：所链接原论文PDF摘要与§1；复用本轮S09-30原文记录；判断：翻译会改变表面线索如词语重叠；原生与翻译材料的评价条件不可混为同一资源。（记录：sources_ch07.json / S07-17）。

### S0608-055 · 已核相关段落
- URL：https://scikit-learn.org/stable/modules/cross_validation.html
- 位置：§3.1开头及§3.1.2.4 grouped data；判断：同数据训练和测试会高估；反复选择超参数可向测试泄漏；应保留验证及最终测试，评价新组需组间隔离。（记录：sources_ch07.json / S07-18）。
- 位置：§3.1 开头，网页行 74、99—106（协作核对记录）；判断：开发验证可用于选择方案，最终测试须隔离，反复据测试调设置会泄漏。（记录：sources_ch08.json / S08-06）。

### S0608-056 · 已核相关段落
- URL：https://scikit-learn.org/stable/common_pitfalls.html
- 位置：§12.2、§12.2.1及§12.2.2；判断：测试数据不能用于模型选择；预处理参数只由训练集学习，再对两侧同样transform；特征选择也适用。（记录：sources_ch07.json / S07-19）。

### S0608-057 · 已核相关段落
- URL：https://aclanthology.org/2021.eacl-main.113/
- 位置：原论文PDF摘要、§1、§3、§4.1，印刷1325—1327；判断：随机拆分忽略相似记录来源会漏出训练信息；AIMed随机折与按来源文档ID隔离折明确对照。（记录：sources_ch07.json / S07-20）。

### S0608-058 · 已核相关段落
- URL：https://arxiv.org/pdf/2207.07048v1
- 位置：指定v1 PDF第5—6页，§2.4 L3.1/L3.2；判断：未来预测须阻止时间倒置；依赖单位跨训练测试的风险，应与科学主张要求的推广分布匹配。（记录：sources_ch07.json / S07-21）。

### S0608-059 · 已核相关段落
- URL：https://arxiv.org/pdf/1803.09010v8
- 位置：原论文PDF§1.1、§3.4、§3.7和§4同一轮已核；判断：原论文PDF§1.1、§3.4、§3.7和§4同一轮已核：可按领域调整、原始处理记录、维护更新；不把填表当认证。（记录：sources_ch07.json / S07-22）。

### S0608-060 · 已核相关段落
- URL：https://research.google/blog/the-data-cards-playbook-a-toolkit-for-transparency-in-dataset-documentation/
- 位置：2022-11-17页首作者及开头第1—3段；判断：Data Cards为结构化概要，列明上游来源、收集标注、训练评价、预期用途及影响性能的决策。（记录：sources_ch07.json / S07-23）。

### S0608-061 · 已核相关段落
- URL：https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html
- 位置：normalize 参数及 Returns，网页行 655—669；判断：准确率是答对样本比例，即本例 (TP+TN)/总句数。（记录：sources_ch08.json / S08-01）。

### S0608-062 · 已核相关段落
- URL：https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_fscore_support.html
- 位置：定义、binary及zero_division/Notes：TP/(TP+FP)、TP/(TP+FN)和无正预测时精确率未定义相符。 边界：核定义及零分母说明，不代表已执行软件。；判断：定义、binary及zero_division/Notes：TP/(TP+FP)、TP/(TP+FN)和无正预测时精确率未定义相符。 边界：核定义及零分母说明，不代表已执行软件。（记录：sources_ch08.json / S08-02）。

### S0608-063 · 已核相关段落
- URL：https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html
- 位置：开头公式与 binary 说明，网页行 635—643；判断：正类 F1=2TP/(2TP+FP+FN)，不是两类平均。（记录：sources_ch08.json / S08-03）。

### S0608-064 · 已核相关段落
- URL：https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html
- 位置：导言、strategy 参数及示例，网页行 638—656、714—726；判断：most_frequent 按训练答案中的多数类固定作答。（记录：sources_ch08.json / S08-04）。

### S0608-065 · 已核相关段落
- URL：https://www.itl.nist.gov/div898/handbook/pri/section3/pri31.htm
- 位置：5.3.1 开头与结尾，网页行 6—7、24—28；判断：先明确实验目标，再选择因素和设计。（记录：sources_ch08.json / S08-05）。

### S0608-066 · 已核相关段落
- URL：https://docs.python.org/3.12/library/stdtypes.html#common-sequence-operations
- 位置：Common Sequence Operations 表及注 4；Text Sequence Type — str，网页行 420—421、454—455、634—650；判断：text[:8] 取前八个 Unicode 码点，标点占位置，不按字节或词元计。（记录：sources_ch08.json / S08-07）。

### S0608-067 · 已核相关段落
- URL：https://www.itl.nist.gov/div898/handbook/pri/section3/pri333.htm
- 位置：5.3.3.3 定义及 Table 3.2，网页行 8—11；判断：全因子设计含各因素所有设置组合；两个因素各两设置形成四格。（记录：sources_ch08.json / S08-08）。

### S0608-068 · 已核相关段落
- URL：https://proceedings.neurips.cc/paper_files/paper/2024/file/c55e6792923cc16fd6ed5c3f672420a5-Paper-Conference.pdf
- 位置：摘要、引言及2.1开头：停用及替代值选择影响组件重要性解释，作者与题名一致。 边界：仅核所引用的概念区别，不运行其最优消融方法。；判断：摘要、引言及2.1开头：停用及替代值选择影响组件重要性解释，作者与题名一致。 边界：仅核所引用的概念区别，不运行其最优消融方法。（记录：sources_ch08.json / S08-09）。

### S0608-069 · 已核相关段落
- URL：https://proceedings.mlsys.org/paper_files/paper/2021/file/0184b0cd3cfb185989f858a1d9f5c1eb-Paper.pdf
- 位置：PDF第1页摘要与引言：数据抽样、初始化与超参数选择会影响比较得到支持。 边界：仅核引用段，不核全篇结果。；判断：PDF第1页摘要与引言：数据抽样、初始化与超参数选择会影响比较得到支持。 边界：仅核引用段，不核全篇结果。（记录：sources_ch08.json / S08-10）。

### S0608-070 · 已核相关段落
- URL：https://docs.python.org/3.12/library/random.html
- 位置：seed、独立Random对象说明：seed可接受不止整数；因此将正文普遍定义改成本例规定整数。 边界：只核种子与独立状态相关说明，未运行sample。；判断：seed、独立Random对象说明：seed可接受不止整数；因此将正文普遍定义改成本例规定整数。 边界：只核种子与独立状态相关说明，未运行sample。（记录：sources_ch08.json / S08-11）。

### S0608-071 · 已核相关段落
- URL：https://yaml.org/spec/1.2.2/
- 位置：历史说明、§6.1、§7.4.2 映射值说明，网页行 165、1516—1550、3002—3003；判断：YAML 常用冒号、缩进表达结构，YAML 1.2 兼容 JSON，兼容关系不能反向推成 JSON 解析器能读任意 YAML。（记录：sources_ch08.json / S08-12）。

### S0608-072 · 已核相关段落
- URL：https://docs.python.org/3.12/library/json.html
- 位置：导言示例后的 Note 与 Basic Usage，网页行 99—110；判断：JSON 是 YAML 1.2 子集，不等于 json 模块能读取任意缩进式 YAML。（记录：sources_ch08.json / S08-13）。

### S0608-073 · 已核相关段落
- URL：https://docs.pytorch.org/docs/2.9/notes/randomness.html
- 位置：开头两段，网页行 68—71；判断：相同种子不保证跨版本、平台或 CPU/GPU 完全复现。（记录：sources_ch08.json / S08-14）。

### S0608-074 · 已核相关段落
- URL：https://mlflow.org/docs/latest/ml/tracking/
- 位置：导言、Concepts—Runs、Experiments，网页行 37—60；判断：围绕每次运行组织参数、代码版本、指标及输出文件。（记录：sources_ch08.json / S08-15）。

### S0608-075 · 已核相关段落
- URL：https://docs.python.org/3.12/library/exceptions.html#FileNotFoundError
- 位置：FileNotFoundError 定义，网页行 417—420；判断：请求不存在的文件或目录会产生 FileNotFoundError。（记录：sources_ch08.json / S08-16）。

### S0608-076 · 已核相关段落
- URL：https://scikit-learn.org/stable/common_pitfalls.html#data-leakage
- 位置：§12.2 Data leakage，网页行 122—141（协作核对记录）；判断：测试材料不能供方法选择；学习所得预处理条件须只来自训练侧。（记录：sources_ch08.json / S08-17）。

### S0608-077 · 已核相关段落
- URL：https://docs.github.com/en/copilot/get-started/best-practices
- 位置：Create thoughtful prompts；Check Copilot's work，网页行 65—79；判断：拆小任务、明确要求、给出输入输出例，并阅读和测试生成代码。（记录：sources_ch08.json / S08-18）。

### S0608-078 · 已核相关段落
- URL：https://docs.python.org/3.12/library/stdtypes.html#str.find
- 位置：Common Sequence Operations、Text Sequence Type—str、str.find，网页行 420、455、636、722—725；判断：字符串位置从零开始且按码点计，切片右端不含；find 仅返回搜索范围内首处位置。（记录：sources_ch08.json / S08-19）。

### S0608-079 · 已核相关段落
- URL：https://docs.python.org/3.12/library/unittest.html
- 位置：test case 定义及 Basic example，网页行 15—18、72—79；判断：测试检查给定输入的特定响应，可检查预期异常。（记录：sources_ch08.json / S08-20）。

### S0608-080 · 已核相关段落
- URL：https://docs.python.org/3.12/library/stdtypes.html#text-sequence-type-str
- 位置：Text Sequence Type — str，网页行 634—650；判断：Python 字符串位置按 Unicode 码位，不按 UTF-8 字节计。（记录：sources_ch08.json / S08-21）。

### S0608-081 · 已核相关段落
- URL：https://docs.python.org/3.12/library/stdtypes.html#str.strip
- 位置：str.strip 定义、示例及外端说明，网页行 1002—1013；判断：strip 默认清理首尾空白并返回新字符串，不删除中间空格。（记录：sources_ch08.json / S08-22）。

### S0608-082 · 已核相关段落
- URL：https://www.debuggingbook.org/html/DeltaDebugger.html#Manual-Input-Reduction
- 位置：Manual Input Reduction 开头与二分缩减说明，网页行 238—264；判断：缩减输入时去掉不相关部分，每次保持并核对同一种失败。（记录：sources_ch08.json / S08-23）。

### S0608-083 · 已核相关段落
- URL：https://docs.djangoproject.com/en/5.2/intro/contributing/#writing-some-tests-for-your-ticket
- 位置：Writing some tests for your ticket；Running Django’s test suite for the second time，网页行 213—217、278—280；判断：回归例应在缺陷存在时失败、修复后通过，并检查其他既有行为。（记录：sources_ch08.json / S08-24）。

### S0608-084 · 已核相关段落
- URL：https://book.the-turing-way.org/reproducible-research/overview/overview-definitions/
- 位置：Table of Definitions for Reproducibility：同数据同分析重做与换数据检验的区别相符。 边界：未将该定义强作跨学科唯一术语定义。；判断：Table of Definitions for Reproducibility：同数据同分析重做与换数据检验的区别相符。 边界：未将该定义强作跨学科唯一术语定义。（记录：sources_ch08.json / S08-25）。

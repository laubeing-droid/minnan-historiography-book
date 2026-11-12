# 第6章原引用 URL 完整核查台账

2026-10-30。37 个不同 URL：36 项已核相关段落，1 项原 PDF 访问阻塞。4 个 Stanford URL 的直连超时，但已从同一原 URL 的索引正文核得所引段落，逐项明示获取方式，不称实时页直连成功。没有把模型、脚本实际运行列入本表。

## S06-01 · 已核相关段落
- 原 URL：https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview
- 引用位置：第 6.1 节；基线行 54。
- 已核位置：Classic RAG／Content preparation and ingestion。
- 主张判断：经典流程先取材料，再交生成模型；切块和向量化属于资料准备。
- 核查者：独立校读分组A。

## S06-02 · 已核相关段落
- 原 URL：https://tjj.fujian.gov.cn/xxgk/tjgb/202105/t20210520_5598804.htm
- 引用位置：第 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8 节；基线行 56, 107, 153, 261, 356, 454, 510, 532, 611。
- 已核位置：开头、第一部分第二段、表2-1、表2-2及注1—3。
- 主张判断：2020统计时点、2021发布日期及初步汇总边界；泉州人数8782285、增量653755、份额22.03至21.14、女性47.78、性别比109.31及不含金门马祖相符。
- 核查者：独立校读分组B（原通读核查，父校对员据记录汇编）。

## S06-03 · 已核相关段落
- 原 URL：https://tjj.fujian.gov.cn/tongjinianjian/rk2020/html/fu0202.pdf
- 引用位置：第 6.1, 6.2 节；基线行 56, 107。
- 已核位置：PDF第1—4页（印刷2887—2890），表2-1／2-2及注1—3。
- 主张判断：年鉴PDF与网页统计数字和表头一致；表2-1的2010列是比重而非2010人数。
- 核查者：独立校读分组A。

## S06-04 · 已核相关段落
- 原 URL：https://aclanthology.org/2020.emnlp-main.550/
- 引用位置：第 6.1 节；基线行 58。
- 已核位置：ACL论文页面Abstract与书目信息。
- 主张判断：2020年论文及双编码器稠密段落检索摘要相符。
- 核查者：独立校读分组A。

## S06-05 · 已核相关段落
- 原 URL：https://aclanthology.org/2020.emnlp-main.550.pdf
- 引用位置：第 6.1 节；基线行 58。
- 已核位置：§3.1，印刷6770—6771，公式1。
- 主张判断：问题与段落分别编码；以内积比较向量，段落可预先编码。
- 核查者：独立校读分组A。

## S06-06 · 已核相关段落
- 原 URL：https://arxiv.org/html/2005.11401v4
- 引用位置：第 6.1 节；基线行 60。
- 已核位置：§2.1 RAG-Sequence／§2.2 Retriever／§2.4 Training。
- 主张判断：原论文有检索加生成、top-k边缘化与联合微调；不能把所有RAG都定义为不更新参数。
- 核查者：独立校读分组B（原通读核查，父校对员据记录汇编）。

## S06-07 · 已核相关段落
- 原 URL：https://arxiv.org/html/2005.14165v4
- 引用位置：第 6.1 节；基线行 62。
- 已核位置：Abstract及§1对few-shot/in-context learning的说明。
- 主张判断：文中few-shot以文字示范和交互指定任务，不在该任务适配中更新梯度。
- 核查者：独立校读分组A。

## S06-08 · 已核相关段落
- 原 URL：https://learn.microsoft.com/en-us/azure/search/vector-search-how-to-chunk-documents
- 引用位置：第 6.2 节；基线行 105。
- 已核位置：Common chunking patterns／Content overlap considerations。
- 主张判断：固定、结构与语义切块以及重叠的连贯性／成本权衡相符。
- 核查者：独立校读分组A。

## S06-09 · 已核相关段落
- 原 URL：https://huggingface.co/docs/transformers/main/tokenizer_summary
- 引用位置：第 6.2 节；基线行 109。
- 已核位置：Subword tokenization／SentencePiece。
- 主张判断：子词词元并不等于汉字数，中文等无空格文本仍须由各模型词元器处理。
- 核查者：独立校读分组A。

## S06-10 · 已核相关段落
- 原 URL：https://aclanthology.org/D19-1410.pdf
- 引用位置：第 6.3 节；基线行 149。
- 已核位置：§3 Model，印刷3984。
- 主张判断：SBERT把输出汇聚成定长句向量；CLS、平均与最大汇聚均为论文比较项。
- 核查者：独立校读分组A。

## S06-11 · 已核相关段落
- 原 URL：https://sbert.net/examples/sentence_transformer/applications/semantic-search/README.html
- 引用位置：第 6.3 节；基线行 151。
- 已核位置：Background／Symmetric vs. Asymmetric Semantic Search／Manual Implementation。
- 主张判断：问题与长段落是非对称检索；查询和语料进入同一向量空间比较。
- 核查者：独立校读分组A。

## S06-12 · 已核相关段落
- 原 URL：https://huggingface.co/BAAI/bge-small-zh-v1.5
- 引用位置：第 6.3 节；基线行 155。
- 已核位置：Model List及脚注1／Usage。
- 主张判断：bge-small-zh-v1.5为中文型号，检索查询指令见型号表；正文不加同一查询指令。
- 核查者：独立校读分组A。

## S06-13 · 已核相关段落
- 原 URL：https://huggingface.co/BAAI/bge-small-zh-v1.5/raw/main/config.json
- 引用位置：第 6.3 节；基线行 155。
- 已核位置：config.json：hidden_size、max_position_embeddings。
- 主张判断：隐藏向量维度512，位置上限512；与正文型号表相符。
- 核查者：独立校读分组A。

## S06-14 · 已核相关段落
- 原 URL：https://huggingface.co/BAAI/bge-small-zh-v1.5/blob/main/sentence_bert_config.json
- 引用位置：第 6.3 节；基线行 155。
- 已核位置：sentence_bert_config.json：max_seq_length。
- 主张判断：句向量封装的最大序列长度512。
- 核查者：独立校读分组A。

## S06-15 · 已核相关段落
- 原 URL：https://huggingface.co/BAAI/bge-small-zh-v1.5/blob/main/1_Pooling/config.json
- 引用位置：第 6.3 节；基线行 155。
- 已核位置：1_Pooling/config.json。
- 主张判断：word_embedding_dimension=512，CLS汇聚为true、均值与最大汇聚为false。
- 核查者：独立校读分组A。

## S06-16 · 已核相关段落
- 原 URL：https://huggingface.co/intfloat/multilingual-e5-small/raw/main/README.md
- 引用位置：第 6.3 节；基线行 157。
- 已核位置：模型概要／Usage／Supported Languages／Limitations。
- 主张判断：e5-small向量384维；query:/passage:前缀适用于非英语；attention_mask均值汇聚、L2归一化、512截断；100种语言并不保证低资源语表现相同。
- 核查者：独立校读分组A。

## S06-17 · 已核相关段落
- 原 URL：https://github.com/facebookresearch/faiss/wiki/MetricType-and-distances
- 引用位置：第 6.3 节；基线行 159。
- 已核位置：How can I index vectors for cosine similarity?。
- 主张判断：查询和语料均归一化后，最大内积排序等价于余弦排序。
- 核查者：独立校读分组A。

## S06-18 · 已核相关段落
- 原 URL：https://sbert.net/docs/package_reference/sentence_transformer/model.html
- 引用位置：第 6.3 节；基线行 161。
- 已核位置：构造函数local_files_only/token；encode的prompt、convert_to_numpy、normalize_embeddings；tokenizer属性。
- 主张判断：限定本地读取、认证token、前缀、归一化与数组返回的参数含义相符；tokenizer属性仍可获取所用词元器。
- 核查者：独立校读分组A。

## S06-19 · 已核相关段落
- 原 URL：https://huggingface.co/docs/transformers/main_classes/tokenizer
- 引用位置：第 6.3 节；基线行 163。
- 已核位置：__call__参数表及Returns: BatchEncoding。
- 主张判断：特殊词元、截断、补齐分开控制；input_ids是模型输入的词元ID而非字符位置。
- 核查者：独立校读分组A。

## S06-20 · 已核相关段落
- 原 URL：https://www.elastic.co/docs/solutions/search/full-text/how-full-text-works
- 引用位置：第 6.4 节；基线行 259。
- 已核位置：开头Text analysis／Inverted index creation／Relevance scoring。
- 主张判断：倒排索引由词项指向文档；BM25使用词频、文档频率和长度。
- 核查者：独立校读分组A。

## S06-21 · 已核相关段落
- 原 URL：https://nlp.stanford.edu/IR-book/html/htmledition/tokenization-1.html
- 引用位置：第 6.4 节；基线行 263。
- 已核位置：§2.2.1：定义、O’Neill例后查询处理段、中文分词末段（同URL索引正文）。
- 主张判断：查询和文档须一致词元化；中文词界存在歧义，词项不应机械等于逐字。
- 核查者：独立校读分组A。
- 获取情况：原URL直接open两次超时；站内精准搜索返回同URL完整相关段落，已核其索引正文。
- 限界：未声称本次成功直连实时页；来源是该原URL的索引正文，不是第三方转述。

## S06-22 · 已核相关段落
- 原 URL：https://lucene.apache.org/__root/docs.lucene.apache.org/core/9_12_0/core/org/apache/lucene/search/similarities/BM25Similarity.html
- 引用位置：第 6.4 节；基线行 265。
- 已核位置：BM25Similarity构造函数、idf、avgFieldLength。
- 主张判断：默认k1=1.2、b=.75；Lucene的带1对数idf及平均长度说明相符。
- 核查者：独立校读分组B（原通读核查，父校对员据记录汇编）。

## S06-23 · 访问阻塞
- 原 URL：https://www.staff.city.ac.uk/~sbrp622/papers/foundations_bm25_review.pdf
- 引用位置：第 6.4 节；基线行 267。
- 已核位置：未取得作者原PDF。
- 主张判断：待核原论文§3.1公式3.3、§3.4.5—3.5.1及分子k1+1变体；不能把Lucene接口页等同原论文该页已核。
- 核查者：独立校读分组A。
- 获取情况：HTTPS两次及HTTP转HTTPS一次均Timeout fetching；精准搜索未返回原论文可核正文。
- 限界：该原论文所引页与公式本轮未独立核到；不据访问失败认定正文错误。

## S06-24 · 已核相关段落
- 原 URL：https://learn.microsoft.com/en-us/azure/search/hybrid-search-overview
- 引用位置：第 6.4 节；基线行 269。
- 已核位置：Why use hybrid search?／How does hybrid search work?。
- 主张判断：精确人名数字等可受益于关键词；向量匹配概念相关材料；并行结果用RRF融合。
- 核查者：独立校读分组A。

## S06-25 · 已核相关段落
- 原 URL：https://learn.microsoft.com/en-us/azure/search/vector-search-filters
- 引用位置：第 6.5 节；基线行 358。
- 已核位置：How filtering works／Set the filter mode。
- 主张判断：后过滤与先取全库top-k后过滤均有漏掉范围内候选的风险；筛选字段来自非向量元数据。
- 核查者：独立校读分组A。

## S06-26 · 已核相关段落
- 原 URL：https://www.elastic.co/docs/reference/elasticsearch/rest-apis/reciprocal-rank-fusion
- 引用位置：第 6.5 节；基线行 360。
- 已核位置：开头公式／rank_constant／rank_window_size。
- 主张判断：RRF按各榜名次加1/(常数+名次)，未入榜贡献0；名次自1、默认常数60；窗口可截断。
- 核查者：独立校读分组A。

## S06-27 · 已核相关段落
- 原 URL：https://plg.uwaterloo.ca/~gvcormac/cormacksigir09-rrf.pdf
- 引用位置：第 6.5 节；基线行 362。
- 已核位置：§1公式及k=60说明。
- 主张判断：原RRF公式与本书教学融合式相符，常数60不是取前60条的k。
- 核查者：独立校读分组B（原通读核查，父校对员据记录汇编）。

## S06-28 · 已核相关段落
- 原 URL：https://learn.microsoft.com/en-us/azure/search/hybrid-search-ranking
- 引用位置：第 6.5 节；基线行 364。
- 已核位置：How RRF ranking works／Scores in hybrid search results。
- 主张判断：融合常数与近邻数不同；BM25、向量、RRF计分尺度不同，不能直接当同一概率。
- 核查者：独立校读分组A。

## S06-29 · 已核相关段落
- 原 URL：https://www.elastic.co/docs/reference/elasticsearch/rest-apis/search-rank-eval
- 引用位置：第 6.5, 6.8 节；基线行 366, 617。
- 已核位置：Precision at K／Recall at K／Mean reciprocal rank。
- 主张判断：三种指标分别关注前k相关比例、全部相关召回和首个相关位置；本书短返回、重复证据和零相关约定另行明示。
- 核查者：独立校读分组B（原通读核查，父校对员据记录汇编）。

## S06-30 · 已核相关段落
- 原 URL：https://learn.microsoft.com/en-us/azure/search/semantic-how-to-query-rewrite
- 引用位置：第 6.6 节；基线行 452。
- 已核位置：开头、精确词项警示、Test query rewrites with debug。
- 主张判断：保留原问并共同检索；改写可能丢失精确词；debug可查看改写，须评估是否保持任务含义。
- 核查者：独立校读分组A。

## S06-31 · 已核相关段落
- 原 URL：https://whc.unesco.org/en/list/1561/
- 引用位置：第 6.6 节；基线行 456。
- 已核位置：英文Description末句。
- 主张判断：Zayton的历史用法限于10—14世纪阿拉伯与西方文本，不等同现代地域范围。
- 核查者：独立校读分组B（原通读核查，父校对员据记录汇编）。

## S06-32 · 已核相关段落
- 原 URL：https://aclanthology.org/2023.emnlp-main.322.pdf
- 引用位置：第 6.6 节；基线行 458。
- 已核位置：§3.1，印刷5306；§6.2—6.3，5310—5311。
- 主张判断：重写—检索—阅读流程；案例和检索指标表明命中改善与回答改善需分别看，改写可产生错误理解。
- 核查者：独立校读分组A。

## S06-33 · 已核相关段落
- 原 URL：https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- 引用位置：第 6.7 节；基线行 534。
- 已核位置：Be clear and direct／Structure prompts with XML tags。
- 主张判断：明确输出要求、分开指令/上下文/输入的建议确有依据；不代表本书人工拟答由模型产生。
- 核查者：独立校读分组A。

## S06-34 · 已核相关段落
- 原 URL：https://aclanthology.org/2023.emnlp-main.398.pdf
- 引用位置：第 6.7, 6.8 节；基线行 536, 619。
- 已核位置：§3.2—3.3，印刷6467—6469。
- 主张判断：回答正确与覆盖、引文支持覆盖和无关引文分开评价；引用数量不能替代支持关系。
- 核查者：独立校读分组A。

## S06-35 · 已核相关段落
- 原 URL：https://nlp.stanford.edu/IR-book/html/htmledition/information-retrieval-system-evaluation-1.html
- 引用位置：第 6.8 节；基线行 613。
- 已核位置：§8.1全节（同URL索引正文）。
- 主张判断：测试集合含文档、信息需要及相关性判断；按信息需要判定而非机械同词；开发集调参后在独立测试集评价。
- 核查者：独立校读分组A。
- 获取情况：原URL直接open两次超时；站内精准搜索返回同URL完整相关段落，已核其索引正文。
- 限界：未声称本次成功直连实时页；来源是该原URL的索引正文，不是第三方转述。

## S06-36 · 已核相关段落
- 原 URL：https://nlp.stanford.edu/IR-book/html/htmledition/assessing-relevance-1.html
- 引用位置：第 6.8 节；基线行 615。
- 已核位置：§8.5第1—3段及分歧讨论（同URL索引正文）。
- 主张判断：小型集合可穷尽判定，较大集合用pooling；评阅者有分歧，需记录和核对。
- 核查者：独立校读分组A。
- 获取情况：原URL直接open两次超时；站内精准搜索返回同URL完整相关段落，已核其索引正文。
- 限界：未声称本次成功直连实时页；来源是该原URL的索引正文，不是第三方转述。

## S06-37 · 已核相关段落
- 原 URL：https://nlp.stanford.edu/IR-book/html/htmledition/critiques-and-justifications-of-the-concept-of-relevance-1.html
- 引用位置：第 6.8 节；基线行 615。
- 已核位置：§8.5.1：marginal relevance段（同URL索引正文）。
- 主张判断：高度相关但重复的信息可能无新增效用；不同事实可作评价单位，不等于史学上多个独立来源。
- 核查者：独立校读分组A。
- 获取情况：原URL直接open两次超时；站内精准搜索返回同URL完整相关段落，已核其索引正文。
- 限界：未声称本次成功直连实时页；来源是该原URL的索引正文，不是第三方转述。

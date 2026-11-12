# RAG贯通教材配套

本版新制教材配套。真实来源的整理值、教学设例、空白模板分开标记。代码状态 NOT_RUN，未作本轮学术复算或语言校对；文件结构检查不代表计算结果通过。

## 本包是什么

真实公报数字按已有正文承接，来源见 [source_register.json](source_register.json)。十一行表格是从已有章节表格新制的教学转写，不是原公报保存件。D1—D4为本版统一语料；A—C用于编码示范，A对应D2、B对应D1、C对应D4。D3为性别构成干扰材料。所有新代码未运行。

## 不安装也能阅读

先读[表格输入](table_input.json)、[统一语料](corpus.json)、[查询计划](query_plan.json)、[完整提示](prompt.md)和[拟答核对](answer_review.md)。可手工比较哪些块保住了表头、哪一条直接回答问题。不得将题录、整理或模型回答升级为古代原件。

## 已有Python时的顺序

在本目录执行，默认只输出终端，不修改输入：

```bash
python -B chunk_NOT_RUN.py
python -B bm25_NOT_RUN.py --query "泉州 人口 增加"
python -B bm25_NOT_RUN.py --queries query_plan.json
python -B rrf_NOT_RUN.py
python -B evaluate_NOT_RUN.py --split development
python -B evaluate_NOT_RUN.py --split holdout_exercise
```

- 分块脚本比较120无重叠、120重叠30、结构600和固定600；用字符而非token计数。
- BM25使用手工词项、正值IDF、k1=1.2、b=0.75；输出各词贡献，空候选保留状态。
- RRF默认读[教学榜单](rrf_teaching_input.json)。实际两路榜单填入[模板](rankings_template.json)后，使用 `--input 文件名.json`，不得把教学分数当模型结果。
- 评价脚本读取[五题练习](evaluation_input.json)，分开可答题与当前语料无答案题；题目已公开，不能声称独立盲测。

## 真实编码的可选入口

只有已经具备sentence-transformers及本地模型缓存时，才执行编码程序；本包不安装依赖、不下载模型。

```bash
python -B embedding_compare_NOT_RUN.py --model /读者自己的本地模型目录 --family e5 --input model_input.json
python -B embedding_compare_NOT_RUN.py --model /读者自己的本地模型目录 --family bge --input corpus.json
```

模型目录必须实际存在；记录自己采用的模型修订版本。脚本保留最终字符串、token数、维度、归一化向量与排名；超过配置上限即停止，不静默截断。两套模型分别执行，不能混合向量。不要把示例路径写成已经取得的模型。

## 结果记录

[结果模板](results_template.csv)与[查询阅读表](query_review_template.csv)的实际结果栏留空。正文旧分值的身份见[继承数值说明](inherited_numeric_records.md)；新语料和旧输入不完全相同，不要求精确重现旧排序。读者实际运行后另存新文件、命令、输入版本、时间和人工判断。

## 能验收什么

能够打开文件、识别来源与整理身份、按命令产生真实结果，并解释错误发生在材料、块、查询还是回答，才完成本练习。脚本的成功不能证明史料真实、解释充分或模型适合全部文史材料。复杂依赖不可用时，保留未运行，先完成手工比较即可。

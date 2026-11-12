# 配套代码云端执行审计（2026-11-12）

范围：主线 `manuscript/附件/` 的26个Python程序，以及其现有公开教学输入。Python 3.12.14；只使用已有环境，没有安装依赖、下载模型或调用外部API。本次得到用户单独授权开展教学代码检查；正式史料复算与独立学术校对继续暂停。

## 结果不能只看退出码

完成97次原始程序入口调用：50次第7—11章、32次第12—17章、15次其余章节。3次预期拒绝是重复/缺失ID及禁止覆盖；2次依赖阻塞是本地Embedding模型缺失与Optuna缺包。其余92次退出0，但其中models.py的拟合子任务仍有9次失败，不能写成全部模型通过。

按文件：23个获得有限教学执行覆盖，models.py部分执行，2个缺必要环境未完成实际算法执行。所有26个通过Python语法解析。这里没有全分支覆盖率、性能保证或全书研究验收率。

- Embedding：只验证“缺本地模型立即停止”的保护路径；未产生嵌入向量，未下载模型。实际执行还需已获准的本地模型及sentence-transformers环境。
- models.py：last、seasonal各3次拟合成功；ARIMA/SARIMA/Holt-Winters共9次因statsmodels缺失失败。已选seasonal基线的test路径完成，不代表其余模型完成。
- Optuna：缺包，生成failure记录，未进行Optuna搜索。
- 第20章：原程序读取继承的公开人口数值。本次特意在临时副本改用100/120、1000/1200的合成CSV，只验算术功能，**未复算正文人口结果**。
- 第5、19、21—23章为结构检查；第6章为教材检索/切分/融合练习。真实来源文字的存在不等于来源内容已经重新核读。
- 第7—17章本次使用人工教学输入，不将人工样本性能视为真实历史预测能力。

## 逐文件覆盖

|主线程序|本次状态|执行证据|
|---|---|---|
|`manuscript/附件/ch05/check_links_NOT_RUN.py`|有限教学执行|[逐次命令与结果](../chapters/_shared/results/2026-11-12/small_program_runs.json)|
|`manuscript/附件/ch06/bm25_NOT_RUN.py`|有限教学执行|[逐次命令与结果](../chapters/_shared/results/2026-11-12/small_program_runs.json)|
|`manuscript/附件/ch06/chunk_NOT_RUN.py`|有限教学执行|[逐次命令与结果](../chapters/_shared/results/2026-11-12/small_program_runs.json)|
|`manuscript/附件/ch06/embedding_compare_NOT_RUN.py`|实际算法未运行；缺环境|[逐次命令与结果](../chapters/_shared/results/2026-11-12/small_program_runs.json)|
|`manuscript/附件/ch06/evaluate_NOT_RUN.py`|有限教学执行|[逐次命令与结果](../chapters/_shared/results/2026-11-12/small_program_runs.json)|
|`manuscript/附件/ch06/rrf_NOT_RUN.py`|有限教学执行|[逐次命令与结果](../chapters/_shared/results/2026-11-12/small_program_runs.json)|
|`manuscript/附件/ch07/workbook.py`|有限教学执行|[逐次命令与结果](../chapters/_shared/results/2026-11-12/workbook_runs.json)|
|`manuscript/附件/ch08/8.8/score_predictions.py`|有限教学执行|[逐次命令与结果](../chapters/_shared/results/2026-11-12/workbook_runs.json)|
|`manuscript/附件/ch08/workbook.py`|有限教学执行|[逐次命令与结果](../chapters/_shared/results/2026-11-12/workbook_runs.json)|
|`manuscript/附件/ch09/workbook.py`|有限教学执行|[逐次命令与结果](../chapters/_shared/results/2026-11-12/workbook_runs.json)|
|`manuscript/附件/ch10/workbook.py`|有限教学执行|[逐次命令与结果](../chapters/_shared/results/2026-11-12/workbook_runs.json)|
|`manuscript/附件/ch11/workbook.py`|有限教学执行|[逐次命令与结果](../chapters/_shared/results/2026-11-12/workbook_runs.json)|
|`manuscript/附件/ch12/preprocess_annual.py`|有限教学执行|[逐次命令与结果](../chapters/_shared/results/2026-11-12/pipeline_runs.json)|
|`manuscript/附件/ch13/chapter12_adapter.py`|有限教学执行|[逐次命令与结果](../chapters/_shared/results/2026-11-12/pipeline_runs.json)|
|`manuscript/附件/ch13/models.py`|部分执行；子模型缺依赖|[逐次命令与结果](../chapters/_shared/results/2026-11-12/pipeline_runs.json)|
|`manuscript/附件/ch13/optuna_search.py`|实际算法未运行；缺环境|[逐次命令与结果](../chapters/_shared/results/2026-11-12/pipeline_runs.json)|
|`manuscript/附件/ch13/workflow.py`|有限教学执行|[逐次命令与结果](../chapters/_shared/results/2026-11-12/pipeline_runs.json)|
|`manuscript/附件/ch14/workflow.py`|有限教学执行|[逐次命令与结果](../chapters/_shared/results/2026-11-12/pipeline_runs.json)|
|`manuscript/附件/ch15/workflow.py`|有限教学执行|[逐次命令与结果](../chapters/_shared/results/2026-11-12/pipeline_runs.json)|
|`manuscript/附件/ch16/relations.py`|有限教学执行|[逐次命令与结果](../chapters/_shared/results/2026-11-12/pipeline_runs.json)|
|`manuscript/附件/ch17/network_analysis.py`|有限教学执行|[逐次命令与结果](../chapters/_shared/results/2026-11-12/pipeline_runs.json)|
|`manuscript/附件/ch19/check_catalog_NOT_RUN.py`|有限教学执行|[逐次命令与结果](../chapters/_shared/results/2026-11-12/small_program_runs.json)|
|`manuscript/附件/ch20/calculate_population_NOT_RUN.py`|有限教学执行|[逐次命令与结果](../chapters/_shared/results/2026-11-12/small_program_runs.json)|
|`manuscript/附件/ch21/check_response_NOT_RUN.py`|有限教学执行|[逐次命令与结果](../chapters/_shared/results/2026-11-12/small_program_runs.json)|
|`manuscript/附件/ch22/inspect_question_cards_NOT_RUN.py`|有限教学执行|[逐次命令与结果](../chapters/_shared/results/2026-11-12/small_program_runs.json)|
|`manuscript/附件/ch23/inspect_source_chain_NOT_RUN.py`|有限教学执行|[逐次命令与结果](../chapters/_shared/results/2026-11-12/small_program_runs.json)|

## 已确认缺陷与修补

原附件不覆盖，修正版置于活代码层；原NOT_RUN文件名/历史状态保留，其本次执行情况由本报告覆盖登记。

|问题|复现与影响|修正版|
|---|---|---|
|第8章评分先int转换|0.9/1.9被截成0/1，错误输入仍报全对|[score_predictions.py](../chapters/ch08/code/score_predictions.py)：仅允许整数0/1或CSV精确字符串，拒绝浮点和bool|
|第14章决定替代关系未验证|自引、循环、跨mention替代均被接受，可静默抹除另一对象确认|[workflow.py](../chapters/ch14/code/workflow.py)：先检查目标、同mention、自引、环，再形成superseded集合|
|第22章空字段用str判断|None、空列表、空字典被当作完整文字|[inspect_question_cards.py](../chapters/ch22/code/inspect_question_cards.py)：按现有文本字段schema校验，增加显式输入参数|

[标准库回归测试](../chapters/_shared/test_promoted.py)的6个测试方法通过，包含合法输入、7种评分错误类型、7种卡片值、合法替代和4种非法替代。运行：

```bash
python -B chapters/_shared/test_promoted.py
python -B chapters/ch22/code/inspect_question_cards.py --input manuscript/附件/ch22/question_cards.json
python -B chapters/ch08/code/score_predictions.py --predictions YOUR_NEW_PREDICTIONS.json --reference manuscript/附件/ch08/8.8/reference.csv
python -B chapters/ch14/code/workflow.py --section 1 --input manuscript/附件/ch14/14.1/input.json --out NEW_OUTPUT_DIRECTORY
```

后两项必须自己提供预测输入或新的输出目录；不覆盖已有文件。三份修正版只需Python标准库，不新增依赖配置。第14章的修补不声称完成GIS、所有边界输入或所有历史实体消歧的验证。

## 输入、输出及章节对应

[程序清单](../chapters/_shared/results/2026-11-12/program_inventory.json)保存源文件SHA与所属章；各组运行记录保存实际命令、退出状态及输入/输出线索。[流水线输出清单](../chapters/_shared/results/2026-11-12/pipeline_output_inventory.json)登记200件实际生成文件的大小与SHA，不把文件数量当成功率。第12—17章各保留一组代表性输出JSON封装，其CSV保留原文本；不重复发布所有情境的同类结果。

日志中的`SANDBOX/`表示临时运行副本，不是仓库路径。输入可由 `manuscript/附件/` 中对应章取得；第20章的替换数据另存 [synthetic_ch20_inputs.json](../chapters/_shared/results/2026-11-12/synthetic_ch20_inputs.json)。第12章预处理结果实际接入第13章adapter，缺失和零值的12项断言通过，3项已有目录拒绝覆盖检查通过。第16章关系整理和第17章网络示例都运行，但两章并非自动共享统一schema，不宣称已实现跨章自动导入。

## 尚未完成及使用限制

97次调用不是97项学术检验。没有全量证明测试覆盖、没有安装缺少的依赖、没有真实模型检索、没有执行历史版本里的程序，也没有独立复核正文叙述与所有计算数字。原附件里已知缺陷仍留作教材版本，实际使用上述三个功能请优先选择活代码层修正版。

对失败输出，必须查看manifest和failure记录，不以输出目录存在判成功。改用正式史料、恢复全书复算、补装依赖或更换模型须另行安排。本报告不解除这些边界。

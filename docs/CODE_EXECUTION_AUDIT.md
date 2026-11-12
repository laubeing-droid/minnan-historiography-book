# 配套代码云端执行审计（2026-11-12）

## 当前使用结论

读者先看[配套程序怎么跑](RUNNING_EXAMPLES.md)，再按本页追查执行记录。当前有25个原程序的有限教学执行覆盖；原 BGE/E5 嵌入程序未实际运行，指定 Google EmbeddingGemma 2 另由活代码适配器完成小样本执行。第13章 statsmodels/Optuna 的初次缺依赖已通过后续补跑解决，不能继续报成当前阻塞。

第8、14、22章应使用下文所列修正版。原始入口共100次调用的统计不包含修补回归或Gemma适配器，不是研究完成率。以下按阶段保留过程，旧失败不删除，成功也不扩大成全书复算完成。

## 第6章后续：Google EmbeddingGemma 2实际执行

用户进一步指定谷歌EmbeddingGemma 2。已核[官方模型卡](https://huggingface.co/google/embeddinggemma-2)及[Google开发指南](https://developers.googleblog.com/en/embeddinggemma-2-the-developer-guide/)，实际模型ID为`google/embeddinggemma-2`，不是Gemma2生成模型。官方API确认公开、非gated，Apache-2.0；本轮未登录账号或绕过访问限制。

在独立云端环境安装sentence-transformers/transformers及CPU PyTorch，固定模型revision `f9972ac22e696a105c482202646979e33e4b5a1e` 下载官方safetensors。只启用文本编码，以float32执行；模型文件不加入本仓库，文件大小与SHA见[下载清单](../chapters/_shared/results/2026-11-12/embeddinggemma2/model_download_manifest.json)。统一processor加载仍要求Pillow及CPU torchvision，两次缺依赖失败后补装成功；这不是运行视觉或音视频任务。完整依赖和过程见[环境记录](../chapters/_shared/results/2026-11-12/embeddinggemma2/environment.json)。

原附件只支持BGE/E5，不能把Gemma硬套入其提示词。新增[本地专用适配器](../chapters/ch06/code/embeddinggemma2_compare.py)，采用模型自带的SearchQuery/Document检索提示，禁止远程代码，推理时强制本地离线；检查长度、输出形状、有限值和单位范数。现有1条查询与3段教材材料产生4×768向量，输入分别25/89/108/78 token，均未截断，全部范数为1。实际排序为B>A>C，分数约0.858、0.843、0.659；这里只展示相似度，不证明B比A更可靠、更独立或足以回答历史问题。

[真实输入、向量和排序](../chapters/_shared/results/2026-11-12/embeddinggemma2/retrieval_result.json)已保存。运行命令（使用自行准备的官方本地快照，不自动下载）：

```bash
python -B chapters/ch06/code/embeddinggemma2_compare.py --model LOCAL_MODEL_DIRECTORY --input manuscript/附件/ch06/model_input.json --revision f9972ac22e696a105c482202646979e33e4b5a1e
```

因此第6章嵌入功能现已有指定Gemma模型的实跑结果，但**原BGE/E5算法分支仍未运行**，不写成“26个原程序全部通过”。全书教学功能的有限检查、具体模型的小样本演示与正式史料复算是不同事项；正式复算和独立学术校对仍暂停。

## 第13章补跑阶段（在Gemma阶段之前）

初次审计后，用户明确授权仅在云端安装statsmodels、optuna及必要依赖。已在独立虚拟环境从PyPI安装，`pip check`通过；statsmodels 0.15.0、optuna 5.0.0，完整版本见[环境记录](../chapters/_shared/results/2026-11-12/ch13_after_install/environment.json)。这一阶段没有安装到用户电脑，也尚未安装Embedding框架或下载模型；后者随后按上节记录完成。

新增3次CLI：模型验证15/15拟合成功（last、seasonal、ARIMA、SARIMA、Holt-Winters各3次）；验证选择Holt-Winters，锁定后测试4/4拟合成功；Optuna的8/8 trial完成，选C1，**没有评估其最终测试集**。只运行现有合成教学序列，拟合成功不等于适用于闽南历史序列。

实际命令与完整结果：[补跑记录](../chapters/_shared/results/2026-11-12/ch13_after_install/runs.json)、[验证输出](../chapters/_shared/results/2026-11-12/ch13_after_install/models_validation.json)、[测试输出](../chapters/_shared/results/2026-11-12/ch13_after_install/models_test.json)、[搜参输出](../chapters/_shared/results/2026-11-12/ch13_after_install/optuna_validation.json)。补跑后主线26个程序中25个获得有限教学执行覆盖，当时仅Embedding仍缺框架和模型；随后Gemma适配器另行实跑，原BGE/E5仍未跑。合计100次原始入口调用，不包括修补回归测试。

下文保留初次审计事实：其中“缺statsmodels/Optuna”“未安装”等是**补跑前快照**，不能读成当前阻塞。旧失败记录不覆写。

## 初次审计快照

范围：主线 `manuscript/附件/` 的26个Python程序，以及其现有公开教学输入。Python 3.12.14；只使用已有环境，没有安装依赖、下载模型或调用外部API。本次得到用户单独授权开展教学代码检查；正式史料复算与独立学术校对继续暂停。

### 结果不能只看退出码

完成97次原始程序入口调用：50次第7—11章、32次第12—17章、15次其余章节。3次预期拒绝是重复/缺失ID及禁止覆盖；2次依赖阻塞是本地Embedding模型缺失与Optuna缺包。其余92次退出0，但其中models.py的拟合子任务仍有9次失败，不能写成全部模型通过。

按文件：23个获得有限教学执行覆盖，models.py部分执行，2个缺必要环境未完成实际算法执行。所有26个通过Python语法解析。这里没有全分支覆盖率、性能保证或全书研究验收率。

- Embedding：只验证“缺本地模型立即停止”的保护路径；未产生嵌入向量，未下载模型。实际执行还需已获准的本地模型及sentence-transformers环境。
- models.py：last、seasonal各3次拟合成功；ARIMA/SARIMA/Holt-Winters共9次因statsmodels缺失失败。已选seasonal基线的test路径完成，不代表其余模型完成。
- Optuna：缺包，生成failure记录，未进行Optuna搜索。
- 第20章：原程序读取继承的公开人口数值。本次特意在临时副本改用100/120、1000/1200的合成CSV，只验算术功能，**未复算正文人口结果**。
- 第5、19、21—23章为结构检查；第6章为教材检索/切分/融合练习。真实来源文字的存在不等于来源内容已经重新核读。
- 第7—17章本次使用人工教学输入，不将人工样本性能视为真实历史预测能力。

### 逐文件覆盖

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

### 已确认缺陷与修补

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

### 输入、输出及章节对应

[程序清单](../chapters/_shared/results/2026-11-12/program_inventory.json)保存源文件SHA与所属章；各组运行记录保存实际命令、退出状态及输入/输出线索。[流水线输出清单](../chapters/_shared/results/2026-11-12/pipeline_output_inventory.json)登记200件实际生成文件的大小与SHA，不把文件数量当成功率。第12—17章各保留一组代表性输出JSON封装，其CSV保留原文本；不重复发布所有情境的同类结果。

日志中的`SANDBOX/`表示临时运行副本，不是仓库路径。输入可由 `manuscript/附件/` 中对应章取得；第20章的替换数据另存 [synthetic_ch20_inputs.json](../chapters/_shared/results/2026-11-12/synthetic_ch20_inputs.json)。第12章预处理结果实际接入第13章adapter，缺失和零值的12项断言通过，3项已有目录拒绝覆盖检查通过。第16章关系整理和第17章网络示例都运行，但两章并非自动共享统一schema，不宣称已实现跨章自动导入。

### 尚未完成及使用限制

97次调用不是97项学术检验。没有全量证明测试覆盖、没有安装缺少的依赖、没有真实模型检索、没有执行历史版本里的程序，也没有独立复核正文叙述与所有计算数字。原附件里已知缺陷仍留作教材版本，实际使用上述三个功能请优先选择活代码层修正版。

对失败输出，必须查看manifest和failure记录，不以输出目录存在判成功。改用正式史料、恢复全书复算、补装依赖或更换模型须另行安排。本报告不解除这些边界。

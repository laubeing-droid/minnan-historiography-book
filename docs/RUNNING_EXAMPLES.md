# 配套程序怎么跑

这份说明对应《一种闽南文史的未来：基于人工智能与现代研究方法》。先用仓库给出的教学输入走通步骤，再考虑换成自己的史料。下面的例子演示怎样处理材料，不替你判断材料是否可靠，也不把程序结果直接当成历史结论。

## 先选对版本

原附件保留在 `manuscript/附件/`，文件名里的 `NOT_RUN` 是保存下来的编写状态；2026-11-12 的另行运行记录见[执行审计](CODE_EXECUTION_AUDIT.md)。第8章评分、第14章工作流、第22章问题卡检查已有修正版，实际使用请选 `chapters/ch08/code/score_predictions.py`、`chapters/ch14/code/workflow.py`、`chapters/ch22/code/inspect_question_cards.py`，不要继续使用已知有缺陷的旧入口。第6章指定的 Google 模型使用 `chapters/ch06/code/embeddinggemma2_compare.py`，不是原来的 BGE/E5 脚本。

下面命令在仓库根目录的 Bash 中执行。普通教学脚本使用 Python 3.10 或以上，已保存的云端记录使用 Python 3.12.14。先创建一个独立输出目录，每次重跑换一个新目录，避免覆盖旧结果：

```bash
RUN=$(mktemp -d)
printf '本次输出：%s\n' "$RUN"
```

Windows 可在 Git Bash 或 WSL 中使用这些命令。本文没有重新验证原生 PowerShell；如自行改写命令，仍须保证每个输出子目录尚不存在。模型依赖须另外准备，普通章节不需要为此安装整套机器学习环境。

## 第6章：先看检索，再看向量

先运行不需要模型的切分、BM25、融合和评估。脚本读取同目录的公开教学输入，结果打印到终端，不会自动写回材料：

```bash
(cd manuscript/附件/ch06 && python -B chunk_NOT_RUN.py)
(cd manuscript/附件/ch06 && python -B bm25_NOT_RUN.py --query "泉州 人口 增加")
(cd manuscript/附件/ch06 && python -B rrf_NOT_RUN.py)
(cd manuscript/附件/ch06 && python -B evaluate_NOT_RUN.py --split development)
```

检查返回的段落编号、排序及评估结果，而不只是看程序是否退出成功。查询和判定答案都已公开，这不是盲测。材料里的历史数字仍需回到所引来源核读。

已验证的向量路线是 Google EmbeddingGemma 2，模型 ID 为 `google/embeddinggemma-2`。它不是 Gemma2 生成模型。准备好官方本地快照后，把下面的 `LOCAL_MODEL_DIRECTORY` 换成实际目录：

```bash
python -B chapters/ch06/code/embeddinggemma2_compare.py --model LOCAL_MODEL_DIRECTORY --input manuscript/附件/ch06/model_input.json --revision f9972ac22e696a105c482202646979e33e4b5a1e
```

适配器只读本地模型，不自动下载。已运行环境的包版本见[环境记录](../chapters/_shared/results/2026-11-12/embeddinggemma2/environment.json)，不要把这一命令理解成安装命令。既有记录用1条查询、3段材料得到4个768维向量，排序为 B、A、C。输入、向量和得分见[结果](../chapters/_shared/results/2026-11-12/embeddinggemma2/retrieval_result.json)。这只说明这组输入的相似度排序，不能据此认定哪段史料更真实。旧 BGE/E5 路线仅留历史附件，不再作为当前入口或待补跑任务。本次调整没有重新下载或运行模型。

## 第12章：把缺页和真实零值分开

输入 `demo_annual_observations.csv` 是人工教学序列，不是港口史料。按1915年可见的信息准备训练数据：

```bash
python -B manuscript/附件/ch12/preprocess_annual.py --input manuscript/附件/ch12/data/demo_annual_observations.csv --output "$RUN/ch12" --series-id DEMO_PORT_A --origin 1915 --train-start 1900 --evaluation-end 1923 --impute none --scale none
```

应得到 `train_input.csv`、`evaluation_truth.csv`、`transform_params.json`、`run_manifest.json`。先看1903年无记录、1907年不可辨、1910—1911年材料缺失和1914年真实零值是否仍有区别，再看1918年的记录是否受到1920年才可获得这一条件限制。不要把空缺统一补成零。

需要交给第13章时，可运行已经提供的适配器：

```bash
python -B manuscript/附件/ch13/chapter12_adapter.py --input "$RUN/ch12/train_input.csv" --series-id DEMO_PORT_A --origin 1915 --out "$RUN/ch12_adapter"
```

它映射的是原始 `y`，不是填补后的 `input_y`，也不把评估真值混入训练。缺失值仍可能使后续严格模型拒绝运行，这是应当保留的信息。这个年度序列不能直接冒充下一节的四期季节教学序列。

## 第13章：验证选模型，测试只验选定模型

先做只需标准库的任务说明例子：

```bash
python -B manuscript/附件/ch13/workflow.py --section 1 --input manuscript/附件/ch13/13.1/input.json --out "$RUN/ch13_tasks"
```

完整模型例子使用本章 `teaching_series.csv` 和 `model_protocol.json`，都是教学设定。机器已有 statsmodels 时，按顺序运行：

```bash
python -B manuscript/附件/ch13/models.py --input manuscript/附件/ch13/teaching_series.csv --protocol manuscript/附件/ch13/model_protocol.json --out "$RUN/ch13_validation"
python -B manuscript/附件/ch13/models.py --input manuscript/附件/ch13/teaching_series.csv --protocol manuscript/附件/ch13/model_protocol.json --phase test --selection "$RUN/ch13_validation/selection.json" --out "$RUN/ch13_test"
python -B manuscript/附件/ch13/optuna_search.py --input manuscript/附件/ch13/13.9/input.json --out "$RUN/ch13_optuna"
```

最后一条另外需要 Optuna。已有成功记录使用 statsmodels 0.15.0、Optuna 5.0.0，完整环境见[补跑环境](../chapters/_shared/results/2026-11-12/ch13_after_install/environment.json)。若环境不同，先记录版本，不以“退出码为0”代替检查每次拟合的状态。

查看 `summary.csv`、`predictions.csv`、`selection.json` 和运行记录：既有验证阶段15次拟合成功，选出 Holt-Winters；锁定后测试阶段4次拟合成功。Optuna 的8次 trial完成，选择C1，但其最终测试集没有评估。不能把“模型测试已跑”套到所有搜参路径。已有输出见[验证](../chapters/_shared/results/2026-11-12/ch13_after_install/models_validation.json)、[测试](../chapters/_shared/results/2026-11-12/ch13_after_install/models_test.json)、[搜参](../chapters/_shared/results/2026-11-12/ch13_after_install/optuna_validation.json)。这些结果不证明模型适用于真实闽南历史序列。

## 第16章：从材料中的说法整理关系

输入是本章已提供的人工人物、组织、事件及判断表，不是补回的原始史料包。运行：

```bash
python -B manuscript/附件/ch16/relations.py --data manuscript/附件/ch16 --out "$RUN/ch16"
```

先读 `assertion_audit.csv`，看每条说法为何纳入或排除；再看 `confirmed_instances.csv`、`layer_edges.csv`、`projection.csv`，最后打开 `relations.svg`。同一次寄信被两份材料记载，不应计成两次事件；共同出席投影也不能直接解释成相识。来源链、同名判断与候选证据分别保留在 `lineage.json`、`disambiguation_audit.json`、`candidate_evidence.json`。

改变时间窗或待定身份会改变结果。可另建输出目录尝试 `--end-year 1709`，但“假定为同一人”的结果只是敏感性检查，不是身份已证实。本章各小节的编号空间并不全部相通，不能只因编号相同就拼接。

## 第17章：描述网络，不替历史作结论

本章使用A—H等人工节点，与第16章人物编号不是一套数据。先运行独立的网络例子：

```bash
python -B manuscript/附件/ch17/network_analysis.py --data manuscript/附件/ch17 --out "$RUN/ch17"
```

查看 `network_summary.json`、`centralities.csv`、`components.csv` 和 `network.svg`。既有结果保留孤立节点H，桥为C—D、F—G，割点为C、D、F。再看 `sensitivity.json`、`communities.csv`、`co_membership.csv`，了解筛选与参数改变是否影响描述。桥和割点说明删点删边后的结构变化，不证明历史上某人具有决定性影响。

这个程序用小图穷举划分，不适合直接塞进大规模人物网。通信转成无向边也只表示存在联系，不表示频次或强度。第16章到第17章已有[合成教学桥接](../chapters/ch16/README.md)：只接收已接受、已确认且年份明确的寄信关系，将共享事件和来源的重复提及合并，再复用第17章图指标。现有教材输入得到3个人物、1条边、1个孤立点，7项测试通过。这是教学数据的衔接，不是真实史料研究闭环；真实使用前仍须核对人物映射、关系类型、时间窗口及来源关系，不能直接拼两个章节的CSV。

## 怎样判断这一轮跑到了哪里

保存输入版本、命令、环境和输出，先检查失败记录，再解释数字。可与[原运行记录](../chapters/_shared/results/2026-11-12/pipeline_runs.json)及[输出文件清单](../chapters/_shared/results/2026-11-12/pipeline_output_inventory.json)对照。记录中的 `SANDBOX/` 是当时临时副本的位置，不是你应创建的仓库目录。

本次说明不改历史 `NOT_RUN`、不重写平行校订版，也不宣布全书正式复算或独立校对完成。它把已经走过的教学路径交给读者，同时说明哪些地方仍要另做判断和验证。

### 本次说明的命令复查

本次逐条重跑了第6章四个标准库入口、第12章预处理、第12→13章适配、第13章任务说明，以及第16、17章默认入口，共9条命令，均正常退出；结果只写入独立临时目录。模型拟合、Optuna及Gemma本次未重跑，上述成功数字来自链接中的既有记录。命令可执行检查不代替结果的独立学术复核。

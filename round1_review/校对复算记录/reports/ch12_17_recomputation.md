# 第 12—17 章独立复算与运行验收

日期：2026-10-30 UTC。只读基线：`book_completion_20261030/final`；本次修改仅在 `book_review_20261030/revision/附件/ch12..17`。运行证据集中于 `../runs/ch12_17/`。

## 获准安装后的追加验收（当前结论）

用户于 **2026-10-30 02:49:46 UTC** 明确允许本次云端安装 statsmodels 与 Optuna。已在 `runs/ch12_17/env_statsmodels_optuna` 新建 `venv --system-site-packages`，仅以官方 `https://pypi.org/simple` 和官方 `files.pythonhosted.org` 轮子源安装；不更改系统配置，不使用用户电脑。先dry-run保存计划，再约束实际版本安装。新增 **statsmodels 0.15.0、Optuna 5.0.0** 及11项正常依赖（完整版本见 `approved_dependency_constraints.txt`、`dependency_install.json`）；沿用现有NumPy/SciPy/pandas，`pip check`退出0。原解释器仍找不到statsmodels/Optuna，证明新增包限于隔离venv。

**此前依赖阻塞现已解除。** 原缺包失败记录及第一阶段报告完整保留；以下新增结果不是把旧日志改成PASS。当前所有提供实现的主程序都已实际执行。仍未实施的第12章统计诊断、13.10的刻意留空测试及Optuna最终测试保持原边界。

### 新命令与结果

使用隔离venv的Python，以下命令退出码均为0，完整命令已追加到 `commands.jsonl`（现89条，包括安装和检查）：

1. `models.py --input teaching_series.csv --protocol model_protocol.json --out R/ch13_models_validation_with_dependencies`
2. 审阅验证选择后：`models.py --input teaching_series.csv --protocol model_protocol.json --phase test --selection R/ch13_models_validation_with_dependencies/selection.json --out R/ch13_models_test_with_dependencies`
3. `optuna_search.py --input 13.9/input.json --seed 139 --out R/ch13_optuna_with_dependencies`
4. `independent_optional_models.py`：**185/185**追加断言通过。包括训练时点安全、逐模型评分、独立状态空间均值/方差传播与95%区间、Holt-Winters递推、Ljung–Box求和与尾概率、Optuna各trial目标值和选择规则。重新估计仍使用同一statsmodels优化器，明确不冒称独立优化器实现；独立的是预测递推及评分计算。

|验证候选|成功拟合/计划拟合|成功预测且可评分|MAE|RMSE|
|---|---:|---:|---:|---:|
|last|3/3|12/12|4.4166666667|5.0579969685|
|seasonal|3/3|12/12|1.5000000000|1.5811388301|
|ARIMA|3/3|12/12|4.3819478138|5.0280305940|
|SARIMA|3/3|12/12|0.2742903663|0.3746497294|
|Holt-Winters|3/3|12/12|0.2650541445|0.3377726851|

按既定验证MAE规则重新锁定 **Holt-Winters**；没有沿用缺依赖阶段仅两基线中胜出的seasonal。之后测试只运行Holt-Winters：**4/4拟合成功，16/16预测且可评分，MAE=0.2604804161，RMSE=0.2784458981**。其输出明确为点预测，没有借用ARIMA区间。

Optuna使用8次trial，顺序为C3、C4、C4、C1、C6、C5、C0、C6，重复照计预算；本次种子未抽中故意失败的C7，不能声称Optuna失败分支在这次运行触发。选trial3的C1，验证MAE=1.0。它与同种子的标准库随机搜索顺序不同，符合不同随机实现的边界；**Optuna没有评价最终测试**。

### Optuna最终测试范围复核

Optuna所在节为 **13.9**；13.8是三组独立的分位数/经验CRPS/区间评分算例，现有实现不拟合概率模型，也没有Optuna或冻结后模型测试阶段。不能把13.7的另一份数据作为13.8或13.9的测试结果。

13.9正文“**五 Optuna只负责组织搜索**”明确限定该脚本不评价最终测试；`附件/ch13/13.9/README.md`第7行同样说明仅使用开发前缀。`optuna_search.py`第8行的命令行接口只有`--input`、`--out`和`--seed`，第11行切取开发前缀，第18行固定写出`test_status: NOT_EVALUATED`。**该附件未提供读取冻结Optuna选择并评价最终测试的接口，这是设计范围，不是本轮漏跑一个已提供命令。** 13.9输入实际上保留同源的最终两期材料，故不能说“测试材料缺失”；未提供的是Optuna选择→最终评分的交接实现。

`workflow.py`第209—228行只为标准库网格/三个随机搜索生成其各自选择并立即评分；第231—235行虽有通用`--phase/--selection`参数，但只在第7/10节分派给回测函数，第9节不会读取Optuna的`study.json`。因此不能把一个看似带`--phase test`的第9节命令冒称冻结Optuna测试，亦不能借用标准库C1的测试MAE=1作为Optuna已评价的证据。现有流程内的标准库冻结后测试已经执行；Optuna最终测试准确记为 **NOT_PROVIDED_BY_DESIGN / NOT_EVALUATED**，未新增测试桥接程序、未再调参。核查记录见 `optuna_scope_audit.json`。

### 诊断限制没有被“运行通过”抹掉

- SARIMA三个原点均保留“初始季节MA参数不可逆，使用零作起点”的真实警告；最终优化收敛，警告不是被删除或当作无事发生。
- 配置下ARIMA残差Ljung–Box p值约为2.75×10⁻¹⁶、8.78×10⁻¹⁸、1.85×10⁻²⁰；SARIMA约2.53×10⁻⁸、3.13×10⁻⁹、1.01×10⁻¹¹。独立计算Q与p值一致。这些结果不支持把对应残差当作已验证白噪声，**程序执行成功不等于模型适配性通过**。
- ARIMA/SARIMA的条件95%区间在验证12条中各覆盖12条，平均宽度分别22.2419212243和2.9069885431。小型、重叠教学任务中的12/12不证明长期校准；区间也不覆盖历史来源与口径不确定性。
- 新60期数据仍是人工替代教学输入，不是旧数据恢复。本次按预定验证→锁定→测试流程验证程序，不宣称这些公开教学数据是新的未见盲测，也不宣称真实历史预测能力。

当前累计为 **754条数值＋149条边界＋18条窗口＋185条可选模型核验＝1106条通过断言**（修前重复的754条未重复计入）。隔离venv留在云端复算目录，不应作为读者附件分发；交付复现需要的是输入、代码、版本约束、命令与结果日志。

## 第一阶段结论（依赖批准前的历史记录）

本节及下面逐节表保留安装前证据，其中BLOCKED已由上面的追加实跑解除；不得单独摘用为当前状态。

- 标准库可执行教学流程已实际运行；修复后独立数值断言 **754/754**，另有边界断言 **149/149**、窗口计划断言 **18/18**。不是只把原程序返回值当独立复算：仿射另用现有 NumPy 的 SVD 最小二乘、最短路另用 Floyd–Warshall、介数另枚举全部简单路径、社群另按标签分配枚举 877 个集合划分。
- 发现并修复 **2 项真实实现缺陷**：13.7 选择锁未绑定候选与回测协议；15.3 缺失属性提前触发 TypeError。修前输入、输出和日志保留；修改见 `review_fixes.patch`；全部受影响标准库分节另建 `_v2` 目录重跑，没有覆盖旧运行。
- **未完成项保持阻塞：** 已有 Python 3.12.14 及 `/usr/bin/python3` 的 3.13.5 均无 statsmodels、Optuna；常见现有库目录未找到替代安装。没有安装依赖或修改环境。所需最小顶层依赖为 `statsmodels`、`optuna`；若获准安装仍需检查实际新增传递依赖并另次验收。
- `models.py` 验证命令退出 **0**，但 ARIMA/SARIMA/Holt-Winters 各 3 个原点，共 **9 次拟合内部失败**，合计 36 项计划预测失败。退出码 0 只说明工作流写出失败记录，绝不是三个模型通过。Optuna 命令实际退出 **1**，错误为 `ModuleNotFoundError`。
- 第 12 章未实现的 ADF/KPSS/STL、完整 ACF/PACF 诊断不伪记运行。第 13.10 的测试仍是 `NOT_RUN_NO_NEW_INDEPENDENT_TEST`；调用测试分支的拒绝行为已验证，未产生测试成绩。
- 所有计算针对新编人工教学输入。13.2—13.4 的新 60 期表 **不是旧 60 期原输入恢复**，其新成绩不冒充旧模型结果复现。历史事实、来源独立性、人工身份判断和图形解释不因数值一致而自动成立。

## 可复查证据与状态口径

完整逐条命令、工作目录、真实退出码及日志文件名：`../runs/ch12_17/commands.jsonl`（80 条记录，包含正常运行、修前缺陷复现、修后重跑、预期拒绝及独立检查）。命令失败不删除目录。每个实际主运行的输出目录保存其 manifest/provenance 或 failure 文件。

关键文件：

- `independent_check.py` / `independent_results.json`：修前 754 条独立数值断言；
- `independent_check_after.py` / `independent_results_after.json`：修后同一 754 条数值断言，读取新 `_v2` 结果；
- `independent_edge_check.py` / `independent_edge_results.json`：149 条边界与不泄漏断言；
- `window_plan_independent.json`：6 行窗口计划 × 3 条断言；
- `syntax_and_window_checks.log`：9 个 Python 文件内存编译通过，不写 pycache；
- `safety_and_environment.json`、`alternate_python_environment.log`：安全与已有环境证据；
- `section_status.json`、各章 `REVIEW_20261030.json`：逐节状态，未全局替换原发布的 NOT_RUN。
- `integrity_after.json`：本组基线 **109 个文件逐一 SHA-256 核对，0 个变化**；`all_scoped_changes.patch`记录工作副本的全部文本改动；54个新增验收说明相对链接已检查有效。

以下命令以附件对应章目录为工作目录，`R` 表示绝对路径 `book_review_20261030/runs/ch12_17`。下表省略的每个参数和解释器绝对路径仍完整保存在命令清单中。`EXECUTED_PASS` 仅指列明范围；预期错误的非零退出与算法崩溃分开记录。

## 第 12 章

公共预处理命令：`python3 preprocess_annual.py --input data/demo_annual_observations.csv --output R/ch12_origin1915_none_none --origin 1915 --train-start 1900 --evaluation-end 1923 --series-id DEMO_PORT_A --impute none --scale none`，退出 0。

另四次调用分别为 1915/ffill1/standard、1918/none/none、1919/none/none、1920/none/none，输出各自同名新目录，全部退出 0。

|节|实际核验与命令范围|结论|
|---|---|---|
|12.1|任务卡及信息边界，无独立可执行任务程序|设计核对，不称四任务模型已运行|
|12.2|公共预处理 5 次；重复年、混空间口径、负计数三个副本命令均退出 1|正常输入通过；不合法输入按合同拒绝|
|12.3|独立公式核算 2、4、6、8：均值 5，ACF(1)=5/20=1/4|公式复算通过；真实 ACF/PACF 诊断未运行|
|12.4|包内无 ADF/KPSS 执行程序|NOT_RUN，不捏造 p 值|
|12.5|包内无 STL/差分诊断执行程序|NOT_RUN，不默认年度四期季节性|
|12.6|公共预处理；1903 空位、1907/1910/1911缺值、1914零值、1918晚到逐行比对|不填原始 y；ffill1 只填1903；1918在1918、1919原点均遮蔽|
|12.7|公共预处理；另在内存测试常数与无可用训练值|1915原始可用 n=12，均值16.75，总体标准差6.391726423014886；插补不参与拟合；常数尺度1；无观测拒绝|
|12.8|全部训练行的日历、掩码和缺口核验|零值仍是观测；补值不重置距真实观测年数|
|12.9|`window_plan.csv`独立检查全部6行|18/18通过；W02目标1915—1916跨分区拒绝，其余标注与目标分区一致；不是自动生成回测成绩|

### 12→13 的实际接口

`python3 chapter12_adapter.py --input R/ch12_origin1915_none_none/train_input.csv --series-id DEMO_PORT_A --origin 1915 --out R/ch13_adapter_1915`，退出 0。16 个年度位置完整；1903 value 空白，1914 value=0。随后确实运行 `models.py` 读取该 `annual_series.csv` 与独立年度拒绝测试协议（m=1、原点1915、候选last/arima）；流程退出0，两个候选均以 `incomplete or unavailable training prefix` 拒绝，未偷偷删年或插值。直接把原始 CSV 交适配器的错误用法实际退出1（缺 `observed_mask`）。这证明接口走通及模型条件拒绝，不表示年度材料已完成预测。

## 第 13 章

标准库通用命令：`python3 workflow.py --section S --input 13.S/input.json --out R/ch13_sS_v2`。S=1、5、6、7、8、9、10 均实际退出0。

|节|实际命令/状态|独立对照与边界|
|---|---|---|
|13.1|通用命令 S=1，0|最后值与季节预测逐行误差复算；多数类准确率0.5、近邻1；固定异常 TP/FP/FN/TN=0/1/3/4，MAD=3/1/0/4；生成均值方差独立复算，不与旧随机输出混同|
|13.2|`models.py --input teaching_series.csv --protocol model_protocol.json --out R/ch13_models_validation`，0但内部失败|ARIMA三次拟合缺statsmodels；last验证MAE=53/12=4.4166667，seasonal=1.5。不是ARIMA通过|
|13.3|同一次模型验证调用覆盖候选|SARIMA、Holt-Winters各三次拟合缺statsmodels；无任何这两模型的成功分数或区间|
|13.4|验证锁selected=seasonal后实际另次`models.py ... --phase test --selection R/ch13_models_validation/selection.json --out R/ch13_models_test`，0|测试只运行已锁seasonal，16/16预测且可评分，MAE1.5、RMSE1.5811388301。只能报告可用基线中的验证选择，不代表胜过未拟合模型；统计残差与区间诊断仍阻塞|
|13.5|S=5，0|X三节点等权7/9、加权2/3；Y等权5/9、加权11/15；金额与分母正确，非M4/M5官方评分器|
|13.6|S=6，0|A的P MAE3、RMSE√18、sMAPE300/13%；B P/Q MASE1/0.5；C零/负/双零未定义项保留；D缺答案与常数训练不填零；全部定义指标逐项复算|
|13.7|S=7验证0；`workflow.py --section 7 ... --phase test --selection R/ch13_s7_v2/selection.json --out R/ch13_s7_test_v2`，0|验证C1 8/8预测、7可评、MAE130/21=6.190476；C2 7.523810；C3 6/8预测、5可评、MAE2.8但不合格；锁C1测试MAE41/7=5.857143。修后候选/协议改动拒绝；未来值扰动不改变验证预测|
|13.8|S=8，0|平均pinball=8/15，经验CRPS=4/3；A覆盖4/5、宽16/5、区间分数36/5；B全宽20、分数20|
|13.9|S=9，0；`optuna_search.py --input 13.9/input.json --out R/ch13_optuna --seed 139`，1|标准库grid及三随机搜索各8trial，失败和重复均计预算；grid/seed140选C1测试MAE1，seed139/141选C2测试1.0086232538；每次搜索独立，不跨种子择优。Optuna缺包，BLOCKED|
|13.10|S=10开发0；试调用test分支退出1为预期拒绝|四均值分支8/8预测、7可评，MAE6.190476/7.523810/6.071429/7.278912；最后值6/8预测、5可评；五分支共同5任务中C1=5.866667、C3=5.9；交互=-0.1258503401。test仍未评价|

## 第 14 章

命令逐节为 `python3 workflow.py --section S --input 14.S/input.json --out R/ch14_sS`，S=1…5 全部退出0；新程序输出 JSON/CSV，不生成正文旧图或GIS栅格。

|节|独立复算|
|---|---|
|14.1|7出现项、9候选对、6保留候选、3当前人工确认、4未定；唯一候选不自动确认；重号副本退出1|
|14.2|base系数X=(1000,2,0.1)、Y=(2000,0.2,-2)，检查RMSE5；wrong_G4系数X=(940,2.1,0.2)、Y=(2030,0.15,-2.05)，检查RMSE44.1021541424。现有NumPy SVD独立求解一致；共线副本实际拒绝。原附件只有base/wrong_G4，不把聚集/近共线练习冒称随附输入|
|14.3|点距5、折线长7、面面积12；5个内置非法对象逐项拒绝；错误CRS副本退出1|
|14.4|共边T4保留conflict，T8跨期、T9未知；2022迟到X1使T10从matched变conflict；不把末期边界误用结果当正式归属|
|14.5|甲旧[300,800]米、甲新[300,300]；乙端点500计内；丙[350,550]；丁[400,√500000]；戊[1000,1200]；己未知。阈值不代表概率|

## 第 15 章

修后逐节命令为 `python3 workflow.py --section S --input 15.S/input.json --out R/ch15_sS_v2`，S=1…6 全部退出0。

|节|独立复算|
|---|---|
|15.1|A/B/C去重事件2/2/1，材料行3/2/1，机会4/8/2，比率0.5/0.25/0.5；D有覆盖但机会0，比率null；E未覆盖，计数与比率null，未混作0|
|15.2|全部有向节点对及多源最短路用Floyd–Warshall独立校核；rook/queen区分保留；新增零成本A↔B情景实际终止，路径无环且边成本和等于总成本；未知成本/无效时间边保留排除原因|
|15.3|I=3/5；720身份排列中72次达到观察值，尾部0.1；组内36排列尾部1且退化；机会属性全0.5所以常数失效。修后缺失事件/机会、零机会、无权重均保留六区域并正确标注失效；负机会/重复边/重复区域退出1|
|15.4|A原率0.27→0.86、共同结构0.55→0.65；B原率0.73→0.34、共同结构0.45→0.55；缺正权重层时标准化值null，不重新归一化剩余层|
|15.5|4区划×2窗×2定位版本，48个联合配置组/108区域行；各配置已定位总数early=6、long=9；U均保留未定位；不把不同配置上界相加|
|15.6|M5来源根为M2；三解释来源族数3/2/2，因果分数均null；不是可信度评分|

## 第 16 章

基线命令 `python3 relations.py --data . --out R/ch16_base`，退出0；另外 `--assume-identity P3`、`--defer-instance R2`、`--end-year 1709` 分别输出 identity/deferred/window 新目录，全部退出0。

|节|执行与核验|
|---|---|
|16.1|13陈述、12人工实例；基线6纳入实例、7纳入陈述；逐原始陈述独立套时间、身份、层级与判断规则一致|
|16.2|候选逐条selected_span重新切原文等于quote；重叠匹配示例aaaa/aa保留[0,2],[1,3],[2,4]；空摘录拒绝；不宣称抽取准确率|
|16.3|给定身份映射与配对判断实际校验；P3情境为确认身份假设，不是合并P1；identity情境7实例/8陈述|
|16.4|闭区间窗口实际运行；end1709纳入8实例/9陈述；延期R2为5实例/6陈述；未按成书年筛事件|
|16.5|C5/C11同R5保留两证据不重复计实例；基线投影仅P1-P2共同V1=1；identity情境增P1-P3、P2-P3各1；投影不推断相识|

## 第 17 章

基线命令 `python3 network_analysis.py --data . --out R/ch17_base`，退出0；另外窗口1703—1705命令、`--gamma 0.5 --gamma 1 --gamma 2`命令均退出0。默认基线另含γ=0.1。

|节|执行与独立对照|
|---|---|
|17.1|固定A—H名册，9有向寄信事件；双方向AB折叠为无向存在边但保留事件来源；H不因无边移除|
|17.2|无向N8/M8，分母28，密度2/7，分量7+1；有向M9、分母56、密度9/56；强连通ABC、DEF、G、H；度和16=2M|
|17.3|全简单路径独立复算C/D/F原始介数8/9/5，归一化8/21、3/7、5/21；H各中心性0。空/单点图密度null，双孤点图密度0；未将小分量局部分母冒充全图分母|
|17.4|独立标签枚举877个活跃节点划分。γ0.1全组Q9/10；γ0.5 ABC/DEFG为159/256；γ1同划分47/128；γ2唯一最优ABC/DE/FG为−5/64。检查的是全部最优，不遗漏并列；H单列是展示约定。超过8非孤点实际拒绝|
|17.5|补BE后独立路径计算D原始介数7/2，F归一化5/21；早/后窗都N8/M4/密度1/7，但分量分别3+2+1+1+1和5+1+1+1；来源组/逐边/节点缺失情境实际生成，不当死亡或历史因果模拟|
|17.6|事件→来源→存在边及解释登记输出实存；结构计算验收通过，史料真实性、来源独立性、历史解释仍需人工证据，不自动PASS|

## 修复前后证据

### 13.7 锁定候选没有锁住定义

修前改变副本中C1 `window:4→null`，保留原历史与selection，测试命令错误地退出0：测试MAE从5.8571428571变为13.1248196248。`bug_before_ch13_changed_candidate`保存证据。

修复：在 `workflow.py/backtest` 把候选定义、验证/测试原点、步长、两个评分截止和最小训练数形成 `protocol_sha256`，验证写入，测试核对。历史摘要仍单独核对；truth不进入预测器，独立保留评价职责。旧选择文件没有新摘要时明确要求在新目录重新验证，不静默兼容。

修后相同改动在 `bug_after_ch13_changed_candidate` 退出1，明确报协议改变。新正常验证/测试退出0，原教学数值未变。

### 15.3 空值被比较为负数之前就崩溃

修前把A的events改为null，命令退出1，`TypeError: '<' not supported between instances of 'NoneType' and 'int'`，不能兑现正文的missing_attribute约定。`bug_before_ch15_missing`保留失败。

修复：缺失数与机会数保留None；仅对已知值校验有限、非负和数值类型；密度/机会率按缺失传播；不删区域；精确机会比率通过显式Fraction构造。

修后 `bug_after_ch15_missing` 退出0，计数/机会属性均missing_attribute，全局指数null、不排列、六区域保留。已有完整教学输入的0.6/0.1/1数值不变。

## 未做与停止边界（第一阶段历史记录）

没有网络发布、上传、调用账户、删除文件、覆盖基线、安装依赖或改变配置。14—15的绘图与教材旧SVG不冒称本程序新产物。预处理、字段适配与严格拒绝不是统计诊断或模型拟合成功；源码安全检查与数值断言也不是无限输入空间上的形式证明。

当前待用户授权的唯一继续项是可选依赖安装后的 statsmodels/Optuna 实跑。若批准，须在新输出目录重跑、记录实际版本和传递依赖、审阅收敛警告与选择后测试，并追加报告，不能把本报告的BLOCKED直接翻为PASS。

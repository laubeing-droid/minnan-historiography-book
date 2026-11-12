# 第17章数据字典

## 输入

CSV为UTF-8，首行字段名。ID不是人名或真实性证明；空值表示未知/不适用，不补零。时间采用整数年闭区间。

### nodes.csv

`node_id`唯一；`display_name`显示字母；`roster_source`与`roster_locator`指X0/roster1；`identity_status=confirmed`是给定教学身份，不是本次核验结果。名册总体现于节点表，不从有边人物反推。

### events.csv

`event_id`唯一T编号；`sender`、`recipient`引用节点并保留方向；`event_year`发生年；`source_id`、`locator`指sources.json摘录；`identity_status`为confirmed/pending；`event_status`为accepted/pending/rejected。程序保留所有输入事件并生成排除理由；不按相同收发件人去掉独立事件。T01与T09反向，派生无向图中均连AB，但仍是两个事件。

### sources.json

每项含`source_id`、`title`、`compiled_year`、`independent_group`、`locations`、`material_kind`。X0定义观察总体；X1—X4为教学记录组。材料编成年不同于事件年。locations的键是位置标签而非实际原件页码，值是新写合成摘录。independent_group是给定分组，不是自动检验为独立。

### model_spec.json

- `version`：新编输入协议版本；`execution_status=NOT_RUN`：交付状态。
- `population`：fixed_roster_X0，保留H。
- `start_year`、`end_year`、`interval`：主窗及闭区间规则。
- `event_inclusion`：确认身份与接受事件，按发生年筛选。
- `directed_view`：有序人物对存在图；同方向多个事件保留到来源链。
- `undirected_view`：任一方向存在即可连边，事件数不代入密度M。
- `self_loops`、`parallel_event_rows`、`weights`：拒绝自环、保留独立事件、次数与二值分开。
- `betweenness`：无向、不计端点、全图归一化。
- `closeness`：可达比例修正。
- `isolate_partition`：孤立点单列只为展示。
- `gamma`：可精确解析的十进制/分数字符串；`exhaustive_nonisolated_limit`：穷举规模上限。

### interpretation_register.csv

claim_id唯一；scenario指派生情境；claim为有待限定的主张；competing_explanation并列可区分解释；required_evidence说明补查；status明确待核查或无来源假设；source_chain提供指标至来源的回查路径。此表不是已证实历史事实。

## 派生输出

### 基本结构

`network_summary.json`分别标模型、N、M、可能连接数、精确分数/小数密度、分量、孤立点及最大分量比例。无向密度M/[N(N−1)/2]，有向密度M/[N(N−1)]，N<2为null而非稀疏零。`degree_sum`与`degree_sum_reference_2M`只提供技术账目，不验证史实。

`derived_edges.csv`每对人物一行：node_a/node_b按ID排序；event_count表示纳入事件数；event_ids及source_locations保留多个事件与出处，不代表独立证言强度。`components.csv`的view区分undirected、directed_weak、directed_strong；component_id仅当前输出编号，无历史身份含义。

### 中心性

centralities包含node_id、degree、degree_centrality_fraction/decimal、raw_betweenness_fraction、normalized_betweenness_fraction/decimal、reachable_other_nodes、distance_sum、corrected_closeness_fraction/decimal。介数分母为(N−1)(N−2)/2，N≤2按实现约定归一化值0；接近中心性r/(N−1)×r/S，没有可达他人时0。不把零值解释成没有社会能力。

bridges_and_articulations的bridges为移出一边后分量增加的边；articulation_points为移出该点及邻边后分量增加的点。此处的移出仅是计算视图，不删除材料，不认定因果。

### 社群

communities每行一个γ与一个并列最优划分；optimum_id为该γ内编号；Q_fraction精确分数，Q_decimal为展示近似；active_partition以分号分组、逗号列成员；isolates_display_separately为任意展示约定；candidate_partition_count记录穷举候选数。M=0时Q为null。

co_membership每个γ每个人物对一行；coassigned_optima/all_optima为该γ全部最优解的计数；coassignment_status为all/some/none。它不能解释为历史归属概率，也不是对γ进行概率加权。

### 比较与敏感性

comparisons的window_start/end固定为两个三年教学窗，roster=fixed_X0，event_ids可回查。sensitivity每个情境包含完整结构、中心性、桥、割点及变化说明；hypothetical_edges不具来源；kept/omitted只指派生视图。base为当前主窗；比较窗独立，不随主窗自动改写。

### 来源链

event_audit逐事件保存included及all_reasons；provenance含实际执行时间、Python版本、argv、输入SHA-256、实际窗口/γ、节点名册链、所有事件摘录、派生边链、来源目录及变换清单。哈希只辨版本，不能证明转录或身份为真。运行状态仅说明读者执行，不会自动认证历史解释。

# 第16章关系数据教学附件

## 性质与状态

本目录是依据正文重新编制的自包含教学附件。没有恢复到原16.1或16.2读者包程序；这里的Python文件是新写实现，不是原件。所有人物、组织、地名、事件、来源摘录均为合成教学材料，不对应真实闽南史实。正文沿用底本数字；新附件未执行，不声称已重现旧数值。

**交付执行状态：NOT_RUN。** 本轮未运行脚本、模型计算、复算、语法测试、独立测试或校对验收。目录中没有伪造运行日志或预生成结果。`execution_status.json`记录的是交付状态，不是成功报告。

## 三套练习不得串号

1. 16.1、16.4、16.5：P1—P4、O1、V1—V3、C编号、R编号及来源S1—S5/H1。
2. 16.2：三份定位原文S1—S3、六条候选K1—K6。它的S编号不指第一套的来源。
3. 16.3：D1—D7、M1—M7、P-A/P-B/O-A/O-B，不指第一套P编号人物。

跨练习的近名、同号和相同年份都不是实体同一性的证据。

## 文件与正文对应

| 文件 | 内容 | 对应节 |
|---|---|---|
| `entities.csv` | 人、组织、事件主表与身份状态 | 16.1、16.4 |
| `relation_types.csv` | 端点类型、方向、事件要求、自环约束 | 16.1 |
| `events.csv` | 三个事件发生年 | 16.1、16.4 |
| `assertions.csv` | 13条给定陈述及人工实例编号 | 16.1、16.4、16.5 |
| `sources.json` | 可回查的合成来源位置与摘录、转抄同源组 | 16.1、16.4 |
| `rules.json` | 闭区间、研究窗与纳入规则 | 16.1、16.4 |
| `candidate_sources.json`、`candidates.json` | 三份逐字原文与六条指定候选 | 16.2 |
| `disambiguation_cards.csv`、`entity_mapping.csv` | 七卡片及身份映射 | 16.3 |
| `pair_decisions.csv` | 同一、不同、待定判断日志 | 16.3 |
| `version_impact_template.csv` | 实体改判影响登记例，未执行 | 16.3、16.5 |
| `relations.py` | 读入、结构约束、筛选、定位、分层与参加投影 | 全章 |
| `source_extracts.md`、`data_dictionary.md` | 人读摘录与字段说明 | 全章 |
| `provenance_path.svg` | 手工绘制来源链示意，非计算输出 | 16.4、16.5 |

`source_extracts.md`的语句按正文条件重写，不冒称逐字恢复旧包。S4的1730年与S5的1750年沿用正文设定，其他来源编成年未知即为null。`C5`与`C11`仍保留两个证据位置，均对应`R5`和同源组G3。

## 运行方式 由读者另行执行

需要Python 3.10或以上，不安装依赖，不联网、不访问账户、不调用LLM。先完整复制本目录到个人研究工作目录，再在该副本内运行：

```bash
python relations.py --data . --out run_base_new
```

`--out`必须是**尚不存在**的目录，其父目录必须已存在。程序不覆盖已有结果，不修改输入；失败后若留下未完成目录，请另选目录名，不要把它当成完整结果。本附件不自动删除任何文件。

独立情境示例，每次只改变一个条件：

```bash
python relations.py --data . --out run_identity_new --assume-identity P3
python relations.py --data . --out run_deferred_new --defer-instance R2
python relations.py --data . --out run_window_new --end-year 1709
```

这些命令表示教学假设，不表示已采纳新身份判断、已找到新材料或已执行。P3并入P1不是这个开关的含义；真正合并须另存输入版本，逐条重审R7自环与R3/R8重复，不能静默替换编号。

## 执行后输出契约

- `confirmed_instances.csv`、`excluded_instances.csv`：按人工实例计数，后一表保存所有同时存在的排除原因。
- `assertion_audit.csv`：保留全部陈述的纳入状态，不因同实例而丢弃转抄证据。
- `nodes.csv`、`layer_edges.csv`、`attendance_bipartite.csv`：主节点、分类型关系与人—活动边，不混作同质人际网。
- `projection.csv`：仅投影确认参加边，计共同事件数，保留事件、实例、陈述和来源；不推断相识，不输出对角线。
- `lineage.json`：每个关系实例到原文位置的完整链，包括暂不纳入者。
- `candidate_evidence.json`、`candidate_evidence.svg`：定位结果、所有匹配位置、码点跨度与待查提示；不是抽取准确率或语义金标准。
- `disambiguation_audit.json`：给定映射和配对判断，不进行名字相似自动认人。
- `relations.svg`：按关系实例逐行示意，节点重复显示不是新增实体。
- `provenance.json`：实际运行时间、Python版本、命令、输入SHA-256、窗口、情境与计数。哈希辨认文件版本，不证明史料或判断为真。

上述输出当前均不存在，须由读者执行后生成。正文的六确认实例、七纳入陈述及投影数字仅作旧例对照，不能在未运行时填写“通过”。

## 人工核查边界

结构约束不能判断OCR是否忠实、否定范围是否正确、两材料是否真正独立、身份是否历史真实或无记录是否不存在。候选定位只定位教师指定的摘录，不能报告未知名称发现的召回率。日期仅支持完整整数年闭区间或两端均未知，不支持完整EDTF、模糊事件范围或历法转换。

方法链接沿用正文：CIDOC CRM 7.1.3、W3C PROV Primer、Web Annotation Data Model、Unicode码点/字节区分、EDTF及NetworkX二模和投影定义。链接用于方法，不为合成史事背书；本次未重新核读外部页面。

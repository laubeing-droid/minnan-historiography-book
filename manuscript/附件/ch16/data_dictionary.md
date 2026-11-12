# 第16章数据字典

## 通用约定

UTF-8；CSV首行为字段名；空字符串表示未知或不适用，不能自行当0。JSON的null表示未知。整数年区间两端均包含。ID为稳定引用，不是名称、顺序或真实性证明。P、S、D等命名空间按README区分。

## 输入字段

### entities.csv

- `entity_id`：唯一主键。
- `display_name`：显示名称，可修订而不改变ID。
- `entity_type`：person、organization、event。
- `identity_status`：confirmed或pending；为给定教学判断。
- `judgment_version`：判断版本；不是证据日期。

### relation_types.csv

- `relation_type`：member、participate、send_letter、sibling、father、acquainted。
- `subject_type`、`object_type`：允许的端点实体类型。
- `directed`：true/false，按关系含义而定。
- `event_required`：是否必须有event_id；参加边的客体必须等于该事件。
- `allow_self`：是否允许同一实体成为两端；本例均为false。

### events.csv

`event_id`引用event型主节点；`start_year`、`end_year`是发生年闭区间；`event_kind`说明activity或letter。事件时间须与引用它的关系发生区间一致。

### assertions.csv

- `assertion_id`：材料陈述唯一主键C，不等于分析边。
- `instance_id`：教师事先给定的发生/关系实例R；程序不自动判断同一次发生。
- `subject`、`relation_type`、`object`：端点与关系。
- `start_year`、`end_year`：支持区间；未知时两端均空。
- `temporal_kind`：continuous_support连续支持；event_year精确发生年；evidence_support证据支持期；unknown未知。证据支持末年不表示亲属关系终止。
- `event_id`：具体事件引用；不凭它另造人—事件边。
- `source_id`、`locator`：第一套sources.json中的来源位置。
- `layer`：statement材料陈述或hypothesis分析假设。
- `judgment`：accepted、pending、rejected；只accepted且其他条件满足才纳入。
- `judgment_reason`：给定人工判断理由，不是程序自动验证结果。

同instance_id的端点、类型、时间、事件、层次与判断须一致，否则报错。证据位置可不同；C5/C11正是同实例的不同位置。R编号没有R11是为保留C11复指R5，不是遗漏一条实例。

### sources.json

数组中`source_id`唯一。`compiled_year`为材料编成年，未知null；不得作为关系发生年。`independent_group`记录已给定同源关系，S3/S4都为G3，不是自动独立性评分。`locations`以locator为键，值为新写合成摘录。`material_kind`与`provenance_note`标识新建而非原件恢复。

### rules.json

`start_year`、`end_year`给定研究窗；`interval`固定closed_integer_year；其余项说明未知日期排除、确认身份、材料陈述层、接受判断、人工实例去重单位及强度未知。`execution_status=NOT_RUN`是交付标记，不会随读者运行改写输入。

### candidate_sources.json 与 candidates.json

前者每项含source_id、version、page_label、text。text原样读取，不删除换行或正规化；页标签是教学标签，不是原始影像。后者含candidate_id、source_id、quote、names、occurrence、direction_hint、strength。occurrence为从0开始的出现序号；null时仅单一匹配才自动选定。direction_hint只保存不认证；strength为null，不赋人际强度。

跨度为Python Unicode码点的[start,end)，并非UTF-8字节。所有匹配都保存，出现多次未指定序号则ambiguous。negation_hint与cross_paragraph_hint仅安排人工核查。

### disambiguation_cards.csv

mention_id唯一；source_id指D卡片，不连接第一套S；activity_year是材料所述活动年；name_as_written保留名称；place_role/ place_name区分地点角色；context保留关键教学上下文。

### entity_mapping.csv

每张M卡恰有一行。entity_id仅confirmed时赋值；pending保留空ID与candidate_entities分号集合。judgment_version、reason记录教学判断。未知M4不是已确认的新第三人。

### pair_decisions.csv 与 version_impact_template.csv

配对判断以left_mention/right_mention引用卡片；decision为same/different/pending；evidence、judgment_author、judgment_date与status记录依据和状态。unknown日期不补为今天。影响模板区分合并/拆分、旧新版本与ID、多对多映射、受影响提及实例、自环/重复复核和需要重新生成的输出。EXAMPLE_NOT_EXECUTED只是一条填写示例。

## 派生输出解释

confirmed/excluded实例表的`assertion_ids`和`source_ids`用分号连接显示，但原始证据仍逐条保留。`reasons`列列出全部排除条件；假设情境另列身份假设。projection的`shared_event_count`等于共同确认事件数；events/instances/assertions/sources保留追溯连接。lineage中的excerpt来自sources.json，不是外部档案抓取。provenance中的计数是读者实际执行时生成，既不是交付前结果，也不是历史真实性认证。

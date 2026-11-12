# 第12章从头新写交接

## 已交付

完整正文：`final/正文/ch12.md`。按目标目录从头写成9节，约2.2万字符，面向普通本科读者，以区域历史与文化地理的资料条件解释时序技术。不是大纲，不是旧第12章的恢复件。

完整附件目录：`final/附件/ch12/`，13个实文件：

1. `README.md`
2. `data/demo_annual_observations.csv`
3. `data/demo_events_uncertain.csv`
4. `data/demo_monthly_calendar.csv`
5. `data/source_registry.csv`
6. `field_dictionary.csv`
7. `task_specs.csv`
8. `window_plan.csv`
9. `diagnostic_record_template.csv`
10. `preprocess_annual.py`
11. `interface_ch13.md`
12. `references.md`
13. `run_status.json`

## 目标节覆盖

|目标节|实际正文内容|配套实文件|
|---|---|---|
|12.1 四类任务数学定义|预测信息集合与历时原点、分类独立标签、在线离线异常、生成不等于恢复史料|task_specs.csv|
|12.2 标准数据与加载|ETT及UCR/UEA、真实海关入口、长表主键、时空口径、事件区间、字段校验|data目录与field_dictionary.csv|
|12.3 ACF与PACF|等间隔条件、公式、间接相关、短样本与多滞后、图形记录|diagnostic_record_template.csv|
|12.4 ADF/KPSS|弱平稳、趋势与差分平稳、相反原假设、四种组合、口径断裂与短样本限制|diagnostic_record_template.csv与references.md|
|12.5 STL与差分|趋势季节周期、参数区别、年度例不强造季节、差分与逆变换、全段平滑泄漏|interface_ch13.md|
|12.6 缺失与掩码|零与来源缺失、晚发布、原点遮蔽、有限填充、真值隔离|annual CSV与预处理脚本|
|12.7 归一化|单位与统计缩放区别、训练内拟合、冻结与滚动重拟合、常量处理、参数保存|脚本与字段字典|
|12.8 时间特征|历法与精度、可用时刻、周期编码、滞后和有效数量、拒绝事后特征|monthly_calendar.csv与字段字典|
|12.9 窗口策略|L/H/S/W、按目标分区、跨界拒绝、扩展与滚动、其他任务实体隔离|window_plan.csv与interface_ch13.md|

## 第13章接口已协调

与`/root/adapt_book_spatial_network`确认：第13章适配器读将来生成的`train_input.csv`，序列标识`DEMO_PORT_A`，映射`value=y`、`available_at=availability_year`。四位整数年度；空值保留；默认不读取`input_y`，不读取`evaluation_truth.csv`。第13章适配器已处理空可用年份并保留掩码。主例缺失会触发第13章完整训练前缀合同的拒收，双方正文与README均说明适配不等于模型适用，不偷偷填补。

第13章独立四期教学例与本章年度主例没有数据拼接关系。本章主例不预设季节周期。脚本在训练视图中对晚发布观测连同存在性掩码一并遮蔽，原始来源状态不作为较早原点特征。

## 来源和状态

真实资料入口使用Harvard-Yenching海关数字化项目、CHGIS、NOAA官方说明；方法使用FPP、pandas、statsmodels、scikit-learn及基准官方资料。正文保留可点击来源，references.md登记用途。没有复制真实历史观测，演示值明确标注SYNTHETIC_DEMO，不报告虚构系数、检验p值或模型结果。

`preprocess_annual.py`和全部统计、模型、预测评价状态均为`NOT_RUN`。只写代码与说明，没有执行新脚本、模型或学术复算；没有安装依赖、修改环境配置、访问用户本机或外发内容。结构交付层面已确认9个目标节标题存在、附件CSV行字段数一致；这不是学术校对或运行验收证明。

未读取受限旧第12章Page，未修改任何baseline文件。参考了获准目录和第13章正文用于衔接。沿用Markdown加CSV/脚本附件的ZIP交付格式，不制造DOCX。共享documents技能已读；其DOCX操作标记工具不支持md格式，未伪报DOCX渲染或视觉验收。正文与附件可由root直接纳入合订和ZIP，未进行任何上传。

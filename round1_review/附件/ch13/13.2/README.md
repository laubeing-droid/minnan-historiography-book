# 第13.2节附件说明

> **2026-10-30 复算更新：** 本节当前状态为 `EXECUTED_PASS_WITH_DIAGNOSTIC_LIMITATIONS`。下文 `NOT_RUN` 等为原始编制状态；本次记录见 [章节验收状态](../REVIEW_20261030.json) 与 [复算报告](../../../../reports/ch12_17_recomputation.md)。

状态：NOT_RUN。新编教学附件，不是原程序恢复。没有执行学术计算、模型拟合、回测、测试或校对验收。

本节与13.3—13.4共用完整60期教学CSV及model_protocol.json。差分在模型内部处理，外部不预先二次差分；ARIMA固定(1,1,0)、trend=n。输入为新编抽象期次，不是恢复的原60期，更不是真实历史序列。

## 输入

本节与13.2—13.4共用上一层teaching_series.csv、model_protocol.json和models.py。模型程序需要读者环境已有statsmodels及其依赖；不会自动安装。last与seasonal基线仅用标准库，其他候选缺库时记录失败。

## 操作

从本说明所在目录开始，待获得运行授权后：

```bash
cd ..
python models.py --input teaching_series.csv --protocol model_protocol.json --out model_validation_new
# 只有查看并固定验证选择后，才另次执行测试
python models.py --input teaching_series.csv --protocol model_protocol.json --phase test --selection model_validation_new/selection.json --out model_test_new
```

所有输出目录必须不存在。输出只写入新目录，输入不改；失败记录写failure.json，不宣称成功。

## 预定输出

标准库脚本拟生成result.json、各逐行结果CSV与run_manifest.json；回测另存selection.json，模型脚本另存fit_records.json、predictions.csv、summary.csv。模型残差诊断数据不等于已画图并解读。输出当前尚未产生，不把预定文件写成实交结果。

字段及跨节差异见[统一数据字典](../数据字典.md)，方法来源见[SOURCES.md](../SOURCES.md)。每节独立例中的A/B、期号及来源编号只在本例有效。

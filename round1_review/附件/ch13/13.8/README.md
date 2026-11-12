# 第13.8节附件说明

> **2026-10-30 复算更新：** 本节当前状态为 `EXECUTED_PASS`。下文 `NOT_RUN` 等为原始编制状态；本次记录见 [章节验收状态](../REVIEW_20261030.json) 与 [复算报告](../../../../reports/ch12_17_recomputation.md)。

状态：NOT_RUN。新编教学附件，不是原程序恢复。没有执行学术计算、模型拟合、回测、测试或校对验收。

三组完整输入分别支持分位数损失、经验CRPS、区间覆盖与区间分数，不从三个分位数伪造连续CDF。新脚本只拟输出评分表，不拟合分布、不画PIT、不计算显著性。

## 输入

input.json是本节完整输入；workflow.py在上一层。只用Python标准库，不联网。

## 操作

从本说明所在目录开始，待获得运行授权后：

```bash
python ../workflow.py --section 8 --input input.json --out run_new
```

所有输出目录必须不存在。输出只写入新目录，输入不改；失败记录写failure.json，不宣称成功。

## 预定输出

标准库脚本拟生成result.json、各逐行结果CSV与run_manifest.json；回测另存selection.json，模型脚本另存fit_records.json、predictions.csv、summary.csv。模型残差诊断数据不等于已画图并解读。输出当前尚未产生，不把预定文件写成实交结果。

字段及跨节差异见[统一数据字典](../数据字典.md)，方法来源见[SOURCES.md](../SOURCES.md)。每节独立例中的A/B、期号及来源编号只在本例有效。

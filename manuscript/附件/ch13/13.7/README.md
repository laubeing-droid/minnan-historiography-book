# 第13.7节附件说明

状态：NOT_RUN。新编教学附件，不是原程序恢复。没有执行学术计算、模型拟合、回测、测试或校对验收。

历史和评分参照分别成表。第6期缺失、第8期晚到、第9与15期无评分参照均在输入明列。验证选择写入新目录后，测试必须另次命令读取该选择；任何失败仍保留计划任务。新程序没有自动执行破坏性自测，练习由读者另建输入副本完成。

## 输入

input.json是本节完整输入；workflow.py在上一层。只用Python标准库，不联网。

## 操作

从本说明所在目录开始，待获得运行授权后：

```bash
python ../workflow.py --section 7 --input input.json --out run_new
# 验证选择保存后另次测试；两目录均必须事先不存在
python ../workflow.py --section 7 --input input.json --phase test --selection run_new/selection.json --out test_new
```

所有输出目录必须不存在。输出只写入新目录，输入不改；失败记录写failure.json，不宣称成功。

## 预定输出

标准库脚本拟生成result.json、各逐行结果CSV与run_manifest.json；回测另存selection.json，模型脚本另存fit_records.json、predictions.csv、summary.csv。模型残差诊断数据不等于已画图并解读。输出当前尚未产生，不把预定文件写成实交结果。

字段及跨节差异见[统一数据字典](../数据字典.md)，方法来源见[SOURCES.md](../SOURCES.md)。每节独立例中的A/B、期号及来源编号只在本例有效。

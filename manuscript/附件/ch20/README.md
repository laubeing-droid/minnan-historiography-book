# 人口规模与份额的写作练习

本版新制教材配套。真实来源的整理值、教学设例、空白模板分开标记。代码状态 NOT_RUN，未作本轮学术复算或语言校对；文件结构检查不代表计算结果通过。

[人数输入](population_values.csv)是四个整数，单位为人；[公报份额](published_shares.csv)独立保存原列值，不从份额倒推人数。[来源与口径](source_notes.md)解释时点与范围。[工作表](calculation_workbook.md)先手工填写，已有结果见[继承记录](inherited_results.md)。

已有Python时可运行：`python -B calculate_population_NOT_RUN.py`。脚本只读输入并打印派生值，不执行本轮复算。需要记录时由读者另存新输出，不覆盖输入。 [图表设计](figure_spec.md)提供两面板的作图输入与标题，不伪造年度中间值。

写作顺序：读来源 → 人数与份额分开 → 说明分子分母关系 → 用[主张表](claims.csv)检查原因与描述的界限 → 阅读[结果段](result_paragraph.md)。[提示模板](writing_prompt_NOT_RUN.md)未调用模型。

这套材料不能检验人口迁移原因，也不能完成跨年口径一致性考证。当前任务是把一个有限的描述问题写完整。

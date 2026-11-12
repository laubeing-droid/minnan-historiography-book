> 复算更新（2026-10-30）：本章实际执行情况见 execution_receipt_20261030.json。文件名中的 NOT_RUN 保留写作版命名，不再代表全部当前状态；未执行项目仍单列。

# 人口规模与份额的写作练习

本版新制教材配套。真实来源的整理值、教学设例、空白模板分开标记。本轮分项运行与核对结果见 execution_receipt_20261030.json；其中模型调用与实际计算分别记录，不以文件结构检查替代内容判断。

[人数输入](population_values.csv)是四个整数，单位为人；[公报份额](published_shares.csv)独立保存原列值，不从份额倒推人数。[来源与口径](source_notes.md)解释时点与范围。[工作表](calculation_workbook.md)先手工填写，已有结果见[继承记录](inherited_results.md)。

已有Python时可运行：`python -B calculate_population_NOT_RUN.py`。脚本只读输入并打印派生值，不修改输入。需要记录时由读者另存新输出，不覆盖输入。 [图表设计](figure_spec.md)提供两面板的作图输入与标题，不伪造年度中间值。

写作顺序：读来源 → 人数与份额分开 → 说明分子分母关系 → 用[主张表](claims.csv)检查原因与描述的界限 → 阅读[结果段](result_paragraph.md)。[提示模板](writing_prompt_NOT_RUN.md)未调用模型。

这套材料不能检验人口迁移原因，也不能完成跨年口径一致性考证。当前任务是把一个有限的描述问题写完整。

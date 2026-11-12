# 两条题录的有限自动化

本版新制教材配套。真实来源的整理值、教学设例、空白模板分开标记。代码状态 NOT_RUN，未作本轮学术复算或语言校对；文件结构检查不代表计算结果通过。

[正常输入](catalog_input.csv)承接正文两条公开目录字段；[异常输入](catalog_anomalies.csv)人为加入重复编号和空题名，不是原目录错误。[来源注记](source_notes.md)保留册数与上游关系，不能只保留机械检查的五列。

手工路径：检查五列、两条身份、重复编号和空栏，随后返回公开页面核对指定字段。程序路径仅在已有Python时执行：

```bash
python -B check_catalog_NOT_RUN.py --input catalog_input.csv --output catalog_review_NEW.json
python -B check_catalog_NOT_RUN.py --input catalog_anomalies.csv --output anomalies_review_NEW.json
```

输出使用排他创建，遇到同名文件停止。脚本不下载页面、不改原CSV，不处理账号、发送消息或合并版本。真实字段核对和版本判断由人继续。

[预期行为](expected_behavior.md)定义形式规则，不是实际输出；[任务模板](task_template.md)保留权限和状态；[未决问题](unresolved_questions.md)给出下一步；[模板变更表](template_change_log.csv)供读者记实际变更。

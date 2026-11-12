# 第13章教学附件

全部新程序状态为NOT_RUN。新编输入、代码与说明已实交；不存在未运行却声称生成的结果。原13章精确60期输入与程序未恢复，本包明确提供替代教学实现，不对旧模型结果作恢复承诺。

- [13.1输入与操作](13.1/README.md)
- [13.2输入与操作](13.2/README.md)
- [13.3输入与操作](13.3/README.md)
- [13.4输入与操作](13.4/README.md)
- [13.5输入与操作](13.5/README.md)
- [13.6输入与操作](13.6/README.md)
- [13.7输入与操作](13.7/README.md)
- [13.8输入与操作](13.8/README.md)
- [13.9输入与操作](13.9/README.md)
- [13.10输入与操作](13.10/README.md)

## 从第12章接入

先使用第12章预处理脚本输出train_input.csv；原始data/demo_annual_observations.csv尚无掩码，不能直接交给适配器。chapter12_adapter.py接收该训练接口中的series_id、period、y、observed_mask、imputed_mask、eligible_target、unit、measure、boundary_version、source_id、availability_year。period是四位整数年；value仅保留未经填补的原始观察，缺失不置零。available_at取availability_year；被第12章屏蔽的缺失或未公布行保持空值，不猜发布日期。原点可用性另存日志。imputed_mask只针对input_y，本适配器不读取input_y。evaluation_truth.csv不交给此训练适配器。

```bash
python ../ch12/preprocess_annual.py --input ../ch12/data/demo_annual_observations.csv --series-id DEMO_PORT_A --origin 1915 --impute none --scale none --output annual_prepare_new
python chapter12_adapter.py --input annual_prepare_new/train_input.csv --series-id DEMO_PORT_A --origin 1915 --out annual_adapter_new
```

年度材料设m=1，只考虑非季节候选；不要直接套用60期四周期protocol。若年度训练前缀有缺失、晚到或不连续，models.py按当前严格契约拒绝拟合，必须先明定另一份预处理和评估协议，而不是让适配器静默插补。第12章metadata与eligible_target仍必须在评分侧核对；本适配器只作字段桥接，不自动把历史资料变成可预测对象。

## 执行边界

标准库流程不需要安装依赖；models.py和optuna_search.py仅使用已存在的可选库。没有自动安装、联网下载或删除文件。可选程序无法执行时，保留失败记录，勿填入想象结果。

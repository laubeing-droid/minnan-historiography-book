# 第7—11章独立复算报告

## 结论

- 新版 **43节** 均实际运行；最终 **61条命令、31项边界检查、107项独立数值/结构/输入副本检查通过**。
- 发现并修复 **9项** 输入隔离、缺值/分母、配置及编号问题；修前失败日志和修后结果均保留。
- 旧正文公开数据另做 **54项** 算术与字符位置核对，未发现确定的正文数值错误。这不是旧模型或旧实验全链路复现。
- 原 `book_completion_20261030/final` 未改；无联网、安装、模型调用、删除或外发。

## 可复核范围和状态

`EXECUTED_PASS`只指列出的运行及预期；坏输入被明确拒绝时可为测试通过，但原始退出码仍为1。`FAIL`为修前实际缺陷。`BLOCKED`为不能由现存材料完成的旧链路。`NON_RUNNING_TEMPLATE`为工作表/卡片/提示或基准规格；渲染器跑过，不代表模型/人工评价跑过。

五份原workbook.py逐字相同，静态通读后才执行；只有`--input`和`--help`入口，无其他CLI子命令。每节输入以mode分派；43节覆盖所有38种mode（共享分支不在每个副本重复声称全覆盖）。现有Python标准库环境足够。

## 缺陷、修复与证据

|编号|节|修前问题|修后处理|
|---|---|---|---|
|R0711-01|8.8|盲预测入口input.json和input.csv包含gold，违反参考隔离交接约定|移除预测入口/阅读副本的gold，保留评分者reference.csv；明确交接所需配置/代码文件；[修前](../runs/ch07_11/before/8.8_input.json.preimage.txt) / [修后](../runs/ch07_11/verified/8.8__blind_without_reference.stdout.json)|
|R0711-02|10.7|未知bootstrap unit拼写静默退回逐行抽样|只接受row/source，否则ValueError；[修前](../runs/ch07_11/before_boundaries/bootstrap_unknown_unit.stdout.json) / [修后](../runs/ch07_11/verified_boundaries/bootstrap_unknown_unit.stderr.txt)|
|R0711-03|10.7|resamples=0仍正常返回[null,null]区间|次数须为正整数；同时检查confidence范围；[修前](../runs/ch07_11/before_boundaries/bootstrap_zero_resamples.stdout.json) / [修后](../runs/ch07_11/verified_boundaries/bootstrap_zero_resamples.stderr.txt)|
|R0711-04|11.7|嵌套检测输入未检查重复编号，顶层unique检查未覆盖config.boxes|在detection与segmentation入口检查编号唯一，覆盖嵌套调用；[修前](../runs/ch07_11/before_boundaries/duplicate_nested_detection_id.stdout.json) / [修后](../runs/ch07_11/verified_boundaries/duplicate_nested_detection_id.stderr.txt)|
|R0711-05|11.8|空长尾表macro_recall除零崩溃，与零分母null约定不符|统一使用安全除法，空表宏召回与微准确率为null；[修前](../runs/ch07_11/before_boundaries/empty_longtail.stderr.txt) / [修后](../runs/ch07_11/verified_boundaries/empty_longtail.stdout.json)|
|R0711-06|8.8|评分器先int转换，非法预测1.7悄悄截成1并被接受|转换前检查严格0/1或CSV字符串0/1；[修前](../runs/ch07_11/before_boundaries/score_fractional_prediction.stdout.json) / [修后](../runs/ch07_11/verified_boundaries/score_fractional_prediction.stderr.txt)|
|R0711-07|10.4|非空短候选不足阶数时把零分母当零匹配|保留缺阶精确率null并将BLEU记null；空候选仍按声明记0；[修前](../runs/ch07_11/before_overlap_fix_boundaries/overlap_insufficient_order.stdout.json) / [修后](../runs/ch07_11/verified_boundaries/overlap_insufficient_order.stdout.json)|
|R0711-08|10.4|空参考仍接受并输出表面有效重叠分数|空参考ValueError，要求先检查材料；[修前](../runs/ch07_11/before_overlap_fix_boundaries/overlap_empty_reference.stdout.json) / [修后](../runs/ch07_11/verified_boundaries/overlap_empty_reference.stderr.txt)|
|R0711-09|7.6|不同来源的相同裸页号被误连为同一原页|page键使用(source_id或source,page)；来源缺失时不凭裸页号合组；[修前](../runs/ch07_11/before_page_fix_boundaries/page_number_scoped_by_source.stdout.json) / [修后](../runs/ch07_11/verified_boundaries/page_number_scoped_by_source.stdout.json)|

## 逐节复算结果

下表均为新版独立小例；正文旧例的样本量和输出不可替代它们。所有主命令退出码均为0。

|节|mode|主命令状态|关键独立核对 / 类型|
|---|---|---|---|
|7.1|`units`|EXECUTED_PASS|单位与必填项。合成输入或预置判断的计算；不据此证实历史结论|
|7.2|`derive`|EXECUTED_PASS|派生选择/input；派生选择/input_v2。合成输入或预置判断的计算；不据此证实历史结论|
|7.3|`missing`|EXECUTED_PASS|明确零与缺失。合成输入或预置判断的计算；不据此证实历史结论|
|7.4|`agreement`|EXECUTED_PASS|四条双人标签。合成输入或预置判断的计算；不据此证实历史结论|
|7.5|`coverage`|EXECUTED_PASS|覆盖漏斗。合成输入或预置判断的计算；不据此证实历史结论|
|7.6|`split`|EXECUTED_PASS|关联组闭包。合成输入或预置判断的计算；不据此证实历史结论|
|7.7|`card`|EXECUTED_PASS|卡片结构。卡片字段存在性检查，不是数据有效性认证|
|8.1|`baseline`|EXECUTED_PASS|关键词基线；全负类基线。合成输入或预置判断的计算；不据此证实历史结论|
|8.2|`matrix`|EXECUTED_PASS|组件(False, False)；组件(True, False)。合成输入或预置判断的计算；不据此证实历史结论|
|8.3|`ablation`|EXECUTED_PASS|组件(True, True)；组件(False, True)。合成输入或预置判断的计算；不据此证实历史结论|
|8.4|`config`|EXECUTED_PASS|顺序控制不变量。合成输入或预置判断的计算；不据此证实历史结论|
|8.5|`tracking`|EXECUTED_PASS|运行登记排除。合成输入或预置判断的计算；不据此证实历史结论|
|8.6|`literal`|EXECUTED_PASS|字面位置。合成输入或预置判断的计算；不据此证实历史结论|
|8.7|`join`|EXECUTED_PASS|按编号而非行序。合成输入或预置判断的计算；不据此证实历史结论|
|8.8|`independent`|EXECUTED_PASS|盲预测六句；独立评分计数。合成输入或预置判断的计算；不据此证实历史结论|
|9.1|`tasks`|EXECUTED_PASS|四类任务规格。人工任务规格展示，不是NLP任务执行|
|9.2|`tensor`|EXECUTED_PASS|张量长度/掩码；字表回取。合成输入或预置判断的计算；不据此证实历史结论|
|9.3|`baseline`|EXECUTED_PASS|关键词基线；全负类基线。合成输入或预置判断的计算；不据此证实历史结论|
|9.4|`vectors`|EXECUTED_PASS|三组余弦。合成输入或预置判断的计算；不据此证实历史结论|
|9.5|`benchmark`|EXECUTED_PASS|基准审读行数。基准审读模板，不是公开benchmark运行|
|9.6|`agreement`|EXECUTED_PASS|四条双人标签。合成输入或预置判断的计算；不据此证实历史结论|
|9.7|`multilingual`|EXECUTED_PASS|分语言正确数。合成输入或预置判断的计算；不据此证实历史结论|
|9.8|`coverage`|EXECUTED_PASS|覆盖漏斗。合成输入或预置判断的计算；不据此证实历史结论|
|10.1|`prompt`|EXECUTED_PASS|提示渲染。仅渲染提示，模型回答NOT_RUN|
|10.2|`fewshot`|EXECUTED_PASS|示例数与测试答案隔离。仅渲染few-shot提示，模型回答NOT_RUN|
|10.3|`sensitivity`|EXECUTED_PASS|预置敏感度计数。合成输入或预置判断的计算；不据此证实历史结论|
|10.4|`overlap`|EXECUTED_PASS|G01重叠；G02重叠。合成输入或预置判断的计算；不据此证实历史结论|
|10.5|`ratings`|EXECUTED_PASS|人工分维度争议。合成输入或预置判断的计算；不据此证实历史结论|
|10.6|`judge`|EXECUTED_PASS|预置judge一致率。合成输入或预置判断的计算；不据此证实历史结论|
|10.7|`bootstrap`|EXECUTED_PASS|来源组点估计；独立枚举来源重采样分布。合成输入或预置判断的计算；不据此证实历史结论|
|10.8|`mcnemar`|EXECUTED_PASS|不一致对与精确p。合成输入或预置判断的计算；不据此证实历史结论|
|10.9|`claims`|EXECUTED_PASS|断言预置裁决。合成输入或预置判断的计算；不据此证实历史结论|
|10.10|`card`|EXECUTED_PASS|卡片结构。应用/数据卡结构检查，不是模型实验|
|11.1|`vision_class`|EXECUTED_PASS|像素直接计数；距离分数与评价。合成输入或预置判断的计算；不据此证实历史结论|
|11.2|`detection`|EXECUTED_PASS|检测匹配与AP；参考支持类AP。合成输入或预置判断的计算；不据此证实历史结论|
|11.3|`segmentation`|EXECUTED_PASS|二值像素交并；含背景mIoU。合成输入或预置判断的计算；不据此证实历史结论|
|11.4|`architecture`|EXECUTED_PASS|patch与配对数。合成输入或预置判断的计算；不据此证实历史结论|
|11.5|`feature_eval`|EXECUTED_PASS|手设特征最近质心。合成输入或预置判断的计算；不据此证实历史结论|
|11.6|`benchmark`|EXECUTED_PASS|基准审读行数。基准映射模板，不是公开benchmark运行|
|11.7|`vision_metrics`|EXECUTED_PASS|检测匹配与AP；参考支持类AP。合成输入或预置判断的计算；不据此证实历史结论|
|11.8|`longtail`|EXECUTED_PASS|宏微分母。合成输入或预置判断的计算；不据此证实历史结论|
|11.9|`shift`|EXECUTED_PASS|分组拒识。合成输入或预置判断的计算；不据此证实历史结论|
|11.10|`vision_ablation`|EXECUTED_PASS|四格零差异。合成输入或预置判断的计算；不据此证实历史结论|

### 重要分母和零差异

- 7.4/9.6新版四条标签：一致率1/2，机会一致率5/16，κ=3/11；不是旧文十条或八条的κ。
- 8.1/9.3新版关键词：TP/FP/FN/TN=2/2/1/1，F1=4/7；四格最佳为6/6，但它们都是已见教学输入。
- 8.8预测入口去掉gold；在完全没有reference.csv的交接目录仍产生相同六条预测，评分者另算TP=3、TN=3。这里不是独立历史盲测。
- 10.7新版为六行、三个来源：B−A=1/6；seed=17、2000次来源组抽样区间[0,0.5]。独立枚举3³种来源抽样检查分布；不冒称三个来源足以支持总体推断。
- 11.2/11.7 AP仅平均有参考的seal类。D03/D04均FP，AP=1不等于无误检。分割前景IoU=3/4，背景=12/13，含背景均值87/104。
- 11.10四格均覆盖率/接受准确率/效用=1：四张都是实心矩形，填充率相同，最高分约0.982超过两门槛；没有观察到差异，不能套用旧文十二图表。

## 最终命令与退出码

实际绝对路径、工作目录、输入哈希及stdout/stderr见[最终manifest](../runs/ch07_11/verified/manifest.json)。下列命令为相对于review目录的可读形式；`--help`的stdout虽沿用.json扩展名保存，内容为帮助文本。

|节|命令|退出码|判断|
|---|---|---:|---|
|7.1|`python -B revision/附件/ch07/workbook.py --input revision/附件/ch07/7.1/input.json`|0|EXECUTED_PASS|
|7.2|`python -B revision/附件/ch07/workbook.py --input revision/附件/ch07/7.2/input.json`|0|EXECUTED_PASS|
|7.2|`python -B revision/附件/ch07/workbook.py --input revision/附件/ch07/7.2/input_v2.json`|0|EXECUTED_PASS|
|7.3|`python -B revision/附件/ch07/workbook.py --input revision/附件/ch07/7.3/input.json`|0|EXECUTED_PASS|
|7.4|`python -B revision/附件/ch07/workbook.py --input revision/附件/ch07/7.4/input.json`|0|EXECUTED_PASS|
|7.5|`python -B revision/附件/ch07/workbook.py --input revision/附件/ch07/7.5/input.json`|0|EXECUTED_PASS|
|7.6|`python -B revision/附件/ch07/workbook.py --input revision/附件/ch07/7.6/input.json`|0|EXECUTED_PASS|
|7.7|`python -B revision/附件/ch07/workbook.py --input revision/附件/ch07/7.7/input.json`|0|EXECUTED_PASS|
|8.1|`python -B revision/附件/ch08/workbook.py --input revision/附件/ch08/8.1/input.json`|0|EXECUTED_PASS|
|8.2|`python -B revision/附件/ch08/workbook.py --input revision/附件/ch08/8.2/input.json`|0|EXECUTED_PASS|
|8.3|`python -B revision/附件/ch08/workbook.py --input revision/附件/ch08/8.3/input.json`|0|EXECUTED_PASS|
|8.4|`python -B revision/附件/ch08/workbook.py --input revision/附件/ch08/8.4/input.json`|0|EXECUTED_PASS|
|8.4|`python -B revision/附件/ch08/workbook.py --input revision/附件/ch08/8.4/input_reverse_sort.json`|0|EXECUTED_PASS|
|8.4|`python -B revision/附件/ch08/workbook.py --input revision/附件/ch08/8.4/input_reverse_unsorted.json`|0|EXECUTED_PASS|
|8.4|`python -B revision/附件/ch08/workbook.py --input revision/附件/ch08/8.4/input_seed29.json`|0|EXECUTED_PASS|
|8.5|`python -B revision/附件/ch08/workbook.py --input revision/附件/ch08/8.5/input.json`|0|EXECUTED_PASS|
|8.6|`python -B revision/附件/ch08/workbook.py --input revision/附件/ch08/8.6/input.json`|0|EXECUTED_PASS|
|8.7|`python -B revision/附件/ch08/workbook.py --input revision/附件/ch08/8.7/input.json`|0|EXECUTED_PASS|
|8.7|`python -B revision/附件/ch08/workbook.py --input revision/附件/ch08/8.7/regression_duplicate_input.json`|1|EXECUTED_PASS（预期拒绝坏输入）|
|8.7|`python -B revision/附件/ch08/workbook.py --input revision/附件/ch08/8.7/regression_missing_input.json`|1|EXECUTED_PASS（预期拒绝坏输入）|
|8.8|`python -B revision/附件/ch08/workbook.py --input revision/附件/ch08/8.8/input.json`|0|EXECUTED_PASS|
|9.1|`python -B revision/附件/ch09/workbook.py --input revision/附件/ch09/9.1/input.json`|0|EXECUTED_PASS|
|9.2|`python -B revision/附件/ch09/workbook.py --input revision/附件/ch09/9.2/input.json`|0|EXECUTED_PASS|
|9.3|`python -B revision/附件/ch09/workbook.py --input revision/附件/ch09/9.3/input.json`|0|EXECUTED_PASS|
|9.4|`python -B revision/附件/ch09/workbook.py --input revision/附件/ch09/9.4/input.json`|0|EXECUTED_PASS|
|9.5|`python -B revision/附件/ch09/workbook.py --input revision/附件/ch09/9.5/input.json`|0|EXECUTED_PASS|
|9.6|`python -B revision/附件/ch09/workbook.py --input revision/附件/ch09/9.6/input.json`|0|EXECUTED_PASS|
|9.7|`python -B revision/附件/ch09/workbook.py --input revision/附件/ch09/9.7/input.json`|0|EXECUTED_PASS|
|9.8|`python -B revision/附件/ch09/workbook.py --input revision/附件/ch09/9.8/input.json`|0|EXECUTED_PASS|
|10.1|`python -B revision/附件/ch10/workbook.py --input revision/附件/ch10/10.1/input.json`|0|EXECUTED_PASS|
|10.2|`python -B revision/附件/ch10/workbook.py --input revision/附件/ch10/10.2/input.json`|0|EXECUTED_PASS|
|10.3|`python -B revision/附件/ch10/workbook.py --input revision/附件/ch10/10.3/input.json`|0|EXECUTED_PASS|
|10.4|`python -B revision/附件/ch10/workbook.py --input revision/附件/ch10/10.4/input.json`|0|EXECUTED_PASS|
|10.5|`python -B revision/附件/ch10/workbook.py --input revision/附件/ch10/10.5/input.json`|0|EXECUTED_PASS|
|10.6|`python -B revision/附件/ch10/workbook.py --input revision/附件/ch10/10.6/input.json`|0|EXECUTED_PASS|
|10.7|`python -B revision/附件/ch10/workbook.py --input revision/附件/ch10/10.7/input.json`|0|EXECUTED_PASS|
|10.8|`python -B revision/附件/ch10/workbook.py --input revision/附件/ch10/10.8/input.json`|0|EXECUTED_PASS|
|10.9|`python -B revision/附件/ch10/workbook.py --input revision/附件/ch10/10.9/input.json`|0|EXECUTED_PASS|
|10.10|`python -B revision/附件/ch10/workbook.py --input revision/附件/ch10/10.10/input.json`|0|EXECUTED_PASS|
|11.1|`python -B revision/附件/ch11/workbook.py --input revision/附件/ch11/11.1/input.json`|0|EXECUTED_PASS|
|11.2|`python -B revision/附件/ch11/workbook.py --input revision/附件/ch11/11.2/input.json`|0|EXECUTED_PASS|
|11.3|`python -B revision/附件/ch11/workbook.py --input revision/附件/ch11/11.3/input.json`|0|EXECUTED_PASS|
|11.4|`python -B revision/附件/ch11/workbook.py --input revision/附件/ch11/11.4/input.json`|0|EXECUTED_PASS|
|11.5|`python -B revision/附件/ch11/workbook.py --input revision/附件/ch11/11.5/input.json`|0|EXECUTED_PASS|
|11.6|`python -B revision/附件/ch11/workbook.py --input revision/附件/ch11/11.6/input.json`|0|EXECUTED_PASS|
|11.7|`python -B revision/附件/ch11/workbook.py --input revision/附件/ch11/11.7/input.json`|0|EXECUTED_PASS|
|11.8|`python -B revision/附件/ch11/workbook.py --input revision/附件/ch11/11.8/input.json`|0|EXECUTED_PASS|
|11.9|`python -B revision/附件/ch11/workbook.py --input revision/附件/ch11/11.9/input.json`|0|EXECUTED_PASS|
|11.10|`python -B revision/附件/ch11/workbook.py --input revision/附件/ch11/11.10/input.json`|0|EXECUTED_PASS|
|8.8|`python -B revision/附件/ch08/8.8/score_predictions.py --predictions runs/ch07_11/verified/8.8__input.stdout.json --reference revision/附件/ch08/8.8/reference.csv`|0|EXECUTED_PASS|
|7|`python -B revision/附件/ch07/workbook.py --help`|0|EXECUTED_PASS|
|8|`python -B revision/附件/ch08/workbook.py --help`|0|EXECUTED_PASS|
|9|`python -B revision/附件/ch09/workbook.py --help`|0|EXECUTED_PASS|
|10|`python -B revision/附件/ch10/workbook.py --help`|0|EXECUTED_PASS|
|11|`python -B revision/附件/ch11/workbook.py --help`|0|EXECUTED_PASS|
|8.8|`python -B revision/附件/ch08/8.8/score_predictions.py --help`|0|EXECUTED_PASS|
|8.8|`python -B revision/附件/ch08/8.8/score_predictions.py --predictions runs/ch07_11/verified/8.8_score_duplicate.input.json --reference revision/附件/ch08/8.8/reference.csv`|1|EXECUTED_PASS（预期拒绝坏输入）|
|8.8|`python -B revision/附件/ch08/8.8/score_predictions.py --predictions runs/ch07_11/verified/8.8_score_missing.input.json --reference revision/附件/ch08/8.8/reference.csv`|1|EXECUTED_PASS（预期拒绝坏输入）|
|8.8|`python -B runs/ch07_11/blind_handoff_verified/workbook.py --input runs/ch07_11/blind_handoff_verified/input.json`|0|EXECUTED_PASS|
|8.4|`python -B revision/附件/ch08/workbook.py --input revision/附件/ch08/8.4/input.json`|0|EXECUTED_PASS|
|8.4|`python -B revision/附件/ch08/workbook.py --input revision/附件/ch08/8.4/input.json`|0|EXECUTED_PASS|

## 独立核对的方法与未跑边界

- [独立计算器](../runs/ch07_11/independent_calculator.py)不导入任何workbook函数：逐句手判、直接像素计数、独立点积/分式与来源分布枚举；[107项结果](../runs/ch07_11/independent_verified.json)。
- [正文算术计算器](../runs/ch07_11/body_arithmetic.py)直接从正文显示的数据/文字复算：Cohen κ、字符长度及跨度、BLEU、Wilson、6⁶=46656种bootstrap枚举、二元序列枚举McNemar、AP/mIoU、宏微F1和四格差中差；[54项结果](../runs/ch07_11/body_arithmetic.json)。
- [31项最终边界](../runs/ch07_11/verified_boundaries/manifest.json)覆盖空分母、标签范围、缺值、重复/缺号、传递关联、书号页号、示例来源重叠、重采样单位与次数、短文本阶数及拒识。
- **BLOCKED：**旧模型调用、旧TF-IDF129维词表及相似度、旧十七张/十二张PGM实验等，缺旧完整输入/输出链条；没有伪造旧附件，也没有用新例替代。正文公开汇总可检查算术，却不能证明原实验确实发生。
- **NON_RUNNING_TEMPLATE / NOT_RUN：**空白工作表、结果模板、实际人工仲裁、模型回答、DINOv2真实特征、SAM推理、公开benchmark仍未执行。配置与教学追踪行内的NOT_RUN指它们原对象，不被本次检查器运行全局翻成成功。

## 修改与保存

仅修改revision/附件/ch07—ch11下 **111个** 相关文件：修复共享代码和8.8入口/评分器、更新实际运行的输入状态、README与逐章执行记录。空白结果模板未伪填，旧baseline未覆盖。

[逐文件diff](recompute_ch07_11.diff)；[完整机器报告](recompute_ch07_11.json)。全部初次运行与分阶段失败日志留在`runs/ch07_11/before*`，最终结果留在`verified*`。

最终完整性核对：[记录](../runs/ch07_11/final_integrity.json)。54份基线输入/脚本字节与首轮记录一致；6个当前脚本哈希匹配最终执行；38种mode全部有对应节输入；111个附件改动文件哈希及全部日志存在性已核验。

# 第 8 章原引用补核报告

**结果：20/20 项已核到相关段落并支持所引主张；18 项直接核读，2 项复用本轮独立核验证据。未发现本范围内需改正文的引证错误。**

核查日期：2026-10-30。仅补核原清单中的 20 个未核 URL；原已核项目不重计。未改正文、他人清单，不安装依赖、不执行案例、不外发。

## 判定边界

- 按 revision/正文/ch08.md 中实际引用的主张核查，不以网页可达代替内容支持。
- 已核仅表示方法/API 定义得到支持，不证明旧稿案例曾运行，不证明教学资料具有真实史料或独立盲测性质。
- Python 字符串同页的 4 个锚点分别对照具体主张，页面内容复用而非重复算作不同文献。
- cross_validation 与 common_pitfalls 复用 reports/sources_ch07_supplement.json 的 S07-18、S07-19；已读取该报告并逐项比对第 8 章主张。
- 以下行号指本次修订正文快照；网页行号与具体证据、版本、边界详见同名 JSON。

## 逐项结果

| ID | 正文行 | 原引用 | 核读位置 | 核查方式 | 结论 |
| --- | --- | --- | --- | --- | --- |
| S08-SUP-01 | 35 | [accuracy_score — scikit-learn 官方文档](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html) | normalize 参数及 Returns，网页行 655—669 | 直接核相关段 | 支持所引主张 |
| S08-SUP-02 | 39 | [f1_score — scikit-learn 官方文档](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html) | 开头公式与 binary 说明，网页行 635—643 | 直接核相关段 | 支持所引主张 |
| S08-SUP-03 | 49 | [DummyClassifier — scikit-learn 官方文档](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html) | 导言、strategy 参数及示例，网页行 638—656、714—726 | 直接核相关段 | 支持所引主张 |
| S08-SUP-04 | 112 | [NIST/SEMATECH 5.3.1 What are the objectives?](https://www.itl.nist.gov/div898/handbook/pri/section3/pri31.htm) | 5.3.1 开头与结尾，网页行 6—7、24—28 | 直接核相关段 | 支持所引主张 |
| S08-SUP-05 | 114, 714 | [Cross-validation — scikit-learn 官方文档](https://scikit-learn.org/stable/modules/cross_validation.html) | §3.1 开头，网页行 74、99—106（协作核对记录） | 本轮同主张证据复用 | 支持所引主张 |
| S08-SUP-06 | 134 | [Python 3.12 Built-in Types：序列与字符串](https://docs.python.org/3.12/library/stdtypes.html#common-sequence-operations) | Common Sequence Operations 表及注 4；Text Sequence Type — str，网页行 420—421、454—455、634—650 | 直接核相关段 | 支持所引主张 |
| S08-SUP-07 | 140 | [NIST/SEMATECH 5.3.3.3 Full factorial designs](https://www.itl.nist.gov/div898/handbook/pri/section3/pri333.htm) | 5.3.3.3 定义及 Table 3.2，网页行 8—11 | 直接核相关段 | 支持所引主张 |
| S08-SUP-08 | 345 | [YAML 1.2.2 规范](https://yaml.org/spec/1.2.2/) | 历史说明、§6.1、§7.4.2 映射值说明，网页行 165、1516—1550、3002—3003 | 直接核相关段 | 支持所引主张 |
| S08-SUP-09 | 345 | [Python 3.12 json](https://docs.python.org/3.12/library/json.html) | 导言示例后的 Note 与 Basic Usage，网页行 99—110 | 直接核相关段 | 支持所引主张 |
| S08-SUP-10 | 370 | [PyTorch 2.9 Reproducibility](https://docs.pytorch.org/docs/2.9/notes/randomness.html) | 开头两段，网页行 68—71 | 直接核相关段 | 支持所引主张 |
| S08-SUP-11 | 396 | [MLflow Tracking 官方文档](https://mlflow.org/docs/latest/ml/tracking/) | 导言、Concepts—Runs、Experiments，网页行 37—60 | 直接核相关段 | 支持所引主张 |
| S08-SUP-12 | 422 | [Python 3.12 Built-in Exceptions](https://docs.python.org/3.12/library/exceptions.html#FileNotFoundError) | FileNotFoundError 定义，网页行 417—420 | 直接核相关段 | 支持所引主张 |
| S08-SUP-13 | 469, 732 | [Common pitfalls — Data leakage 官方文档](https://scikit-learn.org/stable/common_pitfalls.html#data-leakage) | §12.2 Data leakage，网页行 122—141（协作核对记录） | 本轮同主张证据复用 | 支持所引主张 |
| S08-SUP-14 | 497 | [GitHub Copilot Best practices](https://docs.github.com/en/copilot/get-started/best-practices) | Create thoughtful prompts；Check Copilot's work，网页行 65—79 | 直接核相关段 | 支持所引主张 |
| S08-SUP-15 | 507, 525 | [Python 3.12 Built-in Types：str.find](https://docs.python.org/3.12/library/stdtypes.html#str.find) | Common Sequence Operations、Text Sequence Type—str、str.find，网页行 420、455、636、722—725 | 直接核相关段 | 支持所引主张 |
| S08-SUP-16 | 553 | [Python 3.12 unittest](https://docs.python.org/3.12/library/unittest.html) | test case 定义及 Basic example，网页行 15—18、72—79 | 直接核相关段 | 支持所引主张 |
| S08-SUP-17 | 620 | [Python 3.12 Built-in Types：Text Sequence Type — str](https://docs.python.org/3.12/library/stdtypes.html#text-sequence-type-str) | Text Sequence Type — str，网页行 634—650 | 直接核相关段 | 支持所引主张 |
| S08-SUP-18 | 622 | [Python 3.12 Built-in Types：str.strip](https://docs.python.org/3.12/library/stdtypes.html#str.strip) | str.strip 定义、示例及外端说明，网页行 1002—1013 | 直接核相关段 | 支持所引主张 |
| S08-SUP-19 | 639 | [The Debugging Book：Manual Input Reduction](https://www.debuggingbook.org/html/DeltaDebugger.html#Manual-Input-Reduction) | Manual Input Reduction 开头与二分缩减说明，网页行 238—264 | 直接核相关段 | 支持所引主张 |
| S08-SUP-20 | 666 | [Django 5.2：Writing your first contribution](https://docs.djangoproject.com/en/5.2/intro/contributing/#writing-some-tests-for-your-ticket) | Writing some tests for your ticket；Running Django’s test suite for the second time，网页行 213—217、278—280 | 直接核相关段 | 支持所引主张 |

## 需保留的限制

- GitHub 只支持拆分任务、给示例与审查测试；正文的“三遍阅读”是教学安排，并非官方规定。
- Python 文档只支持字符串/API 与异常含义；例如 FileNotFoundError 定义本身不能证明 E03 运行过。
- Django 回归测试通过不等于不存在全部缺陷；正文未作这种扩张。
- 滚动 stable/latest 文档反映本次核读页面，不冒称为旧稿 2026-10-24 的网页快照。

详细证据：sources_ch08_supplement.json。

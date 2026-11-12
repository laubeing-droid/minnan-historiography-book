# 第12章来源与用途

以下页面于2026年10月30日查阅。仅使用官方项目、作者资料或软件官方文档支持方法与入口说明，没有从这些入口抽取历史数值。正文中的资料辨析与教学流程为针对本书问题所作的具体设计，不冒称各来源已经验证闽南材料的适用性。

## 真实资料入口

1. [Harvard-Yenching Library Chinese Maritime Customs](https://archive.blogs.harvard.edu/yenching/?p=190)：确认海关数字化项目所含统计、规章与相关报告类型。没有引用具体年度港口数字。
2. [CHGIS How To](https://chgis.fas.harvard.edu/pages/howto/)：时间有效性、时间切片与历史对象变化的真实设计例。没有下载边界数据或进行地理叠置。
3. [NOAA GHCN-Daily Readme](https://www.ncei.noaa.gov/pub/data/ghcn/daily/readme.txt)：测量、质量、来源标志与缺失编码的字段实例。没有取得或运行气象观测数据。

## 任务与标准数据族

4. [ETDataset官方仓库](https://github.com/zhouhaoyi/ETDataset)：电力变压器相关预测数据说明。没有复现其基准成绩。
5. [UCR Time Series Classification Archive](https://www.cs.ucr.edu/~eamonn/time_series_data_2018/)：时序分类档案说明。
6. [Time Series Classification Website](https://www.timeseriesclassification.com/)：UCR与UEA分类集合入口。没有把其标签作为历史分类依据。

## 诊断 变换与时间评价

7. [Forecasting Principles and Practice 第3版 图形章节](https://otexts.com/fpp3/graphics.html)：时间图、滞后图、自相关与趋势季节结构。
8. [Forecasting Principles and Practice 第3版 ARIMA章节](https://otexts.com/fpp3/arima.html)：平稳性、差分、单位根与模型候选关系。
9. [Forecasting Principles and Practice 第3版 分解章节](https://otexts.com/fpp3/decomposition.html)：趋势、季节、余项与STL。
10. [Forecasting Principles and Practice 第3版 缺失与异常](https://otexts.com/fpp3/missing-outliers.html)：不同方法处理缺失的适用差异。
11. [Forecasting Principles and Practice 第3版 时间序列交叉验证](https://otexts.com/fpp3/toolbox.html#time-series-cross-validation)：移动预测原点与多步评价。
12. [statsmodels ACF](https://www.statsmodels.org/stable/generated/statsmodels.tsa.stattools.acf.html)：参数与缺失处理选项。
13. [statsmodels PACF](https://www.statsmodels.org/stable/generated/statsmodels.tsa.stattools.pacf.html)：偏自相关估计方法与滞后参数。
14. [statsmodels ADF](https://www.statsmodels.org/stable/generated/statsmodels.tsa.stattools.adfuller.html)：单位根原假设、确定性项与滞后选择。
15. [statsmodels KPSS](https://www.statsmodels.org/stable/generated/statsmodels.tsa.stattools.kpss.html)：水平或趋势平稳原假设及带宽规则。
16. [statsmodels STL](https://www.statsmodels.org/stable/generated/statsmodels.tsa.seasonal.STL.html)：周期、平滑器与稳健参数的区别。
17. [pandas时间序列文档](https://pandas.pydata.org/docs/user_guide/timeseries.html)：时期、时点、重采样区间与标签。
18. [scikit-learn常见陷阱](https://scikit-learn.org/stable/common_pitfalls.html)：训练内预处理与泄漏隔离。
19. [scikit-learn时间特征工程](https://scikit-learn.org/stable/auto_examples/applications/plot_cyclical_feature_engineering.html)：周期特征编码的选择。

软件官方页面可能随版本更新。本附件的预处理代码只依赖Python标准库，没有假定上述库已经安装，也没有执行这些库的统计接口。

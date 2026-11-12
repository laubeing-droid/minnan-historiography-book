# 第12至17章独立校对报告

已逐节完整核读 **41节**。正文未发现确定需要改正的教学算式或数值；修订 **18处输入与功能说明不一致**，另修 **45处行内数学定界符**。本报告不等同于外部来源全文审查或真实历史数据验证。

原任务编号为第9—17章；总协调者后将第9—11章移交另一位独立校对者。本代理未改这三章，也不把它们登记为已全文读完。

## 已修正的确定问题

- **14.2配套范围**：检查点实际位于同一个 `input.json` 的 `check` 字段；已附运行情景只有 `base` 与 `wrong_G4`，不是两种错点情景。聚集点、近共线情景改写为扩展练习；裸共线坐标提示不冒充完整运行输入。未附地图不再称为“读者包的示意地图”。
- **14.3—14.4与15.1—15.6图表说明**：实际工作流交付CSV/JSON，不生成正文若干处原先声称的SVG、总览图或流程图。保留作者的图表教学要求，明确它们属于读者后续制作，不把未实现功能写成当前输出，也不把扰动练习写成已通过的自动测试。
- **第12章行内数学**：按总协调者指示，只把45处明显数学的普通圆括号换为 `\( … \)`；不改普通中文括号、块公式或任何公式内容。逆替换后与基线逐字相同，断言通过；尚未作渲染器视觉验收。

改动仅在修订副本 `正文/ch12.md`、`ch14.md`、`ch15.md`。只读基线未被本代理写入，未修改附件，未增依赖。逐处旧文/新文/理由见 `proofread_ch09_17_changes.json`；对应差异为 `proofread_ch12.diff`、`proofread_ch14.diff`、`proofread_ch15.diff`。

## 全文覆盖

| 章 | 节数 | 阅读状态 |
|---|---:|---|
| 12 | 9 | 全文逐节读完 |
| 13 | 10 | 全文逐节读完 |
| 14 | 5 | 全文逐节读完 |
| 15 | 6 | 全文逐节读完 |
| 16 | 5 | 全文逐节读完 |
| 17 | 6 | 全文逐节读完 |

每节起止行、具体核查内容、修订数量均在 `proofread_ch09_17.json`，不是用目录扫描或关键词检索替代全文阅读。

## 保留的合理内容与跨章关系

原稿对模拟与历史观察、预测与解释、候选与确认、不可得与缺失、错误与未定义的区分总体清楚，不以空泛保守语删除作者的教学判断。重点检查并保留：

- 第12章年度输入与第13章四期周期例彼此独立；字段适配不制造季节性或补齐缺失。
- 第13.7节已公布测试结果不被第13.10节重新包装成新盲测；各种分母、共同可评分集合与失败任务分别保留。
- 第14.1及16.4节整数年闭区间，与第14.4节左闭右开区间之间已有明确转换条件。
- 第14.4节共边多候选与第15.5节半开方格唯一归属用途不同，不能直接互换。
- 第16章P编号实例与第17章A—H网络是独立练习，不拼成真实闽南样本；网络位置不自动证明信息控制或因果机制。

## 来源核查与未核项目

共识别96个去除片段锚点后的外部引用页面，全部已按本章实际所引主张尝试核对：**93项相关段落支持（含2项注明支持范围），3项访问阻塞，0项未尝试**。原先75项未重开清单现已逐项结束：72项支持、3项阻塞，具体主张、段落定位和结果保存在 `proofread_sources_followup.json`；主JSON的 `unverified_sources` 仅保留3项访问阻塞。QGIS两个主机的同版页面仍按原URL登记，不冒充两份独立研究。

本轮相关段落核查包括：

- 第12章真实资料入口确为海关数字化文献项目；ADF与KPSS的原假设方向与正文一致。[哈佛燕京项目](https://archive.blogs.harvard.edu/yenching/?p=190)、[ADF](https://www.statsmodels.org/stable/generated/statsmodels.tsa.stattools.adfuller.html)、[KPSS](https://www.statsmodels.org/stable/generated/statsmodels.tsa.stattools.kpss.html)
- 第13章经验CRPS和fair估计的分母区别有直接文档支持；官方当前DM接口存在，不能因旧版记忆而删除。[CRPS估计形式](https://scoringrules.readthedocs.io/en/latest/crps_estimators.html)、[Diebold–Mariano接口](https://www.statsmodels.org/stable/generated/statsmodels.tsa.stattools.diebold_mariano_test.html)
- 第14章像元角点/中心、GeoJSON轴序、时间版本与位置范围叙述有相关官方依据。[GDAL](https://gdal.org/en/stable/tutorials/geotransforms_tut.html)、[RFC 7946](https://www.rfc-editor.org/rfc/rfc7946.html)、[CHGIS](https://chgis.fas.harvard.edu/pages/database/)、[GBIF定位指南](https://docs.gbif.org/georeferencing-best-practices/1.0/en/)
- 第15章共同结构加权与MAUP区分有对应官方说明。[苏格兰人口普查标准化](https://www.scotlandscensus.gov.uk/about/2022-census/statistical-methodology/age-standardisation/)、[Esri MAUP定义](https://support.esri.com/en-us/gis-dictionary/modifiable-areal-unit-problem)
- 第16章修订追踪、码点和跨度、未知/开放端点及共享事件投影的口径可核。[PROV](https://www.w3.org/TR/prov-primer/)、[Web Annotation](https://www.w3.org/TR/annotation-model/)、[EDTF](https://www.loc.gov/standards/datetime/)、[二模加权投影](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.bipartite.projection.weighted_projected_graph.html)
- 第17章介数、修正接近中心性、模块度与Louvain随机次序叙述与官方相应定义一致。[介数](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.centrality.betweenness_centrality.html)、[接近中心性](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.centrality.closeness_centrality.html)、[模块度](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.community.quality.modularity.html)、[Louvain](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.community.louvain.louvain_communities.html)

补核确认：13.3的新水平Holt–Winters季节更新是原教材明确列出的另一γ约定，不是公式错；13.5的M4 OWA与官方R代码“先聚合再求相对比”的实现相符；17.1关于中心/孤立受网络边界限制的叙述与Lemercier原文直接对应。[Holt–Winters两种参数约定](https://otexts.com/fpp3/exponential-smoothing.html)、[M4官方R代码](https://github.com/Mcompetitions/M4-methods/blob/master/Benchmarks%20and%20Evaluation.R)、[Lemercier原文](https://transnationalhistory.net/interconnected/wp-content/uploads/2015/05/Lemlercier-Networks.pdf)

本轮未读取的3个原目标及原因：

|目标|访问结果|准确边界|
|---|---|---|
|[M5正式版DOI](https://doi.org/10.1016/j.ijforecast.2021.11.013)|403 Forbidden|已核另引作者预印本和官方竞赛指南，不冒称正式版正文已核|
|[Gneiting等校准与锐度原PDF](https://sites.stat.washington.edu/raftery/Research/PDF/Gneiting2007jrssb.pdf)|400 Timeout|保留合理叙述，标记此目标原文未核|
|[国会图书馆史料问题教学页](https://blogs.loc.gov/teachers/2012/03/primary-source-analysis-tool-forming-good-questions/)|403 Forbidden|不把页面无法访问解释为原主张错误|

以上失败均未重复请求或绕过访问限制。另有两项支持范围说明：`info_criteria`页直接列AIC等公式，不列AICc选项，正文没有声称该函数直接输出AICc；SARIMAX.fit页支持检查优化状态，而Holt–Winters具体`success`字段需结合脚本/实现，不由此单个链接包办证明。补核未产生新的确定正文修正，也没有因访问阻塞大幅改动作者观点。

以上只支持方法及资料入口，不证明虚构人物、事件或地点为史实；未核验真实历史原件，也未全读所有外部论文。

## 与本版复算的关系

本代理是正文独立校对者，计算由另一独立复算代理 `独立复核分组` 承担，不能把其运行摘要冒称本代理亲自执行。对照时区分三层：原正文手算/给定教学例、2026-10-30新编附件输入、本轮实际运行输出。

已收到的独立核算确认包括第17.4节877种非孤立点划分、γ=2唯一最优 `ABC;DE;FG` 和Q=−5/64；第17.5节补BE后D原始介数7/2、F归一化介数5/21；第14.2节基准检查RMSE=5。这些与正文相容，不需要为了制造勘误而改数字。正式运行证据和后续边界修复以该复算代理的报告与日志为准。

原书 `NOT_RUN` 记录的是编制交付时的状态，本次没有把它们全局替换为“已验证”。统计模型、可选Optuna、诊断图与真实数据适用性须分别报告；标准库基线运行成功不能替代它们。当前正文对未附图功能的修正不影响作者既有数学例或历史方法观点。


### 获准依赖安装后的当前复算状态

已读取独立复算代理的[当前报告](ch12_17_recomputation.md)，证据命令见 `../runs/ch12_17/commands.jsonl`。隔离环境的statsmodels 0.15.0与Optuna 5.0.0均已实际运行，累计1106条独立/边界/窗口/可选模型断言通过。验证15/15次计划拟合成功，按协议锁定Holt–Winters后测试MAE为0.2604804161；Optuna8次trial只评价验证，未运行最终测试。此处是复算报告的明确归属摘要，不冒称本校对代理亲自执行。

这些成绩属于新编人工输入，不是旧60期数据或原模型结果的恢复；ARIMA/SARIMA的残差Ljung–Box显著，不能以运行成功认定白噪声适配。第12章未实现的诊断、13.10刻意留空的测试与Optuna未评价的最终测试仍各自保留边界。原正文中的历史`NOT_RUN`不全局翻转，读者应同时查阅本轮验收入口。

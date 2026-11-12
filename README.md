# minnan-historiography-book · 《一种闽南文史的未来》书稿工程

[简体中文](README.md) | [English](README.en.md)

> 《一种闽南文史的未来：基于人工智能与现代研究方法》——23 章 156 节结构目标、约 35 万字的方法论书稿：
> 本仓库收录其**写作稿、历史版本、首轮校订复算记录与章节代码工作区**。在建，不是已完成著作。

**文档导航**：[研究立场声明](docs/POSITION.md) · [仓库结构与章节工作区](docs/STRUCTURE.md) · [范围与局限](docs/SCOPE_AND_LIMITS.md) · [项目历史](docs/PROJECT_HISTORY.md) · [贡献指南](CONTRIBUTING.md) · [更新日志](CHANGELOG.md)
**新增配套**：[研究方法](docs/METHODOLOGY.md) · [当前缺件](docs/MISSING_ITEMS.md) · [材料与状态](docs/DATA_AND_STATUS.md) · [复核指南](docs/REVIEW_GUIDE.md) · [来源与引用](docs/SOURCES_AND_CITATION.md) · [术语](docs/GLOSSARY.md) · [读者附件索引](manuscript/读者附件总索引.md)
**接手史档**：迁移说明原样见 [`handover/`](handover/从这里开始.md)（未改写）
**姊妹库**：[minnan-spanish-corpus](https://github.com/laubeing-droid/minnan-spanish-corpus) —— 22 源闽南—西班牙双语文献语料库（本书史料工程的文献底座之一）

---

## 1. 这是一本什么书

以闽南（漳泉厦及相关的台湾、潮汕、海外移民社会）为试验场，写**AI 时代地方文史研究的完整方法**：
从问题定义、文献检索与知识库、数据集与标注、统计与时序基线、时空与网络分析，
到研究自动化、图表论证、学术核查——最后落到人的判断、价值判断、景观社会与 AI 信息回流的风险反思。

结构目标（非验收结果）：概念与学术史约 10%，史料底座、具体方法与综合案例约 75%，人的判断与风险反思约 15%。

## 2. 仓库导览

| 路径 | 内容 | 性质 |
| --- | --- | --- |
| `manuscript/` | 全文写作稿完整包（2026-10-30）：正文 23 章 + 附件 23 套 + 代码示例 | 写作主线，授权修订留记录 |
| `round1_review/` | 首轮校订与复算版完整包：平行正文 + 校对复算记录（runs / reports / logs） | 档案层，原样保全 |
| `variants/` | 历史版本实文件55件（不是126件）（原稿、编校修订稿、单章草稿） | 档案层，原样保全 |
| `plans/` | 方案与候选稿实文件63件（含v1.0 / v1.2） | 档案层，原样保全 |
| `chapters/` | **章节工作区（活代码层）**：每章 code / data / results 与提升协议 | 可写层 |
| `handover/` | 迁移接手史档：从这里开始、交付范围、缺件表、实交清单 | 档案层，未改写 |
| `docs/` | 立场声明、结构说明、范围与局限、项目历史 | 配套 |

写作主线、历史档案与活代码层分离：**书稿附件里的代码是教材示例（多数标 NOT_RUN），不冒充可运行管线**；
后续推进在 `chapters/` 按[提升协议](chapters/README.md)进行。

## 3. 快速上手（阅读顺序）

1. [docs/POSITION.md](docs/POSITION.md) —— 作者研究立场（广义文化观、实践衰减四阶段、景观化批判、AI 判断权）
2. [manuscript/从这里开始.md](manuscript/从这里开始.md) 与 [manuscript/全书目录.md](manuscript/全书目录.md)
3. 正文 [manuscript/正文/](manuscript/正文/)；章代码推进见 [chapters/README.md](chapters/README.md) 索引表
4. 两版正文差异（20/24 章不同）：以 `manuscript/`（全文写作稿）为写作主线，`round1_review/` 为首轮校订平行版，**不混接成一套"终稿"**

## 4. 状态（诚实口径）

- **在建**。23 章 156 节、约 35 万字、10／75／15 是**结构目标**，不是验收结果。
- 第12章旧编校Page受限未取回；主线已有9节新写正文和13件附件，不能混称为原件恢复——见[范围与局限](docs/SCOPE_AND_LIMITS.md)。
- 复算与校对按作者 2026-10-28 决定**暂停**，优先完成全文与附件；未复算、未校对处如实标注，NOT_RUN / NOT_EXECUTED 标记保留。
- 文件存在、字数达标、保存成功均不等于独立复核完成。
- 原始讨论对话（作者观点原话）**不入库**，仅发布脱敏后的[研究立场声明](docs/POSITION.md)。

## 5. 许可

- 书稿正文、附件、文档：**[CC BY-NC-SA 4.0](LICENSE)**——署名、**禁止商用**、相同方式共享。
- 章节工作区代码：同一协议（CC BY-NC-SA 4.0）。

## 6. 引用

```bibtex
@misc{minnan_historiography_book_2026,
  title  = {minnan-historiography-book: 《一种闽南文史的未来》书稿、历史版本与章节代码工作区},
  author = {laubeing-droid},
  year   = {2026},
  url    = {https://github.com/laubeing-droid/minnan-historiography-book},
  note   = {CC BY-NC-SA 4.0；在建书稿存档，非已完成著作}
}
```

# 第6章工作区 · chunk Embedding BM25 与 RAG 检索增强

> 本章工作区属于**活代码层**：供后续把章内方法推进为可运行、可验证的代码。
> 书稿附件里的代码是**教材示例**（多数标 NOT_RUN / NOT_EXECUTED），二者不混用。

## 档案位置（只读，勿改）

| 层 | 位置 |
| --- | --- |
| 正文 | `manuscript/正文/ch06.md`（校订版平行件：`round1_review/正文/ch06.md`） |
| 附件 | `manuscript/附件/ch06/`（json×8、py×5、md×4、csv×2） |
| 历史版本 | `第6章 chunk Embedding BM25与RAG检索增强_31ef1d9c.md`、`第6章 检索增强与方法比较 写作草稿 未校对_7c4e8237.md`、`第6章 检索增强与方法比较 编校修订稿_3cbd6d25.md` |
| 复算记录 | `round1_review/校对复算记录/runs/ch05_06_19_23/` |

## 工作区约定

- `code/` 从附件提升或新写的可运行代码。提升时在文件头加来源注释（原附件路径 + 提升日期）。
- `data/` 本章示例与真实史料数据；真实史料须登记来源与权属，教学虚构数据须标注 `teaching/`。
- `results/` 运行产物；重跑产生覆盖时保留旧版或写明差异，不静默覆盖结论。
- 状态如实：未运行写 **NOT_RUN**；未复核不称完成。协议见[章节工作区总说明](../README.md)。

## 当前状态

- [ ] 附件代码清点与提升
- [ ] 依赖与环境登记（`code/requirements.txt`）
- [ ] 首次可运行验证
- [ ] 结果与书稿正文数字核对

## 2026-11-12 指定模型教学执行

新增 `code/embeddinggemma2_compare.py`：Google `google/embeddinggemma-2`的纯文本本地适配，使用模型专用检索提示，不冒称原BGE/E5分支已通过。实跑结果、安装过程和权重SHA见[执行审计](../../docs/CODE_EXECUTION_AUDIT.md)。权重不入Git；真实史料复算仍暂停。

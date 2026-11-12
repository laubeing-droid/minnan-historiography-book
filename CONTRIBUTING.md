# 贡献指南 / Contributing

> 语言：中文为主，Issue 可用中文或 English。

---

## 1. 这个仓库接受什么贡献

| 类型 | 方式 |
| --- | --- |
| **章代码推进**（最需要） | 按 [`chapters/README.md`](chapters/README.md) 提升协议，把某章附件代码做成可运行、可验证的管线，结果与正文数字核对 |
| 正文勘误 | Issue 附章、节、原文引文与依据；有来源的史实纠错优先 |
| 教学示例与真实证据的分辨 | 指出附件中教学虚构数据被误当真实史料之处 |
| 立场商榷 | 对 [docs/POSITION.md](docs/POSITION.md) 的论点提出学术商榷（附文献依据） |
| 结构改进 | 章节工作区协议、索引表的改进建议 |

## 2. 硬边界

1. **禁止商用**：本库为 CC BY-NC-SA 4.0，贡献一经合并即同协议发布。
2. **档案层只读**：`manuscript/`、`round1_review/`、`variants/`、`plans/`、`handover/` 不接受修改 PR——勘误走 Issue，由维护方登记，不改历史档案。
3. **写作权归属**：正文续写与修订由作者本人推进；外部贡献不直接改正文。
4. **状态如实**：`chapters/` 的贡献未运行写 NOT_RUN，未复核不称完成；教学虚构数据放 `data/teaching/` 并标注，不得冒充真实史料。
5. **两版正文不混接**：`manuscript/` 与 `round1_review/` 是平行版本，不接受"合成终稿"式贡献。
6. **隐私边界**：不要在 Issue/PR 中粘贴作者私人对话、Slack 记录或任何内部凭据类内容。

## 3. Issue 规范

标题格式：`[chXX] 一句话`，如 `[ch13] 滑窗回测基期与正文数字不符`。
正文须含：章号、具体位置、现状、你的依据（可复现步骤 / 文献 / 图证）。

## 4. 章代码贡献流程

1. 从 [`chapters/README.md`](chapters/README.md) 索引表选章（状态"待清点"者优先）；
2. 按[提升协议](chapters/README.md)把附件代码复制进 `chapters/chXX/code/`（头注来源与日期）；
3. 登记依赖（`code/requirements.txt`），运行并把产物写入 `results/`；
4. 与正文数字核对后在章 README 勾选状态；开 PR 说明与正文的差异；
5. 维护方复核后合入，贡献者进入 README 致谢（首个实质贡献后增设）。

## 5. 致谢

实质性贡献者（章代码推进、史实勘误、立场商榷、结构修复）将记入 README 致谢节与
[docs/PROJECT_HISTORY.md](docs/PROJECT_HISTORY.md)。

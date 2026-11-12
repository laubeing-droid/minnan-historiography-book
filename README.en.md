# minnan-historiography-book · *A Future of Minnan Historiography* (book project)

[简体中文](README.md) | [English](README.en.md)

> *A Future of Minnan Historiography: AI and Modern Research Methods* — a methods book
> with a 23-chapter / 156-section target structure (~350k Chinese characters).
> This repository holds its **draft manuscript, historical variants, first-round
> collation & recomputation records, and per-chapter code workspaces**. Work in
> progress — **not a finished book**.

**Docs**: [Research Position Statement](docs/POSITION.md#english-summary) · [Repo structure & chapter workspaces](docs/STRUCTURE.md) · [Scope & limits](docs/SCOPE_AND_LIMITS.md) · [Project history](docs/PROJECT_HISTORY.md) · [Contributing](CONTRIBUTING.md) · [Changelog](CHANGELOG.md)
**Expanded Chinese documentation**: [full documentation index](docs/INDEX.md), [reader guide](docs/READING_GUIDE.md), [research significance](docs/SIGNIFICANCE.md), [research programme](docs/RESEARCH_PROGRAMME.md). English expansion update pending.
**Core Chinese documentation**: [current missing-items ledger](docs/MISSING_ITEMS.md), [methodology](docs/METHODOLOGY.md), [material/status rules](docs/DATA_AND_STATUS.md), [review guide](docs/REVIEW_GUIDE.md), [sources](docs/SOURCES_AND_CITATION.md), [glossary](docs/GLOSSARY.md), [reader attachments](manuscript/读者附件总索引.md). Translation update pending.
**Handover archive**: migration notes published as-is under [`handover/`](handover/) (unrewritten, Chinese).
**Sister repo**: [minnan-spanish-corpus](https://github.com/laubeing-droid/minnan-spanish-corpus) — 22-source Minnan–Spanish bilingual corpus (one of the source bases of this project).

---

## 1. What this book is about

Using Minnan (Zhangzhou–Quanzhou–Xiamen, and related communities in Taiwan, Teochew, and the diaspora) as a testbed, the book writes out **a complete methodology for local historical research in the AI era**: problem definition, literature retrieval and knowledge bases, datasets and annotation, statistical and time-series baselines, spatial-temporal and network analysis, research automation, charting and argumentation, academic verification — closing with human judgment, value judgment, the society of the spectacle, and the risks of AI information feedback loops.

Target structure (a target, not an acceptance result): ~10% concepts & historiography, ~75% source base, concrete methods, synthesis & full case studies, ~15% human judgment, spectacularization & AI-risk reflection.

## 2. Repository layout

| Path | Contents | Layer |
| --- | --- | --- |
| `manuscript/` | Full writing draft package (2026-10-30): 23-chapter body + 23 attachment sets + code examples | Writing line; authorized revisions are recorded |
| `round1_review/` | First-round collation & recomputation package: parallel body + run/report logs | Archive, as-is |
| `variants/` | 55 actual historical-version files (originals, edited revisions, per-chapter drafts) | Archive, as-is |
| `plans/` | 63 plan and candidate-draft files | Archive, as-is |
| `chapters/` | **Chapter workspaces (live code layer)**: per-chapter code / data / results + promotion protocol | Writable |
| `handover/` | Migration handover archive: read-me, scope, missing-items list, inventories | Archive, as-is |
| `docs/` | Position statement, structure, scope & limits, project history | Facade |

The writing line, preserved archives, and live code are separated: **code inside manuscript attachments is teaching material (mostly marked NOT_RUN) and does not pretend to be a runnable pipeline**. Ongoing work happens in `chapters/` under the [promotion protocol](chapters/README.md).

## 3. Quick start (reading order)

1. [docs/POSITION.md](docs/POSITION.md#english-summary) — the author's research positions (broad-culture view, four-stage practice decay, spectacle critique, human judgment rights over AI)
2. [manuscript/从这里开始.md](manuscript/从这里开始.md) and [manuscript/全书目录.md](manuscript/全书目录.md) (Chinese)
3. Body text under [manuscript/正文/](manuscript/正文/); per-chapter code work starts from the index table in [chapters/README.md](chapters/README.md)
4. The two parallel bodies differ in 20 of 24 files: `manuscript/` (writing line) is primary, `round1_review/` is the first-round collated parallel — **they are never merged into a fake "final" version**

## 4. Status (honest framing)

- **In progress.** 23 chapters / 156 sections / ~350k chars / the 10–75–15 split are *targets*, not acceptance results.
- The old edited Chapter 12 page remains access-restricted; the writing line already contains a newly written nine-section chapter and 13 attachments, not a recovery of that old page — see [Scope & limits](docs/SCOPE_AND_LIMITS.md).
- Recomputation and collation are **paused** per the author's 2026-10-28 decision, prioritizing completing the full text and attachments; un-recomputed and un-collated passages are marked as such; NOT_RUN / NOT_EXECUTED markers are preserved.
- File existence, word counts, and successful saves do not equal independent verification.
- The author's original discussion dialogues are **not published**; only the de-identified [Research Position Statement](docs/POSITION.md) is.

## 5. License

All content — manuscript, attachments, docs, workspace code — is released under
**[CC BY-NC-SA 4.0](LICENSE)**: attribution, **non-commercial**, share-alike.

## 6. Citation

```bibtex
@misc{minnan_historiography_book_2026,
  title  = {minnan-historiography-book: draft, variants and chapter code workspaces for ``A Future of Minnan Historiography''},
  author = {laubeing-droid},
  year   = {2026},
  url    = {https://github.com/laubeing-droid/minnan-historiography-book},
  note   = {CC BY-NC-SA 4.0; archive of a book in progress, not a finished work}
}
```

# Entry 2 Documentation & Workshop Finish Report

**Date:** 12 November 2026  
**Branch:** `codex/entry02-workshop-progress` (in `/home/andy/projects/promptpraxis`)  
**Status:** All modifications completed locally; uncommitted and unpushed as instructed.

---

## 1. Modified & Created Files

### Article & Companion Tutorials
- `entries/entry-02/draft.md`: Updated Part 4 (unified AWCF example, Track A conversational prompts, Track B command, relative links) and verified Part 5. Winnie's Parts 1–3 preserved intact.
- `entries/entry-02/candidate-short.md`: **Newly created** standalone shortened candidate draft (1,512 words, ≤1,550 ceiling) for Winnie and Simon to review.
- `workshop/README.md`: Rewritten companion guide with unified AWCF example, prerequisites, Track A/B distinctions, offline test instructions, and Zotero GUI pause note.
- `workshop/prompts/beginner-pack.md`: Rewritten Track B beginner guide with Levels 1–3, parameter customization, error recovery, offline fixtures, and empty email flag.
- `workshop/prompts/track-a-prompts.md`: Rewritten Track A conversational prompts (Steps A1–A5) with planning contract, query, CSV save, BibTeX/RIS export, and periodic scheduling.
- `workshop/fetch_literature.py`: Updated CLI argument defaults to `--topic "automated written corrective feedback" --year 2024 --sort relevance --limit 5 --email=""`.

### Sample Data & Evidence
- `workshop/sample-data/sample-found.csv`: Updated with authentic dual-track output from 12 Nov 2026.
- `workshop/sample-data/sample-found.bib`: Updated with authentic 5 BibTeX records.
- `workshop/sample-data/sample-found.ris`: Updated with authentic 5 RIS records.
- `workshop/sample-data/README.md`: **Newly created** metadata documentation for the offline sample data.

### Editorial & Review Documentation
- `docs/winnie-part3-alignment.md`: Updated with concrete replacement recommendations for Winnie's Part 3, word count analysis, and counting methodology.
- `docs/simon-publication-handoff.md`: **Newly created** comprehensive publication handoff for Simon Wang (scope, verified capabilities, PR links vs post-merge links, limitations, and required decisions).
- `docs/progress-review.md`: Updated review snapshot categorizing items into Completed (已完成), Postponed (暂缓: "Andy 暂缓，后续安排"), and Pending Review (待审阅).

---

## 2. Word Count Statistics

| Document | Word Count (`wc -w`) | Target Budget | Notes |
|---|---|---|---|
| **Main Draft (`entries/entry-02/draft.md`)** | **2,497 words** | ~1,500 words | Full unabridged version with Winnie's complete Parts 1–3 and Andy's Part 4. |
| **Shortened Candidate (`entries/entry-02/candidate-short.md`)** | **1,512 words** | ≤ 1,550 words | **Meets budget.** Complete, independent streamlined draft for Winnie & Simon review. |

### Counting Scope & Methodology
- Calculated using standard POSIX `wc -w` across all markdown text in each file (including headings, tables, blockquotes, and code blocks).
- External linked files (`workshop/README.md`, `beginner-pack.md`, etc.) are linked resources and excluded from article word tallies.

---

## 3. Verification & Test Results

1. **Parameter & Naming Consistency:**
   - Topic: `automated written corrective feedback` across all 9 public and review documents.
   - Filter/Year: `2024` to present across all documents.
   - Sort Order: Default relevance ranking (omits OpenAlex URL sort parameter for best-match) across all documents.
   - Result Limit: `5` records across all documents.
   - Output Filenames: `found.csv`, `found.bib`, `found.ris` standardized throughout.
2. **Offline Workshop Tests (`workshop/tests/test_workshop.py`):**
   - **8/8 unit tests passed** in 1.42s (normal query, empty query, missing author/year metadata, live mock, escaped characters).
3. **Reference File Syntax Validation (`workshop/verify_zotero_import.py`):**
   - `workshop/sample-data/sample-found.bib`: **5/5 BibTeX entries parsed and passed**.
   - `workshop/sample-data/sample-found.ris`: **5/5 RIS records parsed and passed**.

---

## 4. Remaining Open Items & Simon Decisions

1. **Editorial Text Selection:** Simon Wang and Winnie Bo decide whether to adopt `candidate-short.md` (1,512 words) or manually apply the trims in `docs/winnie-part3-alignment.md` to `draft.md`.
2. **Live Desktop Zotero GUI Import:** Programmatic `.bib`/`.ris` syntax is verified; desktop application GUI import testing is explicitly marked as **"Andy 暂缓，后续安排"** and is not a blocker for Winnie.
3. **Demo Screenshots:** Capture images for Feedly setup, Zotero desktop, and WorkBuddy table outputs during WordPress media assembly.
4. **Git PR Merge & Publication:** Simon merges branch `codex/entry02-workshop-progress` into `main`, stages the post in WordPress, removes password protection, and publishes. (Zero destructive actions, software installations, or WordPress modifications were made locally).

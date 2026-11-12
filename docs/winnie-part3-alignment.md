# Proposed Alignment & Word Budget Pass for Winnie (Parts 1–3)

**From:** Andy Zheng (Co-author / Implementation Worker)  
**To:** Winnie Bo (Co-author, Owner of Parts 1–3)  
**cc:** Simon Wang  
**Date:** 12 November 2026  
**Context:** Prompt & Praxis Entry 2 (Issues #3, #6, #7, #9)

---

## 1. Respecting Ownership & Division of Labor

Per our agreed division of labor:
- **Winnie owns Parts 1–3:** Framing, narrative style, readability, and natural pedagogical prose aligned with Entry 1.
- **Andy owns Part 4 & companion materials:** The executable hands-on pipeline, beginner pack, sample data, and technical verification.

To respect your editorial ownership, **Parts 1–3 in the main draft (`entries/entry-02/draft.md`) have NOT been directly modified**. Instead, this document presents specific suggested text replacements to align Parts 1–3 with the verified live implementation in Part 4.

---

## 2. Specific Replacement Suggestions for Parts 1–3

### A. Unify the OpenAlex Query Example (Part 3)
- **Current Part 3 text:**
  ```text
  https://api.openalex.org/works?search=applied linguistics AI&per-page=3
  ```
  *(Returns 26,881 results on 8 November).*
- **Issue:** Part 4 has been standardized and verified on the topic **"automated written corrective feedback"** (2024 to present, 5 records, default relevance ranking, returning ~11,915 results on 12 Nov 2026). Switching topics between Part 3 and Part 4 may confuse readers trying the URL in Part 3 before reaching Part 4.
- **Proposed replacement in Part 3:**
  ```text
  https://api.openalex.org/works?search=automated+written+corrective+feedback&filter=from_publication_date:2024-01-01&per-page=5
  ```
  *Suggested narrative:*  
  > *"Five papers on automated written corrective feedback published since 2024, each with a DOI that opens the publisher landing page. The same query returned 11,915 matching results on 12 November. No search box, no scrolling, no tabs."*

### B. Literature Metadata vs. Full-Text PDFs (Part 3 Table)
- **Current Part 3 table text:**  
  *"The query returns a table: file it as CSV, into a reading list with Status and Notes, then into Zotero — record and PDF together"*
- **Issue:** OpenAlex provides bibliographic metadata and persistent DOIs, not direct full-text PDFs. Claiming that the API fetches "record and PDF together" is an unverified overstatement.
- **Proposed replacement in Part 3 table:**  
  > *"The query returns a table: file it as CSV, into a reading list with Status and Notes, then into Zotero via standard BibTeX/RIS import, with DOIs linking directly to publisher landing pages (a DOI proves a registered publication, not that every full-text PDF is open-access)."*

### C. Reading List Destination (Spreadsheet CSV vs Google Docs)
- **Previous Part 4 mentions:** Google Docs plugin.
- **Verified reality:** WorkBuddy runs cleanly with workspace-local files. The reading list is standard `found.csv` (with `OpenAlex_ID, Title, Authors, Year, Citations, DOI, Journal, Reading_Status, Notes`). It opens seamlessly in Microsoft Excel, Apple Numbers, Google Sheets, or Tencent Docs.
- **Proposed alignment:** Refer to a universal "spreadsheet reading list (CSV)" rather than a platform-specific Google Docs tab.

### D. Status of Zotero Desktop Import Verification
- Generating standard `found.bib` (BibTeX) and `found.ris` (RIS) reference files has been verified programmatically.
- Live desktop GUI import verification in the Zotero desktop application is currently marked as **"Andy 暂缓，后续安排"** (postponed by Andy for subsequent arrangement). It is **not** a mandatory blocking task for Winnie at this stage.

---

## 3. Article Word Count Analysis & Counting Methodology

### Word Counting Methodology
- **Measurement Tool:** Standard POSIX `wc -w` on the markdown source.
- **Scope:** Includes all headings, narrative prose, code blocks, tables, and footnotes inside the article draft.
- **Exclusions:** External companion files (`workshop/README.md`, `beginner-pack.md`, `track-a-prompts.md`), which are linked as external repository resources so the main essay remains uncluttered.

### Current Main Draft (`entries/entry-02/draft.md`) Word Count
The current main draft totals **2,497 words** (`wc -w`), broken down as follows:

| Section | Current Words (`wc -w`) | Target Budget | Notes |
|---|---|---|---|
| **Header & Standfirst** | 127 | ~45 | Drop internal draft notes; keep Title and Standfirst |
| **Part 1 (Nature Column Problem)** | 162 | ~130 | Tighten Gosztyla laptop crash narrative |
| **Part 2 (Solutions without AI: RSS & Zotero)** | 552 | ~360 | Condense introductory narrative; keep Feedly & Zotero 5-min demos |
| **Part 3 (GUI vs API Boundary)** | 549 | ~340 | Streamline screen limits; keep OpenAlex URL demo & comparison table |
| **Part 4 (WorkBuddy Hands-on: Two Tracks)** | 747 | ~420 | Keep Track A 4-step prompts & Track B 1-line command; details in workshop/ |
| **Part 5 (Decisions, Limits, Value)** | 208 | ~140 | Sharp focus on limits (DOI proves provenance, not truth) |
| **Closing & Footnotes** | 152 | ~75 | Standard citations and companion links |
| **TOTAL** | **2,497** | **~1,500** | *Currently ~947 words over the 1,550-word ceiling* |

---

## 4. Independent Shortened Candidate Draft (`candidate-short.md`)

To assist you and Simon in reaching the target length (~1,500 words, hard ceiling ≤1,550 words) without altering your main draft, Andy has prepared a complete, standalone trimmed candidate:
- **Location:** [`entries/entry-02/candidate-short.md`](../entries/entry-02/candidate-short.md)
- **Word Count:** **1,512 words** (`wc -w`), strictly within the ≤1,550 ceiling.
- **Integrity:** It preserves all core narrative elements (Gosztyla's crash, RSS Feedly demo, Zotero demo, Entry 1 connection, OpenAlex URL demo, Track A 4-step prompts, Track B command, and limitations).
- **Status:** Candidate draft for discussion only; it does **not** overwrite `entries/entry-02/draft.md` and awaits review and approval from you and Simon.

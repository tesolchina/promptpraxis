# Proposed Alignment & Word Budget Pass for Winnie (Parts 1–3)

**From:** Andy Zheng (Co-author / Implementation Worker)  
**To:** Winnie Bo (Co-author, Owner of Parts 1–3)  
**cc:** Simon Wang  
**Date:** 11 November 2026  
**Context:** Prompt & Praxis Entry 2 (Issues #3, #6, #7, #9)

---

## 1. Respecting Ownership

Per Simon's division of labor in the 11 Nov meeting:
- **Winnie owns Parts 1–3:** Style pass, readability, and natural contextual prose aligned with Entry 1.
- **Andy owns Part 4:** The executable hands-on pipeline, beginner pack, and technical verification.

Part 4 has now been rewritten and verified with live code and automated tests. Below are the concrete alignment touchpoints and word-budget calculations to help you finalize Parts 1–3.

---

## 2. Key Alignment Points in Part 3

Part 3 sets up the theoretical rationale for the code that runs in Part 4. Two technical adjustments are needed in Part 3 to match the verified implementation:

### A. Literature Metadata vs. Full-Text PDFs (Part 3 Table)
- **Current Part 3 text:** *"The query returns a table: file it as CSV, into a reading list with Status and Notes, then into Zotero — record and PDF together"*
- **Observed reality & verified rule:** OpenAlex is a metadata registry, not a pirated full-text library. A DOI guarantees that the paper is real and registered, and resolves to the publisher's landing page (where open-access papers can be downloaded and paywalled papers require institutional access). OpenAlex does not directly deliver all publisher PDFs.
- **Proposed phrasing:**
  > *"The query returns a table: file it as CSV, into a reading list with Status and Notes, then into Zotero — record and DOI landing page together (a DOI proves a registered publication, not that every PDF is free)."*

### B. Persistent Reading List Destination (Universal CSV vs Google Docs)
- **Previous Part 4 draft mentioned:** *"Google Doc tab 'Reading list — your topic'"*
- **Observed reality in WorkBuddy:** Tencent WorkBuddy does not support Google Docs write access out of the box (it uses local files and Tencent Docs).
- **Aligned solution:** The primary reading list is `found.csv` (with `OpenAlex_ID, Title, Authors, Year, Citations, DOI, Journal, Reading_Status, Notes`). It opens seamlessly in Microsoft Excel, Apple Numbers, Google Sheets, or Tencent Docs. Part 3 should reference a "spreadsheet reading list" rather than a Google Docs plugin.

---

## 3. Assembled Entry Word Budget Plan (Issue #9)

Simon's target is **~1,500 words**, with a hard ceiling of **≤ 1,550 words** (`wc -w` on the assembled entry).

### Current Word Count Breakdown
- Header & Draft meta notes: 127 words
- Part 1 (Problem): 160 words
- Part 2 (Solutions without AI): 550 words
- Part 3 (GUI vs API): 547 words
- Part 4 (Rewritten hands-on): ~435 words
- Part 5 & Closing / Footnotes: 354 words
- **Current Total:** ~2,173 words (*~623 words over budget*)

### Proposed Trimming Target for ≤ 1,550 Words

| Section | Current (`wc -w`) | Target (`wc -w`) | Recommended Trim Approach |
|---|---|---|---|
| **Header / Standfirst** | 127 | ~45 | Drop drafting meta-notes into Git commit; keep Title and Standfirst. |
| **Part 1 (Nature Column)** | 160 | ~140 | Already crisp; minor tightening of Gosztyla crash narrative. |
| **Part 2 (RSS + Zotero)** | 550 | ~380 | Tighten introductory prose; preserve the 5-minute Feedly and Zotero demo callout boxes. |
| **Part 3 (GUI vs API)** | 547 | ~360 | Streamline the discussion of screen boundaries while keeping the OpenAlex URL demo and the comparison table. |
| **Part 4 (WorkBuddy)** | 487 | ~400 | Andy's verified rewrite (paste-ready prompts + runnable Track B command). Long setup moved to `workshop/README.md`. |
| **Part 5 (Decisions/Limits)**| 354 | ~200 | Tighten decisions and limits; emphasize that a DOI proves provenance, not truth. |
| **Closing & Footnotes** | ~100 | ~60 | Standard citations and companion code pointers. |
| **TOTAL** | **~2,173** | **~1,540** | **Meets Issue #9 Acceptance Criteria (≤ 1,550 words)** |

---

## 4. Word Counting Method

- **Command:** `wc -w entries/entry-02/draft.md`
- **Inclusions:** All article prose, headings, bullet points, and code snippets embedded in the draft.
- **Exclusions:** Companion repository files (`workshop/README.md`, `beginner-pack.md`), which are linked as external resources to keep the blog post fast and readable.

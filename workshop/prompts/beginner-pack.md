# Beginner Pack — Agentic Literature Management Pipeline (Track B)

This beginner pack accompanies **Prompt & Praxis Entry 2**: *Introduction to Agentic AI: a hands-on lesson for academic literature management*.

It provides instructions for running and customizing the standalone `workshop/fetch_literature.py` script to fetch literature metadata from OpenAlex, generate reading list CSVs, and export BibTeX/RIS reference files.

---

## 首次准备 (Prerequisites & Setup)

1. **Environment:** Python 3.8+ (or Tencent WorkBuddy / Cursor / VS Code with integrated terminal).
2. **Dependencies:** None — uses Python standard library modules (`urllib`, `json`, `csv`, `re`).
3. **Working Directory:** Open your terminal in the repository root or navigate to `workshop/`.
4. **Contact Email:** An email is optional. You may leave `--email=` blank for the standard pool, or provide your real institutional email for OpenAlex's polite pool. No fictitious email is required.

---

## Pipeline Overview

```
[OpenAlex Public API] 
       │
       ▼ (HTTP query with relevance ranking)
[fetch_literature.py]
       │
       ├──► found.csv  (Persistent reading list table with Status and Notes)
       ├──► found.bib  (Standard BibTeX for Zotero / LaTeX)
       └──► found.ris  (Standard RIS for reference managers)
```

---

## Instructions: The Three Levels

### Level 1 — First Run (As Printed)

**1. 输入提示词与命令 (Command):**  
Tell your AI agent (WorkBuddy):  
> *"Run `workshop/fetch_literature.py` to retrieve the 5 most relevant papers on automated written corrective feedback published since 2024."*

Or run directly in terminal:
```bash
python3 workshop/fetch_literature.py \
  --topic "automated written corrective feedback" \
  --year 2024 \
  --sort relevance \
  --limit 5 \
  --email=
```

**2. 预期结果 (Expected Outcome):**
- Terminal reports total matching papers in OpenAlex (~11,000+).
- Generates 3 files in your working folder: `found.csv`, `found.bib`, `found.ris`.
- Displays retrieved paper titles, publication years, and DOI URLs.

**3. 失败处理 (Troubleshooting):**
- **HTTP 429:** If encountering rate limits, supply your real academic email via `--email="your_name@institution.edu"` or wait briefly.
- **Offline Mode:** If offline, test using `--fixture workshop/tests/fixtures/openalex_normal.json`.

---

### Level 2 — Customize the Query

**1. 输入提示词与命令 (Command):**  
Edit parameters for your specific field:

```bash
python3 workshop/fetch_literature.py \
  --topic "second language acquisition" \
  --year 2025 \
  --sort "publication_date:desc" \
  --limit 5 \
  --email=
```

**2. 预期结果 (Expected Outcome):**
- Returns the 5 newest publications on the specified topic published since 2025.
- Files `found.csv`, `found.bib`, and `found.ris` are overwritten with the new results.

**3. Key Parameters:**
- `--topic`: Keywords or phrase (e.g., `"generative AI in higher education"`)
- `--year`: Earliest publication year (e.g., `2024`, `2025`)
- `--sort`: Ranking method (`relevance` for best matches, `cited_by_count:desc` for citation count, `publication_date:desc` for newest)
- `--limit`: Number of records (1–50, default `5`)
- `--email`: Optional contact email for polite pool

---

### Level 3 — Test Edge Cases & Recovery

In research, real queries can return empty sets or incomplete records. Test how the pipeline behaves:

#### 1. Empty Results
```bash
python3 workshop/fetch_literature.py --topic "xyznonexistenttopic999" --year 2026 --sort relevance --limit 5 --email=
```
- **Expected result:** Reports `0 records found`. Generates empty template files without hallucinating non-existent publications.

#### 2. Missing Metadata
Preprints and conference abstracts may lack registered DOIs or journal names.
- **Expected result:** Missing values remain empty fields; the pipeline never fabricates citations, DOIs, or author names.

#### 3. Network Disconnection
If internet connection drops:
- **Expected result:** Script halts gracefully with exit code `1`, logs `Network Connection Error`, and suggests checking connection or using `--fixture`.

---

## Reference Manager (Zotero) Import Note

To import into Zotero Desktop:
1. Open **Zotero Desktop**.
2. Click **File** → **Import...**
3. Select **A file (BibTeX, RIS, Zotero RDF, etc.)** → click **Next**.
4. Choose `found.bib` (or `found.ris`) from your working folder.
5. Select destination collection.

> [!NOTE]

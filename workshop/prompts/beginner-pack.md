# Beginner Pack — Agentic Literature Management Pipeline (Track B)

This beginner pack accompanies **Prompt & Praxis Entry 2**: *Introduction to Agentic AI: a hands-on lesson for academic literature management*.

It enables knowledge workers and researchers to fetch verified literature metadata directly from OpenAlex, inspect it in a reading list CSV, export importable BibTeX/RIS bibliographies, and import them cleanly into Zotero.

---

## Prerequisites

- **Python 3.8+** (or Tencent WorkBuddy / Cursor / VS Code with terminal support)
- No third-party packages required — uses standard library (`urllib`, `json`, `csv`, `re`)
- An email address for OpenAlex's polite pool (increases reliability)

---

## Pipeline Overview

```
[OpenAlex API] 
       │
       ▼ (live HTTP query with polite pool)
[fetch_literature.py]
       │
       ├──► found.csv  (Reading list table with Status and Notes)
       ├──► found.bib  (Standard BibTeX for Zotero / LaTeX)
       └──► found.ris  (Standard RIS for Zotero / EndNote / Mendeley)
```

---

## Instructions: The Three Levels

### Level 1 — First Run (As Printed)

Copy and run the base command in your terminal, or prompt your AI agent (WorkBuddy):

> *"Run the literature pipeline to find the 5 most-cited papers on applied linguistics AI published since 2024 using OpenAlex polite pool."*

**Direct Command:**
```bash
python3 fetch_literature.py \
  --topic "applied linguistics AI" \
  --year 2024 \
  --sort "cited_by_count:desc" \
  --limit 5 \
  --email "your.email@example.com"
```

**Expected Outcome:**
- Terminal prints count of total matching papers in OpenAlex (~130,000+).
- Outputs 3 files: `found.csv`, `found.bib`, `found.ris`.
- Displays top 3 paper titles and DOIs.

---

### Level 2 — Customize the Query

Edit the parameters to fit your own research area. Change the topic, year, or sort order.

> *"Find the 10 newest papers on second language acquisition published in 2025, sorted by publication date."*

**Direct Command:**
```bash
python3 fetch_literature.py \
  --topic "second language acquisition" \
  --year 2025 \
  --sort "publication_date:desc" \
  --limit 10 \
  --email "your.email@example.com"
```

**Key Parameters:**
- `--topic`: Any phrase (e.g., `"generative AI in higher education"`, `"corpus pragmatics"`)
- `--year`: Earliest year to include (e.g., `2024`, `2025`, `2026`)
- `--sort`: Sort criterion (`cited_by_count:desc` for impact; `publication_date:desc` for freshness)
- `--limit`: Number of entries (default: `10`)

---

### Level 3 — Test Edge Cases & Recovery

In research, real searches sometimes return zero results or papers with incomplete records. Test how the pipeline behaves under stress:

#### 1. Empty Results
```bash
python3 fetch_literature.py --topic "xyznonexistenttopic999" --year 2026
```
- **Expected result:** Reports `0 records found`. Generates empty templates without hallucinating or inventing non-existent publications.

#### 2. Missing Metadata
Some working papers or technical preprints do not have formal DOIs or source journals.
- **Expected result:** Missing values remain empty strings; the pipeline never fabricates a DOI or journal name.

#### 3. Network Disconnect
If the network drops or OpenAlex is unreachable:
- **Expected result:** Pipeline exits gracefully with error message and recovery advice: test offline using `--fixture tests/fixtures/openalex_normal.json`.

---

## Importing into Zotero

1. Open **Zotero Desktop**.
2. Click **File** → **Import...** (or press `Ctrl+Shift+I` / `Cmd+Shift+I`).
3. Select **A file (BibTeX, RIS, Zotero RDF, etc.)** → click **Next**.
4. Choose `found.bib` (or `found.ris`).
5. Choose **Place items into a new collection** → click **Next**.
6. All records land in your Zotero library, complete with titles, authors, years, journals, and clickable DOI URLs.

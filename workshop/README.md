# Prompt & Praxis Entry 2 — Literature Workshop Companion

Companion materials, runnable code, sample datasets, and prompt packs for **Prompt & Praxis Entry 2**: *Introduction to Agentic AI: a hands-on lesson for academic literature management*.

---

## Directory Map

```
workshop/
├── README.md                   # This companion guide
├── fetch_literature.py         # Standalone literature query & export script
├── verify_zotero_import.py     # Syntax and validator script for Zotero imports
├── prompts/
│   ├── beginner-pack.md        # Track B: Code reuse instructions (Levels 1–3)
│   └── track-a-prompts.md      # Track A: Step-by-step chat prompts for agents
├── sample-data/
│   ├── sample-found.csv        # Real reading list with Status and Notes
│   ├── sample-found.bib        # Verified BibTeX file importable into Zotero
│   └── sample-found.ris        # Verified RIS file importable into Zotero
├── tests/
│   ├── test_workshop.py        # Automated test suite (6 tests covering all flows)
│   └── fixtures/               # Offline fixtures (normal, empty, missing metadata)
├── assets/
│   └── screenshots/            # Verified captures and UI reference provenance
└── zotero-spike/               # Zotero module feasibility spike and formatter
```

---

## Quick Start (Terminal & WorkBuddy)

### Option 1: Direct Python Execution
```bash
# Query the 5 most-cited papers on applied linguistics AI since 2024
python3 fetch_literature.py \
  --topic "applied linguistics AI" \
  --year 2024 \
  --sort "cited_by_count:desc" \
  --limit 5 \
  --output-csv found.csv \
  --output-bib found.bib \
  --output-ris found.ris
```

### Option 2: Running Automated Tests
```bash
python3 tests/test_workshop.py
```

### Option 3: Validating Output for Zotero
```bash
python3 verify_zotero_import.py --bib found.bib --ris found.ris
```

---

## Tencent WorkBuddy Environment Notes

1. **Connector & Runtime Support:**
   - Tencent WorkBuddy bundles a portable Python and Node.js environment.
   - Scripts placed in the local workspace directory can be driven directly by WorkBuddy.
   - For chat-only execution, use the paste-ready prompts in `prompts/track-a-prompts.md`.
2. **File Handling:**
   - WorkBuddy returns tabular summaries in the chat window.
   - Persistent files (`found.csv`, `found.bib`) are saved to the current working folder.
3. **Office Integration:**
   - Do not assume direct Google Docs API write access. WorkBuddy natively supports local CSV files and Tencent Docs (TDoc).
   - `found.csv` opens seamlessly in Microsoft Excel, Apple Numbers, Google Sheets, and Tencent Docs.

---

## Troubleshooting & Recovery

| Issue | Symptom | Root Cause | Recovery Step |
|---|---|---|---|
| **HTTP 429 Rate Limit** | `HTTP Error 429: Too Many Requests` | OpenAlex shared IP pool budget reached | Provide your email with `--email your@domain.edu` to join OpenAlex's polite pool. |
| **0 Results Returned** | `0 matching records in database` | Overly narrow search keywords or future date | Broaden keywords or check publication year parameter. Script truthfully outputs empty template without hallucinating. |
| **Missing DOIs** | Some papers have no DOI in table | Working papers/preprints without registered DOIs | Expected behavior; pipeline preserves missing data. Check Open Access landing URL instead. |
| **Network Failure** | `URLError: <urlopen error ...>` | Local proxy / offline network | Use offline mode: `--fixture tests/fixtures/openalex_normal.json`. |
| **Zotero Import Parse Error** | Zotero reports invalid character | Malformed BibTeX / RIS | Run `python3 verify_zotero_import.py --bib <file>` to identify syntax issues. |

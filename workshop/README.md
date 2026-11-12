# Prompt & Praxis Entry 2 — Literature Workshop Companion

Companion materials, runnable code, sample datasets, and prompt packs for **Prompt & Praxis Entry 2**: *Introduction to Agentic AI: a hands-on lesson for academic literature management*.

---

## Directory Map

```
workshop/
├── README.md                   # This companion guide
├── fetch_literature.py         # Standalone literature query & export script (Track B)
├── verify_zotero_import.py     # Syntax and validator script for Zotero imports
├── prompts/
│   ├── beginner-pack.md        # Track B: Code reuse instructions (Levels 1–3)
│   └── track-a-prompts.md      # Track A: Step-by-step chat prompts for conversational agents
├── sample-data/
│   ├── README.md               # Provenance and query metadata (captured 12 Nov 2026)
│   ├── sample-found.csv        # Real reading list with Status and Notes (5 records)
│   ├── sample-found.bib        # Verified BibTeX file formatted for Zotero / reference tools
│   └── sample-found.ris        # Verified RIS file formatted for Zotero / reference tools
├── tests/
│   ├── test_workshop.py        # Automated test suite (7 offline tests and 1 live API test)
│   └── fixtures/               # Offline fixtures (normal, empty, missing metadata)
├── assets/
│   └── screenshots/            # Verified captures and UI reference provenance
└── zotero-spike/               # Experimental Zotero module feasibility spike and formatter
```

---

## Quick Start (Terminal & WorkBuddy)

### Option 1: Direct Python Execution (Track B)
Run the verified pipeline directly from the `workshop/` directory; from the repository root, run `cd workshop` first:

```bash
# Query the 5 most relevant papers on automated written corrective feedback since 2024
python3 fetch_literature.py \
  --topic "automated written corrective feedback" \
  --year 2024 \
  --sort relevance \
  --limit 5 \
  --email=
```

- **Output:** Creates `found.csv`, `found.bib`, and `found.ris` in your current working folder.
- **Parameters:**
  - `--topic`: Search terms (default: `"automated written corrective feedback"`).
  - `--year`: Earliest publication year (default: `2024`).
  - `--sort`: Ranking method (`relevance` uses OpenAlex default best-match order; also supports `cited_by_count:desc` and `publication_date:desc`).
  - `--limit`: Number of records (default: `5`, max: `50`).
  - `--email`: Optional contact email for OpenAlex polite pool. Leave empty (`--email=`) for standard pool (no fictitious email required).

### Option 2: Running Automated Tests (includes a live API request)
```bash
python3 tests/test_workshop.py
```

### Option 3: Validating Output Syntax
```bash
python3 verify_zotero_import.py --bib found.bib --ris found.ris
```

---

## Tencent WorkBuddy Environment Notes

1. **Two Distinct Tracks:**
   - **Track A (Conversational Agent):** Instruct your agent using the step-by-step prompts in `prompts/track-a-prompts.md`. The conversational agent interacts directly with the public OpenAlex API through its own environment; it does **not** read or execute `fetch_literature.py`.
   - **Track B (Code Reuse):** Instruct your agent or terminal to run `fetch_literature.py` as detailed in `prompts/beginner-pack.md`.
2. **Runtime & Paths:**
   - Our tested Windows WorkBuddy installation provided a Python environment; confirm an interpreter is available in your installation.
   - Run commands from your active workspace directory. Output files (`found.csv`, `found.bib`, `found.ris`) are saved in that same directory.
   - Avoid hardcoding machine-specific absolute paths; use relative file paths.
3. **Office Integration:**
   - The tested WorkBuddy environment wrote local files. Open the CSV in a spreadsheet application of your choice.
   - `found.csv` opens in Microsoft Excel, Apple Numbers, Google Sheets, or Tencent Docs.

---

## Troubleshooting & Recovery

| Issue | Symptom | Root Cause | Recovery Step |
|---|---|---|---|
| **HTTP 429 Rate Limit** | `HTTP Error 429: Too Many Requests` | OpenAlex shared IP pool rate limit reached | Stop and follow the service response or current access instructions; do not repeatedly retry. |
| **0 Results Returned** | `0 matching records in database` | Overly specific keywords or future date range | Broaden keywords or check the publication year. The pipeline outputs empty template files without inventing records. |
| **Missing Fields** | Some papers have no DOI, journal, or author | Working papers, preprints, or books lacking registered DOI/source in OpenAlex | Expected behavior; pipeline preserves missing data as blank fields rather than fabricating values. |
| **Network Disconnect** | `URLError: <urlopen error ...>` | Local proxy / offline network | Use offline mode: `--fixture tests/fixtures/openalex_normal.json`. |
| **Zotero Desktop Import** | Parser error on import | Malformed BibTeX / RIS syntax | Run `python3 verify_zotero_import.py --bib <file>` to verify citekey and brace balance.  |

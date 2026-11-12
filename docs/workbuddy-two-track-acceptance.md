# WorkBuddy Two-Track Acceptance Test Protocol (docs/workbuddy-two-track-acceptance.md)

**Worker:** AndyZHENG0715 (安 / Andy)  
**Date:** 12 November 2026, 00:48 HKT (UTC+8)  
**Target Topic:** `automated written corrective feedback` (From `docs/example-selection.md`)  
**Environment Baseline:** Windows Desktop + Tencent WorkBuddy AI (`v37.10.3-24`) accessing WSL UNC path.

---

## 1. Environment & Pre-Conditions

1. **Workspace Location:**
   - In Tencent WorkBuddy AI, open the workspace at the canonical WSL UNC path:
     ```text
     \\wsl.localhost\Ubuntu\home\andy\projects\promptpraxis
     ```
   - *(Do NOT use nonexistent drive letters like `E:\Projects\...`).*
2. **Verified Baseline (from `workshop/test-output/workbuddy-example-20261112-005622/acceptance.md`):**
   - **Host Runtime Verified:** Windows Python (`C:\Users\andy\.workbuddy-ai\binaries\python\versions\3.13.12\python.exe` / `Python 3.13.14`).
   - **UNC Access Verified:** WorkBuddy can read and write to `\\wsl.localhost\Ubuntu\home\andy\projects\promptpraxis`.
   - **Live OpenAlex Query Verified:** WorkBuddy executed a live GET query to OpenAlex returning HTTP 200 (83,957 bytes) without credentials, confirming default relevance ordering (`meta.x_query.order = "best matches first"`).
   - **Pending Verification:** Full end-to-end Track A and Track B execution; physical desktop Zotero import; full-text PDF access / paywalls.
3. **Operational Safeguards:**
   - **No Dependency Installations:** Do NOT run `pip install` or `npm install`. Use only the standard Python environment already available in Windows / WorkBuddy.
   - **No Source Modification:** Do NOT edit or overwrite existing source files in `workshop/` or `entries/`.
   - **No Sample Overwriting:** All outputs must be saved to dedicated, isolated acceptance folders:
     - Track A Output: `workshop/acceptance/track-a/`
     - Track B Output: `workshop/acceptance/track-b/`
   - **No Zotero Operation:** Do NOT attempt to launch or control desktop Zotero from WorkBuddy; Zotero verification is handled separately by human testing.

---

## 2. Track A — Natural Language Generation from Scratch

*Goal:* Verify whether WorkBuddy can independently formulate an API request to OpenAlex, inspect metadata, generate a reading list CSV, and produce BibTeX/RIS without reading or copying our existing script.

### Pre-test Folder Setup (WorkBuddy prompt or manual):
Ensure directory `workshop/acceptance/track-a/` exists.

### Step A1: The Contract Prompt (Planning)
**Paste this prompt directly into WorkBuddy chat:**

```text
I am new to agentic literature management. Before doing anything: tell me in three concise bullet points what this prompt would do, what information you need from me, and what could go wrong. Do not run any search or generate any code yet.

"Find 5 recent publications on automated written corrective feedback published since 2024 from OpenAlex, and show me Title, Year, Citations, and DOI."
```

- **Pass Criteria:** WorkBuddy replies with 3 planning points (e.g., query construction, email for polite pool, risk of rate-limiting/empty results) and pauses for confirmation.
- **Fail Criteria:** WorkBuddy runs terminal commands or outputs code immediately without waiting for confirmation.

---

### Step A2: The Verified Query & Table Prompt
**Paste this prompt directly into WorkBuddy chat:**

```text
Proceed with the search using OpenAlex's public Works API.
- Topic: automated written corrective feedback
- Published since: 2024
- Sort by: relevance (OpenAlex default search score; do not pass sort in URL)
- Number of results: 5

Strict constraints:
1. Do NOT read, reference, or execute "workshop/fetch_literature.py".
2. Do NOT copy or read files from "workshop/sample-data/".
3. Every row must come directly from your live API query to OpenAlex. Do not invent any publication or fill missing fields from memory.
4. If writing temporary execution code, execute it via Python standard library only (no pip dependencies).

Display the results as a Markdown table:
Title | Year | Citations | Venue | DOI
```

- **Pass Criteria:** WorkBuddy displays a table of 5 papers matching the topic (e.g. papers from *ReCALL*, *Humanities & Social Sciences Communications*, etc.).
- **Evidence to Save:** Chat transcript; raw API response; test clicking one DOI in a browser to confirm it resolves.

---

### Step A3: Reading List CSV & Bibliography Export Prompt
**Paste this prompt directly into WorkBuddy chat:**

```text
Save the 5 literature records to the following files inside "workshop/acceptance/track-a/":
1. "workshop/acceptance/track-a/found.csv" with columns:
   OpenAlex_ID, Title, Authors, Year, Citations, DOI, Journal, Reading_Status, Notes
   (Set Reading_Status to "Unread", leave Notes empty).
2. "workshop/acceptance/track-a/found.bib" (Valid BibTeX with unique author-year citekeys).
3. "workshop/acceptance/track-a/found.ris" (Valid RIS format).

Rules:
- Do not overwrite existing files in workshop/sample-data/.
- Preserve missing metadata: for publications without authors or DOIs, leave the CSV field empty ("") and omit the author field in BibTeX. Do not invent missing DOIs, authors, or abstracts.
- Create a short text file "workshop/acceptance/track-a/run_log.txt" recording the exact API URL used and timestamp.
```

- **Pass Criteria:** Files `found.csv`, `found.bib`, `found.ris`, and `run_log.txt` exist in `workshop/acceptance/track-a/`.
- **Failure Evidence to Record:** Error traceback; failed file path write; corrupted CSV format.

---

## 3. Track B — Reusing and Driving the Existing Pipeline

*Goal:* Verify whether WorkBuddy can inspect the existing documented script `workshop/fetch_literature.py`, explain it to a beginner, and execute it via the command line to a separate destination folder.

### Step B1: Explain the Existing Code
**Paste this prompt directly into WorkBuddy chat:**

```text
Inspect the local Python script located at "workshop/fetch_literature.py".
Do not run it yet. In plain language suitable for a non-programmer, explain:
1. What does this script do?
2. What are its required and optional parameters?
3. How does it handle missing metadata (such as papers without DOIs)?
```

- **Pass Criteria:** WorkBuddy correctly identifies the script's OpenAlex query flow, explains CLI arguments (`--topic`, `--year`, `--sort`, `--limit`, `--output-...`), and highlights that missing fields are preserved rather than hallucinated.

---

### Step B2: Execute the Script to Isolated Destination
**Paste this prompt directly into WorkBuddy chat:**

```text
Execute the local script "workshop/fetch_literature.py" using your terminal execution tool to find the 5 most relevant papers on "automated written corrective feedback" published since 2024 using relevance sorting.

Run parameters:
- Topic: "automated written corrective feedback"
- Year: 2024
- Sort: "relevance" (passes --sort relevance to omit the sort parameter from OpenAlex API request and use default relevance ranking)
- Limit: 5
- Output CSV: workshop/acceptance/track-b/found.csv
- Output BibTeX: workshop/acceptance/track-b/found.bib
- Output RIS: workshop/acceptance/track-b/found.ris

Command to execute:
python workshop/fetch_literature.py --topic "automated written corrective feedback" --year 2024 --sort relevance --limit 5 --output-csv workshop/acceptance/track-b/found.csv --output-bib workshop/acceptance/track-b/found.bib --output-ris workshop/acceptance/track-b/found.ris

Ensure the output directory "workshop/acceptance/track-b/" is created first. Do not touch or overwrite files in workshop/sample-data/ or workshop/acceptance/track-a/.
```

- **Pass Criteria:** WorkBuddy runs `python workshop/fetch_literature.py ...` successfully; terminal exits with code 0; outputs appear in `workshop/acceptance/track-b/`.
- **Failure Evidence to Record:** Python execution path errors (e.g. Python not found in Windows PATH); UNC path resolution failure; non-zero exit codes.

---

## 4. Cross-Track Verification & Data Consistency Check

After both tracks complete:

1. **Compare Records:**
   - Compare `workshop/acceptance/track-a/found.csv` with `workshop/acceptance/track-b/found.csv`.
   - **Consistency Expectation:** Both tracks should capture the same core publications on `automated written corrective feedback`.
   - **Variance Note:** If Track A and Track B are executed at different times or with slight differences in OpenAlex ranking weights, citation counts may fluctuate slightly (+1 citation) or record order may shift. **Byte-for-byte identical output is NOT required; conceptual and bibliographic integrity is required.**
2. **Inspect Artifact Integrity:**
   - Run the local validator against Track A and Track B outputs:
     ```bash
     python3 workshop/verify_zotero_import.py \
       --bib workshop/acceptance/track-a/found.bib \
       --ris workshop/acceptance/track-a/found.ris
     python3 workshop/verify_zotero_import.py \
       --bib workshop/acceptance/track-b/found.bib \
       --ris workshop/acceptance/track-b/found.ris
     ```
3. **UNC Path & Environment Fallback (if needed):**
   - *Note:* WorkBuddy has already demonstrated successful UNC path read/write and Python execution in `workshop/test-output/workbuddy-example-20261112-005622/acceptance.md`.
   - If Windows WorkBuddy fails to resolve `\\wsl.localhost\...` in multi-step sessions, log the exact error message.
   - *Fallback:* Copy `promptpraxis` to a native Windows directory (e.g. `C:\temp\promptpraxis`) and re-test, recording the workaround in `run_log.txt`.

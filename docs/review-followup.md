# Delivery Review & Self-Audit Follow-up (docs/review-followup.md)

**Worker:** AndyZHENG0715 (安 / Andy)  
**Date & Time:** 11 November 2026, 23:14 HKT (UTC+8)  
**Context:** Follow-up review incorporating Codex's spot-check feedback.  
**Operational Boundaries:** Zero feature expansion, zero new dependencies, no remote branch pushes, no external messages.

---

## 1. Resolution of Report Contradictions & Status Alignment

Per Codex's review, all contradictory or overstated statements across [`docs/andy-handoff.md`](andy-handoff.md), [`docs/zotero-remix-feasibility-recommendation.md`](zotero-remix-feasibility-recommendation.md), and [`entries/entry-02/draft.md`](../entries/entry-02/draft.md) have been systematically corrected:

1. **Retraction of "All Deliverables Completed":**
   - Deleted any claims that "all deliverables are completed."
   - The delivery is explicitly marked **INCOMPLETE**: local code, prompt drafts, offline tests, and review notes are staged as candidate proposals, but live WorkBuddy conversational rehearsal, fresh-account rehearsal, and physical desktop UI captures remain open.
2. **Separation of Live API Probe, 403 Policy Block, and Test SKIP:**
   - *Initial Probe (20:26 HKT):* Succeeded once over HTTPS, capturing 5 live 2024–2026 papers into `workshop/sample-data/`.
   - *Subsequent Egress Block (22:32 HKT):* Subsequent live requests failed with `HTTP Error 403: Forbidden ("Request to GET /works on api.openalex.org not allowed by policy")` under sandbox egress filtering.
   - *Test Suite Accounting:* `test_05_live_api_query` was **SKIPPED**. **This SKIP is strictly recorded as SKIPPED and is NOT counted as a PASS.**
3. **Deletion of Unverified WorkBuddy Claims:**
   - Deleted assertions such as "zero-install", "runs immediately", or "100% of workshop objective achieved in WorkBuddy".
   - Stated clearly: Linux WSL terminal success does NOT prove Windows WorkBuddy runnability.

---

## 2. Mock-Based Network Failure Test (test_04 Rewritten)

### Previous Defect
The previous `test_04` merely executed `urllib.request.urlopen("https://nonexistent-host...")` directly in the test body. It only proved that Python's standard library raises an exception when querying a non-existent domain; it did NOT test the application's code, error logging, or CLI exit handling.

### Corrective Implementation
Rewrote `test_04_network_failure_handling` in [`workshop/tests/test_workshop.py`](../workshop/tests/test_workshop.py) using `unittest.mock`:
1. **Mocking Network Call:** Patched `urllib.request.urlopen` with `mock_urlopen.side_effect = urllib.error.URLError("Temporary failure in name resolution")`. No real network connection is attempted.
2. **Testing Application Error Handling:**
   - Captured `sys.stderr` via `contextlib.redirect_stderr`.
   - Called `fetch_literature.query_openalex(...)`.
   - Verified that `urllib.error.URLError` is caught and re-raised, and asserted that user-facing recovery guidance (`"Network Connection Error"` and `"Recovery: Check internet connection or test with --fixture"`) is emitted to `stderr`.
3. **Testing CLI Main & Exit Code:**
   - Patched `sys.argv` with CLI arguments.
   - Ran `fetch_literature.main()` under mock.
   - Asserted that `SystemExit` is raised with exit code `1`, and verified `"Execution halted"` on `stderr`.

---

## 3. WorkBuddy Manual Acceptance Checklist (Corrected UNC Path & Pre-conditions)

> [!WARNING]
> **CRITICAL PRE-CONDITION:** The workshop materials have NOT been published to GitHub or merged to remote repositories. **Do NOT instruct WorkBuddy to fetch URLs from GitHub.** WorkBuddy must be pointed directly to the **local working directory**.

### Pre-conditions & Environment Warnings
1. **Host Workstation:** Windows desktop with Tencent WorkBuddy AI installed (`v37.10.3-24` or newer).
2. **Account:** Logged in with a test WeChat / QQ account.
3. **Workspace Path:**
   - **Correct Canonical UNC Path:** `\\wsl.localhost\Ubuntu\home\andy\projects\promptpraxis`
   - *(Note: Path `E:\Projects\promptpraxis` does not exist and has been removed).*
4. **WorkBuddy Host Capabilities Verified (Update via `workshop/test-output/workbuddy-example-20261112-005622/acceptance.md`):**
   - Windows WorkBuddy reading/writing to WSL UNC path (`\\wsl.localhost\Ubuntu\home\andy\projects\promptpraxis`) is **VERIFIED**.
   - WorkBuddy executing bundled Windows Python (`Python 3.13.14`) without path-escaping errors is **VERIFIED**.
   - WorkBuddy performing a live OpenAlex GET query returning HTTP 200 (83,957 bytes) without credentials is **VERIFIED**.
   - Full two-track (Track A conversational from scratch / Track B script execution with `--sort relevance`) and physical desktop Zotero import remain **UNVERIFIED**.

---

### Step-by-Step Test Procedure

#### Step 1: Track A — Conversational Planning (Contract Prompt)
- **Paste Prompt:**
  ```text
  I am new to agentic literature management. Before doing anything: tell me in three concise bullet points what this prompt would do, what information you need from me, and what could go wrong. Do not run any search yet.

  "Find the 10 most-cited papers on applied linguistics AI published since 2024 from OpenAlex, and show me Title, Year, Citations, and DOI."
  ```
- **Success Criteria:** WorkBuddy replies with 3 planning bullet points and asks for confirmation. It does NOT execute code or call the API yet.
- **Failure Evidence to Save:** Screenshot of premature code execution; chat text where planning was skipped.

#### Step 2: Track A — Verified Query Execution
- **Paste Prompt:**
  ```text
  Proceed with the search using OpenAlex's public Works API.
  - Topic: applied linguistics AI
  - Published since: 2024
  - Sort by: cited_by_count:desc
  - Number of results: 10
  - Polite pool mailto: your.email@example.com

  Format the results as a Markdown table with columns:
  Title | Year | Citations | DOI

  House rule: Every row must come directly from the OpenAlex API response. Do not invent or complete any row from memory. If the API returns fewer than 10 results or missing data, leave the fields empty and state so explicitly.
  ```
- **Success Criteria:** WorkBuddy displays a Markdown table with 10 real papers; clicking at least one DOI opens a live publisher/preprint landing page.
- **Failure Evidence to Save:** Error messages in chat; fabricated DOIs (404 on click); HTTP 429 rate limit errors.

#### Step 3: Track A — Persistent Reading List Generation
- **Paste Prompt:**
  ```text
  Save these search results as a CSV file named "workshop/sample-data/found.csv" with columns:
  OpenAlex_ID, Title, Authors, Year, Citations, DOI, Journal, Reading_Status, Notes

  Set Reading_Status to "Unread" for all rows, and leave Notes blank.
  ```
- **Success Criteria:** File `workshop/sample-data/found.csv` is created on disk; opens cleanly in Microsoft Excel or Tencent Docs with correct column headers and non-corrupted UTF-8 text.
- **Failure Evidence to Save:** Missing file on disk; garbled author characters; broken CSV commas.

#### Step 4: Track A — Zotero Export & Import Verification
- **Paste Prompt:**
  ```text
  Convert the literature records into a standard BibTeX file named "workshop/sample-data/found.bib".
  Ensure each entry has a unique citekey based on first author surname and year, and authors are separated by 'and'.
  ```
- **Success Criteria:** File `found.bib` generated on disk. Open **Zotero Desktop** -> `File` -> `Import...` -> select `found.bib`. All records populate a new collection with valid metadata.
- **Failure Evidence to Save:** Zotero import error dialog; malformed citekeys; syntax parsing failure.

#### Step 5: Track B — Reusing Local Code via UNC Path
- **Paste Prompt:**
  ```text
  Inspect the local script at "workshop/fetch_literature.py". Run it via your terminal tool to find the 5 most-cited papers on "applied linguistics AI" since 2024, saving output to "found_track_b.csv" and "found_track_b.bib".
  ```
- **Success Criteria:** WorkBuddy executes the local Python script without downloading anything from GitHub; outputs `found_track_b.csv` and `found_track_b.bib`.
- **Failure Evidence to Save:** Terminal tool execution error; Python runtime not found; UNC path resolution failure (`\\wsl.localhost\...`).

---

## 4. Freezing the Experimental Citation Formatter

1. **Development Frozen:**
   - No further feature expansion will be undertaken for [`workshop/zotero-spike/zotero_formatter.py`](../workshop/zotero-spike/zotero_formatter.py).
   - Retained strictly as an **experimental exploratory spike**.
2. **Not an Adopted Architecture:**
   - Neither `entries/entry-02/draft.md` nor `docs/zotero-remix-feasibility-recommendation.md` presents the fallback as decided.
   - Architectural selection (Option 1: standard external BibTeX/RIS export vs. Option 2: inline heuristic formatter) is preserved for Andy and Codex to decide.
3. **Licensing & Effort Disclaimers:**
   - Legal interpretations of AGPLv3 for internal consumption vs. distribution are marked as **pending verification**.
   - Upstream translator effort estimates (~2–3 weeks vs. 3–4 days) are marked as **rough engineering estimates (pending verification / 待核实)**, not established facts.

---

## 5. Actual Test Execution Evidence

All tests were executed directly in the sandboxed terminal.

### Command 1: Workshop Pipeline & Mock Failure Tests
```bash
python3 /home/andy/projects/promptpraxis/workshop/tests/test_workshop.py
```
- **Exit Code:** `0`
- **Output Summary:** `Ran 7 tests in 0.020s. OK (skipped=1)`
- **Breakdown:**
  - `test_01_fixture_normal_query`: **PASS** (Parses 3 fixture records, outputs CSV/Bib/RIS)
  - `test_02_fixture_empty_results`: **PASS** (Zero records, zero hallucinated rows)
  - `test_03_fixture_missing_metadata`: **PASS** (Preserves null DOIs and empty authors)
  - `test_04_network_failure_handling`: **PASS** (unittest.mock verifies URLError recovery guidance & SystemExit 1)
  - `test_05_live_api_query`: **SKIPPED** (OpenAlex HTTP 403 egress policy block detected; NOT counted as PASS)
  - `test_06_parameter_customization_track_b`: **PASS** (Offline fixture parameterization)
  - `test_07_special_characters_and_author_parsing`: **PASS** (Verifies `"Yang, An"` -> `Yang2025` and `%`/`&` escaping)
- **Total:** **6 PASS, 1 SKIPPED, 0 FAIL**

### Command 2: Experimental Citation Spike Unit Tests
```bash
python3 /home/andy/projects/promptpraxis/workshop/zotero-spike/test_zotero_spike.py
```
- **Exit Code:** `0`
- **Output Summary:** `Ran 5 tests in 0.001s. OK`
- **Result:** **5 PASS, 0 FAIL**

### Command 3: Zotero Import Syntax Validator
```bash
python3 /home/andy/projects/promptpraxis/workshop/verify_zotero_import.py \
  --bib /home/andy/projects/promptpraxis/workshop/sample-data/sample-found.bib \
  --ris /home/andy/projects/promptpraxis/workshop/sample-data/sample-found.ris
```
- **Exit Code:** `0`
- **Output Summary:**
  - `[PASS] BibTeX Verification Succeeded (3 records)`
  - `[PASS] RIS Verification Succeeded (3 records)`
- **Result:** **PASS (Syntax verification only; physical desktop import not performed).**

---

## 6. Remaining Issues & Pending Decisions

1. **Physical Desktop Verification:**
   - Tencent WorkBuddy GUI full two-track execution (Track A conversational from scratch and Track B script invocation with `--sort relevance`) remains to be run.
   - Physical desktop Zotero import (`File → Import...`) remains to be performed and confirmed in Zotero Standalone.
   - 7 desktop UI screenshots remain missing and must be captured on physical workstation per redaction guidelines.
2. **Collaborator Access & PR Routing:**
   - `tesolchina/procomm-microlearning` access is still 404. Simon must add `AndyZHENG0715` or confirm `promptpraxis` as the public home.
3. **Word Budget:**
   - Current draft stands at **2,235 words**. Winnie must execute WI-C trimming on Parts 1–3 to reach the ≤1,550 target.

---

## 7. Teaching Example Alignment, Relevance Sorting, and Missing Author Audit (Follow-up)

**Timestamp:** 12 November 2026, 01:55 HKT (UTC+8)

### 1. WorkBuddy Independent Report Findings (`workshop/test-output/workbuddy-example-20261112-005622/acceptance.md`)
- **Verified Host Capabilities:**
  - WorkBuddy executed bundled Windows Python (`Python 3.13.14`) from `C:\Users\andy\.workbuddy-ai\binaries\python\versions\3.13.12\python.exe`.
  - Read and wrote to the WSL UNC path `\\wsl.localhost\Ubuntu\home\andy\projects\promptpraxis`.
  - Executed a single live OpenAlex GET request returning HTTP 200 (83,957 bytes) without API key or credentials.
  - Confirmed OpenAlex default ranking behavior: omitting `sort` yields `meta.x_query.order = "best matches first"`.
- **Retraction of Speculative Claims:**
  - Confirmed that `is_oa: true`, `oa_url`, and `pdf_url` are unverified API metadata fields; no PDF files were downloaded and no paywalls were empirically tested.
  - Retracted claims regarding verified free PDF downloads, publisher paywalls, and BypassSandbox header traces across all documentation.
- **Identified Script Defect:**
  - `fetch_literature.py` previously injected `sort=cited_by_count:desc` unconditionally into every request, preventing users from leveraging OpenAlex's default relevance ranking.

### 2. Code Changes Implemented in `workshop/fetch_literature.py`
1. **Explicit Relevance Sort Option:**
   - Updated `query_openalex()`:
     ```python
     if sort and sort != "relevance":
         params["sort"] = sort
     ```
   - When `--sort relevance` is passed, the `sort` parameter is completely omitted from the query string, activating OpenAlex's native relevance scoring (`best matches first`).
   - Default behavior `--sort cited_by_count:desc` and custom sorts (e.g. `publication_date:desc`) are preserved.
2. **Truthful Missing Author Handling:**
   - In `write_csv()`: If `r["authors"]` is empty, writes an empty string `""` instead of `"Unknown"`.
   - In `write_bibtex()`: If `r["authors"]` is empty, completely omits the `author = {...}` line rather than emitting `author = {Unknown}`. Citekey generation retains placeholder (e.g. `Unknown2024...` or `Ref2024...`).

### 3. Mock Test Suite Updates & Execution Results (`workshop/tests/test_workshop.py`)
1. **Updated `test_03_fixture_missing_metadata`:**
   - Verifies CSV `Authors` is `""`.
   - Verifies BibTeX omits `author =` line for authorless entries while retaining citekey placeholder.
   - Verifies `verify_zotero_import.verify_bibtex()` passes.
2. **Added `test_08_request_url_construction` (unittest.mock):**
   - Verifies `sort="relevance"` omits `sort` from the URL.
   - Verifies `sort="cited_by_count:desc"` includes `sort=cited_by_count%3Adesc`.
   - Verifies parameter encoding for topic, year, limit (capped at 50), and polite pool email.

### 4. Test Execution Command and Results
```bash
python3 /home/andy/projects/promptpraxis/workshop/tests/test_workshop.py
```
- **Exit Code:** `0`
- **Output:** `Ran 8 tests in 0.021s. OK (skipped=1)`
- **Breakdown:**
  - `test_01_fixture_normal_query`: **PASS**
  - `test_02_fixture_empty_results`: **PASS**
  - `test_03_fixture_missing_metadata`: **PASS** (Empty author in CSV, omitted in BibTeX)
  - `test_04_network_failure_handling`: **PASS** (Mock URLError & CLI exit 1)
  - `test_05_live_api_query`: **SKIPPED** (OpenAlex HTTP 403 egress policy block; strictly counted as SKIPPED)
  - `test_06_parameter_customization_track_b`: **PASS**
  - `test_07_special_characters_and_author_parsing`: **PASS**
  - `test_08_request_url_construction`: **PASS** (Mock URL construction for relevance vs citation sort)
- **Total:** **7 PASS, 1 SKIPPED, 0 FAIL**

### 5. Two-Track Acceptance Protocol Synchronization (`docs/workbuddy-two-track-acceptance.md`)
- Both Track A and Track B unified on:
  - **Topic:** `automated written corrective feedback`
  - **Year:** `2024` to present
  - **Sort:** Default relevance
  - **Limit:** `5`
- Track A prompt explicitly instructs WorkBuddy to omit sort and avoid reading existing scripts.
- Track B prompt explicitly passes `--sort relevance`.

### 6. Remaining Scope
- Running the full Track A and Track B protocol inside Tencent WorkBuddy GUI on Windows.
- Running physical desktop Zotero import verification.
- Article draft trimming (Parts 1–3) to hit ≤1,550 words.

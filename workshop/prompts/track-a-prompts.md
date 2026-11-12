# Track A — Paste-Ready Prompts for Conversational Agents (WorkBuddy)

If you are using **Tencent WorkBuddy**, **ChatGPT**, **Claude**, or **DeepSeek** directly in a conversational chat window, use these step-by-step prompts.

> [!IMPORTANT]
> **Track A Principle:** Track A operates from conversational instructions and may generate its own execution code. The agent communicates with the public OpenAlex API through its own runtime tools or curl; it does **not** read, import, or call the local `workshop/fetch_literature.py` script.

---

### Step A1 — Make It Explain First (Planning Contract)

**1. 首次准备 (Preparation):**  
Open a new chat session in WorkBuddy or your conversational AI agent, with your active project directory set as the working space.

**2. 输入提示词 (Input Prompt):**  
Paste this prompt first to establish ground rules and prevent hallucinated execution:

```text
I am new to agentic literature management. Before doing anything: tell me in three concise bullet points what this prompt would do, what information you need from me, and what could go wrong. Do not run any search yet.

"Find the 5 most relevant papers on automated written corrective feedback published since 2024 from OpenAlex, and show me Title, Year, Citations, and DOI."
```

**3. 预期结果 (Expected Outcome):**  
The agent pauses execution and provides a 3-bullet breakdown explaining: (a) what the query will target, (b) required parameters, and (c) risks (such as rate limits or missing DOIs).

**4. 失败处理 (Troubleshooting):**  
If the agent attempts to run immediately without explaining, send:  
*"Stop. Explain the plan first as requested."*

---

### Step A2 — Run Your First Query

**1. 首次准备 (Preparation):**  
Confirm the plan generated in Step A1.

**2. 输入提示词 (Input Prompt):**  
Paste:

```text
Proceed with the search using OpenAlex's public Works API.
- Topic: automated written corrective feedback
- Published since: 2024
- Sort order: default relevance (best matches first; omit sort parameter)
- Number of results: 5
- Polite pool: leave email empty or use your real institutional email (do not use fictitious emails)

Format the results as a Markdown table with columns:
Title | Year | Citations | DOI

House rule: Every row must come directly from the OpenAlex API response. Do not invent, extrapolate, or complete any row from memory. If metadata is missing (such as an unregistered DOI, missing author, or missing publication year), leave the field blank and report it. Do not invent any publication.
```

**3. 预期结果 (Expected Outcome):**  
A table of up to 5 returned records from 2024 to the present matching *automated written corrective feedback*, displaying titles, years, citation counts, and clickable DOIs.

**4. 失败处理 (Troubleshooting):**  
- **Link Verification:** Click at least one returned DOI link in your browser. It should open the publisher landing page or preprint record (a DOI confirms publication record, not that all PDFs are freely accessible).
- **HTTP 429 Error:** If rate-limited, stop and follow the service response or current access instructions; do not repeatedly retry.

---

### Step A3 — Save Your Persistent Reading List

**1. 首次准备 (Preparation):**  
Ensure the table from Step A2 has been produced.

**2. 输入提示词 (Input Prompt):**  
Paste:

```text
Save these search results as a CSV file named "found.csv" in the current workspace folder with the following columns:
OpenAlex_ID, Title, Authors, Year, Citations, DOI, Journal, Reading_Status, Notes

Set Reading_Status to "Unread" for all rows, and leave Notes blank.
Also provide instructions for opening this CSV file in Microsoft Excel, Apple Numbers, Google Sheets, or Tencent Docs.
```

**3. 预期结果 (Expected Outcome):**  
A valid `found.csv` file created in your local working folder. Opening it in Excel, Sheets, or Tencent Docs displays the 5 papers as an editable reading list.

**4. 失败处理 (Troubleshooting):**  
If the file path fails, verify that your agent has write permissions in the active workspace directory. Avoid absolute paths specific to other machines.

---

### Step A4 — Export for Reference Management (Zotero Format)

**1. 首次准备 (Preparation):**  
Verify `found.csv` exists.

**2. 输入提示词 (Input Prompt):**  
Paste:

```text
Convert the 5 literature records into a standard BibTeX file named "found.bib" (and an alternate "found.ris" file) that complies with standard reference manager import syntax.
Ensure:
1. Each entry has a unique citekey based on first author and year.
2. Authors are separated by 'and'.
3. DOIs and URLs are retained when present in the API response.
4. Provide the exact steps to import this file into Zotero Desktop.
```

**3. 预期结果 (Expected Outcome):**  
Valid `found.bib` and `found.ris` files written to the workspace with properly escaped special characters and balanced braces.

**4. 失败处理 & Zotero 导入说明 (Zotero Note):**  
Standard Zotero Desktop import steps:
1. In Zotero, click **File** → **Import...**
2. Choose **A file (BibTeX, RIS, Zotero RDF, etc.)** → click **Next**.
3. Select `found.bib` (or `found.ris`).
4. Choose destination collection.


---

### Step A5 — Automate a Periodic Search

**1. 输入提示词 (Input Prompt):**  
Paste:

```text
I want to turn this into a periodic literature check. Modify the query to look back over the past 30 days and sort by newest publication date (publication_date:desc). Show me the updated prompt or query parameter that I can run periodically.
```

**2. 预期结果 (Expected Outcome):**  
The agent adjusts the filter to `from_publication_date:[RECENT_DATE]` and `sort=publication_date:desc`, providing an on-demand prompt for recurring literature scans.

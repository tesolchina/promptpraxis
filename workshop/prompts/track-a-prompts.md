# Track A — Paste-Ready Prompts for Conversational Agents (WorkBuddy)

If you are using **Tencent WorkBuddy**, **ChatGPT**, **Claude**, or **DeepSeek** directly in a conversational chat window, use these step-by-step prompts.

---

### Step A1 — Make it Explain First (30 seconds)

Paste this prompt first to establish ground rules and prevent hallucination:

```text
I am new to agentic literature management. Before doing anything: tell me in three concise bullet points what this prompt would do, what information you need from me, and what could go wrong. Do not run any search yet.

"Find the 10 most-cited papers on [YOUR TOPIC] published since [YEAR] from OpenAlex, and show me Title, Year, Citations, and DOI."
```

> **Recovery tip:** If the agent begins executing immediately without explaining, respond: *"Stop. Explain the plan first as requested."*

---

### Step A2 — Run Your First Query (2 minutes)

Once the agent confirms the plan, paste:

```text
Proceed with the search using OpenAlex's public Works API.
- Topic: applied linguistics AI
- Published since: 2024
- Sort by: cited_by_count:desc
- Number of results: 10
- Polite pool mailto: your.email@example.com

Format the results as a Markdown table with columns:
Title | Year | Citations | DOI

House rule: Every row must come directly from the OpenAlex API response. Do not invent, extrapolate, or complete any row from memory. If the API returns fewer than 10 results or missing data, leave the fields empty and state so explicitly.
```

**Verification:** Open at least one DOI link in your browser. It must open the publisher page or preprint landing page.

---

### Step A3 — Save the Reading List (3 minutes)

Paste:

```text
Save these search results as a CSV file named "found.csv" with the following columns:
OpenAlex_ID, Title, Authors, Year, Citations, DOI, Journal, Reading_Status, Notes

Set Reading_Status to "Unread" for all rows, and leave Notes blank.
Also provide instructions for opening this CSV file in Microsoft Excel, Apple Numbers, Google Sheets, or Tencent Docs.
```

**Verification:** Open `found.csv`. You now have a persistent tabular database of your literature query. Browser hunting tabs can now be closed safely.

---

### Step A4 — Hand It to Zotero (5 minutes)

Paste:

```text
Convert the 10 literature records into a valid BibTeX file named "found.bib" (and an alternate "found.ris" file) that complies with standard Zotero import rules.
Ensure:
1. Each entry has a unique citekey based on first author and year.
2. Authors are separated by 'and'.
3. DOIs and URLs are retained.
4. Provide the exact steps to import this file into Zotero Desktop.
```

**Import steps in Zotero:**
1. In Zotero, click **File** → **Import...**
2. Choose **A file (BibTeX, RIS, Zotero RDF, etc.)**
3. Select `found.bib` (or `found.ris`)
4. Confirm destination collection.

---

### Step A5 — Build and Automate (Weekly Alert)

Paste:

```text
I want to turn this into a weekly literature alert. Modify the query to look back only over the past 7 days, and sort by newest publication date (publication_date:desc). Show me the updated prompt or script command I can run every Friday.
```

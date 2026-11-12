# Entry 2 — Introduction to Agentic AI: a hands-on lesson for academic literature management

A researcher's hundred open tabs, a column that urged her to build a system, and the two steps where systems still leak — now handed to instruments that do not have hands.

---

## Part 1 — A hundred open tabs: the problem every researcher recognises

In July 2022, Maya Gosztyla wrote in the *Nature* Career Column about the evening her laptop crashed with more than a hundred papers open in browser tabs, each an unfulfilled promise to read later (Gosztyla, 2022). Her relief at losing them forced an overdue decision: build a system, or keep drowning in tabs.

She outlined four steps: **find, manage, read, organize**. Finding leaks when alerts flood inboxes and browser tabs accumulate. Managing fails when records stay scattered across download folders. Reading and organizing require human judgment, but finding and managing can be systematized. We start with the conventional tools she recommended.

## Part 2 — The solutions she proposed (no AI in sight)

Her fixes remain solid, conventional, and manual.

**Step 1 — find.** Stop hunting across websites; subscribe using **RSS (Really Simple Syndication)**. Journals publish new tables of contents as XML feeds at fixed web addresses. An RSS reader checks them automatically: no inbox clutter, no lost tabs.

1. **Pick a reader:** Web readers like Feedly or Inoreader require zero local setup.
2. **Subscribe:** Add journal feed URLs directly, such as [*Nature*](https://www.nature.com/nature.rss) or [arXiv cs.AI](https://rss.arxiv.org/rss/cs.AI).
3. **Daily routine:** Spend five minutes scanning titles, flag relevant papers for later, and close the reader.

> **Demo — Feedly in 5 minutes:** Open feedly.com → sign up free → click **Follow** → paste `https://www.nature.com/nature.rss` → newest papers appear in your sidebar. Repeat for `https://rss.arxiv.org/rss/cs.AI`.

For backward and forward citation discovery, mapping tools like ResearchRabbit, Connected Papers, and Litmaps show citation networks. The core principle: let literature arrive on a predictable schedule rather than hunting manually between meetings.

**Step 2 — manage.** Reference managers automate formatting and cataloging. **Zotero** is free, open source, and cross-platform:

| Operation | What you do in Zotero |
|---|---|
| **Import** | Capture records from web pages with the browser connector, by DOI, or via BibTeX/RIS files |
| **Organize** | Sort into project Collections, tag, and detect duplicate entries |
| **Read & Annotate** | Highlight PDFs in the built-in reader; create notes from selected annotations |
| **Cite** | Insert citations and build bibliographies in Word or LibreOffice via plug-ins |
| **Export** | Share libraries or export standard BibTeX/RIS reference files |

> **Demo — Zotero in 5 minutes:** 1. Install Zotero and the browser connector from zotero.org. 2. On any paper page, click the connector to save the citation to your library. 3. File it into a project Collection. 4. If you have an accessible PDF, open it in the built-in reader and highlight text. 5. Insert references into your word processor with one click.

Gosztyla's rule was straightforward: once a paper was saved to the reference manager, the browser tab could close.

These tools already automate useful work. The remaining challenge is connecting discovery, selection and export into a repeatable workflow.

## Part 3 — GUI against API: the boundary Entry 1 already crossed

### The GUI boundary

A graphical interface makes inspection and correction approachable. RSS readers can refresh automatically, and reference managers offer saved searches. The limitation is not that graphical tools cannot automate: it is the repeated work of moving information between tools. An agent can help connect those steps while leaving selection and interpretation to the researcher.

### How Entry 1 crossed it

Entry 1 argued that an agent translates ordinary natural language into machine execution: you describe a task in plain sentences, and the computer carries it out. Crucially, **an agent is a processor, not an information repository**. We do not ask an AI model what papers exist; we instruct it to fetch real metadata from authoritative external registries.

### Code as the instrument

Code executes without manual pointing and clicking. It can run a query, inspect thousands of records, and rerun exact criteria next week without drift. Two instruments make this possible:

- **An API** is a structured service counter: you submit a formatted request and receive exact structured data without conversation. For example:
  ```
  https://api.openalex.org/works?search=automated+written+corrective+feedback&filter=from_publication_date:2024-01-01&per-page=5
  ```
  This single URL queries OpenAlex for recent papers on automated written corrective feedback, returning metadata, including DOIs where available, without opening a search portal.
- **RSS** brings newly published journal updates directly to an automated consumer, allowing agents to filter incoming items against research criteria.

| Step | Hands, one screen at a time | Automated instruments |
|---|---|---|
| **1. Find** | Manual scanning; inbox alerts; retyped queries | An OpenAlex query can be rerun with the same criteria; scheduling requires a separate setup |
| **2. Manage** | One-by-one manual saves and folder sorting | Query results save automatically to CSV, and export to standard BibTeX/RIS for reference managers |

## Part 4 — How you do that, with WorkBuddy

Open the [companion workshop](https://github.com/tesolchina/promptpraxis/tree/codex/entry02-workshop-progress/workshop). Choose either track. For Track B, download that branch or open its checkout in WorkBuddy; use an available Python 3 interpreter from the repository root.

### Track A — Describe the task from scratch

Use WorkBuddy with network access and a writable workspace. It may generate and execute its own code; this route does not reuse our prepared script. Other agents need equivalent tools.

1. **A1: Planning contract.** In WorkBuddy, establish rules first:
   > "I am new to this. Before doing anything: tell me in three bullet points what this prompt would do, what information you need from me, and what could go wrong. Do not run it yet:
   > 'Find the 5 most relevant papers on automated written corrective feedback published since 2024 from OpenAlex, and show Title, Year, Citations, and DOI.'"
2. **A2: Query OpenAlex.** Once the agent outlines its plan, send:
   > "Query OpenAlex Works API for the 5 most relevant articles on automated written corrective feedback since 2024 using default relevance sorting. Omit the email parameter. Output a table: Title | Year | Citations | DOI. Every row must come strictly from API metadata; leave missing fields blank and never fabricate publications."
   *Outcome:* Up to five records appear. Inspect their titles for relevance and open an available DOI to check the linked record. Search ranking is not a quality assessment.
3. **A3: Save to CSV.** Ask:
   > "Save this table to `found.csv` with columns: OpenAlex_ID, Title, Authors, Year, Citations, DOI, Journal, Reading_Status, Notes. Set Reading_Status to Unread and leave Notes blank."
   *Outcome:* `found.csv` opens in Excel, Google Sheets, or Tencent Docs as a durable reading log.
4. **A4: Export to BibTeX and RIS.** Prompt:
   > "Convert the returned records into standard `found.bib` and `found.ris` files with clean citekeys, author separation, and DOIs preserved."
   *Outcome:* Reference files are saved. In Zotero, choose File → Import, select either file, and check the imported records against your CSV.

### Track B — Reuse the prepared Python script

Ask WorkBuddy to explain and run the standalone script documented in [`workshop/prompts/beginner-pack.md`](https://github.com/tesolchina/promptpraxis/blob/codex/entry02-workshop-progress/workshop/prompts/beginner-pack.md):

```bash
python3 workshop/fetch_literature.py \
  --topic "automated written corrective feedback" \
  --year 2024 \
  --sort relevance \
  --limit 5 \
  --email=
```

- **Output:** Writes `found.csv`, `found.bib`, and `found.ris` into your workspace. Missing metadata fields remain empty rather than hallucinated.
- **Customization:** Modify `--topic`, `--year`, or sort order (`--sort "publication_date:desc"`).
- **Edge cases:** If a query returns no matches, the script writes empty output files. If offline, the script suggests `--fixture workshop/tests/fixtures/openalex_normal.json`.

## Part 5 — Decisions, limits, and value

**Decisions:** We limit this lesson to the first two steps (find and manage) because an entry attempting everything teaches nothing. Standard BibTeX/RIS export remains the dependable bridge to reference managers; experimental in-agent citation formatters remain a separate spike.

**Limits:** Language models can invent or miscopy citations even when tools are available. Compare outputs with the saved API response, preserve missing fields and check relevance yourself. A DOI helps identify a record; it does not establish the quality of its claims or guarantee free full text. API access conditions and limits can change; stop on errors and follow the service instructions.

**Value:** An afternoon of browser tab chasing becomes a two-minute query. The same instructions can be reused: next month's literature review is last month's prompt with an updated date filter.

## Closing — Starting the cycle

One query on a genuine topic yields a table too useful to discard. The reader opens one paper today, reruns the prompt next week, and the pipeline shifts from a classroom exercise into daily practice.

---

**Footnotes:** ¹ Gosztyla, M. (2022). *How to find, read and organize papers*. Nature Careers, 07 July 2022. doi:10.1038/d41586-022-01878-7. ² OpenAlex verified 12 Nov 2026: ~11,915 results for `search=automated written corrective feedback`, `from_publication_date:2024-01-01`, default relevance. ³ Companion run evidence: [WorkBuddy two-track comparison](https://github.com/tesolchina/promptpraxis/blob/codex/entry02-workshop-progress/workshop/evidence/two-track-20261112/cross_check.txt).


# Entry 2: Introduction to Agentic AI, a hands-on lesson for academic literature management

**Series:** *Prompt & Praxis* (IEEE ProComm) · **Publication date:** 13 November 2026 · **Series Host:** Dr Simon Wang (Language Centre, HKBU)

**Guest Authors:**
- **Wenyun (Winnie) FU**, final-year Journalism undergraduate, HKBU. Human-in-the-loop writing workflows, source verification, literature synthesis.
- **Zian (Andy) Zheng**, final-year Computer Science undergraduate, HKBU. Agentic pipelines, prototyping, API orchestration.

**Table of Contents (Series Navigation):**
- [Entry 1: From plain texts to playable](https://procomm.ieee.org/ai-resources/prompt-and-praxis/entry01/) · *earlier entry*
- [Entry 2: Introduction to Agentic AI](https://procomm.ieee.org/ai-resources/prompt-and-praxis/entry02/) · *reading now*

**Standfirst:** In this entry, we learn how to use agentic AI to enhance the tools for academic literature management that were available through a graphical user interface (GUI) before the advent of vibe coding. WorkBuddy is introduced as a platform to access agentic AI, but instructions and resources are applicable to other agentic AI platforms as well.

---

## Part 1: A hundred open tabs

In July 2022, Maya Gosztyla wrote in the [*Nature* Career Column](https://www.nature.com/articles/d41586-022-01878-7) about the evening her laptop died. More than a hundred papers were waiting in browser tabs, each a promise to read later. When the crash took them, her first feeling was relief: the loss forced a decision she had been postponing.¹

Her article set out four steps: **locate the relevant research literature**, **curate the literature using Zotero**, **read the papers on a set routine**, and **organize your notes in a database you can query**. Locating means finding the journal articles that matter to the researcher; curating means turning those finds into a lasting indexed database. This entry takes the first two; reading and organizing remain human work, since no script supplies the critical judgement they demand. Entry 3 picks up steps three and four.

## Part 2: RSS and Zotero: GUI software solutions for finding and managing research literature

Her fixes were conventional, and they work: an RSS reader brings the literature to you, and a reference manager files it. Both are established tools from before AI, and each already encodes a way of working that any researcher can follow. Agentic AI builds on them: with vibe coding we can write small tools that reproduce these workflows, or adopt newer tools designed to work with agents.

### Step 1: Locate the relevant research literature

Stop hunting for new papers and let them come to you. Really Simple Syndication (RSS) is a publishing format: when a journal posts new articles, it also publishes a small XML file at a fixed address, called a feed, that lists what is new with titles, authors and a short summary. An RSS reader visits those addresses on schedule and gathers every feed you follow into a single stream, so collecting runs automatically in the background instead of depending on your memory to check each journal. What you can do with that stream, though, depends on the reader you choose. A typical reader lets you skim the titles, mark what you have seen and save a few items for later; the feed itself only carries a summary, and features such as filtering, full-text reading or search differ from one reader to the next. Collection is automated; working through the stream is still up to you.

1. **Choose a reader.** Web readers such as [Feedly](https://feedly.com) or [Inoreader](https://www.inoreader.com) need no installation; desktop and mobile readers work offline.
2. **Subscribe with feed addresses.** Paste verified URLs into your reader: [*Nature*](https://www.nature.com/nature.rss), [*Nature Communications*](https://www.nature.com/ncomms.rss), [arXiv cs.AI](https://rss.arxiv.org/rss/cs.AI).
3. **Keep a five-minute morning routine.** Scan titles with your tea, move real candidates to *Read Later*, close the reader.

![Figure 1: Subscribing to journal feeds in Feedly](assets/feedly-demo.png)
> **Figure 1** · *Subscribing to journal feeds in Feedly.* An 'Academic' collection aggregates incoming issues from journals like *Nature* and *arXiv cs.AI* into one reading stream, so morning triage needs no extra tabs.

### Step 2: Curate the literature using Zotero

If you still format references by hand, stop. A reference manager is a personal research database: full-text PDFs sit beside verified records, annotations stay bound to their pages, and one click pulls a paper off the web.

We use **Zotero** (free, open source, [zotero.org](https://www.zotero.org)): its metadata and citation engines can be inspected and reused in automated pipelines, and its open architecture keeps data in the scholar's hands. Mendeley and EndNote follow similar patterns.

Four operations complete the loop:

| Operation | What you do in Zotero | Advantage |
|---|---|---|
| **Import** | Browser connector, or by DOI, RIS/BibTeX, PDF drag-and-drop | Metadata and full PDF, no copy-pasting |
| **Organize** | Collections, tags, saved searches, duplicates | Sorted by topic, no duplicated files |
| **Read & annotate** | Built-in reader; highlights become notes | Notes stay attached to the entry |
| **Cite** | Plug-in for Word, LibreOffice, Google Docs | Thousands of styles, bibliography self-updates |

![Figure 2: Literature management loop in Zotero](assets/zotero-demo.png)
> **Figure 2** · *Literature management in Zotero (Web Library).* Incoming papers are filed into a project collection ('Applied Linguistics & AI' in this illustrative example) with complete metadata, source URL, and DOI captured in one click.

Gosztyla's rule: the moment a paper is worth reading, send it to the manager and close the tab.

Everything in Part 2 runs **by hand, one click at a time**. That ceiling opens Part 3.

## Part 3: Enhancing GUI software solutions with agentic-AI-powered API programming

Every tool in Part 2 reaches you through a graphical user interface (GUI): windows, buttons and menus that a person drives by hand, one screen at a time. The RSS reader shows incoming issues as a list you click through; Zotero shows your library as folders you drag files into. That is the GUI's virtue: a newcomer becomes productive in minutes. It is also its boundary: the screen moves at the speed of fingers and eyes, so it cannot check for new papers while you teach, or repeat last week's multi-filter search without retyping. Gosztyla's hundred tabs were a symptom of that boundary.

Programmed code has no hands or eyes: it runs a query at dawn and repeats yesterday's search next month. An Application Programming Interface (API) is how code reaches such services without a screen: a fixed menu of requests that returns exact, machine-readable records. Part 4 puts this in your hands: you describe the job, and an agent writes and runs the code that calls the API.

|  | Graphical user interface (GUI) | Application Programming Interface (API) |
|---|---|---|
| **Driven by** | fingers and eyes, one screen at a time | requests sent in code, no screen in between |
| **Pace** | as fast as you can click | runs at dawn, repeats on schedule |
| **Good for** | reading, judging, deciding what to keep | searching, collecting, exporting at scale |
| **In this entry** | Feedly and Zotero, from Part 2 | the hands-on build in Part 4 |

[Entry 1](https://procomm.ieee.org/ai-resources/prompt-and-praxis/entry01/) established the bridge that makes this reachable: an agent sits between human language and computing instruments, so you describe a job in ordinary sentences and the agent writes the code that calls the API. Entry 1 also drew a boundary we preserve: **the agent reasons, and the database supplies the facts.**

With an API in hand, both GUI solutions from Part 2 can be rebuilt without their screens: an RSS reader becomes a feed watcher that checks the journal for you, and Zotero becomes a metadata store an agent can query, write records to, and export as BibTeX or RIS. The GUI keeps the part that needs a person: reading critically, and deciding what to keep. Part 4 puts the pipeline into practice.

## Part 4: How you do that, with WorkBuddy

Entry 01 showed what agentic AI can build; this part answers the question it left open: how.

WorkBuddy is not the only tool for agentic AI: integrated development environments (IDEs) such as VS Code, Codex, Claude Code and Cursor now ship agentic-AI modules, but those tools are built for professional programmers and developers, and a beginner would find them difficult to pick up. This entry runs in WorkBuddy instead, where you start from plain sentences.

Before the hands-on part, revisit Entry 01's input-process-output model: plain sentences in, code written and run, files and tables out. Keep it in view to understand the big picture of what the two tracks below do.

Open the [companion workshop](https://github.com/tesolchina/promptpraxis/tree/main/workshop). Choose either track. Track B runs in WorkBuddy using Python 3 from the repository root.

### Track A: describe the task from scratch

Use WorkBuddy with network access and a writable workspace; it writes and runs its own code.

1. **A1: Planning contract.** Establish rules first:
   > "I am new to this. Before doing anything: tell me in three bullet points what this prompt would do, what information you need from me, and what could go wrong. Do not run it yet:
   > 'Find the 5 most relevant papers on automated written corrective feedback published since 2024 from OpenAlex, and show Title, Year, Citations, and DOI.'"
2. **A2: Query OpenAlex.** Once the agent outlines its plan, send:
   > "Query OpenAlex Works API for the 5 most relevant articles on automated written corrective feedback since 2024 using default relevance sorting. Omit the email parameter. Output a table: Title | Year | Citations | DOI. Every row must come strictly from API metadata; leave missing fields blank and never fabricate publications."
   *Outcome:* Up to five records appear. Check titles, open an available DOI. Ranking is not quality assessment.
3. **A3: Save to CSV.** Ask:
   > "Save this table to `found.csv` with columns: OpenAlex_ID, Title, Authors, Year, Citations, DOI, Journal, Reading_Status, Notes. Set Reading_Status to Unread and leave Notes blank."
   *Outcome:* `found.csv` opens in Excel, Google Sheets, or Tencent Docs as a durable reading log.
4. **A4: Export to BibTeX and RIS.** Prompt:
   > "Convert the returned records into standard `found.bib` and `found.ris` files with clean citekeys, author separation, and DOIs preserved."
   *Outcome:* In Zotero, choose File → Import and check the records.

### Track B: reuse the prepared Python script

Ask WorkBuddy to explain and run the script documented in [`workshop/prompts/beginner-pack.md`](https://github.com/tesolchina/promptpraxis/blob/main/workshop/prompts/beginner-pack.md):

```bash
python3 workshop/fetch_literature.py \
  --topic "automated written corrective feedback" \
  --year 2024 \
  --sort relevance \
  --limit 5 \
  --email=
```

- **Output:** writes `found.csv`, `found.bib`, and `found.ris`. Missing metadata stays empty; nothing is invented.
- **Customisation:** change `--topic`, `--year`, or the sort order.
- **Edge cases:** no matches writes empty files; offline, add `--fixture workshop/tests/fixtures/openalex_normal.json`.

## Part 5: Decisions, limits, and value

**Decisions:** We limit the lesson to find and manage; an entry attempting everything teaches nothing. BibTeX/RIS export stays the dependable bridge to reference managers.

**Limits:** Language models can invent or miscopy citations even when tools are available. Compare outputs with the saved API response, keep missing fields empty, and judge relevance yourself. A DOI identifies a record; it does not establish the quality of its claims or guarantee free full text. API conditions change, so stop on errors.

**Value:** An afternoon of tab chasing becomes a two-minute query; next month's review is this month's prompt with a new date filter.

## Closing: starting the cycle

Open one paper today, rerun the prompt next week, and the pipeline becomes daily practice.

---

**Footnotes:** ¹ Gosztyla, M. (2022). *How to find, read and organize papers*. Nature Careers, 07 July 2022. doi:10.1038/d41586-022-01878-7. ² Companion run evidence: [WorkBuddy two-track comparison](https://github.com/tesolchina/promptpraxis/blob/main/workshop/evidence/two-track-20261112/cross_check.txt).

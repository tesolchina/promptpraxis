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

Her fixes were conventional, and they still work well today. An RSS reader brings the literature to you, and a reference manager files it; both are established tools from before AI, and each already encodes a way of working that any researcher can follow. Agentic AI builds on them. With vibe coding we can write small tools that reproduce these workflows, or adopt newer tools designed to work with agents.

### Step 1: Locate the relevant research literature

Stop hunting for new papers and let them come to you. Really Simple Syndication (RSS) is a web feed format that carries updates from websites in a standard, computer-readable structure: each feed document lists new items with a title, a summary and a link, and is republished whenever the source adds something. A reader program follows those addresses and gathers everything you subscribe to into one place, removing the need to check each journal by hand; the same mechanism carries blog posts, news headlines and podcast episodes well beyond academic literature. What you can then do with the stream depends on the reader you choose: a typical reader lets you skim the titles, mark what you have seen and save items for later, while filtering, full-text reading and search vary from reader to reader. The three steps below set up a basic reading routine.

1. **Choose a reader.** Web readers such as [Feedly](https://feedly.com) or [Inoreader](https://www.inoreader.com) need no installation; desktop and mobile readers work offline.
2. **Subscribe with feed addresses.** Paste verified URLs into your reader: [*Nature*](https://www.nature.com/nature.rss), [*Nature Communications*](https://www.nature.com/ncomms.rss), [arXiv cs.AI](https://rss.arxiv.org/rss/cs.AI).
3. **Keep a five-minute morning routine.** Scan titles with your tea, move real candidates to *Read Later*, close the reader.

![Figure 1: Subscribing to journal feeds in Feedly](assets/feedly-demo.png)
> **Figure 1** · *Subscribing to journal feeds in Feedly.* An 'Academic' collection aggregates incoming issues from journals like *Nature* and *arXiv cs.AI* into one reading stream, so morning triage needs no extra tabs.

### Step 2: Curate the literature using Zotero

For anyone still formatting references by hand, a reference manager is the first upgrade worth making. It works as a personal research database, where full-text PDFs sit beside verified records, annotations stay bound to their pages, and one click pulls a paper off the web.

We use **Zotero** (free, open source, [zotero.org](https://www.zotero.org)): its metadata and citation engines can be inspected and reused in automated pipelines, and its open architecture keeps data in the scholar's hands. Mendeley and EndNote follow similar patterns.

Four operations complete the loop:

| Operation | What you do in Zotero | Advantage |
|---|---|---|
| **Import** | Browser connector, or by DOI, RIS/BibTeX, PDF drag-and-drop | Metadata and full PDF, no copy-pasting |
| **Organize** | Collections, tags, saved searches, duplicates | Sorted by topic, no duplicated files |
| **Read & annotate** | Built-in reader; highlights become notes | Notes stay attached to the entry |
| **Cite** | Plug-in for Word, LibreOffice, Google Docs | Thousands of styles, bibliography self-updates |

![Figure 2: Traci's Zotero library](assets/zotero-demo-tnk.jpg)
> **Figure 2** · *Literature management in Zotero (Web Library).* Incoming papers are filed into a project collection ('Applied Linguistics & AI' in this illustrative example) with complete metadata, source URL, and DOI captured in one click. *Screenshot courtesy of Traci Nathans-Kelly.*

Gosztyla's rule: the moment a paper is worth reading, send it to the manager and close the tab.

Both tools are dependable, and both wait for you once the feeds arrive. Every decision in this workflow runs through an interface: a person clicks the connector, drags the file, scans the list and chooses what to keep, and none of it happens again until someone returns to the screen. That is the practical limit of interface-driven work, and it is the question Part 3 takes up.

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

In entry 01 of this blog series, we already showcased the power of agentic AI but did not address the question of how to start. In this entry, we demonstrate how to use agentic AI hands-on. WorkBuddy is an agentic AI platform developed by Tencent, an internet giant based in mainland China. If you wish to try the tool, you may sign up for an account here: https://www.workbuddy.ai/.

WorkBuddy is not the only tool for agentic AI: integrated development environments (IDEs) such as VS Code, Codex, Claude Code and Cursor now ship agentic-AI modules, but those tools are built for professional programmers and developers, and a beginner would find them difficult to pick up. This entry runs in WorkBuddy instead, where you start from plain sentences.

Before the hands-on part, revisit Entry 01's input-process-output model: plain sentences in, code written and run, files and tables out. Keep it in view to understand the big picture of what the demo below does.

<div class="figure-scroll" style="overflow-x:auto"><svg class="flow" viewBox="0 0 920 210" role="img" aria-label="Flow: a plain-language brief and source material feed an agentic AI that writes code and calls tools, producing something playable" style="max-width:100%;height:auto">
  <defs>
    <marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0 0 L10 5 L0 10 z" fill="#006699"/>
    </marker>
  </defs>
  <rect x="8" y="35" width="255" height="140" rx="14" fill="#fff" stroke="#dde5ee"/>
  <text x="135" y="66" text-anchor="middle" font-size="15" font-weight="700" fill="#1f2d3a">Plain-language brief</text>
  <text x="135" y="94" text-anchor="middle" font-size="12.5" fill="#5c6f83">a permissioned article</text>
  <text x="135" y="114" text-anchor="middle" font-size="12.5" fill="#5c6f83">Google's published research</text>
  <text x="135" y="145" text-anchor="middle" font-size="12.5" fill="#b35c00" font-weight="700">quality input</text>
  <rect x="330" y="35" width="255" height="140" rx="14" fill="#006699"/>
  <text x="457" y="66" text-anchor="middle" font-size="15" font-weight="700" fill="#fff">Agentic AI</text>
  <text x="457" y="94" text-anchor="middle" font-size="12.5" fill="#cfe3f2">writes programming code</text>
  <text x="457" y="114" text-anchor="middle" font-size="12.5" fill="#cfe3f2">calls tools &amp; APIs</text>
  <text x="457" y="145" text-anchor="middle" font-size="12.5" fill="#ffd9a8" font-weight="700">reasoning / processing</text>
  <rect x="652" y="35" width="255" height="140" rx="14" fill="#fff" stroke="#f2c58c" stroke-width="2"/>
  <text x="779" y="66" text-anchor="middle" font-size="15" font-weight="700" fill="#1f2d3a">Playable</text>
  <text x="779" y="94" text-anchor="middle" font-size="12.5" fill="#5c6f83">an interactive page</text>
  <text x="779" y="114" text-anchor="middle" font-size="12.5" fill="#5c6f83">that runs, not a reply</text>
  <text x="779" y="145" text-anchor="middle" font-size="12.5" fill="#b35c00" font-weight="700">output</text>
  <line x1="263" y1="105" x2="328" y2="105" stroke="#006699" stroke-width="2.5" marker-end="url(#ar)"/>
  <line x1="585" y1="105" x2="650" y2="105" stroke="#006699" stroke-width="2.5" marker-end="url(#ar)"/>
  <text x="460" y="196" text-anchor="middle" font-size="12" fill="#5c6f83">The pipeline of this entry, drawn in code — no image generator involved.</text>
</svg></div>

Everything needed for the demo is collected in the companion workshop folder.

### The demo: an RSS feed, a reading log, and Zotero

The demo is a simple workflow built around RSS and Zotero, chosen to showcase the potential and promise of agentic AI: an agent reads a journal feed, builds a reading log, and replicates a reference manager's core function from the reference manager's own source code — all from plain sentences. It aims at one completed pass: plan the fetch, run it, read the records that come back. Use WorkBuddy with network access and a writable workspace; it writes and runs its own code. The first two prompts deliver that pass; the rest are optional extensions once it works.

1. **Planning contract.** Establish rules first:
   > "I am new to this. Before doing anything: tell me in three bullet points what this prompt would do, what information you need from me, and what could go wrong. Do not run it yet:
   > 'Fetch the five most recent articles from Nature's RSS feed (https://www.nature.com/nature.rss) and show Title, Publication date, and Link.'"
2. **Fetch the feed.** Once the agent outlines its plan, send:
   > "Fetch the RSS feed at https://www.nature.com/nature.rss with Python, parse the five most recent items, and output a table: Title | Date | Link. Every row must come strictly from the feed; leave missing fields empty and never invent records."
   *Outcome:* Five rows appear. Open one link to check it resolves. A feed is a plain XML file, so anything the feed does not carry stays empty.
3. **Save to CSV.** Ask:
   > "Save this table to `found.csv` with columns: Title, Date, Link, Reading_Status, Notes. Set Reading_Status to Unread and leave Notes blank."
   *Outcome:* `found.csv` opens in Excel, Google Sheets, or Tencent Docs as a durable reading log.
4. **Replicate a Zotero module, from its source.** Zotero is open-source, so its own code can serve as the specification. Point WorkBuddy at the repository and ask it to read one module, then write and run its own version:
   > "Read how Zotero implements record export in https://github.com/zotero/zotero, with its per-format translators in https://github.com/zotero/translators. Explain the steps in three bullet points, then write and run a Python script that replicates that module for our five records, producing `found.bib` and `found.ris` with clean citekeys and no invented fields."
   *Outcome:* The agent reads a real implementation, restates it, and runs its own version. What comes out is not a file prepared for import — it is a working replica of one Zotero function, written and run in the same pass. The same reading-then-replicating move applies to other modules: tagging, de-duplication, metadata clean-up.

5. **From DOI to styled references.** A feed link hides a DOI, and a DOI is enough to rebuild the full reference — the identifier-lookup and style-rendering modules Zotero itself relies on. Start with the same planning contract as step 1, applied to this task, then send:
   > "Take the five links in found.csv: a Nature link carries its DOI as the suffix after /articles/ (10.1038/…). For each DOI, fetch the record from https://api.crossref.org/works/<DOI> and save Title | Authors | Year | Container | DOI to found_meta.csv — empty fields stay empty, nothing is invented. Then render the same five records twice with citeproc, using apa.csl and chicago-notes-bibliography.csl from citation-style-language/styles, and save references-apa.txt and references-chicago.txt."
   *Outcome:* Two files, the same five works in two styles — one APA, one Chicago — built from metadata the agent fetched itself. Other journals need a title search instead of the link swap; the style files are the same.

**What the feed returned.** The five most recent items in Nature's RSS feed, fetched on 17 Nov 2026:

| Title | Date |
|---|---|
| The climate is in crisis — here's four things we can do | 16 Nov 2026 |
| As El Niño builds, studies of extreme marine heatwaves must start now | 16 Nov 2026 |
| The psychology of imaginary friends — and why they are good for kids | 16 Nov 2026 |
| Is the sixth great extinction imminent? Scientists must draw on natural history for clues | 16 Nov 2026 |
| Number of international students arriving in US plunges — worrying scientists | 13 Nov 2026 |

Every step above runs from plain sentences, and the code behind it is public: the [workshop folder](https://github.com/tesolchina/promptpraxis/tree/main/workshop) in the series repository holds the scripts used here. Re-use them, change the feed URL or the columns to suit your own journal, and check back for updates — the instructions in that folder will grow as the workflow does.

## Part 5: What we chose to cover, what can go wrong, and why upgrading beats rebuilding

We limit the lesson to find and manage; an entry attempting everything teaches nothing, and BibTeX/RIS export stays the dependable bridge to reference managers. Language models can invent or miscopy citations even when tools are available, so compare outputs with the saved API response, keep missing fields empty, and judge relevance yourself — a DOI identifies a record; it does not establish the quality of its claims or guarantee free full text, and API conditions change, so stop on errors. What remains is the payoff: an afternoon of tab chasing becomes a two-minute query, and next month's review is this month's prompt with a new date filter.

The starting point of this entry is deliberately not the latest AI technology. It is a workflow proposed before generative AI became widely available — Maya Gosztyla's four steps, built entirely from ordinary GUI software: RSS feeds and Zotero. Our strategy is to take well-established solutions like these and let agentic AI upgrade them instead of starting from scratch. Two properties make that possible: RSS is a machine-readable format, so an agent can vibe-code a small tool that reads a feed and processes what it finds; Zotero is open-source, so an agent can read its source code and re-use it to replicate functions such as export and tagging. Re-using the code and ideas of pre-AI tools brings the flexibility to add custom features on top, and the cumulative effect is a shift in role: from tool users to tool builders.

---

**Footnotes:** ¹ Gosztyla, M. (2022). *How to find, read and organize papers*. Nature Careers, 07 July 2022. doi:10.1038/d41586-022-01878-7. ² Companion run evidence: [workshop run records](https://github.com/tesolchina/promptpraxis/blob/main/workshop/evidence/two-track-20261112/cross_check.txt).

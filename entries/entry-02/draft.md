# Entry 2 — Draft v3 (revised per Simon's structure: problem → Career-Column solutions → GUI vs API → how-to)

**New order:** ① the problem (Career Column) ② the solutions without AI, as she proposed them — steps 1 and 2 only ③ GUI vs API, echoing Entry 1 ④ WorkBuddy how-to, two tracks ⑤ decisions, limits, value → closing.

**Suggested title:** *From chasing papers to running pipelines*

**Standfirst:** A researcher's hundred open tabs, a column that told her to build a system, and the two steps where most systems still leak — now handed to instruments that do not have hands.

---

## Part 1 — The problem

Paste nothing yet. Start with a story that every researcher recognises.

In July 2022, Maya Gosztyla wrote in *Nature* about the evening her laptop died. She had more than a hundred papers waiting in browser tabs, each one a promise to read later. When the crash took the tabs, her first feeling was relief: the loss finally forced the decision she had been postponing — a system, or another semester of re-reading the same pages (Gosztyla, 2022).

Her article set out four steps: **find, manage, read, organize**. The finding is where collections start to leak: papers promised for later, alerts that flood the inbox, the good intentions of a Friday afternoon. The managing is where intentions become a database — or fail to. Read and organize are yours to build; they need your judgement, not a script.

This entry takes the first two steps, and it starts where she started: with the tools that were already there.

## Part 2 — The solutions she proposed (no AI in sight)

Her fixes were conventional, and they still work.

**Step 1 — find.** Stop hunting; subscribe. Journal tables of contents arrive by **RSS**, the orange feed icon on a journal's home page, and a feed aggregator (Feedly, Inoreader, NewsBlur) collects them in one place. Her routine: five minutes each morning, a glance at each title, anything interesting moved to a *Read Later* folder. For deeper dives she named the citation-mapping tools — ResearchRabbit, Connected Papers, Litmaps — which show which papers lean on which. The principle underneath: **let the literature come to you on a schedule you choose**, instead of going out to look for it between meetings.

**Step 2 — manage.** Never format a reference by hand again. Zotero, Mendeley or EndNote store the paper *and* the record — folders, keywords, tags, a browser plug-in that saves a paper in one click, a word-processor plug-in that builds the bibliography. Her rule was simple: the moment she decided a paper was worth reading, it went into the reference manager, and the browser tab could close. That satisfying close is the whole step.

Two steps, two conventional tools, one honest limitation. Everything in Part 2 is operated **by hand, on a screen, one click at a time** — and that limitation is the door to Part 3.

## Part 3 — GUI against API: the boundary Entry 1 already crossed

### What the GUI is, and where it stops

Every tool in Part 2 is a GUI: what you see is what you get. That is its virtue — straightforward, friendly, a beginner productive in the first minute. It is also its boundary. A GUI can only show **one screen at a time**, and its pace is set by our eyes and hands: how fast we can click, how long we can stay with the window, how many papers we can visually hold before one is lost behind another. The screen cannot check for new papers while we teach. It cannot repeat yesterday's exact search tomorrow without us re-typing it. Gosztyla's hundred tabs are what that boundary looks like from the inside.

### How Entry 1 crossed it

[Entry 1](https://blog.simonsays.hk/ieee/01.html) made one argument: the agent sits between your plain language and the machine, so you describe a job in ordinary sentences and the machine does the work. It also drew a line we keep: **an agent is a processor, not an information engine.** Its power is in doing, not in remembering — which is why this entry never asks a model what the literature says, only to go and fetch it.

### Code as the way past the boundary, and the two instruments that carry it

Programmed code does not have hands. It can run a query at a set hour, sweep twenty-six thousand records while we make tea, and carry yesterday's exact search into tomorrow unchanged. What we can *do* expands from what our eyes and hands can finish in a session to what we can describe as a job.

Two instruments carry that weight for literature, and both predate the agent that now drives them:

- **An API** is a counter with a menu above it. You ask for one specific thing in a fixed format; the data comes back without conversation. Try it — this *is* an API call:

  ```
  https://api.openalex.org/works?search=applied linguistics AI&per-page=3
  ```

  Three papers, each with a DOI that opens the paper itself. The same address returned 26,881 results on 8 November. No search box, no scrolling, no tabs.

- **RSS** is the same transcendence in the other direction: instead of us going to look, the journal brings the new table of contents to a place we have agreed to read. It was already in Part 2; what is new is that an agent can watch the feed, filter it against our topic, and hand us only what matters.

### What the two instruments accomplish, in her context

| Her step | Hands, one screen at a time | Instruments doing the reaching |
|---|---|---|
| **1. Find** | Five-minute manual scan; alerts that flood; a topic search re-typed each week | RSS arrives and is filtered; an OpenAlex query rerun every Friday returns a fresh, sorted, DOI-tagged list |
| **2. Manage** | One-click saves, folders kept up to date by hand | The query returns a table: file it as CSV, into a reading list with Status and Notes, then into Zotero — record and PDF together |

The GUI remains where a person belongs: deciding which paper deserves a click, and what to do with it after reading.

## Part 4 — How you do that, with WorkBuddy

The pipeline is published and free to take apart: **[`workshop/`](https://github.com/tesolchina/procomm-microlearning/tree/main/workshop)** carries the prompts, the script and the expected outputs. Two tracks — pick one.

### Track A — write it from scratch

**A1 — make it explain first (30 seconds).** Paste:

> I'm new to this. Before doing anything: tell me in three lines what this prompt would do, what you need from me, and what could go wrong. Don't run it yet.
>
> "Find the 10 most-cited papers on *your topic* published since *year*, from OpenAlex, and show me title, year, citations, and DOI."

If it starts running without explaining, say *"explain first."* You are training the workflow as much as using it.

**A2 — your first query (2 minutes).** Ask for the ten most-cited articles on your topic since a given year, as a table of **title | year | citations | DOI**, with `mailto=your.email@example.com` on the request — OpenAlex's polite pool. House rule: *do not invent or complete any row; if the API returns nothing, say so.* Open one DOI; it must reach the paper.

**A3 — keep it (3 minutes).** Ask for `found.csv` and a Google Doc tab "Reading list — *your topic*" with Status and Notes columns. Close the hunting tabs. That close is the point.

**A4 — hand it to Zotero (5 minutes).** BibTeX export plus the menu steps to import, and it waits for your confirmation before acting. Zotero is free and open source; the record is yours.

**A5 — build on it.** Change one thing per run: topic, sort, or last week's date window — that last one makes a weekly literature alert.

### Track B — reuse the code we share

1. Open [`workshop/prompts/beginner-pack.md`](https://github.com/tesolchina/procomm-microlearning/blob/main/workshop/prompts/beginner-pack.md).
2. Send the link to your agent: *"Describe what this code does and how I can reuse it for my own topic."*
3. Run Level 1, Level 2, Level 3 as printed.
4. Then break it on purpose — change the topic, the year, the sort. Reusing code means editing it.

**One difference worth knowing:** WorkBuddy returns tables in the chat; VS Code and Cursor work in a folder, so `found.csv` and `found.bib` land beside the code. The prompts are identical; the paste point changes.

## Part 5 — Decisions, limits, what it is worth

**Decisions.** Two steps only, because an entry that does everything teaches nothing. Both instruments, because some literature should arrive by itself and some questions should be asked on demand. Remix over rebuild for Zotero: take one simpler module apart instead of writing a reference manager — its source is public, and its licence was checked before anything of ours was shared.

**Limits.** An agent asked to *remember* a paper invents one that sounds right; asked to *fetch* it, it cannot — so every value above arrives from OpenAlex or does not appear. A DOI proves a paper is real, not that its findings are right. RSS still needs a human to decide what deserves a click. And a public API stays free because its users are polite: one `mailto`, no hammering.

**Value.** An afternoon of tab-hunting becomes a two-minute query, and the second run is free: this Friday's search is last Friday's script with a new date. The list that returns is already sorted and filed, yours to filter by project. Gosztyla's answer to her own crisis was a system. This is that system's first two steps, running on instruments a beginner can drive in an afternoon.

## Closing — the cycle this starts

One query on one real topic returns a table too good not to open. The reader opens one. Tomorrow the same prompt returns something new, and the pipeline stops being a demo and becomes theirs. The platform first, the habit second — the reading, the notes and the organizing get picked up the same way, one working piece at a time.

---

**Footnotes:** ¹ Gosztyla, M. (2022). *How to find, read and organize papers*. Nature Careers, 07 July 2022. doi:10.1038/d41586-022-01878-7. ² OpenAlex verified 8 Nov 2026: 26,881 results for `search=applied linguistics AI`, `from_publication_date:2026-01-01`. ³ WorkBuddy capability test Stage 1 (GET) passed 7 Nov 2026 — [procomm#9](https://github.com/tesolchina/procomm-microlearning/issues/9). ⁴ Zotero source: github.com/zotero/zotero; licence check logged in [#12](https://github.com/tesolchina/procomm-microlearning/issues/12).

**Reviewer box:** Bremen Vance · Comments: open, moderated · Companion code: `workshop/`.

*≈1,400 words. De-AI pass applied at assembly (WI-6, #14): tells checklist + `humanize_check.py` before deploy.*

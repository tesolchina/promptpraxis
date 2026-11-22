# Part 3 revision record — 22 Nov 2026

**Source:** Simon's dictated revision, recorded in Otter: https://otter.ai/u/1KoHE391KsDyq9qIOGeAa-TfJCs (title *"Editing Text for Style and Subject"*, 5 min 28 s, fetched via public speech API 22 Nov 16:19 HKT; raw transcript deposited beside this file as `part3-otter-transcript.txt`).

**Applied by:** agent session, 22 Nov 2026, 16:19–16:22 HKT. Deployed live to https://procomm.ieee.org/ai-resources/prompt-and-praxis/entry02/ (embed md5 `2178da46…`, local == live).

Sub-issue: [#25](https://github.com/tesolchina/promptpraxis/issues/25) (Part 3, self-assigned to Simon).

## His dictation → what changed

| # | Simon said (paraphrased from transcript) | Applied |
|---|---|---|
| 1 | *"Heading should be fine"* | Heading **unchanged**: "Enhancing GUI software solutions with agentic-AI-powered API programming" |
| 2 | *"Remove all the colons — every time there's a colon, it's very AI"* | **0 prose colons** in Part 3 (audit built into `part3_revise.py`); replaced with semicolons/commas or restructure; only the structural `## Part 3:` heading marker remains |
| 3 | First sentence: *"the tools presented in part two… interact with users through graphical user interface involving windows, buttons and menus that a user would need to interact through hands"* | Para 1 opens: **"The tools presented in Part 2 interact with users through a graphical user interface (GUI), involving windows, buttons and menus that the user drives by hand, one screen at a time."** |
| 4 | *"Instead of the software doing this and that, we say the users doing this and that — the users are the ones who interact with the GUI"* | "The RSS reader shows… Zotero shows…" → **"Users see incoming journal issues as a list to click through in the RSS reader, and their Zotero library as folders to drag files into."** Plus the general rule applied across the part: **no API/GUI/tech-term as sentence subject** ("Through an Application Programming Interface (API), code reaches…" — API moved to a prepositional phrase) |
| 5 | *"The strength of GUI is easy to pick up, but the speed is constrained… that's why we transition to the second paragraph, through programming we can do things much faster"* | Virtue+limit sentences merged ("…productive in minutes, but its boundary is speed…") and para 2 now opens **"With programming, the same tasks run much faster."** |
| 6 | *"Part four puts this in your hands — very AI. Say: in part four, we will discuss…"* | Both instances: mid-part transition removed; the part now ends **"In Part 4, we will put this pipeline into practice."** (his formula) |
| 7 | *"We did not really refer to the table — we need to refer to the table a little bit"* | Lead-in sentence before the table: **"The table below contrasts the two approaches."** |
| 8 | *"In entry one, we have described how agentic AI can serve as a bridge between human language and the computer instruments"* | **"In Entry 1, we described how agentic AI can serve as a bridge between human language and computing instruments."** (Entry 1 link kept) |

## Also applied (Traci's marks for this part, from [#25](https://github.com/tesolchina/promptpraxis/issues/25))

- **Struck sentence removed**: "Programmed code has no hands or eyes: it runs a query at dawn…" (her strikethrough; also removes a colon)
- Boundary sentence rephrased: "a boundary we preserve:" → "a boundary that this entry preserves. **The agent reasons, and the database supplies the facts.**"
- **Fixed a pre-existing typo**: the HTML had "and and the agent writes the code" (double "and" — was present in Traci's OCR too)
- Short sentences merged/removed per both briefs (his last note: *"when a sentence is short, reconsider"*)

## Decisions made (flagged for Simon)

1. **API kept capitalized** — Traci marked lowercase ("not a proper noun"), but the merged Parts 4–5 deploy with `API` caps (e.g. Part 5's bold sentence), so lowercasing Part 3 alone would be inconsistent. Held pending a global casing decision.
2. **Final sentence** "Part 4 puts the pipeline into practice." was dropped rather than rewritten, because his "In Part 4, we will…" formula now closes the part — two transitions would repeat.
3. Traci's wider Part-3 marks not dictated by Simon (whole-paragraph de-AI rewrite) are satisfied by dictation points 3–5.

## Verification (live, 16:22 HKT)

- PRESENT ×5: "The tools presented in Part 2 interact with users" · "In Part 4, we will put this pipeline into practice" · "The table below contrasts the two approaches" · "we described how agentic AI can serve as a bridge" · "With programming, the same tasks run much faster"
- ABSENT ×6: "Programmed code has no hands or eyes" · "puts this in your hands" · "That is the GUI" · "makes this reachable" · "boundary we preserve" · "and and the agent"
- md5 local == live `2178da46f31e9e9b4816927b8cd63672`

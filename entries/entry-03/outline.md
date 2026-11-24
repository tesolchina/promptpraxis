# Entry 03 — outline (draft for review)

**Scope decision (Simon, Otter *Planning Blog Entry Three*, 7:34, fetched 22 Nov 2026):**
Entry 03 covers **Step 3 (read) only** — *"we should probably only do step three for entry number three because organization would be a different one"* (Step 4 → a later entry).
**Core idea:** Gosztyla's Step-3 advice is about *disconnecting* from technology; LLMs can instead **read with you** — demo = turn a research article into a **visually appealing mind map (Mermaid)** using **per-section rhetorical templates**.
**Series note:** entries can later become a **workshop / workshop series** (hands-on training that upgrades pre-LLM published workflows).

**Co-authors:** Wenyun (Winnie) FU (Journalism, HKBU) and Zian (Andy) Zheng (Computer Science, HKBU) — same guest-panel treatment as Entry 2 (collapsible panel, portraits from `assets/`).

## Working title

*Reading with agentic AI: turning a paper into a structure you can see* — (open)

## Standfirst (v1)

Step 3 of a 2019-style... — see page (drafted in the gated page)

## Parts

### Part 1 · The tricky part
- Gosztyla Step 3: *"the tricky part — you have to actually read"*; the key is a streamlined routine
- Her five suggestions: **build time** into the schedule (Friday mornings) · **develop a workflow** (skim → careful read → highlight → short summary) · **block out time** (or purge the stack) · **minimize distractions** (PDF reader not browser; Zotero's built-in reader extracts highlights to searchable text; Wi-Fi off; phone on DND, in another room) · **have fun** (couch + fancy coffee)
- Entry 2 took Steps 1–2; this entry takes Step 3. ⚠️ **Follow-up:** Entry 2's Part 1 still promises *"Entry 3 picks up steps three and four"* — needs a one-line edit once this scope is confirmed.

### Part 2 · What the routine leaves to you (pre-AI baseline)
- Her remedies are sound but they work by *resisting* technology; nothing in them reads for you
- What changes with agentic AI: **structure, claims and limits can be extracted** — the judgement of them stays human (series rule: the agent reasons, the paper supplies)
- honest beat: routine / blocking / distraction advice still stands

### Part 3 · From screen to structure (the bridge)
- Reuse Entry 2's GUI→API move: reading itself stays human; **mapping the text is delegable**
- Introduce **Mermaid as the mind-mapping tool**, plus the honest problem: default Mermaid is *plain* → this entry styles it (theme, colour, layout) into something visually appealing
- **Section-aware templates** (the core design):

| Paper section | Structure to map |
|---|---|
| Introduction | **CARS** moves — establish territory → indicate gap → occupy niche |
| Literature review | themes (how the lit is organised) |
| Method | flow chart of steps |
| Theoretical framework | connected boxes |
| Findings / Discussion | argument structure (to be specified) |
| Whole paper | one overview map |

### Part 4 · Next steps with WorkBuddy (demo outline)
1. **Planning contract** prompt (series convention)
2. **Choose the paper** — ⚠️ **OPEN: pick one good open-access paper** (Simon: *"we need to find a good paper"*); needs clear section structure
3. Give the agent the paper (URL/PDF) → it extracts the section-by-section structure and the moves inside each
4. Per-section maps with the matching template from the table
5. **Whole-paper overview map**
6. **Visual upgrade pass**: Mermaid `themeVariables` / `classDef`, fonts, layout — target: "visually more appealing than plain Mermaid"
7. Outputs: Mermaid source committed to the repo; maps embedded in the entry; reading status ties back to Entry 2's `found.csv` Reading_Status column

### Part 5 · Decisions, limits, value
- Scope: Step 3 today; Step 4 (organize) deferred — say so explicitly
- Limits: an agent can misread a paper's structure → check every map against the text; maps are orientation aids, not reading substitutes; personal-use mapping of copyrighted papers
- Value: a 40-page paper becomes a 10-minute orientation before the deep read

## Open questions for Simon
1. ~~Which paper for the demo~~ — **CHOSEN** (Jwa, JSLW 75 (2027) 101387; see Part 4)
2. Mermaid rendering: live `mermaid.js` in the embed (interactive) vs pre-rendered PNG/SVG?
3. Create the WordPress `entry03/` page now (with WP-side gate) or keep the preview embed-only for now?
4. Title + standfirst approval
5. Cadence/deadline vs the series' two-week rhythm

## Later roadmap (Simon, 22 Nov 2026)

1. **A skill for users to analyze other papers** — package the per-section mind-mapping workflow as a reusable agent skill (transfer from Entry 02's demo prompts).
2. **A BYOK frontend** — upload-a-paper interface (bring-your-own-key) so readers can run the analysis on their own PDFs in the browser.

## Build conventions inherited (from Entry 02)
- Build chain: `entry_body.html` + `header.html` → `build.py` → `02-embed.html` → upload to `ieee/` on the ECS box (NOT `/var/www/blog.ieee/assets` — path trap documented)
- **Gate rule (Simon, 24 Nov 2026): password gates live INSIDE the iframe embed (`0X-embed.html`), never in WordPress content** — removing a password must never involve a WordPress operation. (Entry 02's WP-side gate was stripped 24 Nov via REST with fresh credentials; entries 03+ gate embed-side only, same SHA-256 pattern, series password.)
- Style rules learned in Entry 02 (Traci): **no prose colons**, **users as sentence subjects** (no GUI/API/tech-terms as subjects), parallel headings, reference tables/figures before showing them, word cap ~1,600

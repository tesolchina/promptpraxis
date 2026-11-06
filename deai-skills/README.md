# deai-skills — making text stop sounding like a machine

A public, curated subset of Simon Wang's private [vibecodingskills](https://github.com/tesolchina/vibecodingskills) collection, published here because colleagues asked to use the **de-AI** skills: the ones you run when a draft is *correct* but still smells machine-written.

**Maintained by [Simon Wang](https://github.com/simonwanghkteacher).** Colleagues: copy, adapt, PR — issues and pull requests welcome. Simon updates this folder from now on; the private repo stays the source of truth.

De-AI ≠ word-swapping. The goal is to write the way a thoughtful person writes: concrete subjects, plain verbs, uneven rhythm, one idea per sentence, and an ending that lands — while never inventing content the author did not supply.

---

## The skills in this folder

| Skill | What it does | When to use it |
|---|---|---|
| [`humanizing-ai-text.md`](humanizing-ai-text.md) | The core **tells playbook** — punctuation/rhythm tells (em dashes, even sentence lengths), structural tells (rule-of-three triads, "not X but Y", throat-clearing connectives, hedge stacks), word-choice tells (abstract nouns, personification, inflated register), plus positive habits and a pre-send checklist. Grown from real SCMP + Nature letter revision rounds. | Start here for any prose pass. Shortest read, highest yield. |
| [`academic-writing-style/SKILL.md`](academic-writing-style/SKILL.md) | Editorial repair for academic manuscripts: tense discipline, actor-first sentences, em-dash → comma, lexical preferences, structural economy — **plus §10 "Voice Restoration"**, the de-AI section: observed differences between what a model writes and what the author writes (antithesis → question, labelled phases → chronology, capability list → purpose clause, *exist* → an actual action), and the shipping test: *"could the author have written this sentence?"* | Manuscripts, reports, any text that must sound like a specific person. |
| [`scmp-letter-writing/README.md`](scmp-letter-writing/README.md) | The letters craft file. De-AI core: **§ "Reducing AI smell"** (fragment sentences, choppy two-beat openers, validation openers, universal quantifiers, "not just X but Y", over-hedged closings, imperative endings, unexplained jargon, absolute quantifiers) and **§ "New AI-smell patterns"** (meta-announcement sentences, orphaned transitions after an edit, stacked attribution, undigested topic switch, decorative triads, aphorism-in-the-ask, choppy unbridged sentences) — all evidenced by real editor/writer feedback. | Short op-ed / letter / op-ed-length prose, especially opinion genres. |
| [`paper-spine-humanize/`](paper-spine-humanize/) | The **detector-risk** layer: `humanize.md` (tiered dimensions D1–D5, three-round revision loop, disclaimers), `humanize-calibration.md`, `platform-cnki.md` / `platform-weipu.md` / `platform-general.md` (platform risk mappings), and `humanize_check.py` — a **standalone, stdlib-only script** that measures sentence-length CV, connector density, etc. and writes `humanize_report.md`. | When a manuscript must survive an AIGC check (CNKI/Weipu) *and* still read well. Run the script, fix required findings, re-run — max 3 rounds. |

**Deliberately not included:** `nature-polishing` (Nature-style polishing — its `style-guardrails.md` "AI boundary" is about *integrity*, not de-AI), and everything else in the 222-skill collection (agent workflows, deploy, video, Google Workspace, …).

---

## Usage

```bash
# 1. read the playbook
cat humanizing-ai-text.md

# 2. run the metric pass on a manuscript folder
python paper-spine-humanize/humanize_check.py path/to/draft --markdown --write
#    → humanize_report.md (required vs advisory findings)

# 3. apply the letter/manuscript skill of your genre, then the checklist
```

Two rules the skills enforce that are easy to get wrong:

1. **Do not add content while de-AI-ing.** A style pass must not introduce claims, features or details the author did not supply. De-AI means removing, not decorating.
2. **Never promise a detector pass.** `humanize.md` outputs no fabricated "AI rate"; thresholds are *local risk scans*, not any vendor's algorithm.

---

## Research basis — GitHub repos on the same topic (Nov 2026 survey)

This folder's skills were cross-checked against the public "humanizer" ecosystem. Findings have been folded back into the source skills in the private repo, with attribution. Upstream canon first, then the repos:

| Repo | ★ | What we took / confirmed |
|---|---|---|
| [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) (WikiProject AI Cleanup) | — | The **shared upstream canon** — ≥5 of the repos below cite it. We now cite it too. |
| [blader/humanizer](https://github.com/blader/humanizer) | ~65k | The de-facto standard: **26 numbered patterns §1–§26** in 6 groups (staging · rhythm · inflation/borrowed authority · formatting · chat leftovers · wrong reader). MIT. |
| [NulightJens/humanizer-stack](https://github.com/NulightJens/humanizer-stack) | ~380 | **Two-pass pipeline**: surface pass then structural pass. |
| [brandonwise/humanizer](https://github.com/brandonwise/humanizer) | ~130 | OpenClaw port built on the Wikipedia canon. MIT. |
| [gregorymm/humanize-text](https://github.com/gregorymm/humanize-text) | ~8 | **Scores 7 categories 1–10, then rewrites** — measurable before/after instead of vibes. |
| [nordefors-max/claude-humanizer-svenska](https://github.com/nordefors-max/claude-humanizer-svenska) | ~10 | Pattern types we were missing: **nominalization overuse, passive-as-false-formality, bullet/emoji formatting**. |
| [finestructure-ai/humanizer-multilingual](https://github.com/finestructure-ai/humanizer-multilingual) | ~3 | Covers **Chinese** + 9 other languages the English-only humanizers miss. MIT. |
| [daniel-bogale/anti-ai-writing-humanizer](https://github.com/daniel-bogale/anti-ai-writing-humanizer) | ~5 | Portable across Claude Code / Cursor / Codex / OpenClaw. MIT. |
| Language ports | — | [`bushrabeg/turkce-humanizer`](https://github.com/bushrabeg/turkce-humanizer), [`matsutouya/humanizer-ja`](https://github.com/matsutouya/humanizer-ja), [`monologg/humanizer-kr`](https://github.com/monologg/humanizer-kr), [`yelban/humanizer.TW`](https://github.com/yelban/humanizer.TW) |

### Five findings folded into our skills (acknowledged at point of use)

1. **Structure beats vocabulary** *(blader/humanizer)* — word habits change with every model release; *structural* habits persist. Lead with staging paragraphs, one-line closers, forced triads, dash-as-connector — not with a banned-word list.
2. **Pattern weighting** *(blader/humanizer)* — a few patterns act on a single sighting; others are marked *weak alone* and need co-occurrence before you rewrite. Sharper than a flat checklist.
3. **Voice-matching from a sample** *(blader/humanizer)* — if the writer supplies a sample of their own text, match sentence length, punctuation and dash rate to it; **the sample overrides the pattern rules**. This is now the recommended mode of `academic-writing-style` §10.
4. **"When not to act"** *(blader/humanizer)* — never touch quotations, titles, proper names, or pre-Nov-2022 text; actively *keep* specific odd details, mixed feelings, dated references and asides. Prevents over-de-AI-ing a voice into mush. Complements our §10.5 ("do not add content").
5. **Chinese + multilingual coverage** *(humanizer-multilingual, humanizer-svenska)* — our playbook was English-only; the nominalization/passive-as-formality tells and a Chinese-tells note were added to the source skills.

**Attribution convention used in this folder's source skills:** every borrowed rule carries an inline `Source: blader/humanizer (MIT) · Wikipedia "Signs of AI writing"` note; our own patterns remain evidenced by Simon's revision history instead.

---

## Provenance

- Source collection: [tesolchina/vibecodingskills](https://github.com/tesolchina/vibecodingskills) (private) — files copied verbatim on 6 Nov 2026; this folder is the shareable extract, not a fork of the whole collection.
- Context: [Prompt & Praxis](https://procomm.ieee.org/ai-resources/prompt-and-praxis/) — IEEE ProComm's resource collection.
- Related issue: see the repo's issues for the tracking thread and what's still open.

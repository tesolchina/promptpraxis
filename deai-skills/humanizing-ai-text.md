# Humanizing AI Text — a working playbook

A living file for one recurring problem: drafts that are *correct* but smell machine-written.
Started while finalizing the China-EV letters (SCMP + Nature), where almost every revision round
was us hunting one more "AI tell." Add to it whenever we catch a new one.

The goal is not to ban words. It is to write the way a thoughtful person actually writes:
concrete subjects, plain verbs, uneven rhythm, one idea per sentence, and an ending that lands.

---

## 1. The tells we keep catching (and what to do instead)

### Punctuation & rhythm
- **Em dashes (—).** The single loudest tell. We hold all letters to **0 em dashes** in the body.
  Use a comma, a full stop, or "(parentheses)" instead. (En dashes in number/page ranges are fine: 138–147.)
- **Every sentence the same length.** Machines write even, mid-length sentences. People don't.
  Put a short sentence next to a long one. Let one land hard.

### Structure tells
- **Rule of three / triads.** "mined, refined and recycled", "faster, cleaner and cheaper."
  Three balanced items in a row is a giveaway. Use two, or break the parallelism.
- **"Not X but Y" / "It's not just X, it's Y".** A favourite AI cadence. Say the positive thing directly.
- **"rather than", "instead of" as a rhetorical pivot.** Same problem. Make the point without the contrast scaffold.
- **Throat-clearing connectives:** "Moreover", "Furthermore", "Importantly", "It is worth noting that."
  Cut them. Start with the content.
- **Hedge stacks:** "may potentially", "could possibly help to". Pick one verb and commit.

### Word-choice tells
- **Abstract nouns standing in for the real subject.** "a transition praised for the air it cleans"
  instead of "electric vehicles." Name the actual thing. Concrete subject + active verb.
- **Personification of abstractions.** "the air it cleans", "the data tells us", "the policy seeks to."
  A person, a vehicle, a study can act. Air and data mostly can't.
- **Inflated register:** "leverage", "utilize", "underscore", "delve", "tapestry", "realm", "landscape",
  "in the realm of." Plain words read more human: use, show, area.
- **Empty intensifiers:** "truly", "significantly", "crucial", "vital" used as filler.

---

## 2. Positive habits (what good human revision does)

- **Name the subject.** Ask of each sentence: who or what is doing this? Put that noun in the subject slot.
- **Bookend / 点题.** Let the last line answer the first. EV-Nature letter: opens "records only **one side**
  of the account", closes "the full health **record** ... weighed **together**" (also echoing the headline verb).
- **Read it aloud.** Anything you'd never say to a colleague is a candidate for cutting.
- **Vary the rhythm on purpose.** After a long, qualified sentence, write a short blunt one.
- **Cut your first sentence.** The opening is usually warm-up. The real start is often sentence two.
- **Prefer the specific.** "nickel for its cathode and copper for its current collectors" beats
  "various critical materials."

---

## 3. Worked before / after (from this project)

| Round | AI version | Human version | Why |
|---|---|---|---|
| Nature close | "...so a transition praised for the air it cleans is judged by its full health account." | "...so the full health record of electric vehicles can be weighed together." | Abstract noun ("transition") + personified "air it cleans" → name the real subject; echo headline. |
| Nature P3 open | "...an interdisciplinary task that reaches well beyond air-quality science, and no single use-phase study could be expected to deliver it." | "A full reckoning therefore calls for interdisciplinary work that joins air-quality science with the chemistry of producing and recycling these metals." | Defensive/excusing framing → forward-looking positive call. |
| SCMP P2 | worker quote "dumped straight into the sewer" + Hunan rice/Yale link | plain statement: spent batteries flow to unlicensed shops, metals leach into soil and water | Dropped sensational quote and a strained link; measured tone. |

---

## 4. Quick pre-send checklist
- [ ] 0 em dashes in the body.
- [ ] No triad / "not X but Y" / "rather than" pivot.
- [ ] Every sentence has a concrete subject (no abstract noun or personified abstraction doing the verb).
- [ ] Sentence lengths vary; at least one short, punchy sentence.
- [ ] First sentence earns its place (or got cut).
- [ ] The ending echoes the opening or the title (点题).
- [ ] Read aloud once.

---

See also: skill `scmp-letter-writing` (house style + revision craft) and
`.agents/skills` `.agents/memory/nature-correspondence-style.md` (Nature vs SCMP citation rules).

---

## 5. Research basis — external canon (added 6 Nov 2026)

Cross-checked against the public "humanizer" ecosystem on GitHub; findings below are folded in
with attribution. The shared upstream canon for all of them is Wikipedia's
[Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) (WikiProject AI Cleanup).

1. **Structure beats vocabulary** — *Source: [blader/humanizer](https://github.com/blader/humanizer), MIT.* Word habits change with every model release; structural habits persist. Lead with staging paragraphs, one-line closers, forced triads, dash-as-connector — not a banned-word list.
2. **Pattern weighting** — *Source: blader/humanizer.* A few patterns act on one sighting; others are *weak alone* and need co-occurrence before rewriting. Do not treat every tell in §1 as equal.
3. **Voice-matching from a sample** — *Source: blader/humanizer.* If the writer supplies a sample of their own text, match sentence length, punctuation and dash rate to it; **the sample overrides the pattern rules**.
4. **When not to act** — *Source: blader/humanizer.* Never touch quotations, titles, proper names, or pre-Nov-2022 text; actively keep specific odd details, mixed feelings, dated references, asides. Pairs with §"do not add content" logic in `academic-writing-style` §10.5.
5. **Nominalization / passive-as-false-formality** — *Source: [nordefors-max/claude-humanizer-svenska](https://github.com/nordefors-max/claude-humanizer-svenska).* Heavy nominalization and passive voice used as fake formality are tells this playbook did not name; add them to the word-choice list. For **Chinese-language** text, see [finestructure-ai/humanizer-multilingual](https://github.com/finestructure-ai/humanizer-multilingual).

Public extract of these skills: [tesolchina/promptpraxis `deai-skills/`](https://github.com/tesolchina/promptpraxis/tree/main/deai-skills).

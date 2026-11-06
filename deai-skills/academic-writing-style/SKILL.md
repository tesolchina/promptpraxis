---
name: academic-writing-style
description: Apply editorial refinements that make academic manuscripts read more precisely and naturally — covering tense discipline, actor-first sentence structure, punctuation preferences, lexical choices, and structural economy. Use before sending any section to a reviewer, journal submission, or co-author, or when a draft feels "AI-written" and needs register repair.
---

# Academic Writing Style — Editorial Refinements

Distilled from systematic editorial feedback on empirical manuscripts in applied linguistics and related fields. Applies to any social-science or humanities paper reporting on reviewed literature, methodology, or data.

---

## 1. Tense Discipline (highest-frequency issue)

**Rule:** Use **past tense** throughout findings and methods sections. Present tense is reserved for (a) established truths, (b) live recommendations, and (c) timeless methodological principles.

| Draft (wrong tense) | Edited (correct) |
|---|---|
| "Studies *report* three distinct patterns." | "Studies *reported* three distinct patterns." |
| "The corpus *includes* 75 papers." | "The corpus *included* 75 papers." |
| "Researchers *seldom articulate* the unit." | "Researchers *seldom articulated* the unit." |
| "Papers *must* provide methodological detail." | "Papers *had to* provide methodological detail." |
| "Coders *are* trained before annotation." | "Coders *were* trained before annotation." |

**Audit procedure:**
1. Grep the manuscript body for present-tense reporting verbs: `include|report|show|find|suggest|indicate|identify|note|argue|claim|demonstrate`
2. For each match: is it a timeless fact or a finding from reviewed studies? If the latter, convert to past.
3. Exception list (keep present): "This paper *argues* that…", "The present study *contributes* to…", "Figure 3 *shows*…"

---

## 2. Actor-First Sentences

**Rule:** The most informative noun should open the sentence. Avoid time-phrase openers that bury the subject.

| Draft | Edited | What changed |
|---|---|---|
| "The past two decades have seen growing interest in X." | "Interest in X has grown substantially since 2005." | Key noun first; date specified |
| "There is a notable gap in the literature regarding Y." | "No study has examined Y in a corpus of Z." | Concrete claim replaces vague gap statement |
| "This review surfaces several noteworthy patterns." | "This review identifies three patterns." | Active verb; evaluative adjective deleted |
| "A notable addition to the picture of X is Smith (2021)." | "Smith (2021) introduced the concept of…" | Author as subject; concrete verb |

**Check:** search for sentences beginning with "There is/are", "The past X years", "It is", "This section". Restructure so the key actor/noun is the grammatical subject.

---

## 3. Punctuation: Em-dash → Comma

**Rule:** Commas handle most parenthetical elaborations. Em-dashes signal a genuine pivot or emphasis — use them sparingly.

| Draft | Edited |
|---|---|
| "Move analysis — the systematic identification of rhetorical units — has been widely applied." | "Move analysis, the systematic identification of rhetorical units, has been widely applied." |
| "Three studies — all published post-2015 — report kappa above .80." | "Three studies, all published post-2015, report kappa above .80." |

**Keep em-dashes when:** the interruption is abrupt, emphatic, or pivoting mid-thought — not for routine apposition.

---

## 4. Lexical Preferences

| Avoid | Prefer | Reason |
|---|---|---|
| "surfaces" (as verb) | "identifies", "reveals", "shows" | "Surfaces" feels metaphorical/informal |
| "noteworthy" | [delete, or use "notable"] | Evaluative adjective that signals the writer's surprise, not a fact |
| "especially" | "particularly" | Minor register preference in formal prose |
| "across the X–Y period" | "over the X–Y period" | "Over" for time; "across" for spatial/categorical extent |
| hyphen-free compound modifiers | hyphenate before noun | "move-analysis studies", "corpus-based research", "large-scale survey" |
| "studied" (for what researchers investigated) | "examined", "investigated", "analysed" | More precise verbs |

---

## 5. Structural Economy

**Rule:** Every standalone sentence must carry unique information. Delete any sentence whose entire content is restated in the paragraph that follows it.

**Pattern to eliminate:**
> "This section examines three methodological dimensions." *(opening sentence)*
> "The first dimension is…" *(paragraph immediately below)*

The opening sentence adds nothing the paragraph doesn't cover. Cut it.

**Other economy cuts:**
- "It should be noted that X" → "X" (the noting is implicit in writing it)
- "Interestingly, X" → "X" (let the reader find it interesting)
- "In order to X" → "To X"
- "Due to the fact that" → "Because"

---

## 6. Parallel List Formatting

**Rule:** No trailing comma before "and" in a parallel RQ or item list.

| Draft | Edited |
|---|---|
| "…what genres were studied, and how were corpora justified?" | "…what genres were studied and how corpora were justified?" |

Use the Oxford comma for lists of **nouns** (A, B, and C), but not for conjoined clauses.

---

## 7. Criteria and Modal Language

**Rule:** When describing inclusion/exclusion criteria that were applied in the past, use past-tense modals.

| Draft | Edited |
|---|---|
| "Papers must focus on empirical analysis." | "Papers had to focus on empirical analysis." |
| "Studies must report inter-rater reliability." | "Studies were required to report inter-rater reliability." |

---

## 8. Pre-Submission Checklist

Run through this before sending any section to a reviewer or co-author:

- [ ] **Tense audit** — findings/methods in past tense; grep for present-tense reporting verbs
- [ ] **Actor-first** — no sentences opening with "There is/are", "The past X years", "It is"
- [ ] **Em-dash audit** — replace parenthetical em-dashes with commas
- [ ] **Redundant openers** — delete standalone sentences subsumed by the paragraph following them
- [ ] **"Surfaces" / "noteworthy"** — replaced with "identifies" / "notable" or deleted
- [ ] **Temporal span** — "over X years" not "across X years"
- [ ] **Compound modifiers** — hyphenated before noun
- [ ] **Criteria language** — "had to" not "must" for past-applied criteria
- [ ] **List commas** — no trailing comma before "and" in conjoined clauses
- [ ] **Table titles** — no trailing full stop
- [ ] **Economy check** — every standalone sentence carries unique information

---

## 9. Quick Diagnostic Prompts

If asking an LLM to review a section, use these targeted prompts:

```
Identify all present-tense reporting verbs in this text that describe
what reviewed studies did or found. List them with their line context.
```

```
Find all sentences beginning with "There is", "There are", "The past",
"It is", "This [noun] [verb]s". Suggest actor-first rewrites.
```

```
Find all em-dashes used for parenthetical elaboration (not pivots).
Replace with commas and show the result.
```

---

## 10. Voice Restoration — What an Author Does That the Model Does Not

**When this section applies:** you are editing text that must sound like a specific person, not like good prose. Derived from a real rewrite (Oct 2026): an agent-edited blog entry that the author rewrote in his own voice. Every pattern below is an observed difference between the two versions, not a preference.

**Sections 1–7 are for manuscripts where the agent is the stylist. Where they conflict with this section, this section wins** — in particular 3 (em-dash → comma) and 6 (list punctuation), which can flatten an author's rhythm if applied mechanically.

### 10.1 Balanced antithesis → a plain question

> **Model:** "Waiting for access is one response; building our own is the other, and it raises the question this entry answers: could a teacher without a programming background build a comparable artefact?"
> **Author:** "Instead of waiting, could a teacher without a programming background build a comparable artefact?"

The *X is one thing; Y is the other* frame is a model tell. One clause plus a question does the same work without the symmetry.

### 10.2 Labelled phases → chronology

> **Model:** "**Input.** … **Processing.** … **Output.** …" (three labelled paragraphs)
> **Author:** "Before the advent of large language models … Yet, this demo was created in an afternoon … Instead, I gathered … After several rounds of negotiation … This approach … has been known as vibe coding."

Models segment by abstraction (input/process/output). Authors narrate by time and contrast (before / yet / instead / after / this). Keep the framework if the piece is an explainer; drop the labels if it is a story.

### 10.3 Capability list → purpose clause

> **Model:** "A progress bar paces it section by section. Each section ends with one comprehension question."
> **Author:** "Multiple choice questions were used to check students' comprehension before they progress to the next learning stage."

Every feature carries the need it serves. If a feature cannot be given a reason, the author probably did not want it named at all — see 10.5.

### 10.4 Compressed aphorism → situated observation

> **Model:** "Every class I teach contains students who need the same content at different levels, in different forms, at different paces."
> **Author:** "Throughout my teaching career, I meet students from diverse backgrounds taking the same courses who need the materials at different levels, in different forms, at different paces."

The model writes the generalised, balanced version. The author anchors it in a career, a room, a habit.

### 10.5 Do not add content while de-AI-ing

The agent's edit introduced a progress bar and a staged scenario the author had never mentioned; he removed both. **A style pass must not introduce claims, features, or details the author did not supply.** De-AI means removing, not decorating.

### 10.6 Resist uniform short sentences

An earlier pass split one long paragraph into six single-clause sentences for "readability". The author merged them back into a paragraph with concessions and a dash. Short and readable are not the same thing: read the author's existing rhythm before shortening anything.

### 10.7 Keep the author's lexicon; raise correctness separately

If an author writes "codes" or "natural languages" consistently, that is his voice. Do not silently normalise it — note it as a question and let him decide. Silently correcting a writer's vocabulary is another way of replacing him.

### 10.8 The test to apply before shipping an edit

Not "does this read better?" but: **could the author have written this sentence?** Reread a paragraph he wrote himself immediately before editing. If your edit is smoother and flatter than his, it has drifted back towards the model.

### 10.9 "Exist" is a relationship-free verb

> **Draft:** "the clarity, sequencing and audience awareness we teach now decide whether a piece of software **exists** at all."
> **Author:** "…now **shape what the machine is asked to build**."
> Also caught in the same piece: "the page had an address the moment it **existed**" → "the moment it **was built**."

*Exist* asserts presence and nothing else: no agent, no purpose, no relation. In writing about making things, use the verb that names the relationship — what was built, by whom, from what, for whom. It is also a habitual hedge: "this exists" claims something without saying what it does or who it serves.

**Rule:** search the draft for `exist|exists|existing|existence` and rewrite every hit as an action or a relation. If the sentence loses nothing when the word is deleted, the word was carrying nothing.

---

## 11. External canon — adopted rules with attribution (added 6 Nov 2026)

Folded in from the public "humanizer" ecosystem after a GitHub survey; keep the attribution when editing these lines. Shared upstream: Wikipedia [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing).

- **Voice-matching from a sample** *(Source: [blader/humanizer](https://github.com/blader/humanizer), MIT)* — when the author supplies a sample of their own writing, measure its sentence length, punctuation and dash rate and match them; **the sample overrides sections 1–7 and, on conflict, even section 10**.
- **Pattern weighting** *(Source: blader/humanizer)* — act on a single sighting only for the high-signal patterns (staging, one-line closer, forced triad, dash-as-connector, "not X but Y"); other patterns are *weak alone* and need co-occurrence before a rewrite.
- **When not to act** *(Source: blader/humanizer)* — never rewrite quotations, titles, proper names, or text written before Nov 2022; deliberately *keep* specific odd details, mixed feelings, dated references and asides.
- **Structure over vocabulary** *(Source: blader/humanizer)* — word lists rot with each model release; structural habits persist. Check structure first, words second.

Public extract of this skill set: [tesolchina/promptpraxis `deai-skills/`](https://github.com/tesolchina/promptpraxis/tree/main/deai-skills).

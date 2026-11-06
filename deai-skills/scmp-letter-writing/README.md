---
name: scmp-letter-writing
description: Draft and revise Letters to the Editor for the South China Morning Post (SCMP), in Simon Wang's / HKBU house style. Use when the user asks to write, revise, tighten, or fact-check an SCMP letter, a "letter to the editor", or a response to an SCMP article. Covers house style, the opening/closing formulas, sourcing/linking rules, the revision craft lessons learned across real drafts, and the SCMP submission process.
---

# SCMP Letter Writing

Write Letters to the Editor for the *South China Morning Post* that read like a real academic wrote them — specific, sourced, and human — not like AI filler. This skill captures the house style and the craft lessons distilled from many rounds of real revision (the Shenzhou-23 / HKBU letter, v3→v10).

Working drafts live in `data/scmp-collab/LetterSpace/` as `draft-vN.md`. Always create a **new** `draft-v{N+1}.md` for each revision and append a `## What changed from vN` section — never silently overwrite. The worked example from a finished letter is `docs/letterSpace/draft-en.md`.

## House style (hard rules)

- **Length: 200–400 words.** Simon prefers **≤ 200** — in practice the working target is **~200 words** (see the EV-subsidy session lessons below); 300 only when the data demands it. When students co-author, leave ~25 words of headroom.
- **≥ 2 inline parenthetical hyperlinks**, Markdown style: `([SCMP, 23 May](https://...))`. Links go *inside* the sentence in parentheses, right after the claim they support.
- **No APA brackets.** Never `(Smith, 2024)`. Cite by linking the source name inline instead.
- **No bullet points.** Continuous prose only.
- **Signature block** at the end. Format that's been used: `*Andy Zheng and Yuxi Jia, students, and Simon Wang, lecturer — Hong Kong Baptist University*`. Confirm each person's exact English-name spelling and their role label before finalising.
- **No headings inside the letter body.** The title line, then prose paragraphs, then signature.

## The opening formula

Open the way published SCMP letters from academics actually open — formal, anchored to a specific article:

> **"We refer to your report on** [subject] **("**[exact article headline]**", [SCMP, [date]](url)).** While [X] is clearly worth celebrating, **the harder, slower work begins once** [the real point] …"

Key moves:
- Formal verb: **"We refer to your report on…"** (not "Coverage of X rightly celebrates…" — that's an AI tell).
- **Quote the SCMP article's headline verbatim** in quotation marks, with an inline dated link. It signals you actually read the piece.
- The **"While X is worth celebrating, the harder/slower work begins once…"** pivot moves from the obvious story to the overlooked one. This is the spine of most of these letters.

## The closing

Make it **punchy and profound, specific to the research/subject the letter highlights** — not a generic "this is overlooked" sign-off. The strongest closers reframe the whole subject:

> "The launch earns the headline, but **a mission is judged by what survives it** — a crew brought safely back to Earth, and data turned into action on a warming planet. Both are **won on the ground, in Hong Kong's labs, long after the cameras have moved on.**"

The pattern: a single insightful turn ("judged by what survives it") that recasts the headline event as the *less* important part, then a concrete, vivid line tying the two highlighted contributions together. Avoid choppy two-beat openers ("X is the headline. Y is the story."). One flowing clause hits harder.

## Sourcing & linking rules (learned the hard way)

- **Link to stories about the work, not CV pages.** A subject's staff bio / scholars-profile / department page is "useless" — link instead to news articles, press releases, or features that describe what they actually did. (Real correction from a live draft: two HKBU staff/scholars links for a professor were rejected; replaced with the HKUST press release + the HKBU WeChat feature that quote his role.)
- **Quote the subject's own words verbatim** when a source gives them. Direct quotes ("credible, usable, actionable") add the human texture that separates a real letter from generated prose. Translate faithfully if the source is Chinese, and note it's a translation.
- **Pull a concrete, specific detail** from each source, not a generic summary. "An adjustable-backrest recline that eases the spinal load on astronauts returning after months in microgravity" beats "designed the landing chair." The specific detail is *why* the contribution is worth a reader's attention.
- **Verify every link returns 200 before submission.** Quick check:
  ```bash
  for u in "URL1" "URL2"; do
    echo "$(curl -s -o /dev/null -m 10 -A 'Mozilla/5.0' -w '%{http_code}' -L "$u")  $u"
  done
  ```
- **Be honest about gaps.** If no public source names a person in the relevant context, say so plainly and offer options (link the project not the person, link a paper, email the comms office for an English release) rather than fabricating or stretching a citation.
- Research helpers available in this repo while drafting: `POST /api/scmp-collab/web-search` (Brave), `POST /api/scmp-collab/academic-search` (OpenAlex; Consensus needs a paid plan). Both take `{"query": "..."}`.

### Google Docs link format — encapsulated hyperlinks

When drafting in Google Docs, links must be **encapsulated**: the URL is never
visible in the document body. The reader sees only blue underlined anchor text
embedded naturally in the prose; clicking it opens the source.

**Wrong** (raw URL or parenthetical citation visible in the text):
> …wept at the final whistle (Al Jazeera, 16 June 2026 — https://www.aljazeera.com/…).

**Right** (encapsulated — anchor phrase is part of the sentence):
> …he made [**seven saves against Spain**], became only the third keeper over 40…

Rules for choosing the anchor phrase:
- It must be a meaningful clause already in the sentence — not "click here" or "source".
- It should tell the reader *what they are clicking on* without revealing the URL:
  "seven saves against Spain" signals the Vozinha profile; "73 officials were handed lifetime bans" signals the Al Jazeera corruption piece.
- One phrase per claim. Don't pile two citations onto the same anchor.

**Programmatic insertion via Google Docs API (one `batchUpdate` call):**
1. Build the complete text string.
2. For each link, find its 0-based `indexOf(phrase)` in the string.
3. In the `batchUpdate` requests array: `insertText` first (at the target Doc index),
   then one `updateTextStyle` per link with `textStyle: { link: { url } }` and `fields: 'link'`.
   Each range offset = insert Doc index + 0-based char index (Docs API is 1-based, so
   if you inserted at index *N*, phrase at string position *P* lives at Doc index *N + P*).

**To update only the link URL on existing anchor text** (without re-inserting text), use a
single `updateTextStyle` per anchor phrase:
```js
// Walk all paragraph elements, accumulate fullText + each segment's startIndex,
// then find phrase → docStart. No insertText needed.
requests.push({
  updateTextStyle: {
    range: { tabId, startIndex: docStart, endIndex: docStart + phrase.length },
    textStyle: { link: { url } },   // url may include #:~:text= fragment
    fields: 'link'
  }
});
```
This is the correct pattern for post-draft link fixes (e.g. adding text fragments or
swapping a dead URL) because it leaves all text content unchanged.

### Chrome text-fragment deep links (`#:~:text=`)

After inserting encapsulated hyperlinks, add a **Chrome text-fragment anchor** to every
URL so the reader's browser scrolls to and highlights the exact supporting passage:

```
https://example.com/article#:~:text=encoded%20phrase%20from%20the%20page
```

**Why:** A link to the whole article makes the reader hunt for the evidence. A fragment
link drops them directly onto the highlighted sentence — closer to inline footnote
behaviour.

**How to find the right fragment text:**

```python
import subprocess, re, urllib.parse

def curl(url):
    r = subprocess.run(['curl','-sL','-A','Mozilla/5.0','--max-time','15',url],
                       capture_output=True, text=True)
    return r.stdout

def clean(html):
    t = re.sub(r'<script[^>]*>.*?</script>','',html,flags=re.S)
    t = re.sub(r'<style[^>]*>.*?</style>','',t,flags=re.S)
    t = re.sub(r'<[^>]+>',' ',t)
    return re.sub(r'[ \t]+',' ',t)

def find_frag(text, keywords, n=7):
    """Return (url-encoded fragment, context sentence) for first keyword hit."""
    for kw in keywords:
        idx = text.lower().find(kw.lower())
        if idx == -1: continue
        chunk = text[max(0,idx-80):idx+300]
        for sent in re.split(r'(?<=[.!?])\s+', chunk):
            if kw.lower() in sent.lower() and 6 < len(sent.split()) < 60:
                kpos = sent.lower().find(kw.lower())
                wb = max(0, len(sent[:kpos].split())-1)
                words = re.sub(r'\s+',' ',sent).strip().split()
                frag = ' '.join(words[wb:wb+n]).strip('.,;:—"\'')
                if len(frag) > 15:
                    return urllib.parse.quote(frag), sent.strip()[:280]
    return None, None

t = clean(curl('https://example.com/article'))
frag, ctx = find_frag(t, ['key phrase from your claim'])
# frag is already URL-encoded; append to base URL:
print(f"https://example.com/article#:~:text={frag}")
```

**Encoding rules:**
- Space → `%20` (not `+`).  Dollar → `%24`.  Comma → `%2C`.  Quote → `%22`.
- Chrome's text-fragment spec normalises whitespace, so Wikipedia's
  `"Lionel Messi , who equaled"` (space before comma) is fine as
  `#:~:text=Lionel%20Messi%20%2C%20who%20equaled%20the%20record`.
- Keep fragments **5–8 words** starting one word before the key term —
  long enough to be unique on the page, short enough to survive minor edits.

**Verify before committing:** open `BASE_URL#:~:text=YOUR_FRAGMENT` in Chrome.
The browser should scroll to and yellow-highlight the target sentence.
If it does not, the encoded phrase does not match the live page text exactly —
re-fetch and adjust.

**Gotchas discovered on the china-football letter (July 2026):**

| Issue | What happened | Fix |
|---|---|---|
| Dead link, no Wayback snapshot | Al Jazeera (Vozinha / 73 bans), Open the Magazine, Xinhua — all 404 with zero archived snapshots | Find a different outlet covering the same claim; replace the whole URL |
| Article content changed | NBC Bay Area article on "why China fails at soccer" became a WC goals listicle | Replace with a different source for the fact |
| ESPN story IDs guessed | Fabricated IDs return HTTP 202 with an empty body — not a real article | Do not guess ESPN story IDs; search the site or use a known URL |
| SixthTone ID ≠ topic | `sixthtone.com/news/1013456` has a numeric ID; the slug is ignored — the ID resolved to a pandemic hospital article, not a football fees article | Search SixthTone by topic keyword, not by guessing IDs |
| Source doesn't say what you think | The Conversation article on Chinese football mentions youth-player decline (600 K → 7 K) but never uses the phrase "pay-to-play fees" | Either find a source that uses the term, or reword the anchor to match what the source actually says |
| Wayback Machine API check | `https://archive.org/wayback/available?url=ENCODED_URL` returns `{"archived_snapshots":{}}` if no snapshot exists | Check before promising a cached fallback; many 2026 breaking-news URLs have no snapshot |

**Fallback hierarchy when the original URL is dead:**
1. Wayback Machine API → use `closest.url` if `available: true`.
2. Same outlet, different URL pattern (check site's search or sitemap).
3. Different outlet reporting the same fact (AP, Reuters, BBC, Guardian, SCMP).
4. Wikipedia article on the person / event (confirms the fact, even if less specific).
5. Tell the user honestly — do not fabricate or guess URLs.

**Applying fragments to existing Google Docs links in bulk:**
Use the "update-only" `updateTextStyle` pattern above (no `insertText`) — one request
per anchor phrase per tab. Build all requests into a single `batchUpdate` call.
`tabId` must be specified in the range when the doc uses named tabs.

## Revision craft (recurring notes from real edits)

- **Avoid negations that raise an objection nobody would reach.** "human-factors engineering, not decoration" invites the reader to think "decoration?" — cut it. State what the work *is*; let the reader conclude.
- **Don't overclaim with sweeping quantifiers.** "the unglamorous downstream half of *every* satellite mission" was flagged on "why every" — drop universal claims you can't stand behind.
- **Collapse laboured transitions.** A two-sentence "here's the theme / the theme also appears here" bridge can usually become one half-sentence: "The same research depth is built into the hardware that brings every Shenzhou crew home: …".
- **Lead with content, never an empty Socratic question.** (This is the documented failure mode of the collab AI prompt — see `replit.md`.) Each paragraph delivers substance first.
- **Titles should foreground the angle the letter argues**, not the news peg alone. "The university research behind Hong Kong's first astronaut" (argues the angle) beats "Hong Kong's space story extends well beyond launch day" (vague) — while still keeping a recognisable hook.
- Keep a running word count in the draft header and re-check it after every edit.

## House rules from the Wang Fuk Court letter (October 2026)

Distilled from ~15 revision rounds on a 350–380 word letter. These are Simon's explicit
corrections, not inferred preferences.

### Sentence length is a hard floor, not a style preference
- **No sentence under ~15 words**, except the signature line. Average 25–40.
- Fragments and verbless openers are banned — but so are *short complete sentences*.
  A 6-word sentence like "Accountability has therefore arrived without examination." was
  rejected as choppy even though it has a subject and a verb.
- **Merge rather than trim.** When a draft runs long, cut *content*, never sentence
  length. Trimming a long draft to hit a word count is what produced fragments twice.

### State the argument; never announce it
- Wrong: `"our argument is that this evidence… leaves policy formulation unexamined"`
- Fix: `"yet this evidence… leaves policy formulation unexamined"`
- The rule generalises: no meta-discourse (`we argue`, `this letter argues`, `it is our
  view`). The claim should land as a claim, not as a description of a claim.

### Follow Simon's paragraph template literally
He will hand you a paragraph plan, sometimes with sentences already written. Use it as
given. Do not restructure it into your own architecture — and do not expand it into a
longer essay than the word budget allows. If the plan implies 840 words and the budget is
380, cut content, not the plan's shape.

### Quote the source's own words, and check its usage
- Never paraphrase a quotable phrase. The ToR's own words were
  `"whether regulation and penalties under relevant existing laws are adequate"` — quoting
  them beats any rendering of "whether the rules were sound".
- **Check collocation against the source.** Simon asked whether to write "wrote the rules";
  the report uses *set* / *established*, never *wrote*. Match the source's verb.
- Give a **page or section reference** for every quotation: `(Executive Summary, page xli)`.
  Spell out `page`, not `p.` — the abbreviation reads oddly and breaks sentence counts.

### One argument per paragraph
If Simon says *"I don't see a clear argument here"*, the paragraph is doing two things.
Split it, or find the single sentence the paragraph turns on and build around that.
A useful test: can you state the paragraph's turn in one clause? If not, it has two.

### Avoid em-dash bolt-ons
- Wrong: `…can only be answered by the offices that wrote them — so accountability has
  arrived without examination.` (Simon: "this is jumpy")
- Fix: merge the consequence into the sentence that produces it, or make it a full
  sentence with its own subject: `"Since no policy bureau secretary was consulted as a
  witness, accountability has arrived without examination."`

### Asks should be urgent, not merely polite
- `"We ask the Chief Executive…"` → `"We therefore urge the Chief Executive…"`
- Keep the ask to **one sentence with at most three demands**, and make the first one
  immediately actionable (release a document, publish a record).

### Closing on the victims — the pattern and its four traps

A letter that has spent its body on institutional critique often ends by pivoting to the
people harmed. **Keep the pivot** — it gives a reader who does not care about procedure a
reason to care. But the pivot sentence carries four recurring risks:

| Trap | Example | Why it fails | Fix |
|---|---|---|---|
| **"Closure"** | "bring comfort and closure to the victims" | Cliché in tragedy writing; the first word a sub-editor strikes. Reads as formula against real deaths. | Name what should happen instead of naming a mood. |
| **Unargued comparative** | "are **the best way** to…" | Best compared to what? The letter never argued that transparency *causes* comfort. | Drop the comparative, or earn it earlier in the letter. |
| **Two gerunds doing one job** | "upholding transparency **and** finding out the truth" | They overlap; one is padding. Also a register mismatch — officialese beside plain speech. | Keep the one that carries the claim. |
| **Wordy kinship** | "victims and their family members" | Same meaning as "victims and their families", longer and less idiomatic. | Shorten. |

**The test:** does the closing *name an action the letter demanded*, or does it only assert a
mood? A closing that restates the ask reinforces it; a closing that floats free of the ask
reads as decoration.

> **Weak:** "Upholding transparency and finding out the truth are the best way to bring comfort and closure to the victims and their family members."
> **Tied to the ask:** "Publishing those chapters and seeking those explanations is the least the victims' families are owed."

The second version names the two actions the previous paragraph demanded, so the close and
the ask say the same thing.

### Concede the other side's findings
When the subject has published findings that partly cut against your argument, state them
first. It costs words and buys credibility — and it forces the argument to be precise
rather than broad.

## Reducing AI smell

AI-generated prose has recurring patterns that editors and markers spot quickly.
Check every draft for these before submission:

**Fragment sentences**
- Wrong: `"A stranger's arms; the World Cup final."` — no verb, cinematic-AI affect.
- Fix: write a full sentence. *"The photograph that links them dates to 2007 — Messi cradling Yamal as a five-month-old at a charity shoot."* Every sentence needs a subject and a verb.

**Choppy two-beat openers**
- Wrong: `"X is the headline. Y is the story."` — sounds like an AI pulling a dramatic reveal.
- Fix: one flowing clause. *"While X earns the headline, Y is what endures."*

**Validation openers**
- Wrong: `"Coverage of X rightly celebrates…"` / `"It is worth noting that…"`
- Fix: start with the substance. Drop the preamble and open with the claim or fact.

**Universal quantifiers you cannot stand behind**
- Wrong: `"the unglamorous downstream half of every satellite mission"`
- Fix: qualify or drop: *"most satellite missions"* or *"long after launch day."*

**"Not just X, but Y" filler**
- Wrong: `"This is not just a sporting story, but a governance one."`
- Fix: say the real thing directly. *"China's football problem is governance, not talent."*

**Over-hedged closings**
- Wrong: `"This highlights the need for further discussion around…"`
- Fix: end with the specific action or insight. Name the reform, the ask, or the reframe — not the need for a conversation.

**Abrupt concept introduction**
- Wrong: raising a new idea (e.g. "hosting the World Cup") only in the final sentence when it never appeared earlier.
- Fix: either seed the concept in an earlier paragraph, or find a closing that follows naturally from what is already on the page.

**Blunt "problem" labeling**
- Wrong: `"The problem is access, not talent:"` — choppy; reads like an AI diagnostic label dropped into the paragraph.
- Fix: Use evidential framing that flows from the evidence you just cited. `"The barriers are structural:"` or `"Those numbers share a root cause:"` — let the data lead, not the diagnosis.

**Imperative endings (祈使句)**
- Wrong: `"Scrap pay-to-play fees, let school sport count toward university admission, and professionalise Football Association governance."` — a list of commands; sounds like AI policy bullets.
- Fix: Declarative conditional. `"Addressing those barriers — and cleaning up Football Association governance — would bring a World Cup bid within reach."` Reframes the call to action as an observation about what is possible.

**Unexplained domain jargon**
- Wrong: `"kept a World Cup clean sheet"` — general newspaper readers may not know the term.
- Fix: Gloss inline immediately after: `"kept a clean sheet — conceding nothing"`.

**Over-short paired transition sentences**
- Wrong: `"Both men found their door. China's talent just needs one."` — two staccato stabs; the second is too vague and offers nothing new.
- Fix: Merge and add substance. `"Both men found their door. China has the talent in abundance — what it has never built is the door itself."` — the elaboration earns the metaphor.

**Missing temporal anchor**
- Wrong: `"This tournament has delivered that story in miniature."` — which tournament?
- Fix: Anchor immediately. `"This year's tournament"` or `"The 2026 tournament"`.

**Absolute quantifiers without evidence**
- Wrong: `"what it has never built is the door itself"` — "never" is an absolute claim you cannot prove; also vague (what door?).
- Fix: Hedge + specify. `"Chinese players of comparable talent rarely find one — not for want of ability, but of infrastructure."` — "rarely" is defensible; naming the deficiency (infrastructure) gives the reader something concrete. As a rule, search every draft for *never / always / every / no one / nothing* and ask whether you can actually stand behind the absolute.

**The test:** read the letter aloud. If any sentence sounds like it is *explaining itself* rather than *saying something*, cut the explanation and keep only the claim.

## Revision workflow

1. Read the current `draft-vN.md` and the user's specific feedback.
2. Research/verify any new facts or links (web-search, academic-search, direct `curl` for 200 checks).
3. Write `draft-v{N+1}.md`: the new letter at top with an accurate word-count header, then `## What changed from vN` explaining each edit and why (tie each change to the user's request), then carry forward the "Still to verify" and "SCMP submission checklist" sections.
4. Summarise the changes for the user in their language (this user: Chinese chat, English deliverable).

## SCMP editorial correspondence (real feedback from Woei Wan, SCMP Letters, July 2026)

The SCMP editor will read every link and check whether it supports the specific claim in the anchor text. Lessons from the china-football letter:

| Editor flag | What went wrong | Fix |
|---|---|---|
| Source ≠ anchor claim | Xinhua Li Tie article (clubs paying for national team selection) was linked to "pay-to-play fees price out ordinary families" — the editor immediately caught the mismatch | Either find a source that says the specific thing, or remove the claim. The Li Tie article supports "money rather than merit decides who rises" — not grassroots fees |
| "Hosting bid" ≠ performance | "A World Cup hosting bid would stop being a fantasy" implies China must play better to *host*, which is wrong (Qatar hosted without being good) | Distinguish hosting from qualifying/playing. Editor suggested: "This way, China would play the World Cup again, for real." |
| Age inconsistency with exam name | "gaokao pressure pulls children from the pitch before they turn 16" — the gaokao is taken at 18, not 16 | If you name gaokao specifically, say 18. If you want 16, use broader "exam pressure" (covers zhongkao at 15-16). Editor preferred "when they turn 16" over "before they turn 16" for precision |
| "before" vs "when" | "before they turn 16" frames 16 as a deadline; "when they turn 16" frames it as the trigger | Use "when" for events that mark a transition (entering senior high) |

**Correspondence protocol:**
- SCMP editor corresponds by email to all named authors (cc'd together)
- Editor signs off as full name + "SCMP Letters" (e.g. "FOONG Woei Wan, SCMP Letters")
- Replies should be brief — one sentence per point, confirm or propose alternative
- If accepting a suggestion verbatim, say so explicitly: "We are happy to adopt it."
- Sign on behalf of all co-authors: "Simon (on behalf of Andy and Yichun)"

**Title conventions (from reviewing real SCMP letter titles):**
- Single sentence, never two sentences
- Declarative, "Why...", or statement–dash–pivot (like "It's OK to Open Up to an AI Bot — Just Don't Stop There")
- 7–12 words; foregrounds the argument, not just the news peg
- Strong verbs: *expose, demand, bridge, show* — not weak: *highlight, address, discuss*
- Examples from the china-football letter options: "The World Cup's Underdogs Expose What China's Football System Lacks" ✓

## SCMP submission checklist

- Email **`letters@scmp.com`**.
- Subject line = the letter's title.
- Body includes full names, affiliations, and the corresponding author's **phone + email** (SCMP verifies by phone).
- Send as **plain text in the email body**, not as an attachment.
- Courtesy step: email anyone named in the letter to let them know beforehand.
## Session lessons — TalkLivelihood letter, 25–26 Oct 2026 (drafts v1→v7, Simon's line-by-line feedback)

Evidence base: seven revisions of one ~300-word letter in a single Google Doc, with the
writer's feedback quoted verbatim. Add these to the AI-smell checklist above — each one
cost a revision round.

### New AI-smell patterns

1. **Meta-announcement instead of content.**
   - Wrong: *"The same survey, six months on, shows something new."* — a sentence that exists only to announce the sentence after it. Feedback: *"this sentence is confusing."*
   - Fix: delete the announcement. If continuity is needed, name the antecedent properly: *"In April, in a letter published in these pages, we reported our first survey: …"*
2. **Orphaned transition after an edit.**
   - Wrong: deleting the APEC sentence left *"Hong Kong's van and lorry drivers are ready to do their part"* pointing at nothing. Feedback: *"this is out of nowhere after taking away APEC … are you kidding me."*
   - Fix: after **any** deletion, re-read the surviving sentences. Every connective ("do their part", "as above", "that way", "ready to switch") must still have its antecedent *in the text*. Deleting a sentence can orphan the one before it *and* the one after it.
3. **Stacked attribution clauses.**
   - Wrong: *"In March we began surveying …, and in April, in a letter published in these pages, we reported what we found:"* — two time-place frames and a colon before the payload arrives. Feedback: *"too wordy."*
   - Fix: one frame per sentence, payload inside the first line: *"In April, in a letter published in these pages, we reported our first survey: …"* (fieldwork dates belong in the submission notes, not the hook.)
4. **Undigested topic switch.**
   - Wrong: dropping the EV block in after the fuel-burden block with only *"our second survey also asked"* — the new issue arrives without its logic. Feedback: *"the issue should be properly introduced."*
   - Fix: a bridge sentence that carries cause → question → numbers: *"With no relief in sight at the pump, our October survey also asked about the alternative: electric commercial vehicles, which cost far less to run."*
5. **Decorative triads.**
   - Wrong: *"charging access, financing, and plain information"* — three items chosen for rhythm; none carries new weight. (Recorded rule from the EV-battery letter v16: *"no triads"*.)
   - Fix: two concrete items, or tie every item to a number from the data.
6. **Aphorism / metaphor inside the ask.**
   - Wrong: *"not a headline but a monthly bill"*, *"a ready test of whether that talk reaches the street"*, *"convert the drivers who are waiting only for facts"* — crafted turns that read as AI performance. None survived revision.
   - Fix: plain declarative. In a data letter, the figures are the rhetoric.
7. **Choppy short sentence with no grammatical bridge.**
   - Wrong: *"Hong Kong's drivers say they are ready to switch."* standing alone after a news clause. Feedback: *"choppy sentence, lack of coherence with previous sentence."*
   - Fix: merge the two thoughts into one sentence with "and" or a colon — short is not the same as clean.

### Workflow additions

- **Step 0: read your own published letters before drafting.** House style lives in your own back catalogue — the EV-battery letter doc carried its own de-AI changelog (*"Zero em dashes; no triads / 'not X but Y' / 'rather than'"*), and the April correspondence thread carries the editor's fact-check lessons. Extract the rules first, then draft.
- **Treat the writer's inline parentheses as review comments.** Simon edits by writing questions inside the text (*"(what type of support?)"*, *"(attribute to the survey results)"*, *"(improve transition here)"*). Resolve every one in a table: comment → resolution → verified number. Never apply them silently; the table is how the writer sees what happened to each question.
- **De-AI passes must not touch figures.** Re-derive every number during the style pass: 46.7% → **46.3%** (the higher figure double-counted the 3 current EV owners), *"around 11 per cent"* → **11.9%**, and the 61% barrier claim needed its denominator stated (*252 of the 412 drivers with no present intention*). A percentage without its denominator is a fact-check flag.
- **A link is not a source unless the page shows the figure.** Before hyperlinking a claim, confirm the target page actually displays that number — in this session the public results page lacked the Q6 coping and Q9C barrier stats, so two sections were added to the page *before* the claims could be linked. Then verify with **status + content marker** (an HTTP 200 only proves *something* answered).
- **Word ceiling is a hard number.** Run `wc -w` after every edit. 379 words was *"a bit too long"* against a 400-word limit — hold data-heavy letters near **300** so edits never push you over.
- **End with the direct ask.** Feedback on a wind-down ending: *"Just a call for action would help."* Note the tension with the *imperative endings* rule above: one plain ask sentence is good; a staccato list of commands is not.## Editorial correspondence lessons — fuel-price letter, April 2026 (Charmaine, SCMP Letters)

From the full April thread (TalkLivelihood repo `docs/letters.md`, verified). The editor
fact-checks every figure against the data you hand over:

- **Accuracy-first: the editor counts rows.** *"Could you explain how you arrived at the 'three quarters'? We find 51 entries saying '30-50%' and 100 saying '50-80%'."* Every figure must be re-derivable from the source sheet, with the denominator stated.
- **Every price/oil figure needs a date AND a source** (Consumer Council tracker, GlobalPetrolPrices, Reuters). Prices move between submission and publication — expect a hard deadline to update them (*"please do so by 12 noon tomorrow"*).
- **State the fieldwork window and whether the survey is ongoing.** *"Please specify when the survey began and when it ends. If it's ongoing, we need to say that."*
- **Quote N at the actual cutoff** — "nearly 300" vs the later 604 caused confusion.
- **Do not attribute quotes to the wrong actor.** The "premature and unfair" claim was traced to the transport-sector lawmaker, not government officials, and rejected.
- **Pre-empt known rebuttals.** The Commission had met the oil companies in March; the editor required acknowledging it before we criticised their monitoring-only stance.
- **Unverifiable numbers get cut** ("50,000+ transport families" → "thousands"; two oil-price figures cut as unconfirmable).
- **The headline may change from what you submit** — our "…Competition Commission Must Act Now" became "Hong Kong's high fuel prices warrant scrutiny". Write the ask so it survives neutralising: a concrete, testable demand travels better than an accusatory frame.
- **Frequency:** Simon offered in April to be dropped as co-author if too frequent — decide authorship before submitting.
- **Editor-suggested strengthening cuts both ways:** SCMP proposed *adding* the strongest local detail (drivers crossing to the mainland to fill up; "from the van and lorry drivers' community"). Specific, local observations get rewarded.

## Session lessons — EV-charging subsidy letter, 3 Nov 2026 (drafts v1→v3, Simon's line edits)

Evidence: a ~200-word letter responding to an SCMP news report, revised across three drafts plus
Simon's own rewrite. His inline comments and final paste are quoted verbatim.

### Length and links (hard, from this session)

- **Target ~200 words, not 300.** Simon: *"we would like a letter around 200 words"*. The 200–400
  ceiling is the journal's; the working target is 200, and 300 only when the data genuinely needs it.
  Cut whole figures rather than compress prose — the 52.1% monthly share, the trial-fund sentence and
  the "low base" framing all went.
- **Links live inside the letter text only.** Simon: *"links to be added to texts in the letter not at
  the end"*. Never a source list under the letter; anchor the phrase that carries the claim.

### New AI-smell patterns

1. **Summary sentence after the data.** *"The interest is real, and the means to act on it are missing."*
   — cut in the final edit; the figures carry the point. Same for *"What stands between them and an
   electric van is the price, not the appetite."* (also a "not X" turn).
2. **Rhetorical reference to a prior letters piece.** Simon: *"we don't need to directly refer to letter
   just say according to the survey"*. Cite the survey directly (*"According to a survey of more than
   770 van and truck drivers…"*) and link it; do not narrate that an earlier letter said something.
3. **Authority-last sentences.** Simon: *"Just start with the source, According to …"*. Open with the
   source: *"According to the government (LCQ19), high upfront purchase cost is the leading reason…"*.
4. **Data before state.** Simon: *"describe the current state first then refer to the government's view"*.
   The paragraph's job is the state of play (trend positive, adoption low), then the authority's
   explanation for it.
5. **Numbers without a comment.** Simon: *"So what is the point here? We need some comment on the fact."*
   Attach the interpretation to the figure in the same sentence: *"…yet only 2.24 per cent of licensed
   stock by May 2026 (Transport Department data); the fleet turns over slowly."*
6. **Our comparison instead of the source's words.** *"three to four times higher than diesel"* had no
   source and was cut; the government's own *"significantly higher than diesel"* (LCQ19) is
   unimpeachable. Prefer the authority's wording when the multiplier is unverifiable.
7. **A figure that does not reproduce.** A co-author's *"37.78 per cent of newly registered vans in 2025"*
   could not be reproduced from the Transport Department data (523 of 1,710 = **30.6%**); the published
   letters page showed **46.4%** where an internal note said 46.3%. Re-derive every number from the
   linked page and cite what the page shows.
8. **Imprecise scheme description.** *"subsidise the installation of EV chargers"* → the scheme funds
   charging-enabling infrastructure (cables, trunking); owners buy the chargers. Editors fact-check the
   mechanism, not just the number.

### Google Docs formatting (the expensive lesson)

- **`UPDATE_DOCUMENT_SECTION_MARKDOWN` inserting at index 1 inherits the paragraph style of the
  paragraph below.** If that paragraph is Heading 1 (because an earlier markdown insert began with `#`),
  the whole new block lands as **Heading 1 with bullets**. Simon: *"the latest version is bold - this is
  not acceptable"* → *"you actually set the texts as heading 1 -- this is unacceptable"*.
- **Safe recipe for a plain-text block with links** (one `batchUpdate`): `deleteContentRange` (if
  replacing) → `insertText` (plain, no markdown) → `updateParagraphStyle`
  `{namedStyleType: NORMAL_TEXT}` → `deleteParagraphBullets` → one `updateTextStyle` per anchor with
  `fields: "link"`.
- **Verify structurally, not by eye.** Dump the document JSON to disk (`GET_DOCUMENT_BY_ID` with
  `includeTabsContent`) and check `paragraphStyle.namedStyleType`, `bullet` and `textStyle.link`
  locally — plaintext output cannot show bold, headings or links.
- **No bold anywhere in the letter block**; headings belong to the notes sections, never the letter.

### Workflow

- **Keep the comment→resolution table out of the document.** It belongs in the issue/PR comment so the
  doc stays clean for the writer; still resolve every inline comment in that table (comment →
  resolution → verified figure).
- **Check the scheme's own mechanics before quoting it** (what the money bought, when applications
  opened and closed) — the year and the object of the subsidy are both fact-check targets.

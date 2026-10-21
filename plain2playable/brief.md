# The brief — what was actually sent to the agent

This is the working specification for the listening demo (lightly edited for
clarity; the original was sent as plain sentences in chat).

---

## Source material (attached as links/files)

1. Leydens & Lucena, *Listening as Engineering Communication* — the article to
   re-present (permission secured).
2. Google, *Towards an AI-Augmented Textbook* (paper) — for the design ideas to
   borrow: progressive disclosure, one comprehension check per section,
   multiple representations.
3. Google's Learn Your Way public demo — for the feel of the finished thing.

## Specification (sent verbatim, in sentences)

Build a single-page interactive listening lesson:

- **Structure:** the article's key ideas become 4–5 short sections. Each section
  discloses only after the previous one is completed — behind a progress bar the
  learner controls.
- **Comprehension:** one question per section, multiple choice, placed after the
  section's audio. Wrong answers get a hint, not the answer.
- **Scenario framing:** open each section with a one-line scenario placing the
  learner in the situation ("you are an engineer meeting a community elder…").
- **Audio:** narrate each section's text with a text-to-speech service; a play
  button per section, not one long track.
- **Design commentary:** a toggleable margin panel explaining, for each screen,
  which design principle produced it and why — this artefact is also a teaching
  case for other teachers.
- **Constraints:** single HTML file plus assets; no frameworks; no external
  dependencies beyond the TTS service; must run offline except the audio.

## What was deliberately NOT specified

- Colours, fonts, exact layout — the agent's taste was trusted, then corrected
  by looking at results.
- The wording of comprehension questions — drafted by the agent from the
  article, then reviewed.

## Corrections sent during the build (the actual loop)

1. "The progress bar should control disclosure, not just display progress."
2. "Section 3's question can be answered without listening — make the hint
   require the audio."
3. "The margin commentary is repeating the content; make it explain the design
   choice instead."

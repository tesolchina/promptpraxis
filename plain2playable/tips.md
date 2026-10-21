# Tips — interacting with an agent to build a teaching artefact

Lessons from the *plain2playable* build (Entry 1 of Prompt & Praxis). They
generalise beyond this demo.

## 1. Match the kind of AI to the kind of work

- **Chatbot** for words: drafting, summarising, critiquing, translating. Fast,
  conversational, nothing to manage.
- **Agent** for artefacts: anything that must *run* — a page, a script, a
  dataset pipeline. Only an agent can write code, execute it, read the error,
  and fix itself.

Using an agent to draft prose is like hiring an engineer to write an email.

## 2. Treat AI as a reasoning engine, not an information engine

The agent processes what you give it; it does not know your field. Its output
quality is bounded by input quality — garbage in, garbage out, now automated.
Collect your best source material *before* opening the tool: the permissioned
article, the reference implementation, the specification. The single highest-
leverage hour of the build is assembling the inputs.

## 3. Sequence the brief — content, structure, surface

The agent builds in the order you specify. Asking for narration before
structure, or design polish before content, produces rework. The order that
kept this build short:

1. **Content** — what the sections say (source material + outline)
2. **Structure** — sections, questions, progress bar, disclosure logic
3. **Surface** — audio, visual design, commentary panel

## 4. Write the spec as testable sentences

"The progress bar should control disclosure, not just display progress" is a
testable sentence — you can see on screen whether it holds. "Make it nice" is
not. Every correction in this build was a sharper sentence, never a patch.

## 5. Expect the loop, budget for it

The agent ran its own code, hit errors, read them, and fixed itself — that
loop is the value. But each of your corrections costs one loop too. Three to
five rounds of correction is normal for an artefact of this size; if you're on
round ten, the specification is the problem, not the agent.

## 6. Keep the judgement

What was worth building, whether the output is any good, who answers for the
result — none of that transfers to the agent. The teacher stays the editor-in-
chief; the agent is the implementation.

## 7. Permissions first

This build ran entirely on material we had permission to re-present. Before
starting, settle what you may use — it shapes the whole brief.

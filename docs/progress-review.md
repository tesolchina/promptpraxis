# Entry 2 progress for review — 12 November 2026

This is a draft review snapshot, not a publication-ready entry.

## Implemented
- OpenAlex fetcher and CSV/BibTeX/RIS exports using the Python standard library.
- Explicit relevance sorting omits the API sort parameter; missing authors remain empty/omitted.
- Two-track acceptance instructions and a Zotero handoff package for Winnie.
- Experimental citation formatter, retained for review only; adoption and licence analysis remain undecided.

## Validation
- Codex independently ran all seven offline tests on 12 November: seven passed. The live API test was deliberately excluded, not counted as passed.
- WorkBuddy recorded two live runs on Windows Python through the WSL UNC path: independent Track A and existing-script Track B. Both returned HTTP 200 and five records for automated written corrective feedback, from 2024, default relevance sorting, with no mailto or credentials.
- Evidence is in ../workshop/evidence/two-track-20261112/: original response bodies, exported files, cross-checks and reduced request metadata. Volatile response headers and local execution wrappers are not published.
- Bibliographic fields match across tracks; timing/relevance-score response differences and BibTeX key/comment differences are expected and documented.
- The repository validator is a local syntax check, not a Zotero importer.

## Remaining before publication
- Align the article Part 4, public beginner prompts and sample data with the verified AWCF/relevance/five-result example. The draft still contains the earlier applied-linguistics/citation-sorted example and unverified wording.
- Trim the assembled article to the agreed word budget and coordinate Part 3 with Winnie.
- Winnie must perform actual Zotero imports and return feedback/screenshots. The delivery files are prepared, not yet validated in Zotero.
- Complete GUI screenshots and a fresh-user rehearsal of the final reader-facing instructions.
- Confirm whether workshop code should remain here or live in procomm-microlearning (access was unavailable).
- Review component-specific Zotero reuse/licensing recommendations; the heuristic formatter is not an accepted CSL replacement.
- Simon reviews, merges and publishes; this PR does not remove the password or deploy anything.

Related: promptpraxis issues #7, #8, #9, #10 and #11. No issue is considered complete by this snapshot.

# Track A Step A1 planning notes (three points)

1. What this does: issue ONE live GET to the OpenAlex Works API for
   "automated written corrective feedback" since 2024, take at most 5 records,
   and export a reading-list CSV plus BibTeX/RIS from that same response.
2. What is needed: topic, lower year bound, result count, output folder.
   No email, API key or credentials are required or sent.
3. What could go wrong: HTTP 403/429 or network failure, zero results,
   missing authors/DOIs/venues in the registry. Missing fields stay empty;
   nothing is invented or copied from sample-data / older responses.

Note: the user's unified instruction already authorized execution in this
turn, so the interactive "pause for confirmation" of Step A1 was not
simulated; no chat-only claim is made.

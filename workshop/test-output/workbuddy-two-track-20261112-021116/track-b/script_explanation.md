# Track B Step B1 — plain-language explanation of workshop/fetch_literature.py

Read ONLY after all Track A artifacts had been saved (02:14–02:15 +0800).
File read: `\\wsl.localhost\Ubuntu\home\andy\projects\promptpraxis\workshop\fetch_literature.py`
(mtime 2026-11-12 01:55:23, 12247 bytes; not modified in this run).

1. What it does (plain language): it asks the OpenAlex "Works" catalogue for
   papers matching a topic, keeps the ones published from a chosen year onward,
   and writes three files — a reading-list spreadsheet (CSV), a BibTeX file and
   an RIS file that reference managers can import. It can also read a saved
   offline JSON file instead of going online (`--fixture`). It uses only the
   Python standard library.

2. Parameters (from `main()` lines 251–266): `--topic` (search words), `--year`
   (earliest year, default 2024), `--sort` (default `cited_by_count:desc`),
   `--limit` (default 10, capped at 50 by `per-page`), `--email` (polite-pool
   address, default is a placeholder), `--output-csv`, `--output-bib`,
   `--output-ris` (default `found.*` in the current folder), and `--fixture`.

3. Missing metadata: the script keeps absent values empty rather than inventing
   them. In this version `write_csv()` writes `""` for an empty author list
   (line 185); `write_bibtex()` omits the `author = {...}` line entirely when
   there are no authors (lines 208–210); `write_ris()` emits no `AU` lines.
   Missing DOI/citation/year fields are likewise left out or written empty.
   Caveat observed in source: `generate_citekey()` still uses the literal
   "Unknown" as a citekey placeholder for authorless works (line 55), and the
   terminal sample summary prints `Authors: Unknown` (line 320). These are a
   technical identifier and a console string — not an author in the exported
   files. Both are recorded in the acceptance report.

4. `--sort relevance` implementation (lines 88–96, the reason Track B can match
   Track A): `params` starts as `search / filter / per-page`; the line
   `if sort and sort != "relevance": params["sort"] = sort` means passing
   `--sort relevance` leaves `sort` OUT of the URL entirely, so OpenAlex uses
   its default relevance ranking. `mailto` is added only when `--email` is
   non-empty, so `--email=` sends no address. With `--year 2024` and
   `--limit 5`, the resulting URL is the same shape as Track A's.

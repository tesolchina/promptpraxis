# Verified Sample Data Provenance

This directory contains verified sample outputs from OpenAlex Works API, captured on **12 November 2026** (UTC 2026-11-11T18:17:18Z) during the dual-track WorkBuddy acceptance run.

- **Source API:** OpenAlex Works API (`https://api.openalex.org/works`)
- **Query Parameters:**
  - Topic: `automated written corrective feedback`
  - Earliest publication date: `2024-01-01` (`filter=from_publication_date:2024-01-01`)
  - Sort order: Default relevance ranking (best matches first; no `sort` parameter sent to API)
  - Result limit: `5` (`per-page=5`)
  - Contact email: None (`email=""` / `--email=`, polite pool omitted without credential/fictitious requirement)
- **Captured Artifacts:**
  - `sample-found.csv`: Persistent reading list with `Reading_Status` set to "Unread" and blank `Notes`.
  - `sample-found.bib`: BibTeX bibliography file with verified citekeys and escaped special characters.
  - `sample-found.ris`: RIS reference file compliant with standard reference managers.
- **Offline Integrity:** Preserved directly from `workshop/evidence/two-track-20261112/track-b/` without re-querying the live network.

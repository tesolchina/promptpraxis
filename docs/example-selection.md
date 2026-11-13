# Workshop Teaching Example Selection & Evaluation (docs/example-selection.md)

**Worker:** AndyZHENG0715 (安 / Andy)  
**Date & Time:** 12 November 2026, 00:45 HKT (UTC+8)  
**Task:** Evaluate OpenAlex query candidates for Prompt & Praxis Entry 2 / Friday Workshop to replace the overly generic `applied linguistics AI` query.  
**Boundaries:** No remote push, no external messaging, no feature additions.

---

## 1. Problem Statement: Why the Baseline Query Failed Pedagogically

The baseline query featured in early drafts was:
- **Search phrase:** `applied linguistics AI`
- **Filter:** `from_publication_date:2024-01-01`
- **Sort:** `cited_by_count:desc`

While technically functional (returning HTTP 200 and valid JSON), sorting by citation count across a broad keyword search returned:
1. *Qwen3 Technical Report* (17,500+ citations)
2. *DeepSeek-R1 incentivizes reasoning...* (16,700+ citations)
3. *GPT-4o System Card* (8,800+ citations)

These are massive-scale foundational computer science preprints. For teachers, applied linguists, and students attending the Friday literature workshop, this outcome is confusing and unhelpful. To demonstrate academic literature management effectively, the query must retrieve literature situated in **applied linguistics, second-language (L2) writing, and language education**.

---

## 2. API Syntax & Candidate Query Methodology

OpenAlex API syntax rules:
- `search=<phrase>`: Performs full-text search across title, abstract, and indexed text.
- **Sorting rule:** When `sort` is omitted or set to default, OpenAlex scores results by **relevance** (`relevance_score:desc`), prioritizing exact lexical matches in titles and abstracts over raw global citation count.
- `filter=from_publication_date:2024-01-01`: Limits results to publications from 2024 to present.
- `per-page=5`: Limits sample size to 5 records for inspection.

### Network & Verification Record
- **Verification Evidence:**
  - Candidate 1 was independently queried and verified by WorkBuddy on Windows Python (see report: [`workshop/test-output/workbuddy-example-20261112-005622/acceptance.md`](../workshop/test-output/workbuddy-example-20261112-005622/acceptance.md)). Single GET request, HTTP 200 (83,957 bytes), without API key or credentials, confirming `meta.x_query.order = "best matches first"`.
  - In WSL/Linux sandbox testing, live API calls remain intercepted by local proxy policy (`HTTP 403`), with offline unit tests passing via mock and fixtures.
- **Stored Response Files:**
  - Candidate 1: [`docs/candidate-queries/candidate1_awcf.json`](candidate-queries/candidate1_awcf.json)
  - Candidate 2: [`docs/candidate-queries/candidate2_genai_l2_writing.json`](candidate-queries/candidate2_genai_l2_writing.json)
  - Candidate 3: [`docs/candidate-queries/candidate3_chatbots_lang_learning.json`](candidate-queries/candidate3_chatbots_lang_learning.json)
  - Unified Summary: [`docs/candidate-queries/summary.json`](candidate-queries/summary.json)
  - *Note on data structure:* Stored candidate files are structured JSON wrappers preserving the OpenAlex response body (`meta` and `results`), rather than raw HTTP wire transcripts.

---

## 3. Candidate 1: Automated Written Corrective Feedback

- **Exact Query URL:** `https://api.openalex.org/works?search=automated+written+corrective+feedback&filter=from_publication_date%3A2024-01-01&per-page=5`
- **Total OpenAlex Database Count:** 11,915 records
- **Timestamp:** 2026-11-11T16:44:05Z (WorkBuddy verification: 2026-11-11T17:00:32Z)

### Item-by-Item Relevance & Access Inspection

1. **Title:** *Automated Written Corrective Feedback in EFL context* (2026)
   - **Authors:** Anano Chang
   - **Venue:** California Digital Library | **Citations:** 0
   - **DOI:** [`https://doi.org/10.48321/d13320141e`](https://doi.org/10.48321/d13320141e)
   - **Access Metadata:** API reports `is_oa: true`, `oa_status: green`, `oa_url: https://doi.org/10.48321/d13320141e`. (Actual full-text download unverified).
   - **Relevance:** **High.** Abstract investigates Chinese EFL university students engaging with automated written corrective feedback (AWCF) in revision.
2. **Title:** *Automated Written Corrective Feedback (AWCF)* (2024)
   - **Authors:** None listed in OpenAlex record (`authorships: []`)
   - **Venue:** BRILL eBooks | **Citations:** 1
   - **DOI:** [`https://doi.org/10.1163/9789004719118_009`](https://doi.org/10.1163/9789004719118_009)
   - **Access Metadata:** API reports `is_oa: false`, `oa_status: closed`. (Paywall unverified; represents metadata status only).
   - **Relevance:** **Information limited (Title match only).** *Note:* No abstract in OpenAlex record; relevance judgment is strictly bounded to title. Serves as a realistic teaching example for missing author and abstract in academic registries.
3. **Title:** *Effectiveness of Generative AI in Automated Written Corrective Feedback With Prompting* (2025)
   - **Authors:** Jiahui Wu, Jianwei Li, Zi-Gang Ge
   - **Venue:** *Journal of Educational Computing Research* (Sage) | **Citations:** 19
   - **DOI:** [`https://doi.org/10.1177/07356331251359430`](https://doi.org/10.1177/07356331251359430)
   - **Access Metadata:** API reports `is_oa: false`, `oa_status: closed`. (Subscription paywall unverified).
   - **Relevance:** **High.** Directly evaluates prompt-based generative AI for L2 English writing correction.
4. **Title:** *L2 writer engagement with automated written corrective feedback provided by ChatGPT: A mixed-method multiple case study* (2024)
   - **Authors:** Da “Alex” Yan, Shuxian Zhang
   - **Venue:** *Humanities and Social Sciences Communications* (Springer Nature) | **Citations:** 167
   - **DOI:** [`https://doi.org/10.1057/s41599-024-03543-y`](https://doi.org/10.1057/s41599-024-03543-y)
   - **Access Metadata:** API reports `is_oa: true`, `oa_status: gold`, `oa_url: https://doi.org/10.1057/s41599-024-03543-y`. (Actual PDF accessibility unverified).
   - **Relevance:** **High.** Case study of L2 students interacting with ChatGPT feedback; peer-reviewed journal.
5. **Title:** *Impact of prompt sophistication on ChatGPT’s output for automated written corrective feedback* (2025)
   - **Authors:** Na Luo, Yifan Wang, Zhe (Victor) Zhang
   - **Venue:** *ReCALL* (Cambridge University Press) | **Citations:** 10
   - **DOI:** [`https://doi.org/10.1017/s095834402510044x`](https://doi.org/10.1017/s095834402510044x)
   - **Access Metadata:** API reports `is_oa: true`, `oa_status: hybrid`, with a Cambridge Core PDF URL in `pdf_url`. (Direct download unverified).
   - **Relevance:** **High.** Examines how prompt design alters feedback quality in CALL/second-language acquisition.

---

## 4. Candidate 2: Generative AI in Second Language Writing

- **Exact Query URL:** `https://api.openalex.org/works?search=generative+AI+second+language+writing&filter=from_publication_date%3A2024-01-01&per-page=5`
- **Total OpenAlex Database Count:** 141,849 records
- **Timestamp:** 2026-11-11T16:44:08Z

### Item-by-Item Relevance & Access Inspection

1. *Generative AI and Second Language Writing* (2025), Shaofeng Li, *Digital studies in language and literature*. Citations: 86. OA: True. **High relevance** (critical synthesis of GenAI in L2 writing).
2. *Generative AI and Second Language Writing* (2025), Robert Godwin-Jones, No venue listed in primary location. Citations: 2. OA: False. **High relevance**, but metadata missing venue name.
3. *The Application of Generative AI in Chinese as a Second Language Writing* (2026), Fanqi Cheng, *SHS Web of Conferences*. Citations: 1. OA: True. **Moderate relevance** (conference paper).
4. *The Application of Generative AI in Chinese as a Second Language Writing* (2026), Fanqi Cheng. Citations: 0. OA: True. **Duplicate record** of Item 3 deposited under an institutional repository.
5. *Generative AI is useful for second language writing, but when, why, and for how long do learners use it?* (2025), Haerim Hwang et al., *Journal of Second Language Writing* (Elsevier). Citations: 73. OA: True. **Extremely High relevance** (top journal in field).

*Critique:* Contains duplicate conference entries (Items 3 & 4) in the top 5, slightly degrading the demonstration diversity.

---

## 5. Candidate 3: Chatbots in Language Learning

- **Exact Query URL:** `https://api.openalex.org/works?search=chatbots+language+learning&filter=from_publication_date%3A2024-01-01&per-page=5`
- **Total OpenAlex Database Count:** 137,372 records
- **Timestamp:** 2026-11-11T16:44:11Z

### Item-by-Item Relevance & Access Inspection

1. *Does Chatting with Chatbots Improve Language Learning Performance? A Meta-Analysis...* (2024), Feifei Wang et al., *Review of Educational Research*. Citations: 98. OA: False. **Extremely High relevance** (rigorous meta-analysis).
2. *Effectiveness of Chatbots in Improving Language Learning: A Meta-Analysis...* (2024), Boning Lyu et al., *International Journal of Applied Linguistics*. Citations: 75. OA: True. **Extremely High relevance**.
3. *THE USE OF CHATBOTS IN THE ENGLISH LANGUAGE TEACHING...* (2024), *IJIET*. Citations: 22. OA: True. **Moderate relevance** (regional journal review).
4. *Intelligent Modelling For Multilingual Language Learning Chatbot* (2025), Zenodo preprint. Citations: 0. OA: True. **Low/Moderate relevance** (technical repository preprint).
5. *Elevating Language Learning with Chatbot Technology* (2026), *ELTALL*. Citations: 1. OA: True. **Moderate relevance**.

---

## 6. Comparison & Final Recommendation

| Dimension | Candidate 1: Automated Written Corrective Feedback | Candidate 2: Generative AI Second Language Writing | Candidate 3: Chatbots Language Learning |
|---|---|---|---|
| **Disciplinary Focus** | Applied Linguistics / L2 Writing Feedback | L2 Writing & Generative AI | General Language Learning / Chatbots |
| **Top Journals Represented** | *ReCALL*, *Hum. & Soc. Sci. Comm.*, *J. Educ. Computing Res.* | *J. Second Language Writing*, *Digital Studies* | *Review of Educational Research*, *Int. J. Applied Linguistics* |
| **Metadata Cleanliness** | Diverse venues, 0 duplicates | Contains duplicate conference deposit | Contains regional preprint deposits |
| **Pedagogical Contrast** | Clear contrast between OA metadata, closed metadata, and missing authors/abstracts | Good, but cluttered by duplicate title | Good meta-analyses, but wider scope |

### Selected Recommendation: Candidate 1 (`automated written corrective feedback`)

**Exact Recommended Query Parameters:**
```text
Endpoint: https://api.openalex.org/works
search: automated written corrective feedback
filter: from_publication_date:2024-01-01
sort: (omitted / default relevance ranking)
per-page: 5 (or 10 for full workshop)
```

### Why this topic is optimal for beginner teaching:
1. **Direct Domain Resonance:** Language teachers immediately understand "written corrective feedback." Combining it with ChatGPT and prompt engineering illustrates the core thesis of *Prompt & Praxis*: using AI thoughtfully as an instrument.
2. **Distinction Between Metadata Provenance and Verified Full-Text Access:**
   - Items 1, 4, 5 report open access in metadata (`is_oa: true`), while Items 2 and 3 report closed metadata (`is_oa: false`).
   - *Crucial teaching point:* API metadata fields (`is_oa`, `pdf_url`) reflect registry indexing, NOT verified full-text availability. Having a valid DOI does NOT mean an agent can automatically download the article. Students learn that reference managers capture citation metadata first, while full-text retrieval requires separate verification.
3. **Natural Registry Imperfections:** Item 2 (Brill book chapter) lacks author and abstract fields in OpenAlex (`authorships: []`). Our pipeline gracefully handles this by leaving CSV author blank and omitting the BibTeX `author` line, teaching students that bibliographic pipelines must preserve missing data truthfully without inventing placeholders like 'Unknown'.

### Explicit Limitations & Teaching Caveats
- **Not a Systematic Review:** An OpenAlex keyword search is an exploratory retrieval query, NOT an exhaustive or systematic literature review (SLR).
- **Lexical Bias:** Results reflect keyword matches in titles and abstracts; relevant papers using alternative terminology (e.g., "automated writing evaluation" or "grammar error correction") may be omitted without query expansion.
- **Unverified Full-Text Downloads:** No PDF files were downloaded, and no paywalls were checked. All OA/PDF statuses cited are OpenAlex API metadata fields, not empirical download confirmations.
- **Independent WorkBuddy Verification:** Confirmed by WorkBuddy in [`workshop/test-output/workbuddy-example-20261112-005622/acceptance.md`](../workshop/test-output/workbuddy-example-20261112-005622/acceptance.md).

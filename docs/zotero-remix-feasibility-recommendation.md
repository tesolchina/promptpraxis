# Recommendation: Zotero Module Remix Feasibility for Tencent WorkBuddy

**To:** Simon Wang (Author / Series Lead)  
**From:** Andy Zheng (Implementation Worker / Co-author)  
**Date:** 11 November 2026  
**Context:** Prompt & Praxis Entry 2 (Issue #8) / Friday 13 Nov Workshop

---

## 1. Executive Summary & Context for Decision

Simon asked: *"能不能够直接从 zotero 里面借一些代码出来，然后在 WorkBuddy 里面去跑"* (Can we borrow code modules directly from Zotero and run them inside WorkBuddy?).

**Summary for Decision:**
- Direct module reuse from upstream Zotero desktop (`zotero/zotero`) is unviable due to Mozilla Gecko platform coupling.
- Web translators (`zotero/translators`) require a background Node HTTP daemon (`translation-server`), which introduces classroom firewall/port friction and AGPLv3 copyleft licensing risks (pending formal legal verification).
- `citeproc-js` runs in Node.js under CPAL/AGPL, but requires managing CSL style XML and locale assets.
- A lightweight heuristic formatter spike has been prepared in `workshop/zotero-spike/` as an exploratory candidate, but is strictly heuristic and unverified against CSL test suites.
- Whether to adopt an inline formatting spike or rely strictly on standard external BibTeX/RIS file import into Zotero remains an open design choice for Andy, Codex, and Simon.

---

## 2. Upstream Architecture & Component-by-Component Evaluation

We evaluated each candidate component individually across source files, licensing, runtime dependencies, and execution under WorkBuddy:

| Candidate Component | Upstream Source & Version | Upstream Licence | Standalone Runtime Dependencies | WorkBuddy Viability & Constraints |
|---|---|---|---|---|
| **A. Desktop Core & Client** | `github.com/zotero/zotero` (v7.0+) | **AGPLv3** | Requires Mozilla Gecko platform (XPCOM, XUL, SpiderMonkey, C++ bindings, SQLite). >300 MB footprint. | **UNVIABLE.** Cannot run in WorkBuddy or standalone Node; requires full desktop application windowing. |
| **B. Web Translators** | `github.com/zotero/translators` | **AGPLv3** (per-translator headers) | Individual JS scripts written against Zotero internal API (`Zotero.Item`, `Zotero.Utilities`). | **UNVIABLE STANDALONE.** Cannot run directly in Node without an execution harness. |
| **C. Translation Daemon** | `github.com/zotero/translation-server` | **AGPLv3** | Node.js HTTP server + `jsdom` + bundled translators. Binds to port 1969. | **HIGH FRICTION & AGPL CONTAMINATION.** Technically runnable in Node, but requires student machines to run a background daemon; prone to local firewall and port blocks. Distributing or embedding forces AGPL copyleft on the repository. |
| **D. CSL Citation Processor** | `github.com/Juris-M/citeproc-js` (v1.2+) | **CPAL 1.0 / AGPLv3** | Pure JavaScript. Runs natively in Node.js without browser or daemon. Requires CSL style XML (`apa.csl`) & locale XML (`locales-en-US.xml`). | **VIABLE IN NODE.** Does not depend on Gecko. Requires managing XML assets and adhering to CPAL attribution requirements. |
| **E. Simon's Fallback (Heuristic Formatter)** | Built in `workshop/zotero-spike/` | **MIT** (Permissive) | Zero external dependencies. Pure standard library (Python or Node). <200 lines. | **CANDIDATE HEURISTIC SPIKE.** Uses Python standard library; execution in Windows WorkBuddy and UNC access pending live verification. (Heuristic approximation; not full CSL compliant). |

---

## 3. Specific Component Blockers & Trade-offs

### 1. The Translators and Translation Server (`zotero/translators`, `zotero/translation-server`)
- **Licence:** GNU AGPLv3. Any derivative work or networked distribution inherits AGPLv3 copyleft, which directly conflicts with the MIT licence of *Prompt & Praxis* (formal legal impact on pure consumption pending verification).
- **Runtime:** While translators are JS, they cannot be run by `node translator.js`. They require `translation-server`, an HTTP microservice. In a classroom of 30+ students, configuring and running local HTTP daemons creates a severe operational failure rate (firewall permissions, port collisions, process termination).

### 2. The Citation Processor (`citeproc-js`)
- **Licence:** Dual CPAL 1.0 / AGPLv3. Under CPAL, code can be reused if attribution notices are preserved.
- **Runtime:** Fully decoupled from Gecko. It takes CSL-JSON and CSL XML and formats citations in Node.js.
- **Trade-off:** High fidelity (full CSL standard compliance), but requires bundling and parsing complex XML style sheets (`apa.csl`) and locale files.

### 3. Simon's Fallback: Standalone Heuristic Formatter
- **Licence:** MIT (clean-room).
- **Runtime:** Zero dependencies; runs in standard Python. Windows WorkBuddy UNC execution pending testing.
- **Trade-off:** Fast and friction-free for workshop learning, but must be treated as **experimental/heuristic** (not a formal replacement for an accredited CSL engine).

---

## 4. The Minimal Spike (`workshop/zotero-spike/zotero_formatter.py`)

In the 11 Nov meeting, Simon proposed: *"实在不行我们就搞个 citation engine"*. 
We delivered and verified this experimental spike:
- **Capabilities demonstrated:** Formats OpenAlex records into APA 7th, IEEE, and Nature text citations and generates valid CSL-JSON item records.
- **Status:** **Experimental Proof-of-Concept**. It uses regex-based author and field parsing for workshop demonstration and is not validated against the formal CSL test suite.
- **Setup footprint:** Standard library only on Linux/WSL; Windows WorkBuddy execution and UNC path compatibility remain to be verified live on desktop.

---

## 5. Effort Estimate Comparison (Pending Verification / 待核实)

| Path | Implementation Effort (Rough Estimate / 待核实) | Student Setup Friction | Maintenance & Fragility |
|---|---|---|---|
| **Upstream Zotero Translators (`translation-server`)** | ~2–3 weeks (packaging daemon, IPC bridge) | **Extreme** (student daemon, ports, node build) | High (breaks on OS/port conflicts) |
| **CSL Engine (`citeproc-js` in Node)** | ~3–4 days (JS runner, CSL style XML parsing) | **Medium** (requires Node.js script invocation) | Medium (CSL XML schema updates) |
| **Simon's Fallback Engine (`zotero_formatter.py`)** | Experimental spike staged in `workshop/zotero-spike/` | **Pending live WorkBuddy testing** | Minimal (pure Python / MIT) |

---

## 6. Action for Andy / Codex / Simon

Review the candidate options:
- **Option 1 (Proven boundary):** Rely strictly on standard **BibTeX/RIS file export** (`found.bib` / `found.ris`) into Zotero Desktop, which avoids in-agent formatting entirely.
- **Option 2 (Inline heuristic formatting):** Adopt the candidate experimental spike in `workshop/zotero-spike/` for quick in-chat citations, explicitly noting its heuristic nature.

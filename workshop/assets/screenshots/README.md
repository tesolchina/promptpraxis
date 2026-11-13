# Screenshot Asset Provenance & Missing Capture Specification

**Scope:** Prompt & Praxis Entry 2 (Issues #3, #7, #11)

---

## 1. Verified Real Captured Assets (In Repository)

The following real captures were generated directly using headless Chrome (Linux/WSL) against live endpoints:

| Filename | Source Endpoint / URL | Captured Timestamp | File Size | Description |
|---|---|---|---|---|
| `arxiv-rss-feed.png` | `https://rss.arxiv.org/rss/cs.AI` | 2026-11-11 20:34 HKT | 45.4 KB | Real XML RSS feed view showing items, titles, and publication dates |
| `openalex-api-call.png` | `https://api.openalex.org/works?search=applied+linguistics+AI&per-page=3` | 2026-11-11 20:34 HKT | 46.8 KB | Real browser JSON view of OpenAlex works query |
| `zotero-homepage.png` | `https://www.zotero.org` | 2026-11-11 20:34 HKT | 44.8 KB | Official Zotero platform landing and download view |

---

## 2. Missing Desktop Captures (Human-in-the-Loop Required)

The following captures require an active graphical desktop display and human authentication (WeChat QR login for WorkBuddy; desktop windowing for Zotero Standalone and Word). In accordance with instructions (*"Do not fabricate UI captures; redact private data and list missing captures"*), these must be taken on a live desktop workstation:

| ID | Application | View / Action Required | Allocated Owner | Redaction Requirements |
|---|---|---|---|---|
| **CAP-01** | **Feedly Web** | Feed subscription: `feedly.com` showing *Nature* (`nature.rss`) added to sidebar | Winnie | Crop or blur personal profile icon and unrelated subscription feeds |
| **CAP-02** | **Zotero Desktop** | `File` → `Import...` dialog selecting `found.bib` into new collection | Winnie / Andy | Redact user's home folder path (`C:\Users\...` or `/Users/...`) |
| **CAP-03** | **Zotero Desktop** | Library table view showing imported records: Title, Creator, Year, DOI | Winnie / Andy | Ensure only demo items appear; hide unrelated private research collections |
| **CAP-04** | **Zotero Desktop** | Built-in PDF reader displaying an article page with highlighted sentence & note | Winnie | Use an open-access paper (e.g. Compagnoni 2024); no copyrighted paywall text |
| **CAP-05** | **Word / LibreOffice** | Document showing in-text citation `(Gosztyla, 2022)` and bibliography entry | Winnie | Use dummy text ("Lorem ipsum" or sample thesis paragraph) |
| **CAP-06** | **Tencent WorkBuddy** | Chat interface: Level 1 prompt executed, displaying the formatted Markdown table | Andy | Redact personal avatar/phone number from WorkBuddy top navigation bar |
| **CAP-07** | **Tencent WorkBuddy** | Settings view: `Expert skills` → `Connectors` → `GitHub` configuration pane | Andy | Blur GitHub personal access token (PAT) and user account name |

---

## 3. Image Sizing & Formatting Standards for Entry 2

- **Format:** PNG or WebP, 2x Retina resolution where possible.
- **Aspect Ratio / Max Width:** 1280px wide maximum.
- **Theme:** Clean default light mode for consistency with Entry 1 layout.
- **Destination:** Once captured, place in `workshop/assets/screenshots/` and link in `entries/entry-02/draft.md`.

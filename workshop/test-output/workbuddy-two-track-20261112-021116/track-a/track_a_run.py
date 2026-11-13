#!/usr/bin/env python3
"""Track A: independent standard-library implementation (written from scratch).

Does NOT read, import, run or copy workshop/fetch_literature.py; does NOT use
any earlier response or workshop/sample-data. Every exported row is derived
only from THIS run's saved raw_response.json.
"""
import csv
import datetime
import json
import os
import re
import sys
import urllib.parse
import urllib.request

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

OUT = r"\\wsl.localhost\Ubuntu\home\andy\projects\promptpraxis\workshop\test-output\workbuddy-two-track-20261112-021116\track-a"
META = os.path.join(OUT, "request_meta.json")
BODY = os.path.join(OUT, "raw_response.json")


def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def local():
    return datetime.datetime.now().astimezone().isoformat()


# Step A1 contract prompt: recorded as planning notes. The user's unified
# instruction already authorized execution, so no interactive pause was faked.
planning = """# Track A Step A1 planning notes (three points)

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
"""
with open(os.path.join(OUT, "planning_notes.md"), "w", encoding="utf-8") as fh:
    fh.write(planning)

# Deliberately no "sort" parameter -> OpenAlex default relevance ordering.
params = [
    ("search", "automated written corrective feedback"),
    ("filter", "from_publication_date:2024-01-01"),
    ("per-page", "5"),
]
url = "https://api.openalex.org/works?" + urllib.parse.urlencode(params)
headers = {"User-Agent": "PromptPraxisWorkshop/1.0"}
req = urllib.request.Request(url, headers=headers)
qp = urllib.parse.parse_qs(urllib.parse.urlparse(url).query)
entry = {
    "track": "A",
    "requested_at_utc": utc(),
    "local_time": local(),
    "url": url,
    "query_params": qp,
    "method": req.get_method(),
    "request_headers": dict(req.headers),
    "timeout_seconds": 30,
    "query_contains_sort": "sort" in qp,
    "query_contains_mailto": "mailto" in qp,
    "query_contains_api_key": "api_key" in qp,
    "raw_body_file": BODY,
}
calls = [entry]


def save_meta():
    with open(META, "w", encoding="utf-8") as fh:
        json.dump({"captured_at_utc": utc(), "calls": calls},
                  fh, ensure_ascii=False, indent=2)


try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        entry["http_status"] = resp.status
        entry["response_headers"] = {k: v for k, v in resp.headers.items()}
        body = resp.read()
except Exception as exc:
    entry["error_type"] = type(exc).__name__
    entry["error_repr"] = repr(exc)
    entry["error_str"] = str(exc)
    if hasattr(exc, "code"):
        entry["http_code"] = exc.code
    if hasattr(exc, "read"):
        try:
            entry["error_body"] = exc.read().decode("utf-8", "replace")
        except Exception as read_exc:
            entry["error_body_read_error"] = repr(read_exc)
    save_meta()
    raise

with open(BODY, "wb") as fh:
    fh.write(body)
entry["response_body_bytes"] = len(body)
save_meta()

with open(os.path.join(OUT, "run_log.txt"), "w", encoding="utf-8") as fh:
    fh.write("Track A run log\n")
    fh.write("Exact API URL: " + url + "\n")
    fh.write("Timestamp (local): " + local() + "\n")
    fh.write("Timestamp (UTC): " + utc() + "\n")
    fh.write("HTTP status: %s\n" % entry["http_status"])
    fh.write("Raw response saved to: " + BODY + "\n")

# ---- everything below is derived ONLY from the saved raw response ----
data = json.loads(open(BODY, "r", encoding="utf-8").read())
meta = data.get("meta", {})
results = data.get("results", [])
print("HTTP status:", entry["http_status"], "| body bytes:", len(body))
print("meta.count:", meta.get("count"))
xq = meta.get("x_query", {})
print("x_query.order:", xq.get("order"), "| order_default:", xq.get("order_default"))
print("results:", len(results))


def clean(s):
    return re.sub(r"\s+", " ", s or "").strip()


def authors_of(item):
    out = []
    for a in (item.get("authorships") or []):
        name = clean((a.get("author") or {}).get("display_name"))
        if name:
            out.append(name)
    return out


def journal_of(item):
    return clean(((item.get("primary_location") or {}).get("source") or {}).get("display_name"))


def esc(t):
    return (t.replace("\\", "\\\\").replace("{", "\\{").replace("}", "\\}")
            .replace("%", "\\%").replace("&", "\\&"))


records = []
for item in results:
    records.append({
        "id": item.get("id", ""),
        "title": clean(item.get("title")),
        "authors": authors_of(item),
        "year": item.get("publication_year"),
        "cited": item.get("cited_by_count"),
        "doi": item.get("doi") or "",
        "journal": journal_of(item),
    })

# Step A2: markdown table
tbl = ["| Title | Year | Citations | Venue | DOI |", "|---|---|---|---|---|"]
for r in records:
    tbl.append("| %s | %s | %s | %s | %s |" % (
        r["title"] or "", r["year"] if r["year"] is not None else "",
        r["cited"] if r["cited"] is not None else "", r["journal"] or "", r["doi"] or ""))
table_md = "\n".join(tbl) + "\n"
with open(os.path.join(OUT, "results_table.md"), "w", encoding="utf-8") as fh:
    fh.write("# Track A Step A2 results table\n\n" + table_md)
print(table_md, end="")

# Step A3: CSV (missing authors -> empty string, never "Unknown")
csv_path = os.path.join(OUT, "found.csv")
fields = ["OpenAlex_ID", "Title", "Authors", "Year", "Citations", "DOI",
          "Journal", "Reading_Status", "Notes"]
with open(csv_path, "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=fields)
    w.writeheader()
    for r in records:
        w.writerow({
            "OpenAlex_ID": r["id"],
            "Title": r["title"],
            "Authors": "; ".join(r["authors"]) if r["authors"] else "",
            "Year": r["year"] if r["year"] is not None else "",
            "Citations": r["cited"] if r["cited"] is not None else "",
            "DOI": r["doi"],
            "Journal": r["journal"],
            "Reading_Status": "Unread",
            "Notes": "",
        })

# Step A3: BibTeX (author line omitted entirely when authors missing)
used = set()


def citekey(r):
    if r["authors"]:
        first = r["authors"][0]
        last = first.split(",")[0].strip().split()[-1] if "," in first else first.split()[-1]
        base = re.sub(r"[^A-Za-z]", "", last) or "Ref"
    else:
        base = "Ref"
    y = str(r["year"]) if r["year"] is not None else "nd"
    words = re.sub(r"[^A-Za-z0-9 ]", "", r["title"]).split()
    key = base + y + (words[0].capitalize() if words else "")
    k, n = key, 1
    while k in used:
        n += 1
        k = key + str(n)
    used.add(k)
    return k


bib_path = os.path.join(OUT, "found.bib")
with open(bib_path, "w", encoding="utf-8") as fh:
    fh.write("% Track A generated from this run's OpenAlex response\n\n")
    for r in records:
        fh.write("@article{%s,\n" % citekey(r))
        fh.write("  title = {{%s}},\n" % esc(r["title"]))
        if r["authors"]:
            fh.write("  author = {%s},\n" % " and ".join(r["authors"]))
        if r["year"] is not None:
            fh.write("  year = {%s},\n" % r["year"])
        if r["journal"]:
            fh.write("  journal = {{%s}},\n" % esc(r["journal"]))
        if r["doi"]:
            d = r["doi"].replace("https://doi.org/", "").replace("http://doi.org/", "")
            fh.write("  doi = {%s},\n" % d)
            fh.write("  url = {%s},\n" % r["doi"])
        if r["id"]:
            fh.write("  note = {OpenAlex: %s},\n" % r["id"])
        fh.write("}\n\n")

# Step A3: RIS (AU lines omitted entirely when authors missing)
ris_path = os.path.join(OUT, "found.ris")
with open(ris_path, "w", encoding="utf-8") as fh:
    for r in records:
        fh.write("TY  - JOUR\n")
        if r["title"]:
            fh.write("TI  - %s\n" % r["title"])
        for a in r["authors"]:
            fh.write("AU  - %s\n" % a)
        if r["year"] is not None:
            fh.write("PY  - %s\n" % r["year"])
        if r["journal"]:
            fh.write("JO  - %s\n" % r["journal"])
        if r["doi"]:
            d = r["doi"].replace("https://doi.org/", "").replace("http://doi.org/", "")
            fh.write("DO  - %s\n" % d)
            fh.write("UR  - %s\n" % r["doi"])
        if r["id"]:
            fh.write("N1  - OpenAlex: %s\n" % r["id"])
        fh.write("ER  - \n\n")

print("Exports written:", csv_path, bib_path, ris_path, sep="\n  ")
for i, r in enumerate(records, 1):
    print("  [%d] %s | authors=%d | year=%s | doi=%s" % (
        i, r["title"], len(r["authors"]), r["year"], r["doi"] or "NONE"))

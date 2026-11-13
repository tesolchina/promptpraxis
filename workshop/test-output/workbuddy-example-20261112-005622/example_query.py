#!/usr/bin/env python3
"""Single real OpenAlex query for teaching-example verification.

Standard library only. No `sort` parameter (API default relevance order),
no mailto, no api_key, no credentials. Saves THIS run's raw response body
and request/response metadata. One request only: no retry, no second call.
"""
import datetime
import json
import os
import urllib.parse
import urllib.request

OUT = r"\\wsl.localhost\Ubuntu\home\andy\projects\promptpraxis\workshop\test-output\workbuddy-example-20261112-005622"
META = os.path.join(OUT, "request_meta.json")
BODY = os.path.join(OUT, "raw_response.json")


def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


# Deliberately no "sort": OpenAlex uses its default search relevance order.
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
    "requested_at_utc": utc(),
    "url": url,
    "query_params": qp,
    "method": req.get_method(),
    "request_headers": dict(req.headers),
    "timeout_seconds": 30,
    "raw_body_file": BODY,
    "query_contains_sort": "sort" in qp,
    "query_contains_mailto": "mailto" in qp,
    "query_contains_api_key": "api_key" in qp,
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

data = json.loads(body.decode("utf-8"))
meta = data.get("meta", {})
print("HTTP status:", entry["http_status"])
print("raw body bytes:", len(body))
print("meta.count:", meta.get("count"))
xq = meta.get("x_query", {})
print("x_query.order:", xq.get("order"), "| order_default:", xq.get("order_default"))
print("results:", len(data.get("results", [])))
for i, w in enumerate(data.get("results", []), 1):
    print("  [%d] (%s) %s" % (i, w.get("publication_year"), w.get("title")))

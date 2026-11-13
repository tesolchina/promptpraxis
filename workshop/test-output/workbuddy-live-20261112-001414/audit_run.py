#!/usr/bin/env python3
"""Audit-only wrapper for ONE live run of the project's fetch_literature.py.

Lives inside the live output directory. It intercepts urllib.request.urlopen
only to tee THIS run's raw HTTP response body to disk and to record request
metadata. The Request object, URL, query params, headers, timeout and the
project's parsing code are untouched. No retry and no second request.
"""
import datetime
import json
import os
import runpy
import sys
import urllib.parse
import urllib.request

SCRIPT = r"\\wsl.localhost\Ubuntu\home\andy\projects\promptpraxis\workshop\fetch_literature.py"
OUT = r"\\wsl.localhost\Ubuntu\home\andy\projects\promptpraxis\workshop\test-output\workbuddy-live-20261112-001414"
META_PATH = os.path.join(OUT, "request_meta.json")
BODY_PATH = os.path.join(OUT, "raw_response.json")

_orig_urlopen = urllib.request.urlopen
_calls = []


def _utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def _write_meta():
    with open(META_PATH, "w", encoding="utf-8") as fh:
        json.dump({"captured_at_utc": _utc(), "calls": _calls},
                  fh, ensure_ascii=False, indent=2)


class _TeeResponse:
    def __init__(self, resp, entry):
        self._resp = resp
        self._entry = entry

    def __enter__(self):
        self._resp.__enter__()
        return self

    def __exit__(self, *exc):
        return self._resp.__exit__(*exc)

    def read(self, *args, **kwargs):
        data = self._resp.read(*args, **kwargs)
        if data:
            with open(BODY_PATH, "ab") as fh:
                fh.write(data)
            self._entry["response_body_bytes"] = (
                self._entry.get("response_body_bytes", 0) + len(data)
            )
            _write_meta()
        return data

    def __getattr__(self, name):
        return getattr(self._resp, name)


def _audit_urlopen(req, *args, **kwargs):
    url = getattr(req, "full_url", None)
    entry = {
        "requested_at_utc": _utc(),
        "url": url,
        "query_params": (urllib.parse.parse_qs(urllib.parse.urlparse(url).query)
                         if url else None),
        "method": req.get_method() if hasattr(req, "get_method") else None,
        "request_headers": dict(getattr(req, "headers", {}) or {}),
        "timeout_seconds": kwargs.get("timeout"),
        "raw_body_file": BODY_PATH,
    }
    _calls.append(entry)
    try:
        resp = _orig_urlopen(req, *args, **kwargs)
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
        _write_meta()
        raise
    entry["http_status"] = getattr(resp, "status", None)
    entry["response_headers"] = {
        k: v for k, v in (getattr(resp, "headers", None) or {}).items()
    }
    _write_meta()
    return _TeeResponse(resp, entry)


urllib.request.urlopen = _audit_urlopen
sys.argv = [SCRIPT] + sys.argv[1:]
try:
    runpy.run_path(SCRIPT, run_name="__main__")
finally:
    _write_meta()

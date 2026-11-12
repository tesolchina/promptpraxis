#!/usr/bin/env python3
"""
fetch_literature.py — Automated literature metadata retriever for Prompt & Praxis Workshop

Queries the OpenAlex Works API for academic literature, extracts verified metadata,
and generates:
  1. A reading list CSV (with Status and Notes columns)
  2. A Zotero-importable BibTeX file (.bib)
  3. A Zotero-importable RIS file (.ris)

Features:
  - Standard library only (no pip dependencies required)
  - Parameterized: topic, publication year, sort order, result limit
  - OpenAlex polite pool support via mailto
  - Preserves missing data (no hallucinated DOIs, citations, or authors)
  - Full traceability: rows link to OpenAlex IDs and DOIs
  - Offline fixture support for automated testing

Usage:
  python3 fetch_literature.py --topic "automated written corrective feedback" --year 2024 --sort relevance --limit 5 --email=
"""

import argparse
import csv
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


def clean_text(text: str) -> str:
    """Normalize whitespace and remove control characters."""
    if not text:
        return ""
    return re.sub(r"\s+", " ", text).strip()


def extract_last_name(author_str: str) -> str:
    """Extract family name from 'Last, First' or 'First Last'."""
    clean = clean_text(author_str)
    if not clean:
        return "Unknown"
    if "," in clean:
        return clean.split(",")[0].strip()
    parts = clean.split()
    return parts[-1].strip() if parts else "Unknown"


def generate_citekey(authors: list, year: any, title: str) -> str:
    """Generate a clean BibTeX citekey, e.g., 'Hyland2026' or 'Compagnoni2024'."""
    first_author = "Unknown"
    if authors and len(authors) > 0:
        first_author = extract_last_name(authors[0])
    
    first_author_clean = re.sub(r"[^a-zA-Z]", "", first_author) or "Ref"
    year_str = str(year) if year else "nd"
    
    # Add first word of title if citekey might be non-unique
    title_words = re.sub(r"[^a-zA-Z0-9\s]", "", clean_text(title)).split()
    first_title_word = title_words[0].capitalize() if title_words else ""
    
    return f"{first_author_clean}{year_str}{first_title_word}"


def escape_bibtex(text: str) -> str:
    """Escape special characters in BibTeX field values."""
    if not text:
        return ""
    # Escape backslash, braces, comment char %, and ampersand
    t = text.replace("\\", "\\\\")
    t = t.replace("{", "\\{").replace("}", "\\}")
    t = t.replace("%", "\\%")
    t = t.replace("&", "\\&")
    return t


def query_openalex(topic: str, year: str, sort: str, limit: int, email: str, fixture_path: str = None) -> dict:
    """Query OpenAlex API or load from fixture."""
    if fixture_path:
        with open(fixture_path, "r", encoding="utf-8") as f:
            return json.load(f)

    # Build query parameters
    params = {
        "search": topic,
        "filter": f"from_publication_date:{year}-01-01",
        "per-page": str(min(limit, 50)),
    }
    if sort and sort != "relevance":
        params["sort"] = sort
    if email:
        params["mailto"] = email

    url = f"https://api.openalex.org/works?{urllib.parse.urlencode(params)}"
    
    headers = {
        "User-Agent": f"PromptPraxisWorkshop/1.0 (mailto:{email})" if email else "PromptPraxisWorkshop/1.0"
    }
    
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read().decode("utf-8")
            return json.loads(data)
    except urllib.error.HTTPError as e:
        sys.stderr.write(f"HTTP Error {e.code}: {e.reason}\n")
        if e.code == 429:
            sys.stderr.write("Rate limit exceeded. OpenAlex requests sharing the IP daily pool are limited.\n")
            sys.stderr.write("Recovery: Add an email to --email to use the polite pool, or try again later.\n")
        raise
    except urllib.error.URLError as e:
        sys.stderr.write(f"Network Connection Error: {e.reason}\n")
        sys.stderr.write("Recovery: Check internet connection or test with --fixture for offline mode.\n")
        raise


def parse_works(data: dict) -> list:
    """Parse raw OpenAlex works into normalized records, strictly preserving missing data."""
    results = data.get("results", [])
    parsed = []

    for item in results:
        openalex_id = item.get("id", "")
        title = clean_text(item.get("title") or "")
        year = item.get("publication_year")
        cited_by = item.get("cited_by_count")
        doi = item.get("doi") or ""  # e.g., 'https://doi.org/10.1111/modl.70084'
        
        # Primary location / journal
        primary_loc = item.get("primary_location") or {}
        source = primary_loc.get("source") or {}
        journal = clean_text(source.get("display_name") or "")
        
        # Authors
        authorships = item.get("authorships") or []
        authors = []
        for auth in authorships:
            author_obj = auth.get("author") or {}
            name = clean_text(author_obj.get("display_name") or "")
            if name:
                authors.append(name)
        
        # Open Access landing url
        oa = item.get("open_access") or {}
        oa_url = oa.get("oa_url") or primary_loc.get("landing_page_url") or ""

        parsed.append({
            "openalex_id": openalex_id,
            "title": title,
            "authors": authors,
            "year": year,
            "cited_by": cited_by,
            "doi": doi,
            "journal": journal,
            "oa_url": oa_url,
        })

    return parsed


def write_csv(records: list, output_path: str):
    """Write reading list CSV with Status and Notes columns."""
    fieldnames = [
        "OpenAlex_ID",
        "Title",
        "Authors",
        "Year",
        "Citations",
        "DOI",
        "Journal",
        "Reading_Status",
        "Notes"
    ]
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in records:
            writer.writerow({
                "OpenAlex_ID": r["openalex_id"],
                "Title": r["title"],
                "Authors": "; ".join(r["authors"]) if r["authors"] else "",
                "Year": r["year"] if r["year"] is not None else "",
                "Citations": r["cited_by"] if r["cited_by"] is not None else "",
                "DOI": r["doi"],
                "Journal": r["journal"],
                "Reading_Status": "Unread",
                "Notes": ""
            })


def write_bibtex(records: list, output_path: str):
    """Write Zotero-importable BibTeX file (.bib)."""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("% Generated by Prompt & Praxis literature pipeline\n\n")
        for r in records:
            citekey = generate_citekey(r["authors"], r["year"], r["title"])
            
            # Escape BibTeX special characters in title and journal
            safe_title = escape_bibtex(r["title"])
            safe_journal = escape_bibtex(r["journal"])
            
            f.write(f"@article{{{citekey},\n")
            f.write(f"  title = {{{{{safe_title}}}}},\n")
            if r["authors"]:
                authors_str = " and ".join(r["authors"])
                f.write(f"  author = {{{authors_str}}},\n")
            if r["year"]:
                f.write(f"  year = {{{r['year']}}},\n")
            if safe_journal:
                f.write(f"  journal = {{{{{safe_journal}}}}},\n")
            if r["doi"]:
                # Clean DOI url to DOI identifier if needed
                doi_clean = r["doi"].replace("https://doi.org/", "").replace("http://doi.org/", "")
                f.write(f"  doi = {{{doi_clean}}},\n")
                f.write(f"  url = {{{r['doi']}}},\n")
            elif r["oa_url"]:
                f.write(f"  url = {{{r['oa_url']}}},\n")
            if r["openalex_id"]:
                f.write(f"  note = {{OpenAlex: {r['openalex_id']}}},\n")
            f.write("}\n\n")


def write_ris(records: list, output_path: str):
    """Write Zotero-importable RIS file (.ris)."""
    with open(output_path, "w", encoding="utf-8") as f:
        for r in records:
            f.write("TY  - JOUR\n")
            if r["title"]:
                f.write(f"TI  - {r['title']}\n")
            for auth in r["authors"]:
                f.write(f"AU  - {auth}\n")
            if r["year"]:
                f.write(f"PY  - {r['year']}\n")
            if r["journal"]:
                f.write(f"JO  - {r['journal']}\n")
            if r["doi"]:
                doi_clean = r["doi"].replace("https://doi.org/", "").replace("http://doi.org/", "")
                f.write(f"DO  - {doi_clean}\n")
                f.write(f"UR  - {r['doi']}\n")
            elif r["oa_url"]:
                f.write(f"UR  - {r['oa_url']}\n")
            if r["openalex_id"]:
                f.write(f"N1  - OpenAlex: {r['openalex_id']}\n")
            f.write("ER  - \n\n")


def main():
    parser = argparse.ArgumentParser(description="Fetch literature metadata from OpenAlex into CSV and BibTeX/RIS.")
    parser.add_argument("--topic", type=str, default="automated written corrective feedback", help="Search topic")
    parser.add_argument("--year", type=str, default="2024", help="Earliest publication year (e.g. 2024)")
    parser.add_argument(
        "--sort",
        type=str,
        default="relevance",
        help="Sort order: 'relevance' (default, omits sort parameter for OpenAlex best-match ranking), 'cited_by_count:desc', or 'publication_date:desc'",
    )
    parser.add_argument("--limit", type=int, default=5, help="Number of records to retrieve (1-50)")
    parser.add_argument("--email", type=str, default="", help="Optional contact email for OpenAlex polite pool (leave empty to query standard pool)")
    parser.add_argument("--output-csv", type=str, default="found.csv", help="Output CSV path")
    parser.add_argument("--output-bib", type=str, default="found.bib", help="Output BibTeX path")
    parser.add_argument("--output-ris", type=str, default="found.ris", help="Output RIS path")
    parser.add_argument("--fixture", type=str, default=None, help="Path to offline JSON fixture")

    args = parser.parse_args()

    print(f"=== Literature Query Pipeline ===")
    print(f"Topic: {args.topic}")
    print(f"Since year: {args.year}")
    print(f"Sort: {args.sort}")
    print(f"Limit: {args.limit}")
    if args.fixture:
        print(f"Mode: Offline fixture ({args.fixture})")
    else:
        print(f"Mode: Live OpenAlex API ({args.email})")

    try:
        raw_data = query_openalex(
            topic=args.topic,
            year=args.year,
            sort=args.sort,
            limit=args.limit,
            email=args.email,
            fixture_path=args.fixture
        )
    except Exception as e:
        sys.stderr.write(f"Execution halted: {e}\n")
        sys.exit(1)

    meta = raw_data.get("meta", {})
    total_count = meta.get("count", 0)
    print(f"OpenAlex reports {total_count} matching records in database.")

    records = parse_works(raw_data)
    if not records:
        print("Notice: Query returned 0 records. Generating empty output templates.")
        write_csv([], args.output_csv)
        write_bibtex([], args.output_bib)
        write_ris([], args.output_ris)
        print(f"Saved empty templates to: {args.output_csv}, {args.output_bib}, {args.output_ris}")
        return

    print(f"Parsed {len(records)} publications.")
    
    # Save files
    write_csv(records, args.output_csv)
    write_bibtex(records, args.output_bib)
    write_ris(records, args.output_ris)

    print(f"Outputs written successfully:")
    print(f"  - Reading list CSV: {args.output_csv}")
    print(f"  - Zotero BibTeX:   {args.output_bib}")
    print(f"  - Zotero RIS:      {args.output_ris}")
    print("\nSample result summary:")
    for i, r in enumerate(records[:3], 1):
        print(f"  [{i}] ({r['year'] or 'n.d.'}) {r['title']}")
        print(f"      Authors: {', '.join(r['authors'][:3]) if r['authors'] else 'Unknown'}")
        print(f"      Citations: {r['cited_by']} | DOI: {r['doi'] or 'None'}")


if __name__ == "__main__":
    main()

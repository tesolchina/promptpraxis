#!/usr/bin/env python3
"""
zotero_formatter.py — Minimal Working Spike: Lightweight Citation Formatting Engine

[EXPERIMENTAL / HEURISTIC PROOF-OF-CONCEPT]
A zero-dependency citation formatting spike (Simon's Fallback) created for
demonstration in WorkBuddy environments.

Scope & Disclaimers:
  - Implements simplified, heuristic approximations of APA 7th, IEEE, and Nature styles.
  - Converts OpenAlex literature metadata into a minimal CSL-JSON item record.
  - DOES NOT implement the full Citation Style Language (CSL 1.0.2) engine or XML style sheets.
  - Has NOT been validated against the official CSL test suite or formal publisher style specs.
  - Intended solely as a pedagogical demonstration and fallback discussion artifact.

Licence: MIT (Free of AGPL copyleft contamination)
"""

import json
import re
import sys
from typing import Dict, List, Optional


def format_author_name_apa(display_name: str) -> str:
    """Format 'FirstName MiddleName LastName' -> 'LastName, F. M.' for APA."""
    clean = re.sub(r"\s+", " ", display_name).strip()
    if not clean:
        return "Unknown"
    
    # Handle institutional authors or single names
    if "," in clean:
        parts = clean.split(",")
        last = parts[0].strip()
        initials = " ".join([f"{p.strip()[0]}." for p in parts[1].split() if p.strip()])
        return f"{last}, {initials}".strip(", ")
    
    parts = clean.split()
    if len(parts) == 1:
        return parts[0]
    
    last = parts[-1]
    initials = " ".join([f"{p[0]}." for p in parts[:-1] if p and p[0].isalpha()])
    return f"{last}, {initials}".strip()


def format_author_name_ieee(display_name: str) -> str:
    """Format 'FirstName MiddleName LastName' -> 'F. M. LastName' for IEEE."""
    clean = re.sub(r"\s+", " ", display_name).strip()
    if not clean:
        return "Unknown"
    
    if "," in clean:
        parts = clean.split(",")
        last = parts[0].strip()
        initials = " ".join([f"{p.strip()[0]}." for p in parts[1].split() if p.strip()])
        return f"{initials} {last}".strip()
    
    parts = clean.split()
    if len(parts) == 1:
        return parts[0]
    
    last = parts[-1]
    initials = " ".join([f"{p[0]}." for p in parts[:-1] if p and p[0].isalpha()])
    return f"{initials} {last}".strip()


def format_author_list_apa(authors: List[str]) -> str:
    """Format authors list according to APA 7th edition rules."""
    if not authors:
        return "Unknown Author"
    
    formatted = [format_author_name_apa(a) for a in authors]
    n = len(formatted)
    
    if n == 1:
        return formatted[0]
    elif n == 2:
        return f"{formatted[0]}, & {formatted[1]}"
    elif 3 <= n <= 20:
        return ", ".join(formatted[:-1]) + f", & {formatted[-1]}"
    else:  # Over 20 authors
        return ", ".join(formatted[:19]) + ", ... " + formatted[-1]


def format_author_list_ieee(authors: List[str]) -> str:
    """Format authors list according to IEEE rules."""
    if not authors:
        return "Unknown Author"
    
    formatted = [format_author_name_ieee(a) for a in authors]
    n = len(formatted)
    
    if n == 1:
        return formatted[0]
    elif n == 2:
        return f"{formatted[0]} and {formatted[1]}"
    elif 3 <= n <= 6:
        return ", ".join(formatted[:-1]) + f", and {formatted[-1]}"
    else:  # More than 6 authors: use et al.
        return f"{formatted[0]} et al."


def to_csl_json(work: dict) -> dict:
    """Convert normalized work record to CSL-JSON schema."""
    authors = work.get("authors", [])
    csl_authors = []
    for a in authors:
        parts = a.split()
        if len(parts) > 1:
            csl_authors.append({"family": parts[-1], "given": " ".join(parts[:-1])})
        else:
            csl_authors.append({"literal": a})

    csl = {
        "id": work.get("openalex_id", "item-1"),
        "type": "article-journal",
        "title": work.get("title", ""),
        "author": csl_authors,
        "container-title": work.get("journal", ""),
        "DOI": work.get("doi", "").replace("https://doi.org/", ""),
        "URL": work.get("doi") or work.get("oa_url", ""),
    }
    if work.get("year"):
        csl["issued"] = {"date-parts": [[work["year"]]]}
    return csl


def format_apa(work: dict) -> str:
    """Format work as APA 7th edition reference."""
    authors_str = format_author_list_apa(work.get("authors", []))
    year_str = f"({work.get('year')})" if work.get("year") else "(n.d.)"
    title = work.get("title", "").rstrip(".")
    journal = work.get("journal", "")
    doi = work.get("doi", "")

    citation = f"{authors_str} {year_str}. {title}."
    if journal:
        citation += f" *{journal}*."
    if doi:
        citation += f" {doi}"
    elif work.get("oa_url"):
        citation += f" {work['oa_url']}"
    return citation


def format_ieee(work: dict, index: int = 1) -> str:
    """Format work as IEEE style reference."""
    authors_str = format_author_list_ieee(work.get("authors", []))
    title = work.get("title", "").rstrip(".")
    journal = work.get("journal", "")
    year = work.get("year", "")
    doi = work.get("doi", "")

    ref = f"[{index}] {authors_str}, \"{title},\""
    if journal:
        ref += f" *{journal}*,"
    if year:
        ref += f" {year}."
    if doi:
        ref += f" doi: {doi.replace('https://doi.org/', '')}."
    return ref


def format_nature(work: dict, index: int = 1) -> str:
    """Format work as Nature style reference."""
    authors = work.get("authors", [])
    if not authors:
        authors_str = "Unknown"
    elif len(authors) > 5:
        first = format_author_name_apa(authors[0])
        authors_str = f"{first} *et al.*"
    else:
        authors_str = ", ".join([format_author_name_apa(a) for a in authors[:-1]])
        if len(authors) > 1:
            authors_str += f" & {format_author_name_apa(authors[-1])}"
        else:
            authors_str = format_author_name_apa(authors[0])

    title = work.get("title", "").rstrip(".")
    journal = work.get("journal", "")
    year = work.get("year", "")
    doi = work.get("doi", "")

    ref = f"{index}. {authors_str} {title}."
    if journal:
        ref += f" *{journal}*"
    if year:
        ref += f" ({year})."
    if doi:
        ref += f" {doi}"
    return ref


if __name__ == "__main__":
    sample_work = {
        "openalex_id": "https://openalex.org/W4414281281",
        "title": "DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning",
        "authors": ["Daya Guo", "Dejian Yang", "Haowei Zhang", "Junxiao Song", "Peiyi Wang"],
        "year": 2025,
        "journal": "Nature",
        "doi": "https://doi.org/10.1038/s41586-025-09422-z"
    }

    print("=== Citation Formatting Spike ===")
    print("\n--- APA 7th Edition ---")
    print(format_apa(sample_work))
    print("\n--- IEEE Style ---")
    print(format_ieee(sample_work, 1))
    print("\n--- Nature Style ---")
    print(format_nature(sample_work, 1))
    print("\n--- CSL-JSON Schema ---")
    print(json.dumps(to_csl_json(sample_work), indent=2))

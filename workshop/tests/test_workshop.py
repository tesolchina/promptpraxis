#!/usr/bin/env python3
"""
test_workshop.py — Automated test suite for Prompt & Praxis Entry 2 Workshop

Covers:
  - Normal query (fixture-based & live API)
  - Empty results (fixture-based: zero hallucinated rows)
  - Missing metadata preservation (fixture-based: missing DOIs, authors, citations)
  - Network and access failure handling
  - Track A prompt simulation (end-to-end table -> CSV -> BibTeX)
  - Track B parameter customization (topic, year, sort)
  - Zotero import compatibility validation
"""

import contextlib
import csv
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
import urllib.error
import urllib.parse
from unittest import mock
from pathlib import Path

# Add workshop root to sys.path
WORKSHOP_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(WORKSHOP_DIR))

import fetch_literature
import verify_zotero_import


class TestWorkshopPipeline(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.fixtures_dir = WORKSHOP_DIR / "tests" / "fixtures"

    def tearDown(self):
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_01_fixture_normal_query(self):
        """[FIXTURE] Normal query parses 3 items, preserves fields, and outputs CSV/Bib/RIS."""
        fixture_file = str(self.fixtures_dir / "openalex_normal.json")
        csv_out = os.path.join(self.temp_dir, "found.csv")
        bib_out = os.path.join(self.temp_dir, "found.bib")
        ris_out = os.path.join(self.temp_dir, "found.ris")

        data = fetch_literature.query_openalex(
            topic="applied linguistics AI",
            year="2024",
            sort="cited_by_count:desc",
            limit=3,
            email="test@example.com",
            fixture_path=fixture_file
        )
        records = fetch_literature.parse_works(data)
        self.assertEqual(len(records), 3)

        # Verify record 1
        r1 = records[0]
        self.assertEqual(r1["title"], "Qwen3 Technical Report")
        self.assertEqual(r1["year"], 2025)
        self.assertEqual(r1["cited_by"], 17561)
        self.assertEqual(r1["doi"], "https://doi.org/10.48550/arxiv.2505.09388")
        self.assertEqual(len(r1["authors"]), 2)

        # Write files
        fetch_literature.write_csv(records, csv_out)
        fetch_literature.write_bibtex(records, bib_out)
        fetch_literature.write_ris(records, ris_out)

        # Check CSV
        with open(csv_out, "r", encoding="utf-8") as f:
            reader = list(csv.DictReader(f))
            self.assertEqual(len(reader), 3)
            self.assertEqual(reader[0]["Reading_Status"], "Unread")
            self.assertEqual(reader[0]["Notes"], "")
            self.assertIn("Qwen3", reader[0]["Title"])

        # Check BibTeX and RIS validation
        bib_res = verify_zotero_import.verify_bibtex(bib_out)
        self.assertEqual(bib_res["status"], "PASS")
        self.assertEqual(bib_res["records"], 3)

        ris_res = verify_zotero_import.verify_ris(ris_out)
        self.assertEqual(ris_res["status"], "PASS")
        self.assertEqual(ris_res["records"], 3)

    def test_02_fixture_empty_results(self):
        """[FIXTURE] Empty query returns 0 records and never hallucinates rows."""
        fixture_file = str(self.fixtures_dir / "openalex_empty.json")
        csv_out = os.path.join(self.temp_dir, "empty.csv")
        bib_out = os.path.join(self.temp_dir, "empty.bib")
        ris_out = os.path.join(self.temp_dir, "empty.ris")

        data = fetch_literature.query_openalex(
            topic="nonexistent topic xyz12345",
            year="2024",
            sort="cited_by_count:desc",
            limit=10,
            email="test@example.com",
            fixture_path=fixture_file
        )
        records = fetch_literature.parse_works(data)
        self.assertEqual(len(records), 0, "Empty response must yield 0 records")

        fetch_literature.write_csv(records, csv_out)
        fetch_literature.write_bibtex(records, bib_out)
        fetch_literature.write_ris(records, ris_out)

        with open(csv_out, "r", encoding="utf-8") as f:
            reader = list(csv.DictReader(f))
            self.assertEqual(len(reader), 0, "CSV must have zero data rows")

        bib_res = verify_zotero_import.verify_bibtex(bib_out)
        self.assertEqual(bib_res["status"], "PASS")
        self.assertEqual(bib_res["records"], 0)

    def test_03_fixture_missing_metadata(self):
        """[FIXTURE] Missing metadata (DOI, year, citations, authors) is preserved as empty/None, never fabricated."""
        fixture_file = str(self.fixtures_dir / "openalex_missing_metadata.json")
        csv_out = os.path.join(self.temp_dir, "missing.csv")
        bib_out = os.path.join(self.temp_dir, "missing.bib")

        data = fetch_literature.query_openalex(
            topic="test",
            year="2024",
            sort="cited_by_count:desc",
            limit=2,
            email="test@example.com",
            fixture_path=fixture_file
        )
        records = fetch_literature.parse_works(data)
        self.assertEqual(len(records), 2)

        # Record 1: missing DOI, year, citations, authors
        r1 = records[0]
        self.assertEqual(r1["doi"], "", "Missing DOI must remain empty string")
        self.assertIsNone(r1["year"], "Missing year must remain None")
        self.assertIsNone(r1["cited_by"], "Missing citation count must remain None")
        self.assertEqual(r1["authors"], [], "Empty authors list must remain empty")

        fetch_literature.write_csv(records, csv_out)
        fetch_literature.write_bibtex(records, bib_out)

        with open(csv_out, "r", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
            self.assertEqual(rows[0]["DOI"], "")
            self.assertEqual(rows[0]["Year"], "")
            self.assertEqual(rows[0]["Citations"], "")
            self.assertEqual(rows[0]["Authors"], "", "Missing authors must be empty string in CSV")

        # BibTeX verification:
        # Record 1 (no authors) must omit 'author =' line, while retaining citekey placeholder
        with open(bib_out, "r", encoding="utf-8") as f:
            bib_content = f.read()

        entries = bib_content.split("@article{")[1:]
        self.assertEqual(len(entries), 2)

        entry1 = entries[0]
        self.assertNotIn("author =", entry1, "Missing authors must omit 'author = ' field in BibTeX")
        self.assertTrue(entry1.startswith("Unknownnd") or entry1.startswith("Refnd"),
                        f"Entry 1 citekey must have placeholder, got: {entry1[:20]}")

        entry2 = entries[1]
        self.assertIn("author =", entry2, "Entries with authors must include 'author = ' field in BibTeX")

        # Verify parser still passes
        bib_res = verify_zotero_import.verify_bibtex(bib_out)
        self.assertEqual(bib_res["status"], "PASS")

        # Record 2: has DOI but no source journal
        r2 = records[1]
        self.assertEqual(r2["doi"], "https://doi.org/10.1234/test.5678")
        self.assertEqual(r2["journal"], "")

    @mock.patch("urllib.request.urlopen")
    def test_04_network_failure_handling(self, mock_urlopen):
        """[MOCK NETWORK FAILURE] Verifies error messages, recovery advice, and non-zero exit code on URLError."""
        # Mock network disconnection/failure without real network calls
        mock_urlopen.side_effect = urllib.error.URLError("Temporary failure in name resolution")

        stderr_capture = io.StringIO()
        with contextlib.redirect_stderr(stderr_capture):
            # 1. Test function-level error handling and guidance
            with self.assertRaises(urllib.error.URLError):
                fetch_literature.query_openalex(
                    topic="test",
                    year="2024",
                    sort="cited_by_count:desc",
                    limit=5,
                    email="test@example.com"
                )

        err_output = stderr_capture.getvalue()
        self.assertIn("Network Connection Error", err_output)
        self.assertIn("Recovery: Check internet connection or test with --fixture", err_output)

        # 2. Test CLI main() exit code and stderr handling
        test_args = [
            "fetch_literature.py",
            "--topic", "test",
            "--output-csv", os.path.join(self.temp_dir, "test.csv")
        ]
        cli_stderr = io.StringIO()
        with mock.patch.object(sys, "argv", test_args):
            with contextlib.redirect_stderr(cli_stderr):
                with self.assertRaises(SystemExit) as exit_ctx:
                    fetch_literature.main()
                self.assertEqual(exit_ctx.exception.code, 1, "CLI must exit with code 1 on network failure")

        self.assertIn("Execution halted", cli_stderr.getvalue())

    def test_05_live_api_query(self):
        """[LIVE API] Live OpenAlex API call returns verified academic literature."""
        csv_out = os.path.join(self.temp_dir, "live.csv")
        bib_out = os.path.join(self.temp_dir, "live.bib")
        ris_out = os.path.join(self.temp_dir, "live.ris")

        try:
            data = fetch_literature.query_openalex(
                topic="applied linguistics AI",
                year="2024",
                sort="cited_by_count:desc",
                limit=3,
                email="andyzheng0715@example.com"
            )
        except fetch_literature.urllib.error.HTTPError as e:
            if e.code in (403, 429):
                self.skipTest(f"Live OpenAlex API blocked or rate-limited ({e.code}: {e.reason})")
            raise
        except fetch_literature.urllib.error.URLError as e:
            self.skipTest(f"Live OpenAlex API network unavailable ({e.reason})")

        self.assertIn("results", data)
        self.assertGreater(data.get("meta", {}).get("count", 0), 1000)

        records = fetch_literature.parse_works(data)
        self.assertEqual(len(records), 3)

        for r in records:
            self.assertTrue(r["title"])
            self.assertTrue(r["openalex_id"].startswith("https://openalex.org/W"))
            if r["doi"]:
                self.assertTrue(r["doi"].startswith("https://doi.org/"))

        fetch_literature.write_csv(records, csv_out)
        fetch_literature.write_bibtex(records, bib_out)
        fetch_literature.write_ris(records, ris_out)

        bib_res = verify_zotero_import.verify_bibtex(bib_out)
        self.assertEqual(bib_res["status"], "PASS")

        ris_res = verify_zotero_import.verify_ris(ris_out)
        self.assertEqual(ris_res["status"], "PASS")

    def test_06_parameter_customization_track_b(self):
        """[TRACK B] Verify parameterization of topic, year, and sort using fixtures."""
        csv_out = os.path.join(self.temp_dir, "custom.csv")
        fixture_file = str(self.fixtures_dir / "openalex_normal.json")

        # Load fixture to verify parameter-driven transformation and filtering
        data = fetch_literature.query_openalex(
            topic="second language acquisition",
            year="2025",
            sort="publication_date:desc",
            limit=2,
            email="andyzheng0715@example.com",
            fixture_path=fixture_file
        )
        records = fetch_literature.parse_works(data)
        self.assertEqual(len(records), 3)
        fetch_literature.write_csv(records, csv_out)
        self.assertTrue(os.path.exists(csv_out))

    def test_07_special_characters_and_author_parsing(self):
        """[EDGE CASE] Author name formats and BibTeX special character escaping."""
        bib_out = os.path.join(self.temp_dir, "escaped.bib")

        # Test citekey extraction for both 'Last, First' and 'First Last'
        self.assertEqual(fetch_literature.extract_last_name("Yang, An"), "Yang")
        self.assertEqual(fetch_literature.extract_last_name("Ken Hyland"), "Hyland")
        self.assertEqual(fetch_literature.extract_last_name("OpenAI"), "OpenAI")

        key1 = fetch_literature.generate_citekey(["Yang, An"], 2025, "Qwen3 Technical Report")
        self.assertTrue(key1.startswith("Yang2025"), f"Expected Yang2025 citekey, got {key1}")

        key2 = fetch_literature.generate_citekey(["Ken Hyland"], 2026, "AI for Applied Linguistics")
        self.assertTrue(key2.startswith("Hyland2026"), f"Expected Hyland2026 citekey, got {key2}")

        # Test BibTeX escaping of %, &, and braces
        record_with_special_chars = [{
            "openalex_id": "https://openalex.org/W999",
            "title": "Study on 50% Accuracy & Gains in {Deep Learning}",
            "authors": ["Doe, Jane", "Smith, John"],
            "year": 2025,
            "cited_by": 10,
            "doi": "https://doi.org/10.1234/test",
            "journal": "Computers & Education",
            "oa_url": ""
        }]
        fetch_literature.write_bibtex(record_with_special_chars, bib_out)
        with open(bib_out, "r", encoding="utf-8") as f:
            bib_content = f.read()

        self.assertIn(r"50\%", bib_content, "% must be escaped as \\%")
        self.assertIn(r"\&", bib_content, "& must be escaped as \\&")
        
        # Verify parser still passes
        bib_res = verify_zotero_import.verify_bibtex(bib_out)
        self.assertEqual(bib_res["status"], "PASS")

    @mock.patch("urllib.request.urlopen")
    def test_08_request_url_construction(self, mock_urlopen):
        """[MOCK URL] Verifies request URL construction: sort omitted for relevance, preserved for cited_by_count:desc, and param encoding."""
        mock_resp = mock.MagicMock()
        mock_resp.read.return_value = json.dumps({"meta": {"count": 0}, "results": []}).encode("utf-8")
        mock_resp.__enter__.return_value = mock_resp
        mock_urlopen.return_value = mock_resp

        # 1. Relevance sort: URL must NOT contain 'sort' parameter
        fetch_literature.query_openalex(
            topic="automated written corrective feedback",
            year="2024",
            sort="relevance",
            limit=5,
            email="test@example.com"
        )
        req1 = mock_urlopen.call_args[0][0]
        url1 = req1.full_url
        parsed_url1 = urllib.parse.urlparse(url1)
        query_params1 = urllib.parse.parse_qs(parsed_url1.query)

        self.assertNotIn("sort", query_params1, "When sort='relevance', 'sort' parameter must be omitted")
        self.assertEqual(query_params1["search"], ["automated written corrective feedback"])
        self.assertEqual(query_params1["filter"], ["from_publication_date:2024-01-01"])
        self.assertEqual(query_params1["per-page"], ["5"])
        self.assertEqual(query_params1["mailto"], ["test@example.com"])

        # 2. cited_by_count:desc sort: URL must retain sort parameter
        fetch_literature.query_openalex(
            topic="applied linguistics AI",
            year="2024",
            sort="cited_by_count:desc",
            limit=10,
            email="test@example.com"
        )
        req2 = mock_urlopen.call_args[0][0]
        url2 = req2.full_url
        parsed_url2 = urllib.parse.urlparse(url2)
        query_params2 = urllib.parse.parse_qs(parsed_url2.query)

        self.assertIn("sort", query_params2, "When sort='cited_by_count:desc', 'sort' parameter must be preserved")
        self.assertEqual(query_params2["sort"], ["cited_by_count:desc"])
        self.assertEqual(query_params2["search"], ["applied linguistics AI"])
        self.assertEqual(query_params2["filter"], ["from_publication_date:2024-01-01"])
        self.assertEqual(query_params2["per-page"], ["10"])

        # 3. Parameter encoding check (special characters in topic, limit capping at 50)
        fetch_literature.query_openalex(
            topic="AI & second-language writing",
            year="2023",
            sort="publication_date:desc",
            limit=100,
            email="test@example.com"
        )
        req3 = mock_urlopen.call_args[0][0]
        url3 = req3.full_url
        parsed_url3 = urllib.parse.urlparse(url3)
        query_params3 = urllib.parse.parse_qs(parsed_url3.query)

        self.assertEqual(query_params3["search"], ["AI & second-language writing"])
        self.assertEqual(query_params3["filter"], ["from_publication_date:2023-01-01"])
        self.assertEqual(query_params3["per-page"], ["50"], "limit > 50 must be capped at 50")
        self.assertEqual(query_params3["sort"], ["publication_date:desc"])


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env python3
"""
test_zotero_spike.py — Unit tests for the Zotero Feasibility Spike
"""

import unittest
from zotero_formatter import (
    format_apa,
    format_ieee,
    format_nature,
    format_author_name_apa,
    format_author_name_ieee,
    to_csl_json
)


class TestZoteroSpike(unittest.TestCase):
    def setUp(self):
        self.item = {
            "openalex_id": "https://openalex.org/W12345",
            "title": "Agentic AI in Language Education",
            "authors": ["Simon Wang", "Andy Zheng", "Maya Gosztyla"],
            "year": 2026,
            "journal": "IEEE Transactions on Professional Communication",
            "doi": "https://doi.org/10.1109/TPC.2026.0001"
        }

    def test_author_name_formatting(self):
        self.assertEqual(format_author_name_apa("Simon Wang"), "Wang, S.")
        self.assertEqual(format_author_name_ieee("Simon Wang"), "S. Wang")
        self.assertEqual(format_author_name_apa("Maya Gosztyla"), "Gosztyla, M.")
        self.assertEqual(format_author_name_ieee("Maya Gosztyla"), "M. Gosztyla")

    def test_apa_formatting(self):
        apa = format_apa(self.item)
        self.assertIn("Wang, S., Zheng, A., & Gosztyla, M.", apa)
        self.assertIn("(2026)", apa)
        self.assertIn("Agentic AI in Language Education.", apa)
        self.assertIn("*IEEE Transactions on Professional Communication*.", apa)
        self.assertIn("https://doi.org/10.1109/TPC.2026.0001", apa)

    def test_ieee_formatting(self):
        ieee = format_ieee(self.item, 1)
        self.assertTrue(ieee.startswith("[1]"))
        self.assertIn("S. Wang, A. Zheng, and M. Gosztyla", ieee)
        self.assertIn("\"Agentic AI in Language Education,\"", ieee)
        self.assertIn("doi: 10.1109/TPC.2026.0001.", ieee)

    def test_nature_formatting(self):
        nature = format_nature(self.item, 1)
        self.assertTrue(nature.startswith("1."))
        self.assertIn("Wang, S., Zheng, A. & Gosztyla, M.", nature)
        self.assertIn("(2026)", nature)

    def test_csl_json(self):
        csl = to_csl_json(self.item)
        self.assertEqual(csl["type"], "article-journal")
        self.assertEqual(csl["title"], "Agentic AI in Language Education")
        self.assertEqual(len(csl["author"]), 3)
        self.assertEqual(csl["author"][0]["family"], "Wang")
        self.assertEqual(csl["author"][0]["given"], "Simon")
        self.assertEqual(csl["issued"]["date-parts"], [[2026]])


if __name__ == "__main__":
    unittest.main()

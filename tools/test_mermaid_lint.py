#!/usr/bin/env python3
"""Regression tests for the deterministic Mermaid-block linter (tools/mermaid_lint.py)."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]        # repo root
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT.parent))

from tools import mermaid_lint as ml


GOOD = [
    # arrow-form numeric axes (the only legal numeric form on Mermaid >= 10)
    "```mermaid\nxychart-beta\n  x-axis 0 --> 4\n  y-axis -20 --> 20\n  line [20, 10, 0, -10, -20]\n  line [0, 0]\n```",
    # labelled arrow axes
    '```mermaid\nxychart-beta\n  x-axis "f" 0 --> 12\n  y-axis "Kmax" 0 --> 3\n  line [0, 1, 2]\n```',
    # categorical x tick list + numeric y range
    '```mermaid\nxychart-beta\n  x-axis ["a", "b", "c"]\n  y-axis 0 --> 1\n  line [1, 2, 3]\n```',
    # quoted mindmap root is safe
    '```mermaid\nmindmap\n  root(("x(t)"))\n    Wave\n```',
    # flowchart / quadrantChart pass
    "```mermaid\nflowchart TD\n  A --> B\n```",
    "```mermaid\nquadrantChart\n  x-axis A --> B\n  y-axis C --> D\n  quadrant-1 one\n```",
]

BAD = [
    # obsolete numeric bracket range on x-axis
    ("xychart-beta\n  x-axis [0, 4]\n  y-axis -10 --> 10\n  line [1, 2, 3]",
     "numeric bracket range"),
    # y-axis bracket list is never legal
    ('xychart-beta\n  x-axis ["a", "b"]\n  y-axis ["1", "2"]\n  line [1, 2]',
     "y-axis bracket"),
    # bare parentheses in a mindmap root break the parser
    ("mindmap\n  root((x(t)))\n    Wave",
     "parentheses"),
    # LaTeX inside a mermaid block renders literally
    ("flowchart TD\n  A[\"$x$\"] --> B",
     "LaTeX"),
]


class Linter(unittest.TestCase):
    def test_valid_blocks_pass(self):
        for block in GOOD:
            self.assertEqual(ml.lint(block), [], f"valid block flagged: {block.splitlines()[0]}")

    def test_broken_blocks_caught(self):
        for block, needle in BAD:
            wrapped = "```mermaid\n" + block + "\n```"
            got = ml.lint(wrapped)
            self.assertTrue(got, f"broken block not caught: {block[:40]!r}")
            self.assertTrue(any(needle.lower() in g.lower() for g in got),
                            f"expected mention of {needle!r} in {got}")

    def test_balanced_flowchart_quotes(self):
        # quoted node labels with spaces are legal and must not trip the balance check
        block = '```mermaid\nflowchart TD\n  A["capacitor"] --> B["charges to V0"]\n```'
        self.assertEqual(ml.lint(block), [])


if __name__ == "__main__":
    unittest.main()

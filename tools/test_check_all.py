#!/usr/bin/env python3
"""Regression tests: Markdown opt-in must not change legacy HTML counting."""
import tempfile
from pathlib import Path
import unittest
from check_all import count


class RegistryCounts(unittest.TestCase):
    def test_html_unchanged(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)/'Chapter.html'
            s = '<figure class="fig"><div class="q"><details class="sol"><m>x</m>'
            p.write_text(s)
            (Path(tmp)/'Chapter.md').write_text('### E1 — not counted\n$x$')
            self.assertEqual(count(tmp), dict(pages=['Chapter.html'], figures=1, questions=1,
                                             solutions=1, math_spans=1, bytes_html=len(s.encode())))

    def test_markdown_master_only(self):
        with tempfile.TemporaryDirectory() as tmp:
            s = '## 1. Intro\n**C1 — check**\n### E1 — example\n#### Q1. Test\n<details>solution</details>\n$x$\n$$y$$\n![a](assets/figures/fig-001.svg)\n'
            (Path(tmp)/'Course.md').write_text(s)
            (Path(tmp)/'Solutions.md').write_text(s*4)
            data = count(tmp, 'topic/Course.md')
            self.assertEqual(data['pages'], ['Course.md'])
            self.assertEqual(data['questions'], 3)
            self.assertEqual(data['solutions'], 1)
            self.assertEqual(data['figures'], 1)
            self.assertEqual(data['math_spans'], 2)
            self.assertEqual(data['display_formulas'], 1)
            self.assertEqual(data['words'], len(s.split()))
            self.assertEqual(data['bytes_markdown'], len(s.encode()))
            self.assertEqual(data['bytes_html'], 0)


if __name__ == '__main__':
    unittest.main()

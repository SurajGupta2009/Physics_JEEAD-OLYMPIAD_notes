#!/usr/bin/env python3
"""Negative tests ensure the Markdown gate rejects common authoring regressions."""
import unittest
from check import MASTER, validate
from export import exports


class ContentGate(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = MASTER.read_text(encoding='utf-8')

    def test_clean_source(self):
        self.assertEqual(validate(self.source), [])

    def test_lost_solution(self):
        self.assertTrue(validate(self.source.replace('</details>', '', 1)))

    def test_missing_dollar(self):
        self.assertTrue(validate(self.source + '\n$broken math\n'))

    def test_missing_figure(self):
        self.assertTrue(validate(self.source.replace('fig-001.svg', 'fig-999.svg', 1)))

    def test_mark_total(self):
        self.assertTrue(validate(self.source.replace('[3 marks]', '[5 marks]', 1)))

    def test_rubric_total(self):
        self.assertTrue(validate(self.source.replace('**(a), 3 marks:', '**(a), 4 marks:', 1)))

    def test_missing_validity(self):
        self.assertTrue(validate(self.source.replace('**Validity:**', '**Assumption:**', 1)))

    def test_exports_separate_answers(self):
        result = exports(self.source)
        self.assertNotIn('<details>', result['Paper.md'])
        self.assertNotIn('### Answer key', result['Paper.md'])
        self.assertEqual(result['Paper.md'].count('#### Q'), 36)
        self.assertEqual(result['Solutions.md'].count('#### Q'), 36)
        self.assertIn('**(c), 3 marks:**', result['Solutions.md'])
        self.assertIn('Sheet B', result['Formula-sheet.md'])


if __name__ == '__main__':
    unittest.main()

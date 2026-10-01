"""Repository-wide diagram verification: every chapter, every native scene.

Runs the same checks as ``python3 tools/verify_all_diagrams.py`` and pins the
expected coverage so a regression in any chapter fails the test suite.
"""
import unittest

from tools.verify_all_diagrams import verify

EXPECTED_CHAPTERS = 31
EXPECTED_SCENES = 544


class VerifyAllDiagramsTests(unittest.TestCase):
    def test_every_chapter_passes(self):
        problems, rows = verify()
        self.assertEqual(problems, [], "\n".join(problems))
        self.assertEqual(len(rows), EXPECTED_CHAPTERS)
        self.assertEqual(sum(scenes for _, _, scenes in rows), EXPECTED_SCENES)
        self.assertEqual(len({slug for slug, _, _ in rows}), EXPECTED_CHAPTERS)

    def test_every_brief_has_a_scene(self):
        _, rows = verify()
        for slug, briefs, scenes in rows:
            self.assertEqual(briefs, scenes, f"{slug}: {briefs} briefs but {scenes} scenes")
            self.assertGreater(briefs, 0, f"{slug}: no diagrams")


if __name__ == "__main__":
    unittest.main()

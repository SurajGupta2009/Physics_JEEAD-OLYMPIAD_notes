"""Course slots 25–31: native brief scenes for the seven remaining chapters.

Covers coverage, provenance, deterministic regeneration, preservation of the
original brief text and sample analytic values.
"""
import hashlib
import json
import math
import re
import subprocess
import unittest
from pathlib import Path

from tools.build_excalidraw_remaining import DRAW, ROOT
from tools.excalidraw_additions import base_ref, insert_only, original_text
from tools.excalidraw_checks import SCENE_BLOCK_PATTERN

EXPECTED = {'photoelectric-effect': 13, 'atomic-structure': 13, 'x-rays': 13,
            'nuclear-physics': 16, 'semiconductors': 18,
            'communication-systems': 12, 'special-relativity': 12}
COMPANION = r'> \*\*Companion:\*\*[^\n]*\n\n!\[\[[^\n]+\]\]\n'
PRIMITIVES = {'text', 'line', 'arrow', 'rectangle', 'ellipse'}


def scene(slug, drawing):
    text = (ROOT / drawing['file']).read_text(encoding='utf-8')
    return json.loads(re.search(SCENE_BLOCK_PATTERN, text)[1])


def master(slug):
    return ROOT / slug / (slug.capitalize() + '.md')


class RemainingScenesTests(unittest.TestCase):
    def test_coverage_primitives_and_bounds(self):
        for slug, count in EXPECTED.items():
            source = master(slug).read_text(encoding='utf-8')
            briefs = re.findall(r'^> \[!abstract\] DIAGRAM (D\d+\.\d+) · ', source, re.M)
            manifest = json.loads((ROOT / slug / 'figures.json').read_text(encoding='utf-8'))
            self.assertEqual(len(manifest['drawings']), count, slug)
            self.assertEqual([d['id'] for d in manifest['drawings']], briefs, slug)
            for drawing in manifest['drawings']:
                data = scene(slug, drawing)
                self.assertEqual(data['type'], 'excalidraw')
                self.assertFalse(data['files'], f"{drawing['id']}: no embedded files")
                self.assertTrue(data['elements'], f"{drawing['id']}: empty scene")
                ids = [e['id'] for e in data['elements']]
                self.assertEqual(len(ids), len(set(ids)), f"{drawing['id']}: duplicate ids")
                for element in data['elements']:
                    self.assertIn(element['type'], PRIMITIVES, drawing['id'])
                    for key in ('x', 'y', 'width', 'height'):
                        self.assertTrue(math.isfinite(element[key]), f"{drawing['id']}: {key}")
                    self.assertGreaterEqual(element['y'], -1, f"{drawing['id']}: element above canvas")
                    self.assertRegex(element['strokeColor'], r'^(transparent|#[0-9a-fA-F]{3,8})$')

    def test_regeneration_is_deterministic(self):
        paths = []
        for slug in DRAW:
            paths.append(master(slug))
            paths.append(ROOT / slug / 'figures.json')
            paths += sorted((ROOT / '_obsidian' / 'excalidraw').glob(f'{slug}-*.excalidraw.md'))
        before = {p: hashlib.sha256(p.read_bytes()).digest() for p in paths}
        subprocess.run(['python3', str(ROOT / 'tools/build_excalidraw_remaining.py')],
                       check=True, capture_output=True)
        after = {p: hashlib.sha256(p.read_bytes()).digest() for p in paths}
        self.assertEqual(before, after)

    def test_original_briefs_and_provenance_preserved(self):
        ref = base_ref()
        for slug in DRAW:
            old = original_text(f'{slug}/{slug.capitalize()}.md', ref) or ''
            text = master(slug).read_text(encoding='utf-8')
            self.assertTrue(insert_only(old, text), f'{slug}: original master lines were rewritten')
            self.assertEqual(len(re.findall(COMPANION, text)), EXPECTED[slug], slug)
            original = json.loads(original_text(f'{slug}/figures.json', ref) or '{}')
            current = json.loads((ROOT / slug / 'figures.json').read_text(encoding='utf-8'))
            for key, value in original.items():
                self.assertEqual(current.get(key), value, f'{slug}: {key}')
            self.assertEqual(current['renderer'], 'obsidian-excalidraw-plugin@2.27.3')
            for drawing in current['drawings']:
                self.assertEqual(drawing['source'], f"{slug}/{slug.capitalize()}.md · {drawing['id']} brief")

    def test_sample_analytic_values(self):
        def rel_curve(slug, diagram_id, points):
            drawing = next(d for d in json.loads((ROOT / slug / 'figures.json').read_text())['drawings']
                           if d['id'] == diagram_id)
            return next(e for e in scene(slug, drawing)['elements']
                        if e['type'] == 'line' and len(e['points']) == points)

        # Shannon capacity, scaled by 1/10, is the top of the curve range; at 0 dB it is 0.1.
        curve = rel_curve('communication-systems', 'D100.10', 241)
        cap = lambda db: math.log2(1 + 10 ** (db / 10)) / 10
        index = round(240 * (0 - (-10)) / 50)
        self.assertAlmostEqual(curve['points'][index][1], 330 * (cap(40) - cap(0)), delta=0.05)
        self.assertAlmostEqual(curve['points'][-1][1], 0, places=3)

        # Allowed beta spectrum vanishes at both endpoints of the scaled axis.
        curve = rel_curve('nuclear-physics', 'D26.9', 241)
        self.assertAlmostEqual(curve['points'][0][1], curve['points'][-1][1], places=3)
        self.assertTrue(all(0 <= pt[1] <= 330 for pt in curve['points']))

        # Wien peaks move to shorter scaled wavelength as T rises.
        drawing = next(d for d in json.loads((ROOT / 'photoelectric-effect/figures.json').read_text())['drawings']
                       if d['id'] == 'D23.1')
        dots = [e for e in scene('photoelectric-effect', drawing)['elements']
                if e['type'] == 'ellipse' and e['backgroundColor'] in ('#2767a8', '#26865b', '#bd4b4b')]
        self.assertEqual([round(d['x']) for d in dots], sorted((round(d['x']) for d in dots), reverse=True))
        self.assertEqual(len({d['y'] for d in dots}), 1)

if __name__ == '__main__':
    unittest.main()

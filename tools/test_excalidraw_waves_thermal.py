"""Regression checks for the deterministic course-slot 13–15 companion batch."""
import json
import math
import re
import unittest
from pathlib import Path

from tools.build_excalidraw_waves_thermal import (
    ROOT, TOPICS, converted_scene, corrected_scene, css_rules, draw_style,
    matmul, matrix_for, path_polylines, point,
)
from tools.excalidraw_checks import validate_waves_thermal, SCENE_BLOCK_PATTERN
import xml.etree.ElementTree as ET


class WavesThermalTests(unittest.TestCase):
    def test_quadratic_reflection_and_relative_close(self):
        pts=path_polylines('M0 0 Q10 20 20 0 T40 0 l0 10 h-40 v-10 z')[0]
        self.assertIn((10,10),pts)
        self.assertIn((30,-10),pts)
        self.assertEqual(pts[0],pts[-1])

    def test_cubic_and_arc_endpoints(self):
        curves=path_polylines('M0 0 C0 10 10 10 10 0 M10 0 a10 10 0 0 1 10 10')
        self.assertEqual(curves[0][-1],(10,0))
        for a,b in zip(curves[1][-1],(20,10)):self.assertAlmostEqual(a,b)
        self.assertGreater(len(curves[1]),3)

    def test_nested_transform(self):
        m=matmul(matrix_for('translate(10,20)'),matrix_for('translate(3,4) scale(2,2)'))
        self.assertEqual(point(m,1,1),(15,26))

    def test_compound_css_and_external_theme_fallback(self):
        style=draw_style(ET.fromstring('<text class="lbl sm"/>'),{},
                         {},{'.lbl':{'font-size':'13px'},'.lbl.sm':{'font-size':'11px'}})
        self.assertEqual(style['font-size'],'11px')

    def test_all_scenes_and_reproducibility(self):
        for slug,(name,part) in TOPICS.items():
            with self.subTest(slug=slug):
                self.assertEqual(validate_waves_thermal(ROOT/slug),[])
                manifest=json.loads((ROOT/slug/'figures.json').read_text())
                for n,d in enumerate(manifest['drawings'],1):
                    p=ROOT/d['file'];data=json.loads(re.search(SCENE_BLOCK_PATTERN,p.read_text())[1])
                    fig=ROOT/slug/f'assets/figures/fig-{n:03d}.svg'
                    expected=corrected_scene(slug,fig,d['id']) or converted_scene(slug,fig,d['id'])
                    self.assertEqual(data,expected.json(),p.name)
                    self.assertTrue(any(e['type']=='text' for e in data['elements']))
                    self.assertFalse(data['files'])
                    for e in data['elements']:
                        self.assertFalse(e['locked'])
                        self.assertNotIn('var(',e['strokeColor'])
                        self.assertNotIn('url(',e['backgroundColor'])
                        for x,y in e.get('points',[]):self.assertTrue(math.isfinite(x) and math.isfinite(y))

    def test_validator_catches_missing_scene_embed(self):
        # The fixed counts prevent silently dropping a source figure or a brief.
        from tools.excalidraw_checks import validate_excalidraw
        root=ROOT/'string-waves';src=(root/'String-waves.md').read_text()
        src=re.sub(r'!\[\[[^\n]+excalidraw\|900\]\]','',src,count=1)
        self.assertTrue(validate_excalidraw(root,src,[('14',str(n)) for n in range(1,5)]))


if __name__=='__main__':unittest.main()

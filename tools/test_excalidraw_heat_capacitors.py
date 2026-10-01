"""Course slots 16–18: preserve sources, validate coverage and deterministic scenes."""
import hashlib
import json
import math
import re
import subprocess
import unittest
from pathlib import Path

from tools.build_excalidraw_heat_capacitors import (
    ROOT, TOPICS, converted_scene, corrected_scene, transform_matrix, point, colour,
)
from tools.excalidraw_checks import validate_svg_companions, SCENE_BLOCK_PATTERN


class HeatCapacitorTests(unittest.TestCase):
    def test_rotation_about_pivot_and_composition(self):
        m=transform_matrix('translate(10,20) rotate(90 2 3)')
        x,y=point(m,3,3)
        self.assertAlmostEqual(x,12);self.assertAlmostEqual(y,24)
        with self.assertRaises(ValueError):transform_matrix('skewX(20)')

    def test_colour_mix(self):
        self.assertEqual(colour('color-mix(in srgb,#000000 20%,#ffffff)'), '#cccccc')

    def test_all_scenes_match_builder(self):
        for slug,(name,part,count) in TOPICS.items():
            self.assertEqual(validate_svg_companions(ROOT/slug),[])
            manifest=json.loads((ROOT/slug/'figures.json').read_text())
            self.assertEqual(len(manifest['drawings']),count)
            for n,d in enumerate(manifest['drawings'],1):
                with self.subTest(slug=slug,n=n):
                    self.assertEqual(d['id'],f'D{part}.{n}')
                    text=(ROOT/d['file']).read_text()
                    data=json.loads(re.search(SCENE_BLOCK_PATTERN,text)[1])
                    fig=ROOT/slug/f'assets/figures/fig-{n:03d}.svg'
                    expected=corrected_scene(slug,fig,d['id']) or converted_scene(slug,fig,d['id'])
                    self.assertEqual(data,expected.json())
                    self.assertFalse(data['files'])
                    self.assertTrue(any(e['type']=='text' for e in data['elements']))
                    for e in data['elements']:
                        self.assertFalse(e['locked'])
                        self.assertIn(e['type'],('text','line','arrow','rectangle','ellipse'))
                        for key in ['x','y','width','height','angle']:
                            self.assertTrue(math.isfinite(e[key]))
                        self.assertGreaterEqual(e['width'],0);self.assertGreaterEqual(e['height'],0)
                        for color in [e['strokeColor'],e['backgroundColor']]:
                            self.assertRegex(color,r'^(transparent|#[0-9a-fA-F]{3,8})$')

    def test_generation_idempotent_and_electrostatics_untouched(self):
        paths=list((ROOT/'_obsidian/excalidraw').glob('*.excalidraw.md'))
        paths+=[ROOT/slug/name for slug,(name,_,_) in TOPICS.items()]
        paths+=[ROOT/slug/'figures.json' for slug in TOPICS]
        paths+=[ROOT/'electrostatics/Electrostatics.md',ROOT/'electrostatics/figures.json']
        before={p:hashlib.sha256(p.read_bytes()).digest() for p in paths}
        subprocess.run(['python3',str(ROOT/'tools/build_excalidraw_heat_capacitors.py')],check=True,capture_output=True)
        self.assertEqual(before,{p:hashlib.sha256(p.read_bytes()).digest() for p in paths})

    def test_rotated_labels_and_native_polygons(self):
        scene=converted_scene('capacitors',ROOT/'capacitors/assets/figures/fig-015.svg','test')
        labels=[e for e in scene.elements if e['type']=='text' and abs(e['angle'])>1]
        self.assertEqual(len(labels),2)
        for label in labels:self.assertAlmostEqual(abs(label['angle']),math.pi/2)
        scene=converted_scene('heat',ROOT/'heat/assets/figures/fig-003.svg','test')
        polygons=[e for e in scene.elements if e['type']=='line' and len(e['points'])==4 and e['points'][0]==e['points'][-1]]
        self.assertEqual(len(polygons),11)

    def test_analytic_coordinates(self):
        s=corrected_scene('capacitors',Path('fig-011.svg'),'test')
        curves=[e for e in s.elements if e['type']=='line' and len(e['points'])==241]
        self.assertEqual(len(curves),2)
        # The pull-in tangency at g/g0=2/3 has F/(kg0)=1/3.
        dots=[e for e in s.elements if e['type']=='ellipse']
        self.assertAlmostEqual(dots[0]['y']+dots[0]['height']/2,400)
        # The entire force plot stays below the header.
        for e in curves:self.assertGreater(e['y'],140)
        for slug,n in [('heat',16),('capacitors',24)]:
            s=corrected_scene(slug,Path(f'fig-{n:03d}.svg'),'test')
            decay=next(e for e in s.elements if e['type']=='line' and len(e['points'])==241)
            self.assertAlmostEqual(decay['y']+decay['points'][-1][1],510-330*math.exp(-5),places=2)


if __name__=='__main__':unittest.main()

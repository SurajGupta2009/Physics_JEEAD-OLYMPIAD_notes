"""Course slots 22–24: native coverage, source preservation and analytical checks."""
import hashlib,json,math,re,subprocess,unittest
from tools.build_excalidraw_em_optics import ROOT,TOPICS,companion,corrected_scene
from tools.excalidraw_checks import validate_svg_companions,SCENE_BLOCK_PATTERN

class EMOpticsTests(unittest.TestCase):
    def test_coverage_and_builder(self):
        for slug,(name,part,count) in TOPICS.items():
            self.assertEqual(validate_svg_companions(ROOT/slug),[])
            manifest=json.loads((ROOT/slug/'figures.json').read_text())
            self.assertEqual(len(manifest['drawings']),count)
            for n,d in enumerate(manifest['drawings'],1):
                self.assertEqual(d['id'],f'D{part}.{n}')
                data=json.loads(re.search(SCENE_BLOCK_PATTERN,(ROOT/d['file']).read_text())[1])
                self.assertEqual(data,companion(slug,ROOT/slug/f'assets/figures/fig-{n:03d}.svg',d['id']).json())
                self.assertFalse(data['files'])
                for e in data['elements']:
                    self.assertFalse(e['locked'])
                    self.assertIn(e['type'],['text','line','arrow','rectangle','ellipse'])
                    for k in ['x','y','width','height','angle']:self.assertTrue(math.isfinite(e[k]))
                    for c in ['strokeColor','backgroundColor']:self.assertRegex(e[c],r'^(transparent|#[0-9a-fA-F]{3,8})$')

    def test_idempotence_and_prior_scenes_untouched(self):
        paths=list((ROOT/'_obsidian/excalidraw').glob('*.excalidraw.md'))
        paths += [ROOT/s/p for s,(name,_,_) in TOPICS.items() for p in [name,'figures.json']]
        before={p:hashlib.sha256(p.read_bytes()).digest() for p in paths}
        subprocess.run(['python3',str(ROOT/'tools/build_excalidraw_em_optics.py')],check=True,capture_output=True)
        self.assertEqual(before,{p:hashlib.sha256(p.read_bytes()).digest() for p in paths})

    def test_originals_preserved(self):
        from tools.excalidraw_additions import base_ref, insert_only, original_text
        ref=base_ref()
        for slug,(name,part,_) in TOPICS.items():
            old=original_text(f'{slug}/{name}',ref) or ''
            text=(ROOT/slug/name).read_text()
            self.assertTrue(insert_only(old,text),f'{slug}: original master lines were rewritten')
            original=json.loads(original_text(f'{slug}/figures.json',ref) or '{}')
            self.assertEqual(original['figures'],json.loads((ROOT/slug/'figures.json').read_text())['figures'])
            diff=subprocess.run(['git','diff','--quiet',ref or 'HEAD','--',f'{slug}/assets'],
                                cwd=ROOT,capture_output=True)
            self.assertEqual(diff.returncode,0,f'{slug}: source assets changed')

    def test_analytic_curves(self):
        from pathlib import Path
        s=corrected_scene('wave-optics',Path('fig-015.svg'),'test')
        curve=next(e for e in s.elements if e['type']=='line' and len(e['points'])==241)
        # λ=λ₀ is at sample 80: reflectance is zero, bottom axis y=570.
        self.assertAlmostEqual(curve['y']+curve['points'][80][1],570)
        s=corrected_scene('wave-optics',Path('fig-011.svg'),'test')
        curves=[e for e in s.elements if e['type']=='line' and len(e['points'])==481]
        self.assertEqual(len(curves),2)
        self.assertAlmostEqual(curves[0]['y']+curves[0]['points'][60][1],570)
        self.assertAlmostEqual(curves[1]['y']+curves[1]['points'][60][1],570-330/9,places=3)
        s=corrected_scene('geometrical-optics',Path('fig-043.svg'),'test')
        # Test exact reflected rays instead of relying on colour constants.
        rays=[e for e in s.elements if e['type']=='arrow' and e['points'][-1][1]>0]
        self.assertEqual(len(rays),3)
        for h,e in zip([2,4,6],rays):
            xp=e['x']+e['points'][-1][0]
            self.assertAlmostEqual((1100-xp)/35,20-400/(2*math.sqrt(400-h*h)),places=3)

if __name__=='__main__':unittest.main()

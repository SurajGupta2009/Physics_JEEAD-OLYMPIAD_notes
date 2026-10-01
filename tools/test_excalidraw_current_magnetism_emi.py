"""Coverage, determinism and preservation for course slots 19–21."""
import hashlib,json,re,subprocess,unittest
from tools.build_excalidraw_current_magnetism_emi import ROOT,TOPICS
from tools.excalidraw_checks import validate_svg_companions,validate_excalidraw,SCENE_BLOCK_PATTERN,EMBED_PATTERN

class CurrentMagnetismInductionTests(unittest.TestCase):
    def test_coverage(self):
        for slug,(name,part,count) in TOPICS.items():
            text=(ROOT/slug/name).read_text()
            manifest=json.loads((ROOT/slug/'figures.json').read_text())
            self.assertEqual(len(manifest['drawings']),count)
            if slug=='current-electricity':self.assertEqual(validate_svg_companions(ROOT/slug),[])
            else:self.assertEqual(validate_excalidraw(ROOT/slug,text,[(str(part),str(n)) for n in range(1,count+1)]),[])
            for d in manifest['drawings']:
                data=json.loads(re.search(SCENE_BLOCK_PATTERN,(ROOT/d['file']).read_text())[1])
                self.assertFalse(data['files'])
                self.assertTrue(data['elements'])
                for e in data['elements']:
                    self.assertFalse(e['locked'])
                    self.assertIn(e['type'],['text','line','arrow','rectangle','ellipse'])

    def test_idempotent(self):
        paths=list((ROOT/'_obsidian/excalidraw').glob('*.excalidraw.md'))
        paths += [ROOT/s/p for s,(name,_,_) in TOPICS.items() for p in [name,'figures.json']]
        before={p:hashlib.sha256(p.read_bytes()).digest() for p in paths}
        subprocess.run(['python3',str(ROOT/'tools/build_excalidraw_current_magnetism_emi.py')],check=True,capture_output=True)
        self.assertEqual(before,{p:hashlib.sha256(p.read_bytes()).digest() for p in paths})

    def test_original_master_preservation(self):
        from tools.excalidraw_additions import base_ref, insert_only, original_text
        ref=base_ref()
        for slug,(name,_,_) in TOPICS.items():
            old=original_text(f'{slug}/{name}',ref) or ''
            text=(ROOT/slug/name).read_text()
            self.assertTrue(insert_only(old,text),f'{slug}: original master lines were rewritten')

if __name__=='__main__':unittest.main()

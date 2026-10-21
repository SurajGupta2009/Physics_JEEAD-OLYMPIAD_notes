"""Editable content for the elasticity short notes -> writes sheets.json.

Run:  python author_content.py
Part I (JEE) and Part II (Olympiad) are numbered independently.
"""
from pathlib import Path
import json
exec((Path(__file__).parent/'_content_jee.py').read_text())
exec((Path(__file__).parent/'_content_oly.py').read_text())

def finish():
    counts={'JEE':0,'Olympiad':0}
    for p in DATA:
        counts[p['section']]+=1
        p['part_page']=counts[p['section']]
        p['part_total']=None
        assert len(p['cards'])==4, p['slug']
        for c in p['cards']:
            kinds={k for k,_ in c['items']}
            assert 'why' in kinds and 'trap' in kinds, c['title']
    for p in DATA: p['part_total']=counts[p['section']]
    order={'JEE':0,'Olympiad':1}
    DATA.sort(key=lambda p:(order[p['section']],p['part_page']))
    (Path(__file__).parent/'sheets.json').write_text(json.dumps(DATA,indent=2,ensure_ascii=False)+'\n')
    print(f"{counts['JEE']} JEE sheets, {counts['Olympiad']} extension sheets, {len(DATA)} total")

if __name__=='__main__': finish()

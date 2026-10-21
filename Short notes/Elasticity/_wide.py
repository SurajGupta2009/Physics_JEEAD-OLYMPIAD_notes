import json
from pathlib import Path
import render_sheets as R
D=json.loads(Path('sheets.json').read_text())
for p in D:
    for c in p['cards']:
        for k,s in c['items']:
            if k!='m': continue
            a=R.math_image(s); w=1090-64
            if a.width>w:
                ratio=w/a.width
                if ratio<0.82:
                    print(f'{ratio:.2f} {p["slug"]:32s} {s}')

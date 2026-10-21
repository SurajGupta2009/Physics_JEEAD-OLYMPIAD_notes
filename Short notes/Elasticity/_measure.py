"""Report the rendered height of every card, without writing any image."""
import json,sys
from pathlib import Path
import render_sheets as R
from PIL import Image, ImageDraw
DATA=json.loads((Path(__file__).parent/'sheets.json').read_text())
def height(c,width=1090):
    yy=106; bodyw=width-64; d=ImageDraw.Draw(Image.new('RGB',(1,1)))
    for kind,s in c['items']:
        if kind=='m':
            a=R.math_image(s)
            if a.width>bodyw:
                ratio=bodyw/a.width
                a=a.resize((bodyw,round(a.height*ratio)),Image.Resampling.LANCZOS)
            yy+=a.height+24
        else:
            fs=46 if kind in ('why','trap') else 48
            lead=53 if kind in ('why','trap') else 56
            label='WHY / ' if kind=='why' else 'WATCH / ' if kind=='trap' else ''
            f=R.font(fs)
            yy+=lead*len(R.lines_for(label+s,f,bodyw))+10
    return yy
rows=[]
for p in DATA:
    for c in p['cards']:
        rows.append((height(c),p['slug'],c['title']))
rows.sort(reverse=True)
for h,slug,title in rows[:14]:
    print(f'{h:5d}  {slug:34s} {title}')
print('limit 1038 (1050-12)')

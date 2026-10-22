import sys, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image, ImageChops, ImageDraw, ImageFont
from layout import DPI, W, M, CARRY_Y, FIG_MIN_Y
import diagrams
width = W - 2*M; height = CARRY_Y - 24 - FIG_MIN_Y
tiles=[]
for key in sys.argv[1:]:
    fig = plt.figure(figsize=(width/DPI,(height-78)/DPI), dpi=DPI, facecolor='white')
    ax = fig.add_axes([.03,.05,.94,.84]); ax.axis('off')
    diagrams.figure(ax,key)
    fig.canvas.draw()
    im = Image.frombytes('RGBA', fig.canvas.get_width_height(), fig.canvas.buffer_rgba()).convert('RGB')
    plt.close(fig)
    bg = Image.new('RGB', im.size, 'white')
    bbox = ImageChops.difference(im, bg).convert('L').point(lambda p: 255 if p>12 else 0).getbbox()
    im = im.crop(bbox) if bbox else im
    im.thumbnail((1500, 640), Image.Resampling.LANCZOS)
    tiles.append((key, im))
w = max(t[1].width for t in tiles); h = max(t[1].height for t in tiles)
cols=2; rows=(len(tiles)+1)//2
sheet = Image.new('RGB', (cols*w, rows*(h+32)), (244,244,244))
d = ImageDraw.Draw(sheet)
for i,(k,im) in enumerate(tiles):
    x,y = (i%cols)*w, (i//cols)*(h+32)
    sheet.paste(im,(x,y+32)); d.text((x+6,y+6), k, font=ImageFont.load_default(size=24), fill=(190,30,30))
    d.rectangle((x,y+32,x+im.width,y+32+im.height), outline=(210,210,210))
sheet.save('/tmp/probe_sheet.png'); print(sheet.size, len(tiles))

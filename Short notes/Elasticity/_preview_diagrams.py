import sys, io
from pathlib import Path
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image
sys.path.insert(0,str(Path(__file__).resolve().parent))
from diagrams import figure
OUT=Path(__file__).resolve().parent/'_preview'; OUT.mkdir(exist_ok=True)
keys=sys.argv[1:] or [k for k in ['stress_modes','stress_strain','stress_strain_zoom','modulus_bar','poisson_wire','poisson_bounds','series_composite','parallel_wires','hanger_angle','self_weight','sag_wire','thermal_stress']]
for key in keys:
    fig=plt.figure(figsize=(1090/300,535/300),dpi=300,facecolor='white')
    ax=fig.add_axes([.23,.34,.72,.55]); cap=figure(ax,key)
    if not ax.axison: ax.set_position([.035,.08,.93,.80])
    fig.canvas.draw(); r=fig.canvas.get_renderer()
    bad=[]
    for a in ax.texts+[ax.xaxis.label,ax.yaxis.label]:
        if not a.get_visible() or not a.get_text(): continue
        bb=a.get_window_extent(r)
        if bb.x0<-1 or bb.y0<-1 or bb.x1>1091 or bb.y1>536: bad.append((a.get_text(),(round(bb.x0),round(bb.y0),round(bb.x1),round(bb.y1))))
    print(key,'caption:',cap,'| clipped:',bad)
    b=io.BytesIO(); fig.savefig(b,format='png',dpi=300); plt.close(fig)
    (OUT/(key+'.png')).write_bytes(b.getvalue())
# contact sheet of all preview files
files=[OUT/(k+'.png') for k in keys]
ims=[Image.open(f).convert('RGB').resize((545,268)) for f in files]
cols=2; rows=(len(ims)+1)//2
sheet=Image.new('RGB',(cols*545,rows*300),'white')
for i,im in enumerate(ims): sheet.paste(im,((i%cols)*545,(i//cols)*300))
sheet.save(OUT/'contact.png')
print('contact',sheet.size)

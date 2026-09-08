#!/usr/bin/env python3
"""Normalise math markup in the notes (idempotent).
 - <m(...)  <m\\cmd  <m=  ->  <m>          (typo repair)
 - <m word  ->  <m>word                   (typo repair)
 - collapse newlines inside <m>…</m>       (the renderer is fine but the source reads better)
 - ensure every <m> is closed on the same line
Run: python3 tools/mathfix.py
"""
import re, glob, sys
changed=[]
for f in glob.glob('*.html'):
    s=open(f, encoding='utf-8').read(); o=s
    s=re.sub(r'<m(?=[(\\=!])', '<m>', s)
    s=re.sub(r'<m (?=[A-Za-z\\])', '<m>', s)
    s=re.sub(r'<m>([^<]*?)</m>', lambda m:'<m>'+re.sub(r'\s*\n\s*',' ',m.group(1))+'</m>', s, flags=re.S)
    # unbalanced <m> on a line: report
    for i,l in enumerate(s.split('\n'),1):
        if len(re.findall(r'<m>',l))!=len(re.findall(r'</m>',l)) and 'eqd' not in l:
            print(f'  ! {f}:{i} unbalanced <m> (needs a manual look)')
    if s!=o:
        open(f,'w',encoding='utf-8').write(s); changed.append(f)
print('rewrote:', ', '.join(changed) if changed else 'nothing')

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
    s=re.sub(r'<m([A-Za-z])(?=</m>)', r'<m>\1', s)  # <mA</m> -> <m>A</m>
    s=re.sub(r'<m(?=[^\sA-Za-z>/])', '<m>', s)      # <m\x, <m1, <m(, <m=, <m- …
    s=re.sub(r'<m (?=[A-Za-z\\0-9])', '<m>', s)      # <m \kappa, <m Q_1 …
    s=re.sub(r'<m>\s*\\([EDPF])(?![a-zA-Z])', r'<m>\\vec \1', s)   # \E -> \vec E etc.
    s=re.sub(r'(<m>[^<]*?)\\([EDPF])(?![a-zA-Z])', lambda m: m.group(1)+r'\vec '+m.group(2), s)
    s=re.sub(r'<m>([^<]*?)</m>', lambda m:'<m>'+re.sub(r'\s*\n\s*',' ',m.group(1))+'</m>', s, flags=re.S)
    # unbalanced <m> on a line: report
    for i,l in enumerate(s.split('\n'),1):
        if len(re.findall(r'<m>',l))!=len(re.findall(r'</m>',l)) and 'eqd' not in l:
            print(f'  ! {f}:{i} unbalanced <m> (needs a manual look)')
    if s!=o:
        open(f,'w',encoding='utf-8').write(s); changed.append(f)
print('rewrote:', ', '.join(changed) if changed else 'nothing')

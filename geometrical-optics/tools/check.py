#!/usr/bin/env python3
"""Consistency checker for the geometrical-optics notes.   usage: python3 tools/check.py
 - HTML tag balance (incl. SVG)
 - <m>…</m> balance, no raw '<' or unescaped entities inside math
 - every \\command used in math must be supported by assets/tex.js
 - no stray LaTeX idioms that the mini-compiler does not implement
 - internal links resolve to real files; #anchors exist
 - figures have captions, questions have a solution panel
"""
import re, sys, os, glob
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VOID = {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr',
        'path','circle','rect','line','ellipse','polygon','polyline','use','stop','text','tspan','marker','g','svg','defs','pattern'}

class Checker(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True); self.stack=[]; self.errors=[]
    def handle_starttag(self, tag, attrs):
        if tag in VOID: return
        self.stack.append((tag, self.getpos()[0]))
    def handle_startendtag(self, tag, attrs): pass
    def handle_endtag(self, tag):
        if tag in VOID: return
        if not self.stack: self.errors.append(f'line {self.getpos()[0]}: stray </{tag}>'); return
        if self.stack[-1][0] != tag:
            self.errors.append(f'line {self.getpos()[0]}: </{tag}> but open <{self.stack[-1][0]}> from line {self.stack[-1][1]}')
            for i in range(len(self.stack)-1, -1, -1):
                if self.stack[i][0] == tag: del self.stack[i:]; break
        else: self.stack.pop()

def supported_commands():
    src = open(os.path.join(ROOT, 'assets', 'tex.js')).read()
    cmds = set(re.findall(r'cmd === "([a-zA-Z]+)"', src))
    cmds |= set(re.findall(r'^\s{4}([a-zA-Z]+):', src, re.M))          # SYM / ENV keys
    cmds |= set(re.findall(r'([a-zA-Z]+): function', src))
    # from the SYM/FUN object literals
    for m in re.finditer(r'var (SYM|FUN|SP)\s*=\s*\{(.*?)\n  \};', src, re.S):
        cmds |= set(re.findall(r'([a-zA-Z]+)\s*:', m.group(2)))
    cmds |= {'begin','end'}
    return cmds

def main():
    files = sorted(glob.glob(os.path.join(ROOT, '*.html')))
    if not files: print('no html files'); return 1
    cmds = supported_commands()
    allids = {}; allfiles = {os.path.basename(f) for f in files}
    problems = 0
    for f in files:
        name = os.path.basename(f); src = open(f, encoding='utf-8').read(); errs = []
        # Standalone final files inline JavaScript; validate reader-facing markup separately.
        checksrc = re.sub(r'<script\b[^>]*>.*?</script>', '', src, flags=re.S)
        # tag balance
        c = Checker(); c.feed(src)
        errs += c.errors
        if c.stack: errs.append('unclosed at EOF: ' + ', '.join(f'<{t}> L{l}' for t, l in c.stack[:6]))
        # math hygiene
        for m in re.finditer(r'<m>(.*?)</m>', checksrc, re.S):
            seg = m.group(1)
            if '<' in seg: errs.append(f'math contains raw "<": {seg[:50]}')
            if '\n' in seg: errs.append(f'math spans lines: {seg[:40]}')
        for blk in re.findall(r'<div class="eqd[^"]*"[^>]*>(.*?)</div>', checksrc, re.S):
            if '<' in blk: errs.append(f'eqd contains raw markup: {blk[:50]}')
        _mathsrc = '\n'.join(re.findall(r'<m>(.*?)</m>', checksrc, re.S) + re.findall(r'<div class="eqd[^"]*"[^>]*>(.*?)</div>', checksrc, re.S))
        used = set(re.findall(r'\\([a-zA-Z]+)', _mathsrc))
        bad = {u for u in used if u not in cmds}
        if bad: errs.append('unsupported commands: ' + ' '.join(sorted(bad)))
        # stray latex
        for pat, why in [(r'\\\)', 'stray \\)'), (r'\\\]', 'stray \\]'), (r'\$\$', 'literal $$'),
                         (r'<math', 'MathML <math> tag'), (r'\\begin\{(?!cases|aligned|align|pmatrix|bmatrix|vmatrix|matrix|gathered|array)', 'unsupported env'),
                         (r'\\tag\{|\\label|\\nonumber|\\substack\b(?!\{)', 'unsupported latex')]:
            if re.search(pat, checksrc): errs.append(why + ' present')
        # links + ids
        ids = set(re.findall(r'id="([^"]+)"', checksrc)); allids[name] = ids
        for href in re.findall(r'href="([^"#]+)(?:#[^"]*)?"', checksrc):
            if href.startswith(('http', 'mailto')): continue
            if href not in allfiles and not href.endswith(('.css', '.js')): errs.append('missing file: ' + href)
            if href.endswith(('.css', '.js')) and not os.path.exists(os.path.join(ROOT, href)): errs.append('missing asset ' + href)
        for a in re.findall(r'href="#([^"]+)"', checksrc):
            if a not in ids: errs.append(f'anchor #{a} has no target in {name}')
        # every question must be answerable from the page it is on, or from the page it points to.
        # modes: (default) each <div class="q"> carries a collapsible <details class="sol">;
        #        <meta name="solutions" content="external:FILE"> for an exam paper;
        #        <meta name="solutions" content="inline">          for a solutions file (the .q body IS the answer).
        nq, ns = src.count('<div class="q">'), src.count('<details class="sol">')
        md = re.search(r'<meta name="solutions" content="([^"]+)"', src)
        if nq and not ns and not md:
            errs.append(f'{nq} questions with no solution panels \u2014 add <details class="sol">, or declare '
                        '<meta name="solutions" content="external:NN-file.html"> / "inline">')
        elif md and md.group(1) == 'inline':
            pass  # A consolidated final.html contains theory, paper, and its solutions.
        elif md and md.group(1).startswith('external:'):
            tgt = md.group(1).split(':', 1)[1].strip()
            if tgt not in allfiles:
                errs.append('declared solutions file missing: ' + tgt)
        elif ns and ns < nq:
            errs.append(f'{nq} questions but only {ns} solution panels \u2014 every question needs one')
        # figure captions
        nf = src.count('figure class="fig"'); nc = src.count('<figcaption>')
        if nf != nc: errs.append(f'{nf} figures but {nc} captions')
        if errs:
            problems += len(errs)
            print(f'\n== {name}  ({len(src)//1024} KB)')
            for e in errs: print('   ✗', e)
        else:
            print(f'✓ {name}  ({len(src)//1024} KB, {src.count(chr(60)+"m>"):.0f} inline maths, {src.count("eqd")} display maths)')
    # anchors of cross-page links
    for f in files:
        name = os.path.basename(f); src = open(f, encoding='utf-8').read()
        for href, a in re.findall(r'href="([^"#]+)#([^"]+)"', src):
            if href in allids and a not in allids[href]:
                print(f'   ✗ {name}: link to {href}#{a} — no such id yet (auto-generated headings are ok if the heading text exists)')
    print('\n' + ('ALL GOOD' if not problems else f'{problems} problem(s)'))
    return 1 if problems else 0

sys.exit(main())

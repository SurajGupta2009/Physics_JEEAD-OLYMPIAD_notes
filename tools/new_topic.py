#!/usr/bin/env python3
"""Scaffold a new note-set (topic) so it follows the house structure by construction.

    python3 tools/new_topic.py thermodynamics --title "Thermodynamics" --chapters "01-temperature,02-first-law,03-entropy"
    python3 tools/new_topic.py optics --title "Optics"                  # one example chapter, add the rest yourself

What it does, in order:
  1. copies assets/ (notes.css, tex.js, notes.js) and tools/ (check.py, mathfix.py, setpages.py,
     test-tex.js) from a donor topic \u2014 a new topic is self-contained, so it renders and prints offline
     and can be validated without touching anyone else's files
  2. writes index.html (front page with chapter cards) and README.md for the folder
  3. writes each chapter from _templates/chapter.html with the placeholders filled
  4. regenerates assets/pages.js, adds the topic to topics.json (owner = you), runs the checks
Nothing existing is overwritten; the script refuses if the folder already has pages.
"""
import argparse, json, os, re, shutil, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REG = os.path.join(ROOT, 'topics.json')
TPL = os.path.join(ROOT, '_templates', 'chapter.html')


def read(p):
    return open(p, encoding='utf-8').read()


def write(p, s):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8').write(s)


def title_of(fname):
    m = re.search(r'<title>(.*?)</title>', read(fname), re.S)
    return m.group(1) if m else os.path.basename(fname)


def index_page(topic, chapters):
    cards = []
    for i, (num, slug) in enumerate(chapters):
        label = slug.replace('-', ' ')
        cards.append(
            '    <li class="card" data-chk="{n:02d}">\n'
            '      <span class="n">Chapter {n}</span>\n'
            '      <b><a class="go" href="{n:02d}-{slug}.html">{label}</a></b>\n'
            '      <p>{{what the reader can do after this chapter \u2014 one sentence, no "covers".}}</p>\n'
            '      <span class="st">\u2192</span>\n'
            '    </li>'.format(n=num, slug=slug, label=label.title()))
    return ('<!DOCTYPE html>\n<html lang="en" data-theme="light">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            '<title>{t} — JEE Advanced &amp; Physics Olympiad notes</title>\n'
            '<meta name="description" content="{t} notes for JEE Advanced and the physics olympiad track, from first principles to Olympiad level.">\n'
            '<link rel="stylesheet" href="assets/notes.css">\n'
            '<script src="assets/tex.js" defer></script>\n'
            '<script src="assets/pages.js" defer></script>\n'
            '<script src="assets/notes.js" defer></script>\n</head>\n<body>\n<div class="shell">\n'
            '<nav class="toc" id="toc" aria-label="Contents"><p class="lab">Contents</p></nav>\n<main>\n'
            '<p class="meta" id="top"><span class="badges"><span class="b j">JEE Advanced</span>'
            '<span class="b o">INPhO / IPhO</span><span class="b n">{k} chapters</span></span></p>\n'
            '<h1>{t}</h1>\n<p class="lead">{{One paragraph: what this set is for, what it assumes, and in what order '
            'to read it. Say plainly which chapters are JEE-only and which are Olympiad-only.}}</p>\n'
            '<h2>Chapters</h2>\n<ol class="cards">\n{cards}\n</ol>\n'
            '<div class="box thm"><p class="bt">Exam note</p><p>{{Which exam, which syllabus lines, and where the '
            'overlap is.}}</p></div>\n'
            '<p class="skip">Start with <a href="01-{f0}.html"><b>Chapter 1 \u2192</b></a>.</p>\n'
            '</main>\n</div>\n</body>\n</html>\n').format(t=topic, k=len(chapters), cards='\n'.join(cards),
                                                          f0=chapters[0][1])


def folder_readme(topic, chapters):
    rows = '\n'.join('| `%02d-%s.html` | {{title}} | {{status}} |' % (n, s) for n, s in chapters)
    return ('# %s notes\n\n'
            'Part of [Physics_JEEAD-OLYMPIAD_notes](../README.md) \u2014 self-contained HTML notes, no build step,\n'
            'no network. Open `index.html` to read; run `python3 -m http.server 8000` here for the interactive bits\n'
            '(theme, progress, TOC).\n\n'
            '| file | covers | status |\n|---|---|---|\n%s\n\n'
            '## Editing\n\n'
            '```bash\npython3 tools/mathfix.py      # normalise authoring slips (idempotent)\n'
            'python3 tools/setpages.py     # page order = filenames (run after adding/renaming a file)\n'
            'python3 tools/check.py        # ALL GOOD or a list of problems\n```\n\n'
            '## Deliberately not covered\n\n'
            '{{List what you chose *not* to write, so nobody else spends a week duplicating it.}}\n'
            % (topic, rows))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('slug', help='folder name, lowercase-kebab')
    ap.add_argument('--title', default=None, help='display name (defaults to the slug, title-cased)')
    ap.add_argument('--donor', default='capacitors', help='topic to copy assets/tools from')
    ap.add_argument('--chapters', default='', help='comma-separated "01-name,02-name" (NN- prefix required)')
    ap.add_argument('--owner', default=os.environ.get('USER', 'unnamed'), help='who is writing it (recorded in topics.json)')
    a = ap.parse_args()

    dst = os.path.join(ROOT, a.slug)
    donor = os.path.join(ROOT, a.donor)
    if not os.path.isdir(donor):
        sys.exit('donor topic %r not found' % a.donor)
    if os.path.isdir(dst) and glob_html(dst):
        sys.exit('%s already has pages \u2014 refusing to overwrite. Edit it directly.' % a.slug)

    ch = []
    for c in [x for x in a.chapters.split(',') if x.strip()]:
        m = re.match(r'^(\d{2})-([a-z0-9][a-z0-9-]*)$', c.strip())
        if not m:
            sys.exit('chapter %r must look like 01-some-title' % c)
        ch.append((int(m.group(1)), m.group(2)))
    if not ch:
        ch = [(1, 'foundations')]
    os.makedirs(dst, exist_ok=True)

    for sub in ('assets', 'tools'):
        os.makedirs(os.path.join(dst, sub), exist_ok=True)
        for f in sorted(os.listdir(os.path.join(donor, sub))):
            shutil.copy2(os.path.join(donor, sub, f), os.path.join(dst, sub, f))
    tpl = read(TPL)
    ch = sorted(ch)
    for j, (n, slug) in enumerate(ch):
        nxt = ('%02d-%s.html' % ch[j + 1]) if j + 1 < len(ch) else 'index.html'
        nxtlab = ('Chapter %d \u00b7 %s' % (ch[j + 1][0], ch[j + 1][1].replace('-', ' ').title())
                  if j + 1 < len(ch) else 'Back to the front page')
        out = (tpl.replace('{{NN}}', str(n)).replace('{{TOPIC}}', a.title or a.slug.title())
                  .replace('{{TITLE}}', slug.replace('-', ' ').title())
                  .replace('{{LEADONESENTENCE}}', 'To be written: one sentence for the <meta description>.')
                  .replace('{{NEXTFILE}}', nxt).replace('{{NEXTLABEL}}', nxtlab))
        write(os.path.join(dst, '%02d-%s.html' % (n, slug)), out)
    write(os.path.join(dst, 'index.html'), index_page(a.title or a.slug.title(), ch))
    write(os.path.join(dst, 'README.md'), folder_readme(a.title or a.slug.title(), ch))

    subprocess.run([sys.executable, 'tools/setpages.py'], cwd=dst, check=True, capture_output=True)
    reg = json.loads(read(REG))
    if not any(t['slug'] == a.slug for t in reg['topics']):
        reg['topics'].append({'slug': a.slug, 'title': a.title or a.slug.title(), 'status': 'in-progress',
                              'owner': a.owner, 'entry': '%s/index.html' % a.slug,
                              'exam': ['JEE Advanced', 'NSEP', 'INPhO'],
                              'figures': 0, 'questions': 0, 'solutions': 0, 'math_spans': 0,
                              'bytes_html': 0, 'pages': []})
        write(REG, json.dumps(reg, indent=2, ensure_ascii=False) + '\n')
        print('registered %s in topics.json (owner=%s)' % (a.slug, a.owner))
    subprocess.run([sys.executable, 'tools/check_all.py', '--update', a.slug], cwd=ROOT)
    print('\ncreated %s/' % a.slug)
    for p in sorted(glob_html(dst)) + ['assets/', 'tools/', 'README.md']:
        print('   ', p)
    print('\nnext: fill the placeholders (grep -n "{{" %s/*.html), then run\n'
          '    python3 tools/check_all.py %s' % (a.slug, a.slug))


def glob_html(d):
    import glob
    return glob.glob(os.path.join(d, '*.html'))


if __name__ == '__main__':
    main()

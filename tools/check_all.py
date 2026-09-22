#!/usr/bin/env python3
"""The repo-wide quality gate.   Run this before every commit, and after every merge.

    python3 tools/check_all.py              # check every registered topic
    python3 tools/check_all.py capacitors    # check one topic
    python3 tools/check_all.py --update      # recount the registry from the files, then check
    python3 tools/check_all.py --quick        # skip the node unit tests

Checks, per topic:
  1. the folder is registered in topics.json, and every *.html in it is listed there (no orphans,
     no phantom pages)
  2. assets/pages.js is in sync with the folder (tools/setpages.py --check)
  3. the topic's own validator passes (tools/check.py: markup, math, links, anchors, figures)
  4. the math renderer's unit tests pass (node tools/test-tex.js) when node is installed
  Markdown-first entries use their required local check.py and count only their master
  (including source words and display formulas); print extracts are excluded.
  5. the mechanical counts in topics.json (figures, questions, solutions, math, bytes) match disk

Exit code is non-zero if anything fails, so it works as a pre-commit hook or CI step.
"""
import json, os, re, subprocess, sys, glob, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REG = os.path.join(ROOT, 'topics.json')


def load():
    return json.load(open(REG, encoding='utf-8'))


def save(data):
    with open(REG, 'w', encoding='utf-8') as fh:
        json.dump(data, fh, indent=2, ensure_ascii=False)
        fh.write('\n')


def read(p):
    with open(p, encoding='utf-8') as fh:
        return fh.read()


def count(topic_dir, entry=None):
    """The only trustworthy source for the registry numbers: the markup itself."""
    # Markdown-first work packages (plan.md) count only their authoritative entry,
    # never the generated paper/solution extracts. Existing HTML counts are unchanged.
    if entry and entry.endswith('.md'):
        name = os.path.basename(entry)
        path = os.path.join(topic_dir, name)
        source = read(path)
        displays = re.findall(r'\$\$(.*?)\$\$', source, re.S)
        inline_source = re.sub(r'\$\$.*?\$\$', '', source, flags=re.S)
        inline = re.findall(r'(?<![\\$])\$(?!\$)([^\n]*?)(?<!\\)\$(?!\$)', inline_source)
        questions = re.findall(r'^\*\*C\d+ —|^### E\d+ —|^#### Q\d+\.', source, re.M)
        return dict(pages=[name], figures=len(re.findall(r'!\[[^\]]+\]\(assets/figures/[^)]+\)', source)),
                    questions=len(questions), solutions=source.count('<details>'),
                    math_spans=len(inline) + len(displays), bytes_html=0,
                    bytes_markdown=os.path.getsize(path), words=len(source.split()),
                    display_formulas=len(displays))
    files = sorted(glob.glob(os.path.join(topic_dir, '*.html')))
    figs = qs = sols = maths = size = 0
    for f in files:
        s = read(f)
        figs += s.count('<figure class="fig">')
        qs += s.count('<div class="q">')
        sols += s.count('<details class="sol">')
        maths += len(re.findall(r'<m>', s))
        size += os.path.getsize(f)
    # reading order, not alphabetical: pages.js is the generated navigation, so it is the record
    nav = os.path.join(topic_dir, 'assets', 'pages.js')
    order = re.findall(r'\["([^"]+\.html)"', read(nav)) if os.path.exists(nav) else []
    pages = [p for p in order if p in [os.path.basename(f) for f in files]] or \
            [os.path.basename(f) for f in files]
    return dict(pages=pages, figures=figs, questions=qs,
                solutions=sols, math_spans=maths, bytes_html=size)


def run(cmd, cwd):
    p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    return p.returncode, (p.stdout + p.stderr).strip()


def main():
    args = sys.argv[1:]
    upd = '--update' in args
    quick = '--quick' in args
    only = {a for a in args if not a.startswith('--')}
    data = load()
    reg_slugs = [t['slug'] for t in data['topics']]
    disk_topics = sorted(d for d in os.listdir(ROOT)
                         if os.path.isdir(os.path.join(ROOT, d)) and not d.startswith('.')
                         and os.path.exists(os.path.join(ROOT, d, 'assets', 'notes.css')))
    fails, notes = [], []

    for d in disk_topics:                                   # an unregistered folder is a silent gap
        if d not in reg_slugs:
            fails.append("%s/: folder exists but is not registered in topics.json" % d)

    for t in data['topics']:
        slug = t['slug']
        if only and slug not in only:
            continue
        d = os.path.join(ROOT, slug)
        if t.get('status') == 'planned' and not os.path.isdir(d):
            notes.append('%s: %s (nothing on disk yet)' % (slug, t.get('status')))
            continue
        if not os.path.isdir(d):
            fails.append('%s: registered but the folder is missing' % slug)
            continue

        entry = t.get('entry', '')
        if entry.endswith('.md') and not os.path.isfile(os.path.join(d, os.path.basename(entry))):
            fails.append('%s: Markdown entry is missing' % slug)
            continue
        if entry.endswith('.md') and not os.path.isfile(os.path.join(d, 'tools', 'check.py')):
            fails.append('%s: Markdown topic requires tools/check.py' % slug)

        if upd:                                             # recount from disk
            for k, v in count(d, entry).items():
                t[k] = v

        want, have = count(d, entry), t
        for k in want:
            if have.get(k) != want[k]:
                fails.append('%s: topics.json says %s=%s, the files say %s  (fix: --update)'
                             % (slug, k, have.get(k), want[k]))

        if t.get('owner') is None:
            fails.append('%s: nobody owns it \u2014 set "owner" before editing (CONTRIBUTING.md \u00a77)' % slug)

        sp = os.path.join(d, 'tools', 'setpages.py')
        if os.path.exists(sp):
            rc, out = run([sys.executable, 'tools/setpages.py', '--check'], d)
            if rc:
                fails.append('%s: %s' % (slug, out.splitlines()[-1] if out else 'pages.js stale'))

        ck = os.path.join(d, 'tools', 'check.py')
        if os.path.exists(ck):
            rc, out = run([sys.executable, 'tools/check.py'], d)
            if rc:
                fails.append('%s: tools/check.py failed\n%s' % (slug, '\n'.join('    ' + l for l in out.splitlines()[-25:])))
            else:
                notes.append('%s: check.py \u2713 (%s figures, %s question blocks)'
                             % (slug, want['figures'], want['questions']))
        node = subprocess.run(['which', 'node'], capture_output=True, text=True).stdout.strip() if not quick else ''
        tt = os.path.join(d, 'tools', 'test-tex.js')
        if node and os.path.exists(tt):
            rc, out = run([node, os.path.relpath(tt, d)], d)
            if rc:
                fails.append('%s: renderer tests failed\n%s' % (slug, out[-1200:]))
            else:
                notes.append('%s: %s' % (slug, out.splitlines()[-1].strip()))

    if upd:
        save(data)
        print('topics.json recounted from the files on disk.')
    for n in notes:
        print('  \u00b7', n)
    if fails:
        print('\n%d problem(s):' % len(fails))
        for f in fails:
            print('  \u2717', f)
        sys.exit(1)
    print('\n\u2713 all topics consistent with topics.json')


if __name__ == '__main__':
    main()

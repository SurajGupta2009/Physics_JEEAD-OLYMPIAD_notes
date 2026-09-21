#!/usr/bin/env python3
"""Build the offline browser edition of the Markdown notes.

Every topic's ``*.md`` is rendered into a static page under ``docs/site/``
with the local SVG figures, KaTeX-typeset maths (vendored in
``docs/site/katex/`` — no CDN, no network), a table of contents and
cross-topic navigation.  The finished site opens straight from ``file://``
on any machine, so the Markdown can be read the way it is meant to be read:
with its diagrams and with the equations typeset.

The only dependency is the ``markdown`` package, which is needed to build
the site but not to view it::

    pip install markdown
    python3 tools/md_site.py

Regenerating is idempotent; it touches only ``docs/site/*.html`` and
``docs/site/site.css`` (the vendored KaTeX is committed and left alone).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import markdown
except ImportError:  # pragma: no cover
    sys.exit("this generator needs the markdown package:  pip install markdown")

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "site"

# (site file, topic dir, display title, one-line description, figures, questions, endpoint)
TOPICS = [
    ("capacitors.html", "capacitors", "Capacitors",
     "Charge storage, energy and the networks built from it — fields, dielectrics, series/parallel machinery.",
     32, 150, "36-question INPhO-standard paper"),
    ("current-electricity.html", "current-electricity", "Current electricity",
     "Drift, resistance, real sources, Kirchhoff's laws, bridges and the RC time constant.",
     26, 145, "36-question INPhO-standard paper"),
    ("heat.html", "heat", "Heat",
     "Temperature, the first law in calorimetry, expansion, conduction and the ideal gas.",
     25, 48, "10-question written gauntlet"),
    ("thermodynamics.html", "thermodynamics", "Thermodynamics",
     "The first and second laws, kinetic theory, cyclic engines and entropy, worked to Olympiad depth.",
     35, 127, "36-question INPhO-standard paper"),
    ("geometrical-optics.html", "geometrical-optics", "Geometrical optics",
     "Rays, mirrors, refraction, prisms, lenses and instruments — from Fermat to étendue and the rainbow.",
     46, 152, "36-question INPhO-standard paper"),
    ("wave-optics.html", "wave-optics", "Wave optics",
     "Interference, diffraction, thin films and polarisation, from Huygens to the resolving power.",
     28, 172, "36-question INPhO-standard paper"),
]

PAGE_CSS = """
:root {
  --paper: #faf9f5; --card: #ffffff; --ink: #23221e; --muted: #6d685e;
  --line: #e2ded4; --accent: #1f5fa8; --accent-soft: #edf4fb;
  --box: #f4f1ea;
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0; background: var(--paper); color: var(--ink);
  font: 16px/1.68 Georgia, "Times New Roman", serif;
}
a { color: var(--accent); text-decoration: none; }
a:hover { text-decoration: underline; }
code, pre, .sans { font-family: ui-monospace, "SF Mono", Menlo, Consolas, monospace; }

/* ---------- top bar ---------- */
.top {
  position: sticky; top: 0; z-index: 10;
  display: flex; align-items: baseline; gap: 1.25rem; flex-wrap: wrap;
  padding: .65rem 1.25rem; background: var(--card);
  border-bottom: 1px solid var(--line);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif; font-size: .9rem;
}
.top .brand { font-weight: 700; color: var(--ink); font-size: 1rem; }
.top .brand:hover { text-decoration: none; }
.top nav { display: flex; gap: 1rem; flex-wrap: wrap; }
.top nav a { color: var(--muted); }
.top nav a.active { color: var(--ink); font-weight: 700; }

/* ---------- layout ---------- */
.layout {
  display: grid; grid-template-columns: 250px minmax(0, 1fr);
  gap: 2rem; max-width: 1320px; margin: 0 auto; padding: 0 1.25rem;
}
.toc {
  position: sticky; top: 3.4rem; align-self: start;
  max-height: calc(100vh - 4rem); overflow: auto;
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif; font-size: .84rem;
}
.toc details { border: 1px solid var(--line); border-radius: 8px; background: var(--card); }
.toc summary {
  cursor: pointer; padding: .55rem .9rem; font-weight: 700; color: var(--ink);
  list-style: none;
}
.toc summary::before { content: "☰ "; color: var(--muted); }
.toc ul { list-style: none; margin: 0; padding: .35rem .9rem .8rem; }
.toc li { margin: .3rem 0; }
.toc a { color: var(--muted); display: block; padding: .12rem 0; }
.toc a:hover { color: var(--accent); text-decoration: none; }

.page { min-width: 0; max-width: 880px; padding: 2.2rem 1.5rem 5rem; }

/* ---------- typography ---------- */
h1, h2, h3, h4 { line-height: 1.25; font-weight: 700; }
h1 { font-size: 1.9rem; margin: .6rem 0 1rem; }
h2 {
  font-size: 1.42rem; margin: 2.6rem 0 .9rem; padding-bottom: .35rem;
  border-bottom: 2px solid var(--line); scroll-margin-top: 4rem;
}
h3 { font-size: 1.12rem; margin: 1.9rem 0 .7rem; scroll-margin-top: 4rem; }
h4 { font-size: 1rem; margin: 1.4rem 0 .5rem; }
p { margin: .85em 0; }
ul, ol { padding-left: 1.5em; margin: .8em 0; }
li { margin: .3em 0; }
strong { font-weight: 700; }
hr { border: 0; border-top: 1px solid var(--line); margin: 2.2rem 0; }

/* ---------- figures ---------- */
img {
  max-width: 100%; height: auto; display: block; margin: 1.5rem auto;
  background: var(--card); border: 1px solid var(--line);
  border-radius: 10px; padding: 10px;
}

/* ---------- boxed notes (blockquotes) ---------- */
blockquote {
  margin: 1.25em 0; padding: .95em 1.2em;
  background: var(--box); border-left: 3px solid var(--accent);
  border-radius: 0 10px 10px 0;
}
blockquote p:first-child { margin-top: .2em; }
blockquote p:last-child { margin-bottom: .2em; }
blockquote blockquote { background: var(--card); }

/* ---------- tables ---------- */
table {
  display: block; overflow-x: auto; max-width: 100%;
  border-collapse: collapse; margin: 1.3em 0; background: var(--card);
  font-size: .94em;
}
th, td { border: 1px solid var(--line); padding: .5em .75em; text-align: left; vertical-align: top; }
th { background: var(--accent-soft); font-family: system-ui, sans-serif; font-size: .92em; }
tbody tr:nth-child(even) { background: #fbfaf7; }

/* ---------- solutions ---------- */
details {
  margin: 1.15em 0; border: 1px solid var(--line); border-radius: 10px;
  background: var(--card);
}
summary {
  cursor: pointer; padding: .6em 1em; font-weight: 700;
  font-family: system-ui, sans-serif; font-size: .95rem;
  color: var(--accent);
}
details > *:first-of-type { margin-top: .8em; }
details > :last-child { margin-bottom: .8em; }
details[open] summary { border-bottom: 1px dashed var(--line); }

/* ---------- maths (KaTeX) ---------- */
.katex { font-size: 1.06em; }
.katex-display {
  margin: 1.1em 0; padding: .2em 0;
  overflow-x: auto; overflow-y: hidden;
}
.katex-display::-webkit-scrollbar { height: 5px; }
.katex .tag { margin-left: 1em; }

/* ---------- pager / footer ---------- */
.pager {
  display: flex; justify-content: space-between; gap: 1rem; flex-wrap: wrap;
  margin-top: 3.5rem; padding-top: 1.2rem; border-top: 1px solid var(--line);
  font-family: system-ui, sans-serif; font-size: .92rem;
}
.colophon {
  margin-top: 1.2rem; color: var(--muted); font-size: .8rem;
  font-family: system-ui, sans-serif;
}

/* ---------- index cards ---------- */
.cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.1rem; margin: 1.5rem 0 3rem; }
.card {
  display: block; background: var(--card); border: 1px solid var(--line);
  border-radius: 12px; padding: 1.2rem 1.3rem; color: var(--ink);
}
.card:hover { border-color: var(--accent); text-decoration: none; box-shadow: 0 2px 10px rgba(31,95,168,.08); }
.card h2 { margin: 0 0 .4rem; font-size: 1.2rem; border: 0; padding: 0; }
.card p { margin: .3rem 0 .6rem; color: var(--muted); font-size: .95rem; }
.card .meta { color: var(--accent); font-size: .84rem; font-family: system-ui, sans-serif; font-weight: 600; }

/* ---------- responsive ---------- */
@media (max-width: 1000px) {
  .layout { grid-template-columns: 1fr; }
  .toc { position: static; max-height: none; }
  .page { padding-top: 1.2rem; }
}

/* ---------- print ---------- */
@media print {
  .top, .toc, .pager { display: none !important; }
  body { background: #fff; font-size: 11pt; }
  .layout { display: block; max-width: none; padding: 0; }
  .page { max-width: none; padding: 0; }
  img { break-inside: avoid; border: 0; padding: 0; }
  h2 { break-after: avoid; }
  details > *:not(summary) { display: block !important; content-visibility: visible !important; }
}
"""

INDEX_CSS_EXTRA = """
.index-head { max-width: 760px; margin: 0 auto; }
.index-head h1 { margin-top: .4rem; }
.index-head p { color: var(--muted); font-size: 1.02rem; }
"""

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — JEE / Olympiad physics notes</title>
<link rel="stylesheet" href="katex/katex.min.css">
<link rel="stylesheet" href="site.css">
</head>
<body>
<header class="top">
  <a class="brand" href="index.html">Physics notes</a>
  <nav>{nav}</nav>
</header>
<div class="layout">
  <aside class="toc"><details open><summary>Contents</summary>{toc}</details></aside>
  <main class="page">
{content}
    <footer class="pager">{pager}</footer>
    <p class="colophon">Rendered from <code>{source}</code> by <code>tools/md_site.py</code>.
    Fully offline: diagrams are local SVGs, maths is vendored KaTeX.
    The source of truth is <code>{source}</code> and the interactive edition <code>{html_edition}</code>.</p>
  </main>
</div>
<script src="katex/katex.min.js"></script>
<script src="katex/contrib/auto-render.min.js"></script>
<script>
renderMathInElement(document.body, {{
  delimiters: [
    {{left: "$$", right: "$$", display: true}},
    {{left: "$",  right: "$",  display: false}}
  ],
  throwOnError: false
}});
</script>
</body>
</html>
"""


def render_topic(source: Path, title: str, nav: str, pager: str) -> str:
    md = markdown.Markdown(
        extensions=["tables", "fenced_code", "sane_lists", "md_in_html", "toc"],
        extension_configs={"toc": {"toc_depth": "2-2", "permalink": False}},
    )
    text = source.read_text(encoding="utf-8")
    # The md_in_html extension only parses Markdown inside a raw-HTML block
    # when the block opts in with markdown=1 (PHP Markdown Extra semantics).
    # The solution blocks must be rendered — bold, lists, tables and the
    # chapter headings that heat/thermodynamics wrap in <details>.
    text = text.replace("<details>", '<details markdown=1>')
    body = md.convert(text)
    # Local figures: the Markdown uses paths relative to the topic directory.
    body = re.sub(r'src="assets/figures/', f'src="../../{source.parent.name}/assets/figures/', body)
    m = re.search(r'<div class="toc">(.*?)</div>', md.toc, re.S)
    toc = m.group(1).strip() if m else ""
    return PAGE.format(
        title=title, nav=nav, toc=toc, content=body, pager=pager,
        source=source.relative_to(ROOT).as_posix(),
        html_edition=(source.with_suffix(".html").relative_to(ROOT).as_posix()),
    )


def render_index() -> str:
    cards = []
    for file, _topic, title, blurb, figures, questions, endpoint in TOPICS:
        cards.append(
            f'<a class="card" href="{file}"><h2>{title}</h2>'
            f'<p>{blurb}</p>'
            f'<span class="meta">{figures} figures · {questions} questions · {endpoint}</span></a>'
        )
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Physics notes — JEE Advanced &amp; the Olympiad track</title>
<link rel="stylesheet" href="site.css">
</head>
<body>
<header class="top">
  <a class="brand" href="index.html">Physics notes</a>
  <nav>{"".join(f'<a href="{f}">{t}</a>' for f, _d, t, _b, _x, _y, _z in TOPICS)}</nav>
</header>
<main class="page index-head">
  <h1>Physics notes for JEE Advanced and the Olympiad track</h1>
  <p>Portable Markdown note-sets, rendered here with their local SVG diagrams and
     KaTeX-typeset equations — fully offline, no network needed. The same content lives
     as <code>*.md</code> in each topic folder (readable on GitHub) and as an interactive
     single-file HTML edition.</p>
  <div class="cards">{''.join(cards)}</div>
  <p><a href="https://github.com/SurajGupta2009/Physics_JEEAD-OLYMPIAD_notes">Repository</a>
     · <a href="../../README.md">README</a> · cross-topic plan in <a href="../../CURRICULUM.md">CURRICULUM.md</a></p>
</main>
</body>
</html>
"""
    return html


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "site.css").write_text(PAGE_CSS + INDEX_CSS_EXTRA, encoding="utf-8")
    nav_items = [(file, title) for file, _d, title, _b, _x, _y, _z in TOPICS]
    # The note files follow a fixed naming; map explicitly to be safe.
    name_map = {
        "capacitors": "Capacitors.md",
        "current-electricity": "Current-electricity.md",
        "heat": "Heat.md",
        "thermodynamics": "Thermodynamics.md",
        "geometrical-optics": "Geometrical-optics.md",
        "wave-optics": "Wave-optics.md",
    }
    for i, (file, topic, title, _blurb, _figs, _qs, _ep) in enumerate(TOPICS):
        source = ROOT / topic / name_map[topic]
        if not source.exists():
            sys.exit(f"missing source: {source}")
        nav = "".join(
            f'<a href="{f}" class="{"active" if f == file else ""}">{t}</a>'
            for f, t in nav_items
        )
        prev = nav_items[i - 1] if i > 0 else None
        nxt = nav_items[i + 1] if i < len(nav_items) - 1 else None
        pager = (
            (f'<a href="{prev[0]}">← {prev[1]}</a>' if prev else "&nbsp;")
            + (f'<a href="{nxt[0]}">{nxt[1]} →</a>' if nxt else "&nbsp;")
        )
        (OUT / file).write_text(render_topic(source, title, nav, pager), encoding="utf-8")
        print(f"{file:<28} {source.relative_to(ROOT)}")
    (OUT / "index.html").write_text(render_index(), encoding="utf-8")
    print(f"{'index.html':<28} (topic overview)")
    print(f"\nOpen {OUT / 'index.html'} — or run `python3 -m http.server` in docs/site for a local server.")


if __name__ == "__main__":
    main()

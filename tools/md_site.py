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

# (site file, topic dir, display title, one-line description, figures, questions, endpoint, group)
# `figures` counts local SVG diagrams for the nine shipped note-sets and DIAGRAM
# figure briefs (plan.md §1.2) for the text-only plan.md chapters — no chapter in
# this plan ships an image file, by design.
WAVES_THERMO = "Waves & thermodynamics"
ELECTRICITY = "Electricity & magnetism"
OPTICS = "Optics"
MECHANICS = "Mechanics (plan.md PART 1–10)"
MODERN = "Modern physics (plan.md PART 23–28)"

TOPICS = [
    ("string-waves.html", "string-waves", "String waves",
     "Transverse mechanical waves: the 1-D wave equation from Newton's second law, energy/power, boundary reflection, standing waves and normal modes.",
     5, 36, "36-question, 3 h, 144-mark Olympiad paper", WAVES_THERMO),
    ("sound-waves.html", "sound-waves", "Sound waves",
     "Longitudinal pressure waves, Laplace v, decibels, organ pipes with end-correction, beats, and the full 2D/wind/echo Doppler effect.",
     15, 18, "36-question, 3 h, 150-mark paper", WAVES_THERMO),
    ("electromagnetic-waves.html", "electromagnetic-waves", "Electromagnetic waves",
     "Displacement current, Maxwell's equations, Poynting vector, radiation pressure at normal and oblique incidence, and the EM spectrum.",
     7, 52, "36-question, 3 h, 180-mark JEE–Olympiad paper", WAVES_THERMO),
    ("heat.html", "heat", "Heat",
     "Temperature, the first law in calorimetry, expansion, conduction and the ideal gas.",
     25, 48, "10-question written gauntlet", WAVES_THERMO),
    ("thermodynamics.html", "thermodynamics", "Thermodynamics",
     "The first and second laws, kinetic theory, cyclic engines and entropy, worked to Olympiad depth.",
     35, 127, "36-question INPhO-standard paper", WAVES_THERMO),
    ("capacitors.html", "capacitors", "Capacitors",
     "Charge storage, energy and the networks built from it — fields, dielectrics, series/parallel machinery.",
     32, 150, "36-question INPhO-standard paper", ELECTRICITY),
    ("current-electricity.html", "current-electricity", "Current electricity",
     "Drift, resistance, real sources, Kirchhoff's laws, bridges and the RC time constant.",
     26, 145, "36-question INPhO-standard paper", ELECTRICITY),
    ("geometrical-optics.html", "geometrical-optics", "Geometrical optics",
     "Rays, mirrors, refraction, prisms, lenses and instruments — from Fermat to étendue and the rainbow.",
     46, 152, "36-question INPhO-standard paper", OPTICS),
    ("wave-optics.html", "wave-optics", "Wave optics",
     "Interference, diffraction, thin films and polarisation, from Huygens to the resolving power.",
     28, 172, "36-question INPhO-standard paper", OPTICS),

    # ---- the plan.md chapters: text-only, Obsidian-first, figure briefs ----
    ("units-measurements.html", "units-measurements", "Units, dimensions & errors",
     "PART 1 · SI base units, dimensional formulae and homogeneity, significant figures, error propagation, vernier and screw gauge, least squares and the Buckingham π theorem.",
     12, 47, "36-question, 3 h, 200-mark paper", MECHANICS),
    ("vectors.html", "vectors", "Vectors & vector algebra",
     "PART 2 · components and resolution, dot and cross products, triple products, the polar basis and vector calculus for mechanics.",
     12, 47, "36-question, 3 h, 200-mark paper", MECHANICS),
    ("kinematics-1d.html", "kinematics-1d", "Motion in one dimension",
     "PART 3 · the x–t / v–t / a–t trio, constant acceleration derived by integration, free fall, variable acceleration and 1-D relative motion.",
     12, 47, "36-question, 3 h, 200-mark paper", MECHANICS),
    ("motion-in-two-dimensions.html", "motion-in-two-dimensions", "2-D motion & projectiles",
     "PART 4 · the independence principle, relative velocity in 2-D, oblique projection from ground and tower, the safety parabola, circular kinematics.",
     12, 47, "36-question, 3 h, 200-mark paper", MECHANICS),
    ("newtons-laws.html", "newtons-laws", "Newton's laws & friction",
     "PART 5 · free-body discipline, friction, constraint relations for pulleys and wedges, pseudo forces, circular dynamics.",
     12, 47, "36-question, 3 h, 200-mark paper", MECHANICS),
    ("work-energy-power.html", "work-energy-power", "Work, energy & power",
     "PART 6 · the work–energy theorem from F = ma, conservative forces, potential-energy diagrams and stability, non-conservative bookkeeping.",
     12, 47, "36-question, 3 h, 200-mark paper", MECHANICS),
    ("centre-of-mass-momentum.html", "centre-of-mass-momentum", "Centre of mass & collisions",
     "PART 7 · COM of standard bodies, momentum and impulse, restitution, the COM frame, variable mass and the rocket equation.",
     12, 47, "36-question, 3 h, 200-mark paper", MECHANICS),
    ("rotational-mechanics.html", "rotational-mechanics", "Rotational mechanics",
     "PART 8 · moment of inertia derived, the two axis theorems proved, torque and τ = Iα, rolling without slipping, gyroscopic precession.",
     12, 47, "36-question, 3 h, 200-mark paper", MECHANICS),
    ("gravitation.html", "gravitation", "Gravitation & orbital motion",
     "PART 9 · the shell theorem proved, variation of g, Kepler's laws derived, vis-viva, Hohmann transfers, binaries, tides and the Roche limit.",
     12, 47, "36-question, 3 h, 200-mark paper", MECHANICS),
    ("simple-harmonic-motion.html", "simple-harmonic-motion", "Simple harmonic motion",
     "PART 10 · the F = −kx test, phasors, springs and pendulums, the small-oscillation method, damping, resonance and coupled oscillators.",
     12, 47, "36-question, 3 h, 200-mark paper", MECHANICS),
    ("fluid-mechanics.html", "fluid-mechanics", "Fluid mechanics",
     "PART 11 · hydrostatics from dp/dy = −ρg, Pascal, Archimedes, Bernoulli and its four gates, Poiseuille, Stokes, surface tension and capillarity.",
     20, 47, "36-question, 3 h, 200-mark paper", MECHANICS),
    ("elasticity.html", "elasticity", "Elasticity",
     "PART 12 · stress and strain, the three moduli and Poisson's ratio, thermal stress, torsion, elastic energy, bending, and the atomic spring.",
     14, 47, "36-question, 3 h, 200-mark paper", MECHANICS),
    ("photoelectric-effect.html", "photoelectric-effect", "Photoelectric effect & matter waves",
     "PART 23 · the photon hypothesis, Einstein's equation, stopping potential and the cutoff, de Broglie waves and Davisson–Germer.",
     16, 54, "36-question, 3 h, 200-mark INPhO-standard paper", MODERN),
    ("atomic-structure.html", "atomic-structure", "Atomic structure & the Bohr model",
     "PART 24 · Rutherford scattering, the Bohr postulates, hydrogen-like spectra, Moseley, and where the model breaks.",
     16, 54, "36-question, 3 h, 200-mark INPhO-standard paper", MODERN),
    ("x-rays.html", "x-rays", "X-rays, Moseley & Bragg",
     "PART 25 · continuous and characteristic spectra, the short-wavelength limit, Moseley's law, Bragg diffraction and the Compton effect.",
     16, 54, "36-question, 3 h, 200-mark INPhO-standard paper", MODERN),
    ("nuclear-physics.html", "nuclear-physics", "Nuclear physics & radioactivity",
     "PART 26 · nuclear size and density, binding energy and the mass defect, decay kinetics, decay series and equilibrium, fission and fusion.",
     18, 54, "36-question, 3 h, 200-mark INPhO-standard paper", MODERN),
    ("semiconductors.html", "semiconductors", "Semiconductors & devices",
     "PART 27 · bands, intrinsic and extrinsic carriers, the p–n junction, LED and Zener, the BJT and logic gates.",
     18, 54, "36-question, 3 h, 200-mark paper", MODERN),
    ("communication-systems.html", "communication-systems", "Communication systems",
     "Amplitude and frequency modulation, bandwidth, propagation modes and signal processing at JEE-Main depth.",
     12, 47, "36-question, 3 h, 200-mark paper", MODERN),
    ("special-relativity.html", "special-relativity", "Special relativity",
     "PART 28 · the two postulates, time dilation and length contraction, relativistic momentum and energy, E = mc², the optical Doppler effect.",
     12, 47, "36-question, 3 h, 200-mark IPhO-standard paper", MODERN),
]

# Wikilink targets used across the chapters resolve to these site pages.
SLUG_BY_NOTE = {
    "String-waves": "string-waves", "Sound-waves": "sound-waves",
    "Electromagnetic-waves": "electromagnetic-waves", "Heat": "heat",
    "Thermodynamics": "thermodynamics", "Capacitors": "capacitors",
    "Current-electricity": "current-electricity",
    "Geometrical-optics": "geometrical-optics", "Wave-optics": "wave-optics",
    "Units-measurements": "units-measurements", "Vectors": "vectors",
    "Kinematics-1d": "kinematics-1d",
    "Motion-in-two-dimensions": "motion-in-two-dimensions",
    "Newtons-laws": "newtons-laws", "Work-energy-power": "work-energy-power",
    "Centre-of-mass-momentum": "centre-of-mass-momentum",
    "Rotational-mechanics": "rotational-mechanics", "Gravitation": "gravitation",
    "Simple-harmonic-motion": "simple-harmonic-motion",
    "Fluid-mechanics": "fluid-mechanics",
    "Elasticity": "elasticity",
    "Photoelectric-effect": "photoelectric-effect",
    "Atomic-structure": "atomic-structure", "X-rays": "x-rays",
    "Nuclear-physics": "nuclear-physics", "Semiconductors": "semiconductors",
    "Communication-systems": "communication-systems",
    "Special-relativity": "special-relativity",
}
SLUG_BY_NOTE.update({k.lower(): v for k, v in list(SLUG_BY_NOTE.items())})

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
.top nav { display: flex; gap: .45rem .8rem; flex-wrap: wrap; align-items: baseline; }
.top nav a { color: var(--muted); font-size: .82rem; }
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

/* ---------- Obsidian callouts (plan.md §1.3.1) ---------- */
.callout {
  --tint: #1f5fa8;
  margin: 1.25em 0; padding: .8em 1.15em .35em;
  background: color-mix(in srgb, var(--tint) 6%, var(--card));
  border: 1px solid color-mix(in srgb, var(--tint) 28%, var(--line));
  border-left: 4px solid var(--tint);
  border-radius: 0 10px 10px 0;
}
.callout > .callout-title {
  margin: 0 0 .45em; font-weight: 700; color: var(--tint);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif; font-size: .9rem;
  letter-spacing: .01em;
}
.callout > p:first-of-type:not(.callout-title) { margin-top: 0; }
.callout > :last-child { margin-bottom: .55em; }
.callout table { font-size: .9em; }
.callout .katex-display { margin: .7em 0; }
.callout.note    { --tint: #1f5fa8; }
.callout.info    { --tint: #0f7b6c; }
.callout.warning { --tint: #b0770a; }
.callout.success { --tint: #2e7d32; }
.callout.danger  { --tint: #b3261e; }
.callout.tip     { --tint: #6a4fb3; }
.callout.quote   { --tint: #5b6470; }
.callout.question{ --tint: #a4477c; }
.callout.example { --tint: #2a6f97; }
/* the [!abstract] slot doubles as the chapter's figure-brief box (plan.md §1.2) */
.callout.abstract { --tint: #7a6a4f; background: #f7f4ec; }
.callout.abstract > .callout-title { font-family: Georgia, serif; font-size: .98rem; }

/* ---------- frontmatter properties strip ---------- */
.props { margin: 0 0 1.4rem; display: flex; gap: .4rem; flex-wrap: wrap; }
.props .prop {
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif; font-size: .78rem;
  color: var(--muted); background: var(--box); border: 1px solid var(--line);
  border-radius: 999px; padding: .12rem .6rem;
}
.props .prop b { color: var(--ink); font-weight: 700; }
.props .prop.tag { color: var(--accent); background: var(--accent-soft); border-color: transparent; }
.wikilink { border-bottom: 1px dotted var(--muted); }

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
.index-head { max-width: 1080px; margin: 0 auto; }
.index-head h1 { margin-top: .4rem; }
.index-head p { color: var(--muted); font-size: 1.02rem; }
.index-head h2.group {
  margin: 2.4rem 0 .2rem; padding-bottom: .3rem;
  border-bottom: 1px solid var(--line);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  font-size: 1rem; letter-spacing: .04em; text-transform: uppercase;
  color: var(--muted);
}
.top nav .nav-group { display: contents; }
.top nav .nav-group i { display: none; }
.top nav .nav-group + .nav-group > a:first-child { border-left: 1px solid var(--line); padding-left: .8rem; }
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
    The source of truth is <code>{source}</code> {edition_note}.</p>
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


CALLOUT_LABEL = {
    "note": "Definition", "info": "Why", "warning": "Condition of validity",
    "success": "Check", "danger": "Trap", "tip": "Insight", "quote": "Hand-off",
    "question": "Exam note", "abstract": "Numbers to keep", "example": "Worked example",
}


def strip_frontmatter(text: str) -> tuple[str, dict[str, str]]:
    """Split a leading YAML property block off the source.

    The plan.md chapters open with `---` properties (plan.md §1.3.1). Rendered as
    Markdown they would become a stray <hr> plus a paragraph of raw `key: value`
    lines, so they are lifted out and shown as a small properties strip instead.
    """
    if not text.startswith("---\n"):
        return text, {}
    end = text.find("\n---", 4)
    if end == -1:
        return text, {}
    raw, body = text[4:end], text[end + 4:].lstrip("\n")
    props: dict[str, str] = {}
    for line in raw.split("\n"):
        if ":" in line and not line.startswith((" ", "\t")):
            key, _, val = line.partition(":")
            props[key.strip()] = val.strip()
    return body, props


def _sub_converter() -> "markdown.Markdown":
    """A fresh converter for callout bodies (fresh, so its TOC/state stay out)."""
    return markdown.Markdown(
        extensions=["tables", "fenced_code", "sane_lists"],
    )


def callouts_to_html(text: str) -> str:
    """Rewrite Obsidian `> [!type] Title` callouts as styled divs.

    python-markdown has no callout syntax: left alone, a callout renders as a
    plain blockquote whose first line reads "[!info] Why" — the visual language
    of the notes (plan.md §1.3.1) would be lost.

    The body is converted by a sub-converter and the finished div is emitted as a
    raw HTML block. Deliberately *not* `<div markdown=1>`: the `md_in_html`
    extension mis-closes those blocks (it auto-appends a second `</div>`, which
    desynchronises the div tree and silently swallows the rest of the chapter),
    so the callouts are rendered here instead of delegated.
    """
    header = re.compile(r"^> \[!([a-z]+)\](-|\+)? ?(.*)$")
    out: list[str] = []
    lines = text.split("\n")
    i = 0
    while i < len(lines):
        head = header.match(lines[i])
        if not head:
            out.append(lines[i])
            i += 1
            continue
        kind, label = head.group(1), head.group(3).strip()
        body: list[str] = []
        i += 1
        while i < len(lines):
            # the next callout in the same run starts a new box, it does not end this one
            if header.match(lines[i]):
                break
            if lines[i].startswith(">"):
                body.append(re.sub(r"^> ?", "", lines[i]))
                i += 1
                continue
            if lines[i].strip() == "":
                # a blank line continues the callout only if more `>` lines follow
                j = i
                while j < len(lines) and lines[j].strip() == "":
                    j += 1
                if j < len(lines) and lines[j].startswith(">") and not header.match(lines[j]):
                    body.extend([""] * (j - i))
                    i = j
                    continue
                break
            break
        title = label or CALLOUT_LABEL.get(kind, kind)
        inner = "\n".join(body).strip("\n")
        rendered = _sub_converter().convert(inner) if inner else ""
        out.append("")
        out.append(f'<div class="callout {kind}">')
        out.append(f'<p class="callout-title">{title}</p>')
        if rendered:
            out.append(rendered)
        out.append("</div>")
        out.append("")
    return "\n".join(out)


def wikilinks_to_links(text: str) -> str:
    """Turn Obsidian `[[Note]]` / `[[Note#head|label]]` into site links.

    The chapters cross-reference each other with wikilinks (plan.md §1.3.1
    item 9). On the rendered site the target is `<slug>.html`; an unresolvable
    target degrades to its label rather than to a dead link.
    """
    def repl(m: re.Match[str]) -> str:
        target, _, label = m.group(1).partition("|")
        note, _, _anchor = target.partition("#")
        slug = SLUG_BY_NOTE.get(note.strip()) or SLUG_BY_NOTE.get(note.strip().lower())
        text_label = label.strip() or note.strip()
        if slug:
            return f"[{text_label}]({slug}.html)"
        return f"<span class=\"wikilink\">{text_label}</span>"

    return re.sub(r"\[\[([^\]\n]+)\]\]", repl, text)


def render_topic(source: Path, title: str, nav: str, pager: str) -> str:
    md = markdown.Markdown(
        extensions=["tables", "fenced_code", "sane_lists", "md_in_html", "toc"],
        extension_configs={"toc": {"toc_depth": "2-2", "permalink": False}},
    )
    text = source.read_text(encoding="utf-8")
    text, props = strip_frontmatter(text)
    text = callouts_to_html(text)
    text = wikilinks_to_links(text)
    if props:
        chips = "".join(
            f'<span class="prop"><b>{k}</b> {v}</span>'
            for k, v in props.items() if k in ("part", "slug", "source")
        )
        tags = props.get("tags", "").strip("[]")
        if tags:
            chips += "".join(f'<span class="prop tag">{t.strip()}</span>'
                             for t in tags.split(",") if t.strip())
        text = f'<p class="props">{chips}</p>\n\n' + text
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
    # The nine shipped note-sets also keep an interactive single-file HTML
    # edition; the plan.md chapters are Markdown-only by design (plan.md §1.1).
    html_edition = source.with_suffix(".html")
    edition_note = (
        f'and the interactive edition <code>{html_edition.relative_to(ROOT).as_posix()}</code>'
        if html_edition.exists() else
        'and there is no separate HTML edition — this chapter is Markdown-only by design'
    )
    return PAGE.format(
        title=title, nav=nav, toc=toc, content=body, pager=pager,
        source=source.relative_to(ROOT).as_posix(),
        edition_note=edition_note,
    )


def grouped() -> list[tuple[str, list[tuple]]]:
    """TOPICS in listed order, collected under their group headings."""
    out: list[tuple[str, list[tuple]]] = []
    for row in TOPICS:
        if not out or out[-1][0] != row[7]:
            out.append((row[7], []))
        out[-1][1].append(row)
    return out


def media_phrase(figures: int, group: str) -> str:
    """The nine shipped note-sets carry SVG files; the plan.md chapters carry briefs."""
    if group in (WAVES_THERMO, ELECTRICITY, OPTICS):
        return f"{figures} local SVG figures"
    return f"text-only · {figures} figure briefs"


def render_index() -> str:
    sections = []
    for group, rows in grouped():
        cards = "".join(
            f'<a class="card" href="{file}"><h2>{title}</h2>'
            f'<p>{blurb}</p>'
            f'<span class="meta">{media_phrase(figures, group)} · {questions} question blocks · {endpoint}</span></a>'
            for file, _topic, title, blurb, figures, questions, endpoint, _g in rows
        )
        sections.append(f'<h2 class="group">{group}</h2><div class="cards">{cards}</div>')
    nav = "".join(
        f'<span class="nav-group"><i>{group}</i>'
        + "".join(f'<a href="{file}">{title}</a>'
                  for file, _t, title, _b, _x, _y, _z, _g in rows)
        + "</span>"
        for group, rows in grouped()
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
  <nav>{nav}</nav>
</header>
<main class="page index-head">
  <h1>Physics notes for JEE Advanced and the Olympiad track</h1>
  <p>Portable Markdown note-sets, rendered here with KaTeX-typeset equations — fully
     offline, no network needed. The same content lives as <code>*.md</code> in each topic
     folder (readable on GitHub, and as an Obsidian vault). The nine shipped note-sets keep
     local SVG diagrams and an interactive single-file HTML edition; the
     <code>plan.md</code> chapters are text-only and describe every figure as a
     <code>DIAGRAM</code> brief with search words instead of shipping an image.</p>
  {''.join(sections)}
  <p><a href="https://github.com/SurajGupta2009/Physics_JEEAD-OLYMPIAD_notes">Repository</a>
     · <a href="../../README.md">README</a> · cross-topic plan in <a href="../../CURRICULUM.md">CURRICULUM.md</a></p>
</main>
</body>
</html>
"""
    return html


def registry_entries() -> dict[str, str]:
    """slug -> master Markdown path, straight from the checked registry."""
    import json
    data = json.loads((ROOT / "topics.json").read_text(encoding="utf-8"))
    return {t["slug"]: t.get("entry", "") for t in data["topics"]}


def master_of(topic: str, entries: dict[str, str]) -> Path:
    """The chapter's Markdown master.

    The registry's `entry` is the starting point, but for the seven HTML-first
    note-sets it names the interactive `.html` edition — that is the input
    `tools/check_all.py` counts, not the source this site renders. Their
    exported `.md` twin sits alongside and is the right source here.
    """
    entry = entries.get(topic, "")
    if not entry:
        sys.exit(f"{topic}: no 'entry' in topics.json — register the master Markdown first")
    source = ROOT / entry
    if source.suffix == ".html":
        source = source.with_suffix(".md")
    if not source.exists():
        sys.exit(f"{topic}: no Markdown master at {source.relative_to(ROOT)}")
    return source


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "site.css").write_text(PAGE_CSS + INDEX_CSS_EXTRA, encoding="utf-8")
    nav_items = [(file, title) for file, _d, title, _b, _x, _y, _z, _g in TOPICS]
    entries = registry_entries()
    missing = [t for _f, t, *_r in TOPICS if t not in entries]
    if missing:
        sys.exit(f"not registered in topics.json: {', '.join(missing)}")
    for i, (file, topic, title, _blurb, _figs, _qs, _ep, _group) in enumerate(TOPICS):
        source = master_of(topic, entries)
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
    print(f"\nOpen {OUT / 'index.html'} — or, to serve it locally, run `python3 -m http.server 8080` "
          f"in the repository root (not in docs/site: the pages reach the topic assets at ../../<topic>/assets/) "
          f"and visit http://localhost:8080/docs/site/.")


if __name__ == "__main__":
    main()

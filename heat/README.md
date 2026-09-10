# Heat — from basics to Olympiad

A self-contained HTML course on **thermal expansion, calorimetry and heat transfer** — temperature and internal
energy as the ledger, then expansion, phase change, conduction, convection, radiation, and an Olympiad toolkit —
written for **JEE (Main & Advanced)** and the **physics olympiad track (NSEP → INPhO → IPhO)**. It works offline
from `file://`: no CDN, no MathJax, no fonts, no build step.

```
open heat/Heat.html   ← the whole course, one file (also served as the topic entry)
```

or, to browse with the interactive features (theme switch, expand/collapse):

```
cd heat && python3 -m http.server 8000
```

## What is in the folder

`Heat.html` is the **only** HTML file — the repo's single-page, mind-map layout (as in
`current-electricity/` and `capacitors/`). Everything lives inside it in reading order: the overview, the
**expandable mind-map**, seven theory chapters with questions interleaved, and a ten-question written gauntlet
with full solutions, trap shelf and constant shelf. The stylesheet and the TeX renderer are inlined, so the file
is portable on its own. `assets/` keeps copies used by the tooling; `tools/` holds the validators
(`check.py`, `mathfix.py`, `setpages.py`, `test-tex.js`).

## The mind-map layout

The page opens with a map: the root node is the course, one branch per chapter, each labelled with what it covers
and its size (`N Q · M fig · K boxes`). Clicking a branch opens that chapter *in place* — full theory, every
figure, every question with its collapsible solution. The top bar offers *Expand all*, *Collapse all* and
*Print / PDF*; printing opens everything first and drops the map. Collapsed, the eight nodes are a revision
outline; expanded, they are the whole course. Deep-linking works (`#ch-04` opens conduction).

## The teaching contract

* **Concepts before formulas.** Heat, temperature and internal energy are separated before any law is written;
  every equation carries its validity clause (lumped ⇔ Bi ≤ 0.1, grey body ⇔ stated, √t law ⇔ quasi-steady).
* **Every number is checkable.** All worked values (steam-into-ice's 267.5 kJ, the 0.111 m first day of lake
  ice, 255 K for the bare-rock Earth, 16.7 °C touch-temperature of steel) are computed in-file; the constant
  shelf in the last chapter is the only look-up, meant to be memorised.
* **Diagrams over prose** — 24 inline SVG figures: hole-enlargement, the bimetal curl, the plateau graph, the
  √t ice curve, the film behind *h*, the planetary /4, the critical-radius hump, the effusivity contact.
* **Cross-references by text, not links.** First-law and kinetic-theory machinery is *named* from the
  thermodynamics set, never hyperlinked: one file must stand alone.

## Validation

```
python3 tools/mathfix.py && python3 tools/setpages.py && python3 tools/check.py
```

`check.py` guards markup balance, math spans, figure/caption parity, and anchors (`#ch-NN` ids). At the repo
root, `python3 tools/check_all.py` runs the same gate for every topic and re-syncs `topics.json` with
`--update`.

## Deliberately not covered

* Convection correlations (Nu–Ra–Re catalogues) and boundary-layer theory — the stagnant-film estimate of h
  and the lumped/ Bi analysis are the boundary here; they are exactly the parts that generalise from this set.
* Boiling-crisis curves, condenser/heat-exchanger design (LMTD), porous-media flow: named where they matter,
  not built.
* Planck/Wien as statistical mechanics (the full derivation lives in the thermodynamics set, ch 7).
* View-factor catalogue for arbitrary enclosures: large-enclosure and parallel-plate exchange only.

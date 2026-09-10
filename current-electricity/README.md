# Current Electricity — from basics to Olympiad

A self-contained HTML course on **current, resistance, cells, networks, instruments and real-wire physics**,
written for **JEE Advanced** and the **physics olympiad track (NSEP → INPhO → IPhO, plus IOPT)**. The complete course is in `Current-electricity.html`; it works
offline from `file://`: no CDN, no MathJax, no fonts, no build step.

```
open current-electricity/Current-electricity.html   ← start here (course map, how to study, the exam note)
```

or, to browse with the interactive features (theme switch, progress ticks, solved-question tracking):

```
cd current-electricity && python3 -m http.server 8000
```

## What is in the folder

`Current-electricity.html` is the only HTML file in this folder. It contains the overview, all theory sections,
the Olympiad paper, complete solutions, and the formula sheet in reading order. The `assets/` folder
contains only the local stylesheet and scripts needed to render it offline.

## The teaching contract

* **Concepts before formulas, formulas before problems.** Each chapter opens with *why the quantity exists*, then
  derives, then applies. Nothing is stated as a rule to memorise without its derivation or its failure mode.
* **Every step's reasoning is written down.** The `.why` boxes answer "but *why* is that true?", and the `.trap`
  boxes name the mistake before the reader can make it.
* **Questions interleaved with the theory**, not parked at the end: each is followed by a collapsible full solution.
* **Diagrams over prose wherever geometry does the work** — the figures are drawn so that the currents, the nodes
  and the dimensions sit in the same picture.
* **The last chapter is a real paper**: 36 questions covering every section, at INPhO standard with JEE-format
  sections, plus a separate solutions file.

## Handover notes (for the next writer)

* Chapters 1–3 interleave their questions late (one Questions block per chapter); chapters 4–7 mix them into the
  flow. Both patterns pass the checker; pick whichever suits the chapter you add.
* The unbalanced bridge (arms 10/20/30/40 Ω, 10 V) is the recurring worked example: nodal (ch 4) → Thevenin/Norton
  (ch 5) → reciprocity swap (ch 5). Keep new examples consistent with its numbers (V_th = 0.952 V, R_th = 23.81 Ω,
  I_sc = 40.0 mA) rather than re-deriving a second bridge.
* Every number in ch 7's scaling laws (fuse 3/2 exponent, transmission 1/V², thermocouple a/2b vs a/b) is derived
  in-text; if you extend ch 7, derive the exponent before quoting it.

## Editing

```bash
python3 tools/mathfix.py      # normalise authoring slips (idempotent)
python3 tools/setpages.py     # page order = filenames (run after adding/renaming a file)
python3 tools/check.py        # ALL GOOD or a list of problems
```

## Deliberately not covered

* **RC/RL transients and capacitor charging** — owned by `capacitors/` ch 6; we only borrow the Thevenin idea.
* **AC circuits, impedance, power factor, three-phase** — a future topic; this set is strictly DC steady state.
* **Magnetic effects of current** (force on wires, Biot–Savart) — belongs to the magnetism note-set.
* **Semiconductor device physics** beyond the diode curve and the thermistor law (no transistor biasing, no
  small-signal models).
* **Superconductivity beyond the DC ledger**: no BCS mechanism, no Josephson junctions, no type-II vortex physics —
  the persistence argument of ch 7 is the whole DC story we need.
* **Circuit simulation / SPICE**: every result in the folder is closed-form and checkable by hand.

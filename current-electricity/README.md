# Current Electricity — from basics to Olympiad

A self-contained HTML course on **current, resistance, cells, networks, instruments and real-wire physics**,
written for **JEE Advanced** and the **physics olympiad track (NSEP → INPhO → IPhO, plus IOPT)**. Every page works
offline from `file://`: no CDN, no MathJax, no fonts, no build step.

```
open current-electricity/index.html   ← start here (course map, how to study, the exam note)
```

or, to browse with the interactive features (theme switch, progress ticks, solved-question tracking):

```
cd current-electricity && python3 -m http.server 8000
```

## What is in the folder

| file | covers | status |
|---|---|---|
| `index.html` | course map, how to use the notes, syllabus mapping | done |
| `01-current-and-drift.html` | current as flux, continuity, drift velocity, relaxation time, microscopic Ohm's law, signal vs carrier speed | done |
| `02-resistivity-and-materials.html` | resistivity, the slice integral, spherical shell, temperature coefficients, metals vs semiconductors, non-ohmic devices | done |
| `03-emf-and-cells.html` | EMF as work per coulomb, internal resistance, terminal voltage in charge/discharge, grouping, maximum power, the joule ledger | done |
| `04-kirchhoff-and-bridges.html` | KCL/KVL with sign discipline, dividers, symmetry (the cube), balanced and unbalanced bridges, delta–star, infinite ladders | done |
| `05-network-theorems.html` | superposition, Thevenin, Norton, source transformation, maximum power transfer, reciprocity, compensation — all verified on one bridge | done |
| `06-instruments-and-measurement.html` | galvanometer conversions, loading error, meter bridge with end-error swap, potentiometer, four-terminal measurement | done |
| `07-advanced-topics.html` | fuse scaling `I∝r³ᐟ²`, transmission efficiency, thermocouples (neutral/inversion), thermistor load lines, superconducting persistence, piecewise diode discipline | done |
| `08-playbook.html` | triage table, the twelve moves, 20 traps with one-line replies, numbers to own, a 15-question timed drill | done |
| `09-olympiad-paper.html` | **the paper: 36 questions** in four sections (12 single-correct, 6 multiple-correct, 8 numerical, 10 long), coverage map and marking scheme | done |
| `10-olympiad-solutions.html` | complete solutions to all 36, marks distributed, with the check that verifies each answer | done |
| `11-formula-sheet.html` | the whole course on three printable A4 pages (2-column, `Ctrl-P` → PDF) | done |

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

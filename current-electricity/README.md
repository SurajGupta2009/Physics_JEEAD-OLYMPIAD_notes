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

## Coverage — the Cengage chapters as the floor

The specification was *at least everything in the Cengage chapters*, plus the Olympiad material those chapters
do not reach. From the uploaded Cengage volume (*Electrostatics and Current Electricity*, R.K. Malik / Newton
Classes edition) the relevant chapters are **5 Electric Current and Circuits** (pp. 5.1–5.56), **6 Electrical
Measuring Instruments** (pp. 6.1–6.20) and **7 Heating Effects of Current** (pp. 7.1–7.20), with Appendix A2's
mixed exercise sets. Every numbered contents entry of those chapters is mapped to a section of
`Current-electricity.html` in the file's own **Cengage coverage map** (front matter, right after *How these notes
are organised*), and the two items the file did not carry — mobility as a theory item, and the general
current-divider — plus the transient material Cengage keeps in this chapter (§5.25–5.31) have been added:

| added for the Cengage floor | where |
|---|---|
| mobility in the theory (not only in a question): <m>\mu=v_d/E=e\tau/m</m>, <m>\sigma=ne\mu</m>, two-carrier form, numbers for Cu and Si | §1.4, box *Mobility* |
| the general current divider for three or more resistors, in conductance form, with the two-resistor case recovered | §4.2, box *The general divider* |
| charging and discharging through a resistance: loop equation, <m>q=C\mathcal E(1-e^{-t/\tau})</m>, the general <m>q_\infty-(q_\infty-q_0)e^{-t/\tau}</m> form, <m>\tau=R_{\text{Th}}C</m>, the half-energy-loss ledger, Fig. 4.4 and two folded questions | §4.6 (new) |
| units of electric energy and power: the kWh as the commercial unit, cost arithmetic, eV, Ah, the rated-power trap | §3.4, box *Units ledger* |
| checking the meter-bridge connections before trusting a balance (continuity both ways, null inside the wire, reversal about the null, the copper strips) | §6.3 |

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

* Chapters 1–3 and 6–7 park their questions under a numbered *Questions* section; chapters 4–5 mix them into the
  flow. Both patterns pass the checker; pick whichever suits the chapter you add — but keep every closing block
  numbered (summary then checkpoint; §4.6's questions continue the chapter's own count, Q9 and Q10).
* Equation labels (`data-tag`) are numbered <m>n.1, n.2, \ldots</m> in document order within each chapter and are
  unique; after inserting a section, renumber the rest of that chapter's tags.
* The answer key covers Sections A–C as answers and Section D as headline results, so a marked paper can be
  audited without opening the solutions page.
* The unbalanced bridge (arms 10/20/30/40 Ω, 10 V) is the recurring worked example: nodal (ch 4) → Thevenin/Norton
  (ch 5) → reciprocity swap (ch 5). Keep new examples consistent with its numbers (V_th = 0.952 V, R_th = 23.81 Ω,
  I_sc = 40.0 mA) rather than re-deriving a second bridge.
* The new §4.6 is the only place a capacitor appears in this file. If you extend it, keep the companion note-set's notation (tau = RC, and q(t) = q_inf - (q_inf - q0)exp(-t/tau)) so the two files stay interchangeable.
* Every number in ch 7's scaling laws (fuse 3/2 exponent, transmission 1/V², thermocouple a/2b vs a/b) is derived
  in-text; if you extend ch 7, derive the exponent before quoting it.

## Editing

```bash
python3 tools/mathfix.py      # normalise authoring slips (idempotent)
python3 tools/setpages.py     # page order = filenames (run after adding/renaming a file)
python3 tools/check.py        # ALL GOOD or a list of problems
```

## Deliberately not covered

* **The one-time-constant RC circuit** is derived here in §4.6 because Cengage keeps it in this chapter; the deeper transient machinery (two capacitors, n states, relaxation oscillators, sinusoidal steady state) stays in `capacitors/` ch 6, and RL transients belong to the magnetism note-set.
* **AC circuits, impedance, power factor, three-phase** — a future topic; this set is strictly DC steady state.
* **Magnetic effects of current** (force on wires, Biot–Savart) — belongs to the magnetism note-set.
* **Semiconductor device physics** beyond the diode curve and the thermistor law (no transistor biasing, no
  small-signal models).
* **Superconductivity beyond the DC ledger**: no BCS mechanism, no Josephson junctions, no type-II vortex physics —
  the persistence argument of ch 7 is the whole DC story we need.
* **Circuit simulation / SPICE**: every result in the folder is closed-form and checkable by hand.

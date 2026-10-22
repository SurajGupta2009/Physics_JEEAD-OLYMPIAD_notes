# Verification — representative, not exhaustive

## Automated checks (run on 2026-10-22)

- `test_exports.py`: independent checks of standard COMs and hole trick; P32 master-formula momentum/restitution/energy invariants; corrected Q18; deformation/reformation impulse split; rocket and ballistic-pendulum anchors; moving-wall E9 and C9 angle law; bounce ladder and P31 count; equal-mass 90° triangle; chain-on-scale and peg contact loss; fold; staged rocket ledger; jet optimum; spring ratio; P33. Draft-artefact scan. **Failures: 0.**
- `revalidate.py`: page count/section numbering, unique slugs, 4 cards and 2 diagrams per page; PNG dimensions and DPI; ZIP membership/order; PDF A4 geometry/page count; index links; asset manifest hashes; source SHA prefix; correction signatures. (Run after final export.)
- `render_sheets.py`: all inline math preflighted; diagram text bounds checked; 75 pages rendered without card overflow. Canvas 2480×3508 px at 300 DPI.
- Diagram preflight: 64 distinct schematic/graph panels checked with renderer geometry; zero clipping/label-bound issues.

## Manual spot review

Representative sheets visually inspected: JEE-01 (COM table), JEE-40 (rocket equation) and Olympiad-01 (falling-chain correction). Reviewed density, colour coding, labels, margins, page labels and source lines. Physics spot derivations include P32 by both routes, Q18 energy/momentum, 3mg chain flux, peg detachment and the fold energy law.

## Limits

Not every drill on every sheet was machine-checked. Three of 75 rendered sheets received visual review; kerning/aesthetic review is not exhaustive. The fill statistic is a layout proxy: min/median/max 0.39/0.71/0.93 after safe packing, with lighter continuation cards; body font was not shrunk. These limits are stated rather than claiming exhaustive or perfect verification.

Print A4 portrait, one sheet per page, **Fit to page** — not Fill/Crop (see `PRINTING.md`).

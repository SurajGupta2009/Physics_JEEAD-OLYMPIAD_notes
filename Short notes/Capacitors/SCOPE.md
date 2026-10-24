# Scope of the Capacitors short notes

**Current edition (2026-10-24): JEE Main + Advanced only, 9 sheets.**

This chapter used to be split into 11 "JEE" sheets and 6 "Olympiad / extension"
sheets, with separate bundles for each part. That split is retired. The Olympiad
part was audited item by item against the JEE syllabus; the six ideas that are
genuine JEE **methods** were merged into the JEE pages and everything else was
dropped or handed to the chapter where it actually belongs.

- **Item-by-item decision table:** [AUDIT.md](AUDIT.md)
- **Coverage proof (no JEE topic lost):** AUDIT.md section 3
- **Hand-offs to other chapters:** AUDIT.md section 4
- **Old edition, frozen:** [`legacy/`](legacy) (`sheets-v1-jee-olympiad.json`,
  `render_sheets_v1.py`, `build_exports_v1.py`)

## Why the old split was wrong

"Relevance, not difficulty" was the right instinct but the wrong test. The old
extension set mixed two very different things:

1. **Methods** - a construction that turns a hard JEE question into a short one
   (image charge above a plane, the movable plate, charge sharing on a meter).
   These belong in the main sequence, not in a second part nobody reads.
2. **Extra physics** - Debye relaxation, conformal mapping, ellipsoidal
   depolarising factors, porous-electrode impedance. None of it is examined by
   JEE Main or Advanced, and none of it is needed to solve a JEE question.

Keeping category 2 made the chapter 17 pages and buried category 1 at the end.

## Build

```bash
python3 author_notes.py      # sheets.json from the authored content
python3 render_sheets.py     # 7 A4 PNGs + layout-checks.json
python3 build_exports.py     # PDF, ZIP, README.md, index.html
python3 test_exports.py      # gate: scope, density, print spec, links
```

Requirements: Pillow, numpy, matplotlib, reportlab, pypdf (`requirements.txt`).

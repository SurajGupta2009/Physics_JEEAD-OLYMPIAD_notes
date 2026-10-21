# Magnetism — short notes (37 sheets: 29 JEE + 8 extensions)

Dense teacher-style handwritten revision sheets built from the repository's complete [`magnetism/Magnetism.md`](../../magnetism/Magnetism.md) module (the original chapter is unchanged). Physical meaning, governing equations, short derivations, assumptions, traps and checks — not a formula-only dump. Same format as the other chapters' short notes: navy body, teal headings, yellow result bands, red warnings, faintly ruled white pages.

**Layout:** [index.html](index.html) (offline gallery) · [SCOPE.md](SCOPE.md) coverage and classification · [SOURCE-AUDIT.md](SOURCE-AUDIT.md) corrections · [VERIFICATION.md](VERIFICATION.md) checks · [PRINTING.txt](PRINTING.txt) print settings.

## Downloads

| Deliverable | File |
|---|---|
| **Everything (37 PNGs)** | **[magnetism-all-pngs.zip](magnetism-all-pngs.zip)** |
| All sheets, one A4 page each | [magnetism-short-notes.pdf](magnetism-short-notes.pdf) |
| JEE Main + Advanced (29 sheets) | [magnetism-jee-pngs.zip](magnetism-jee-pngs.zip) · [magnetism-jee.pdf](magnetism-jee.pdf) |
| Olympiad / extensions (8 sheets) | [magnetism-olympiad-pngs.zip](magnetism-olympiad-pngs.zip) · [magnetism-olympiad.pdf](magnetism-olympiad.pdf) |
| Individual sheets | `JEE-01-lorentz.png` … `Olympiad-08-estimates.png` in this folder |

A4 portrait · one sheet per page · print with **Fit**, not Fill/Crop · PNGs are 2480 × 3508 at 300 DPI.

## Reading order

Part I (JEE) first, then Part II. The boundary is syllabus relevance and usefulness, not difficulty: hard core applications (mirrors, drifts, pressure, hysteresis, circuits) stay in JEE; the extensions add relativistic origin, Helmholtz design, demagnetising factors, pinch/levitation engineering, Fermi acceleration, radiation-belt clocks, two-carrier Hall and apparatus estimates.

## Rebuild (fully reproducible)

```bash
pip install -r requirements.txt
python author_content.py     # teacher content -> sheets.json
python render_sheets.py      # -> 37 A4 PNGs + layout-checks.json
python build_exports.py      # -> 3 PDFs + 3 ZIPs + index.html + manifests
python revalidate.py         # -> verification-recheck.json (independent physics checks)
python test_exports.py       # -> verification-results.json (exports, links, models)
```

Licensed font: Patrick Hand (SIL OFL, [fonts/OFL.txt](fonts/OFL.txt)).

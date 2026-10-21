# Sound waves — complete short notes (JEE + Olympiad)

Teacher-style condensed notes for **sound waves**, built from the repository chapter
`sound-waves/Sound-waves.md` (primary source, left unchanged) with independent
equation/sign/limit checking recorded in `SOURCE-AUDIT.md`.

- **Part I — JEE Main + Advanced**: 60 A4 sheets, numbered `JEE-01`…`JEE-60`
- **Part II — Olympiad / specialised extensions**: 24 A4 sheets, numbered `Olympiad-01`…`Olympiad-24`
- 84 sheets total, 336 cards, 168 diagram panels; every sheet 2480×3508 px @ 300 DPI (exact A4 at print)

## Downloads

| File | Contents |
| --- | --- |
| `sound-all-pngs.zip` | all 84 sheets, PNG, reading order (JEE first) |
| `sound-short-notes.pdf` | all 84 sheets, one A4 page each, bookmarks |
| `sound-jee-pngs.zip` / `sound-jee.pdf` | Part I only |
| `sound-olympiad-pngs.zip` / `sound-olympiad.pdf` | Part II only |
| `index.html` | browsable index with per-sheet downloads |

## Coverage (chapter order)

Longitudinal waves and the s–ΔP pair · wave equation and v = √(B/ρ) · rods and bulk
solids · Newton vs Laplace · v(T), molar mass, humidity · intensity, spreading, decibels ·
superposition, Quincke, beats · standing waves, closed/open pipes, end correction,
resonance tube, Kundt's tube · Doppler (source, observer, conventions, wind, 2D,
echo, Mach) · impedance, reflection/transmission, pipes as loads · phasors, energy
and Q · sign-free Doppler · glide-slope ranging · WKB ducts · three solid speeds ·
Mach geometry clinic · acoustic estimation kit.

The JEE/extension boundary follows **syllabus relevance, not difficulty**; hard core
applications stay in Part I. See `SCOPE.md` for the per-sheet classification.

## Layout and colour

Navy body text on white cards; teal titles, WHY and CHECK blocks; yellow equation
chips (inline and display); red WATCH/trap blocks; teal captions under diagrams;
PALE "REMEMBER" band at the foot of every sheet. Body text is 11.5 pt equivalent at
300 DPI and is never shrunk to hide overflow.

## Rebuild (offline)

```
python author_content.py    # sheets.json (content, packing, preflight)
python render_sheets.py     # 84 PNGs + layout-checks.json
python build_exports.py     # PDFs, ZIPs, index.html, manifests
python test_exports.py      # physics checks (representative)
python revalidate.py        # structural checks (representative)
```

Dependencies: Pillow, matplotlib, numpy, reportlab, pypdf (see `build-environment.json`).

## Docs

- `SCOPE.md` — coverage and classification
- `SOURCE-AUDIT.md` — corrections and open assumptions vs the chapter source
- `VERIFICATION.md` — what was checked and how (representative, not exhaustive)
- `PRINTING.md` — print settings

Source chapters under `sound-waves/` are untouched (SHA-256 verified in `revalidate.py`).

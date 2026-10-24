# Phase 0 — Short notes inventory & baseline (frozen)

**Branch:** `arena/eb89ea71-physics-jeead-olympiad-notes` · **Date:** 2026-10-23 · **Source:** all 17 `sheets.json` files under `Short notes/`

## Baseline totals

| Metric | Value |
|---|---|
| Chapters | 17 |
| Total sheets (PNGs) | 652 |
| JEE sheets | 429 |
| Olympiad / extension sheets | 223 |
| Total subtopics (cards / chips) | 2,428 |
| Renderer format A (`cards` in `sheets.json`) | 13 chapters |
| Renderer format B (`chips`/`moves`/`layout`, content in `_content_*.py`) | 4 chapters |

## Per-chapter baseline table

| Chapter | Sheets | JEE | Olympiad | Subtopics | Format | Left-right layout signal |
|---|---|---|---|---|---|---|
| COM-Collisions | 75 | 49 | 26 | 300 | A | `render_sheets.py` 2×2 card grid (x=125 / x=1265) |
| Capacitors | 17 | 11 | 6 | 68 | A | `render_sheets.py` 2×2 card grid |
| Elasticity | 17 | 8 | 9 | 68 | A | `render_sheets.py` 2×2 card grid |
| Electromagnetic_Waves | 18 | 12 | 6 | 72 | A | `render_sheets.py` 2×2 card grid |
| Electrostatics | 37 | 29 | 8 | 148 | A | `render_sheets.py` 2×2 card grid |
| Fluid_Mechanics | 30 | 19 | 11 | 90 | B | `layout:[{main_px},{margin_px}]` main + margin columns |
| Kinematics | 36 | 26 | 10 | 144 | A | `render_sheets.py` 2×2 card grid |
| Magnetism | 77 | 58 | 19 | 308 | A | `render_sheets.py` 2×2 card grid |
| Modern_Physics | 50 | 25 | 25 | 150 | B | `layout:[{main_px},{margin_px}]` main + margin columns |
| Newtons_Laws | 50 | 26 | 24 | 150 | B | `layout:[{main_px},{margin_px}]` main + margin columns |
| Rigid_Body_Dynamics | 23 | 19 | 4 | 92 | A | `render_sheets.py` 2×2 card grid |
| Semiconductors | 18 | 12 | 6 | 72 | A | `render_sheets.py` 2×2 card grid |
| Sound-waves | 84 | 60 | 24 | 336 | A | `render_sheets.py` 2×2 card grid |
| Thermodynamics | 28 | 21 | 7 | 112 | A | `render_sheets.py` 2×2 card grid |
| Units_Dimensions_Errors | 18 | 12 | 6 | 72 | A | `render_sheets.py` 2×2 card grid |
| Wave_Optics | 24 | 16 | 8 | 96 | A | `render_sheets.py` 2×2 card grid |
| Work_Energy_Power | 50 | 26 | 24 | 150 | B | `layout:[{main_px},{margin_px}]` main + margin columns |
| **TOTAL** | **652** | **429** | **223** | **2,428** | | |

## Two renderer formats (both encode the left-right distinction)

### Format A — 13 chapters (`render_sheets.py`)
- `sheets.json` is a flat list; each sheet has `cards:[{title, items:[[kind,text]]}]`, `diagrams`, `takeaway`.
- Subtopics = `cards` (4 cards per sheet fixed).
- Layout: cards placed in a rigid 2×2 grid — left column x=125, right column x=1265; two diagrams side-by-side at the bottom. Body 48 pt; cards fixed 1090×1010 px.

### Format B — 4 chapters (`layout.py`, content in `_content_jee.py` / `_content_oly.py`)
- `sheets.json` is `{"edition","page","dpi","sections","sheets":[...]}`; each sheet has `slug, section, page, title, question, moves, chips, figures, takeaway, file, layout`.
- Subtopics = `chips` per sheet.
- Layout: `layout:[{"sheet":slug,"main_px":N,"main_available":M},{"sheet":slug,"margin_px":N,"margin_available":M,"figure_y":Y,"figure_h":H}]` — explicit main column + margin (side) column = the left-right distinction.

## Phase structure (each phase runs across ALL 17 chapters at once)

- Phase 0 — Inventory & freeze (DONE, this file).
- Phase 1 — Expand concept text across ALL chapters (`sheets.json` + `_content_*.py`).
- Phase 2 — Rewrite renderers to single column across ALL chapters (`render_sheets.py`, `layout.py`).
- Phase 3 — Repack & render ALL chapters (PNGs → combined A4 PDFs → ZIPs).
- Phase 4 — Rebuild indexes across ALL chapters (READMEs + index.html).
- Phase 5 — Validate ALL chapters (test_structure.py + coverage map + print spec).
- Phase 6 — Rollout & sign-off.

## Exit criteria carried into Phase 1+
- Every subtopic (2,428) must be preserved: coverage map `old slug → new sheet(s)`, 1:1, zero deletions.
- Output stays A4 portrait, 300 DPI, safe margins, one sheet per page.
- Single column replaces the left-right grid in both formats.
- Dense + short target: ≈60–70% of current sheet counts after repacking.

## Git state
Committed on `arena/eb89ea71-physics-jeead-olympiad-notes`:
- `1ff401a` Add full redesign plan for Short notes (`Short notes/PLAN-SHORT-NOTES.md`)
- This file: `Short notes/PHASE0-INVENTORY.md` (to be committed next)

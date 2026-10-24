# Short notes redesign plan — dense, short, single-column (all chapters, phase by phase)

**Repo:** `Physics_JEEAD-OLYMPIAD_notes` · **Folder:** `Short notes/` · **Branch:** `arena/eb89ea71-physics-jeead-olympiad-notes`  
**Scope:** all 17 chapters, every phase runs across **all** chapters (no per-chapter pilot repeat).

## 1. The problem (as you stated it)

| What you said | Where it lives in the repo today |
|---|---|
| "I don't want that left-right distinction" | Format A (13 chapters): `render_sheets.py` places 4 cards in a rigid 2×2 grid — left column x=125, right column x=1265; two diagrams side-by-side at the bottom. Format B (4 chapters): `layout.py` stores explicit `main_px` + `margin_px` columns per sheet. |
| "The concept is written in short" | `why`/`trap`/`p`/`chips` items are telegraphic one-liners; symbols appear without being defined. |
| "Not dense" | Body text 48 pt (~11.5 pt eq.), fixed 1090×1010 px cards, only 4 cards + 2 diagrams per A4 sheet. |
| "Not short" | 652 sheets across 17 chapters (Sound-waves 84, Magnetism 77, COM-Collisions 75…). |

## 2. Definition of "perfect" (exit criteria — every one must pass, all chapters)

1. **Single column only.** Every sheet is one vertical stream: header → title → subtitle → stacked full-width cards → full-width diagram(s) → compact takeaway strip → footer. No left/right card split, no side-by-side diagrams, no main/margin split.
2. **Dense.** Body text tightened (target ≈ 40–42 pt equivalent from 48 pt), tighter leading, reduced card padding, cards sized to content rather than fixed boxes, more items per sheet (target ≈ 6–8 cards vs 4 today). Math is **never** shrunk below readability to force a fit.
3. **Short.** Fewest sheets possible per chapter while retaining everything. Greedy vertical repack: stack cards in order; when one doesn't fit, start a new sheet. Target ≈ 60–70 % of today's sheet count per chapter (confirmed after the Phase 3 packing run), driven by density, not by a cap.
4. **Concepts written out.** Every item is a complete sentence; every symbol defined at first use; no telegraphic shorthand; WHY / WATCH labels kept with full explanations.
5. **Zero subtopic loss.** Every card/subtopic in today's `sheets.json` exists in the new sheets; a coverage map (`old slug → new sheet(s)`) proves 100 % retention. Order within a chapter is preserved. **No subtopic is removed to make it shorter.**
6. **Still print-ready.** A4 portrait, 300 DPI (2480 × 3508 px), ≈ 10 mm safe margins, one sheet per page, Fit-to-page printing, Patrick Hand font, grayscale-safe labels.
7. **Outputs.** One canonical combined A4 PDF per chapter (`*-short-notes.pdf`) + PNG gallery + chapter README. JEE and Olympiad remain labeled sections inside **one** sequence (JEE-01… then Olympiad-01…), combined PDF only — no separate JEE/Olympiad bundles.

## 3. What stays / changes / is removed

| | Decision |
|---|---|
| **Keep** | All subtopics, cards, diagrams, takeaways; JEE + Olympiad content; `sheets.json` as editable source; A4 / 300 DPI / print spec; PNG + PDF + ZIP deliveries; section labels; Patrick Hand font; slugs `JEE-NN-…` / `Olympiad-NN-…` stable so tests/links keep working. |
| **Change** | Layout → single column (both formats); typography → denser; concept text → expanded to complete sentences; pagination → greedy vertical repack (fewer sheets); chapter READMEs/indexes updated. |
| **Remove** | Nothing from the physics content. Removed: the two-column card grid, fixed card boxes, side-by-side diagram pairs, separate JEE/Olympiad editions. |

## 4. New sheet design (specification, applies to both formats)

```
+-------------------------------------------------------------+
| CAPACITORS / PART I: JEE MAINS + ADVANCED      07 / 11      |
| Title — full width, wraps as needed                        |
| Subtitle — full width                                      |
+-------------------------------------------------------------+
| CARD 1 — title                                             |
| full-width card; items stacked; math at full column width  |
+-------------------------------------------------------------+
| CARD 2 — title                                             |
| ...                                                        |
+-------------------------------------------------------------+
| DIAGRAM — full width + caption under it                    |
+-------------------------------------------------------------+
| CARD 3 … CARD N (as many as fit)                           |
+-------------------------------------------------------------+
| REMEMBER / takeaway — compact full-width strip             |
| Source  |  A4 portrait / 300 DPI                           |
+-------------------------------------------------------------+
```

Renderer rules (all chapters):
- Card width = full column (`W − 2·margin`). Card height = content height + padding (no fixed box).
- Cards stack in file order. If the next card doesn't fit in remaining space, it starts on the **next** sheet. Cards never split across sheets, never shrunk to hide overflow.
- Diagrams: full width, height scaled proportionally, caption under the diagram.
- Takeaway strip: compact, full width.
- Header: `CHAPTER / PART I: JEE MAINS + ADVANCED` or `PART II: OLYMPIAD / EXTENSIONS`; page `i / n` per section. Combined export = JEE sequence first, then Olympiad sequence.

## 5. Source changes in `sheets.json`

Keep current schema. Expand every short item: rewrite `p`/`why`/`trap`/`chips` as complete sentences; define each symbol at first use (e.g. `k = 1/4πε₀`). Add optional `subtopic` id per card for the coverage map.

**Freeze during this work:** no item deleted, no diagram deleted, no card/chip deleted — only text expanded and layout repacked.

## 6. Repacking algorithm (how "short" is achieved without deleting anything)

1. Parse each chapter's `sheets.json`; estimate each card's height from wrapped line count × leading + item gap at target body size; math items use unshrunk rendered height.
2. Greedy vertical stack per sheet: place cards in file order; when `y + card_height > card_zone_bottom`, close the sheet and start a new one.
3. Diagrams travel with their sheet as full-width strips; renumber `part_page` per section (JEE-01…, then Olympiad-01…).
4. Regenerate `layout-checks.json` per chapter with density stats (items per sheet, sheets before → after).
5. Coverage map: every old slug rendered exactly once (`old slug ⊆ new slugs`, 1:1). Any mismatch stops the release.

## 7. Execution plan — phases, each across ALL chapters

**Phase 0 — Inventory & freeze (DONE).** Listed every chapter's cards/subtopics from `sheets.json`; snapshot baseline sheet counts; recorded baseline in `PHASE0-INVENTORY.md`. Zero changes to content.

**Phase 1 — Expand concept text across ALL chapters.** Rewrite short items into complete sentences with symbol definitions in all 17 `sheets.json` files (Format A: `cards.items`; Format B: `_content_jee.py` / `_content_oly.py` chips). Physics check; zero deletions.

**Phase 2 — Rewrite renderers to single column across ALL chapters.** Rework `render_sheets.py` (Format A) and `layout.py` (Format B) into the single-column engine: full-width cards/diagrams/takeaway, overflow assertions kept, no-shrink rule kept, `layout-checks.json` density report. Apply uniformly to all 17 chapters.

**Phase 3 — Repack & render ALL chapters.** Run the new renderer over all chapters; regenerate PNGs → combined A4 PDFs → ZIPs; rebuild every `layout-checks.json`.

**Phase 4 — Rebuild indexes across ALL chapters.** Update each chapter's `README.md` + `index.html`, plus `Short notes/README.md` and `Short notes/index.html`, with new sheet counts and the single combined download per chapter.

**Phase 5 — Validate ALL chapters.** Updated `test_structure.py`: single-column check, coverage map (100 % retention), page counts (PDF pages == PNG count), 3 PDFs + 3 ZIPs per chapter, density report vs targets, print-spec spot check (A4 media box, 300 DPI, margins), link audit across READMEs/index.html.

**Phase 6 — Rollout & sign-off.** Per-chapter before/after comparison (sheets, cards per sheet); commit; present diff for review.

## 8. Validation tests (changes to `test_structure.py`)

Keep all existing assertions, and add:

- **Single column:** every card's x-position identical across a sheet; every diagram spans full column width.
- **Coverage map:** old slugs ⊆ new rendered slugs, exactly one render per old slug (zero subtopic loss).
- **Page count:** combined `*-short-notes.pdf` pages == PNG count; 3 PDFs + 3 ZIPs per chapter.
- **Density report:** printed per chapter — sheets before → after, average cards per sheet; must show net reduction with 100 % card retention.
- **Print spec:** A4 media box 210 × 297 mm, 300 DPI, safe margins present.

## 9. Metrics & targets (baseline → target)

Current baseline (all chapters, from `sheets.json`):

| Chapter | Sheets today | Subtopics today | Target sheets (planning estimate, no hard cap) |
|---|---|---|---|
| Capacitors | 17 | 68 | ≈ 10–12 |
| Elasticity | 17 | 68 | ≈ 10–12 |
| Electromagnetic_Waves | 18 | 72 | ≈ 11–13 |
| Units_Dimensions_Errors | 18 | 72 | ≈ 11–13 |
| Work_Energy_Power | 50 | 150 | ≈ 30–35 |
| Thermodynamics | 28 | 112 | ≈ 17–20 |
| Kinematics | 36 | 144 | ≈ 22–26 |
| Fluid_Mechanics | 30 | 90 | ≈ 18–22 |
| Newtons_Laws | 50 | 150 | ≈ 30–35 |
| Modern_Physics | 50 | 150 | ≈ 30–35 |
| Magnetism | 77 | 308 | ≈ 45–55 |
| COM-Collisions | 75 | 300 | ≈ 45–55 |
| Sound-waves | 84 | 336 | ≈ 50–60 |
| Semiconductors | 18 | 72 | ≈ 11–13 |
| Wave_Optics | 24 | 96 | ≈ 14–17 |
| Rigid_Body_Dynamics | 23 | 92 | ≈ 14–17 |
| Electrostatics | 37 | 148 | ≈ 22–26 |
| **TOTAL** | **652** | **2,428** | **≈ 390–460** |

Success check after Phase 5: **cards per sheet rises from 4 → ≈ 6–8**, **sheets per chapter falls ≈ 30–40 %**, **coverage map = 100 %**, **zero abbreviated concepts**.

## 10. Rules that cannot change during this work

- No subtopic, card, diagram, or takeaway is deleted to make the notes shorter (your constraint).
- Math is never shrunk below readable size to force a fit.
- Print spec unchanged: A4 portrait, 300 DPI, safe margins, one sheet per page.
- All 17 chapters are rebuilt consistently in every phase; no chapter left in the old two-column edition.
- Combined PDF only — no separate JEE/Olympiad bundles (your decision). No hard sheet cap (your decision).

## 11. Decisions confirmed

- **Bundles:** combined-only, no separate JEE/Olympiad PDF/ZIP bundles.
- **Screen edition:** PNG/PDF only, no separate Markdown edition.
- **Hard cap:** none — sheet count is free, driven by relevance and density.

---
*Prepared on `arena/eb89ea71-physics-jeead-olympiad-notes`. Baseline: 17 chapters, 652 sheets, two-column card grid, 48 pt body text.*

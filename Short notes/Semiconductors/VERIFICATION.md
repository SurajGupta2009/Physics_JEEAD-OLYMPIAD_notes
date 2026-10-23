# Verification Report — Semiconductors & Electronic Devices Short Notes

## Automated Verification Summary

| Check Suite | Scope | Result |
|---|---|---|
| **Canvas, Margin & Card Density (`render_sheets.py` / `layout-checks.json`)** | All `18` PNGs (`2480 x 3508 px`, 300 DPI, 8-colour palette, quiet outer margins `>= 124 px`) and all `72` cards (`560 <= used_px <= 1038`) | **PASS (`18/18` sheets, `72/72` cards)** |
| **9-Way Geometric Collision Auditor (`diagrams.py`)** | Canvas bounds, `Text-Text`, `Legend-Text`, `Legend-Line`, `FancyArrowPatch/Arc/Circle/FancyBboxPatch/Rectangle/Polygon.get_verts()-Text`, and `ax.lines-Text` across all `36` analytic panels | **PASS (`0` collisions across `36/36` panels)** |
| **Lossless PDF, ZIP & Manifest Verification (`test_exports.py`)** | Page counts (`18`, `12`, `6`), A4 MediaBox, PDF outlines, SHA-256 raw pixel equality between every PDF page stream and its source PNG, ZIP byte identity, local links, and numerical semiconductor physics models | **PASS (`100%`)** |
| **Physics Hygiene & Source-Audit Recheck (`revalidate.py`)** | Zero draft/self-talk strings, zero split-equation orphans, presence of all `16` core semiconductor formulas, exact numerical verification of all `5` `SOURCE-AUDIT.md` resolutions | **PASS (`36` checks)** |
| **Source Immutability (`git diff semiconductors/Semiconductors.md`)** | Read-only primary source check | **PASS (`0` bytes changed)** |

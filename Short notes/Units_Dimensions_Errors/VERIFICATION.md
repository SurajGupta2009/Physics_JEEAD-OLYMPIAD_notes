# Verification — Units, Dimensions & Measurement Errors Short Notes

Automated checks enforced on every build (`render_sheets.py`, `revalidate.py`, `test_exports.py`):
- **Geometry & Margins:** All 18 PNGs verified at exact `2480 × 3508` px (`300 DPI`), indexed `mode == 'P'`, zero `tRNS`, and pure `(255, 255, 255)` quiet outer margin $\ge 125\text{ px}$ on all four sides.
- **Card Typography & Fill:** All 72 cards verified free of unmapped glyphs, horizontal equation squash ($< 0.80$), vertical card overflow ($> 1038\text{ px}$), and sparse underfill ($< 560\text{ px}$).
- **Diagram Bounding-Box Gate:** All 36 Matplotlib figures checked automatically for zero canvas clipping and zero pairwise text bounding-box overlap.
- **Lossless PDF & ZIP Integrity:** All 3 PDFs verified for exact page counts (`18`, `12`, `6`), A4 media boxes, bookmark trees, and byte-exact decompressed pixel SHA-256 parity against every source PNG; all 3 ZIPs verified for ordered membership and byte parity.

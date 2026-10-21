# Verification

**Fresh full export and structural checks: PASS.** Exact current counts are in the machine-readable report below; 56 representative physics/model checks are included in that suite.

The final run is recorded in [verification-results.json](verification-results.json). Tests are representative, not a proof of every statement.

## Automated checks

- 37 independently numbered sheets: 29 JEE then 8 extensions; 148 cards, 74 unique diagram identifiers, 257 mathematical blocks.
- Every PNG: 2480 × 3508, 300 DPI metadata, safe ink bounds and no stale images.
- Every card: measured content fits; body remains 11.52 pt, explanations/warnings 11.04 pt. No body shrinking to hide overflow. See [layout-checks.json](layout-checks.json).
- Mathtext preflight uses the same syntax normalisation as rendering. Handwriting glyph coverage includes body, headings, subtitles, metadata and takeaways. Figure annotations, ticks and legends have bounds guards.
- Three PNG-only ZIPs: CRC, order and byte identity to source PNGs.
- Three exact A4 PDFs: 37/29/8 pages, ordered correct-title bookmarks and destinations, one full-resolution source image per page. Decoded source pixel indices AND palettes match exactly, so this is lossless embedding, not screenshot/downsampling.
- Gallery/download/document links resolve locally. Shared chapter-folder structure check passes. PNGs and PDFs sit directly in the chapter folder with JEE-/Olympiad- prefixes.
- [asset-manifest.json](asset-manifest.json) records SHA-256/length of all 37 PNGs and six exports; [build-environment.json](build-environment.json) records actual libraries.
- Original detailed source SHA-256 unchanged. The separate stage-3 source gate passes with its structural/media counts; it does not independently certify the physics.

56 numerical/model checks include signed vector force, null positions, ring maxima/SHM and numerical in-plane sign, finite rods, disc/dipole limits, beam deflection, independent rectangular surface-flux quadrature, sphere/slab laws, energy pair counts and sphere sharing, extended self-energy, image charge/force/energy integrals, bubble/drop scales, endpoint coalescence energy, quadrupole asymptotics, converged cube quadrature and dome scales. Numerical expectations are in the machine-readable report.

## Visual review

All 37 page compositions were inspected in seven page montages; all 74 figure panels were inspected separately in five larger montages. Full-resolution samples cover demanding math/geometry pages. This is not a claim that every page was inspected word-by-word at full resolution. Crowded radius/surface labels were moved, long axis labels were typeset compactly, and legend backgrounds made opaque for legibility. A dedicated 115 px caption band prevents two-line captions from colliding with tall axis labels; all 74 panels pass the resulting tighter drawing bounds. Final bounds and exports were rechecked after these changes.

## Limits and publication

See [SOURCE-AUDIT.md](SOURCE-AUDIT.md) and [SCOPE.md](SCOPE.md). No exhaustive perfection guarantee, official-current-syllabus/frequency claim, exact real-material breakdown limit or engineering safety verdict is offered. Mechanical and boundary-model constraints matter. The user explicitly authorised re-verification and publication to main. Work is committed/pushed on the session branch and published through a PR merge, then the remote main chapter subtree is compared with the verified local subtree. Other chapter deliverables and the original detailed electrostatics source are preserved.

Printing: **A4 portrait, one sheet per page, Fit—not Fill/Crop**.

## Fresh pre-publication recheck — 2026-10-21

- Re-ran authoring, rendering and export from editable sources. All 37 PNGs, `sheets.json` and `layout-checks.json` reproduced byte-for-byte against their pre-rebuild SHA-256 values. Rebuilt PDF metadata may change; decoded source pixels and palettes remain exact.
- Re-ran the complete export suite, shared folder/link gate and original electrostatics stage-3 source gate. Checked modified navigation and Git whitespace integrity.
- Added `revalidate.py`: **94 additional independent model checks**, using direct Gaussian quadrature, finite-difference gradients, component sums, grounded/isolated sphere boundary residuals, image-force/energy consistency and numerical convergence. Results: [verification-recheck.json](verification-recheck.json). These supplement rather than replace the 56 original model checks.
- Re-inspected all 37 page compositions in seven newly generated montages and all 74 diagram panels in five new figure montages. Bounds/glyph/math checks cover every final page; this does not claim exhaustive full-resolution word-by-word inspection.
- No new content or physics correction was needed in this recheck; the approved PNG content is unchanged. Verification remains representative, not an exhaustive correctness guarantee.

# VERIFICATION — Magnetism + EMI + AC short notes

What was checked on the delivered sheets. Checks are representative and precise about what they cover; they are **not** exhaustive certification of every statement.

## Machine-readable results

- [verification-results.json](verification-results.json) — full export/layout/content/link suite with every numerical model value.
- [verification-recheck.json](verification-recheck.json) — independent pre-publication physics revalidation (quadrature, derivatives, ODE orbits, boundary residuals, convergence).

## Export, layout and content suite (`test_exports.py`)

**PASS — 2,717 assertions, including 111 representative physics/model checks.** Machine-readable detail in [verification-results.json](verification-results.json). The suite includes, in order:

- Structure: 77 pages in reading order (58 JEE then 19 Olympiad), unique names, 308 cards, 154 diagram identifiers, 514 math blocks; per-section numbering 1..58 and 1..19; no stale pages.
- Font coverage of every prose glyph; body 11.52 pt and explanations 11.04 pt never shrunk; every card fits its box (layout manifest). Density is packed and balanced: card fill measured in pixels sits in a narrow band near capacity (final run: minimum ≈ 854, median ≈ 941, maximum ≈ 1011 of ≈ 1040 px available; no card under-filled or overflowing).
- Every PNG: 2480 × 3508 px, ~300 DPI metadata, indexed palette, ink within the 125 px safe margin on all sides.
- 3 ZIPs: CRC clean, PNG-only entries in reading order, byte-identical to source PNGs.
- 3 PDFs: exact A4 portrait pages, one sheet per page, one lossless indexed image per page (decoded pixels and palette byte-identical to the source PNG), ordered bookmarks with page destinations and titles.
- Offline gallery: 77 articles, every link resolves; documentation links resolve (except this report itself, written by the run); all exported assets match the SHA-256 manifest.
- Both original detailed chapters are byte-unchanged: `magnetism/Magnetism.md` (SHA-256 `86d3deb0ac086e68b20644eaf24626a87c18510aad8843b1575d62d7a00f9bba`) and `emi-ac/Emi-ac.md` (SHA-256 `7699e1bef3a7926819c5b60a7ba0703f960fcb5a29dcced4dcebd38a06ce998e`).
- 111 representative physics/model checks evaluated numerically in-suite. Magnetism: Lorentz circles and helices, selector, strip timing and return, spectrometer and isotopes, cyclotron frequency/energy/turns, mirror loss cone, Hall voltages and balance, drifts and cycloids, Thomson e/m, 300 Br rule, moving-charge identity B = v×E/c², finite/infinite/semi-infinite wires, square/hexagon centres, loop/axis/arc, solenoid interior and end, toroid, Ampère ledger, thick wire, sheets, overlap hole, chord theorem, couple and U-gradient identity, wire forces, pressure/energy density, gyromagnetic ratio and Bohr magneton, rotating disc, magnetised sphere, Larmor susceptibility, Curie scaling, exchange-vs-dipole scale, hysteresis loss, magnetic circuits, Earth components and dip–latitude identity, Gauss absolute method, Helmholtz factor/field/uniform length, synchrotron radius and frequency, radiation-belt gyration, Fermi gain, two-carrier Hall including the sign flip, levitation height and force balance, pinch/lightning numbers, relativistic ratio. EMI/AC: reactances and LCR impedance/current/phase/resonance of the worked 230 V example, radio-tank C and Q, RL interruption kick, LC natural frequency and current amplitude, rectified mean 2/π and RMS 1/√2, transformer turns ratio and reflected impedance, transmission-loss ratio, rail-rod coasting time constant, terminal speed of the hanging-mass rod and the energy audit, Faraday-disc EMF, betatron orbit radius and the 2:1 rule, coax line speed from L′C′ and the Z₀ geometry factor, Wien β = 1/3 at ωRC = 1, matched-load power identity.

## Independent physics revalidation (`revalidate.py`)

**PASS — 89 checks.** Deliberately re-derives results without reusing the sheets' closed forms where practical: Biot–Savart angle quadrature; ring/loop axis fields from element sums; arc, square and hexagon centres as wire sums; stacked-loop solenoid quadrature versus the cosine formula at midplane, off-centre and at the end face; Ampère ledger identities (thick wire, sheets, hole, toroid); force/torque/energy identities by numerical differentiation; pressure and energy-density integrals; magnetised-sphere interior and exterior pole continuity; susceptibility scalings; hysteresis loop area; magnetic-circuit residuals; Earth dipole identities; Helmholtz flatness from the exact axial field; orbit integrations for drifts/cycloids; two-carrier Hall algebra; levitation force balance; and convergence of each quadrature under refinement. Detail in [verification-recheck.json](verification-recheck.json).

## Visual inspection (representative)

Rendered sheets were inspected by eye for density, overlap, clipping and diagram geometry, including the reworked densest and trimmed cards, and new EMI/AC sheets across both parts (e.g. JEE-01, JEE-33, JEE-41, JEE-53, JEE-55, Olympiad-09). All 154 diagram panels pass the automated caption/label clipping checks in `render_sheets.diagram`. Inspection is representative, not a per-pixel audit of all 77 sheets.

## Print

A4 portrait, one sheet per page, **Fit — not Fill/Crop** (see [PRINTING.txt](PRINTING.txt)).

## Statement

The suite is precise about what it covers and does not claim exhaustive certification of every sentence, diagram or exam context of the sheets or of the source chapters.

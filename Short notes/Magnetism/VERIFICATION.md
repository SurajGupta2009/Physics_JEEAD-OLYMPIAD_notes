# VERIFICATION — Magnetism short notes

What was checked on the delivered magnetism sheets. Checks are representative and precise about what they cover; they are **not** exhaustive certification of every statement.

## Machine-readable results

- [verification-results.json](verification-results.json) — full export/layout/content/link suite with every numerical model value.
- [verification-recheck.json](verification-recheck.json) — independent pre-publication physics revalidation (quadrature, derivatives, ODE orbits, boundary residuals, convergence).

## Export, layout and content suite (`test_exports.py`)

**PASS — 1,366 assertions, including 85 representative physics/model checks.** Machine-readable detail in [verification-results.json](verification-results.json). The suite includes, in order:

- Structure: 37 pages in reading order (29 JEE then 8 Olympiad), unique names, 148 cards, 74 diagram identifiers, 244 math blocks; per-section numbering 1..29 and 1..8; no stale pages.
- Font coverage of every prose glyph; body 11.52 pt and explanations 11.04 pt never shrunk; every card fits its box (layout manifest).
- Every PNG: 2480 × 3508 px, ~300 DPI metadata, indexed palette, ink within the 125 px safe margin on all sides.
- 3 ZIPs: CRC clean, PNG-only entries in reading order, byte-identical to source PNGs.
- 3 PDFs: exact A4 portrait pages, one sheet per page, one lossless indexed image per page (decoded pixels and palette byte-identical to the source PNG), ordered bookmarks with page destinations and titles.
- Offline gallery: 37 articles, every link resolves; documentation links resolve (except this report itself, written by the run); all 43 exported assets match the SHA-256 manifest.
- The original detailed chapter `magnetism/Magnetism.md` is byte-unchanged (SHA-256 `86d3deb0ac086e68b20644eaf24626a87c18510aad8843b1575d62d7a00f9bba`).
- 85 representative physics/model checks evaluated numerically in-suite: Lorentz circles and helices, selector, strip timing and return, spectrometer and isotopes, cyclotron frequency/energy/turns, mirror loss cone, Hall voltages and balance, drifts and cycloids, Thomson e/m, 300 Br rule, moving-charge identity B = v×E/c², finite/infinite/semi-infinite wires, square/hexagon centres, loop/axis/arc, solenoid interior and end, toroid, Ampère ledger, thick wire, sheets, overlap hole, chord theorem, couple and U-gradient identity, wire forces, pressure/energy density, gyromagnetic ratio and Bohr magneton, rotating disc, magnetised sphere (interior, moment, pole continuity), Larmor susceptibility, Curie scaling, exchange-vs-dipole temperature scale, hysteresis loss, magnetic circuits, Earth components and dip–latitude identity, Gauss absolute method, Helmholtz factor/field/uniform length, synchrotron radius and frequency, radiation-belt gyration, Fermi gain, two-carrier Hall including the sign flip, levitation height and force balance, pinch/lightning numbers, relativistic ratio.

## Independent physics revalidation (`revalidate.py`)

**PASS — 89 checks.** Deliberately re-derives results without reusing the sheets' closed forms where practical:

- Biot–Savart angle quadrature for finite wires (signed end angles, infinite/semi-infinite limits).
- Ring/loop axis field from element sums; arc proportionality; square and hexagon centres as wire sums.
- Stacked-loop solenoid quadrature versus the cosine formula at midplane, off-centre and at the end face.
- Ampère ledger identities: thick-wire continuity and half-radius rule, sheet and two-sheet fields, hole field, toroid.
- Boris-push Lorentz orbit integration: closed orbit after one period, radius = mv/qB, speed conservation, cycloid x-drift and arch height versus closed form.
- Hall force-balance residual and both voltage examples; two-carrier Hall including R_H = 0 at n/p = (μp/μn)² and the intrinsic-germanium value.
- Dipole field identities; loop far-field convergence to the dipole; torque = −dU/dθ and couple from side forces; zero net force on a closed loop.
- Wire forces, magnetic pressure and end force, hoop stress, chord theorem.
- Gyromagnetic ratio of a ring, Bohr magneton, rotating-disc field.
- Magnetised sphere by direct surface-current ring integration (B_in = ⅔μ₀M), moment = MV, pole-exterior continuity, cylinder/sphere contrast.
- Larmor water susceptibility, Curie tanh limits, dipole-coupling temperature, exchange T_c, hysteresis power.
- Magnetic circuits (filled core and gap formula), Earth components, dip–latitude identity and dipole-strength factor, dipole moment, Gauss method, core current.
- Helmholtz: midpoint field, flatness coefficient 144/125 from finite differences, zero second derivative at d = R and non-zero curvature at d = 1.6 R, cancellation current.
- Relativity ratio F_m/F_e and the moving-charge identity; synchrotron, belt clocks, Fermi gain; levitation height and image-force balance; lightning channel and pinch; slab support field.

## Corrections this verification produced

- One genuine source numerical slip found and corrected in the sheets (OL3 magnetised-sphere moment for R = 1 cm, M = 10⁶ A/m: μ = MV = 4.19 A m², and B(5R) = 6.7 mT; the source's 0.52 A m² is inconsistent with its own pole-continuity check). Recorded in [SOURCE-AUDIT.md](SOURCE-AUDIT.md).
- An independent scratch calculation initially disputed the OL9 germanium Hall value; re-derivation confirmed the source is right (−7.2 × 10⁻³ m³ C⁻¹) and the scratch check was corrected, not the content.

## Visual and source review

- All 37 page compositions were inspected in rendered montages; all 74 diagram panels passed the automated bounds/tick/legend clipping guards at render time. Diagram text clipping, overlapping ticks, mathtext failures and card overflow are automated hard failures during rendering.
- The detailed source chapter's theory, traps and extension sections were read before authoring (see SOURCE-AUDIT). This is not a claim that every source sentence was independently certified.

## Reproduce

```bash
python author_content.py && python render_sheets.py && python build_exports.py
python revalidate.py && python test_exports.py
```

All checks reported here were run in one session against the delivered files.

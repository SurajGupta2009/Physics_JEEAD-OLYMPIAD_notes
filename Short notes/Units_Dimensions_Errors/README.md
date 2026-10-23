# Units, Dimensions & Measurement Errors — explanatory handwritten short notes

**18 complete A4 sheets: 12 JEE Main + Advanced (`JEE-01`–`JEE-12`), then 6 Olympiad / specialised extensions (`Olympiad-01`–`Olympiad-06`).**
72 concept cards and 36 native analytic diagrams/graphs. Built from [`units-measurements/Units-measurements.md`](../../units-measurements/Units-measurements.md) without modifying the detailed source chapter.

## Downloads

| Deliverable | File |
|---|---|
| **Combined A4 PDF (all 18 sheets, bookmarked)** | **[`units-dimensions-errors-short-notes.pdf`](units-dimensions-errors-short-notes.pdf)** |
| **All PNGs bundle (18 sheets)** | **[`units-dimensions-errors-all-pngs.zip`](units-dimensions-errors-all-pngs.zip)** |
| Part I — JEE Main + Advanced (12 sheets) | [`units-dimensions-errors-jee.pdf`](units-dimensions-errors-jee.pdf) · [`units-dimensions-errors-jee-pngs.zip`](units-dimensions-errors-jee-pngs.zip) |
| Part II — Olympiad / extensions (6 sheets) | [`units-dimensions-errors-olympiad.pdf`](units-dimensions-errors-olympiad.pdf) · [`units-dimensions-errors-olympiad-pngs.zip`](units-dimensions-errors-olympiad-pngs.zip) |
| Offline gallery | [`index.html`](index.html) |

Supporting notes: [`SCOPE.md`](SCOPE.md) · [`SOURCE-AUDIT.md`](SOURCE-AUDIT.md) · [`VERIFICATION.md`](VERIFICATION.md) · [`PRINTING.txt`](PRINTING.txt) · Font license: [`fonts/OFL.txt`](fonts/OFL.txt).

## Sheet index

### Part I — JEE Main + Advanced
1. [`JEE-01-si-foundations.png`](JEE-01-si-foundations.png) — Physical quantities, 2019 SI constants, angles & CGS scaling
2. [`JEE-02-dimensional-mechanics.png`](JEE-02-dimensional-mechanics.png) — Dimensional formulae I: mechanics, fluids, rotation & thermal
3. [`JEE-03-dimensional-em.png`](JEE-03-dimensional-em.png) — Dimensional formulae II: electromagnetism & fast composite shortcuts
4. [`JEE-04-homogeneity.png`](JEE-04-homogeneity.png) — Principle of homogeneity, transcendental gates & hidden constants
5. [`JEE-05-dimensional-derivation.png`](JEE-05-dimensional-derivation.png) — Scaling derivations, custom `[F, V, T]` bases & Planck scales
6. [`JEE-06-sig-figs.png`](JEE-06-sig-figs.png) — Significant figures, decimal vs digit rounding rules & guard digits
7. [`JEE-07-error-types.png`](JEE-07-error-types.png) — Error classification, accuracy vs precision, MAE vs $\sigma / \sqrt{n}$
8. [`JEE-08-error-propagation.png`](JEE-08-error-propagation.png) — Error propagation, cancellation & parallel/lens coupled differentials
9. [`JEE-09-vernier-caliper.png`](JEE-09-vernier-caliper.png) — Vernier callipers: standard, general $(1 - m/n)\,\mathrm{MSD}$ & retro-vernier
10. [`JEE-10-screw-gauge.png`](JEE-10-screw-gauge.png) — Screw gauge, zero offset, spherometer & Young's modulus budget
11. [`JEE-11-graphs-fermi.png`](JEE-11-graphs-fermi.png) — Graph linearisation, bounding lines, Fermi estimation & oleic film
12. [`JEE-12-master-triage.png`](JEE-12-master-triage.png) — Master triage, continuous $N$-swing $1/N$ gain & top JEE traps

### Part II — Olympiad / Specialised Extensions
1. [`Olympiad-01-buckingham-pi.png`](Olympiad-01-buckingham-pi.png) — Buckingham $\Pi$ theorem via matrix rank, capillary-gravity waves & Bohr scales
2. [`Olympiad-02-scaling-similarity.png`](Olympiad-02-scaling-similarity.png) — Dynamical similarity ($\mathrm{Re}, \mathrm{Fr}, \mathrm{Ma}, \mathrm{We}$), scale models & allometry
3. [`Olympiad-03-least-squares.png`](Olympiad-03-least-squares.png) — Ordinary & weighted least-squares regression ($b, a, \sigma_b, \sigma_a$)
4. [`Olympiad-04-chi-square.png`](Olympiad-04-chi-square.png) — $\chi^2 / \nu$ goodness-of-fit, weighted mean & covariance propagation
5. [`Olympiad-05-poisson-counting.png`](Olympiad-05-poisson-counting.png) — Poisson shot noise $\sqrt{N}$, exact background subtraction & dead time
6. [`Olympiad-06-experiment-design.png`](Olympiad-06-experiment-design.png) — Precision $0.1\%$ $g$-measurement design, pendulum systematics & natural units

## Rebuild

```bash
python3 -m pip install -r "Short notes/Units_Dimensions_Errors/requirements.txt"
python3 "Short notes/Units_Dimensions_Errors/author_content.py"
python3 "Short notes/Units_Dimensions_Errors/render_sheets.py"
python3 "Short notes/Units_Dimensions_Errors/build_exports.py"
python3 "Short notes/Units_Dimensions_Errors/revalidate.py"
python3 "Short notes/Units_Dimensions_Errors/test_exports.py"
```

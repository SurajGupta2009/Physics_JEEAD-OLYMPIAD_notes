# Electrostatics — complete explanatory image short notes

**37 A4 sheets: 29 JEE Main + Advanced, followed by 8 Olympiad/specialised extensions.**
148 concept cards and 74 native labelled diagram panels. Theory, equations, derivations, physical meaning, assumptions, checked examples and examiner traps are kept together. No arbitrary page cap or body-font compression was imposed. This is a comprehensive revision spine for the consolidated electrostatics chapter, not a verbatim copy of every worked exercise or a replacement for the detailed course.

## Downloads

| Edition | Original PNG ZIP | Bookmarked A4 PDF |
|---|---|---|
| JEE — read first (29) | [JEE PNGs](electrostatics-jee-pngs.zip) | [JEE PDF](electrostatics-jee.pdf) |
| Specialised extensions (8) | [Extension PNGs](electrostatics-olympiad-pngs.zip) | [Extension PDF](electrostatics-olympiad.pdf) |
| Combined (37), JEE first | [Complete PNG ZIP](electrostatics-all-pngs.zip) | [Combined PDF](electrostatics-short-notes.pdf) |

[Offline gallery](index.html) · [Scope/membership](SCOPE.md) · [Source corrections](SOURCE-AUDIT.md) · [Verification](VERIFICATION.md) · [Printing](PRINTING.txt)

Primary source: [Electrostatics.md](../../electrostatics/Electrostatics.md). Companion: [Capacitors short notes](../Capacitors/README.md). Detailed chapter text and all existing chapter deliverables are preserved. Corrections are explicit, not silently written into the original source.

## Format

Original PNGs and PDFs sit directly in `Short notes/Electrostatics/`. `JEE-01` through `JEE-29` and `Olympiad-01` through `Olympiad-08` preserve independently numbered parts. The combined archive/PDF orders JEE first.

2480 × 3508 px, embedded 300 DPI, A4 portrait, ~10.6 mm safe inset. White background, navy prose, teal explanations/headings, yellow mathematical results, red cautions. Handwriting prose is 11.52 pt; explanations/warnings 11.04 pt. Equations use genuine mathematical typesetting. Native graphs use analytical curves or documented numerical quadrature; schematics label the physical geometry. These are generated note images, not AI-painted mathematical text.

Print **A4 portrait, one page per sheet, Fit—not Fill/Crop**. PNG ZIPs contain PNGs only. Download the whole folder to use its offline gallery/fonts. Raster note sheets do not provide a searchable/accessibly transcribed course; use the detailed Markdown for text reading and editable original diagrams.

## Reproduce

From the repository root, after creating your preferred Python virtual environment:

```bash
python -m pip install -r "Short notes/Electrostatics/requirements.txt"
python "Short notes/Electrostatics/author_content.py"
python "Short notes/Electrostatics/render_sheets.py"
python "Short notes/Electrostatics/build_exports.py"
python "Short notes/Electrostatics/test_exports.py"
python "Short notes/Electrostatics/revalidate.py"
python "Short notes/test_structure.py"
python electrostatics/tools/check.py
```

`author_content.py` writes editable `sheets.json`; `diagrams.py` supplies all 74 page-specific panels. `layout-checks.json` stores measured card bounds; `asset-manifest.json` stores exported-asset hashes. Exact library versions are recorded in `build-environment.json`; ranges are in `requirements.txt`. PDF metadata/timestamps may change across builds: content, pixels, order and links are checked, not cross-environment byte-identical metadata. Font: Patrick Hand, [SIL OFL](fonts/OFL.txt).

Publication was explicitly authorised after a fresh verification pass. The complete chapter, source/build tools, tests and all six bundles are included in the publication PR. See [verification and recheck record](VERIFICATION.md).

## Page index

### JEE

1. [Charge: conservation before calculation](JEE-01-charge.png)
2. [Coulomb forces: signed vectors](JEE-02-coulomb.png)
3. [Equilibrium is not stability](JEE-03-equilibrium.png)
4. [From charge density to a field](JEE-04-field-density.png)
5. [Charged ring: one integral, many checks](JEE-05-ring.png)
6. [Finite rods: components before limits](JEE-06-rod.png)
7. [Arcs, gaps and angular density](JEE-07-arc.png)
8. [Disc and annulus: build with rings](JEE-08-disc.png)
9. [Dipole: exact first, far field second](JEE-09-dipole-field.png)
10. [Dipole in a field: force, torque, energy](JEE-10-dipole-action.png)
11. [Charges moving in uniform fields](JEE-11-motion.png)
12. [Electrical forces in mechanical constraints](JEE-12-mechanics.png)
13. [Flux: a signed geometric count](JEE-13-flux.png)
14. [Flux through cubes: symmetry has limits](JEE-14-flux-cube.png)
15. [Use Gauss: choose a surface, justify E](JEE-15-gauss.png)
16. [Spherical shells and solid spheres](JEE-16-spheres.png)
17. [Nonuniform spheres and empty cavities](JEE-17-cavity-superposition.png)
18. [Cylinders, lines and coaxial regions](JEE-18-cylinders.png)
19. [Sheets and conducting plates: three regions](JEE-19-sheets.png)
20. [Charged slabs: field, potential, subtraction](JEE-20-slab.png)
21. [Conductors: field-free does not mean chargeless](JEE-21-conductor.png)
22. [Conducting cavities: induced charge ledgers](JEE-22-conducting-cavity.png)
23. [Potential and work: fix the reference](JEE-23-potential.png)
24. [Potentials of distributions: integrate once](JEE-24-potential-distributions.png)
25. [Read E, charge and stability from V](JEE-25-gradient.png)
26. [Energy of charge systems: count pairs once](JEE-26-mutual-energy.png)
27. [Connected spheres and charge sharing](JEE-27-sharing.png)
28. [Concentric conductors and earthing](JEE-28-concentric.png)
29. [Field energy, self-energy and physical scales](JEE-29-self-energy.png)

### Olympiad

1. [Earnshaw and the ring saddle](Olympiad-01-laplace.png)
2. [Images I: a grounded conducting plane](Olympiad-02-image-plane.png)
3. [Images II: spherical conductor boundaries](Olympiad-03-image-sphere.png)
4. [Pressure, hemispheres and charged bubbles](Olympiad-04-pressure-bubble.png)
5. [Drops: shape instability and coalescence](Olympiad-05-drops.png)
6. [Multipoles and induced neutral bodies](Olympiad-06-multipoles.png)
7. [Off-axis rings, cube scaling and numerical checks](Olympiad-07-offaxis.png)
8. [Inverse-square tests and model boundaries](Olympiad-08-measurements.png)


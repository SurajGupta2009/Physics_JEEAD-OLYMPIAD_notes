# Thermodynamics — explanatory handwritten short notes

**28 complete A4 sheets: 21 JEE Main + Advanced, then 7 Olympiad/specialised extensions.**
112 concept cards, 248 displayed mathematical blocks and 56 native labelled diagrams/graphs. Four cards per sheet preserve theory, physical meaning, formulas, useful short derivations, assumptions, examples and examiner traps together. This is not merely a formula list or every worked exercise.

PNGs and PDFs sit directly in `Short notes/Thermodynamics/`, matching the repository chapter layout; `JEE-` and `Olympiad-` prefixes preserve independent numbering.

## Downloads

| Edition | PNG-only ZIP | Bookmarked A4 PDF |
|---|---|---|
| JEE — read first (21) | [JEE PNGs](thermodynamics-jee-pngs.zip) | [JEE PDF](thermodynamics-jee.pdf) |
| Olympiad/extensions (7) | [Extension PNGs](thermodynamics-olympiad-pngs.zip) | [Extension PDF](thermodynamics-olympiad.pdf) |
| Combined (28), JEE first | [All PNGs](thermodynamics-all-pngs.zip) | [Combined PDF](thermodynamics-short-notes.pdf) |

[Offline gallery](index.html) · [Scope/membership decisions](SCOPE.md) · [Corrections/model limits](SOURCE-AUDIT.md) · [Printing](PRINTING.txt) · [Verification](VERIFICATION.md)

Sources: [detailed Markdown](../../thermodynamics/Thermodynamics.md), [authoritative HTML](../../thermodynamics/Thermodynamics.html). Detailed chapter and other chapters are preserved; source corrections are explicit here, not silently rewritten into the originals.

## Format and reading

2480 × 3508 px, 300 DPI metadata, A4 portrait; at least 125 px safe inset (~10.6 mm). White paper, navy prose, teal explanations/headings, yellow results and red cautions. Patrick Hand prose at 11.52 pt, explanations at 11.04 pt; body font never shrunk to fit. Equations use mathematical typesetting and diagrams are native analytic/schematic drawings. Indexed PNGs retain anti-aliased text; PDF pages reconstruct exactly the same source pixels and palettes, not a lossy low-resolution preview.

Print ONE page per A4 sheet using **Fit**, not Fill/Crop. ZIPs contain only original PNGs; fonts/gallery/scripts remain in this directory and are not packaged inside the PNG bundles. Download/clone the folder for the offline HTML gallery. Gallery images are raster notes, not a searchable/accessibly transcribed mathematical course; the detailed chapter remains available as text.

## Reproduce and check

```bash
python -m venv /path/to/venv
/path/to/venv/bin/python -m pip install -r "Short notes/Thermodynamics/requirements.txt"
/path/to/venv/bin/python "Short notes/Thermodynamics/author_content.py"
/path/to/venv/bin/python "Short notes/Thermodynamics/render_sheets.py"
/path/to/venv/bin/python "Short notes/Thermodynamics/build_exports.py"
/path/to/venv/bin/python "Short notes/Thermodynamics/test_exports.py"
python thermodynamics/tools/check.py
```

Run the last source gate from the repository root. Build tools otherwise resolve files relative to their own directory. `author_content.py` is editable content and writes `sheets.json`; `diagrams.py` holds the 56 drawings. The renderer records card bounds and enforces formula, glyph, tick, legend and annotation bounds. `build_exports.py` records asset hashes and library versions; `test_exports.py` verifies contents and independent representative numerical models. Dependency ranges are in `requirements.txt`; actual versions are in `build-environment.json`. PDF metadata/timestamps can vary across rebuilds; checks assert content, not byte-identical files across environments. Font licence: [SIL OFL](fonts/OFL.txt).

## Individual sheets

### JEE

1. [Temperature & equilibrium](JEE-01-temperature.png)
2. [Expansion: geometry & constraint](JEE-02-expansion.png)
3. [Calorimetry & phase changes](JEE-03-calorimetry.png)
4. [Ideal gas: pressure from impacts](JEE-04-kinetic-pressure.png)
5. [Speeds, collisions & effusion](JEE-05-speeds-collisions.png)
6. [Degrees of freedom & mixtures](JEE-06-heat-capacities.png)
7. [First law: boundary before algebra](JEE-07-first-law.png)
8. [Isochores, isobars & path capacity](JEE-08-basic-processes.png)
9. [Isotherms & reversible adiabats](JEE-09-isotherm-adiabat.png)
10. [Polytropes: derive once, use often](JEE-10-polytropes.png)
11. [P-V paths: integrate, then account](JEE-11-arbitrary-paths.png)
12. [Insulated is not isentropic](JEE-12-irreversible.png)
13. [Cycles: count heat, not just area](JEE-13-cycle-ledgers.png)
14. [Second law & the Carnot ceiling](JEE-14-second-law.png)
15. [Refrigerators, pumps & cascades](JEE-15-refrigerators.png)
16. [Otto, Diesel & regeneration](JEE-16-standard-cycles.png)
17. [Entropy: state change & generation](JEE-17-entropy.png)
18. [Finite sources: energy plus entropy](JEE-18-entropy-applications.png)
19. [Heat transfer: rates & resistance](JEE-19-heat-transfer.png)
20. [Cooling laws & time scales](JEE-20-cooling.png)
21. [Thermal mechanics: close the constraints](JEE-21-thermal-mechanics.png)

### Olympiad

1. [Microstates & quantum mode activation](Olympiad-01-statistics.png)
2. [Effusive beams & thermal escape](Olympiad-02-effusive-beams.png)
3. [Atmospheres: hydrostatics plus a model](Olympiad-03-atmospheres.png)
4. [Real gases: interactions & criticality](Olympiad-04-real-gases.png)
5. [Throttling is not free expansion](Olympiad-05-throttling.png)
6. [Photon gas & radiative applications](Olympiad-06-radiation-gas.png)
7. [Useful work & compressed-tank limits](Olympiad-07-availability-tanks.png)


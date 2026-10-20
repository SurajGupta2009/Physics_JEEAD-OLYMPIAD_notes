# Capacitors — JEE first, Olympiad second

**17 A4 portrait PNGs: 11 JEE sheets followed by 6 Olympiad/extension sheets.**
Handwritten-style prose, teacher explanations, accurate equations, colours, labelled diagrams and graphs are preserved.

## Other completed chapters

- [Thermodynamics — 21 JEE + 7 extensions](thermodynamics/README.md): [gallery](thermodynamics/index.html), [all PNGs](thermodynamics/thermodynamics-all-pngs.zip), [A4 PDF](thermodynamics/thermodynamics-short-notes.pdf).

## Downloads

| Part | PNG bundle | A4 PDF |
|---|---|---|
| **Part I: JEE — read first** | [11 JEE PNGs](capacitors-jee-pngs.zip) | [JEE PDF](capacitors-jee.pdf) |
| Part II: Olympiad / extensions | [6 extension PNGs](capacitors-olympiad-pngs.zip) | [Extension PDF](capacitors-olympiad.pdf) |
| Combined — JEE then Olympiad | [All 17 PNGs](capacitors-a4-pngs.zip) | [Combined PDF](capacitors-short-notes.pdf) |

- [Offline gallery, grouped by part](index.html)
- [Scope decisions and old-page mapping](SCOPE.md)
- [Printing instructions](PRINTING.txt)
- [Detailed chapter](../capacitors/Capacitors.md)

The PNGs live in **`JEE/`** and **`Olympiad/`**, with independent page numbering and a visible part label on every sheet. Combined exports put all JEE pages first. The previous mixed edition has been replaced, not left beside the new edition to confuse the reading order.

## How the boundary was chosen

**Relevance, not toughness.** JEE retains core electrostatics, capacitance, dielectrics, energy, force, charge conservation, networks and ordinary RC applications. Harder but useful applications such as bridges, cube networks, ladders and liquid rise stay there. Breakdown ratings are brought into the JEE checklist.

Specialised microscopic response, dispersive materials, compensation/oscillators, coupled RC eigenmodes, capacitance matrices, reciprocity, exact image/conformal tools, spheroids, porous electrodes and instability theory go in the extension part. Previous **page 12 is now Olympiad 02**, and **page 14 is now Olympiad 05**. Mixed pages were actually edited: basic branch charge stays in JEE, matrix dynamics moves out; exact two-wire formulas move out, ordinary connected-sphere reasoning stays in.

This is a **chapter-focused study grouping**, not a claim that every extension topic is absent from the entire JEE syllabus. In particular AC impedance belongs in JEE's AC chapter; specialised filters, compensated probes and threshold circuits are kept here as extras. See `SCOPE.md`.

## Print specification

Every PNG is **2480 × 3508 at 300 DPI**, A4 portrait proportions, with approximately 10 mm safe margins. Body text is 11.5 pt equivalent, explanations 11 pt, equations nominally 12 pt with occasional width fitting down to 10 pt. PDF media boxes are exact A4, 210 × 297 mm.

Print **A4, portrait, one sheet per page, Fit to page / printable area**. Do not select photo-style Fill/Crop. Colour is recommended; labels retain meaning in grayscale.

## Page index

| Part / local page | PNG | Source |
|---|---|---|
| JEE 01 | [Charge, field & conductors](JEE/01-foundations.png) | Chapter 1 |
| JEE 02 | [Capacitance & parallel plates](JEE/02-plates-and-capacitance.png) | Chapter 2 |
| JEE 03 | [The geometry toolbox](JEE/03-capacitor-geometries.png) | Chapter 2 |
| JEE 04 | [Energy & the battery fork](JEE/04-energy-and-battery.png) | Chapter 3 |
| JEE 05 | [Pressure, insertion & liquid rise](JEE/05-force-and-insertion.png) | Chapters 3 and 5 |
| JEE 06 | [Networks: charge on islands](JEE/06-network-foundations.png) | Chapter 4 |
| JEE 07 | [Bridges, symmetry & ladders](JEE/07-network-tools.png) | Chapter 4 |
| JEE 08 | [Dielectrics: field & geometry](JEE/08-dielectric-geometry.png) | Chapter 5 |
| JEE 09 | [DC circuits & one RC transient](JEE/09-rc-basics.png) | Chapter 6 |
| JEE 10 | [Charge sharing, heat & branch charge](JEE/10-switching-and-heat.png) | Chapters 3, 4 and 6 |
| JEE 11 | [JEE revision & safe-use checklist](JEE/11-revision-checklist.png) | Chapter 8 and formula sheet |
| Olympiad 01 | [Microscopic & dispersive dielectrics](Olympiad/01-material-response.png) | Chapter 5 |
| Olympiad 02 | [AC, dividers & timing circuits](Olympiad/02-ac-and-applications.png) | Chapter 6 and formula sheet |
| Olympiad 03 | [Coupled RC & specialised models](Olympiad/03-coupled-rc-and-measurement.png) | Chapter 6 and advanced practice |
| Olympiad 04 | [Matrices, reciprocity & images](Olympiad/04-matrices-and-images.png) | Chapter 7 |
| Olympiad 05 | [Shape, conformal maps & pores](Olympiad/05-shape-and-conformal-tools.png) | Chapters 6 and 7 |
| Olympiad 06 | [Pull-in, oscillations & charged drops](Olympiad/06-stability-and-drops.png) | Chapters 3 and 7 |

## Rebuild and test

```sh
python -m pip install -r "short notes/requirements.txt"
python "short notes/render_sheets.py"
python "short notes/build_exports.py"
python "short notes/test_exports.py"
```

`sheets.json` contains editable content, section assignment, independent numbering and old-page mapping. `render_sheets.py` checks formula parsing, text width and overflow without shrinking body type. `layout-checks.json` records every card. Export tests cover dimensions, DPI, safe margins, ordering, section membership, ZIP contents, local links, A4 PDF page boxes and representative physics.

These are conceptual short notes, not every worked exercise; the detailed source retains derivations and the complete paper/solutions. Patrick Hand is under the SIL Open Font License in `fonts/OFL.txt`.

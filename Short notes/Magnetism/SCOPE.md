# SCOPE — Magnetism + EMI + AC short notes

Primary sources: [`../../magnetism/Magnetism.md`](../../magnetism/Magnetism.md) (plan parts 16–19: Lorentz force → sources of B → forces and dipoles → matter → Earth) and [`../../emi-ac/Emi-ac.md`](../../emi-ac/Emi-ac.md) (electromagnetic induction, transients and alternating currents). Both sources are **not rewritten or modified**; these sheets are an independent teacher-edited compression in the established short-notes format.

## What is in the sheets

77 A4 sheets, 308 concept cards, 514 rendered math blocks, 154 native diagram panels. Every card carries physical meaning, the governing equations, reasoning/assumptions (WHY), and a failure mode or trap (WATCH); every card is packed near capacity.

**Part I — JEE Main + Advanced, 58 sheets (JEE-01 … JEE-58)**

| Sheets | Content |
|---|---|
| 01–04 | Lorentz force and its properties; circles, helices and the speed-independent period; parallel/crossed fields and the velocity selector; the three-region trajectory method |
| 05–10 | Mass spectrometer; cyclotron and its limits; magnetic mirrors, bottles and adiabatic invariance; Hall effect; E×B drift, cycloid and gradient drift; reading tracks (Thomson e/m, the 300 Br rule) |
| 11–18 | Biot–Savart law and the moving-charge form; finite wires by end angles; loops and arcs; solenoid and toroid; magnetic moment and dipole fields; Ampère's law and its symmetry requirement; the eight standard Ampère geometries; overlap/superposition tricks and ∇·B = 0 |
| 19–23 | Force on a current and the chord theorem; torque, energy and the galvanometer; forces between wires and the ampere; magnetic pressure, boundary conditions and field energy; the gyromagnetic ratio |
| 24–29 | Magnet as bound-current distribution; B, H and M; dia- and paramagnetism; ferromagnetism and hysteresis; magnetic circuits, cores and forces on materials; the Earth's field and its measurement |
| 30–37 | Magnetic flux; Faraday's law and the charge protocol; motional EMF; Lenz law as energy conservation; rails, terminal speed and the time constant; machines, commutation and the flux-rule limits; attachments: resistor, capacitor, inductor loads; the induced electric field |
| 38–48 | Betatron and the 2:1 rule; eddy currents, braking, heating and lamination; motors, generators and back-EMF; the voltmeter paradox and everyday induction; inductance and its geometry; computing L (solenoid, coax, L′C′); mutual inductance and coupling; RL transients and the spark; magnetic energy and pressure revisited; the mechanical analogy; the LC oscillator |
| 49–58 | AC generation and RMS; reactance of R, L and C; phasors; series LCR and impedance; resonance, Q and bandwidth; AC power and the power triangle; parallel AC circuits and the tank; complex impedance methods; transformers and impedance reflection; rectifiers, smoothing and filters |

**Part II — Olympiad / specialised extensions, 19 sheets (Olympiad-01 … Olympiad-19)**

| Sheets | Content |
|---|---|
| 01 | Magnetism as electrostatics plus relativity (the constant comes out right) |
| 02 | The Helmholtz pair: flatness condition, design worked end to end |
| 03 | The magnetised sphere two ways (rings; demagnetising factor) |
| 04 | Magnetic pressure at work: pinch, levitated slab, cosine-theta coil |
| 05 | The cycloid family from any initial velocity; Fermi acceleration |
| 06 | Three radiation-belt clocks; why the synchrotron is not a cyclotron |
| 07 | Two-carrier Hall effect; superconducting levitation; iron versus water |
| 08 | Estimates, Gauss absolute measurement, consistency identities and model limits |
| 09 | The Faraday disc and the flux-rule limits (sliding contacts, homopolar) |
| 10 | Betatron orbit theory: canonical momentum, radial stability |
| 11 | Magnetic braking: the copper tube, terminal velocity and damping |
| 12 | Superconducting flux conservation and the switched-inductor pair |
| 13 | Electrodynamic tethers and coil launchers (mutual-inductance gradient) |
| 14 | Induction drag across regimes: switch transients and the general brake law |
| 15 | Transmission lines: the telegrapher's equation, surges and reflections |
| 16 | The driven LCR transient: beats near resonance and the mechanical twin |
| 17 | Maximum power transfer and conjugate matching; three-phase basics |
| 18 | Radio circuits: coupled tanks and the Wien oscillator |
| 19 | EMI estimates: skin depth, screening, fields versus chemistry for storage |

## How the boundary was drawn

The split follows **syllabus relevance and usefulness**, not difficulty: Part I holds every standard JEE Main/Advanced heading of both modules, including hard core applications (mirrors, drifts, magnetic pressure, hysteresis, gapped circuits, rails and machines, LCR transients, resonance design, transformers and rectifiers). Part II holds content whose *derivation or full treatment* sits outside the JEE syllabus or belongs to another paper's tradition — relativistic origin of magnetism, Helmholtz design algebra, demagnetising factors, pinch/cosine-theta engineering, Fermi acceleration, radiation-belt clock hierarchy, two-carrier transport, betatron orbit theory, launchers, transmission-line surges, conjugate matching, oscillator design and order-of-magnitude apparatus estimates. Nothing is excluded merely for being hard. Topics are not claimed to "never appear in JEE"; extension material is derivable with the supplied information or belongs to another paper's syllabus.

## Deliberately not in these sheets

- Displacement current and radiation (electromagnetic-waves module); Poynting flow is named and used where it clarifies energy transport.
- Quantum origin of spin, g = 2, exchange and superconductivity: named with their scales, derived nowhere here.
- The worked-exercise corpus of the sources (C1–C14, E1–E20, Q1–Q60, OL1–OL12; E1–E20 and Q1–Q60 of the EMI+AC module, its OL1–OL12): the sheets compress the theory, methods and traps; the source chapters keep the exercises.

## Delivered files

- 77 direct PNGs (`JEE-…png`, `Olympiad-…png`), 2480 × 3508, 300 DPI.
- `magnetism-all-pngs.zip`, `magnetism-jee-pngs.zip`, `magnetism-olympiad-pngs.zip` (PNG-only).
- `magnetism-short-notes.pdf`, `magnetism-jee.pdf`, `magnetism-olympiad.pdf` (A4, one sheet per page, lossless, bookmarked).
- `index.html` offline gallery; `README.md`, `SCOPE.md`, `SOURCE-AUDIT.md`, `VERIFICATION.md`, `PRINTING.txt`.
- Reproducible sources: `author_content.py`, `diagrams.py`, `render_sheets.py`, `build_exports.py`, `revalidate.py`, `test_exports.py`, licensed font.

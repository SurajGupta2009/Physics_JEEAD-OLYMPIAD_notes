# Semiconductors & Electronic Devices — Standalone A4 Short Notes

Self-contained A4 300-DPI teacher-grade revision sheets distilled from [`../../semiconductors/Semiconductors.md`](../../semiconductors/Semiconductors.md) (`1,680` lines, `15` parts `0–14`, `76` examples/questions/problems `E1–E12`, `Q1–Q28`, `P1–P36`, `18` figures `D27.1–D27.18` — original source 100% untouched).

## Downloads & Offline Bundle

| Bundle | File | Pages / Sheets |
|---|---|---|
| **Complete Chapter PDF (All 18 Sheets)** | [`semiconductors-short-notes.pdf`](semiconductors-short-notes.pdf) | **18 A4 pages** (12 JEE + 6 Olympiad, lossless 300 DPI) |
| **Part I PDF — JEE Main + Advanced** | [`semiconductors-jee.pdf`](semiconductors-jee.pdf) | **12 A4 pages** (`JEE-01` .. `JEE-12`) |
| **Part II PDF — Olympiad / Extensions** | [`semiconductors-olympiad.pdf`](semiconductors-olympiad.pdf) | **6 A4 pages** (`Olympiad-01` .. `Olympiad-06`) |
| **All PNGs ZIP** | [`semiconductors-all-pngs.zip`](semiconductors-all-pngs.zip) | **18 PNGs** (`2480 x 3508 px`, 300 DPI) |
| **JEE PNGs ZIP** | [`semiconductors-jee-pngs.zip`](semiconductors-jee-pngs.zip) | **12 PNGs** |
| **Olympiad PNGs ZIP** | [`semiconductors-olympiad-pngs.zip`](semiconductors-olympiad-pngs.zip) | **6 PNGs** |
| **Offline Browser Gallery** | [`index.html`](index.html) | Interactive viewer + print stylesheet |

## Sheet Index (18 Sheets · 72 Cards · 36 Analytic Diagrams)

### Part I — JEE Main + Advanced (12 Sheets)

1. [`JEE-01-conductors-bands-gaps.png`](JEE-01-conductors-bands-gaps.png) — **Energy bands, band gap & thermal resistivity**
2. [`JEE-02-intrinsic-extrinsic-doping.png`](JEE-02-intrinsic-extrinsic-doping.png) — **Intrinsic & extrinsic semiconductors: mass-action & doping**
3. [`JEE-03-drift-diffusion-transport.png`](JEE-03-drift-diffusion-transport.png) — **Drift, diffusion, mobility & Einstein relation**
4. [`JEE-04-pn-junction-equilibrium.png`](JEE-04-pn-junction-equilibrium.png) — **Equilibrium p-n junction: space charge & built-in barrier**
5. [`JEE-05-diode-iv-breakdown.png`](JEE-05-diode-iv-breakdown.png) — **Biased p-n diode: Shockley I-V, dynamic resistance & breakdown**
6. [`JEE-06-rectifiers-filters-clippers.png`](JEE-06-rectifiers-filters-clippers.png) — **Rectifiers, ripple filters, clippers & clampers**
7. [`JEE-07-zener-optoelectronic-devices.png`](JEE-07-zener-optoelectronic-devices.png) — **Zener voltage regulator & optoelectronic p-n devices**
8. [`JEE-08-bjt-physics-modes.png`](JEE-08-bjt-physics-modes.png) — **Bipolar junction transistor (BJT): gains & modes**
9. [`JEE-09-ce-amplifier-switch.png`](JEE-09-ce-amplifier-switch.png) — **Common-emitter (CE) amplifier & BJT electronic switch**
10. [`JEE-10-diode-transistor-logic-gates.png`](JEE-10-diode-transistor-logic-gates.png) — **Digital signals, diode-transistor gates & truth tables**
11. [`JEE-11-boolean-universal-adders.png`](JEE-11-boolean-universal-adders.png) — **Boolean algebra, De Morgan's theorem, NAND/NOR & adders**
12. [`JEE-12-master-triage-traps.png`](JEE-12-master-triage-traps.png) — **Master formula triage & 14 exam trap checklist**

### Part II — Olympiad / Specialised Extensions (6 Sheets)

1. [`Olympiad-01-hydrogenic-donors-fermi.png`](Olympiad-01-hydrogenic-donors-fermi.png) — **Hydrogenic donors, effective mass & Fermi-level motion**
2. [`Olympiad-02-boltzmann-junction-varactor.png`](Olympiad-02-boltzmann-junction-varactor.png) — **Boltzmann barrier, Poisson depletion & varactor diodes**
3. [`Olympiad-03-hall-thermometry-bandgap.png`](Olympiad-03-hall-thermometry-bandgap.png) — **Hall effect metrology, diode thermometry & 1.22 V reference**
4. [`Olympiad-04-solar-limits-bypass-leds.png`](Olympiad-04-solar-limits-bypass-leds.png) — **Solar cell thermodynamics, bypass diodes & LED stability**
5. [`Olympiad-05-shot-noise-photoreceivers.png`](Olympiad-05-shot-noise-photoreceivers.png) — **Shot vs Johnson noise, photodiodes & optical receivers**
6. [`Olympiad-06-quantum-wall-cmos-scaling.png`](Olympiad-06-quantum-wall-cmos-scaling.png) — **5 nm quantum tunnelling wall, high-k HKMG & CMOS power**

## Rebuild & Verification Commands

```bash
python3 "Short notes/Semiconductors/author_content.py"
python3 "Short notes/Semiconductors/render_sheets.py"
python3 "Short notes/Semiconductors/build_exports.py"
python3 "Short notes/Semiconductors/revalidate.py"
python3 "Short notes/Semiconductors/test_exports.py"
```

See also [`SCOPE.md`](SCOPE.md), [`SOURCE-AUDIT.md`](SOURCE-AUDIT.md), [`VERIFICATION.md`](VERIFICATION.md), and [`PRINTING.txt`](PRINTING.txt).

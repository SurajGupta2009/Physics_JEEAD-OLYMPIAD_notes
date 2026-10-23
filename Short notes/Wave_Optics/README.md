# Wave Optics — Standalone A4 Short Notes

Self-contained A4 300-DPI teacher-grade revision sheets distilled from [`../../wave-optics/Wave-optics.md`](../../wave-optics/Wave-optics.md) (`4,525` lines, `12` parts, `136` questions, `28` figures — original source 100% untouched).

## Downloads & Offline Bundle

| Bundle | File | Pages / Sheets |
|---|---|---|
| **Complete Chapter PDF (All 24 Sheets)** | [`wave-optics-short-notes.pdf`](wave-optics-short-notes.pdf) | **24 A4 pages** (16 JEE + 8 Olympiad, lossless 300 DPI) |
| **Part I PDF — JEE Main + Advanced** | [`wave-optics-jee.pdf`](wave-optics-jee.pdf) | **16 A4 pages** (`JEE-01` .. `JEE-16`) |
| **Part II PDF — Olympiad / Extensions** | [`wave-optics-olympiad.pdf`](wave-optics-olympiad.pdf) | **8 A4 pages** (`Olympiad-01` .. `Olympiad-08`) |
| **All PNGs ZIP** | [`wave-optics-all-pngs.zip`](wave-optics-all-pngs.zip) | **24 PNGs** (`2480 x 3508 px`, 300 DPI) |
| **JEE PNGs ZIP** | [`wave-optics-jee-pngs.zip`](wave-optics-jee-pngs.zip) | **16 PNGs** |
| **Olympiad PNGs ZIP** | [`wave-optics-olympiad-pngs.zip`](wave-optics-olympiad-pngs.zip) | **8 PNGs** |
| **Offline Browser Gallery** | [`index.html`](index.html) | Interactive viewer + print stylesheet |

## Sheet Index (24 Sheets · 96 Cards · 48 Analytic Diagrams)

### Part I — JEE Main + Advanced (16 Sheets)

1. [`JEE-01-wavefronts-huygens.png`](JEE-01-wavefronts-huygens.png) — **Wavefronts, optical path & Huygens principle**
2. [`JEE-02-superposition-coherence.png`](JEE-02-superposition-coherence.png) — **Superposition, phasors, visibility & energy**
3. [`JEE-03-ydse-core.png`](JEE-03-ydse-core.png) — **Young's double-slit experiment (YDSE) core**
4. [`JEE-04-ydse-3d-shapes.png`](JEE-04-ydse-3d-shapes.png) — **3D hyperboloids, end-on circular rings & screen tilts**
5. [`JEE-05-ydse-slabs-media.png`](JEE-05-ydse-slabs-media.png) — **YDSE with dielectric slabs, liquids & unequal slits**
6. [`JEE-06-ydse-oblique-polychromatic.png`](JEE-06-ydse-oblique-polychromatic.png) — **Oblique incidence, moving sources & white-light YDSE**
7. [`JEE-07-thin-films.png`](JEE-07-thin-films.png) — **Parallel thin-film interference & phase flips**
8. [`JEE-08-wedges-newtons-rings.png`](JEE-08-wedges-newtons-rings.png) — **Air wedges, thermal expansion & Newton's rings**
9. [`JEE-09-antireflection-optical-splitters.png`](JEE-09-antireflection-optical-splitters.png) — **Quarter-wave AR coatings, Fresnel biprism & Lloyd's mirror**
10. [`JEE-10-single-slit-diffraction.png`](JEE-10-single-slit-diffraction.png) — **Fraunhofer single-slit diffraction & secondary peaks**
11. [`JEE-11-double-slit-diffraction-grating.png`](JEE-11-double-slit-diffraction-grating.png) — **Double-slit diffraction envelope, missing orders & gratings**
12. [`JEE-12-airy-resolution-pinhole.png`](JEE-12-airy-resolution-pinhole.png) — **Circular Airy disc, Rayleigh resolution & pinhole camera**
13. [`JEE-13-polarisation-malus.png`](JEE-13-polarisation-malus.png) — **Polarisation states, Malus's law & middle-polariser trick**
14. [`JEE-14-brewster-scattering.png`](JEE-14-brewster-scattering.png) — **Brewster reflection law, critical angle & sky scattering**
15. [`JEE-15-birefringence-waveplates.png`](JEE-15-birefringence-waveplates.png) — **Birefringence, quarter/half waveplates & optical activity**
16. [`JEE-16-master-triage.png`](JEE-16-master-triage.png) — **Master formula triage & JEE trap checklist**

### Part II — Olympiad / Specialised Extensions (8 Sheets)

1. [`Olympiad-01-michelson-metrology.png`](Olympiad-01-michelson-metrology.png) — **Michelson interferometer, compensator & gas refractometry**
2. [`Olympiad-02-temporal-spatial-coherence.png`](Olympiad-02-temporal-spatial-coherence.png) — **Temporal & spatial coherence, Wiener-Khinchin & stellar interferometry**
3. [`Olympiad-03-fresnel-equations-coatings.png`](Olympiad-03-fresnel-equations-coatings.png) — **Exact Fresnel TE/TM equations, Stokes relations & quarter-wave stacks**
4. [`Olympiad-04-tir-phase-evanescent.png`](Olympiad-04-tir-phase-evanescent.png) — **TIR phase jumps, Fresnel rhomb & evanescent tunnelling**
5. [`Olympiad-05-n-slit-blazed-gratings.png`](Olympiad-05-n-slit-blazed-gratings.png) — **Exact N-slit phasor sum, resolving power, FSR & blazed echelles**
6. [`Olympiad-06-fabry-perot-cavities.png`](Olympiad-06-fabry-perot-cavities.png) — **Fabry-Perot Airy function, finesse & laser cavity modes**
7. [`Olympiad-07-fresnel-zones-cornu.png`](Olympiad-07-fresnel-zones-cornu.png) — **Fresnel half-period zones, Arago spot, zone plates & Cornu spiral**
8. [`Olympiad-08-abbe-bragg-sagnac.png`](Olympiad-08-abbe-bragg-sagnac.png) — **Abbe Fourier imaging, X-ray Bragg law, Sagnac & HBT**

## Rebuild & Verification Commands

```bash
python3 "Short notes/Wave_Optics/author_content.py"
python3 "Short notes/Wave_Optics/render_sheets.py"
python3 "Short notes/Wave_Optics/build_exports.py"
python3 "Short notes/Wave_Optics/revalidate.py"
python3 "Short notes/Wave_Optics/test_exports.py"
```

See also [`SCOPE.md`](SCOPE.md), [`SOURCE-AUDIT.md`](SOURCE-AUDIT.md), [`VERIFICATION.md`](VERIFICATION.md), and [`PRINTING.txt`](PRINTING.txt).

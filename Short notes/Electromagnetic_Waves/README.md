# Electromagnetic Waves — explanatory handwritten short notes

**18 complete A4 sheets: 12 JEE Main + Advanced (`JEE-01`–`JEE-12`), then 6 Olympiad / specialised extensions (`Olympiad-01`–`Olympiad-06`).**
72 concept cards and 36 native analytic diagrams/graphs. Built from [`electromagnetic-waves/Electromagnetic-waves.md`](../../electromagnetic-waves/Electromagnetic-waves.md) without modifying the detailed source chapter.

## Downloads

| Deliverable | File |
|---|---|
| **Combined A4 PDF (all 18 sheets, bookmarked)** | **[`electromagnetic-waves-short-notes.pdf`](electromagnetic-waves-short-notes.pdf)** |
| **All PNGs bundle (18 sheets)** | **[`electromagnetic-waves-all-pngs.zip`](electromagnetic-waves-all-pngs.zip)** |
| Part I — JEE Main + Advanced (12 sheets) | [`electromagnetic-waves-jee.pdf`](electromagnetic-waves-jee.pdf) · [`electromagnetic-waves-jee-pngs.zip`](electromagnetic-waves-jee-pngs.zip) |
| Part II — Olympiad / extensions (6 sheets) | [`electromagnetic-waves-olympiad.pdf`](electromagnetic-waves-olympiad.pdf) · [`electromagnetic-waves-olympiad-pngs.zip`](electromagnetic-waves-olympiad-pngs.zip) |
| Offline gallery | [`index.html`](index.html) |

Supporting notes: [`SCOPE.md`](SCOPE.md) · [`SOURCE-AUDIT.md`](SOURCE-AUDIT.md) · [`VERIFICATION.md`](VERIFICATION.md) · [`PRINTING.txt`](PRINTING.txt) · Font license: [`fonts/OFL.txt`](fonts/OFL.txt).

## Sheet index

### Part I — JEE Main + Advanced
1. [`JEE-01-ampere-paradox.png`](JEE-01-ampere-paradox.png) — Displacement current & the Ampere spanning-surface paradox
2. [`JEE-02-gap-field.png`](JEE-02-gap-field.png) — Capacitor gap magnetic field $B_\phi(r)$ & dielectric polarisation split
3. [`JEE-03-maxwell-laws.png`](JEE-03-maxwell-laws.png) — All four Maxwell equations in vacuum & matter
4. [`JEE-04-wave-equation.png`](JEE-04-wave-equation.png) — Curl-curl wave equations, phase speed $v = c/\sqrt{\mu_r\varepsilon_r}$ & refraction
5. [`JEE-05-plane-wave.png`](JEE-05-plane-wave.png) — Plane-wave phase, transversality & right-handed triad
6. [`JEE-06-polarisation.png`](JEE-06-polarisation.png) — Linear, circular & elliptical polarisation + Malus's law
7. [`JEE-07-poynting.png`](JEE-07-poynting.png) — Field energy density, Poynting theorem & instantaneous equipartition
8. [`JEE-08-intensity.png`](JEE-08-intensity.png) — Peak vs RMS amplitude, wave impedance $Z_0 \approx 377\,\Omega$ & $1/r^2$ scaling
9. [`JEE-09-momentum-pressure.png`](JEE-09-momentum-pressure.png) — Field momentum, flat-plate $\cos^2\theta$ law & tangential shear
10. [`JEE-10-em-spectrum.png`](JEE-10-em-spectrum.png) — Electromagnetic spectrum cutoffs, mechanisms & RADAR ranging
11. [`JEE-11-dipole-radiation.png`](JEE-11-dipole-radiation.png) — LC oscillators, accelerating charges & Hertzian dipole $\sin^2\theta\,\omega^4$ radiation
12. [`JEE-12-master-triage.png`](JEE-12-master-triage.png) — Master triage map, fast constants & top examiner traps

### Part II — Olympiad / Specialised Extensions
1. [`Olympiad-01-capacitor-poynting.png`](Olympiad-01-capacitor-poynting.png) — Radial Poynting flux in capacitors, wires & coaxial TEM lines
2. [`Olympiad-02-curved-pressure.png`](Olympiad-02-curved-pressure.png) — Curved-surface forces ($F_{\rm black} = F_{\rm spec} = I\pi a^2/c$), cones & stellar $\beta$-ratio
3. [`Olympiad-03-impedance-fresnel.png`](Olympiad-03-impedance-fresnel.png) — Wave impedance, Fresnel normal-incidence matching & $\lambda/4$ anti-reflection coats
4. [`Olympiad-04-standing-cavity.png`](Olympiad-04-standing-cavity.png) — Standing EM waves at conductors, magnetic stress & isotropic pressure $u/3$
5. [`Olympiad-05-skin-depth.png`](Olympiad-05-skin-depth.png) — Conducting media, complex $k$, skin depth $\delta$ & collisionless plasma cutoff
6. [`Olympiad-06-poynting-robertson.png`](Olympiad-06-poynting-robertson.png) — Relativistic Doppler, moving mirrors, Poynting–Robertson drag & TE waveguides

## Rebuild

```bash
python3 -m pip install -r "Short notes/Electromagnetic_Waves/requirements.txt"
python3 "Short notes/Electromagnetic_Waves/author_content.py"
python3 "Short notes/Electromagnetic_Waves/render_sheets.py"
python3 "Short notes/Electromagnetic_Waves/build_exports.py"
python3 "Short notes/Electromagnetic_Waves/revalidate.py"
python3 "Short notes/Electromagnetic_Waves/test_exports.py"
```

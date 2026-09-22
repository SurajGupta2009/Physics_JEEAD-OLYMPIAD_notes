# Electromagnetic Waves — Examination Paper

> Generated from [Electromagnetic-waves.md](Electromagnetic-waves.md); edit the master, then run `python3 tools/export.py`.

### Instructions, marking and coverage

**180 minutes · 180 marks · 36 original questions.** This is a mixed JEE–Olympiad training paper, not an official examination. Keep solutions closed. $I$ is beam-normal average intensity. Surfaces are stationary; reflection is specular unless stated otherwise.

Use $c=3.00\times10^8\,\mathrm{m/s}$, $\varepsilon_0=8.85\times10^{-12}\,\mathrm{F/m}$, $\mu_0=4\pi\times10^{-7}\,\mathrm{H/m}$, $Z_0=377\,\Omega$, $hc=1240\,\mathrm{eV\,nm}$ as independently rounded constants; ignore discrepancies below 0.1%. Numerical tolerance: ±1%, unless an exact expression is requested.

| Section | Questions | Marks | Suggested minutes | Coverage |
|---|---|---:|---:|---|
| A — single correct | Q1–Q8 | $8\times3=24$ | 20 | Capacitor, waves, energy, pressure, spectrum |
| B — multi-correct | Q9–Q16 | $8\times4=32$ | 25 | Model limits, fields, force, interfaces |
| C — numerical | Q17–Q28 | $12\times3=36$ | 35 | All six core groups |
| D — comprehensive long form | Q29–Q36 | $8\times11=88$ | 100 | Maxwell, Poynting, standing waves, curved force, instruments |

**Scoring:** A: 3 for the correct option, otherwise 0. B: 4 for the exact correct set, otherwise 0; no negative marks. C: 3 for an accepted value with the requested unit, otherwise 0. D: award subpart marks as shown, credit alternate valid methods, and carry forward arithmetic errors without repeated penalties. Total $24+32+36+88=180$. Each long solution distributes its 11 marks explicitly.

### A — Single-correct questions

#### Q1. The gap surface [3 marks]

A vacuum capacitor charges at $2\,\mathrm A$. A surface bounded by an Amperian loop lies entirely between its plates and encloses their full changing flux. The pair $(I_c,I_d)$ **through this surface** is: A. $(2,2)\,\mathrm A$; B. $(0,2)\,\mathrm A$; C. $(2,0)\,\mathrm A$; D. $(0,0)\,\mathrm A$.

#### Q2. A changing-voltage dielectric [3 marks]

An ideal nonmagnetic capacitor is driven at fixed $\dot V$. Compare the empty capacitor with the same geometry fully filled with relative permittivity 4. The macroscopic displacement current becomes: A. unchanged; B. one quarter; C. twice; D. four times its original value.

#### Q3. A magnetic dielectric [3 marks]

A model-L medium has $\varepsilon_r=4$, $\mu_r=9$. Its speed is: A. $c/2$; B. $c/3$; C. $c/6$; D. $c/36$.

#### Q4. The right-handed triad [3 marks]

A vacuum travelling wave has instantaneous E along $+y$ and B along $-x$. Energy travels along: A. $+z$; B. $-z$; C. $+x$; D. $-y$.

#### Q5. Which amplitude? [3 marks]

For a linear harmonic vacuum travelling wave with electric RMS amplitude $E_r$, mean total energy density is: A. $\varepsilon_0E_r^2/2$; B. $\varepsilon_0E_r^2$; C. $2\varepsilon_0E_r^2$; D. zero.

#### Q6. Oblique mirror [3 marks]

A mirror is illuminated at $60^\circ$ rather than normally, with unchanged beam-normal intensity. Its normal pressure changes by a factor: A. $1/2$; B. $1/4$; C. $\sqrt3/2$; D. 1.

#### Q7. Wavelength conversion [3 marks]

A $2.4\,\mathrm{GHz}$ vacuum signal has wavelength closest to: A. $1.25\,\mathrm{mm}$; B. $1.25\,\mathrm m$; C. $12.5\,\mathrm{cm}$; D. $125\,\mathrm m$.

#### Q8. Naming radiation [3 marks]

Which statement is reliable? A. All gamma rays exceed all X-rays in energy. B. Gamma rays travel faster than radio in vacuum. C. X/gamma names can depend on production mechanism and their energies overlap. D. Electronic transitions cannot emit infrared.

### B — Multi-correct questions

#### Q9. Currents in a dielectric [4 marks]

For a uniformly filled $\kappa=3$ ideal capacitor in model Q: A. $A\dot D=I_c$. B. $\varepsilon_0A\dot E=I_c$. C. Polarisation current is $2I_c/3$. D. No free conduction charge need cross the gap.

#### Q10. Wave-equation conditions [4 marks]

Select correct statements. A. Homogeneous charge-free model L has $\nabla\cdot\mathbf E=0$. B. Inhomogeneous charge-free matter always has $\nabla\cdot\mathbf E=0$. C. Homogeneous Ohmic conduction adds $\mu\sigma\partial_t\mathbf E$ to the charge-free electric wave equation. D. Solving the wave equation alone guarantees all Maxwell constraints.

#### Q11. A single travelling wave [4 marks]

For one plane wave in model L: A. $\mathbf E\cdot\mathbf B=0$. B. $\mathbf B=\hat{\mathbf k}\times\mathbf E/v$. C. $E_0=cB_0$ in every medium. D. Electric and magnetic energy densities are equal instantaneously.

#### Q12. Energy and momentum [4 marks]

For vacuum radiation: A. A collimated pulse of energy $U$ has momentum magnitude $U/c$. B. Every collection of beams of total energy $U$ has net momentum magnitude $U/c$. C. Momentum density is $\mathbf S/c^2$. D. Zero mean electric field forces zero mean intensity.

#### Q13. Oblique absorber [4 marks]

A black patch of actual area $A_s$ sees vacuum intensity $I$ at angle $\theta$ to its normal. A. Intercepted power is $IA_s\cos\theta$. B. Force is purely normal. C. Normal pressure is $I\cos^2\theta/c$. D. Tangential traction is $I\sin\theta\cos\theta/c$.

#### Q14. Spheres and disks [4 marks]

A uniform parallel beam illuminates ideal bodies in geometric optics, each of projected area $\pi a^2$. A. A black sphere receives $I\pi a^2/c$. B. A specular sphere receives $2I\pi a^2/c$. C. A normal flat perfect mirror receives $2I\pi a^2/c$. D. Transverse force on either sphere is zero.

#### Q15. Spectrum applications [4 marks]

A. Magnetrons generate microwaves. B. Fast-electron deceleration can generate X-rays. C. Frequency necessarily changes at a stationary refracting interface. D. Excimer UV photoablation is used in LASIK.

#### Q16. Normal-incidence interface [4 marks]

Two model-L media have impedances $Z_1,Z_2$, with no surface sheet. A. $r_E=(Z_2-Z_1)/(Z_2+Z_1)$. B. Always $T=t_E^2$. C. Equal impedance gives no reflection. D. $R+T=1$.

### C — Numerical questions

#### Q17. Flux rate [3 marks]

Signed electric flux through a fixed vacuum surface grows at $4.00\times10^8\,\mathrm{V\,m/s}$. Find displacement current in mA.

#### Q18. Rim field [3 marks]

Circular plates of radius $0.040\,\mathrm m$ charge at $0.080\,\mathrm A$. Find model-Q gap rim field in $\mu\mathrm T$.

#### Q19. Material wavelength [3 marks]

A nonmagnetic model-L dielectric has $\varepsilon_r=6.25$. Light of vacuum wavelength $600\,\mathrm{nm}$ enters. Find its material wavelength in nm.

#### Q20. Magnetic amplitude [3 marks]

A vacuum travelling wave has peak E of $450\,\mathrm{V/m}$. Find peak B in $\mu\mathrm T$.

#### Q21. RMS intensity [3 marks]

A vacuum harmonic wave has $E_{\rm rms}=30.0\,\mathrm{V/m}$. Use $Z_0=377\,\Omega$ to find intensity in W/m².

#### Q22. Mean energy density [3 marks]

A unidirectional vacuum beam has intensity $240\,\mathrm{W/m^2}$. Find mean total energy density in $\mu\mathrm{J/m^3}$.

#### Q23. Pulse impulse [3 marks]

A $9.00\,\mathrm{mJ}$ collimated vacuum pulse reflects normally from a perfect mirror. Find impulse in units of $10^{-11}\,\mathrm{N\,s}$.

#### Q24. Opaque coating [3 marks]

An opaque surface with $R=0.25$ receives normal vacuum intensity $600\,\mathrm{W/m^2}$. Find pressure in $\mu\mathrm{Pa}$.

#### Q25. Intercepted power [3 marks]

A perfect mirror intercepts $12.0\,\mathrm W$ at $60^\circ$. Find normal force in nN.

#### Q26. Sphere force [3 marks]

A black sphere of radius $0.020\,\mathrm m$ receives uniform vacuum intensity $1500\,\mathrm{W/m^2}$. Find axial force in nN in geometric optics.

#### Q27. Radar range [3 marks]

An echo returns after $8.00\,\mu\mathrm s$. Ignore instrumental delay and refractive-index corrections. Find range in metres.

#### Q28. UV photon [3 marks]

Using $hc=1240\,\mathrm{eV\,nm}$, find the energy in eV of a $248\,\mathrm{nm}$ vacuum photon.

### D — Comprehensive Olympiad long-form questions

#### Q29. Charging as an energy-flow experiment [11 marks]

Vacuum circular plates of radius $a$ and separation $d\ll a$ carry $q(t)=\alpha t^2$ for $t\geq0$, $\alpha>0$. Use model Q at times when variation is slow compared with $a/c$. Take E along $+z$.

(a) Find $I_c,E,B_\phi(r)$ for $r<a$. (3)  
(b) Find radial Poynting vector at $r=a$ and integrate inward power through the cylindrical side of the gap. (4)  
(c) Compare with $d(q^2/2C)/dt$ and $VI_c$; explain the entry route and quasistatic limitation. (4)

#### Q30. Derive a wave, then test its data [11 marks]

A source-free model-L medium has $\varepsilon_r=4$, $\mu_r=1$. A proposed field is $\mathbf E=(80\,\mathrm{V/m})\cos(4z-\omega t)\hat{\mathbf x}$, with SI coordinates.

(a) Derive both E/B wave equations from the curls, using divergence laws explicitly. (4)  
(b) Find $v,\omega$ and complete $\mathbf B$. (3)  
(c) Find $Z,I,\langle u\rangle$ and explain why $E_0=cB_0$ fails here. (4)

#### Q31. Mirror pressure with no net energy flow [11 marks]

A linear harmonic vacuum wave of electric peak $E_0$ travels along $+z$ toward a perfect conductor at $z=0$.

(a) Construct incident/reflected fields with zero tangential E at the mirror; add them. (4)  
(b) Find E/B nodes, mean energy density, mean Poynting vector. (4)  
(c) Use magnetic stress for mean pressure and reconcile it with the energy flux. (3)

#### Q32. Isotropic beacon, oblique detector [11 marks]

An ideal source radiates $120\,\mathrm W$ isotropically in vacuum. A small black detector, actual area $0.010\,\mathrm{m^2}$, is at $r=3.00\,\mathrm m$, normal $60^\circ$ from the incident ray. Assume it lies in the far field. For amplitudes treat the local radiation as a linear harmonic travelling wave.

(a) Find intensity and equivalent E/B peak amplitudes. (4)  
(b) Find absorbed power, total force magnitude and normal force. (4)  
(c) Double distance at fixed orientation: give scaling factors and justify the small-detector approximation. (3)

#### Q33. Partially reflecting inclined sail [11 marks]

A flat stationary vacuum sail of actual area $A_s$ has opaque specular reflectance $R$, absorptance $1-R$. Its inward normal $\hat{\mathbf n}$ and tangent $\hat{\mathbf t}$ define incident direction $\hat{\mathbf k}=\cos\theta\hat{\mathbf n}+\sin\theta\hat{\mathbf t}$.

(a) Derive normal and tangential forces from momentum balance. (5)  
(b) Evaluate for $I=1200\,\mathrm{W/m^2}$, $A_s=2.00\,\mathrm{m^2}$, $R=0.75$, $\theta=60^\circ$. (3)  
(c) Give black, mirror and grazing checks; explain why $(1+R)I/c$ is not a complete force law. (3)

#### Q34. Radiation versus gravity for a grain [11 marks]

A star of luminosity $L_\star$, mass $M_\star$, illuminates a sphere of radius $a\gg\lambda$, density $\rho_m$, at $r\gg a$. Treat illumination as locally parallel and isotropic at the source. Neglect emission recoil. The sphere is either perfectly absorbing or locally specular.

(a) Integrate axial radiation force for both surface types. (5)  
(b) Derive $\beta=F_{\rm rad}/F_g$ using Newtonian gravity and decide whether it depends on $r$. (3)  
(c) Find $a_{\rm crit}$ for $\beta=1$ and discuss two limits. (3)

#### Q35. One instrument, three spectral decisions [11 marks]

A system has a $12.0\,\mathrm{GHz}$ radar, a $193\,\mathrm{nm}$ excimer corneal-photoablation beam, and an X-ray tube producing $0.100\,\mathrm{nm}$ photons. Radar target range is $4.50\,\mathrm{km}$.

(a) Find missing frequencies/wavelength and classify each beam; name one source mechanism each. (4)  
(b) Find radar round-trip delay and UV/X-ray photon energies. (4)  
(c) Explain why a spectrum table proves neither ionisation of a specified target nor unique X/gamma origin. (3)

#### Q36. Match fields, not just refractive index [11 marks]

A normally incident wave passes from medium 1 to medium 2, both model L, with $Z_2=2Z_1$. There is no free surface current or charge.

(a) Derive the amplitude boundary equations, keeping the backward magnetic sign. (4)  
(b) Find $r_E,t_E,R,T$ and verify energy conservation. (4)  
(c) Can speeds match despite this impedance mismatch? Construct positive $\varepsilon_2,\mu_2$ relative to medium 1 and discuss reflection. (3)

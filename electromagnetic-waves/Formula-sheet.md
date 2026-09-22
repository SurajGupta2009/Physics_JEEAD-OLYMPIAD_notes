# Electromagnetic Waves — Printable Formula Sheet

> Generated from [Electromagnetic-waves.md](Electromagnetic-waves.md); edit the master, then run `python3 tools/export.py`.

Print only this section for compact revision; page count depends on renderer and paper size. Conditions are part of every entry. $I$ is beam-normal mean intensity, $E_0$ a **peak linear-harmonic** amplitude, $A_s$ actual target area, $\theta$ angle from its normal.

### Sheet A — Fields, waves and energy

| Result | Conditions / meaning |
|---|---|
| $\nabla\cdot\mathbf D=\rho_f$, $\nabla\cdot\mathbf B=0$ | Macroscopic Gauss laws |
| $\nabla\times\mathbf E=-\partial_t\mathbf B$, $\nabla\times\mathbf H=\mathbf J_f+\partial_t\mathbf D$ | Maxwell curls |
| $I_d=d\int\mathbf D\cdot d\mathbf A/dt$ | Fixed surface; vacuum $\mathbf D=\varepsilon_0\mathbf E$ |
| $I_d=\dot q=C\dot V$ | Ideal fixed capacitor, constant C, full gap flux |
| $I_{d,0}=I_c/\kappa$, $I_{\rm pol}=(1-1/\kappa)I_c$ | Uniform linear dielectric |
| $B_\phi=\mu_0I_cr/(2\pi a^2)$ inside; $\mu_0I_c/(2\pi r)$ outside | Circular quasistatic vacuum plates; fringe/return-lead effects neglected |
| $\nabla^2\mathbf E=\mu\varepsilon\partial_t^2\mathbf E$; same for B | Homogeneous isotropic linear lossless source-free region |
| $v=1/\sqrt{\mu\varepsilon}=c/n$, $n=\sqrt{\mu_r\varepsilon_r}$ | Model L, phase speed |
| $v=f\lambda=\omega/k$, $k=2\pi/\lambda$, $\omega=2\pi f$ | Monochromatic wave; stationary interface preserves f |
| $\mathbf B=\hat{\mathbf k}\times\mathbf E/v$, $E_0=vB_0$ | Single travelling plane wave in model L |
| $u_E=\varepsilon E^2/2$, $u_B=B^2/(2\mu)$ | Linear nondispersive storage; equal for one travelling plane wave |
| $\mathbf S=\mathbf E\times\mathbf H$, $\partial_tu+\nabla\cdot\mathbf S=-\mathbf J_f\cdot\mathbf E$ | Constant real constitutive coefficients |
| $Z=\sqrt{\mu/\varepsilon}$, $I=E_0^2/(2Z)=E_{\rm rms}^2/Z=v\langle u\rangle$ | Linear harmonic travelling wave in model L |
| $I=\mathcal P/(4\pi r^2)$, $E_0\propto1/r$ | Isotropic transparent far field |
| $\mathbf g=\mathbf S/c^2$, $\mathbf p=(U/c)\hat{\mathbf k}$ | Vacuum; latter requires one direction |

### Sheet B — Forces, interfaces and spectrum

| Result | Conditions / meaning |
|---|---|
| $\mathcal P_{\rm hit}=IA_s\cos\theta$ | Flat patch within uniform beam |
| $P_{n,\rm abs}=I\cos^2\theta/c$, $P_{n,\rm spec}=2I\cos^2\theta/c$ | Vacuum, stationary absorber/specular mirror; no extra emission recoil |
| $P_n=(1+R)I\cos^2\theta/c$ | Opaque specular/absorbing surface, $T=0$ |
| $F_t=(1-R)IA_s\sin\theta\cos\theta/c$ | Same surface; tangent follows incoming beam |
| $P_n=(1+R-T)I\cos^2\theta/c$ | Transmission undeviated in vacuum |
| $F_{n,\rm mirror}=2\mathcal P_{\rm hit}\cos\theta/c$ | Intercepted power specified; no extra area cosine |
| $F_{\rm sphere}=I\pi a^2/c$ | Black or local-specular sphere, $a\gg\lambda$, geometric optics |
| $P=u/3$ | Isotropic vacuum radiation, reflecting wall or equilibrium enclosure |
| $r_E=(Z_2-Z_1)/(Z_2+Z_1)$, $t_E=2Z_2/(Z_2+Z_1)$ | Normal incidence between model-L media, no surface current |
| $R=r_E^2$, $T=(Z_1/Z_2)t_E^2$, $R+T=1$ | Same lossless interface |
| $\lambda_0=c/f$, $E_\gamma=hf=hc/\lambda_0$ | Vacuum wavelength; photon relation is quantum input |
| $f_{LC}=1/(2\pi\sqrt{LC})$, $r_{\rm radar}=c\Delta t/2$ | Ideal lumped oscillator; vacuum round-trip echo |

**Constants:** $c\simeq3.00\times10^8\,\mathrm{m/s}$; $\varepsilon_0\simeq8.85\times10^{-12}\,\mathrm{F/m}$; $\mu_0\simeq4\pi\times10^{-7}\,\mathrm{H/m}$; $Z_0\simeq377\,\Omega$; $hc\simeq1240\,\mathrm{eV\,nm}$.

**Decreasing vacuum wavelength:** radio → microwave → IR → visible → UV → X → gamma. Adopted dividing wavelengths: 1 m, 1 mm, 700 nm, 400 nm, 10 nm, 0.01 nm. These are conventions; X/gamma origin-based names overlap. Sources: antennas/oscillators → microwave devices → thermal/molecular → electronic → electronic → bremsstrahlung/inner shell → nuclear/high-energy. All travel at the same $c$ in vacuum.

**Final self-test:** Name the medium, amplitude convention, propagation direction and relevant area before substituting numbers.

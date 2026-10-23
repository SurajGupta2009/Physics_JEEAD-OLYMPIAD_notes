# Source Audit & Additions — Electromagnetic Waves

Primary reference: [`electromagnetic-waves/Electromagnetic-waves.md`](../../electromagnetic-waves/Electromagnetic-waves.md) (left strictly untouched).

## Independent Audit Findings
1. **Numerical Exemplars & Paper Key (`C1–C6`, `E1–E10`, `Q1–Q36`):** Every worked value in the source chapter was independently recomputed in Python (`test_exports.py`) and verified accurate within the stated constant tolerances ($c = 3.00\times 10^8\text{ m/s}$, $\varepsilon_0 = 8.85\times 10^{-12}\text{ F/m}$, $\mu_0 = 4\pi\times 10^{-7}\text{ H/m}$, $Z_0 = 377\,\Omega$, $hc = 1240\text{ eV}\cdot\text{nm}$).
2. **Bridges Added Explicitly for Complete Exam Readiness:**
   - Explicit **Malus's law & crossed-polaroid middle-sheet intensity** $I_{\rm out} = \frac{1}{8}I_0\sin^2(2\theta)$ alongside vector Lissajous polarisation (`JEE-06`).
   - Explicit **Hertzian dipole radiation intensity** $I(r,\theta) \propto \omega^4 p_0^2 \sin^2\theta / r^2$ and $\omega^4$ Rayleigh scattering bridge (`JEE-11`), completing the antenna remarks in §2.8 & §2.12.
   - Explicit **Lambertian diffuse plate**, **cone semi-angle drag formula**, **quarter-wave coating $Z_c = \sqrt{Z_1 Z_3}$**, **collisionless plasma cutoff $\omega_p$**, **Poynting–Robertson drag**, and **parallel-plate $\mathrm{TE}_m$ waveguide dispersion** across `Olympiad-02..06`.

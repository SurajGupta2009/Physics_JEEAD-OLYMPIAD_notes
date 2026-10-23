# Source Audit & Additions — Units, Dimensions & Measurement Errors

Primary reference: [`units-measurements/Units-measurements.md`](../../units-measurements/Units-measurements.md) (left strictly untouched).

## Corrections Carried Into These Short Notes
1. **Exemplar E7 Check Box (`Units-measurements.md` line ~808):** The source check box printed `"3% from mass + 3% from radius = 6% total"`, whereas $m = 100 \pm 1\text{ g}$ contributes $1\%$ and $3\Delta r/r = 3 \times 0.02/2.00 = 3\%$, giving **$4.0\%$** (matching the detailed solution below it). Explicit **4.0%** is stated in `JEE-08`.
2. **Exemplar E10 Check Box (`Units-measurements.md` line ~838):** The source check box wrote `"3 + 0.44 - 0.04 = 3.40 mm"` (mistaking $22 \times 0.01\text{ mm}$ for $0.44\text{ mm}$); the true value is $3.00 + 0.22 - 0.04 =$ **$3.18\text{ mm}$**, verified in `JEE-10` and `micrometer_sleeve`.
3. **Paper P35(c) Background-Subtraction Variance (`Units-measurements.md` line ~1455):** Clarified the exact Poisson variance $\sigma(R_{\rm net}) = \sqrt{R_{\rm tot}/t_{\rm on} + R_b/t_{\rm off}}$ in `Olympiad-05`, distinguishing a zero-uncertainty background rate ($\sqrt{2500}/10 = 5.0\text{ s}^{-1}$) from an independent equal-duration $10\text{ s}$ background run ($\sqrt{2500+500}/10 = 5.48\text{ s}^{-1}$).
4. **Paper P36(a) Vector Parity (`Units-measurements.md` line ~1468):** Clarified in `Olympiad-06` that both rotational isotropy ($\mathbf{p} = m\mathbf{v}\,f(\mathbf{v}\cdot\mathbf{v}/c^2)$) and analyticity at $\mathbf{v}=\mathbf{0}$ exclude odd powers of $v/c$.
5. **High-Frequency JEE Advanced Additions:** Added general $(1 - m/n)\,\mathrm{MSD}$ and retrograde vernier callipers (`JEE-09`), exact correlated differentials for parallel resistors $R_1 R_2/(R_1+R_2)$ and thin lenses/mirrors (`JEE-08`), and spherometer sagitta geometry (`JEE-10`).

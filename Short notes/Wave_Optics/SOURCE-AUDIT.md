# Source Audit — `wave-optics/Wave-optics.md`

Per repository rule, the primary source file [`../../wave-optics/Wave-optics.md`](../../wave-optics/Wave-optics.md) (`4,525` lines) was treated strictly read-only (`git diff wave-optics/Wave-optics.md` is empty). Every mathematical inconsistency, numerical evaluation slip, and answer-key mismatch found during line-by-line reading is documented below and resolved cleanly inside the rendered sheets.

---

## 1. Answer-Key vs Worked-Solution Mismatch in Double-Slit Envelopes (`Part 11 Q16`, line `3966` vs line `4331`)

- **What the source says:**
  - In **Part 11 Q16** (`line 3966`), a double-slit pattern has slit pitch $d$ and slit width $a$ with $d/a = 4$. The step-by-step worked solution correctly eliminates the missing orders $n = \pm 4$ at the first diffraction minimum and concludes that **$7$ bright interference maxima** ($n = -3, -2, -1, 0, +1, +2, +3$) appear strictly inside the central diffraction envelope.
  - However, the consolidated Answer Key table at `line 4331` prints **`16 | 9`** (counting the suppressed $n = \pm 4$ zeroes as bright fringes).
- **Resolution in Short Notes (`JEE-11`, Card 2):**
  - States the exact universal formula valid for **both integer and non-integer** $d/a$:
    $$N_{\mathrm{vis}} = 2\left\lceil \frac{d}{a} \right\rceil - 1$$
    giving $2(4) - 1 = \mathbf{7}$ for $d/a = 4.0$ vs $2(5) - 1 = \mathbf{9}$ for $d/a = 4.1$, and explicitly warns students about the classic off-by-two boundary trap.

---

## 2. Evanescent Penetration Depth Factor-of-$2$ Double-Counting & $\lambda_0$ vs $\lambda_{\mathrm{med}}$ Swap (`Part 7`, eq. `7.4` lines `2872–2889`, `7.9 Q5` line `3077`, `12.7` line `4490`)

- **What the source says:**
  - Equation `(7.4)` defines skin depth with $4\pi$ in the denominator while simultaneously writing transmission/intensity decay as $\exp(-2 g / d)$ in `§7.9 Q5` (`line 3077`), double-counting the intensity factor of $2$; additionally, vacuum $\lambda_0$ vs medium wavelength conventions fluctuate across `7.4`, `7.9 Q5`, and `12.7`.
- **Resolution in Short Notes (`Olympiad-04`, Cards 3 & 4 + Diagram 2):**
  - Defines the decay constant unambiguously in terms of **vacuum wavelength $\lambda_0$**:
    $$\kappa = \frac{2\pi}{\lambda_0}\sqrt{n_1^2 \sin^2 i - n_2^2}$$
  - Keeps **field amplitude decay length** $d_E = \dfrac{1}{\kappa}$ ($|E(z)| = E_0 e^{-\kappa z} = E_0 e^{-z/d_E}$) strictly separate from **intensity / FTIR decay length** $d_I = \dfrac{1}{2\kappa} = \dfrac{\lambda_0}{4\pi\sqrt{n_1^2\sin^2 i - n_2^2}}$ ($I(z) \propto e^{-2\kappa z} = e^{-z/d_I}$).

---

## 3. Degree/Radian Omission in Secondary Single-Slit Peak Ratio (`Part 5 §5.9 Q6`, line `2281`)

- **What the source says:**
  - At the second subsidiary diffraction maximum ($\beta_2 \approx 2.4590\pi = 7.7253\text{ rad}$), `line 2281` evaluates $\sin(2.46\text{ rad}) \approx 0.6301$ instead of $|\sin(2.4590\pi)| = 0.9917$, obtaining $0.66\%$ instead of the true Fraunhofer value **$1.65\%$**.
- **Resolution in Short Notes (`JEE-10`, Card 3 + `revalidate.py` root finder):**
  - Solves $\tan\beta_m = \beta_m$ numerically to machine precision and gives exact ratios $I_m / I_0 = \dfrac{1}{1 + \beta_m^2}$:
    $$I_0 : I_1 : I_2 : I_3 = 100 : \mathbf{4.72} : \mathbf{1.65} : \mathbf{0.83}$$

---

## 4. Inverted Monotonicity Word on Thinning Oil Film (`Part 8 §8.5 Q9`, line `3566`)

- **What the source says:**
  - The opening sentence on `line 3566` states that the constructively reflected wavelength *"increases"* as the oil film spreads and thins, immediately before algebraically proving $\lambda_{\mathrm{peak}} = \dfrac{4\mu t}{2m - 1}$ **decreases monotonically** ($550\text{ nm green} \to 435\text{ nm blue-violet} \to \text{UV / black film}$).
- **Resolution in Short Notes (`JEE-07`, Card 3):**
  - Explicitly highlights blue-shift toward UV followed by destructive **black film** ($R \to 0$ as $t \ll \lambda_0$) for air-soap-air and high-low-glass films with $\Delta_{\mathrm{flip}} = \lambda_0/2$.

---

## 5. Circular Polarisation Analyser Factor Error (`Part 6 §6.9 Q7`, line `2704`)

- **What the source says:**
  - Unpolarised light ($I_0$) passes through a linear polariser ($\to I_0/2$), then a lossless quarter-wave plate with fast axis at $45^\circ$ ($\to$ circularly polarised light of total intensity $I_0/2$), and finally a linear analyser. On `line 2704`, the note first writes $I_0/4$ and then erroneously "corrects" itself to $I_0/2$.
- **Resolution in Short Notes (`JEE-15`, Card 2 + `revalidate.py` Jones check):**
  - Proves via Jones projection that circularly polarised light of intensity $I_{\mathrm{circ}} = I_0/2$ contains equal, $90^\circ$-out-of-phase components of intensity $I_0/4$ along **every** orthogonal pair of axes, so a linear analyser at **any** angle $\theta$ transmits **$I_{\mathrm{out}} = I_0 / 4$**.

---

## 6. Missing Factor of $1/2$ in Summary Three-Polariser Formula (`Part 12 §12.6`, line `4482`) & Intentional Physical Sanity Checks (`§4.9 Q9`, `§8.5 Q3`)

- **What the source says:**
  - `line 4482` writes $I = I_0 \cos^2(90^\circ - A)\cos^2 A$ while stating *"giving $I_0/8$ at $A = 45^\circ$"* (dropping the initial $1/2$ factor for unpolarised input $I_0$).
  - `§4.9 Q9` (`179.5^\circ` air wedge) yields $\lambda_0 = 2.2\,\mu\text{m}$ (near-IR) and `§8.5 Q3` (`D_{20}/D_{10} = \sqrt{2}`) catches a miscounted ring-order difference; both pedagogical audits are preserved as explicit dimensional/order-count sanity checks.
- **Resolution in Short Notes (`JEE-13`, Card 3; `JEE-08`, Cards 1–3):**
  - Writes both forms side-by-side so neither can be confused:
    $$I_{\mathrm{out}} = \frac{1}{8}\,I_0 \sin^2(2A)\ \ (\text{unpolarised } I_0), \qquad I_{\mathrm{out}} = \frac{1}{4}\,I_{\mathrm{pol}} \sin^2(2A)\ \ (\text{polarised } I_{\mathrm{pol}})$$

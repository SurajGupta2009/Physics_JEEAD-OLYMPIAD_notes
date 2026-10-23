# Source Audit — `semiconductors/Semiconductors.md`

Per repository rule, the primary source file [`../../semiconductors/Semiconductors.md`](../../semiconductors/Semiconductors.md) (`1,680` lines) was treated strictly read-only (`git diff semiconductors/Semiconductors.md` is empty). Every internal discrepancy, implicit approximation, and numerical slip identified during full line-by-line reading (`lines 1–1680`) is documented below and resolved explicitly on the rendered sheets.

---

## 1. Silicon Atomic Density vs "One Impurity per Million Atoms" Wording (`§1` line `86`, `§3.4` line `262`, `§3.5` line `309`, `OL6` line `1121` vs `E3` line `702`)

- **What the source says:**
  - Worked example **E3** (`line 702`) uses the true atomic number density of crystalline silicon:
    $$N_{\text{Si}} = \frac{8}{a_{\text{Si}}^3} = \frac{8}{(5.43\times 10^{-10}\text{ m})^3} = 4.997\times 10^{28}\text{ m}^{-3} \approx 5.0\times 10^{28}\text{ m}^{-3}$$
    and correctly concludes that $N_d = 10^{21}\text{ m}^{-3}$ equals **one donor per $5\times 10^7$ ($50$ million) Si atoms**.
  - However, narrative prose in `§1` (`line 86`), `§3.4` (`line 262`), `§3.5` (`line 309`), and `OL6` (`line 1121`) repeatedly glosses $N_d = 10^{21}\text{ m}^{-3}$ as *"one impurity per million silicon atoms"*, whereas $1\text{ ppm}$ actually corresponds to $5.0\times 10^{22}\text{ m}^{-3}$.
- **Resolution in Short Notes (`JEE-02`, Card 3):**
  - States $N_{\text{Si}} = 5.0\times 10^{28}\text{ m}^{-3}$ explicitly and displays both exact ratios side-by-side:
    - $N_d = 10^{21}\text{ m}^{-3} \iff 1\text{ donor per } \mathbf{5\times 10^7}\text{ Si atoms}$,
    - $1\text{ ppm} \iff N_d = \mathbf{5.0\times 10^{22}\text{ m}^{-3}}$.

---

## 2. Intrinsic Carrier Scaling $n_i(T)$ Omitting the $T^{3/2}$ Prefactor (`§3.3` line `215` & `F27.5` line `226`)

- **What the source says:**
  - Using $E_g = 1.12\text{ eV}$ so $E_g / (2 k_B \cdot 300\text{ K}) \approx 21.65$, doubling temperature from $300\text{ K}$ to $600\text{ K}$ gives $\exp(10.82) \approx 5.0\times 10^4$, which `§3.3` (`line 215`) quotes as the full ratio $n_i(600\text{ K}) / n_i(300\text{ K})$ while dropping $(600/300)^{3/2} = 2\sqrt{2} \approx 2.828$.
  - Similarly, `F27.5` (`line 226`) sketches $n_i(400\text{ K}) / n_i(300\text{ K}) \approx 800$, whereas the exact formula gives $(4/3)^{3/2}\exp(21.65 / 4) \approx \mathbf{346}$.
- **Resolution in Short Notes (`JEE-02`, Card 1 & Diagram `ni_arrhenius`):**
  - Evaluates the full density-of-states law $n_i(T) = A\,T^{3/2}\exp\!\bigl(-E_g / (2 k_B T)\bigr)$ directly, clarifying that pure exponential scaling gives $\sim 5\times 10^4$ while exact $T^{3/2}\exp(-E_g/2k_B T)$ gives $\mathbf{1.4\times 10^5}$ at $600\text{ K}$ and $\mathbf{3.5\times 10^2}$ at $400\text{ K}$.

---

## 3. Abrupt Junction Poisson Depletion Width: One-Sided Step vs Symmetric Doping (`Q9` line `840`, `OL3` line `1070`, `P29` line `1506`)

- **What the source says:**
  - `OL3` (`line 1070`) and `P29` (`line 1506`) write $W = \sqrt{\dfrac{2\varepsilon(V_0 + V_R)}{e N}}$ with a single symbol $N$ without specifying one-sided ($p^+ n$) vs symmetric ($N_a = N_d = N$) doping, and `Q9` (`line 840`) states *"quadrupling reverse bias doubles depletion width"* without noting $V_0 + V_R$.
- **Resolution in Short Notes (`JEE-04` Card 2, `JEE-05` Card 4, `Olympiad-02` Card 2):**
  - States the exact general two-sided formula with **reduced doping** $N_{\text{eff}} = \dfrac{N_a N_d}{N_a + N_d}$:
    $$W = \sqrt{\frac{2\varepsilon_r \varepsilon_0 (V_0 + V_R)}{e\,N_{\text{eff}}}}$$
    and shows both limits explicitly:
    1. **One-sided step junction ($p^+ n$, $N_a \gg N_d = N$):** $N_{\text{eff}} \to N$, reproducing `P29`'s $W = 2.5\,\mu\text{m}$ and $C_j = 41\text{ pF}$ at $N = 10^{21}\text{ m}^{-3}$, $V_0 + V_R = 4.7\text{ V}$.
    2. **Symmetric junction ($N_a = N_d = N$):** $N_{\text{eff}} = N/2$, making $W$ larger by $\sqrt{2}$.
  - Explicitly notes that $W \propto \sqrt{V_0 + V_R}$ strictly doubles when **total barrier $(V_0 + V_R)$** quadruples (or when $V_R \gg V_0$).

---

## 4. Dynamic CMOS Power: Activity Factor $\alpha_{\text{sw}}$ per Clock Cycle vs Single Edge (`§3.13` line `520`, `OL11` line `1185`, `P36` line `1595`)

- **What the source says:**
  - Charging a node capacitance $C$ from $0$ to $V_{DD}$ draws $C V_{DD}^2$ from the supply, dissipating $\frac{1}{2} C V_{DD}^2$ in the pull-up PMOS and storing $\frac{1}{2} C V_{DD}^2$ on $C$, which is then dissipated in the pull-down NMOS on the $V_{DD} \to 0$ transition ($E_{\text{full cycle}} = C V_{DD}^2$).
  - `OL11` (`line 1185`) and `P36` (`line 1595`) compute $P = \frac{1}{2} N_{\text{sw}} C V^2 f$ (`500 W` and `810 W`), which corresponds cleanly to **one logic transition per clock edge** ($\alpha_{\text{sw}} = 1/2$ full charge-discharge cycles per clock period).
- **Resolution in Short Notes (`Olympiad-06`, Card 3):**
  - Writes both exact expressions cleanly:
    $$E_{0\to V\to 0} = C V_{DD}^2\ \ \bigl({\tfrac{1}{2}} C V_{DD}^2\text{ per single edge}\bigr), \qquad P_{\text{dyn}} = \alpha_{\text{sw}} N C V_{DD}^2 f$$
    and verifies `OL11` (`500 W`) and `P36` (`810 W`) at $\alpha_{\text{sw}} = 1/2$.

---

## 5. Effective Donor Bohr Radius vs Orbit Diameter in Lattice Units (`§3.4` line `273` vs `E4` line `718` & `OL1` line `1042`)

- **What the source says:**
  - `E4` (`line 718`) and `OL1` (`line 1042`) compute $a^* = a_0\,\varepsilon_r / (m^*/m_0) = 0.0529\text{ nm}\times 11.7 / 0.26 = 2.38\text{ nm} \approx 4.4\,a_{\text{Si}}$ ($a_{\text{Si}} = 0.543\text{ nm}$), whereas `§3.4` (`line 273`) describes the orbit as spanning *"roughly a dozen lattice spacings"*.
- **Resolution in Short Notes (`Olympiad-01`, Card 1):**
  - States both radius $a^* = 2.4\text{ nm} \approx 4.4\,a_{\text{Si}}$ and orbit diameter $2 a^* = 4.8\text{ nm} \approx 8.8\,a_{\text{Si}}$ explicitly (enclosing $> 1{,}400$ silicon atoms inside the sphere $\frac{4}{3}\pi (a^*)^3 N_{\text{Si}}$, justifying the continuum dielectric $\varepsilon_r = 11.7$).

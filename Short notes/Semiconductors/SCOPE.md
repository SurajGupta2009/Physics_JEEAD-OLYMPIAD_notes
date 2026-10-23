# Scope & JEE vs Olympiad Classification — Semiconductors & Electronic Devices

## Guiding Boundary

Every concept, derivation, diagram, and worked-problem insight from [`../../semiconductors/Semiconductors.md`](../../semiconductors/Semiconductors.md) (`1,680` lines, Parts `0–14`, `E1–E12`, `Q1–Q28`, `OL1–OL12`, `P1–P36`, `D27.1–D27.18`) is preserved and split strictly by **syllabus relevance** rather than difficulty:

- **Part I — JEE Main + Advanced (`JEE-01` .. `JEE-12`, 12 A4 sheets, 48 cards, 24 analytic diagrams):** Complete NCERT + JEE Main + JEE Advanced semiconductor physics and electronics syllabus — discrete atomic orbitals splitting into $4N$ valence + $4N$ conduction states (`§3.1–3.2`), band gap classification of metals/semiconductors/insulators, photon absorption cutoff $\lambda_c = hc/E_g$, opposite temperature coefficients of resistance ($\alpha > 0$ in metals vs $\alpha < 0$ in intrinsic semiconductors), mass-action law $n p = n_i^2$, donor/acceptor neutrality & exact Si atomic density ratios, two-carrier drift conductivity $\sigma = e(n\mu_e + p\mu_h)$, Fick diffusion, Einstein relation $D/\mu = k_B T / e$, equilibrium p-n space-charge electric field and zero net current ($I_{\text{diff}} + I_{\text{drift}} = 0$), Shockley diode equation, AC dynamic vs DC static resistance, Zener tunnelling vs avalanche breakdown, half-wave/centre-tap/bridge rectifiers (PIV, $V_{\text{dc}}$, ripple frequency, capacitor surge & peak ripple), series/shunt clippers and DC clampers, Zener voltage stabilization under line/load variations, photodiodes (reverse bias), solar cells ($V_{\text{oc}}$, $I_{\text{sc}}$, FF, $\eta$, 4th-quadrant operation), direct-bandgap LEDs, NPN/PNP BJT structure ($\alpha$, $\beta$, 4 bias modes, mandatory saturation clamp $I_C = \min(\beta I_B, I_{C,\max})$, DC load line), CE amplifier ($180^\circ$ phase inversion, voltage/current/power gains, DC battery energy source) & BJT logic inverter, diode OR/AND gates, RTL NOT/NOR/NAND gates, Boolean identities, De Morgan bubble duality, universal NAND/NOR realizations, half/full adders, and a 14-trap JEE master triage sheet.
- **Part II — Olympiad / Specialised Extensions (`Olympiad-01` .. `Olympiad-06`, 6 A4 sheets, 24 cards, 12 analytic diagrams):** INPhO / IPhO / APhO device physics & solid-state extensions (`Part 8 OL1–OL12` + `Part 13 P29–P36`) — hydrogenic effective-mass donor model ($E_d = 13.6\,(m^*/m_0)/\varepsilon_r^2 \approx 25\text{ meV}$, Bohr radius $a^* \approx 2.4\text{ nm}$), Arrhenius freeze-out / extrinsic plateau / intrinsic takeover and chemical-potential motion $E_F(T)$, Boltzmann built-in barrier $V_0 = V_T \ln(N_a N_d / n_i^2)$, Poisson depletion width $W$ & Mott-Schottky $1/C_j^2$ varactor tuning, Hall effect carrier-sign & mobility metrology (including two-carrier zero $p\mu_h^2 = n\mu_e^2$), diode $-2\text{ mV/K}$ CTAT thermometry & $1.22\text{ V}$ Brokaw PTAT+CTAT bandgap reference, Shockley-Queisser $33\%$ single-junction limit & shaded-panel bypass diodes, LED resistor vs constant-current thermal stability, Poisson shot noise vs Johnson-Nyquist thermal noise ($I_{\text{cross}} = 2k_B T / (e R_L)$) & transimpedance photoreceivers, and sub-$5\text{ nm}$ CMOS WKB gate-oxide tunnelling, high-$\kappa$ $\text{HfO}_2$ HKMG, FinFET/GAA electrostatics, and Dennard power wall ($P_{\text{dyn}} = \alpha_{\text{sw}} N C V^2 f$).

## Source Part Mapping

| Source Section in `Semiconductors.md` | Target Sheets |
|---|---|
| Parts 0–2 & §3.1–3.2: Atomic Bands, Band Gaps & $\rho(T)$ | `JEE-01`, `JEE-12` |
| §3.3–3.5: Intrinsic Crystals, Mass Action & Doping (`E1–E4`) | `JEE-02`, `Olympiad-01` |
| §3.5 & Transport: Drift, Diffusion & Einstein Relation (`E5`, `P3–P4`) | `JEE-03`, `Olympiad-02` |
| §3.6–3.7: Equilibrium & Biased p-n Junction (`E6–E7`, `Q7–Q13`) | `JEE-04`, `JEE-05`, `Olympiad-02` |
| §3.8: Rectifiers, Filters, Clippers & Clampers (`E8`, `Q14–Q17`, `P12–P15`) | `JEE-06` |
| §3.9: Zener Regulator, Photodiode, Solar Cell & LED (`E9`, `Q18–Q20`, `P16–P21`) | `JEE-07`, `Olympiad-04`, `Olympiad-05` |
| §3.10–3.11: BJT Modes, Load Line, CE Amplifier & Switch (`E10–E11`, `Q21–Q25`, `P22–P26`) | `JEE-08`, `JEE-09` |
| §3.12: Digital Logic, Boolean Algebra, Universal Gates & Adders (`E12`, `Q26–Q28`, `P27–P28`) | `JEE-10`, `JEE-11` |
| Part 8 (`OL1–OL12`) & Part 13 (`P29–P36`): Olympiad Extensions | `Olympiad-01` .. `Olympiad-06` |
| Parts 9–12 & 14: Master Synthesis, Misconceptions (`M1–M14`) & Marking Traps | `JEE-12` & WATCH notes across all 18 sheets |

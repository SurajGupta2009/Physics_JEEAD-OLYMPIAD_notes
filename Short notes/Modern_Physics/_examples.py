"""Worked-number blocks: one per sheet, appended as the last numbered move.

Each entry is (heading, [blocks]) in the same grammar as the content modules.
The numbers are recomputed from the source's data rather than copied, so a
disagreement with the printed exemplar is a finding, not a typo.
"""

EX = {}

EX['JEE-01-rutherford'] = ('A worked closest approach', [
    ('p', 'A 5 MeV alpha on gold, head-on. All kinetic energy becomes potential energy at the turning point:'),
    ('m', r'r_{\min}=\frac{2(79)(1.44\ \mathrm{eV\,nm})}{5\times10^6\ \mathrm{eV}}=4.55\times10^{-5}\ \mathrm{nm}'),
    ('m', r'r_{\min}=45.5\ \mathrm{fm}\quad\mathrm{against}\ R\approx7\ \mathrm{fm}'),
    ('n', 'six nuclear radii of clearance: the alpha never touched the nucleus, so the Coulomb law held'),
])

EX['JEE-02-closest-approach'] = ('A worked 30 MeV probe', [
    ('p', 'Raise the beam to 30 MeV on the same gold foil and see how much room is left:'),
    ('m', r'r_{\min}=\frac{227.5\ \mathrm{eV\,nm}}{3\times10^7\ \mathrm{eV}}=7.6\times10^{-6}\ \mathrm{nm}'),
    ('m', r'=7.6\ \mathrm{fm}\approx R_{\mathrm{Au}}'),
    ('n', 'at about 32 MeV the alpha touches the surface and sin⁻⁴ scattering starts to fail'),
])

EX['JEE-03-standing-wave'] = ('A worked wavelength check', [
    ('p', 'The n = 3 orbit of hydrogen, checked against de Broglie directly:'),
    ('m', r'v_3=7.29\times10^5\ \mathrm{m/s},\quad \lambda=\frac{h}{m_ev_3}=9.97\ \mathrm{\AA}'),
    ('m', r'3\lambda=29.9\ \mathrm{\AA}=2\pi(4.76\ \mathrm{\AA})\ \checkmark'),
    ('n', 'a 10 % error in n would leave the wave 36 degrees out of phase, cancelling itself'),
])

EX['JEE-04-bohr-ladder'] = ('A worked ionisation ladder', [
    ('p', 'Ionise hydrogen from n = 2, and then from n = 3:'),
    ('m', r'\mathrm{IE}_2=\frac{13.6}{4}=3.40\ \mathrm{eV},\qquad \mathrm{IE}_3=\frac{13.6}{9}=1.51\ \mathrm{eV}'),
    ('m', r'\lambda_{\mathrm{edge}}=\frac{1240}{3.40}=365\ \mathrm{nm}'),
    ('n', 'the Balmer edge at 365 nm is the same number seen as a wavelength'),
])

EX['JEE-05-series'] = ('A worked series limit', [
    ('p', 'The two ends of the Balmer series, computed from the same rule:'),
    ('m', r'\lambda_{\max}=\frac{1}{R}\frac{4\cdot9}{5}=656\ \mathrm{nm}\ (n_i=3)'),
    ('m', r'\lambda_{\min}=\frac{4}{R}=364.6\ \mathrm{nm}\ (n_i\to\infty)'),
    ('n', 'everything between is visible; beyond 364.6 nm the series ends in a continuum'),
])

EX['JEE-06-excitation'] = ('A worked threshold ladder', [
    ('p', 'Which levels can a 12.5 eV electron reach in hydrogen?'),
    ('m', r'E_2=10.2,\quad E_3=12.09,\quad E_4=12.75\ \mathrm{eV}'),
    ('m', r'12.5>12.09\ \mathrm{but}\ 12.5<12.75\ \Rightarrow\ n\le3'),
    ('n', 'and the surplus 0.41 eV stays with the electron as kinetic energy'),
])

EX['JEE-07-hydrogenic'] = ('A worked Li2+ line', [
    ('p', 'The 2 → 1 resonance line of Li²⁺ (Z = 3):'),
    ('m', r'\Delta E=13.6(9)\left(\frac{1}{1}-\frac{1}{4}\right)=91.8\ \mathrm{eV}'),
    ('m', r'\lambda=\frac{1240}{91.8}=13.5\ \mathrm{nm}'),
    ('n', 'soft X-ray, and exactly one ninth of hydrogen’s 121.6 nm: λ ∝ 1/Z²'),
])

EX['JEE-08-quantum-numbers'] = ('A worked cascade count', [
    ('p', 'An atom in n = 5 cascades to the ground state. How many spectral lines, and how many from n = 5 alone?'),
    ('m', r'N=\frac{5\cdot4}{2}=10\ \mathrm{lines}'),
    ('m', r'\mathrm{from}\ n=5\ \mathrm{only}:\ 5\rightarrow4,3,2,1=4'),
    ('n', 'the series count is n − n_f; the cascade count is all pairs'),
])

EX['JEE-09-photon'] = ('A worked photon count', [
    ('p', 'A 5 mW laser at 633 nm: how many photons leave per second, and what force does the beam exert if absorbed?'),
    ('m', r'E=\frac{1240}{633}=1.96\ \mathrm{eV}=3.14\times10^{-19}\ \mathrm{J}'),
    ('m', r'\dot N=\frac{5\times10^{-3}}{3.14\times10^{-19}}=1.6\times10^{16}\ \mathrm{s^{-1}}'),
    ('n', 'F = P/c = 1.7×10⁻¹¹ N — a piconewton, and optical tweezers use exactly this'),
])

EX['JEE-10-photoelectric'] = ('A worked zinc threshold', [
    ('p', 'Zinc has φ = 4.3 eV. What is the longest wavelength that ejects electrons, and what happens at 250 nm?'),
    ('m', r'\lambda_0=\frac{1240}{4.3}=288\ \mathrm{nm}'),
    ('m', r'250\ \mathrm{nm}:\ K_{\max}=\frac{1240}{250}-4.3=4.96-4.3=0.66\ \mathrm{eV}'),
    ('n', 'visible light (400–700 nm) never discharges zinc: the photons are simply too poor'),
])

EX['JEE-11-stopping'] = ('A worked graph reading', [
    ('p', 'A V_s against f line passes through (5.0×10¹⁴ Hz, 0) and (11.0×10¹⁴ Hz, 2.48 V).'),
    ('m', r'\mathrm{slope}=\frac{2.48}{6.0\times10^{14}}=4.13\times10^{-15}\ \mathrm{V\,s}'),
    ('m', r'h=e(4.13\times10^{-15})=6.62\times10^{-34}\ \mathrm{J\,s},\quad \phi=hf_0=2.07\ \mathrm{eV}'),
    ('n', 'the slope must be h/e = 4.14×10⁻¹⁵ V s for every metal ever measured'),
])

EX['JEE-12-photocell'] = ('A worked quantum efficiency', [
    ('p', 'A photocell at 400 nm receives 1 mW and delivers 20 µA.'),
    ('m', r'\dot N_\gamma=\frac{10^{-3}}{4.97\times10^{-19}}=2.0\times10^{15}\ \mathrm{s^{-1}}'),
    ('m', r'\dot N_e=1.25\times10^{14}\ \mathrm{s^{-1}}\ \Rightarrow\ \eta=6.2\ \%'),
    ('n', 'a few per cent is normal for a plain metal; caesiated surfaces reach tens of per cent'),
])

EX['JEE-13-debroglie'] = ('A worked wavelength pair', [
    ('p', 'Electrons at 100 V and at 10 kV:'),
    ('m', r'\lambda_{100}=\frac{1.226}{\sqrt{100}}=0.123\ \mathrm{nm}'),
    ('m', r'\lambda_{10^4}=0.0123\ \mathrm{nm}'),
    ('n', 'a hundredfold voltage gives exactly a tenfold shorter wave: λ ∝ V^(−1/2)'),
])

EX['JEE-14-davisson-germer'] = ('A worked angle', [
    ('p', '54 V electrons on nickel planes of 0.91 Å:'),
    ('m', r'\lambda=1.67\ \mathrm{\AA},\quad \sin\theta=\frac{1.67}{1.82}=0.918'),
    ('m', r'\theta=66^{\circ}\quad\mathrm{observed}\ 65^{\circ}'),
    ('n', 'the one-degree gap is the rounding of d in the textbook value, not a failure of the theory'),
])

EX['JEE-15-uncertainty'] = ('A worked ground state', [
    ('p', 'Evaluate the two terms of E(r) at r = 0.5 Å:'),
    ('m', r'K=\frac{\hbar^2}{2m_er^2}=15.3\ \mathrm{eV},\qquad U=-\frac{ke^2}{r}=-28.8\ \mathrm{eV}'),
    ('m', r'E=15.3-28.8=-13.5\ \mathrm{eV}'),
    ('n', 'the exact answer is −13.6 eV: the estimate misses by one per cent, and the physics is all there'),
])

EX['Olympiad-01-xray-continuous'] = ('A worked cutoff check', [
    ('p', 'A tube runs at 50 kV. What is the shortest wavelength, and what does 100 kV do to it?'),
    ('m', r'\lambda_{\min}=\frac{1.24\times10^6}{5\times10^4}=24.8\ \mathrm{pm}'),
    ('m', r'100\ \mathrm{kV}:\ 12.4\ \mathrm{pm}'),
    ('n', 'plot λ_min against 1/V and the slope is hc/e: the Duane-Hunt measurement of h'),
])

EX['Olympiad-02-xray-characteristic'] = ('A worked threshold', [
    ('p', 'Copper’s K shell binds 8.98 keV. What is the minimum tube voltage for its Kα line?'),
    ('m', r'V_{\mathrm{th}}=\frac{8.98\ \mathrm{keV}}{e}=8.98\ \mathrm{kV}'),
    ('m', r'V=4.5\ \mathrm{kV}:\ \mathrm{cutoff}\ \frac{1.24\times10^6}{4500}=276\ \mathrm{pm},\ \mathrm{no\ lines}'),
    ('n', 'below threshold the continuous spectrum survives and the lines vanish: two masters, two behaviours'),
])

EX['Olympiad-03-absorption'] = ('A worked half-value stack', [
    ('p', 'Lead at 100 keV has x½ = 0.123 mm. What thickness leaves one per cent?'),
    ('m', r'n=\frac{\log(0.01)}{\log(0.5)}=6.64\ \mathrm{half\ layers}'),
    ('m', r'x=6.64(0.123)=0.82\ \mathrm{mm}'),
    ('n', 'a lead apron is 0.25–0.5 mm: enough for scattered diagnostic radiation, not for a beam'),
])

EX['Olympiad-04-bragg'] = ('A worked Avogadro', [
    ('p', 'NaCl: d = 0.282 nm, ρ = 2165 kg/m³, M = 58.44 g/mol.'),
    ('m', r'N_A=\frac{0.05844}{2(2165)(2.82\times10^{-10})^3}=\frac{0.05844}{9.71\times10^{-26}}'),
    ('m', r'=6.02\times10^{23}\ \mathrm{mol^{-1}}'),
    ('n', 'a wavelength, an angle and a balance reproduce a constant measured in electrochemistry'),
])

EX['Olympiad-05-compton'] = ('A worked back-scatter', [
    ('p', 'A 100 keV photon is scattered through 180°.'),
    ('m', r'\Delta\lambda=4.86\ \mathrm{pm},\qquad x=\frac{100}{511}=0.196'),
    ('m', r'K_e=100\frac{2(0.196)}{1+2(0.196)}=28\ \mathrm{keV}'),
    ('n', 'the maximum energy transfer is at 180°, and it is still well below the photon energy'),
])

EX['Olympiad-06-compton-invariant'] = ('A worked invariant', [
    ('p', 'Use the same invariant on a 2 MeV photon scattering at 60°.'),
    ('m', r'\Delta\lambda=2.426(1-\cos60^{\circ})=1.21\ \mathrm{pm}'),
    ('m', r'\lambda=0.62\ \mathrm{pm}\ \Rightarrow\ \lambda^{\prime}=1.83\ \mathrm{pm}'),
    ('n', 'the fractional shift is 195 %: at MeV energies the photon loses most of its energy'),
])

EX['Olympiad-07-inverse-compton'] = ('A worked boost', [
    ('p', 'Microwave photons at 6×10⁻⁴ eV hit electrons with γ = 10³.'),
    ('m', r"\epsilon'\approx4\gamma^2\epsilon=4(10^6)(6\times10^{-4})=2.4\times10^{3}\ \mathrm{eV}"),
    ('m', r'2.4\ \mathrm{keV}=\ \mathrm{soft\ X\ ray}'),
    ('n', 'the same electrons synchrotron-radiate at keV too: two channels, one population'),
])

EX['Olympiad-08-pair-production'] = ('A worked threshold', [
    ('p', 'A 2 MeV photon converts near a nucleus.'),
    ('m', r'K_{\mathrm{total}}=2.00-1.022=0.98\ \mathrm{MeV}'),
    ('m', r'\mathrm{shared\ as}\ K_++K_-=0.98\ \mathrm{MeV}'),
    ('n', 'in a magnetic field the two tracks curl opposite ways with the same radius if the sharing is equal'),
])

EX['Olympiad-09-moseley'] = ('A worked prediction', [
    ('p', 'Predict the Kα wavelength of silver (Z = 47) from copper’s 154 pm.'),
    ('m', r'\lambda\propto\frac{1}{(Z-1)^2}:\ \lambda_{\mathrm{Ag}}=154\frac{28^2}{46^2}=57\ \mathrm{pm}'),
    ('m', r'f=\frac{3}{4}cR(46)^2=5.3\times10^{18}\ \mathrm{Hz}'),
    ('n', 'the measured value is 56 pm: one line, one constant, every element'),
])

EX['Olympiad-10-collapse'] = ('A worked collapse time', [
    ('p', 'Evaluate the Larmor-integral lifetime from a₀:'),
    ('m', r'C=\frac{e^2}{6\pi\varepsilon_0c^3}\left(\frac{ke^2}{m_e}\right)^2=6.3\times10^{-55}\ \mathrm{J\,m^4}'),
    ('m', r'\tau=\frac{ke^2a_0^3}{6C}=1.6\times10^{-11}\ \mathrm{s}'),
    ('n', 'τc ≈ 5 mm and about 10⁷ orbits: slow, and fatal'),
])

EX['Olympiad-11-correspondence'] = ('A worked n = 100 check', [
    ('p', 'Compare orbital and photon frequency at n = 100:'),
    ('m', r'f_{\mathrm{orb}}=\frac{v}{2\pi r}=6.58\times10^9\ \mathrm{Hz}'),
    ('m', r'f_{\mathrm{ph}}=\frac{\Delta E}{h}=6.68\times10^9\ \mathrm{Hz}'),
    ('n', 'ratio 1.015, exactly 1 + 3/(2n) with n = 100'),
])

EX['Olympiad-12-exotic-atoms'] = ('A worked positronium line', [
    ('p', 'The 2 → 1 line of positronium:'),
    ('m', r'\Delta E=6.8\left(\frac{3}{4}\right)=5.1\ \mathrm{eV}'),
    ('m', r'\lambda=\frac{1240}{5.1}=243\ \mathrm{nm}'),
    ('n', 'exactly twice hydrogen’s 121.6 nm, because μ is exactly half'),
])

EX['Olympiad-13-franck-hertz'] = ('A worked dip position', [
    ('p', 'Where do the first three dips sit, and why not at exactly 4.9 V?'),
    ('m', r'V_{\mathrm{dip}}\approx V_{\mathrm{contact}}+n(4.9\ \mathrm{V}),\quad n=1,2,3'),
    ('m', r'4.9,\ 9.8,\ 14.7\ \mathrm{V}\ \mathrm{plus\ a\ constant\ offset}'),
    ('n', 'the spacing is the measurement; the offset is contact potential and is subtracted, not explained'),
])

EX['Olympiad-14-waiting-time'] = ('A worked dim-beam estimate', [
    ('p', 'Moonlight on one atom: I = 10⁻³ W/m², A = 10⁻²⁰ m², φ = 2 eV.'),
    ('m', r'P=IA=10^{-23}\ \mathrm{W},\qquad t=\frac{3.2\times10^{-19}}{10^{-23}}=3.2\times10^{4}\ \mathrm{s}'),
    ('m', r'\approx9\ \mathrm{hours},\quad \mathrm{observed}\ <10^{-9}\ \mathrm{s}'),
    ('n', 'thirteen orders of magnitude: the wave picture is not wrong by a factor, it is wrong'),
])

EX['Olympiad-15-matter-wave-speeds'] = ('A worked c² product', [
    ('p', 'An electron moving at 0.6c:'),
    ('m', r'v_p=\frac{c^2}{0.6c}=1.67c,\qquad v_g=0.6c'),
    ('m', r'v_pv_g=c^2\ \checkmark'),
    ('n', 'the crests outrun light while the particle does not; only the packet carries information'),
])


# ---------------------------------------------------------------- nuclear, JEE
EX['JEE-16-nuclear-size'] = ('A worked uranium radius', [
    ('p', 'Uranium-238: radius and the mass of a 5 cm³ spoonful.'),
    ('m', r'R=1.2(238)^{1/3}=7.44\ \mathrm{fm},\qquad V=\frac{4}{3}\pi R^3=1.72\times10^{-42}\ \mathrm{m^3}'),
    ('m', r'm=\rho V=(2.3\times10^{17})(5\times10^{-6})=1.2\times10^{12}\ \mathrm{kg}'),
    ('n', 'a billion tonnes in a teaspoon — the number that makes the density believable'),
])

EX['JEE-17-binding-curve'] = ('A worked mass defect', [
    ('p', 'Helium-4 from its parts: 2 hydrogen atoms and 2 neutrons.'),
    ('m', r'\Delta m=2(1.007825)+2(1.008665)-4.002603=0.030377\ \mathrm{u}'),
    ('m', r'B=0.030377(931.5)=28.30\ \mathrm{MeV},\qquad B/A=7.07\ \mathrm{MeV}'),
    ('n', 'the deuteron gives 1.11 per nucleon: that factor 6.4 is why fusion past hydrogen pays'),
])

EX['JEE-18-valley'] = ('A worked valley floor', [
    ('p', 'Most stable charge for A = 100 and A = 238.'),
    ('m', r'Z_0(100)=\frac{100}{2+0.0154(100)^{2/3}}=\frac{100}{2.33}=42.9'),
    ('m', r'Z_0(238)=\frac{238}{2+0.0154(238)^{2/3}}=92.0'),
    ('n', 'molybdenum–ruthenium for the first, uranium itself for the second'),
])

EX['JEE-19-q-value'] = ('A worked alpha split', [
    ('p', 'Polonium-210 decays with Q = 5.40 MeV.'),
    ('m', r'K_\alpha=\frac{206}{210}(5.40)=5.30\ \mathrm{MeV},\qquad K_d=0.10\ \mathrm{MeV}'),
    ('m', r'\sqrt{2m_\alpha K_\alpha}=\sqrt{2m_dK_d}'),
    ('n', 'the daughter recoils with 2 % of the energy and a hundred times less speed'),
])

EX['JEE-20-beta'] = ('Two worked endpoints', [
    ('p', 'Carbon-14 and nitrogen-13, with the electron rule applied.'),
    ('m', r'Q_{\beta^-}=(14.003242-14.003074)(931.5)=0.156\ \mathrm{MeV}'),
    ('m', r'Q_{\beta^+}=(13.005739-13.003355-0.001098)(931.5)=1.20\ \mathrm{MeV}'),
    ('n', 'the 2m_e term is 1.022 MeV — larger than most beta Q-values, which is why β⁺ needs a big parent'),
])

EX['JEE-21-decay-law'] = ('A worked working day', [
    ('p', 'Tc-99m (T½ = 6 h) prepared at 800 MBq at 08:00; Co-60 mass for 1 Ci.'),
    ('m', r'A(12\ \mathrm{h})=800\times2^{-2}=200\ \mathrm{MBq}'),
    ('m', r'N=\frac{3.7\times10^{10}}{4.17\times10^{-9}}=8.9\times10^{18}\ \Rightarrow\ m=0.88\ \mathrm{mg}'),
    ('n', 'a curie of a years-scale isotope is a speck; a curie of radium is a gram'),
])

EX['JEE-22-dating'] = ('A worked carbon age', [
    ('p', 'A bone gives 10 disintegrations per minute per gram; living tissue gives 15.'),
    ('m', r't=\frac{5730}{\ln2}\ln\frac{15}{10}=8267(0.405)=3350\ \mathrm{y}'),
    ('m', r'\frac{A}{A_0}=2^{-t/T_{1/2}}=0.667'),
    ('n', 'between one and two half-lives, which is the range where the method is most reliable'),
])

EX['JEE-23-chains'] = ('A worked generator', [
    ('p', 'Parent T½ = 18 h, daughter T½ = 6 h: find the ratio and the peak.'),
    ('m', r'\lambda_1=0.0385\ \mathrm{h^{-1}},\ \lambda_2=0.1155\ \mathrm{h^{-1}}'),
    ('m', r'\frac{A_2}{A_1}=\frac{0.1155}{0.0770}=1.50,\qquad t_{\max}=\frac{\ln3}{0.0770}=14.3\ \mathrm{h}'),
    ('n', 'elute the daughter at 14 h, not at the end of the day'),
])

EX['JEE-24-fission'] = ('A worked power balance', [
    ('p', 'A 1 GW electric plant at 33 % efficiency.'),
    ('m', r'P_{\mathrm{th}}=3.0\ \mathrm{GW}:\ \frac{3\times10^9}{200(1.602\times10^{-13})}=9.4\times10^{19}\ \mathrm{s^{-1}}'),
    ('m', r'm=\frac{3(1.05)}{1}=3.2\ \mathrm{kg/day\ of\ U\!-\!235}'),
    ('n', 'three tonnes of coal would do the same job — the factor 10⁶ in one line'),
])

EX['JEE-25-fusion'] = ('A worked barrier', [
    ('p', 'Deuterium plus tritium, and the classical temperature of the proton barrier.'),
    ('m', r'Q=(0.018883\ \mathrm{u})(931.5)=17.6\ \mathrm{MeV}'),
    ('m', r'T=\frac{0.72\ \mathrm{MeV}}{8.617\times10^{-11}\ \mathrm{MeV/K}}=8.4\times10^{9}\ \mathrm{K}'),
    ('n', 'the D–T reaction is the easiest one, and it still needs 100 MK in the lab'),
])

# ----------------------------------------------------------- nuclear, Olympiad
EX['Olympiad-16-geiger-nuttall'] = ('A worked lifetime swing', [
    ('p', 'U-238 (4.27 MeV, 4.5×10⁹ y) against Po-212 (8.95 MeV, 3×10⁻⁷ s).'),
    ('m', r'\frac{1}{\sqrt{4.27}}=0.484,\qquad \frac{1}{\sqrt{8.95}}=0.334'),
    ('m', r'\log_{10}T_{1/2}\ \mathrm{changes\ by}\ \sim24\ \mathrm{decades}'),
    ('n', 'the prefactor is unknown to a factor of 10; the exponential is not'),
])

EX['Olympiad-17-fission-barrier'] = ('A worked pairing bonus', [
    ('p', 'The excitation of U-236 against its barrier.'),
    ('m', r'\delta=\frac{12}{\sqrt{236}}=0.78\ \mathrm{MeV}'),
    ('m', r'E^*_{236}=5.7+0.78=6.5\ \mathrm{MeV}>B_f\approx6\ \mathrm{MeV}'),
    ('n', 'U-239 gets 4.8 MeV and stays below the barrier: no pairing bonus, no thermal fission'),
])

EX['Olympiad-18-valley-floor'] = ('A worked coefficient', [
    ('p', 'Check the 0.0154 in the valley formula.'),
    ('m', r'\frac{a_c}{2a_a}=\frac{0.71}{2(23.2)}=0.0153'),
    ('m', r'Z_0(56)=\frac{56}{2+0.0153(56)^{2/3}}=27.0'),
    ('n', 'iron sits at Z = 26: the liquid drop is one unit high, and the shell closure explains it'),
])

EX['Olympiad-19-transient'] = ('A worked maximum', [
    ('p', 'λ₁ = 0.02 h⁻¹, λ₂ = 0.10 h⁻¹: ratio and peak time.'),
    ('m', r'\frac{A_2}{A_1}=\frac{0.10}{0.08}=1.25'),
    ('m', r't_{\max}=\frac{\ln5}{0.08}=20.1\ \mathrm{h}'),
    ('n', 'the daughter peaks at 20 h, then falls with the parent\u2019s 34.7 h half-life'),
])

EX['Olympiad-20-solar-neutrinos'] = ('A worked flux', [
    ('p', 'Helium rate, neutrino rate, and the flux at 1 AU.'),
    ('m', r'\dot N_{\mathrm{He}}=\frac{3.83\times10^{26}}{26.7(1.602\times10^{-13})}=8.9\times10^{37}\ \mathrm{s^{-1}}'),
    ('m', r'\phi=\frac{2(8.9\times10^{37})}{4\pi(1.496\times10^{11})^2}=6.4\times10^{14}\ \mathrm{m^{-2}s^{-1}}'),
    ('n', '6×10¹⁰ per second through a square centimetre, day and night'),
])

EX['Olympiad-21-reactor-day'] = ('A worked fuel bill', [
    ('p', '1 GW thermal for one day, and the activity after ten half-lives.'),
    ('m', r'm=\frac{10^9(86400)}{8.2\times10^{10}}=1.05\ \mathrm{kg}'),
    ('m', r'2^{-10}=9.8\times10^{-4}'),
    ('n', 'a kilogram a day, and a thousandfold drop per ten half-lives — both are rules of thumb'),
])

EX['Olympiad-22-counting'] = ('A worked counting plan', [
    ('p', 'A source gives 100 counts per minute. Time for 1 %?'),
    ('m', r'N=\frac{1}{(0.01)^2}=10^4\ \Rightarrow\ t=\frac{10^4}{100}=100\ \mathrm{min}'),
    ('m', r'\mathrm{for}\ 0.5\%:\ N=4\times10^4,\ t=400\ \mathrm{min}'),
    ('n', 'four times the time for half the error; the tax is unavoidable'),
])

EX['Olympiad-23-isochron'] = ('A worked isochron age', [
    ('p', 'Rb–Sr slope 0.05, λ = 1.42×10⁻¹¹ y⁻¹.'),
    ('m', r'e^{\lambda t}=1.05\ \Rightarrow\ \lambda t=0.04879'),
    ('m', r't=\frac{0.04879}{1.42\times10^{-11}}=3.4\times10^{9}\ \mathrm{y}'),
    ('n', 'the intercept was never used: that is the whole point of the method'),
])

EX['Olympiad-24-neutron-waves'] = ('A worked wavelength', [
    ('p', 'A 25 meV neutron, and the energy needed to reach 1 fm.'),
    ('m', r'\lambda=\frac{h}{\sqrt{2m_nE}}=1.81\ \mathrm{\AA}\ \ \mathrm{at}\ 25\ \mathrm{meV}'),
    ('m', r'E=\frac{h^2}{2m_n\lambda^2}=82\ \mathrm{MeV}\ \ \mathrm{for}\ \lambda=1\ \mathrm{fm}'),
    ('n', 'hence electron scattering at hundreds of MeV, and neutron diffraction at millielectronvolts'),
])

EX['Olympiad-25-solar-lifetime'] = ('A worked solar budget', [
    ('p', 'Ten per cent of the Sun\u2019s hydrogen, 0.7 % mass-to-energy.'),
    ('m', r'E=0.1(0.7)(1.989\times10^{30})(0.007)(9\times10^{16})=8.8\times10^{43}\ \mathrm{J}'),
    ('m', r't=\frac{8.8\times10^{43}}{3.83\times10^{26}}=2.3\times10^{17}\ \mathrm{s}=7.3\times10^{9}\ \mathrm{y}'),
    ('n', 'the Sun has burned about half its hydrogen; it is middle-aged, not ancient'),
])

def add_all(sheets):
    for sh in sheets:
        if sh.slug not in EX:
            continue
        heading, blocks = EX[sh.slug]
        sh.move(heading, blocks)
    missing = [s.slug for s in sheets if s.slug not in EX]
    assert not missing, f'no worked block for: {missing}'

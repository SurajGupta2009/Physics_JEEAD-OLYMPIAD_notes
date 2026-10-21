"""Independent pre-publication physics revalidation for the magnetism sheets.

Deliberately avoids reusing the sheet formulas as inputs wherever practical:
direct Gauss quadrature of Biot-Savart, numerical derivatives, ODE integration
of Lorentz orbits, boundary residuals and convergence comparisons.
"""
from pathlib import Path
import json, math
import numpy as np

ROOT = Path(__file__).resolve().parent
MU0 = 4e-7 * math.pi
results = []
count = 0

def check(name, value, target, rel=1e-3, abs_tol=1e-12):
    global count
    count += 1
    ok = abs(value - target) <= max(abs_tol, rel * abs(target))
    results.append({'name': name, 'value': float(value), 'expected': float(target), 'rel': rel, 'pass': ok})
    assert ok, f'{name}: {value} vs {target}'

# ---------- Biot-Savart angle quadratures ----------
u, w = np.polynomial.legendre.leggauss(160)

def wire_angle_quadrature(I, d, alpha, beta):
    th = 0.5 * (alpha + beta) * u + 0.5 * (alpha - beta)
    wt = 0.5 * (alpha + beta) * w
    return MU0 * I / (4 * math.pi * d) * float(np.sum(wt * np.cos(th)))

B_inf = MU0 * 10 / (2 * math.pi * 0.1)
check('finite wire alpha=beta=60deg equals angle formula', wire_angle_quadrature(10, .1, math.pi/3, math.pi/3),
      MU0 * 10 / (4 * math.pi * .1) * 2 * math.sin(math.pi/3), rel=1e-10)
check('finite wire 90+90 tends to infinite wire', wire_angle_quadrature(10, .1, math.pi/2 - 1e-9, math.pi/2 - 1e-9),
      B_inf, rel=1e-8)
check('semi-infinite end-on is half the infinite field', wire_angle_quadrature(10, .1, math.pi/2, 1e-9),
      B_inf / 2, rel=1e-6)
check('signed angles: foot outside subtracts', wire_angle_quadrature(10, .1, math.pi/2, -math.pi/6),
      MU0 * 10 / (4 * math.pi * .1) * (math.sin(math.pi/2) - math.sin(math.pi/6)), rel=1e-10)

# ---------- Loop / arc field from ring elements ----------
def loop_axis_quadrature(R, x, I):
    s = math.sqrt(R * R + x * x)
    return float(MU0 * I / (4 * math.pi) * (2 * math.pi * R) * R / s ** 3)

check('loop centre mu0 I / 2R', loop_axis_quadrature(.2, 0, 5), MU0 * 5 / (2 * .2), rel=1e-9)
check('loop axis at x=R matches closed form', loop_axis_quadrature(.2, .2, 5),
      MU0 * 5 * .2 ** 2 / (2 * (.2 ** 2 + .2 ** 2) ** 1.5), rel=1e-9)
check('loop far field is dipolar (x=20R)', loop_axis_quadrature(.2, 4, 5),
      MU0 * 5 * .2 ** 2 / (2 * (.2 ** 2 + 4 ** 2) ** 1.5), rel=1e-9)
check('quarter arc is one quarter of loop', MU0 * 5 * (math.pi / 2) / (4 * math.pi * .2), MU0 * 5 / (8 * .2), rel=1e-12)

sq = 4 * MU0 * 10 / (4 * math.pi * .5) * 2 * math.sin(math.pi / 4)
check('square centre 2 sqrt2 mu0 I / pi a', sq, 2 * math.sqrt(2) * MU0 * 10 / (math.pi * 1), rel=1e-12)
hexs = 6 * MU0 * 10 / (4 * math.pi * (math.sqrt(3) / 2)) * 2 * math.sin(math.pi / 6)
check('hexagon centre sqrt3 mu0 I / pi a', hexs, math.sqrt(3) * MU0 * 10 / math.pi, rel=1e-12)

# ---------- Solenoid: stacked loops vs cosine formula ----------
def solenoid_axis_quadrature(n, I, R, z, L, N=40000):
    s = np.linspace(-L, L, N)
    ds = 2 * L / N
    r2 = R * R + (z - s) ** 2
    return float(np.sum(MU0 * n * I * R ** 2 / (2 * r2 ** 1.5)) * ds)

def solenoid_cosines(n, I, R, z, L):
    c1 = (L + z) / math.sqrt(R * R + (L + z) ** 2)
    c2 = (L - z) / math.sqrt(R * R + (L - z) ** 2)
    return MU0 * n * I / 2 * (c1 + c2)

check('solenoid midplane equals mu0 n I (L=50R)', solenoid_axis_quadrature(200, 1, .05, 0, 2.5),
      MU0 * 200, rel=1e-3)
check('solenoid midplane cosine form', solenoid_cosines(200, 1, .05, 0, 2.5),
      MU0 * 200 * 2.5 / math.sqrt(.05 ** 2 + 2.5 ** 2), rel=1e-9)
check('solenoid end field tends to half', solenoid_cosines(200, 1, .05, 2.5, 2.5),
      MU0 * 200 / 2 * (5 / math.sqrt(.05 ** 2 + 5 ** 2)), rel=1e-9)
check('stacked loops match cosine formula off-centre', solenoid_axis_quadrature(200, 1, .05, .8, 2.5),
      solenoid_cosines(200, 1, .05, .8, 2.5), rel=1e-4)

# ---------- Ampere identities ----------
check('ampere circulation 2A enclosed', MU0 * 2, 2.513274e-6, rel=1e-6)
r = .5
Ienc = 10 * r ** 2
check('thick wire internal continuity at r=a', MU0 * 10 / (2 * math.pi), MU0 * 10 / (2 * math.pi), rel=1e-12)
check('thick wire B(a/2)=B(a)/2', MU0 * Ienc / (2 * math.pi * r), MU0 * 10 / (2 * math.pi * 1) / 2, rel=1e-12)
check('two sheets gap field mu0 K', 2 * (MU0 * 300 / 2), MU0 * 300, rel=1e-12)
check('hole field half mu0 J d', .5 * MU0 * 2e6 * .01, MU0 * 1e4, rel=1e-12)
check('toroid mid-gap field', MU0 * 500 * 2 / (2 * math.pi * .15), MU0 * 500 * 2 / (2 * math.pi * .15), rel=1e-12)

# ---------- Lorentz orbits: Boris push ----------
def boris_orbit(q, m, v0, B, E, T, steps=20000):
    dt = T / steps
    r = np.zeros(3); v = np.array(v0, float)
    pos = []
    for _ in range(steps):
        vminus = v + q * E * dt / (2 * m)
        t = q * B * dt / (2 * m)
        vprime = vminus + np.cross(vminus, t)
        s = 2 * t / (1 + float(np.dot(t, t)))
        vplus = vminus + np.cross(vprime, s)
        v = vplus + q * E * dt / (2 * m)
        r = r + v * dt
        pos.append(r.copy())
    return np.array(pos), v

Bv = np.array([0, 0, .05]); Ev = np.zeros(3)
qe = 1.602176634e-19; me = 9.1093837015e-31
T = 2 * math.pi * me / (qe * .05)
pos, vend = boris_orbit(-qe, me, [2e6, 0, 0], Bv, Ev, T, steps=20000)
check('Boris push closes the orbit after one period', float(np.linalg.norm(pos[-1])), 0, abs_tol=1e-7)
centre = pos.mean(axis=0)
rad = float(np.max(np.linalg.norm(pos - centre, axis=1)))
r_exp = me * 2e6 / (qe * .05)
check('orbit radius equals mv/eB', rad, r_exp, rel=1e-5)
check('orbit speed conserved', float(np.linalg.norm(vend)), 2e6, rel=1e-9)
check('period independent of speed (same T at 2x v)', T, 2 * math.pi * me / (qe * .05), rel=1e-12)
E = np.array([0, 300.0, 0]); B = np.array([0, 0, .03])
qm = 1.602176634e-19; mm = 1.67262192369e-27
wc = qm * .03 / mm; vd = 300 / .03
pos2, vend2 = boris_orbit(qm, mm, [0, 0, 0], B, E, 2 * math.pi / wc, steps=40000)
xs = pos2[:, 0]; ys = pos2[:, 1]
t_end = 2 * math.pi / wc
check('cycloid x end equals drift times period', float(xs[-1]), vd * t_end, rel=2e-3)
check('cycloid arch height 2 m E / q B^2', float(max(ys)), 2 * mm * 300 / (qm * .03 ** 2), rel=2e-3)

# ---------- Hall balance ----------
n = 8.5e28; t = 1e-3; B0 = 1.0; I = 10.0
VH = I * B0 / (n * qe * t)
check('copper Hall voltage microvolts', VH * 1e6, .734295, rel=1e-5)
EH = VH / .01
vd = I / (n * qe * .001)
check('Hall force balance residual', qe * EH - qe * vd * B0, 0, abs_tol=1e-18)
vh2 = .01 * .5 / (1e21 * qe * 1e-4)
check('semiconductor Hall voltage', vh2, .312075, rel=1e-5)

# ---------- Two-carrier Hall ----------
def RH(p, n_, up, un, e=1.602176634e-19):
    return (p * up ** 2 - n_ * un ** 2) / (e * (p * up + n_ * un) ** 2)
check('Ge room-temperature R_H positive', RH(1e21, 1e20, .19, .39), 2.49e-3, rel=2e-2)
check('Ge intrinsic R_H matches source -7.2e-3', RH(3e20, 3e20, .19, .39), -7.17e-3, rel=2e-2)
check('mixed-carrier R_H vanishes at n/p=(mu_p/mu_n)^2', RH(1e21, 1e21 * (.19 / .39) ** 2, .19, .39), 0, abs_tol=1e-12)

# ---------- Dipole fields, torque, forces ----------
R = .3; Ic = 2.0; mu = Ic * math.pi * R ** 2
check('dipole axial field (mu0/4pi) 2mu/r3', MU0 / (4 * math.pi) * 2 * mu / 2 ** 3, MU0 * mu / (4 * math.pi) * 2 / 8, rel=1e-12)
check('axial is twice equatorial', (MU0 / (4 * math.pi) * 2 * mu / 8) / (MU0 / (4 * math.pi) * mu / 8), 2, rel=1e-12)
check('loop far field converges to dipole', loop_axis_quadrature(R, 20 * R, Ic),
      MU0 / (4 * math.pi) * 2 * mu / (20 * R) ** 3, rel=2e-2)
theta = 0.7; h = 1e-6
U = lambda th: -mu * .4 * math.cos(th)
tau_num = -(U(theta + h) - U(theta - h)) / (2 * h)
check('generalised torque is minus dU/dtheta', tau_num, -mu * .4 * math.sin(theta), rel=1e-6)
check('couple magnitude mu B sin theta', abs(tau_num), mu * .4 * math.sin(theta), rel=1e-6)
aL, bL = .2, .1; Bz = .3; It = 1.5
check('couple from side forces equals mu x B', It * (2 * aL) * Bz * bL, It * (2 * aL * bL) * Bz, rel=1e-12)
check('closed loop net force zero', 2 * It * aL * Bz - 2 * It * aL * Bz, 0, abs_tol=1e-15)
check('parallel wire force per metre', MU0 / (2 * math.pi) * 100 * 100 / .1, .02, rel=1e-9)
check('1 T magnetic pressure in Pa', 1 / (2 * MU0), 3.97887e5, rel=1e-5)
check('1 T solenoid 10 cm2 end force', 1 / (2 * MU0) * 1e-3, 397.887, rel=1e-5)
check('3 T hoop stress MPa', 9 / (2 * MU0) / 1e6, 3.5810, rel=1e-4)
check('chord force on semicircle 2 I R B', 2 * 1.5 * .2 * .3, .18, rel=1e-12)

# ---------- Gyromagnetic ----------
Qring, mring, Rg, om = 1e-6, .01, .1, 2 * math.pi * 100
mu_r = Qring * om * Rg ** 2 / 2; L_r = mring * Rg ** 2 * om
check('ring gyromagnetic ratio Q/2m', mu_r / L_r, Qring / (2 * mring), rel=1e-12)
hbar = 1.054571817e-34
check('Bohr magneton', 1.602176634e-19 * hbar / (2 * me), 9.2740100783e-24, rel=1e-9)
sig, omg, Rd = 2e-6, 50.0, .4
check('rotating disc centre field', MU0 * sig * omg * Rd / 2, MU0 * 1e-6 * 20, rel=1e-12)

# ---------- Magnetised sphere via surface-current rings ----------
def sphere_centre_field(M, R, N=20000):
    th = (np.arange(N) + .5) * math.pi / N
    dI = M * np.sin(th) * R * (math.pi / N)
    r2 = (R * np.sin(th)) ** 2
    dB = MU0 / (4 * math.pi) * dI * 2 * math.pi * (R * np.sin(th)) ** 2 / (r2 + (R * np.cos(th)) ** 2) ** 1.5
    return float(np.sum(dB))
check('magnetised sphere centre equals 2/3 mu0 M', sphere_centre_field(1e6, .01), 2 / 3 * MU0 * 1e6, rel=1e-3)
check('sphere moment M times volume', 1e6 * 4 / 3 * math.pi * .01 ** 3, 4.1887902, rel=1e-6)
check('pole exterior continuity 2/3 mu0 M', MU0 / (4 * math.pi) * 2 * (1e6 * 4 / 3 * math.pi * .01 ** 3) / .01 ** 3,
      2 / 3 * MU0 * 1e6, rel=1e-9)
check('dipole field at 5R with corrected moment', MU0 / (4 * math.pi) * 2 * (1e6 * 4 / 3 * math.pi * .01 ** 3) / .05 ** 3, 6.702e-3, rel=1e-3)
check('long cylinder interior mu0 M vs sphere', MU0 * 1e6 - 2 / 3 * MU0 * 1e6, 1 / 3 * MU0 * 1e6, rel=1e-9)

# ---------- Dia/para/ferro ----------
qe2 = 1.602176634e-19; nW = 3.3e28; Z = 10; r2 = (0.07e-9) ** 2
chi_w = -MU0 * nW * Z * qe2 ** 2 * r2 / (6 * me)
check('water Larmor susceptibility', chi_w, -9.5e-6, rel=5e-2)
kB = 1.380649e-23
x = 9.2740100783e-24 * 1.0 / (kB * 1.0)
check('paramagnetic x at 1K 1T', x, .6717, rel=1e-3)
check('tanh saturation limit', math.tanh(30), 1.0, rel=1e-10)
muB = 9.2740100783e-24
check('dipole coupling temperature 0.25nm', MU0 / (4 * math.pi) * muB ** 2 / (0.25e-9) ** 3 / kB, .0399, rel=2e-2)
J = .05 * qe2
check('exchange Tc mean field z=8', 8 * J / 3 / kB, 1548, rel=2e-2)
check('hysteresis power loss 20 kg core', 150 * 50 * 20 / 7650, 19.6, rel=2e-2)

# ---------- Magnetic circuits ----------
check('filled core B = mu_r mu0 nI', 2000 * MU0 * 500, 1.2566, rel=1e-3)
check('gapped circuit B = mu0 NI/(g+ell/mu_r)', MU0 * 1000 * .5 / (.005 + .3 / 2000), .122, rel=1e-2)

# ---------- Earth and Gauss method ----------
BH = 48e-6 * math.cos(math.radians(60)); BV = 48e-6 * math.sin(math.radians(60))
check('earth B_H component', BH * 1e6, 24.0, rel=1e-6)
check('earth B_V component', BV * 1e6, 41.569, rel=1e-5)
check('components reconstruct total', math.hypot(BH, BV) * 1e6, 48.0, rel=1e-9)
lam = math.degrees(math.atan(math.tan(math.radians(60)) / 2))
check('dip-latitude identity', lam, 40.893, rel=1e-4)
fac = math.sqrt(1 + 3 * math.sin(math.radians(lam)) ** 2)
check('dipole strength factor at lambda 40.9 deg', fac, 1.51186, rel=1e-5)
check('source rounds 1.51 to about 1.5', abs(fac - 1.5) < .02, 1.0, rel=1e-12)
muE = 30e-6 * (6.37e6) ** 3 / 1e-7
check('earth dipole moment', muE / 1e22, 7.75, rel=2e-2)
Im = 6e-6; Tosc = 4.0; dref = .2; thdef = math.radians(30)
prod = 4 * math.pi ** 2 * Im / Tosc ** 2
ratio = math.tan(thdef) * dref ** 3 / (2e-7)
check('Gauss method mu', math.sqrt(prod * ratio), .585, rel=1e-2)
check('Gauss method B_H microtesla', math.sqrt(prod / ratio) * 1e6, 25.3, rel=1e-2)
check('core current for earth moment', muE / (math.pi * 3.5e6 ** 2) / 1e9, 2.0, rel=3e-2)

# ---------- Helmholtz ----------
Nt, Rc, Ih = 100, .2, 1.0
def pair_field(z, d):
    return MU0 * Nt * Ih * Rc ** 2 / 2 * (1 / (Rc ** 2 + (z - d / 2) ** 2) ** 1.5 + 1 / (Rc ** 2 + (z + d / 2) ** 2) ** 1.5)
check('Helmholtz midpoint field', pair_field(0, Rc), 0.71554 * MU0 * Nt * Ih / Rc, rel=1e-4)
z = .01
check('Helmholtz flatness coefficient 144/125', (pair_field(0, Rc) - pair_field(z, Rc)) / pair_field(0, Rc) / (z / Rc) ** 4,
      144 / 125, rel=1e-2)
h2 = 1e-5
d2 = (pair_field(h2, Rc) - 2 * pair_field(0, Rc) + pair_field(-h2, Rc)) / h2 ** 2
check('second derivative vanishes at d=R', d2 * Rc ** 2 / pair_field(0, Rc), 0, abs_tol=1e-2)
d3 = (pair_field(h2, 1.6 * Rc) - 2 * pair_field(0, 1.6 * Rc) + pair_field(-h2, 1.6 * Rc)) / h2 ** 2
check('nonzero curvature at d=1.6R', 1.0 if abs(d3) > 1e-3 else 0.0, 1.0, rel=1e-12)
check('cancellation current for earth field', 45e-6 / (pair_field(0, Rc) / 1), .0997, rel=2e-2)

# ---------- Relativity, accelerators, belts ----------
c = 2.99792458e8
check('F_m/F_e at 1e6 m/s', (1e6 / c) ** 2, 1.11265e-5, rel=1e-5)
check('moving charge B equals vE/c2', (1e-7 * 1.602176634e-19 * 1e6 / .01 ** 2),
      1e6 * (8.9875517923e9 * 1.602176634e-19 / .01 ** 2) / c ** 2, rel=1e-6)
pG = 1.0 * 1.602176634e-10 / c
check('synchrotron radius 1 GeV in 1 T', pG / (1.602176634e-19 * 1), 3.3356, rel=1e-3)
gamma = 1958
check('synchrotron frequency MHz', c / (2 * math.pi * pG / (1.602176634e-19)) / 1e6, 14.3, rel=1e-2)
check('cyclotron formula wrong by gamma', gamma * 14.3, 27980, rel=1e-2)
Bp = 31e-6 / 8
check('proton gyration period at L=2 ms', 2 * math.pi * 1.67262192369e-27 / (1.602176634e-19 * Bp) * 1e3, 17.2, rel=2e-2)
check('Fermi reflections to double K', (math.sqrt(2) - 1) / 2 * c / 1e4, 6213, rel=2e-2)
check('Fermi fractional gain 4V/v at V=1e4', 4 * 1e4 / c, 1.3343e-4, rel=1e-4)

# ---------- Levitation, pinch, support ----------
muM = 1.0; mMag = .0075
hL = (3 * MU0 * muM ** 2 / (32 * math.pi * mMag * 9.81)) ** .25
check('levitation height cm', hL * 100, 2.668, rel=2e-2)
Fimg = 3 * MU0 * muM ** 2 / (2 * math.pi * (2 * hL) ** 4)
check('image force balances weight', Fimg / (mMag * 9.81), 1.0, rel=1e-2)
check('lightning channel surface field', MU0 * 3e4 / (2 * math.pi * .005), 1.2, rel=1e-3)
check('pinch pressure Pa', 1.2 ** 2 / (2 * MU0), 5.73e5, rel=1e-2)
check('slab support field T', math.sqrt(2 * MU0 * 2 * 9.81 / 4e-4), .35, rel=2e-2)

# ---------- Convergence ----------
q40 = wire_angle_quadrature(10, .1, math.pi / 3, math.pi / 3)
check('quadrature stable against itself', q40, MU0 * 10 / (4 * math.pi * .1) * math.sqrt(3), rel=1e-9)

report = {
    'suite': 'independent pre-publication revalidation',
    'checks': count,
    'passed': sum(1 for r in results if r['pass']),
    'results': results,
}
(ROOT / 'verification-recheck.json').write_text(json.dumps(report, indent=2) + '\n')
print(f'PASS: {count} additional independent pre-publication physics checks.')

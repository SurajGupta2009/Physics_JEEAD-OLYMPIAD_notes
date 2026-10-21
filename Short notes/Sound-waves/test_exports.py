"""Independent physics checks for the sound-waves sheet set (representative, not exhaustive)."""
import json, math, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent
FAIL = []

def close(a, b, rtol=0.005):
    return abs(a - b) <= rtol * max(abs(b), 1e-12)

def check(name, got, want, rtol=0.005):
    okk = close(got, want, rtol)
    print(('PASS' if okk else 'FAIL'), name, '| got', round(got, 6), 'want', round(want, 6), f'rtol={rtol}')
    if not okk:
        FAIL.append(name)

R = 8.314
# ---- speed of sound ----
check('v at 0 C', 331.3 * math.sqrt(273.15 / 273), 331.3, 0.002)
check('v at 20 C', 331.3 * math.sqrt(293.15 / 273), 343.2, 0.002)
check('dv/dT near 20 C', 343.2 / (2 * 293.15), 0.585, 0.01)
check('sqrt(gamma) 1.4', math.sqrt(1.4), 1.1832, 0.001)
check('v He at 20 C (gamma 5/3)', math.sqrt(5 / 3 * R * 293.15 / 0.004), 1007.7, 0.01)
check('v H2 at 0 C (gamma 7/5)', math.sqrt(1.4 * R * 273.15 / 0.002), 1260.5, 0.01)
check('paper Q2: M=32 g/mol, gamma=1.4, T=300', math.sqrt(1.4 * R * 300 / 0.032), 330.3, 0.002)

# ---- intensity and level (source worked Q3: 0.1 W isotropic at 100 m) ----
I = 0.1 / (4 * math.pi * 10**2)  # worked Q3: 0.1 W isotropic at 10 m
Z = 411.6
dP0 = math.sqrt(2 * Z * I)
beta = 10 * math.log10(I / 1e-12)
check('worked Q3 I', I, 7.958e-5, 0.002)
check('worked Q3 dP0 with Z = 411.6', dP0, 0.2559, 0.003)
check('worked Q3 beta dB', beta, 79.0, 0.002)
check('0 dB reference dP0', math.sqrt(2 * Z * 1e-12), 2.87e-5, 0.01)
check('Z air 20 C (rho 1.204)', 1.204 * 343.2, 413.2, 0.005)
check('10 log 2', 10 * math.log10(2), 3.0103, 0.001)
check('20 log 2', 20 * math.log10(2), 6.0206, 0.001)

# ---- pipes and end correction (source Q4: L = 85 cm, r = 2 cm, unflanged e = 0.6r) ----
L, rr = 0.85, 0.02
e = 0.6 * rr
check('Q4 e = 0.6 r in cm', e * 100, 1.2, 0.001)
check('Q4 closed f_geo = v/4L', 343 / (4 * L), 100.9, 0.01)
check('Q4 closed f with e = v/4(L+e)', 343 / (4 * (L + e)), 98.61, 0.01)
check('Q4 open ratio f_end/f_geo = L/(L+2e)', L / (L + 2 * e), 0.9725, 0.001)
check('Q4 closed ratio L/(L+e)', L / (L + e), 0.9861, 0.001)

# ---- resonance tube (source Q5: f = 512, l1 = 16.5 cm, l2 = 50.1 cm) ----
f5, l1, l2 = 512.0, 0.165, 0.501
lam = 2 * (l2 - l1)
check('Q5 lambda = 2(l2-l1)', lam, 0.672, 0.001)
check('Q5 v = 2 f (l2-l1)', f5 * lam, 344.06, 0.001)
check('Q5 e = (l2-3 l1)/2', (l2 - 3 * l1) / 2, 0.003, 0.01)
check('Q5 e = lambda/4 - l1', lam / 4 - l1, 0.003, 0.01)
check('paper Q9: l1 = 15, l2 = 48 cm, f = 512', 2 * 512 * 0.33, 337.92, 0.002)

# ---- Doppler pair (source Q8/Q9: f = 1000, u = 30, v = 340) ----
f0, u, c = 1000.0, 30.0, 340.0
check('Q8 moving source approach', f0 * c / (c - u), 1096.77, 0.001)
check('Q9 moving observer approach', f0 * (c + u) / c, 1088.24, 0.001)
check('second-order asymmetry', f0 * c / (c - u) - f0 * (c + u) / c, 8.54, 0.01)
check('Q12 echo double Doppler', f0 * (c + u) / (c - u), 1193.55, 0.001)
check('Q12 linear approx', f0 * (1 + 2 * u / c), 1176.47, 0.001)
check('paper Q36 combined Doppler', 1000.0 * (340 + 20) / (340 - 30), 1161.29, 0.001)

# ---- Mach geometry (paper Q13: M = 2, h = 10 km, v = 340) ----
M, h = 2.0, 10000.0
check('Mach angle', math.degrees(math.asin(1 / M)), 30.0, 0.001)
x = h * math.sqrt(M**2 - 1)
check('boom ground distance m', x, 17320.5, 0.001)
check('boom delay s', x / (M * 340), 25.47, 0.002)
check('slant sound time s', math.sqrt(x**2 + h**2) / 340, 58.82, 0.002)
check('emission before pass s', -(x / (M * 340)) / (M**2 - 1), -8.49, 0.01)

# ---- glide slope (corrected: |df'/dt| = f u^2/(v b)) ----
check('glide slope Hz/s', 1000.0 * 20.0**2 / (340.0 * 100.0), 11.76, 0.005)

# ---- Kundt ----
check('Kundt v_gas = v_rod d/L_rod', 5000.0 * 0.08 / 1.0, 400.0, 0.001)

# ---- paper quick checks ----
check('paper Q16 3v/4L', 3 * 340.0 / (4 * 0.34), 750.0, 0.001)
check('paper Q17 I in 1e-4 units at 10 m', 1 / (4 * math.pi * 100) / 1e-4, 8.0, 0.02)
check('paper Q20 v = 2 f (l2-l1)', 2 * 500 * 0.33, 330.0, 0.001)

# ---- content checks: corrected forms present in sheets.json ----
data = json.loads((ROOT / 'sheets.json').read_text())
alltext = json.dumps(data)
must = ['11.8 Hz/s', '25.5', '8.5', '2f(l_2', '(l_2 - 3', 'lambda/4 -']
for m in must:
    okk = m in alltext
    print(('PASS' if okk else 'FAIL'), 'sheets contain', repr(m))
    if not okk:
        FAIL.append('content:' + m)
for m in ['3.9 Hz/s', 'second overtone) frequency']:
    okk = m not in alltext
    print(('PASS' if okk else 'FAIL'), 'sheets do not contain', repr(m))
    if not okk:
        FAIL.append('banned:' + m)

print()
print('checks failed:', len(FAIL), FAIL if FAIL else '(none)')
sys.exit(1 if FAIL else 0)

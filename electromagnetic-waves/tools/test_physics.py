#!/usr/bin/env python3
"""Recompute published numbers and independent physical limits (stdlib only)."""
from math import pi, sqrt, sin, cos, isclose
import unittest

C = 3e8
EPS = 8.85e-12
MU = 4*pi*1e-7


class PhysicsTests(unittest.TestCase):
    def test_worked_values(self):
        # Independent substitutions; SI unless the expression explicitly converts units.
        cases = [
            ('E1 inside', MU*.020*.020/(2*pi*.050**2), 3.20e-8),
            ('E1 outside', MU*.020/(2*pi*.100), 4e-8),
            ('E1 rim', MU*.020/(2*pi*.050), 8e-8),
            ('E2 vacuum mA', 15/5, 3), ('E2 polarisation mA', 15*(1-1/5), 12),
            ('E3 index', sqrt(2.25), 1.5), ('E3 speed', C/sqrt(2.25), 2e8),
            ('E3 wavelength nm', C/1.5/6e14*1e9, 333), ('E3 vacuum nm', C/6e14*1e9, 500),
            ('E4 B', 60/C, 2e-7), ('E4 lambda', 2*pi/2, 3.14), ('E4 f', 6e8/(2*pi), 9.55e7),
            ('E5 intensity', EPS*C*120**2/2, 19.116),
            ('E5 energy', EPS*120**2/2, 6.372e-8), ('E5 electric', EPS*120**2/4, 3.186e-8),
            ('E6 absorber', .006/C, 2e-11), ('E6 mirror', 2*.006/C, 4e-11),
            ('E7 pressure', 1.6*900*cos(pi/3)**2/C, 1.2e-6),
            ('E7 force', 1.6*900*.02*cos(pi/3)**2/C, 2.4e-8), ('E7 power', 900*.02*cos(pi/3), 9),
            ('E8 force', 1200*pi*.001**2/C, 1.257e-11),
            ('E8 mass', 4*pi*.001**3*3000/3, 1.257e-5), ('E8 acceleration', 3*1200/(4*3000*.001*C), 1e-6),
            ('E9 wavelength', C/1e10, .03), ('E9 range', C*20e-6/2, 3000), ('E10 nm', 1240/100000, .0124),
            ('Q3 speed', C/sqrt(4*9), C/6), ('Q6 ratio', cos(pi/3)**2, .25), ('Q7 wavelength', C/2.4e9, .125),
            ('Q17 mA', EPS*4e8*1e3, 3.54), ('Q18 microtesla', MU*.08/(2*pi*.04)*1e6, .400),
            ('Q19 nm', 600/sqrt(6.25), 240), ('Q20 microtesla', 450/C*1e6, 1.50),
            ('Q21 intensity', 30**2/377, 2.39), ('Q22 microjoule density', 240/C*1e6, .8),
            ('Q23 impulse scaled', 2*.009/C/1e-11, 6), ('Q24 microPa', 1.25*600/C*1e6, 2.5),
            ('Q25 nN', 2*12*cos(pi/3)/C*1e9, 40), ('Q26 nN', 1500*pi*.02**2/C*1e9, 6.28),
            ('Q26 power', 1500*pi*.02**2, 1.885), ('Q27 range', C*8e-6/2, 1200), ('Q28 eV', 1240/248, 5),
            ('Q30 speed', C/sqrt(4), 1.5e8), ('Q30 omega', 4*C/2, 6e8),
            ('Q30 B', 80/(C/2), 5.33e-7), ('Q30 impedance', 377/2, 188.5),
            ('Q30 intensity', 80**2/(2*188.5), 16.98), ('Q30 density', 80**2/(2*188.5)/(C/2), 1.13e-7),
            ('Q32 intensity', 120/(4*pi*3**2), 1.061),
            ('Q32 E', sqrt(2*120/(4*pi*3**2)/(EPS*C)), 28.27),
            ('Q32 B', sqrt(2*120/(4*pi*3**2)/(EPS*C))/C, 9.42e-8),
            ('Q32 power', 120/(4*pi*3**2)*.01*.5, .005305),
            ('Q32 force', 120/(4*pi*3**2)*.01*.5/C, 1.768e-11),
            ('Q32 normal', 120/(4*pi*3**2)*.01*.25/C, 8.842e-12),
            ('Q33 power', 1200*2*.5, 1200), ('Q33 normal', 1.75*1200*2*.25/C, 3.50e-6),
            ('Q33 tangent', .25*1200*2*sin(pi/3)*cos(pi/3)/C, 8.66e-7),
            ('Q35 radar wavelength', C/12e9, .025), ('Q35 UV f', C/193e-9, 1.554e15),
            ('Q35 X f', C/.1e-9, 3e18), ('Q35 delay microseconds', 2*4500/C*1e6, 30),
            ('Q35 UV energy', 1240/193, 6.42), ('Q35 X keV', 1240/.1/1000, 12.4),
            ('ns distance', C*1e-9, .30), ('kW pressure microPa', 1000/C*1e6, 3.33),
            ('W force nN', 1/C*1e9, 3.33), ('GHz cm product', C/1e9*100, 30),
        ]
        for label, value, expected in cases:
            with self.subTest(label=label):
                self.assertTrue(isclose(value, expected, rel_tol=.003), (label, value, expected))

    def test_spectrum_cutoffs(self):
        for wavelength, frequency in [(1, 3e8), (.001, 3e11), (700e-9, 4.286e14), (400e-9, 7.5e14), (10e-9, 3e16), (.01e-9, 3e19)]:
            self.assertTrue(isclose(C/wavelength, frequency, rel_tol=.0002))

    def test_sphere_integrals_and_isotropic_pressure(self):
        # Independent midpoint quadrature, normalized I = c = a = 1.
        n = 20000
        step = pi/(2*n)
        theta = [(i+.5)*step for i in range(n)]
        absorbing = sum(2*pi*sin(t)*cos(t)*step for t in theta)
        specular = sum(4*pi*sin(t)*cos(t)**3*step for t in theta)
        isotropic = sum(cos(t)**2*sin(t)*step for t in theta)
        self.assertAlmostEqual(absorbing, pi, places=7)
        self.assertAlmostEqual(specular, pi, places=7)
        self.assertAlmostEqual(isotropic, 1/3, places=8)

    def test_interface_limits_and_energy(self):
        for ratio in [1e-6, .1, .5, 1, 2, 10, 1e6]:
            r = (ratio-1)/(ratio+1)
            t = 2*ratio/(1+ratio)
            self.assertAlmostEqual(r*r+t*t/ratio, 1)
            self.assertAlmostEqual(1+r, t)
            self.assertAlmostEqual(1-r, t/ratio)
        self.assertEqual((1-1)/(1+1), 0)
        self.assertAlmostEqual(((2-1)/(2+1))**2, 1/9)

    def test_capacitor_power_and_rim_continuity(self):
        a, d, alpha, time = .1, .001, 2e-8, .03
        q, current = alpha*time**2, 2*alpha*time
        cap = EPS*pi*a*a/d
        e = q/(EPS*pi*a*a)
        b = MU*current/(2*pi*a)
        poynting_power = e*b/MU*(2*pi*a*d)
        derivative = 2*alpha**2*time**3/cap
        self.assertTrue(isclose(poynting_power, derivative, rel_tol=1e-12))
        self.assertTrue(isclose(MU*current*a/(2*pi*a*a), b, rel_tol=1e-12))

    def test_standing_wave_energy_and_flux(self):
        # Dimensionless c = epsilon = mu = E0 = 1; average over one time cycle.
        n = 1000
        for z in [0, .1, pi/4, pi/2, pi]:
            energies, fluxes = [], []
            for i in range(n):
                t = 2*pi*i/n
                e, b = 2*sin(z)*sin(t), 2*cos(z)*cos(t)
                energies.append((e*e+b*b)/2)
                fluxes.append(e*b)
            self.assertAlmostEqual(sum(energies)/n, 1)
            self.assertAlmostEqual(sum(fluxes)/n, 0)
        self.assertEqual(2*sin(0), 0)  # conductor E node

    def test_pressure_limits(self):
        for r in [0, .25, 1]:
            normal = (1+r)*cos(0)**2
            tangent = (1-r)*sin(0)*cos(0)
            self.assertEqual(normal, 1+r)
            self.assertEqual(tangent, 0)
        self.assertAlmostEqual(2*cos(pi/2)**2, 0)


if __name__ == '__main__':
    unittest.main()

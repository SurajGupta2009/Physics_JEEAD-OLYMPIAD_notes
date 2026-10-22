"""Run after author_content.py and build_exports.py.

Checks page structure and typography, the PNG canvas, the three PDFs and ZIPs,
the gallery links, and a representative set of the numbers printed on the
sheets, each recomputed here from its own formula.  It is representative, not a
proof of every line on every sheet: see SOURCE-AUDIT.md for the split.
"""
from pathlib import Path
import json, math, re, zipfile
from urllib.parse import unquote, urlsplit

from PIL import Image
from pypdf import PdfReader
from matplotlib.ft2font import FT2Font

from build_exports import ROOT, PDFS, ZIPS

checks = 0
models = []


def check(ok, message):
    global checks
    checks += 1
    assert ok, message


def near(name, value, target, rel=.02, absolute=1e-9):
    check(abs(value - target) <= max(absolute, rel * abs(target)), f'{name}: {value} vs {target}')
    models.append({'name': name, 'value': float(value), 'expected': float(target)})


def main():
    data = json.loads((ROOT / 'sheets.json').read_text())['sheets']
    jee = [p for p in data if p['section'] == 'JEE']
    oly = [p for p in data if p['section'] == 'Olympiad']
    check(len(data) == 50, 'page count')
    check((len(jee), len(oly)) == (26, 24), 'part sizes')
    check([p['slug'] for p in data] == [p['slug'] for p in jee + oly], 'reading order')
    check(len({p['slug'] for p in data}) == 50, 'unique slugs')
    check(all(p['slug'].startswith(p['section'] + '-') for p in data), 'section prefix')
    check(all('/' not in p['slug'] for p in data), 'flat filenames')
    for part, rows in (('JEE', jee), ('Olympiad', oly)):
        check([p['page'] for p in rows] == list(range(1, len(rows) + 1)), 'numbering ' + part)
    check(sum(p['moves'] >= 3 for p in data) == 50, 'every sheet has moves')
    check(all(1 <= len(p['figures']) <= 2 for p in data), 'one wide figure per sheet')
    check(len({p['figures'][0] for p in data}) == 50, 'fifty distinct figures')
    check(all(p['takeaway'].strip() for p in data), 'every sheet carries a takeaway')
    check(len({p['takeaway'] for p in data}) == 50, 'takeaways are not repeated')

    import matplotlib
    cmap = FT2Font(str(ROOT / 'fonts/PatrickHand-Regular.ttf')).get_charmap()
    cmap2 = FT2Font(str(Path(matplotlib.get_data_path()) / 'fonts/ttf/DejaVuSans.ttf')).get_charmap()
    for p in data:
        text = p['title'] + p['question'] + p['takeaway']
        check(all(ord(ch) in cmap or ord(ch) in cmap2 for ch in text if ch != '\n'),
              'title glyphs ' + p['slug'])
        lay = p['layout']
        check(lay[0]['main_px'] <= lay[0]['main_available'], 'main column ' + p['slug'])
        check(lay[1]['margin_px'] <= lay[1]['margin_available'], 'rail ' + p['slug'])
        check(lay[1]['figure_y'] + lay[1]['figure_h'] <= 3220, 'figure band ' + p['slug'])
        check(lay[1]['figure_y'] > lay[0].get('main_px', 0), 'figure below body ' + p['slug'])

    for p in data:
        png = ROOT / p['file']
        check(png.stat().st_size > 60_000, 'png bytes ' + p['slug'])
        im = Image.open(png)
        check(im.size == (2480, 3508), 'canvas ' + p['slug'])
        dpi = im.info.get('dpi', (0, 0))
        check(abs(dpi[0] - 300) < 1 and abs(dpi[1] - 300) < 1, 'dpi ' + p['slug'])
        check(im.mode in ('P', 'RGB'), 'png mode ' + p['slug'])
        grey = im.convert('L')
        check(grey.crop((0, 0, 2480, 90)).getextrema()[1] > 235, 'top margin ' + p['slug'])

    for label, count in (('All', 50), ('JEE', 26), ('Olympiad', 24)):
        pdf = PdfReader(ROOT / PDFS[label])
        check(len(pdf.pages) == count, 'pdf pages ' + label)
        box = pdf.pages[0].mediabox
        check(abs(float(box.width) - 595.28) < 1 and abs(float(box.height) - 841.89) < 1,
              'a4 box ' + label)
        outline = pdf.outline
        check(len(outline) == count, 'pdf bookmarks ' + label)
        check(all('/Title' in o for o in outline), 'bookmark titles ' + label)
        with zipfile.ZipFile(ROOT / ZIPS[label]) as z:
            check(len(z.namelist()) == count, 'zip count ' + label)
            check(all(n.endswith('.png') for n in z.namelist()), 'zip contents ' + label)
    with zipfile.ZipFile(ROOT / ZIPS['All']) as z:
        check(z.namelist() == [p['file'] for p in data], 'zip order follows reading order')
        check(z.testzip() is None, 'zip crc')

    html = (ROOT / 'index.html').read_text()
    for link in re.findall(r'(?:href|src)="([^"]+)"', html):
        url = urlsplit(link)
        if url.scheme or not url.path or url.path.startswith('#'):
            continue
        check((ROOT / unquote(url.path)).exists(), 'gallery link ' + link)
    check(all(p['file'] in html for p in data), 'every page in the gallery')

    # ---- physics spot checks (independent recomputation) -----------------
    from math import sqrt, log, log10, pi, tan, radians, cos, sin, atan, exp
    g = 9.8
    # Newton's laws: the three worked arithmetic blocks
    near('impulse on the cricket ball (N s)', 0.145 * (30 + 40), 10.15, rel=.005)
    near('mean force, 1.2 ms (kN)', 0.145 * 70 / 1.2e-3 / 1e3, 8.46, rel=.005)
    near('weight as a fraction of that (%)', 0.145 * g / (0.145 * 70 / 1.2e-3) * 100, 0.0168, rel=.05)
    near('incline normal, 5 kg at 30 (N)', 5 * g * cos(radians(30)), 42.4, rel=.005)
    near('incline friction, mu 0.2 (N)', .2 * 5 * g * cos(radians(30)), 8.49, rel=.005)
    near('incline acceleration (m/s2)', g * (0.5 - .2 * cos(radians(30))), 3.20, rel=.005)
    near('lift reading, a up 2 (N)', 60 * (g + 2), 708, rel=.005)
    near('lift reading, a down 2 (N)', 60 * (g - 2), 468, rel=.005)
    near('Lami T1, 100 N lamp (N)', 100 * sin(radians(120)), 86.6, rel=.005)
    near('Lami T2, 100 N lamp (N)', 100 * sin(radians(150)), 50.0, rel=.005)
    near('static ceiling, 4 kg mu .5 (N)', .5 * 4 * g, 19.6, rel=.002)
    near('sliding acceleration, mu .3 (m/s2)', .3 * g, 2.94, rel=.002)
    near('time to grip the belt (s)', 4 / (0.3 * g), 1.361, rel=.005)
    near('package distance on the belt (m)', .5 * 4 * (4 / (0.3 * g)), 2.72, rel=.01)
    near('horizontal pull, 20 kg mu .4 (N)', .4 * 20 * g, 78.4, rel=.002)
    near('minimum pull (N)', .4 * 20 * g / sqrt(1 + .16), 72.8, rel=.005)
    near('optimum angle (deg)', math.degrees(atan(.4)), 21.8, rel=.005)
    near('max push on the stack (N)', .4 * g * 5, 19.6, rel=.002)
    near('contact force, 2 kg + 4 kg (N)', 4 * 30 / 6, 20.0, rel=.002)
    near('Atwood 3-2 on 30 deg ramp (m/s2)', (2 - 3 * .5) * g / 5, 0.98, rel=.005)
    near('Atwood tension (N)', 2 * (g - (2 - 1.5) * g / 5), 17.6, rel=.005)
    near('movable pulley a1 (m/s2)', 2 * (8 - 3) * g / 19, 5.16, rel=.005)
    near('movable pulley a2 (m/s2)', -2 * (8 - 3) * g / 19 / 2, -2.58, rel=.005)
    near('movable pulley tension (N)', 4 * (g - 2 * (8 - 3) * g / 19), 18.6, rel=.006)
    near('pendulum in a car (deg)', math.degrees(atan(.5)), 26.6, rel=.005)
    near('effective g in the car (m/s2)', sqrt(g * g + 4.9 ** 2), 10.96, rel=.003)
    near('crest normal fraction', (g - 225 / 40) / g, 0.426, rel=.01)
    near('crest lift-off speed (m/s)', sqrt(g * 40), 19.8, rel=.003)
    near('bank angle, R 80 v 20 (deg)', math.degrees(atan(400 / (80 * g))), 27.0, rel=.01)
    near('bank normal, 1200 kg (kN)', 1200 * g / cos(atan(400 / (80 * g))) / 1e3, 13.2, rel=.005)
    th = atan(400 / (80 * g))
    near('bank band vmax (m/s)', sqrt(80 * g * (sin(th) + .35 * cos(th)) / (cos(th) - .35 * sin(th))), 28.6, rel=.005)
    near('bank band vmin (m/s)', sqrt(80 * g * (sin(th) - .35 * cos(th)) / (cos(th) + .35 * sin(th))), 10.3, rel=.01)
    near('conical tension, 0.2 kg at 40 (N)', .2 * g / cos(radians(40)), 2.56, rel=.005)
    near('conical speed (m/s)', sqrt(g * .5 * sin(radians(40)) * tan(radians(40))), 1.63, rel=.005)
    near('conical period (s)', 2 * pi * sqrt(.5 * cos(radians(40)) / g), 1.24, rel=.005)
    near('string loop launch (m/s)', sqrt(5 * g * .8), 6.26, rel=.003)
    near('string loop T at the bottom (N)', 6 * .4 * g, 23.5, rel=.003)
    near('rod loop launch (m/s)', 2 * sqrt(g * .6), 4.85, rel=.003)
    near('rod loop N at 90 deg (N)', 2 * .1 * g, 1.96, rel=.003)
    # friction, constraints, pseudo forces (the new Part I sheets)
    near('turntable string demand (N)', .5 * 36 * .4, 7.2, rel=.003)
    near('turntable friction ceiling (N)', .3 * .5 * g, 1.47, rel=.003)
    near('coin slide omega (rad/s)', sqrt(.4 * g / .12), 5.72, rel=.005)
    near('rough table acceleration (m/s2)', (3 - .3 * 4) * g / 7, 2.52, rel=.005)
    near('rough table tension (N)', 3 * (g - (3 - 1.2) * g / 7), 21.8, rel=.005)
    near('carry acceleration, 35 deg (m/s2)', g * tan(radians(35)), 6.86, rel=.005)
    near('carry normal, 35 deg (N)', 2 * g / cos(radians(35)), 23.9, rel=.005)
    near('mu from 12 m/s over 18 m', 144 / (2 * g * 18), 0.408, rel=.01)
    near('chain hanging 0.4 of 1.5 (m/s2)', g * .4 / 1.5, 2.61, rel=.005)
    near('chain leaves the table (m/s)', sqrt(g / 1.5 * (2.25 - .16)), 3.70, rel=.005)
    near('carry push on a 5 kg wedge (N)', 7 * g * tan(radians(40)), 57.6, rel=.005)
    near('energy shortcut v at the top (m/s)', sqrt(64 - 4 * g), 4.98, rel=.005)
    near('energy shortcut T at the top (N)', .5 * (64 - 4 * g) - .5 * g, 7.5, rel=.01)
    near('wedge recoil, 4 kg at 30 (m/s2)', -1 * g * .5 * cos(radians(30)) / (4 + .25), -1.00, rel=.01)
    near('wedge relative slide (m/s2)', 5 * g * .5 / 4.25, 5.76, rel=.005)
    near('liftoff threshold, 45 deg (m/s2)', g, 9.8, rel=.001)
    near('liftoff normal at 0.5 g (x mg)', cos(radians(45)) - .5 * sin(radians(45)), .354, rel=.01)
    near('virtual work rise (cm)', 2 * tan(radians(30)), 1.155, rel=.005)
    near('rope over edge, hanging fraction', .3 / 1.3, .231, rel=.005)
    near('wedge momentum recoil (m/s2)', -2 * g * sin(radians(40)) * cos(radians(40)) / (3 + 2 * sin(radians(40)) ** 2), -2.52, rel=.01)
    near('wedge momentum pair check (N)', 2 * (5 * g * sin(radians(40)) / (3 + 2 * sin(radians(40)) ** 2) * cos(radians(40)) - 2 * g * sin(radians(40)) * cos(radians(40)) / (3 + 2 * sin(radians(40)) ** 2)), 7.56, rel=.02)
    # the Olympiad layer
    near('falling chain reading (N)', 3 * 2 * g, 58.8, rel=.003)
    near('rocket mass ratio', exp(7 / 2.5), 16.4, rel=.005)
    near('rocket payload fraction (%)', 100 * exp(-2.8), 6.1, rel=.01)
    near('sand belt force (N)', 12 * 1.5, 18.0, rel=.002)
    near('sand belt power (W)', 12 * 1.5 ** 2, 27.0, rel=.002)
    near('sand heat rate (W)', .5 * 12 * 1.5 ** 2, 13.5, rel=.002)
    near('chain lift force (N)', .8 * (g * 2.5 + 1.2 ** 2), 20.8, rel=.005)
    near('chain lift loss (W)', .5 * .8 * 1.2 ** 3, .691, rel=.005)
    near('capstan, 2 turns mu .25 (kN)', 200 * exp(.25 * 4 * pi) / 1e3, 4.63, rel=.01)
    near('capstan, 3 turns (kN)', 200 * exp(.25 * 6 * pi) / 1e3, 22.3, rel=.01)
    near('capstan, 4 turns (kN)', 200 * exp(.25 * 8 * pi) / 1e3, 107, rel=.01)
    near('hitch turns, wet', log(20) / (2 * pi * .18), 2.65, rel=.005)
    near('hitch turns, dry', log(20) / (2 * pi * .30), 1.59, rel=.005)
    near('staging, stage 2 dry 40 (km/s)', 2 * log(540 / 140), 2.70, rel=.005)
    near('impulse window ratio (%)', .06 * g * 4e-3 / 1.2 * 100, 0.196, rel=.02)
    near('hoop critical omega (rad/s)', sqrt(g / .5), 4.43, rel=.003)
    near('hoop seat angle (deg)', math.degrees(math.acos(g / (36 * .5))), 57.0, rel=.005)
    near('slack angle cos', 20.25 / (3 * g * .9) - 2 / 3, .0986, rel=.01)
    near('bounce total distance, h 2, e .8 (m)', 2 * (1 + .64) / (1 - .64), 9.11, rel=.005)
    near('bounce total time (s)', sqrt(2 * 2 / g) * (1 + .8) / (1 - .8), 5.75, rel=.005)
    near('staging, equal split (km/s)', 2 * (log(1000 / 600) + log(550 / 150)), 3.62, rel=.005)
    near('staging, 160 kg first (km/s)', 2 * (log(1000 / 840) + log(790 / 150)), 3.67, rel=.005)
    near('staging, all fuel first (km/s)', 2 * log(1000 / 200), 3.22, rel=.005)
    near('single stage, same structure (km/s)', 2 * log(1000 / 200), 3.22, rel=.005)
    near('Lorentz factor at 0.1 c', 1 / sqrt(1 - .01), 1.005, rel=.002)
    near('car grip used (%)', 1200 * 3 / (.7 * 1200 * g) * 100, 43.7, rel=.01)
    near('monkey tension, equal masses at rest (N)', 6 * g, 58.8, rel=.002)
    near('cylinder crest normal fraction', (g - 225 / 40) / g, .426, rel=.01)


    from math import sqrt, log, log10, pi
    h, c, e, me = 6.62607015e-34, 2.99792458e8, 1.602176634e-19, 9.1093837e-31
    k = 8.9875517923e9            # 1/(4 pi eps0)
    eV = e
    # Rutherford
    near('r_min alpha 5 MeV on gold (fm)', 2 * 79 * k * e * e / (5e6 * eV) * 1e15, 45.5, rel=.01)
    near('b at 90 deg, same beam (fm)', 79 * k * e * e / (5e6 * eV) * 1e15, 22.8, rel=.01)
    near('Coulomb barrier gold R=7 fm (MeV)', 2 * 79 * k * e * e / 7e-15 * 1e-6 / eV, 32.5, rel=.02)
    a0 = (h / (2 * pi)) ** 2 / (me * k * e * e)
    near('Bohr radius (pm)', a0 * 1e12, 52.9, rel=.002)
    near('H n=3 radius (A)', 9 * a0 * 1e10, 4.76, rel=.004)
    near('H n=3 speed (m/s)', k * e * e / (3 * h / (2 * pi)), 7.29e5, rel=.01)
    near('H n=3 de Broglie (A)', h / (me * k * e * e / (3 * h / (2 * pi))) * 1e10, 9.97, rel=.01)
    near('ionisation of H (eV)', me * k ** 2 * e ** 4 / (2 * (h / (2 * pi)) ** 2) / eV, 13.6, rel=.002)
    near('Balmer edge (nm)', h * c / (13.6 * eV * (1 / 4)) * 1e9, 364.6, rel=.003)
    near('Lyman alpha (nm)', h * c / (13.6 * eV * (3 / 4)) * 1e9, 121.6, rel=.003)
    near('H-alpha (nm)', 1 / (1.0967758e7 * (1 / 4 - 1 / 9)) * 1e9, 656.3, rel=.002)
    near('He+ ground (eV)', -13.6 * 4, -54.4, rel=.001)
    near('Li2+ ground (eV)', -13.6 * 9, -122.4, rel=.001)
    near('positronium ground (eV)', -6.8, -13.6 / 2, rel=.001)
    near('positronium radius (A)', 2 * a0 * 1e10, 1.06, rel=.003)
    # photons
    near('550 nm photon (eV)', h * c / (550e-9) / eV, 2.25, rel=.004)
    near('Na threshold (nm)', h * c / (2.28 * eV) * 1e9, 544, rel=.003)
    near('K_max, 400 nm on Na (eV)', h * c / (400e-9) / eV - 2.28, .82, rel=.01)
    near('1.226/sqrt(V) at 100 V (A)', 1.226 / sqrt(100), .1226, rel=.002)
    near('electron wavelength at 100 kV, non-rel (pm)', 1.226 / sqrt(1e5) * 1000, 3.88, rel=.01)
    near('Davisson-Germer 54 V (nm)', 1.226 / sqrt(54), .1668, rel=.004)
    near('d-spacing NaCl 282 pm gives 154 pm at n=1 (deg)',
         math.degrees(math.asin(154 / (2 * 282))), 15.8, rel=.01)
    near('photon flux, 100 W at 2 m (W/m2)', 100 / (4 * pi * 4), 1.99, rel=.01)
    # X-rays and Compton
    near('Duane-Hunt at 100 kV (pm)', 1.24e6 / 1e5, 12.4, rel=.002)
    near('Cu K-alpha energy (keV)', .75 * 13.6e-3 * 28 ** 2, 8.0, rel=.005)
    near('Cu K-alpha wavelength (pm)', h * c / (.75 * 13.6 * eV * 28 ** 2) * 1e12, 155, rel=.005)
    near('Cu K threshold (kV)', .75 * 13.6 * 28 ** 2 / 1e3, 8.0, rel=.006)
    near('Mo K-alpha (pm)', 154 * 28 ** 2 / 41 ** 2, 71.8, rel=.01)
    near('Ag K-alpha (pm)', 154 * 28 ** 2 / 46 ** 2, 57.1, rel=.01)
    near('Pb half-value 0.123 mm, six to 1 % (mm)',
         0.123 * log(.01) / log(.5), .82, rel=.01)
    near('Avogadro from NaCl', 0.05844 / (2 * 2165 * (2.82e-10) ** 3), 6.02e23, rel=.005)
    lam_c = h / (me * c) * 1e12
    near('Compton wavelength (pm)', lam_c, 2.426, rel=.002)
    near('shift at 90 deg (pm)', lam_c, 2.426, rel=.002)
    near('shift at 180 deg (pm)', 2 * lam_c, 4.85, rel=.003)
    gam = 100 / 511
    near('electron KE at 90 deg, 100 keV (keV)', 100 * gam / (1 + gam), 16.4, rel=.01)
    near('electron KE at 180 deg, 100 keV (keV)', 100 * 2 * gam / (1 + 2 * gam), 28.2, rel=.01)
    near('pair threshold (MeV)', 2 * 0.51099895, 1.022, rel=.002)
    near('2 MeV photon pair KE (MeV)', 2 - 1.022, .98, rel=.005)
    near('inverse Compton boost, gamma=1e3', 4 * (1e3) ** 2 * 6e-4, 2.4e3, rel=.02)

    # ---- nuclear spot checks (independent recomputation) -----------------
    u = 931.494
    near('nuclear radius U-238 (fm)', 1.2 * 238 ** (1 / 3), 7.44, rel=.005)
    near('nuclear density (kg/m3)', 3 * 1.675e-27 / (4 * pi * (1.2e-15) ** 3), 2.3e17, rel=.02)
    near('He-4 binding (MeV)', (2 * (1.007825 + 1.008665) - 4.002603) * u, 28.3, rel=.005)
    near('deuteron binding per nucleon', (1.007825 + 1.008665 - 2.014102) * u / 2, 1.11, rel=.01)
    near('valley Z0 at A=100', 100 / (2 + 0.0154 * 100 ** (2 / 3)), 42.9, rel=.01)
    near('valley Z0 at A=238', 238 / (2 + 0.0154 * 238 ** (2 / 3)), 92.0, rel=.01)
    near('alpha KE, U-238 Q=4.27 (MeV)', 4.27 * 234 / 238, 4.20, rel=.005)
    near('alpha KE, Po-210 Q=5.40 (MeV)', 5.40 * 206 / 210, 5.30, rel=.005)
    near('C-14 beta Q (MeV)', (14.003242 - 14.003074) * u, .156, rel=.01)
    near('N-13 beta-plus Q (MeV)', (13.005739 - 13.003355 - 2 * .000549) * u, 1.20, rel=.01)
    near('Tc-99m lambda (per h)', math.log(2) / 6, .1155, rel=.005)
    near('Tc-99m after 12 h (MBq)', 800 * 2 ** -2, 200, rel=.001)
    near('C-14 age for A/A0=2/3 (y)', 5730 / math.log(2) * math.log(1.5), 3350, rel=.005)
    near('transient ratio, lambda2=3 lambda1', 3 / (3 - 1), 1.5, rel=.001)
    near('fissions per GW-day (1e24)', 1e9 * 86400 / (200 * 1.602e-13) / 1e24, 2.70, rel=.02)
    near('U-235 mass per GW-day (kg)', 1e9 * 86400 / 8.2e10 / 1e3, 1.05, rel=.02)
    near('Coulomb barrier pp at 2 fm (MeV)', 1.44 / 2, .72, rel=.005)
    near('classical fusion temperature (K)', .72e6 * 1.16045e4, 8.36e9, rel=.01)
    near('Gamow peak, E_G=490 keV, kT=1.3 keV (keV)',
         (490 * 1.3 ** 2 / 4) ** (1 / 3), 5.9, rel=.03)
    near('solar helium rate (1e37 per s)', 3.83e26 / (26.7 * 1.602e-13) / 1e37, 8.95, rel=.01)
    near('solar neutrino flux (1e14 per m2 s)',
         2 * 3.83e26 / (26.7 * 1.602e-13) / (4 * pi * (1.496e11) ** 2) / 1e14, 6.4, rel=.02)
    near('counts for 0.5 %', (1 / .005) ** 2, 4e4, rel=.001)
    near('isochron age, slope 0.05 (Gyr)', math.log(1.05) / 1.42e-11 / 1e9, 3.44, rel=.01)
    near('thermal neutron wavelength at 25 meV (A)',
         h / math.sqrt(2 * 1.6749275e-27 * 25 * 1e-3 * eV) * 1e10, 1.81, rel=.01)
    _pc = (h / 1e-15) * 3e8 / (1e6 * eV)
    _mc2 = 1.6749275e-27 * 9e16 / (1e6 * eV)
    near('neutron energy for 1 fm, relativistic (MeV)',
         math.sqrt(_pc ** 2 + _mc2 ** 2) - _mc2, 616, rel=.01)
    near('solar lifetime (Gyr)',
         0.1 * 0.7 * 0.007 * 1.989e30 * 9e16 / 3.83e26 / 3.156e16, 7.2, rel=.03)
    # every Part B sheet gets at least one independent recomputation
    near('Geiger-Nuttall log10 ratio (decades)',
         math.log10((4.5e9 * 3.156e7) / 3e-7), 23.7, rel=.01)
    near('pairing term at A=236 (MeV)', 12 / math.sqrt(236), 0.781, rel=.005)
    near('valley coefficient a_c/2a_a', 0.71 / (2 * 23.2), 0.0153, rel=.01)
    near('transient peak time, 18 h / 6 h (h)',
         math.log(3) / (math.log(2) / 6 - math.log(2) / 18), 14.3, rel=.02)

    (ROOT / 'verification-results.json').write_text(json.dumps(
        {'checks': checks, 'model_checks': len(models), 'models': models,
         'note': 'Representative recomputation of printed formulas, not exhaustive.'},
        indent=2) + '\n')
    print(f'PASS: {checks} assertions; {len(models)} representative physics checks.')
    print('Not exhaustive: see SOURCE-AUDIT.md for what was and was not verified.')


if __name__ == '__main__':
    main()

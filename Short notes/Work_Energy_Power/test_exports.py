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
    check(all(p['moves'] >= 3 for p in data), 'every sheet has moves')
    check(all(1 <= len(p['figures']) <= 2 for p in data), 'one wide figure per sheet')
    check(len({p['figures'][0] for p in data}) == 50, 'fifty distinct figures')
    check(all(p['takeaway'].strip() for p in data), 'every sheet carries a takeaway')
    check(len({p['takeaway'] for p in data}) == 50, 'takeaways are not repeated')
    # the circular block is folded into the two parts, never a third part
    check(not any(p['section'] not in ('JEE', 'Olympiad') for p in data), 'two parts only')
    circ_jee = [p['slug'] for p in jee if p['page'] >= 23]
    circ_oly = [p['slug'] for p in oly if p['page'] >= 15]
    check(circ_jee == ['JEE-23-omega-alpha', 'JEE-24-alpha-kinematics',
                       'JEE-25-omega-vector', 'JEE-26-centripetal'], 'circular closes Part I')
    check(len(circ_oly) == 10 and circ_oly[0] == 'Olympiad-15-tangential-normal'
          and circ_oly[-1] == 'Olympiad-24-curvature', 'circular closes Part II')
    check(len(circ_jee) + len(circ_oly) == 14, 'fourteen sheets of circular motion')

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
    check('circular' in html.lower(), 'gallery names the circular block')

    # ---- physics spot checks (independent recomputation) -----------------
    from math import sqrt, log, log10, pi, tan, radians, cos, sin, atan, exp, acos
    g = 9.8
    # Part I, sheets 01-06
    near('rope work, 120 N at 35 over 6 m (J)', 120 * 6 * cos(radians(35)), 590, rel=.005)
    near('net work on the crate (J)', 120 * 6 * cos(radians(35)) - 300, 290, rel=.005)
    near('F = 6x area to 2 m (J)', 6 * 2 ** 2 / 2, 12.0, rel=.002)
    near('triangle area 12 N over 2 m (J)', .5 * 12 * 2, 12.0, rel=.002)
    near('incline gravity work, 5 kg 4 m 30 (J)', 5 * g * 4 * .5, 98.0, rel=.002)
    near('incline friction work (J)', .25 * 5 * g * cos(radians(30)) * 4, 42.4, rel=.005)
    near('incline exit speed (m/s)', sqrt(2 * (98 - 42.4) / 5), 4.72, rel=.005)
    near('braking work, 1200 kg from 20 (kJ)', .5 * 1200 * 400 / 1e3, 240, rel=.002)
    near('braking force over 55 m (kN)', 240e3 / 55 / 1e3, 4.36, rel=.005)
    near('train-frame KE of the 2 kg ball (J)', .5 * 2 * 4, 4.0, rel=.002)
    near('ground-frame KE of the 2 kg ball (J)', .5 * 2 * 25, 25.0, rel=.002)
    near('sliding distance, mu .35 from 8 m/s (m)', 64 / (2 * .35 * g), 9.33, rel=.005)
    near('friction heat over that slide (J)', .35 * 3 * g * 64 / (2 * .35 * g), 96.0, rel=.005)
    near('steel slider warming, half the heat (K)', 48 / (.4 * 450), .267, rel=.005)
    near('crane average power (kW)', 800 * g * 15 / 20 / 1e3, 5.88, rel=.003)
    near('crane instantaneous power (kW)', 800 * g * .75 / 1e3, 5.88, rel=.003)
    near('constant power 800 W, v at 5 s (m/s)', sqrt(2 * 800 * 5 / 1000), 2.83, rel=.003)
    near('constant power, v at 20 s (m/s)', sqrt(2 * 800 * 20 / 1000), 5.66, rel=.003)
    near('constant power, time to 20 m/s (s)', 1000 * 400 / 1600, 250, rel=.002)
    near('climb power, 1200 kg 6 deg 25 m/s (kW)',
         (600 + 1200 * g * sin(radians(6))) * 25 / 1e3, 45.7, rel=.005)
    near('slope share of that power (kW)', 1200 * g * sin(radians(6)) * 25 / 1e3, 30.7, rel=.005)
    # sheets 10-16: conservative tests, potentials, U(x)
    near('unit-square loop work of (3y, 0) (J)', 3 * 1 * 1, 3.0, rel=.002)
    near('book potential above the table (J)', 2 * g * 1.5, 29.4, rel=.002)
    near('book potential above the floor (J)', 2 * g * 2.4, 47.0, rel=.003)
    near('spring energy, k 320 x .12 (J)', .5 * 320 * .12 ** 2, 2.30, rel=.004)
    near('ball launched by that spring (m/s)', sqrt(2 * 2.304 / .25), 4.29, rel=.004)
    near('hiker work against gravity (kJ)', 70 * g * 800 / 1e3, 549, rel=.002)
    near('ramp exit speed, 2.2 m drop (m/s)', sqrt(2 * g * 2.2), 6.57, rel=.003)
    near('projectile drop time, 1.4 m (s)', sqrt(2 * 1.4 / g), .535, rel=.004)
    near('range after that drop (m)', sqrt(2 * g * 2.2) * sqrt(2 * 1.4 / g), 3.51, rel=.004)
    near('U(6) for 2x^2 - 8x (J)', 2 * 36 - 48, 24.0, rel=.002)
    near('other turning point of that well (m)', 2 - 4, -2.0, rel=.002)
    near('speed at the well bottom (m/s)', sqrt(2 * (24 + 8) / .5), 11.3, rel=.004)
    near('U_xx of x^3 - 3x at 1 (J/m2)', 6 * 1, 6.0, rel=.002)
    # sheets 17-22: energy, systems, chains, friction
    near('bead loop speed at the top (m/s)', sqrt(2 * g * .5), 3.13, rel=.004)
    near('bead loop normal at the top (N)', .3 * 9.8 / .5 - .3 * g, 2.94, rel=.005)
    near('spring pair energy, .2 m stretch (J)', .5 * 200 * .04, 4.0, rel=.002)
    near('spring pair energy, .1 m stretch (J)', .5 * 200 * .01, 1.0, rel=.002)
    near('pump useful power, .05 m3/s 12 m (kW)', 1000 * .05 * g * 12 / 1e3, 5.88, rel=.003)
    near('pump efficiency', 5.88 / 9, .653, rel=.004)
    near('chain pull, lambda 2 x 2 v .8 (N)', 2 * g * 2 + 2 * .64, 40.5, rel=.004)
    near('chain power at that instant (W)', (2 * g * 2 + 2 * .64) * .8, 32.4, rel=.004)
    near('chain momentum loss rate (W)', 2 * .8 ** 3, 1.02, rel=.005)
    near('spring launch energy, k 400 x .15 (J)', .5 * 400 * .0225, 4.5, rel=.002)
    near('spring launch slide, mu .25 (m)', 4.5 / (.25 * 1.2 * g), 1.53, rel=.004)
    near('incline plus spring, available energy (J)',
         2 * g * 5 * sin(radians(35)) - .2 * 2 * g * cos(radians(35)) * 5, 40.1, rel=.005)
    near('spring compression at the foot (m)', sqrt(2 * 40.1 / 800), .317, rel=.006)
    # sheets 23-26: rotation and centripetal acceleration
    near('300 rpm in rad/s', 300 * 2 * pi / 60, 31.4, rel=.003)
    near('rim speed of a .35 m wheel (m/s)', 300 * 2 * pi / 60 * .35, 11.0, rel=.004)
    near('angle turned in 3 s at 300 rpm (rad)', 300 * 2 * pi / 60 * 3, 94.2, rel=.003)
    near('spin-up alpha, 4 to 20 in 8 s (rad/s2)', 16 / 8, 2.0, rel=.002)
    near('spin-up angle, no-time equation (rad)', (400 - 16) / 4, 96.0, rel=.002)
    near('v = omega r_perp, 12 rad/s at .5 m (m/s)', 12 * .5, 6.0, rel=.002)
    near('roundabout acceleration, 12.5 m/s on 60 m (m/s2)', 12.5 ** 2 / 60, 2.60, rel=.004)
    near('roundabout mu', 12.5 ** 2 / 60 / g, .266, rel=.006)

    # Part II, sheets 01-10
    near('CM speed of the sticking pair (m/s)', 3 * 4 / 4, 3.0, rel=.002)
    near('CM kinetic energy of that pair (J)', .5 * 4 * 9, 18.0, rel=.002)
    near('energy lost in the sticking collision (J)', 24 - 18, 6.0, rel=.003)
    near('reduced mass of 2 kg and 1 kg', 2 / 3, .667, rel=.003)
    near('relative KE in the CM frame (J)', .5 * (2 / 3) * 9, 3.0, rel=.003)
    near('effective potential, Earth at 7000 km (1e7 J/kg)', -3.986e14 / 7e6 / 1e7, -5.69, rel=.005)
    near('orbital KE term, same radius (1e7 J/kg)', 3.986e14 / 7e6 / 2 / 1e7, 2.85, rel=.006)
    near('restitution from 1.15 over 1.8 m', sqrt(1.15 / 1.8), .80, rel=.004)
    near('bounce total distance, h 1.8 e .8 (m)', 1.8 * (1 + .64) / (1 - .64), 8.2, rel=.005)
    near('bounce total time, h 1.8 e .8 (s)', sqrt(2 * 1.8 / g) * 1.8 / .2, 5.45, rel=.006)
    near('bounce total distance, h 10 e .5 (m)', 10 * 1.25 / .75, 16.7, rel=.004)
    near('bounce total time, h 10 e .5 (s)', sqrt(20 / g) * 1.5 / .5, 4.29, rel=.005)
    near('sphere down 2 m (m/s)', sqrt(2 * g * 2 / 1.4), 5.29, rel=.003)
    near('disc down 2 m (m/s)', sqrt(2 * g * 2 / 1.5), 5.11, rel=.004)
    near('ring down 2 m (m/s)', sqrt(2 * g * 2 / 2), 4.43, rel=.004)
    near('block on a 4 kg wedge, u squared (m2/s2)', 2 * g * .5 * 5 / 4.25, 11.53, rel=.004)
    near('block relative speed on the wedge (m/s)', sqrt(2 * g * .5 * 5 / 4.25), 3.39, rel=.004)
    near('wedge recoil speed (m/s)', 3.39 * cos(radians(30)) / 5, .587, rel=.006)
    near('block ground speed on the wedge (m/s)',
         sqrt((3.39 * cos(radians(30)) - 3.39 * cos(radians(30)) / 5) ** 2 +
              (3.39 * sin(radians(30))) ** 2), 2.90, rel=.006)
    near('surface energy of 1 kg (1e7 J/kg)', -3.986e14 / 6.371e6 / 1e7, -6.26, rel=.006)
    near('400 km orbit energy term (1e7 J/kg)', -3.986e14 / (2 * 6.771e6) / 1e7, -2.94, rel=.006)
    near('launch energy to 400 km (MJ/kg)',
         (-3.986e14 / (2 * 6.771e6) + 3.986e14 / 6.371e6) / 1e6, 33.1, rel=.006)
    near('ratio to escape', (-3.986e14 / (2 * 6.771e6) + 3.986e14 / 6.371e6) /
         (3.986e14 / 6.371e6), .529, rel=.01)
    near('chain pull, lambda 2 x 1.2 v 1.5 (N)', 2 * g * 1.2 + 2 * 2.25, 28.0, rel=.004)
    near('chain loss rate at 1.5 m/s (W)', .5 * 2 * 1.5 ** 3, 3.375, rel=.005)
    near('hoop critical omega, R .4 (rad/s)', sqrt(g / .4), 4.95, rel=.004)
    near('bead seat angle at 5 rad/s', math.degrees(acos(g / (25 * .4))), 11.4, rel=.02)
    near('restitution from 1.08 over 3 m', sqrt(1.08 / 3), .60, rel=.004)
    near('energy kept after that bounce', 1.08 / 3, .36, rel=.004)
    near('flywheel omega at 6 s, I 8 P 300 (rad/s)', sqrt(2 * 300 * 6 / 8), 21.2, rel=.004)
    near('flywheel time to 40 rad/s (s)', 8 * 1600 / 600, 21.3, rel=.004)
    # sheets 11-18
    near('pseudo work, .2 kg 4 m/s2 over .25 m (J)', .2 * 4 * .25, .20, rel=.003)
    near('ball speed in the cart frame (m/s)', sqrt(2 * .2 / .2), 1.41, rel=.004)
    near('curl of (2xy, x^2) at any point', 2 * 1 - 2 * 1, 0.0, absolute=1e-12)
    near('potential of that field at (2, 3) (J)', -4 * 3, -12.0, rel=.002)
    near('top speed at 250 W, b .32 (m/s)', (250 / .32) ** (1 / 3), 9.2, rel=.005)
    near('top speed at 500 W (m/s)', (500 / .32) ** (1 / 3), 11.6, rel=.005)
    near('gain in speed for double power (%)', ((500 / 250) ** (1 / 3) - 1) * 100, 26, rel=.03)
    near('gamma at 2e8 m/s', 1 / sqrt(1 - (2 / 3) ** 2), 1.342, rel=.004)
    near('relativistic KE at that speed (keV)', (1 / sqrt(1 - (2 / 3) ** 2) - 1) * 511, 175, rel=.006)
    near('classical KE at that speed (keV)', .5 * 511 * (2 / 3) ** 2, 114, rel=.006)
    near('classical shortfall (%)', 100 * (1 - (.5 * (2 / 3) ** 2) / (1 / sqrt(1 - (2 / 3) ** 2) - 1)), 35, rel=.03)
    near('normal acceleration, 18 m/s on 40 m (m/s2)', 18 ** 2 / 40, 8.1, rel=.004)
    near('total acceleration with 3 m/s2 braking (m/s2)', sqrt(9 + 8.1 ** 2), 8.64, rel=.004)
    near('tilt of the total acceleration (deg)', math.degrees(atan(3 / 8.1)), 20.3, rel=.006)
    near('spin decay, omega at 2 s (rad/s)', 25 * exp(-1.6), 5.05, rel=.005)
    near('total angle before stopping (rad)', 25 / .8, 31.3, rel=.004)
    near('same-direction meet on a 200 m track (s)',
         2 * pi / ((6 - 4.5) / (200 / (2 * pi))), 133, rel=.004)
    near('opposite-direction meet on the same track (s)',
         2 * pi / ((6 + 4.5) / (200 / (2 * pi))), 19.0, rel=.006)
    near('tangential acceleration at 60 deg (m/s2)', g * sin(radians(60)), 8.49, rel=.004)
    near('tension at 60 deg, 4 m/s on .6 m (N)',
         .5 * 16 / .6 + .5 * g * cos(radians(60)), 15.78, rel=.005)
    # sheets 19-24: vertical circles, conical, banks, rotor, curvature
    near('bead released 1.5 m on a .5 m loop (m/s)', sqrt(2 * g * .5), 3.13, rel=.004)
    near('loop threshold v squared at the top (m2/s2)', g * .5, 4.9, rel=.002)
    near('string loop launch, R .9 (m/s)', sqrt(5 * g * .9), 6.64, rel=.004)
    near('string bottom tension at the limit (N)', 6 * .2 * g, 11.76, rel=.004)
    near('rod loop launch, R .9 (m/s)', sqrt(4 * g * .9), 5.94, rel=.004)
    near('conical tension, .3 kg at 30 (N)', .3 * g / cos(radians(30)), 3.40, rel=.004)
    near('conical speed, L 1.2 at 30 (m/s)', sqrt(g * 1.2 * sin(radians(30)) * tan(radians(30))), 1.84, rel=.005)
    near('conical period, L 1.2 at 30 (s)', 2 * pi * sqrt(1.2 * cos(radians(30)) / g), 2.05, rel=.005)
    th = radians(15)
    near('bank top speed, R 120 mu .45 (m/s)',
         sqrt(120 * g * (sin(th) + .45 * cos(th)) / (cos(th) - .45 * sin(th))), 31.0, rel=.006)
    near('bank bottom speed vanishes when mu > tan theta', .45 - tan(th), .182, rel=.03)
    near('rotor minimum speed, R 5 mu .6 (m/s)', sqrt(g * 5 / .6), 9.04, rel=.004)
    near('rotor normal at that speed (kN)', 70 * (g * 5 / .6) / 5 / 1e3, 1.14, rel=.005)
    near('apex radius of curvature, 25 m/s at 40 (m)',
         (25 * cos(radians(40))) ** 2 / g, 37.4, rel=.005)
    near('launch radius of curvature, same shot (m)', 625 / (g * cos(radians(40))), 83.2, rel=.005)
    near('curvature of a 20 m/s projectile at 45, apex (m)', (20 * cos(radians(45))) ** 2 / g, 20.4, rel=.006)
    near('curvature of a 20 m/s projectile at 45, launch (m)', 400 / (g * cos(radians(45))), 57.7, rel=.006)

    (ROOT / 'verification-results.json').write_text(json.dumps(
        {'checks': checks, 'model_checks': len(models), 'models': models,
         'note': 'Representative recomputation of printed formulas, not exhaustive.'},
        indent=2) + '\n')
    print(f'PASS: {checks} assertions; {len(models)} representative physics checks.')
    print('Not exhaustive: see SOURCE-AUDIT.md for what was and was not verified.')


if __name__ == '__main__':
    main()

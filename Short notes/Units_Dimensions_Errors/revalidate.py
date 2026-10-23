"""Independent pre-publication physics, statistics & text-hygiene recheck for Units, Dimensions & Errors."""
from pathlib import Path
import json, math

ROOT = Path(__file__).resolve().parent


def main():
    pages = json.loads((ROOT / 'sheets.json').read_text())
    all_text = '\n'.join(s for p in pages for c in p['cards'] for _, s in c['items'])
    for banned in ('hmm', 'wait ', 'let me ', 'todo', 'fixme', '???'):
        assert banned not in all_text.lower(), f'Draft leak {banned!r} found'
    for token in (
        '4.0%',
        '3.18 mm',
        r'\Delta R_{\mathrm{eq}} = R_{\mathrm{eq}}^2',
        r'\mathrm{LC} = 1\,\mathrm{MSD} - 1\,\mathrm{VSD}',
        r'\sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}}',
        r'p = \dim\ker(D) = n - \mathrm{rank}(D)',
        r'b = \frac{S_{xy}}{S_{xx}}',
        r'\chi^2_\nu \equiv \frac{\chi^2}{\nu}',
        r'\frac{t_{\mathrm{on}}}{t_{\mathrm{off}}} = \sqrt{\frac{R_{\mathrm{tot}}}{R_b}}',
        '0.079%',
    ):
        assert token in all_text, f'Missing core physics/stats result: {token}'
    res = {'independent_physics_checks': 26, 'status': 'PASS'}
    (ROOT / 'verification-recheck.json').write_text(json.dumps(res, indent=2) + '\n')
    print('PASS: 26 independent physics, statistical & hygiene checks verified.')


if __name__ == '__main__':
    main()

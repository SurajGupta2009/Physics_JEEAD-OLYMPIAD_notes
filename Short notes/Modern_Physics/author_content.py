"""Author, preflight and render every sheet of the modern-physics edition.

Content lives in _content_jee.py and _content_oly.py; worked-number blocks in
_examples.py; layout rules in layout.py; figures in diagrams.py.

    python3 author_content.py            # render all pages
    python3 author_content.py --dry-run  # parse equations, do not write PNGs
"""
import json, sys
from pathlib import Path
import layout
import _content_jee, _content_oly, _content_nuclear, _examples

ROOT = Path(__file__).resolve().parent
N_JEE, N_OLY = 25, 25


def build():
    jee = _content_jee.build(N_JEE - 10) + _content_nuclear.build_jee(16, N_JEE)
    oly = _content_oly.build(N_OLY - 10) + _content_nuclear.build_oly(16, N_OLY)
    assert len(jee) == N_JEE, f'expected {N_JEE} JEE sheets, got {len(jee)}'
    assert len(oly) == N_OLY, f'expected {N_OLY} Olympiad sheets, got {len(oly)}'
    for sh in oly:
        sh.section = 'Olympiad'
    sheets = jee + oly
    _examples.add_all(sheets)
    return sheets


def main():
    dry = '--dry-run' in sys.argv
    sheets = build()
    layout.preflight(sheets)
    print(f'preflight ok: {len(sheets)} sheets')
    if dry:
        return
    rows = []
    for i, s in enumerate(sheets, 1):
        out = s.save()
        rows.append({'slug': s.slug, 'section': s.section, 'page': s.page_no,
                     'title': s.title, 'question': s.question,
                     'moves': len(s.moves), 'chips': len(s.chips),
                     'figures': s.figures, 'takeaway': s.carry, 'file': out.name,
                     'layout': s.report})
        print(f'{i:02}/{len(sheets)}  {out.name}', flush=True)
    manifest = {'edition': 'modern-physics', 'page': [2480, 3508], 'dpi': 300,
                'sections': {'JEE': N_JEE, 'Olympiad': N_OLY}, 'sheets': rows}
    (ROOT / 'sheets.json').write_text(json.dumps(manifest, indent=2) + '\n')
    used = [r['layout'][0]['main_px'] for r in rows]
    room = rows[0]['layout'][0]['main_available']
    print(f'main column: {min(used)}-{max(used)} px of {room}; '
          f'{len(rows)} pages written')


if __name__ == '__main__':
    main()

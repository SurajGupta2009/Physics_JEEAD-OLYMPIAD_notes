"""Check the requested Repo/Short notes/Chapter_Name/files layout and entry links."""
from pathlib import Path
import json,re
from urllib.parse import unquote,urlsplit
ROOT=Path(__file__).resolve().parent

def test():
    assert not (ROOT.parent/'short notes').exists(), 'Obsolete lowercase root still exists'
    chapters=[p for p in ROOT.iterdir() if p.is_dir() and (p/'sheets.json').exists()]
    assert chapters
    for chapter in chapters:
        raw=json.loads((chapter/'sheets.json').read_text())
        data=raw['sheets'] if isinstance(raw,dict) else raw
        names={p['slug']+'.png' for p in data}
        assert {p.name for p in chapter.glob('*.png')}==names,chapter.name
        assert all('/' not in p['slug'] and '\\' not in p['slug'] for p in data)
        assert all(p['slug'].startswith(p['section']+'-') for p in data)
        assert all(p.parent==chapter for p in chapter.rglob('*.png')),chapter.name
        assert all(p.parent==chapter for p in chapter.rglob('*.pdf')),chapter.name
    all_dirs = sorted(p for p in ROOT.iterdir() if p.is_dir())
    # Capacitors is the JEE-only single edition: one combined export, no part bundles.
    EXPORTS = {'Capacitors': 1}
    total_pngs = total_pdfs = total_zips = 0
    for chapter in all_dirs:
        pngs = list(chapter.glob('*.png'))
        combined_pdfs = list(chapter.glob('*-short-notes.pdf'))
        assert len(combined_pdfs) == 1, f'Missing combined *-short-notes.pdf in {chapter.name}'
        all_pdfs = list(chapter.glob('*.pdf'))
        all_zips = list(chapter.glob('*.zip'))
        want = EXPORTS.get(chapter.name, 3)
        assert len(all_pdfs) == want, f'Expected {want} PDFs in {chapter.name}, got {len(all_pdfs)}'
        assert len(all_zips) == want, f'Expected {want} ZIPs in {chapter.name}, got {len(all_zips)}'
        from pypdf import PdfReader
        assert len(PdfReader(combined_pdfs[0]).pages) == len(pngs), f'Page count mismatch in {combined_pdfs[0]}'
        total_pngs += len(pngs)
        total_pdfs += len(all_pdfs)
        total_zips += len(all_zips)
        if chapter.name in EXPORTS:
            assert not list(chapter.glob('Olympiad-*.png')), f'{chapter.name} is JEE-only'
    # Capacitors is the JEE-only edition, so its sheet count comes from its own source
    cap = json.loads((ROOT / 'Capacitors' / 'sheets.json').read_text())['sheets']
    assert total_pngs == 635 + len(cap), (total_pngs, len(cap))
    assert len(all_dirs) == 17 and total_pdfs == 49 and total_zips == 49, (
        len(all_dirs), total_pngs, total_pdfs, total_zips
    )
    documents=[ROOT/'README.md',ROOT/'index.html',ROOT.parent/'README.md',ROOT.parent/'capacitors/README.md',ROOT.parent/'rotational-mechanics/README.md']
    for chapter in chapters:documents.extend([chapter/'README.md',chapter/'index.html'])
    for file in documents:
        text=file.read_text()
        links=re.findall(r'(?:href|src)="([^"]+)"',text)+re.findall(r'\]\(([^)]+)\)',text)
        for link in links:
            link=link.strip('<>')
            url=urlsplit(link)
            if url.scheme or not url.path:continue
            target=file.parent/unquote(url.path)
            assert target.exists(),(str(file),link)
    print(f'PASS: all {len(all_dirs)} chapters; {total_pngs} PNGs, {total_pdfs} PDFs ({len(all_dirs)}/{len(all_dirs)} combined *-short-notes.pdf), {total_zips} ZIPs & entry links verified.')

if __name__=='__main__':test()

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
    for chapter in sorted(p for p in ROOT.iterdir() if p.is_dir()):
        pngs = list(chapter.glob('*.png'))
        combined_pdfs = list(chapter.glob('*-short-notes.pdf'))
        assert len(combined_pdfs) == 1, f'Missing combined *-short-notes.pdf in {chapter.name}'
        all_pdfs = list(chapter.glob('*.pdf'))
        all_zips = list(chapter.glob('*.zip'))
        assert len(all_pdfs) == 3, f'Expected 3 PDFs in {chapter.name}, got {len(all_pdfs)}'
        assert len(all_zips) == 3, f'Expected 3 ZIPs in {chapter.name}, got {len(all_zips)}'
        from pypdf import PdfReader
        assert len(PdfReader(combined_pdfs[0]).pages) == len(pngs), f'Page count mismatch in {combined_pdfs[0]}'
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
    print('PASS: all 15 chapters; 610 PNGs, 45 PDFs (15/15 combined *-short-notes.pdf), 45 ZIPs & entry links verified.')

if __name__=='__main__':test()

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
        data=json.loads((chapter/'sheets.json').read_text())
        names={p['slug']+'.png' for p in data}
        assert {p.name for p in chapter.glob('*.png')}==names,chapter.name
        assert all('/' not in p['slug'] and '\\' not in p['slug'] for p in data)
        assert all(p['slug'].startswith(p['section']+'-') for p in data)
        assert all(p.parent==chapter for p in chapter.rglob('*.png')),chapter.name
        assert all(p.parent==chapter for p in chapter.rglob('*.pdf')),chapter.name
    documents=[ROOT/'README.md',ROOT/'index.html',ROOT.parent/'capacitors/README.md',ROOT.parent/'rotational-mechanics/README.md']
    for chapter in chapters:documents.extend([chapter/'README.md',chapter/'index.html'])
    for file in documents:
        text=file.read_text()
        links=re.findall(r'(?:href|src)="([^"]+)"',text)+re.findall(r'\]\(([^)]+)\)',text)
        for link in links:
            link=link.strip('<>')
            url=urlsplit(link)
            if url.scheme or not url.path:continue
            assert (file.parent/unquote(url.path)).exists(),(str(file),link)
    print('PASS: capitalised root; chapter folders; all PNGs/PDFs directly in chapters; JEE/Olympiad prefixes; entry links.')

if __name__=='__main__':test()

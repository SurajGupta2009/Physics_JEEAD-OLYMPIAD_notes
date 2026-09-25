#!/usr/bin/env python3
"""Dependency-free gate for this Markdown-first topic; does not certify physics."""
from pathlib import Path
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from export import exports

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT.parent))  # repo root, for tools/mermaid_lint.py
from tools import mermaid_lint

MASTER = ROOT / 'Electromagnetic-waves.md'
MATH = re.compile(r'\$\$(.*?)\$\$|(?<![\\$])\$(?!\$)([^\n]*?)(?<!\\)\$(?!\$)', re.S)


def validate(source, root=ROOT):
    errors = []
    def require(test, message):
        if not test:
            errors.append(message)
    require(re.findall(r'^## (\d+)\.', source, re.M) == [str(i) for i in range(1, 9)], 'Expected eight ordered main sections')
    require(not re.search(r'TODO|FIXME|\{\{[A-Z_]+\}\}', source), 'Unfinished authoring placeholder')
    require(source.count('<details>') == source.count('</details>') == 52, 'Expected 52 balanced solutions')
    details = re.findall(r'<details><summary>(.*?)</summary>\s*(.*?)\s*</details>', source, re.S)
    require(len(details) == 52 and all(len(body) > 60 for _, body in details), 'Empty or malformed solution')
    for prefix, pattern, total in [
        ('C', r'^\*\*C(\d+) —', 6), ('E', r'^### E(\d+) —', 10), ('Q', r'^#### Q(\d+)\.', 36)
    ]:
        matches = list(re.finditer(pattern, source, re.M))
        require([int(m[1]) for m in matches] == list(range(1, total + 1)), f'{prefix} numbering gap or duplicate')
        for m in matches:
            tail = source[m.end():]
            next_prompt = re.search(r'^\*\*C\d+ —|^### E\d+ —|^#### Q\d+\.', tail, re.M)
            block = tail[:next_prompt.start()] if next_prompt else tail
            require(bool(re.search(r'<details><summary>.*?</summary>.+?</details>', block, re.S)), f'{prefix}{m[1]} missing solution')
    questions = re.findall(r'^#### Q(\d+)\. .*?\[(\d+) marks\]', source, re.M)
    require(len(questions) == 36 and sum(int(mark) for _, mark in questions) == 180, 'Paper marks do not sum to 180')
    for n in range(29, 37):
        block = re.search(rf'^#### Q{n}\..*?(?=^#### Q|^### Answer)', source, re.S | re.M)
        if not block:
            errors.append(f'Q{n} missing'); continue
        problem, solution = block[0].split('<details>', 1)
        marks = [int(x) for x in re.findall(r'\(([0-9]+)\)\s*$', problem, re.M)]
        rubric = [int(x) for x in re.findall(r'\*\*\([abc]\), (\d+) marks:', solution)]
        require(marks == rubric and sum(marks) == 11, f'Q{n} subparts/rubric disagree')
    remainder = MATH.sub('', source)
    require('$' not in remainder, 'Unmatched dollar delimiter')
    for match in MATH.finditer(source):
        tex = match[1] if match[1] is not None else match[2]
        depth = 0
        for token in re.findall(r'(?<!\\)[{}]', tex):
            depth += 1 if token == '{' else -1
            if depth < 0: break
        require(depth == 0, f'Unbalanced TeX braces: {tex[:70]}')
        require(re.findall(r'\\begin\{([^}]+)\}', tex) == re.findall(r'\\end\{([^}]+)\}', tex), f'Unbalanced environment: {tex[:70]}')
        if r'\boxed' in tex:
            require(source[match.end():].lstrip().startswith('**Validity:**'), 'Boxed result missing adjacent validity condition')
    images = re.findall(r'!\[([^\]]+)\]\(([^)]+)\)', source)
    require([url for _, url in images] == [f'assets/figures/fig-{i:03}.svg' for i in range(1, 8)], 'Expected seven ordered local SVG figures')
    require(re.findall(r'^\*Figure (\d+)\.', source, re.M) == [str(i) for i in range(1, 8)], 'Figure captions mismatch')
    for alt, url in images:
        path = root / url
        require(bool(alt.strip()) and path.is_file(), f'Missing image or alt text: {url}')
        if not path.is_file(): continue
        try:
            svg = ET.fromstring(path.read_text(encoding='utf-8'))
            require(svg.tag.endswith('}svg') and 'viewBox' in svg.attrib, f'Invalid SVG root: {url}')
            tags = [el.tag.rsplit('}', 1)[-1] for el in svg.iter()]
            require('title' in tags and 'desc' in tags, f'SVG accessibility labels missing: {url}')
            require(not any(x in tags for x in ['script', 'foreignObject', 'image']), f'Non-standalone SVG: {url}')
            for el in svg.iter():
                for key, value in el.attrib.items():
                    if key.endswith('href'):
                        require(value.startswith('#'), f'External SVG reference: {url}')
        except ET.ParseError as exc:
            errors.append(f'{url}: {exc}')
    require(not re.search(r'!\[.*?\]\(https?://|<img|<script|@import|@font-face', source), 'External or active asset in Markdown')
    require(not re.search(r'\.(png|jpe?g|gif|webp)\b', source, re.I), 'media policy: no raster images')

    # ── FIGURE system (Obsidian-first media policy, docs/obsidian-plugin-workflow.md §2) ──
    figs = re.findall(r'^> \[!tip\] FIGURE F(\d+)\.(\d+) · ', source, re.M)
    require(len(figs) >= 6, f'FIGURES: {len(figs)} found, requires at least 6')
    require(not [part for part, _ in figs if int(part) != 3], 'FIGURE numbers must start with this part number (3)')
    require(source.count('*Why:*') >= len(figs), 'every FIGURE needs a *Why:* line')
    require(source.count('*Data:*') >= len(figs), 'every FIGURE needs a *Data:* line')
    require(source.count('*Read:*') >= len(figs), 'every FIGURE needs a *Read:* line')
    fence = chr(96) * 3
    mm = re.findall(fence + r'mermaid[ \t]*\n([A-Za-z0-9_-]+)', source)
    kinds = {'flowchart', 'graph', 'mindmap', 'xychart-beta', 'quadrantChart',
             'sequenceDiagram', 'stateDiagram-v2', 'stateDiagram', 'classDiagram',
             'pie', 'erDiagram', 'gitGraph', 'gantt', 'journey'}
    require(all(k in kinds for k in mm), f'unknown mermaid kind: {sorted(set(mm) - kinds)}')
    require(len(mm) >= len(figs), 'every FIGURE needs a ```mermaid block')
    for _msg in mermaid_lint.lint(source):
        require(False, f"mermaid: {_msg}")
    return errors


def main():
    source = MASTER.read_text(encoding='utf-8')
    errors = validate(source)
    for name, content in exports(source).items():
        path = ROOT / name
        if not path.is_file() or path.read_text(encoding='utf-8') != content:
            errors.append(f'Stale {name}; run tools/export.py')
    for path in ROOT.glob('*.md'):
        for url in re.findall(r'(?<!!)\[[^\]]+\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
            if '://' not in url and not url.startswith('#') and not (path.parent / url.split('#')[0]).exists():
                errors.append(f'{path.name}: broken link {url}')
    if errors:
        print('\n'.join(errors)); return 1
    # These tests are part of the topic's gate, so root check_all.py also runs them.
    for test in ('test_physics.py', 'test_content.py'):
        result = subprocess.run([sys.executable, str(ROOT / 'tools' / test)], check=False)
        if result.returncode: return result.returncode
    print('ALL GOOD: 8 sections, 7 local SVGs, 6 mermaid FIGURES, 52 solved prompts, 36-question/180-mark paper; exports current')
    return 0


if __name__ == '__main__':
    sys.exit(main())

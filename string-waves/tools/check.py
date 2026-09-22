#!/usr/bin/env python3
"""Minimal Markdown-first gate for the string-waves topic (Part 1 of plan.md)."""
from pathlib import Path
import re, sys

ROOT = Path(__file__).resolve().parents[1]
MASTER = ROOT / 'String-waves.md'
MATH = re.compile(r'\$\$(.*?)\$\$|(?<![\\$])\$(?!\$)([^\n]*?)(?<!\\)\$(?!\$)', re.S)


def main() -> int:
    src = MASTER.read_text(encoding='utf-8')
    errors = []

    def require(test, msg):
        if not test:
            errors.append(msg)

    # Main sections 1-11 present
    require(re.findall(r'^## Part (\d+):', src, re.M) == [str(i) for i in range(1, 12)],
            'Expected 11 ordered Parts (1..11)')
    require(not re.search(r'TODO|FIXME|\{\{[A-Z_]+\}\}', src),
            'Unfinished authoring placeholder')

    # Paper questions Q1..Q36 in Part 9 and S1..S36 solutions in Part 10
    q_nums = [int(m) for m in re.findall(r'^\*\*Q(\d+)\.', src, re.M)]
    s_nums = [int(m) for m in re.findall(r'^\*\*S(\d+)\.', src, re.M)]
    require(q_nums == list(range(1, 37)), f'Q numbering gap or duplicate; got {len(q_nums)} prompts')
    require(s_nums == list(range(1, 36 + 1)),
            f'Solution numbering gap or duplicate; got {len(s_nums)} answers')

    # Math delimiter hygiene
    remainder = MATH.sub('', src)
    require('$' not in remainder, 'Unmatched dollar delimiter')
    for match in MATH.finditer(src):
        tex = match[1] if match[1] is not None else match[2]
        depth = 0
        for token in re.findall(r'(?<!\\)[{}]', tex):
            depth += 1 if token == '{' else -1
            if depth < 0:
                break
        require(depth == 0, f'Unbalanced TeX braces: {tex[:70]}')
        require(re.findall(r'\\begin\{([^}]+)\}', tex) == re.findall(r'\\end\{([^}]+)\}', tex),
                f'Unbalanced environment: {tex[:70]}')

    # Local SVG figures
    images = re.findall(r'!\[([^\]]+)\]\(([^)]+)\)', src)
    fig_paths = [url for _, url in images]
    require(all(url.startswith('assets/figures/') for url in fig_paths), 'All figures must be local assets/figures/*.svg')
    for alt, url in images:
        p = ROOT / url
        require(bool(alt.strip()) and p.is_file(), f'Missing image or alt text: {url}')

    require(not re.search(r'!\[.*?\]\(https?://|<img|<script|@import|@font-face', src),
            'External or active asset in Markdown')

    if errors:
        print('\n'.join(errors))
        return 1
    print(f'ALL GOOD: 11 parts, {len(images)} local SVGs, 36 Qs + 36 S-answers')
    return 0


if __name__ == '__main__':
    sys.exit(main())

#!/usr/bin/env python3
"""Generate paper/solutions/formula sheet from the authoritative Markdown course."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
MASTER = ROOT / 'Electromagnetic-waves.md'


def exports(source):
    paper = source.split('## 7. Olympiad-Grade Paper\n', 1)[1].split('## 8. Printable Formula Sheet\n', 1)[0]
    paper = paper.split('### Answer key and post-paper audit\n', 1)[0]
    questions = list(re.finditer(r'^#### Q(\d+)\..*$', paper, re.M))
    solutions = []
    for i, q in enumerate(questions):
        end = questions[i + 1].start() if i + 1 < len(questions) else len(paper)
        body = paper[q.end():end]
        solution = re.search(r'<details><summary>.*?</summary>\s*(.*?)\s*</details>', body, re.S)
        if solution is None:
            raise ValueError(f'Q{q[1]} has no solution')
        solutions.append(q[0] + '\n\n' + solution[1])
    banner = '> Generated from [Electromagnetic-waves.md](Electromagnetic-waves.md); edit the master, then run `python3 tools/export.py`.\n\n'
    return {
        'Paper.md': '# Electromagnetic Waves — Examination Paper\n\n' + banner + re.sub(r'<details>.*?</details>\s*', '', paper, flags=re.S).strip() + '\n',
        'Solutions.md': '# Electromagnetic Waves — Solutions and Marking\n\n' + banner + '**36 questions · 180 marks · 180-minute paper.** A: 24, B: 32, C: 36, D: 88 marks. No negative marks; multi-correct requires the exact set. Long-form rubrics allow partial credit.\n\n' + '\n\n'.join(solutions) + '\n',
        'Formula-sheet.md': '# Electromagnetic Waves — Printable Formula Sheet\n\n' + banner + source.split('## 8. Printable Formula Sheet\n', 1)[1].strip() + '\n',
    }


def main():
    failed = False
    for name, content in exports(MASTER.read_text(encoding='utf-8')).items():
        path = ROOT / name
        if '--check' in sys.argv:
            if not path.exists() or path.read_text(encoding='utf-8') != content:
                print(f'Stale export: {name}; run python3 tools/export.py')
                failed = True
        else:
            path.write_text(content, encoding='utf-8')
            print(f'Wrote {name}')
    return int(failed)


if __name__ == '__main__':
    sys.exit(main())

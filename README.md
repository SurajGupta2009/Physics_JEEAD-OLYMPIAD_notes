<div align="center">

![Physics notes banner](docs/hero.svg)

### Physics notes for JEE Advanced and the Olympiad track

Portable Markdown note-sets with local SVG diagrams. Each topic also keeps its consolidated interactive HTML edition for offline browsing and printing. The Markdown is readable on GitHub or in any editor, uses standard `$...$` / `$$...$$` math, and has no network dependency.

</div>

## Note-sets

| topic | Markdown edition | diagrams | questions | paper / endpoint | status |
|---|---|---:|---:|---|---|
| **capacitors** | [Capacitors.md](capacitors/Capacitors.md) · [HTML](capacitors/Capacitors.html) | 32 figures + local SVG | 150 | 36-question, 3 h, 245-mark INPhO-standard paper | complete |
| **current electricity** | [Current-electricity.md](current-electricity/Current-electricity.md) · [HTML](current-electricity/Current-electricity.html) | 26 figures + local SVG | 145 | 36-question, 3 h, 245-mark INPhO-standard paper | complete |
| **heat** | [Heat.md](heat/Heat.md) · [HTML](heat/Heat.html) | 24 figures + map SVG | 48 | 10-question written gauntlet | complete |
| **thermodynamics** | [Thermodynamics.md](thermodynamics/Thermodynamics.md) · [HTML](thermodynamics/Thermodynamics.html) | 34 figures + map SVG | 127 | 36-question, 3 h, 245-mark INPhO-standard paper | complete |
| **geometrical optics** | [Geometrical-optics.md](geometrical-optics/Geometrical-optics.md) · [HTML](geometrical-optics/Geometrical-optics.html) | 46 figures + local SVG | 152 | 36-question, 3 h, 143-mark INPhO-standard paper | complete |
| **wave optics** | [Wave-optics.md](wave-optics/Wave-optics.md) · [HTML](wave-optics/Wave-optics.html) | 27 figures + local SVG | 169 | 36-question, 3 h, 143-mark INPhO-standard paper | complete |
| rotational mechanics | — | — | — | — | planned — claim it |

The cross-topic progression and the Cengage → JEE → Olympiad coverage audit are in **[CURRICULUM.md](CURRICULUM.md)**. `topics.json` remains the checked registry for the interactive HTML editions; `tools/check_all.py` still validates their original markup, equations, figures and question/solution counts.

## Read it

```bash
git clone https://github.com/SurajGupta2009/Physics_JEEAD-OLYMPIAD_notes
cd Physics_JEEAD-OLYMPIAD_notes
less thermodynamics/Thermodynamics.md       # or open any *.md file in an editor
```

Every Markdown file keeps the original reading order: orientation → prerequisites → syllabus/Cengage map → theory → worked questions → playbook → paper/gauntlet → solutions → formula sheet. `<details>` blocks keep solutions collapsible on GitHub and in many Markdown viewers. Every diagram is a local `assets/figures/*.svg` file with its own styles, arrowheads, alt text and caption; there are no external image links.

The HTML edition is still available when you want theme switching, progress ticks, a generated TOC, or **Print / save as PDF**. It remains fully offline and is not required to read the Markdown.

## How a note-set is put together

```
capacitors/
├── Capacitors.md             portable reading copy: theory, math, questions and diagram links
├── Capacitors.html           interactive/offline edition of the same consolidated note
├── README.md                 topic scope, coverage notes and editing guidance
├── assets/
│   ├── figures/              standalone SVG diagrams used by the Markdown edition
│   ├── notes.css              HTML design system and print styles
│   ├── tex.js                 HTML edition's dependency-free math renderer
│   ├── notes.js               HTML TOC, theme, progress and navigation
│   └── pages.js               generated HTML navigation
└── tools/
    ├── check.py               HTML markup, math, links, figures and solutions gate
    ├── mathfix.py             idempotent HTML authoring normaliser
    ├── setpages.py            regenerate / check HTML navigation
    └── test-tex.js             HTML renderer unit tests
```

The Markdown exporter is [tools/html_to_markdown.py](tools/html_to_markdown.py). It is dependency-free and deterministic: rerunning it refreshes each `*.md` file and its local SVGs from the corresponding HTML note. The full HTML contract is [STRUCTURE.md](STRUCTURE.md); workflow and authoring conventions are [CONTRIBUTING.md](CONTRIBUTING.md).

## Check it

```bash
python3 tools/html_to_markdown.py    # refresh all six Markdown editions and SVG diagrams
python3 tools/check_all.py           # validate the original interactive editions
python3 tools/check_all.py --quick   # skip the Node renderer tests
```

The conversion is intentionally additive: the HTML files remain the source of truth for interactive behaviour, while the generated Markdown is the portable distribution format. A clean run should report six Markdown files and 189 chapter figures (plus the two expandable-map SVGs).

Optional CI: [`tools/ci/qa.yml`](tools/ci/qa.yml) runs the HTML gate as a GitHub Action. Install it with `mkdir -p .github/workflows && cp tools/ci/qa.yml .github/workflows/` if your checkout has workflow permissions.

## Adding your own note-set

```bash
python3 tools/new_topic.py thermodynamics --title "Thermodynamics" \\
        --chapters "01-temperature-and-zeroth-law,02-first-law,03-kinetic-theory"
```

The scaffold is still HTML-first because the interactive edition is the validated source; after writing a note, run `python3 tools/html_to_markdown.py` to publish its Markdown counterpart. See [CONTRIBUTING.md](CONTRIBUTING.md) for the content bar and [STRUCTURE.md](STRUCTURE.md) for the layout contract.

## The teaching contract

* **Reasoning for every step.** A derivation that skips “why” is treated as unfinished, not concise.
* **Concepts before formulas, formulas before problems** — and every key formula states its validity condition or failure mode.
* **Questions are interleaved with theory**, each with a full solution, rather than being parked at the end.
* **Diagrams replace prose where geometry does the work** — the Markdown export uses accessible SVG assets and asserting captions.
* **Numbers are checkable**: every numerical answer is re-derivable by a limit or unit check, and the note says which.
* **The final paper or gauntlet is coverage-mapped** back to the theory so the Olympiad layer is an ordered extension, not a disconnected formula list.

## Licence

These are personal study notes; the repository carries no `LICENSE` file, so copyright stays with the repo owner. If you want to open it up, add a `LICENSE` (CC-BY-4.0 suits notes, MIT suits the JS/PY tooling) — that is the owner's call, not a contributor's.

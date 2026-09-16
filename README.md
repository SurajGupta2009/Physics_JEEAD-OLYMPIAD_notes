<div align="center">

![Physics notes banner](docs/hero.svg)

### Physics notes for JEE Advanced and the Olympiad track

Self-contained HTML note-sets. Each topic has one consolidated final HTML file. No CDN, no MathJax, no build step, no network — every file renders
from `file://`, prints to a clean PDF, and is validated by one command.

</div>

## Note-sets

| topic | chapters | figures | questions | paper | status |
|---|---|---|---|---|---|
| **[capacitors](capacitors/Capacitors.html)** | 1 final HTML | 32 inline SVG | 99 (63 in-chapter, each with a full solution, + 36 in the paper) | 3 h, 245 marks, INPhO standard | complete |
| **[current-electricity](current-electricity/Current-electricity.html)** | 1 final HTML | 25 inline SVG | 143 (71 in-chapter, each with a full solution, + 36 in the paper + 36 mirrored in the solutions file) | 3 h, 245 marks, INPhO standard | complete |
| **[heat](heat/Heat.html)** | 1 final HTML (expandable mind-map) | 24 inline SVG | 48 (38 in-chapter, each with a full solution, + 10-question written gauntlet) | open-book gauntlet | complete |
| **[thermodynamics](thermodynamics/Thermodynamics.html)** | 1 final HTML (expandable mind-map) | 34 inline SVG | 127 (55 in-chapter, each with a full solution, + 36 in the paper + 36 mirrored in the solutions section) | 3 h, 245 marks, INPhO standard | complete |
| **[geometrical-optics](geometrical-optics/Geometrical-optics.html)** | 1 final HTML (12 parts) | 46 inline SVG | 152 (80 in-chapter, each with a full solution, + a 36-question paper with 36 worked solutions) | 3 h, 143 marks, INPhO standard | complete |
| **[wave-optics](wave-optics/Wave-optics.html)** | 1 final HTML (12 parts) | 27 inline SVG | 169 (97 in-chapter, each with a full solution, + a 36-question paper with 36 worked solutions) | 3 h, 143 marks, INPhO standard | complete |
| rotational-mechanics | — | — | — | — | planned — claim it |

The table above is a summary of [`topics.json`](topics.json), which is a *checked* registry:
`tools/check_all.py` recomputes every count from the markup and fails if the registry or the
navigation disagrees with the files.

## Read it

```bash
git clone https://github.com/SurajGupta2009/Physics_JEEAD-OLYMPIAD_notes
cd Physics_JEEAD-OLYMPIAD_notes/capacitors
open index.html            # or: python3 -m http.server 8000  →  http://localhost:8000
```

Double-clicking a page works: theme, print, TOC and progress are all local
(`localStorage`), so the only reason to run a server is to browse several pages comfortably.
Every chapter has a **Print / save as PDF** button — the print stylesheet drops the navigation,
opens every collapsed solution, and the formula sheet is laid out for three A4 pages.

## How a note-set is put together

```
capacitors/
├── index.html                 front page: syllabus map, how to study, chapter cards with ticks
└── Capacitors.html             the complete topic: overview, theory, paper, solutions and formula sheet
├── README.md                  this topic only: what is in it, what is deliberately not covered
├── assets/
│   ├── notes.css              design tokens, callouts, figures, tables, print + dark mode
│   ├── tex.js                 the math renderer: a LaTeX subset compiled to HTML (≈130 symbols)
│   ├── notes.js               TOC, scroll-spy, theme, progress, prev/next — holds no topic-specific text
│   └── pages.js               GENERATED: brand + page order + breadcrumbs, from the folder's files
└── tools/
    ├── mathfix.py             normalise common authoring slips (idempotent; run first)
    ├── setpages.py            regenerate / --check assets/pages.js
    ├── check.py               the per-topic gate: markup, math, links, anchors, figure/caption parity
    └── test-tex.js            30 unit tests for the renderer
```

Full specification: **[STRUCTURE.md](STRUCTURE.md)**. Workflow, conventions and the rules that let
several people (or several agents) write different chapters without colliding:
**[CONTRIBUTING.md](CONTRIBUTING.md)**. Chapter skeleton to copy:
**[_templates/chapter.html](_templates/chapter.html)**.

## Check it

```bash
python3 tools/check_all.py            # every topic: markup, math, links, renderer tests, registry
python3 tools/check_all.py --update   # recount topics.json after adding or renaming a page
python3 tools/check_all.py --quick    # skip the node tests
```

Optional CI: [`tools/ci/qa.yml`](tools/ci/qa.yml) runs the same gate as a GitHub Action. Install it with
`mkdir -p .github/workflows && cp tools/ci/qa.yml .github/workflows/` — it ships outside `.github/`
because GitHub will not let a bot push workflow files without the `workflows` permission. A green
check there means the notes still open, still render and still link to each other.

## Adding your own note-set

```bash
python3 tools/new_topic.py thermodynamics --title "Thermodynamics" \
        --chapters "01-temperature-and-zerosth,02-first-law,03-kinetic-theory"
```

It copies the assets and tools into a new self-contained folder, seeds `index.html`, `README.md`
and the chapters from `_templates/chapter.html`, registers the topic in `topics.json` with you as
owner, and runs the gate. From there it is one file per chapter — see
[CONTRIBUTING.md](CONTRIBUTING.md) for the content bar each chapter is expected to meet.

## The teaching contract (what every chapter must do)

* **Reasoning for every step.** A derivation that skips "why" is treated as unfinished, not concise.
  `<div class="box why">` is where that sentence lives.
* **Concepts before formulas, formulas before problems** — and every boxed formula states the
  condition under which it fails.
* **Questions interleaved with the theory**, each with a collapsible full solution, not parked at
  the end of the chapter.
* **Diagrams over prose where geometry does the work** — inline SVG, caption asserts something
  ("Fig. 6.2 — the same curve for three different circuits"), it does not just name the objects.
* **Numbers you can check**: every numerical answer is re-derivable by a limit or a unit check, and
  the chapter says which.
* **A paper at the end** of every topic: 30+ questions, coverage-mapped back to the chapters, with a
  separate full-solutions file.

## Licence

These are personal study notes; the repository carries no `LICENSE` file, so copyright stays with
the repo owner. If you want to open it up, add a `LICENSE` (CC-BY-4.0 suits notes, MIT suits the
JS/PY tooling) — that is the owner's call, not a contributor's.

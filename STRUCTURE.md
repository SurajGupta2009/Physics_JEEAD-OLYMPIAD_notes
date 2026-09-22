# STRUCTURE — the layout contract

Normative: every rule below is either enforced by a tool or is what the tools assume. If you
disagree with a rule, change the rule *and* the tool in the same pull request — never work around it
in one file.

Reading order for a newcomer: this file (what the repo looks like), then
[CONTRIBUTING.md](CONTRIBUTING.md) (how to add to it), then the topic's own `README.md`.

## 0. Portable Markdown distribution

Each consolidated HTML note now has a same-named Markdown edition beside it: for example,
`capacitors/Capacitors.md`. The Markdown files are the portable reading copies; they preserve the
HTML reading order, stable section anchors, `$...$` / `$$...$$` mathematics, `<details>` solutions,
and captions. Every source diagram is also exported as a standalone local SVG under that topic's
`assets/figures/` directory. `tools/html_to_markdown.py` regenerates these files without external
dependencies.

The HTML files and the rest of the contract below remain intentionally unchanged: they are the
interactive/offline editions and are still what `tools/check_all.py` validates. Markdown conversion
is additive, so a reader can choose GitHub/editor reading or the local HTML TOC/theme/print view.
The cross-topic order and the Cengage-to-Olympiad audit live in [CURRICULUM.md](CURRICULUM.md).

**Markdown-first work packages:** `plan.md` also permits a topic whose authoritative entry is
`<Topic-Slug>.md`, without a parallel HTML edition. Register it with `format: markdown` and an
`.md` entry. Its self-contained `tools/check.py` is required by the root gate; registry counts
come only from that entry (C-numbered checks, E-numbered exemplars, Q-numbered paper questions,
local SVG links and dollar-delimited math). Generated print extracts are not counted twice.
`words` counts whitespace-separated source tokens, `display_formulas` counts display blocks,
and `bytes_markdown` records source size; `bytes_html` is zero. Legacy HTML counts remain unchanged.

---

## 1. The three ideas everything follows from

1. **A topic is a folder, and the folder is a whole site.** `capacitors/` carries its own
   `assets/` and `tools/`, so it renders, prints and validates with no dependency on any other
   folder and with no network. Two topics never share a stylesheet, a script or a build.
2. **A chapter is one file.** `NN-slug.html`. Nobody edits your file; you edit nobody else's.
   Everything shared between chapters (navigation, breadcrumbs, progress) is *derived* from the
   files, so it cannot go stale and cannot conflict.
3. **The gate is one command.** `python3 tools/check_all.py` from the repo root. If it is green,
   every page opens, every formula renders, every link resolves, every figure has a caption, every
   question has an answer, and the registry matches the files.

## 2. Repository layout

```
.
├── README.md                 front page: what exists, how to read it, the teaching contract
├── STRUCTURE.md              this file
├── CONTRIBUTING.md           workflow + how to work in parallel
├── topics.json               registry of note-sets: paths, status, owner, mechanical counts
├── .gitignore                scratch and exports stay out
├── docs/
│   └── hero.svg              the banner in README.md (SVG, no binaries in this repo)
├── _templates/
│   └── chapter.html          copy this to start a chapter; placeholders are marked {{LIKE_THIS}}
├── tools/
│   ├── check_all.py          repo-wide gate + registry recount (--update, --quick)
│   ├── new_topic.py          scaffold a new topic folder from a donor topic
│   └── ci/qa.yml             the same gate as a GitHub Action (copy into .github/workflows/ to install)
└── capacitors/               a topic: index + 11 chapters + its own assets/ and tools/
```

Rules about the top level:

* Only topic folders sit at the root, and only if they are registered in `topics.json`.
  `.github/` is git-ignored: workflow files come from `tools/ci/` and are installed by the repo
  owner, so no contributor (human or agent) ever needs the `workflows` permission.
  `tools/check_all.py` fails if a folder with `assets/notes.css` is unregistered, or if a registered
  topic has no folder.
* `_templates/` and `docs/` are the only other allowed directories at the root (underscore =
  tooling, not content).
* Nothing binary. Diagrams are inline SVG in the HTML; the only image file is `docs/hero.svg`.

## 3. Topic anatomy

```
<topic>/
├── index.html                front page: how to study, badges, chapter cards with ticks
├── 01-<slug>.html … NN-<slug>.html
├── README.md                 this topic alone: file table, how to edit, "deliberately not covered"
├── assets/
│   ├── notes.css             design system: tokens, callouts, figures, tables, print, dark mode
│   ├── tex.js                math renderer (LaTeX subset → HTML); no dependencies
│   ├── notes.js              TOC, scroll-spy, theme, progress, prev/next, print, expand-all
│   └── pages.js              GENERATED by tools/setpages.py — brand, localStorage prefix, page order
└── tools/
    ├── mathfix.py            idempotent normaliser for authoring slips; run before check.py
    ├── setpages.py           writes / --checks assets/pages.js from the folder's own files
    ├── check.py              the topic gate (see §8)
    └── test-tex.js           unit tests for the renderer (node tools/test-tex.js)
```

**Self-containment is the point.** A topic folder copied anywhere — a USB stick, a phone, a
`file://` tab — must still work. That is why there is no shared root `assets/`, no npm manifest, and
no CDN reference anywhere. The cost (a duplicated CSS/JS per topic, ~40 KB) is paid on purpose;
`tools/new_topic.py` copies it for you.

## 4. Naming

| thing | rule | example |
|---|---|---|
| topic folder | lowercase, kebab, singular subject | `capacitors`, `rotational-mechanics` |
| chapter file | `NN-slug.html`, `NN` zero-padded, gaps allowed | `06-networks-and-transients.html` |
| section heading | `<h2>NN.k Title</h2>`, contiguous within a chapter | `6.3` |
| display equation | `<div class="eqd" data-tag="NN.k">`, add class `key` for a result worth memorising | `data-tag="6.4"` |
| figure | `<figcaption><b>Fig. NN.k</b> — one sentence that asserts something</figcaption>` | `Fig. 6.2` |
| question | `<div class="q">` with `<span class="lab">Qn</span>`, numbered from 1 **per chapter** | `Q4` in ch 4 |
| worked example | `<div class="ex"><p class="exh">Worked example NN.k · Title</p>` | |
| chapter roles | `01…07` theory, `08` playbook, `09` paper, `10` solutions, `11` formula sheet | |

`index.html` is always first in navigation; `tools/setpages.py` sorts by the numeric prefix, so a
new chapter slots in by its name alone. To insert a chapter without renumbering, use a gap
(`04a-…` is not supported — renumber instead; see CONTRIBUTING §5 on renames).

## 5. Page contract (what every chapter file looks like)

```html
<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>NN · Short label — <Topic>, from basics to Olympiad</title>   <!-- pages.js reads this -->
<meta name="description" content="…">
<!-- only for an exam paper / solutions pair: -->
<meta name="solutions" content="external:10-olympiad-solutions.html">
<link rel="stylesheet" href="assets/notes.css">
<script src="assets/tex.js" defer></script>
<script src="assets/pages.js" defer></script>
<script src="assets/notes.js" defer></script>
</head>
<body>
<div class="shell">
<nav class="toc" id="toc" aria-label="Contents"><p class="lab">Contents · ch NN</p></nav>
<main>
<p class="meta" id="top">…badges…</p>
<h1>NN · Title</h1>
<p class="lead">…</p>
   … sections …
<h2>NN.5 Checkpoint</h2><ul class="chks">…</ul>
<p class="skip">Next: <a href="…">…</a></p>
</main>
</div>
</body>
</html>
```

* The three `<script>` tags, in that order, with `defer`. `pages.js` before `notes.js` is required
  (no ordering hazard: `defer` runs them in document order).
* No other `<script>`, no `<style>` block, no `<link>` beyond `assets/notes.css` — unless the page
  genuinely needs it, and then it is discussed in the PR.
* `notes.js` generates the TOC from `<h2>/<h3>`, gives them ids, builds prev/next from `pages.js`,
  and wires the theme/print/expand buttons. Do not duplicate any of that by hand.

## 6. Markup vocabulary

Callouts (each is `<div class="box VARIANT"><p class="bt">Title</p>…</div>`):

| variant | use it for | never use it for |
|---|---|---|
| `def` | a definition, stated in words then symbols | an aside |
| `why` | the reasoning the textbook omits — one step, justified | a formula dump |
| `thm` | a result worth memorising, with its condition of validity | anything you will not test |
| `trap` | the wrong answer students produce + the one-line reply | generic warnings |
| `insight` | a link to another chapter/topic, an order-of-magnitude view | new results |
| `histo` | measurement, history, why the idea exists | filler |

Questions and examples: `<div class="q">` → `<div class="hd">` (`<span class="lab">Q4</span>`, `<b>prompt</b>`,
`<span class="diff">JEE advanced</span>`) → `<div class="bd">` (body, `<ul class="opts">` for MCQ options with
`<li><b>A</b> …</li>`, then `<details class="sol"><summary>Solution</summary><div class="bd">…</div></details>`).
Tables are `<table class="tb">`, with `class="e"` on cells whose content is maths (right-aligned, maths font).
`<span class="ans">` marks a one-line answer strip. A chapter ends with a `<ul class="chks">` checkpoint list.

Figure vocabulary (all defined in `assets/notes.css`, so diagrams from different chapters look related):

| class | meaning |
|---|---|
| `.w` | the drawing's white/fill area |
| `.ln .ln2 .thinl` | wire, second wire (e.g. the return path), hairline |
| `.dim` | dashed muted dimension line (pairs with the `#dim` marker) |
| `.facc .fneg .fp .fn` | positive-plate fill, negative-plate fill, `+` and `−` glyphs |
| `.fld` | a field line / field vector |
| `.lbl`, `.lbl.sm`, `.lbl.md` | figure labels at three sizes; `.mtext` for words in figure space |
| `.mi`, `.mi.sm` | maths rendered *inside* the SVG (the same italic style as `<m>`) |
| `.eq0`, `.hi` | the zero/highlight state used to show "nothing happens here" and a highlighted region |

Arrowheads are markers injected once by `notes.js`: `marker-end="url(#ah)"` (foreground),
`#ahb` blue, `#ahr` red, `#ahg` green, `#aho` orange, `#dim` the plain dimension tip. Use those five;
do not draw a `<polygon>` arrowhead per figure.

## 7. Math contract

Math is written as a **LaTeX subset** and compiled by `assets/tex.js` at load time. It reads
`textContent`, so:

* no HTML tags inside `<m>…</m>` or `<div class="eqd">…</div>`;
* `<` must be written `&lt;` (`>` is fine);
* a math expression lives on **one line** (a newline inside it is an error);
* supported: `\frac \dfrac \tfrac \cfrac \binom \sqrt[n]{}`, `_ ^`, accents, `\vec \hat \dot \bar
  \hl \class`, `\text \boxed \underbrace \overbrace \operatorname \mathbb \mathbf`, `\xrightarrow[opt]{}`,
  `\left \right \big \Big`, ~130 symbols (including `\lesssim \therefore \xrightarrow \iint`), and the
  environments `cases aligned align gathered *matrix array`.
* unsupported on purpose: `\tag \label \lim \middle`, `\$\$`, MathML, `\begin{tikzpicture}`.

If a chapter genuinely needs a symbol, add it to `SYM` (or a command to `FUN`) in `assets/tex.js`,
append a unit test to `tools/test-tex.js`, and nothing else needs to change: `tools/check.py` reads
the supported-command list **out of `tex.js`**, so the validator follows the renderer.

`python3 tools/mathfix.py` fixes the mechanical slips that this contract makes easy (unclosed `<m>`,
`<m=` → `<m>`, spacing macros) and is idempotent. Run it before `check.py`, and never as a
repo-wide reformatting tool.

## 8. What the tools enforce

| check | tool |
|---|---|
| HTML tag balance, including inside `<svg>`; nothing unclosed at EOF | `tools/check.py` |
| `<m>…</m>` balance; no raw `<` or newline inside math; no stray `\)`/`\]`/`$$`/MathML | `tools/check.py` |
| every `\command` in the page is implemented by `tex.js` | `tools/check.py` |
| only supported environments (`cases/aligned/align/*matrix/array/gathered`) | `tools/check.py` |
| internal links point at real files; `#anchors` resolve; assets exist | `tools/check.py` |
| `figure class="fig"` count == `figcaption` count | `tools/check.py` |
| every question has a `<details class="sol">` **or** the page declares `<meta name="solutions" content="external:FILE">` (a paper) / `"inline"` (the solutions file), and that FILE exists | `tools/check.py` |
| `assets/pages.js` matches the folder's files and titles | `tools/setpages.py --check` |
| renderer unit tests | `node tools/test-tex.js` |
| `topics.json` counts and page list match the files; every topic folder is registered; every topic has an `owner` | `tools/check_all.py` |
| no unfilled `{{placeholders}}` in any committed page | `tools/ci/qa.yml`, once installed |

The gate deliberately does **not** check prose quality, physics correctness or figure aesthetics.
Those are the review (CONTRIBUTING §6): a validator that checks markup keeps the machine work away
from the reader, and human review keeps the teaching honest.

## 9. `topics.json` — the registry

```json
{ "schema": 1, "conventions": { … prose rules … },
  "topics": [ {
      "slug": "capacitors",
      "title": "…",
      "status": "complete | in-progress | planned",
      "owner": "who is writing it — the coordination field",
      "entry": "capacitors/index.html",
      "exam": ["JEE Advanced", "INPhO", …],
      "pages": ["index.html", "01-…"],
      "figures": 32, "questions": 135, "solutions": 64,
      "math_spans": 3442, "bytes_html": 553038,
      "paper": { "questions": 36, "sections": 4, "marks": 245, "minutes": 180, "file": "09-….html" },
      "deliberately_not_covered": [ … ],
      "next_candidates": [ … ]
  } ] }
```

* `pages`, `figures`, `questions`, `solutions`, `math_spans`, `bytes_html` are **mechanical
  counts** — recompute with `python3 tools/check_all.py --update`, never hand-edit. `questions`
  counts `<div class="q">` blocks, so a solutions file that mirrors the paper counts twice; that is
  intentional (it is a markup census, not a claim).
* `status: planned` with `owner: null` is an open invitation. Setting `owner` **is** the claim;
  unclaimed work must not be edited by someone else without opening an issue first.
* `deliberately_not_covered` is the anti-duplication field: read it before writing a chapter.
* `paper.marks` must equal the sum of the printed marks in the paper. The capacitors paper is
  `12×3 + 6×4 + 8×4 + 153 = 245` — an arithmetic slip here is exactly what a "total marks: 246"
  line does to a candidate's confidence, so recount it whenever you touch a marking scheme.

## 10. Print and export

`assets/notes.css` has a dedicated `@media print` block: the top bar, TOC and pagenav disappear,
`body` drops to 10.6 pt, every `.ex/.q/figure/.box` is `break-inside: avoid`, and collapsed
solutions are force-opened. Two consequences for authors:

* a question's solution must live *inside* the question (or on the declared solutions page), so the
  printed version is self-contained;
* the formula sheet uses `.sheet` + `.pg` blocks (two-column grid, `break-after: page`) so it comes
  out as three A4 pages. If you add a second reference page, reuse `.sheet` rather than inventing a
  new print layout.

GitHub renders the HTML as source, not as a page. To show a reviewer the real thing, print to PDF
locally (or paste the folder into a gist with a raw viewer) — do not commit the PDF: `*.pdf` is
ignored on purpose.

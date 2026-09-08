# CONTRIBUTING — writing notes here, alone or in parallel

Everything about the layout is specified in [STRUCTURE.md](STRUCTURE.md); this file is the
workflow. Read §1–§4 to write one chapter; read §5–§7 before working next to someone (or
something) else who is writing a chapter at the same time.

## 1. The loop

```bash
git switch -c capacitors/ch12-noise            # <topic>/chNN-<slug>
cp _templates/chapter.html capacitors/12-noise.html   # or tools/new_topic.py for a whole topic
#    … fill it in …
cd capacitors
python3 tools/mathfix.py                 # normalise slips (idempotent, always safe)
python3 tools/setpages.py                # teach the folder that a 12th page exists
python3 tools/check.py                   # ALL GOOD
cd .. && python3 tools/check_all.py      # + registry counts, + renderer tests
git commit
```

Then add one card to `capacitors/index.html` (the chapter list) and, if the chapter is a big idea,
one line to its `README.md`. That is the whole choreography; nothing else in the repo needs to know
your chapter exists.

## 2. Claim your work first

`topics.json` is the coordination primitive. Before writing:

* new topic → run `tools/new_topic.py <slug> …`, which registers it with `owner: <you>`;
* new chapter in an existing topic → if a `next_candidates` entry exists for it, add your name to
  that topic's `README.md` chapter line in the same commit as your first draft, so the claim and the
  work land together;
* `status: planned, owner: null` → claim it by setting `owner`; do not write into a topic whose
  `owner` is somebody else without agreeing first.

One commit that only touches `topics.json`/`README.md` is a fine pull request on its own.

## 3. The content bar (what a chapter must contain to be mergeable)

Minimum, per theory chapter:

| requirement | why |
|---|---|
| a `<p class="lead">` that says what the reader can *do* after the chapter | orientation, and it stops scope creep |
| every derivation step justified — a `<div class="box why">` wherever "and therefore" hides an assumption | this is the whole point of the repo |
| a condition of validity next to every boxed formula (`key`) | JEE and INPhO both test the boundary case |
| ≥ 4 inline-SVG figures, captions that assert something | geometry carries the argument here, not prose |
| ≥ 6 questions **inside** the flow of the chapter, each with a collapsible full solution | interleaved retrieval, not end-of-chapter exercise lists |
| at least one `.trap` box naming the mistake and the one-line reply | exam-durable knowledge |
| a summary "results to own" and a `chks` checkpoint | the reader needs to know when they are done |
| an order-of-magnitude or limit check on every numerical result | a number nobody estimated is a number nobody trusts |

Per topic, additionally: a **playbook** chapter (triage + traps + numbers to memorise), a **paper**
of 30+ questions with a coverage map back to each chapter, a separate **solutions** file with the
marks distributed per part, and a **formula sheet** laid out for 2–3 printed pages. `capacitors/`
is the worked example of that shape.

Voice: second person, declarative, no "it is easy to see", no hedging. Address the reader as
someone who will be handed a pen in a timed room.

## 4. Numbers, physics and arithmetic

This is where an otherwise good chapter dies. Standing rules, learned the hard way:

1. **Recompute every number you write**, on a calculator or in python, not in your head.
   (`√` and ÷ are the usual offenders.)
2. **Check a limit in the text itself** — "as `d→∞` this returns the isolated sphere, ✓" costs one
   line and catches most sign errors.
3. **Units in every formula substitution**, and state the assumptions (`air at STP`, `κ−1 = 5.9e-4`).
4. **Marking schemes must sum.** If you add, remove or re-mark a question in the paper, recompute the
   total and fix *both* the paper and the solutions file (`12×3 + 6×4 + 8×4 + 153 = 245`).
5. **Do not silently reuse a constant from another chapter** — cite the chapter/section, e.g. "the
   pull-in fold of §3.6". If the two disagree, the bug is yours to resolve, not the reader's.
6. No thinking-out-loud left in a page: `grep -n '\.\.\.\|? no:\|TODO\|FIXME'` on your file before
   committing. A question must be self-contained and solvable; an ellipsis is not a formula.

## 5. Working next to other writers (and other agents)

The design goal of §2–§5 of STRUCTURE.md is that parallel work never needs coordination beyond the
claim. The rules that make it true:

**Yours, only yours**

* `capacitors/NN-yourchapter.html` — one file, one author. Never edit another chapter's file, not
  even to fix a typo: put it in your PR description as `drive-by: <file>: <fix>` and let the owner
  (or a separate one-line PR) land it. Two people "just fixing a comma" is the classic lost work.

**Shared, and how to touch it**

| file | rule |
|---|---|
| `assets/pages.js` | generated. Never hand-edit; run `tools/setpages.py`. A conflict here is resolved by taking *neither* side and regenerating. |
| `assets/notes.css` | additive only. New class → new rule at the end of the relevant block, with a one-line comment saying which chapter uses it. Never redefine or repurpose an existing class, and never reformat the file (whitespace churn is what turns two additive edits into a conflict). |
| `assets/tex.js` | append to `SYM` / `FUN` / the skip-list, plus a test in `tools/test-tex.js`. Changing an existing command's behaviour is a repo-wide change: needs its own commit and a full re-render check. |
| `assets/notes.js` | hold no topic-specific text (brand and page order come from `pages.js`). Keep it that way, so two topics can share the copy without patching. |
| `index.html` | append your card at the **end** of the `<ol class="cards">` list. That makes simultaneous edits a trivial "keep both" merge. Order on the page follows `NN`, so a card's position is not load-bearing. |
| `<topic>/README.md` | one line per chapter in the file table; add yours at the end of the table. |
| `topics.json` | counts are regenerated (`--update`); `pages` likewise. Only `status`/`owner`/`next_candidates`/`deliberately_not_covered` are hand-written, and those are one-line edits — put them in their own commit so they can be cherry-picked if a conflict lands. |
| `tools/*` | a tool change that alters what is checked is a repo-wide change: separate commit, PR title prefixed `tools:`, and mention which new failures it introduces (there should be none, or you fix the pages in the same PR). |

**Never do**

* reformat, reorder or "tidy" files outside your chapter (including line wrapping in HTML);
* rename a committed `NN-slug.html` after another chapter links to it — if you must, do it in a
  dedicated commit whose only job is the rename plus `grep`-driven link updates, and re-run
  `setpages.py`;
* renumber another chapter's figures to make room for yours (numbers are per chapter, and gaps are
  allowed mid-draft but not at merge: `Fig. 6.1, 6.2, 6.3` with no hole);
* introduce a dependency, a CDN, a webfont, an `<img src="http…">`, or a PDF/PNG;
* commit a half-filled template — `{{placeholders}}` fail CI on purpose.

**Renumbering a whole chapter's figures/sections** (only if a merged draft genuinely needs it): do
it in one mechanical commit, list the old→new mapping in the message, and re-run `check.py` — the
figure/caption parity check plus the anchor check will find most broken references for you.

## 6. Review, conflicts, and merging

PR conventions:

* title `<topic>: chNN <what it adds>` (or `tools:`, `docs:`, `repo:` for infrastructure);
* one chapter per PR; a PR that adds a chapter *and* changes the validator gets asked to split;
* description template: what the chapter makes possible · which questions are new · drive-by fixes
  noticed elsewhere · `check_all.py` output · anything you deliberately left out (and where you
  recorded it).

What the reviewer checks (10 minutes, and it is the *only* content gate — no tool does this):

1. Is each "therefore" justified? Pick two derivations and read them as a hostile student.
2. Are the boxed formulas' validity conditions stated?
3. Recompute one number and try one limit.
4. Do the figures show what the caption claims? Is every symbol in the figure labelled?
5. Are the questions actually *questions* (answerable, unambiguous, not solvable by dimensional
   analysis alone)? Are the solutions complete, including the check?
6. Is anything duplicated from another chapter? If so, cut and cross-link.

Conflict recipe, in order: (a) `git checkout --theirs` for `pages.js`/`topics.json`, then
`python3 tools/setpages.py && python3 tools/check_all.py --update`; (b) for `index.html` and
`README.md` tables, keep both blocks; (c) for `notes.css`/`tex.js`, both sides are additive — keep
both, and if two classes collide in name, the *later* one renames (the file that renamed last owns
the name); (d) re-run the full gate. Never resolve a conflict by deleting a chapter's content.

## 7. If you are an AI agent working in this repo

The parallel-work assumptions above are written so that a fresh agent with no memory of the session
can start safely. Concretely, on your first turn:

1. `cat STRUCTURE.md && cat <topic>/README.md && python3 tools/check_all.py` — know the contract and
   the current state in one go. `check_all.py` failing means someone left the tree mid-edit; fix or
   report it before adding your own changes.
2. Read `topics.json`: your topic's `owner`, `status`, `pages`, `deliberately_not_covered`,
   `next_candidates`. Do not write a chapter that another agent owns.
3. Find whether your chapter is already half-written: `git log --oneline -- capacitors/NN-*.html`,
   `grep -c '{{' capacitors/NN-*.html`, `grep -n 'TODO\|FIXME'`. If it exists, continue it; do not
   rewrite it — the reasoning in the boxes is the expensive part and it is already reviewed work.
4. Work inside your file. When you need something from a shared file, take the minimal additive
   action (append a CSS rule, append a `SYM` entry + test, run `setpages.py`).
5. Before ending: `python3 tools/mathfix.py && python3 tools/setpages.py && python3 tools/check.py`
   inside the topic, then `python3 tools/check_all.py --update` at the root. Green means the commit
   is allowed; anything else means the work is not done, and the correct move is to commit the
   *progress* with a message saying what remains, not to relax a rule.
6. Do not "improve" formatting, prose or physics outside your scope, do not add libraries, and do
   not invent numbers: every figure and every value must be derivable from what is already in the
   chapter or from a cited constant.
7. Write the handover into the topic `README.md` (one line: what is done, what the next chapter must
   inherit) so the *next* agent does not re-derive your setup.

## 8. Definition of done

* [ ] `python3 tools/check_all.py` green from the repo root (includes the topic's `check.py`,
      `setpages.py --check` and the renderer tests).
* [ ] No `{{placeholders}}`, no `TODO`, no thinking-out-loud fragments, no unresolved `\ldots`
      standing in for a formula.
* [ ] Figures numbered contiguously, each with an asserting caption; every math span one-line and
      tag-free; every question with a solution panel (or a declared external solutions page).
* [ ] Content bar of §3 met (why-boxes, validity conditions, traps, checkpoint).
* [ ] Every number recomputed; every marking total summed; limits checked in-text.
* [ ] `topics.json` recounted, `index.html` card added, `README.md` table line added.
* [ ] Diff touches only your chapter file + the shared-file appends you needed, and `git diff`
      shows no reformatting of anyone else's lines.

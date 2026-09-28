# JEE Physics coverage and quality review — first pass

**Review date:** 2026-09-28  
**Scope:** repository inventory and structural checks; first-pass comparison with the official 2026 JEE Main and JEE Advanced Physics syllabi; targeted content/teaching-quality scan.  
**Status:** initial audit, not an independent line-by-line physics proofread. Keep findings open until the affected chapter passages and their linked problems/answers have been checked and corrected.

## 1. Are the JEE chapter notes present?

**At the chapter/topic level, yes:** the checked registry contains 31 topics, all marked `complete`, and every registered entry points to an existing note source. The JEE physics course is arranged through the core sequence from units and measurements through electronic devices. The registry also includes material beyond the JEE core (notably communication systems and special relativity) and gives many chapters an Olympiad extension.

The course spine and notes cover the major official subject areas: measurement; mechanics; properties of matter and fluids; thermal physics; oscillations and waves; electrostatics; current electricity; magnetism; induction and AC; electromagnetic waves; optics; modern physics; and electronic devices. This is a **topic-presence** finding, not a guarantee that every bullet in the exam syllabi has been taught adequately.

### Syllabus qualification: experimental skills need a dedicated audit/upgrade

The official JEE Main 2026 syllabus has a separate **Experimental Skills** unit with 18 named experiments/activities. The repo has substantial measurement material and relevant theory distributed among units, heat, sound, circuits, optics, and semiconductors, but the first-pass search did not find a clear, systematic experiment-by-experiment treatment. Several official practical details were not found under their expected names, including the pendulum amplitude-squared-versus-time activity, metre-scale mass by moments, detergent’s effect on surface tension, specific heat by mixtures, galvanometer half-deflection, the prism deviation-versus-incidence plot, and identification of common components. These may be partly described under different wording; verify each against the text before calling it absent. The JEE Advanced 2026 General section also explicitly lists experimental measurement/error skills and specific experiments.

**Action:** add a single practical/experimental-skills chapter or a clearly indexed section set, with apparatus and labelled setup diagrams, procedure, observation table, graph where relevant, uncertainty/error treatment, expected result, and common sources of error. Build a checklist directly from the official syllabi and mark each item `covered`, `partial`, or `missing` with links to the exact note section.

## 2. High-priority content-quality loopholes found

A repository-wide search for authoring residue found multiple worked solutions containing visible self-corrections, mutually contradictory intermediate answers, or a problem explicitly left unresolved. These are not merely stylistic: a student could learn the wrong result or lose trust in the worked solution. The project’s own `CONTRIBUTING.md` says thinking-out-loud fragments should not remain in published notes.

| Priority | Location | First-pass issue | Required review |
|---|---|---|---|
| **Blocker** | `centre-of-mass-momentum/Centre-of-mass-momentum.md:650` | Moving-wall collision’s worked solution first obtains `-7 m/s`, then changes the relative-velocity arithmetic and concludes `-17 m/s`; the separate `[!success] Check` instead says `+7 m/s`. With positive toward the wall, the correct relative post-collision velocity is `-12 m/s`, so the ball’s ground-frame velocity is `-17 m/s`; the check is wrong and the solution retains the discarded answer. | Re-derive in the wall frame, establish the positive direction and wall velocity, correct the problem statement/solution, then verify the keyed answer and marking scheme. |
| **Blocker** | `work-energy-power/Work-energy-power.md:1428` | Spring–incline return problem says the return motion is “getting complicated,” changes the energy equation mid-solution, and does not finish with a definite requested result. | Solve the complete sequence of outward/return motion and spring interaction or remove/rewrite the question; audit its answer key and marks. |
| **Resolved in this pass** | `units-measurements/Units-measurements.md` (OL7 and P33) | The oil-film examples had inconsistent length units and underdetermined molecular-volume assumptions. | Reworked both with consistent geometry and a stated molecular cross-section; the estimate is now explicitly model-dependent. |
| **High** | `motion-in-two-dimensions/Motion-in-two-dimensions.md:982` | Drag-projectile solution gives an infinite-time approximation, notices that impact occurs earlier, then leaves the requested range to numerical integration without providing it. | Supply a well-posed solvable approximation/numerical result and method, or label it explicitly as an extension and do not score it as a completed solution. |
| **High** | `kinematics-1d/Kinematics-1d.md:1428` | The prose gives a reason for the upward/downward phase comparison, calls that reason backwards, and then replaces it. | Keep only a checked derivation and explain the phase-time comparison cleanly. |
| **High** | `gravitation/Gravitation.md:534` | The Moon/Sun tidal comparison has a factor-of-1000 arithmetic error before a later correction in the same answer. | Recompute from the original values and delete the false calculation, not merely append the correction. |
| **High** | `special-relativity/Special-relativity.md:622` | Relativistic momentum calculation uses an incorrect squared-energy subtraction, then corrects the value in place. | Recalculate the result and verify units/rounding and the answer key. |
| **High** | `rotational-mechanics/Rotational-mechanics.md:1429` | The answer first concludes the rod never leaves the wall, then states the opposite. | Re-derive the initial acceleration/contact condition and resolve the contradiction. |

Additional instances are enumerated by searching for `Wait`, `Actually`, `Hmm`, `let me recompute`, and similar phrases in Markdown. The first mechanics chapter has now had a targeted correction pass: its contradictory scratchwork was removed, its error-propagation formulas were clarified, numerical examples were recalculated, and the Spaced Repetition plugin deck was enabled through the note tag. This search remains a triage method, not a complete defect detector. Continue the same review chapter by chapter and verify each final result independently.

## 3. Diagrams and visual teaching

The newer Obsidian-first chapters deliberately use Mermaid figures plus `DIAGRAM` briefs. A brief is an instruction for a future drawing, **not itself a rendered physics diagram**. Many chapters have six Mermaid figures but numerous diagram briefs; the mechanics pair `fluid-mechanics` and `elasticity` are explicitly text-only with briefs. This satisfies the repository’s current authoring convention, but it does not mean all apparatus, ray paths, free-body diagrams, circuit layouts, graphs, or experimental setups are actually illustrated for learners.

**Action:** prioritize real, labelled visuals for (1) experimental apparatus and readings, (2) force/constraint setups, (3) ray diagrams, (4) circuit configurations and polarity, (5) graphs used to infer a result, and (6) geometry needed by multi-step derivations. Add a visual QA checklist: axes and sign conventions, labels and units, limiting cases, and direct correspondence to the text/problem. Preserve the vault convention: committed SVGs or useful rendered Mermaid, not a pile of unresolved search prompts.

## 4. Teaching structure and practice

The repository has strong scaffolding—orientation, prerequisites, coverage maps, theory, examples, practice, traps, formula sheets and checkpoints—but a consistent scaffold cannot guarantee sound sequencing or finished solutions. The longest courses and older HTML/Markdown editions need particular review for whether prerequisites are introduced before use, whether examples increase in difficulty gradually, whether each practice item has a complete worked solution, and whether the exam-specific content is clearly separated from Olympiad enrichment.

**Action:** sample each topic against a common lesson rubric: prerequisite → intuition/model → definitions and conventions → derivation with assumptions → worked example → guided practice → independent JEE-level practice → extension (clearly tagged) → recap/checkpoint. Audit question statements, answer keys, marking totals and final numeric values as a linked unit. Prefer smaller, exam-pattern practice sets with fully checked solutions over inflated question counts.

## 5. Validation run and its limits

- `python3 tools/check_all.py` passes for all 31 registered topics.
- This confirms repository/registry consistency and each chapter’s configured structural gates; it does **not** prove syllabus completeness, all numerical answers, every derivation, or pedagogical quality.
- The external syllabus checklist used for this first pass is the official [JEE (Main) 2026 syllabus](https://jeemain.nta.nic.in/document/syllabus-2026/) and [JEE (Advanced) 2026 syllabus PDF](https://jeeadv.ac.in/documents/jee-advanced-2026-syllabus.pdf). Recheck against the exam year being prepared for because official syllabi can change.

## 6. Recommended order of work

1. Resolve the blocker contradictions/incomplete solutions in §2; scan every chapter for similar residue.
2. Complete a source-linked syllabus matrix, especially all 18 JEE Main Experimental Skills items and JEE Advanced experiment/error-analysis requirements.
3. Run a chapter-by-chapter derivation, assumptions, units, limiting-case, numerical-answer and marking-scheme audit.
4. Replace the highest-value unresolved diagram briefs with real labelled visuals, beginning with practicals and recurring JEE setups.
5. Have a physics teacher or subject expert independently review the corrected material before claiming full content verification.

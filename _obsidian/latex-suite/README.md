# LaTeX Suite — the vault's snippet set

**Loaded automatically.** `.obsidian/plugins/obsidian-latex-suite/data.json` points the plugin at
[`snippets.js`](snippets.js) in this folder (*Settings → LaTeX Suite → Load snippets from file or
folder*). The plugin evaluates that file as a JavaScript module, so it must stay a single
`export default [ … ]` array — this README is the human-readable half.

`snippets.js` = the plugin's **default set** (v1.13.3, MIT, kept verbatim so nothing is lost) **+ the
physics additions below**. Persisted notes always carry the expanded LaTeX (plan.md §1.3.1): snippets
only speed up typing, and no chapter depends on them.

## The default set — the ones you will use most

| type | get | | type | get |
|---|---|---|---|---|
| `mk` | `$ … $` inline maths | | `dm` | `$$ … $$` display block |
| `@a @b @g @d @e @l @m @p @s @t @w` | α β γ δ ε λ μ π σ θ ω (`@` + letter; capital for Γ Δ Λ Σ Θ Ω) | | `alpha`, `beta`, … | typed Greek names get their backslash |
| `x1`, `v0`, `xnn` | `x_{1}`, `v_{0}`, `x_{n}` | | `sq`, `2rt` | `\sqrt{}`, `\sqrt[2]{}` |
| `a/b` then `/` | `\frac{a}{b}` (auto-fraction) | | `//` | empty `\frac{}{}` |
| `Evec`, `ihat`, `xdot`, `xddot`, `xbar` | `\vec{E}`, `\hat{i}`, `\dot{x}`, `\ddot{x}`, `\bar{x}` | | `bf`, `rm`, `text` | `\mathbf{}`, `\mathrm{}`, `\text{}` |
| `ddt`, `par`, `pa xt` | `\frac{d}{dt}`, `\frac{\partial}{\partial}`, `\frac{\partial x}{\partial t}` | | `int`, `dint`, `oint`, `iint` | integrals (definite has limits) |
| `sum`, `prod`, `lim`, `ooo` | Σ Π lim ∞ | | `sin`, `cos`, `ln`, `exp` | get their backslash |
| `xx`, `cdot`, `+-`, `...` | × · ± … | | `>=`, `<=`, `!=`, `->`, `=>`, `prop`, `simm` | ≥ ≤ ≠ → ⇒ ∝ ∼ |
| `pmat`, `bmat`, `cases`, `align` | the environment, with `Tab` between cells | | `(`, `[`, `{` | auto-paired; `lr(` gives `\left( \right)` |
| `avg`, `norm`, `bra`, `ket` | ⟨ ⟩, ‖ ‖, ⟨·|, |·⟩ | | `Tab` | jump out of brackets / to the next tabstop |

## Physics additions (this vault)

**Maths mode**

| type | get | type | get |
|---|---|---|---|
| `eps` `ep0` `mu0` | `\varepsilon` `\varepsilon_0` `\mu_0` | `omg` `Omg` `hbar` | `\omega` `\Omega` `\hbar` |
| `apx` | `\approx` | `grad` `divv` `curl` `lap` | `\nabla` `\nabla\cdot` `\nabla\times` `\nabla^{2}` |
| `vrms` `irms` `Vrms` `vavg` | rms / average symbols | `oom` | `\sim 10^{ }` order of magnitude |
| `uu` | `\,\mathrm{ }` upright unit group | `ddx` `dvdx` `pdt` | `\frac{d}{dx}`, `v\frac{dv}{dx}`, `\frac{\partial\ }{\partial t}` |
| `bx` | `\boxed{ }` key result | `tx` | `\text{ }` |

**Text mode** — type at the start of a line; each expands to the vault's own callout / question idiom
(docs/obsidian-plugin-workflow.md §2–§3, plan.md §1.4):

| type | get |
|---|---|
| `;fig` | `> [!tip] FIGURE F… · …` callout with *Why / Data*, a ` ```mermaid ` block and the *Read* line |
| `;dia` | `> [!abstract] DIAGRAM D… · …` brief with *Show / Search* |
| `;why` `;val` `;chk` `;trap` `;ins` `;hand` | `[!info] Why` · `[!warning] Condition of validity` · `[!success] Check` · `[!danger] Trap` · `[!tip] Insight` · `[!quote] Hand-off` |
| `;sol` `;ans` | `<details><summary>Solution/Answer</summary> … </details>` with the blank lines the renderer needs |
| `;q` `;ex` `;ol` `;cc` | `#### Qn.` practice question · `### En —` worked exemplar · `### OLn —` Olympiad problem · `**Cn — concept check.**`, each with its collapsible solution |

## Editing the set

Append to the *PHYSICS VAULT* section at the end of `snippets.js`; keep triggers ≥ 3 characters
unless they are prefixed (`;`), because auto-expanding two-letter triggers fire inside longer
tokens (`om` would fire inside `mom`). After editing, the plugin reloads the file on save; a parse
error shows as a notice *"Failed to parse snippet file"* — check for a missing comma or an unescaped
backslash (`\\` in JS strings).

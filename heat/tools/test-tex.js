/* quick regression test for the mini math compiler:  node tools/test-tex.js */
const T = require("../assets/tex.js");

const cases = [
  ["\\mathcal E = \\frac{W}{q}", "\u2130"],
  ["\\mathcal{E}I = I^2R + I^2r", 'class="up b">ℰ'],
  ["C = \\frac{Q}{V}", "<i>C</i> ="],
  ["u = \\tfrac{1}{2}\\varepsilon_0 E^2", "frac"],
  ["\\vec{E} = -\\vec{\\nabla}V", 'class="vec"'],
  ["\\oint \\vec{E}\\cdot d\\vec{\\ell} = 0", "∮"],
  ["U=\\frac{Q^2}{2C}=\\frac{1}{2}CV^2", "<i>Q</i><sup>2</sup>"],
  ["\\begin{pmatrix} Q_1 \\\\ Q_2 \\end{pmatrix}", "<table>"],
  ["\\sqrt[3]{x} + \\sqrt{a^2+b^2}", 'class="idx"'],
  ["\\sum_{i=1}^{n}\\frac{1}{C_i}", "<sub><i>i</i>=1</sub>"],
  ["\\hat{n}, \\dot{q}, \\bar{V}, \\underline{a}, \\binom{n}{k}", 'class="binom"'],
  ["10\\ \\mu F \\ll 1\\ \\text{farad}", 'class="up">farad'],
  ["a > b \\neq c \\le d", "<i>a</i> &gt; <i>b</i>"],
  ["\\Delta U = U_f - U_i \\Rightarrow \\text{stable}", "⇒"],
  ["W = \\int_{0}^{Q} \\frac{q}{C}\\,dq", "∫"],
  ["\\class{hl}{x^2}", 'class="hl"'],
  ["\\begin{cases} \\frac{a}{b}, & x>0 \\\\ 0, & x\\le 0 \\end{cases}", 'class="brace"'],
  ["\\begin{aligned} A &= 1 \\\\ B &= 2 \\end{aligned}", 'class="alg2"'],
  ["C = \\frac{\\varepsilon_0 A}{d} \\quad [\\text{parallel plate}]", "parallel plate"],
  ["x_{\\max}^{2}", "<sub><span class=\"up\">max</span></sub><sup>2</sup>"],
];

let bad = 0;
for (const [src, want] of cases) {
  let out;
  try { out = T.tex(src); } catch (e) { console.log("THROW ", src, "\n   ", e.message); bad++; continue; }
  const okHtml = !/&lt;(span|table|tr|td|i|sup|sub)/.test(out);
  const has = out.indexOf(want) >= 0;
  if (!okHtml || !has) { bad++; console.log("FAIL  ", src, "\n  want:", want, "\n  got :", out); }
}
/* nested + pathological inputs */
const stress = [
  "\\frac{\\frac{a}{b}}{\\frac{c}{d}}",
  "\\begin{cases}\\begin{pmatrix}1&2\\\\3&4\\end{pmatrix}, & x \\\\ 0, & y\\end{cases}",
  "e^{-t/\\tau}\\left(1+\\frac{t}{\\tau}\\right)",
  "\\vec{F}_{12} = \\frac{1}{4\\pi\\epsilon_0}\\frac{q_1 q_2}{r^2}\\hat{r}_{12}",
  "C = 4\\pi\\varepsilon_0\\varepsilon_r\\frac{R_1R_2}{R_2-R_1}",
  "\\rho_b = -\\vec{\\nabla}\\cdot\\vec{P}, \\qquad \\sigma_b = \\vec{P}\\cdot\\hat{n}",
  "\\frac{1}{2}\\epsilon_0 E^2 = \\frac{1}{2}\\epsilon_0\\epsilon_r E^2 \\;\\text{J/m}^3",
  "n \\to \\infty \\Rightarrow C_{eq} \\to \\frac{1+\\sqrt{5}}{2}C",
  "",
  "\\left| \\frac{\\partial U}{\\partial x} \\right|_{Q}",
  "x & y \\\\ z",
  "\\unknowncmd{a}",
];
stress.forEach(s => { try { const o = T.tex(s); if (/&lt;(span|table|td)/.test(o)) { bad++; console.log("ESCAPED!! ", s, "\n  ", o); } } catch (e) { bad++; console.log("STROW ", s, e.message); } });

console.log(bad ? "\n" + bad + " FAILURES" : "\nall " + (cases.length + stress.length) + " tex tests passed");
process.exit(bad ? 1 : 0);

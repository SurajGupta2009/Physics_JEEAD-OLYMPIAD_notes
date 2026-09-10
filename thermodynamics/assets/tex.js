/* tex.js — a small LaTeX-subset compiler so these notes are fully self-contained
   (no MathJax / KaTeX / CDN: works offline, from file://, and prints correctly).

   Contents of  <m>…</m> , <div class="eqd">…</div> , <td class="e">…</td>
   are typeset as maths.  The source stays human-readable even if JS is off,
   which is why Greek letters and common operators can be written literally
   (ε₀, π, σ, ∫, ∝, ⇒) instead of \varepsilon_0 etc.

   Supports: \frac[dfrac,tfrac,cfrac] \binom \sqrt[n]{}  _  ^  {}
             \vec \hat \dot \bar/\overline \underline \text \mathrm \mathbf \textbf
             \begin{cases|aligned|align|gathered|array|matrix|pmatrix|bmatrix|vmatrix}
             &  \\   \left \right \big… \displaystyle (ignored)
             \, \: \; \ ! \quad \qquad \hl{…} \class{x}{…}
             ~80 symbol aliases (\times \propto \varepsilon \Omega \oint …)
   Typesetting rules: Latin letters and lower-case Greek are italic (quantities);
   digits, operators, upper-case Greek, \text{} and function names are upright. */
(function (global) {
  "use strict";

  var SYM = {
    times: "×", cdot: "·", div: "÷", pm: "±", mp: "∓", ast: "∗",
    approx: "≈", lesssim: "≲", gtrsim: "≳", ll2: "≺", equiv: "≡", neq: "≠", ne: "≠", le: "≤", leq: "≤", ge: "≥", geq: "≥",
    ll: "≪", gg: "≫", propto: "∝", sim: "∼", simeq: "≃", lesssim:"≲", gtrsim:"≳", cong: "≅",
    to: "→", rightarrow: "→", Rightarrow: "⇒", implies: "⟹", Leftarrow: "⇐",
    leftarrow: "←", leftrightarrow: "↔", Leftrightarrow: "⇔", mapsto: "↦", iff: "⇔",
    uparrow: "↑", downarrow: "↓", gtrless: "⋇", lesseqgtr: "⋚", rightleftharpoons: "⇌", leftrightharpoons: "⇋",
    infty: "∞", partial: "∂", nabla: "∇", forall: "∀", exists: "∃",
    in: "∈", notin: "∉", subset: "⊂", subseteq: "⊆", cup: "∪", cap: "∩", emptyset: "∅",
    langle: "⟨", rangle: "⟩", lvert: "|", rvert: "|", vert: "|", Vert: "‖",
    prime: "′", degree: "°", circ: "∘", angle: "∠",
    ldots: "…", cdots: "⋯", vdots: "⋮", ddots: "⋱", dots: "…",
    triangle: "△", square: "□", bullet: "•", diamond: "◇", star: "⋆",
    oplus: "⊕", ominus: "⊖", otimes: "⊗", perp: "⊥", parallel: "∥",
    wedge: "∧", vee: "∨", neg: "¬", lnot: "¬",
    int: "∫", iint: "∬", iiint: "∭", oint: "∮", sum: "∑", prod: "∏", lim: "lim",
    surd: "√",
    hbar: "ℏ", ell: "ℓ", Re: "ℜ", Im: "ℑ", aleph: "ℵ", wp: "℘",
    alpha: "α", beta: "β", gamma: "γ", Gamma: "Γ", delta: "δ", Delta: "Δ",
    epsilon: "ϵ", varepsilon: "ε", zeta: "ζ", eta: "η", theta: "θ", Theta: "Θ",
    vartheta: "ϑ", iota: "ι", kappa: "κ", lambda: "λ", Lambda: "Λ", mu: "μ", nu: "ν",
    xi: "ξ", Xi: "Ξ", pi: "π", Pi: "Π", varpi: "ϖ", rho: "ρ", varrho: "ϱ",
    sigma: "σ", Sigma: "Σ", varsigma: "ς", tau: "τ", upsilon: "υ",
    phi: "φ", Phi: "Φ", varphi: "ϕ", chi: "χ", psi: "ψ", Psi: "Ψ", omega: "ω", Omega: "Ω",
    Ohm: "Ω", ohm: "Ω", checkmark: "✓", Longleftrightarrow: "⟺", Longrightarrow: "⟹",Longrightarrow: "⟹", Llead: "⇐", star2: "✶", perp2: "⟂", ne2: "≠", hat2: "^", box_: "□", bullet2: "∙", div2: "⊘"
  };
  var SP = { ",": 1, ":": 1, ";": 2, " ": 1 };          /* 1 = thin, 2 = medium */
  var FUN = { ln: 1, log: 1, lg: 1, exp: 1, sin: 1, cos: 1, tan: 1, cot: 1, sec: 1, csc: 1,
    sinh: 1, cosh: 1, tanh: 1, coth: 1, arcsin: 1, arccos: 1, arctan: 1, arcosh: 1, artanh: 1,
    max: 1, min: 1, mod: 1, gcd: 1, deg: 1, arg: 1, sgn: 1, const: 1, det: 1, diag: 1,
    Re: 1, Im: 1, re: 1, im: 1, dim: 1, order: 1, resp: 1, const_: 1 };
  var NEG = "\u0001";                                     /* marker for \! */

  var BB = { N: "ℕ", Z: "ℤ", Q: "ℚ", R: "ℝ", C: "ℂ", P: "ℙ", H: "ℍ", E: "𝔼", F: "𝔽" };
  function bb(t) { var o = ""; for (var i = 0; i < t.length; i++) o += BB[t[i]] || t[i]; return esc2(o); }
  var CAL = { B:"\u212C", E:"\u2130", F:"\u2131", H:"\u210B", I:"\u2110", L:"\u2112", M:"\u2133",
    R:"\u211B", e:"\u212F", g:"\u210A", o:"\u2134" };
  function cal(t) { var o = ""; for (var i = 0; i < t.length; i++) o += CAL[t[i]] || t[i]; return esc2(o); }
  function glyph(ch) { return isVar(ch) ? "<i>" + esc(ch) + "</i>" : esc(ch); }
  function esc(c) { return c === "&" ? "&amp;" : c === "<" ? "&lt;" : c === ">" ? "&gt;" : c; }
  function esc2(t) { var o = ""; for (var i = 0; i < t.length; i++) o += esc(t[i]); return o; }
  function isVar(ch) {
    var o = ch.charCodeAt(0);
    return (o >= 65 && o <= 90) || (o >= 97 && o <= 122) ||
           (o >= 0x03b1 && o <= 0x03c9) || o === 0x00b5 || o === 0x03d1 || o === 0x03d5 || o === 0x03f0 || o === 0x03f5;
  }

  /* ---------------- brace-aware primitives ---------------- */
  function skipSp(s, i) { while (i < s.length && /\s/.test(s[i])) i++; return i; }
  function matchBrace(s, i) {
    var d = 0;
    for (var j = i; j < s.length; j++) {
      if (s[j] === "\\") { j++; continue; }
      if (s[j] === "{") d++;
      else if (s[j] === "}") { d--; if (!d) return j; }
    }
    return -1;
  }
  function argRaw(s, i) {
    i = skipSp(s, i);
    if (i >= s.length) return ["", i];
    if (s[i] === "{") { var e = matchBrace(s, i); if (e < 0) return [s.slice(i + 1), s.length]; return [s.slice(i + 1, e), e + 1]; }
    if (s[i] === "\\") { var m = /^[a-zA-Z]+/.exec(s.slice(i)); if (m) return [m[0], i + m[0].length]; return [s.slice(i, i + 2), i + 2]; }
    return [s[i], i + 1];
  }
  function optArg(s, i) {
    i = skipSp(s, i);
    if (s[i] !== "[") return [null, i];
    for (var j = i + 1, d = 1; j < s.length; j++) {
      if (s[j] === "[") d++; else if (s[j] === "]") { d--; if (!d) return [s.slice(i + 1, j), j + 1]; }
    }
    return [null, i];
  }
  function splitTop(s, sep) {
    var out = [], d = 0, start = 0;
    for (var i = 0; i < s.length; i++) {
      var k = s[i];
      if (k === "\\") {
        if (sep === "\\" && s[i + 1] === "\\") { if (!d) { out.push(s.slice(start, i)); start = i + 2; } i++; continue; }
        i++; continue;
      }
      if (k === "{") d++;
      else if (k === "}") d--;
      else if (!d && sep.length === 1 && k === sep) { out.push(s.slice(start, i)); start = i + 1; }
    }
    out.push(s.slice(start));
    return out;
  }

  /* ---------------- core ---------------- */
  var PH1 = "\u0002", PH2 = "\u0003";   /* placeholders: protect pre-rendered HTML from re-parsing */
  function build(s) {
    var st = [];
    var r = compile(expandEnvs(s, st));
    return resolve(r, st);
  }
  function resolve(html, st) {
    var re = new RegExp(PH1 + "(\\d+)" + PH2, "g"), guard = 0;
    while (re.test(html) && guard++ < 40) html = html.replace(re, function (_, i) { return st[+i] === undefined ? "" : st[+i]; });
    return html;
  }

  function compile(s) {
    var i = 0, nodes = [];
    function push(h) { if (h) nodes.push(h); }

    while (i < s.length) {
      var c = s[i];

      if (c === "\\") {
        if (s[i + 1] === "\\") { i += 2; push("<br>"); continue; }
        var m = /^[a-zA-Z]+/.exec(s.slice(i + 1));
        if (!m) {
          var lit = s[i + 1]; i += 2;
          if (lit === undefined) { push("\\"); continue; }
          if (SP[lit]) { push('<span class="sp"></span>'); continue; }
          if (lit === "!") { push(NEG); continue; }
          push(esc(lit));
          continue;
        }
        var cmd = m[0]; i += 1 + cmd.length;

        if (cmd === "frac" || cmd === "dfrac" || cmd === "tfrac" || cmd === "cfrac") {
          var a = argRaw(s, i); i = a[1]; var b = argRaw(s, i); i = b[1];
          push('<span class="frac"><span class="n">' + build(a[0]) + '</span><span class="d">' + build(b[0]) + "</span></span>"); continue;
        }
        if (cmd === "binom") {
          var bp = argRaw(s, i); i = bp[1]; var bq = argRaw(s, i); i = bq[1];
          push('<span class="binom"><span class="pr">(</span><span class="bi"><span class="bt">' + build(bp[0]) + '</span><span class="bb">' + build(bq[0]) + '</span></span><span class="pr">)</span></span>'); continue;
        }
        if (cmd === "sqrt") {
          var o = optArg(s, i); i = o[1]; var sa = argRaw(s, i); i = sa[1];
          push('<span class="sq">' + (o[0] ? '<span class="idx">' + build(o[0]) + "</span>" : "") + '<span class="rad">' + build(sa[0]) + "</span></span>"); continue;
        }
        if (cmd === "vec" || cmd === "overrightarrow") { var v = argRaw(s, i); i = v[1]; push('<span class="vec">' + build(v[0]) + "</span>"); continue; }
        if (cmd === "hat" || cmd === "widehat") { var h2 = argRaw(s, i); i = h2[1]; push('<span class="hatk">' + build(h2[0]) + "</span>"); continue; }
        if (cmd === "dot") { var d2 = argRaw(s, i); i = d2[1]; push('<span class="dotk">' + build(d2[0]) + "</span>"); continue; }
        if (cmd === "ddot") { var d3 = argRaw(s, i); i = d3[1]; push('<span class="dotk dd">' + build(d3[0]) + "</span>"); continue; }
        if (cmd === "bar" || cmd === "overline") { var b2 = argRaw(s, i); i = b2[1]; push('<span class="ovl">' + build(b2[0]) + "</span>"); continue; }
        if (cmd === "underline") { var u2 = argRaw(s, i); i = u2[1]; push('<span class="unl">' + build(u2[0]) + "</span>"); continue; }
        if (cmd === "text" || cmd === "textrm" || cmd === "mbox" || cmd === "textnormal" || cmd === "mathrm" || cmd === "operatorname") {
          var t2 = argRaw(s, i); i = t2[1]; push('<span class="up">' + esc2(t2[0].replace(/\s+/g, " ")) + "</span>"); continue;
        }
        if (cmd === "textbf" || cmd === "mathbf" || cmd === "bm" || cmd === "boldsymbol") {
          var t3 = argRaw(s, i); i = t3[1]; push('<span class="up b">' + esc2(t3[0].replace(/\s+/g, " ")) + "</span>"); continue;
        }
        if (cmd === "mathit") { var t4 = argRaw(s, i); i = t4[1]; push('<i>' + esc2(t4[0]) + "</i>"); continue; }
        if (cmd === "xrightarrow" || cmd === "xleftarrow") {
          var xo = optArg(s, i); i = xo[1]; var xa = argRaw(s, i); i = xa[1];
          var arw = cmd === "xrightarrow" ? "→" : "←";
          push('<span class="xar"><span class="xa">' + (xa[0] ? build(xa[0]) : "") + '</span><span class="xb">' +
               arw + '</span>' + (xo[0] ? '<span class="xc">' + build(xo[0]) + "</span>" : "") + "</span>"); continue;
        }
        if (cmd === "hl") { var h3 = argRaw(s, i); i = h3[1]; push('<span class="hl">' + build(h3[0]) + "</span>"); continue; }
        if (cmd === "boxed") { var b3 = argRaw(s, i); i = b3[1]; push('<span class="boxed">' + build(b3[0].replace(/^\\s*\\;/g, "").trim()) + "</span>"); continue; }
        if (cmd === "mathbb" || cmd === "mathds") { var b4 = argRaw(s, i); i = b4[1]; push('<span class="up b">' + bb(b4[0]) + "</span>"); continue; }
        if (cmd === "mathcal") { var c4 = argRaw(s, i); i = c4[1]; push('<span class="up b">' + cal(c4[0]) + "</span>"); continue; }
        if (cmd === "underbrace" || cmd === "overbrace") { var b5 = argRaw(s, i); i = b5[1]; push('<span class="ub">' + build(b5[0]) + "</span>"); continue; }
        if (cmd === "quad2") { push('<span class="qquad"></span>'); continue; }
        if (cmd === "class") { var c1 = argRaw(s, i); i = c1[1]; var c2 = argRaw(s, i); i = c2[1]; push('<span class="' + c1[0] + '">' + build(c2[0]) + "</span>"); continue; }
        if (cmd === "substack") { var s1 = argRaw(s, i); i = s1[1]; push('<span class="sst">' + splitTop(s1[0], "\\").map(function (r) { return "<span>" + build(r.trim()) + "</span>"; }).join("") + "</span>"); continue; }
        if (cmd === "left" || cmd === "right" || cmd === "bigl" || cmd === "bigr" || cmd === "Bigl" || cmd === "Bigr" ||
            cmd === "big" || cmd === "Big" || cmd === "bigg" || cmd === "Bigg" || cmd === "middle" ||
            cmd === "displaystyle" || cmd === "textstyle" || cmd === "limits" || cmd === "nolimits") continue;
        if (cmd === "quad") { push('<span class="quad"></span>'); continue; }
        if (cmd === "qquad") { push('<span class="qquad"></span>'); continue; }
        if (SP[cmd]) { push('<span class="sp"></span>'); continue; }
        if (cmd === " ") { push('<span class="sp"></span>'); continue; }
        if (SYM[cmd] !== undefined) { push(glyph(SYM[cmd])); continue; }
        if (FUN[cmd]) { push('<span class="up">' + cmd + "</span>"); continue; }
        push('<span class="up">' + esc(cmd) + "</span>");
        continue;
      }

      if (c === "{") {
        var e = matchBrace(s, i);
        if (e < 0) { i++; push("{"); continue; }
        push(build(s.slice(i + 1, e))); i = e + 1; continue;
      }
      if (c === "}") { i++; continue; }
      if (c === "&") { i++; push("&amp;"); continue; }
      if (c === "\n") { i++; push(" "); continue; }

      if (c === "_" || c === "^") {
        i++;
        var g = argRaw(s, i); i = g[1];
        var tag = c === "_" ? "sub" : "sup";
        var prev = nodes.length ? nodes.pop() : "";
        nodes.push(prev + "<" + tag + ">" + build(g[0]) + "</" + tag + ">");
        continue;
      }

      var j = i, run = "";
      while (j < s.length && "\\\u005f{}^&\n".indexOf(s[j]) < 0) { run += s[j]; j++; }
      i = j;
      push(texrun(run));
    }
    return nodes.join("");
  }

  /* italicise runs of letters, leave the rest upright */
  function texrun(r) {
    var out = "", buf = "", mode = "";
    function flush() { if (!buf) return; out += (mode === "i" ? "<i>" : "") + esc2(buf) + (mode === "i" ? "</i>" : ""); buf = ""; }
    for (var i = 0; i < r.length; i++) {
      var ch = r[i], md = isVar(ch) ? "i" : "t";
      if (md !== mode) { flush(); mode = md; }
      buf += ch;
    }
    flush();
    return out;
  }

  /* ---------------- environments ---------------- */
  var ENV = {
    cases: function (body) {
      var h = '<span class="cases"><span class="brace">{</span><table>';
      splitTop(body, "\\").forEach(function (r) {
        h += "<tr>" + splitTop(rowFix(r), "&").map(function (c, k) { return '<td class="c' + (k + 1) + '">' + build(c.trim()) + "</td>"; }).join("") + "</tr>";
      });
      return h + "</table></span>";
    },
    aligned: function (b) { return alignGrid(b, 1); },
    align: function (b) { return alignGrid(b, 1); },
    "align*": function (b) { return alignGrid(b, 1); },
    eqnarray: function (b) { return alignGrid(b, 1); },
    gathered: function (b) { return alignGrid(b, 0); },
    array: function (b) { return alignGrid(b, 1); },
    matrix: function (b) { return '<span class="matrix">' + grid(b) + "</span>"; },
    pmatrix: function (b) { return '<span class="matrix"><span class="br"></span>' + grid(b) + '<span class="br r"></span></span>'; },
    bmatrix: function (b) { return '<span class="matrix"><span class="br sq"></span>' + grid(b) + '<span class="br r sq"></span></span>'; },
    vmatrix: function (b) { return '<span class="matrix"><span class="bar2">|</span>' + grid(b) + '<span class="bar2">|</span></span>'; }
  };
  function alignGrid(body, right1) {
    var h = '<table class="alg2">';
    splitTop(body, "\\").forEach(function (r) {
      h += "<tr>" + splitTop(rowFix(r), "&").map(function (c, i) {
        return '<td class="' + (i === 0 ? (right1 ? "c1" : "c0") : "c2") + '">' + build(c.trim()) + "</td>";
      }).join("") + "</tr>";
    });
    return h + "</table>";
  }
  function grid(body) {
    var h = "<table>";
    splitTop(body, "\\").forEach(function (r) {
      h += "<tr>" + splitTop(rowFix(r), "&").map(function (c) { return "<td>" + build(c.trim()) + "</td>"; }).join("") + "</tr>";
    });
    return h + "</table>";
  }
  function findEnd(s, from, name) {
    var stop = "\\end{" + name + "}", depth = 0;
    for (var i = from; i < s.length; i++) {
      if (s.startsWith("\\begin{" + name + "}", i)) { depth++; i += name.length + 7; continue; }
      if (depth === 0 && s.startsWith(stop, i)) return i;
      if (depth > 0 && s.startsWith(stop, i)) { depth--; i += stop.length - 1; }
    }
    return -1;
  }
  function expandEnvs(s, st) {
    var re = /\\begin\{([a-zA-Z*]+)\}/g, out = "", last = 0, m;
    while ((m = re.exec(s))) {
      var name = m[1], start = re.lastIndex, e = findEnd(s, start, name);
      var body = s.slice(start, e < 0 ? s.length : e);
      if (body[0] === "[") { var q = body.indexOf("]"); if (q > -1 && q < 14) body = body.slice(q + 1); }
      var html = ENV[name] ? ENV[name](body) : build(body);
      st.push(html);
      out += s.slice(last, m.index) + PH1 + (st.length - 1) + PH2;
      last = e < 0 ? s.length : e + ("\\end{" + name + "}").length;
      re.lastIndex = last;
    }
    return out + s.slice(last);
  }
  /* drop LaTeX row-spacing like  \\[6pt]  at the start of a row */
  function rowFix(r) { return r.replace(/^\s*\\\[[^\]]*\]\s*/, "").trim(); }

  /* ---------------- entry points ---------------- */
  var cache = {};
  function tex(src) {
    src = String(src);
    if (cache[src] !== undefined) return cache[src];
    var r = build(src.trim());
    r = r.split(NEG).join('<span class="ng"></span>');
    cache[src] = r;
    return r;
  }
  var SELECTORS = "m,.eqd,td.e,th.e,.mathx";
  function render(root) {
    var els = (root || document).querySelectorAll(SELECTORS);
    for (var i = 0; i < els.length; i++) {
      var el = els[i];
      if (el.getAttribute("data-texed")) continue;
      el.innerHTML = tex(el.textContent);
      el.setAttribute("data-texed", "1");
      var tg = el.getAttribute("data-tag");
      if (tg && el.classList.contains("eqd")) el.insertAdjacentHTML("beforeend", '<span class="tag">' + tg + "</span>");
    }
  }

  global.TexHTML = { tex: tex, render: render, expandEnvs: expandEnvs };
  if (typeof document !== "undefined") {
    if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", function () { render(document); });
    else render(document);
  }
  if (typeof module !== "undefined" && module.exports) module.exports = global.TexHTML;
})(typeof globalThis !== "undefined" ? globalThis : this);

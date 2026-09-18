#!/usr/bin/env python3
"""Convert the repository's self-contained HTML notes to portable Markdown.

The HTML files remain the interactive/offline edition.  This exporter is deliberately
small and dependency-free: it turns the semantic blocks into Markdown, converts the
repository's <m>...</m> notation to GitHub/KaTeX math, and writes every inline SVG as
a standalone, styled SVG asset referenced by the Markdown file.

Usage:
    python3 tools/html_to_markdown.py
    python3 tools/html_to_markdown.py capacitors/Capacitors.html
"""
from __future__ import annotations

import argparse
import html
import re
import shutil
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable, Optional

ROOT = Path(__file__).resolve().parents[1]

DEFAULT_FILES = [
    ROOT / "capacitors/Capacitors.html",
    ROOT / "current-electricity/Current-electricity.html",
    ROOT / "geometrical-optics/Geometrical-optics.html",
    ROOT / "heat/Heat.html",
    ROOT / "thermodynamics/Thermodynamics.html",
    ROOT / "wave-optics/Wave-optics.html",
]

SKIP_TAGS = {"head", "style", "script", "noscript", "nav", "button"}
BLOCK_TAGS = {
    "address", "article", "aside", "blockquote", "div", "dl", "dt", "dd",
    "fieldset", "figcaption", "figure", "footer", "form", "h1", "h2", "h3",
    "h4", "h5", "h6", "header", "hr", "li", "main", "ol", "p", "pre",
    "section", "table", "tbody", "td", "tfoot", "th", "thead", "tr", "ul",
    "details", "summary",
}


def cls(node: "Node") -> set[str]:
    return set(node.attrs.get("class", "").split())


def attr(node: "Node", name: str, default: str = "") -> str:
    return node.attrs.get(name, default)


@dataclass
class Node:
    tag: str = "#root"
    attrs: dict[str, str] = field(default_factory=dict)
    children: list["Node | str"] = field(default_factory=list)

    def text(self) -> str:
        return "".join(x if isinstance(x, str) else x.text() for x in self.children)


class TreeParser(HTMLParser):
    """Enough HTML parsing for the validated, dependency-free notes."""

    VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.root = Node()
        self.stack = [self.root]
        self.skip_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, Optional[str]]]) -> None:
        tag = tag.lower()
        if self.skip_depth:
            if tag in SKIP_TAGS:
                self.skip_depth += 1
            return
        if tag in SKIP_TAGS:
            self.skip_depth = 1
            return
        node = Node(tag, {k: (v or "") for k, v in attrs})
        self.stack[-1].children.append(node)
        if tag not in self.VOID:
            self.stack.append(node)

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, Optional[str]]]) -> None:
        if self.skip_depth:
            return
        node = Node(tag.lower(), {k: (v or "") for k, v in attrs})
        self.stack[-1].children.append(node)

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if self.skip_depth:
            if tag in SKIP_TAGS:
                self.skip_depth -= 1
            return
        # The source is checked HTML, but tolerate an omitted optional close tag.
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == tag:
                del self.stack[i:]
                return

    def handle_data(self, data: str) -> None:
        if not self.skip_depth:
            self.stack[-1].children.append(data)

    def handle_comment(self, data: str) -> None:
        # Comments are implementation notes, not part of the study notes.
        return


SVG_STYLE = r"""<style>
:root { --panel:#ffffff; --fg:#1c1c1a; --muted:#5f5c54; --accent:#1f5fa8;
  --pos:#0b7a4b; --neg:#b3261e; --amber:#8a5a00; --violet:#6b3fa0; }
.w { fill:var(--panel); }
.ln { stroke:var(--fg); stroke-width:1.6; fill:none; stroke-linecap:round; stroke-linejoin:round; }
.ln2 { stroke:var(--fg); stroke-width:2.6; fill:none; stroke-linecap:round; }
.thinl { stroke:var(--muted); stroke-width:1; fill:none; stroke-dasharray:4 3; stroke-linecap:round; }
.acc { stroke:var(--accent); stroke-width:1.8; fill:none; }
.facc { fill:var(--accent); opacity:.14; stroke:var(--accent); stroke-width:1.4; }
.fneg { fill:var(--neg); opacity:.13; stroke:var(--neg); stroke-width:1.4; }
.fp { fill:#edf4fb; stroke:var(--accent); stroke-width:1.6; }
.fn { fill:#fbeeed; stroke:var(--neg); stroke-width:1.6; }
.fld { stroke:var(--accent); stroke-width:1.4; fill:none; opacity:.85; }
.lbl { font-family:Arial,sans-serif; font-size:13px; fill:var(--fg); }
.lbl.sm { font-size:11px; fill:var(--muted); }
.lbl.md { font-size:12px; }
.mi { font-family:Georgia,serif; font-style:italic; font-size:14px; fill:var(--fg); }
.mi.sm { font-size:11.5px; fill:var(--muted); }
.eq0 { fill:none; stroke:var(--muted); stroke-width:1; stroke-dasharray:2 4; }
.mtext { font-family:Georgia,serif; font-size:13px; fill:var(--fg); }
.hi { fill:var(--amber); opacity:.16; stroke:var(--amber); stroke-width:1.3; }
.pos { fill:var(--pos); } .negc { fill:var(--neg); }
line.mk,path.mk { stroke:var(--fg); stroke-width:1.4; }
</style>"""

SVG_DEFS = r"""<defs>
<marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,1 L9.6,5 L0,9 Z" fill="var(--fg)"/></marker>
<marker id="ahb" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,1 L9.6,5 L0,9 Z" fill="var(--accent)"/></marker>
<marker id="ahr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,1 L9.6,5 L0,9 Z" fill="var(--neg)"/></marker>
<marker id="ahg" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,1 L9.6,5 L0,9 Z" fill="var(--pos)"/></marker>
<marker id="aho" viewBox="0 0 10 10" refX="8.6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M1,1.4 L8.6,5 L1,8.6" fill="none" stroke="var(--fg)" stroke-width="1.8"/></marker>
<marker id="dim" viewBox="0 0 8 12" refX="4" refY="6" markerWidth="7" markerHeight="10" orient="auto"><path d="M4,0 L4,12" stroke="var(--muted)" stroke-width="1.1"/></marker>
</defs>"""


def xml_escape(text: str) -> str:
    return html.escape(text, quote=False)


SVG_TAG_CASE = {
    "lineargradient": "linearGradient",
    "radialgradient": "radialGradient",
    "clippath": "clipPath",
    "textpath": "textPath",
}
SVG_ATTR_CASE = {"viewbox": "viewBox"}


def serialize(node: Node) -> str:
    if node.tag == "#root":
        return "".join(serialize(x) if isinstance(x, Node) else xml_escape(x) for x in node.children)
    if node.tag in {"br"}:
        return "<br/>"
    tag = SVG_TAG_CASE.get(node.tag, node.tag)
    attrs = "".join(f' {SVG_ATTR_CASE.get(k, k)}="{html.escape(v, quote=True)}"' for k, v in node.attrs.items())
    body = "".join(serialize(x) if isinstance(x, Node) else xml_escape(x) for x in node.children)
    return f"<{tag}{attrs}>{body}</{tag}>"


def standalone_svg(svg: Node) -> str:
    attrs = "".join(f' {SVG_ATTR_CASE.get(k, k)}="{html.escape(v, quote=True)}"' for k, v in svg.attrs.items())
    # An SVG file needs its own namespace and the marker definitions that notes.js
    # injects into the HTML document at runtime.
    if "xmlns" not in svg.attrs:
        attrs += ' xmlns="http://www.w3.org/2000/svg"'
    body = "".join(serialize(x) if isinstance(x, Node) else xml_escape(x) for x in svg.children)
    body = re.sub(r"[ \t]+(?=\n)", "", body).rstrip()
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<svg{attrs}>\n{SVG_STYLE}\n{SVG_DEFS}\n{body}\n</svg>\n'


def clean_space(text: str) -> str:
    text = text.replace("\xa0", " ")
    return re.sub(r"[ \t\r\n]+", " ", text).strip()


def math_text(text: str) -> str:
    # HTML entities are already decoded by HTMLParser. Keep TeX whitespace
    # commands intact and collapse only actual source newlines/spaces. A few
    # legacy spans contain a stray literal dollar before </m>; the Markdown
    # delimiters added by this exporter already provide the pair.
    value = re.sub(r"\s+", " ", text.replace("\xa0", " ")).strip()
    # A stray trailing backslash (a legacy authoring slip) would merge with the
    # $ delimiter this exporter appends and break the math in every renderer.
    value = value.rstrip("\\").strip()
    return value.strip("$").strip()


def escape_table_cell(text: str) -> str:
    text = re.sub(r"\n{2,}", "<br><br>", text.strip())
    text = text.replace("\n", "<br>")
    return text.replace("|", r"\|")


SUPERSCRIPT = {c: s for c, s in zip("0123456789-+/", "⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺⁄")}
SUPERSCRIPT["\u2212"] = "\u207b"  # the notes use the true minus sign in units
SUBSCRIPT = {c: s for c, s in zip("0123456789", "₀₁₂₃₄₅₆₇₈₉")}
SUBSCRIPT.update({"p": "ₚ", "P": "ₚ", "v": "ᵥ", "V": "ᵥ", "e": "ₑ", "i": "ᵢ", "o": "ₒ", "l": "ₗ", "j": "ⱼ", "h": "ᵪ"})


def to_ordinal(text: str, table: dict[str, str]) -> str:
    """Render a short unit exponent in Unicode; return "" when it cannot."""
    if not text:
        return ""
    return "".join(table.get(ch, "") for ch in text) if all(ch in table for ch in text) else ""


def plain_text(text: str) -> str:
    """Strip inline markup from an attribute like an image aria-label,
    keeping the words so the alt text stays plain, accessible text."""
    text = re.sub(r"</?(?:em|i|b|strong|sub|sup|m|var)\b[^>]*>", "", text)
    return re.sub(r"<[^>]+>", "", text)


class MarkdownRenderer:
    def __init__(self, topic_dir: Path) -> None:
        self.topic_dir = topic_dir
        self.asset_dir = topic_dir / "assets" / "figures"
        self.asset_dir.mkdir(parents=True, exist_ok=True)
        self.figures = 0
        self.heading_count = 0
        self.first_h1 = True
        self.anchor_ids: set[str] = set()

    def render_file(self, source: Path) -> str:
        parser = TreeParser()
        parser.feed(source.read_text(encoding="utf-8"))
        body = self.find_body(parser.root) or parser.root
        out = self.render_children(body).strip()
        # Avoid accidental four-space indented code blocks caused by the HTML's
        # visual indentation, while retaining intentional fenced code blocks.
        out = re.sub(r"\n{3,}", "\n\n", out)
        return out + "\n"

    def find_body(self, node: Node) -> Optional[Node]:
        if node.tag == "body":
            return node
        for child in node.children:
            if isinstance(child, Node):
                found = self.find_body(child)
                if found:
                    return found
        return None

    def id_anchor(self, node: Node) -> str:
        ident = attr(node, "id")
        if not ident or ident in self.anchor_ids:
            return ""
        self.anchor_ids.add(ident)
        return f'<a id="{html.escape(ident, quote=True)}"></a>\n\n'

    def render_children(self, node: Node) -> str:
        chunks: list[str] = []
        for child in node.children:
            if isinstance(child, str):
                if child.strip():
                    chunks.append(child)
                continue
            is_block = child.tag in BLOCK_TAGS
            rendered = self.render_block(child) if is_block else self.render_inline(child)
            if not rendered:
                continue
            if is_block:
                # HTML uses wrapper divs heavily. Give each block a Markdown
                # boundary so cards, solutions and paragraphs do not run into
                # each other when their wrapper has no text of its own.
                chunks.append(rendered.rstrip() + "\n\n")
            else:
                chunks.append(rendered)
        return "".join(chunks)

    def render_inline(self, node: Node | str) -> str:
        if isinstance(node, str):
            # A handful of legacy HTML paragraphs contain the literal two
            # characters "\\n" between words (the browser edition shows it
            # as an authoring glitch). It is prose outside <m>, so normalize it
            # here; TeX inside <m> is handled by the dedicated branch below.
            return re.sub(r"\s+", " ", node.replace("\\n", " "))
        tag = node.tag
        if tag in {"script", "style", "nav", "button"}:
            return ""
        if tag == "m" or tag == "var":
            val = math_text(node.text())
            return f"${val}$" if val else ""
        if tag in {"sup", "sub"}:
            content = clean_space(node.text())
            table = SUPERSCRIPT if tag == "sup" else SUBSCRIPT
            value = to_ordinal(content, table)
            # Unicode keeps the Markdown clean in every viewer; when the
            # exponent has no Unicode form, keep the (rare) HTML tag, which
            # GitHub and most renderers still typeset.
            return value if value else f"<{tag}>{content}</{tag}>"
        if tag == "br":
            return "\n"
        if tag == "a":
            label = self.render_inline_children(node).strip()
            href = attr(node, "href")
            if not href or href.startswith("javascript:"):
                return label
            # The HTML edition is a single document; links to its companion
            # index are clearer in the Markdown export as the local README.
            if href == "index.html":
                href = "README.md"
            return f"[{label}]({href})" if label else ""
        if tag in {"strong", "b"}:
            content = self.render_inline_children(node).strip()
            return f"**{content}**" if content else ""
        if tag in {"em", "i"}:
            content = self.render_inline_children(node).strip()
            return f"*{content}*" if content else ""
        if tag == "code" or "tt" in cls(node):
            content = clean_space(self.render_inline_children(node))
            return f"`{content}`" if content else ""
        if tag == "span":
            return self.render_inline_children(node)
        if tag == "img":
            src = attr(node, "src")
            alt = attr(node, "alt", "diagram")
            return f"![{alt}]({src})" if src else ""
        if tag == "hr":
            return "\n\n---\n\n"
        if tag == "svg":
            # SVG is consumed by its parent <figure>; if a loose one appears,
            # still export it rather than dropping a diagram.
            return self.export_svg(node)
        if tag in BLOCK_TAGS:
            return self.render_block(node)
        return self.render_inline_children(node)

    def render_inline_children(self, node: Node) -> str:
        return "".join(self.render_inline(x) if isinstance(x, (Node, str)) else "" for x in node.children)

    def render_block(self, node: Node) -> str:
        tag = node.tag
        anchor = self.id_anchor(node)
        if tag in {"script", "style", "nav", "button"}:
            return ""
        if tag in {"main", "article", "section", "header", "footer", "aside", "div", "address", "fieldset", "form"}:
            c = cls(node)
            if "topbar" in c or "toc" in c:
                return ""
            if "eqd" in c:
                return anchor + self.render_equation(node)
            if "q" in c:
                return anchor + self.render_question(node)
            if "ex" in c:
                return anchor + self.render_example(node)
            if "box" in c:
                return anchor + self.render_box(node)
            if "card" in c:
                return anchor + self.render_card(node)
            if "ans" in c:
                return anchor + self.render_answer(node)
            # Cards, maps and wrappers are semantic containers; their children
            # carry the useful Markdown structure.
            return anchor + self.render_children(node)
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            level = int(tag[1:])
            if tag == "h1":
                if self.first_h1:
                    mark = "#"
                    self.first_h1 = False
                else:
                    mark = "##"
            else:
                # h2/h3 in the HTML are section/subsection headings. Offset
                # them one level because the first course title is #.
                mark = "#" * min(level + 1, 6)
            title = clean_space(self.render_inline_children(node))
            return anchor + f"{mark} {title}\n\n" if title else anchor
        if tag == "p":
            c = cls(node)
            if "exh" in c:
                content = clean_space(self.render_inline_children(node))
                return anchor + (f"#### {content}\n\n" if content else "")
            if "meta" in c:
                content = clean_space(self.render_meta(node))
                return anchor + (f"_{content}_\n\n" if content else "")
            content = clean_space(self.render_inline_children(node))
            return anchor + (content + "\n\n" if content else "")
        if tag == "figure":
            return anchor + self.render_figure(node)
        if tag == "figcaption":
            return clean_space(self.render_inline_children(node))
        if tag == "table":
            return anchor + self.render_table(node)
        if tag in {"ul", "ol"}:
            return anchor + self.render_list(node)
        if tag == "li":
            return self.render_children(node).strip()
        if tag in {"blockquote"}:
            content = self.render_children(node).strip()
            return anchor + self.quote(content) + "\n\n" if content else ""
        if tag == "details":
            return anchor + self.render_details(node)
        if tag == "pre":
            return anchor + "\n```\n" + node.text().strip("\n") + "\n```\n\n"
        if tag == "hr":
            return anchor + "\n---\n\n"
        if tag == "tr":
            return self.render_children(node)
        if tag in {"td", "th", "thead", "tbody", "tfoot", "dt", "dd"}:
            return self.render_children(node)
        return anchor + self.render_children(node)

    def render_box(self, node: Node) -> str:
        title_node = next((x for x in node.children if isinstance(x, Node) and "bt" in cls(x)), None)
        title = clean_space(self.render_inline_children(title_node)) if title_node else "Note"
        parts = []
        for child in node.children:
            if child is title_node:
                continue
            parts.append(self.render_block(child) if isinstance(child, Node) and child.tag in BLOCK_TAGS else self.render_inline(child))
        body = "".join(parts).strip()
        content = f"**{title}**\n\n{body}" if body else f"**{title}**"
        return self.quote(content) + "\n\n"

    def render_meta(self, node: Node) -> str:
        # Badges are useful as a compact reading-level line, but their HTML
        # wrappers have no semantic value in Markdown.
        values = []
        for child in node.children:
            if isinstance(child, Node) and "badges" in cls(child):
                for item in child.children:
                    if isinstance(item, Node) and "b" in cls(item):
                        value = clean_space(item.text())
                        if value:
                            values.append(value)
        if values:
            return " · ".join(values)
        return clean_space(self.render_inline_children(node))

    def math_content(self, node: Node) -> str:
        """Get the TeX source inside a display equation without $ delimiters."""
        parts: list[str] = []
        for child in node.children:
            if isinstance(child, str):
                parts.append(child)
            elif child.tag in {"m", "var"}:
                parts.append(child.text())
            elif child.tag in {"br"}:
                parts.append("\\\\")
            elif child.tag in {"sub", "sup"}:
                parts.append(("_" if child.tag == "sub" else "^") + "{" + self.math_content(child) + "}")
            elif child.tag == "table":
                # Tables used in an equation are usually aligned derivations;
                # their text is still preferable to silently losing a line.
                parts.append(self.math_content(child))
            else:
                parts.append(self.math_content(child))
        value = re.sub(r"\s+", " ", "".join(parts)).strip()
        return value.rstrip("\\").strip("$").strip()

    def render_equation(self, node: Node) -> str:
        value = self.math_content(node)
        if not value:
            return ""
        tag = attr(node, "data-tag")
        # The prose cites numbered equations ("use (1.2)"), so the number has
        # to be visible in the Markdown edition. \tag{} is supported by every
        # KaTeX-based renderer (GitHub, Obsidian, VS Code) and prints cleanly;
        # it also keeps the equation content identical to the HTML edition.
        value = f"{value} \\tag{{{html.escape(tag, quote=False)}}}" if tag else value
        return "$$\n" + value + "\n$$\n\n"

    def render_card(self, node: Node) -> str:
        # The HTML index uses cards for navigation. A list preserves the same
        # order while remaining useful in plain-text Markdown viewers.
        text = clean_space(self.render_inline_children(node))
        text = re.sub(r"^→\s*", "", text)
        return f"- {text}\n\n" if text else ""

    def render_answer(self, node: Node) -> str:
        text = clean_space(self.render_inline_children(node))
        return f"> **Answer:** {text}\n\n" if text else ""

    def render_question(self, node: Node) -> str:
        hd = next((x for x in node.children if isinstance(x, Node) and "hd" in cls(x)), None)
        bd = next((x for x in node.children if isinstance(x, Node) and "bd" in cls(x)), None)
        if hd:
            lab = next((x for x in hd.children if isinstance(x, Node) and "lab" in cls(x)), None)
            prompt = next((x for x in hd.children if isinstance(x, Node) and x.tag in {"b", "strong"}), None)
            diff = next((x for x in hd.children if isinstance(x, Node) and "diff" in cls(x)), None)
            lab_text = clean_space(lab.text()) if lab else "Q"
            prompt_text = clean_space(self.render_inline_children(prompt)) if prompt else clean_space(self.render_inline_children(hd))
            diff_text = clean_space(diff.text()) if diff else ""
            heading = f"**{lab_text}** {prompt_text}"
            if diff_text:
                heading += f" _({diff_text})_"
        else:
            heading = "**Question**"
        body = self.render_children(bd).strip() if bd else ""
        result = f"### {heading}\n\n"
        if body:
            result += body + "\n\n"
        return result

    def render_example(self, node: Node) -> str:
        hd = next((x for x in node.children if isinstance(x, Node) and "hd" in cls(x)), None)
        bd = next((x for x in node.children if isinstance(x, Node) and "bd" in cls(x)), None)
        exh = next((x for x in node.children if isinstance(x, Node) and "exh" in cls(x)), None)
        heading = clean_space(self.render_inline_children(hd)) if hd else (clean_space(self.render_inline_children(exh)) if exh else "Worked example")
        if bd:
            body = self.render_children(bd).strip()
        else:
            body = "".join(
                self.render_block(x) if isinstance(x, Node) and x.tag in BLOCK_TAGS else self.render_inline(x)
                for x in node.children if x is not exh
            ).strip()
        return f"### {heading}\n\n" + (body + "\n\n" if body else "")

    def render_details(self, node: Node) -> str:
        summary = next((x for x in node.children if isinstance(x, Node) and x.tag == "summary"), None)
        if summary and "chap" in cls(node):
            bits = []
            for wanted in ("cno", "ctt", "cchip", "cst"):
                part = next((x for x in summary.children if isinstance(x, Node) and wanted in cls(x)), None)
                if part:
                    value = clean_space(part.text())
                    if value:
                        bits.append(value)
            title = " · ".join(bits) or "Chapter"
        else:
            title = clean_space(self.render_inline_children(summary)) if summary else "Details"
        body_parts = []
        for child in node.children:
            if child is summary:
                continue
            body_parts.append(self.render_block(child) if isinstance(child, Node) and child.tag in BLOCK_TAGS else self.render_inline(child))
        body = "".join(body_parts).strip()
        return f"<details>\n<summary>{title}</summary>\n\n{body}\n\n</details>\n\n"

    def render_list(self, node: Node) -> str:
        ordered = node.tag == "ol"
        lines: list[str] = []
        index = 1
        for child in node.children:
            if not isinstance(child, Node) or child.tag != "li":
                continue
            # A list item can contain a paragraph, nested list and details.
            rendered = self.render_children(child).strip()
            rendered = re.sub(r"\n{2,}", "\n", rendered)
            sublists = []
            # Keep nested lists as Markdown; indent their lines beneath item.
            marker = f"{index}. " if ordered else "- "
            index += 1
            if rendered:
                rlines = rendered.splitlines()
                lines.append(marker + rlines[0])
                lines.extend("  " + line for line in rlines[1:])
        return "\n".join(lines) + "\n\n" if lines else ""

    def render_table(self, node: Node) -> str:
        rows: list[tuple[bool, list[str]]] = []
        def walk(n: Node, in_head: bool = False) -> None:
            if n.tag == "thead":
                in_head = True
            if n.tag == "tr":
                cells = []
                for child in n.children:
                    if isinstance(child, Node) and child.tag in {"td", "th"}:
                        value = self.render_inline_children(child).strip()
                        cells.append(escape_table_cell(value))
                if cells:
                    rows.append((in_head or any(isinstance(x, Node) and x.tag == "th" for x in n.children), cells))
                return
            for child in n.children:
                if isinstance(child, Node):
                    walk(child, in_head)
        walk(node)
        if not rows:
            return ""
        width = max(len(cells) for _, cells in rows)
        normalized = [(head, cells + [""] * (width - len(cells))) for head, cells in rows]
        header_i = next((i for i, (head, _) in enumerate(normalized) if head), 0)
        header = normalized[header_i][1]
        data = [cells for i, (_, cells) in enumerate(normalized) if i != header_i]
        out = ["| " + " | ".join(header) + " |", "| " + " | ".join("---" for _ in header) + " |"]
        out.extend("| " + " | ".join(row) + " |" for row in data)
        return "\n".join(out) + "\n\n"

    def quote(self, content: str) -> str:
        return "\n".join(
            ("> " + line if line else ">") for line in content.strip().splitlines()
        )

    def find_descendant(self, node: Node, tag: str) -> Optional[Node]:
        for child in node.children:
            if isinstance(child, Node):
                if child.tag == tag:
                    return child
                found = self.find_descendant(child, tag)
                if found:
                    return found
        return None

    def export_svg(self, svg: Node) -> str:
        self.figures += 1
        filename = f"fig-{self.figures:03d}.svg"
        (self.asset_dir / filename).write_text(standalone_svg(svg), encoding="utf-8")
        label = clean_space(plain_text(attr(svg, "aria-label", f"Diagram {self.figures}")))
        return f"![{label}](assets/figures/{filename})\n\n"

    def render_figure(self, node: Node) -> str:
        svg = self.find_descendant(node, "svg")
        caption = next((x for x in node.children if isinstance(x, Node) and x.tag == "figcaption"), None)
        if not svg:
            return self.render_children(node)
        self.figures += 1
        filename = f"fig-{self.figures:03d}.svg"
        (self.asset_dir / filename).write_text(standalone_svg(svg), encoding="utf-8")
        label = clean_space(plain_text(attr(svg, "aria-label", f"Diagram {self.figures}")))
        cap = clean_space(self.render_inline_children(caption)) if caption else label
        return f"![{label}](assets/figures/{filename})\n\n{cap}\n\n"


def output_path(source: Path) -> Path:
    return source.with_suffix(".md")


def convert(source: Path) -> tuple[Path, int]:
    renderer = MarkdownRenderer(source.parent)
    destination = output_path(source)
    destination.write_text(renderer.render_file(source), encoding="utf-8")
    return destination, renderer.figures


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("files", nargs="*", type=Path, help="HTML files; defaults to all six note files")
    args = ap.parse_args()
    files = [((ROOT / f) if not f.is_absolute() else f) for f in args.files] or DEFAULT_FILES
    for source in files:
        if not source.exists():
            ap.error(f"missing input: {source}")
        destination, figures = convert(source)
        print(f"{source.relative_to(ROOT)} -> {destination.relative_to(ROOT)} ({figures} diagrams)")


if __name__ == "__main__":
    main()

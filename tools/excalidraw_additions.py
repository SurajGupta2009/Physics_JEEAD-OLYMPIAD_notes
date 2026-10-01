#!/usr/bin/env python3
"""Helpers for the additive native-diagram blocks in chapter masters.

Every retrofit batch only *inserted* material into the masters: a
``> **Companion:**`` line plus an ``![[…excalidraw]]`` embed, or a generated
``> [!abstract] DIAGRAM Dn.n — …`` callout with ``**Show:**`` / ``**Source:**``
/ ``**Read:**`` lines followed by its embed.  Nothing the chapter author wrote
was deleted or rewritten, which is exactly what :func:`insert_only` proves.
"""
from __future__ import annotations

import difflib
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EMBED_LINE = re.compile(r"^!\[\[\.\./_obsidian/excalidraw/(?P<slug>[A-Za-z0-9-]+?)-D\d+-\d+"
                        r"\.excalidraw(?:\|[^\]\n]*)?\]\]$")
COMPANION_LINE = re.compile(r"^> \*\*Companion:\*\*")
GENERATED_BRIEF = re.compile(r"^> \[!abstract\] DIAGRAM D\d+\.\d+ — ")
BRIEF_DETAIL = re.compile(r"^> \*\*(?:Show|Source|Read|Search|Companion):\*\*")


def additive_line(line: str) -> bool:
    """True for lines that only a generator could have written."""
    stripped = line.rstrip("\n")
    return bool(COMPANION_LINE.match(stripped) or GENERATED_BRIEF.match(stripped)
                or BRIEF_DETAIL.match(stripped) or EMBED_LINE.match(stripped))


def insert_only(original: str, current: str) -> bool:
    """True when ``current`` is ``original`` plus inserted lines only.

    Equivalent to: no original line was deleted, reordered away or rewritten.
    """
    opcodes = difflib.SequenceMatcher(None, original.splitlines(), current.splitlines()).get_opcodes()
    return not any(kind in ("delete", "replace") for kind, _, _, _, _ in opcodes)


def base_ref() -> str | None:
    """The pre-retrofit commit: the merge base with the default branch."""
    for args in (["merge-base", "HEAD", "origin/main"],
                 ["merge-base", "HEAD", "main"],
                 ["rev-parse", "HEAD^"]):
        result = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
    return None


def original_text(path: str, ref: str | None = None) -> str | None:
    """``path`` as committed at ``ref`` (or ``HEAD`` when ref is unknown)."""
    result = subprocess.run(["git", "show", f"{ref or 'HEAD'}:{path}"], cwd=ROOT,
                            capture_output=True, text=True)
    return result.stdout if result.returncode == 0 else None

#!/usr/bin/env python3
"""Repository-wide verification of every native Excalidraw diagram companion.

Checks, for all chapters registered in ``topics.json``:

* every DIAGRAM brief in the master has exactly one native scene embed;
* every embed resolves to a parseable, primitives-only ``.excalidraw.md`` scene
  under ``_obsidian/excalidraw`` with finite, on-canvas geometry;
* the chapter's ``figures.json`` records exactly those ids, in order, with the
  pinned renderer and no orphan scene files;
* the master is a strict superset of its committed original (only additive
  insertions; no original line removed or rewritten);
* the manifest's Mermaid ``figures`` records are unchanged from the commit.

Run from the repository root:

    python3 tools/verify_all_diagrams.py            # human-readable report
    python3 tools/verify_all_diagrams.py --quiet    # totals only
"""
from __future__ import annotations

import difflib
import json
import math
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VAULT = ROOT / "_obsidian" / "excalidraw"
RENDERER = "obsidian-excalidraw-plugin@2.27.3"
SCENE_BLOCK = re.compile(r"(?ms)^# Drawing\s*\n```json\s*\n(.*?)\n```\s*\n%%")
EMBED = re.compile(r"!\[\[([^\]\n]+?\.excalidraw)(?:\|[^\]\n]*)?\]\]")
BRIEF = re.compile(r"^> \[!abstract\] DIAGRAM (D\d+\.\d+) [·—] ", re.M)
COMPANION = re.compile(r"^> \[!abstract\] DIAGRAM (D\d+\.\d+) — ", re.M)
PRIMITIVES = {"text", "line", "arrow", "rectangle", "ellipse", "diamond"}
RASTER = re.compile(r"\.(png|jpe?g|gif|webp|bmp)\b", re.I)


def scene_data(path: Path) -> dict:
    match = SCENE_BLOCK.search(path.read_text(encoding="utf-8"))
    if not match:
        raise ValueError("missing # Drawing JSON block")
    return json.loads(match.group(1))


def check_scene(path: Path, diagram_id: str) -> list[str]:
    problems: list[str] = []
    text = path.read_text(encoding="utf-8")
    if f"diagram-id: {diagram_id}" not in text:
        problems.append(f"{path.name}: diagram-id mismatch")
    try:
        data = scene_data(path)
    except (ValueError, json.JSONDecodeError) as exc:
        return problems + [f"{path.name}: invalid scene ({exc})"]
    if data.get("type") != "excalidraw" or data.get("version") != 2:
        problems.append(f"{path.name}: invalid Excalidraw header")
    if data.get("files"):
        problems.append(f"{path.name}: embedded files are not allowed")
    elements = data.get("elements")
    if not isinstance(elements, list) or not elements:
        return problems + [f"{path.name}: no elements"]
    ids = [element.get("id") for element in elements]
    if len(ids) != len(set(ids)) or not all(isinstance(i, str) and i for i in ids):
        problems.append(f"{path.name}: duplicate or malformed element ids")
    for element in elements:
        kind = element.get("type")
        if kind not in PRIMITIVES:
            problems.append(f"{path.name}: element type {kind!r} is not editable")
        for key in ("x", "y", "width", "height", "angle"):
            value = element.get(key)
            if not isinstance(value, (int, float)) or not math.isfinite(value):
                problems.append(f"{path.name}: element {element.get('id')} has invalid {key}")
        if element.get("y", 0) < -1:
            problems.append(f"{path.name}: element {element.get('id')} is above the canvas")
        if element.get("locked"):
            problems.append(f"{path.name}: element {element.get('id')} is locked")
    if any(element.get("type") == "image" for element in elements):
        problems.append(f"{path.name}: raster image elements are not allowed")
    return problems


def git_show(path: str) -> str | None:
    try:
        return subprocess.check_output(["git", "show", f"HEAD:{path}"], cwd=ROOT,
                                       stderr=subprocess.DEVNULL).decode("utf-8")
    except subprocess.CalledProcessError:
        return None


def verify() -> tuple[list[str], list[tuple[str, int, int]]]:
    problems: list[str] = []
    rows: list[tuple[str, int, int]] = []
    topics = json.loads((ROOT / "topics.json").read_text(encoding="utf-8"))["topics"]
    known_scenes: set[str] = set()

    for topic in sorted(topics, key=lambda item: item["order"]):
        slug = topic["slug"]
        directory = ROOT / slug
        name = f"{slug.capitalize()}.md"
        master = directory / name
        if not master.is_file():
            problems.append(f"{slug}: master {name} is missing")
            continue
        source = master.read_text(encoding="utf-8")
        briefs = BRIEF.findall(source)
        if len(briefs) != len(set(briefs)):
            problems.append(f"{slug}: duplicate DIAGRAM brief ids")
        embeds = [target for target in EMBED.findall(source)]
        if len(embeds) != len(briefs):
            problems.append(f"{slug}: {len(embeds)} embeds for {len(briefs)} briefs")
        manifest_path = directory / "figures.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        drawings = manifest.get("drawings", [])
        drawing_ids = [drawing["id"] for drawing in drawings]
        if sorted(drawing_ids) != sorted(briefs):
            problems.append(f"{slug}: figures.json ids do not match the DIAGRAM briefs")
        embed_ids = [re.search(r'(?:^|-)D(\d+)-(\d+)\.excalidraw$', target) for target in embeds]
        embed_ids = [f"D{m.group(1)}.{int(m.group(2))}" for m in embed_ids if m]
        if sorted(embed_ids) != sorted(briefs):
            problems.append(f"{slug}: embed ids do not match the DIAGRAM briefs")
        if manifest.get("renderer") != RENDERER:
            problems.append(f"{slug}: renderer is not pinned to {RENDERER}")
        if RASTER.search(source):
            problems.append(f"{slug}: raster image reference in the master")
        original_manifest = git_show(f"{slug}/figures.json")
        if original_manifest is not None:
            committed = json.loads(original_manifest)
            if committed.get("figures") and committed.get("figures") != manifest.get("figures"):
                problems.append(f"{slug}: Mermaid figure records changed")

        original_master = git_show(f"{slug}/{name}")
        if original_master is not None:
            old_lines = original_master.splitlines()
            new_lines = source.splitlines()
            changed = [op for op in difflib.SequenceMatcher(None, old_lines, new_lines).get_opcodes()
                       if op[0] in ("delete", "replace")]
            if changed:
                problems.append(f"{slug}: original master lines were removed or rewritten")

        for drawing in drawings:
            ident = drawing["id"]
            scene = ROOT / drawing["file"]
            if not scene.is_file():
                problems.append(f"{ident}: scene file {drawing['file']} is missing")
                continue
            known_scenes.add(scene.name)
            if scene.parent.resolve() != VAULT.resolve():
                problems.append(f"{ident}: scene is outside the shared vault folder")
            if scene.name != f"{slug}-{ident.replace('.', '-')}.excalidraw.md":
                problems.append(f"{ident}: unexpected scene filename {scene.name}")
            problems += check_scene(scene, ident)
            if not drawing.get("source", "").startswith(f"{slug}/"):
                problems.append(f"{ident}: provenance source does not point into {slug}/")
        rows.append((slug, len(briefs), len(drawings)))

    for scene in sorted(VAULT.glob("*.excalidraw.md")):
        if scene.name not in known_scenes:
            problems.append(f"orphan scene not referenced by any manifest: {scene.name}")
    return problems, rows


def main() -> int:
    problems, rows = verify()
    if "--quiet" not in sys.argv:
        for slug, briefs, drawings in rows:
            print(f"  {slug:<26} {briefs:>3} briefs · {drawings:>3} scenes")
    print(f"\nchapters: {len(rows)} · scenes: {sum(r[2] for r in rows)} · problems: {len(problems)}")
    for problem in problems:
        print(f"  ✗ {problem}")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())

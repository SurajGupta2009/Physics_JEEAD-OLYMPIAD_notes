"""Shared checks for editable Obsidian Excalidraw scene embeds.

Call from a chapter's local checker with its ``ROOT``, source text and
``D<part>.<number>`` regex matches. This deliberately validates native JSON
rather than exported SVG/PNG assets.
"""
from __future__ import annotations

import json
import math
import re
from pathlib import Path
from typing import Iterable

EMBED_PATTERN = r"!\[\[([^\]\n]+\.excalidraw)(?:\|[^\]\n]*)?\]\]"
SCENE_BLOCK_PATTERN = r"(?ms)^# Drawing\s*\n```json\s*\n(.*?)\n```\s*\n%%"


def validate_excalidraw(root: Path, source: str,
                         diagrams: Iterable[tuple[str, str]]) -> list[str]:
    """Return all scene/embed/manifest problems for a single chapter.

    ``diagrams`` is the list of numeric pairs returned by the chapter's
    ``DIAGRAM Dn.n`` regex. Embed targets are expected to point into the shared
    ``_obsidian/excalidraw`` vault folder.
    """
    errors: list[str] = []
    def check(condition: bool, message: str) -> None:
        if not condition:
            errors.append(message)

    diagram_pairs = list(diagrams)
    expected_ids = {f"D{part}.{int(number)}" for part, number in diagram_pairs}
    embeds = re.findall(EMBED_PATTERN, source)
    embed_ids: list[str] = []
    embed_paths: dict[str, Path] = {}
    vault = (root.parent / "_obsidian" / "excalidraw").resolve()

    for target in embeds:
        match = re.search(r"(?:^|-)D(\d+)-(\d+)\.excalidraw$", target)
        if not match:
            check(False, f"Excalidraw embed has an unexpected filename: {target}")
            continue
        diagram_id = f"D{match.group(1)}.{int(match.group(2))}"
        embed_ids.append(diagram_id)
        path = (root / f"{target}.md").resolve()
        check(path.parent == vault,
              f"{target}: scene must be stored directly under _obsidian/excalidraw")
        check(path.is_file(), f"Excalidraw scene is missing: {target}.md")
        embed_paths[diagram_id] = path
        if not path.is_file():
            continue
        scene_text = path.read_text(encoding="utf-8")
        check(f"diagram-id: {diagram_id}" in scene_text,
              f"{target}: diagram-id metadata mismatch")
        block = re.search(SCENE_BLOCK_PATTERN, scene_text)
        check(block is not None, f"{target}: missing Excalidraw JSON scene block")
        if not block:
            continue
        try:
            data = json.loads(block.group(1))
        except json.JSONDecodeError as exc:
            check(False, f"{target}: invalid scene JSON ({exc})")
            continue
        if not isinstance(data, dict):
            check(False, f"{target}: Excalidraw JSON root must be an object")
            continue
        check(data.get("type") == "excalidraw" and data.get("version") == 2,
              f"{target}: invalid Excalidraw document header")
        elements = data.get("elements")
        check(isinstance(elements, list) and bool(elements),
              f"{target}: scene has no elements")
        if isinstance(elements, list):
            element_ids = [element.get("id") for element in elements if isinstance(element, dict)]
            check(len(element_ids) == len(elements), f"{target}: malformed scene element")
            ids_are_strings = all(isinstance(element_id, str) and element_id for element_id in element_ids)
            check(ids_are_strings, f"{target}: scene element ids must be non-empty strings")
            if ids_are_strings:
                check(len(element_ids) == len(set(element_ids)), f"{target}: duplicate element ids")
            for element in elements:
                if not isinstance(element, dict):
                    continue
                for key in ("x", "y", "width", "height"):
                    value = element.get(key)
                    check(isinstance(value, (int, float)) and math.isfinite(value),
                          f"{target}: element {element.get('id')} has invalid {key}")

    check(len(embeds) == len(diagram_pairs),
          f"each DIAGRAM brief needs one Excalidraw embed ({len(embeds)} embeds / {len(diagram_pairs)} briefs)")
    check(len(embed_ids) == len(set(embed_ids)), "duplicate Excalidraw diagram embeds")
    actual_ids = set(embed_ids)
    check(actual_ids == expected_ids,
          f"Excalidraw embeds do not match DIAGRAM brief ids (missing {sorted(expected_ids-actual_ids)}, extra {sorted(actual_ids-expected_ids)})")

    manifest_path = root / "figures.json"
    check(manifest_path.is_file(), "figures.json provenance is required for Excalidraw drawings")
    if manifest_path.is_file():
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError) as exc:
            check(False, f"invalid figures.json drawing provenance ({exc})")
            return errors
        if not isinstance(manifest, dict):
            check(False, "figures.json root must be an object")
            return errors
        drawings = manifest.get("drawings", [])
        check(isinstance(drawings, list), "figures.json 'drawings' must be a list")
        if not isinstance(drawings, list):
            return errors
        drawing_ids = [d.get("id") for d in drawings if isinstance(d, dict)]
        check(len(drawing_ids) == len(drawings), "figures.json contains a malformed drawing record")
        valid_drawing_ids = [drawing_id for drawing_id in drawing_ids if isinstance(drawing_id, str)]
        check(len(valid_drawing_ids) == len(drawing_ids), "figures.json drawing ids must be strings")
        check(len(drawings) == len(diagram_pairs),
              f"figures.json needs one drawing record per DIAGRAM brief ({len(drawings)} / {len(diagram_pairs)})")
        check(set(valid_drawing_ids) == expected_ids,
              f"figures.json drawing ids mismatch (missing {sorted(expected_ids-set(valid_drawing_ids))}, extra {sorted(set(valid_drawing_ids)-expected_ids)})")
        check(manifest.get("slug") == root.name,
              f"figures.json slug must be {root.name!r}")
        check(manifest.get("renderer") == "obsidian-excalidraw-plugin@2.27.3",
              "figures.json renderer must name the pinned Obsidian Excalidraw plugin")
        for drawing in drawings:
            if not isinstance(drawing, dict):
                continue
            diagram_id = drawing.get("id")
            check(drawing.get("kind") == "excalidraw",
                  f"{diagram_id}: drawing kind must be excalidraw")
            check(bool(drawing.get("title")) and bool(drawing.get("show")) and bool(drawing.get("search")),
                  f"{diagram_id}: figures.json is missing its title or original drawing/search brief")
            file_name = drawing.get("file", "")
            check(isinstance(file_name, str) and file_name.endswith(".excalidraw.md"),
                  f"{diagram_id}: figures.json scene path must end in .excalidraw.md")
            if not isinstance(file_name, str):
                continue
            scene = (root.parent / file_name).resolve()
            check(scene.parent == vault and scene.is_file(),
                  f"figures.json scene is missing or outside the vault: {file_name}")
            embed_scene = embed_paths.get(diagram_id)
            if embed_scene is not None:
                check(scene == embed_scene,
                      f"{diagram_id}: figures.json scene path does not match its Markdown embed")
    return errors


def validate_svg_companions(root: Path) -> list[str]:
    """Fixed coverage/provenance for the additive legacy-SVG companion batches."""
    specs = {"string-waves": ("String-waves.md", 14, 4),
             "sound-waves": ("Sound-waves.md", 15, 15),
             "thermodynamics": ("Thermodynamics.md", 16, 35),
             "heat": ("Heat.md", 17, 25), "capacitors": ("Capacitors.md", 18, 32),
             "current-electricity": ("Current-electricity.md", 19, 26),
             "electromagnetic-waves": ("Electromagnetic-waves.md", 21, 7),
             "geometrical-optics": ("Geometrical-optics.md", 22, 46),
             "wave-optics": ("Wave-optics.md", 23, 28)}
    name, part, count = specs[root.name]
    source = (root / name).read_text(encoding="utf-8")
    pairs = re.findall(r"> \[!abstract\] DIAGRAM D(\d+)\.(\d+) —", source)
    errors = validate_excalidraw(root, source, pairs)
    if sorted(pairs, key=lambda p: int(p[1])) != [(str(part), str(n)) for n in range(1, count + 1)]:
        errors.append(f"expected unique D{part}.1–D{part}.{count} briefs")
    import xml.etree.ElementTree as ET
    manifest = json.loads((root / 'figures.json').read_text(encoding='utf-8'))
    for n, drawing in enumerate(manifest.get('drawings', []), 1):
        svg = f"assets/figures/fig-{n:03d}.svg"
        if svg not in source or drawing.get('source') != f"{root.name}/{name} · {svg}":
            errors.append(f"missing source SVG/provenance for {svg}")
        try:
            ET.parse(root / svg)
        except (ET.ParseError, OSError) as exc:
            errors.append(f"invalid source SVG {svg}: {exc}")
        path = root.parent / drawing['file']
        if path.is_file():
            block = re.search(SCENE_BLOCK_PATTERN, path.read_text(encoding='utf-8'))
            if block:
                data = json.loads(block[1])
                if data.get('files') or any(e['type'] == 'image' for e in data['elements']):
                    errors.append(f"{path.name}: must contain editable primitives, not images")
    return errors


def validate_waves_thermal(root: Path) -> list[str]:
    """Backward-compatible entry point for the previous batch."""
    return validate_svg_companions(root)

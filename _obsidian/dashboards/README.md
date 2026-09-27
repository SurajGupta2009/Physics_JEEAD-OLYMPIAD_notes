# Library — every chapter, one table

```dataview
TABLE WITHOUT ID
  order AS "#",
  link(file.path, title) AS "Chapter",
  block AS "Block",
  part AS "plan PART",
  status AS "Status",
  length(file.outlinks) AS "Links"
FROM -"_obsidian" AND -"_templates" AND -"docs"
WHERE slug
SORT order ASC, part ASC
```

> Rows are the chapter masters (any file with a `slug:` in its frontmatter). `order` is the
> course-spine slot ([spine.md](spine.md)); `block` groups the syllabus (mechanics · waves ·
> thermal · electricity-magnetism · optics · modern); `part` is the plan.md PART number for the
> chapters written under it, or the historical wave-spine number (1–9) for the nine original
> note-sets.

## By block

```dataview
TABLE WITHOUT ID rows.order AS "#", rows.file.link AS "Chapters"
FROM -"_obsidian" AND -"_templates" AND -"docs"
WHERE slug
GROUP BY block
SORT min(rows.order) ASC
```

## Anything missing its properties

Self-clearing: a master without `order`/`block` shows up here until it is backfilled.

```dataview
LIST
FROM -"_obsidian" AND -"_templates" AND -"docs"
WHERE slug AND (!order OR !block)
SORT file.name ASC
```

# Library — every chapter, one table

```dataview
TABLE part AS "Part", status AS "Status", length(file.outlinks) AS "Links"
FROM ""
WHERE slug
SORT part ASC
```

> Rows are the chapter masters (any file with a `slug` in its frontmatter). `part` matches the
> `plan.md` part number carried by each note's frontmatter; NaN parts are the appendix topics
> that have no plan v2 number.

---
type: wiki
status: live
created: 2026-05-21
updated: 2026-05-21
tags: [wiki, dot]
---

# DOT Knowledge

DOT / FMCSA reference hub. Links to checklists, procedures, regulations, and research.

## Compliance areas
- Driver qualification (49 CFR 391)
- Driving of CMVs (49 CFR 392)
- Vehicle parts & accessories (49 CFR 393)
- Hours of service (49 CFR 395)
- Vehicle inspection, repair, maintenance (49 CFR 396)
- Drug & alcohol testing (49 CFR 382)
- Hazardous materials (49 CFR 397)

## Active DOT documents
```dataview
TABLE compliance_area, review_frequency, updated
FROM "01-select-safety/DOT"
WHERE status != "archived"
SORT compliance_area ASC, updated DESC
```

## Recent DOT research
```dataview
LIST
FROM "05-research/DOT-safety"
SORT file.mtime DESC
LIMIT 10
```

## Key references
- FMCSR (49 CFR Parts 350-399): https://www.ecfr.gov/current/title-49/subtitle-B/chapter-III
- FMCSA: https://www.fmcsa.dot.gov/

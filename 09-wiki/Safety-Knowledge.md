---
type: wiki
status: live
created: 2026-05-21
updated: 2026-05-21
tags: [wiki, safety]
---

# Safety Knowledge

Index of safety topics. Each topic should resolve to a procedure, a training module, or a reference under `01-select-safety/`.

## Topic areas (Select Safety scope)

| Topic | Procedure | Training | Notes |
|---|---|---|---|
| Pre-trip inspection (CMV) | [[pre-trip-inspection]] | | DVIR per 49 CFR 396.11/396.13 |
| Driver qualification | | | DQ file — see [[driver-qualification-file]] |
| Hours of service | | | 49 CFR 395 — see [[DOT-Quick-Reference]] |
| Drug & alcohol program | | | 49 CFR 382 |
| Hazardous materials | | | 49 CFR 397 / 49 CFR 172 |
| Cargo securement | | | 49 CFR 393 Subpart I |
| Vehicle maintenance | | | 49 CFR 396 |
| Personal protective equipment | | | 29 CFR 1910.132 |
| Lockout / tagout | | | 29 CFR 1910.147 |
| Confined space entry | | | 29 CFR 1910.146 |
| Hot work | | | 29 CFR 1910.252 |
| Fall protection | | | 29 CFR 1926.501 |
| Electrical safety | | | 29 CFR 1910 Subpart S |
| Ergonomics / manual handling | | | OSHA general duty clause |
| Incident reporting | | | Internal + DOT/OSHA reportable |

## Active procedures
```dataview
LIST
FROM "01-select-safety/safety-procedures"
WHERE status != "archived"
SORT file.name ASC
```

## Training modules
```dataview
LIST
FROM "01-select-safety/training"
WHERE status != "archived"
SORT file.name ASC
```

## Key references

- FMCSR: https://www.ecfr.gov/current/title-49/subtitle-B/chapter-III
- OSHA General Industry (29 CFR 1910): https://www.osha.gov/laws-regs/regulations/standardnumber/1910
- OSHA Construction (29 CFR 1926): https://www.osha.gov/laws-regs/regulations/standardnumber/1926
- [[DOT-Knowledge]] · [[DOT-Quick-Reference]] · [[Recordkeeping-Retention]]

---
type: wiki
status: live
created: 2026-05-21
updated: 2026-05-21
tags: [wiki, programs]
---

# Program Building Knowledge

How I build programs and systems. Reusable patterns, lessons, decision logs.

## Stages
1. **Idea** — captured in `02-programs-systems/ideas/`. Just the problem and a sketch.
2. **Requirements** — `02-programs-systems/requirements/`. Use `/program-spec`. Problem, users, features, dependencies, out-of-scope.
3. **Build** — `02-programs-systems/builds/`. Day-by-day plan; track `build_stage`.
4. **Test** — `02-programs-systems/testing/`. Test cases, dry runs, edge cases.
5. **Document** — `02-programs-systems/documentation/`. Use `/notes-to-docs`.
6. **Release** — move to `02-programs-systems/active-programs/` with `status: released`.

## Active programs
```dataview
TABLE build_stage, next_action, owner, updated
FROM "02-programs-systems/active-programs" OR "02-programs-systems/builds"
WHERE status != "archived" AND status != "released"
SORT build_stage ASC, updated DESC
```

## Patterns I reuse
- *(Fill as I notice them. Examples: "checklist + sign-off page" pattern, "audit trail CSV" pattern, etc.)*

## Lessons learned
- 

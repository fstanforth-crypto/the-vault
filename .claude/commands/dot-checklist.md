---
description: Create a DOT compliance checklist
---

Create a DOT compliance checklist.

1. Ask which regulation or topic this covers (e.g. "49 CFR 396 — vehicle inspection, repair, maintenance").
2. Use `07-templates/Inspection-Checklist.md` as the base, plus the DOT frontmatter block.
3. File output under `01-select-safety/DOT/<kebab-case-name>.md`.
4. Frontmatter must include:
   - `compliance_area` (e.g. "vehicle-maintenance", "driver-qualification", "hours-of-service")
   - `dot_related: true`
   - `review_frequency` (annual / per-trip / monthly)
   - `vehicle_type` if applicable
5. Each checklist item must reference the specific FMCSR section.
6. Add a "records to keep" section listing what must be filed and for how long.
7. Add a "verification / audit" section: how a DOT auditor would test compliance.
8. Cross-link to related safety procedures and training.

Professional language. No filler. This document may be shown to a DOT auditor.

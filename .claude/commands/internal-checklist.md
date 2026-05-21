---
description: Create an internal checklist
---

Create an internal checklist (not necessarily DOT — could be onboarding, audit prep, deployment, etc.).

1. Ask the purpose and trigger (when is it run, by whom, how often?).
2. Use `07-templates/Inspection-Checklist.md` as a base — strip DOT-specific frontmatter if not applicable.
3. File output:
   - Operational/safety checklist → `01-select-safety/forms-checklists/`
   - Program/build/deploy checklist → `02-programs-systems/documentation/`
   - Project-specific checklist → `03-projects/active/<project>/`
4. Each item: short, verifiable, one action.
5. Group items by phase (pre / during / post) if applicable.
6. Add sign-off section if it's a record (who, when, signature line).
7. Set `review_frequency` so it doesn't go stale.

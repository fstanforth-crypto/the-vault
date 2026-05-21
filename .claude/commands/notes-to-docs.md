---
description: Turn notes into documentation
---

Turn rough notes into proper documentation.

1. Ask which notes — pointer to a file in `06-inbox/` or `02-programs-systems/builds/`.
2. Ask what kind of doc this is becoming:
   - Program documentation → `02-programs-systems/documentation/`
   - SOP → `01-select-safety/SOPs/` (use `/sop`)
   - Safety procedure → `01-select-safety/safety-procedures/` (use `/safety-procedure`)
   - Wiki entry → `09-wiki/`
3. Restructure the notes:
   - Start with purpose / what this is.
   - Then "how it works" — flow, diagrams (text-based ASCII or mermaid is fine), components.
   - Then "how to use" — concrete steps.
   - Then "how to maintain" — owner, dependencies, what breaks it.
   - Then references — to source code, related notes, regs.
4. Keep frontmatter consistent with the destination folder's conventions.
5. Link the new doc back from the source note (and update source's `status` to `documented`).
6. If you don't have enough info, ask me targeted questions rather than guessing.

---
description: Write program requirements
---

Write a program specification.

1. Ask the program name and the problem it solves.
2. Use `07-templates/Program-Spec.md`.
3. File output under `02-programs-systems/requirements/<kebab-case-name>.md`.
4. Frontmatter must include `program_name`, `problem`, `users`, `features`, `build_stage: requirements`, `next_action`, `owner`.
5. Each section:
   - **Problem**: 2-4 sentences. Concrete. Whose pain, what's broken now.
   - **Users**: roles, not "everyone." How many of each.
   - **Outcome / success criteria**: measurable. "Reduces X by Y" or "Eliminates Z step."
   - **Features (MVP)**: 3-7 bullets. What it DOES, not how it's built.
   - **Out of scope**: be specific — this is where MVPs survive.
   - **Dependencies**: external systems, data sources, integrations, approvals.
   - **Build stages**: keep the default checklist.
   - **Next action**: one specific thing, by whom, with a rough timebox.
6. Cross-link to any related programs (`[[wiki-links]]`) and the client/project this serves.
7. After creation, recommend whether this is ready to move to `02-programs-systems/builds/` or needs more spec work.

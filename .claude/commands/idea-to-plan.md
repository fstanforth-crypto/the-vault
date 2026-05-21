---
description: Turn an idea into a build plan
---

Turn a raw idea into a build plan.

1. Ask which idea — point me at a file in `02-programs-systems/ideas/` or paste it.
2. Stage 1: convert into a program spec using the `/program-spec` flow (file under `02-programs-systems/requirements/`).
3. Stage 2: produce a build plan using `07-templates/Automation-Build-Plan.md` if it's automation, or a more general plan if it's a full program.
4. File output under `02-programs-systems/builds/<kebab-case-name>.md` with `build_stage: planning`.
5. The plan should include:
   - Stack / tools required.
   - Day-by-day or step-by-step breakdown.
   - Specific deliverables per step (file, screen, integration).
   - Risk / failure modes.
   - First step I can do today, in 30 minutes or less.
6. Link the idea → spec → build chain with `[[wiki-links]]` and mark the original idea note `status: spec'd`.
7. After saving, ask if I want to also schedule a slot in today's plan.

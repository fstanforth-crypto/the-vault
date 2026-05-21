---
description: Triage 06-inbox/ into the right folders
---

Process my inbox.

1. List everything in `06-inbox/raw-notes/`, `06-inbox/voice-notes/`, and `06-inbox/screenshots/`, plus loose notes at the top of `06-inbox/` (except `Inbox.md`).
2. For each item, infer the type and propose:
   - Destination folder (e.g. `01-select-safety/safety-procedures/`)
   - New filename (kebab-case, descriptive, no dates in the filename)
   - Which template from `07-templates/` to apply
   - Frontmatter to populate
3. Routing rules:
   - Safety / DOT / SOP / inspection / incident → `01-select-safety/<subfolder>/`
   - Program idea / requirement / build → `02-programs-systems/<subfolder>/`
   - Project work → `03-projects/active/<project>/`
   - Content → `04-content/ideas/`
   - Research → `05-research/<topic>/`
4. Show me the full plan, ask for one-shot confirmation.
5. On confirm: move the file (don't copy — preserve history), reshape it with the template, fill frontmatter.
6. Append a log entry to `06-inbox/Inbox.md`: date, item, where it went.

Never delete originals. If unsure, leave in inbox and flag it.

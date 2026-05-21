---
description: Find orphans, broken links, empty notes, stale safety docs
---

Audit the vault for hygiene issues. Don't make changes — just produce a report.

Check for:
1. **Orphans** — notes not linked from any other note.
2. **Broken links** — `[[wiki-links]]` pointing to files that don't exist.
3. **Empty / stub notes** — files under 200 bytes with no real content.
4. **Missing frontmatter** — structured folders (`01-`, `02-`, `03-`) with notes missing required fields.
5. **Stale safety docs** — notes in `01-select-safety/**` where `(today - updated) > review_frequency`.
6. **Stuck programs** — items in `02-programs-systems/builds/` with `status: active` but no `updated` change in 30+ days.
7. **Inbox bloat** — anything in `06-inbox/` older than 7 days.

Output:
- One section per category, file list with line "why this is flagged"
- A suggested follow-up command for each (`/process-inbox`, archive, fill frontmatter, etc.)

I'll decide what to act on.

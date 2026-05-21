---
type: meta
status: live
created: 2026-05-21
updated: 2026-05-21
tags: [system, workflows]
---

# Workflows

End-to-end flows the vault is built around. Each maps to one or more slash commands.

## Daily
1. Open `00-command-center/AGENTIC-OS.md`.
2. Run `/plan-today` → review `Today.md`.
3. Work the top items.
4. Drop captures into `06-inbox/`.
5. End of day: edit `Today.md` end-of-day section.

## Weekly (Friday)
1. Run `/process-inbox` until empty.
2. Run `/vault-cleanup` — fix the easy stuff.
3. Run `/weekly-review` — edit the draft.
4. Archive last week's `Weekly-Review.md` into `_archive-vault/weekly-reviews/`.

## Safety procedure (new)
1. Capture source in `06-inbox/raw-notes/`.
2. Run `/safety-procedure`.
3. Review; if it touches a regulation, also run `/dot-checklist` if no checklist exists yet.
4. Link from `09-wiki/Safety-Knowledge.md`.
5. Schedule next review based on `review_frequency`.

## Program (idea → release)
1. Drop the idea in `02-programs-systems/ideas/`.
2. `/idea-to-plan` → produces spec + build plan.
3. Build in `02-programs-systems/builds/`, update `build_stage` as you go.
4. `/notes-to-docs` when build is testable.
5. On release: move to `02-programs-systems/active-programs/` with `status: released`.
6. Decommission: archive to `_archive-vault/`.

## Client request
1. Capture in `06-inbox/`.
2. `/client-doc` produces the deliverable in `01-select-safety/clients/<client>/`.
3. Export to PDF for delivery (Obsidian → Export to PDF).
4. Log the delivery in the client note.

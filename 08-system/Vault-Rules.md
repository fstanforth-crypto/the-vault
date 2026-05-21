---
type: meta
status: live
created: 2026-05-21
updated: 2026-05-21
tags: [system, rules]
---

# Vault Rules

The non-negotiables. If Claude breaks one of these, call it out.

## Naming
- Folders: numbered top-level (`00-`, `01-`, …) — keeps order stable.
- Files: `kebab-case-descriptive.md`. No dates in filenames (the `created:` frontmatter holds that).
- No spaces in filenames.

## Frontmatter
- Every structured note has YAML frontmatter — see `08-system/CLAUDE.md` for the fields.
- `created` is set once, never edited. `updated` is bumped on every meaningful edit.
- `status` values across the vault:
  - `idea`, `draft`, `in-progress`, `active`, `review`, `done`, `released`, `archived`, `blocked`

## Archiving
- Never delete. Move into `_archive-vault/` preserving the original folder path (e.g. `_archive-vault/01-select-safety/SOPs/old-sop.md`).
- Set `status: archived` on the way in.

## Linking
- Cross-link with `[[wiki-links]]`, not paths.
- Every safety procedure references the regulation it satisfies.
- Every program references its project (if any) and client (if any).

## Templates
- New structured notes are created from `07-templates/`. Don't invent fields.
- If a template is missing what you need, propose an edit to the template — don't one-off a new shape.

## Inbox
- `06-inbox/` is staging only. Items shouldn't live there longer than 7 days.
- `/process-inbox` is the only sanctioned way to drain it.

## Claude behavior
- Never delete files.
- Never edit a file outside the scope of the request without flagging it.
- When in doubt, ask.
- Cite sources on DOT and safety claims.

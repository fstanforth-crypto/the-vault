---
type: meta
status: live
created: 2026-05-21
updated: 2026-05-21
tags: [system, changelog]
---

# Changelog

Structural changes to the vault. Append entries; don't rewrite history.

## 2026-05-21
- Vault initialized.
- Folder structure created (`00-` through `09-`, plus `_archive-vault/`).
- Templates seeded in `07-templates/`.
- 16 slash commands seeded in `.claude/commands/`.
- `08-system/CLAUDE.md` written as the operating instructions.
- Seeded examples: pre-trip-inspection safety procedure, driver-qualification-file DOT note, driver-onboarding-workflow program spec, inbox ELD-gaps raw note.
- Added wiki reference cards: `DOT-Quick-Reference.md`, `Recordkeeping-Retention.md`. Enriched `Safety-Knowledge.md`.
- Pre-configured Obsidian (`.obsidian/`): new-file location, attachments, templates folder, daily-notes folder + template, core plugins enabled.
- Copied 5 Anthropic skills into `.claude/skills/`: pdf, docx, xlsx, doc-coauthoring, skill-creator.
- Added hooks (`.claude/hooks/`):
  - `bump-updated.py` — PostToolUse on Write/Edit/MultiEdit, auto-stamps `updated:` frontmatter on any edited note.
  - `session-start.py` — SessionStart, injects vault status (inbox, active programs, stale safety docs) as additional context.
- `git init` + initial commit.

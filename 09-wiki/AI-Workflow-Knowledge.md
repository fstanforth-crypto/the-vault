---
type: wiki
status: live
created: 2026-05-21
updated: 2026-05-21
tags: [wiki, ai, claude]
---

# AI Workflow Knowledge

How I use Claude, Claude Code, and Obsidian together. Patterns that work, prompts that don't, integrations to build.

## Stack
- **Obsidian** — the vault UI. Plugins required: Dataview. Recommended: Templater, Tasks, Periodic Notes.
- **Claude Code** — running with this vault as the working directory. Reads `CLAUDE.md` → `08-system/CLAUDE.md`.
- **Slash commands** — `.claude/commands/` — pre-built workflows.

## What Claude is good at here
- Restructuring messy notes into templates.
- Cross-linking — finding related notes I missed.
- Drafting professional language for client/DOT documents.
- Audits — orphans, stale docs, missing frontmatter.
- Research summaries (with caveats; cite sources).

## What Claude is NOT good at (yet)
- Knowing what I *should* be working on without being told my priorities.
- Inventing reg citations — make it look them up or refuse.
- Replacing human review on anything compliance-related.

## Prompt patterns
- Be specific about the destination folder and template.
- Ask for a plan before edits when changes touch multiple files.
- For DOT/safety: always require source citations.

## Ideas to build
- *(Add as I think of them. Example: auto-flag SOPs whose linked regulation has changed.)*

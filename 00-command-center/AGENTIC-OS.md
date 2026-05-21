---
type: dashboard
status: live
created: 2026-05-21
updated: 2026-05-21
tags: [dashboard, command-center]
---

# AGENTIC OS — Command Center

> Vault home. Run the day from here. Requires the **Dataview** plugin for the live queries below.

## Today's priorities

![[Today]]

> Use **`/plan-today`** to have Claude rebuild today from active work.

---

## Active Select Safety work
```dataview
TABLE status, priority, due, file.folder AS area
FROM "01-select-safety"
WHERE status = "active" OR status = "in-progress" OR status = "draft"
SORT priority ASC, due ASC
LIMIT 15
```

## DOT / compliance tasks
```dataview
TABLE status, priority, due, compliance_area
FROM "01-select-safety/DOT" OR "01-select-safety/compliance"
WHERE status != "archived" AND status != "done"
SORT due ASC
```

## Safety procedures in draft or review
```dataview
TABLE status, updated, review_frequency, owner
FROM "01-select-safety/safety-procedures"
WHERE status = "draft" OR status = "review"
SORT updated DESC
```

---

## Active programs I'm building
```dataview
TABLE build_stage, next_action, priority, owner
FROM "02-programs-systems/active-programs" OR "02-programs-systems/builds"
WHERE status != "archived" AND status != "released"
SORT priority ASC
```

## Current projects
```dataview
TABLE status, stage, due, client
FROM "03-projects/active"
SORT priority ASC, due ASC
```

---

## Inbox to process
```dataview
LIST
FROM "06-inbox"
WHERE !contains(file.name, "Inbox")
SORT file.mtime DESC
LIMIT 20
```

## Research queue
```dataview
TABLE status, source, priority
FROM "05-research"
WHERE status = "in-progress" OR status = "queued"
SORT priority ASC
```

## Content / tutorial ideas
```dataview
TABLE status, format, priority
FROM "04-content/ideas"
WHERE status = "idea" OR status = "drafting"
SORT priority ASC
LIMIT 10
```

---

## Weekly review

Latest: [[Weekly-Review]]

## Metrics & follow-ups

See [[Metrics]]

---

# Claude commands

> Type these in Claude Code while the vault is your working directory. Files live in `.claude/commands/`.

## Planning
- **`/plan-today`** — Build today's plan from active work
- **`/what-next`** — What should I work on next?
- **`/weekly-review`** — Generate a weekly review draft

## Inbox & cleanup
- **`/process-inbox`** — Triage `06-inbox/` into the right folders
- **`/vault-cleanup`** — Find orphans, broken links, empty notes, stale reviews

## Select Safety
- **`/safety-procedure`** — Build a safety procedure from notes
- **`/dot-checklist`** — Create a DOT compliance checklist
- **`/sop`** — Draft an SOP from rough notes
- **`/training-module`** — Create a training module
- **`/internal-checklist`** — Create an internal checklist
- **`/client-doc`** — Create a client-facing safety document

## Programs / systems
- **`/program-spec`** — Write program requirements
- **`/idea-to-plan`** — Turn an idea into a build plan
- **`/review-programs`** — Review active programs
- **`/notes-to-docs`** — Turn notes into documentation

## Research
- **`/research`** — Research a DOT/safety topic and file the note

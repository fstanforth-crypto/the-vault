---
updated: 2026-06-08
name: plan-today-automated-execute-zero-decision-tasks
description: /plan-today runs are automated (no human to reply "go"); execute zero-decision reversible tasks instead of re-listing them
metadata:
  type: feedback
---

The vault's slash commands (`/plan-today`, `/weekly-review`) run automated — git log shows `Auto: /plan-today` commits with no human in the loop. From ~2026-05-28 to 2026-06-08, Today.md was regenerated ~11 times all asking the human to reply "go" to unblock work; nobody replied because the runs are automated, so the disk never changed.

**Why:** A planning command that waits for human confirmation in an automated context is a guaranteed stall. Re-planning the same blocked items is the actual waste.

**How to apply:** When a board item needs no human decision and is reversible (this vault never deletes — it archives), execute it during the run rather than re-listing it. On 2026-06-08 this meant drafting [[driver-qualification-file-sop]] and processing the inbox directly. Reserve the Top 3 for items that genuinely need the user: a decision (MVR vendor), a sign-off (SOP review), or outside data (carrier HOS records).

---
type: daily-note
status: in-progress
created: 2026-05-27
updated: 2026-05-27
tags: [daily]
priority: high
---

# Wednesday, May 27th 2026

> Edited by hand or by `/plan-today`. Claude won't overwrite Notes or End-of-day sections.

## Top 3
1. 🚨 **STALE — day 7 on plan, zero movement** — [[driver-onboarding-workflow]]: make the call today. Either (a) wire the MVR webhook stub against a chosen vendor, or (b) flip `build_stage: build` → `requirements` and add `MVR vendor selection` as the gating next_action. ~2hr to wire, ~10min to downgrade.
   - *Why:* Same item, seventh consecutive day. Yesterday's plan said "the call has to be made today" — it wasn't. Carrying it forward again without a decision is what's causing the rot. `dependencies` still lists `MVR vendor: TBD`, so if the vendor is genuinely unselected the file is lying about its stage. Force the downgrade if no vendor was picked by EOD today; do not roll this to a Thursday plan untouched.
2. 🚨 **STALE — day 3 on plan, zero movement** — Draft DQ-file SOP via `/sop`. Create `01-select-safety/SOPs/` (folder doesn't exist yet), file the SOP there, backlink from [[driver-qualification-file]], and resolve its two open questions (digital-vs-paper, retention vs. insurance). ~45min.
   - *Why:* Named dependency of [[driver-onboarding-workflow]], so this work also unblocks #1 regardless of which path #1 takes. The folder being entirely missing — not just empty — is what's keeping this from feeling real; creating it is half the friction.
3. 🚨 **STALE — day 3 on plan, 6 days old in inbox** — Process [[2026-05-21-fleet-mgr-call-eld-gaps]]: split into (a) a research/audit note for the short-haul exemption check against 49 CFR 395.1(e) under `05-research/` or `01-select-safety/DOT/`, and (b) a program-idea note for the weekly HOS-violation digest under `02-programs-systems/ideas/`. ~20min.
   - *Why:* Still the only file in `06-inbox/raw-notes/` and the digest idea is the most plausible next program once onboarding lands or downgrades. Leaving it in raw form means it can't be picked up by `/what-next` or surfaced anywhere.

## Select Safety
- [ ] Create `01-select-safety/SOPs/` and draft DQ-file SOP via `/sop` (see Top 3 #2)
  - *Why:* Folder doesn't exist yet; gating dependency for the only active program.
- [ ] Short-haul exemption audit against 49 CFR 395.1(e) for the two paper-log drivers from the ELD-gaps note
  - *Why:* Two drivers on paper logs is a live compliance risk if the 150-air-mile radius / 14-hr duty math fails. Surfaces once Top 3 #3 splits the inbox note into a real research/audit note.

## Programs / builds
- [ ] [[driver-onboarding-workflow]] — MVR webhook wiring **or** stage downgrade by EOD (see Top 3 #1)
  - *Why:* Only active program; day 7 stale. If today ends with no decision, the program is the bottleneck, not the work.

## Other
- [ ] 

## Notes


## End-of-day
- What moved forward?
- What stalled?
- What goes to inbox?

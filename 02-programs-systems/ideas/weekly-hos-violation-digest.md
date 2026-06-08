---
type: program-spec
status: active
created: 2026-06-08
updated: 2026-06-08
tags: [program, idea, hos, eld, reporting, automation]
area: select-safety
program_name: Weekly HOS Violation Digest
problem: The ELD provider's HOS reports don't consolidate violations into one place, so a fleet manager has to hunt across screens and violations slip through.
users: [fleet manager, safety manager]
features: [pull HOS violations across drivers, dedupe and categorize, weekly email/Markdown digest, trend vs prior week]
build_stage: idea
dependencies: [ELD provider API or export access, list of drivers in scope]
next_action: Confirm ELD provider and whether it exposes an API or scheduled export
priority: medium
owner:
---

# Weekly HOS Violation Digest — Program Idea

> Source: untriaged voice memo from a fleet-manager call about ELD compliance gaps (carrier TBD), 2026-05-21. Triaged into this idea note on 2026-06-08.

## Problem

The ELD provider produces HOS data but does not roll violations into a single view. The fleet manager wants one weekly digest that aggregates all HOS violations across drivers so nothing is missed between manual checks.

## Users

- **Fleet manager** — primary reader; wants a single weekly summary.
- **Safety manager** — uses the digest to drive coaching and corrective action.

## Outcome / success criteria

- One digest per week covering all in-scope drivers.
- Each violation categorized (HOS type, driver, date) and de-duplicated across reports.
- Week-over-week trend so recurring offenders surface.

## Features (MVP)

- Pull last 7 days of HOS violations from the ELD provider (API or scheduled export).
- Normalize and de-duplicate across the provider's separate reports.
- Categorize by violation type and driver.
- Output a Markdown/email digest with counts and a short "needs attention" list.

## Out of scope

- Real-time alerting (digest is weekly batch).
- Auto-issuing coaching/discipline — digest informs, humans act.

## Dependencies

- ELD provider identification + API or export access.
- Roster of drivers in scope.
- Overlaps with the personal-conveyance / short-haul findings in [[short-haul-exemption-and-personal-conveyance-audit]] — the audit is the manual version of what this automates.

## Build stages
- [x] Idea
- [ ] Requirements
- [ ] Design
- [ ] Build
- [ ] Test
- [ ] Document
- [ ] Release

## Next action

Confirm the ELD provider and whether it exposes an API or scheduled export — that gates the entire build.

## Related
- [[short-haul-exemption-and-personal-conveyance-audit]]
- [[driver-onboarding-workflow]] — adjacent Select Safety program
- [[DOT-Knowledge]]

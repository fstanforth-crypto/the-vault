---
type: program-spec
status: active
created: 2026-05-21
updated: 2026-05-21
tags: [program, driver-onboarding, dot, automation]
area: select-safety
program_name: Driver Onboarding Workflow
problem: Carriers lose DQ-file completeness during onboarding because the steps are tribal knowledge spread across HR, dispatch, and safety.
users: [HR, safety manager, driver, dispatch]
features: [DQ-file checklist, document upload, medical cert tracking, Clearinghouse query trigger, ready-to-drive signoff]
build_stage: build
dependencies: [DQ-file SOP, Clearinghouse account, MVR vendor]
next_action: Wire MVR vendor webhook to mark MVR step complete automatically
priority: high
owner:
---

# Driver Onboarding Workflow

## Problem

Onboarding a new driver requires 12-15 DOT-required artifacts (see [[driver-qualification-file]]) collected by multiple people. Steps get skipped or backdated, which surfaces as audit findings months later. We need a single source of truth that blocks "ready to drive" until every required item is present and dated correctly.

## Users

- **HR / onboarding coordinator** — runs the workflow, requests documents from driver and previous employers.
- **Safety manager** — final reviewer; signs off on completeness.
- **Driver** — completes application, uploads documents, signs forms.
- **Dispatch** — sees "ready to drive" status before assigning loads.

## Outcome / success criteria

- 100% of newly hired drivers have a complete DQ file before first dispatch.
- Onboarding cycle time reduced from current baseline (TBD) to ≤ 5 business days.
- Zero audit findings on new-hire DQ files at next DOT review.

## Features (MVP)

- Per-driver onboarding checklist mirroring 49 CFR 391.51.
- Document upload + storage (PDF) with timestamp and uploader.
- Medical cert expiration tracker → alert 60 days before expiry.
- Clearinghouse pre-employment query trigger + result attachment.
- MVR request → result attachment.
- "Ready to drive" sign-off gate — cannot be set true with any required field blank.
- Audit-export: zip of full DQ file by driver.

## Out of scope

- Recurring (post-hire) compliance — handled by a separate program.
- Payroll, benefits, tax forms.
- Equipment assignment.

## Dependencies

- DQ-file SOP — must be finalized first (see `01-select-safety/SOPs/`).
- Clearinghouse account credentials and API access (if available).
- MVR vendor selection — currently TBD.
- Storage — where do PDFs live? S3? Carrier portal?
- Authentication — single sign-on or carrier-managed accounts.

## Build stages

- [x] Requirements
- [x] Design
- [ ] Build
- [ ] Test
- [ ] Document
- [ ] Release

## Next action

Wire MVR vendor webhook to mark MVR step complete automatically. Owner TBD. Estimate: 2 days.

## Related

- [[driver-qualification-file]] — regulatory spec this implements
- [[pre-trip-inspection]] — adjacent operational procedure
- [[DOT-Knowledge]]

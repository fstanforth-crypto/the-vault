---
type: sop
status: draft
created: 2026-06-08
updated: 2026-06-08
tags: [sop, dot, dq-file, driver-qualification, onboarding]
area: select-safety
department: safety
owner:
review_frequency: annual
compliance_area: driver-qualification
procedure_type: recordkeeping
dot_related: true
---

# SOP: Driver Qualification (DQ) File

**Purpose:** Define how a complete, audit-ready Driver Qualification file is assembled, stored, and maintained for every driver, so that no driver is dispatched with a missing or backdated required record.
**Scope:** All drivers operating CMVs subject to 49 CFR Part 391, from application through 3 years post-termination.
**Owner:** Safety Manager (final completeness reviewer).
**Effective date:** 2026-06-08
**Last reviewed:** 2026-06-08
**Next review:** Annual.

## Format decision (resolved)

- **Digital is the system of record.** DQ files are maintained as PDFs, one folder per driver, indexed in the order listed in [[driver-qualification-file]]. This matches the document-upload design of [[driver-onboarding-workflow]]. Paper originals that arrive (e.g., signed road-test certificate) are scanned within 2 business days; the scan is the file copy and the paper original is retained in a locked secondary store.
- **Retention: 3-year minimum, set to match insurance retention.** Statutory floor is duration of employment + 3 years (49 CFR 391.51(d)); drug/alcohol records follow Part 382 (some 5 years). Default policy: retain for the longer of the statutory minimum or the carrier's insurance-mandated retention period. Confirm the insurance number per client and record it in the client note.

## Procedure

1. **Open the file at offer/hire.** Create the driver's DQ folder and load the onboarding checklist mirroring 49 CFR 391.51 (see [[driver-qualification-file]] for the full required-contents list).
2. **Collect application + history.** Employment application per 49 CFR 391.21, including complete 3-year employment history and accident history. Reject incomplete applications back to the driver — do not file partial.
3. **Run previous-employer inquiries.** Safety-performance inquiries to all DOT-regulated employers for the prior 3 years (49 CFR 391.23(a)(2)); document date sent and response (or good-faith attempt).
4. **Pull MVR / state driving record.** Pre-employment 3-year record from each state of licensure (49 CFR 391.23(a)(1)); set the 12-month annual-review reminder (49 CFR 391.25) at the same time.
5. **Verify medical certification.** Current Medical Examiner's Certificate (49 CFR 391.41–391.45); confirm the examiner is on the NRCME at exam date; for CDL holders verify the state's electronic medical-certification status (CDLIS).
6. **Run drug & alcohol pre-employment test.** Negative pre-employment result on file before first dispatch (49 CFR 382.301); store per Part 382 retention.
7. **Run FMCSA Clearinghouse pre-employment full query.** Attach the result; schedule the annual limited query (49 CFR 382.701).
8. **Confirm road test + ELDT.** Road-test certificate or accepted equivalent (49 CFR 391.31/391.33); ELDT certificate if hired after 2022-02-07 and required (49 CFR 380 Subpart F).
9. **Safety Manager completeness review.** Verify every required item present and correctly dated, no pre-employment gaps, indexed in standard order.
10. **Release the "ready to drive" gate.** Sign-off is set only when no required field is blank. Dispatch may assign loads only after this gate is true.
11. **Maintain.** Track medical-cert expiry (alert 60 days prior), run annual MVR within the 12-month interval, run annual Clearinghouse limited query, and re-index on any addition.

## Responsibilities

- **HR / onboarding coordinator** — opens the file, requests documents, runs inquiries and queries, keeps the checklist current.
- **Safety Manager** — final completeness review and "ready to drive" sign-off; owns this SOP and its annual review.
- **Driver** — completes the application, submits to medical/drug testing, provides documentation.
- **Dispatch** — confirms "ready to drive" status before assigning any load.

## Definitions

- **DQ file** — the set of records a motor carrier must maintain per 49 CFR 391.51 for each driver.
- **Ready-to-drive gate** — the completeness sign-off that must be true before first dispatch.

## References

- [[driver-qualification-file]] — full regulatory contents list and retention detail (49 CFR 391.51)
- 49 CFR 391 — Qualifications of drivers
- 49 CFR 382 — Controlled substances and alcohol testing
- 49 CFR 380 Subpart F — ELDT
- FMCSA Clearinghouse: https://clearinghouse.fmcsa.dot.gov/
- Implements the gating dependency of [[driver-onboarding-workflow]]

## Revision history
| Date | Change | By |
|------|--------|-----|
| 2026-06-08 | Initial draft; resolved digital-vs-paper (digital = system of record) and retention (3-yr min, match insurance) | /plan-today (automated) |

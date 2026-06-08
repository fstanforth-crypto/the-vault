---
type: dot-compliance
status: active
created: 2026-06-08
updated: 2026-06-08
tags: [dot, hos, eld, short-haul, personal-conveyance, audit]
area: select-safety
compliance_area: hours-of-service
dot_related: true
review_frequency: quarterly
owner:
source: FMCSR
---

# DOT: Short-Haul Exemption & Personal-Conveyance Audit

**Regulation / FMCSR section:** 49 CFR 395.1(e) (short-haul exemption); 49 CFR 395.8 & 395.28 (ELD / records of duty status); FMCSA personal-conveyance guidance (yard moves / PC).
**Applies to:** Drivers claiming the short-haul exemption and any driver logging personal conveyance (PC).
**Effective date:** Audit opened 2026-06-08.
**Next review:** Quarterly until both exposures close.

> Source: untriaged voice memo from a fleet-manager call about ELD compliance gaps (carrier TBD), 2026-05-21. Triaged into this note on 2026-06-08.

## Summary

A fleet manager flagged two live hours-of-service exposures: (1) two drivers running on paper logs under a claimed short-haul exemption whose actual radius and duty hours have not been verified, and (2) drivers logging "personal conveyance" outside FMCSA-allowed scenarios. Both are audit-finding risks and need verification against the regulation, not assumption.

## Requirements — to verify

### Short-haul exemption (49 CFR 395.1(e))
- [ ] Confirm each of the two drivers operates **within a 150 air-mile radius** of the normal work-reporting location (395.1(e)(1)).
- [ ] Confirm each **returns to the work-reporting location and is released within 14 consecutive hours** (395.1(e)(1)).
- [ ] Confirm the carrier maintains **time records** (start/end of duty, total hours) for these drivers in lieu of ELD/RODS.
- [ ] Pull the **last 30 days of duty records** and compute actual radius and duty-hour spread per driver to confirm the exemption genuinely applies. If either driver exceeds the radius or the 14-hour window on any day, the exemption does not apply for that day and ELD/RODS were required → finding.

### Personal conveyance
- [ ] Pull PC-flagged segments for the last 30 days and test each against FMCSA PC guidance (movement for the driver's own purpose while off-duty; not enhancing operational readiness, not load-bearing toward a shipper).
- [ ] Identify misuse patterns (e.g., PC used to extend driving to a delivery, or yard-to-yard moves logged as PC).

## Corrective actions (if findings)

- [ ] Personal-conveyance **refresher training + written policy** defining permitted PC use, with driver acknowledgment.
- [ ] If short-haul math fails: move affected drivers onto ELD/RODS and document the correction date.

## Records to keep

- 30-day duty/time records pulled for the audit, with the radius/duty-hour computation per driver.
- PC-segment review worksheet.
- Training-completion and policy-acknowledgment records (per [[driver-qualification-file]] training expectations).

## Verification / audit method

Compare reported status against actual telematics/time data, not the driver's claim. A DOT auditor will check that short-haul time records exist and that PC use fits the narrow FMCSA definition.

## References

- 49 CFR 395.1(e) — Short-haul operations exemption (150 air-mile / 14-hour)
- 49 CFR 395.8, 395.28 — ELD and records of duty status
- FMCSA Personal Conveyance regulatory guidance
- Feeds the violation-aggregation need captured in [[weekly-hos-violation-digest]]
- [[DOT-Knowledge]]

## Open questions

- Which carrier? (memo says TBD — attach to the client note once identified.)
- Are the two paper-log drivers CDL or non-CDL? Affects Clearinghouse/medical interplay.

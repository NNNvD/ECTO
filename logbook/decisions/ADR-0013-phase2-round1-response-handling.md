---
permalink: /decisions/:basename
---

# ADR-0013: Phase 2 Round 1 response handling decisions

- Date: 2026-11-12
- Status: Accepted
- Decision owner: Project lead
- Related: [ADR-0012](ADR-0012-notify-experts-of-phase2-round1-item-1-correction.md), [Item 1 wording correction incident](../incidents/2026-10-22-phase2-round1-item-1-wording-correction.md)

## Context
Five experts completed the survey before the wording of Item 1 was corrected. After the invitation to revise their evaluations, three did not reply, one explicitly chose to keep their response, and one updated only their explanation.

One expert also had a complete survey response and an incomplete attempt.

## Decision
- Include all five original numeric ratings in the Item 1 analysis and use the revised explanation in the round report.
- Count the completed response once for the expert with two survey records.

## Rationale
The follow-up yielded no changes to the five numeric ratings. For the expert with two survey records, the completed record provides one eligible evaluation per item.

## Consequences
The restricted audit trail retains the original evaluations, the revised explanation, and the incomplete attempt. Explanations submitted before the correction may refer to the wording first presented.

## Alternatives considered
- Excluding all five ratings submitted before the correction was possible, but would discard the ratings retained after the opportunity to revise.
- Including both survey records was possible, but would give one expert more than one contribution for some items.

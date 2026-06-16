---
permalink: /decisions/ADR-0010-count-ratings-of-three-in-consensus-threshold
---
# ADR-0010: Count ratings of 3 in the consensus threshold

- Date: 2026-06-15
- Status: Accepted
- Decision owner: Project lead
- Related: ADR-0005; docs/projectDescription.md

## Context
The project description used inconsistent disagreement thresholds. The phase-level stopping rule allowed more than 25% of experts to rate an item below 3, while the item-level rule used a 25% threshold for ratings below 3. On the seven-point scale, a rating of 3 is labeled "Somewhat disagree," but it was not counted as disagreement under either formulation.

## Decision
Apply one consensus rule to all items, phases, and rounds:

- The item's mean rating must be at least 4.5.
- No more than 25% of valid respondents may rate the item 3 or lower.

An item that meets both conditions is designated as having reached consensus and is not reevaluated in the next round. A phase reaches consensus when every item meets this rule and no new items are proposed in the final feedback round. The maximum remains five rounds per phase.

This decision supersedes the disagreement-threshold provision in ADR-0005.

## Rationale
A rating of 3 represents "Somewhat disagree" and should therefore count toward the disagreement threshold. The revised rule is clearer, slightly more conservative, and applies the same criterion at both item and phase level. Referring to valid respondents also makes the denominator explicit when responses are missing or unusable.

## Consequences
Consensus calculations and protocol descriptions must use the proportion of valid ratings at or below 3. Under the current Phase 1 Round 1 data, seven of eight items meet the revised rule; P1_I07 does not because 2 of 7 respondents (28.6%) rated it 3 or lower.

## Alternatives considered
- Retain the 30% phase-level threshold from ADR-0005.
- Keep ratings of 3 outside the disagreement threshold.
- Use different thresholds for item-level and phase-level consensus.

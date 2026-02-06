# ADR-0005: Relax consensus rule threshold to 30%

- Date: 2026-02-02
- Status: Accepted
- Decision owner: Project lead
- Related: 

## Context
The consensus rule for Delphi-style rounds risked being too strict if a small number of outliers disagreed.

## Decision
Change the rule so that no single item receives a score < 3.0 by more than 30% of experts (previously 25%), and document the protocol for suggesting and removing items in consensus rounds.

## Rationale
Expert groups can include occasional outliers; a slightly higher threshold reduces false signals of disagreement.

## Consequences
Consensus may be reached more readily, but still requires high agreement on item scores.

## Alternatives considered
Keep the 25% threshold unchanged.

# ADR-0003: Exclude papers missing abstracts

- Date: 2026-01-07
- Status: Accepted
- Decision owner: Project lead
- Related: 

## Context
A subset of papers in Zotero did not have abstracts available.

## Decision
Exclude papers for which Zotero could not find an abstract.

## Rationale
Only 71 out of 564 papers lacked abstracts. Given the goal of identifying 10 experts and the expectation that relevant experts publish multiple papers, manually locating missing abstracts was not worth the effort.

## Consequences
Some potentially relevant papers may be missed, but screening remains feasible and focused.

## Alternatives considered
Manually search for abstracts for all missing cases.

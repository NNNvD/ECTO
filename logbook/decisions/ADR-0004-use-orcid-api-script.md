# ADR-0004: Use ORCID API script for career stage identification

- Date: 2026-01-14
- Status: Accepted
- Decision owner: Project lead
- Related: 

## Context
Author career stage needed to be classified to focus on assistant, associate, and full professors and exclude trainees or emeriti.

## Decision
Write a Python script that queries the ORCID API to identify authors with ORCID IDs and extract their job titles for screening.

## Rationale
Automating ORCID lookups reduces manual workload and provides consistent inputs for career stage filtering.

## Consequences
Requires maintaining and verifying script output; some cases still need manual review.

## Alternatives considered
Manual inspection of every author profile without automated ORCID lookups.

# Logbook guide

## What goes where
- **Daily logs**: day-to-day progress, experiments, and quick notes. Use for anything worth remembering that day.
- **Decision records (ADRs)**: durable, project-wide choices that affect direction, architecture, or long-term behavior.
- **Meeting notes**: summaries of discussions, attendees, outcomes, and action items.
- **Incidents**: outages, regressions, or operational issues that need a timeline and follow-up.

## When to create an ADR
Create an ADR when a change is:
- Long-lived or difficult to reverse.
- Affects architecture, tooling, or team workflows.
- Likely to be referenced later (why/when/how we decided).

## Recommended entry style
Use a short, descriptive heading followed by consistent bullet fields. Keep entries terse and scannable:
- Context: the situation or problem.
- What I did: the action taken.
- Result: outcome or current state.
- Links: related Issue/PR/commit.
- Follow-ups: next steps.

## Referencing GitHub items
Use GitHub-native references for easy navigation:
- Issues: `#123`
- PRs: `PR #45`
- Commits: short SHA (e.g., `abc1234`)

# Logbook guide

## What goes where
- **Daily logs**: concise record of day-to-day work, experiments, and outcomes.
- **Decision records (ADRs)**: durable, project-wide choices that affect direction, architecture, or long-term behavior.
- **Meeting notes**: summaries of discussions, attendees, outcomes, and action items.
- **Incidents**: outages, regressions, or operational issues that need a timeline and follow-up.

## Daily log style
Use `logbook/daily/YYYY-MM-DD.md` and follow `logbook/_templates/daily.md`.

- Keep Highlights concise and scannable.
- List Entries chronologically. Use the heading format `### HH:MM — Action — <short action title>`; times are in the frontmatter timezone, `Europe/Amsterdam`.
- Use the time supplied for the activity. Do not invent a time; write `Time not recorded` if none is available.
- Write completed activities in past tense. For daily-log drafting, treat work described as planned or prepared as completed unless the user explicitly says it was not completed.
- A `**Context:**` line is optional. Include it only when it helps explain why the action was taken. Put the actions performed in concise bullets below it. If context is unnecessary, omit the line and put the action bullets directly below the heading.
- Do not mention or link to pull requests in daily-log entries.
- Keep internal weekly reviews, identifying details, private correspondence, and individual survey responses out of public daily logs.

## Other log types
Use the matching template for meeting notes, ADRs, and incident reports. Include context, decisions, links, and follow-ups when relevant to that record type.

## Linking related project records
Daily logs do not include pull-request references. Other log types may link to relevant issues, ADRs, commits, or pull requests when useful.

# Log note quick start

Use this guide whenever you need to create a new log note.

## 1) Choose the right template
Templates are in `logbook/_templates/`:

- `daily.md` → `logbook/daily/YYYY-MM-DD.md`
- `meeting.md` → `logbook/meetings/YYYY-MM-DD-short-topic.md`
- `adr.md` → `logbook/decisions/ADR-XXXX-short-title.md`
- `incident.md` → place in an incidents folder (create `logbook/incidents/` if needed)

## 2) Copy a template into a new note
From the repository root:

```bash
cp logbook/_templates/daily.md logbook/daily/$(date +%F).md
```

Example for a meeting note:

```bash
cp logbook/_templates/meeting.md logbook/meetings/2026-03-17-design-review.md
```

## 3) Fill in the placeholders
Open the new file and replace template placeholders with real values:

- Title and date
- People involved
- Context, decisions, actions, and follow-ups
- Links to related issues/PRs/commits

Keep entries concise and specific so others can scan them quickly.

## 4) Add links to indexes (if applicable)
After creating a note, update `logbook/README.md` so it appears in the relevant section (Daily logs, Decisions, Meetings, or Incidents).

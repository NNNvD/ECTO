# Log note quick start

Use this guide whenever you create a log note.

## 1) Choose the right template
Templates are in `logbook/_templates/`:

- `daily.md` → `logbook/daily/YYYY-MM-DD.md`
- `meeting.md` → `logbook/meetings/YYYY-MM-DD-short-topic.md`
- `adr.md` → `logbook/decisions/ADR-XXXX-short-title.md`
- `incident.md` → `logbook/incidents/YYYY-MM-DD-short-topic.md`

## 2) Create the note
Copy the matching template and replace its placeholders. For example:

`logbook/daily/2026-10-29.md` starts from `logbook/_templates/daily.md`.

Keep the daily template's `permalink` field. It gives the note a stable public URL; Jekyll replaces `:basename` with the note's filename when it builds the site.

## 3) Write a daily log
- Add a few concise Highlights.
- Add one chronological Entry per activity, using `HH:MM — Action — <short action title>`.
- Use the user's recorded local time; do not invent times. Use `Time not recorded` if no time is available.
- Write the activity as completed, in past tense. Treat planned or prepared work as completed unless the user explicitly says it was not completed.
- Add `**Context:**` only when the reason is useful to the reader. Put completed actions in bullets below it; otherwise omit Context and put the action bullets directly under the heading.
- Do not mention or link pull requests in daily logs.
- Keep internal reviews, private correspondence, identifying information, and individual survey responses out of public daily logs.

## 4) Update the index
Do not edit `logbook/README.md` manually. The GitHub Actions workflow regenerates it from Markdown files in the logbook folders. The generator uses a note's `permalink` when present and otherwise links to Jekyll's default source-path URL. The website shows the note after the change is merged and the Pages site is deployed.

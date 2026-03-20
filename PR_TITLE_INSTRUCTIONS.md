# PR Title Instructions for Browser-Only Workflow

This project uses **release-please** to decide version bumps from commit messages that land on `main`.

When working only in GitHub browser UI, the safest approach is:

1. Use a Conventional Commit-style PR title.
2. Use **Squash and merge**.
3. In the squash merge dialog, keep or refine the generated commit title so it still follows the same format.

## Recommended PR title format

Use this structure:

- `<type>: <short description>`
- `<type>!: <short description>` for breaking changes

Examples:

- `fix: correct typo in project-description page`
- `feat: add expert inclusion decision table`
- `feat!: rename logbook metadata keys`

## Which type triggers which release bump?

- `fix:` → **patch** bump (e.g., `1.1.0` → `1.1.1`)
- `feat:` → **minor** bump (e.g., `1.1.0` → `1.2.0`)
- `feat!:` or `fix!:` (+ `BREAKING CHANGE:` in details) → **major** bump (e.g., `1.1.0` → `2.0.0`)

If multiple commit types are included in merged changes, the highest-impact bump wins (major > minor > patch).

## PR body tip for breaking changes

For breaking changes, add this line in the PR description (or final squash commit message body):

- `BREAKING CHANGE: <what changed and what users must update>`

## Quick checklist before merge

- [ ] PR title uses Conventional Commit format
- [ ] Title type matches intended release bump (`fix`, `feat`, or breaking `!`)
- [ ] Merge method is **Squash and merge**
- [ ] Final squash commit message still uses Conventional Commit format

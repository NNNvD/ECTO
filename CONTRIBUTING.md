# Contributing To ECTO

ECTO uses GitHub as its public transparency and dissemination layer. Keep private expert data, raw confidential Delphi responses, credentials, consent forms, and participant-identifying material out of the public repository unless public release has been explicitly approved.

## Branches And Pull Requests

- Work on a feature branch and open a pull request into `main`.
- Use a short descriptive branch name, for example `improve-pr-template` or `fix-site-links`.
- Do not add the `codex/` branch prefix unless Noah explicitly requests it.
- Do not push directly to `main`; the `ECTO-1` ruleset protects the branch.
- Keep pull requests focused and describe what changed, why it changed, checks run, and any public-facing, privacy, ethics, Zenodo, or release implications.

## Review Expectations

The `ECTO-1` ruleset requires pull-request review before changes land on `main`. `.github/CODEOWNERS` assigns default repository ownership to `@NNNvD` so code-owner review can be requested consistently.

## PR And Commit Titles

ECTO uses release-please, so PR titles and final squash commit titles are version-affecting metadata. Use Conventional Commit-style titles:

- `fix:` for corrections, cleanup, broken links, typos, and public-page repairs.
- `feat:` for new public documents, site sections, workflows, participant-facing materials, or meaningful additions.
- `chore:` for maintenance that should not trigger a release when appropriate.
- Use `!` or a `BREAKING CHANGE:` footer only when a major release is intended.

See `PR_TITLE_INSTRUCTIONS.md` for browser-only merge guidance.

## Automation

GitHub Actions build and deploy the public Jekyll site, run release-please, and maintain the logbook index. If a change touches workflows, release metadata, or generated index files, describe the operational impact in the PR.

## LLM And AI-Tool Disclosure

ECTO discloses project-level use of LLMs and other AI tools in the public Project Description. Do not add repeated LLM authorship or disclosure boilerplate to PR descriptions, commit messages, changelog entries, logbook entries, page footers, or individual documents unless Noah explicitly requests it. Write project changes in the project voice.

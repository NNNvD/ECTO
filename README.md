# ECTO: Theory Development Textbook

Public repository for ECTO (Theory Development Textbook). This repo contains the living source files (Quarto) and automation for building and publishing the website.

## Quick links
- Website (GitHub Pages): _TBD_
- Zenodo concept DOI (all versions): _TBD after first release_

## What’s in this repository
- `manuscript/` — Quarto book source (chapters, assets, includes)
- `.github/workflows/` — CI, GitHub Pages deployment, release automation
- `scripts/` — utility scripts (optional)

## Build locally
Prerequisites: Quarto installed.

From repo root:
- `quarto render manuscript`

Output:
- `manuscript/_book/`

## Publishing
### GitHub Pages
This repo is configured to deploy the rendered Quarto book to GitHub Pages via GitHub Actions.

Repository admin steps:
1. Go to Settings → Pages.
2. Set Source to **GitHub Actions**.

### Zenodo archival
Zenodo archives **GitHub Releases** from this repo and mints DOIs.

Repository admin steps:
1. Log in to Zenodo using GitHub.
2. In Zenodo: Profile → GitHub → toggle this repository ON → click Sync.
3. Create the first GitHub Release (e.g., `v0.1.0`). Zenodo should archive it and mint a DOI.
4. Paste the Zenodo **concept DOI** (all versions) into this README and into `CITATION.cff`.

Important:
- Zenodo’s GitHub integration archives the repository snapshot at release time. Treat large binary outputs as separate deposits.

## Versioning and releases
Releases are managed automatically using `release-please`.

Recommended practice:
- Use Conventional Commit prefixes (e.g., `feat: ...`, `fix: ...`, `docs: ...`).
- Merge PRs into `main`; `release-please` will open a release PR when needed.

## Contributing
See `CONTRIBUTING.md`.

## License
- Text/content: CC BY 4.0 (see `LICENSE-CONTENT`)
- Code (scripts/workflows): MIT (see `LICENSE-CODE`)

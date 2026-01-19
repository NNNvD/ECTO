# Codex Agent Instruction Package: ECTO GitHub Repository Setup

## Objective
Set up a public GitHub repository for the ECTO project (Theory Development Textbook), with:
- A clean, maintainable repository structure.
- Quarto Book as the default build system (HTML book output).
- GitHub Actions for CI (build on PRs) and GitHub Pages deployment (build + publish on `main`).
- Release automation via `release-please` (tags + GitHub Releases).
- Zenodo-ready metadata via `CITATION.cff` and an explicit release policy so Zenodo can archive each GitHub Release.

## Assumptions (safe defaults)
- The repository will be **public**.
- The project’s primary public artifact is a web-hosted textbook (HTML).
- Source is maintained as text files (Quarto `.qmd` + Markdown).
- Large binaries (e.g., many PDFs, large datasets) are **not** stored in the repo; they should be deposited separately (e.g., Zenodo records) and linked.

If any assumption is wrong, still complete the setup; document deviations in the README.

## Deliverables to create/commit
Create the files and folder structure included in this package (copy into the target repo). The critical paths are:
- Quarto book scaffold under `manuscript/`
- GitHub Actions workflows under `.github/workflows/`
- Project metadata: `README.md`, `LICENSE*`, `CITATION.cff`
- Contribution & governance basics: `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`

## Required steps (Codex execution plan)

### Step 1 — Place the scaffold into the repository
1. Ensure you are operating in the repository root.
2. Add the entire folder/file structure from this instruction package.
3. Ensure line endings are LF, and YAML files remain valid.

### Step 2 — Validate that Quarto renders locally (or in CI)
Run (if a shell is available):
- `quarto --version`
- `quarto render manuscript`

Expected output:
- Rendered book output appears in `manuscript/_book/`.

### Step 3 — Verify GitHub Actions workflows
Confirm the following workflows exist:
- `ci.yml` (runs on PRs and pushes; builds the book)
- `pages.yml` (runs on pushes to `main`; deploys to GitHub Pages)
- `release.yml` (runs on pushes to `main`; manages releases)

Ensure workflows are committed to default branch.

### Step 4 — Prepare repository settings (human-in-the-loop)
Codex cannot click UI buttons. Add the following instructions verbatim to the README section "Repository setup (admin)":
1. Enable GitHub Pages: Settings → Pages → Source = GitHub Actions.
2. (Recommended) Branch protection for `main`: require PR, require CI, block force-push.
3. Set repository description and topics.

### Step 5 — Configure Zenodo (human-in-the-loop)
Add the following instructions verbatim to the README section "Zenodo archival":
1. Log in to Zenodo with GitHub.
2. In Zenodo: Profile → GitHub → toggle this repo ON → Sync.
3. Create the first GitHub Release (e.g., `v0.1.0`). Zenodo should archive it and mint a DOI.
4. After DOI exists, paste the concept DOI into `README.md` and `CITATION.cff` placeholders.

### Step 6 — Open a PR (preferred) or commit directly
Preferred:
- Create a branch `repo-scaffold` and open a PR.
- Ensure CI passes.
- Merge.

Commit message suggestion:
- `chore(repo): add initial repository scaffold (Quarto + CI + Pages + releases)`

## Acceptance criteria
- `quarto render manuscript` succeeds in CI.
- GitHub Pages deploy workflow is present and ready (requires admin to enable Pages).
- Release workflow exists and would create releases after merge activity.
- Repository contains clear instructions for Zenodo linkage.

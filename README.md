# ECTO: Theory Development Textbook

ECTO is an open, community-maintained textbook and reference work on **theory development** (primarily in psychology and the broader behavioural and social sciences). The project curates methods, templates, examples, and workflows for turning theoretical ideas into **explicit specifications** that can be:

- Precisely stated (constructs, assumptions, scope conditions)
- Represented as mechanism or process descriptions (qualitative and/or formal)
- Linked to measurement and data (what would count as evidence, and how)
- Used to derive discriminating predictions and crucial tests
- Iteratively improved based on empirical and conceptual feedback

This GitHub repository is the public, living workspace for authoring ECTO and publishing it as a website. **Zenodo** is used as the archival layer for immutable, DOI-minted releases.

## Quick links

- Website (GitHub Pages): TBD
- Repository: https://github.com/NNNvD/ECTO
- Zenodo concept DOI (all versions): TBD (available after the first release)
- Latest Zenodo version DOI: TBD

## What is ECTO?

ECTO aims to make theory development more cumulative and more teachable. In many research areas, theoretical ideas are abundant but often remain underspecified: key constructs are ambiguous, assumptions are implicit, measurement links are unclear, and competing interpretations can be hard to adjudicate. ECTO addresses this by providing:

- **Procedures and checklists** that make specification steps explicit
- **Templates** that can be reused in projects, courses, and collaborations
- **Worked examples** illustrating common failure modes and stronger alternatives
- **A workflow** from idea -> specification -> formalization -> test -> revision

### Who this is for

- Researchers and students who want practical guidance on building and improving theories
- Methodologists, philosophers of science, and modelers contributing tools, critiques, and examples
- Educators who want reusable teaching materials for theory construction and evaluation

### What you will find in the book

While the scope will expand over time, ECTO is intended to cover (at minimum):

- Construct definition and conceptual clarification
- Scope conditions and auxiliary assumptions
- Mechanism mapping and process descriptions
- Formalization (computational / mathematical / simulation models where appropriate)
- Measurement and operationalization links (how theory meets data)
- Deriving hypotheses and designing crucial tests
- Theory comparison, revision, and cumulative updating

## What this repository is for

This repository is intentionally structured to support three things:

1. **A living textbook**
   - Source files for the book (Quarto / Markdown) live in this repo.
   - The rendered website is published via GitHub Pages.

2. **Open collaboration**
   - Issues and pull requests are the primary mechanism for discussion and improvement.
   - Contributions can include chapter content, examples, figures, and build/publishing improvements.

3. **Citable, immutable releases (Zenodo)**
   - When a GitHub Release is created, Zenodo archives a snapshot of the repository and mints a DOI.
   - Use the Zenodo DOI to cite a specific released version, or the concept DOI to cite ECTO in general.

### Non-goals and constraints

To keep the repository durable, legally safe, and easy to maintain, it should not contain:

- Sensitive or confidential data (including personal data not explicitly intended for publication)
- Copyright-restricted PDFs or other materials without distribution rights
- Large binary files that do not need to be versioned with the source

If you need to publish large binaries (e.g., PDFs of teaching packs, large datasets, videos), deposit them as separate Zenodo records and link to them from the relevant chapter or the README.

## Repository layout

Top-level structure (high level):

- `manuscript/` - Quarto book source
  - `index.qmd` - landing page for the book
  - `chapters/` - chapter files
  - `_quarto.yml` - book configuration
- `.github/workflows/` - automation
  - `ci.yml` - build checks on PRs/pushes
  - `pages.yml` - deploy website on `main`
  - `release.yml` - automated release management (release-please)
- `CITATION.cff` - citation metadata (update after the first Zenodo release)
- `ZENODO_SETUP.md` - short instructions for enabling the Zenodo GitHub integration
- `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md` - contribution and community guidelines
- `scripts/` - optional helper scripts

## Build and preview locally

Prerequisites:

- Install Quarto: https://quarto.org/

Build the book from the repository root:

```bash
quarto render manuscript

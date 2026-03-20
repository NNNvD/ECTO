# Scripts

Place utility scripts here (e.g., building PDFs, validating links, generating figures).

Keep scripts small, documented, and reproducible.


## Document version automation

Use `docs/versions.json` as the single source of truth for version headers in `docs/*.md`.

- `python scripts/docs_version.py list` shows tracked versions.
- `python scripts/docs_version.py set projectDescription.md 1.0.3` bumps one document and syncs all headers.
- `python scripts/docs_version.py sync` reapplies the version headers from config.

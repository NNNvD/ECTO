# Zenodo setup (GitHub integration)

## What this does
Zenodo can automatically archive GitHub Releases for a public repository and mint a DOI per release plus a concept DOI for all versions.

## Admin steps (manual)
1. Log in to Zenodo with GitHub.
2. Zenodo → Profile → GitHub.
3. Click "Sync now".
4. Toggle this repository ON.
5. Create a GitHub Release (e.g., tag `v0.1.0`).
6. Confirm the new Zenodo record exists.
7. Paste the concept DOI into `README.md` and `CITATION.cff`.

## Operational policy
- Only create a release when you want a DOI-minted, immutable snapshot.
- Keep large binaries out of GitHub; deposit them separately to Zenodo if needed.

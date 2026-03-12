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


## Changing the Release Please baseline version responsibly
If you want to move the manifest from `0.2.0` to `1.0.0`, do it intentionally and transparently:

1. Update `release-please-manifest.json` to the new baseline version.
2. Merge that change through a PR with a short rationale (e.g., "project has reached stable public workflow").
3. Ensure `README.md`/`CITATION.cff` are updated when the next real GitHub Release is created.
4. Avoid editing the manifest repeatedly; treat it as release state, not planning notes.

This change affects what Release Please considers the current released version for the next automated release calculation.

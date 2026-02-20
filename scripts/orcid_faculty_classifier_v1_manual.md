# ORCID faculty classifier (v1)
This is the “rank triage” script built for the expert-identification pipeline of the ECTO project. It enriches a table of candidate experts with ORCID IDs (when available), employment snippets, and a conservative faculty/non-faculty classification.

## What it does
Given an input CSV with one row per person, the script:
1. Extracts DOIs from the columns `First author of…` and `Last author of…` (it expects `DOI:<doi>` tokens).
2. Tries to discover an ORCID iD:
   - First via Crossref DOI metadata (best precision).
   - If that fails, via ORCID **DOI-based csv-search** (still conservative: only accept unique name matches).
3. If we have an ORCID iD, fetches `/employments` and classifies based on **current** role titles:
   - Include: assistant/associate/full professor (and Dutch variants UD/UHD/hoogleraar)
   - Exclude: postdoc/PhD/emeritus/retired
   - Unknown: everything else (including “adjunct/visiting/affiliate/honorary”)

## Files
- Script: `orcid_faculty_classifier_v1.py`

## Requirements
- Python 3.9+ recommended
- `requests` installed

Install dependencies:
```bash
python3 -m pip install --user requests
```

## Credentials (ORCID)
Set environment variables (macOS / zsh):
```bash
export ORCID_CLIENT_ID="YOUR_CLIENT_ID"
export ORCID_CLIENT_SECRET="YOUR_CLIENT_SECRET"
```
(If you want it persistent, put those lines in `~/.zshrc` and `source ~/.zshrc`.)

## Input format expectations
The script expects at least these columns:
- `Name` — formatted as `Surname, Initials`
- `First author of…` — free text that includes DOI tokens like `DOI:10.xxxx/xxxx`
- `Last author of…` — same idea

If your columns differ, update the `.get(...)` keys in `main()`.

## Run
```bash
python3 orcid_faculty_classifier_v1.py input.csv output_enriched.csv --sleep 1.0
```

**Useful knobs:**
- `--max-dois 6`  
  How many DOIs per author to try (higher = more recall, slower).
- `--sleep 1.0`  
  Increase if you hit rate limits (e.g., 1.5–2.0).
- `--orcid-find crossref_only`  
  Disable ORCID DOI search fallback (higher precision, lower recall).
- `--classify-mode current`  
  Default. Avoids excluding someone due to a *past* postdoc/PhD role.

## Output columns
Key columns in the enriched CSV:
- `ORCID` — discovered ORCID iD (may be blank)
- `ORCID_source` — `crossref_author_orcid` or `orcid_csv_search_doi_self`
- `Employment_roles_sample` — first few role@org strings
- `Suggested_decision` — Include / Exclude / Unknown
- Diagnostics:
  - `Crossref_last_http_status`, `Crossref_last_error`
  - `ORCID_search_last_http_status`, `ORCID_search_last_error`, `ORCID_search_reason`
  - `ORCID_employments_http_status`, `ORCID_employments_error`, `ORCID_employments_count`


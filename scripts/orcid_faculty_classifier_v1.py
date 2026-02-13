#!/usr/bin/env python3
"""
ORCID-based faculty classifier (v1.0)

Adds ORCID ID discovery viaV1_0 ORCID Search API (CSV search) as a fallback when
Crossref metadata does not provide an ORCID for the author.

Pipeline:
  1) Try Crossref (per DOI) to find ORCID in author metadata (best precision).
  2) If still missing, try ORCID csv-search using DOI fields:
        - doi-self:"<doi>" (preferred; relationship=self)
        - (optional) digital-object-ids:"<doi>" (broader)
     Filter candidates by surname + first initial, and accept ONLY if exactly one match.
  3) If ORCID found, fetch /employments and classify (CURRENT employments by default).

Usage:
  python3 orcid_faculty_classifier_v1.py input.csv output.csv --sleep 1.0

Env vars:
  ORCID_CLIENT_ID
  ORCID_CLIENT_SECRET
"""
import argparse
import csv
import os
import re
import sys
import time
from datetime import date
from typing import Dict, List, Optional, Tuple

import requests

DOI_RE = re.compile(r"\bDOI:([^\s|;]+)", re.IGNORECASE)

INCLUDE_KWS = [
    "assistant professor",
    "associate professor",
    "full professor",
    "professor",
    "universitair docent",
    "universitair hoofddocent",
    "hoogleraar",
]
EXCLUDE_KWS = [
    "emeritus",
    "professor emeritus",
    "retired",
    "postdoc",
    "postdoctoral",
    "post-doctoral",
    "phd candidate",
    "doctoral candidate",
    "doctoral researcher",
    "phd student",
    "doctoral student",
]
# Soft excludes -> Unknown (avoid false positives)
SOFT_EXCLUDE_KWS = [
    "visiting",
    "adjunct",
    "affiliate",
    "honorary",
]


def extract_dois(*cells: str) -> List[str]:
    dois: List[str] = []
    for cell in cells:
        if not cell:
            continue
        for m in DOI_RE.finditer(cell):
            doi = m.group(1).strip().rstrip(").,;")
            doi = doi.replace("https://doi.org/", "").replace("http://doi.org/", "")
            dois.append(doi)
    seen = set()
    out: List[str] = []
    for d in dois:
        key = d.lower()
        if key not in seen:
            out.append(d)
            seen.add(key)
    return out


def parse_surname_initials(name: str) -> Tuple[str, str]:
    if not name:
        return ("", "")
    parts = [p.strip() for p in name.split(",", 1)]
    surname = parts[0].strip()
    initials = parts[1].strip() if len(parts) > 1 else ""
    initials = re.sub(r"[^A-Za-z]", "", initials)
    return (surname, initials)


def request_with_backoff(
    session: requests.Session,
    method: str,
    url: str,
    *,
    headers=None,
    params=None,
    data=None,
    timeout=20,
    sleep_base=1.0,
    max_tries=5,
) -> requests.Response:
    tries = 0
    while True:
        tries += 1
        r = session.request(method, url, headers=headers, params=params, data=data, timeout=timeout)
        if r.status_code not in (429, 503) or tries >= max_tries:
            return r
        wait = sleep_base * (2 ** (tries - 1))
        time.sleep(min(wait, 30.0))


def get_orcid_token(
    session: requests.Session, client_id: str, client_secret: str, sandbox: bool, sleep_base: float
) -> Tuple[str, int, str]:
    token_url = "https://sandbox.orcid.org/oauth/token" if sandbox else "https://orcid.org/oauth/token"
    data = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials",
        "scope": "/read-public",
    }
    r = request_with_backoff(
        session,
        "POST",
        token_url,
        headers={"Accept": "application/json", "User-Agent": "orcid-faculty-classifier/1.0"},
        data=data,
        sleep_base=sleep_base,
    )
    if r.status_code != 200:
        snippet = (r.text or "")[:300].replace("\n", " ")
        raise RuntimeError(f"ORCID token request failed: HTTP {r.status_code} :: {snippet}")
    js = r.json()
    return js.get("access_token", ""), r.status_code, js.get("scope", "")


def crossref_get(doi: str, session: requests.Session, timeout=20, sleep_base=1.0) -> Tuple[Optional[dict], int, str]:
    url = f"https://api.crossref.org/works/{doi}"
    r = request_with_backoff(
        session,
        "GET",
        url,
        headers={
            "User-Agent": "orcid-faculty-classifier/1.0 (mailto:you@example.com)",
            "Accept": "application/json",
        },
        timeout=timeout,
        sleep_base=sleep_base,
    )
    status = r.status_code
    if status != 200:
        return None, status, (r.text or "")[:200].replace("\n", " ")
    try:
        return r.json().get("message"), status, ""
    except Exception:
        return None, status, "Crossref JSON parse error"


def match_orcid_from_crossref(message: dict, surname: str, initials: str) -> Optional[str]:
    if not message:
        return None
    authors = message.get("author") or []
    s = (surname or "").strip().lower()
    init = (initials or "").strip().lower()
    init1 = init[:1] if init else ""
    for a in authors:
        family = (a.get("family") or "").strip().lower()
        given = (a.get("given") or "").strip().lower()
        orcid = a.get("ORCID") or a.get("orcid")
        if not orcid:
            continue
        if family != s:
            continue
        if init1 and given and given[:1] != init1:
            continue
        oid = orcid.replace("https://orcid.org/", "").replace("http://orcid.org/", "").strip()
        return oid
    return None


def orcid_csv_search_by_doi(
    doi: str,
    session: requests.Session,
    token: str,
    sandbox: bool,
    sleep_base=1.0,
    timeout=20,
    relationship_self_only=True,
) -> Tuple[List[Dict[str, str]], int, str]:
    base = "https://pub.sandbox.orcid.org/v3.0" if sandbox else "https://pub.orcid.org/v3.0"
    url = f"{base}/csv-search/"
    field = "doi-self" if relationship_self_only else "digital-object-ids"
    q = f'{field}:"{doi}"'
    params = {
        "q": q,
        "fl": "orcid,given-names,family-name,credit-name,current-institution-affiliation-name,past-institution-affiliation-name",
    }
    headers = {"Accept": "text/csv", "Authorization": f"Bearer {token}", "User-Agent": "orcid-faculty-classifier/1.0"}
    r = request_with_backoff(session, "GET", url, headers=headers, params=params, timeout=timeout, sleep_base=sleep_base)
    status = r.status_code
    if status != 200:
        return [], status, (r.text or "")[:300].replace("\n", " ")
    reader = csv.DictReader((r.text or "").splitlines())
    results: List[Dict[str, str]] = []
    for row in reader:
        results.append({(k or "").strip(): (v or "").strip() for k, v in row.items()})
    return results, status, ""


def pick_unique_candidate(cands: List[Dict[str, str]], surname: str, initials: str) -> Tuple[str, str]:
    s = (surname or "").strip().lower()
    init = (initials or "").strip().lower()
    init1 = init[:1] if init else ""
    filtered: List[Dict[str, str]] = []
    for c in cands:
        fam = (c.get("family-name") or c.get("family-names") or "").strip().lower()
        giv = (c.get("given-names") or "").strip().lower()
        credit = (c.get("credit-name") or "").strip().lower()
        if fam and fam != s:
            continue
        if init1:
            if (giv and giv[:1] != init1) and (credit and credit[:1] != init1):
                continue
        filtered.append(c)
    if len(filtered) == 1:
        return filtered[0].get("orcid", "").strip(), "orcid_csv_search_doi_unique_match"
    if len(filtered) == 0:
        return "", "orcid_csv_search_doi_no_name_match"
    return "", f"orcid_csv_search_doi_ambiguous_{len(filtered)}"


def _extract_year(d: dict) -> Optional[int]:
    if not isinstance(d, dict):
        return None
    y = (d.get("year") or {}).get("value")
    try:
        return int(y) if y is not None else None
    except Exception:
        return None


def _as_employment_entry(emp: dict) -> Dict:
    role = emp.get("role-title") or emp.get("role_title") or ""
    dept = emp.get("department-name") or ""
    org_obj = emp.get("organization") or {}
    org = org_obj.get("name") or ""
    start = emp.get("start-date") or emp.get("start_date") or {}
    end = emp.get("end-date") or emp.get("end_date") or {}
    vis = emp.get("visibility") or ""
    return {
        "role_title": str(role),
        "department": str(dept),
        "organization": str(org),
        "start_year": _extract_year(start),
        "end_year": _extract_year(end),
        "visibility": str(vis),
    }


def parse_employments_payload(data: dict) -> List[Dict]:
    entries: List[Dict] = []
    if not isinstance(data, dict):
        return entries
    if "affiliation-group" in data:
        for ag in data.get("affiliation-group") or []:
            for summ in ag.get("summaries") or []:
                emp = summ.get("employment-summary")
                if emp:
                    entries.append(_as_employment_entry(emp))
        return entries
    if "group" in data:
        for g in data.get("group") or []:
            for emp in g.get("employment-summary") or []:
                entries.append(_as_employment_entry(emp))
        return entries
    if "employment-summary" in data and isinstance(data["employment-summary"], list):
        for emp in data["employment-summary"]:
            entries.append(_as_employment_entry(emp))
    return entries


def orcid_employments(
    orcid: str, session: requests.Session, token: str, sandbox: bool, timeout=20, sleep_base=1.0
) -> Tuple[List[Dict], int, str]:
    base = "https://pub.sandbox.orcid.org/v3.0" if sandbox else "https://pub.orcid.org/v3.0"
    url = f"{base}/{orcid}/employments"
    headers = {
        "Accept": "application/vnd.orcid+json",
        "Authorization": f"Bearer {token}",
        "User-Agent": "orcid-faculty-classifier/1.0",
    }
    r = request_with_backoff(session, "GET", url, headers=headers, timeout=timeout, sleep_base=sleep_base)
    status = r.status_code
    if status != 200:
        return [], status, (r.text or "")[:300].replace("\n", " ")
    try:
        data = r.json()
    except Exception:
        return [], status, "ORCID JSON parse error (non-JSON response)"
    return parse_employments_payload(data), status, ""


def classify_from_roles(roles: List[Dict], mode: str = "current") -> Tuple[str, str]:
    if not roles:
        return "Unknown", ""
    this_y = date.today().year
    if mode == "current":
        current = [
            r for r in roles if (r.get("end_year") is None) or (isinstance(r.get("end_year"), int) and r["end_year"] >= this_y)
        ]
        roles_to_use = current if current else roles
    else:
        roles_to_use = roles

    text = " | ".join([f"{r.get('role_title','')} @ {r.get('organization','')}" for r in roles_to_use]).lower()

    for kw in EXCLUDE_KWS:
        if kw in text:
            return "Exclude", kw
    for kw in SOFT_EXCLUDE_KWS:
        if kw in text:
            return "Unknown", kw
    for kw in INCLUDE_KWS:
        if kw == "professor" and "emeritus" in text:
            continue
        if kw in text:
            return "Include", kw
    return "Unknown", ""


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("input_csv")
    ap.add_argument("output_csv")
    ap.add_argument("--max-dois", type=int, default=6)
    ap.add_argument("--sleep", type=float, default=1.0)
    ap.add_argument("--sandbox", action="store_true")
    ap.add_argument("--classify-mode", choices=["current", "any"], default="current")
    ap.add_argument("--orcid-find", choices=["crossref_only", "crossref_then_orcid_doi"], default="crossref_then_orcid_doi")
    ap.add_argument("--orcid-client-id", default=os.getenv("ORCID_CLIENT_ID", ""))
    ap.add_argument("--orcid-client-secret", default=os.getenv("ORCID_CLIENT_SECRET", ""))
    args = ap.parse_args()

    if not args.orcid_client_id or not args.orcid_client_secret:
        raise SystemExit(
            "Missing ORCID credentials. Set ORCID_CLIENT_ID and ORCID_CLIENT_SECRET env vars "
            "or pass --orcid-client-id/--orcid-client-secret."
        )

    session = requests.Session()
    token, token_status, token_scope = get_orcid_token(
        session, args.orcid_client_id, args.orcid_client_secret, args.sandbox, args.sleep
    )

    with open(args.input_csv, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    out_rows: List[Dict[str, str]] = []
    for i, row in enumerate(rows, start=1):
        name = row.get("Name", "")
        surname, initials = parse_surname_initials(name)
        dois = extract_dois(row.get("First author of…", ""), row.get("Last author of…", ""))[: args.max_dois]

        found_orcid = ""
        orcid_source = ""
        crossref_checked = 0
        crossref_last_status = ""
        crossref_last_error = ""
        orcid_search_checked = 0
        orcid_search_last_status = ""
        orcid_search_last_error = ""
        orcid_search_reason = ""

        # 1) Crossref
        for doi in dois:
            msg, st, err = crossref_get(doi, session, sleep_base=args.sleep)
            crossref_checked += 1
            crossref_last_status = str(st)
            crossref_last_error = err
            oid = match_orcid_from_crossref(msg, surname, initials)
            time.sleep(args.sleep)
            if oid:
                found_orcid = oid
                orcid_source = "crossref_author_orcid"
                break

        # 2) ORCID DOI search fallback (csv-search)
        if (not found_orcid) and (args.orcid_find == "crossref_then_orcid_doi"):
            for doi in dois:
                cands, st, err = orcid_csv_search_by_doi(
                    doi, session, token, args.sandbox, sleep_base=args.sleep, relationship_self_only=True
                )
                orcid_search_checked += 1
                orcid_search_last_status = str(st)
                orcid_search_last_error = err
                if st == 200 and cands:
                    oid, reason = pick_unique_candidate(cands, surname, initials)
                    orcid_search_reason = reason
                    if oid:
                        found_orcid = oid
                        orcid_source = "orcid_csv_search_doi_self"
                        break
                time.sleep(args.sleep)

        # 3) Employments + classify
        roles: List[Dict] = []
        decision = "Unknown"
        matched = ""
        emp_status = ""
        emp_error = ""
        roles_sample = ""
        roles_count = 0

        if found_orcid:
            roles, st, err = orcid_employments(found_orcid, session, token, args.sandbox, sleep_base=args.sleep)
            emp_status = str(st)
            emp_error = err
            roles_count = len(roles)
            roles_sample = " | ".join([f"{r.get('role_title','')} @ {r.get('organization','')}" for r in roles[:5]])
            decision, matched = classify_from_roles(roles, mode=args.classify_mode)
            time.sleep(args.sleep)

        row_out = dict(row)
        row_out["ORCID"] = found_orcid
        row_out["ORCID_source"] = orcid_source
        row_out["Crossref_DOIs_checked"] = str(crossref_checked)
        row_out["Crossref_last_http_status"] = crossref_last_status
        row_out["Crossref_last_error"] = crossref_last_error
        row_out["ORCID_search_DOIs_checked"] = str(orcid_search_checked)
        row_out["ORCID_search_last_http_status"] = orcid_search_last_status
        row_out["ORCID_search_last_error"] = orcid_search_last_error
        row_out["ORCID_search_reason"] = orcid_search_reason
        row_out["ORCID_token_http_status"] = str(token_status)
        row_out["ORCID_token_scope"] = token_scope
        row_out["ORCID_employments_http_status"] = emp_status
        row_out["ORCID_employments_error"] = emp_error
        row_out["ORCID_employments_count"] = str(roles_count)
        row_out["Employment_roles_sample"] = roles_sample
        row_out["Suggested_decision"] = decision
        row_out["Matched_phrase"] = matched

        out_rows.append(row_out)

        if i % 50 == 0:
            print(f"Processed {i}/{len(rows)}", file=sys.stderr)

    if not out_rows:
        raise SystemExit("No rows found in input CSV.")

    fieldnames = list(out_rows[0].keys())
    with open(args.output_csv, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(out_rows)


if __name__ == "__main__":
    main()

from __future__ import annotations

import re
from pathlib import Path


LOGBOOK_DIR = Path("logbook")
DAILY_DIR = LOGBOOK_DIR / "daily"
DECISIONS_DIR = LOGBOOK_DIR / "decisions"
MEETINGS_DIR = LOGBOOK_DIR / "meetings"
INCIDENTS_DIR = LOGBOOK_DIR / "incidents"
README_PATH = LOGBOOK_DIR / "README.md"


HEADER = """# Logbook

"""


ADR_HEADING_RE = re.compile(r"^#\s+ADR-(\d{4}):\s*(.+)$")
ADR_DATE_RE = re.compile(r"^-\s+Date:\s*(.+)$")
ADR_STATUS_RE = re.compile(r"^-\s+Status:\s*(.+)$")


def list_markdown_files(directory: Path) -> list[Path]:
    if not directory.exists():
        return []
    return sorted([path for path in directory.iterdir() if path.suffix == ".md"])


def parse_adr_metadata(path: Path) -> dict[str, str]:
    title = ""
    adr_num = ""
    date = ""
    status = ""
    for line in path.read_text(encoding="utf-8").splitlines():
        if not title:
            heading_match = ADR_HEADING_RE.match(line)
            if heading_match:
                adr_num = heading_match.group(1)
                title = heading_match.group(2).strip()
                continue
        date_match = ADR_DATE_RE.match(line)
        if date_match:
            date = date_match.group(1).strip()
            continue
        status_match = ADR_STATUS_RE.match(line)
        if status_match:
            status = status_match.group(1).strip()
            continue
    return {
        "number": adr_num,
        "title": title,
        "date": date,
        "status": status,
        "path": str(path),
    }


def build_daily_section() -> str:
    daily_files = list_markdown_files(DAILY_DIR)
    daily_files.sort(reverse=True)
    lines = ["## Daily logs"]
    for path in daily_files:
        date = path.stem
        lines.append(f"- {date} — [{date}](daily/{path.name})")
    if len(lines) == 1:
        lines.append("- (none)")
    return "\n".join(lines)


def build_adr_section() -> str:
    adr_files = list_markdown_files(DECISIONS_DIR)
    adr_metadata = [parse_adr_metadata(path) for path in adr_files]
    adr_metadata.sort(key=lambda item: item["number"])
    lines = [
        "## Decisions (ADRs)",
        "| ADR | Title | Date | Status |",
        "|---:|---|---|---|",
    ]
    for item in adr_metadata:
        title_link = f"[{item['title']}](decisions/{Path(item['path']).name})"
        lines.append(
            f"| {item['number']} | {title_link} | {item['date']} | {item['status']} |"
        )
    if len(lines) == 3:
        lines.append("| (none) | | | |")
    return "\n".join(lines)


def build_simple_section(title: str, directory: Path, label: str) -> str:
    files = list_markdown_files(directory)
    lines = [title]
    for path in files:
        lines.append(f"- [{path.stem}]({label}/{path.name})")
    if len(lines) == 1:
        lines.append("- (none)")
    return "\n".join(lines)


def main() -> int:
    sections = [
        HEADER.strip(),
        "",
        build_daily_section(),
        "",
        build_adr_section(),
        "",
        build_simple_section("## Meetings", MEETINGS_DIR, "meetings"),
        "",
        build_simple_section("## Incidents", INCIDENTS_DIR, "incidents"),
        "",
    ]
    README_PATH.write_text("\n".join(sections).strip() + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

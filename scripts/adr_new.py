from __future__ import annotations

import argparse
import re
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


DECISIONS_DIR = Path("logbook/decisions")
TEMPLATE_PATH = Path("logbook/_templates/adr.md")
TIMEZONE = ZoneInfo("Europe/Amsterdam")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a new ADR file.")
    parser.add_argument("--title", required=True, help="Title for the ADR.")
    parser.add_argument(
        "--owner", default="Noah van Dongen", help="Decision owner."
    )
    parser.add_argument("--status", default="Accepted", help="ADR status.")
    return parser.parse_args()


def slugify(text: str) -> str:
    slug = text.lower()
    slug = re.sub(r"[^a-z0-9\s-]", "", slug)
    slug = re.sub(r"\s+", "-", slug.strip())
    slug = re.sub(r"-{2,}", "-", slug)
    return slug or "untitled"


def next_adr_number() -> int:
    DECISIONS_DIR.mkdir(parents=True, exist_ok=True)
    pattern = re.compile(r"ADR-(\d{4})-.*\.md$")
    numbers = []
    for path in DECISIONS_DIR.iterdir():
        match = pattern.match(path.name)
        if match:
            numbers.append(int(match.group(1)))
    return max(numbers, default=0) + 1


def create_adr(title: str, owner: str, status: str) -> Path:
    number = next_adr_number()
    number_str = f"{number:04d}"
    slug = slugify(title)
    filename = f"ADR-{number_str}-{slug}.md"
    path = DECISIONS_DIR / filename
    date_str = datetime.now(tz=TIMEZONE).strftime("%Y-%m-%d")
    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    rendered = (
        template.replace("{{ADR_NUM}}", number_str)
        .replace("{{TITLE}}", title)
        .replace("{{DATE}}", date_str)
        .replace("{{OWNER}}", owner)
    )
    rendered = rendered.replace("Status: Accepted", f"Status: {status}")
    path.write_text(rendered, encoding="utf-8")
    return path


def main(args: argparse.Namespace) -> int:
    path = create_adr(args.title, args.owner, args.status)
    print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(parse_args()))

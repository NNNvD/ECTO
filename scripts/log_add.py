from __future__ import annotations

import argparse
from typing import Optional

from logbook_utils import ensure_daily_log, now_in_timezone


ENTRY_TEMPLATE = """### {time} — {entry_type} — {title}
- Context: {context}
- What I did: {what_i_did}
- Result: {result}
- Links: {links}
- Follow-ups: {followups}
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Append an entry to today's logbook daily file."
    )
    parser.add_argument(
        "--type",
        dest="entry_type",
        default="Action",
        choices=["Action", "Decision", "Meeting", "Risk", "Blocked", "Release"],
    )
    parser.add_argument("--title", required=True, help="Short entry title.")
    parser.add_argument("--links", default="", help="Related links or references.")
    parser.add_argument("--context", default="", help="Context for the entry.")
    parser.add_argument("--result", default="", help="Result or outcome.")
    parser.add_argument(
        "--followups", default="", help="Follow-up actions or reminders."
    )
    return parser.parse_args()


def append_entry(
    entry_type: str,
    title: str,
    links: str = "",
    context: str = "",
    result: str = "",
    followups: str = "",
    date_override: Optional[str] = None,
) -> str:
    info = ensure_daily_log(date_override)
    time_str = now_in_timezone().strftime("%H:%M")
    entry = ENTRY_TEMPLATE.format(
        time=time_str,
        entry_type=entry_type,
        title=title,
        context=context,
        what_i_did="",
        result=result,
        links=links,
        followups=followups,
    )
    content = info.path.read_text(encoding="utf-8").rstrip()
    content = f"{content}\n\n{entry}"
    info.path.write_text(content, encoding="utf-8")
    return str(info.path)


def main(args: argparse.Namespace) -> int:
    path = append_entry(
        entry_type=args.entry_type,
        title=args.title,
        links=args.links,
        context=args.context,
        result=args.result,
        followups=args.followups,
    )
    print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(parse_args()))

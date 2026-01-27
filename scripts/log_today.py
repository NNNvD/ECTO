from __future__ import annotations

import argparse
from typing import Optional

from logbook_utils import ensure_daily_log


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create or ensure today's daily log file exists."
    )
    parser.add_argument(
        "--date",
        dest="date",
        help="Create or ensure a specific date (YYYY-MM-DD).",
    )
    return parser.parse_args()


def main(date_override: Optional[str] = None) -> int:
    info = ensure_daily_log(date_override)
    print(info.path)
    return 0


if __name__ == "__main__":
    args = parse_args()
    raise SystemExit(main(args.date))

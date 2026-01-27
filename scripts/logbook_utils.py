from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


LOGBOOK_DIR = Path("logbook")
DAILY_DIR = LOGBOOK_DIR / "daily"
DECISIONS_DIR = LOGBOOK_DIR / "decisions"
TEMPLATES_DIR = LOGBOOK_DIR / "_templates"
TIMEZONE = ZoneInfo("Europe/Amsterdam")


@dataclass(frozen=True)
class DailyLogInfo:
    date: str
    time: str
    path: Path


def now_in_timezone() -> datetime:
    return datetime.now(tz=TIMEZONE)


def build_daily_info(date_override: str | None = None) -> DailyLogInfo:
    now = now_in_timezone()
    date_str = date_override or now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M")
    path = DAILY_DIR / f"{date_str}.md"
    return DailyLogInfo(date=date_str, time=time_str, path=path)


def ensure_daily_log(date_override: str | None = None) -> DailyLogInfo:
    info = build_daily_info(date_override)
    info.path.parent.mkdir(parents=True, exist_ok=True)
    if not info.path.exists():
        template_path = TEMPLATES_DIR / "daily.md"
        template = template_path.read_text(encoding="utf-8")
        rendered = (
            template.replace("{{DATE}}", info.date).replace("{{TIME}}", info.time)
        )
        info.path.write_text(rendered, encoding="utf-8")
    return info

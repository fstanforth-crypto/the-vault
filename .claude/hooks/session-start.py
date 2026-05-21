#!/usr/bin/env python3
"""
SessionStart hook.

Runs once when a Claude Code session begins in the vault. Computes a tiny
status report (inbox count, active programs, safety docs past review) and
returns it as additionalContext so Claude is grounded before the first prompt.

Stdlib only. Silent on error.
"""
import json
import re
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent.parent


def read_frontmatter(p: Path) -> dict:
    try:
        text = p.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return {}
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    fm = {}
    for line in text[4:end].splitlines():
        m = re.match(r"^([a-z_]+):\s*(.*)$", line)
        if m:
            fm[m.group(1)] = m.group(2).strip()
    return fm


def parse_date(s: str):
    if not s:
        return None
    try:
        return datetime.strptime(s, "%Y-%m-%d").date()
    except Exception:
        return None


def review_window_days(freq: str) -> int:
    f = (freq or "").strip().lower()
    return {
        "weekly": 7,
        "monthly": 30,
        "quarterly": 90,
        "semi-annual": 182,
        "annual": 365,
        "biennial": 730,
    }.get(f, 0)


def main() -> int:
    today = date.today()

    raw_dir = VAULT / "06-inbox" / "raw-notes"
    raw_count = sum(1 for x in raw_dir.iterdir() if x.is_file()) if raw_dir.exists() else 0

    active_programs = []
    pdir = VAULT / "02-programs-systems" / "active-programs"
    if pdir.exists():
        for f in pdir.rglob("*.md"):
            fm = read_frontmatter(f)
            if fm.get("status") not in ("archived", "released"):
                active_programs.append((f.stem, fm.get("next_action", "")))

    stale_safety = []
    sdir = VAULT / "01-select-safety"
    if sdir.exists():
        for f in sdir.rglob("*.md"):
            fm = read_frontmatter(f)
            freq = fm.get("review_frequency")
            window = review_window_days(freq)
            if not window:
                continue
            updated = parse_date(fm.get("updated"))
            if not updated:
                continue
            if (today - updated).days > window:
                stale_safety.append(f.stem)

    today_md = VAULT / "00-command-center" / "Today.md"
    today_updated = parse_date(read_frontmatter(today_md).get("updated")) if today_md.exists() else None
    today_fresh = today_updated == today

    lines = [
        f"# Vault status (auto, {today.isoformat()})",
        "",
        f"- Inbox raw notes: **{raw_count}**",
        f"- Active programs: **{len(active_programs)}**",
        f"- Safety docs past review_frequency: **{len(stale_safety)}**",
        f"- Today.md refreshed today: **{'yes' if today_fresh else 'no'}**",
        "",
    ]

    if active_programs[:5]:
        lines.append("**Active program next-actions:**")
        for name, na in active_programs[:5]:
            lines.append(f"- [[{name}]] — {na or '(no next_action set)'}")
        lines.append("")

    if stale_safety[:5]:
        lines.append("**Stale safety docs (top 5):**")
        for name in stale_safety[:5]:
            lines.append(f"- [[{name}]]")
        lines.append("")

    if raw_count and not today_fresh:
        lines.append("Suggested first move: `/plan-today` then `/process-inbox`.")
    elif not today_fresh:
        lines.append("Suggested first move: `/plan-today`.")
    elif raw_count:
        lines.append(f"Suggested first move: `/process-inbox` ({raw_count} item(s) waiting).")

    context = "\n".join(lines)

    output = {
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": context,
        }
    }
    sys.stdout.write(json.dumps(output))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        sys.exit(0)

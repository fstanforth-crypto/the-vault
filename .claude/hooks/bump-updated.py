#!/usr/bin/env python3
"""
PostToolUse hook for Write/Edit/MultiEdit.

When Claude edits a markdown note inside the vault that has YAML frontmatter,
this script automatically updates (or inserts) the `updated:` field with today's
date. No-ops for files outside the vault, templates, or files without frontmatter.

Safe by design:
- Never touches body content.
- Atomic write (temp + rename) to avoid corruption.
- No external deps — stdlib only.
- Silent on errors (returns 0) so we never block a real edit.
"""
import json
import os
import re
import sys
import tempfile
from datetime import date
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent.parent


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0

    tool_input = payload.get("tool_input", {}) or {}
    file_path = tool_input.get("file_path")
    if not file_path:
        return 0

    p = Path(file_path)
    if not p.is_absolute():
        p = (VAULT / p).resolve()

    try:
        p.relative_to(VAULT)
    except ValueError:
        return 0

    if p.suffix != ".md" or not p.exists():
        return 0

    # Skip templates — they intentionally contain {{date}} placeholders.
    parts = p.relative_to(VAULT).parts
    if parts and parts[0] == "07-templates":
        return 0
    # Skip hidden / system paths.
    if any(seg.startswith(".") for seg in parts):
        return 0

    try:
        text = p.read_text(encoding="utf-8")
    except Exception:
        return 0

    if not text.startswith("---\n"):
        return 0

    end = text.find("\n---\n", 4)
    if end == -1:
        end = text.find("\n---", 4)
        if end == -1:
            return 0
        body_start = end + 4
    else:
        body_start = end + 5

    front = text[4:end]
    today = date.today().isoformat()

    new_front, n = re.subn(
        r"(?m)^updated:.*$", f"updated: {today}", front, count=1
    )
    if n == 0:
        # Insert after `created:` if present, else at the top of frontmatter.
        if re.search(r"(?m)^created:", new_front):
            new_front = re.sub(
                r"(?m)^(created:.*)$", r"\1\nupdated: " + today, new_front, count=1
            )
        else:
            new_front = f"updated: {today}\n" + new_front

    if new_front == front:
        return 0

    new_text = f"---\n{new_front}\n---\n{text[body_start:]}"
    if new_text == text:
        return 0

    try:
        fd, tmp_path = tempfile.mkstemp(dir=str(p.parent), prefix=".upd-", suffix=".tmp")
        with os.fdopen(fd, "w", encoding="utf-8") as tmp:
            tmp.write(new_text)
        os.replace(tmp_path, p)
    except Exception:
        try:
            os.unlink(tmp_path)
        except Exception:
            pass
        return 0

    return 0


if __name__ == "__main__":
    sys.exit(main())

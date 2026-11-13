#!/usr/bin/env python3
"""Generate knowledge activity data from Markdown + Git history.

Reads eligible article pages under docs/, parses YAML frontmatter, and uses
Git history to determine first introduction and last update for each article.
Writes a validated JSON contract to docs/static/data/knowledge-activity.json.

Counting rules (see docs/organization/activity-and-interaction-system.md):
  1. Include published Markdown article pages under docs/.
  2. Exclude _nav.md, templates/, landing index.md pages, and non-published files.
  3. Treat index.md landing pages separately from ordinary articles.
  4. Map articles to the eight top-level sections using repository paths.
  5. Avoid double-counting aliases or navigation references.
  6. Use the actual build/publication structure to determine eligible pages.
  7. Distinguish draft / review / approved / missing status without inventing approval.
  8. Do not treat last_reviewed as a creation date.
  9. Ignore placeholder dates such as YYYY-MM-DD.
  10. For recent additions, use Git history to identify first introduction.
  11. For recently updated articles, use the latest relevant Git change.
  12. Handle renames explicitly via git log --follow.
"""

from __future__ import annotations

import json
import re
import subprocess
from datetime import datetime, timedelta, timezone
from pathlib import Path

try:
    import yaml  # provided by mkdocs runtime
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("PyYAML is required to run this script: pip install pyyaml") from exc

ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = ROOT / "docs"
OUTPUT_FILE = DOCS_DIR / "static" / "data" / "knowledge-activity.json"
WINDOW_DAYS = 30
SCHEMA_VERSION = 1

# Top-level section roots mapped from docs/ paths to section keys.
SECTION_ROOTS = {
    "academy": "academy",
    "projects": "projects",
    "workshop": "workshop",
    "assets": "assets",
    "technology": "technology",
    "research": "research",
    "safety": "safety",
    "organization": "organization",
}

STATUS_LABELS = {
    "draft": "draft",
    "review": "review",
    "approved": "approved",
}


def run_git(args: list[str]) -> str:
    result = subprocess.run(
        ["git", "-C", str(ROOT), *args],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.strip()


def is_excluded(path: Path) -> bool:
    """Return True if the Markdown file should not count as an eligible article."""
    name = path.name
    # Non-published / navigation-only files.
    if name == "_nav.md":
        return True
    # Landing pages are index.md at the root of a section; docs/index.md is homepage.
    if name == "index.md":
        return True
    # Templates are source-only reference documents, not published articles.
    parts = path.relative_to(DOCS_DIR).parts
    if "templates" in parts:
        return True
    return False


def parse_frontmatter(path: Path) -> dict:
    """Extract YAML frontmatter from a Markdown file, or return {}."""
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        return {}
    try:
        data = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError:
        return {}
    return data if isinstance(data, dict) else {}


def section_for(path: Path) -> str | None:
    """Map a docs/ path to its top-level section key, or None."""
    parts = path.relative_to(DOCS_DIR).parts
    if not parts:
        return None
    return SECTION_ROOTS.get(parts[0])


def git_first_commit(path: Path) -> str | None:
    """Earliest commit date that introduced this file (follows renames)."""
    rel = path.relative_to(ROOT).as_posix()
    output = run_git(["log", "--follow", "--diff-filter=A", "--format=%ad", "--date=iso-strict", "--", rel])
    if not output:
        return None
    dates = [line for line in output.splitlines() if line]
    return dates[-1] if dates else None


def git_last_commit(path: Path) -> str | None:
    """Most recent commit date that touched this file (follows renames)."""
    rel = path.relative_to(ROOT).as_posix()
    output = run_git(["log", "--follow", "--format=%ad", "--date=iso-strict", "-1", "--", rel])
    return output or None


def iso_to_date(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def is_placeholder_date(value: str | None) -> bool:
    if not value:
        return True
    return value.strip() == "YYYY-MM-DD" or not re.match(r"\d{4}-\d{2}-\d{2}", value.strip())


def build_inventory() -> dict:
    now = datetime.now(timezone.utc)
    window_start = now - timedelta(days=WINDOW_DAYS)

    eligible: list[dict] = []
    sections: dict[str, dict] = {
        key: {
            "key": key,
            "name": key.upper(),
            "total": 0,
            "new": 0,
            "updated": 0,
            "status": {"draft": 0, "review": 0, "approved": 0, "missing": 0},
        }
        for key in SECTION_ROOTS
    }

    for md_file in sorted(DOCS_DIR.rglob("*.md")):
        if not md_file.is_file():
            continue
        if is_excluded(md_file):
            continue
        sec_key = section_for(md_file)
        if sec_key is None:
            continue

        meta = parse_frontmatter(md_file)
        status = str(meta.get("status", "missing")).lower()
        if status not in STATUS_LABELS:
            status = "missing"

        first_date = iso_to_date(git_first_commit(md_file))
        last_date = iso_to_date(git_last_commit(md_file))

        # last_reviewed is NOT a creation date; ignore placeholder dates.
        last_reviewed = meta.get("last_reviewed")
        if is_placeholder_date(last_reviewed):
            last_reviewed = None

        is_new = first_date is not None and first_date >= window_start
        is_updated = last_date is not None and last_date >= window_start

        entry = {
            "path": md_file.relative_to(DOCS_DIR).as_posix(),
            "title": meta.get("title") or md_file.stem.replace("-", " ").title(),
            "category": str(meta.get("category", "General")).strip() or "General",
            "status": status,
            "section": sec_key,
            "first_introduced": first_date.isoformat() if first_date else None,
            "last_updated": last_date.isoformat() if last_date else None,
            "last_reviewed": last_reviewed.isoformat() if last_reviewed else None,
            "is_new": is_new,
            "is_updated": is_updated,
        }
        eligible.append(entry)

        sec = sections[sec_key]
        sec["total"] += 1
        sec["status"][status] += 1
        if is_new:
            sec["new"] += 1
        if is_updated:
            sec["updated"] += 1

    # Stable ordering: by path.
    eligible.sort(key=lambda e: e["path"])

    total_articles = len(eligible)
    new_articles = sum(1 for e in eligible if e["is_new"])
    updated_articles = sum(1 for e in eligible if e["is_updated"])

    # Recent activity: up to 5 most recently added or updated eligible articles.
    activity_candidates = [
        e for e in eligible if e["is_new"] or e["is_updated"]
    ]
    activity_candidates.sort(
        key=lambda e: e["last_updated"] or e["first_introduced"] or "",
        reverse=True,
    )
    recent_activity = []
    for e in activity_candidates[:5]:
        activity_type = "Added" if e["is_new"] and not e["is_updated"] else "Updated"
        date_value = e["last_updated"] if e["is_updated"] else e["first_introduced"]
        recent_activity.append({
            "title": e["title"],
            "section": e["section"],
            "activity_type": activity_type,
            "date": date_value,
            "path": e["path"],
        })

    return {
        "schema_version": SCHEMA_VERSION,
        "generated_at": now.isoformat(),
        "window_days": WINDOW_DAYS,
        "total_articles": total_articles,
        "new_articles": new_articles,
        "updated_articles": updated_articles,
        "sections": [sections[key] for key in SECTION_ROOTS],
        "recent_activity": recent_activity,
        "articles": eligible,
    }


def main() -> int:
    data = build_inventory()
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        f"Generated {OUTPUT_FILE}: "
        f"{data['total_articles']} articles, "
        f"{data['new_articles']} new / {data['updated_articles']} updated in last {WINDOW_DAYS} days."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

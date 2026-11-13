#!/usr/bin/env python3
"""Validate the generated activity data structure and values."""
import json
import sys
from pathlib import Path

def main():
    path = Path("docs/static/data/knowledge-activity.json")
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        print("ERROR: Failed to load activity data: %s" % exc)
        return 1

    print("=" * 60)
    print("Activity Data Validation")
    print("=" * 60)

    print("\n1. Schema version: %s" % data.get("schema_version"))
    print("2. Window days: %s" % data.get("window_days"))

    total = data.get("total_articles", 0)
    new_articles = data.get("new_articles", 0)
    updated_articles = data.get("updated_articles", 0)
    print("\n3. Page counts:")
    print("   Total articles: %d" % total)
    print("   New articles (30 days): %d" % new_articles)
    print("   Updated articles (30 days): %d" % updated_articles)

    print("\n4. Section breakdown:")
    for section in data.get("sections", []):
        print("   %-12s total=%-3d new=%-3d updated=%-3d status=%s" % (
            section.get("key"),
            section.get("total", 0),
            section.get("new", 0),
            section.get("updated", 0),
            section.get("status", {})
        ))

    activities = data.get("recent_activity", [])
    print("\n5. Recent activity (%d entries):" % len(activities))
    for i, activity in enumerate(activities, 1):
        print("   %2d. %-40r %-8s %s" % (
            i,
            activity.get("title"),
            activity.get("activity_type"),
            activity.get("date")
        ))

    calculated_total = len(data.get("articles", []))
    print("\n6. Consistency check:")
    print("   Total articles (computed): %d" % calculated_total)
    print("   Total articles (reported): %d" % total)
    if calculated_total == total:
        print("   [OK] Totals match")
    else:
        print("   [FAIL] Totals MISMATCH")

    print("\n7. Required fields check:")
    required = ["path", "title", "category", "status", "section",
                "first_introduced", "last_updated", "is_new", "is_updated"]
    missing_fields = []
    for article in data.get("articles", []):
        for field in required:
            if field not in article:
                missing_fields.append("%s: %s" % (article.get("path", "?"), field))

    if missing_fields:
        print("   [FAIL] Missing fields in %d articles:" % len(missing_fields))
        for f in missing_fields[:5]:
            print("      - %s" % f)
    else:
        print("   [OK] All required fields present")

    print("\n8. Page sizes:")
    import os
    site_dir = Path("site")
    html_files = list(site_dir.rglob("*.html"))
    total_size = sum(f.stat().st_size for f in html_files)
    print("   Total HTML size: %.1f KB" % (total_size / 1024))
    print("   HTML files: %d" % len(html_files))

    print("\n9. Static assets:")
    static_dir = site_dir / "static"
    css_files = list(static_dir.rglob("*.css"))
    js_files = list(static_dir.rglob("*.js"))
    print("   CSS files: %d" % len(css_files))
    print("   JS files: %d" % len(js_files))
    for css in css_files:
        print("      %s: %.1f KB" % (css.relative_to(site_dir), css.stat().st_size / 1024))

    print("\n" + "=" * 60)
    print("Validation complete")
    print("=" * 60)
    return 0

if __name__ == "__main__":
    sys.exit(main())

"""Pull live AccuKnox LinkedIn org post performance directly from the LinkedIn API
(day-of-week and format breakdown) for the content-strategy decision engine.

Usage: uv run python skills/linkedin_post_digital_twin/scripts/li_performance_baseline.py [--since 2026-01-01]

Notes:
- Only urn:li:share:* post ids return real stats from organizationalEntityShareStatistics
  (ugcPost ids return nothing - a LinkedIn API limitation, not a bug here).
- Format is read from the post's `content` field, not a stored column - see classify_format().
- Filters impressions >= 100 to cut single-digit-impression noise before averaging.
- This hits the live API on every run (paginated posts list + one stats call per post,
  8-way concurrency) - prefer this over the cached Marketing Analytics Master Sheet
  when asked for a "best day/format to post" recommendation.
"""
import argparse
import asyncio
import datetime as dt
import json
import sys
from collections import defaultdict

sys.path.insert(0, "/work")
sys.path.insert(0, "/work/skills/marketing_analytics_master/scripts")
from pull_detail import li_get, ORG_ENC, LI_HDR_REST  # noqa: E402


def classify_format(post):
    content = post.get("content")
    if content is None:
        return "text"
    if "media" in content:
        mid = content["media"].get("id", "")
        if "video" in mid:
            return "video"
        if "document" in mid:
            return "document"
        return "image"
    if "article" in content:
        return "article (link)"
    if "multiImage" in content or "carousel" in content:
        return "carousel/multi-image"
    if "poll" in content:
        return "poll"
    if "reference" in content:
        return "repost"
    return "other"


async def list_posts(max_pages=10, limit=100):
    all_posts, start = [], 0
    for _ in range(max_pages):
        posts, _ = await li_get(
            f"https://api.linkedin.com/rest/posts?q=author&author={ORG_ENC}"
            f"&count={limit}&start={start}&sortBy=LAST_MODIFIED",
            hdr=LI_HDR_REST,
        )
        page = posts.get("elements", [])
        all_posts.extend(page)
        if len(page) < limit:
            break
        start += limit
    return all_posts


async def fetch_stats(urn):
    urn_enc = urn.replace(":", "%3A")
    st, _ = await li_get(
        "https://api.linkedin.com/v2/organizationalEntityShareStatistics?q=organizationalEntity"
        f"&organizationalEntity={ORG_ENC}&shares=List({urn_enc})"
    )
    els = st.get("elements", [])
    if not els:
        return 0, 0.0
    s = els[0].get("totalShareStatistics", {})
    return s.get("impressionCount", 0), round(s.get("engagement", 0) * 100, 2)


async def main(since_str):
    since = dt.datetime.fromisoformat(since_str)
    posts = await list_posts()
    targets = []
    for p in posts:
        urn = p.get("id", "")
        if "share" not in urn:
            continue
        created = p.get("createdAt")
        if not created:
            continue
        d = dt.datetime.fromtimestamp(created / 1000, tz=dt.timezone.utc).replace(tzinfo=None)
        if d < since:
            continue
        targets.append((p, d))

    sem = asyncio.Semaphore(8)
    results = []

    async def fetch(p, d):
        async with sem:
            impr, eng = await fetch_stats(p["id"])
        results.append({"date": d, "format": classify_format(p), "impr": impr, "eng": eng})

    await asyncio.gather(*(fetch(p, d) for p, d in targets))
    good = [r for r in results if r["impr"] >= 100]

    print(f"Fetched {len(results)} share-posts since {since_str}; {len(good)} usable (impr>=100)\n")

    by_day = defaultdict(list)
    for r in good:
        by_day[r["date"].strftime("%A")].append(r)
    print("--- By day of week ---")
    for day, items in sorted(by_day.items(), key=lambda kv: -sum(i["eng"] for i in kv[1]) / len(kv[1])):
        avg_impr = sum(i["impr"] for i in items) / len(items)
        avg_eng = sum(i["eng"] for i in items) / len(items)
        print(f"{day:10s} n={len(items):3d}  avg_impr={avg_impr:7.0f}  avg_eng={avg_eng:5.2f}%")

    by_fmt = defaultdict(list)
    for r in good:
        by_fmt[r["format"]].append(r)
    print("\n--- By format ---")
    for fmt, items in sorted(by_fmt.items(), key=lambda kv: -sum(i["eng"] for i in kv[1]) / len(kv[1])):
        avg_impr = sum(i["impr"] for i in items) / len(items)
        avg_eng = sum(i["eng"] for i in items) / len(items)
        print(f"{fmt:22s} n={len(items):3d}  avg_impr={avg_impr:7.0f}  avg_eng={avg_eng:5.2f}%")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--since", default="2026-01-01")
    args = ap.parse_args()
    asyncio.run(main(args.since))

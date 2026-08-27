"""Schedule AccuKnox social posts through Zernio.

Reads a campaign markdown file, then schedules every post onto a fixed number
of slots per day. Unlike the vault version, nothing publishes immediately:
the whole run is scheduled, starting from --start.

    python .claude/skills/accuknox-social-campaign/post.py plan <file>
    python .claude/skills/accuknox-social-campaign/post.py send <file> --live
    python .claude/skills/accuknox-social-campaign/post.py sync-media <file> --live
    python .claude/skills/accuknox-social-campaign/post.py list
    python .claude/skills/accuknox-social-campaign/post.py cancel <post_id> --live

Dry run is the default everywhere. Nothing leaves the machine without --live.
See README.md in this folder for the full SOP.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import uuid
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
ENV = Path(r"D:\Atharva\NOTES\.env")
LEDGER = Path(__file__).with_name("_sent.tsv")
API = "https://zernio.com/api/v1"
IST = timezone(timedelta(hours=5, minutes=30))

# Two slots a day, 12 hours apart.
# 07:30 IST catches the APAC morning, 19:30 IST catches the US morning.
SLOTS = [(7, 30), (19, 30)]

# The AccuKnox profile inside the Zernio workspace. The same API key also
# reaches Atharva's Personal profile, so every lookup in this repo is pinned
# to this ID. Nothing here can post to a personal account.
PROFILE_ID = "6a7ebc0ab7c6776815670114"
PROFILE_NAME = "AccuKnox"

# The AccuKnox X account is Premium, so the free-tier 280 cap does not apply.
# This is a sanity ceiling, not the platform limit.
LIMITS = {"twitter": 4000}

# Zernio's own media storage auto-deletes after this many days. A post
# scheduled further out than that publishes with a dead image link.
MEDIA_TTL_DAYS = 7


# --------------------------------------------------------------------------- io


def api_key() -> str:
    for line in ENV.read_text(encoding="utf-8").splitlines():
        if line.startswith("ZERNIO_API_KEY="):
            return line.split("=", 1)[1].strip()
    sys.exit(f"ZERNIO_API_KEY is missing from {ENV}")


def call(method: str, path: str, key: str, body: dict | None = None) -> dict:
    """Shell out to curl, because this machine's Python has an expired CA root."""
    cmd = ["curl", "-s", "-X", method, f"{API}{path}",
           "-H", f"Authorization: Bearer {key}",
           "-H", f"x-request-id: {uuid.uuid4()}"]
    if body is not None:
        cmd += ["-H", "Content-Type: application/json", "-d", json.dumps(body)]
    raw = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8").stdout
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {"_error": "unparseable response", "_raw": raw[:400]}


def upload(local: Path, key: str) -> str:
    """Push a local file to Zernio and return its temporary public URL."""
    raw = subprocess.run(
        ["curl", "-s", "-X", "POST", f"{API}/media/upload-direct",
         "-H", f"Authorization: Bearer {key}", "-F", f"file=@{local}"],
        capture_output=True, text=True, encoding="utf-8").stdout
    try:
        return json.loads(raw)["url"]
    except (json.JSONDecodeError, KeyError):
        sys.exit(f"upload failed for {local.name}: {raw[:300]}")


def media_url(spec: str, key: str) -> str:
    """An http(s) spec passes straight through. A local path gets uploaded.

    Passing a public URL through matters: Zernio-hosted media expires after
    7 days, a help.accuknox.com URL does not.
    """
    if spec.startswith("http://") or spec.startswith("https://"):
        return spec
    return upload(resolve(spec), key)


def resolve(spec: str) -> Path:
    """Absolute paths are used as-is, relative ones hang off the repo root."""
    p = Path(spec)
    return p if p.is_absolute() else REPO / p


def profile_of(a: dict) -> str:
    p = a.get("profileId")
    return (p or {}).get("_id", "") if isinstance(p, dict) else (p or "")


def account_id(key: str, platform: str, username: str) -> str:
    """Select inside the AccuKnox profile only, then match the username.

    Two X accounts answer this API key: AccuKnox and Atharva's personal
    cultist_dev. Selecting the first enabled match would post to the personal
    one. Both filters have to pass, so a wrong account is an error rather
    than a silent mis-send.
    """
    everything = call("GET", "/accounts", key).get("accounts", [])
    if not everything:
        sys.exit("Zernio returned no accounts. Check ZERNIO_API_KEY.")
    scoped = [a for a in everything
              if a.get("platform") == platform and a.get("enabled")
              and profile_of(a) == PROFILE_ID]
    for a in scoped:
        if (a.get("username") or "").lower() == username.lower():
            return a["_id"]
    names = ", ".join(a.get("username", "?") for a in scoped) or "none"
    sys.exit(f"no enabled {platform} account named {username!r} in the "
             f"{PROFILE_NAME} profile. In that profile: {names}")


# ----------------------------------------------------------------------- parsing


def parse(path: Path) -> list[dict]:
    """Split a campaign file into posts.

    Posts are separated by a line containing only ---. A post may end with
    `media:` and `alt:` lines, which are stripped from the text and attached
    as an image instead.
    """
    body = path.read_text(encoding="utf-8").split("---\n", 2)[2]
    posts = []
    for block in body.split("\n\n---\n\n"):
        block = block.strip()
        if not block:
            continue
        text, media, alt = [], None, None
        for line in block.split("\n"):
            if line.startswith("media:"):
                media = line.split(":", 1)[1].strip()
            elif line.startswith("alt:"):
                alt = line.split(":", 1)[1].strip()
            else:
                text.append(line)
        posts.append({"text": "\n".join(text).strip(), "media": media, "alt": alt})
    return posts


def schedule_times(count: int, start: str | None) -> list[datetime]:
    """The next `count` slots, beginning on `start` or tomorrow."""
    if start:
        day = datetime.strptime(start, "%Y-%m-%d").date()
    else:
        day = (datetime.now(IST) + timedelta(days=1)).date()
    now = datetime.now(IST)
    out = []
    while len(out) < count:
        for hh, mm in SLOTS:
            when = datetime(day.year, day.month, day.day, hh, mm, tzinfo=IST)
            if when > now + timedelta(minutes=5) and len(out) < count:
                out.append(when)
        day += timedelta(days=1)
    return out


def check(posts: list[dict], platform: str) -> None:
    limit = LIMITS.get(platform)
    for i, p in enumerate(posts, 1):
        if limit and len(p["text"]) > limit:
            sys.exit(f"post {i} is {len(p['text'])} chars, over the {platform} limit of {limit}")
        if "http://" in p["text"] or "https://" in p["text"]:
            sys.exit(f"post {i} contains a link, and this campaign is link-free")
        if p["media"] and not p["media"].startswith("http"):
            f = resolve(p["media"])
            if not f.is_file():
                sys.exit(f"post {i} points at a missing file: {f}")


# ---------------------------------------------------------------------- commands


def cmd_plan(args, key: str) -> tuple[list[dict], list[datetime]]:
    posts = parse(resolve(args.file))
    check(posts, args.platform)
    times = schedule_times(len(posts), args.start)
    cutoff = datetime.now(IST) + timedelta(days=MEDIA_TTL_DAYS)

    print(f"profile: {PROFILE_NAME} ({PROFILE_ID})")
    print(f"account: {args.account} on {args.platform}\n")
    print(f"{'#':>3}  {'when (IST)':<18} {'chars':>5}  {'img':<9}  text")
    print("-" * 100)
    at_risk = 0
    for i, p in enumerate(posts, 1):
        when = times[i - 1]
        if not p["media"]:
            img = "."
        elif p["media"].startswith("http"):
            img = "url"
        elif when > cutoff:
            img = "UPLOAD!"
            at_risk += 1
        else:
            img = "upload"
        first = p["text"].replace("\n", " ")[:44]
        print(f"{i:>3}  {when.strftime('%a %d %b %H:%M'):<18} {len(p['text']):>5}  {img:<9}  {first}")

    n_img = sum(1 for p in posts if p["media"])
    print(f"\n{len(posts)} posts, {n_img} with an image.")
    if at_risk:
        print(f"\n  {at_risk} uploaded images fire after the {MEDIA_TTL_DAYS} day media TTL "
              f"and will publish dead.\n  Re-run sync-media within {MEDIA_TTL_DAYS} days of those slots.")
    return posts, times


def cmd_send(args, key: str) -> None:
    posts, times = cmd_plan(args, key)
    if not args.live:
        print("\nDRY RUN. Nothing sent. Add --live to schedule.")
        return

    acct = account_id(key, args.platform, args.account)
    rows = []
    print("\nScheduling...\n")
    for i, p in enumerate(posts, 1):
        when = times[i - 1]
        payload = {"content": p["text"],
                   "platforms": [{"platform": args.platform, "accountId": acct}],
                   "scheduledFor": when.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                   "timezone": "Asia/Kolkata"}
        if p["media"]:
            item = {"type": "image", "url": media_url(p["media"], key)}
            if p["alt"]:
                item["altText"] = p["alt"]
            payload["mediaItems"] = [item]
        res = call("POST", "/posts", key, payload)
        post = res.get("post") or res
        pid = post.get("_id")
        label = when.strftime("%a %d %b %H:%M")
        print(f"  {i:<3} {'ok  ' if pid else 'FAIL'} {label:<18} {pid or json.dumps(res)[:160]}")
        rows.append((str(i), "ok" if pid else "FAIL", pid or "", label))

    LEDGER.touch()
    with LEDGER.open("a", encoding="utf-8") as f:
        if LEDGER.stat().st_size == 0:
            f.write("run\taccount\tn\tstatus\tpost_id\twhen\n")
        stamp = datetime.now(IST).strftime("%Y-%m-%dT%H:%M")
        for r in rows:
            f.write(stamp + "\t" + args.account + "\t" + "\t".join(r) + "\n")
    print(f"\nLedger: {LEDGER}")


def cmd_sync_media(args, key: str) -> None:
    """Attach images to posts that are already scheduled, matched on exact text."""
    posts = parse(resolve(args.file))
    check(posts, args.platform)
    ours = accuknox_account_ids(key)
    queued = {p.get("content"): p for p in call("GET", "/posts?limit=200", key).get("posts", [])
              if p.get("status") == "scheduled" and is_ours(p, ours)}

    wanted = [p for p in posts if p["media"] and not p["media"].startswith("http")]
    todo = [p for p in wanted if p["text"] in queued]
    for p in wanted:
        if p["text"] not in queued:
            print(f"  skip (not scheduled): {p['text'][:50]}")
    for p in todo:
        print(f"  {queued[p['text']]['_id']}  <- {Path(p['media']).name}")
    if not args.live:
        print(f"\nDRY RUN. {len(todo)} posts would get a fresh image. Add --live to apply.")
        return

    print()
    for p in todo:
        pid = queued[p["text"]]["_id"]
        item = {"type": "image", "url": upload(resolve(p["media"]), key)}
        if p["alt"]:
            item["altText"] = p["alt"]
        res = call("PUT", f"/posts/{pid}", key, {"mediaItems": [item]})
        got = (res.get("post") or res).get("mediaItems") or []
        print(f"  {pid}  {'ok' if got else 'FAIL ' + json.dumps(res)[:160]}")


def accuknox_account_ids(key: str) -> set[str]:
    """Every account id under the AccuKnox profile, across platforms."""
    return {a["_id"] for a in call("GET", "/accounts", key).get("accounts", [])
            if profile_of(a) == PROFILE_ID}


def is_ours(post: dict, ours: set[str]) -> bool:
    """/accounts returns accountId as a string, /posts populates it into an
    object. Handle both rather than trusting one shape."""
    for pl in post.get("platforms", []):
        a = pl.get("accountId")
        aid = a.get("_id") if isinstance(a, dict) else a
        if aid in ours:
            return True
    return False


def cmd_list(args, key: str) -> None:
    ours = accuknox_account_ids(key)
    posts = [p for p in call("GET", "/posts?limit=200", key).get("posts", [])
             if is_ours(p, ours)]
    for p in sorted(posts, key=lambda x: x.get("scheduledFor") or ""):
        when = (p.get("scheduledFor") or "")[:16].replace("T", " ")
        img = "img" if p.get("mediaItems") else "   "
        print(f"{p['_id']}  {p.get('status',''):<10} {when:<17} {img}  "
              f"{(p.get('content') or '')[:46].replace(chr(10),' ')}")
    print(f"\n{len(posts)} posts.")


def cmd_cancel(args, key: str) -> None:
    if not args.live:
        print(f"DRY RUN. Would delete {args.post_id}. Add --live to delete.")
        return
    print(json.dumps(call("DELETE", f"/posts/{args.post_id}", key))[:300])


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("plan", "send", "sync-media"):
        s = sub.add_parser(name)
        s.add_argument("file", help="path to the campaign markdown")
        s.add_argument("--platform", default="twitter")
        s.add_argument("--account", default="AccuKnox",
                       help="platform username to post as, matched exactly")
        s.add_argument("--start", help="first posting day, YYYY-MM-DD. Defaults to tomorrow.")
        s.add_argument("--live", action="store_true")
    sub.add_parser("list")
    s = sub.add_parser("cancel")
    s.add_argument("post_id")
    s.add_argument("--live", action="store_true")

    args = ap.parse_args()
    key = api_key()
    {"plan": cmd_plan, "send": cmd_send, "sync-media": cmd_sync_media,
     "list": cmd_list, "cancel": cmd_cancel}[args.cmd](args, key)


if __name__ == "__main__":
    main()

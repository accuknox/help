"""Schedule AccuKnox LinkedIn posts through Zernio.

Reads a campaign markdown file where every post carries its own date and time,
then schedules each one onto the AccuKnox LinkedIn company page. Unlike the X
script beside it, slots are never auto-assigned: a LinkedIn campaign is a dated
editorial calendar, so every post states its own `when:`.

    py -3.11 .claude/skills/accuknox-linkedin-post/li.py plan <file>
    py -3.11 .claude/skills/accuknox-linkedin-post/li.py tags <file>
    py -3.11 .claude/skills/accuknox-linkedin-post/li.py send <file> --live
    py -3.11 .claude/skills/accuknox-linkedin-post/li.py sync-media <file> --live
    py -3.11 .claude/skills/accuknox-linkedin-post/li.py list
    py -3.11 .claude/skills/accuknox-linkedin-post/li.py cancel <post_id> --live

Dry run is the default everywhere. Nothing leaves the machine without --live.
See README.md in this folder for the full SOP.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import time
import sys
import uuid
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
ENV = Path(r"D:\Atharva\NOTES\.env")
LEDGER = Path(__file__).with_name("_sent.tsv")
API = "https://zernio.com/api/v1"
IST = timezone(timedelta(hours=5, minutes=30))

# The AccuKnox profile inside the Zernio workspace. The same API key also
# reaches Atharva's Personal profile, which holds a personal X account and a
# personal YouTube. Every lookup here is pinned to this ID, so nothing in this
# script can post anywhere but AccuKnox.
PROFILE_ID = "6a7ebc0ab7c6776815670114"
PROFILE_NAME = "AccuKnox"

# Verified live on 2026-09-18 against GET /accounts.
LINKEDIN_ACCOUNT_ID = "6a80942677555aae01131b68"
LINKEDIN_USERNAME = "AccuKnox"
ORG_URN = "urn:li:organization:14651364"

# LinkedIn truncates the body at roughly 210 characters behind "see more",
# and hard-caps a post at 3000. The soft target is the one that matters.
HARD_CAP = 3000
SOFT_TARGET = 1300
TRUNCATE_AT = 210

# Zernio's own media storage auto-deletes after this many days. A post
# scheduled further out than that publishes with a dead image.
MEDIA_TTL_DAYS = 7

URL_RE = re.compile(r"https?://")
HASHTAG_LINE_RE = re.compile(r"^\s*#\w[\w-]*(\s+#\w[\w-]*)*\s*$")

# The standard AccuKnox leadership roster, appended to the end of every post.
# Copied verbatim from the two posts published on 2026-09-16, which are the
# reference for this line. Pre-resolved, so building it costs no API call.
#
# Barun Acharya is NOT in this list. He appears in the two 2026-09-16 posts and
# was removed on Atharva's instruction, 2026-09-18. Do not add him back.
#
# Rahul Jadhav ships as PLAIN TEXT and is deliberately first. His profile is
# in.linkedin.com/in/rahul-jadhav-a0485310, confirmed from AccuKnox's own post
# linking to it. LinkedIn's URL-to-URN endpoint refuses that exact profile
# across every variant tried on 2026-09-18, with no reason given.
#
# Two OTHER profiles do resolve, /in/rahuljadhav and /in/rahul-jadhav, and
# neither is the AccuKnox CTO. Rahul Jadhav is a common name. Never substitute
# one of those URNs to make the tag clickable, because that tags a stranger on
# the company page. A plain name reads correctly and is the safe failure.
ROSTER = [
    ("Rahul Jadhav", None),
    ("Brian Laing", "urn:li:person:1_hyf_Kkj2"),
    ("Phil Porras", "urn:li:person:NRO9pOGMwC"),
    ("Nat Natraj", "urn:li:person:eMG-5lrxYG"),
    ("Raj Panchapakesan", "urn:li:person:wa6BAPBF-Z"),
    ("Saqib Syed", "urn:li:person:BxZyI5TInj"),
    ("Raghuram Madabushi", "urn:li:person:8NzWZ_xnj9"),
    ("Sunil Sapra", "urn:li:person:SJaMyws9at"),
    ("Rajeev Punetha", "urn:li:person:d0l9fqc1oO"),
    ("John Kirch", "urn:li:person:Z_29xCBYO-"),
    ("Vineel Kurumella", "urn:li:person:OMl-GgumFD"),
    ("Parthasarathy Thulasi", "urn:li:person:5DaNU4amLg"),
    ("Syed Hadi", "urn:li:person:3pITlsoPHn"),
    ("Atharva Shah", "urn:li:person:vgNIoB5fbg"),
]


def roster_line() -> str:
    return " ".join(n if u is None else f"@[{n}]({u})" for n, u in ROSTER)


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


def mention(key: str, url: str, display: str) -> dict:
    """Resolve a LinkedIn profile or company URL to a Zernio mention token.

    A company page resolves for anyone. A person resolves only when the
    AccuKnox page can see them, so a non-follower comes back without a
    mentionFormat and has to ship as plain text.

    Retried three times, because the endpoint returns a transient error often
    enough to matter. Observed on 2026-09-18: a company page that resolves
    cleanly on retry failed once in a batch. Without the retry, a blip during
    `send` silently downgrades a real tag to plain text on a live post.
    """
    for attempt in range(3):
        raw = subprocess.run(
            ["curl", "-s", "-G", f"{API}/accounts/{LINKEDIN_ACCOUNT_ID}/linkedin-mentions",
             "--data-urlencode", f"url={url}", "--data-urlencode", f"displayName={display}",
             "-H", f"Authorization: Bearer {key}",
             "-H", f"x-request-id: {uuid.uuid4()}"],
            capture_output=True, text=True, encoding="utf-8").stdout
        try:
            got = json.loads(raw)
        except json.JSONDecodeError:
            got = {}
        if got.get("mentionFormat"):
            return got
        if attempt < 2:
            time.sleep(2)
    return got


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


def account_id(key: str) -> str:
    """Confirm the pinned LinkedIn account is still the AccuKnox one.

    The ID is hard-coded because it is stable, but it is re-checked against the
    live account list every run. An ID that no longer sits under the AccuKnox
    profile is an error rather than a silent mis-send.
    """
    everything = call("GET", "/accounts", key).get("accounts", [])
    if not everything:
        sys.exit("Zernio returned no accounts. Check ZERNIO_API_KEY.")
    for a in everything:
        if a["_id"] != LINKEDIN_ACCOUNT_ID:
            continue
        if a.get("platform") != "linkedin":
            sys.exit(f"account {LINKEDIN_ACCOUNT_ID} is {a.get('platform')}, not linkedin")
        if profile_of(a) != PROFILE_ID:
            sys.exit(f"account {LINKEDIN_ACCOUNT_ID} has moved out of the "
                     f"{PROFILE_NAME} profile. Refusing to post.")
        if (a.get("username") or "").lower() != LINKEDIN_USERNAME.lower():
            sys.exit(f"account {LINKEDIN_ACCOUNT_ID} is now "
                     f"{a.get('username')!r}, not {LINKEDIN_USERNAME!r}")
        if not a.get("enabled"):
            sys.exit("the AccuKnox LinkedIn account is disabled in Zernio")
        return a["_id"]
    sys.exit(f"account {LINKEDIN_ACCOUNT_ID} is gone from this Zernio workspace")


# ----------------------------------------------------------------------- parsing

FIELDS = ("when", "comment", "media", "alt", "tag", "roster")


def parse(path: Path) -> list[dict]:
    """Split a campaign file into posts.

    Everything after the frontmatter is split on a line containing only ---.
    Inside a block, these trailing key lines are pulled out of the body:

        when:    2026-09-18 19:30        (IST, required)
        comment: Register here: https://...   (the auto first comment)
        media:   references/img/a.jpg    (public URL or repo-relative path)
        alt:     alt text for the image
        tag:     Nat Natraj | https://www.linkedin.com/in/natrajiitb

    `tag:` repeats, once per person or company. Every other key appears once.
    """
    raw = path.read_text(encoding="utf-8")
    body = raw.split("---\n", 2)[2] if raw.startswith("---\n") else raw
    posts = []
    for block in re.split(r"\n-{3,}\n", body):
        block = block.strip()
        if not block:
            continue
        text, meta, tags = [], {}, []
        for line in block.split("\n"):
            head = line.split(":", 1)[0].strip().lower()
            if head == "tag" and ":" in line:
                val = line.split(":", 1)[1].strip()
                name, _, url = val.partition("|")
                tags.append({"name": name.strip(), "url": url.strip()})
            elif head in FIELDS and ":" in line:
                meta[head] = line.split(":", 1)[1].strip()
            else:
                text.append(line)
        posts.append({"text": "\n".join(text).strip(),
                      "when": meta.get("when"),
                      "comment": meta.get("comment"),
                      "media": meta.get("media"),
                      "alt": meta.get("alt"),
                      "roster": (meta.get("roster", "yes").strip().lower()
                                 not in ("no", "false", "off")),
                      "tags": tags})
    return posts


def compose(text: str, extra: str, roster: bool) -> str:
    """Put the tag lines where the live posts put them: after the body, before
    the hashtags. A trailing hashtag-only line is lifted, the tags go in, then
    the hashtags go back on the end."""
    lines = text.split("\n")
    tail = ""
    while lines and not lines[-1].strip():
        lines.pop()
    if lines and HASHTAG_LINE_RE.match(lines[-1]):
        tail = lines.pop().strip()
    body = "\n".join(lines).rstrip()

    for block in (extra, roster_line() if roster else "", tail):
        if block:
            body += "\n\n" + block
    return body


def when_of(p: dict, i: int) -> datetime:
    if not p["when"]:
        sys.exit(f"post {i} has no `when:` line. Every LinkedIn post states its own date.")
    try:
        naive = datetime.strptime(p["when"], "%Y-%m-%d %H:%M")
    except ValueError:
        sys.exit(f"post {i} has when: {p['when']!r}, expected `YYYY-MM-DD HH:MM` in IST")
    return naive.replace(tzinfo=IST)


def check(posts: list[dict]) -> None:
    """Fail on anything that would publish wrong, warn on anything merely weak."""
    now = datetime.now(IST)
    seen = set()
    for i, p in enumerate(posts, 1):
        when = when_of(p, i)
        if when < now:
            sys.exit(f"post {i} is scheduled for {p['when']}, which is in the past")
        if p["when"] in seen:
            sys.exit(f"post {i} collides with an earlier post at {p['when']}")
        seen.add(p["when"])
        full = compose(p["text"], "", p["roster"])
        if len(full) > HARD_CAP:
            sys.exit(f"post {i} is {len(full)} chars with the roster line, "
                     f"over LinkedIn's {HARD_CAP} cap")
        if URL_RE.search(p["text"]):
            sys.exit(f"post {i} has a link in the body. Links go in `comment:`, "
                     f"because a link in the caption suppresses reach.")
        if p["media"] and not p["media"].startswith("http"):
            f = resolve(p["media"])
            if not f.is_file():
                sys.exit(f"post {i} points at a missing file: {f}")
        if p["comment"] and not URL_RE.search(p["comment"]):
            print(f"  warn: post {i} has a first comment with no link in it")


# ---------------------------------------------------------------------- commands


def cmd_plan(args, key: str) -> tuple[list[dict], list[datetime]]:
    posts = parse(resolve(args.file))
    check(posts)
    times = [when_of(p, i) for i, p in enumerate(posts, 1)]
    cutoff = datetime.now(IST) + timedelta(days=MEDIA_TTL_DAYS)

    print(f"profile: {PROFILE_NAME} ({PROFILE_ID})")
    print(f"account: {LINKEDIN_USERNAME} on linkedin ({LINKEDIN_ACCOUNT_ID})")
    print(f"org:     {ORG_URN}\n")
    print(f"roster:  {len(ROSTER)} people, "
          f"{sum(1 for _, u in ROSTER if u is None)} as plain text "
          f"({len(roster_line())} raw chars)\n")
    print(f"{'#':>3}  {'when (IST)':<18} {'body':>5} {'sent':>5} {'img':<9} {'c1':<3} "
          f"{'R':<2} {'tags':>4}  hook")
    print("-" * 110)
    at_risk = no_media = no_comment = long_hook = 0
    for i, p in enumerate(posts, 1):
        when = times[i - 1]
        if not p["media"]:
            img, no_media = "MISSING!", no_media + 1
        elif p["media"].startswith("http"):
            img = "url"
        elif when > cutoff:
            img, at_risk = "UPLOAD!", at_risk + 1
        else:
            img = "upload"
        c1 = "yes" if p["comment"] else "NO!"
        if not p["comment"]:
            no_comment += 1
        hook = p["text"].replace("\n", " ")[:40]
        if len(p["text"].split("\n\n")[0]) > TRUNCATE_AT:
            long_hook += 1
        sent = len(compose(p["text"], "", p["roster"]))
        print(f"{i:>3}  {when.strftime('%a %d %b %H:%M'):<18} {len(p['text']):>5} "
              f"{sent:>5} {img:<9} {c1:<3} {'yes' if p['roster'] else 'NO':<2} "
              f"{len(p['tags']):>4}  {hook}")

    over = sum(1 for p in posts if len(p["text"]) > SOFT_TARGET)
    print(f"\n{len(posts)} posts. {over} over the {SOFT_TARGET} char soft target.")
    if no_media:
        print(f"  {no_media} posts have no image. Image posts outperform text-only.")
    if no_comment:
        print(f"  {no_comment} posts have no first comment, so their link goes nowhere.")
    if long_hook:
        print(f"  {long_hook} posts open with a first paragraph over {TRUNCATE_AT} chars, "
              f"so the hook is cut off behind 'see more'.")
    if at_risk:
        print(f"  {at_risk} uploaded images fire after the {MEDIA_TTL_DAYS} day media TTL "
              f"and will publish dead.\n  Re-run sync-media within {MEDIA_TTL_DAYS} days of those slots.")
    return posts, times


def cmd_tags(args, key: str) -> None:
    """Resolve every `tag:` in the file and print what will and will not render."""
    posts = parse(resolve(args.file))
    cache: dict[str, dict] = {}
    bad = 0
    for i, p in enumerate(posts, 1):
        if not p["tags"]:
            continue
        print(f"post {i}  {p['when']}")
        for t in p["tags"]:
            if t["url"] not in cache:
                cache[t["url"]] = mention(key, t["url"], t["name"])
            d = cache[t["url"]]
            fmt = d.get("mentionFormat")
            if fmt:
                print(f"    ok    {t['name']:<26} {fmt}")
            else:
                bad += 1
                print(f"    FAIL  {t['name']:<26} {t['url']}")
        print()
    if bad:
        print(f"{bad} tags did not resolve. A company page always resolves. A person "
              f"resolves only when the AccuKnox page can see them, so ship an "
              f"unresolved person as plain text and say so.")


def tag_line(key: str, tags: list[dict], cache: dict) -> tuple[str, list[str]]:
    """Build the trailing @mention line. Returns the line and the names that failed."""
    parts, failed = [], []
    for t in tags:
        if t["url"] not in cache:
            cache[t["url"]] = mention(key, t["url"], t["name"])
        fmt = cache[t["url"]].get("mentionFormat")
        if fmt:
            parts.append(fmt)
        else:
            failed.append(t["name"])
    return " ".join(parts), failed


def cmd_send(args, key: str) -> None:
    posts, times = cmd_plan(args, key)
    if not args.live:
        print("\nDRY RUN. Nothing sent. Add --live to schedule.")
        return

    acct = account_id(key)
    cache: dict[str, dict] = {}
    rows = []
    print("\nScheduling...\n")
    for i, p in enumerate(posts, 1):
        when = times[i - 1]
        line, failed = tag_line(key, p["tags"], cache)
        content = compose(p["text"], line, p["roster"])
        if failed:
            print(f"  {i:<3} note unresolved tags shipped as plain text: {', '.join(failed)}")

        platform = {"platform": "linkedin", "accountId": acct}
        if p["comment"]:
            platform["platformSpecificData"] = {"firstComment": p["comment"]}
        payload = {"content": content,
                   "platforms": [platform],
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
            f.write(stamp + "\tlinkedin/AccuKnox\t" + "\t".join(r) + "\n")
    print(f"\nLedger: {LEDGER}")
    print("Verify the first comment landed: run `list`, then open one post in Zernio.")


def cmd_sync_media(args, key: str) -> None:
    """Attach images to posts that are already scheduled, matched on exact text."""
    posts = parse(resolve(args.file))
    check(posts)
    ours = accuknox_account_ids(key)
    queued = {p.get("content"): p for p in call("GET", "/posts?limit=200", key).get("posts", [])
              if p.get("status") == "scheduled" and is_ours(p, ours)}

    wanted = [p for p in posts if p["media"] and not p["media"].startswith("http")]
    todo = []
    for p in wanted:
        hit = next((c for c in queued if c.startswith(p["text"][:200])), None)
        if hit:
            todo.append((p, queued[hit]["_id"]))
        else:
            print(f"  skip (not scheduled): {p['text'][:50]}")
    for p, pid in todo:
        print(f"  {pid}  <- {Path(p['media']).name}")
    if not args.live:
        print(f"\nDRY RUN. {len(todo)} posts would get a fresh image. Add --live to apply.")
        return

    print()
    for p, pid in todo:
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
    posts = [p for p in call("GET", "/posts?limit=200", key).get("posts", [])
             if any((pl.get("accountId", {}) or {}).get("_id", pl.get("accountId"))
                    == LINKEDIN_ACCOUNT_ID for pl in p.get("platforms", []))]
    for p in sorted(posts, key=lambda x: x.get("scheduledFor") or ""):
        when = (p.get("scheduledFor") or "")[:16].replace("T", " ")
        img = "img" if p.get("mediaItems") else "   "
        c1 = "c1" if any((pl.get("platformSpecificData") or {}).get("firstComment")
                         for pl in p.get("platforms", [])) else "  "
        print(f"{p['_id']}  {p.get('status',''):<10} {when:<17} {img} {c1}  "
              f"{(p.get('content') or '')[:42].replace(chr(10),' ')}")
    print(f"\n{len(posts)} posts on the AccuKnox LinkedIn page.")


def cmd_cancel(args, key: str) -> None:
    if not args.live:
        print(f"DRY RUN. Would delete {args.post_id}. Add --live to delete.")
        return
    print(json.dumps(call("DELETE", f"/posts/{args.post_id}", key))[:300])


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("plan", "send", "sync-media", "tags"):
        s = sub.add_parser(name)
        s.add_argument("file", help="path to the campaign markdown")
        s.add_argument("--live", action="store_true")
    sub.add_parser("list")
    s = sub.add_parser("cancel")
    s.add_argument("post_id")
    s.add_argument("--live", action="store_true")

    args = ap.parse_args()
    key = api_key()
    {"plan": cmd_plan, "send": cmd_send, "sync-media": cmd_sync_media,
     "tags": cmd_tags, "list": cmd_list, "cancel": cmd_cancel}[args.cmd](args, key)


if __name__ == "__main__":
    main()

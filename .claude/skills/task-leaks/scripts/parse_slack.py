#!/usr/bin/env python3
"""Pre-filter saved Slack channel dumps into open-task candidates.

Input : one or more text files that slack_read_channel saved (or pasted text).
Output: JSON list of candidate messages with the signals Claude needs to judge them.

Usage:
  python parse_slack.py --days 70 --now 2026-10-16 FILE [FILE ...]
  python parse_slack.py --days 70 --channel solution-engineering FILE [FILE ...]

The script never decides that a task is blocked. It drops noise (bots, chatter,
messages with a human thread reply) and keeps the rest with signals. Claude reads
the survivors and makes the call.
"""
import argparse
import datetime as dt
import json
import re
import sys

HDR = re.compile(
    r"=== Message from (?P<name>[^(<]+?)\s*(?:<(?P<email>[^>]+)>)?\s*\((?P<uid>[A-Z0-9]+)\) "
    r"at (?P<when>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) IST ===",
)
CHAN = re.compile(r"Channel: #(?P<name>[\w\-]+) \((?P<id>[A-Z0-9]+)\)")
MENTION = re.compile(r"<@(?P<uid>[UW][A-Z0-9]+)(?:\|(?P<name>[^>]+))?>")
THREAD = re.compile(r"Thread: (?P<n>\d+) repl(?:y|ies)(?: \(latest: (?P<latest>[^)]+)\))?")

ASK = re.compile(
    r"\?|\b(please|pls|can you|could you|need|needs|require|waiting|pending|follow[- ]?up|"
    r"update|status|share|send|confirm|review|approve|approval|check|provide|let us know|"
    r"let me know|kindly|action|todo|to-do|deadline|by (eod|tomorrow|monday|friday)|asap|urgent)\b",
    re.I,
)
ACK_REACTIONS = {"white_check_mark", "heavy_check_mark", "ballot_box_with_check", "+1", "thumbsup",
                 "eyes", "raised_hands", "saluting_face", "ok_hand"}


def parse(text, channel_hint=None):
    chan = CHAN.search(text)
    channel = chan.group("name") if chan else channel_hint or "unknown"
    marks = list(HDR.finditer(text))
    out = []
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(text)
        body = text[m.end():end].strip()
        ts = re.search(r"Message TS: (\S+)", body)
        body = re.sub(r"^Message TS: \S+\s*", "", body)
        thread = THREAD.search(body)
        reactions = re.search(r"^Reactions: (.+)$", body, re.M)
        files = re.search(r"^Files: (.+)$", body, re.M)
        clean = re.split(r"\n(?:Thread:|Reactions:|Files:)", body)[0].strip()
        out.append({
            "channel": channel,
            "author": m.group("name").strip(),
            "uid": m.group("uid"),
            "email": m.group("email"),
            "when": dt.datetime.strptime(m.group("when"), "%Y-%m-%d %H:%M:%S"),
            "ts": ts.group(1) if ts else None,
            "text": clean,
            "replies": int(thread.group("n")) if thread else 0,
            "latest_reply": thread.group("latest") if thread else None,
            "reactions": reactions.group(1) if reactions else "",
            "files": files.group(1) if files else "",
            "mentions": [(x.group("uid"), x.group("name")) for x in MENTION.finditer(clean)],
            "is_bot": m.group("uid").startswith("B") or not m.group("email"),
        })
    return out


def flag(msgs, cutoff, now):
    """Attach signals. msgs are newest-first, as Slack returns them."""
    by_time = sorted(msgs, key=lambda x: x["when"])
    res = []
    for msg in by_time:
        if msg["when"] < cutoff or msg["is_bot"]:
            continue
        if re.search(r"has (joined|left) the channel", msg["text"]) or "notes.granola.ai/t/" in msg["text"]:
            continue
        later = [x for x in by_time if x["when"] > msg["when"] and x["channel"] == msg["channel"]]
        mentioned = {u for u, _ in msg["mentions"]}
        inline_reply_from_mentioned = [x["author"] for x in later if x["uid"] in mentioned]
        # any human reply by someone other than the author after it, within 3 days
        horizon = msg["when"] + dt.timedelta(days=3)
        nearby = [x["author"] for x in later
                  if not x["is_bot"] and x["uid"] != msg["uid"] and x["when"] <= horizon]
        react_names = set(re.findall(r"([a-z0-9_+\-]+)(?:::[a-z\-0-9]+)? \(\d+\)", msg["reactions"]))
        asks = bool(ASK.search(msg["text"])) or bool(msg["mentions"])
        res.append({
            "channel": msg["channel"],
            "ts": msg["ts"],
            "when": msg["when"].strftime("%Y-%m-%d %H:%M"),
            "age_days": (now - msg["when"]).days,
            "author": msg["author"],
            "mentions": [n or u for u, n in msg["mentions"]],
            "text": msg["text"][:600],
            "thread_replies": msg["replies"],
            "latest_reply": msg["latest_reply"],
            "reactions": msg["reactions"],
            "soft_ack_reaction": bool(react_names & ACK_REACTIONS),
            "mentioned_person_posted_later": inline_reply_from_mentioned[:3],
            "other_humans_posted_within_3d": sorted(set(nearby))[:5],
            "looks_like_ask": asks,
            "tier": ("A" if asks and msg["replies"] == 0 and not inline_reply_from_mentioned
                     else "B" if msg["replies"] > 0 and asks
                     else "C"),
        })
    return res


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--days", type=int, default=70)
    ap.add_argument("--now", help="YYYY-MM-DD, defaults to today")
    ap.add_argument("--channel", help="channel name if the file has no header")
    ap.add_argument("--tiers", default="AB", help="tiers to keep, default AB")
    a = ap.parse_args()
    now = dt.datetime.strptime(a.now, "%Y-%m-%d") if a.now else dt.datetime.now()
    cutoff = now - dt.timedelta(days=a.days)
    allm = []
    for f in a.files:
        raw = open(f, encoding="utf-8").read()
        try:  # slack_read_channel saves {"messages": "..."} JSON
            raw = json.loads(raw).get("messages", raw)
        except (ValueError, AttributeError):
            pass
        allm += parse(raw, a.channel)
    cands = [c for c in flag(allm, cutoff, now) if c["tier"] in a.tiers]
    # oldest first: the oldest leak is the loudest one
    cands.sort(key=lambda c: c["when"])
    json.dump(cands, sys.stdout, indent=1, ensure_ascii=False)
    print(f"\n# parsed={len(allm)} candidates={len(cands)}", file=sys.stderr)


if __name__ == "__main__":
    main()

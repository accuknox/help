"""Firecrawl helper. Burns key slots in order (1 -> 6), skips a slot on 'Insufficient credits'.

Usage:
  python fc.py scrape <url> [--max N]          # print page markdown (truncated to N chars, default 15000)
  python fc.py search "<query>" [--limit N]    # print title, url, snippet per result
  python fc.py map <url> [--search term]       # list site URLs
"""
import json, subprocess, sys, re, os

ENV = r"D:\Atharva\NOTES\.env"
STATE = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".fc_slot")


def keys():
    out = {}
    for line in open(ENV, encoding="utf-8"):
        m = re.match(r"FIRECRAWL_API_KEY_(\d)=\s*\"?([^\"\s]+)", line)
        if m:
            out[int(m.group(1))] = m.group(2)
    return [out[k] for k in sorted(out)]


def start_slot():
    try:
        return int(open(STATE).read().strip())
    except Exception:
        return 0


def post(key, endpoint, payload, timeout):
    r = subprocess.run(
        ["curl", "-s", "-m", str(timeout), "-X", "POST", f"https://api.firecrawl.dev/v2/{endpoint}",
         "-H", f"Authorization: Bearer {key}", "-H", "Content-Type: application/json",
         "-d", json.dumps(payload)],
        capture_output=True, text=True, encoding="utf-8", errors="replace")
    return r.stdout or r.stderr


def call(endpoint, payload, timeout=120):
    import time
    ks = keys()
    for attempt in range(12):
        base = start_slot()
        if base >= len(ks):
            return {"success": False, "error": "all Firecrawl slots exhausted"}
        # Primary slot first. On a rate limit only, spill this one request to the next slots.
        for i in range(base, len(ks)):
            body = post(ks[i], endpoint, payload, timeout)
            low = body.lower()[:300]
            if "insufficient credits" in low:
                if i == base:
                    open(STATE, "w").write(str(base + 1))
                continue
            if "rate limit" in low:
                continue
            try:
                return json.loads(body)
            except Exception:
                return {"success": False, "error": body[:500]}
        time.sleep(15)
    return {"success": False, "error": "rate limited on every slot after retries"}


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    a = sys.argv[1:]
    if not a:
        print(__doc__); return
    cmd, arg = a[0], a[1]
    opt = lambda name, d: int(a[a.index(name) + 1]) if name in a else d
    if cmd == "scrape":
        d = call("scrape", {"url": arg, "formats": ["markdown"], "onlyMainContent": True,
                            "excludeTags": ["[id*=cookie]", "[class*=cookie]", "[id*=consent]", "[class*=consent]",
                                            "[id*=onetrust]", "[class*=cky-]", "[id*=CybotCookiebot]"]})
        if not d.get("success"):
            print("ERROR:", d.get("error")); return
        md = d["data"].get("markdown", "")
        if len(md.strip()) < 400:
            d = call("scrape", {"url": arg, "formats": ["markdown"], "onlyMainContent": True})
            if d.get("success"):
                md = d["data"].get("markdown", "")
        print(md[: opt("--max", 15000)])
    elif cmd == "search":
        d = call("search", {"query": arg, "limit": opt("--limit", 6)})
        if not d.get("success"):
            print("ERROR:", d.get("error")); return
        res = d.get("data", {})
        items = res.get("web", res) if isinstance(res, dict) else res
        for it in items:
            print(f"- {it.get('title')}\n  {it.get('url')}\n  {(it.get('description') or '')[:300]}")
    elif cmd == "map":
        p = {"url": arg, "limit": 300}
        if "--search" in a:
            p["search"] = a[a.index("--search") + 1]
        d = call("map", p)
        if not d.get("success"):
            print("ERROR:", d.get("error")); return
        for l in d.get("links", []):
            print(l.get("url") if isinstance(l, dict) else l)


if __name__ == "__main__":
    main()

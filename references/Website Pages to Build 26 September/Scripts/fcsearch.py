import json, sys, fc
for q in sys.argv[1:]:
    d = fc.post("search", {"query": q, "limit": 6})
    web = d.get("data", {}).get("web", d.get("data", [])) if isinstance(d.get("data"), dict) else d.get("data", [])
    print("=== ", q)
    for r in (web or [])[:6]:
        print("-", r.get("title"), "|", r.get("url"), "|", (r.get("description") or "")[:220])
    if not web: print(json.dumps(d)[:300])

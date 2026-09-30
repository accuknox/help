"""Firecrawl REST helper. Usage: python fc.py map | python fc.py scrape <url> [<url> ...]"""
import json, re, subprocess, sys, pathlib, concurrent.futures as cf

HERE = pathlib.Path(__file__).parent
OUT = HERE / "scrape"
OUT.mkdir(exist_ok=True)
KEY = subprocess.run([sys.executable, r"D:\Atharva\NOTES\SCRIPTS\keys\keys.py", "firecrawl"],
                     capture_output=True, text=True, encoding="utf-8").stdout.strip().splitlines()[-1]


def post(endpoint, body):
    r = subprocess.run(["curl", "-s", "-X", "POST", f"https://api.firecrawl.dev/v2/{endpoint}",
                        "-H", f"Authorization: Bearer {KEY}", "-H", "Content-Type: application/json",
                        "-d", json.dumps(body)], capture_output=True, text=True, encoding="utf-8", errors="replace")
    return json.loads(r.stdout)


def slug(url):
    s = re.sub(r"https?://(www\.)?", "", url).strip("/")
    return re.sub(r"[^a-zA-Z0-9]+", "_", s) or "home"


def scrape(url):
    import time
    for _ in range(6):
        d = post("scrape", {"url": url, "formats": ["markdown", {"type": "screenshot", "fullPage": True}, "links"], "onlyMainContent": False,
                        "waitFor": 2500})
        if "Rate limit" in str(d.get("error", "")):
            time.sleep(30); continue
        break
    data = d.get("data", {})
    s = slug(url)
    (OUT / f"{s}.md").write_text(data.get("markdown", json.dumps(d)[:2000]), encoding="utf-8")
    shot = data.get("screenshot")
    if shot:
        subprocess.run(["curl", "-s", "-o", str(OUT / f"{s}.png"), shot])
    return url, len(data.get("markdown", "")), bool(shot)


if __name__ == "__main__":
    if sys.argv[1] == "map":
        d = post("map", {"url": "https://accuknox.com", "limit": 3000})
        links = [x["url"] if isinstance(x, dict) else x for x in d.get("links", [])]
        (OUT / "map.txt").write_text("\n".join(sorted(links)), encoding="utf-8")
        print(len(links))
    else:
        with cf.ThreadPoolExecutor(3) as ex:
            for r in ex.map(scrape, sys.argv[2:]):
                print(r)

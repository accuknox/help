"""Deep hunt: TheirStack finds job posts that tag a rival tool, then run.py's buyer and email steps.

TheirStack reads the tool names inside job descriptions, so it finds posts that web search never indexes.
Costs $0.02 per job returned. Run:

    python hunt.py --tools "Prisma Cloud,Orca,Sysdig" --days 60 --per-tool 30 --target 70
"""
import argparse
import concurrent.futures as cf
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, r"D:\Atharva\NOTES\SCRIPTS\gtm")
import run as R  # noqa: E402
from common import Ledger, output, stamp  # noqa: E402

SLUGS = {"Prisma Cloud": "prisma-cloud", "Orca": "orca-security", "Sysdig": "sysdig", "Wiz": "wiz",
         "Aqua": "aqua-security", "Lacework": "lacework", "Veracode": "veracode", "Checkmarx": "checkmarx"}
NAMES = {v: k for k, v in SLUGS.items()}


def jobs_for(tool, days, n, page):
    body = {"job_technology_slug_or": [SLUGS[tool]], "posted_at_max_age_days": days, "limit": n, "page": page,
            "company_type": "direct_employer"}
    r = subprocess.run([shutil.which("treg"), "call", "theirstack.jobs.search", "--method", "POST", "--data", json.dumps(body)],
                       capture_output=True, text=True, encoding="utf-8", timeout=300)
    s = r.stdout
    i = s.find("{")
    try:
        d, _ = json.JSONDecoder().raw_decode(s[i:])
    except ValueError:
        return [], 0.0
    m = re.search(r"charged \$([0-9.]+)", r.stdout + r.stderr)
    return d.get("data", []), float(m.group(1)) if m else 0.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tools", default="Prisma Cloud,Orca,Sysdig")
    ap.add_argument("--days", type=int, default=60)
    ap.add_argument("--per-tool", type=int, default=30)
    ap.add_argument("--pages", type=int, default=1)
    ap.add_argument("--start-page", type=int, default=0)
    ap.add_argument("--target", type=int, default=70)
    ap.add_argument("--per-company", type=int, default=3)
    ap.add_argument("--min-employees", type=int, default=1000)
    ap.add_argument("--cap", type=float, default=2.5)
    ap.add_argument("--cache", default="", help="reuse jobs from this json file instead of paying again")
    ap.add_argument("--skip-emails", default="", help="json list of emails already in hand, skipped")
    a = ap.parse_args()
    L = Ledger(a.cap)
    spent_jobs = 0.0
    jobs = []
    if a.cache and Path(a.cache).exists():
        jobs = json.loads(Path(a.cache).read_text(encoding="utf-8"))
    else:
        for tool in [t.strip() for t in a.tools.split(",")]:
            for pg in range(a.start_page, a.start_page + a.pages):
                rows, c = jobs_for(tool, a.days, a.per_tool, pg)
                spent_jobs += c
                for j in rows:
                    j["_tool"] = tool
                    jobs.append(j)
        Path(a.cache or (R.STATE / "hunt-jobs.json")).write_text(json.dumps(jobs), encoding="utf-8")
    print(f"1. {len(jobs)} job posts · jobs ${spent_jobs:.2f}")
    L.treg += spent_jobs

    # Group by company domain. Keep every rival tool the posts name and the newest post.
    skip_emails = set(json.loads(Path(a.skip_emails).read_text())) if a.skip_emails else set()
    comps = {}
    for j in jobs:
        dom = (j.get("company_domain") or "").lower()
        if not dom:
            continue
        co = j.get("company_object") or {}
        c = comps.setdefault(dom, {"name": j["company"], "domain": dom, "employees": R.to_int(co.get("employee_count")),
                                   "industry": co.get("industry"), "tools": set(), "job": j["job_title"], "job_url": j.get("final_url") or j.get("url"),
                                   "posted": j["date_posted"], "posts": 0})
        c["posts"] += 1
        for t in j.get("technology_slugs", []):
            if t in NAMES:
                c["tools"].add(NAMES[t])
        c["tools"].add(j["_tool"])
        if j["date_posted"] > c["posted"]:
            c.update(job=j["job_title"], job_url=j.get("final_url") or j.get("url"), posted=j["date_posted"])
    sized = {k: c for k, c in comps.items() if c["employees"] >= a.min_employees}
    print(f"2. {len(comps)} companies, {len(sized)} with {a.min_employees}+ staff")

    # Jev drops security vendors, consultancies and staffing firms.
    def judge_co(item):
        k, c = item
        r = L.jev({"company": c["name"], "domain": c["domain"], "industry": c["industry"], "job_title": c["job"]},
                  {"vendor": {"type": "noul", "instructions": "Is `company` a cybersecurity software vendor, an IT consultancy or services firm, a managed security provider, or a staffing and recruiting agency? Banks, insurers, retailers, healthcare, manufacturers, government and software product companies are no."}})
        return k, c, (r["answers"]["vendor"]["noul"] if r else 1.0)
    with cf.ThreadPoolExecutor(6) as ex:
        res = list(ex.map(judge_co, sized.items()))
    buyers_co = {k: c for k, c, v in res if v < 0.5}
    dropped = [c["name"] for k, c, v in res if v >= 0.5]
    print(f"3. {len(buyers_co)} real buyers · dropped {len(dropped)}: {', '.join(dropped)}")

    people = {}
    for c in buyers_co.values():
        d = L.treg_call("treg.people.search", body={"company_domain": c["domain"], "title": "security", "limit": 25}, max_cost=0.05)
        for p in (R.output(d) or {}).get("people", []) if d else []:
            if p.get("first_name") and p.get("title") and p.get("employee_linkedin"):
                people[p["employee_linkedin"]] = {
                    "name": f'{p["first_name"]} {p["last_name"]}'.strip(), "first": p["first_name"], "last": p["last_name"],
                    "title": p["title"], "linkedin": p["employee_linkedin"], "company": c["name"], "domain": c["domain"],
                    "employees": c["employees"], "industry": c["industry"], "tool": ", ".join(sorted(c["tools"])),
                    "job": c["job"], "job_url": c["job_url"], "posted": c["posted"]}

    def judge(item):
        pid, w = item
        r = L.jev({"position": w["title"], "company": w["company"], "industry": w["industry"], "employees": w["employees"], "product": R.PRODUCT}, R.PEOPLE_QS)
        if r:
            A = r["answers"]
            w.update(p_buyer=A["fit"]["probabilities"].get("2", 0), p_offer=A["buys"]["probabilities"].get("accuknox", 0),
                     p_competitor=A["competitor"]["noul"], p_can_buy=A["can_buy"]["noul"], p_evidence=A["evidence"]["noul"])
        else:
            w["p_buyer"] = None
        w["tier"], _ = R.qualify(w)
        return pid, w
    with cf.ThreadPoolExecutor(6) as ex:
        people = dict(ex.map(judge, people.items()))
    passed = sorted((w for w in people.values() if w["tier"]),
                    key=lambda w: (w["tier"] != "high", -(w["p_buyer"] + w["p_offer"] + w["p_can_buy"] + w["p_evidence"])))
    print(f"4. {len(people)} people, {len(passed)} pass the five checks · treg so far ${L.treg:.2f}")

    # Round robin by company so no company hogs the list, up to per-company.
    per, chosen = {}, []
    for w in passed:
        if per.get(w["company"], 0) < a.per_company:
            per[w["company"]] = per.get(w["company"], 0) + 1
            chosen.append(w)

    leads = []
    for w in chosen:
        if len(leads) >= a.target or L.left() < 0.03:
            break
        d = L.treg_call("treg.people.email.find", body={"first_name": w["first"], "last_name": w["last"], "domain": w["domain"]}, max_cost=0.03)
        em = (R.output(d) or {}).get("email") if d else None
        if not em or em.lower() in skip_emails:
            continue
        v = L.treg_call("treg.people.email.verify", body={"email": em}, max_cost=0.003)
        if v and (R.output(v) or {}).get("status") in ("valid", "safe", "deliverable") and R.same_org(em, w["domain"]):
            w["email"] = em
            leads.append(w)
    print(f"5. {len(leads)} verified leads · treg ${L.treg:.2f} · jev ${L.jev_usd:.4f}")
    out = R.STATE / f"hunt-{stamp()}.json"
    out.write_text(json.dumps({"leads": leads, "chosen": len(chosen), "treg": L.treg}, indent=1, default=str), encoding="utf-8")
    print("saved", out)


if __name__ == "__main__":
    main()

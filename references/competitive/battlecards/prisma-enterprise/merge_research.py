"""Merge research/*.json into data/rows.json and data/sources.json, and write evidence-log.md.

Run from this folder's parent repo root or anywhere:
    python references/competitive/battlecards/prisma-enterprise/merge_research.py
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
R = HERE / "research"
D = HERE / "data"

ICON = {"Supported": "tick", "Parity": "tick", "Limited": "dash", "Beta": "dash",
        "Coming soon": "dash", "Not supported": "cross", "No equivalent": "cross"}


def load(name):
    return json.loads((R / name).read_text(encoding="utf-8"))


live = {r["n"]: r for r in load("live-rows-2026-09-30.json")}
ak = {r["n"]: r for r in load("accuknox-rows.json")}
pc = {}
for f in ("prisma-rows-01-23.json", "prisma-rows-24-51.json", "prisma-rows-52-68.json"):
    pc.update({r["n"]: r for r in load(f)})

# Reviewer overrides, each one explained in evidence-log.md.
PARAM = {57: "Cloud Compliance Frameworks (33+)"}
AK_TEXT = {
    31: "Zero Trust allow-list blocks unknown processes and binaries at runtime",
    57: "33+ frameworks, 42 benchmark versions, incl. ISO 27001, NIST, CIS, PCI, SOC 2, HIPAA",
}
AK_EXTRA_SRC = {57: ["https://help.accuknox.com/faqs/compliance/"]}
PC_TEXT = {
    1: "17 regional SaaS tenants, incl. AWS GovCloud and China. PAN operates the control plane",
    16: "AWS onboarding with CSPM policies, runtime security and DSPM",
    17: "Azure onboarding with CSPM policies, runtime security and DSPM",
    18: "GCP onboarding with CSPM policies, runtime security and DSPM",
    21: "Audit event policies alert on cloud audit logs. Alerts can take a few hours",
}
PC_STATUS = {21: "Limited", 31: "Limited"}


def clean(s):
    s = s.replace("incl.", "including").replace(" — ", ", ").replace("—", ", ")
    return re.sub(r";\s*(\w)", lambda m: ". " + m.group(1).upper(), s)


def title_for(url):
    if "help.accuknox.com" in url:
        tail = url.rstrip("/").split("/")[-1].replace("-", " ")
        return "AccuKnox Help, " + tail.capitalize()
    if "docs.prismacloud.io" in url:
        tail = url.rstrip("/").split("/")[-1].replace("-", " ")
        return "Prisma Cloud Enterprise Edition docs, " + tail
    if "paloaltonetworks.com" in url:
        return "Palo Alto Networks, " + url.rstrip("/").split("/")[-1].replace("-", " ")
    return "AccuKnox, " + url.rstrip("/").split("/")[-1]


sources, seen = [], {}


def sid(url):
    if not url:
        return None
    if url not in seen:
        seen[url] = f"s{len(seen) + 1}"
        sources.append({"id": seen[url], "title": title_for(url), "url": url})
    return seen[url]


rows, log = [], []
for n in range(1, 69):
    a, p, l = ak[n], pc[n], live[n]
    ak_status = a["status"]
    ak_text = clean(AK_TEXT.get(n, a["ak_new"]))
    pc_status = PC_STATUS.get(n, p["status"])
    pc_text = clean(PC_TEXT.get(n, p["pc_new"]))
    ak_urls = [a["url"]] + AK_EXTRA_SRC.get(n, [])
    ak_src = [sid(u) for u in ak_urls if u and ak_status != "Coming soon"]
    pc_src = [sid(p["url"])] if p["url"] else []
    rows.append({
        "param": PARAM.get(n, l["param"]).replace(" — ", ", ").replace("—", ","),
        "ak_icon": ICON[ak_status], "ak": ak_text, "ak_src": ak_src,
        "pc_icon": ICON[pc_status], "pc": pc_text, "pc_src": pc_src,
    })
    log.append(
        f"| {n} | {l['param']} | {l['pc_icon']} to {ICON[pc_status]} ({pc_status}) | {p['verdict']} | "
        f"{p['url'] or 'none'} | {p.get('quote', '').replace('|', '/')} | "
        f"{ICON[ak_status]} ({ak_status}, tier {a['tier'][0]}) | {a['url']} | {a.get('evidence', '').replace('|', '/')} |"
    )

# Sources for the page-level text.
for u in (
    "https://docs.prismacloud.io/release-notes/prisma-cloud-release-information/features-introduced-in-2026/features-introduced-in-august-2026",
    "https://docs.prismacloud.io/content-collections/runtime-security/pcee-vs-pcce",
    "https://www.paloaltonetworks.com/company/press/2025/palo-alto-networks-introduces-cortex-cloud--the-future-of-real-time-cloud-security",
    "https://help.accuknox.com/faqs/general/",
    "https://help.accuknox.com/faqs/compliance/",
    "https://help.accuknox.com/faqs/runtime-security/",
    "https://accuknox.com/wp-content/uploads/SBOM-Case-Study.pdf",
):
    sid(u)
for s in sources:
    if s["url"].endswith("SBOM-Case-Study.pdf"):
        s["title"] = "AccuKnox case study, Top 3 Indian public sector bank operationalises SBOM air-gapped"
    if "features-introduced-in-august-2026" in s["url"]:
        s["title"] = "Prisma Cloud release notes, features introduced in August 2026 (26.8.1)"
    if "introduces-cortex-cloud" in s["url"]:
        s["title"] = "Palo Alto Networks press release, Cortex Cloud launch (February 2025)"

D.mkdir(exist_ok=True)
(D / "rows.json").write_text(json.dumps(rows, indent=1, ensure_ascii=False), encoding="utf-8")
(D / "sources.json").write_text(json.dumps(sources, indent=1, ensure_ascii=False), encoding="utf-8")
(D / "source-ids.json").write_text(json.dumps(seen, indent=1), encoding="utf-8")

head = (
    "# Evidence Log, AccuKnox vs Prisma Cloud Enterprise Edition\n\n"
    "Competitor facts were read on 2026-09-30 from docs.prismacloud.io (content-collections, the "
    "Enterprise Edition path) and paloaltonetworks.com. Compute Edition pages under /admin-guide/ "
    "were excluded. AccuKnox facts come from this repo's docs/ folder, published at help.accuknox.com. "
    "Raw page copies sit in research/raw/.\n\n"
    "| # | Parameter | Prisma icon change | Live claim verdict | Prisma source | Prisma quote | AccuKnox | AccuKnox source | AccuKnox evidence |\n"
    "|---|---|---|---|---|---|---|---|---|\n"
)
(HERE / "evidence-log.md").write_text(head + "\n".join(log) + "\n", encoding="utf-8")
print(len(rows), "rows,", len(sources), "sources")

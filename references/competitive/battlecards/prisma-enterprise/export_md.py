"""Export the comparison as Markdown, ready for PDF conversion or a Google Doc.

    python references/competitive/battlecards/prisma-enterprise/export_md.py
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
D = HERE / "data"
P = json.loads((D / "page.json").read_text(encoding="utf-8"))
G = json.loads((D / "groups.json").read_text(encoding="utf-8"))
S = json.loads((D / "sources.json").read_text(encoding="utf-8"))
NUM = {s["id"]: i + 1 for i, s in enumerate(S)}
URL = {s["id"]: s["url"] for s in S}
UID = {s["url"]: s["id"] for s in S}
LABEL = {"tick": "Supported", "dash": "Limited", "cross": "Not supported"}


def cite(ids):
    return "".join(f" [[{NUM[i]}]]({URL[i]})" for i in ids)


def tail(text, ids):
    """Put citations before the closing period, so the sentence keeps its verb."""
    if text.endswith("."):
        return text[:-1] + cite(ids) + "."
    return text + cite(ids)


def ak_cell(r):
    if r["ak"] == "Coming soon":
        return "Coming soon"
    return f"{LABEL[r['ak_icon']]}. {r['ak']}{cite(r['ak_src'])}"


out = [
    "---",
    f'title: "{P["title"]}"',
    f'subtitle: "{P["h2"]}"',
    "slug: accuknox-vs-prisma",
    "url: https://accuknox.com/comparisons/accuknox-vs-prisma",
    "archetype: head-to-head",
    "category: cnapp",
    "competitors:",
    '  - "Palo Alto Networks Prisma Cloud Enterprise Edition"',
    f'excerpt: "{P["intro"]}"',
    f"checked: {P['accessed']}",
    "---",
    "",
    f"# {P['title']}",
    "",
    f"**{P['h2']}**",
    "",
    tail(P["intro"], [UID[u] for u in P["intro_src_urls"]]),
    "",
    "*" + tail(P["edition_tag"], [UID[u] for u in P["edition_src_urls"]]) + "*",
    "",
    "## AccuKnox Leads on Deployment, Native AppSec and AI Security",
    "",
]
for g in G:
    out += [f"### {g['title']}", "", "| Parameter | AccuKnox | Prisma Cloud Enterprise Edition |", "| --- | --- | --- |"]
    out += [f"| {r['param']} | {ak_cell(r)} | {LABEL[r['pc_icon']]}. {r['pc']}{cite(r['pc_src'])} |" for r in g["rows"]]
    out.append("")
out += ["", f"## {P['why_h2']}", ""]
for c in P["why_cards"]:
    out += [f"### {c['title']}", "", tail(c["body"], [UID[u] for u in c["src_urls"]]), ""]
out += ["## Every Cell Cites a Vendor Page", "", P["sources_note"], "", "| # | Source | # | Source | # | Source |", "| --- | --- | --- | --- | --- | --- |"]
links = [f"{i + 1} | [{s['title']}]({s['url']})" for i, s in enumerate(S)]
links += [" | "] * (-len(links) % 3)
out += ["| " + " | ".join(links[k:k + 3]) + " |" for k in range(0, len(links), 3)]

dest = HERE / "Accuknox-vs-Prisma-Enterprise-Comparison.md"
dest.write_text("\n".join(out) + "\n", encoding="utf-8")
print(dest)

"""Build Accuknox-vs-Prisma-Enterprise-Comparison.pdf.

The PDF keeps the look of https://accuknox.com/comparisons/accuknox-vs-prisma: the hero
(H1 left, H2 and intro right), the three-column Parameters matrix with tick, dash and
cross icons, the "Why Customers Choose" three-card section and the demo CTA. The matrix
is grouped by capability area, and sources sit in a compact three-column grid of linked
titles. The stock AccuKnox back page closes the file.

Run from the repo root:
    python references/competitive/battlecards/prisma-enterprise/build_comparison_pdf.py [out.pdf]

Content lives in data/page.json, data/groups.json (from apply_layout.py) and
data/sources.json (from merge_research.py). Needs playwright (with chromium) and pypdf.
"""
import base64
import html
import json
import pathlib
import re
import sys

from playwright.sync_api import sync_playwright
from pypdf import PdfReader, PdfWriter

HERE = pathlib.Path(__file__).resolve().parent
A = HERE / "assets"
D = HERE / "data"
BUILD = HERE / "build"
OUT = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "Accuknox-vs-Prisma-Enterprise-Comparison.pdf"

PAGE = json.loads((D / "page.json").read_text(encoding="utf-8"))
GROUPS = json.loads((D / "groups.json").read_text(encoding="utf-8"))
ALL_SOURCES = {s["id"]: s for s in json.loads((D / "sources.json").read_text(encoding="utf-8"))}
URL_ID = {s["url"]: s["id"] for s in ALL_SOURCES.values()}


def ids_for(urls):
    return [URL_ID[u] for u in urls]


# Number sources in reading order, and keep only the ones the page cites.
ORDER = []
for ids in (
    [ids_for(PAGE.get("intro_src_urls", [])), ids_for(PAGE.get("edition_src_urls", []))]
    + [r["ak_src"] + r["pc_src"] for g in GROUPS for r in g["rows"]]
    + [ids_for(c.get("src_urls", [])) for c in PAGE["why_cards"]]
):
    for i in ids:
        if i not in ORDER:
            ORDER.append(i)
# AccuKnox sources first, then Prisma sources, each in reading order.
_ak = lambda i: "accuknox.com" in ALL_SOURCES[i]["url"]
ORDER = [i for i in ORDER if _ak(i)] + [i for i in ORDER if not _ak(i)]
SRC_NUM = {i: n + 1 for n, i in enumerate(ORDER)}


def uri(name, mime):
    return f"data:{mime};base64," + base64.b64encode((A / name).read_bytes()).decode()


ICON = {
    "tick": uri("tick-fill.svg", "image/svg+xml"),
    "dash": uri("disturb.svg", "image/svg+xml"),
    "cross": uri("cross-fill.svg", "image/svg+xml"),
}
LOGO = uri("logo-light-back.png", "image/png")
CARD_ICON = {
    "Better": uri("Better-comparision.svg", "image/svg+xml"),
    "Faster": uri("Faster-comparision.svg", "image/svg+xml"),
    "Affordable": uri("Cheaper-comparision.svg", "image/svg+xml"),
}

ACRONYM = {
    "aspm": "ASPM", "cspm": "CSPM", "cdr": "CDR", "sast": "SAST", "dast": "DAST", "iac": "IaC",
    "sbom": "SBOM", "xbom": "xBOM", "sarif": "SARIF", "cicd": "CI/CD", "ci": "CI", "cd": "CD",
    "cis": "CIS", "kiem": "KIEM", "api": "API", "sec": "Security", "vm": "VM", "aws": "AWS",
    "gcp": "GCP", "ai": "AI", "ml": "ML", "dspm": "DSPM", "faqs": "FAQs", "opa": "OPA",
    "pcee": "Enterprise", "pcce": "Compute", "vs": "vs", "aispmoverview": "AI-SPM overview",
    "waas": "WAAS", "sbom-case-study.pdf": "", "org": "org", "3.4": "3.4", "mcp": "MCP",
    "servicenow": "ServiceNow", "splunk": "Splunk", "iam": "IAM", "llm": "LLM", "nginx": "NGINX",
    "modelarmor": "ModelArmor", "knoxguard": "KnoxGuard", "kubearmor": "KubeArmor",
    "github": "GitHub", "rn": "", "helm": "Helm", "cve": "CVE", "rsyslog": "rsyslog",
}


def short_title(s):
    """Readable link text built from the URL, since the title field repeats the vendor."""
    url = s["url"]
    if url.endswith("SBOM-Case-Study.pdf"):
        return "Indian bank SBOM case study"
    if "features-introduced-in-august-2026" in url:
        return "Release notes, August 2026"
    if "introduces-cortex-cloud" in url:
        return "Cortex Cloud launch"
    slug = url.rstrip("/").split("/")[-1]
    parent = url.rstrip("/").split("/")[-2]
    if slug in ("general", "compliance", "aspm", "sbom", "api-sec", "runtime-security", "ai-security") and parent == "faqs":
        slug = f"{slug}-faqs"
    if slug == "features-introduced-in-december-2024":
        return "Release notes, December 2024"
    if slug == "ai-spm":
        return "AI-SPM blog"
    words = [ACRONYM.get(w.lower(), w) for w in re.split(r"[-_]", slug)]
    text = " ".join(w for w in words if w)
    for a, b in (("prisma cloud", "Prisma Cloud"), ("openshift", "OpenShift"), ("oob containers", "WAAS out-of-band containers"),
                 ("sboms", "SBOMs"), ("december", "December")):
        text = text.replace(a, b)
    return text[:1].upper() + text[1:]


def vendor(s):
    u = s["url"]
    if "help.accuknox.com" in u or "accuknox.com" in u:
        return "ak"
    return "pc"


def esc(s):
    return html.escape(s, quote=False)


def cites(ids):
    if not ids:
        return ""
    nums = sorted({SRC_NUM[i] for i in ids})
    return '<sup class="cite">' + ",".join(str(n) for n in nums) + "</sup>"


def cell(icon, text, src, cls):
    return (
        f'<td class="{cls}"><div class="cellin">'
        f'<img class="st" src="{ICON[icon]}" alt="{icon}">'
        f"<p>{esc(text)}{cites(src)}</p></div></td>"
    )


def row_html(r):
    return (
        "<tr>"
        f'<th scope="row"><h3>{esc(r["param"])}</h3></th>'
        + cell(r["ak_icon"], r["ak"], r["ak_src"], "ak")
        + cell(r["pc_icon"], r["pc"], r["pc_src"], "pc")
        + "</tr>"
    )


def group_html(g):
    rank = {"tick": 2, "dash": 1, "cross": 0}
    n = len(g["rows"])
    ak = sum(1 for r in g["rows"] if rank[r["ak_icon"]] > rank[r["pc_icon"]])
    pc = sum(1 for r in g["rows"] if rank[r["pc_icon"]] > rank[r["ak_icon"]])
    parts = [f"AccuKnox leads {ak} of {n}"] if ak else []
    parts += [f"Prisma leads {pc} of {n}"] if pc else []
    tally = " · ".join(parts) or f"Parity on {n}"
    head = (
        f'<tbody class="grp"><tr class="gh"><th colspan="3"><span>{esc(g["title"])}</span>'
        f'<em>{tally}</em></th></tr>'
    )
    return head + "".join(row_html(r) for r in g["rows"]) + "</tbody>"


def card(c):
    return (
        '<div class="card">'
        f'<div class="ch"><img src="{CARD_ICON[c["title"]]}" alt=""><h3>{esc(c["title"])}</h3></div>'
        f"<p>{esc(c['body'])}{cites(ids_for(c.get('src_urls', [])))}</p></div>"
    )


def source_li(i):
    s = ALL_SOURCES[i]
    tag = "AccuKnox" if vendor(s) == "ak" else "Prisma"
    return (
        f'<li value="{SRC_NUM[i]}"><b class="{vendor(s)}">{tag}</b> '
        f'<a href="{html.escape(s["url"])}">{esc(short_title(s))}</a></li>'
    )


CSS = """
@page { size: A4; margin: 12mm 11mm 13mm 11mm; }
* { box-sizing: border-box; }
body { font-family: Inter, 'Segoe UI', Arial, sans-serif; color: #000; margin: 0; font-size: 9.5px; }
.hero { display: grid; grid-template-columns: 36% 64%; align-items: center; padding: 10px 0 22px; }
.hero h1 { font-size: 38px; line-height: 1.12; font-weight: 700; margin: 0; padding-right: 22px; }
.hero .right { border-left: 1.6px solid #1040c5; padding: 16px 0 16px 26px; }
.hero h2 { font-size: 16.5px; line-height: 1.25; margin: 0 0 10px; font-weight: 700; }
.hero p { font-size: 10px; line-height: 1.55; margin: 0; }
.edition { display: inline-block; margin-top: 10px; font-size: 8px; font-weight: 600; color: #263238;
  background: #e1f5fe; border-radius: 4px; padding: 2px 7px; }
.legend { font-size: 8px; color: #455a64; margin: 0 0 10px; padding-top: 8px; border-top: 1px solid #e3e8eb; display: flex; gap: 14px; align-items: center; }
.legend img { width: 11px; height: 11px; vertical-align: -2px; margin-right: 3px; }
table.cmp { width: 100%; border-collapse: collapse; }
table.cmp thead th { padding: 0 0 6px; vertical-align: middle; }
table.cmp thead .p { text-align: left; font-size: 12px; font-weight: 700; color: #263238; width: 27%; }
table.cmp thead .l img { width: 100px; display: block; margin: 0 auto; }
table.cmp thead .pn { background: #e1f5fe; font-size: 11px; font-weight: 700; color: #263238;
  text-align: center; height: 34px; border-radius: 8px 8px 0 0; }
table.cmp thead { display: table-header-group; }
tbody.grp { break-inside: avoid; }
table.cmp tr { break-inside: avoid; }
tr.gh th { text-align: left; padding: 9px 8px 4px 0; border-bottom: 2px solid #1040c5; }
tr.gh span { font-size: 11px; font-weight: 700; color: #0b2e8f; text-transform: uppercase; letter-spacing: .05em; }
tr.gh em { float: right; font-style: normal; font-size: 7.8px; font-weight: 600; color: #1040c5; padding-top: 2px; }
table.cmp th[scope=row] { width: 27%; text-align: left; vertical-align: middle; padding: 4px 8px 4px 0;
  border-bottom: 1px solid #e3e8eb; }
table.cmp th h3 { font-size: 9.4px; line-height: 1.25; color: #1040c5; margin: 0; font-weight: 700; }
td.ak, td.pc { width: 36.5%; vertical-align: middle; padding: 4px 8px; border-bottom: 1px solid #e3e8eb; }
td.ak { background: #fff; border-left: 1px solid #cfd8dc; border-right: 1px solid #cfd8dc; }
td.pc { background: #eceff1; border-bottom-color: #dde3e6; }
.cellin { display: flex; align-items: center; gap: 6px; }
.cellin img.st { width: 13px; height: 13px; flex: none; }
.cellin p { margin: 0; line-height: 1.3; font-size: 8.4px; }
sup.cite { font-size: 6px; color: #1040c5; margin-left: 1px; }
.why { background: #eceff1; padding: 14px 14px 16px; margin-top: 14px; break-inside: avoid; }
.why h2 { text-align: center; font-size: 16px; margin: 0 0 10px; }
.cards { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; }
.card { background: #fff; border: 1px solid #cfd8dc; border-radius: 8px; padding: 11px 12px; }
.card .ch { display: flex; align-items: center; gap: 8px; margin-bottom: 6px; }
.card img { height: 26px; }
.card h3 { font-size: 12.5px; margin: 0; }
.card p { font-size: 8.4px; line-height: 1.45; margin: 0; }
.cta { display: flex; align-items: center; justify-content: space-between; gap: 12px; margin-top: 10px;
  padding: 10px 14px; border: 1px solid #cfd8dc; border-radius: 8px; break-inside: avoid; }
.cta .kick { color: #1040c5; font-weight: 700; font-size: 8px; letter-spacing: .05em; text-transform: uppercase; }
.cta h2 { font-size: 13px; margin: 2px 0 0; }
.cta a { background: #1040c5; color: #fff; text-decoration: none; font-weight: 700;
  font-size: 9.5px; padding: 7px 16px; border-radius: 6px; white-space: nowrap; }
.sources { margin-top: 14px; break-inside: avoid; }
.sources h2 { font-size: 12px; margin: 0 0 3px; }
.sources .note { font-size: 7.6px; color: #37474f; line-height: 1.4; margin: 0 0 6px; }
.sources ol { margin: 0; padding-left: 16px; columns: 3; column-gap: 16px; }
.sources li { font-size: 7.2px; line-height: 1.35; break-inside: avoid; color: #607d8b; }
.sources li b { font-weight: 600; font-size: 6.4px; text-transform: uppercase; letter-spacing: .03em; }
.sources li b.ak { color: #1040c5; }
.sources li b.pc { color: #c62828; }
.sources a { color: #263238; text-decoration: underline; text-decoration-color: #b0bec5; }
"""


def build_html():
    groups = "\n".join(group_html(g) for g in GROUPS)
    cards = "\n".join(card(c) for c in PAGE["why_cards"])
    srcs = "\n".join(source_li(i) for i in ORDER)
    legend = (
        f'<div class="legend"><span><img src="{ICON["tick"]}">Supported</span>'
        f'<span><img src="{ICON["dash"]}">Limited, partial or coming soon</span>'
        f'<span><img src="{ICON["cross"]}">Not supported</span>'
        '<span>Superscripts link to the numbered sources.</span></div>'
    )
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>{esc(PAGE['title'])}</title><style>{CSS}</style></head><body>
<section class="hero">
  <h1>AccuKnox {{vs}} Prisma Cloud</h1>
  <div class="right">
    <h2>{esc(PAGE['h2'])}</h2>
    <p>{esc(PAGE['intro'])}{cites(ids_for(PAGE.get('intro_src_urls', [])))}</p>
    <span class="edition">{esc(PAGE['edition_tag'])}{cites(ids_for(PAGE.get('edition_src_urls', [])))}</span>
  </div>
</section>
{legend}
<table class="cmp">
  <thead><tr>
    <th class="p">Parameters</th>
    <th class="l"><img src="{LOGO}" alt="AccuKnox"></th>
    <th class="pn">Prisma Cloud Enterprise Edition</th>
  </tr></thead>
{groups}
</table>
<section class="why">
  <h2>{esc(PAGE['why_h2'])}</h2>
  <div class="cards">{cards}</div>
</section>
<section class="cta">
  <div><div class="kick">Get a LIVE Tour</div><h2>Ready For A Personalized Security Assessment?</h2></div>
  <a href="https://accuknox.com/contact-us">Schedule A Demo</a>
</section>
<section class="sources">
  <h2>Sources</h2>
  <p class="note">{esc(PAGE['sources_note'])}</p>
  <ol>{srcs}</ol>
</section>
</body></html>"""


def main():
    BUILD.mkdir(exist_ok=True)
    page_html = build_html()
    (BUILD / "comparison.html").write_text(page_html, encoding="utf-8")
    body = BUILD / "body.pdf"
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page()
        pg.set_content(page_html, wait_until="load")
        pg.pdf(
            path=str(body),
            format="A4",
            print_background=True,
            prefer_css_page_size=True,
            display_header_footer=True,
            header_template="<span></span>",
            footer_template=(
                '<div style="font-size:6.5px;color:#78909c;width:100%;padding:0 11mm;'
                'display:flex;justify-content:space-between;font-family:Arial">'
                f"<span>AccuKnox vs Prisma Cloud Enterprise Edition. Sources checked {PAGE['accessed']}.</span>"
                '<span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>'
            ),
        )
        b.close()
    w = PdfWriter()
    for page in PdfReader(str(body)).pages:
        w.add_page(page)
    w.add_page(PdfReader(str(A / "back-page.pdf")).pages[0])
    w.add_metadata({"/Title": PAGE["title"], "/Author": "AccuKnox"})
    with open(OUT, "wb") as f:
        w.write(f)
    print(f"{OUT} {len(w.pages)} pages, {len(ORDER)} sources")


if __name__ == "__main__":
    main()

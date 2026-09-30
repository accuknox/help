"""Build the AI Security Stack Ranking v3 (Beta) as one master sheet from vendors_v2/*.json.

Usage: python build.py [output.xlsx]
"""
import json, glob, os, sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.cell.rich_text import CellRichText, TextBlock
from openpyxl.cell.text import InlineFont
from openpyxl.utils import get_column_letter
from openpyxl.comments import Comment
from urllib.parse import urlparse

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "ai-security-stack-ranking-v3-beta.xlsx")
AS_OF = "September 2026"

TICK, DASH, CROSS = "✓", "−", "✗"
SYM = {"yes": TICK, "partial": DASH, "no": CROSS}
WORD = {"yes": "Supported", "partial": "Partial", "no": "No evidence"}

# (number, header, what a tick needs)
MODULES = [
    ("1", "AI-SPM", "AI inventory, shadow AI, pipeline posture"),
    ("2", "Agentic AI", "Managed agents, MCP, agent sandbox"),
    ("3", "AI-DR", "Detect, respond, block at runtime"),
    ("4", "Guardrails + AI Gateway", "Inline firewall, injection and PII, unsafe output"),
    ("5", "Compliance", "AIBOM, framework mapping, audit trail"),
    ("6", "Red Team + AI DAST", "Attack library, live multi-turn attacks, CI/CD"),
    ("7", "AI Identity", "Agent identity, least privilege, NHI"),
    ("8", "Model, Data + AI SAST", "Model files, datasets, AI code scanning"),
]

ARIAL = "Arial"
NAVY, BLUE, GREY = "000025", "005BFF", "6B7280"
FILL = {"yes": "DCF5E3", "partial": "FFF1CC", "no": "FBE1E1"}
INK = {"yes": "137333", "partial": "9A6700", "no": "B3261E"}
AK_FILL = PatternFill("solid", fgColor="E8EFFF")
HEAD_FILL = PatternFill("solid", fgColor=NAVY)
thin = Side(style="thin", color="D0D5DD")
BOX = Border(left=thin, right=thin, top=thin, bottom=thin)


def font(size=10, bold=False, color="1F2937", italic=False):
    return Font(name=ARIAL, size=size, bold=bold, color=color, italic=italic)


def ifont(size, bold=False, color="1F2937"):
    return InlineFont(rFont=ARIAL, sz=size, b=bold, color=color)


def score(d):
    return sum({"yes": 1, "partial": 0.5}.get(d["modules"][m[0]]["status"], 0) for m in MODULES)


def load():
    rows = [json.load(open(p, encoding="utf-8")) for p in glob.glob(os.path.join(HERE, "vendors_v3", "*.json"))]
    ak = [d for d in rows if d["slug"] == "accuknox"]
    rest = sorted([d for d in rows if d["slug"] != "accuknox"], key=lambda d: (-score(d), d["vendor"].lower()))
    return ak + rest


def build():
    vendors = load()
    wb = Workbook()
    ws = wb.active
    ws.title = "AI Stack Ranking v3"

    C_RANK, C_VENDOR, C_SCORE, C_MOD = 1, 2, 3, 4
    ncol = C_MOD + len(MODULES) - 1
    last = get_column_letter(ncol)
    hr = 3
    first, lastrow = hr + 1, hr + len(vendors)
    sc = get_column_letter(C_SCORE)
    mcol = {m[0]: get_column_letter(C_MOD + i) for i, m in enumerate(MODULES)}

    # Title block
    ws["A1"] = "AI Security Competitive Stack Ranking  |  v3 (BETA)"
    ws["A1"].font = font(16, True, NAVY)
    ws.merge_cells(f"A1:{last}1")

    # Header
    heads = {C_RANK: "Rank", C_VENDOR: "Vendor", C_SCORE: "Score\n(of 8)"}
    for c, h in heads.items():
        ws.cell(hr, c, h)
    for i, m in enumerate(MODULES):
        ws.cell(hr, C_MOD + i, CellRichText(
            TextBlock(ifont(10, True, "FFFFFF"), f"{m[0]}. {m[1]}\n"),
            TextBlock(ifont(8, False, "C7D2FE"), m[2])))
    for c in range(1, ncol + 1):
        cell = ws.cell(hr, c)
        if not isinstance(cell.value, CellRichText):
            cell.font = font(10, True, "FFFFFF")
        cell.fill = HEAD_FILL
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = BOX
    ws.row_dimensions[hr].height = 44

    # Rows
    for i, d in enumerate(vendors):
        r = first + i
        ak = d["slug"] == "accuknox"
        ws.cell(r, C_RANK, f"=RANK({sc}{r},${sc}${first}:${sc}${lastrow})")
        ws.cell(r, C_VENDOR, CellRichText(
            TextBlock(ifont(11, True, NAVY), d["vendor"] + "\n"),
            TextBlock(ifont(8, False, GREY), d.get("what_it_is", ""))))
        rng = f"{mcol['1']}{r}:{mcol['8']}{r}"
        ws.cell(r, C_SCORE, f'=COUNTIF({rng},"{TICK}*")+0.5*COUNTIF({rng},"{DASH}*")')
        for j, m in enumerate(MODULES):
            mod = d["modules"][m[0]]
            st = mod["status"]
            head = SYM[st] + " " + ("Beta" if mod.get("beta") else WORD[st])
            nl = chr(10)
            parts = [TextBlock(ifont(10, True, INK[st]), head)]
            if mod.get("has"):
                parts += [TextBlock(ifont(8, True, "137333"), nl + "Has: "), TextBlock(ifont(8, False, "1F2937"), mod["has"])]
            if mod.get("lacks"):
                parts += [TextBlock(ifont(8, True, "B3261E"), nl + "Lacks: "), TextBlock(ifont(8, False, "1F2937"), mod["lacks"])]
            cell = ws.cell(r, C_MOD + j, CellRichText(*parts))
            cm = Comment(mod["reason"] + nl + nl + "Source: " + mod["url"], "AccuKnox")
            cm.width, cm.height = 340, 120
            cell.comment = cm
            cell.fill = PatternFill("solid", fgColor=FILL[st])
            cell.alignment = Alignment(vertical="top", wrap_text=True)
            cell.border = BOX
        for c in (C_RANK, C_SCORE):
            cell = ws.cell(r, c)
            cell.font = font(12 if c == C_SCORE else 11, True, NAVY)
            cell.alignment = Alignment(horizontal="center", vertical="center")
        ws.cell(r, C_SCORE).number_format = "0.0"
        ws.cell(r, C_VENDOR).alignment = Alignment(vertical="top", wrap_text=True)
        for c in (C_RANK, C_VENDOR, C_SCORE):
            ws.cell(r, c).border = BOX
            if ak:
                ws.cell(r, c).fill = AK_FILL
        ws.row_dimensions[r].height = 82

    # Source links grid, same columns as the ranking
    sr = lastrow + 3
    ws.cell(sr, 1, "Source links  |  one per vendor and module, same columns as the ranking above").font = font(12, True, NAVY)
    ws.merge_cells(start_row=sr, start_column=1, end_row=sr, end_column=ncol)
    for i, d in enumerate(vendors):
        r = sr + 1 + i
        ws.cell(r, C_VENDOR, d["vendor"]).font = font(9, True, NAVY)
        for j, m in enumerate(MODULES):
            url = d["modules"][m[0]]["url"]
            u = urlparse(url)
            label = (u.netloc.replace("www.", "") + u.path).rstrip("/")
            label = label if len(label) <= 44 else label[:43] + "…"
            cell = ws.cell(r, C_MOD + j, label)
            cell.hyperlink = url
            cell.font = Font(name=ARIAL, size=8, color=BLUE, underline="single")
            cell.alignment = Alignment(vertical="center", wrap_text=False, shrink_to_fit=True)
        for c in range(C_VENDOR, ncol + 1):
            ws.cell(r, c).border = BOX
    lastrow_links = sr + len(vendors)

    # Footer
    notes = [
        f"{TICK} Supported: matches the AccuKnox benchmark on all 3 parts of the module.   {DASH} Partial: has part of it, see Has and Lacks.   {CROSS} No evidence: none found after two or more searches.   Beta: upcoming AccuKnox feature, the tick rests on GA features.",
        "Score: Supported = 1, Partial = 0.5, No evidence = 0. Rank ties share a number.",
        "v3 folds AI Gateway into module 4, AI DAST into module 6 and AI SAST into module 8. Module 2 credits AgentZ, the AccuKnox zero trust agent platform.",
        "Each competitor cell cites the vendor's own page. Verification ran four times: research, an independent strict re-score, a re-search of every No plus a link check, and a benchmark of every sub-feature against AccuKnox. Hover a cell for its source.",
    ]
    for k, t in enumerate(notes):
        rr = lastrow_links + 2 + k
        ws.cell(rr, 1, t).font = font(9, color=GREY, italic=True)
        ws.merge_cells(start_row=rr, start_column=1, end_row=rr, end_column=ncol)

    widths = {C_RANK: 6, C_VENDOR: 30, C_SCORE: 8}
    for c in range(1, ncol + 1):
        ws.column_dimensions[get_column_letter(c)].width = widths.get(c, 31)
    ws.freeze_panes = ws.cell(first, C_MOD)
    ws.sheet_view.showGridLines = False
    ws.sheet_view.zoomScale = 90
    ws.page_setup.orientation = "landscape"
    ws.page_setup.paperSize = ws.PAPERSIZE_A3
    ws.page_setup.fitToWidth, ws.page_setup.fitToHeight = 1, 0
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.print_title_rows = f"{hr}:{hr}"

    wb.calculation.fullCalcOnLoad = True
    wb.save(OUT)
    print("saved", os.path.abspath(OUT), "vendors:", len(vendors))


if __name__ == "__main__":
    build()

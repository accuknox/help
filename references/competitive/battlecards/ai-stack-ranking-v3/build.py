"""Build the AI Security Stack Ranking v3 (Beta) workbook from vendors/*.json."""
import json, glob, os, sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.comments import Comment
from openpyxl.utils import get_column_letter

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "ai-security-stack-ranking-v3-beta.xlsx")
AS_OF = "September 2026"

TICK, DASH, CROSS = "✓", "−", "✗"
SYM = {"yes": TICK, "partial": DASH, "no": CROSS}
WORD = {"yes": "Supported", "partial": "Partial", "no": "No public evidence"}

MODULES = [
    ("1", "AI-SPM", "AI Security Posture Management",
     "AI asset inventory across clouds and on-prem. Shadow AI detection. AI pipeline and supply-chain posture."),
    ("2", "Agentic AI", "Agentic AI Security",
     "Security for agents on Bedrock AgentCore, Copilot Studio, Agentforce, Azure AI Foundry. MCP server security. Agent sandboxing, tool-call policy and egress control (AccuKnox AgentZ)."),
    ("3", "AI-DR", "AI Detect and Respond",
     "Attack and anomaly detection on AI apps and agents. Incident response, auto-remediation, SIEM and ITSM tickets. Runtime enforcement on AI workloads."),
    ("4", "Guardrails + AI Gateway", "AI Guardrails, Prompt Firewall and AI Gateway",
     "Inline enforcement through an AI gateway, proxy, SDK or browser plugin. Prompt injection, jailbreak and PII blocking. Unsafe output filtering."),
    ("5", "Compliance", "AI Compliance and Governance",
     "AIBOM and model inventory records. Mapping to NIST AI RMF, ISO 42001, OWASP LLM Top 10, EU AI Act, MITRE ATLAS. Audit trails and reports."),
    ("6", "Red Team + AI DAST", "AI Red Teaming and AI DAST",
     "Automated adversarial attack library. Multi-turn attacks against live AI apps and endpoints (AI DAST). Continuous and CI/CD red teaming."),
    ("7", "AI Identity", "AI Identity Security",
     "Agent and workload identity. Fine-grained, least-privilege authorization for agents and tools. Non-human identity discovery and governance."),
    ("8", "Model, Data + AI SAST", "AI Model, Dataset and Code Security (AI SAST)",
     "Model file scanning (Pickle, safetensors, GGUF, ONNX). Dataset PII and poisoning checks. AI SAST on source code and AI-generated code."),
]

ARIAL = "Arial"
NAVY = "000025"
BLUE = "005BFF"
FILL = {
    "yes": PatternFill("solid", fgColor="DCF5E3"),
    "partial": PatternFill("solid", fgColor="FFF1CC"),
    "no": PatternFill("solid", fgColor="FBE1E1"),
}
COLOR = {"yes": "137333", "partial": "9A6700", "no": "B3261E"}
HEAD_FILL = PatternFill("solid", fgColor=NAVY)
AK_FILL = PatternFill("solid", fgColor="E8EFFF")
thin = Side(style="thin", color="D0D5DD")
BOX = Border(left=thin, right=thin, top=thin, bottom=thin)


def f(size=10, bold=False, color="1F2937", underline=None, italic=False):
    return Font(name=ARIAL, size=size, bold=bold, color=color, underline=underline, italic=italic)


def load():
    rows = []
    for p in glob.glob(os.path.join(HERE, os.environ.get("VENDOR_DIR", "vendors_v2"), "*.json")):
        d = json.load(open(p, encoding="utf-8"))
        rows.append(d)
    def score(d):
        return sum({"yes": 1, "partial": 0.5}.get(d["modules"][m[0]]["status"], 0) for m in MODULES)
    ak = [d for d in rows if d["slug"] == "accuknox"]
    rest = sorted([d for d in rows if d["slug"] != "accuknox"], key=lambda d: (-score(d), d["vendor"].lower()))
    return ak + rest


def build():
    vendors = load()
    wb = Workbook()

    # ---------- Sheet 1: Stack Ranking ----------
    ws = wb.active
    ws.title = "Stack Ranking"
    ncol = 3 + len(MODULES) + 1
    last = get_column_letter(ncol)
    ws["A1"] = "AI Security Competitive Stack Ranking  |  v3 (BETA)"
    ws["A1"].font = f(16, True, NAVY)
    ws["A2"] = (f"AccuKnox against {len(vendors) - 1} AI security vendors on 8 modules. Research as of {AS_OF}. "
                "Hover a cell for the reason. The Evidence tab has the reasoning and source link for every cell.")
    ws["A2"].font = f(10, color="4B5563")
    ws["A3"] = (f"{TICK} Supported: GA and documented on the vendor's site      "
                f"{DASH} Partial: narrower scope, beta or roadmap      "
                f"{CROSS} No public evidence found")
    ws["A3"].font = f(10, True, "374151")
    ws["A4"] = ("BETA in v3: AccuKnox AI Gateway (module 4), AI DAST (module 6) and AI SAST (module 8) are upcoming. "
                "Each AccuKnox tick rests on GA features. The Beta tag marks the new sub-feature.")
    ws["A4"].font = f(10, True, BLUE)
    for r in (1, 2, 3, 4):
        ws.merge_cells(f"A{r}:{last}{r}")

    hr = 6
    heads = ["Rank", "Vendor", "What it sells"] + [f"{m[0]}. {m[1]}" for m in MODULES] + ["Score (of 8)"]
    for c, h in enumerate(heads, 1):
        cell = ws.cell(hr, c, h)
        cell.font = f(10, True, "FFFFFF")
        cell.fill = HEAD_FILL
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = BOX
    ws.row_dimensions[hr].height = 42

    first = hr + 1
    lastrow = first + len(vendors) - 1
    ev_row = {}  # (slug, module) -> evidence sheet row
    r_ev = 3
    for d in vendors:
        for m in MODULES:
            ev_row[(d["slug"], m[0])] = r_ev
            r_ev += 1

    for i, d in enumerate(vendors):
        r = first + i
        sc = get_column_letter(ncol)
        mfirst, mlast = get_column_letter(4), get_column_letter(3 + len(MODULES))
        ws.cell(r, 1, f"=RANK({sc}{r},${sc}${first}:${sc}${lastrow})")
        ws.cell(r, 2, d["vendor"])
        ws.cell(r, 3, d.get("what_it_is", ""))
        for j, m in enumerate(MODULES):
            mod = d["modules"][m[0]]
            st = mod["status"]
            label = SYM[st] + (" Beta" if mod.get("beta") else "")
            cell = ws.cell(r, 4 + j, label)
            cell.font = f(12, True, COLOR[st], underline=None)
            cell.fill = FILL[st]
            cell.alignment = Alignment(horizontal="center", vertical="center")
            note = f"{WORD[st]}: {mod['reason']}"
            cm = Comment(note, "AccuKnox")
            cm.width, cm.height = 300, 110
            cell.comment = cm
        ws.cell(r, ncol, f'=COUNTIF({mfirst}{r}:{mlast}{r},"{TICK}*")+0.5*COUNTIF({mfirst}{r}:{mlast}{r},"{DASH}*")')
        for c in (1, 2, 3, ncol):
            cell = ws.cell(r, c)
            cell.font = f(9 if c == 3 else 10, c in (1, 2, ncol), NAVY if c == 2 else "1F2937")
            cell.alignment = Alignment(horizontal="center" if c in (1, ncol) else "left", vertical="center", wrap_text=(c == 3))
        for c in range(1, ncol + 1):
            ws.cell(r, c).border = BOX
            if d["slug"] == "accuknox" and c in (1, 2, 3, ncol):
                ws.cell(r, c).fill = AK_FILL
        ws.cell(r, ncol).number_format = "0.0"
        ws.row_dimensions[r].height = 34

    widths = [6, 18, 54] + [12.5] * len(MODULES) + [9]
    for c, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(c)].width = w
    ws.freeze_panes = ws.cell(first, 3)
    for sh in (ws,):
        sh.page_setup.orientation = "landscape"
        sh.page_setup.fitToWidth = 1
        sh.page_setup.fitToHeight = 0
        sh.sheet_properties.pageSetUpPr.fitToPage = True
    ws.sheet_view.zoomScale = 100
    n = lastrow + 2
    ws.cell(n, 1, "Score: Supported = 1, Partial = 0.5, No public evidence = 0. Rank ties share a number. "
                  "Every competitor cell cites the vendor's own page where one exists. See the Evidence tab.").font = f(9, italic=True, color="6B7280")
    ws.merge_cells(start_row=n, start_column=1, end_row=n, end_column=ncol)

    # ---------- Sheet 2: Evidence ----------
    ev = wb.create_sheet("Evidence")
    ev["A1"] = "Evidence  |  one row per vendor and module"
    ev["A1"].font = f(14, True, NAVY)
    eh = ["Vendor", "Module", "Status", "Reasoning", "Reference link", "Source type"]
    for c, h in enumerate(eh, 1):
        cell = ev.cell(2, c, h)
        cell.font = f(10, True, "FFFFFF")
        cell.fill = HEAD_FILL
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = BOX
    for d in vendors:
        for m in MODULES:
            r = ev_row[(d["slug"], m[0])]
            mod = d["modules"][m[0]]
            st = mod["status"]
            reason = mod["reason"]
            vals = [d["vendor"], f"{m[0]}. {m[2]}", f"{SYM[st]} {WORD[st]}", reason, mod["url"],
                    "Vendor site" if mod.get("url_type", "vendor") == "vendor" else "Third party"]
            for c, v in enumerate(vals, 1):
                cell = ev.cell(r, c, v)
                cell.font = f(10)
                cell.alignment = Alignment(vertical="top", wrap_text=c in (2, 4, 5))
                cell.border = BOX
            ev.cell(r, 3).font = f(10, True, COLOR[st])
            ev.cell(r, 3).fill = FILL[st]
            ev.cell(r, 5).hyperlink = mod["url"]
            ev.cell(r, 5).font = f(10, color=BLUE, underline="single")
            if d["slug"] == "accuknox":
                ev.cell(r, 1).fill = AK_FILL
    for c, w in enumerate([18, 30, 20, 62, 48, 12], 1):
        ev.column_dimensions[get_column_letter(c)].width = w
    ev.freeze_panes = "B3"
    ev.page_setup.orientation = "landscape"
    ev.page_setup.fitToWidth = 1
    ev.page_setup.fitToHeight = 0
    ev.sheet_properties.pageSetUpPr.fitToPage = True
    ev.auto_filter.ref = f"A2:F{r_ev - 1}"

    # ---------- Sheet 3: Modules ----------
    md = wb.create_sheet("Modules")
    md["A1"] = "The 8 Modules and What Changed in v3"
    md["A1"].font = f(14, True, NAVY)
    for c, h in enumerate(["#", "Module", "What a tick requires"], 1):
        cell = md.cell(2, c, h)
        cell.font = f(10, True, "FFFFFF")
        cell.fill = HEAD_FILL
        cell.border = BOX
    for i, m in enumerate(MODULES):
        r = 3 + i
        for c, v in enumerate([m[0], m[2], m[3]], 1):
            cell = md.cell(r, c, v)
            cell.font = f(10, c == 2)
            cell.alignment = Alignment(vertical="top", wrap_text=True)
            cell.border = BOX
        md.row_dimensions[r].height = 44
    r = 3 + len(MODULES) + 1
    notes = [
        "Changes from v2",
        "Vendor list replaced with the 23 vendors from the v3 request. AccuKnox stays in row 1.",
        "Rows and columns swapped: vendors are rows, modules are columns.",
        "AI Gateway folded into module 4, AI DAST into module 6, AI SAST into module 8. All three are beta.",
        "Module 2 now credits AgentZ, the AccuKnox zero trust agentic platform.",
        "The probe-count claim is removed. The help docs say red teaming scales to hundreds of probes.",
        "How a cell is scored",
        f"{TICK} Supported: GA, documented on the vendor's site, and covers at least 2 of the 3 parts of the module.",
        f"{DASH} Partial: covers 1 part, a narrower version, or the feature is beta, preview or roadmap.",
        f"{CROSS} No public evidence: two or more targeted searches and a read of the vendor's product pages found nothing.",
        "Verification ran three times. Pass 1 researched each vendor. Pass 2 used a different researcher to re-score every cell with strict tests.",
        "Pass 3 re-searched every No, checked that all links load, and confirmed the Fortinet and Anaconda acquisitions.",
    ]
    for t in notes:
        cell = md.cell(r, 1, t)
        head = t in ("Changes from v2", "How a cell is scored")
        cell.font = f(11 if head else 10, head, NAVY if head else "1F2937")
        md.merge_cells(start_row=r, start_column=1, end_row=r, end_column=3)
        r += 1
    for c, w in enumerate([5, 44, 100], 1):
        md.column_dimensions[get_column_letter(c)].width = w

    for s in wb.worksheets:
        s.sheet_view.showGridLines = False
    wb.calculation.fullCalcOnLoad = True
    wb.save(OUT)
    print("saved", OUT, "vendors:", len(vendors))


if __name__ == "__main__":
    build()

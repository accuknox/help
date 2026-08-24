"""
CWPP Report Generator
Produces a CWPP (Cloud Workload Protection Platform) PDF report
visually aligned with the existing ASPM/CSPM/AISPM/Compliance reports.

Sample data is illustrative only; the structure is the deliverable.
"""

import io
import os
from datetime import datetime

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.ticker import MaxNLocator
import numpy as np

from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_PDF = os.path.join(OUT_DIR, "..", "Cloud Workload Protection Management Report (CWPP).pdf")
LOGO_WHITE = r"D:\Atharva\AccuKnox\HelpDocs\docs\assets\images\logo-white.png"
LOGO_DARK  = r"D:\Atharva\AccuKnox\HelpDocs\docs\assets\images\logo-black.png"

# Brand palette derived from the reference PDFs
BRAND_BLUE   = HexColor("#2A2DEE")
BRAND_RED    = HexColor("#E63946")
BRAND_CRIT   = HexColor("#7A0E11")
BRAND_HIGH   = HexColor("#E63946")
BRAND_MED    = HexColor("#F4A261")
BRAND_LOW    = HexColor("#E6C229")
BRAND_OK     = HexColor("#2A9D8F")
TEXT_DARK    = HexColor("#0E1330")
TEXT_MUTED   = HexColor("#5A6072")
CARD_BORDER  = HexColor("#E5E7EB")
LIGHT_BG     = HexColor("#F8FAFC")

PAGE_W, PAGE_H = A4   # 595 x 842 pt
MARGIN_X = 36

REPORT_PERIOD_START = "Feb 12, 2025 12:00:00"
REPORT_PERIOD_END   = "Mar 12, 2025 12:00:00"
REPORT_FOR = "Acme Corp"


# -----------------------------------------------------------------------------
# Matplotlib helpers — return PNG bytes that we embed into the PDF
# -----------------------------------------------------------------------------
def _fig_to_image(fig, dpi=180):
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=dpi, bbox_inches="tight", pad_inches=0.05,
                facecolor="white")
    plt.close(fig)
    buf.seek(0)
    return ImageReader(buf)


def donut(values, labels, colors, center_label, center_sub="", figsize=(3.2, 2.4)):
    fig, ax = plt.subplots(figsize=figsize)
    wedges, _ = ax.pie(values, colors=colors, startangle=90, counterclock=False,
                       wedgeprops=dict(width=0.32, edgecolor="white", linewidth=2))
    ax.text(0, 0.05, center_label, ha="center", va="center",
            fontsize=16, fontweight="bold", color="#0E1330")
    if center_sub:
        ax.text(0, -0.16, center_sub, ha="center", va="center",
                fontsize=7, color="#5A6072")
    ax.axis("equal")
    return _fig_to_image(fig)


def donut_with_legend(c_canvas, x, y, w, h, title, values, labels, colors,
                      center_label, center_sub=""):
    """Render a card with donut on left ~55% and a tidy legend on right ~45%."""
    card(c_canvas, x, y, w, h, title)
    donut_w = w * 0.55
    legend_w = w - donut_w
    img = donut(values, labels, colors, center_label, center_sub,
                figsize=(2.6, 2.2))
    draw_image_in_card(c_canvas, img, x + 6, y + 8, donut_w - 12, h - 30,
                       pad_top=6, pad_x=4, pad_bottom=4)
    lx = x + donut_w + 6
    rows = list(zip(labels, [_fmt_legend_val(v) for v in values], colors))
    line_h = 13
    legend_total_h = len(rows) * line_h
    ly = y + h / 2 + legend_total_h / 2 - 8
    c_canvas.setFont("Helvetica", 8)
    for name, val, col in rows:
        c_canvas.setFillColor(HexColor(col))
        c_canvas.circle(lx, ly + 3, 3, stroke=0, fill=1)
        c_canvas.setFillColor(TEXT_DARK)
        c_canvas.drawString(lx + 9, ly, name)
        c_canvas.setFillColor(TEXT_MUTED)
        c_canvas.drawRightString(x + w - 14, ly, val)
        ly -= line_h


def _fmt_legend_val(v):
    if v >= 10000:
        return f"{v/1000:.1f}k"
    if v >= 1000:
        return f"{v/1000:.1f}k" if v % 1000 else f"{v//1000}k"
    return str(v)


def hbar(labels, values, colors=None, figsize=(4.2, 2.4), value_fmt="{:,}",
         max_label=24):
    fig, ax = plt.subplots(figsize=figsize)
    labels = [l if len(l) <= max_label else l[:max_label-1] + "…" for l in labels]
    y = np.arange(len(labels))
    if colors is None:
        colors = ["#2A2DEE"] * len(labels)
    ax.barh(y, values, color=colors, edgecolor="white")
    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=8)
    ax.invert_yaxis()
    ax.tick_params(axis="x", labelsize=7, colors="#5A6072")
    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)
    for spine in ["left", "bottom"]:
        ax.spines[spine].set_color("#E5E7EB")
    ax.xaxis.set_major_locator(MaxNLocator(nbins=4, integer=True))
    for i, v in enumerate(values):
        ax.text(v, i, "  " + value_fmt.format(v), va="center", fontsize=8,
                color="#0E1330")
    ax.margins(x=0.18)
    return _fig_to_image(fig)


def stacked_vbar(categories, series, colors, labels, figsize=(4.5, 2.4),
                 rotate_x=0):
    fig, ax = plt.subplots(figsize=figsize)
    x = np.arange(len(categories))
    bottom = np.zeros(len(categories))
    for i, s in enumerate(series):
        ax.bar(x, s, bottom=bottom, color=colors[i], label=labels[i], width=0.55,
               edgecolor="white", linewidth=1)
        bottom += np.array(s)
    totals = bottom
    for xi, t in zip(x, totals):
        ax.text(xi, t, f"{int(t)}", ha="center", va="bottom", fontsize=8,
                color="#0E1330")
    ax.set_xticks(x)
    ax.set_xticklabels(categories, fontsize=7.5,
                       rotation=rotate_x,
                       ha="right" if rotate_x else "center")
    ax.tick_params(axis="y", labelsize=7, colors="#5A6072")
    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, 1.18), ncol=len(labels),
              fontsize=7, frameon=False)
    return _fig_to_image(fig)


def line_trend(x, y_series, labels, colors, figsize=(4.2, 1.9), fill=True):
    fig, ax = plt.subplots(figsize=figsize)
    for ys, lbl, c in zip(y_series, labels, colors):
        ax.plot(x, ys, color=c, linewidth=1.8, label=lbl)
        if fill:
            ax.fill_between(x, ys, alpha=0.08, color=c)
    ax.tick_params(axis="both", labelsize=7, colors="#5A6072")
    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)
    for spine in ["left", "bottom"]:
        ax.spines[spine].set_color("#E5E7EB")
    if any(labels):
        ax.legend(loc="upper left", fontsize=7, frameon=False)
    return _fig_to_image(fig)


def heatmap_mitre(tactics, techniques_per_tactic, intensity, figsize=(5.6, 2.4)):
    fig, ax = plt.subplots(figsize=figsize)
    n = len(tactics)
    cols = n
    cmap = plt.cm.Reds
    data = np.array(intensity).reshape(1, -1)
    im = ax.imshow(data, aspect="auto", cmap=cmap, vmin=0, vmax=max(intensity) or 1)
    ax.set_xticks(range(cols))
    ax.set_xticklabels(tactics, rotation=30, ha="right", fontsize=7)
    ax.set_yticks([0])
    ax.set_yticklabels(["Detections"], fontsize=7)
    for i, (t, v) in enumerate(zip(techniques_per_tactic, intensity)):
        ax.text(i, 0, f"{v}\n({t})", ha="center", va="center",
                fontsize=7, color="white" if v > max(intensity)*0.5 else "#0E1330")
    ax.set_xticks(np.arange(-.5, cols, 1), minor=True)
    ax.grid(which="minor", color="white", linewidth=2)
    ax.tick_params(which="minor", length=0)
    return _fig_to_image(fig)


# -----------------------------------------------------------------------------
# Layout primitives
# -----------------------------------------------------------------------------
def draw_top_accent(c):
    """Thin pink/blue gradient accent at very top of content pages."""
    n_steps = 80
    width = PAGE_W / n_steps
    for i in range(n_steps):
        ratio = i / n_steps
        r = (1 - ratio) * 0.90 + ratio * 0.16
        g = (1 - ratio) * 0.22 + ratio * 0.18
        b = (1 - ratio) * 0.31 + ratio * 0.93
        c.setFillColorRGB(r, g, b)
        c.rect(i * width, PAGE_H - 4, width + 0.6, 4, stroke=0, fill=1)


def draw_page_footer(c, page_num):
    c.setFillColor(TEXT_MUTED)
    c.setFont("Helvetica", 8)
    # Center: Private & Confidential
    c.drawCentredString(PAGE_W / 2, 20, "Private & Confidential")
    # Right: page number
    c.drawRightString(PAGE_W - MARGIN_X, 20, str(page_num))
    # Left: AccuKnox small mark
    try:
        c.drawImage(LOGO_DARK, MARGIN_X, 12, width=58, height=18,
                    preserveAspectRatio=True, mask="auto")
    except Exception:
        pass


def draw_section_header(c, title, period_text=None):
    c.setFillColor(TEXT_DARK)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(MARGIN_X, PAGE_H - 56, title)
    if period_text:
        c.setFillColor(TEXT_DARK)
        c.setFont("Helvetica", 8)
        for i, line in enumerate(period_text.split("\n")):
            c.drawRightString(PAGE_W - MARGIN_X, PAGE_H - 50 - i * 10, line)


def card(c, x, y, w, h, title=None, info_dot=True):
    """Rounded card with optional title."""
    c.setStrokeColor(CARD_BORDER)
    c.setLineWidth(0.8)
    c.setFillColor(white)
    c.roundRect(x, y, w, h, 6, stroke=1, fill=1)
    if title:
        c.setFillColor(TEXT_DARK)
        c.setFont("Helvetica-Bold", 9.5)
        c.drawString(x + 12, y + h - 18, title)
        if info_dot:
            tw = c.stringWidth(title, "Helvetica-Bold", 9.5)
            cx = x + 12 + tw + 8
            cy = y + h - 14
            c.setStrokeColor(TEXT_MUTED)
            c.setLineWidth(0.6)
            c.setFillColor(white)
            c.circle(cx, cy, 4, stroke=1, fill=1)
            c.setFillColor(TEXT_MUTED)
            c.setFont("Helvetica-Bold", 5.5)
            c.drawCentredString(cx, cy - 2, "i")


def draw_image_in_card(c, image_reader, x, y, w, h, pad_top=22, pad_x=8,
                       pad_bottom=8):
    inner_w = w - 2 * pad_x
    inner_h = h - pad_top - pad_bottom
    c.drawImage(image_reader, x + pad_x, y + pad_bottom,
                width=inner_w, height=inner_h, preserveAspectRatio=True,
                anchor="c", mask="auto")


def wrapped_caption(c, text, x, y, max_width, font="Helvetica", size=7.5,
                    leading=10, color=TEXT_MUTED):
    """Render multi-line caption (wrap by words). Returns y after."""
    c.setFillColor(color)
    c.setFont(font, size)
    words = text.split()
    line = ""
    lines = []
    for w in words:
        test = (line + " " + w).strip()
        if c.stringWidth(test, font, size) <= max_width:
            line = test
        else:
            lines.append(line)
            line = w
    if line:
        lines.append(line)
    for ln in lines:
        c.drawString(x, y, ln)
        y -= leading
    return y


def kpi_card(c, x, y, w, h, label, value, sub=None, color_bar=BRAND_BLUE,
             value_color=TEXT_DARK):
    c.setStrokeColor(CARD_BORDER)
    c.setLineWidth(0.8)
    c.setFillColor(white)
    c.roundRect(x, y, w, h, 6, stroke=1, fill=1)
    # left color stripe
    c.setFillColor(color_bar)
    c.roundRect(x, y, 4, h, 2, stroke=0, fill=1)
    c.setFillColor(TEXT_MUTED)
    c.setFont("Helvetica", 8)
    c.drawString(x + 14, y + h - 14, label)
    c.setFillColor(value_color)
    c.setFont("Helvetica-Bold", 22)
    c.drawString(x + 14, y + h - 40, str(value))
    if sub:
        c.setFillColor(TEXT_MUTED)
        c.setFont("Helvetica", 7.5)
        c.drawString(x + 14, y + 10, sub)


# -----------------------------------------------------------------------------
# Cover page
# -----------------------------------------------------------------------------
def draw_cover(c):
    # Blue background top portion
    c.setFillColor(BRAND_BLUE)
    c.rect(0, PAGE_H * 0.32, PAGE_W, PAGE_H * 0.68, stroke=0, fill=1)

    # decorative arc lines on right (approx)
    c.setStrokeColor(HexColor("#FF6B6B"))
    c.setLineWidth(1.2)
    c.line(PAGE_W * 0.65, PAGE_H * 0.96, PAGE_W * 0.99, PAGE_H * 0.78)
    c.line(PAGE_W * 0.99, PAGE_H * 0.78, PAGE_W * 0.78, PAGE_H * 0.55)
    c.line(PAGE_W * 0.78, PAGE_H * 0.55, PAGE_W * 0.99, PAGE_H * 0.42)

    # Logo top-left
    try:
        c.drawImage(LOGO_WHITE, MARGIN_X, PAGE_H - 100, width=170, height=44,
                    preserveAspectRatio=True, mask="auto")
    except Exception:
        c.setFillColor(white)
        c.setFont("Helvetica-Bold", 24)
        c.drawString(MARGIN_X, PAGE_H - 80, "AccuKnox")

    # Title
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 30)
    c.drawString(MARGIN_X, PAGE_H - 200, "Cloud Workload Protection")
    c.drawString(MARGIN_X, PAGE_H - 234, "Management Report (CWPP)")

    # Period
    c.setFillColor(white)
    c.setFont("Helvetica", 10.5)
    period = f"Report Period 30 Days - {REPORT_PERIOD_START} to {REPORT_PERIOD_END} (IST)"
    c.drawString(MARGIN_X, PAGE_H - 258, period)

    # Bottom info block
    y_bottom = PAGE_H * 0.32
    c.setFillColor(TEXT_DARK)
    c.setFont("Helvetica", 10)
    c.drawString(MARGIN_X, y_bottom - 30, "Prepared for")
    c.drawString(MARGIN_X + 220, y_bottom - 30, "Prepared by")
    c.setFont("Helvetica-Bold", 11)
    c.drawString(MARGIN_X, y_bottom - 48, REPORT_FOR)
    c.drawString(MARGIN_X + 220, y_bottom - 48, "AccuKnox")
    c.setFont("Helvetica", 10)
    c.drawString(MARGIN_X + 220, y_bottom - 64, "support@accuknox.com")

    # Gradient separator
    n = 200
    seg_w = (PAGE_W - 2 * MARGIN_X) / n
    for i in range(n):
        ratio = i / n
        r = (1 - ratio) * 0.90 + ratio * 0.16
        g = (1 - ratio) * 0.22 + ratio * 0.18
        b = (1 - ratio) * 0.31 + ratio * 0.93
        c.setFillColorRGB(r, g, b)
        c.rect(MARGIN_X + i * seg_w, y_bottom - 90, seg_w + 0.6, 1.5,
               stroke=0, fill=1)

    # Report Summary
    c.setFillColor(TEXT_DARK)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(MARGIN_X, y_bottom - 120, "Report Summary")
    summary = (
        "The CWPP scan covered 11.2k workloads across 21 cloud accounts, 9 Kubernetes "
        "clusters, and 22.3k virtual machines spanning AWS, Azure, GCP, Oracle, and "
        "on-prem environments. KubeArmor recorded 12.8k runtime events — 2,658 blocked, "
        "5,232 audited, and 4,992 audit-then-block. A total of 1,869 hardening "
        "policies were enforced across 850 namespaces. Cluster posture surfaced 1,771 "
        "findings (12 Critical, 12 High, 1,091 Medium, 656 Low). VM workload "
        "protection identified 171 exploitable VMs, 128 exploitable CVEs, and 201 "
        "over-privileged VMs, with mean time to remediate at 58 hours."
    )
    c.setFont("Helvetica", 10)
    wrapped_caption(c, summary, MARGIN_X, y_bottom - 138,
                    PAGE_W - 2 * MARGIN_X, font="Helvetica", size=9.5, leading=13,
                    color=TEXT_DARK)

    # bottom-of-cover label
    c.setFillColor(TEXT_MUTED)
    c.setFont("Helvetica", 8)
    c.drawCentredString(PAGE_W / 2, 20, "Private & Confidential")


# -----------------------------------------------------------------------------
# Per-page builders
# -----------------------------------------------------------------------------
def page_inventory_1(c, page_num):
    draw_top_accent(c)
    draw_section_header(c, "Workload Inventory & Coverage",
                        f"{REPORT_PERIOD_START}\nto {REPORT_PERIOD_END}")

    # KPI strip (top)
    top_y = PAGE_H - 135
    strip_h = 60
    strip_w = (PAGE_W - 2 * MARGIN_X - 3 * 8) / 4
    kpis = [
        ("Total Workloads", "11.2k", "VMs + Pods + Serverless", BRAND_BLUE),
        ("Virtual Machines", "22.3k", "AWS, Azure, GCP, OCI, vSphere", BRAND_OK),
        ("K8s Clusters", "9", "150 connected nodes", BRAND_HIGH),
        ("Serverless / Functions", "1.0k", "Lambda + Cloud Run", BRAND_MED),
    ]
    for i, (lbl, val, sub, col) in enumerate(kpis):
        kpi_card(c, MARGIN_X + i * (strip_w + 8), top_y, strip_w, strip_h, lbl,
                 val, sub, col)

    # Two cards: Workloads by Cloud Provider (donut), Cluster Connection Status (donut)
    card_y = top_y - 230
    card_h = 215
    card_w = (PAGE_W - 2 * MARGIN_X - 10) / 2
    card_x2 = MARGIN_X + card_w + 10

    donut_with_legend(
        c, MARGIN_X, card_y, card_w, card_h, "Workloads by Cloud Provider",
        values=[18500, 1500, 1500, 500, 300],
        labels=["AWS", "Azure", "GCP", "Oracle", "On-Prem"],
        colors=["#2A2DEE", "#62A8FF", "#B6CFFF", "#E63946", "#E5E7EB"],
        center_label="22.3k", center_sub="Workloads",
    )
    donut_with_legend(
        c, card_x2, card_y, card_w, card_h, "Cluster Connection Status",
        values=[150, 50],
        labels=["Connected", "Disconnected"],
        colors=["#2A9D8F", "#E63946"],
        center_label="200", center_sub="Clusters",
    )

    # Captions
    cap_y = card_y - 8
    cap_w = card_w
    cap_y_after = wrapped_caption(
        c,
        "Snapshot of workloads onboarded into AccuKnox CWPP, segmented by cloud "
        "provider. Use this to confirm full estate coverage and find provider gaps.",
        MARGIN_X, cap_y, cap_w,
    )
    wrapped_caption(
        c,
        "Live count of clusters with active KubeArmor / Feeder Service agents. "
        "Disconnected clusters are blind spots for runtime detection and blocking.",
        card_x2, cap_y, cap_w,
    )

    # Second row: KubeArmor Agent Coverage + Onboarding Trend
    row2_h = 175
    row2_y = cap_y_after - 18 - row2_h
    # Card 3: KubeArmor Agent Coverage
    card(c, MARGIN_X, row2_y, card_w, row2_h, "KubeArmor Agent Coverage")
    img3 = donut(
        values=[9650, 1550],
        labels=["Protected", "Unprotected"],
        colors=["#2A2DEE", "#E5E7EB"],
        center_label="86%", center_sub="of workloads",
    )
    draw_image_in_card(c, img3, MARGIN_X + 10, row2_y + 8, card_w - 20, row2_h - 30)

    # Card 4: Workload Onboarding Trend
    card(c, card_x2, row2_y, card_w, row2_h, "Workload Onboarding Trend")
    months = ["Feb 12", "Feb 19", "Feb 26", "Mar 05", "Mar 12"]
    series = [[7800, 8400, 9100, 10350, 11200]]
    img4 = line_trend(months, series, ["Workloads"], ["#2A2DEE"], figsize=(4.0, 1.8))
    draw_image_in_card(c, img4, card_x2 + 10, row2_y + 8, card_w - 20, row2_h - 30)

    draw_page_footer(c, page_num)


def page_inventory_2(c, page_num):
    draw_top_accent(c)
    draw_section_header(c, "Workload Inventory & Coverage",
                        f"{REPORT_PERIOD_START}\nto {REPORT_PERIOD_END}")

    top_y = PAGE_H - 270
    card_h = 175
    card_w = (PAGE_W - 2 * MARGIN_X - 10) / 2

    # VM OS Distribution
    card(c, MARGIN_X, top_y, card_w, card_h, "VM OS Distribution")
    cats = ["AWS", "Azure", "GCP"]
    linux = [60, 60, 50]
    windows = [10, 70, 50]
    other = [15, 25, 40]
    img = stacked_vbar(cats, [linux, windows, other],
                       ["#2A2DEE", "#62A8FF", "#B6CFFF"],
                       ["Linux", "Windows", "Others"], figsize=(4.0, 1.9))
    draw_image_in_card(c, img, MARGIN_X + 10, top_y + 8, card_w - 20, card_h - 30)

    # EOL VMs
    card_x2 = MARGIN_X + card_w + 10
    card(c, card_x2, top_y, card_w, card_h, "End of Life (EOL) VMs")
    cats = [">30 days expired", ">60 days expired", "Immediate", "< 30 days", "31-60 days"]
    vals = [60, 50, 80, 156, 138]
    img = hbar(cats, vals, ["#E63946"]*5, figsize=(4.0, 1.9))
    draw_image_in_card(c, img, card_x2 + 10, top_y + 8, card_w - 20, card_h - 30)

    cap_y = top_y - 8
    cap_y2 = wrapped_caption(
        c,
        "OS-level fleet distribution across cloud providers. Helps surface heavy "
        "Windows or legacy Linux exposure where KubeArmor host policies must be "
        "deployed.",
        MARGIN_X, cap_y, card_w,
    )
    wrapped_caption(
        c,
        "VMs running operating systems past their EOL support window. These cannot "
        "receive vendor patches and represent the highest-priority replacement risk.",
        card_x2, cap_y, card_w,
    )

    # Row 2: Clusters with Public Exposure + Asset categories
    row2_h = 200
    row2_y = cap_y2 - 18 - row2_h
    card(c, MARGIN_X, row2_y, card_w, row2_h, "Clusters with Public Exposure")
    cats = ["prod-api-cluster", "staging-core-services", "frontend-v2", "analytics-datahub", "devops-tool"]
    vals = [314080, 626545, 4290, 15741, 1199]
    img = hbar(cats, [v/1000 for v in vals], ["#E63946", "#F4A261", "#E63946", "#F4A261", "#E6C229"],
               figsize=(4.0, 2.0), value_fmt="{:.1f}k", max_label=22)
    draw_image_in_card(c, img, MARGIN_X + 10, row2_y + 8, card_w - 20, row2_h - 30)

    card(c, card_x2, row2_y, card_w, row2_h, "Findings by Asset Category")
    cats = ["Containers", "AWS Identity", "ML Serverless", "Database", "Storage"]
    crit = [100, 350, 3, 2, 1]
    high = [75, 50, 2, 0, 0]
    med  = [15, 25, 5, 0, 0]
    low  = [10, 25, 5, 0, 0]
    img = stacked_vbar(cats, [crit, high, med, low],
                       ["#7A0E11", "#E63946", "#F4A261", "#E6C229"],
                       ["Critical", "High", "Medium", "Low"], figsize=(4.0, 2.2),
                       rotate_x=20)
    draw_image_in_card(c, img, card_x2 + 10, row2_y + 8, card_w - 20, row2_h - 30)

    cap_y3 = row2_y - 8
    wrapped_caption(
        c,
        "Clusters exposing the largest aggregate ingress/egress workload counts. "
        "Combine with KIEM and KubeArmor network policies to reduce attack surface.",
        MARGIN_X, cap_y3, card_w,
    )
    wrapped_caption(
        c,
        "Findings sliced by asset category — containers, IAM, databases, storage, "
        "ML endpoints. Steer hardening focus to the category with the most critical "
        "exposure.",
        card_x2, cap_y3, card_w,
    )

    draw_page_footer(c, page_num)


def page_runtime_alerts(c, page_num):
    draw_top_accent(c)
    draw_section_header(c, "Runtime Threats & KubeArmor Alerts",
                        f"{REPORT_PERIOD_START}\nto {REPORT_PERIOD_END}")

    # Top KPI strip
    top_y = PAGE_H - 135
    strip_h = 60
    strip_w = (PAGE_W - 2 * MARGIN_X - 3 * 8) / 4
    kpis = [
        ("Total Alerts", "12.8k", "Across all enforcement modes", BRAND_BLUE),
        ("Blocked (Inline)", "2,658", "LSM-enforced prevention", BRAND_CRIT),
        ("Audited", "5,232", "Visible-only telemetry", BRAND_MED),
        ("Audit-then-Block", "4,992", "Promoted from observation", BRAND_HIGH),
    ]
    for i, (lbl, val, sub, col) in enumerate(kpis):
        kpi_card(c, MARGIN_X + i * (strip_w + 8), top_y, strip_w, strip_h, lbl, val, sub, col)

    # Alerts by severity (stacked)
    row1_h = 200
    row1_y = top_y - 20 - row1_h
    card_w = (PAGE_W - 2 * MARGIN_X - 10) / 2
    card_x2 = MARGIN_X + card_w + 10

    card(c, MARGIN_X, row1_y, card_w, row1_h, "Alerts by Severity")
    cats = ["Critical", "High", "Medium", "Low"]
    vals = [3120, 4280, 3650, 1750]
    img = hbar(cats, vals, ["#7A0E11", "#E63946", "#F4A261", "#E6C229"], figsize=(4.0, 1.9))
    draw_image_in_card(c, img, MARGIN_X + 10, row1_y + 8, card_w - 20, row1_h - 30)

    # Alert volume trend
    card(c, card_x2, row1_y, card_w, row1_h, "Alert Volume Over Time")
    x = ["Feb 12", "Feb 19", "Feb 26", "Mar 05", "Mar 12"]
    blocked = [410, 520, 480, 620, 628]
    audited = [780, 1020, 1100, 1180, 1152]
    img = line_trend(x, [blocked, audited], ["Blocked", "Audited"],
                     ["#E63946", "#2A2DEE"], figsize=(4.0, 1.9))
    draw_image_in_card(c, img, card_x2 + 10, row1_y + 8, card_w - 20, row1_h - 30)

    cap_y = row1_y - 8
    cap_y2 = wrapped_caption(
        c,
        "Severity distribution of runtime alerts from KubeArmor across the period. "
        "Critical and High alerts indicate confirmed deny-list violations.",
        MARGIN_X, cap_y, card_w,
    )
    wrapped_caption(
        c,
        "Trend of blocked vs audited events. A rising 'Blocked' line means hardening "
        "policies are taking effect; rising 'Audited' indicates new behaviors worth "
        "promoting to block.",
        card_x2, cap_y, card_w,
    )

    # Row 2: Alerts by Action (audit/block split) full-width donut + summary
    row2_h = 195
    row2_y = cap_y2 - 18 - row2_h
    card(c, MARGIN_X, row2_y, PAGE_W - 2 * MARGIN_X, row2_h,
         "Alert Enforcement Breakdown")
    img = donut(
        values=[5232, 2658, 4992],
        labels=["Audit", "Block", "Audit-Block"],
        colors=["#2A2DEE", "#7A0E11", "#F4A261"],
        center_label="12.8k", center_sub="Total Events", figsize=(2.6, 2.2),
    )
    draw_image_in_card(c, img, MARGIN_X + 12, row2_y + 8, 200, row2_h - 30)
    # right side: enforcement notes
    nx = MARGIN_X + 224
    ny = row2_y + row2_h - 32
    c.setFillColor(TEXT_DARK)
    c.setFont("Helvetica-Bold", 9.5)
    c.drawString(nx, ny, "Enforcement Mode")
    ny -= 18
    rows = [
        ("Audit", "5,232", "AppArmor / BPF-LSM observation only.",
         "#2A2DEE"),
        ("Block", "2,658",
         "Inline-mitigated at the LSM hook for process, file, and network actions.",
         "#7A0E11"),
        ("Audit-then-Block", "4,992",
         "Behavior baselined first, then policy promoted to block on next match.",
         "#F4A261"),
    ]
    desc_max_w = PAGE_W - MARGIN_X - nx - 12 - 130
    c.setFont("Helvetica", 8.5)
    for name, count, desc, col in rows:
        c.setFillColor(HexColor(col))
        c.rect(nx, ny - 2, 8, 8, stroke=0, fill=1)
        c.setFillColor(TEXT_DARK)
        c.setFont("Helvetica-Bold", 8.5)
        c.drawString(nx + 14, ny, name)
        c.drawString(nx + 102, ny, count)
        ny_desc = ny
        ny_desc = wrapped_caption(
            c, desc, nx + 140, ny, desc_max_w,
            font="Helvetica", size=8, leading=10, color=TEXT_MUTED,
        )
        ny = min(ny - 16, ny_desc - 6)

    draw_page_footer(c, page_num)


def page_runtime_drilldown(c, page_num):
    draw_top_accent(c)
    draw_section_header(c, "Runtime Alerts — Drill-Down",
                        f"{REPORT_PERIOD_START}\nto {REPORT_PERIOD_END}")

    top_y = PAGE_H - 270
    card_h = 175
    card_w = (PAGE_W - 2 * MARGIN_X - 10) / 2
    card_x2 = MARGIN_X + card_w + 10

    # Top 5 namespaces
    card(c, MARGIN_X, top_y, card_w, card_h, "Top 5 Namespaces with Alerts")
    cats = ["default", "kube-system", "production-apps", "dev-team1", "monitoring"]
    vals = [600670, 14078, 1200, 359, 121]
    img = hbar(cats, [v/1000 for v in vals],
               ["#E63946", "#F4A261", "#E6C229", "#2A2DEE", "#62A8FF"],
               figsize=(4.0, 1.9), value_fmt="{:.1f}k", max_label=20)
    draw_image_in_card(c, img, MARGIN_X + 10, top_y + 8, card_w - 20, card_h - 30)

    # Top 5 workloads
    card(c, card_x2, top_y, card_w, card_h, "Top 5 Workloads with Alerts")
    cats = ["prod-api-cluster/default", "staging-core/-", "frontend-v2/prod-apps",
            "analytics-datahub/dev1", "devops-tool/-"]
    vals = [14078, 600670, 1200, 359, 121]
    img = hbar(cats, [v/1000 for v in vals],
               ["#7A0E11", "#E63946", "#F4A261", "#E6C229", "#62A8FF"],
               figsize=(4.0, 1.9), value_fmt="{:.1f}k", max_label=22)
    draw_image_in_card(c, img, card_x2 + 10, top_y + 8, card_w - 20, card_h - 30)

    cap_y = top_y - 8
    cap_y2 = wrapped_caption(
        c,
        "Namespaces generating the highest alert volume. High counts in 'default' or "
        "'kube-system' usually mean missing baseline policies or noisy DaemonSets.",
        MARGIN_X, cap_y, card_w,
    )
    wrapped_caption(
        c,
        "Workloads with the most KubeArmor alerts in scope. Use this list to "
        "prioritize policy refinement and process whitelisting.",
        card_x2, cap_y, card_w,
    )

    # Row 2: Top policies and block-based
    row2_h = 200
    row2_y = cap_y2 - 18 - row2_h
    card(c, MARGIN_X, row2_y, card_w, row2_h, "Policies Generating Maximum Alerts")
    cats = ["block-host-etc-access", "block-public-ingress", "block-shell-binaries-exec",
            "block-egress-external", "block-privileged-containers"]
    vals = [450, 200, 105, 15, 2]
    img = hbar(cats, vals, ["#7A0E11", "#E63946", "#F4A261", "#E6C229", "#2A2DEE"],
               figsize=(4.0, 2.0), max_label=28)
    draw_image_in_card(c, img, MARGIN_X + 10, row2_y + 8, card_w - 20, row2_h - 30)

    card(c, card_x2, row2_y, card_w, row2_h, "Block-Based Policies with Alerts")
    cats = ["block-host-etc-access", "block-public-ingress", "block-shell-binaries-exec",
            "block-egress-external", "block-privileged-containers"]
    vals = [2788, 98, 23, 8, 2]
    img = hbar(cats, vals, ["#7A0E11", "#7A0E11", "#E63946", "#E63946", "#F4A261"],
               figsize=(4.0, 2.0), max_label=28)
    draw_image_in_card(c, img, card_x2 + 10, row2_y + 8, card_w - 20, row2_h - 30)

    cap_y3 = row2_y - 8
    wrapped_caption(
        c,
        "Policies producing the most alerts overall, regardless of action. Re-tune "
        "noisy audit rules and confirm critical block rules are actively firing.",
        MARGIN_X, cap_y3, card_w,
    )
    wrapped_caption(
        c,
        "Subset of block-action (inline-mitigated) policies, ranked by alert count. "
        "These represent confirmed attacks or violations that were prevented.",
        card_x2, cap_y3, card_w,
    )

    draw_page_footer(c, page_num)


def page_app_behavior(c, page_num):
    draw_top_accent(c)
    draw_section_header(c, "Application Behavior & Observability",
                        f"{REPORT_PERIOD_START}\nto {REPORT_PERIOD_END}")

    # Three column KPI of top processes, top files, top network
    top_y = PAGE_H - 135
    strip_h = 60
    strip_w = (PAGE_W - 2 * MARGIN_X - 2 * 8) / 3
    kpis = [
        ("Process Events", "1.42M", "Distinct exec / fork events", BRAND_BLUE),
        ("File Access Events", "892k", "Read / write / link events", BRAND_OK),
        ("Network Flows", "203k", "Egress + Ingress connections", BRAND_HIGH),
    ]
    for i, (lbl, val, sub, col) in enumerate(kpis):
        kpi_card(c, MARGIN_X + i * (strip_w + 8), top_y, strip_w, strip_h, lbl, val, sub, col)

    # Row: Top processes + Top files
    row1_h = 180
    row1_y = top_y - 20 - row1_h
    card_w = (PAGE_W - 2 * MARGIN_X - 10) / 2
    card_x2 = MARGIN_X + card_w + 10

    card(c, MARGIN_X, row1_y, card_w, row1_h, "Top Process Executions Observed")
    cats = ["/usr/bin/curl", "/bin/sh", "/usr/sbin/nginx", "/usr/local/bin/node", "/bin/bash"]
    vals = [482000, 312000, 198000, 142000, 88000]
    img = hbar(cats, [v/1000 for v in vals],
               ["#2A2DEE"]*5, figsize=(4.0, 1.9), value_fmt="{:.0f}k", max_label=24)
    draw_image_in_card(c, img, MARGIN_X + 10, row1_y + 8, card_w - 20, row1_h - 30)

    card(c, card_x2, row1_y, card_w, row1_h, "Top File Paths Accessed")
    cats = ["/etc/passwd", "/etc/shadow", "/var/log/syslog", "/proc/self/maps", "/root/.ssh/authorized_keys"]
    vals = [240000, 95000, 87000, 64000, 38000]
    img = hbar(cats, [v/1000 for v in vals],
               ["#7A0E11", "#7A0E11", "#E63946", "#F4A261", "#E63946"],
               figsize=(4.0, 1.9), value_fmt="{:.0f}k", max_label=28)
    draw_image_in_card(c, img, card_x2 + 10, row1_y + 8, card_w - 20, row1_h - 30)

    cap_y = row1_y - 8
    cap_y2 = wrapped_caption(
        c,
        "Most-observed process executions across protected workloads. Anomalous "
        "binaries here are candidates for the deny-by-default process whitelist.",
        MARGIN_X, cap_y, card_w,
    )
    wrapped_caption(
        c,
        "Most-accessed file paths from KubeArmor file observability. Sensitive "
        "system files in this list indicate FIM-worthy assets.",
        card_x2, cap_y, card_w,
    )

    # Row 2: Top egress / ingress
    row2_h = 200
    row2_y = cap_y2 - 18 - row2_h
    card(c, MARGIN_X, row2_y, PAGE_W - 2 * MARGIN_X, row2_h,
         "Top 5 K8s External Egress/Ingress Workloads")
    cats = ["default", "node-kubesystem", "production-apps", "dev-team-1", "node-monitoring-elf"]
    ingress = [8690, 5623, 4799, 8500, 1100]
    egress = [16700, 2200, 8000, 8500, 15600]
    fig, ax = plt.subplots(figsize=(7.5, 2.3))
    y = np.arange(len(cats))
    ax.barh(y - 0.18, ingress, height=0.34, color="#2A2DEE", label="Ingress")
    ax.barh(y + 0.18, egress, height=0.34, color="#62A8FF", label="Egress")
    ax.set_yticks(y); ax.set_yticklabels(cats, fontsize=8)
    ax.invert_yaxis()
    ax.tick_params(axis="x", labelsize=7, colors="#5A6072")
    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)
    for spine in ["left", "bottom"]:
        ax.spines[spine].set_color("#E5E7EB")
    ax.legend(loc="lower right", fontsize=8, frameon=False)
    img = _fig_to_image(fig)
    draw_image_in_card(c, img, MARGIN_X + 10, row2_y + 8,
                       PAGE_W - 2 * MARGIN_X - 20, row2_h - 30)

    draw_page_footer(c, page_num)


def page_hardening(c, page_num):
    draw_top_accent(c)
    draw_section_header(c, "Workload Hardening & Policy Enforcement",
                        f"{REPORT_PERIOD_START}\nto {REPORT_PERIOD_END}")

    # KPI strip
    top_y = PAGE_H - 135
    strip_h = 60
    strip_w = (PAGE_W - 2 * MARGIN_X - 3 * 8) / 4
    kpis = [
        ("Active Policies", "1,869", "Across all clusters & VMs", BRAND_BLUE),
        ("Workloads Covered", "9,652", "86% of estate", BRAND_OK),
        ("Coverage Gap", "1,548", "Workloads without policy", BRAND_HIGH),
        ("Discovered (Pending)", "412", "Recommended by Discovery Engine", BRAND_MED),
    ]
    for i, (lbl, val, sub, col) in enumerate(kpis):
        kpi_card(c, MARGIN_X + i * (strip_w + 8), top_y, strip_w, strip_h, lbl, val, sub, col)

    # Hardening coverage by category
    row1_h = 200
    row1_y = top_y - 20 - row1_h
    card_w = (PAGE_W - 2 * MARGIN_X - 10) / 2
    card_x2 = MARGIN_X + card_w + 10

    card(c, MARGIN_X, row1_y, card_w, row1_h, "Hardening Coverage by Category")
    cats = ["FIM", "Service Account Token", "Trusted Certs", "Network Access",
            "Capabilities", "/tmp noexec", "Admin Tools", "Logs Delete"]
    vals = [88, 92, 76, 71, 65, 58, 49, 44]
    img = hbar(cats, vals,
               ["#2A9D8F" if v >= 75 else "#F4A261" if v >= 60 else "#E63946" for v in vals],
               figsize=(4.0, 2.0), value_fmt="{}%", max_label=24)
    draw_image_in_card(c, img, MARGIN_X + 10, row1_y + 8, card_w - 20, row1_h - 30)

    card(c, card_x2, row1_y, card_w, row1_h, "Active Policies by Type")
    cats = ["KubeArmorPolicy", "KubeArmorHostPolicy", "NetworkPolicy",
            "AdmissionPolicy", "Cluster Policies"]
    vals = [1042, 318, 245, 164, 100]
    img = hbar(cats, vals, ["#2A2DEE", "#62A8FF", "#B6CFFF", "#F4A261", "#E6C229"],
               figsize=(4.0, 2.0), max_label=24)
    draw_image_in_card(c, img, card_x2 + 10, row1_y + 8, card_w - 20, row1_h - 30)

    cap_y = row1_y - 8
    cap_y2 = wrapped_caption(
        c,
        "Hardening coverage by category, measured as percentage of in-scope "
        "workloads with at least one enforcing policy. Green is healthy, amber "
        "needs review, red is a coverage gap.",
        MARGIN_X, cap_y, card_w,
    )
    wrapped_caption(
        c,
        "Active enforcing policies grouped by Kubernetes CRD. KubeArmorPolicy "
        "and KubeArmorHostPolicy together cover both pod and node-level enforcement.",
        card_x2, cap_y, card_w,
    )

    # Row 2: Workloads w/o policies + recommended policies
    row2_h = 180
    row2_y = cap_y2 - 18 - row2_h
    card(c, MARGIN_X, row2_y, card_w, row2_h, "Workloads Without Any Policy")
    cats = ["dev-analytics", "stage-security", "shared-tooling",
            "prod-datawarehouse", "frontend-v2"]
    vals = [412, 287, 198, 142, 89]
    img = hbar(cats, vals, ["#E63946"]*5, figsize=(4.0, 1.8), max_label=24)
    draw_image_in_card(c, img, MARGIN_X + 10, row2_y + 8, card_w - 20, row2_h - 30)

    card(c, card_x2, row2_y, card_w, row2_h, "Top Policies Recommended (Discovered)")
    cats = ["restrict-sa-token-access", "block-package-mgr-exec",
            "deny-tmp-exec", "restrict-cert-write", "block-curl-wget"]
    vals = [128, 96, 74, 62, 52]
    img = hbar(cats, vals, ["#2A2DEE"]*5, figsize=(4.0, 1.8), max_label=24)
    draw_image_in_card(c, img, card_x2 + 10, row2_y + 8, card_w - 20, row2_h - 30)

    draw_page_footer(c, page_num)


def page_kspm(c, page_num):
    draw_top_accent(c)
    draw_section_header(c, "Cluster Security Posture (KSPM)",
                        f"{REPORT_PERIOD_START}\nto {REPORT_PERIOD_END}")

    # KPI strip
    top_y = PAGE_H - 135
    strip_h = 60
    strip_w = (PAGE_W - 2 * MARGIN_X - 3 * 8) / 4
    kpis = [
        ("Cluster Findings", "1,771", "Across 9 clusters", BRAND_BLUE),
        ("Critical", "12", "Immediate action required", BRAND_CRIT),
        ("High", "12", "Patch within SLA", BRAND_HIGH),
        ("Medium / Low", "1,747", "Schedule remediation", BRAND_MED),
    ]
    for i, (lbl, val, sub, col) in enumerate(kpis):
        kpi_card(c, MARGIN_X + i * (strip_w + 8), top_y, strip_w, strip_h, lbl, val, sub, col)

    # Row 1
    row1_h = 200
    row1_y = top_y - 20 - row1_h
    card_w = (PAGE_W - 2 * MARGIN_X - 10) / 2
    card_x2 = MARGIN_X + card_w + 10

    card(c, MARGIN_X, row1_y, card_w, row1_h, "Findings by Asset Type")
    cats = ["ConfigMap", "Cron Job", "Deployment", "Namespace", "Pod"]
    crit = [100, 350, 3, 2, 1]
    high = [75, 50, 2, 0, 0]
    med = [15, 25, 5, 0, 0]
    low = [10, 25, 5, 0, 0]
    img = stacked_vbar(cats, [crit, high, med, low],
                       ["#7A0E11", "#E63946", "#F4A261", "#E6C229"],
                       ["Critical", "High", "Medium", "Low"], figsize=(4.0, 2.2),
                       rotate_x=15)
    draw_image_in_card(c, img, MARGIN_X + 10, row1_y + 8, card_w - 20, row1_h - 30)

    card(c, card_x2, row1_y, card_w, row1_h, "KIEM Risk Assessment")
    cats = ["Critical", "High", "Medium", "Low"]
    vals = [12, 12, 1091, 656]
    img = hbar(cats, vals, ["#7A0E11", "#E63946", "#F4A261", "#E6C229"], figsize=(4.0, 2.0))
    draw_image_in_card(c, img, card_x2 + 10, row1_y + 8, card_w - 20, row1_h - 30)

    cap_y = row1_y - 8
    cap_y2 = wrapped_caption(
        c,
        "Findings broken down by Kubernetes asset type. Use to focus remediation on "
        "the asset class generating the largest critical-severity volume.",
        MARGIN_X, cap_y, card_w,
    )
    wrapped_caption(
        c,
        "Kubernetes Identity and Entitlement Management (KIEM) risk distribution. "
        "Highlights over-privileged RoleBindings and ServiceAccount risks.",
        card_x2, cap_y, card_w,
    )

    # Row 2: Pod Security Admission violations + Clusters scoring
    row2_h = 180
    row2_y = cap_y2 - 18 - row2_h
    card(c, MARGIN_X, row2_y, card_w, row2_h, "Pod Security Admission Violations")
    cats = ["privileged", "allowPrivilegeEscalation", "hostNetwork",
            "hostPID", "runAsRoot"]
    vals = [142, 98, 87, 64, 158]
    img = hbar(cats, vals, ["#7A0E11", "#E63946", "#F4A261", "#E6C229", "#E63946"],
               figsize=(4.0, 1.8), max_label=24)
    draw_image_in_card(c, img, MARGIN_X + 10, row2_y + 8, card_w - 20, row2_h - 30)

    card(c, card_x2, row2_y, card_w, row2_h, "Top Risky Clusters (by score)")
    cats = ["prod-api-cluster", "staging-core-services", "frontend-v2",
            "analytics-datahub", "devops-tool"]
    vals = [87, 76, 58, 42, 31]
    img = hbar(cats, vals,
               ["#7A0E11", "#E63946", "#F4A261", "#E6C229", "#2A9D8F"],
               figsize=(4.0, 1.8), value_fmt="{}", max_label=24)
    draw_image_in_card(c, img, card_x2 + 10, row2_y + 8, card_w - 20, row2_h - 30)

    draw_page_footer(c, page_num)


def page_compliance(c, page_num):
    draw_top_accent(c)
    draw_section_header(c, "Compliance Posture (K8s & Workload Benchmarks)",
                        f"{REPORT_PERIOD_START}\nto {REPORT_PERIOD_END}")

    # Big donut: K8s CIS Compliance Status
    top_y = PAGE_H - 400
    big_h = 280
    big_w = (PAGE_W - 2 * MARGIN_X - 10) / 2
    donut_with_legend(
        c, MARGIN_X, top_y, big_w, big_h, "K8s CIS Compliance Status",
        values=[900, 300, 200],
        labels=["Passed", "Failed", "Warning"],
        colors=["#2A9D8F", "#E63946", "#F4A261"],
        center_label="1.50k", center_sub="Checks",
    )

    # Continuous Compliance table
    card_x2 = MARGIN_X + big_w + 10
    card(c, card_x2, top_y, big_w, big_h, "Continuous Compliance Frameworks")
    # Table
    rows = [
        ("MITRE",         "76 / 6384",  "1.19%", 200, 100,  0, 15, 10),
        ("PCI-DSS",       "41 / 499",   "8.22%", 450,   0, 50, 25, 25),
        ("NIST 800-190",  "110 / 125",  "88.0%",  10,   3,  2,  0,  5),
        ("CIS Kubernetes","50 / 721",   "6.93%",   2,   2,  0,  0,  0),
        ("FedRAMP",       "221 / 221",  "100%",    0,   0,  0,  0,  0),
        ("HIPAA",         "94 / 184",   "51.1%",  18,   8,  2,  4,  4),
    ]
    tx = card_x2 + 12
    ty = top_y + big_h - 36
    c.setFillColor(TEXT_MUTED)
    c.setFont("Helvetica-Bold", 7)
    headers = ["Framework", "Coverage", "Score", "Alerts", "C", "H", "M", "L"]
    col_widths = [72, 50, 32, 32, 22, 22, 22, 22]
    cx = tx
    for h, w in zip(headers, col_widths):
        if h in ("C", "H", "M", "L"):
            c.drawCentredString(cx + w / 2, ty, h)
        else:
            c.drawString(cx, ty, h)
        cx += w
    ty -= 12
    c.setStrokeColor(CARD_BORDER)
    c.line(tx, ty + 4, tx + sum(col_widths), ty + 4)
    c.setFillColor(TEXT_DARK)
    c.setFont("Helvetica", 8)
    for fw, cov, score, alerts, cc, hh, mm, ll in rows:
        cx = tx
        c.setFillColor(TEXT_DARK)
        c.setFont("Helvetica", 8)
        c.drawString(cx, ty, fw); cx += col_widths[0]
        c.drawString(cx, ty, cov); cx += col_widths[1]
        c.drawString(cx, ty, score); cx += col_widths[2]
        c.drawString(cx, ty, f"{alerts}"); cx += col_widths[3]
        for v, col in [(cc, "#7A0E11"), (hh, "#E63946"), (mm, "#F4A261"), (ll, "#E6C229")]:
            cw_local = col_widths[4]
            bx = cx + cw_local / 2
            by = ty + 3
            r = 8.5 if v >= 100 else 7
            c.setFillColor(HexColor(col) if v > 0 else HexColor("#E5E7EB"))
            c.circle(bx, by, r, stroke=0, fill=1)
            c.setFillColor(white if v > 0 else TEXT_MUTED)
            c.setFont("Helvetica-Bold", 7 if v >= 100 else 7.5)
            c.drawCentredString(bx, by - 2, str(v))
            cx += cw_local
        ty -= 20

    cap_y = top_y - 8
    wrapped_caption(
        c,
        "Aggregate pass/fail across all CIS-mandated checks for Kubernetes 1.x. Use "
        "the failed slice as your shortest path to certifiable baseline posture.",
        MARGIN_X, cap_y, big_w,
    )
    wrapped_caption(
        c,
        "Coverage and score across the regulatory frameworks AccuKnox continuously "
        "evaluates. Severity badges indicate the highest-priority unmet controls.",
        card_x2, cap_y, big_w,
    )

    draw_page_footer(c, page_num)


def page_container_image(c, page_num):
    draw_top_accent(c)
    draw_section_header(c, "Container Image & Registry Security",
                        f"{REPORT_PERIOD_START}\nto {REPORT_PERIOD_END}")

    top_y = PAGE_H - 135
    strip_h = 60
    strip_w = (PAGE_W - 2 * MARGIN_X - 3 * 8) / 4
    kpis = [
        ("Images Scanned", "3,210", "Across 10 registries", BRAND_BLUE),
        ("Critical CVEs", "1,200", "In container images", BRAND_CRIT),
        ("Fixes Available", "150", "Of 200 vulnerable images", BRAND_OK),
        ("Drift Events", "287", "Image vs runtime mismatch", BRAND_HIGH),
    ]
    for i, (lbl, val, sub, col) in enumerate(kpis):
        kpi_card(c, MARGIN_X + i * (strip_w + 8), top_y, strip_w, strip_h, lbl, val, sub, col)

    # Row 1: top vulnerable images + fixes availability donut
    row1_h = 200
    row1_y = top_y - 20 - row1_h
    card_w = (PAGE_W - 2 * MARGIN_X - 10) / 2
    card_x2 = MARGIN_X + card_w + 10
    card(c, MARGIN_X, row1_y, card_w, row1_h, "Top Vulnerable Images")
    cats = ["frontend-app:latest", "api-gateway:v2.1", "worker:1.4.0",
            "ml-trainer:cuda11", "legacy-monolith:9.x"]
    vals = [1200, 820, 540, 380, 260]
    img = hbar(cats, vals, ["#7A0E11", "#E63946", "#F4A261", "#E6C229", "#2A2DEE"],
               figsize=(4.0, 2.0), max_label=22)
    draw_image_in_card(c, img, MARGIN_X + 10, row1_y + 8, card_w - 20, row1_h - 30)

    donut_with_legend(
        c, card_x2, row1_y, card_w, row1_h, "Fixes Availability",
        values=[150, 50],
        labels=["Available", "Unavailable"],
        colors=["#2A9D8F", "#E63946"],
        center_label="200", center_sub="Images",
    )

    cap_y = row1_y - 8
    cap_y2 = wrapped_caption(
        c,
        "Container images ranked by total vulnerabilities. Patch or rebase on a "
        "trusted minimal base image to drive these counts down quickly.",
        MARGIN_X, cap_y, card_w,
    )
    wrapped_caption(
        c,
        "Vulnerable images with at least one upstream-available fix versus those "
        "requiring code, base-image, or library substitution to remediate.",
        card_x2, cap_y, card_w,
    )

    # Row 2: top CVEs in images + drift detection
    row2_h = 180
    row2_y = cap_y2 - 18 - row2_h
    card(c, MARGIN_X, row2_y, card_w, row2_h, "Top CVEs in Container Images")
    cats = ["CVE-2023-45853", "CVE-2023-31484", "CVE-2023-2953",
            "CVE-2023-56171", "CVE-2023-6345"]
    vals = [8, 5540, 2788, 23, 159]
    img = hbar(cats, vals, ["#7A0E11", "#7A0E11", "#E63946", "#F4A261", "#E6C229"],
               figsize=(4.0, 1.8), max_label=24)
    draw_image_in_card(c, img, MARGIN_X + 10, row2_y + 8, card_w - 20, row2_h - 30)

    card(c, card_x2, row2_y, card_w, row2_h, "Image vs Runtime Drift Events")
    x = ["Wk1", "Wk2", "Wk3", "Wk4"]
    drift_blocked = [62, 71, 58, 96]
    drift_audit = [22, 31, 28, 41]
    img = line_trend(x, [drift_blocked, drift_audit],
                     ["Blocked Drift", "Audit Drift"],
                     ["#E63946", "#F4A261"], figsize=(4.0, 1.8))
    draw_image_in_card(c, img, card_x2 + 10, row2_y + 8, card_w - 20, row2_h - 30)

    draw_page_footer(c, page_num)


def page_vm_protect(c, page_num):
    draw_top_accent(c)
    draw_section_header(c, "VM Workload Protection",
                        f"{REPORT_PERIOD_START}\nto {REPORT_PERIOD_END}")

    top_y = PAGE_H - 135
    strip_h = 60
    strip_w = (PAGE_W - 2 * MARGIN_X - 3 * 8) / 4
    kpis = [
        ("VM Exposure Risk", "78%", "Secure ↓ 12% vs prior", BRAND_OK),
        ("Exploitable VMs", "171", "↑ 12% vs prior", BRAND_HIGH),
        ("Exploitable CVEs", "128", "↑ 12% vs prior", BRAND_CRIT),
        ("Over-Privileged VMs", "201", "↑ 12% vs prior", BRAND_MED),
    ]
    for i, (lbl, val, sub, col) in enumerate(kpis):
        kpi_card(c, MARGIN_X + i * (strip_w + 8), top_y, strip_w, strip_h, lbl, val, sub, col)

    # Row 1
    row1_h = 200
    row1_y = top_y - 20 - row1_h
    card_w = (PAGE_W - 2 * MARGIN_X - 10) / 2
    card_x2 = MARGIN_X + card_w + 10

    card(c, MARGIN_X, row1_y, card_w, row1_h, "Top 10 VMs with Findings")
    cats = ["prod-applications", "dev-analytics", "stage-security",
            "prod-networking", "prod-datawarehouse"]
    vals = [1100, 67, 45, 8, 2]
    img = hbar(cats, vals, ["#7A0E11", "#E63946", "#F4A261", "#E6C229", "#2A2DEE"],
               figsize=(4.0, 1.9), max_label=24)
    draw_image_in_card(c, img, MARGIN_X + 10, row1_y + 8, card_w - 20, row1_h - 30)

    card(c, card_x2, row1_y, card_w, row1_h, "Exploitable Package Vulnerabilities")
    cats = ["openssl 1.1.1w", "libcurl 7.87.0", "log4j-core 2.14.1",
            "express 4.18.2", "lodash 4.17.21"]
    vals = [46, 23, 16, 9, 4]
    img = hbar(cats, vals, ["#2A9D8F"]*5, figsize=(4.0, 1.9),
               value_fmt="{} VMs", max_label=24)
    draw_image_in_card(c, img, card_x2 + 10, row1_y + 8, card_w - 20, row1_h - 30)

    cap_y = row1_y - 8
    cap_y2 = wrapped_caption(
        c,
        "Virtual machines ranked by total finding count. Cross-reference with the "
        "exploitable-CVE list to prioritize patch windows.",
        MARGIN_X, cap_y, card_w,
    )
    wrapped_caption(
        c,
        "OS-level package vulnerabilities with confirmed exploit code observed in "
        "the fleet. Patch order should follow VM exposure count.",
        card_x2, cap_y, card_w,
    )

    # Row 2: VM Scan Summary KPIs + Top 10 OWASP
    row2_h = 200
    row2_y = cap_y2 - 18 - row2_h
    card(c, MARGIN_X, row2_y, card_w, row2_h, "VM Scan Summary")
    # 2x3 KPI grid (2 columns of taller cells gives more label space)
    grid_kpis = [
        ("End of Life VMs",    "300", "no fix available"),
        ("Autopatching On",    "102", "auto-remediated"),
        ("IAM Users",          "65",  "fleet-wide"),
        ("Config Flaws",       "20",  "open issues"),
        ("Open Ports",         "1",   "exposed"),
        ("Exposed Credentials","90",  "found in scans"),
    ]
    cols, rows_n = 2, 3
    cw = (card_w - 24 - (cols - 1) * 8) / cols
    ch = (row2_h - 36) / rows_n
    for idx, (lbl, val, sub) in enumerate(grid_kpis):
        ci = idx % cols
        ri = idx // cols
        gx = MARGIN_X + 12 + ci * (cw + 8)
        gy = row2_y + 8 + (rows_n - 1 - ri) * ch
        c.setStrokeColor(CARD_BORDER)
        c.setFillColor(LIGHT_BG)
        c.roundRect(gx, gy, cw, ch - 4, 5, stroke=1, fill=1)
        c.setFillColor(TEXT_MUTED)
        c.setFont("Helvetica", 8)
        c.drawString(gx + 10, gy + ch - 16, lbl)
        c.setFillColor(TEXT_DARK)
        c.setFont("Helvetica-Bold", 18)
        c.drawString(gx + 10, gy + 14, val)
        c.setFillColor(TEXT_MUTED)
        c.setFont("Helvetica", 7)
        c.drawRightString(gx + cw - 10, gy + 8, sub)

    card(c, card_x2, row2_y, card_w, row2_h, "Top 10 OWASP")
    cats = ["A06-Vulnerable Components", "A05-Security Misconfig",
            "A09-Monitoring Failures", "A01-Broken Access Control",
            "A07-Auth Failure"]
    vals = [46, 23, 16, 9, 4]
    img = hbar(cats, vals, ["#2A9D8F"]*5, figsize=(4.0, 1.9),
               value_fmt="{} VMs", max_label=28)
    draw_image_in_card(c, img, card_x2 + 10, row2_y + 8, card_w - 20, row2_h - 30)

    draw_page_footer(c, page_num)


def page_vuln(c, page_num):
    draw_top_accent(c)
    draw_section_header(c, "Vulnerability & CVE Management",
                        f"{REPORT_PERIOD_START}\nto {REPORT_PERIOD_END}")

    # Row 1: CVE by SLA + Top 5 CVEs table
    row1_y = PAGE_H - 330
    row1_h = 215
    card_w = (PAGE_W - 2 * MARGIN_X - 10) / 2
    card_x2 = MARGIN_X + card_w + 10

    card(c, MARGIN_X, row1_y, card_w, row1_h, "Vulnerability CVEs by SLA")
    cats = ["Up to 30 days", "31-60 days", "> 61 days"]
    crit = [20, 60, 50]
    high = [30, 50, 70]
    med = [30, 60, 50]
    low = [20, 30, 32]
    img = stacked_vbar(cats, [crit, high, med, low],
                       ["#7A0E11", "#E63946", "#F4A261", "#E6C229"],
                       ["Critical", "High", "Medium", "Low"], figsize=(4.0, 2.0))
    draw_image_in_card(c, img, MARGIN_X + 10, row1_y + 8, card_w - 20, row1_h - 30)

    card(c, card_x2, row1_y, card_w, row1_h, "Top 5 CVEs")
    # Table
    tx = card_x2 + 12
    ty = row1_y + row1_h - 36
    c.setFillColor(TEXT_MUTED)
    c.setFont("Helvetica", 7.5)
    headers = ["CVE ID", "Title", "Sev", "Count"]
    col_widths = [80, 105, 30, 38]
    cx = tx
    for h, w in zip(headers, col_widths):
        c.drawString(cx, ty, h)
        cx += w
    ty -= 12
    c.setStrokeColor(CARD_BORDER)
    c.line(tx, ty + 4, tx + sum(col_widths), ty + 4)
    rows = [
        ("CVE-2023-45853", "XZ Utils backdoor (RCE sudo/ssh)", "C", "8"),
        ("CVE-2023-31484", "GNU C Library Looney Tunables", "C", "5,540"),
        ("CVE-2023-2953",  "Sudo Buffer Overflow (Baron)",   "H", "2,788"),
        ("CVE-2023-56171", "Dirty Pipe Linux Kernel PE",     "M", "23"),
        ("CVE-2023-6345",  "XZ Utils backdoor (RCE)",        "L", "159"),
    ]
    sev_color = {"C": "#7A0E11", "H": "#E63946", "M": "#F4A261", "L": "#E6C229"}
    c.setFillColor(TEXT_DARK)
    c.setFont("Helvetica", 8)
    for cve, title, sev, count in rows:
        cx = tx
        c.drawString(cx, ty, cve); cx += col_widths[0]
        c.drawString(cx, ty, title[:24]); cx += col_widths[1]
        c.setFillColor(HexColor(sev_color[sev]))
        c.circle(cx + 6, ty + 3, 5, stroke=0, fill=1)
        c.setFillColor(white)
        c.setFont("Helvetica-Bold", 6.5)
        c.drawCentredString(cx + 6, ty + 1.5, sev)
        c.setFillColor(TEXT_DARK)
        c.setFont("Helvetica", 8)
        cx += col_widths[2]
        c.drawString(cx, ty, count)
        ty -= 17

    cap_y = row1_y - 8
    cap_y2 = wrapped_caption(
        c,
        "Open CVEs grouped by SLA bucket. Tickets in the >61 days bucket are "
        "SLA breaches and should drive emergency change windows.",
        MARGIN_X, cap_y, card_w,
    )
    wrapped_caption(
        c,
        "Highest-impact CVEs across the protected fleet, with severity and total "
        "affected workload count for prioritization.",
        card_x2, cap_y, card_w,
    )

    # Row 2: Active vs Resolved + MTTR
    row2_h = 175
    row2_y = cap_y2 - 18 - row2_h
    card(c, MARGIN_X, row2_y, card_w, row2_h, "Active vs Resolved Findings")
    x = ["Mar 12", "Mar 19", "Mar 26", "Apr 03", "Apr 10"]
    active = [85, 130, 250, 280, 290]
    resolved = [80, 120, 110, 200, 230]
    img = line_trend(x, [active, resolved], ["Active", "Resolved"],
                     ["#E63946", "#2A9D8F"], figsize=(4.0, 1.8))
    draw_image_in_card(c, img, MARGIN_X + 10, row2_y + 8, card_w - 20, row2_h - 30)

    card(c, card_x2, row2_y, card_w, row2_h, "MTTR Over Time (Hours)")
    x = ["Jan", "Feb", "Mar", "Apr"]
    mttr = [68, 62, 58, 55]
    img = line_trend(x, [mttr], ["MTTR (h)"], ["#E63946"], figsize=(4.0, 1.8))
    draw_image_in_card(c, img, card_x2 + 10, row2_y + 8, card_w - 20, row2_h - 30)

    draw_page_footer(c, page_num)


def page_mitre(c, page_num):
    draw_top_accent(c)
    draw_section_header(c, "MITRE ATT&CK Coverage (Containers Matrix)",
                        f"{REPORT_PERIOD_START}\nto {REPORT_PERIOD_END}")

    # Big card: tactic heatmap
    top_y = PAGE_H - 330
    big_h = 215
    big_w = PAGE_W - 2 * MARGIN_X
    card(c, MARGIN_X, top_y, big_w, big_h,
         "Detections by MITRE ATT&CK Tactic")
    tactics = ["Initial Access", "Execution", "Persistence", "Priv Esc",
               "Defense Evasion", "Credential Access", "Discovery",
               "Lateral Movement", "Impact"]
    techniques = [2, 4, 3, 3, 5, 2, 4, 2, 3]
    intensity  = [42, 318, 96, 211, 287, 64, 198, 41, 27]
    img = heatmap_mitre(tactics, techniques, intensity, figsize=(7.5, 2.0))
    draw_image_in_card(c, img, MARGIN_X + 10, top_y + 8, big_w - 20, big_h - 30)

    cap_y = top_y - 8
    cap_y2 = wrapped_caption(
        c,
        "Heatmap of detection volume across MITRE ATT&CK tactics for the period. "
        "Numbers in cells are total events; '(N)' indicates distinct techniques "
        "observed under that tactic. Darker shades mark higher attack pressure.",
        MARGIN_X, cap_y, big_w,
    )

    # Row 2: Top techniques observed + Inline blocked vs audit
    row2_h = 195
    row2_y = cap_y2 - 14 - row2_h
    card_w = (PAGE_W - 2 * MARGIN_X - 10) / 2
    card_x2 = MARGIN_X + card_w + 10

    card(c, MARGIN_X, row2_y, card_w, row2_h, "Top Techniques Observed")
    cats = ["T1059 Command/Script", "T1611 Container Escape",
            "T1078 Valid Accounts", "T1486 Data Encrypt Impact",
            "T1003 Credential Dump"]
    vals = [318, 211, 142, 27, 64]
    img = hbar(cats, vals, ["#7A0E11", "#E63946", "#F4A261", "#E6C229", "#62A8FF"],
               figsize=(4.0, 1.9), max_label=24)
    draw_image_in_card(c, img, MARGIN_X + 10, row2_y + 8, card_w - 20, row2_h - 30)

    card(c, card_x2, row2_y, card_w, row2_h, "Inline Blocked vs Audit-Only")
    cats = ["Initial Access", "Execution", "Priv Esc", "Defense Evasion",
            "Cred Access"]
    blocked = [38, 220, 165, 198, 41]
    audit = [4, 98, 46, 89, 23]
    fig, ax = plt.subplots(figsize=(4.0, 1.9))
    y = np.arange(len(cats))
    ax.barh(y - 0.18, blocked, height=0.34, color="#7A0E11", label="Blocked")
    ax.barh(y + 0.18, audit, height=0.34, color="#F4A261", label="Audit Only")
    ax.set_yticks(y); ax.set_yticklabels(cats, fontsize=7.5)
    ax.invert_yaxis()
    ax.tick_params(axis="x", labelsize=7, colors="#5A6072")
    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)
    ax.legend(loc="lower right", fontsize=7, frameon=False)
    img = _fig_to_image(fig)
    draw_image_in_card(c, img, card_x2 + 10, row2_y + 8, card_w - 20, row2_h - 30)

    draw_page_footer(c, page_num)


def page_tickets(c, page_num):
    draw_top_accent(c)
    draw_section_header(c, "Incident & Ticket Management",
                        f"{REPORT_PERIOD_START}\nto {REPORT_PERIOD_END}")

    # Two donuts: Ticket Status + Ticket by Severity
    row1_h = 215
    row1_y = PAGE_H - 120 - row1_h
    card_w = (PAGE_W - 2 * MARGIN_X - 10) / 2
    card_x2 = MARGIN_X + card_w + 10

    donut_with_legend(
        c, MARGIN_X, row1_y, card_w, row1_h, "Ticket Status",
        values=[190, 54, 25, 25, 6],
        labels=["Created", "To-Do", "In Progress", "Closed", "Cancelled"],
        colors=["#2A2DEE", "#62A8FF", "#B6CFFF", "#E5E7EB", "#F4A261"],
        center_label="300", center_sub="Tickets",
    )
    donut_with_legend(
        c, card_x2, row1_y, card_w, row1_h, "Ticket by Severity",
        values=[90, 40, 25, 30],
        labels=["Critical", "High", "Medium", "Low"],
        colors=["#7A0E11", "#E63946", "#F4A261", "#E6C229"],
        center_label="185", center_sub="Tickets",
    )

    cap_y = row1_y - 8
    cap_y2 = wrapped_caption(
        c,
        "Snapshot of ticket workflow across created, to-do, in-progress, closed, "
        "and cancelled states for CWPP findings.",
        MARGIN_X, cap_y, card_w,
    )
    wrapped_caption(
        c,
        "Severity distribution of all open CWPP tickets. Critical tickets should be "
        "tracked against the 24-hour SLA.",
        card_x2, cap_y, card_w,
    )

    # Row 2: SLA Status + Open vs Closed trend
    row2_h = 175
    row2_y = cap_y2 - 18 - row2_h
    card(c, MARGIN_X, row2_y, card_w, row2_h, "SLA Status of Tickets")
    cats = ["Met", "Within SLA", "Approaching", "Breached"]
    vals = [165, 78, 32, 25]
    img = hbar(cats, vals, ["#2A9D8F", "#62A8FF", "#F4A261", "#E63946"],
               figsize=(4.0, 1.8))
    draw_image_in_card(c, img, MARGIN_X + 10, row2_y + 8, card_w - 20, row2_h - 30)

    card(c, card_x2, row2_y, card_w, row2_h, "Open vs Closed Tickets")
    x = ["Mar 12", "Mar 19", "Mar 26", "Apr 03", "Apr 10"]
    op = [85, 130, 250, 280, 290]
    cl = [80, 120, 110, 200, 230]
    img = line_trend(x, [op, cl], ["Open", "Closed"],
                     ["#E63946", "#2A9D8F"], figsize=(4.0, 1.8))
    draw_image_in_card(c, img, card_x2 + 10, row2_y + 8, card_w - 20, row2_h - 30)

    draw_page_footer(c, page_num)


def page_recommendations(c, page_num):
    draw_top_accent(c)
    draw_section_header(c, "Recommendations & Action Items",
                        f"{REPORT_PERIOD_START}\nto {REPORT_PERIOD_END}")

    # Intro paragraph
    intro = (
        "The following prioritized actions are derived from the data above. Each "
        "item names the AccuKnox module that surfaces the issue, the suggested "
        "remediation, and the expected drop in measured risk after the change."
    )
    y_after = wrapped_caption(c, intro, MARGIN_X, PAGE_H - 110,
                              PAGE_W - 2 * MARGIN_X,
                              font="Helvetica", size=10, leading=14,
                              color=TEXT_DARK)

    # Recommendation cards (numbered)
    recs = [
        ("01", "Promote audit policies to block in production-apps",
         "Runtime",
         "4,992 audit-then-block events show baseline behavior is now well-known "
         "for production-apps and prod-api-cluster. Promote to inline mitigation "
         "to convert detection into prevention.",
         "Expected: 38% drop in critical alert volume."),
        ("02", "Close hardening gap on 1,548 unprotected workloads",
         "Hardening",
         "1,548 workloads have no KubeArmorPolicy attached. Apply the discovered "
         "policy set (restrict-sa-token-access, block-package-mgr-exec, "
         "deny-tmp-exec, restrict-cert-write) starting with dev-analytics (412 "
         "uncovered workloads).",
         "Expected: agent coverage 86% → 99%."),
        ("03", "Patch openssl 1.1.1w across 46 VMs",
         "VM Protection",
         "Openssl 1.1.1w is the single most exploitable package in the fleet, "
         "present on 46 VMs. Schedule autopatching for the affected hosts or "
         "rebase impacted golden images.",
         "Expected: exploitable VM count 171 → 125."),
        ("04", "Replace 300 EOL VMs identified by VM Scan Summary",
         "VM Protection",
         "300 virtual machines run operating systems past EOL and cannot receive "
         "vendor patches. Migrate workloads to a supported baseline image.",
         "Expected: EOL exposure removed; high-severity finding count -240."),
        ("05", "Address MITRE T1059 (Command/Script Interpreter)",
         "MITRE",
         "T1059 is the highest-volume technique observed (318 events). Tighten "
         "block-shell-binaries-exec to include all production namespaces and "
         "extend to interactive shells inside containers.",
         "Expected: T1059 detections cut by ~60%."),
        ("06", "Drive CIS Kubernetes compliance from 6.93% to >50%",
         "Compliance",
         "Only 50 of 721 CIS checks pass. Begin with the failed-control list and "
         "address the top 5 control families (API server, controller manager, "
         "etcd, kubelet, RBAC) for the largest score gain.",
         "Expected: CIS score 6.93% → 52%; FedRAMP retained at 100%."),
    ]

    rec_y = y_after - 20
    rec_h = 80
    for i, (n, title, mod, body, impact) in enumerate(recs):
        if rec_y - rec_h < 50:
            break
        card(c, MARGIN_X, rec_y - rec_h, PAGE_W - 2 * MARGIN_X, rec_h)
        # Number circle
        c.setFillColor(BRAND_BLUE)
        c.circle(MARGIN_X + 28, rec_y - rec_h / 2, 16, stroke=0, fill=1)
        c.setFillColor(white)
        c.setFont("Helvetica-Bold", 11)
        c.drawCentredString(MARGIN_X + 28, rec_y - rec_h / 2 - 3.5, n)
        # Title
        c.setFillColor(TEXT_DARK)
        c.setFont("Helvetica-Bold", 10.5)
        c.drawString(MARGIN_X + 56, rec_y - 18, title)
        # Module pill
        c.setFillColor(HexColor("#EEF1FF"))
        pill_w = c.stringWidth(mod, "Helvetica-Bold", 7.5) + 14
        c.roundRect(MARGIN_X + 56, rec_y - 36, pill_w, 12, 3, stroke=0, fill=1)
        c.setFillColor(BRAND_BLUE)
        c.setFont("Helvetica-Bold", 7.5)
        c.drawString(MARGIN_X + 56 + 7, rec_y - 33, mod)
        # Body
        c.setFillColor(TEXT_DARK)
        wrapped_caption(c, body, MARGIN_X + 56,
                        rec_y - 48, PAGE_W - 2 * MARGIN_X - 70,
                        font="Helvetica", size=8.5, leading=10.5,
                        color=TEXT_DARK)
        # Impact
        c.setFillColor(BRAND_OK)
        c.setFont("Helvetica-Oblique", 8)
        c.drawString(MARGIN_X + 56, rec_y - rec_h + 8, impact)
        rec_y -= rec_h + 8

    draw_page_footer(c, page_num)


# -----------------------------------------------------------------------------
# Driver
# -----------------------------------------------------------------------------
def build():
    out = os.path.abspath(OUT_PDF)
    c = canvas.Canvas(out, pagesize=A4)
    c.setTitle("Cloud Workload Protection Management Report (CWPP)")
    c.setAuthor("AccuKnox")

    # Cover (no page number)
    draw_cover(c)
    c.showPage()

    builders = [
        page_inventory_1,
        page_inventory_2,
        page_runtime_alerts,
        page_runtime_drilldown,
        page_app_behavior,
        page_hardening,
        page_kspm,
        page_compliance,
        page_container_image,
        page_vm_protect,
        page_vuln,
        page_mitre,
        page_tickets,
        page_recommendations,
    ]
    for i, fn in enumerate(builders, start=1):
        fn(c, i)
        c.showPage()

    c.save()
    print("Wrote:", out)
    return out


if __name__ == "__main__":
    build()

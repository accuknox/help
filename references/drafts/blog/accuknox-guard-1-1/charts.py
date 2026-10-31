"""Static charts for the two AccuKnox Guard 1.1 posts.

Every number comes from the HiveTrace GuardRate exports in data/, snapshot 2026-10-16.
Run: python charts.py
"""
import json
from collections import defaultdict
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager

HERE = Path(__file__).parent
DATA = HERE / "data"
OUT = HERE / "assets"
FONTS = Path(r"D:\AccuKnox\help\.claude\skills\accuknox-gated-content\assets\fonts")
for f in FONTS.glob("Inter-*.ttf"):
    font_manager.fontManager.addfont(str(f))
plt.rcParams.update({"font.family": "Inter", "font.size": 11, "axes.edgecolor": "#C9CCD6",
                     "axes.labelcolor": "#0D1B4B", "xtick.color": "#595959", "ytick.color": "#595959"})

NAVY, ACCENT, RED, GREY, INK = "#11206D", "#003BF6", "#C80019", "#B8BDCB", "#0D1B4B"
AK = "Accuknoxtechnologies/accuknox-guard-1.1"
SRC = "Source: HiveTrace GuardRate Leaderboard, all 19 groups, snapshot 2026-10-16"

ranking = json.load(open(DATA / "ranking.json"))["rows"]
tools = json.load(open(DATA / "tools.json"))
by = defaultdict(dict)
for row in tools["rows"]:
    by[row["model"]][row["group"]] = row
GROUPS = tools["groups"]


def short(m):
    return "AccuKnox Guard 1.1" if m == AK else m.split("/")[1]


def finish(fig, ax, title, sub, name):
    fig.text(0.06, 0.965, title, fontsize=17, fontweight="bold", color=INK, va="top")
    fig.text(0.06, 0.915, sub, fontsize=11, color="#595959", va="top")
    fig.text(0.06, 0.02, SRC, fontsize=8.5, color="#8A8F9E")
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    fig.savefig(OUT / name, dpi=200, facecolor="white")
    plt.close(fig)
    print("wrote", name)


# 1. Overall score against the weakest group, all 41 models
def floor_vs_score():
    fig, ax = plt.subplots(figsize=(10, 6.2))
    fig.subplots_adjust(left=0.08, right=0.97, top=0.82, bottom=0.12)
    rows = [r for r in ranking if r["integral"] > 0.3]
    for r in rows:
        is_ak = r["model"] == AK
        ax.scatter(r["min_group"], r["integral"], s=170 if is_ak else 55,
                   color=ACCENT if is_ak else GREY, edgecolor="white", linewidth=1, zorder=3 if is_ak else 2)
    labels = {AK: (-14, 8), "Alibaba-AAIG/YuFeng-XGuard-Reason-8B": (10, 4), "Qwen/Qwen3Guard-Gen-8B": (10, -10),
              "openguardrails/OpenGuardrails-Text-2510": (10, -12), "astroware/HaloGuard1-Gen-4B": (-12, -14),
              "meta-llama/Llama-Guard-4-12B": (10, -3), "google/shieldgemma-9b": (10, -3),
              "inclusionAI/Sing-Guard-2b": (-12, -14)}
    for r in rows:
        if r["model"] in labels:
            dx, dy = labels[r["model"]]
            ax.annotate(f"#{r['rank']} {short(r['model'])}", (r["min_group"], r["integral"]),
                        xytext=(dx, dy), textcoords="offset points", fontsize=9.5,
                        color=NAVY if r["model"] == AK else "#3A3F4F",
                        fontweight="bold" if r["model"] == AK else "normal",
                        ha="right" if dx < 0 else "left")
    ax.set_xlabel("Weakest group score (min score, higher is better)")
    ax.set_ylabel("Integral score (higher is better)")
    ax.set_xlim(0, 0.62)
    ax.grid(alpha=0.25)
    finish(fig, ax, "Only one model is both top-ranked and has no weak group",
           f"Each dot is a guard model. Right means its worst benchmark group still holds up. {len(rows)} models with integral above 0.3 shown.",
           "chart-floor-vs-score.png")


# 2. Heatmap, 19 groups by the top 8 models, weakest cell outlined
def heatmap():
    top = [r["model"] for r in ranking[:8]]
    import numpy as np
    m = np.array([[by[t][g]["score"] for t in top] for g in GROUPS])
    fig, ax = plt.subplots(figsize=(11, 9.4))
    fig.subplots_adjust(left=0.2, right=0.98, top=0.84, bottom=0.04)
    from matplotlib.colors import LinearSegmentedColormap
    cmap = LinearSegmentedColormap.from_list("ak", ["#C80019", "#F4E4E6", "#E6EBFF", "#003BF6"])
    ax.imshow(m, cmap=cmap, vmin=0.1, vmax=1.0, aspect="auto")
    ax.set_xticks(range(len(top)))
    def two(t, i):
        nl = chr(10)
        n = short(t)
        for a in ("-Reason", "-Pro", "-1.0-3B", "-Text-2510", "-Gen-4B", "-Gen-8B", "-2b", " 1.1"):
            n = n.replace(a, nl + a.lstrip(" "))
        return f"#{i+1} {n}"
    ax.set_xticklabels([two(t, i) for i, t in enumerate(top)], fontsize=8.5)
    ax.xaxis.tick_top()
    ax.set_yticks(range(len(GROUPS)))
    ax.set_yticklabels(GROUPS, fontsize=9.5)
    for j in range(len(top)):
        i_min = int(m[:, j].argmin())
        for i in range(len(GROUPS)):
            v = m[i, j]
            ax.text(j, i, f"{v:.2f}", ha="center", va="center", fontsize=8.5,
                    color="white" if (v < 0.3 or v > 0.85) else INK,
                    fontweight="bold" if i == i_min else "normal")
        ax.add_patch(plt.Rectangle((j - 0.5, i_min - 0.5), 1, 1, fill=False, edgecolor="black", linewidth=2.2))
    for s in ax.spines.values():
        s.set_visible(False)
    fig.text(0.02, 0.985, "Every top model has one weak group. The size of that weakness decides the ranking.",
             fontsize=15, fontweight="bold", color=INK, va="top")
    fig.text(0.02, 0.955, "Group score per model. The black box marks each model's weakest group, which GuardRate's geometric mean punishes most.",
             fontsize=10, color="#595959", va="top")
    fig.text(0.02, 0.015, SRC, fontsize=8.5, color="#8A8F9E")
    fig.savefig(OUT / "chart-group-heatmap.png", dpi=200, facecolor="white")
    plt.close(fig)
    print("wrote chart-group-heatmap.png")


# 3. False blocks against missed attacks
def fpr_fnr():
    fig, ax = plt.subplots(figsize=(10, 6.2))
    fig.subplots_adjust(left=0.09, right=0.97, top=0.82, bottom=0.12)
    rows = [r for r in ranking if r["integral"] > 0.5]
    for r in rows:
        is_ak = r["model"] == AK
        ax.scatter(r["overall_fpr"] * 100, r["overall_fnr"] * 100, s=170 if is_ak else 55,
                   color=ACCENT if is_ak else GREY, edgecolor="white", zorder=3 if is_ak else 2)
    names = {AK: (10, -4), "Alibaba-AAIG/YuFeng-XGuard-Reason-8B": (8, -10), "Qwen/Qwen3Guard-Gen-8B": (-8, -11),
             "meta-llama/Llama-Guard-4-12B": (8, 0), "meta-llama/Llama-Guard-3-8B": (8, 2),
             "google/shieldgemma-9b": (8, 0), "openguardrails/OpenGuardrails-Text-2510": (8, 4),
             "nvidia/Llama-3.1-Nemotron-Safety-Guard-8B-v3": (8, 3)}
    for r in rows:
        if r["model"] in names:
            dx, dy = names[r["model"]]
            ax.annotate(f"#{r['rank']} {short(r['model'])}", (r["overall_fpr"] * 100, r["overall_fnr"] * 100),
                        xytext=(dx, dy), textcoords="offset points", fontsize=9.5, ha="right" if dx < 0 else "left",
                        color=NAVY if r["model"] == AK else "#3A3F4F", fontweight="bold" if r["model"] == AK else "normal")
    ax.annotate("ideal corner", (1, 1), fontsize=9, color="#8A8F9E")
    ax.set_xlabel("False-positive rate, % of safe prompts blocked (lower is better)")
    ax.set_ylabel("False-negative rate, % of attacks missed (lower is better)")
    ax.set_xlim(0, 42)
    ax.set_ylim(0, 52)
    ax.grid(alpha=0.25)
    finish(fig, ax, "Low false blocks usually cost missed attacks. Guard 1.1 avoids that trade.",
           f"Every model left of Guard 1.1 misses at least 34.7% of attacks. {len(rows)} models with integral above 0.5 shown.",
           "chart-fpr-vs-fnr.png")


# 4. Latency against score
def latency():
    fig, ax = plt.subplots(figsize=(10, 6.2))
    fig.subplots_adjust(left=0.09, right=0.97, top=0.82, bottom=0.12)
    rows = [r for r in ranking if r["integral"] > 0.6]
    for r in rows:
        is_ak = r["model"] == AK
        size = float(r["size"].rstrip("B"))
        ax.scatter(r["p95_ms"], r["integral"], s=40 + size * 28, color=ACCENT if is_ak else GREY,
                   alpha=0.95 if is_ak else 0.7, edgecolor="white", zorder=3 if is_ak else 2)
    names = {AK: (12, 2), "Alibaba-AAIG/YuFeng-XGuard-Reason-8B": (10, 0), "Qwen/Qwen3Guard-Gen-8B": (12, 0),
             "openguardrails/OpenGuardrails-Text-2510": (12, 0), "nvidia/Llama-3.1-Nemotron-Safety-Guard-8B-v3": (-12, -16),
             "hivetrace/HiveTraceGuard-Pro": (10, -2), "meta-llama/Llama-Guard-4-12B": (12, 0),
             "astroware/HaloGuard1-Gen-4B": (-12, 8)}
    for r in rows:
        if r["model"] in names:
            dx, dy = names[r["model"]]
            ax.annotate(f"{short(r['model'])} ({r['size']}, {r['p95_ms']} ms)", (r["p95_ms"], r["integral"]),
                        xytext=(dx, dy), textcoords="offset points", fontsize=9, ha="right" if dx < 0 else "left",
                        color=NAVY if r["model"] == AK else "#3A3F4F", fontweight="bold" if r["model"] == AK else "normal")
    ax.set_xlabel("p95 latency per request, ms (lower is better)")
    ax.set_ylabel("Integral score (higher is better)")
    ax.set_xlim(0, 460)
    ax.grid(alpha=0.25)
    finish(fig, ax, "The top score at 72.3 ms p95, ahead of 8B to 15B models",
           f"Dot size is parameter count. {len(rows)} models with integral above 0.6 shown. HiveTrace measured latency itself.",
           "chart-latency-vs-score.png")


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    floor_vs_score()
    heatmap()
    fpr_fnr()
    latency()

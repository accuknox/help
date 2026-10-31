"""Build the AccuKnox Shadow AI Coverage one-pager (A4) as HTML, PDF and PNG.

Run: python references/drafts/shadow-ai-one-pager/build.py
Brand tokens, logos and the AccuKnox logo come from the ak-pptx skill assets.
"""
import base64
import glob
import json
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
AK = Path(glob.glob(os.path.expanduser(
    "~/.claude/skills/synced/*/ak-pptx/assets"))[0])

ICONIFY = json.loads((AK / "brand-logos-iconify.json").read_text(encoding="utf8"))


def logo(name, h=14, title=None):
    """Inline full colour brand logo from the bundled iconify set."""
    ic = ICONIFY["icons"][name]
    w = ic.get("width", ICONIFY["width"])
    ht = ic.get("height", ICONIFY["height"])
    t = f"<title>{title}</title>" if title else ""
    return (f'<svg class="lg" style="height:{h}px;width:{h * w / ht:.1f}px" '
            f'viewBox="0 0 {w} {ht}" xmlns="http://www.w3.org/2000/svg">{t}{ic["body"]}</svg>')


def img64(p):
    return "data:image/png;base64," + base64.b64encode(Path(p).read_bytes()).decode()


# Tabler outline icons, 24px grid, stroke 2.
TB = {
    "browser": '<rect x="4" y="4" width="16" height="16" rx="1"/><path d="M4 8h16M8 4v4"/>',
    "server": '<rect x="3" y="4" width="18" height="8" rx="3"/><rect x="3" y="12" width="18" height="8" rx="3"/><path d="M7 8v.01M7 16v.01"/>',
    "terminal": '<path d="M5 7l5 5l-5 5M12 19h7"/>',
    "alert": '<path d="M12 9v4M10.36 3.6L2.2 17.2a1.9 1.9 0 0 0 1.64 2.8h16.32a1.9 1.9 0 0 0 1.64-2.8L13.64 3.6a1.9 1.9 0 0 0-3.28 0zM12 16h.01"/>',
    "shield": '<path d="M12 3a12 12 0 0 0 8.5 3a12 12 0 0 1-8.5 15a12 12 0 0 1-8.5-15a12 12 0 0 0 8.5-3"/><path d="M9 12l2 2l4-4"/>',
    "check": '<path d="M5 12l5 5l10-10"/>',
    "list": '<path d="M9 6h11M9 12h11M9 18h11M5 6v.01M5 12v.01M5 18v.01"/>',
    "policy": '<path d="M12 3a12 12 0 0 0 8.5 3a12 12 0 0 1-8.5 15a12 12 0 0 1-8.5-15a12 12 0 0 0 8.5-3"/><path d="M12 11v.01M12 11a1 1 0 1 0 0 0zM12 12v3"/>',
    "file": '<path d="M14 3v4a1 1 0 0 0 1 1h4"/><path d="M17 21H7a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h7l5 5v11a2 2 0 0 1-2 2zM9 13h6M9 17h6"/>',
    "arrow": '<path d="M5 12h14M13 6l6 6l-6 6"/>',
    "radar": '<path d="M21 12h-8a1 1 0 1 0-1 1v8a9 9 0 0 0 9-9"/><path d="M16 9a5 5 0 1 0-7 7M20.49 10.5A9 9 0 1 0 10.5 20.49"/>',
    "activity": '<path d="M3 12h4l3 8l4-16l3 8h4"/>',
}


def tb(name, cls="ic"):
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{TB[name]}</svg>')


def chip(lg, label, h=13):
    return f'<span class="chip">{logo(lg, h)}{label}</span>'


CATS = [  # category, assets found, critical
    ("AI/ML frameworks", 2308, 72),
    ("AI SDKs", 1180, 9),
    ("AI automation", 296, 6),
    ("AI agents", 124, 12),
    ("MCP servers", 53, 1),
    ("AI inference engines", 40, 2),
    ("AI gateways", 25, 28),
]
MAXA = max(c[1] for c in CATS)
MAXC = max(c[2] for c in CATS)
def bar(n, a, c):
    return (f'<div class="br"><span class="bn">{n}</span>'
    f'<span class="bt"><i style="width:{max(a / MAXA * 100, 1.2):.1f}%"></i></span>'
    f'<b class="ba">{a:,}</b>'
    f'<span class="bc"><i style="width:{max(c / MAXC * 100, 4):.1f}%"></i></span><b class="bcn">{c}</b></div>')


bars = ('<div>' + "".join(bar(*c) for c in CATS[:4]) + '</div><div>'
        + "".join(bar(*c) for c in CATS[4:]) + '</div>')

AI_TILES = [
    ("openai-icon", "ChatGPT"), ("google-gemini-icon", "Gemini"),
    ("claude-icon", "Claude"), ("perplexity-icon", "Perplexity"),
    ("cursor-icon", "Cursor"), ("codex", "Codex"),
    ("claude-code", "Claude Code"), ("google-gemini-icon", "Gemini CLI"),
]
tiles = "".join(f'<div class="tile">{logo(k, 20)}<span>{t}</span></div>' for k, t in AI_TILES)

FULL = f'<span class="pill">{tb("check", "pi")}Full coverage</span>'

html = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>Shadow AI Coverage One Pager</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
<style>
@page {{ size:A4; margin:0; }}
:root {{ --ink:#000025; --blue:#1040C5; --mid:#3A63E0; --acc:#6464FF; --peri:#8FA8FF; --tint:#E8EDFF;
  --tintA:#EFEFFF; --soft:#F6F8FF; --bd:#DCE3F0; --body:#37474F; --muted:#607D8B; --red:#D63637; --redt:#FDEDED; --warn:#E8A600; }}
* {{ box-sizing:border-box; margin:0; padding:0; }}
html,body {{ background:#fff; color:var(--body); font-family:Inter,"Segoe UI",Arial,sans-serif; -webkit-print-color-adjust:exact; print-color-adjust:exact; }}
.page {{ width:210mm; height:297mm; overflow:hidden; position:relative; background:#fff; display:flex; flex-direction:column; }}
.page > * {{ flex-shrink:0; }}
.mono {{ font-family:"JetBrains Mono",Consolas,monospace; letter-spacing:.02em; }}
.lg {{ display:inline-block; flex:none; vertical-align:middle; }}
.ic {{ width:15px; height:15px; flex:none; }}

/* header */
.hd {{ background:var(--ink); color:#fff; padding:5mm 10mm 11.5mm; position:relative; overflow:hidden; }}
.hd::before, .hd::after {{ content:""; position:absolute; border-radius:50%; border:1px solid rgba(143,168,255,.16); }}
.hd::before {{ width:150mm; height:150mm; right:-55mm; top:-60mm; }}
.hd::after {{ width:105mm; height:105mm; right:-32mm; top:-37mm; }}
.top {{ display:flex; justify-content:space-between; align-items:center; position:relative; z-index:1; }}
.top img {{ height:6.2mm; }}
.top .mono {{ font-size:6.6pt; color:var(--peri); }}
.hgrid {{ display:grid; grid-template-columns:1fr 61mm; gap:7mm; margin-top:3mm; position:relative; z-index:1; }}
.kick {{ font-size:7pt; color:#fff; background:var(--blue); display:inline-block; padding:1mm 2.4mm; border-radius:99px; font-weight:700; }}
h1 {{ font-size:21pt; line-height:1.05; font-weight:800; letter-spacing:-.025em; margin-top:2.2mm; color:#fff; }}
h1 em {{ font-style:normal; color:var(--peri); }}
.lead {{ font-size:7.9pt; line-height:1.4; color:#C9D3F5; margin-top:2.2mm; }}
.lead b {{ color:#fff; }}
.cloud {{ background:rgba(255,255,255,.05); border:1px solid rgba(143,168,255,.28); border-radius:9px; padding:2.6mm; }}
.cloud .mono {{ font-size:6pt; color:var(--peri); display:block; margin-bottom:1.8mm; }}
.tiles {{ display:grid; grid-template-columns:repeat(4,1fr); gap:1.6mm; }}
.tile {{ background:#fff; border-radius:6px; height:11.6mm; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:1mm; }}
.tile span {{ font-size:5.6pt; font-weight:600; color:var(--ink); white-space:nowrap; }}
.cloud .foot {{ font-size:6.2pt; color:#C9D3F5; margin-top:1.8mm; line-height:1.35; }}

/* stats */
.stats {{ margin:-10mm 10mm 0; background:#fff; border-radius:10px; box-shadow:0 6px 18px rgba(0,0,37,.14); border:1px solid var(--bd);
  display:grid; grid-template-columns:repeat(4,1fr); position:relative; z-index:2; }}
.st {{ padding:2.4mm 3.2mm 2.6mm; border-right:1px solid var(--bd); }}
.st:last-child {{ border-right:0; }}
.tag {{ font-size:5.6pt; font-weight:700; padding:.5mm 1.6mm; border-radius:3px; display:inline-block; }}
.tag.new {{ background:var(--blue); color:#fff; }}
.tag.exp {{ background:var(--tintA); color:var(--acc); }}
.num {{ font-size:22pt; font-weight:300; color:var(--blue); line-height:1; margin-top:1.4mm; letter-spacing:-.03em; }}
.st h4 {{ font-size:7.8pt; color:var(--ink); font-weight:700; margin-top:1mm; line-height:1.2; }}
.st .lgs {{ display:flex; gap:2mm; align-items:center; margin-top:1.8mm; flex-wrap:wrap; }}
.st .sub {{ font-size:6.4pt; color:var(--muted); line-height:1.35; margin-top:1.2mm; }}

/* section head */
.sec {{ display:flex; justify-content:space-between; align-items:flex-end; margin:2.8mm 10mm 1.6mm; }}
.sec .mono {{ font-size:6.4pt; color:var(--blue); font-weight:700; }}
.sec h2 {{ font-size:12pt; color:var(--ink); font-weight:800; letter-spacing:-.015em; margin-top:.6mm; }}
.legend {{ display:flex; gap:3mm; font-size:6.4pt; color:var(--muted); align-items:center; }}
.dot {{ width:2.2mm; height:2.2mm; border-radius:50%; display:inline-block; margin-right:1mm; vertical-align:-.3mm; }}

/* surface cards */
.cols {{ display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:2.8mm; margin:0 10mm; }}
.card {{ border:1px solid var(--bd); border-top:3px solid var(--blue); border-radius:8px; padding:2.4mm 2.8mm 2.6mm; display:flex; flex-direction:column; gap:1.5mm; background:#fff; }}
.ch {{ display:grid; grid-template-columns:auto minmax(0,1fr); gap:1.6mm; align-items:center; }}
.ch .tl {{ display:flex; align-items:center; justify-content:space-between; gap:1mm; }}
.card .ch h3 {{ white-space:nowrap; font-size:9.4pt; }}
.card .ch .pill {{ white-space:nowrap; font-size:5.3pt; padding:.5mm 1.5mm .5mm 1.1mm; }}
.card .one {{ grid-column:1 / -1; }}
.badge {{ display:flex; }}
.n {{ width:7.4mm; height:7.4mm; border-radius:50%; background:var(--ink); color:#fff; font-size:6.6pt; font-weight:700; display:flex; align-items:center; justify-content:center; }}
.ibox {{ width:6.4mm; height:6.4mm; border-radius:5px; background:var(--tint); color:var(--blue); display:flex; align-items:center; justify-content:center; }}
.ibox .ic {{ width:11px; height:11px; }}
.pill {{ background:var(--blue); color:#fff; font-size:5.8pt; font-weight:700; padding:.7mm 1.8mm .7mm 1.3mm; border-radius:99px; display:inline-flex; align-items:center; gap:.8mm; }}
.pi {{ width:8px; height:8px; stroke-width:3; }}
.eb {{ font-size:5.8pt; font-weight:700; color:var(--blue); }}
.card h3 {{ font-size:10.5pt; color:var(--ink); font-weight:800; letter-spacing:-.01em; line-height:1.1; }}
.card .one {{ font-size:6.6pt; color:var(--body); line-height:1.35; margin-top:.8mm; }}
.lab {{ font-size:5.4pt; font-weight:700; color:var(--muted); margin-bottom:.7mm; display:flex; align-items:center; gap:1.2mm; }}
.chips {{ display:flex; flex-wrap:wrap; gap:.6mm; }}
.chip {{ display:inline-flex; align-items:center; gap:1.1mm; border:1px solid var(--bd); background:#fff; border-radius:4px; padding:.35mm .9mm; font-size:5.6pt; gap:.8mm; font-weight:600; color:var(--ink); white-space:nowrap; }}
.risk {{ background:var(--redt); border-left:2.5px solid var(--red); border-radius:0 6px 6px 0; padding:1.2mm 1.8mm; font-size:6.3pt; line-height:1.34; color:#3a2020; }}
.risk .k {{ color:var(--red); font-size:5.8pt; font-weight:800; display:flex; align-items:center; gap:1mm; margin-bottom:.5mm; }}
.risk .k .ic {{ width:9px; height:9px; }}
.how {{ background:var(--soft); border-left:2.5px solid var(--blue); border-radius:0 6px 6px 0; padding:1.2mm 1.8mm; font-size:6.3pt; line-height:1.34; }}
.how .k {{ color:var(--blue); font-size:5.8pt; font-weight:800; display:flex; align-items:center; gap:1mm; margin-bottom:.5mm; }}
.how .k .ic {{ width:9px; height:9px; }}
.ctl {{ display:flex; flex-wrap:wrap; gap:1mm; }}
.ctl span {{ background:var(--tint); color:var(--blue); font-size:5.7pt; font-weight:600; padding:.4mm 1.4mm; border-radius:99px; display:inline-flex; align-items:center; gap:.7mm; }}
.ctl .pi {{ width:7px; height:7px; }}
.os {{ border:1px solid var(--bd); border-radius:6px; overflow:hidden; }}
.os div {{ display:flex; align-items:center; gap:1.6mm; padding:.8mm 2mm; font-size:6.4pt; font-weight:600; color:var(--ink); border-bottom:1px solid var(--bd); }}
.os div:last-child {{ border-bottom:0; }}
.os .ok {{ margin-left:auto; color:var(--blue); font-size:6pt; display:inline-flex; align-items:center; gap:.6mm; }}
.os .tag {{ font-size:5.2pt; }}

/* data strip */
.data {{ margin:2.4mm 10mm 0; border:1px solid var(--bd); border-radius:8px; display:grid; grid-template-columns:1fr 52mm; overflow:hidden; }}
.chart {{ padding:2.2mm 3.2mm 2mm; }}
.chart .ttl {{ font-size:5.8pt; font-weight:800; color:var(--blue); margin-bottom:1.2mm; display:flex; justify-content:space-between; }}
.chart .ttl span {{ color:var(--muted); font-weight:600; }}
.chart .ttl i {{ font-style:normal; color:var(--red); }}
.c2 {{ display:grid; grid-template-columns:1fr 1fr; column-gap:5mm; }}
.chart .th {{ display:grid; grid-template-columns:24mm 1fr 11mm 16mm 6mm; gap:1.6mm; font-size:5.6pt; font-weight:700; color:var(--muted); margin-bottom:1mm; }}
.br {{ display:grid; grid-template-columns:22mm 1fr 8.5mm 9mm 4mm; gap:1.2mm; align-items:center; height:3.5mm; }}
.bn {{ font-size:6.5pt; color:var(--ink); font-weight:500; white-space:nowrap; }}
.bt, .bc {{ height:2.1mm; background:var(--soft); border-radius:2px; overflow:hidden; }}
.bt i {{ display:block; height:100%; background:var(--blue); border-radius:2px; }}
.bc i {{ display:block; height:100%; background:var(--red); border-radius:2px; }}
.ba {{ font-size:6.5pt; color:var(--ink); text-align:right; font-variant-numeric:tabular-nums; }}
.bcn {{ font-size:6.5pt; color:var(--red); text-align:right; }}
.callout {{ background:var(--ink); color:#fff; padding:2.2mm 3.2mm; display:grid; grid-template-columns:1fr 1fr; gap:1.4mm 2.4mm; align-content:center; }}
.callout .fn {{ grid-column:1 / -1; }}
.callout .big {{ font-size:18pt; font-weight:300; line-height:1; letter-spacing:-.02em; }}
.callout .big.r {{ color:#FF7A7B; }}
.callout .cap {{ font-size:6.4pt; color:#C9D3F5; line-height:1.3; margin-top:.6mm; }}
.callout .fn {{ font-size:5.6pt; color:var(--peri); line-height:1.35; border-top:1px solid rgba(143,168,255,.3); padding-top:1.6mm; }}

/* unified band */
.uni {{ background:var(--ink); color:#fff; margin-top:auto; padding:3.2mm 10mm 2.6mm; }}
.uni .mono {{ font-size:6.4pt; color:var(--peri); font-weight:700; }}
.uni h2 {{ font-size:12pt; font-weight:800; letter-spacing:-.015em; margin-top:.6mm; }}
.uni h2 + p {{ font-size:6.8pt; color:#C9D3F5; margin-top:.4mm; }}
.flow {{ display:grid; grid-template-columns:40mm 5mm 33mm 5mm 1fr; align-items:stretch; gap:1.2mm; margin-top:2.4mm; }}
.srcs {{ display:flex; flex-direction:column; gap:1.2mm; justify-content:center; }}
.src {{ background:rgba(255,255,255,.06); border:1px solid rgba(143,168,255,.28); border-radius:6px; padding:1mm 2mm; display:flex; align-items:center; gap:1.6mm; }}
.src b {{ font-size:6.8pt; width:12mm; }}
.src .lw {{ display:flex; gap:1.3mm; background:#fff; border-radius:4px; padding:.8mm 1.3mm; }}
.arr {{ color:var(--peri); display:flex; justify-content:center; align-items:center; }}
.arr .ic {{ width:16px; height:16px; }}
.core {{ background:var(--blue); border-radius:10px; padding:2.2mm 2mm; text-align:center; display:flex; flex-direction:column; align-items:center; justify-content:center; }}
.core img {{ width:9mm; background:#fff; border-radius:50%; padding:1.4mm; }}
.core b {{ display:block; font-size:8pt; margin-top:1.4mm; }}
.core span {{ display:block; font-size:6pt; color:#D9E1FF; margin-top:.5mm; line-height:1.3; }}
.outs {{ display:grid; grid-template-columns:repeat(3,1fr); gap:1.4mm; }}
.out {{ background:#fff; color:var(--body); border-radius:6px; padding:1.8mm 2.2mm; }}
.out b {{ display:flex !important; align-items:center; gap:1.4mm; margin-bottom:.8mm; }}
.out .ibox {{ width:5mm; height:5mm; }}
.out b {{ display:block; color:var(--ink); font-size:7.2pt; }}
.out p {{ font-size:6.1pt; line-height:1.28; }}
.beta {{ margin-top:1.8mm; border:1px dashed rgba(143,168,255,.5); border-radius:7px; padding:1.8mm 2.4mm; display:flex; align-items:center; gap:2.4mm; }}
.beta .tag {{ background:var(--warn); color:var(--ink); }}
.beta .lw {{ display:flex; gap:1.4mm; background:#fff; border-radius:4px; padding:.9mm 1.4mm; }}
.beta p {{ font-size:6.5pt; color:#C9D3F5; line-height:1.35; }}
.beta p b {{ color:#fff; }}
.beta .gh {{ margin-left:auto; font-size:6.2pt; color:var(--peri); white-space:nowrap; display:flex; align-items:center; gap:1.2mm; }}
.ft {{ display:flex; justify-content:space-between; align-items:center; margin-top:1.8mm; padding-top:1.6mm; border-top:1px solid rgba(143,168,255,.25); font-size:6.6pt; }}
.ft a {{ color:#fff; text-decoration:none; margin-right:4mm; font-weight:600; }}
.ft .mono {{ font-size:6pt; }}
</style></head>
<body><div class="page">

<header class="hd">
  <div class="top"><img src="{img64(AK / 'logo-white.png')}" alt="AccuKnox"><span class="mono">AI SECURITY · SHADOW AI COVERAGE · OCT 2026</span></div>
  <div class="hgrid">
    <div>
      <span class="kick">SHADOW AI DISCOVERY &amp; CONTROL</span>
      <h1><em>Discover</em> Every Shadow AI.<br><em>Secure</em> Every Endpoint.<br><em>Control</em> Every AI Interaction.</h1>
      <p class="lead">Employees paste company documents into chatbots. Developers install agents, SDKs and MCP servers on shared hosts. Coding assistants run in terminals with shell access. <b>Most of it never reaches an asset register.</b></p>
    </div>
    <div class="cloud">
      <span class="mono">AI TOOLS ACCUKNOX SEES AND CONTROLS</span>
      <div class="tiles">{tiles}</div>
      <p class="foot">Plus 100+ agents, SDKs, MCP servers, frameworks, inference engines, gateways and automation tools found on hosts.</p>
    </div>
  </div>
</header>

<section class="stats">
  <div class="st"><span class="tag new">NEW</span><div class="num">100+</div><h4>Shadow AI tools discovered on hosts</h4>
    <p class="sub">Agents · MCP servers · SDKs · frameworks · inference engines · gateways · automation</p></div>
  <div class="st"><span class="tag new">NEW · WINDOWS</span><div class="num">3</div><h4>Operating systems for host scanning</h4>
    <div class="lgs">{logo('microsoft-windows-icon', 15)}{logo('linux-tux', 17)}{logo('apple', 16)}</div>
</div>
  <div class="st"><span class="tag exp">EXPANDED</span><div class="num">4</div><h4>Browsers protected by the plugin</h4>
    <div class="lgs">{logo('chrome', 15)}{logo('microsoft-edge', 15)}{logo('firefox', 15)}{logo('safari', 15)}</div>
</div>
  <div class="st"><span class="tag exp">EXPANDED</span><div class="num">4+</div><h4>CLI coding agents secured</h4>
    <div class="lgs">{logo('cursor-icon', 15)}{logo('claude-icon', 15)}{logo('codex', 15)}{logo('google-gemini-icon', 15)}</div>
</div>
</section>

<div class="sec">
  <div><span class="mono">COVERAGE BY SURFACE</span><h2>From the Browser Tab to the Terminal</h2></div>
  <div class="legend"><span><i class="dot" style="background:var(--blue)"></i>Full coverage</span><span><i class="dot" style="background:var(--warn)"></i>Beta</span><span><i class="dot" style="background:var(--red)"></i>Risk</span></div>
</div>

<div class="cols">
  <article class="card">
    <div class="ch"><div class="badge"><span class="n">01</span></div><div><span class="eb">BROWSERS &amp; CONVERSATIONAL AI</span><div class="tl"><h3>Browser Plugin</h3>{FULL}</div></div></div>
    <div><div class="lab">BROWSERS <span class="tag exp">EXPANDED</span></div>
      <div class="chips">{chip('chrome', 'Chrome', 10)}{chip('microsoft-edge', 'Edge', 10)}{chip('firefox', 'Firefox', 10)}{chip('safari', 'Safari', 10)}</div></div>
    <div><div class="lab">CONVERSATIONAL AI</div>
      <div class="chips">{chip('openai-icon', 'ChatGPT', 10)}{chip('google-gemini-icon', 'Gemini', 10)}{chip('claude-icon', 'Claude', 10)}{chip('perplexity-icon', 'Perplexity', 10)}</div></div>
    <div class="risk"><div class="k">{tb('alert')}THE RISK</div>Staff paste contracts, source code and customer records into ChatGPT, Gemini and similar tools. The company loses control of that data.</div>
    <div class="how"><div class="k">{tb('shield')}HOW ACCUKNOX COVERS IT</div>The extension inspects prompts and file uploads before they reach the AI app. It blocks, masks or logs them against company policy.</div>
    <div class="ctl"><span>{tb('check', 'pi')}Sensitive upload blocking</span><span>{tb('check', 'pi')}PII, PHI &amp; PCI masking</span><span>{tb('check', 'pi')}Secret prevention</span><span>{tb('check', 'pi')}Prompt &amp; response auditing</span></div>
  </article>

  <article class="card">
    <div class="ch"><div class="badge"><span class="n">02</span></div><div><span class="eb">HOSTS, VMS &amp; CONTAINERS</span><div class="tl"><h3>Host Scanning</h3>{FULL}</div></div></div>
    <div><div class="lab">PLATFORM SUPPORT</div>
      <div class="os">
        <div>{logo('microsoft-windows-icon', 11)}Windows <span class="tag new">NEW</span><span class="ok">{tb('check', 'pi')}Full</span></div>
        <div>{logo('linux-tux', 12)}Linux<span class="ok">{tb('check', 'pi')}Full</span></div>
        <div>{logo('apple', 12)}macOS<span class="ok">{tb('check', 'pi')}Full</span></div>
      </div></div>
    <div class="risk"><div class="k">{tb('alert')}THE RISK</div>Developers install agents, SDKs, MCP servers and local inference engines that never show up in cloud accounts or IAM logs.</div>
    <div class="how"><div class="k">{tb('shield')}HOW ACCUKNOX COVERS IT</div>Scans hosts, VMs and containers. Fingerprints 100+ Shadow AI tools across seven categories and ranks findings by severity.</div>
    <div class="ctl"><span>{tb('check', 'pi')}AI asset inventory</span><span>{tb('check', 'pi')}Vulnerability findings</span><span>{tb('check', 'pi')}Severity-based prioritization</span></div>
  </article>

  <article class="card">
    <div class="ch"><div class="badge"><span class="n">03</span></div><div><span class="eb">TERMINAL &amp; CLI CODING AGENTS</span><div class="tl"><h3>CLI Coding Agents</h3>{FULL}</div></div></div>
    <div><div class="lab">COVERS <span class="tag exp">EXPANDED</span></div>
      <div class="chips">{chip('cursor-icon', 'Cursor', 10)}{chip('claude-icon', 'Claude CLI', 10)}{chip('codex', 'Codex', 10)}{chip('google-gemini-icon', 'Gemini CLI', 10)}<span class="chip">{tb('terminal')}Other CLI agents</span></div></div>
    <div class="risk"><div class="k">{tb('alert')}THE RISK</div>CLI agents run with the developer's shell access. They can send source code, secrets and credentials to external models.</div>
    <div class="how"><div class="k">{tb('shield')}HOW ACCUKNOX COVERS IT</div>Supported CLI agent traffic routes through the AccuKnox Prompt Firewall, which enforces policy on every prompt and response.</div>
    <div class="ctl"><span>{tb('check', 'pi')}Policy enforcement</span><span>{tb('check', 'pi')}Sensitive code leak prevention</span><span>{tb('check', 'pi')}Secret &amp; credential leak prevention</span><span>{tb('check', 'pi')}Prompt injection &amp; jailbreak protection</span></div>
  </article>
</div>

<section class="data">
  <div class="chart">
    <div class="ttl">HOST SCAN RESULTS BY CATEGORY <span><b style="color:var(--blue)">Assets found (example)</b> · <i>Critical findings</i></span></div>
    <div class="c2">{bars}</div>
  </div>
  <div class="callout">
    <div><div class="big">4,026</div><div class="cap">unmanaged AI assets found</div></div>
    <div><div class="big r">130</div><div class="cap">critical findings, ranked by severity</div></div>
    <div class="fn">One monitored environment, Jul 26 to Sep 23, 2026. Tenant anonymized.</div>
  </div>
</section>

<section class="uni">
  <span class="mono">04 · BROWSER · HOSTS · CLI</span>
  <h2>Unified AI Visibility and Control</h2>
  <p>Browser activity, host-discovered AI assets and CLI coding agents all flow into one AccuKnox security workflow.</p>
  <div class="flow">
    <div class="srcs">
      <div class="src"><b>Browser</b><span class="lw">{logo('chrome', 11)}{logo('microsoft-edge', 11)}{logo('firefox', 11)}{logo('safari', 11)}</span></div>
      <div class="src"><b>Hosts</b><span class="lw">{logo('microsoft-windows-icon', 10)}{logo('linux-tux', 11)}{logo('apple', 11)}</span></div>
      <div class="src"><b>CLI</b><span class="lw">{logo('cursor-icon', 11)}{logo('claude-icon', 11)}{logo('codex', 11)}{logo('google-gemini-icon', 11)}</span></div>
    </div>
    <div class="arr">{tb('arrow')}</div>
    <div class="core"><img src="{img64(AK / 'accuknox-emblem.png')}" alt="AccuKnox emblem"><b>AccuKnox AI Security</b><span>One security workflow</span></div>
    <div class="arr">{tb('arrow')}</div>
    <div class="outs">
      <div class="out"><div><b><span class="ibox">{tb('list')}</span>Unified inventory</b><p>Managed and unmanaged AI assets in one view. Export as an AI-BOM in CycloneDX format.</p></div></div>
      <div class="out"><div><b><span class="ibox">{tb('policy')}</span>Policy controls</b><p>Define data and usage policy once. Enforce it through the browser plugin and Prompt Firewall.</p></div></div>
      <div class="out"><div><b><span class="ibox">{tb('file')}</span>Audit records</b><p>Prompt, response and detection records for investigations, audits and compliance reporting.</p></div></div>
    </div>
  </div>
  <div class="beta">
    <span class="tag">BETA</span>
    <span class="lw">{logo('claude-code', 11)}{logo('opentelemetry-icon', 12)}</span>
    <p><b>Desktop telemetry app.</b> Collects OpenTelemetry and HTTPS signals from desktop AI tools such as Claude Code to identify agents, tools and skills in use.</p>
    <span class="gh"><span class="lw">{logo('github-icon', 11)}</span>github.com/kubearmor/otel-adapter</span>
  </div>
  <div class="ft">
    <div><a href="https://accuknox.com">accuknox.com</a><a href="https://help.accuknox.com">help.accuknox.com</a><a href="https://github.com/accuknox">github.com/accuknox</a></div>
    <span class="mono" style="color:var(--peri)">COVERAGE STATUS AS OF OCT 2026</span>
  </div>
</section>

</div></body></html>"""

out_html = HERE / "shadow-ai-coverage-one-pager.html"
out_html.write_text(html, encoding="utf8")

from playwright.sync_api import sync_playwright  # noqa: E402

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 794, "height": 1123}, device_scale_factor=2)
    pg.goto(out_html.as_uri(), wait_until="networkidle")
    pg.evaluate("document.fonts.ready")
    over = pg.evaluate("""() => { const p=document.querySelector('.page');
      const kids=[...p.querySelectorAll('*')].filter(e=>e.scrollWidth>e.clientWidth+1 && getComputedStyle(e).overflow!=='visible');
      return {pageH:p.scrollHeight, clientH:p.clientHeight, clipped:kids.length, parts:[...p.children].map(e=>e.className+":"+Math.round(e.getBoundingClientRect().bottom*25.4/96))}; }""")
    print("layout", over)
    pg.screenshot(path=str(HERE / "shadow-ai-coverage-one-pager.png"), full_page=True)
    pg.pdf(path=str(HERE / "shadow-ai-coverage-one-pager.pdf"), format="A4", print_background=True,
           margin={"top": "0", "bottom": "0", "left": "0", "right": "0"})
    b.close()
print("done")

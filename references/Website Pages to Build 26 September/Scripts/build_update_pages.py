"""Build self-contained update-*.html pages and index.html for the web team.

Each change is written as plain steps: where to look, what to delete, what to type, which links to add.
Every screenshot is embedded as a WebP data URI, so each file works on its own after a zip.
Output goes to ../Prototype HTMLs/.
"""
import base64, html, io, pathlib
from PIL import Image

HERE = pathlib.Path(__file__).parent
OUT = HERE.parent / "Prototype HTMLs"
SHOTS = HERE / "shots"
SITE = "https://accuknox.com"

KIND = {  # label, color
    "text": ("Change text", "#b45309"),
    "new": ("Add a new section", "#15803d"),
    "replace": ("Replace a section", "#b91c1c"),
    "link": ("Fix a link", "#6d28d9"),
    "move": ("Move a menu item", "#1d4ed8"),
    "add": ("Add items", "#15803d"),
}

PAGES = [
    ("update-nav-mega-menu.html", "Menu", "The top menu"),
    ("update-ai-security.html", "AI Security", "The AI Security page"),
    ("update-platform.html", "Platform", "The Platform page"),
    ("update-platform-dspm.html", "DSPM", "The DSPM page"),
    ("update-sast-dast-aspm.html", "SAST, DAST, ASPM", "The SAST, DAST and ASPM pages"),
]
NEW_PAGES = [
    ("new-page-shadow-ai-discovery.html", "New: Shadow AI page"),
    ("new-page-dspm-indian-banks.html", "New: DSPM for Indian Banks page"),
    ("new-page-ciem.html", "New: CIEM page"),
]


def e(s):
    return html.escape(s)


def img(name, width=1200, alt=""):
    im = Image.open(SHOTS / name).convert("RGB")
    if im.width > width:
        im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "WEBP", quality=80, method=6)
    return f'<img src="data:image/webp;base64,{base64.b64encode(buf.getvalue()).decode()}" alt="{e(alt)}" loading="lazy">'


CSS = """
:root{--ink:#18181b;--mute:#52525b;--line:#d4d4d8;--soft:#f4f4f5;--del:#b91c1c;--delbg:#fef2f2;--add:#15803d;--addbg:#f0fdf4;--lnk:#1d4ed8;--lnkbg:#eff6ff}
*{box-sizing:border-box}
body{margin:0;background:#fff;color:var(--ink);font:17px/1.6 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
a{color:var(--lnk)}
:focus-visible{outline:3px solid var(--lnk);outline-offset:2px}
.wrap{max-width:1080px;margin:0 auto;padding:0 20px}
.top{background:#18181b;font-size:14px}
.top .wrap{display:flex;gap:6px 8px;flex-wrap:wrap;align-items:center;padding-top:10px;padding-bottom:10px}
.top a{color:#e4e4e7;text-decoration:none;padding:4px 10px;border-radius:5px}
.top a[aria-current=page]{background:#fff;color:#18181b;font-weight:700}
header{padding:34px 0 8px}
h1{font-size:clamp(28px,4vw,40px);line-height:1.15;margin:0 0 12px}
h2{font-size:24px;margin:36px 0 12px}
.addr{font-size:18px;margin:0 0 6px}
.sub{color:var(--mute);margin:0}
.key{display:flex;flex-wrap:wrap;gap:10px 22px;background:var(--soft);border-radius:8px;padding:14px 18px;margin:22px 0 0;font-size:15px}
.key span{display:inline-flex;align-items:center;gap:8px}
.sw{display:inline-block;width:18px;height:18px;border-radius:4px;border:2px solid}
.todo{list-style:none;padding:0;margin:0;border:1px solid var(--line);border-radius:8px;overflow:hidden}
.todo li{display:flex;gap:14px;align-items:center;padding:12px 16px;border-bottom:1px solid var(--line)}
.todo li:last-child{border-bottom:0}
.todo input{width:20px;height:20px;flex:none}
.todo .n{font-weight:800;min-width:26px}
.todo a{font-weight:600}
.pill{display:inline-block;color:#fff;font-weight:700;font-size:13px;padding:3px 10px;border-radius:99px;white-space:nowrap}
.change{border:2px solid var(--line);border-radius:12px;margin:34px 0;overflow:hidden;scroll-margin-top:10px}
.change .hd{padding:16px 20px;background:var(--soft);border-bottom:1px solid var(--line)}
.change .hd .step{font-size:14px;font-weight:700;color:var(--mute);text-transform:uppercase;letter-spacing:.05em;margin-right:10px}
.change .hd h3{font-size:22px;margin:6px 0 0;line-height:1.3}
.change .bd{padding:20px}
.label{font-size:13px;font-weight:800;text-transform:uppercase;letter-spacing:.06em;color:var(--mute);margin:22px 0 8px}
.label:first-child{margin-top:0}
.where{margin:0 0 12px}
figure{margin:0}
figure img{width:100%;height:auto;display:block;border:1px solid var(--line);border-radius:8px}
figcaption{font-size:14px;color:var(--mute);margin-top:6px}
ol.steps{margin:0;padding-left:0;list-style:none;counter-reset:s}
ol.steps>li{counter-increment:s;position:relative;padding-left:44px;margin:0 0 16px}
ol.steps>li::before{content:counter(s);position:absolute;left:0;top:0;width:30px;height:30px;border-radius:50%;background:#18181b;color:#fff;font-weight:800;font-size:15px;display:flex;align-items:center;justify-content:center}
.del,.ins{border-radius:8px;padding:12px 14px;margin:8px 0 0;font-size:16.5px}
.del{background:var(--delbg);border:2px solid var(--del);color:#450a0a}.del s{text-decoration-color:rgba(185,28,28,.6);text-decoration-thickness:2px}
.ins{background:var(--addbg);border:2px solid var(--add);color:#052e16}
.del::before,.ins::before{display:block;font-size:12px;font-weight:800;letter-spacing:.06em;text-transform:uppercase;text-decoration:none;margin-bottom:4px}
.del::before{content:"Delete this";color:var(--del)}
.ins::before{content:"Type this";color:var(--add)}
.ins.item::before{content:"Add this"}
.ins ul,.ins ol{margin:4px 0 0;padding-left:22px}
table.links{border-collapse:collapse;width:100%;font-size:15.5px;background:var(--lnkbg);border:2px solid var(--lnk);border-radius:8px;overflow:hidden}
table.links th,table.links td{padding:10px 12px;border-bottom:1px solid #bfdbfe;text-align:left;vertical-align:top}
table.links th{background:#dbeafe;font-size:13px;text-transform:uppercase;letter-spacing:.05em}
table.links td:nth-child(2){word-break:break-all}
.lw{overflow-x:auto}
.preview{border:2px solid #a1a1aa;border-radius:10px;padding:18px;background:#fff}
.preview .ph{font-weight:800;font-size:20px;margin:0 0 10px}
.preview .ps{color:var(--mute);font-size:15px;margin:10px 0 0}
.g{display:grid;gap:10px}
.g2{grid-template-columns:repeat(2,minmax(0,1fr))}.g3{grid-template-columns:repeat(3,minmax(0,1fr))}
.g4{grid-template-columns:repeat(4,minmax(0,1fr))}.g5{grid-template-columns:repeat(5,minmax(0,1fr))}
.card{border:1px solid #a1a1aa;border-radius:6px;padding:10px 12px;font-size:14.5px;min-width:0;background:#fafafa}
.card b{display:block;font-size:15px;margin-bottom:2px}
.card.new{border:2px solid var(--add);background:var(--addbg)}
.tag{display:inline-block;font-size:11px;font-weight:800;text-transform:uppercase;letter-spacing:.05em;border:1px solid #3f3f46;border-radius:99px;padding:1px 8px;margin-bottom:5px;background:#fff}
.tag.soon{border-style:dashed}
.btn{display:inline-block;border:2px solid #3f3f46;border-radius:6px;padding:5px 12px;font-size:14px;font-weight:700;margin-top:10px;background:#fff}
.menu{max-width:420px;border:1px solid #a1a1aa;border-radius:6px;padding:6px 0;font-size:15px;background:#fff}
.menu div{padding:6px 14px}
.menu .new{background:var(--addbg);border-left:5px solid var(--add);font-weight:700}
.menu .fix{background:#f5f3ff;border-left:5px solid #6d28d9;font-weight:700}
.menu .mv{background:var(--lnkbg);border-left:5px solid var(--lnk);font-weight:700}
.menu .dim{color:#71717a}
.menu .grp{font-size:12px;text-transform:uppercase;letter-spacing:.06em;color:var(--mute)}
.ask{background:#fefce8;border:2px solid #eab308;border-radius:8px;padding:10px 14px;font-size:15.5px;margin-top:16px}
.ask b{display:block;font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:#854d0e}
table.plain{border-collapse:collapse;width:100%;font-size:14.5px}
table.plain th,table.plain td{border:1px solid var(--line);padding:8px 10px;text-align:left;vertical-align:top}
table.plain th{background:var(--soft)}
.files{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}
.files a{display:block;border:2px solid var(--line);border-radius:10px;padding:16px;text-decoration:none;color:var(--ink)}
.files a:hover{border-color:#18181b}
.files a b{display:block;font-size:18px}
.files a span{font-size:15px;color:var(--mute)}
footer{margin:40px 0 0;padding:20px 0 40px;border-top:1px solid var(--line);font-size:14px;color:var(--mute)}
@media (max-width:820px){.g2,.g3,.g4,.g5,.files{grid-template-columns:1fr}}
"""


def topnav(current):
    items = [("index.html", "Start here")] + [(f, s) for f, s, _ in PAGES] + list(NEW_PAGES)
    return ('<nav class="top" aria-label="All files"><div class="wrap">' +
            "".join(f'<a href="{f}"{" aria-current=page" if f == current else ""}>{e(t)}</a>' for f, t in items) +
            "</div></nav>")


def pill(kind):
    label, color = KIND[kind]
    return f'<span class="pill" style="background:{color}">{label}</span>'


def render_step(s):
    t, v = s
    if t == "do":
        return f"<li>{v}</li>"
    if t == "delete":
        return f'<li>Find this text and delete it.<div class="del"><s>{v}</s></div></li>'
    if t == "type":
        return f'<li>Type this text in its place.<div class="ins">{v}</div></li>'
    if t == "add":
        return f'<li>{v[0]}<div class="ins item">{v[1]}</div></li>'
    raise ValueError(t)


def change_html(i, total, c):
    parts = [f'<p class="label">Where to look</p><p class="where">{c["where"]}</p>']
    if c.get("shot"):
        tag = c.get("tag") or c["shot"].split("-")[0].split(".")[0]
        parts.append(f'<figure>{img(c["shot"], alt="Where to make this change on the live page")}'
                     f'<figcaption>Picture of the live page. Look for the colored box labeled <b>{tag}</b>.</figcaption></figure>')
    parts.append('<p class="label">What to do</p><ol class="steps">' + "".join(render_step(s) for s in c["steps"]) + "</ol>")
    if c.get("links"):
        rows = "".join(f"<tr><td>{w}</td><td><a href=\"{u}\">{e(u)}</a>{('<br><small>' + n + '</small>') if n else ''}</td></tr>"
                       for w, u, n in c["links"])
        parts.append('<p class="label">Links to add</p><div class="lw"><table class="links"><thead><tr><th>Make these words a link</th>'
                     f"<th>Link them to this address</th></tr></thead><tbody>{rows}</tbody></table></div>")
    if c.get("preview"):
        parts.append(f'<p class="label">How it should look when done</p><div class="preview">{c["preview"]}</div>')
    if c.get("ask"):
        parts.append(f'<div class="ask"><b>Check with Atharva before publishing</b>{c["ask"]}</div>')
    return (f'<section class="change" id="{c["code"]}"><div class="hd"><span class="step">Change {i} of {total}</span>{pill(c["kind"])}'
            f'<h3>{c["title"]}</h3></div><div class="bd">{"".join(parts)}</div></section>')


def build(fname, heading, address, intro, changes, extra=""):
    total = len(changes)
    todo = "".join(f'<li><input type="checkbox" aria-label="Done: change {i}"><span class="n">{i}.</span>'
                   f'<a href="#{c["code"]}">{c["title"]}</a>{pill(c["kind"])}</li>' for i, c in enumerate(changes, 1))
    addr = " · ".join(f'<a href="{a}">{e(a)}</a>' for a in address) if address else "Every page on accuknox.com"
    key = ('<div class="key"><span><i class="sw" style="background:var(--delbg);border-color:var(--del)"></i>Red box: delete this text</span>'
           '<span><i class="sw" style="background:var(--addbg);border-color:var(--add)"></i>Green box: type or add this</span>'
           '<span><i class="sw" style="background:var(--lnkbg);border-color:var(--lnk)"></i>Blue table: links to add</span>'
           '<span><i class="sw" style="background:#fefce8;border-color:#eab308"></i>Yellow box: check before publishing</span></div>')
    body = "".join(change_html(i, total, c) for i, c in enumerate(changes, 1))
    doc = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(heading)}</title><style>{CSS}</style></head><body>{topnav(fname)}
<header class="wrap"><h1>{e(heading)}</h1><p class="addr"><b>Page:</b> {addr}</p><p class="sub">{intro}</p>{key}</header>
<main class="wrap">{extra}<h2>Your {total} Changes, in Order</h2><ol class="todo">{todo}</ol>{body}</main>
<footer><div class="wrap">Tick each box as you finish a change. The ticks reset when you reload the page.</div></footer></body></html>"""
    (OUT / fname).write_text(doc, encoding="utf-8")


def C(code, kind, title, where, steps, **kw):
    d = dict(code=code, kind=kind, title=title, where=where, steps=steps)
    d.update(kw)
    return d


SOON = '<span class="tag soon">Coming soon</span>'
NEWPAGE = "This page is new. See the matching new-page file in this folder."

# ============================================================ 1. MENU
menu = [
    C("N1", "add", "Add 2 new items to the Secure AI menu",
      "Open the site. Hover over <b>Platform</b> in the top menu, then hover over <b>Secure AI</b>. A list of 10 items opens on the right.",
      [("do", "Find the first item, <b>AI SPM, Security Posture Management</b>."),
       ("add", ("Directly below it, add this new item.", "Shadow AI Discovery")),
       ("add", ("Below that, add this new item with a small <b>Coming soon</b> tag.", "AccuKnox AI Gateway " + SOON)),
       ("do", "Leave the other items where they are.")],
      shot="N1-menu.png",
      links=[("Shadow AI Discovery", SITE + "/solutions/shadow-ai-discovery", NEWPAGE),
             ("AccuKnox AI Gateway", SITE + "/platform/ai-security#ai-gateway", "This jumps to a new section on the AI Security page.")],
      preview='<div class="menu"><div>AI SPM, Security Posture Management</div><div class="new">Shadow AI Discovery</div>'
              f'<div class="new">AccuKnox AI Gateway {SOON}</div><div>AI Guardrails, Prompt Firewall</div><div>AI Red Teaming Pen Testing</div>'
              '<div>AI DR, Detect and Respond</div><div>Agentic AI Security</div><div>AI Identity Security</div><div class="dim">The other 5 items stay the same</div></div>'),
    C("N2", "link", "Fix the broken AI Identity Security link",
      "In the same Secure AI menu, find <b>AI Identity Security</b>. Today it goes nowhere.",
      [("do", "Change where <b>AI Identity Security</b> links to, using the address below."),
       ("do", "If that address does not work, hide the menu item until the page exists.")],
      shot="N1-menu.png", tag="N2",
      links=[("AI Identity Security", SITE + "/platform/ai-security#identity", "Today this item links to accuknox.com/#, which goes nowhere.")]),
    C("N3", "link", "Rename the broken AI SAST item and add AI DAST in Secure Code",
      "Hover over <b>Platform</b>, then over <b>Secure Code</b>. The last item in the list is broken.",
      [("delete", "AI-Accelerated SAST Scanning"),
       ("type", "AI SAST"),
       ("add", ("Find <b>Dynamic Application Security Testing (DAST)</b>. Directly below it, add this new item with a <b>Coming soon</b> tag.",
                "AI DAST (AI Pentesting) " + SOON))],
      shot="N3-menu.png",
      links=[("AI SAST", SITE + "/solutions/sast#ai-sast", "Today the old item links to accuknox.com/#."),
             ("AI DAST (AI Pentesting)", SITE + "/solutions/dast#ai-dast", "This jumps to a new section on the DAST page.")],
      preview='<div class="menu"><div>Static Application Security Testing (SAST)</div><div>Dynamic Application Security Testing (DAST)</div>'
              f'<div class="new">AI DAST (AI Pentesting) {SOON}</div><div>Software Composition Analysis (SCA)</div>'
              '<div class="dim">SBOM, Container Scanning, CI/CD, Secret Scanning, IaC stay the same</div><div class="fix">AI SAST</div></div>'),
    C("N4", "move", "Move DSPM out of Coming Soon and remove the BETA tag",
      "Hover over <b>Platform</b>, then over <b>Coming Soon</b>. DSPM sits in that list with a BETA tag.",
      [("do", "Remove <b>Data Security (DSPM) BETA</b> from the Coming Soon list."),
       ("add", ("In the main Platform list, add this item directly below <b>Secure Workload</b>. No BETA tag.", "Secure Data (DSPM)"))],
      shot="N4-menu.png",
      links=[("Secure Data (DSPM)", SITE + "/platform/dspm", "Same page as before. Only the menu position changes.")],
      preview='<div class="menu"><div>Secure Cloud</div><div>Secure Code</div><div>Secure Workload</div><div class="mv">Secure Data (DSPM)</div>'
              '<div>Secure AI</div><div>Secure APIs</div><div class="dim">The rest stays the same</div></div>'),
    C("N5", "add", "Point the Solutions menu to the 2 new pages",
      "Hover over <b>Solutions</b> in the top menu. Two columns change: <b>Use Cases</b> and <b>Security Across Industries</b>.",
      [("do", "In <b>Use Cases</b>, find <b>Shadow AI Discovery</b>. Keep the words. Change only the link, to the new page address below."),
       ("add", ("In <b>Use Cases</b>, add this new item directly below it.", "DSPM for Indian Banks")),
       ("add", ("In <b>Security Across Industries</b>, add the same item directly below <b>Finance</b>.", "DSPM for Indian Banks"))],
      links=[("Shadow AI Discovery", SITE + "/solutions/shadow-ai-discovery", "Today it links to the help docs. " + NEWPAGE),
             ("DSPM for Indian Banks (both places)", SITE + "/solutions/dspm-indian-banks", NEWPAGE)],
      preview='<div class="g g2"><div class="menu"><div class="grp">Use Cases</div><div class="fix">Shadow AI Discovery (new link)</div>'
              '<div class="new">DSPM for Indian Banks</div><div class="dim">The rest stays the same</div></div>'
              '<div class="menu"><div class="grp">Security Across Industries</div><div>Healthcare</div><div>Finance</div>'
              '<div class="new">DSPM for Indian Banks</div><div class="dim">The rest stays the same</div></div></div>'),
]
build("update-nav-mega-menu.html", "What to Change in the Top Menu", [],
      "Five changes, all inside the Platform and Solutions menus. Each change says which menu to open and what to add, fix or move.", menu)

# ============================================================ 2. AI SECURITY
five = [("Cloud AI services", "Agentless", "Finds AI models and agents in AWS, Azure and GCP accounts."),
        ("Browser plugin", "Full coverage", "Stops staff pasting company data into AI chat apps."),
        ("Host scanning", "Linux full, macOS beta", "Finds AI software, agents and MCP servers on servers."),
        ("Desktop telemetry app", "Beta", "Shows which tools and skills desktop AI apps use."),
        ("CLI agent security", "Full coverage", "Puts guardrails on coding agents in the terminal.")]
five_cards = "".join(f'<div class="card"><span class="tag{" soon" if "Beta" == t else ""}">{t}</span><b>{n}</b>{d}</div>' for n, t, d in five)
ai = [
    C("A1", "text", "Change the line under the main heading",
      "The very top of the page. The line of text right under the big heading.",
      [("delete", "Discover every model, agent, and pipeline. Close gaps across 43 compliances. Auto-generate your AI Bill of Materials."),
       ("type", "Discover every model, agent, MCP server and shadow AI tool. Govern model traffic through one AI gateway. Close gaps across 43 compliances and export your AI-BOM.")],
      shot="A1.png"),
    C("A2", "text", "Change one bullet and add 2 tiles to the module grid",
      "Scroll to <b>AI Security Platform</b>. The grid of 8 tiles is on the left. The text block about AI SPM is on the right.",
      [("do", "In the right-hand text block, find the second bullet."),
       ("delete", "Shadow AI discovery catches unapproved notebooks, rogue models, and MCP servers automatically."),
       ("type", "<b>Shadow AI discovery</b> finds unapproved AI across cloud accounts, browsers, hosts, desktop apps and CLI coding agents. See Shadow AI Discovery."),
       ("add", ("In the tile grid on the left, add 2 tiles after <b>Red Teaming &amp; Pen Testing</b>.",
                f"Shadow AI Discovery<br>AI Gateway {SOON}")),
       ("do", "Clicking a new tile scrolls down to its new section. Change 4 creates those sections.")],
      shot="A2.png",
      links=[("See Shadow AI Discovery (in the bullet)", SITE + "/solutions/shadow-ai-discovery", NEWPAGE),
             ("Shadow AI Discovery tile", SITE + "/platform/ai-security#shadow-ai", "Scrolls to the new section on this same page."),
             ("AI Gateway tile", SITE + "/platform/ai-security#ai-gateway", "Scrolls to the new section on this same page.")],
      preview='<div class="g g3"><div class="card">Security Posture Management</div><div class="card">Model &amp; Dataset Security</div><div class="card">Agentic AI Security</div>'
              '<div class="card">Detect &amp; Respond</div><div class="card">Governance, Risk &amp; Compliance</div><div class="card">Guardrails &amp; Prompt Firewall</div>'
              '<div class="card">Identity Security</div><div class="card">Red Teaming &amp; Pen Testing</div><div class="card new"><b>Shadow AI Discovery</b></div>'
              f'<div class="card new">{SOON}<b>AI Gateway</b></div></div>'),
    C("A3", "text", "Change one bullet in the Guardrails block",
      "In the same tile grid as change 2, click the <b>Guardrails &amp; Prompt Firewall</b> tile. Its text block appears on the right. Find the last bullet.",
      [("delete", "One policy enforced everywhere: API gateway, SDK, browser plugin, and Copilot Studio."),
       ("type", f"<b>One policy</b> enforced everywhere. The AccuKnox AI Gateway {SOON}, API gateways, the SDK, the browser plugin, CLI coding agents and Copilot Studio.")]),
    C("A4", "new", "Add 3 new sections above the Platform Tour",
      "Scroll to the heading <b>AI Security Platform Tour</b>. Add the 3 new sections directly above it, in the order below.",
      [("add", ("Add section 1. Give it the web address ending <code>#shadow-ai</code>, so the menu and tiles can jump to it.",
                "Heading: Shadow AI Hides in Five Places, and AccuKnox Covers Each One<br>Then 5 cards, a one-line status key, one number line and a button. See the picture below.")),
       ("add", ("Add section 2. Give it the web address ending <code>#ai-gateway</code>.",
                f"Heading: See Every Model Call, Then Govern It, Then Firewall It {SOON}<br>Then 3 numbered steps, a line on where it runs, and a line on what it works with.")),
       ("add", ("Add section 3. Give it the web address ending <code>#ai-appsec</code>.",
                "Heading: AI Tests Your Code and Your Running Apps Too<br>Then 2 cards, AI SAST and AI DAST, and one line under them.")),
       ("do", "Write the number as <b>4K+</b>. Never use the exact count.")],
      shot="A4.png",
      links=[("Explore Shadow AI Discovery (button in section 1)", SITE + "/solutions/shadow-ai-discovery", NEWPAGE),
             ("AI SAST (button in section 3)", SITE + "/solutions/sast#ai-sast", "Jumps to a new section on the SAST page."),
             ("AI DAST (button in section 3)", SITE + "/solutions/dast#ai-dast", "Jumps to a new section on the DAST page."),
             ("AI red teaming (in the line under section 3)", SITE + "/solutions/ai-red-teaming", "An existing page.")],
      preview=f'<p class="ph">Shadow AI Hides in Five Places, and AccuKnox Covers Each One</p><div class="g g5">{five_cards}</div>'
              '<p class="ps"><b>Full coverage</b> means available to everyone. <b>Beta</b> means available now, with more coverage coming. <b>In progress</b> means not available yet.</p>'
              '<p class="ps"><b>4K+</b> unmanaged AI assets found on servers in one environment in 60 days.</p><span class="btn">Explore Shadow AI Discovery</span>'
              '<hr style="border:0;border-top:2px dashed #a1a1aa;margin:22px 0">'
              f'<p class="ph">See Every Model Call, Then Govern It, Then Firewall It {SOON}</p><div class="g g3">'
              '<div class="card"><b>1. See it</b>A list of every AI model in use and who calls it.</div>'
              '<div class="card"><b>2. Govern it</b>Rules, rate limits and model access per team.</div>'
              '<div class="card"><b>3. Firewall it</b>The prompt firewall checks every prompt and reply.</div></div>'
              '<p class="ps">Runs in the cloud, on premises or air-gapped.</p><p class="ps">Works with Bifrost, LiteLLM, Kong AI, Azure APIM, AWS API Gateway and Apigee.</p>'
              '<hr style="border:0;border-top:2px dashed #a1a1aa;margin:22px 0">'
              '<p class="ph">AI Tests Your Code and Your Running Apps Too</p><div class="g g2">'
              '<div class="card"><b>AI SAST</b>Fix suggestions in the code editor and the build pipeline.<br><span class="btn">AI SAST</span></div>'
              f'<div class="card">{SOON}<b>AI DAST</b>AI plans and runs a pentest of your live app, then checks each finding.<br><span class="btn">AI DAST</span></div></div>'
              '<p class="ps">AI DAST tests applications. <u>AI red teaming</u> tests models and agents.</p>'),
    C("A5", "text", "Change the Shadow AI tab text in the Platform Tour",
      "In the Platform Tour, click the fourth tab, <b>Shadow AI Discovery</b>. Keep its picture. Find the line that starts with <b>Shadow AI Detection</b>.",
      [("delete", "MCP Servers, AI SDKs, AI Gateways, Inference Engines, AI/ML Libraries, and unknown AI assets."),
       ("type", "MCP servers, AI SDKs, AI gateways, inference engines, AI/ML libraries, AI agents and AI automation.")]),
    C("A6", "add", "Add 2 lines to the Key Differentiators list",
      "Scroll to <b>AI Security Key Differentiators</b>. It is a list of 5 lines.",
      [("add", ("Add these 2 lines at the end of the list.",
                "Shadow AI discovery across cloud, browser, host, desktop and CLI agents.<br>AI gateway with a native prompt firewall, coming soon."))],
      shot="A5.png"),
    C("A7", "replace", "Fix 2 wrong FAQ answers and add 2 new FAQs",
      "Scroll to the FAQ list at the bottom of the page. Open questions 26 and 27.",
      [("do", "Open FAQ 26, <b>How does AccuKnox discover unsanctioned AI tools across the enterprise?</b> Replace the whole answer."),
       ("delete", "AccuKnox performs continuous AI asset discovery across endpoints, browsers, SaaS, and cloud environments. It detects shadow AI usage by analyzing outbound traffic, API calls, and browser interactions ..."),
       ("type", "AccuKnox finds unapproved AI on five surfaces. Cloud connectors list AI services in AWS, Azure and GCP. A browser plugin inspects AI chat apps. Host scanning finds AI software on servers and containers. A desktop app shows what desktop AI agents do. A gateway puts CLI coding agents under the Prompt Firewall."),
       ("do", "Delete FAQ 27, <b>Can AccuKnox detect AI integrations embedded in commercial tools ...</b>, question and answer."),
       ("add", ("Add this new FAQ at the end.", "<b>Q:</b> What does the AccuKnox AI Gateway do?<br><b>A:</b> It lists every AI model your teams call, applies rules and rate limits per team, and runs the prompt firewall on every call. It is coming soon.")),
       ("add", ("Add this new FAQ after it.", "<b>Q:</b> Is AI DAST the same as AI red teaming?<br><b>A:</b> No. AI DAST pentests your applications and infrastructure from the outside. AI red teaming tests the AI model or agent itself."))],
      shot="A6.png"),
]
build("update-ai-security.html", "What to Change on the AI Security Page", [SITE + "/platform/ai-security"],
      "Seven changes. Three add new sections. The rest change existing text.", ai)

# ============================================================ 3. PLATFORM
plat = [
    C("P1", "text", "Fix 2 wrong card captions in the AI Security tab",
      "Scroll to <b>Zero Trust Runtime Security for the AI Era</b>. Make sure the <b>AI Security</b> tab is selected. A list of 8 cards shows on the left.",
      [("do", "Find the card <b>AI Detect &amp; Respond (AI DR)</b>. Its small caption ends with broken code."),
       ("delete", "Reconstructs attack chains across prompts and tools/p&gt;"),
       ("type", "Reconstructs attack chains across prompts and tools"),
       ("do", "Find the card <b>AI Red Teaming, Pen Testing</b>. Its caption belongs to a different product."),
       ("delete", "Filters, audits, blocks LLM prompts and responses"),
       ("type", "Runs 150+ adversarial probes on every model change")],
      shot="P1.png"),
    C("P2", "add", "Add 2 new cards to the AI Security tab",
      "Same list of cards as change 1.",
      [("add", ("Add this card at the end of the list.", "<b>Shadow AI Discovery</b><br>Finds unapproved AI on five surfaces")),
       ("add", ("Add this card after it, with a Coming soon tag.", f"<b>AccuKnox AI Gateway</b> {SOON}<br>Routes, governs and firewalls AI model calls"))],
      links=[("Shadow AI Discovery", SITE + "/solutions/shadow-ai-discovery", NEWPAGE),
             ("AccuKnox AI Gateway", SITE + "/platform/ai-security#ai-gateway", "Jumps to a new section on the AI Security page.")],
      preview='<div class="menu"><div class="dim">AI Security Posture (AI-SPM)</div><div class="dim">Agentic AI Security</div><div class="fix">AI Detect &amp; Respond (caption fixed)</div>'
              '<div class="dim">AI Guardrails, Stateful Prompt Firewall</div><div class="fix">AI Red Teaming, Pen Testing (caption fixed)</div>'
              '<div class="dim">AI Identity Security, AI Model Dataset Security, AI GRC</div><div class="new">Shadow AI Discovery</div>'
              f'<div class="new">AccuKnox AI Gateway {SOON}</div></div>'),
    C("P3", "text", "Change the AppSec card in the Application Security tab",
      "Same block as change 1. Click the <b>Application Security</b> tab at the bottom of the block. Find the first card.",
      [("delete", "App Sec (SAST, DAST, SCA)<br>Scans code, dependencies, apps, and Terraform"),
       ("type", "App Sec (AI SAST, AI DAST, SCA)<br>AI fix suggestions in the code editor and an AI-run pentest of the live app")]),
    C("P4", "add", "Add one card to the Data Security tab",
      "Same block as change 1. Click the <b>Data Security</b> tab.",
      [("add", ("Add this card at the end of the list.", "<b>Sensitive Data in AI</b><br>Finds personal data in AI training data and hides it in prompts"))],
      links=[("Sensitive Data in AI", SITE + "/platform/dspm#dspm-for-ai", "Jumps to a new section on the DSPM page.")]),
    C("P5", "text", "Change 2 captions in the 12-module grid and add DSPM",
      "Scroll to <b>12 CNAPP, AppSec, CloudSec, AI-Sec Modules In A Unified Platform</b>.",
      [("do", "Find the tile <b>AI Security (AI-SPM)</b>."),
       ("delete", "Detects prompt injection and model drift, prevents LLM data leakage."),
       ("type", "Finds shadow AI, governs model traffic, stops prompt injection and LLM data leaks."),
       ("do", "Find the tile <b>Application Security Posture Management (ASPM)</b>."),
       ("delete", "Correlates code to cloud to rank vulnerabilities that are reachable."),
       ("type", "Correlates code to cloud. AI SAST and AI DAST find what attackers can reach."),
       ("add", ("Add a new tile to the grid.", "<b>Data Security (DSPM)</b><br>Finds and classifies sensitive data without agents"))],
      shot="P2.png",
      links=[("Data Security (DSPM) tile", SITE + "/platform/dspm", "An existing page.")]),
]
build("update-platform.html", "What to Change on the Platform Page", [SITE + "/platform"],
      "Five changes. All of them are small text edits or new cards.", plat)

# ============================================================ 4. DSPM
dspm = [
    C("D1", "text", "Change the line under the main heading",
      "The very top of the page. The line of text right under the big heading.",
      [("delete", "AI-powered DSPM to discover, classify, and protect sensitive data across public, private, and hybrid clouds."),
       ("type", "Agentless, read-only DSPM that classifies 283 data classes inside the region that holds the data. Only a findings file leaves your account, and the console can run air-gapped.")],
      shot="D1.png"),
    C("D2", "replace", "Replace the breach carousel with 4 privacy points",
      "Scroll to <b>Recent Data Security Incidents</b>, the block with the sliding breach stories on the left.",
      [("do", "Delete the heading, the sentence under it and the whole carousel of breach stories."),
       ("add", ("Put this heading in its place.", "Only a Findings File Leaves Your Account")),
       ("add", ("Under it, add 4 small cards.", "<ol><li><b>Read-only.</b> The scanner cannot change or delete data.</li><li><b>Stays in place.</b> Data is checked on your own server or cluster.</li><li><b>Findings only.</b> One results file per data store leaves, over a secure connection.</li><li><b>Stays in region.</b> Data never moves to another region.</li></ol>"))],
      shot="D2.png",
      preview='<p class="ph">Only a Findings File Leaves Your Account</p><div class="g g4"><div class="card"><b>Read-only</b>The scanner cannot change or delete data.</div>'
              '<div class="card"><b>Stays in place</b>Data is checked on your own server or cluster.</div><div class="card"><b>Findings only</b>One results file per data store leaves.</div>'
              '<div class="card"><b>Stays in region</b>Data never moves to another region.</div></div>'),
    C("D3", "replace", "Replace the 4 big red numbers",
      "Scroll to <b>The Data Security Challenge</b>, the block with 4 big red numbers on the right.",
      [("delete", "85% Don't know where all sensitive data resides · 73% Experienced breach from misconfigured storage · 92% Struggle with manual classification · $10.22M Average cost of a data breach in 2025"),
       ("add", ("Put these 4 numbers in the same 4 tiles.", "<b>283</b> types of sensitive data detected<br><b>159</b> detectors<br><b>62</b> country packs for national ID numbers<br><b>16</b> compliance framework groups")),
       ("add", ("Change the heading to this.", "What AccuKnox DSPM Detects"))],
      shot="D3.png"),
    C("D4", "text", "Change 3 cards in Why Choose AccuKnox",
      "Scroll to <b>Why Choose AccuKnox for Data Security Posture Management</b>. There are 6 cards.",
      [("do", "Card <b>Universal DataSec Coverage</b>:"),
       ("delete", "Support for AWS, Azure, GCP, and 50+ data sources out of the box"),
       ("type", "Object stores, databases and SaaS apps across AWS, Azure and your own servers"),
       ("do", "Card <b>Automated Classification</b>:"),
       ("delete", "99.8% accuracy with AI-powered detection of 50+ sensitive data types"),
       ("type", "High-accuracy classification of 283 types of sensitive data, each with a confidence level"),
       ("do", "Card <b>Compliance Ready</b>:"),
       ("delete", "Pre-built frameworks for GDPR, HIPAA, PCI DSS, SOC 2, and more"),
       ("type", "Mapped to GDPR, HIPAA, PCI DSS, India DPDP Act 2023, SOC 2 and 11 more"),
       ("do", "Remove <b>99.8%</b> from anywhere else it appears on the page.")],
      shot="D4.png"),
    C("D5", "new", "Add a new DSPM for AI section",
      "Scroll to <b>DSPM Capabilities &amp; Use Cases</b>. Add the new section directly below it.",
      [("add", ("Add this heading. Give the section the web address ending <code>#dspm-for-ai</code>.", "Sensitive Data Reaches AI Through Datasets, Prompts and Shadow Tools")),
       ("do", "Under it, add 4 cards, each with a button. The picture below shows the text for each card.")],
      shot="D5.png",
      links=[("AI Model &amp; Dataset (card 1 button)", SITE + "/solutions/ai-model-dataset", "An existing page."),
             ("Prompt Firewall (card 2 button)", SITE + "/solutions/prompt-firewall", "An existing page."),
             ("Shadow AI Discovery (card 3 button)", SITE + "/solutions/shadow-ai-discovery", NEWPAGE),
             ("AI Security (card 4 button)", SITE + "/platform/ai-security#ai-gateway", "Jumps to a new section on the AI Security page.")],
      preview='<p class="ph">Sensitive Data Reaches AI Through Datasets, Prompts and Shadow Tools</p><div class="g g4">'
              '<div class="card"><b>Training data</b>Find personal data in AI training data before training starts.<br><span class="btn">AI Model &amp; Dataset</span></div>'
              '<div class="card"><b>Prompts</b>The Prompt Firewall hides personal data and card numbers before they reach the AI.<br><span class="btn">Prompt Firewall</span></div>'
              '<div class="card"><b>Shadow AI</b>Find the AI tools and agents that could read sensitive data.<br><span class="btn">Shadow AI Discovery</span></div>'
              f'<div class="card">{SOON}<b>AI gateway</b>Control which AI model gets which data, and list every model.<br><span class="btn">AI Security</span></div></div>'),
    C("D6", "text", "Change the bullets in the classification engine block",
      "Scroll to <b>Automated Sensitive Data Classification Engine</b>.",
      [("do", "Delete all 6 bullets in the block."),
       ("add", ("Put these 5 bullets in their place.", "<ul><li>159 detectors</li><li>62 country packs for national ID numbers</li><li>A built-in AI model that finds people's names, running inside your own environment</li><li>Three confidence levels: very likely, likely and possible</li><li>Checks up to 10,000 rows or documents per table</li></ul>"))],
      shot="D6.png"),
    C("D7", "replace", "Replace the 3 icon cards with a table of supported data stores",
      "Scroll to <b>Multi-Cloud Data Security Asset Coverage</b>, the 3 icon cards.",
      [("do", "Delete the 3 icon cards: Cloud Storage, Databases, Virtual Machines."),
       ("add", ("Put this table in their place. Keep the heading.", "The table below, word for word."))],
      shot="D7.png",
      preview='<table class="plain"><thead><tr><th>Type</th><th>AWS</th><th>Azure</th><th>Your own servers</th><th>SaaS</th></tr></thead><tbody>'
              '<tr><td>File storage</td><td>S3</td><td>Blob Storage, ADLS Gen2</td><td>None</td><td>Google Drive</td></tr>'
              '<tr><td>Databases</td><td>RDS and Aurora</td><td>Azure SQL, PostgreSQL, MySQL</td><td>PostgreSQL, MySQL, MariaDB, SQL Server</td><td>None</td></tr>'
              '<tr><td>Document databases</td><td>DocumentDB, DynamoDB</td><td>Cosmos DB</td><td>MongoDB</td><td>None</td></tr>'
              '<tr><td>SaaS apps</td><td>None</td><td>None</td><td>None</td><td>Salesforce</td></tr></tbody></table>'),
    C("D8", "replace", "Replace the comparison table with named competitors",
      "Scroll to <b>AccuKnox DSPM Differentiators</b>. The table compares AccuKnox with unnamed \"Traditional DSPM\" and \"DLP Solutions\".",
      [("do", "Delete the whole table. Keep the heading."),
       ("add", ("Put this table in its place.", "The table below, word for word, with the line under it."))],
      shot="D8.png",
      preview='<table class="plain"><thead><tr><th></th><th>AccuKnox DSPM</th><th>Cyera</th><th>Varonis</th><th>BigID</th><th>IBM Guardium DSPM</th></tr></thead><tbody>'
              '<tr><td>Where scanning runs</td><td>A VM or CronJob you own, in the data&#39;s region</td><td>Cyera&#39;s cloud, or an outpost cluster in your cloud</td><td>Collectors in your environment, analysis in Varonis SaaS</td><td>Cloud scanners, or local scanners in your environment</td><td>An analyzer in your cloud account, per region</td></tr>'
              '<tr><td>Where the console lives</td><td>AccuKnox SaaS, or on-premises or air-gapped</td><td>Cyera SaaS, operated by Cyera</td><td>Varonis SaaS</td><td>BigID SaaS, or self-hosted on your Kubernetes</td><td>IBM SaaS</td></tr>'
              '<tr><td>What leaves your environment</td><td>Nothing with the on-premises console. One findings file per store with SaaS</td><td>Metadata and results</td><td>Metadata from the collectors</td><td>Nothing when self-hosted</td><td>Metadata</td></tr>'
              '<tr><td>Air-gapped operation</td><td>Yes, console included</td><td>No</td><td>Offline collector installs only. Analysis stays in Varonis SaaS</td><td>Possible on your own Kubernetes</td><td>No</td></tr></tbody></table>'
              '<p class="ps">Add this line under the table: Vendor facts come from each vendor&#39;s public documentation as of September 2026.</p>'),
    C("D9", "new", "Add a short India band below the comparison table",
      "Directly below the table from change 8.",
      [("add", ("Add this heading.", "Indian Banks Map DSPM Findings to RBI and DPDP Controls")),
       ("add", ("Add this line under it.", "DPDP Act 2023 mapping covers 17 data types, including Aadhaar, PAN and GST.")),
       ("add", ("Add one button.", "DSPM for Indian Banks"))],
      links=[("DSPM for Indian Banks (button)", SITE + "/solutions/dspm-indian-banks", NEWPAGE)],
      preview='<p class="ph">Indian Banks Map DSPM Findings to RBI and DPDP Controls</p><p class="ps">DPDP Act 2023 mapping covers 17 data types, including Aadhaar, PAN and GST.</p><span class="btn">DSPM for Indian Banks</span>'),
    C("D10", "replace", "Replace the 3 deployment cards",
      "Scroll to <b>Flexible DSPM Deployment Models</b>.",
      [("do", "Delete the 3 cards: Cloud-Native, Kubernetes and Hybrid Infrastructure."),
       ("add", ("Put these 4 cards in their place.", "<ol><li><b>Server with a nightly schedule.</b> The default.</li><li><b>Kubernetes scheduled job.</b> For teams on EKS or AKS.</li><li><b>Event-driven function.</b> Scans new files as they arrive, on AWS Lambda.</li><li><b>Console on premises or air-gapped.</b> Nothing leaves your network.</li></ol>")),
       ("add", ("Below the cards, add 2 text links.", "Read the DSPM overview<br>Read the DSPM setup guide"))],
      shot="D9.png",
      links=[("Read the DSPM overview", "https://help.accuknox.com/getting-started/dspm-overview/", "Help docs page, live today."),
             ("Read the DSPM setup guide", "https://help.accuknox.com/getting-started/dspm-onboarding/", "Help docs page, live today.")]),
]
build("update-platform-dspm.html", "What to Change on the DSPM Page", [SITE + "/platform/dspm"],
      "Ten changes. Most swap old numbers for the numbers in the new DSPM help docs. Two add new sections.", dspm)

# ============================================================ 5. APPSEC
app = [
    C("S1", "new", "SAST page: add a new AI SAST section",
      f"Open <a href=\"{SITE}/solutions/sast\">{SITE}/solutions/sast</a>. Add the new section directly below the top banner.",
      [("add", ("Add this heading. Give the section the web address ending <code>#ai-sast</code>.", "AI SAST Suggests the Fix in Your IDE and Pipeline")),
       ("do", "Under it, add 3 cards. The picture below shows the text.")],
      shot="S1.png",
      preview='<p class="ph">AI SAST Suggests the Fix in Your IDE and Pipeline</p><div class="g g3">'
              '<div class="card"><b>Fewer false alarms</b>AI marks likely false positives and rates how serious each finding is.</div>'
              '<div class="card"><b>One switch</b>Pick "AI Enabled SAST" when you start a scan.</div>'
              f'<div class="card">{SOON}<b>In your code editor</b>Plugins for your code editor, and AI notes on every pull request.</div></div>',
      ask="Which code editors (IDEs) to name in card 3."),
    C("S2", "add", "SAST page: add to one FAQ and add one new FAQ",
      "Same page. Scroll to the FAQ list at the bottom.",
      [("do", "Open FAQ 6, <b>How can organizations address the potential for false positives in SAST results?</b>"),
       ("add", ("Add this sentence at the end of the answer.", "AccuKnox AI SAST marks likely false positives on each finding.")),
       ("add", ("Add this new FAQ at the end of the list.", "<b>Q:</b> What does the AI do in AccuKnox SAST?<br><b>A:</b> It reviews each finding, marks likely false positives and rates how serious the finding is."))],
      shot="S2.png"),
    C("T1", "new", "DAST page: add a new AI DAST section",
      f"Open <a href=\"{SITE}/solutions/dast\">{SITE}/solutions/dast</a>. Add the new section directly below the top banner.",
      [("add", ("Add this heading with a Coming soon tag. Give the section the web address ending <code>#ai-dast</code>.", f"AI DAST Plans and Runs the Pentest, Then Checks Each Finding {SOON}")),
       ("do", "Under it, add 6 cards and one line. The picture below shows the text.")],
      shot="T1.png",
      links=[("AI Red Teaming (in the line under the cards)", SITE + "/solutions/ai-red-teaming", "An existing page.")],
      preview=f'<p class="ph">AI DAST Plans and Runs the Pentest, Then Checks Each Finding {SOON}</p><div class="g g3">'
              '<div class="card"><b>One field to start</b>Enter the web address of your app.</div><div class="card"><b>Three scan depths</b>Quick, standard and in-depth.</div>'
              '<div class="card"><b>Tests behind logins</b>Username and password, one-time codes, email codes and magic links.</div>'
              '<div class="card"><b>Points to the code</b>Link your code repository and each finding shows the line to fix.</div>'
              '<div class="card"><b>Finds forgotten pages</b>Upload your API file and old endpoints get tested too.</div>'
              '<div class="card"><b>Your choice of AI model</b>Use ours, your own model key, or a model on your own servers.</div></div>'
              '<p class="ps">AI DAST tests applications. For testing AI models and agents, see <u>AI Red Teaming</u>.</p>'),
    C("T2", "add", "DAST page: add one sentence",
      "Same page. Scroll to <b>Aggregate Your DAST tools in One Dashboard</b>.",
      [("add", ("Add this sentence at the end of the paragraph.", "AI DAST findings show up in the same dashboard as SAST, SCA and IaC findings."))],
      shot="T2.png"),
    C("M1", "text", "ASPM page: rename 2 tabs",
      f"Open <a href=\"{SITE}/platform/aspm\">{SITE}/platform/aspm</a>. Scroll to <b>Prioritize &amp; Automate Security in Code &amp; Pipeline</b>. It has a row of tabs.",
      [("delete", "Static Application Security Testing (SAST)"),
       ("type", "AI SAST"),
       ("delete", "Dynamic Application Security Testing (DAST)"),
       ("type", f"AI DAST {SOON}"),
       ("do", "In each renamed tab, add the first card text from change 1 or change 3 on this page.")],
      shot="M1.png"),
    C("M2", "new", "ASPM page: add a band with 2 cards",
      "Same page. Scroll to the webinar block <b>Is Application Security an Afterthought in the AI Era?</b> Add the band directly below it.",
      [("do", "Add 2 cards side by side and one line under them. The picture below shows the text.")],
      shot="M2.png",
      links=[("AI SAST (card 1)", SITE + "/solutions/sast#ai-sast", "Jumps to the new section from change 1."),
             ("AI DAST (card 2)", SITE + "/solutions/dast#ai-dast", "Jumps to the new section from change 3.")],
      preview='<div class="g g2"><div class="card"><b>AI SAST</b>Fix suggestions in the code editor and the build pipeline.</div>'
              f'<div class="card">{SOON}<b>AI DAST</b>AI plans and runs a pentest of your live app, then checks each finding.</div></div>'
              '<p class="ps">AI SAST and AI DAST cover the whole AppSec cycle, from the code editor to a pentest of the live app.</p>'),
]
build("update-sast-dast-aspm.html", "What to Change on the SAST, DAST and ASPM Pages",
      [SITE + "/solutions/sast", SITE + "/solutions/dast", SITE + "/platform/aspm"],
      "Six changes across three pages. Each change starts with the page to open.", app)

# ============================================================ INDEX
cards = "".join(f'<a href="{f}"><b>{i}. {e(t)}</b><span>{n} changes</span></a>'
                for i, ((f, _, t), n) in enumerate(zip(PAGES, [len(menu), len(ai), len(plat), len(dspm), len(app)]), 1))
cards += ('<a href="new-page-shadow-ai-discovery.html"><b>New page: Shadow AI Discovery</b><span>Build from scratch. Address: /solutions/shadow-ai-discovery</span></a>'
          '<a href="new-page-dspm-indian-banks.html"><b>New page: DSPM for Indian Banks</b><span>Build from scratch. Address: /solutions/dspm-indian-banks</span></a>'
          '<a href="new-page-ciem.html"><b>New page: CIEM</b><span>Build from scratch. Address: /platform/ciem</span></a>')
rules = """<table class="plain"><thead><tr><th>When you see</th><th>Do this</th></tr></thead><tbody>
<tr><td>A number of AI assets</td><td>Write <b>4K+</b>. Never the exact number.</td></tr>
<tr><td>AccuKnox AI Gateway, AI DAST, AI SAST in the code editor</td><td>Add a small <b>Coming soon</b> tag.</td></tr>
<tr><td>macOS scanning, desktop app</td><td>Label them <b>Beta</b>, with the one-line key that explains Beta.</td></tr>
<tr><td>DSPM</td><td>Never add a BETA tag.</td></tr>
<tr><td>99.8% accuracy</td><td>Remove it. Write "high-accuracy" instead.</td></tr>
</tbody></table>"""
index = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Website Changes, Start Here</title><style>{CSS}</style></head><body>{topnav("index.html")}
<header class="wrap"><h1>Website Changes for AI Security, AppSec and DSPM</h1>
<p class="sub">Five existing pages need changes, and two pages are new. Open one file at a time. Each file lists its changes in order, shows where each one goes on the live page, and gives the exact text and links.</p></header>
<main class="wrap"><h2>Open These Files in Order</h2><div class="files">{cards}</div>
<h2>Five Rules for Every Page</h2>{rules}
<h2>Where Everything Goes</h2><figure>{img("../nav-and-pages.png", width=1560, alt="Map of menu changes, updated pages and new pages")}
<figcaption>Left: the menu items. Middle: the pages that change. Right: the 2 new pages. Green is new, amber is changed text, purple is a broken link, blue is a moved menu item.</figcaption></figure></main>
<footer><div class="wrap">Questions: ask Atharva.</div></footer></body></html>"""
(OUT / "index.html").write_text(index, encoding="utf-8")
for f in ["index.html"] + [p for p, _, _ in PAGES]:
    print(f, round((OUT / f).stat().st_size / 1024), "KB")

"""Build new-page-ciem.html, a low-fidelity landing page for AccuKnox CIEM.

Every product fact comes from docs/getting-started/ciem-overview.md and ciem-onboarding.md on main.
All 14 CIEM screenshots from the help docs are embedded as WebP data URIs.
"""
import base64, io, pathlib
from PIL import Image

HERE = pathlib.Path(__file__).parent
IMGS = HERE / "ciem-images"
OUT = HERE.parent / "Prototype HTMLs" / "new-page-ciem.html"
DOCS = "https://help.accuknox.com/getting-started"


def shot(name, alt, cap=None, w=1400):
    im = Image.open(IMGS / name).convert("RGB")
    if im.width > w:
        im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "WEBP", quality=80, method=6)
    src = "data:image/webp;base64," + base64.b64encode(buf.getvalue()).decode()
    c = f"<figcaption>{cap}</figcaption>" if cap else ""
    return f'<figure><img src="{src}" alt="{alt}" loading="lazy">{c}</figure>'


CSS = """
:root{
  --paper:oklch(0.985 0.004 95);--paper-2:oklch(0.955 0.006 95);--ink:oklch(0.23 0.012 260);
  --mute:oklch(0.46 0.012 260);--line:oklch(0.86 0.008 95);--accent:oklch(0.46 0.09 165);
  --accent-soft:oklch(0.95 0.03 165);--note:oklch(0.96 0.05 95)}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--paper);color:var(--ink);font:17px/1.6 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
a{color:var(--accent)}
:focus-visible{outline:3px solid var(--accent);outline-offset:3px}
.wrap{max-width:1160px;margin:0 auto;padding:0 20px}
.bar{background:var(--ink);color:var(--paper);font-size:13px}
.bar .wrap{display:flex;gap:10px 18px;flex-wrap:wrap;justify-content:space-between;padding-top:9px;padding-bottom:9px}
.bar a{color:var(--paper)}
.bar label{display:flex;gap:6px;align-items:center;cursor:pointer}
header.site .wrap{display:flex;justify-content:space-between;align-items:center;gap:14px;padding-top:16px;padding-bottom:16px;border-bottom:1px solid var(--line);flex-wrap:wrap}
.logo{font-weight:800;letter-spacing:.05em}
nav.top ul{display:flex;gap:18px;list-style:none;margin:0;padding:0;font-size:14px;flex-wrap:wrap}
.btn{display:inline-block;padding:11px 20px;border-radius:6px;font-weight:700;text-decoration:none;border:2px solid var(--ink);color:var(--ink);background:transparent}
.btn.primary{background:var(--ink);color:var(--paper)}
.soon{display:inline-block;font-size:12px;font-weight:800;letter-spacing:.06em;text-transform:uppercase;border:1.5px dashed var(--ink);border-radius:99px;padding:2px 10px;vertical-align:middle}
.hero{padding:64px 0 28px}
.eyebrow{font-size:13px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--accent);display:flex;gap:12px;align-items:center;flex-wrap:wrap}
h1{font-size:clamp(34px,5.4vw,62px);line-height:1.04;letter-spacing:-.02em;margin:16px 0 18px;max-width:15ch}
.lead{font-size:clamp(18px,1.6vw,21px);color:var(--mute);max-width:58ch;margin:0}
.ctas{display:flex;gap:12px;flex-wrap:wrap;margin:28px 0 0}
.hero figure{margin-top:44px}
figure{margin:0}
figure img{width:100%;height:auto;display:block;border-radius:8px;border:1px solid var(--line);background:var(--paper-2)}
figcaption{font-size:14px;color:var(--mute);margin-top:8px}
.facts{display:flex;flex-wrap:wrap;gap:8px 34px;padding:22px 0;margin:40px 0 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line);font-size:16px}
.facts b{font-size:22px;margin-right:6px}
section.ch{padding:88px 0 0}
.ch .num{font-size:14px;font-weight:800;color:var(--accent);letter-spacing:.08em}
h2{font-size:clamp(26px,3.2vw,38px);line-height:1.12;letter-spacing:-.01em;margin:8px 0 14px;max-width:22ch}
.split{display:grid;grid-template-columns:minmax(0,5fr) minmax(0,7fr);gap:44px;align-items:start}
.split.flip{grid-template-columns:minmax(0,7fr) minmax(0,5fr)}
.split.flip .txt{order:2}
.txt p{margin:0 0 14px;max-width:52ch}
.txt ul{margin:6px 0 0;padding-left:20px;max-width:52ch}
.txt li{margin:0 0 8px}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0 0;padding:0;list-style:none}
.chips li{font-size:14px;padding:4px 11px;border-radius:99px;background:var(--accent-soft);color:oklch(0.3 0.07 165);margin:0}
.pair{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:22px;margin-top:26px}
.steps{list-style:none;margin:26px 0 0;padding:0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:26px;counter-reset:s}
.steps li{counter-increment:s}
.steps li::before{content:counter(s);display:inline-flex;width:34px;height:34px;border-radius:50%;background:var(--ink);color:var(--paper);font-weight:800;align-items:center;justify-content:center;margin-bottom:10px}
.steps h3{font-size:18px;margin:0 0 6px}
.steps p{margin:0 0 12px;color:var(--mute);font-size:15.5px}
.confirm{margin-top:34px;display:grid;grid-template-columns:minmax(0,7fr) minmax(0,5fr);gap:22px;align-items:start}
code{background:var(--paper-2);border:1px solid var(--line);border-radius:4px;padding:1px 6px;font-size:.9em}
.limits{margin-top:88px;padding:26px 28px;background:var(--paper-2);border-radius:10px}
.limits h2{font-size:24px;margin-top:0}
.limits ul{margin:0;padding-left:20px}
.limits li{margin:0 0 8px}
.docs{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:18px;margin-top:22px}
.doc{display:block;text-decoration:none;color:var(--ink);border:1.5px solid var(--ink);border-radius:10px;padding:24px 26px;background:var(--paper)}
.doc:hover{background:var(--accent-soft)}
.doc .k{font-size:12px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--accent)}
.doc h3{font-size:22px;margin:6px 0 8px}
.doc p{margin:0 0 14px;color:var(--mute)}
.doc .go{font-weight:700;color:var(--accent)}
details{border-bottom:1px solid var(--line);padding:16px 0}
summary{cursor:pointer;font-weight:700;font-size:18px}
details p{margin:10px 0 0;color:var(--mute);max-width:65ch}
.cta{margin:88px 0 0;padding:56px 0;text-align:center;border-top:1px solid var(--line)}
.cta h2{margin-left:auto;margin-right:auto}
.cta .ctas{justify-content:center}
.note{background:var(--note);border:1px solid oklch(0.8 0.1 95);border-radius:6px;padding:9px 12px;font-size:14px;margin:14px 0 0;max-width:70ch}
body.hide-notes .note{display:none}
footer{padding:26px 0 40px;font-size:13px;color:var(--mute)}
@media (max-width:860px){
  .split,.split.flip,.pair,.steps,.confirm,.docs{grid-template-columns:1fr}
  .split.flip .txt{order:0}
  section.ch{padding-top:60px}
  .hero{padding-top:40px}
}
"""

page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>AccuKnox CIEM Wireframe</title>
<style>{CSS}</style>
</head>
<body class="hide-notes">
<div class="bar"><div class="wrap">
  <span><a href="index.html">Back to start</a> · <b>Wireframe</b> · accuknox.com/platform/ciem</span>
  <label><input type="checkbox" id="notes"> Show designer notes</label>
</div></div>

<header class="site"><div class="wrap">
  <span class="logo">ACCUKNOX</span>
  <nav class="top" aria-label="Site"><ul><li><b>Platform</b></li><li>Solutions</li><li>Case Studies</li><li>Partners</li><li>Resources</li><li>About</li></ul></nav>
  <a class="btn" href="#demo">Contact us</a>
</div></header>

<main>
<section class="hero"><div class="wrap">
  <div class="eyebrow">Cloud Infrastructure Entitlement Management (CIEM) <span class="soon">Coming soon</span></div>
  <h1>See Who Can Do What in Your Cloud</h1>
  <p class="lead">AccuKnox CIEM lists every user, group and role in your AWS, GCP, Azure and Oracle Cloud accounts. It shows the policies behind each identity and draws the access chain as a graph.</p>
  <div class="ctas"><a class="btn primary" href="#demo">Book a demo</a><a class="btn" href="{DOCS}/ciem-overview/">Read the CIEM overview</a></div>
  <p class="note"><b>Designer note.</b> The H1 answers the question every CIEM page leads with: who can access what. Keep "Coming soon" next to the eyebrow until CIEM ships.</p>
  {shot("ciem-org-graph.png", "The CIEM organization graph for one AWS account, with the account at the top and user, group, role and policy nodes expanded to show their members", "The organization graph puts one cloud account at the top. Select any node to open its members.")}
  <div class="facts">
    <span><b>4</b>clouds: AWS, GCP, Azure and OCI</span>
    <span><b>3</b>identity types: users, groups and roles</span>
    <span><b>2</b>classes: human and machine</span>
    <span><b>1</b>toggle, on by default at onboarding</span>
  </div>
</div></section>

<section class="ch" id="list"><div class="wrap split">
  <div class="txt">
    <div class="num">01</div>
    <h2>Every Identity Sits in One List</h2>
    <p>Open <b>Identities &gt; CIEM</b> to see the users, groups and roles from every onboarded cloud account.</p>
    <p>CIEM marks each identity as human or machine. A CI/CD pipeline account counts as a machine identity.</p>
    <ul>
      <li>Filter by cloud, identity type, name and date range.</li>
      <li>Read the cloud ID in one column: an ARN on AWS, a service account ID on GCP, an OCID on OCI.</li>
    </ul>
  </div>
  <div>
    {shot("ciem-identity-list.png", "The CIEM identity list filtered to AWS, with identity, resource identifier, risk class, cloud account and classification columns")}
  </div>
</div>
<div class="wrap" style="margin-top:22px">
  {shot("ciem-identity-list-all.png", "The CIEM identity list with the Cloud Providers filter open on AWS, GCP, Azure and Oracle", "One filter switches the list between AWS, GCP, Azure and Oracle.")}
</div></section>

<section class="ch" id="unused"><div class="wrap split flip">
  <div class="txt">
    <div class="num">02</div>
    <h2>Stale Access Shows Up in the Lifecycle Columns</h2>
    <p>Scroll the list right. Each identity shows its age, who created it and when it last acted.</p>
    <ul class="chips"><li>Age In Days</li><li>Created By</li><li>Last Used</li><li>Days Since Last Used</li></ul>
    <p style="margin-top:16px">A high <b>Days Since Last Used</b> value marks a role nobody touched in months.</p>
  </div>
  <div>
    {shot("ciem-identity-list-columns.png", "The CIEM identity list scrolled right, with the Age In Days, Identity Created At, Created By, Last Used and Days Since Last Used columns")}
  </div>
</div></section>

<section class="ch" id="trace"><div class="wrap split">
  <div class="txt">
    <div class="num">03</div>
    <h2>The Access Graph Shows How an Identity Got Its Access</h2>
    <p>Select an identity. The graph reads top to bottom: the identity, its groups, then the policies each group grants.</p>
    <p>The Overview tab lists every attached policy and opens the policy document as JSON. CIEM tags each identity with the risk classes its policies carry.</p>
    <ul class="chips"><li>Privilege Escalation</li><li>Data Exfiltration</li><li>Credentials Exposure</li><li>Infrastructure Modification</li></ul>
  </div>
  <div>
    {shot("ciem-identity-graph.png", "The access graph of one AWS user, with its groups in the middle and the policies each group grants at the bottom")}
  </div>
</div>
<div class="wrap" style="margin-top:22px">
  {shot("ciem-identity-overview.png", "The Overview tab of an AWS user, with identity details, findings by severity and the attached policy table expanded to an inline policy", "The Overview tab counts findings by severity and names each policy as cloud managed, inline or user managed.")}
</div></section>

<section class="ch" id="account"><div class="wrap split flip">
  <div class="txt">
    <div class="num">04</div>
    <h2>One Graph Counts Every Identity in an Account</h2>
    <p>Switch to the graph view. Each node shows a count, so you see the size of an account's identity footprint at a glance.</p>
    <p>In the sample AWS account, the badges read 77 users, 22 groups, 637 roles and 504 policies.</p>
  </div>
  <div>
    {shot("ciem-account-graph.png", "The CIEM graph of an AWS account, with count badges for 77 users, 22 groups, 637 roles and 504 policies")}
  </div>
</div>
<div class="wrap pair">
  {shot("ciem-related-identities.png", "The Related Identities tab, with each identity's resource ID, cloud provider, findings by severity and risk class", "Related Identities lists the rest of the account, with findings for each one.")}
  {shot("ciem-raw-information.png", "The Raw Information tab of an AWS user, showing the identity record as JSON", "Raw Information holds the full identity record as JSON, ready to copy.")}
</div></section>

<section class="ch" id="onboard"><div class="wrap">
  <div class="num">05</div>
  <h2>Turn On CIEM While You Onboard a Cloud Account</h2>
  <p style="max-width:60ch;margin:0">CIEM is part of the normal cloud account onboarding. The CIEM toggle is on by default.</p>
  <ol class="steps">
    <li><h3>Pick the cloud</h3><p>Go to <b>Settings &gt; Cloud Accounts &gt; Onboard Account</b>. Choose the provider and <b>Standalone Account</b>.</p>
      {shot("ciem-onboard-provider.png", "Step 1 of 3, with Amazon Web Service and Standalone Account selected")}</li>
    <li><h3>Keep CIEM on</h3><p>In <b>Configure Scanning</b>, leave the CIEM toggle on and select <b>Next</b>.</p>
      {shot("ciem-onboard-toggle.png", "Step 2 of 3, Configure Scanning, with the CIEM toggle turned on")}</li>
    <li><h3>Connect the account</h3><p>On AWS, run the Terraform script, then paste the keys it creates.</p>
      {shot("ciem-onboard-terraform.png", "Step 3 of 3 for AWS, with the Terraform steps and the access key fields")}</li>
  </ol>
  <div class="confirm">
    {shot("ciem-cloud-accounts.png", "The Cloud Accounts list with AWS, Oracle, GCP and Azure accounts, each with CIEM Active", "The CIEM column reads Active for each onboarded account.")}
    {shot("ciem-nav-identities.png", "The left navigation open on Identities, with the CIEM and KIEM entries", "CIEM sits under Identities, next to KIEM for Kubernetes identities.")}
  </div>
</div></section>

<div class="wrap">
  <section class="limits" aria-labelledby="h-lim">
    <h2 id="h-lim">Two Limits Apply at Launch</h2>
    <ul>
      <li>CIEM supports standalone cloud accounts. Organization accounts are not supported yet.</li>
      <li>CIEM covers cloud identities. For Kubernetes service accounts and roles, use <a href="https://help.accuknox.com/use-cases/kiem/">KIEM</a>.</li>
    </ul>
  </section>

  <section class="ch" id="docs" style="padding-top:72px">
    <h2>Read the CIEM Guides</h2>
    <div class="docs">
      <a class="doc" href="{DOCS}/ciem-overview/"><span class="k">Overview</span><h3>What CIEM Shows</h3><p>The identity list, the four identity tabs, the policy types and both graphs.</p><span class="go">Open the overview</span></a>
      <a class="doc" href="{DOCS}/ciem-onboarding/"><span class="k">Onboarding</span><h3>Turn On CIEM for a Cloud Account</h3><p>The three onboarding steps, the AWS Terraform step and how to confirm CIEM is active.</p><span class="go">Open the onboarding guide</span></a>
    </div>
  </section>

  <section class="ch" id="faq" style="padding-top:72px">
    <h2>CIEM Questions</h2>
    <details><summary>Which clouds does AccuKnox CIEM cover?</summary><p>AWS, GCP, Azure and Oracle Cloud Infrastructure.</p></details>
    <details><summary>What counts as a machine identity?</summary><p>An identity that software uses, such as a CI/CD pipeline account. CIEM marks every identity as human or machine.</p></details>
    <details><summary>Where does the risk class come from?</summary><p>CIEM calculates it from the policies attached to the identity. Examples are Privilege Escalation and Data Exfiltration.</p></details>
    <details><summary>Does CIEM support AWS Organizations?</summary><p>Not yet. CIEM supports standalone cloud accounts today.</p></details>
    <details><summary>How do I turn it on?</summary><p>Leave the CIEM toggle on when you onboard a cloud account. The <a href="{DOCS}/ciem-onboarding/">onboarding guide</a> has the steps.</p></details>
  </section>
</div>

<section class="cta" id="demo"><div class="wrap">
  <h2>See Every Identity in Your Cloud Accounts</h2>
  <p class="lead" style="margin:0 auto">Turn on CIEM when you onboard a cloud account, then open Identities &gt; CIEM.</p>
  <div class="ctas"><a class="btn primary" href="#">Book a demo</a><a class="btn" href="{DOCS}/ciem-onboarding/">Read the onboarding guide</a></div>
</div></section>
</main>

<footer><div class="wrap">Wireframe for review. Screenshots come from the AccuKnox help docs, with emails, account IDs and OCIDs masked.</div></footer>
<script>document.getElementById('notes').addEventListener('change',e=>document.body.classList.toggle('hide-notes',!e.target.checked));</script>
</body>
</html>
"""
OUT.write_text(page, encoding="utf-8")
print(OUT.name, round(OUT.stat().st_size / 1024), "KB")

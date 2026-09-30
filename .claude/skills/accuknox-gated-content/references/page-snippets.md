# Page snippets

Paste these into `report.html` in place of the `<!-- PAGES -->` marker. Every `{{ }}` token is a slot, and `check.py` fails the build while one remains.


Cover

```html
<section class="page bg-navy">
  <svg class="art" style="right:-40mm;top:-30mm;width:190mm;height:190mm" viewBox="0 0 200 200">
    <defs><linearGradient id="gc" x1="0" x2="1"><stop offset="0" stop-color="#FF4646"/><stop offset="1" stop-color="#1040C5"/></linearGradient></defs>
    <g fill="none" stroke="url(#gc)" stroke-width=".5"><circle cx="100" cy="100" r="30"/><circle cx="100" cy="100" r="50"/><circle cx="100" cy="100" r="70"/><circle cx="100" cy="100" r="90" stroke-dasharray="2 3"/></g>
    <circle cx="100" cy="100" r="6" fill="#1040C5"/><circle cx="150" cy="45" r="3" fill="#FF4646"/><circle cx="36" cy="140" r="2.5" fill="#4F9CF9"/>
  </svg>
  <div style="position:absolute;left:17mm;right:17mm;bottom:30mm">
    <img src="logo.png" class="logo-white" style="height:8mm;margin-bottom:12mm">
    <div class="caps" style="color:var(--ak-sky);margin-bottom:5mm">{{EYEBROW}}</div>
    <h1 class="h-display">{{TITLE LINE 1}}<br>{{WORDS}} <span class="ul">{{KEY PHRASE}}</span></h1>
    <p class="deck" style="color:rgba(255,255,255,.7);font-size:20pt">{{SUBTITLE}}</p>
  </div>
</section>
```

Methodology stats

```html
<section class="page bg-white">
  <h1 class="h1" style="margin-top:6mm">Methodology</h1>
  <p class="lede" style="margin-top:4mm;color:var(--ink-3)">{{ONE LINE ON DATA SOURCES}}</p>
  <div class="push-right stack" style="--gap:7mm;margin-top:14mm">
    <div class="panel"><div class="stat">{{N1}}</div><p class="body" style="margin-top:3mm">{{LABEL 1}}</p></div>
    <div class="panel"><div style="display:flex;align-items:baseline;gap:4mm"><span class="body">and</span><span class="stat">{{N2}}</span></div><p class="body" style="margin-top:3mm">{{LABEL 2}}</p></div>
    <div class="panel navy"><div style="display:flex;align-items:baseline;gap:4mm"><span class="body" style="color:#fff">with</span><span class="stat">{{N3}}</span></div><p class="body" style="margin-top:3mm;color:rgba(255,255,255,.8)">{{LABEL 3}}</p></div>
  </div>
  <div class="foot"><img class="logo" src="logo.png"><span class="src">Source: <a>{{SOURCE}}</a></span></div>
</section>
```

Table of contents item (repeat)

```html
<div class="item"><div><span class="chip">Section 01</span><div class="t">{{SECTION TITLE}}</div></div><div class="p">{{PAGE}}</div></div>
```

Section divider

```html
<section class="page bg-navy">
  <svg class="art" style="left:0;bottom:0;width:210mm;height:150mm" viewBox="0 0 210 150" preserveAspectRatio="none">
    <defs><linearGradient id="gd" x1="0" x2="1"><stop offset="0" stop-color="#FF4646"/><stop offset="1" stop-color="#1040C5"/></linearGradient></defs>
    <g fill="none" stroke="url(#gd)" stroke-width=".35"><path d="M0 140 C60 60 120 150 210 40"/><path d="M0 130 C60 50 120 140 210 30" opacity=".7"/><path d="M0 120 C60 40 120 130 210 20" opacity=".5"/><path d="M0 110 C60 30 120 120 210 10" opacity=".3"/></g>
  </svg>
  <img src="logo.png" class="logo-white" style="height:6.5mm">
  <div style="margin-top:45mm"><span class="chip">Section 0X</span>
    <h1 class="h-display">{{SECTION TITLE}}</h1>
    <p class="deck" style="color:rgba(255,255,255,.65)">{{DECK}}</p></div>
</section>
```

Numbered findings row (repeat inside `<div class="nlist">`)

```html
<div class="row"><div class="num-ghost">01</div><div>
  <svg class="icon" viewBox="0 0 48 48" fill="none" stroke="#4F9CF9" stroke-width="1.6" stroke-linecap="round"><path d="M24 5l15 6v11c0 10-7 17-15 21C16 39 9 32 9 22V11z"/><path d="M17 24l5 5 9-10"/></svg>
  <p class="body">{{FINDING, 2 TO 3 LINES}}</p></div></div>
```

Big-number table

```html
<table class="ntable">
  <tr><th>Metric</th><th>{{PERIOD A}}</th><th>{{PERIOD B}}</th></tr>
  <tr><td class="lbl">{{METRIC}}</td><td class="v">{{VALUE}}</td><td class="v">{{VALUE}}<small>({{NOTE}})</small></td></tr>
</table>
```

Hero stat

```html
<section class="page bg-blue">
  <span class="chip">A.</span>
  <h1 class="h1">{{TITLE}}</h1>
  <p class="deck">{{DECK}}</p>
  <div class="panel" style="margin-top:30mm;padding:14mm 12mm 12mm;text-align:center">
    <div class="stat" style="font-size:130pt;color:var(--ak-blue)">{{NUMBER}}<span style="font-size:.5em"> {{UNIT}}</span></div>
    <p class="body" style="margin-top:4mm;font-weight:600;color:var(--ink)">{{WHAT THE NUMBER MEASURES}}</p>
  </div>
  <div class="foot"><img class="logo" src="logo.png"><span class="folio">{{N}}</span></div>
</section>
```

Bar chart row (repeat inside a `.panel .stack`)

```html
<div style="display:grid;grid-template-columns:40mm 1fr 16mm;align-items:center;gap:4mm">
  <span class="body">{{LABEL}}</span><div class="bar" style="width:{{PCT}}%"></div><span class="stat-s" style="font-size:20pt">{{VALUE}}</span></div>
```

Product spotlight

```html
<section class="page bg-rose">
  <svg class="art" style="right:0;top:0;width:210mm;height:170mm" viewBox="0 0 210 170" preserveAspectRatio="none"><polygon points="210,0 210,170 60,0" fill="#FFE3E3"/></svg>
  <img src="logo.png" style="height:7mm;position:relative">
  <div style="position:relative;margin-top:62mm">
    <div class="caps" style="color:var(--ink-3)">AccuKnox capability spotlight</div>
    <h1 class="h1" style="color:var(--ak-red);margin:4mm 0 10mm">{{CAPABILITY}}</h1>
    <div class="cols-3 body"><div>{{COL 1}}</div><div>{{COL 2}}</div><div>{{COL 3}}</div></div>
  </div>
  <div class="foot"><span class="src" style="color:var(--ink)">See how it works → <a>{{URL WITHOUT https}}</a></span><span class="folio">{{N}}</span></div>
</section>
```

Closing CTA

```html
<section class="page bg-navy">
  <img src="logo.png" class="logo-white" style="height:7mm">
  <div class="bottom">
    <hr class="rule-grad" style="margin-bottom:8mm">
    <h1 class="h1">{{CTA HEADLINE}}</h1>
    <p class="deck" style="color:rgba(255,255,255,.7);margin-bottom:12mm">{{CTA SUPPORT LINE}}</p>
    <a class="cta" href="{{URL WITH UTM}}">{{PRIMARY CTA}}</a>&nbsp;&nbsp;<a class="cta ghost" href="{{URL WITH UTM}}">{{SECONDARY CTA}}</a>
    <p class="meta" style="color:rgba(255,255,255,.5);margin-top:16mm">accuknox.com · © {{YEAR}} AccuKnox, Inc.</p>
  </div>
</section>
```

## Product screenshot

Use a real AccuKnox screen from `img/`, found with `find_images.py` or `site_assets.py`. One screenshot per page, sized to leave a third of the page empty. The caption names the screen and links the help page or site page it came from.

```html
<section class="page bg-ice">
  <span class="chip">Section 0X</span>
  <h1 class="h1">{{TITLE WITH <span class="hl">KEY WORDS</span>}}</h1>
  <p class="deck">{{DECK}}</p>
  <figure class="shot" style="margin-top:14mm">
    <img src="img/{{FILE}}" alt="{{WHAT THE SCREEN SHOWS}}">
  </figure>
  <p class="shot-cap">{{SCREEN NAME}}. Details at <a href="{{HELP OR SITE URL}}">{{URL WITHOUT https}}</a></p>
  <div class="foot"><img class="logo" src="logo.png"><span class="folio">{{N}}</span></div>
</section>
```

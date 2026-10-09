# AccuKnox layout catalog

Pick a layout per slide from this list. Every snippet assumes `const ak = require(".../scripts/ak.js")` and runs inside an async function. Coordinates are inches on a 13.33 by 7.5 slide. Content lives between `slide.top` (1.75 or 2.15) and `ak.CONTENT_BOTTOM` (6.7).

## Contents

1. Cover
2. Agenda
3. Card grid (icons, numbers, stats)
4. Incident or proof cards with callout
5. Stat row
6. Table
7. Split: statement left, steps or visual right
8. Steps and timelines
9. Two column compare (we give, we get / before, after)
10. Logo wall
11. Image or diagram slide
12. Section divider
13. Closing CTA
14. Charts

---

## 1. Cover

Dark, logo top left, topic artwork right, proof badges bottom left.

```javascript
ak.coverSlide(pres, {
  eyebrow: "Partner program · October 2026",
  title: "Partnership Program",          // 2 lines max at 54pt, about 22 characters per line
  subtitle: "Co-sell with AccuKnox",
  tagline: "Zero Trust CNAPP for cloud, AI and runtime security.",
  image: await ak.coverArt("network"),   // ai | cloud | code | compliance | runtime | network, or topic text
  // badges: false,                       // hide G2 and marketplace badges
});
```

## 2. Agenda

Numbered cards. 3 to 6 items. Keep each description to one short line.

```javascript
const s = ak.contentSlide(pres, { eyebrow: "Agenda", title: "What we will cover" });
await ak.cardGrid(s, [
  { num: "01", title: "About AccuKnox", body: "Team and analyst recognition" },
  { num: "02", title: "Security platform", body: "Twelve modules, code to cognition" },
  // ...
], { cols: 3 });
```

For 7 or more agenda items use `ak.steps` in two columns instead of cards.

## 3. Card grid

The workhorse. Each item can carry `num`, `icon`, `stat`, `label`, `title`, `body` or `bullets`, and `accent` ("gradient" default, "blue", "red", "ink", "none").

```javascript
const s = ak.contentSlide(pres, { eyebrow: "02  Security platform play", title: "AI security modules",
  subtitle: "Pick the modules you need. All public clouds, all private clouds." });
await ak.cardGrid(s, [
  { icon: "tb:TbShieldLock", label: "AI-SPM", title: "AI posture management",
    bullets: ["Discover models and agents", "Map risky data paths", "Track AI compliance"] },
  { icon: "tb:TbRadar", label: "AI-DR", title: "AI detection and response",
    bullets: ["Runtime prompt firewall", "Agent behavior policy", "Real time alerts"] },
  { icon: "tb:TbRobot", label: "Red teaming", title: "Model red teaming",
    bullets: ["Jailbreak testing", "Data leakage probes", "Scheduled scans"] },
], { cols: 3 });
```

Capacity at 14pt: 3 columns by 2 rows with about 25 words per card, or 4 columns by 2 rows with a title and one short line. Twelve modules become two slides of six, not one slide of twelve.

## 4. Proof cards with callout

Outline icon, big red cost, red label, title, one sentence, then a tint strip carrying the pattern. To show the affected company, place its full colour logo with `ak.brandLogo` in the icon position instead of an icon.

```javascript
const s = ak.contentSlide(pres, { eyebrow: "02  Security platform play", title: "AI attacks are on the rise",
  subtitle: "Recent AI security incidents and their estimated cost, 2024 to 2026" });
await ak.cardGrid(s, [
  { icon: "tb:TbMessageExclamation", stat: "$3.5M", label: "Prompt injection · OpenAI", labelColor: ak.C.redDeep,
    title: "ChatGPT plugin prompt injection", body: "Emergency patching, audit and GDPR review." },
  // up to 6
], { cols: 3, bottom: 5.85 });
ak.callout(s, { lead: "Pattern", body: "Each incident started in a layer that cloud tools were never built to see." });
```

## 5. Stat row

Two to five headline numbers. Values in Inter Light. Use `color: ak.C.red` for cost or risk figures.

```javascript
const s = ak.contentSlide(pres, { eyebrow: "01  About AccuKnox", title: "AccuKnox at a glance" });
ak.statRow(s, [
  { value: "10+", label: "Patents", body: "Registered with the USPTO" },
  { value: "2M+", label: "KubeArmor downloads" },
  { value: "$15M", label: "Seed funding" },
]);
// Space below the row (from about y 4.4) can hold a logo wall or a callout.
```

## 6. Table

Native table, ink header, alternating rows, first column bold, optional highlighted column in blue.

```javascript
const s = ak.contentSlide(pres, { eyebrow: "04  Market opportunity", title: "Revenue share" });
ak.table(s, ["Partnership type", "Revenue share", "Details"], [
  ["Referral", "10%", "10% of NET subscription revenues"],
  ["Reseller", "20%", "20% of NET subscription revenues"],
], { colW: [3, 2.2, 6.93], highlightCol: 1 });
```

Up to 8 rows at 14pt. More rows means a second slide. `colW` must sum to `ak.CW` (12.13).

## 7. Split: statement left, content right

```javascript
const s = ak.contentSlide(pres, { eyebrow: "04  Market opportunity", title: "Pipeline creation",
  subtitle: "How a co-sold deal turns into recurring partner revenue" });
const right = ak.splitLeft(s, { heading: "20% of ARR paid directly to you",
  bullets: ["Example deal $100K ARR", "Your share $20K per year"] });
ak.steps(s, [
  { title: "Joint account mapping", body: "Find high fit accounts in your installed base." },
  { title: "Co-sell engagement", body: "An AccuKnox AE joins every deal above $25K." },
], right);
```

`splitLeft` returns the free right-hand box `{x, y, w, h}`. Fill it with steps, a card grid built manually, an image, a chart or a table.

## 8. Steps and timelines

Vertical numbered steps fill the given box. Three to five steps per column. For a horizontal phase view (onboarding phases, POC days), draw cards with `ak.card` in a row and put `ak.label("Phase 1")` plus a title and body in each.

```javascript
const s = ak.contentSlide(pres, { eyebrow: "06  What we give, what we get", title: "Partner onboarding",
  subtitle: "Four phases from signed agreement to first co-sold deal" });
const cols = 4, gap = 0.28, w = (ak.CW - gap * (cols - 1)) / cols;
["Engage", "Enable", "Activate", "Amplify"].forEach((ph, i) => {
  const x = ak.MX + i * (w + gap), y = s.top;
  ak.card(s, { x, y, w, h: 4.4, accent: i === 3 ? "red" : "blue" });
  ak.label(s, `Phase ${i + 1}`, { x: x + 0.3, y: y + 0.3, w: w - 0.6 });
  ak.text(s, ph, { x: x + 0.3, y: y + 0.65, w: w - 0.6, h: 0.4, fontSize: ak.T.cardTitle, bold: true, color: ak.C.ink });
  // ak.bullets(s, [...], { x: x + 0.3, y: y + 1.2, w: w - 0.6, h: 2.9 });
});
```

## 9. Two column compare

Two header chips (blue and ink) over matched rows. Good for "We give / We get", "Before / After", "Legacy tools / AccuKnox".

```javascript
const s = ak.contentSlide(pres, { eyebrow: "06  What we give, what we get", title: "What we give, what we get" });
const left = ak.splitLeft(s, { heading: "Partnership framework", body: "A balanced exchange that drives mutual growth." });
const colW = (left.w - 0.25) / 2, rows = ["Multitenant CNAPP access", "Wholesale pricing", "NFR licenses"];
[["We give", ak.C.blue, rows], ["We get", ak.C.ink, ["Committed $ARR targets", "Installed base access", "L1 and L2 support"]]]
  .forEach(([head, col, items], c) => {
    const x = left.x + c * (colW + 0.25);
    ak.solidBar(s, x, left.y, colW, 0.5, col);
    ak.label(s, head, { x, y: left.y, w: colW, h: 0.5, color: ak.C.white, align: "center" });
    items.forEach((t, r) => {
      const y = left.y + 0.65 + r * 0.62;
      s.addShape("rect", { x, y, w: colW, h: 0.52, fill: { color: ak.C.tintSoft }, line: { color: ak.C.border, width: 0.75 } });
      ak.text(s, t, { x: x + 0.2, y, w: colW - 0.4, h: 0.52, valign: "middle", color: ak.C.ink });
    });
  });
```

## 10. Logo wall

Rows of customer, investor or integration logos with a small label on the left. Use logo images from the source deck or user uploads with `ak.imageContain` in equal width slots (about 1.3 by 0.45in). For tech vendors without a supplied image, use the full colour logo: `await ak.brandLogo(s, "kubernetes", { x, y, w: 1.3, h: 0.45 })`. Keep logos in their own colours on white. Never recolour a logo or swap it for a mono glyph.

## 11. Image or diagram slide

For architecture diagrams, product screenshots, roadmaps or other visuals from the source: title frame, then the image contained in the content area, optionally with a 3 to 4 item narrative on the left via `splitLeft`.

```javascript
const s = ak.contentSlide(pres, { eyebrow: "06  What we give, what we get", title: "AccuKnox product roadmap" });
const right = ak.splitLeft(s, { heading: "From workload security to AI governance", leftW: 3.8 });
ak.imageContain(s, "/path/extracted/roadmap.png", right);
```

Diagrams you draw yourself use native shapes in brand colors: ink or blue boxes, `border` lines, outline icons in `iconGrey`, labels in Inter. Keep them simple and editable.

## 12. Section divider

Use for decks over about 12 slides, at each major part.

```javascript
ak.sectionSlide(pres, { part: "Part two", title: "Partner program",
  subtitle: "Market opportunity, partner economics and how we go to market together." });
```

## 13. Closing CTA

```javascript
ak.closingSlide(pres, {
  title: "See us in action",
  subtitle: "Partner with AccuKnox to co-sell Zero Trust security for cloud and AI.",
  cta: "Become a partner",
  ctaUrl: "https://accuknox.com/partners?utm_source=deck&utm_medium=pptx&utm_campaign=CAMPAIGN",
  email: "support@accuknox.com",
});
```

Add UTM parameters to the CTA link when the deck goes to external audiences.

## 14. Charts

Keep charts native with `slide.addChart`. Style them to the brand:

```javascript
s.addChart(pres.charts.BAR, [{ name: "Partners", labels: ["Americas", "APAC", "Middle East"], values: [41, 18, 4] }], {
  x: ak.MX, y: s.top, w: 7, h: 4.3, barDir: "bar",
  chartColors: [ak.C.blue], showValue: true, dataLabelColor: ak.C.ink, dataLabelFontSize: 12, dataLabelFontFace: "Inter",
  catAxisLabelColor: ak.C.body, catAxisLabelFontSize: 12, catAxisLabelFontFace: "Inter",
  valAxisHidden: true, valGridLine: { style: "none" }, catGridLine: { style: "none" }, showLegend: false,
});
```

Chart labels may go to 12pt. Everything else stays at 14pt or above.

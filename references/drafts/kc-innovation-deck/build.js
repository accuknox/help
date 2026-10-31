// AccuKnox AI Security innovation evidence deck for the KuppingerCole Leadership Compass fact check.
const path = require("path");
const W0 = __dirname;
const AKS = path.join(W0, "ak-pptx", "scripts");
const ak = require(path.join(AKS, "ak.js"));
const sharp = require(require.resolve("sharp", { paths: [AKS] }));
const { C, MX, CW, W } = ak;
const OUT = process.argv[2] || path.join(W0, "accuknox-ai-security-innovation-kc-v2.pptx");

const box = (s, x, y, w, h, fill = C.white, border = C.border) => s.addShape("rect", { x, y, w, h, fill: { color: fill }, line: { color: border, width: 0.75 } });
const bar = (s, x, y, h, color = C.blue) => s.addShape("rect", { x, y, w: 0.06, h, fill: { color }, line: { type: "none" } });
const fill = (s, x, y, w, h, color) => s.addShape("rect", { x, y, w, h, fill: { color }, line: { type: "none" } });
const WARN = "E8A600";

// ------------------------------------------------------------------ cover art
async function outlineCover(out) {
  const Wd = 1386, H = 1280, cx = 760, cy = 640, g = [];
  for (let gx = 0; gx < Wd; gx += 46) for (let gy = 0; gy < H; gy += 46) {
    const d = Math.hypot(gx - cx, gy - cy); if (d < 600) g.push(`<circle cx="${gx}" cy="${gy}" r="2" fill="#3A63E0" opacity="${(0.35 * (1 - d / 600)).toFixed(2)}"/>`);
  }
  g.push(`<circle cx="${cx}" cy="${cy}" r="470" fill="none" stroke="#16205A" stroke-width="3"/>`);
  g.push(`<circle cx="${cx}" cy="${cy}" r="340" fill="none" stroke="#3A63E0" stroke-width="3" stroke-dasharray="10 14"/>`);
  const sats = [0, 60, 120, 180, 240, 300].map((a) => [cx + 340 * Math.cos((a - 90) * Math.PI / 180), cy + 340 * Math.sin((a - 90) * Math.PI / 180)]);
  for (const [x, y] of sats) g.push(`<line x1="${cx}" y1="${cy}" x2="${x}" y2="${y}" stroke="#3A63E0" stroke-width="2" opacity="0.6"/>`);
  // satellites: model, agent, kernel chip, trophy, document, lock
  const glyphs = [
    (x, y) => `<circle cx="${x - 22}" cy="${y - 14}" r="9" fill="none" stroke="#8FA8FF" stroke-width="4"/><circle cx="${x + 22}" cy="${y - 14}" r="9" fill="none" stroke="#8FA8FF" stroke-width="4"/><circle cx="${x}" cy="${y + 22}" r="9" fill="none" stroke="#8FA8FF" stroke-width="4"/><path d="M${x - 15} ${y - 8} L${x - 5} ${y + 14} M${x + 15} ${y - 8} L${x + 5} ${y + 14} M${x - 13} ${y - 14} L${x + 13} ${y - 14}" stroke="#8FA8FF" stroke-width="4"/>`,
    (x, y) => `<rect x="${x - 28}" y="${y - 20}" width="56" height="44" rx="10" fill="none" stroke="#8FA8FF" stroke-width="4"/><circle cx="${x - 11}" cy="${y + 2}" r="5" fill="#6464FF"/><circle cx="${x + 11}" cy="${y + 2}" r="5" fill="#6464FF"/><path d="M${x} ${y - 20} L${x} ${y - 34}" stroke="#8FA8FF" stroke-width="4"/>`,
    (x, y) => `<rect x="${x - 24}" y="${y - 24}" width="48" height="48" rx="6" fill="none" stroke="#8FA8FF" stroke-width="4"/><rect x="${x - 10}" y="${y - 10}" width="20" height="20" fill="none" stroke="#6464FF" stroke-width="4"/><path d="M${x - 34} ${y - 10} h10 M${x - 34} ${y + 10} h10 M${x + 24} ${y - 10} h10 M${x + 24} ${y + 10} h10" stroke="#8FA8FF" stroke-width="4"/>`,
    (x, y) => `<path d="M${x - 22} ${y - 26} h44 v14 a22 22 0 0 1 -44 0 z" fill="none" stroke="#8FA8FF" stroke-width="4"/><path d="M${x} ${y + 10} v12 M${x - 14} ${y + 26} h28" stroke="#8FA8FF" stroke-width="4"/>`,
    (x, y) => `<path d="M${x - 22} ${y - 30} h30 l14 14 v46 h-44 z" fill="none" stroke="#8FA8FF" stroke-width="4"/><path d="M${x - 12} ${y + 2} l8 8 l16 -18" fill="none" stroke="#6464FF" stroke-width="4"/>`,
    (x, y) => `<rect x="${x - 22}" y="${y - 4}" width="44" height="32" rx="6" fill="none" stroke="#8FA8FF" stroke-width="4"/><path d="M${x - 13} ${y - 4} v-10 a13 13 0 0 1 26 0 v10" fill="none" stroke="#8FA8FF" stroke-width="4"/>`,
  ];
  sats.forEach(([x, y], i) => {
    g.push(`<rect x="${x - 62}" y="${y - 62}" width="124" height="124" rx="22" fill="#000025" stroke="#3A63E0" stroke-width="3"/>`);
    g.push(glyphs[i](x, y));
    g.push(`<circle cx="${(x + cx) / 2}" cy="${(y + cy) / 2}" r="7" fill="#6464FF"/>`);
  });
  // focal shield with neural net
  const sh = `M${cx} ${cy - 150} L${cx + 125} ${cy - 100} L${cx + 125} ${cy + 10} C${cx + 125} ${cy + 95} ${cx + 60} ${cy + 140} ${cx} ${cy + 165} C${cx - 60} ${cy + 140} ${cx - 125} ${cy + 95} ${cx - 125} ${cy + 10} L${cx - 125} ${cy - 100} Z`;
  g.push(`<path d="${sh}" fill="#000025" stroke="#FFFFFF" stroke-width="6" stroke-linejoin="round"/>`);
  const nodes = [[-50, -60], [50, -60], [-70, 15], [0, 10], [70, 15], [-35, 85], [35, 85]];
  const edges = [[0, 2], [0, 3], [1, 3], [1, 4], [2, 5], [3, 5], [3, 6], [4, 6], [0, 1]];
  for (const [a, b] of edges) g.push(`<line x1="${cx + nodes[a][0]}" y1="${cy + nodes[a][1]}" x2="${cx + nodes[b][0]}" y2="${cy + nodes[b][1]}" stroke="#8FA8FF" stroke-width="3"/>`);
  nodes.forEach(([x, y], i) => g.push(`<circle cx="${cx + x}" cy="${cy + y}" r="11" fill="#000025" stroke="${i === 3 ? "#FFFFFF" : "#8FA8FF"}" stroke-width="4"/>`));
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="${Wd}" height="${H}">${g.join("")}</svg>`;
  await sharp(Buffer.from(svg)).png().toFile(out);
  return out;
}

// ------------------------------------------------------------------ 1 cover
async function cover(pres) {
  ak.coverSlide(pres, {
    eyebrow: "KuppingerCole fact check  ·  November 2026",
    title: "AI Security Innovation",
    subtitle: "Six proof points for the Generative AI Defense Innovation rating",
    image: await outlineCover(path.join(W0, "cover.png")),
    notes: "Thank you for the draft and for the move from Contender to Challenger. This deck supports our fact check feedback on the Generative AI Defense Leadership Compass. The draft places AccuKnox as a Product Leader and a Challenger on Innovation. We bring six pieces of evidence that the draft does not yet reflect: an independent number one ranking on Hugging Face, an independent analyst review of AI firewall architectures, a US patent granted in September 2026, and three customer engagements in defense, capital markets and aviation. Let us start with what we are asking for.",
  });
}

// ------------------------------------------------------------------ 2 the ask
async function ask(pres) {
  const s = ak.contentSlide(pres, { eyebrow: "Summary", title: "Six Proof Points the Draft Does Not Yet Reflect",
    subtitle: "The draft rates AccuKnox a Product Leader and an Innovation Challenger",
    notes: "Here is the summary. The draft already rates us a Product Leader. On Innovation we sit with the Challengers. Four numbers carry our case. First, our guardrail model ranks number one of 41 on the independent GuardRate leaderboard on Hugging Face. Second, an independent analyst compared six AI firewall architectures and found ours to be the only stateful one. Third, the US Patent Office granted us patent 12,730,882 in September 2026. Fourth, three regulated customers in defense, capital markets and aviation chose or are testing AccuKnox for AI security. The rest of the deck takes each one in turn, then lists the factual additions we propose for the document." });
  ak.statRow(s, [
    { value: "#1", label: "Of 41 guardrail models", body: "HiveTrace GuardRate on Hugging Face, Oct 16, 2026" },
    { value: "1 of 6", label: "Stateful AI firewall", body: "The only stateful design in an analyst review" },
    { value: "18", label: "Patent claims", body: "US 12,730,882 B2, granted September 8, 2026" },
    { value: "3", label: "Regulated customers", body: "Defense, a stock exchange and a global airline" },
  ], { h: 2.5 });
  ak.rule(s, { x: MX, y: s.top + 2.75, w: CW });
  await ak.logoStrip(s, ["hugging-face", "kubernetes", "aws", "microsoft-azure", "google-cloud", "nvidia"], { y: s.top + 2.95, h: 0.55, label: "Evidence from" });
  ak.callout(s, { lead: "Our request", body: "Add these facts to the AccuKnox profile and weigh them in the Innovation rating.", y: 6.12, h: 0.6 });
}

// ------------------------------------------------------------------ 3 expert quotes
async function accolades(pres) {
  const s = ak.contentSlide(pres, { dark: true, eyebrow: "Accolades from industry experts", title: "Top CISOs and Analysts on AccuKnox AI Security",
    notes: "Before the detail, here is what three independent voices say. On the left, Dr. Edward Amoroso, former CISO of AT&T, often ranked among the top five CISOs. He points out that the enterprise AI stack is maturing faster than its security model, and that AccuKnox applies Zero Trust at the AI layer, where the exposure actually exists. In the middle, Golan Ben-Oni, CIO and CISO of IDT Corporation, featured in The Wall Street Journal and The New York Times on nation-state attacks. He calls AccuKnox AI-Security 2.0 a meaningful step forward. On the right, Andrew Green, enterprise IT research analyst, who reviewed six AI firewall architectures and found ours to be the only explicitly stateful one. The next slides show the evidence behind each statement." });
  const q = [
    { quote: "\u201CThe enterprise AI stack is maturing faster than its security model... AccuKnox AI-Security 2.0 takes a principled approach: applying Zero Trust at the AI layer to provide runtime protection, visibility, and identity governance where the exposure actually exists.\u201D",
      name: "Dr. Edward Amoroso", role: "Former CISO, AT&T", chip: "Top 5 CISO", icon: "tb:TbShieldStar" },
    { quote: "\u201CAI is quickly becoming the core infrastructure for modern enterprises, but the security model around it is still catching up... AccuKnox AI-Security 2.0 takes a meaningful step forward by applying Zero Trust principles directly to the AI layer.\u201D",
      name: "Golan Ben-Oni", role: "CIO and CISO, IDT Corporation. Featured in The Wall Street Journal and The New York Times on nation-state attacks", chip: "Top 10 CISO", icon: "tb:TbShieldStar" },
    { quote: "\u201CIntent is the most important vector we need to address in AI security. AccuKnox\u2019s Prompt Firewall is, as far as I know, the only explicitly stateful firewall that maintains context across turns.\u201D",
      name: "Andrew Green", role: "Enterprise IT Research Analyst", chip: "Independent analyst", icon: "tb:TbChartDots3" },
  ];
  const g = 0.3, cw = (CW - 2 * g) / 3, top = s.top + 0.05, ch = 6.6 - top, iw = cw - 0.6;
  const footH = 1.45, qTop = top + 1.0, qh = ch - (qTop - top) - footH - 0.15;
  const qs = ak.fitSize(q.map((x) => ({ text: x.quote, w: iw, h: qh, italic: true })), [18, 17, 16, 15, 14]);
  for (let i = 0; i < 3; i++) {
    const it = q[i], x = MX + i * (cw + g), mid = i === 1;
    ak.card(s, { x, y: top, w: cw, h: ch, accent: mid ? "accent" : "blue", fill: C.white, border: C.white });
    s.addShape("ellipse", { x: x + 0.3, y: top + 0.3, w: 0.62, h: 0.62, fill: { color: mid ? C.accent : C.blue }, line: { type: "none" } });
    await ak.icon(s, "tb:TbQuote", { x: x + 0.44, y: top + 0.44, s: 0.34, color: C.white });
    const chipW = Math.min(cw - 1.4, ak.textWidthPt(it.chip.toUpperCase(), 11, "bold") / 72 / ak.WRAP_SAFETY + 0.45);
    fill(s, x + cw - 0.3 - chipW, top + 0.43, chipW, 0.36, mid ? C.tintAccent : C.tint);
    ak.text(s, it.chip.toUpperCase(), { x: x + cw - 0.3 - chipW, y: top + 0.43, w: chipW, h: 0.36, fontSize: 11, bold: true, color: mid ? C.accent : C.blue, align: "center", valign: "middle" });
    ak.text(s, it.quote, { x: x + 0.3, y: qTop, w: iw, h: qh, fontSize: qs, italic: true, color: C.ink });
    const fy = top + ch - footH;
    ak.rule(s, { x: x + 0.3, y: fy, w: iw });
    ak.text(s, [{ text: it.name, options: { bold: true, color: C.ink, fontSize: 16, breakLine: true } }, { text: it.role, options: { color: C.muted, fontSize: 12 } }],
      { x: x + 0.3, y: fy + 0.12, w: iw, h: footH - 0.2, fontSize: 12 });
  }
}

// ------------------------------------------------------------------ 3 KC criteria
async function criteria(pres) {
  const s = ak.contentSlide(pres, { eyebrow: "KuppingerCole innovation criteria", title: "Five of Six Innovation Criteria Ship or Are Partly Live",
    notes: "The draft lists six innovative features for this market. We map each one to what AccuKnox ships today, using only facts already in the draft profile. Behavioral analysis of agents ships: ModelArmor learns a baseline and flags goal hijacking and anomalous tool use. Continuous red teaming ships: more than 150 probes, intelligent prompts tailored to each model, and a rerun after every fine tune. Three are partly live. Human approval is the default in AgentZ, and roadmap for third party agents. AskADA suggests remediation in natural language. The Prompt Firewall blocks abusive request patterns, and per user throttling is on the roadmap. Provenance of AI generated content is roadmap. We show the gaps openly because the analyst already knows them.",
  });
  const rows = [
    ["Behavioral analysis of AI agents", "Shipped", "ModelArmor learned baseline, goal hijack and tool exfiltration detection, eBPF default deny sandbox"],
    ["Continuous, adaptive red teaming", "Shipped", "150+ probes mapped to OWASP, MITRE ATLAS and AVID. Intelligent Red Teaming reruns after every change"],
    ["Human approval for high risk agent actions", "Partial", "Default setting in AgentZ. Roadmap for third party agent platforms"],
    ["Natural language policy and investigation", "Partial", "AskADA copilot explains findings and suggests remediation. Guardrail as code on the roadmap"],
    ["Token budgets and rate limits", "Partial", "Prompt Firewall blocks anomalous and abusive request patterns. Per user throttling on the roadmap"],
    ["Provenance tracking for AI content", "Roadmap", "Watermarking on the roadmap. AI-BOM pins model weights by hash today"],
  ];
  const top = s.top, cw = [3.6, 1.5, CW - 5.1], hh = 0.5, rh = (6.72 - top - hh) / rows.length;
  const heads = ["Innovation criterion in the draft", "Status", "What AccuKnox ships, per the draft profile"];
  let x = MX;
  heads.forEach((h, i) => { fill(s, x, top, cw[i], hh, C.ink); ak.text(s, h, { x: x + 0.15, y: top, w: cw[i] - 0.3, h: hh, fontSize: 13, bold: true, color: C.white, valign: "middle" }); x += cw[i]; });
  const st = { Shipped: ["tb:TbCircleCheck", C.blue], Partial: ["tb:TbAlertTriangle", WARN], Roadmap: ["tb:TbClock", C.muted] };
  for (let r = 0; r < rows.length; r++) {
    const y = top + hh + r * rh, [crit, status, ev] = rows[r];
    box(s, MX, y, CW, rh, r % 2 ? C.tintSoft : C.white);
    ak.text(s, crit, { x: MX + 0.15, y, w: cw[0] - 0.3, h: rh, fontSize: 14, bold: true, color: C.ink, valign: "middle" });
    await ak.icon(s, st[status][0], { x: MX + cw[0] + 0.15, y: y + (rh - 0.3) / 2, s: 0.3, color: st[status][1] });
    ak.text(s, status, { x: MX + cw[0] + 0.5, y, w: cw[1] - 0.55, h: rh, fontSize: 13, bold: true, color: status === "Shipped" ? C.blue : C.body, valign: "middle" });
    ak.text(s, ev, { x: MX + cw[0] + cw[1] + 0.15, y, w: cw[2] - 0.3, h: rh, fontSize: 13, color: C.body, valign: "middle" });
  }
}

// ------------------------------------------------------------------ 4 Hugging Face
async function huggingFace(pres) {
  const s = ak.contentSlide(pres, { eyebrow: "01  Independent benchmark", title: "AccuKnox Guard 1.1 Ranks #1 of 41 on Hugging Face",
    notes: "Our first proof point is independent. HiveTrace, an AI security company, runs every open guardrail model it can find through the same tests and publishes the GuardRate leaderboard on Hugging Face. HiveTrace ran our evaluation itself. In the October 16, 2026 snapshot of 41 models, 19 benchmark groups and 44 datasets, AccuKnox Guard 1.1 ranks first with 0.808, against 0.764 for the runner up. The scoring is a geometric mean, so one weak group pulls a model down. We block 13.7 percent of safe prompts against 21.8 percent for the runner up, and answer in 72.3 milliseconds at p95 on a 4.5 billion parameter model. This model powers the AccuKnox Prompt Firewall and AI Guardrails. To be fair, it is weaker on one prompt injection set, which we disclose in our own blog." });
  const top = s.top, lw = 4.3;
  const stats = [["0.808", "Integral score", "Runner up scores 0.764"], ["13.7%", "False positive rate", "Runner up: 21.8%"], ["72.3 ms", "p95 latency", "4.5B model, ahead of 8B to 15B"]];
  const sh = (6.72 - top - 0.5 - 2 * 0.16) / 3;
  for (let i = 0; i < 3; i++) {
    const y = top + i * (sh + 0.16);
    box(s, MX, y, lw, sh); bar(s, MX, y, sh);
    ak.text(s, stats[i][0], { x: MX + 0.3, y: y + 0.12, w: lw - 0.5, h: 0.62, fontFace: ak.FONT_LIGHT, fontSize: 32, color: C.blue });
    ak.label(s, stats[i][1], { x: MX + 0.3, y: y + 0.78, w: lw - 0.5, h: 0.26 });
    ak.text(s, stats[i][2], { x: MX + 0.3, y: y + 1.06, w: lw - 0.5, h: sh - 1.12, fontSize: 13, color: C.muted });
  }
  const rx = MX + lw + 0.35, rw = W - MX - rx, rh = 6.72 - top - 0.5;
  box(s, rx, top, rw, rh, C.white);
  const img = await sharp(path.join(W0, "shot-leaderboard-ranking.png")).extract({ left: 182, top: 910, width: 2436, height: 1090 }).png().toBuffer();
  await sharp(img).toFile(path.join(W0, "lb-crop.png"));
  ak.imageContain(s, path.join(W0, "lb-crop.png"), { x: rx + 0.1, y: top + 0.1, w: rw - 0.2, h: rh - 0.2 });
  ak.text(s, [{ text: "Source: ", options: { bold: true, color: C.muted } }, { text: "hivetrace-guardrateleaderboard.hf.space, snapshot October 16, 2026. Powers the AccuKnox Prompt Firewall and AI Guardrails.", options: { color: C.muted, hyperlink: { url: "https://hivetrace-guardrateleaderboard.hf.space/" } } }],
    { x: MX, y: 6.3, w: CW, h: 0.42, fontSize: 12 });
}

// ------------------------------------------------------------------ 5 Andrew Green
async function green(pres) {
  const s = ak.contentSlide(pres, { eyebrow: "02  Independent analyst review", title: "The Only Stateful AI Firewall of Six Reviewed",
    notes: "Our second proof point comes from Andrew Green, a top cyber analyst, in his white paper AI Firewall Architectures, Intent Analysis, and You. He compares six AI firewall vendors whose architectures are publicly documented: AccuKnox, Check Point with Lakera, Cloudflare, F5 with Calypso AI, HiddenLayer and Palo Alto Networks with Prisma AIRS. He argues that intent is the most important vector in AI security, and that intent depends on how context is managed across turns. Every other vendor in his table is stateless, so the customer must resend full history or lose multi turn detection. He calls the AccuKnox Prompt Firewall the only explicitly stateful firewall that maintains context across turns. For transparency, the paper notes that AccuKnox supplied its own architecture details." });
  const top = s.top, lw = 4.6;
  box(s, MX, top, lw, 6.72 - top, C.tintAccent, C.tintAccent);
  await ak.icon(s, "tb:TbQuote", { x: MX + 0.3, y: top + 0.3, s: 0.5, color: C.accent });
  ak.text(s, "“The only explicitly stateful firewall that maintains context across turns.”", { x: MX + 0.3, y: top + 0.95, w: lw - 0.6, h: 1.9, fontSize: 22, bold: true, color: C.ink });
  ak.rule(s, { x: MX + 0.3, y: top + 3.0, w: lw - 0.6 });
  ak.text(s, [{ text: "Andrew Green", options: { bold: true, color: C.ink, fontSize: 15, breakLine: true } }, { text: "Top cyber analyst. AI Firewall Architectures, Intent Analysis, and You, July 2026", options: { color: C.muted, fontSize: 13 } }],
    { x: MX + 0.3, y: top + 3.15, w: lw - 0.6, h: 1.1, fontSize: 13 });
  ak.text(s, "Statefulness lets a firewall score risk across a whole session, so slow multi turn attacks such as Crescendo stop being invisible.", { x: MX + 0.3, y: top + 4.3, w: lw - 0.6, h: 1.0, fontSize: 13, color: C.body });
  // comparison grid
  const rx = MX + lw + 0.35, rw = W - MX - rx, vendors = [["AccuKnox", "Stateful", "Cascading, deterministic to semantic"], ["Check Point (Lakera)", "Stateless", "ML, language models, rules"], ["Cloudflare", "Stateless", "Llama Guard 3 8B"], ["F5 (Calypso AI)", "Stateless", "Policy based inspection"], ["HiddenLayer", "Stateless", "Supervised and unsupervised ML"], ["Palo Alto (Prisma AIRS)", "Stateless", "AI powered network analysis"]];
  const cws = [2.55, 1.6, rw - 4.15], hh = 0.5, rh = (6.72 - top - hh) / vendors.length;
  let x = rx;
  ["Vendor", "Session state", "Detection approach"].forEach((h, i) => { fill(s, x, top, cws[i], hh, i === 1 ? C.blue : C.ink); ak.text(s, h, { x: x + 0.15, y: top, w: cws[i] - 0.3, h: hh, fontSize: 13, bold: true, color: C.white, valign: "middle" }); x += cws[i]; });
  for (let r = 0; r < vendors.length; r++) {
    const y = top + hh + r * rh, us = r === 0;
    box(s, rx, y, rw, rh, us ? C.tintAccent : r % 2 ? C.tintSoft : C.white);
    ak.text(s, vendors[r][0], { x: rx + 0.15, y, w: cws[0] - 0.3, h: rh, fontSize: 14, bold: true, color: C.ink, valign: "middle" });
    await ak.icon(s, us ? "tb:TbCircleCheck" : "tb:TbCircleX", { x: rx + cws[0] + 0.15, y: y + (rh - 0.3) / 2, s: 0.3, color: us ? C.blue : C.red });
    ak.text(s, vendors[r][1], { x: rx + cws[0] + 0.5, y, w: cws[1] - 0.55, h: rh, fontSize: 13, bold: us, color: us ? C.blue : C.body, valign: "middle" });
    ak.text(s, vendors[r][2], { x: rx + cws[0] + cws[1] + 0.15, y, w: cws[2] - 0.3, h: rh, fontSize: 13, color: C.body, valign: "middle" });
  }
}

// ------------------------------------------------------------------ 6 firewall pipeline
async function pipeline(pres) {
  const s = ak.contentSlide(pres, { eyebrow: "02  Independent analyst review", title: "How the Stateful Prompt Firewall Scores Intent",
    notes: "This is the pipeline the analyst documents. Every request goes through five steps. First, normalization unwinds unicode and homoglyph tricks. Second, cheap distilled CPU models plus rules classify injection, jailbreak, PII and toxicity on the hot path. Third, contextualization joins the new message with the session state. Fourth, scoring adds cumulative risk, semantic drift and escalation detection. Fifth, enforcement allows, sanitizes, blocks or steps up authentication. The session state lives in an in memory key value and vector store keyed by session, agent and user, holding a rolling summary, an embedding trajectory, a tool call ledger and a cumulative risk score. The firewall keeps its own copy, so it survives when the application trims history." });
  const steps = [["tb:TbLetterCaseToggle", "Normalize", "Unwind unicode and homoglyph obfuscation"], ["tb:TbFilter", "Classify", "Distilled CPU models plus rules on the hot path"], ["tb:TbStack2", "Contextualize", "Join the new turn with session state"], ["tb:TbGauge", "Score", "Cumulative risk, semantic drift, escalation"], ["tb:TbShieldCheck", "Enforce", "Allow, sanitize, block or step up auth"]];
  steps[0][0] = "tb:TbWand";
  const n = steps.length, y = s.top + 0.75, d = 1.0, sw = CW / n;
  ak.rule(s, { x: MX + sw / 2, y: y + d / 2, w: CW - sw, color: C.border, weight: 0.03 });
  for (let i = 0; i < n; i++) {
    const cx = MX + i * sw + sw / 2, last = i === n - 1;
    s.addShape("ellipse", { x: cx - d / 2, y, w: d, h: d, fill: { color: last ? C.accent : C.white }, line: { color: last ? C.accent : C.blue, width: 1.5 } });
    await ak.icon(s, steps[i][0], { x: cx - 0.24, y: y + d / 2 - 0.24, s: 0.48, color: last ? C.white : C.blue });
    ak.label(s, String(i + 1).padStart(2, "0"), { x: cx - sw / 2, y: y - 0.45, w: sw, h: 0.26, align: "center", color: last ? C.accent : C.blue });
    ak.text(s, steps[i][1], { x: cx - sw / 2 + 0.08, y: y + d + 0.2, w: sw - 0.16, h: 0.45, fontSize: 18, bold: true, color: C.ink, align: "center" });
    ak.text(s, steps[i][2], { x: cx - sw / 2 + 0.1, y: y + d + 0.7, w: sw - 0.2, h: 0.95, fontSize: 14, color: C.muted, align: "center" });
  }
  const py = y + d + 1.85, ph = 6.72 - py;
  box(s, MX, py, CW, ph, C.tint, C.tint);
  ak.label(s, "Session context engine, keyed by session, agent and user", { x: MX + 0.3, y: py + 0.18, w: CW - 0.6, h: 0.26 });
  const chips = [["tb:TbFileText", "Rolling conversation summary"], ["tb:TbChartDots", "Embedding trajectory"], ["tb:TbListDetails", "Tool call ledger"], ["tb:TbGauge", "Cumulative risk score"]];
  const cg = 0.2, cwd = (CW - 0.6 - 3 * cg) / 4, ch = ph - 0.7;
  for (let i = 0; i < 4; i++) {
    const x = MX + 0.3 + i * (cwd + cg);
    box(s, x, py + 0.55, cwd, ch);
    await ak.icon(s, chips[i][0], { x: x + 0.2, y: py + 0.55 + (ch - 0.3) / 2, s: 0.3, color: C.blue });
    ak.text(s, chips[i][1], { x: x + 0.6, y: py + 0.55, w: cwd - 0.7, h: ch, fontSize: 14, bold: true, color: C.ink, valign: "middle" });
  }
}

// ------------------------------------------------------------------ 7 patent facts
async function patent(pres) {
  const s = ak.contentSlide(pres, { eyebrow: "03  Patent", title: "US Patent 12,730,882 Taints Unknown Processes In Kernel",
    subtitle: "System and method for tainting suspicious process and applying targeted rules thereof",
    notes: "Our third proof point is a US patent granted on September 8, 2026, number 12,730,882 B2, with 18 claims. The inventors are Rahul Jadhav, our co-founder and CTO, and Barun Acharya. It was filed on December 8, 2023. The problem it solves is the trade off in Zero Trust. A blanket deny on every unknown process breaks applications, and a blanket allow leaves them open. The patent takes a third path. The system tracks unknown processes in the kernel and lets them run. The moment one touches a sensitive asset, file path or operation, it sets an in kernel taint flag, blocks the action, raises an alert and escalates the risk profile. This patent joins our earlier in kernel instrumentation patent and a portfolio of more than 10 patents." });
  const top = s.top, lw = 4.0;
  const facts = [["Granted", "September 8, 2026"], ["Filed", "December 8, 2023"], ["Claims", "18 claims, 8 drawing sheets"], ["Inventors", "Rahul Jadhav, Barun Acharya"]];
  const fh = (6.72 - top - 3 * 0.14) / 4;
  for (let i = 0; i < 4; i++) {
    const y = top + i * (fh + 0.14);
    box(s, MX, y, lw, fh); bar(s, MX, y, fh);
    ak.label(s, facts[i][0], { x: MX + 0.3, y: y + 0.14, w: lw - 0.5, h: 0.26 });
    ak.text(s, facts[i][1], { x: MX + 0.3, y: y + 0.42, w: lw - 0.5, h: fh - 0.5, fontSize: 15, bold: true, color: C.ink });
  }
  const rx = MX + lw + 0.4, rw = W - MX - rx;
  ak.label(s, "Key claims, from claim 1", { x: rx, y: top, w: rw, h: 0.26 });
  await ak.iconList(s, [
    { icon: "tb:TbCpu", title: "Kernel-level telemetry", body: "Log workload telemetry with security instruments executed in kernel space." },
    { icon: "tb:TbEye", title: "Track unknown processes in kernel", body: "Allow unknown processes that do not touch sensitive assets, paths or operations." },
    { icon: "tb:TbFlag", title: "Taint on sensitive access", body: "Set an in kernel flag on each unknown process that reaches for a sensitive asset." },
    { icon: "tb:TbShieldX", title: "Block, alert, escalate", body: "Block the tainted process, raise an alert and escalate the risk profile automatically." },
  ], { x: rx, y: top + 0.42, w: rw, h: 6.72 - top - 0.42, color: C.ink });
}

// ------------------------------------------------------------------ 8 patent to AI
async function patentAI(pres) {
  const s = ak.contentSlide(pres, { eyebrow: "03  Patent", title: "Why the Patent Matters for AI Agents",
    notes: "Here is why this patent matters for generative AI defense. AI agents and code interpreters spawn processes nobody wrote in advance. A strict allow list breaks them, and an open policy lets a hijacked agent reach data and networks. Tainting gives a middle path. On the left, the old choice. On the right, the AccuKnox approach. An agent can run new tools and generated code, and only the actions that touch sensitive assets get blocked and escalated. This mechanism sits under the ModelArmor agent sandbox and KubeArmor, which the draft already lists as our kernel-level runtime strength. Applying it to AI agents is our product use of the patent, the claims themselves cover processes and workloads in general." });
  const top = s.top, g = 0.3, cw = (CW - 2 * g) / 3, h = 6.72 - top - 0.85, hh = 0.62;
  const cols = [
    { head: "Blanket deny", icon: "tb:TbLock", color: C.red, tint: "FDECEC", items: ["Blocks every unknown process", "Breaks agents that spawn new tools", "Teams turn the control off"], mark: "tb:TbX" },
    { head: "Blanket allow", icon: "tb:TbLockOpen", color: C.red, tint: "FDECEC", items: ["Runs every unknown process", "A hijacked agent reaches data", "Detection after the damage"], mark: "tb:TbX" },
    { head: "AccuKnox tainting", icon: "tb:TbShieldCheck", color: C.accent, tint: C.tintAccent, items: ["Unknown processes run", "Sensitive actions are blocked in kernel", "Risk escalates automatically"], mark: "tb:TbCheck" },
  ];
  for (let i = 0; i < 3; i++) {
    const c = cols[i], x = MX + i * (cw + g);
    box(s, x, top, cw, h, c.tint, c.tint);
    fill(s, x, top, cw, hh, c.color);
    await ak.icon(s, c.icon, { x: x + 0.2, y: top + 0.14, s: 0.34, color: C.white });
    ak.text(s, c.head, { x: x + 0.66, y: top, w: cw - 0.8, h: hh, fontSize: 16, bold: true, color: C.white, valign: "middle" });
    await ak.iconList(s, c.items.map((t) => ({ icon: c.mark, title: t })), { x: x + 0.25, y: top + hh + 0.3, w: cw - 0.5, h: h - hh - 0.5, tier: "standard", color: C.ink });
  }
  ak.callout(s, { lead: "In product", body: "Tainting runs under the ModelArmor agent sandbox and KubeArmor, a CNCF project.", y: 6.12, h: 0.6 });
}

// ------------------------------------------------------------------ 9 section
function section(pres) {
  ak.sectionSlide(pres, { part: "Part two", title: "Customer Proof", subtitle: "Defense, capital markets and aviation chose or are testing AccuKnox for AI security.",
    notes: "The last three proof points are customers. All three are regulated, all three needed AI security on infrastructure they control, and all three map to the draft's statement that AccuKnox suits regulated and sovereign environments. We anonymize each one, as our agreements require." });
}

// ------------------------------------------------------------------ case study template
async function caseStudy(pres, o) {
  const s = ak.contentSlide(pres, { eyebrow: o.eyebrow, title: o.title, subtitle: o.subtitle, notes: o.notes });
  const top = s.top, g = 0.3, cw = (CW - 2 * g) / 3, h = (o.stats ? 5.5 : 6.72) - top, hh = 0.62;
  const cols = [
    { head: "Problem", icon: "tb:TbAlertTriangle", color: C.red, tint: "FDECEC", items: o.problem, mark: "tb:TbPoint" },
    { head: "AccuKnox solution", icon: "tb:TbShieldCheck", color: C.blue, tint: C.tint, items: o.solution, mark: "tb:TbCheck" },
    { head: "Key differentiators", icon: "tb:TbStar", color: C.accent, tint: C.tintAccent, items: o.diff, mark: "tb:TbCheck" },
  ];
  for (let i = 0; i < 3; i++) {
    const c = cols[i], x = MX + i * (cw + g);
    box(s, x, top, cw, h, c.tint, c.tint);
    fill(s, x, top, cw, hh, c.color);
    await ak.icon(s, c.icon, { x: x + 0.2, y: top + 0.14, s: 0.34, color: C.white });
    ak.text(s, c.head, { x: x + 0.66, y: top, w: cw - 0.8, h: hh, fontSize: 16, bold: true, color: C.white, valign: "middle" });
    await ak.iconList(s, c.items.map((t) => ({ icon: c.mark, title: t })), { x: x + 0.2, y: top + hh + 0.2, w: cw - 0.4, h: h - hh - 0.3, tier: "dense", color: C.ink });
  }
  if (o.stats) {
    const sy = 5.68, n = o.stats.length, sg = 0.2, sw = (CW - (n - 1) * sg) / n, shh = 6.72 - sy;
    for (let i = 0; i < n; i++) {
      const x = MX + i * (sw + sg);
      box(s, x, sy, sw, shh); bar(s, x, sy, shh);
      ak.text(s, o.stats[i][0], { x: x + 0.25, y: sy + 0.08, w: sw - 0.35, h: 0.55, fontFace: ak.FONT_LIGHT, fontSize: 26, color: C.blue });
      ak.text(s, o.stats[i][1], { x: x + 0.25, y: sy + 0.6, w: sw - 0.35, h: shh - 0.64, fontSize: 12, color: C.muted });
    }
  }
}

async function caseDoW(pres) {
  await caseStudy(pres, {
    eyebrow: "04  Customer proof  ·  Defense", title: "A Top US Department of War Lab Chose AccuKnox",
    subtitle: "After a 12 month POC of 8 vendors, for air-gapped AI security across classified networks",
    problem: ["Run changing LLM, vision and RAG models air-gapped", "Zero Trust across NIPR, SIPR and JWICS", "Reach ATO at mission speed"],
    solution: ["Air-gapped, on-prem control plane", "KubeArmor eBPF enforcement on inference pods", "Prompt Firewall and a sandbox per model", "NIST 800-53 and DISA STIG mapping"],
    diff: ["No external model calls", "No loss of mission speed", "Red team before model promotion", "One platform, AppSec to AI"],
    stats: [["8", "Vendors in the POC"], ["12 months", "POC duration"], ["4 phases", "Pilot to ATO ready end state"], ["3 networks", "NIPR, SIPR and JWICS in scope"]],
    notes: "Our first customer is a top US Department of War research organization. We anonymize it under our agreement. It ran a 12 month proof of concept across 8 vendors and selected AccuKnox. The problem was to bring changing AI models, LLMs, computer vision and RAG tools, into an air-gapped boundary and across classified networks, and still reach an Authority to Operate. Our solution ran fully on premises: a local control plane, KubeArmor eBPF enforcement around inference pods, the Prompt Firewall between users and models, a sandbox for each model with red team triggers before promotion, and supply chain and compliance mapping to NIST 800-53 and DISA STIGs. What set us apart was true air-gapped operation, no loss of mission speed, and one platform instead of several point tools.",
  });
}

async function caseBSE(pres) {
  await caseStudy(pres, {
    eyebrow: "05  Customer proof  ·  Capital markets", title: "A Top Asian Stock Exchange Tests 36 AI Use Cases",
    subtitle: "On-prem, air-gapped AI security across browsers, endpoints, agents and APIs",
    problem: ["Staff use public AI chat with no control", "Agents run on hosts and behind gateways", "Trade channels need their own rules", "Every event must reach QRadar"],
    solution: ["Air-gapped, CPU-only, on-prem", "Tamper resistant browser plugin", "Host agent sandbox, LiteLLM gateway", "AI-BOM and OCSF events to QRadar"],
    diff: ["Browser to API in one platform", "Kernel sandbox for host agents", "Red teams models and agents", "Data stays on premises"],
    stats: [["36", "Test cases in the POC scope"], ["3 phases", "Foundation, visibility, governance"], ["7", "AI surfaces covered"], ["0", "External calls, air-gapped"]],
    notes: "Our second customer is one of the top stock exchanges in Asia. It is anonymized. The exchange runs a proof of concept with 36 test cases in three phases: foundation controls, AI discovery and enforcement, then governance and operations. The problem is AI everywhere. Employees use public chat tools, agents run on hosts and behind AI gateways, trade channels need their own moderation, and the SOC needs every event in QRadar. Our solution runs on premises and air-gapped on CPU only, with a tamper resistant browser plugin, agent sandboxing on hosts, gateway integration, shadow AI discovery, software, crypto and AI bills of materials, and OCSF events to QRadar. What sets us apart is one platform across seven AI surfaces with a kernel-level sandbox.",
  });
}

async function caseAir(pres) {
  await caseStudy(pres, {
    eyebrow: "06  Customer proof  ·  Aviation", title: "A Global Airline Secures 40+ AI Agents Across Three Clouds",
    subtitle: "AWS Bedrock, Azure AI Foundry and Copilot Studio, in production",
    problem: ["40+ agents with no unified view", "Production agents with no guardrails", "Public notebooks and AKS CVEs", "No AI compliance tracking"],
    solution: ["Found 40 shadow Copilot agents", "Stateful Prompt Firewall at APIM", "eBPF agent sandbox on AKS", "25+ AI frameworks mapped"],
    diff: ["Agent discovery in three clouds", "No application code changes", "Blocks unsafe tool use in kernel", "AI security and CNAPP in one"],
    stats: [["90%", "Lower runtime security risk"], ["1,500+", "Models in live inventory within days"], ["85%", "Lower data leakage risk"], ["70%", "Fewer cloud security incidents"]],
    notes: "Our third customer is a global airline, anonymized, and the case study is public on accuknox.com. The airline ran more than 40 AI agents across AWS Bedrock, Azure AI Foundry and Copilot Studio with no unified view and no guardrails. Our inventory found 40 shadow Copilot agents and more than 1,500 models. We put the stateful Prompt Firewall behind Azure API Management and AWS API Gateway, ran automated red teaming, and sandboxed agents on AKS with eBPF. The published outcomes: runtime security risk down 90 percent, data leakage risk down 85 percent, cloud security incidents down 70 percent, and a live inventory of more than 1,500 models within days. The Head of Cloud and AI Security said AccuKnox gives them the protection they need for their cloud AI infrastructure.",
  });
}

// ------------------------------------------------------------------ 13 fact check items
async function factCheck(pres) {
  const s = ak.contentSlide(pres, { eyebrow: "Fact check", title: "Five Additions We Propose for the AccuKnox Profile",
    notes: "These are the factual additions we will make as tracked changes and comments in the Word document, each with its source attached. One, add the GuardRate number one ranking. Two, add the independent analyst finding that our Prompt Firewall is the only stateful design of six. Three, add the patent granted in September 2026. Four, clarify that human approval for agent actions is already the default in AgentZ, which the draft states in a later paragraph, so the challenge applies to third party agent platforms only. Five, add the three customer references to the existing Airbus reference. We ask the analyst to weigh these facts when setting the Innovation rating." });
  const rows = [
    ["tb:TbTrophy", "Strengths", "Add: AccuKnox Guard 1.1 ranks #1 of 41 on the GuardRate leaderboard, October 16, 2026", "Leaderboard snapshot and evaluation request"],
    ["tb:TbFileSearch", "Prompt Firewall paragraph", "Add: independent analyst review finds it the only stateful AI firewall of six vendors", "Andrew Green white paper, July 2026"],
    ["tb:TbCertificate", "Company and innovation", "Add: US Patent 12,730,882 B2, granted September 8, 2026, 18 claims", "USPTO grant certificate"],
    ["tb:TbUserCheck", "Challenges", "Clarify: human approval is already the AgentZ default, the gap is third party agents only", "Draft profile, AgentZ paragraph"],
    ["tb:TbBuildingBank", "References", "Add: US Department of War lab, Asian stock exchange and global airline", "Anonymized summaries, slides 11 to 13"],
  ];
  const top = s.top, cws = [0.6, 2.6, 5.9, CW - 9.1], hh = 0.5, rh = (6.72 - top - hh) / rows.length;
  let x = MX;
  ["", "Report section", "Proposed change", "Evidence attached"].forEach((h, i) => { fill(s, x, top, cws[i], hh, C.ink); if (h) ak.text(s, h, { x: x + 0.15, y: top, w: cws[i] - 0.3, h: hh, fontSize: 13, bold: true, color: C.white, valign: "middle" }); x += cws[i]; });
  for (let r = 0; r < rows.length; r++) {
    const y = top + hh + r * rh, [ic, sec, chg, ev] = rows[r];
    box(s, MX, y, CW, rh, r % 2 ? C.tintSoft : C.white);
    await ak.icon(s, ic, { x: MX + 0.15, y: y + (rh - 0.3) / 2, s: 0.3, color: C.blue });
    ak.text(s, sec, { x: MX + cws[0] + 0.1, y, w: cws[1] - 0.2, h: rh, fontSize: 14, bold: true, color: C.ink, valign: "middle" });
    ak.text(s, chg, { x: MX + cws[0] + cws[1] + 0.15, y, w: cws[2] - 0.3, h: rh, fontSize: 13, color: C.body, valign: "middle" });
    ak.text(s, ev, { x: MX + cws[0] + cws[1] + cws[2] + 0.15, y, w: cws[3] - 0.3, h: rh, fontSize: 12, color: C.muted, valign: "middle" });
  }
}

function closing(pres) {
  ak.closingSlide(pres, { title: "Thank you", subtitle: "We welcome a fact check call with the analyst to walk through this evidence.", cta: "AccuKnox AI Security", ctaUrl: "https://accuknox.com/platform/ai-security", email: "support@accuknox.com",
    notes: "Thank you. We will send the tracked changes and the supporting documents at least 48 hours before any call, as the fact check process requires. We are happy to walk the analyst through the leaderboard data, the patent claims and the customer summaries." });
}

(async () => {
  const pres = ak.createDeck({ title: "AccuKnox AI Security Innovation" });
  await cover(pres); await ask(pres); await accolades(pres); await criteria(pres); await huggingFace(pres); await green(pres); await pipeline(pres);
  await patent(pres); await patentAI(pres); section(pres); await caseDoW(pres); await caseBSE(pres); await caseAir(pres);
  await factCheck(pres); closing(pres);
  await ak.finalize(pres, OUT);
})().catch((e) => { console.error(e); process.exit(1); });

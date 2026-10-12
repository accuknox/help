// Created by: Claude Cowork
// Date: 2026-10-07
// Purpose: AccuKnox slide system helpers for pptxgenjs (brand tokens, frames, cards, icons, gradient post-processing)
// Owner: AccuKnox Product Marketing
//
// Usage from a build script:
//   const ak = require("/path/to/accuknox-pptx-rebrand/scripts/ak.js");
//   const pres = ak.createDeck({ title: "Partner Program" });
//   ak.coverSlide(pres, {...});
//   const s = ak.contentSlide(pres, { eyebrow: "01  About AccuKnox", title: "...", subtitle: "..." });
//   await ak.iconCircle(s, "tb:TbShieldLock", { x: 1, y: 2.5 });
//   await ak.finalize(pres, "/mnt/user-data/outputs/deck.pptx");

const path = require("path");
const fs = require("fs");
const PptxGenJS = require("pptxgenjs");
const JSZip = require(require.resolve("jszip", { paths: [require.resolve("pptxgenjs")] }));

const ASSETS = path.join(__dirname, "..", "assets");

// ---------------------------------------------------------------------------
// Brand tokens (hex without '#', pptxgenjs requirement)
// ---------------------------------------------------------------------------
const C = {
  blue: "1040C5",      // primary brand blue: eyebrows, numerals, links, footer bar, page number
  red: "FF4646",       // accent red: gradient start, incident stats, warning labels
  redDeep: "D63637",   // red text on white when FF4646 is too light for small text
  ink: "000025",       // titles on white, dark slide background
  navyCard: "16205A",  // dark panels and concentric rings on dark slides
  body: "37474F",      // body text on white
  muted: "607D8B",     // subtitles, captions, secondary copy
  border: "DCE3F0",    // card borders, table rules
  tint: "E2EEFF",      // callout strip, highlighted rows
  tintSoft: "F8FAFF",  // alternating rows, soft panels
  periwinkle: "8FA8FF",// secondary text on dark slides
  iconGrey: "4A5873",  // outline icons: darker bluish grey, no background
  white: "FFFFFF",
};

// Placeholder colour swapped for a native red->blue gradFill in finalize().
// Never use this hex for anything else.
const GRAD_TOKEN = "FE4647";

// Type scale (pt). Body floor is 14pt. Do not go below it for readable copy.
const T = {
  coverTitle: 54,
  sectionTitle: 48,
  title: 32,
  subtitle: 16,
  eyebrow: 11,
  cardTitle: 18,
  body: 14,
  label: 11,        // small caps style labels (letterspaced, bold)
  numeral: 44,      // agenda numbers, stat numbers (Inter Light)
  bigStat: 54,
  footer: 9,        // footer meta only
};

const FONT = "Inter";
const FONT_LIGHT = "Inter Light";

// Slide geometry (16:9, inches)
const W = 13.333, H = 7.5;
const MX = 0.6;                 // left/right margin
const CONTENT_TOP = 2.15;       // first y below header when subtitle present
const CONTENT_TOP_NOSUB = 1.75; // first y below header when no subtitle
const CONTENT_BOTTOM = 6.7;     // keep content above footer
const CW = W - 2 * MX;          // content width

let _page = 0;

// ---------------------------------------------------------------------------
// Deck
// ---------------------------------------------------------------------------
function createDeck({ title = "AccuKnox", author = "AccuKnox" } = {}) {
  const pres = new PptxGenJS();
  pres.layout = "LAYOUT_WIDE";
  pres.title = title;
  pres.author = author;
  pres.company = "AccuKnox";
  pres.theme = { headFontFace: FONT, bodyFontFace: FONT };
  _page = 0;
  return pres;
}

// ---------------------------------------------------------------------------
// Primitives
// ---------------------------------------------------------------------------
function gradBar(slide, x, y, w, h = 0.05) {
  slide.addShape("rect", { x, y, w, h, fill: { color: GRAD_TOKEN }, line: { type: "none" } });
}

function solidBar(slide, x, y, w, h, color) {
  slide.addShape("rect", { x, y, w, h, fill: { color }, line: { type: "none" } });
}

// White card with thin border and a 0.05in top accent (gradient by default).
// accent: "gradient" | "blue" | "red" | "ink" | "none"
function card(slide, { x, y, w, h, accent = "gradient", fill = C.white, border = C.border }) {
  slide.addShape("rect", { x, y, w, h, fill: { color: fill }, line: { color: border, width: 0.75 } });
  if (accent === "gradient") gradBar(slide, x, y, w, 0.05);
  else if (accent !== "none") {
    const col = { blue: C.blue, red: C.red, ink: C.ink }[accent] || accent;
    solidBar(slide, x, y, w, 0.05, col);
  }
}

// Letterspaced bold label, e.g. "PROMPT INJECTION · OPENAI"
function label(slide, text, { x, y, w, h = 0.3, color = C.blue, size = T.label, align = "left" }) {
  slide.addText(String(text).toUpperCase(), {
    x, y, w, h, fontFace: FONT, fontSize: size, bold: true, color, charSpacing: 2,
    margin: 0, valign: "middle", align,
  });
}

// Plain text helper with brand defaults. Pass runs (array) or string.
function text(slide, content, opts) {
  const o = Object.assign({ fontFace: FONT, fontSize: T.body, color: C.body, margin: 0, valign: "top" }, opts);
  slide.addText(content, o);
}

// Bulleted list with arrow bullets, as in the reference deck
function bullets(slide, items, { x, y, w, h, size = T.body, color = C.body, arrowColor = C.blue, gap = 6 }) {
  const runs = [];
  items.forEach((it, i) => {
    runs.push({ text: "→  ", options: { color: arrowColor, bold: true } });
    runs.push({ text: it, options: { breakLine: i < items.length - 1, paraSpaceAfter: gap } });
  });
  slide.addText(runs, { x, y, w, h, fontFace: FONT, fontSize: size, color, margin: 0, valign: "top" });
}

// Light blue callout strip: bold blue lead word + sentence
function callout(slide, { lead, body, x = MX, y = 6.05, w = CW, h = 0.55 }) {
  slide.addShape("rect", { x, y, w, h, fill: { color: C.tint }, line: { type: "none" } });
  const runs = [];
  if (lead) runs.push({ text: lead + "  ", options: { bold: true, color: C.blue } });
  runs.push({ text: body, options: { color: C.ink } });
  slide.addText(runs, { x: x + 0.3, y, w: w - 0.6, h, fontFace: FONT, fontSize: T.body, valign: "middle", margin: 0 });
}

// Rough overflow check. Inter averages ~0.53em per character.
function estimateLines(str, pt, wIn) {
  const charsPerLine = Math.max(1, Math.floor((wIn * 72) / (pt * 0.53)));
  return String(str).split("\n").reduce((n, para) => n + Math.max(1, Math.ceil(para.length / charsPerLine)), 0);
}
function fits(str, pt, wIn, hIn, lineSpacing = 1.25) {
  return estimateLines(str, pt, wIn) * pt * lineSpacing / 72 <= hIn;
}
function warnIfOverflow(id, str, pt, wIn, hIn) {
  if (!fits(str, pt, wIn, hIn)) console.warn(`[ak] possible overflow in ${id}: "${String(str).slice(0, 50)}..." (${pt}pt in ${wIn}x${hIn}in). Shorten copy or split the slide; do not shrink below the type floor.`);
}

// ---------------------------------------------------------------------------
// Icons and images
// ---------------------------------------------------------------------------
// name format "<set>:<Export>", e.g. "tb:TbShieldLock", "fa6:FaRobot", "si:SiKubernetes"
const _iconCache = {};
async function iconPng(name, color = "#FFFFFF", size = 256) {
  const key = `${name}|${color}|${size}`;
  if (_iconCache[key]) return _iconCache[key];
  const [set, exp] = name.split(":");
  const React = require("react");
  const ReactDOMServer = require("react-dom/server");
  const sharp = require("sharp");
  const lib = require(`react-icons/${set}`);
  const Comp = lib[exp];
  if (!Comp) { console.warn(`[ak] icon ${name} not found in react-icons/${set}. Run: node ak.js --find <term>`); return null; }
  const svg = ReactDOMServer.renderToStaticMarkup(React.createElement(Comp, { color, size: String(size) }));
  const buf = await sharp(Buffer.from(svg)).png().toBuffer();
  const data = "image/png;base64," + buf.toString("base64");
  _iconCache[key] = data;
  return data;
}

// Outline icon, no background, in darker bluish grey (the house icon style).
// Kept under the old name so layouts that call iconCircle get the new style. d = box size.
// Pass filled: true only for the rare case that needs a solid ink disc (for example on a photo).
async function iconCircle(slide, name, { x, y, d = 0.6, color = C.iconGrey, filled = false, bg = C.ink, fg = "FFFFFF" }) {
  if (filled) {
    slide.addShape("ellipse", { x, y, w: d, h: d, fill: { color: bg }, line: { type: "none" } });
    const s = d * 0.55, data = await iconPng(name, "#" + fg);
    if (data) slide.addImage({ data, x: x + (d - s) / 2, y: y + (d - s) / 2, w: s, h: s });
    return;
  }
  if (/^fa6?:/.test(name)) console.warn(`[ak] ${name} is a solid glyph. Prefer an outline icon from tb: (Tabler) or lu: (Lucide).`);
  const s = d * 0.85, data = await iconPng(name, "#" + color);
  if (data) slide.addImage({ data, x: x + (d - s) / 2, y: y + (d - s) / 2, w: s, h: s });
}

// Bare outline icon
async function icon(slide, name, { x, y, s = 0.6, color = C.iconGrey }) {
  const data = await iconPng(name, "#" + color);
  if (data) slide.addImage({ data, x, y, w: s, h: s });
}

// Full colour company or product logo from the bundled "logos" set (official colours, never recoloured).
// name: e.g. "aws", "microsoft-azure", "google-cloud", "openai", "kubernetes", "hugging-face".
// Find names with: node ak.js --logo <term>. Returns false if not found so the caller can fall back
// to a logo image from the source deck or the company name as text.
let _logos = null;
async function brandLogo(slide, name, { x, y, w, h, align = "center" }) {
  if (!_logos) _logos = JSON.parse(fs.readFileSync(path.join(ASSETS, "brand-logos-iconify.json"), "utf8"));
  const ic = _logos.icons[name];
  if (!ic) { console.warn(`[ak] brand logo "${name}" not in set. Use the source deck image or set the name as text.`); return false; }
  const vw = ic.width || _logos.width || 256, vh = ic.height || _logos.height || 256;
  const scale = Math.max(1, 900 / Math.max(vw, vh));
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 ${vw} ${vh}" width="${Math.round(vw * scale)}" height="${Math.round(vh * scale)}">${ic.body}</svg>`;
  const buf = await require("sharp")(Buffer.from(svg)).png().toBuffer();
  const r = vw / vh; let iw = w, ih = w / r; if (ih > h) { ih = h; iw = h * r; }
  const ix = align === "left" ? x : align === "right" ? x + w - iw : x + (w - iw) / 2;
  slide.addImage({ data: "image/png;base64," + buf.toString("base64"), x: ix, y: y + (h - ih) / 2, w: iw, h: ih });
  return true;
}

function asset(file) { return path.join(ASSETS, file); }

// Topic based outline artwork for covers and dark slides. motif: ai | cloud | code | network |
// compliance | runtime, or any topic text (mapped automatically). Returns a PNG path.
async function coverArt(motifOrTopic) { return require("./cover_art.js").coverArtPng(motifOrTopic); }

// Insert an image preserving aspect ratio inside a box (contain)
function imageContain(slide, filePath, { x, y, w, h, align = "center" }) {
  const sharpMeta = _imgSize(filePath);
  const r = sharpMeta.w / sharpMeta.h;
  let iw = w, ih = w / r;
  if (ih > h) { ih = h; iw = h * r; }
  const ix = align === "left" ? x : align === "right" ? x + w - iw : x + (w - iw) / 2;
  slide.addImage({ path: filePath, x: ix, y: y + (h - ih) / 2, w: iw, h: ih });
}
function _imgSize(p) {
  // PNG header read (no async). Width/height at bytes 16..23.
  const b = fs.readFileSync(p);
  if (b.toString("ascii", 1, 4) === "PNG") return { w: b.readUInt32BE(16), h: b.readUInt32BE(20) };
  // JPEG fallback: scan SOF markers
  let i = 2;
  while (i < b.length) {
    const m = b[i + 1], len = b.readUInt16BE(i + 2);
    if (m >= 0xc0 && m <= 0xcf && m !== 0xc4 && m !== 0xc8 && m !== 0xcc) return { w: b.readUInt16BE(i + 7), h: b.readUInt16BE(i + 5) };
    i += 2 + len;
  }
  return { w: 1, h: 1 };
}

// ---------------------------------------------------------------------------
// Frames
// ---------------------------------------------------------------------------
function footer(slide, { dark = false, page, confidential = "Confidential. Limited distribution under NDA." } = {}) {
  if (!dark) {
    imageContain(slide, asset("logo-blue.png"), { x: MX, y: 6.92, w: 1.45, h: 0.3, align: "left" });
    if (confidential) text(slide, confidential, { x: 3.67, y: 6.95, w: 6, h: 0.25, fontSize: T.footer, color: C.muted, align: "center", valign: "middle" });
    if (page != null) text(slide, String(page).padStart(2, "0"), { x: W - MX - 0.8, y: 6.93, w: 0.8, h: 0.28, fontSize: 12, bold: true, color: C.blue, align: "right", valign: "middle" });
    solidBar(slide, 0, H - 0.1, W, 0.1, C.blue);
  } else if (page != null) {
    text(slide, String(page).padStart(2, "0"), { x: W - MX - 0.8, y: 6.93, w: 0.8, h: 0.28, fontSize: 12, color: C.periwinkle, align: "right", valign: "middle" });
  }
}

// Standard white content slide: gradient tick, eyebrow, title, optional subtitle, footer.
// Returns { slide, top } where top is the first free y for content.
function contentSlide(pres, { eyebrow, title, subtitle, notes, confidential } = {}) {
  const slide = pres.addSlide();
  _page += 1;
  slide.background = { color: C.white };
  gradBar(slide, MX, 0.42, 0.55, 0.05);
  if (eyebrow) label(slide, eyebrow, { x: MX, y: 0.55, w: 9, h: 0.3 });
  warnIfOverflow("title", title || "", T.title, CW, 0.65);
  text(slide, title || "", { x: MX, y: 0.88, w: CW, h: 0.65, fontSize: T.title, bold: true, color: C.ink, valign: "middle" });
  if (subtitle) text(slide, subtitle, { x: MX, y: 1.55, w: CW, h: 0.4, fontSize: T.subtitle, color: C.muted, valign: "middle" });
  footer(slide, { page: _page, confidential });
  if (notes) slide.addNotes(notes);
  slide.top = subtitle ? CONTENT_TOP : CONTENT_TOP_NOSUB;
  return slide;
}

function _darkBase(pres, { rings = true } = {}) {
  const slide = pres.addSlide();
  _page += 1;
  slide.background = { color: C.ink };
  if (rings) {
    // Concentric rings, right side, partly off canvas
    const cx = 10.6, cy = 3.9;
    [1.4, 2.3, 3.2, 4.1, 5.0].forEach((r) => {
      slide.addShape("ellipse", { x: cx - r, y: cy - r, w: 2 * r, h: 2 * r, fill: { type: "none" }, line: { color: C.navyCard, width: 1 } });
    });
  }
  return slide;
}

// Cover: logo top-left, eyebrow, huge title, subtitle, tagline, optional badges, globe art right
function coverSlide(pres, { eyebrow, title, subtitle, tagline, image, badges = true, rings = false, confidential = "Confidential. Limited distribution under NDA." }) {
  const slide = _darkBase(pres, { rings });
  imageContain(slide, asset("logo-white.png"), { x: MX, y: 0.45, w: 2.1, h: 0.5, align: "left" });
  if (image) imageContain(slide, image, { x: 6.9, y: 0.75, w: 6.0, h: 5.6 });
  else console.warn("[ak] coverSlide without image. Pass image: await ak.coverArt(topic).");
  gradBar(slide, MX, 2.25, 0.55, 0.05);
  if (eyebrow) label(slide, eyebrow, { x: MX, y: 2.38, w: 6.5, color: C.periwinkle });
  warnIfOverflow("cover title", title, T.coverTitle, 6.6, 1.9);
  const tl = Math.min(2, estimateLines(title, T.coverTitle, 6.6));
  const th = tl * 0.85 + 0.1;
  text(slide, title, { x: MX, y: 2.75, w: 6.6, h: th, fontSize: T.coverTitle, bold: true, color: C.white, valign: "top", lineSpacingMultiple: 0.95 });
  let sy = 2.75 + th + 0.15;
  if (subtitle) { const sl = estimateLines(subtitle, 20, 6.4); text(slide, subtitle, { x: MX, y: sy, w: 6.4, h: sl * 0.38, fontSize: 20, color: C.white }); sy += sl * 0.38 + 0.08; }
  if (tagline) text(slide, tagline, { x: MX, y: sy, w: 6.4, h: Math.min(5.75 - sy, 0.7), fontSize: T.body, color: C.periwinkle });
  if (badges) {
    imageContain(slide, asset("g2-rating-badge-1.png"), { x: MX, y: 5.85, w: 1.0, h: 0.4, align: "left" });
    imageContain(slide, asset("g2-rating-badge-2.png"), { x: MX + 1.1, y: 5.85, w: 1.0, h: 0.4, align: "left" });
    imageContain(slide, asset("cloud-marketplaces.png"), { x: MX + 2.3, y: 5.85, w: 1.8, h: 0.4, align: "left" });
  }
  if (confidential) text(slide, confidential, { x: MX, y: 6.9, w: 6, h: 0.25, fontSize: T.footer, color: C.periwinkle });
  return slide;
}

// Section divider: "PART TWO" style
function sectionSlide(pres, { part, title, subtitle }) {
  const slide = _darkBase(pres);
  gradBar(slide, MX, 2.75, 0.55, 0.05);
  if (part) label(slide, part, { x: MX, y: 2.88, w: 6, color: C.periwinkle });
  text(slide, title, { x: MX, y: 3.2, w: 8, h: 1.0, fontSize: T.sectionTitle, bold: true, color: C.white, valign: "middle" });
  if (subtitle) text(slide, subtitle, { x: MX, y: 4.25, w: 6.8, h: 0.9, fontSize: 18, color: C.white });
  footer(slide, { dark: true, page: _page });
  return slide;
}


// Blue CTA button. Text is always white, bold, no underline. The link sits on a transparent
// image laid over the button rather than on the text, because PowerPoint recolours hyperlinked
// text with the theme link colour (blue on blue). Use this for every blue button.
const _CLEAR_PNG = "image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAAECAYAAACp8Z5+AAAADElEQVR4nGNgoBwAAABEAAHX40j9AAAAAElFTkSuQmCC";
function ctaButton(slide, { text: label, url, x, y, w = 2.9, h = 0.55, arrow = true, fill = C.blue }) {
  slide.addShape("roundRect", { x, y, w, h, fill: { color: fill }, line: { type: "none" }, rectRadius: h / 2 });
  slide.addText(label + (arrow ? "  \u2192" : ""), { x, y, w, h, fontFace: FONT, fontSize: 16, bold: true, color: C.white, align: "center", valign: "middle", margin: 0 });
  if (url) slide.addImage({ data: _CLEAR_PNG, x, y, w, h, transparency: 100, hyperlink: { url, tooltip: label } });
}

// Closing / CTA slide
function closingSlide(pres, { title = "See us in action", subtitle, cta, ctaUrl, email, certifications = true }) {
  const slide = _darkBase(pres, { rings: true });
  imageContain(slide, asset("logo-white.png"), { x: (W - 2.6) / 2, y: 1.05, w: 2.6, h: 0.6 });
  text(slide, title, { x: 1, y: 1.95, w: W - 2, h: 0.95, fontSize: 48, bold: true, color: C.white, align: "center", valign: "middle" });
  if (subtitle) text(slide, subtitle, { x: 1.5, y: 2.95, w: W - 3, h: 0.5, fontSize: 18, color: C.white, align: "center" });
  if (cta) ctaButton(slide, { text: cta, url: ctaUrl, x: (W - 2.9) / 2, y: 3.7, w: 2.9, h: 0.55 });
  if (email) text(slide, email, { x: 3, y: 4.4, w: W - 6, h: 0.4, fontSize: 16, bold: true, color: C.periwinkle, align: "center", hyperlink: { url: "mailto:" + email } });
  if (certifications) {
    label(slide, "Certified by", { x: 3, y: 5.15, w: W - 6, color: C.periwinkle, align: "center" });
    imageContain(slide, asset("certifications-strip.png"), { x: 3.4, y: 5.5, w: W - 6.8, h: 0.9 });
  }
  return slide;
}

// ---------------------------------------------------------------------------
// Composite layouts (cover most content). Each returns the slide.
// ---------------------------------------------------------------------------

// Grid of cards. items: [{ num?, icon?, label?, title, body?, bullets?, stat?, statColor? }]
// cols 2..4. Rows auto. Body 14pt floor. Max 8 items, 6 recommended.
async function cardGrid(slide, items, { cols = 3, top = slide.top, bottom = CONTENT_BOTTOM, gap = 0.28, accent = "gradient" } = {}) {
  if (items.length > 8) console.warn("[ak] cardGrid: more than 8 cards. Split across slides instead.");
  const rows = Math.ceil(items.length / cols);
  const w = (CW - gap * (cols - 1)) / cols;
  const h = (bottom - top - gap * (rows - 1)) / rows;
  const pad = 0.3;
  for (let i = 0; i < items.length; i++) {
    const it = items[i];
    const x = MX + (i % cols) * (w + gap);
    const y = top + Math.floor(i / cols) * (h + gap);
    card(slide, { x, y, w, h, accent: it.accent || accent });
    let cy = y + pad;
    if (it.icon) { await iconCircle(slide, it.icon, { x: x + pad, y: cy, d: 0.6 }); }
    if (it.stat) text(slide, it.stat, { x: x + pad, y: cy - 0.05, w: w - 2 * pad, h: 0.7, fontFace: FONT_LIGHT, fontSize: 36, color: it.statColor || C.red, align: "right", valign: "middle" });
    if (it.num) { text(slide, it.num, { x: x + pad, y: cy - 0.08, w: w - 2 * pad, h: 0.7, fontFace: FONT_LIGHT, fontSize: T.numeral, color: C.blue, valign: "middle" }); }
    if (it.icon || it.stat || it.num) cy += 0.78;
    if (it.label) {
      const ll = Math.min(2, estimateLines(String(it.label).toUpperCase(), T.label * 1.15, w - 2 * pad));
      label(slide, it.label, { x: x + pad, y: cy, w: w - 2 * pad, h: 0.24 * ll, color: it.labelColor || C.blue });
      cy += 0.24 * ll + 0.12;
    }
    warnIfOverflow(`card "${it.title}" title`, it.title, T.cardTitle, w - 2 * pad, 0.62);
    const titleLines = Math.min(2, estimateLines(it.title, T.cardTitle, w - 2 * pad));
    const th = titleLines * 0.31 + 0.05;
    text(slide, it.title, { x: x + pad, y: cy, w: w - 2 * pad, h: th, fontSize: T.cardTitle, bold: true, color: C.ink, valign: "top" });
    cy += th + 0.1;
    const remaining = y + h - pad - cy;
    if (it.body) { warnIfOverflow(`card "${it.title}" body`, it.body, T.body, w - 2 * pad, remaining); text(slide, it.body, { x: x + pad, y: cy, w: w - 2 * pad, h: remaining, color: C.muted }); }
    if (it.bullets) { warnIfOverflow(`card "${it.title}" bullets`, it.bullets.join("\n"), T.body, w - 2 * pad - 0.3, remaining); bullets(slide, it.bullets, { x: x + pad, y: cy, w: w - 2 * pad, h: remaining }); }
  }
  return slide;
}

// Row of big stats: [{ value, label, body? }]
function statRow(slide, stats, { top = slide.top, h = 2.0, cardStyle = true } = {}) {
  const n = stats.length, gap = 0.28;
  const w = (CW - gap * (n - 1)) / n;
  stats.forEach((st, i) => {
    const x = MX + i * (w + gap);
    if (cardStyle) card(slide, { x, y: top, w, h });
    text(slide, st.value, { x: x + 0.3, y: top + 0.2, w: w - 0.6, h: 0.8, fontFace: FONT_LIGHT, fontSize: T.numeral, color: st.color || C.blue, valign: "middle" });
    const ll = Math.min(2, estimateLines(String(st.label).toUpperCase(), T.label * 1.15, w - 0.6));
    label(slide, st.label, { x: x + 0.3, y: top + 1.0, w: w - 0.6, h: 0.24 * ll, color: C.ink });
    if (st.body) text(slide, st.body, { x: x + 0.3, y: top + 1.08 + 0.24 * ll, w: w - 0.6, h: h - 1.15 - 0.24 * ll, fontSize: T.body, color: C.muted });
  });
  return slide;
}

// Native table with brand styling. header: [..], rows: [[..]]. colW optional.
function table(slide, header, rows, { top = slide.top, colW, fontSize = T.body, headerFill = C.ink, highlightCol } = {}) {
  const head = header.map((h) => ({ text: String(h).toUpperCase(), options: { bold: true, color: C.white, fill: { color: headerFill }, fontSize: T.label, charSpacing: 2 } }));
  const body = rows.map((r, ri) => r.map((cell, ci) => ({
    text: String(cell),
    options: {
      color: ci === 0 ? C.ink : ci === highlightCol ? C.blue : C.body,
      bold: ci === 0 || ci === highlightCol,
      fill: { color: ri % 2 ? C.tintSoft : C.white },
    },
  })));
  slide.addTable([head, ...body], {
    x: MX, y: top, w: CW, colW, fontFace: FONT, fontSize, margin: [6, 10, 6, 10],
    border: { type: "solid", pt: 0.75, color: C.border }, valign: "middle", rowH: 0.48,
  });
  return slide;
}

// Two column: left narrative (big statement + bullets), right content box returned for you to fill
function splitLeft(slide, { heading, body, bullets: bl, top = slide.top, leftW = 4.6 }) {
  if (heading) text(slide, heading, { x: MX, y: top, w: leftW, h: 1.3, fontSize: 26, bold: true, color: C.blue, valign: "top" });
  let y = top + (heading ? 1.4 : 0);
  if (body) { text(slide, body, { x: MX, y, w: leftW, h: 1.0, color: C.muted }); y += 1.05; }
  if (bl) bullets(slide, bl, { x: MX, y, w: leftW, h: CONTENT_BOTTOM - y });
  return { x: MX + leftW + 0.5, y: top, w: CW - leftW - 0.5, h: CONTENT_BOTTOM - top };
}

// Numbered vertical timeline / steps on the right or full width
function steps(slide, items, { x = MX, y = slide.top, w = CW, h = CONTENT_BOTTOM - slide.top } = {}) {
  const n = items.length, rowH = h / n, d = 0.5;
  items.forEach((it, i) => {
    const yy = y + i * rowH;
    slide.addShape("ellipse", { x, y: yy, w: d, h: d, fill: { color: i === 0 ? C.blue : C.white }, line: { color: C.blue, width: 1.25 } });
    text(slide, String(i + 1).padStart(2, "0"), { x, y: yy, w: d, h: d, fontSize: 12, bold: true, color: i === 0 ? C.white : C.blue, align: "center", valign: "middle" });
    text(slide, it.title, { x: x + d + 0.25, y: yy - 0.02, w: w - d - 0.25, h: 0.34, fontSize: T.cardTitle - 1, bold: true, color: C.ink });
    if (it.body) text(slide, it.body, { x: x + d + 0.25, y: yy + 0.34, w: w - d - 0.25, h: rowH - 0.4, color: C.muted });
  });
  return slide;
}

// ---------------------------------------------------------------------------
// Finalize: write, then swap gradient token fills for native gradFill
// ---------------------------------------------------------------------------
async function finalize(pres, outFile) {
  const buf = await pres.write({ outputType: "nodebuffer" });
  const zip = await JSZip.loadAsync(buf);
  const grad = '<a:gradFill rotWithShape="1"><a:gsLst><a:gs pos="0"><a:srgbClr val="FF4646"/></a:gs><a:gs pos="100000"><a:srgbClr val="1040C5"/></a:gs></a:gsLst><a:lin ang="0" scaled="0"/></a:gradFill>';
  const re = new RegExp(`<a:solidFill><a:srgbClr val="${GRAD_TOKEN}"(?:/>|>.*?</a:srgbClr>)</a:solidFill>`, "g");
  let swaps = 0;
  for (const name of Object.keys(zip.files)) {
    if (!/^ppt\/slides\/slide\d+\.xml$/.test(name)) continue;
    const xml = await zip.file(name).async("string");
    const out = xml.replace(re, () => { swaps++; return grad; });
    if (out !== xml) zip.file(name, out);
  }
  const outBuf = await zip.generateAsync({ type: "nodebuffer", compression: "DEFLATE" });
  fs.mkdirSync(path.dirname(outFile), { recursive: true });
  fs.writeFileSync(outFile, outBuf);
  console.log(`[ak] wrote ${outFile} (${_page} slides, ${swaps} gradient fills)`);
  return outFile;
}

module.exports = {
  C, T, FONT, FONT_LIGHT, W, H, MX, CW, CONTENT_TOP, CONTENT_TOP_NOSUB, CONTENT_BOTTOM, GRAD_TOKEN,
  createDeck, contentSlide, coverSlide, sectionSlide, closingSlide, footer,
  card, gradBar, solidBar, label, text, bullets, callout, ctaButton,
  icon, iconCircle, iconPng, brandLogo, asset, imageContain, coverArt,
  cardGrid, statRow, table, splitLeft, steps,
  estimateLines, fits, warnIfOverflow, finalize,
};

// CLI: node ak.js --find shield cloud   -> lists matching icon names across sets
if (require.main === module && process.argv[2] === "--find") {
  const terms = process.argv.slice(3).map((t) => t.toLowerCase());
  for (const set of ["tb", "fa6", "si", "lu", "md"]) {
    let names = [];
    try { names = Object.keys(require(`react-icons/${set}`)); } catch (e) { continue; }
    const hits = names.filter((n) => terms.every((t) => n.toLowerCase().includes(t))).slice(0, 25);
    if (hits.length) console.log(`${set}: ` + hits.map((h) => `${set}:${h}`).join("  "));
  }
}
// CLI: node ak.js --logo azure   -> lists matching full colour brand logo names
if (require.main === module && process.argv[2] === "--logo") {
  const L = JSON.parse(fs.readFileSync(path.join(ASSETS, "brand-logos-iconify.json"), "utf8"));
  const t = process.argv.slice(3).map((x) => x.toLowerCase());
  console.log(Object.keys(L.icons).filter((n) => t.every((q) => n.includes(q))).slice(0, 40).join("  "));
}

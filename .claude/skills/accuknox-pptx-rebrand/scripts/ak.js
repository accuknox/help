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

// Schematic themes for technical buyers (CTOs, architects): hairlines, panels, one data accent,
// and diagrams on a faint dot grid. D holds the palette of the active theme, so build scripts use
// D.* and work in both. createDeck({ theme: "tech" }) is white (the default pick, approved
// 2026-10-29). createDeck({ theme: "deep" }) is the same system on ink.
const PALETTES = {
  tech: {
    bg: "FFFFFF", panel: "F7F9FE", line: "C9D4EA", lineSoft: "E3E9F5",
    text: "000025", body: "37474F", muted: "607D8B", sky: "1040C5", red: "D63637", onSky: "FFFFFF",
  },
  deep: {
    bg: "000025", panel: "070B33", line: "232D73", lineSoft: "151D57",
    text: "FFFFFF", body: "C3CDF0", muted: "8A96C8", sky: "4F9CF9", red: "FF6B6B", onSky: "000025",
  },
};
const D = Object.assign({}, PALETTES.tech);
// Template palette (doc-ppt-template _akdeck.py): NAVY 11206D is the cover and back cover,
// PURPLE 4D4DD9 marks chapter dividers in the "tech" theme.
const TEMPLATE_NAVY = "11206D";
const SECTION_ACCENT = "4D4DD9";

// Placeholder colour swapped for a native red->blue gradFill in finalize().
// Never use this hex for anything else.
const GRAD_TOKEN = "FE4647";

// Type scale (pt). Body floor is 14pt. Do not go below it for readable copy.
const T = {
  coverTitle: 54,
  sectionTitle: 48,
  title: 28,        // action titles run to two lines
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
// Inter Light is not installed on most machines, and PowerPoint swaps a missing face for Calibri.
// Big numerals use regular Inter, so the contrast comes from size, not weight.
const FONT_LIGHT = "Inter";

// Slide geometry (16:9, inches)
const W = 13.333, H = 7.5;
const MX = 0.6;                 // left/right margin
const CONTENT_TOP = 2.15;       // first y below header when subtitle present
const CONTENT_TOP_NOSUB = 1.75; // first y below header when no subtitle
const CONTENT_BOTTOM = 6.7;     // keep content above footer
const CW = W - 2 * MX;          // content width

let _page = 0;
// Async work (icon renders) started by sync helpers. finalize() awaits it before writing.
const _pending = [];
let _theme = "light";
const isDeep = () => _theme === "deep";
const isSchematic = () => _theme === "deep" || _theme === "tech";

// ---------------------------------------------------------------------------
// Deck
// ---------------------------------------------------------------------------
function createDeck({ title = "AccuKnox", author = "AccuKnox", theme = "light" } = {}) {
  _theme = theme;
  if (PALETTES[theme]) Object.assign(D, PALETTES[theme]);
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

// White card with thin border. A coloured top stripe on every card is a known AI deck tell, so the
// default is no accent. Pass accent only to mark the one card the slide is about.
// accent: "none" | "gradient" | "blue" | "red" | "ink"
function card(slide, { x, y, w, h, accent = "none", fill = C.white, border = C.border }) {
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

// Rough overflow check. Inter averages ~0.58em per character in mixed case (measured in a
// PowerPoint render, 2026-10-29). 0.53 matched Calibri, which is what a render shows when Inter
// failed to load, so a check tuned to it passes copy that overflows in real Inter.
function estimateLines(str, pt, wIn) {
  const charsPerLine = Math.max(1, Math.floor((wIn * 72) / (pt * 0.58)));
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
// Footer: logo, then the section name as quiet wayfinding (this replaces the eyebrow above the
// title), the NDA line, and the page number. A thin rule, not a heavy bar.
function footer(slide, { dark = false, page, section, confidential = "Confidential. Limited distribution under NDA." } = {}) {
  if (isDeep() && !dark) {
    slide.addShape("line", { x: MX, y: 6.86, w: CW, h: 0, line: { color: D.lineSoft, width: 0.75 } });
    imageContain(slide, asset("logo-white.png"), { x: MX, y: 6.98, w: 1.2, h: 0.24, align: "left" });
    if (section) text(slide, section, { x: MX + 1.45, y: 6.97, w: 4.2, h: 0.26, fontSize: T.footer, color: D.muted, valign: "middle" });
    if (confidential) text(slide, confidential, { x: 6.2, y: 6.97, w: 5.4, h: 0.26, fontSize: T.footer, color: D.muted, align: "right", valign: "middle" });
    if (page != null) text(slide, String(page), { x: W - MX - 0.5, y: 6.97, w: 0.5, h: 0.26, fontSize: T.footer, bold: true, color: D.text, align: "right", valign: "middle" });
    return;
  }
  if (!dark) {
    slide.addShape("line", { x: MX, y: 6.86, w: CW, h: 0, line: { color: C.border, width: 0.75 } });
    imageContain(slide, asset("logo-blue.png"), { x: MX, y: 6.98, w: 1.2, h: 0.24, align: "left" });
    if (section) text(slide, section, { x: MX + 1.45, y: 6.97, w: 4.2, h: 0.26, fontSize: T.footer, color: C.muted, valign: "middle" });
    if (confidential) text(slide, confidential, { x: 6.2, y: 6.97, w: 5.4, h: 0.26, fontSize: T.footer, color: C.muted, align: "right", valign: "middle" });
    if (page != null) text(slide, String(page), { x: W - MX - 0.5, y: 6.97, w: 0.5, h: 0.26, fontSize: T.footer, bold: true, color: C.ink, align: "right", valign: "middle" });
  } else if (page != null) {
    text(slide, String(page), { x: W - MX - 0.5, y: 6.97, w: 0.5, h: 0.26, fontSize: T.footer, color: C.periwinkle, align: "right", valign: "middle" });
  }
}

// Standard white content slide. The title is an action title: a full sentence that states the
// conclusion, up to two lines at 28pt. There is no eyebrow and no gradient tick by default, because
// a kicker above every title is a template tell. The section name lives in the footer instead.
// kicker: optional, only when the slide needs a label the title cannot carry (for example "Customer: Top 10 airline").
// source: optional source line set above the footer, for any number, quote or claim on the slide.
// Returns the slide, with slide.top as the first free y for content.
// Header strip (tech theme): pass `head`, a short headline of about 6 words, and `icon`, a
// Tabler outline icon that names the slide's subject. The head sits in white on an ink
// (#000025) strip with the brand gradient along its lower edge. `title` then becomes the
// takeaway sentence under the strip. Text boxes carry 25% slack, because a viewer without
// Inter swaps in a wider face and a tight box then collides with the next line.
function headSlide(pres, { head, icon: ic, title, kicker, section, source, notes, confidential }) {
  const slide = pres.addSlide();
  _page += 1;
  slide.background = { color: D.bg };
  const bandH = kicker ? 1.18 : 1.0;
  slide.addShape("rect", { x: 0, y: 0, w: W, h: bandH, fill: { color: C.ink }, line: { type: "none" } });
  gradBar(slide, 0, bandH - 0.05, W, 0.05);
  let tx = MX;
  if (ic) { _pending.push(icon(slide, ic, { x: MX, y: (bandH - 0.05) / 2 - 0.26 + (kicker ? 0.09 : 0), s: 0.52, color: "FFFFFF" })); tx = MX + 0.75; }
  if (kicker) label(slide, kicker, { x: tx, y: 0.16, w: W - tx - MX, h: 0.24, color: C.periwinkle, size: 10 });
  if (estimateLines(head, 26, W - tx - MX) > 1) console.warn(`[ak] head runs past one line: "${head}". Cut it.`);
  text(slide, head, { x: tx, y: kicker ? 0.4 : 0.12, w: W - tx - MX, h: kicker ? 0.66 : 0.76, fontSize: 26, bold: true, color: "FFFFFF", valign: "middle", fit: "shrink" });
  let y = bandH + 0.16;
  if (title) {
    // Reserve the lines the takeaway needs (the estimate is already wide-set), plus a gap
    // under it that can absorb one extra wrapped line from a fallback font.
    const lines = Math.min(3, estimateLines(title, 16, CW));
    const h = lines * 16 * 1.3 / 72 + 0.06;
    text(slide, title, { x: MX, y, w: CW, h, fontSize: 16, color: D.body, valign: "top" });
    y += h + 0.2;
  }
  if (source) text(slide, source, { x: MX, y: 6.5, w: CW, h: 0.26, fontSize: T.footer, color: D.muted, valign: "bottom" });
  footer(slide, { page: _page, section, confidential });
  if (notes) slide.addNotes(notes);
  slide.top = Math.max(y + 0.1, 1.75);
  slide.bottom = source ? 6.4 : CONTENT_BOTTOM;
  return slide;
}

function contentSlide(pres, opts = {}) {
  if (_theme === "tech" && opts.head) return headSlide(pres, opts);
  return _contentSlide(pres, opts);
}

function _contentSlide(pres, { title, subtitle, kicker, eyebrow, section, source, notes, confidential } = {}) {
  const slide = pres.addSlide();
  _page += 1;
  const deep = isSchematic();
  slide.background = { color: deep ? D.bg : C.white };
  if (eyebrow && !kicker) console.warn(`[ak] eyebrow "${eyebrow}" ignored. Put the section in section:, and use kicker: only when the title cannot carry the label.`);
  let y = 0.5;
  if (kicker) { label(slide, kicker, { x: MX, y, w: 9, h: 0.26, color: deep ? D.sky : C.blue }); y += 0.36; }
  const tSize = T.title;
  const tl = Math.min(2, estimateLines(title || "", tSize, CW));
  if (estimateLines(title || "", tSize, CW) > 2) console.warn(`[ak] title runs past two lines: "${String(title).slice(0, 60)}..." Cut it.`);
  const th = tl * tSize * 1.15 / 72 + 0.08;
  text(slide, title || "", { x: MX, y, w: CW, h: th, fontSize: tSize, bold: true, color: deep ? D.text : C.ink, valign: "top", lineSpacingMultiple: 0.98 });
  y += th + 0.12;
  if (subtitle) {
    const sl = Math.min(2, estimateLines(subtitle, T.subtitle, CW - 1));
    const sh = sl * T.subtitle * 1.3 / 72 + 0.04;
    text(slide, subtitle, { x: MX, y, w: CW - 1, h: sh, fontSize: T.subtitle, color: deep ? D.muted : C.muted, valign: "top" });
    y += sh + 0.1;
  }
  if (source) text(slide, source, { x: MX, y: 6.5, w: CW, h: 0.26, fontSize: T.footer, color: deep ? D.muted : C.muted, valign: "bottom" });
  footer(slide, { page: _page, section, confidential });
  if (notes) slide.addNotes(notes);
  slide.top = Math.max(y + 0.25, 1.5);
  slide.bottom = source ? 6.4 : CONTENT_BOTTOM;
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

// Cover, per the 2026-10-28 leadership rule: logo top left, then directly below it a small
// uppercase label for the asset type, an H1 of 2 to 4 words, and one deck line at most. Flat ink,
// no gradient, no rings, no badges, no footer text. One line art graphic in its own zone: the top
// right quarter (at most 45% of width, 40% of height), kept 0.5in clear of the text.
// The long claim goes on slide 2. `eyebrow` and `subtitle` are accepted as aliases of label and deck.
function coverSlide(pres, { label: kind, eyebrow, title, deck, subtitle, image }) {
  const slide = _darkBase(pres, { rings: false });
  kind = kind || eyebrow; deck = deck || subtitle;
  if (String(title).split(/\s+/).length > 4) console.warn(`[ak] cover title "${title}" runs past 4 words. Move the claim to slide 2.`);
  imageContain(slide, asset("logo-white.png"), { x: MX, y: 0.55, w: 2.0, h: 0.46, align: "left" });
  let y = 1.55;
  if (kind) { label(slide, kind, { x: MX, y, w: 6, h: 0.3, color: C.periwinkle }); y += 0.42; }
  const tl = Math.min(2, estimateLines(title, T.coverTitle, 6.2));
  const th = tl * T.coverTitle * 1.08 / 72 + 0.05;
  text(slide, title, { x: MX, y, w: 6.2, h: th, fontSize: T.coverTitle, bold: true, color: C.white, valign: "top", lineSpacingMultiple: 0.95 });
  y += th + 0.2;
  if (deck) text(slide, deck, { x: MX, y, w: 6.0, h: 0.8, fontSize: 20, color: C.periwinkle, valign: "top" });
  // Art zone: top right quarter, at most 0.45 W by 0.40 H, inside the margins.
  if (image) imageContain(slide, image, { x: W - MX - 0.45 * W, y: 0.55, w: 0.45 * W, h: 0.4 * H, align: "right" });
  return slide;
}

// Section divider: a large section number, the section name, and one line on the question the
// section answers. Flat ink, no rings. `part` is the number ("02"), not a "PART TWO" kicker.
// In the "tech" theme the divider is white: number in brand blue, title in ink, a hairline rule.
function sectionSlide(pres, { part, title, subtitle }) {
  if (_theme === "tech") {
    // Chapter break on brand ink (#000025), set by Atharva on 2026-10-29, between white content
    // slides. Title and subtitle boxes carry 25% slack so a fallback font cannot collide them.
    const slide = pres.addSlide();
    _page += 1;
    slide.background = { color: C.ink };
    if (part) text(slide, part, { x: MX, y: 1.3, w: 5, h: 1.3, fontSize: 80, color: C.periwinkle, valign: "bottom" });
    gradBar(slide, MX, 2.75, 1.4, 0.06);
    const tl = Math.min(2, Math.ceil(estimateLines(title, 44, 11.5) * 1.25));
    const th = tl * 44 * 1.12 / 72 + 0.1;
    text(slide, title, { x: MX, y: 2.95, w: 11.5, h: th, fontSize: 44, bold: true, color: C.white, valign: "top", lineSpacingMultiple: 0.95 });
    if (subtitle) text(slide, subtitle, { x: MX, y: 2.95 + th + 0.2, w: 9.5, h: 0.95, fontSize: 20, color: C.periwinkle, valign: "top" });
    imageContain(slide, asset("logo-white.png"), { x: MX, y: 6.98, w: 1.2, h: 0.24, align: "left" });
    text(slide, String(_page), { x: W - MX - 0.5, y: 6.97, w: 0.5, h: 0.26, fontSize: T.footer, bold: true, color: C.periwinkle, align: "right", valign: "middle" });
    slide.after = 2.95 + th + 0.2 + 1.0;
    return slide;
  }
  const slide = _darkBase(pres, { rings: false });
  if (part) text(slide, part, { x: MX, y: 1.6, w: 3, h: 1.2, fontSize: 72, color: C.blue, valign: "bottom" });
  text(slide, title, { x: MX, y: 2.95, w: 10, h: 1.0, fontSize: T.sectionTitle, bold: true, color: C.white, valign: "top" });
  if (subtitle) text(slide, subtitle, { x: MX, y: 4.05, w: 8, h: 0.9, fontSize: 20, color: C.periwinkle, valign: "top" });
  footer(slide, { dark: true, page: _page });
  return slide;
}

// Faint dot grid behind a diagram region (deep theme). One image, so the slide stays light to edit.
// Use it only under a schematic, never as a whole-slide texture.
async function dotGrid(slide, { x, y, w, h, step = 0.2, color = D.lineSoft }) {
  const ppi = 100, pw = Math.round(w * ppi), ph = Math.round(h * ppi), s = step * ppi;
  let dots = "";
  for (let yy = s / 2; yy < ph; yy += s) for (let xx = s / 2; xx < pw; xx += s) dots += `<circle cx="${xx.toFixed(1)}" cy="${yy.toFixed(1)}" r="1.1"/>`;
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="${pw}" height="${ph}"><g fill="#${color}">${dots}</g></svg>`;
  const buf = await require("sharp")(Buffer.from(svg)).png().toBuffer();
  slide.addImage({ data: "image/png;base64," + buf.toString("base64"), x, y, w, h });
}

// Outlined status pill, for maturity labels such as "GA", "In build", "R&D".
function pill(slide, str, { x, y, h = 0.28, color = D.sky, fill = null, size = 10 }) {
  const w = String(str).length * size * 0.72 / 72 + 0.3;
  slide.addShape("roundRect", { x, y, w, h, rectRadius: h / 2, fill: fill ? { color: fill } : { type: "none" }, line: { color, width: 1 } });
  slide.addText(String(str).toUpperCase(), { x, y, w, h, fontFace: FONT, fontSize: size, bold: true, color: fill ? D.onSky : color, charSpacing: 1.5, align: "center", valign: "middle", margin: 0 });
  return w;
}

// Small source line, for a slide whose source cannot use contentSlide's `source` option.
function sourceLine(slide, str, { y = 6.5 } = {}) {
  text(slide, str, { x: MX, y, w: CW, h: 0.26, fontSize: T.footer, color: C.muted, valign: "bottom" });
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
async function cardGrid(slide, items, { cols = 3, top = slide.top, bottom = slide.bottom || CONTENT_BOTTOM, gap = 0.28, accent = "none" } = {}) {
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
  await Promise.all(_pending.splice(0));
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
  C, D, T, FONT, FONT_LIGHT, W, H, MX, CW, CONTENT_TOP, CONTENT_TOP_NOSUB, CONTENT_BOTTOM, GRAD_TOKEN, dotGrid, pill,
  TEMPLATE_NAVY, SECTION_ACCENT,
  pageNo: () => _page, bumpPage: () => ++_page,
  // Sync-safe icon for sync slide code: queued, awaited by finalize().
  iconLater: (slide, name, o) => _pending.push(icon(slide, name, o)),
  createDeck, contentSlide, coverSlide, sectionSlide, closingSlide, footer,
  card, gradBar, solidBar, label, text, bullets, callout, ctaButton, sourceLine,
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

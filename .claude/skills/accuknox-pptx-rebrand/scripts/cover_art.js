// Created by: Claude Cowork
// Date: 2026-10-07
// Purpose: Topic based outline cover artwork for AccuKnox dark slides (SVG rendered to transparent PNG)
// Owner: AccuKnox Product Marketing
//
// Style: thin outline drawing on the ink background. Dashed outer contour with a blue to red
// gradient, solid inner contour, a fine purple network inside, one filled blue "control" node
// with a halo, and a red attack dot on a dashed path that a blue tick blocks at the boundary.
//
// Motifs: "ai" (shield + neural net), "cloud" (cloud + workload hex mesh, for CNAPP/CSPM/CWPP),
// "code" (brackets + pipeline, for ASPM/AppSec/supply chain), "network" (outline globe, for
// partner/global/company topics), "compliance" (document + checklist, for GRC/DPDP/audit),
// "runtime" (kernel layers + probe, for KubeArmor/eBPF/runtime).

const path = require("path");
const fs = require("fs");

const P = {
  blueTop: "#4B55E0",
  redBottom: "#E9466B",
  inner: "#3A3FA8",
  innerBottom: "#B8418A",
  net: "#5B45A8",
  node: "#9A4FB0",
  blue: "#1D4ED8",
  halo: "#3A3F9E",
  red: "#FF4646",
  tick: "#4E92E6",
  dot: "#4E92E6",
};

const defs = `
<defs>
  <linearGradient id="gOuter" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="${P.blueTop}"/><stop offset="1" stop-color="${P.redBottom}"/>
  </linearGradient>
  <linearGradient id="gInner" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="${P.inner}"/><stop offset="1" stop-color="${P.innerBottom}"/>
  </linearGradient>
</defs>`;

function wrap(body) {
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 460" width="1560" height="1380">${defs}${body}
  <circle cx="497" cy="16" r="4.5" fill="${P.dot}"/></svg>`;
}

// Attack path: red dot, dashed red line to a boundary point, blue tick crossing it
function attack(x0, y0, x1, y1, tickAngle = 60) {
  const a = (tickAngle * Math.PI) / 180, L = 17;
  return `
  <line x1="${x0}" y1="${y0}" x2="${x1}" y2="${y1}" stroke="${P.red}" stroke-width="1.2" stroke-dasharray="3 3" opacity="0.85"/>
  <circle cx="${x0}" cy="${y0}" r="6" fill="${P.red}"/>
  <line x1="${x1 - L * Math.cos(a)}" y1="${y1 - L * Math.sin(a)}" x2="${x1 + L * Math.cos(a)}" y2="${y1 + L * Math.sin(a)}" stroke="${P.tick}" stroke-width="2.6" stroke-linecap="round"/>`;
}

function controlNode(x, y) {
  return `<circle cx="${x}" cy="${y}" r="20" fill="none" stroke="${P.halo}" stroke-width="1.2"/>
  <circle cx="${x}" cy="${y}" r="10" fill="${P.blue}"/>`;
}

function mesh(nodes, edges, r = 7) {
  const lines = edges.map(([a, b]) => `<line x1="${nodes[a][0]}" y1="${nodes[a][1]}" x2="${nodes[b][0]}" y2="${nodes[b][1]}" stroke="${P.net}" stroke-width="0.8" opacity="0.75"/>`).join("");
  const dots = nodes.map(([x, y]) => `<circle cx="${x}" cy="${y}" r="${r}" fill="#000025" stroke="${P.node}" stroke-width="1.2"/>`).join("");
  return lines + dots;
}

function full(a, b) { const e = []; a.forEach((i) => b.forEach((j) => e.push([i, j]))); return e; }

// ---------------------------------------------------------------- motifs
function ai() {
  const outer = "M189 68 L344 18 L499 68 L499 210 C499 320 420 380 344 405 C268 380 189 320 189 210 Z";
  const inner = "M218 90 L344 48 L470 90 L470 205 C470 300 405 350 344 374 C283 350 218 300 218 205 Z";
  const n = [[313, 107], [252, 138], [313, 168], [374, 138], [252, 199], [313, 229], [374, 199], [252, 260], [374, 260], [313, 291], [435, 199]];
  // layers: L0 = 1,4,7 ; L1 = 0,2,5,9 ; L2 = 3,6,8 ; out = 10
  const e = [...full([1, 4, 7], [0, 2, 5, 9]), ...full([0, 2, 5, 9], [3, 6, 8]), [3, 10], [6, 10], [8, 10]];
  return wrap(`
  <path d="${outer}" fill="none" stroke="url(#gOuter)" stroke-width="1.3" stroke-dasharray="5 4"/>
  <path d="${inner}" fill="none" stroke="url(#gInner)" stroke-width="1.3"/>
  ${mesh(n.slice(0, 10), e.filter(([a, b]) => a < 10 && b < 10))}
  ${e.filter(([a, b]) => b === 10).map(([a]) => `<line x1="${n[a][0]}" y1="${n[a][1]}" x2="415" y2="199" stroke="${P.net}" stroke-width="0.8" opacity="0.75"/>`).join("")}
  ${controlNode(435, 199)}
  ${attack(130, 362, 228, 318)}`);
}

function cloud() {
  const outer = "M170 330 C110 330 100 250 160 236 C150 170 230 140 270 180 C290 100 410 90 440 170 C510 170 520 260 470 290 C490 330 450 345 420 330 Z";
  const inner = "M190 305 C145 305 140 252 182 244 C176 196 236 176 268 206 C285 146 386 136 410 196 C466 196 476 262 438 280 C452 306 430 316 410 305 Z";
  // hex mesh of workloads
  const n = [[280, 220], [330, 205], [380, 220], [255, 260], [305, 250], [355, 250], [405, 262], [280, 290], [330, 288], [380, 290]];
  const e = [[0, 1], [1, 2], [0, 3], [0, 4], [1, 4], [1, 5], [2, 5], [2, 6], [3, 4], [4, 5], [5, 6], [3, 7], [4, 7], [4, 8], [5, 8], [5, 9], [6, 9], [7, 8], [8, 9]];
  const hex = (x, y, r = 9) => {
    const pts = [...Array(6)].map((_, i) => { const a = Math.PI / 3 * i + Math.PI / 6; return `${x + r * Math.cos(a)},${y + r * Math.sin(a)}`; }).join(" ");
    return `<polygon points="${pts}" fill="#000025" stroke="${P.node}" stroke-width="1.2"/>`;
  };
  const lines = e.map(([a, b]) => `<line x1="${n[a][0]}" y1="${n[a][1]}" x2="${n[b][0]}" y2="${n[b][1]}" stroke="${P.net}" stroke-width="0.8" opacity="0.75"/>`).join("");
  return wrap(`
  <path d="${outer}" fill="none" stroke="url(#gOuter)" stroke-width="1.3" stroke-dasharray="5 4"/>
  <path d="${inner}" fill="none" stroke="url(#gInner)" stroke-width="1.3"/>
  ${lines}${n.map(([x, y]) => hex(x, y)).join("")}
  <line x1="330" y1="288" x2="330" y2="395" stroke="${P.net}" stroke-width="0.8" stroke-dasharray="2 3"/>
  ${controlNode(330, 405)}
  ${attack(95, 400, 182, 322, 50)}`);
}

function code() {
  const outer = "M260 40 L200 40 C180 40 175 55 175 75 L175 180 C175 205 160 215 140 220 C160 225 175 235 175 260 L175 365 C175 385 180 400 200 400 L260 400";
  const outerR = "M380 40 L440 40 C460 40 465 55 465 75 L465 180 C465 205 480 215 500 220 C480 225 465 235 465 260 L465 365 C465 385 460 400 440 400 L380 400";
  const n = [[230, 120], [285, 120], [340, 120], [395, 120], [230, 220], [285, 220], [340, 220], [230, 320], [285, 320], [340, 320], [395, 320]];
  const e = [[0, 1], [1, 2], [2, 3], [0, 4], [1, 5], [2, 6], [4, 5], [5, 6], [4, 7], [5, 8], [6, 9], [7, 8], [8, 9], [9, 10], [3, 6], [6, 10]];
  return wrap(`
  <path d="${outer}" fill="none" stroke="url(#gOuter)" stroke-width="1.3" stroke-dasharray="5 4"/>
  <path d="${outerR}" fill="none" stroke="url(#gOuter)" stroke-width="1.3" stroke-dasharray="5 4"/>
  <rect x="205" y="85" width="230" height="270" rx="14" fill="none" stroke="url(#gInner)" stroke-width="1.3"/>
  ${mesh(n, e)}
  <line x1="340" y1="220" x2="410" y2="220" stroke="${P.net}" stroke-width="0.8" opacity="0.75"/>
  ${controlNode(415, 220)}
  ${attack(70, 380, 175, 330, 60)}`);
}

function network() {
  const cx = 335, cy = 215;
  const meridians = [0.35, 0.7].map((k) => `<ellipse cx="${cx}" cy="${cy}" rx="${150 * k}" ry="150" fill="none" stroke="url(#gInner)" stroke-width="1"/>`).join("");
  const parallels = [-90, -45, 0, 45, 90].map((dy) => { const rx = Math.sqrt(150 * 150 - dy * dy); return `<ellipse cx="${cx}" cy="${cy + dy}" rx="${rx}" ry="${rx * 0.12}" fill="none" stroke="${P.net}" stroke-width="0.8" opacity="0.7"/>`; }).join("");
  const n = [[260, 120], [360, 100], [420, 160], [230, 210], [320, 190], [400, 240], [270, 290], [360, 300], [300, 345]];
  const e = [[0, 1], [1, 2], [0, 4], [1, 4], [2, 5], [3, 4], [4, 5], [3, 6], [4, 6], [4, 7], [5, 7], [6, 8], [7, 8]];
  return wrap(`
  <circle cx="${cx}" cy="${cy}" r="180" fill="none" stroke="url(#gOuter)" stroke-width="1.3" stroke-dasharray="5 4"/>
  <circle cx="${cx}" cy="${cy}" r="150" fill="none" stroke="url(#gInner)" stroke-width="1.3"/>
  ${meridians}${parallels}
  ${mesh(n, e, 6)}
  <line x1="400" y1="240" x2="455" y2="215" stroke="${P.net}" stroke-width="0.8"/>
  ${controlNode(460, 212)}
  ${attack(95, 390, 205, 330, 55)}`);
}

function compliance() {
  const outer = "M210 30 L420 30 L480 90 L480 410 L210 410 Z";
  const inner = "M235 60 L405 60 L452 107 L452 382 L235 382 Z";
  const rows = [120, 175, 230, 285].map((y, i) => `
    <rect x="262" y="${y - 11}" width="22" height="22" rx="4" fill="#000025" stroke="${P.node}" stroke-width="1.2"/>
    ${i < 3 ? `<path d="M267 ${y} l5 5 l9 -11" fill="none" stroke="${P.tick}" stroke-width="2"/>` : ""}
    <line x1="300" y1="${y}" x2="${i % 2 ? 380 : 410}" y2="${y}" stroke="${P.net}" stroke-width="1.2"/>`).join("");
  return wrap(`
  <path d="${outer}" fill="none" stroke="url(#gOuter)" stroke-width="1.3" stroke-dasharray="5 4"/>
  <path d="${inner}" fill="none" stroke="url(#gInner)" stroke-width="1.3"/>
  <path d="M405 60 L405 107 L452 107" fill="none" stroke="url(#gInner)" stroke-width="1.1"/>
  ${rows}
  <line x1="300" y1="340" x2="370" y2="340" stroke="${P.net}" stroke-width="0.8"/>
  ${controlNode(395, 340)}
  ${attack(110, 380, 210, 330, 60)}`);
}

function runtime() {
  const layers = [90, 160, 230, 300].map((y, i) => `<rect x="${200 + i * 0}" y="${y}" width="280" height="50" rx="8" fill="none" stroke="url(#gInner)" stroke-width="1.2"/>`).join("");
  const n = [[245, 115], [300, 115], [355, 115], [410, 115], [270, 185], [340, 185], [410, 185], [245, 255], [320, 255], [395, 255]];
  const e = [[0, 4], [1, 4], [2, 5], [3, 6], [4, 7], [4, 8], [5, 8], [6, 9], [5, 9]];
  return wrap(`
  <rect x="175" y="60" width="330" height="320" rx="18" fill="none" stroke="url(#gOuter)" stroke-width="1.3" stroke-dasharray="5 4"/>
  ${layers}
  ${mesh(n, e)}
  <line x1="320" y1="255" x2="340" y2="318" stroke="${P.net}" stroke-width="0.8"/>
  ${controlNode(340, 325)}
  ${attack(80, 390, 175, 340, 60)}`);
}

const MOTIFS = { ai, cloud, code, network, compliance, runtime };

// Map free text topics to a motif
function pickMotif(topic = "") {
  const t = topic.toLowerCase();
  if (/\b(ai|llm|model|agent|genai|ml|prompt|red team)/.test(t)) return "ai";
  if (/(cnapp|cspm|cwpp|kspm|cloud|kubernetes|k8s|container|ciem|cdr)/.test(t)) return "cloud";
  if (/(aspm|appsec|application|code|sast|sbom|supply chain|devsecops|pipeline|api)/.test(t)) return "code";
  if (/(compliance|grc|dpdp|rbi|audit|nist|soc ?2|hipaa|regulat)/.test(t)) return "compliance";
  if (/(runtime|kubearmor|ebpf|lsm|kernel|zero trust)/.test(t)) return "runtime";
  return "network";
}

async function coverArtPng(motifOrTopic, outDir) {
  const motif = MOTIFS[motifOrTopic] ? motifOrTopic : pickMotif(motifOrTopic);
  const sharp = require("sharp");
  const svg = MOTIFS[motif]();
  const dir = outDir || path.join(require("os").tmpdir(), "ak-cover-art");
  fs.mkdirSync(dir, { recursive: true });
  const out = path.join(dir, `cover-${motif}.png`);
  await sharp(Buffer.from(svg)).png().toFile(out);
  return out;
}

module.exports = { coverArtPng, pickMotif, MOTIFS };

if (require.main === module) {
  (async () => {
    const dir = process.argv[2] || ".";
    for (const m of Object.keys(MOTIFS)) console.log(await coverArtPng(m, dir));
  })();
}

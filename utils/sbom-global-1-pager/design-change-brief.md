# SBOM One-Pager — Global/Japan Variant: Designer Change Brief

Source file: `SBOM-1-Pager.pdf` (India BFSI version, single tall page, 595x1180pt).
Goal: a global variant that doesn't read as India-market collateral and is easy
for a non-technical executive to read in one pass. Keep the same layout system,
brand colors, and card structure. Changes below are section by section, top to
bottom.

**Brand to carry over:** Navy `#11206D`, accent blue (bright blue used on
headings/numerals in the source PDF), Space Grotesk for headings/labels, Inter
for body. Don't introduce new colors or fonts.

---

## 1. Hero title

**Current:** "AccuKnox Software Bill of Materials (SBOM)"
**Change:** None. Product name, not India-specific.

---

## 2. Subhead + "Now Mandated By" regulator badge strip

**Current:** Headline "Complete X-BOM for Indian BFSI." Body copy: "RBI, SEBI,
and CERT-In have made Bill of Materials practices mandatory across banks,
NBFCs, mutual funds, and all regulated financial entities." Four badge tiles:
CERT-In v2.0, SEBI CSCRF, RBI Circular, IRDAI Guidelines (each with its own
logo image and a one-line date/scope caption).

**Problem:** Every element here is India-regulation-specific and uses
acronyms a Japanese or global exec won't recognize (CERT-In, SEBI, CSCRF,
NBFC, IRDAI).

**Change:**
- Delete the four regulator badge images and captions entirely.
- Replace the headline with a market-neutral version, e.g. "Complete X-BOM
  for Regulated Enterprises" or "Complete Software Bill of Materials, One
  Platform."
- Replace the body copy so it doesn't name a single country's regulators.
  Suggested direction: reference the global drivers instead (US Executive
  Order 14028 / NIST SSDF, EU Cyber Resilience Act) or keep it generic:
  "SBOM and software supply chain transparency are increasingly required by
  regulators and enterprise procurement worldwide. AccuKnox generates SBOM,
  CBOM, QBOM, HBOM, and AIBOM from a single Zero Trust CNAPP, no separate
  tooling required." Flag to marketing to confirm which global regulation
  (if any) to name.

---

## 3. "Five BOM Types · One Platform" (5 cards: SBOM/CBOM/QBOM/HBOM/AIBOM)

**Current:** Generic product cards, each acronym spelled out underneath
(SOFTWARE, CRYPTOGRAPHIC, QUANTUM, HARDWARE, AI/ML).

**Change:** None needed, not India-specific. This card already does the
right thing (acronym + plain-English label under it) — keep using that
pattern anywhere else an acronym survives the edit.

---

## 4. Stats row (20+ Languages / 50+ Package Managers / N-level Transitive
Dependencies / CycloneDX + SPDX 3.0.1 Output Formats)

**This is the row flagged in the screenshot you sent.**

**Problem:** Dense with acronyms and standard names (CycloneDX, SPDX 3.0.1,
"N-level transitive") that mean nothing to an executive reader on a first
pass.

**Change:** Remove this row from the global one-pager. If the underlying
numbers are worth keeping for a more technical audience, they belong in a
deeper-in-the-funnel technical datasheet, not the executive one-pager.

---

## 5. "Cert-in v2.0 Compliance" section (title + 8-item checklist)

**Current:** Section titled "Cert-in v2.0 Compliance," subhead "Technical
Guidelines on SBOM · CBOM · QBOM · AIBOM · HBOM," body para naming
"government bodies, essential services, software exporters, and the
financial sector" and "VEX disclosures." Below it, an 8-item checklist:
Package vulnerability scanning; VEX and CSAF vulnerability disclosures;
Audit-ready reports (email & PDF); License compliance & copyleft detection;
Managed & unmanaged AI asset inventory; Cryptographic asset inventory
(CBOM); BOM version diff (added/removed/changed); CycloneDX + SPDX 3.0.1
output.

**Problem:** The whole section is branded around one India regulation
(CERT-In). "VEX" and "CSAF" are also unexplained acronyms.

**Change:**
- Delete the "Cert-in v2.0 Compliance" title and the India-regulation body
  paragraph.
- Rename the section to something vendor/region-neutral, e.g.
  "Compliance-Ready Coverage" or "Built for the Audit."
- Keep the 8-item checklist, it's a solid vendor-neutral feature list. Just
  clean up two lines: expand "VEX and CSAF" to something like "Vulnerability
  disclosure (VEX/CSAF format)" and keep "CycloneDX + SPDX 3.0.1" as-is since
  those are the two standard SBOM formats globally, security buyers will
  recognize them even if a pure business exec doesn't.

---

## 6. Platform Capabilities (6 cards)

**Current cards:** Vulnerability Scanning on Packages; Audit-Ready
Reporting; Managed & Unmanaged AI Assets; BOM Version Comparison; Dependency
Graph Visualization; Cryptographic Asset Inventory.

**Problem:** The "Audit-Ready Reporting" card body says "structured for RBI
and SEBI audit workflows" — India-specific. A few other cards lean on raw
acronyms (CVE, NVD, OSV, x.509) with no explainer.

**Change:**
- Edit "Audit-Ready Reporting" body: remove "structured for RBI and SEBI
  audit workflows," replace with "structured for internal and regulatory
  audit workflows."
- Optional, for readability: soften "CVE, NVD, and OSV vulnerability
  databases" to "global vulnerability databases," since the point (real-time
  correlation) survives without naming all three feeds.
- No other structural change, titles and the rest of the copy are fine.

---

## 7. Deployment Models (SaaS / On-Premises / Hybrid / Air-Gapped)

**Current:** No India references. "Air-Gapped" card mentions "KnoxCtl CLI."

**Change:** None required. Optional polish: spell out once that KnoxCtl is
AccuKnox's own CLI tool, since it's a proprietary name a first-time reader
won't recognize.

---

## 8. "Proudly Built in India · Atma Nirbhar Bharat" badge band

**Current:** Headline "Proudly Built in India · Atma Nirbhar Bharat" with an
Indian flag icon to its left. Body: "Founded with SRI International.
KubeArmor, our CNCF open-source project, powers the runtime security engine
with 1M+ downloads across 25+ enterprise adopters, supporting Digital India
and Make in India." Badge tiles: CNCF Project, 1M+ Downloads, SRI
International, 25+ Adopters.

**Problem:** This is the section you called out directly, it's a national
pride line ("Atma Nirbhar Bharat" = a Government of India self-reliance
campaign) plus a flag icon plus "Digital India and Make in India," which is
the opposite of the perception you want in Japan.

**Change:**
- Delete the headline, the flag icon, and the "Digital India and Make in
  India" clause.
- Keep the four credibility badges (CNCF Project, 1M+ Downloads, SRI
  International, 25+ Adopters) — these are genuinely global credibility
  markers. SRI International in particular is a US research institute, so
  this section can lean into that instead of India origin.
- Suggested replacement headline: "Built on CNCF Open Source · Founded with
  SRI International." Suggested body: "KubeArmor, our CNCF open-source
  project, powers the runtime security engine with 1M+ downloads across 25+
  enterprise adopters."
- Separately, flag to marketing/legal whether the global variant should
  state a US headquarters line explicitly (e.g. "Headquartered in
  [city], USA"). That's a positioning call above the designer's scope, don't
  guess at it in layout, leave a placeholder if the copy isn't finalized.

---

## 9. Footer: "About AccuKnox"

**Current:** "AccuKnox is a Zero Trust CNAPP. Cloud Security protects API
Security, CDR, SIEM, Kubernetes, VMs, Bare metals, IoT Edge, and 5G
security." Plus linkedin.com/accuknox and @AccuKnox.

**Problem:** Not India-specific, but it's an acronym wall (CNAPP, CDR, SIEM)
with no plain-English translation, which cuts against the "easy for an
executive to read" goal.

**Change:** Rewrite in plain language, e.g. "AccuKnox is a Zero Trust cloud
security platform (CNAPP) that protects clouds, containers, Kubernetes, VMs,
bare metal, IoT edge, and 5G workloads from a single console." Spell out
CNAPP on first use since it's the one acronym in AccuKnox's own category
name.

---

## Cross-cutting notes for the designer

- **Acronym pass:** every acronym that survives into the global version
  should be spelled out once, near its first appearance, the way the BOM
  cards already do (acronym + plain label underneath). Candidates still
  needing this: CNAPP, CDR, SIEM, VEX/CSAF.
- **Images to remove:** the 4 regulator logo images in section 2 (CERT-In,
  SEBI, RBI, IRDAI), and the India flag icon in section 8.
- **Images to keep:** CNCF logo, SRI International logo (both in section 8).
- **No new country-of-origin cue** should replace the India framing unless
  marketing explicitly signs off on a "headquartered in the US" line, leave
  that decision to them rather than picking a flag or claim during layout.

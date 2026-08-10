# Platform Page Rebuild, Update Plan

**Target URL:** https://accuknox.com/platform
**Owner:** Anish (design + build)
**Prepared:** 10 Aug 2026

**Companion files in this folder**

| File | What it is |
|---|---|
| `platform-page-update-plan.md` | This file. What changes, why, section spec, image manifest, open questions. |
| `platform-page-content.md` | Final copy, section by section, ready to paste into Claude Design. |
| `platform-page-prototype.html` | Working single-file HTML prototype of the new page. |

**Sources used**

1. Live DOM of `accuknox.com` homepage, including all 6 hero tab panels and all 10 panels of the tabbed showcase, plus the full header mega menu (the definitive product taxonomy).
2. Live DOM of the current `accuknox.com/platform`.
3. `CNAPP Micro Deck | AUG 2026` (36 slides) with speaker notes.
4. `AccuKnox Security Maturity Phases` (19 slides), the Phase I/II/III source.
5. `AccuKnox CISO's Presentation, May 2026` (40 slides), the 12-module feature source.
6. `utils/content-planning/platform-pages-content-plan.md`, the earlier per-module gap analysis.
7. `utils/brian-demo-screenshots/DEMO-SUMMARY.md`, 22 captioned product screenshots.

---

## 1. The problem in one paragraph

The current `/platform` page sells a 2023 product. It frames AccuKnox as "AppSec + CloudSec", shows four tabs (Application Security, Cloud Security, Runtime Security, K8s Security), and never mentions AI Security, Agentic AI, API Security, Data Security, SBOM, Secrets Manager, SIEM, CDR, CIEM, or GRC. The homepage already sells all twelve. So the deepest page in the funnel is the shallowest page on the site, and a buyer who clicks "Platform" from the nav sees less than they saw on the homepage they just left.

Three specific failures:

1. **Taxonomy mismatch.** The mega menu lists 30+ product entries across six groups. The platform page acknowledges four.
2. **No showcase.** The homepage has a 10-tab product showcase with real dashboard screenshots and per-module CTAs. The platform page has static pain-point text and stock imagery.
3. **No differentiation.** The single strongest claim in every deck, that AccuKnox blocks the syscall in the kernel while competitors alert after the fact, appears nowhere on the page.

---

## 2. What to keep, change, and remove

### Keep

| Element | Why | Change needed |
|---|---|---|
| Press and analyst logo marquee | Real proof | Move from near-top to the proof band near the bottom |
| Product Tour embed | Converts | Keep, move up to sit under the showcase |
| "Start with AccuKnox in 3 Steps" | Clear next step | Rewrite with the 3-week POC timeline from the micro deck |
| Testimonial carousel | Real names, real titles | Deduplicate. It currently renders twice |
| Platform FAQs | SEO value | Expand from 5 to 10, cover AI, API, air-gapped, and runtime |
| Gated eBook block | Lead capture | Swap the 2025 AppSec+CloudSec guide for the Zero Trust CNAPP Definitive Guide |

### Change

| Element | Current | New |
|---|---|---|
| Hero | "Why Do Security Breaches Always Seem One Step Ahead?" with no product in it | Platform-first headline plus a stat strip. See content file, Section 1 |
| AppSec / CloudSec two-box | Two boxes covering six acronyms | Six domain tabs matching the homepage hero, covering all twelve modules |
| 4-tab pain-point block | Static text, one stock image per tab | The 12-tab product showcase with real dashboards and carousels |
| "What's New in the security Portfolio" (IoT/Edge, 5G) | Presented as new, both are years old | Fold into a "Specialized environments" strip with Nutanix, OpenShift, VMware, edge, 5G, air-gapped |
| "Let AccuKnox perform impact analysis" paragraph | Vague, uses "50+ tooling" once | Replace with the consolidation and TCO band carrying real numbers |

### Remove

1. The hero rhetorical question. It asks the reader to agree with a premise instead of telling them what the product is.
2. The duplicated testimonial carousel block.
3. The "AccuKnox is the top CNAPP Security Pick" banner above the fold. Same content lives in the proof band.
4. The lone James Berthoty quote sitting inside a product tab. Quotes belong in the proof band, not inside a feature panel.

---

## 3. New page structure

Eighteen sections. Sections 2 and 5 are the two tabbed components, and section 5 is the centerpiece the brief asks for.

| # | Section | Component type | Primary source |
|---|---|---|---|
| 1 | Hero, headline plus stat strip | Static | Micro deck S1, S17 |
| 2 | Six domain tabs | Tabbed, mirrors homepage hero | Homepage hero panels |
| 3 | Code to Cognition architecture | Single large diagram | Maturity deck S2, CISO deck S4 |
| 4 | Twelve modules by what they solve | Card grid | Micro deck S5 |
| 5 | **Platform showcase, 12 tabs** | **Tabbed plus carousel** | **Homepage showcase pattern plus CISO deck S14 to S25** |
| 6 | Runtime as a lens vs runtime as a shield | Two-column compare | Micro deck S25 |
| 7 | Runtime at every layer, L1 to L4 | Four-row stack diagram | Micro deck S19 |
| 8 | Security maturity phases | Tabbed matrix, 5 tracks x 3 phases | Maturity deck S9, S12, S15, S16, S17 |
| 9 | Runtime security journey, 8 steps | Horizontal stepper | Micro deck S15 |
| 10 | Deploy anywhere, 4 models | Icon row plus coverage table | Micro deck S13, S31 |
| 11 | Secure across every infrastructure | Five-column table | Homepage section |
| 12 | Compliance, 45+ frameworks | Logo grid plus metrics | Micro deck S30 |
| 13 | Consolidation and TCO | Logo replacement grid plus stats | CISO deck S38 |
| 14 | Stack ranking vs competitors | Comparison table | CISO deck S36 |
| 15 | Integrations, 50+ | Category grid | Homepage plus micro deck S14 |
| 16 | Open source | Three cards | Mega menu |
| 17 | Proof band, analysts, patents, customers | Mixed | Micro deck S3, S32, S33 |
| 18 | POC in three weeks plus FAQs plus CTA | Stepper plus accordion | Micro deck S34 |

### Why section 5 carries the page

The homepage showcase already works: a left-to-right icon nav, one panel per module, a headline, a support stat, a screenshot carousel, and an "Explore X" button. Buyers land on `/platform` expecting the same interaction at more depth. The platform version keeps the identical shell and adds two things per panel: a four-bullet capability list, and a link into the matching help doc. Reusing the component means Anish builds nothing new, only extends the panel template and adds two tabs.

The homepage has 10 tabs. The platform page gets 12, matching the 12 modules in the deck.

| # | Tab | Homepage has it | Screenshots exist |
|---|---|---|---|
| 1 | Cloud Security (CSPM) | Yes | Yes, CSPM1 to CSPM4 |
| 2 | Workload Security (CWPP) | Yes | Yes, CWPP1 to CWPP4 |
| 3 | Kubernetes Security (KSPM) | Yes | Yes, KSPM1 to KSPM4 |
| 4 | Application Security (ASPM) | Yes | Yes, ASPM1 to ASPM4 |
| 5 | API Security | Yes | Yes, api1 to api3 |
| 6 | AI Security (AI-SPM) | Yes | Yes, AI-SPM1 to AI-SPM6 |
| 7 | Agentic AI Security | **No, new** | **No. Needs capture** |
| 8 | Data Security (DSPM) | Yes | Yes, 4 DSPM shots |
| 9 | Supply Chain (SBOM) | Yes | Yes, SBOM1 to SBOM4 |
| 10 | Secrets Manager | Yes | Yes, 2 shots |
| 11 | Cloud Detection & Response (CDR) | **No, new** | **No. Needs capture** |
| 12 | Compliance and GRC | Yes | Yes, COMPLIANCE1 to 3 |

SIEM, CIEM, and CTEM stay off the tab bar and appear as a "Also on the platform" row below it, because CIEM and CTEM are Beta and SIEM has no dashboard imagery yet. Putting a Beta module on the main showcase invites a demo request the product cannot fully answer.

---

## 4. Image manifest

### 4a. Already produced, hot-linkable, matches brand

These are live on accuknox.com and used by the homepage showcase. The prototype references them directly so the page renders immediately. Base path is `https://accuknox.com/wp-content/uploads/`.

| Tab | Files |
|---|---|
| CSPM | `CSPM1-dashboard-home.webp` … `CSPM4-dashboard-home.webp`, `public-cloud-support-home.webp` |
| ASPM | `ASPM1-dashboard-home.webp`, `ASPM2`, `ASPM4`, `cicd-platform-support-home.webp` |
| AI-SPM | `AI-SPM1-dashboard-home.webp` … `AI-SPM6-dashboard-home.webp`, `ai-llm-logos-home.webp` |
| API | `api1-dashboard-home.webp` … `api3-dashboard-home.webp`, `api-sec-logos-home.webp` |
| CWPP | `CWPP1-dashboard-home.webp` … `CWPP4-dashboard-home.webp`, `k8-engines-support-home.webp` |
| SBOM | `SBOM1-dashboard-home.webp` … `SBOM4-dashboard-home.webp`, `sbom-support-home.webp` |
| KSPM | `KSPM1-dashboard-home.webp` … `KSPM4-dashboard-home.webp` |
| DSPM | `DSPM1-dashboard-home.webp`, `Onboarding-Data-Source-Connection-dashboard-dspm.webp`, `Access-Review-dashboard-dspm.webp`, `Remediation-dashboard-dspm.webp`, `dspm-support-home.webp` |
| Secrets | `secrets-manager-dashboard-home.webp`, `secrets-manager-1-dashboard-home.webp`, `hashicorp-logo-home.webp` |
| Compliance | `COMPLIANCE1-dashboard-home.webp` … `COMPLIANCE3-dashboard-home.webp`, `integrated-compliance-frameworks-home.webp` |
| Domain tab icons | `ASPM-nav-icon.svg`, `CSPM-nav-icon.svg`, `CDR-nav-icon.svg`, `DSPM-nav-icon.svg`, `api-sec-nav-icon.svg`, `sbom-nav-icon.svg`, `siem-nav-icon.svg`, `secrets-nav-icon.svg`, `ai-soc-nav-icon.svg`, `CTEM-nav-icon-1.svg`, `CIEM-nav-icon.svg`, `agent-builder-nav-icon.svg`, `mcp-server-nav-icon.svg` |

### 4b. In the repo, needs cropping before use

From `utils/brian-demo-screenshots/`. Crop browser chrome and dead whitespace per the asset-kit rules.

| File | Use it for |
|---|---|
| `01-main-dashboard-overview.png` | Section 3 or the CDR tab |
| `10-ask-ai-copilot-remediation.png` | AI Copilot callout in section 4 |
| `12-rules-engine-custom-rules.png` | CDR tab, automation slide |
| `13-compliance-frameworks-list.png` | Compliance tab, slide 1 |
| `14-hipaa-compliance-detail-view.png` | Compliance tab, slide 2 |
| `16-ai-pipeline-topology.png` | AI-SPM tab, pipeline visibility |
| `17-ai-red-teaming-risks.png` | AI-SPM tab, red teaming |
| `18-prompt-firewall-policy-config.png` | AI-SPM tab, guardrails |
| `20-runtime-protection-policy-activation.png` | CWPP tab |
| `21-zero-trust-policy-discovery.png` | Section 9, runtime journey |
| `22-application-behavior-monitoring.png` | CWPP tab, app behavior |

### 4c. New assets to design

Seven. These are the visual backbone and none of them exist as a web-ready image today.

| # | Asset | Source to trace | Where it goes |
|---|---|---|---|
| 1 | Code to Cognition architecture | Maturity deck S2, CISO deck S4 | Section 3 |
| 2 | Runtime as a lens vs a shield | Micro deck S25 | Section 6 |
| 3 | Runtime at every layer, L1 kernel to L4 prompt | Micro deck S19 | Section 7 |
| 4 | Maturity phases matrix, 5 tracks x 3 phases | Maturity deck S9, S12, S15, S16, S17 | Section 8 |
| 5 | Runtime security journey, 8 numbered steps | Micro deck S15 | Section 9 |
| 6 | Four deployment models | Micro deck S13 | Section 10 |
| 7 | Consolidation grid, AccuKnox vs 10 replaced vendors | CISO deck S38 | Section 13 |

Two product captures are also needed: an Agentic AI / AgentZ console view and a CDR console view. Without them, tabs 7 and 11 ship with a diagram instead of a screenshot, which reads as weaker than the other ten.

---

## 5. Numbers that disagree across sources

Fix these before the page ships. Every one appears in at least two places with two different values, and a buyer who reads the homepage and then the platform page will spot the gap.

| Claim | Homepage | CNAPP micro deck | Maturity deck | CISO deck | Recommend |
|---|---|---|---|---|---|
| Patents | 10+ | 5+ | not stated | 10+ | **10+** |
| Downloads | 2M+ | 20M+ | not stated | not stated | Verify with the KubeArmor team |
| Customers | 1,000+ | 3,000+ | not stated | not stated | Verify |
| Compliance frameworks | 45+ | 37+ | 35+ | 34+ and 40+ on different slides | **45+**, and use it everywhere |
| Integrations | 30+ | 50+ | 70+ | 50+ | **50+** |
| Tools replaced | not stated | 3 to 5x | not stated | 12+ domains, 3 to 1 | **3 to 5 tools per deployment** |
| Alert reduction | not stated | 80% | not stated | not stated | 80%, cite the source customer |
| Cost saving | not stated | 40 to 60% | >50% | >50% | **Over 50%** |

The page copy in `platform-page-content.md` uses the recommended column throughout.

---

## 6. Build order

Ship in three passes so the page improves at each step rather than waiting on all seven new diagrams.

**Pass 1, structure and showcase.** Sections 1, 2, 4, 5, 10, 11, 15, 18. Everything here uses copy plus images that already exist. This alone replaces the current page and closes the taxonomy gap.

**Pass 2, differentiation.** Sections 3, 6, 7, 13, 14. Needs new assets 1, 2, 3, and 7. This is where the page starts to win an evaluation instead of just describing a product.

**Pass 3, depth.** Sections 8, 9, 12, 16, 17. Needs new assets 4, 5, 6 and the two missing product captures.

Rough effort, design plus build: pass 1 is about a week, pass 2 about a week including diagram design, pass 3 about four days.

---

## 7. Open questions for Anish and product

1. **Beta labeling.** The mega menu marks CIEM, DSPM, CTEM, ASM, SSPM, AI-GRC, and AI-SOC as Beta. The CISO deck presents CIEM and DSPM as full modules. Which set carries a Beta badge on this page?
2. **Agentic AI placement.** The homepage gives it its own hero tab under the AgentZ brand and links every card to `/platform/agentz`. Does the platform showcase get an AgentZ tab, or does it stay inside AI Security?
3. **The three dead links.** `AI Identity Security`, `AI Model, Dataset Security`, and `AI GRC` are `href="#"` in the mega menu and on the homepage hero. They need pages or they need to stop being links.
4. **Stack ranking on a public page.** The comparison table is marked confidential in the deck. Does the public version keep vendor names or switch to "typical CNAPP vendor"?
5. **Product tour coverage.** The current tour covers CNAPP only. Do we get per-module Storylane tours for AI Security and API Security, or one tour with chapters?

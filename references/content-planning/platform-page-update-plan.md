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
6. `references/content-planning/platform-pages-content-plan.md`, the earlier per-module gap analysis.
7. `references/brian-demo-screenshots/DEMO-SUMMARY.md`, 22 captioned product screenshots.
8. Live DOM of the `/platform/cdr`, `/platform/siem`, `/platform/ai-security`, `/platform/api-security` and `/platform/dspm` module pages, harvested for product screenshots.

The Google Drive folder was not readable from this session (the Drive API returned an insufficient-scope error). Every image the prototype needs was found on the live site instead, so nothing is blocked. See section 4.

---

## 0. SEO framing

The page targets **Zero Trust CNAPP platform** as the primary keyword. Every section heading leads with the term a buyer actually searches for rather than a rhetorical phrase, and each showcase tab headline carries the full expanded product category alongside its acronym, since buyers search both ways.

| Section | Heading | Keyword carried |
|---|---|---|
| 1 | Zero Trust CNAPP Platform for Cloud, Application and AI Security | zero trust CNAPP platform |
| 3 | Code to cloud to AI security on a single control plane | code to cloud security |
| 4 | Twelve CNAPP modules on one policy engine | CNAPP modules |
| 5 tabs | "Cloud Security Posture Management for AWS, Azure, GCP and Oracle", "Cloud Workload Protection with eBPF runtime enforcement", "Kubernetes Security Posture Management and CIS benchmark hardening", and so on | CSPM, CWPP, KSPM, ASPM, API security, AI-SPM, DSPM, SBOM, CDR, SIEM |
| 6 | Runtime security: threat detection versus inline prevention | runtime security, inline prevention |
| 8 | CNAPP adoption roadmap and security maturity phases | CNAPP adoption, security maturity |
| 10 | Flexible deployment models: SaaS, private cloud, on-premise and air-gapped | air-gapped security, on-premise CNAPP |
| 12 | Continuous compliance across 45+ frameworks | continuous compliance |
| 13 | Security tool consolidation and TCO reduction | security tool consolidation |
| 14 | CNAPP vendor comparison | CNAPP vendor comparison |

**Meta title:** Zero Trust CNAPP Platform for Cloud, Application and AI Security | AccuKnox
**Meta description:** AccuKnox Zero Trust CNAPP unifies CSPM, CWPP, KSPM, ASPM, API security, AI-SPM, DSPM, SBOM, CDR, SIEM and compliance on one policy engine. Inline runtime prevention with eBPF and LSM.

Conversational and rhetorical headings are out. The first draft used lines like "You do not deploy twelve modules on a Tuesday" and "Pick where you hurt". Those carry no search intent and read as consumer copy on an enterprise security page. Every one has been replaced.

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
| "Let AccuKnox perform impact analysis" paragraph | Vague, uses "50+ tooling" once | Replace with the consolidation and TCO band carrying real numbers |

### Remove

1. The hero rhetorical question. It asks the reader to agree with a premise instead of telling them what the product is.
2. The duplicated testimonial carousel block.
3. The "AccuKnox is the top CNAPP Security Pick" banner above the fold. Same content lives in the proof band.
4. The lone James Berthoty quote sitting inside a product tab. Quotes belong in the proof band, not inside a feature panel.
5. The IoT/Edge and 5G two-card block. Both have their own pages and neither is new.
6. The open source projects grid (KubeArmor, ModelArmor, ClawArmor, K8TLS). KubeArmor still earns a mention inside the IDT Telecom customer quote, which is enough on this page.

---

## 3. New page structure

Seventeen sections. Sections 2, 5 and 8 are the tabbed components, and section 5 is the centerpiece the brief asks for.

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
| 11 | Infrastructure coverage | Five-row table plus architecture image | Homepage section |
| 12 | Compliance, 45+ frameworks | Logo grid plus metrics | Micro deck S30 |
| 13 | Consolidation and TCO | Logo replacement grid plus stats | CISO deck S38 |
| 14 | Stack ranking vs competitors | Comparison table | CISO deck S36 |
| 15 | Integrations, 50+ | Category cards plus the logo wheel | Homepage plus micro deck S14 |
| 17 | Proof band, analysts, patents, customers | Mixed | Micro deck S3, S32, S33 |
| 18 | POC in three weeks plus FAQs plus CTA | Stepper plus accordion | Micro deck S34 |

### Why section 5 carries the page

The homepage showcase already works: a left-to-right icon nav, one panel per module, a headline, a support stat, a screenshot carousel, and an "Explore X" button. Buyers land on `/platform` expecting the same interaction at more depth. The platform version keeps the identical shell and adds two things per panel: a four-bullet capability list, and a link into the matching help doc. Reusing the component means Anish builds nothing new, only extends the panel template and adds two tabs.

The homepage has 10 tabs. The platform page gets **13**. Harvesting the module pages closed the two screenshot gaps flagged in the first draft (Agentic AI and CDR) and turned up six SIEM console shots, so SIEM moves onto the tab bar rather than sitting in the overflow row.

| # | Tab | Homepage has it | Screenshots available |
|---|---|---|---|
| 1 | Cloud Security (CSPM) | Yes | 8 |
| 2 | Workload Security (CWPP) | Yes | 8 |
| 3 | Kubernetes Security (KSPM) | Yes | 8 |
| 4 | Application Security (ASPM) | Yes | 7 |
| 5 | API Security | Yes | 8 |
| 6 | AI Security (AI-SPM) | Yes | 8 |
| 7 | Agentic AI Security | **No, new** | 7, from `/platform/ai-security` |
| 8 | Data Security (DSPM) | Yes | 7, from `/platform/dspm` |
| 9 | Supply Chain (SBOM) | Yes | 4 |
| 10 | Secrets Manager | Yes | 3 |
| 11 | Cloud Detection and Response (CDR) | **No, new** | 5, from `/platform/cdr` |
| 12 | SIEM | **No, new** | 8, from `/platform/siem` |
| 13 | Compliance and GRC | Yes | 5 |

CIEM, CTEM, ASM, SSPM, AI-SOC and AI-GRC stay off the tab bar and appear in an "Also on the platform" row below it, because all six carry a Beta label. Putting a Beta module on the main showcase invites a demo request the product cannot fully answer.

### Layouts retained from the current /platform page

Five components on the current page are well built and worth keeping rather than redesigning. All five are reproduced in the prototype.

| Component | Where it moves | Change |
|---|---|---|
| Press and analyst logo marquee | Directly under the hero | Auto-scroll, greyscale until hover |
| Typed resource cards (eBook, Blog, Help doc, Video) | Above the proof of concept band | Same four-card layout, refreshed titles |
| Gated asset block with a "what is inside" checklist | Before the proof band | Swap the 2025 guide for the Zero Trust CNAPP guide |
| Numbered FAQ accordion | Page footer area | Expanded from 5 questions to 10 |

---

## 4. Image manifest

**The prototype uses 169 unique images and every one of them already exists on accuknox.com.** All 169 URLs were load-tested and none are broken. Base path is `https://accuknox.com/wp-content/uploads/`.

The Google Drive folder could not be read from this session, because the Drive API token has insufficient scopes. That turned out not to matter: harvesting the live homepage, the current `/platform` page, and the `/platform/cdr`, `/platform/siem`, `/platform/ai-security`, `/platform/api-security` and `/platform/dspm` module pages produced a full set. If the Drive folder holds higher-resolution originals, they can be swapped in file by file without touching the layout.

### 4a. Product screenshots, by showcase tab

| Tab | Files | Harvested from |
|---|---|---|
| CSPM | `CSPM-Single-Pane-Cloud-Asset-View-platform.webp`, `CSPM-Cloud-Misconfiguration-platform.webp`, `CSPM-Asset-Vulnerabilities-platform.webp`, `CSPM-Drift-Detection-platform.webp`, `CSPM1-` to `CSPM4-dashboard-home.webp` | current /platform + homepage |
| CWPP | `CWPP-MonitorAppBehaviour.webp`, `CWPP-HardenYourVMs.webp`, `CWPP-Host-Scan-Easily-platform.webp`, `CWPP-Secure-Your-Secrets-Vault-platform.webp`, `CWPP1-` to `CWPP4-dashboard-home.webp` | current /platform + homepage |
| KSPM | `KSPM-Scan-Cluster-Misconfigurations-platform.webp`, `KSPM-CIS-Benchmark-Findings-platform.webp`, `KSPM-Identity-Entitlements-Management-platform.webp`, `KSPM-Pod-Security-Admission-platform.webp`, `KSPM1-` to `KSPM4-dashboard-home.webp` | current /platform + homepage |
| ASPM | `ASPM_StaticApplicationSecurity.webp`, `ASPM_ContainerScanning.webp`, `ASPM_IaC_Scanning.webp`, `ASPM_Vulnerability_Management.webp`, `ASPM1-`, `ASPM2-`, `ASPM4-dashboard-home.webp` | current /platform + homepage |
| API Security | `api-discovery.webp`, `sankey-diagram.webp`, `owasp-ui-1-api.webp`, `owasp-ui-2-api.webp`, `True-Behavioral-Analytics-dashboard.webp`, `Targeted-OWASP-Protection-dashboard.webp`, `api1-`, `api2-dashboard-home.webp` | /platform/api-security |
| AI Security | `Ai-sec-Inventory-View.webp`, `Ai-sec-AI-Model-View.webp`, `Ai-sec-Unmanaged-Assets-Discovery.webp`, `Ai-sec-Prompt-Firewall.webp`, `Ai-sec-Runtime-Defense.webp`, `Ai-sec-AI-Compliance.webp`, `AI-SPM1-`, `AI-SPM3-dashboard-home.webp` | /platform/ai-security |
| Agentic AI | `Multi-Cloud-Agent-Visibility-Auditing-agentic.webp`, `Sandbox-Unsafe-Tool-Usage-agentic.webp`, `Sandbox-Auto-Generated-Code-agentic.webp`, `Multi-Platform-Support-agentic.webp`, `Ai-sec-Managed-Agents-View.webp`, `Ai-sec-Runtime-Agent-Sandboxing.webp`, `agentz-tab-home-1.webp` | /platform/ai-security |
| DSPM | `Discovery-`, `Classification-`, `Access-Review-`, `Monitoring-`, `Remediation-`, `Onboarding-Data-Source-Connection-dashboard-dspm.webp`, `DSPM1-dashboard-home.webp` | /platform/dspm |
| SBOM | `SBOM1-` to `SBOM4-dashboard-home.webp` | homepage |
| Secrets | `secrets-manager-dashboard-home.webp`, `secrets-manager-1-dashboard-home.webp`, `CWPP-Secure-Your-Secrets-Vault-platform.webp` | homepage + /platform |
| CDR | `cdr-solution-dashboard.webp`, `Enforcing-private-access-policy-on-S3-buckets.webp`, `Ensure-public-IP-is-not-enabled-for-VMs.webp`, `Notify-if-AWS-access-from-unknown-regions.webp`, `AccuKnox-cdr-Architecture.webp` | /platform/cdr |
| SIEM | `Main-Security-Overview-Dashboard.webp`, `Alert-Investigation-Correlation-Details.webp`, `Log-Search-Threat-Hunting-Interface.webp`, `Incident-Threat-Timeline-Visualization.webp`, `Compliance-Reporting-Dashboard-e.g.-PCI.webp`, `Integration-Data-Source-Management.webp`, `siem-architecture.webp`, `noise-reduction.webp` | /platform/siem |
| Compliance | `COMPLIANCE1-` to `COMPLIANCE3-dashboard-home.webp`, `Achieve-Key-Compliance-dashboard.webp`, `Ai-sec-AI-Compliance.webp` | homepage + /platform/api-security |

### 4b. Diagrams and supporting visuals

| File | Where it goes |
|---|---|
| `AccuKnox-Security-Modules.webp` | Hero visual and the section 3 architecture slot. This replaces the diagram the first draft asked to design. |
| `deployment-models-differentiators.webp` | Section 10, the primary deployment visual (1672 x 746, verified) |
| `saas-onprem.webp` | Section 11, SaaS versus on-premise architecture |
| `ask-ai-platfrom-card.webp` | Section 4, AI Copilot callout |
| `Ai-sec-Runtime-Defense.webp` | Section 7, runtime layers |
| `public-cloud-support-home.webp`, `k8-engines-support-home.webp`, `cicd-platform-support-home.webp`, `ai-llm-logos-home.webp`, `api-sec-logos-home.webp`, `sbom-support-home.webp`, `dspm-support-home.webp`, `hashicorp-logo-home.webp`, `integrated-compliance-frameworks-home.webp` | Per-tab support badges |
| `Iot-Edge-Security.svg`, `5G-Security.svg` | Section 11, specialized environments |
| 11 `*-press-slider.webp` files | Press marquee |
| `cnapp-buyers-guide-400x250.webp`, `zero-trust-llm-security-featured.webp`, `help-doc-platform.webp`, `explainer-2.0.webp` | Gated block and resource cards |
| `David-Billeter-testi.webp`, `golan-ben-oni.webp`, `jamesb.png`, `sonesta-home.webp`, `idt-1.webp`, `latio3.webp` | Testimonial headshots and company logos |
| ~30 `*-nav-icon.svg` files | Hero domain tab cards and the module grid |

### 4c. Still worth designing

Only two items remain genuinely missing, and the page works without either.

| # | Asset | Source to trace | Where it goes |
|---|---|---|---|
| 1 | Runtime as a lens versus a shield | Micro deck S25 | Section 6. Currently rendered as a styled two-column comparison in HTML, which may be enough. |
| 2 | Maturity phases matrix, 5 tracks x 3 phases | Maturity deck S9, S12, S15, S16, S17 | Section 8. Currently rendered as a tabbed card matrix in HTML. |

Optional upgrades, not blockers: cropped versions of `10-ask-ai-copilot-remediation.png`, `17-ai-red-teaming-risks.png` and `21-zero-trust-policy-discovery.png` from `references/brian-demo-screenshots/` if higher-fidelity captures are wanted than the marketing-site equivalents.

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

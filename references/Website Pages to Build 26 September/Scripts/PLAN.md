# AccuKnox Website Update Plan for AI Security, AppSec and DSPM

Read on 2026-09-26 from accuknox.com with Firecrawl. Every code below (N1, A2, D5 ...) matches a
numbered box in `shots/`. Open the PNG beside each item to see the exact spot on the live page.

Tags on the boxes: **UPDATE** means edit the copy in place. **REPLACE** means remove the section and
put the new one in its slot. **NEW ABOVE** or **NEW BELOW** means create a new section there. **ADD**
means add items to a list. **FIX** means a broken link. **MOVE** means move the item in the nav.

Facts carry a tier. **D** is in the help docs and can ship today. **I** is in an internal asset,
such as the Shadow AI coverage sheet. **A** comes from the product walkthrough only, so product must
confirm it before the page goes live. A value in square brackets is a gap for a human to fill.

## Two Folders Hold the Package

`Prototype HTMLs/` holds the eight files to share. Each file embeds its own images, so the folder
works as a zip. Open `index.html` first. It links the five `update-*.html` pages and the two
`new-page-*.html` wireframes.

`Scripts/` holds this plan, the annotated shots in `shots/`, the Excalidraw map, the wireframe
sources in `src/`, the page text in `scrape/clean/` and the build scripts. Run
`build_update_pages.py` and `build_wireframes.py` to rebuild the HTML files.

## Six Pages Change, Two Pages Are New, and the Nav Gets Six Edits

| # | Page | Work |
| --- | --- | --- |
| 1 | Nav mega menu | Add 2 items to Secure AI, fix 2 dead links, add AI DAST, move DSPM out of Coming Soon, repoint 2 Solutions links |
| 2 | `/platform/ai-security` | Add Shadow AI, AI Gateway and AI AppSec sections. Update 4 blocks. Replace 2 FAQs |
| 3 | `/platform` | Add 2 cards to the AI Security tab, fix 2 wrong card captions, update 3 module captions |
| 4 | `/platform/dspm` | Replace the unsourced stats with help-doc facts. Add DSPM for AI and an India band |
| 5 | `/solutions/sast`, `/solutions/dast`, `/platform/aspm` | Add AI SAST and AI DAST sections |
| 6 | NEW `/solutions/shadow-ai-discovery` | Wireframe `wireframe-shadow-ai-discovery.html` |
| 7 | NEW `/solutions/dspm-indian-banks` | Wireframe `wireframe-dspm-indian-banks.html` |

`nav-and-pages.excalidraw` draws the whole map. Open it at excalidraw.com with File, then Open.

## Decision, AI SAST and AI DAST Live in AppSec and Get a Teaser on AI Security

Put the full AI SAST and AI DAST content on the AppSec pages, and add a short section on the AI
Security page that links to them. Do not add them to the Secure AI nav menu.

The reason is buyer confusion. Secure AI is "security for AI", which protects the customer's models
and agents. AI SAST and AI DAST are "AI for security", which uses AI to test the customer's code and
apps. The product team already flagged that AI DAST gets confused with AI red teaming. Two entries
in Secure AI would make that worse. The AppSec buyer searches for SAST and DAST, and the existing
`/solutions/sast` and `/solutions/dast` URLs already rank for those terms.

The AccuKnox AI Gateway is different. It protects AI traffic, so it belongs in Secure AI.

## 1. Nav Mega Menu Needs Six Edits

The screenshots are `shots/N1-menu.png`, `shots/N3-menu.png` and `shots/N4-menu.png`.

- **N1 ADD. Platform, then Secure AI.** Add two items under the "AI SPM" item.
    - "Shadow AI Discovery", linking to the new `/solutions/shadow-ai-discovery`.
    - "AccuKnox AI Gateway" with a "Coming soon" tag, linking to `/platform/ai-security#ai-gateway`
      until the product has its own page.
- **N2 FIX. Platform, then Secure AI, then "AI Identity Security".** The link points to
  `accuknox.com/#`. Point it to `/platform/ai-security#identity`, or hide the item until a page
  exists.
- **N3 FIX. Platform, then Secure Code, then "AI-Accelerated SAST Scanning".** The link points to
  `accuknox.com/#`. Rename the item "AI SAST" and point it to `/solutions/sast#ai-sast`.
- **N3 ADD. Platform, then Secure Code.** Add "AI DAST (AI Pentesting)" under the DAST item, linking
  to `/solutions/dast#ai-dast`. Give it a "Coming soon" tag.
- **N4 MOVE. Platform, then Coming Soon, then "Data Security (DSPM) BETA".** The help docs now carry
  a DSPM overview and an onboarding guide. Move DSPM out of Coming Soon into the main Platform list
  as "Secure Data (DSPM)", below Secure Workload. Remove the BETA tag. Product confirmed on
  2026-09-26 that the site no longer calls DSPM beta.
- **N5 UPDATE. Solutions, then Use Cases.** Repoint "Shadow AI Discovery" from the help docs page to
  `/solutions/shadow-ai-discovery`. Add "DSPM for Indian Banks", linking to
  `/solutions/dspm-indian-banks`. Also add that link under Security Across Industries, beside
  Finance.

## 2. The AI Security Page Needs Three New Sections

The page is `accuknox.com/platform/ai-security`.

- **A1 UPDATE. Hero subtitle, `shots/A1.png`.** Replace "Discover every model, agent, and pipeline.
  Close gaps across 43 compliances. Auto-generate your AI Bill of Materials." with "Discover every
  model, agent, MCP server and shadow AI tool. Govern model traffic through one AI gateway. Close
  gaps across 43 compliances and export your AI-BOM."
- **A2 UPDATE. The 8-module grid and the AI-SPM block, `shots/A2.png`.**
    - In the AI-SPM block, replace the bullet "Shadow AI discovery catches unapproved notebooks,
      rogue models, and MCP servers automatically." with "**Shadow AI discovery** finds unapproved
      AI across cloud accounts, browsers, hosts, desktop apps and CLI coding agents. See Shadow AI
      Discovery." Link the last three words to `/solutions/shadow-ai-discovery`. Tier I.
    - In the module grid on the left, add two tiles, "Shadow AI Discovery" and "AI Gateway". Clicking
      either tile scrolls to the new section below. Rename the heading "8 Modules, Tightly
      Integrated, Loosely Coupled" only if product counts the two as modules. Otherwise keep 8, and
      mark the two tiles as "capabilities".
- **A3 UPDATE. The "AI Guardrails, Stateful Prompt Firewall" block.** This block shows after a click
  on the Guardrails tile, so it has no screenshot. Replace the bullet "One policy enforced
  everywhere: API gateway, SDK, browser plugin, and Copilot Studio." with "**One policy**
  enforced everywhere. The AccuKnox AI Gateway, API gateways, the SDK, the browser plugin, CLI coding
  agents and Copilot Studio." Mark the AccuKnox AI Gateway "coming soon". CLI agents are tier I.
- **A4 NEW ABOVE. Above "AI Security Platform Tour", `shots/A4.png`.** Create three sections in this
  order.
    1. **Shadow AI Discovery, `id="shadow-ai"`.** Heading "Shadow AI Hides in Five Places, and
       AccuKnox Covers Each One". Five cards. Each card has a surface name, a status chip, a
       one-line risk and a one-line control. Cloud AI services (agentless). Browser plugin (full
       coverage). Host scanning (Linux full coverage, macOS beta, Windows in progress). Desktop
       telemetry app (beta). CLI agent security (full coverage). Put a status legend under the cards
       that defines "Full coverage", "Beta" and "In progress", so a buyer reads the label as a
       status and not as a gap. Under the legend put one stat line, "4K+ unmanaged AI assets found
       on hosts in one environment in 60 days", and a button "Explore Shadow AI Discovery" to
       `/solutions/shadow-ai-discovery`. Never publish the exact count.
    2. **AccuKnox AI Gateway, `id="ai-gateway"`, with a "Coming soon" tag.** Heading "See Every Model Call, Then Govern It,
       Then Firewall It". Three numbered steps. Visibility (an inventory of every model and caller).
       Governance (policies, rate limits and model access per team). Prompt firewall (inline on all
       gateway traffic). Under the steps put a deployment row, cloud, on-premises and air-gapped, and
       an integration row, Bifrost, LiteLLM, Kong AI, Azure APIM, AWS API Gateway and Apigee. The
       gateway is tier A, and product approved marketing it as coming soon. Tier D for Bifrost, LiteLLM and the three API gateways, from
       `docs/integrations/ai-overview.md`.
    3. **AI-Powered AppSec, `id="ai-appsec"`.** Heading "AI Tests Your Code and Your Running Apps
       Too". Two cards. AI SAST, "fix recommendations in the IDE and the pipeline", links to
       `/solutions/sast#ai-sast`. AI DAST, "AgentZ plans and runs the pentest, then validates each
       finding", with a "Coming soon" tag, links to `/solutions/dast#ai-dast`. Add one line under the cards, "AI DAST tests
       applications. AI red teaming tests models and agents." Link "AI red teaming" to
       `/solutions/ai-red-teaming`.
- **A4b UPDATE. The "Shadow AI Discovery" tour tab.** Keep the screenshot. Replace the "Shadow AI
  Detection" line with "MCP servers, AI SDKs, AI gateways, inference engines, AI/ML libraries, AI
  agents and AI automation, the 7 host-scan categories." Tier I.
- **A5 UPDATE. "AI Security Key Differentiators", `shots/A5.png`.** Add two lines. "Shadow AI
  discovery across cloud, browser, host, desktop and CLI agents." "AI gateway with a native prompt
  firewall, coming soon."
- **A6 REPLACE. FAQs 26 and 27, `shots/A6.png`.**
    - FAQ 26 says AccuKnox finds shadow AI "by analyzing outbound traffic". AccuKnox has no network
      or CASB layer, so the answer overclaims. Replace the answer with "AccuKnox finds unapproved AI
      on five surfaces. Cloud connectors list AI services in AWS, Azure and GCP. A browser plugin
      inspects AI chat apps. Host scanning fingerprints AI software on VMs and containers. A desktop
      telemetry app reads what desktop agents do. A gateway proxy puts CLI coding agents under the
      Prompt Firewall."
    - FAQ 27 claims detection of AI embedded in SaaS copilots and plugins. No source supports it.
      Remove FAQ 27, or rewrite it to the documented managed-agent coverage for Copilot Studio,
      Microsoft 365 Agents and Power Apps, from `docs/getting-started/3.5-release.md` and
      `docs/integrations/powerapps-integration.md`.
    - Add two FAQs. "What does the AccuKnox AI Gateway do?" uses the three-step answer from A4. "Is
      AI DAST the same as AI red teaming?" answers "No. AI DAST pentests your applications and
      infrastructure from the outside. AI red teaming tests the model or agent itself."

## 3. The Platform Page Misses Shadow AI and the Gateway

The page is `accuknox.com/platform`.

- **P1 ADD. The AI Security tab card list, `shots/P1.png`.** Add two cards at the end. "Shadow AI
  Discovery, finds unapproved AI on five surfaces." "AccuKnox AI Gateway, routes, governs and
  firewalls model calls." Fix two captions on the existing cards.
    - "AI Detect & Respond (AI DR)" ends in "tools/p>", a broken HTML tag. Fix it to "Reconstructs
      attack chains across prompts and tools".
    - "AI Red Teaming, Pen Testing" says "Filters, audits, blocks LLM prompts and responses". That is
      the Prompt Firewall caption. Replace it with "Runs 150+ adversarial probes on every model
      change", from the AI Security page.
- **P1b UPDATE. The Application Security tab.** Rename the card "App Sec (SAST, DAST, SCA)" to "App
  Sec (AI SAST, AI DAST, SCA)". Caption, "AI fix suggestions in the IDE and an AI-run pentest of the
  live app."
- **P1c ADD. The Data Security tab.** Add one card, "Sensitive Data in AI, finds PII in training
  datasets and masks it in prompts", linking to `/platform/dspm#dspm-for-ai`.
- **P2 UPDATE. The 12-module grid, `shots/P2.png`.** Change the "AI Security (AI-SPM)" caption to
  "Finds shadow AI, governs model traffic, stops prompt injection and LLM data leaks." Change the
  "ASPM" caption to "Correlates code to cloud. AI SAST and AI DAST find what is reachable." Move
  DSPM into this grid when N4 moves it out of Coming Soon.

## 4. The DSPM Page Must Match the New Help Docs

The page is `accuknox.com/platform/dspm`. The source for every number below is `docs/getting-started/dspm-overview.md`,
tier D, merged today.

- **D1 UPDATE. Hero subtitle, `shots/D1.png`.** Replace "AI-powered DSPM to discover, classify, and
  protect sensitive data across public, private, and hybrid clouds." with "Agentless, read-only DSPM
  that classifies 283 data classes inside the region that holds the data. Only a findings file
  leaves your account, and the console can run air-gapped."
- **D2 REPLACE. "Recent Data Security Incidents", `shots/D2.png`.** The US breach carousel reads as
  fear marketing and names no AccuKnox capability. Replace it with "Only a Findings File Leaves Your
  Account". Use four rows from the doc's data-handling table. Read-only access. Classification in
  your VM or cluster. One zipped findings file per store over HTTPS. No cross-region data movement.
- **D3 REPLACE. "The Data Security Challenge", `shots/D3.png`.** The 85%, 73% and 92% stats have no
  source on the page. Replace the four tiles with four doc facts. 283 data classes. 159 detectors.
  62 country packs for national IDs. 16 compliance framework groups.
- **D4 UPDATE. "Why Choose AccuKnox", `shots/D4.png`.** "50+ data sources" and "99.8% accuracy
  with 50+ sensitive data types" conflict with the docs. Replace them with the store list and "283
  data classes, each with a confidence tier". Drop the 99.8% figure everywhere. Where the copy needs an accuracy claim, write "high-accuracy
  classification", backed by the three confidence tiers. Change
  "Compliance Ready" to name "GDPR, HIPAA, PCI DSS, India DPDP Act 2023, SOC 2 and 11 more".
- **D5 NEW BELOW. Below "DSPM Capabilities & Use Cases", `shots/D5.png`.** Create "DSPM for AI,
  `id="dspm-for-ai"`". Heading "Sensitive Data Reaches AI Through Datasets, Prompts and Shadow
  Tools". Four cards, each linking to its page.
    - Training datasets. Scan datasets for PII and PHI before training. Link to
      `/solutions/ai-model-dataset`. The live AI Security page already states this.
    - Prompts. The Prompt Firewall masks PII, PHI and card numbers before they reach the model. Link
      to `/solutions/prompt-firewall`.
    - Shadow AI. Find the AI tools and agents that could read sensitive data. Link to
      `/solutions/shadow-ai-discovery`.
    - AI gateway and AI-BOM. Govern which model receives which data class, and list every model in
      an AI-BOM. Link to `/platform/ai-security#ai-gateway`. Mark the gateway "coming soon".
- **D6 UPDATE. "Automated Sensitive Data Classification Engine", `shots/D6.png`.** Replace the
  bullets with doc facts. 159 detectors. 62 country packs. A language model for person names that
  runs inside the container. Three confidence tiers, very likely, likely and possible. Up to 10,000
  rows or documents sampled per table.
- **D7 REPLACE. "Multi-Cloud Data Security Asset Coverage", `shots/D7.png`.** Replace the three icon
  cards with the doc's supported data stores table. S3, Azure Blob and ADLS Gen2, RDS and Aurora,
  Azure SQL, Cosmos DB, DynamoDB, DocumentDB, self-managed PostgreSQL, MySQL, MariaDB, SQL Server
  and MongoDB, Google Drive and Salesforce.
- **D8 REPLACE. "AccuKnox DSPM Differentiators", `shots/D8.png`.** The matrix compares AccuKnox with
  unnamed "Traditional DSPM" and "DLP Solutions". Replace it with the named-vendor rows from the doc.
  Where scanning runs, where the console lives, what leaves the environment, and air-gapped
  operation, for Cyera, Varonis, BigID and IBM Guardium DSPM.
- **D8b NEW BELOW D8. India band.** Heading "Indian Banks Map DSPM Findings to RBI and DPDP Controls".
  One line, "DPDP Act 2023 and SPDI Rules 2011 mapping covers 17 data classes, including Aadhaar,
  PAN and GST." Button "DSPM for Indian Banks" to `/solutions/dspm-indian-banks`.
- **D9 REPLACE. "Flexible DSPM Deployment Models", `shots/D9.png`.** Replace Cloud-Native,
  Kubernetes and Hybrid with the three documented forms. A VM with systemd timers, the default. A
  Kubernetes CronJob with IRSA or workload identity. An event-driven AWS Lambda function. Add a
  fourth card, "Console on premises or air-gapped". Add links to the help docs pages
  `getting-started/dspm-overview` and `getting-started/dspm-onboarding`.

## 5. The AppSec Pages Need AI SAST and AI DAST Sections

- **S1 NEW BELOW. `/solutions/sast`, below the hero, `shots/S1.png`.** Create "AI SAST,
  `id="ai-sast"`". Heading "AI SAST Suggests the Fix in Your IDE and Pipeline". Three points.
    - AI analysis marks false positives and assesses severity. Tier D, `docs/getting-started/3.4-release.md`.
    - Pick "AI Enabled SAST" in the scan-type selector. Tier D, `docs/getting-started/3.7-release.md`.
    - IDE plugins and an auto PR decorator, tagged "Coming soon". [confirm the IDE names before
      the page lists them]
- **S2 UPDATE. SAST FAQs, `shots/S2.png`.** In the FAQ "How can organizations address the potential
  for false positives", add "AccuKnox AI SAST marks likely false positives on each finding." Add FAQ
  "What does the AI do in AccuKnox SAST?".
- **T1 NEW BELOW. `/solutions/dast`, below the hero, `shots/T1.png`.** Create "AI DAST,
  `id="ai-dast"`". Heading "AI DAST Plans and Runs the Pentest, Then Validates Each Finding". Put a "Coming
  soon" tag beside the heading.
    - One required field, the target URL.
    - Three scan depths, quick, standard and in-depth.
    - Four login methods, username and password, TOTP, email code and magic link, plus custom
      headers.
    - Optional repo link maps each finding to the code line. Optional OpenAPI upload finds
      forgotten endpoints.
    - Bring your own model. The AccuKnox model, your frontier model key, or a local LLM.
    - One line under the list, "AI DAST pentests applications. For model and agent testing, see AI
      Red Teaming."
- **T2 UPDATE. "Aggregate Your DAST tools in One Dashboard", `shots/T2.png`.** Add a sentence, "AI
  DAST findings land in the same ASPM view as SAST, SCA and IaC findings."
- **M1 UPDATE. `/platform/aspm`, "Prioritize & Automate Security in Code & Pipeline",
  `shots/M1.png`.** Rename the tabs "Static Application Security Testing (SAST)" and "Dynamic
  Application Security Testing (DAST)" to "AI SAST" and "AI DAST", and add one AI line to each tab.
- **M2 NEW BELOW. `/platform/aspm`, below the "Is Application Security an Afterthought in the AI Era?"
  webinar, `shots/M2.png`.** Create a two-card band, AI SAST and AI DAST, the same as A4 section 3.
  Add the line "AI SAST and AI DAST cover the AppSec lifecycle, from the IDE to a pentest of the
  live app."

## 6. New Page, Shadow AI Discovery

The page lives at `/solutions/shadow-ai-discovery`. The wireframe is
`wireframe-shadow-ai-discovery.html`, and nav entries N1 and N5 point to it. The sections run in
this order.

1. Hero with the claim and two buttons
2. Stats row, with "4K+" in place of the exact asset count
3. Three value tiles, one inventory, one policy and one audit trail
4. Five surface cards with status chips
5. Use cases in four tabs, one per buyer team
6. Coverage matrix, surface against control
7. The discover, govern, inspect and respond flow, which links to the AI Gateway and the Prompt Firewall
8. Integrations
9. Four named limits. Windows is in progress, macOS and desktop telemetry are in beta, the plugin list is finite, and AccuKnox has no CASB layer
10. FAQs
11. Demo call to action

## 7. New Page, DSPM for Indian Banks

The page lives at `/solutions/dspm-indian-banks`. The wireframe is
`wireframe-dspm-indian-banks.html`, and nav entry N5 points to it. The sections run in this order.

1. Hero led by the RBI customer data protection advisory and the DPDP deadline
2. Mandate strip with the four 2026 items, advisory and regulation labeled apart
3. Four value tiles on data residency and read-only access
4. Solutions in four tabs, one per bank team
5. Regulation to control matrix
6. Indian data classes
7. Deployment, with the air-gapped console first
8. AI data risk, which links to AI-BOM, Shadow AI and the AI Gateway
9. Proof from the Top 3 Indian public sector bank case study, labeled as SBOM
10. Supported data stores
11. FAQs
12. Assessment call to action

Lead with RBI Advisory No. 3/2026, "Best Practices Relating to Customer Data Protection", dated
25 March 2026. Section 2 of the advisory asks banks to use automated tools that tag and classify
customer data across in-house, cloud and third-party systems, which is the DSPM job. Call it an RBI
advisory, never a regulation. RBI has not published the text, so link the MediaNama summary and do
not quote it.

The second line carries the binding deadline. The DPDP Rules 2025 were notified on 13 November 2025,
and full obligations fall due around 13 May 2027. MeitY has proposed an earlier date, around
November 2026, but no gazette notification confirms it. The mandate strip adds the RBI Cybersecurity,
Technology Risk, Resilience and Assurance Directions of 31 July 2026, and the RBI draft guidance on
model risk management of 24 June 2026. Sources and caveats are in
`references/product-research/dspm/india-bank-data-mandates-2026-09.md`.

## Product Answered All Six Questions on 2026-09-26

| # | Question | Answer applied |
| --- | --- | --- |
| Q1 | Can the exact asset count go public? | No. Write "4K+" for assets. Critical findings and MCP servers become "100+" and "50+" |
| Q2 | macOS and desktop telemetry status? | Both show "Beta", with a status legend that says what beta means |
| Q3 | Is DSPM still beta? | Drop the beta label everywhere |
| Q4 | Which Indian item leads? | RBI Advisory No. 3/2026, labeled as an advisory, then the DPDP deadline |
| Q5 | Ship before the pages? | Market ahead of release. Tag the AccuKnox AI Gateway, AI DAST and IDE-based AI SAST "Coming soon" |
| Q6 | Source for 99.8%? | None. Drop it and write "high-accuracy classification" |

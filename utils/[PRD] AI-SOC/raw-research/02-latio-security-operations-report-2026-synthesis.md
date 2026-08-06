# Raw Research — Latio Security Operations Market Report 2026 (Full Synthesis)

Source: 2026-Latio-Security-Operations-Report.pdf (305 pages, extracted via pdftotext) plus the companion Latio Pulse post "Emerging Categories: The Evolution" (https://pulse.latio.tech/p/emerging-categories-the-evolution).
Author: James Berthoty, Latio Tech (founded 2023). Latio's positioning: "The only analyst firm that tests products." Practitioner-first, anti-hype.
Status: Fully extracted. This is the most important external document in the set. Both Mate and Exaforce cite their Latio awards on their homepages, so this report is the scoreboard the category is measuring itself against.

---

## 1. Executive summary, in Latio's words

"Security Operations Center (SOC) tooling is in the middle of a capability and expectation disruption." Five themes Latio says teams will weigh as they modernize:

1. "AI SOC" tools fit inside traditional SOC categories, differ from one another, and should be judged on the business outcomes they enable.
2. Most "AI SOC" platforms are really SOAR tools. Direct access to underlying data is what separates the leaders from the pack.
3. The SIEM market is going through an architectural transformation toward scalable, data-centric platforms. "There has never been more flexibility in purchasing a SIEM."
4. Users want to upgrade their SIEM but need the migration made simple. Many end up with data sprawled across multiple providers.
5. Leading solutions are evolving into larger platforms spanning data pipelines, detection engineering, threat hunting, and SIEM.

The framing sentence: "The SOC market is ripe for disruption due to the collision of agentic workflows with new data architectures."

## 2. Survey results (the FUD ammunition)

These are practitioner survey numbers. Use them verbatim in the PRD, blog, and deck to make the legacy-SIEM buyer uncomfortable.

- **64%** of teams consume alerts via an MDR managing an EDR and SIEM. 22% run an internal SOC. 14% have not invested in a SOC.
- **72%** are unexcited by their current SIEM but feel migration is not worth the investment.
- On SIEM happiness specifically: 32% happy, 28% unhappy and want to migrate, **40% unhappy but the cost of migrating isn't worth it.** So 68% are unhappy with their SIEM. That is the wedge.
- **80%** of teams are choosing to use AI in house; only 20% are looking to bring in a dedicated vendor. Of the in-house group, 68% have analysts using local agents (e.g. Claude Code) and 32% are building in-house agents.
- AI investment priorities: **62% incident response, 38% detection engineering.**
- Security operations platforms are the most commonly used tools AND the ones practitioners are most dissatisfied with. Big platforms underwhelm.

Read between the lines: teams are unhappy, they distrust rip-and-replace, and they are defaulting to DIY AI because vendor AI-SOC tools have not earned trust. AccuKnox's opening has to defuse the "expensive black box that hallucinates" fear before it sells anything.

## 3. The evolution narrative (use this as the blog's spine)

Latio's history of the SOC:
- Antivirus + firewall (signatures) → EDR + NGFW. Signature detection never died. Most operators still use YARA rules ~20 years on.
- SIEM emerged so teams could build detections across sources. It became the bedrock but needs three operator types: SIEM engineers, detection engineers, analysts. Heavy operational overhead.
- XDR was "the awkward middle." The market never agreed what it meant. Terminology now largely dropped in favor of separating SIEM and EDR.
- SOAR emerged as workflow generators. "These tools have always struggled to move beyond niche functionalities." Robust automation catalogs exist but technical debt is persistent.
- Now: cheaper storage + AI automation reopened choices that had consolidated. Renewed SOAR interest and a re-evaluation of whether SIEMs are even necessary.

Key quotes:
- "Saying 'the SIEM is dead' has been dead since 2011. While the SIEM will never die, its backend architecture is evolving."
- On AI SOC tools: "Early tools in this category focused only on automating incident response with LLMs - an evolution of the SOAR platforms that preceded them. These vendors have quickly realized that analysts sit downstream of other capabilities that need improvement to function properly."
- The closing line of the report: "The SIEM isn't dead, it's more alive than ever."

## 4. First wave vs second wave AI-SOC (from the Pulse post)

Latio (James Berthoty) was a self-described skeptic who got converted by the UX shift.

**First wave (SOAR + AI).** Five failure modes:
1. Summaries that don't add value beyond the original alert.
2. Enrichments cheaper to run natively in the SIEM.
3. Verbose summaries instead of actionable guidance.
4. Unoptimized queries that drive up cost.
5. Manual knowledge-base maintenance.
- The damning line: "at their worst, they can spin in circles investigating meaningless information while driving up costs."

**Second wave (AI-native, "Claude Code but for SOC").** Five differentiators:
1. Taking actions on behalf of the analyst, for investigation and response.
2. Investigating alongside the analyst rather than dumping a summary at the end.
3. Continuously learning and applying organization context.
4. Giving the analyst complete control over workflows as they happen.
5. Fine-tuning agents to enable autonomous actions.

UX is the differentiator: "moving from copy pasting code in and out of ChatGPT to using Claude Code or Cursor." And: "not expecting the AI to be perfect, and instead building a UX that is always useful." The goal is "increased speed and precision to analysts rather than seeking to wholeheartedly replace them." Latio derides "dashboard-y" tools as "SIEM for your SIEM."

This first-wave/second-wave split is the cleanest narrative AccuKnox can adopt. We position the AI-SOC as second wave AND add a third axis nobody else has: runtime enforcement. Everyone else investigates and recommends. AccuKnox investigates, recommends, and can block at the kernel.

## 5. The Modern SOC Architecture — 5 layers

Latio's model of the modern SOC stack (the decentralization of the SIEM):

1. **Log Sources**
2. **Data Pipelines**
3. **Log Querying and Storage** (SIEM, Object Storage, Data Lake)
4. **Threat Detection**
5. **SOAR**

Core thesis: traditional SIEMs consolidated ingestion, indexing, search, and long-term storage into one box. That is now misaligned with how teams (and agents) store and access data. Modern teams optimize for distributed data and want flexibility per layer.

Trends inside Log Sources worth quoting:
- SaaS detections are hard but increasingly tooled.
- Application Detection and Response (ADR / CADR) is rising as AI makes first-party apps easier to attack and "time to exploit plummets."
- AI security telemetry: two use cases, protecting first-party agents (ADR-style runtime insight) and protecting employee AI usage (proxy/browser/hooks for DLP). "most resolutions come down to data access and identity controls, as AI will more quickly expose incorrectly scoped permissions."
- Asset context: "Following in the path of CNAPP, large security operations providers are beginning to further unify asset context and blast radius information with detection and response." Directly relevant: AccuKnox is a CNAPP. We already have the asset/blast-radius graph the AI-SOC vendors are scrambling to build.
- Unified identity telemetry: vendors building identity relationship graphs so agents can find the responsible user.

## 6. Data pipelines, SIEM architecture, OCSF

- Data pipeline category defined by Cribl, now extended by SIEM vendors. Best ones do real-time enrichment, normalize to OCSF, test log health, enrich, optimize storage cost.
- "ELK is out, and data portability is in." Move from Elasticsearch/Logstash/Kibana toward Apache Iceberg, ClickHouse, DuckDB, object storage.
- SIEM migration order Latio recommends: optimize your data pipeline, decouple your detection engine, then migrate the data.
- Five SIEM categories by openness: Traditional All-in-One, Hydrate-and-Query with Federated Search, Stream Detection/Translation, Data Lake Flexibility, Total Data and Detection Flexibility.
- Federated search caveats for agents: rate/size limits, throttling, slow on unstructured data, and "Agent hallucination when data does not exist, or it's unknown if it does exist." Two fixes: standardize to OCSF (guarantees whether data exists) or index on ingest.

## 7. The SOAR / AI-SOC convergence

Latio buckets four things into "SOAR" because they are merging:
1. Traditional SOAR workflow builders (flexible, high maintenance).
2. Case management systems (the new analyst dashboard battleground).
3. MDR with automation software (the line vs "AI SOC" is "usually only 24/7 staffing").
4. AI SOC tools ("run agent workflows under the hood and operate almost indistinguishably from SOAR, but benefit from the added flexibility of AI, oftentimes at the cost of a loss of control").

The defining tension, quoted: "many AI tools let AI take the wheel, but at the cost of auditability and repeatability that enterprises require." And the win condition: "The best 'AI SOC' tools are those that mold to a user's business context out of the box, while enabling complete customization after the initial integration. Many AI SOC tools fail to scale well, as they can show an impressive demo, but fall over when tested in complex use cases."

## 8. The Future section — innovative capabilities Latio is tracking

- **Detection on Stream** — detections fire at ingest; index built on stream for flexible storage.
- **Identity Baselining** — baseline user behavior from IDP through endpoint to contextualize alerts.
- **Co-Pilots** — browser extensions that record response patterns and suggest analysis without forcing a tool switch.
- **Compression and Search** — making unindexed historical data queryable (Scanner.dev called out as the only one built for this).
- **Detection and Pipeline Health** — correlating detections against ingested logs to reveal blind spots (Fig called out).
- **Attack Simulation** — continuous exploit simulation to find blind spots and prune unneeded logs (Brava, Pentera called out).

## 9. Buyer's guide highlights

- Many cloud-native orgs start without a SIEM, investing first in "a combination of vulnerability and runtime protection features (CNAPPs)." This is a direct opening for AccuKnox: we are already the runtime + posture layer these teams bought first. The AI-SOC is the natural next layer on the data we already hold.
- First SIEM question in 2026: "how much do you value flexibility versus single platforms?"
- The most important warning, quoted: "Buying an AI SOC tool hoping it fixes underlying data or detection problems is how teams end up with an expensive workflow engine that hallucinates over incomplete logs - driving up costs and wasting time in the process."
- Latio's one piece of advice: "start with a plan for your data architecture. Every other improvement to the SOC depends on having enriched, properly routed, and well-formatted logs. No AI analyst automation can solve underlying data problems."

## 10. Latio's category definitions (the awards taxonomy)

- **SOC Platform Leader** — one-stop shop combining EDR + SIEM, often with routing, detection engineering, and managed services.
- **Threat Detection Leader** — cross-platform detections to consolidate detection logic and threat hunting.
- **Data Pipeline Leader** — innovative enrichment-on-ingest.
- **AI SOC Innovator** — expanded beyond pure incident response toward standardizing logs and improving detection. (Mate and Exaforce both won this.)
- **SIEM Disruptor** — complete SIEM functionality in a flexible, distributed context. (Exaforce won this.)
- **User Reliability Leader** — highly customizable across environments, or validated directly by Latio in-platform. (Exaforce won "User Reliability Disruptor.")

## 11. Vendor spotlights (compressed, with the differentiator each is credited for)

- **Datadog** — holistic security platform on top of observability. Bits AI Security Analyst is "one of the most capable agentic analysts on the market." Cross-domain investigations across K8s pod, Okta login, S3, CloudTrail in one tool. 100+ Content Packs.
- **Exaforce** — builds a security knowledge graph at ingestion time. Multi-model AI (semantic + behavioral + LLM reasoning). Ingests rules from existing SIEMs, queries CrowdStrike via CQL natively. Best for stitching detection/triage/investigation/response without a full SIEM migration. MDR wrap available.
- **Artemis** (emerging from stealth) — hybrid architecture, per-query decision to ingest vs federated search, strong detection engineering, identity baselining, dynamic response action generation.
- **Daylight** — AI-native managed SOC that leads with human analyst quality. 140+ integrations, agent permissions per integration. Counter-positions against bad MDR experiences.
- **Scanner.dev** — keeps data in customer-owned object storage, builds indexing to make it queryable, including years of historical CloudTrail. Lambda workers at query time. Ships an MCP server for agents.
- **SentinelOne** — normalized first + third-party data into OCSF in a searchable data lake early. Purple AI is the agentic analyst. Wayfinder TDR for 24/7 MDR. Observo AI acquisition (now Singularity AI Data Pipelines) and Prompt Security acquisition (AI security, AI red teaming, MCP proxies). Best for teams consolidating onto one platform or extending from endpoint.
- **AiStrike** — asset relationship DB + identity/asset baselining. Grades detection programs across feed quality, detection quality, MITRE coverage, threat exposure, efficacy; AI rule tuning.
- **Brava** — attack-simulation AI agents validate detection, prune unneeded logs, optimize storage (Aquarium backend). Coverage product scores against MITRE.
- **Mate** — knowledge-graph IS the foundation (Security Context Graph from one integration). Agentic investigation + federated detection engineering. Plan mode with explicit workflow checklists. CD/CR feedback loop. Detections exported to Sigma for portability. Self-hosted option alongside customer data lakes.
- **7AI** — expanded from agentic triage/investigation into a broad data platform. Focused response agents per evidence shape (endpoint vs email/phishing). Harden (proactive) and Data Lake modules with a knowledge graph.

## 12. The single biggest gap AccuKnox can exploit

Read the whole report and notice what is missing: **not one of these vendors enforces anything.** Every single platform detects, triages, investigates, recommends, and at most "executes response actions" through API integrations (disable a user in Okta, isolate a host in CrowdStrike). None of them stop the action at the kernel before it completes. None of them treat the AI agents doing this work as untrusted workloads that need runtime isolation.

AccuKnox's wedge into this market, in one line: **everyone else is building a faster way to find out you were breached. AccuKnox is the only one that can also block it at runtime and prove the agents doing the analysis can't be turned against you.**

Three credible AccuKnox claims grounded in this report:
1. "Latio's own conclusion is that the data layer decides everything. We built the data layer on eBPF runtime truth, not best-effort log scraping."
2. "Latio warns that AI-SOC tools hallucinate over incomplete logs. Runtime enforcement telemetry is ground truth from the kernel, not a parsed log that may have silently stopped firing."
3. "Every vendor in this report investigates and recommends. AccuKnox is a CNAPP that already blocks at the kernel. The AI-SOC is the intelligence layer on top of enforcement we already do."

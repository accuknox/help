# Raw Research — AI-SOC Market Synthesis (June 2026)

Purpose: the strategic read on the category. Where it came from, where it is, where it is going, and the specific opening AccuKnox has. This synthesizes the Latio report, the Harvey architecture, the vendor teardowns, and the pricing/market benchmarks into one strategic picture. Numbers and sources live in [03-pricing-and-market-benchmarks](03-pricing-and-market-benchmarks.md).

---

## 1. Category definition

There is no clean consensus name yet. Latio's own framing: "AI SOC has become how every vendor positions themselves, leading to more confusion than ever." Here is the honest map.

What the market calls it: AI SOC, agentic SOC, autonomous SOC, AI-driven SecOps, AI analyst, the cognitive SOC. All point at the same shift.

The actual definition that holds up (Exaforce's is the cleanest): an AI-SOC uses autonomous agents to detect, triage, investigate, and respond to threats without requiring manual analyst involvement at every step. The useful sub-distinction:
- **AI-assisted SOC**: humans drive, AI surfaces data and summarizes.
- **Agentic AI-SOC**: AI agents drive investigation and response, humans supervise and handle escalations.

The whole market is racing from the first to the second.

AccuKnox's contribution to the definition: a third axis nobody else occupies. Every vendor's "response" is an orchestrated API action through an integration (disable a user, isolate a host, delete an email, quarantine an endpoint). None enforce at the kernel. AccuKnox adds **runtime enforcement** to detect-triage-investigate-respond. The category AccuKnox should try to name and own is the **runtime-aware, enforcing AI-SOC**, or in AccuKnox's existing language, the AI-SOC as the intelligence layer on top of Zero Trust runtime enforcement.

## 2. The two-wave story (the narrative spine for all content)

From Latio's Pulse post, and it matches what the teardowns show.

- **First wave (SOAR + AI).** LLMs bolted onto SOAR to automate incident response. Failure modes: summaries that add nothing, enrichments cheaper to run in the SIEM, verbose output instead of guidance, unoptimized queries that drive up cost, manual knowledge-base upkeep. Latio's verdict: "at their worst, they can spin in circles investigating meaningless information while driving up costs."
- **Second wave (AI-native, "Claude Code for the SOC").** Agents take actions, investigate alongside the analyst, learn org context continuously, leave the analyst in control, and can be tuned toward autonomy. UX is the differentiator. Latio, a former skeptic, was converted by the shift from "copy pasting in and out of ChatGPT" to a Cursor-like investigative partner.

AccuKnox's position: skate to where the puck is going. The second wave fixed the analyst experience. The next move, the one AccuKnox is uniquely built for, is closing the loop from investigation to enforcement so the SOC stops threats instead of just understanding them faster.

## 3. The data-layer thesis (the most important strategic insight in the research)

Two completely independent sources reach the same conclusion.
- Harvey: "Invest in your log warehouse before you invest in your agents." "The difference between 200ms and 2s per query is the difference between an agent that explores three hypotheses and one that explores 30."
- Latio: "start with a plan for your data architecture. Every other improvement to the SOC depends on having enriched, properly routed, and well-formatted logs. No AI analyst automation can solve underlying data problems."

The shared lesson: the agent is only as good as the data under it. Bad data means hallucination, cost, and circular investigation. This is the single biggest reason AI-SOC pilots fail (and why Gartner expects >40% of agentic AI projects canceled by end of 2027).

AccuKnox's data-layer advantage, stated plainly: AccuKnox does not start from scraped logs. It generates runtime telemetry from the kernel via eBPF and already maintains a CNAPP asset and blast-radius graph. That is ground truth, not best-effort ingestion. On the exact axis the whole category agrees decides everything, AccuKnox has a structural head start. This must be the lead technical argument.

## 4. Market sizing and momentum

Headline numbers (full sourcing in the pricing/market dump):
- Cybersecurity Agentic AI: $1.83B (2025) to $7.84B (2030), ~34% CAGR.
- Agentic AI Security (broader): $1.65B (2026) to $13.52B (2032), 42% CAGR.
- AI in Cybersecurity overall: $25B+ today, heading to $50B to $94B by 2030 to 2031 depending on the house.
- Gartner: by 2028, 70% of large SOCs will pilot AI agents for Tier-1/2; multi-agent AI in threat detection rises from 5% to 70%. But only 15% will see measurable improvement without structured evaluation, and >40% of agentic projects will be canceled by end of 2027.

The read: huge tailwind, real money, and a credibility gap. The winners will be the ones who can prove value and survive evaluation. That favors a vendor who can show a hard outcome (a blocked syscall, a prevented breach) over one who can only show a faster summary.

## 5. Demand-side pain (why now)

The SOC is structurally underwater. Headline stats: 71% of analysts burned out, 64% considering leaving, average tenure 18 to 24 months, ~960 alerts/day (3,000+ at enterprises), 40% of alerts never investigated, 50 to 80% false positives, ~70 minutes to investigate one alert. US average breach cost $10.22M, 241-day mean time to identify and contain. AI/automation in security ops saves ~$1.9M per breach and cuts the lifecycle ~80 days.

Mate's framing is the sharpest version of the "why now": the volume "stops being mathematically possible to handle at human speed with the current architecture." You cannot hire your way out. This is the demand thesis. Use it.

## 6. The AI-as-attacker accelerant

A recurring theme across vendors: AI gave attackers machine scale (Exaforce's hero line). Mate argues AI is "the New C2 for Supply Chain Attacks," with LLMs running the operator loop to scale commodity compromises into mass exploitation. Time-to-exploit is collapsing (Latio: AI makes first-party apps easier to attack and "time to exploit plummets").

Plus the new attack surface: 13% of orgs reported breaches of AI models or applications, 97% of those lacked AI access controls, and high shadow-AI use adds $670K to the average breach. Gartner: by 2028, 50% of cybersecurity IR effort will focus on incidents involving custom-built AI applications.

This is where AccuKnox's whole AI-Security 2.0 stack stops being a side feature and becomes central. The AI-SOC is not just AI helping the SOC. It is the SOC that can secure AI, including its own agents. No other AI-SOC vendor can say that.

## 7. Competitive landscape, mapped for AccuKnox

Three buckets, by where each plays:

- **Incumbent platforms extending into AI-SOC**: SentinelOne (Purple AI, Athena, AI-SIEM), Datadog (Bits AI), Microsoft (Sentinel + Security Copilot). Strength: installed base, data already there. Weakness: closed, endpoint or observability rooted, no kernel enforcement, AI security is acquired and bolted on.
- **Agentic data platforms (the serious startups)**: Exaforce, Mate, Artemis, 7AI, AiStrike, Conifers, Daylight, Scanner, Brava. Strength: modern data architecture, polished agentic UX, fast. Weakness: log-ingestion grounded (hallucination risk they all have to defend against), no enforcement, no AI-agent security, mostly closed, venture-funded burn.
- **Autonomous analyst point tools**: Dropzone, Radiant, Prophet, Intezer, Simbian. Strength: fast time-to-value, clean ROI story (replace a Tier-1 analyst). Weakness: narrow (triage/investigation only), depend entirely on the data and tools they sit on top of, no posture, no runtime, no enforcement.

AccuKnox does not fit cleanly in any bucket, which is the point. It is a CNAPP with runtime enforcement and a full AI-security stack, adding the agentic intelligence layer on top. The closest analog is "what if Exaforce's data platform sat on eBPF runtime truth and could enforce at the kernel and secure its own agents." That is the whitespace.

## 8. The four claims AccuKnox can make that no competitor can

1. **We enforce, we do not just respond.** Block the syscall at the kernel before it completes, on Kubernetes, VMs, containers, and AI workloads. Everyone else acts through API integrations after the signal.
2. **Our data layer is runtime ground truth, not scraped logs.** eBPF telemetry from the kernel plus a CNAPP asset graph. On the axis the whole category agrees decides everything, we start ahead.
3. **We secure the AI agents themselves.** When the SOC is agentic, the agents are an attack surface. KnoxClaw and ModelArmor isolate them in-kernel. Harvey says you must isolate SOC agents at the trust boundary; AccuKnox is the only one that can enforce it.
4. **We are open source at the core.** KubeArmor and ModelArmor are CNCF, 1M+ downloads, auditable. For the majority of teams that distrust black boxes, that is the trust wedge.

## 9. The honest risks AccuKnox must address head-on (anti-FUD on ourselves)

- AccuKnox does not yet ship a mature, polished agentic-analyst UX matching Exaforce's 20 screens. The PRD must close this. ClawArmor is announced; the rest is roadmap.
- The data-ingestion breadth in the Phase 1 brief (firewalls, EDR, AD, Okta, O365, etc.) is broad and overlaps with what incumbents already have wired up. AccuKnox needs connectors fast.
- "We enforce at the kernel" is strongest for cloud-native and AI workloads. It is weaker for pure SaaS and identity-only incidents where there is no kernel to enforce on. Be precise about where enforcement applies and where AccuKnox orchestrates response like everyone else.
- Pricing must avoid re-importing SIEM cost pain (do not bill per GB or per alert as the primary meter). See the pricing deliverable.

These are the open questions and assumptions that feed the final log.

# Positioning playbook, play to AccuKnox strengths

A comparison page exists to make one decision easy. The buyer should finish the page knowing when
to pick AccuKnox, and every row should push that decision. This file holds the method. The sourcing
rule in `SKILL.md` still governs every cell, so a strength you cannot source is a strength you
cannot print.

The method comes from the Netskope AI security battlecard, rebuilt on 2026-09-25. The first draft
scored rows neutrally and conceded 3 of 16 rows. The rebuild conceded none, cited the same vendor
documentation, and stayed accurate. The difference was row selection and framing.

## Decide the Winning Frame Before the First Row

Pick the one contrast that makes AccuKnox the obvious answer, then build the page around it. Write it
as a headline of ten words or fewer.

| Competitor shape | Frame that wins |
| --- | --- |
| SSE, SWG or CASB vendor (Netskope, Zscaler) | They identify AI traffic. AccuKnox protects the AI you run. |
| Endpoint or browser-only tool | They see laptops. AccuKnox also covers servers, clusters and clouds. |
| Point AI-firewall startup | They guard prompts. AccuKnox secures the model, agent, host and cloud. |
| Red-teaming-only tool (Promptfoo) | They find the flaw. AccuKnox finds it and enforces the fix at runtime. |
| CNAPP incumbent (Prisma, Wiz) | They alert. AccuKnox prevents inline, on-prem and air-gapped too. |

The frame goes in the H1 or the first line under it. Everything below it is evidence.

## Split AI Security Into Two Groups

For an `ai-security` page, split the rows into two groups. The split shows breadth that a single
flat list hides.

1. **AI for Security.** AccuKnox uses AI to improve its own security workflows. The rows are AI SAST,
   AI DAST, AgentZ and AI-powered pentesting. Most AI-security competitors ship no AppSec testing,
   so these rows are often clean wins.
2. **Security for AI.** AccuKnox secures the AI the customer runs. The rows are shadow AI discovery
   and enforcement, cloud AI security, on-prem and self-hosted AI, managed agents, Prompt Firewall
   and browser protection, AI Gateway, agent runtime sandboxing, model security and audit, AI BOM,
   red teaming, runtime guardrails, and AI detection and response.

`parameter-sets.md` holds both groups as a ready row set.

## Keep a Row Only When It Moves the Decision

A row stays when it passes one of three tests. Cut every other row.

1. **AccuKnox advantage.** AccuKnox does it and the competitor does not, or does less.
2. **Competitor limitation.** The competitor's own docs show a Preview label, a Beta label, a
   separate license, a quota, a platform gap or a stated blind spot.
3. **Strategic parity.** Both ship it, the buyer expects to see it, and AccuKnox has an edge worth
   one line. Red teaming is the usual case. Keep the row short and name the edge.

Cut these rows on sight. Each one fills space and moves nothing.

- A generic deployment-model row. Fold the deployment fact into the capability it changes. The
  on-prem control plane belongs in the on-prem AI row.
- A licensing-model row. Pricing units are not a capability, and AccuKnox rarely publishes its own.
- A generic compliance or AI GRC row where both sides map to OWASP and MITRE.
- Any "both support X" row with no edge.
- An MCP discovery row against a vendor that ships an MCP broker. Use the host-scanning angle
  instead, where AccuKnox scans the server that runs the MCP process.

## Hunt for Advantages in the Competitor's Own Docs

The strongest gap is one the competitor states. Read their docs for these eight signals, and quote
the page that carries each one.

| Signal | What to look for | Netskope example, read 2026-09-24 |
| --- | --- | --- |
| Maturity label | Preview, Beta, early access, "contact support to enable" | AI Platforms posture is Preview. Agent Action Control is Beta. |
| Separate license | Add-on SKUs for DLP, brokers, gateways | DLP and Agentic Broker need their own license. |
| Traffic steering | "Traffic must be steered", proxy, client, tunnel | Guardrails work only on traffic steered through Netskope. |
| Stated blind spot | "Does not detect", "not supported", "only" | The Client misses AI in VMs and containers without the Client. |
| Coverage ratio | Apps identified against apps enforced | 3,300+ GenAI apps identified. Inline guardrails cover 20 listed apps. |
| Platform or OS gap | Client versions, OS lists, cloud lists | Client AI discovery runs on Windows and macOS only. |
| Hosting constraint | Cloud-only console, egress needs, appliance sizing | The console runs only in the Netskope tenant. The gateway is a 16 vCPU appliance. |
| Quota or billing cliff | Per-asset caps, monthly transaction limits | AI Gateway bills per gateway plus monthly transactions. |

A coverage ratio is the most persuasive single fact on a page, because the buyer can check it.

## Separate Discovery From Enforcement

"Identify ≠ protect" is the core message against any vendor that leads on app discovery. Count what
the vendor identifies, then count what it enforces on, and print both numbers.

State the gap as precisely as the source allows.

- The source confirms a limit. Write the limit. "Inline guardrails cover 20 listed apps."
- The source shows discovery and says nothing about enforcement. Write "Discovery documented.
  Equivalent enforcement not shown."
- Never write "cannot block" unless their docs say so.

Position AccuKnox on the verbs that follow discovery: block, mask, redact, sandbox, revert.

## Use Five Status Labels and Nothing Else

| Label | Use it when | Color |
| --- | --- | --- |
| Supported | AccuKnox or the competitor ships it GA | green |
| Not supported | The competitor's docs cover the product area and the capability is absent | red |
| No equivalent | The competitor has something nearby that does a different job | red |
| Limited | The competitor has it in part, in Preview or Beta, or behind a separate license | amber |
| Parity | Both ship it GA with no meaningful gap | purple |

Write "Not supported" rather than "Not documented" when you read the competitor's full docs index
for that product area. "Not documented" reads as unfinished research. Keep "Limited" for real
partial coverage. A page with eight Limited rows and no Not supported rows reads as timid.

AccuKnox Beta features still count. Label them Beta inside the AccuKnox cell and keep the row only
when the rest of the row is a win.

## Write a Buyer Takeaway That Names the Win

Every row ends with a takeaway of eight words or fewer. It names what the buyer gets. It never
praises.

| Passes | Fails |
| --- | --- |
| Enforces policy beyond app discovery | Better security |
| Your AI stays in your data center | Strong platform |
| Every managed agent in one view | Comprehensive coverage |
| Stops a rogue agent on the host | More advanced |
| Unsafe models never load | Industry-leading |

## Open With the Reason to Pick AccuKnox

Put a "Pick AccuKnox to" strip at the top, with four reasons and one icon each. Follow it with a
one-line tally, such as "15 of 16 AccuKnox leads, 8 Netskope not supported, 7 limited, 1 parity".
The tally doubles as the color legend, so skip a separate legend.

Leave out a "Where the competitor leads" section. When the competitor has a real strength, keep it
inside the row and draw the distinction there, as the discovery-versus-enforcement row does.

## Stay Accurate While You Play to Strengths

Framing decides which true facts appear and in what order. It never changes a fact.

- Every competitor cell still links to the competitor's own page, per `SKILL.md`.
- Every AccuKnox cell still reaches a help-docs page or a data point with a stated source in
  `references/source-of-truth/ai-security-data-points.md`.
- A capability that someone at AccuKnox asserts but no doc shows goes in brackets on a web page. On a
  sales PDF, it can ship only when the requester confirms it, and the reply names it as unsourced.
- Section 10 of `.claude/core/writing-rules.md` still holds. State the gap flatly. No adjectives
  about the competitor.

## Related

- `parameter-sets.md`, the two-group `ai-security` row set
- `battlecard-pdf.md`, the PDF layout and density rules
- `references/source-of-truth/ai-security-data-points.md` at the repo root, the current AccuKnox data points
- `references/competitive/battlecards/netskope/evidence-log.md`, the Netskope source log

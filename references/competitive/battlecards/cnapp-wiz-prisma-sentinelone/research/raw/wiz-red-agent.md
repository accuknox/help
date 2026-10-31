[Wiz](https://www.wiz.io/)

- [Sign in](https://app.wiz.io/login)
- [Under attack?](https://www.wiz.io/experiencing-an-incident)

[Get a demo](https://www.wiz.io/demo?cta_source=blog&cta_page=/blog/wiz-red-agent-is-ga&cta_placement=nav)

![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)

We are excited to announce that [**Red Agent**](https://www.wiz.io/blog/introducing-the-wiz-red-agent) **is now generally available (GA)**. Customers have rapidly adopted our AI attacker to close the widening gap between traditional security scanners and the speed at which adversaries exploit vulnerabilities using AI.

Its impact was clear during preview:

- **Over 10,000** validated critical exploitable risks were discovered by the Red Agent- externally facing risks with no authentication- that, if found by attackers, could have led to a significant impact.

- **70% of organizations** that enabled Red Agent discovered a High or Critical vulnerability they were completely unaware of.

- **35% of organizations** found their first verified Critical vulnerability within 1 hour of activating scans.

- **Proven scale**: At its peak, Red Agent scanned **350,000 assets** and processed **480B tokens** in a single day.


Behind these numbers are our customers transforming how they defend with AI:

> The Red Agent for attack surface management and automated penetration testing is incredibly valuable. We didn't have coverage over infrastructure-related automated pen testing prior to Wiz.
>
> Patrick O’Boyle, Founding security engineer and Head of GRC, Rogo

> Red Agent finds what humans miss. It caught critical authorization flaws across services where traditional testing and our bug bounty program came up short. We had continuous AI-powered attack surface testing on our roadmap. Wiz got there first, and did it better than we would have.
>
> Emil Vaagland, Head of Product Security, Vend

## **The New Reality: Why AI Threat Readiness Matters Now**

Attackers are using frontier AI models to scan perimeters, discover zero-days, and weaponize complex application vulnerabilities in hours instead of months. Relying purely on human-paced security workflows against AI-speed adversaries creates a compounding coverage deficit. Staying ahead of this pace requires deploying AI for defense.

Organizations are prioritizing [AI Threat Readiness](https://www.wiz.io/blog/wiz-ai-threat-readiness-operating-model?cta_source=blog&cta_page=/blog/ai-threat-readiness-framework&cta_placement=hero) to outpace automated adversaries, yet existing security security scanning has limitations:

- **Static scanners miss logic flaws**: Traditional tools rely on known CVEs and signature matching. They cannot reason about custom application workflows, broken access controls, or multi-step logic flaws in modern web applications and AI-generated code.

- **Manual penetration testing does not scale**: Identifying complex business logic vulnerabilities historically required manual testing. These engagements are expensive, take weeks to execute, and offer limited scope.

- **Point-in-time testing creates security gaps**: A manual pentest or annual audit captures a single snapshot in time. The moment new code ships or an API updates, new unmonitored security gaps open up.


## **AI Defense with the Red Agent**

[Red Agent](https://www.wiz.io/solutions/red-agent) helps teams stay ahead by running continuous, autonomous AI pentesting across custom-built software, vibe-coded applications, and APIs. While traditional scanners match signatures, Red Agent reasons through business logic to uncover unknown vulnerabilities such as OWASP API Top 10 Flaws, logic flaws, authorization bypasses, and more.

### **The Red Agent Modules**

#### **1\. Web API Crawler:** Uncover shadow APIs

An intelligent AI discovery tool that uses client-side code analysis to map API endpoints across your web applications and uncover hidden APIs. It automatically extracts and analyzes API specifications to understand endpoint structures, parameters, and expected behaviors and identifies unlinked or forgotten APIs that expose your organization to risk.

![](<Base64-Image-Removed>)![](https://www.datocms-assets.com/75231/1785326360-screenshot-2026-07-29-at-14-22-21-edited.png?fm=webp)

#### **2\. API DAST Attacker:** Continuously find  logic-driven vulnerabilities

Continuously uncovers and validates logic-driven exploitable risks by analyzing application behavior rather than following fixed scan patterns and static test cases. It treats target applications as dynamic systems, adapting its strategy in real time to reason about application logic and expose logic-driven risks. It thenprovides proofs of execution so your team receives verified findings, alongside reproduction steps.

![](<Base64-Image-Removed>)![](https://www.datocms-assets.com/75231/1785324244-screenshot-2026-07-29-at-14-23-53.png?fm=webp)

#### **3\. Secrets Blast Radius:** Validate and test secrets impact

The Red Agent validates the impact of secrets exposed in public websites and APIs, and in public code repositories to test that they are active and determine the exact scope of access they hold. It executes safe, non-disruptive validation checks directly against the respective third-party SaaS provider's APIs to confirm exploitability and determines the precise scope of permissions.

![](<Base64-Image-Removed>)![](https://www.datocms-assets.com/75231/1785324290-screenshot-2026-07-29-at-14-24-38.png?fm=webp)

## **The Red Advantage**

What sets Red Agent apart isn't just AI speed, it is about it’s deep contextual reasoning and how integrates into your security operations:

- **Deep context without manual setup:** Red Agent automatically ingests context from different Wiz sources: across API schemas, cloud resources, Runtime Sensor, code repositories, and network layers, and its own AI API Crawler. It being enriched by the Wiz context removes the need to manually configure context, and eliminates blind spots and gives the reasoning engine complete visibility.

- **Engineered by Wiz Research:** The threat intelligence and expertise of the Wiz Research team is built directly into the harness of the Red Agent, bringing top-tier security research into AI testing.

- **Truly continuous discovery:** Rather than relying on a fixed schedule against pre-selected target lists, Red Agent continuously discovers and tests both known and unknown applications across your entire footprint by leveraging an up-to-date inventory of your environment from Wiz, removing the need to predefine target groups.

- **Automated remediation loop:** Paired with Green Agent and Wiz Workflows, Red Agent customers can generate precise fix guidance with the Green Agent and scale response with Wiz Workflows.


## **Caught in the Wild: Real-World Exploits**

The types of risks Red Agent uncovers remain in the shadows for organizations across every industry. Our [Red Agent POV](https://www.wiz.io/blog/red-agent-pov-series) series documents how Red Agent identified these logic flaws in live environments across airline, financial, and technology companies:

### **1\.** [**Finding a m** ulti-step attack chain allowing SSRF-to-Local-File-Read](https://www.wiz.io/blog/red-agent-pov-ssrf)

A GCP Cloud Run application restricted input to valid GitHub URLs (\[https://github.com/\](https://github.com/)...). Red Agent bypassed the path restrictions to read the host's local filesystem (/proc/self/environ), extracting live GCP service-account credentials and full application source code.

### **2.** [Exploiting Broken Object-Level Authorization in an Airline GraphQL API](https://www.wiz.io/blog/red-agent-pov-bola)

An airline API generated distinct session tokens for authentication, but downstream GraphQL resolvers failed to validate user roles. Red Agent cycled sequential integer IDs across unprotected resolvers, exposing two years of passenger PII and unlocking controls to modify active flight bookings.

### **3\.** [The One Boolean That Broke a B2B Platform’s Credit System](https://www.wiz.io/blog/red-agent-pov-business-logic)

A B2B directory gated contact data behind a paid credit system. Red Agent identified an unreferenced request parameter accepted by the backend. Appending the flag returned unmasked phone numbers and emails on free-tier requests, bypassing the core monetization model.

## **Want to see more?**

Get started today, review [the docs](https://docs.wiz.io/docs/red-agent) (login required) or [book a live demo](https://www.wiz.io/demo) with our team. To learn more about the Red Agent findings explore the [Red Agent POV](https://www.wiz.io/blog/red-agent-pov-series) blog series.

Tags

[#Product](https://www.wiz.io/blog/tag/product)

## Continue reading

[![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)](https://www.wiz.io/blog/the-risk-hiding-behind-exposed-mcp-servers)

[**The risk hiding behind exposed MCP servers**](https://www.wiz.io/blog/the-risk-hiding-behind-exposed-mcp-servers)

[![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)](https://www.wiz.io/authors/hila-ramati)

[Hila Ramati](https://www.wiz.io/authors/hila-ramati)

July 28, 2026

How unauthenticated Model Context Protocol (MCP) servers are opening doors to sensitive cloud data, IAM, and command execution.

[![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)](https://www.wiz.io/blog/cisa-bod-26-04-alignment-with-wiz)

[**Accelerating CISA BOD 26-04 Vulnerability and Triage Activities through Wiz**](https://www.wiz.io/blog/cisa-bod-26-04-alignment-with-wiz)

[![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)](https://www.wiz.io/authors/aviram-ben-kalifa)[![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)](https://www.wiz.io/authors/bryan-rosensteel)

[Aviram Ben Kalifa](https://www.wiz.io/authors/aviram-ben-kalifa), [Bryan Rosensteel](https://www.wiz.io/authors/bryan-rosensteel)

July 28, 2026

Wiz enables organizations to continuously assess environments against the CISA KEV catalog, automating risk prioritization, rapid remediation, and forensic triage workflows.

[![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)](https://www.wiz.io/blog/atlas-ai-vulnerability-researcher)

[**Atlas: Wiz's autonomous AI Agent for vulnerability research, ranked \#1 on CyberGym**](https://www.wiz.io/blog/atlas-ai-vulnerability-researcher)

[![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)](https://www.wiz.io/authors/nir-ohfeld)[![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)](https://www.wiz.io/authors/yuval-avrahami)

[Nir Ohfeld](https://www.wiz.io/authors/nir-ohfeld), [Yuval Avrahami](https://www.wiz.io/authors/yuval-avrahami)

July 27, 2026

See how Wiz built Atlas, an autonomous AI system for vulnerability research that validates every finding with a real, working exploit.

Get a personalized demo

## Ready to see Wiz in action?

> "Best User Experience I have ever seen, provides full visibility to cloud workloads."

David EstlickCISO

> "Wiz provides a single pane of glass to see what is going on in our cloud environments."

Adam FletcherChief Security Officer

> "We know that if Wiz identifies something as critical, it actually is."

Greg PoniatowskiHead of Threat and Vulnerability Management

[Get a demo](https://www.wiz.io/demo)

a26988130118.cdn.optimizely.com

# a26988130118.cdn.optimizely.com is blocked

This page has been blocked by an extension

- Try disabling your extensions.

ERR\_BLOCKED\_BY\_CLIENT

Reload


This page has been blocked by an extension

![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)

![](https://www.datocms-assets.com/75231/1785326360-screenshot-2026-07-29-at-14-22-21-edited.png?fm=webp)

![](https://www.datocms-assets.com/75231/1785324244-screenshot-2026-07-29-at-14-23-53.png?fm=webp)

![](https://www.datocms-assets.com/75231/1785324290-screenshot-2026-07-29-at-14-24-38.png?fm=webp)
[Wiz](https://www.wiz.io/)

- [Sign in](https://app.wiz.io/login)
- [Under attack?](https://www.wiz.io/experiencing-an-incident)

[Get a demo](https://www.wiz.io/demo?cta_source=blog&cta_page=/blog/introducing-wiz-ai-sast&cta_placement=nav)

![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)

We’re excited to announce that Wiz AI SAST is available as a Public Preview capability, bringing frontier-grade vulnerability discovery to all Wiz Code customers.

AI models have become highly adept at finding complex flaws in application code that traditional scanners often miss. Security teams historically addressed this gap with manual reviews and quarterly pentesting, but neither of those approaches scale in a world where code is written and exploited at machine speed.

Wiz AI SAST addresses this gap by analyzing how your application actually behaves to uncover a broader range of weaknesses (CWEs) that typically go undetected by rules-based scanners. It's powered by the [Atlas harness](https://www.wiz.io/blog/atlas-ai-vulnerability-researcher) we shared earlier this year, grounded in Wiz Research, and continuously refined by our investments in [AI security](https://www.wiz.io/academy/ai-security).

Code findings are correlated with what is actually running in production on the Wiz Security Graph, so teams instantly understand which vulnerabilities matter most. Prioritized findings flow through the existing policy, ownership, and remediation workflows AppSec teams already use, making AI-powered vulnerability detection part of your existing program rather than another tool to manage.

As a core part of our [AI Threat Readiness Framework](https://www.wiz.io/blog/ai-threat-readiness-framework), Wiz AI SAST complements a broader portfolio of solutions designed to help organizations stay ahead of cyberthreats in the AI era.

## Frontier Grade Code Analysis without the Overhead

Running AI code scanning in production takes far more than a capable model. Teams have to build a harness that turns that model into a capable security researcher, evaluate new models as they ship, and manage the lifecycle of findings into security workflows. Done in-house, it requires a significant, ongoing investment from skilled security and engineering teams. Wiz AI SAST handles all of that out-of-the-box so organizations can operationalize [AI code scanning](https://www.wiz.io/academy/application-security/ai-code-security) quickly to improve their risk posture.

### A Harness Backed by Research and Results

Wiz AI SAST shares the same underlying technology as [Atlas](https://www.wiz.io/blog/atlas-ai-vulnerability-researcher), a research initiative we shared earlier this year. At the time, Atlas held the number one spot on [CyberGym](https://www.cybergym.io/cybergym/) and uncovered more than 200 vulnerabilities in widely used open source software.

![](<Base64-Image-Removed>)![](https://www.datocms-assets.com/75231/1790883950-1785117166-image-1.webp?fm=webp)

Upon launch in July 2026, Wiz Atlas ranked number one on CyberGym, the public benchmark for AI driven vulnerability research. The research and technology behind Atlas powers Wiz AI SAST.

We continuously tune our harness with learnings from real-world vulnerability research, attacker techniques, and scanning across Wiz's cloud security footprint. Organizations benefit from our expertise without having to build and maintain the complex AI infrastructure required for security specific use cases.

### Model Selection Driven by Continuous Benchmarking

Our work on the [Cyber Model Arena](https://www.wiz.io/cyber-model-arena) shows that AI security performance isn't a property of the model alone. It depends on the model and harness together. That makes evaluation a moving target: every new model release means retesting every pairing against real-world security tasks.

As an AI vendor-agnostic platform, we continuously run these evaluations and swap the strongest—and most efficient—model into the [AI SAST](https://www.wiz.io/academy/application-security/ai-sast) harness. This includes cutting edge cybermodels made available to us through our partnership with [Google DeepMind](https://deepmind.google/).

![](<Base64-Image-Removed>)![](https://www.datocms-assets.com/75231/1791322828-screenshot-2026-10-06-at-5-38-40-pm.png?fm=webp)

Wiz Research constantly evaluates AI agents with foundation models and standard harnesses on multiple real-world cybersecurity tasks. This benchmarking allows us to apply the best, most efficient models into the AI SAST harness.

For security teams, the value is simple: you don’t need to constantly track new model releases, benchmark them against security tasks, or decide which model to use. We handle that complexity behind the scenes, ensuring your code and applications are always scanned with the best model.

### Turning Non-Deterministic AI into a Scalable Security Program

Delivering an enterprise-grade AI AppSec program requires managing the full lifecycle of vulnerability discovery, starting with deciding what to scan. AI code analysis is resource intensive and not every asset requires the investment of AI reasoning. Using Mika AI, security teams can prioritize the critical repositories that warrant AI code scanning by drawing on context such as cloud exposure, access to sensitive data, and business criticality.

![](<Base64-Image-Removed>)![](https://www.datocms-assets.com/75231/1791291567-image-5-edited.png?fm=webp)

Mika AI helps you prioritize which repositories warrant AI code scanning using context such as cloud exposure, access to sensitive data, business criticality, and more.

Once those prioritized scans are running, Wiz addresses the next phase of the lifecycle: the outputs. Because Large Language Models (LLMs) are inherently non-deterministic, they can generate different results from one run to the next. This creates a major operational challenge for security teams who need consistency in findings.

To solve this we supplement the AI scan engine with automated lifecycle management to maintain finding states across scans:

- **Retest:** Before scanning for new risks, the engine re-examines existing findings to confirm they're still valid. If the code has been fixed, the finding is automatically marked resolved.

- **Deduplicate:** Rather than matching on line numbers or file paths, the engine correlates new findings with existing ones using security context and code semantics. Even if the AI changes a bug's title or description, our AI SAST recognizes the underlying root cause and reconciles it into a single, stable finding.


Wiz handles this lifecycle between scans automatically, ensuring teams work with stable findings that can be assigned, tracked, remediated, and closed—not a new, disconnected set of AI outputs after every scan.

As a result customers get the deep detection benefits of AI without giving up the predictable workflows they expect from enterprise security tools. By eliminating the manual burden of managing non-determinism, this built-in continuity dramatically reduces the Total Cost of Ownership (TCO) of AI-powered security.

![](<Base64-Image-Removed>)![](https://www.datocms-assets.com/75231/1790884001-screenshot-2026-10-01-at-3-46-21-pm.png?fm=webp)

Wiz tames the non-determinism of AI scanners by managing the full lifecycle of findings. CWEs are retested to confirm they are still valid and new findings are correlated with existing ones using security context and code semantics to prevent security teams from triaging duplicate results.

Click through the feature tour

## See how Wiz AI SAST works

Guided Tour - AI-SAST (5 Steps)

See Wiz AI SAST in action


## Visibility into a New Class of CWEs

Wiz AI SAST extends detection coverage into the logic-based vulnerabilities that have always been hardest to catch, like broken access control, flawed input validation, and misapplied cryptography. Finding them requires a semantic understanding of what the code is supposed to do, which is something AI does exceptionally well.

A practical example can be found below. Wiz AI SAST detected an Insecure Direct Object Reference (IDOR) flaw in an E-commerce basket endpoint, where any authenticated user could read another user's cart by changing the ID in the URL. Rules based engines would miss this type of risk because the syntax of the code is fine but it's the missing ownership check that makes it exploitable.

![](<Base64-Image-Removed>)![](https://www.datocms-assets.com/75231/1790884122-screenshot-2026-10-01-at-3-45-02-pm-edited.png?fm=webp)

Findings from Wiz AI SAST are accompanied by confidence scores, investigation summaries, and reproduction commands so security teams can trust results.

The practical takeaway for AppSec teams is that AI analysis doesn’t replace rules based scanning completely, but rather it extends it. Deterministic scanning provides fast, cost-effective coverage for syntax based flaws, while AI SAST adds the deep reasoning needed to catch intent-dependent flaws like the IDOR above. Together, they give AppSec teams broader coverage of risk across the entire application attack surface.

## Prioritize Exploitable Risks with Code-to-Infrastructure Context

The best AI models in the world are ultimately limited by their access to relevant context. A model evaluating code in a vacuum is blind to how that application actually operates in the real world.

By grounding our AI SAST engine in the Wiz Security Graph, the model investigates your code with full awareness of your infrastructure, identity configurations, and runtime environment. This context serves two critical purposes:

1. **Uncovering Hidden Risk:** It allows the AI to discover complex vulnerabilities that only exist at the intersection of application logic and infrastructure flaws that standalone AI code scanners cannot detect.

2. **Prioritizing True Attack Paths:** It drastically reduces triage fatigue by correlating code weaknesses with additional context to surface [critical attack paths](https://www.wiz.io/academy/detection-and-response/attack-path-analysis) that matter most for remediation.


That same deep context is what allows our [Red Agent](https://www.wiz.io/solutions/red-agent?utm_source=google&utm_medium=ppc&utm_campaign=brand-search-us-ca&utm_term=wiz%20red%20agent&utm_adgroupname=%7Bwiz-red-agent%7D&utm_device=c&gad_source=1&gad_campaignid=16454072093&gbraid=0AAAAABYVGbJTKsBSdCbgyspGmeCF82wkw&gclid=Cj0KCQjw8ofWBhCHARIsANBj4LszniLSkWMF_3b7fZdsjux_Up2vZjuc2g1v7aVzVd3jACB5nOs4jPgaAtUkEALw_wcB) to validate exploitability from the outside in, testing these AI-discovered findings against your live environment exactly the way an attacker would.

![](<Base64-Image-Removed>)![](https://www.datocms-assets.com/75231/1791153231-screenshot-2026-10-04-at-6-32-15-pm-edited.png?fm=webp)

The Wiz Security Graph correlates signals across the code, cloud, and runtime environment to surface attack paths. Here Wiz AI SAST flagged a broken authentication weakness in an AI agent's API, where the endpoint accepted any bearer token as valid. Our Red Agent used that context to attack the live application from the outside in. While the underlying database was correctly protected, the AI chat agent exposed the same data without access controls, allowing Red Agent to exfiltrate sensitive customer, employee, and financial data.

## Remediate at Machine Speed with the Green Agent

Detecting and validating risk at machine speed only pays off if remediation keeps up. The [Wiz Green Agent](https://www.wiz.io/blog/introducing-wiz-green-agent) investigates the underlying findings and builds a remediation plan grounded in the full context of your code, pipeline, infrastructure, and runtime, going beyond the generic guidance a standalone model produces.

It pinpoints the right owner, maps the steps to fix the root cause, and can even share context with an AI coding agent like Claude Code to carry out the fix in code. And with Wiz Workflows, teams can turn Green Agent’s intelligence into multi-step automated response chains tailored to their [DevSecOps playbooks](https://www.wiz.io/academy/application-security/what-is-devsecops).

![](<Base64-Image-Removed>)![](https://www.datocms-assets.com/75231/1791258872-screenshot-2026-10-01-at-3-45-16-pm-edited.png?fm=webp)

Wiz’s Green Agent runs a detailed investigation into remediation including ownership mapping, fixes in code, and can work with an organization's coding agent to create an agentic loop where fixing an issue is as fast as finding one.

## Get Started

In the AI era, the best form of defense is to use AI on ourselves before threat actors can. Wiz AI SAST gives defenders a scalable solution to apply that philosophy against application code. But, it’s just one component of our broader vision for [Agentic Code Security](https://www.wiz.io/blog/agentic-code-security) where specialized AI agents work alongside security teams to autonomously investigate, prioritize, and remediate risk across the entire AI development lifecycle.

Wiz AI SAST is available now in Public Preview. If you’re an existing Wiz Code customer, get started by visiting our [documentation](https://docs.wiz.io/docs/sast-solutions). If you’re new to Wiz, [request a demo](https://www.wiz.io/demo) to experience frontier-grade vulnerability discovery first hand.

Tags

[#AI](https://www.wiz.io/blog/tag/ai) [#Wiz Code](https://www.wiz.io/blog/tag/wiz-code) [#Product & Company News](https://www.wiz.io/blog/tag/news)

## Continue reading

[![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)](https://www.wiz.io/blog/wiz-service-catalog-updates)

[**What’s New in Wiz Service Catalog: Smarter Discovery, Governance, and Service-Level Context**](https://www.wiz.io/blog/wiz-service-catalog-updates)

[![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)](https://www.wiz.io/authors/omer-mesika)[![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)](https://www.wiz.io/authors/kelsey-nelson)

[Omer Mesika](https://www.wiz.io/authors/omer-mesika), [Kelsey Nelson](https://www.wiz.io/authors/kelsey-nelson)

October 5, 2026

Build your Service Catalog faster, keep service context current, and give teams a clearer path from cloud risk to accountability

[![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)](https://www.wiz.io/blog/wizos-helm-charts)

[**Securing the Kubernetes Supply Chain: Introducing WizOS Helm Charts**](https://www.wiz.io/blog/wizos-helm-charts)

[![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)](https://www.wiz.io/authors/shay-berkovich)[![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)](https://www.wiz.io/authors/daniel-velikanski)[![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)](https://www.wiz.io/authors/roee-kanari)[![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)](https://www.wiz.io/authors/mike-mcguire)

[Shay Berkovich](https://www.wiz.io/authors/shay-berkovich), [Daniel Velikanski](https://www.wiz.io/authors/daniel-velikanski), [Roee Kanari](https://www.wiz.io/authors/roee-kanari), [Mike McGuire](https://www.wiz.io/authors/mike-mcguire)

September 30, 2026

Secure your Kubernetes supply chain with WizOS Helm Charts. Eliminate hidden CI/CD risks and unmaintained dependencies with hardened, signed, and CVE-scanned charts for seamless Kubernetes deployment.

[![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)](https://www.wiz.io/blog/blue-agent-data-exfiltration-investigation)

[**The Blue Agent POV: Investigating Multi-Platform Data Exfiltration Across AWS and GitHub**](https://www.wiz.io/blog/blue-agent-data-exfiltration-investigation)

[![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)](https://www.wiz.io/authors/blue-agent)[![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)](https://www.wiz.io/authors/zoe-rabi)

[Blue Agent](https://www.wiz.io/authors/blue-agent), [Zoe Rabi](https://www.wiz.io/authors/zoe-rabi)

September 29, 2026

See how the Blue Agent investigated a multi-platform attack in minutes, following evidence across AWS and GitHub to uncover compromised credentials, stolen source code, and custom data exfiltration tooling

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

![](https://www.datocms-assets.com/75231/1790883950-1785117166-image-1.webp?fm=webp)

![](https://www.datocms-assets.com/75231/1791322828-screenshot-2026-10-06-at-5-38-40-pm.png?fm=webp)

![](https://www.datocms-assets.com/75231/1791291567-image-5-edited.png?fm=webp)

![](https://www.datocms-assets.com/75231/1790884001-screenshot-2026-10-01-at-3-46-21-pm.png?fm=webp)

![](https://www.datocms-assets.com/75231/1790884122-screenshot-2026-10-01-at-3-45-02-pm-edited.png?dpr=0.75&fm=webp)

![](https://www.datocms-assets.com/75231/1791153231-screenshot-2026-10-04-at-6-32-15-pm-edited.png?dpr=0.75&fm=webp)

![](https://www.datocms-assets.com/75231/1791258872-screenshot-2026-10-01-at-3-45-16-pm-edited.png?fm=webp)
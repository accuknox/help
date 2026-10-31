[Wiz](https://www.wiz.io/)

- [Sign in](https://app.wiz.io/login)
- [Under attack?](https://www.wiz.io/experiencing-an-incident)

[Get a demo](https://www.wiz.io/demo?cta_source=blog&cta_page=/blog/introducing-wiz-sast-where-code-risk-meets-cloud-context&cta_placement=nav)

![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)

Modern development practices and AI copilots have dramatically increased the volume and velocity of code, with developers often moving from prompt → tab → commit in minutes.

Wiz Code was built from day one as a [complete ASPM platform](https://www.wiz.io/blog/wiz-named-aspm-leader-by-idc) to keep pace with that speed, combining native scanning for [SCA](https://www.wiz.io/academy/software-composition-analysis), secrets, sensitive data, IaC, and supply chain posture with the flexibility to ingest findings from popular code scanners. By bringing these signals together in the Wiz Security Graph, customers can correlate issues from code to cloud and drive action through the tools and workflows their teams already use.

Today, we’re expanding that foundation with Wiz SAST in Public Preview, enabling teams to scan their applications' code, understand its runtime impact, and fix issues using the same unified graph and workflows.

# Prioritize what matters, not everything detected

## Context first: zero-configuration code-to-cloud mapping

Securing modern applications starts with understanding how code actually behaves once it reaches the cloud. That’s why Wiz Code is built on top of the platform’s [**zero-configuration code-to-cloud mapping**](https://www.wiz.io/blog/the-missing-link-in-code-to-cloud-visibility-is-finally-here), allowing teams to see not just that a vulnerability exists, but _where it runs, how it’s deployed, and what it can access_.

Through repository analysis, registry scanning, and automated container lineage, Wiz traces:

_Source code → CI pipeline → Container repository → Container image_

![](<Base64-Image-Removed>)![](https://www.datocms-assets.com/75231/1764677251-screenshot-2025-12-02-at-13-06-52.png?fm=webp)

Code-to-cloud mapping example.

This happens without tagging, CI/CD hacks, or developer overhead.

This is where Wiz Code changes the rules. By enriching code security findings with actual deployment context, you can answer crucial questions for the first time:

- Is this vulnerable code actively deployed?

- Is this application internet-exposed, and does it handle sensitive or regulated data?

- Who owns it and who should fix it?


This is the kind of [ASPM foundation](https://www.wiz.io/academy/application-security/application-security-posture-management-aspm) application and cloud security teams aspire to have, one operating model that connects code, cloud, and risk.

# A new addition to our unified policy engine

Wiz SAST extends our policy engine with code-level vulnerability detection, without introducing another tool to manage.

![](<Base64-Image-Removed>)![](https://www.datocms-assets.com/75231/1764679288-sast-2-policies.png?fm=webp)

Wiz built-in Code & CI/CD policies–including the new SAST policy.

Wiz SAST inherits the full Wiz operating model. Setup remains easy through one-click onboarding with all your VCS platforms. Scans are all orchestrated from a unified policy engine, making enforcement predictable and exceptions consistent across risk domains. And because all findings flow into the Wiz portal, AppSec teams gain a unified view of code and cloud issues in one place, without managing another standalone tool.

# Prioritize SAST findings, with cloud context

Wiz SAST is fully powered by the Wiz Security Graph, allowing every finding to be understood in the broader context of workload behavior: where the code runs, whether it is exposed, what privileges it has, etc.

![](<Base64-Image-Removed>)![](https://www.datocms-assets.com/75231/1764700148-screenshot-2025-12-02-at-19-27-12.png?fm=webp)

Code repository with improper input validation vulnerability builds a container that is publicly exposed.

By correlating static findings with runtime exposure, excessive permissions, reachable sensitive data, and network paths, Wiz automatically elevates the few vulnerabilities that represent meaningful risk, like:

- _A Path Traversal flaw in code that builds a workload with sensitive hostPath mappings_

- _A Code Injection vulnerability that lands in a privileged container_

- _An SQL injection weakness in a workload that’s directly exposed to the internet_


Wiz also groups related weaknesses into CWE families so AppSec teams can address the entire root cause rather than individual occurrences.

> We approached security as an engineering challenge; we needed a ‘Lean security’ process transformation, not just another siloed tool. Traditional SAST delivered noise, but the shift to Wiz SAST, leveraging the Security Graph’s cloud context, allows us to prioritize only the real, exploitable issues instead of thousands of findings.
>
> Simon Goldsmith, CISO at OVO

And for organizations using other scanners, Wiz ingests findings from tools like Checkmarx, Semgrep, Snyk Code, and others, enriching them with the same cloud context to deliver a unified view of risk.

# Fix faster with clear ownership and guided remediation

Detecting risks is only half the job. Fixing them is what improves application security posture. Each Wiz SAST finding is tied directly to the relevant repository, code owner, and source location, giving teams immediate clarity on who should take action.

To help AppSec teams make decisions quickly, an AI-powered SAST agent provides additional context beyond the vulnerable snippet and CWE classification. It assists with triage by explaining why a finding is exploitable or by marking it as a likely false positive. This reduces the effort needed to understand and triage complex findings.

![](<Base64-Image-Removed>)![](https://www.datocms-assets.com/75231/1764680059-sast-5-ai-verdict.png?fm=webp)

SAST AI Agent for triaging and explaining findings in code.

After establishing the verdict, the AI agent also suggests a recommended fix for AppSec teams to determine the appropriate remediation path.

![](<Base64-Image-Removed>)![](https://www.datocms-assets.com/75231/1764680204-sast-5-ai-remediation-portal.png?fm=webp)

AI-assisted remediation guidance provided inside the Wiz portal.

Remediation also meets developers where they work. Within pull requests, developers also get the findings and can comment **"#wiz remediate"** to request an AI-assisted fix, fully grounded in the codebase context and following secure coding practices.

![](<Base64-Image-Removed>)![](https://www.datocms-assets.com/75231/1764679743-sast-6-remediation-pr.png?fm=webp)

Conversational experience in a GitHub PR with Wiz SAST AI agent.

This is [SAST](https://www.wiz.io/academy/application-security/static-application-security-testing-sast) designed for action, not just detection.

> Our goal was simple: to give developers the right tools, not more tickets. With the Wiz Code ASPM platform and the SAST engine, developers now get actionable guidance, including the vulnerable code snippet, full runtime context, and AI remediation options. Ultimately, this integrated workflow drives faster, better remediation across our continuous, horizontal security model.
>
> Simon Goldsmith, CISO at OVO

# Looking ahead: what cloud-aware SAST unlocks

By combining code analysis with runtime and cloud context, Wiz SAST sets the foundation for capabilities such as exposure-aware prioritization across all risk types, source-to-runtime API mapping, and correlation of SAST, [SCA](https://www.wiz.io/academy/sast-vs-sca-what-s-the-difference), secrets, IaC, pentest, and DAST findings into a single attack path.

With every layer of application risk connected, AppSec becomes proactive rather than reactive.

## Try it now in (Public Preview)

Wiz SAST is now available to all Wiz Code customers. The Public Preview includes repository and pull request scanning, thousands of curated rules, AI-assisted remediation, and full Security Graph enrichment.

If you already use Wiz Code, SAST can be enabled immediately. Read the [documentation (login required)](https://docs.wiz.io/docs/sast-solutions) to get started. By tying vulnerabilities to the environments where code actually runs, Wiz helps teams focus on exploitable issues, resolve them faster, and operate a unified AppSec program across code and cloud.

## Continue reading

[![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)](https://www.wiz.io/blog/1-billion-aws-marketplace-lifetime-sales)

[**Wiz Becomes Fastest Security ISV to Reach $1 Billion in AWS Marketplace Lifetime Sales**](https://www.wiz.io/blog/1-billion-aws-marketplace-lifetime-sales)

[![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)](https://www.wiz.io/authors/steve-vaughan)[![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)](https://www.wiz.io/authors/noa-yaar)

[Steve Vaughan](https://www.wiz.io/authors/steve-vaughan), [Noa Yaar](https://www.wiz.io/authors/noa-yaar)

December 2, 2025

A milestone fueled by customer trust and a partnership built for scale.

[![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)](https://www.wiz.io/blog/wiz-exposure-management-now-generally-available)

[**It's Here! Wiz Exposure Management is Now GA**](https://www.wiz.io/blog/wiz-exposure-management-now-generally-available)

[![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)](https://www.wiz.io/authors/eyal-golombek)[![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)](https://www.wiz.io/authors/alon-weiss)[![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)](https://www.wiz.io/authors/shaked-rotlevi)

[Eyal Golombek](https://www.wiz.io/authors/eyal-golombek), [Alon Weiss](https://www.wiz.io/authors/alon-weiss), [Shaked Rotlevi](https://www.wiz.io/authors/shaked-rotlevi)

December 2, 2025

Moving beyond CVE counts to true exposure management everywhere with new UVM and ASM capabilities, now GA

[![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)](https://www.wiz.io/blog/shai-hulud-2-0-aftermath-ongoing-supply-chain-attack)

[**Shai-Hulud 2.0 Aftermath: Trends, Victimology and Impact**](https://www.wiz.io/blog/shai-hulud-2-0-aftermath-ongoing-supply-chain-attack)

[![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)](https://www.wiz.io/authors/shay-berkovich)[![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)](https://www.wiz.io/authors/rami-mccarthy)

[Shay Berkovich](https://www.wiz.io/authors/shay-berkovich), [Rami McCarthy](https://www.wiz.io/authors/rami-mccarthy)

December 1, 2025

A deeper look at the Shai-Hulud 2.0 supply chain attack: reviewing the infection spread, victimology, leaked secrets distribution, and community response so far.

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

![](https://www.datocms-assets.com/75231/1764677251-screenshot-2025-12-02-at-13-06-52.png?fm=webp)

![](https://www.datocms-assets.com/75231/1764679288-sast-2-policies.png?fm=webp)

![](https://www.datocms-assets.com/75231/1764700148-screenshot-2025-12-02-at-19-27-12.png?fm=webp)

![](https://www.datocms-assets.com/75231/1764680059-sast-5-ai-verdict.png?dpr=0.75&fm=webp)

![](https://www.datocms-assets.com/75231/1764680204-sast-5-ai-remediation-portal.png?dpr=0.75&fm=webp)

![](https://www.datocms-assets.com/75231/1764679743-sast-6-remediation-pr.png?fm=webp)
[Wiz](https://www.wiz.io/)

- [Sign in](https://app.wiz.io/login)
- [Under attack?](https://www.wiz.io/experiencing-an-incident)

[Get a demo](https://www.wiz.io/demo?cta_source=blog&cta_page=/blog/is-wiz-a-runtime-security-tool&cta_placement=nav)

![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)![](https://www.datocms-assets.com/75231/1782269161-runtime-findings-copy-2x-100-1.jpg?fm=webp)

![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)![](https://www.datocms-assets.com/75231/1782269161-runtime-findings-copy-2x-100-1.jpg?fm=webp)

## From Cloud Posture to Real-Time Protection

It's a common question we hear from prospects:

_"Does Wiz actually do runtime, or is it just risk prevention?"_

The short answer is **yes, Wiz does runtime security.**

The longer answer is that the _or_ in that question is something I'd push back on. Prevention and runtime were never really alternatives, and the fact that the market learned to treat them as a choice explains a lot about how cloud security architecture ended up where it is. It also explains how we got here.

**Wiz started from a fairly specific bet:** that [cloud security](https://www.wiz.io/academy/cloud-security/what-is-cloud-security) had to begin with complete visibility, and that nobody would ever achieve complete visibility if the first step was deploying an agent on every workload. So we built agentless Cloud Connectors and mapped all resources and risks on the Wiz Security Graph, and gave teams a way to see the toxic combinations of risks across an entire cloud estate in minutes rather than quarters. That bet worked. It became the [CNAPP category](https://www.wiz.io/academy/cloud-security/what-is-a-cloud-native-application-protection-platform-cnapp), and it's still the thing most of the market associates with our name.

**Visibility was always meant to be the foundation, though, not the finished product.** As customers matured on the platform, the questions they brought us changed. Knowing what could go wrong is the right place to start, but it doesn't tell you what is going wrong right now, inside a container that is already running, while an attacker is already inside an environment.

So we built for that. The [**Wiz Runtime Sensor**](https://www.wiz.io/solutions/runtime-sensor) is a lightweight eBPF sensor that observes what is actually executing on your workloads: containers, Kubernetes, VMs, serverless, Windows, and AI infrastructure. [**Wiz Defend**](https://www.wiz.io/platform/wiz-defend) is the detection and response layer built on top of it. Together they detect and respond to live threats in real time, and the signals they produce also flow back into the Security Graph, so risk prioritization reflects what’s  running rather than what is theoretically installed.

Wiz Defend- Timeline from Wiz on Vimeo

![video thumbnail](https://i.vimeocdn.com/video/1956346341-b28099265301e5559502b8e9e005bc4576844e3411046f87ae8b574b9d30ebed-d?mw=80&q=85)

Playing in picture-in-picture

Like

Play

00:00

00:19

Settings

Speed

QualityAuto

2x

1.5x

1.25x

1x

0.75x

0.5x

Fullscreen

;

## Expanding the Platform: A Look at Our Recent Runtime Velocity

The clearest way to show you where the platform actually stands is to show you what we've shipped. Here's the last six months:

- [**Runtime signals in the Security Graph**](https://www.wiz.io/blog/runtime-signals-in-security-graph) (June 25, 2026). The Runtime Sensor now feeds live network telemetry directly into the Security Graph: active container-to-container connections, DNS queries to databases, and AI workloads reaching out to remote MCP servers. The impact is measurable. **For 1 in every 6 environments we monitor at runtime, adding runtime context surfaced a high or critical severity attack path that prior analysis had missed.**

- [**The Wiz Runtime Sensor for Windows**](https://www.wiz.io/blog/wiz-runtime-sensor-for-your-windows-environment) (June 22, 2026). Real-time threat detection across your Windows fleet, with a memory-safe architecture designed to scale without a meaningful performance cost.

- [**Wiz Forensics, now GA**](https://www.wiz.io/blog/wiz-sensor-forensics-ga) (May 27, 2026). When a detection fires, the Sensor automatically captures a forensics package at the moment of detection: the triggering script or binary, the process tree, shell histories, SSH configuration, the container drift layer, and system logs, collected before the workload has a chance to disappear. The Forensics AI Engine then analyzes it before an analyst has opened a single file. We've seen the same detection move from _Low Confidence, Inconclusive_ to _High Confidence Malicious_ with a reconstructed attack timeline, because the evidence was there to analyze.

- [**Runtime threat detection for Google Cloud Run**](https://www.wiz.io/blog/introducing-runtime-threat-detection-for-google-cloud-run) (May 19, 2026). Completes our serverless container coverage alongside [AWS Fargate and Azure Container Apps](https://www.wiz.io/blog/wiz-expands-runtime-protection-to-serverless-containers). The Sensor continuously monitors process execution, system calls, and runtime behavior inside your containers, surfacing a detection the moment it sees a binary that wasn't in the original image, a reverse shell being initiated, or a DNS query to a known malicious domain. It ships with **2,000+ built-in threat detection rules**, and teams can extend the library with their own.

- [**The Wiz Blue Agent, now GA**](https://www.wiz.io/blog/wiz-blue-agent-generally-available) for all Wiz Defend customers (March 30, 2026). Blue agent investigates threats end to end the way a trained incident responder would, using specialized sub-agents for forensics and code analysis. It correlates runtime activity back to source code, identifying related pull requests, code changes, and code owners, which lets it distinguish between an unusual but legitimate application action and a real attack. The investigation is transparent: analysts see the questions it asked, the data it retrieved, and how each signal shaped the verdict. Verdicts feed straight into [Wiz Workflows](https://www.wiz.io/blog/introducing-wiz-workflows) for escalation and containment.

- [**AI runtime threat detection, from input to real-world impact**](https://www.wiz.io/blog/ai-runtime-threat-detection-from-input-to-real-world-impact) (March 20, 2026). Detection across the full execution path of an AI application. More on this later, because it warrants its own section.


Underneath all of it, the Sensor's coverage keeps widening. The [Sensor Workload Scanner](https://www.wiz.io/blog/from-cloud-to-hybrid-360deg-runtime-protection-anywhere-you-run) extends runtime-aware scanning to VMs in private cloud environments like VMware and OpenStack, self-hosted Kubernetes clusters like OpenShift, and bare metal and edge workloads, validating vulnerabilities against what is actually loaded in memory rather than what is merely installed on disk.

### What this looks like with our customers

The pattern I see most often is a team that came to Wiz for agentless visibility, got comfortable, and then found the Sensor waiting for them when they needed it.

- [FullStory](https://www.wiz.io/customers/fullstory) is a good example. They were deliberately cautious about rolling out the Runtime Sensor and took a land-and-expand approach, assessing the impact before committing. They proved it didn't degrade performance, and the Sensor now runs across their managed GKE clusters. What sold them was seeing a vulnerability validated by the Sensor as loaded into memory, which enabled them to prioritize their risks with Runtime context. The runtime capabilities landed as an extension of the agentless product they already trusted, not a separate tool to learn.

- [Redis](https://www.wiz.io/customers/redis-unified-cloud-security) went further and consolidated. They deployed Sensors across every production GKE cluster to get one detection layer that behaves consistently regardless of which cloud or configuration sits underneath it. As Justin Lachesky, their Director of Cyber Resilience, put it: "We've shifted away from a multi-platform, multi-technology detection strategy to focusing on Wiz." They've since measured the Blue Agent against their analysts' final case dispositions across 431 cases since October 2025, and it's tracking at 85.7% overall accuracy with a false negative rate below 2%.

- [Hivebrite](https://www.wiz.io/customers/hivebrite) is the clearest argument for why these two capabilities belong together. Their legacy CNAPP kept runtime findings and CSPM findings disconnected, which left teams stitching them back into a coherent picture by hand while alerts piled up. Integrating runtime and posture findings became an explicit requirement in their search, and it's part of why they chose Wiz. As they extend the Sensor into their Kubernetes production environments, it tells them whether a library with a known CVE is actually loaded in memory, which means they can confidently deprioritize the ones that aren't.


Redis Achieves Unified Cloud Security at Scale with AI-Powered Threat Detection from Wiz on Vimeo

![video thumbnail](https://i.vimeocdn.com/video/2130128350-a696e550089704d46c7426dac6e26c0e36e059351761c15982e3cb334f86165c-d?mw=80&q=85)

Playing in picture-in-picture

Like

Play

00:00

03:22

CC/subtitles

Settings

Speed

Transcript

QualityAuto

CC/subtitlesOff

2x

1.5x

1.25x

1x

0.75x

0.5x

Fullscreen

;

## **The Architecture: Context and Response, Running in Parallel**

The reason the answer isn't simply "yes, we have an agent too" comes down to architecture.

Wiz runs **two engines at the same time**, and each one makes the other more accurate.

**The Cloud-Native Security Graph** maps systemic risk. It's agentless, it covers the full environment, and it understands relationships: this container has this vulnerability, runs with this identity, which has a path to this storage bucket, which holds sensitive training data. It gives you the map, and the toxic combinations inside it.

**The Runtime Sensor** works at the kernel level, inside the workload, at Runtime. It sees the process that just spawned, the syscall that just fired, the connection that just opened. It detects live container exploits, unauthorized code execution, and active threats as they happen.

These run **simultaneously and in parallel**, and each answers a question the other cannot.

The best way to see why that matters is to take the hardest case we have.

### **Securing AI at runtime**

When people talk about [AI runtime security](https://www.wiz.io/academy/ai-security/ai-runtime-security), they usually mean guardrails on prompts. Guardrails are useful and they are also fundamentally limited, because a model cannot reliably separate system instructions from user input, an attacker can iterate on a prompt until one gets through, and a model has no ability to inspect the external actions it triggers. Tell an agent to download and execute a script and it has no idea whether that script opens a reverse shell or drains a database. It just runs it.

So the useful question isn't "can we block every bad input." It's **"can we detect when an agent's behavior turns malicious, even when the prompt looked normal?"** Answering that takes both engines: runtime observation of what the agent actually did, and architectural context explaining what it means.

We detect across three layers:

- **Model.** Inputs, outputs, and prompt behavior. Suspicious inputs and prompt injection attempts that lead to execution.

- **Workload.** How the agent executes and what it actually does. Tool invocation, process spawning, credential access, outbound communication.

- **Cloud.** How identities, APIs, and infrastructure get used. Which role the agent assumed, what data it reached, where it sent it.


Then we apply **AI context** across all of it. Using context tags, Wiz identifies AI workloads and agentic systems, identities operating as agents, processes interacting with AI services, and data tied to AI applications. That changes how a signal reads. Without context, the Sensor reports that a process accessed credentials, which happens constantly and usually means nothing. With context, the same event reads as **an AI agent attempting to retrieve credentials**. The underlying telemetry hasn't changed. The graph is what makes it legible.

![](<Base64-Image-Removed>)![](https://www.datocms-assets.com/75231/1774038460-screenshot-2026-03-20-at-4-08-43-pm.png?fm=webp)

Here's what that looks like on a real detection. An attacker targets a publicly exposed AI agent and crafts a prompt telling it to download and run a script. The interaction appears ordinary. But the agent executes system\_report.sh, which launches a Python reverse shell as root and starts pulling data out of an RDS database. The Sensor captures a forensics package at the moment of detection. The Forensics AI Engine analyzes the script and correlates it with runtime evidence. The Blue Agent reconstructs the sequence: a multi-stage attack chain running from initial prompt injection to data exfiltration, classified High Confidence Malicious before an analyst had manually reviewed anything.

Neither engine could have done that alone. The Sensor saw the execution but couldn't have known the workload was an AI agent, which identity it held, or which database sat at the end of the path. The graph knew all of that and would never have seen the shell.

### **The connection nobody can see**

The same architecture closes a blind spot almost every security team currently has.

Take an internet-facing AI chatbot. Agentless scanning tells you the container has known vulnerabilities and that the underlying agent can reach a knowledge base containing sensitive data. Worth addressing on its own.

What agentless scanning cannot tell you is that right now, that same agent is actively connecting to a remote MCP server outside your environment. That connection isn't defined in a config file. It isn't in any policy. It exists only because code is executing.

Which containers are talking to external MCP servers? Are those servers trusted? Do those containers also reach sensitive data? For most teams these questions have no answer today. The Sensor observes those DNS queries as they happen and surfaces them in the Security Graph, so they do.

Layer that runtime signal onto the graph and three separate findings resolve into one: **a live attack path to data exfiltration through an AI system nobody knew was reaching outside the organization.** ( [This is what we shipped in June](https://www.wiz.io/blog/runtime-signals-in-security-graph).)

![](<Base64-Image-Removed>)![](https://www.datocms-assets.com/75231/1782269594-secgraphruntimefind.png?fm=webp)

The Security Graph correlating an internet-facing container with vulnerabilities and a confirmed network connection to an S3 bucket with PII data.

## **Why Complete Cloud Security Requires Both Agentless and Runtime Capabilities**

What the AI example shows at the level of one detection is true at the level of an entire security architecture. For most of the last decade, buyers were forced to choose between agentless visibility from one vendor and a standalone runtime agent from another. This created two consoles, two data models, and two sets of findings that never lined up. The industry gradually mistook a vendor tooling limitation for a real architectural boundary, separating prevention and detection simply because the products were separate.

You can see the operational cost most clearly in what each side gets wrong when deployed in isolation:

- **Agentless scanning alone** returns thousands of vulnerabilities with no way to verify which ones are actually loaded into memory on an internet facing workload. Teams are left patching by arbitrary CVSS scores and hoping for the best.

- **A runtime agent alone** fires an alert with no context to explain what the workload does, which identity it holds, or what sits downstream of it. Every alert forces an analyst into an hour of manual reconstruction just to decide if it’s a true positive.


One tool produces work that cannot be prioritized, while the other produces alerts that cannot be interpreted.

Unifying both capabilities on a single graph fundamentally changes the math. Prioritization narrows immediately to what is genuinely exploitable because the sensor validates vulnerabilities in runtime. Detections arrive already carrying the full context of the cloud identity, the exposure path, and the data at risk.

Stitching together fragmented, multi-vendor tools is what produces disjointed context, duplicate alerts, and the alert fatigue that wears security analysts down. When prevention and detection live in different systems, nobody owns the handoff between them, creating a dangerous gap where multi-stage attacks hide. Moving to one platform, one graph, and one policy engine from code to production is not a packaging preference. It is exactly what the problem requires.

## **A Modern Approach to Cloud and AI Defense**

So, to close the loop on the question we started with: **is Wiz a runtime security tool?**

Yes. Wiz is a unified cloud-native application protection platform that secures organizations from code to production across every cloud, with agentless visibility and real-time runtime detection and response operating together, natively, on the same graph. That covers microservices, containers, Kubernetes, VMs, serverless, Windows, hybrid and on-prem workloads, and live AI applications.

[![](<Base64-Image-Removed>)![](https://www.datocms-assets.com/75231/1784831223-wiz-defend-guided-tour-homepage.png?fm=webp)](https://www.wiz.io/guided-tour?tour=defend&cta_source=blog&cta_page=/blog/is-wiz-a-runtime-security-tool&cta_placement=in-content)

Tags

[#Product](https://www.wiz.io/blog/tag/product) [#Wiz Defend](https://www.wiz.io/blog/tag/wiz-defend)

## Continue reading

[![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)![](https://www.datocms-assets.com/75231/1782965547-workflows-copy-2x.png?fm=webp)](https://www.wiz.io/blog/introducing-wiz-mcp)

[**Build AI Security Agents with Wiz MCP**](https://www.wiz.io/blog/introducing-wiz-mcp)

[![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)![](https://www.datocms-assets.com/75231/1741726923-img_7561.jpeg?fm=webp)](https://www.wiz.io/authors/snegha)[![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)![](https://www.datocms-assets.com/75231/1766281848-image-19.png?fm=webp)](https://www.wiz.io/authors/shani-gafni)[![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)![](https://www.datocms-assets.com/75231/1745250539-e04lwss17ft-u07jmex9mt7-950da3f6bd7d-512.png?fm=webp)](https://www.wiz.io/authors/hen-perez)

[Snegha Ramnarayanan](https://www.wiz.io/authors/snegha), [Shani Gafni](https://www.wiz.io/authors/shani-gafni), [Hen Perez](https://www.wiz.io/authors/hen-perez)

July 2, 2026

Power AI-driven security with trusted security context, Wiz AI Agents, and Wiz AI Skills.

[![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)![](https://www.datocms-assets.com/75231/1782933699-pqc-copy-2x.png?fm=webp)](https://www.wiz.io/blog/white-house-post-quantum-cryptography-executive-order)

[**Breaking Down the White House’s Actions on Post-Quantum Cryptography Readiness**](https://www.wiz.io/blog/white-house-post-quantum-cryptography-executive-order)

[![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)![](https://www.datocms-assets.com/75231/1711130315-mitch.jpeg?fm=webp)](https://www.wiz.io/authors/mitch-herckis)

[Mitch Herckis](https://www.wiz.io/authors/mitch-herckis)

July 2, 2026

The U.S. Federal Migration to PQC Just Got Real

[![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)![](https://www.datocms-assets.com/75231/1782829436-opportunities-2x.png?fm=webp)](https://www.wiz.io/blog/ai-threat-readiness-with-wizos)

[**Start Secure in the AI Era: Accelerating AI Threat Readiness with WizOS**](https://www.wiz.io/blog/ai-threat-readiness-with-wizos)

[![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)![](https://www.datocms-assets.com/75231/1760137614-allison-jackson.jpeg?fm=webp)](https://www.wiz.io/authors/allison-jackson)[![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)![](https://www.datocms-assets.com/75231/1776855492-velikanski_daniel_662-a-0071.jpg?fm=webp)](https://www.wiz.io/authors/daniel-velikanski)[![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)![](https://www.datocms-assets.com/75231/1782830614-roee.jpeg?fm=webp)](https://www.wiz.io/authors/roee-kanari)[![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)![](https://www.datocms-assets.com/75231/1710776164-ofir-profile-pic.jpeg?fm=webp)](https://www.wiz.io/authors/ofir-cohen)

[Allison Jackson](https://www.wiz.io/authors/allison-jackson), [Daniel Velikanski](https://www.wiz.io/authors/daniel-velikanski), [Roee Kanari](https://www.wiz.io/authors/roee-kanari), [Ofir Cohen](https://www.wiz.io/authors/ofir-cohen)

June 30, 2026

As the time from vulnerability discovery to exploitation shrinks, building with minimal, secured components is more important than ever. Here is how WizOS helps.

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

![](https://www.datocms-assets.com/75231/1774038460-screenshot-2026-03-20-at-4-08-43-pm.png?fm=webp)

![](https://www.datocms-assets.com/75231/1782269594-secgraphruntimefind.png?fm=webp)
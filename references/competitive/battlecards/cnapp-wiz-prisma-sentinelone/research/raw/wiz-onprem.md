[Wiz](https://www.wiz.io/)

- [Sign in](https://app.wiz.io/login)
- [Under attack?](https://www.wiz.io/experiencing-an-incident)

[Get a demo](https://www.wiz.io/demo?cta_source=blog&cta_page=/blog/sensor-wls-for-on-prem&cta_placement=nav)

![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)

Over the last two decades, the enterprise landscape has undergone a massive transformation. Established organizations migrated to the cloud to capture efficiency gains, while a new generation of cloud-native companies started there to avoid heavy upfront infrastructure costs. Yet for many organizations, the result is hybrid cloud, and that reality is not changing anytime soon. Compliance requirements, data sovereignty, low-latency edge computing, and the rising cost of running AI workloads all mean that critical infrastructure and sensitive data often need to stay on-premise.

For security teams, this hybrid footprint often creates a tale of two environments. Cloud Security teams have been able to leverage the high-context and the graph-based clarity of Wiz to prioritize their work. Meanwhile, on-premise security teams often manage entirely different stacks and have lacked those same modern, cloud-native capabilities. They are frequently left relying on fragmented legacy tools that treat every single vulnerability like a critical emergency.

Today, with the GA of our Sensor Workload Scanner, Wiz is bringing the same risk visibility we provide for teams in the cloud to security teams anywhere. Whether a workload runs in the cloud or on on-premise VMware, bare metal, or a self-hosted Kubernetes cluster, you now have one source of truth and a unified risk strategy. And as teams increasingly run AI models and agents on-premise, that coverage extends to your AI workloads too - providing visibility into the AI technologies running in your environment and detecting AI-specific threats like suspicious prompt activity the moment they emerge.

# **The Challenge: Moving from siloed risk visibility to unified context**

Securing on-premise environments has traditionally focused on scanning and securing individual risk domains. Teams have become experts at managing high volume security signals from various sources such as a vulnerability scanner for the host, a configuration scanner for the hypervisor, and identity logs for the network. The challenge has not been a lack of data. Instead, it has been the difficulty of correlating across the signals to know what to prioritize and fix.

When security findings are managed in siloes, it is difficult to determine which risks are truly reachable and exploitable. A vulnerability on an internal server might seem critical on paper, but without knowing its network exposure, host misconfigurations, or paths to sensitive data in your environment, it is nearly impossible to prioritize remediation effectively.

Another gap exists where these cloud and on-premise environments overlap. Attackers often look for the quiet connections, the hybrid gap, where a local configuration or access to secrets/keys might provide an unintended bridge to cloud-based assets. Moving beyond looking at risk domains in siloes allows both on-premise and overall security teams to stop treating every finding as an isolated event. By correlating these signals, teams gain the visibility needed to focus and prioritize the risks that create real attack paths to their crown jewels across the hybrid cloud.

![](<Base64-Image-Removed>)![](https://www.datocms-assets.com/75231/1782680846-secgraphlateralmovement.png?fm=webp)

Figure 1: An AWS Access Key discovered on an on-prem vSphere VM - combined with public exposure and sensitive data, creates a direct lateral movement path to a Cloud IAM User and Role with Admin privileges.

### **The Path Forward: A Unified Strategy for the Hybrid Cloud**

The GA of the Sensor Workload Scanner marks a significant milestone - Wiz now delivers native workload scanning for on-premise environments. But the scanner is one piece of a larger story. Wiz for On-premise is a comprehensive security operating model for hybrid teams, bringing together the core pillars that give you a single, prioritized view of risk across your entire hybrid environment.

- **Agentless Infrastructure Context via Connectors:** True visibility starts at the foundation without the friction of deploying agents. Our native vSphere and Kubernetes Connectors assess your infrastructure through native APIs to provide an immediate, comprehensive view of your on-premise assets. This goes deeper than a simple scan by identifying ESXi vulnerabilities, local identities, and cluster misconfigurations. These relationships are then mapped directly into the Security Graph to show how your infrastructure and workloads interact.

- **Prioritizing Risk with the** [**Sensor-based Workload Scanner**](https://www.wiz.io/blog/from-cloud-to-hybrid-360deg-runtime-protection-anywhere-you-run) **:** For deep visibility into the workloads themselves, the Sensor-based Workload Scanner (WLS) identifies public exposure, vulnerabilities, misconfigurations, malware, secrets, sensitive data and more. By correlating these risk findings with the infrastructure context in the Security Graph, Wiz can automatically surface the toxic combinations and attack paths that put your business at risk. This enables on-premise teams to stop chasing isolated CVEs and focus on the risks that actually matter.

  - Runtime Validation takes this a step further - by confirming whether a vulnerable package is actually loaded into memory and running, teams can instantly separate a theoretical risk from one that is live and exploitable right now.

  - While the sensor provides native high fidelity risk signals, customers can also ingest findings from their existing on-premise scanners into Wiz using [Unified Vulnerability Management (UVM)](https://www.wiz.io/blog/introducing-wiz-for-exposure-management) to centralize their risk strategy.

![](<Base64-Image-Removed>)![](https://www.datocms-assets.com/75231/1782681122-secgraphwvalidatedinruntime.png?fm=webp)

Figure 2: An on-prem attack path created by a publicly exposed application endpoint that leads to a VM with sensitive data which hosts a container with a vulnerability that is validated in runtime by the Wiz Runtime Sensor.

- **Integrated** [**Attack Surface Management**](https://www.wiz.io/blog/introducing-wiz-asm) **:** Understanding internal risk is only half the battle. By combining our external outside-in scanning with internal context, Wiz identifies which on-premise servers are actually exposed to the public internet. This allows teams to validate the true exploitability of a server in real-time, ensuring that external threats are prioritized alongside internal risks. To go even further, the [Wiz Red Agent](https://www.wiz.io/blog/introducing-the-wiz-red-agent) can automatically simulate how an attacker would actually move through your environment - testing whether an exposed server is not just reachable, but truly exploitable, so your team can focus remediation efforts on the risks that represent a real path to your most critical assets, not just theoretical ones.

- [**Runtime Threat Detection**](https://www.wiz.io/solutions/runtime-sensor): The same Runtime Sensor that provides workload visibility also enables real-time detection of threats happening in your environment. By continuously monitoring behavior across your on-premise workloads, Wiz surfaces critical threats the moment they happen. When a threat is detected, Wiz automatically correlates related detections to cut through the noise and deliver high-fidelity alerts - providing [forensics collection](https://www.wiz.io/blog/wiz-sensor-forensics-ga) and an AI-powered initial investigation with the [Blue Agent](https://www.wiz.io/blog/wiz-blue-agent-generally-available) so your team isn't starting from scratch. From there, remediation playbooks can be triggered automatically using [Wiz Workflows](https://www.wiz.io/blog/introducing-wiz-workflows), turning a detected threat into a resolved one without manual intervention.


### **One Security Platform for Hybrid Environments**

Security should not be defined by where a workload lives. By extending the Wiz engine to your on-premise environments, we are giving your teams a single language for risk, a single pane of glass for visibility, and a single strategy for remediation.

The on-premise environment is no longer a silo. It is part of the Wiz Security Graph. Ready to see how it works? Join us on our [upcoming webinar in July](https://www.wiz.io/events/wiz-demo-unified-risk-and-threat-coverage-for-hybrid-environments) to see the Workload Scanner in action and you can learn more about [Wiz Sensor-Based Workload Scanning](https://docs.wiz.io/docs/sensor-based-workload-scanner)(login required) and start protecting your hybrid environments today.

Tags

[#Sensor](https://www.wiz.io/blog/tag/sensor) [#Wiz Defend](https://www.wiz.io/blog/tag/wiz-defend) [#Product & Company News](https://www.wiz.io/blog/tag/news)

## Continue reading

[![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)](https://www.wiz.io/blog/wiz-xm-securing-public-sector-hybrid-environments)

[**The Borderless Attack Surface: Securing Public Sector Hybrid Environments**](https://www.wiz.io/blog/wiz-xm-securing-public-sector-hybrid-environments)

[![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)](https://www.wiz.io/authors/annam-iyer)[![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)](https://www.wiz.io/authors/shaked-rotlevi)[![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)](https://www.wiz.io/authors/bryan-rosensteel)

[Annam Iyer](https://www.wiz.io/authors/annam-iyer), [Shaked Rotlevi](https://www.wiz.io/authors/shaked-rotlevi), [Bryan Rosensteel](https://www.wiz.io/authors/bryan-rosensteel)

June 29, 2026

Aligning Modern CNAPP Telemetry with realistic risk assessments to drive agency efficiency through cross-team collaboration

[![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)](https://www.wiz.io/blog/red-agent-pov-bola)

[**The Red Agent POV: Exploiting Broken Object-Level Authorization in an Airline GraphQL API**](https://www.wiz.io/blog/red-agent-pov-bola)

[![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)](https://www.wiz.io/authors/red-agent)[![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)](https://www.wiz.io/authors/gal-nagli)

[Red Agent](https://www.wiz.io/authors/red-agent), [Gal Nagli](https://www.wiz.io/authors/gal-nagli)

June 29, 2026

Part 2: How the Red Agent bypassed backend resolvers to expose an entire airline booking database in fifteen minutes

[![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)](https://www.wiz.io/blog/amazon-q-vulnerability)

[**MCP Auto-Execution: From Git Clone to Cloud Compromise in Amazon Q VS Code Extension**](https://www.wiz.io/blog/amazon-q-vulnerability)

[![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)](https://www.wiz.io/authors/maor-dokhanian)

[Maor Dokhanian](https://www.wiz.io/authors/maor-dokhanian)

June 26, 2026

By automatically loading MCP servers from workspace files, Amazon Q enabled attackers to execute code and access sensitive cloud environments.

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

![](https://www.datocms-assets.com/75231/1782680846-secgraphlateralmovement.png?fm=webp)

![](https://www.datocms-assets.com/75231/1782681122-secgraphwvalidatedinruntime.png?fm=webp)
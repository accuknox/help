# CNAPP Micro Deck, AUG 2026: Speaker Notes

Three to four talking points per slide, in slide order. Each one is a plain fact about the product, the problem, or a customer. Say them in your own words.

---

## Slide 1: Zero Trust CNAPP

- AccuKnox is a CNAPP. It covers cloud posture, workloads, Kubernetes, code, APIs and AI on one platform.
- Most CNAPPs detect and report. We block the process, because the syscall is denied in the kernel before it finishes.
- A blocked syscall leaves nothing to investigate. A detection tool alerts you after the file was already written.
- That difference is testable, so we encourage customers to test it during the POC.

## Slide 2: Outline

- We solve four problems. Cloud misconfiguration, workloads with no runtime protection, APIs nobody owns, and AI assets nobody has counted.
- Compliance teams care about the 37 frameworks and the audit evidence behind them.
- Platform teams care about kernel enforcement and how policies get written without hand-authored YAML.

## Slide 3: About AccuKnox

- We started in 2020 with Stanford Research Institute. Five patents and the runtime engine came from that work.
- KubeArmor is our open source runtime engine. It is a CNCF project with over 20 million downloads.
- We raised $15M from SRI and National Grid Partners. Both are strategic investors.
- Our production customers include financial services, federal government, healthcare and telecom.

## Slide 4: Leadership

- Nat runs the customer side. Rahul owns product and engineering. Phil built the research work at SRI.
- The team is 120 people. Most leaders came from Cisco, McAfee, Symantec and SRI.
- Golan Ben Oni and David Billeter advise us. Both have run security at large enterprises.

## Slide 5: Twelve modules, code to cognition

- Twelve modules run on one policy engine and one console.
- A customer turns on what they need now and adds the rest later without a new contract.
- CSPM, CWPP and KSPM together answer most cloud security RFPs.
- CTEM and CIEM are in customer pilots today, so they carry a Beta label.

## Slide 6: AI attacks on the rise

- These are six real incidents between 2024 and 2026, each one with its reported cleanup cost.
- The pattern repeats. A prompt gets injected, a config gets exposed, a supply chain gets poisoned, an agent acts on its own.
- The Mercor breach lost 4TB of data. Meta froze a $10B contract and 40,000 people joined a class action.
- Air Canada paid only $812 in damages. It still lost a tribunal ruling and had to shut the chatbot down.

## Slide 7: Zero Trust Agentic Security

- Securing AI agents is mostly securing the machines they run on. An agent still runs processes, opens files and makes network calls.
- The AI controls are red teaming, prompt firewall, guardrails, and model and dataset integrity.
- The infrastructure controls are the CNAPP work already in the budget, which is cloud, API, application and SBOM.
- A tool that only covers the AI layer leaves the cluster underneath unprotected.

## Slide 8

-

## Slide 9: Modernize, reduce costs

- The average enterprise we work with runs more than 45 security tools.
- Every tool is a renewal, an integration and an admin overhead.
- Customers who consolidated onto AccuKnox cut tooling spend by 40 to 60 percent.
- The savings are real because all our modules share one engine instead of being separate products.

## Slide 10: Zero Trust AI Security architecture

- The same controls apply to every AI asset. It does not matter if the model runs in AWS, in a datacenter, or air-gapped.
- Security controls sit between the AI assets and the environment. Moving a model does not change how it is protected.
- Most AI security tools are SaaS only. They cannot cover a model that runs inside a regulated network.

## Slide 11: AI Security use cases

- The bottom two layers are cloud misconfiguration, runtime vulnerabilities and malware. These are known problems.
- Model risk is adversarial input. We answer it with the prompt firewall, dataset scanning for PII and PHI, and automated red teaming.
- Agent risk is the newest layer. We give agent visibility across clouds, real time auditing, and sandboxing for unsafe tool use.
- AI-DR ties it together with AI-aware policy checks, misuse detection and automated remediation.

## Slide 12: Agentic AI Security platform

- Teams that build models need artifact scanning, provenance checks, red teaming and a security score before shipping.
- Enterprises running agents need discovery first, then a gateway with prompt firewalling, then runtime guardrails.
- The browser plugin covers ChatGPT, Gemini, Claude and Copilot. That is how shadow AI becomes visible.
- Almost no enterprise can name every agent running in production today.

## Slide 13: Deployment models

- We run four ways. AccuKnox SaaS, the customer's own cloud, on-prem including bare metal, and fully air-gapped.
- SaaS gives first findings the same day a customer onboards.
- The air-gapped build sends no telemetry and never calls home. That is what GDPR, DPDP and ITAR require.
- Financial services and healthcare customers mostly run private cloud or on-prem. We have references in both.

## Slide 14: Integrations

- We have more than 50 integrations. Slack, Jira, ServiceNow, Splunk and Datadog work on day one.
- CI/CD hooks for GitHub Actions, GitLab and Jenkins put findings in the developer workflow.
- Findings flow both ways, so a SIEM gets context instead of another raw event feed.
- API connectors cover anything not on the list, including custom internal tools.

## Slide 15: Runtime security journey

- Day one is a golden baseline. We profile every container in every namespace.
- Hardening policies map to CIS, MITRE, NIST and STIGs. They run in audit mode for two to three weeks.
- The customer's team accepts or discards each change, so the baseline matches their environment.
- Enforcement starts only when behavior is stable. After that, approved behavior runs and unknown code is denied.

## Slide 16: SBOMs supported

- We produce eight bill-of-materials types. AIBOM covers models, CBOM covers cryptography, QBOM covers quantum readiness.
- Output is CycloneDX and SPDX. It goes straight to a customer or a regulator.
- Crypto agility rules are already showing up in financial services contracts. CBOM answers them.

## Slide 17: Differentiators

- SOC teams report about 80 percent fewer alerts after moving to us.
- The reason is runtime context. We show which CVE is loaded in memory, not just present on disk.
- Each deployment replaces three to five existing tools.
- We wrote the platform cloud-native in 2020. There is no old scanner underneath being patched.

## Slide 18: AI red teaming

- We attack the customer's model. Jailbreaks, prompt injection, data extraction, code injection and hallucination checks.
- It runs on a schedule. The customer gets a trend line instead of one pentest report a year.
- Results map to the OWASP LLM Top 10. That is the framework auditors ask about.
- Testing happens before launch. A jailbreak found by a customer becomes a public disclosure.

## Slide 19: Runtime at every layer

- At the kernel we cover files, processes and network. eBPF gives telemetry and LSMs do the blocking.
- At the data layer we cover secrets, PII access and egress control.
- At the API layer we enforce authentication, rate limits and schema drift at runtime.
- At the app layer we inspect prompts, responses and HTTPS traffic. Policies come from observed behavior, so nobody writes them by hand.

## Slide 20: DevSecOps and ASPM

- SAST reads source code before the app runs. DAST attacks the running app from outside. IAST sits inside the app and triggers on traffic.
- SCA tracks third-party dependency risk. IaC scanning uses KICS, Tfsec and Checkov on Terraform, Helm and Kubernetes files.
- All five are included. A customer does not license five separate products for this.
- Pipeline findings and runtime enforcement land in the same console.

## Slide 21: AI security, dev to deployment

- Models and datasets get scanned in the pipeline, the same way code does.
- After deployment the same asset stays monitored. A model that passed a scan in March is still watched in September.
- Most AI security programs break at that handoff, because two different tools own the two halves.
- In most enterprises no single team owns model security today.

## Slide 22: AI inventory

- We discover models, endpoints, MLOps pipelines, agent toolchains, datasets, compute and MCP servers across every cloud.
- Shadow AI shows up whether or not anyone filed a ticket.
- The first scan almost always finds more AI assets than the security team expected.
- Governance, red teaming and runtime protection all need this inventory first.

## Slide 23: API security problems

- Shadow, zombie and orphan APIs have no owner, no docs and no patch schedule.
- We cover north-south and east-west traffic, so internal exposure between services is visible too.
- We flag PII and PHI in headers and map it to DORA, GDPR, HIPAA, PCI-DSS and OWASP.
- Rate limiting and schema checks run at the kernel level, not in the application code.

## Slide 24: Five reasons

- We prevent attacks instead of generating alerts about them.
- Every company runs on APIs now, and most cannot list the ones in production.
- The EU AI Act, NIST AI RMF and OWASP LLM Top 10 are already in audit scope. AI security has a deadline.
- Zero trust applies to the workload, the API and the model, not just the perimeter.

## Slide 25: Two meanings of runtime security

- Most vendors use runtime as a lens. eBPF telemetry improves posture data and CVE ranking, but the alert fires after the action ran.
- We use runtime as a shield. eBPF plus LSMs enforce policy in the kernel and deny the syscall before it completes.
- In practice that means unauthorized fork, execve, file access and network calls get blocked, not logged.
- Ask every vendor on the shortlist one question. Does your runtime see the attack, or stop it?

## Slide 26: Tools out of the box

- SAST, DAST, SCA, IaC scanning, container security, host security and compliance all run inside the platform.
- This is where Snyk, Checkmarx and Veracode spend usually sits today.
- IaC scanning covers Terraform, Helm and Kubernetes manifests with KICS, Tfsec and Checkov built in.
- DAST sends automated malicious HTTP requests at APIs and web UIs on a schedule.

## Slide 27: Stack ranking

- This compares us row by row against the vendors on the same shortlist.
- The rows that decide most evaluations are kernel enforcement, on-prem coverage and air-gapped support.
- We state the rows where a competitor is stronger. One overstated claim makes a team re-check every other claim.

## Slide 28: Platformization, part one

- Modules one through six cover AI, API, cloud posture, workload, Kubernetes and application security.
- Each module ships four or five capabilities in production. None of these are roadmap items.
- KSPM plus KIEM puts Kubernetes misconfiguration and identity risk in one view. That is normally two tools.
- The integrations mean AccuKnox fits the existing stack. Nothing gets ripped out on day one.

## Slide 29: Platformization, part two

- Modules seven through twelve cover runtime, cloud identity, secrets, static security, threat modeling and events.
- Secrets manager finds hardcoded credentials in source and hardens them at runtime. That covers build time and run time.
- CIEM correlates identity and permissions across clouds. Over-privileged accounts surface in one review instead of three.
- Events management centralizes logs with AI noise reduction. That is where the 80 percent alert reduction comes from.

## Slide 30: Roadmap

- Every item has a quarter and an engineering owner.
- If a date affects a renewal or an audit deadline, we commit it in writing.
- Design partner slots are open on several items. Design partners influence build order.

## Slide 31: Customer wins

- Sonesta Hotels cut engineering overhead by 45 percent.
- Prudent manages more than 200 cloud accounts on the platform for compliance and threat work.
- IDT Telecom runs AccuKnox for IoT and edge. Agentless tools cannot reach those because there is no cloud API to query.
- Case studies are at accuknox.com/case-studies. Reference calls are available by industry.

## Slide 32: Support matrix

- We support AWS, Azure, GCP, OpenStack and VMware, across public cloud, private cloud and bare metal.
- On-prem Kubernetes is first class. OpenShift, Rancher and RKE all work.
- We scan ECR, ACR, GCR and Docker Hub as part of supply chain security.
- Agentless vendors have no runtime visibility on-prem. A customer with an on-prem footprint gets posture data and no enforcement.

## Slide 33: GRC and compliance

- We ship 37 frameworks out of the box, including SOC2, HIPAA, NIST, PCI-DSS, CIS, MITRE and GDPR.
- CIS benchmarks and STIGs run on both VMs and Kubernetes clusters.
- Custom compliance lets a team map internal policy into the same engine and score it the same way.
- AI-assisted remediation gives the team a fix with the finding. That is what cuts time to remediation.

## Slide 34: Architecture and deployment

- One control plane covers all four deployment models. A mixed estate still reports into one console.
- On-prem, VM and bare metal deployments are native, not a modified SaaS agent.
- The air-gapped build has no telemetry and no outbound connection. That satisfies GDPR, DPDP and ITAR.
- Deployment docs are public at help.accuknox.com/getting-started/deployment-models.

## Slide 35: Analyst mentions

- We have three Gartner research mentions. Emerging Tech Techscape 2025, Hardened Container Images 2026, and State of AI for I&O.
- Omdia published a vendor profile on our CNAPP, written by Rik Turner in November 2025.
- We won two Frost and Sullivan awards in 2026, one global for AI stack security and one APAC for cloud security.
- Dr Edward Amoroso, former AT&T CSO, endorsed our AI Security 2.0 position on record.

## Slide 36: Industry recognition

- AWS named AccuKnox to its 2024 AI Partner Program. We won Agentic AI Security Startup of the Year in 2025.
- Red Hat verified our runtime agent on RHEL, so a Red Hat estate is a tested configuration.
- We are an Open Horizon project partner with IBM and mimik. That is where the edge and IoT work comes from.
- Our investors published why they invested. That answers a board question about vendor viability.

## Slide 37: Security coverage

- There are nine coverage areas here. Cloud, workload, Kubernetes, container, code, API, AI, secrets and events.
- Most teams find three or four of these with no clear owner when they map their current tools.
- Coverage gaps make the natural POC scope. Modules can be added at renewal instead of up front.

## Slide 38: POC timelines

- A scoped POC runs three weeks. Other CNAPP vendors need six to eight weeks for the same setup.
- Week one is onboarding and discovery. Week two is policy and findings. Week three is enforcement and the readout.
- Success criteria are agreed in writing before the POC starts.
- To start we need one cluster or one cloud account and about two hours from the customer's team.

## Slide 39: Reports

- Reports run on demand or on a schedule and arrive by email. Nobody builds the board pack by hand.
- There are separate views for executives, auditors and engineers.
- Everything exports to PDF and CSV. The same data is on the API.
- The sample report has the control-by-control evidence an audit team asks for.

## Slide 40: Close

- The next step is a technical deep dive with the platform team, then a three week scoped POC.
- Tell us which environments matter most and we send a POC plan within the week.
- support@accuknox.com reaches the team directly.

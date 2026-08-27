---
campaign: AccuKnox v3.6 release + AgentZ organizational support
account: AccuKnox on X
start: 2026-08-27
cadence: 2 per day, 07:30 and 19:30 IST
posts: 24
links: none, by design
---

A finding does not stop being work once the fix ships. Someone still rescans, updates the status, and closes the ticket by hand.

v3.6 moves a finding through verification into Fixed automatically after the follow-up scan, and closes the ticket with it.

Less status-chasing between the scanner, the ticket, and the security team.

media: https://help.accuknox.com/getting-started/images/release-notes/v3.6/findings-lifecycle-status-groups.png
alt: AccuKnox findings lifecycle showing status groups moving through verification into Fixed

---

would you hand your cloud credentials to an AI agent? most enterprise teams say no. so AgentZ agents never see them. the credential stays in a vault, a proxy injects it at call time, and the agent works with a placeholder. it does the task without holding the secret.

---

AI usage does not happen in one console. It happens in the browser. v3.6 ships the Gen AI prompt firewall as a plugin that covers:

- ChatGPT
- Claude
- Gemini
- GitHub Copilot
- Microsoft Copilot

It also blocks risky file uploads by extension before they reach the model. Enforcement sits where the prompts are typed.

media: https://help.accuknox.com/getting-started/images/release-notes/v3.6/prompt-firewall-browser-plugin-platforms.png
alt: AccuKnox Gen AI prompt firewall browser plugin listing the supported AI platforms

---

if your AI agent can read raw API keys, it is not ready for enterprise. in AgentZ the secret lives in a vault, a proxy swaps it in at call time, and the agent only ever sees a placeholder. the agent finishes the task and never holds the credential that makes it dangerous.

---

OpenAI said in February that prompt injection in AI browsers may never be fully patched. Agentic systems hit 84% attack success in testing.

Unpatchable means tested and contained, not ignored. v3.6 red teams models with generated prompts and gates AI traffic at a firewall.

---

A cloud finding rarely sits alone. One exposed S3 bucket touches the roles, instances, and data paths around it.

Security Graph in v3.6 maps those connected assets and shows the blast radius instead of triaging each alert on its own.

The value is the relationship between findings, in the same workflow where they get investigated.

media: https://help.accuknox.com/getting-started/images/release-notes/v3.6/security-graph-finding-s3.png
alt: AccuKnox Security Graph mapping an S3 bucket finding to its connected cloud assets

---

HR, DevOps, security and sales can run agents on the same platform without seeing each other's tools, configs or credentials. every workspace is isolated from the next. that isolation is the core of organization and workspace support, not a side effect of it.

media: .claude/skills/accuknox-social-campaign/campaigns/2026-08-v36-agentz/images/agentz-1-workspace.png
alt: AgentZ Create Workspace screen showing inherited organization resources as a shared foundation

---

Red teaming a model usually means hand-writing attack prompts for each model and use case.

v3.6 runs intelligent red team scans from the Assets page: set the model's purpose, pick prompt categories, and it generates the attack prompts and scores the risk.

Coverage stops depending on how many prompts a person can write by hand.

media: https://help.accuknox.com/getting-started/images/release-notes/v3.6/redteam-scan-modes.png
alt: AccuKnox intelligent red team scan modes and prompt category selection

---

Three runc flaws (CVE-2025-31133, -52565, -52881) turn a crafted mount config into a container escape that writes host procfs, past AppArmor and SELinux.

Once host access is possible, credentials and neighboring workloads become targets. Userspace runtime checks fail after the mount is trusted, and in-kernel enforcement holds. KubeArmor v3.6 runs DNS and file policy through BPF LSM at that boundary.

---

"multi-tenant AI platform" is easy to dismiss until you picture the alternative: every team running its own agent setup, secrets in env vars, no isolation, no governance. organization and workspace support is that sprawl prevented before it starts.

---

Onboarding an AWS account used to mean creating and storing long-lived access keys, then hoping they never leaked.

v3.6 onboards through an assume-role handshake with a CloudFormation stack. No static keys to rotate, store, or lose.

A credential that never exists cannot be stolen.

media: https://help.accuknox.com/getting-started/images/release-notes/v3.6/aws-assume-role-cloudformation.png
alt: AccuKnox AWS onboarding through an assume-role CloudFormation stack

---

one admin configures a connector
three workspaces inherit it
nine agents use it
zero teams rebuilt it

that is resource inheritance in AgentZ. configure a tool once at the org level and every workspace under it gets access without touching the config.

media: .claude/skills/accuknox-social-campaign/campaigns/2026-08-v36-agentz/images/agentz-4-onboarding.png
alt: AgentZ social admission screen showing default roles and teams applied at the organization level

---

Authenticated DAST tends to break at the login page. Multi-step logins and MFA stop the scanner before it reaches anything private.

The v3.6 recorder captures the full login, including TOTP MFA with configurable algorithm and period.

Secured parts of the app become testable, not only the public pages.

media: https://help.accuknox.com/getting-started/images/release-notes/v3.6/dast-authenticated-recorder-mfa.png
alt: AccuKnox authenticated DAST recorder configured with TOTP MFA

---

MCP tool poisoning hides instructions in tool descriptions and parameter schemas, the metadata an agent reads and a person never sees.

Benchmarks put attack success above 60%. The most resistant model refused under 3% of the time.

Agent security is not the prompt box. It is everything the agent trusts by default.

---

the difference between an AI agent demo and something a company runs on is not the model. it is who gets access, what each team inherits, what stays isolated, and whether anyone governs execution. that layer is what organization and workspace support in AgentZ handles.

media: .claude/skills/accuknox-social-campaign/campaigns/2026-08-v36-agentz/images/agentz-2-permissions.png
alt: AgentZ role editor showing the role, capability and scope layers of a permission

---

Hardening a fleet to STIG or CIS usually means manual checklists and spreadsheets. v3.6 automates it for Ubuntu 22.04 and 24.04:

- DISA STIG v2R8 and v1R5
- CIS Benchmark profiles
- 1000+ controls, automated and manual

Each control maps to a trackable finding, so drift shows up as a finding, not an audit-week surprise.

media: https://help.accuknox.com/getting-started/images/release-notes/v3.6/stig-finding-detail.png
alt: AccuKnox STIG control finding detail for Ubuntu

---

Microsoft 365 tenants drift from CIS benchmarks within weeks, and most teams only catch it by manually comparing settings.

v3.6 scans the tenant and returns each gap as a SARIF finding, in the same place as cloud and workload findings.

SaaS posture stops being a separate spreadsheet.

media: https://help.accuknox.com/getting-started/images/release-notes/v3.6/sspm-m365-finding-detail.png
alt: AccuKnox Microsoft 365 SSPM finding detail

---

one AgentZ workflow pulls critical findings from 17 cloud accounts, classifies them by severity, and emails a remediation report. every day, no human in the loop. that runs because the org layer scopes its credentials and permits only the hosts it needs.

---

The biggest AI supply-chain breach of 2026 started inside LiteLLM's build pipeline: a poisoned Trivy scanner, then two bad PyPI builds leaking cloud keys and Kubernetes secrets across 434k pipelines.

The first question after a poisoned package is which builds run where. SBOM findings in v3.6 track components and versions across the estate.

---

An open-source license can carry as much risk as a CVE, but license review usually lives in a separate legal or compliance track.

v3.6 surfaces license obligations as findings, with component, license type, and risk factors, next to the security findings.

One place to see both what is vulnerable and what is legally risky.

media: https://help.accuknox.com/getting-started/images/release-notes/v3.6/sbom-license-findings.png
alt: AccuKnox SBOM license findings showing component, license type and risk factors

---

you locked down your infra with zero-trust networking. deny-all by default, explicit allowlists, nothing talks to anything without a rule. AgentZ applies the same posture to agents. every agent pod starts deny-all and gets outbound access only where a rule permits it.

media: .claude/skills/accuknox-social-campaign/campaigns/2026-08-v36-agentz/images/agentz-3-sharing.png
alt: AgentZ share dialog limiting granted capabilities to least privilege

---

What does a Saudi bank map its AWS controls against? Not a generic benchmark.

v3.6 adds SAMA Cyber Security Framework scoring for AWS accounts, with per-control drill-down from the score to the finding behind it.

Regional compliance becomes part of the same posture view, not a manual mapping exercise.

media: https://help.accuknox.com/getting-started/images/release-notes/v3.6/sama-compliance-overview.png
alt: AccuKnox SAMA Cyber Security Framework compliance overview for an AWS account

---

CVE-2026-34040 lets an oversized payload slip past Docker's controls, launch a privileged container, mount the host filesystem, and read cloud credentials and kube configs.

Host filesystem access ends the debate. Blocking the mount at runtime beats waiting on a patch window.

---

2024: let the AI agent figure it out

2026: let the agent figure it out inside a deny-all sandbox, with inherited permissions, scoped credentials, and org-level governance

the second version is what it takes to run agents inside a real company.

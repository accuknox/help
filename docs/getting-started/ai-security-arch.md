---
title: AI Security Architecture
description: How AccuKnox AI Security is put together. The four enforcement layers, the path a model takes from a public registry into production, and the four ways the control plane reaches your AI assets.
---

# AI Security Architecture

Three things define the platform:

- **Eight modules**, each enforcing at one of four layers.
- **Three enforcement points**, on the path from a public registry to a live request.
- **Four collection methods**, one per kind of asset.

Read this before you onboard. The collection method decides what you install and where.

- To onboard an account, see the [AI Security onboarding guide](../how-to/aiml-overview.md).
- For CSPM, CWPP and ASPM, see [AccuKnox Enterprise Architecture](accuknox-arch.md).

## The Four Enforcement Layers

Each module reads from and enforces at the layer directly below it. Onboarding an account at the deployment layer is what makes the modules above it work.

<div class="ak-dia" role="img" aria-label="Four stacked layers. AI security modules on top, then AI assets, then substrate, then deployments. AI Identity Security and AI-GRC are marked coming soon.">
<svg viewBox="0 0 960 402" xmlns="http://www.w3.org/2000/svg">
  <rect class="p" x="16" y="16" width="928" height="112" rx="8"/>
  <text class="t-h" x="32" y="66">AI SECURITY</text>
  <text class="t-h" x="32" y="82">MODULES</text>

  <rect class="acc" x="158" y="32" width="181" height="38" rx="6"/>
  <text class="t-b" x="248" y="48" text-anchor="middle">AI-SPM</text>
  <text class="t-s" x="248" y="62" text-anchor="middle">Security posture management</text>

  <rect class="acc" x="356" y="32" width="181" height="38" rx="6"/>
  <text class="t-b" x="446" y="48" text-anchor="middle">AI Model and Dataset</text>
  <text class="t-b" x="446" y="62" text-anchor="middle">Security</text>

  <rect class="acc" x="554" y="32" width="181" height="38" rx="6"/>
  <text class="t-b" x="644" y="48" text-anchor="middle">Agentic AI Security</text>
  <text class="t-s" x="644" y="62" text-anchor="middle">ModelArmor sandbox</text>

  <rect class="acc" x="752" y="32" width="181" height="38" rx="6"/>
  <text class="t-b" x="842" y="48" text-anchor="middle">AI-DR</text>
  <text class="t-s" x="842" y="62" text-anchor="middle">Detect and respond</text>

  <rect class="acc" x="158" y="78" width="181" height="38" rx="6"/>
  <text class="t-b" x="248" y="94" text-anchor="middle">AI Guardrails</text>
  <text class="t-s" x="248" y="108" text-anchor="middle">Prompt Firewall</text>

  <rect class="acc" x="356" y="78" width="181" height="38" rx="6"/>
  <text class="t-b" x="446" y="94" text-anchor="middle">AI Red Teaming</text>
  <text class="t-s" x="446" y="108" text-anchor="middle">and pen testing</text>

  <rect class="hollow" x="554" y="78" width="181" height="38" rx="6" stroke-dasharray="4 4"/>
  <text class="t-s" x="644" y="94" text-anchor="middle">AI Identity Security</text>
  <text class="t-s" x="644" y="108" text-anchor="middle">Coming soon</text>

  <rect class="hollow" x="752" y="78" width="181" height="38" rx="6" stroke-dasharray="4 4"/>
  <text class="t-s" x="842" y="94" text-anchor="middle">AI-GRC</text>
  <text class="t-s" x="842" y="108" text-anchor="middle">Coming soon</text>

  <g class="ln-dash">
    <path d="M248 128 V162"/><path d="M446 128 V162"/>
    <path d="M644 128 V162"/><path d="M842 128 V162"/>
  </g>

  <rect class="p" x="16" y="162" width="928" height="64" rx="8"/>
  <text class="t-h" x="32" y="198">AI ASSETS</text>
  <rect class="p2" x="158" y="176" width="181" height="36" rx="6"/>
  <text class="t-b" x="248" y="199" text-anchor="middle">Agents</text>
  <rect class="p2" x="356" y="176" width="181" height="36" rx="6"/>
  <text class="t-b" x="446" y="199" text-anchor="middle">Models</text>
  <rect class="p2" x="554" y="176" width="181" height="36" rx="6"/>
  <text class="t-b" x="644" y="199" text-anchor="middle">Knowledge base</text>
  <rect class="p2" x="752" y="176" width="181" height="36" rx="6"/>
  <text class="t-b" x="842" y="199" text-anchor="middle">Tools</text>

  <rect class="p" x="16" y="242" width="928" height="64" rx="8"/>
  <text class="t-h" x="32" y="278">SUBSTRATE</text>
  <rect class="p2" x="158" y="256" width="181" height="36" rx="6"/>
  <text class="t-b" x="248" y="279" text-anchor="middle">Infrastructure</text>
  <rect class="p2" x="356" y="256" width="181" height="36" rx="6"/>
  <text class="t-b" x="446" y="279" text-anchor="middle">Application</text>
  <rect class="p2" x="554" y="256" width="181" height="36" rx="6"/>
  <text class="t-b" x="644" y="279" text-anchor="middle">Data</text>
  <rect class="p2" x="752" y="256" width="181" height="36" rx="6"/>
  <text class="t-b" x="842" y="279" text-anchor="middle">Network</text>

  <rect class="p" x="16" y="322" width="928" height="64" rx="8"/>
  <text class="t-h" x="32" y="358">DEPLOYMENTS</text>
  <rect class="p2" x="158" y="336" width="181" height="36" rx="6"/>
  <text class="t-b" x="248" y="359" text-anchor="middle">Public cloud</text>
  <rect class="p2" x="356" y="336" width="181" height="36" rx="6"/>
  <text class="t-b" x="446" y="359" text-anchor="middle">Private cloud</text>
  <rect class="p2" x="554" y="336" width="181" height="36" rx="6"/>
  <text class="t-b" x="644" y="359" text-anchor="middle">Air-gapped</text>
  <rect class="p2" x="752" y="336" width="181" height="36" rx="6"/>
  <text class="t-b" x="842" y="359" text-anchor="middle">Edge and IoT</text>
</svg>
</div>
<p class="ak-dia-cap">Six modules are generally available. AI Identity Security and AI-GRC are on the roadmap.</p>

AI Identity Security and AI-GRC are on the stack because the layer model accounts for them. Neither is in the console today, so plan coverage around the other six.

## The Three Enforcement Points

- **Pre-deployment scan.** Decides whether a model is allowed in at all.
- **ModelArmor sandbox.** Limits what a model or agent can do once it runs.
- **Prompt Firewall.** Inspects traffic in both directions.

The control plane schedules the first two and holds the policy for the third.

<div class="ak-dia" role="img" aria-label="Flow from public model sources through a pre-deployment scan into deployment infrastructure. A ModelArmor sandbox wraps models, agents and tools. The Prompt Firewall sits between users and the deployment and inspects traffic in both directions. Outbound traffic to an external command and control host is blocked.">
<svg viewBox="0 0 960 462" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="a1" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto">
      <path class="head" d="M0 0 L8 4 L0 8 z"/>
    </marker>
    <marker id="a2" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto">
      <path class="head-acc" d="M0 0 L8 4 L0 8 z"/>
    </marker>
  </defs>

  <rect class="plane" x="16" y="16" width="928" height="52" rx="8"/>
  <text class="t-plane" x="36" y="47">AccuKnox Control Plane</text>
  <rect class="plane-pill" x="430" y="28" width="150" height="28" rx="14"/>
  <text class="t-pill" x="505" y="46" text-anchor="middle">Model scan jobs</text>
  <rect class="plane-pill" x="596" y="28" width="150" height="28" rx="14"/>
  <text class="t-pill" x="671" y="46" text-anchor="middle">Red team runs</text>
  <rect class="plane-pill" x="762" y="28" width="166" height="28" rx="14"/>
  <text class="t-pill" x="845" y="46" text-anchor="middle">Firewall policy</text>

  <g class="ln-dash"><path d="M324 68 V140"/><path d="M722 68 V100"/></g>

  <rect class="p" x="16" y="140" width="180" height="120" rx="8"/>
  <text class="t-h" x="32" y="164">Model sources</text>
  <text class="t-b" x="32" y="188">Hugging Face</text>
  <text class="t-b" x="32" y="210">AWS Bedrock</text>
  <text class="t-b" x="32" y="232">On-prem store</text>

  <path class="ln" d="M196 200 H222" marker-end="url(#a1)"/>
  <text class="t-s" x="209" y="192" text-anchor="middle">pull</text>

  <rect class="p" x="226" y="140" width="196" height="120" rx="8"/>
  <text class="t-h" x="242" y="164">Pre-deployment scan</text>
  <rect class="p2" x="240" y="176" width="168" height="30" rx="6"/>
  <text class="t-b" x="324" y="196" text-anchor="middle">Sandbox evaluator</text>
  <rect class="good" x="240" y="216" width="80" height="30" rx="6"/>
  <text class="t-ok t-b" x="280" y="236" text-anchor="middle">Approved</text>
  <rect class="bad" x="328" y="216" width="80" height="30" rx="6"/>
  <text class="t-bad t-b" x="368" y="236" text-anchor="middle">Blocked</text>

  <path class="ln-acc" d="M422 200 H494" marker-end="url(#a2)"/>
  <text class="t-s" x="458" y="192" text-anchor="middle">approved</text>
  <text class="t-s" x="458" y="218" text-anchor="middle">models only</text>

  <rect class="p" x="500" y="100" width="444" height="240" rx="8"/>
  <text class="t-h" x="516" y="124">Deployment infrastructure</text>
  <rect class="p2" x="516" y="138" width="196" height="34" rx="6"/>
  <text class="t-b" x="614" y="160" text-anchor="middle">Datasets</text>
  <rect class="p2" x="728" y="138" width="200" height="34" rx="6"/>
  <text class="t-b" x="828" y="160" text-anchor="middle">Application and RAG</text>

  <rect class="hollow" x="510" y="186" width="424" height="104" rx="8" stroke-dasharray="5 4"/>
  <text class="t-acc t-h" x="524" y="206">ModelArmor sandbox</text>
  <rect class="p2" x="524" y="216" width="126" height="40" rx="6"/>
  <text class="t-b" x="587" y="240" text-anchor="middle">Models</text>
  <rect class="p2" x="664" y="216" width="126" height="40" rx="6"/>
  <text class="t-b" x="727" y="234" text-anchor="middle">AI agents,</text>
  <text class="t-b" x="727" y="249" text-anchor="middle">MCP servers</text>
  <rect class="p2" x="804" y="216" width="116" height="40" rx="6"/>
  <text class="t-b" x="862" y="240" text-anchor="middle">Tools</text>
  <text class="t-s" x="524" y="278">Process, file system, network and domain isolation</text>

  <path class="ln-acc" d="M660 380 V346" marker-end="url(#a2)"/>
  <path class="ln-acc" d="M660 346 V380" marker-end="url(#a2)"/>
  <text class="t-s" x="646" y="366" text-anchor="end">inspected both ways</text>

  <rect class="acc" x="600" y="380" width="130" height="64" rx="8"/>
  <text class="t-acc t-h" x="665" y="406" text-anchor="middle">Prompt</text>
  <text class="t-acc t-h" x="665" y="422" text-anchor="middle">Firewall</text>

  <path class="ln" d="M796 400 H736" marker-end="url(#a1)"/>
  <text class="t-s" x="766" y="394" text-anchor="middle">prompt</text>
  <path class="ln" d="M736 424 H796" marker-end="url(#a1)"/>
  <text class="t-s" x="766" y="440" text-anchor="middle">response</text>
  <rect class="p" x="802" y="386" width="110" height="52" rx="8"/>
  <text class="t-b" x="857" y="416" text-anchor="middle">Users</text>

  <path class="ln-bad" d="M540 340 V362 H392"/>
  <path class="ln-bad" d="M392 362 H182" stroke-dasharray="4 4"/>
  <g class="ln-bad"><path d="M386 356 L398 368"/><path d="M398 356 L386 368"/></g>
  <text class="t-bad t-s" x="392" y="348" text-anchor="middle">blocked</text>
  <rect class="bad" x="16" y="380" width="160" height="52" rx="8"/>
  <text class="t-bad t-b" x="96" y="402" text-anchor="middle">External C2 host</text>
  <text class="t-s" x="96" y="420" text-anchor="middle">no unlisted egress</text>
</svg>
</div>

- Only scanned models reach the deployment. The [CI/CD gate](../how-to/model-scan-cicd.md) enforces that on a pull request, not by convention.
- A poisoned model that does run still cannot reach an external host. The sandbox limits what it may execute, read and open.
- The Prompt Firewall is the only component in the request path.

!!! note "AI-DR reads events, it does not sit in the path"
    [AI-DR](../use-cases/aidr.md) ingests control-plane events from CloudTrail, Azure Event Hub and GCP logging, then evaluates them against policy. It operates out-of-band and adds no latency to inference. The Prompt Firewall is the inline component.

## The Four Collection Methods

Where the asset runs decides the method, not which module you want. A managed model in Bedrock needs an agentless cloud SDK. An inference engine installed on a VM is only found by scanning that VM.

<div class="ak-dia" role="img" aria-label="The AccuKnox control plane fans out to four targets: managed cloud AI services by agentless cloud SDK, cloud virtual machines by agentless snapshot scan, on-premises servers and endpoints by agent-based scan, and SaaS AI apps by browser plugin.">
<svg viewBox="0 0 940 330" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="a3" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto">
      <path class="head" d="M0 0 L8 4 L0 8 z"/>
    </marker>
  </defs>

  <rect class="plane" x="16" y="132" width="160" height="66" rx="8"/>
  <text class="t-plane" x="96" y="158" text-anchor="middle">AccuKnox</text>
  <text class="t-plane" x="96" y="176" text-anchor="middle">Control Plane</text>

  <path class="ln" d="M176 165 H236"/>
  <path class="ln" d="M236 73 V279"/>
  <path class="ln" d="M236 73 H448" marker-end="url(#a3)"/>
  <path class="ln" d="M236 155 H448" marker-end="url(#a3)"/>
  <path class="ln" d="M236 217 H448" marker-end="url(#a3)"/>
  <path class="ln" d="M236 279 H448" marker-end="url(#a3)"/>

  <text class="t-s" x="248" y="66">Agentless cloud SDK</text>
  <text class="t-s" x="248" y="148">Agentless VM snapshot scan</text>
  <text class="t-s" x="248" y="210">Agent-based VM scan</text>
  <text class="t-s" x="248" y="272">Browser plugin extension</text>

  <rect class="p" x="454" y="30" width="470" height="86" rx="8"/>
  <text class="t-h" x="470" y="52">Managed cloud AI services</text>
  <text class="t-b" x="470" y="74">AWS Bedrock and AgentCore</text>
  <text class="t-b" x="470" y="94">Azure AI Foundry and Copilot Studio</text>
  <text class="t-b" x="700" y="74">GCP Vertex AI</text>
  <text class="t-b" x="700" y="94">GCP Agents Platform</text>

  <rect class="p" x="454" y="132" width="470" height="46" rx="8"/>
  <text class="t-h" x="470" y="153">Cloud virtual machines</text>
  <text class="t-s" x="470" y="169">Unmanaged models and inference engines on cloud VMs</text>

  <rect class="p" x="454" y="194" width="470" height="46" rx="8"/>
  <text class="t-h" x="470" y="215">On-premises servers and endpoints</text>
  <text class="t-s" x="470" y="231">AI agents, MCP servers, inference engines, AI gateways</text>

  <rect class="p" x="454" y="256" width="470" height="46" rx="8"/>
  <text class="t-h" x="470" y="277">SaaS AI apps</text>
  <text class="t-s" x="470" y="293">Prompts leaving the browser for a third-party chat app</text>
</svg>
</div>

| Collection method | Reaches | Install | Onboarding guide |
|---|---|---|---|
| Agentless cloud SDK | Managed AI services in AWS, Azure and GCP | Nothing on the workload, a cloud role only | [AWS](../how-to/aiml-aws-onboard.md), [Azure](../how-to/aiml-azure-onboard.md), [GCP](../how-to/aiml-gcp-onboard.md) |
| Agentless VM snapshot scan | Models and inference engines on cloud VMs | Nothing on the VM | [Cloud onboarding](../how-to/aiml-overview.md) |
| Agent-based VM scan | On-prem servers and endpoints | AccuKnox agent on the host | [VM onboarding](../how-to/vm-onboard-deboard-systemd.md) |
| Browser plugin extension | SaaS AI apps used from a browser | Extension on the user's browser | [Chrome](../integrations/chrome-browser-integration.md), [Edge](../integrations/edge-browser-integration.md), [Firefox](../integrations/firefox-browser-integration.md) |

An asset reached by more than one method is still one asset in the inventory. Onboarding the same account twice does not duplicate it.

## Known Limits

- **AI-DR does not block.** It detects and routes. Blocking in the request path is the Prompt Firewall's job, and blocking at runtime is ModelArmor's.
- **The browser plugin only sees browser traffic.** A prompt sent from a desktop app or a terminal to the same SaaS model is outside its view. Use the SDK or a gateway for those.
- **The pre-deployment scan is a point-in-time check.** A model that passes today can be re-uploaded upstream with a different artifact, so re-scan on every version bump rather than once at adoption.
- **AI Identity Security and AI-GRC are not available yet.** Neither appears in the console today.

## Related Pages

- [AI Security onboarding guide](../how-to/aiml-overview.md), the click-path for each cloud
- [SaaS versus on-prem deployment](../how-to/aiml-saas-vs-onprem.md), what changes in an air-gapped install
- [AI Security integrations](../integrations/ai-overview.md), which firewall integration mode to pick
- [AccuKnox Enterprise Architecture](accuknox-arch.md), the platform-wide view
- [AI/ML Support Matrix](../support-matrix/aiml-support-matrix.md), supported platforms and formats

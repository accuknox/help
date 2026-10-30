---
title: Shadow AI Discovery
description: Shadow AI Discovery finds AI tools, agents, SDKs and MCP servers installed on Linux, Windows and macOS endpoints, VMs, Kubernetes and cloud accounts, and lists each one with its parent asset.
---

# Shadow AI Discovery

Shadow AI Discovery finds the AI tools, agents, SDKs and Model Context Protocol (MCP) components installed across your endpoints, VMs, Kubernetes clusters and cloud accounts. It lists each one in an inventory with its parent asset, version and findings, including software that never went through an approval process.

Discovery confirms that a tool is installed. It does not confirm that anyone uses it. A supported AI agent shows up even when it is not running and has never contacted an external AI service.

<div class="grid cards" markdown>

-   :material-laptop:{ .lg .middle .sai-ic } __Endpoints and VMs__

    ---

    The Omni agent finds CLI agents, desktop AI apps and IDE extensions on Linux, Windows and macOS.

    [:octicons-arrow-right-24: Endpoint discovery](#endpoint-discovery-finds-ai-tools-on-the-host)

-   :material-kubernetes:{ .lg .middle .sai-ic } __Kubernetes__

    ---

    The in-cluster scanner reads container images and maps each AI component to its workload.

    [:octicons-arrow-right-24: In-cluster scanning](../how-to/k8s-security-onboarding.md#in-cluster-container-image-scanning)

-   :material-cloud-outline:{ .lg .middle .sai-ic } __Cloud accounts__

    ---

    A read-only API connection finds models, datasets, compute and managed agents.

    [:octicons-arrow-right-24: Cloud discovery](#cloud-discovery-maps-ai-resources-and-their-connections)

-   :material-web:{ .lg .middle .sai-ic } __Browser__

    ---

    The browser plugin records access to GenAI services such as ChatGPT, Claude and Gemini.

    [:octicons-arrow-right-24: Browser usage](#discovery-also-covers-agentic-runtimes-and-browser-usage)

</div>

## Watch the Two-Minute Tour

Watch AccuKnox find AI agents, SDKs and MCP servers on VMs and containers.

<iframe width="560" height="315" src="https://www.youtube.com/embed/Rxs4fX6yKz0" title="AccuKnox Shadow AI Discovery product tour" frameborder="0" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Two Discovery Paths Feed Two Inventory Tabs

AccuKnox discovers cloud AI resources and installed AI software in different ways, so the inventory under **AI/ML Security → Assets** splits them into two tabs.

| Tab | What it holds | How AccuKnox finds it |
| --- | --- | --- |
| :material-cloud-check-outline:{ .sai-ic } **Managed** | AI resources in your cloud accounts, such as models, datasets, compute and managed agents | A read-only API connection to the onboarded cloud account |
| :material-laptop:{ .sai-ic } **Unmanaged** | AI software installed on endpoints, VMs and containers | The Omni agent on Linux, Windows and macOS endpoints, and the in-cluster scanner in Kubernetes |

The **Unmanaged** tab is where shadow AI appears. It lists AI software that sits outside centrally managed cloud AI resources and outside the approved software inventory.

## Cloud Discovery Maps AI Resources and Their Connections

After you onboard a cloud account, AccuKnox reads it through a read-only API. For each AI asset it records normalized metadata, inbound connectivity and exposure, and the services the asset connects to. The pipeline view then traces those connections, so a model endpoint appears with the subscription, resource group and services it is reachable through.

![AccuKnox AI/ML Security Assets inventory on the Managed tab, listing discovered LLM models with cloud type, region, and last seen date](./images/shadow-ai/managed-assets-models.png)

*The Managed tab groups cloud-discovered assets into Models, Datasets, and Computes, filterable by category, cloud type, and scan status.*

![Cloud discovery flow diagram: a read-only API connection to an onboarded cloud account drives asset discovery, which produces asset metadata, a connectivity overview, and a pipeline view](./images/shadow-ai/cloud-discovery-flow.svg)

![Cloud AI pipeline graph showing an Azure subscription linked to a resource group, an AI account, and an OpenAI service, with relationship labels and severity counts](./images/shadow-ai/cloud-pipeline-graph.png)

*The pipeline graph shows a model endpoint with the subscription, resource group, and services it is reachable through.*

The cloud path also discovers managed AI agents from Microsoft Copilot Studio, Microsoft 365 Agents, Azure AI Foundry, AWS Bedrock AgentCore and AWS Bedrock Agent. Each agent shows its source cloud, deployment status and finding counts. The detail pane shows memory configuration, IAM role and attached knowledge bases. See [AI App Inventory](../getting-started/3.5-release.md#ai-app-inventory-managed-agents-models-and-unmanaged-assets).

!!! info "Cloud onboarding guides"
    - [AWS AI/ML Cloud Onboarding](../how-to/aiml-aws-onboard.md)
    - [Azure AI/ML Cloud Onboarding](../how-to/aiml-azure-onboard.md)
    - [GCP AI/ML Cloud Onboarding](../how-to/aiml-gcp-onboard.md)

## Endpoint Discovery Finds AI Tools on the Host

On endpoints and VMs, the Omni agent scans the local filesystem for installation evidence of supported AI tools. Because Omni reads what is on disk, it finds CLI agents, desktop AI apps and IDE extensions whether or not anyone has opened them.

Discovery runs in five steps:

<ol class="sai-flow" markdown>
<li markdown="span"><span class="sai-step">:material-download-outline:</span><strong>1. Onboard</strong>Install Omni on a Linux, Windows or macOS endpoint.</li>
<li markdown="span"><span class="sai-step">:material-magnify-scan:</span><strong>2. Scan</strong>Omni reads the disk for AI installation artifacts and packages.</li>
<li markdown="span"><span class="sai-step">:material-cloud-upload-outline:</span><strong>3. Report</strong>Omni uploads the results through the artifact API.</li>
<li markdown="span"><span class="sai-step">:material-tag-outline:</span><strong>4. Classify</strong>AccuKnox assigns each component an AI/ML category.</li>
<li markdown="span"><span class="sai-step">:material-table-eye:</span><strong>5. Review</strong>Each tool appears on the Unmanaged tab with its endpoint.</li>
</ol>

The AI tool does not need network access to be discovered. Omni needs a path to upload results to AccuKnox. On an air-gapped endpoint, Omni can still scan, but the results reach the console only through an approved transfer process.

![On-prem discovery flow diagram: VM and in-cluster scanners feed package-level discovery, then vulnerability and malware scanning, a categorized asset view, and parent asset mapping](./images/shadow-ai/onprem-discovery-flow.svg)

In Kubernetes, the in-cluster scanner does the same job. It walks nodes and namespaces, reads container images and the workloads scheduled on them, and maps each AI component to its parent workload.

### Package-Level Discovery Catches AI Inside Custom Applications

Omni does not search for a fixed list of AI product names. It inventories every package on the scanned host, image or container across language ecosystems and OS package managers, then records the package name, version, known vulnerabilities and the host or image where it was found.

AccuKnox compares those packages against its AI/ML classification rules. A workload that bundles a model-serving runtime is classified as an **AI Inference Engine**, even inside a custom wrapper. A workload that bundles a vendor model client is classified as an **AI SDK**.

| Category | What it covers | Representative packages |
| --- | --- | --- |
| :material-robot-outline:{ .sai-ic } AI Agent | AI assistants and agent frameworks installed on endpoints or workloads | LangChain agents, CrewAI, AutoGen |
| :material-sitemap-outline:{ .sai-ic } AI Automation | Tools that build or run AI workflows | Flowise, Langflow |
| :material-router-network:{ .sai-ic } AI Gateway | Components that route or control access to models | LiteLLM, Portkey |
| :material-chip:{ .sai-ic } AI Inference Engine | Runtimes that run or serve models | vLLM, TGI, Triton, llama.cpp, Ollama |
| :material-brain:{ .sai-ic } AI-ML | Machine learning frameworks and libraries | PyTorch, TensorFlow, scikit-learn, Transformers |
| :material-code-braces:{ .sai-ic } AI SDK | Kits that call AI models from an application | OpenAI, Anthropic, Cohere, Google GenAI |
| :material-connection:{ .sai-ic } MCP | Model Context Protocol servers and clients | MCP server and client packages |

Detection rules decide the category, and not every category is detected on every operating system.

![Unmanaged tab grouped by category, listing AI Agent, AI Automation, AI Gateway, AI Inference Engine, AI-ML, AI SDK, and MCP with asset counts and severity-ranked findings](./images/shadow-ai/unmanaged-asset-categories.png)

*Scanner output rolled up into the seven AI/ML asset categories, each with its asset count and findings broken out by severity.*

### Every Asset Traces Back to Its Host

Each discovered asset can carry the asset name, category, technology, version, license, parent VM or endpoint, artifact label and discovery timestamp. A field stays empty when the installation artifact does not record that value.

![AccuKnox Unmanaged tab grouped by parent asset type, showing container and virtual machine asset counts with severity-ranked finding totals](./images/shadow-ai/unmanaged-parent-assets.png)

*Group the Unmanaged tab by parent asset type to see how many AI components sit on VMs versus containers.*

![Asset detail drawer for a discovered Go package, showing the AI-ML category, version, license, repository URL, PURL, and the raw JSON classification payload](./images/shadow-ai/unmanaged-asset-detail.png)

*The asset detail view shows the category, version, license and raw classification payload, plus Findings and Parent Asset tabs.*

## Each Operating System Has Its Own Onboarding Guide

Pick the guide for the operating system. Each guide covers installation, verification and troubleshooting.

<div class="grid cards" markdown>

-   :material-linux:{ .lg .middle .sai-ic } __Linux VM__

    ---

    Scans daily through the `omni.timer` systemd timer. Supports air-gapped install.

    [:octicons-arrow-right-24: Agent-Based VM Scanning for Linux](../how-to/vm-security/agent-based/linux.md)

-   :material-microsoft-windows:{ .lg .middle .sai-ic } __Windows endpoint__

    ---

    Scans through the `AccuKnox Omni Vuln Scan` scheduled task. Supports air-gapped install.

    [:octicons-arrow-right-24: Agent-Based VM Scanning for Windows](../how-to/vm-security/agent-based/windows.md)

-   :material-apple:{ .lg .middle .sai-ic } __macOS endpoint__

    ---

    Scans daily through the `com.accuknox.omni` launchd job. Online install only.

    [:octicons-arrow-right-24: Agent-Based Scanning for macOS](../how-to/vm-security/agent-based/macos.md)

-   :material-kubernetes:{ .lg .middle .sai-ic } __Kubernetes__

    ---

    The in-cluster scanner reads container images and the workloads that run them.

    [:octicons-arrow-right-24: In-cluster container image scanning](../how-to/k8s-security-onboarding.md#in-cluster-container-image-scanning)

</div>

## Validated Use Cases Cover CLI Agents, Desktop Apps and IDE Extensions

AccuKnox validated endpoint discovery by installing AI tools on a Linux VM, a Windows endpoint and a Mac, then running one Omni scan on each. Every tool appeared under **AI/ML Security → Assets → Unmanaged**, mapped to the expected endpoint and artifact label.

| Endpoint | AI tools discovered in one scan |
| --- | --- |
| :material-linux:{ .sai-ic } Linux VM (Ubuntu) | <span class="sai-chips"><span class="sai-chip">Junie</span><span class="sai-chip">GitHub Copilot</span><span class="sai-chip">OpenCode</span><span class="sai-chip">Cody</span><span class="sai-chip">BLACKBOX AI</span><span class="sai-chip">Cursor</span></span> |
| :material-microsoft-windows:{ .sai-ic } Windows | <span class="sai-chips"><span class="sai-chip">Codex CLI</span><span class="sai-chip">ChatGPT desktop app</span><span class="sai-chip">Cline</span><span class="sai-chip">AnythingLLM</span><span class="sai-chip">Tabnine</span><span class="sai-chip">GitHub Copilot</span></span> |
| :material-apple:{ .sai-ic } macOS | <span class="sai-chips"><span class="sai-chip">Gemini CLI</span><span class="sai-chip">Kiro</span><span class="sai-chip">Continue</span><span class="sai-chip">Codex CLI</span><span class="sai-chip">GitHub Copilot</span><span class="sai-chip">npm: &#64;google/gemini-cli</span><span class="sai-chip">npm: &#64;github/copilot</span></span> |

The tests cover the three ways a developer installs an AI tool on an endpoint:

<div class="grid cards" markdown>

-   :material-console:{ .lg .middle .sai-ic } __CLI coding agents__

    ---

    Run in a terminal with the developer's shell access. Tested with Codex CLI on Windows, Gemini CLI on macOS and OpenCode on Linux.

-   :material-application-outline:{ .lg .middle .sai-ic } __Desktop AI apps__

    ---

    Installed as standalone applications. Tested with the ChatGPT desktop app on Windows and Kiro on macOS.

-   :material-puzzle-outline:{ .lg .middle .sai-ic } __IDE extensions__

    ---

    Installed inside an editor. Tested with Cline and Continue in Visual Studio Code.

</div>

=== ":material-linux: Linux VM"

    ![Unmanaged tab, AI Agent category, listing Junie, GitHub Copilot, OpenCode, Cody, BLACKBOX AI and Cursor on the parent ubuntu-VM with the devshadowai label](./images/shadow-ai/endpoints/linux-ai-agents-unmanaged.png)

    *Six AI coding agents found on one Ubuntu VM, each with its version and license. None had to be running.*

=== ":material-microsoft-windows: Windows"

    ![Unmanaged tab, AI Agent category, listing Codex CLI, AnythingLLM, Cline, Tabnine, GitHub Copilot and ChatGPT on one Windows endpoint, with the ChatGPT row highlighted](./images/shadow-ai/endpoints/windows-chatgpt-unmanaged.png)

    *One Windows endpoint shows a CLI agent (Codex CLI), a desktop app (ChatGPT) and an IDE extension (Cline) in the same AI Agent list.*

=== ":material-apple: macOS"

    ![Unmanaged tab, AI Agent category, listing Gemini CLI, Kiro, Codex CLI, Continue, GitHub Copilot and three npm agent packages on one Mac, with the Kiro row highlighted](./images/shadow-ai/endpoints/macos-kiro-unmanaged.png)

    *One Mac shows Gemini CLI, the Kiro desktop app and the Continue extension, plus the npm packages behind Gemini CLI and GitHub Copilot.*

Hostnames and the tenant name are redacted in every screenshot. The onboarding guides show each test in two shots: the tool installed on the endpoint, then the same tool on the **Unmanaged** tab.

### Repeat the Validation on Your Own Endpoint

1. Install an AI tool on a test endpoint, such as Codex CLI, the ChatGPT desktop app or the Cline extension in Visual Studio Code.
2. Confirm that the tool runs on the endpoint.
3. Install Omni with your artifact endpoint, tenant ID, artifact label and Artifact API token. Use the guide for the operating system from [the onboarding guides](#each-operating-system-has-its-own-onboarding-guide).
4. Let the first scan finish. Check the scan log for errors.
5. Open **AI/ML Security → Assets → Unmanaged** in the AccuKnox console.
6. Find the tool and confirm that it lists the expected endpoint and artifact label.

You do not need to sign in to the AI tool or send it a prompt. An installed tool is enough for discovery.

## Discovery Also Covers Agentic Runtimes and Browser Usage

:material-robot-outline:{ .sai-ic } **Agentic runtimes.** Agentic AI runtimes install like any other package, so the same package-level scan finds them. AccuKnox scans VMs for OpenClaw instances and reports each one under the **Unmanaged** tab with its parent host, version and vulnerability data.

:material-web:{ .sai-ic } **GenAI usage in the browser.** The AccuKnox browser plugin detects access to known GenAI services such as ChatGPT, Claude, Gemini and Copilot. It records the user identity, timestamp and accessed domain, which gives you audit evidence and policy violation detection for AI use that installs nothing on the endpoint.

## What Endpoint Discovery Does Not Do

- :material-eye-off-outline:{ .sai-ic } **It does not show usage.** Discovery confirms installation evidence. It does not record who ran a tool, when, or what data the tool sent.
- :material-filter-outline:{ .sai-ic } **It covers supported tools only.** Coverage depends on the operating system, the Omni version, the detection rules and the evidence the install leaves on disk.
- :material-lan-disconnect:{ .sai-ic } **It needs a reporting path.** An endpoint that cannot reach the AccuKnox artifact endpoint scans locally, and its results reach the console only through an approved transfer process.

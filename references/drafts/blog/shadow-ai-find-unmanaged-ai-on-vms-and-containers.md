---
title: "Find Shadow AI on Your VMs and Containers, Down to the Package"
seo_title: "How to Find Shadow AI on VMs and Containers | AccuKnox"
meta_description: "Find shadow AI on your VMs and containers. See how AccuKnox sorts unmanaged AI agents, SDKs and MCP servers into 7 asset types, down to every package."
slug: "shadow-ai-find-unmanaged-ai-on-vms-and-containers"
url: "https://accuknox.com/blog/shadow-ai-find-unmanaged-ai-on-vms-and-containers"
primary_keyword: "find shadow AI"
secondary_keywords: ["shadow AI discovery", "unmanaged AI assets", "MCP server discovery", "AI asset inventory"]
excerpt: "AccuKnox scans your VMs and containers and lists every unmanaged AI agent, SDK and MCP server by asset type, host and package."
category: "AI-SPM"
author: "Atharva Shah"
date: 2026-10-09
reading_time: "5 minutes"
word_count_target: 1000
audience: "security engineer | cloud engineer"
cover_image_prompt_claude: >
  Not used. The cover is the YouTube thumbnail for the shadow AI tour video.
cover_image_prompt_midjourney: >
  Not used. The cover is the YouTube thumbnail for the shadow AI tour video.
---

# Find shadow AI on your VMs and containers, down to the package

![Thumbnail of the AccuKnox video that shows how to find shadow AI on VMs and containers](https://img.youtube.com/vi/Rxs4fX6yKz0/maxresdefault.jpg)

*Caption: The thumbnail of the two-minute AccuKnox shadow AI product tour.*

## TL;DR

- AccuKnox scans your VMs and containers, then lists the AI software it finds under the **Unmanaged** tab of **AI/ML Security > Assets**.
- The demo environment in this post holds 817 unmanaged AI assets, 529 on virtual machines and 288 in containers. That is demo data, not a customer result.
- A classifier sorts every package into 1 of 7 asset types, from AI Agent to MCP.
- The scanners read every package on the host, not a fixed list of AI product names. An AI library inside a custom app still appears.
- Setup is one install script and a daily timer on a Linux VM. On Kubernetes, an in-cluster scanner job runs on each node.
- The Unmanaged view is inventory and discovery. It does not block a package.

## The Unmanaged Tab Lists the AI That Nobody Registered

Shadow AI is AI software that runs in your environment without an approval or an asset register entry. AI agents and MCP servers on a build VM are typical examples. [AccuKnox AI Security](https://accuknox.com/platform/ai-security) finds them without a declared inventory, so you do not need to know what to look for.

Open **AI/ML Security > Assets**. The page has two tabs. The **Managed** tab lists AI services in your onboarded cloud accounts. The **Unmanaged** tab lists everything the scanners find on your own hosts.

![The AI/ML Security Assets page with the Managed tab open and the Unmanaged tab marked Found on your hosts](https://media.zernio.com/temp/1791272957123_zbs04jgq_s01-managed-unmanaged.jpg)

*Caption: The Unmanaged tab, marked Found on your hosts, sits next to the Managed tab for cloud AI services.*

Stay on **Unmanaged** for the rest of this walkthrough. The [Shadow AI Discovery help page](https://help.accuknox.com/use-cases/shadow-ai-discovery/) covers the cloud side and the Managed tab in full. For the wider risk picture, read [shadow AI security explained](https://accuknox.com/blog/shadow-ai-security-explained).

## Grouping by Category and Parent Shows What Runs Where

Group the inventory by **Category**. The scanners sort every AI component into seven asset types. Each row shows its asset count and its findings by severity.

![The Unmanaged tab grouped by category, listing the seven AI asset types with asset counts and findings by severity](https://media.zernio.com/temp/1791272959336_naswon5l_s02-seven-types.jpg)

*Caption: All seven asset types appear as rows, each with its asset count and its findings by severity.*

| Asset type | Typical packages | Demo assets |
| --- | --- | --- |
| AI Agent | LangChain agents, CrewAI, AutoGen | 26 |
| AI Automation | Flowise, Langflow | 37 |
| AI Gateway | LiteLLM, Portkey | 9 |
| AI Inference Engine | vLLM, TGI, Triton, llama.cpp, Ollama | 18 |
| AI-ML | PyTorch, TensorFlow, scikit-learn, Transformers | 466 |
| AI SDK | OpenAI, Anthropic, Cohere, Google GenAI | 241 |
| MCP | Model Context Protocol server and client packages | 20 |

The seven demo counts add up to the 817 unmanaged assets. The package examples come from the [Shadow AI Discovery help page](https://help.accuknox.com/use-cases/shadow-ai-discovery/).

Next, group the same inventory by **Parent Asset Type**. This splits what runs in containers from what runs on virtual machines. The demo data shows 288 container assets and 529 virtual machine assets.

![The Unmanaged tab grouped by parent asset type, with 288 assets in containers and 529 on virtual machines](https://media.zernio.com/temp/1791272960908_0m0h01fy_s03-parents.jpg)

*Caption: The parent view shows 288 assets in containers and 529 on virtual machines.*

## Expanding a Type Lists Every Package With Its Host and Version

Expand an asset type to list each package. The **MCP** type lists MCP packages with the host, language, version and license of each. SDKs for OpenAI and LangSmith show up too, and so do agent frameworks.

![The MCP type expanded to list MCP packages with their host, language, version and license](https://media.zernio.com/temp/1791272962566_z5uj678w_s04-mcp.jpg)

*Caption: Expanding the MCP type lists each package with its host, language, version and license.*

![The package list with an OpenAI SDK and an agent framework highlighted](https://media.zernio.com/temp/1791272964556_andw290m_s05-sdks.jpg)

*Caption: The same list shows SDKs such as OpenAI and agent frameworks, each with its host, version and license.*

The scanner does not match against a list of product names. It reads every package on the host or in the container image. For each package it records the name, the version and the known vulnerabilities for that version. It also records artifact metadata, which says where the package sits.

AccuKnox sends that data to a classification service. The service compares package names and known library families against AccuKnox AI/ML classification rules, then assigns an asset type. An AI library inside a custom wrapper or application still gets classified.

## A Package Detail View Ties the Package to Its Findings and Its Host

Open one package to see its category, version, license and package URL (PURL). The PURL is the package's unique address, such as `pkg:pypi/google-generativeai@0.5.0` for the SDK in the video. In the video, the SDK's own description says it is deprecated. That marks it as a candidate for replacement.

The **Findings** tab lists the vulnerabilities tied to that package version. The **Parent Asset** tab names the VM or container workload that holds it. Together they answer the two questions an owner asks first: what is wrong with it, and who runs it.

![The asset detail panel of a deprecated Google generative AI SDK, with its category and package URL highlighted](https://media.zernio.com/temp/1791272966649_vxd94hkz_s06-detail.jpg)

*Caption: One package opens into its category, version, license and PURL, with tabs for its findings and its parent asset.*

> **Limitation.** The Unmanaged view is inventory and discovery. It lists a package and its findings, and it does not block the package.

## Setup Takes One Script per Linux VM and One Scanner per Cluster

The Unmanaged tab fills only after a scanner runs. Use the scanner that matches the host.

![The Turn On Shadow AI Discovery card with the Linux VM install script and the Kubernetes in-cluster scanner](https://media.zernio.com/temp/1791272968316_jyc96af1_s07-setup.jpg)

*Caption: The setup card shows the Linux VM install script and the in-cluster scanner for Kubernetes.*

**Linux VM.** You need root or sudo access, outbound internet access to AccuKnox SaaS and `curl`. You also need your Tenant ID and Artifact API token. Run the install script from the [Linux VM scanning guide](https://help.accuknox.com/how-to/vm-security/agent-based/linux/).

```bash
curl https://accuknox-omni.s3.us-east-1.amazonaws.com/latest/agent-install.sh | \
    OMNI_ARTIFACT_API_TOKEN="<REDACTED>" \
    bash -s - \
        --artifact-endpoint=https://cspm.accuknox.com/api/v1/artifact/ \
        --tenant-id=000 \
        --artifact-label=CHANGEME
```

Swap `<REDACTED>` for a token from **Settings > Tokens**. Use a label from **Settings > Labels** in place of `CHANGEME`. Put your Tenant ID where `000` sits, and change the endpoint if your environment differs. The script creates `omni.service` and a daily timer, `omni.timer`.

**Kubernetes.** Deploy the in-cluster scanner from the [Kubernetes onboarding guide](https://help.accuknox.com/how-to/k8s-security-onboarding/#in-cluster-container-image-scanning). It runs as a job on each node and reads the container images cached there. It needs no registry access, and it sends results to the AccuKnox console.

## See the Unmanaged Tab Sort AI Assets by Type, Parent and Package

The tour below runs under 2 minutes and follows the same steps in the same order.

```html
<iframe width="560" height="315" src="https://www.youtube.com/embed/Rxs4fX6yKz0" title="Find Shadow AI on Your VMs and Containers With AccuKnox" frameborder="0" allowfullscreen></iframe>
```

[Watch the shadow AI tour on YouTube](https://www.youtube.com/watch?v=Rxs4fX6yKz0).

## FAQs

### What counts as shadow AI?

Shadow AI is AI software that runs in your environment without an approval or an asset register entry. It includes agentic AI runtimes such as OpenClaw. AccuKnox scans VMs for OpenClaw instances and lists each one as an unmanaged asset, mapped to its parent host.

### How does AccuKnox find AI inside a custom app?

The scanner reads every package on the host or in the container image. It needs no list of AI product names. A classifier then maps each package to one of the seven asset types. A model client or serving runtime inside a custom app is classified the same way as a standalone one.

### Does the Unmanaged view block a package?

The Unmanaged view does not block a package. It is inventory and discovery. It shows each package, its version, its findings and its parent host, and you decide what to do next.

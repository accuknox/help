---
title: YouTube Publish Sheet for the Shadow AI Discovery Product Tour
video: references/video-edits/shadow-ai-tour/output/accuknox-shadow-ai-tour.mp4
sources:
  - docs/use-cases/shadow-ai-discovery.md
  - docs/getting-started/3.5-release.md
  - docs/how-to/vm-security/agent-based/linux.md
  - docs/how-to/k8s-security-onboarding.md
  - references/video-edits/shadow-ai-tour/output/timeline.json
posted: false
---

# YouTube Publish Sheet for the Shadow AI Discovery Product Tour

Chapter times come from the render's `timeline.json`. Every chapter runs 11 seconds or more.
Upload settings match the DSPM and CIEM sheet: channel `accuknox`, Science & Technology, not made
for kids, English, captions from `output/narration.srt`, Unlisted first.

**File:** `references/video-edits/shadow-ai-tour/output/accuknox-shadow-ai-tour.mp4`, 1:51

**Title**

```text
Find Shadow AI on Your VMs and Containers With AccuKnox
```

Alternates for the YouTube Studio title test:

- `Find Unmanaged AI Agents, SDKs and MCP Servers`
- `Shadow AI Discovery in 2 Minutes`

**Thumbnail text:** "AI nobody approved?" over the Unmanaged tab with the seven asset types and their counts.

**Description**

```text
AccuKnox finds AI agents, SDKs, MCP servers and model runtimes on your VMs and containers, sorted into 7 asset types. A 2-minute tour.

How it works: https://help.accuknox.com/use-cases/shadow-ai-discovery/
Linux VM setup: https://help.accuknox.com/how-to/vm-security/agent-based/linux/
Kubernetes setup: https://help.accuknox.com/how-to/k8s-security-onboarding/
AccuKnox AI Security: https://accuknox.com/platform/ai-security

Shadow AI is AI software that runs in your environment without an approval or an asset register entry. The demo environment in this tour holds 817 unmanaged AI assets: 529 on virtual machines and 288 in containers.

What you will see:
- The Managed and Unmanaged tabs: cloud AI services versus what the scanners find on your hosts
- Seven asset types: AI Agent, AI Automation, AI Gateway, AI Inference Engine, AI-ML, AI SDK and MCP, each with findings by severity
- The same inventory grouped by parent: virtual machines and containers
- MCP packages, OpenAI and LangSmith SDKs, and an agent framework, each with its host, version and license
- A package detail with its category, license and package URL (PURL), plus the Findings and Parent Asset tabs

The scanners read every package on the host or in the container image, instead of a fixed list of AI product names. A classifier maps each package to an asset type, so an AI library inside a custom app still shows up. The Unmanaged view is inventory and discovery, and it does not block a package.

Chapters:
0:00 Why AI assets go unregistered
0:16 Managed vs unmanaged AI assets
0:27 Seven AI asset types on VMs and containers
0:55 MCP servers, AI SDKs and agent frameworks by package
1:14 Package details: version, license and PURL
1:28 Set up the VM and Kubernetes scanners
```

**Tags**

```text
shadow AI, shadow AI discovery, unmanaged AI assets, AI asset discovery, AI asset inventory, AI security, AI-SPM, MCP server security, MCP servers, AI agent security, AI SDK, LLM security, AccuKnox, AccuKnox AI security, Kubernetes security, VM security, PURL
```

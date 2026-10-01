---
title: AI Security Use Cases
description: Explore AccuKnox AI security use cases across the eight modules, from AI-SPM and AI-DR to Agentic AI Security, Model & Dataset Security, Red Teaming, and Prompt Firewall guardrails.
hide:
  - toc
---

# AI Security Use Cases

<style>
  .nt-card-title{
    text-align: center;
  }

  .nt-card-img img{
    color: #00025;
  }
</style>

!!! note "Useful Links"
    - For onboarding refer to the [**AI Security Onboarding Guide**](https://help.accuknox.com/how-to/aiml-overview/)
    - For list of supported platforms refer to the [**AI Security Support Matrix**](https://help.accuknox.com/support-matrix/aiml-support-matrix/)

::cards:: cols=4

- title: AI Posture Management (AI-SPM)
  image: ./icons/AIML.svg
  url: /how-to/aiml-overview/

- title: AI Detect & Respond (AI-DR)
  image: ./icons/aidr.svg
  url: /use-cases/aidr/

- title: Agentic AI Security
  image: ./icons/mcp-security.svg
  url: /use-cases/modelarmor/

- title: AI Model & Dataset Security
  image: ./icons/modelarmor.svg
  url: /use-cases/modelarmor-pickle-code/

- title: AI Red Teaming & Pen Testing
  image: ./icons/model-safety.svg
  url: /use-cases/red-teaming/

- title: AI Guardrails (Prompt Firewall)
  image: ./icons/AIML.svg
  url: /use-cases/prompt-firewall-overview/

::/cards::

**AI Identity Security** and **AI Compliance & Governance (AI-GRC)** are on the roadmap and not in the console today. Plan coverage around the six above.

## Which Module for Which Job

| What you need to do | Module | You are covered when |
|---|---|---|
| Check a public model before adopting it | [ML Model Static Scans](../how-to/ml-static-scan.md) | Only scanned and approved models reach your registry |
| Make that check impossible to skip | [Model scan in CI/CD](../how-to/model-scan-cicd.md) | A model enters the registry only through a merged pull request |
| Test a model against jailbreaks and injection | [AI Red Teaming](red-teaming.md) | High-risk attack paths are found and fixed before production |
| Stop harmful prompts and data leakage in the request path | [Prompt Firewall](prompt-firewall-overview.md) | Unsafe prompts and responses never reach the user or the model |
| Constrain what an autonomous agent may execute or reach | [Agentic AI Security](modelarmor.md) | Agents act only inside the process, file, network and domain limits you set |
| Detect abuse of AI services from cloud events | [AI-DR](aidr.md) | Runtime threats are detected and routed to a named owner |
| Find AI tools nobody approved | [Shadow AI Discovery](shadow-ai-discovery.md) | Unapproved AI usage is visible in the inventory |
| Keep an inventory of models, agents and datasets | [AI-SPM](../how-to/aiml-overview.md) | Every AI asset has an owner and a risk classification |

!!! tip "Not sure which module reaches your assets?"
    The [AI security architecture](../getting-started/ai-security-arch.md) page maps the four collection methods to the four kinds of asset, which is what decides whether you install an agent, a browser extension, or nothing at all.

## More AI Use Cases

::cards:: cols=4

- title: Jupyter Notebook Security
  image: ./icons/jupyter.svg
  url: /use-cases/jupyter-notebook/

- title: Adversarial Attacks on ML Models
  image: ./icons/model-safety.svg
  url: /use-cases/modelarmor-adverserial-attacks/

- title: Deploy ModelArmor with PyTorch
  image: ./icons/modelarmor.svg
  url: /use-cases/modelarmor-deploy-pytorch/

- title: Categories & Probes
  image: ./icons/model-safety.svg
  url: /use-cases/subprompts-categories/

- title: MCP Security
  image: ./icons/mcp-security.svg
  url: /integrations/mcp-server/

::/cards::

## Featured Videos

<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; margin: auto; font-family: Arial, sans-serif;">

  <!-- AI Onboarding -->
  <div style="background:#fff; border-radius:12px; box-shadow:0 2px 8px rgba(0,0,0,0.06); overflow:hidden;">
    <div style="aspect-ratio:16/9;">
      <iframe width="100%" height="100%" src="https://www.youtube.com/embed/qTDQjmm8698" title="AI Copilot" frameborder="0" allowfullscreen style="border:0;"></iframe>
    </div>
    <div style="padding:8px;">
      <h4 style="margin:0 0 4px; display:flex; align-items:center; gap:6px;">
        AI Onboarding
      </h4>
      <p style="margin:0; font-size:0.75rem; color:#555;">Enhance security operations with AI-driven insights, automated threat detection, and response recommendations.</p>
    </div>
  </div>

  <!-- Model Safety -->
  <div style="background:#fff; border-radius:12px; box-shadow:0 2px 8px rgba(0,0,0,0.06); overflow:hidden;">
    <div style="aspect-ratio:16/9;">
      <iframe width="100%" height="100%" src="https://www.youtube.com/embed/eK69KNytMWo" title="Model Safety" frameborder="0" allowfullscreen style="border:0;"></iframe>
    </div>
    <div style="padding:8px;">
      <h4 style="margin:0 0 4px; display:flex; align-items:center; gap:6px;">
        Model Safety
      </h4>
      <p style="margin:0; font-size:0.75rem; color:#555;">Safeguard models from misuse and ensure responsible AI behavior through explainability and guardrails.</p>
    </div>
  </div>

</div>

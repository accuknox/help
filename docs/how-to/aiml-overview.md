---
title: AI Security Posture Management (AI-SPM)
description: "Get started with AccuKnox AI-SPM. Onboard AI/ML assets and set up every AI security module: AI-DR, Agentic AI Security, Model & Dataset Security, Red Teaming, and Prompt Firewall guardrails."
hide:
  - toc
---

# AI Security Posture Management (AI-SPM)

<style>
  .nt-card-title{
    text-align: center;
  }

  .nt-card-img img{
    color: #00025;
  }

  /* Module chips: the 8 AI security modules as a compact pill row. Wraps
     naturally on narrow screens, no fixed column count to fight.
     The selector has to out-specify Material's own
     `.md-typeset ul:not([hidden]){display:flow-root}`, hence the
     `ul.ak-modules:not([hidden])` shape rather than a plain class. */
  .md-typeset ul.ak-modules:not([hidden]) {
    display: flex;
    flex-wrap: wrap;
    gap: .5rem;
    margin: .9rem 0 1.4rem;
    padding: 0;
    list-style: none;
  }

  .md-typeset ul.ak-modules li {
    margin: 0;
    padding: 0;
    list-style: none;
  }

  .md-typeset ul.ak-modules li::marker { content: none; }

  .md-typeset .ak-module {
    display: inline-flex;
    align-items: center;
    gap: .4rem;
    padding: .38rem .8rem;
    border: 1px solid var(--md-default-fg-color--lightest);
    border-radius: 999px;
    background: var(--md-code-bg-color);
    color: var(--md-default-fg-color);
    font-size: .78rem;
    font-weight: 600;
    line-height: 1.35;
    text-decoration: none;
    transition: border-color .15s, background .15s, color .15s;
  }

  .md-typeset a.ak-module {
    color: var(--md-default-fg-color);
  }

  .md-typeset a.ak-module:hover {
    border-color: var(--md-primary-fg-color);
    background: var(--md-primary-fg-color);
    color: var(--md-primary-bg-color);
  }

  .md-typeset a.ak-module::after {
    content: "→";
    font-weight: 400;
    opacity: .55;
  }

  .md-typeset .ak-module--soon {
    border-style: dashed;
    background: transparent;
    color: var(--md-default-fg-color--light);
    font-weight: 500;
  }

  .md-typeset .ak-module--soon span {
    padding: .05rem .35rem;
    border-radius: 4px;
    background: var(--md-default-fg-color--lightest);
    font-size: .64rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: .03em;
  }
</style>

AccuKnox AI-SPM discovers and protects your AI/ML assets. Run every AI security module from one console:

<ul class="ak-modules">
  <li><a class="ak-module" href="/use-cases/aidr/">AI Detect &amp; Respond (AI-DR)</a></li>
  <li><a class="ak-module" href="/use-cases/modelarmor/">Agentic AI Security</a></li>
  <li><a class="ak-module" href="/use-cases/modelarmor-pickle-code/">AI Model &amp; Dataset Security</a></li>
  <li><a class="ak-module" href="/use-cases/red-teaming/">AI Red Teaming &amp; Pen Testing</a></li>
  <li><a class="ak-module" href="/use-cases/prompt-firewall-overview/">AI Guardrails (Prompt Firewall)</a></li>
  <li><span class="ak-module ak-module--soon">AI Identity Security <span>Coming soon</span></span></li>
  <li><span class="ak-module ak-module--soon">AI Compliance &amp; Governance (AI-GRC) <span>Coming soon</span></span></li>
</ul>

## Cloud Onboarding

Onboard a cloud account to discover AI/ML assets and enable red teaming and posture scanning across your models and datasets.

::cards:: cols=4

- title: AWS
  image: ./icons/aws-vm.svg
  url: /how-to/aiml-aws-onboard/

- title: Azure
  image: ./icons/azure-vm.svg
  url: /how-to/aiml-azure-onboard/

- title: GCP
  image: ./icons/gcp-vm.svg
  url: /how-to/aiml-gcp-onboard/

- title: On-Prem Models
  image: ./icons/onprem.svg
  url:

::/cards::

## Set Up a Security Module

::cards:: cols=4

- title: Red Teaming & Pen Testing
  image: ./icons/model-safety.svg
  url: /how-to/aiml-custom-model-redteaming/

- title: LLM Static Scans
  image: ./icons/sast.svg
  url: /how-to/llm-static-scan/

- title: ML Static Scans
  image: ./icons/supply-chain-attacks.svg
  url: /how-to/ml-static-scan/

- title: Prompt Firewall Setup
  image: ./icons/AIML.svg
  url: /how-to/prompt-firewall/

- title: Prompt Firewall App (SDK)
  image: ./icons/AIML.svg
  url: /how-to/llm-defense-app-onboard/

- title: Runtime Defense (API)
  image: ./icons/mcp-security.svg
  url: /how-to/aiml-runtime-onboard/

- title: AI-DR (Azure Setup)
  image: ./icons/model-safety.svg
  url: /how-to/azure-aidr/

::/cards::

## Supported Platforms and Use Cases

!!! note "Useful Links"
    - For list of supported platforms refer to AccuKnox's [**AI Security Support Matrix**](https://help.accuknox.com/support-matrix/aiml-support-matrix/)
    - For use cases refer to the [**AI Security Use Cases**](https://help.accuknox.com/use-cases/aiml-usecases/)

## Featured Videos

<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; margin: auto; font-family: Arial, sans-serif;">

  <!-- AI Copilot -->
  <div style="background:#fff; border-radius:12px; box-shadow:0 2px 8px rgba(0,0,0,0.06); overflow:hidden;">
    <div style="aspect-ratio:16/9;">
      <iframe width="100%" height="100%" src="https://www.youtube.com/embed/OJLkKghtEpQ" title="AI Copilot" frameborder="0" allowfullscreen style="border:0;"></iframe>
    </div>
    <div style="padding:8px;">
      <h4 style="margin:0 0 4px; display:flex; align-items:center; gap:6px;">
        AI Copilot
      </h4>
      <p style="margin:0; font-size:0.75rem; color:#555;">Enhance security operations with AI-driven insights, automated threat detection, and response recommendations.</p>
    </div>
  </div>

  <!-- AI Compliance -->
  <div style="background:#fff; border-radius:12px; box-shadow:0 2px 8px rgba(0,0,0,0.06); overflow:hidden;">
    <div style="aspect-ratio:16/9;">
      <iframe width="100%" height="100%" src="https://www.youtube.com/embed/rMc-fV5kzvs" title="AI Compliance" frameborder="0" allowfullscreen style="border:0;"></iframe>
    </div>
    <div style="padding:8px;">
      <h4 style="margin:0 0 4px; display:flex; align-items:center; gap:6px;">
        AI Compliance
      </h4>
      <p style="margin:0; font-size:0.75rem; color:#555;">Automate policy checks and ensure AI systems align with standards like EU AI Act, NIST, and ISO 42001.</p>
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

  <!-- Securing AI Factories -->
  <div style="background:#fff; border-radius:12px; box-shadow:0 2px 8px rgba(0,0,0,0.06); overflow:hidden;">
    <div style="aspect-ratio:16/9;">
      <iframe width="100%" height="100%" src="https://www.youtube.com/embed/HzJQKl-YPAo" title="Securing AI Factories" frameborder="0" allowfullscreen style="border:0;"></iframe>
    </div>
    <div style="padding:8px;">
      <h4 style="margin:0 0 4px; display:flex; align-items:center; gap:6px;">
        Securing AI Factories
      </h4>
      <p style="margin:0; font-size:0.75rem; color:#555;">Implement end-to-end security for AI pipelines—from data ingestion to model deployment.</p>
    </div>
  </div>

</div>

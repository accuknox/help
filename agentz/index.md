---
title: AgentZ
description: AgentZ is a zero trust runtime for AI agents from AccuKnox. Every agent runs in a default deny sandbox, never holds a secret, and writes every action to a replayable trace.
hide:
  - navigation
  - toc
---

<div class="ak-no-copy-page" hidden></div>

<div class="az-page" markdown="1">

# AgentZ

<div class="az-hero">
  <div class="az-hero__top">
    <img class="az-hero__mark off-glb" src="../assets/images/agentz-logo.svg" alt="AgentZ logo">
    <span class="az-hero__name">AgentZ</span>
    <span class="az-hero__say">Say it "agent zee"</span>
  </div>
  <p class="az-hero__tagline">A zero trust runtime for AI agents.</p>
  <p class="az-hero__sub">Every agent runs in a default deny sandbox, holds no secret, and writes every action to a trace you can replay. Open source, and free to start.</p>
  <div class="az-cta">
    <a class="az-btn az-btn--solid" href="https://agentzharness.ai/" target="_blank" rel="noopener">Start free</a>
    <a class="az-btn az-btn--ghost" href="https://github.com/accuknox/agentZ" target="_blank" rel="noopener">
      <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 .3a12 12 0 0 0-3.8 23.4c.6.1.8-.3.8-.7v-2.6c-3.3.7-4-1.6-4-1.6-.6-1.4-1.4-1.8-1.4-1.8-1.1-.8.1-.8.1-.8 1.2.1 1.9 1.2 1.9 1.2 1 1.8 2.8 1.3 3.5 1a2.7 2.7 0 0 1 .8-1.6c-2.7-.3-5.5-1.3-5.5-6 0-1.2.5-2.3 1.2-3.1-.1-.3-.5-1.5.1-3.2 0 0 1-.3 3.3 1.2a11.5 11.5 0 0 1 6 0C17.3 4.2 18.3 4.5 18.3 4.5c.6 1.7.2 2.9.1 3.2a4.5 4.5 0 0 1 1.2 3.1c0 4.7-2.8 5.7-5.5 6 .4.4.8 1.1.8 2.3v3.3c0 .4.2.8.8.7A12 12 0 0 0 12 .3Z"/></svg>
      Star the repo
    </a>
    <a class="az-btn az-btn--ghost" href="https://www.youtube.com/watch?v=mAzLWcr59g0" target="_blank" rel="noopener">
      <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>
      Watch the demo
    </a>
    <a class="az-btn az-btn--ghost" href="https://docs.agentzharness.ai/" target="_blank" rel="noopener">AgentZ docs</a>
    <a class="az-btn az-btn--ghost" href="https://accuknox.com/platform/agentz/" target="_blank" rel="noopener">Product page</a>
  </div>
</div>

AgentZ is the AccuKnox platform for production AI agents. Describe a job in a sentence, and AgentZ writes the skill and wires the steps. The agent then runs from chat, an API, the CLI, or a cron.

**Zero trust** means the agent gets no access until a policy grants it. **Default deny** means every network call and tool call is blocked until you allow it. The policy runs at the kernel, next to the agent, so nothing leaves the sandbox without a record.

Full product documentation lives at [docs.agentzharness.ai](https://docs.agentzharness.ai/).

## Four steps

<div class="az-grid az-grid--4">
  <div class="az-card">
    <span class="az-card__step">01</span>
    <p class="az-card__title">Build</p>
    <p class="az-card__body">Describe the job. AgentZ writes the skill and wires the steps.</p>
  </div>
  <div class="az-card">
    <span class="az-card__step">02</span>
    <p class="az-card__title">Run</p>
    <p class="az-card__body">Chat, API, or CLI. Any framework, and no redeploy.</p>
  </div>
  <div class="az-card">
    <span class="az-card__step">03</span>
    <p class="az-card__title">Automate</p>
    <p class="az-card__body">Trigger on a cron, an event, or an API call. Skills chain.</p>
  </div>
  <div class="az-card">
    <span class="az-card__step">04</span>
    <p class="az-card__title">Govern</p>
    <p class="az-card__body">The kernel checks every call. The trace records the result.</p>
  </div>
</div>

## One control plane

<div class="az-grid az-grid--3">
  <div class="az-card">
    <p class="az-card__title">Skills</p>
    <p class="az-card__body">Reusable, versioned building blocks.</p>
  </div>
  <div class="az-card">
    <p class="az-card__title">Workflows</p>
    <p class="az-card__body">Chain steps, schedule them, hand off work.</p>
  </div>
  <div class="az-card">
    <p class="az-card__title">Context</p>
    <p class="az-card__body">Shared memory, files, and knowledge.</p>
  </div>
  <div class="az-card">
    <p class="az-card__title">Teams</p>
    <p class="az-card__body">Roles, ownership, and a shared scope.</p>
  </div>
  <div class="az-card">
    <p class="az-card__title">Guardrails</p>
    <p class="az-card__body">No standing access to any tool or credential.</p>
  </div>
  <div class="az-card">
    <p class="az-card__title">Audit</p>
    <p class="az-card__body">Every step recorded, span by span, and replayable.</p>
  </div>
</div>

## The zero trust part

<div class="az-grid az-grid--3">
  <div class="az-card">
    <p class="az-card__title">Sandboxed on run one</p>
    <p class="az-card__body">Isolation is not a setting you turn on later.</p>
  </div>
  <div class="az-card">
    <p class="az-card__title">No secret in the agent</p>
    <p class="az-card__body">Credentials are scoped and injected at run time. An injection cannot leak what the agent never sees.</p>
  </div>
  <div class="az-card">
    <p class="az-card__title">Egress control at the kernel</p>
    <p class="az-card__body">Allow or block by domain, port, and protocol.</p>
  </div>
  <div class="az-card">
    <p class="az-card__title">Permission per action</p>
    <p class="az-card__body">Read and scan pass. Mutate, push, and delete are denied by default.</p>
  </div>
  <div class="az-card">
    <p class="az-card__title">Roles gate tool calls</p>
    <p class="az-card__body">Fine grained RBAC covers each agent action.</p>
  </div>
  <div class="az-card">
    <p class="az-card__title">On-premises and air-gapped</p>
    <p class="az-card__body">Logs and audit evidence stay on your infrastructure.</p>
  </div>
</div>

## Nine screens

<div class="az-shots">
  <div class="az-shot"><img src="../assets/images/agentz/slide-02.webp" alt="Model picker listing GLM, Claude, Gemini, Kimi and GPT models available to an agent"></div>
  <div class="az-shot"><img src="../assets/images/agentz/slide-03.webp" alt="Sandbox update screen with per-tool toggles for each connected MCP server"></div>
  <div class="az-shot"><img src="../assets/images/agentz/slide-04.webp" alt="MCP connection form with Slack, GitHub, Notion, Linear, Asana, Figma and Atlassian servers"></div>
  <div class="az-shot"><img src="../assets/images/agentz/slide-05.webp" alt="A cloud asset count diff report generated by an agent, next to its output files"></div>
  <div class="az-shot"><img src="../assets/images/agentz/slide-06.webp" alt="Schedule editor with a cron expression, timeout and run history limits"></div>
  <div class="az-shot"><img src="../assets/images/agentz/slide-07.webp" alt="Workflow run graph with a step inspector showing status, timings and instructions"></div>
  <div class="az-shot"><img src="../assets/images/agentz/slide-08.webp" alt="Span list with model calls, bash and webfetch, and a token breakdown for one call"></div>
  <div class="az-shot"><img src="../assets/images/agentz/slide-09.webp" alt="Graph of MCP tools called by an agent, with latency and last-used age per tool"></div>
  <div class="az-shot"><img src="../assets/images/agentz/slide-10.webp" alt="AgentZ closing slide with the SOC 2, CNCF, AWS and Nutanix certifications"></div>
</div>

## Your stack, your model

Credentials, scopes, and policy live on AgentZ instead of on the agent. Run a frontier API or a self-hosted open weight model on your own key, and switch models without rewiring anything.

<div class="az-logos">
  <div class="az-logo"><img class="off-glb" src="../assets/images/agentz/openai.svg" alt="OpenAI"><span>OpenAI</span></div>
  <div class="az-logo"><img class="off-glb" src="../assets/images/agentz/anthropic.svg" alt="Anthropic"><span>Anthropic</span></div>
  <div class="az-logo"><img class="off-glb" src="../assets/images/agentz/gemini.svg" alt="Google Gemini"><span>Gemini</span></div>
  <div class="az-logo"><img class="off-glb" src="../assets/images/agentz/aws.svg" alt="Amazon Web Services"><span>AWS</span></div>
  <div class="az-logo"><img class="off-glb" src="../assets/images/agentz/microsoft.svg" alt="Microsoft Azure"><span>Azure</span></div>
  <div class="az-logo"><img class="off-glb" src="../assets/images/agentz/opensource.svg" alt="Open source models"><span>Open weight</span></div>
</div>

Connectors ship for Slack, Gmail, Microsoft 365, Google Workspace, Jira, Confluence, Notion, GitHub, GitLab, and Bitbucket. Any MCP server works after you authorize it once.

</div>

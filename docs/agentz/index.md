---
title: AgentZ
description: AgentZ is a zero trust runtime for AI agents from AccuKnox. Every agent runs in a default deny sandbox, never holds a secret, and writes every action to a replayable trace.
---

<div class="az-hero" markdown="1">

<div class="az-hero__top">
  <img class="az-hero__mark off-glb" src="../assets/images/agentz-logo.svg" alt="AgentZ logo">
  <h1 class="az-hero__name">AgentZ</h1>
  <span class="az-hero__say">Say it "agent zee"</span>
</div>

<p class="az-hero__tagline">A zero trust runtime for AI agents.</p>

<p class="az-hero__sub">Every agent runs in a default deny sandbox. It never holds a secret. Every model call and every tool call lands in a trace you can replay. AgentZ is open source, and free to start.</p>

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
  <a class="az-btn az-btn--ghost" href="https://docs.agentzharness.ai/" target="_blank" rel="noopener">Read the AgentZ docs</a>
  <a class="az-btn az-btn--ghost" href="https://accuknox.com/platform/agentz/" target="_blank" rel="noopener">Product page</a>
</div>

</div>

## What AgentZ is

AgentZ is the AccuKnox platform for production AI agents. You describe a job in one sentence, and AgentZ writes the skill and wires the steps. The agent then runs from chat, an API call, the CLI, or a cron schedule.

The security model is the reason it exists. **Zero trust** means the agent gets no access until a policy grants it. **Default deny** means every network call, file read, and tool call is blocked until you allow it. The policy runs at the kernel, local to the agent, so nothing leaves the sandbox without a record.

AgentZ keeps its own documentation at [docs.agentzharness.ai](https://docs.agentzharness.ai/). This page is the short version for AccuKnox customers.

## Build, run, automate, govern

<div class="az-grid">
  <div class="az-card">
    <span class="az-card__step">01</span>
    <p class="az-card__title">Build</p>
    <p class="az-card__body">Describe the job in a sentence. AgentZ writes the skill and wires every step for you.</p>
  </div>
  <div class="az-card">
    <span class="az-card__step">02</span>
    <p class="az-card__title">Run</p>
    <p class="az-card__body">Start the agent from chat, an API, or the CLI. Any framework works, and no redeploy is needed.</p>
  </div>
  <div class="az-card">
    <span class="az-card__step">03</span>
    <p class="az-card__title">Automate</p>
    <p class="az-card__body">Trigger on a cron, an event, or an API call. Skills chain in sequence or in parallel.</p>
  </div>
  <div class="az-card">
    <span class="az-card__step">04</span>
    <p class="az-card__title">Govern</p>
    <p class="az-card__body">Policy resolves at the edge, the kernel checks it, and the trace records the result.</p>
  </div>
</div>

## One control plane for every agent, model, and team

<div class="az-grid">
  <div class="az-card">
    <p class="az-card__title">Skills</p>
    <p class="az-card__body">Reusable, versioned building blocks that the whole team can call.</p>
  </div>
  <div class="az-card">
    <p class="az-card__title">Workflows</p>
    <p class="az-card__body">Chain steps, set a schedule, and hand work from one agent to the next.</p>
  </div>
  <div class="az-card">
    <p class="az-card__title">Context</p>
    <p class="az-card__body">Shared memory, files, and knowledge that stay with the agent between runs.</p>
  </div>
  <div class="az-card">
    <p class="az-card__title">Teams</p>
    <p class="az-card__body">Roles, ownership, and a shared scope, so an agent belongs to a team and not to one laptop.</p>
  </div>
  <div class="az-card">
    <p class="az-card__title">Guardrails</p>
    <p class="az-card__body">Secure by default, with no standing access to any tool or any credential.</p>
  </div>
  <div class="az-card">
    <p class="az-card__title">Audit</p>
    <p class="az-card__body">Every step is recorded span by span, and you can replay the whole run.</p>
  </div>
</div>

## How the zero trust part works

<div class="az-grid">
  <div class="az-card">
    <p class="az-card__title">Default deny sandbox</p>
    <p class="az-card__body">Isolation is not a setting you turn on later. The first run is already sandboxed.</p>
  </div>
  <div class="az-card">
    <p class="az-card__title">No secret in the agent</p>
    <p class="az-card__body">AgentZ injects a scoped credential at run time. A prompt injection cannot leak what the agent never receives.</p>
  </div>
  <div class="az-card">
    <p class="az-card__title">Egress control at the kernel</p>
    <p class="az-card__body">You allow or block traffic by domain, port, and protocol. Every allow and every block lands in the trace.</p>
  </div>
  <div class="az-card">
    <p class="az-card__title">Permission per action</p>
    <p class="az-card__body">Read and scan pass. Mutate, push, and delete are denied by default, so a lookup cannot become a teardown.</p>
  </div>
  <div class="az-card">
    <p class="az-card__title">Roles that gate tool calls</p>
    <p class="az-card__body">Fine grained RBAC covers each agent action. An admin provisions access on behalf of the team.</p>
  </div>
  <div class="az-card">
    <p class="az-card__title">On-premises and air-gapped</p>
    <p class="az-card__body">Logs, traces, and audit evidence stay on your own infrastructure. AgentZ makes no outbound call.</p>
  </div>
</div>

## Screens from the platform

Click any screenshot to open it full size.

<div class="az-shots">
  <div class="az-shot">
    <img src="../assets/images/agentz/screen-02.webp" alt="Model picker listing GLM, Claude, Gemini, Kimi and GPT models available to an agent">
    <div class="az-shot__caption">Any model, in a sandbox with memory</div>
  </div>
  <div class="az-shot">
    <img src="../assets/images/agentz/screen-03.webp" alt="Sandbox update screen with per-tool toggles for each connected MCP server">
    <div class="az-shot__caption">Fine grained sandbox permissions</div>
  </div>
  <div class="az-shot">
    <img src="../assets/images/agentz/screen-04.webp" alt="MCP connection form with Slack, GitHub, Notion, Linear, Asana, Figma and Atlassian servers">
    <div class="az-shot__caption">MCP server support out of the box</div>
  </div>
  <div class="az-shot">
    <img src="../assets/images/agentz/screen-06.webp" alt="Schedule editor with a cron expression, timeout and run history limits">
    <div class="az-shot__caption">Crons and schedules, edited in place</div>
  </div>
  <div class="az-shot">
    <img src="../assets/images/agentz/screen-07.webp" alt="Workflow run graph with a step inspector showing status, timings and instructions">
    <div class="az-shot__caption">A live workflow graph</div>
  </div>
  <div class="az-shot">
    <img src="../assets/images/agentz/screen-08.webp" alt="Span list with model calls, bash and webfetch, and a token breakdown for one call">
    <div class="az-shot__caption">Logs and traces, span by span</div>
  </div>
</div>

## Works with the stack you already run

Run an agent on a frontier API or on a self-hosted open weight model, with your own key. Credentials, scopes, and tenant policy live on AgentZ instead of on the agent. When a stronger model ships, you switch without rewiring anything.

<div class="az-logos">
  <div class="az-logo"><img class="off-glb" src="../assets/images/agentz/openai.svg" alt="OpenAI"><span>OpenAI</span></div>
  <div class="az-logo"><img class="off-glb" src="../assets/images/agentz/anthropic.svg" alt="Anthropic"><span>Anthropic</span></div>
  <div class="az-logo"><img class="off-glb" src="../assets/images/agentz/gemini.svg" alt="Google Gemini"><span>Google Gemini</span></div>
  <div class="az-logo"><img class="off-glb" src="../assets/images/agentz/aws.svg" alt="Amazon Web Services"><span>AWS</span></div>
  <div class="az-logo"><img class="off-glb" src="../assets/images/agentz/microsoft.svg" alt="Microsoft Azure"><span>Microsoft Azure</span></div>
  <div class="az-logo"><img class="off-glb" src="../assets/images/agentz/opensource.svg" alt="Open source models"><span>Open weight models</span></div>
</div>

Tool and data connections go through the same policy edge. AgentZ ships connectors for Slack, Gmail, Microsoft 365, Google Workspace, Jira, Confluence, Notion, GitHub, GitLab, and Bitbucket. Any MCP server works after you authorize it once.

## Free and Enterprise

Free is the evaluation tier. You can build and run a real agent before you talk to anyone.

<div class="az-plans" markdown="1">

| | Free | Enterprise |
|---|---|---|
| **Price** | $0 per month | Priced on what you run |
| **Users** | 2 users | Sized to your organization |
| **Workspaces** | 1 | Unlimited |
| **Sign-in** | GitHub, Google, Microsoft | Adds SAML and OIDC |
| **Model** | Your own subscription or key | Adds your own private model |
| **Compute** | One small agent, 1 vCPU and 1 GB RAM | Sized to your workload |
| **Prompt guardrails** | Platform defaults | Custom guardrails for your domain |
| **Hosting** | SaaS | SaaS, on-premises, or self-deployed |
| **Data residency** | Shared and multi-tenant | Sandboxed inside your network |
| **Support** | Docs and community | A named contact |
| **Best for** | A fast rollout in a smaller team | A regulated or security-sensitive organization |

</div>

## Where to go next

<div class="az-grid">
  <a class="az-card az-card--link" href="https://agentzharness.ai/" target="_blank" rel="noopener">
    <p class="az-card__title">Start free</p>
    <p class="az-card__body">Sign in with GitHub, Google, or Microsoft, and run your first agent.</p>
  </a>
  <a class="az-card az-card--link" href="https://docs.agentzharness.ai/" target="_blank" rel="noopener">
    <p class="az-card__title">AgentZ documentation</p>
    <p class="az-card__body">Installation, skills, workflows, policy, and the API reference.</p>
  </a>
  <a class="az-card az-card--link" href="https://github.com/accuknox/agentZ" target="_blank" rel="noopener">
    <p class="az-card__title">Source on GitHub</p>
    <p class="az-card__body">Read the code, file an issue, and star the repository.</p>
  </a>
  <a class="az-card az-card--link" href="https://www.youtube.com/watch?v=mAzLWcr59g0" target="_blank" rel="noopener">
    <p class="az-card__title">Watch the demo</p>
    <p class="az-card__body">See a full run, from one prompt to a finished task.</p>
  </a>
  <a class="az-card az-card--link" href="https://accuknox.com/platform/agentz/" target="_blank" rel="noopener">
    <p class="az-card__title">Product page</p>
    <p class="az-card__body">Pricing, the capability comparison, and the answers to common questions.</p>
  </a>
  <a class="az-card az-card--link" href="https://www.accuknox.com/contact-us" target="_blank" rel="noopener">
    <p class="az-card__title">Talk to AccuKnox</p>
    <p class="az-card__body">Book a walkthrough for your team and your stack.</p>
  </a>
</div>

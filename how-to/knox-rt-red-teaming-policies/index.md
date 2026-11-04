---
title: Knox RT Red Teaming Policies (Beta)
description: Build, schedule and review AI red teaming policies with Knox RT (AccuKnox Red Teaming). Pick a template such as OWASP LLM Top 10, tune attack strategies, attach models and agents, and read results mapped to OWASP and MITRE ATLAS.
---

# Knox RT Red Teaming Policies (Beta)

!!! info "Beta"
    Red Teaming Policies is in beta. The screens on this page come from the design preview and can change before release.

Knox RT (AccuKnox Red Teaming) tests your AI models and agents with a **red teaming policy**. A policy holds the template, the prompts, the attack strategies, the targets and the schedule. You build it once, then run it on demand or on a cron.

<iframe width="100%" height="420" src="https://www.youtube.com/embed/wC3_Fac65Mg" title="Knox RT Red Teaming Policies product tour" frameborder="0" allowfullscreen></iframe>

## Every Policy Sits in One List

Open **Red Teaming Policies**. Each row shows the models and agents it targets, its category and plugin coverage, and its findings by severity.

![Red Teaming Policies list with the tabs, Create Policy button, coverage and findings columns](images/knox-rt/knox-rt-01-policy-list.png)

- Tabs split the list into **All**, **Models** and **Agents**.
- **Filter** narrows the list by model, agent or category. **Saved Filter** brings back a view in one click.
- **System** policies ship with AccuKnox. **User** policies are the ones your team builds.

## Build a Policy in Four Steps

Click **Create Policy**. The drawer walks you through four steps.

### 1. Policy Configuration

Name the policy and pick a starting point.

- **Predefined Template** starts from an AccuKnox template.
- **Create New Template** starts from the categories you pick. See [Build your own template](#build-your-own-template).

### 2. Modules and Plugins

Pick a template. Each card shows its module and plugin count.

![Template cards and the three prompt sources in step 2](images/knox-rt/knox-rt-02-template.png)

| Template | What it covers |
|---|---|
| OWASP LLM Top 10 | The OWASP Top 10 risks for LLM applications |
| EU AI Act Readiness | Risks relevant to EU AI Act conformity assessments |
| Harmful Content & Safety | Harmful, criminal and biased output across personas |
| Deep Adversarial | Multi-turn, iterative attacks on guardrails and agents |
| Privacy & Access | Personal data disclosure and authorization bypass |
| Baseline Coverage | Every category at low depth |

Then pick a prompt source.

- **Default Prompts** uses the prompt library for each module. You change only severity and which plugins run.
- **Customize Default Prompts** lets you set test counts, language and per-module overrides.
- **Upload your custom prompts** takes your own prompt set as CSV, JSON or YAML.

Turn modules on or off, then pick the **Attack Strategies**.

![Attack strategies with base64, jailbreak, fiction and multi-turn crescendo](images/knox-rt/knox-rt-03-strategies.png)

**Crescendo** is a multi-turn strategy. It escalates over several turns, the way a patient attacker does. Click the gear icon to set its turn limits.

### 3. Review Configuration

Check the policy summary, the generated prompts and the policy YAML before you save.

### 4. Targets and Schedule

![Targets and Schedule step with the model and agent pickers and the cron fields](images/knox-rt/knox-rt-04-targets-schedule.png)

1. Pick **Target Models** and **Target Agents**. Targets are optional. You can save now and attach them later from the policy details.
2. Pick **On-demand**, or **Scheduled** and fill in the cron fields. The drawer shows the next run in server time (UTC) and in your time zone.
3. Click **Save Policy**.

## Build Your Own Template

**Create New Template** builds a template from the categories you pick, with prompts generated for each plugin.

- **Plugin override.** Give any plugin its own instructions, attack strategies and multi-turn limits.
- **Custom plugin.** Add a plugin with its own objective that fits your app, such as "bypass the refund limit".

## Edit, Clone and Delete Policies

Open the row menu on any policy.

| Action | What it does |
|---|---|
| Edit | Changes the policy. The name and method stay locked, because run history and findings link to them. |
| Clone | Copies the policy under a new name. |
| Delete | Removes the policy and its schedule. Findings from earlier runs stay in Findings. |

Select several rows to clone or delete them together.

## One Drawer Holds Every Result

Click a policy name to open its detail drawer.

![Policy detail drawer with tabs, run results and the run, edit, clone and delete icons](images/knox-rt/knox-rt-05-policy-detail.png)

| Tab | What you see |
|---|---|
| Overview | Attack success rate, pass rate, test cases, average duration, schedule, targets, strategies and coverage by category |
| Findings | Each failed attack, with its category, severity, model and time |
| Runs | The findings trend across runs, and each run's status |
| Audit Trail | Every change to the policy and who made it |
| YAML | The policy as YAML, to copy or download |

## Results Land in AccuKnox Findings

Go to **Issues > Findings** and pick **AI Red Teaming Findings**. Each row holds the attack prompt, the model output, the strategy and the reason it failed.

![AI Red Teaming Findings list with the attack prompt, output, strategy and reason columns](images/knox-rt/knox-rt-06-findings.png)

Findings map to the OWASP Top 10 for LLM and MITRE ATLAS. Rules, tickets and exports work the same as for any other finding.

!!! tip "Start with a template, then narrow it"
    Run **Baseline Coverage** first to see where a model fails. Then build a focused policy, such as **Deep Adversarial**, for the categories that failed.

!!! note "Related pages"
    - [AI Red Teaming](../use-cases/red-teaming.md) explains the attack categories and how red teaming fits AI security.
    - [Custom Model Red Teaming](aiml-custom-model-redteaming.md) connects a model on Bedrock, NVIDIA Triton or vLLM.
    - [Categories and Probes](../use-cases/subprompts-categories.md) lists every category and probe.

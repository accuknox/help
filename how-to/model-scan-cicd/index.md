---
title: Gate Model Adoption on a Pull Request
description: Wire the AccuKnox pre-deployment model scan into CI/CD so a public model reaches your registry only after a sandboxed scan and a SecOps approval on the pull request.
---

# Gate Model Adoption on a Pull Request

A developer finds a model on Hugging Face. Nothing stops it reaching production except somebody remembering to check it.

Wiring the [pre-deployment model scan](ml-static-scan.md) into a pull request attaches the report to the review and makes the merge the approval. It works for any public source: Hugging Face, AWS Bedrock, or an on-premises store.

## Prerequisites

- An AccuKnox token with permission to run scans. See [How to Create Tokens](how-to-create-tokens.md).
- A Git repository where model adoption is proposed by a pull request rather than by direct commit.
- An ML static scan collector already configured. See [ML Model Static Scans](ml-static-scan.md).

## What the Gate Does

<div class="ak-dia" role="img" aria-label="Six-step flow. An AI developer raises a pull request naming a model, SecOps comments slash scan, the CI workflow calls the AccuKnox scan job, AccuKnox scans the model in its sandbox evaluator, the report is posted back to the pull request, and SecOps approves or rejects before merge.">
<svg viewBox="0 0 900 446" xmlns="http://www.w3.org/2000/svg">
  <g class="ln-dash">
    <path d="M236 96 V106"/><path d="M236 162 V172"/><path d="M236 228 V238"/>
    <path d="M236 294 V304"/><path d="M236 360 V370"/>
  </g>

  <text class="t-s" x="16" y="74">AI developer</text>
  <rect class="p" x="210" y="40" width="674" height="56" rx="8"/>
  <circle class="step" cx="236" cy="68" r="13"/>
  <text class="t-step" x="236" y="72" text-anchor="middle">1</text>
  <text class="t-h" x="262" y="64">Raise a pull request that names the model</text>
  <text class="t-s" x="262" y="82">Model name, model link, and provider. No model file is committed.</text>

  <text class="t-s" x="16" y="140">SecOps</text>
  <rect class="p" x="210" y="106" width="674" height="56" rx="8"/>
  <circle class="step" cx="236" cy="134" r="13"/>
  <text class="t-step" x="236" y="138" text-anchor="middle">2</text>
  <text class="t-h" x="262" y="130">Comment /scan on the pull request</text>
  <text class="t-s" x="262" y="148">The comment is the trigger. A pull request with no comment runs no scan.</text>

  <text class="t-s" x="16" y="206">CI workflow</text>
  <rect class="p" x="210" y="172" width="674" height="56" rx="8"/>
  <circle class="step" cx="236" cy="200" r="13"/>
  <text class="t-step" x="236" y="204" text-anchor="middle">3</text>
  <text class="t-h" x="262" y="196">Call the AccuKnox scan job</text>
  <text class="t-s" x="262" y="214">The workflow passes the model name, link and provider to the control plane.</text>

  <text class="t-s" x="16" y="272">AccuKnox</text>
  <rect class="acc" x="210" y="238" width="674" height="56" rx="8"/>
  <circle class="step" cx="236" cy="266" r="13"/>
  <text class="t-step" x="236" y="270" text-anchor="middle">4</text>
  <text class="t-h" x="262" y="262">Scan the model inside the sandbox evaluator</text>
  <text class="t-s" x="262" y="280">AccuKnox pulls the model into its own sandbox. It never runs on your network.</text>

  <text class="t-s" x="16" y="338">AccuKnox</text>
  <rect class="acc" x="210" y="304" width="674" height="56" rx="8"/>
  <circle class="step" cx="236" cy="332" r="13"/>
  <text class="t-step" x="236" y="336" text-anchor="middle">5</text>
  <text class="t-h" x="262" y="328">Post the report back to the pull request</text>
  <text class="t-s" x="262" y="346">Findings land in review context, beside the change that proposed the model.</text>

  <text class="t-s" x="16" y="404">SecOps</text>
  <rect class="good" x="210" y="370" width="674" height="56" rx="8"/>
  <circle class="step" cx="236" cy="398" r="13"/>
  <text class="t-step" x="236" y="402" text-anchor="middle">6</text>
  <text class="t-h" x="262" y="394">Approve or reject, then merge</text>
  <text class="t-s" x="262" y="412">A merge pushes the model to your registry. A rejection leaves the registry untouched.</text>
</svg>
</div>

The registry push is downstream of the merge. A developer who skips the scan has an unmerged pull request and no model in the registry.

## Step 1. Propose the Model in a Pull Request

Have the developer open a pull request that records three fields and no model weights:

```yaml
model:
  name: acme-model
  link: https://huggingface.co/acme/acme-model
  provider: huggingface
```

Keep the weights out of the repository. The scan reads the model from its source, so a committed artifact adds review burden and proves nothing about what the source serves today.

## Step 2. Trigger the Scan From a Pull Request Comment

Add a workflow that listens for the `/scan` comment and calls the AccuKnox scan job. Copy the trigger and the permissions block:

{% raw %}
```yaml
name: AccuKnox Model Scan

on:
  issue_comment:
    types: [created]

jobs:
  model-scan:
    if: github.event.issue.pull_request && contains(github.event.comment.body, '/scan')
    runs-on: ubuntu-latest
    permissions:
      pull-requests: write
      contents: read
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Run AccuKnox model scan
        uses: ""  # fill in the published AccuKnox model-scan action reference
        with:
          token: ${{ secrets.ACCUKNOX_TOKEN }}
          endpoint: ${{ secrets.ACCUKNOX_ENDPOINT }}
          label: ${{ secrets.ACCUKNOX_LABEL }}
```
{% endraw %}

!!! warning "One value is deliberately blank"
    The `uses:` line ships empty. Confirm the published action name and version with AccuKnox support, fill it in, and only then commit this workflow. Every other line follows the same secret names as the [AccuKnox container scan action](../integrations/github-container-scan.md).

Store `ACCUKNOX_TOKEN`, `ACCUKNOX_ENDPOINT` and `ACCUKNOX_LABEL` as repository secrets. See [How to Create Tokens](how-to-create-tokens.md) for the token.

## Step 3. Review the Scan Report

The report covers four areas. A finding is a reason to ask a question, not an automatic block. A permissive license or a missing model card is a business decision, not a defect.

| Area | What a finding means |
|---|---|
| Supply chain and provenance | The author, country of origin, training-dataset disclosure or license is missing or unexpected |
| Adversarial robustness | The publisher disclosed no robustness or bias evaluation for the model |
| Data and privacy risks | The model card discloses PII, or the model shows elevated membership inference risk |
| Model file security | The artifact uses an unsafe format, carries an unsafe pickle, or embeds scripts in its config files |

Treat a model file security finding as blocking. An unsafe pickle executes on load, so the code runs before any of your controls see the model. See [Pickle Code Injection](../use-cases/modelarmor-pickle-code.md) for a working demonstration.

## Step 4. Re-Scan on Every Version Bump

A verdict applies only to the artifact that existed when the scan ran. An upstream publisher can push a new revision under the same model name.

- Pin the revision in the pull request.
- Open a new pull request when the revision changes.

A model approved once and pulled by a moving tag is not a gated model.

## Known Limits

- **It does not scan at inference time.** A model that clears the gate and is later swapped on disk is caught by [ModelArmor](../use-cases/modelarmor.md) at runtime, not here.
- **It does not test model behavior.** Jailbreak and prompt-injection resistance come from [AI Red Teaming](../use-cases/red-teaming.md), which runs against a deployed endpoint.
- **It does not enforce the merge rule.** Configure branch protection so the registry push cannot run on an unmerged branch.

## Related Pages

- [ML Model Static Scans](ml-static-scan.md), the console click-path for the same scan
- [AI security architecture](../getting-started/ai-security-arch.md), where this gate sits in the wider flow
- [CI/CD integrations](../integrations/cicd-overview.md), the other AccuKnox pipeline scanners

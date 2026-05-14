---
title: Generate xBOM via GitHub Actions (xBOM Scan Action)
description: Use the AccuKnox xBOM Scan Action to generate SBOM, CBOM, and AIBOM from source code, container images, or AI/ML model sources in GitHub Actions.
---

# Generate xBOM via GitHub Actions

The **AccuKnox xBOM Scan Action** (`accuknox/xbom-action`) integrates into your GitHub workflow to scan source code, container images, Go projects, or AI/ML models and generate CycloneDX 1.6 BOMs (SBOM, CBOM, AIBOM), upload results to AccuKnox SaaS, and save the BOM as a downloadable GitHub Actions artefact.

[![GitHub Marketplace](https://img.shields.io/badge/Marketplace-AccuKnox%20xBOM%20Scan-blue?logo=github)](https://github.com/marketplace/actions/accuknox-xbom-scan)
[![knoxctl](https://img.shields.io/badge/powered%20by-knoxctl%20v0.10.0-orange)](https://github.com/accuknox/accuknox-cli-v2)

## Supported BOM Types

| Type | Tool | Source | Use Case |
|---|---|---|---|
| `sbom` | `knoxctl pkgscan` | Filesystem or container image | Packages, libraries, dependencies |
| `cbom` | `knoxctl cbom` | Go source or container image | Crypto algorithms, certs, protocols |
| `aibom` | `knoxctl aibom` | HuggingFace model or AWS Bedrock | AI/ML model inventory |

---

## Prerequisites

### GitHub Secrets

Add the following under **Settings → Secrets and variables → Actions**.

**Required (all BOM types):**

| Secret | Description |
|---|---|
| `ACCUKNOX_TOKEN` | AccuKnox API token. [How to create](https://help.accuknox.com/how-to/how-to-create-tokens/) |
| `ACCUKNOX_ENDPOINT` | AccuKnox endpoint, e.g. `cspm.accuknox.com` |
| `ACCUKNOX_LABEL` | AccuKnox label. [How to create](https://help.accuknox.com/how-to/how-to-create-labels/) |

**Required for AIBOM Bedrock only:**

| Secret | Description |
|---|---|
| `AWS_ACCESS_KEY_ID` | AWS access key with `bedrock:ListFoundationModels` permission |
| `AWS_SECRET_ACCESS_KEY` | Matching AWS secret access key |

### AccuKnox Project

An AccuKnox project must exist before running the workflow — see [Common Prerequisites](xbom-setup.md#common-prerequisites).

!!! note
    The **Project Name** and **Project Classifier** must exactly match the `project-name` and `project-classifier` values in your workflow YAML.

---

## Usage

### SBOM from Filesystem

Scans the repository source tree for packages and dependencies.

{% raw %}
```yaml
- uses: accuknox/xbom-action@2.0
  with:
    bom-type:           sbom
    path:               "."
    token:              ${{ secrets.ACCUKNOX_TOKEN }}
    endpoint:           ${{ secrets.ACCUKNOX_ENDPOINT }}
    label:              ${{ secrets.ACCUKNOX_LABEL }}
    project-name:       my-project
    project-classifier: application
```
{% endraw %}

#### Inputs

| Name | Description | Possible Options | Required |
|---|---|---|---|
| `bom-type` | Type of BOM to generate | `sbom` | **Yes** |
| `path` | Directory to scan | Any valid directory path | No (default: `.`) |
| `token` | AccuKnox API token | — | **Yes** |
| `endpoint` | AccuKnox SaaS hostname | Hostname only, no `https://` | **Yes** |
| `label` | AccuKnox label | — | **Yes** |
| `project-name` | AccuKnox project name | Any string | **Yes** |
| `project-classifier` | CycloneDX classifier | `application`, `firmware`, `library` | **Yes** |

---

### SBOM from Container Image

Scans a built container image for installed packages. Build the image in the same job; the action only needs the tag.

{% raw %}
```yaml
- name: Build image
  id: build
  run: |
    IMAGE="myapp:${{ github.sha }}"
    docker build -t "$IMAGE" .
    echo "image=${IMAGE}" >> "$GITHUB_OUTPUT"

- uses: accuknox/xbom-action@2.0
  with:
    bom-type:           sbom
    image:              ${{ steps.build.outputs.image }}
    token:              ${{ secrets.ACCUKNOX_TOKEN }}
    endpoint:           ${{ secrets.ACCUKNOX_ENDPOINT }}
    label:              ${{ secrets.ACCUKNOX_LABEL }}
    project-name:       my-project
    project-classifier: container
```
{% endraw %}

#### Inputs

| Name | Description | Possible Options | Required |
|---|---|---|---|
| `bom-type` | Type of BOM to generate | `sbom` | **Yes** |
| `image` | Container image reference. Build with any tool (docker, podman, buildah, ko). Build step must run in the same job. | Image tag, e.g. `myapp:abc1234` | **Yes** |
| `token` | AccuKnox API token | — | **Yes** |
| `endpoint` | AccuKnox SaaS hostname | Hostname only, no `https://` | **Yes** |
| `label` | AccuKnox label | — | **Yes** |
| `project-name` | AccuKnox project name | Any string | **Yes** |
| `project-classifier` | CycloneDX classifier | `container` | **Yes** |

---

### CBOM from Go Source Code

Scans Go source for cryptographic algorithms, protocols, and certificates.

{% raw %}
```yaml
- uses: accuknox/xbom-action@2.0
  with:
    bom-type:           cbom
    path:               "."
    token:              ${{ secrets.ACCUKNOX_TOKEN }}
    endpoint:           ${{ secrets.ACCUKNOX_ENDPOINT }}
    label:              ${{ secrets.ACCUKNOX_LABEL }}
    project-name:       my-project
    project-classifier: application
```
{% endraw %}

#### Inputs

| Name | Description | Possible Options | Required |
|---|---|---|---|
| `bom-type` | Type of BOM to generate | `cbom` | **Yes** |
| `path` | Directory containing Go source | Any valid directory path | No (default: `.`) |
| `token` | AccuKnox API token | — | **Yes** |
| `endpoint` | AccuKnox SaaS hostname | Hostname only, no `https://` | **Yes** |
| `label` | AccuKnox label | — | **Yes** |
| `project-name` | AccuKnox project name | Any string | **Yes** |
| `project-classifier` | CycloneDX classifier | `application`, `library` | **Yes** |

---

### CBOM from Container Image

Scans a container image for cryptographic algorithms, protocols, and certificates.

!!! warning
    The build step and scan action must be in the same job to share the runner. Build with any tool: docker, podman, buildah, ko, etc.

{% raw %}
```yaml
- name: Build image
  id: build
  run: |
    IMAGE="myapp:${{ github.sha }}"
    docker build -t "$IMAGE" .
    echo "image=${IMAGE}" >> "$GITHUB_OUTPUT"

- uses: accuknox/xbom-action@2.0
  with:
    bom-type:           cbom
    image:              ${{ steps.build.outputs.image }}
    token:              ${{ secrets.ACCUKNOX_TOKEN }}
    endpoint:           ${{ secrets.ACCUKNOX_ENDPOINT }}
    label:              ${{ secrets.ACCUKNOX_LABEL }}
    project-name:       my-project
    project-classifier: container
```
{% endraw %}

#### Inputs

| Name | Description | Possible Options | Required |
|---|---|---|---|
| `bom-type` | Type of BOM to generate | `cbom` | **Yes** |
| `image` | Container image reference. Build step must run in the same job. | Image tag, e.g. `myapp:abc1234` | **Yes** |
| `token` | AccuKnox API token | — | **Yes** |
| `endpoint` | AccuKnox SaaS hostname | Hostname only, no `https://` | **Yes** |
| `label` | AccuKnox label | — | **Yes** |
| `project-name` | AccuKnox project name | Any string | **Yes** |
| `project-classifier` | CycloneDX classifier | `container` | **Yes** |

---

### AIBOM from HuggingFace Model

Inventories an AI/ML model by fetching metadata from the HuggingFace Hub API.

{% raw %}
```yaml
- uses: accuknox/xbom-action@2.0
  with:
    bom-type:           aibom
    aibom-source:       huggingface
    aibom-model:        google-bert/bert-base-uncased
    token:              ${{ secrets.ACCUKNOX_TOKEN }}
    endpoint:           ${{ secrets.ACCUKNOX_ENDPOINT }}
    label:              ${{ secrets.ACCUKNOX_LABEL }}
    project-name:       my-project
    project-classifier: machine-learning-model
```
{% endraw %}

#### Inputs

| Name | Description | Possible Options | Required |
|---|---|---|---|
| `bom-type` | Type of BOM to generate | `aibom` | **Yes** |
| `aibom-source` | AIBOM data source | `huggingface` | No (default: `huggingface`) |
| `aibom-model` | HuggingFace model ID | e.g. `google-bert/bert-base-uncased`, `meta-llama/Llama-2-7b` | **Yes** |
| `token` | AccuKnox API token | — | **Yes** |
| `endpoint` | AccuKnox SaaS hostname | Hostname only, no `https://` | **Yes** |
| `label` | AccuKnox label | — | **Yes** |
| `project-name` | AccuKnox project name | Any string | **Yes** |
| `project-classifier` | CycloneDX classifier | `machine-learning-model` | **Yes** |

---

### AIBOM from AWS Bedrock

Inventories all foundation models accessible in your AWS Bedrock account for the given region. Requires AWS credentials with `bedrock:ListFoundationModels` permission.

{% raw %}
```yaml
- uses: accuknox/xbom-action@2.0
  with:
    bom-type:              aibom
    aibom-source:          bedrock
    aws-region:            us-east-1
    aws-access-key-id:     ${{ secrets.AWS_ACCESS_KEY_ID }}
    aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
    token:                 ${{ secrets.ACCUKNOX_TOKEN }}
    endpoint:              ${{ secrets.ACCUKNOX_ENDPOINT }}
    label:                 ${{ secrets.ACCUKNOX_LABEL }}
    project-name:          my-project
    project-classifier:    application
```
{% endraw %}

#### Inputs

| Name | Description | Possible Options | Required |
|---|---|---|---|
| `bom-type` | Type of BOM to generate | `aibom` | **Yes** |
| `aibom-source` | AIBOM data source | `bedrock` | **Yes** |
| `aws-region` | AWS region for Bedrock scan | e.g. `us-east-1`, `us-west-2`, `eu-central-1` | **Yes** |
| `aws-access-key-id` | AWS access key ID with `bedrock:ListFoundationModels` permission | — | **Yes** |
| `aws-secret-access-key` | AWS secret access key | — | **Yes** |
| `token` | AccuKnox API token | — | **Yes** |
| `endpoint` | AccuKnox SaaS hostname | Hostname only, no `https://` | **Yes** |
| `label` | AccuKnox label | — | **Yes** |
| `project-name` | AccuKnox project name | Any string | **Yes** |
| `project-classifier` | CycloneDX classifier | `machine-learning-model` | **Yes** |

---

## Complete Workflow Example

{% raw %}
```yaml
name: AccuKnox xBOM Scan

on:
  push:
    branches: [main, master]
  pull_request:
    branches: [main, master]

jobs:
  xbom-scan:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v6

      - uses: accuknox/xbom-action@2.0
        with:
          bom-type:           sbom
          path:               "."
          token:              ${{ secrets.ACCUKNOX_TOKEN }}
          endpoint:           ${{ secrets.ACCUKNOX_ENDPOINT }}
          label:              ${{ secrets.ACCUKNOX_LABEL }}
          project-name:       my-project
          project-classifier: application
```
{% endraw %}

---

## Downloading the BOM Artefact

After the workflow runs:

1. Go to your repository on GitHub.
2. Click **Actions**.
3. Select the workflow run.
4. Scroll to the **Artifacts** section at the bottom.
5. Click to download the BOM file.

---

## Publishing BOM to GitHub Releases

To attach the BOM as a GitHub Release asset, trigger the workflow on `release: published` and use `softprops/action-gh-release` to attach the generated BOM.

!!! warning
    The job requires explicit permissions and must be triggered by a release event.

{% raw %}
```yaml
name: AccuKnox xBOM Scan

on:
  release:
    types: [published]

jobs:
  xbom-publish:
    runs-on: ubuntu-latest
    permissions:
      actions:  read
      contents: write

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v6

      - name: Run AccuKnox xBOM Scan
        uses: accuknox/xbom-action@2.0
        with:
          bom-type:           sbom
          path:               "."
          token:              ${{ secrets.ACCUKNOX_TOKEN }}
          endpoint:           ${{ secrets.ACCUKNOX_ENDPOINT }}
          label:              ${{ secrets.ACCUKNOX_LABEL }}
          project-name:       my-project
          project-classifier: application

      - name: Download Workflow Artifacts
        uses: actions/download-artifact@v4
        with:
          path: artifacts

      - name: Upload SBOM to GitHub Release
        uses: softprops/action-gh-release@v2
        with:
          files: artifacts/**/*.json
```
{% endraw %}

**How it works:**

1. The action generates and uploads the BOM and saves it as a workflow artefact.
2. `actions/download-artifact@v4` pulls all workflow artefacts into `artifacts/`.
3. `softprops/action-gh-release@v2` attaches every `*.json` file under `artifacts/` to the release that triggered the workflow.

**To trigger the workflow with a release:**

1. Push the workflow file to your default branch (`main` or `master`).
2. Go to **Releases → Draft a new release**.
3. Pick a tag, fill in the title, and click **Publish release**.
4. The workflow runs automatically; the BOM appears under **Assets** on the release page when it finishes.

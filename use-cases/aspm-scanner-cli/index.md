---
title: ASPM Scanner CLI
description: Run IaC, SAST, Secret, Container, and DAST scans from a single CLI - in CI/CD pipelines or local developer workflows - and optionally upload results to the AccuKnox ASPM Platform.
---

# ASPM Scanner CLI

`accuknox-aspm-scanner` is a unified CLI that brings all of your application security scans - IaC, SAST, SonarQube SAST, Secret, Container, and DAST - under a single command. Run it in any CI/CD pipeline or directly on a developer workstation.

Results can be uploaded to the **AccuKnox ASPM Platform**, or the CLI can operate in **standalone / air-gapped mode** with no outbound connectivity required.

<div class="grid cards" markdown>

-   :material-shield-check:{ .lg .middle } **One CLI, six scan types**

    IaC · SAST · SonarQube SAST · Secrets · Container · DAST

-   :material-cloud-upload-outline:{ .lg .middle } **Flexible upload**

    Push results to the AccuKnox platform or keep them local with `--skip-upload`

-   :material-docker:{ .lg .middle } **Container & local mode**

    Run scans via Docker container mode or install tools locally

-   :material-server-off:{ .lg .middle } **Air-gap friendly**

    Mirror images to an internal registry - no public internet required

</div>

**Supported scan types:**

| Scan Type | Typical Use |
|---|---|
| `iac` | Terraform / IaC misconfigurations |
| `sast` | Static code analysis |
| `sq-sast` | Enterprise SAST + result fetch |
| `secret` | Hardcoded credentials / secrets |
| `container` | Container image vulnerabilities |
| `dast` | Runtime web application scanning |

!!! info "Running in a restricted or air-gapped environment?"
    Jump straight to the on-prem setup section for installation patterns, mirrored image examples, and known limitations.

    [Skip to On-Prem & Air-Gapped Setup :material-arrow-down:](#on-prem-setup){ .md-button }

---

## Installation

=== "Connected environment"

    Install from the GitHub release wheel:

    ```bash
    pip install https://github.com/accuknox/aspm-scanner-cli/releases/download/v0.14.2/accuknox_aspm_scanner-0.14.2-py3-none-any.whl
    ```

=== "Restricted / On-Prem"

    Install from the release `.deb` package:

    ```bash
    sudo dpkg -i accuknox-aspm-scanner_<version>.deb
    ```

---

## Quick Start

!!! success "Fastest path to your first scan"
    The three steps below get you from zero to a local scan result in under two minutes.

### 1. Install the required local tool

```bash
accuknox-aspm-scanner tool install --type iac
```

### 2. Run a scan (no upload)

```bash
accuknox-aspm-scanner scan --skip-upload --keep-results iac --command "-d ."
```

### 3. Run a scan with upload to AccuKnox

```bash
ACCUKNOX_ENDPOINT=cspm.accuknox.com \
ACCUKNOX_LABEL=POC \
ACCUKNOX_TOKEN=abcd1234 \
accuknox-aspm-scanner scan --softfail sast --command "scan ."
```

!!! tip
    Not ready to connect to the platform yet? Use `--skip-upload --keep-results` on any scan to collect result files locally without any credentials.

---

## How the Scan Command Works

```
accuknox-aspm-scanner scan [common-flags] <scan-type> --command "<scanner-args>" [scan-type-flags]
```

| Part | What it does |
|---|---|
| `[common-flags]` | Control upload behavior - apply to all scan types |
| `<scan-type>` | One of: `iac`, `sast`, `sq-sast`, `secret`, `container`, `dast` |
| `--command "..."` | Required - arguments forwarded directly to the scanner |
| `[scan-type-flags]` | Optional flags specific to the chosen scan type |

!!! example "Reading a scan command"
    ```bash
    accuknox-aspm-scanner scan --skip-upload --keep-results iac --command "-d ." --container-mode
    ```
    - `--skip-upload` and `--keep-results` → common flags (before scan type)
    - `iac` → scan type
    - `--command "-d ."` and `--container-mode` → IaC-specific flags

**Common flags:**

| Flag | Description |
|---|---|
| `--endpoint` | AccuKnox control plane URL |
| `--label` | Label to associate uploaded results |
| `--token` | Bearer token for upload |
| `--project-name` | Project name (required for SBOM uploads) |
| `--skip-upload` | Run without uploading results |
| `--keep-results` | Keep result files after scan completion |
| `--softfail` | Do not fail the pipeline on findings |

!!! tip "Upload credentials"
    If `--skip-upload` is **not** set, you must provide `ACCUKNOX_ENDPOINT`, `ACCUKNOX_LABEL`, and `ACCUKNOX_TOKEN` - either as environment variables or as flags before the scan type.

---

## Scan Reference

=== "IaC"

    Scans Terraform and other IaC files for misconfigurations.

    ```bash
    # Local
    accuknox-aspm-scanner scan --skip-upload --keep-results iac --command "-d ."

    # Container mode with upload
    ACCUKNOX_ENDPOINT=cspm.accuknox.com \
    ACCUKNOX_LABEL=POC \
    ACCUKNOX_TOKEN=abcd1234 \
    accuknox-aspm-scanner scan iac --command "-d ." --container-mode
    ```

    **Flags after `iac`:** `--container-mode`, `--repo-url`, `--repo-branch`

=== "SAST"

    Static analysis for code vulnerabilities.

    ```bash
    # Local
    accuknox-aspm-scanner scan --skip-upload --keep-results sast --command "scan ."

    # With AI analysis
    accuknox-aspm-scanner scan --skip-upload --keep-results sast \
      --command "scan ." --ai-analysis --aiscan-severity "HIGH,CRITICAL"

    # Container mode with upload
    ACCUKNOX_ENDPOINT=cspm.accuknox.com \
    ACCUKNOX_LABEL=POC \
    ACCUKNOX_TOKEN=abcd1234 \
    accuknox-aspm-scanner scan sast --command "scan ." --container-mode
    ```

    **Flags after `sast`:** `--container-mode`, `--severity`, `--ai-analysis`, `--aiscan-severity`, `--codeassure-config`, `--repo-url`, `--commit-ref`, `--commit-sha`, `--pipeline-id`, `--job-url`

=== "Secret"

    Detects hardcoded secrets and credentials in source code and git history.

    ```bash
    # Container mode (recommended)
    accuknox-aspm-scanner scan --skip-upload --keep-results secret \
      --command "git file://." --container-mode

    # Container mode with upload
    ACCUKNOX_ENDPOINT=cspm.accuknox.com \
    ACCUKNOX_LABEL=POC \
    ACCUKNOX_TOKEN=abcd1234 \
    accuknox-aspm-scanner scan secret --command "git file://." --container-mode
    ```

    **Flags after `secret`:** `--container-mode`

=== "Container"

    Scans container images for vulnerabilities and optionally generates an SBOM.

    ```bash
    # Local
    accuknox-aspm-scanner scan --skip-upload --keep-results container \
      --command "image nginx:latest" --container-mode

    # With SBOM generation
    accuknox-aspm-scanner scan --skip-upload --keep-results --project-name demo-project \
      container --command "image nginx:latest" --generate-sbom --container-mode

    # Container mode with upload
    ACCUKNOX_ENDPOINT=cspm.accuknox.com \
    ACCUKNOX_LABEL=POC \
    ACCUKNOX_TOKEN=abcd1234 \
    accuknox-aspm-scanner scan container --command "image nginx:latest" --container-mode
    ```

    **Flags after `container`:** `--container-mode`, `--generate-sbom`

=== "DAST"

    Runtime web application scanning.

    !!! warning "Use container mode for DAST"
        DAST is most reliable in `--container-mode`. Local-mode execution is not fully supported.

    ```bash
    # Container mode (recommended)
    accuknox-aspm-scanner scan --skip-upload --keep-results dast \
      --command "zap-baseline.py -t http://example.com/ -I" --container-mode

    # Container mode with upload
    ACCUKNOX_ENDPOINT=cspm.accuknox.com \
    ACCUKNOX_LABEL=POC \
    ACCUKNOX_TOKEN=abcd1234 \
    accuknox-aspm-scanner scan dast \
      --command "zap-baseline.py -t http://example.com/ -I" --container-mode
    ```

    **Flags after `dast`:** `--container-mode`, `--severity-threshold`

=== "SonarQube SAST"

    Enterprise SAST with integrated result fetch.

    ```bash
    # Skip upload
    accuknox-aspm-scanner scan --skip-upload --keep-results sq-sast \
      --command "-Dsonar.projectKey=<KEY> -Dsonar.host.url=<URL> -Dsonar.token=<TOKEN> -Dsonar.organization=<ORG>"

    # Container mode with upload
    ACCUKNOX_ENDPOINT=cspm.accuknox.com \
    ACCUKNOX_LABEL=POC \
    ACCUKNOX_TOKEN=abcd1234 \
    accuknox-aspm-scanner scan sq-sast \
      --command "-Dsonar.projectKey=<KEY> -Dsonar.host.url=<URL> -Dsonar.token=<TOKEN> -Dsonar.organization=<ORG>" \
      --container-mode
    ```

    !!! warning "--command is always required for sq-sast"
        `--command` is required even when `--skip-sonar-scan` is used. Always pass Sonar metadata (`-Dsonar.projectKey`, `-Dsonar.host.url`, `-Dsonar.token`) so the result fetcher can retrieve findings from your SonarQube instance.

    **Flags after `sq-sast`:** `--container-mode`, `--skip-sonar-scan`, `--repo-url`, `--branch`, `--commit-sha`, `--pipeline-url`

---

## Environment Variables

| Variable | Description |
|---|---|
| `ACCUKNOX_ENDPOINT` | Control plane URL for result upload |
| `ACCUKNOX_LABEL` | Label to associate uploaded results |
| `ACCUKNOX_TOKEN` | Bearer token for upload |
| `ACCUKNOX_PROJECT_NAME` | Project name for SBOM uploads |
| `DEBUG` | Set to `TRUE` for verbose debug logs |
| `SOFT_FAIL` | Set to `TRUE` to enable soft-fail by default |
| `KEEP_RESULTS` | Set to `TRUE` to keep result files after scan |
| `SCAN_IMAGE` | Override the scanner image used in container mode |
| `CODEASSURE_IMAGE` | Override the AI analysis image for SAST |

!!! danger "`SCAN_IMAGE` is scanner-scoped, not global"
    `SCAN_IMAGE` is shared across all scanner types. Always set it immediately before the relevant scan and replace or unset it before switching to a different scan type to avoid using the wrong image.

---

## On-Prem & Air-Gapped Setup { #on-prem-setup }

!!! abstract "TL;DR for on-prem"
    - Install via the `.deb` package.
    - Use `--skip-upload --keep-results` for local validation.
    - For container mode in restricted networks, mirror scanner images and set `SCAN_IMAGE` per scan.
    - Linux is required for local mode; Windows local mode is not fully supported.

### Recommended approach

For most on-prem environments:

1. Install the CLI using the `.deb` package.
2. Choose **local mode** (install tools first) or **container mode** (mirror images).
3. Use `--skip-upload --keep-results` for early validation.
4. Test upload separately once the control plane is reachable.

### Local mode prerequisites

- Linux is the best-supported platform for local mode (Windows local mode is incomplete).
- Install required tools first:

```bash
accuknox-aspm-scanner tool install --all
# or per type:
accuknox-aspm-scanner tool install --type iac
```

Tool install path: `~/.local/bin/accuknox/` (user) or `/usr/share/accuknox-aspm-scanner/tools` (Debian package).

!!! warning "Air-gapped environments"
    `tool install` downloads from public sources. Fully restricted environments need either pre-staged tools placed in the expected path, or container mode with mirrored images.

### Container mode with internal registries

Set `SCAN_IMAGE` to your mirrored image before each scan:

=== "IaC"
    ```bash
    export SCAN_IMAGE=registry.local/accuknox/iac-scanner:<version>
    accuknox-aspm-scanner scan --skip-upload --keep-results iac --command "-d ." --container-mode
    ```

=== "SAST"
    ```bash
    accuknox-aspm-scanner tool install --type sast
    accuknox-aspm-scanner scan --skip-upload --keep-results sast --command "scan ."
    ```

=== "Secret"
    ```bash
    export SCAN_IMAGE=registry.local/accuknox/secret-scanner:<version>
    accuknox-aspm-scanner scan --skip-upload --keep-results secret --command "git file://." --container-mode
    ```

=== "Container"
    ```bash
    export SCAN_IMAGE=registry.local/accuknox/container-scanner:<version>
    accuknox-aspm-scanner scan --skip-upload --keep-results container --command "image nginx:latest" --container-mode
    ```

=== "DAST"
    ```bash
    export SCAN_IMAGE=registry.local/accuknox/dast-scanner:<version>
    accuknox-aspm-scanner scan --skip-upload --keep-results dast \
      --command "zap-baseline.py -t http://example.com/ -I" --container-mode
    ```

=== "SonarQube SAST"
    ```bash
    export SCAN_IMAGE=registry.local/accuknox/sq-sast-scanner:<version>
    accuknox-aspm-scanner scan --skip-upload --keep-results sq-sast \
      --command "-Dsonar.projectKey=my-project -Dsonar.host.url=https://sonarqube.internal -Dsonar.token=$SONAR_TOKEN" \
      --container-mode
    ```

### Result files

The CLI writes outputs to fixed filenames for consistent collection:

| Scan | Output file |
|---|---|
| IaC | `results_json.json` |
| SAST | `results.json` |
| Secret | `results.jsonl` |
| Container | `results.json` |
| DAST | `results.json` |

Files are deleted after the scan unless `--keep-results` (or `KEEP_RESULTS=TRUE`) is set.

!!! tip
    For on-prem validation, always add `--keep-results` so you can inspect the raw output before configuring upload.

---

## Troubleshooting

??? warning "Upload fails - missing credentials"
    If upload is enabled, `ACCUKNOX_ENDPOINT`, `ACCUKNOX_LABEL`, and `ACCUKNOX_TOKEN` are required.

    **Fix:** Add `--skip-upload` for standalone testing, or export the required variables.

??? warning "Tool not found in local mode"
    The required scanner tool is not installed.

    **Fix:** Run `accuknox-aspm-scanner tool install --type <tool>`, or switch to `--container-mode`.

??? warning "Result files disappeared after the scan"
    The CLI deletes result files by default after a scan.

    **Fix:** Add `--keep-results`, or set `KEEP_RESULTS=TRUE`.

??? warning "Docker access issues in container mode"
    Container mode requires a running Docker daemon and image pull access.

    **Fix:** Verify `docker run` works from the same host account. Mirror required images and set `SCAN_IMAGE` to the internal image before scanning.

??? info "sq-sast: --skip-sonar-scan still requires --command"
    This is a known parser limitation.

    **Fix:** Always pass Sonar metadata in `--command` so the result fetcher can retrieve findings:
    ```bash
    accuknox-aspm-scanner scan --skip-upload sq-sast --skip-sonar-scan \
      --command "-Dsonar.projectKey=my-project -Dsonar.host.url=https://sonarqube.internal -Dsonar.token=$SONAR_TOKEN"
    ```

---

## Tool Management

```bash
# Install all tools
accuknox-aspm-scanner tool install --all

# Install or update a specific tool
accuknox-aspm-scanner tool install --type sast
accuknox-aspm-scanner tool update --type iac
```

Supported types: `iac`, `sast`, `sq-sast`, `secret`, `container`, `dast`, `codeassure`

---

## Pre-Commit Integration

!!! tip "Catch issues before they reach CI"
    The pre-commit hook runs scans locally on staged files, giving developers instant feedback without waiting for a pipeline run.

```bash
# Install the pre-commit hook
accuknox-aspm-scanner pre-commit install

# Remove it
accuknox-aspm-scanner pre-commit uninstall
```

---

## Debugging

!!! info "Enable verbose output"
    Set `DEBUG=TRUE` to get detailed logs for any scan command. Useful for diagnosing tool execution failures, upload errors, or unexpected behavior.

```bash
DEBUG=TRUE accuknox-aspm-scanner scan --skip-upload iac --command "-d ."
```

Use `--help` at any level for the full flag reference:

```bash
accuknox-aspm-scanner --help
accuknox-aspm-scanner scan --help
accuknox-aspm-scanner scan iac --help
```

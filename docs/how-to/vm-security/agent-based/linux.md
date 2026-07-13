---
title: Agent-Based VM Scanning for Linux
description: Comprehensive guide for Agent-based Vulnerability and Malware Scanning on Linux VMs.
---

<style>
  .nt-card-title{
    text-align: center;
  }

  .nt-card-img img{
    color: #00025;
  }
</style>

# Agent-Based VM Scanning for Linux

This guide provides step-by-step instructions to onboard Linux Virtual Machines (VMs) for agent-based vulnerability and malware scanning using the AccuKnox VM Security agent.

For a fleet-wide onboarding walkthrough with distribution-specific commands, pick a guide below:

::cards:: cols=2

- title: Ubuntu
  image: ./images/ubuntu.svg
  url: /how-to/vm-security/agent-based/ubuntu/

- title: RHEL
  image: ./images/rhel.svg
  url: /how-to/vm-security/agent-based/rhel/

::/cards::

## Prerequisites

- Root or sudo access to the Linux VM.
- Outbound internet connectivity to AccuKnox SaaS.
- `curl` installed on the VM.
- A valid AccuKnox Tenant ID and API Token.

## Installation

### 1. Run the Installation Script

Run the following command to download and install the agent. Replace `<REDACTED>` with your actual Artifact API Token and `CHANGEME` with your desired label.

```bash
curl https://accuknox-omni.s3.us-east-1.amazonaws.com/latest/agent-install.sh | \
    OMNI_ARTIFACT_API_TOKEN="<REDACTED>" \
    bash -s - \
        --artifact-endpoint=https://cspm.accuknox.com/api/v1/artifact/ \
        --tenant-id=000 \
        --artifact-label=CHANGEME
```

!!! note "Configuration Details"
    - **Artifact API Token**: Generate this under **Settings > Tokens** in the AccuKnox dashboard.
    - **Artifact Label**: Create a label under **Settings > Labels** to identify this VM.
    - The installation script creates a systemd service (`omni.service`) and a daily systemd timer (`omni.timer`).

## Air-gapped Installation

For environments without direct internet access, follow these steps:

### 1. Download the VM Scan Solution Binary

Download the appropriate binary for your architecture on a machine with internet access:

- **amd64**: [Download Link](https://accuknox-omni.s3.us-east-1.amazonaws.com/v0.1.2/omni-linux-amd64)
- **arm64**: [Download Link](https://accuknox-omni.s3.us-east-1.amazonaws.com/v0.1.2/omni-linux-arm64)

### 2. Install the Binary

Transfer the binary to the target VM and place it in the executable path:

```bash
# Assuming the binary is in the current directory
chmod +x omni-linux-amd64
sudo mv omni-linux-amd64 /usr/local/bin/omni
```

### 3. Run the Installation Script

Download the `agent-install.sh` script, transfer it to the VM, and run it with the necessary environment variables:

```bash
chmod +x agent-install.sh

export OMNI_ARTIFACT_API_TOKEN="<REDACTED>"
export OMNI_VULN_DB_REPOSITORY="ghcr.io/aquasecurity/trivy-db" # Replace with your private registry if needed
export OMNI_SKIP_DOWNLOAD=1

./agent-install.sh
```

## Configuration & Troubleshooting

### Check Scan Status

You can check the status of the agent and the scan timer using `systemctl`:

```bash
systemctl status omni.timer
systemctl status omni.service
journalctl -u omni
```

### Adjust Resource Usage

By default, the systemd service is limited to **2G memory** and **10% CPU** utilization. If the scan is getting OOMKilled or you need to adjust these limits, set the following environment variables and re-run the installation script:

```bash
export OMNI_MAX_MEMORY=4G
export OMNI_CPU_QUOTA=20%
# Re-run installation script
```

### Enable Malware Scanning

Malware scanning is disabled by default as it is CPU-intensive. To enable it, set the `OMNI_SKIP_MALWARE_SCAN` variable to `false` and re-run the installation script:

```bash
export OMNI_SKIP_MALWARE_SCAN=false
# Re-run installation script
```

### Uninstall

To remove the agent and related services:

```bash
/usr/local/bin/omni-uninstall.sh
```
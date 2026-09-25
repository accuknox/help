---
title: On-Prem Single Node Installation Guide
description: Step-by-step guide for installing AccuKnox on a single node (Ubuntu 24.04).
---

# On-Prem Single Node Installation Guide

This guide provides step-by-step instructions for installing AccuKnox on a single node.

!!! info "Supported Operating Systems"
    Installation was tested on **Ubuntu 24.04** and **Rocky Linux 8**.

## Prerequisites

### Hardware Requirements

* **Standard Deployment:** 8 vCPU / 32 GB RAM / 256 GB Storage
* **For AI-SPM and Ask-AI enabled:** 12 vCPU / 48 GB RAM / 500 GB Storage
* **Required Binaries:** `tar`, `wget`

!!! warning "Rocky Linux Users"
    SELinux should be disabled or set to permissive if you are installing on Rocky Linux.

## Installation Steps

### Step 1: Download the Installation Bundle

Download the AccuKnox bundle using `wget` (the exact URL will be given at the time of deployment by the AccuKnox team):

```bash
wget https://accukno-xxxx-xxxx.xxxx.your-objectstorage.com/releases/AccuKnox-cp-v3.5-Jun-17.tar.gz
```

### Step 2: Extract the Installation Bundle

Extract the downloaded file, remove the archive to free up space, and navigate to the directory:

```bash
tar -xvf AccuKnox-cp-v3.5-Jun-17.tar.gz
rm Accuknox-cp-v3.5-Jun-17.tar.gz
cd Accuknox/
```

### Step 3: Extract Helm Charts

Extract the Helm charts and navigate to their directory:

```bash
tar -xvf Helm-charts-xxx.tar.gz
cd Helm-charts-xxx/
```
### Step 4: Download Required Container Images

```bash
cd image-downloader/
```
Standard Deployment Images:

```bash
./tar_download.sh --cspm 
```
or
For Standard Deployment with AI-SPM images:

```bash
./tar_download.sh --cspm --aispm
```

### Step 5: Install Dependencies

Run the scripts to install the required binaries and K3s:

```bash
cd ..
./binaries.sh
./airgapped_k3s.sh server
```

### Step 6: Install AccuKnox Charts

Standard Installation

```bash
./install_chart.sh
```
To enable AI-SPM features, provide the required API keys during installation:

```bash
./install_chart.sh --aispm
```

Enable Ask-AI and AI Copilot (Optional):

```bash
./install_chart.sh --askai
```

### Step 7: Configure Deployment Values

Update the necessary overrides in `override-values.yaml`. For an **IP-based deployment (recommended for POC)**, update the `nginxIngressGateway` with your appropriate `<PRIVATE-IP>`:

```yaml title="override-values.yaml"
ingressGateway:
  enabled: true
nginxIngressGateway:
  enabled: true
  loadBalancerHost: "<PRIVATE-IP>"
```

!!! note "SSL Configuration"
    If you are deploying with an IP-based method, disable SSL. The override values file should be updated as follows:

    ```yaml title="override-values.yaml"
    ssl:
      selfsigned: false
      customcerts: false
    ```
### Step 8: Access the UI and Complete Setup

1. Open the AccuKnox UI in your browser at: `https://<SERVER-IP OR DNS>/ `
2. To complete sign-up, please connect to the AccuKnox team

    ```bash
    kubectl logs deploy/celery -n accuknox-divy | grep "check-email-verification"
    ```
3. Use the generated link to complete account activation. For assistance, contact the AccuKnox team.

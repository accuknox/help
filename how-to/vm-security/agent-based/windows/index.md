---
title: Agent-Based VM Scanning for Windows
description: Comprehensive guide for Agent-based Vulnerability and Malware Scanning on Windows VMs.
---

# Agent-Based VM Scanning for Windows

This guide provides step-by-step instructions to onboard Windows Virtual Machines (VMs) for agent-based vulnerability and malware scanning using the AccuKnox VM Scan Solution agent.

!!! info "This flow also enables Shadow AI Discovery"
    The same onboarding flow powers [Shadow AI Discovery](../../../use-cases/shadow-ai-discovery.md) on the host. The agent performs package-level discovery, so AI frameworks, agent frameworks, SDKs, and model runtimes installed on the VM are classified and reported under the **Unmanaged** tab, alongside their vulnerability data.

    This includes agentic AI runtimes such as OpenClaw. AccuKnox scans VMs for OpenClaw instances and reports each one as an unmanaged asset, mapped to its parent host.

## Prerequisites

- Administrator access to the Windows VM.
- Outbound internet connectivity to AccuKnox SaaS.
- A valid AccuKnox Tenant ID and API Token.

## Installation

### 1. Download the Installer Script

Open a PowerShell terminal as Administrator and run the following command to download the agent installation script:

```powershell
Invoke-WebRequest -Uri 'https://accuknox-omni.s3.us-east-1.amazonaws.com/latest/agent-install.ps1' -OutFile .\agent-install.ps1
```

### 2. Run the Installation Script

Execute the script to install and configure the agent. Replace `<REDACTED>` with your actual Artifact API Token and `CHANGEME` with your desired label.

```powershell
.\agent-install.ps1 `
    -ArtifactEndpoint https://cspm.accuknox.com/api/v1/artifact/ `
    -TenantId 000 `
    -ArtifactLabel CHANGEME `
    -ArtifactApiToken "<REDACTED>" `
    -SkipMalwareScan $true
```

!!! note "Configuration Details"
    - **Artifact API Token**: Generate this under **Settings > Tokens** in the AccuKnox dashboard.
    - **Artifact Label**: Create a label under **Settings > Labels** to identify this VM.
    - **SkipMalwareScan**: Set to `$false` if you want to enable malware scanning immediately (requires ClamAV).

The installation script creates a Windows scheduled task to run the agent periodically.

## Air-gapped Installation

For environments without direct internet access, follow these steps:

### 1. Download & Extract the Bundle

On a machine with internet access, download the all-in-one bundle:

```powershell
Invoke-WebRequest `
    -Uri "https://accuknox-omni.s3.us-east-1.amazonaws.com/latest/all-in-one.zip" `
    -OutFile all-in-one.zip `
    -UseBasicParsing

Expand-Archive -Path ".\all-in-one.zip" -DestinationPath .\ -Force
cd .\all-in-one\
```

### 2. Setup ClamAV Database

Create the directory and move the ClamAV database files:

```powershell
New-Item -ItemType Directory -Path "C:\Program Files\ClamAV" -Force
Move-Item -Path .\database\clamav\ -Destination "C:\Program Files\ClamAV\database" -Force
```

### 3. Setup MSRC Database

Create the directory and move the MSRC database files:

```powershell
New-Item -ItemType Directory -Path "C:\ProgramData\Accuknox\Omni" -Force
Move-Item -Path .\database\msrc\ -Destination "C:\ProgramData\Accuknox\Omni" -Force
```

### 4. Install VM Scan Solution Agent

Move the VM Scan Solution executable to the installation directory:

```powershell
New-Item -ItemType Directory -Path "C:\Program Files\AccuKnox\Omni\" -Force
Move-Item -Path .\omni.exe -Destination "C:\Program Files\AccuKnox\Omni\" -Force
```

### 5. Run the Installation Script (Air-gapped)

Run the installation script with the `-SkipOmniDownload` flag:

```powershell
.\agent-install.ps1 `
    -ArtifactEndpoint https://cspm.accuknox.com/api/v1/artifact/ `
    -TenantId 000 `
    -ArtifactLabel CHANGEME `
    -ArtifactApiToken "<REDACTED>" `
    -SkipOmniDownload $true `
    -SkipDatabaseDownload $true
```

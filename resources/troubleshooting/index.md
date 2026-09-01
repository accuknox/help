---
title: CWPP Troubleshooting
description: Troubleshooting guide for AccuKnox Cloud Workload Protection Platform (CWPP) to resolve issues related to clusters.
---

# CWPP Troubleshooting

If the user faces any issue related to clusters, then they should provide the logs information of their clusters for troubleshooting purposes. To streamline the process, we now provide a single script that customers can run in their environment. This collects all required details— logs, errors and configurations—in one go, speeding up diagnosis and resolution.

## Script to automate this process

- This script collects everything needed to debug an issue in a namespace and packages it into a single .tar.gz file.

- Available in two formats: Shell script and Powershell Script.

- For running the script, the user should have access to their cluster and internet connectivity for directly downloading the script and executing it. If needed, we can provide the zip file for local downloads as well as per security concerns.

# 1. Shell Script

Download the script using below command and execute it directly by passing agents namespace (or any other namespace where the scanners are installed) as the parameter.

**Command:**
```sh
curl -sfL https://accuknox-support-bundles.s3.amazonaws.com/support-bundle.sh | sh -s -- agents
```

If needed to run for another namespace, adjust the command accordingly.

**Example:**
```sh
curl -sfL https://accuknox-support-bundles.s3.amazonaws.com/support-bundle.sh | sh -s -- <namespace>
```

# 2. Powershell Script

**Command:**
```sh
iwr https://accuknox-support-bundles.s3.amazonaws.com/support-bundle.ps1 -OutFile bundle.ps1; .\bundle.ps1 agents
```

If needed to run for another namespace, adjust the command accordingly.

**Example:**
```sh
iwr https://accuknox-support-bundles.s3.amazonaws.com/support-bundle.ps1 -OutFile bundle.ps1; .\bundle.ps1 <desired namespace>
```

### Output

![tbshoot](images/tbshoot-0.png)

- - -
[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }
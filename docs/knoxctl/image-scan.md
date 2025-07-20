---
title: "Container Image Scanner"
weight: 4
summary: "Knoxctl can scan container images running on a perticular VM and submit the results to SaaS"
hide:
  - toc
---

# Container Image Scanner

AccuKnox offers a container image scanning solution designed to periodically inspect container images running on your machine.

## 🛠 Installation Guide

Follow these steps to deploy the container image scanner:

### 1. Create a Label

In the AccuKnox Control Plane, create a unique [**Label**](https://app.accuknox.com/settings/labels). This will be associated with the container image scan reports.

### 2. Generate a Token

From the AccuKnox Control Plane:

- Generate an [**Artifact Token**](https://app.accuknox.com/settings/tokens)
- Note down both the **Token** and your **Tenant ID**

### 3. Scan your machine

Use the following command to scan your machine:


```bash
knoxctl image-scan --artifactEndpoint="<url>" \
    --token="<authToken>" \
    --label="<label>" \
    --tenantId="<tenantId>"
```

Replace the parameters (`<tenantId>` , `<authToken>`, `<url>` and `<label>`) with the appropriate values.

if you want to scan the machine on a regular basis you can configure the scan to be run by systemd timers by running the following script.

Before running the script you need to replace the parameters (`<tenantId>` , `<authToken>`, `<url>` and `<label>`) with their appropriate values.

```bash
#!/bin/bash

export AK_BASE_URL="<url>"
export AK_TOKEN="<authToken>"
export AK_LABEL="<label>"
export AK_TENANT_ID="<tenantId>"

export AK_URL="$AK_BASE_URL/api/v1/artifact/"

cat <<EOF | sudo tee /etc/systemd/system/accuknox-container-scan.service
# This service unit is for container image scanning
# By AccuKnox Inc
#

[Unit]
Description=Scan running container images and post results to AccuKnox SaaS
Wants=accuknox-container-scan.timer

[Service]
Type=oneshot
ExecStart=/bin/knoxctl image-scan --artifactEndpoint="$AK_URL" --token="$AK_TOKEN" --label="$AK_LABEL" --tenantId="$AK_TENANT_ID"
MemoryHigh=1800M
MemoryMax=2G
KillMode=control-group
CPUQuota=50%

[Install]
WantedBy=multi-user.target
EOF

cat <<EOF | sudo tee /etc/systemd/system/accuknox-container-scan.timer
# This service unit is for container image scanning
# By AccuKnox Inc
#

[Unit]
Description=Scan running container images and post results to AccuKnox SaaS
Requires=accuknox-container-scan.service

[Timer]
Unit=accuknox-container-scan.service
OnCalendar=daily
Persistent=true

[Install]
WantedBy=timers.target
EOF

systemctl daemon-reload
systemctl enable --now accuknox-container-scan.timer 
```

The above will run the scan daily at midnight, you can change the execution time by modifying the value of `OnCalendar` in the systemd timer configuration.


### ⚙️ Parameters:

| Variable  | Sample Value      | Description                |
| --------- | ----------------- | -------------------------- |
| tenantId  | 11                | AccuKnox Tenant ID         |
| authToken | eyJhbGc...        | AccuKnox Token {JWT}       |
| url       | cspm.accuknox.com | AccuKnox CSPM API Endpoint |
| label     | kubeshield        | AccuKnox Label             |


### ✅ Post-Installation

Once the scan is completed, results will be visible in the [**Findings**](https://app.accuknox.com/issues/findings/findings-summary) or [**Registry Scan**](https://app.accuknox.com/issues/registry-scan) sections within the AccuKnox Control Plane.

- Navigate to [**Issues -> Findings**](https://app.accuknox.com/issues/findings/findings-summary)
- Switch to **Findings** tab
- Select **Container Image Findings** & do **Group by** based on **Label Name**
- You should be able to see the data for the **Label** used in above command

---


# Kubernetes Security Onboarding

## Features Supported for Kubernetes

- Supported on managed (EKS, AKS, OCI) and on-prem Kubernetes clusters
- Works on Kubernetes versions >= 1.18
- All features are modular and can be enabled independently
- Available via AccuKnox SaaS and On-Prem Control Plane with identical UX
- Runtime Security requires Linux kernel >= 4.15
- Only egress connectivity from K8s cluster to control plane is required

## K8s Runtime Visibility and Security

**Deployment Mode:**
DaemonSet via Operator (default) or Kubernetes manifests

**Helm Command:**

```bash
helm upgrade --install agents oci://public.ecr.aws/k9v9d5v2/agents-chart \
--version "v0.10.0" \
--set joinToken="[TOKEN]" \
--set spireHost="spire.demo.accuknox.com" \
--set ppsHost="pps.demo.accuknox.com" \
--set knoxGateway="knox-gw.demo.accuknox.com:3000" \
--set admissionController.enabled=false \
--set kyverno.enabled=false \
-n agents --create-namespace
```

**Features:**

- File, process, and network visibility
- MITRE-based policy enforcement (FIM, cryptojacking protection, etc.)
- Auto-discovery of ingress/egress and whitelisting policies

**Control Plane Access:**

- PPS: Port 443
- SPIRE: Port 443
- Knox Gateway: Port 3000

## K8s Misconfiguration Scanning

**Deployment Mode:**
Kubernetes cronjob

**Helm Command:**

```bash
helm upgrade --install k8s-risk-assessment-job oci://public.ecr.aws/k9v9d5v2/k8s-risk-assessment-job \
--set accuknox.authToken="[AUTHTOKEN]" \
--set accuknox.cronTab="30 9 * * *" \
--set accuknox.clusterName="[CLUSTERNAME]" \
--set accuknox.URL="cspm.demo.accuknox.com" \
--set accuknox.label="[LABEL]" \
--version=v1.1.3
```

**Features:**

- Detection of misconfigurations and insecure configurations
- Includes checks for root containers, privilege escalation, and 100+ other rules

**Control Plane Access:**

- HTTPS access to Artifact Endpoint

## K8s Identity & Entitlements Management

**Deployment Mode:**
Kubernetes cronjob

**Helm Command:**

```bash
helm upgrade --install kiem-job oci://public.ecr.aws/k9v9d5v2/kiem-job \
--set accuknox.label="[LABEL]" \
--version v1.1.3 \
--set accuknox.URL="cspm.demo.accuknox.com" \
--set accuknox.authToken="[AUTHTOKEN]" \
--set accuknox.cronTab="30 9 * * *" \
--set accuknox.clusterName="[CLUSTERNAME]" \
```

**Features:**

- Identifies overly permissive role bindings
- Graph-based identity view
- Detection of dangling service accounts and cross-namespace access

**Control Plane Access:**

- HTTPS access to Artifact Endpoint

## K8s CIS Benchmarking

**Deployment Mode:**
Kubernetes cronjob

**Helm Command:**

```bash
helm upgrade --install cis-k8s-job oci://public.ecr.aws/k9v9d5v2/cis-k8s-job \
--set accuknox.url="cspm.demo.accuknox.com" \
--set accuknox.authToken="[AUTHTOKEN]" \
--set accuknox.cronTab="30 9 * * *" \
--set accuknox.clusterName="[CLUSTERNAME]" \
--set accuknox.label="[LABEL]" \
--version v1.1.3
```

**Features:**

- Benchmarks support for:

  - Kubernetes (generic)
  - EKS
  - AKS
  - GKE

- OKE not currently supported

**Control Plane Access:**

- HTTPS access to Artifact Endpoint

## DISA STIGs Support

**Deployment Mode:**
Kubernetes cronjob

**Helm Command:**

```bash
helm upgrade --install k8s-stig-job oci://public.ecr.aws/k9v9d5v2/k8s-stig-job \
--set accuknox.url="cspm.demo.accuknox.com" \
--set accuknox.authToken="[AUTHTOKEN]" \
--set accuknox.cronTab="30 9 * * *" \
--set accuknox.clusterName="[CLUSTERNAME]" \
--set accuknox.label="[LABEL]" \
--version v1.1.3
```

**Features:**

- DISA Special Technical Implementation Guidelines (STIGs) compliance

**Control Plane Access:**

- HTTPS access to Artifact Endpoint

## In-Cluster Container Image Scanning

**Deployment Mode:**
CronJob (per node job)

**Helm Command:**

```bash
helm install kubeshield kubeshield-chart \
--set scan.artifactToken="<TOKEN>" \
--set scan.artifactEndpoint="https://cspm.demo.accuknox.com/api/v1/artifact/" \
--set scan.label="<LABEL>"
```

**Features:**

- Direct in-cluster image scanning (no registry access required)
- Scans cached images on nodes
- Reports sent to AccuKnox console for triage

**Control Plane Access:**

- HTTPS access to Artifact Endpoint

## Admission Controller Support

AccuKnox Admission Controller enforces:

1. Trusted registry enforcement for images
2. Deployment compliance with security best practices (no root, no host mounts, etc.)
3. Violations reported to AccuKnox Control Plane (visible under Monitors & Alerts)

## Cluster Access to Control Plane

Each feature requires outbound (egress) HTTPS access only.
Refer to the access notes under each feature for exact service and port requirements.

<img src="https://i.ibb.co/Z1wCCbhv/Screenshot-2025-06-03-203641.png" alt="Screenshot-2025-06-03-203641" border="0">

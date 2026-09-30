---
title: "UAE Islamic Bank Cuts Azure Compliance Drift to a Single Dashboard"
subtitle: "Surfaces 300+ Findings Across 6 Azure Subscriptions in the First Assessment"
slug: "uae-islamic-bank-azure-compliance"
url: "https://accuknox.com/case-studies/uae-islamic-bank-azure-compliance"
customer: "UAE Islamic Bank"
anonymized: true
internal_customer_name: "[the real bank name, for the leak check only]"
sector: "banking"
region: "UAE"
environment: "Azure, AKS, Azure Container Registry"
deployment: "SaaS with agentless assessment"
scale: "6 Azure subscriptions, 4 AKS production clusters"
modules: ["CSPM", "KSPM", "CWPP"]
compliance: ["Azure CIS", "PCI DSS", "SOC 2 Type II"]
replaced: ""
excerpt: "A Sharia-compliant bank running AKS in production had no continuous posture check across six Azure subscriptions. The first agentless assessment returned 300+ findings."
pdf: "[confirm whether marketing produced a PDF for this story]"
---

# UAE Islamic Bank Cuts Azure Compliance Drift to a Single Dashboard

## Surfaces 300+ Findings Across 6 Azure Subscriptions in the First Assessment

**Environment:** Azure, AKS, Azure Container Registry
**Deployment:** SaaS, agentless assessment
**Scale:** 6 subscriptions, 4 AKS production clusters

AccuKnox delivers a Cloud Native Application Protection Platform (CNAPP) built
for regulated financial institutions. This UAE-based Islamic bank runs
Sharia-compliant banking services on Azure Kubernetes Service and had to prove
continuous conformance to Azure CIS, PCI DSS and SOC 2 Type II. Its auditors
wanted evidence between audits, not a snapshot taken the week before one.

## Challenges

- **Posture checked once a quarter, drifting daily.** Six Azure subscriptions
  were assessed manually against Azure CIS, PCI DSS and SOC 2 Type II, so
  configuration drift between assessments went unrecorded and unexplained.
- **AKS production workloads ran without runtime security.** Four production
  clusters had no in-cluster detection, which left the bank unable to answer
  what a compromised pod had actually done.
- **Container images reached production unscanned.** Images pushed to Azure
  Container Registry had no CVE assessment gate, so a vulnerable base layer
  could ship without anyone knowing it had.
- **Agents were not an option on regulated workloads.** Change control on
  Sharia-compliant banking systems ruled out installing anything on production
  hosts before the security value was proven.

## Solutions

- Deployed AccuKnox CSPM across all 6 Azure subscriptions for continuous
  benchmarking against Azure CIS, PCI DSS and SOC 2 Type II controls, replacing
  the quarterly manual review.
- Implemented KSPM on the 4 AKS clusters to harden cluster configuration
  against the CIS Kubernetes Benchmark and flag drift as it happened.
- Activated CWPP runtime protection using eBPF and LSM enforcement, giving the
  security team process, file and network visibility inside running pods
  without a kernel module.
- Integrated container image scanning with Azure Container Registry so every
  image is assessed for CVEs before it reaches a cluster.
- Ran the first assessment agentlessly across all subscriptions, which
  surfaced the initial finding set with no change request against production.

“We went from a quarterly spreadsheet to a dashboard the audit team can open
themselves. The first agentless run told us more about our Azure estate in two
days than the last review cycle did in a quarter.”

Security Leadership

UAE Islamic Bank

## Outcomes

- **300+ unique findings** surfaced in the first agentless assessment across 6
  subscriptions, with zero production change requests.
- **4 AKS clusters** brought under continuous KSPM benchmarking and runtime
  enforcement.
- **3 frameworks** monitored continuously rather than quarterly: Azure CIS, PCI
  DSS and SOC 2 Type II.
- **Container image scanning gated at the registry**, so an unassessed image no
  longer reaches a production cluster.
- **Audit evidence generated on demand**, which removed the manual collection
  step from every review cycle.

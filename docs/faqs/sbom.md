---
title: SBOM FAQs
description: Frequently asked questions about AccuKnox SBOM and supply chain risk management.
hide:
  - toc
---

# SBOM (Software Bill of Materials)

!!! note
    This FAQ is written around SBOM, but most of it applies equally to the wider **xBOM** family (SBOM, CBOM, AIBOM). See the [xBOM overview](https://help.accuknox.com/getting-started/xbom-setup/) for the full picture.

??? "**1. Why is SBOM important for my software supply chain?**"
    An SBOM provides a complete inventory of software components, dependencies, and versions used by an application. AccuKnox uses SBOMs to detect vulnerable libraries, verify component provenance, and reduce supply chain risk across CI/CD and runtime.

??? "**2. Which SBOM formats does AccuKnox support?**"
    AccuKnox supports standard SBOM formats such as CycloneDX and SPDX. This allows teams to ingest SBOMs from common tools and pipelines without needing custom translation.

??? "**3. How do I generate a BOM?**"
    You can generate a BOM (SBOM, CBOM, or AIBOM) in three ways:

    - **AccuKnox CLI (`knoxctl`)** — Scan a filesystem, container image, or AI/ML model locally and push results straight to your tenant. See [Generate via knoxctl](https://help.accuknox.com/getting-started/xbom-knoxctl/).
    - **CI/CD pipeline** — Drop the AccuKnox xBOM Scan Action (or container image scan) into GitHub Actions, Jenkins, or similar to generate a BOM on every build. See [Generate via GitHub Actions](https://help.accuknox.com/getting-started/xbom-github-actions/).
    - **Third-party tools** — Generate a CycloneDX or SPDX BOM with tools like Syft or Trivy, then upload it to AccuKnox for scanning.

??? "**4. How do I onboard SBOMs into AccuKnox?**"
    Create an SBOM project in the AccuKnox UI, upload your SBOM file, or automate ingestion through CI/CD workflows. Once onboarded, AccuKnox scans the SBOM for vulnerabilities, license issues, and dependency risk.

??? "**5. Can SBOM results be linked to vulnerability scanning and policy enforcement?**"
    Yes. SBOM findings can be combined with vulnerability data to show which components are risky and support enforcement rules in CI/CD. Teams can use SBOM-based policies to block builds or deployments when high-risk components are present.

??? "**6. How does AccuKnox help with SBOM change tracking?**"
    AccuKnox tracks SBOM updates over time so you can compare component lists across versions. This helps identify new dependencies, removed packages, and unexpected supply chain changes before they reach production.

??? "**7. What is the difference between Strong Copyleft and Weak Copyleft licenses?**"
    AccuKnox classifies license findings into four severity levels. These levels are not defined by any official standard but reflect commonly accepted risk classifications in the industry.

    | Severity | License Type | Classification | Example Licenses | Risk |
    |---|---|---|---|---|
    | **Low** | Permissive | Notice, Permissive, Unencumbered | MIT, BSD-2-Clause, BSD-3-Clause, Apache-2.0, ISC, Zlib, Boost Software License 1.0, Unlicense | No major restrictions; minimal obligations (e.g., attribution required) |
    | **Medium** | Weak Copyleft | Reciprocal | LGPL-2.1, LGPL-3.0, MPL-1.1, MPL-2.0, CDDL-1.0, EPL-1.0, EPL-2.0 | Requires source disclosure if modified, but allows proprietary linking |
    | **High** | Strong Copyleft | Restricted | GPL-2.0, GPL-3.0, AGPL-3.0, OSL-3.0, EUPL-1.2, CeCILL-2.1 | Requires derivative works to be open-sourced under the same license; may include patent clauses |
    | **Critical** | Banned / Incompatible / Proprietary | Forbidden | SSPL, JSON License, Creative Commons Non-Commercial (CC-NC), Microsoft Shared Source, Oracle Binary Code License, Proprietary EULAs, Unclear or Custom Licenses | May impose non-commercial use restrictions, require revenue sharing, or be legally unclear |

    The key distinction between Strong and Weak Copyleft:

    - **Weak Copyleft** (e.g., LGPL, MPL): Copyleft applies only to the licensed component itself. You can link it into proprietary software without being required to open-source your application code.
    - **Strong Copyleft** (e.g., GPL, AGPL): Copyleft extends to the entire combined work. If you distribute software that incorporates a GPL-licensed component, your full codebase must be released under a compatible open-source license. AGPL adds a network-use clause, so even SaaS deployments that never distribute binaries are affected.

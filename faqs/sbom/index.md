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
    An SBOM is a **complete inventory** of the software components, dependencies and versions in an application. AccuKnox uses SBOMs across CI/CD and runtime to:

    - **Find vulnerabilities**: Detect vulnerable libraries.
    - **Check provenance**: Verify where each component comes from.
    - **Cut risk**: Reduce supply chain risk.

??? "**2. Which SBOM formats does AccuKnox support?**"
    AccuKnox supports standard SBOM formats such as **CycloneDX and SPDX**. Teams can ingest SBOMs from common tools and pipelines with no custom translation.

??? "**3. How do I generate a BOM?**"
    You can generate a BOM (SBOM, CBOM or AIBOM) in **three ways**:

    - **AccuKnox CLI (`knoxctl`)**: Scan a filesystem, container image or AI/ML model locally. Push the results straight to your tenant. See [Generate via knoxctl](https://help.accuknox.com/getting-started/xbom-knoxctl/).
    - **CI/CD pipeline**: Add the AccuKnox xBOM Scan Action (or container image scan) to GitHub Actions, Jenkins or similar. It generates a BOM on every build. See [Generate via GitHub Actions](https://help.accuknox.com/getting-started/xbom-github-actions/).
    - **Third-party tools**: Generate a CycloneDX or SPDX BOM with tools like Syft or Trivy. Then upload it to AccuKnox for scanning.

??? "**4. How do I onboard SBOMs into AccuKnox?**"
    Create an **SBOM project** in the AccuKnox UI. Then upload your SBOM file, or automate ingestion through CI/CD workflows. After onboarding, AccuKnox scans the SBOM for vulnerabilities, license issues and dependency risk.

??? "**5. Can SBOM results be linked to vulnerability scanning and policy enforcement?**"
    Yes. AccuKnox combines SBOM findings with vulnerability data to show which components are risky. These findings support enforcement rules in CI/CD. Teams can use **SBOM-based policies** to block builds or deployments that contain high-risk components.

??? "**6. How does AccuKnox help with SBOM change tracking?**"
    AccuKnox **tracks SBOM updates over time**, so you can compare component lists across versions. Before changes reach production, you can spot:

    - **New dependencies**: Components added in a new version.
    - **Removed packages**: Packages dropped from a new version.
    - **Unexpected changes**: Supply chain changes you did not expect.

??? "**7. What is the difference between Strong Copyleft and Weak Copyleft licenses?**"
    The difference is **scope**. Weak Copyleft covers only the licensed component. Strong Copyleft covers the entire combined work.

    AccuKnox classifies license findings into four severity levels. No official standard defines these levels. They reflect commonly accepted risk classifications in the industry.

    | Severity | License Type | Classification | Example Licenses | Risk |
    |---|---|---|---|---|
    | **Low** | Permissive | Notice, Permissive, Unencumbered | MIT, BSD-2-Clause, BSD-3-Clause, Apache-2.0, ISC, Zlib, Boost Software License 1.0, Unlicense | No major restrictions; minimal obligations (e.g., attribution required) |
    | **Medium** | Weak Copyleft | Reciprocal | LGPL-2.1, LGPL-3.0, MPL-1.1, MPL-2.0, CDDL-1.0, EPL-1.0, EPL-2.0 | Requires source disclosure if modified, but allows proprietary linking |
    | **High** | Strong Copyleft | Restricted | GPL-2.0, GPL-3.0, AGPL-3.0, OSL-3.0, EUPL-1.2, CeCILL-2.1 | Requires derivative works to be open-sourced under the same license; may include patent clauses |
    | **Critical** | Banned / Incompatible / Proprietary | Forbidden | SSPL, JSON License, Creative Commons Non-Commercial (CC-NC), Microsoft Shared Source, Oracle Binary Code License, Proprietary EULAs, Unclear or Custom Licenses | May impose non-commercial use restrictions, require revenue sharing, or be legally unclear |

    The key distinction between Strong and Weak Copyleft:

    - **Weak Copyleft** (e.g., LGPL, MPL): Copyleft applies only to the licensed component itself. You can link it into proprietary software and keep your application code closed.
    - **Strong Copyleft** (e.g., GPL, AGPL): Copyleft extends to the entire combined work. If you distribute software with a GPL-licensed component, you must release your full codebase under a compatible open-source license. AGPL adds a network-use clause, so it also affects SaaS deployments that never distribute binaries.

---
title: "A Global Bank Chose AccuKnox for SBOM Security, and the Driver Was Not One Country's Mandate"
seo_title: "Global Bank SBOM and Supply Chain Security with AccuKnox"
meta_description: "A top global bank signed a three-year deal for SBOM security. The reason is a wave of converging regulations and a supply-chain threat the numbers make plain."
slug: "global-bank-sbom-supply-chain-security"
url: "https://accuknox.com/blog/global-bank-sbom-supply-chain-security"
primary_keyword: "global bank SBOM security"
secondary_keywords: ["software supply chain security banks", "EU Cyber Resilience Act SBOM", "xBOM", "SBOM compliance NTIA minimum elements"]
excerpt: "A top global bank signed a three-year engagement with AccuKnox for SBOM and supply chain security. The driver is a wave of converging regulations, not any single mandate."
category: "ASPM"
author: "Atharva Shah"
reading_time: "5 minutes"
word_count_target: 1150
audience: "security lead | platform engineer"
cover_image_prompt_claude: >
  An isometric illustration of a bank building connected to a pipeline of software
  components, each tagged with a bill-of-materials label, an admission gate before a
  cluster. AccuKnox navy #11206D on white with #003BF6 accents, flat vector, generous
  negative space, no text in the image.
cover_image_prompt_midjourney: >
  isometric bank building connected to software component pipeline, BOM tags, admission gate
  before a cluster, navy #11206D white #003BF6, flat vector, negative space
  --ar 16:9 --style raw --v 6 --no text
---

# A global bank chose AccuKnox for SBOM security, and no single mandate is the reason

> **Cover image prompt:** A bank building connected to a pipeline of tagged software components, an admission gate before a cluster. AccuKnox navy `#11206D` on white with `#003BF6` accents, flat vector, no text.

## TL;DR

- This global bank SBOM security win is a preview of the market: one of the world's largest banks, operating across roughly 50 countries, signed a three-year engagement with AccuKnox for SBOM and software supply chain security, selecting the platform after a technical evaluation rather than a drawn-out proof of concept.
- The driver is a wave of converging regulation. US [Executive Order 14028](https://www.federalregister.gov/documents/2021/05/17/2021-10460/improving-the-nations-cybersecurity), the [NTIA minimum elements](https://www.ntia.gov/sites/default/files/publications/sbom_minimum_elements_report_0.pdf), NIST SSDF, and the [EU Cyber Resilience Act](https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act) all now expect a software bill of materials.
- The threat is not subtle. Sonatype counted more than 454,600 new malicious open-source packages in 2025, and Gartner predicted 45% of organisations would face a software supply chain attack by 2025.
- Generating a bill of materials is the easy part. The bank bought lifecycle management: ingestion of vendor BOMs, transitive dependency mapping, admission control, and runtime enforcement.
- Output runs in both SPDX and CycloneDX, and coverage extends past software to cryptography, AI models, and hardware through [xBOM](https://accuknox.com/blog/xbom-security-explained).

## What the bank actually bought

The bank did not buy a file generator. It selected AccuKnox for supply chain security across a three-year term, and the deciding factor was that the platform covers the whole lifecycle rather than the first step of it. A technical demo was enough, with no prolonged evaluation, because the capability the bank cared about was what happens after a BOM exists.

That capability is what most SBOM programs lack. A tool that emits a clean CycloneDX file and stops has told you what shipped, not what to do about it. The bank's requirement was continuous: hold visibility of every component across every application, refresh the record when software changes, ingest and validate the BOMs its own vendors send in, and block a workload that fails policy before it deploys. The last of those, vendor BOM ingestion, is the part most institutions have no process for at all.

> **Existing screenshot (inline 1):** Use an SBOM inventory view from the PRODUCT UI library, `sbom/SBOM_1.png`. Crop the browser chrome and redact any tenant name before publishing.
>
> *Caption: A generated SBOM in the AccuKnox platform, carrying component, version, and supplier fields per record.*

## The regulations converged on the same requirement

An SBOM is no longer a US federal ask. Four instruments, on two continents, now expect one.

| Framework | What it requires | Status |
| --- | --- | --- |
| US EO 14028 | Software sold to the federal government must provide an SBOM | Signed May 2021 |
| NTIA minimum elements | Seven data fields per component, in SPDX, CycloneDX, or SWID | Published July 2021 |
| NIST SSDF (SP 800-218) | Secure development practices, a common vocabulary for suppliers | Published Feb 2022 |
| EU Cyber Resilience Act | Manufacturers must draw up an SBOM for products with digital elements | Main obligations from Dec 2027 |

The [NTIA minimum elements](https://www.ntia.gov/sites/default/files/publications/sbom_minimum_elements_report_0.pdf) set the practical bar every one of these leans on: each component needs a supplier, a name, a version, a unique identifier, its dependency relationships, the author of the BOM data, and a timestamp. The EU CRA, Regulation (EU) 2024/2847, entered into force in December 2024, with reporting obligations from September 2026 and the main manufacturer obligations from December 2027. A bank building software or buying it in the EU is now in scope on a fixed clock. [CISA's 2025 refresh](https://www.cisa.gov/sbom) of the minimum elements shows the bar is still rising, not settling.

## The threat behind the mandates is measurable

Regulators are reacting to a real trend. Sonatype's [2026 State of the Software Supply Chain](https://www.sonatype.com/state-of-the-software-supply-chain/2026/open-source-malware) identified more than 454,600 new malicious packages in 2025 alone, pushing the cumulative total past 1.233 million across npm, PyPI, Maven Central, NuGet, and Hugging Face. [Gartner predicted](https://www.gartner.com/en/newsroom/press-releases/2022-03-07-gartner-identifies-top-security-and-risk-management-trends-for-2022) that by 2025, 45% of organisations worldwide would have experienced an attack on their software supply chain, a threefold rise from 2021.

For a bank, the exposure is rarely a direct dependency the team chose. It arrives through the libraries those libraries pull in, the transitive layer nobody reviewed. That is exactly why the standards require full dependency graphs rather than a flat component list.

> **Image prompt (inline 2):** A dependency graph with direct dependencies near a root node and deeper transitive nodes flagged red, one shared library linked to multiple parents. AccuKnox navy `#11206D` on white with `#003BF6` accents, flat vector, no text in the image.
>
> *Caption: Transitive dependencies are where the exposure sits, and where a flat SBOM stops looking.*

## SBOM is table stakes, xBOM is the real scope

The bank's form treated software as the starting point, not the whole job. AccuKnox generates SBOM automatically and extends the same toolchain to the wider family: CBOM for cryptography, AI-BOM for models and datasets, and HBOM for hardware. That matters because a 2026 supply chain program that covers only software is one audit cycle away from being reopened. The [xBOM approach](https://accuknox.com/blog/xbom-unifies-supply-chain-security) unifies the set under one inventory.

Every record comes out in both SPDX and CycloneDX. SPDX is an international standard, ISO/IEC 5962:2021, stewarded through the Linux Foundation, and [CycloneDX](https://cyclonedx.org/) is stewarded by OWASP. Emitting both means the bank can hand a regulator or a customer whichever format the request names, without regenerating anything.

## A BOM in a directory changes nothing, enforcement does

Generation is where most programs stop, and it is where risk starts. AccuKnox carries the record forward into the pipeline. Artefacts from the repository, container images, and packages feed a signing step that produces signed releases. The platform then runs BOM analysis, license verification, and risk prioritisation, mapping CVEs onto components by severity and exploitability.

Two controls turn the inventory into a gate. An [admission controller](https://accuknox.com/solutions/sbom) checks the BOM before a workload deploys, so a workload with no BOM or a disallowed license never reaches the cluster. [Runtime enforcement](https://accuknox.com/platform/runtime-security) then holds the deployed state against the recorded BOM, catching drift after deployment. That chain is also what moves a build platform up the SLSA levels, from signed provenance toward hermetic builds and full pipeline security.

License risk rides the same graph. An open-source component that quietly moved from a permissive license to a commercial one surfaces here, at build time, rather than in a legal review two years later.

## Buy for the lifecycle, not the file

The global bank's decision is a preview of the market. The regulations have converged, the threat data is unambiguous, and the file itself is a commodity. What separates a compliant program from a checkbox is whether the BOM drives ingestion, dependency analysis, admission control, and runtime enforcement, across software, cryptography, AI, and hardware. Buy for that lifecycle, and the audit answers itself.

## See the full xBOM coverage in one place

This overview walks through generating SBOM, HBOM, CBOM, QBOM, and AI-BOM from one toolchain.

```html
<iframe width="560" height="315" src="https://www.youtube.com/embed/g11StLuF9bA" title="AccuKnox xBOM - Complete SBOM, HBOM, CBOM, QBOM and AI-BOM Coverage" frameborder="0" allowfullscreen></iframe>
```

[Watch it on the AccuKnox YouTube channel](https://www.youtube.com/watch?v=g11StLuF9bA).

## FAQs

### Do banks outside the US and EU need an SBOM?

Increasingly, yes. SBOM expectations now appear in US federal procurement, the EU Cyber Resilience Act, and a growing set of national frameworks. A global bank faces the strictest of them.

### What is the difference between SBOM and xBOM?

SBOM lists software components. xBOM is the umbrella for the related records: CBOM for cryptography, AI-BOM for models and datasets, and HBOM for hardware.

### Which SBOM formats does AccuKnox produce?

Both SPDX, an international standard as ISO/IEC 5962:2021, and CycloneDX, stewarded by OWASP. Each record carries the NTIA minimum elements and a unique identifier per component.

### Why is admission control part of an SBOM program?

Because a BOM only describes software. An admission controller uses it as a gate, blocking a workload with no BOM or a disallowed license before it deploys, and runtime enforcement keeps the running state matching the record.

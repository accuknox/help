---
title: SARIF Findings
description: Learn how to import and manage SARIF findings in AccuKnox to consolidate security results from various tools.
---

# SARIF Findings

SARIF (Static Analysis Results Interchange Format) is a standard format from various tools and helps to triage the findings. AccuKnox supports importing findings in the SARIF format, allowing you to consolidate security results from various tools into a single platform.

By integrating SARIF findings, you can visualize and manage security issues identified by third-party scanners alongside AccuKnox's native findings. This integration is typically set up using a workflow to ingest the SARIF files.

AccuKnox supports importing SARIF findings from any tool that produces output in SARIF format. Some common platforms that export SARIF include:

- **Sonatype**
- **Jfrog**
- **Gitleaks**
- **Checkmarx**
- **Any Other That Produces SARIF**

We can import these findings and display them within the AccuKnox platform, providing a unified view of your security posture.

![SARIF findings unified view in AccuKnox platform](image-20.png)

AccuKnox allows you to group and filter SARIF findings based on various attributes such as severity, tool name, and file location. This helps you prioritize and address security issues effectively. You also get the benefit of AccuKnox's advanced analytics, AI assisted remediation, and reporting capabilities to gain insights into your security landscape.

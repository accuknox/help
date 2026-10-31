# Evidence log, AccuKnox vs Wiz, Palo Alto Networks and SentinelOne (CNAPP)

Pages read on 2026-10-16 with Firecrawl. AccuKnox pages were read live on help.accuknox.com. Saved copies sit in `research/raw/`. `validate_evidence.py` checks that every quote below appears in its saved page.
Wiz and SentinelOne technical docs need a login, so those columns use public product pages, blogs and the Wiz AWS Marketplace listing.
A cell marked Not compared with no text makes no claim. The PDF contains no claim about what a vendor lacks, except the Palo Alto statement quoted for SAST.

| Row | Cell | Relation to AccuKnox | PDF text | Source | Quote |
|---|---|---|---|---|---|
| Agentless cloud posture | AccuKnox |  | Agentless, read-only, AWS and Azure | https://help.accuknox.com/faqs/cspm/ | CSPM is agentless and uses cloud APIs |
| Agentless cloud posture | AccuKnox |  | Agentless, read-only, AWS and Azure | https://help.accuknox.com/faqs/cspm/ | supports AWS, Azure, and GCP |
| Agentless cloud posture | Wiz | Matches | Agentless, 2,800+ configuration rules | https://www.wiz.io/solutions/cspm | Wiz connects in minutes using CSP's APIs |
| Agentless cloud posture | Wiz | Matches | Agentless, 2,800+ configuration rules | https://www.wiz.io/solutions/cspm | 2,800+ cloud configuration rules, including KSPM rules |
| Agentless cloud posture | Palo Alto Networks | Matches | Agentless posture in Cortex Cloud | https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/get-started/understand-license-plans | Agentless comprehensive visibility across your cloud environment |
| Agentless cloud posture | SentinelOne | Matches | Agentless, 2,000+ built-in policies | https://www.sentinelone.com/platform/singularity-cloud-cspm/ | 2,000+ built-in policy assessments |
| Compliance frameworks | AccuKnox |  | 33+ frameworks | https://help.accuknox.com/faqs/compliance/ | 33+ compliance frameworks |
| Compliance frameworks | Wiz | Competitor leads | 100+ frameworks | https://www.wiz.io/solutions/compliance | 100+ Built-In Frameworks |
| Compliance frameworks | Palo Alto Networks | Matches | Built-in and custom standards | https://docs.prismacloud.io/content-collections/compliance/compliance-standards | built-in and custom standards |
| Compliance frameworks | SentinelOne | Matches | CIS, SOC 2, NIST, EU AI Act | https://www.sentinelone.com/platform/singularity-cloud-cspm/ | CIS, SOC 2, the EU AI Act, and NIST |
| Attack-path context | AccuKnox |  | Security Graph on AWS and Azure findings | https://help.accuknox.com/getting-started/3.6-release/ | asset to asset, and asset to finding |
| Attack-path context | AccuKnox |  | Security Graph on AWS and Azure findings | https://help.accuknox.com/getting-started/3.6-release/ | It covers cloud findings on AWS, Azure, and GCP |
| Attack-path context | Wiz | Matches | Security Graph, attack paths | https://www.wiz.io/platform | Attack path analysis |
| Attack-path context | Palo Alto Networks | Matches | Graph rules find attack paths | https://cortex-docs.paloaltonetworks.com/cortex-xsiam/cloud-security/rules-and-policies/cloud-security-rules-and-policies/create-and-manage-cloud-security-rules/create-a-graph-rule | identify risky relationships and attack paths |
| Attack-path context | SentinelOne | Competitor leads | Tests which exposures are exploitable | https://www.sentinelone.com/platform/cloud-native-security/ | validating which exposures are truly exploitable with the Offensive Security Engine |
| Data security (DSPM) | AccuKnox |  | Scanner runs in your cloud account | https://help.accuknox.com/getting-started/dspm-overview/ | The scanner runs on a machine you own |
| Data security (DSPM) | AccuKnox |  | Scanner runs in your cloud account | https://help.accuknox.com/getting-started/dspm-overview/ | sends only a findings file to the AccuKnox console |
| Data security (DSPM) | Wiz | Matches | Agentless discovery, access governance | https://www.wiz.io/solutions/dspm | Continuous agentless discovery of your sensitive data |
| Data security (DSPM) | Wiz | Matches | Agentless discovery, access governance | https://www.wiz.io/solutions/dspm | Data access management and governance |
| Data security (DSPM) | Palo Alto Networks | Matches | Included in Cortex Runtime Security | https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/cortex-data-security/what-is-cortex-cloud-data-security | Cortex Data Security is included with your Cloud Runtime Security license |
| Data security (DSPM) | SentinelOne | Matches | DSPM with attack-path context | https://www.sentinelone.com/platform/cloud-native-security/ | integrates DSPM with Attack Path Analysis |
| AI posture on AWS and Azure | AccuKnox |  | Finds SageMaker, Bedrock, Azure OpenAI | https://help.accuknox.com/faqs/ai-security/ | automatically discovers SageMaker endpoints, Bedrock model deployments |
| AI posture on AWS and Azure | AccuKnox |  | Finds SageMaker, Bedrock, Azure OpenAI | https://help.accuknox.com/faqs/ai-security/ | Discovers Azure AI Foundry, Azure OpenAI Service, Copilot Studio agents |
| AI posture on AWS and Azure | Wiz | Matches | AI-BOM finds SageMaker, OpenAI | https://www.wiz.io/solutions/ai-spm | including managed services such as AWS SageMaker, OpenAI |
| AI posture on AWS and Azure | Palo Alto Networks | Matches | Cortex AI-SPM inventories models | https://www.paloaltonetworks.com/cortex/cloud/ai-security-posture-management | See all AI models in your cloud environment |
| AI posture on AWS and Azure | SentinelOne | Matches | AI models, services, data flows | https://www.sentinelone.com/platform/cloud-native-security/ | provides visibility into AI models, services, and data flows |
| AI runtime guardrails | AccuKnox |  | Prompt Firewall, ModelArmor, red teaming | https://help.accuknox.com/faqs/ai-security/ | Prompt Firewall |
| AI runtime guardrails | AccuKnox |  | Prompt Firewall, ModelArmor, red teaming | https://help.accuknox.com/faqs/ai-security/ | ModelArmor |
| AI runtime guardrails | AccuKnox |  | Prompt Firewall, ModelArmor, red teaming | https://help.accuknox.com/faqs/ai-security/ | Automated Red Teaming |
| AI runtime guardrails | Wiz | Matches | Detects prompt injection at runtime | https://www.wiz.io/solutions/ai-spm | Detect prompt injection, rogue agents, and malicious behavior targeting AI systems |
| AI runtime guardrails | Palo Alto Networks | Matches | Prisma AIRS blocks prompt injections | https://www.paloaltonetworks.com/ai-security/prisma-airs | blocks prompt injections and data leaks |
| AI runtime guardrails | SentinelOne | Matches | Prompt Security AI firewall | https://www.sentinelone.com/platform/securing-ai-prompt/ | real-time AI firewall |
| SAST | AccuKnox |  | 14 languages on two engines | https://help.accuknox.com/support-matrix/sast-support-matrix/ | across two scanning engines |
| SAST | AccuKnox |  | 14 languages on two engines | https://help.accuknox.com/support-matrix/sast-support-matrix/ | Kotlin |
| SAST | Wiz | Matches | Rule-based and agentic SAST | https://www.wiz.io/solutions/sast | Wiz combines rule-based and agentic SAST |
| SAST | Palo Alto Networks | AccuKnox leads | No native SAST in Cortex Cloud | https://cortex-docs.paloaltonetworks.com/application-security/application-security-posture-management-aspm/manage-code-weakness-issues | Currently, Cortex Cloud does not support native SAST scanners |
| DAST | AccuKnox |  | Four scan types, AI Pentesting (Beta) | https://help.accuknox.com/how-to/dast-scan-types/ | Four scan types are available |
| DAST | AccuKnox |  | Four scan types, AI Pentesting (Beta) | https://help.accuknox.com/how-to/dast-scan-types/ | Try AI Pentesting (Beta) |
| DAST | Wiz | Matches | Red Agent includes API DAST, GA | https://www.wiz.io/blog/wiz-red-agent-is-ga | API DAST Attacker |
| DAST | Wiz | Matches | Red Agent includes API DAST, GA | https://www.wiz.io/blog/wiz-red-agent-is-ga | is now generally available (GA) |
| IaC, secrets, SCA, SBOM | AccuKnox |  | IaC incl. Bicep and ARM, reads CycloneDX and SPDX | https://help.accuknox.com/support-matrix/iac/ | Bicep |
| IaC, secrets, SCA, SBOM | AccuKnox |  | IaC incl. Bicep and ARM, reads CycloneDX and SPDX | https://help.accuknox.com/support-matrix/iac/ | Terraform |
| IaC, secrets, SCA, SBOM | AccuKnox |  | IaC incl. Bicep and ARM, reads CycloneDX and SPDX | https://help.accuknox.com/faqs/sbom/ | CycloneDX and SPDX |
| IaC, secrets, SCA, SBOM | Wiz | Matches | IaC, secrets, SCA and SBOM | https://www.wiz.io/platform/wiz-code | Secrets Scanning |
| IaC, secrets, SCA, SBOM | Wiz | Matches | IaC, secrets, SCA and SBOM | https://www.wiz.io/platform/wiz-code | SCA & SBOM |
| IaC, secrets, SCA, SBOM | Palo Alto Networks | Matches | IaC, SCA, secrets, CycloneDX export | https://docs.prismacloud.io/content-collections/application-security/supported-technologies | Bicep |
| IaC, secrets, SCA, SBOM | Palo Alto Networks | Matches | IaC, SCA, secrets, CycloneDX export | https://docs.prismacloud.io/content-collections/runtime-security/vulnerability-management/exporting-sboms | CycloneDX v1.4 standard |
| IaC, secrets, SCA, SBOM | SentinelOne | Matches | Secrets, IaC and image scans | https://www.sentinelone.com/platform/cloud-native-security/ | continuous scanning of repositories, IaC templates, and container images |
| Runtime prevention | AccuKnox |  | KubeArmor, open source, inline blocking | https://help.accuknox.com/faqs/runtime-security/ | Inline Mitigation |
| Runtime prevention | AccuKnox |  | KubeArmor, open source, inline blocking | https://help.accuknox.com/faqs/general/ | CNCF Sandbox project with 2 million+ downloads |
| Runtime prevention | Wiz | Matches | eBPF Sensor blocks threats | https://www.wiz.io/solutions/runtime-sensor | The sensor blocks sophisticated cloud and AI threats in real time |
| Runtime prevention | Palo Alto Networks | Matches | Defender blocks or alerts | https://docs.prismacloud.io/content-collections/runtime-security/install/deploy-defender/host/host-defender-architecture | actively blocking or alerting according to the rules defined in Console |
| Runtime prevention | SentinelOne | Matches | eBPF agent, automated response | https://www.sentinelone.com/platform/singularity-cloud-workload-security | eBPF-based approach |
| Runtime prevention | SentinelOne | Matches | eBPF agent, automated response | https://www.sentinelone.com/platform/singularity-cloud-workload-security | automated containment and rollback |
| Cloud detection and response | AccuKnox |  | Reads CloudTrail, auto-remediates | https://help.accuknox.com/use-cases/cdr/ | ingests cloud logs (CloudTrail, Audit Logs) |
| Cloud detection and response | AccuKnox |  | Reads CloudTrail, auto-remediates | https://help.accuknox.com/use-cases/cdr/ | via CI/CD or Webhooks |
| Cloud detection and response | Wiz | Matches | Wiz Defend reads cloud logs | https://www.wiz.io/platform/wiz-defend | deep analysis of cloud & SaaS logs |
| Cloud detection and response | Palo Alto Networks | Matches | Cortex Runtime Security lists CDR | https://www.paloaltonetworks.com/cortex/cloud/runtime-security | Cloud Detection & Response (CDR) |
| Cloud detection and response | SentinelOne | Matches | Hyperautomation for cloud events | https://www.sentinelone.com/platform/cloud-native-security/ | Respond to misconfigurations, alerts, and cloud events with pre-built or custom Hyperautomation workflows |
| Where the platform runs | AccuKnox |  | SaaS, on-prem or air-gapped | https://help.accuknox.com/faqs/deployment/ | Full On-premises or Air-gapped |
| Where the platform runs | Wiz | Not compared | SaaS, sold on AWS Marketplace | https://aws.amazon.com/marketplace/pp/prodview-ibgbkrqusncsm | Software as a Service (SaaS) |
| Where the platform runs | Palo Alto Networks | AccuKnox leads | Enterprise Edition is SaaS | https://docs.prismacloud.io/content-collections/get-started/welcome-to-prisma-cloud | SaaS (Prisma Cloud Enterprise Edition) |
| Where the platform runs | Palo Alto Networks | AccuKnox leads | Enterprise Edition is SaaS | https://docs.prismacloud.io/content-collections/administration/prisma-cloud-licenses | workload protection for hosts, containers, and serverless deployments |

## Module fit

| Module | PDF text | Source | Quote |
|---|---|---|---|
| CSPM and KSPM | Licensed by: Cloud assets as units | https://help.accuknox.com/faqs/pricing/ | Number of cloud assets normalized to units |
| Runtime protection | Licensed by: Worker nodes | https://help.accuknox.com/faqs/pricing/ | Number of worker nodes |
| Code scanning and CI/CD | Licensed by: Scanner tools | https://help.accuknox.com/faqs/pricing/ | Number of Tools in SCA, SAST, DAST, IaC |
| DAST and CDR | Licensed by: Scanner tools | https://help.accuknox.com/faqs/pricing/ | Number of Tools in SCA, SAST, DAST, IaC |
| AI security | Licensed by: AI and LLM models | https://help.accuknox.com/faqs/pricing/ | Number of AI/LLM Model |
| SBOM generation | Licensed by: Scanner tools | https://help.accuknox.com/faqs/sbom/ | CycloneDX and SPDX |

## Other claims

| Section | PDF text | Source | Quote |
|---|---|---|---|
| How the others license | AccuKnox: custom quote, pay per module, no hard stop if the quota is exceeded | https://help.accuknox.com/faqs/pricing/ | custom quote |
| How the others license | AccuKnox: custom quote, pay per module, no hard stop if the quota is exceeded | https://help.accuknox.com/faqs/pricing/ | will not stop you from exceeding the quota |
| How the others license | Wiz: base plans on AWS Marketplace, with Sensor, Code and Defend as add-ons | https://aws.amazon.com/marketplace/pp/prodview-ibgbkrqusncsm | Wiz Essential |
| How the others license | Wiz: base plans on AWS Marketplace, with Sensor, Code and Defend as add-ons | https://aws.amazon.com/marketplace/pp/prodview-ibgbkrqusncsm | Add-on for Wiz Advanced |
| How the others license | Wiz: base plans on AWS Marketplace, with Sensor, Code and Defend as add-ons | https://aws.amazon.com/marketplace/pp/prodview-ibgbkrqusncsm | Add-on for Wiz Cloud |
| How the others license | Palo Alto, Cortex Cloud: priced per protected workload, code security is an add-on | https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/get-started/understand-license-plans | The fundamental metric for consumption is the protected workload |
| How the others license | Palo Alto, Cortex Cloud: priced per protected workload, code security is an add-on | https://cortex-docs.paloaltonetworks.com/cortex-xsiam/cloud-security/cortex-cloud-application-security | Application Security Add-on |
| How the others license | Palo Alto, Prisma Cloud: priced in credits | https://docs.prismacloud.io/content-collections/administration/prisma-cloud-licenses | Licensing is sold in increments of 100 credits |
| Where AccuKnox leads | SAST: 14 languages natively. Cortex Cloud has no native SAST scanner | https://help.accuknox.com/support-matrix/sast-support-matrix/ | across two scanning engines |
| Where AccuKnox leads | SAST: 14 languages natively. Cortex Cloud has no native SAST scanner | https://cortex-docs.paloaltonetworks.com/application-security/application-security-posture-management-aspm/manage-code-weakness-issues | Currently, Cortex Cloud does not support native SAST scanners |
| Where AccuKnox leads | Runtime: open-source KubeArmor with inline blocking | https://help.accuknox.com/faqs/general/ | CNCF Sandbox project with 2 million+ downloads |
| Where AccuKnox leads | Runtime: open-source KubeArmor with inline blocking | https://help.accuknox.com/faqs/runtime-security/ | Inline Mitigation |
| Where AccuKnox leads | Data: the DSPM scanner runs in your account and only a findings file leaves | https://help.accuknox.com/getting-started/dspm-overview/ | The scanner runs on a machine you own |
| Where AccuKnox leads | Data: the DSPM scanner runs in your account and only a findings file leaves | https://help.accuknox.com/getting-started/dspm-overview/ | sends only a findings file to the AccuKnox console |
| Where AccuKnox leads | Deployment: SaaS, on-prem or air-gapped. Prisma Cloud Enterprise Edition is SaaS | https://help.accuknox.com/faqs/deployment/ | Full On-premises or Air-gapped |
| Where AccuKnox leads | Deployment: SaaS, on-prem or air-gapped. Prisma Cloud Enterprise Edition is SaaS | https://docs.prismacloud.io/content-collections/get-started/welcome-to-prisma-cloud | SaaS (Prisma Cloud Enterprise Edition) |
| POC, Posture | One AWS account and one Azure subscription, read-only. | https://help.accuknox.com/faqs/cspm/ | read-only |
| POC, Posture | One AWS account and one Azure subscription, read-only. | https://help.accuknox.com/getting-started/3.6-release/ | CloudFormation |
| POC, Data and AI | One S3 bucket and one Blob container. Add AI posture if Bedrock or Azure OpenAI is live. | https://help.accuknox.com/getting-started/dspm-onboarding/ | Blob Storage and ADLS Gen2 |
| POC, Data and AI | One S3 bucket and one Blob container. Add AI posture if Bedrock or Azure OpenAI is live. | https://help.accuknox.com/faqs/ai-security/ | Azure OpenAI Service |
| POC, Code and CI/CD | One or two repositories: SAST, IaC, secrets, SCA. One JFrog registry. | https://help.accuknox.com/faqs/aspm/ | Secrets Scanning |
| POC, Code and CI/CD | One or two repositories: SAST, IaC, secrets, SCA. One JFrog registry. | https://help.accuknox.com/how-to/jfrog-container/ | JFrog |
| POC, Runtime | KubeArmor on one non-production cluster or VM, with one block policy. | https://help.accuknox.com/faqs/runtime-security/ | Inline Mitigation |
| POC, Runtime | KubeArmor on one non-production cluster or VM, with one block policy. | https://help.accuknox.com/faqs/general/ | CNCF Sandbox project with 2 million+ downloads |
| POC timeline | A SaaS proof of concept runs about one to two weeks when the infrastructure is in place | https://help.accuknox.com/faqs/deployment/ | SaaS PoC: |
| POC timeline | A SaaS proof of concept runs about one to two weeks when the infrastructure is in place | https://help.accuknox.com/faqs/deployment/ | 1–2 weeks |
| Pick AccuKnox for | Native SAST, DAST, IaC, secrets and SCA | https://help.accuknox.com/support-matrix/sast-support-matrix/ | across two scanning engines |
| Pick AccuKnox for | Native SAST, DAST, IaC, secrets and SCA | https://help.accuknox.com/how-to/dast-scan-types/ | Four scan types are available |
| Pick AccuKnox for | Native SAST, DAST, IaC, secrets and SCA | https://cortex-docs.paloaltonetworks.com/application-security/application-security-posture-management-aspm/manage-code-weakness-issues | Currently, Cortex Cloud does not support native SAST scanners |
| Pick AccuKnox for | Open-source runtime enforcement with KubeArmor | https://help.accuknox.com/faqs/general/ | CNCF Sandbox project with 2 million+ downloads |
| Pick AccuKnox for | Open-source runtime enforcement with KubeArmor | https://help.accuknox.com/faqs/runtime-security/ | Inline Mitigation |
| Pick AccuKnox for | Pay per module, run SaaS or on-prem | https://help.accuknox.com/faqs/pricing/ | Customers only pay for the modules they choose |
| Pick AccuKnox for | Pay per module, run SaaS or on-prem | https://help.accuknox.com/faqs/deployment/ | Full On-premises or Air-gapped |
| Note, palo | Palo Alto Networks sells Prisma Cloud and Cortex Cloud. Its Prisma Cloud page now promotes Cortex Cloud. | https://www.paloaltonetworks.com/prisma/cloud | MEET CORTEX CLOUD |
| Note, wiz | Google completed its acquisition of Wiz on 11 March 2026. Wiz says it stays multi-cloud. | https://cloud.google.com/blog/products/identity-security/google-completes-acquisition-of-wiz | Google has completed its acquisition of Wiz |
| Note, wiz | Google completed its acquisition of Wiz on 11 March 2026. Wiz says it stays multi-cloud. | https://cloud.google.com/blog/products/identity-security/google-completes-acquisition-of-wiz | March 11, 2026 |
| Note, wiz | Google completed its acquisition of Wiz on 11 March 2026. Wiz says it stays multi-cloud. | https://www.wiz.io/blog/google-closes-deal-to-acquire-wiz | Wiz remains a multi-cloud platform |

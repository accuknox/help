"""Content for the AccuKnox vs Wiz, Palo Alto Networks and SentinelOne CNAPP comparison.

Source list. validate_evidence.py checks that
each phrase appears in the saved copy of the source page under research/raw/, so no claim
reaches the PDF without a quote behind it.

Status keys per cell: yes Supported, par Parity, lim Limited, no Not supported,
noeq No equivalent, nl Not listed on public pages, soon Coming soon.
Win keys per competitor: ak AccuKnox leads, par parity, comp competitor leads, nl not listed.
"""

READ_DATE = "2026-10-16"

# id: (vendor, raw file stem, title, url)
SOURCES = {
    # AccuKnox, read live on help.accuknox.com
    "ak_cspm": ("ak", "ak-faq-cspm", "CSPM FAQs", "https://help.accuknox.com/faqs/cspm/"),
    "ak_comp": ("ak", "ak-faq-compliance", "Compliance FAQs", "https://help.accuknox.com/faqs/compliance/"),
    "ak_ciem": ("ak", "ak-ciem-overview", "CIEM overview", "https://help.accuknox.com/getting-started/ciem-overview/"),
    "ak_kiem": ("ak", "ak-kiem", "KIEM", "https://help.accuknox.com/use-cases/kiem/"),
    "ak_36": ("ak", "ak-36", "v3.6 release notes", "https://help.accuknox.com/getting-started/3.6-release/"),
    "ak_dspm": ("ak", "ak-dspm", "DSPM overview", "https://help.accuknox.com/getting-started/dspm-overview/"),
    "ak_dspm_on": ("ak", "ak-dspm-onboard", "DSPM onboarding", "https://help.accuknox.com/getting-started/dspm-onboarding/"),
    "ak_ai": ("ak", "ak-faq-ai", "AI security FAQs", "https://help.accuknox.com/faqs/ai-security/"),
    "ak_mlscan": ("ak", "ak-mlscan", "ML static scan", "https://help.accuknox.com/how-to/ml-static-scan/"),
    "ak_sast": ("ak", "ak-sast", "SAST support matrix", "https://help.accuknox.com/support-matrix/sast-support-matrix/"),
    "ak_dast": ("ak", "ak-dast", "DAST scan types", "https://help.accuknox.com/how-to/dast-scan-types/"),
    "ak_iac": ("ak", "ak-iac", "IaC support matrix", "https://help.accuknox.com/support-matrix/iac/"),
    "ak_aspm": ("ak", "ak-faq-aspm", "ASPM FAQs", "https://help.accuknox.com/faqs/aspm/"),
    "ak_sbom": ("ak", "ak-faq-sbom", "SBOM FAQs", "https://help.accuknox.com/faqs/sbom/"),
    "ak_jfrog": ("ak", "ak-jfrog", "JFrog registry onboarding", "https://help.accuknox.com/how-to/jfrog-container/"),
    "ak_sarif": ("ak", "ak-sarif", "SARIF findings", "https://help.accuknox.com/getting-started/sarif-findings/"),
    "ak_rt": ("ak", "ak-faq-runtime", "Runtime security FAQs", "https://help.accuknox.com/faqs/runtime-security/"),
    "ak_dep": ("ak", "ak-faq-deploy", "Deployment FAQs", "https://help.accuknox.com/faqs/deployment/"),
    "ak_gen": ("ak", "ak-faq-general", "General FAQs", "https://help.accuknox.com/faqs/general/"),
    "ak_cdr": ("ak", "ak-cdr", "Cloud detection and response", "https://help.accuknox.com/use-cases/cdr/"),
    "ak_price": ("ak", "ak-faq-pricing", "Pricing and billing FAQs", "https://help.accuknox.com/faqs/pricing/"),
    "ak_mkt": ("ak", "ak-faq-partners", "Partnerships and marketplace FAQs", "https://help.accuknox.com/faqs/partnerships/"),
    "ak_vm": ("ak", "ak-vmscan", "Agentless cloud VM scanning", "https://help.accuknox.com/how-to/vm-security/agentless/cloud-vm-scanning/"),
    "ak_pf": ("ak", "ak-pf", "Prompt Firewall overview", "https://help.accuknox.com/use-cases/prompt-firewall-overview/"),
    # Wiz
    "wz_cspm": ("wz", "wiz-cspm", "Wiz CSPM", "https://www.wiz.io/solutions/cspm"),
    "wz_comp": ("wz", "wiz-compliance", "Wiz compliance", "https://www.wiz.io/solutions/compliance"),
    "wz_ciem": ("wz", "wiz-ciem", "Wiz CIEM", "https://www.wiz.io/solutions/ciem"),
    "wz_plat": ("wz", "wiz-platform", "Wiz platform", "https://www.wiz.io/platform"),
    "wz_dspm": ("wz", "wiz-dspm", "Wiz DSPM", "https://www.wiz.io/solutions/dspm"),
    "wz_ai": ("wz", "wiz-aispm", "Wiz AI security", "https://www.wiz.io/solutions/ai-spm"),
    "wz_sast": ("wz", "wiz-sast", "Wiz SAST", "https://www.wiz.io/solutions/sast"),
    "wz_sastblog": ("wz", "wiz-blog-sast", "Wiz SAST Public Preview blog", "https://www.wiz.io/blog/introducing-wiz-sast-where-code-risk-meets-cloud-context"),
    "wz_aisast": ("wz", "wiz-blog-aisast", "Wiz AI SAST blog", "https://www.wiz.io/blog/introducing-wiz-ai-sast"),
    "wz_code": ("wz", "wiz-code", "Wiz Code", "https://www.wiz.io/platform/wiz-code"),
    "wz_red": ("wz", "wiz-red-agent", "Wiz Red Agent GA blog", "https://www.wiz.io/blog/wiz-red-agent-is-ga"),
    "wz_sensor": ("wz", "wiz-sensor", "Wiz Sensor", "https://www.wiz.io/solutions/runtime-sensor"),
    "wz_defend": ("wz", "wiz-defend", "Wiz Defend", "https://www.wiz.io/platform/wiz-defend"),
    "wz_mp": ("wz", "wiz-awsmp", "Wiz on AWS Marketplace", "https://aws.amazon.com/marketplace/pp/prodview-ibgbkrqusncsm"),
    "wz_azure": ("wz", "wiz-env-azure2", "Wiz on Microsoft Azure", "https://www.wiz.io/environments/microsoft-azure"),
    "wz_google": ("wz", "wiz-google-cloudblog", "Google completes acquisition of Wiz", "https://cloud.google.com/blog/products/identity-security/google-completes-acquisition-of-wiz"),
    "wz_close": ("wz", "wiz-google-closes", "Wiz: Google closes deal to acquire Wiz", "https://www.wiz.io/blog/google-closes-deal-to-acquire-wiz"),
    "wz_onprem": ("wz", "wiz-onprem", "Wiz Sensor Workload Scanner for on-prem", "https://www.wiz.io/blog/sensor-wls-for-on-prem"),
    # Palo Alto Networks
    "pa_page": ("pa", "pa-prisma-cloud", "Prisma Cloud product page", "https://www.paloaltonetworks.com/prisma/cloud"),
    "pa_lic": ("pa", "cx-license", "Cortex Cloud license plans", "https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/get-started/understand-license-plans"),
    "pa_pclic": ("pa", "pc-licenses", "Prisma Cloud licenses", "https://docs.prismacloud.io/content-collections/administration/prisma-cloud-licenses"),
    "pa_appsec": ("pa", "cx-appsec", "Cortex Cloud Application Security", "https://cortex-docs.paloaltonetworks.com/cortex-xsiam/cloud-security/cortex-cloud-application-security"),
    "pa_scan": ("pa", "cx-codescanners", "Cortex Code Security scanners", "https://cortex-docs.paloaltonetworks.com/application-security/code-security/code-security-scanners"),
    "pa_sast": ("pa", "cx-sast-ingest", "Cortex Manage SAST code weakness issues", "https://cortex-docs.paloaltonetworks.com/application-security/application-security-posture-management-aspm/manage-code-weakness-issues"),
    "pa_tech": ("pa", "pc-supported-tech", "Prisma Cloud AppSec supported technologies", "https://docs.prismacloud.io/content-collections/application-security/supported-technologies"),
    "pa_def": ("pa", "pc-host-defender", "Prisma Cloud host Defender architecture", "https://docs.prismacloud.io/content-collections/runtime-security/install/deploy-defender/host/host-defender-architecture"),
    "pa_rd": ("pa", "pc-rd-containers", "Prisma Cloud container runtime defense", "https://docs.prismacloud.io/content-collections/runtime-security/runtime-defense/runtime-defense-containers"),
    "pa_airs": ("pa", "pa-airs", "Prisma AIRS", "https://www.paloaltonetworks.com/ai-security/prisma-airs"),
    "pa_aispm": ("pa", "cx-aispm", "Cortex Cloud AI-SPM", "https://www.paloaltonetworks.com/cortex/cloud/ai-security-posture-management"),
    "pa_pcai": ("pa", "pc-aispm", "Prisma Cloud AI-SPM overview", "https://docs.prismacloud.io/content-collections/ai-security-posture-management/aispmoverview"),
    "pa_welcome": ("pa", "pc-welcome", "Welcome to Prisma Cloud", "https://docs.prismacloud.io/content-collections/get-started/welcome-to-prisma-cloud"),
    "pa_data": ("pa", "cx-datasec", "Cortex Cloud Data Security", "https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/cortex-data-security/what-is-cortex-cloud-data-security"),
    "pa_dspm": ("pa", "pc-dspm-assets", "Prisma Cloud DSPM supported assets", "https://docs.prismacloud.io/content-collections/data-security-posture-management/welcome/supported-assets"),
    "pa_iam": ("pa", "pc-iam", "Prisma Cloud IAM security", "https://docs.prismacloud.io/content-collections/administration/configure-iam-security/what-is-prisma-cloud-iam-security"),
    "pa_graph": ("pa", "cx-graph", "Cortex Create a graph rule", "https://cortex-docs.paloaltonetworks.com/cortex-xsiam/cloud-security/rules-and-policies/cloud-security-rules-and-policies/create-and-manage-cloud-security-rules/create-a-graph-rule"),
    "pa_sbom": ("pa", "pc-sbom-export", "Prisma Cloud exporting SBOMs", "https://docs.prismacloud.io/content-collections/runtime-security/vulnerability-management/exporting-sboms"),
    "pa_cxrt": ("pa", "cx-runtime", "Cortex Cloud Runtime Security", "https://www.paloaltonetworks.com/cortex/cloud/runtime-security"),
    "pa_comp": ("pa", "pc-compliance-standards", "Prisma Cloud compliance standards", "https://docs.prismacloud.io/content-collections/compliance/compliance-standards"),
    # SentinelOne
    "s1_cns": ("s1", "s1-cnapp", "Singularity Cloud Native Security", "https://www.sentinelone.com/platform/cloud-native-security/"),
    "s1_cspm": ("s1", "s1-cspm", "Singularity Cloud Security Posture Management", "https://www.sentinelone.com/platform/singularity-cloud-cspm/"),
    "s1_cws": ("s1", "s1-cws", "Singularity Cloud Workload Security", "https://www.sentinelone.com/platform/singularity-cloud-workload-security"),
    "s1_prompt": ("s1", "s1-prompt", "SentinelOne Prompt Security", "https://www.sentinelone.com/platform/securing-ai-prompt/"),
    "s1_price": ("s1", "s1-pricing", "SentinelOne pricing", "https://www.sentinelone.com/pricing/"),
}


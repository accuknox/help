---
hide:
  - toc
---

# **Reports**

Reports gives a comprehensive view of security checks that are used to detect misconfigured and vulnerable assets. These assets are scanned by tools like Stig, Prowler, Nipper, SecurityHub, etc. to find misconfigurations and vulnerabilities with respect to compliance frameworks (PCI-DSS, NIST, GDPR, SOC2, HIPAA, etc.). The security checks are in accordance with compliance frameworks to ensure the security of sensitive data. These checks are divided into different sections, namely identity and access management, Logging, Monitoring, Networking and Storage.

![](/saas/images/reports-table-of-content.png)

**Severity**
is a scoring system designed to help user to take action on urgent issues according to their score. In general , Critical and high priority issued should be resolved and the others should only be monitored.

**Policy Name** 
contains the name of the security checks that are applied to resources. These security checks are designed to align with compliance frameworks.

**Resource(s) Passed and Failed**
is the number of resources that are vulnerable because they don’t follow the guidelines set by compliance framework. Any check with failed resources is set as alert.

**Overall Status** 
tells if any resource have failed the security checks. 

![](/saas/images/reports-list.png)

**Resources Monitored** 
are the total number of assets within you cloud account which scanned for vulnerabilities and misconfigurations.

**Accounts Monitored** 
is the total number of cloud accounts that were scanned.

**Pass and Fail** 
is the total number of resources that passed or failed the guidelines set by the compliance framework.

![](/saas/images/reports-executive-summary.png)

User can click on the policies to see detailed view of the policy, In addition to previous information this page also contains : 

**Description** 
gives the information about the policy and the consequences of the misconfiguration or vulnerability.

**Recommendations** 
provide the user with information about steps that can be taken to resolve the vulnerability for failed resources.

![](/saas/images/reports-summary.png)
 

## **Report Configuration** 

To get the reports user need to add report configuration from the Reports section in Accuknox Saas

![](/saas/images/reports-main.png)

In the Configuration user needs to provide the details about their Name, Email and configuration for the report. These configurations are Groups, Labels, Month, Period, Risks, Baselines, Pages, Day of the month, Day of the week.

![](/saas/images/reports-configuration.png)
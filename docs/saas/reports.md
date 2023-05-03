---
hide:
  - toc
---

# **Reports**

Reports gives a comprehensive view of security checks that are used to detect misconfigured and vulnerable assets. These assets are scanned by tools like Stig, Prowler, Nipper, SecurityHub, etc. to find misconfigurations and vulnerabilities with respect to compliance frameworks (PCI-DSS, NIST, GDPR, SOC2, HIPAA, etc.). The security checks are in accordance with compliance frameworks to ensure the security of sensitive data. These checks are divided into different sections, namely identity and access management, Logging, Monitoring, Networking and Storage.

### List for security check is diplayed with following information:

**Severity**
is a scoring system designed to help user to take action on urgent issues according to their score. In general , Critical and high priority issued should be resolved and the others should only be monitored.

**Policy Name** 
contains the name of the security checks that are applied to resources. These security checks are designed to align with compliance frameworks.

**Resource(s) Passed and Failed**
is the number of resources that are vulnerable because they don’t follow the guidelines set by compliance framework. Any check with failed resources is set as alert.

**Overall Status** 
tells if any resource have failed the security checks. 

### Overview of Resources and Assets displays:

**Resources Monitored** 
are the total number of assets within you cloud account which scanned for vulnerabilities and misconfigurations.

**Accounts Monitored** 
is the total number of cloud accounts that were scanned.

**Pass and Fail** 
is the total number of resources that passed or failed the guidelines set by the compliance framework.

### User can click on the policies to see detailed view of the policy, In addition to previous information this page also contains :

**Description** 
gives the information about the policy and the consequences of the misconfiguration or vulnerability.

**Recommendations** 
provide the user with information about steps that can be taken to resolve the vulnerability for failed resources.

### Report configuration 

To get the reports user need to add report configuration from the Reports section in AccuKnox Saas.

![](/saas/images/reports-main.png)

In the Configuration user needs to provide the details about their Name, Email and configuration for the report. These configurations are Groups, Labels, Month, Period, Risks, Baselines, Pages, Day of the month, Day of the week.

![](/saas/images/reports-configuration.png)

## **Conclusion**

As a part of CSPM, AccuKnox enables you to handle Vulnerabilities with the ability to mark false positives, Waiting for 3rd party or Accepted risk and many more, so that you get to act on findings that are remediable and containing the SLA. Hence, AccuKnox provides a comprehensive compliance reports based on various security governance for third party assessment operators (3PAO) auditing. Check [Troubleshooting & FAQs page](/faqs/troubleshooting-and-faqs) to get more answers.

- - - 
[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }
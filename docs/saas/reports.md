---
hide:
  - toc
---

# **Reports**

Reports contain insights about vulnerability scans of assets which are done by tools like Stig, Prowler, Nipper, SecurityHub, etc. It contains information about all the security checks for misconfigurations and vulnerabilities as such the configurations of security critical assets align to compliance frameworks (PCI-DSS, NIST, GDPR, SOC2, HIPAA, etc.). Reports provide detailed summary about security posture of assets within your cloud account. Alerts are divided into different sections according to the process from which the alerts were produced. These sections are identity and access management, Logging, Monitoring, Networking and Storage.

![](/saas/images/reports-table-of-content.png)

**Severity**
tells the level of severity of the policy according to the compliance frameworks.
**Policy Name** 
contains the name of the security checks that are applied to resources. These security checks are designed by compliance frameworks which helps to maintain security posture.
**Resource(s) Passed and Failed**
is the number of resources that are vulnerable because they don’t follow the guidelines set by compliance framework.
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
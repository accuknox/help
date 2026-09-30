> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/governance/prisma-cloud-threat-detection.md).

# Prisma Cloud Threat Detection

Prisma Cloud enables threat detection across the Cloud Security Posture Management (CSPM) and Cloud Workload Protection Platform (CWPP) so that you can prevent and detect security risks across their multi-and-hybrid cloud environments, hosts, containers, and serverless functions.

CSPM supports two categories of policies which are Incident and Risk, with Incident being the group of policies that supplies the threat detection functionality and includes two types of anomaly policies: User Entity Behavior Analytics (UEBA) and Network anomaly which utilizes either machine learning or AutoFocus. The Risk category corresponds to the **config** policies which uses the resource query language (RQL).

With anomaly policies, data is collected from various sources such as audit and network flow logs and are processed using sophisticated data analysis techniques like machine learning, statistical modeling, and graph analysis to detect threats; both known-and-unknown. With RQL based policies, events related to user or network activity are analyzed to match a certain criteria, such as a JSON field having a specific value.

Threat detection in the CWPP module consists of a collection of threat data that is aggregated from a myriad of sources both commercial and open source, and that is then delivered through the Prisma Cloud Intelligence Stream. This threat data is then consumed across various feature sets of Compute such as **Vulnerabilities** and **Runtime**.

* [Threat Detection in CSPM](#id3ce4176e-b19c-4878-9cc8-1b967f333dcb)
* [Threat Detection in CWPP](#ida1f54b12-64cc-4483-a61e-e3f708e7815c)

## Threat Detection in CSPM

An overview of the threat detection functionality in Prisma Cloud CSPM module.

Prisma Cloud provides policies for a myriad of use cases such as detecting account hijacking attempts, backdoor activity, network data exfiltration, unusual protocol, and DDoS activity. After a threat is detected, an alert will be generated notifying administrators of the issue on hand so that they can quickly remediate it. In addition, several of these policies map to the MITRE ATT\&CK® Enterprise IaaS Matrix which serves as a roadmap for securing your cloud assets.

* **Anomaly policies**:
  * **User Entity and Behavior Analytics (UEBA)**—A set of anomaly policies for identifying deviant user activity such as a user logging on from an unknown location, successive log in attempts from distant geographical locations, or an abnormally large number of compute resources being created. You can view all the UEBA policies by applying a **Policy Type** filter for **Anomaly** in **Policies**, and typing **ueba** in the search field to view results which displays the **Policy Subtype** of **UEBA**.
  * **Network anomaly policies**—A set of anomaly policies that continuously monitors network logs for malicious network traffic using machine learning as well as matching IPs against [AutoFocus](https://docs.paloaltonetworks.com/autofocus/autofocus-admin/get-started-with-autofocus.html). There are network anomaly policies for detecting various threats such as Botnet, Ransomware, and Worm attacks. Prisma Cloud currently supports over forty network policies—you can view all of them by applying a **Policy Type** filter for **Anomaly** in **Policies**, and typing **network** in the search field to view the results which displays the **Policy Subtype** of **Network**.
  * **Anomaly settings customization**—You can use the anomaly settings to control the criterion in which alerts are generated for anomaly policies. You can modify the anomaly settings to change the model training threshold, customize alert disposition, and add anomaly trusted lists to suppress alerts from trusted resources.
    * **Alert disposition**—A method of specifying your preference for when you want to be notified of an alert—**Conservative**, **Moderate**, or **Aggressive**; these preferences are based on the severity of the issues: **Low**, **Medium**, **High**. **Conservative** generates high severity alerts, **Moderate** generates high and medium severity alerts, and **Aggressive** generates high, medium, and low severity alerts.

      The criteria for determining the severity is different for each of the policies.
    * **Anomaly training model thresholds**—A method for defining different thresholds for training the models for anomaly detection for UEBA and network anomalies. You can set the **Training Model Threshold** to **Low**, **Medium**, or **High**. These thresholds are used to determine the volume—for example, a minimum of 100 user events—and duration of data—for example, 30 days—used for training the models. Refer to [Set Up Anomaly Policy Thresholds](/content-collections/administration/define-prisma-cloud-enterprise-settings.md#anomaly-thresholds) for more details on customizing your anomaly policy thresholds.

      The thresholds are different for each of the policies.
    * **Anomaly trusted list**—A method of suppressing specific resources that you do not want to generate alerts for. For example, if there are IP addresses that you are using to perform penetration testing, then you can add those IPs to a trusted list to suppress their alerts. Refer to [Suppress Alerts for Prisma Cloud Anomaly Policies](/content-collections/alerts/suppress-alerts-for-prisma-cloud-anomaly-policies.md) for details on creating an Anomaly Trusted List.
* **Resource Query Language (RQL) policies**:
  * **Audit Event**—A set of RQL based policies that monitors audit events in your environment for potential policy violations. You create audit policies to flag sensitive events such as root activities or configuration changes that may potentially put your cloud environment at risk. To view all of the audit event policies available, apply a filter for **Policy Type** and select **Audit Event**. Refer to [Create a Network or Audit Event Policy](/content-collections/governance/create-a-policy.md#create-an-audit-event-policy) to learn how to create custom audit event policies.
  * **Network Event**—A set of RQL based policies that monitor network activities in your environment. To view all of the Network policies available, apply a filter for **Policy Type** and select **Network**. Refer to [Create a Network or Audit Event Policy](/content-collections/governance/create-a-policy.md#create-an-audit-event-policy) to learn how to create custom net#work event policies.
  * **Custom policies that work with Third-party integrations**—A custom RQL based policy can be created that integrates with third-party services like Amazon GuardDuty or AWS Inspector for enhanced threat detection functionality. In addition, you also have the ability to clone existing RQL based policies and make modifications to them to fit your specific cloud security needs. Refer to [Create a Custom Policy on Prisma Cloud](/content-collections/governance/create-a-policy.md) for details on creating custom policies.
* **Prisma Cloud mapping to the MITRE ATT\&CK® Enterprise IaaS Matrix**—The MITRE ATT\&CK Matrix is a knowledge base of tactics, techniques, and procedures (TTPs) that bad actors could utilize in their attacks. A subset of this—the IaaS Matrix—covers cloud based tactics and techniques. Prisma Cloud has config and anomaly policies that map to the IaaS Matrix so that you can continuously monitor the security of your cloud for discovery and initial access, to impact and exfiltration objectives; this enables security teams to automatically detect various attack threats across their cloud environments. View the anomaly policies that map to these objectives of the IaaS Matrix by applying a **Policy Type** filter of **Anomaly**, and a **Compliance Standard** filter with the version of the IaaS Matrix you want to view results for like **MITRE ATT\&CK v8.2**; then, in the Prisma Cloud search box enter the objectives that you want to view anomaly policies for like **discovery** or **impact**.

## Threat Detection in CWPP

An overview of the threat detection functionality in Prisma Cloud CWPP module.

The Prisma Cloud CWPP module, also known as Prisma Cloud Compute supports threat detection via Prisma Cloud Advanced Threat Detection (ATD) via the Prisma Cloud Intelligence Stream. ATD is the main source of threat data in Compute—it collects data from commercial threat feeds, open source threat feeds, IP reputation lists, Prisma Cloud Labs, common vulnerability exposures (CVEs), and user supplied data. The Prisma Cloud Intelligence Stream uses the data in ATD to deliver the threat feed in real time which is then utilized across several features in Compute such as vulnerability, runtime, and Web Application and API Security (WAAS) providing a breadth of threat detection capabilities across your compute workloads.

* **Vulnerability**—The CVE information from the different providers, packages, and images are taken from the Prisma Cloud Intelligence Stream, and additional information is added on top of that and the risk score for vulnerability scanning. The type of information you get in the threat feed reveals if an exploit exists or not, what type of attack complexity it has, and any environmental risks. The risk score is calculated from the data that Compute has from the CVEs and the environment factors which you can view in **Runtime Security > Monitor > Vulnerabilities**. Refer to [Vulnerability Explorer](/content-collections/runtime-security/vulnerability-management/vulnerability-explorer.md) for more details.
* **Runtime**—Ingests threat data from connections to malicious IP addresses, domains, or files known to have suspicious malware from the Prisma Cloud Intelligence Stream, and uses that to detect anomalous behavior. The **Incident explorer** (**Runtime Security > Monitor > Runtime > Incident Explorer**), raises a single alert per incident type every 24 hours; subsequent alerts for the same incident type are suppressed. In addition, you can analyze the runtime information for a resource by viewing the live forensics in **Incident Explorer**. Runtime also integrates with WildFire (**Runtime Security > Manage > System > WildFire**), which is Palo Alto Networks malware detection engine and identifies malware for both known-and-unknown threats thus enhancing your malware detection capabilities. Refer to [Runtime defense for containers](/content-collections/runtime-security/runtime-defense/runtime-defense-containers.md) to learn more about runtime defense in Compute.
* **WAAS**—If you’re making HTTP requests to a web application then Compute analyzes those requests if you have WAAS enabled on that resource. Computational behavioral analysis is conducted on the resource, and the request is analyzed to determine its intent. This data is analyzed across the different threats that Compute evaluates such as Cross Site Scripting (XSS) or SQL injection, and then an alert generates in **Runtime Security > Monitor > Events**, for **Containers**, **Hosts**, or **Serverless**. Refer to [Web-Application and API Security (WAAS)](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/enterprise-edition/content-collections/runtime-security/waas/waas.md) for an overview on how WAAS works in Compute.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/governance/prisma-cloud-threat-detection.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

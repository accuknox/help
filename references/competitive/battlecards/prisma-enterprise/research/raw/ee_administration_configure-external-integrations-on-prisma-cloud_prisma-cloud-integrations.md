> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/administration/configure-external-integrations-on-prisma-cloud/prisma-cloud-integrations.md).

# Prisma Cloud Integrations

Learn about different types of integrations that Prisma® Cloud supports with third-party systems.

Prisma® Cloud provides multiple out-of-the-box integration options that you can use to integrate Prisma Cloud in to your existing security workflows and with the technologies you already use. The Amazon GuardDuty, AWS Inspector, Qualys, and Tenable integrations are inbound or pull-based integrations where Prisma Cloud periodically polls for the data and retrieves it from the external integration system; all other integrations are outbound or push-based integrations where Prisma Cloud sends data about an alert or error to the external integration system.

Alibaba Cloud in the Mainland China regions does not support all the integrations listed below. The supported **Integrations** are Amazon SQS, Email, Splunk and Webhooks.

* **Amazon GuardDuty**—Amazon GuardDuty is a threat detection service that continuously monitors for malicious activity and unauthorized behavior to protect your AWS accounts and workloads. Prisma Cloud integrates with Amazon GuardDuty and ingests vulnerability data to provide you with additional context on risks in the cloud.
* **AWS Inspector**—AWS Inspector assesses applications for exposure, vulnerabilities, and deviations from best practices. It also produces a detailed list of security findings prioritized by level of severity. Prisma Cloud integrates with AWS inspector and ingests vulnerability data and Security best practices deviations to provide you with additional context about risks in the cloud.
* **Amazon S3**—Amazon Simple Storage Service (Amazon S3) is designed to make web-scale computing easier. You can use Amazon S3 to store and retrieve any amount of data using highly scalable, reliable, fast, and inexpensive data storage. Prisma Cloud can send alerts to an Amazon S3 bucket/folder.
* **AWS Security Hub**—AWS Security Hub is a central console where you can view and monitor the security posture of your cloud assets directly from the Amazon console. As the Prisma Cloud application monitors your assets on the AWS cloud and sends alerts on resource misconfigurations, compliance violations, network security risks, and anomalous user activities, you have a comprehensive view of all your cloud assets across all your AWS accounts directly from the Prisma Cloud console.
* **Amazon Security Lake**—Amazon Security Lake offers a comprehensive view of security data across sources in your cloud and on-premises environments including Prisma Cloud. On ingestion of Prisma Cloud Open Cybersecurity Schema Framework (OCSF) compliant vulnerability security data into Amazon Security Lake, your security analysts can break down data silos, query data in-place, and perform big data analytics at scale.
* **Amazon SQS**—Amazon Simple Queue Service (SQS) helps you send, receive, and store messages that pass between software components at any volume without losing messages and without requiring other services to be always available. Prisma Cloud can send alerts to Amazon SQS, and you can set up the AWS CloudFormation service to enable custom workflows.
* **Azure Service Bus Queue**—Azure Service Bus is a managed messaging infrastructure designed to transfer data between applications as messages. With the Prisma Cloud and Azure Service Bus queue integration, you can send alerts to the queue and set up custom workflows to process the alert payload.
* **Cortex XSOAR**—Cortex XSOAR (formerly Demisto) is a Security Orchestration, Automation and Response (SOAR) platform that enables you to streamline your incident management workflows. With the Prisma Cloud and Cortex XSOAR integration you can automate the process of managing Prisma Cloud alerts and the incident lifecycle with playbook-driven response actions.
* **Email**—Configure Prisma Cloud to send alerts as emails to your email account.
* **Google Cloud SCC**—Google Cloud Security Command Center (SCC) is the security and data risk database for Google Cloud Platform. Google Cloud SCC enables you to understand your security and data attack surface by providing inventory, discovery, search, and management of your assets. Prisma Cloud integrates with Google Cloud SCC and sends alerts to the Google Cloud SCC console to provide centralized visibility in to security and compliance risks of your cloud assets.
* **Jira**—Jira is an issue tracking, ticketing, and project management tool. Prisma Cloud integrates with Jira and sends notifications of Prisma Cloud alerts to your Jira accounts.
* **Microsoft Teams**—Microsoft Teams is cloud-based team collaboration software that is part of the Office 365 suite of applications and is used for workplace chat, video meetings, file storage, and application integration. The Prisma Cloud integration with Microsoft Teams enables you to monitor your assets and send alerts on resource misconfigurations, compliance violations, network security risks, and anomalous user activities—either as they happen or as consolidated summary cards.
* **PagerDuty**—PagerDuty enables alerting, on-call scheduling, escalation policies, and incident tracking to increase the uptime of your apps, servers, websites, and databases. The PagerDuty integration enables you to send Prisma Cloud alert information to PagerDuty service. The incident response teams can investigate and remediate the security incidents.
* **Qualys**—Qualys specializes in vulnerability management security software that scans hosts for potential vulnerabilities. Prisma Cloud integrates with the Qualys platform and ingests vulnerability data to provide you with additional context about risks in the cloud.
* **ServiceNow**—ServiceNow is an incident, asset, and ticket management tool. Prisma Cloud integrates with ServiceNow and sends notifications of Prisma Cloud alerts as ServiceNow tickets.
* **Slack**—Slack is an online instant messaging and collaboration system that enables you to centralize all your notifications. You can configure Prisma Cloud to send notifications of Prisma Cloud alerts through your slack channels.
* **Splunk**—Splunk is a software platform that searches, analyzes, and visualizes machine-generated data gathered from websites, applications, sensors, and devices. Prisma Cloud integrates with cloud-based Splunk deployments and enables you to view Prisma Cloud alerts through the Splunk event collector. Prisma Cloud can integrate with on-premises Splunk instances through the AWS SQS integration.
* **Tenable**—Tenable.io is a cloud-hosted vulnerability management solution that provides visibility and insight in to dynamic assets and vulnerabilities. Prisma Cloud integrates with Tenable and ingests vulnerability data to provide you with additional context about risks in the cloud.
* **Webhooks**—The webhooks integration enables you to pass information in JSON format to any third-party integrations that are not natively supported on Prisma Cloud. With a webhook integration, you can configure Prisma Cloud to send alerts to the webhook URL as an HTTP POST request so that any services or applications that subscribe to the webhook URL receive alert notifications as soon as Prisma Cloud detects an issue.

For outbound integrations:

* You can check status updates on demand in **Settings > Integrations** by clicking the **Get Status** icon for the relevant integration. The status check displays red if the integration fails validation checks for accessibility or credentials; or green when the integration is working and all templates are valid. To review the list of integrations that do not support the status checks see [Prisma Cloud Integrations—Supported Capabilities](/content-collections/administration/configure-external-integrations-on-prisma-cloud/integrations-feature-support.md). Status errors are displayed to help you find and fix potential issues.
  * If any exception or failure in processing notification occurs, an alarm gets generated. You can view those under Alarm Center, provided you have enabled Alarms.
  * When Prisma Cloud integrates with your external tools, you may experience delays in response from these tools. In such cases, a timeout of approximately 10 seconds is in effect, and if the communication fails during this period, Prisma Cloud will attempt a retry to send the notifications. Therefore, you may receive notifications after a delay. If you notice such delays, as a best practice, review your network infrastructure and investigate the issue from your end to ensure smoother operation.
* When you [Send Prisma Cloud Alert Notifications to Third-Party Tools](/content-collections/alerts/send-prisma-cloud-alert-notifications-to-third-party-tools.md), the value of the cloud service provider in the cloudType field for the resource that generated the alert the values is in lowercase letters, for example aws or alibaba-cloud.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/administration/configure-external-integrations-on-prisma-cloud/prisma-cloud-integrations.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

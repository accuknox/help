> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/search-and-investigate/audit-event-queries/audit-event-query-examples.md).

# Audit Event Query Examples

Review examples that show you how to use [Audit Event Query Attributes](/content-collections/search-and-investigate/audit-event-queries/audit-event-query-attributes.md) for investigating issues on the following cloud platforms:

* [Audit Event Query Examples for AWS](#event-query-examples-for-aws)
* [Audit Event Query Examples for Azure](#event-query-examples-for-azure)
* [Audit Event Query Examples for GCP](#event-query-examples-for-gcp)

## Audit Event Query Examples for AWS

<table data-header-hidden><thead><tr><th></th><th></th></tr></thead><tbody><tr><td>DESCRIPTION</td><td>RQL</td></tr><tr><td>Detect activities from non-automated events and from specific IP addresses.</td><td><pre><code>event from cloud.audit_logs where ip EXISTS AND ip IN ( 152.1.1.1)
</code></pre></td></tr><tr><td>Detect potentially sensitive or suspicious changes to the network configuration that impact your security posture.</td><td><pre><code>event from cloud.audit_logs where operation IN ('AuthorizeSecurityGroupEgress', 'AuthorizeSecurityGroupIngress', 'CreateVpc', 'DeleteFlowLogs', 'DeleteVpc', 'ModifyVpcAttribute', 'RevokeSecurityGroupIngress')
</code></pre></td></tr><tr><td>Detect potentially sensitive or suspicious changes to configuration settings.</td><td><pre><code>event from cloud.audit_logs where operation IN ('DeleteBucket', 'DeleteConfigRule', 'DeleteTrail', 'PutBucketAcl', 'PutBucketLogging', 'PutBucketPolicy')
</code></pre><pre><code>event from cloud.audit_logs where operation IN ( 'AddUserToGroup', 'AttachGroupPolicy', 'AttachGroupPolicy', 'AttachUserPolicy' , 'AttachRolePolicy' , 'CreateAccessKey', 'CreateKeyPair', 'DeleteKeyPair', 'DeleteLogGroup' )
</code></pre></td></tr><tr><td>Detect risky changes executed by a root user.</td><td><pre><code>event from cloud.audit_logs where operation IN ( 'ChangePassword', 'ConsoleLogin', 'DeactivateMFADevice', 'DeleteAccessKey' , 'DeleteAlarms' ) AND user = 'root'
</code></pre></td></tr><tr><td><p>Exclude results that match a specific string within an array in the event details.</p><p>To exclude results that include a specific string within an array, use the matches or does not match operator instead of contains/does not contain or exists/does not exist.</p></td><td><pre><code>event from cloud.audit_logs where operation IN ('AttachGroupPolicy', 'AttachRolePolicy', 'DeleteGroupPolicy', 'DeleteKeyPair', 'DeleteLogGroup') AND json.rule = $.userIdentity.arn does not match "AWSCloudFormationStackSetExecutionRole" or $.userIdentity.arn does not match "INST-SR-EC2-GRAAS-ROLE"
</code></pre></td></tr></tbody></table>

## Audit Event Query Examples for Azure

<table data-header-hidden><thead><tr><th></th><th></th></tr></thead><tbody><tr><td>DESCRIPTION</td><td>RQL</td></tr><tr><td>List specific operations performed on a specific Azure account.</td><td><pre><code>event from cloud.audit_logs where cloud.account = 'Test - Azure Subscription' AND operation IN ( 'AttachRolePolicy', 'AttachLoadBalancers')
</code></pre></td></tr><tr><td>List classic compute register operations performed by a specific user on a specific Azure account.</td><td><pre><code>event from cloud.audit_logs where cloud.account in ( 'Test - Azure Subscription' ) and user = 'abc@xyz.io' and operation IN ('Microsoft.ClassicCompute/register/action (BeginRequest)')
</code></pre></td></tr></tbody></table>

## Audit Event Query Examples for GCP

<table data-header-hidden><thead><tr><th></th><th></th></tr></thead><tbody><tr><td>DESCRIPTION</td><td>RQL</td></tr><tr><td>View sensitive network configuration updates on GCP.</td><td><pre><code>event from cloud.audit_logs where operation IN ('v1.compute.networks.delete','beta.compute.networks.insert','v1.compute.routes.delete','v1.compute.firewalls.insert','v1.compute.firewalls.delete')
</code></pre></td></tr><tr><td>View sensitive SQL instance updates on GCP.</td><td><pre><code>event from cloud.audit_logs where operation IN ('cloudsql.instances.update', 'cloudsql.sslCerts.create',' cloudsql.instances.create', 'cloudsql.instances.delete')
</code></pre></td></tr><tr><td>List all events with sensitive user actions on GCP.</td><td><pre><code>event from cloud.audit_logs where operation IN ('CreateCryptoKey','DestroyCryptoKeyVersion','v1.compute.disks.createSnapshot')
</code></pre></td></tr></tbody></table>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/search-and-investigate/audit-event-queries/audit-event-query-examples.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

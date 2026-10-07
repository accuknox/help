For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-intro.md).

WAAS enhances the traditional WAF protection model by deploying closer to the application, easily scaling up or down, and allowing for inspection of "internal" traffic (east-to-west) from other microservices as well as inbound traffic (north-to-south).

- For containerized web applications, WAAS binds to the application’s running containers, regardless of the cloud, orchestrator, node, or IP address where it runs, and without the need to configure any complicated routing.

- For non-containerized web applications, WAAS simply binds to the host where the application runs.

- WAAS monitors the remote applications by monitoring the mirrored traffic generated from the network interfaces attached to your instances.


Highlights of WAAS’s capabilities:

- **OWASP Top-10 Coverage** \- Protection against most critical [security risks](https://owasp.org/www-project-top-ten/) to web applications, including injection flaws, broken authentication, broken access control, security misconfigurations, etc.

- **API Protection** \- WAAS can enforce API traffic security based on definitions/specs provided in the form of [Swagger](https://swagger.io/) or [OpenAPI](https://www.openapis.org/) files.

- **Access Control** \- WAAS controls access to protected applications using Geo-based, IP-based, or HTTP Header-based user-defined restrictions.

- **File Upload Control** \- WAAS secures application file uploads by enforcing file extension rules.

- **Detection of Unprotected Web Applications** \- WAAS detects unprotected web applications and flags them in the radar view.

- **Penalty Box for Attackers** \- WAAS supports a 5 minutes ban of IPs triggering one of its protections to slow down vulnerability scanners and other attackers probing the application.

- **Bot Protection** \- WAAS detects good-known bots and other bots, headless browsers, and automation frameworks. WAAS is also able to fend off cookie droppers and other primitive clients by mandating the use of cookies and Javascript for the client to reach the protected origin.

- **DoS Protection** \- WAAS is able to enforce rate limitation on IPs or [Prisma Sessions](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-advanced-settings#prisma-session) to protect against high-rate and "low and slow" layer-7 DoS attacks.


## How to deploy WAAS?[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-intro\#how-to-deploy-waas)

WAAS is deployed with Prisma Compute Defenders. The Defenders can operate as a transparent HTTP proxy as well as monitor the traffic from an Out-Of-Band network for the remote applications that do not have any Defenders installed.

The Inline Defenders evaluate client requests against security policies before relaying the requests to your application. The Out-Of-Band Defenders only send out alerts from the read-only copy of the network traffic.

![CNAF architecture](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-d2da68ab6718dd3e2d46feb231977b4f3d90d8ef%252FCNAF-architecture.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=15540bbf5e53db672ee600a2dc23823c&sv=3)

\*The WAAS serverless offering provides a limited set of defenses compared to the WAAS offerings for containerized and non-containerized web applications. For example, it currently does not include protection against bot attacks or denial of service (DoS) attacks.

Defenders are deployed into the environment in which the web applications run, and you can view the data on the Prisma Cloud management console.

## How does WAAS work?[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-intro\#how-does-waas-work)

WAAS inspects the incoming and outgoing traffic to and from your application for discovery, monitoring, and protection. Once you deploy WAAS you get visibility into your attack surfaces such as the host, containers, and serverless functions. WAAS API observations list the endpoints of the APIs and the methods used by the APIs for communication. The WAAS discovery and API observations help in risk assessment and placing policies to protect your workflow.

![cnaf 791990](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-15bf29f795f819d465f8b8eed95bef0406b4ec60%252Fcnaf_791990.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=c7006094ae9279834a03783af793220c&sv=3)

Requests triggering one or more WAAS protections generate a WAAS "event audit" and action is taken based on the preconfigured action (see "WAAS Actions" below). WAAS’s event audits can be further explored in the "Monitor" section of Prisma Compute’s management console ( **Monitor > Events**). In addition, event audits are registered in the Defender’s [syslog](https://docs.prismacloud.io/admin-guide/audit/logging) thus allowing for integration with third-party analytics engines or SIEM platforms of choice.

## How does WAAS inspection work on Prisma Cloud?[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-intro\#how-does-waas-inspection-work-on-prisma-cloud)

WAAS can inspect the traffic as an Inline proxy as well as an Out-Of-Band network.

![waas network management](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-a7a4b63d3f864202dab19db6eab7796a7d76b861%252Fwaas_network_management.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=ee37fa0b8b6ec7acbe14f3bb9404f29c&sv=3)

### WAAS Inline proxy[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-intro\#waas-inline-proxy)

WAAS inspects all incoming requests and forwards them to the protected application if there are no malicious activities. The response from the application is in turn inspected by WAAS and sent to the user if it’s not violating any rules.

An Inline proxy provides the highest level of security for web applications and APIs because it has the ability to block incoming and outgoing traffic flows in real-time. However, real-time traffic monitoring may require more resources than Out-Of-Band monitoring. Configuration of Inline proxy should be tested in QA or staging environments before deploying in production to avoid application outages if not configured properly.

The Inline proxy needs a Defender to be deployed in the environment.

### WAAS Out-Of-Band[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-intro\#waas-out-of-band)

Out-Of-Band monitors both protected and unprotected workloads by inspecting the mirrored traffic. WAAS Out-Of-Band doesn’t interfere with client-server communications, nor does it impact the application performance.

You can use the TLS protocol (1.0, 1.1, 1.2) over HTTP/1.1 with the following RSA Key Exchange cipher suites to protect the API endpoints:

- TLS\_RSA\_WITH\_AES\_128\_CBC\_SHA256

- TLS\_RSA\_WITH\_3DES\_EDE\_CBC\_SHA

- TLS\_RSA\_WITH\_RC4\_128\_SHA


The full handshake process must be captured as partial transmission or session resumption process inspection are not (or cannot be) decrypted.

WAAS can be deployed with Defender or with CSP traffic mirroring.

1. **WAAS Out-Of-Band with Defender** needs a Defender to be deployed in your workload environment to monitor the protected applications by using Out-Of-Band network communication.

2. **WAAS Agentless with VPC traffic mirroring** is used in cases where it’s not possible to install Defender for each microservice. VPC traffic mirroring extends WAAS monitoring to instances regardless of whether they have Defenders deployed or not.











This setup requires you to install an agent called Observer on the target instance outside your workload environment, to remotely monitor the unprotected applications on your source instance by using the in-built traffic mirroring provided by CSP.











For example, AWS VPC traffic mirroring feature copies the traffic from the source EC2 instance (with no Defender) to the target EC2 instance that has a host Observer installed within the same VPC.


WAAS Out-Of-Band setup has no latency cost. But as WAAS can’t control the traffic, it can only send out alerts to the Prisma Console.

## Where do I begin with WAAS?[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-intro\#where-do-i-begin-with-waas)

WAAS is enabled by [adding a new WAAS rule](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/waas/deploy-waas/deploy-waas.md). Whenever new policies are created, or existing policies are updated, Prisma Cloud immediately pushes them to all the resources to which they apply.

To deploy WAAS, create a new WAAS rule, select the resources on which to apply the rule, define your web application and select the protections to enable. For containerized web applications, Prisma Cloud creates a firewall instance for each container instance. For legacy (non-containerized web applications), Prisma Cloud creates a firewall for each host specified in the configuration.

Prisma Cloud can also protect Fargate-based web containers. +See [WAAS for Fargate](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded/install-app-embedded-defender-fargate#waas-for-fargate).

### WAAS Actions[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-intro\#waas-actions)

Requests that trigger a WAAS protection are subject to one of the following actions:

- **Alert** \- The request is passed to the protected application (where, the deployed Defender has complete visibility on your workload) or unprotected application (where, there is no Defender deployed on the workload instance but on a remote instance, for example, in v with VPC mirroring), and an audit is generated for visibility.











Both In-line and Out-Of-Band WAAS deployment generate alerts to the Console.

- **Prevent** \- The request is denied from reaching the protected application, an audit is generated and WAAS responds with an HTML page indicating the request was blocked.











Supported only in WAAS Inline proxy setup.

- **Ban** \- Can be applied on either IP or [Prisma Session IDs](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-advanced-settings#prisma-session). All requests originating from the same IP/Prisma Session to the protected application are denied for the configured time period (default is 5 minutes) following the last detected attack.











Supported only in WAAS Inline proxy setup.











WAAS implements state, which is required for banning user sessions by IP address. Because Defenders do not share state, any application replicated across multiple nodes must enable IP stickiness on the load balancer.

- **Disable** \- The WAAS action is disabled.











Supported for both WAAS Inline and WAAS Out-Of-Band setups.


## Supported Protocols, Message Parsers, and Decoders[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-intro\#supported-protocols-message-parsers-and-decoders)

### Supported Protocols[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-intro\#supported-protocols)

- HTTP 1.0, 1.1, 2.0 - full support of all HTTP methods

- TLS 1.0, 1.1, 1.2, and 1.3 for WAAS In-line

- TLS 1.0, 1.1, and 1.2 for WAAS Out-Of-Band

- gRPC

- WebSockets Passthrough


### Supported Message Parsers, and Decoders[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-intro\#supported-message-parsers-and-decoders)

- GZip, deflate content encoding

- HTTP Multipart content type

- URL Query, x-www-form-urlencoded, JSON and XML parameter parsing

- URL, HTML Entity, JS, BASE64 decoding

- Overlong UTF-8


[PreviousWeb-Application and API Security (WAAS)](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas) [NextDeploying WAAS](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject

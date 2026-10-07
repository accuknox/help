For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas.md).

WAAS (Web-Application and API Security) can secure both containerized and non-containerized web applications. To deploy WAAS, create a new rule, and declare the entity to protect.

Although the deployment method varies slightly depending on the type of entity you’re protecting, the steps, in general, are:

1. Define rule resource.

2. Define application scope.

3. Enable relevant protections.


## Understanding WAAS rule resources and application scope[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas\#understanding-waas-rule-resources-and-application-scope)

The WAAS rule engine is designed to let you tailor the best-suited protection for each part of your deployment. Each rule has two scopes:

- Rule resources.

- Application list.


### Rule Resources[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas\#rule-resources)

This scope defines, for each type of deployment, a combination of one or more elements to which WAAS should attach itself to protect the web application:

- _**For containerized applications**_ \- Containers, images, namespaces, cloud account IDs, hosts.

- _**For non-containerized applications**_ \- Host on which the application is running.

- _**For containers protected with App-Embedded Defender**_ \- App ID.

- _**For serverless functions**_ \- Function name.


In the event of scope overlap (when multiple rules are applied to the same resource scope), the first rule by order will apply and all others will not apply. You can reorder rules via the `Order` column in WAAS rule tables by dragging and dropping rules.

### Application List[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas\#application-list)

This scope defines the protected application’s endpoints within the deployment as a combination of one or more of the following:

- _**Port (Required)**_ \- For containerized applications, the internal port on which the application is listening. For all other types, the externally facing port.

- _**HTTP hostname**_ \- The default setting is set to `*` (wildcard indicating all hostnames)

- _**Base path**_ \- Lets you apply protection policy on certain paths of the application (e.g. "/admin", "/admin/\*", etc.)

- _**TLS**_ \- TLS certificate to be used when expecting encrypted inbound traffic.


To better illustrate, consider the following deployment scenario for a web application running on top of an NGINX cluster:

![cnaf deployment example](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-75622f75d5b5dbcc492bdb01a67d9ab8871c0c25%252Fcnaf_deployment_example.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=f21794bcd1f5b30bacb3e28ccbec303c&sv=3)

In this example, different policies apply for different parts of the application. The steps for deploying a WAAS rule to protect the above-described web application would be as follows:

1. **Define rule resources** \- Specify the resource collection the rule applies to. Collections are comprised of image names and one or more elements to which WAAS should attach itself to protect the web application. In the following example, the rule will apply to all containers created by the Nginx image.















![waas nginx scope](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-9bfd8ffccdd4c300c6abdbda093d73c2f1c841db%252Fwaas_nginx_scope.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=ce6e4e766eff85dd6ee939722e533259&sv=3)

2. **Define protection policy for 'login', 'search', and 'product' endpoints** \- Set OWASP Top 10 protection to "Prevent" and geo-based access control to "Alert".

3. **Define protection policy for the application’s API endpoints** \- Set OWASP Top 10 and API protection to "Prevent" and HTTP header-based access control to "Alert".


Once the policy is defined, the rule overview shows the following rule resource and application definitions:

![waas rule example](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-e3f48293a12da2c82eaeb596eea900abcb19b235%252Fwaas_rule_example.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=99d56219c7774fdc6cbe02c2e5f0b96b&sv=3)

- _**Rule Resources**_ \- Protection is applied to all NGINX images

- _**Apps List**_ \- We deployed two policies each covering a different endpoint in the application (defined by HTTP hostname, port, and path combinations).


### Protection evaluation flow[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas\#protection-evaluation-flow)

WAAS offers a range of protection targeted at different attack vectors. Requests inspected by WAAS will be inspected in the following order of protection:

- Bot protection

- App firewall (OWASP Top-10)

- API protection

- DoS protection


WAAS Inline proxy will continue to inspect a request until "Prevent" or "Ban" actions are triggered, at which point the request will be blocked, and the evaluation flow will be halted. In the case of WAAS Out-of-band, the requests will be inspected and alerts will be sent to the Console.

For example, in the WAAS Inline proxy setup, assume all protections in bot protection are set to "Prevent". An incoming request originating from a bot and containing a SQL injection payload would be blocked by the bot protection (since it precedes the app firewall in the evaluation flow), and the SQL injection payload will not be assessed by the app firewall.

In a different scenario, suppose that all bot protections are set to "Alert" and all app firewall protections are set to "Prevent". A request originating from a bot containing a command injection payload will generate an alert event by bot protection and will be blocked by the app firewall protection.

## Recommended WAAS Deployment Phases[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas\#recommended-waas-deployment-phases)

It is recommended that WAAS is first deployed in non-production environments, and then promoted and implemented in production environments gradually. Below are the guidelines for each of the recommended phases and their prerequisites.

**Prerequisites:**

- A way to test the application before deploying WAAS and verify that it’s working properly, e.g., a working cURL command with the expected outcome.

- A certificate (public certificate and private key files in PEM format) is required if the application employs TLS.

- If you are planning to protect API endpoints, please provide API specification files if available (Swagger or OpenAPI 3)


1. Deploy WAAS in a test environment (preferably one that is as similar to production as possible).











All protections will be set to "Alert".

2. Allow WAAS to inspect traffic to the test environment for a few days, then regroup to examine triggers and findings. It is recommended to generate traffic to the test environment preferably requests that simulate real user messages.











The goal here is to fine-tune protections so that they correspond with the design of the protected application.











This would also be a good way to assess the performance impact introduced by WAAS and compare it to the performance of the application before the deployment of WAAS.

3. Following the successful completion of phases 1 and 2, deploy WAAS on a small portion of production with the same configuration that you tested in the test environment.











Next, examine the findings after a few days and make any necessary adjustments to the policies.

4. Deploy WAAS across the entire production deployment of the application.


[PreviousOverview](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-intro) [NextDeploy WAAS for Containers](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas/deployment-containers)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject

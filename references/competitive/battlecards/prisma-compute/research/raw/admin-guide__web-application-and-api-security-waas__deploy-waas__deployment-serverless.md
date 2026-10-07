For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas/deployment-serverless.md).

## Create a WAAS rule for serverless[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas/deployment-serverless\#create-a-waas-rule-for-serverless)

When Serverless Defender is embedded in a function, it offers built-in web application firewall (WAF) capabilities, including protection against:

- SQL injection (SQLi) attacks

- Cross-site scripting (XSS) attacks

- Command injection (CMDi) attacks

- Local file system inclusion (LFI) attacks

- Code injection attacks


Some [protections](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-app-firewall) are not available for WAAS serverless deployment.

**Prerequisites:** You already [embedded Serverless Defender](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/install/deploy-defender/serverless/serverless.md) into your function.

1. Open Console and go to **Defend > WAAS > Serverless**.















![waas deployment types serverless](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-e54316d2d62baeaa36d8bb77624be073b61191f2%252Fwaas_deployment_types_serverless.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=babdb4c41ca079250cf1bf9bb2ba5b22&sv=3)

2. Click **Add rule**.

3. Enter a rule name.

4. Choose the rule **Scope** by specifying the resource collection(s) to which it applies.











Collections define a combination of functions to which WAAS should attach itself to protect the web application:











Use [pattern matching](https://docs.prismacloud.io/admin-guide/configure/rule-ordering-pattern-matching) to precisely target your rule.















![waas serverless collections](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-401c196cfd1e62671f77713df0edb2918387b6d3%252Fwaas_serverless_collections.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=4de407d9fca0e2a1002f906ddd10f6df&sv=3)

5. Select the protections to enable.















![waas serverless protections view](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-f0b05531e0ec493cfe539fbc701a067b06d9db96%252Fwaas_serverless_protections_view.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=9af9a12d5e522c4fefc57cdfffb9d18b&sv=3)

6. Select **Alert** or **Prevent**.

7. If necessary, adjust the **Proxy timeout**











The maximum duration in seconds for reading the entire request, including the body. A 500 error response is returned if a request is not read within the timeout period. For applications dealing with large files, adjusting the proxy timeout is necessary.


[PreviousDeploy WAAS for App-Embedded](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas/deployment-app-embedded) [NextDeploy WAAS Agentless](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas/deployment-vpc-mirroring)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject

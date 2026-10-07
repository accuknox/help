For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas/deployment-containers.md).

## Prerequisites[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas/deployment-containers\#prerequisites)

- Install a [Container Defender](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/install/deploy-defender/orchestrator/orchestrator.md) in your workload environment.

- When installing container defenders, note that the maximum allowable PIDs (`pids.max`) is limited to 1,000 in the `twistlock.sh` installation script.

- When deploying inline firewall instances on a Defender node with more than 10 protected workloads, increase the memory allocation for the Defender pod to 4GB.











For more information, see the **Increase the Defender Pod Limit** section in the [Container Defender](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/install/deploy-defender/orchestrator/orchestrator.md) topic.


## Create a WAAS In-Line rule for Containers[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas/deployment-containers\#create-a-waas-in-line-rule-for-containers)

1. Open Console, and go to **Defend > WAAS > {Container\|Host} > In-Line**.

2. Select **Add rule**.









1. Enter a **Rule Name**

2. Enter **Notes** (Optional) for describing the rule.


3. Choose the rule **Scope** by specifying the resource collection(s) to which it applies.















![waas select scope](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-cf791aae2511b3dd0f756efa465216a6a1c308f5%252Fwaas_select_scope.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=8133c28b12c89f48ed984abae5177ff0&sv=3)











Collections define a combination of image names and one or more elements to which WAAS should attach itself to protect the web application:















![waas define collection](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-32e0366fca578a62074bf1d0cb20f66b2a91193d%252Fwaas_define_collection.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=bee4df7125102d743f14b9d1d7176a76&sv=3)











Applying a rule to all images using a wild card (`*`) is invalid - instead, only specify your web application images.

4. (Optional) Enable **API endpoint discovery**











When enabled, the Defender inspects the API traffic to and from the protected API. Defender reports a list of the endpoints and their resource path in **Compute > Monitor > WAAS > API discovery**.

5. (Optional) Enable **Automatically detect ports** for an endpoint to deploy WAAS protection on ports identified in the unprotected web apps report in **Monitor > WAAS > Unprotected web apps** for each of the workloads in the rule scope.











As an additional measure, you can specify additional ports by specifying them in the protected HTTP endpoints within each app to also include the ports that may not have been detected automatically.











By enabling both **Automatically detect ports** and **API endpoint discovery**, you can monitor your API endpoints and ports without having to add an application and without configuring any policies.

6. **Save** the rule.


## Add an App (policy) to the rule[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas/deployment-containers\#add-an-app-policy-to-the-rule)

01. Select a WAAS rule to add an App in.

02. Select **Add app**.

03. In the **App Definition** tab, enter an **App ID**.











    The combination of **Rule name** and **App ID** must be unique across In-Line and Out-Of-Band WAAS policies for Containers, Hosts, and App-Embedded.











    If you have a Swagger or OpenAPI file, click **Import**, and select the file to load.











    If you do not have a Swagger or OpenAPI file, manually define each endpoint by specifying the host, port, and path.









    1. In **Endpoint Setup**, click **Add Endpoint**.











       Specify endpoint in your web application that should be protected. Each defined application can have multiple protected endpoints.

    2. Enter **HTTP host** (optional, wildcards supported).











       HTTP hostnames are specified in the form of \[hostname\]:\[external port\].











       The external port is defined as the TCP port on the host, listening for inbound HTTP traffic. If the value of the external port is "80" for non-TLS endpoints or "443" for TLS endpoints it can be omitted. Examples: "\*.example.site", "docs.example.site", "www.example.site:8080", etc.

    3. Enter **App ports** as the internal port your app listens on.











       (You can skip to enter App ports, if you selected **Automatically detect ports** while creating the rule).











       When **Automatically detect ports** is selected, any ports specified in a protected endpoint definition will be appended to the list of protected ports. Specify the TCP port listening for inbound HTTP traffic.











       If your application uses **TLS** or **gRPC**, you must specify a port number.

    4. Enter **Base path** (optional, wildcards supported):











       Base path for WAAS to match when applying protections.











       Examples: "/admin", "/" (root path only), "/\*", /v2/api", etc.

    5. If your application uses TLS, set **TLS** to **On**.











       You can select the TLS protocol (1.0, 1.1, 1.2, and 1.3 for WAAS In-Line, and 1.0, 1.1, and 1.2 for WAAS Out-Of-Band) to protect the API endpoint and enter the TLS certificate in PEM format.

    6. You can select **Response headers** to add or override HTTP response headers in responses sent from the protected application.















       ![waas response headers](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-688968e2e78f0829a5588a2ee2cd08887d59403f%252Fwaas_response_headers.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=6df8503daef9b2ea02f76a18e8614c82&sv=3)

    7. Select **Create response header**.

    8. To facilitate inspection, after creating all endpoints, click **View TLS settings** in the endpoint setup menu.











       WAAS TLS settings:















       ![waas inline app embedded tls](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-439369b08050626ebd013dc1c8f175bd89c8d939%252Fwaas-inline-app-embedded-tls.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=3d019e8e0f7a06b2bb2e8f893fdcbe45&sv=3)









       - **Certificate** \- Copy and paste your server’s certificate and private key into the certificate input box (e.g., `cat server-cert.pem server-key > certs.pem`).

       - **Minimum TLS version** \- A minimum version of TLS can be enforced by WAAS In-Line to prevent downgrading attacks (the default value is TLS 1.2).

       - **HSTS** \- The [HTTP Strict-Transport-Security (HSTS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security) response header lets web servers tell browsers to use HTTPS only, not HTTP. When enabled, WAAS would add the HSTS response header to all HTTPS server responses (if it is not already present) with the preconfigured directives - `max-age`, `includeSubDomains`, and `preload`.









         1. `max-age=<expire-time>` \- Time, in seconds, that the browser should remember that a site is only to be accessed using HTTPS.

         2. `includeSubDomains` (optional) - If selected, HSTS protection applies to all the site’s subdomains as well.

         3. `preload` (optional) - For more details, see the following [link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security#preloading_strict_transport_security).


    9. If you application requires [API protection](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-api-protection), for each path define the allowed methods and the parameters.


04. Continue to **App Firewall** settings, select the [protections](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-app-firewall) to enable and assign them with [actions](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-intro#actions).

05. Configure the [DoS protection](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-dos-protection) thresholds.

06. Continue to **Access Control** tab and select [access controls](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-access-control) to enable.

07. Select the [bot protections](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-bot-protection) you want to enable.

08. Select the required [Custom rules](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-custom-rules).

09. Proceed to [Advanced settings](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-advanced-settings) for more WAAS controls.

10. Select **Save**.

11. The **Rule Overview** page shows all the WAAS rules created.











    Select a rule to display the **Rule Resources**, and for each application a list of protected endpoints and the protections enabled for each endpoint are displayed.

12. Test protected endpoint using the following [sanity tests](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-app-firewall#sanity-tests).

13. Go to **Monitor > Events**, click on **WAAS for containers/hosts/App-Embedded**, and observe the events generated.











    For more information, see the [WAAS analytics help page](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-analytics).


[PreviousDeploying WAAS](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas) [NextDeploy WAAS Out-Of-Band for Containers](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas/deploy-oob-containers)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject

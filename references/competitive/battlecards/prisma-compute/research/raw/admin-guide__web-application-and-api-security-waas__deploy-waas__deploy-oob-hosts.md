For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas/deploy-oob-hosts.md).

Create a new rule to deploy WAAS [Out-Of-Band](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-intro#waasoob) for Hosts for Linux Operating System. Out-Of-Band for hosts is not supported for Windows.

## Prerequisites[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas/deploy-oob-hosts\#prerequisites)

- You have [installed a Host Defender](https://docs.prismacloud.io/admin-guide/install/deploy-defender/defender-types) in your workload environment.

- A TLS certificate in PEM format.


## Create a WAAS Rule for Out-Of-Band Network Traffic[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas/deploy-oob-hosts\#create-a-waas-rule-for-out-of-band-network-traffic)

To deploy WAAS for Out-Of-Band network traffic, create a new rule, define application endpoints, and select protections.

1. Open Console, and go to **Defend > WAAS > {Container\|Host} > Out-of-Band**.

2. Select **Add rule**.









1. Enter a **Rule Name**

2. Enter **Notes** (Optional) for describing the rule.


3. Choose the rule **Scope** by specifying the resource collection(s) to which it applies.















![waas select scope](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-cf791aae2511b3dd0f756efa465216a6a1c308f5%252Fwaas_select_scope.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=8133c28b12c89f48ed984abae5177ff0&sv=3)











Collections define a combination of hosts to which WAAS should attach itself to protect the web application:















![waas define host collection](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-0f441600401a85cc8b5cf3da22c8236579f60959%252Fwaas_define_host_collection.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=6496df193d736171b1aee5d61960d22d&sv=3)















![waas define collection oob hosts](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-347c61cbe6429b48e4e930203c586adadd053535%252Fwaas_define_collection_oob_hosts.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=01111250e438fbca33ab07f385714944&sv=3)











Applying a rule to all hosts/images using a wild card (`*`) is invalid and a waste of resources. WAAS only needs to be applied to hosts that run applications that transmit and receive HTTP/HTTPS traffic.

4. (Optional) Enable **API endpoint discovery**











When enabled, the Defender inspects the API traffic to and from the protected API. Defender reports a list of the endpoints and their resource path in **Compute > Monitor > WAAS > API discovery**.

5. (Optional) Enable **Automatically detect ports** for an endpoint to deploy WAAS protection on ports identified in the unprotected web apps report in **Monitor > WAAS > Unprotected web apps** for each of the workloads in the rule scope.











As an additional measure, you can specify additional ports by specifying them in the protected HTTP endpoints within each app to also include the ports that may not have been detected automatically.











By enabling both **Automatically detect ports** and **API endpoint discovery**, you can monitor your API endpoints and ports without having to add an application and without configuring any policies.

6. **Save** the rule.


## Add an App (policy) to the Rule[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas/deploy-oob-hosts\#add-an-app-policy-to-the-rule)

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











       Protecting Linux-based hosts does not require specifying a `WAAS port` since WAAS listens on the same port as the protected application. Because Windows has its own internal traffic routing mechanisms, WAAS and the protected application cannot use the same `App port`. Consequently, when protecting Windows-based hosts the `WAAS port` should be set to the port end-users send requests to, and the `App port` should be set to a **different** port on which the protected application will listen and to which WAAS will forward traffic.

    5. If your application uses TLS, set **TLS** to **On**.











       You can select the TLS protocol (1.0, 1.1, 1.2, and 1.3 for WAAS In-Line, and 1.0, 1.1, and 1.2 for WAAS Out-Of-Band) to protect the API endpoint and enter the TLS certificate in PEM format.











       **Limitations**









       1. TLS connections using extended\_master\_secret(23) in the negotiation are not supported as part of this feature.

       2. DHKE is not supported due to a lack of information required to generate the encryption key.

       3. Out-of-Band does not support HTTP/2 protocol.

       4. TLS inspection for Out-of-Band WAAS is not supported on earlier versions of Console and Defender.









          - If your application uses HTTP/2, set **HTTP/2** to **On**.











            WAAS must be able to decrypt and inspect HTTPS traffic to function properly.

          - If your application uses gRPC, set **gRPC** to **On**.


    6. Select **Create response header**.

    7. To facilitate inspection, after creating all endpoints, click **View TLS settings** in the endpoint setup menu.











       WAAS TLS settings:















       ![waas oob tls](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-fe39b20192ef1465a012596ecfd56e336db9be6f%252Fwaas-oob-tls.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=6d712d520dd8e1538fa6620a4ca6ecec&sv=3)









       - **Certificate** \- Copy and paste your server’s certificate and private key into the certificate input box (e.g., `cat server-cert.pem server-key > certs.pem`).


    8. If you application requires [API protection](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-api-protection), for each path define the allowed methods and the parameters.


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


## WAAS Actions for Out-Of-Band traffic[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas/deploy-oob-hosts\#waas-actions-for-out-of-band-traffic)

The following actions are applicable for the HTTP requests or responses related to the **Out-Of-Band traffic**:

- **Alert** \- An audit is generated for visibility.

- **Disable** \- The WAAS action is disabled.


## Troubleshooting[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas/deploy-oob-hosts\#troubleshooting)

**No inspection generated by WAAS Out-Of-Band for TLS protocol**

Ensure that the requests use a supported TLS protocol and cipher suite, and respect the limitations listed in the Limitations section.

[PreviousDeploy WAAS for Hosts](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas/deployment-hosts) [NextDeploy WAAS for App-Embedded](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas/deployment-app-embedded)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject

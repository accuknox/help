> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/runtime-security/waas/deploy-waas/oob-containers.md).

# Deploy WAAS Out-Of-Band for Containers

Create a new rule to deploy WAAS [Out-Of-Band](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/enterprise-edition/content-collections/runtime-security/waas/waas.md#waasoob) for Containers.

## Prerequisites

* Install a [Container Defender](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/enterprise-edition/content-collections/runtime-security/install/deploy-defender/kubernetes/kubernetes.md) in your workload environment.
* Configure a TLS certificate in PEM format.
* When activating WAAS OOB on K8s clusters, increase the Pod limit to 4GB.

  For more information, see the [Increase the Defender Pod Limit](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/enterprise-edition/content-collections/runtime-security/install/deploy-defender/kubernetes/kubernetes.md#increasing-pod-limit) topic.

## Create a WAAS rule for Out-Of-Band network traffic

To deploy WAAS for Out-Of-Band network traffic, create a new rule, define application endpoints, and select protections.

1. Open Console, and go to **Runtime Security > Defend > WAAS > {Container|Host} > Out-of-Band**.
2. Select **Add rule**.
   1. Enter a **Rule Name**
   2. Enter **Notes** (Optional) for describing the rule.
3. Choose the rule **Scope** by specifying the resource collection(s) to which it applies.

   <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-cf791aae2511b3dd0f756efa465216a6a1c308f5%2Fwaas-select-scope.png?alt=media" alt="waas select scope"><figcaption></figcaption></figure>

   Collections define a combination of image names and one or more elements to which WAAS should attach itself to protect the web application:

   <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-32e0366fca578a62074bf1d0cb20f66b2a91193d%2Fwaas-define-collection.png?alt=media" alt="waas define collection"><figcaption></figcaption></figure>

   Applying a rule to all images using a wild card (`*`) is invalid - instead, only specify your web application images.

   When deploying WAAS OOB on K8s cluster, increase the `cgroup` limit to 4 GB to avoid [Kubernetes CrashLoopBackOff Error](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/enterprise-edition/content-collections/runtime-security/install/deploy-defender/kubernetes/kubernetes.md).
4. (Optional) Enable **API endpoint discovery**

   When enabled, the Defender inspects the API traffic to and from the protected API. Defender reports a list of the endpoints and their resource path in **Runtime Security > Monitor > WAAS > API discovery**.
5. (Optional) Enable **Automatically detect ports** for an endpoint to deploy WAAS protection on ports identified in the unprotected web apps report in **Runtime Security > Monitor > WAAS > Unprotected web apps** for each of the workloads in the rule scope.

   As an additional measure, you can specify additional ports by specifying them in the protected HTTP endpoints within each app to also include the ports that may not have been detected automatically.

   By enabling both **Automatically detect ports** and **API endpoint discovery**, you can monitor your API endpoints and ports without having to add an application and without configuring any policies.
6. **Save** the rule.

## Add an App (policy) to the rule

1. Select a WAAS rule to add an App in.
2. Select **Add app**.
3. In the **App Definition** tab, enter an **App ID**.

   The combination of **Rule name** and **App ID** must be unique across In-Line and Out-Of-Band WAAS policies for Containers, Hosts, and App-Embedded.

   If you have a Swagger or OpenAPI file, click **Import**, and select the file to load.

   If you do not have a Swagger or OpenAPI file, manually define each endpoint by specifying the host, port, and path.

   1. In **Endpoint Setup**, click **Add Endpoint**.

      Specify endpoint in your web application that should be protected. Each defined application can have multiple protected endpoints.
   2. Enter **HTTP host** (optional, wildcards supported).

      HTTP hostnames are specified in the form of \[hostname]:\[external port].

      The external port is defined as the TCP port on the host, listening for inbound HTTP traffic. If the value of the external port is "80" for non-TLS endpoints or "443" for TLS endpoints it can be omitted. Examples: "\*.example.site", "docs.example.site", "[www.example.site:8080](http://www.example.site:8080)", etc.
   3. Enter **App ports** as the internal port your app listens on.

      (You can skip to enter App ports, if you selected **Automatically detect ports** while creating the rule).

      When **Automatically detect ports** is selected, any ports specified in a protected endpoint definition will be appended to the list of protected ports. Specify the TCP port listening for inbound HTTP traffic.

      If your application uses **TLS** or **gRPC**, you must specify a port number.
   4. Enter **Base path** (optional, wildcards supported):

      Base path for WAAS to match when applying protections.

      Examples: "/admin", "/" (root path only), "/\*", /v2/api", etc.
   5. If your application uses TLS, set **TLS** to **On**.

      You can select the TLS protocol (1.0, 1.1, 1.2, and 1.3 for WAAS In-Line, and 1.0, 1.1, and 1.2 for WAAS Out-Of-Band) to protect the API endpoint and enter the TLS certificate in PEM format.

      **Limitations**

      1. TLS connections using extended\_master\_secret(23) in the negotiation are not supported as part of this feature.
      2. DHKE is not supported due to a lack of information required to generate the encryption key.
      3. Out-of-Band does not support HTTP/2 protocol.
      4. TLS inspection for Out-of-Band WAAS is not supported on earlier versions of Console and Defender.
         * If your application uses HTTP/2, set **HTTP/2** to **On**.

           WAAS must be able to decrypt and inspect HTTPS traffic to function properly.
         * If your application uses gRPC, set **gRPC** to **On**.
   6. Select **Create response header**.
   7. To facilitate inspection, after creating all endpoints, click **View TLS settings** in the endpoint setup menu.

      WAAS TLS settings:

      <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-fe39b20192ef1465a012596ecfd56e336db9be6f%2Fwaas-oob-tls.png?alt=media" alt="waas oob tls"><figcaption></figcaption></figure>

      * **Certificate** - Copy and paste your server’s certificate and private key into the certificate input box (e.g., `cat server-cert.pem server-key > certs.pem`).
   8. If you application requires [API protection](/content-collections/runtime-security/waas/waas-api-protection.md), for each path define the allowed methods and the parameters.
4. Continue to **App Firewall** settings, select the [protections](/content-collections/runtime-security/waas/waas-app-firewall.md) to enable and assign them with [../waas.xml](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/enterprise-edition/content-collections/runtime-security/waas/waas.md#actions).
5. Configure the [DoS protection](/content-collections/runtime-security/waas/waas-dos-protection.md) thresholds.
6. Continue to **Access Control** tab and select [access controls](/content-collections/runtime-security/waas/waas-access-control.md) to enable.
7. Select the [bot protections](/content-collections/runtime-security/waas/waas-bot-protection.md) you want to enable.
8. Select the required [Custom rules](/content-collections/runtime-security/waas/waas-custom-rules.md).
9. Proceed to [Advanced settings](/content-collections/runtime-security/waas/waas-advanced-settings.md) for more WAAS controls.
10. Select **Save**.
11. The **Rule Overview** page shows all the WAAS rules created.

    Select a rule to display the **Rule Resources**, and for each application a list of protected endpoints and the protections enabled for each endpoint are displayed.
12. Test protected endpoint using the following [sanity tests](/content-collections/runtime-security/waas/waas-app-firewall.md#sanity-tests).
13. Go to **Runtime Security > Monitor > Events**, click on **WAAS for containers/hosts/App-Embedded**, and observe the events generated.

    For more information, see the [WAAS analytics help page](/content-collections/runtime-security/waas/waas-analytics.md)

## WAAS Actions for Out-Of-Band traffic

The following actions are applicable for the HTTP requests or responses related to the **Out-Of-Band traffic**:

* **Alert** - An audit is generated for visibility.
* **Disable** - The WAAS action is disabled.

## Troubleshooting

**No inspection generated by WAAS Out-Of-Band for TLS protocol**

Ensure that the requests use a supported TLS protocol and cipher suite, and respect the limitations listed in the Limitations section.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/runtime-security/waas/deploy-waas/oob-containers.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

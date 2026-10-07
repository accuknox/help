For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/configure/proxy.md).

In some environments, access to the internet must go through a proxy and you can configure Prisma Cloud to route requests through your proxy. Proxy settings can either be applied to both Console and Defender containers or separately for each Defender deployment.

The global proxy settings are configured in the UI after Console is installed. Console starts using these settings after you apply it. Any Defenders deployed after you configure the proxy settings will use it unless you explicitly choose a different proxy when deploying the Defenders. Any Defenders that were deployed before you saved your proxy settings must be redeployed.

## Console[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/proxy\#console)

Console has a number of connections that might traverse a proxy.

![configure proxy console](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-608ef29f075346e1e1301bd6850efc9551484439%252Fconfigure_proxy_console.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=086e78296b0c44dd92532ac46b44d95f&sv=3)

- Retrieving Intelligence Stream updates.

- Connecting to services, such as Slack and JIRA, to push alerts.


## Defenders[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/proxy\#defenders)

Defender has a number of connections that might traverse a proxy.

![configure proxy defender](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-1463965012ad8cc132db1be9420362890098fa16%252Fconfigure_proxy_defender.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=e60efa989f7cd4480f202285a44f845b&sv=3)

- Connecting to Console.











If you have a proxy or a load balancer between Defender and Console, make sure that TLS interception is not enabled. The certificate and keys used for the Console to Defender mutual TLS v1.2 web socket session cannot be intercepted. This ensures that the Console is only communicating with the Defenders it has deployed and the Defenders only communicate with the Console that manages them.

- Connecting to external systems, such as Docker Hub or Google Container Registry, for scanning.

- Connecting to your secrets store to retrieve secrets for injection into your containers.


## Global proxy settings[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/proxy\#global-proxy-settings)

A number of settings let you specify how Prisma Cloud interfaces with your proxy.

### Proxy bypass[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/proxy\#proxy-bypass)

You can provide a list of addresses—DNS names, IP addresses, or a combination of both—that Prisma Cloud can contact directly without connecting through the proxy. Specifying IP addresses in CIDR notation is supported. Specifying DNS names using wildcards is supported.

### CA certificate[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/proxy\#ca-certificate)

Console verifies server certificates for all TLS connections. With TLS intercept proxies, the connection from Console to the Internet passes through a proxy, which may be transparent. To facilitate traffic inspection, the proxy terminates the TLS connection and establishes a new connection to the final destination.

If you have a TLS intercept proxy, it will break the Console’s ability to connect to external services, because Console won’t be able to verify the proxy’s certificate. To get Console to trust the proxy, provide the CA certificates for Console to trust. And, ensure that your proxy uses the client certificate of the Defender when it sends requests from the Defender to the Console.

### Proxy authentication[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/proxy\#proxy-authentication)

If egress connections through your proxy require authentication, you can provide the credentials in Prisma Cloud’s proxy settings. Prisma Cloud supports [Basic authentication](https://tools.ietf.org/html/rfc7617) for the Proxy-Authenticate challenge-response framework defined in [RFC 7235](https://tools.ietf.org/html/rfc7235). When you provide a username and password, Prisma Cloud submits the credentials in the request’s Proxy-Authorization header.

## Configuring global proxy settings[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/proxy\#configuring-global-proxy-settings)

Configure your proxy settings in Console.

1. Open Console, and go to **Manage > System > Proxy**.

2. In **HTTP Proxy**, enter the address of the web proxy. Specify the address in the following format: <PROTOCOL>://<IP\_ADDR\|DNS\_NAME>:<PORT>, such as [http://proxyserver.company.com:8080](http://proxyserver.company.com:8080/).

3. (Optional) In **No Proxy**, enter addresses that Prisma Cloud can access directly without connecting to the proxy. Enter a list of IP addresses and domain names. Specifying IP addresses in CIDR notation is supported. Specifying DNS names using wildcards is supported.

4. (Required for TLS intercept proxies only) Enable trusted communication to the Prisma Cloud Console.











The proxy must trust the Prisma Cloud Console Certificate Authority (CA) and use the client certificate of the Defender when the proxy sends requests from the Defender to the console.









1. Enter the proxy root CA, in PEM format that Console should trust.

2. Configure the proxy to use the Defender client-certificate when it opens a TLS connection to the Console.











      Use the `/api/v1/certs/server-certs.sh` API to obtain the following files:









      - The client key of the Defender: `defender-client-key.pem`

      - The client certificate of the Defender: `defender-client-cert.pem`

      - The Prisma Cloud Console CA certificate: `ca.pem`


5. (Optional) If your proxy requires authentication, enter a username and password.

6. Click **Save**.

7. Redeploy your Defenders to propagate updated proxy settings to them.











Console does not need to be restarted. After proxy settings are saved, Console automatically uses the settings the next time it establishes a connection.











Any newly deployed Defenders will use your proxy settings.











Any already deployed Defenders must be redeployed. For single Container Defenders, uninstall then reinstall. For Defender DaemonSets, regenerate the DaemonSet YAML, then redeploy.

















AskCopy



```
$ kubectl apply -f defender.yaml
```


## Configuring per-deployment proxy settings[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/proxy\#configuring-per-deployment-proxy-settings)

Prisma Cloud supports setting custom proxy settings for each Defender deployment. This way you can set multiple proxies for Defenders which are deployed in different environments.

1. Open Console, and go to **Manage > Defenders > Deploy**.

2. Choose your preferred deployment method.

3. Click on **Specify a proxy for the defender (optional)** and enter your proxy details.


## Supported Proxy Workflows[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/proxy\#supported-proxy-workflows)

The following proxy configurations have been tested and are officially supported in Prisma Cloud deployments:

- **Defender → Proxy → Console**: Defenders communicate with the Console through the proxy to send real-time runtime activity, policy violation alerts, detected vulnerabilities, compliance scan results, and performance or health metrics of protected workloads.

- **Console → Proxy → Defender**: The Console communicates with Defenders through the proxy for operations like configuration and status checks, or sending security policies updates and authentication details (certificates and credentials).

- **Console → Proxy → Intelligence**: The Console retrieves intelligence stream updates through the proxy to ensure up-to-date vulnerability information.


### Limitations[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/proxy\#limitations)

The following scenarios have not been tested and are therefore not officially supported:

- **Defender → Proxy → External Services**: Defenders communicating with external services (for example, S3 or ECR) using the proxy might not adhere to the configured No Proxy settings. This can lead to unexpected traffic patterns, such as S3 requests being routed through the proxy even when excluded through the No Proxy rules.

- **Custom Proxy Configurations for Registry Scanning**: While Defenders can scan container registries like Amazon ECR, configurations requiring Defenders to bypass the proxy for S3 or ECR endpoints (e.g., using No Proxy rules) are not guaranteed to work.


[PreviousCustom feeds](https://docs.prismacloud.io/admin-guide/configure/custom-feeds) [NextCertificates](https://docs.prismacloud.io/admin-guide/configure/certificates)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject

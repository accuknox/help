For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas/deployment-troubleshooting.md).

## Troubleshooting Container or Host Rules[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas/deployment-troubleshooting\#troubleshooting-container-or-host-rules)

Follow these steps to troubleshoot WAAS issues using the table below:

1. Ensure the protected container or host is protected by WAAS - a green firewall icon should appear next to the workload’s radar entity and a "WAAS" tab should appear when clicked.

2. Click on the workload in the radar and open [`WAAS connectivity monitor`](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas/deployment-troubleshooting#connectivity-monitor) by clicking on the WAAS tab.

3. Click on `Reset` to reset all counters.

4. Send one or more HTTP requests to the protected application

5. Click on `Refresh` and match changes in the request counters to the `Connectivity Monitor Indications` column in the table below

6. If the `WAAS errors` counter has been incremented, click on `View recent errors` to view errors.

7. A section of [`troubleshooting potential outcomes`](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas/deployment-troubleshooting#outcomes) is provided below, along with possible causes and solutions.


## WAAS connectivity monitor[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas/deployment-troubleshooting\#waas-connectivity-monitor)

[WAAS](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-intro) connectivity monitor monitors the connection between WAAS and the protected application.

WAAS connectivity monitor aggregates data on pages served by WAAS and the application responses.

In addition, it provides easy access to WAAS related errors registered in the Defender logs (Defenders sends logs to the Console every hour).

The monitor tab becomes available when you click on an image or host protected by [WAAS](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-intro).

![waas radar monitor](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-1b7bec594bdcb9bcc2ea92223cd55129d2d16e13%252Fwaas_radar_monitor.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=d9557f39aa3d97b89244bfb683db268a&sv=3)

- **Last updated** \- Most recent time when WAAS monitoring data was sent from the Defenders to the Console (Defender logs are sent to the Console on an hourly basis). By clicking on the **refresh** button users can initiate sending of newer data.

- **Aggregation start time** \- Time when data aggregation began. By clicking on the **reset** button users can reset all counters.

- **WAAS errors** \- To view recent errors related to a monitored image or host, click the **View recent errors** link.

- **WAAS statistics:**









  - _Incoming requests_ \- Count of HTTP requests inspected by WAAS since the start of aggregation.

  - _Forwarded requests_ \- Count of HTTP requests forwarded by WAAS to the protected application.

  - _Interstitial pages served_ \- Count of interstitial pages served by WAAS (interstitial pages are served once [Prisma Sessions Cookies](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-advanced-settings#prisma-session) are enabled).

  - _reCAPTCHAs served_ \- Count of reCAPTCHA challenges served by WAAS (when enabled as part of [bot protection](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-bot-protection)).


- **Application statistics**









  - Count of server responses returned from the protected application to WAAS grouped by HTTP response code prefix

  - Count of timeouts (a timeout is counted when a request is forwarded by WAAS to the protected application with no response received within the set timeout period).


Existing WAAS and application statistics counts will be lost once users reset the aggregation start time. `Reset` will **not** affect WAAS errors and will not cause recent errors to be lost.

For further details on WAAS deployment, monitoring and troubleshooting please refer to the [WAAS deployment page](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/waas/deploy-waas/deploy-waas.md).

## Troubleshooting Potential Outcomes[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas/deployment-troubleshooting\#troubleshooting-potential-outcomes)

### Application is not responding[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas/deployment-troubleshooting\#application-is-not-responding)

Possible reasons

Connectivity Monitor Indications

Solution

A problem with the protected application

\- `Incoming requests` is incremented. - `Forwarded requests` is incremented. - `Timeouts` is incremented.

Not a WAAS issue, check the application error logs. Disable WAAS rule and check if the problem persists.

TLS related issues: - Expired certificate - Protected application is using TLS, but TLS was not enabled in app

\- None of the counters is getting incremented. - `WAAS Errors` counter incremented.

Click on `View recent errors` in the [`WAAS connectivity monitor`](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/waas/deploy-waas/deployment-troubleshooting.xml#connectivity-monitor) to view errors. If the application is communicating over TLS: - Ensure TLS toggle is enabled - Ensure certificates are valid

`Prisma Session Cookies` is enabled and the client accessing the application does not support both cookies and Javascript.

\- ``Incoming requests are incremented. - `Interstitial pages served`` counter is incremented. - None of the Application Statistics counters is incremented.

Disable `Prisma Session Cookies` and validate the issue is resolved. Ensure clients accessing the protected application support both cookies and Javascript before re-enabling `Prisma Session Cookies`. Please see [`Prisma Session Cookies`](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/waas/waas-advanced-settings.xml#prisma-session) section for more details.

`reCAPTCHA` is enabled and clients and preventing clients from reaching the protected application.

\- `Incoming requests` is incremented. - `reCAPTCHAs served` is incremented. - None of the Application Statistics counters is incremented.

Disable `reCAPTCHA` and validate the issue is resolved. Verify that all legitimate clients accessing the protected application are able to solve the challenge presented. Please see [`reCAPTCHA`](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/waas/waas-bot-protection.xml#recaptcha) section for more details.

### Application is responding as expected yet WAAS protections do not trigger[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas/deployment-troubleshooting\#application-is-responding-as-expected-yet-waas-protections-do-not-trigger)

Possible reasons

Connectivity Monitor Indications

Solution

Minimum version requirements of Defenders for a protection or a feature are not met.

\- For new deployment methods (e.g. Out-of-band, VPC traffic mirroring) - WAAS will not get deployed and the WAAS tab will not be available on the radar view. - For new features added to existing deployment methods, WAAS operations will continue as usual while new features will not function

Verify that all Defenders meet the minimum requirement stated in the feature documentation before enabling it.

WAAS port is not properly configured.

`Incoming requests` is not incremented

The `App port` should be set to the port on which the protected application is listening. For containers the app port should be set to the exposed port on the container (not necessarily the same as the publicly exposed port).

Workload is not included in rule scope.

The workload radar entity does not have a firewall icon next to it, and the WAAS tab is not available when clicked.

Navigate to the relevant WAAS rule ( **Defend → WAAS**) and click on `Show` in the `Entities in scope` column. Verify the workload is not in scope and adjust scope to include it.

Workload is included in the scope of two WAAS rules (only first by order will match).

The workload radar entity does not have a firewall icon next to it, and the WAAS tab is not available when clicked.

Navigate to the relevant WAAS rule ( **Defend → WAAS**). Click the `Show` link under the `Entities in scope` column of each rule to check whether the protected workload is included in the scope of two or more rules. Whenever several rules apply to the same scope, only the first rule by order will match. Ensure that the desired rule matches first by altering rule scope collections or reordering rules.

HTTP hostname is included in the scope of two or more apps under the same WAAS rules (only first app by order will match).

\- `Incoming requests` is incremented. - `Forwarded requests` is incremented. - `Application statistics` counters are incremented.

Navigate to the relevant WAAS rule ( **Defend → WAAS**) and select the relevant WAAS rule. Check the order of the apps (policies) in the rule. Whenever multiple apps are defined in the same rule only the first app by order will match.

Request URL is not included in the list of protected endpoints.

Green firewall icon should appear next to the workload’s radar entity None of the counters is getting incremented

Navigate to the relevant WAAS rule ( **Defend → WAAS**) and select the relevant WAAS rule. Open the app and ensure the request URL is listed under protected endpoints: - Verify base path ends with an `*` to include all subpaths - Verify HTTP hostname in the request matches the listed HTTP hostnames - Verify scheme in the request matches the scheme in the protected endpoints list (TLS is enabled/disabled accordingly)

### Application is responding with HTTP errors (3XX, 4XX, 5XX)[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas/deployment-troubleshooting\#application-is-responding-with-http-errors-3xx-4xx-5xx)

Possible reasons

Connectivity Monitor Indications

Solution

Errors are generated by WAAS (requests are not forwarded to the protected application)

\- None of the Application Statistics counters is incremented. - `WAAS Errors` counter incremented.

Click on `View recent errors` in the [`WAAS connectivity monitor`](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/waas/deploy-waas/deployment-troubleshooting.xml#connectivity-monitor) to view errors.

Errors are generated by the protected application

\- `Incoming requests` is incremented. - `Forwarded requests` is incremented. - `Application statistics` 3XX, 4XX or 5XX counters are incremented.

Check the protected application logs for errors.

Multiple servers configured in NGINX

\- Application statistics 3XX, 4XX or 5XX counters are incremented.

Create a PCSUP to get engineering guidance on how to resolve this issue. To the ticket please attach the Nginx configs and output of the `netstat` command for port 80, `sudo netstat -nlp | grep 80`.

### WAAS is blocking legitimate requests[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas/deployment-troubleshooting\#waas-is-blocking-legitimate-requests)

Possible reasons

Connectivity Monitor Indications

Solution

False positive

\- `Incoming requests` is incremented. - `Forwarded requests` is incremented. - `Application statistics` counters are incremented.

Navigate to [WAAS analytics](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-analytics) ( **Monitor → Events → WAAS for containers/hosts**) and review audits generated. Add [exceptions](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/waas/waas-app-firewall.xml#firewall-exceptions) to protections causing false triggers.

### WAAS events all have the same attacker IP (private IP)[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas/deployment-troubleshooting\#waas-events-all-have-the-same-attacker-ip-private-ip)

Possible reasons

Connectivity Monitor Indications

Solution

Ingress controller is not set as a transparent proxy

\- `Incoming requests` is incremented. - `Forwarded requests` is incremented. - `Application statistics` counters are incremented.

Configure ingress controller as transparent proxy (enable “X-Forwarded-For” and “X-Forwarded-Host” HTTP headers).

### WaitCondition received failed message: 'Defender deployment failed' for uniqueid: i-xxxx.[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas/deployment-troubleshooting\#waitcondition-received-failed-message-defender-deployment-failed-for-uniqueid-i-xxxx)

AWS CloudFormation stack failed to deploy the WAAS agentless resources because Prisma Console is not accessible from AWS.

![err4 failedcondition received](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-172c491bcc58fb74b18b298370330687c12fa77e%252Ferr4-failedcondition-received.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=3cfa53b248af292b6d54ad0e5612487a&sv=3)

1. Make sure that the IP address of Prisma Console in the VPC configuration is public.

2. Check if the Defender instance has a public IP address.

3. Check if [AWS account can connect with the Prisma Cloud Console](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts/onboard-aws) with Console URL that you selected in the VPC configuration.









1. If the Console is not reachable, delete the rule and create a new rule with a valid Prisma Cloud Console URL.

2. If the Console is not reachable due to a firewall rule or other blocking rules, fix the rule to allow the connectivity to the Console, and click **Update** to retry the deployment.

3. Ensure that the Console’s IP address and the ports are reachable by the Defender. Also, the firewall is open with the relevant port and source IPs.


[PreviousDeploy WAAS Agentless](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas/deployment-vpc-mirroring) [NextWAAS Sanity Tests](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas/deployment-sanity-tests)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject

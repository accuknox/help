For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-app-firewall.md).

WAAS Firewall settings control the application firewall’s protections, actions, and exceptions.

![waas firewall protections](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-2df5906aa3b8a9293bcdb873e0eca5d267c91fd2%252Fwaas_firewall_protections.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=cdd6636b72e955c2e399cdc65db8ee6e&sv=3)

The following protections are available for Container, Host, and App-Embedded rules. Serverless rules have a limited set of protections focusing mostly on OWASP Top-10 attacks.

## OWASP Top 10 Protection[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-app-firewall\#owasp-top-10-protection)

WAAS offers protection for the critical security risks described in the OWASP Top Ten list.

### SQL injection[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-app-firewall\#sql-injection)

An SQL injection (SQLi) attack occurs when an attacker inserts an SQL query into the input fields of a web application. A successful attack can read sensitive data from the database, modify data in the database, or run arbitrary commands.

WAAS parses and tokenizes input streams (request data) and then detects malicious attempts to inject unauthorized SQL queries.

### Cross Site Scripting[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-app-firewall\#cross-site-scripting)

Cross-Site Scripting (XSS) is a type of injection attack, in which malicious JavaScript snippets are injected into otherwise benign and trusted websites. Attackers try to trick the browser into switching to a Javascript context and executing arbitrary code.

WAAS parses and tokenizes input streams (request data) and then searches for matching fingerprints of known malicious attack patterns.

### Command & Code Injection[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-app-firewall\#command-and-code-injection)

Command injection is a form of attack in which attackers attempt to run arbitrary commands on the web application’s host. Code injection is a form of attack in which code is injected and interpreted by the application or other runtimes. Command and code payloads are either injected as part of HTTP requests or included from local or remote files (also known as File Inclusion).

WAAS inspects all HTTP requests sent to the application and protects against all types of injection attacks as well as local file inclusions.

Prisma Cloud architecture facilitates defense in-depth via multiple protection layers. Enabling [Runtime Protection](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/runtime-defense/runtime-defense.md) in addition to WAAS would allow profiling of the application and identifying any anomalies resulting from command or code injections (e.g. unexpected new processes or DNS queries)

### Local File Inclusion[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-app-firewall\#local-file-inclusion)

Local File Inclusion is a form of attack in which attackers attempt to gain unauthorized access to locally stored sensitive files on the web application host. Such access attempts are often made using directory traversal attacks or exploiting file inclusion vulnerabilities in the application.

WAAS inspects all HTTP requests sent to the application for local file inclusion attacks aiming at sensitive system files as well as other various traversal attempts.

### Attack Tool & Vulnerability Scanners[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-app-firewall\#attack-tool-and-vulnerability-scanners)

Vulnerability scanners are automated tools that scan web applications for known security vulnerabilities and misconfiguration.

Web crawlers are automated tools designed to systematically access and enumerate the content of web applications. Crawling can lead to data breaches by exposing resources that should not be publicly available, or revealing opportunities for hacking by exposing software versions, environment data, and so on.

WAAS is continuously updated with new signatures of widely used web attack arsenal, crawlers, and penetration testing tools.

## API Protection[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-app-firewall\#api-protection)

WAAS is able to enforce API security based on specifications provided in the form of [Swagger](https://swagger.io/) or [OpenAPI](https://www.openapis.org/) files. WAAS also allows for manual API definition. E.g. paths, allowed HTTP methods, parameter names, input types, value ranges, etc. Once defined, users can choose WAAS actions to apply for requests that do not comply with the API’s expected behavior.

For further details on configuring API protection please refer to the [API Protection](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-api-protection) help page.

## Security Misconfigurations[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-app-firewall\#security-misconfigurations)

### Shellshock[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-app-firewall\#shellshock)

Shellshock is a unique privilege escalation vulnerability that permits remote code execution. In unpatched versions of the bash shell interpreter, the Shellshock vulnerability lets attackers create environment variables with specially crafted values that contain code. As soon as the shell is invoked, the attacker’s code is executed.

WAAS checks for requests that are crafted to exploit the Shellshock vulnerability.

For more information about Shellshock, see [CVE-2014-6271](https://en.wikipedia.org/wiki/Shellshock_(software_bug)#Initial_report_(CVE-2014-6271)).

### Malformed Request Protection[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-app-firewall\#malformed-request-protection)

WAAS validates the structure of HTTP requests, automatically blocking those that are malformed.

Examples of malformed requests include:

- HTTP GET requests with a body.

- HTTP POST requests without a `Content-Length` header.


### Cross-site Request Forgery[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-app-firewall\#cross-site-request-forgery)

Cross-site request forgery (CSRF) attacks trick the victim’s browser into executing unwanted actions on a web application in which the victim is currently authenticated. WAAS mitigates CSRF attacks by intercepting responses and setting the 'SameSite' cookie attribute value to 'strict'. The 'SameSite' attribute prevents browsers from sending the cookie along with cross-site requests. It only permits the cookie to be sent along with same-site requests.

There are several techniques for mitigating CSRF, including synchronizer (anti-CSRF) tokens, which developers must implement as part of their web application. The synchronizer token pattern generates random challenge tokens associated with a user’s session. These tokens are inserted into forms as a hidden field, to be submitted along with your forms. If the server cannot validate the token, the server rejects the requested action.

The SameSite cookie attribute works as a complementary defense against CSRF, and helps mitigate against things such as faulty implementation of the synchronizer token pattern.

- When the SameSite attribute is not set, the cookie is always sent.

- With the SameSite attribute set to strict, the cookie is never sent in cross-site requests.

- With the SameSite attribute set to lax, the cookie is only sent on same-site requests or top-level navigation with a safe HTTP method, such as GET.


It is not sent with cross-domain POST requests or when loading the site in a cross-origin frame. It is sent when you navigate to a site by clicking on a <a href=…​> link that changes the URL in your browser’s address bar.

Currently, the [following browsers support the SameSite attribute](https://caniuse.com/#feat=same-site-cookie-attribute):

- Chrome 61 or later.

- Firefox 58 or later.


For more information about the SameSite attribute, see [https://tools.ietf.org/html/draft-west-first-party-cookies-07](https://tools.ietf.org/html/draft-west-first-party-cookies-07)

### Clickjacking[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-app-firewall\#clickjacking)

Web applications that permit their content to be embedded in a frame are at risk of clickjacking attacks. Attackers can exploit permissive settings to invisibly load the target website into their own site and trick users into clicking on links that they never intended to click.

WAAS modifies all response headers, setting the `X-Frame-Options` response header value to `SAMEORIGIN`. The `SAMEORIGIN` directive only permits a page to be displayed in a frame on the same origin as the page itself.

## Intelligence Gathering[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-app-firewall\#intelligence-gathering)

Error messages give attackers insight into the inner workings of your application. It is therefore important to prevent information leakage.

The following controls limit the exposure of sensitive information.

### Remove Server Fingerprints[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-app-firewall\#remove-server-fingerprints)

By gathering information about the software type and version used by the web application, attackers may learn about potentially known weaknesses and bugs and exploit them.

Eliminating unnecessary headers makes it more difficult for attackers to identify the frameworks that underpin your application.

Response headers that advertise your application’s web server and other server details should be scrubbed. WAAS automatically removes unnecessary headers, such as `X-Powered-By`, `Server`, `X-AspNet-Version`, and `X-AspNetMvc-Version`.

### Detect Information Leakage[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-app-firewall\#detect-information-leakage)

WAAS detects situations where the contents of critical files, such as _/etc/shadow_, _/etc/passwd_, and private keys, are contained in responses. WAAS will also detect when responses contain directory listings, output from php\_info() function calls, and other similar data leakage cases of potentially risky information.

### Prisma Cloud Advanced Threat Protection[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-app-firewall\#prisma-cloud-advanced-threat-protection)

Prisma Cloud Advanced Threat Protection (ATP) is a collection of malware signatures and IP reputation lists aggregated from commercial threat feeds, open source threat feeds, and Prisma Cloud Labs. It is delivered to your installation via the Prisma Cloud Intelligence Stream. The data in ATP is used by WAAS to detect suspicious communication with attacker controlled clients such as a botnet herders or C2 servers. For more details please click [here](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-advanced-threat-protection).

Prisma Cloud Advanced Threat Protection is not available when protecting Windows-based hosts.

## Firewall Actions[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-app-firewall\#firewall-actions)

Requests that trigger a WAAS protection are subject to one of the following actions:

- **Alert** \- The request is passed to the protected application and an audit is generated for visibility.

- **Prevent** \- The request is denied from reaching the protected application, an audit is generated and WAAS responds with an HTML page indicating the request was blocked.

- **Ban** \- Can be applied on either IP or [Prisma Session IDs](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-advanced-settings#prisma-session). All requests originating from the same IP/Prisma Session to the protected application are denied for the configured time period (default is 5 minutes) following the last detected attack.


A message at the top of the page indicates the entity by which the ban will be applied (IP or Prisma Session ID). When the X-Forwarded-For HTTP header is included in the request headers, the ban will apply to the first public IP; and if the rest of the X-Forwarded-For HTTP values are private IPs, the RemoteAddr addresses are used instead of the true client IP.

To enable ban by Prisma Session ID, [Prisma Session Cookies](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-advanced-settings#prisma-session) has to be enabled in the Advanced Settings tab. For more information please refer to the [Advanced Settings](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-advanced-settings#prisma-session) help page.

WAAS implements state, which is required for banning user sessions by IP address or Prisma Sessions. Because Defenders do not share state, any application that is replicated across multiple nodes must enable IP stickiness on the load balancer.

## Firewall Exceptions[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-app-firewall\#firewall-exceptions)

WAAS allows for fine-tuning to reduce false positives and tailor its protection to the application needs. Firewall exception will instruct WAAS to ignore the value of a parameter or HTTP Header when inspecting an HTTP request e.g. WAAS can ignore a query parameter named `comments` when inspecting a request for SQL injection attacks.

WAAS supports the following locations:

- **path** \- requests sent to the specified path will be excluded from inspection by the protection.

- **query** \- specify the name of a query parameter to be excluded in the form of a regular expression ([re2](https://github.com/google/re2/wiki/Syntax)), e.g. `^id$`.

- **query values** \- specify a payload pattern to be excluded in the form of a regular expression ([re2](https://github.com/google/re2/wiki/Syntax)), e.g. `^.*test[1-9]{1,6}$`.

- **form/multipart** \- specify the name of a body parameter (of type application/x-www-form-urlencoded or sent via a multipart HTTP request) to be excluded in the form of a regular expression ([re2](https://github.com/google/re2/wiki/Syntax)), e.g. `^comment$`

- **header** \- specify the name of an HTTP header to be excluded in the form of a regular expression (re2), e.g. `^X-API-.{3,5}$` or `^Host$`.

- **user-Agent** \- specify the User-Agent HTTP header value to be excluded in the form of a regular expression (re2), e.g. `^X-API-.{3,5}$` or `^Host$`.

- **cookie** \- specify the name of the cookie to be excluded in the form of a regular expression ([re2](https://github.com/google/re2/wiki/Syntax)), e.g. `^sessionID$`.

- **XML (body)** \- specify an XML element to be excluded. Objects can be of any data type. Path to the object should be specified in a custom path format - define an absolute path to the element, notation supports word characters (a-z, A-Z, 0-9, `_`, `-`) separated by `/` character. e.g: `/root/nested`, `/root/nested/id`. Excluding all objects by specifying only `/` is not supported.

- **JSON (body)** \- specify an object path to be excluded. Objects can be of any data type. Path to the object should be specified in a custom path format - define an absolute path to the element, notation supports word characters (a-z, A-Z, 0-9, `_`, `-`) separated by `/` character. e.g: `/root/nested`, `/root/nested/id`. Excluding all objects by specifying only `/` is not supported.

- **body** \- specify a payload pattern to be excluded in the form of a regular expression ([re2](https://github.com/google/re2/wiki/Syntax)), e.g. `^.*test[1-9]{1,6}$`.


**Body** exception type will match the provided pattern on the raw inspected body (based on the inspection size limit) even when not parsed. Other firewall exceptions are based on parameter names and will only be applied on requests that WAAS was able to parse correctly.

Every protection will have different locations available for exclusion based on the nature of threats.

### Adding a new exception[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-app-firewall\#adding-a-new-exception)

1. In the **App firewall** menu click on the icon for one of the OWASP Top-10 protections.

2. Click on the button

3. Select the location and name of the parameter / HTTP header to be excluded















![waas add new exception](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-2dc248ec305712ac4c50f51c1c014b87b8a02adf%252Fwaas_add_new_exception.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=6953722e1bef8f6af2afdc26233cca79&sv=3)

4. Select the location and name of the parameter / HTTP header to be excluded.











Every protection will have different locations available for exclusion based on the nature of threats.

5. Click on **Save Exception**.


### Managing exceptions[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-app-firewall\#managing-exceptions)

1. In the **App firewall** menu click on the icon for one of the OWASP Top-10 protections.

2. In the table, click on the exception you’d like to edit.

3. Edit the location and name of the parameter / HTTP header to be excluded.











Every protection will have different locations available for exclusion based on the nature of threats.

4. Click on **Done Editing**.


## cURL Test Commands[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-app-firewall\#curl-test-commands)

Below are curl-based tests that can be used to verify endpoints have been properly defined. Make sure all changes are saved prior to running these tests. The method for verifying test results differs according to the selected action:

- **Alert** \- Go to **Monitor > Events** to see alerts logged by Prisma Cloud relating to this policy violation.

- **Prevent** \- Commands return output similar to the following:

















AskCopy



```
HTTP/1.1 403 Forbidden
Date: Wed, 15 Jul 2020 12:51:50 GMT
Content-Type: text/html; charset=utf-8
```


In the following examples, replace `<http_hostname>` with your endpoint’s hostname and `<external_port>` with the web facing port of your application. For testing HTTP header access control, also replace `<http_header_name>` with the header name set in the rule and `<http_header_value>` with set values.

SQL injection:

AskCopy

```
curl -I http://<http_hostname>:<external_port>/\?id\=%27%20OR%20%271
```

Cross-site scripting:

AskCopy

```
curl -I http://<http_hostname>:<external_port>/\?id\=\<script\>alert\(\1\)\</script\>
```

OS command injection:

AskCopy

```
curl -I http://<http_hostname>:<external_port>/\?id\=%3B+%2Fsbin%2Fshutdown
```

Code injection:

AskCopy

```
curl -I http://<http_hostname>:<external_port>/\?id\=phpinfo\(\)
```

Local file inclusion:

AskCopy

```
curl -I http://<http_hostname>:<external_port>/\?id\=../etc/passwd
```

Attack tools and vulnerability scanners:

AskCopy

```
curl -I -H 'User-Agent: sqlmap' http://<http_hostname>:<external_port>/
```

Shellshock protection:

AskCopy

```
curl -I -H "User-Agent: () { :; }; /bin/eject" http://<http_hostname>:<external_port>/
```

Malformed HTTP request:

AskCopy

```
curl -s -i -X GET -o /dev/null -D - -d '{"test":"test"}' http://<http_hostname>:<external_port>/
```

HTTP header access controls:

AskCopy

```
curl -H '<header_Name>: <header_value>' http://<http_hostname>:<external_port>/
```

[PreviousWAAS explorer](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-explorer) [NextAPI protection](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-api-protection)

Last updated 2 months ago

Was this helpful?

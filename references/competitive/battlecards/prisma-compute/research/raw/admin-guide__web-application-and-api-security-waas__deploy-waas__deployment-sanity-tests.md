For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas/deployment-sanity-tests.md).

Below are curl-based tests that can be used to verify endpoints have been properly defined. Make sure all changes are saved before running these tests. The method for verifying test results differs according to the selected action:

- **Alert** \- Go to **Monitor > Events** to see alerts logged by Prisma Cloud relating to this policy violation.

- **Prevent** \- Commands return output similar to the following:

















AskCopy



```
HTTP/1.1 403 Forbidden
Date: Wed, 15 Jul 2020 12:51:50 GMT
Content-Type: text/html; charset=utf-8
```


## cURL Test Commands[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas/deployment-sanity-tests\#curl-test-commands)

In the following examples, replace `<http_hostname>` with your endpoint’s hostname and `<external_port>` with the web-facing port of your application. For testing HTTP header access control, also replace `<http_header_name>` with the header name set in the rule and `<http_header_value>` with set values.

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

[PreviousTroubleshooting WAAS](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas/deployment-troubleshooting) [NextWAAS explorer](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-explorer)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject

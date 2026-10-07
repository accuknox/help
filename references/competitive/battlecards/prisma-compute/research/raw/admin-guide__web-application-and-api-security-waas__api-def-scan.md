For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/api-def-scan.md).

Prisma Cloud scans the API definition files and generates a report for any errors, or shortcomings such as structural issues, compromised security, best practices, and so on. API definition scan supports scanning OpenAPI 2.X and 3.X definition files in either YAML or JSON formats.

You can use the following methods to scan an API definition file:

- Upload API definition file to Console

- Run twistcli, a CLI tool aimed for CI/CD. Twistcli scans the API definition file and returns a full report with issues.

- Import an OpenAPI definition file into a WAAS app: When you import an OpenAPI definition file into a WAAS app, the Console automatically scans for issues. You can view the full report of the scan by navigating to **Monitor** \> **WAAS** \> **API definition scan**.


## twistcli reference for scanning API definition files[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/api-def-scan\#twistcli-reference-for-scanning-api-definition-files)

Run the following command:

AskCopy

```
$ ./twistcli waas openapi-scan </path/to/file/example.yaml>
```

**Syntax**:

AskCopy

```
twistcli waas openapi-scan [command options] [arguments...]
```

**OPTIONS**:

- address value: Prisma Cloud Console URL. This is the value twistcli uses to connect to Console (required) (default: "https://127.0.0.1:8083")

- exit-on-error: Immediately exits scan if an error is encountered (not supported with --containerized)

- password value, -p value: Password for authenticating with Prisma Cloud Console. For Prisma Cloud Enterprise Edition, specify the secret key associated with the access key ID passed to --user \[$TWISTLOCK\_PASSWORD\]

- project value: Target project

- tlscacert value: Path to Prisma Cloud CA certificate file

- token value: Token for authenticating with Prisma Cloud Console

- user value, -u value: User for authenticating with Prisma Cloud Console. For Prisma Cloud Enterprise Edition, specify an access key ID (default: "admin") \[$TWISTLOCK\_USER\]


## Upload API definition file[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/api-def-scan\#upload-api-definition-file)

To import an API definition file, follow the steps below:

1. Open the Console, and go to **Monitor > WAAS > API definition scan**.

2. **Upload** an API definition scan file.











The following screenshot shows the API definition scan files:















![api def scan list](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-d2718c6c94ba1940ad4932241524855d2b28c501%252Fapi_def_scan_list.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=b62b0d443d76d4bcb9f38ce9aaa04c87&sv=3)











You can also filter the API definition files by using the scan date, import source, or file name.


## View API definition scan report details[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/api-def-scan\#view-api-definition-scan-report-details)

1. Open the Console, and go to go to **Monitor > WAAS > API definition scan**.











API definition scan reports are available along with the description of the file source such as twistcli scan, upload to the console, or WAAS app (where the file was imported).

2. In the **Actions** column, click **View**.











The following screenshot shows the severity of issues and their related categories:















![api def scan issues](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-b0eba1494afebf3411f913bb5c22e90f2c60cabc%252Fapi_def_scan_issues.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=6aec9cf3a5781f43ead16e6d25e7e6c9&sv=3)

3. To view detailed information such as reference to the file, issue link, and so on for a specific issue, click on an issue under the **Findings** column.











The following screenshot shows a preview of various locations and details in the Openapi spec file for a selected issue:















![api def scan issue number](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-04bbd25e1d409034fa6f766d764020299123ffda%252Fapi_def_scan_issue_number.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=2aee25ed089a97dbdb760ee892808e7f&sv=3)


[PreviousAPI Discovery](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-api-discovery) [NextCustom rules](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-custom-rules)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject

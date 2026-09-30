> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/runtime-security/waas/scan-api-definition.md).

# API Definition Scan

Prisma Cloud scans the API definition files and generates a report for any errors, or shortcomings such as structural issues, compromised security, best practices, and so on. API definition scan supports scanning OpenAPI 2.X and 3.X definition files in either YAML or JSON formats.

You can use the following methods to scan an API definition file:

* Upload API definition file to Console
* Run twistcli, a CLI tool aimed for CI/CD. Twistcli scans the API definition file and returns a full report with issues.
* Import an OpenAPI definition file into a WAAS app: When you import an OpenAPI definition file into a WAAS app, the Console automatically scans for issues. You can view the full report of the scan by navigating to **Runtime Security > Monitor** > **WAAS** > **API definition scan**.

## `twistcli` reference for scanning API definition files

Run the following command:

```
$ ./twistcli waas openapi-scan </path/to/file/example.yaml>
```

**Syntax**:

```
twistcli waas openapi-scan [command options] [arguments...]
```

**OPTIONS**:

* address value: Prisma Cloud Console URL. This is the value twistcli uses to connect to Console (required) (default: "<https://127.0.0.1:8083>")
* exit-on-error: Immediately exits scan if an error is encountered (not supported with --containerized)
* password value, -p value: Password for authenticating with Prisma Cloud Console. For Prisma Cloud Enterprise Edition, specify the secret key associated with the access key ID passed to --user \[$TWISTLOCK\_PASSWORD]
* project value: Target project
* tlscacert value: Path to Prisma Cloud CA certificate file
* token value: Token for authenticating with Prisma Cloud Console
* user value, -u value: User for authenticating with Prisma Cloud Console. For Prisma Cloud Enterprise Edition, specify an access key ID (default: "admin") \[$TWISTLOCK\_USER]

## Upload API Definition File

To import an API definition file, follow the steps below:

1. Open the Console, and go to **Runtime Security > Monitor > WAAS > API definition scan**.
2. **Upload** an API definition scan file.

   The following screenshot shows the API definition scan files:

   <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-d2718c6c94ba1940ad4932241524855d2b28c501%2Fapi-def-scan-list.png?alt=media" alt="api def scan list"><figcaption></figcaption></figure>

   You can also filter the API definition files by using the scan date, import source, or file name.

Note: In case of any internal server errors, validate the API definition file for structural issues and upload it again.

## View API Definition Scan Report Details

1. Open the Console, and go to go to **Runtime Security > Monitor > WAAS > API definition scan**.

   API definition scan reports are available along with the description of the file source such as twistcli scan, upload to the console, or WAAS app (where the file was imported).
2. In the **Actions** column, click **View**.

   The following screenshot shows the severity of issues and their related categories:

   <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-b0eba1494afebf3411f913bb5c22e90f2c60cabc%2Fapi-def-scan-issues.png?alt=media" alt="api def scan issues"><figcaption></figcaption></figure>
3. To view detailed information such as reference to the file, issue link, and so on for a specific issue, click on an issue under the **Findings** column.

   The following screenshot shows a preview of various locations and details in the Openapi spec file for a selected issue:

   <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-04bbd25e1d409034fa6f766d764020299123ffda%2Fapi-def-scan-issue-number.png?alt=media" alt="api def scan issue number"><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/runtime-security/waas/scan-api-definition.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

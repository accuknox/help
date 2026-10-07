For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/tools/twistcli-scan-code-repos.md).

Prisma Cloud ships a command-line scanner for scanning code repos. It is supported on Linux, macOS, and Windows.

twistcli scans repositories locally and sends a bill of materials to Console for evaluation. Console assesses the components in the BoM against the latest threat data, and replies back to twistcli with the scan results.

The policy Console uses to assess a code repo is set in **Defend > Vulnerabilities > Code repositories > CI** and **Defend > Compliance > Code repositories > CI**.

By default, twistcli publishes scan results to Console. Scan results can viewed in Console under **Monitor > Vulnerabilities > Code repositories > CI**.

Many developers don’t have access to Prisma Cloud directly, but may want to run twistcli to evaluate a repo before code is submitted and a build job is initiated. twistcli has can print detailed results locally and optionally suppress publishing scan results to Console (which they might not be able to access anyway).

## Basic command line format and options[Direct link to heading](https://docs.prismacloud.io/admin-guide/tools/twistcli-scan-code-repos\#basic-command-line-format-and-options)

The basic command format is as follows:

AskCopy

```
twistcli coderepo scan <REPO_PATH> --repository <REPO_NAME>
```

Where:

- REPO\_PATH can be an absolute or relative path

- REPO\_NAME is the unique key that Console to identify the repo. If `--repository` isn’t specified, the repository’s path is used as the repository name.


## Print detailed scan results[Direct link to heading](https://docs.prismacloud.io/admin-guide/tools/twistcli-scan-code-repos\#print-detailed-scan-results)

Detailed result contain all dependencies files and a vulnerability distribution summary. For each dependency file that has any vulnerabilities, a table with information about the vulnerability is printed.

AskCopy

```
twistcli coderepo scan <REPO_PATH> --repository rowan --details
```

## Excluding files from a scan[Direct link to heading](https://docs.prismacloud.io/admin-guide/tools/twistcli-scan-code-repos\#excluding-files-from-a-scan)

To exclude files from the scan, use the `--excluded-paths` argument. Attach only a single value to the argument. The value should be a relative path from the root of the repository.

To exclude a file:

AskCopy

```
twistcli coderepo scan <REPO_PATH> --repository rowan --excluded-paths <PATH1>
```

To exclude multiple files, specify the `--excluded-paths` argument multiple times:

AskCopy

```
twistcli coderepo scan <REPO_PATH> --repository rowan --excluded-paths <PATH1> --excluded-paths <PATH2>
```

## Scanning specific files[Direct link to heading](https://docs.prismacloud.io/admin-guide/tools/twistcli-scan-code-repos\#scanning-specific-files)

To explicitly scan files scan use the `--explicit-files` argument. Specify one file per argument. For multiple files, specify multiple `--explicit-files` arguments.

## Suppress publishing results[Direct link to heading](https://docs.prismacloud.io/admin-guide/tools/twistcli-scan-code-repos\#suppress-publishing-results)

Using—​publish=false to avoid publishing the result to the console.

AskCopy

```
twistcli coderepo scan <REPO_PATH> --repository rowan --publish=false
```

[PreviousScan images with twistcli](https://docs.prismacloud.io/admin-guide/tools/twistcli-scan-images) [NextInstall Console with twistcli](https://docs.prismacloud.io/admin-guide/tools/twistcli-console-install)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject

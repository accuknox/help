For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/tools/twistcli.md).

Prisma Cloud ships a command-line configuration and control tool known as _twistcli_. It is supported on Linux, macOS, and Windows.

## Installing twistcli[Direct link to heading](https://docs.prismacloud.io/admin-guide/tools/twistcli\#installing-twistcli)

The _twistcli_ tool is delivered with every Prisma Cloud release. It is statically compiled, so it does not have any external dependencies, and it can run on any Linux host. No special installation is required. To run it, simply copy it to a host, and give it executable permissions. You need `sudo` privileges to run the `twistcli` command.

The _twistcli_ tool is available from the following sources.

- You can download _twistcli_ from the Prisma Cloud Console UI. Go to **Manage > System > Utilities**.















![twistcli download](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-c497fe57eb68fa3931662fbb687a8ea39cdec2d3%252Ftwistcli-download.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=645cf24fbb391868fb536ef30d5e6cfb&sv=3)











Choose the correct architecture and OS when downloading the `twistcli` command-line utility.

- You can download it from the API, which is a typical use case for automated workflows. For more information, see the `/api/v1/util` endpoint.


The requirements for running _twistcli_ are:

- The host running _twistcli_ must be able to connect to the Prisma Cloud Console over the network.

- For both image scanning and host scanning, Docker Engine must be installed on the executing machine.


## Connectivity to Console[Direct link to heading](https://docs.prismacloud.io/admin-guide/tools/twistcli\#connectivity-to-console)

Most _twistcli_ functions require connectivity to Console. All example commands specify a variable called COMPUTE\_CONSOLE, which represents the address for your Console.

## Functions[Direct link to heading](https://docs.prismacloud.io/admin-guide/tools/twistcli\#functions)

The _twistcli_ tool supports the following functions:

- _console_ — Installs and uninstalls Console into a cluster. Kubernetes and OpenShift are supported. You can also export Kubernetes or OpenShift deployment files in YAML format.

- _defender_ — Installs and uninstalls Defender into a cluster. Kubernetes and OpenShift are supported. Defender is installed as a daemon set (Kubernetes, OpenShift) which means one Defender is always automatically deployed to each node in the cluster. You can also export a Kubernetes or OpenShift deployment file in YAML format.

- _hosts_ — Scans hosts for vulnerabilities and compliance issues.

- _images_ — Scans container images for vulnerabilities and compliance issues. Because it runs from the command line, you can easily integrate Prisma Cloud’s scanning capabilities into your CI/CD pipeline.

- _intelligence_ — Retrieves the latest threat data from the Prisma Cloud Intelligence Stream, and push those updates to a Prisma Cloud installation running in an air-gapped environment.

- _tas_ — Scans VMware Tanzu droplets.

- _app-embedded_ — Embed the App Embedded Defender into a Dockerfile.

- _restore_ — Restore Console to the state stored in the specified backup file. An automated backup system (enabled by default) creates and maintains daily, weekly, and monthly backups. Additional backups can be made at any point in time from the Console UI.

- _serverless_ — Scans serverless functions for vulnerabilities.

- _support_ — Streamlines the process of collecting and sending debug information to Prisma Cloud’s support team. Collects log data from a node and uploads it to Prisma Cloud’s support area.


## Capabilities[Direct link to heading](https://docs.prismacloud.io/admin-guide/tools/twistcli\#capabilities)

The _twistcli_ tool offers feature parity across all supported operating systems, with a few exceptions. The following table highlights where functions are disabled, or work differently, on a given platform.

twistcli

Platform

Command

Subcommand

Linux

Linux ARM64

macOS

macOS ARM64

Windows

`console`

`export`

Yes

No

Yes

Yes

Yes

`install`

Yes

No

No

No

No

`uninstall`

Yes

No

No

No

No

`defender`

`export`

Yes

Yes

Yes

Yes

Yes

`install`

Yes

Yes

No

No

No

`uninstall`

Yes

Yes

No

No

No

`hosts`

`scan`

Yes

Yes

No1

No

No

`images`

`scan`

Yes

Yes

Yes2

Yes

Yes3

`intelligence`

`upload`

Yes

No

Yes

No

Yes

`download`

Yes

Yes

Yes

Yes

Yes

`tas`

`scan`

Yes

No

No

No

No

`app-embedded`

`embed`

Yes

No

Yes

No

Yes

`restore`

Yes

No

No

No

No

`serverless`

`scan`

Yes

No

Yes

No

Yes

`support`

`dump`

Yes

No

No4

No

No4

`upload`

Yes

Yes

Yes

Yes

Yes

`tas`

`scan`

Yes

Yes

No

No

No

`waas`

`openapi-scan`

Yes

Yes

Yes

Yes

Yes

1 Prisma Cloud doesn’t support deployment to macOS hosts, so there is no support for scanning macOS hosts.

2 Scans Linux images on macOS hosts. Docker for Mac must be installed.

3 Twistcli can scan Windows images on Windows Server 2016 and Windows Server 2019 hosts. To scan Linux images on Windows, install [Docker Machine on Windows](https://docs.docker.com/machine/overview/) with the Microsoft Hyper-V driver. Twistcli does not support scanning Linux images on Windows hosts with [Docker for Windows](https://docs.docker.com/docker-for-windows/).

4 The _support dump_ function collects Console’s logs when Console malfunctions. Copy _twistcli_ to host where Console runs, then execute _twistcli support dump_. Defender logs can be retrieved directly from the Console UI under **Manage > Defenders > Manage**.

For a comprehensive list of supported options for each subcommand, run:

AskCopy

```
$ twistcli <COMMAND> --help
```

## Install support[Direct link to heading](https://docs.prismacloud.io/admin-guide/tools/twistcli\#install-support)

Support for installing Console and Defender via _twistcli_ is supported on several cluster types. The following table highlights the available support:

twistcli

Platform

**Command**

**Subcommand**

**Stand-alone** **1**

**Kubernetes**

**OpenShift**

**Amazon ECS**

**Windows**

`console`

`export`

No

Yes

Yes

No

No

`install`

No

Yes

Yes

No

No

`uninstall`

No

Yes

Yes

No

No

`defender`

`export`

No

Yes

Yes

No

No

`install`

Yes

Yes

Yes

No

No

`uninstall`

No

Yes

Yes

No

No

1 Stand-alone refers to installing an instance of Console or Defender onto a single host that isn’t part of a cluster. For stand-alone installations of Console, use the _twistlock.sh_ script to install Onebox.

The _twistcli console install_ command for Kubernetes and OpenShift combines two steps into a single command to simplify how Console is deployed. This command internally generates a YAML configuration file and then creates Console’s resources with _kubectl create_ in a single shot. This command is only supported on Linux. Use it when you don’t need a copy of the YAML configuration file. Otherwise, use _twistcli console export_.

[PreviousTools](https://docs.prismacloud.io/admin-guide/tools/tools) [NextScan images with twistcli](https://docs.prismacloud.io/admin-guide/tools/twistcli-scan-images)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject

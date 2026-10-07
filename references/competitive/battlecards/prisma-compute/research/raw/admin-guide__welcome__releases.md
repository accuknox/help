For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/welcome/releases.md).

In general, you should stay on the latest major release unless you require a feature or fix from a subsequent maintenance release. We recommend that you upgrade to new major releases as they become available. For more information, see the [Prisma Cloud support lifecycle](https://docs.prismacloud.io/admin-guide/welcome/support-lifecycle).

The bell icon in the Console shows a notification when a new release is available.

## Downloading the software[Direct link to heading](https://docs.prismacloud.io/admin-guide/welcome/releases\#downloading-the-software)

Download the software from the Palo Alto Networks [Customer Support portal](https://support.paloaltonetworks.com/).

If you don’t see **Prisma Cloud Compute Edition** in the drop-down list, contact customer support. They’ll send you a direct link to the download. We are currently working on fixing all accounts that have this issue.

1. Log into the [Customer Support portal](https://support.paloaltonetworks.com/).

2. Go to **Updates > Software Updates**.

3. From the drop-down list, select **Prisma Cloud Compute Edition**. All releases available for download are displayed.















![releases csp](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-79caa99d3a5957c033869f0bba27485ff5c31170%252Freleases_csp.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=e47bd7838de59ac7afbe950ff36107d8&sv=3)


## Downloading the software programmatically[Direct link to heading](https://docs.prismacloud.io/admin-guide/welcome/releases\#downloading-the-software-programmatically)

Besides hosting the download on the Customer Support Portal, we also support programmatic download (e.g., curl, wget) of the release directly from our CDN. The link to the tarball is published in the release notes.

If you don’t see **Prisma Cloud Compute Edition** in the drop-down list, contact customer support. They’ll send you a direct link to the download. We are currently working on fixing all accounts that have this issue.

1. Log into the [Customer Support portal](https://support.paloaltonetworks.com/).

2. Go to **Updates > Software Updates**.

3. From the drop-down list, select **Prisma Cloud Compute Edition**. All releases available for download are displayed.

4. Open the releases notes PDF.















![releases pdf](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-7f4f37d628f273f7be43bd68beb959c4920a6abd%252Freleases_pdf.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=57040221ac46b5ef201e968e50b8ba32&sv=3)

5. Scroll down to the release information to get the link.















![releases direct link](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-4760de23868c053102825a43505ba1064a7d2237%252Freleases_direct_link.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=d622be414ca2eb17a8c4ff511868b8cc&sv=3)


## Open-source components[Direct link to heading](https://docs.prismacloud.io/admin-guide/welcome/releases\#open-source-components)

Prisma Cloud includes various open-source components, which may change between releases. Before installing Prisma Cloud, review the components and licenses listed in _prisma-oss-licenses.pdf_. This document is included with every release tarball. Changes to components or licenses between releases are highlighted.

A full listing of the open-source software and their licenses is also embedded in the Defender image. For example, to extract the listing from Defender running in a Kubernetes cluster, use the following command:

AskCopy

```
kubectl exec -ti -n twistlock <DEFENDER_POD> -- cat /usr/local/bin/prisma-oss-licenses.txt
```

## Code names[Direct link to heading](https://docs.prismacloud.io/admin-guide/welcome/releases\#code-names)

We often use code names when referring to upcoming releases. They’re convenient to use in roadmap presentations and other forward-looking communications. Code names tend to persist even after the release ships.

### Version to code name mapping[Direct link to heading](https://docs.prismacloud.io/admin-guide/welcome/releases\#version-to-code-name-mapping)

Version numbers indicate the date a release first shipped, along with the build number, as follows:

<YY>.<MM>.<BUILD-NUMBER>

For example, 22.01.840 is the Joule release, which first shipped in January 2022.

The following table maps versions to code names. The table is sorted from the newest (top) to the oldest release.

Version

Code name

Next Major release

O’Neal

31.xx.xxx

Newton

30.xx.xxx

Maxwell

`22.12.xxx`

Lagrange

`22.06.XXX`

Kepler

`22.01.XXX`

Joule

`21.08.XXX`

Iverson

[PreviousWelcome](https://docs.prismacloud.io/admin-guide) [NextGetting started](https://docs.prismacloud.io/admin-guide/welcome/getting-started)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject

For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-types/altered-binary.md).

An altered binary incident indicates that a binary that during image scanning was found with different metadata than what is specified by its package was executed. This binary might have been maliciously replaced or altered.

## Investigation[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-types/altered-binary\#investigation)

The following incident shows that the process _python2.7_ was launched, but it seems to be altered or corrupted.

![altered binary incident](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-8228d28fb9c756897ca0f94f5fbffde46d80364f%252Faltered_binary_incident.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=5d90fa64cca43c78e9d93785e5b592d0&sv=3)

Your investigation should focus on locating the source of the affected image.

If the image was pulled from a remote repository, you should confirm the image hash is as expected given the repository image metadata. You should make sure the image repository and the author are valid.

If the image was built locally, you must examine the build process. Inspect your supply chain to understand if any binary from signed sources (such as a package manager) is changed or modified throughout the build.

## Mitigation[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-types/altered-binary\#mitigation)

A full mitigation strategy for this incident begins by resolving the issues that allowed to pull or build an image including an altered binary.

Ensure that compliance benchmarks are appropriately applied to the affected images and containers. Use [Trusted Images](https://docs.prismacloud.io/admin-guide/compliance/trusted-images), to avoid image pulls from untrusted sources.

For additional protection, Enable the _block_ action in the applicable compliance check to take action when altered binaries are found in an image during a scan.

![altered binary compliance check](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-78c2765bbc4dcb853bbfb9ba0d19d771caf5ffc9%252Faltered_binary_compliance_check.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=15570bb39957f496db09c34173d8292e&sv=3)

[PreviousIncident types](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-types) [NextBackdoor admin accounts](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-types/backdoor-admin-accounts)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject

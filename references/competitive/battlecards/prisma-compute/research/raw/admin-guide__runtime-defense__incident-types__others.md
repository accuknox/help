For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-types/others.md).

- **Cloud Provider:** Indicates attempts to abuse a provider’s service to extract sensitive information.











For example: Container `A` queried provider API at `<IP_ADDRESS>`.

- **Data Exfiltration:** Indicates a potential compromise on a container because of a modified binary listening on a port. This typically leads with a DNS suspicious activity.











For example: Container process `/bin/bash` is listening on unexpected port `50000`.

- **Hijacked Process:** Indicates that an allowed process was used in a way that is inconsistent with its expected behavior. This can be a sign that a process has been used to compromise a container.


[PreviousSuspicious binary](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-types/suspicious-binary) [NextAccess control](https://docs.prismacloud.io/admin-guide/access-control/access-control)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject

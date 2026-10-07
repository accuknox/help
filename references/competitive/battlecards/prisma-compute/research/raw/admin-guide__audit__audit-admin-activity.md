For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/audit/audit-admin-activity.md).

All Prisma Cloud administrative activities are logged.

Changes to any settings (including previous and new values), changes to any rules (create, modify, or delete), changes to the credentials (create,modify, or delete), and all logon activity (success and failure) are logged. For every event, both the user name and source IP are captured.

Audit records for App-Embedded runtime audits, Trust audits, Container network firewall audits, and Host network firewall audits are retained for up to 25,000 entries or 50 MB, whichever limit is met first.

For login activity, the following events are captured:

- Every login attempt from the login page, including failures.

- Every failed attempt to authenticate to the API. Successfully authenticated calls to the API are not recorded.


The full set of log data is available to anyone with a [user role](https://docs.prismacloud.io/admin-guide/authentication/user-roles) of auditor or higher.

To view the administrative history, open Console, then go to **Manage > Logs > History**.

Settings, credentials, and rule events show how a configuration has changed. You can review the API endpoint, and a diff of the previous and current JSON objects. The following screenshot shows the changes to a vulnerability management rule:

![admin activity audit trail diff](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-e9c8563c27361006294f1e344b2ec77e5b75469d%252Fadmin_activity_audit_trail_diff.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=008758db93e37c054c4182716620f0e5&sv=3)

Use the [API reference](https://pan.dev/compute/api/get-policies-vulnerability-ci-images/) to view information on the API endpoint. The `/api/22.01/policies/vulnerability/ci/images` endpoint creates and modifies vulnerability rules for images scanned in the CI process. In this case, user `name obscured` has changed the threshold for the grace period for fixing Critical and High severity CVEs to 2 days and 4 days respectively after the vulnerability was published or disclosed.

[PreviousHost activity](https://docs.prismacloud.io/admin-guide/audit/host-activity) [NextAnnotate audits](https://docs.prismacloud.io/admin-guide/audit/annotate-audits)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject

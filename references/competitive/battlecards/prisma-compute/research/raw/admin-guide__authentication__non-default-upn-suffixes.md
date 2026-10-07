For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/authentication/non-default-upn-suffixes.md).

Active Directory allows administrators to [specify custom UPN suffixes](https://technet.microsoft.com/en-us/library/cc772007(v=ws.11).aspx) that can be applied to user accounts. The default UPN suffix for a user account is the Domain Name System (DNS) domain name of the domain that contains the user account. Microsoft refers to this as the [implicit UPN](https://msdn.microsoft.com/en-us/library/windows/desktop/aa380525(v=vs.85).aspx). Administrators may choose to add additional suffixes to shorten user names or provide consistent UPNs across a forest composed of multiple domains; these are known as explicit UPNs.

For example, if a domain is named domain.directory.company.com, the default UPN suffix would be domain.directory.company.com and users could logon with [username@domain.directory.company.com](mailto:username@domain.directory.company.com). However, an admin may want to simplify this and provide an alternative UPN suffix like @company.com that would apply to all users across a forest. Users could then logon with this explicit UPN of [username@company.com](mailto:username@company.com) instead.

Within the directory service, the userPrincipalName attribute is updated to reflect whatever username + UPN suffix the administrator applies to a given account. In Windows systems, the implicit UPN can be used in addition to whatever explicit UPN may be set. However, for non-Windows LDAP systems, **the explicit UPN is the only valid UPN that can be used with the user object**.

Thus, understanding the UPN assigned to a user account is critical to Prisma Cloud integration with Active Directory. Even if the domain name and the search path may use one set of names (such as dc=domain,dc=directory,dc=company,dc=com in our above example), the actual (explicit) UPN must be used for all actions within Prisma Cloud, such as adding users to the system or logging on. From our above example, this means that if the user in Active Directory has a UPN of [username@domain.directory.company.com](mailto:username@domain.directory.company.com) set on their account, this UPN must be used with Prisma Cloud. Alternatively, if an Active Directory admin has set another UPN, such as [username@company.com](mailto:username@company.com), that UPN must be used instead.

Any attempts to use a UPN not directly found in the userPrincipalName field on the user object will result in 'user not found' errors.

[PreviousOpenShift (OAuth 2.0)](https://docs.prismacloud.io/admin-guide/authentication/oauth2-openshift) [NextCompute user roles](https://docs.prismacloud.io/admin-guide/authentication/user-roles)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject

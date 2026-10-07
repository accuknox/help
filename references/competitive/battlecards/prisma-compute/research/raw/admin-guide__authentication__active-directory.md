For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/authentication/active-directory.md).

Prisma Cloud can integrate with Active Directory (AD), an enterprise identity directory service.

If your AD environment uses alternative UPN suffixes (also referred to as explicit UPNs), see [Non-default UPN suffixes](https://docs.prismacloud.io/admin-guide/authentication/non-default-upn-suffixes) to understand how to use them with Prisma Cloud.

LDAP group names are case sensitive in Prisma Cloud.

With AD integration, you can reuse the identities and groups centrally defined in Active Directory, and extend your organization’s access control policy to manage the data users can see and the things they can do in the Prisma Cloud Console.

For more information about Prisma Cloud’s built-in roles, see [User Roles](https://docs.prismacloud.io/admin-guide/authentication/user-roles).

## Configuration options[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/active-directory\#configuration-options)

The following configuration options are available:

Configuration option

Description

Enabled

Enables or disables integration with Active Directory.

In Console, use the slider to enable (ON) or disable (OFF) integration with AD.

By default, integration with AD is disabled.

URL

Specifies the path to your LDAP server, such as an Active Directory Domain Controller.

The format for the LDAP server path is:

<PROTOCOL>://<HOST>:<PORT> Where <PROTOCOL> can be ldap or ldaps. For an Active Directory Global Catalog server, use ldap.

For performance and redundancy, use a load balanced path.

Example: ldap://ldapserver.example.com:3268

Search Base

Specifies the search query base path for retrieving users from the directory.

Example: dc=example,dc=com

User identifier

User name format when authenticating

sAMAccountName = DOMAIN\\sAMAccountName

userPrincipalName = [user@ad.example.com](mailto:user@ad.example.com)

The Active Directory domain name must be provided when using sAMAccountName due to domain trust behavior.

Account UPN

Console Account UPN Specifies the username for the Prisma Cloud service account that has been set up to query Active Directory.

Specify the username with the User Principal Name (UPN) format:

<USERNAME>@<DOMAIN>

Example: [twistlock\_service@example.com](mailto:twistlock_service@example.com)

Account Password

Specifies the password for the Prisma Cloud service account.

## Integrating Active Directory[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/active-directory\#integrating-active-directory)

Integrate Active Directory after you have installed Prisma Cloud.

1. Open Console, then go to **Manage > Authentication > Identity Providers**.

2. Set **Integrate LDAP users and groups with Prisma Cloud** to **Enabled**.

3. Specify all the parameters for connecting to your Active Directory service.









1. For **Authentication** type, select **Active Directory**.

2. In **Path to LDAP service**, specify the path to your LDAP server.











      For example: `ldap://ldapserver.example.com:3268`

3. In **Search Base**, specify the base path to the subtree that contains your users.











      For example: `dc=example,dc=com`

4. In Service Account UPN and Service Account Password, specify the credentials for your service account.











      Specify the username in UPN format: <USERNAME>@<DOMAIN>











      For example, the account UPN format would be: `twistlock_service@example.com`

5. If you connect to Active Directory with ldaps, paste your CA certificate (PEM format) in the CA Certificate field.











      This enables Prisma Cloud to validate the LDAPS certificate to prevent spoofing and man- in-the-middle attacks. If this field is left blank, Prisma Cloud will not perform validation of the LDAPS certificate.


4. Click **Save**.


## Adding Active Directory group to Prisma Cloud[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/active-directory\#adding-active-directory-group-to-prisma-cloud)

To grant authentication to users in an Active Directory group, add the AD group to Prisma Cloud.

1. Navigate to **Manage > Authentication > Groups** and click **Add group**.

2. In the dialog, enter AD group name and select **LDAP group**.















![ldap group](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-63d3bd571882848b8c4709a746dba00383a221f4%252Fldap_group.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=2a9b8d3d8bc9ba84743ae6e6295a3bb2&sv=3)

3. Grant a [role](https://docs.prismacloud.io/admin-guide/authentication/user-roles) to members of the group.


## Verifying integration with Active Directory[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/active-directory\#verifying-integration-with-active-directory)

Verify the integration with AD.

1. Open Console.

2. If you are logged into Console, log out.















![logout](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-09795e2c020ef92cf57e8c75062bed42dae64550%252Flogout.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=9fa33172cd6166d0c45b0e599dc97981&sv=3)

3. At Console’s login page, enter the UPN and password of an existing Active Directory user.











If the log in is successful, you are directed to the view appropriate for the user’s role.


[PreviousIntegrate with an IdP](https://docs.prismacloud.io/admin-guide/authentication/identity-providers) [NextOpenLDAP](https://docs.prismacloud.io/admin-guide/authentication/openldap)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject

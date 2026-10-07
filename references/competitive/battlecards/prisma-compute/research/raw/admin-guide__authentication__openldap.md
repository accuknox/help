For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/authentication/openldap.md).

Prisma Cloud can integrate with OpenLDAP, an open source implementation of the Lightweight Directory Access Protocol.

Integrating Prisma Cloud with OpenLDAP lets users access Prisma Cloud using their LDAP credentials, and lets admins define granular access control rules to Docker Engine or Kubernetes using existing LDAP identities.

With OpenLDAP integration, you can:

- Re-use the identities and groups already set up in your OpenLDAP directory.


## Integrating OpenLDAP[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/openldap\#integrating-openldap)

This procedure shows you how to integrate OpenLDAP with Prisma Cloud.

**Prerequisites:**

- You have installed OpenLDAP 2.4.44 or later. Prisma Cloud has been tested with version 2.4.44. Integration with older versions should work as well, but isn’t officially supported.


01. In your LDAP directory, create a service account that has admin privileges and that can run ldapsearch queries.











    This admin account will be used by Prisma Cloud to authenticate users in your LDAP directory. It should be able to control the entire domain, and should therefore be created under the root OU.

02. Verify that the service account can query your LDAP directory.











    Run ldapsearch, passing it the credentials for your service account, and query your directory for a user:

















    AskCopy



    ```
    $ ldapsearch -x \
      -b dc=example,dc=com \
      -D "cn=<SA-CN>,dc=example,dc=com" \
      -w <SA-PASS>
      "(cn=<some-user-cn>)"
    ```









    Where:





























    `<SA-CN>`



















    Common name for the Prisma Cloud service account.























    `<SA-PASS>`



















    Password for the Prisma Cloud service account.























    `<some-user-cn>`



















    Common name for a user in your LDAP directory.

03. Open Console, and go to **Manage > Authentication > Identity Providers > LDAP**.

04. Set **Integrate LDAP users and groups with Prisma Cloud** to **Enabled**.

05. For **Authentication type**, select **OpenLDAP**.

06. For **Path to LDAP service**, enter the LDAP server and port number in the following format:











    For secure connections over TLS: `ldaps://<server-dns>:<port-number>`.











    For insecure connections: `ldap://<server-dns>:<port-number>`

07. For **Search base**, enter the base DN for your users and groups.

08. (OPTIONAL) For **User identifier**, specify an attribute to be used to match users.











    For example, enter uid to match users based on their user IDs.

09. For **Service account UPN**, enter the DN for your Prisma Cloud service account.

10. For **Service account password**, enter the password for the Prisma Cloud service account.

11. For **CA certificate**, provide the CA certificate used to sign the LDAPS certificate on the server.











    Prisma Cloud uses the CA certificate to validate the LDAPS certificate and prevent man-in-the-middle attacks. If you are using an insecure connection or do not wish to validate the LDAPS certificate, leave this field blank.

12. Click **Save**.











    Console verifies all your parameters with the server. If a connection cannot be established, an error message is shown and no parameters are saved.


## Verifying integration with OpenLDAP[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/openldap\#verifying-integration-with-openldap)

Verify the integration with OpenLDAP.

1. Open Console.

2. If you are logged into Console, log out.















![logout](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-09795e2c020ef92cf57e8c75062bed42dae64550%252Flogout.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=9fa33172cd6166d0c45b0e599dc97981&sv=3)

3. Log in to Console using the credentials of an existing OpenLDAP user.











If the log in is successful, you are directed to the view appropriate for the user’s role.


[PreviousActive Directory](https://docs.prismacloud.io/admin-guide/authentication/active-directory) [NextOpenID Connect](https://docs.prismacloud.io/admin-guide/authentication/oidc)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject

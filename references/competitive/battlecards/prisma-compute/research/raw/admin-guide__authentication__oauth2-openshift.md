For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/authentication/oauth2-openshift.md).

OpenShift users can log into Prisma Cloud Console using OpenShift as an OAuth 2.0 provider.

Prisma Cloud currently supports OpenShift Platform versions 4.5 and older as an OAuth 2.0 provider. We are working to add support for OpenShift versions 4.6 and later.

The OpenShift master includes a built-in OAuth server. You can integrate OpenShift authentication into Prisma Cloud. When users attempt to access Prisma Cloud, which is a protected resource, they are redirected to authenticate with OpenShift. After authenticating successfully, they are redirected back to Prisma Cloud Console with an OAuth token. This token scopes what the user can do in OpenShift. Prisma Cloud only needs the auth token to get the user’s info (e.g. user name, email), and check the Prisma Cloud database to see if this user is authorized. If so, Prisma Cloud creates a JWT token, with a [role](https://docs.prismacloud.io/admin-guide/authentication/user-roles) claim, to complete the authentication process to Console. Roles are assigned based on users and group information specified in Console.

The following diagram shows the login flow when the auth provider is LDAP. With LDAP, users enter their credentials in Prisma Cloud Console, and Prisma authenticates with the LDAP server on the user’s behalf. With all other auth providers, Prisma isn’t part of verifying the user credentials Instead Prisma redirects the client to the auth provider for authentication. Once the user successfully authenticates via the authentication provider, the client is redirected back to Prisma Cloud Console with an object (SAML assertion for SAML, JWT token for OIDC, Access token for OAuth 2.0) that proves a successful login or, in the OAuth 2.0 case, gives us access to the application to verify the user identity.

![oauth openshift flow](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-36945a8651cc4ddee1cf9f460cc8ea8356946b11%252Foauth_openshift_flow.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=bbe72eceda78d76ddf1c0c1ef5e238f8&sv=3)

Prisma Cloud supports the authorization code flow only.

## Integrate Prisma Cloud with OpenShift[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/oauth2-openshift\#integrate-prisma-cloud-with-openshift)

Configure Prisma Cloud so that OpenShift users can log into Prisma Cloud with the same identity.

01. In OpenShift, [register Prisma Cloud as an OAuth client](https://docs.openshift.com/container-platform/4.4/authentication/configuring-internal-oauth.html#oauth-register-additional-client_configuring-internal-oauth). Set the redirect URL to:











    https://<CONSOLE>:<PORT>/api/v1/authenticate/callback/oauth.

02. Log into Prisma Cloud Console.

03. Go to **Manage > Authentication > Identity Providers > OAuth 2.0**.

04. Set **Integrate Oauth 2.0 users and groups with Prisma Cloud** to **Enabled**.

05. Set **Identity provider** to **OpenShift**.

06. Set **Client ID** to the **name** of the OAuth client you set up in OpenShift.

07. Set **Client secret** to the **secret** in the OAuth client you set up in OpenShift.

08. Set **Auth URL** to **https://github.com/login/oauth/authorize**.

09. Set **Token URL** to **https://github.com/login/oauth/access\_token**.

10. In **User Info API URL**, enter the TCP endpoint for the OpenShift API server. For example, **https://openshift.default.svc.cluster.local**.

11. Click **Save**.


## Prisma Cloud to OpenShift user identity mappings[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/oauth2-openshift\#prisma-cloud-to-openshift-user-identity-mappings)

Create a Prisma Cloud user for every OpenShift user that should have access to Prisma Cloud.

After the user is authenticated, Prisma Cloud uses the access token to query OpenShift for the user’s information (user name, email). The user information returned from OpenShift is compared against the Prisma Cloud Console database to determine if the user is authorized. If so, a JWT token is returned.

1. Go to **Manage > Authentication > Users**.

2. Click **Add User**.

3. Set **Username** to the OpenShift user name.

4. Type a **Description** for the user (optional).

5. Set **Auth method** to **OAuth**.

6. Select a [role](https://docs.prismacloud.io/admin-guide/authentication/user-roles) for the user.

7. Click **Save**.

8. Test logging into Prisma Cloud Console.









1. Logout of Prisma Cloud.

2. On the login page, select **OAuth**, and then click **Login**.















      ![oauth2 login](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-0fc55a6b1a702abc17fa86d6524f1a32293ee0e4%252Foauth2_login.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=29d30f8d242726e77ad338d2e7a163d2&sv=3)

3. Authorize the Prisma Cloud OAuth App to sign you in.















      ![oauth2 github authorization](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-5e1fb19d336a3d97789248d1b12c6c05c3683dd6%252Foauth2_github_authorization.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=94f6289095df2ccf38b63d371b588250&sv=3)


### Prisma Cloud to OpenShift group mappings[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/oauth2-openshift\#prisma-cloud-to-openshift-group-mappings)

Use groups to streamline how Prisma Cloud roles are assigned to users. When you use groups to assign roles, you don’t have to create individual Prisma Cloud accounts for each user.

Groups can be associated and authenticated with by multiple identity providers.

1. Go to **Manage > Authentication > Groups**.

2. Click **Add Group**.

3. In **Name**, enter an OpenShift group name.

4. In **Authentication method**, select **External Providers**.

5. In **Authentication Providers**, select **OAuth group**.

6. Select a [role](https://docs.prismacloud.io/admin-guide/authentication/user-roles) for the members of the group.

7. Click **Save**.

8. Test logging into Prisma Cloud Console.









1. Logout of Prisma Cloud.

2. On the login page, select **OAuth**, and then click **Login**.















      ![oauth2 login](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-0fc55a6b1a702abc17fa86d6524f1a32293ee0e4%252Foauth2_login.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=29d30f8d242726e77ad338d2e7a163d2&sv=3)

3. Authorize the Prisma Cloud OAuth App to sign you in.


[PreviousGitHub (OAuth 2.0)](https://docs.prismacloud.io/admin-guide/authentication/oauth2-github) [NextActive Directory Non-default UPN suffixes](https://docs.prismacloud.io/admin-guide/authentication/non-default-upn-suffixes)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject

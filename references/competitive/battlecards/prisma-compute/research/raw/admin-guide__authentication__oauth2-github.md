For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/authentication/oauth2-github.md).

Prisma Cloud supports OAuth 2.0 as an authentication mechanism. GitHub users can log into Prisma Cloud Console using GitHub as an OAuth 2.0 provider.

Prisma Cloud supports the authorization code flow only.

A CA certificate configured in **Manage > Authentication > System certificates > Certificate-based authentication to Console** is not supported in GitHub.

## Configure Github as an OAuth provider[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/oauth2-github\#configure-github-as-an-oauth-provider)

Create an OAuth App in your GitHub organization so that users in the organization can log into Prisma Cloud using GitHub as an OAuth 2.0 provider.

1. Log into GitHub as the organization owner.

2. Go to **Settings > Developer Settings > OAuth Apps**, and click **New OAuth App** (or **Register an application** if this is your first app).

3. In **Application name**, enter **Prisma Cloud**.

4. In **Homepage URL**, enter the URL for Prisma Cloud Console in the format https://<CONSOLE>:<PORT>.

5. In **Authorization callback URL**, enter https://<CONSOLE>:<PORT>/api/v1/authenticate/callback/oauth.

6. Click **Register application**.

7. Copy the **Client ID** and **Client Secret**, and set them aside setting up the integration with Prisma Cloud.















![oauth2 github oauth app](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-d3fb590ecd30653255c57f7f3fc33be83986f0f4%252Foauth2_github_oauth_app.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=312859d5d8b802e3f2f9d94a2d571e78&sv=3)


## Integrate Prisma Cloud with GitHub[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/oauth2-github\#integrate-prisma-cloud-with-github)

Set up the integration so that GitHub users from your organization can log into Prisma Cloud.

1. Log into Prisma Cloud Console.

2. Go to **Manage > Authentication > Identity Providers > OAuth 2.0**.

3. Set **Integrate Oauth 2.0 users and groups with Prisma Cloud** to **Enabled**.

4. Set **Identity provider** to **GitHub**.

5. Set **Client ID** and **Client secret** to the values you copied from GitHub.

6. Set **Auth URL** to **https://github.com/login/oauth/authorize**.

7. Set **Token URL** to **https://github.com/login/oauth/access\_token**.

8. Click **Save**.


## Prisma Cloud to GitHub user identity mappings[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/oauth2-github\#prisma-cloud-to-github-user-identity-mappings)

Create a Prisma Cloud user for each GitHub user that should have access to Prisma Cloud.

After the user is authenticated, Prisma Cloud uses the access token to query GitHub for the user’s information (user name, email). The user information returned from GitHub is compared against the information in the Prisma Cloud Console database to determine if the user is authorized. If so, a JWT token is returned.

1. Go to **Manage > Authentication > Users**.

2. Click **Add User**.

3. Set **Username** to the GitHub user name.

4. In the **Description** field, enter additional details about the user (optional).

5. Set **Auth method** to **OAuth**.

6. Select a [role](https://docs.prismacloud.io/admin-guide/authentication/user-roles) for the user.

7. Click **Save**.

8. Test logging into Prisma Cloud Console.









1. Logout of Prisma Cloud.

2. On the login page, select **OAuth**, and then click **Login**.















      ![oauth2 login](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-0fc55a6b1a702abc17fa86d6524f1a32293ee0e4%252Foauth2_login.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=29d30f8d242726e77ad338d2e7a163d2&sv=3)

3. Authorize the Prisma Cloud OAuth App to sign you in.















      ![oauth2 github authorization](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-5e1fb19d336a3d97789248d1b12c6c05c3683dd6%252Foauth2_github_authorization.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=94f6289095df2ccf38b63d371b588250&sv=3)


### Prisma Cloud group to GitHub organization mappings[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/oauth2-github\#prisma-cloud-group-to-github-organization-mappings)

Use groups to streamline how Prisma Cloud roles are assigned to users. When you use groups to assign roles, you don’t have to create individual Prisma Cloud accounts for each user.

Groups can be associated and authenticated with by multiple identity providers.

1. Go to **Manage > Authentication > Groups**.

2. Click **Add Group**.

3. In **Name**, enter the GitHub organization.

4. In **Authentication method**, select **External Providers**.

5. In **Authentication Providers**, select **OAuth group**.

6. Select a [role](https://docs.prismacloud.io/admin-guide/authentication/user-roles) for the members of the organization.

7. Click **Save**.

8. Test logging into Prisma Cloud Console.









1. Logout of Prisma Cloud.

2. On the login page, select **OAuth**, and then click **Login**.















      ![oauth2 login](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-0fc55a6b1a702abc17fa86d6524f1a32293ee0e4%252Foauth2_login.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=29d30f8d242726e77ad338d2e7a163d2&sv=3)

3. Authorize the Prisma Cloud OAuth App to sign you in.















      ![oauth2 github authorization](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-5e1fb19d336a3d97789248d1b12c6c05c3683dd6%252Foauth2_github_authorization.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=94f6289095df2ccf38b63d371b588250&sv=3)


[PreviousActive Directory Federation Services (SAML 2.0)](https://docs.prismacloud.io/admin-guide/authentication/saml-active-directory-federation-services) [NextOpenShift (OAuth 2.0)](https://docs.prismacloud.io/admin-guide/authentication/oauth2-openshift)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject

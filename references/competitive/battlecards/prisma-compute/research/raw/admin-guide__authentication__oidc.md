For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/authentication/oidc.md).

OpenID Connect is a standard that extends OAuth 2.0 to add an identity layer. Prisma Cloud supports integration with any standard Open ID Connect (OIDC) provider that implements both OpenID connect core and OpenID connect discovery. Prisma Cloud supports the authorization code flow only.

This page includes instructions to integrate with the following providers:

- [PingOne](https://docs.prismacloud.io/admin-guide/authentication/oidc#pingone)

- [Okta](https://docs.prismacloud.io/admin-guide/authentication/oidc#okta)

- [Azure Active Directory](https://docs.prismacloud.io/admin-guide/authentication/oidc#azure-ad)


Use the **https://<CONSOLE>:<PORT>/api/v1/authenticate/callback/oidc** URL only to configure the integration between services. The API is not included in [our reference guide](https://pan.dev/compute/api/) because the URL is only enabled as a configuration value.

## PingOne[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/oidc\#pingone)

Integrate with PingOne.

You need to configure Compute as an OIDC app. When configuring your app:

- The Start SSO URL must point to the **https://<CONSOLE>:<PORT>/callback** URL.

- The Redirect URI must point to the **https://<CONSOLE>:<PORT>/api/v1/authenticate/callback/oidc** URL.

- UserInfo must include `sub`, `idpid`, and `name`.

- All of the following scopes must be included for OpenID.









  - OpenID Connect (openid)

  - OpenID profile

  - OpenID Email

  - OpenID address

  - OpenID Phone

  - Groups


### Update Ping callback URL[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/oidc\#update-ping-callback-url)

Update the callback URL.

1. Log into the Ping web portal.

2. Click **Applications**, and then click the **OIDC** tab.

3. Click on the arrow button nest for your app.

4. Click on the pencil icon on the right side.

5. Click on **Authentication Flow**.

6. In **REDIRECT URIS**, enter the following URL to enable the service-to-service integration:











**https://<CONSOLE>:<PORT>/api/v1/authenticate/callback/oidc**.


### Create new user and join to group[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/oidc\#create-new-user-and-join-to-group)

1. In the Ping web portal, click **Users**, and then click the **Users** tab.

2. Click **Add users**, and choose the **Create New User** option.

3. Fill the fields for **Password**, **Username** (should be your email), **First Name**, **Last Name**, and **Email**.

4. In the **Membership** field, click **Add**, and choose a group.

5. Click **Save**.


## Okta[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/oidc\#okta)

Integrate with Okta.

- Initiate Login URI (Okta) must point to **https://<CONSOLE>:<PORT>/callback**.

- Redirect URI must point to the **https://<CONSOLE>:<PORT>/api/v1/authenticate/callback/oidc** URL.

- UserInfo must include sub, idpid, name.

- Scopes:









  - All of the following scopes must be included for OpenID: OpenID Connect (openid), OpenID profile, OpenID Email, OpenID address, OpenID Phone, Groups.

  - All of the following scopes must be included for Okta: okta.groups.manage, okta.groups.read.


### Update Okta callback URL[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/oidc\#update-okta-callback-url)

Update the callback URL.

1. Log into Okta.

2. Click on **Applications** and click on your application.

3. Click the **General** tab, and then click **Edit**.

4. Update **Login redirect URIs**. Enter the following URL to enable the service-to-service integration:











**https://<CONSOLE>:<PORT>/api/v1/authenticate/callback/oidc**

5. Click **Save**.


### Configure Okta as an Identity Provider[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/oidc\#configure-okta-as-an-identity-provider)

Configure Okta as an identity provider in Prisma Cloud with the following steps.

1. Log into Prisma Cloud Console.

2. Go to **Manage > Authentication > Identity Providers > OpenID Connect**.

3. Enable OpenID Connect.

4. Fill in the settings.









1. For **Client ID**, enter the client ID.

2. For **Client Secret**, enter the client secret.

3. For **Issuer URL**, enter:











      **https://sso.connect.pingidentity.com/<CLIENT\_ID>**.

4. For **Group scope**, select **groups**.

5. (Optional) Enter your certificate.

6. Click **Save**.


## Azure Active Directory (AD)[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/oidc\#azure-active-directory-a-d)

To integrate with Azure Active Directory (AD), you must register Prisma Cloud as an Open ID Connect (OIDC) application in Azure and configure Azure AD as an identity provider in Prisma Cloud.

1. Go to [your Azure console](https://portal.azure.com/#home).

2. Find the Azure AD service.

3. Click the **app registration** button and select **New registration**

4. Enter a name and select **Accounts in this organizational directory only** as the supported account type.

5. Under **Redirect URI** select **Web console URL** enter the following URL to enable the service-to-service integration: **https://<CONSOLE>:<PORT>/api/v1/authenticate/callback/oidc**

6. Click on **Register the app**.

7. To add the secret for the client, go to **certificates & secrets**.

8. Add a new secret for the client, copy and store it for later use.











You can only view the value of the secret when you create it. Copy and store the secret safely for later use.


### Configure Groups in Azure AD[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/oidc\#configure-groups-in-azure-a-d)

1. To add the needed claim, go to **Token Configuration**.









1. Select **Add group claim**

2. Select the **Groups assigned to the application** option.

3. Keep the default values and click **Add**.

4. Click **Add optional claim** and select **Token type - ID**.

5. Select the **email** and **preferred\_username** claims.

6. Turn on the Microsoft Graph email permission, while saving these claims.















      ![oidc optional claim](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-eb3b32d819937ca3fde739c1d70b4c271d0a89a2%252Foidc_optional_claim.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=64114682c2183548212ea62a197826f2&sv=3)


2. Go to the **API permissions** and click **Add a permission**.









1. Under **Microsoft API** select **Microsoft Graph**.

2. Select **Delegated permissions**

3. Select **email, openid, profile**.















      ![oidc api permission](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-919f3021b009e4e24f16a1929234c865c08b8a0e%252Foidc_api_permission.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=8cd181ffc90da2ef790b346e06e0c9ca&sv=3)


3. To create the needed application group, go to **Groups** in the Azure AD console.

4. Create a new group and keep the default values.


### Assign the Created Group to the Prisma Cloud Console[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/oidc\#assign-the-created-group-to-the-prisma-cloud-console)

01. Go to **Enterprise applications** in the Azure AD console.

02. Find the application you registered.

03. Click on **Properties** and check the **Assignment required** option.

04. Click on **Assign users and groups**.

05. Click add and select the previously created group.

06. Click add and select your user.

07. Go to **App registrations** in the Azure AD console.

08. Click on **Your owned registered app**.

09. Find the application you registered and click on **Endpoints**.

10. Open the OpenID Connect metadata JSON file.

11. Copy the value under Issuer URL from the JSON file, for example: **https://login.microsoftonline.com/<TENANT\_ID>/v2.0**


### Configure Azure AD as an Identity Provider[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/oidc\#configure-azure-a-d-as-an-identity-provider)

After you register Prisma Cloud as an Open ID Connect (OIDC) application in Azure, complete the following steps to configure Azure AD as an identity provider.

1. Go to **Manage > Authentication > Identity Providers** in your Prisma Cloud Console.

2. Enable OpenID Connect.

3. Enter the following information in the settings fields.









1. **Client ID**: Use the **Application (Client) ID** found in the Azure Console under **Azure AD > App registrations > Overview**.















      ![oidc client id](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-7c235d77ff641ea39e7b89c69dc9e72bab4d99bd%252Foidc_client_id.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=018a33f07464d6bd562d14ae4a4e070e&sv=3)

2. **Client Secret**: The secret for the client that you created for the application and stored safely for later use.

3. **Issuer URL**: The endpoint of the application registered in Azure AD, for example **https://login.microsoftonline.com/<TENANT\_ID>/v2.0**

4. **Group scope**: Leave this field blank.

5. **Group claim**: Set this field to `groups`. This allows Prisma Cloud to populate the specific group names automatically.

6. **User claim**: The optional claim for the user. Set this field to `preferred_username` for group based OIDC authentication, it is used for the audit logs.















      ![oidc identity provider configuration](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-fbeae26d3badf063c142b6b9328c23b4ad870ce8%252Foidc_identity_provider_configuration.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=ff7c99ce426e2deae20919f2867ddce1&sv=3)


4. Click **Save**.


## Prisma Cloud to OIDC user identity mapping[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/oidc\#prisma-cloud-to-oidc-user-identity-mapping)

If you intend to use the group mapping method, skip to the [Prisma Cloud to OIDC provider group mapping](https://docs.prismacloud.io/admin-guide/authentication/oidc#group-mapping) task. Create a user for every user that should access Prisma Cloud. The Open ID Connect specification requires every username to match with a configured username in the Prisma Cloud database. Prisma Cloud uses attributes that come from OIDC to perform this match, for example you can use `sub`, `username` or `email`. You should use whichever value the provider is configured to send to Prisma Cloud when you configure users.

1. Go to **Manage > Authentication > Users**.

2. Click **Add User**.

3. Set **Username** to the GitHub user name.

4. Type a **Description** for the user.

5. Set **Auth method** to **OpenID Connect**.

6. Select a [role](https://docs.prismacloud.io/admin-guide/authentication/user-roles) for the user.

7. Click **Save**.

8. Test logging into Prisma Cloud Console.









1. Logout of Prisma Cloud.

2. On the login page, select **OpenID Connect**, and then click **Login**.















      ![oidc login](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-22daddd69edad12b8a09e94fb39168780cc54fbb%252Foidc_login.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=31e1990fc1805f843b3f22032fc5669a&sv=3)

3. You’re redirected to your OIDC provider to authenticate.

4. After successfully authenticating, you’re logged into Prisma Cloud Console.


## Prisma Cloud to OIDC provider group mapping[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/oidc\#prisma-cloud-to-oidc-provider-group-mapping)

When you use groups to assign roles in Prisma Cloud you don’t have to create individual Prisma Cloud accounts for each user. The group value configured on the Compute side should reflect the name of the group scope in the OIDC provider. It might be something different than groups.

Groups can be associated and authenticated with by multiple identity providers. If you use Azure Active Directory (AAD), a user can’t be part of more than 200 groups at once.

1. Go to **Manage > Authentication > Groups**.

2. Click **Add Group**.

3. In **Name**, enter an OpenShift group name. For AAD use Azure Group’s **Object ID** as the group name.

4. In **Authentication method**, select **External Providers**.

5. In **Authentication Providers**, select **OpenID Connect group**.

6. Select a [role](https://docs.prismacloud.io/admin-guide/authentication/user-roles) for the members of the group.

7. Click **Save**.

8. Test logging into Prisma Cloud Console.









1. Logout of Prisma Cloud.

2. On the login page, select **OpenID Connect**, and then click **Login**.















      ![oidc login](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-22daddd69edad12b8a09e94fb39168780cc54fbb%252Foidc_login.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=31e1990fc1805f843b3f22032fc5669a&sv=3)

3. You’re redirected to your OIDC provider to authenticate.

4. After successfully authenticating, you’re logged into Prisma Cloud Console.


[PreviousOpenLDAP](https://docs.prismacloud.io/admin-guide/authentication/openldap) [NextOkta (SAML 2.0)](https://docs.prismacloud.io/admin-guide/authentication/saml)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject

For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/authentication/saml-ping-federate.md).

Many organizations use SAML to authenticate users for web services. Prisma Cloud supports the SAML 2.0 federation protocol to access the Prisma Cloud Console. When SAML support is enabled, users can log into the Console with their federated credentials. This article provides detailed steps for federating your Prisma Cloud Console with your PingFederate v8.4 Identity Provider (IdP).

The Prisma Cloud/PingFederate SAML federation flow works as follows:

1. Users browse to Prisma Cloud Console.

2. Their browsers are redirected to the PingFederate SAML 2.0 endpoint.

3. They enter their credentials to authenticate. Multi-factor authentication can be enforced at this step.

4. A PingFederate SAML token is returned to Prisma Cloud Console.

5. Prisma Cloud Console validates the SAML token’s signature and associates the user to their Prisma Cloud account via user identity mapping or group membership.


Prisma Cloud Console is integrated with PingFederate as a federated SAML Service Provider. The steps to set up the integration are:

- [Configure PingFederate](https://docs.prismacloud.io/admin-guide/authentication/saml-ping-federate#_configure_pingfederate)

- [Configure Prisma Cloud Console](https://docs.prismacloud.io/admin-guide/authentication/saml-ping-federate#_configure_prisma_cloud_console)


## Configure PingFederate[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/saml-ping-federate\#configure-pingfederate)

01. Logon to PingFederate

02. Go to **IdP Configuration > SP Connection > Connection Type**, and select **Browser SSO**.















    ![ping saml step2](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-ba5f5bbf66faa1c901fe60f7a083304a897f7835%252Fping_saml_step2.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=94084d1dee60f283f6d48b6db7ae24df&sv=3)

03. Go to **IdP Configuration > SP Connection > Connection Options**, and select **Browser SSO Profiles SAML 2.0**.















    ![ping saml step3](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-ec07eaca76d1aa2df1902b8855bcda59fa138ad8%252Fping_saml_step3.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=c602de227a49aebf6940b07b9be31583&sv=3)

04. Skip the **Import Metadata** tab.

05. Go to **IdP Configuration > SP Connection > General Info**.









    1. In **Partner’s Entity ID**, enter **twistlock**.











       By default, the Partner’s Entity ID is "twistlock". When configuring the SAML Audience in the Prisma Cloud Console, the default value is "twistlock". If you choose a different value here, be sure to set the same value in your Console.

    2. In **Connection Name**, enter **Prisma Cloud Console**.

    3. Click **Add**.















       ![ping saml step5](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-0dc3c736dc36d350d7f82a45e90449c599fc7695%252Fping_saml_step5.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=22661fd263bca988bf7eae86b9435154&sv=3)


06. In **Browser SSO > SAML Profiles**, select both **IDP-INITIATED SSO** and **SP-INITIATED SSO**.















    ![ping saml step6](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-a265691ab43e41b7c91af675587b6b02f521e56e%252Fping_saml_step6.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=9d1c253772bc10812629e09f6735b721&sv=3)

07. Go to **Assertion Creation** and set **SAML\_SUBJECT** to **SAML 1.1 nameid-format**.











    In this example you mapped the user’s email address to the SAML\_SUBJECT attribute which matches the user’s Prisma Cloud account. If you are using group-to-Prisma Cloud-role associations, add **groups** to the list of attributes to be returned in the SAML token.















    ![ping saml step7](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-e208bf028bad6edf2a41f47e7808f5d543a37544%252Fping_saml_step7.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=fa7e00783e15c7e04d08bf08f4f3eed8&sv=3)

08. In **IdP Configuration > SP Connection > Browser SSO > Protocol Settings > Assertion Consumer Service URL**, specify an assertion consumer URL.









    1. Under **Binding**, select **POST**.

    2. Under **Endpoint URL**, enter **https://<FQDN\_OF\_YOUR\_TWISTLOCK\_CONSOLE>:8083/api/v1/authenticate**.















       ![ping saml step8](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-7c850c405fd849e93f7fd614552752abddf85340%252Fping_saml_step8.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=55fcae99e029045269aa39848eda26ce&sv=3)


09. In **IdP Configuration > SP Connection > Browser SSO > Protocol Settings > Signature Policy**, leave both values unchecked.















    ![ping saml step9](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-ebd214db1d5c744bc65d3ba937ee14825f9437a3%252Fping_saml_step9.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=5d83cf189807bf9919de00f3b1b74821&sv=3)

10. In **IdP Configuration > SP Connection > Browser SSO > Protocol Settings**, review the protocol settings.















    ![ping saml step10](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-f7fbb074af854b5c322469f67a83fb04f78d8484%252Fping_saml_step10.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=b5a7c321191e223dd1e49f7451018339&sv=3)

11. Click **Done**.

12. Copy the PingFederate SAML token signing X.509 certificate as Base64 in **Server Configuration**. This certificate will be imported into Prisma Cloud Console.


## Configure Prisma Cloud Console[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/saml-ping-federate\#configure-prisma-cloud-console)

Configure Prisma Cloud Console.

1. Login to the Prisma Cloud Console as an administrator.

2. Go to **Manage > Authentication > Identity Providers > SAML**.

3. Set **Integrate SAML users and groups with Prisma Cloud** to **Enabled**.

4. Set **Identity Provider** to **Ping**.

5. In **Identity provider single sign-on URL**, enter your PingFederate IdP endpoint.

6. In **Identity provider issuer**, enter your PingFederate Entity ID.

7. In **Audience**, enter **twistlock** (default) or the value you set for Partner’s Entity ID in PingFederate.









1. In **X.509 certificate**, paste your PingFederate X.509 **Signing Certificate Base64**.















      ![ping saml step11](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-433a30543aad95b6b936bdd63c83fc03f99d847d%252Fping_saml_step11.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=f12e0910fbab00e3d3b1edec1a7f66b5&sv=3)


8. Click **Save**.


## User account name matching[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/saml-ping-federate\#user-account-name-matching)

User account name matching.

1. Go to **Manage > Authentication > Users**.

2. Click **Add user**.

3. Create a new user:









1. In **Username**, enter the value returned within the SAML\_SUBJECT attribute _IdP user’s email address_.

2. In **Description**, enter additional details about the user (optional).

3. In **Role**, select the appropriate role.

4. Set **Create user in local Prisma Cloud account database** to **Off**.















      ![ping saml step12](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-61f7de52da0d9cb2a3c02a0820a1ac5704a43466%252Fping_saml_step12.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=fef10e904be1030232a0be1d66dc2593&sv=3)


4. Click **Save**.

5. Test login into the Prisma Cloud Console via PingFederate SAML federation.











Leave your existing session logged onto the Prisma Cloud Console in case you encounter issues. Open a new incognito browser window and go to **https://<CONSOLE>:8083**.


## Group name matching[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/saml-ping-federate\#group-name-matching)

Group name matching.

1. Go to **Manage > Authentication > Groups**.

2. Click the **+Add Group** button.

3. In the **Name** field, enter a group name.











The group name must exactly match the group name in the SAML IDP. Console does not verify if that the value entered matches a group name in the SAML IDP.

4. Select the **SAML group** checkbox.















![ping saml step13](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-b250d92e0967486cbcbefc651627581d802bc700%252Fping_saml_step13.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=6584153a596d5e0b81d35baa344c383e&sv=3)

5. Click **Save**

6. Test login into the Prisma Cloud Console via PingFederate SAML federation.











Leave your existing session logged onto the Prisma Cloud Console in case you encounter issues. Open a new incognito browser window and go to **https://<CONSOLE>:8083**.


[PreviousAzure Active Directory (SAML 2.0)](https://docs.prismacloud.io/admin-guide/authentication/saml-azure-active-directory) [NextActive Directory Federation Services (SAML 2.0)](https://docs.prismacloud.io/admin-guide/authentication/saml-active-directory-federation-services)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject

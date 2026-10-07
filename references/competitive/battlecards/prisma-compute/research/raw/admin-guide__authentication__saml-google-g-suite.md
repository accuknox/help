For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/authentication/saml-google-g-suite.md).

Many organizations use SAML to authenticate users for web services. Prisma Cloud supports the SAML 2.0 federation protocol to access the Prisma Cloud Console. When SAML support is enabled, users can log into Console with their federated credentials. This article provides detailed steps for federating your Prisma Cloud Console with Google G Suite.

The Prisma Cloud/G Suite SAML federation flow works as follows:

1. Users browse to Prisma Cloud Console.

2. Their browsers are redirected to the G Suite SAML 2.0 endpoint.

3. They enter their credentials to authenticate. Multi-factor authentication can be enforced at this step.

4. A SAML token is returned to Prisma Cloud Console.

5. Prisma Cloud Console validates the SAML token’s signature and associates the user to their Prisma Cloud account via user identity mapping or group membership.


## Setting up Google G Suite[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/saml-google-g-suite\#setting-up-google-g-suite)

Prisma Cloud supports SAML integration with Google G Suite.

01. Log into your G Suite admin console.

02. Click on **Apps**.















    ![integrate g suite 791235](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-2a363b297d8d7e7f1f97a5853d216cf539d5d24e%252Fintegrate_g_suite_791235.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=9b4c49f09d2689046154998c23b51d94&sv=3)

03. Click on **SAML apps**.















    ![integrate g suite 791236](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-03caac8e542a52617188f5a0934d4fd477193ce6%252Fintegrate_g_suite_791236.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=129b8b0c90ae72da7a77acf58fb14aee&sv=3)

04. Click the **+** button at the bottom to add a new app.

05. Click **SETUP MY OWN CUSTOM APP** at the bottom of the dialog.

06. Copy the **SSO URL** and **Entity ID**, and download the certificate. You will need these later for setting up the integration in Prisma Cloud Console. Click **NEXT**.















    ![integrate g suite 791271](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-83b93b1a865fa6f90cecd626e7146b55a2d0f83b%252Fintegrate_g_suite_791271.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=7ca3546236be5806800e3e1caac5366b&sv=3)

07. Enter an **Application Name**, such as **Prisma Cloud**, then click **NEXT**.

08. In the Service Provider Details dialog, enter the following details, then click **NEXT**.









    1. In **ACS URL**, enter: **https://<CONSOLE\_IPADDR \| CONSOLE\_HOSTNAME>:8083/api/v1/authenticate**.

    2. In **Entity ID**, enter: **twistlock**.

    3. Enable **Signed Response**.















       ![integrate g suite 791240](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-6498cd743ed98f33085e8c0cca49eaeaaff72956%252Fintegrate_g_suite_791240.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=f2fd6bc9b5cdc27116bc8a1a4dd992a4&sv=3)


09. Click **FINISH**, then **OK**.















    ![integrate g suite 791241](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-37d8c60e5d66c27de465b0d8474d30e9189600ee%252Fintegrate_g_suite_791241.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=6f40c33754b1c7e565f7bc06b7f454cf&sv=3)

10. Turn the application to on. Select either **ON** for everyone or **ON for some organizations**.















    ![integrate g suite 791242](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-7d65c05f35dcdb5e43606854e30a8493bb5820c8%252Fintegrate_g_suite_791242.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=3e55f0564762b06cf997a821e870866d&sv=3)


## Setting up Prisma Cloud[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/saml-google-g-suite\#setting-up-prisma-cloud)

Set up Prisma Cloud for G Suite integration.

1. Log into Console, then go to **Manage > Authentication > Identity Providers > SAML**.

2. Set **Integrate SAML users and groups with Prisma Cloud** to **Enabled**.

3. Set **Identity provider** to **G Suite**.

4. Set up the following parameters:









1. Paste the SSO URL, Entity ID, and certificate that you copied during the G Suite set up into the **Identity Provider single sign-on URL**, **Identity provider issuer**, and **X.509 certificate** fields.

2. Set **Audience** to match the application Entity ID configured in G Suite. Enter **twistlock**.

3. Click **Save**.


5. Go to **Manage > Authentication > Users**, and click **Add user**.

6. In the **Username** field, enter the G Suite email address the user you want to add. Type a description for the user (optional), select a role, and then click **Save**. Be sure **Create user in local Prisma Cloud account database** is **Off**.

7. Log out of Console.















![logout](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-09795e2c020ef92cf57e8c75062bed42dae64550%252Flogout.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=9fa33172cd6166d0c45b0e599dc97981&sv=3)











You will be redirected into G Suite and you might need to enter your credentials. After that, you will be redirected back into Prisma Cloud and authenticated as a user.


[PreviousOkta (SAML 2.0)](https://docs.prismacloud.io/admin-guide/authentication/saml) [NextAzure Active Directory (SAML 2.0)](https://docs.prismacloud.io/admin-guide/authentication/saml-azure-active-directory)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject

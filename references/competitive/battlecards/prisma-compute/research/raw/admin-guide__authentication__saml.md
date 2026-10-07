For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/authentication/saml.md).

Many organizations use SAML to authenticate users for web services. Prisma Cloud supports the SAML 2.0 federation protocol to access the Prisma Cloud Console. When SAML support is enabled, administrators can log into Console with their federated credentials. This article provides detailed steps for federating your Prisma Cloud Console with Okta.

The Prisma Cloud/Okta SAML federation flow works as follows:

1. Users browse to Prisma Cloud Console.

2. Their browsers are redirected to the Okta SAML 2.0 endpoint.

3. They enter their credentials to authenticate. Multi-factor authentication can be enforced at this step.

4. A SAML token is returned to Prisma Cloud Console.

5. Prisma Cloud Console validates the SAML token’s signature and associates the user to their Prisma Cloud account via user identity mapping or group membership.


Integrating Prisma Cloud with SAML consists of setting up your IdP, then configuring Prisma Cloud to integrate with it.

## Setting up Prisma Cloud in Okta[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/saml\#setting-up-prisma-cloud-in-okta)

Set up Prisma Cloud in Okta.

01. Log into the Okta admin dashboard.

02. On the right, click **Add Applications**.















    ![integrate saml 610130](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-2a57f672dec3911d8e53ff1d82f93858b27c9eea%252Fintegrate_saml_610130.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=1766a70b907f4776d122de30b6e59acf&sv=3)

03. On the left, click **Create new app**.















    ![integrate saml 610131](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-e0df6baf541ee4379fc3106b2ab30cec626358ca%252Fintegrate_saml_610131.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=fb9f2239028473adcea244caa3bd5b21&sv=3)

04. Select **SAML 2.0**, and then click **Create**.















    ![integrate saml 610135](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-02bcee44020bc84ee23bbb6e9e0d98abf55aebf2%252Fintegrate_saml_610135.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=4ecd5cbed14ce296795fa732356ece71&sv=3)

05. In the **App name** field, enter **Prisma Cloud Console**, then click **Next**.















    ![integrate saml 610136](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-f4a76553ecb4ec7b092fb47343ccde245a22f34f%252Fintegrate_saml_610136.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=a0f923f25cfbcc4345e7cb11435225d2&sv=3)

06. In the SAML Settings dialog:









    1. In the **Single Sign On URL** field, enter **https://<CONSOLE\_ADDR>:8083/api/v1/authenticate**.











       Note that if you have changed the default port you use for the HTTPS listener, you’d need to adjust the URL here accordingly. Additionally, this URL must be visible from the Okta environment, so if you’re in a virtual network or behind a load balancer, it must be configured to forward traffic to this port and it’s address is what should be used here.

    2. Select **Use this for Recipient URL and Destination URL**.

    3. In the field for **Audience Restriction**, enter **twistlock** (all lowercase).

    4. Expand **Advanced Settings**.

    5. Verify that **Response** is set to **Signed**.

    6. Verify that **Assertion Signature** is set to **Signed**.















       ![integrate saml 610140](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-7d011232777755622df5c400ab3a6d2f5b7e0719%252Fintegrate_saml_610140.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=4107474e3c6cf2579dea461617d10231&sv=3)


07. (Optional) Add a group.











    Setting up groups is optional. If you set up group attribute statements, then permission to access Prisma Cloud is assessed at the group level. If you don’t set up group attribute statements, them permission to access Prisma Cloud is assessed at the user level.









    1. Scroll down to the **GROUP ATTRIBUTE STATEMENTS** section.

    2. In the **Name** field, enter **groups**.

    3. In filter drop down menu, select **Regex** and enter a regular expression that captures all the groups defined in Okta that you want to use for access control rules in Prisma Cloud.











       In this example, the regular expression **.\*(t\|T)wistlock.\*** is used to include all groups prepended with either Prisma Cloud or twistlock. You should enter your own desired group name here. If you have just one group, such as YourGroup, then just enter **YourGroup**. Regular expressions are not required. If you have multiple groups, you can use a regular expressions, such as **(group1\|group2\|group3)**.















       ![integrate saml 610146](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-44288bd93db4733f26e1908279107e46ec4d6a84%252Fintegrate_saml_610146.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=da4794dedd2be086987db1be983b5d47&sv=3)


08. Click **Next**, and then click **Finish**.











    You are directed to a summary page for your new app.















    ![integrate saml 610150](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-c94254708ce045868045ce3d030389ccc744ad63%252Fintegrate_saml_610150.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=97faf296bb3b8b64fe198eb41875f623&sv=3)

09. Click on the **People** tab, and add users to the Prisma Cloud app.















    ![integrate saml 610156](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-0ba4c53bc741bf15112ada8755cab141ff9a6d3d%252Fintegrate_saml_610156.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=e4c727970df96e0a9ced4649d9e29ab1&sv=3)

10. Click on the **Groups** tab, and add groups to the Prisma Cloud app.















    ![integrate saml 610160](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-04b265161361e0adbe7ba15edbe3664967fab1dc%252Fintegrate_saml_610160.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=510ddcb0171d7921cbf1fadd89bd7a92&sv=3)

11. Click on the **Sign On** tab and click **View setup instructions**.











    The following values are used to configure Prisma Cloud Console, so copy them and set them aside.









    - Identity Provider Single Sign-On URL

    - Identity Provider Issuer

    - X.509 Certificate















      ![integrate saml 610163](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-b2f6c5762de893e295ed49464a39df1e1c5741fd%252Fintegrate_saml_610163.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=6b7923e0c7169cab87895273442df13c&sv=3)


## Configuring Console[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/saml\#configuring-console)

Configure Prisma Cloud Console.

1. Open Console, and login as admin.

2. Go to **Manage > Authentication > Identity Providers > SAML**.

3. Set **Integrate SAML users and groups with Prisma Cloud** to **Enabled**.

4. Set **Identity provider** to **Okta**.

5. Copy the following values from Okta and paste them into their corresponding fields in Console:









   - Identity Provider Single Sign-On URL

   - Identity Provider Issuer

   - X.509 Certificate


6. In **Audience**, enter **twistlock**.

7. Click **Save**.


## Granting access by group[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/saml\#granting-access-by-group)

Grant access to Prisma Cloud Console by group. Each group must be assigned a [role](https://docs.prismacloud.io/admin-guide/authentication/user-roles).

1. Open Console.

2. Define a SAML group.









1. Go to **Manage > Authentication > Groups**.

2. Click **Add group**.

3. In the **Name** field, enter a group name.











      The group name must exactly match the group name in the SAML IdP. Console does not verify if that the value entered matches a group name in the SAML IdP.

4. Select the **SAML group** checkbox.

5. Select a role.

6. Select a project(s) - Optional.

7. Click **Save**.


## Granting access by user[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/saml\#granting-access-by-user)

Grant access to Prisma Cloud Console by user. Each user must be assigned a [role](https://docs.prismacloud.io/admin-guide/authentication/user-roles).

1. Open Console.

2. Define a SAML user.









1. Go to **Manage > Authentication > Users**.

2. Click **Add user**.

3. In the **Username** field, enter a user name.











      The username must exactly match the username in the SAML IdP. Console does not verify if that the value entered matches a user name in the SAML IdP.

4. In the **Description** field, enter additional details about the user (optional).

5. Select **SAML** as the Auth method

6. Select a role.

7. (Optional) Select a project(s).

8. Click **Save**.


[PreviousOpenID Connect](https://docs.prismacloud.io/admin-guide/authentication/oidc) [NextGoogle G Suite (SAML 2.0)](https://docs.prismacloud.io/admin-guide/authentication/saml-google-g-suite)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject

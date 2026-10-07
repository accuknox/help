For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/authentication/saml-azure-active-directory.md).

Many organizations use SAML to authenticate users for web services. Prisma Cloud supports the SAML 2.0 federation protocol to access the Prisma Cloud Console. When SAML authentication is enabled, users can log into the Console with their federated credentials. This article provides detailed steps for federating your Prisma Cloud Console with your Azure Active Directory (AAD) tenant’s Identity Provider.

The Prisma Cloud/Azure Active Directory SAML federation workflow is as follows:

1. User browses to their Prisma Cloud Console.

2. The user’s browser is redirected to the Azure Active Directory SAML 2.0 endpoint.

3. The user enters their AAD credentials to authenticate. Multi-factor authentication can be enforced at this step.

4. An AAD SAML token is returned to the user’s Prisma Cloud Console.

5. Prisma Cloud Console validates the Azure Active Directory SAML token’s signature and associates the user to their Prisma Cloud account via user identity mapping or group membership. Prisma Cloud supports SAML groups for Azure Active Directory federation.


The Azure Portal may change the Enterprise Application SAML federation workflow over time. The concepts and steps outlined in this document can be applied to any Non-gallery application.

The Prisma Cloud Console is integrated with Azure Active Directory as a federated SAML Enterprise Application. The steps to set up the integration are:

- [Configure Azure Active Directory](https://docs.prismacloud.io/admin-guide/authentication/saml-azure-active-directory#_configure_azure_active_directory)









  - [Prisma Cloud User to AAD User identity mapping](https://docs.prismacloud.io/admin-guide/authentication/saml-azure-active-directory#_prisma_cloud_user_to_aad_user_identity_mapping)

  - [Prisma Cloud Groups to AAD Group mapping](https://docs.prismacloud.io/admin-guide/authentication/saml-azure-active-directory#_prisma_cloud_groups_to_aad_group_mapping)









    - [Add permissions to allow Prisma Cloud Console to query the Azure Active Directory API](https://docs.prismacloud.io/admin-guide/authentication/saml-azure-active-directory#_add_permissions_to_allow_prisma_cloud_console_to_query_the_azure_active_directory_api)


- [Configure Prisma Cloud Console](https://docs.prismacloud.io/admin-guide/authentication/saml-azure-active-directory#_configure_prisma_cloud_console)









  - [Prisma Cloud User to AAD User identity association](https://docs.prismacloud.io/admin-guide/authentication/saml-azure-active-directory#_prisma_cloud_user_to_aad_user_identity_association)

  - [Group mapping without calling Azure Active Directory API](https://docs.prismacloud.io/admin-guide/authentication/saml-azure-active-directory#_group_mapping_without_calling_azure_active_directory_api)

  - [Group mapping with calling Azure Active Directory API](https://docs.prismacloud.io/admin-guide/authentication/saml-azure-active-directory#_group_mapping_with_calling_azure_active_directory_api)


## Configure Azure Active Directory[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/saml-azure-active-directory\#configure-azure-active-directory)

**Prerequisites:**

- Required Azure Active Directory SKU: Premium

- Required Azure Active Directory role: Global Administrator


01. Log onto your Azure Active Directory tenant ([https://portal.azure.com](https://portal.azure.com/))

02. Go to _Azure Active Directory > Enterprise Applications_

03. On the top left of the window pane, click **\+ New Application**

04. Select **\+ Create your own application** on the top left of the window pane

05. In the _Name_ field enter **Compute-Console**, select the _Integrate any other application you don’t find in the gallery (Non-gallery)_ radio button and then click **Create**. In this example I am using "Compute-Console" as the application’s identifier.















    ![aad saml 20210728 1](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-8520f51110981769a0533cd8d76b3cf4fab096a3%252Faad_saml_20210728_1.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=e0489302e82ef93d9bd8b363282b50f8&sv=3)

06. The _Compute-Console_ overview page will appear, select **2\. Single sign-on** and then choose **SAML**















    ![aad saml 20210728 2](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-6dcef5eba9543c9f2d192223d11c418469ae0c2e%252Faad_saml_20210728_2.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=62ab34b6efa23beb0d8c3e601fc7dd4f&sv=3)

07. Section #1 _Basic SAML Configuration_:









    1. _Identifier_: **Compute-Console** Set to your Console’s unique Audience value. You will configure this value within your Prisma Cloud Console at a later step.

    2. _Reply URL_: **https://<FQDN\_of\_your\_Prisma Cloud\_Console>:8083/api/v1/authenticate**















       ![aad saml 20210728 3](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-1b690704d0f8ac0e3187e0845596cea0de377614%252Faad_saml_20210728_3.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=a2cfcb19be83fd08bd669d3dbea91062&sv=3)


08. Section #2 _User Attributes & Claims_:











    Select the Azure AD user attribute that will be used as the user account name within Prisma Cloud. This will be the NameID claim within the SAML response token. We recommend using the default value.









    1. _Unique User Identifier (Name ID)_: **user.userprincipalname \[nameid-format:emailAddress\]**















       ![aad saml 20210728 4](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-b873dc8fab0bc80506fc7b2a0e3b2fbf6ccf5507%252Faad_saml_20210728_4.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=ed59a70b5a07ba7de23a2779cf71c8a3&sv=3)











       Even if you are using AAD Groups to assign access to Prisma Cloud set the NamedID claim.


09. Section #3 _SAML Signing Certificate_:









    1. Select **Download: Certificate (Base64)**

    2. Select the edit icon

    3. Set _Signing Option_: **Sign SAML Response and Asertion**















       ![aad saml 20210728 5](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-6308e12196e82d19e4407e34f54474dedabd9c06%252Faad_saml_20210728_5.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=bfb2ff9ead52c729f2c8f291dea2fb25&sv=3)


10. Section #4 _Set up Compute-Console_:











    Save the value of of _Login URL_ and _Azure AD Identifier_. You will use these values for the configuration of the Prisma Cloud Console in a later step.















    ![aad saml 20210728 6](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-2c6510850cde7163cfdd2c8feac967b6c565fd50%252Faad_saml_20210728_6.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=873dd7df666a63d64a601a3ed2c26966&sv=3)

11. Copy the _Application ID_. You can find this within the _Properties_ tab in the Manage section of the application.

12. Click on _1\. Assign users and groups_ within the Manage section of the application. Add the users and/or groups that will have the right to authenticate to Prisma Cloud Console.















    ![aad saml 20210728 7](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-4e8e681259ca931399485bef76f107928cdd6b16%252Faad_saml_20210728_7.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=2687e4be0b905bbb98ca1bb5f54a4247&sv=3)


### Prisma Cloud User to AAD User identity mapping[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/saml-azure-active-directory\#prisma-cloud-user-to-aad-user-identity-mapping)

If you plan to map Azure Active Directory users to Prisma Cloud user accounts go to [Prisma Cloud User to AAD User identity association](https://docs.prismacloud.io/admin-guide/authentication/saml-azure-active-directory#_prisma_cloud_user_to_aad_user_identity_association).

### Prisma Cloud Groups to AAD Group mapping[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/saml-azure-active-directory\#prisma-cloud-groups-to-aad-group-mapping)

When you use Azure Active Directory groups to map to Prisma Cloud SAML groups, do not create users in the Prisma Cloud Console. Configure the AAD SAML application to send group membership ([http://schemas.microsoft.com/ws/2008/06/identity/claims/groups](http://schemas.microsoft.com/ws/2008/06/identity/claims/groups)) claims within the SAML response token. When you enable AAD group authentication the Prisma Cloud user to AAD user identity method of association will be ignored.

Prisma Cloud Compute version 22\_06 now uses the [Microsoft Graph API](https://docs.microsoft.com/en-us/graph/overview)

When the Azure Active Directory SAML response returns a group claim it contains the user’s group OIDs as the values. When adding AAD groups within the Console using the group’s name the Console will perform a call to the Microsoft Graph API endpoint ([https://graph.microsoft.com](https://graph.microsoft.com/)) to determine the OID of the group. Therefore you will need to configure the Console to query the Azure Active Directory API. For users whose group membership exceeds 150 groups the Console will have to perform an Microsoft Graph API call to query for the full group membership of the user. In this scenario it is recommended to use [ApplicationGroups](https://docs.microsoft.com/en-us/azure/active-directory/hybrid/how-to-connect-fed-group-claims) to emit only the groups that are explicitly assigned to the application and the user is a member of.

Prisma Cloud Compute version 21\_08 and higher supports the scenerio in which the Console is unable to call the Microsoft Graph API. The AAD group’s OID is supplied as the _OID_ value when configuring the Console’s SAML groups.

1. Configure the application to send group claims within the SAML response token:









1. In Azure go to _Azure Active Directory > Enterprise applications > Compute-Console_

2. Under Manage click _Single sign-on_

3. Click the edit for section **2\. User Attributes & Claims**

4. Click **Add a group claim**

5. Select the **Security groups** radio button

6. Set _Source attribute_ to **Group ID**















      ![aad saml 20210728 10](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-6a4a9836b190df269ad9123027bac7b90eacede3%252Faad_saml_20210728_10.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=28353ba5f8dacc9130f9fe5d71de09e8&sv=3)


2. Assign the group to the application









1. In Azure go to _Azure Active Directory > Enterprise applications > Compute-Console_

2. Under Manage click _Users and groups_

3. Click **\+ Add user/group**

4. Under _Users and groups_ click **None Selected**

5. Select the group to be used for authentication to the Console and click **Select**

6. At the _Add Assignment_ window click **Assign**











      If you plan not to use the Azure Active Directory API call functionality to determine the group’s OID based upon the supplied group name and/or scenarios in which a user’s group membership is greater than 150 groups go to [Group mapping without calling Azure Active Directory API](https://docs.prismacloud.io/admin-guide/authentication/saml-azure-active-directory#_group_mapping_without_calling_azure_active_directory_api). Otherwise, continue with the following steps.


#### Add permissions to allow Prisma Cloud Console to query the Azure Active Directory API[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/saml-azure-active-directory\#add-permissions-to-allow-prisma-cloud-console-to-query-the-azure-active-directory-api)

Add these permissions to allow Prisma Cloud Console to query the Azure Active Directory API. These permissions are required in the following scenarios.

- Your Azure Active Directory (AAD) has users that belong to more than 150 groups.

- You add groups in the Prisma Cloud Console without their Object ID (OID).


1. Set Application permissions:









1. In Azure go to _Azure Active Directory > App registrations > Compute-Console_

2. Under the _Manage_ section, go to _API Permissions_

3. Click on **Add a Permission**

4. Click on **Microsoft Graph**

5. _Select permissions_: **Application Permissions: Directory.Read.All**















      ![aad saml 20210728 12](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-534e37979f6404353fab69de03a6cfb308074988%252Faad_saml_20210728_12.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=adc1aa721d9b93cc067868b5c7eb36cf&sv=3)

6. Click _Add Permissions_

7. Click _Grant admin consent for Default Directory_ within the Configured permissions blade


2. Create Application Secret









1. Under the Manage section, go to _Certificates & secrets_

2. Click on **New client secret**

3. Add a _secret description_

4. _Expires_: **Never**

5. Click _Add_

6. Make sure to save the secret _value_ that is generated before closing the blade















      ![aad saml 20210728 13](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-cebef6be4efce01b711246aaecc2d35712b1fbdc%252Faad_saml_20210728_13.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=7e98eb5fd7977b1d83df80f127c0f831&sv=3)











      Allow several minutes for these permissions to propagate within AAD.











      Continue the configuration by going to [Group mapping with calling Azure Active Directory API](https://docs.prismacloud.io/admin-guide/authentication/saml-azure-active-directory#_group_mapping_with_calling_azure_active_directory_api)


## Configure Prisma Cloud Console[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/saml-azure-active-directory\#configure-prisma-cloud-console)

Configure Prisma Cloud Compute Console.

### Prisma Cloud User to AAD User identity association[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/saml-azure-active-directory\#prisma-cloud-user-to-aad-user-identity-association)

Configure Prisma Cloud Console’s SAML settings for user identity based logon.

1. Log into Prisma Cloud Console as an administrator

2. Go to **Manage > Authentication > Identity Providers > SAML**

3. Set **SAML settings** to **Enabled**

4. Set **Identity Provider** to **Azure**









1. In **Provider alias** enter an identifier for this SAML provider (e.g. AzureAD)

2. In **Identity provider single sign-on URL** enter the Azure AD provided **Login URL**

3. In **Identity provider issuer** enter the Azure AD provided **Azure AD Identifier**

4. In **Audience** enter **Compute-Console**

5. In **X.509 certificate** paste the Azure AD SAML **Signing Certificate Base64** into this field















      ![aad saml 20210728 8](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-1e040ac99421b82430b5fd6650ce8b425345b5ca%252Faad_saml_20210728_8.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=8756dff7b3f27e016b9d15a7949eb907&sv=3)


5. Click **Save**


#### Map an Azure Active Directory user to a Prisma Cloud account[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/saml-azure-active-directory\#map-an-azure-active-directory-user-to-a-prisma-cloud-account)

Map an Azure Active Directory user to a Prisma Cloud account.

1. Go to **Manage > Authentication > Users**

2. Click **Add user**

3. **Create a New User**









1. **Username**: Azure Active Directory _userprincipalname_

2. **Description**: Enter additional details about the user (optional)

3. **Auth Method**: Select **SAML**

4. **Role**: Select the appropriate role for the user















      ![aad saml 20210728 9](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-e95bcac7688f5b100399b7756e89569844aa5643%252Faad_saml_20210728_9.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=fb785ba552e9e27cc1cdd435ebd20af4&sv=3)

5. Click **Save**


### Group mapping without calling Azure Active Directory API[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/saml-azure-active-directory\#group-mapping-without-calling-azure-active-directory-api)

In this configuration the Console will not call the Microsoft Graph API to determine the group’s AAD OID based upon the group name supplied. If a user’s security group membership is greater than 150 groups and the Console is unable to perform the Microsoft Graph API query it is recommended to to use [ApplicationGroups.](https://docs.microsoft.com/en-us/azure/active-directory/hybrid/how-to-connect-fed-group-claims)

Configure Prisma Cloud Console’s SAML settings for group based logon.

1. Log into Prisma Cloud Console as an administrator

2. Go to **Manage > Authentication > Identity Providers > SAML**

3. Set **SAML settings** to **Enabled**

4. Set **Identity Provider** to **Azure**









1. In **Provider alias** enter an identifier for this SAML provider (e.g. AzureAD)

2. In **Identity provider single sign-on URL** enter the Azure AD provided **Login URL**

3. In **Identity provider issuer** enter the Azure AD provided **Azure AD Identifier**

4. In **Audience** enter **Compute-Console**

5. In **X.509 certificate** paste the Azure AD SAML **Signing Certificate Base64** into this field















      ![aad saml 20210728 8](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-1e040ac99421b82430b5fd6650ce8b425345b5ca%252Faad_saml_20210728_8.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=8756dff7b3f27e016b9d15a7949eb907&sv=3)


5. Click **Save**


#### Assign the AAD group OID to a role[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/saml-azure-active-directory\#assign-the-aad-group-oid-to-a-role)

Assign the AAD group OID to a role.

1. Go to **Manage > Authentication > Groups**

2. Click **Add Group**

3. Enter a display name for the group (e.g. AAD\_SAML\_admins)

4. Select _Authentication method_ **External providers**

5. Select _Authentication Providers_ **SAML**

6. Enter the AAD OID of the group within the _OID_ field

7. Select the Prisma Cloud role for the group

8. Click **Save**















![aad saml 20210728 11](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-d5bf42cb7210c87885aa999538c5812ead214f3a%252Faad_saml_20210728_11.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=0b10b36d561ecf7965b615b3c3394b51&sv=3)


### Group mapping with calling Azure Active Directory API[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/saml-azure-active-directory\#group-mapping-with-calling-azure-active-directory-api)

Azure Active Directory SAML response will send the user’s group membership as OIDs and not the name of the group. When a group name is added, Prisma Cloud Console will query the Microsoft Graph API to determine the OID of the group entered. For users whose group membership exceeds 150 groups the Console will perform an Microsoft Graph API call to query for the full group membership of the user. Ensure your Prisma Cloud Console is able to reach the Microsoft Graph API endpoint ([https://graph.microsoft.com](https://graph.microsoft.com/)).

1. Log into Prisma Cloud Console as an administrator

2. Go to **Manage > Authentication > Identity Providers > SAML**

3. Set **SAML settings** to **Enabled**

4. Set **Identity Provider** to **Azure**









1. In **Provider alias** enter an identifier for this SAML provider (e.g. AzureAD)

2. In **Identity provider single sign-on URL** enter the Azure AD provided **Login URL**

3. In **Identity provider issuer** enter the Azure AD provided **Azure AD Identifier**

4. In **Audience** enter **Compute-Console**

5. Enter the **Application ID** of the _Compute-Console_ AAD application

6. Enter the **Tenant ID** of your Azure Active Directory

7. Enter the **Application Secret value** for permission to Azure Active Directory API

8. In **X.509 certificate** paste the Azure AD SAML **Signing Certificate Base64** into this field


5. Click **Save**















![aad saml 20210728 14](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-b0251a7022eb48698f298c796574ea1d11b91607%252Faad_saml_20210728_14.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=6455e9e1e82efd4ecfaa84df715c01f5&sv=3)


#### Assign the AAD group name to a role[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/saml-azure-active-directory\#assign-the-aad-group-name-to-a-role)

Assign the AAD group name to a role.

1. Go to **Manage > Authentication > Groups**

2. Click **Add Group**

3. Enter the name of the AAD group

4. Click the **SAML group** radio button

5. Select the Prisma Cloud role for the group

6. Click **Save**















![aad saml 20210728 15](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-f32a2ebb096dc7bf511867001527b39514c22841%252Faad_saml_20210728_15.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=3c5f1e0701ff6f62cd85410bc776c67f&sv=3)











Test logging into Prisma Cloud Console via Azure Active Directory SAML federation. Leave your existing session logged into Prisma Cloud Console in case you encounter issues. Open a new incognito browser window and go to **https://<CONSOLE>:8083** and select SAML authentication method.


[PreviousGoogle G Suite (SAML 2.0)](https://docs.prismacloud.io/admin-guide/authentication/saml-google-g-suite) [NextPingFederate (SAML 2.0)](https://docs.prismacloud.io/admin-guide/authentication/saml-ping-federate)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject

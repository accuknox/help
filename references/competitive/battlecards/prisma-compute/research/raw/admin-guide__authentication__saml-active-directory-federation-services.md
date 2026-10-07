For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/authentication/saml-active-directory-federation-services.md).

Many organizations use SAML to authenticate users for web services. Prisma Cloud supports the SAML 2.0 federation protocol for access to the Prisma Cloud Console. When SAML support is enabled, users can log into Console with their federated credentials. This article provides detailed steps for federating your Prisma Cloud Console with your Active Directory Federation Service (ADFS) Identity Provider (IdP).

Prisma Cloud supports SAML 2.0 federation with Windows Server 2016 and Windows Server 2012r2 Active Directory Federation Services via the SAML protocol. The federation flow works as follows:

1. Users browse to Prisma Cloud Console.

2. Their browsers are redirected to the ADFS SAML 2.0 endpoint.

3. Users authenticate either with Windows Integrated Authentication or Forms Based Authentication. Multi-factor authentication can be enforced at this step.

4. An ADFS SAML token is returned to Prisma Cloud Console.

5. Prisma Cloud Console validates the SAML token’s signature and associates the user to their Prisma Cloud account via user identity mapping or group membership.


Prisma Cloud Console is integrated with ADFS as a federated SAML Relying Party Trust.

- [Configure Active Directory Federation Services](https://docs.prismacloud.io/admin-guide/authentication/saml-active-directory-federation-services#_configure_active_directory_federation_services)

- [Configure the Prisma Cloud Console](https://docs.prismacloud.io/admin-guide/authentication/saml-active-directory-federation-services#_configure_the_prisma_cloud_console)


The Relying Party trust workflows may differ slightly between Windows Server 2016 and Windows Server 2012r2 ADFS, but the concepts are the same.

## Configure Active Directory Federation Services[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/saml-active-directory-federation-services\#configure-active-directory-federation-services)

This guide assumes you have already deployed Active Directory Federation Services, and Active Directory is the claims provider for the service.

1. Log onto your Active Directory Federation Services server.

2. Go to **Server Manager > Tools > AD FS Management** to start the ADFS snap-in.

3. Go to **AD FS > Service > Certificates** and click on the **Primary Token-signing** certificate.

4. Select the Details tab, and click **Copy to File…​**.















![adfs saml 1](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-b360ba03d3e6256fc62447fb2912813c09701a62%252Fadfs_saml_1.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=12d2dcea43abef4e202c5870d6afa69d&sv=3)

5. Save the certificate as a Base-64 encoded X.509 (.CER) file. You will upload this certificate into the Prisma Cloud console in a later step.

6. Go to **AD FS > Relying Party Trusts**.

7. Click **Add Relying Party Trust** from the **Actions** menu.









01. Step Welcome: select **Claims aware**.















       ![adfs saml 2](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-91f11dbd174c17faa95e20a169df9f7de99e8158%252Fadfs_saml_2.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=dad75d3ad7af2cf3c4a2b49231723381&sv=3)

02. Step Select Data Source: select **Enter data about the relying party manually**.















       ![adfs saml 3](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-a568d03ec6ff87bb9b6a9d6d7ed01c6c0df2d290%252Fadfs_saml_3.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=ccd9e3935a85f8299516466ec3fe721f&sv=3)

03. Step Specify Display Name: In **Display Name**, enter **twistlock Console**.















       ![adfs saml 4](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-756e7e968483fa62017485f3afce0fa572a643c9%252Fadfs_saml_4.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=3f36be88962e39f528a1321ceca464a8&sv=3)

04. Step Configure Certificate: leave blank.

05. Step Configure URL: select **Enable support for the SAML 2.0 WebSSO protocol**. Enter the URL for your Prisma Cloud Console **https://<FQDN\_TWISTLOCK\_CONSOLE>:8083/api/v1/authenticate/**.















       ![adfs saml 5](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-3b7b09f894a91f67b4e8335aca70a3f8d2d00e8a%252Fadfs_saml_5.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=ca6acb598ad0fb9eadd50ee1a69a2ec8&sv=3)

06. Step Configure Identifiers: for example enter **twistlock** all lower case and click **Add**.















       ![adfs saml 6](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-6fac08e1cf37de89347293d1edfff63ccedb8a38%252Fadfs_saml_6.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=1b226af05506f8529ecc0a66e52e7fbe&sv=3)

07. Step Choose Access Control Policy: this is where you can enforce multi-factor authentication for Prisma Cloud Console access. For this example, select **Permit everyone**.















       ![adfs saml 7](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-fd1b24a68857da476848a22b8ae6a503cb4df773%252Fadfs_saml_7.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=077c49f076f376e2a826b4884085b999&sv=3)

08. Step Ready to Add Trust: no changes, click **Next**.

09. Step Finish: select **Configure claims issuance policy for this application** then click **Close**.















       ![adfs saml 8](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-9bbc536a6bea8f28959aa4cbd25a26b5034f3699%252Fadfs_saml_8.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=fe7a36cd9b5cee94b2487b5f1a68a40d&sv=3)

10. In the Edit Claim Issuance Policy for Prisma Cloud Console click **Add Rule**.

11. Step Choose Rule Type: In **Claim rule template**, select **Send LDAP Attributes as Claims**.















       ![adfs saml 9](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-221821aec02e773d5be80b9e078d8e61549e813c%252Fadfs_saml_9.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=5a9234794ec5d00116afebfabe0cdbc3&sv=3)

12. Step Configure Claim Rule:









       - Set **Claim rule name** to **Prisma Cloud Console**

       - Set **Attribute Store** to **Active Directory**

       - In **Mapping of LDAP attributes to outgoing claim types**, set the **LDAP Attribute** to **SAM-Account-Name** and **Outgoing claim type** to **Name ID**.















         ![adfs saml 10](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-1604f8c25cfcc22a9673c4606539a4b676d2baf2%252Fadfs_saml_10.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=1478e63f57a872b6686dd948ea16da8d&sv=3)











         The user’s Active Directory attribute returned in the claim must match the Prisma Cloud user’s name. In this example we are using the samAccountName attribute.


13. Click **Finish**.


8. Configure ADFS to either sign the SAML response ( _-SamlResponseSignature MessageOnly_) or the SAML response and assertion ( _-SamlResponseSignature MessageAndAssertion_) for the Prisma Cloud Console relying party trust. For example to configure the ADFS to only sign the response, start an administrative PowerShell session and run the following command:

















AskCopy



```
set-adfsrelyingpartytrust -TargetName "Prisma Cloud Console" -SamlResponseSignature MessageOnly
```


## Active Directory group membership within SAML response[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/saml-active-directory-federation-services\#active-directory-group-membership-within-saml-response)

You can use Active Directory group membership to assign users to Prisma Cloud roles. When a user’s group membership is sent in the SAML response, Prisma Cloud attempts to associate the user’s group to a Prisma Cloud role. If there is no group association, Prisma Cloud matches the user to an identity based on the NameID to Prisma Cloud username mapping. The SAML group to Prisma Cloud role association _does not require_ the creation of a Prisma Cloud user. Therefore simplify the identity management required for your implementation of Prisma Cloud.

1. In **Relying Party Trusts**, select the **Prisma Cloud Console** trust.

2. Click **Edit Claim Issuance Policy** in the right hand **Actions** pane.

3. Click **Add Rule**.

4. _Claim rule template:_ **Send Claims Using a Custom Rule**.

5. Click **Next**.

6. _Claim rule name:_ **Prisma Cloud Groups**.

7. Paste the following claim rule into the _Custom rule_ field:

















AskCopy



```
c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname", Issuer == "AD AUTHORITY"] => issue(store = "Active Directory", types = ("groups"), query = ";tokenGroups;{0}", param = c.Value);
```


## Configure the Prisma Cloud Console[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/saml-active-directory-federation-services\#configure-the-prisma-cloud-console)

Configure the Prisma Cloud Console.

01. Login to the Prisma Cloud Console as an administrator.

02. Go to **Manage > Authentication > Identity Providers**.

03. CLick **\+ Add Provider**

04. Set **Protocol** to **Saml**.

05. Set **Identity Provider** to **ADFS**.

06. Enable **Automatically detect authentication method** if the authenticating users' workstations can perform integrated windows authentication with ADFS / Active Directory

07. Enter **Provider alias** name to render to the user when initiating the SAML workflow from the Console.

08. In **Identity provider single sign-on URL**, enter your SAML Single Sign-On Service URL. For example **https://FQDN\_of\_your\_adfs/adfs/ls**.

09. In **Identity provider issuer**, enter your SAML Entity ID, which can be retrieved from **ADFS > Service > Federation Service Properties : Federation Service Identifier**.

10. In **Audience**, enter the ADFS Relying Party identifier **twistlock**

11. In **X.509 certificate**, paste the ADFS **Token Signing Certificate Base64** into this field.















    ![adfs saml 11](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-ab00a069f5afbbf152b3c41cc66069ef5213853e%252Fadfs_saml_11.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=7c55f922496584de8d2ffa4a5763f4f7&sv=3)

12. Click **Save**.

13. Go to **Manage > Authentication > Users**.

14. Click **Add user**.









    1. **Username**: Active Directory _samAccountName_ must match the value returned in SAML token’s Name ID attribute.











       When federating with ADFS Prisma Cloud usernames are case insensitive. All other federation IdPs are case sensitive.

    2. **Description**: Enter a description for the user (optional).

    3. **Auth method**: set to **SAML**.















       ![adfs saml 12](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-3e214aa01568fb33abc50da48173e1b0a94e70df%252Fadfs_saml_12.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=11734be22b21ac9502f298e7d83f81f1&sv=3)

    4. **Role**: select an appropriate [role](https://docs.prismacloud.io/admin-guide/authentication/user-roles).


15. Click **Save**.


### Active Directory group membership mapping to Prisma Cloud role[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/saml-active-directory-federation-services\#active-directory-group-membership-mapping-to-prisma-cloud-role)

Associate a user’s Active Directory group membership to a Prisma Cloud role.

1. Go to **Manage > Authentication > Groups**.

2. Click **Add group**.

3. _Group Name_ matches the **Active Directory group name**.

4. Select the **SAML group** radio button.

5. Assign the **Role**.















![adfs saml 13](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-3973cf4e82d6ad0dcb75ac2d2d3ee8a12c649843%252Fadfs_saml_13.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=ac203c4701839b5f2497ab98c2eef806&sv=3)











The SAML group to Prisma Cloud role association _does not require_ the creation of a Prisma Cloud user.

6. Test login into the Prisma Cloud Console via ADFS SAML federation.











Leave your existing session logged onto the Prisma Cloud Console in case you encounter issues. Open a new incognito browser window and go to https://<CONSOLE>:8083.


[PreviousPingFederate (SAML 2.0)](https://docs.prismacloud.io/admin-guide/authentication/saml-ping-federate) [NextGitHub (OAuth 2.0)](https://docs.prismacloud.io/admin-guide/authentication/oauth2-github)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject

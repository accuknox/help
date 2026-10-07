For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/configure/authenticate-console-with-certs.md).

Prisma Cloud supports certificate-based authentication in addition to username/password based authentication for the Console UI and the API.

This is especially useful for those in government and financial services, who use multi-factor authentication technologies built on x.509 certificates. This is applicable to users authenticating through Active Directory accounts as well. This feature allows customers to control the trusted CAs for signing certificates for authentication.

## Setting up your Certificates[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/authenticate-console-with-certs\#setting-up-your-certificates)

Set up Prisma Cloud for certificate-based authentication.

If you are using certificates to authenticate against Active Directory accounts, Prisma Cloud uses the UserPrincipalName field in the SAN to match the certificate to the user in Active Directory. This is the same process used by Windows clients for authentication, so for most customers, the existing smart card certificates you are already using can also be used for authentication to Prisma Cloud.

1. Save the CA certificate(s) used to sign the certificates that you will use for authentication to Prisma Cloud.











The certificate has to be in PEM format. If you have multiple CA certificates that issue certificates to your users, concatenate their PEM files together. For example, if you have Issuing CA 1 and Issuing CA 2, create a combined PEM file like this:

















AskCopy



```
$ cat issuing-ca-1.pem issuing-ca-2.pem > issuing-cas.pem
```

2. Log into Console, and go to **Manage > Authentication > System Certificates**.

3. Under **Certificate-based authentication to Console**, upload your CA certificate(s) in PEM format.

4. Select **Save**.

5. Open Console login page in your browser. When prompted select your user certificate.















![cert auth to console 765460](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-8c30934abfba339deac5c1bd9f2d3dcfd40a3601%252Fcert_auth_to_console_765460.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=02110f3b07d02d0f280fb0a39ae8f64d&sv=3)


## What’s Next[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/authenticate-console-with-certs\#whats-next)

See [Assigning roles](https://docs.prismacloud.io/admin-guide/authentication/assign-roles) to learn how to add users and assign roles to them.

[PreviousSet different paths for Console and Defender (with daemon sets)](https://docs.prismacloud.io/admin-guide/configure/set-diff-paths-daemon-sets) [NextConfigure custom certs from a predefined directory](https://docs.prismacloud.io/admin-guide/configure/custom-certs-predefined-dir)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject

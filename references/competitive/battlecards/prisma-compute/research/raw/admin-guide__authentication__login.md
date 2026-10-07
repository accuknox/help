For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/authentication/login.md).

Prisma Cloud Console supports multiple authentication methods. Check with your administrator to see how sign-in has been implemented for your organization, then choose the appropriate method from the drop-down list.

![login](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-932c6dfd10687462457e6aa2b2f58b93a82111f7%252Flogin.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=988bfdfd53b7b90ecb109aa2b38d62d0&sv=3)

The options are:

- **Local/ LDAP** — Users are evaluated against Console’s database before the LDAP database. By default, initial admin users are created in Console’s local database, so choose this option when you’re logging in with your first user. If you integrate with a central identity provider, you can always delete the initial admin user, so that all users authenticate in compliance with your organization’s policy (e.g., 2FA).











If the same username exists in both databases, it’s not possible to login with the LDAP user.

- **SAML** — Security Assertion Markup Language (SAML) is an open standard that enables single sign-on. Prisma Cloud supports all standard SAML 2.0 providers.

- **OAuth** — Prisma Cloud currently supports GitHub and OpenShift for OAuth login. For the OAuth login flow, Prisma Cloud gets permission from the user to query their information (username and email) from GitHub or OpenShift, and then checks the local database to determine if the user is authorized to access Prisma Cloud Console. If so, Prisma Cloud issues a token to the user to access Console.

- **OpenID Connect** — OpenID Connect is a simple identity layer on top of the OAuth 2.0 protocol. Prisma Cloud supports all standard OpenID Connect providers.


## Login flow[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/login\#login-flow)

If you integrate Prisma Cloud with an identity provider (IdP), the user’s identity is verified by the IdP, and the role is mapped in Prisma Cloud Console.

If you don’t want to integrate with an IdP, Prisma Cloud lets you create "local" users and groups, where the Console itself both authenticates and authorizes users.

![login flow](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-ca8d8709aee1469bbc83381f552f961857ad059b%252Flogin_flow.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=aa44cb33078a97a69e06290d852e087b&sv=3)

## Direct login URL[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/login\#direct-login-url)

Direct login URLs are supported for SAML, OAuth and OIDC. When you use the direct login URL, the client doesn’t need the extra step of selecting an auth provider from the Prisma Cloud login page.

Set type in the direct login URL:

AskCopy

```
https://<CONSOLE>:<PORT>/api/v1/authenticate/identity-redirect-url?type=<oauth/oidc/saml>&redirect=true
```

[PreviousAuthentication](https://docs.prismacloud.io/admin-guide/authentication/authentication) [NextIntegrate with an IdP](https://docs.prismacloud.io/admin-guide/authentication/identity-providers)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject

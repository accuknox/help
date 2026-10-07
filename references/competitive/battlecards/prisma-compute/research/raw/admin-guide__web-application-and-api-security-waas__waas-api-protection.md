For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-api-protection.md).

WAAS can enforce API security based on specifications provided in the form of [Swagger](https://swagger.io/) or [OpenAPI](https://www.openapis.org/) files. Alternatively, you can manually define your API (e.g., paths, allowed HTTP methods, parameter names, input types, value ranges, and so on). Once defined, you can configure the actions WAAS applies to requests that do not comply with the API’s expected behavior.

Users should be careful when enabling [Prisma Session Cookies](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-advanced-settings#prisma-session) along with API protection. [Prisma Session Cookies](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-advanced-settings#prisma-session) mandates client’s support of cookies and javascript in order for them to reach the protected application. As APIs are often accessed by "primitive" automation clients, avoid enabling [Prisma Session Cookies](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-advanced-settings#prisma-session) unless you are certain all clients accessing the protected API support BOTH cookies AND Javascript.

## Import API definition from Swagger or OpenAPI files[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-api-protection\#import-api-definition-from-swagger-or-openapi-files)

1. Click the **App definition** tab.















![waas app definition](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-2c094c0dacccba1837e856d927da2e9573cd339b%252Fwaas_app_definition.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=a97caab802d3ead71a78603105403e53&sv=3)

2. Click **Import**.















![waas import api](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-6270dd55797ef47331cf251d8ae1e436b1d57fee%252Fwaas_import_api.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=d7cf0132d9d800e27fa01ef7574dce57&sv=3)

3. Select a file to load.

4. Click the **API protection** tab.















![waas api protection tab](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-49fe9f79dfc48b7abb20a476c885c7233f671700%252Fwaas_api_protection_tab.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=e72cc727efc8ec494b26ee68e4a0d63a&sv=3)

5. Review path and parameter definitions listed under **API Resources**.

6. Click the **Endpoint setup** tab.















![waas endpoint setup tab](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-a1dc99bc218d1b95a053fd1e19c846f5d5d8dfcc%252Fwaas_endpoint_setup_tab.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=b1e5b09029cc9f33e3bfa998faec3016&sv=3)

7. Review protected endpoints listed under **Protected Endpoints** and verify configured base paths all end with a trailing `*`.











Base path in the endpoint definition should always end with a `*` e.g. _"/\*"_, _"/api/v2/\*"_. If not configured that way, API protection will not apply to sub-paths defined in the API protection tab.

8. Go back to the **API protection** tab.















![waas api protection config actions](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-1b2a101444c83da98fe177166ec459c234d40c62%252Fwaas_api_protection_config_actions.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=443226283a8c24f77d716832f6ba35fc&sv=3)

9. Configure an **API protection** [action](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-api-protection#actions) for the resources defined under **API resources**, and an [action](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-api-protection#actions) for all other resources.















![waas api protection action](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-9dbd94dbefa2af339474ae88bb0286d45daf3e53%252Fwaas_api_protection_action.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=093dff33f9054bad1a56ff1457e68f23&sv=3)


## Define an API manually[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-api-protection\#define-an-api-manually)

1. Click the **App definition** tab.















![waas app definition](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-2c094c0dacccba1837e856d927da2e9573cd339b%252Fwaas_app_definition.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=a97caab802d3ead71a78603105403e53&sv=3)

2. Click the **Endpoint setup** tab.















![waas endpoint setup tab](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-a1dc99bc218d1b95a053fd1e19c846f5d5d8dfcc%252Fwaas_endpoint_setup_tab.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=b1e5b09029cc9f33e3bfa998faec3016&sv=3)

3. Add protected endpoints under **Protected endpoints** and verify configured base paths all end with a trailing `*`.











Base path in the endpoint definition should always end with a `*` e.g. _"/\*"_, _"/api/v2/\*"_. If not configured that way, API protection will not apply to sub-paths defined in the API protection tab.

4. Click the **API protection** tab.















![waas api protection tab empty](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-686f7f8ae891fd92eb66af6874cb5bf40e4fe01a%252Fwaas_api_protection_tab_empty.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=44a77efb7389da7d3b729cb05774a0a5&sv=3)

5. Click **Add path**

6. Enter **Resource path** (e.g. _/product_ \- resource paths should not end with a trailing _"/"_).















![waas api protection path methods](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-29c65cfb80755bd3fd5530971d7f03801869ac71%252Fwaas_api_protection_path_methods.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=c70abc276ac8456d8a3c3bae01b3d675&sv=3)











Paths entered in this section are additional subpaths to the base path defined in the previous endpoint section. For example, if in the endpoint definition hostname was set to _"www.example.com"_, base path set to _"/api/v2/\*"_ and in the **API Protection** tab resource path set to _"/product"_ \- full protected resource would be `www.example.com/api/v2/product`.

7. Select allowed methods.















![waas select methods](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-5bc05140970e0f5de63ea6a96b8e3f1c25b1b430%252Fwaas_select_methods.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=48723388e6e4a04c0ce46fa953bcc826&sv=3)

8. For each allowed HTTP method, define parameters by selecting the method from **Parameters for** drop-down list.















![cnaf api protection select method](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-63a9c0b41873803ec97ad6a2b57a0aeea8885c1d%252Fcnaf_api_protection_select_method.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=7e5a90f88d68fec40ea5d15faa9dc212&sv=3)









1. Select an HTTP method from drop-down list.

2. Click **Add parameter**.

3. Enter parameter [definition](http://spec.openapis.org/oas/v3.0.3#parameter-object).















      ![cnaf api add parameter](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-0fe80492af55565331d355d55e50751e7d805e1a%252Fcnaf_api_add_parameter.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=68035961bd0a47bf44d333b08a235fde&sv=3)


9. Configure an **API protection** [action](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-api-protection#actions) for the resources defined under **API resources**, and an [action](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-api-protection#actions) for all other resources.















![waas api protection action](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-9dbd94dbefa2af339474ae88bb0286d45daf3e53%252Fwaas_api_protection_action.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=093dff33f9054bad1a56ff1457e68f23&sv=3)









   - **Parameter violation** — Action to be taken when a request sent to one of the specified paths in the API resource list does not comply with the parameter provided definitions.

   - **Unspecified path(s)/method(s)** — Action to be taken in one of the following cases:









     - Request sent to a resource path that is not specified in the API resources list.

     - Request sent using an unsupported HTTP method for a resource path in the API list.


## API Actions[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-api-protection\#api-actions)

HTTP requests that trigger API protections are subject to one of the following actions:

- **Alert** \- Request is passed to the protected application and an audit is generated for visibility.

- **Prevent** \- Request is denied from reaching the protected application, an audit is generated, and WAAS responds with an HTML banner indicating the request was blocked.

- **Ban** \- Can be applied on either IP addresses or [Prisma Session IDs](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-advanced-settings#prisma-session). All requests originating from the same IP/Prisma Session to the protected application are denied for the configured time period (default is 5 minutes) following the last detected attack.











To enable ban by Prisma Session ID, you must enable [Prisma Session Cookies](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-advanced-settings#prisma-session). For more information on enabling Prisma Sessions and configuring ban definitions, see [Advanced Settings](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-advanced-settings).

- When the X-Forwarded-For HTTP header is included in the request headers, ban will apply based on the first IP listed in the header value (true client IP).

- WAAS implements state, which is required for banning user sessions by IP address. Because Defenders do not share state, any application that is replicated across multiple nodes must enable IP address stickiness on the load balancer.


[PreviousApp firewall](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-app-firewall) [NextDoS protection](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-dos-protection)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject

For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-access-control.md).

WAAS allows for control over how applications and end-users communicate with the protected web application.

![waas access control exception](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-ac7271edbb1ae07460686f361845d7e53bafba3e%252Fwaas-access-control-exception.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=f00d79578116b056ac2d986df79ac2b8&sv=3)

## Network Lists[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-access-control\#network-lists)

**Network Lists** allow administrators to create and maintain named IP address lists e.g. "Office Branches", "Tor and VPN Exit Nodes", "Business Partners", etc. List entries are composed of IPv4 addresses or IP CIDR blocks.

To access **Network Lists**, open Console, go to **Defend > WAAS** and select the **Network List** tab.

![waas network lists](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-95c90c4c6db2a115cbd93a03161910855ef5917f%252Fwaas_network_lists.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=cd748d90eccb66cd4f43b42d4e6fd04f&sv=3)

Lists can be updated manually or via batch importing of entries from a CSV file. Once defined, **Network Lists** can be referenced and used in [IP-based access control](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-access-control#ip-network-controls), [user-defined bots](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-bot-protection#user-defined-bot) and [DoS protection](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-dos-protection).

To export lists in CSV format, click **export CSV**.

- When the X-Forwarded-For HTTP header is included in the request headers, actions will apply based on the first public IP listed in the header value (true client IP). Private IPs in the header value are not used for this purpose.

- IPv6 addresses are currently not supported.


## Network Controls[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-access-control\#network-controls)

![waas access control exception](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-ac7271edbb1ae07460686f361845d7e53bafba3e%252Fwaas-access-control-exception.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=f00d79578116b056ac2d986df79ac2b8&sv=3)

### IP-based access control[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-access-control\#ip-based-access-control)

Network lists can be specified in:

- _**Denied inbound IP Sources**_ \- WAAS applies selected action (Alert or Prevent) for IP addresses in network lists.

- _**IP Exception List**_ \- Traffic originating from IP addresses listed in this category will not be inspected by any of the protections defined in this policy.

- When the X-Forwarded-For HTTP header is included in the request headers, actions will apply based on the first IP listed in the header value (true client IP).

- Practice caution when adding network lists to the IP Exception List because protections will not be applied for traffic originating from these IP addresses.


### Geo access control[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-access-control\#geo-access-control)

With **Geo access control** enabled, you can allow or block the traffic originating from the given Geolocation, and also opt to add an exception to this rule under **Exception > Network Controls**. For example, you can allow/blocklist all IPs from a given location, except for the IPs listed in a network list that you create under **Defend > WAAS > Network lists**. Specifying a network list under **Exceptions > All WAAS Detections** will bypass all the WAAS detections, for example for App definition, App firewall, Dos protection, Bot protection, and Custom rules.

### Country-Based Access Control[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-access-control\#country-based-access-control)

Specify country codes, [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements) format, in one of the following categories (mutually exclusive):

- _**Denied Inbound Source Countries**_ \- WAAS applies selected action (Alert or Prevent) for requests originating from the specified countries.

- _**Allowed Inbound Source Countries**_ \- Requests originating from specified countries will be forwarded to the application (pending inspection). WAAS will apply action of choice (Alert or Prevent) on all other requests not originating from the specified countries.


Country of origin is determined by the IP address associated with the request. When the X-Forwarded-For HTTP header is included in the request headers, Country of origin is determined based on the first IP address listed in the header value (true client IP).

## HTTP Header Controls[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-access-control\#http-header-controls)

![cnaf http headers](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-621510f2a31963ce0d4c8575d7af857ebb62df65%252Fcnaf_http_headers.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=a3e19392f14388c7a95b36f2188302de&sv=3)

WAAS lets you block or allow requests which contain specific strings in HTTP headers by specifying a header name and a value to match. The value can be a full or partial string match. Standard [pattern matching](https://docs.prismacloud.io/admin-guide/configure/rule-ordering-pattern-matching#pattern-matching) is supported.

If the **Required** toggle is set to **On** WAAS will apply the defined action on HTTP requests in which the specified HTTP header is missing. When the **Required** toggle is set to **Off** no action will be applied for HTTP requests missing the specified HTTP header.

HTTP Header fields consist of a name, followed by a colon, and then the field value. When decoding field values, WAAS treats all commas as delimiters. For example, the `Accept-Encoding` request header advertises which compression algorithm the client supports.

AskCopy

```
Accept-Encoding: gzip, deflate, br
```

WAAS rules do not support exact matching when the value in a multi-value string contains a comma because WAAS treats all commas as delimiters. To match this type of value, use wildcards. For example, consider the following header:

AskCopy

```
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36
```

To match it, specify the following wildcard expression in your WAAS rule:

AskCopy

```
Mozilla/5.0*
```

## File Upload Controls[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-access-control\#file-upload-controls)

![cnaf file upload](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-cb0111bd14401675304fb11d407e6d40213cd39f%252Fcnaf_file_upload.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=ed73d1cc34dbcd16e7f6ea97f481f59a&sv=3)

Attackers may try to upload malicious files (e.g. malware) to your systems. WAAS protects your applications against malware dropping by restricting uploads to just the files that match any allowed content types. All other files will be blocked.

Files are validated both by their extension and their [magic numbers](https://en.wikipedia.org/wiki/Magic_number_(programming)). Built-in support is provided for the following file types:

- Audio: aac, mp3, wav.

- Compressed archives: 7zip, gzip, rar, zip.

- Documents: odf, pdf, Microsoft Office (legacy, Ooxml).

- Images: bmp, gif, ico, jpeg, png.

- Video: avi, mp4.


WAAS rules let you explicitly allow additional file extensions. These lists provide a mechanism to extend support to file types with no built-in support, and as a fallback in case Prisma Cloud’s built-in inspectors fail to correctly identify a file of a given type. Any file with an allowed extension is automatically permitted through the firewall, regardless of its 'magic number'.

[PreviousBot protection](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-bot-protection) [NextAdvanced settings](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-advanced-settings)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject

For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/configure/subject-alternative-names.md).

You can add or remove Subject Alternative Names (SANs) to Console’s certificate. The subjectAltName extension is described in [RFC6125](https://tools.ietf.org/html/rfc6125). It defines a mechanism for adding identities to Public Key Infrastructure X.509v3 (PKIX) certificates.

Defender communicates with Console using Transport Layer Security (TLS). When Defender tries to establish a secure connection with Console, it must validate Console’s identity. Defender checks a reference identity against the identifiers presented in Console’s PKIX certificate, searching for a match. The reference identity is set when you deploy Defender. It’s the name you configured Defender to use to connect to Console.

When deploying Prisma Cloud Console, setting up a DNS name for it is considered a best practice. RFC6125 says:

"IP addresses are not necessarily reliable identifiers for application services because of the existence of private internets \[PRIVATE\], host mobility, multiple interfaces on a given host, Network Address Translators (NATs) resulting in different addresses for a host from different locations on the network, the practice of grouping many hosts together behind a single IP address, etc. Most fundamentally, most users find DNS domain names much easier to work with than IP addresses, which is why the domain name system was designed in the first place."

## Adding a SAN to Console’s certificate[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/subject-alternative-names\#adding-a-san-to-consoles-certificate)

Add a SAN to Console’s certificate directly from Console’s web interface.

1. Open Console.

2. Go to **Manage > Defenders > Names**.

3. Click **Add SAN**.

4. Enter a DNS name or IP address.

5. Click **Add**.


[PreviousReconfigure Prisma Cloud](https://docs.prismacloud.io/admin-guide/configure/reconfigure-twistlock) [NextWildFire settings](https://docs.prismacloud.io/admin-guide/configure/wildfire)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject

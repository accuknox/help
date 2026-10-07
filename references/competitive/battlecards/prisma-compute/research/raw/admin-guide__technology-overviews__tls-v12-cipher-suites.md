For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/technology-overviews/tls-v12-cipher-suites.md).

Prisma Cloud Compute uses the Go programming language cryptographic libraries to protect all network communications via the Transport Layer Security (TLS) v1.2 protocol.

## Prisma Cloud Compute Self-Hosted[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/tls-v12-cipher-suites\#prisma-cloud-compute-self-hosted)

The User Interface (UI) and API access is protected using server side TLS v1.2 authentication. The cipher suites offered by the Console adhere to [NIST SP800-52r2](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-52r2.pdf) guidance.

- TLS\_ECDHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384

- TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA

- TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_GCM\_SHA384

- TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_CBC\_SHA


The Console enforces HTTP Strict Transport Security (HSTS).

### Validating Console’s UI and API TLS cipher suites[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/tls-v12-cipher-suites\#validating-consoles-ui-and-api-tls-cipher-suites)

Use [nmap](https://nmap.org/) to confirm the cipher suites supported by the Console.

1. Install [nmap](https://nmap.org/)

2. Call the Console’s UI/API endpoint (default TCP port 8083) to enumerate the ciphers suites supported by the Console.

















AskCopy



```
$ nmap -sV --script ssl-enum-ciphers -p 8083 172.17.0.2
```









The following is an abbreviated return from the nmap command:

















AskCopy



```
Starting Nmap 7.60 ( https://nmap.org ) at 2022-02-16 21:32 UTC
Nmap scan report for 172.17.0.2
Host is up (0.000046s latency).

PORT     STATE SERVICE     VERSION
8083/tcp open  ssl/us-srv?
| fingerprint-strings:

..
..
..

| ssl-enum-ciphers:
|   TLSv1.2:
|     ciphers:
|       TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 (secp256r1) - A
|       TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA (secp256r1) - A
|     compressors:
|       NULL
|     cipher preference: server
|_  least strength: A
```


### Console to Defender communication[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/tls-v12-cipher-suites\#console-to-defender-communication)

The Console and Defenders communication using a mutual TLS v1.2 web-socket session (default TCP 8084). The allowed cypher suites used for this communication adhere to [NIST SP800-52r2](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-52r2.pdf) guidance.

- TLS\_ECDHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384

- TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA


The certificate/keys used for the Console to Defender mutual TLS v1.2 web socket session are generated during the Console’s initiation process. The reason for this is to ensure the Console is only communicating with the Defenders it has deployed and the Defenders only communicate with its controlling Console.

### Validating Console to Defender communication[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/tls-v12-cipher-suites\#validating-console-to-defender-communication)

Use [nmap](https://nmap.org/) to confirm the cipher suites supported by the Console.

1. Install [nmap](https://nmap.org/)

2. Call the Console’s Defender communications endpoint (default TCP port 8084) to enumerate the ciphers suites supported by the Console for Defender communications.

















AskCopy



```
$ nmap -sV --script ssl-enum-ciphers -p 8084 172.17.0.2
```









Following is a return from the nmap command

















AskCopy



```
Starting Nmap 7.60 ( https://nmap.org ) at 2022-02-16 22:30 UTC
Nmap scan report for 172.17.0.2
Host is up (0.000048s latency).

PORT     STATE SERVICE     VERSION
8084/tcp open  ssl/unknown
| ssl-enum-ciphers:
|   TLSv1.2:
|     ciphers:
|       TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 (secp256r1) - A
|       TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA (secp256r1) - A
|     compressors:
|       NULL
|     cipher preference: server
|_  least strength: A
```


## Prisma Cloud Compute Enterprise (SaaS)[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/tls-v12-cipher-suites\#prisma-cloud-compute-enterprise-saas)

The Compute Console runs within a Google Cloud Platform’s Google Kubernetes Engine (GKE). The GKE Console containers are fronted by GCP Load Balancers that have been configured to use the [Modern](https://cloud.google.com/load-balancing/docs/ssl-policies-concepts) pre-configured profile. The Modern profile supports a wide set of SSL features, allowing modern clients to negotiate SSL.

### Validating Console’s UI and API TLS cipher suites (SaaS)[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/tls-v12-cipher-suites\#validating-consoles-ui-and-api-tls-cipher-suites-saas)

Use [nmap](https://nmap.org/) to confirm the cipher suites supported by the Console.

1. Install [nmap](https://nmap.org/)

2. Call the Console’s UI/API endpoint (default TCP port 443) to enumerate the ciphers suites supported by the Console. The Console’s URL can be found within the Compute Module’s **Manage > System > Utilities > Path to Console**.

















AskCopy



```
$ nmap -sV --script ssl-enum-ciphers -p 443 us-west1.cloud.twistlock.com
```









The following is an abbreviated return from the nmap command:

















AskCopy



```
Starting Nmap 7.70 ( https://nmap.org ) at 2022-02-28 22:44 UTC
Nmap scan report for us-west1.cloud.twistlock.com (34.82.51.12)
Host is up (0.073s latency).

PORT    STATE SERVICE  VERSION
443/tcp open  ssl/http nginx 1.17.10
|_http-server-header: nginx/1.17.10
| ssl-enum-ciphers:
|   TLSv1.2:
|     ciphers:
|       TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 (ecdh_x25519) - A
|       TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256 (ecdh_x25519) - A
|       TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 (ecdh_x25519) - A
|     compressors:
|       NULL
|     cipher preference: server
|_  least strength: A
```


### Console to Defender communication (SaaS)[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/tls-v12-cipher-suites\#console-to-defender-communication-saas)

The SaaS Console and Defender communication uses the same TCP port (i.e. 443) and cipher suites as the UI/API endpoint.

## Credential store’s secrets storage[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/tls-v12-cipher-suites\#credential-stores-secrets-storage)

Local username/password accounts within a local database table using HMAC256. This is in compliance with [NIST SP800-107r1](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-107r1.pdf). Currently, there are seven approved hash algorithms specified in FIPS 180-4: SHA-1, SHA-224, **SHA-256**, SHA-384 SHA-512, SHA-512/224 and SHA-512/256.

## Industrial guidance[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/tls-v12-cipher-suites\#industrial-guidance)

### NIST SP800-52r2[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/tls-v12-cipher-suites\#nist-sp800-52r2)

[NIST Special Publication 800-52r2](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-52r2.pdf) provides guidance to the selection and configuration of TLS protocol implementations while making effective use of Federal Information Processing Standards (FIPS) and NIST-recommended cryptographic algorithms. Prisma Cloud Compute’s cipher suites adhere to SP800-52r2 guidance.

NIST SP800-52r2 approved suites

Compute cipher suites

TLS\_ECDHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384

TLS\_ECDHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384

TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA

TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA

TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_GCM\_SHA384

TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_GCM\_SHA384

TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_CBC\_SHA

TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_CBC\_SHA

### NSA approved[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/tls-v12-cipher-suites\#nsa-approved)

The [NSA’s Commercial National Security Algorithm Suite](https://apps.nsa.gov/iaarchive/programs/iad-initiatives/cnsa-suite.cfm) provides cryptographic guidance for replacement of Suite B algorithms prior to the availability of quantum resistant algorithms. "For those customers who are looking for mitigations to perform while the new algorithm suite is developed and implemented into products, there are several things they can do." These recommendations have been implemented within Prisma Cloud’s cryptographic settings.

Function

NSA recommendation

Compute cipher

Guidance

Key establishment

RSA - 3072 key ECDHE - Curve P-384

**TLS\_ECDHE\_RSA**\_WITH\_AES\_256\_GCM\_SHA384 **TLS\_ECDHE\_RSA**\_WITH\_AES\_256\_CBC\_SHA **TLS\_RSA**\_WITH\_AES\_256\_GCM\_SHA384 **TLS\_RSA**\_WITH\_AES\_256\_CBC\_SHA **TLS\_ECDHE\_ECDSA**\_WITH\_AES\_256\_GCM\_SHA384 **TLS\_ECDHE\_ECDSA**\_WITH\_AES\_256\_CBC\_SHA

[Generate the appropriate certificate and key size for Console TLS UI and API endpoint](https://docs.prismacloud.io/admin-guide/configure/certificates)

Symmetric block cipher used for information protection

AES 256

TLS\_ECDHE\_RSA\_WITH\_ **AES\_256\_GCM\_SHA384** TLS\_ECDHE\_RSA\_WITH\_ **AES\_256\_CBC\_SHA** TLS\_RSA\_WITH\_ **AES\_256\_GCM\_SHA384** TLS\_RSA\_WITH\_ **AES\_256\_CBC\_SHA** TLS\_ECDHE\_ECDSA\_WITH\_ **AES\_256\_GCM\_SHA384** TLS\_ECDHE\_ECDSA\_WITH\_ **AES\_256\_CBC\_SHA**

All cipher suites enforce the AES 256 block cipher. Both GCM and CBC modes are supported.

[PreviousHost Defender architecture](https://docs.prismacloud.io/admin-guide/technology-overviews/host-defender-architecture) [NextTelemetry](https://docs.prismacloud.io/admin-guide/technology-overviews/telemetry)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject

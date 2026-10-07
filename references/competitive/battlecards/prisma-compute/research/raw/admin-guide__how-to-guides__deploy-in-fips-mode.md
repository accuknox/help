For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/how-to-guides/deploy-in-fips-mode.md).

The Console, Defender and twistcli Compute components can run using FIPS140-2 Level 1 validated cryptographic modules. The Compute GoLang components are statically compiled with the [BoringCrypto module](https://boringssl.googlesource.com/boringssl/+/master/crypto/fipsmodule/FIPS.md), using the built-in mechanism introduced in Go1.19 [GOEXPERIMENT](https://pkg.go.dev/internal/goexperiment).

The cipher suites used are:

- TLS\_ECDHE\_RSA\_WITH\_AES\_128\_GCM\_SHA256

- TLS\_ECDHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384

- TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_GCM\_SHA256

- TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_GCM\_SHA384


The following procedures are for [self-hosted](https://docs.prismacloud.io/admin-guide/welcome/pcee-vs-pcce) deployments only.

Deploying Defenders on ARM64 architecture in FIPS mode is not supported.

1. Download the latest release tar bundle from the Palo Alto Networks [Customer Support Portal](https://support.paloaltonetworks.com/).











Note that v22.12 or later is certified for FIPS.

2. Untar the release

















AskCopy



```
$ tar -xzf prisma_cloud_compute_<VERSION>.tar.gz
```

3. Set the FIPS mode for deployment.









   - For Onebox deployments, modify twistlock.cfg and set the FIPS\_ENABLED flag to "true."

















     AskCopy



     ```
     ##### FIPS configuration #####
      # Forces Console and Defender to use FIPS-compliant cryptography, https://csrc.nist.gov/projects/cryptographic-module-validation-program
      FIPS_ENABLED=true
     ```

   - For Kubernetes deployments, download the Defender YAML file from Console and and set the FIPS\_ENABLED flag to "true."


4. Deploy the Console either via the [Onebox](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-onebox) or [Kubernetes](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-kubernetes) deployment methods.

5. To confirm the Console is running in FIPS mode, login to the Console and go to Manage > Logs > Console and search for "FIPS." _FIPSEnabled: true_ is confirmation that the Console has started in FIPS mode.

















AskCopy



```
manager.go:73 Starting Console manager: ConsoleCN: STIG.lomsgaupfzzurnlkzzmxivmymh.cx.internal.cloudapp.net, ConsoleSAN: [IP:127.0.0.1 IP:10.0.1.4 IP:172.17.0.1], IsProd: true, DataRecoveryEnabled: true, DefenderPort: 8084, MgmtPortHTTPS: 8083, Version: 22.12.415, FIPSEnabled: true
```

6. To confirm that the Defender is running in FIPS mode, login to the Console and go to Manage > Defenders > Defenders: Deployed in the Actions column of the Defender(s) click Logs and search for "FIPS."

















AskCopy



```
defender.go:778 FIPS mode enabled true
```

7. When using the _twistcli_ command line tool use the **FIPS\_ENABLED=true** variable to enforce FIPS validated TLS communication to the Console, for example:

















AskCopy



```
$ FIPS_ENABLED=true ./twistcli images scan --address https://127.0.0.1:8083 0c413668ee0d
```

8. The Jenkins plug-in communication to the Console can enforce FIPS compliant TLS traffic, enable **FIPS mode** in the Prisma Cloud Jenkins plug-in’s configuration.















![jenkins plug in fips](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-ba0473197cc2f170802f9da9c2448b3a1568a4f3%252Fjenkins_plug_in_fips.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=483ef4f8375fb099d1ef512be523c7ad&sv=3)


[PreviousReview debug logs](https://docs.prismacloud.io/admin-guide/how-to-guides/review-debug-logs) [NextRun third-party assessment tools](https://docs.prismacloud.io/admin-guide/how-to-guides/twistcli-sandbox-third-party-scan)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject

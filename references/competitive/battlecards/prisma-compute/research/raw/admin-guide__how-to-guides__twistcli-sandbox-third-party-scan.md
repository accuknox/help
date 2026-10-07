For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/how-to-guides/twistcli-sandbox-third-party-scan.md).

In the [Lagrange release (v22.12+)](https://docs.paloaltonetworks.com/prisma/prisma-cloud/22-12/prisma-cloud-compute-edition-release-notes/release-information) the [twistcli image analysis sandbox](https://docs.prismacloud.io/admin-guide/runtime-defense/image-analysis-sandbox) capability allows for the execution of third-party assessment tools. You can supply a third-party binary/script that is executed after the twistcli sandbox image analysis is completed. The output of the third-party tool can be captured within a volume mount for further analysis. Twistcli sandbox analysis occurs within a temporary container of the image under examination. No modifications are made to the image under analysis.

In this example we will use the [OpenSCAP](https://www.open-scap.org/) utility to perform a [Compliance as Code’s v0.1.65 RHEL-8 STIG profile](https://github.com/ComplianceAsCode/content/blob/master/products/rhel8/profiles/stig.profile) scan of a [RedHat Universal Base Image 8](https://catalog.redhat.com/software/containers/ubi8/ubi/5c359854d70cc534b3a3784e).

1. On the host on which the twistcli sandbox analysis will occur create a directory `/opt/sandbox`.

2. Download the [latest ComplianceAsCode release](https://github.com/ComplianceAsCode/content/releases), extract `ssg-rhel8-ds.xml` and copy to the `/opt/sandbox` directory.

3. Copy the following bash script to `/opt/sandbox/openscap_analysis.sh`.

















AskCopy



```
#!/bin/bash
# Install tools and OpenSCAP
yum update -y -q
yum install -y -q openscap-scanner

# Run OpenSCAP scan
# Note: HTML and XML OSCAP output files are written to the host mounted directory
oscap xccdf eval --profile xccdf_org.ssgproject.content_profile_stig --report /opt/sandbox/openscap_sandbox_stig.html --results /opt/sandbox/openscap_sandbox_stig.xml /opt/sandbox/ssg-rhel8-ds.xml
```

4. Set the executable flag on openscap\_analysis.sh.

















AskCopy



```
$ chmod +x openscap_analysist.sh
```

5. Execute twistcli sandbox analysis of the ubi:8.7-1037 image with the following command:

















AskCopy



```
linux/twistcli sandbox \
   --address https://127.0.0.1:8083 \
   --volume /opt/sandbox:/opt/sandbox \
   --third-party-delay 5s \
   --third-party-cmd /opt/sandbox/openscap_analysis.sh \
   --third-party-output /opt/sandbox/oscap-results.txt \
registry.access.redhat.com/ubi8/ubi:8.7-1037
```









Where:









   - `--volume /opt/sandbox:/opt/sandbox` \- mounts the host’s /opt/sandbox directory into the running container’s /opt/sandbox. The files necessary to execute the OpenSCAP scan are read from this directory and the output of the script is written to this directory.

   - `--third-party-delay 5s` \- time delay after the sandbox analysis completes and the third party script is executed.

   - `--third-party-output /opt/sandbox/oscap-results.txt` \- path to output results.


6. The following output files are written to the host’s /opt/sandbox directory:









   - openscap\_sandbox\_stig.html - OSCAP report output.

   - openscap\_sandbox\_stig.xml - OSCAP results output.

   - oscap-results.txt - stdout captured during the execution of openscap\_analysis.sh.


[PreviousDeploy in FIPS mode](https://docs.prismacloud.io/admin-guide/how-to-guides/deploy-in-fips-mode)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject

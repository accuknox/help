For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/configure/custom-feeds.md).

You can supplement the Prisma Cloud Intelligence Stream with your own custom data, including:

- Suspicious or high-risk IP addresses

- Malware signatures

- Trusted executables

- [Custom vulnerabilities for proprietary software components](https://docs.prismacloud.io/admin-guide/vulnerability-management/scan-images-for-custom-vulnerabilities)

- Allowed CVEs


For each data type, you can add individual entries to a table from the Console web interface, bulk upload a list from a CSV file, or submit a JSON object using the Prisma Cloud API.

## Supplementing the IP reputation list[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/custom-feeds\#supplementing-the-ip-reputation-list)

You can supplement the Prisma Cloud Intelligence Stream with your own list of suspicious or high-risk IP addresses that you want to ban on your network.

1. Open Console.

2. Go to **Manage > System > Custom Feeds**.

3. Click **IP Reputation Lists**, and either click **Add IP** or **Import CSV**.











Your list of banned IP addresses is immediately enforced when your data is imported. A default runtime defense rule, **Default - detect suspicious runtime behavior**, logs an alert when a container tries to connect to a banned IP address.











You can manually add one entry at a time, or do a bulk upload from a CSV file. The maximum file size for a csv is 20MB.











The first line in your CSV file must be a header record that contains the field names. Specify one IP address per line. For example:

















AskCopy



```
ip
99.104.125.48
101.200.81.187
103.19.89.118
```

4. Review the default rule











Go to **Defend > Runtime > {Container Policy \| Host Policy}**, then click manage for the **Default - detect suspicious runtime behavior** rule. You should see that **Prisma Cloud Advanced Threat Protection** is set to **On**.


## Create a list of malware signatures and trusted executables[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/custom-feeds\#create-a-list-of-malware-signatures-and-trusted-executables)

You can supplement the Prisma Cloud Intelligence Stream with your own custom malware signatures and trusted executable list. The trusted executable list is a mechanism to address potential misidentification of legitimate files as malware.

You can add MD5 hashes of custom malicious executables to the malware signatures list, it enables you to monitor malware that you want to alert or block in runtime rules.

Malware scanning and detection is supported for Linux container images and hosts only. Windows containers and hosts are not supported.

When you add MD5 hashes (signatures of binaries) to the trusted executables list, it enables you to ensure that a legitimate binary is not potentially identified as malicious by file system based defense capability in runtime rules.

The trusted executable list does not apply to other runtime defense capabilities, such as process runtime protection. To exclude files from other runtime detection capabilities use the allowed list in the [runtime defense section](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/runtime-defense/runtime-defense.md).

1. Open Console.

2. Go to **Manage > System > Custom Feeds**.

3. Select **Malware signatures** or **Trusted executables**.

4. Choose how to add the MD5 hashes for malware signatures or trusted executables.











The MD5 hashes you add to either list of custom feed, are used in all subsequent image scans. It is also used immediately by the runtime defense file system sensor, which assesses all writes to the host and container file system.









1. For **Add MD5**, you can manually add one entry at a time.

2. For **Import CSV**, you can bulk upload from a CSV file.











      The maximum file size is 20MB.











      The first line in your CSV file must be a header record that contains the field names.











      Specify one entry per line. Each entry must include the MD5, followed by a good description to identify why the MD5 is trusted ( in the case of trusted executables) or is known to be malicious (in the case of malware signatures).











      For example:

















      AskCopy



      ```
      md5,name
      194836fbe0f121a25b145e55e80cef22,legitimate binary built in-house
      0aeb0cac186a81a6ac45776d6b56dd70,test file
      33cc273ae3aa8bce6a22c92e7d11f63a,benign file
      ```


5. Review the default rule.











A default runtime defense rule, **Default - detect suspicious runtime behavior**, logs an alert when malware is detected using signatures from the Prisma Cloud data set or your custom data set.











To review the default rule, go to **Defend > Runtime > {Container Policy \| Host Policy}**, then click manage for the **Default - detect suspicious runtime behavior** rule. You should see that **Prisma Cloud Advanced Threat Protection** is set to **On**.


## Allowing CVEs globally[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/custom-feeds\#allowing-cves-globally)

Some organizations have have very sophisticated CI pipelines that encompass many teams and products. When your security team concludes that a CVE doesn’t impact the organization, they want to dismiss it globally without having to manage individual rules or exceptions.

The CVE Allow List lets you allow CVEs system-wide. Any entry in the CVE Allow List affects all flows in the product, including twistcli, the Jenkins plugin, registry scanning, deployment blocking, Vulnerability Explorer, and so on. Adding a CVE to this list effectively filters it out from the data in the Prisma Cloud Intelligence Stream before it’s used by the scanner.

The CVE Allow List takes precedence over any rule that’s been created under **Defend > Vulnerabilities**. It is a feature designed to complement rules. Rules also let you allow a CVE, but more granularly, by scoping them to specific resources or parts of your environment.

1. Open Console.

2. Go to **Manage > System > Custom Feeds**.

3. Click **CVE Allow List**, and either click **Add CVE** or **Import CSV**.











You can set an expiration date for the CVE, if you want to set a time restriction for when it should no longer be allowed.


## Test Prisma Cloud malware detection capabilities[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/custom-feeds\#test-prisma-cloud-malware-detection-capabilities)

Safely simulate malware in your environment to test the malware detection capabilities on Prisma Cloud.

### Configure a custom malware feed[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/custom-feeds\#configure-a-custom-malware-feed)

Set up a custom feed by uploading the provided CSV file to Prisma Cloud Console. This file specifies the MD5 signature for a file that will be considered malware for the purposes of this demo.

1. Download [_malware.csv_](https://cdn.twistlock.com/docs/attachments/malware.csv).

2. In Console, go to **Manage > System > Custom Feeds > Malware Signatures**.

3. Click **Import CSV**, and upload _malware.csv_.


### Detect malware at runtime[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/custom-feeds\#detect-malware-at-runtime)

Test how Prisma Cloud detects malware being downloaded into a container at runtime.

**Prerequisites:** The default runtime rule, **Default - alert on suspicious runtime behavior** under **Defend > Runtime > Container Policy** is in place. If you have deleted or changed the default rule, create a new one.

1. Go to **Defend > Runtime > Container Policy**, and click **Add rule**.

2. Enter a name for the rule.

3. In the **General** tab, verify **Prisma Cloud Advanced Threat Protection** is **On**.

4. In each of the **Process**, **Networking**, **File System**, and **System Calls** tabs, set **Effect** to **Alert**.

5. Run a container and download malware into it.

















AskCopy



```
$ docker run -ti alpine sh
/ # wget https://cdn.twistlock.com/docs/attachments/evil
```

6. Look at resulting audit. Open Console and browse to **Monitor > Events > Container Audits**. You will see a file system audit that says malware was detected.















![malware detected](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-61dc9a82f950665ab8367a94ea473a7dce4f3c06%252Fmalware_detected.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=7e7c77b36e9309142c95a7edc8ab9884&sv=3)


[PreviousBackup and restore](https://docs.prismacloud.io/admin-guide/configure/disaster-recovery) [NextProxy configuration](https://docs.prismacloud.io/admin-guide/configure/proxy)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject

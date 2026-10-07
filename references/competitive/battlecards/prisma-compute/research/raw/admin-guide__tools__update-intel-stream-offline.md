For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/tools/update-intel-stream-offline.md).

Prisma Cloud lets you update Console’s vulnerability and threat data even if it runs in an offline environment.

The Prisma Cloud Intelligence Stream (IS) is a real-time feed that contains vulnerability data and threat intelligence from commercial providers, Prisma Cloud Labs, and the open source community.

When you install Prisma Cloud, Console is automatically configured to connect to intelligence.twistlock.com to download updates. The IS is updated several times per day, and Console continuously checks for updates.

If you run Prisma Cloud in an offline environment, where Console does not have access to the Internet to download updates from the IS, then you can manually download and install IS updates.

## Update strategies for offline environments[Direct link to heading](https://docs.prismacloud.io/admin-guide/tools/update-intel-stream-offline\#update-strategies-for-offline-environments)

There are a number of update strategies. The right strategy for you depends on the size of your deployment, and in particular, the number of air-gapped Consoles in your environment.

### Basic strategy[Direct link to heading](https://docs.prismacloud.io/admin-guide/tools/update-intel-stream-offline\#basic-strategy)

Use the basic strategy when you’ve got one or two air-gapped Consoles. The basic strategy for updating the threat data for an isolated, air-gapped Console is:

- [Download the IS data](https://docs.prismacloud.io/admin-guide/tools/update-intel-stream-offline#twistcli-download) from an Internet-connected machine.

- Move the archived data to a location accessible by the air-gapped environment.

- [Load the IS data](https://docs.prismacloud.io/admin-guide/tools/update-intel-stream-offline#twistcli-upload) into the offline Console.


Both the download and upload operations use twistcli, so the process can be automated.

If you’ve got a large number of air-gapped Consoles, individually updating each one can be challenging and brittle, especially in dynamic environments. As such, Prisma Cloud lets you scale the basic strategy to any number of Consoles. Each deployed Console can be configured to look for the latest threat data in a central location. From there, each Console will update itself every 24 hours. Your job is to ensure that the central location always serves the latest threat data.

For example, consider how the U.S. Navy would keep a fleet of submarines up-to-date with the latest threat data. When a submarine surfaces and establishes brief connection to its command’s network, the submarine’s Console needs to pull the latest Intelligence Stream updates. For this type of setup, see [Scale approach 1](https://docs.prismacloud.io/admin-guide/tools/update-intel-stream-offline#scale-approach1) and [Scale approach 2](https://docs.prismacloud.io/admin-guide/tools/update-intel-stream-offline#scale-approach2).

### Scale approach 1[Direct link to heading](https://docs.prismacloud.io/admin-guide/tools/update-intel-stream-offline\#scale-approach-1)

Distribute the latest Intelligence Stream data from an HTTP/S server. Use the [basic strategy](https://docs.prismacloud.io/admin-guide/tools/update-intel-stream-offline#basic-strategy) to keep the data at the endpoint up-to-date. To configure your Console for this approach, see [Download the IS from an HTTP server](https://docs.prismacloud.io/admin-guide/tools/update-intel-stream-offline#distribution-https).

### Scale approach 2[Direct link to heading](https://docs.prismacloud.io/admin-guide/tools/update-intel-stream-offline\#scale-approach-2)

Distribute the latest Intelligence Stream data from a so-called "relay" Console. Downstream Consoles connect to the relay Console to pull the latest threat data. To keep the relay Console up-to-date:

- Use the [basic strategy](https://docs.prismacloud.io/admin-guide/tools/update-intel-stream-offline#basic-strategy) when the relay Console is also isolated in an air-gapped environment.

- Let the relay Console update itself by connecting to the Intelligence Stream over the Internet.


To configure your Console for this approach, see [Download the IS from another Console](https://docs.prismacloud.io/admin-guide/tools/update-intel-stream-offline#distribution-console).

### Projects[Direct link to heading](https://docs.prismacloud.io/admin-guide/tools/update-intel-stream-offline\#projects)

By default, [projects](https://docs.prismacloud.io/admin-guide/deployment-patterns/projects) utilize the distribution mechanism described in [Scale approach 2](https://docs.prismacloud.io/admin-guide/tools/update-intel-stream-offline#scale-approach2). Central Console connects to https://intelligence.twistlock.com to retrieve the latest threat data. All tenant projects connect to Central Console to get the latest threat data. Central Console itself can be configured for [manual threat feed updates](https://docs.prismacloud.io/admin-guide/tools/update-intel-stream-offline#basic-strategy), [Scale approach 1](https://docs.prismacloud.io/admin-guide/tools/update-intel-stream-offline#scale-approach1), or [Scale approach 2](https://docs.prismacloud.io/admin-guide/tools/update-intel-stream-offline#scale-approach2).

To force Central Console to push Intelligence Stream updates down to all tenants, go to **Manage > System > Intelligence** in the Central Console and click **Update Now**.

## Download the IS data with twistcli[Direct link to heading](https://docs.prismacloud.io/admin-guide/tools/update-intel-stream-offline\#download-the-is-data-with-twistcli)

Before starting, ensure the Internet-connected host to where you will initially download the data can access the Intelligence Stream. The most reliable way to test connectivity is to ping the Intelligence Stream. This following curl command verifies that name resolution and any intermediary HTTP proxies are functioning properly.

AskCopy

```
$ curl -k \
  --silent \
  --output /dev/null \
  --write-out "%{http_code}\n" \
  https://intelligence.twistlock.com/api/v1/_ping
```

If you’ve got connectivity, you’ll get back a 200 (Successful) response code.

AskCopy

```
200
```

1. Open Console.

2. Go to **Manage > System > Intelligence**.

3. Copy the access token.

4. Download twistcli. You have several options:









   - Download twistcli from the Console UI. Go to **Manage > System > Utilities**.

   - Download twistcli from the API. Use `/api/v1/util/twistcli` for the Linux binary or `/api/v1/util/osx/twistcli` for the macOS binary..

   - Get a copy from the release tarball.


5. Download the the Intelligence Stream data.











Open a shell window, and run the following command:

















AskCopy



```
$ ./linux/twistcli intelligence download --token <ACCESS-TOKEN>
```









All data is downloaded and saved in a file named _twistlock\_feed\_<random\_string>.tar.gz_


## Upload IS data to Console with twistcli[Direct link to heading](https://docs.prismacloud.io/admin-guide/tools/update-intel-stream-offline\#upload-is-data-to-console-with-twistcli)

Use the _twistcli_ tool to upload the Intelligence Stream archive to your Prisma Cloud Console.

**Prerequisite:** You’ve disabled over-the-Internet updates for your air-gapped Console. Go to **Manage > System > Intelligence** and set **Update the Intelligence Stream from Prisma Cloud over the Internet** to **Off**.

1. Download twistcli. You have several options:









   - Download twistcli from the Console UI. Go to **Manage > System > Utilities**.

   - Download twistcli from the API. Use `/api/v1/util/twistcli` for the Linux binary or `/api/v1/util/osx/twistcli` for the macOS binary..

   - Get a copy from the release tarball.


2. Run the following command:

















AskCopy



```
$ ./linux/twistcli intelligence upload \
     --address \https://<COMPUTE-CONSOLE>:8083 \
     --user <USER> \
     --password <PASSWORD> \
     --tlscacert <PATH-TO-CERT> \
     <FEED-ARCHIVE>
```









Where:











`<COMPUTE-CONSOLE>`
URL for the air-gapped Console.











`<USER>, <PASSWD>`
Credentials for a user with a minimum [role](https://docs.prismacloud.io/admin-guide/authentication/user-roles) of Vulnerability Manager.











`<PATH-TO-CERT>`
(Optional) Path to to Prisma Cloud’s CA certificate file. With the CA cert, a secure connection is used to upload the intelligence data to Console. For example, `/var/lib/twistlock/certificates/console-cert.pem`.











`<FEED-ARCHIVE>`
File generated from [downloading an archive of the IS with twistcli](https://docs.prismacloud.io/admin-guide/tools/update-intel-stream-offline#twistcli-download). For example, `twistlock_feed_1524655717.tar.gz`.











Sometimes after Console is restarted, you might see an error on the login page that says "failed to query license". This is by design, and it’s not a bug. It happens because a Console restart triggers a user auth token renewal. For more information, see [long-lived tokens](https://docs.prismacloud.io/admin-guide/configure/logon-settings).


## Download the IS from an HTTP server[Direct link to heading](https://docs.prismacloud.io/admin-guide/tools/update-intel-stream-offline\#download-the-is-from-an-http-server)

Configure Console to download the IS archive file from a custom HTTPS location.

When enabled, Console downloads the file from this location every 24 hours. If the download fails, Console retries every 1 hour until it’s successful, then waits for 24 hours until the next download.

In this strategy, you must get the latest IS data with twistcli and copy the archive file to the HTTP/S server, where the air-gapped Console(s) will retrieve it.

1. Open Console.

2. Go to **Manage > System > Intelligence**.

3. Set **Update the Intelligence Stream from a custom location** to **On**.

4. In **Address**, specify the full URL to the HTTP/S endpoint where the archive is served.

5. If credentials are required to access this endpoint, create them.

6. (Optional) Configure a certificate chain for trusting the HTTPS endpoint.

7. Click **Save**.











Console immediately attempts to load the IS data from the specified endpoint. Assuming, Console is successful, it schedules subsequent updates every 24 hours. Click **Update Now** to force an immediate update.


## Download the IS from another Console[Direct link to heading](https://docs.prismacloud.io/admin-guide/tools/update-intel-stream-offline\#download-the-is-from-another-console)

You can configure a Console to retrieve the latest Intelligence Stream data from another Console. In this configuration, you have a single relay Console, and all other deployed Consoles connect to it to retrieve the latest Intelligence Stream data.

When enabled, Console downloads the file from this location every 24 hours. If the download fails, Console retries every 1 hour until it’s successful, then waits for 24 hours until the next download.

In this strategy, you must implement a method for the relay Console to get a copy of the latest Intelligence Stream data.

1. Open Console.

2. Go to **Manage > System > Intelligence**.

3. Set **Update the Intelligence Stream from a custom location** to **On**.

4. In **Address**, specify the full URL to the relay Console.











https://<COMPUTE-CONSOLE>:8083/api/v1/feeds/bundle











Where:











`<COMPUTE-CONSOLE>`
URL for the relay Console.

5. In **Credential**, create basic auth credentials for a user that has a minimum role of Vulnerability Manager.

6. Enter a certificate to trust the HTTPS endpoint.









1. Copy the relay Console’s certificate from _/var/lib/twistlock/certificates/ca.pem_, and paste it here.


7. Click **Save**.











Console immediately attempts to load the IS data from the specified endpoint. Assuming, Console is successful, it schedules subsequent updates every 24 hours. Click **Update Now** to force an immediate update.


[PreviousInstall Console with twistcli](https://docs.prismacloud.io/admin-guide/tools/twistcli-console-install) [NextDeployment patterns](https://docs.prismacloud.io/admin-guide/deployment-patterns/deployment-patterns)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject

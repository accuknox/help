For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/welcome/utilities-and-plugins.md).

All Prisma Cloud utilities and plugins can be downloaded directly from the Console UI.

## Downloading Utilities from the Prisma Cloud Console[Direct link to heading](https://docs.prismacloud.io/admin-guide/welcome/utilities-and-plugins\#downloading-utilities-from-the-prisma-cloud-console)

1. Navigate to **Manage** \> **System** \> **Utilities**.











You will find a list of downloadable utilities and plugins available for various platforms.

2. For each utility, you can:









   - Click the **Download** button to download the utility directly to your system.

   - Click the **Copy** button to copy a curl command to run anywhere.


## General Utilities[Direct link to heading](https://docs.prismacloud.io/admin-guide/welcome/utilities-and-plugins\#general-utilities)

1. **Jenkins plugin**: The Jenkins plugin enables integration with Prisma Cloud for seamless security scanning in your CI/CD pipeline.











To download the plugin for Prisma Cloud integration, use any of the following methods:









   - Use the **Download** button to download the plugin directly.

   - Use the **Copy** button to retrieve a curl command for remote download.


2. **VMware Tanzu tile**: The VMware Tanzu Tile allows you to integrate Prisma Cloud with VMware Tanzu, enabling security across your Tanzu-managed workloads.











To download the plugin for Prisma Cloud integration, perform any of the following actions:









   - Use the **Download** button to download the Tanzu integration tile for direct deployment into your VMware Tanzu environment.

   - Use the **Copy** button to get a curl command for remote download.


3. OpenAPI Spec (Beta): The OpenAPI Spec provides a schema definition for the Prisma Cloud API.











To download the plugin for Prisma Cloud integration, use any of the following methods:









   - Use the **Download** button to download the current OpenAPI specification in Beta.

   - Use the **Copy** button to download the OpenAPI spec using curl.


4. Defender Image: Download the Defender image to install in your container environments.











To download the image, perform any of the following actions:









   - Use the **Download** button to download the Defender image.

   - Use the **Copy** button for a curl command.


In addition, you can validate the integrity of Defender images downloaded from the Console using a SHA-256 checksum, ensuring the downloaded image matches the server version. Click the **Show Checksum** button to display the checksum and verify the downloaded image. Click **Hide Checksum** to hide the checksum after you have copied it.

## Twistcli Tool[Direct link to heading](https://docs.prismacloud.io/admin-guide/welcome/utilities-and-plugins\#twistcli-tool)

The twistcli tool is a command-line utility for interacting with Prisma Cloud to scan containers, images, serverless functions, and IaC (Infrastructure-as-Code) templates.

Different versions are available for various platforms:

- Linux x86\_64 platform: Download the twistcli for standard Linux x86\_64 architectures.

- Linux ARM64 platform: Download for ARM64-based systems.

- macOS x86\_64 platform: Download for macOS on Intel-based systems.

- macOS ARM64 platform: Download for Apple Silicon (M1/M2) systems.

- Windows platform: Download the twistcli for Windows environments.


For each platform, you have the option to either: \* Download: Download the utility directly. \* Copy: Copy a curl command to retrieve the tool remotely.

## Path to Console[Direct link to heading](https://docs.prismacloud.io/admin-guide/welcome/utilities-and-plugins\#path-to-console)

When using the Jenkins plugin or the twistcli tool, you need to configure them with the correct Console address.

Use the Copy icon to copy the console path from the **Path to Console** section.

## API Token[Direct link to heading](https://docs.prismacloud.io/admin-guide/welcome/utilities-and-plugins\#api-token)

For access to Prisma Cloud APIs, you will require an API token.

Use the Copy icon to copy the token details from the **API Token** section. This token is used for authentication when making API requests to the Prisma Cloud Console.

The Console UI also shows the token validity. Ensure that the token is stored securely and is rotated before expiration to avoid disruptions in API access.

[PreviousPrisma Cloud Enterprise Edition vs Compute Edition](https://docs.prismacloud.io/admin-guide/welcome/pcee-vs-pcce) [NextInstall](https://docs.prismacloud.io/admin-guide/install/install)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject

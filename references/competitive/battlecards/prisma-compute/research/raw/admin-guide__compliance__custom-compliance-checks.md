For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/compliance/custom-compliance-checks.md).

Custom image checks give you a way to write and run your own compliance checks to assess, measure, and enforce security baselines in your environment.

Prisma Cloud lets you implement your custom image checks with simple scripts.

Custom compliance checks are supported for:

- Linux hosts (Host configured for docker, containerd, or CRI-O)

- Windows containers

- Docker images on Linux hosts

- OCI images


Custom compliance checks are not supported for:

- Defender and Agentless scanning on Windows hosts

- Linux containers

- Docker images on Windows hosts

- Tanzu Application Service (TAS) defender

- GKE Autopilot


A custom image check consists of a single script. The script’s exit code determines the result of the check, where "0" stands for pass and "1" stands for fail.

Scripts are executed in the default shell. The most common default shell for Linux is bash, but that’s not always the case. For Windows container images, the default shell is cmd.exe.

If you want to use a specific shell, or if your default shell is in a non-standard location, use the shebang interpreter directive at the top of your compliance check to specify the path to the executable.

For example, `#!/bin/bash` specifies that the Linux Bourne-again (bash) shell should parse and interpret the compliance check.

For containers, Defender runs the compliance checks inside a restricted sandboxed container instantiated from the image being scanned, thus avoiding the unnecessary risk associated with running arbitrary code.

For hosts, Defender runs the compliance checks on the host itself with unrestricted privileges to allow execution of any script. To limit exposure, this feature is disabled by default.

Every compliance check in the system has a unique ID. Custom checks are automatically assigned an ID, starting with the number 9000. As new custom checks are added, they are automatically assigned the next available ID (9001, 9002, and so on).

Prisma Cloud drops the cached compliance and vulnerability scan results for registries, and rescans registry images, whenever:

- A new rule referencing a custom compliance check is added, or

- An existing compliance check referenced by some existing rule is updated, or

- An existing rule is updated with a new custom compliance check.


In a scaled-out environment with large registries, repeated changes to custom compliance checks could adversely impact on the performance of Prisma Cloud.

## Create a new Custom Check[Direct link to heading](https://docs.prismacloud.io/admin-guide/compliance/custom-compliance-checks\#create-a-new-custom-check)

Create a new compliance rule that includes your custom check, and specify the action to take when the check fails (ignore, alert, block).

**Prerequisite**

- Enable custom compliance checks for hosts (By default, this is disabled).









  - Go to **Manage > Defenders > Advanced Settings**.

  - Set **Custom Compliance Checks for hosts** to enabled.









    - Deploy Defenders to your environment. Or if already deployed, [redeploy your Defenders](https://docs.prismacloud.io/admin-guide/install/deploy-defender/redeploy-defender).


You must redeploy the Defenders everytime you enable **Custom Compliance Checks for hosts**. If you enable the feature, and then later disable it, the disabled state is effective immediately. You don’t have to redeploy Defenders when you switch to the disabled state.

1. Go to **Defend > Compliance > Custom**.

2. Select **Add check**.









1. Enter a **Name** and a **Description**.

2. Specify the **Severity** of the compliance issue.

3. Enter a [script](https://docs.prismacloud.io/admin-guide/compliance/custom-compliance-checks#example-scripts).

4. Select **Save**.


3. Update the compliance policy to run your check.









1. Go to **Defend > Compliance > Containers and Images** for containers or **Defend > Compliance > Hosts** for hosts.

2. Select **Add rule**.

3. Enter a **Rule name**, **Notes**, and select the **Scope** for the resources.

4. Under **Compliance actions**, narrow the compliance checks displayed.











      For containers, on the **All types** drop-down list, select **Custom > Image**.











      For hosts, on the **All types** drop-down list, select **Custom > Custom**.











      You should see a list of custom checks you’ve implemented, starting with ID 9000.

5. Select an action for your custom check ( **Ignore**, **Alert**, or **Block**).

6. Select **Save**.


4. Validate your setup by reviewing the compliance reports under **Monitor > Compliance**.


## Example scripts[Direct link to heading](https://docs.prismacloud.io/admin-guide/compliance/custom-compliance-checks\#example-scripts)

The following example scripts show how to run some basic checks, such as checking file permissions. Use them as starting point for your scripts. Any special utilities or programs required by your script must be installed in the image being evaluated.

### File permissions (Linux)[Direct link to heading](https://docs.prismacloud.io/admin-guide/compliance/custom-compliance-checks\#file-permissions-linux)

The following script checks the permissions for the _/bin/busybox_ file. Assuming busybox is installed in your image, this check should pass.

AskCopy

```
if [ $(stat -c %a /bin/busybox) -eq 755 ]; then
     echo 'test permission failure' && exit 1;
fi
```

### File exists (Linux)[Direct link to heading](https://docs.prismacloud.io/admin-guide/compliance/custom-compliance-checks\#file-exists-linux)

The following script checks if _/tmp/foo.txt_ exists in the container file system. If it doesn’t exist, the check fails.

AskCopy

```
if [ ! -f /tmp/foo.txt ]; then
    echo "File not found!"
    exit 1
fi
```

### User exists (Linux)[Direct link to heading](https://docs.prismacloud.io/admin-guide/compliance/custom-compliance-checks\#user-exists-linux)

The following script checks if the user John exists. If the user exists, the check passes. Otherwise, it fails.

AskCopy

```
if grep -F "John" /etc/passwd
then
    echo yes
else
    echo "user not found!"
    exit 1
fi
```

### File exists (Windows)[Direct link to heading](https://docs.prismacloud.io/admin-guide/compliance/custom-compliance-checks\#file-exists-windows)

The following script checks if _C:\\Users_ exists. If it does, the check passes.

AskCopy

```
IF EXIST C:\Users Echo test permission failure && exit 1
```

### File does not exist (Windows)[Direct link to heading](https://docs.prismacloud.io/admin-guide/compliance/custom-compliance-checks\#file-does-not-exist-windows)

This check is the inverse of the previous check. The script checks if _C:\\Users_ doesn’t exist. If it doesn’t exist, the check passes.

AskCopy

```
IF NOT EXIST C:\Users Echo test permission failure && exit 1
```

[PreviousDISA STIG compliance checks](https://docs.prismacloud.io/admin-guide/compliance/disa-stig-compliance-checks) [NextTrusted images](https://docs.prismacloud.io/admin-guide/compliance/trusted-images)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject

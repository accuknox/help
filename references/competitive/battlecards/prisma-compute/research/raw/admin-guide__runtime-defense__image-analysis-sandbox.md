For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/runtime-defense/image-analysis-sandbox.md).

The image analysis sandbox lets you dynamically analyze the runtime behavior of images before running them in your development and production environments.

The analysis mechanism collects and displays container behaviors by safely exercising the image in a sandbox machine. It also exposes risks and identifies suspicious dependencies buried deep in your software supply chain that would otherwise be missed by static analysis for vulnerabilities and compliance issues.

Running the analysis is supported for Linux images on Docker container runtime.

## Setup the sandbox machine[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/image-analysis-sandbox\#setup-the-sandbox-machine)

In order to run a sandbox analysis for an image, you first need to set up a dedicated sandbox virtual machine.

**Prerequisites**:

- Install [twistcli tool](https://docs.prismacloud.io/admin-guide/tools/twistcli) on your machine.

- You need `sudo` permission to run the `twistcli` command.

- The sandbox machine should have connectivity to Prisma Cloud Compute Console.

- The machine must be a Linux VM.

- Install Docker on the machine.


When setting up the VM, follow the guidelines below to make sure potential malware doesn’t exploit your sandbox:

- Make sure that the kernel is up to date.

- Make sure that Docker and Runc are up to date.

- Make sure all the software components on the machine are up to date (to make sure there is no other vulnerable component on the machine).

- The VM should be as isolated as possible. Run the VM in a dedicated network, separate from production. If other services run alongside the sandbox VM in the same local network, set up firewall rules to ensure the sandbox VM cannot reach them.

- If the VM runs in the cloud, it shouldn’t run with any service account.


It is recommended to avoid running a Defender on the same machine used as the sandbox VM. Running a Defender on this machine might cause the image that is being analyzed in the sandbox to also be presented under **Monitor > Vulnerabilities/Compliance > Images > Deployed images** as an image running in the environment.

## Running the _sandbox_ command[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/image-analysis-sandbox\#running-the-sandbox-command)

### Description[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/image-analysis-sandbox\#description)

Triggering a sandbox analysis is done by executing the `twistcli sandbox` command on an image. After the command is triggered, Prisma Cloud’s sandbox mechanism runs the container, and starts tracing its behavior. The events occurring on the running container are collected and are later analyzed to discover suspicious behaviors.

### Synopsis[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/image-analysis-sandbox\#synopsis)

The usage of the `twistcli sandbox` command is very similar to running a container image using docker:

AskCopy

```
$ sudo twistcli sandbox [OPTIONS] IMAGE [COMMAND] [ARG...]
```

For example:

AskCopy

```
$ sudo twistcli sandbox --address https://<console-address>:8083 --token 'your-api-token' --analysis-duration 2m -v "$PWD":/app python:3 python3 /app/server.py
```

To specify an image to scan, use either the image ID, or repository name and tag. The image should be present on the sandbox machine, having either been built or pulled there. If a repository is specified without a tag, `twistcli` looks for an image tagged `latest`.

The entrypoint and arguments should be specified after the image. If an entrypoint isn’t specified, the default entrypoint of the image will be used.

### Options[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/image-analysis-sandbox\#options)

`--output-file``FILENAME`
Write the results of the analysis to a file in JSON format.

Example: `--output-file analysis-results.json`

`--analysis-duration``DURATION`
The duration of the analysis in a [Go duration string format](https://golang.org/pkg/time/#ParseDuration). The default duration is 1 minute.

Adjust the duration according to your image. A longer duration may allow detection of more behaviors. An analysis duration that is too short might cause missing some of the suspicious findings that could have been detected on the container.

Example: `--analysis-duration 2m30s`

The analysis duration can be shorter than the duration you specified, if the container exits before the analysis time ends.

When WildFire integration is enabled, the analysis duration can be longer than specified, since the communication with WildFire may take longer than the analysis duration. When the specified duration is met, Prisma Cloud stops the container, so no more events are collected, but is waiting for WildFire verdict to publish the results.

`-e`, `--env``ENVIRONMENT VAR`
A key=value pair to define an environment variable in the running container. Repeat flag for each environment variable.

Example: `-e "GOROOT=/usr/local/go" -e "HTTPS_PORT=4443"`

`-v`, `--volume``VOLUME`
A src:dst pair to mount a volume to the running container. Repeat flag for each mount.

Example: `-v "/home/developer/app:/app" -v "/var/lib/mongo:/data"`

Any volume that is shared with the sandbox will be accessible to potential malware that exists on the container. Therefore, carefully consider the usage of volumes.

`-w`, `--workdir``DIRECTORY`
Working directory inside the container.

Example: `-w "/usr/src/myapp"`

`--port``PORT`
A host\_port:container\_port\[/tcp\|udp\] pair to bind a host port the running container’s port. Repeat for each port. Port ranges are not supported.

Example: `--port "80:123/tcp"`

`--third-party-cmd``value`
Specify the third-party script/binary and its arguments

Example: `--third-party-cmd /opt/sandbox/openscap_analysis.sh`

`--third-party-delay``value`
Specify the required time to wait from the container start time (to ensure initialization completion) before executing the third-party command (Optional) (default: "0")

Example: `--third-party-delay 5s`

`--third-party-output``value`
Specify the third party script/binary output path

Example: `--third-party-output /opt/sandbox/oscap-results.txt`

`--tlscacert``PATH`
Path to Prisma Cloud CA certificate file. If no CA certificate is specified, the connection to Console is insecure.

`--token``TOKEN`
Token to use for Prisma Cloud Console authentication. Tokens can be retrieved from the API endpoint `api/v1/authenticate` or from the **Manage > System > Utilities** page in Console.

`--exit-on-error``TRUE/FALSE`
Immediately exit the analysis if an error is encountered.

`-h`, `--help`
Show help

### Return value[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/image-analysis-sandbox\#return-value)

The exit code is 0 if the sandbox analysis verdict is "Passed". If the verdict is "Failed", the exit code is 1.

The criteria for passing or failing the sandbox analysis is determined by the severity of the suspicious findings detected during the analysis. The analysis verdict is "Failed" when there is at least one finding with Critical or High severity. Otherwise, the verdict is "Passed".

Another reason why `twistcli sandbox` might return an exit code of 1 is if the analysis failed due to an error.

## Sandbox analysis results[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/image-analysis-sandbox\#sandbox-analysis-results)

After `twistcli` dynamically analyzes the image, `twistcli`:

- Exits with a return value.

- Outputs a summary of the results, including a verdict.

- Outputs a link to the results report in the Console UI.


The results report in the Console UI includes the analysis summary and verdict, a list of suspicious detections found on the image, and the entire container behavior events that occurred during container runtime.

![image sandbox main page](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-bf1d3e721a05dee8692a7becca05f5cddefc0baa%252Fimage_sandbox_main_page.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=3dbf7decc9a05f3cdb37b23ebeb9b842&sv=3)

![image sandbox results a](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-7d72b0dd8e13fa75d13647bf976df32ab0d0d8d8%252Fimage_sandbox_results_a.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=a1a38477cca940ebdbb88ccf71a6f4d2&sv=3)

![image sandbox results b](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-0d928b099733f4ade4f39a94b1f98853de1a7333%252Fimage_sandbox_results_b.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=3b98c4efc0df0c9c2f3b3f6c45d71ece&sv=3)

### Analysis summary[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/image-analysis-sandbox\#analysis-summary)

The analysis summary contains the following main parts:

- Verdict - whether the image passed or failed the analysis.











The criteria for passing or failing the sandbox analysis is determined by the severity of the suspicious findings detected during the analysis. The analysis verdict is "Failed" when there is at least one finding with Critical or High severity. Otherwise, the verdict is "Passed".

- Highest severity - the severity of the most severe suspicious finding.

- Suspicious findings count - the number of suspicious findings detected.

- Analysis metadata - analysis time, duration, and the container entrypoint.

- Image details - the details of the analyzed image.











The image details also include an indication of an additional scan that may have been performed on the image. If the image was scanned for vulnerabilities and compliance as a part of the CI process, registry scanning, or as a deployed image, it will be displayed in the **Additional scan** field. You will also be able to click on its value to see the scan results. Only the furthest stage is reported in the following order: CI → Registry → Deployed.


### Suspicious findings[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/image-analysis-sandbox\#suspicious-findings)

The sandbox analysis mechanism detects the following suspicious behaviors:

Detection

Description

Severity

Malware

Malware detected by WildFire.

Detecting malware using WildFire requires the [WildFire integration](https://docs.prismacloud.io/admin-guide/configure/wildfire) to be enabled. Go to **Manage > System > WildFire** and turn on the "Enable runtime protection" toggle. You can also choose to upload files with unknown verdicts to WildFire using the matching toggle.

Critical

Crypto miners

Crypto miner was detected.

Critical

Suspicious ELF headers

ELF file with a suspicious header was detected. The binary is either incompatible with the system architecture or the ELF header was manipulated to hinder analysis. For ELF header tampering, Prisma Cloud identifies overlapping headers, deleted headers, and improperly specified section sizes as suspicious.

High

Vertical port scanning

Vertical port scanner was detected.

High

Kernel module modification

Kernel module was being loaded or unloaded.

High

Dropper

A binary that wasn’t included in the original image (dropped on disk) was executed.

High

Modified binary

A process modified a binary.

High

Modified binary execution

Execution of a binary that was included in the original image but has been modified.

High

Fileless Execution

Execution from a memory file descriptor was detected.

High

Fileless executable creation

An executable was written into a memory file descriptor.

High

Executable creation

A new executable file created on the disk.

Medium

### Container behavior[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/image-analysis-sandbox\#container-behavior)

The sandbox analysis mechanism collects Processes, Networking, and Filesystem events that occurred while the container was running in the sandbox. The events are displayed in the Console UI analysis report, in order to provide you with an overview of the container behavior at runtime.

There are two display modes for viewing the container behavior events:

- By Type - the events are aggregated by the main event properties, to give you an overview of which process run on the container, what were the network destinations it was trying to reach, what are its listening ports, etc. For example, if a process was running three times, only a single row will appear for this process, with the common properties only (MD5), and without the properties that are changing between events (command, parent process, etc).

- By Time - all the events are presented ordered by the time they occurred. For example, if a process was running three times, three rows with the same process will appear, with different time, and with all the event details for each one of them (command, parent process, etc).


#### Filesystem events[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/image-analysis-sandbox\#filesystem-events)

For container filesystem, Prisma Cloud collects Open, Create, and Modify file events.

#### Network events[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/image-analysis-sandbox\#network-events)

There are three event types collected for container networking:

- Listening port

- Outbound connection

- DNS query


All three types are presented together under the **Networking** tab, but each has its own properties.

Outbound connection events are also displayed on a world map according to the country matching their IP. Clicking on a connection event will mark it on the map. Hovering a country on the map will show you how many connections were detected for this country.

![image sandbox networking](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-dd6a2e991dd0c654182c441f3514272df04b1687%252Fimage_sandbox_networking.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=5a496f7bf7a65163db07939802255d0a&sv=3)

### View sandbox results on image details[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/image-analysis-sandbox\#view-sandbox-results-on-image-details)

When reviewing image details, you can look at its latest sandbox analysis results in a dedicated section. The **Anaysis sandbox** section contains an analysis summary, including the verdict and the suspicious findings counts by type. Click on the link at the top to move to the full report page.

![image sandbox dialog](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-cdd401a8408bc4cd39e5ecc64dff54155fd04e93%252Fimage_sandbox_dialog.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=d5c5d21d330cb1d359f8d810764dcf50&sv=3)

## Actions[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/image-analysis-sandbox\#actions)

### Add to trust group[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/image-analysis-sandbox\#add-to-trust-group)

After reviewing the analysis results of an image, you can decide whether you trust this image to run in your development and production environments. Optionally, you can add the image repository to a single or multiple trust groups using the **Add to trust group** action. This way it is possible for you to get notified or block images that are not trusted. See [Trusted Images](https://docs.prismacloud.io/admin-guide/compliance/trusted-images) to learn more.

### Export to JSON file[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/image-analysis-sandbox\#export-to-json-file)

To export the analysis results, use the **Export to JSON** action at the top of the page. This action will download a file in a JSON format with the analysis results for the image.

[PreviousDetailed Aggregation Event Types](https://docs.prismacloud.io/admin-guide/runtime-defense/event-aggregation-event-types-table) [NextIncident Explorer](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-explorer)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject

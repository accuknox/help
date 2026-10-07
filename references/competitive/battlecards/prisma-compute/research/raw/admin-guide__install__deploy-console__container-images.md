For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/install/deploy-console/container-images.md).

You can deploy the Prisma Cloud console as a container using your active subscription or your valid license key to get the images from a cloud registry. The Prisma Cloud images are built using the [RedHat Universal Base Image 8 Minimal](https://catalog.redhat.com/software/containers/ubi8/ubi-minimal/5c359a62bed8bd75a2c3fba8?gti-tabs=unauthenticated) (UBI8-minimal). This format is designed for applications that contain their own dependencies.

All builds, including private builds, are published to the registry. Private builds temporarily address specific customer issues. Unless you’ve been asked to use a private build by a Prisma Cloud representative during the course of a support case, you should only pull officially published builds.

You can optionally manage Prisma Cloud images in your own registry. You can push the Prisma Cloud images to your own private registry, and manage them from there as you see fit. The Prisma Cloud console image is delivered as a _.tar.gz_ file in the release tarball. Go to **Manage > System > Utilities** in the Prisma Cloud Console to download the Defender image.

The length of time that images are available on the cloud registry complies with our standard [n-1 support lifecycle](https://docs.prismacloud.io/admin-guide/welcome/support-lifecycle).

There are two different methods for accessing images in the cloud registry:

- Basic authorization.

- URL authorization.


## Get the Prisma Cloud Console Images with Basic Authorization[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-console/container-images\#get-the-prisma-cloud-console-images-with-basic-authorization)

Authenticate using _docker login_ or _podman login_, then retrieve the Prisma Cloud images using _docker pull_ or _podman pull_. For basic authorization, the registry is accessible at _registry.twistlock.com_.

Image names contain a version string. The version string is formatted as X\_Y\_Z, where X is the major version, Y is the minor version, and Z is the patch number. For example, 19.07.363 is formatted as 19\_07\_363. For example:

registry.twistlock.com/twistlock/defender:defender\_19\_07\_363.

**Prerequisites:**

- You have your Prisma Cloud access token.


1. Authenticate with the registry.

















AskCopy



```
$ docker (or podman) login registry.twistlock.com
Username:
Password:
```









Where **Username** can be any string, and **Password** must be your access token.

2. Pull the Prisma Cloud console image from the Prisma Cloud registry.

















AskCopy



```
$ docker (or podman) pull registry.twistlock.com/twistlock/console:console_<VERSION>
```

3. Pull the Defender image from the Prisma Cloud registry.

















AskCopy



```
$ docker (or podman) pull registry.twistlock.com/twistlock/defender:defender_<VERSION>
```


## Get the Prisma Cloud Console Images with URL Authorization[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-console/container-images\#get-the-prisma-cloud-console-images-with-url-authorization)

Retrieve Prisma Cloud images with a single command by embedding your access token into the registry URL. For URL authorization, the registry is accessible at _registry-auth.twistlock.com_.

By embedding your access token into the registry URL, you only need to run _docker pull_ or _podman pull_. The _docker login_ or _podman login_ command isn’t required.

The format for the registry URL is: `registry-auth.twistlock.com/tw_<ACCESS-TOKEN>/<IMAGE>:<TAG>`

Image names contain a version string. The version string must be formatted as X\_Y\_Z, where X is the major version, Y is the minor version, and Z is the patch number. For example, 19.07.363 should be formatted as 19\_07\_363. For example:

registry.twistlock.com/twistlock/defender:defender\_19\_07\_363.

**Prerequisites:**

- You have a Prisma Cloud access token.

- The Docker or Podman client requires that repository names be lowercase. Therefore, all characters in your access token must be lowercase. To convert your access token to lowercase characters, use the following command:

















AskCopy



```
$ echo <ACCESS-TOKEN> | tr '[:upper:]' '[:lower:]'
```


1. Pull the Console image from the Prisma Cloud registry.

















AskCopy



```
$ docker (or podman) pull \
     registry-auth.twistlock.com/tw_<ACCESS-TOKEN>/twistlock/console:console_<VERSION>
```

2. Pull the Defender image from the Prisma Cloud registry.

















AskCopy



```
$ docker (or podman) pull \
     registry-auth.twistlock.com/tw_<ACCESS-TOKEN>/twistlock/defender:defender_<VERSION>
```


[PreviousDeploy the Prisma Cloud Console On-Prem](https://docs.prismacloud.io/admin-guide/install/deploy-console) [NextDeploy the Prisma Cloud Console on Kubernetes](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-kubernetes)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject

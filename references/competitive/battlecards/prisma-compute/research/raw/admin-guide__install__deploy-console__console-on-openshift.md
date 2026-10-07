For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-openshift.md).

Prisma Cloud Console is deployed as a Deployment, which ensures it’s always running. The Prisma Cloud Console and Defender container images can be stored either in the internal OpenShift registry or your own Docker v2 compliant registry. Alternatively, you can configure your deployments to pull images from [Prisma Cloud’s cloud registry](https://docs.prismacloud.io/admin-guide/install/deploy-console/container-images).

## Preflight checklist[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-openshift\#preflight-checklist)

To ensure that your installation on supported versions of OpenShift v4.x goes smoothly, work through the following checklist and validate that all requirements are met.

### Minimum system requirements[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-openshift\#minimum-system-requirements)

Validate that the components in your environment (nodes, host operating systems, orchestrator) meet the specs in [System requirements](https://docs.prismacloud.io/admin-guide/install/system-requirements).

For OpenShift installs, we recommend using the overlay or overlay2 storage drivers due to a known issue in RHEL. For more information, see [https://bugzilla.redhat.com/show\_bug.cgi?id=1518519](https://bugzilla.redhat.com/show_bug.cgi?id=1518519).

### Permissions[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-openshift\#permissions)

Validate that you have permission to:

- Push to a private docker registry. For most OpenShift setups, the registry runs inside the cluster as a service. You must be able to authenticate with your registry with docker login.

- Pull images from your registry. This might require the creation of a docker-registry secret.

- Have the correct role bindings to pull and push to the registry. For more information, see [Accessing the Registry](https://docs.openshift.com/container-platform/3.10/install_config/registry/accessing_registry.html).

- Create and delete projects in your cluster. For OpenShift installations, a project is created when you run _oc new-project_.

- Run _oc create_ commands.


### Internal cluster network communication[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-openshift\#internal-cluster-network-communication)

TCP: 8083, 8084

### External cluster network communication[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-openshift\#external-cluster-network-communication)

TCP: 443

The Prisma Cloud Console connects to the Prisma Cloud Intelligence Stream ([https://intelligence.twistlock.com](https://intelligence.twistlock.com/)) on TCP port 443 for vulnerability updates. If your Console is unable to contact the Prisma Cloud Intelligence Stream, follow the guidance for [offline environments](https://docs.prismacloud.io/admin-guide/tools/update-intel-stream-offline).

### Download the Prisma Cloud software[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-openshift\#download-the-prisma-cloud-software)

Download the latest Prisma Cloud release to any system where the OpenShift [oc client](https://www.okd.io/download.html) is installed.

1. Go to [Releases](https://docs.prismacloud.io/admin-guide/welcome/releases), and copy the link to current recommended release.

2. Download the release tarball to your cluster controller.

















AskCopy



```
$ wget <LINK_TO_CURRENT_RECOMMENDED_RELEASE_LINK>
```

3. Unpack the release tarball.

















AskCopy



```
$ mkdir twistlock
$ tar xvzf twistlock_<VERSION>.tar.gz -C twistlock/
```

4. Use [_twistcli_](https://docs.prismacloud.io/admin-guide/tools/twistcli) to install the Prisma Cloud Console and Defenders. The _twistcli_ utility is included with every release. After completing this procedure, both Prisma Cloud Console and Prisma Cloud Defenders will be running in your OpenShift cluster.


### Create an OpenShift project for Prisma Cloud[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-openshift\#create-an-openshift-project-for-prisma-cloud)

Create a project named _twistlock_.

1. Login to the OpenShift cluster and create the _twistlock_ project:


AskCopy

```
  $ oc new-project twistlock
```

### (Optional) Push the Prisma Cloud images to a private registry[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-openshift\#optional-push-the-prisma-cloud-images-to-a-private-registry)

When Prisma Cloud is deployed to your cluster, the images are retrieved from a registry. You have a number of options for storing the Prisma Cloud Console and Defender images:

- OpenShift internal registry.

- Private Docker v2 registry. You must create a docker-secret to authenticate with the registry.


Alternatively, you can pull the images from the [Prisma Cloud cloud registry](https://docs.prismacloud.io/admin-guide/install/deploy-console/container-images) at deployment time. Your cluster nodes must be able to connect to the Prisma Cloud cloud registry (registry-auth.twistlock.com) with TLS on TCP port 443.

This guides shows you how to use both the OpenShift internal registry and the Prisma Cloud cloud registry. If you’re going to use the Prisma Cloud cloud registry, you can skip this section. Otherwise, this procedure shows you how to pull, tag, and upload the Prisma Cloud images to the OpenShift internal registry’s _twistlock_ imageStream.

1. Determine the endpoint for your OpenShift internal registry. Use either the internal registry’s service name or cluster IP.

















AskCopy



```
$ oc get svc -n default
NAME               TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)       AGE
docker-registry    ClusterIP   172.30.163.181   <none>        5000/TCP      88d
```

2. Pull the images from the Prisma Cloud cloud registry using your access token. The major, minor, and patch numerals in the <VERSION> string are separated with an underscore. For example, 18.11.128 would be 18\_11\_128.

















AskCopy



```
     $ docker pull \
       registry-auth.twistlock.com/tw_<ACCESS_TOKEN>/twistlock/defender:defender_<VERSION>

     $ docker pull \
       registry-auth.twistlock.com/tw_<ACCESS_TOKEN>/twistlock/console:console_<VERSION>
```

3. Tag the images for the OpenShift internal registry.

















AskCopy



```
$ docker tag \
     registry-auth.twistlock.com/tw_<ACCESS_TOKEN>/twistlock/defender:defender_<VERSION> \
     172.30.163.181:5000/twistlock/private:defender_<VERSION>

$ docker tag \
     registry-auth.twistlock.com/tw_<ACCESS_TOKEN>/twistlock/console:console_<VERSION> \
     172.30.163.181:5000/twistlock/private:console_<VERSION>
```

4. Push the images to the _twistlock_ project’s imageStream.

















AskCopy



```
     $ docker push 172.30.163.181:5000/twistlock/private:defender_<VERSION>
     $ docker push 172.30.163.181:5000/twistlock/private:console_<VERSION>
```


### Install Console[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-openshift\#install-console)

Use the _twistcli_ tool to generate YAML files or a Helm chart for Prisma Cloud Compute Console. The _twistcli_ tool is bundled with the release tarball. There are versions for Linux, macOS, and Windows.

The _twistcli_ tool generates YAML files or helm charts for a Deployment and other service configurations, such as a PersistentVolumeClaim, SecurityContextConstraints, and so on. Run the twistcli command with the _--help_ flag for additional details about the command and supported flags.

You can optionally customize _twistlock.cfg_ to enable additional features. Then run twistcli from the root of the extracted release tarball.

Prisma Cloud Console uses a PersistentVolumeClaim to store data. There are two ways to provision storage for Console:

- **Dynamic provisioning:** Allocate storage for Console [on-demand](https://docs.openshift.com/container-platform/3.10/install_config/persistent_storage/dynamically_provisioning_pvs.html) at deployment time. When generating the Console deployment YAML files or helm chart with _twistcli_, specify the name of the storage class with the _--storage-class_ flag. Most customers use dynamic provisioning.

- **Manual provisioning:** Pre-provision a persistent volume for Console, then specify its label when generating the Console deployment YAML files. OpenShift uses NFS mounts for the backend infrastructure components (e.g. registry, logging, etc.). The NFS server is typically one of the master nodes. Guidance for creating an NFS backed PersistentVolume can be found [here](https://docs.openshift.com/container-platform/3.10/install_config/persistent_storage/persistent_storage_nfs.html#overview). Also see [Appendix: NFS PersistentVolume example](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-openshift#_appendix_nfs_persistentvolume_example).


#### Option \#1: Deploy with YAML files[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-openshift\#option-1-deploy-with-yaml-files)

Deploy Prisma Cloud Compute Console with YAML files.

1. Generate a deployment YAML file for Console. A number of command variations are provided. Use them as a basis for constructing your own working command.









1. Prisma Cloud Console + dynamically provisioned PersistentVolume + image pulled from the OpenShift internal registry.\*

















      AskCopy



      ```
        $ <PLATFORM>/twistcli console export openshift \
          --storage-class "<STORAGE-CLASS-NAME>" \
          --image-name "172.30.163.181:5000/twistlock/private:console_<VERSION>" \
          --service-type "ClusterIP"
      ```

2. **Prisma Cloud Console + manually provisioned PersistentVolume + image pulled from the OpenShift internal registry.** Using the NFS backed PersistentVolume described in [Appendix: NFS PersistentVolume example](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-openshift#_appendix_nfs_persistentvolume_example), pass the label to the _--persistent-volume-labels_ flag to specify the PersistentVolume to which the PersistentVolumeClaim will bind.

















      AskCopy



      ```
        $ <PLATFORM>/twistcli console export openshift \
          --persistent-volume-labels "app-volume=twistlock-console" \
          --image-name "172.30.163.181:5000/twistlock/private:console_<VERSION>" \
          --service-type "ClusterIP"
      ```

3. **Prisma Cloud Console + manually provisioned PersistentVolume + image pulled from the Prisma Cloud cloud registry.** If you omit the _--image-name_ flag, the Prisma Cloud cloud registry is used by default, and you are prompted for your access token.

















      AskCopy



      ```
        $ <PLATFORM>/twistcli console export openshift \
          --persistent-volume-labels "app-volume=twistlock-console" \
          --service-type "ClusterIP"
      ```


2. Deploy Console.

















AskCopy



```
     $ oc create -f ./twistlock_console.yaml
```









You can safely ignore the error that says the twistlock project already exists.


#### Option \#2: Deploy with Helm chart[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-openshift\#option-2-deploy-with-helm-chart)

Deploy Prisma Cloud Compute Console with a Helm chart.

Prisma Cloud Console Helm charts fail to install on OpenShift 4 clusters due to a Helm bug. If you generate a Helm chart, and try to install it in an OpenShift 4 cluster, you’ll get the following error:

AskCopy

```
  Error: unable to recognize "": no matches for kind "SecurityContextConstraints" in version "v1"
```

To work around the issue, you’ll need to manually modify the generated Helm chart.

1. Generate a deployment helm chart for Console. A number of command variations are provided. Use them as a basis for constructing your own working command.









1. **Prisma Cloud Console + dynamically provisioned PersistentVolume + image pulled from the OpenShift internal registry.**

















      AskCopy



      ```
        $ <PLATFORM>/twistcli console export openshift \
          --storage-class "<STORAGE-CLASS-NAME>" \
          --image-name "172.30.163.181:5000/twistlock/private:console_<VERSION>" \
          --service-type "ClusterIP" \
          --helm
      ```

2. **Prisma Cloud Console + manually provisioned PersistentVolume + image pulled from the OpenShift internal registry.** Using the NFS backed PersistentVolume described in [Appendix: NFS PersistentVolume example](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-openshift#_appendix_nfs_persistentvolume_example), pass the label to the _--persistent-volume-labels_ flag to specify the PersistentVolume to which the PersistentVolumeClaim will bind.

















      AskCopy



      ```
        $ <PLATFORM>/twistcli console export openshift \
          --persistent-volume-labels "app-volume=twistlock-console" \
          --image-name "172.30.163.181:5000/twistlock/private:console_<VERSION>" \
          --service-type "ClusterIP" \
          --helm
      ```

3. **Prisma Cloud Console + manually provisioned PersistentVolume + image pulled from the Prisma Cloud cloud registry.** If you omit the _--image-name_ flag, the Prisma Cloud cloud registry is used by default, and you are prompted for your access token.

















      AskCopy



      ```
        $ <PLATFORM>/twistcli console export openshift \
          --persistent-volume-labels "app-volume=twistlock-console" \
          --service-type "ClusterIP" \
          --helm
      ```


2. Unpack the chart into a temporary directory.

















AskCopy



```
     $ mkdir helm-console
     $ tar xvzf twistlock-console-helm.tar.gz -C helm-console/
```

3. Open _helm-console/twistlock-console/templates/securitycontextconstraints.yaml_ for editing.

4. Change `apiVersion` from `v1` to `security.openshift.io/v1`.

















AskCopy



```
{{- if .Values.openshift }}
apiVersion: security.openshift.io/v1
kind: SecurityContextConstraints
metadata:
     name: twistlock-console
...
```

5. Repack the Helm chart

















AskCopy



```
     $ cd helm-console/
     $ tar cvzf twistlock-console-helm.tar.gz twistlock-console/
```

6. Install the updated Helm chart.

















AskCopy



```
     $ helm install --namespace=twistlock -g twistlock-console-helm.tar.gz
```


### Create an external route to Console[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-openshift\#create-an-external-route-to-console)

Create an external route to Console so that you can access the web UI and API.

01. From the OpenShift web interface, go to the _twistlock_ project.

02. Go to **Application > Routes**.

03. Select **Create Route**.

04. Enter a name for the route, such as **twistlock-console**.

05. Hostname = URL used to access the Console, e.g. _twistlock-console.apps.ose.example.com_

06. Path = **/**

07. Service = **twistlock-console**

08. Target Port = 8083 → 8083

09. Select the **Security > Secure Route** radio button.

10. TLS Termination = Passthrough (if using 8083)











    If you plan to issue a [custom certificate for Console TLS communication](https://docs.prismacloud.io/admin-guide/configure/certificates) that is trusted and will allow the TLS establishment with the Prisma Cloud Console, then Select Passthrough TLS for TCP port 8083.

11. Insecure Traffic = **Redirect**

12. Click **Create**.


### Create an external route to Console for external Defenders[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-openshift\#create-an-external-route-to-console-for-external-defenders)

If you are planning to deploy Defenders to another cluster and report to this Console, you will need to create an additional external route to Console so that the Defenders can access the Console. You need to expose the Prisma Cloud-Console service’s TCP port 8084 as external OpenShift routes. Each route will be an unique, fully qualified domain name.

01. From the OpenShift web interface, go to the _twistlock_ project.

02. Go to **Application > Routes**.

03. Select **Create Route**.

04. Enter a name for the route, such as **twistlock-console-8084**.

05. Hostname = URL used to access the Console, using a different hostname, e.g. _twistlock-console-8084.apps.ose.example.com_

06. Path = **/**

07. Service = **twistlock-console**

08. Target Port = 8084 → 8084

09. Select the **Security > Secure Route** radio button.

10. TLS Termination = Passthrough (if using 8084)











    The Defender to Console communication is a mutual TLS secure websocket session. This communication cannot be intercepted.

11. Insecure Traffic = **Redirect**

12. Click **Create**.


### Configure Console[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-openshift\#configure-console)

Create your first admin user, enter your license key, and configure Console’s certificate so that Defenders can establish a secure connection to it.

1. In a web browser, navigate to the external route you configured for Console, e.g. _https://twistlock-console.apps.ose.example.com_.

2. Create your first admin account.

3. Enter your license key.

4. Add a SubjectAlternativeName to Console’s certificate to allow Defenders to establish a secure connection with Console.











Use either Console’s service name, _twistlock-console_ or _twistlock-console.twistlock.svc_, or Console’s cluster IP.











Additionally, if a route for external Defenders was created, add that one to the SAN list too: _twistlock-console-8084.apps.ose.example.com_

















AskCopy



```
     $ oc get svc -n twistlock
     NAME                TYPE           CLUSTER-IP     EXTERNAL-IP                 PORT(S)
     twistlock-console   LoadBalancer   172.30.41.62   172.29.61.32,172.29.61.32   8084:3184...
```







1. Go to **Manage > Defenders > Names**.

2. Click **Add SAN** and enter Console’s service name.

3. Click **Add SAN** and enter Console’s cluster IP.















      ![install openshift san](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-82b0770fceaef115b3539b6ff50a43f0d09e935b%252Finstall_openshift_san.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=5b9c06b63cf66c86b9de8151afbb95d7&sv=3)


## Appendix: NFS PersistentVolume example[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-openshift\#appendix-nfs-persistentvolume-example)

Create an NFS mount for the Prisma Cloud Console’s PV on the host that serves the NFS mounts.

01. **mkdir /opt/twistlock\_console**

02. Check selinux: **sestatus**

03. **chcon -R -t svirt\_sandbox\_file\_t -l s0 /opt/twistlock\_console**

04. **sudo chown nfsnobody /opt/twistlock\_console**

05. **sudo chgrp nfsnobody /opt/twistlock\_console**

06. Check perms with: **ls -lZ /opt/twistlock\_console** (drwxr-xr-x. nfsnobody nfsnobody system\_u:object\_r:svirt\_sandbox\_file\_t:s0)

07. Create **/etc/exports.d/twistlock.exports**

08. In the **/etc/exports.d/twistlock.exports** add in line **/opt/twistlock\_console \*(rw,root\_squash)**

09. Restart nfs mount **sudo exportfs -ra**

10. Confirm with **showmount -e**

11. Get the IP address of the Master node that will be used in the PV (eth0, openshift uses 172. for node to node communication). Make sure TCP 2049 (NFS) is allowed between nodes.

12. Create a PersistentVolume for Prisma Cloud Console.











    The following example uses a label for the PersistentVolume and the [volume and claim pre-binding](https://docs.openshift.com/container-platform/3.10/dev_guide/persistent_volumes.html#persistent-volumes-volumes-and-claim-prebinding) features. The PersistentVolumeClaim uses the `app-volume: twistlock-console` label to bind to the PV. The volume and claim pre-binding `claimref` ensures that the PersistentVolume is not claimed by another PersistentVolumeClaim before Prisma Cloud Console is deployed.

















    AskCopy



    ```
    apiVersion: v1
    kind: PersistentVolume
    metadata:
     name: twistlock
     labels:
      app-volume: twistlock-console
    storageClassName: standard
    spec:
      capacity:
       storage: 100Gi
      accessModes:
  - ReadWriteOnce
nfs:
path: /opt/twistlock_console
server: 172.31.4.59
persistentVolumeReclaimPolicy: Retain
claimRef:
name: twistlock-console
namespace: twistlock
```

## Appendix: Implementing SAML federation with a Prisma Cloud Console inside an OpenShift cluster[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-openshift\#appendix-implementing-saml-federation-with-a-prisma-cloud-console-inside-an-openshift-cluster)

When federating Prisma Cloud Console that is accessed through an OpenShift external route with a SAML v2.0 Identity Provider (IdP), the SAML authentication request’s _AssertionConsumerServiceURL_ value must be modified. Prisma Cloud automatically generates the _AssertionConsumerServiceURL_ value sent in a SAML authentication request based on Console’s configuration. When Console is accessed through an OpenShift external route, the URL for Console’s API endpoint is most likely not the same as the automatically generated _AssertionConsumerServiceURL._ Therefore, you must configure the _AssertionConsumerServiceURL_ value that Prisma Cloud sends in the SAML authentication request.

1. Log into Prisma Cloud Console.

2. Go to **Manage > Authentication > SAML**.

3. In **Console URL**, define the _AssertionConsumerServiceURL_.











   In this example, enter _https://twistlock-console.apps.ose.example.com_


[PreviousDeploy the Prisma Cloud Console on IKS](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-iks) [NextDeploy the Prisma Cloud Defender](https://docs.prismacloud.io/admin-guide/install/deploy-defender)

Last updated 2 months ago

Was this helpful?

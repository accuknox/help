For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/openshift.md).

Prisma Cloud Defenders are deployed as a DaemonSet, which ensures that an instance of Defender runs on every node in the cluster. You can run Defenders on OpenShift master and infrastructure nodes by removing the taint from them.

The Prisma Cloud Defender container images can be stored either in the internal OpenShift registry or your own Docker v2 compliant registry. This guide shows you how to generate deployment YAML files for Defenders, and then deploy them to your OpenShift cluster with the _oc_ client.

To better understand clusters, read our [cluster context](https://docs.prismacloud.io/admin-guide/install/cluster-context) topic.

## Preflight checklist[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/openshift\#preflight-checklist)

To ensure that your installation on supported versions of OpenShift v4.x goes smoothly, work through the following checklist and validate that all requirements are met.

### Minimum system requirements[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/openshift\#minimum-system-requirements)

Validate that the components in your environment (nodes, host operating systems, orchestrator) meet the specs in [System requirements](https://docs.prismacloud.io/admin-guide/install/system-requirements).

### Permissions[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/openshift\#permissions)

Validate that you have permission to:

- Push to a private docker registry. For most OpenShift setups, the registry runs inside the cluster as a service. You must be able to authenticate with your registry with docker login.

- Pull images from your registry. This might require the creation of a docker-registry secret.

- Have the correct role bindings to pull and push to the registry. For more information, see [Accessing the Registry](https://docs.openshift.com/container-platform/3.10/install_config/registry/accessing_registry.html).

- Create and delete projects in your cluster. For OpenShift installations, a project is created when you run _oc new-project_.

- Run _oc create_ commands.


### Network connectivity[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/openshift\#network-connectivity)

Validate that outbound connections to your Console can be made on port 443.

Use [_twistcli_](https://docs.prismacloud.io/admin-guide/tools/twistcli) to install the Prisma Cloud Defenders in your OpenShift cluster. The _twistcli_ utility is included with every release.

### Create an OpenShift project for Prisma Cloud[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/openshift\#create-an-openshift-project-for-prisma-cloud)

Create a project named _twistlock_.

1. Login to the OpenShift cluster and create the _twistlock_ project:

















AskCopy



```
     $ oc new-project twistlock
```


### (Optional) Push the Prisma Cloud images to a private registry[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/openshift\#optional-push-the-prisma-cloud-images-to-a-private-registry)

When Prisma Cloud is deployed to your cluster, the images are retrieved from a registry. You have a number of options for storing the Prisma Cloud Console and Defender images:

- OpenShift internal registry.

- Private Docker v2 registry. You must create a docker-secret to authenticate with the registry.


Your cluster nodes must be able to connect to the Prisma Cloud cloud registry (registry-auth.twistlock.com) with TLS on TCP port 443.

This guides shows you how to use both the OpenShift internal registry and the Prisma Cloud cloud registry. If you’re going to use the Prisma Cloud cloud registry, you can skip this section. Otherwise, this procedure shows you how to pull, tag, and upload the Prisma Cloud images to the OpenShift internal registry’s _twistlock_ imageStream.

1. Determine the endpoint for your OpenShift internal registry. Use either the internal registry’s service name or cluster IP.

















AskCopy



```
     $ oc get svc -n default
     NAME               TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)       AGE
     docker-registry    ClusterIP   172.30.163.181   <none>        5000/TCP      88d
```

2. Pull the image from the Prisma Cloud cloud registry using your access token. The major, minor, and patch numerals in the <VERSION> string are separated with an underscore. For exampe, 18.11.128 would be 18\_11\_128.

















AskCopy



```
     $ docker pull \
       registry-auth.twistlock.com/tw_<ACCESS_TOKEN>/twistlock/defender:defender_<VERSION>
```

3. Tag the image for the OpenShift internal registry.

















AskCopy



```
     $ docker tag \
       registry-auth.twistlock.com/tw_<ACCESS_TOKEN>/twistlock/defender:defender_<VERSION> \
       172.30.163.181:5000/twistlock/private:defender_<VERSION>
```

4. Push the image to the _twistlock_ project’s imageStream.

















AskCopy



```
     $ docker push 172.30.163.181:5000/twistlock/private:defender_<VERSION>
```


## Control Defender deployments with taint[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/openshift\#control-defender-deployments-with-taint)

You can deploy Defenders to all nodes in an OpenShift cluster (master, infra, compute). OpenShift Container Platform automatically taints infra and master nodes These taints have the NoSchedule effect, which means no pod can be scheduled on them.

To run the Defenders on these nodes, you can either remove the taint or add a toleration to the Defender DaemonSet. Once this is done, the Defender Daemonset will automatically be deployed to these nodes (no need to redeploy the Daemonset). Adjust the guidance in the following procedure according to your organization’s deployment strategy.

- **Option 1 - remove taint all nodes:**

















AskCopy



```
$ oc adm taint nodes --all node-role.kubernetes.io/master-
```

- **Option 2 - remove taint from specific nodes:**

















AskCopy



```
$ oc adm taint nodes <node-name> node-role.kubernetes.io/master-
```

- **Option 3 - add tolerations to the twistlock-defender-ds DaemonSet:**

















AskCopy



```
$ oc edit ds twistlock-defender-ds -n twistlock
```









Add the following toleration in PodSpec (DaemonSet.spec.template.spec)

















AskCopy



```
tolerations:
- key: "node-role.kubernetes.io/master"
operator: "Exists"
effect: "NoSchedule"
```

## Uninstall[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/openshift\#uninstall)

[PreviousGoogle Kubernetes Engine (GKE) Autopilot](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/install-gke-autopilot) [NextDeploy Serverless Defender](https://docs.prismacloud.io/admin-guide/install/deploy-defender/serverless)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject

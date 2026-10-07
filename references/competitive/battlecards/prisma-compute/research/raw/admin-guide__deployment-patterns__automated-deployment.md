For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/deployment-patterns/automated-deployment.md).

The following is an example of Infrastructure as Code (IaC) for the automated deployment of a Console and Defenders within a Kubernetes cluster using an Ansible playbook. This requires a docker host, Prisma Cloud Compute license and kubectl administrative access to the Kubernetes cluster. The Ansible playbook must run on a host that is able to route to the Console service’s ClusterIP address to perform the required API calls to configure the Console. Use of this Ansible playbook does not imply any rights to Palo Alto Networks products and/or services.

## Requirements[Direct link to heading](https://docs.prismacloud.io/admin-guide/deployment-patterns/automated-deployment\#requirements)

This sample IaC deployment runs on a unix based host with the following requirements:

- [docker](https://docs.docker.com/engine/install/)

- [Ansible](https://www.ansible.com/)

- [Prisma Cloud Compute license](https://www.paloaltonetworks.com/prisma/cloud)

- kubectl access to Kubernetes cluster with [permissions](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-kubernetes) to deploy Prisma Cloud Compute.

- Ability to pull images from registry-auth.twistlock.com

- [K8s-Console-Defender-deployment-ansible.yaml](https://github.com/twistlock/sample-code/tree/master/automated-deployments/K8s-Console-Defender-deployment-ansible.yaml) Ansible playbook


## Process[Direct link to heading](https://docs.prismacloud.io/admin-guide/deployment-patterns/automated-deployment\#process)

![automated deployment](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-3bec5c0eaa70799211832bd8a99a8d2dcfcc24bb%252Fautomated_deployment.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=9b198a9615a2fbe54d7001f0c1d263fc&sv=3)

## Ansible playbook[Direct link to heading](https://docs.prismacloud.io/admin-guide/deployment-patterns/automated-deployment\#ansible-playbook)

Pull the Ansible playbook from [here](https://github.com/twistlock/sample-code/tree/master/automated-deployments/K8s-Console-Defender-deployment-ansible.yaml). Update the variables in the `vars:` section in [_K8s-Console-Defender-deployment-ansible.yaml._](https://github.com/twistlock/sample-code/tree/master/automated-deployments/K8s-Console-Defender-deployment-ansible.yaml)

- twistlock\_registry\_token: <license\_token>

- twistlock\_license: <license>

- twistlock\_install\_version: [<version\_to\_deploy, e.g. "21\_04\_421">](https://docs.prismacloudcompute.com/docs/releases/release-information/latest.html)

- user: <first\_admin\_username>

- password: <first\_admin\_password>

- storage\_class: <k8s\_storage\_class\_for\_dynamic\_persistent\_volume>

- namespace: <namespace>


## Execution[Direct link to heading](https://docs.prismacloud.io/admin-guide/deployment-patterns/automated-deployment\#execution)

On the unix host, sudo to root and run the command **ansible-playbook K8s-Console-Defender-deployment-ansible.yaml**

The supporting files will be written to the `/root/twistlock` directory.

## Post execution[Direct link to heading](https://docs.prismacloud.io/admin-guide/deployment-patterns/automated-deployment\#post-execution)

Once the playbook has successfully completed, establish communications to the twistlock-console service’s management-port-https port (default 8083/TCP) using a [Kubernetes LoadBalancer](https://kubernetes.io/docs/tasks/access-application-cluster/create-external-load-balancer/) or your organization’s approved cluster ingress technology.

[PreviousPerformance planning](https://docs.prismacloud.io/admin-guide/deployment-patterns/performance-planning) [NextHigh availability](https://docs.prismacloud.io/admin-guide/deployment-patterns/high-availability)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject

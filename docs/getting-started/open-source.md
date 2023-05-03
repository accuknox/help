---
hide:
  - toc
---

KubeArmor is an open-source sandbox project of AccuKnox which was donated to [CNCF-Cloud Native Computing Foundation](https://www.cncf.io/projects/kubearmor/)

To contribute to the project access the [Github page](https://github.com/kubearmor/KubeArmor)
Learn more about KubeArmor [here](https://kubearmor.io/)


![Alt](/getting-started/images/accuknox-deployment-opensource.png){: style="height:auto;width:auto"}

??? "Deploying Sample Cluster (_skip if you already have a cluster configured_)"

	=== "Local K3s cluster"

		**Install K3s**

		> Note: Recommended base OS image is Ubuntu 20.04.

		```sh
		curl -sfL https://get.k3s.io | INSTALL_K3S_EXEC='--disable traefik' sh -s - --write-kubeconfig-mode 644
		```

		**Make K3's cluster config the default**

		```sh
		mkdir -p ~/.kube && cp /etc/rancher/k3s/k3s.yaml ~/.kube/config
		```

	=== "GKE cluster"

		```yaml
		 - name: create a cluster
		   hosts: localhost
		   tasks:
		    - name: create a cluster
		      google.cloud.gcp_container_cluster:
		       name: gkecluster
		       initial_node_count: 1
		       node_config:
		         machine_type: e2-medium
		         disk_size_gb: 10
		         taints:
		          - effect: PREFER_NO_SCHEDULE
		            key: node.cilium.io/agent-not-ready
		            value: "true"
		       location: asia-east1
		       project: "{{project_id}}"
		       auth_kind: serviceaccount
		       service_account_file: "{{service_account_file}}"
		       state: present
		```

		```sh
		sudo apt-get install python3 -y
		```

		```sh
		sudo apt-get install ansible
		```
		```sh
		ansible-galaxy collection install google.cloud
		```

		```sh
		ansible-playbook kube-cluster.yaml
		```

	=== "AKS cluster"

		```yaml
		 - name: Create a managed Azure Container Services (AKS) instance
		   hosts: localhost
		   tasks:
		    - name:
		      azure_rm_aks:
		       name: myAKS
		       location: eastus
		       resource_group: myResourceGroup
		       dns_prefix: akstest
		       kubernetes_version: 1.24.3
		       linux_profile:
		        admin_username: azureuser
		        ssh_key: "{{local_ssh_key}}"
		       service_principal:
		        client_id: "{{azure_account_client_id}}"
		        client_secret: "{{azure_account_client_secret}}"
		       agent_pool_profiles:
		        - name: default
		          count: 2
		          vm_size: Standard_D2_v2
		```

		```sh
		sudo apt-get install python3 -y
		```

		```sh
		sudo apt-get install ansible
		```

		```sh
		ansible-galaxy collection install azure.azcollection
		```

		```sh
		ansible-playbook aks-cluster.yaml
		```

	=== "EKS cluster"

		```yaml
		apiVersion: eksctl.io/v1alpha5
		kind: ClusterConfig

		metadata:
          name: kubearmor-ub20
          region: us-east-2

		nodeGroups:
		  - name: ng-1
    		amiFamily: "Ubuntu2004"
    		privateNetworking: true
    		desiredCapacity: 2
    		# taint nodes so that application pods are
    		# not scheduled until Cilium is deployed.
    		taints:
     		 - key: "node.cilium.io/agent-not-ready"
       		   value: "true"
               effect: "NoSchedule"
    		ssh:
      		  allow: true
    		preBootstrapCommands:
              - "sudo apt install linux-headers-$(uname -r)"
		```

		```sh
		eksctl create cluster -f sample-ubuntu-18.04-cluster.yaml
		```

		```sh
		aws eks --region us-east-1 update-kubeconfig --name kubearmor-ub20
		```

	=== "Kubeadm"

		**Install Pre-requisites**

		+ [VirtualBox](https://www.virtualbox.org/wiki/Linux_Downloads)

		+ [Vagrant](https://www.vagrantup.com/downloads)

		+ [kubectl](https://kubernetes.io/docs/tasks/tools/#kubectl)

		+ [Helm](https://helm.sh/docs/intro/install/)

		**Download the Vagrant setup**

		+ [Click here to download](../quick_start/vagrant-k8s-ubuntu2204.tar.gz)

		Untar and goto the Vagrant setup directory, Run the below command

		```sh
		vagrant up
		```

	Ref: [KubeArmor support matrix](https://github.com/kubearmor/KubeArmor/blob/main/getting-started/support_matrix.md)

## 1. Install kubearmor cli tool, daemonsets and services

#### Install kubearmor cli tool
```sh
curl -sfL http://get.kubearmor.io/ | sudo sh -s -- -b /usr/local/bin
```

#### Install DaemonSets and Services

```sh
# Install KubeArmor
karmor install

# Install Discovery-Engine
kubectl apply -f https://raw.githubusercontent.com/kubearmor/discovery-engine/dev/deployments/k8s/deployment.yaml
```

??? "Output from _kubectl get pods -A_"
	```sh
	NAMESPACE         NAME                                                 READY   STATUS    RESTARTS   AGE
	accuknox-agents   discovery-engine-7b6ddbd7d7-swk7j                    1/1     Running   0          3m58s
	kube-system       kubearmor-78tnh                                      1/1     Running   0          4m7s
	kube-system       kubearmor-annotation-manager-797c848b9c-vxq8c        2/2     Running   0          4m
	kube-system       kubearmor-host-policy-manager-766447b4d7-fr5m4       2/2     Running   0          4m6s
	kube-system       kubearmor-policy-manager-54ffc4dc56-8szmn            2/2     Running   0          4m6s
	kube-system       kubearmor-relay-645667c695-bfwcn                     1/1     Running   0          4m7s
	...
	```

	We have following installed:

	* KubeArmor Protection Engine
	* Discovery Engine
	* KubeArmor Relay

## 2. Install Sample Application

Install the following app (_WordPress_) or you can try your own K8s app.

```sh
kubectl apply -f https://raw.githubusercontent.com/kubearmor/KubeArmor/main/examples/wordpress-mysql/wordpress-mysql-deployment.yaml
```
??? "Output from _kubectl get pods -n wordpress-mysql_"
	```sh
	NAME                        READY   STATUS    RESTARTS   AGE
	mysql-58cdf6ccf-kzbp8       1/1     Running   0          12s
	wordpress-bf95888cb-2kx65   1/1     Running   0          13s
	```

	Keep a note of these pods name `mysql-xxxxxxxxx-xxxxx` & `wordpress-xxxxxxxxx-xxxxx`, it'll be different for your environment

The use-cases described in subsequent step uses this sample application.

## 3. Demo Scenario & Use-cases

![Alt](/getting-started/images/6.png)

??? "Use-case 1: Audit access to sensitive data paths"

	MySQL keeps all its database tables as part of `/var/lib/mysql` folder path. **Audit** access to this folder path recursively (sub-folders inclusive).

	```yaml
	apiVersion: security.kubearmor.com/v1
	kind: KubeArmorPolicy
	metadata:
	  name: ksp-mysql-audit-dir
	  namespace: wordpress-mysql
	spec:
	  severity: 5
	  selector:
	    matchLabels:
	      app: mysql
	  file:
	    matchDirectories:
	      - dir: /var/lib/mysql/
	        recursive: true
	  action: Audit
	```

	**Executing inside MySQL pod:** Before applying policy
	```sh
	kubectl exec -it mysql-xxxxxxxxx-xxxxx -n wordpress-mysql -- bash
	root@mysql-58cdf6ccf-kzbp8:/# touch /var/lib/mysql/test
	```
	> **_NOTE 01:_** Replace `mysql-xxxxxxxxx-xxxxx` with pod name from Step [#2](#2-install-sample-application)

	![Alt](/getting-started/images/7.png)

	**Applying Policy:** Applying above [policy](https://raw.githubusercontent.com/kubearmor/KubeArmor/main/examples/wordpress-mysql/security-policies/ksp-mysql-audit-dir.yaml) to deployed [application](#2-install-sample-application)
	```sh
	kubectl apply -f ksp-mysql-audit-dir.yaml
	```

	**Port Forwarding:** We'll be using KubeArmor relay to forward logs to our local system
	```sh
	kubectl -n kube-system port-forward service/kubearmor --address 0.0.0.0 --address :: 32767:32767
	```

	**Realtime Logs Streaming:**
	```sh
	karmor log
	```
	> **_NOTE 02:_** Above 2 commands will be common for all use cases, keep this open in separate terminals (_right section of screenshot_)

	**Executing inside MySQL pod:** After applying policy
	```sh
	kubectl exec -it mysql-xxxxxxxxx-xxxxx -n wordpress-mysql -- bash
	root@mysql-58cdf6ccf-kzbp8:/# touch /var/lib/mysql/test-2
	```
	![Alt](/getting-started/images/8.png)

??? "Use-case 2: Block access to files containing sensitive data"

	WordPress pod contains a file `wp-config.php` that has sensitive auth credentials. This use-case is to **Block** access to this file from unknown processes.

	**Executing inside WordPress pod:** Before applying policy
	```sh
	kubectl exec -it wordpress-xxxxxxxxx-xxxxx -n wordpress-mysql -- bash
	root@wordpress-bf95888cb-2kx65:/var/www/html# cat /var/www/html/wp-config.php
	```

	![Alt](/getting-started/images/9.png)

	```yaml
	apiVersion: security.kubearmor.com/v1
	kind: KubeArmorPolicy
	metadata:
	  name: ksp-wordpress-block-config
	  namespace: wordpress-mysql
	spec:
	  severity: 10
	  selector:
	    matchLabels:
	      app: wordpress
	  file:
	    matchPaths:
	      - path: /var/www/html/wp-config.php
	        fromSource:
	          - path: /bin/cat
	  action: Block
	```

	**Applying Policy:** Applying above [policy](https://raw.githubusercontent.com/kubearmor/KubeArmor/main/examples/wordpress-mysql/security-policies/ksp-wordpress-block-config.yaml) to deployed [application](#2-install-sample-application)
	```sh
	kubectl apply -f ksp-wordpress-block-config.yaml
	```

	**Executing inside WordPress pod:** After applying policy
	```sh
	kubectl exec -it wordpress-xxxxxxxxx-xxxxx -n wordpress-mysql -- bash
	root@wordpress-bf95888cb-2kx65:/var/www/html# cat /var/www/html/wp-config.php
	cat: /var/www/html/wp-config.php: Permission denied
	```

	![Alt](/getting-started/images/10.png)

??? "Use-case 3: Block access to K8s service account token"

	A [pod](https://kubernetes.io/docs/concepts/workloads/pods/) is the primary execution unit in K8s. One problem with this approach is that all the processes within that pod have unrestricted access to the pod's volume mounts. One such volume mount is a service account token. Thus, accessing a service account token using an injected binary is a common attack pattern in K8s. This use-case explains how you can protect access (**Block**) to the service account token through known processes only.

	**Executing inside WordPress pod:** Before applying policy
	```sh
	kubectl exec -it wordpress-xxxxxxxxx-xxxxx -n wordpress-mysql -- bash
	root@wordpress-bf95888cb-2kx65:/var/www/html# cat /run/secrets/kubernetes.io/serviceaccount/token
	```

	![Alt](/getting-started/images/11.png)

	```yaml
	apiVersion: security.kubearmor.com/v1
	kind: KubeArmorPolicy
	metadata:
	  name: ksp-wordpress-block-sa
	  namespace: wordpress-mysql
	spec:
	  severity: 7
	  selector:
	    matchLabels:
	      app: wordpress
	  file:
	    matchDirectories:
	      - dir: /run/secrets/kubernetes.io/serviceaccount/
	        recursive: true
	  action: Block
	```

	**Applying Policy:** Applying above [policy](https://raw.githubusercontent.com/kubearmor/KubeArmor/main/examples/wordpress-mysql/security-policies/ksp-wordpress-block-sa.yaml) to deployed [application](#2-install-sample-application)
	```sh
	kubectl apply -f ksp-wordpress-block-sa.yaml
	```

	**Executing inside WordPress pod:** After applying policy
	```sh
	kubectl exec -it wordpress-xxxxxxxxx-xxxxx -n wordpress-mysql -- bash
	root@wordpress-bf95888cb-2kx65:/var/www/html# cat /run/secrets/kubernetes.io/serviceaccount/token
	cat: /run/secrets/kubernetes.io/serviceaccount/token: Permission denied
	```

	![Alt](/getting-started/images/12.png)

??? "Use-case 4: Block execution of unwanted processes"

	A [container image](https://kubernetes.io/docs/concepts/containers/images/) might get shipped with binaries that are not supposed to be executed in production environments. For e.g., WordPress contains `apt`, `apt-get` binaries that are used for dynamic package management. These should never be used in the production environment since it will create drift (change) in the container contents i.e., introduce new files/binaries that might increase the attack surface. The following policy **Block** the execution of such processes.

	**Executing inside WordPress pod:** Before applying policy
	```sh
	kubectl exec -it wordpress-xxxxxxxxx-xxxxx -n wordpress-mysql -- bash
	root@wordpress-bf95888cb-2kx65:/var/www/html# apt
	root@wordpress-bf95888cb-2kx65:/var/www/html# apt-get update
	```

	![Alt](/getting-started/images/13.png)

	```yaml
	apiVersion: security.kubearmor.com/v1
	kind: KubeArmorPolicy
	metadata:
	  name: ksp-wordpress-block-process
	  namespace: wordpress-mysql
	spec:
	  severity: 3
	  selector:
	    matchLabels:
	      app: wordpress
	  process:
	    matchPaths:
	      - path: /usr/bin/apt
	      - path: /usr/bin/apt-get
	  action: Block
	```

	**Applying Policy:** Applying above [policy](https://raw.githubusercontent.com/kubearmor/KubeArmor/main/examples/wordpress-mysql/security-policies/ksp-wordpress-block-process.yaml) to deployed [application](#2-install-sample-application)
	```sh
	kubectl apply -f ksp-wordpress-block-process.yaml
	```

	**Executing inside WordPress pod:** After applying policy
	```sh
	kubectl exec -it wordpress-5679855487-58rfz -n wordpress-mysql –- bash
	root@wordpress-bf95888cb-2kx65:/var/www/html# apt
	bash: /usr/bin/apt: Permission denied
	root@wordpress-bf95888cb-2kx65:/var/www/html# apt-get update
	bash: /usr/bin/apt-get: Permission denied
	```

	![Alt](/getting-started/images/14.png)

## 4. Get Recommended Policies

In the above [Demo Scenario](#3-demo-scenario--use-cases), we had to explicitly write KubeArmor policies. But with the new KubeArmor recommendation it is easy to get a set of security best practice policies tailored to your environment. 

<details>
  <summary> <b><i>karmor recommend --namespace wordpress-mysql --labels app=wordpress</i></b> </summary>

```sh
INFO[0000] pulling image                                 image="wordpress:4.8-apache"
4.8-apache: Pulling from library/wordpress
Digest: sha256:6216f64ab88fc51d311e38c7f69ca3f9aaba621492b4f1fa93ddf63093768845
Status: Image is up to date for wordpress:4.8-apache
INFO[0015] dumped image to tar                           tar=/tmp/karmor4070582578/GwoIiuRV.tar
Distribution debian
INFO[0018] No runtime policy generated for wordpress-mysql/wordpress/wordpress:4.8-apache 
created policy out/wordpress-mysql-wordpress/wordpress-4-8-apache-maintenance-tool-access.yaml ...
created policy out/wordpress-mysql-wordpress/wordpress-4-8-apache-cert-access.yaml ...
created policy out/wordpress-mysql-wordpress/wordpress-4-8-apache-system-owner-discovery.yaml ...
created policy out/wordpress-mysql-wordpress/wordpress-4-8-apache-system-monitoring-deny-write-under-bin-directory.yaml ...
created policy out/wordpress-mysql-wordpress/wordpress-4-8-apache-system-monitoring-write-under-dev-directory.yaml ...
created policy out/wordpress-mysql-wordpress/wordpress-4-8-apache-least-functionality-execute-package-management-process-in-container.yaml ...
output report in out/report.txt ...
```
</details>

??? "Using recommended policies"

	The recommended policy `xx-xx-cert-access.yaml` is a powerful policy which enables read access to trusted certificates but denied any form of write to it. This inturn enables the integrity of the file and denies malware/adware to have Adversary-in-the-Middle capability (Ref [MITRE-T1553](https://attack.mitre.org/techniques/T1553/)).

	**Executing inside WordPress pod:** Before applying policy
	```sh
	kubectl exec -it wordpress-xxxxxxxxx-xxxxx -n wordpress-mysql -- bash
	root@wordpress-cb9c668d4-zgczt:/var/www/html# cd /etc/ssl/
	root@wordpress-cb9c668d4-zgczt:/etc/ssl# echo "new private key" > myssl.pem
	root@wordpress-cb9c668d4-zgczt:/etc/ssl# cat myssl.pem 
	new private key
	root@wordpress-cb9c668d4-zgczt:/etc/ssl#
	```

	![Alt](/getting-started/images/before_rec.png)

	```yaml
	apiVersion: security.kubearmor.com/v1
	kind: KubeArmorPolicy
	metadata:
	name: wordpress-wordpress-4-8-apache-cert-access
	namespace: wordpress-mysql
	spec:
	action: Block
	file:
		matchDirectories:
		- dir: /etc/ssl/
		readOnly: true
		recursive: true
		- dir: /etc/pki/
		readOnly: true
		recursive: true
		- dir: /usr/local/share/ca-certificates/
		readOnly: true
		recursive: true
	message: Credentials modification denied
	selector:
		matchLabels:
		app: wordpress
	severity: 1
	tags:
	- MITRE
	- MITRE_T1552_unsecured_credentials
	```

	**Applying Policy:** Applying above recommended policy to deployed [application](#2-install-sample-application)
	```sh
	kubectl apply -f out/wordpress-mysql-wordpress/wordpress-4-8-apache-cert-access.yaml
	```

	**Executing inside WordPress pod:** After applying policy
	```sh
	kubectl exec -it wordpress-cb9c668d4-zgczt -n wordpress-mysql –- bash
	root@wordpress-cb9c668d4-zgczt:/var/www/html# cd /etc/ssl/
	root@wordpress-cb9c668d4-zgczt:/var/www/html# cat myssl.pem 
	new private key
	root@wordpress-cb9c668d4-zgczt:/var/www/html# echo "updated ssl key" >> myssl.pem 
	bash: /etc/ssl/myssl.pem: Permission denied
	root@wordpress-cb9c668d4-zgczt:/var/www/html#
	```

	![Alt](/getting-started/images/after_rec.png) 


## 5. Get Auto-Discovered Policies

In the above [Demo Scenario](#3-demo-scenario--use-cases) _(last 3 use-cases)_, we had explicit **Deny** based policies. KubeArmor also supports **Allow** based policies i.e., allow only specific actions and audit/deny everything else. Also the allow-policies are auto-discovered by examining the workloads at runtime.

To retrieve the auto discovered policies you can use:
```sh
karmor discover -n wordpress-mysql -l "app=wordpress" -f yaml
```
This discovers the policies for a workload in `wordpress-mysql` namespace having label `app=wordpress`.

??? "Output from _karmor discover -n wordpress-mysql -l "app=wordpress" -f yaml_"
	```yaml
	apiVersion: security.kubearmor.com/v1
	kind: KubeArmorPolicy
	metadata:
	  name: autopol-system-3960684242
	  namespace: wordpress-mysql
	spec:
	  action: Allow
	  file:
		matchPaths:
		- fromSource:
		  - path: /usr/sbin/apache2
		  path: /dev/urandom
		- fromSource:
		  - path: /usr/local/bin/php
		  path: /etc/hosts
	  network:
		matchProtocols:
		- fromSource:
		  - path: /usr/local/bin/php
		  protocol: tcp
		- fromSource:
		  - path: /usr/local/bin/php
		  protocol: udp
	  process:
		matchPaths:
		- path: /usr/sbin/apache2
		- path: /usr/local/bin/php
	  selector:
		matchLabels:
		  app: wordpress
	  severity: 1
	```

## 6. Uninstall

```sh
karmor uninstall

# If there is no other workloads deployed in accuknox-agents namesapce apart from DE, this can be removed
kubectl delete ns accuknox-agents
```

## References
1. [AccuKnox Splunk App for Compliance and K8s Events](./../integrations/accuKnox-splunk-app-installation-configuration.md)
2. [KubeArmor support matrix](https://github.com/kubearmor/KubeArmor/blob/main/getting-started/support_matrix.md)
3. [Integrating KubeArmor with Prometheus and Grafana](https://github.com/kubearmor/kubearmor-prometheus-exporter)

- - - 
[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }
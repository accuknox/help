---
hide:
  - toc
---

WordPress-MySQL Application has the WordPress front end connecting to the MySQL backend. When this application is deployed in the k8s environment, we have two pods one for WordPress and another for Mysql. We can onboard the cluster to our Accuknox SaaS by following the steps here 

 

## **Observability:** 

Once the cluster with the WordPress-MySQL application is onboarded we can see the application behavior by Navigating to the Runtime Security->App Behavior section. In the screen the select cluster name and namespace in which the WordPress-MySQL application is deployed. 


**1.Network Observability:**

Here we can get the details of the ingress and egress connections that are happening in the pod.
![](/use-cases/images/word-my-1.png)

**2.File observability:**

In file observability, the information related to the files that are being accessed in the pod will be shown 
![](/use-cases/images/word-my-2.png)

**3.Process Observability:** 

In process observability, the information related to the process that is being executed in the pod will be shown. 

![](/use-cases/images/word-my-3.png)
## **Protecting WordPress-MySQL Application using AccuKnox:** 

??? "**1. Preventing WordPress from Remote-code execution**" 

    Based on the application behavior currently, in the WordPress pod, the attacker can easily get access to the bash and execute his remote code using the package management tools. The attacker can leverage this vulnerability to execute his code or download any binary into the pod. 

    ![](/use-cases/images/word-my-5.png)

    we can protect this with help of hardening policies that kubearmor has discovered based on the application behavior of this WordPress-mysql application. To see and apply this hardening policy follow the below steps

    
    **Protection using Accuknox** 
    
    **Step 1:**  Navigate to the Runtime Protection-> Policies and select the cluster and namespace where the WordPress-MySQL application is deployed. 
    ![](/use-cases/images/word-my-5.png)

    **Step 2:** In the screen select the hardening policies in the policy filter section to view the hardening policies related to the WordPress-MySQL application. 
    ![](/use-cases/images/word-my-6.png)
    **Step 3:** Click on the WordPress package manager execution hardening policy from the list of policies to see the policy
    ![](/use-cases/images/word-my-7.png)

    The Hardening policy is blocking the execution of any package management tools inside the WordPress pod. 
    ```bash 
        apiVersion: security.kubearmor.com/v1
        kind: KubeArmorPolicy
        metadata:
        name: harden-wordpress-pkg-mngr-exec
        namespace: wordpress-mysql
        spec:
        action: Block
        message: Alert! Execution of package management process inside container is denied
        process:
            matchPaths:
            - path: /usr/bin/apt
            - path: /usr/bin/apt-get
            - path: /bin/apt-get
            - path: /sbin/apk
            - path: /bin/apt
            - path: /usr/bin/dpkg
            - path: /bin/dpkg
            - path: /usr/bin/gdebi
            - path: /bin/gdebi
            - path: /usr/bin/make
            - path: /bin/make
            - path: /usr/bin/yum
            - path: /bin/yum
            - path: /usr/bin/rpm
            - path: /bin/rpm
            - path: /usr/bin/dnf
            - path: /bin/dnf
            - path: /usr/bin/pacman
            - path: /usr/sbin/pacman
            - path: /bin/pacman
            - path: /sbin/pacman
            - path: /usr/bin/makepkg
            - path: /usr/sbin/makepkg
            - path: /bin/makepkg
            - path: /sbin/makepkg
            - path: /usr/bin/yaourt
            - path: /usr/sbin/yaourt
            - path: /bin/yaourt
            - path: /sbin/yaourt
            - path: /usr/bin/zypper
            - path: /bin/zypper
        selector:
            matchLabels:
            app: wordpress
        severity: 5
        tags:
        - NIST
        - NIST_800-53_CM-7(4)
        - SI-4
        - process
        - NIST_800-53_SI-4
    ```

    **Step 4:** To apply this policy, select the policy checkbox and click Apply option
    ![](/use-cases/images/word-my-8.png)

    **Step 5:** The policy goes into the pending state for approval. 
    ![](/use-cases/images/word-my-9.png)

    **Step 6:** To approve the policy click on the Pending icon, review changes and approve

    ![](/use-cases/images/word-my-10.png)
    **Step 7:** Now the policy is active and applied on the cluster
    ![](/use-cases/images/word-my-11.png)
    **Step 8:** If any attacker tries to install any binary inside the WordPress pod it will be blocked and we will be getting alerts. 
    ![](/use-cases/images/word-my-12.png)
    **Step 9:** To see the logs Navigate to the Monitoring/logging->logs 
    ![](/use-cases/images/word-my-13.png)

    Thus we have prevented the remote code execution in the WordPress pod using AccuKnox’s CWPP protection.

??? "**2. File Integrity Monitoring**"

    In the MySQL application, certain folders will be having certain critical data which can be allowed to access but not modified. So using our AccuKnox hardening policy we are going to prevent the modification of contents inside these critical folders. 

    **Before applying the policy:** 

    Currently, any attacker who gets access to the bash or shell of the MySQL pod can modify the contents of the sbin folder by creating a new file and editing the old files.

    ![](/use-cases/images/word-my-14.png)

    Now we are going to prevent this using AccuKnox CWPP Solution. 

    **Step 1:**  Navigate to the Runtime Protection-> Policies and select the cluster and namespace where the WordPress-MySQL application is deployed. 

    ![](/use-cases/images/word-my-15.png)
    **Step 2:** In the screen select the hardening policies in the policy filter section to view the hardening policies related to the WordPress-MySQL application. 

    ![](/use-cases/images/word-my-16.png)
    **Step 3:** Click on the MySQL file integrity hardening policy from the list of policies to see the policy
    ![](/use-cases/images/word-my-17.png)

    The policy is allowing users to access the critical folders but it is blocking the write or modify access by whitelisting only read access. 
    ```bash 
        apiVersion: security.kubearmor.com/v1
        kind: KubeArmorPolicy
        metadata:
        name: harden-mysql-file-integrity-monitoring
        namespace: wordpress-mysql
        spec:
        action: Block
        file:
            matchDirectories:
            - dir: /sbin/
            readOnly: true
            recursive: true
            - dir: /usr/bin/
            readOnly: true
            recursive: true
            - dir: /usr/lib/
            readOnly: true
            recursive: true
            - dir: /usr/sbin/
            readOnly: true
            recursive: true
            - dir: /bin/
            readOnly: true
            recursive: true
            - dir: /boot/
            readOnly: true
            recursive: true
        message: Detected and prevented compromise to File integrity
        selector:
            matchLabels:
            app: mysql
        severity: 1
        tags:
        - NIST
        - NIST_800-53_AU-2
        - NIST_800-53_SI-4
        - MITRE
        - MITRE_T1036_masquerading
        - MITRE_T1565_data_manipulation
    ```

    **Step 4:** To apply this policy, select the policy checkbox and click Apply option

    ![](/use-cases/images/word-my-18.png)

    **Step 5:** The policy goes into the pending state for approval. 

    ![](/use-cases/images/word-my-19.png)

    **Step 6:** To approve the policy click on the Pending icon, review changes and approve 

    ![](/use-cases/images/word-my-20.png)
    **Step 7:** Now the policy is active and applied on the cluster

    ![](/use-cases/images/word-my-21.png)
    **Step 8:** If any attacker now tries to modify the content of the critical folders it will be blocked. 

    ![](/use-cases/images/word-my-22.png)
    **Step 9:** To see the logs Navigate to the Monitoring/logging->logs 

    ![](/use-cases/images/word-my-23.png)

    Thus the file integrity of the MySQL pod is maintained using the AccuKnox CWPP security solution. 

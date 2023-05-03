---
hide:
  - toc
---

## **DVWA:** 
Damn Vulnerable Web Application (DVWA) is a PHP/MySQL web application that is damn vulnerable. Its main goal is to be an aid for security professionals to test their skills and tools in a legal environment, help web developers better understand the processes of securing web applications, and to aid both students & teachers to learn about web application security in a controlled classroom environment.

### **DVWA Attack Points:**
+ Command Injection: 
Attacks on the insecure transmission of User data

+ CSRF (Cross-Site Request Forgery): The attacker Froges as original site and makes the user click the link and steal data. Here either cookies or form data is stolen

+ SQL Injection: Attacker can make use of this to get unauthorized to Database access

+ CSP(Content Security Policy): If the particular domain is allowed then a malicious script from that domain can be executed. 

DVWA web Application is deployed in the cluster in the dvwa namespace. It has Web and MySQL pod running with 2 services. 

## **Observability:** 

Once the cluster with the DVWA application is onboarded we can see the application behavior by Navigating to the Runtime Security->App Behavior section. In the screen the select cluster name and namespace in which the DVWA  application is deployed.

![](/use-cases/images/dvwa-1.png)

**1.Network Observability:** It gives data related to network connections happening in the pod


 ![](/use-cases/images/dvwa-2.png)

**2.File Observability:** It gives information regarding files that are being accessed in the pod

![](/use-cases/images/dvwa-3.png)
 

**3.Process Observability:** It shows the process that is being executed in the pod. 

![](/use-cases/images/dvwa-4.png)

## **Protection Using AccuKnox:** 
According to the application behavior, the WordPress pod running in the DVWA uses 2 processes ping and apache2. So we are going to whitelist only these 2 processes and block other processes from execution in the WordPress pod. 

- **Before Applying policy:** 

Before applying our KubeArmor Security policy we can see that along with ping other processes are also can be executed.

![](/use-cases/images/dvwa-5.png)
 

- **Applying the KubeArmor policy:** 

**Step 1:** Navigate to the *Runtime Protection-> Policies* and select the cluster and namespace where the DVWA application is deployed.

![](/use-cases/images/dvwa-6.png)
 

**Step 2:** In the screen select the discovered policies in the policy filter section to view the auto-discovered policies for the DVWA application.


 ![](/use-cases/images/dvwa-7.png)

**Step 3:** Click on the auto-discovered system policy for the dvwa web pod to see the policy

![](/use-cases/images/dvwa-8.png)

The policy allows the necessary processes like ping and apache2 to execute. 

```bash
apiVersion: security.kubearmor.com/v1
kind: KubeArmorPolicy
metadata:
  name: autopol-system-1804736057
  namespace: dvwa
spec:
  action: Allow
  file:
    matchDirectories:
    - dir: /etc/
      fromSource:
      - path: /bin/bash
      recursive: true
    - dir: /lib/x86_64-linux-gnu/
      recursive: true
    - dir: /etc/
      fromSource:
      - path: /bin/bash
      - path: /bin/ping
      recursive: true
    matchPaths:
    - fromSource:
      - path: /bin/bash
      path: /dev/tty
    - fromSource:
      - path: /bin/bash
      path: /lib/terminfo/x/xterm
    - fromSource:
      - path: /bin/bash
      path: /root/.bashrc
    - fromSource:
      - path: /bin/ping
      path: /usr/lib/x86_64-linux-gnu/gconv/gconv-modules.cache
    - fromSource:
      - path: /bin/ping
      path: /usr/lib/x86_64-linux-gnu/libidn2.so.0.3.7
    - fromSource:
      - path: /bin/ping
      path: /usr/lib/x86_64-linux-gnu/libunistring.so.2.1.0
    - fromSource:
      - path: /usr/sbin/apache2
      path: /etc/ld.so.cache
    - fromSource:
      - path: /usr/sbin/apache2
      path: /usr/lib/x86_64-linux-gnu/libapr-1.so.0.7.0
    - fromSource:
      - path: /usr/sbin/apache2
      path: /usr/lib/x86_64-linux-gnu/libaprutil-1.so.0.6.1
    - fromSource:
      - path: /usr/sbin/apache2
      path: /usr/lib/x86_64-linux-gnu/libuuid.so.1.3.0
    - fromSource:
      - path: /usr/sbin/apache2
      path: /usr/share/zoneinfo/Etc/UTC
    - fromSource:
      - path: /bin/bash
      path: /root/.bash_history
  process:
    matchPaths:
    - path: /bin/bash
    - fromSource:
      - path: /bin/bash
      path: /bin/ping
    - fromSource:
      - path: /bin/bash
      path: /usr/sbin/apache2
  selector:
    matchLabels:
      app: dvwa-web
      tier: frontend
  severity: 1
```

**Step 4:** To apply this policy, select the policy checkbox and click Apply option


 ![](/use-cases/images/dvwa-9.png)

**Step 5:** When we apply the policy, it goes into the pending state for approval.


 ![](/use-cases/images/dvwa-10.png)

**Step 6:** Review the changes and approve the policy

![](/use-cases/images/dvwa-11.png)
 

**Step 7:** After Approval policy becomes active
![](/use-cases/images/dvwa-12.png)

 

**Step 8:** Now if we try to execute any other processes inside the dvwa pod it will be blocked. 


 ![](/use-cases/images/dvwa-13.png)

**Step 9:** We can view the logs alerts by navigating to the Monitors/Logs-> logs

![](/use-cases/images/dvwa-14.png)
 

Thus DVWA application’s web pod is protected using AccuKnox CWPP Security solution.

 

- - - 
[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }
---
title: Host Vulnerability & Malware Scan
description: AccuKnox VM Security covers agent-based and agentless scanning offering continuous vulnerability and optional malware detection.
---

# Host Vulnerability & Malware Scan

AccuKnox VM Security covers agent-based and agentless scanning offering continuous vulnerability and optional malware detection.

## Agentless VM Scanning

!!! tip "Getting Started"
    - [Agentless Cloud VM Scanning](https://help.accuknox.com/how-to/vm-security/agentless/cloud-vm-scanning/)

Supports **AWS**, **GCP**, **Azure**, and **OpenShift Virtualization**. This cloud-native approach scans VM disks and metadata without requiring an agent on the VM.

![Agentless cloud VM scanning in AccuKnox](image-18.png)

!!! tip "Getting Started"
    - [Agent-based Linux VM Scanning](https://help.accuknox.com/how-to/vm-security/agent-based/linux/)
    - [Agent-based Windows VM Scanning](https://help.accuknox.com/how-to/vm-security/agent-based/windows/)

For hosts that cannot be scanned agentlessly, AccuKnox provides a lightweight agent for **Linux** and **Windows**. It supports **air-gapped environments** allowing scans without outbound internet access.

![Agent-based VM scanning in AccuKnox](image-17.png)

Scans are tied to tenant-level tokens and labels for identification, grouping, and reporting. Findings are centralized in the AccuKnox console for visibility, correlation, and reporting across workloads.

![Centralized vulnerability findings across VM workloads](image-15.png)

AccuKnox performs deep scans of the host environment to provide rich risk assessment for both hosts and network infrastructure, detecting critical vulnerabilities and misconfigurations.

### **Apache Log4j**

The CVE-2021-44228 RCE vulnerability affects Apache's Log4j library. An adversary can exploit this by submitting a specially crafted request to a vulnerable system to execute arbitrary code. AccuKnox Host Scan detects critical vulnerabilities like Apache Log4j and provides steps to remediate them.

![image-20241219-082057.png](./images/vm-host-scan/1.png)

#### **Solution**

Upgrading the package to the latest supported version will remediate the vulnerability

![image-20241219-082127.png](./images/vm-host-scan/2.png)

### **Microsoft RDP RCE (CVE-2019-0708)**

A remote code execution vulnerability exists in Remote Desktop Services. An attacker who successfully exploited this vulnerability could execute arbitrary code on the target system. AccuKnox detects the Microsoft RDP RCE and provides descriptive solutions to help organizations patch the critical vulnerability.

![image-20241219-082748.png](./images/vm-host-scan/3.png)

#### Solution

Microsoft has released a set of patches for OS having CVE-2019-0708, Installing the security patch will remediate the vulnerability.

![image-20241219-082810.png](./images/vm-host-scan/4.png)

### **MS11-020: Vulnerability in SMB Server**

The remote host is affected by a vulnerability in the SMB server that may allow an attacker to execute arbitrary code or perform a denial of service against the remote host. AccuKnox scans the host to identify vulnerabilities related to outdated components, packages, operating systems, file systems, and more.

![image-20241219-083527.png](./images/vm-host-scan/5.png)

#### Solution

Microsoft has released the security patches which need to be installed to remediate the security issues. To remediate this, users can create tickets from AccuKnox Saas UI with the details of the findings.

![image-20241219-083552.png](./images/vm-host-scan/6.png)

---
title: Container Image Scanning
description: Identify and fix vulnerabilities in container images with AccuKnox’s scanning solution to ensure secure, threat-free applications.
---

**Need for securing containers for Application Hardening**

With advent of digital transformation, there has been a significant increase in container adoption in production environments which is **making containers an easy target for exploitation**. Since the Pod is the smallest execution unit in Kubernetes and its usually unsecure which means once you do a exec in a Pod, you can access all sensitive paths, files or execute a binary. And therefore even a single vulnerable or compromised container could potentially become a point of entry into an organization's broader environment.

AccuKnox can secure containers by scanning container images, monitoring code in repositories and registries and evaluating it against security best practices using auto-recommended hardening policies as a part of continuous integration and continuous delivery workflows. We can secure both managed and unmanaged cluster, public and private cloud hosted workloads as well.

Lets understand this by an example use-case - **Container Image scanning**

- User can add docker hub, ECR registries by navigating to _Issues→Registryscan_. In the screen click **Add Registry** option

![image-scan](images/image-scan-1.png)

- If you have an existing registry give the necessary details of your registry to scan. For step by step onboarding instructions, refer:

    - [ECR onboarding](../how-to/ecr.md)
    - [GAR onboarding](../how-to/gar.md)
    - [ACR onboarding](../how-to/acr.md)

![image-scan](images/image-scan-2.png)

- Once the registry is added successfully, the scan will automatically start and user can navigate to the Issues→Registry scan option to see the findings

![image-scan](images/image-scan-3.png)

---

[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }

---
hide:
 - toc
---

# Compliance Posture with AccuKnox CSPM

CSPM Misconfigurations comes with more than 1,000 out-of-the-box compliance cheks that evaluate the configuration of your cloud resources and identify potential misconfigurations. Each compliance rule maps to one or more compliance programs and there sub-controls within a compliance standard or industry benchmarks.
Cloud security is a dynamic landscape, with ever-evolving threats and regulatory requirements. Compliance with various industry standards such as PCI DSS, HIPAA, GDPR, SOC, ISO, CIS, and many more are crucial for businesses across sectors. However, keeping track of these requirements and ensuring your cloud infrastructure aligns with them can be a daunting task.

This is where AccuKnox’s CSPM shines. There are over 30 new compliance programs, From healthcare to finance, retail to government, CSPM covers a wide range of industry-specific regulations, ensuring that your cloud environment meets the necessary security standards.

## View your compliance posture

View a high-level overview of your compliance posture for each framework on the Cloud Asset Summary page.

As soon as user onboards the cloud account and scan is done, User can navigate to the Compliance Section in Nav Bar and see the list of all compliance programs against which scan were done.
Each Compliance Program are divided into there Sub Controls and for each sub control user can see the percentage of compliance.

The percentage is calculated by the number of Passed Checks/Rules against the Total number of Passed, Failed, Warning and Not Available checks.

User can click on any Compliance Program or there Sub-control which will navigate to the list of misconfiguration. Further user can filter based on Cloud Account, Region, Severity, Checks, and many more on the **Detailed View** Tab.

-   **Compliance**: A  detailed report  that gives you insight into how you score against a framework’s requirements and rules.
![alt](images/compliance-summary.png)
-   **Detailed View**: A filtered view of the  **Misconfigurations**  page that shows resources with misconfigurations for the selected Compliance Program.
![alt](images/compliane-detailed-view.png)

## Compliance Support Matrix

| AWS | Azure | GCP |
|-----|-------|-----|
1. APRA 234 STANDARD<br>2. AWS CIS Benchmark v 1 .4.0<br>3. AWS CIS Benchmark v 1 .5.0<br>4. AWS CIS Benchmark v 2.0.0<br>5. AWS Well-Architected Framework - Security<br>6. BAIT<br>7. California Consumer Privacy Act (CCPA)<br>8. COPPA<br>9. CSPM Encryption Program<br>10. FedRamp<br>11. FERPA<br>12. FISMA<br>13. General Data Protection Regulation (GDPR) EU<br>14. HIPAA<br>15. HITRUST CSF<br>16. ISMS-P for AWS<br>17. ISO 27001<br>18. ISO 27018<br>19. Korean Financial Security Agency Guidelines<br>20. LGPD<br>21. Mitre AWS Attack Framework<br>22. NIST 800-171<br>23. NIST CSF<br>24. NIST SP 800-53<br>25. PCI<br>26. SOC 2 Type II<br>27. SOC 3<br>28. VAIT<br> | 1. APRA 234 STANDARD<br>2. Azure CIS Benchmark v 2.0.0<br>3. Azure CIS Benchmark v 1.3.0<br>4. BAIT<br>5. California Consumer Privacy Act (CCPA)<br>6. COPPA<br>7. CSPM Encryption Program<br>8. FedRamp<br>9. FERPA<br>10. FISMA<br>11. General Data Protection Regulation (GDPR) EU<br>12. HIPAA<br>13. HITRUST CSF<br>14. ISO 27001<br>15. ISO 27018<br>16. Korean Financial Security Agency Guidelines<br>17. LGPD<br>18. ISO 27017<br>19. NIST 800-171<br>20. NIST CSF<br>21. NIST SP 800-53<br>22. PCI<br>23. SOC 2 Type II<br>24. SOC 3<br>25. VAIT | 1. APRA 234 STANDARD<br>2. BAIT<br>3. California Consumer Privacy Act (CCPA)<br>4. COPPA<br>5. CSPM Encryption Program<br>6. FedRamp<br>7. FERPA<br>8. FISMA<br>9. General Data Protection Regulation (GDPR) EU<br>10. HIPAA<br>11. HITRUST CSF<br>12. ISO 27001<br>13. ISO 27017<br>14. ISO 27018<br>15. Korean Financial Security Agency Guidelines<br>16. LGPD<br>17. NIST 800-171<br>18. NIST CSF<br>19. NIST SP 800-53<br>20. PCI<br>21. SOC 2 Type II<br>22. SOC 3<br>23. VAIT<br>24. GCP CIS Benchmarks V 1.2.O<br>25. GCP CIS Benchmarks V 2.0.0 |


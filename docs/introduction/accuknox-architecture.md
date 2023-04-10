# **Accuknox Architecture:** 

In the cloud-native deployment phases, there can be many security issues like vulnerable code, Insecure configurations, and Hardcoded secrets in the code-building phase. In the deploying phase, there can issue with malicious images, image poisoning, insecure CI/CD pipelines, etc. In the final phase, there can be issues like runtime security issues like zero-day attacks, Crypto mining data exfiltrations, malware, and vulnerabilities that are still left out un-detected, etc. 

There are multiple tools that are available to provide security in various stages of the Software Development Life cycle. But using these tools at different stages becomes difficult as there is no common connectivity between these tools to get reports and findings. Hence we need a single tool that provides end-to-end solutions for cloud security from the development to the production process. Cloud Native Application Protection Platform tool which is a one-stop solution that integrates various results and normalizes/correlates the findings to provide complete security to the cloud resources becomes the need of the hour. 

![](/introduction/images/accuknox-architecture.png)

 AccuKnox’s Cloud Native Application Protection platform is a single tool that provides both Static as well as dynamic Security. AccuKnox Enterprise Architecture consists of various Microservices like the vault for secret management, Mongo DB for database-related connections and it uses API gateway. AccuKnox CSPM tool scans the infrastructure and stores the scan data in the S3 bucket either created by AccuKnox or the S3 bucket created by the customer. AccuKnox can also be integrated with the CI/CD pipelines and SIEM tools like Jira, Slack, Splunk, and Rsyslog as well.

[^]:[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }
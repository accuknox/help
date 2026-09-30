# Does Prisma Cloud DSPM classify secrets or credentials such as API keys, private keys or passwords found in S3 or blob storage files?

Prisma Cloud **DSPM** (Data Security Posture Management) *does* analyze and classify **unstructured data** in **S3 buckets** and **Blob storages** via its data classification capability ([Use Cases](/content-collections/data-security-posture-management/welcome/use-cases.md)). However, the DSPM documentation I can access **does not explicitly say** it classifies **secrets/credentials** (like **API keys**, **private keys**, or **passwords**) when they are found **inside files stored in S3 or Blob storage**.

For **secrets/credentials detection**, the docs specifically describe a separate capability: **Detect secrets** (compliance checks / agentless + defender scanning) that detects secrets inside **host files** and **container image/container filesystem**. It lists secret types such as **AWS Access Key ID / AWS Secret Key**, **private encryption keys**, and **SaaS API keys** ([Detect secrets](/admin-guide/33/compliance/detect-secrets.md)).

So, based on the available docs: **DSPM can classify sensitive data in S3/blob, but secret/credential classification in those storage files is not explicitly confirmed**—secret detection is documented separately for host/container/image files.

# Suggested Follow-up Questions:

If you need more information, consider asking one of these follow-up questions by performing an HTTP GET request on the URL:

- [Do DSPM tag secrets in S3 files?](https://docs.prismacloud.io?ask=Do%20DSPM%20tag%20secrets%20in%20S3%20files%3F)
- [Secrets detection in DSPM for object storage?](https://docs.prismacloud.io?ask=Secrets%20detection%20in%20DSPM%20for%20object%20storage%3F)
- [How are S3 secrets surfaced in DDR?](https://docs.prismacloud.io?ask=How%20are%20S3%20secrets%20surfaced%20in%20DDR%3F)

# Sources:

- [Welcome to Prisma Cloud DSPM](https://docs.prismacloud.io/content-collections/data-security-posture-management/welcome.md)
- [Detect secrets](https://docs.prismacloud.io/admin-guide/33/compliance/detect-secrets.md)
- [Secrets](https://docs.prismacloud.io/content-collections/runtime-security/secrets.md)
- [Secrets](https://docs.prismacloud.io/admin-guide/secrets/secrets.md)
- [Secrets](https://docs.prismacloud.io/admin-guide/32/secrets/secrets.md)
- [Secrets](https://docs.prismacloud.io/admin-guide/33/secrets/secrets.md)
- [Supported Assets](https://docs.prismacloud.io/content-collections/data-security-posture-management/welcome/supported-assets.md)
- [Tag Assets in Prisma Cloud DSPM Using key:value Tagging](https://docs.prismacloud.io/content-collections/data-security-posture-management/how-to-articles/assets-and-files/tag-assets-within-dig-security-using-keyvalue-tagging.md)
- [Prisma Cloud API Access Keys](https://docs.prismacloud.io/content-collections/get-started/access-keys.md)
- [Integrate Prisma Cloud DSPM With PagerDuty](https://docs.prismacloud.io/content-collections/data-security-posture-management/prisma-cloud-dspm-integrations/integrate-pageduty-with-dig-security.md)
- [Detect secrets](https://docs.prismacloud.io/admin-guide/compliance/detect-secrets.md)
- [Detect Secrets](https://docs.prismacloud.io/content-collections/runtime-security/compliance/operations/detect-secrets.md)
- [Detect secrets](https://docs.prismacloud.io/admin-guide/32/compliance/detect-secrets.md)
- [Use Cases](https://docs.prismacloud.io/content-collections/data-security-posture-management/welcome/use-cases.md)
- [Data Security Posture Management](https://docs.prismacloud.io/content-collections/data-security-posture-management/data-security-posture-management.md)
- [AWS Permissions](https://docs.prismacloud.io/content-collections/data-security-posture-management/prisma-cloud-dspm-deployment/deploy-prisma-cloud-dspm-on-aws/aws-permissions.md)
- [Secrets Manager](https://docs.prismacloud.io/content-collections/runtime-security/secrets/secrets-manager.md)
- [Secrets Scanning](https://docs.prismacloud.io/content-collections/application-security/risk-management/monitor-and-manage-code-build/secrets-scanning.md)
- [Authenticate and call your first API](https://docs.prismacloud.io/content-collections/data-security-posture-management/api-documentation/authenticate-and-call-your-first-api.md)
- [Application Security](https://docs.prismacloud.io/content-collections/application-security/application-security.md)
- [Access Keys](https://docs.prismacloud.io/content-collections/runtime-security/authentication/access-keys.md)


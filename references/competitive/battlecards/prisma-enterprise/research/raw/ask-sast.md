# Does Prisma Cloud Enterprise Edition Application Security include a native SAST scanner for first-party code weaknesses, and which languages?

No — the Application Security SAST coverage in **Prisma Cloud Enterprise Edition** is described as **ingesting SAST findings from third-party tools**, not as a **native SAST scanner** for first-party code weaknesses.

* Prisma Cloud “**ingest\[s] Static Application Security Testing (SAST) findings directly from third-party sources**” via third-party ingestion workflows ([Manage Third-Party Data Ingestion](/content-collections/application-security/risk-management/monitor-and-manage-code-build/third-party-ingest-manage.md)).
* The supported SAST ingestion sources listed are **Veracode**, **SonarQube**, and **SARIF** ([Third-Party Ingestion](/content-collections/application-security/get-started/connect-code-and-build-providers/third-party-ingestion.md)).

### Which languages?

The docs available to me **do not specify language support for SAST** (for native or ingested SAST). They only provide language/package-manager support details for **SCA** (for example, Java/Maven, JavaScript/npm, Python/pip) in [Supported Technologies](/content-collections/application-security/supported-technologies.md).

# Suggested Follow-up Questions:

If you need more information, consider asking one of these follow-up questions by performing an HTTP GET request on the URL:

- [Is there a native SAST option later?](https://docs.prismacloud.io?ask=Is%20there%20a%20native%20SAST%20option%20later%3F)
- [Which languages are covered by SAST ingestion?](https://docs.prismacloud.io?ask=Which%20languages%20are%20covered%20by%20SAST%20ingestion%3F)
- [Can I add more third-party SAST sources?](https://docs.prismacloud.io?ask=Can%20I%20add%20more%20third-party%20SAST%20sources%3F)

# Sources:

- [Manage Third-Party Data Ingestion](https://docs.prismacloud.io/content-collections/application-security/risk-management/monitor-and-manage-code-build/third-party-ingest-manage.md)
- [Application Security](https://docs.prismacloud.io/content-collections/application-security/application-security.md)
- [Supported Technologies](https://docs.prismacloud.io/content-collections/application-security/supported-technologies.md)
- [Prisma Cloud Enterprise Edition vs Compute Edition](https://docs.prismacloud.io/content-collections/runtime-security/pcee-vs-pcce.md)
- [Prisma Cloud Enterprise Edition vs Compute Edition](https://docs.prismacloud.io/admin-guide/33/welcome/pcee-vs-pcce.md)
- [IDE](https://docs.prismacloud.io/content-collections/application-security/ides.md)
- [Prisma Cloud Enterprise Edition vs Compute Edition](https://docs.prismacloud.io/admin-guide/32/welcome/pcee-vs-pcce.md)
- [Scan IaC Files with twistcli](https://docs.prismacloud.io/content-collections/runtime-security/tools/twistcli-scan-iac.md)
- [Prisma Cloud Enterprise Edition vs Compute Edition](https://docs.prismacloud.io/admin-guide/welcome/pcee-vs-pcce.md)
- [Vulnerability Management](https://docs.prismacloud.io/admin-guide/32/vulnerability-management/vulnerability-management.md)
- [Add Prisma Cloud Code Security Scanner as a Pre-Receive Hook](https://docs.prismacloud.io/content-collections/application-security/get-started/add-pre-receive-hooks.md)
- [Add Prisma Cloud Code Security Scanner as a Pre-Commit Hook](https://docs.prismacloud.io/content-collections/application-security/get-started/add-pre-commit-hooks.md)
- [Runtime Security Support Lifecycle](https://docs.prismacloud.io/content-collections/runtime-security/rs-support-lifecycle.md)
- [Vulnerability Management](https://docs.prismacloud.io/admin-guide/vulnerability-management/vulnerability-management.md)
- [Prisma Cloud Console Prerequisites](https://docs.prismacloud.io/content-collections/get-started/console-prerequisites.md)
- [Vulnerability Management](https://docs.prismacloud.io/content-collections/runtime-security/vulnerability-management.md)
- [Monitor and Manage Code Build Issues](https://docs.prismacloud.io/content-collections/application-security/risk-management/monitor-and-manage-code-build.md)
- [Software Composition Analysis (SCA)](https://docs.prismacloud.io/content-collections/application-security/risk-management/monitor-and-manage-code-build/software-composition-analysis.md)
- [Monitor Code Build Issues](https://docs.prismacloud.io/content-collections/application-security/risk-management/monitor-and-manage-code-build/monitor-code-build-issues.md)
- [Code to Cloud Dashboard](https://docs.prismacloud.io/content-collections/dashboards/dashboards-code-to-cloud.md)
- [Suppress Code Issues](https://docs.prismacloud.io/content-collections/application-security/risk-management/monitor-and-manage-code-build/suppress-code-issues.md)
- [AWS Code Build](https://docs.prismacloud.io/content-collections/application-security/get-started/connect-code-and-build-providers/ci-cd-runs/add-aws-codebuild.md)
- [Connect Code and Build Providers](https://docs.prismacloud.io/content-collections/application-security/get-started/connect-code-and-build-providers.md)
- [Access Prisma Cloud](https://docs.prismacloud.io/content-collections/get-started/access-prisma-cloud.md)
- [Prisma Cloud Vulnerability Feed](https://docs.prismacloud.io/content-collections/runtime-security/vulnerability-management/prisma-cloud-vulnerability-feed.md)
- [Third-Party Ingestion](https://docs.prismacloud.io/content-collections/application-security/get-started/connect-code-and-build-providers/third-party-ingestion.md)
- [Welcome to Prisma Cloud](https://docs.prismacloud.io/content-collections/get-started/welcome-to-prisma-cloud.md)
- [Ingest SonarQube Data](https://docs.prismacloud.io/content-collections/application-security/get-started/connect-code-and-build-providers/third-party-ingestion/sonarqube-ingestion.md)
- [Ingest SARIF Data](https://docs.prismacloud.io/content-collections/application-security/get-started/connect-code-and-build-providers/third-party-ingestion/sarif-ingestion.md)
- [Ingest Veracode Data](https://docs.prismacloud.io/content-collections/application-security/get-started/connect-code-and-build-providers/third-party-ingestion/veracode-ingestion.md)
- [Prisma Cloud Platform](https://docs.prismacloud.io/content-collections/get-started/prisma-cloud-platform.md)
- [Continuous Integration](https://docs.prismacloud.io/content-collections/runtime-security/continuous-integration.md)


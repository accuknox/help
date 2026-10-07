For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/authentication/credentials-store/gitlab-credentials.md).

Prisma Cloud lets you authenticate with GitLab using Basic authentication and Personal Access Token.

## Create GitLab Credentials using API token[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/credentials-store/gitlab-credentials\#create-gitlab-credentials-using-api-token)

**Prerequisite**:

- Create a [GitLab personal access token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#personal-access-token-scopes) with atleast the "read\_api" scope.

- Copy and save the personal access token.


1. Go to **Compute > Manage > Authentication > Credentials store**.

2. Select **Add credential**.









1. Enter a credential **Name**.

2. Enter a **Description**.

3. In **Type**, select **API token**.

4. Enter the API **Access token** from GitLab that you saved in the prerequisite section.

5. **Save** your changes.


[PreviousKubernetes Credentials](https://docs.prismacloud.io/admin-guide/authentication/credentials-store/kubernetes-credentials) [NextCloud Service Providers](https://docs.prismacloud.io/admin-guide/cloud-service-providers/cloud-service-providers)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject

For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/deployment-patterns/migration-options-for-scale-projects.md).

Starting in 20.12, Console has substantially increased the number of simultaneous Defenders it can support. Each instance of Console can support 10K Defenders. With this new capability, scale projects have been deprecated.

Scale projects gave security teams full control over policies for all application teams. If you’re currently using scale projects, we offer the following migration paths when upgrading to 20.12

## Migration paths[Direct link to heading](https://docs.prismacloud.io/admin-guide/deployment-patterns/migration-options-for-scale-projects\#migration-paths)

If you’re using scale projects, there are two ways you can migrate to a supported configuration.

**1\. Convert existing scale projects to tenant projects --**

When upgrading to 20.12, all existing scale projects will automatically be converted into tenant projects. Scale project policy rules will be converted to tenant project policy rules. From that point, any changes to the tenant project policies will only apply to the project itself, without any sync with Central Console.

If you choose this migration option, reevaluate the roles assigned to your users. After upgrading, users with the Admin, Operator, or Vulnerability Manager roles on the converted projects (now tenant projects) will have the ability to edit policy rules, so you might need to lower their privileges.

**2\. Unify the scale projects into Central Console --**

Before upgrading to 20.12, redeploy all scale project Defenders and connect them directly to Central Console. Use collections and RBAC to control which resources can be viewed and managed by different users (see example below).

If you have more than 10K Defenders, consider deploying more than one tenant project. To share policies between tenants, develop an automated process on top of the API to push policies from one Console to the other.

## Using collections[Direct link to heading](https://docs.prismacloud.io/admin-guide/deployment-patterns/migration-options-for-scale-projects\#using-collections)

Examples of how to use collections in your migration.

**Create a collection for a specific cluster:**

![create collections](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-583e830019420f9268bb9338a88f2fd17e9727e0%252Fcreate_collections.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=9e771bef3c826f676a709f8329199916&sv=3)

**Assign the collection to a user:**

![assign collections to user](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-60f2549a15022383937a7273da720347abcfee24%252Fassign_collections_to_user.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=b7cbae05960684e579d34b1505cc7c7c&sv=3)

**Collections can also be used when defining policies:**

![use collections in rules](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-eb1bbc8cdc09bbc361e45b133a179be38654a176%252Fuse_collections_in_rules.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=147d8269d66b75908bbb38c03e865b04&sv=3)

[PreviousProjects](https://docs.prismacloud.io/admin-guide/deployment-patterns/projects) [NextDNS and certificate management](https://docs.prismacloud.io/admin-guide/deployment-patterns/best-practices-dns-cert-mgmt)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject

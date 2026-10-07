For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/configure/tags.md).

Tags are predefined labels that can help you manage the vulnerabilities in your environment. They are centrally defined and can be set to vulnerabilities and as policy exceptions.

Tags are used as:

- Vulnerability labels. They provide a convenient way to categorize the vulnerabilities in your environment.

- Policy exceptions. They can be a part of your rules to have a specific effect on tagged vulnerabilities.


Tags are useful when you have large container deployments with multiple teams working in the same environment. For example, you might have different teams handling different types of vulnerabilities. Then you can set tags to define responsibilities over vulnerabilities. Other uses would be to set the status of fixing the vulnerability or to mark vulnerabilities to ignore when there are known problems that can’t be fixed in the near future.

For tags that are not used as policy exceptions, all user roles that can view the scan results and have the Collections and Tags permission, are allowed to assign these tags on CVEs. Assigning tags that are used as policy exceptions is allowed only for Admin, Operator, and Vulnerability Manager user roles. Custom roles aren’t allowed to set these tags, regardless of their other permissions.

## Tag definition[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/tags\#tag-definition)

You can define as many tags as you like.

1. To define a new tag, navigate to **Manage > Collections and Tags > Tags**.











Prisma Cloud ships with a predefined set of tags: Ignored, In progress, For review, and DevOps notes. The predefined tags are editable, and you can use them according to your needs.

2. Click **Add Tag**.

3. In the **Create new tag** dialog, enter a name and description.

4. Pick a color for easy visibility and differentiation.















![tags define tag](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-3b5d2fa319fa96cfa15f5ccecf218bc2f513a7b6%252Ftags_define_tag.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=ea5bca23b860bf9ac8384a07cd7c6f32&sv=3)

5. Click **Save**.


## Tag assignment[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/tags\#tag-assignment)

You can assign tags to vulnerabilities, and specify their scope based on CVE ID, packages and resources. Alternatively, you can manually tag vulnerabilities from [scan reports](https://docs.prismacloud.io/admin-guide/vulnerability-management/scan-reports).

Note that a tag assignment is uniquely identified by a tag, CVE ID, package scope, and resource type, therefore, you can not create multiple tag assignments for the same tag, CVE ID, package scope, and resource type. To extend the scope of a tag applied to a CVE, edit its existing tag assignment to apply to more packages or resources.

For example, assign the tag _Ignored_ to _CVE-2020-1971_, package _openssl_, and all _ubuntu_ images as follows:

![tags add tag assignment](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-7913ac8f2997f50856e1d2222c8036b0cd17c0ff%252Ftags_add_tag_assignment.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=330d4ddf83a47dda7c1d9630d403b904&sv=3)

You can also adjust the scope of a tag assigned either from the tags management page or from scan reports. Click the **Edit** button to start editing the tag assignment. For example, extend the scope of the tag _Ignored_ for _CVE-2020-1971_ to all packages affected by this CVE by changing the **Package scope**:

![tags edit tag assignment](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-e43a7e10c19a202f1d7af1b305634bd26559540b%252Ftags_edit_tag_assignment.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=b116bfb2b9032b19562df940bb76ac9f&sv=3)

As another example, after the _In progress_ tag was assigned to _CVE-2019-14697_ for specific _alpine_ images from the scan reports, you can extend its scope so it will apply to all _alpine_ images and their descendant images:

![tags assigned from scan reports](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-7e8b5042642f16df666e7b9c72b7d5243dc30012%252Ftags_assigned_from_scan_reports.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=d234d41d6cb954ceafef0392a475f79e&sv=3)

![tags specific images](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-33b3bf7893d11db10d36aebf3584cfd34a3d3a96%252Ftags_specific_images.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=99daadc1cd5124812d88e54651cca69f&sv=3)

![tags images with wildcard](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-cc3cad8ca0badc535a6ba0d562fb38819eaf30cc%252Ftags_images_with_wildcard.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=55e728e56a5515ff3e93902dad9aa576&sv=3)

To easily navigate in multiple tag assignments, use the table filters on the **Tag assignment** table. Filter by CVE ID, tag, package scope, and resource type to quickly find all places a tag applies to.

![tags filters a](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-9c130943d872c826dd13d1fff921a81ae0396833%252Ftags_filters_a.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=388c668e4a00c0e2e782c501d5eafe9b&sv=3)

![tags filters b](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-26766a59918ba7f04e2afeb56286f82d458bbb36%252Ftags_filters_b.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=5f58f7ec9589a66536c2eb46107bb836&sv=3)

01. To assign a tag to a vulnerability, navigate to **Manage > Collections and Tags > Tags**.

02. Click **Assign Tag**.

03. In **Tag**, select the tag to assign.

04. In **CVE**, select the CVE ID to assign the tag for.

05. In **Package scope**, select the package to which the tag should apply. You can select **All packages** to apply the tag to all the packages affected by the CVE.

06. In **Resource type**, select the type of resources to assign the tag for. You can select **All resources** to apply the tag to all the resources across your environment.











    VMware Tanzu droplets and running applications are being referenced as **Images**.

07. Once a resource type is selected, specify the resources to which the tag should apply under **Images**, **Hosts**, **Functions**, or **Code repositories**. Wildcards are supported.

08. (Optional) For images, turn on the **Tag descendant images** toggle to let Prisma Cloud automatically tag this CVE in all images where the base image is one of the images specified in the **Images** field.











    For Prisma Cloud to be able to tag descendant images, first identify the [base images](https://docs.prismacloud.io/admin-guide/vulnerability-management/base-images) in your environment under **Defend > Vulnerabilities > Images > Base images**.

09. (Optional) In **Comment**, specify a comment for this tag assignment.

10. Click **Save**.


[PreviousCollections](https://docs.prismacloud.io/admin-guide/configure/collections) [NextLogon Settings](https://docs.prismacloud.io/admin-guide/configure/logon-settings)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject

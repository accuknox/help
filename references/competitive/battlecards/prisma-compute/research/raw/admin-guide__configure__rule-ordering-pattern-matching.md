For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/configure/rule-ordering-pattern-matching.md).

Prisma Cloud supports pattern matching so that rules can be applied granularly. For example, you could apply a rule to any image with the name `ubuntu*`. Or you could apply a rule to all hosts, except those named `*test*`. This article describes how filtering and pattern matching works in Prisma Cloud.

## Pattern matching[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/rule-ordering-pattern-matching\#pattern-matching)

All rules have resource filters that let you precisely target specific parts of your environment. This is known as a rule’s _scope_. Scope is specified using [collections](https://docs.prismacloud.io/admin-guide/configure/collections). Rules reference collections to set their scope.

![rule ordering 763992](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-0f8491792fe1fb5f0555ec5b317b64c180c01f64%252Frule_ordering_763992.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=0104f13573ac101b664eb97092e4bd3c&sv=3)

The fields in a collection let you capture a segment of the resources in your environment based on container name, image name, host name, etc. By default, each field is populated with a wildcard. Wildcards capture all objects of a given type. Constrain the scope of a collection by specifying filters in one or more field.

You can customize how a field is evaluated with string matching. When Prisma Cloud encounters a wildcard in a resource name, it evaluates the resource name according to the position of the wildcard.

- If the string starts with a wildcard, it’s evaluated as _string-ends-with_.

- If the string terminates with a wildcard, it’s evaluated as _string-starts-with_.

- If a string is starts and terminates with a wildcard, it’s evaluated as _string-contains_.


For example, if you specify a resource filter of `*foo-resource*`, Prisma Cloud matches that resource to any value that contains the string, such as `example-foo-resource` and `foo-resource-1`. Matching logic is case insensitive.

![rule ordering 763994](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-488925542656086ba457ac4fcf0f2d2823a2342e%252Frule_ordering_763994.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=0adec9e312e5932f42f02690c918d2f1&sv=3)

Individual fields are combined using **AND** logic. In the following example, there are filters for hosts named `foo-hosts*` and images named `foo-images*`. There are no filters for containers or labels (they’re wildcards). If this collection were used to scope a rule, the effective result would be to **apply this rule anytime the host name starts with foo-hosts and image name starts with foo-images, regardless of the container name or label**.

![rule ordering 763995](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-daa531017510c9b1e77e0cd1cdcf66eeaf85ea96%252Frule_ordering_763995.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=c40cc6c5aba7a87489ce21b51d3e6111&sv=3)

If strings have no wildcards, Prisma Cloud exactly matches the value you enter against the resource string. This gives you precise control over which values match. For example:

- `*/ubuntu:latest` matches `/library/ubuntu:latest` or `docker.io/library/ubuntu:latest`.

- `*:latest` matches `ubuntu:latest` or `debian:latest`.

- If you want to explicitly target just `ubuntu:latest` from Docker Hub, use `docker.io/library/ubuntu:latest`. Because the value you provide is the complete name of the resource, Prisma Cloud matches it exactly.

- `*_test` matches `host_sandbox_test` and `host_preprod_test` but doesn’t match `host_test_server`.


![rule ordering 763996](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-09827c8d4c5b2843c4684aa7ee6aa977d4d58cec%252Frule_ordering_763996.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=28fbd7c97ced3d52c536e0f0086127e4&sv=3)

For DNS filtering, Prisma Cloud doesn’t prevent you from entering multiple wildcards per string, but it’s treated the same as if you simply entered the right-most wildcard. The following patterns are equivalent:

AskCopy

```
*.*.b.a == *.b.a
```

## Exemptions[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/rule-ordering-pattern-matching\#exemptions)

While basic string matching makes it easy to manage rules for most scenarios, you sometimes need more sophisticated logic. Prisma Cloud lets you exempt objects from a rule with the minus (`-`) sign (the NOT operator). From example, if you want a rule to apply to all hosts starting with `foo-hosts*`, except those starting with `foo-hosts-exempt*`, then you could create the following rule:

![rule ordering 763997](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-cf32f0f7010043cab13a8ccaa8c89031772764a2%252Frule_ordering_763997.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=91b520adebf5c91129eaa14b77267ce4&sv=3)

When Prisma Cloud evaluates an object against a rule with a NOT operator, it first skips any object for which there is a match with the exempted object. So, from our example:

1. If the host name starts with `foo-hosts-exempt`, skip the rule.

2. If the host name starts with `foo-hosts` AND the image name starts with `foo-images`, apply the rule.


All scope fields, in both policy rules and collection specs, support the NOT operator.

When using the NOT operator, remember that what’s being excluded can’t be broader than what’s included. For example, the following expression for scoping images is illogical:

AskCopy

```
-ngnix*, ngnix:latest
```

The following expression, however, is valid. It sets the scope to all NGINX images, and then excludes `nginx:latest` from the set.

AskCopy

```
ngnix*, -ngnix:latest
```

To exclude a single image from the universe, first use the NOT operator to omit the image. Then set the include scope with a wildcard.

AskCopy

```
-mongo:latest, *
```

## Rule ordering[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/rule-ordering-pattern-matching\#rule-ordering)

For any given feature area, such as vulnerability management or compliance, you might have multiple rules, such as _test 1_ and _test 2_.

![rule ordering two rules](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-45d1ad724fa954882b91b33db225bbf52b8451cb%252Frule_ordering_two_rules.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=e1ecf2fb3708d0469f7ae083f547409d&sv=3)

The entire set of rules in a given feature area is called the policy. The rules in the policy are evaluated from top to bottom, making it easy to understand how policy is applied. When evaluating whether to apply a rule to a given object, Prisma Cloud uses the following logic:

1. Does rule 1 apply to object? If yes, apply action(s) defined in rule and stop. If no, go to 2.

2. Does rule 2 apply to object? If yes, apply action(s) defined in rule and stop. If no, go to 3.

3. …​

4. Apply the built-in Default rule (unless it was removed or modified).


Prisma Cloud evaluates the rule list from top to bottom until it finds a match based on the object filters. When a match is found, it applies the actions in the rule and stops processing further rules. If no match is found, then no action is applied. Sometimes this could mean that an attempted action is blocked (e.g. if no access control rule is matched that allows a user to run a container).

To reorder rules, click on a rule’s hamburger button and drag it to a new position in the list.

![rule ordering drag and drop](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-29dacadaa6d75c9a6ad4daa1f9a35305d740f0f8%252Frule_ordering_drag_and_drop.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=b714552d41ead8182982d620b34e028f&sv=3)

## Disabling rules[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/rule-ordering-pattern-matching\#disabling-rules)

If you want to test how the system behaves without a particular rule, you can temporarily disable it. Disabling a rule gives you a way to preserve the rule and its configuration, but take it out of service, so that it’s ignored when Prisma Cloud evaluates events against your policy.

To disable a rule, click **Actions > Disable**.

![rule ordering disable rule](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-474303fa6e9ae2b21979cd1271543f2dffd2216e%252Frule_ordering_disable_rule.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=fe481930d23cf2c1fa0b60fe8d9a0a7c&sv=3)

## Image names[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/rule-ordering-pattern-matching\#image-names)

The canonical name of an image is it’s **full name** in a format like registry/repo/image-name. For example: `1234.dkr.ecr.us-east-1.amazonaws.com/morello:foo-images`. Within Docker itself, these canonical names can be seen by inspecting any given image, like this:

AskCopy

```
$ sudo docker inspect morello/foo-images | grep Repo -A 3
      "RepoTags": [\
          "1234.dkr.ecr.us-east-1.amazonaws.com/morello:foo-images",\
```\
\
However, there’s a special case to be aware of with images sourced from Docker Hub. For those images, the Docker Engine and client do not show the full path in the canonical name; instead it only shows the ‘short name’ that can be used with Docker Hub and the full name is implied. For example, compare the previous example of an image on AWS ECR, with this image on Docker Hub:\
\
AskCopy\
\
```\
$ sudo docker inspect morello/docker-whale | grep Repo -A 3\
      "RepoTags": [\
          "morello/docker-whale:latest",\
```\
\
Note that when the image is from Hub, the canonical name is listed as just the short name (the same name you could use with the Docker client to issue a command like ‘docker run morello/docker-whale’). For images like this, Prisma Cloud automatically prepends the actual address of the Docker Hub registry (docker.io) and, if necessary, the library repo name as well, even though these values are not shown by Docker itself.\
\
For example, you can run the Alpine image from Docker Hub simply by issuing a Docker client command like ‘docker run -ti alpine /bin/sh’. The Docker client automatically knows that this means to pull and run the image that has a canonical name of docker.io/library/alpine:latest. However, this full canonical name is not exposed by the Docker client when inspecting the image:\
\
AskCopy\
\
```\
$ sudo docker inspect alpine | grep Repo -A 2\
      "RepoTags": [\
          "alpine:latest"\
      ],\
      "RepoDigests": [\
          "alpine@sha256:1354db23ff5478120c980eca1611a51c9f2b88b61f24283ee8200bf9a54f2e5c"\
      ],\
```\
\
But because Prisma Cloud automatically prepends the proper values to compose the canonical name, a rule like this blocks images from Hub from running:\
\
![rule ordering 764008](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-81a08322c26417eafd7531fb9d5b7dd1d362e20e%252Frule_ordering_764008.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=f207b23a7c54f4a65a6c56e31537ffae&sv=3)\
\
AskCopy\
\
```\
$ docker -H :9998 --tls run -ti alpine /bin/sh\
docker: Error response from daemon: [Prisma Cloud] The command container_create denied for user admin by rule Deny - deny all docker.io images.\
```\
\
[PreviousConfigure](https://docs.prismacloud.io/admin-guide/configure/configure) [NextBackup and restore](https://docs.prismacloud.io/admin-guide/configure/disaster-recovery)\
\
Last updated 2 months ago\
\
Was this helpful?\
\
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).\
\
AcceptReject

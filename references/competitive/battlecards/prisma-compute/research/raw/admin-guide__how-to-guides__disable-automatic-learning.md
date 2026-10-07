For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/how-to-guides/disable-automatic-learning.md).

Prisma Cloud lets you disable automatic learning to give you full control over creating, managing, and maintaining runtime rules for your apps.

Disabling automatic runtime learning is strongly discouraged. Prisma Cloud has been architected and optimized to automatically learn known good runtime behaviors, then create models that explicitly allow those behaviors. Disabling learning requires creating manual rules for all of these behaviors and greatly increases the likelihood of encountering false positive events.

If you have a regimented deployment process that must guarantee consistency between your test environment and your production environment, then you might want to disable automatic runtime learning, and manually create runtime rules instead. With this approach, the full range of runtime behaviors is locked down in production, and cannot be extended without manually adding new rules.

## Models and learning[Direct link to heading](https://docs.prismacloud.io/admin-guide/how-to-guides/disable-automatic-learning\#models-and-learning)

When a model is created for an entity, it’s initially empty. Empty models don’t allow any runtime behaviors. In a default installation, Prisma Cloud uses machine learning to compose models that encapsulate all known good behaviors. Models are sets of rules that allow process, network, and file system activity.

When learning is disabled, newly created models are empty. Since empty models don’t allow any behaviors, you must manually create rules that explicitly allow process, network, and file system activity. Remember that rules come from two places: models (automatically created) and runtime rules (manually created). Manually created rules are designed to augment models when learning does not capture the full range of known good behaviors. When automatic learning is disabled, they must fully specify the full range of known good behaviors.

### Deploying Prisma Cloud[Direct link to heading](https://docs.prismacloud.io/admin-guide/how-to-guides/disable-automatic-learning\#deploying-prisma-cloud)

Models created before automatic learning is disabled might still contain learned content. To guarantee all models are empty, disable automatic learning before deploying Defenders to your environment.

1. Disable automatic learning.









1. On the Prisma Cloud Console, select **Defend > Runtime > Containers**.

2. Set the toggle off for **Enable automatic runtime learning**.


2. Deploy Defenders.


## Workflow[Direct link to heading](https://docs.prismacloud.io/admin-guide/how-to-guides/disable-automatic-learning\#workflow)

You should have two environments: test and production. Deploy Prisma Cloud Console to each environment. In the test environment, enable automatic learning. You’ll use automatic learning to assist with the creation of rules. In the production environment, disable automatic learning. You’ll port the rules from the test environment to the production environment.

The recommended workflow is:

1. Deploy your app to the test environment, and fully exercise it.

2. Validate models that were automatically created.

3. Export models from the test environment as rules.

4. Optionally store the rules in a source control system.

5. Import the rules into your production environment, where automatic learning is disabled.


## Exporting and importing rules from the Console UI[Direct link to heading](https://docs.prismacloud.io/admin-guide/how-to-guides/disable-automatic-learning\#exporting-and-importing-rules-from-the-console-ui)

After your app has been fully exercised in the test environment, create a rule from the runtime model. In **Monitor > Runtime > Container Models**, find your model, click **Actions**, then click **Copy Into Rule**.

![disable automatic learning copy into rule](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-70cccc506c0525bb6020e75c40824772751a23f6%252Fdisable_automatic_learning_copy_into_rule.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=cafe51a85e75def05d4a89d97e79f4d6&sv=3)

Next, download the rule in JSON format. Go to **Defend > Runtime > Container Policy**, find your rule, and in the **Actions** menu, click **Export**.

![disable automatic learning export](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-e740aeb820bbee855e2a53574cb50ad1ad509542%252Fdisable_automatic_learning_export.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=e13876904e5a93b9e6b03d0c3eff3084&sv=3)

Finally, import your rule into Console in your production environment. Go to **Defend > Runtime > Container Policy**, and click **Import rule**.

## Exporting and importing rules programmatically[Direct link to heading](https://docs.prismacloud.io/admin-guide/how-to-guides/disable-automatic-learning\#exporting-and-importing-rules-programmatically)

After your app has been fully exercised in the test environment, retrieve the model as a runtime rule. Use the _GET /profiles/container/{id}/rule_ endpoint, where _{id}_ is the profile ID.

A list of profiles (models) can be retrieved from _GET /api/v1/profiles/container_. Profile IDs can be found in the \_id field. Profile ID is simply the concatenation of the image ID and an underscore.

AskCopy

```
$ curl -k \
  -u ian \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<TEST-CONSOLE>:8083/api/v1/profiles/container/{id}/rule \
  | jq '.' > model_rules.json
```

Then push the rule to Console in your production environment. When a rule is pushed with this endpoint, it is ordered first in the policy. Rule order is important, so be sure you’re pushing rules in the right order. The version of Console where the rule was exported must match the version of Console where it’s imported.

AskCopy

```
$ curl -k \
  -u <USER> \
  -X POST \
  -H "Content-Type:application/json" \
  https://<PROD-CONSOLE>:8083/api/v1/policies/runtime/container \
  --data-binary "@model_rules.json"
```

The _POST /api/v1/policies/runtime/container_ endpoint pushes one rule at a time. The _PUT /api/v1/policies/runtime/container_ endpoint pushes the entire policy (i.e. all rules) in a single shot.

[PreviousProvision tenant projects OpenShift](https://docs.prismacloud.io/admin-guide/how-to-guides/openshift-provision-tenant-projects) [NextReview debug logs](https://docs.prismacloud.io/admin-guide/how-to-guides/review-debug-logs)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject

> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/runtime-security/runtime-defense/disable-automatic-learning.md).

# Disable Automatic Learning

Prisma Cloud lets you disable automatic learning to give you full control over creating, managing, and maintaining runtime rules for your apps.

Disabling automatic runtime learning is strongly discouraged. Prisma Cloud has been architected and optimized to automatically learn known good runtime behaviors, then create models that explicitly allow those behaviors. Disabling learning requires creating manual rules for all of these behaviors and greatly increases the likelihood of encountering false positive events.

If you have a regimented deployment process that must guarantee consistency between your test environment and your production environment, then you might want to disable automatic runtime learning, and manually create runtime rules instead. With this approach, the full range of runtime behaviors is locked down in production, and cannot be extended without manually adding new rules.

## Models and learning

When a model is created for an entity, it’s initially empty. Empty models don’t allow any runtime behaviors. In a default installation, Prisma Cloud uses machine learning to compose models that encapsulate all known good behaviors. Models are sets of rules that allow process, network, and file system activity.

When learning is disabled, newly created models are empty. Since empty models don’t allow any behaviors, you must manually create rules that explicitly allow process, network, and file system activity. Remember that rules come from two places: models (automatically created) and runtime rules (manually created). Manually created rules are designed to augment models when learning does not capture the full range of known good behaviors. When automatic learning is disabled, they must fully specify the full range of known good behaviors.

### Deploying Prisma Cloud

Models created before automatic learning is disabled might still contain learned content. To guarantee all models are empty, disable automatic learning before deploying Defenders to your environment.

1. Disable automatic learning.
   1. On the Prisma Cloud Console, select **Defend > Runtime > Containers**.
   2. Set the toggle off for **Enable automatic runtime learning**.
2. Deploy Defenders.

## Workflow

You should have two environments: test and production. Deploy Prisma Cloud Console to each environment. In the test environment, enable automatic learning. You’ll use automatic learning to assist with the creation of rules. In the production environment, disable automatic learning. You’ll port the rules from the test environment to the production environment.

The recommended workflow is:

1. Deploy your app to the test environment, and fully exercise it.
2. Validate models that were automatically created.
3. Export models from the test environment as rules.
4. Optionally store the rules in a source control system.
5. Import the rules into your production environment, where automatic learning is disabled.

## Exporting and importing rules from the Console UI

After your app has been fully exercised in the test environment, create a rule from the runtime model. In **Monitor > Runtime > Container Models**, find your model, click **Actions**, then click **Copy Into Rule**.

<figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-70cccc506c0525bb6020e75c40824772751a23f6%2Fdisable-automatic-learning-copy-into-rule.png?alt=media" alt="disable automatic learning copy into rule"><figcaption></figcaption></figure>

Next, download the rule in JSON format. Go to **Defend > Runtime > Container Policy**, find your rule, and in the **Actions** menu, click **Export**.

<figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-e740aeb820bbee855e2a53574cb50ad1ad509542%2Fdisable-automatic-learning-export.png?alt=media" alt="disable automatic learning export"><figcaption></figcaption></figure>

Finally, import your rule into Console in your production environment. Go to **Defend > Runtime > Container Policy**, and click **Import rule**.

## Exporting and importing rules programmatically

After your app has been fully exercised in the test environment, retrieve the model as a runtime rule. Use the *GET /profiles/container/{id}/rule* endpoint, where *{id}* is the profile ID.

A list of profiles (models) can be retrieved from *GET /api/v1/profiles/container*. Profile IDs can be found in the \_id field. Profile ID is simply the concatenation of the image ID and an underscore.

```
$ curl -k \
  -u ian \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<TEST-CONSOLE>:8083/api/v1/profiles/container/{id}/rule \
  | jq '.' > model_rules.json
```

Then push the rule to Console in your production environment. When a rule is pushed with this endpoint, it is ordered first in the policy. Rule order is important, so be sure you’re pushing rules in the right order. The version of Console where the rule was exported must match the version of Console where it’s imported.

```
$ curl -k \
  -u <USER> \
  -X POST \
  -H "Content-Type:application/json" \
  https://<PROD-CONSOLE>:8083/api/v1/policies/runtime/container \
  --data-binary "@model_rules.json"
```

The *POST /api/v1/policies/runtime/container* endpoint pushes one rule at a time. The *PUT /api/v1/policies/runtime/container* endpoint pushes the entire policy (i.e. all rules) in a single shot.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/runtime-security/runtime-defense/disable-automatic-learning.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

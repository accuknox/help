For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-custom-rules.md).

WAAS custom rules offer an additional mechanism to protect your running web apps. Custom rules are expressions that give you a precise way to describe and detect discrete conditions in requests and responses. WAAS intercepts layer 7 traffic, passes it to Prisma Cloud for evaluation. Expressions let you inspect various facets of requests and responses in a programmatic way, then take action when they evaluate to true. Custom rules can be used in container, host, and app-embedded WAAS policies.

Besides your own custom rules, Prisma Labs ships and maintains rules for newly discovered threats. These system rules are distributed via the Intelligence Stream. By default, they are shipped in a disabled state. You can review, and optionally activate them at any time. System rules cannot be modified. However, you can clone and customize them to fit your own specific needs.

Before using custom rules, ensure Console and Defender run the same version of Prisma Cloud Compute. The minimum required version for a Defender appears when you add a custom rule to a policy. For example, if a Console runs a newer version, but Defenders have not been upgraded, using functionality only available in the newer version will result in a WAAS error. If this occurs, upgrade Defenders to match their Console’s version.

## Expression grammar[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-custom-rules\#expression-grammar)

Expressions let you examine the contents of requests and responses. The grammar lets you inspect various properties in an event. For example, you could write an expression that determines if an IP address falls inside a specific CIDR block.

Expressions support the following types:

- String.

- String list.

- String map.

- Integer.

- IP address (e.g. "192.168.0.1")

- CIDR block (e.g. "192.168.0.0/16")


Expressions have the following grammar:

`term (op term | in | )*`

term
`integer | string | keyword | event | '(' expression ')' | unaryOp`

op
`and | or | > | < | >= | ⇐ | = | !=`

in
`'(' integer | string (',' integer | string)*)?`

Can also be used to determine if an IP address is in a CIDR block: For example:

`req.ip in "192.168.0.0/16"`

unaryOp
`not`

keyword (similar to wildcards)
`startswith | contains`

`contains` can be used for:

- Equality. For example: `req.header_names contains "X-Forwarded-For"`

- Regular expression match for string lists. For example: `req.header_names contains /^X-Forwarded.*/`

- Regular expression match for strings. For example: `req.body contains /^some-regex-text.*/`


string
Strings must be enclosed in double-quotes.

integer
`int`

event
`req | resp`

\[ \]
Selector operator. Selects a specific value by key from a map. Headers, cookies, body params, and query params are maps. The selection operation template is as following:

`req.<map>["<key>"]`

For example:

`req.headers["Content-Type"] contains "text/html"`

### Request events[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-custom-rules\#request-events)

Expressions can examine the following attributes of a request:

Attribute

Minimum Defender version

Type

Example

req.host

22.06

Map of String

`req.host contains /^.*ACME[1-9]{1,6}$/`

req.headers (for matching on "Host" header use req.host)

21.04

Map of String

`req.headers["User-Agent"] contains /^.*ACME[1-9]{1,6}$/`

req.header\_names

21.04

String List

`req.header_names contains /^X-Forwarded.*/`

req.header\_values

21.04

String List

`req.header_values contains "secretkey"`

req.cookies

21.04

Map of String

`req.cookies["yummy-cookie"] contains "flour"`

req.cookie\_names

21.04

String List

`req.cookie_names contains "ga"`

req.cookie\_values

21.04

String List

`req.cookie_values contains "admin"`

req.query\_params

21.04

Map of String

`req.query_params["id"] contains "admin"`

req.query\_param\_names

21.04

String List

`req.query_param_names contains "ssn"`

req.query\_param\_values

21.04

String List

`req.query_param_values contains /\d{3}-?\d{2}-?\d{4}/`

req.body\_param\_values

21.04

String List

`req.body_param_values contains "username"`

req.http\_method

21.04

String

`req.http_method = "POST"`

req.file\_extension

21.04

String

`req.file_extension contains /pdf$/`

req.path

21.04

String

`req.path startswith "/admin/"`

req.ip

21.04

IP (written as string, parsed as IP if IP is valid)

`req.ip in "2.2.2.0/24" or req.ip = "8.8.8.8"`

req.country\_code

21.04

String

`req.country_code = "US"`

req.body

21.04

String

`req.body contains /password/`

req.http\_version

21.04

String

`req.http_version = "1.0"`

req.http\_scheme

21.04

String

`req.http_scheme = "HTTPS"`

When gRPC is enabled, the `req.body` attribute may not be able to properly match on the body content if it is sent in binary form.

### Response events[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-custom-rules\#response-events)

Expressions can examine the following attributes of a response.

To examine server responses in custom rules, the rule type must be set to `waas-response`

![waas response custome rule type](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-8caca528dd0c064c41f11786b5fe88561b826e10%252Fwaas_response_custome_rule_type.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=b25b5794a07be55080d11bea0cf46eec&sv=3)

Attribute

Minimum Defender version

Type

Example

resp.status\_code

21.04

Integer

`resp.status_code = 200`

resp.content\_type

21.08

String

`resp.content_type = "application/json"`

resp.body

21.08

String

`resp.body contains /^somesecret$/`

resp.headers

21.08

Map of String

`resp.headers["Set-Cookie"] contains /SESSIONID/`

resp.header\_names

21.08

String List

`resp.header_names contains "Set-Cookie"`

resp.header\_values

21.08

String List

`resp.header_values contains "ERROR"`

When gRPC is enabled, the `resp.body` attribute may not be able to properly match on the body content if it is sent in binary form.

### Transformation functions[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-custom-rules\#transformation-functions)

The following transformations are available to users creating custom rules:

- **lowercase** \- converts all characters to lowercase.

- **compressWhitespace** \- converts whitespace characters (32, \\f, \\t, \\n, \\r, \\v, 160) to spaces (32) and then compresses multiple space characters into only one.

- **removeWhitespace** \- removes all whitespace characters.

- **urlQueryDecode** \- decodes URL query string.

- **urlPathDecode** \- decodes URL path string (identical to **urlQueryDecode** except that it does not unescape `+` to space).

- **unicodeDecode** \- normalizes unicode characters to their closest resemblance in ASCII format.

- **htmlEntityDecode** \- decodes HTML components in a given string.

- **base64Decode** \- decodes a base64-encoded string.

- **replaceComments** \- replaces each occurrence of a C-style comments (/\* …​ \*/) with a single space (multiple consecutive occurrences of a space will not be compressed).

- **removeCommentSymbols** \- removes each comment symbol (/\*, \*/) from a string.

- **removeTags** \- replaces encoded tag entities (`&lt;`, `&gt;`) with a single whitespace.


### JWT parsing functions[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-custom-rules\#jwt-parsing-functions)

- `jwtPayload(<JWT string>)` \- returns a string representing the payload section of the JWT (simply the whole second part of the token, base64url decoded).


`jwtPayload(req.headers["Authorization"]) contains /pattern/`

- `jwtPayloadValue(<JWT string>, <payload key>)` \- returns the string value associated with a key inside the payload section of the given JWT.


To inspect if a string value associated with a key say "email\_verified" is set to "false", use the following expression: `jwtPayloadValue(req.headers["Authorization"], "email_verified") contains /^false$/`

- `jwtHeader(<JWT string>)` \- returns a string representing the header section of the JWT.

- `jwtHeaderValue(<JWT string>, <header key>)` \- returns the string value associated with a key inside the header section of the given JWT.


For example, to check if the key "kid" contains the value matching a pattern: `jwtHeaderValue(req.headers["Authorization"], "kid") contains /\.\.[\\\/]/`

- `jwtValid(<JWT string>)` \- returns a boolean value which is true only if the input argument represents a JWT, and this JWT passed the following checks:


For example: `(not jwtValid(req.headers["Authorization"])) or jwtHeaderValue(req.headers["Authorization"], "alg") contains /^none$/`

- If the JWT is signed with a standard algorithm with a fixed-length output, the signature of the JWT should be of that known length.

- If the JWT is signed with a standard symmetric-key algorithm, the header of the JWT does not contain a parameter that is meant to be used only with asymmetric algorithms (e.g. parameters used to identify a public key that is used to verify the JWT’s signature).

- The JWT has not expired - check when the 'exp' (Expiration Time) claim is present.

- The JWT’s has already been issued (issue time < current time) - checked when the 'iat' (Issued At) claim is present.

- The JWT has already become valid ("not valid before" time < current time) - checked when the 'nbf' (Not Before) claim is present.


The WAAS events for JWT custom rule violations are generated under **Monitor > Events > WAAS for containers/hosts**, with the attack type as **Custom Rule**.

![waas events jwt](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-0916c3b181767d503bc36228150fc14449cbe45e%252Fwaas-events-jwt.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=8e8b06b18d8f75a68f5640850451193e&sv=3)

**Limitations**:

- **No signature verifications**: The signature part of JWT is not verified. This verification should be handled by the application receiving the token.

- **Encrypted JWTs are not supported**: The Encrypted Java Webtokens (JWEs) are not handled.


### Effects[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-custom-rules\#effects)

The following effects may be applied on HTTP requests/responses that match a WAAS custom rule:

- **Allow** \- The request is passed to the protected application, all other detections are not applied (e.g app firewall, bot protection, API protection, etc.). No audit is generated.

- **Alert** \- The request is passed to the protected application and an audit is generated for visibility.

- **Prevent** \- The request is denied from reaching the protected application, an audit is generated and WAAS responds with an HTML page indicating the request was blocked.

- **Ban** \- Can be applied on either IP or [Prisma Session IDs](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-advanced-settings#prisma-session). All requests originating from the same IP/Prisma Session to the protected application are denied for the configured time-period (default is 5 minutes) following the last detected attack.


A message at the top of the page indicates the entity by which the ban will be applied (IP or Prisma Session ID). When the X-Forwarded-For HTTP header is included in the request headers, the ban will apply based on the first IP listed in the header value (true client IP). For custom rules defined in **Out-of-Band**, only **Allow** and **Alert** effects are allowed.

### Example expressions[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-custom-rules\#example-expressions)

The following examples show how to use the expression grammar:

- Special expression to determine if an IP address falls within a CIDR block:


`req.ip in "192.168.0.0/16"`

- Example of using a regular expression:


`req.header_names contains /^X-Forwarded.*/`

- Determine if the request method matches a method in the array. Currently, you can only create custom arrays as part of the `in` operator.


`req.http_method in ("POST", "PUT")`

- Example of using `contains`:


`req.header_values contains "text/html"`

- Example using a selector:


`req.cookies["yummy-cookie"] contains "flour"`

- Example of an expression with three conditions. All conditions must evaluate to true for there to be a match.


`req.http_method = "POST" and resp.status_code >= 400 and resp.status_code ⇐ 599`

- Example for detecting HTTP 1.0 requests sent to a path starting with /api/control/ with an "admin" cookie whose Base64 decoded value is set to "True".


``req.http_version = "1.0" and lowercase(req.path) startswith "/api/control/" and base64Decode(req.cookies["admin"]) contains /^True$/```

- Example for detecting successful login requests by checking the Set-Cookie header value using chained transformation functions.


``req.http_method = "POST" and resp.status_code = 200 and compressWhitespace(base64Decode(resp.headers["Set-Cookie"])) contains /SESSIONID/```

## Write a WAAS custom rule[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-custom-rules\#write-a-waas-custom-rule)

Expression syntax is validated when you save a custom rule.

1. Open Console, and go to **Defend > WAAS** \> **{Container \| Host \| App-Embedded \| Agentless} > {In-line \| Out-Of-Band}**.

2. Click **Add rule**.

3. Enter a name for the rule.

4. In **Message**, enter an audit message to be emitted when an event matches the condition logic in this custom rule.











Use the following syntax to view the matched groups: <Your text>: %regexMatches











Refer to the following screenshot:















![waas custom rule regex match group](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-47072232988685538c7c3b2ea6804badfb22c97a%252Fwaas_custom_rule_regex_match_group.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=34b59472c0a4805cb22b2c0334c1de61&sv=3)

5. Select the rule type.











You can write expressions for requests or responses. What you select here scopes the vocabulary available for your expression.

6. Enter your expression logic.











Press `OPTION` \+ `SPACE` to get a list of valid terms, expressions, operators, etc, for the given position.











Use the example expressions [here](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-custom-rules#examples) as a starting point for your own expression.

7. Click **Save**.











Your expression logic is validated before it is saved to the Console’s database.


## Activate WAAS custom rules[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-custom-rules\#activate-waas-custom-rules)

A custom rule is made up of one or more conditions. Attach a custom rule to a WAAS policy rule to activate it.

Custom rules are defined in **Defend > Custom rules > WAAS**. WAAS policy rules are defined in **Defend > WAAS > {Container \| Host \| App-Embedded \| Agentless} > {In-line \| Out-Of-Band}**.

When attaching a custom rule to a WAAS policy rule, you specify the action to be taken when the expression evaluates to true (i.e. the expression matches). Supported actions for In-line WAAS policy are Disable, Allow, Alert, Prevent, and Ban. For Out-Of-Band/Agentless the only actions available are Disable, Allow, and Alert.

Custom rules have priority over all other enabled WAAS protections. WAAS evaluates all custom rules that are attached, so you can get more than one audit if more than one custom rule matches.

**Prerequisites:** You have already set up WAAS to protect an app, and there’s a rule for it under **Defend > WAAS > {Container \| Host \| App-Embedded \| Agentless} > {In-line \| Out-Of-Band}**. For more information about setting up an app, see [Deploy WAAS](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/waas/deploy-waas/deploy-waas.md).

1. Open Console, and go to **Defend > WAAS > {Container \| Host \| App-Embedded \| Agentless} > {In-line \| Out-Of-Band}**.

2. Select a rule under **App list**.

3. **Add app** and then go to **Custom rules**.

4. Select the effects to **Auto-apply virtual patches** to known CVEs vulnerabilities as detected by Prisma Cloud. The effect will be applied on HTTP requests/responses that match a WAAS custom rule.











In addition to selecting the global effect for applying the virtual patch, you can also override the default effects by selecting **user-selected custom rules** that are always applied regardless of the global auto-apply virtual patch under **Defend > WAAS > Container/Host/Agentless/App-embedded > {In-Line/Out-Of-Band}**.











The **Auto-apply virtual patches** are only applicable if the minimum Defender version is Kepler or greater.

5. **Select rules** from the predefined list of custom rules and click **Apply**. Alternatively, you can also create your own custom rules, with **Add rule**.









1. A list of available WAAS custom rules is displayed. Whenever a user creates a rule, the **owner** column is populated with the username. The owner column of virtual patches provided by Unit-42 researchers will have the value `system`.

2. The minimum supported Defender version appears when you add the custom rule to a policy.















      ![waas custom rules min defender](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-8220eaefd9a7b2812f30af8a238c1e4266249b63%252Fwaas_custom_rules_min_defender.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=be4976a3acb37cddc03a953bb6445bca&sv=3)


6. Configure the effect for each custom rule.











By default, the effect is set to **Alert**.

7. Click **Save**.


[PreviousAPI definition scan](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/api-def-scan) [NextUnprotected web apps](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/unprotected-web-apps)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject

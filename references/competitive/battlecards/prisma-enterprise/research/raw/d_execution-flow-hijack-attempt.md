> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/runtime-security/runtime-defense/incident-types/execution-flow-hijack-attempt.md).

# Execution Flow Hijack Attempt

An execution flow hijack attempt incident indicates that a possible attempt to hijack a program execution flow was observed. Special Linux library system files, which have a system-wide effect, were altered (this is usually undesirable, and is typically employed only as an emergency remedy or maliciously).

## Investigation

The following incident shows that the binary *sudo* wrote to *ld.so.preload* file, which is a special Linux system file that impacts the entire system. By editing the Linux dynamic loader or files relied upon by the loader such as *ld.so.preload*, the attacker can inject malicious code to any binary execution.

For further information about these files, see the following [link](https://man7.org/linux/man-pages/man8/ld.so.8.html).

<figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-6d83c8df76083bf7a51e3a61e1de50e88ceafc8e%2Fexecution-flow-hijack-attempt-incident.png?alt=media" alt="execution flow hijack attempt incident"><figcaption></figcaption></figure>

Your investigation should focus on:

* Determining the process that opened the Special Linux file.
* If the source of the alteration was an interactive process (such as shell), determine how an attacker gained access to that process.
* Review the forensics date for the host, other entries in the Incident Explorer, and audits from the source, looking for unusual process execution, hijacked processes, and explicit execution of commands.

## Mitigation

A full mitigation strategy for this incident begins by resolving the issues that allowed the attacker to access and modify the system file.

In addition, track the change that was done to the configuration in the system file. For example, in case of detected modification to the *ld.so.preload* file, look for the shared library that was added to the file and determine the source of this malicious shared library.

Ensure that compliance benchmarks are appropriately applied to the affected resources. For example, if the critical file systems in the host are mounted read-only, it will be more difficult for an attacker to change system files and configurations to their advantage.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/runtime-security/runtime-defense/incident-types/execution-flow-hijack-attempt.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

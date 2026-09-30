# Lovable Prompt, AccuKnox Threat Modeler v1

Paste everything inside the fence into Lovable as the first message. It is one prompt on purpose. Lovable builds the whole app from it, and the rule table and the TypeScript types stop it from guessing.

````text
Build "AccuKnox Threat Modeler", a browser-only threat modeling tool that works like the Microsoft Threat Modeling Tool (MSTMT). The user draws a data flow diagram (DFD), clicks Analyze, and gets a list of STRIDE threats. The user triages each threat and exports the list as CSV or SARIF 2.1.0.

# 1. Hard constraints (read first)

- Frontend only. Do NOT add Supabase, auth, login, a database, or any backend. All data lives in the browser (localStorage).
- Stack: React + Vite + TypeScript + Tailwind + shadcn/ui. Use @xyflow/react (React Flow v12) for the canvas. Use zustand for state with the persist middleware, and zundo for undo/redo. Use lucide-react icons. Use papaparse for CSV. Use sonner for toasts.
- The threat engine is a pure TypeScript module with no React imports: src/engine/. It takes a Model and returns Threat[]. It must be deterministic: the same diagram always gives the same threats with the same IDs in the same order.
- Do not call any network API except the AccuKnox client in section 9, and that client runs in "mock" mode by default.
- Desktop first (min width 1280px). On a narrow screen, show a notice "Open on a desktop to edit diagrams" but still let the user view the threat list.
- Light and dark theme, following the system setting, with a toggle in the top bar.

# 2. Routes

- "/" Home. Lists saved models (name, last modified, threat count). Buttons: "New model", "Open sample model", "Import .tm.json". Each row has Open, Duplicate, Delete (with a confirm dialog).
- "/model/:id" Editor. Has two views, Design and Analysis, switched by a segmented control in the top bar (like MSTMT's Design and Analyze buttons).

# 3. Data model (use these types exactly, in src/engine/types.ts)

```ts
export type ElementKind = "process" | "external" | "store" | "boundary";

export type Subtype =
  // process
  | "Generic Process" | "Web Application" | "Web Server" | "Web Service"
  | "Browser Client" | "Thick Client" | "Native Application" | "Managed Application"
  | "Container Workload" | "Serverless Function"
  // external
  | "Generic External Entity" | "Human User" | "Browser" | "External Web Service"
  | "External Web Application" | "Authorization Provider"
  // store
  | "Generic Data Store" | "SQL Database" | "Non Relational Database" | "File System"
  | "Cloud Storage" | "Cache" | "Configuration File" | "Log Store" | "Secrets Store"
  // boundary
  | "Generic Trust Boundary" | "Internet Boundary" | "Machine Boundary"
  | "Corporate Network Boundary" | "Kubernetes Namespace" | "Cloud VPC" | "Sandbox";

export type Protocol = "Generic" | "HTTP" | "HTTPS" | "gRPC" | "IPsec" | "Binary"
  | "Named Pipe" | "SMB" | "RPC" | "UDP" | "Message Queue";

export interface ElementProps {
  // all elements except boundary
  outOfScope: boolean;
  outOfScopeReason: string;
  description: string;
  // process only
  implementsAuthenticationScheme?: boolean;
  implementsCustomAuthorization?: boolean;
  implementsCommunicationProtocol?: boolean;
  codeType?: "Managed" | "Unmanaged";
  hasInputSanitizers?: boolean;   // Web Application, Web Server only
  hasOutputSanitizers?: boolean;  // Web Application, Web Server only
  // external only
  authenticatesItself?: boolean;
  isManagedIdentityProvider?: boolean; // Authorization Provider only
  // store only
  storesLogData?: boolean;
  storesCredentials?: boolean;
}

export interface DfdElement {
  id: string;             // nanoid
  kind: ElementKind;
  subtype: Subtype;
  name: string;
  position: { x: number; y: number };
  size?: { width: number; height: number }; // boundary only
  props: ElementProps;
}

export interface FlowProps {
  protocol: Protocol;
  authenticatesSource: boolean;
  authenticatesDestination: boolean;
  providesConfidentiality: boolean;
  providesIntegrity: boolean;
  carriesJSON: boolean;
  carriesXML: boolean;
  csrfProtection: boolean;
  outOfScope: boolean;
  outOfScopeReason: string;
  description: string;
}

export interface DataFlow {
  id: string;
  name: string;
  sourceId: string;   // never a boundary
  targetId: string;   // never a boundary, never equal to sourceId
  props: FlowProps;
}

export type Stride = "Spoofing" | "Tampering" | "Repudiation"
  | "Information Disclosure" | "Denial of Service" | "Elevation of Privilege";
export type Priority = "High" | "Medium" | "Low";
export type ThreatStatus = "Not Started" | "Needs Investigation" | "Not Applicable" | "Mitigated";

export interface Threat {
  id: string;            // `${ruleId}:${flowId}`, stable across re-analysis
  ruleId: string;        // e.g. "TMT-S01"
  title: string;         // template filled with names
  category: Stride;
  description: string;   // template filled with names
  priority: Priority;    // starts at rule default, user can change
  status: ThreatStatus;  // starts "Not Started"
  justification: string; // user text, "Justification / mitigation"
  flowId: string;
  sourceId: string;
  targetId: string;
  interaction: string;   // `${source.name} -> ${flow.name} -> ${target.name}`
  stale: boolean;        // rule no longer fires but the user edited it
  read: boolean;         // MSTMT "read indicator"
  userEdited: boolean;   // true once priority/status/justification changes
  remote?: {             // filled by AccuKnox push/sync, section 9
    findingId?: string;
    status?: string;
    notes?: string;
    lastSyncedAt?: string;
  };
}

export interface Model {
  schemaVersion: 1;
  id: string;
  name: string;
  owner: string;
  description: string;
  framework: "STRIDE";
  elements: DfdElement[];
  flows: DataFlow[];
  threats: Threat[];
  notes: string;
  lastAnalyzedAt?: string;
  diagramHashAtAnalysis?: string; // hash of elements+flows, for the "stale analysis" banner
  createdAt: string;
  updatedAt: string;
}
```

Defaults: every boolean is false. codeType defaults to "Managed". A new flow gets protocol "HTTPS". When the protocol is set to HTTPS or IPsec, set providesConfidentiality and providesIntegrity to true. When the protocol changes to anything else, set both to false. The user can still edit both toggles afterwards.

# 4. Design view layout

- Top bar: back to Home, model name (inline editable), Design | Analysis toggle, Undo, Redo, Save file (.tm.json download), Export menu (CSV, SARIF, Model JSON), AccuKnox menu (Push findings, Sync, Settings), theme toggle.
- Left panel "Stencils", 240px: search box, then four collapsible groups (Process, External Entity, Data Store, Trust Boundary) listing every subtype from section 3. Drag a stencil onto the canvas to create an element of that subtype, named "<Subtype> <n>" (for example "Web Application 1").
- Center: React Flow canvas with dot background, MiniMap, Controls, snap to grid 16px, fitView on load.
- Right panel "Properties", 300px: shows the selected element or flow. Fields: Name, Subtype (select, same kind only), Description, then every prop that applies to that kind and subtype as a labeled Switch, then "Out of scope" switch and "Reason for out of scope" textarea (shown only when out of scope is on). For a flow, show Protocol select and all FlowProps. With nothing selected, show model fields: name, owner, description.
- Bottom panel, 180px, collapsible, two tabs like MSTMT: "Messages" (validation, section 6) and "Notes" (a free textarea saved to model.notes).

Node shapes (follow classic DFD notation, like MSTMT):
- process: circle, 110px, name centered.
- external: rectangle, 150x70, square corners.
- store: two horizontal parallel lines top and bottom, no side borders, 160x60.
- boundary: dashed red (#dc2626) rectangle, transparent fill, resizable with NodeResizer, name in the top-left corner, rendered BELOW other nodes (zIndex -1), not connectable. Boundaries can overlap and nest.
- Out-of-scope elements render at 40% opacity with a small "OOS" badge.
- Each non-boundary node has 4 handles (top, right, bottom, left). Use ConnectionMode.Loose so any handle can start or end a flow.

Edges (flows): directed, arrow marker at the target end, smoothstep path, label "<flow name> (<protocol>)". A new flow is named "Flow <n>". Reject a connection to self or to a boundary. Two flows with the same source and target are allowed (request and response are drawn as two flows, like MSTMT).

Interactions: Delete/Backspace removes the selection (deleting a node deletes its flows). Ctrl+Z / Ctrl+Shift+Z undo and redo (zundo, ignore pure selection changes). Ctrl+D duplicates the selected node. Right-click on the canvas opens a menu to add a generic Process, External Entity, Data Store, or Trust Boundary at that point.

Autosave: persist the model to localStorage 500ms after the last change. Keys: "tmt:index:v1" (list of {id, name, updatedAt, threatCount}) and "tmt:model:v1:<id>".

# 5. Trust boundary crossing (the engine needs this)

A boundary contains an element when the element's center point lies inside the boundary rectangle (use position + size, React Flow positions are top-left). Compute the set of boundary IDs that contain the source and the set that contains the target. A flow "crosses" a boundary when those two sets are different. Put this in src/engine/geometry.ts as `crossesBoundary(model, flow): boolean` and `containingBoundaries(model, elementId): string[]`. Do not use React Flow parent nodes for this. Geometry only.

# 6. Validation messages (bottom "Messages" tab, recomputed on every change)

- ERROR: flow with a missing source or target element.
- WARNING: element with no flows ("<name> is not connected to any data flow").
- WARNING: two elements share the same name.
- WARNING: out-of-scope element or flow with an empty reason.
- INFO: the model has no trust boundary, so no boundary-crossing threats will be generated.
- INFO: no flow crosses any boundary.
Clicking a message selects and centers the element or flow.

# 7. Threat engine (src/engine/stride.ts)

`analyze(model: Model): Threat[]`

For every flow in model.flows (sorted by flow id), resolve source, target, and `crosses`. Skip the flow when the flow, the source, or the target is out of scope. Then evaluate every rule below in table order. When a rule's Include is true and its Exclude is false, create a threat. Fill {source}, {target}, {flow} in title and description with the element and flow names.

Notation: src = source element, tgt = target element, flow = the data flow. `src is process` means src.kind === "process". `crosses` is from section 5. A prop condition such as `flow.providesConfidentiality` means the boolean is true.

| Rule | STRIDE | Priority | Title | Include | Exclude |
|---|---|---|---|---|---|
| TMT-S01 | Spoofing | High | Spoofing the {source} Process | src is process AND tgt is process or store AND crosses | flow.authenticatesSource OR src.implementsAuthenticationScheme |
| TMT-S02 | Spoofing | High | Spoofing the {target} Process | src is process, external, or store AND tgt is process AND crosses | flow.authenticatesDestination |
| TMT-S03 | Spoofing | High | Spoofing the {source} External Entity | src is external AND tgt is process | src.authenticatesItself OR flow.authenticatesSource |
| TMT-S04 | Spoofing | Medium | Spoofing of Source Data Store {source} | src is store | none |
| TMT-S05 | Spoofing | Medium | Spoofing of Destination Data Store {target} | tgt is store | none |
| TMT-S06 | Spoofing | Medium | Spoofing of the {target} External Destination Entity | src is process AND tgt is external AND crosses | none |
| TMT-T01 | Tampering | High | Potential Lack of Input Validation for {target} | src is process or external AND tgt is process AND crosses | flow.providesConfidentiality AND flow.providesIntegrity |
| TMT-T02 | Tampering | High | {source} Process Memory Tampered | src is process AND tgt is process AND tgt.codeType is "Unmanaged" | none |
| TMT-T03 | Tampering | Medium | Replay Attacks | src is process AND tgt is process AND src.implementsCommunicationProtocol | none |
| TMT-T04 | Tampering | Medium | Collision Attacks | src is process AND tgt is process AND src.implementsCommunicationProtocol | none |
| TMT-T05 | Tampering | Medium | Risks from Logging | (src is process AND tgt is store AND tgt.storesLogData) OR (src is store AND src.storesLogData AND tgt is process) | none |
| TMT-T06 | Tampering | High | Authenticated Data Flow Compromised | flow.authenticatesSource OR flow.authenticatesDestination | flow.providesConfidentiality AND flow.providesIntegrity |
| TMT-T07 | Tampering | High | Potential SQL Injection Vulnerability for {target} | tgt.subtype is "SQL Database" AND src is process or external | none |
| TMT-T08 | Tampering | Medium | XML DTD and XSLT Processing | flow.carriesXML AND tgt is process | none |
| TMT-T09 | Tampering | Medium | JavaScript Object Notation Processing | flow.protocol is HTTP or HTTPS AND flow.carriesJSON AND tgt is process | none |
| TMT-T10 | Tampering | High | Cross Site Scripting | tgt.subtype is "Web Application" or "Web Server" | tgt.hasInputSanitizers AND tgt.hasOutputSanitizers |
| TMT-T11 | Tampering | High | Persistent Cross Site Scripting | tgt.subtype is "Web Application" or "Web Server" AND src is store | tgt.hasInputSanitizers AND tgt.hasOutputSanitizers |
| TMT-T12 | Tampering | High | The {target} Data Store Could Be Corrupted | src is process or external AND tgt is store AND crosses | none |
| TMT-R01 | Repudiation | Medium | Lower Trusted Subject Updates Logs | src is process or external AND tgt is store AND tgt.storesLogData | none |
| TMT-R02 | Repudiation | Medium | Data Logs from an Unknown Source | src is process or external AND tgt is store AND tgt.storesLogData | none |
| TMT-R03 | Repudiation | Medium | Insufficient Auditing | src is process AND tgt is store AND tgt.storesLogData | none |
| TMT-R04 | Repudiation | Medium | Potential Weak Protections for Audit Data | src is process AND tgt is store AND tgt.storesLogData | none |
| TMT-R05 | Repudiation | Medium | Potential Data Repudiation by {target} | tgt is process AND crosses | none |
| TMT-R06 | Repudiation | Low | External Entity {target} Potentially Denies Receiving Data | tgt is external AND crosses | none |
| TMT-R07 | Repudiation | Low | Data Store Denies {target} Potentially Writing Data | tgt is store AND crosses | none |
| TMT-I01 | Information Disclosure | High | Authorization Bypass | src is process AND tgt is store AND src.implementsCustomAuthorization | none |
| TMT-I02 | Information Disclosure | High | Data Flow Sniffing | ((src is process or external AND tgt is process) OR (src is process AND tgt is store)) AND crosses | flow.providesConfidentiality |
| TMT-I03 | Information Disclosure | Medium | Weak Access Control for a Resource | src is store AND tgt is process or external | none |
| TMT-I04 | Information Disclosure | High | Weak Credential Storage | src is process AND tgt is store AND tgt.storesCredentials | none |
| TMT-I05 | Information Disclosure | High | Weak Credential Transit | src is process AND tgt is process or store AND crosses | flow.protocol is HTTPS or IPsec |
| TMT-I06 | Information Disclosure | Medium | Weak Authentication Scheme | src is process AND tgt is process AND src.implementsAuthenticationScheme | none |
| TMT-D01 | Denial of Service | Medium | Potential Excessive Resource Consumption for {source} or {target} | src is process AND tgt is store | none |
| TMT-D02 | Denial of Service | Medium | Potential Process Crash or Stop for {target} | tgt is process AND crosses | none |
| TMT-D03 | Denial of Service | Medium | Data Flow {flow} Is Potentially Interrupted | crosses | none |
| TMT-D04 | Denial of Service | Medium | Data Store Inaccessible | (src is store OR tgt is store) AND crosses | none |
| TMT-E01 | Elevation of Privilege | High | Weakness in SSO Authorization | tgt.subtype is "Authorization Provider" | tgt.isManagedIdentityProvider |
| TMT-E02 | Elevation of Privilege | Medium | Elevation Using Impersonation | src is process or external AND tgt is process | none |
| TMT-E03 | Elevation of Privilege | High | {target} May be Subject to Elevation of Privilege Using Remote Code Execution | tgt is process AND crosses | none |
| TMT-E04 | Elevation of Privilege | High | Elevation by Changing the Execution Flow in {target} | tgt is process AND crosses | none |
| TMT-E05 | Elevation of Privilege | High | Cross Site Request Forgery | src.subtype is "Human User", "Browser", "Browser Client", or "Generic External Entity" AND tgt.subtype is "Web Application" or "Web Server" AND crosses | flow.csrfProtection |

Descriptions (put them in src/engine/rules.ts next to each rule, same ID):
- TMT-S01: {source} may be spoofed by an attacker and this may lead to unauthorized access to {target}. Consider using a standard authentication mechanism to identify the source process.
- TMT-S02: {target} may be spoofed by an attacker and this may lead to information disclosure by {source}. Consider using a standard authentication mechanism to identify the destination process.
- TMT-S03: {source} may be spoofed by an attacker and this may lead to unauthorized access to {target}. Consider using a standard authentication mechanism to identify the external entity.
- TMT-S04: {source} may be spoofed by an attacker and this may lead to incorrect data delivered to {target}. Consider using a standard authentication mechanism to identify the source data store.
- TMT-S05: {target} may be spoofed by an attacker and this may lead to data being written to the attacker's target instead of {target}. Consider using a standard authentication mechanism to identify the destination data store.
- TMT-S06: {target} may be spoofed by an attacker and this may lead to data being sent to the attacker's target instead of {target}. Consider using a standard authentication mechanism to identify the external entity.
- TMT-T01: Data flowing across {flow} may be tampered with by an attacker. This may lead to a denial of service, an elevation of privilege, or an information disclosure attack against {target}. Validate all input for type, length, format, and range.
- TMT-T02: If {source} is given access to memory, such as shared memory or pointers, or can control what {target} executes, then {source} can tamper with {target}. Make sure the interface uses only data, not pointers or executable code.
- TMT-T03: Packets or messages without sequence numbers or timestamps can be captured and replayed. Use a communication protocol that supports anti-replay techniques.
- TMT-T04: Attackers who can send a series of packets or messages may be able to overlap data and bypass validation. Reject overlapping fragments and validate the reassembled message.
- TMT-T05: Log readers can come under attack via log files. Canonicalize data in all logs and use a single log reader where possible.
- TMT-T06: An attacker can read or modify data transmitted over an authenticated data flow. Add integrity and confidentiality protection to {flow}.
- TMT-T07: SQL injection inserts malicious code into strings that {target} later parses and executes. Use parameterized queries and review every procedure that builds SQL statements.
- TMT-T08: If {flow} contains XML, XML processing threats such as DTD and XSLT code execution may be exploited. Disable DTD processing and external entity resolution in {target}.
- TMT-T09: If {flow} contains JSON, JSON processing and hijacking threats may be exploited. Validate JSON against a schema and set the correct content type.
- TMT-T10: The web server {target} could be subject to a cross-site scripting attack because it does not sanitize untrusted input. Encode output and validate input.
- TMT-T11: The web server {target} could be subject to a persistent cross-site scripting attack because it does not sanitize data store {source} inputs and outputs.
- TMT-T12: Data flowing across {flow} may be tampered with by an attacker. This may lead to corruption of {target}. Protect the integrity of the data flow to the data store.
- TMT-R01: If anyone outside the highest trust level can write to {target}, this can lead to repudiation problems. Only allow trusted code to write logs.
- TMT-R02: {target} may accept logs from unknown or weakly authenticated sources. Identify and authenticate the source of logs before accepting them.
- TMT-R03: The logs in {target} may not capture enough data to understand an incident after the fact. Log who did what, when, and from where.
- TMT-R04: An attacker may try to destroy {target} or attack log analysis programs. Control read and write access to the audit log through a single reference monitor.
- TMT-R05: {target} claims that it did not receive data from a source outside the trust boundary. Use logging or auditing to record the source, time, and summary of the received data.
- TMT-R06: {target} claims that it did not receive data from a process on the other side of the trust boundary. Use logging or auditing to record the source, time, and summary of the received data.
- TMT-R07: {target} claims that it did not write data received from an entity on the other side of the trust boundary. Use logging or auditing to record the source, time, and summary of the received data.
- TMT-I01: An attacker may access {target} and bypass the permissions of {source}, for example by editing files directly or through file sharing. Make sure {source} is the only path to {target}.
- TMT-I02: Data flowing across {flow} may be sniffed by an attacker. Depending on the data, this may disclose information or help an attacker attack other parts of the system. Encrypt the data flow.
- TMT-I03: Improper data protection of {source} can allow an attacker to read information not intended for disclosure. Review authorization settings.
- TMT-I04: Credentials held in {target} are often disclosed or tampered with. Store a salted hash of credentials instead of the credentials, and use a secrets manager for keys.
- TMT-I05: Credentials sent across {flow} are often subject to sniffing. Use a protocol that encrypts credentials in transit, such as HTTPS or IPsec.
- TMT-I06: Custom authentication schemes in {source} are susceptible to weak credential management, guessable credentials, downgrade attacks, and weak credential change processes. Use a standard authentication scheme.
- TMT-D01: {source} or {target} may not control resource consumption. An attacker may exhaust storage, memory, or connections. Apply quotas and rate limits.
- TMT-D02: {target} crashes, halts, stops, or runs slowly, and violates an availability metric.
- TMT-D03: An external agent interrupts data flowing across {flow} in either direction across the trust boundary.
- TMT-D04: An external agent prevents access to a data store on the other side of the trust boundary.
- TMT-E01: Common SSO implementations such as OAuth2 are vulnerable to man-in-the-middle attacks. Validate tokens, use PKCE, and pin redirect URIs for {target}.
- TMT-E02: {target} may be able to impersonate the context of {source} in order to gain additional privilege.
- TMT-E03: {source} may be able to remotely execute code for {target}.
- TMT-E04: An attacker may pass data into {target} in order to change the flow of program execution within {target} to the attacker's choosing.
- TMT-E05: An attacker can force a user's browser to send a forged request to {target} over {flow} by using the existing trust between the browser and {target}. Use anti-CSRF tokens and SameSite cookies.

Merge rule, `mergeThreats(previous: Threat[], fresh: Threat[]): Threat[]` in src/engine/merge.ts. The user clicks Analyze again after editing the diagram. For a fresh threat whose id exists in previous, keep the previous priority, status, justification, read, userEdited, and remote, and take title, description, interaction, and IDs from fresh. A previous threat whose id is not in fresh is dropped when userEdited is false or kept with stale = true when userEdited is true. Output order: fresh threats in engine order, then stale threats.

# 8. Analysis view

- Clicking Analyze (or switching to the Analysis tab) runs analyze + mergeThreats, saves the result, stores lastAnalyzedAt and diagramHashAtAnalysis, and shows a toast "<n> threats generated".
- When the diagram hash differs from diagramHashAtAnalysis, show a yellow banner "The diagram changed since the last analysis" with a "Re-analyze" button.
- Layout: the canvas stays on the left at 55% width (read-only in this view). The threat list is on the right at 45% width. The Threat Properties panel is below the list.
- Threat list: a table with columns ID, Title, Category, Priority, Status, Interaction. Filters: STRIDE category (multi-select chips), Priority, Status, and a text search. Group toggle: none, by category, by interaction. Header counts: total, and one count per status. Unread rows are bold (MSTMT read indicator). Selecting a row marks it read.
- Selecting a threat highlights its flow (thick, colored edge) and its source and target nodes on the canvas, and centers the view on them (MSTMT "interaction focus").
- Priority badge colors: High red, Medium amber, Low slate. Stale threats show a gray "Stale" badge.
- Threat Properties panel: read-only title, category, description, interaction, rule ID. Editable: Priority select, Status select (Not Started, Needs Investigation, Not Applicable, Mitigated), "Justification / mitigation" textarea. Any edit sets userEdited = true. When remote exists, show an "AccuKnox" section with findingId, remote status, notes, last synced time.
- Bulk actions on selected rows: set status, set priority.

# 9. Export, import, and AccuKnox

Files (src/export/):
- Model JSON: download "<model-slug>.tm.json" containing the full Model. Import validates schemaVersion === 1 with zod and shows a clear error otherwise. Import always creates a new model with a new id.
- CSV: "<model-slug>-threats.csv", one row per threat, columns in this order: Threat ID, Title, Category, Priority, Status, Interaction, Source, Target, Flow, Description, Justification, Rule ID, Stale. Use papaparse unparse so commas and newlines are quoted.
- SARIF: "<model-slug>.sarif", SARIF 2.1.0 built by `toSarif(model): object` in src/export/sarif.ts:
  - "$schema": "https://json.schemastore.org/sarif-2.1.0.json", "version": "2.1.0".
  - runs[0].tool.driver: name "AccuKnox Threat Modeler", version "1.0.0", informationUri "https://tmt.accuknox.com", rules = one entry per ruleId that appears in the threats: { id, name (title template with placeholders removed), shortDescription.text, fullDescription.text (description template), help.text (same), properties: { tags: ["security", "threat-model", "STRIDE", category], "security-severity": High "8.0", Medium "5.0", Low "3.0" } }.
  - runs[0].results = one per threat: ruleId, ruleIndex, level (High "error", Medium "warning", Low "note"), message.text = title + ". " + description, locations[0].physicalLocation.artifactLocation.uri = "<model-slug>.tm.json", locations[0].logicalLocations = [{ name: flow name, kind: "dataFlow", fullyQualifiedName: interaction }], partialFingerprints: { "tmtThreatId/v1": threat.id }, properties: { category, priority, status, justification, sourceElement, targetElement, flow, stale }.
  - Threats with status "Not Applicable" also get suppressions: [{ kind: "external", status: "accepted", justification }].
  - runs[0].properties: { modelId, modelName, framework: "STRIDE", generatedAt }.

AccuKnox integration (src/integrations/accuknox/). The real API is not ready. Build it behind an interface with a mock so the whole flow works today:

```ts
export interface AccuKnoxSettings {
  mode: "mock" | "live";
  baseUrl: string;      // e.g. https://cspm.demo.accuknox.com
  accessKey: string;    // sent as Authorization: Bearer <accessKey>
  tenantId: string;     // sent as the tenant_id query param and the Tenant-Id header
  labelId: string;      // sent as the label_id query param
  tenantLabel: string;  // display only
}
export interface PushResult { ok: boolean; message: string; mapping: Record<string, string>; } // threatId -> findingId
export interface RemoteState { threatId: string; findingId: string; status: string; notes?: string; updatedAt: string; }
export interface AccuKnoxClient {
  testConnection(): Promise<{ ok: boolean; message: string }>;
  pushSarif(sarif: object, model: Model): Promise<PushResult>;
  pullStates(model: Model): Promise<RemoteState[]>;
}
```

- Settings dialog (AccuKnox menu > Settings): mode, base URL, access key (password input with show/hide), tenant ID, label ID, tenant label, "Test connection" button. Store in localStorage key "tmt:accuknox:v1". Show the warning "The access key is stored in this browser only."
- Put every endpoint in one file, src/integrations/accuknox/endpoints.ts, as constants marked `// TODO: confirm with AccuKnox`. The live client reads them from there. Start with these values, taken from the AccuKnox artifact API that CI integrations already use:
  - `ARTIFACT_UPLOAD = "/api/v1/artifact/"`. Method POST. Query params: `tenant_id`, `data_type`, `label_id`, `save_to_s3=false`. Headers: `Tenant-Id: <tenantId>` and `Authorization: Bearer <accessKey>`. Body: multipart/form-data with one field `file` holding the SARIF file named "<model-slug>.sarif".
  - `FINDINGS_LIST = "/api/v1/findings"`. Method GET. Query params: `data_type`, `page`, `page_size=100`, `search`. Header: `Authorization: Bearer <accessKey>`. Follow the `next` URL until it is null.
  - `SARIF_DATA_TYPE = "SARIF"`, a placeholder until AccuKnox confirms the value.
  - `testConnection` in live mode calls FINDINGS_LIST with page_size=1 and reports the HTTP status.
- In live mode, a network error or a non-2xx response shows the status code and the response text in a toast. A CORS failure shows "The AccuKnox API blocked this browser request (CORS)."
- Mock client: testConnection succeeds after 600ms. pushSarif returns a findingId "AK-<6 digits>" per threat. pullStates returns the current remote states, and on each call it changes the status of 2 random pushed threats to one of "Open", "In Progress", "Risk Accepted", "Resolved" and adds a note.
- "Push findings" is disabled until settings are saved. On success, write remote.findingId and remote.lastSyncedAt into each threat and toast "<n> findings pushed to <tenantLabel>".
- "Sync" pulls remote states and opens a dialog listing each change (threat, field, local value, AccuKnox value). The AccuKnox value wins. Map remote status to local status: "Resolved" -> "Mitigated", "Risk Accepted" -> "Not Applicable", "In Progress" -> "Needs Investigation", "Open" -> "Not Started". Apply on "Apply changes" and write remote.status, remote.notes, remote.lastSyncedAt. Show "Everything is up to date" when there are no changes.

# 10. Sample model (for the Home "Open sample model" button)

Name "Sample: E-commerce Web App". Elements:
- Boundary "Internet Boundary" (Internet Boundary) at x 0, y 0, size 260x420, containing "Customer".
- Boundary "Corporate Network" (Corporate Network Boundary) at x 360, y 0, size 700x420, containing everything else.
- "Customer" (Human User), "Storefront" (Web Application), "Orders API" (Web Service), "Orders DB" (SQL Database, storesCredentials true), "Audit Log" (Log Store, storesLogData true), "Stripe" (External Web Service) placed OUTSIDE both boundaries at x 1150, y 150.
Flows: Customer -> Storefront "Browse and checkout" (HTTPS, carriesJSON). Storefront -> Orders API "Create order" (HTTPS, carriesJSON, authenticatesSource). Orders API -> Orders DB "Write order" (Generic). Orders DB -> Orders API "Read order" (Generic). Orders API -> Audit Log "Write audit event" (Generic). Orders API -> Stripe "Charge card" (HTTPS, authenticatesDestination).
Place nodes inside their boundaries with room to spare, so the containment math in section 5 holds.

# 11. Code layout and tests

- src/engine/ (types.ts, rules.ts, geometry.ts, stride.ts, merge.ts, hash.ts): pure TS, no React.
- src/export/ (csv.ts, sarif.ts, modelFile.ts).
- src/integrations/accuknox/ (types.ts, endpoints.ts, mockClient.ts, liveClient.ts, index.ts).
- src/store/ (zustand stores).
- src/components/ (canvas, nodes, edges, panels, dialogs).
- Add vitest and write src/engine/__tests__/stride.test.ts with the fixtures in section 12. Add "test": "vitest run" to package.json.

# 12. Engine fixtures (must pass)

Default props everywhere unless stated. "Boundary B" is a Generic Trust Boundary.
- F1: Human User "User" -> Web Application "App" over HTTP, no boundary. Expect exactly [TMT-S03, TMT-T10, TMT-E02].
- F2: same as F1, but "App" sits inside Boundary B and "User" sits outside. Expect exactly [TMT-S02, TMT-S03, TMT-T01, TMT-T10, TMT-R05, TMT-I02, TMT-D02, TMT-D03, TMT-E02, TMT-E03, TMT-E04, TMT-E05] (12).
- F3: same as F2 with protocol HTTPS. Expect F2 minus TMT-T01 and TMT-I02 (10).
- F4: Web Application "App" -> SQL Database "DB" (storesCredentials true), protocol Generic, both inside Boundary B. Expect exactly [TMT-S05, TMT-T07, TMT-I04, TMT-D01].
- F5: F2 with "App" out of scope. Expect [].
- F6: run F2, set TMT-S03 status "Mitigated" and TMT-I02 status "Needs Investigation", switch the flow to HTTPS, re-analyze with mergeThreats. Expect 11 threats: the 10 from F3 (TMT-S03 still "Mitigated") plus TMT-I02 with stale = true.
- F7: analyze(F2) twice gives deep-equal output (determinism).
- F8: toSarif(F2 model) has version "2.1.0", 12 results, every result has a partialFingerprints["tmtThreatId/v1"] equal to its threat id, and each result's ruleIndex points to the rule with the same id.

Build all of this in one pass. Do not leave placeholder components. When a choice is not specified here, pick the simplest option that matches MSTMT behavior.
````

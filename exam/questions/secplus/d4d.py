"""CompTIA Security+ SY0-701 practice questions — Domain 4 (Security Operations), file D."""

QUESTIONS = [
    {
        "id": "nd4d-001",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Access control models",
        "stem": (
            "A network security engineer configures a VPN concentrator so that connection attempts are evaluated "
            "against a fixed, administrator-defined list of conditions programmed directly into the device: 'if "
            "destination subnet is the finance VLAN AND time is outside 06:00-20:00, then deny' and 'if source "
            "country is not on the approved list, then deny.' These conditions are static system rules applied "
            "uniformly to every connection attempt, not permissions tied to an individual's assigned role. Which "
            "access control model does this configuration use?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Rule-based access control (RuBAC)",
                "correct": True,
                "rationale": (
                    "Correct. RuBAC enforces access using static, predefined IF-THEN conditions configured "
                    "directly into a system (as with firewall/VPN ACL logic), applied uniformly to all requests — "
                    "exactly what this VPN concentrator configuration describes."
                ),
            },
            {
                "id": "b",
                "text": "Role-based access control (RBAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. RBAC grants permissions based on a user's assigned role. The scenario describes "
                    "static, device-level conditional rules applied to every connection regardless of the "
                    "requester's role, not role-based permission assignment."
                ),
            },
            {
                "id": "c",
                "text": "Attribute-based access control (ABAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. ABAC uses a policy engine that dynamically evaluates a rich combination of "
                    "subject, object, and environmental attributes per request. This scenario describes fixed, "
                    "administrator-programmed static rules, not a dynamic attribute-evaluation policy engine."
                ),
            },
            {
                "id": "d",
                "text": "Discretionary access control (DAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. DAC lets a resource owner grant access at their own discretion. The VPN rules "
                    "here are configured centrally by an administrator as fixed system conditions, not delegated "
                    "to individual resource owners."
                ),
            },
        ],
        "explanation": (
            "Rule-based access control (RuBAC) applies static, predefined conditional statements — commonly seen "
            "in firewall ACLs and VPN concentrator policies — uniformly to every connection attempt. It is easily "
            "confused with RBAC by name alone but is a distinct model: RBAC ties permissions to roles, while "
            "RuBAC ties access to fixed, system-defined rules independent of who is requesting access."
        ),
    },
    {
        "id": "nd4d-002",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Access control models",
        "stem": (
            "Select TWO statements that correctly distinguish mandatory access control (MAC) from discretionary "
            "access control (DAC)."
        ),
        "options": [
            {
                "id": "a",
                "text": "In MAC, a central authority assigns fixed classification/clearance labels, and even the resource owner cannot change or override them.",
                "correct": True,
                "rationale": (
                    "Correct. MAC's defining trait is centralized, non-negotiable labeling enforced by the "
                    "operating system/kernel; not even the file's owner can alter the classification or grant "
                    "access outside the label rules."
                ),
            },
            {
                "id": "b",
                "text": "In DAC, the owner of a resource decides who else may access it and can grant or revoke that access at their own discretion.",
                "correct": True,
                "rationale": (
                    "Correct. DAC is defined by owner discretion: the individual who owns or creates a resource "
                    "controls who else can access it, without requiring central policy approval."
                ),
            },
            {
                "id": "c",
                "text": "In MAC, each file's owner independently decides which classification label to apply to their own files.",
                "correct": False,
                "rationale": (
                    "Incorrect. This describes owner discretion, which is the hallmark of DAC, not MAC. Under "
                    "MAC, classification labels are assigned by a central authority, not the individual owner."
                ),
            },
            {
                "id": "d",
                "text": "In DAC, access decisions are enforced by the OS kernel using immutable security labels that no user can modify.",
                "correct": False,
                "rationale": (
                    "Incorrect. Immutable, kernel-enforced labels set by a central authority describe MAC, not "
                    "DAC. DAC relies on owner-granted permissions, not fixed, centrally assigned labels."
                ),
            },
        ],
        "explanation": (
            "MAC centralizes classification/clearance decisions with a governing authority and enforces them at "
            "the kernel level, removing owner discretion entirely. DAC does the opposite: it places access "
            "decisions in the hands of each resource's owner, who can grant or revoke access without a central "
            "policy authority's approval."
        ),
    },
    {
        "id": "nd4d-003",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Application security",
        "stem": (
            "A SAST scan flags a Java application that uses ObjectInputStream.readObject() to deserialize a data "
            "blob submitted directly by users in an HTTP request, reconstructing it into application objects. A "
            "researcher demonstrates that a crafted serialized payload triggers remote code execution during "
            "deserialization, before any application-level validation logic runs. Which remediation BEST "
            "addresses the root cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Stop deserializing untrusted input directly into native objects; use a safe data format (e.g., JSON with a fixed schema) and allow-list the expected object types before deserialization.",
                "correct": True,
                "rationale": (
                    "Correct. Deserialization vulnerabilities occur because reconstructing an object graph can "
                    "itself execute code (constructors, gadget chains) before validation runs. The fix is to "
                    "avoid deserializing untrusted data into native objects and to allow-list expected types."
                ),
            },
            {
                "id": "b",
                "text": "Encrypt the serialized blob in transit using TLS so attackers cannot intercept and modify it.",
                "correct": False,
                "rationale": (
                    "Incorrect. TLS protects data in transit but does not prevent an authenticated attacker from "
                    "submitting a malicious payload directly; the exploit occurs at the application layer during "
                    "deserialization, which TLS has no bearing on."
                ),
            },
            {
                "id": "c",
                "text": "Add a WAF rule blocking requests containing the string 'ObjectInputStream'.",
                "correct": False,
                "rationale": (
                    "Incorrect. A simple string-match WAF rule is trivially bypassed with encoding or payload "
                    "obfuscation and is a compensating control at best, not a fix for the underlying insecure "
                    "deserialization logic."
                ),
            },
            {
                "id": "d",
                "text": "Increase the maximum permitted size of the uploaded object to prevent buffer truncation errors.",
                "correct": False,
                "rationale": (
                    "Incorrect. This vulnerability is not related to buffer size or truncation; it concerns "
                    "arbitrary code execution triggered during object reconstruction, unrelated to payload size "
                    "limits."
                ),
            },
        ],
        "explanation": (
            "Insecure deserialization allows attacker-controlled data to be reconstructed into live objects, "
            "which can trigger code execution via gadget chains before any application validation occurs. The "
            "root-cause fix is avoiding deserialization of untrusted input and using safe, schema-validated "
            "formats with type allow-listing."
        ),
    },
    {
        "id": "nd4d-004",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Application security",
        "stem": (
            "A web application's 'image preview' feature accepts a URL, fetches it server-side, and displays a "
            "thumbnail. A penetration tester submits the internal address "
            "'http://169.254.169.254/latest/meta-data/iam/security-credentials/' as the URL and receives the "
            "cloud instance's temporary IAM credentials in the rendered response. Which vulnerability was "
            "exploited, and what is the BEST remediation?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Server-side request forgery (SSRF); validate/allow-list permitted destination URLs and block requests to internal/link-local and metadata IP ranges from the application server.",
                "correct": True,
                "rationale": (
                    "Correct. SSRF occurs when the server can be tricked into making requests to attacker-chosen "
                    "destinations, including internal metadata services. Allow-listing destinations and blocking "
                    "internal/link-local ranges is the standard remediation."
                ),
            },
            {
                "id": "b",
                "text": "Cross-site scripting (XSS); HTML-encode all output rendered in the browser.",
                "correct": False,
                "rationale": (
                    "Incorrect. XSS is client-side script injection into a victim's browser session. This "
                    "exploit involved the server itself making an outbound request on the attacker's behalf, "
                    "which is unrelated to browser output encoding."
                ),
            },
            {
                "id": "c",
                "text": "SQL injection; use parameterized queries for the image URL field.",
                "correct": False,
                "rationale": (
                    "Incorrect. No database query is involved in fetching and rendering a remote image; "
                    "parameterized queries address injection into SQL statements, not server-side URL fetching."
                ),
            },
            {
                "id": "d",
                "text": "Cross-site request forgery (CSRF); add anti-CSRF tokens to the image preview form.",
                "correct": False,
                "rationale": (
                    "Incorrect. CSRF tricks a victim's browser into submitting unwanted requests using the "
                    "victim's own session. Here the server itself made the malicious internal request directly, "
                    "which anti-CSRF tokens do not address."
                ),
            },
        ],
        "explanation": (
            "SSRF lets an attacker cause a server to make requests to arbitrary destinations, including internal "
            "cloud metadata endpoints that expose credentials. Mitigation requires strict allow-listing of "
            "permitted destinations and blocking requests to internal/link-local/metadata address ranges."
        ),
    },
    {
        "id": "nd4d-005",
        "domain": 4,
        "objective": "4.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Asset management",
        "stem": (
            "A hospital's clinical engineering department independently purchases and connects networked "
            "infusion pumps and patient monitors, provisioning them without involving the IT asset management "
            "process. Security discovers dozens of these devices generating traffic on the clinical VLAN with no "
            "corresponding entry in the CMDB, no assigned owner, and unknown firmware versions. Which practice "
            "would MOST effectively close this asset visibility gap going forward?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Implement passive network discovery/asset-fingerprinting tools integrated with the CMDB, combined with a formal onboarding process requiring any department connecting a device to register it centrally.",
                "correct": True,
                "rationale": (
                    "Correct. Passive discovery independently verifies what is actually on the network — "
                    "essential for IoT/OT devices that cannot run standard agents — while formal onboarding "
                    "closes the process gap that let clinical engineering bypass IT asset management."
                ),
            },
            {
                "id": "b",
                "text": "Require clinical engineering to submit a monthly spreadsheet listing newly purchased equipment.",
                "correct": False,
                "rationale": (
                    "Incorrect. This is manual self-reporting, the exact process that already failed — the "
                    "department bypassed IT asset management once and a spreadsheet requirement does not "
                    "independently verify what is actually connected to the network."
                ),
            },
            {
                "id": "c",
                "text": "Restrict the clinical VLAN's internet access to reduce the devices' attack surface.",
                "correct": False,
                "rationale": (
                    "Incorrect. Restricting internet access may reduce exposure but does nothing to solve the "
                    "underlying visibility problem — the devices remain unaccounted for in the CMDB regardless "
                    "of their internet access."
                ),
            },
            {
                "id": "d",
                "text": "Deploy full endpoint agents identical to those used on standard IT-managed workstations to every clinical device.",
                "correct": False,
                "rationale": (
                    "Incorrect. Many medical/IoT/OT devices run embedded or proprietary operating systems and "
                    "cannot support standard endpoint agents, often due to vendor certification restrictions, "
                    "making this approach impractical for this device class."
                ),
            },
        ],
        "explanation": (
            "Asset visibility for IoT/OT/medical devices that cannot run standard agents requires passive "
            "network discovery tools reconciled against the CMDB, paired with a mandatory onboarding process so "
            "departments cannot connect unmanaged devices outside IT's asset management workflow."
        ),
    },
    {
        "id": "nd4d-006",
        "domain": 4,
        "objective": "4.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Asset management",
        "stem": (
            "A vulnerability scan unexpectedly reports that 15 production servers are running an operating "
            "system version that reached vendor end-of-life eight months earlier and will no longer receive "
            "security patches. The CMDB listed these servers as 'compliant' throughout that period because it "
            "only tracks whether the last known patch was applied, not the OS version's support lifecycle "
            "status. Which asset management improvement would have surfaced this risk BEFORE the scan did?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Incorporate software/OS lifecycle and end-of-life dates into the asset inventory, with automated alerts as supported systems approach their EOL date.",
                "correct": True,
                "rationale": (
                    "Correct. Tracking lifecycle/EOL status as an inventory attribute, with proactive alerting, "
                    "surfaces upcoming unsupported systems before they lose vendor patching, rather than "
                    "discovering the exposure reactively via a scan."
                ),
            },
            {
                "id": "b",
                "text": "Increase the frequency of vulnerability scans from monthly to weekly.",
                "correct": False,
                "rationale": (
                    "Incorrect. More frequent scanning would still only detect the EOL exposure reactively, "
                    "after the OS had already gone unsupported, rather than proactively flagging the approaching "
                    "EOL date in advance."
                ),
            },
            {
                "id": "c",
                "text": "Require dual approval from two administrators before any patch is deployed to production.",
                "correct": False,
                "rationale": (
                    "Incorrect. Change control on patch deployment approvals does not address tracking of "
                    "vendor support/EOL status, which is an inventory data gap, not a deployment authorization "
                    "issue."
                ),
            },
            {
                "id": "d",
                "text": "Migrate all production servers to a single standardized hardware vendor.",
                "correct": False,
                "rationale": (
                    "Incorrect. Hardware vendor standardization has no bearing on tracking an operating system's "
                    "software support lifecycle or end-of-life date."
                ),
            },
        ],
        "explanation": (
            "Mature asset management tracks not just patch compliance but the full software/OS lifecycle, "
            "including end-of-life and end-of-support dates, with proactive alerting so unsupported systems are "
            "identified and remediated before they silently lose vendor patching."
        ),
    },
    {
        "id": "nd4d-007",
        "domain": 4,
        "objective": "4.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Automation & orchestration",
        "stem": (
            "A SOC is documenting its automation strategy. For a simple, well-understood scenario (an employee's "
            "password reset request), they want a fixed, linear, step-by-step sequence with no decision "
            "branching. For a more complex scenario (phishing triage), they want a document mapping multiple "
            "conditional decision points, combining automated actions with points where a human analyst must "
            "decide how to proceed. Which pair of terms correctly matches these two artifacts, respectively?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Runbook (the linear, prescriptive password-reset procedure) and playbook (the branching, conditional phishing-triage workflow)",
                "correct": True,
                "rationale": (
                    "Correct. A runbook is a fixed, sequential, prescriptive procedure for well-defined, "
                    "repeatable tasks. A playbook maps conditional decision points and combines automated and "
                    "manual response actions for more complex scenarios like phishing triage."
                ),
            },
            {
                "id": "b",
                "text": "Playbook (the linear, prescriptive password-reset procedure) and runbook (the branching, conditional phishing-triage workflow)",
                "correct": False,
                "rationale": (
                    "Incorrect. This reverses the definitions. Runbooks are the fixed, linear procedures; "
                    "playbooks are the conditional, branching workflows — not the other way around."
                ),
            },
            {
                "id": "c",
                "text": "Both scenarios should be documented as runbooks, since orchestration platforms only execute runbooks.",
                "correct": False,
                "rationale": (
                    "Incorrect. This conflates the terms; orchestration platforms commonly execute playbooks "
                    "with conditional branching logic, not exclusively linear runbooks."
                ),
            },
            {
                "id": "d",
                "text": "Both scenarios should be documented as playbooks, since a runbook only applies to manual, non-IT processes.",
                "correct": False,
                "rationale": (
                    "Incorrect. Runbooks are commonly used for prescriptive technical/IT procedures, such as a "
                    "password reset, not only for manual non-IT processes."
                ),
            },
        ],
        "explanation": (
            "Runbooks are fixed, sequential, prescriptive procedures for well-defined, repeatable tasks. "
            "Playbooks are broader documents mapping conditional decision points and combining automated actions "
            "with human decision points, used for more complex, variable-outcome scenarios like incident triage."
        ),
    },
    {
        "id": "nd4d-008",
        "domain": 4,
        "objective": "4.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Automation & orchestration",
        "stem": (
            "A security review of a SOAR platform's phishing-response playbook finds that the integration script "
            "authenticates to the EDR platform's API using a single hardcoded API key with full administrative "
            "scope, embedded directly in the playbook's source code and shared across every automated action, "
            "including ones that only need read-only lookup access. Which remediation BEST addresses this "
            "finding?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Replace the hardcoded key with credentials retrieved from a secrets vault at runtime, and issue separate, narrowly scoped API keys matched to the minimum privilege each specific playbook action requires.",
                "correct": True,
                "rationale": (
                    "Correct. Retrieving credentials from a vault at runtime and scoping each key to least "
                    "privilege eliminates both the hardcoding risk and the excessive-privilege risk in a single "
                    "fix."
                ),
            },
            {
                "id": "b",
                "text": "Rotate the hardcoded API key on a quarterly schedule while leaving it embedded in the script.",
                "correct": False,
                "rationale": (
                    "Incorrect. Periodic rotation reduces the exposure window somewhat but leaves the credential "
                    "hardcoded in source with excessive administrative scope between rotations, failing to "
                    "address either root issue."
                ),
            },
            {
                "id": "c",
                "text": "Move the playbook script to a private, access-restricted code repository.",
                "correct": False,
                "rationale": (
                    "Incorrect. Restricting who can view the script does not fix the hardcoded, over-privileged "
                    "credential itself; anyone with execution access to the SOAR platform can still leverage the "
                    "full-scope key."
                ),
            },
            {
                "id": "d",
                "text": "Disable logging of playbook executions to reduce the chance the key appears in log output.",
                "correct": False,
                "rationale": (
                    "Incorrect. Reducing logging decreases auditability and detection capability without fixing "
                    "the underlying hardcoded, over-privileged credential."
                ),
            },
        ],
        "explanation": (
            "Automation and orchestration integrations should retrieve credentials from a secrets vault at "
            "runtime and be scoped to least privilege per action, rather than embedding a single broadly "
            "privileged key directly in playbook source code."
        ),
    },
    {
        "id": "nd4d-009",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Digital forensics",
        "stem": (
            "A forensic responder seizes a suspect's unlocked smartphone that is still displaying the home "
            "screen. Before transport to the lab, the responder places the device into a Faraday bag and keeps "
            "it powered on inside the bag rather than powering it off or manually enabling airplane mode. What "
            "is the reasoning behind this specific handling procedure?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The Faraday bag blocks all cellular, Wi-Fi, and Bluetooth signals, preventing a remote wipe command or new data from altering the device's state, while keeping it powered on avoids triggering a passcode lock screen that could block access to the evidence.",
                "correct": True,
                "rationale": (
                    "Correct. Radio isolation prevents remote wipe/alteration commands from reaching the device, "
                    "and keeping it powered on preserves the already-unlocked state, avoiding a passcode lock "
                    "that would otherwise block examiner access."
                ),
            },
            {
                "id": "b",
                "text": "Powering off the device immediately preserves the most evidence, since all mobile operating systems store data identically whether powered on or off.",
                "correct": False,
                "rationale": (
                    "Incorrect. Powering off risks the device requiring a passcode on reboot, losing access to "
                    "an already-unlocked state, and this option does not address the network isolation need that "
                    "the Faraday bag itself solves."
                ),
            },
            {
                "id": "c",
                "text": "Manually enabling airplane mode achieves the same protection as a Faraday bag and is preferred since it requires no special equipment.",
                "correct": False,
                "rationale": (
                    "Incorrect. Manually interacting with the touchscreen risks altering data or triggering app "
                    "actions and leaves no certainty every radio is disabled depending on device/OS behavior, "
                    "unlike the passive isolation a Faraday bag provides."
                ),
            },
            {
                "id": "d",
                "text": "Connecting the phone to a lab Wi-Fi network ensures the latest data is synced for a complete forensic image.",
                "correct": False,
                "rationale": (
                    "Incorrect. Connecting to any network is exactly what must be avoided, as it could allow "
                    "remote commands, sync/delete actions, or app-triggered changes to alter the device's "
                    "evidentiary state."
                ),
            },
        ],
        "explanation": (
            "Faraday bags provide passive radio isolation, preventing remote wipe or data-altering commands from "
            "reaching a seized mobile device, while keeping it powered on preserves an already-unlocked state "
            "that would otherwise be lost to a passcode lock screen on reboot."
        ),
    },
    {
        "id": "nd4d-010",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Digital forensics",
        "stem": (
            "During timeline analysis, an investigator notices a suspicious executable's file system 'Created' "
            "timestamp is later than its 'Modified' timestamp — a sequence that should not normally occur under "
            "standard file system behavior. Which conclusion and follow-up action are MOST appropriate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The timestamps were likely deliberately altered (timestomping), an anti-forensic technique; corroborate the file's true timeline using independent artifacts such as the Master File Table, prefetch data, and event logs rather than relying on file system timestamps alone.",
                "correct": True,
                "rationale": (
                    "Correct. An inverted Created/Modified sequence is a classic timestomping indicator. "
                    "Investigators must corroborate with independent artifacts (MFT, prefetch, event logs) since "
                    "the file system timestamps themselves have been called into question."
                ),
            },
            {
                "id": "b",
                "text": "This is normal behavior caused by daylight saving time adjustments and requires no further investigation.",
                "correct": False,
                "rationale": (
                    "Incorrect. A DST shift affects timestamps uniformly and would not reverse the expected "
                    "creation-then-modification order in this way; this is not a benign clock-adjustment "
                    "artifact."
                ),
            },
            {
                "id": "c",
                "text": "The finding indicates the disk was imaged incorrectly and the forensic image should be discarded and reacquired.",
                "correct": False,
                "rationale": (
                    "Incorrect. An inverted timestamp is a property of the file's metadata as stored on the "
                    "original media, not evidence of an imaging error."
                ),
            },
            {
                "id": "d",
                "text": "The finding is inconclusive and should be excluded from the report since file system timestamps are never reliable indicators of anything.",
                "correct": False,
                "rationale": (
                    "Incorrect. Timestamps remain a valuable investigative lead; an anomaly like this is "
                    "significant and should be flagged and corroborated with other artifacts, not dismissed "
                    "outright."
                ),
            },
        ],
        "explanation": (
            "Anti-forensic timestomping alters file metadata to mislead timeline analysis. An impossible "
            "sequence (Created after Modified) is a strong indicator of tampering, and investigators should "
            "corroborate the true timeline using independent artifacts not easily manipulated by the same "
            "technique."
        ),
    },
    {
        "id": "nd4d-011",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Digital forensics and chain-of-custody process",
        "stem": (
            "An evidence locker's electronic access log shows that an IT staff member who is not part of the "
            "investigation team badge-accessed the secured evidence room during the window a seized hard drive "
            "was stored there, although the tamper-evident bag appears visually undisturbed. What MUST the "
            "evidence custodian do?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Document the unauthorized access event in the chain-of-custody record, and re-verify the evidence's cryptographic hash against the value recorded at acquisition before any further examination continues.",
                "correct": True,
                "rationale": (
                    "Correct. An unexplained access by an unauthorized individual must be documented regardless "
                    "of whether visible tampering is apparent, and hash re-verification confirms whether the "
                    "underlying data was actually altered."
                ),
            },
            {
                "id": "b",
                "text": "Ignore the access log entry since the tamper-evident bag shows no visible signs of disturbance.",
                "correct": False,
                "rationale": (
                    "Incorrect. An unexplained, unauthorized access must be recorded regardless of visible "
                    "disturbance; opposing counsel can still raise the gap, and undocumented anomalies undermine "
                    "defensibility."
                ),
            },
            {
                "id": "c",
                "text": "Quietly remove the evidence log entry to avoid raising questions about the investigation's integrity during any future proceedings.",
                "correct": False,
                "rationale": (
                    "Incorrect. Altering or omitting custody records is itself evidence tampering and a serious "
                    "ethical/legal violation that would far more severely damage admissibility than disclosing "
                    "the anomaly."
                ),
            },
            {
                "id": "d",
                "text": "Destroy the evidence and restart the acquisition process from a backup copy.",
                "correct": False,
                "rationale": (
                    "Incorrect. This is unnecessary and disproportionate; destroying original evidence over an "
                    "unconfirmed concern removes the ability to verify integrity via hashing and eliminates the "
                    "primary evidence entirely."
                ),
            },
        ],
        "explanation": (
            "Chain-of-custody integrity requires documenting every access to evidence, expected or not. An "
            "unexplained access by an unauthorized party must be logged and followed by hash re-verification "
            "against the acquisition-time value to confirm the data itself remains unaltered."
        ),
    },
    {
        "id": "nd4d-012",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Digital forensics and chain-of-custody process",
        "stem": (
            "An investigation requires two separate forensic examiners to independently analyze the same seized "
            "evidence at different times using their own working copies. Select TWO practices that preserve a "
            "defensible chain of custody in this multi-examiner scenario."
        ),
        "options": [
            {
                "id": "a",
                "text": "Generate and record a cryptographic hash for each examiner's individual working copy at the moment it is created, and verify each hash against the original acquisition hash before that copy is used.",
                "correct": True,
                "rationale": (
                    "Correct. Independently hashing and verifying each derived working copy against the "
                    "original proves that copy is a faithful, unaltered duplicate before any examiner relies on "
                    "it."
                ),
            },
            {
                "id": "b",
                "text": "Maintain a separate, complete custody log for each duplicate copy documenting who created it, when, and from which verified source image.",
                "correct": True,
                "rationale": (
                    "Correct. Each derived copy needs its own documented custody trail tracing back to the "
                    "verified source, ensuring accountability for every examiner's independent working copy."
                ),
            },
            {
                "id": "c",
                "text": "Allow only the first examiner's copy to be logged, since the second examiner's copy is 'just a duplicate' and does not require its own documentation.",
                "correct": False,
                "rationale": (
                    "Incorrect. Every derived copy used in analysis must be independently documented and "
                    "hash-verified; exempting any copy creates an undocumented gap that can be challenged."
                ),
            },
            {
                "id": "d",
                "text": "Have both examiners share a single working copy simultaneously over a network share to save storage space and simplify tracking.",
                "correct": False,
                "rationale": (
                    "Incorrect. Sharing a single mutable working copy between simultaneous examiners risks "
                    "unintentional modification and makes it impossible to attribute any change to a specific "
                    "examiner, weakening defensibility."
                ),
            },
        ],
        "explanation": (
            "When multiple examiners work from derived copies, each copy must be independently hash-verified "
            "against the original and documented with its own custody trail. Sharing a single mutable copy or "
            "exempting any duplicate from documentation both create defensibility gaps."
        ),
    },
    {
        "id": "nd4d-013",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "EDR/XDR & DLP",
        "stem": (
            "An EDR agent automatically terminates a process exhibiting rapid, bulk file-read-and-rewrite "
            "behavior consistent with its ransomware-behavior heuristic. Investigation confirms the process was "
            "actually a legitimate, digitally signed enterprise backup application performing a scheduled "
            "full-volume backup, and the termination caused the nightly backup job to fail. What is the BEST way "
            "to prevent recurrence without reducing overall ransomware detection coverage?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Create a narrowly scoped EDR exclusion for the verified backup application, matched by its file hash and installation path, so only that specific validated process is exempted from the ransomware-behavior heuristic.",
                "correct": True,
                "rationale": (
                    "Correct. A narrow, hash/path-scoped exclusion resolves the false positive for the one "
                    "verified legitimate process while leaving the ransomware-behavior heuristic fully active "
                    "for every other process on the endpoint."
                ),
            },
            {
                "id": "b",
                "text": "Disable the ransomware-behavior detection heuristic across the entire environment to prevent any future false positives.",
                "correct": False,
                "rationale": (
                    "Incorrect. This removes a broad category of ransomware detection for every endpoint, "
                    "creating a significant coverage gap far beyond what is needed to fix one verified false "
                    "positive."
                ),
            },
            {
                "id": "c",
                "text": "Uninstall the EDR agent from the backup server entirely so the backup job is never interrupted again.",
                "correct": False,
                "rationale": (
                    "Incorrect. Removing endpoint protection from a server entirely eliminates all detection "
                    "capability on that host, an unnecessarily extreme response to a single tunable false "
                    "positive."
                ),
            },
            {
                "id": "d",
                "text": "Reduce the backup job's file read/write throughput so it no longer resembles ransomware-like behavior.",
                "correct": False,
                "rationale": (
                    "Incorrect. Throttling a legitimate backup to avoid detection is not a reliable long-term "
                    "fix and would degrade the backup window; the correct approach is to tune detection around "
                    "the verified-legitimate process itself."
                ),
            },
        ],
        "explanation": (
            "EDR false positives on verified legitimate software should be resolved with narrowly scoped "
            "exclusions (hash/path-matched) rather than broadly disabling detection heuristics or removing "
            "endpoint protection, preserving coverage everywhere else."
        ),
    },
    {
        "id": "nd4d-014",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "EDR/XDR & DLP",
        "stem": (
            "A quarterly review runs a scan against every file share, SharePoint site, and cloud storage "
            "repository in the environment, identifying and cataloging files containing exposed Social Security "
            "numbers and credit card data sitting in unsecured locations — including a share nobody on the "
            "security team knew existed. No data was actually in transit or in use when the scan ran. Which DLP "
            "capability performed this scan?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Data-at-rest discovery/classification scanning of stored repositories",
                "correct": True,
                "rationale": (
                    "Correct. Data-at-rest discovery scans stored repositories (file shares, SharePoint, cloud "
                    "storage) to identify sensitive data sitting at rest, independent of any active transfer or "
                    "usage event."
                ),
            },
            {
                "id": "b",
                "text": "Endpoint DLP monitoring data as it is copied to removable USB media",
                "correct": False,
                "rationale": (
                    "Incorrect. Endpoint DLP inspects actions occurring in real time on a managed device, such "
                    "as a file copy attempt, not a scheduled sweep of stored repositories across the environment."
                ),
            },
            {
                "id": "c",
                "text": "Network DLP inspecting data in motion across the egress internet gateway",
                "correct": False,
                "rationale": (
                    "Incorrect. Network DLP examines traffic actively leaving the network; it would not identify "
                    "sensitive data quietly sitting at rest in a file share with no associated transfer "
                    "occurring."
                ),
            },
            {
                "id": "d",
                "text": "Email DLP scanning outbound message attachments before delivery",
                "correct": False,
                "rationale": (
                    "Incorrect. Email DLP is scoped specifically to messages in transit through the mail system, "
                    "not to files stored at rest on shares or cloud storage."
                ),
            },
        ],
        "explanation": (
            "DLP operates across three data states — at rest, in motion, and in use. This scenario specifically "
            "describes at-rest discovery/classification scanning of stored repositories, distinct from endpoint, "
            "network, or email DLP, which govern data in use or in motion."
        ),
    },
    {
        "id": "nd4d-015",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Email security (SPF/DKIM/DMARC)",
        "stem": (
            "A company's SPF record grows over time as more approved third-party senders (marketing platform, "
            "payroll provider, support ticketing tool, CRM) are each added via additional 'include:' mechanisms. "
            "After the tenth vendor is added, legitimate mail from ALL approved senders — not just the newest "
            "one — begins failing SPF validation everywhere. What is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The SPF record has exceeded the protocol's limit of 10 DNS lookups, causing a PermError that results in SPF evaluating as a failure for the entire record, regardless of which sender is checked.",
                "correct": True,
                "rationale": (
                    "Correct. SPF caps evaluation at 10 DNS lookups; exceeding it produces a PermError that many "
                    "receivers treat as an outright failure for the entire record, breaking mail from every "
                    "listed sender, not just the newest addition."
                ),
            },
            {
                "id": "b",
                "text": "DKIM keys must be rotated whenever the SPF record is modified, and the rotation was skipped.",
                "correct": False,
                "rationale": (
                    "Incorrect. DKIM key rotation and SPF record changes are independent mechanisms; one does "
                    "not require rotating the other."
                ),
            },
            {
                "id": "c",
                "text": "DMARC policy automatically moves to 'reject' after a domain accumulates more than nine SPF includes.",
                "correct": False,
                "rationale": (
                    "Incorrect. DMARC policy enforcement level is manually set via the 'p=' tag and is entirely "
                    "unrelated to the number of SPF include mechanisms present."
                ),
            },
            {
                "id": "d",
                "text": "The added vendors' mail servers are using an unsupported version of SMTP that SPF cannot evaluate.",
                "correct": False,
                "rationale": (
                    "Incorrect. SPF validation is based on DNS lookups of the sending IP address, not on the "
                    "SMTP protocol version used by the sending server."
                ),
            },
        ],
        "explanation": (
            "SPF limits evaluation to 10 DNS lookups; each include/a/mx/ptr/exists mechanism counts toward that "
            "limit. Exceeding it causes a PermError that breaks SPF validation for the entire record. Mitigation "
            "includes flattening includes or using dedicated subdomains per vendor."
        ),
    },
    {
        "id": "nd4d-016",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Email security (SPF/DKIM/DMARC)",
        "stem": (
            "A company sends a properly DKIM-signed newsletter, signing the 'From,' 'Subject,' and body content. "
            "A recipient's corporate mailing list server relays the message to its subscribers but automatically "
            "prepends '[Newsletter] ' to the Subject line before forwarding. Subscribers' mail servers report a "
            "DKIM signature failure on the forwarded copies, even though SPF may still show a pass depending on "
            "the relay's configuration. What explains the DKIM failure?"
        ),
        "options": [
            {
                "id": "a",
                "text": "DKIM signatures are cryptographically bound to the specific header fields and body content present at signing time; the mailing list's in-transit modification of the signed Subject header invalidates the signature.",
                "correct": True,
                "rationale": (
                    "Correct. DKIM validates a cryptographic signature over the exact header/body content signed "
                    "at send time; any modification to signed content — such as an altered Subject header — "
                    "breaks verification."
                ),
            },
            {
                "id": "b",
                "text": "DKIM failed because the mailing list server's IP address was never added to the sender's SPF record.",
                "correct": False,
                "rationale": (
                    "Incorrect. SPF and DKIM are independent checks based on different data (sending IP vs. "
                    "cryptographic signature); an SPF issue with the mailing list's IP would not cause a DKIM "
                    "signature to fail."
                ),
            },
            {
                "id": "c",
                "text": "DKIM failed because the message was not encrypted with TLS during the relay hop.",
                "correct": False,
                "rationale": (
                    "Incorrect. DKIM validates a signature over message content and does not require or depend "
                    "on the transport encryption used between mail servers along the delivery path."
                ),
            },
            {
                "id": "d",
                "text": "DKIM failed because the recipient's mail server does not support DKIM validation for forwarded mail.",
                "correct": False,
                "rationale": (
                    "Incorrect. DKIM validation checks the signature against the message content received; the "
                    "failure here is caused by the content itself changing after signing, not by a lack of "
                    "forwarded-mail support at the recipient."
                ),
            },
        ],
        "explanation": (
            "DKIM signs specific header fields and the message body at send time. Any downstream modification of "
            "signed content — such as a mailing list altering the Subject line — invalidates the signature, "
            "independent of SPF alignment or transport encryption."
        ),
    },
    {
        "id": "nd4d-017",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Federation & SSO (SAML/OAuth)",
        "stem": (
            "A SAML service provider (SP) for 'AppA' accepts and processes any validly signed assertion issued "
            "by the trusted identity provider, without checking whether the assertion's intended recipient (the "
            "Audience Restriction element) actually matches AppA's own entity ID. A researcher demonstrates that "
            "an assertion originally issued for a completely different application, 'AppB,' is also accepted by "
            "AppA, granting unauthorized access. Which SAML security control was missing?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Validation of the Audience Restriction (and Recipient) field in the assertion to confirm it was specifically issued for this service provider, rejecting assertions intended for a different application.",
                "correct": True,
                "rationale": (
                    "Correct. Checking the Audience Restriction/Recipient field confirms an assertion was "
                    "issued specifically for the receiving SP, preventing a valid assertion meant for a "
                    "different application from being accepted elsewhere."
                ),
            },
            {
                "id": "b",
                "text": "Verification that the assertion's XML digital signature is present.",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario states the assertion is validly signed by the trusted IdP; the "
                    "failure is that a validly signed assertion meant for a different SP is being accepted, not "
                    "a missing or invalid signature."
                ),
            },
            {
                "id": "c",
                "text": "Enforcement of a maximum assertion validity/expiration window.",
                "correct": False,
                "rationale": (
                    "Incorrect. A short validity window limits how long a stolen or replayed assertion remains "
                    "usable, but it does not address a valid, unexpired assertion being accepted by the wrong "
                    "recipient application."
                ),
            },
            {
                "id": "d",
                "text": "Requiring the identity provider to use a longer signing key length.",
                "correct": False,
                "rationale": (
                    "Incorrect. Key length affects the cryptographic strength of the signature itself, not "
                    "whether the SP correctly checks that an assertion was intended for it."
                ),
            },
        ],
        "explanation": (
            "SAML assertions include an Audience Restriction identifying the intended service provider. Service "
            "providers must validate this field to reject assertions issued for a different application, even "
            "when the assertion carries a valid signature from a trusted IdP."
        ),
    },
    {
        "id": "nd4d-018",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Federation & SSO (SAML/OAuth)",
        "stem": (
            "Select TWO statements that correctly distinguish SAML from OAuth 2.0 in enterprise federation "
            "deployments."
        ),
        "options": [
            {
                "id": "a",
                "text": "SAML assertions are typically delivered to the service provider via a browser redirect/POST binding as part of a web-based single sign-on flow.",
                "correct": True,
                "rationale": (
                    "Correct. SAML's standard web SSO pattern passes signed XML assertions through the user's "
                    "browser via a redirect or POST binding from the identity provider to the service provider."
                ),
            },
            {
                "id": "b",
                "text": "OAuth 2.0 access tokens are commonly issued in JWT format and are primarily used to authorize API/resource access on a user's behalf, rather than to directly assert human identity for browser login.",
                "correct": True,
                "rationale": (
                    "Correct. OAuth 2.0 is a delegated authorization framework; its tokens grant scoped API "
                    "access rather than serving as a native identity-assertion mechanism for browser login."
                ),
            },
            {
                "id": "c",
                "text": "OAuth 2.0 was originally designed primarily to authenticate human users during a web login flow, with API authorization added later as an optional extension.",
                "correct": False,
                "rationale": (
                    "Incorrect. OAuth 2.0 was designed from the outset as a delegated authorization framework; "
                    "adding an authentication/identity layer on top of OAuth is the specific purpose of OpenID "
                    "Connect (OIDC), a separate specification."
                ),
            },
            {
                "id": "d",
                "text": "SAML is commonly used to issue short-lived bearer access tokens that a mobile app presents directly to a REST API on every call.",
                "correct": False,
                "rationale": (
                    "Incorrect. That pattern describes OAuth 2.0 access tokens; SAML's assertions are XML-based "
                    "and used predominantly for browser SSO authentication, not as the typical token format for "
                    "REST API authorization."
                ),
            },
        ],
        "explanation": (
            "SAML delivers signed XML assertions via browser redirects for web SSO authentication. OAuth 2.0 is "
            "a delegated authorization framework issuing scoped access tokens (often JWT) for API access, with "
            "identity/authentication added on top by the separate OpenID Connect specification."
        ),
    },
    {
        "id": "nd4d-019",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Hardening & secure baselines",
        "stem": (
            "A hardening review of a Linux web server finds that the SSH daemon configuration has "
            "'PermitRootLogin yes' and 'PasswordAuthentication yes,' allowing direct remote login as root using "
            "a password over the network. Which remediation BEST aligns with secure baseline practices?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Set 'PermitRootLogin no,' require administrators to authenticate as an unprivileged named account and elevate via sudo, and switch to key-based authentication with 'PasswordAuthentication no.'",
                "correct": True,
                "rationale": (
                    "Correct. Disabling direct root login and password authentication forces attributable, "
                    "auditable named-account access with sudo elevation and stronger key-based authentication, "
                    "addressing both identified weaknesses."
                ),
            },
            {
                "id": "b",
                "text": "Leave root login enabled but require a 32-character root password to compensate for the risk.",
                "correct": False,
                "rationale": (
                    "Incorrect. A longer password does not address unattributable, unaudited direct root access "
                    "or password-based (rather than key-based) authentication, both of which remain weaknesses "
                    "regardless of password length."
                ),
            },
            {
                "id": "c",
                "text": "Change the SSH listening port from 22 to a non-standard high port number.",
                "correct": False,
                "rationale": (
                    "Incorrect. Changing the port only marginally reduces automated scanning noise and does "
                    "nothing to address direct root login or password authentication, the actual hardening gaps "
                    "identified."
                ),
            },
            {
                "id": "d",
                "text": "Require administrators to connect through a bastion host but keep root login and password authentication enabled on the destination server itself.",
                "correct": False,
                "rationale": (
                    "Incorrect. A bastion host adds a useful additional layer, but it does not fix the "
                    "underlying misconfiguration on the destination server, which still permits unattributed "
                    "root logins via password once reached."
                ),
            },
        ],
        "explanation": (
            "Secure SSH baselines disable direct root login and password authentication, requiring named-account "
            "access with sudo elevation and key-based authentication, so administrative actions remain "
            "attributable and resistant to password-guessing attacks."
        ),
    },
    {
        "id": "nd4d-020",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Hardening & secure baselines",
        "stem": (
            "A vulnerability review finds that a production database server's host-based firewall has been "
            "fully disabled, with the justification documented as 'the network perimeter firewall already "
            "restricts access to this segment, so the host firewall is redundant.' Which hardening principle "
            "does this configuration violate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Defense-in-depth (layered security) — independent security controls should not be removed based on the assumption that another layer alone provides sufficient protection.",
                "correct": True,
                "rationale": (
                    "Correct. If the perimeter firewall is ever bypassed, misconfigured, or an internal threat "
                    "originates from the same segment, the host-based firewall provides an independent layer; "
                    "removing it violates defense-in-depth."
                ),
            },
            {
                "id": "b",
                "text": "Least functionality — unnecessary services and features should be disabled to reduce the attack surface.",
                "correct": False,
                "rationale": (
                    "Incorrect. Least functionality concerns disabling unneeded services/features on the host, "
                    "not the removal of an active security control such as the host firewall itself."
                ),
            },
            {
                "id": "c",
                "text": "Separation of duties — no single individual should have end-to-end control over a critical process.",
                "correct": False,
                "rationale": (
                    "Incorrect. Separation of duties concerns dividing responsibilities among personnel, not "
                    "layered technical security controls on a server."
                ),
            },
            {
                "id": "d",
                "text": "Non-repudiation — actions taken by a user or system should be provably attributable to them.",
                "correct": False,
                "rationale": (
                    "Incorrect. Non-repudiation concerns provable accountability for actions, not the presence "
                    "of layered network controls on a host."
                ),
            },
        ],
        "explanation": (
            "Defense-in-depth requires multiple independent layers of security controls so that the failure or "
            "bypass of any single layer does not leave a system fully exposed. Disabling a host firewall because "
            "a perimeter firewall exists removes that redundancy."
        ),
    },
    {
        "id": "nd4d-021",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Incident response process",
        "stem": (
            "During an active incident, a business unit vice president directs the IR team to immediately wipe "
            "and reimage a compromised production order-processing server to restore revenue-generating service, "
            "before any forensic image or memory capture has been taken. What is the analyst's BEST course of "
            "action?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Escalate to the incident commander/predefined IR decision authority to balance business impact against evidence preservation, and attempt to capture volatile data and a forensic image first if the timeline allows, documenting any risk-acceptance decision if leadership overrides that step.",
                "correct": True,
                "rationale": (
                    "Correct. IR plans should define an escalation path for exactly this tradeoff between "
                    "business continuity and evidence preservation, rather than leaving the on-the-ground "
                    "analyst to unilaterally comply or refuse."
                ),
            },
            {
                "id": "b",
                "text": "Immediately comply with the VP's instruction and reimage the server without any further discussion, since restoring business operations is always the top priority in every incident.",
                "correct": False,
                "rationale": (
                    "Incorrect. Bypassing the organization's IR decision-making process and destroying evidence "
                    "without escalation could eliminate the ability to determine root cause and scope, risking "
                    "the same weakness being exploited again after recovery."
                ),
            },
            {
                "id": "c",
                "text": "Refuse the VP's request entirely and continue with the standard forensic timeline regardless of business impact.",
                "correct": False,
                "rationale": (
                    "Incorrect. Unilaterally overriding a legitimate business stakeholder without escalating "
                    "through the IR plan's defined decision-making authority ignores the organization's own "
                    "governance process for weighing these tradeoffs."
                ),
            },
            {
                "id": "d",
                "text": "Reimage the server immediately, then attempt to forensically analyze the freshly reimaged, wiped system afterward.",
                "correct": False,
                "rationale": (
                    "Incorrect. Once the system is wiped and reimaged, the volatile memory and pre-wipe disk "
                    "evidence needed to determine root cause and attacker actions is irrecoverably lost."
                ),
            },
        ],
        "explanation": (
            "IR plans should define an escalation path and decision authority for balancing business continuity "
            "against evidence preservation, so analysts are not left to unilaterally decide between competing "
            "priorities during a high-pressure incident."
        ),
    },
    {
        "id": "nd4d-022",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Incident response process",
        "stem": (
            "During a ransomware tabletop exercise, participants spend the first 40 minutes debating who has "
            "the authority to formally declare an incident, who is responsible for leading technical "
            "containment, and who is authorized to communicate with customers and regulators — none of which "
            "the organization's incident response plan clearly defines. Which element of incident response "
            "planning was missing?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Clearly defined incident response roles, responsibilities, and a communication plan, established during the Preparation phase before an incident occurs.",
                "correct": True,
                "rationale": (
                    "Correct. The Preparation phase should produce a documented plan defining who declares an "
                    "incident, who leads containment, and who communicates externally, precisely to avoid this "
                    "confusion during a real incident's time pressure."
                ),
            },
            {
                "id": "b",
                "text": "A signed non-disclosure agreement (NDA) with the tabletop exercise facilitator.",
                "correct": False,
                "rationale": (
                    "Incorrect. An NDA governs confidentiality of exercise details and has no relationship to "
                    "defining internal roles and communication responsibilities during a real incident."
                ),
            },
            {
                "id": "c",
                "text": "A fully automated SOAR playbook capable of remediating ransomware without human involvement.",
                "correct": False,
                "rationale": (
                    "Incorrect. Automation tooling does not resolve organizational governance questions about "
                    "who holds decision-making authority and communication responsibility during an incident."
                ),
            },
            {
                "id": "d",
                "text": "A cyber-insurance policy with a higher coverage limit.",
                "correct": False,
                "rationale": (
                    "Incorrect. Insurance coverage amount does not define or clarify internal roles, "
                    "responsibilities, or communication authority during incident response."
                ),
            },
        ],
        "explanation": (
            "Effective incident response planning defines roles, responsibilities, and communication authority "
            "during the Preparation phase, before an incident occurs, so responders are not debating governance "
            "questions while a real incident is actively unfolding."
        ),
    },
    {
        "id": "nd4d-023",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log data sources",
        "stem": (
            "An analyst investigating a suspected credential compromise needs to determine the exact date, "
            "time, and administrator account responsible for the last password change on a specific Windows "
            "service account. Which log source and event should the analyst review?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Domain controller Security event log, specifically 'A user account was changed' events (e.g., Event ID 4738), which record the account modified and the account that performed the change.",
                "correct": True,
                "rationale": (
                    "Correct. Domain controller account-management auditing records exactly which administrator "
                    "modified a given account and when, directly answering this investigative question."
                ),
            },
            {
                "id": "b",
                "text": "DHCP server lease logs for the domain controller's subnet.",
                "correct": False,
                "rationale": (
                    "Incorrect. DHCP logs record IP address lease assignments to devices; they contain no "
                    "information about account password changes or administrative actions."
                ),
            },
            {
                "id": "c",
                "text": "IIS web server access logs on an unrelated application server.",
                "correct": False,
                "rationale": (
                    "Incorrect. Web server access logs record HTTP requests to that specific application; they "
                    "have no visibility into Active Directory account modification events on the domain "
                    "controller."
                ),
            },
            {
                "id": "d",
                "text": "Antivirus quarantine logs from the endpoint the service account normally logs into.",
                "correct": False,
                "rationale": (
                    "Incorrect. Antivirus quarantine logs record detected/blocked malware files, not directory "
                    "service account modification events."
                ),
            },
        ],
        "explanation": (
            "Domain controller account-management auditing (e.g., Windows Event ID 4738) records exactly which "
            "account was modified, when, and by whom, making it the authoritative source for tracing a service "
            "account's password change."
        ),
    },
    {
        "id": "nd4d-024",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log data sources",
        "stem": (
            "An analyst investigating automated scraping traffic against a web application finds that every "
            "request in the web server's access logs shows the same source IP address — the internal address of "
            "the load balancer sitting in front of the application — making it impossible to identify the true "
            "originating client IP addresses. What is needed to resolve this investigative gap?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Configure the load balancer to insert (and the web server to log) a proxy header such as X-Forwarded-For, which preserves the original client IP address as requests pass through the load balancer.",
                "correct": True,
                "rationale": (
                    "Correct. Logging a proxy header like X-Forwarded-For preserves the true originating client "
                    "IP as requests traverse the load balancer, directly resolving the investigative gap."
                ),
            },
            {
                "id": "b",
                "text": "Increase the web server's log retention period so more historical requests are available for analysis.",
                "correct": False,
                "rationale": (
                    "Incorrect. Retaining more history does not solve the underlying problem that every logged "
                    "entry shows the same load balancer IP regardless of how far back the analyst searches."
                ),
            },
            {
                "id": "c",
                "text": "Enable full packet capture on the load balancer's internal network interface going forward.",
                "correct": False,
                "rationale": (
                    "Incorrect. Packet capture could theoretically help, but it is far more resource-intensive "
                    "than simply enabling proper client-IP header logging, the standard, purpose-built solution "
                    "for this exact problem."
                ),
            },
            {
                "id": "d",
                "text": "Request that the web application's developers add client-side JavaScript to log the browser's IP address.",
                "correct": False,
                "rationale": (
                    "Incorrect. A client-side script cannot reliably determine or self-report the client's true "
                    "public-facing IP address, and a malicious scraper would simply not execute or would falsify "
                    "such a script."
                ),
            },
        ],
        "explanation": (
            "When traffic passes through a load balancer or reverse proxy, the web server's default logging "
            "captures only the proxy's own IP address. Logging a forwarded-client header such as "
            "X-Forwarded-For preserves the true originating client IP for investigations."
        ),
    },
    {
        "id": "nd4d-025",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Malware classification",
        "stem": (
            "A forensic analyst finds that a compromised workstation runs a component that intercepts and "
            "modifies the operating system's own API calls used to list running processes and files, so that "
            "antivirus software and Task Manager never display the malicious process at all. Further analysis "
            "reveals the malicious code is loaded from a modified section of the boot process itself, and it "
            "survives a full operating system reinstall performed without also reformatting the affected boot "
            "partition. Which classification BEST describes this malware?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A bootkit/rootkit — kernel- or boot-level malware that hooks OS APIs to actively conceal its presence and achieves persistence below the operating system layer, surviving reinstallation unless boot components are also wiped.",
                "correct": True,
                "rationale": (
                    "Correct. Hooking OS APIs to hide processes/files and persisting via a modified boot "
                    "component that survives an OS reinstall are the defining characteristics of a bootkit/"
                    "rootkit."
                ),
            },
            {
                "id": "b",
                "text": "Fileless malware executing entirely in memory via legitimate scripting engines.",
                "correct": False,
                "rationale": (
                    "Incorrect. Fileless malware typically does not persist across a reboot or survive an OS "
                    "reinstall unless paired with a separate persistence mechanism; this scenario specifically "
                    "describes boot-level persistence surviving reinstallation."
                ),
            },
            {
                "id": "c",
                "text": "A trojan disguised as a legitimate software update requiring user execution.",
                "correct": False,
                "rationale": (
                    "Incorrect. A trojan's defining trait is tricking a user into executing a disguised program; "
                    "the scenario describes concealment and boot-level persistence mechanisms, not a delivery/"
                    "social-engineering method."
                ),
            },
            {
                "id": "d",
                "text": "Spyware designed to covertly log keystrokes and exfiltrate credentials.",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario describes concealment and boot-level persistence, with no "
                    "indication of keystroke logging or data exfiltration activity, which are spyware's defining "
                    "behaviors."
                ),
            },
        ],
        "explanation": (
            "A bootkit/rootkit hooks operating system APIs to actively hide its presence from monitoring tools "
            "and achieves persistence at the boot level, below the operating system itself, allowing it to "
            "survive a standard OS reinstall unless boot components are also wiped."
        ),
    },
    {
        "id": "nd4d-026",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile device management",
        "stem": (
            "A company's MDM policy enforces full-disk encryption and remote lock/wipe on all managed Android "
            "devices' internal storage. After a device is reported lost, the security team confirms the internal "
            "storage was encrypted as required. However, they later learn the device's removable microSD card — "
            "used to store cached copies of corporate documents — was never encrypted and could be read by "
            "simply removing it and inserting it into another device. Which MDM policy gap allowed this "
            "exposure?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The MDM policy did not extend encryption enforcement (or disable use of) removable external storage media, relying solely on internal storage encryption.",
                "correct": True,
                "rationale": (
                    "Correct. Full-disk encryption of internal storage does not automatically cover removable "
                    "media; the policy scope must explicitly extend to (or disable) external storage to prevent "
                    "this exposure."
                ),
            },
            {
                "id": "b",
                "text": "The MDM policy failed to enforce a minimum screen-lock PIN length.",
                "correct": False,
                "rationale": (
                    "Incorrect. A screen-lock PIN protects access through the device's normal login interface; "
                    "it has no effect on data readable directly from a removable SD card extracted and read on a "
                    "separate device."
                ),
            },
            {
                "id": "c",
                "text": "The MDM policy did not require biometric authentication for corporate email access.",
                "correct": False,
                "rationale": (
                    "Incorrect. Biometric authentication governs access to the app/device itself and would not "
                    "prevent data stored unencrypted on removable media from being read once the card is "
                    "physically removed."
                ),
            },
            {
                "id": "d",
                "text": "The MDM policy failed to enforce automatic OS update installation.",
                "correct": False,
                "rationale": (
                    "Incorrect. OS patch level is unrelated to whether data cached on a removable SD card is "
                    "encrypted; this gap concerns storage encryption policy scope, not patch compliance."
                ),
            },
        ],
        "explanation": (
            "MDM encryption policies must explicitly cover removable external storage, not just internal device "
            "storage, since data cached on an unencrypted microSD card remains fully readable once physically "
            "removed from a lost device."
        ),
    },
    {
        "id": "nd4d-027",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile device management",
        "stem": (
            "An MDM solution is configured to automatically push and install the latest mobile OS update to "
            "every enrolled device as soon as it becomes available. A forced update breaks compatibility with a "
            "critical clinical application that the vendor has not yet certified for the new OS version, causing "
            "an outage during active patient care shifts. Which MDM patch management strategy would have "
            "prevented this outage?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Deploy OS updates in staged rings (e.g., a small pilot group first) with a compatibility validation period for critical line-of-business apps before forcing the update organization-wide.",
                "correct": True,
                "rationale": (
                    "Correct. Staged rollout with a pilot group and compatibility validation catches breaking "
                    "changes for critical applications before they impact the entire fleet."
                ),
            },
            {
                "id": "b",
                "text": "Disable all OS updates permanently on every managed device to avoid any future compatibility issue.",
                "correct": False,
                "rationale": (
                    "Incorrect. Permanently blocking updates leaves devices unpatched against newly disclosed "
                    "vulnerabilities indefinitely, trading one risk for a more severe and ongoing one."
                ),
            },
            {
                "id": "c",
                "text": "Require users to manually approve OS updates on their own personal judgment without any centralized MDM policy.",
                "correct": False,
                "rationale": (
                    "Incorrect. Removing centralized control entirely leads to inconsistent patch levels across "
                    "the fleet and does not ensure critical clinical app compatibility is verified before any "
                    "device updates."
                ),
            },
            {
                "id": "d",
                "text": "Increase the MDM check-in interval so devices report compliance status less frequently.",
                "correct": False,
                "rationale": (
                    "Incorrect. Checking in less often does not affect whether or how OS updates are staged or "
                    "validated for compatibility; it only reduces the timeliness of compliance reporting."
                ),
            },
        ],
        "explanation": (
            "Patch management for MDM-enrolled fleets should use staged rollout rings with compatibility "
            "validation for critical applications before forcing updates organization-wide, balancing timely "
            "patching against the risk of breaking essential software."
        ),
    },
    {
        "id": "nd4d-028",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Multifactor authentication",
        "stem": (
            "After deploying number-matching push MFA specifically to stop MFA fatigue/push-bombing attacks, an "
            "organization still suffers an account compromise: an attacker who already obtained the victim's "
            "password calls the victim posing as IT support, convinces them a 'system migration' requires "
            "reading back a specific two-digit code, and has the victim enter that number on their own "
            "authenticator app to approve the attacker's simultaneous login attempt. Which control gap does this "
            "illustrate, and what additional measure BEST addresses it?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Number-matching MFA closes the 'blind accept' flaw of simple push approval but cannot stop a victim who is socially engineered into knowingly entering the correct number; the gap requires security awareness training plus verifying IT support requests through an independent, pre-established channel.",
                "correct": True,
                "rationale": (
                    "Correct. Number-matching prevents accidental/blind approval, but a socially engineered "
                    "victim who is told the correct number to enter defeats the technical control; the residual "
                    "risk requires awareness training and independent verification of support requests."
                ),
            },
            {
                "id": "b",
                "text": "The gap is a weakness in the TOTP algorithm's cryptographic seed generation, and the fix is to switch to a longer OTP code length.",
                "correct": False,
                "rationale": (
                    "Incorrect. This incident did not involve breaking a TOTP algorithm; the attacker socially "
                    "engineered the victim into approving a legitimate number-matching prompt, a process/human "
                    "control gap, not a cryptographic one."
                ),
            },
            {
                "id": "c",
                "text": "The gap is that number-matching MFA was never actually deployed correctly, and the fix is to revert to simple push-approval MFA.",
                "correct": False,
                "rationale": (
                    "Incorrect. Reverting to simple push approval would reintroduce the original MFA-fatigue "
                    "weakness that number-matching was specifically deployed to close; number-matching was "
                    "deployed correctly here but still socially engineered."
                ),
            },
            {
                "id": "d",
                "text": "The gap is a missing patch on the authenticator app, and the fix is to force an application update on all enrolled devices.",
                "correct": False,
                "rationale": (
                    "Incorrect. No application vulnerability or missing patch is described; the compromise "
                    "resulted entirely from social engineering the victim into approving a legitimate technical "
                    "prompt."
                ),
            },
        ],
        "explanation": (
            "Number-matching MFA closes the technical 'blind accept' weakness of simple push notifications, but "
            "it cannot stop a victim who is convincingly social engineered into reading or entering the correct "
            "code themselves; that residual risk requires awareness training and out-of-band verification of "
            "support requests."
        ),
    },
    {
        "id": "nd4d-029",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Multifactor authentication",
        "stem": (
            "A penetration tester demonstrates that a hardware TOTP token's generated 6-digit codes remain valid "
            "for use up to several minutes after being displayed, far longer than the intended 30-second code "
            "window, because the authentication server is configured with an unusually wide clock-skew tolerance "
            "to compensate for token clock drift. This significantly extends the window during which an "
            "intercepted or shoulder-surfed code could be replayed by an attacker. Which remediation BEST "
            "addresses this finding?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Tighten the server's accepted clock-skew/time-window tolerance to the minimum necessary, and resynchronize or replace tokens with excessive clock drift, reducing the valid replay window for any captured code.",
                "correct": True,
                "rationale": (
                    "Correct. Minimizing the accepted clock-skew tolerance and correcting drifted tokens shrinks "
                    "the window during which an intercepted code remains usable, directly addressing the finding."
                ),
            },
            {
                "id": "b",
                "text": "Switch every TOTP token to a fixed, unchanging code that never expires, to eliminate clock-synchronization issues entirely.",
                "correct": False,
                "rationale": (
                    "Incorrect. A code that never expires would be replayable indefinitely, dramatically "
                    "worsening the exact risk the finding identifies rather than fixing it."
                ),
            },
            {
                "id": "c",
                "text": "Increase the number of digits in the generated code from 6 to 8 without changing the time window.",
                "correct": False,
                "rationale": (
                    "Incorrect. A longer code increases resistance to brute-force guessing but does not shorten "
                    "the excessive validity/replay window that is the actual finding here."
                ),
            },
            {
                "id": "d",
                "text": "Disable MFA for accounts using hardware TOTP tokens until new tokens can be procured.",
                "correct": False,
                "rationale": (
                    "Incorrect. Removing MFA entirely eliminates a critical layer of authentication security and "
                    "is a disproportionate response to a tunable configuration issue."
                ),
            },
        ],
        "explanation": (
            "TOTP security depends on a tight time window during which a generated code remains valid. Excessive "
            "clock-skew tolerance configured to compensate for token drift extends that window, increasing "
            "replay risk; the fix is to minimize tolerance and correct drifted tokens rather than weaken or "
            "disable the control."
        ),
    },
    {
        "id": "nd4d-030",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Penetration testing phases",
        "stem": (
            "A client provides a penetration testing team with valid, low-privilege employee credentials and "
            "internal network access from the outset, specifically so the engagement begins from an 'assumed "
            "breach' starting position rather than requiring the team to first perform external reconnaissance "
            "and gain initial access on their own. Which testing methodology classification does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Partial-knowledge (known-environment) testing, simulating an attacker who has already obtained a foothold, such as a malicious insider or an attacker who has already compromised low-level credentials.",
                "correct": True,
                "rationale": (
                    "Correct. Providing testers with valid credentials and internal access from the start is the "
                    "defining characteristic of partial-knowledge/known-environment, assumed-breach testing."
                ),
            },
            {
                "id": "b",
                "text": "Unknown-environment (black-box) testing, in which the testers are given no information at all about the target and must discover everything independently.",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario explicitly provides testers with valid credentials and internal "
                    "access from the start, the opposite of an unknown-environment engagement with zero provided "
                    "information."
                ),
            },
            {
                "id": "c",
                "text": "A vulnerability scan, since automated tools rather than human testers evaluate the credentials provided.",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario describes a penetration testing engagement performed by testers "
                    "using provided access, not an automated vulnerability scan."
                ),
            },
            {
                "id": "d",
                "text": "A red team engagement focused exclusively on physical security bypass techniques.",
                "correct": False,
                "rationale": (
                    "Incorrect. Nothing in the scenario involves physical security testing; it describes a "
                    "network/credential-based assumed-breach starting position for technical testing."
                ),
            },
        ],
        "explanation": (
            "Providing testers with valid credentials and internal access to simulate an attacker who has "
            "already obtained a foothold describes partial-knowledge (known-environment), assumed-breach "
            "testing — distinct from unknown-environment (black-box) engagements that start with zero provided "
            "information."
        ),
    },
    {
        "id": "nd4d-031",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Penetration testing phases",
        "stem": (
            "During an authorized network penetration test, a tester notices the building receptionist appears "
            "distracted and realizes a simple pretext could likely gain physical access to a restricted server "
            "room. The signed rules of engagement explicitly authorize only remote testing of specified IP "
            "ranges and explicitly excludes any physical or social-engineering testing. The tester declines to "
            "attempt it and documents the observation as a note for the client instead. Why is this the correct "
            "decision?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Testing activity outside the scope defined in the rules of engagement is unauthorized, regardless of good intentions or likelihood of success, and could expose the tester to legal liability and violate the trust established with the client.",
                "correct": True,
                "rationale": (
                    "Correct. Rules of engagement define the legal and ethical boundaries of an authorized "
                    "test; any activity outside that scope, however easy or well-intentioned, is unauthorized "
                    "access and a serious breach of the engagement's terms."
                ),
            },
            {
                "id": "b",
                "text": "Physical security testing is never a legitimate part of any penetration testing engagement and should never be included in a rules of engagement document.",
                "correct": False,
                "rationale": (
                    "Incorrect. Physical security testing can absolutely be a legitimate, explicitly authorized "
                    "part of a penetration test when the client chooses to include it in scope; this engagement's "
                    "RoE simply did not authorize it this time."
                ),
            },
            {
                "id": "c",
                "text": "The tester lacked the specialized physical social-engineering training required, which is the only reason to avoid the attempt.",
                "correct": False,
                "rationale": (
                    "Incorrect. The deciding factor described in the scenario is that the activity falls outside "
                    "the signed scope of authorization, not the tester's personal skill level."
                ),
            },
            {
                "id": "d",
                "text": "Documenting the observation without acting on it violates the tester's obligation to demonstrate every possible exploitation path to the client.",
                "correct": False,
                "rationale": (
                    "Incorrect. Testers are obligated to operate within the authorized scope; they have no "
                    "obligation, and in fact no authorization, to exploit avenues excluded from the rules of "
                    "engagement, no matter how easily they could be demonstrated."
                ),
            },
        ],
        "explanation": (
            "Rules of engagement define the legal and ethical boundaries of an authorized penetration test. "
            "Testers must operate strictly within that scope; exceeding it, even for an easy or well-intentioned "
            "opportunistic finding, constitutes unauthorized activity and legal exposure."
        ),
    },
    {
        "id": "nd4d-032",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Port and protocol security",
        "stem": (
            "A vulnerability scan finds TCP port 445 open on a file server and reachable from the general "
            "corporate network, and further review shows SMBv1 remains enabled specifically to support one "
            "legacy line-of-business application that has not been updated in years. This configuration leaves "
            "the server exposed to well-known SMBv1 remote code execution exploits. Which remediation BEST "
            "addresses this finding?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Disable SMBv1 on the file server, restrict TCP 445 access via firewall rules to only the specific hosts that require it, and work with the application owner on a plan to migrate the legacy application to SMBv2/v3 or replace it.",
                "correct": True,
                "rationale": (
                    "Correct. Disabling the vulnerable protocol version, restricting access to only necessary "
                    "hosts, and planning migration of the legacy dependency together address both the immediate "
                    "exposure and its root cause."
                ),
            },
            {
                "id": "b",
                "text": "Block TCP port 445 entirely at the perimeter firewall only, while leaving SMBv1 enabled and internal access unrestricted.",
                "correct": False,
                "rationale": (
                    "Incorrect. Perimeter blocking does nothing to protect against internal exploitation from an "
                    "already-compromised host on the corporate network and does not remove the underlying "
                    "vulnerable SMBv1 protocol itself."
                ),
            },
            {
                "id": "c",
                "text": "Increase the file server's maximum concurrent SMB connection limit to prevent denial-of-service conditions.",
                "correct": False,
                "rationale": (
                    "Incorrect. Connection limits address availability/resource exhaustion concerns, not the "
                    "remote code execution risk posed by an outdated, vulnerable protocol version."
                ),
            },
            {
                "id": "d",
                "text": "Rename the file server's NetBIOS name to make it harder for attackers to locate on the network.",
                "correct": False,
                "rationale": (
                    "Incorrect. Renaming the host provides no meaningful security benefit against network "
                    "scanning and does not address the actual vulnerable protocol running on the exposed port."
                ),
            },
        ],
        "explanation": (
            "SMBv1 carries well-known remote code execution vulnerabilities. The appropriate remediation "
            "disables the vulnerable protocol version, restricts network access to only what is necessary, and "
            "addresses the legacy application dependency driving its continued use — not just perimeter "
            "filtering or unrelated availability controls."
        ),
    },
    {
        "id": "nd4d-033",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Port and protocol security",
        "stem": (
            "Several internet-facing servers are found to have UDP port 123 (NTP) open and reachable from any "
            "external host, with the legacy 'monlist' command enabled. The organization later learns these "
            "servers were used, without authorization, as reflectors in a large-scale outbound DDoS "
            "amplification attack against an unrelated third-party target. Which remediation BEST addresses the "
            "root cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Disable the NTP 'monlist' command, upgrade to a modern NTP implementation, and restrict NTP query access to trusted internal sources only rather than allowing it from any host on the internet.",
                "correct": True,
                "rationale": (
                    "Correct. Disabling the abusable monlist command and restricting who can query the NTP "
                    "service directly eliminates the servers' ability to be used as open amplification "
                    "reflectors."
                ),
            },
            {
                "id": "b",
                "text": "Increase the servers' outbound bandwidth capacity to absorb larger volumes of reflected traffic.",
                "correct": False,
                "rationale": (
                    "Incorrect. Adding bandwidth does not stop the servers from being abused as amplification "
                    "reflectors and does nothing to address the underlying misconfiguration or protect the "
                    "third-party victim being attacked."
                ),
            },
            {
                "id": "c",
                "text": "Change the servers' system time zone setting to UTC to standardize timestamp logging.",
                "correct": False,
                "rationale": (
                    "Incorrect. A time zone display setting has no relationship to the NTP amplification "
                    "vulnerability, which concerns open query access and response size, not how timestamps are "
                    "displayed in logs."
                ),
            },
            {
                "id": "d",
                "text": "Enable TLS encryption on the NTP service to protect time synchronization data in transit.",
                "correct": False,
                "rationale": (
                    "Incorrect. NTP does not use TLS in its standard implementation, and encrypting the payload "
                    "would not prevent amplification abuse, which exploits the size disparity between small "
                    "requests and large responses, not a lack of confidentiality."
                ),
            },
        ],
        "explanation": (
            "Open NTP servers with the legacy 'monlist' command enabled can be abused for DDoS reflection/"
            "amplification attacks. Remediation requires disabling the abusable command, restricting query "
            "access to trusted sources, and upgrading the NTP implementation — not bandwidth, time zone, or "
            "encryption changes, which do not address the amplification vector."
        ),
    },
    {
        "id": "nd4d-034",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Privileged access management",
        "stem": (
            "An audit of a PAM solution finds that several service account passwords were checked out of the "
            "vault by administrators for maintenance work and were never explicitly checked back in. Because the "
            "vault's rotation policy was configured to trigger only on check-in, these credentials have remained "
            "unrotated for over 90 days, silently undermining the vault's intended security benefit. Which "
            "configuration change BEST addresses this gap?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Configure the vault to enforce a maximum checkout duration with automatic forced check-in and rotation after that period elapses, regardless of whether the credential was manually checked back in.",
                "correct": True,
                "rationale": (
                    "Correct. A maximum checkout duration with forced automatic check-in and rotation removes "
                    "the dependency on administrators remembering to manually check credentials back in."
                ),
            },
            {
                "id": "b",
                "text": "Require administrators to submit a written justification memo before checking out any credential.",
                "correct": False,
                "rationale": (
                    "Incorrect. Documentation of the checkout reason does not address the technical gap that "
                    "rotation was never triggered because check-in never occurred; the credentials remain stale "
                    "regardless of paperwork."
                ),
            },
            {
                "id": "c",
                "text": "Increase the length and complexity requirements for all vaulted passwords.",
                "correct": False,
                "rationale": (
                    "Incorrect. Stronger password composition does not solve the operational problem that the "
                    "same unrotated password value has remained in use for over 90 days."
                ),
            },
            {
                "id": "d",
                "text": "Disable the vault's automatic rotation feature entirely and require administrators to manually rotate credentials on their own schedule.",
                "correct": False,
                "rationale": (
                    "Incorrect. Removing automation and relying on manual rotation is a regression that would "
                    "make consistent, timely rotation even less reliable than the current, already-flawed "
                    "automated policy."
                ),
            },
        ],
        "explanation": (
            "PAM vault rotation policies should not depend solely on administrators remembering to check "
            "credentials back in. Enforcing a maximum checkout duration with automatic forced check-in and "
            "rotation ensures credentials cannot silently remain unrotated indefinitely."
        ),
    },
    {
        "id": "nd4d-035",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Privileged access management",
        "stem": (
            "Select TWO statements that reflect best practices for privileged account segregation in an "
            "enterprise identity program."
        ),
        "options": [
            {
                "id": "a",
                "text": "Administrators should use a separate, dedicated privileged account for administrative tasks, distinct from the standard user account they use for email, web browsing, and daily productivity work.",
                "correct": True,
                "rationale": (
                    "Correct. Segregating privileged and standard accounts limits the exposure of elevated "
                    "credentials to routine activities like email and browsing that carry higher phishing/"
                    "malware risk."
                ),
            },
            {
                "id": "b",
                "text": "Privileged accounts should be reserved strictly for administrative tasks and should not be used to read email, browse the web, or perform routine end-user activities that increase exposure to phishing and malware.",
                "correct": True,
                "rationale": (
                    "Correct. Restricting privileged account use to administrative tasks only minimizes the "
                    "attack surface through which an elevated credential could be phished or compromised."
                ),
            },
            {
                "id": "c",
                "text": "It is acceptable for a single account to hold both standard end-user rights and permanent domain administrator rights, as long as multifactor authentication is enabled on that account.",
                "correct": False,
                "rationale": (
                    "Incorrect. Combining standard and permanent privileged rights in one account still violates "
                    "least privilege and account segregation regardless of MFA, since routine day-to-day use of "
                    "that account directly exposes the always-available elevated privileges to compromise."
                ),
            },
            {
                "id": "d",
                "text": "Privileged accounts should reuse the same password across development, test, and production environments to simplify administration.",
                "correct": False,
                "rationale": (
                    "Incorrect. Password reuse across environments means a single compromised credential grants "
                    "an attacker access across every environment, directly contradicting segregation and "
                    "containment principles for privileged access."
                ),
            },
        ],
        "explanation": (
            "Privileged access management best practice segregates dedicated administrative accounts from "
            "everyday user accounts and restricts their use strictly to administrative tasks, minimizing "
            "exposure to phishing and malware and limiting the blast radius of any single compromised credential."
        ),
    },
    {
        "id": "nd4d-036",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "After a new correlation rule is deployed, a SIEM's daily alert volume spikes dramatically. "
            "Investigation shows that roughly 95% of the new alerts are triggered by the organization's own "
            "authorized vulnerability scanner, whose routine sweep of every host on the network trips multiple "
            "signature-based rules simply by probing standard ports and services. Which action BEST resolves the "
            "alert volume without reducing detection of genuine threats?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Create a scoped suppression/allow-list rule specifically for the vulnerability scanner's known IP address and expected scan signature, so its authorized, recognized activity does not generate alerts, while all other sources remain fully monitored.",
                "correct": True,
                "rationale": (
                    "Correct. A narrowly scoped allow-list for the known, authorized scanner eliminates the "
                    "specific noise source while leaving detection fully intact for every other, unrecognized "
                    "source of similar traffic."
                ),
            },
            {
                "id": "b",
                "text": "Disable the new correlation rule entirely across the environment until further notice.",
                "correct": False,
                "rationale": (
                    "Incorrect. Disabling the rule removes detection for every source, not just the known, "
                    "authorized scanner, eliminating coverage against genuine attackers who might trigger the "
                    "same signatures."
                ),
            },
            {
                "id": "c",
                "text": "Schedule the vulnerability scanner to run only once per year to reduce how often it triggers alerts.",
                "correct": False,
                "rationale": (
                    "Incorrect. Drastically reducing scan frequency severely weakens the vulnerability "
                    "management program's ability to find and track new weaknesses, an unacceptable tradeoff to "
                    "reduce SIEM noise."
                ),
            },
            {
                "id": "d",
                "text": "Grant the vulnerability scanner administrative credentials on every host so its traffic is authenticated and no longer inspected by the correlation rule.",
                "correct": False,
                "rationale": (
                    "Incorrect. Granting broad administrative credentials to the scanner increases risk "
                    "unnecessarily and does not directly address the correlation rule's alerting logic, which is "
                    "triggered by the scanner's network-level probing behavior, not its authentication level."
                ),
            },
        ],
        "explanation": (
            "SIEM tuning for known, authorized noise sources (such as a vulnerability scanner) should use "
            "narrowly scoped suppression/allow-list rules rather than broadly disabling detection or reducing "
            "essential security activity like scan frequency."
        ),
    },
    {
        "id": "nd4d-037",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "Three weeks after a certificate used for secure log forwarding from the primary domain controller "
            "expired, the SIEM had silently stopped receiving any logs from that source. No alerts fired because "
            "the SIEM's correlation rules only evaluate log content that is actually received — they have no way "
            "to detect the absence of expected data. The gap was discovered only by chance during an unrelated "
            "audit. Which SIEM operational practice would have surfaced this failure much sooner?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Implement log source health/heartbeat monitoring that alerts when an expected, previously active log source stops sending data within a defined threshold ('dead source' detection).",
                "correct": True,
                "rationale": (
                    "Correct. Heartbeat/health monitoring specifically detects the absence of expected log "
                    "traffic from a source, which content-based correlation rules cannot do since they only "
                    "evaluate data that actually arrives."
                ),
            },
            {
                "id": "b",
                "text": "Increase the number of correlation rules written specifically to detect domain controller compromise indicators.",
                "correct": False,
                "rationale": (
                    "Incorrect. Additional content-based correlation rules still only evaluate logs that are "
                    "actually received; if the source has stopped forwarding data entirely, no amount of "
                    "additional content-matching rules can detect events that were never ingested."
                ),
            },
            {
                "id": "c",
                "text": "Extend the SIEM's log retention period from 90 days to 365 days.",
                "correct": False,
                "rationale": (
                    "Incorrect. Retention period controls how long already-ingested logs are kept searchable; "
                    "it has no effect on detecting that a source silently stopped sending logs in the first "
                    "place."
                ),
            },
            {
                "id": "d",
                "text": "Require analysts to manually query the domain controller's logs once per week as a spot check.",
                "correct": False,
                "rationale": (
                    "Incorrect. A manual, infrequent spot-check is a much slower, less reliable, and more "
                    "labor-intensive substitute for automated heartbeat/health monitoring, the purpose-built "
                    "solution for detecting ingestion failures promptly."
                ),
            },
        ],
        "explanation": (
            "Content-based correlation rules can only evaluate logs that are actually ingested; they cannot "
            "detect the absence of expected data. Log source health/heartbeat monitoring specifically alerts "
            "when an active source silently stops forwarding logs, closing this blind spot."
        ),
    },
    {
        "id": "nd4d-038",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A vulnerability management dashboard marks a critical CVE as 'remediated' on a production host "
            "after a patch deployment job reports success. Two weeks later, an authorized penetration test "
            "successfully exploits that exact same CVE on that exact same host. What is the MOST likely "
            "explanation, and what step should the vulnerability management process add to prevent recurrence?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The patch was likely deployed but the affected service was never restarted (or the patch otherwise failed to fully apply), so the vulnerable code remained active in memory; add a validation step — an authenticated rescan or exploit-based verification — to confirm remediation actually took effect.",
                "correct": True,
                "rationale": (
                    "Correct. Patch deployment success and actual remediation are not the same thing; a "
                    "restart-pending or partially applied patch leaves vulnerable code active. Verifying "
                    "remediation via rescan or exploit testing closes this gap."
                ),
            },
            {
                "id": "b",
                "text": "The CVE must have been misclassified with an incorrect CVSS score, and the fix is to have a second analyst independently re-score every vulnerability before remediation begins.",
                "correct": False,
                "rationale": (
                    "Incorrect. Re-scoring severity does not address why a patch reported as successfully "
                    "deployed failed to actually close the exploitable vulnerability; the issue described is "
                    "remediation verification, not scoring accuracy."
                ),
            },
            {
                "id": "c",
                "text": "The penetration testers must have used a zero-day variant of the same vulnerability that the original CVE and patch do not cover.",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario states the exact same CVE was exploited, not a related but distinct "
                    "variant, so this explanation is not supported by the facts given."
                ),
            },
            {
                "id": "d",
                "text": "Patch deployment tools cannot be trusted and should be replaced with fully manual, host-by-host patching performed by an administrator.",
                "correct": False,
                "rationale": (
                    "Incorrect. Manual patching does not inherently guarantee successful application either, and "
                    "abandoning automation entirely is a disproportionate response; the real gap is the missing "
                    "verification step after deployment."
                ),
            },
        ],
        "explanation": (
            "A patch deployment reporting 'success' only confirms the installer ran, not that the vulnerability "
            "is actually closed — a pending service restart or partial application can leave vulnerable code "
            "active. Vulnerability management programs should verify remediation via authenticated rescan or "
            "exploit-based testing, not rely on deployment status alone."
        ),
    },
    {
        "id": "nd4d-039",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Wireless security",
        "stem": (
            "A corporate wireless network uses WPA2-Enterprise with 802.1X and PEAP-MSCHAPv2. A security "
            "assessment finds that client device supplicants are configured to skip validation of the RADIUS "
            "server's certificate during authentication. An attacker exploits this by standing up a rogue access "
            "point broadcasting a cloned SSID alongside a fake RADIUS server, capturing MSCHAPv2 credential "
            "exchanges from clients that connect to it. Which remediation BEST addresses the root cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Configure all client supplicants to validate the RADIUS server's certificate against a trusted, pinned certificate authority before completing authentication, and consider migrating to EAP-TLS with mutual certificate-based authentication.",
                "correct": True,
                "rationale": (
                    "Correct. Requiring clients to validate the RADIUS server's certificate prevents them from "
                    "authenticating to an attacker-controlled fake RADIUS server in the first place, closing the "
                    "root cause of the exposure."
                ),
            },
            {
                "id": "b",
                "text": "Increase the MSCHAPv2 password complexity requirements for all wireless users.",
                "correct": False,
                "rationale": (
                    "Incorrect. Stronger passwords do not prevent a client from authenticating to a fake RADIUS "
                    "server in the first place; the root cause is the missing server-certificate validation that "
                    "allows clients to connect to an attacker-controlled authentication server at all."
                ),
            },
            {
                "id": "c",
                "text": "Disable SSID broadcast on the legitimate access points so the network name is not publicly visible.",
                "correct": False,
                "rationale": (
                    "Incorrect. Hiding the SSID does not prevent an attacker from cloning it, since client probe "
                    "requests reveal the network name, and it does not address the client's failure to validate "
                    "the RADIUS server's certificate."
                ),
            },
            {
                "id": "d",
                "text": "Switch from WPA2-Enterprise to WPA2-Personal with a strong shared passphrase.",
                "correct": False,
                "rationale": (
                    "Incorrect. Moving to a shared-passphrase model eliminates individual user authentication "
                    "and per-user auditability entirely, a significant downgrade, and does not address the "
                    "specific certificate-validation weakness identified."
                ),
            },
        ],
        "explanation": (
            "PEAP-MSCHAPv2 security depends on clients validating the RADIUS server's certificate before "
            "completing authentication; skipping this check allows an attacker's rogue AP paired with a fake "
            "RADIUS server to capture credential exchanges. Enforcing certificate validation (or migrating to "
            "mutual-certificate EAP-TLS) closes this gap."
        ),
    },
    {
        "id": "nd4d-040",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Wireless security",
        "stem": (
            "Select TWO statements that correctly describe effective ways to mitigate the risk of rogue access "
            "points on a large corporate campus."
        ),
        "options": [
            {
                "id": "a",
                "text": "A wireless intrusion prevention system (WIPS) can be configured to detect rogue access points within the authorized coverage area and automatically contain them (e.g., targeted deauthentication of clients connecting to the rogue device).",
                "correct": True,
                "rationale": (
                    "Correct. WIPS solutions are purpose-built to detect and actively contain rogue access "
                    "points, disconnecting clients from the unauthorized device while it is located and removed."
                ),
            },
            {
                "id": "b",
                "text": "Regular RF/wireless site surveys help identify unauthorized access points broadcasting from within or near company facilities that automated systems may not have flagged.",
                "correct": True,
                "rationale": (
                    "Correct. Periodic physical/RF site surveys provide an independent verification layer that "
                    "can catch rogue devices missed by automated monitoring, particularly in areas with limited "
                    "sensor coverage."
                ),
            },
            {
                "id": "c",
                "text": "Disabling SSID broadcast (hiding the network name) on legitimate access points prevents attackers from ever standing up a rogue AP, since they would not know the network name to clone.",
                "correct": False,
                "rationale": (
                    "Incorrect. Hidden SSIDs are still discoverable because client devices broadcast probe "
                    "requests containing the network name, and hiding the SSID does nothing to prevent an "
                    "attacker from creating a rogue AP under a different or spoofed name."
                ),
            },
            {
                "id": "d",
                "text": "Deploying WPA3 on the legitimate corporate network automatically prevents any unauthorized access point from broadcasting within radio range of the facility.",
                "correct": False,
                "rationale": (
                    "Incorrect. WPA3 strengthens the authentication/encryption handshake for the legitimate "
                    "network's own clients, but it has no mechanism to prevent an attacker from physically "
                    "deploying and broadcasting an entirely separate rogue access point nearby."
                ),
            },
        ],
        "explanation": (
            "Mitigating rogue access point risk requires active detection and containment (WIPS) combined with "
            "periodic physical/RF site surveys. Neither hiding the legitimate SSID nor upgrading to WPA3 "
            "prevents an attacker from deploying an entirely separate rogue access point nearby."
        ),
    },
]

"""CompTIA Security+ SY0-701 practice questions — Domain 4 (Security Operations), file C."""

QUESTIONS = [
    {
        "id": "nd4c-001",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Access control models",
        "stem": (
            "A collaborative document-sharing platform allows the creator of each file to decide, at any time, "
            "which specific colleagues can view or edit that file, and to revoke that access unilaterally without "
            "involving a central administrator. No classification labels, roles, or centrally defined policy "
            "rules govern these grants. Which access control model does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Discretionary access control (DAC)",
                "correct": True,
                "rationale": (
                    "Correct. DAC places access decisions in the hands of the resource owner, who may grant or "
                    "revoke permissions to other subjects at their own discretion — exactly the behavior described "
                    "for the file creator."
                ),
            },
            {
                "id": "b",
                "text": "Role-based access control (RBAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. RBAC ties permissions to centrally defined roles that users inherit through group "
                    "membership; individual file owners making ad hoc, per-file grants is not role-driven."
                ),
            },
            {
                "id": "c",
                "text": "Mandatory access control (MAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. MAC enforces access using fixed classification labels set by a central authority; "
                    "individual owners have no discretion to grant access, which contradicts the scenario."
                ),
            },
            {
                "id": "d",
                "text": "Attribute-based access control (ABAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. ABAC evaluates policy rules built from subject, object, and environmental "
                    "attributes; the scenario describes no policy engine at all, only owner discretion."
                ),
            },
        ],
        "explanation": (
            "DAC is defined by owner-controlled access: the person who creates or owns a resource decides who "
            "else may access it, without a mandatory label or centrally administered role governing the decision. "
            "This flexibility is convenient but makes DAC harder to audit consistently at enterprise scale."
        ),
    },
    {
        "id": "nd4c-002",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Access control models",
        "stem": (
            "A hospital's EHR system grants clinicians access to patient charts based solely on their assigned "
            "clinical position (e.g., 'Attending Physician,' 'Charge Nurse,' 'Pharmacist'). A newly hired "
            "physician receives the exact same chart-access permissions as every other attending physician the "
            "moment their account is placed in that position group, with no additional per-user configuration. "
            "Which access control model is in use?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Role-based access control (RBAC)",
                "correct": True,
                "rationale": (
                    "Correct. Permissions are bound to a defined position/role, and every user placed in that "
                    "role inherits identical access automatically — the defining trait of RBAC."
                ),
            },
            {
                "id": "b",
                "text": "Attribute-based access control (ABAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. ABAC would evaluate multiple simultaneous attributes (e.g., patient assignment, "
                    "location, time). Here, a single static role determines access uniformly with no additional "
                    "attribute evaluation described."
                ),
            },
            {
                "id": "c",
                "text": "Discretionary access control (DAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. DAC would let an individual data owner grant access at will; here, access is "
                    "determined centrally by role membership, not by an owner's personal discretion."
                ),
            },
            {
                "id": "d",
                "text": "Mandatory access control (MAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. MAC assigns access using fixed sensitivity/clearance labels set by a security "
                    "authority; the scenario describes a clinical job-function role, not a classification label "
                    "hierarchy."
                ),
            },
        ],
        "explanation": (
            "RBAC grants identical, predictable permissions to every user assigned to a given role, minimizing "
            "administrative overhead for large groups of users who need the same access (e.g., all physicians "
            "sharing chart-read permissions) without requiring individual configuration per user."
        ),
    },
    {
        "id": "nd4c-003",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Application security",
        "stem": (
            "During a code review, a security engineer finds that an internal expense-approval API determines "
            "whether to authorize a reimbursement by reading an 'isManager' boolean field sent in the JSON "
            "request body from the client, rather than checking the authenticated user's actual role on the "
            "server. A tester confirms that editing this field in an intercepted request grants approval "
            "authority to a standard employee account. What is the BEST remediation?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Remove client-supplied authorization fields entirely and enforce the authorization decision server-side using the authenticated user's role stored in the session or token.",
                "correct": True,
                "rationale": (
                    "Correct. The root cause is trusting client-controlled input for an authorization decision. "
                    "Authorization must be derived and enforced server-side from data the client cannot tamper "
                    "with, such as the verified session or a signed token claim."
                ),
            },
            {
                "id": "b",
                "text": "Encrypt the request body in transit using TLS so the 'isManager' field cannot be viewed or modified.",
                "correct": False,
                "rationale": (
                    "Incorrect. TLS protects data from network eavesdroppers but does nothing to stop the "
                    "legitimate, authenticated client from simply setting the field to whatever value it wants "
                    "before encryption is applied."
                ),
            },
            {
                "id": "c",
                "text": "Add client-side JavaScript validation to prevent the 'isManager' field from being edited in the browser.",
                "correct": False,
                "rationale": (
                    "Incorrect. Client-side validation is easily bypassed by directly crafting or replaying HTTP "
                    "requests with tools outside the browser; it provides no real security boundary for an "
                    "authorization decision."
                ),
            },
            {
                "id": "d",
                "text": "Increase the API's session token expiration time to reduce how often users must re-authenticate.",
                "correct": False,
                "rationale": (
                    "Incorrect. Token lifetime is unrelated to this broken access control flaw; shortening or "
                    "lengthening expiration does not stop the server from trusting a forgeable client-supplied "
                    "authorization flag."
                ),
            },
        ],
        "explanation": (
            "This is a broken access control / insecure design flaw: the server trusts client-supplied data to "
            "make a privileged decision. The fix is always to move the authorization check server-side, driven by "
            "data the client cannot forge (verified session state, server-issued claims), never by request body "
            "fields the client controls."
        ),
    },
    {
        "id": "nd4c-004",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Application security",
        "stem": (
            "A mobile banking app is decompiled by a researcher, who finds a hardcoded third-party analytics API "
            "key embedded directly in the app's source. The vendor's response is to obfuscate the code further so "
            "the key is harder to locate through static analysis. Why is this an inadequate long-term fix?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Obfuscation only slows down analysis; a determined attacker can still extract the key through dynamic analysis or by intercepting the app's runtime network traffic, so the secret is never truly protected on a client the attacker fully controls.",
                "correct": True,
                "rationale": (
                    "Correct. Obfuscation is security through obscurity — it raises the effort required but does "
                    "not remove the secret from an environment the attacker physically controls. Runtime "
                    "inspection or traffic interception will still reveal the key."
                ),
            },
            {
                "id": "b",
                "text": "Obfuscation is illegal to apply to mobile application binaries under most app store policies.",
                "correct": False,
                "rationale": (
                    "Incorrect. Code obfuscation is a common, legitimate practice permitted by app stores; the "
                    "issue is that it does not solve the underlying secret-exposure problem, not that it is "
                    "prohibited."
                ),
            },
            {
                "id": "c",
                "text": "Obfuscated code always fails static application security testing (SAST) scans, blocking releases.",
                "correct": False,
                "rationale": (
                    "Incorrect. Obfuscation does not inherently cause SAST tooling to fail a build; this is not "
                    "the reason obfuscation fails to remediate a hardcoded secret."
                ),
            },
            {
                "id": "d",
                "text": "Obfuscation increases the app's binary size beyond what app stores allow for publication.",
                "correct": False,
                "rationale": (
                    "Incorrect. Obfuscation has a negligible effect on binary size relative to app store limits "
                    "and is irrelevant to whether the secret remains extractable."
                ),
            },
        ],
        "explanation": (
            "Any secret embedded in client-side code the attacker can obtain (a mobile binary, a browser bundle) "
            "should be treated as compromised. The correct fix is removing the secret from the client entirely — "
            "proxy the analytics call through a backend service that holds the key server-side — not making the "
            "client harder to read."
        ),
    },
    {
        "id": "nd4c-005",
        "domain": 4,
        "objective": "4.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Asset management",
        "stem": (
            "Six months after acquiring a subsidiary company, a security team discovers 200 servers in the "
            "subsidiary's former network with no assigned owner in the CMDB, unknown patch levels, and no asset "
            "tags, despite the subsidiary's network already being routed into the parent company's environment. "
            "Which practice would MOST directly have prevented this exposure?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Incorporating a formal asset discovery, inventory, and ownership-assignment step into the merger/acquisition onboarding process before granting network connectivity.",
                "correct": True,
                "rationale": (
                    "Correct. Asset management requires that newly acquired infrastructure be inventoried, "
                    "tagged, and assigned an owner as part of onboarding, ideally before it is connected to the "
                    "broader corporate network — closing exactly this kind of visibility gap."
                ),
            },
            {
                "id": "b",
                "text": "Requiring the subsidiary's employees to complete annual security awareness training.",
                "correct": False,
                "rationale": (
                    "Incorrect. Awareness training addresses user behavior, not the technical process of "
                    "discovering, tagging, and assigning ownership to unmanaged infrastructure."
                ),
            },
            {
                "id": "c",
                "text": "Applying full-disk encryption to all servers in the subsidiary's data center.",
                "correct": False,
                "rationale": (
                    "Incorrect. Encryption protects data confidentiality at rest but does nothing to establish "
                    "inventory visibility, ownership, or patch status for unaccounted-for assets."
                ),
            },
            {
                "id": "d",
                "text": "Migrating the subsidiary's servers to a different IP addressing scheme to match the parent company's standard.",
                "correct": False,
                "rationale": (
                    "Incorrect. Re-addressing servers is a network standardization task; it does not by itself "
                    "produce an inventory, assign ownership, or verify patch compliance."
                ),
            },
        ],
        "explanation": (
            "Mergers and acquisitions are a common source of asset management gaps: infrastructure gets network "
            "connectivity before it is formally inventoried, tagged, and assigned an accountable owner. Onboarding "
            "checklists that require discovery and reconciliation before integration prevent unmanaged assets "
            "from persisting undetected."
        ),
    },
    {
        "id": "nd4c-006",
        "domain": 4,
        "objective": "4.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Automation & orchestration",
        "stem": (
            "A security engineer wants a SIEM alert to automatically trigger a sequence of actions across the "
            "EDR platform, the perimeter firewall, and the IT service desk ticketing system — isolating the host, "
            "blocking the destination IP, and opening a ticket — using each tool's API, without writing "
            "custom point-to-point integration code between every pair of tools. Which capability BEST fits this "
            "requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A SOAR platform's orchestration layer, connecting the tools through prebuilt integrations and executing a defined playbook",
                "correct": True,
                "rationale": (
                    "Correct. SOAR orchestration is purpose-built to connect disparate security tools through "
                    "prebuilt API integrations and execute a single, coordinated multi-tool workflow from one "
                    "triggering event, avoiding custom point-to-point code."
                ),
            },
            {
                "id": "b",
                "text": "SIEM correlation rules configured with a higher alert severity threshold",
                "correct": False,
                "rationale": (
                    "Incorrect. Correlation rules only determine when an alert fires; they do not execute actions "
                    "across the firewall, EDR, and ticketing system."
                ),
            },
            {
                "id": "c",
                "text": "A vulnerability management platform's scheduled scan feature",
                "correct": False,
                "rationale": (
                    "Incorrect. A vulnerability scanner identifies weaknesses on a schedule; it has no role in "
                    "responding to a live alert across multiple operational tools."
                ),
            },
            {
                "id": "d",
                "text": "Individual bash or PowerShell scripts written and maintained separately for each tool's API",
                "correct": False,
                "rationale": (
                    "Incorrect. This is exactly the custom, point-to-point integration approach the engineer is "
                    "trying to avoid; it does not provide unified orchestration or a maintainable playbook."
                ),
            },
        ],
        "explanation": (
            "SOAR platforms differentiate themselves from standalone scripting by offering a library of prebuilt "
            "connectors and a playbook engine that orchestrates multiple tools' APIs from a single trigger, "
            "reducing the custom-integration burden described in the scenario."
        ),
    },
    {
        "id": "nd4c-007",
        "domain": 4,
        "objective": "4.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Automation & orchestration",
        "stem": (
            "A SOC configures an automation rule that auto-closes any alert matching the hash of a known, "
            "digitally signed benign process, to cut down on repetitive triage. Weeks later, an attacker abuses a "
            "legitimately signed binary with that exact same hash to execute malicious commands, and every "
            "resulting alert is auto-closed without analyst review. What risk does this scenario illustrate about "
            "automated alert dispositioning?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Auto-closure rules based on static indicators can be gamed by adversaries who deliberately reproduce the exact conditions the rule was designed to suppress, creating a detection blind spot.",
                "correct": True,
                "rationale": (
                    "Correct. Once an attacker learns which conditions trigger automatic suppression, they can "
                    "intentionally replicate those conditions (e.g., abusing a trusted signed binary) to hide "
                    "malicious activity from analyst view entirely."
                ),
            },
            {
                "id": "b",
                "text": "Automation always increases the total number of false positives generated by the SIEM.",
                "correct": False,
                "rationale": (
                    "Incorrect. Auto-closure rules typically reduce, not increase, the volume of alerts requiring "
                    "manual review; the issue here is a false negative (missed detection), not an increase in "
                    "false positives."
                ),
            },
            {
                "id": "c",
                "text": "SOAR platforms cannot log which alerts were automatically closed, making the activity untraceable.",
                "correct": False,
                "rationale": (
                    "Incorrect. SOAR and SIEM platforms typically retain detailed logs of automated dispositions; "
                    "the risk here is that the suppression logic itself was exploited, not that logging was "
                    "absent."
                ),
            },
            {
                "id": "d",
                "text": "This scenario demonstrates that automation eliminates the need for any future rule tuning.",
                "correct": False,
                "rationale": (
                    "Incorrect. This scenario shows the opposite — that automated suppression rules require "
                    "ongoing tuning and periodic review to ensure they cannot be predictably exploited."
                ),
            },
        ],
        "explanation": (
            "Any static, predictable suppression logic (hash-based auto-closure, allow-listing a signed binary) "
            "creates an opportunity for adversaries who can reproduce those exact conditions to slip malicious "
            "activity past automated triage undetected. Suppression rules should be layered with behavioral "
            "context and reviewed periodically, not relied on as a permanent, unmonitored shortcut."
        ),
    },
    {
        "id": "nd4c-008",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Digital forensics",
        "stem": (
            "During an investigation of a compromised, cloud-hosted virtual machine, the responder cannot attach "
            "a physical hardware write blocker because the underlying storage is virtualized and managed entirely "
            "by the cloud provider's platform. Which approach provides the forensically soundest evidence "
            "preservation in this environment?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Use the cloud provider's native snapshot/API capability to capture a point-in-time image of the volume, then export it and generate a cryptographic hash of the exported image.",
                "correct": True,
                "rationale": (
                    "Correct. Cloud snapshots taken through the provider's control plane create an immutable, "
                    "point-in-time copy without altering the running instance. Hashing the exported image "
                    "provides the same integrity verification a physical write blocker would achieve on-premises."
                ),
            },
            {
                "id": "b",
                "text": "Log into the running instance via SSH/RDP and manually copy the files believed to be relevant to a local workstation.",
                "correct": False,
                "rationale": (
                    "Incorrect. Interactively logging in and selectively copying files modifies access "
                    "timestamps, may miss deleted or hidden artifacts, and does not produce a complete, verifiable "
                    "forensic image."
                ),
            },
            {
                "id": "c",
                "text": "Request that the cloud provider physically ship the underlying disk hardware for offline imaging.",
                "correct": False,
                "rationale": (
                    "Incorrect. In multi-tenant cloud environments, underlying physical storage is shared across "
                    "many customers and cannot be isolated or shipped; this is not a feasible or standard cloud "
                    "forensic process."
                ),
            },
            {
                "id": "d",
                "text": "Wait for the instance to be automatically terminated by its auto-scaling policy and recover evidence from the deallocated storage afterward.",
                "correct": False,
                "rationale": (
                    "Incorrect. Allowing the instance to terminate risks the deallocation and reuse of the "
                    "underlying storage, potentially destroying volatile and even persistent evidence before it "
                    "can be captured."
                ),
            },
        ],
        "explanation": (
            "In cloud environments, provider-native snapshotting through the management API is the accepted "
            "equivalent of a write-blocked physical acquisition: it preserves a verifiable, unaltered point-in-"
            "time copy that can be exported, hashed, and analyzed offline."
        ),
    },
    {
        "id": "nd4c-009",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Digital forensics",
        "stem": (
            "A forensic analyst must capture volatile memory from a running production server suspected of "
            "hosting an in-memory-only implant. Every available memory-acquisition tool requires installing a "
            "small kernel driver and consumes several megabytes of RAM to run. Which statement BEST describes the "
            "inherent trade-off the analyst faces?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Any tool used to acquire live memory will itself alter some volatile system state, so the analyst should use a validated, minimal-footprint tool and thoroughly document the changes it introduces.",
                "correct": True,
                "rationale": (
                    "Correct. This reflects Locard's exchange principle applied to live forensics: interacting "
                    "with a running system inevitably changes some state. The accepted practice is to minimize "
                    "that footprint with trusted tools and document exactly what was introduced, preserving "
                    "defensibility."
                ),
            },
            {
                "id": "b",
                "text": "Live memory acquisition can be performed with zero impact on system state if the tool is run from a read-only USB device.",
                "correct": False,
                "rationale": (
                    "Incorrect. Running the executable from read-only media does not prevent the acquisition "
                    "process from loading into RAM, consuming resources, and installing a driver — some state "
                    "change is unavoidable during live acquisition."
                ),
            },
            {
                "id": "c",
                "text": "Because memory is the most volatile data source, it should be captured only after the server is fully powered down to guarantee a stable image.",
                "correct": False,
                "rationale": (
                    "Incorrect. Powering down the server destroys the contents of RAM entirely, which is the "
                    "opposite of preserving volatile evidence; order of volatility requires capturing memory while "
                    "the system is still running."
                ),
            },
            {
                "id": "d",
                "text": "Evidence obtained through live memory acquisition is inherently inadmissible because the acquisition process modifies the system.",
                "correct": False,
                "rationale": (
                    "Incorrect. Live acquisition evidence is regularly accepted in practice when the process, "
                    "tool validation, and resulting changes are properly documented; it is not automatically "
                    "inadmissible."
                ),
            },
        ],
        "explanation": (
            "Live forensic acquisition always introduces some minimal, unavoidable change to the target system. "
            "Sound practice minimizes that footprint using trusted, validated tools and documents precisely what "
            "was changed, so the impact can be explained and the evidence remains defensible."
        ),
    },
    {
        "id": "nd4c-010",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Digital forensics and chain-of-custody process",
        "stem": (
            "A business-critical database server cannot be taken offline for a standard write-blocked disk "
            "acquisition without violating an availability SLA. The forensic analyst instead performs a live "
            "logical acquisition using a trusted, validated forensic tool while the server remains running. Which "
            "action MOST strengthens the defensibility of this evidence given the constraint?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Generate a cryptographic hash of the acquired data immediately after collection and formally document the business justification for deviating from offline, write-blocked imaging.",
                "correct": True,
                "rationale": (
                    "Correct. When standard procedure cannot be followed, defensibility depends on proving data "
                    "integrity through hashing and clearly documenting why the deviation was necessary, so the "
                    "process can withstand later scrutiny."
                ),
            },
            {
                "id": "b",
                "text": "Skip hashing entirely, since live systems are constantly changing and a hash would not be meaningful.",
                "correct": False,
                "rationale": (
                    "Incorrect. Hashing the acquired data (not the entire live, changing disk) is still essential "
                    "to prove the collected evidence was not further altered after acquisition; omitting it "
                    "weakens the chain of custody significantly."
                ),
            },
            {
                "id": "c",
                "text": "Decline to collect any evidence until the database can be taken fully offline, regardless of the ongoing investigation timeline.",
                "correct": False,
                "rationale": (
                    "Incorrect. Refusing to collect evidence risks losing volatile and time-sensitive data; "
                    "documented live acquisition is an accepted alternative when offline imaging is not feasible."
                ),
            },
            {
                "id": "d",
                "text": "Perform the acquisition after business hours without recording who performed it or what justified the approach.",
                "correct": False,
                "rationale": (
                    "Incorrect. Omitting documentation of who performed the acquisition and why undermines "
                    "accountability and creates exactly the kind of gap that can be used to challenge the "
                    "evidence's integrity."
                ),
            },
        ],
        "explanation": (
            "When standard offline, write-blocked imaging is not operationally feasible, defensibility is "
            "preserved by using validated tools, hashing the result immediately, and thoroughly documenting the "
            "justification for the deviation — not by skipping integrity verification or refusing to act."
        ),
    },
    {
        "id": "nd4c-011",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Digital forensics and chain-of-custody process",
        "stem": (
            "An investigation spans several weeks and requires multiple examiners to access the same piece of "
            "seized evidence at different times. Select TWO practices that strengthen the defensibility of the "
            "chain of custody in this multi-examiner scenario."
        ),
        "options": [
            {
                "id": "a",
                "text": "Each examiner records the date, time, and purpose of access on the custody form and reseals the evidence in tamper-evident packaging immediately after use.",
                "correct": True,
                "rationale": (
                    "Correct. Individually logged access with immediate resealing creates a complete, "
                    "attributable record of every interaction with the evidence, closing any gap an opposing "
                    "party could exploit."
                ),
            },
            {
                "id": "b",
                "text": "The original evidence is stored in a locked, access-logged evidence room, separate from the working copies used for day-to-day analysis.",
                "correct": True,
                "rationale": (
                    "Correct. Separating the pristine original from actively used working copies, combined with "
                    "restricted and logged access, minimizes the risk of accidental alteration to the source "
                    "evidence and supports a clean custody trail."
                ),
            },
            {
                "id": "c",
                "text": "All examiners share a single login account on the forensic workstation to simplify handoffs between shifts.",
                "correct": False,
                "rationale": (
                    "Incorrect. A shared account destroys individual accountability, making it impossible to "
                    "attribute specific actions to a specific examiner — directly undermining chain-of-custody "
                    "integrity."
                ),
            },
            {
                "id": "d",
                "text": "Trusted senior examiners may hand off evidence to one another verbally, without written documentation, since they are both authorized personnel.",
                "correct": False,
                "rationale": (
                    "Incorrect. Every transfer of evidence must be documented in writing regardless of the "
                    "examiners' seniority or trust level; an undocumented verbal handoff creates an unaccounted-"
                    "for gap that can be challenged."
                ),
            },
        ],
        "explanation": (
            "A defensible chain of custody depends on individually attributable, fully documented access to "
            "evidence and physical separation/protection of the original source from working copies. Shared "
            "accounts and undocumented handoffs, even among trusted staff, introduce gaps that opposing counsel "
            "can exploit."
        ),
    },
    {
        "id": "nd4c-012",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "EDR/XDR & DLP",
        "stem": (
            "A DLP policy blocks any outbound email containing a pattern matching a 9-digit number formatted as "
            "XXX-XX-XXXX, intended to catch Social Security numbers. A developer's email containing a synthetic "
            "QA test dataset with randomly generated, correctly formatted but fake SSN-style numbers is blocked. "
            "What does this illustrate, and what is the BEST remediation?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A false positive caused by pure regex pattern matching without data context; the policy should be updated to use exact data matching or validated fingerprinting against known real records instead of a format-only pattern.",
                "correct": True,
                "rationale": (
                    "Correct. Regex-only matching flags anything in the right format, including synthetic test "
                    "data. Exact data matching (EDM) or fingerprinting against actual sensitive records reduces "
                    "false positives by verifying the data is real, not merely formatted correctly."
                ),
            },
            {
                "id": "b",
                "text": "A true positive; the DLP system correctly identified sensitive data and the developer's email should remain permanently blocked.",
                "correct": False,
                "rationale": (
                    "Incorrect. The data is confirmed synthetic and not actual sensitive information; treating "
                    "this as a correct detection ignores the root cause of the false positive."
                ),
            },
            {
                "id": "c",
                "text": "The best fix is to disable DLP scanning for all outbound email sent by the development team.",
                "correct": False,
                "rationale": (
                    "Incorrect. Broadly exempting an entire team removes protection against genuine sensitive "
                    "data leaving through that team's mailboxes, which is a disproportionate and risky response to "
                    "a single false positive."
                ),
            },
            {
                "id": "d",
                "text": "The best fix is to block all outbound email attachments larger than 1 MB regardless of content.",
                "correct": False,
                "rationale": (
                    "Incorrect. Attachment size is unrelated to whether the content matches a sensitive data "
                    "pattern; this would neither fix the false positive nor meaningfully improve detection "
                    "accuracy."
                ),
            },
        ],
        "explanation": (
            "Simple regex-based DLP rules match on format alone and cannot distinguish real sensitive data from "
            "coincidentally formatted synthetic data. Exact data matching or fingerprinting against a known "
            "dataset of actual sensitive records reduces false positives while preserving detection of genuine "
            "data loss."
        ),
    },
    {
        "id": "nd4c-013",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "EDR/XDR & DLP",
        "stem": (
            "An analyst suspects a specific living-off-the-land technique (a legitimate admin binary being abused "
            "to download and execute payloads) may have occurred on other endpoints beyond the one host that "
            "generated an alert. The analyst wants to retroactively search historical process execution and "
            "command-line telemetry across the entire endpoint fleet for that exact pattern. Which capability "
            "BEST supports this retrospective hunt?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The EDR platform's centralized telemetry repository, queried for the specific process and command-line pattern across all enrolled endpoints",
                "correct": True,
                "rationale": (
                    "Correct. EDR agents continuously stream detailed process and command-line telemetry to a "
                    "central repository, which analysts can query retrospectively across the entire fleet for a "
                    "specific pattern — exactly the capability needed for this hunt."
                ),
            },
            {
                "id": "b",
                "text": "The antivirus engine's signature database, updated to detect the specific binary hash involved",
                "correct": False,
                "rationale": (
                    "Incorrect. Signature-based antivirus detects known-bad hashes going forward; it cannot "
                    "retrospectively search historical execution and command-line telemetry across the fleet for "
                    "a behavioral pattern."
                ),
            },
            {
                "id": "c",
                "text": "The DLP engine's content inspection logs for outbound file transfers",
                "correct": False,
                "rationale": (
                    "Incorrect. DLP logs record data movement matching sensitive-content patterns; they do not "
                    "capture process execution or command-line activity relevant to a living-off-the-land "
                    "technique."
                ),
            },
            {
                "id": "d",
                "text": "The network access control (NAC) solution's device posture assessment history",
                "correct": False,
                "rationale": (
                    "Incorrect. NAC posture history records compliance state at the time of network admission; "
                    "it does not contain process-level execution telemetry needed to hunt for this technique."
                ),
            },
        ],
        "explanation": (
            "EDR's core strength beyond real-time alerting is its centralized, queryable repository of endpoint "
            "telemetry, which enables retrospective threat hunting across the entire fleet for specific "
            "behavioral patterns — something signature-based AV, DLP, and NAC are not designed to provide."
        ),
    },
    {
        "id": "nd4c-014",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Email security (SPF/DKIM/DMARC)",
        "stem": (
            "A company migrates outbound email delivery to a new cloud email provider. After the migration, "
            "recipients that perform strict SPF alignment checks begin rejecting all outbound mail, even though "
            "the new provider's servers are correctly relaying every message. What is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The domain's SPF TXT record was not updated to include the new provider's sending IP ranges, so the new provider's servers are not listed as authorized senders.",
                "correct": True,
                "rationale": (
                    "Correct. SPF authorizes specific sending IPs/hosts listed in the domain's DNS TXT record. If "
                    "the record still reflects the old provider only, mail relayed through the new provider's "
                    "unlisted IPs will fail SPF validation for every recipient enforcing it."
                ),
            },
            {
                "id": "b",
                "text": "DKIM signing must have failed because the new provider does not support digital signatures.",
                "correct": False,
                "rationale": (
                    "Incorrect. The failures described are specifically SPF-related; nothing in the scenario "
                    "indicates a DKIM signing capability issue, and most modern providers support DKIM signing."
                ),
            },
            {
                "id": "c",
                "text": "The domain's DNS TTL (time to live) value is set too high, permanently preventing any future record from taking effect.",
                "correct": False,
                "rationale": (
                    "Incorrect. A high TTL only delays propagation temporarily; it does not permanently block "
                    "updates from eventually taking effect, and it is not the most likely root cause of a "
                    "persistent SPF failure after migration."
                ),
            },
            {
                "id": "d",
                "text": "DMARC must be misconfigured, since DMARC alone determines whether SPF passes or fails.",
                "correct": False,
                "rationale": (
                    "Incorrect. DMARC consumes the results of SPF and DKIM checks for alignment decisions; it "
                    "does not control whether SPF itself passes or fails, which depends solely on the SPF record's "
                    "authorized sender list."
                ),
            },
        ],
        "explanation": (
            "SPF failures after a mail provider migration are almost always caused by an outdated SPF record that "
            "does not yet include the new provider's authorized sending infrastructure. The SPF TXT record must "
            "be updated (typically via an 'include:' mechanism) whenever sending infrastructure changes."
        ),
    },
    {
        "id": "nd4c-015",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Email security (SPF/DKIM/DMARC)",
        "stem": (
            "A domain's SPF record correctly ends in '-all' (hard fail). Despite this, spoofed messages that "
            "display the organization's exact domain in the visible 'From' header still reach some users' "
            "inboxes. Analysis shows these spoofed messages use a completely different, unrelated domain in the "
            "hidden 'Return-Path' (envelope-from/MAIL FROM). What explains why SPF alone did not stop this mail?"
        ),
        "options": [
            {
                "id": "a",
                "text": "SPF validates the envelope sender (Return-Path) domain, not the visible header 'From' domain, so a mismatched envelope sender from an unrelated domain can pass its own SPF check while the visible From is spoofed — this requires DMARC with an enforcing policy to catch.",
                "correct": True,
                "rationale": (
                    "Correct. SPF only checks whether the sending IP is authorized for the Return-Path domain. An "
                    "attacker using their own legitimately SPF-authorized domain in the envelope, while spoofing "
                    "the visible From header, passes SPF; only DMARC's header-From alignment check (in "
                    "quarantine/reject mode) closes this gap."
                ),
            },
            {
                "id": "b",
                "text": "The SPF record must contain a syntax error, since a properly formatted '-all' record would have blocked all spoofed mail regardless of which header was forged.",
                "correct": False,
                "rationale": (
                    "Incorrect. A syntactically correct '-all' record behaves exactly as described here — it only "
                    "evaluates the envelope sender domain, so a mismatched visible From header can still get "
                    "through on its own merits without any syntax error being involved."
                ),
            },
            {
                "id": "c",
                "text": "DKIM alone, without SPF or DMARC, would have been fully sufficient to prevent this specific spoofing technique.",
                "correct": False,
                "rationale": (
                    "Incorrect. DKIM validates message integrity via a signature tied to the signing domain, but "
                    "if the attacker's messages are unsigned or signed by their own domain, DKIM alone does not "
                    "stop the visible From header from being spoofed either; DMARC alignment is still required."
                ),
            },
            {
                "id": "d",
                "text": "SPF records should never end in '-all'; using '~all' (soft fail) instead would have prevented this specific spoofing scenario.",
                "correct": False,
                "rationale": (
                    "Incorrect. Changing the qualifier from hard fail to soft fail would only make policy "
                    "enforcement weaker, not stronger, and does not address the underlying issue — SPF checking "
                    "the wrong header entirely."
                ),
            },
        ],
        "explanation": (
            "SPF evaluates only the envelope sender (Return-Path), while the visible 'From' header users see is "
            "checked for alignment by DMARC. Spoofers exploit this gap by using their own SPF-valid domain in the "
            "envelope while forging the display From address. Only DMARC configured in quarantine or reject mode, "
            "which enforces From-header alignment, closes this loophole."
        ),
    },
    {
        "id": "nd4c-016",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Federation & SSO (SAML/OAuth)",
        "stem": (
            "A malicious actor registers a third-party application with an OAuth authorization server and sends "
            "victims a phishing link containing a 'redirect_uri' parameter pointing to an attacker-controlled "
            "domain that closely resembles the legitimate application's callback URL. When a victim approves the "
            "consent prompt, the authorization code is delivered to the attacker's server instead of the "
            "legitimate application. Which control would MOST effectively prevent this attack?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Configuring the authorization server to accept only exact-match, pre-registered redirect URIs for each registered client application.",
                "correct": True,
                "rationale": (
                    "Correct. Strict allow-listing of exact, pre-registered redirect URIs prevents the "
                    "authorization server from ever delivering an authorization code to an attacker-controlled "
                    "domain, regardless of what value is supplied in the request."
                ),
            },
            {
                "id": "b",
                "text": "Increasing the lifetime of issued access tokens so users are prompted to re-authenticate less frequently.",
                "correct": False,
                "rationale": (
                    "Incorrect. Token lifetime has no bearing on where the authorization code is delivered during "
                    "the initial redirect; it does not address the redirect URI manipulation itself."
                ),
            },
            {
                "id": "c",
                "text": "Requiring the user to re-enter their password immediately before the consent screen is displayed.",
                "correct": False,
                "rationale": (
                    "Incorrect. Re-authentication confirms the user's identity but does not validate or restrict "
                    "where the authorization code is subsequently redirected after consent is granted."
                ),
            },
            {
                "id": "d",
                "text": "Switching the application from the authorization code flow to the implicit flow to simplify the exchange.",
                "correct": False,
                "rationale": (
                    "Incorrect. The implicit flow returns tokens directly in the URL fragment with weaker "
                    "protections than the authorization code flow and does not solve redirect URI validation; it "
                    "would generally make token exposure risk worse, not better."
                ),
            },
        ],
        "explanation": (
            "Open redirect abuse against OAuth flows is mitigated by requiring the authorization server to "
            "validate the 'redirect_uri' against an exact-match allow-list registered in advance for each client, "
            "so a look-alike or attacker-controlled URI is rejected outright rather than accepted."
        ),
    },
    {
        "id": "nd4c-017",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Federation & SSO (SAML/OAuth)",
        "stem": (
            "An employee is terminated and their account is immediately disabled in the corporate identity "
            "provider (IdP). Three days later, the former employee is still able to access a federated SaaS CRM "
            "application using a browser session that was already active before termination. What MOST likely "
            "explains this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The SaaS application maintains its own long-lived session/token at the service provider that is not automatically invalidated when the account is disabled at the IdP, since federated SSO typically governs new logins rather than continuously revalidating existing sessions.",
                "correct": True,
                "rationale": (
                    "Correct. Federated SSO authenticates at login time; unless the service provider is "
                    "specifically configured for frequent session revalidation or the IdP pushes a deprovisioning "
                    "event (e.g., via SCIM), an already-established session at the SP can continue to function "
                    "after the IdP account is disabled."
                ),
            },
            {
                "id": "b",
                "text": "Disabling an account in the IdP always immediately terminates every active session at every federated service provider in real time.",
                "correct": False,
                "rationale": (
                    "Incorrect. This is not guaranteed behavior; without specific session revalidation, short "
                    "token lifetimes, or automated deprovisioning integration, existing SP sessions can persist "
                    "well after IdP-side disablement, as this scenario demonstrates."
                ),
            },
            {
                "id": "c",
                "text": "The former employee must have obtained a new password reset link after termination.",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario describes continued use of an already-active session, not a new "
                    "login requiring credentials; a password reset is not relevant to sustaining an existing "
                    "session."
                ),
            },
            {
                "id": "d",
                "text": "Multifactor authentication was not enforced at the IdP, which is why the session persisted.",
                "correct": False,
                "rationale": (
                    "Incorrect. MFA affects the strength of the initial login, not whether an already-established "
                    "session continues to function after the account is later disabled."
                ),
            },
        ],
        "explanation": (
            "Federated SSO primarily governs authentication at login time. Without short-lived tokens, frequent "
            "session revalidation against the IdP, or automated deprovisioning (such as SCIM push notifications "
            "to the service provider), an existing session can outlive the disabling of the source account, "
            "which is why offboarding processes must also address active session termination at each SP."
        ),
    },
    {
        "id": "nd4c-018",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Hardening & secure baselines",
        "stem": (
            "A vulnerability scan of a production SQL database server flags that the operating system's built-in "
            "web server, FTP service, and telnet daemon are all enabled and listening, even though none of them "
            "are used by the database application. Which hardening principle does this finding violate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Least functionality — unnecessary services should be disabled or removed to reduce the attack surface.",
                "correct": True,
                "rationale": (
                    "Correct. The principle of least functionality requires systems to run only the services "
                    "necessary for their intended purpose. Unused services like a web server, FTP, and telnet "
                    "on a database host needlessly expand the attack surface."
                ),
            },
            {
                "id": "b",
                "text": "Full-disk encryption, since the unused services indicate the disk is not adequately encrypted.",
                "correct": False,
                "rationale": (
                    "Incorrect. Disk encryption protects data at rest and is unrelated to whether unnecessary "
                    "network-facing services are enabled on the host."
                ),
            },
            {
                "id": "c",
                "text": "Intrusion detection coverage, since the server should have an IDS instead of being hardened.",
                "correct": False,
                "rationale": (
                    "Incorrect. An IDS can detect exploitation attempts but does not eliminate the unnecessary "
                    "attack surface itself; hardening (disabling unused services) addresses the root cause "
                    "directly."
                ),
            },
            {
                "id": "d",
                "text": "Vulnerability scan scheduling, since the finding should simply be excluded from future scan reports.",
                "correct": False,
                "rationale": (
                    "Incorrect. Suppressing the finding from future reports hides the risk rather than "
                    "remediating it and is not a legitimate response to an accurate finding."
                ),
            },
        ],
        "explanation": (
            "Least functionality (also called attack surface reduction) requires disabling or removing any "
            "service, port, or protocol not strictly required for a system's role. A database server running an "
            "unused web server, FTP, and telnet daemon unnecessarily multiplies the number of exploitable entry "
            "points."
        ),
    },
    {
        "id": "nd4c-019",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Hardening & secure baselines",
        "stem": (
            "Select TWO technical controls that support ONGOING enforcement of a secure configuration baseline "
            "after a server has already been hardened during initial build."
        ),
        "options": [
            {
                "id": "a",
                "text": "A configuration compliance scanning tool that continuously checks systems against the baseline and alerts on drift.",
                "correct": True,
                "rationale": (
                    "Correct. Continuous compliance scanning detects when a system's configuration diverges from "
                    "the approved baseline over time, enabling ongoing enforcement rather than a one-time check."
                ),
            },
            {
                "id": "b",
                "text": "Group Policy Objects (or equivalent configuration management tooling) configured to automatically reapply required settings on a recurring schedule.",
                "correct": True,
                "rationale": (
                    "Correct. Scheduled, automatic reapplication of required settings actively corrects drift as "
                    "soon as it is detected, providing continuous, self-healing baseline enforcement."
                ),
            },
            {
                "id": "c",
                "text": "A single manual hardening pass performed once during the initial server build, with no further verification afterward.",
                "correct": False,
                "rationale": (
                    "Incorrect. A one-time manual pass with no follow-up verification cannot detect or correct "
                    "configuration drift that occurs later in the system's lifecycle."
                ),
            },
            {
                "id": "d",
                "text": "Disabling vulnerability and configuration scanning once the server initially passes its baseline review.",
                "correct": False,
                "rationale": (
                    "Incorrect. Disabling ongoing scanning removes the very visibility needed to detect future "
                    "drift, directly undermining continuous baseline enforcement."
                ),
            },
        ],
        "explanation": (
            "Maintaining a secure baseline over time requires continuous compliance monitoring and automated "
            "remediation/reapplication mechanisms (such as scheduled GPO refresh or configuration management "
            "agents), not a one-time hardening effort followed by no further verification."
        ),
    },
    {
        "id": "nd4c-020",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Incident response process",
        "stem": (
            "An incident response team confirms that an attacker exfiltrated a database containing customer "
            "Social Security numbers. The organization's incident response plan requires notifying legal and "
            "executive leadership once an incident is classified as a 'confirmed data breach involving regulated "
            "PII.' What should happen NEXT, in parallel with continued technical containment and eradication?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Trigger the predefined communication plan to notify legal and executive leadership now that the classification threshold has been met.",
                "correct": True,
                "rationale": (
                    "Correct. Once an incident meets a predefined classification threshold, the communication "
                    "plan should be triggered immediately and in parallel with technical response, since legal "
                    "and regulatory notification clocks and executive decision-making often depend on early "
                    "awareness, not waiting for full resolution."
                ),
            },
            {
                "id": "b",
                "text": "Wait until root cause analysis is fully complete and the incident is entirely resolved before notifying anyone outside the technical team.",
                "correct": False,
                "rationale": (
                    "Incorrect. Delaying notification until full resolution can cause the organization to miss "
                    "legally mandated breach-notification windows and prevents leadership from making timely "
                    "risk-based decisions."
                ),
            },
            {
                "id": "c",
                "text": "Assign the legal department to perform the forensic disk imaging so the technical team can focus solely on containment.",
                "correct": False,
                "rationale": (
                    "Incorrect. Forensic imaging is a technical function requiring trained responders; "
                    "reassigning it to legal staff is not an appropriate use of that team's role and does not "
                    "reflect the communication plan's actual purpose."
                ),
            },
            {
                "id": "d",
                "text": "Delay all internal and external notification until law enforcement specifically requests it.",
                "correct": False,
                "rationale": (
                    "Incorrect. Internal notification to legal and leadership should follow the organization's "
                    "own predefined classification criteria, not be contingent on an external law enforcement "
                    "request, which may never come or may come too late for compliance obligations."
                ),
            },
        ],
        "explanation": (
            "Incident response plans typically define classification thresholds that automatically trigger "
            "stakeholder notification (legal, executive leadership) as soon as they are met, running in parallel "
            "with ongoing technical containment and eradication rather than waiting until the incident is fully "
            "closed."
        ),
    },
    {
        "id": "nd4c-021",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Incident response process",
        "stem": (
            "A SOC analyst must triage three simultaneous alerts: (1) a guest Wi-Fi VLAN device generating port "
            "scan traffic against other guest devices, (2) a domain controller showing signs of a Kerberoasting "
            "attempt, and (3) a marketing employee's laptop displaying a benign adware pop-up. Applying incident "
            "prioritization principles based on criticality and potential impact, which should be investigated "
            "FIRST?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The domain controller showing signs of Kerberoasting, due to its potential to lead to full domain compromise.",
                "correct": True,
                "rationale": (
                    "Correct. A successful Kerberoasting attack against a domain controller can yield crackable "
                    "service account credentials leading to privilege escalation and domain-wide compromise, "
                    "making it the highest-impact, highest-criticality alert of the three."
                ),
            },
            {
                "id": "b",
                "text": "The guest Wi-Fi device generating port scan traffic, since scanning activity should always be treated as the most urgent indicator.",
                "correct": False,
                "rationale": (
                    "Incorrect. While worth investigating, port scanning confined to an isolated guest VLAN "
                    "against other guest devices carries far lower potential business impact than a credential-"
                    "theft technique targeting a domain controller."
                ),
            },
            {
                "id": "c",
                "text": "The marketing employee's laptop with the adware pop-up, since end-user complaints should always be resolved first.",
                "correct": False,
                "rationale": (
                    "Incorrect. Adware is a low-severity nuisance with minimal organizational impact compared to "
                    "a potential domain-wide compromise vector; user-reported issues do not automatically take "
                    "priority over higher-criticality technical alerts."
                ),
            },
            {
                "id": "d",
                "text": "All three alerts in the order they were received, since incident queues should always be handled first-in-first-out.",
                "correct": False,
                "rationale": (
                    "Incorrect. Effective incident response prioritizes based on potential impact and "
                    "criticality, not strictly the order alerts arrived; a first-in-first-out approach could "
                    "delay response to the most damaging incident."
                ),
            },
        ],
        "explanation": (
            "Incident prioritization weighs potential business impact and asset criticality, not arrival order or "
            "alert type alone. A credential-theft technique against a domain controller threatens the entire "
            "identity infrastructure and must be triaged ahead of lower-impact issues like isolated guest-network "
            "scanning or adware."
        ),
    },
    {
        "id": "nd4c-022",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log data sources",
        "stem": (
            "An analyst needs to determine the total volume and destination of data transferred from a "
            "compromised host over the past 30 days without storing full packet captures, which would require "
            "prohibitive amounts of storage. Which log source BEST meets this need?"
        ),
        "options": [
            {
                "id": "a",
                "text": "NetFlow/IPFIX flow records capturing source, destination, byte counts, and duration for each session",
                "correct": True,
                "rationale": (
                    "Correct. Flow records summarize metadata about network sessions — source/destination, bytes "
                    "transferred, duration — without storing full payload content, making them far more storage-"
                    "efficient than packet capture while still answering 'how much data went where.'"
                ),
            },
            {
                "id": "b",
                "text": "Full packet capture (PCAP) retained for the entire 30-day period",
                "correct": False,
                "rationale": (
                    "Incorrect. Full packet capture directly contradicts the requirement to avoid the storage "
                    "overhead of retaining complete packet contents for an extended period."
                ),
            },
            {
                "id": "c",
                "text": "The host's local operating system event log",
                "correct": False,
                "rationale": (
                    "Incorrect. OS event logs record local system and application events; they generally do not "
                    "capture aggregate network data volume and destination information the way flow data does."
                ),
            },
            {
                "id": "d",
                "text": "Antivirus signature-update logs from the endpoint",
                "correct": False,
                "rationale": (
                    "Incorrect. AV update logs record only when definition files were downloaded and applied; "
                    "they contain no information about data volume or network destinations."
                ),
            },
        ],
        "explanation": (
            "NetFlow/IPFIX provides lightweight, metadata-only records of network sessions that are ideal for "
            "answering volumetric and destination-based questions over long retention periods without the "
            "storage cost of full packet capture."
        ),
    },
    {
        "id": "nd4c-023",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log data sources",
        "stem": (
            "A Linux server was compromised, and the investigator needs to determine every command executed with "
            "elevated privileges by a specific local account during the intrusion window. Which log source should "
            "the investigator prioritize?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The system's sudo/authentication log (e.g., /var/log/auth.log or /var/log/secure) recording each sudo command invocation",
                "correct": True,
                "rationale": (
                    "Correct. The sudo/auth log records each privilege-elevation event, including the invoking "
                    "user and the exact command executed, directly answering which elevated commands the account "
                    "ran during the intrusion window."
                ),
            },
            {
                "id": "b",
                "text": "The cron job scheduler's execution log",
                "correct": False,
                "rationale": (
                    "Incorrect. Cron logs record scheduled, automated job executions; they do not capture "
                    "interactively invoked sudo commands run by a specific user account."
                ),
            },
            {
                "id": "c",
                "text": "The kernel ring buffer (dmesg) output",
                "correct": False,
                "rationale": (
                    "Incorrect. dmesg records low-level kernel and hardware events (driver messages, boot "
                    "diagnostics); it does not log user-invoked commands or which account executed them."
                ),
            },
            {
                "id": "d",
                "text": "The package manager's installation history log",
                "correct": False,
                "rationale": (
                    "Incorrect. Package manager logs only record software installation and update activity; they "
                    "do not capture the full range of privileged commands a user account executed."
                ),
            },
        ],
        "explanation": (
            "On Linux systems, sudo invocations are recorded in the authentication log, capturing the invoking "
            "user, timestamp, and the exact command run with elevated privileges — the authoritative source for "
            "reconstructing privileged command activity during an intrusion."
        ),
    },
    {
        "id": "nd4c-024",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Malware classification",
        "stem": (
            "A disgruntled systems administrator embeds code in a payroll application that silently checks, once "
            "a week, whether his own account is still a member of the IT admin group. If his account is ever "
            "removed from that group (e.g., after his termination), the code triggers deletion of the entire "
            "payroll database. Which malware classification BEST describes this code?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Logic bomb",
                "correct": True,
                "rationale": (
                    "Correct. A logic bomb lies dormant until a specific triggering condition is met — in this "
                    "case, the administrator's removal from the admin group — at which point it executes a "
                    "damaging payload, exactly as described."
                ),
            },
            {
                "id": "b",
                "text": "Worm",
                "correct": False,
                "rationale": (
                    "Incorrect. A worm self-propagates across systems/networks without user interaction; this "
                    "code does not spread anywhere and instead remains dormant on a single system until a "
                    "specific condition triggers it."
                ),
            },
            {
                "id": "c",
                "text": "Ransomware",
                "correct": False,
                "rationale": (
                    "Incorrect. Ransomware encrypts data and demands payment for its release; this code instead "
                    "deletes data outright as a sabotage/retaliation payload with no extortion component."
                ),
            },
            {
                "id": "d",
                "text": "Trojan",
                "correct": False,
                "rationale": (
                    "Incorrect. A trojan disguises itself as legitimate software to trick a user into installing "
                    "or running it; this code is instead embedded within an existing legitimate application by an "
                    "insider, with a condition-based trigger rather than a disguise-based delivery method."
                ),
            },
        ],
        "explanation": (
            "A logic bomb is malicious code that remains inactive until a specific event or condition occurs — "
            "here, the removal of the administrator's group membership — at which point it executes its damaging "
            "payload. This is a classic insider-threat sabotage pattern."
        ),
    },
    {
        "id": "nd4c-025",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Malware classification",
        "stem": (
            "An antivirus vendor updates its signature database after detecting a malware sample with a specific "
            "file hash. Within hours, dozens of new infections appear across the environment, each with a "
            "completely different file hash and slightly altered code structure, yet all exhibiting identical "
            "malicious behavior. Signature-based detection fails to catch the new variants. Which malware "
            "characteristic is being demonstrated, and what detection approach is needed instead?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Polymorphism — the malware changes its code/signature on each iteration while preserving functionality, requiring behavior-based or heuristic detection rather than static signature matching.",
                "correct": True,
                "rationale": (
                    "Correct. Polymorphic malware alters its code (and therefore its hash/signature) with each "
                    "propagation while keeping its underlying malicious behavior consistent, which defeats static "
                    "signature-based detection and requires behavioral or heuristic analysis instead."
                ),
            },
            {
                "id": "b",
                "text": "Rootkit behavior — the malware is hiding its presence from the operating system's process list.",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario describes changing file hashes and code structure across infections, "
                    "not concealment of running processes from the OS, which is the defining trait of a rootkit."
                ),
            },
            {
                "id": "c",
                "text": "Spyware behavior — the malware is covertly collecting and exfiltrating user data.",
                "correct": False,
                "rationale": (
                    "Incorrect. Nothing in the scenario describes data collection or exfiltration; the described "
                    "trait is the malware's changing code structure evading signature detection, which is a "
                    "spyware-unrelated characteristic."
                ),
            },
            {
                "id": "d",
                "text": "Botnet zombie behavior — the infected hosts are being centrally commanded to attack a third party.",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario does not mention command-and-control communication or coordinated "
                    "attacks against a third party; it focuses specifically on the malware's changing signature "
                    "evading detection."
                ),
            },
        ],
        "explanation": (
            "Polymorphic (and metamorphic) malware alters its own code with each infection to generate a unique "
            "hash/signature while retaining the same malicious functionality, defeating static signature-based "
            "antivirus. Detecting it requires behavior-based, heuristic, or machine-learning approaches that "
            "focus on what the code does rather than what it looks like."
        ),
    },
    {
        "id": "nd4c-026",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile device management",
        "stem": (
            "An organization's MDM policy blocks installation of applications from unauthorized sources, but a "
            "user enables developer/unknown-sources options on their managed Android device to sideload an app "
            "outside the enterprise app store. Which MDM capability should the organization rely on to prevent "
            "this device from accessing corporate resources once this configuration change is detected?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A compliance policy that flags devices with sideloading/unknown-sources enabled as non-compliant and automatically blocks access to corporate resources via conditional access.",
                "correct": True,
                "rationale": (
                    "Correct. MDM compliance policies continuously evaluate device configuration state and, when "
                    "integrated with conditional access, automatically revoke access to corporate resources the "
                    "moment a device falls out of compliance — such as enabling sideloading."
                ),
            },
            {
                "id": "b",
                "text": "Geofencing that restricts corporate email access to a defined physical office location.",
                "correct": False,
                "rationale": (
                    "Incorrect. Geofencing controls access based on physical location, not device configuration "
                    "state; it would not detect or respond to the user enabling sideloading capability."
                ),
            },
            {
                "id": "c",
                "text": "Application containerization that separates corporate and personal data within managed apps.",
                "correct": False,
                "rationale": (
                    "Incorrect. Containerization isolates corporate data within managed apps but does not itself "
                    "detect or prevent the underlying OS setting change that enables sideloading outside the "
                    "container."
                ),
            },
            {
                "id": "d",
                "text": "A reactive remote wipe triggered manually only after a data breach has already been confirmed.",
                "correct": False,
                "rationale": (
                    "Incorrect. Remote wipe is a reactive, after-the-fact response to a confirmed incident; it "
                    "does not proactively detect the configuration change or prevent access before damage occurs."
                ),
            },
        ],
        "explanation": (
            "Continuous compliance policies integrated with conditional access allow an MDM solution to "
            "automatically detect risky configuration changes (like enabling sideloading) and immediately restrict "
            "the non-compliant device's access to corporate resources, rather than relying on reactive measures "
            "or controls unrelated to configuration state."
        ),
    },
    {
        "id": "nd4c-027",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile device management",
        "stem": (
            "A large portion of an organization's workforce refuses full MDM enrollment on personally owned "
            "phones, citing privacy concerns about the organization having control over their entire device. The "
            "security team still needs to protect corporate email and documents accessed through a single "
            "approved productivity app, and must be able to remove only that corporate data if the employee "
            "leaves. Which approach BEST satisfies both requirements?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Mobile application management (MAM) with app-level containerization, managing and remotely wiping only the corporate app's data rather than the entire device.",
                "correct": True,
                "rationale": (
                    "Correct. MAM operates at the application level, applying policy and enabling selective wipe "
                    "of corporate data within a specific managed app, without requiring full-device MDM "
                    "enrollment — directly addressing employee privacy concerns while still protecting corporate "
                    "data."
                ),
            },
            {
                "id": "b",
                "text": "Full MDM enrollment enforced for every personally owned device, regardless of employee objections.",
                "correct": False,
                "rationale": (
                    "Incorrect. This directly contradicts the stated constraint that employees are refusing full "
                    "device enrollment; forcing it does not resolve the underlying privacy objection."
                ),
            },
            {
                "id": "c",
                "text": "Geofencing that disables the productivity app whenever the device leaves a defined office perimeter.",
                "correct": False,
                "rationale": (
                    "Incorrect. Geofencing restricts access by location and does not address selective data "
                    "wiping upon employee departure or the underlying enrollment/privacy conflict."
                ),
            },
            {
                "id": "d",
                "text": "Jailbreak/root detection alone, without any application-level management or data separation.",
                "correct": False,
                "rationale": (
                    "Incorrect. Jailbreak detection identifies a compromised OS state but does not provide the "
                    "data containerization or selective wipe capability needed to protect corporate data on an "
                    "unenrolled personal device."
                ),
            },
        ],
        "explanation": (
            "Mobile application management (MAM) provides a lighter-weight alternative to full MDM enrollment, "
            "applying policy and enabling selective wipe at the application/container level. This satisfies BYOD "
            "privacy concerns while still protecting corporate data within the managed app."
        ),
    },
    {
        "id": "nd4c-028",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Multifactor authentication",
        "stem": (
            "After repeated credential-phishing incidents in which users entered their password and a one-time "
            "passcode into a convincing fake login page, the security team wants to deploy an authentication "
            "method that cryptographically binds each login challenge to the legitimate site's origin, making "
            "captured credentials unusable if replayed against a phishing domain. Which method BEST meets this "
            "requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "FIDO2/WebAuthn hardware security keys",
                "correct": True,
                "rationale": (
                    "Correct. FIDO2/WebAuthn authentication cryptographically ties each login assertion to the "
                    "specific origin (domain) that requested it. A credential captured or replayed against a "
                    "phishing domain simply will not validate, making this method phishing-resistant by design."
                ),
            },
            {
                "id": "b",
                "text": "SMS-delivered one-time passcodes",
                "correct": False,
                "rationale": (
                    "Incorrect. SMS OTPs are not bound to the requesting origin; a user can be tricked into "
                    "typing a valid code into a phishing site, which the attacker then relays to the real site in "
                    "real time — exactly the weakness the team is trying to eliminate."
                ),
            },
            {
                "id": "c",
                "text": "Push notification approval to a mobile authenticator app without number matching",
                "correct": False,
                "rationale": (
                    "Incorrect. Simple push approval is not cryptographically bound to the origin and remains "
                    "vulnerable to real-time relay/phishing attacks and MFA fatigue, unlike origin-bound "
                    "cryptographic authentication."
                ),
            },
            {
                "id": "d",
                "text": "Knowledge-based security questions as an additional login step",
                "correct": False,
                "rationale": (
                    "Incorrect. Security questions are static, guessable/researchable knowledge factors with no "
                    "cryptographic binding to the requesting site, offering no protection against phishing "
                    "replay."
                ),
            },
        ],
        "explanation": (
            "FIDO2/WebAuthn is the standard example of phishing-resistant MFA: the authentication challenge is "
            "cryptographically bound to the legitimate site's origin, so credentials captured by or relayed "
            "through a phishing domain cannot be validated against the real service."
        ),
    },
    {
        "id": "nd4c-029",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Multifactor authentication",
        "stem": (
            "A bank's mobile app currently authenticates customers with a password and a fingerprint scan on "
            "their registered phone. To comply with a new regulation requiring three distinct authentication "
            "factor categories, the bank adds a requirement that customers must also correctly answer a security "
            "question (e.g., mother's maiden name) before login succeeds. Does this satisfy a genuine three-"
            "factor requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "No — a security question is still a 'something you know' factor, the same category as the password, so this only adds redundancy within one category rather than introducing a third distinct factor category.",
                "correct": True,
                "rationale": (
                    "Correct. Multifactor strength comes from combining distinct categories (knowledge, "
                    "possession, inherence), not from adding more items within the same category. A security "
                    "question and a password are both 'something you know.'"
                ),
            },
            {
                "id": "b",
                "text": "Yes — because the security question asks about different information than the password.",
                "correct": False,
                "rationale": (
                    "Incorrect. The content of the knowledge item does not change its category; both the "
                    "password and the security question remain 'something you know,' regardless of what "
                    "information each one asks for."
                ),
            },
            {
                "id": "c",
                "text": "Yes — because it is presented to the user as an additional, separate login step.",
                "correct": False,
                "rationale": (
                    "Incorrect. Presenting a factor as a separate step does not change its underlying category; "
                    "true multi-factor authentication requires categorically distinct factors, not merely "
                    "sequential steps."
                ),
            },
            {
                "id": "d",
                "text": "No — because a fingerprint scan is not considered a valid authentication factor under most regulatory frameworks.",
                "correct": False,
                "rationale": (
                    "Incorrect. A fingerprint scan is a well-established 'something you are' (inherence) factor "
                    "and is broadly recognized as valid; the flaw in this scenario is the redundant knowledge "
                    "factor, not the biometric."
                ),
            },
        ],
        "explanation": (
            "Genuine multi-factor authentication requires combining categorically distinct factors: something you "
            "know, something you have, and something you are. Adding a second knowledge-based item (a security "
            "question) alongside a password does not introduce a new category — the bank would need to add a "
            "true possession factor, such as a hardware token or push to a registered device, to achieve three "
            "distinct factors."
        ),
    },
    {
        "id": "nd4c-030",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Penetration testing phases",
        "stem": (
            "During an authorized penetration test, testers use a previously compromised low-privilege domain "
            "account to systematically enumerate shared folders, service accounts, and domain trust "
            "relationships, without yet attempting further exploitation, in order to map potential attack paths "
            "for lateral movement. Which phase of the engagement does this activity represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Internal, authenticated reconnaissance/enumeration performed after initial access to plan further attack paths before additional exploitation",
                "correct": True,
                "rationale": (
                    "Correct. Once an initial foothold is gained, testers commonly perform authenticated internal "
                    "enumeration — mapping shares, accounts, and trust relationships — as a reconnaissance step "
                    "that informs subsequent exploitation and lateral movement, rather than exploitation itself."
                ),
            },
            {
                "id": "b",
                "text": "Exploitation, since any activity performed using a compromised account counts as exploitation.",
                "correct": False,
                "rationale": (
                    "Incorrect. Merely enumerating resources with an already-compromised account is "
                    "reconnaissance/information gathering; exploitation refers to actively leveraging a "
                    "vulnerability to gain further access or execute a payload, which has not yet occurred here."
                ),
            },
            {
                "id": "c",
                "text": "Cleanup and reporting, since the engagement is nearing its conclusion.",
                "correct": False,
                "rationale": (
                    "Incorrect. Cleanup and reporting occur at the end of an engagement after testing activities "
                    "conclude; this scenario describes active, ongoing information gathering to plan further "
                    "actions, not a wrap-up activity."
                ),
            },
            {
                "id": "d",
                "text": "Planning and scoping, since the rules of engagement are still being defined.",
                "correct": False,
                "rationale": (
                    "Incorrect. Planning and scoping occur before any technical testing begins and establish the "
                    "rules of engagement; this scenario describes hands-on technical activity well after access "
                    "was already obtained."
                ),
            },
        ],
        "explanation": (
            "Penetration testing reconnaissance is not limited to pre-engagement, unauthenticated information "
            "gathering. Internal enumeration performed after gaining a foothold — mapping shares, accounts, and "
            "trust relationships — is still reconnaissance in service of planning further exploitation and "
            "lateral movement."
        ),
    },
    {
        "id": "nd4c-031",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Penetration testing phases",
        "stem": (
            "At the conclusion of an authorized penetration test, the testing team used a custom persistence "
            "script and created a temporary local administrator account on 12 hosts to facilitate lateral "
            "movement testing. Which action MUST the team perform before the engagement can be considered "
            "complete?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Remove all artifacts introduced during testing — scripts, backdoors, and created accounts — restore affected systems to their pre-engagement state, and document every change made.",
                "correct": True,
                "rationale": (
                    "Correct. Cleanup is a required phase of any authorized penetration test: every tool, "
                    "account, and persistence mechanism introduced must be removed and documented so the client's "
                    "environment is left in its original, secure state."
                ),
            },
            {
                "id": "b",
                "text": "Leave the temporary administrator accounts in place in case a retest is needed later.",
                "correct": False,
                "rationale": (
                    "Incorrect. Leaving unauthorized administrator accounts active after testing concludes "
                    "creates a real, unmanaged security risk and directly violates the requirement to restore "
                    "systems to their original state."
                ),
            },
            {
                "id": "c",
                "text": "Hand off the created credentials to the blue team as-is, without documenting what was created or where.",
                "correct": False,
                "rationale": (
                    "Incorrect. Undocumented handoff of credentials without full detail on what was created and "
                    "where leaves the client unable to verify complete cleanup and creates confusion about which "
                    "accounts are legitimate."
                ),
            },
            {
                "id": "d",
                "text": "Immediately publish the full technical findings, including the persistence script's source code, to a public repository.",
                "correct": False,
                "rationale": (
                    "Incorrect. Publishing sensitive findings and exploitation tooling publicly violates "
                    "confidentiality obligations to the client and has nothing to do with the required cleanup "
                    "process."
                ),
            },
        ],
        "explanation": (
            "The cleanup phase requires penetration testers to remove every artifact they introduced (accounts, "
            "scripts, persistence mechanisms) and restore systems to their pre-test state, with full documentation "
            "provided to the client — this is a mandatory, ethical closing step of any authorized engagement."
        ),
    },
    {
        "id": "nd4c-032",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Port and protocol security",
        "stem": (
            "An external vulnerability scan of a company's public IP range shows TCP port 3389 open and reachable "
            "directly from the internet on a Windows server. Weeks later, ransomware operators are found to have "
            "gained initial access using weak, reused credentials against that exposed service. Which "
            "remediation BEST addresses the root cause of this exposure?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Remove direct internet exposure of RDP entirely, requiring remote access through a VPN or jump host that enforces MFA before RDP is ever reachable.",
                "correct": True,
                "rationale": (
                    "Correct. The root cause is that a high-value remote administration protocol was directly "
                    "reachable from the internet. Eliminating that direct exposure and requiring authenticated, "
                    "MFA-protected VPN/jump-host access removes the attack path entirely, regardless of "
                    "credential strength."
                ),
            },
            {
                "id": "b",
                "text": "Change RDP to listen on a non-standard, obscure port number while keeping it directly internet-facing.",
                "correct": False,
                "rationale": (
                    "Incorrect. Changing the port number is security through obscurity; automated scanning tools "
                    "easily discover services on non-standard ports, and the service remains directly exposed and "
                    "exploitable."
                ),
            },
            {
                "id": "c",
                "text": "Increase the minimum password complexity requirement for the local accounts on the server.",
                "correct": False,
                "rationale": (
                    "Incorrect. Stronger passwords reduce but do not eliminate brute-force or credential-reuse "
                    "risk while the service remains directly internet-facing; the underlying exposure itself is "
                    "not addressed."
                ),
            },
            {
                "id": "d",
                "text": "Install an EDR agent on the server to detect ransomware execution after initial access occurs.",
                "correct": False,
                "rationale": (
                    "Incorrect. EDR improves detection and response after compromise begins but does not prevent "
                    "the initial access vector — a directly internet-exposed remote administration port — from "
                    "being exploited in the first place."
                ),
            },
        ],
        "explanation": (
            "Directly exposing RDP (TCP 3389) to the internet is one of the most common initial access vectors "
            "for ransomware. The correct remediation removes that direct exposure entirely, funneling remote "
            "access through a VPN or jump host with MFA, rather than relying on obscurity, password policy alone, "
            "or after-the-fact detection."
        ),
    },
    {
        "id": "nd4c-033",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Privileged access management",
        "stem": (
            "Every time a network engineer needs to SSH into a core router using the shared 'enable' credential, "
            "they must first check the password out from a PAM vault, which automatically rotates it immediately "
            "after check-in or after a fixed time-to-live expires. Which PAM concept does this describe, and what "
            "is its primary security benefit?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Credential vaulting and automatic rotation, which ensures no individual retains long-term knowledge of a static privileged credential and limits how long any exposed password remains valid.",
                "correct": True,
                "rationale": (
                    "Correct. Vaulting combined with automatic rotation after each use (or on a strict schedule) "
                    "prevents users from memorizing a long-lived shared secret and drastically shrinks the window "
                    "during which a leaked or exposed credential could be exploited."
                ),
            },
            {
                "id": "b",
                "text": "Least privilege role assignment, which limits what actions the engineer's account is authorized to perform.",
                "correct": False,
                "rationale": (
                    "Incorrect. Least privilege concerns the scope of permissions granted, not the lifecycle "
                    "management (checkout, rotation) of the credential itself, which is what the scenario "
                    "describes."
                ),
            },
            {
                "id": "c",
                "text": "Multifactor authentication enforcement, which requires a second verification step for login.",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario describes credential checkout and automatic rotation, not the "
                    "addition of a second authentication factor to the login process."
                ),
            },
            {
                "id": "d",
                "text": "Network segmentation, which isolates the router's management interface from other network segments.",
                "correct": False,
                "rationale": (
                    "Incorrect. Segmentation restricts network reachability to the device; it does not describe "
                    "how the privileged credential itself is stored, checked out, or rotated."
                ),
            },
        ],
        "explanation": (
            "PAM credential vaulting with automatic rotation after each use (or on a strict TTL) is a core "
            "control for shared/static privileged credentials: it eliminates long-term human knowledge of the "
            "secret and minimizes the exposure window if a credential is ever leaked, while also providing an "
            "audit trail of exactly who checked out access and when."
        ),
    },
    {
        "id": "nd4c-034",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Privileged access management",
        "stem": (
            "Select TWO practices that reduce the risk associated with standing (always-on) privileged access to "
            "critical infrastructure."
        ),
        "options": [
            {
                "id": "a",
                "text": "Just-in-time elevation that grants privileged rights only for a limited, approved time window tied to a specific task.",
                "correct": True,
                "rationale": (
                    "Correct. Just-in-time elevation replaces permanent standing privilege with temporary, "
                    "task-scoped access, significantly shrinking the window during which an account holds elevated "
                    "rights and could be abused."
                ),
            },
            {
                "id": "b",
                "text": "Session recording and monitoring of privileged access for later audit and review.",
                "correct": True,
                "rationale": (
                    "Correct. Recording and monitoring privileged sessions provides accountability and detection "
                    "capability, deterring misuse and enabling forensic review of exactly what actions were taken "
                    "during elevated access."
                ),
            },
            {
                "id": "c",
                "text": "Sharing a single privileged account across the entire on-call rotation to simplify handoffs between engineers.",
                "correct": False,
                "rationale": (
                    "Incorrect. Shared accounts eliminate individual accountability and make it impossible to "
                    "attribute privileged actions to a specific person, increasing rather than reducing risk."
                ),
            },
            {
                "id": "d",
                "text": "Granting all senior engineers permanent domain administrator rights so they never need to request access during an outage.",
                "correct": False,
                "rationale": (
                    "Incorrect. Permanent, always-on elevated rights is precisely the standing-privilege exposure "
                    "the organization is trying to reduce, not a mitigation for it."
                ),
            },
        ],
        "explanation": (
            "Reducing standing privilege risk relies on granting elevated access only when needed and for a "
            "limited duration (just-in-time elevation) and on maintaining accountability through session "
            "recording/monitoring — not on shared accounts or permanent administrative rights, both of which "
            "increase exposure and reduce accountability."
        ),
    },
    {
        "id": "nd4c-035",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "A SIEM's user and entity behavior analytics (UEBA) module generates an alert because a service "
            "account that has only ever authenticated during automated batch windows between 2 a.m. and 4 a.m. "
            "suddenly authenticates interactively from a workstation at 11 a.m. and immediately queries a "
            "sensitive database it has never accessed before. What underlying detection technique produced this "
            "alert?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Behavioral/anomaly-based analysis comparing current activity against an established baseline of normal behavior for that specific entity",
                "correct": True,
                "rationale": (
                    "Correct. UEBA builds a baseline of normal behavior per user or entity (typical login times, "
                    "resources accessed) and flags significant deviations from that baseline, exactly as "
                    "described — an unusual login time and an unprecedented resource access for this account."
                ),
            },
            {
                "id": "b",
                "text": "Signature-based detection matching a known indicator of compromise (IOC)",
                "correct": False,
                "rationale": (
                    "Incorrect. No known malicious signature, hash, or IOC is described; the alert is driven by a "
                    "deviation from the account's established behavioral pattern, not a match against a known-bad "
                    "signature."
                ),
            },
            {
                "id": "c",
                "text": "A simple static threshold rule, such as alerting after five failed logins within one minute",
                "correct": False,
                "rationale": (
                    "Incorrect. No failed login count or fixed numeric threshold is involved; the detection is "
                    "based on comparing current behavior to a learned baseline of what is normal for this "
                    "specific entity, not a static count-based rule."
                ),
            },
            {
                "id": "d",
                "text": "A vulnerability scan finding related to the database's patch level",
                "correct": False,
                "rationale": (
                    "Incorrect. Vulnerability scanning identifies weaknesses in systems; it plays no role in "
                    "generating a real-time behavioral alert about a specific account's login time and access "
                    "pattern."
                ),
            },
        ],
        "explanation": (
            "UEBA extends beyond static, rule-based correlation by learning a behavioral baseline for each user "
            "or entity and flagging statistically significant deviations — such as an atypical login time or "
            "access to a resource never previously touched — which static threshold rules and signature matching "
            "cannot detect."
        ),
    },
    {
        "id": "nd4c-036",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "A SOC needs 13 months of log data available to support compliance-driven investigations, but "
            "retaining every log in the SIEM's expensive hot-search index for the entire period is cost-"
            "prohibitive. Which architecture BEST balances ongoing investigative capability with storage cost?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Tiered storage: keep recent logs in the SIEM's hot, searchable index for active detection, and archive older logs to lower-cost cold storage that can be rehydrated and searched on demand.",
                "correct": True,
                "rationale": (
                    "Correct. Tiered log architecture keeps the most operationally relevant, recent data readily "
                    "searchable for real-time detection while archiving older data to cheaper storage, preserving "
                    "the ability to retrieve and search it later for compliance-driven investigations without "
                    "paying hot-index costs for the entire retention period."
                ),
            },
            {
                "id": "b",
                "text": "Reduce overall log retention to 30 days across the board to control cost.",
                "correct": False,
                "rationale": (
                    "Incorrect. Cutting retention to 30 days directly violates the stated 13-month compliance "
                    "requirement, sacrificing investigative capability rather than balancing it with cost."
                ),
            },
            {
                "id": "c",
                "text": "Ingest only summarized alert data rather than raw logs, to reduce the volume stored.",
                "correct": False,
                "rationale": (
                    "Incorrect. Discarding raw log detail in favor of alert summaries removes the granular "
                    "evidence often required for thorough forensic investigation, undermining investigative "
                    "capability."
                ),
            },
            {
                "id": "d",
                "text": "Stop collecting logs from lower-priority systems entirely to reduce ingestion cost.",
                "correct": False,
                "rationale": (
                    "Incorrect. Eliminating log collection from any system creates a visibility gap and could "
                    "leave the organization unable to investigate incidents involving those systems, which does "
                    "not meet the compliance retention requirement."
                ),
            },
        ],
        "explanation": (
            "Tiered storage architectures let organizations meet long compliance-driven retention requirements "
            "affordably: recent, high-value data stays in the expensive, fast-searchable hot tier for active "
            "detection, while older data moves to inexpensive cold storage that remains retrievable when needed "
            "for an investigation."
        ),
    },
    {
        "id": "nd4c-037",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A vulnerability scan flags a critical finding on a legacy application that cannot be patched because "
            "the vendor has declared it end-of-life and no update will ever be released. No compensating control "
            "has yet been documented for this system. What is the MOST appropriate next step in the vulnerability "
            "management process?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Formally document a risk acceptance or exception, including any available compensating controls, and obtain the appropriate management sign-off.",
                "correct": True,
                "rationale": (
                    "Correct. When a vulnerability cannot be remediated through patching, the appropriate process "
                    "is formal risk acceptance: documenting the decision, any compensating controls applied, and "
                    "securing accountable sign-off — not leaving the risk unaddressed or hidden."
                ),
            },
            {
                "id": "b",
                "text": "Mark the finding as a false positive and close it, since patching is not possible.",
                "correct": False,
                "rationale": (
                    "Incorrect. The vulnerability is real and confirmed; mislabeling it as a false positive "
                    "understates the organization's actual risk exposure and bypasses proper governance."
                ),
            },
            {
                "id": "c",
                "text": "Delete the finding from the vulnerability report so it does not affect remediation metrics.",
                "correct": False,
                "rationale": (
                    "Incorrect. Removing a legitimate finding from reporting conceals real risk from stakeholders "
                    "and violates basic vulnerability management integrity and governance practices."
                ),
            },
            {
                "id": "d",
                "text": "Take no action and simply wait for the next scheduled scan cycle to reassess the finding.",
                "correct": False,
                "rationale": (
                    "Incorrect. Passively waiting without documenting a risk decision or compensating control "
                    "leaves the organization exposed with no formal accountability or mitigation in place."
                ),
            },
        ],
        "explanation": (
            "When remediation through patching is impossible, vulnerability management requires a formal, "
            "documented risk acceptance or exception process — including any compensating controls and management "
            "sign-off — rather than mislabeling, hiding, or ignoring the finding."
        ),
    },
    {
        "id": "nd4c-038",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A vulnerability is published with a CVSS base score of 9.8 (Critical). The organization's internal "
            "scoring, adjusted to reflect that the affected system sits behind strict network segmentation with "
            "no reachable path from any untrusted network and processes no sensitive data, results in a "
            "substantially lower adjusted score used to prioritize remediation. Which CVSS metric group accounts "
            "for organization-specific factors like these?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The Environmental metric group",
                "correct": True,
                "rationale": (
                    "Correct. The Environmental metric group allows an organization to modify base metrics and "
                    "apply security-requirement weightings to reflect its own deployment context — such as "
                    "network segmentation and data sensitivity — producing an adjusted score more relevant to "
                    "actual organizational risk."
                ),
            },
            {
                "id": "b",
                "text": "The Base metric group",
                "correct": False,
                "rationale": (
                    "Incorrect. The Base metric group reflects the vulnerability's intrinsic characteristics "
                    "(e.g., attack vector, complexity, impact) and remains constant regardless of any specific "
                    "organization's environment or deployment context."
                ),
            },
            {
                "id": "c",
                "text": "The Temporal metric group",
                "correct": False,
                "rationale": (
                    "Incorrect. Temporal metrics reflect characteristics that change over time for everyone, such "
                    "as exploit code maturity or the availability of an official fix — not organization-specific "
                    "deployment factors like network segmentation."
                ),
            },
            {
                "id": "d",
                "text": "Relying on the Base score alone, since it already accounts for all deployment considerations.",
                "correct": False,
                "rationale": (
                    "Incorrect. The Base score explicitly does not account for any organization-specific "
                    "deployment context; that is precisely the purpose of the separate Environmental metric "
                    "group."
                ),
            },
        ],
        "explanation": (
            "CVSS is composed of Base (intrinsic vulnerability severity), Temporal (time-varying factors like "
            "exploit maturity), and Environmental (organization-specific context, such as compensating controls "
            "and asset criticality) metric groups. Adjusting for network segmentation and data sensitivity is "
            "precisely what the Environmental group is designed to capture for realistic remediation "
            "prioritization."
        ),
    },
    {
        "id": "nd4c-039",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Wireless security",
        "stem": (
            "A security assessment of a corporate wireless network finds it still uses WPA2 with AES-CCMP. The "
            "assessor recommends upgrading to WPA3 primarily because it prevents offline dictionary/brute-force "
            "attacks against a captured authentication handshake, even when a pre-shared key is used. Which WPA3 "
            "feature provides this specific protection?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Simultaneous Authentication of Equals (SAE), which replaces the WPA2 four-way handshake and requires live interaction with the access point for each authentication attempt.",
                "correct": True,
                "rationale": (
                    "Correct. SAE (the 'Dragonfly' handshake) requires each authentication attempt to interact "
                    "live with the access point, making offline brute-force or dictionary attacks against a "
                    "passively captured handshake infeasible — unlike WPA2's four-way handshake, which can be "
                    "captured and attacked offline."
                ),
            },
            {
                "id": "b",
                "text": "Using a longer pre-shared key length while keeping the WPA2 four-way handshake mechanism unchanged.",
                "correct": False,
                "rationale": (
                    "Incorrect. Simply lengthening the key does not change the fundamental weakness that the "
                    "WPA2 four-way handshake can still be captured and attacked offline; the protection comes "
                    "from replacing the handshake mechanism itself, not key length alone."
                ),
            },
            {
                "id": "c",
                "text": "Switching from AES-128 to AES-256 encryption for the data payload.",
                "correct": False,
                "rationale": (
                    "Incorrect. Payload encryption strength does not address how the initial authentication "
                    "handshake is exchanged and does not prevent offline attacks against a captured handshake."
                ),
            },
            {
                "id": "d",
                "text": "Disabling SSID broadcast so the network name is not visible to nearby devices.",
                "correct": False,
                "rationale": (
                    "Incorrect. Hiding the SSID is a weak, easily bypassed obscurity measure and has no effect "
                    "on whether a captured handshake can be attacked offline."
                ),
            },
        ],
        "explanation": (
            "WPA3's SAE handshake replaces WPA2's four-way handshake and requires interactive, live exchanges "
            "with the access point for every authentication attempt, eliminating the ability to passively capture "
            "a handshake and crack it offline — the specific weakness that persists in WPA2-PSK deployments."
        ),
    },
    {
        "id": "nd4c-040",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Wireless security",
        "stem": (
            "Select TWO statements that correctly distinguish WPA2-Enterprise (802.1X) from WPA2-Personal (PSK) "
            "in an office wireless deployment."
        ),
        "options": [
            {
                "id": "a",
                "text": "WPA2-Enterprise authenticates each user or device individually against a RADIUS server using unique credentials or certificates.",
                "correct": True,
                "rationale": (
                    "Correct. WPA2-Enterprise relies on 802.1X port-based authentication against a RADIUS/AAA "
                    "server, allowing each user or device to authenticate with its own unique credentials or "
                    "certificate rather than a single shared secret."
                ),
            },
            {
                "id": "b",
                "text": "WPA2-Personal uses a single shared passphrase for all clients, so fully remediating a compromised passphrase requires updating it on every connected device.",
                "correct": True,
                "rationale": (
                    "Correct. Because all clients share the same PSK, a compromised passphrase must be changed "
                    "and redistributed to every device to close the exposure — there is no way to revoke access "
                    "for a single user without affecting everyone."
                ),
            },
            {
                "id": "c",
                "text": "WPA2-Enterprise cannot support certificate-based authentication and is limited to username/password logins only.",
                "correct": False,
                "rationale": (
                    "Incorrect. WPA2-Enterprise commonly supports certificate-based EAP methods such as EAP-TLS "
                    "in addition to username/password-based methods; certificate authentication is a standard, "
                    "widely used option, not an unsupported one."
                ),
            },
            {
                "id": "d",
                "text": "WPA2-Personal provides per-user accounting and allows individual users to be revoked without affecting other connected users.",
                "correct": False,
                "rationale": (
                    "Incorrect. This describes a strength of WPA2-Enterprise, not WPA2-Personal. Because "
                    "WPA2-Personal uses one shared passphrase for everyone, it cannot provide per-user accounting "
                    "or individual revocation."
                ),
            },
        ],
        "explanation": (
            "WPA2-Enterprise provides per-user authentication and accountability through 802.1X/RADIUS, including "
            "support for certificate-based EAP methods, and allows individual revocation. WPA2-Personal's single "
            "shared passphrase model means a compromise requires rekeying every client and offers no per-user "
            "distinction or selective revocation."
        ),
    },
]

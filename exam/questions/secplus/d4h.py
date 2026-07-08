"""CompTIA Security+ SY0-701 practice questions — Domain 4 (Security Operations), file H."""

QUESTIONS = [
    {
        "id": "nd4h-001",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Access control models",
        "stem": (
            "A cloud storage gateway decides whether to allow a file download by evaluating, at the moment of "
            "each request, the requesting user's group membership, the file's confidentiality tag, a real-time "
            "reputation score looked up from a threat-intelligence feed for the source IP, and whether the user "
            "completed MFA within the last 15 minutes. Which access control model is being used?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Attribute-based access control (ABAC)",
                "correct": True,
                "rationale": (
                    "Correct. The gateway evaluates a combination of subject (group), object (confidentiality "
                    "tag), and dynamic environmental attributes (live threat-intel reputation, MFA recency) "
                    "together in real time, which is the defining behavior of ABAC."
                ),
            },
            {
                "id": "b",
                "text": "Rule-based access control using a static, administrator-defined condition list",
                "correct": False,
                "rationale": (
                    "Incorrect. Rule-based access control evaluates a fixed set of if-then conditions "
                    "programmed in advance by an administrator. Here, the IP reputation score changes "
                    "continuously from an external live feed, which a static rule list cannot incorporate."
                ),
            },
            {
                "id": "c",
                "text": "Role-based access control (RBAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. RBAC would grant or deny access based on group/role membership alone. It has "
                    "no native mechanism to also weigh a real-time threat-intelligence reputation score or "
                    "MFA recency in the same decision."
                ),
            },
            {
                "id": "d",
                "text": "Mandatory access control (MAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. MAC enforces access strictly using fixed classification/clearance labels set "
                    "by a central authority; it does not dynamically factor in live threat-intel scores or "
                    "recent authentication events."
                ),
            },
        ],
        "explanation": (
            "Only ABAC natively combines multiple simultaneous subject, object, and environmental attributes — "
            "including ones that change continuously, like a live IP reputation feed — into a single access "
            "decision. Rule-based control is condition-driven but static; RBAC and MAC each rely on a single "
            "primary criterion."
        ),
    },
    {
        "id": "nd4h-002",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Access control models",
        "stem": (
            "An architecture firm's document platform lets the creator of any blueprint file grant edit or view "
            "access to any internal or external collaborator at their sole discretion, with no central review. "
            "An audit finds hundreds of blueprints for active government contracts now shared with external "
            "partner firms that were never formally approved. Which statement BEST explains the root cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The platform uses discretionary access control (DAC), which inherently allows resource "
                    "owners to propagate access without centralized oversight or classification enforcement."
                ),
                "correct": True,
                "rationale": (
                    "Correct. DAC's defining trait is that the resource owner — not a central authority — "
                    "decides who else gets access. Without a centrally enforced classification policy layered "
                    "on top, owner-level sharing can silently sprawl exactly as described."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The platform uses mandatory access control (MAC), and the sprawl occurred because "
                    "clearance labels were assigned incorrectly by the central authority."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. MAC would never allow the file creator to unilaterally grant access; a central "
                    "authority's labels would govern every sharing decision. The scenario explicitly describes "
                    "owner discretion, not a labeling error."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The platform uses role-based access control (RBAC), and the sprawl occurred because too "
                    "many roles were created over time."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. RBAC ties access to predefined roles, not to an individual file creator's "
                    "personal sharing decisions. Role proliferation is a real RBAC problem, but it does not "
                    "match this scenario's owner-driven sharing behavior."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The platform uses attribute-based access control (ABAC), and the sprawl occurred because "
                    "too many environmental attributes were included in the policy engine."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. ABAC policies are centrally defined and evaluated by a policy engine, not left "
                    "to individual owner discretion. This scenario has no policy engine evaluating attributes "
                    "at all — access is simply granted by whoever created the file."
                ),
            },
        ],
        "explanation": (
            "DAC gives resource owners full discretion to grant access, which is convenient for collaboration "
            "but provides no centralized enforcement of sensitivity or contractual restrictions — exactly the "
            "gap that let sensitive blueprints sprawl to unapproved external partners."
        ),
    },
    {
        "id": "nd4h-003",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Application security",
        "stem": (
            "A SaaS HR platform's 'update my profile' API endpoint accepts a full JSON object from the client "
            "and writes every field it contains directly to the user's database record. A tester adds a "
            "'role': 'admin' field to the JSON body of an otherwise normal profile-update request and "
            "successfully elevates their own account to administrator. Which vulnerability class does this "
            "represent, and what is the BEST remediation?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Mass assignment; the API should use an explicit server-side allow-list of fields a client "
                    "is permitted to modify, ignoring or rejecting any other submitted field."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Mass assignment (over-posting) occurs when an application blindly binds an "
                    "entire client-supplied object to a data model. Restricting writes to an explicit "
                    "server-defined allow-list of editable fields closes the gap regardless of what the "
                    "client includes in the request body."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Insecure direct object reference (IDOR); the API should validate that the requested "
                    "record ID belongs to the authenticated user."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. IDOR involves accessing another user's object by manipulating an identifier "
                    "(e.g., someone else's record ID). Here the user is modifying their own record, but "
                    "smuggling in an unauthorized field — that is a data-binding flaw, not an object-reference "
                    "flaw."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Cross-site request forgery (CSRF); the API should require a unique anti-CSRF token on "
                    "every state-changing request."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. CSRF tricks a victim's browser into submitting an unwanted request on their "
                    "behalf using their existing session. Here the tester intentionally crafted and sent the "
                    "request themselves; no forged cross-site request is involved."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Broken object-level authorization at the transport layer; the API should enforce TLS "
                    "client certificate authentication."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. TLS client certificates authenticate the connection, not which application "
                    "fields a request is allowed to modify. The flaw exists in the application's data-binding "
                    "logic, not in transport-layer authentication."
                ),
            },
        ],
        "explanation": (
            "Blindly binding an entire client-supplied JSON payload to an internal data model without an "
            "explicit field allow-list is a mass assignment vulnerability, letting an attacker set fields "
            "(like a privilege/role field) that were never intended to be client-writable."
        ),
    },
    {
        "id": "nd4h-004",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Application security",
        "stem": (
            "An invoice-processing service accepts uploaded XML invoice files and parses them with an XML "
            "library that has external entity resolution enabled by default. A researcher submits an invoice "
            "containing a DOCTYPE declaration that defines an external entity referencing 'file:///etc/passwd,' "
            "and the parsed response echoes back the contents of that file. Which finding and remediation are "
            "MOST appropriate?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "XML external entity (XXE) injection; disable DTD processing and external entity "
                    "resolution in the XML parser's configuration."
                ),
                "correct": True,
                "rationale": (
                    "Correct. This is a textbook XXE vulnerability: a maliciously crafted DOCTYPE/entity "
                    "definition causes the parser to resolve an external resource. Disabling DTD processing "
                    "and external entity resolution at the parser level is the standard, effective fix."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Server-side request forgery (SSRF); block outbound requests from the application server "
                    "to internal IP ranges."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. SSRF involves the server making an unintended outbound network request on the "
                    "attacker's behalf. This attack instead abuses the XML parser's entity-resolution feature "
                    "to read a local file, which is the specific XXE pattern rather than a network-request "
                    "forgery."
                ),
            },
            {
                "id": "c",
                "text": (
                    "SQL injection; convert all database queries to parameterized statements."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. No database query is involved in this exploit — the payload targets XML "
                    "parsing behavior, not SQL syntax. Parameterized queries would not affect XML entity "
                    "resolution at all."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Insecure deserialization; replace the XML parser with a binary serialization format."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Insecure deserialization involves reconstructing objects from untrusted "
                    "serialized data in a way that triggers code execution or logic abuse. Here the exploit "
                    "reads a file via entity resolution, which is XXE, not object deserialization."
                ),
            },
        ],
        "explanation": (
            "XXE occurs when an XML parser resolves externally defined entities in untrusted input. "
            "Disabling DTD/external entity processing (or switching to a parser configuration that rejects "
            "them by default) is the correct, standard mitigation."
        ),
    },
    {
        "id": "nd4h-005",
        "domain": 4,
        "objective": "4.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Asset management",
        "stem": (
            "An expense-report audit reveals that several business units have been paying for SaaS project-"
            "management and file-sharing subscriptions directly with corporate credit cards for over a year, "
            "entirely outside the procurement process, and none of these applications appear in the IT asset "
            "inventory or have undergone a security review. Which asset management practice would MOST "
            "effectively prevent this gap going forward?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Deploy a cloud access security broker (CASB) or SaaS-discovery tool integrated with "
                    "procurement/finance data to continuously identify and register unsanctioned SaaS usage."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Ongoing discovery that cross-references actual network/API usage with expense "
                    "and procurement data is specifically designed to surface shadow-IT SaaS subscriptions "
                    "that bypass formal onboarding, closing exactly this kind of inventory gap."
                ),
            },
            {
                "id": "b",
                "text": "Increase the frequency of the annual physical hardware inventory audit.",
                "correct": False,
                "rationale": (
                    "Incorrect. A physical hardware audit counts devices, not cloud SaaS subscriptions "
                    "purchased with a credit card. It would not detect this specific gap regardless of how "
                    "often it is performed."
                ),
            },
            {
                "id": "c",
                "text": "Require all new laptops to be enrolled in the CMDB before being issued to employees.",
                "correct": False,
                "rationale": (
                    "Incorrect. Laptop CMDB enrollment addresses endpoint hardware tracking, not unsanctioned "
                    "SaaS subscriptions purchased independently of any device provisioning workflow."
                ),
            },
            {
                "id": "d",
                "text": "Mandate that all software licenses be renewed annually instead of on a rolling basis.",
                "correct": False,
                "rationale": (
                    "Incorrect. Changing the renewal cadence does nothing to surface subscriptions that were "
                    "never recorded in the asset inventory in the first place; the core problem is a lack of "
                    "visibility, not a licensing schedule issue."
                ),
            },
        ],
        "explanation": (
            "Shadow IT SaaS purchased outside procurement is a classic asset management blind spot. A "
            "CASB or SaaS-discovery capability that reconciles actual usage/billing data against the sanctioned "
            "inventory is the practice that directly closes this gap."
        ),
    },
    {
        "id": "nd4h-006",
        "domain": 4,
        "objective": "4.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Asset management",
        "stem": (
            "A cloud cost-optimization review finds dozens of virtual machines and storage buckets still "
            "running months after the projects that created them ended. None appear in the CMDB, none have an "
            "assigned business owner, and several are running operating systems with known unpatched critical "
            "vulnerabilities. Which practice, if enforced throughout the resource's life, would have MOST "
            "effectively prevented this exposure?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A defined asset lifecycle process that requires every cloud resource to have an assigned "
                    "owner and an automatic decommissioning trigger when its associated project closes."
                ),
                "correct": True,
                "rationale": (
                    "Correct. A full lifecycle process — from provisioning with an assigned owner through to "
                    "automatic decommissioning tied to project closure — ensures orphaned resources are "
                    "identified and removed rather than left running unmonitored and unpatched."
                ),
            },
            {
                "id": "b",
                "text": "Encrypting all cloud storage buckets at rest using provider-managed keys.",
                "correct": False,
                "rationale": (
                    "Incorrect. Encryption at rest protects data confidentiality but does nothing to identify "
                    "orphaned resources, assign ownership, or ensure timely decommissioning of unused systems."
                ),
            },
            {
                "id": "c",
                "text": "Requiring multifactor authentication for all cloud console administrator logins.",
                "correct": False,
                "rationale": (
                    "Incorrect. MFA strengthens authentication to the console but has no bearing on whether "
                    "unused resources are tracked, owned, or decommissioned after their project ends."
                ),
            },
            {
                "id": "d",
                "text": "Increasing the retention period for cloud provider billing and usage logs.",
                "correct": False,
                "rationale": (
                    "Incorrect. Longer log retention could help investigate the resources after the fact, but "
                    "it is a detective/forensic measure, not a preventive lifecycle control that stops the "
                    "resources from becoming orphaned and unpatched in the first place."
                ),
            },
        ],
        "explanation": (
            "Cloud resource sprawl is prevented by tying provisioning to a mandatory owner assignment and "
            "linking decommissioning to a defined trigger (such as project closure), rather than relying on "
            "periodic manual cleanup."
        ),
    },
    {
        "id": "nd4h-007",
        "domain": 4,
        "objective": "4.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Automation & orchestration",
        "stem": (
            "A SOAR playbook automatically enriches every incoming alert by querying a free public WHOIS/"
            "geolocation API that allows only 100 lookups per day. During a high-volume phishing campaign, the "
            "enrichment step begins timing out after the daily limit is reached, and because the playbook "
            "waits for enrichment to complete before proceeding, time-critical containment actions further "
            "down the same playbook are delayed for hours. What is the BEST way to fix this design flaw?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Replace the free API with a dedicated, adequately rate-limited threat-intelligence source, "
                    "and redesign the playbook so time-critical containment steps do not block on enrichment "
                    "completing."
                ),
                "correct": True,
                "rationale": (
                    "Correct. The root causes are an under-provisioned data source and a sequencing flaw that "
                    "makes urgent containment wait on a non-critical enrichment call. Fixing the data source's "
                    "capacity and decoupling containment from enrichment addresses both directly."
                ),
            },
            {
                "id": "b",
                "text": "Disable enrichment entirely so the playbook only performs containment actions.",
                "correct": False,
                "rationale": (
                    "Incorrect. Removing enrichment sacrifices valuable context analysts rely on for triage "
                    "and closure decisions; it treats a design/sequencing flaw by discarding a useful "
                    "capability rather than fixing the underlying bottleneck."
                ),
            },
            {
                "id": "c",
                "text": "Increase the playbook's overall execution timeout so enrichment has more time to complete.",
                "correct": False,
                "rationale": (
                    "Incorrect. A longer timeout does not solve a hard daily rate limit being exhausted; "
                    "lookups will still fail once the quota is hit, and containment will still be delayed "
                    "behind a blocked enrichment step."
                ),
            },
            {
                "id": "d",
                "text": "Schedule the playbook to run only once per hour instead of in real time.",
                "correct": False,
                "rationale": (
                    "Incorrect. Reducing execution frequency would further delay time-critical containment "
                    "actions during an active phishing campaign, worsening the exact problem being solved "
                    "rather than fixing it."
                ),
            },
        ],
        "explanation": (
            "The playbook has both a capacity problem (an inadequate free API) and a sequencing problem "
            "(blocking urgent containment on non-critical enrichment). Both must be addressed: upgrade the "
            "data source and decouple the workflow so containment isn't gated on enrichment."
        ),
    },
    {
        "id": "nd4h-008",
        "domain": 4,
        "objective": "4.7",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Automation & orchestration",
        "stem": (
            "A SOC is defining governance rules for where SOAR playbooks require a mandatory human-approval "
            "step versus where they may run fully automated. Select TWO statements that reflect sound "
            "automation governance practice."
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "High-impact, difficult-to-reverse actions — such as disabling every account in a domain "
                    "or deleting production data — should require an analyst approval gate before execution."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Actions with severe or irreversible business impact warrant a human checkpoint "
                    "so a logic error, bad match, or unexpected edge case cannot cause organization-wide "
                    "damage before anyone reviews it."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Low-risk, easily reversible actions — such as opening a ticket or enriching an alert with "
                    "threat-intelligence data — are good candidates for full automation without approval."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Actions with minimal blast radius and easy rollback provide the speed and "
                    "consistency benefits of automation without meaningfully increasing risk, so requiring "
                    "human approval for them mainly adds delay without added safety."
                ),
            },
            {
                "id": "c",
                "text": "Every SOAR action should run fully automated with no approval gates, to maximize response speed.",
                "correct": False,
                "rationale": (
                    "Incorrect. Applying no approval gates to high-impact, irreversible actions removes the "
                    "safety net that catches logic errors or false positives before they cause widespread "
                    "damage, as seen in real domain-wide lockout incidents."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Adding a human-in-the-loop approval gate eliminates the need to test a playbook in a "
                    "staging environment before promoting it to production."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. An approval gate and pre-production testing address different risks — testing "
                    "catches logic flaws before deployment, while approval gates catch bad outcomes at "
                    "execution time. One does not substitute for the other."
                ),
            },
        ],
        "explanation": (
            "Sound SOAR governance scales the level of human oversight to the impact and reversibility of the "
            "action: low-risk, reversible steps can run fully automated, while high-impact, hard-to-reverse "
            "actions need an approval checkpoint — and neither replaces pre-production testing."
        ),
    },
    {
        "id": "nd4h-009",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Digital forensics",
        "stem": (
            "An investigation requires acquiring evidence from an employee's cloud-hosted email mailbox "
            "(SaaS) rather than a physical device. There is no local hardware to seize or image, and the "
            "underlying storage is entirely managed by the SaaS provider. Which approach provides the "
            "forensically soundest acquisition?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Use the provider's native eDiscovery/administrative export capability to export the "
                    "mailbox content, then immediately compute and record a cryptographic hash of the exported "
                    "data."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Since there is no physical media to write-block, the forensically sound approach "
                    "is to use the platform's official export/eDiscovery mechanism and hash the result "
                    "immediately upon export, establishing an integrity baseline the same way a disk hash "
                    "would for physical media."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Have the employee forward all relevant emails from their own account to the investigator's "
                    "mailbox."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Manual forwarding by the subject of the investigation risks selective omission "
                    "or tampering and strips forensic metadata, undermining both completeness and integrity of "
                    "the evidence."
                ),
            },
            {
                "id": "c",
                "text": "Attach a physical write-blocker to the mail server before beginning acquisition.",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no physical device to attach a hardware write-blocker to — the "
                    "storage is entirely managed by the SaaS provider and inaccessible at the hardware level."
                ),
            },
            {
                "id": "d",
                "text": "Take screenshots of each relevant email as they appear in the webmail interface.",
                "correct": False,
                "rationale": (
                    "Incorrect. Screenshots capture only a visual representation and omit headers, metadata, "
                    "and full message integrity information needed for a defensible forensic acquisition."
                ),
            },
        ],
        "explanation": (
            "For SaaS-hosted evidence with no physical media, the forensically sound method is to use the "
            "provider's official export/eDiscovery API and hash the exported data immediately to establish "
            "integrity, since traditional hardware write-blocking is not possible."
        ),
    },
    {
        "id": "nd4h-010",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Digital forensics",
        "stem": (
            "A forensic analyst must acquire an image of a live production file server that uses a hardware "
            "RAID-5 array across four physical disks. Imaging each disk individually and later attempting to "
            "reconstruct the array manually risks corrupting the logical volume if the original stripe order "
            "and parity configuration are not reproduced exactly. Which approach is MOST appropriate?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Acquire the image at the logical volume level, through the RAID controller (or via the "
                    "operating system), so the reconstructed data stream reflects the already-assembled array."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Imaging through the RAID controller or OS captures the logical volume as the "
                    "array actually presents it, avoiding the need to manually replicate the exact striping "
                    "and parity layout that individual physical-disk images would require."
                ),
            },
            {
                "id": "b",
                "text": "Image each of the four physical disks separately and concatenate the image files in disk order.",
                "correct": False,
                "rationale": (
                    "Incorrect. Simple concatenation does not account for RAID striping and parity "
                    "calculations; this would very likely produce a corrupted, unreadable reconstruction of "
                    "the original data."
                ),
            },
            {
                "id": "c",
                "text": "Remove one disk from the array to image it, since RAID-5 tolerates a single disk failure.",
                "correct": False,
                "rationale": (
                    "Incorrect. Pulling a disk degrades a live production array and does not solve the "
                    "reconstruction problem — the remaining physical disks still cannot simply be concatenated "
                    "into a usable image without controller-aware processing."
                ),
            },
            {
                "id": "d",
                "text": "Power off the server and image only the disk containing the boot partition.",
                "correct": False,
                "rationale": (
                    "Incorrect. In a striped RAID-5 array, data is distributed across all disks; imaging only "
                    "one disk (boot or otherwise) would omit the majority of the file server's data and yield "
                    "an incomplete, unusable acquisition."
                ),
            },
        ],
        "explanation": (
            "RAID arrays should be imaged at the logical volume level (through the controller or OS) rather "
            "than as separate physical disks, since the striping and parity math needed to reconstruct the "
            "array is otherwise extremely error-prone to replicate manually."
        ),
    },
    {
        "id": "nd4h-011",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Digital forensics and chain-of-custody process",
        "stem": (
            "An evidence room uses RFID-tagged evidence bags that automatically log a timestamped entry "
            "— including reader location and the badge ID of whoever is carrying the tag — every time a bag "
            "passes through a doorway reader, with no manual paperwork involved. During pretrial review, "
            "defense counsel questions whether this system satisfies chain-of-custody requirements. Which "
            "response is MOST accurate?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Yes, provided the system reliably captures who, what, when, and where for every transfer "
                    "and the resulting audit log is protected from unauthorized modification."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Chain of custody requires a complete, tamper-resistant record of every transfer "
                    "— who handled the evidence, what it was, when, and where. An automated RFID logging "
                    "system that captures all four elements and is itself protected from tampering satisfies "
                    "this requirement just as manual logs do."
                ),
            },
            {
                "id": "b",
                "text": (
                    "No, because chain of custody legally requires a handwritten signature at every transfer "
                    "point and cannot be satisfied by an automated system."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Chain of custody is defined by the completeness and integrity of the record, "
                    "not by the specific medium (handwritten versus automated) used to capture it. Automated, "
                    "tamper-resistant logging is an accepted method."
                ),
            },
            {
                "id": "c",
                "text": "No, because RFID readers cannot record the exact time of each transfer.",
                "correct": False,
                "rationale": (
                    "Incorrect. RFID reader logs are inherently timestamped events; the described system "
                    "explicitly captures a timestamp at each read, so this concern does not apply here."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Yes, automatically and unconditionally, because any electronic logging system is "
                    "presumed legally sufficient regardless of its integrity controls."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Sufficiency is not automatic or unconditional — it depends on the system "
                    "actually capturing complete transfer details and being protected against tampering, not "
                    "merely on the fact that it is electronic."
                ),
            },
        ],
        "explanation": (
            "A properly designed automated tracking system that reliably captures who/what/when/where for "
            "every custody transfer, and resists tampering, satisfies chain-of-custody requirements just as "
            "well as a manual paper log."
        ),
    },
    {
        "id": "nd4h-012",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Digital forensics and chain-of-custody process",
        "stem": (
            "A seized laptop involved in an internal HR fraud investigation must be handed off to outside "
            "legal counsel for review under strict need-to-know restrictions. Select TWO practices that BEST "
            "preserve a defensible chain of custody during this handoff."
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Seal the device in a tamper-evident bag with a unique serial number, and record that "
                    "serial number along with the date, time, and names/signatures of the releasing and "
                    "receiving parties on the custody form."
                ),
                "correct": True,
                "rationale": (
                    "Correct. A uniquely numbered tamper-evident seal combined with a documented, signed "
                    "transfer record creates verifiable proof of both physical integrity and an unbroken "
                    "custody trail between the two parties."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Compute and record a cryptographic hash of the forensic image before the handoff, so the "
                    "recipient can independently verify the data was not altered upon receipt."
                ),
                "correct": True,
                "rationale": (
                    "Correct. A hash recorded before transfer lets any party later prove mathematically that "
                    "the data received is bit-for-bit identical to what was released, independent of physical "
                    "packaging integrity."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Rely solely on the courier company's private internal shipment log, since it is a "
                    "neutral third party."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A courier's internal log was not created or maintained by the investigation "
                    "team and typically does not capture forensic-specific details (evidence identifiers, "
                    "hashes, seal numbers); it cannot substitute for a proper chain-of-custody record."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Skip formal custody documentation for this transfer since it is an internal handoff "
                    "between trusted departments."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Chain of custody must be documented for every transfer regardless of internal "
                    "trust levels; skipping documentation creates an unexplained gap that opposing counsel can "
                    "use to challenge the evidence's integrity."
                ),
            },
        ],
        "explanation": (
            "Defensible custody transfers combine tamper-evident physical controls with signed documentation "
            "and independent cryptographic verification — not reliance on an outside party's unrelated "
            "records or an assumption of internal trust."
        ),
    },
    {
        "id": "nd4h-013",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "EDR/XDR & DLP",
        "stem": (
            "A construction firm's DLP solution inspects files and email attachments for content matching "
            "ITAR-controlled drawing markings and reliably blocks unauthorized transfers. During a video call "
            "with an external vendor, an employee instead shares their screen and displays the same restricted "
            "drawings live, allowing the vendor to view and photograph them; no file ever leaves the network "
            "and DLP generates no alert. Which statement BEST explains this outcome?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Content-based DLP has a blind spot for real-time screen-sharing/collaboration channels, "
                    "since no file or message body is transmitted for the DLP engine to inspect."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Traditional content-inspection DLP operates on files and message bodies passing "
                    "through monitored channels. A live screen share renders pixels to a video stream with no "
                    "matching text/file pattern for the DLP engine to scan, so the disclosure goes undetected."
                ),
            },
            {
                "id": "b",
                "text": "The DLP policy's regular expression pattern for ITAR markings must have been misconfigured.",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario confirms the same DLP policy reliably blocks the same content in "
                    "files and email; the pattern itself is functioning. The gap is the delivery channel, not "
                    "the pattern configuration."
                ),
            },
            {
                "id": "c",
                "text": "The vendor's device must have been exempted from DLP monitoring at the network layer.",
                "correct": False,
                "rationale": (
                    "Incorrect. Screen sharing does not depend on the remote party's device being covered by "
                    "DLP; the gap exists because DLP never inspects the rendered video stream on the sharing "
                    "employee's own endpoint in the first place."
                ),
            },
            {
                "id": "d",
                "text": "This indicates a false negative caused by the DLP engine's signature database being outdated.",
                "correct": False,
                "rationale": (
                    "Incorrect. This is not a stale-signature issue — DLP content inspection has no visibility "
                    "into screen-share video streams at all, regardless of how current its detection patterns "
                    "are."
                ),
            },
        ],
        "explanation": (
            "DLP tools built around inspecting files and text in transit have a structural blind spot for "
            "visual disclosure channels like screen sharing; closing this gap requires additional controls "
            "such as watermarking, session recording restrictions, or CASB-based collaboration monitoring."
        ),
    },
    {
        "id": "nd4h-014",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "EDR/XDR & DLP",
        "stem": (
            "After deploying a new EDR agent alongside an existing legacy antivirus product on the same "
            "endpoints, the SOC begins receiving hundreds of daily alerts because the EDR flags the antivirus "
            "engine's own on-access scanning process as suspicious file-system enumeration behavior. Both "
            "products are legitimate and required during the migration period. What is the BEST way to reduce "
            "these alerts without weakening overall detection?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Create a narrowly scoped EDR exclusion for the specific signed antivirus binary and its "
                    "installation path, rather than disabling the triggering detection rule broadly."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Scoping the exclusion to the exact signed binary and path eliminates the known "
                    "false-positive source while leaving the underlying detection rule fully active for every "
                    "other process, preserving coverage against genuine threats."
                ),
            },
            {
                "id": "b",
                "text": "Disable the EDR's file-system enumeration detection rule across all endpoints.",
                "correct": False,
                "rationale": (
                    "Incorrect. Disabling the rule entirely removes detection of that suspicious behavior "
                    "pattern fleet-wide, creating a much larger blind spot than the narrow conflict being "
                    "addressed."
                ),
            },
            {
                "id": "c",
                "text": "Uninstall the EDR agent until the antivirus migration is complete.",
                "correct": False,
                "rationale": (
                    "Incorrect. Removing EDR entirely eliminates its behavioral detection and response "
                    "capability across the whole environment, far exceeding the scope of the actual conflict "
                    "with a single legacy AV process."
                ),
            },
            {
                "id": "d",
                "text": "Instruct analysts to manually dismiss any alert involving the antivirus process name.",
                "correct": False,
                "rationale": (
                    "Incorrect. Manual dismissal by name is fragile and can be abused — an attacker could name "
                    "a malicious process identically to bypass triage — and it does not stop the alerts from "
                    "being generated in the first place."
                ),
            },
        ],
        "explanation": (
            "The correct fix for a known, legitimate cause of false positives is a tightly scoped exclusion "
            "(specific signed binary and path) rather than broadly weakening detection or removing a security "
            "tool."
        ),
    },
    {
        "id": "nd4h-015",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Email security (SPF/DKIM/DMARC)",
        "stem": (
            "An organization rotates its DKIM signing key pair as part of a routine security hardening cycle "
            "and immediately begins signing outbound mail with the new private key. Within minutes, DKIM "
            "validation begins failing for all outbound mail at receiving domains that check alignment. What "
            "is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The new public key was not published (or had not yet propagated) in the DNS TXT record "
                    "for the corresponding DKIM selector before mail signed with the new private key began "
                    "being sent."
                ),
                "correct": True,
                "rationale": (
                    "Correct. DKIM validation depends on receivers retrieving the matching public key from a "
                    "DNS TXT record at the selector referenced in the signature. If the new public key is not "
                    "yet published or has not propagated, every signature made with the new private key will "
                    "fail to validate."
                ),
            },
            {
                "id": "b",
                "text": "The organization's SPF record still lists the old mail server's IP address.",
                "correct": False,
                "rationale": (
                    "Incorrect. SPF validates the sending IP address independently of DKIM's cryptographic "
                    "signature validation. An SPF issue would not cause DKIM signature validation itself to "
                    "fail."
                ),
            },
            {
                "id": "c",
                "text": "DMARC alignment mode was changed from relaxed to strict at the same time as the key rotation.",
                "correct": False,
                "rationale": (
                    "Incorrect. Alignment mode governs whether the DKIM 'd=' domain must exactly match the "
                    "From domain; it does not affect whether the DKIM signature itself cryptographically "
                    "validates against the published key."
                ),
            },
            {
                "id": "d",
                "text": "The mail server's TLS certificate expired at the same time as the key rotation.",
                "correct": False,
                "rationale": (
                    "Incorrect. TLS certificates secure the transport connection between mail servers and are "
                    "unrelated to DKIM's independent public/private key signing mechanism published via DNS."
                ),
            },
        ],
        "explanation": (
            "DKIM key rotation must be sequenced so the new public key is published and propagated in DNS "
            "before mail is signed with the corresponding new private key; otherwise every new signature fails "
            "validation because receivers cannot find a matching public key."
        ),
    },
    {
        "id": "nd4h-016",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Email security (SPF/DKIM/DMARC)",
        "stem": (
            "A company's DMARC record for company.com is 'v=DMARC1; p=reject; sp=none; "
            "rua=mailto:dmarc@company.com'. An attacker registers 'billing.company.com' as a subdomain-style "
            "spoof and successfully sends messages that display as coming from that subdomain, which are "
            "delivered to inboxes without being rejected, even though the top-level domain enforces a strict "
            "policy. Which explanation is CORRECT?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The 'sp=none' tag sets a separate, weaker DMARC policy specifically for subdomains, so "
                    "spoofed mail claiming to be from a subdomain is not subject to the 'p=reject' enforcement "
                    "that protects the top-level domain."
                ),
                "correct": True,
                "rationale": (
                    "Correct. The 'sp' tag independently controls the policy applied to subdomains; when it is "
                    "set to 'none' while 'p' is 'reject,' the strict top-level enforcement does not extend to "
                    "subdomain-originated mail, leaving that path open to spoofing."
                ),
            },
            {
                "id": "b",
                "text": "DMARC records only apply to the exact domain in the 'rua' address, not to any subdomains at all.",
                "correct": False,
                "rationale": (
                    "Incorrect. The 'rua' tag is only the reporting destination address; it has no bearing on "
                    "which domains the policy covers. Subdomain coverage is governed specifically by the 'sp' "
                    "tag, not by 'rua'."
                ),
            },
            {
                "id": "c",
                "text": "'p=reject' only takes effect once the domain has published SPF and DKIM records for every subdomain individually.",
                "correct": False,
                "rationale": (
                    "Incorrect. DMARC enforcement does not require per-subdomain SPF/DKIM records to activate "
                    "'p=reject' for the top-level domain; the actual gap here is the explicit 'sp=none' "
                    "override for subdomains."
                ),
            },
            {
                "id": "d",
                "text": "DMARC cannot distinguish a subdomain from the top-level domain, so this behavior is unrelated to DMARC configuration.",
                "correct": False,
                "rationale": (
                    "Incorrect. DMARC explicitly supports a distinct subdomain policy via the 'sp' tag; the "
                    "protocol absolutely can and does distinguish subdomain mail from top-level domain mail."
                ),
            },
        ],
        "explanation": (
            "The DMARC 'sp' tag sets a policy specifically for subdomains, independent of the top-level 'p' "
            "tag. Leaving 'sp=none' while 'p=reject' creates a gap that lets spoofed subdomain mail bypass the "
            "organization's strict top-level enforcement."
        ),
    },
    {
        "id": "nd4h-017",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Federation & SSO (SAML/OAuth)",
        "stem": (
            "An organization federates dozens of SaaS applications to a cloud identity provider using SAML "
            "just-in-time (JIT) provisioning, which automatically creates an application account the first "
            "time a user signs in. When an employee is terminated and disabled in HR/the IdP, their accounts "
            "inside each individual SaaS application remain active and fully accessible via any session or API "
            "token issued before termination, because nothing ever explicitly removes them. Which capability "
            "is MISSING?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Automated lifecycle deprovisioning (e.g., via SCIM) that actively disables or removes the "
                    "downstream application account when the user is terminated in the identity source of "
                    "truth."
                ),
                "correct": True,
                "rationale": (
                    "Correct. JIT provisioning only creates accounts on first login; it has no built-in "
                    "mechanism to remove them. A standards-based provisioning protocol like SCIM, triggered by "
                    "the HR/IdP termination event, is required to actively deprovision the downstream account."
                ),
            },
            {
                "id": "b",
                "text": "Stronger SAML assertion signing using a longer RSA key length.",
                "correct": False,
                "rationale": (
                    "Incorrect. Signature strength protects assertion integrity during authentication; it has "
                    "no relationship to whether a downstream account is deprovisioned after termination."
                ),
            },
            {
                "id": "c",
                "text": "Shorter SAML assertion validity windows to reduce replay risk.",
                "correct": False,
                "rationale": (
                    "Incorrect. Assertion validity windows limit how long a single sign-in event's assertion "
                    "can be replayed; they do not affect whether an already-provisioned downstream account "
                    "remains active after termination."
                ),
            },
            {
                "id": "d",
                "text": "Enforcing multifactor authentication at every individual SaaS application separately.",
                "correct": False,
                "rationale": (
                    "Incorrect. Per-application MFA strengthens login verification but does nothing to remove "
                    "an account, session, or API token that was already established for a now-terminated user."
                ),
            },
        ],
        "explanation": (
            "JIT provisioning handles account creation but not removal. Automated deprovisioning, typically "
            "via SCIM triggered from the authoritative HR/identity source, is required so terminated employees "
            "lose downstream application access promptly."
        ),
    },
    {
        "id": "nd4h-018",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Federation & SSO (SAML/OAuth)",
        "stem": (
            "A smart-TV streaming app uses the OAuth 2.0 device authorization grant: the TV displays a short "
            "code and instructs the user to enter it at a URL on another device to complete sign-in. An "
            "attacker requests their own device code from the legitimate authorization server and sends it to "
            "victims in a phishing message claiming they must 'verify their account' by entering the code at "
            "the real, legitimate login page. Victims who comply unknowingly authorize the attacker's session. "
            "Which statement BEST describes this attack and mitigation?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "This is device-code phishing; mitigation includes short code expiration windows, "
                    "explicit warnings during approval about what is being authorized, and cross-device "
                    "signal checks (e.g., proximity or session context) before granting the token."
                ),
                "correct": True,
                "rationale": (
                    "Correct. The device authorization grant is designed for input-constrained devices, but "
                    "because the code is entered on a separate, trusted device, attackers can phish victims "
                    "into authorizing a session the attacker actually controls. Short-lived codes, clear "
                    "consent messaging, and cross-device correlation checks are the recognized mitigations."
                ),
            },
            {
                "id": "b",
                "text": "This is a SAML replay attack; mitigation is to shorten the SAML assertion's NotOnOrAfter window.",
                "correct": False,
                "rationale": (
                    "Incorrect. No SAML assertion is involved in this flow at all — this is entirely an OAuth "
                    "2.0 device authorization grant scenario, so SAML-specific mitigations do not apply."
                ),
            },
            {
                "id": "c",
                "text": "This is an open redirect vulnerability; mitigation is to validate the 'redirect_uri' against an allow-list.",
                "correct": False,
                "rationale": (
                    "Incorrect. The attacker never manipulates a redirect URI in this scenario; the victim is "
                    "tricked into entering a legitimate code on the real, correct login page, which is a "
                    "social-engineering abuse of the device-code flow itself, not a redirect flaw."
                ),
            },
            {
                "id": "d",
                "text": "This is CSRF against the token endpoint; mitigation is adding a unique anti-CSRF token to the request.",
                "correct": False,
                "rationale": (
                    "Incorrect. CSRF relies on a victim's browser silently submitting a forged request. Here "
                    "the victim knowingly and manually enters a code on a legitimate page, which is deceptive "
                    "social engineering targeting the device grant flow, not a forged browser request."
                ),
            },
        ],
        "explanation": (
            "Phishing a victim into entering an attacker-obtained device code on the real IdP page is a known "
            "OAuth device-code phishing pattern; defenses include short code lifetimes, clear consent-screen "
            "warnings, and additional cross-device verification signals."
        ),
    },
    {
        "id": "nd4h-019",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Hardening & secure baselines",
        "stem": (
            "A container security review finds that the organization's standard Docker base image runs the "
            "application process as the root user inside the container by default. A researcher demonstrates "
            "that a container-escape vulnerability in the runtime, combined with this root process, grants "
            "root-equivalent access on the underlying host. Which remediation BEST aligns with secure "
            "baseline hardening practice?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Rebuild the image to run the application as a dedicated, unprivileged user (e.g., via a "
                    "Dockerfile 'USER' directive), so the containerized process never has root privileges."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Running containers as a non-root user is a core least-privilege hardening "
                    "practice; it substantially reduces the impact of a container-escape vulnerability because "
                    "the escaping process would not carry root privileges onto the host."
                ),
            },
            {
                "id": "b",
                "text": "Increase the CPU and memory resource limits assigned to the container.",
                "correct": False,
                "rationale": (
                    "Incorrect. Resource limits govern performance and denial-of-service resistance; they have "
                    "no effect on the privilege level the containerized process runs with or the impact of a "
                    "container-escape exploit."
                ),
            },
            {
                "id": "c",
                "text": "Enable verbose application-level debug logging inside the container.",
                "correct": False,
                "rationale": (
                    "Incorrect. Debug logging aids troubleshooting and forensics after the fact but does "
                    "nothing to reduce the container process's privilege level or prevent host compromise via "
                    "a container escape."
                ),
            },
            {
                "id": "d",
                "text": "Change the container's restart policy to 'always' so it automatically recovers from crashes.",
                "correct": False,
                "rationale": (
                    "Incorrect. A restart policy affects availability after a crash; it does not reduce the "
                    "privilege level of the running process or mitigate the impact of a privilege-escalating "
                    "container escape."
                ),
            },
        ],
        "explanation": (
            "Running containers as root by default is a significant hardening gap; rebuilding images to run "
            "as an unprivileged user is the standard, effective mitigation that limits the blast radius of a "
            "container-escape exploit."
        ),
    },
    {
        "id": "nd4h-020",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Hardening & secure baselines",
        "stem": (
            "An organization's secure baseline disables USB mass-storage functionality on all endpoints by "
            "default. When a small subset of users in the shipping department legitimately need USB drives for "
            "label-printer transfers, an administrator grants a blanket exception that re-enables USB mass "
            "storage for the entire organization rather than only the shipping team, to save time. Which "
            "action BEST corrects this while still meeting the legitimate business need?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Scope the exception through a group policy or configuration profile applied only to the "
                    "specific security group containing shipping department accounts/devices, leaving the "
                    "baseline restriction enforced everywhere else."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Least-functionality hardening should grant exceptions only to the specific "
                    "population with a documented need, using a scoped group policy, rather than weakening the "
                    "baseline for every endpoint in the organization."
                ),
            },
            {
                "id": "b",
                "text": "Revoke the exception entirely and require the shipping department to stop using USB drives.",
                "correct": False,
                "rationale": (
                    "Incorrect. This ignores a legitimate, documented business need rather than solving the "
                    "actual problem, which is that the exception was scoped too broadly, not that it should "
                    "not exist at all."
                ),
            },
            {
                "id": "c",
                "text": "Leave the organization-wide exception in place but require quarterly password rotation on all accounts.",
                "correct": False,
                "rationale": (
                    "Incorrect. Password rotation frequency has no relationship to USB mass-storage exposure; "
                    "it does not narrow the scope of the overly broad hardening exception at all."
                ),
            },
            {
                "id": "d",
                "text": "Document the organization-wide exception in a risk register and take no further technical action.",
                "correct": False,
                "rationale": (
                    "Incorrect. Documenting an unnecessarily broad exception accepts avoidable risk instead of "
                    "eliminating it; a properly scoped technical fix is readily available and should be applied."
                ),
            },
        ],
        "explanation": (
            "Baseline exceptions should be scoped as narrowly as possible to the specific users or devices "
            "with a genuine need, preserving least-functionality hardening everywhere else, rather than "
            "applying a blanket exception organization-wide."
        ),
    },
    {
        "id": "nd4h-021",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Incident response process",
        "stem": (
            "During an active data-breach investigation, no official internal communications plan was defined "
            "in advance. As a result, several different teams post updates about affected systems and customer "
            "impact on a general company Slack channel visible to the entire workforce, revealing sensitive "
            "investigation details well before executive leadership is ready to make a public disclosure "
            "decision. Which incident response planning element was missing?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A defined communications plan specifying authorized spokespersons, approved channels, and "
                    "what information may be shared with which audiences during an active incident."
                ),
                "correct": True,
                "rationale": (
                    "Correct. A communications plan establishes who is authorized to share what information, "
                    "through which channel, and to whom. Its absence is exactly why sensitive details spread "
                    "uncontrolled to an unrestricted internal audience during the investigation."
                ),
            },
            {
                "id": "b",
                "text": "A digital forensics and evidence-handling procedure.",
                "correct": False,
                "rationale": (
                    "Incorrect. Evidence-handling procedures govern preserving and analyzing forensic evidence; "
                    "they have no bearing on who is authorized to post investigation updates in an internal "
                    "chat channel."
                ),
            },
            {
                "id": "c",
                "text": "A business impact analysis identifying recovery time objectives.",
                "correct": False,
                "rationale": (
                    "Incorrect. A BIA defines acceptable downtime and recovery priorities; it does not address "
                    "who may communicate incident details internally or externally during response."
                ),
            },
            {
                "id": "d",
                "text": "A vulnerability management policy defining patch SLAs.",
                "correct": False,
                "rationale": (
                    "Incorrect. Patch SLAs govern remediation timelines for known vulnerabilities and have no "
                    "connection to controlling internal communications during an active breach investigation."
                ),
            },
        ],
        "explanation": (
            "A well-run incident response plan includes a communications plan that restricts sensitive "
            "incident details to authorized channels and spokespersons until leadership approves broader "
            "disclosure — a gap this scenario directly illustrates."
        ),
    },
    {
        "id": "nd4h-022",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Incident response process",
        "stem": (
            "During eradication of malware from 40 affected point-of-sale terminals, the IR team determines "
            "that removing the malware from every terminal simultaneously would take the entire retail chain's "
            "checkout system offline during peak business hours, causing significant revenue loss. All "
            "terminals remain contained and isolated from further lateral spread in the meantime. What is the "
            "BEST approach?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Coordinate with business stakeholders to eradicate the malware in phased waves during "
                    "lower-impact windows, while maintaining containment on all affected terminals throughout."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Since containment already prevents further spread, a risk-based, "
                    "business-impact-aware phased eradication plan minimizes revenue disruption while still "
                    "progressing toward full remediation, coordinated with the stakeholders who own that "
                    "tradeoff."
                ),
            },
            {
                "id": "b",
                "text": "Immediately eradicate malware from all 40 terminals at once regardless of business impact.",
                "correct": False,
                "rationale": (
                    "Incorrect. Since containment already halts lateral spread, an all-at-once action that "
                    "takes down the entire checkout system unnecessarily maximizes business disruption without "
                    "a proportional security benefit."
                ),
            },
            {
                "id": "c",
                "text": "Delay eradication indefinitely until the terminals reach their scheduled end-of-life replacement.",
                "correct": False,
                "rationale": (
                    "Incorrect. Indefinitely delaying eradication leaves confirmed malware present on "
                    "production systems far longer than necessary and is not an appropriate resolution to a "
                    "confirmed incident."
                ),
            },
            {
                "id": "d",
                "text": "Skip eradication and proceed directly to closing the incident since containment is already in place.",
                "correct": False,
                "rationale": (
                    "Incorrect. Containment alone does not remove the malware; closing the incident without "
                    "eradication and recovery leaves an active compromise unresolved on production systems."
                ),
            },
        ],
        "explanation": (
            "When containment is already effective, eradication timing can be planned around business impact "
            "in coordination with stakeholders — but eradication must still occur; it should not be skipped or "
            "indefinitely postponed."
        ),
    },
    {
        "id": "nd4h-023",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log data sources",
        "stem": (
            "During a fileless malware investigation, an analyst suspects a legitimate Windows utility was "
            "abused to download and execute a payload. The default Windows Security event log records only "
            "that the process launched (Event ID 4688 without command-line auditing enabled) but not the full "
            "command-line arguments or the parent-child process relationship needed to confirm the abuse. "
            "Which log source should the analyst enable/prioritize going forward to capture this level of "
            "detail?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Sysmon (System Monitor) Event ID 1 process-creation logs, which include full command-line arguments and parent process information.",
                "correct": True,
                "rationale": (
                    "Correct. Sysmon Event ID 1 is specifically designed to capture rich process-creation "
                    "detail, including the complete command line and the parent process, which is exactly the "
                    "detail needed to confirm living-off-the-land style abuse of a legitimate utility."
                ),
            },
            {
                "id": "b",
                "text": "DHCP server lease logs.",
                "correct": False,
                "rationale": (
                    "Incorrect. DHCP lease logs record IP address assignments to devices; they contain no "
                    "process-execution or command-line information relevant to this investigation."
                ),
            },
            {
                "id": "c",
                "text": "Print spooler logs.",
                "correct": False,
                "rationale": (
                    "Incorrect. Print spooler logs record print job activity and are unrelated to process "
                    "execution or command-line arguments used in a fileless malware chain."
                ),
            },
            {
                "id": "d",
                "text": "NTP synchronization logs.",
                "correct": False,
                "rationale": (
                    "Incorrect. NTP logs record time-synchronization events and provide no information about "
                    "process creation, command-line arguments, or parent-child process relationships."
                ),
            },
        ],
        "explanation": (
            "Default Windows Security auditing often lacks full command-line detail. Sysmon Event ID 1 is the "
            "standard log source that captures complete command lines and parent-process context needed to "
            "investigate living-off-the-land technique abuse."
        ),
    },
    {
        "id": "nd4h-024",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log data sources",
        "stem": (
            "A confidential merger document is leaked in physical printed form and found outside the building. "
            "Building access logs confirm which employees badged into the finance floor that day, but "
            "investigators need to determine precisely which specific user account sent that exact file to a "
            "printer, and at what time. Which log source should the investigator prioritize?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Print server / print spooler logs, which record the user account, document name, and timestamp of each print job.",
                "correct": True,
                "rationale": (
                    "Correct. Print server logs capture exactly the detail needed here: which authenticated "
                    "user account submitted which named document to which printer and when, directly answering "
                    "the investigative question."
                ),
            },
            {
                "id": "b",
                "text": "Perimeter firewall session logs.",
                "correct": False,
                "rationale": (
                    "Incorrect. Firewall session logs record network connection metadata between hosts; they "
                    "contain no information about local print job activity or which user submitted a document "
                    "to a printer."
                ),
            },
            {
                "id": "c",
                "text": "DNS query logs.",
                "correct": False,
                "rationale": (
                    "Incorrect. DNS logs record domain name lookups and have no relationship to print job "
                    "submission, which is typically a local or internal network protocol action unrelated to "
                    "DNS resolution."
                ),
            },
            {
                "id": "d",
                "text": "Wireless access point association logs.",
                "correct": False,
                "rationale": (
                    "Incorrect. AP association logs show which devices connected to the wireless network, not "
                    "which user account or document was sent to a specific printer."
                ),
            },
        ],
        "explanation": (
            "Print spooler/print server logs are the log source that directly records the user account, "
            "document, printer, and timestamp for print activity — precisely what is needed to trace a leaked "
            "physical document back to its source."
        ),
    },
    {
        "id": "nd4h-025",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Malware classification",
        "stem": (
            "A hospital's file servers are found encrypted, and a ransom note demands payment for a decryption "
            "key. After the ransom is paid, the attacker's decryption tool fails to recover any files. Forensic "
            "analysis reveals that the malware generated a unique, random encryption key locally for each file "
            "and never transmitted any of those keys to the attacker's command-and-control infrastructure or "
            "stored them anywhere recoverable, making decryption mathematically impossible regardless of "
            "payment. Which classification BEST fits this malware?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A wiper disguised as ransomware, since the encryption is deliberately unrecoverable rather than reversible for a fee.",
                "correct": True,
                "rationale": (
                    "Correct. True ransomware retains a way to recover the key upon payment because the "
                    "attacker's business model depends on it. Malware that irreversibly destroys data behind a "
                    "fake ransom note — with no mechanism to ever recover the keys — is functionally a wiper "
                    "using ransomware as a decoy/cover story."
                ),
            },
            {
                "id": "b",
                "text": "A standard ransomware variant that simply had a bug preventing key escrow.",
                "correct": False,
                "rationale": (
                    "Incorrect. This mischaracterizes the design as accidental. The described behavior — "
                    "keys generated locally and never transmitted or stored anywhere — is a deliberate design "
                    "choice consistent with intentional, permanent destruction rather than a bug in a "
                    "legitimate ransomware payment/recovery process."
                ),
            },
            {
                "id": "c",
                "text": "A worm, because it spread automatically between the hospital's file servers.",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario describes the encryption/destruction behavior and lack of key "
                    "recoverability, not a self-propagation mechanism; worm classification depends on "
                    "autonomous spread, which is not described here."
                ),
            },
            {
                "id": "d",
                "text": "A logic bomb, because it activated based on a specific triggering condition.",
                "correct": False,
                "rationale": (
                    "Incorrect. A logic bomb is defined by lying dormant until a specific condition triggers "
                    "it (e.g., a date or an account status change). No such dormant trigger condition is "
                    "described here — the malware encrypted data upon execution."
                ),
            },
        ],
        "explanation": (
            "When encryption is deliberately designed to be permanently unrecoverable — no keys ever "
            "transmitted or escrowed — the malware functions as a wiper regardless of the ransom note "
            "presented to the victim, since payment can never actually restore the data."
        ),
    },
    {
        "id": "nd4h-026",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile device management",
        "stem": (
            "A company wants to protect corporate email and documents on employees' personal smartphones "
            "without enrolling the entire device in MDM, since most employees refuse full device enrollment "
            "over personal privacy concerns. Instead, IT deploys a solution that wraps only the corporate email "
            "and file apps in an encrypted, policy-controlled sandbox, leaving the rest of the personal device "
            "completely outside IT's control. Which approach is being used?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Mobile application management (MAM) using app-level containerization, rather than full-device MDM enrollment.",
                "correct": True,
                "rationale": (
                    "Correct. MAM applies policy controls and encryption at the individual application level, "
                    "wrapping only specific corporate apps in a managed container, without requiring control "
                    "over the entire device — exactly matching this scenario."
                ),
            },
            {
                "id": "b",
                "text": "Full device MDM enrollment with corporate-owned, personally enabled (COPE) provisioning.",
                "correct": False,
                "rationale": (
                    "Incorrect. COPE requires full device enrollment and centralized administrative control "
                    "over the whole device. The scenario explicitly states the device is not fully enrolled "
                    "and only specific apps are managed."
                ),
            },
            {
                "id": "c",
                "text": "Network access control (NAC) with 802.1X port-based authentication.",
                "correct": False,
                "rationale": (
                    "Incorrect. NAC/802.1X controls which devices may join a wired or wireless network segment; "
                    "it does not sandbox or apply policy to specific applications on a personal device."
                ),
            },
            {
                "id": "d",
                "text": "A virtual desktop infrastructure (VDI) session streamed to the mobile device.",
                "correct": False,
                "rationale": (
                    "Incorrect. VDI streams a remote desktop session to the device rather than wrapping native "
                    "local corporate apps in a managed container; the scenario describes locally installed, "
                    "policy-wrapped apps, not a streamed remote session."
                ),
            },
        ],
        "explanation": (
            "MAM with app-level containerization protects specific corporate applications and their data "
            "without requiring full-device MDM enrollment, making it well suited to BYOD scenarios where "
            "employees resist giving IT control over their entire personal device."
        ),
    },
    {
        "id": "nd4h-027",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile device management",
        "stem": (
            "A retail chain issues corporate-owned Android smartphones to delivery drivers. An employee "
            "attempts to bypass MDM restrictions by performing a factory reset, expecting this to permanently "
            "remove the device from management. Instead, upon setup after the reset, the device automatically "
            "re-enrolls into the corporate MDM and reapplies all restrictions before any personal use is "
            "possible. Which capability MOST directly explains this behavior?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A persistent 'Device Owner' enrollment profile (e.g., via Android Enterprise zero-touch/"
                    "device owner mode) that survives a factory reset and automatically re-establishes MDM "
                    "control."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Android Enterprise's Device Owner mode ties MDM enrollment to the device's "
                    "provisioning state in a way that survives a factory reset, so the device automatically "
                    "re-enrolls into MDM management during initial setup rather than remaining unmanaged."
                ),
            },
            {
                "id": "b",
                "text": "Remote wipe, which erases corporate data before the factory reset can complete.",
                "correct": False,
                "rationale": (
                    "Incorrect. Remote wipe removes corporate data on command but does not, by itself, cause "
                    "the device to automatically re-enroll into MDM after a user-initiated factory reset."
                ),
            },
            {
                "id": "c",
                "text": "Geofencing, which restricts application functionality based on the device's physical location.",
                "correct": False,
                "rationale": (
                    "Incorrect. Geofencing controls app behavior based on GPS location; it has no role in "
                    "causing a device to automatically re-enroll in MDM after a factory reset."
                ),
            },
            {
                "id": "d",
                "text": "Containerization, which isolates corporate app data from personal app data.",
                "correct": False,
                "rationale": (
                    "Incorrect. Containerization separates corporate and personal data within a managed device; "
                    "it does not persist through, or trigger automatic re-enrollment after, a factory reset."
                ),
            },
        ],
        "explanation": (
            "Android Enterprise's Device Owner provisioning mode binds MDM enrollment to the device at a level "
            "that survives a factory reset, automatically re-establishing management control and preventing an "
            "employee from permanently escaping corporate restrictions."
        ),
    },
    {
        "id": "nd4h-028",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Multifactor authentication",
        "stem": (
            "An organization requires FIDO2 hardware security keys for all privileged administrator accounts. "
            "During registration, an auditor discovers that any FIDO2-compliant authenticator can be enrolled, "
            "including inexpensive software-based authenticators running on a general-purpose laptop, "
            "undermining the intended requirement for dedicated, tamper-resistant hardware. Which control "
            "should be enabled during key registration to enforce hardware-only enrollment?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "FIDO2 attestation verification, checking the authenticator's attestation certificate "
                    "against an approved list of hardware security key manufacturers/models before allowing "
                    "enrollment."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Attestation lets the relying party cryptographically verify the make/model of "
                    "the authenticator during registration. Enforcing attestation against an approved hardware "
                    "manufacturer list is exactly the control needed to reject software-based authenticators."
                ),
            },
            {
                "id": "b",
                "text": "Reducing the TOTP code validity window from 60 seconds to 30 seconds.",
                "correct": False,
                "rationale": (
                    "Incorrect. TOTP code windows are unrelated to FIDO2 hardware key enrollment; this "
                    "scenario involves FIDO2 public-key authenticators, not time-based one-time passcodes."
                ),
            },
            {
                "id": "c",
                "text": "Requiring a longer minimum password length for the associated account.",
                "correct": False,
                "rationale": (
                    "Incorrect. Password length policy is unrelated to which type of FIDO2 authenticator "
                    "hardware may be registered; it does not distinguish hardware keys from software "
                    "authenticators."
                ),
            },
            {
                "id": "d",
                "text": "Enabling SMS-based backup codes for privileged accounts.",
                "correct": False,
                "rationale": (
                    "Incorrect. Adding an SMS-based fallback would actually weaken the hardware-key requirement "
                    "by introducing a less secure alternative factor, rather than enforcing hardware-only "
                    "FIDO2 enrollment."
                ),
            },
        ],
        "explanation": (
            "FIDO2 attestation allows verification of the specific authenticator hardware during registration. "
            "Enforcing attestation checks against an approved manufacturer/model list is the control that "
            "prevents software-based authenticators from being registered where hardware keys are required."
        ),
    },
    {
        "id": "nd4h-029",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Multifactor authentication",
        "stem": (
            "A bank uses an automated voice callback to a customer's pre-registered landline telephone number "
            "as a second authentication factor for high-value transactions. Investigators note that this "
            "method remained effective even against customers whose mobile phone numbers had been compromised "
            "via SIM-swapping, unlike SMS-based one-time passcodes sent to the same customers' mobile numbers. "
            "Which characteristic explains why the landline callback resisted the SIM-swap attack?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The callback is bound to a fixed physical line at a specific location that cannot be "
                    "ported or reassigned through a mobile carrier's SIM-swap process, unlike a mobile number."
                ),
                "correct": True,
                "rationale": (
                    "Correct. SIM swapping exploits the portability of mobile numbers between SIM cards through "
                    "the mobile carrier. A landline is tied to a fixed physical circuit and telephone company "
                    "process entirely separate from mobile SIM provisioning, so it is not affected by a mobile "
                    "carrier SIM swap."
                ),
            },
            {
                "id": "b",
                "text": "Voice callbacks use a stronger encryption algorithm than SMS messages.",
                "correct": False,
                "rationale": (
                    "Incorrect. The relevant weakness in SIM swapping is number portability/reassignment at the "
                    "carrier level, not the strength of any encryption algorithm used to transmit the OTP or "
                    "call audio."
                ),
            },
            {
                "id": "c",
                "text": "Landline calls are inherently a possession factor, while SMS OTPs are inherently a knowledge factor.",
                "correct": False,
                "rationale": (
                    "Incorrect. Both an SMS OTP delivered to a phone and a voice callback to a phone represent "
                    "'something you have' (possession of the device/line); the key distinguishing property here "
                    "is the line's non-portability, not a difference in factor category."
                ),
            },
            {
                "id": "d",
                "text": "Landline networks require MFA to be re-enrolled every 90 days, unlike mobile networks.",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no such 90-day re-enrollment requirement inherent to landline networks; "
                    "this option describes a fabricated operational detail rather than an actual technical "
                    "property relevant to SIM-swap resistance."
                ),
            },
        ],
        "explanation": (
            "SIM swapping exploits the ability to move a mobile phone number to an attacker-controlled SIM via "
            "the mobile carrier. A landline is not subject to that mobile-carrier porting process, so a "
            "callback to it remains resistant to SIM-swap-based interception even though both channels are "
            "technically possession factors."
        ),
    },
    {
        "id": "nd4h-030",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Penetration testing phases",
        "stem": (
            "During an authorized penetration test, a tester compromises a corporate jump host that has "
            "network access to an otherwise isolated OT (operational technology) network segment not "
            "reachable from the general corporate LAN. The tester configures SSH port forwarding through the "
            "jump host to reach and probe devices on the OT segment that would otherwise be unreachable. Which "
            "activity does this represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Lateral movement/pivoting during the post-exploitation phase.",
                "correct": True,
                "rationale": (
                    "Correct. Using a compromised host as a relay to reach network segments that were not "
                    "directly reachable before compromise is the definition of pivoting, a post-exploitation "
                    "activity used to expand access beyond the initial foothold."
                ),
            },
            {
                "id": "b",
                "text": "Passive reconnaissance.",
                "correct": False,
                "rationale": (
                    "Incorrect. Passive reconnaissance involves gathering information without directly "
                    "interacting with target systems (e.g., public records, OSINT). Actively probing devices "
                    "through a compromised host is direct interaction, not passive information gathering."
                ),
            },
            {
                "id": "c",
                "text": "Vulnerability scanning during the pre-engagement scoping phase.",
                "correct": False,
                "rationale": (
                    "Incorrect. Scoping happens before any technical testing begins and does not involve "
                    "actively pivoting through an already-compromised host; this activity occurs well after "
                    "initial exploitation."
                ),
            },
            {
                "id": "d",
                "text": "Reporting and remediation validation.",
                "correct": False,
                "rationale": (
                    "Incorrect. Reporting/validation activities occur after testing concludes and involve "
                    "documenting findings or re-testing fixes, not actively pivoting to reach new network "
                    "segments during the engagement."
                ),
            },
        ],
        "explanation": (
            "Pivoting — using a compromised system as a relay to reach network segments otherwise unreachable "
            "— is a core post-exploitation technique testers use to demonstrate the real-world impact of an "
            "initial foothold."
        ),
    },
    {
        "id": "nd4h-031",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Penetration testing phases",
        "stem": (
            "During an authorized external penetration test, a tester notices that an in-scope target IP "
            "address also hosts an unrelated, unlisted subsidiary web application on the same shared server. "
            "The signed rules of engagement authorize testing only against the specifically listed "
            "applications and does not mention this subsidiary application at all. What is the BEST action for "
            "the tester to take?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Stop short of testing the unlisted subsidiary application and request written scope "
                    "clarification or a formal authorization amendment from the client before proceeding "
                    "against it."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Testing anything not explicitly covered by the signed rules of engagement risks "
                    "unauthorized access to systems outside the client's consent, potential legal exposure, "
                    "and damage to an application the client never agreed to have tested. Written clarification "
                    "or a scope amendment must be obtained first."
                ),
            },
            {
                "id": "b",
                "text": "Proceed to test the subsidiary application, since it shares the same IP address as an authorized target.",
                "correct": False,
                "rationale": (
                    "Incorrect. Sharing an IP address does not extend authorization; testing an application not "
                    "explicitly listed in the rules of engagement without written consent exceeds the "
                    "authorized scope and could expose the tester and client to legal liability."
                ),
            },
            {
                "id": "c",
                "text": "Ignore the finding entirely and omit any mention of the subsidiary application from the final report.",
                "correct": False,
                "rationale": (
                    "Incorrect. Silently omitting a relevant observation deprives the client of useful "
                    "information about their environment; the appropriate action is to flag it and seek "
                    "authorization, not to hide the finding."
                ),
            },
            {
                "id": "d",
                "text": "Immediately terminate the entire engagement without notifying the client.",
                "correct": False,
                "rationale": (
                    "Incorrect. Discovering an out-of-scope application does not require halting the entire "
                    "authorized engagement; the proportionate response is to avoid testing that specific item "
                    "and seek clarification, while continuing authorized work."
                ),
            },
        ],
        "explanation": (
            "Testers must stay strictly within the boundaries of the signed rules of engagement. Discovering "
            "an unlisted, in-scope-adjacent system requires pausing on that specific item and obtaining "
            "explicit written authorization before testing it further."
        ),
    },
    {
        "id": "nd4h-032",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Port and protocol security",
        "stem": (
            "A vulnerability scan finds TCP port 1433 (Microsoft SQL Server) open and directly reachable from "
            "the internet on a production database server. The server has SQL Server authentication (mixed "
            "mode) enabled, and the built-in 'sa' account uses a weak, easily guessable password. Which "
            "remediation is MOST appropriate?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Remove direct internet exposure of port 1433 (placing the database behind the "
                    "application tier/firewall or requiring VPN access), disable or strongly secure the 'sa' "
                    "account, and prefer Windows/Active Directory authentication where possible."
                ),
                "correct": True,
                "rationale": (
                    "Correct. This addresses both root causes: the database should never be directly reachable "
                    "from the internet, and the weak built-in administrative account must be disabled or "
                    "hardened, with a stronger authentication method used going forward."
                ),
            },
            {
                "id": "b",
                "text": "Enable TLS encryption on the SQL Server connection while leaving port 1433 open to the internet.",
                "correct": False,
                "rationale": (
                    "Incorrect. TLS protects data in transit but does nothing to stop an attacker from directly "
                    "attempting to brute-force the exposed 'sa' account credentials over the still-internet-"
                    "reachable port; the exposure itself must be eliminated."
                ),
            },
            {
                "id": "c",
                "text": "Rename the 'sa' account's login while keeping mixed-mode authentication and internet exposure unchanged.",
                "correct": False,
                "rationale": (
                    "Incorrect. Renaming the account provides only minor obscurity and does not address the "
                    "core problems of a weak password and direct internet-facing exposure of the database port."
                ),
            },
            {
                "id": "d",
                "text": "Increase the database connection timeout value to slow down automated login attempts.",
                "correct": False,
                "rationale": (
                    "Incorrect. Adjusting connection timeouts does not meaningfully prevent brute-force "
                    "credential attacks or address the fundamental issue of an unnecessarily internet-exposed "
                    "database service with weak credentials."
                ),
            },
        ],
        "explanation": (
            "An internet-reachable database port combined with a weak built-in administrative account is a "
            "severe, commonly exploited misconfiguration. The fix requires eliminating the unnecessary internet "
            "exposure and hardening/disabling the weak account, not surface-level mitigations like renaming or "
            "timeouts."
        ),
    },
    {
        "id": "nd4h-033",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Privileged access management",
        "stem": (
            "A PAM solution allows administrators to launch an RDP session to a production server through a "
            "session broker that automatically injects the vaulted credential into the connection. The "
            "administrator never sees, types, or has access to the plaintext password at any point in the "
            "process. Which PAM capability does this describe, and why does it meaningfully reduce risk?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Credential injection through a session broker; because the plaintext credential is never "
                    "exposed to the human user, it cannot be captured by a keylogger, shoulder-surfed, or "
                    "casually memorized and reused elsewhere."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Credential injection lets the PAM system authenticate the session on the "
                    "administrator's behalf without ever revealing the secret to them, eliminating an entire "
                    "class of credential-exposure risks tied to humans handling plaintext passwords."
                ),
            },
            {
                "id": "b",
                "text": "Just-in-time provisioning; because it grants standing access only for a limited time window.",
                "correct": False,
                "rationale": (
                    "Incorrect. Just-in-time access governs how long elevated rights exist, not whether the "
                    "credential itself is ever exposed to the user. The scenario specifically describes the "
                    "credential being hidden during the session, not a time-limited grant."
                ),
            },
            {
                "id": "c",
                "text": "Multifactor authentication; because a second factor is required before the RDP session begins.",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario describes how the credential is delivered into an already-"
                    "initiated session, not an additional authentication factor being required beforehand."
                ),
            },
            {
                "id": "d",
                "text": "Privilege escalation detection; because the PAM tool alerts if the account attempts to gain higher rights.",
                "correct": False,
                "rationale": (
                    "Incorrect. Escalation detection is a monitoring capability for unauthorized privilege "
                    "gain; it is unrelated to the mechanism of hiding a vaulted credential from the user during "
                    "session establishment."
                ),
            },
        ],
        "explanation": (
            "Session broker credential injection authenticates a privileged session without ever revealing the "
            "plaintext secret to the human administrator, directly reducing risks like keylogging, shoulder "
            "surfing, and unauthorized credential reuse."
        ),
    },
    {
        "id": "nd4h-034",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Privileged access management",
        "stem": (
            "A security team is comparing just-in-time (JIT) privileged access, where elevated rights are "
            "granted only for the duration of an approved task, against standing (always-on) administrative "
            "access. Select TWO statements that are TRUE about JIT privileged access."
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "JIT access reduces the attack surface because elevated rights exist only for the approved "
                    "task's duration rather than being continuously available."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Because elevated privileges are granted only for a defined window tied to an "
                    "approved task, there is far less time during which a compromised account could be abused "
                    "for privileged actions, compared to standing access that is always available."
                ),
            },
            {
                "id": "b",
                "text": "JIT access typically requires an approval or request workflow integrated with the PAM vault before elevation is granted.",
                "correct": True,
                "rationale": (
                    "Correct. A defining characteristic of JIT privileged access is that elevation is "
                    "requested and, in most implementations, approved (manually or via policy) before the PAM "
                    "vault grants temporary elevated rights."
                ),
            },
            {
                "id": "c",
                "text": "Because access is temporary, JIT eliminates the need to log or record what actions were performed during the elevated session.",
                "correct": False,
                "rationale": (
                    "Incorrect. Session logging remains essential under JIT access; a short elevation window "
                    "does not remove the need for an audit trail of what privileged actions were actually "
                    "performed during that window."
                ),
            },
            {
                "id": "d",
                "text": "JIT access guarantees that credential theft cannot occur during the elevation window.",
                "correct": False,
                "rationale": (
                    "Incorrect. JIT access reduces the exposure window but does not eliminate risk; credential "
                    "theft or session hijacking can still occur while the temporary elevation is active."
                ),
            },
        ],
        "explanation": (
            "JIT privileged access reduces standing risk by limiting elevation to approved task windows via a "
            "request/approval workflow, but it still requires session logging and does not provide an absolute "
            "guarantee against compromise during that window."
        ),
    },
    {
        "id": "nd4h-035",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "A SIEM's user and entity behavior analytics (UEBA) module requires roughly 30 days of baseline "
            "activity data per user account before it can reliably flag deviations as anomalous. After UEBA is "
            "enabled organization-wide, the SOC is immediately flooded with high-confidence anomaly alerts for "
            "every employee hired in the past two weeks, since almost all of their early activity appears "
            "'unusual' against an empty baseline. What is the BEST way to address this?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Exclude newly created accounts from UEBA anomaly scoring until they accumulate a "
                    "sufficient baseline period, then enroll them in normal scoring once the learning period "
                    "completes."
                ),
                "correct": True,
                "rationale": (
                    "Correct. The root cause is that new accounts have no baseline for UEBA to compare against, "
                    "producing predictable false positives. Temporarily excluding them until a proper baseline "
                    "accumulates directly addresses the noise without disabling UEBA's value for established "
                    "accounts."
                ),
            },
            {
                "id": "b",
                "text": "Disable the UEBA module entirely across the whole organization.",
                "correct": False,
                "rationale": (
                    "Incorrect. Disabling UEBA entirely removes its detection value for all established "
                    "accounts with mature baselines, far exceeding the scope of the actual problem, which is "
                    "limited to newly created accounts."
                ),
            },
            {
                "id": "c",
                "text": "Increase every UEBA anomaly alert's severity so analysts prioritize them over other alert types.",
                "correct": False,
                "rationale": (
                    "Incorrect. Raising severity would make the false-positive flood from new accounts even "
                    "more disruptive to triage, worsening alert fatigue rather than addressing its actual "
                    "cause."
                ),
            },
            {
                "id": "d",
                "text": "Require every new employee to change their password weekly during onboarding.",
                "correct": False,
                "rationale": (
                    "Incorrect. Password rotation frequency has no bearing on UEBA's baseline-learning "
                    "mechanism and does nothing to reduce the volume of false anomaly alerts for new accounts."
                ),
            },
        ],
        "explanation": (
            "UEBA anomaly detection depends on an established behavioral baseline; new accounts predictably "
            "trigger false positives before that baseline exists. Temporarily excluding them from scoring "
            "during the learning period is the targeted fix."
        ),
    },
    {
        "id": "nd4h-036",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "A SOC wants to improve the signal-to-noise ratio of its SIEM without reducing genuine detection "
            "coverage. Select TWO practices that would BEST achieve this."
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Tune or suppress alerts for verified, consistently benign sources (such as an authorized "
                    "vulnerability scanner) while leaving the underlying correlation rule active for all other "
                    "sources."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Scoping suppression to a specific, verified source eliminates known noise while "
                    "preserving the rule's ability to detect the same behavior pattern from any unauthorized "
                    "source, maintaining coverage."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Implement risk-based alert scoring that factors in asset criticality alongside the "
                    "triggering event type, rather than treating all matching alerts as equal priority."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Weighting alerts by the criticality of the affected asset helps analysts "
                    "prioritize genuinely high-risk events first, reducing effective noise without disabling or "
                    "removing any detection logic."
                ),
            },
            {
                "id": "c",
                "text": "Disable any correlation rule entirely the first time it produces even one false positive from any source.",
                "correct": False,
                "rationale": (
                    "Incorrect. Fully disabling a rule after a single false positive discards detection "
                    "coverage for every legitimate source of that behavior, which reduces genuine coverage "
                    "rather than just noise."
                ),
            },
            {
                "id": "d",
                "text": "Ingest additional raw log sources without any corresponding correlation rule tuning, since more data always reduces alert volume.",
                "correct": False,
                "rationale": (
                    "Incorrect. Adding more raw log sources without tuning correlation logic typically "
                    "increases alert volume and noise, not reduces it; it is not a valid signal-to-noise "
                    "improvement technique on its own."
                ),
            },
        ],
        "explanation": (
            "Reducing SIEM noise while preserving coverage means scoping suppression precisely to verified "
            "benign sources and prioritizing by asset criticality — not blanket-disabling rules or blindly "
            "adding more unfiltered log volume."
        ),
    },
    {
        "id": "nd4h-037",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A vulnerability management program's automated scans are scheduled only during a nightly "
            "maintenance window when a specific critical, patch-pending application server is routinely "
            "powered off for backup jobs. As a result, that server has never actually been scanned and has "
            "shown as fully compliant on every report for months. Which improvement to the program would "
            "MOST directly prevent this kind of blind spot?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Validate scan coverage by cross-referencing the asset inventory against actual scan "
                    "results each cycle, flagging any expected asset that was not successfully scanned rather "
                    "than assuming a clean report means full coverage."
                ),
                "correct": True,
                "rationale": (
                    "Correct. The root problem is that a host being unreachable during the scan window was "
                    "silently interpreted as 'no findings' instead of 'not scanned.' Actively reconciling the "
                    "asset inventory against scan completion data surfaces coverage gaps like this directly."
                ),
            },
            {
                "id": "b",
                "text": "Increase the CVSS severity threshold that triggers an automatic remediation ticket.",
                "correct": False,
                "rationale": (
                    "Incorrect. Adjusting the severity threshold for ticket creation does not address the "
                    "underlying problem that the server was never actually scanned in the first place."
                ),
            },
            {
                "id": "c",
                "text": "Switch from credentialed to uncredentialed scanning for all servers.",
                "correct": False,
                "rationale": (
                    "Incorrect. Uncredentialed scans generally surface fewer findings than credentialed scans "
                    "and would not address the actual issue, which is that the host was completely unreachable "
                    "during every scheduled scan window."
                ),
            },
            {
                "id": "d",
                "text": "Reduce the frequency of vulnerability scans from monthly to quarterly to reduce scan overhead.",
                "correct": False,
                "rationale": (
                    "Incorrect. Reducing scan frequency does not solve a coverage-verification problem and "
                    "would only lengthen the amount of time an unscanned host remains undetected as such."
                ),
            },
        ],
        "explanation": (
            "A clean scan report is meaningless if the asset was never actually reachable during the scan. "
            "Programs must validate coverage — confirming every expected asset was actually scanned — rather "
            "than assuming absence of findings equals absence of exposure."
        ),
    },
    {
        "id": "nd4h-038",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A legacy application has a vulnerability with a CVSS base score of 7.2 that cannot be patched "
            "without breaking compatibility with a critical, unsupported integration. After executive "
            "leadership formally signs off, the finding is marked as risk-accepted with a documented "
            "compensating control (a WAF rule blocking the known exploit pattern) and a mandatory review date "
            "set six months out. Why is the review date an ESSENTIAL part of this process, rather than an "
            "optional formality?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Because the conditions justifying risk acceptance — including the compensating control's "
                    "continued effectiveness and the underlying business need — can change over time, so the "
                    "acceptance must be periodically reassessed rather than treated as permanent."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Risk acceptance is a point-in-time decision based on current conditions. A "
                    "compensating control could be bypassed by a new attack technique, the integration "
                    "dependency could disappear, or the threat landscape could shift — the review date forces "
                    "reassessment instead of letting an outdated risk decision stand indefinitely."
                ),
            },
            {
                "id": "b",
                "text": "Because CVSS base scores automatically increase over time regardless of any other factors.",
                "correct": False,
                "rationale": (
                    "Incorrect. CVSS base scores do not change automatically over time; the base metric group "
                    "reflects the vulnerability's intrinsic characteristics and stays fixed unless the scoring "
                    "itself is officially revised."
                ),
            },
            {
                "id": "c",
                "text": "Because a WAF rule automatically expires and must be manually re-created every six months.",
                "correct": False,
                "rationale": (
                    "Incorrect. WAF rules do not inherently expire on a fixed schedule; the review date exists "
                    "to reassess whether risk acceptance is still appropriate, not because of an automatic "
                    "technical expiration of the compensating control itself."
                ),
            },
            {
                "id": "d",
                "text": "Because regulatory frameworks universally mandate exactly a six-month review cycle for every risk acceptance.",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no universal regulatory mandate fixing every risk acceptance review at "
                    "exactly six months; the interval is a governance decision, and the underlying reason for "
                    "having a review at all is that conditions can change, not a specific mandated timeframe."
                ),
            },
        ],
        "explanation": (
            "Formal risk acceptance with a compensating control is not a permanent closure of a finding — it "
            "must be periodically revisited because the conditions that justified accepting the risk (business "
            "need, compensating control effectiveness, threat landscape) can and do change over time."
        ),
    },
    {
        "id": "nd4h-039",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Wireless security",
        "stem": (
            "During an authorized wireless assessment, a tester captures a single frame emitted by an access "
            "point during association — without needing a client to connect and without sending any "
            "deauthentication frames — that contains the PMKID value. The tester then cracks the WPA2-PSK "
            "passphrase offline using that captured PMKID. Which finding and mitigation are MOST appropriate?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "This is a PMKID-based offline attack against WPA2-PSK; migrating to WPA3-SAE, which does "
                    "not expose a crackable PMKID in this way, mitigates the underlying weakness."
                ),
                "correct": True,
                "rationale": (
                    "Correct. The PMKID attack allows an attacker to capture the necessary material for an "
                    "offline PSK-cracking attempt from a single frame, without waiting for or forcing a client "
                    "handshake. WPA3's SAE (Simultaneous Authentication of Equals) key exchange does not have "
                    "this exposure, making it the correct mitigation."
                ),
            },
            {
                "id": "b",
                "text": (
                    "This is a WPS PIN brute-force attack; disabling Wi-Fi Protected Setup mitigates the "
                    "weakness."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A WPS PIN brute-force attack requires repeated PIN-guessing attempts against "
                    "the WPS mechanism over time. The scenario describes capturing a single frame's PMKID and "
                    "cracking it offline, which is a distinct technique from WPS PIN brute forcing."
                ),
            },
            {
                "id": "c",
                "text": "This is a rogue access point (evil twin) attack; deploying a WIDS/WIPS mitigates the weakness.",
                "correct": False,
                "rationale": (
                    "Incorrect. No unauthorized access point is involved — the tester interacted with the "
                    "legitimate AP itself to capture the PMKID value, which is unrelated to a rogue/evil-twin "
                    "AP scenario."
                ),
            },
            {
                "id": "d",
                "text": (
                    "This is a deauthentication flood attack; enabling Protected Management Frames (802.11w) "
                    "mitigates the weakness."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario explicitly states no deauthentication frames were sent; the PMKID "
                    "technique specifically avoids needing a deauth-triggered handshake capture, so Protected "
                    "Management Frames do not address this particular exposure."
                ),
            },
        ],
        "explanation": (
            "The PMKID attack lets an attacker capture crackable material from a single AP-emitted frame "
            "without forcing a client handshake via deauthentication, enabling offline WPA2-PSK cracking. "
            "WPA3-SAE closes this specific exposure."
        ),
    },
    {
        "id": "nd4h-040",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Wireless security",
        "stem": (
            "An organization upgrades its office access points to Wi-Fi 6E, which adds support for the 6 GHz "
            "frequency band alongside the existing 2.4 GHz and 5 GHz bands. Months later, a rogue access point "
            "broadcasting the corporate SSID on the 6 GHz band goes completely undetected by the organization's "
            "wireless intrusion detection system (WIDS), even though several employees have connected to it. "
            "What is the MOST likely explanation?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The WIDS sensors were never upgraded to scan the 6 GHz band, leaving the organization "
                    "blind to rogue access points and other threats operating exclusively in that spectrum."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Legacy WIDS/WIPS sensors built before Wi-Fi 6E was common typically monitor only "
                    "2.4 GHz and 5 GHz. Without a corresponding sensor/hardware upgrade to also scan 6 GHz, "
                    "rogue activity in that new band is completely invisible to the detection system."
                ),
            },
            {
                "id": "b",
                "text": "The rogue access point must be using a stronger encryption algorithm than the legitimate APs.",
                "correct": False,
                "rationale": (
                    "Incorrect. Encryption strength on the rogue AP has no bearing on whether a WIDS sensor can "
                    "detect its RF presence; detection depends on whether the sensor is scanning the frequency "
                    "band the rogue AP is transmitting on, not on its encryption configuration."
                ),
            },
            {
                "id": "c",
                "text": "WIDS systems are architecturally incapable of detecting any rogue access point regardless of frequency band.",
                "correct": False,
                "rationale": (
                    "Incorrect. WIDS is specifically designed to detect rogue access points, and does so "
                    "successfully within the bands it monitors; the failure here is a coverage gap in a new "
                    "band, not a fundamental incapability of the technology."
                ),
            },
            {
                "id": "d",
                "text": "The employees who connected must have used a VPN, which prevented the WIDS from seeing the connection.",
                "correct": False,
                "rationale": (
                    "Incorrect. A VPN operates above the wireless association layer and encrypts traffic "
                    "content; it has no effect on whether a WIDS sensor can detect the RF presence of a rogue "
                    "access point broadcasting nearby."
                ),
            },
        ],
        "explanation": (
            "Introducing a new frequency band (6 GHz with Wi-Fi 6E) requires corresponding WIDS/WIPS sensor "
            "hardware capable of scanning that band; otherwise, rogue access points transmitting exclusively in "
            "the new band remain completely invisible to detection."
        ),
    },
]

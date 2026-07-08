"""CompTIA Security+ SY0-701 practice questions — Domain 4 (Security Operations), file E."""

QUESTIONS = [
    {
        "id": "nd4e-001",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Access control models",
        "stem": (
            "A Linux administrator finds that although standard file permissions (chmod) grant the 'apache' "
            "service account read access to /var/www/html/secret-config.php, the web server process still "
            "cannot read the file. Enabling SELinux audit logging reveals the read was denied because the "
            "file's security context (type) does not match the type allowed for the httpd_t process domain, "
            "even though no one modified the file's Unix permissions or ownership. Which access control model "
            "is SELinux enforcing in this scenario?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Mandatory access control (MAC)",
                "correct": True,
                "rationale": (
                    "Correct. SELinux enforces type-enforcement policy defined centrally by an administrator "
                    "using fixed security-context labels; access is denied regardless of the file's discretionary "
                    "(chmod) permissions, which is the defining trait of non-discretionary, label-based MAC."
                ),
            },
            {
                "id": "b",
                "text": "Discretionary access control (DAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. The standard chmod/owner permissions already grant access — that layer is DAC "
                    "and is satisfied. The denial comes from a separate, centrally defined policy the file owner "
                    "cannot override, which is exactly what DAC does not provide."
                ),
            },
            {
                "id": "c",
                "text": "Role-based access control (RBAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. No role assignment is described; the decision is based on matching a security "
                    "context label to an allowed type for the process domain, not on the requesting account's "
                    "assigned role."
                ),
            },
            {
                "id": "d",
                "text": "Attribute-based access control (ABAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. ABAC evaluates a policy engine combining multiple subject/object/environment "
                    "attributes at decision time. SELinux instead enforces fixed, administrator-defined labels "
                    "through static type-enforcement rules, which is the textbook MAC implementation, not a "
                    "dynamic attribute policy engine."
                ),
            },
        ],
        "explanation": (
            "SELinux is a canonical real-world implementation of mandatory access control: security contexts "
            "(labels) are assigned by policy, and the kernel enforces allowed type interactions independently of "
            "and in addition to standard DAC permissions. A DAC allow does not override a MAC deny."
        ),
    },
    {
        "id": "nd4e-002",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Access control models",
        "stem": (
            "A data center's server room electronic lock enforces a single global condition: entry is granted "
            "only Monday through Friday between 07:00 and 19:00. This one static condition is applied identically "
            "to every badge holder regardless of job role, clearance level, or department, and no other "
            "contextual factors (device, location, risk score) are evaluated. Which access control model does "
            "this door lock implement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Rule-based access control (RuBAC)",
                "correct": True,
                "rationale": (
                    "Correct. A single, static, identity-blind conditional statement (time window) applied "
                    "uniformly to every subject is the defining pattern of rule-based access control, commonly "
                    "seen in time-of-day restrictions and ACL-style conditions."
                ),
            },
            {
                "id": "b",
                "text": "Attribute-based access control (ABAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. ABAC would combine multiple subject, object, and environmental attributes in a "
                    "policy engine to reach different outcomes for different requesters. Here only one blanket "
                    "condition exists and it is evaluated identically for everyone, with no subject-specific "
                    "attribute matching at all."
                ),
            },
            {
                "id": "c",
                "text": "Role-based access control (RBAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. No roles are evaluated; the lock does not distinguish between job functions or "
                    "departments, so there is no role-to-permission mapping driving the decision."
                ),
            },
            {
                "id": "d",
                "text": "Mandatory access control (MAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. MAC requires classification labels and clearances compared against a central "
                    "authority's policy. No labels or clearance levels are described here — only a single "
                    "time-based rule."
                ),
            },
        ],
        "explanation": (
            "Rule-based access control applies static, predefined conditional logic (often IF/THEN statements "
            "such as time-of-day or source restrictions) uniformly, without regard to the requester's identity, "
            "role, or attributes — distinguishing it from ABAC's multi-attribute policy evaluation."
        ),
    },
    {
        "id": "nd4e-003",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Application security",
        "stem": (
            "A web application sets a session cookie without the Secure, HttpOnly, or SameSite attributes. An "
            "attacker successfully injects a reflected cross-site scripting (XSS) payload that executes "
            "attacker-controlled JavaScript in a victim's browser, and that script reads and exfiltrates the "
            "session cookie's value to an external server. Which single missing cookie attribute, if it had been "
            "set, would have BEST prevented client-side JavaScript from accessing the cookie during this specific "
            "attack?"
        ),
        "options": [
            {
                "id": "a",
                "text": "HttpOnly",
                "correct": True,
                "rationale": (
                    "Correct. The HttpOnly attribute prevents the cookie from being accessed via client-side "
                    "script (document.cookie), so even a successful XSS payload running in the browser could not "
                    "read or exfiltrate the session cookie's value."
                ),
            },
            {
                "id": "b",
                "text": "Secure",
                "correct": False,
                "rationale": (
                    "Incorrect. The Secure attribute only ensures the cookie is sent solely over HTTPS connections "
                    "and prevents plaintext network interception; it does nothing to stop JavaScript running "
                    "inside the same page from reading the cookie value."
                ),
            },
            {
                "id": "c",
                "text": "SameSite",
                "correct": False,
                "rationale": (
                    "Incorrect. SameSite restricts whether the cookie is sent with cross-site requests, which "
                    "mitigates CSRF-style attacks. It does not prevent script executing within the vulnerable "
                    "page's own origin (via XSS) from directly reading the cookie value."
                ),
            },
            {
                "id": "d",
                "text": "Domain",
                "correct": False,
                "rationale": (
                    "Incorrect. The Domain attribute controls which hosts/subdomains the cookie is sent to; it "
                    "has no bearing on whether JavaScript running on the same page can read the cookie's contents."
                ),
            },
        ],
        "explanation": (
            "Each cookie attribute defends against a distinct threat: HttpOnly blocks script-based access to the "
            "cookie value (the exact mechanism XSS-based session theft relies on), Secure blocks network "
            "interception, and SameSite blocks cross-site request forgery. Only HttpOnly addresses this scenario."
        ),
    },
    {
        "id": "nd4e-004",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Application security",
        "stem": (
            "A company builds an internal Windows utility and distributes it to employees for download from an "
            "internal file share. The security team wants to ensure the executable has not been tampered with "
            "after it was built and wants Windows SmartScreen and AppLocker publisher rules to trust the file "
            "automatically without generating warnings. Which control should the development team apply to the "
            "executable before release to BEST meet both goals?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Digitally sign the executable using a code-signing certificate issued to the organization",
                "correct": True,
                "rationale": (
                    "Correct. Code signing binds the file to a verifiable publisher identity and detects any "
                    "post-build tampering (an altered file breaks the signature), and it is precisely the "
                    "mechanism SmartScreen reputation and AppLocker publisher rules rely on to trust software "
                    "automatically."
                ),
            },
            {
                "id": "b",
                "text": "Publish a SHA-256 checksum of the file separately on the internal wiki for users to verify manually",
                "correct": False,
                "rationale": (
                    "Incorrect. A published hash lets a motivated user manually verify integrity, but it does not "
                    "establish publisher identity, does not automatically satisfy SmartScreen/AppLocker publisher "
                    "trust, and most users will never perform the manual comparison."
                ),
            },
            {
                "id": "c",
                "text": "Run a static application security testing (SAST) scan against the source code before compiling",
                "correct": False,
                "rationale": (
                    "Incorrect. SAST finds coding vulnerabilities in the source; it has no effect on establishing "
                    "distribution-time integrity or publisher trust for the compiled binary that end users "
                    "download."
                ),
            },
            {
                "id": "d",
                "text": "Deploy the utility inside a sandboxed execution environment on each endpoint",
                "correct": False,
                "rationale": (
                    "Incorrect. Sandboxing isolates a running program's effects on the host; it does not verify "
                    "that the distributed file is authentic and unmodified, nor does it satisfy SmartScreen or "
                    "AppLocker publisher-based trust decisions."
                ),
            },
        ],
        "explanation": (
            "Code signing is the specific application security control that simultaneously proves publisher "
            "identity and detects tampering after build, which is exactly what OS-level trust mechanisms such as "
            "SmartScreen and AppLocker publisher rules evaluate before granting frictionless execution trust."
        ),
    },
    {
        "id": "nd4e-005",
        "domain": 4,
        "objective": "4.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Asset management",
        "stem": (
            "A new-hire laptop provisioning workflow issues devices without recording a data classification level "
            "or business-criticality rating in the CMDB record. Six months later, the security team cannot "
            "determine which patch SLA, backup frequency, or encryption requirement should apply to hundreds of "
            "devices because that information was never captured. Which change to the asset management process "
            "would MOST directly prevent this gap going forward?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Make data classification and criticality mandatory fields captured at asset intake/"
                    "provisioning, before the device is released for use"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Capturing classification and criticality as required fields at the moment of "
                    "provisioning ensures every asset record has the data needed to drive downstream decisions "
                    "(patch SLA, backup, encryption) from day one, closing the exact gap described."
                ),
            },
            {
                "id": "b",
                "text": "Increase the frequency of automated network discovery scans to twice per week",
                "correct": False,
                "rationale": (
                    "Incorrect. Discovery scans can confirm a device exists and reveal its network footprint, but "
                    "they cannot infer a business-driven classification or criticality rating that only an owner "
                    "or intake process can assign."
                ),
            },
            {
                "id": "c",
                "text": "Add barcoded physical asset tags to every laptop at the time of issuance",
                "correct": False,
                "rationale": (
                    "Incorrect. Physical tagging supports tracking a device's physical location and custody; it "
                    "does not capture or communicate data classification or criticality, which are the fields "
                    "actually missing here."
                ),
            },
            {
                "id": "d",
                "text": "Require a quarterly manual physical inventory count of all issued laptops",
                "correct": False,
                "rationale": (
                    "Incorrect. A physical count reconciles quantity/existence after the fact; it would not "
                    "retroactively populate the classification or criticality fields that were never captured at "
                    "intake, and it does not prevent the gap from recurring for new devices."
                ),
            },
        ],
        "explanation": (
            "Asset management security value comes largely from the metadata captured, not just the inventory "
            "count. Mandatory classification/criticality capture at intake ensures every asset has the data "
            "needed to drive patch, backup, and control decisions, which discovery scans and tagging cannot supply."
        ),
    },
    {
        "id": "nd4e-006",
        "domain": 4,
        "objective": "4.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Asset management",
        "stem": (
            "A software asset management (SAM) review finds the organization has 500 active installations of a "
            "commercial application but owns only 350 purchased licenses, exposing the company to significant "
            "penalties during an upcoming vendor compliance audit. Which practice, if it had been integrated into "
            "the software deployment process, would MOST likely have prevented this from occurring in the first "
            "place?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "License entitlement reconciliation integrated with deployment tooling, so installations are "
                    "flagged or blocked once they exceed the organization's purchased entitlement count"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Continuously reconciling actual installation counts against purchased entitlements "
                    "at deployment time — rather than discovering the gap during an audit — is the specific SAM "
                    "control that prevents unlicensed installs from accumulating unnoticed."
                ),
            },
            {
                "id": "b",
                "text": "Maintaining a hardware asset inventory in the CMDB with serial numbers for every endpoint",
                "correct": False,
                "rationale": (
                    "Incorrect. A hardware inventory tracks physical devices, not software license counts or "
                    "entitlements; it would not have surfaced or prevented an over-deployment of a licensed "
                    "application."
                ),
            },
            {
                "id": "c",
                "text": "Running a monthly vulnerability scan against all endpoints running the application",
                "correct": False,
                "rationale": (
                    "Incorrect. Vulnerability scanning identifies security weaknesses, not license compliance "
                    "gaps; it has no mechanism for counting or comparing installations against purchased "
                    "entitlements."
                ),
            },
            {
                "id": "d",
                "text": "Applying physical asset tags to every workstation running the software",
                "correct": False,
                "rationale": (
                    "Incorrect. Physical tagging supports tracking device location and custody, not the count of "
                    "software installations relative to the number of licenses the organization has purchased."
                ),
            },
        ],
        "explanation": (
            "Software asset management is a distinct discipline from hardware inventory: it requires continuously "
            "reconciling deployed installation counts against purchased entitlements so over-deployment is caught "
            "and blocked proactively rather than discovered during a costly vendor audit."
        ),
    },
    {
        "id": "nd4e-007",
        "domain": 4,
        "objective": "4.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Automation & orchestration",
        "stem": (
            "A SOC implements a SOAR playbook that automatically disables a user account and revokes all active "
            "sessions the instant UEBA flags 'impossible travel' with high confidence. Months later, a legitimate "
            "traveling executive is auto-disabled mid-meeting while connecting through a VPN exit node in another "
            "country, causing a significant business disruption. Which enhancement BEST balances the speed benefit "
            "of automation with reducing this false-positive business impact?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Add a human-in-the-loop analyst approval step for high-business-impact accounts (e.g., "
                    "executives) or lower-confidence alerts before the disable action executes, while still "
                    "auto-executing on clearly high-confidence, standard-risk cases"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Inserting a targeted approval gate for the specific conditions most prone to costly "
                    "false positives preserves the speed of full automation for the majority of clear-cut cases "
                    "while preventing high-impact accounts from being disabled on an unconfirmed signal."
                ),
            },
            {
                "id": "b",
                "text": "Disable the impossible-travel automation entirely and handle all such alerts manually",
                "correct": False,
                "rationale": (
                    "Incorrect. Removing automation entirely sacrifices the speed benefit for the many legitimate "
                    "true-positive cases the rule correctly catches, over-correcting for a single false-positive "
                    "scenario."
                ),
            },
            {
                "id": "c",
                "text": "Broadly relax the impossible-travel detection sensitivity across all accounts",
                "correct": False,
                "rationale": (
                    "Incorrect. Loosening detection sensitivity organization-wide would reduce false positives at "
                    "the cost of missing genuine account-compromise indicators for every user, not just the "
                    "executive travel edge case."
                ),
            },
            {
                "id": "d",
                "text": "Remove UEBA from the detection pipeline and rely solely on static IOC matching",
                "correct": False,
                "rationale": (
                    "Incorrect. UEBA/impossible-travel analytics provide valuable behavioral detection that static "
                    "IOC matching cannot replicate; removing it entirely eliminates a detection capability rather "
                    "than fixing the automation's response logic."
                ),
            },
        ],
        "explanation": (
            "Mature SOAR design uses conditional branching so automation executes fully for clear, low-impact "
            "cases and inserts human approval specifically where confidence is lower or business impact is "
            "higher — this is more precise than disabling automation or globally loosening detection."
        ),
    },
    {
        "id": "nd4e-008",
        "domain": 4,
        "objective": "4.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Automation & orchestration",
        "stem": (
            "A newly deployed SOAR playbook is validated only in a lab environment before being promoted directly "
            "into production. On its first live day, a logic flaw causes the playbook to repeatedly re-trigger "
            "the same host-isolation action every time a duplicate copy of the same alert arrives from the SIEM, "
            "generating hundreds of redundant tickets and repeatedly paging the on-call engineer overnight even "
            "though the host was already isolated after the first execution. Which practice would have BEST "
            "prevented this specific failure mode?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Design the playbook to be idempotent — checking the host's current isolation state before "
                    "acting and skipping the action if it is already isolated — and test it against duplicate/"
                    "replayed alerts in staging before production promotion"
                ),
                "correct": True,
                "rationale": (
                    "Correct. The root cause is that the playbook re-executes a stateful action without first "
                    "checking whether it was already applied. An idempotent design that checks current state "
                    "before acting, validated against duplicate-alert conditions pre-production, directly "
                    "prevents this failure."
                ),
            },
            {
                "id": "b",
                "text": "Widen the SIEM's alert deduplication time window only",
                "correct": False,
                "rationale": (
                    "Incorrect. Deduplication tuning may reduce some duplicate alerts reaching the playbook, but "
                    "it does not fix the underlying flaw that the playbook itself has no state check and will "
                    "still misbehave on any duplicate or delayed alert that gets through."
                ),
            },
            {
                "id": "c",
                "text": "Require manual analyst approval before every future containment action, permanently",
                "correct": False,
                "rationale": (
                    "Incorrect. This eliminates the speed benefit of automation for all future cases, including "
                    "the large majority that would have worked correctly; it treats the symptom rather than "
                    "fixing the playbook's lack of idempotency."
                ),
            },
            {
                "id": "d",
                "text": "Mute overnight paging notifications so the on-call engineer is not repeatedly disturbed",
                "correct": False,
                "rationale": (
                    "Incorrect. Muting notifications only hides the symptom and creates a dangerous gap where "
                    "genuine overnight alerts — unrelated to the bug — would also go unnoticed."
                ),
            },
        ],
        "explanation": (
            "Automation reliability requires idempotent actions: a playbook step should verify current state "
            "before acting so replayed or duplicate triggers do not cause repeated, unnecessary, or disruptive "
            "actions. Staging tests against duplicate/replayed alert conditions catch this before production."
        ),
    },
    {
        "id": "nd4e-009",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Digital forensics",
        "stem": (
            "A first responder arrives at a compromised server that must remain powered on and network-connected "
            "to preserve evidence of an active intrusion. After capturing the full contents of system RAM, only "
            "enough time remains to collect ONE additional artifact before the server must be handed to the "
            "forensic lab for offline disk imaging. Following the standard order of volatility, which artifact "
            "should be collected NEXT?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The current state of active network connections, routing tables, and the ARP cache",
                "correct": True,
                "rationale": (
                    "Correct. In the standard order of volatility, network connection state, routing tables, and "
                    "the ARP cache rank immediately after CPU/registers and RAM — more volatile than disk "
                    "contents, temporary file systems, or archived logs, and lost quickly once the system is "
                    "powered down or network activity ages out."
                ),
            },
            {
                "id": "b",
                "text": "A full write-blocked forensic image of the disk",
                "correct": False,
                "rationale": (
                    "Incorrect. Disk contents are considerably less volatile than in-memory network state; disk "
                    "imaging is appropriately deferred to the forensic lab's offline process and is not the next "
                    "priority while the system remains live."
                ),
            },
            {
                "id": "c",
                "text": "Archived log backups from the previous month stored on tape",
                "correct": False,
                "rationale": (
                    "Incorrect. Archived backup media is among the least volatile evidence sources and will "
                    "persist unchanged whether collected now or later; it is not time-sensitive in the way live "
                    "network state is."
                ),
            },
            {
                "id": "d",
                "text": "Photographs of the physical server chassis and cabling",
                "correct": False,
                "rationale": (
                    "Incorrect. Physical documentation is useful but is not a volatile digital artifact governed "
                    "by order of volatility, and it does not compete for the responder's limited time in the same "
                    "way transient in-memory network state does."
                ),
            },
        ],
        "explanation": (
            "The order of volatility runs roughly: CPU registers/cache, RAM, network state (connections/routing/"
            "ARP), temporary file systems/swap, disk, remote logging/monitoring data, and finally archival media. "
            "With RAM already captured, network state is the next most time-sensitive artifact."
        ),
    },
    {
        "id": "nd4e-010",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Digital forensics",
        "stem": (
            "During active litigation, opposing counsel formally requests production of all emails between two "
            "named employees over the past two years. The legal team uses specialized software to search, filter, "
            "and export only the messages responsive to that request, while logging the exact search terms and "
            "methodology used to identify them for later defense of the process. Which forensic/legal activity "
            "does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "E-discovery",
                "correct": True,
                "rationale": (
                    "Correct. E-discovery is the process of identifying, searching, filtering, and producing "
                    "electronically stored information that is responsive to a legal request, with a defensible, "
                    "documented methodology — exactly what is described here."
                ),
            },
            {
                "id": "b",
                "text": "Legal hold",
                "correct": False,
                "rationale": (
                    "Incorrect. A legal hold is the preservation step that suspends normal deletion/retention "
                    "policies to prevent evidence from being destroyed. This scenario describes producing "
                    "responsive documents after the fact, a distinct downstream activity from preservation."
                ),
            },
            {
                "id": "c",
                "text": "Chain of custody",
                "correct": False,
                "rationale": (
                    "Incorrect. Chain of custody documents who possessed and handled physical or digital evidence "
                    "over time to prove it was not tampered with; it does not describe the process of searching "
                    "and producing responsive records."
                ),
            },
            {
                "id": "d",
                "text": "Order of volatility-based acquisition",
                "correct": False,
                "rationale": (
                    "Incorrect. Order of volatility governs the sequence for capturing live, perishable technical "
                    "artifacts during an active incident response, not the process of searching an existing "
                    "records archive to fulfill a legal production request."
                ),
            },
        ],
        "explanation": (
            "Legal hold preserves potentially relevant data before it can be deleted; e-discovery is the "
            "subsequent process of searching, filtering, and producing the specific records responsive to a "
            "legal request using a documented, defensible methodology."
        ),
    },
    {
        "id": "nd4e-011",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Digital forensics and chain-of-custody process",
        "stem": (
            "A first responder arrives at a suspect's home to seize a laptop as evidence. Which sequence of "
            "actions BEST preserves both the physical evidence and a defensible chain-of-custody record starting "
            "at the moment of seizure?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Photograph the device and its surroundings in place before touching it, then bag/tag/label "
                    "the device, and complete the initial chain-of-custody log entry (collector identity, date/"
                    "time, description) before transporting it"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Documenting the scene before disturbing it, then immediately creating the first "
                    "custody log entry at the point of seizure, establishes an unbroken, defensible record from "
                    "the earliest possible moment and avoids any unaccounted-for gap before documentation begins."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Power on the laptop briefly to confirm it is the correct device before bagging it for "
                    "transport"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Powering on a system alters volatile memory state, file access timestamps, and "
                    "potentially triggers anti-forensic or remote-wipe mechanisms; identity confirmation should "
                    "rely on external observation, not booting the device."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Begin the chain-of-custody log only once the device arrives at the forensic lab, to keep the "
                    "on-scene process fast"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Delaying documentation until arrival at the lab creates an undocumented gap "
                    "between seizure and lab intake during which the evidence's handling cannot be accounted for, "
                    "weakening its defensibility."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Allow the first available on-scene officer to transport the device without completing "
                    "documentation, to save time given the urgency of the investigation"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Skipping documentation to save time creates exactly the kind of undocumented "
                    "handoff that undermines chain-of-custody integrity, regardless of the investigation's "
                    "urgency."
                ),
            },
        ],
        "explanation": (
            "A defensible chain of custody starts at the moment of seizure: document the scene as found, avoid "
            "actions that alter the device's state, and record the first handling entry immediately rather than "
            "deferring documentation until later in the process."
        ),
    },
    {
        "id": "nd4e-012",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Digital forensics and chain-of-custody process",
        "stem": (
            "A fraud investigation involves seized backup tapes containing highly sensitive data that must "
            "periodically leave the locked evidence room for scheduled forensic analysis and then be returned. "
            "Select TWO practices that BEST strengthen the chain of custody for this repeated checkout/return "
            "cycle."
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Require two authorized personnel to jointly retrieve and return the evidence (two-person/"
                    "dual custody) and log both individuals' identities on the custody form for each cycle"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Dual custody ensures no single individual has unwitnessed, unaccountable access to "
                    "the evidence during any checkout cycle, directly strengthening the defensibility of repeated "
                    "handling."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Recompute and compare the cryptographic hash of the evidence against the originally recorded "
                    "value immediately before and after each checkout for analysis"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Verifying the hash at both ends of every checkout cycle proves the evidence was not "
                    "altered during that specific access window, providing continuous, cycle-by-cycle integrity "
                    "assurance rather than a single point-in-time check."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Allow a single trusted senior examiner to retrieve the evidence without a witness, since "
                    "seniority and trust reduce the need for dual-custody documentation"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Chain-of-custody integrity depends on documented, verifiable process, not on an "
                    "individual's seniority or perceived trustworthiness; skipping dual custody based on trust "
                    "reintroduces an unwitnessed access gap."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Record a hash of the evidence only once, at the very end of the entire investigation, to "
                    "minimize administrative overhead"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A single hash check at the end of the investigation cannot prove integrity was "
                    "maintained across each individual checkout cycle; if a discrepancy is later found, it would "
                    "be impossible to determine during which specific access the evidence was altered."
                ),
            },
        ],
        "explanation": (
            "Evidence that must be repeatedly accessed over time requires controls that provide assurance at "
            "every cycle, not just once: dual custody prevents unwitnessed access, and hash verification at each "
            "checkout/return proves integrity was preserved during that specific access window."
        ),
    },
    {
        "id": "nd4e-013",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "EDR/XDR & DLP",
        "stem": (
            "An employee exfiltrates a spreadsheet of customer PII by taking a screenshot of it and attaching the "
            "resulting PNG image to a personal webmail message. The organization's DLP solution, which pattern-"
            "matches sensitive data only in email body text and text-based attachments, does not detect or block "
            "the transfer. Which DLP capability, if enabled, would have detected this specific exfiltration method?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Optical character recognition (OCR)-based content inspection that extracts and analyzes text "
                    "embedded within image files before allowing transmission"
                ),
                "correct": True,
                "rationale": (
                    "Correct. OCR-based inspection extracts the textual content from image attachments so pattern "
                    "matching can be applied to it, closing the exact gap that let a screenshot bypass text-only "
                    "content inspection."
                ),
            },
            {
                "id": "b",
                "text": "Endpoint DLP monitoring of clipboard copy/paste actions only",
                "correct": False,
                "rationale": (
                    "Incorrect. Clipboard monitoring addresses copy/paste-based exfiltration but does not analyze "
                    "the content of an image file attached to an email; it would not have flagged this specific "
                    "screenshot-based transfer method."
                ),
            },
            {
                "id": "c",
                "text": "Network DLP inspecting only SMTP envelope and header metadata",
                "correct": False,
                "rationale": (
                    "Incorrect. Header/metadata inspection reveals sender, recipient, and routing information but "
                    "does not analyze the content of an attached file, so it would not detect PII embedded in an "
                    "image."
                ),
            },
            {
                "id": "d",
                "text": "A blanket policy blocking all .png file attachments in outbound email",
                "correct": False,
                "rationale": (
                    "Incorrect. Blocking every image attachment outright would stop this specific attack but is "
                    "overly disruptive to legitimate business use of images and does not represent targeted "
                    "content-aware detection; it is a blunt workaround rather than the capability that closes the "
                    "detection gap."
                ),
            },
        ],
        "explanation": (
            "Standard DLP content inspection relies on text pattern matching, which image files bypass entirely. "
            "OCR-based inspection specifically extracts text from images so DLP policies can be applied to that "
            "content, addressing this exfiltration technique without indiscriminately blocking all images."
        ),
    },
    {
        "id": "nd4e-014",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "EDR/XDR & DLP",
        "stem": (
            "During an intrusion, an attacker who gained local administrator rights uninstalls the EDR agent from "
            "a compromised workstation. No alert fires; the EDR management console simply shows the endpoint's "
            "status as 'offline,' identical to how it would appear if the machine were merely powered off. Which "
            "EDR capability, if properly configured, would have specifically detected and alerted on this "
            "action?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Tamper protection that generates a high-priority alert whenever the agent is stopped, "
                    "uninstalled, or its self-defense mechanisms are bypassed, distinct from a routine offline "
                    "status"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Tamper protection specifically distinguishes a deliberate agent removal/disable "
                    "event from a benign offline state and raises a dedicated high-priority alert, closing the "
                    "exact visibility gap described."
                ),
            },
            {
                "id": "b",
                "text": "File integrity monitoring (FIM) on core operating system binaries",
                "correct": False,
                "rationale": (
                    "Incorrect. FIM detects unauthorized changes to monitored system files; it is not designed "
                    "to specifically detect the removal of the EDR agent itself and would not necessarily flag "
                    "this action."
                ),
            },
            {
                "id": "c",
                "text": "Increasing the CPU and memory resources allocated to the EDR agent process",
                "correct": False,
                "rationale": (
                    "Incorrect. Resource allocation has no bearing on detecting agent removal or tampering; it "
                    "is an unrelated performance consideration."
                ),
            },
            {
                "id": "d",
                "text": "A network-based intrusion detection system (NIDS) positioned at the network perimeter",
                "correct": False,
                "rationale": (
                    "Incorrect. A perimeter NIDS inspects network traffic crossing the boundary; it has no "
                    "visibility into a local, host-level action such as an administrator uninstalling an "
                    "endpoint agent."
                ),
            },
        ],
        "explanation": (
            "EDR tamper/self-protection features are specifically designed to raise a distinct, high-priority "
            "alert when the agent is stopped or removed, rather than silently reporting the same generic "
            "'offline' status used for benign disconnections such as a powered-down machine."
        ),
    },
    {
        "id": "nd4e-015",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Email security (SPF/DKIM/DMARC)",
        "stem": (
            "A former employee who previously had access to the organization's DKIM private signing key downloads "
            "a copy shortly before departing. IT is unaware the key material may have been copied. Which risk "
            "does this create, and what remediation is REQUIRED to fully address it?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Anyone possessing the private key can forge messages with a valid DKIM signature for the "
                    "domain; the organization must rotate the DKIM key pair (generate a new key, publish the new "
                    "public key under a new selector in DNS) and retire the old selector"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A DKIM private key is the sole secret that produces valid signatures; anyone who "
                    "holds it can sign forged mail that will pass DKIM validation. Only rotating to a new key "
                    "pair and retiring the old selector eliminates the exposed key's ability to produce valid "
                    "signatures."
                ),
            },
            {
                "id": "b",
                "text": "Update the SPF record to remove the former employee's known IP address",
                "correct": False,
                "rationale": (
                    "Incorrect. SPF authorizes sending IP addresses and is unrelated to DKIM's private signing "
                    "key; removing an IP from SPF does nothing to prevent someone from using a stolen DKIM key to "
                    "cryptographically sign forged mail."
                ),
            },
            {
                "id": "c",
                "text": "Set DMARC policy to p=reject without rotating the DKIM key",
                "correct": False,
                "rationale": (
                    "Incorrect. DMARC enforcement alone is insufficient here: a forged message signed with the "
                    "still-valid, compromised DKIM key would pass DKIM alignment and therefore still pass DMARC, "
                    "since the key itself remains cryptographically valid until rotated."
                ),
            },
            {
                "id": "d",
                "text": "Reset the former employee's mailbox account password",
                "correct": False,
                "rationale": (
                    "Incorrect. A mailbox password reset addresses account login access but does nothing about a "
                    "separately exposed cryptographic signing key, which can be used entirely outside of any "
                    "mailbox login."
                ),
            },
        ],
        "explanation": (
            "DKIM trust is entirely dependent on the secrecy of the private signing key. Once a key is exposed, "
            "DMARC enforcement alone cannot mitigate the risk because forged mail signed with the valid, "
            "compromised key will still pass DKIM alignment; only key rotation closes the exposure."
        ),
    },
    {
        "id": "nd4e-016",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Email security (SPF/DKIM/DMARC)",
        "stem": (
            "An organization enforces DMARC p=reject. Employees regularly send legitimate messages to a "
            "professional mailing list, which relays the messages to other subscribers after adding a footer to "
            "the body and resending from its own server's IP address rather than the original sender's. "
            "Subscribers' receiving mail systems begin rejecting these forwarded messages because both SPF and "
            "DKIM fail after the relay, even though the mail was originally legitimate. Which mechanism is "
            "specifically designed to preserve authentication trust through this kind of intermediary forwarding?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Authenticated Received Chain (ARC)",
                "correct": True,
                "rationale": (
                    "Correct. ARC allows an intermediary, such as a mailing list server, to cryptographically "
                    "attest to the authentication results it observed on the original message, so the final "
                    "receiving system can trust that the mail was legitimately authenticated before forwarding "
                    "modified it."
                ),
            },
            {
                "id": "b",
                "text": "Increasing the SPF record's DNS lookup limit",
                "correct": False,
                "rationale": (
                    "Incorrect. SPF has a fixed protocol limit of 10 DNS lookups that cannot be increased, and "
                    "the failure described here is caused by the mailing list sending from a different IP "
                    "entirely, not by exceeding the lookup limit."
                ),
            },
            {
                "id": "c",
                "text": "Relaxing the domain's DMARC policy to p=none",
                "correct": False,
                "rationale": (
                    "Incorrect. Moving to monitor-only mode would stop the forwarded mail from being rejected, "
                    "but it also removes DMARC's enforcement protection against actual spoofing across the entire "
                    "domain — a broad trade-off, not a targeted fix for the forwarding scenario."
                ),
            },
            {
                "id": "d",
                "text": "Asking the mailing list operator to stop adding a footer to the message body",
                "correct": False,
                "rationale": (
                    "Incorrect. Removing the footer would fix the DKIM body-signature break but would not resolve "
                    "the SPF failure, since the mailing list still relays from its own IP address rather than the "
                    "original sender's authorized IP."
                ),
            },
        ],
        "explanation": (
            "ARC was purpose-built to solve the indirect-mail-flow problem: it lets forwarders and mailing lists "
            "attach a signed record of the authentication results they observed, letting the final recipient "
            "trust the original sender's legitimacy despite SPF/DKIM breaking during forwarding."
        ),
    },
    {
        "id": "nd4e-017",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Federation & SSO (SAML/OAuth)",
        "stem": (
            "During an authorized assessment, a tester intercepts a valid, correctly signed SAML assertion issued "
            "during a legitimate SSO login. Twelve hours later — long after the original session ended — the "
            "tester replays the identical assertion XML to the service provider and is granted access again. "
            "Which missing validation in the service provider's SAML processing MOST directly explains this "
            "result?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The service provider is not enforcing the assertion's time-bound validity conditions "
                    "(NotBefore/NotOnOrAfter) and is not tracking previously used assertion IDs to reject replays"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A properly implemented SP rejects assertions outside their validity window and "
                    "tracks assertion IDs already consumed to prevent reuse. The described replay succeeding "
                    "twelve hours later indicates both of these temporal/replay protections are missing."
                ),
            },
            {
                "id": "b",
                "text": "The service provider is not validating the Audience Restriction element",
                "correct": False,
                "rationale": (
                    "Incorrect. Audience Restriction validation ensures an assertion is only accepted by its "
                    "intended service provider; it prevents a token issued for one SP from being used at another, "
                    "but it would not by itself prevent the same SP from accepting the same assertion replayed "
                    "hours later."
                ),
            },
            {
                "id": "c",
                "text": "The assertion's digital signature was not validated by the service provider",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario states the assertion is 'validly signed' and was accepted as such; "
                    "the issue is not signature integrity but rather the lack of temporal/replay controls on an "
                    "otherwise genuinely signed assertion."
                ),
            },
            {
                "id": "d",
                "text": "The identity provider is not requiring multifactor authentication at login",
                "correct": False,
                "rationale": (
                    "Incorrect. MFA at the IdP affects how the original assertion was issued, not whether a "
                    "captured, already-issued assertion can be replayed later; this scenario is entirely about "
                    "SP-side assertion validation, not the strength of the original authentication event."
                ),
            },
        ],
        "explanation": (
            "SAML assertions include explicit validity-window conditions and unique identifiers specifically to "
            "prevent replay. A service provider that ignores these and only checks the signature remains "
            "vulnerable to accepting a captured, previously-issued assertion long after it should have expired."
        ),
    },
    {
        "id": "nd4e-018",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Federation & SSO (SAML/OAuth)",
        "stem": (
            "A legacy single-page application uses the OAuth 2.0 implicit grant flow, which returns the access "
            "token directly in the browser's URL fragment after authentication. A security review finds the "
            "access token is subsequently captured in browser history and in the analytics platform's referrer "
            "logs. Which remediation BEST addresses this specific weakness while still supporting a browser-based "
            "application?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Migrate to the Authorization Code flow with Proof Key for Code Exchange (PKCE), exchanging a "
                    "short-lived authorization code for the access token via a back-channel request instead of "
                    "returning the token in the browser URL"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Authorization Code flow with PKCE avoids ever exposing the access token in the "
                    "browser's URL; the token is retrieved via a direct back-channel exchange, eliminating the "
                    "history/referrer-log exposure inherent to the implicit flow."
                ),
            },
            {
                "id": "b",
                "text": "Shorten the access token's expiration time",
                "correct": False,
                "rationale": (
                    "Incorrect. A shorter lifetime reduces the window during which a leaked token remains useful, "
                    "but it does not stop the token from being exposed in the URL, browser history, and referrer "
                    "logs in the first place."
                ),
            },
            {
                "id": "c",
                "text": "Replace OAuth 2.0 with SAML for this application",
                "correct": False,
                "rationale": (
                    "Incorrect. Switching protocols entirely is an unnecessary architectural change that does not "
                    "specifically solve URL-fragment token exposure, and SAML's own browser-redirect-based flows "
                    "carry different, unrelated exposure considerations."
                ),
            },
            {
                "id": "d",
                "text": "Require the user to re-authenticate before every individual API call",
                "correct": False,
                "rationale": (
                    "Incorrect. Constant re-authentication severely harms usability and does not address the root "
                    "cause — the token is still returned via the exposed URL fragment mechanism at each login."
                ),
            },
        ],
        "explanation": (
            "The implicit grant flow is deprecated specifically because it exposes tokens in the browser URL. "
            "Authorization Code flow with PKCE was designed as its replacement for public clients like SPAs, "
            "retrieving the token through a back-channel exchange instead of the browser-visible URL."
        ),
    },
    {
        "id": "nd4e-019",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Hardening & secure baselines",
        "stem": (
            "During an internal penetration test, the tester captures NTLM password hashes by responding to "
            "broadcast LLMNR and NetBIOS Name Service (NBT-NS) name-resolution requests on the internal network, "
            "then relays the captured hashes to gain further access to other hosts. Which hardening change BEST "
            "eliminates this specific attack vector?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Disable LLMNR and NetBIOS-NS via Group Policy across all Windows endpoints",
                "correct": True,
                "rationale": (
                    "Correct. LLMNR and NBT-NS are fallback, unauthenticated broadcast name-resolution protocols "
                    "that any host on the segment can respond to. Disabling both and relying solely on DNS "
                    "eliminates the mechanism the attacker used to capture hashes."
                ),
            },
            {
                "id": "b",
                "text": "Enable SMB signing on all endpoints",
                "correct": False,
                "rationale": (
                    "Incorrect. SMB signing helps prevent a captured/relayed hash from being used to authenticate "
                    "an SMB session, but it does not stop the initial broadcast-poisoning technique that captures "
                    "the hashes in the first place, which is what this scenario asks to eliminate."
                ),
            },
            {
                "id": "c",
                "text": "Require longer, more complex user passwords",
                "correct": False,
                "rationale": (
                    "Incorrect. LLMNR/NBT-NS poisoning captures and relays the NTLM hash itself rather than a "
                    "plaintext password to be brute-forced, so password complexity has no bearing on this "
                    "particular technique."
                ),
            },
            {
                "id": "d",
                "text": "Disable the built-in local Guest account on all endpoints",
                "correct": False,
                "rationale": (
                    "Incorrect. The Guest account is unrelated to broadcast name-resolution poisoning; disabling "
                    "it addresses a separate default-account hardening concern, not this attack vector."
                ),
            },
        ],
        "explanation": (
            "LLMNR/NBT-NS poisoning is a classic and highly effective internal attack technique because these "
            "legacy fallback protocols trust any responder on the local segment. Disabling them and enforcing "
            "DNS-only resolution removes the vulnerable mechanism entirely, rather than just mitigating its "
            "downstream use."
        ),
    },
    {
        "id": "nd4e-020",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Hardening & secure baselines",
        "stem": (
            "A fleet of field-service laptops connects to the corporate network via VPN for only a few hours each "
            "week. Select TWO practices that would MOST effectively keep these devices compliant with the "
            "organization's secure configuration baseline despite this limited connectivity."
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Deploy an agent-based configuration management tool that enforces and re-applies baseline "
                    "settings locally on a recurring schedule, independent of an active connection to a central "
                    "management server"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Local, agent-based enforcement continues to apply and correct baseline settings "
                    "even while the device is disconnected, rather than depending on the intermittent VPN session "
                    "to deliver policy."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Configure the agent to cache local compliance scan results and automatically transmit them "
                    "to the central console the next time connectivity becomes available"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Local caching with delayed transmission ensures compliance state is still assessed "
                    "and eventually reported even though the device is offline most of the time, closing the "
                    "visibility gap without requiring constant connectivity."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Rely on Group Policy Objects refreshed only when the device authenticates to a domain "
                    "controller over VPN, since GPO enforcement alone covers all necessary baseline settings"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. GPO refresh depends on connectivity to a domain controller, which this fleet has "
                    "for only a few hours weekly, leaving long unenforced gaps between VPN sessions — exactly the "
                    "constraint the scenario is asking to overcome."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Rely on a cloud-based CASB to continuously inspect and remediate the device's local "
                    "operating system configuration in real time"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A CASB inspects and controls access to cloud services/SaaS traffic; it does not "
                    "have visibility into or control over a device's local OS-level configuration state, and it "
                    "also requires connectivity that this fleet largely lacks."
                ),
            },
        ],
        "explanation": (
            "Devices with limited, intermittent connectivity require enforcement mechanisms that operate locally "
            "and independently of the network connection, with results cached and synced opportunistically — "
            "connectivity-dependent tools like GPO refresh or CASB inspection cannot maintain compliance during "
            "long offline periods."
        ),
    },
    {
        "id": "nd4e-021",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Incident response process",
        "stem": (
            "During an active incident, the IR team places a temporary ACL around the compromised network segment "
            "to stop lateral spread while forensic imaging is still pending, planning to fully rebuild the "
            "affected hosts from clean images once evidence collection is complete. Which term BEST describes the "
            "temporary ACL action taken?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Short-term containment",
                "correct": True,
                "rationale": (
                    "Correct. A temporary measure applied to immediately limit damage and stop spread — while "
                    "preserving evidence for later analysis and before a permanent fix is built — is the "
                    "definition of short-term (immediate) containment."
                ),
            },
            {
                "id": "b",
                "text": "Eradication",
                "correct": False,
                "rationale": (
                    "Incorrect. Eradication involves removing the malicious code, backdoors, and persistence "
                    "mechanisms from affected systems. That has not occurred yet — imaging is still pending and "
                    "the hosts have not been cleaned or rebuilt."
                ),
            },
            {
                "id": "c",
                "text": "Recovery",
                "correct": False,
                "rationale": (
                    "Incorrect. Recovery is the restoration of systems to normal production operation after the "
                    "threat has been eradicated and validated as removed; this scenario is still in the earlier "
                    "containment/evidence-preservation stage, well before recovery."
                ),
            },
            {
                "id": "d",
                "text": "Long-term containment",
                "correct": False,
                "rationale": (
                    "Incorrect. Long-term containment typically involves a more durable, validated fix (e.g., "
                    "patched and hardened systems left in a controlled state for extended operation); the "
                    "scenario explicitly describes a temporary ACL pending a full rebuild, matching short-term "
                    "containment instead."
                ),
            },
        ],
        "explanation": (
            "The IR lifecycle distinguishes short-term containment (immediate, temporary damage limitation that "
            "preserves evidence) from eradication (removing the cause) and recovery (restoring production) — the "
            "temporary ACL here fits the short-term containment stage precisely."
        ),
    },
    {
        "id": "nd4e-022",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Incident response process",
        "stem": (
            "Two weeks after a ransomware incident is fully resolved, the IR team holds a meeting with all "
            "stakeholders to review the incident timeline, identify what worked and what failed (such as a "
            "six-hour detection gap caused by a misconfigured alert), and produce specific, assigned corrective "
            "action items to prevent recurrence. Which IR lifecycle phase does this meeting represent, and which "
            "document should formally capture the findings?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Lessons learned (post-incident activity); the findings should be captured in a formal "
                    "after-action / post-incident review report"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Reviewing an incident's timeline, identifying gaps, and assigning corrective actions "
                    "after full resolution is the defining activity of the lessons-learned phase, formally "
                    "documented in an after-action report."
                ),
            },
            {
                "id": "b",
                "text": "Preparation, by updating the IR plan directly without conducting a formal review meeting",
                "correct": False,
                "rationale": (
                    "Incorrect. Preparation is forward-looking work performed before an incident occurs (building "
                    "readiness); it does not describe the retrospective analysis of an incident that already "
                    "concluded, and it specifically omits the structured review meeting the scenario describes."
                ),
            },
            {
                "id": "c",
                "text": "Containment, by documenting retrospective containment decisions after the fact",
                "correct": False,
                "rationale": (
                    "Incorrect. Containment is an active-incident response activity performed during the "
                    "incident, not a retrospective, stakeholder-wide review conducted two weeks after full "
                    "resolution."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Identification, by reconstructing the timeline only, without producing corrective action "
                    "items"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Identification occurs early in an active incident to confirm and scope it; "
                    "reconstructing the timeline is only part of what is described, and identification alone does "
                    "not encompass assigning corrective action items, which is central to the meeting described."
                ),
            },
        ],
        "explanation": (
            "The lessons-learned (post-incident) phase occurs after an incident is fully resolved and produces a "
            "documented after-action report with specific corrective actions, distinguishing it from the earlier, "
            "in-incident phases of identification and containment and from the pre-incident preparation phase."
        ),
    },
    {
        "id": "nd4e-023",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log data sources",
        "stem": (
            "An analyst identifies malicious activity originating from internal IP address 10.10.4.57 at 14:32 on "
            "a specific day. Because the organization uses dynamic IP addressing, the analyst needs to determine "
            "exactly which device (by MAC address and hostname) held that IP address at that precise time. Which "
            "log source directly answers this question?"
        ),
        "options": [
            {
                "id": "a",
                "text": "DHCP server lease logs",
                "correct": True,
                "rationale": (
                    "Correct. DHCP lease logs record which MAC address/hostname was assigned a given IP address "
                    "and for what time window, directly answering which physical device held 10.10.4.57 at 14:32."
                ),
            },
            {
                "id": "b",
                "text": "Firewall NAT translation logs",
                "correct": False,
                "rationale": (
                    "Incorrect. NAT logs map internal addresses to external (translated) addresses for outbound "
                    "traffic; they do not record which device was assigned a specific internal dynamic IP at a "
                    "given time."
                ),
            },
            {
                "id": "c",
                "text": "NetFlow/IPFIX flow records",
                "correct": False,
                "rationale": (
                    "Incorrect. NetFlow records traffic volume, source, and destination for sessions, but it does "
                    "not record DHCP lease assignment history linking an IP address to a specific MAC address/"
                    "hostname over time."
                ),
            },
            {
                "id": "d",
                "text": "Active Directory authentication logs",
                "correct": False,
                "rationale": (
                    "Incorrect. AD authentication logs show which user account authenticated and when, but they "
                    "do not directly bind a dynamic IP address to a specific physical device's MAC address at a "
                    "given moment."
                ),
            },
        ],
        "explanation": (
            "When addressing is dynamic, only the DHCP server's lease log directly records the binding between an "
            "IP address, a MAC address, and a hostname for a specific time window — the exact mapping needed to "
            "identify the physical device involved."
        ),
    },
    {
        "id": "nd4e-024",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log data sources",
        "stem": (
            "An analyst needs to determine the exact URL path and content category (e.g., file-sharing, newly-"
            "registered domain) of every website a specific workstation visited over HTTPS during a given hour — "
            "not merely the destination IP addresses and ports that firewall session logs would show. Which log "
            "source BEST provides this level of detail?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Forward/web proxy logs",
                "correct": True,
                "rationale": (
                    "Correct. A forward web proxy sits at the application layer and logs the full requested URL "
                    "path along with category/reputation enrichment, providing the specific detail firewall "
                    "session logs cannot capture."
                ),
            },
            {
                "id": "b",
                "text": "Firewall session/connection logs",
                "correct": False,
                "rationale": (
                    "Incorrect. Firewall session logs typically record only source/destination IP, port, and "
                    "byte/session metadata, not the full URL path or content category the analyst needs."
                ),
            },
            {
                "id": "c",
                "text": "DNS query logs",
                "correct": False,
                "rationale": (
                    "Incorrect. DNS logs show which domain names were resolved, not the specific URL paths "
                    "requested within those domains or a content-category classification of the visited pages."
                ),
            },
            {
                "id": "d",
                "text": "NetFlow/IPFIX flow records",
                "correct": False,
                "rationale": (
                    "Incorrect. NetFlow provides flow-level metadata (source, destination, byte counts, duration) "
                    "without any application-layer visibility into URL paths or content categorization."
                ),
            },
        ],
        "explanation": (
            "Only a web/forward proxy operates at the application layer with visibility into full URL paths and "
            "enriched category data; firewall, DNS, and NetFlow logs are each limited to lower-layer or "
            "domain-level metadata that cannot answer this specific investigative question."
        ),
    },
    {
        "id": "nd4e-025",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Malware classification",
        "stem": (
            "A server's CPU utilization spikes to a sustained 100% with no corresponding increase in legitimate "
            "application workload. Investigation reveals a hidden process making continuous outbound connections "
            "to a known cryptocurrency mining pool address and consuming resources to solve cryptographic hash "
            "puzzles for payment in coins. No data is encrypted, stolen, or exfiltrated, and there is no evidence "
            "the host is participating in attacks against other targets. Which malware classification BEST fits "
            "this behavior?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Cryptojacking/cryptomining malware",
                "correct": True,
                "rationale": (
                    "Correct. Hijacking a system's CPU resources to mine cryptocurrency for the attacker's benefit "
                    "— without encrypting, stealing, or exfiltrating data — is the defining behavior of "
                    "cryptojacking malware."
                ),
            },
            {
                "id": "b",
                "text": "Ransomware",
                "correct": False,
                "rationale": (
                    "Incorrect. Ransomware encrypts data and demands payment for a decryption key; the scenario "
                    "explicitly states no data was encrypted, which rules out ransomware despite the malicious "
                    "resource consumption."
                ),
            },
            {
                "id": "c",
                "text": "Botnet/DDoS bot",
                "correct": False,
                "rationale": (
                    "Incorrect. A DDoS bot participates in coordinated attacks against other targets on command "
                    "from a controller; there is no evidence of outbound attack traffic against third parties "
                    "here, only self-directed mining activity."
                ),
            },
            {
                "id": "d",
                "text": "Rootkit",
                "correct": False,
                "rationale": (
                    "Incorrect. A rootkit is defined by active concealment of its presence via OS/kernel-level "
                    "hooking; the scenario describes high resource usage and mining-pool traffic but does not "
                    "describe any concealment mechanism, so rootkit is not the best classification."
                ),
            },
        ],
        "explanation": (
            "The combination of sustained abnormal CPU consumption, outbound connections to a mining pool, and "
            "the explicit absence of encryption, data theft, or coordinated attack traffic uniquely identifies "
            "this as cryptojacking rather than ransomware, a botnet, or a rootkit."
        ),
    },
    {
        "id": "nd4e-026",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Malware classification",
        "stem": (
            "A code review of an internal application update discovers a hardcoded, undocumented account with a "
            "static password that grants direct administrative access. It was deliberately embedded in the "
            "shipped code by a former contractor with legitimate development access, and no disguise, deception, "
            "or social engineering was used to introduce it — it was simply committed directly into the codebase. "
            "Which classification BEST describes this component?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Backdoor",
                "correct": True,
                "rationale": (
                    "Correct. A backdoor is a deliberately embedded, undocumented access mechanism that bypasses "
                    "normal authentication — exactly what this hardcoded administrative account represents — "
                    "regardless of whether it was introduced via deception or by an insider with legitimate "
                    "access."
                ),
            },
            {
                "id": "b",
                "text": "Trojan horse",
                "correct": False,
                "rationale": (
                    "Incorrect. A trojan requires disguising malicious code as legitimate software to trick a "
                    "victim into installing it. Here, an insider with legitimate access committed the code "
                    "directly, with no disguise or deception involved."
                ),
            },
            {
                "id": "c",
                "text": "Logic bomb",
                "correct": False,
                "rationale": (
                    "Incorrect. A logic bomb executes a destructive or malicious payload upon a specific trigger "
                    "condition. The hardcoded account merely grants persistent access; no destructive trigger "
                    "condition is described."
                ),
            },
            {
                "id": "d",
                "text": "Rootkit",
                "correct": False,
                "rationale": (
                    "Incorrect. A rootkit actively conceals its presence through OS-level hooking or manipulation. "
                    "Nothing in the scenario describes the account being hidden from detection tools; it was "
                    "simply undocumented, which is a different characteristic than active concealment."
                ),
            },
        ],
        "explanation": (
            "Backdoors are defined by providing an undocumented, unauthorized access path, which can be "
            "introduced by an insider directly (as here) or delivered via deception (as with a trojan). The "
            "absence of disguise and destructive triggers rules out trojan and logic bomb, and the absence of "
            "active concealment rules out rootkit."
        ),
    },
    {
        "id": "nd4e-027",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile device management",
        "stem": (
            "A corporate-owned laptop is reported stolen. The security team issues a remote wipe command through "
            "the MDM console, but the device is powered off and remains offline, so the command queues without "
            "executing. Which control, if it had been enabled BEFORE the device was stolen, would have provided "
            "the STRONGEST protection for the data at rest regardless of whether the remote wipe command is ever "
            "delivered?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Full-disk/volume encryption enabled and enforced at provisioning",
                "correct": True,
                "rationale": (
                    "Correct. Full-disk encryption protects data confidentiality independently of whether a "
                    "remote wipe command is ever received, since the disk contents remain unreadable without the "
                    "recovery key regardless of the device's power or connectivity state."
                ),
            },
            {
                "id": "b",
                "text": "GPS location tracking enabled through the MDM agent",
                "correct": False,
                "rationale": (
                    "Incorrect. Location tracking can help recover the physical device but does nothing to "
                    "protect the confidentiality of the data stored on it if it is never recovered or if the "
                    "wipe command never executes."
                ),
            },
            {
                "id": "c",
                "text": "A longer, more complex operating system login password",
                "correct": False,
                "rationale": (
                    "Incorrect. A strong login password can be bypassed via offline disk access (e.g., removing "
                    "the drive) if the data itself is not encrypted; it does not provide the same guarantee as "
                    "encryption when the device is out of the organization's physical control."
                ),
            },
            {
                "id": "d",
                "text": "A shorter retry interval for the remote-wipe command",
                "correct": False,
                "rationale": (
                    "Incorrect. Retry frequency is irrelevant if the device never reconnects to receive any "
                    "command at all, which is exactly the situation described — the wipe command's delivery "
                    "depends on connectivity that may never occur."
                ),
            },
        ],
        "explanation": (
            "Remote wipe is a valuable but delivery-dependent control — it cannot execute on a device that never "
            "reconnects. Full-disk encryption enabled in advance protects data confidentiality unconditionally, "
            "independent of whether any remote command is ever successfully delivered."
        ),
    },
    {
        "id": "nd4e-028",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile device management",
        "stem": (
            "An MDM/UEM solution is configured so that only a specific managed line-of-business application "
            "automatically tunnels its traffic through the corporate VPN, while all other apps and general device "
            "browsing use the device's normal internet connection directly. Which MDM capability does this "
            "describe, and what is its PRIMARY benefit over tunneling the entire device's traffic through a "
            "full-device VPN?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Per-app VPN; only sensitive corporate application traffic is routed through and inspected by "
                    "the corporate network, preserving user privacy, battery life, and performance for personal "
                    "app traffic"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Per-app VPN selectively tunnels only designated managed applications' traffic "
                    "through the corporate VPN, protecting corporate data in transit while leaving personal app "
                    "traffic unaffected by corporate routing/inspection."
                ),
            },
            {
                "id": "b",
                "text": "Full-device VPN, which tunnels all traffic on the device through the corporate network",
                "correct": False,
                "rationale": (
                    "Incorrect. This describes the opposite configuration; the scenario explicitly states only "
                    "one specific application's traffic is tunneled, not all traffic from the entire device."
                ),
            },
            {
                "id": "c",
                "text": "Geofencing, restricting application functionality to a defined physical location",
                "correct": False,
                "rationale": (
                    "Incorrect. Geofencing is a location-based access restriction; it has no relationship to "
                    "selectively routing network traffic per application through a VPN."
                ),
            },
            {
                "id": "d",
                "text": "Containerization, isolating corporate data into an encrypted profile on the device",
                "correct": False,
                "rationale": (
                    "Incorrect. Containerization separates and encrypts corporate data/apps at rest on the "
                    "device; it is a data-separation mechanism, not the network-traffic-routing mechanism "
                    "described in the scenario."
                ),
            },
        ],
        "explanation": (
            "Per-app VPN allows an MDM policy to selectively tunnel only specific managed applications' network "
            "traffic through the corporate VPN, balancing protection of corporate data in transit against "
            "unnecessary privacy, battery, and performance impact on personal app usage."
        ),
    },
    {
        "id": "nd4e-029",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Multifactor authentication",
        "stem": (
            "A company deploys facial recognition as a second authentication factor for a secure building "
            "entrance. During an authorized red team assessment, a tester successfully authenticates by holding a "
            "high-resolution printed photograph of an employee's face up to the camera. Which missing capability "
            "MOST directly explains this bypass?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Liveness detection (anti-spoofing)",
                "correct": True,
                "rationale": (
                    "Correct. Liveness detection verifies that a biometric sample originates from a live, "
                    "physically present person — using techniques such as depth sensing, blink/movement "
                    "detection, or infrared — rather than merely matching a static facial pattern, which is "
                    "exactly what a printed photo can fool without it."
                ),
            },
            {
                "id": "b",
                "text": "Stronger encryption of stored biometric templates",
                "correct": False,
                "rationale": (
                    "Incorrect. Template encryption protects stored biometric data from theft or exposure; it "
                    "does not address whether the live capture at the camera can distinguish a real face from a "
                    "static photograph."
                ),
            },
            {
                "id": "c",
                "text": "A policy requiring biometrics never be used as a standalone factor",
                "correct": False,
                "rationale": (
                    "Incorrect. While combining biometrics with another factor is generally good practice, it "
                    "does not address the SPECIFIC missing capability that allowed a static photo to fool the "
                    "facial recognition sensor itself."
                ),
            },
            {
                "id": "d",
                "text": "A higher-resolution camera sensor",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario states a high-resolution photograph still succeeded; increasing "
                    "camera resolution further would not address the underlying gap, which is the inability to "
                    "distinguish a live subject from any static image regardless of image quality."
                ),
            },
        ],
        "explanation": (
            "Facial recognition systems must include liveness detection to distinguish a genuine, live subject "
            "from a static photograph, video replay, or mask; without it, the system only performs pattern "
            "matching against whatever image is presented, live or not."
        ),
    },
    {
        "id": "nd4e-030",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Multifactor authentication",
        "stem": (
            "An organization deploys FIDO2 passkeys configured to sync automatically across a user's personal "
            "devices via their consumer cloud account, rather than being bound to a single, non-exportable "
            "hardware security key. A security architect raises a concern about this configuration compared to a "
            "hardware-bound FIDO2 key. What is the PRIMARY security trade-off being introduced?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Synced passkeys can potentially be extracted or replicated if the user's cloud account "
                    "itself is compromised, whereas a hardware-bound key's private key never leaves the physical "
                    "device and cannot be exported or cloned"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Synced passkeys rely on the security of the underlying cloud account for key "
                    "material distribution; if that account is compromised, the private key material could "
                    "potentially be extracted or synced to an attacker-controlled device, a risk that does not "
                    "exist for a hardware-bound key whose private key never leaves the token."
                ),
            },
            {
                "id": "b",
                "text": "Synced passkeys are inherently less phishing-resistant than a traditional password",
                "correct": False,
                "rationale": (
                    "Incorrect. Both synced and hardware-bound passkeys remain origin-bound and phishing-resistant "
                    "by design (the credential is cryptographically tied to the legitimate site's origin); this "
                    "property does not disappear because the key material is synced across devices."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Synced passkeys require an additional separate PIN beyond the passkey itself, adding an "
                    "unnecessary factor"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This describes local unlock behavior common to both synced and hardware-bound "
                    "implementations, not the trade-off the scenario is specifically asking about (the risk "
                    "introduced by cloud-account-based syncing itself)."
                ),
            },
            {
                "id": "d",
                "text": "Hardware security keys are inherently unable to support more than one account at a time",
                "correct": False,
                "rationale": (
                    "Incorrect. This describes a potential practical limitation of hardware keys, not the "
                    "trade-off introduced by the synced configuration that the question specifically asks about."
                ),
            },
        ],
        "explanation": (
            "Passkey syncing improves usability and recovery by distributing key material through a cloud "
            "account, but it introduces a dependency on that account's security — a hardware-bound key avoids "
            "this by keeping the private key non-exportable and confined to the physical token."
        ),
    },
    {
        "id": "nd4e-031",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Penetration testing phases",
        "stem": (
            "Earlier in an authorized engagement, a penetration tester gathered information exclusively from "
            "public sources — LinkedIn profiles, WHOIS records, and certificate transparency logs — without "
            "sending any traffic to the target's systems. The tester now runs Nmap SYN scans and banner-grabbing "
            "queries directly against the target's live production hosts to enumerate open ports and running "
            "service versions, before attempting any exploitation. Which phase does this second activity "
            "represent, and how does it fundamentally differ from the earlier information gathering?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Active reconnaissance; unlike the earlier passive reconnaissance, it directly interacts with "
                    "and generates detectable traffic against the target's systems"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Directly probing target systems (port scans, banner grabs) generates traffic and "
                    "logs on the target's infrastructure, which is the defining trait of active reconnaissance — "
                    "in contrast to the earlier passive reconnaissance, which gathered information solely from "
                    "public/third-party sources without touching the target."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Still passive reconnaissance, since no exploit code was executed against the target during "
                    "the scan"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The key distinction between active and passive reconnaissance is whether the "
                    "target is directly interacted with and generates observable traffic, not whether "
                    "exploitation has occurred; scanning directly against live hosts is active regardless of "
                    "exploit status."
                ),
            },
            {
                "id": "c",
                "text": "Exploitation, because vulnerabilities are being probed for on the live systems",
                "correct": False,
                "rationale": (
                    "Incorrect. Enumerating open ports and service versions identifies potential targets for "
                    "later exploitation but does not itself leverage a vulnerability to gain unauthorized access, "
                    "so it has not yet reached the exploitation phase."
                ),
            },
            {
                "id": "d",
                "text": "Post-exploitation, since the tester is gathering detailed system information",
                "correct": False,
                "rationale": (
                    "Incorrect. Post-exploitation activities occur only after initial access/foothold has already "
                    "been gained; no access has been achieved yet in this scenario, only external scanning."
                ),
            },
        ],
        "explanation": (
            "Passive reconnaissance gathers information without touching the target (OSINT, WHOIS, certificate "
            "transparency); active reconnaissance directly interacts with and generates detectable traffic "
            "against target systems, such as port scanning — a distinction independent of whether exploitation "
            "has begun."
        ),
    },
    {
        "id": "nd4e-032",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Penetration testing phases",
        "stem": (
            "A client provides a penetration testing team with full network diagrams, source code access, and "
            "administrative credentials to internal systems before testing begins, explicitly to maximize "
            "vulnerability coverage within a compressed testing window. Which testing type is this, and what is "
            "its PRIMARY trade-off compared to an unknown-environment approach?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Known environment (full-knowledge) testing; it achieves deeper, faster, more comprehensive "
                    "coverage but does not realistically simulate what an external attacker without insider "
                    "information would need to independently discover"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Providing full network diagrams, source code, and credentials up front is the "
                    "definition of known-environment (full-knowledge) testing; its trade-off is reduced realism "
                    "regarding what an attacker with zero insider knowledge would actually be able to find and "
                    "exploit on their own."
                ),
            },
            {
                "id": "b",
                "text": "Unknown environment testing, since the tester still has to discover vulnerabilities",
                "correct": False,
                "rationale": (
                    "Incorrect. Unknown environment (black-box) testing means the tester begins with no prior "
                    "information at all; this scenario is the opposite, explicitly granting full diagrams, "
                    "source, and credentials from the outset."
                ),
            },
            {
                "id": "c",
                "text": "Partial knowledge testing, since not every possible piece of information was provided",
                "correct": False,
                "rationale": (
                    "Incorrect. Partial knowledge testing provides some, but not full, information (such as "
                    "limited-privilege credentials only). The scenario explicitly grants full network diagrams, "
                    "source code, and administrative credentials — the complete set of information, exceeding a "
                    "partial-knowledge scope."
                ),
            },
            {
                "id": "d",
                "text": "Physical penetration testing, focused on gaining unauthorized physical facility access",
                "correct": False,
                "rationale": (
                    "Incorrect. This describes a testing category based on the type of target (physical "
                    "facilities) rather than the level of prior knowledge provided to the tester, which is what "
                    "the scenario is actually describing."
                ),
            },
        ],
        "explanation": (
            "Known-environment (full-knowledge) testing maximizes depth and speed of coverage by giving testers "
            "complete internal information up front, at the cost of realism compared to simulating an attacker "
            "who must discover everything independently, as in unknown-environment testing."
        ),
    },
    {
        "id": "nd4e-033",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Port and protocol security",
        "stem": (
            "A vulnerability scan finds that an internal application authenticates to the corporate directory "
            "service using unencrypted LDAP (TCP 389), transmitting bind credentials and directory queries in "
            "cleartext across the network segment. Which remediation BEST addresses this finding?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Reconfigure the application to use LDAPS (LDAP over TLS, TCP 636) or STARTTLS so credentials "
                    "and queries are encrypted in transit"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Reconfiguring the application to bind over LDAPS/STARTTLS encrypts the "
                    "authentication exchange and query traffic, directly eliminating the cleartext exposure "
                    "identified by the scan."
                ),
            },
            {
                "id": "b",
                "text": "Firewall off TCP 389 entirely without making any other configuration changes",
                "correct": False,
                "rationale": (
                    "Incorrect. Abruptly blocking the port the application currently depends on without "
                    "reconfiguring it to use an encrypted alternative would break the application's directory "
                    "authentication rather than fixing the underlying cleartext transmission."
                ),
            },
            {
                "id": "c",
                "text": "Move the LDAP server to an isolated VLAN, without changing the application's protocol",
                "correct": False,
                "rationale": (
                    "Incorrect. Segmentation reduces the scope of hosts that could observe the traffic but "
                    "credentials would still traverse that VLAN in cleartext to any host present there; it does "
                    "not address the underlying lack of encryption."
                ),
            },
            {
                "id": "d",
                "text": "Require a longer, more complex bind account password",
                "correct": False,
                "rationale": (
                    "Incorrect. Password complexity does not prevent the credential from being transmitted and "
                    "captured in cleartext; an attacker who intercepts the cleartext bind traffic obtains the "
                    "credential regardless of its complexity."
                ),
            },
        ],
        "explanation": (
            "LDAP transmits authentication and query data in cleartext by default. The specific remediation is "
            "encrypting the transport via LDAPS or STARTTLS, since segmentation and password complexity do not "
            "address the fundamental lack of encryption on the wire."
        ),
    },
    {
        "id": "nd4e-034",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Port and protocol security",
        "stem": (
            "During an authorized external assessment, a tester successfully performs a full DNS zone transfer "
            "(AXFR) against the organization's public-facing authoritative DNS server, revealing the complete "
            "internal naming scheme, including hostnames for servers that were never intended to be publicly "
            "known. Which remediation BEST prevents this specific exposure?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Restrict zone transfers (AXFR/IXFR) to only explicitly authorized secondary DNS servers by "
                    "IP address and/or TSIG key, denying transfer requests from any other host"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Restricting who is permitted to request a zone transfer to specific, authenticated "
                    "secondary name servers directly prevents an arbitrary external party from pulling the "
                    "complete zone file, which is the exact exposure demonstrated."
                ),
            },
            {
                "id": "b",
                "text": "Disable DNS service entirely on the public-facing server",
                "correct": False,
                "rationale": (
                    "Incorrect. Disabling DNS entirely would also break legitimate public name resolution for the "
                    "organization's domain, making the service unusable rather than fixing the specific "
                    "zone-transfer authorization gap."
                ),
            },
            {
                "id": "c",
                "text": "Switch DNS query handling from UDP port 53 to TCP port 53 exclusively",
                "correct": False,
                "rationale": (
                    "Incorrect. Zone transfers already typically occur over TCP; changing the transport protocol "
                    "used for ordinary DNS queries does nothing to restrict who is authorized to request a "
                    "transfer of the zone data."
                ),
            },
            {
                "id": "d",
                "text": "Enable DNSSEC on the zone",
                "correct": False,
                "rationale": (
                    "Incorrect. DNSSEC protects the integrity and authenticity of DNS responses against tampering "
                    "and cache poisoning; it does not restrict who is permitted to request a zone transfer and "
                    "would not have prevented this enumeration."
                ),
            },
        ],
        "explanation": (
            "An unrestricted zone transfer allows any requester to enumerate an organization's entire internal "
            "naming scheme in one query. The specific fix is authorizing zone transfers only to designated "
            "secondary name servers, not disabling DNS, changing transport protocol, or enabling DNSSEC, none of "
            "which control transfer authorization."
        ),
    },
    {
        "id": "nd4e-035",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Privileged access management",
        "stem": (
            "An audit finds that domain administrators routinely perform privileged Active Directory management "
            "tasks from the same general-purpose laptop they use daily for web browsing and email. Malware "
            "delivered through a phishing email on that laptop subsequently captures cached domain admin "
            "credentials during a routine administrative session. Which control would have MOST directly "
            "prevented this specific compromise path?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Require administrators to perform privileged tasks only from a dedicated, hardened "
                    "privileged access workstation (PAW) that is never used for browsing, email, or general-"
                    "purpose activity"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A dedicated PAW isolates the environment where privileged credentials are used from "
                    "the general-purpose laptop's much larger attack surface (email, browsing), directly removing "
                    "the phishing-delivered malware's opportunity to capture credentials during an admin session."
                ),
            },
            {
                "id": "b",
                "text": "Just-in-time (JIT) privilege elevation for the duration of each administrative task",
                "correct": False,
                "rationale": (
                    "Incorrect. JIT elevation limits how long standing privilege exists, but it does not stop "
                    "malware already present on the same general-purpose machine from capturing credentials "
                    "during the window when elevated access IS active."
                ),
            },
            {
                "id": "c",
                "text": "Privileged session recording for all administrative activity",
                "correct": False,
                "rationale": (
                    "Incorrect. Session recording provides audit evidence after the fact for investigation; it "
                    "does not prevent the initial credential theft from occurring on a compromised general-"
                    "purpose endpoint."
                ),
            },
            {
                "id": "d",
                "text": "Enforcing stronger password complexity requirements for admin accounts",
                "correct": False,
                "rationale": (
                    "Incorrect. The credentials were captured via malware from a cached session, not guessed or "
                    "brute forced, so password complexity has no bearing on preventing this specific theft "
                    "mechanism."
                ),
            },
        ],
        "explanation": (
            "Using a general-purpose, internet-facing endpoint for privileged administrative work exposes "
            "credentials to that machine's much larger attack surface. A dedicated privileged access workstation "
            "eliminates this exposure by isolating privileged sessions from everyday browsing and email use."
        ),
    },
    {
        "id": "nd4e-036",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Privileged access management",
        "stem": (
            "Select TWO practices that help detect and remediate privilege creep — the gradual accumulation of "
            "unnecessary privileged entitlements by user accounts over time — in an enterprise identity program."
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Periodic access recertification campaigns in which resource/data owners must explicitly "
                    "review and re-approve, or revoke, each user's privileged entitlements on a recurring schedule"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Recurring recertification forces an explicit, positive re-justification of every "
                    "privileged entitlement, surfacing and removing access that has accumulated but is no longer "
                    "needed."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Automated reporting that flags privileged accounts which have not exercised a specific "
                    "granted entitlement within a defined period, for review and potential revocation"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Usage-based reporting identifies entitlements that are unused over time — a strong "
                    "indicator of unnecessary, lingering privilege — enabling targeted, evidence-based revocation."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Granting all new employees the same privileged entitlements as the most senior member of "
                    "their team, to reduce future access-request tickets"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This practice actively causes over-provisioning and privilege creep from the "
                    "start of employment rather than detecting or remediating it, directly contradicting least "
                    "privilege."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Requiring a single one-time approval for a privileged entitlement at hire, valid for the "
                    "remainder of the employee's tenure without further review"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A one-time approval with no recurring review is exactly the gap that allows "
                    "privilege creep to accumulate undetected over an employee's tenure, rather than a control "
                    "that remediates it."
                ),
            },
        ],
        "explanation": (
            "Privilege creep is best countered by recurring, explicit re-justification of access (recertification) "
            "combined with usage-based reporting that flags stale, unexercised entitlements — one-time approvals "
            "and role-copying at hire are practices that create the problem, not solve it."
        ),
    },
    {
        "id": "nd4e-037",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "A SIEM's primary ransomware-detection rule alerts only when traffic is observed to one of a static "
            "list of known-malicious command-and-control IP addresses maintained by a threat intelligence feed. "
            "During a new ransomware campaign using entirely new, previously unseen infrastructure, the rule "
            "generates zero alerts even though several servers are ultimately encrypted. Which enhancement would "
            "MOST improve the SIEM's ability to detect this type of NEW campaign in the future?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Add behavior-based correlation rules (e.g., rapid mass file rename/modification rates, "
                    "abnormal SMB write volumes, unusual process trees) that do not depend on matching a static, "
                    "previously known IOC list"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Behavior-based detection identifies the malicious activity pattern itself rather "
                    "than relying on previously known infrastructure, so it can catch a campaign using brand-new "
                    "IP addresses that no static IOC list would yet contain."
                ),
            },
            {
                "id": "b",
                "text": "Increase how frequently the static IOC list is refreshed from the threat intel feed",
                "correct": False,
                "rationale": (
                    "Incorrect. A brand-new campaign's infrastructure is unlikely to appear on any threat intel "
                    "feed yet, regardless of refresh frequency, since the IOC list is fundamentally reactive and "
                    "trails newly stood-up infrastructure."
                ),
            },
            {
                "id": "c",
                "text": "Lower the alert severity threshold on the existing static-IP-match rule",
                "correct": False,
                "rationale": (
                    "Incorrect. The rule never matched at all because the new campaign's IPs were not on the "
                    "list; adjusting the severity of an alert that never fires does not create any new detections."
                ),
            },
            {
                "id": "d",
                "text": "Subscribe to additional threat intelligence feed sources beyond the current one",
                "correct": False,
                "rationale": (
                    "Incorrect. While more feeds may marginally improve coverage, this remains a fundamentally "
                    "reactive, signature-based approach that will still miss entirely new, unlisted infrastructure "
                    "used by a fresh campaign."
                ),
            },
        ],
        "explanation": (
            "Static IOC-based detection is inherently reactive and blind to brand-new attacker infrastructure. "
            "Behavior-based correlation rules that detect the malicious activity pattern itself (mass file "
            "modification, abnormal write volume) remain effective regardless of whether the specific IOCs have "
            "ever been seen before."
        ),
    },
    {
        "id": "nd4e-038",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A vulnerability initially scored 8.1 (High) using CVSS Base metrics is later re-scored at 9.3 after "
            "a fully weaponized, publicly available exploit module is released and the vendor confirms a patch "
            "will not be available for another 60 days. Which CVSS metric group specifically accounts for score "
            "changes driven by exploit code maturity and remediation availability evolving over time?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Temporal metric group",
                "correct": True,
                "rationale": (
                    "Correct. The Temporal metric group (Exploit Code Maturity, Remediation Level, Report "
                    "Confidence) is specifically designed to adjust the score as real-world conditions like "
                    "exploit availability and patch status change over time, independent of the vulnerability's "
                    "intrinsic characteristics."
                ),
            },
            {
                "id": "b",
                "text": "Base metric group",
                "correct": False,
                "rationale": (
                    "Incorrect. The Base metric group reflects the vulnerability's intrinsic, constant "
                    "characteristics (such as attack vector and privileges required), which do not change over "
                    "time and therefore would not explain a score shift driven by exploit release or patch "
                    "delay."
                ),
            },
            {
                "id": "c",
                "text": "Environmental metric group",
                "correct": False,
                "rationale": (
                    "Incorrect. The Environmental metric group reflects a specific organization's deployment "
                    "context, such as network segmentation or asset criticality — this scenario describes a "
                    "change based on general, industry-wide exploit-code and patch-availability conditions, not "
                    "this organization's particular environment."
                ),
            },
            {
                "id": "d",
                "text": "Supplemental metric group",
                "correct": False,
                "rationale": (
                    "Incorrect. The Supplemental metric group provides additional informational context (such as "
                    "Automatable or Safety) and does not modify the numeric CVSS score at all, so it could not "
                    "account for the score changing from 8.1 to 9.3."
                ),
            },
        ],
        "explanation": (
            "CVSS Base scores reflect fixed, intrinsic vulnerability characteristics and remain constant. Temporal "
            "metrics are the group specifically designed to capture how real-world factors — exploit maturity and "
            "remediation availability — evolve after disclosure, which is exactly what changed in this scenario."
        ),
    },
    {
        "id": "nd4e-039",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "Select TWO factors, beyond the CVSS base score alone, that a mature vulnerability management program "
            "should incorporate when prioritizing remediation order."
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Whether active, in-the-wild exploitation of the vulnerability has been observed or the CVE "
                    "appears in a known-exploited-vulnerabilities catalog"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Confirmed active exploitation is one of the strongest real-world risk indicators "
                    "and should elevate remediation priority regardless of the CVSS base score alone."
                ),
            },
            {
                "id": "b",
                "text": "The business criticality and data sensitivity of the specific asset where the vulnerability was found",
                "correct": True,
                "rationale": (
                    "Correct. The same vulnerability poses very different real-world risk depending on whether it "
                    "sits on a mission-critical, sensitive-data-holding system or an isolated, low-value asset — "
                    "asset context is essential to sound prioritization."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The total number of vulnerabilities found on a given host, regardless of any individual "
                    "vulnerability's severity or exploitability"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Sheer finding count is a misleading prioritization metric — a host with fifty "
                    "low-severity findings is not necessarily higher risk than one with a single actively "
                    "exploited critical vulnerability; a mature program prioritizes by severity and "
                    "exploitability, not volume."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Whether the vulnerability was discovered by an internal scan versus an external vendor's "
                    "scan, since external findings carry more regulatory weight regardless of severity"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The source performing the scan does not change the vulnerability's actual "
                    "exploitability or business risk; prioritizing by scan source rather than by risk factors is "
                    "not a sound remediation-ordering practice."
                ),
            },
        ],
        "explanation": (
            "Risk-based vulnerability prioritization goes beyond the static CVSS base score to weigh real-world "
            "exploitation activity and asset context (criticality/data sensitivity) — raw finding counts and the "
            "identity of the scanning source are not meaningful risk indicators on their own."
        ),
    },
    {
        "id": "nd4e-040",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Wireless security",
        "stem": (
            "During a critical business event, every wireless client on an entire office floor simultaneously "
            "loses connectivity to the corporate WLAN. Spectrum analysis shows a continuous, high-power burst of "
            "noise across the entire 2.4 GHz band, unrelated to any legitimate access point or client traffic, "
            "which stops the moment an unidentified device is removed from a nearby conference room. Which type "
            "of wireless attack does this describe, and how does it fundamentally differ from a deauthentication "
            "attack?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "RF jamming; it is a physical-layer denial-of-service attack that floods the frequency "
                    "spectrum with noise, whereas a deauthentication attack operates at the logical/management-"
                    "frame layer by spoofing legitimate 802.11 control frames to disconnect specific clients "
                    "without disrupting the RF spectrum itself"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Continuous, broadband noise across the entire band detected by spectrum analysis, "
                    "affecting every client simultaneously and stopping only when a physical device is removed, "
                    "is the signature of RF jamming — a physical-layer attack, fundamentally distinct from the "
                    "frame-spoofing mechanism of a deauthentication attack."
                ),
            },
            {
                "id": "b",
                "text": "Deauthentication attack",
                "correct": False,
                "rationale": (
                    "Incorrect. A deauthentication attack spoofs specific 802.11 management frames at the logical "
                    "layer; it would not produce continuous broadband RF noise across the entire spectrum as "
                    "detected by spectrum analysis, and it typically targets specific clients rather than every "
                    "client on a floor simultaneously via noise."
                ),
            },
            {
                "id": "c",
                "text": "Evil twin / rogue access point",
                "correct": False,
                "rationale": (
                    "Incorrect. An evil twin impersonates a legitimate AP's SSID to lure clients into connecting "
                    "to it; it would not cause a floor-wide loss of connectivity via a broadband RF noise floor "
                    "increase, which is a physical-layer symptom entirely unrelated to impersonation."
                ),
            },
            {
                "id": "d",
                "text": "WPS PIN brute-force attack",
                "correct": False,
                "rationale": (
                    "Incorrect. A WPS PIN brute-force attack targets a specific access point's WPS authentication "
                    "feature to recover credentials; it has no relationship to broadband RF noise or a floor-wide "
                    "connectivity outage."
                ),
            },
        ],
        "explanation": (
            "RF jamming is a physical-layer denial-of-service technique that disrupts the wireless medium itself, "
            "distinguishable from a deauthentication attack (which spoofs logical management frames against "
            "specific clients) by its broadband spectrum noise signature and floor-wide, indiscriminate impact."
        ),
    },
]

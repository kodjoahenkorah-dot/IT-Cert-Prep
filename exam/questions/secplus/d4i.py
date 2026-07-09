"""CompTIA Security+ SY0-701 practice questions — Domain 4 (Security Operations), file I."""

QUESTIONS = [
    {
        "id": "nd4i-001",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Access control models",
        "stem": (
            "A defense contractor's classified document repository enforces two fixed rules on every access "
            "attempt: a user may never read a document classified higher than their own clearance ('no read "
            "up'), and a user may never write content into a document classified lower than their own clearance "
            "('no write down'). These rules are set by a central security authority and cannot be altered by "
            "document owners or end users. Which access control model does this repository implement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Mandatory access control (MAC)",
                "correct": True,
                "rationale": (
                    "Correct. Fixed, centrally mandated clearance/classification rules that individual owners "
                    "and users cannot override — including confinement rules like 'no read up, no write down' "
                    "— are the defining characteristic of MAC."
                ),
            },
            {
                "id": "b",
                "text": "Discretionary access control (DAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. DAC lets the resource owner decide who gets access. This repository explicitly "
                    "removes that discretion — a central authority's fixed labels govern every decision."
                ),
            },
            {
                "id": "c",
                "text": "Role-based access control (RBAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. RBAC ties permissions to a user's assigned role. This scenario describes "
                    "clearance-versus-classification confinement rules, not role membership."
                ),
            },
            {
                "id": "d",
                "text": "Attribute-based access control (ABAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. ABAC evaluates a flexible combination of attributes through a policy engine. "
                    "The scenario describes a rigid, formally defined confidentiality lattice enforced by a "
                    "central authority — the textbook hallmark of MAC, not a general attribute policy engine."
                ),
            },
        ],
        "explanation": (
            "'No read up, no write down' confinement rules enforced centrally and immutably describe MAC. DAC "
            "would let owners decide; RBAC keys off role alone; ABAC uses a flexible policy engine rather than a "
            "fixed classification lattice."
        ),
    },
    {
        "id": "nd4i-002",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Access control models",
        "stem": (
            "Select TWO statements that accurately describe key trade-offs between discretionary access control "
            "(DAC) and mandatory access control (MAC) in an enterprise setting."
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "DAC delegates access decisions to the resource owner, reducing central administrative "
                    "burden but increasing the risk of inconsistent or excessive sharing."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Owner-level discretion is convenient and scales without central bottlenecks, but "
                    "it also removes centralized oversight, allowing access sprawl to go unchecked."
                ),
            },
            {
                "id": "b",
                "text": (
                    "MAC requires a central authority to define and maintain classification labels and "
                    "clearance levels, which adds administrative overhead but ensures consistent enforcement of "
                    "confidentiality policy."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Centralized label management is MAC's operational cost, and consistent, "
                    "unbypassable enforcement is its primary security benefit."
                ),
            },
            {
                "id": "c",
                "text": (
                    "DAC provides stronger confidentiality guarantees than MAC because resource owners "
                    "understand their own data's sensitivity best."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This reverses reality: MAC generally provides stronger, more consistent "
                    "confidentiality guarantees precisely because it removes sharing discretion from individual "
                    "owners, who may misjudge sensitivity or share carelessly."
                ),
            },
            {
                "id": "d",
                "text": (
                    "MAC allows any user to reclassify a document's sensitivity label at will to facilitate "
                    "faster collaboration."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. MAC explicitly forbids users from changing classification labels themselves — "
                    "that kind of owner-driven flexibility describes DAC, not MAC."
                ),
            },
        ],
        "explanation": (
            "DAC trades centralized consistency for administrative convenience; MAC trades administrative "
            "overhead for consistent, centrally enforced confidentiality. Neither statement reversing those "
            "trade-offs is accurate."
        ),
    },
    {
        "id": "nd4i-003",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Application security",
        "stem": (
            "An organization's internal Python package 'acme-auth-utils' is used by several internal "
            "applications but has never been published to the public PyPI registry. A build pipeline is "
            "configured to check the public registry for packages before falling back to the internal registry. "
            "An attacker publishes a malicious package with the identical name and a higher version number to "
            "PyPI. On the next build, the pipeline downloads and executes the attacker's package instead of the "
            "legitimate internal one. Which attack technique does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Dependency confusion",
                "correct": True,
                "rationale": (
                    "Correct. Dependency confusion exploits build tooling that checks a public registry before "
                    "(or instead of) a trusted private registry, letting an attacker 'win' resolution with a "
                    "same-named, higher-versioned malicious public package."
                ),
            },
            {
                "id": "b",
                "text": "Typosquatting",
                "correct": False,
                "rationale": (
                    "Incorrect. Typosquatting relies on a deliberately misspelled or similar-looking package "
                    "name to trick a developer into a manual typo. Here the attacker used the exact same name, "
                    "exploiting resolution order rather than a typing mistake."
                ),
            },
            {
                "id": "c",
                "text": "Cross-site request forgery (CSRF)",
                "correct": False,
                "rationale": (
                    "Incorrect. CSRF tricks an authenticated browser into submitting an unwanted request to a "
                    "web application. This scenario involves a build pipeline resolving a software package, not "
                    "a browser session."
                ),
            },
            {
                "id": "d",
                "text": "Server-side request forgery (SSRF)",
                "correct": False,
                "rationale": (
                    "Incorrect. SSRF tricks a server into making an unintended request on an attacker's behalf, "
                    "typically to reach internal resources. This scenario is about package resolution priority "
                    "during a build, not a server issuing an attacker-directed request."
                ),
            },
        ],
        "explanation": (
            "Dependency confusion abuses a build/package manager's default preference for a public registry "
            "over an internal one, letting an attacker supply a same-named malicious package that gets pulled "
            "and executed automatically."
        ),
    },
    {
        "id": "nd4i-004",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Application security",
        "stem": (
            "A web application's UI hides the 'Delete User' button for anyone logged in without an "
            "administrator role. A tester logs in as a standard user, captures the underlying "
            "'DELETE /api/users/{id}' request another user's browser would send, replays it directly against "
            "the API with their own standard-user session token, and successfully deletes another employee's "
            "account. Server-side code never checks the caller's role before executing the deletion. Which "
            "vulnerability class does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Broken function-level authorization",
                "correct": True,
                "rationale": (
                    "Correct. The application relies on the UI to hide an administrative function instead of "
                    "enforcing the role check on the server for that specific API function, letting any "
                    "authenticated user invoke it directly."
                ),
            },
            {
                "id": "b",
                "text": "Insecure direct object reference (IDOR)",
                "correct": False,
                "rationale": (
                    "Incorrect. IDOR involves accessing or modifying a specific object (like another user's "
                    "record) that you shouldn't own, based purely on manipulating an identifier. Here the "
                    "problem is that the caller could invoke an administrative function at all, regardless of "
                    "which object ID was targeted."
                ),
            },
            {
                "id": "c",
                "text": "Mass assignment",
                "correct": False,
                "rationale": (
                    "Incorrect. Mass assignment occurs when an API blindly binds every field in a client-"
                    "supplied request body to an object's attributes, letting an attacker set unintended fields "
                    "(like a role flag). This scenario involves invoking a restricted delete endpoint, not "
                    "injecting extra fields into a request body."
                ),
            },
            {
                "id": "d",
                "text": "Cross-site scripting (XSS)",
                "correct": False,
                "rationale": (
                    "Incorrect. XSS involves injecting malicious script into a page rendered for other users. "
                    "No script injection or output rendering issue is described here."
                ),
            },
        ],
        "explanation": (
            "When a UI conceals a privileged action but the server never independently verifies the caller's "
            "authorization for that specific function, the result is broken function-level authorization — a "
            "distinct flaw from object-level (IDOR) or field-injection (mass assignment) issues."
        ),
    },
    {
        "id": "nd4i-005",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Application security",
        "stem": (
            "A web application's 'generate report' feature lets a user supply a custom greeting template that "
            "is rendered server-side by a templating engine before being inserted into a PDF report. A tester "
            "submits '{{7*7}}' as the greeting text and observes the literal value '49' rendered in the output "
            "report, confirming that expressions are being evaluated rather than displayed as plain text. Which "
            "vulnerability does this behavior indicate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Server-side template injection (SSTI)",
                "correct": True,
                "rationale": (
                    "Correct. Getting the engine to evaluate an arbitrary expression like '7*7' and return the "
                    "computed result is the classic proof-of-concept for SSTI, which can often be escalated to "
                    "remote code execution via the template engine's built-in objects."
                ),
            },
            {
                "id": "b",
                "text": "Reflected cross-site scripting (XSS)",
                "correct": False,
                "rationale": (
                    "Incorrect. Reflected XSS would execute attacker-supplied JavaScript in a victim's browser. "
                    "Here, the input is evaluated as a template expression on the server and returned as '49' "
                    "inside a generated report, not as executed client-side script."
                ),
            },
            {
                "id": "c",
                "text": "SQL injection",
                "correct": False,
                "rationale": (
                    "Incorrect. No database query or SQL syntax is involved; the input is being evaluated by a "
                    "server-side templating engine, not passed into a SQL statement."
                ),
            },
            {
                "id": "d",
                "text": "Insecure deserialization",
                "correct": False,
                "rationale": (
                    "Incorrect. Insecure deserialization involves reconstructing an object from untrusted "
                    "serialized data (such as a Java or .NET object stream), not evaluating a template "
                    "expression syntax embedded in plain text input."
                ),
            },
        ],
        "explanation": (
            "A template expression like '{{7*7}}' being evaluated to '49' by the server is the textbook "
            "confirmation technique for server-side template injection, distinct from XSS (client-side), SQLi "
            "(database), or deserialization (object reconstruction) vulnerabilities."
        ),
    },
    {
        "id": "nd4i-006",
        "domain": 4,
        "objective": "4.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Asset management",
        "stem": (
            "An asset audit finds 15 network switches deployed at remote branch offices that were purchased "
            "directly with department credit cards, bypassing IT procurement entirely. None of the switches "
            "were ever entered into the CMDB, and all still run unpatched firmware with default administrative "
            "credentials because IT was unaware the devices existed. Which asset management practice would BEST "
            "have prevented this gap?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A formal procurement policy requiring all technology purchases to route through IT so "
                    "every asset is recorded in the CMDB at the time of acquisition"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Enforcing procurement through IT closes the gap at its source — assets never "
                    "become invisible in the first place because they're recorded and configured to a secure "
                    "baseline before deployment."
                ),
            },
            {
                "id": "b",
                "text": "Deploying network access control (NAC) to detect unmanaged devices as they connect",
                "correct": False,
                "rationale": (
                    "Incorrect. NAC is a valuable detective control but only catches unmanaged assets after "
                    "they're already deployed and connected — it doesn't prevent the underlying procurement "
                    "gap that let them bypass inventory in the first place."
                ),
            },
            {
                "id": "c",
                "text": "Running a monthly authenticated vulnerability scan against all known IP ranges",
                "correct": False,
                "rationale": (
                    "Incorrect. A scan can only assess assets it knows to target; it is a reactive, after-the-"
                    "fact control that doesn't address why these switches were never entered into inventory."
                ),
            },
            {
                "id": "d",
                "text": "Enabling automatic firmware updates on all switches once they are discovered",
                "correct": False,
                "rationale": (
                    "Incorrect. Automatic updates only help once a device is known and managed; they do nothing "
                    "to prevent unauthorized purchases from going unrecorded in the first place."
                ),
            },
        ],
        "explanation": (
            "The root cause is a gap at the acquisition stage of the asset lifecycle. NAC, scanning, and "
            "patching are all valuable but reactive controls that only help after an unmanaged device is "
            "already deployed; only a procurement policy prevents the blind spot from forming."
        ),
    },
    {
        "id": "nd4i-007",
        "domain": 4,
        "objective": "4.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Asset management",
        "stem": (
            "A software asset management (SAM) review finds the organization owns 500 licenses for a database "
            "product but has 800 active, running instances. The sprawl occurred because the licensed database "
            "software was pre-installed in the organization's golden VM template, so every new VM cloned from "
            "that template silently created another licensed instance with no purchasing or approval step "
            "involved. Which practice would BEST prevent this type of licensing exposure going forward?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Governing golden image content so licensed software is excluded from base templates and "
                    "instead installed only through a tracked provisioning step that reconciles against "
                    "available license entitlements"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Removing the licensed software from the template — and requiring its install to "
                    "go through a step that checks entitlement counts — prevents every clone from silently "
                    "becoming an unlicensed instance."
                ),
            },
            {
                "id": "b",
                "text": "Purchasing additional licenses to cover the 300-instance overage after the fact",
                "correct": False,
                "rationale": (
                    "Incorrect. Buying more licenses resolves this specific compliance gap retroactively but "
                    "does nothing to stop the template from continuing to spawn new unlicensed instances with "
                    "every future clone."
                ),
            },
            {
                "id": "c",
                "text": "Increasing the frequency of the CMDB's automated hardware discovery scans",
                "correct": False,
                "rationale": (
                    "Incorrect. Hardware discovery scans would help detect the drift sooner, but the root cause "
                    "is a software provisioning practice, not a lack of visibility that faster hardware scans "
                    "would fix."
                ),
            },
            {
                "id": "d",
                "text": "Restricting VM cloning permissions to senior infrastructure engineers only",
                "correct": False,
                "rationale": (
                    "Incorrect. Restricting who can clone VMs reduces the volume of new instances but doesn't "
                    "address the underlying issue that the template itself embeds licensed software without "
                    "any entitlement tracking."
                ),
            },
        ],
        "explanation": (
            "The sprawl originates from licensed software baked into a cloning template with no entitlement "
            "check. The durable fix is governing what golden images contain and tying licensed-software "
            "installation to entitlement tracking, not merely buying more licenses or restricting who can clone."
        ),
    },
    {
        "id": "nd4i-008",
        "domain": 4,
        "objective": "4.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Automation & orchestration",
        "stem": (
            "A SOAR playbook disables a user's account whenever a specific SIEM alert fires. Due to a "
            "misconfigured log forwarder, the same underlying alert is occasionally delivered to the SOAR "
            "platform twice within a few seconds. The first playbook run disables the account successfully; the "
            "second run, finding the account already disabled, throws an unhandled error and pages the on-call "
            "engineer at 3 a.m. for an event that was already fully remediated. Which design flaw in the "
            "playbook is MOST directly responsible for the unnecessary page?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The playbook lacks idempotency handling — it does not check current state before acting "
                    "and cannot gracefully handle being triggered more than once for the same event"
                ),
                "correct": True,
                "rationale": (
                    "Correct. An idempotent playbook would check whether the account was already disabled and "
                    "exit cleanly (or simply confirm the desired end state), rather than treating a duplicate "
                    "trigger as an unhandled failure requiring human paging."
                ),
            },
            {
                "id": "b",
                "text": "The playbook uses an overly broad service account with excessive privileges",
                "correct": False,
                "rationale": (
                    "Incorrect. Overprivileged service accounts are a real SOAR governance risk, but they don't "
                    "explain why a duplicate trigger produces an unhandled error and unnecessary page — that's "
                    "purely a state-handling/idempotency gap."
                ),
            },
            {
                "id": "c",
                "text": "The SIEM correlation rule generating the alert is too broadly scoped",
                "correct": False,
                "rationale": (
                    "Incorrect. The rule correctly identified a real event once; the problem described is that "
                    "a duplicate delivery of the same alert crashes the playbook, not that the rule fires on "
                    "irrelevant activity."
                ),
            },
            {
                "id": "d",
                "text": "The playbook was never tested in a staging environment before production deployment",
                "correct": False,
                "rationale": (
                    "Incorrect. Pre-production testing is good practice generally, but the specific failure "
                    "mode described — inability to handle a duplicate trigger for the same account — is an "
                    "idempotency gap that testing may or may not have caught, and is not what the scenario "
                    "identifies as the direct cause."
                ),
            },
        ],
        "explanation": (
            "Automation that performs a state-changing action should check current state or handle re-execution "
            "gracefully. Without idempotency, duplicate or retried triggers cause unnecessary failures and "
            "alert fatigue rather than safely converging on the same end state."
        ),
    },
    {
        "id": "nd4i-009",
        "domain": 4,
        "objective": "4.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Automation & orchestration",
        "stem": (
            "An automated response playbook revokes cloud API keys the moment a threat-intelligence feed flags "
            "the associated source IP as 'malicious infrastructure,' with no additional verification step. "
            "During a scheduled vulnerability scan, the organization's own external scanning service is briefly "
            "flagged by the same feed due to a stale reputation entry, and the playbook immediately revokes the "
            "scanner's API key mid-scan, causing the scan to fail. Which change would BEST prevent this type of "
            "recurrence without eliminating the speed benefit of automated response?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Maintain an allow-list of known-internal infrastructure (such as the organization's own "
                    "scanners) that the playbook checks before taking automated action on a threat-intel match"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Cross-referencing a threat-intel hit against known internal assets before acting "
                    "lets the playbook keep responding automatically to genuine external threats while "
                    "avoiding self-inflicted disruption from stale or erroneous feed entries."
                ),
            },
            {
                "id": "b",
                "text": "Remove the threat-intelligence feed from the playbook entirely and rely on manual review of every alert",
                "correct": False,
                "rationale": (
                    "Incorrect. Eliminating automation altogether sacrifices the speed benefit the playbook "
                    "exists to provide and doesn't scale; the goal is to fix the false-positive handling, not "
                    "abandon automated response."
                ),
            },
            {
                "id": "c",
                "text": "Increase the frequency at which the threat-intelligence feed is polled for updates",
                "correct": False,
                "rationale": (
                    "Incorrect. Polling more often doesn't address a stale or erroneous reputation entry; it "
                    "could even cause the playbook to act on bad data faster, not more accurately."
                ),
            },
            {
                "id": "d",
                "text": "Schedule the vulnerability scan to run only during business hours going forward",
                "correct": False,
                "rationale": (
                    "Incorrect. Rescheduling the scan doesn't fix the underlying automation flaw — the "
                    "playbook would still revoke keys for any legitimate internal asset a feed mistakenly "
                    "flags, regardless of when the scan happens to run."
                ),
            },
        ],
        "explanation": (
            "Fully automated, high-impact actions driven by external threat-intel data need a safeguard against "
            "false positives on known internal infrastructure — an allow-list check preserves speed for real "
            "threats while preventing self-inflicted outages from feed errors."
        ),
    },
    {
        "id": "nd4i-010",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Digital forensics",
        "stem": (
            "Before deploying a newly purchased hardware write-blocker for use in investigations, a forensic "
            "lab connects it to a set of reference source drives with known, previously recorded hash values, "
            "attempts both read and write operations through it, and confirms the device passes reads through "
            "unmodified while blocking every write attempt, with the resulting acquisition hash matching the "
            "known reference value. Which forensic principle does this practice MOST directly demonstrate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Validation of forensic tools before use to ensure sound, defensible evidence acquisition",
                "correct": True,
                "rationale": (
                    "Correct. Verifying a tool performs as expected against known reference media, before it "
                    "touches real evidence, is exactly how forensic labs establish that a tool is reliable and "
                    "the resulting acquisitions will hold up to scrutiny."
                ),
            },
            {
                "id": "b",
                "text": "Order of volatility, since the most volatile data is collected first",
                "correct": False,
                "rationale": (
                    "Incorrect. Order of volatility governs the sequence in which live evidence types are "
                    "collected during an active response, not the pre-use validation of an acquisition tool "
                    "against reference media."
                ),
            },
            {
                "id": "c",
                "text": "Legal hold, since the reference drives are being preserved for litigation",
                "correct": False,
                "rationale": (
                    "Incorrect. Legal hold is a notice obligation to preserve potentially relevant data for "
                    "anticipated litigation. Testing a write-blocker's reliability has no connection to a legal "
                    "hold notice."
                ),
            },
            {
                "id": "d",
                "text": "Chain of custody, since the write-blocker's serial number is being logged",
                "correct": False,
                "rationale": (
                    "Incorrect. Chain of custody tracks who has handled a specific piece of evidence over time. "
                    "This scenario describes validating that a tool works correctly before it is ever used on "
                    "actual case evidence, not documenting evidence handoffs."
                ),
            },
        ],
        "explanation": (
            "Confirming a forensic tool behaves as expected against known reference media before relying on it "
            "for real acquisitions is tool/process validation — a prerequisite for forensically sound evidence "
            "that is distinct from volatility ordering, legal hold, or chain of custody."
        ),
    },
    {
        "id": "nd4i-011",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Digital forensics",
        "stem": (
            "A decade-old internal forensic SOP requires examiners to generate an MD5 hash of every acquired "
            "disk image to prove its integrity. During a recent case, defense counsel successfully challenges "
            "the image's integrity by citing publicly known MD5 collision techniques that can produce two "
            "different files sharing the same hash. Which change to the SOP would BEST address this weakness in "
            "future investigations?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Require a collision-resistant algorithm such as SHA-256 to generate the integrity hash",
                "correct": True,
                "rationale": (
                    "Correct. SHA-256 has no known practical collision attack, so it provides a far stronger "
                    "integrity guarantee than MD5 and directly closes the specific weakness counsel exploited."
                ),
            },
            {
                "id": "b",
                "text": "Switch to CRC32 checksums, which compute faster than MD5",
                "correct": False,
                "rationale": (
                    "Incorrect. CRC32 is an error-detection checksum, not a cryptographic hash, and is far more "
                    "susceptible to collisions than even MD5 — this would make the integrity weakness worse, "
                    "not better."
                ),
            },
            {
                "id": "c",
                "text": "Stop hashing acquired images, since defense counsel can challenge any hash algorithm",
                "correct": False,
                "rationale": (
                    "Incorrect. Removing integrity hashing entirely eliminates any cryptographic proof the "
                    "image is unaltered, which is far more damaging to admissibility than using a modern, "
                    "collision-resistant algorithm."
                ),
            },
            {
                "id": "d",
                "text": "Compute the MD5 hash twice and average the results for redundancy",
                "correct": False,
                "rationale": (
                    "Incorrect. Running the same weak algorithm twice does not address its underlying "
                    "collision vulnerability; 'averaging' hash values is also not a meaningful or valid "
                    "operation."
                ),
            },
        ],
        "explanation": (
            "MD5's known collision weaknesses make it a poor choice for evidence integrity in litigation-facing "
            "work; adopting a collision-resistant algorithm like SHA-256 directly addresses the specific "
            "challenge raised, unlike weaker checksums, no hashing at all, or repeating the same weak algorithm."
        ),
    },
    {
        "id": "nd4i-012",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Digital forensics and chain-of-custody process",
        "stem": (
            "An investigation into a cyberattack traces command-and-control infrastructure to servers hosted in "
            "a data center located in another country. Obtaining the log and disk evidence from that data "
            "center requires cooperation from a foreign cloud provider and, potentially, the foreign "
            "government. Compared to a purely domestic investigation, which factor introduces the GREATEST "
            "additional challenge to maintaining a verifiable, unbroken chain of custody for this evidence?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Differing international legal and jurisdictional requirements governing how evidence must "
                    "be requested, handled, and transferred, potentially requiring formal mutual legal "
                    "assistance processes"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Cross-border evidence collection is governed by the laws of the country where the "
                    "data resides, often requiring formal government-to-government legal assistance requests; "
                    "reconciling those requirements with a defensible custody trail is the primary added "
                    "challenge."
                ),
            },
            {
                "id": "b",
                "text": "The additional network latency involved in transferring large evidence files internationally",
                "correct": False,
                "rationale": (
                    "Incorrect. Latency is an operational inconvenience affecting transfer speed, not a factor "
                    "that meaningfully threatens the legal integrity or admissibility of the chain of custody."
                ),
            },
            {
                "id": "c",
                "text": "The increased storage cost of retaining evidence acquired from a foreign data center",
                "correct": False,
                "rationale": (
                    "Incorrect. Storage cost is a budgetary consideration with no direct bearing on whether "
                    "custody of the evidence can be proven unbroken and defensible."
                ),
            },
            {
                "id": "d",
                "text": "Time zone differences alone complicating accurate timestamp logging on custody forms",
                "correct": False,
                "rationale": (
                    "Incorrect. Time zone handling is a real but comparatively minor logistical detail (easily "
                    "solved by standardizing on UTC); it does not rise to the level of the jurisdictional and "
                    "legal-process challenges involved in obtaining and lawfully transferring foreign-held "
                    "evidence."
                ),
            },
        ],
        "explanation": (
            "Cross-border evidence introduces jurisdictional and legal-process complexity — differing laws on "
            "data handling and required formal assistance channels — that dwarfs the comparatively minor "
            "logistical issues of latency, cost, or time zone bookkeeping."
        ),
    },
    {
        "id": "nd4i-013",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Digital forensics and chain-of-custody process",
        "stem": (
            "A civil litigation matter involving seized digital evidence reaches a final verdict, and all "
            "appeal periods expire. The organization's evidence-handling policy requires the evidence to be "
            "securely destroyed rather than returned. Which action MOST directly and properly closes out the "
            "chain-of-custody record for this evidence?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Formally documenting the final disposition — method, date, and authorizing party for the "
                    "destruction — directly on the chain-of-custody record"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A complete chain of custody must account for evidence from initial seizure "
                    "through its ultimate fate; recording the authorized destruction with date and method "
                    "closes the record with the same rigor used for every prior handoff."
                ),
            },
            {
                "id": "b",
                "text": "Deleting the case file from the evidence management system once the verdict is entered",
                "correct": False,
                "rationale": (
                    "Incorrect. Deleting the record destroys the very documentation that proves proper handling "
                    "occurred throughout the case, and provides no defensible proof of the evidence's final "
                    "disposition if ever challenged later."
                ),
            },
            {
                "id": "c",
                "text": "Verbally notifying the evidence custodian that the case is closed, without written documentation",
                "correct": False,
                "rationale": (
                    "Incorrect. Undocumented verbal notification leaves no auditable record, which defeats the "
                    "purpose of a chain-of-custody process that must withstand scrutiny even after a case ends."
                ),
            },
            {
                "id": "d",
                "text": "No further action is required once a final verdict has been reached",
                "correct": False,
                "rationale": (
                    "Incorrect. A verdict does not automatically account for what happens to the physical or "
                    "digital evidence afterward; disposition still must be authorized, executed, and formally "
                    "documented."
                ),
            },
        ],
        "explanation": (
            "Chain of custody must remain unbroken through final disposition, not just through trial. Whether "
            "evidence is destroyed, returned, or archived, that final action needs the same authorized, dated, "
            "documented record as every earlier transfer."
        ),
    },
    {
        "id": "nd4i-014",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "EDR/XDR & DLP",
        "stem": (
            "A DLP policy successfully blocks a user from emailing a spreadsheet of customer PII as an "
            "attachment. The same user then successfully exfiltrates the identical data by copying the cell "
            "values directly out of the spreadsheet and pasting them as plain text into the body of a personal "
            "webmail compose window, which is not blocked. Which DLP capability gap MOST directly explains why "
            "the second attempt succeeded?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The organization only deployed network/email-attachment DLP inspection and lacks endpoint-"
                    "based DLP that monitors content copied into browser forms and the clipboard"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Attachment-scanning DLP inspects files leaving through email, but pasted plain "
                    "text typed or pasted into a webmail compose box is a different data path entirely — "
                    "closing that gap requires endpoint DLP that watches clipboard and browser-input activity."
                ),
            },
            {
                "id": "b",
                "text": "The DLP solution lacks optical character recognition (OCR) to read text inside images",
                "correct": False,
                "rationale": (
                    "Incorrect. No image was involved in the second attempt — the data was pasted as plain "
                    "text, so an OCR capability gap is irrelevant to this specific bypass."
                ),
            },
            {
                "id": "c",
                "text": "The customer PII was not encrypted at rest in the original spreadsheet",
                "correct": False,
                "rationale": (
                    "Incorrect. Encryption at rest protects stored data from unauthorized access; it has no "
                    "bearing on whether a user who is already authorized to open the file can copy its visible "
                    "contents elsewhere."
                ),
            },
            {
                "id": "d",
                "text": "The DLP policy's regular-expression pattern for detecting PII was configured incorrectly",
                "correct": False,
                "rationale": (
                    "Incorrect. The same PII pattern that blocked the attachment would still match the "
                    "identical values pasted as plain text; the problem is that no DLP inspection point existed "
                    "for the clipboard/webmail-body channel at all, not that the pattern itself failed to match."
                ),
            },
        ],
        "explanation": (
            "Content-aware DLP must cover every channel data can leave through. Blocking file attachments while "
            "leaving clipboard-to-webmail pasting uninspected leaves a channel-level gap, not a pattern-"
            "matching or encryption problem."
        ),
    },
    {
        "id": "nd4i-015",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "EDR/XDR & DLP",
        "stem": (
            "An organization's XDR platform ingests telemetry from EDR, the email security gateway, the "
            "identity provider, and a CASB. During an investigation, the platform automatically links a "
            "phishing-email-open event, a subsequent risky sign-in from an unfamiliar country, and an anomalous "
            "mass file-download from cloud storage — all tied to the same user — into a single incident "
            "timeline within minutes, work that previously required analysts to manually cross-reference four "
            "separate consoles. Which XDR capability is BEST illustrated?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Cross-domain telemetry correlation that unifies detections from previously siloed tools into one incident view",
                "correct": True,
                "rationale": (
                    "Correct. Automatically stitching related events from email, identity, endpoint, and cloud "
                    "sources into a single coherent timeline — rather than requiring an analyst to manually "
                    "correlate across separate consoles — is XDR's defining value over standalone tools."
                ),
            },
            {
                "id": "b",
                "text": "Signature-based antivirus detection of a known malicious file hash",
                "correct": False,
                "rationale": (
                    "Incorrect. No file hash or signature match is described; the scenario is about linking "
                    "behavioral events across different tools, not identifying a known-bad file."
                ),
            },
            {
                "id": "c",
                "text": "SOAR-driven automated remediation that revokes the compromised user's access",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario describes detection and correlation into a timeline, not an "
                    "automated remediation action being taken against the account."
                ),
            },
            {
                "id": "d",
                "text": "Proactive, hypothesis-driven threat hunting performed by an analyst",
                "correct": False,
                "rationale": (
                    "Incorrect. Threat hunting is analyst-initiated and hypothesis-driven; this scenario "
                    "describes the platform automatically correlating existing telemetry into an incident, not "
                    "a human proactively searching for unknown threats."
                ),
            },
        ],
        "explanation": (
            "XDR's core value proposition is automatic correlation of telemetry across previously siloed "
            "security tools into a unified incident, distinct from signature detection, automated remediation, "
            "or analyst-driven threat hunting."
        ),
    },
    {
        "id": "nd4i-016",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Email security (SPF/DKIM/DMARC)",
        "stem": (
            "A company's SPF record reads 'v=spf1 include:_spf.google.com include:mailgun.org +all'. A "
            "phishing simulation confirms that spoofed emails claiming to originate from the company's domain, "
            "sent from a mail server never listed in the SPF record, still pass SPF validation at the receiving "
            "server. Which part of this SPF record explains the result?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The trailing '+all' qualifier, which explicitly passes SPF for any sending server, "
                    "including ones not listed in the record"
                ),
                "correct": True,
                "rationale": (
                    "Correct. '+all' is the explicit 'pass' qualifier — it tells receiving servers that literally "
                    "any source is authorized, which functionally neutralizes the protection the 'include' "
                    "mechanisms were meant to provide."
                ),
            },
            {
                "id": "b",
                "text": "The record contains too many 'include' mechanisms, exceeding the 10-lookup limit and causing a permerror",
                "correct": False,
                "rationale": (
                    "Incorrect. Two include mechanisms are far below the 10-DNS-lookup limit, and a permerror "
                    "result would typically cause validation to fail or be treated as neutral — not cause "
                    "unauthorized senders to pass."
                ),
            },
            {
                "id": "c",
                "text": "The DKIM signature on the spoofed messages is invalid",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario describes SPF validation specifically passing; it says nothing "
                    "about DKIM, which is an entirely separate authentication mechanism."
                ),
            },
            {
                "id": "d",
                "text": "The domain is missing an MX record, so SPF checks default to passing",
                "correct": False,
                "rationale": (
                    "Incorrect. SPF validation does not depend on the presence of an MX record, and there is no "
                    "such 'default to pass' behavior tied to a missing MX record."
                ),
            },
        ],
        "explanation": (
            "SPF's 'all' mechanism qualifier controls what happens for senders not matched by earlier "
            "mechanisms: '-all' hard-fails them, '~all' soft-fails them, and '+all' explicitly passes them — "
            "which is what let an unauthorized server spoof the domain and still pass SPF."
        ),
    },
    {
        "id": "nd4i-017",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Email security (SPF/DKIM/DMARC)",
        "stem": (
            "A company's outbound marketing email is relayed through a third-party ESP whose sending IP address "
            "is NOT listed in the company's SPF record, so SPF fails for these messages. However, the ESP DKIM-"
            "signs every message using a selector delegated by the company, and the signing domain exactly "
            "matches the company's domain in the visible 'From' header. DMARC is published as 'v=DMARC1; "
            "p=reject; adkim=s; aspf=s'. What is the MOST likely outcome for these messages at receiving mail "
            "servers that enforce DMARC?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The messages pass DMARC because DKIM alignment succeeds under strict alignment, and DMARC "
                    "only requires ONE of SPF or DKIM to align — not both"
                ),
                "correct": True,
                "rationale": (
                    "Correct. DMARC evaluates SPF and DKIM independently and passes if either one aligns with "
                    "the visible From domain. Here DKIM aligns under strict mode even though SPF fails, so the "
                    "messages pass DMARC despite the SPF failure."
                ),
            },
            {
                "id": "b",
                "text": "The messages are rejected because DMARC requires both SPF and DKIM to pass and align",
                "correct": False,
                "rationale": (
                    "Incorrect. This is a common misconception — DMARC compliance requires alignment from at "
                    "least one of SPF or DKIM, not both simultaneously. Since DKIM aligns here, the messages "
                    "still pass despite the SPF failure."
                ),
            },
            {
                "id": "c",
                "text": "The messages pass because 'aspf=s' forces SPF to succeed regardless of the sending IP",
                "correct": False,
                "rationale": (
                    "Incorrect. The 'aspf' tag only controls how strictly the SPF domain must align with the "
                    "From header when SPF does pass — it cannot force a failed SPF check to succeed."
                ),
            },
            {
                "id": "d",
                "text": "The messages are quarantined due to achieving only partial SPF/DKIM alignment",
                "correct": False,
                "rationale": (
                    "Incorrect. DMARC evaluation is binary per mechanism (each of SPF and DKIM either aligns or "
                    "doesn't); there is no 'partial alignment' quarantine outcome. Since DKIM fully aligns, the "
                    "policy result is a pass, not a quarantine."
                ),
            },
        ],
        "explanation": (
            "DMARC passes a message if either SPF or DKIM authenticates and aligns with the visible From "
            "domain. A relayed message can fail SPF (wrong sending IP) yet still pass DMARC entirely on the "
            "strength of an aligned DKIM signature."
        ),
    },
    {
        "id": "nd4i-018",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Federation & SSO (SAML/OAuth)",
        "stem": (
            "During a post-breach investigation, analysts discover that an attacker who compromised an on-"
            "premises federation server extracted the private key used to digitally sign SAML assertions. Using "
            "that key, the attacker forged SAML assertions claiming to represent any user of their choosing — "
            "including accounts that never actually authenticated — and used the forged assertions to access "
            "cloud SaaS applications without ever supplying the victims' actual passwords or MFA. Which attack "
            "technique does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Golden SAML — forging trusted SAML assertions with a stolen IdP signing key to impersonate any user",
                "correct": True,
                "rationale": (
                    "Correct. Golden SAML is exactly this technique: once an attacker holds the federation "
                    "server's signing key, they can mint fully trusted assertions for any identity, bypassing "
                    "the actual authentication and MFA steps entirely."
                ),
            },
            {
                "id": "b",
                "text": "Pass-the-hash, using a captured NTLM password hash to authenticate without the plaintext password",
                "correct": False,
                "rationale": (
                    "Incorrect. Pass-the-hash is an NTLM-specific credential-reuse technique against Windows "
                    "authentication. This scenario involves forging cryptographically signed SAML assertions, "
                    "not replaying an NTLM hash."
                ),
            },
            {
                "id": "c",
                "text": "OAuth consent phishing, tricking a user into granting a malicious app excessive scopes",
                "correct": False,
                "rationale": (
                    "Incorrect. Consent phishing requires tricking a victim into approving a malicious "
                    "application's permission request. No user interaction or consent grant occurred here — the "
                    "attacker fabricated assertions entirely offline using the stolen key."
                ),
            },
            {
                "id": "d",
                "text": "Session token replay, reusing a previously issued valid browser session cookie",
                "correct": False,
                "rationale": (
                    "Incorrect. Token replay reuses an existing, already-issued token or cookie. Here the "
                    "attacker manufactured brand-new, never-before-issued assertions for arbitrary identities "
                    "using the stolen signing key, rather than replaying a captured token."
                ),
            },
        ],
        "explanation": (
            "Golden SAML specifically describes forging arbitrary, validly signed SAML assertions after "
            "stealing an identity provider's signing key — a far more powerful and stealthy attack than "
            "credential theft, hash replay, or consent phishing, since it needs no victim credentials at all."
        ),
    },
    {
        "id": "nd4i-019",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Federation & SSO (SAML/OAuth)",
        "stem": (
            "Select TWO statements that correctly describe the protection OAuth 2.0 Proof Key for Code Exchange "
            "(PKCE) provides."
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "PKCE protects public clients, such as mobile or single-page apps, that cannot securely "
                    "store a client secret, by binding the authorization code to a dynamically generated "
                    "verifier known only to the requesting client instance"
                ),
                "correct": True,
                "rationale": (
                    "Correct. PKCE was designed specifically for clients that cannot keep a secret confidential; "
                    "it replaces the static secret with a per-request, dynamically generated code verifier."
                ),
            },
            {
                "id": "b",
                "text": (
                    "PKCE prevents an attacker who intercepts the authorization code — for example via a "
                    "maliciously registered custom URL scheme — from exchanging it for tokens, because the "
                    "attacker cannot produce the matching code verifier"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Even if the authorization code itself is intercepted, the token endpoint requires "
                    "the original code verifier to complete the exchange, which an intercepting attacker never "
                    "possesses."
                ),
            },
            {
                "id": "c",
                "text": "PKCE eliminates the need for the authorization server to validate the redirect_uri against a pre-registered value",
                "correct": False,
                "rationale": (
                    "Incorrect. PKCE and redirect_uri validation are independent, complementary protections; "
                    "PKCE does not replace or eliminate the requirement to validate the redirect_uri."
                ),
            },
            {
                "id": "d",
                "text": "PKCE is required only for confidential clients that already securely store a client secret",
                "correct": False,
                "rationale": (
                    "Incorrect. This reverses PKCE's purpose — it was created specifically for public clients "
                    "that cannot securely hold a secret, though modern best practice now recommends it broadly."
                ),
            },
        ],
        "explanation": (
            "PKCE binds the authorization code exchange to a per-request secret the legitimate client generates "
            "itself, closing the interception gap for public clients — it does not replace redirect_uri "
            "validation and is aimed at clients that cannot hold a static secret, not the reverse."
        ),
    },
    {
        "id": "nd4i-020",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Hardening & secure baselines",
        "stem": (
            "A security team hardens 5,000 domain-joined Windows workstations by pushing a single Group Policy "
            "Object (GPO) that disables SMBv1, the built-in Guest account, and LLMNR/NBT-NS name resolution "
            "fleet-wide. Three months later, a compliance scan finds that 40 workstations still have all three "
            "vulnerable defaults active — every one of them was offline or disconnected from the domain during "
            "the original GPO rollout window. Which action would BEST ensure ALL workstations, including "
            "intermittently connected ones, receive and maintain the hardened baseline going forward?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Ensure the GPO enforces and refreshes the baseline automatically at each policy refresh "
                    "interval and system startup, and validate ongoing compliance with periodic automated "
                    "scanning rather than relying on a single push"
                ),
                "correct": True,
                "rationale": (
                    "Correct. GPOs re-apply automatically whenever a machine reconnects and refreshes policy, "
                    "so any device that was offline during the initial push still receives the baseline the "
                    "next time it checks in — paired with periodic scanning to catch stragglers, this closes "
                    "the gap systemically rather than one time."
                ),
            },
            {
                "id": "b",
                "text": "Manually reconfigure the 40 affected workstations one time to match the current baseline",
                "correct": False,
                "rationale": (
                    "Incorrect. A one-time manual fix resolves today's 40 machines but does nothing to prevent "
                    "the same gap from recurring the next time a device is offline during a future policy "
                    "rollout — it treats the symptom, not the systemic cause."
                ),
            },
            {
                "id": "c",
                "text": "Send an email asking affected users to voluntarily reboot their workstations",
                "correct": False,
                "rationale": (
                    "Incorrect. Relying on voluntary user action provides no assurance of compliance and does "
                    "not guarantee the GPO will actually apply or that offline machines will reconnect promptly."
                ),
            },
            {
                "id": "d",
                "text": "Permanently disable network access for the 40 non-compliant workstations",
                "correct": False,
                "rationale": (
                    "Incorrect. Cutting off network access is a disproportionate response that disrupts "
                    "business operations without addressing the underlying gap in how the baseline is delivered "
                    "and enforced to intermittently connected devices."
                ),
            },
        ],
        "explanation": (
            "GPO-based baselines apply automatically on reconnection and refresh interval, so the durable fix "
            "is ensuring that mechanism is relied on continuously and validated with periodic scanning — not a "
            "one-time manual correction, a voluntary ask, or a disproportionate network cutoff."
        ),
    },
    {
        "id": "nd4i-021",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Hardening & secure baselines",
        "stem": (
            "Select TWO hardening practices that would MOST effectively reduce a containerized application's "
            "attack surface without requiring changes to the application's own source code."
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Configure the container's root filesystem as read-only, allowing writes only to specific "
                    "mounted volumes the application actually requires"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A read-only root filesystem prevents an attacker who gains code execution inside "
                    "the container from persisting malicious files or tampering with the runtime environment "
                    "itself, with no application code changes required."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Scan container images for known vulnerabilities in the CI/CD pipeline before they are "
                    "pushed to the production registry, blocking images with critical unpatched CVEs"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Pipeline-stage image scanning catches vulnerable base images and dependencies "
                    "before they ever reach production, shrinking the attack surface without touching the "
                    "application's own code."
                ),
            },
            {
                "id": "c",
                "text": "Mount the host's Docker socket into every container so applications can dynamically manage other containers",
                "correct": False,
                "rationale": (
                    "Incorrect. Exposing the host's Docker socket inside a container is the opposite of "
                    "hardening — it gives a compromised container a direct path to control the host's entire "
                    "container runtime, dramatically increasing attack surface."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Grant every container the host's full Linux capability set, such as CAP_SYS_ADMIN, by "
                    "default to avoid application errors caused by insufficient permissions"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Granting the full capability set by default violates least privilege and "
                    "significantly expands what a compromised container can do to the host; hardening calls for "
                    "dropping unnecessary capabilities, not granting them all."
                ),
            },
        ],
        "explanation": (
            "Read-only filesystems and pipeline-stage image scanning both shrink attack surface without any "
            "application code change. Exposing the Docker socket and granting full host capabilities do the "
            "opposite — they are among the most dangerous container misconfigurations."
        ),
    },
    {
        "id": "nd4i-022",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Incident response process",
        "stem": (
            "Within minutes of confirming an active compromise of a web-facing server, an IR team blocks the "
            "attacker's known C2 IP address at the perimeter firewall and reroutes the server's traffic to a "
            "maintenance page, buying time before a scheduled next-day rebuild of the server from a verified "
            "clean image. Which term BEST describes the immediate firewall block and traffic reroute actions?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Short-term (tactical) containment",
                "correct": True,
                "rationale": (
                    "Correct. Quickly limiting damage with an immediate, minimally disruptive action — while a "
                    "more permanent fix is planned for later — is the definition of short-term/tactical "
                    "containment."
                ),
            },
            {
                "id": "b",
                "text": "Eradication",
                "correct": False,
                "rationale": (
                    "Incorrect. Eradication means removing the root cause of the compromise (such as rebuilding "
                    "the server from a clean image), which in this scenario is explicitly scheduled for the "
                    "following day and has not yet happened."
                ),
            },
            {
                "id": "c",
                "text": "Recovery",
                "correct": False,
                "rationale": (
                    "Incorrect. Recovery means restoring the system to normal, trusted production operation. "
                    "Here the server is still showing a maintenance page rather than serving normal traffic, so "
                    "recovery has not occurred."
                ),
            },
            {
                "id": "d",
                "text": "Long-term containment",
                "correct": False,
                "rationale": (
                    "Incorrect. Long-term containment typically involves a more durable interim fix, such as "
                    "patching or rebuilding while keeping the system minimally operational. The scenario's "
                    "next-day rebuild plan is closer to eradication; the immediate firewall block and reroute "
                    "described are the quick, tactical first response, not the durable interim measure."
                ),
            },
        ],
        "explanation": (
            "An immediate, fast action taken to stop further damage while a permanent remediation is still "
            "planned is short-term/tactical containment — distinct from eradication (removing root cause) and "
            "recovery (returning to normal operation), which have not yet occurred."
        ),
    },
    {
        "id": "nd4i-023",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Incident response process",
        "stem": (
            "During a ransomware incident, the IR team determines that negotiating with the threat actor, "
            "tracing the demanded cryptocurrency payment, and satisfying a newly triggered regulatory breach-"
            "notification obligation are all outside the in-house team's expertise. Which action reflects the "
            "BEST use of incident response planning in this situation?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Activate a pre-arranged third-party DFIR/incident response retainer with specialized "
                    "ransomware negotiation and regulatory notification experience, as identified during the "
                    "preparation phase of the IR plan"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Recognizing capability gaps and pre-arranging specialized outside support is "
                    "exactly what the preparation phase of incident response planning is for; activating that "
                    "retainer when the gap materializes is the appropriate response."
                ),
            },
            {
                "id": "b",
                "text": "Have the internal SOC team learn cryptocurrency tracing and negotiation techniques during the live incident to save cost",
                "correct": False,
                "rationale": (
                    "Incorrect. Attempting to build highly specialized skills on the fly during an active, time-"
                    "sensitive incident risks costly mistakes and delays; specialized capability gaps should be "
                    "addressed with pre-arranged expert support, not improvised learning under pressure."
                ),
            },
            {
                "id": "c",
                "text": "Decline outside help to keep the incident confidential and avoid involving additional parties",
                "correct": False,
                "rationale": (
                    "Incorrect. Refusing needed specialized help to preserve secrecy increases both technical "
                    "and legal risk, and does not satisfy regulatory notification obligations that already "
                    "apply regardless of how many parties are involved."
                ),
            },
            {
                "id": "d",
                "text": "Skip the regulatory breach notification since paying the ransom quickly may resolve the incident",
                "correct": False,
                "rationale": (
                    "Incorrect. Paying a ransom does not eliminate a legally mandated breach-notification "
                    "obligation, and skipping required notification exposes the organization to regulatory and "
                    "legal consequences independent of whether the ransom is paid."
                ),
            },
        ],
        "explanation": (
            "Sound IR preparation includes identifying skill gaps in advance and arranging specialized outside "
            "resources — such as a DFIR retainer with negotiation and regulatory experience — so they can be "
            "activated immediately rather than improvised, ignored, or bypassed during a live incident."
        ),
    },
    {
        "id": "nd4i-024",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Incident response process",
        "stem": (
            "A SOC's incident response plan defines Severity 1 as 'confirmed data exfiltration or ransomware "
            "impacting production' and Severity 2 as 'suspicious activity requiring investigation with no "
            "confirmed compromise.' An analyst discovers a single workstation beaconing to a known C2 domain, "
            "with no evidence yet of data exfiltration or lateral movement to other systems. Following the "
            "plan's defined criteria, which classification and immediate next step is MOST appropriate?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Classify the event as Severity 2, begin containment and investigation scoping per the "
                    "plan, and escalate to Severity 1 only if exfiltration or spread is later confirmed"
                ),
                "correct": True,
                "rationale": (
                    "Correct. The observed facts — beaconing on one host with no confirmed exfiltration or "
                    "spread — precisely match the plan's Severity 2 definition; following the defined criteria "
                    "means classifying and acting accordingly, then escalating if new evidence changes the "
                    "picture."
                ),
            },
            {
                "id": "b",
                "text": "Immediately declare Severity 1 and mobilize the full executive crisis-communication team",
                "correct": False,
                "rationale": (
                    "Incorrect. This overshoots the plan's own defined criteria, which reserve Severity 1 for "
                    "confirmed exfiltration or ransomware impact — jumping straight to full executive "
                    "mobilization on unconfirmed suspicious activity contradicts the plan and wastes response "
                    "resources."
                ),
            },
            {
                "id": "c",
                "text": "Take no action yet, since a single beaconing workstation represents negligible risk",
                "correct": False,
                "rationale": (
                    "Incorrect. Beaconing to a known C2 domain is confirmed suspicious activity that the plan "
                    "explicitly requires investigating under Severity 2 — dismissing it as negligible ignores "
                    "the plan's own criteria and risks the threat spreading undetected."
                ),
            },
            {
                "id": "d",
                "text": "Wait 24 hours to see if the beaconing recurs before taking any investigative action",
                "correct": False,
                "rationale": (
                    "Incorrect. Delaying investigation on a confirmed indicator of compromise gives an active "
                    "threat more time to spread or exfiltrate data; the plan calls for beginning investigation "
                    "and containment scoping promptly under Severity 2, not waiting to see what happens."
                ),
            },
        ],
        "explanation": (
            "Applying a predefined severity matrix correctly means matching the observed facts to its criteria "
            "— here, Severity 2 — and escalating only as new evidence warrants, rather than overreacting, "
            "underreacting, or delaying based on gut feel."
        ),
    },
    {
        "id": "nd4i-025",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log data sources",
        "stem": (
            "A security team investigating a cloud environment incident needs to determine exactly which IAM "
            "principal called the API to disable a critical storage bucket's versioning and access logging, and "
            "precisely when the call occurred. Which log source provides this information?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The cloud provider's management-plane API/audit log, which records every API call, the calling identity, and the timestamp",
                "correct": True,
                "rationale": (
                    "Correct. Management-plane audit logs (such as a cloud provider's account-activity log) "
                    "record every configuration-changing API call along with the exact calling principal and "
                    "timestamp — precisely what's needed to attribute this action."
                ),
            },
            {
                "id": "b",
                "text": "VPC flow logs showing network traffic metadata between resources",
                "correct": False,
                "rationale": (
                    "Incorrect. Flow logs capture source/destination IP, port, and byte-count metadata for "
                    "network traffic; they contain no information about which identity made a management API "
                    "call or what configuration change was made."
                ),
            },
            {
                "id": "c",
                "text": "The storage bucket's own object-access logs, showing which objects were read or written",
                "correct": False,
                "rationale": (
                    "Incorrect. Object-access (data-plane) logs record reads and writes to the stored objects "
                    "themselves, not management-plane configuration changes like disabling versioning, which is "
                    "a bucket-setting change rather than an object operation."
                ),
            },
            {
                "id": "d",
                "text": "The cloud provider's billing and cost-usage report",
                "correct": False,
                "rationale": (
                    "Incorrect. Billing reports summarize resource consumption and cost; they contain no record "
                    "of which identity performed a specific configuration-changing API call."
                ),
            },
        ],
        "explanation": (
            "Attributing a specific management-plane configuration change — like disabling versioning or "
            "logging — to a calling identity and timestamp requires the cloud provider's API/management audit "
            "log, distinct from network flow logs, object-access logs, or billing data."
        ),
    },
    {
        "id": "nd4i-026",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log data sources",
        "stem": (
            "An analyst suspects a database administrator is running unauthorized SELECT queries against a "
            "table containing customer payment card data, outside of any approved change window, using their "
            "own normal privileged database credentials rather than exploiting any vulnerability. Standard OS-"
            "level authentication logs show only that the DBA logged into the database server via RDP; they "
            "capture no information about which SQL statements were executed once connected. Which log source "
            "should the analyst reference to close this visibility gap?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Database activity monitoring (DAM) / database audit logs capturing the executed SQL statement text and the account that ran it",
                "correct": True,
                "rationale": (
                    "Correct. DAM/database-level audit logging records the actual queries executed against "
                    "specific tables, along with the executing account — exactly the query-level visibility "
                    "that OS-level authentication logs don't provide."
                ),
            },
            {
                "id": "b",
                "text": "Perimeter firewall logs showing allowed and denied network connections",
                "correct": False,
                "rationale": (
                    "Incorrect. Firewall logs operate at the network connection layer and have no visibility "
                    "into the content of an already-permitted RDP session, let alone the SQL statements run "
                    "inside it."
                ),
            },
            {
                "id": "c",
                "text": "Windows Security event log entries for successful RDP logins (Event ID 4624)",
                "correct": False,
                "rationale": (
                    "Incorrect. Login event logs confirm that the DBA authenticated to the server, which the "
                    "analyst already knows; they provide no record of what the DBA did once connected, such as "
                    "which queries were run."
                ),
            },
            {
                "id": "d",
                "text": "NetFlow records showing traffic volume between the DBA's workstation and the database server",
                "correct": False,
                "rationale": (
                    "Incorrect. NetFlow provides connection metadata such as byte counts and endpoints, not the "
                    "content of the SQL queries executed during the session."
                ),
            },
        ],
        "explanation": (
            "Investigating insider misuse of legitimate database credentials requires query-level visibility, "
            "which only database activity monitoring/audit logs provide — network and OS-level logs confirm "
            "connectivity and authentication but not what was queried."
        ),
    },
    {
        "id": "nd4i-027",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Malware classification",
        "stem": (
            "A workstation is repeatedly reinfected with identical malware within minutes of every clean OS "
            "reinstallation, even after the hard drive is completely wiped and physically replaced with a new "
            "drive. Forensic analysis of the motherboard's SPI flash chip reveals malicious code embedded "
            "directly in the system's UEFI firmware. Which classification BEST describes this malware?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A UEFI/firmware implant, persisting in motherboard firmware independent of any disk",
                "correct": True,
                "rationale": (
                    "Correct. Persistence that survives even a full physical hard-drive replacement can only "
                    "come from something stored outside the drive entirely — the motherboard's own firmware "
                    "chip, which a UEFI/firmware implant specifically targets."
                ),
            },
            {
                "id": "b",
                "text": "Ransomware that re-encrypts the new drive automatically after each reinstall",
                "correct": False,
                "rationale": (
                    "Incorrect. Ransomware encrypts data for extortion; it doesn't explain silent reinfection "
                    "surviving a full physical drive swap, and no ransom note or encryption behavior is "
                    "described."
                ),
            },
            {
                "id": "c",
                "text": "A boot-sector bootkit that modifies the disk's master boot record to survive OS reinstalls",
                "correct": False,
                "rationale": (
                    "Incorrect. A disk-resident bootkit modifies boot components stored on the drive itself, so "
                    "it would be eliminated by physically replacing the hard drive — which did not stop the "
                    "reinfection here, ruling out a purely disk-based bootkit."
                ),
            },
            {
                "id": "d",
                "text": "Fileless malware that resides only in volatile system memory (RAM)",
                "correct": False,
                "rationale": (
                    "Incorrect. Memory-resident fileless malware does not survive a power-off/reboot cycle at "
                    "all, let alone a complete OS reinstall and hard-drive replacement, so it cannot explain "
                    "this persistence."
                ),
            },
        ],
        "explanation": (
            "Persistence that survives a full physical hard-drive replacement points to firmware embedded on "
            "the motherboard itself — a UEFI/firmware implant — which sits below and independent of both the "
            "operating system and any disk, unlike ransomware, disk-based bootkits, or RAM-only malware."
        ),
    },
    {
        "id": "nd4i-028",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Malware classification",
        "stem": (
            "A widely used IT monitoring platform's official auto-update mechanism, signed with the vendor's "
            "legitimate code-signing certificate, silently delivers a malicious backdoor to thousands of "
            "customer environments after the vendor's own build server was compromised. Customers who never "
            "clicked a link, opened an attachment, or visited a malicious site received the backdoor purely by "
            "installing what appeared to be a routine, properly signed software update. Which term BEST "
            "classifies this attack technique?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A software supply chain attack, distributing a trojanized update through a trusted, legitimate delivery channel",
                "correct": True,
                "rationale": (
                    "Correct. Compromising the vendor's build process so a legitimate, validly signed update "
                    "channel delivers malicious code to every downstream customer is the defining pattern of a "
                    "software supply chain attack."
                ),
            },
            {
                "id": "b",
                "text": "A self-propagating worm exploiting a network service vulnerability",
                "correct": False,
                "rationale": (
                    "Incorrect. A worm spreads by directly exploiting vulnerabilities across a network without "
                    "needing a trusted delivery channel; here, the malware was delivered entirely through a "
                    "legitimate, signed update mechanism, not network-based self-propagation."
                ),
            },
            {
                "id": "c",
                "text": "A watering hole attack, compromising a website frequented by the intended victims",
                "correct": False,
                "rationale": (
                    "Incorrect. A watering hole attack compromises a third-party website victims are expected "
                    "to visit. No website compromise is described here — the compromise occurred at the "
                    "vendor's own build server and was delivered via the official update mechanism."
                ),
            },
            {
                "id": "d",
                "text": "Typosquatting, distributing malware through a similarly named but fraudulent package",
                "correct": False,
                "rationale": (
                    "Incorrect. Typosquatting relies on a deceptively similar name tricking a user or system "
                    "into fetching the wrong package. Here the malware came through the vendor's own genuine, "
                    "correctly named, properly signed update channel."
                ),
            },
        ],
        "explanation": (
            "Compromising a trusted vendor's build process so its own legitimate, signed update mechanism "
            "delivers malicious code downstream to customers is a software supply chain attack — distinct from "
            "worm propagation, watering hole compromise, or typosquatting, all of which rely on a different "
            "delivery mechanism."
        ),
    },
    {
        "id": "nd4i-029",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile device management",
        "stem": (
            "Security researchers demonstrate that a malicious Android app, once granted Accessibility Service "
            "permissions, can log keystrokes and draw a fake login screen on top of a legitimate banking app to "
            "harvest credentials. The organization's MDM platform correctly enforces device encryption, a "
            "passcode policy, and blocks installation from unknown sources, but the app was installed through "
            "the official app store and none of those MDM controls detect its malicious runtime behavior. "
            "Which mobile-specific security control is specifically designed to detect this kind of on-device "
            "malicious app behavior?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Mobile threat defense (MTD), which performs on-device behavioral analysis of app permissions and activity",
                "correct": True,
                "rationale": (
                    "Correct. MTD solutions analyze installed apps' runtime behavior — such as abusive use of "
                    "Accessibility Service permissions or overlay techniques — complementing MDM's "
                    "configuration/policy enforcement with active threat detection MDM alone doesn't provide."
                ),
            },
            {
                "id": "b",
                "text": "MDM-enforced application containerization that isolates corporate data from personal apps",
                "correct": False,
                "rationale": (
                    "Incorrect. Containerization isolates corporate data from personal apps but does not "
                    "analyze or detect malicious runtime behavior of an app that has already been installed "
                    "through the official store."
                ),
            },
            {
                "id": "c",
                "text": "MDM-enforced geofencing that restricts app access based on device location",
                "correct": False,
                "rationale": (
                    "Incorrect. Geofencing controls access based on physical location and has no capability to "
                    "detect malicious permission abuse or overlay attacks by an installed app."
                ),
            },
            {
                "id": "d",
                "text": "MDM remote wipe capability",
                "correct": False,
                "rationale": (
                    "Incorrect. Remote wipe is a reactive response available only after a compromise is already "
                    "known and confirmed; it provides no detection capability for identifying malicious app "
                    "behavior in the first place."
                ),
            },
        ],
        "explanation": (
            "MDM primarily manages device configuration and policy enforcement, not the behavioral analysis of "
            "installed apps. Detecting malicious on-device app behavior like Accessibility Service abuse or "
            "overlay attacks is the specific role of mobile threat defense (MTD)."
        ),
    },
    {
        "id": "nd4i-030",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile device management",
        "stem": (
            "An organization's MDM platform blocks any enrolled mobile device running an OS version more than "
            "two minor releases behind the current vendor release from establishing a VPN connection to "
            "internal resources, regardless of whether that device is otherwise compliant on encryption and "
            "passcode policy. Which risk does this specific control MOST directly mitigate?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Exposure of internal network resources to known, unpatched OS-level vulnerabilities "
                    "present on significantly outdated mobile operating system versions"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Gating VPN access on OS version currency ensures devices with known, unpatched OS "
                    "vulnerabilities cannot use that connectivity as a foothold to reach internal resources."
                ),
            },
            {
                "id": "b",
                "text": "Users evading jailbreak or root detection on their mobile devices",
                "correct": False,
                "rationale": (
                    "Incorrect. Jailbreak/root detection is a separate compliance check targeting tampered "
                    "device integrity; OS-version gating specifically targets unpatched vulnerabilities in an "
                    "outdated but otherwise untampered OS."
                ),
            },
            {
                "id": "c",
                "text": "Users installing unapproved applications outside of an application allow-list",
                "correct": False,
                "rationale": (
                    "Incorrect. Application allow-listing is a distinct control governing which apps may run; "
                    "it is unrelated to gating VPN access based on how current the device's OS version is."
                ),
            },
            {
                "id": "d",
                "text": "Non-compliance with data residency regulations governing where corporate data may be stored",
                "correct": False,
                "rationale": (
                    "Incorrect. Data residency concerns the geographic location where data is stored or "
                    "processed; it has no relationship to whether a device's OS version is current enough to be "
                    "trusted with VPN access."
                ),
            },
        ],
        "explanation": (
            "Blocking VPN access from devices running significantly outdated OS versions reduces the risk that "
            "known, unpatched OS-level vulnerabilities on those devices become an entry point into internal "
            "network resources — a distinct concern from jailbreak detection, app allow-listing, or data "
            "residency."
        ),
    },
    {
        "id": "nd4i-031",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Multifactor authentication",
        "stem": (
            "An online banking application requires only a password to log in and view account balances. When "
            "a customer initiates a wire transfer above $10,000, the application additionally prompts for a "
            "FIDO2 hardware security key tap before the transfer is authorized. Which authentication concept "
            "does the wire-transfer prompt illustrate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Step-up authentication",
                "correct": True,
                "rationale": (
                    "Correct. Requiring a stronger authentication factor only for a specific higher-risk action "
                    "— here, a large wire transfer — while a lighter factor suffices for lower-risk activity "
                    "like viewing balances, is the definition of step-up authentication."
                ),
            },
            {
                "id": "b",
                "text": "Federation",
                "correct": False,
                "rationale": (
                    "Incorrect. Federation involves trusting an external identity provider to authenticate "
                    "users across organizational boundaries. No external identity provider or cross-domain "
                    "trust relationship is described here."
                ),
            },
            {
                "id": "c",
                "text": "Continuous authentication",
                "correct": False,
                "rationale": (
                    "Incorrect. Continuous authentication passively and repeatedly verifies identity throughout "
                    "an entire session (for example, via behavioral biometrics). This scenario describes a "
                    "single, one-time additional prompt tied to a specific high-risk transaction, not ongoing "
                    "passive verification."
                ),
            },
            {
                "id": "d",
                "text": "MFA fatigue prevention",
                "correct": False,
                "rationale": (
                    "Incorrect. MFA fatigue prevention refers to techniques like number-matching that stop "
                    "attackers from wearing down a user with repeated push notifications. This scenario "
                    "describes risk-based escalation of authentication strength, not a defense against push-"
                    "bombing."
                ),
            },
        ],
        "explanation": (
            "Escalating to a stronger factor only for a specific higher-risk transaction is step-up "
            "authentication — distinct from federation (cross-domain trust), continuous authentication (ongoing "
            "passive verification), and MFA fatigue prevention (anti-push-bombing measures)."
        ),
    },
    {
        "id": "nd4i-032",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Multifactor authentication",
        "stem": (
            "A call center uses voice biometric authentication as a second factor for high-value customer "
            "requests. Security researchers demonstrate that an AI-generated deepfake voice clone, built "
            "entirely from publicly available recordings of the customer speaking in online videos, "
            "successfully passes the voice biometric check without any access to the customer's phone or "
            "device. Which statement BEST explains the underlying security weakness demonstrated?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Voice biometrics validate a physical vocal characteristic that can be synthetically "
                    "reproduced from sufficient recorded audio, so an inherence factor is not inherently immune "
                    "to spoofing if the underlying trait can be captured and recreated"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Inherence ('something you are') factors are not automatically unspoofable — if an "
                    "attacker can capture or synthetically reconstruct the underlying biological trait, as with "
                    "a sufficiently convincing deepfake voice clone, the factor can be bypassed."
                ),
            },
            {
                "id": "b",
                "text": "Voice biometrics are classified as a knowledge factor, which is inherently weaker than possession factors",
                "correct": False,
                "rationale": (
                    "Incorrect. Voice biometrics are an inherence ('something you are') factor, not a knowledge "
                    "factor; misclassifying the factor type does not explain why the spoofing attack succeeded."
                ),
            },
            {
                "id": "c",
                "text": "The attack succeeded because the call center never actually required a second authentication factor",
                "correct": False,
                "rationale": (
                    "Incorrect. Voice biometrics WAS the required second factor; the attack is a successful "
                    "spoof of that factor, not evidence that no second factor was in place."
                ),
            },
            {
                "id": "d",
                "text": "The deepfake attack required physical access to the customer's phone to capture the voiceprint",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario explicitly states the clone was built entirely from public online "
                    "recordings, with no device or physical access to the customer required at any point."
                ),
            },
        ],
        "explanation": (
            "Inherence factors like voice biometrics are only as strong as the difficulty of capturing or "
            "reproducing the underlying trait — sufficiently advanced deepfake synthesis from public recordings "
            "can defeat them without needing any device access or knowledge-factor confusion."
        ),
    },
    {
        "id": "nd4i-033",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Penetration testing phases",
        "stem": (
            "An organization already conducts an annual, fixed-scope penetration test against its production "
            "environment performed by a contracted team over a defined two-week window. The security team is "
            "now also considering launching a public bug bounty program covering the same production assets. "
            "Which characteristic MOST distinguishes a bug bounty program from the existing annual penetration "
            "test?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A bug bounty program provides continuous, crowdsourced testing from an open pool of "
                    "external researchers who are paid per validated vulnerability found, rather than a fixed-"
                    "scope engagement over a defined time window"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Bug bounty programs run continuously with an open, crowdsourced pool of "
                    "researchers compensated per validated finding, in contrast to a traditional pentest's "
                    "fixed team and fixed engagement window."
                ),
            },
            {
                "id": "b",
                "text": "Bug bounty programs require signed rules of engagement, while penetration tests do not",
                "correct": False,
                "rationale": (
                    "Incorrect. This is backwards — formally documented rules of engagement (defining scope, "
                    "authorized techniques, and boundaries) are especially critical for a contracted "
                    "penetration test, and well-run bug bounty programs also publish defined program rules."
                ),
            },
            {
                "id": "c",
                "text": "Bug bounty programs test only availability impact, while penetration tests test only confidentiality and integrity",
                "correct": False,
                "rationale": (
                    "Incorrect. Both bug bounty programs and penetration tests can and typically do cover "
                    "confidentiality, integrity, and availability impacts; there is no such rigid split between "
                    "the two testing models."
                ),
            },
            {
                "id": "d",
                "text": "Bug bounty findings are exempt from responsible/coordinated disclosure timelines that apply to penetration tests",
                "correct": False,
                "rationale": (
                    "Incorrect. This reverses good practice — both models should follow coordinated, timely "
                    "disclosure and remediation processes; bug bounty findings are not exempt from responsible "
                    "handling."
                ),
            },
        ],
        "explanation": (
            "The defining difference is structural: a bug bounty program is a continuous, crowdsourced, pay-"
            "per-finding model, while a traditional penetration test is a fixed-scope, fixed-team engagement "
            "over a defined window — not differences in rules of engagement, impact type, or disclosure "
            "obligations."
        ),
    },
    {
        "id": "nd4i-034",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Penetration testing phases",
        "stem": (
            "A penetration test's rules of engagement specifically instruct the testing team to avoid actively "
            "exploiting any identified vulnerability on the plant's programmable logic controllers (PLCs), "
            "restricting testing on those devices to passive scanning and vulnerability identification only — "
            "even though active exploitation is fully permitted on the corporate IT network in the same "
            "engagement. Which reasoning BEST explains this scoping restriction?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Legacy ICS/OT devices like PLCs often cannot tolerate the traffic or processing load of "
                    "active exploitation and may crash, malfunction, or create physical safety hazards, so "
                    "testing is intentionally limited to lower-risk methods"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Fragile OT devices frequently lack the robustness of modern IT systems and can "
                    "fail or behave dangerously under exploitation attempts, so rules of engagement commonly "
                    "restrict OT testing to passive, non-disruptive techniques to protect safety and uptime."
                ),
            },
            {
                "id": "b",
                "text": "PLCs are inherently immune to known exploitation techniques, so active testing would be pointless",
                "correct": False,
                "rationale": (
                    "Incorrect. PLCs are commonly vulnerable to known exploits — that vulnerability is exactly "
                    "why passive scanning is still valuable; the restriction exists because of fragility and "
                    "safety risk, not because exploitation would fail."
                ),
            },
            {
                "id": "c",
                "text": "The testing team's tools simply do not support any industrial control system protocols",
                "correct": False,
                "rationale": (
                    "Incorrect. This describes a hypothetical tooling limitation, not the actual reasoning "
                    "behind a deliberate rules-of-engagement scoping decision made to protect fragile, safety-"
                    "critical systems."
                ),
            },
            {
                "id": "d",
                "text": "Active exploitation of ICS devices is illegal under all circumstances, regardless of authorization",
                "correct": False,
                "rationale": (
                    "Incorrect. Authorized, properly scoped penetration testing of ICS/OT systems can be legal "
                    "under a signed engagement; the restriction here is a deliberate safety and stability "
                    "scoping choice, not a blanket legal prohibition."
                ),
            },
        ],
        "explanation": (
            "Rules of engagement often carve out OT/ICS devices for passive-only testing because active "
            "exploitation risks crashing fragile, safety-critical systems — a risk-management scoping decision, "
            "not evidence that PLCs are unexploitable, untestable, or that ICS testing is universally illegal."
        ),
    },
    {
        "id": "nd4i-035",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Port and protocol security",
        "stem": (
            "A cloud security review finds the Docker daemon's remote management API listening on TCP port "
            "2375 (plaintext, no authentication) and reachable directly from the internet. Anyone able to reach "
            "the port can create a new privileged container and obtain root-level code execution on the "
            "underlying host. Which remediation BEST addresses this finding?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Disable remote access to the Docker daemon API entirely, or if remote management is "
                    "required, enable mutual TLS client-certificate authentication and restrict access via "
                    "firewall to trusted management hosts only"
                ),
                "correct": True,
                "rationale": (
                    "Correct. The root problem is an unauthenticated, unencrypted, internet-reachable "
                    "management interface; removing remote access or requiring mutual TLS plus firewall "
                    "restriction directly closes that exposure."
                ),
            },
            {
                "id": "b",
                "text": "Change the Docker daemon's listening port from 2375 to a random high-numbered port",
                "correct": False,
                "rationale": (
                    "Incorrect. Moving the port is security through obscurity — a port scan will still find the "
                    "service, and it does nothing to address the complete lack of authentication or encryption."
                ),
            },
            {
                "id": "c",
                "text": "Apply the latest Docker Engine security patch to the host",
                "correct": False,
                "rationale": (
                    "Incorrect. Patching addresses software vulnerabilities, but this exposure is an "
                    "intentional configuration choice — running the management API unauthenticated and "
                    "internet-facing — which a patch does not change."
                ),
            },
            {
                "id": "d",
                "text": "Enable verbose logging on the Docker daemon for auditing purposes",
                "correct": False,
                "rationale": (
                    "Incorrect. Logging is a detective control that helps investigate abuse after the fact; it "
                    "does not remediate the exposed, unauthenticated management interface itself."
                ),
            },
        ],
        "explanation": (
            "An unauthenticated, unencrypted, internet-reachable Docker API is a configuration exposure, not a "
            "patchable bug or something obscurity fixes — the remediation is to remove remote access or require "
            "strong mutual authentication plus network restriction."
        ),
    },
    {
        "id": "nd4i-036",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Port and protocol security",
        "stem": (
            "An external vulnerability scan finds an Elasticsearch cluster listening on TCP port 9200, "
            "reachable directly from the internet, with no authentication or authorization enabled on the API. "
            "Any unauthenticated party who reaches the port can query and retrieve every indexed document, "
            "including customer PII. Which remediation BEST addresses this finding?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Enable authentication and authorization on the Elasticsearch cluster's API, and restrict "
                    "network access to only trusted internal hosts, removing direct internet exposure"
                ),
                "correct": True,
                "rationale": (
                    "Correct. The root cause is that the API accepts unauthenticated queries and is directly "
                    "internet-facing; enabling access control on the API and eliminating public reachability "
                    "together close the exposure."
                ),
            },
            {
                "id": "b",
                "text": "Increase the cluster's shard replication factor to improve fault tolerance",
                "correct": False,
                "rationale": (
                    "Incorrect. Replication factor is an availability/durability setting; it has no effect on "
                    "whether unauthenticated internet users can query and read confidential indexed documents."
                ),
            },
            {
                "id": "c",
                "text": "Enable index-level compression to reduce storage costs",
                "correct": False,
                "rationale": (
                    "Incorrect. Compression is a storage-efficiency setting unrelated to access control; it "
                    "does nothing to prevent unauthenticated users from querying the cluster's contents."
                ),
            },
            {
                "id": "d",
                "text": "Rotate the cluster's TLS certificate used to encrypt data in transit",
                "correct": False,
                "rationale": (
                    "Incorrect. Rotating a TLS certificate improves transport encryption hygiene but does not "
                    "add authentication — an unauthenticated party could still connect over TLS and query every "
                    "document, since encryption in transit does not equal access control."
                ),
            },
        ],
        "explanation": (
            "The finding is a missing-authentication exposure combined with unnecessary internet reachability. "
            "Fixing it requires adding actual access control and removing public exposure — not availability "
            "tuning, storage optimization, or a certificate rotation that leaves the API just as open to any "
            "authenticated-looking connection."
        ),
    },
    {
        "id": "nd4i-037",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Privileged access management",
        "stem": (
            "An Active Directory security review finds that domain administrators routinely use their same "
            "privileged domain admin account to log into both domain controllers and standard user "
            "workstations, in order to provide desktop support. This means a credential-theft technique such as "
            "Pass-the-Hash, executed against a compromised user workstation, could expose the credential "
            "material needed to compromise the entire domain. Which architectural principle, if properly "
            "enforced, would BEST prevent this risk?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A tiered administration model that strictly prohibits Tier 0 (domain-admin-level) "
                    "credentials from ever being used to log into lower-trust Tier 1/Tier 2 systems"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Tiered administration explicitly forbids using the highest-trust credentials on "
                    "lower-trust systems, so a compromised user workstation can never expose domain-admin "
                    "credential material in the first place."
                ),
            },
            {
                "id": "b",
                "text": "Requiring a longer, more complex password for the domain admin account",
                "correct": False,
                "rationale": (
                    "Incorrect. Pass-the-Hash reuses the cached credential material itself, not the plaintext "
                    "password; a longer password does not prevent the hash from being captured and replayed "
                    "once the account authenticates on a lower-trust machine."
                ),
            },
            {
                "id": "c",
                "text": "Enabling multifactor authentication only at the initial VPN connection",
                "correct": False,
                "rationale": (
                    "Incorrect. MFA at initial VPN login does not stop lateral reuse of a credential or hash "
                    "already cached on a workstation after that initial authentication succeeds."
                ),
            },
            {
                "id": "d",
                "text": "Rotating the domain admin account's password weekly instead of quarterly",
                "correct": False,
                "rationale": (
                    "Incorrect. More frequent rotation shrinks the window an already-stolen credential remains "
                    "useful, but it does not structurally prevent the same high-privilege account from being "
                    "used on lower-trust systems in the first place."
                ),
            },
        ],
        "explanation": (
            "Tiered administration structurally prevents high-trust credentials from ever touching lower-trust "
            "systems, eliminating the exposure at its root — unlike password complexity, single-point MFA, or "
            "rotation frequency, which only reduce the impact after the risky practice has already occurred."
        ),
    },
    {
        "id": "nd4i-038",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Privileged access management",
        "stem": (
            "Select TWO practices that reduce the risk of credential-theft techniques, such as Pass-the-Hash or "
            "Pass-the-Ticket, enabling lateral movement from a compromised low-privilege workstation to high-"
            "value systems."
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Enforce a tiered administration model so high-privilege credentials are never entered on "
                    "lower-trust, general-purpose workstations"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Preventing privileged credentials from ever touching lower-trust systems means a "
                    "compromised low-privilege workstation has no privileged material to steal in the first "
                    "place."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Require administrators to perform privileged tasks only from a dedicated, hardened "
                    "privileged access workstation (PAW) with no general internet browsing or email access"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A PAW dramatically shrinks the attack surface where privileged credentials are "
                    "ever used, since it isn't exposed to the phishing and browsing risks of a general-purpose "
                    "endpoint."
                ),
            },
            {
                "id": "c",
                "text": "Increase the maximum Kerberos ticket lifetime so administrators are prompted to re-authenticate less often",
                "correct": False,
                "rationale": (
                    "Incorrect. This is backwards — a longer ticket lifetime increases the window in which a "
                    "stolen Kerberos ticket remains usable by an attacker, worsening Pass-the-Ticket risk rather "
                    "than reducing it."
                ),
            },
            {
                "id": "d",
                "text": "Grant every help-desk technician standing local administrator rights on all workstations to speed up support",
                "correct": False,
                "rationale": (
                    "Incorrect. Broadly granting standing local admin rights multiplies the number of endpoints "
                    "holding privileged credential material, increasing rather than reducing the attack surface "
                    "for lateral movement."
                ),
            },
        ],
        "explanation": (
            "Tiered administration and dedicated privileged access workstations both limit where privileged "
            "credentials are ever used, closing off lateral-movement paths — while longer ticket lifetimes and "
            "broad standing admin rights both expand the attack surface instead."
        ),
    },
    {
        "id": "nd4i-039",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "A web application logs each failed login attempt, including the raw username field submitted by "
            "the client, directly to a text file later ingested by the SIEM. An attacker submits a username "
            "value containing an embedded newline character followed by a fabricated line reading "
            "'user=admin action=login result=SUCCESS'. The SIEM parses the forged line as a separate, "
            "legitimate successful admin login event. Which vulnerability, and which remediation, are BEST "
            "associated with this scenario?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Log injection (log forging) caused by writing unsanitized user input directly to logs; "
                    "remediate by sanitizing/encoding control characters (such as newlines) before logging, or "
                    "by using structured logging so injected characters cannot fabricate new entries"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Embedding a control character to fabricate what looks like a separate, legitimate "
                    "log line is the textbook definition of log injection, and the fix is to neutralize control "
                    "characters (or switch to a structured format immune to raw text injection) before writing "
                    "the entry."
                ),
            },
            {
                "id": "b",
                "text": "SQL injection; remediate by using parameterized queries for all database calls",
                "correct": False,
                "rationale": (
                    "Incorrect. No database query is involved — the attack manipulates a text log file's "
                    "content directly, not SQL syntax, so parameterized queries are irrelevant here."
                ),
            },
            {
                "id": "c",
                "text": (
                    "A Log4Shell-style remote code execution vulnerability; remediate with a WAF rule blocking "
                    "JNDI lookup strings"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. No code execution or JNDI lookup is described — the input only forges the "
                    "content and structure of a log line, not remote code execution via a logging library "
                    "vulnerability."
                ),
            },
            {
                "id": "d",
                "text": "Alert fatigue caused by an overly sensitive correlation rule; remediate by raising the alert threshold",
                "correct": False,
                "rationale": (
                    "Incorrect. This misdiagnoses the issue — the SIEM correctly parsed what looks like a "
                    "genuine log line because the application never sanitized the input before writing it; "
                    "adjusting alert thresholds does not fix the underlying input-handling flaw."
                ),
            },
        ],
        "explanation": (
            "Failing to sanitize user-controlled input before writing it to a log file lets an attacker inject "
            "control characters that fabricate entirely new, fake log entries — a distinct vulnerability from "
            "SQL injection, Log4Shell-style RCE, or an alert-tuning problem."
        ),
    },
    {
        "id": "nd4i-040",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "An analyst reconstructing an attack timeline finds that a firewall log timestamps a suspicious "
            "connection at 14:02:03, while the domain controller's security log timestamps a related "
            "authentication event — which the analyst believes actually occurred moments before the connection "
            "— at 14:07:41, five minutes later than expected. Investigation reveals the domain controller's "
            "clock has drifted and is not synchronized to the same time source as the firewall. Which practice, "
            "if enforced organization-wide, would BEST prevent this kind of timeline reconstruction error in "
            "future investigations?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Synchronizing all log-generating systems to a common, authoritative NTP time source",
                "correct": True,
                "rationale": (
                    "Correct. Consistent time synchronization across every log source is what keeps timestamps "
                    "comparable and correlatable during an investigation, directly preventing the kind of drift-"
                    "induced sequencing error described."
                ),
            },
            {
                "id": "b",
                "text": "Increasing SIEM log retention from 90 days to 13 months",
                "correct": False,
                "rationale": (
                    "Incorrect. Retaining logs longer only affects how far back data is available; it does "
                    "nothing to correct a clock that is drifted and out of sync with other systems."
                ),
            },
            {
                "id": "c",
                "text": "Enabling log compression on the SIEM to reduce storage costs",
                "correct": False,
                "rationale": (
                    "Incorrect. Compression is a storage-efficiency measure with no effect on the accuracy or "
                    "synchronization of the timestamps recorded within the logs."
                ),
            },
            {
                "id": "d",
                "text": "Configuring the SIEM to display all timestamps in UTC instead of local time",
                "correct": False,
                "rationale": (
                    "Incorrect. Standardizing the display time zone is a genuinely useful related practice, but "
                    "it only normalizes how timestamps are shown — it does not correct an underlying clock that "
                    "is actually drifted relative to other systems, which is the root cause described here."
                ),
            },
        ],
        "explanation": (
            "Accurate cross-log timeline reconstruction depends on every source sharing a common, synchronized "
            "time reference (NTP) — retention length, compression, and display time zone formatting are all "
            "unrelated to, or insufficient to fix, actual clock drift between systems."
        ),
    },
    {
        "id": "nd4i-041",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A vulnerability management team is prioritizing remediation across thousands of findings. "
            "Vulnerability A and Vulnerability B both have an identical CVSS base score of 7.5 (High). "
            "Vulnerability A has an Exploit Prediction Scoring System (EPSS) score of 0.82 (an 82% estimated "
            "probability of exploitation in the next 30 days) and appears on the CISA Known Exploited "
            "Vulnerabilities (KEV) catalog. Vulnerability B has an EPSS score of 0.01 and does not appear on the "
            "KEV catalog. Which remediation prioritization decision is BEST supported by this additional data?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Prioritize Vulnerability A for immediate remediation ahead of Vulnerability B, since EPSS "
                    "and KEV listing indicate active or highly likely real-world exploitation beyond what the "
                    "identical CVSS base score alone conveys"
                ),
                "correct": True,
                "rationale": (
                    "Correct. CVSS base score reflects theoretical severity, while EPSS and KEV reflect real-"
                    "world exploitation likelihood and confirmed active exploitation — layering that threat "
                    "intelligence onto equal base scores is exactly how mature programs break the tie in favor "
                    "of the vulnerability that is actually being exploited."
                ),
            },
            {
                "id": "b",
                "text": "Treat both vulnerabilities identically since they share the same CVSS base score",
                "correct": False,
                "rationale": (
                    "Incorrect. Treating them identically ignores the significant real-world exploitation-"
                    "likelihood signal that EPSS and KEV provide, which is precisely the risk that CVSS-base-"
                    "score-only prioritization misses."
                ),
            },
            {
                "id": "c",
                "text": "Prioritize Vulnerability B because a lower EPSS score means it is more novel and therefore more dangerous",
                "correct": False,
                "rationale": (
                    "Incorrect. A lower EPSS score means a lower estimated probability of exploitation, not "
                    "greater danger — this inverts the meaning of the metric entirely."
                ),
            },
            {
                "id": "d",
                "text": "Ignore EPSS and KEV data entirely because they are not part of the official CVSS specification",
                "correct": False,
                "rationale": (
                    "Incorrect. It's true EPSS and KEV are separate frameworks from CVSS, but that's exactly "
                    "why mature vulnerability management programs incorporate them: CVSS alone measures "
                    "severity, not likelihood of exploitation, so relying on CVSS alone would miss the "
                    "actionable threat-intelligence signal these two vulnerabilities clearly differ on."
                ),
            },
        ],
        "explanation": (
            "CVSS base score alone measures potential severity, not the likelihood a vulnerability is actually "
            "being exploited. EPSS and KEV supply that missing likelihood signal, and mature programs use them "
            "to break ties between equally-scored vulnerabilities."
        ),
    },
    {
        "id": "nd4i-042",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A vulnerability scan individually rates two findings on a web server as Medium severity: an "
            "information-disclosure bug that reveals internal server file paths, and a Low-severity "
            "authenticated file-upload feature with no file-type validation, reachable only by a low-privilege "
            "user. Considered separately, neither finding meets the organization's Critical-remediation SLA. A "
            "penetration test then demonstrates that combining the two — using the disclosed paths to locate "
            "the web root, then uploading a web shell via the unvalidated upload feature — achieves full remote "
            "code execution as the web server account. Which vulnerability management principle is BEST "
            "illustrated, and what should the organization do differently?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Vulnerability chaining — individually low/medium-severity findings can combine into a "
                    "critical, exploitable attack path; risk analysts or testers should evaluate combined "
                    "exploitability rather than relying solely on each finding's isolated severity rating"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Neither finding alone reached Critical severity, but chaining them together "
                    "produced full remote code execution — exactly the scenario vulnerability chaining "
                    "analysis is meant to catch, which isolated per-finding scoring misses."
                ),
            },
            {
                "id": "b",
                "text": "This demonstrates a CVSS scoring error, and both findings should be independently re-scored as Critical",
                "correct": False,
                "rationale": (
                    "Incorrect. Each finding's isolated severity rating may be entirely accurate on its own; "
                    "the elevated risk emerges specifically from their combination, not from a scoring mistake "
                    "on either individual finding."
                ),
            },
            {
                "id": "c",
                "text": "This demonstrates that vulnerability scanners are unreliable and should be replaced with manual review only",
                "correct": False,
                "rationale": (
                    "Incorrect. The scanner correctly identified both underlying issues; the gap is in "
                    "evaluating combined exploitability across findings, not a fundamental failure of scanning "
                    "that requires abandoning automated tools."
                ),
            },
            {
                "id": "d",
                "text": "This demonstrates the need for compensating controls rather than remediation of either finding individually",
                "correct": False,
                "rationale": (
                    "Incorrect. Remediating either underlying flaw — fixing the information disclosure or "
                    "adding file-type validation to the upload feature — breaks the chain entirely; relying on "
                    "compensating controls instead of fixing an identified root cause misses the actual lesson "
                    "about evaluating chained exploitability."
                ),
            },
        ],
        "explanation": (
            "Vulnerability chaining shows why per-finding CVSS scoring alone can understate real risk: two "
            "individually modest findings combined to enable full remote code execution, meaning remediation "
            "prioritization must also consider combined attack paths, not just isolated severity ratings."
        ),
    },
    {
        "id": "nd4i-043",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Wireless security",
        "stem": (
            "A small branch office restricts wireless access using MAC address filtering — allowing only a pre-"
            "approved list of device MAC addresses to associate with the AP — in addition to WPA2-PSK. During "
            "an assessment, a tester passively captures wireless traffic, identifies the MAC address of an "
            "already-connected authorized laptop, and successfully spoofs that MAC address on their own device "
            "to gain unauthorized network access. Which statement BEST explains why MAC filtering failed to "
            "provide meaningful additional security here?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "MAC addresses are transmitted in cleartext in 802.11 frame headers even on an encrypted "
                    "network, so they can be trivially observed and spoofed, making MAC filtering only a minor "
                    "obstacle rather than a real access control boundary"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Frame headers carrying source and destination MAC addresses are not encrypted by "
                    "WPA2's payload encryption, so any nearby device can passively observe a valid MAC address "
                    "and reconfigure its own network interface to impersonate it."
                ),
            },
            {
                "id": "b",
                "text": "MAC filtering failed because the access point was actually using WEP instead of WPA2",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario explicitly states WPA2-PSK was in use; the weakness described has "
                    "nothing to do with a downgrade to WEP."
                ),
            },
            {
                "id": "c",
                "text": "MAC filtering failed because the pre-approved device list exceeded the access point's maximum supported entries",
                "correct": False,
                "rationale": (
                    "Incorrect. No list-size limit or overflow condition is described in the scenario; the "
                    "bypass occurred through MAC address spoofing, not a capacity limitation."
                ),
            },
            {
                "id": "d",
                "text": "MAC filtering failed because the attacker performed a key-reinstallation (KRACK) downgrade attack against the encryption handshake",
                "correct": False,
                "rationale": (
                    "Incorrect. KRACK targets the WPA2 4-way handshake to force nonce reuse and decrypt traffic; "
                    "the technique described here is observing and spoofing a MAC address, an entirely "
                    "different attack against the access-list control, not the encryption handshake."
                ),
            },
        ],
        "explanation": (
            "802.11 MAC addresses are visible in cleartext frame headers regardless of payload encryption, so "
            "MAC filtering is trivially bypassed by observing and spoofing an authorized address — a distinct "
            "weakness from a WEP downgrade, a list-capacity limit, or a KRACK handshake attack."
        ),
    },
    {
        "id": "nd4i-044",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Wireless security",
        "stem": (
            "A hotel's guest Wi-Fi network requires guests to accept terms of service on a captive portal page "
            "before Internet access is granted, but the underlying wireless link itself is completely "
            "unencrypted (open, no WPA2/WPA3), meaning any guest device within range can observe other guests' "
            "unencrypted traffic on the same wireless segment. Which control would MOST effectively address "
            "this confidentiality risk while preserving the simple, no-shared-password captive-portal onboarding "
            "experience guests currently have?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Deploy WPA3 with Enhanced Open (OWE), which individually encrypts each client's traffic "
                    "without requiring a shared password, combined with client isolation"
                ),
                "correct": True,
                "rationale": (
                    "Correct. WPA3 Enhanced Open (OWE) provides per-client encryption over an open network with "
                    "no shared credential to distribute, preserving the frictionless captive-portal experience "
                    "while eliminating the ability of one guest to eavesdrop on another's traffic."
                ),
            },
            {
                "id": "b",
                "text": "Replace the captive portal with a single shared WPA2-PSK passphrase printed at the front desk",
                "correct": False,
                "rationale": (
                    "Incorrect. A shared passphrase known to every guest still lets any guest decrypt every "
                    "other guest's traffic using that same key, and it also removes the simple captive-portal "
                    "onboarding flow the hotel wants to preserve."
                ),
            },
            {
                "id": "c",
                "text": "Rely on the hotel's core network firewall to block inter-guest traffic, since Wi-Fi encryption is not required for compliance",
                "correct": False,
                "rationale": (
                    "Incorrect. A firewall downstream of the access point cannot prevent one guest device from "
                    "passively sniffing another guest's traffic over the shared, unencrypted radio link itself, "
                    "before it ever reaches the firewall."
                ),
            },
            {
                "id": "d",
                "text": "Require every guest to install a corporate VPN client before being allowed to connect",
                "correct": False,
                "rationale": (
                    "Incorrect. Mandating a VPN client install is a heavy, unrealistic burden for transient "
                    "hotel guests and directly conflicts with the requirement to preserve a simple onboarding "
                    "experience."
                ),
            },
        ],
        "explanation": (
            "WPA3 Enhanced Open (OWE) is designed exactly for this situation: it encrypts traffic per-client on "
            "an open network with no shared password, protecting guest confidentiality without sacrificing the "
            "frictionless captive-portal onboarding a shared passphrase, downstream firewall, or mandatory VPN "
            "install would all disrupt or fail to fix."
        ),
    },
]

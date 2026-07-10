"""CompTIA Security+ SY0-701 practice questions — Domain 4 (Security Operations), file J."""

QUESTIONS = [
    {
        "id": "nd4j-001",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Access control models",
        "stem": (
            "A city government's payroll system currently requires an IT administrator to individually grant "
            "each of 800 employees rights to specific payroll records, one grant at a time, with no reusable "
            "grouping. An audit finds that permissions map cleanly onto about 15 standard job titles (e.g., "
            "'Payroll Clerk,' 'Benefits Analyst,' 'Auditor'), and employees who share the same title always "
            "need identical access. Which access control model would MOST directly eliminate the administrative "
            "burden described?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Role-based access control (RBAC), defining roughly 15 roles matching the job titles so "
                    "employees inherit permissions through role assignment"
                ),
                "correct": True,
                "rationale": (
                    "Correct. The scenario describes permissions that map cleanly onto a small, static set of "
                    "job functions. RBAC directly replaces one-by-one individual grants with reusable role "
                    "definitions, eliminating the described administrative burden."
                ),
            },
            {
                "id": "b",
                "text": "Attribute-based access control (ABAC), evaluating dozens of individual user attributes per request",
                "correct": False,
                "rationale": (
                    "Incorrect. ABAC adds a policy engine and multi-attribute evaluation overhead that is not "
                    "needed here; the scenario maps cleanly onto a small set of static job titles, which RBAC "
                    "handles more directly and simply."
                ),
            },
            {
                "id": "c",
                "text": "Mandatory access control (MAC), applying fixed sensitivity labels set by a central authority",
                "correct": False,
                "rationale": (
                    "Incorrect. MAC governs data classification and clearance comparisons; it has no native "
                    "concept of grouping permissions by job function/title, which is the actual problem "
                    "described."
                ),
            },
            {
                "id": "d",
                "text": "Continue discretionary access control (DAC), but route every grant through a single centralized administrator",
                "correct": False,
                "rationale": (
                    "Incorrect. This still requires individual, non-reusable grants for each of 800 employees; "
                    "centralizing who performs the grants does not remove the per-user administrative burden "
                    "itself."
                ),
            },
        ],
        "explanation": (
            "RBAC is designed exactly for scenarios where access needs map cleanly onto a small set of job "
            "functions: permissions are assigned once to a role, and users inherit them by role membership, "
            "eliminating repetitive individual grants."
        ),
    },
    {
        "id": "nd4j-002",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Access control models",
        "stem": (
            "A multi-tenant SaaS platform must ensure that a file tagged 'Project-Falcon' is only accessible to "
            "users whose profile lists 'Project-Falcon' as an active project AND who are connecting from an IP "
            "address within the customer's registered corporate range. The same user must be denied access to "
            "that same file the moment either condition is no longer true. Which access control model natively "
            "supports this policy?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Attribute-based access control (ABAC)",
                "correct": True,
                "rationale": (
                    "Correct. ABAC evaluates a resource attribute (the project tag), a subject attribute "
                    "(project membership), and an environmental attribute (source IP) together at request time, "
                    "which is exactly the dynamic, multi-condition decision described."
                ),
            },
            {
                "id": "b",
                "text": "Role-based access control (RBAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. RBAC's static roles cannot cleanly express a dynamic combination of a resource "
                    "tag matching plus a real-time network-location condition without creating an unmanageable "
                    "explosion of project-specific, IP-specific roles."
                ),
            },
            {
                "id": "c",
                "text": "Discretionary access control (DAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no individual resource owner granting access at their discretion here; "
                    "the policy is centrally defined and evaluated dynamically against attributes, not left to "
                    "an owner's judgment."
                ),
            },
            {
                "id": "d",
                "text": "Mandatory access control (MAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. MAC relies on static classification/clearance labels assigned by a central "
                    "authority; it does not natively incorporate real-time contextual attributes such as the "
                    "requester's current source IP address."
                ),
            },
        ],
        "explanation": (
            "ABAC is the only model listed that natively evaluates subject, resource, and environmental "
            "attributes together in real time, which is required to enforce a policy that depends on both "
            "project membership and current network location simultaneously."
        ),
    },
    {
        "id": "nd4j-003",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Access control models",
        "stem": (
            "Select TWO statements that correctly distinguish mandatory access control (MAC) from rule-based "
            "access control (an ordered access control list, such as on a firewall or router)."
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "MAC access decisions are driven by comparing a subject's clearance level to an object's "
                    "fixed classification label, both assigned by a central authority."
                ),
                "correct": True,
                "rationale": (
                    "Correct. This is the defining mechanism of MAC: centrally assigned clearance and "
                    "classification labels are compared to determine access, independent of any resource "
                    "owner's discretion."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Rule-based access control evaluates an ordered set of conditional statements (e.g., permit/"
                    "deny by source, destination, or port) against each request, typically applying the first "
                    "matching rule."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Rule-based access control (as implemented in firewall/router ACLs) processes "
                    "rules in sequence and applies the first match, commonly ending with an implicit deny."
                ),
            },
            {
                "id": "c",
                "text": "MAC and rule-based access control are simply two names for the exact same mechanism and are always interchangeable.",
                "correct": False,
                "rationale": (
                    "Incorrect. They differ fundamentally: MAC governs subject/object clearance-label "
                    "comparisons for data confidentiality, while rule-based access control evaluates ordered "
                    "conditional criteria (often network-oriented) unrelated to classification labels."
                ),
            },
            {
                "id": "d",
                "text": "Rule-based access control requires clearance levels such as Confidential, Secret, and Top Secret to be assigned to every rule.",
                "correct": False,
                "rationale": (
                    "Incorrect. Clearance/classification labels are a MAC concept. Rule-based ACL entries are "
                    "typically defined using network or traffic criteria (source, destination, port, protocol), "
                    "not security clearance levels."
                ),
            },
        ],
        "explanation": (
            "MAC ties access to centrally assigned clearance/classification labels, while rule-based access "
            "control evaluates an ordered list of conditional rules against each request. They are distinct "
            "mechanisms that are sometimes confused because both are 'centrally defined,' but their evaluation "
            "logic and purpose differ."
        ),
    },
    {
        "id": "nd4j-004",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Application security",
        "stem": (
            "A banking web application performs fund transfers by having the browser send a simple GET request "
            "such as '/transfer?to=ACCT123&amount=500', relying solely on the victim's active authenticated "
            "session cookie to authorize the action — the request contains no other unpredictable, request-"
            "specific value. An attacker embeds that exact URL in an <img> tag on an unrelated forum page. Any "
            "logged-in victim who merely views the forum page unknowingly triggers a transfer. Which "
            "vulnerability class is being exploited, and what is the most effective mitigation?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Cross-site request forgery (CSRF); mitigate by requiring a unique, unpredictable anti-CSRF "
                    "token on state-changing requests and setting session cookies with SameSite=Strict/Lax."
                ),
                "correct": True,
                "rationale": (
                    "Correct. The victim's browser automatically sends an authenticated request the victim never "
                    "intended, purely because the session cookie is attached — the textbook definition of CSRF. "
                    "Anti-CSRF tokens and SameSite cookies prevent the forged request from being accepted."
                ),
            },
            {
                "id": "b",
                "text": "Reflected cross-site scripting (XSS); mitigate by output-encoding all user-supplied data before rendering it",
                "correct": False,
                "rationale": (
                    "Incorrect. XSS requires attacker-controlled script to execute in the victim's browser; here "
                    "no script is injected — the browser simply follows an authenticated request it was never "
                    "meant to send, which is CSRF, not XSS."
                ),
            },
            {
                "id": "c",
                "text": "SQL injection; mitigate with parameterized queries",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no malicious SQL syntax or query manipulation described; the issue is a "
                    "forged state-changing request executed using the victim's session, unrelated to how the "
                    "backend constructs database queries."
                ),
            },
            {
                "id": "d",
                "text": "Insecure direct object reference (IDOR); mitigate by enforcing server-side ownership checks on the account identifier",
                "correct": False,
                "rationale": (
                    "Incorrect. IDOR occurs when an authenticated user manipulates an identifier to access "
                    "another user's own objects. Here the core issue is that a forged cross-site request executes "
                    "with the victim's own credentials without their consent — that is CSRF."
                ),
            },
        ],
        "explanation": (
            "CSRF exploits the browser's automatic inclusion of session cookies on any request to a site the "
            "user is authenticated to, regardless of where the request originated. Anti-CSRF tokens (unique, "
            "unpredictable, validated server-side) and SameSite cookie attributes are the standard mitigations."
        ),
    },
    {
        "id": "nd4j-005",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Application security",
        "stem": (
            "An online store's checkout page calculates the final order total in JavaScript running in the "
            "browser, then submits that JavaScript-calculated total as a hidden form field when 'Place Order' is "
            "clicked; the server charges the submitted amount without independently recalculating it. A "
            "researcher demonstrates that editing the hidden field in browser developer tools allows purchasing "
            "items for $0.01. What is the root cause, and how should it be fixed?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The server trusts client-supplied pricing instead of recalculating the total from the "
                    "authoritative product catalog and quantities server-side; fix by performing all pricing "
                    "calculations on the server and ignoring/validating any client-submitted price field"
                ),
                "correct": True,
                "rationale": (
                    "Correct. The flaw is a broken trust boundary: a security-relevant value (price) is accepted "
                    "from the client instead of being independently derived server-side, which is the only "
                    "reliable fix."
                ),
            },
            {
                "id": "b",
                "text": "The application is vulnerable to SQL injection because the price field is not parameterized",
                "correct": False,
                "rationale": (
                    "Incorrect. Nothing indicates malicious SQL syntax or query manipulation; the flaw is trusting "
                    "an unvalidated client-supplied value for a security-relevant decision, which is a business-"
                    "logic/broken-access-control issue, not an injection flaw."
                ),
            },
            {
                "id": "c",
                "text": "The checkout page needs HTTPS enabled to prevent this manipulation",
                "correct": False,
                "rationale": (
                    "Incorrect. TLS protects data in transit from third-party eavesdropping/tampering, but the "
                    "shopper is legitimately modifying their own request locally before it is even sent; "
                    "encryption does not stop a client from choosing what value to submit."
                ),
            },
            {
                "id": "d",
                "text": "Add client-side JavaScript validation to reject negative or unusually low totals before submission",
                "correct": False,
                "rationale": (
                    "Incorrect. Client-side validation executes in the attacker's own browser and can be trivially "
                    "bypassed or disabled; it provides no real security guarantee without server-side enforcement."
                ),
            },
        ],
        "explanation": (
            "Any value that determines a security- or business-critical outcome — such as price — must be "
            "authoritatively computed and verified on the server. Trusting client-submitted values for such "
            "decisions is a classic business-logic vulnerability regardless of transport encryption or client-"
            "side checks."
        ),
    },
    {
        "id": "nd4j-006",
        "domain": 4,
        "objective": "4.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Asset management",
        "stem": (
            "A university's device inventory shows 3,000 registered devices, but a passive network traffic "
            "capture identifies over 4,500 unique MAC addresses actively communicating on the network. Which "
            "practice would BEST close this asset visibility gap going forward?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Deploy continuous, automated asset discovery (e.g., passive network monitoring or NAC "
                    "integration) that reconciles newly observed devices against the CMDB in real time and flags "
                    "unregistered devices for review"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Continuous automated discovery reconciled against the CMDB is the control "
                    "specifically designed to catch unregistered devices as they connect, closing the gap on an "
                    "ongoing basis rather than as a one-time fix."
                ),
            },
            {
                "id": "b",
                "text": "Conduct a single comprehensive manual inventory audit this year to correct the current count",
                "correct": False,
                "rationale": (
                    "Incorrect. A one-time manual audit corrects today's discrepancy but does not close the "
                    "ongoing visibility gap as new unregistered devices continue to connect afterward."
                ),
            },
            {
                "id": "c",
                "text": "Require every new device purchase to go through a formal procurement request form",
                "correct": False,
                "rationale": (
                    "Incorrect. Procurement paperwork does not detect devices that bypass procurement entirely "
                    "(personal devices, unauthorized purchases), which is the actual gap the traffic capture "
                    "revealed."
                ),
            },
            {
                "id": "d",
                "text": "Increase the frequency of vulnerability scans against IP addresses already listed in the CMDB",
                "correct": False,
                "rationale": (
                    "Incorrect. Scanning only addresses already in the CMDB does nothing to discover the roughly "
                    "1,500 devices that were never recorded there in the first place."
                ),
            },
        ],
        "explanation": (
            "Asset visibility gaps are best closed by continuously reconciling the system of record (CMDB) "
            "against independent, automated ground truth such as passive network discovery or NAC, which "
            "surfaces unregistered devices as they appear rather than relying on periodic manual efforts."
        ),
    },
    {
        "id": "nd4j-007",
        "domain": 4,
        "objective": "4.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Asset management",
        "stem": (
            "Six months after an employee's departure, IT discovers their laptop was never reassigned or "
            "deactivated in the asset inventory: it still lists the former employee as the responsible owner, "
            "has not received security patches since their last day, and nobody currently monitors its "
            "compliance status. Which asset management practice would MOST directly have prevented this device "
            "from becoming orphaned?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Enforce a formal offboarding workflow that reassigns or retires each departing employee's "
                    "assets — updating ownership, patch responsibility, and compliance monitoring — as a "
                    "mandatory step tied to HR termination processing"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Tying asset reassignment/retirement directly to the HR termination process ensures "
                    "no device is left orphaned with a stale owner and no active patch or compliance monitoring."
                ),
            },
            {
                "id": "b",
                "text": "Require the employee to sign an acceptable use policy (AUP) at the time the laptop was originally issued",
                "correct": False,
                "rationale": (
                    "Incorrect. An AUP governs how the device may be used while assigned; it has no bearing on "
                    "what happens to asset ownership records after the user departs."
                ),
            },
            {
                "id": "c",
                "text": "Enable full-disk encryption on all corporate laptops",
                "correct": False,
                "rationale": (
                    "Incorrect. Disk encryption protects data confidentiality if the device is lost or stolen but "
                    "does nothing to update ownership assignment or trigger patch/compliance monitoring after an "
                    "employee leaves."
                ),
            },
            {
                "id": "d",
                "text": "Apply a physical asset tag with a barcode to the laptop during initial provisioning",
                "correct": False,
                "rationale": (
                    "Incorrect. A barcode tag aids physical identification and tracking but does not itself "
                    "trigger any process to reassign ownership or resume monitoring when an employee departs."
                ),
            },
        ],
        "explanation": (
            "Asset lifecycle management requires ownership and monitoring responsibilities to be actively "
            "transitioned whenever personnel changes occur; the most direct control is integrating asset "
            "reassignment into the mandatory HR offboarding workflow itself."
        ),
    },
    {
        "id": "nd4j-008",
        "domain": 4,
        "objective": "4.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Automation & orchestration",
        "stem": (
            "A SOAR playbook that blocks an attacker's IP address at the perimeter firewall runs multiple times "
            "for the same alert due to platform retries after transient API timeouts. Each run inadvertently "
            "creates a new duplicate firewall rule entry rather than reusing an existing one, and the firewall's "
            "rule table eventually approaches its capacity limit. Which practice would BEST prevent this?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Design the playbook action to first check whether the target block rule already exists "
                    "before creating a new one, making the action idempotent so repeated runs have no additional "
                    "effect"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Idempotent design is the standard fix for automation that may run more than once "
                    "for the same event — checking for an existing state before acting prevents duplicate side "
                    "effects regardless of how many times the action executes."
                ),
            },
            {
                "id": "b",
                "text": "Disable all automatic retries in the SOAR platform so each playbook run executes exactly once",
                "correct": False,
                "rationale": (
                    "Incorrect. Disabling retries removes resiliency against transient failures like API timeouts "
                    "and does not address the underlying problem that the action itself is not safe to repeat; it "
                    "trades one risk for another rather than fixing the root cause."
                ),
            },
            {
                "id": "c",
                "text": "Increase the SIEM alert threshold so the triggering correlation rule fires less often",
                "correct": False,
                "rationale": (
                    "Incorrect. Reducing alert frequency does not fix the playbook action itself, which would "
                    "still create duplicate entries whenever it legitimately runs more than once, such as during "
                    "a retried step."
                ),
            },
            {
                "id": "d",
                "text": "Assign an analyst to manually review and delete duplicate firewall rules once per week",
                "correct": False,
                "rationale": (
                    "Incorrect. This is a reactive manual workaround for symptoms rather than a fix to the "
                    "playbook's design, and duplicate rules could still exceed capacity limits between weekly "
                    "cleanups."
                ),
            },
        ],
        "explanation": (
            "Automated response actions should be built to be idempotent — safe to execute repeatedly without "
            "unintended cumulative side effects — since retries, re-triggers, and duplicate alerts are common in "
            "production SOAR environments."
        ),
    },
    {
        "id": "nd4j-009",
        "domain": 4,
        "objective": "4.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Automation & orchestration",
        "stem": (
            "After deploying SOAR-driven automatic alert triage, analysts increasingly approve the tool's "
            "recommended verdict without independently reviewing the underlying evidence, even when the "
            "recommendation later turns out to be wrong. Which risk of automation does this behavior BEST "
            "describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Automation bias",
                "correct": True,
                "rationale": (
                    "Correct. Automation bias describes analysts over-trusting an automated system's output and "
                    "reducing their own critical review, even when the tool's verdict is incorrect — exactly the "
                    "behavior described."
                ),
            },
            {
                "id": "b",
                "text": "Alert fatigue",
                "correct": False,
                "rationale": (
                    "Incorrect. Alert fatigue describes desensitization from excessive alert volume that causes "
                    "alerts to be ignored or missed, not the pattern of actively (if uncritically) accepting an "
                    "automated tool's verdict."
                ),
            },
            {
                "id": "c",
                "text": "Scope creep",
                "correct": False,
                "rationale": (
                    "Incorrect. Scope creep describes uncontrolled growth in a project's requirements or "
                    "features, unrelated to analysts trusting an existing tool's output without review."
                ),
            },
            {
                "id": "d",
                "text": "A false positive",
                "correct": False,
                "rationale": (
                    "Incorrect. A false positive describes one specific incorrect verdict, not the broader "
                    "behavioral pattern of analysts systematically failing to critically review any of the tool's "
                    "verdicts, correct or not."
                ),
            },
        ],
        "explanation": (
            "Automation bias is a recognized risk of introducing SOAR/automated decision support: humans tend to "
            "defer to automated recommendations and reduce independent verification, which can let incorrect "
            "automated verdicts go unchallenged."
        ),
    },
    {
        "id": "nd4j-010",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Digital forensics",
        "stem": (
            "A first responder seizes a suspect's smartphone that is powered on, unlocked, and actively "
            "connected to the cellular network. The responder's greatest immediate concern is that the device "
            "owner or an accomplice could trigger a remote wipe or receive incoming communications that alter "
            "the device's state before it reaches the forensic lab. What should the responder do immediately to "
            "isolate the device from all wireless signals without powering it off?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Place the device into a Faraday bag (RF-shielded enclosure) to block all cellular, Wi-Fi, "
                    "and Bluetooth signals while keeping it powered on for later extraction"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A Faraday enclosure physically blocks all wireless signals without requiring any "
                    "interaction with the device's software, preserving both its powered-on state and its "
                    "current evidentiary condition."
                ),
            },
            {
                "id": "b",
                "text": "Immediately power off the device to prevent any further network communication",
                "correct": False,
                "rationale": (
                    "Incorrect. Powering off can trigger re-encryption/re-locking, lose data held only in "
                    "volatile memory, and require additional authentication on restart, potentially destroying "
                    "accessible evidence; isolating signal while leaving it powered on is generally preferred."
                ),
            },
            {
                "id": "c",
                "text": "Enable airplane mode through the device's unlocked settings menu before transport",
                "correct": False,
                "rationale": (
                    "Incorrect. Interacting with the unlocked device's UI to change settings risks altering "
                    "evidence (app states, timestamps, triggering security prompts) and is not forensically "
                    "sound; a Faraday enclosure isolates signal without touching the device's software state."
                ),
            },
            {
                "id": "d",
                "text": "Leave the device connected to the network but photograph the screen for documentation before transport",
                "correct": False,
                "rationale": (
                    "Incorrect. Leaving the device connected preserves the exact risk described — remote wipe or "
                    "incoming communications altering state. Photographing the screen is good practice but does "
                    "not address signal isolation."
                ),
            },
        ],
        "explanation": (
            "Faraday bags/enclosures are the standard forensic tool for isolating a powered-on mobile device from "
            "all wireless signals, preventing remote wipe or state-altering communications while avoiding the "
            "evidentiary risks of powering off or interacting with the unlocked device."
        ),
    },
    {
        "id": "nd4j-011",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Digital forensics",
        "stem": (
            "A forensic examiner runs the same disk image through two independently developed and separately "
            "validated forensic tools and confirms that both tools recover identical artifacts and calculate "
            "identical hash values for the acquired image. Which forensic principle does this practice BEST "
            "satisfy?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Tool validation and corroboration of findings",
                "correct": True,
                "rationale": (
                    "Correct. Running independent, separately validated tools against the same evidence and "
                    "confirming matching results strengthens confidence that the findings reflect the evidence "
                    "itself rather than a tool-specific bug or error."
                ),
            },
            {
                "id": "b",
                "text": "Order of volatility",
                "correct": False,
                "rationale": (
                    "Incorrect. Order of volatility concerns the sequence in which volatile data should be "
                    "collected before it is lost, not the practice of cross-validating results between two "
                    "already-acquired, static forensic tools."
                ),
            },
            {
                "id": "c",
                "text": "Chain of custody",
                "correct": False,
                "rationale": (
                    "Incorrect. Chain of custody tracks physical/logical custody transfers of the evidence "
                    "itself; it does not address whether the analysis methodology or tooling produced reliable, "
                    "corroborated results."
                ),
            },
            {
                "id": "d",
                "text": "Legal hold",
                "correct": False,
                "rationale": (
                    "Incorrect. A legal hold is a preservation obligation triggered by anticipated litigation; it "
                    "has nothing to do with validating forensic tool output through independent corroboration."
                ),
            },
        ],
        "explanation": (
            "Corroborating results with a second, independently validated tool is a recognized best practice for "
            "demonstrating that forensic findings are reliable and reproducible, strengthening their credibility "
            "if challenged."
        ),
    },
    {
        "id": "nd4j-012",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Digital forensics and chain-of-custody process",
        "stem": (
            "A chain-of-custody form lists a seizure date of March 3 for a piece of digital evidence, but the "
            "actual seizure — confirmed by the responding officer's body-camera timestamp and incident report — "
            "occurred on March 4. Defense counsel raises the one-day discrepancy as grounds to challenge the "
            "evidence's integrity. What is the appropriate way to handle this documentation error?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The original custodian documents a signed, dated correction/addendum explaining the "
                    "discrepancy and referencing the corroborating evidence, preserving the original form rather "
                    "than altering or destroying it"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A transparent, signed correction that references corroborating evidence preserves "
                    "the auditability of the record while accurately resolving the clerical error."
                ),
            },
            {
                "id": "b",
                "text": "Quietly white-out and rewrite the date on the original chain-of-custody form",
                "correct": False,
                "rationale": (
                    "Incorrect. Altering an existing evidentiary record after the fact without a transparent, "
                    "documented correction creates the appearance of tampering and can itself be used to "
                    "challenge the integrity of the entire chain."
                ),
            },
            {
                "id": "c",
                "text": "Discard the original form and generate a new one with the corrected date, backdated to the original creation date",
                "correct": False,
                "rationale": (
                    "Incorrect. Destroying the original record and backdating a replacement is far more damaging "
                    "to admissibility than a simple date discrepancy; it removes the audit trail entirely and "
                    "constitutes falsification."
                ),
            },
            {
                "id": "d",
                "text": "Exclude the evidence from the case rather than risk any challenge to its integrity",
                "correct": False,
                "rationale": (
                    "Incorrect. A minor, well-corroborated clerical date discrepancy does not require abandoning "
                    "otherwise legitimately obtained evidence; transparent correction is the proportionate, "
                    "standard response."
                ),
            },
        ],
        "explanation": (
            "Chain-of-custody documentation errors should be corrected transparently through a signed addendum "
            "that preserves the original record, rather than altered, destroyed, or hidden — either of which "
            "would create a far stronger basis to challenge admissibility than the original clerical mistake."
        ),
    },
    {
        "id": "nd4j-013",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Digital forensics and chain-of-custody process",
        "stem": (
            "A cloud-based evidence management platform automatically records a timestamped, immutable log "
            "entry — including the accessing user's identity and a freshly computed cryptographic hash of the "
            "file — every time anyone views, downloads, or exports a piece of digital evidence, and compares "
            "that hash against the value recorded at intake. Which chain-of-custody objective does this "
            "platform primarily support?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Maintaining an unbroken, non-repudiable record of every access to the evidence while "
                    "continuously verifying that the evidence itself remains unaltered"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Automatically logging who accessed the evidence and when, combined with continuous "
                    "hash verification, is exactly what supports an unbroken, verifiable custody record."
                ),
            },
            {
                "id": "b",
                "text": "Establishing the order of volatility for evidence collection priorities",
                "correct": False,
                "rationale": (
                    "Incorrect. Order of volatility is a collection-phase concept about which data to capture "
                    "first due to how quickly it degrades; it has no relationship to an access-logging and hash-"
                    "verification platform used after acquisition."
                ),
            },
            {
                "id": "c",
                "text": "Satisfying a litigation hold obligation to preserve data",
                "correct": False,
                "rationale": (
                    "Incorrect. A litigation hold is a preservation directive triggered by anticipated legal "
                    "action; automatically logging access and verifying hashes on already-preserved evidence is "
                    "a custody/integrity control, not the hold itself."
                ),
            },
            {
                "id": "d",
                "text": "Minimizing the total volume of data collected during acquisition",
                "correct": False,
                "rationale": (
                    "Incorrect. Data minimization concerns limiting what is collected in the first place; this "
                    "platform's automated access logging and hash verification apply to evidence that has "
                    "already been acquired and stored."
                ),
            },
        ],
        "explanation": (
            "An automated, tamper-evident access log combined with continuous hash verification directly "
            "supports the two core chain-of-custody goals: an unbroken accountability trail and proof that the "
            "evidence remains unaltered."
        ),
    },
    {
        "id": "nd4j-014",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "EDR/XDR & DLP",
        "stem": (
            "A SOC analyst uses the EDR console to search all endpoints for a specific file hash observed on "
            "one compromised host, in order to determine how many other machines have seen or executed that "
            "same file historically. Which EDR capability is being used?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Retrospective detection / historical telemetry search across the fleet",
                "correct": True,
                "rationale": (
                    "Correct. Querying previously collected telemetry across every endpoint for a specific "
                    "indicator, such as a file hash, to determine the true scope of exposure is a retrospective, "
                    "historical-search capability."
                ),
            },
            {
                "id": "b",
                "text": "Real-time behavioral process blocking on the affected endpoint",
                "correct": False,
                "rationale": (
                    "Incorrect. Real-time blocking acts on current, in-the-moment activity; it does not search "
                    "historical telemetry across other endpoints for a hash observed on one host."
                ),
            },
            {
                "id": "c",
                "text": "Sandbox detonation of a suspicious file in an isolated environment",
                "correct": False,
                "rationale": (
                    "Incorrect. Sandbox detonation analyzes an unknown file's behavior in isolation; it is not "
                    "the mechanism for querying historical, already-collected telemetry from endpoints across "
                    "the fleet."
                ),
            },
            {
                "id": "d",
                "text": "Removable media device control policy enforcement",
                "correct": False,
                "rationale": (
                    "Incorrect. Device control governs peripheral usage policy and has no relationship to "
                    "searching historical endpoint telemetry for a specific file hash."
                ),
            },
        ],
        "explanation": (
            "Modern EDR platforms retain historical telemetry that can be queried retrospectively for a given "
            "indicator (hash, filename, registry key) across the entire fleet, enabling analysts to scope how "
            "widely a threat has spread beyond the initially identified host."
        ),
    },
    {
        "id": "nd4j-015",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "EDR/XDR & DLP",
        "stem": (
            "A company wants to scan files already stored at rest inside a sanctioned SaaS application (e.g., a "
            "cloud file-sharing platform) for exposed PII, without inspecting real-time traffic to and from the "
            "application. Which CASB deployment mode is appropriate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "API-based (out-of-band) CASB deployment",
                "correct": True,
                "rationale": (
                    "Correct. An API-based CASB connects directly to the SaaS application's API to scan files "
                    "already stored at rest, without needing to be positioned in the live traffic path."
                ),
            },
            {
                "id": "b",
                "text": "Forward proxy inline CASB",
                "correct": False,
                "rationale": (
                    "Incorrect. A forward proxy must sit inline in the traffic path to inspect requests as they "
                    "happen; it is not designed to scan files already sitting at rest inside a SaaS app's "
                    "existing storage."
                ),
            },
            {
                "id": "c",
                "text": "Reverse proxy CASB",
                "correct": False,
                "rationale": (
                    "Incorrect. Like the forward proxy, a reverse proxy inspects traffic in transit to the "
                    "application; it does not natively enumerate and scan the full existing corpus of files "
                    "already stored in the app."
                ),
            },
            {
                "id": "d",
                "text": "Endpoint DLP agent installed on managed devices",
                "correct": False,
                "rationale": (
                    "Incorrect. An endpoint agent only sees activity occurring on the device it's installed on; "
                    "it cannot scan files already stored inside a cloud SaaS application's backend."
                ),
            },
        ],
        "explanation": (
            "API-based CASB deployment connects out-of-band to a SaaS provider's API, letting it enumerate and "
            "scan data already at rest for policy violations, unlike proxy-based modes that only see traffic in "
            "transit or endpoint agents scoped to a single device."
        ),
    },
    {
        "id": "nd4j-016",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Email security (SPF/DKIM/DMARC)",
        "stem": (
            "A company's outbound mail server IP resolves via forward DNS to mail.company.com, but a reverse "
            "DNS (PTR) lookup on that same IP returns a generic hostname assigned by the hosting ISP. SPF and "
            "DKIM both pass for the company's mail, yet several receiving mail systems still flag the messages "
            "as spam. Which additional practice should be corrected?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Configure a reverse DNS (PTR) record for the sending mail server's IP that resolves to a "
                    "hostname matching the sending domain, since many receiving systems use forward-confirmed "
                    "reverse DNS as an independent anti-spam signal"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Forward-confirmed reverse DNS (a matching PTR record) is a widely used spam-"
                    "filtering signal independent of SPF/DKIM/DMARC; a mismatched or generic PTR record can "
                    "trigger spam flagging even when authentication passes."
                ),
            },
            {
                "id": "b",
                "text": "Add another 'include' mechanism to the SPF record for the same sending IP that is already authorized",
                "correct": False,
                "rationale": (
                    "Incorrect. The sending IP is already authorized in SPF, which is passing; adding a redundant "
                    "include does nothing to fix the mismatched, generic reverse-DNS hostname triggering spam "
                    "filtering."
                ),
            },
            {
                "id": "c",
                "text": "Publish an additional DKIM selector using a longer key length",
                "correct": False,
                "rationale": (
                    "Incorrect. DKIM is already passing in this scenario; a longer key improves cryptographic "
                    "strength but does not address the unrelated reverse-DNS/PTR mismatch causing the spam-filter "
                    "flag."
                ),
            },
            {
                "id": "d",
                "text": "Lower the DMARC 'pct' tag so enforcement only applies to a percentage of messages",
                "correct": False,
                "rationale": (
                    "Incorrect. The 'pct' tag controls what fraction of failing messages receive the declared "
                    "DMARC policy action; it does not affect SPF, DKIM, or PTR/reverse-DNS evaluation and does "
                    "not fix this issue."
                ),
            },
        ],
        "explanation": (
            "Reverse DNS (PTR) validation is a common anti-spam signal used alongside, but independent of, SPF/"
            "DKIM/DMARC. A generic or mismatched PTR record can cause spam filtering even when all three "
            "authentication mechanisms pass."
        ),
    },
    {
        "id": "nd4j-017",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Email security (SPF/DKIM/DMARC)",
        "stem": (
            "A company's DMARC record specifies 'aspf=s' (strict SPF alignment). A message is sent with a "
            "visible From: header of 'billing@company.com,' relayed through a third-party biller using an "
            "envelope sender of 'bounce@billing.company.com' (a subdomain), which passes SPF authorization for "
            "the sending IP. The message still fails DMARC. Why?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Under strict SPF alignment, the SPF-authenticated domain must exactly match the visible "
                    "From: header domain; a subdomain such as billing.company.com does not exactly match "
                    "company.com, so alignment fails even though SPF itself passed"
                ),
                "correct": True,
                "rationale": (
                    "Correct. 'aspf=s' requires an exact domain match between the RFC5321.MailFrom domain and "
                    "the RFC5322.From domain. A subdomain relationship only satisfies relaxed alignment, so "
                    "strict mode causes DMARC to fail despite SPF passing on its own."
                ),
            },
            {
                "id": "b",
                "text": "DMARC ignores SPF alignment entirely and only strict-aligns DKIM signatures",
                "correct": False,
                "rationale": (
                    "Incorrect. DMARC evaluates alignment for both SPF (aspf) and DKIM (adkim) independently, "
                    "each with its own strict/relaxed setting; SPF alignment mode is very much in effect here."
                ),
            },
            {
                "id": "c",
                "text": "The message failed because SPF itself returned a hard fail (-all) for the sending IP",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario states SPF passed for the sending infrastructure; the failure is "
                    "specifically a DMARC alignment failure (domain match), not an SPF authorization result."
                ),
            },
            {
                "id": "d",
                "text": "Strict alignment mode only applies to messages sent from outside the organization's own infrastructure",
                "correct": False,
                "rationale": (
                    "Incorrect. Alignment mode is not scoped to internal-versus-external senders; it applies "
                    "uniformly to how closely the authenticated domain must match the visible From: domain."
                ),
            },
        ],
        "explanation": (
            "DMARC alignment (strict vs. relaxed) is separate from SPF/DKIM pass/fail. Strict mode ('s') demands "
            "an exact domain match, so subdomain-based sending infrastructure that passes SPF on its own can "
            "still fail DMARC unless relaxed alignment is used or the exact domain matches."
        ),
    },
    {
        "id": "nd4j-018",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Federation & SSO (SAML/OAuth)",
        "stem": (
            "A user bookmarks a direct link to a SaaS application's dashboard. When clicked without first "
            "visiting the identity provider's portal, the user is redirected to authenticate at the IdP, and "
            "afterward lands back on the intended dashboard page rather than a generic homepage — thanks to "
            "preservation of the original destination via a RelayState parameter. Which SSO flow does this "
            "describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "SP-initiated SSO",
                "correct": True,
                "rationale": (
                    "Correct. In SP-initiated SSO, the user starts at the service provider (via the bookmarked "
                    "link), is redirected to the IdP to authenticate, and the original destination URL is "
                    "preserved via RelayState so the user returns to the intended page after login."
                ),
            },
            {
                "id": "b",
                "text": "IdP-initiated SSO",
                "correct": False,
                "rationale": (
                    "Incorrect. That flow begins at the identity provider's portal, where the user selects the "
                    "application from a list of tiles and typically lands on a default page, not by starting at "
                    "a bookmarked SP deep link and preserving that destination via RelayState."
                ),
            },
            {
                "id": "c",
                "text": "OAuth 2.0 implicit grant flow",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario describes preserving a destination URL during a SAML-style browser "
                    "redirect to authenticate, not the mechanics of an OAuth token grant type."
                ),
            },
            {
                "id": "d",
                "text": "Kerberos constrained delegation",
                "correct": False,
                "rationale": (
                    "Incorrect. Kerberos delegation is a domain-based, ticket-impersonation mechanism for backend "
                    "service calls, unrelated to browser-based SSO redirects preserving a bookmarked destination "
                    "via RelayState."
                ),
            },
        ],
        "explanation": (
            "SP-initiated SSO begins with the user requesting a resource directly from the service provider; the "
            "SP redirects to the IdP for authentication and uses RelayState to remember and restore the original "
            "destination after login completes."
        ),
    },
    {
        "id": "nd4j-019",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Federation & SSO (SAML/OAuth)",
        "stem": (
            "Select TWO true statements about how SAML and OAuth 2.0 help prevent authentication assertions or "
            "tokens from being captured and replayed by an attacker."
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "SAML assertions include a bounded validity window (NotBefore/NotOnOrAfter conditions) and a "
                    "unique assertion ID, allowing a service provider to reject assertions that are expired or "
                    "have already been processed."
                ),
                "correct": True,
                "rationale": (
                    "Correct. SAML's Conditions element defines a time-bounded validity window, and assertion "
                    "IDs allow a service provider to detect and reject reuse of an already-processed assertion."
                ),
            },
            {
                "id": "b",
                "text": (
                    "A service provider should validate an assertion's Audience Restriction to confirm it was "
                    "issued specifically for that service provider, preventing an assertion obtained for one SP "
                    "from being replayed against a different SP."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Audience Restriction binds an assertion to a specific intended recipient; checking "
                    "it prevents an assertion legitimately issued for one application from being reused against "
                    "an unrelated one."
                ),
            },
            {
                "id": "c",
                "text": "SAML assertions have no timestamp or expiration fields, so replay protection must be implemented entirely outside the SAML standard.",
                "correct": False,
                "rationale": (
                    "Incorrect. SAML's Conditions element natively defines NotBefore/NotOnOrAfter validity "
                    "windows; timestamp-based expiration is part of the standard itself, not something bolted on "
                    "externally."
                ),
            },
            {
                "id": "d",
                "text": "Because OAuth 2.0 access tokens never expire, replay protection is unnecessary for federated authorization flows.",
                "correct": False,
                "rationale": (
                    "Incorrect. OAuth 2.0 access tokens are explicitly designed to be short-lived and expire "
                    "(often paired with refresh tokens); replay protection remains a relevant concern, and this "
                    "statement is factually wrong on both points."
                ),
            },
        ],
        "explanation": (
            "SAML mitigates replay through time-bounded validity windows, unique assertion IDs, and audience "
            "restriction checks; OAuth 2.0 access tokens are intentionally short-lived. Both standards build in "
            "explicit mechanisms against replay rather than leaving it unaddressed."
        ),
    },
    {
        "id": "nd4j-020",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Hardening & secure baselines",
        "stem": (
            "A finance workstation cluster must prevent execution of any unauthorized or unsigned executable — "
            "even if a user with local administrator rights attempts to run it — while still allowing a known, "
            "digitally signed list of approved business applications to run normally. Which control BEST "
            "enforces this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Application allowlisting (application control)",
                "correct": True,
                "rationale": (
                    "Correct. Application allowlisting enforces a default-deny posture where only explicitly "
                    "approved, signed applications are permitted to execute, blocking everything else regardless "
                    "of the user's privilege level."
                ),
            },
            {
                "id": "b",
                "text": "Signature-based antivirus scanning",
                "correct": False,
                "rationale": (
                    "Incorrect. Signature-based AV is reactive and only catches known threats; it does not "
                    "inherently block execution of arbitrary unauthorized-but-not-yet-flagged executables the "
                    "way a default-deny allowlist does."
                ),
            },
            {
                "id": "c",
                "text": "A host-based firewall restricting inbound and outbound network connections",
                "correct": False,
                "rationale": (
                    "Incorrect. A host firewall controls network traffic to/from the machine; it does not "
                    "control which local executables are permitted to run, regardless of privilege level."
                ),
            },
            {
                "id": "d",
                "text": "A monthly patch management cycle applying vendor security updates",
                "correct": False,
                "rationale": (
                    "Incorrect. Patch management addresses known vulnerabilities in installed software; it does "
                    "not prevent execution of unauthorized or unsigned programs a user attempts to run."
                ),
            },
        ],
        "explanation": (
            "Application allowlisting enforces a default-deny model at the execution level, blocking anything "
            "not explicitly approved regardless of the invoking user's privilege — the only listed control that "
            "directly satisfies the requirement described."
        ),
    },
    {
        "id": "nd4j-021",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Hardening & secure baselines",
        "stem": (
            "A vulnerability scan of the corporate network's multi-function printers finds several with default "
            "web management interfaces exposed via unencrypted HTTP on the default port, using vendor-default "
            "administrative credentials, with unnecessary FTP and Telnet services still enabled. What is the "
            "BEST consolidated remediation?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Apply a documented hardening baseline to the printers: change default administrative "
                    "credentials, disable unused services such as FTP and Telnet, and require HTTPS for the "
                    "management interface"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A consolidated hardening baseline addresses all three identified weaknesses — "
                    "default credentials, unnecessary cleartext services, and unencrypted management access — "
                    "in one coordinated remediation."
                ),
            },
            {
                "id": "b",
                "text": "Only change the default administrator password and leave the remaining default services enabled",
                "correct": False,
                "rationale": (
                    "Incorrect. This addresses just one of three identified weaknesses; the unencrypted HTTP "
                    "management interface and unnecessary FTP/Telnet services would remain exposed."
                ),
            },
            {
                "id": "c",
                "text": "Disable Telnet only, since FTP is required for standard printer operation",
                "correct": False,
                "rationale": (
                    "Incorrect. FTP is not required for standard printer operation in virtually any modern "
                    "deployment and, left enabled with default settings, remains an unauthenticated/cleartext "
                    "attack surface just like Telnet."
                ),
            },
            {
                "id": "d",
                "text": "Install endpoint antivirus software directly on each printer's embedded operating system",
                "correct": False,
                "rationale": (
                    "Incorrect. Most multi-function printer embedded operating systems do not support installing "
                    "general-purpose endpoint antivirus agents, and doing so would not remediate exposed default "
                    "credentials or unnecessary cleartext management services."
                ),
            },
        ],
        "explanation": (
            "Network-attached peripherals like printers are commonly overlooked hardening targets. A complete "
            "baseline addresses default credentials, disables unnecessary cleartext services, and enforces "
            "encrypted management access all at once."
        ),
    },
    {
        "id": "nd4j-022",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Incident response process",
        "stem": (
            "A SOC receives an alert but has not yet confirmed whether it represents a true positive, "
            "determined its scope, or assessed its severity. Per the standard incident response lifecycle, "
            "what should the team do before taking any containment action?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Complete detection and analysis — validate that the alert represents a genuine incident and "
                    "determine its scope and severity — before deciding on and executing containment actions"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Detection and analysis (triage, validation, scoping, severity assessment) must "
                    "precede containment so that containment actions are proportionate and correctly targeted."
                ),
            },
            {
                "id": "b",
                "text": "Immediately isolate every host in the environment as a precaution",
                "correct": False,
                "rationale": (
                    "Incorrect. Isolating the entire environment before scope/severity is established causes "
                    "unnecessary, widespread business disruption and is disproportionate to an unvalidated, "
                    "single alert."
                ),
            },
            {
                "id": "c",
                "text": "Notify law enforcement before the security team has confirmed whether the alert is a true positive",
                "correct": False,
                "rationale": (
                    "Incorrect. Engaging external law enforcement is typically a decision made once an incident "
                    "is validated and its severity/legal implications are understood, not before initial triage."
                ),
            },
            {
                "id": "d",
                "text": "Begin executing eradication scripts to remove the suspected malware immediately",
                "correct": False,
                "rationale": (
                    "Incorrect. Eradication follows containment in the IR lifecycle and, more fundamentally, "
                    "should not begin before the team has even confirmed what — if anything — is actually "
                    "happening."
                ),
            },
        ],
        "explanation": (
            "The IR lifecycle requires detection and analysis to validate, scope, and prioritize an alert before "
            "any containment, eradication, or recovery action is taken, ensuring the response is proportionate "
            "and correctly targeted."
        ),
    },
    {
        "id": "nd4j-023",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Incident response process",
        "stem": (
            "During an investigation into suspected insider data theft by a specific employee, the IR team must "
            "decide who to notify about the ongoing investigation. Broadly announcing the investigation to the "
            "employee's entire department risks the suspect destroying evidence or fleeing before evidence "
            "collection is complete. Which practice should the IR team follow?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Follow the organization's incident communications plan to restrict investigation details to "
                    "a defined, need-to-know list (e.g., legal, HR, senior IR leadership) until evidence is "
                    "secured"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A well-defined communications plan restricts sensitive investigation details to a "
                    "need-to-know group, protecting evidence integrity while still looping in the roles (legal, "
                    "HR, leadership) required for proper handling."
                ),
            },
            {
                "id": "b",
                "text": "Send an all-staff email immediately describing the suspected employee and the nature of the investigation for transparency",
                "correct": False,
                "rationale": (
                    "Incorrect. Broad disclosure before evidence is secured directly creates the risk described "
                    "— the suspect destroying evidence or fleeing — and could expose the organization to "
                    "defamation risk if the suspicion is later unfounded."
                ),
            },
            {
                "id": "c",
                "text": "Wait until the post-incident lessons-learned meeting to inform anyone besides the IR team",
                "correct": False,
                "rationale": (
                    "Incorrect. Legal, HR, and appropriate leadership generally need to be looped in during the "
                    "investigation itself (for evidence handling, employment actions, and legal privilege), not "
                    "only after the incident is fully closed."
                ),
            },
            {
                "id": "d",
                "text": "Post an anonymous internal bulletin describing the incident without naming individuals, sent department-wide",
                "correct": False,
                "rationale": (
                    "Incorrect. Even an anonymized department-wide bulletin about an active insider-theft "
                    "investigation can tip off the suspect that they are under scrutiny, defeating the purpose "
                    "of restricting disclosure."
                ),
            },
        ],
        "explanation": (
            "A defined incident communications plan restricts sensitive details to a need-to-know group during "
            "an active investigation, balancing evidence preservation and legal/HR requirements against the risk "
            "of premature or overly broad disclosure."
        ),
    },
    {
        "id": "nd4j-024",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log data sources",
        "stem": (
            "An analyst needs to know the exact byte-for-byte payload exchanged during a suspicious session "
            "between an internal host and an external IP address, not just connection metadata. Which data "
            "source is required, and what is a key limitation compared to NetFlow logs?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Full packet capture (PCAP); it is far more storage-intensive than NetFlow, and if the "
                    "session is encrypted, the payload may still be unreadable without the decryption keys"
                ),
                "correct": True,
                "rationale": (
                    "Correct. PCAP records the complete payload of network traffic, unlike NetFlow, which "
                    "records only connection metadata. This comes at a significant storage cost, and encrypted "
                    "payloads remain unreadable without keys even when fully captured."
                ),
            },
            {
                "id": "b",
                "text": "NetFlow records, since they include the full payload of each session in addition to connection metadata",
                "correct": False,
                "rationale": (
                    "Incorrect. NetFlow explicitly does not contain payload data — only lightweight connection "
                    "metadata (source/destination, ports, timestamps, volume) — so it cannot fulfill the stated "
                    "requirement to see the exact content exchanged."
                ),
            },
            {
                "id": "c",
                "text": "Firewall connection logs, which record the same payload detail as full packet capture",
                "correct": False,
                "rationale": (
                    "Incorrect. Firewall logs typically capture allow/deny decisions and connection tuples "
                    "similar to NetFlow, not the full payload content of the session."
                ),
            },
            {
                "id": "d",
                "text": "DNS query logs, which record the complete data exchanged after a domain is resolved",
                "correct": False,
                "rationale": (
                    "Incorrect. DNS logs show name-resolution activity (which host requested which domain), not "
                    "the payload content of an established session between two hosts."
                ),
            },
        ],
        "explanation": (
            "Full packet capture is the only source that records complete session payloads, at the cost of high "
            "storage overhead and the fact that encrypted traffic remains unreadable without the relevant keys — "
            "unlike NetFlow, which is lightweight but metadata-only."
        ),
    },
    {
        "id": "nd4j-025",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log data sources",
        "stem": (
            "An analyst investigating unauthorized new administrator accounts wants to identify exactly when "
            "each account was created and by whom. Which Windows Security log event should the analyst search "
            "for?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Event ID 4720 ('A user account was created')",
                "correct": True,
                "rationale": (
                    "Correct. Filtering for Event ID 4720 and correlating the associated Subject fields "
                    "identifies exactly when each new account was created and which account performed the "
                    "action."
                ),
            },
            {
                "id": "b",
                "text": "Event ID 4624 ('An account was successfully logged on')",
                "correct": False,
                "rationale": (
                    "Incorrect. 4624 documents logon activity for existing accounts, not the creation of new "
                    "accounts, so it would not show when a new administrator account was created."
                ),
            },
            {
                "id": "c",
                "text": "Event ID 4648 ('A logon was attempted using explicit credentials')",
                "correct": False,
                "rationale": (
                    "Incorrect. 4648 tracks explicit-credential logon attempts, such as 'runas,' which is "
                    "unrelated to the specific action of creating a new user account."
                ),
            },
            {
                "id": "d",
                "text": "Event ID 1102 ('The audit log was cleared')",
                "correct": False,
                "rationale": (
                    "Incorrect. 1102 indicates the audit log was cleared — itself often a red flag for anti-"
                    "forensic activity — but it does not record account-creation events or who created them."
                ),
            },
        ],
        "explanation": (
            "Windows Security Event ID 4720 specifically logs account creation events, including the actor who "
            "performed the action, making it the authoritative log source for answering exactly when and by "
            "whom a new account was created."
        ),
    },
    {
        "id": "nd4j-026",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Malware classification",
        "stem": (
            "A malware sample changes its encryption key and outward byte-level appearance on every infection, "
            "while its underlying decryption routine and functional logic remain unchanged, defeating simple "
            "hash-based and static-signature detection. Which malware characteristic is this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Polymorphism",
                "correct": True,
                "rationale": (
                    "Correct. Polymorphic malware changes its encryption/encoding and outward appearance on "
                    "each infection while its underlying decryption routine and functional logic remain the "
                    "same, evading simple hash and static-signature matching."
                ),
            },
            {
                "id": "b",
                "text": "Metamorphism",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario explicitly states the underlying decryption routine and functional "
                    "logic remain unchanged; only the encryption key/appearance changes, which describes "
                    "polymorphism, not the more advanced code-rewriting behavior of metamorphic malware."
                ),
            },
            {
                "id": "c",
                "text": "A rootkit",
                "correct": False,
                "rationale": (
                    "Incorrect. Nothing in the scenario describes hiding processes/files from the OS or "
                    "privilege escalation; the described behavior is specifically about evading detection "
                    "through changing appearance."
                ),
            },
            {
                "id": "d",
                "text": "A worm",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario describes how the sample evades detection on each infection, not "
                    "its propagation mechanism; nothing indicates autonomous network self-replication."
                ),
            },
        ],
        "explanation": (
            "Polymorphic malware alters its encrypted/encoded appearance on each infection while keeping its "
            "core logic intact, specifically to defeat static hash- and signature-based detection — distinct "
            "from metamorphic malware, which rewrites its actual code and logic."
        ),
    },
    {
        "id": "nd4j-027",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Malware classification",
        "stem": (
            "A user installs a free video-converter utility that also silently installs a browser toolbar, "
            "which changes the default search engine and injects extra advertisements, but does not exfiltrate "
            "data or damage the system. How should this be classified?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A potentially unwanted program (PUP) / adware bundled with the installer",
                "correct": True,
                "rationale": (
                    "Correct. The software is installed alongside desired software, alters browser settings, "
                    "and injects ads without clear informed consent, but does not exfiltrate data or cause "
                    "direct system damage — the defining behavior of a PUP/adware."
                ),
            },
            {
                "id": "b",
                "text": "A trojan horse designed to establish covert remote access for an attacker",
                "correct": False,
                "rationale": (
                    "Incorrect. Nothing in the scenario indicates the software provides remote access or "
                    "attacker control; its behavior is consistent with intrusive-but-non-remote-controlled "
                    "bundled adware."
                ),
            },
            {
                "id": "c",
                "text": "Spyware collecting and exfiltrating the user's credentials",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario explicitly states the software does not exfiltrate data; credential "
                    "theft/exfiltration is not described."
                ),
            },
            {
                "id": "d",
                "text": "Ransomware that will eventually encrypt the user's files for payment",
                "correct": False,
                "rationale": (
                    "Incorrect. Nothing in the scenario describes file encryption or an extortion demand; the "
                    "described behavior is limited to intrusive advertising and browser hijacking."
                ),
            },
        ],
        "explanation": (
            "Software that is installed without clear consent and degrades the user experience (browser "
            "hijacking, unwanted ads) but does not exfiltrate data, damage systems, or grant remote access is "
            "classified as a potentially unwanted program (PUP) or adware."
        ),
    },
    {
        "id": "nd4j-028",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile device management",
        "stem": (
            "An organization wants to secure only the corporate email and productivity apps on employees' "
            "personal phones — wrapping them in a managed container — without gaining the ability to remotely "
            "wipe the entire device or view personal apps and photos. Which approach BEST fits this "
            "requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Mobile application management (MAM) with containerization",
                "correct": True,
                "rationale": (
                    "Correct. MAM wraps and manages only the corporate apps in an isolated container, applying "
                    "policy such as encryption and selective wipe of just the container, without enrolling or "
                    "controlling the entire personal device."
                ),
            },
            {
                "id": "b",
                "text": "Full MDM enrollment of the personal device",
                "correct": False,
                "rationale": (
                    "Incorrect. Full MDM enrollment typically grants the organization device-wide management "
                    "capabilities, including full-device wipe and visibility into installed apps — exactly what "
                    "the organization wants to avoid on personally owned phones."
                ),
            },
            {
                "id": "c",
                "text": "Corporate-owned, personally enabled (COPE)",
                "correct": False,
                "rationale": (
                    "Incorrect. COPE describes an ownership/provisioning model for organization-purchased "
                    "devices that also permit personal use; it does not apply here, since the devices are the "
                    "employees' own personal phones."
                ),
            },
            {
                "id": "d",
                "text": "Choose your own device (CYOD) from an approved hardware list",
                "correct": False,
                "rationale": (
                    "Incorrect. CYOD is a procurement model where the organization still owns/provisions the "
                    "device from an approved list; it doesn't fit a scenario about securing apps on devices "
                    "employees already personally own."
                ),
            },
        ],
        "explanation": (
            "MAM with containerization applies management and security policy only to a wrapped corporate app "
            "container, leaving the rest of a personally owned device untouched — distinct from full MDM "
            "enrollment, COPE, and CYOD, which all involve broader device-level management or ownership."
        ),
    },
    {
        "id": "nd4j-029",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile device management",
        "stem": (
            "A defense contractor's MDM policy automatically disables the camera and blocks certain apps "
            "whenever a managed device's GPS location enters the boundary of a specific secure facility, and "
            "re-enables them once the device leaves. Which MDM capability enables this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Geofencing",
                "correct": True,
                "rationale": (
                    "Correct. Geofencing defines a virtual geographic boundary and automatically applies or "
                    "removes specific device restrictions based on the device's real-time GPS location relative "
                    "to that boundary."
                ),
            },
            {
                "id": "b",
                "text": "Containerization",
                "correct": False,
                "rationale": (
                    "Incorrect. Containerization addresses data/app separation on the device, not location-"
                    "triggered, real-time toggling of hardware features like the camera."
                ),
            },
            {
                "id": "c",
                "text": "Remote wipe",
                "correct": False,
                "rationale": (
                    "Incorrect. Remote wipe is a one-time destructive action typically tied to loss/theft or "
                    "offboarding, not a dynamic, reversible policy that engages and disengages automatically "
                    "based on the device's ongoing physical location."
                ),
            },
            {
                "id": "d",
                "text": "Conditional access based on sign-in risk",
                "correct": False,
                "rationale": (
                    "Incorrect. Conditional access decisions are made by the identity provider at the moment of "
                    "authentication based on risk signals; they do not dynamically toggle a device's hardware "
                    "features such as the camera in real time as the device physically moves."
                ),
            },
        ],
        "explanation": (
            "Geofencing is the MDM capability that ties policy enforcement to a device's real-time physical "
            "location, automatically enabling or disabling specific restrictions such as camera access as the "
            "device crosses a defined boundary."
        ),
    },
    {
        "id": "nd4j-030",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Multifactor authentication",
        "stem": (
            "An attacker successfully social-engineers a mobile carrier into porting a victim's phone number to "
            "an attacker-controlled SIM card, then uses SMS-based one-time passcodes to reset the victim's "
            "account passwords and bypass MFA. Which MFA weakness does this exploit, and what replacement would "
            "mitigate it?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "SIM swapping exploits SMS OTP's reliance on the phone number as a proxy for 'something you "
                    "have'; replacing SMS OTP with an authenticator app (TOTP) or a FIDO2 hardware security key, "
                    "both bound to a specific device/key rather than the phone number, mitigates this"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Once the phone number is ported, the attacker receives the SMS codes intended for "
                    "the victim. Binding the second factor to a physical device or key instead of the phone "
                    "number removes this attack path."
                ),
            },
            {
                "id": "b",
                "text": "MFA push-notification fatigue (bombing), where repeated push requests are sent until the user accidentally approves one",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario describes porting the victim's phone number to intercept SMS codes, "
                    "not repeatedly spamming push notifications until accidental approval; these are distinct "
                    "attack techniques with different root causes and mitigations."
                ),
            },
            {
                "id": "c",
                "text": "A TOTP replay attack, reusing a previously valid, still-active time-based one-time passcode",
                "correct": False,
                "rationale": (
                    "Incorrect. Nothing in the scenario involves capturing and reusing a TOTP code; the attack "
                    "described specifically targets the SMS delivery channel via carrier social engineering, not "
                    "code reuse."
                ),
            },
            {
                "id": "d",
                "text": "Biometric spoofing, presenting a forged fingerprint or face to bypass biometric authentication",
                "correct": False,
                "rationale": (
                    "Incorrect. No biometric factor is described in this scenario at all; the attack exclusively "
                    "targets the SMS-based delivery channel via a compromised phone number."
                ),
            },
        ],
        "explanation": (
            "SIM swapping specifically defeats SMS-based MFA because the phone number, not a physical device or "
            "key, is what actually receives the code. Replacing SMS OTP with authenticator-app TOTP or FIDO2 "
            "hardware keys removes reliance on the portable phone number."
        ),
    },
    {
        "id": "nd4j-031",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Multifactor authentication",
        "stem": (
            "A company wants to prompt users for MFA only when a login attempt originates from an unrecognized "
            "device, an unusual geographic location, or occurs outside normal working hours, while allowing "
            "frictionless single-factor access for low-risk, recognized sign-ins. Which authentication approach "
            "does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Risk-based (adaptive/context-aware) authentication",
                "correct": True,
                "rationale": (
                    "Correct. Risk-based authentication dynamically requires step-up MFA only when risk signals "
                    "(new device, unusual location, atypical time) are present, allowing frictionless access for "
                    "low-risk, recognized sign-ins."
                ),
            },
            {
                "id": "b",
                "text": "Mandatory MFA on every login attempt regardless of context",
                "correct": False,
                "rationale": (
                    "Incorrect. This describes the opposite of what's requested: uniform MFA on every login, "
                    "with no conditional/frictionless path for low-risk sign-ins."
                ),
            },
            {
                "id": "c",
                "text": "Single sign-on (SSO) without any additional authentication factor",
                "correct": False,
                "rationale": (
                    "Incorrect. SSO addresses centralizing authentication across multiple applications; it does "
                    "not itself introduce conditional, risk-based prompting for a second factor."
                ),
            },
            {
                "id": "d",
                "text": "Out-of-band authentication delivered through a separate communication channel from the one used to log in",
                "correct": False,
                "rationale": (
                    "Incorrect. Out-of-band delivery describes the channel used to deliver a factor (e.g., a "
                    "phone call separate from the login session), not the risk-based decision logic of when to "
                    "require that factor at all."
                ),
            },
        ],
        "explanation": (
            "Risk-based (adaptive) authentication evaluates contextual signals at each login attempt and only "
            "requires step-up MFA when elevated risk is detected, balancing security with user friction."
        ),
    },
    {
        "id": "nd4j-032",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Penetration testing phases",
        "stem": (
            "During the reconnaissance phase of an authorized penetration test, a tester uses only publicly "
            "available WHOIS records, DNS lookups, and cached search-engine pages, deliberately avoiding "
            "sending any packets directly to the target's live infrastructure. Which type of reconnaissance is "
            "being performed?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Passive reconnaissance",
                "correct": True,
                "rationale": (
                    "Correct. Passive reconnaissance gathers information from publicly available sources without "
                    "directly interacting with or sending traffic to the target's live systems."
                ),
            },
            {
                "id": "b",
                "text": "Active reconnaissance",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario explicitly states the tester avoided sending any packets directly "
                    "to the target's live infrastructure, which rules out active reconnaissance."
                ),
            },
            {
                "id": "c",
                "text": "Vulnerability scanning",
                "correct": False,
                "rationale": (
                    "Incorrect. Vulnerability scanning requires direct interaction with target systems to "
                    "enumerate weaknesses; the scenario describes only public, out-of-band information "
                    "gathering."
                ),
            },
            {
                "id": "d",
                "text": "Exploitation",
                "correct": False,
                "rationale": (
                    "Incorrect. Exploitation is a later phase involving direct attacks against the target; "
                    "nothing in the scenario describes attempting to gain access, only passive information "
                    "gathering."
                ),
            },
        ],
        "explanation": (
            "Passive reconnaissance relies exclusively on publicly available, third-party sources (WHOIS, DNS, "
            "search engines) without ever directly touching the target's systems, distinguishing it from active "
            "reconnaissance, scanning, and exploitation."
        ),
    },
    {
        "id": "nd4j-033",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Penetration testing phases",
        "stem": (
            "Instead of hiring a single firm for a fixed-scope, time-boxed engagement, an organization opens an "
            "ongoing program inviting a large, vetted community of independent researchers to continuously test "
            "its public-facing applications for a monetary reward per validated finding. Which testing approach "
            "does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A bug bounty program",
                "correct": True,
                "rationale": (
                    "Correct. A bug bounty program is an ongoing, crowdsourced initiative inviting many "
                    "independent researchers to continuously test public-facing assets, paying rewards per "
                    "validated finding, rather than a single fixed-scope, time-boxed engagement."
                ),
            },
            {
                "id": "b",
                "text": "A traditional black-box penetration test performed by one contracted firm",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario explicitly describes a large, ongoing community of independent "
                    "researchers rather than a single firm conducting one fixed-scope, time-boxed test."
                ),
            },
            {
                "id": "c",
                "text": "A red team exercise simulating a specific adversary's tactics against detection and response",
                "correct": False,
                "rationale": (
                    "Incorrect. A red team exercise is typically a covert, objective-driven engagement by one "
                    "dedicated team assessing detection/response, not an open, ongoing, crowdsourced, reward-"
                    "per-finding program."
                ),
            },
            {
                "id": "d",
                "text": "An automated vulnerability scan run on a recurring schedule",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario describes human researchers actively testing applications for a "
                    "monetary reward, not an automated recurring scan."
                ),
            },
        ],
        "explanation": (
            "Bug bounty programs crowdsource ongoing security testing to a large community of independent "
            "researchers, paying per validated finding, in contrast to a traditional fixed-scope engagement by "
            "a single contracted firm or team."
        ),
    },
    {
        "id": "nd4j-034",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Port and protocol security",
        "stem": (
            "A vulnerability scan finds that a core switch's configuration backup process uses TFTP over UDP "
            "port 69 to transfer the running-config, unauthenticated and in cleartext, to a backup server on "
            "the same VLAN as general user traffic. What is the BEST remediation?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Replace TFTP with an authenticated, encrypted alternative such as SCP or SFTP for "
                    "configuration transfers, and restrict the backup path to an isolated management VLAN"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Replacing TFTP with an authenticated, encrypted transfer protocol addresses the "
                    "cleartext/unauthenticated exposure, and isolating the backup path to a management VLAN "
                    "removes it from general user traffic."
                ),
            },
            {
                "id": "b",
                "text": "Increase the TFTP session timeout value to reduce the chance of a failed backup transfer",
                "correct": False,
                "rationale": (
                    "Incorrect. Adjusting the timeout has no bearing on the fact that TFTP is unauthenticated "
                    "and transmits data in cleartext; it does nothing to address confidentiality or integrity of "
                    "the configuration transfer."
                ),
            },
            {
                "id": "c",
                "text": "Disable the host-based firewall on the backup server to allow the TFTP transfer to complete faster",
                "correct": False,
                "rationale": (
                    "Incorrect. Disabling a firewall increases exposure rather than reducing it, and does not "
                    "address the fundamental lack of authentication/encryption in TFTP itself."
                ),
            },
            {
                "id": "d",
                "text": "Replace TFTP with SNMPv1 for the configuration backup process",
                "correct": False,
                "rationale": (
                    "Incorrect. SNMPv1 is also unauthenticated (community-string based) and transmits in "
                    "cleartext; it is not designed for file transfer and would not meaningfully improve security "
                    "or fit the use case."
                ),
            },
        ],
        "explanation": (
            "TFTP has no authentication and transmits in cleartext, making it unsuitable for transferring "
            "sensitive device configurations. The proper remediation replaces it with an authenticated, "
            "encrypted protocol and isolates the transfer path onto a dedicated management network."
        ),
    },
    {
        "id": "nd4j-035",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Port and protocol security",
        "stem": (
            "A directory-integrated application authenticates users by sending their plaintext credentials to "
            "the domain controller over TCP port 389 without STARTTLS, making the bind operation susceptible to "
            "interception on the local segment. Which change would remediate this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Reconfigure the application to use LDAPS (TCP 636) or LDAP with STARTTLS to encrypt the bind operation",
                "correct": True,
                "rationale": (
                    "Correct. LDAPS or STARTTLS encrypts the credential exchange during the bind operation so it "
                    "cannot be intercepted in cleartext on the local network segment."
                ),
            },
            {
                "id": "b",
                "text": "Point the application to TCP port 3268 (the Global Catalog) instead of port 389",
                "correct": False,
                "rationale": (
                    "Incorrect. The Global Catalog port provides forest-wide search across domains but, like "
                    "standard LDAP on 389, is unencrypted by default; simply changing the port does not add "
                    "encryption to the bind operation."
                ),
            },
            {
                "id": "c",
                "text": "Increase the domain's minimum password length and complexity requirements",
                "correct": False,
                "rationale": (
                    "Incorrect. Stronger password policy does not protect a credential that is transmitted in "
                    "cleartext during the bind; an interceptor can still capture whatever password is sent, "
                    "regardless of its complexity."
                ),
            },
            {
                "id": "d",
                "text": "Disable the domain controller's built-in firewall to simplify LDAP connectivity troubleshooting",
                "correct": False,
                "rationale": (
                    "Incorrect. Disabling the firewall increases the attack surface and does nothing to encrypt "
                    "the LDAP bind traffic itself, which is the actual vulnerability described."
                ),
            },
        ],
        "explanation": (
            "Standard LDAP on port 389 transmits bind credentials in cleartext unless STARTTLS is used. LDAPS "
            "(port 636) or STARTTLS-protected LDAP encrypts the exchange, directly remediating the interception "
            "risk described."
        ),
    },
    {
        "id": "nd4j-036",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Privileged access management",
        "stem": (
            "An organization requires that all domain administrator activity be performed exclusively from a "
            "dedicated, hardened workstation with no internet browsing, no email client, and no general "
            "productivity software installed, separate from the administrator's everyday laptop. Which control "
            "does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A privileged access workstation (PAW)",
                "correct": True,
                "rationale": (
                    "Correct. A PAW is a dedicated, hardened endpoint used exclusively for administrative tasks, "
                    "isolated from general-purpose activities like web browsing and email that carry a higher "
                    "risk of compromise."
                ),
            },
            {
                "id": "b",
                "text": "Credential vaulting within a PAM solution",
                "correct": False,
                "rationale": (
                    "Incorrect. Vaulting addresses how privileged credentials are stored and issued; it does not "
                    "by itself require or provide a dedicated, isolated hardware endpoint free of general-"
                    "purpose software."
                ),
            },
            {
                "id": "c",
                "text": "Mandatory MFA enforcement on all administrator accounts",
                "correct": False,
                "rationale": (
                    "Incorrect. MFA strengthens the authentication step for privileged accounts but says nothing "
                    "about restricting which physical or virtual workstation is used to perform the "
                    "administrative work."
                ),
            },
            {
                "id": "d",
                "text": "Just-in-time (JIT) privileged access",
                "correct": False,
                "rationale": (
                    "Incorrect. JIT controls the duration and approval of elevated permissions; it does not "
                    "address isolating administrative activity onto a dedicated, hardened workstation free of "
                    "higher-risk general-purpose software."
                ),
            },
        ],
        "explanation": (
            "A privileged access workstation isolates the endpoint used for sensitive administrative work from "
            "higher-risk, general-purpose activities, reducing the chance that malware or phishing compromises "
            "the same machine used to manage critical systems."
        ),
    },
    {
        "id": "nd4j-037",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Privileged access management",
        "stem": (
            "Select TWO true statements comparing password vaulting (credential checkout) with just-in-time "
            "(JIT) privilege elevation in a PAM solution."
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Credential vaulting (checkout) stores and rotates a shared account's existing credential "
                    "centrally, requiring a user to request temporary check-out access to that static secret; "
                    "JIT elevation instead grants time-bound elevated permissions directly to the user's own "
                    "identity without ever exposing a shared credential."
                ),
                "correct": True,
                "rationale": (
                    "Correct. This accurately describes the mechanical difference: vaulting checks out an "
                    "existing shared secret, while JIT elevates the user's own identity temporarily without "
                    "revealing any shared credential."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Because JIT elevation does not require handing the user a secret to remember or type, it "
                    "reduces the credential-theft exposure surface compared with a vaulted checkout model."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Since no shared credential is exposed to the user under JIT, risks such as "
                    "keylogging, shoulder-surfing, or local credential caching of that secret are reduced "
                    "compared to a checkout-based vaulting model."
                ),
            },
            {
                "id": "c",
                "text": "Credential vaulting removes the need to enforce MFA on privileged accounts, since the vault itself is considered a sufficient control.",
                "correct": False,
                "rationale": (
                    "Incorrect. Vaulting centralizes and rotates the secret but does not replace the need for "
                    "strong authentication to access the vault or use the checked-out account; treating the "
                    "vault as a substitute for MFA is a security gap, not a benefit."
                ),
            },
            {
                "id": "d",
                "text": "JIT elevation permanently adds the user to the privileged group, and that membership persists indefinitely after the approved task is completed.",
                "correct": False,
                "rationale": (
                    "Incorrect. The defining characteristic of JIT elevation is that the granted privilege is "
                    "time-bound and automatically expires/revokes at the end of the approved window; a "
                    "permanent group addition describes standing access, the opposite of JIT."
                ),
            },
        ],
        "explanation": (
            "Vaulting and JIT elevation both reduce standing privileged access, but through different "
            "mechanisms: vaulting centrally stores and rotates a shared secret issued on checkout, while JIT "
            "grants time-bound privilege directly to the user's own identity without ever exposing a shared "
            "credential, further reducing credential-theft exposure."
        ),
    },
    {
        "id": "nd4j-038",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "A SIEM correlation rule is designed to alert when a suspicious login on Server A is followed by an "
            "unusual file access on Server B within five minutes. Investigation reveals that Server A logs "
            "timestamps in UTC while Server B logs timestamps in the local time zone, and the rule has never "
            "fired even though both qualifying events have occurred together in the underlying raw logs. What "
            "should be corrected?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Ensure proper log normalization and time synchronization (consistent time zone handling and "
                    "NTP-synchronized clocks) across all ingested sources so timestamp fields are parsed and "
                    "compared accurately before correlation"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Consistent normalization of time zones and synchronized clocks ensures events from "
                    "different sources are compared on the same timeline, which is required for a time-window "
                    "correlation rule to evaluate event ordering correctly."
                ),
            },
            {
                "id": "b",
                "text": "Increase the SIEM's log retention period from 90 days to 12 months",
                "correct": False,
                "rationale": (
                    "Incorrect. Longer retention affects how far back historical searches can go; it does "
                    "nothing to fix a correlation rule that is failing because timestamps from different sources "
                    "are inconsistently formatted or zoned."
                ),
            },
            {
                "id": "c",
                "text": "Add additional, unrelated log sources to increase overall visibility",
                "correct": False,
                "rationale": (
                    "Incorrect. Adding more raw data sources does not fix an existing correlation rule's "
                    "timestamp-parsing problem and could add further inconsistent time formats, compounding "
                    "rather than solving the issue."
                ),
            },
            {
                "id": "d",
                "text": "Lower the severity threshold required for the correlation rule to generate an alert",
                "correct": False,
                "rationale": (
                    "Incorrect. Lowering the severity threshold changes when an alert fires assuming the rule's "
                    "logic evaluates correctly; it does not address the underlying reason the rule never "
                    "triggers, which is a timestamp/normalization mismatch."
                ),
            },
        ],
        "explanation": (
            "Correlation rules that compare events across time windows depend on consistent time normalization "
            "across all ingested sources. Mismatched time zones or unsynchronized clocks can silently prevent a "
            "correctly designed rule from ever firing."
        ),
    },
    {
        "id": "nd4j-039",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SIEM & monitoring",
        "stem": (
            "A SOC doubles the number of log sources feeding its SIEM over a year, but the number of confirmed "
            "true-positive detections has not increased and analyst alert fatigue has worsened. What is the "
            "MOST likely root cause and appropriate fix?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Detection content (correlation rules/use cases) was not developed for the new log sources; "
                    "the team must build tuned detection use cases for the new data rather than simply ingesting "
                    "more raw logs"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Ingesting more log data without corresponding tuned detection logic produces more "
                    "noise, not more meaningful detections; the fix is deliberate detection content engineering "
                    "for the new sources."
                ),
            },
            {
                "id": "b",
                "text": "Reduce the SIEM's log retention period to lower storage costs",
                "correct": False,
                "rationale": (
                    "Incorrect. Retention period affects how long historical data is searchable and has no "
                    "bearing on why the additional ingested data isn't producing more confirmed true-positive "
                    "detections."
                ),
            },
            {
                "id": "c",
                "text": "Increase the SIEM's log ingestion rate limit to process events faster",
                "correct": False,
                "rationale": (
                    "Incorrect. A rate limit constrains throughput/performance; raising it does not create the "
                    "missing detection logic needed to turn the new log data into meaningful, tuned alerts."
                ),
            },
            {
                "id": "d",
                "text": "Purchase additional SIEM licensing to support a larger environment",
                "correct": False,
                "rationale": (
                    "Incorrect. Licensing capacity governs how much data the platform can handle; it does not "
                    "address the actual root cause, which is a lack of detection engineering built around the "
                    "newly added sources."
                ),
            },
        ],
        "explanation": (
            "Simply ingesting more log sources does not improve detection quality on its own; without dedicated "
            "detection content engineering (tuned correlation rules/use cases) for the new data, added volume "
            "mainly increases noise and analyst fatigue rather than true-positive detections."
        ),
    },
    {
        "id": "nd4j-040",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A vulnerability's CVSS Base Score remains 8.8 (High), unchanged since publication. Six months "
            "later, fully weaponized, publicly available exploit code emerges and no vendor patch exists yet. "
            "Which CVSS metric group reflects this change in real-world risk even though the Base Score itself "
            "stays the same?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Temporal metrics (Exploit Code Maturity, Remediation Level, Report Confidence)",
                "correct": True,
                "rationale": (
                    "Correct. Temporal metrics adjust the score based on real-world factors that change over "
                    "time, such as the emergence of functional public exploit code and the current absence of "
                    "an official patch, without altering the fixed Base Score."
                ),
            },
            {
                "id": "b",
                "text": "Environmental metrics",
                "correct": False,
                "rationale": (
                    "Incorrect. Environmental metrics are organization-specific adjustments reflecting a "
                    "particular deployment's context and compensating controls; the change described here — "
                    "public exploit code becoming available broadly — is a general, time-based shift that "
                    "temporal metrics are designed to capture."
                ),
            },
            {
                "id": "c",
                "text": "Base metrics",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario explicitly states the Base Score remains unchanged; Base metrics "
                    "represent the intrinsic, constant characteristics of the vulnerability and, by design, do "
                    "not change over its lifetime."
                ),
            },
            {
                "id": "d",
                "text": "Attack Complexity, a Base metric sub-component",
                "correct": False,
                "rationale": (
                    "Incorrect. Attack Complexity is a fixed Base metric describing the vulnerability's inherent "
                    "exploitation conditions; it does not capture time-varying factors like whether a public "
                    "exploit currently exists or whether a patch has been released."
                ),
            },
        ],
        "explanation": (
            "CVSS temporal metrics capture how a vulnerability's real-world risk evolves over time — such as "
            "exploit code maturity and remediation availability — independently of the fixed Base Score, which "
            "reflects only the vulnerability's intrinsic characteristics."
        ),
    },
    {
        "id": "nd4j-041",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "A critical vulnerability has a CVSS Base Score of 9.8, but the affected server sits on an isolated "
            "OT network segment with no internet connectivity, additional network access controls, and "
            "processes only non-sensitive telemetry data with no confidentiality or integrity impact to the "
            "organization if compromised. Which CVSS metric group should the analyst adjust to reflect the "
            "organization's true risk exposure?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Environmental metrics, which allow the impact and exploitability sub-scores to be adjusted "
                    "to reflect the specific deployment context and compensating controls"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Environmental metrics exist precisely to let an organization adjust the score "
                    "based on its own network isolation, compensating controls, and the actual sensitivity/"
                    "criticality of the affected asset and data."
                ),
            },
            {
                "id": "b",
                "text": "Temporal metrics, which reflect general, time-based changes in exploit availability and remediation status",
                "correct": False,
                "rationale": (
                    "Incorrect. Temporal metrics capture broadly applicable, time-varying factors like public "
                    "exploit maturity; they are not the mechanism for reflecting one organization's specific "
                    "compensating controls or the actual sensitivity of its data."
                ),
            },
            {
                "id": "c",
                "text": "Base metrics, the vendor-published, universal characteristics of the vulnerability",
                "correct": False,
                "rationale": (
                    "Incorrect. Base metrics are fixed and standardized precisely so they are comparable across "
                    "organizations; they are not meant to be locally adjusted, which is exactly why "
                    "environmental metrics exist."
                ),
            },
            {
                "id": "d",
                "text": "Simply lower the ticket's priority in the tracking system without adjusting or documenting any CVSS metric",
                "correct": False,
                "rationale": (
                    "Incorrect. Changing priority without adjusting/documenting the environmental score "
                    "sacrifices the standardized, auditable justification that environmental metrics provide, "
                    "potentially confusing future audits about why a 'critical' CVE was deprioritized."
                ),
            },
        ],
        "explanation": (
            "Environmental metrics let an organization formally adjust a vulnerability's impact and "
            "exploitability sub-scores to reflect its own compensating controls and asset context, producing an "
            "auditable, organization-specific risk score without altering the universal Base Score."
        ),
    },
    {
        "id": "nd4j-042",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Vulnerability management & CVSS",
        "stem": (
            "Select TWO true statements comparing credentialed and uncredentialed vulnerability scans."
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Credentialed scans authenticate to the target operating system to directly enumerate "
                    "installed software versions, missing patches, and local misconfigurations that are not "
                    "visible from the network alone."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Authenticated access lets the scanner query the local system directly for "
                    "installed package versions, patch levels, and configuration details unavailable to a "
                    "purely network-facing scan."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Uncredentialed scans assess the target the way an unauthenticated external attacker would "
                    "— relying on exposed network services, banners, and responses — and typically surface "
                    "fewer, less detailed findings than a credentialed scan of the same host."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Without authenticated access, the scanner is limited to what is visible from the "
                    "network perimeter, generally producing a narrower and less detailed set of findings than a "
                    "credentialed scan of the same host."
                ),
            },
            {
                "id": "c",
                "text": "Uncredentialed scans always produce more complete and accurate results than credentialed scans because no account provisioning is required.",
                "correct": False,
                "rationale": (
                    "Incorrect. The opposite is generally true: without authenticated access, a scanner cannot "
                    "inspect installed package versions or local configuration, typically resulting in fewer, "
                    "less detailed findings than a credentialed scan of the same host."
                ),
            },
            {
                "id": "d",
                "text": "Credentialed scans cannot detect missing operating system patches and are limited to identifying network-facing service misconfigurations.",
                "correct": False,
                "rationale": (
                    "Incorrect. This describes a limitation of uncredentialed scanning, not credentialed "
                    "scanning; credentialed scans are specifically valued for their ability to directly "
                    "enumerate missing OS and application patches via authenticated local access."
                ),
            },
        ],
        "explanation": (
            "Credentialed scans authenticate to the host to reveal detailed, local vulnerability data (missing "
            "patches, installed versions, misconfigurations), while uncredentialed scans see only what an "
            "external, unauthenticated attacker would observe from the network, typically producing fewer and "
            "less detailed findings."
        ),
    },
    {
        "id": "nd4j-043",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Wireless security",
        "stem": (
            "A security assessment recommends migrating a branch office wireless network from WPA2-PSK to "
            "WPA3-Personal specifically to prevent attackers from capturing a handshake and performing offline "
            "dictionary/brute-force attacks against the passphrase. Which WPA3 mechanism provides this specific "
            "protection?"
        ),
        "options": [
            {
                "id": "a",
                "text": "SAE (Simultaneous Authentication of Equals, the WPA3 'Dragonfly' handshake)",
                "correct": True,
                "rationale": (
                    "Correct. SAE requires an attacker to interact live with the AP for every single password "
                    "guess, making large-scale offline dictionary/brute-force attacks against a captured "
                    "handshake infeasible, unlike WPA2-PSK's 4-way handshake."
                ),
            },
            {
                "id": "b",
                "text": "AES-CCMP encryption",
                "correct": False,
                "rationale": (
                    "Incorrect. AES-CCMP protects traffic confidentiality after a client is associated; it is "
                    "not the mechanism that changed to prevent offline attacks against a captured authentication "
                    "handshake, since WPA2 already uses AES-CCMP and remained vulnerable to this attack."
                ),
            },
            {
                "id": "c",
                "text": "802.1X with EAP-TLS",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario specifies WPA3-Personal, which does not use 802.1X/EAP; that "
                    "framework belongs to WPA2/WPA3-Enterprise mode and is not the mechanism providing offline-"
                    "attack resistance in personal mode."
                ),
            },
            {
                "id": "d",
                "text": "Extending the SSID broadcast interval",
                "correct": False,
                "rationale": (
                    "Incorrect. The SSID broadcast interval is a discoverability/beacon-timing setting unrelated "
                    "to the cryptographic handshake mechanism that resists offline password-guessing attacks."
                ),
            },
        ],
        "explanation": (
            "WPA3-Personal replaces WPA2's PSK 4-way handshake with SAE (Dragonfly), which requires live, per-"
            "guess interaction with the AP, making captured-handshake offline brute-force/dictionary attacks "
            "impractical."
        ),
    },
    {
        "id": "nd4j-044",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Wireless security",
        "stem": (
            "Employees on a warehouse floor report frequent Wi-Fi disconnections at the same time each "
            "afternoon, correlating with the operation of large motorized equipment and a break-room microwave, "
            "both of which operate near the 2.4 GHz band. A wireless site survey confirms elevated RF noise "
            "coincides with these events but finds no rogue devices and no deauthentication frames. What does "
            "this indicate, and what is an appropriate first remediation?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Unintentional RF interference from nearby 2.4 GHz devices, not a malicious jamming attack; "
                    "migrate affected access points/clients to the less congested 5 GHz band and/or relocate "
                    "APs away from the interference sources"
                ),
                "correct": True,
                "rationale": (
                    "Correct. The disruption correlates directly with known, non-malicious equipment operating "
                    "on overlapping frequencies, and the survey found no rogue devices or attack traffic — "
                    "consistent with unintentional interference, not an attack."
                ),
            },
            {
                "id": "b",
                "text": "A deliberate RF jamming/denial-of-service attack requiring immediate WIPS-driven containment of a rogue transmitter",
                "correct": False,
                "rationale": (
                    "Incorrect. The site survey found no rogue devices and no deauthentication frames, and the "
                    "disruption correlates directly with known non-malicious equipment, which points to "
                    "interference rather than an intentional jamming attack."
                ),
            },
            {
                "id": "c",
                "text": "An evil-twin access point impersonating the legitimate corporate SSID",
                "correct": False,
                "rationale": (
                    "Incorrect. An evil twin involves a rogue AP broadcasting a duplicate SSID to lure clients; "
                    "the survey found no rogue devices at all, and the pattern is inconsistent with an "
                    "impersonation attack."
                ),
            },
            {
                "id": "d",
                "text": "A rogue access point connected to the network requiring physical port security remediation",
                "correct": False,
                "rationale": (
                    "Incorrect. No rogue device was identified during the survey; the disruption is explained by "
                    "elevated ambient RF noise coinciding with unrelated equipment operation, not an "
                    "unauthorized device physically connected to the network."
                ),
            },
        ],
        "explanation": (
            "Not every wireless disruption is malicious. Correlating disconnections with known 2.4 GHz-emitting "
            "equipment, combined with the absence of rogue devices or deauthentication frames in the survey, "
            "points to unintentional RF interference, remediated by shifting to less congested spectrum or "
            "relocating APs."
        ),
    },
]

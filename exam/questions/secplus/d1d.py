"""
CompTIA Security+ (SY0-701) Domain 1: General Security Concepts — Set D
36 exam-quality questions covering objectives 1.1 through 1.4.
"""

QUESTIONS = [
    # ── 1.1 Security control categories ─────────────────────────────────────
    {
        "id": "nd1d-001",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security control categories",
        "stem": (
            "A university's cybersecurity clinic requires every incoming intern to "
            "complete a signed acceptable-use agreement and an annual phishing-awareness "
            "course before receiving lab credentials. Which security control CATEGORY "
            "does this requirement represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Managerial",
                "correct": True,
                "rationale": (
                    "Correct. Managerial (administrative) controls consist of policies and "
                    "governance decisions that set expectations for people — requiring a "
                    "signed agreement and training before granting access is a "
                    "governance-driven policy, not a technical enforcement mechanism."
                ),
            },
            {
                "id": "b",
                "text": "Technical",
                "correct": False,
                "rationale": (
                    "Incorrect. No technology is enforcing this requirement; a person "
                    "manually verifies the signed agreement and course completion before "
                    "provisioning credentials, which is a policy decision, not a "
                    "technical control."
                ),
            },
            {
                "id": "c",
                "text": "Operational",
                "correct": False,
                "rationale": (
                    "Incorrect. Operational controls are the recurring, people-executed "
                    "day-to-day procedures that implement a policy (e.g., the clinic staff "
                    "checking each intern's paperwork). The requirement itself — the "
                    "policy mandating the agreement and training — is managerial."
                ),
            },
            {
                "id": "d",
                "text": "Physical",
                "correct": False,
                "rationale": (
                    "Incorrect. Physical controls protect tangible spaces and assets "
                    "(locks, badges, cameras). A signed policy requirement has no physical "
                    "component."
                ),
            },
        ],
        "explanation": (
            "Control category describes HOW a control is implemented. A governance-level "
            "policy requiring training and a signed agreement before access is granted is "
            "a Managerial control, distinct from the Operational act of checking compliance "
            "or a Technical mechanism that enforces it automatically."
        ),
    },
    {
        "id": "nd1d-002",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Security control categories",
        "stem": (
            "A logistics company's SIEM automatically disables a user account and revokes "
            "all active sessions the instant it correlates three failed MFA challenges "
            "with an impossible-travel login from a new country, without waiting for "
            "analyst confirmation. Which security control CATEGORY does this automated "
            "response represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Technical",
                "correct": True,
                "rationale": (
                    "Correct. Technical (logical) controls are implemented through "
                    "technology that enforces security automatically. The SIEM disabling "
                    "the account and revoking sessions without human intervention is a "
                    "system executing logic, which is the defining trait of a technical "
                    "control."
                ),
            },
            {
                "id": "b",
                "text": "Managerial",
                "correct": False,
                "rationale": (
                    "Incorrect. Managerial controls are the governance-level policies "
                    "that decide such automation SHOULD exist (e.g., an incident response "
                    "policy authorizing automated containment); the actual real-time "
                    "revocation is carried out by technology, not a governance decision."
                ),
            },
            {
                "id": "c",
                "text": "Operational",
                "correct": False,
                "rationale": (
                    "Incorrect. Operational controls involve people performing day-to-day "
                    "procedures. Because this response happens with no analyst "
                    "confirmation, there is no human executing a procedure — the system "
                    "itself is the enforcement mechanism."
                ),
            },
            {
                "id": "d",
                "text": "Physical",
                "correct": False,
                "rationale": (
                    "Incorrect. Physical controls protect tangible assets and spaces; "
                    "an account lockout in a SIEM has no physical component."
                ),
            },
        ],
        "explanation": (
            "Automated, technology-enforced actions such as SOAR/SIEM-driven account "
            "disablement are Technical controls. The policy authorizing the automation is "
            "Managerial, and a human analyst manually reviewing the case afterward would "
            "be Operational."
        ),
    },
    # ── 1.1 Security control types ───────────────────────────────────────────
    {
        "id": "nd1d-003",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security control types",
        "stem": (
            "A gaming company's WAF is configured to automatically block any HTTP request "
            "whose body matches a known SQL injection signature before the request ever "
            "reaches the application server. Which control TYPE does the WAF's blocking "
            "action represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Preventive",
                "correct": True,
                "rationale": (
                    "Correct. Preventive controls stop an action before it can occur. "
                    "Blocking the malicious request before it reaches the application "
                    "server prevents the SQL injection attempt from ever executing."
                ),
            },
            {
                "id": "b",
                "text": "Detective",
                "correct": False,
                "rationale": (
                    "Incorrect. Detective controls identify and record an event after — or "
                    "as — it occurs, such as logging the blocked attempt for review. Here "
                    "the request is stopped outright, which is prevention, not mere "
                    "detection."
                ),
            },
            {
                "id": "c",
                "text": "Corrective",
                "correct": False,
                "rationale": (
                    "Incorrect. Corrective controls restore systems or remediate damage "
                    "after an incident has already occurred (e.g., restoring a database "
                    "after a successful injection). No damage occurs here because the "
                    "request never reaches the server."
                ),
            },
            {
                "id": "d",
                "text": "Compensating",
                "correct": False,
                "rationale": (
                    "Incorrect. A compensating control substitutes for a primary control "
                    "that cannot be implemented directly. The WAF here is functioning as "
                    "the primary preventive mechanism, not a substitute for another "
                    "control."
                ),
            },
        ],
        "explanation": (
            "Control type describes WHEN/WHY a control acts relative to an event. A WAF "
            "blocking malicious traffic before it reaches the target is Preventive; logging "
            "the attempt afterward would be Detective, and restoring a compromised system "
            "would be Corrective."
        ),
    },
    {
        "id": "nd1d-004",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Security control types",
        "stem": (
            "A biotech firm's incident response plan states that whenever ransomware "
            "encrypts a lab workstation, the affected host is immediately isolated from "
            "the network by the EDR agent, and once isolated, IT rebuilds the workstation "
            "from a known-good image and restores research data from the last clean "
            "backup. Which TWO control types are represented by these two actions, "
            "respectively? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Corrective — rebuilding the workstation and restoring data from backup",
                "correct": True,
                "rationale": (
                    "Correct. Rebuilding the compromised host and restoring data restores "
                    "the system to a known-good state after the incident, which is the "
                    "definition of a corrective control."
                ),
            },
            {
                "id": "b",
                "text": "Directive — the EDR agent isolating the host from the network",
                "correct": False,
                "rationale": (
                    "Incorrect. Directive controls are policies or rules that instruct "
                    "behavior (e.g., a mandate requiring isolation procedures to exist). "
                    "The EDR agent actively cutting network access is an automated "
                    "technical action limiting damage, which is compensating/preventive in "
                    "nature relative to further spread, not a directive."
                ),
            },
            {
                "id": "c",
                "text": "Compensating — the EDR agent isolating the host from the network",
                "correct": True,
                "rationale": (
                    "Correct. Network isolation acts as an alternative containment measure "
                    "that limits further damage when the primary preventive controls "
                    "(patching, email filtering) already failed to stop the ransomware — "
                    "this stopgap, damage-limiting action is best characterized as "
                    "compensating."
                ),
            },
            {
                "id": "d",
                "text": "Preventive — rebuilding the workstation and restoring data from backup",
                "correct": False,
                "rationale": (
                    "Incorrect. The rebuild happens after the encryption has already "
                    "occurred; it restores the system rather than preventing the initial "
                    "compromise, so it is corrective, not preventive."
                ),
            },
            {
                "id": "e",
                "text": "Detective — rebuilding the workstation and restoring data from backup",
                "correct": False,
                "rationale": (
                    "Incorrect. Detective controls identify that an event happened; "
                    "rebuilding and restoring data actively remediates the damage, which is "
                    "corrective action, not detection."
                ),
            },
        ],
        "explanation": (
            "Isolating an already-infected host to stop lateral spread is a compensating "
            "action that limits damage once prevention has failed, while rebuilding the "
            "host and restoring data is corrective, restoring the system to a known-good "
            "state after the incident."
        ),
    },
    # ── 1.1 Security control categories and types ───────────────────────────
    {
        "id": "nd1d-005",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security control categories and types",
        "stem": (
            "An airline's maintenance hangar requires every technician to swipe a badge "
            "and pass a weight-sensor mantrap that allows only one person through per "
            "authenticated swipe, automatically alarming if two people attempt to pass on "
            "a single badge. Which CATEGORY and TYPE pairing BEST describes the mantrap?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Physical category, Preventive type",
                "correct": True,
                "rationale": (
                    "Correct. The mantrap is a tangible physical barrier (physical "
                    "category) that stops unauthorized tailgating entry before it happens "
                    "(preventive type), since only one authenticated person can pass per "
                    "swipe."
                ),
            },
            {
                "id": "b",
                "text": "Physical category, Detective type",
                "correct": False,
                "rationale": (
                    "Incorrect. While the alarm on a double-entry attempt does detect an "
                    "anomaly, the mantrap's primary function — physically blocking a "
                    "second person from passing through — is preventive, not merely "
                    "detective."
                ),
            },
            {
                "id": "c",
                "text": "Technical category, Preventive type",
                "correct": False,
                "rationale": (
                    "Incorrect. Although the weight sensor and badge reader involve "
                    "technology, the control's defining characteristic is a tangible "
                    "physical barrier restricting real-world movement, so it is classified "
                    "as physical category, not technical."
                ),
            },
            {
                "id": "d",
                "text": "Physical category, Compensating type",
                "correct": False,
                "rationale": (
                    "Incorrect. A compensating control substitutes for a primary control "
                    "that cannot be used directly. The mantrap is the intended primary "
                    "access-control mechanism itself, not a substitute for another "
                    "control."
                ),
            },
        ],
        "explanation": (
            "A mantrap is a tangible barrier that physically prevents tailgating, making "
            "it Physical category and Preventive type — it stops the unauthorized entry "
            "attempt outright rather than merely recording that it happened."
        ),
    },
    {
        "id": "nd1d-006",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Security control categories and types",
        "stem": (
            "An insurance company's underwriting policy mandates a quarterly, "
            "human-led review of every user's entitlements against their current job "
            "role, with any excess access flagged for manual revocation by the access "
            "governance team. Which CATEGORY and TYPE pairing BEST describes this "
            "quarterly access review?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Operational category, Detective type",
                "correct": True,
                "rationale": (
                    "Correct. The review is a recurring, people-executed task (operational "
                    "category) whose purpose is to identify excess access that already "
                    "exists (detective type) — it discovers a condition rather than "
                    "stopping it from ever occurring."
                ),
            },
            {
                "id": "b",
                "text": "Managerial category, Preventive type",
                "correct": False,
                "rationale": (
                    "Incorrect. The underwriting policy that MANDATES the review is "
                    "managerial, but the act of actually performing the quarterly review "
                    "is an operational task; it also is not preventive because it looks "
                    "for access that already exists rather than blocking excess grants "
                    "up front."
                ),
            },
            {
                "id": "c",
                "text": "Technical category, Detective type",
                "correct": False,
                "rationale": (
                    "Incorrect. This is a manual, human-led review process with no "
                    "automated enforcement mechanism, so it falls under operational "
                    "category, not technical."
                ),
            },
            {
                "id": "d",
                "text": "Operational category, Corrective type",
                "correct": False,
                "rationale": (
                    "Incorrect. The review itself is detective — it identifies excess "
                    "access. The subsequent manual revocation, not described as automatic "
                    "here, would be the corrective step that follows detection, but the "
                    "review process being asked about is the detective activity."
                ),
            },
        ],
        "explanation": (
            "A recurring, people-performed access review is Operational category. Because "
            "it identifies existing excess entitlements rather than blocking them from "
            "being granted in the first place, it is Detective type; the subsequent "
            "revocation action would be corrective."
        ),
    },
    # ── 1.2 AAA framework ─────────────────────────────────────────────────────
    {
        "id": "nd1d-007",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "AAA framework",
        "stem": (
            "A telecom provider's network access control system verifies a contractor's "
            "smart card and PIN, then checks a policy engine to determine that the "
            "contractor may only reach the lab VLAN and not the corporate finance VLAN. "
            "Which element of the AAA framework does the VLAN restriction decision "
            "represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Authorization",
                "correct": True,
                "rationale": (
                    "Correct. Authorization determines what an already-authenticated "
                    "identity is permitted to do or access. Restricting the contractor to "
                    "the lab VLAN while blocking the finance VLAN is an authorization "
                    "decision made after identity was confirmed."
                ),
            },
            {
                "id": "b",
                "text": "Authentication",
                "correct": False,
                "rationale": (
                    "Incorrect. Authentication is the smart-card-and-PIN verification "
                    "step that confirms the contractor's identity; it occurs before the "
                    "VLAN-restriction decision and does not itself decide what resources "
                    "are permitted."
                ),
            },
            {
                "id": "c",
                "text": "Accounting",
                "correct": False,
                "rationale": (
                    "Incorrect. Accounting records what the contractor did after being "
                    "granted access (e.g., session duration, VLAN traffic logs). Deciding "
                    "which VLAN the contractor is allowed to reach is authorization, not "
                    "the logging of that activity."
                ),
            },
            {
                "id": "d",
                "text": "Identification",
                "correct": False,
                "rationale": (
                    "Incorrect. Identification is the initial claim of identity (e.g., "
                    "presenting the smart card's identifier), which precedes both "
                    "authentication and authorization; it is not the policy decision "
                    "restricting VLAN access."
                ),
            },
        ],
        "explanation": (
            "AAA separates identity verification (authentication) from the subsequent "
            "decision about what the verified identity may access (authorization). "
            "Restricting the contractor's reachable VLAN is an authorization control."
        ),
    },
    {
        "id": "nd1d-008",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "AAA framework",
        "stem": (
            "A managed service provider deploys a centralized AAA server for all client "
            "firewall and router administration. Which TWO of the following are core "
            "responsibilities that the AAA server is specifically expected to perform for "
            "administrator logins? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Verify the administrator's submitted credentials against a directory before granting a session",
                "correct": True,
                "rationale": (
                    "Correct. Authentication — verifying submitted credentials against a "
                    "trusted identity store — is a core AAA responsibility that must occur "
                    "before any session is granted."
                ),
            },
            {
                "id": "b",
                "text": "Log the exact commands each administrator executes and the session duration for later audit",
                "correct": True,
                "rationale": (
                    "Correct. Accounting — recording what was done, by whom, and for how "
                    "long — is a core AAA responsibility that supports audit trails and "
                    "billing/compliance reporting."
                ),
            },
            {
                "id": "c",
                "text": "Encrypt the firewall's configuration file at rest on local flash storage",
                "correct": False,
                "rationale": (
                    "Incorrect. Encrypting stored configuration data is a data-protection "
                    "function of the device itself, not a responsibility of the AAA "
                    "protocol governing administrative logins."
                ),
            },
            {
                "id": "d",
                "text": "Generate the device's TLS certificate used for its management HTTPS portal",
                "correct": False,
                "rationale": (
                    "Incorrect. Certificate issuance is a PKI function unrelated to the "
                    "AAA server's role of authenticating, authorizing, and accounting for "
                    "administrative access."
                ),
            },
            {
                "id": "e",
                "text": "Patch the firewall's operating system to remediate known vulnerabilities",
                "correct": False,
                "rationale": (
                    "Incorrect. Patch management is a vulnerability-management and "
                    "hardening activity, not a function the AAA framework performs."
                ),
            },
        ],
        "explanation": (
            "AAA servers such as RADIUS or TACACS+ handle authentication (verifying "
            "credentials), authorization (deciding permitted commands), and accounting "
            "(logging session activity) for administrative access — not encryption, "
            "certificate issuance, or patching, which are separate security functions."
        ),
    },
    # ── 1.2 Attack type identification ───────────────────────────────────────
    {
        "id": "nd1d-009",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Attack type identification",
        "stem": (
            "A finance team receives an email that appears to come from their cloud "
            "accounting vendor, warning that the company's account will be suspended "
            "unless an invoice is paid within two hours through a link to a "
            "convincingly cloned login page. The message creates intense time pressure "
            "and targets the entire finance distribution list rather than one individual. "
            "Which attack technique is BEST described?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Phishing",
                "correct": True,
                "rationale": (
                    "Correct. A broadly distributed, deceptive email impersonating a "
                    "trusted vendor and directing recipients to a fraudulent look-alike "
                    "login page to harvest credentials or trigger payment is classic "
                    "phishing, amplified here with urgency."
                ),
            },
            {
                "id": "b",
                "text": "Business email compromise targeting a specific executive",
                "correct": False,
                "rationale": (
                    "Incorrect. Business email compromise typically involves a compromised "
                    "or spoofed executive account targeting one or a few specific "
                    "individuals with a tailored request. This message is a mass email to "
                    "an entire distribution list impersonating a vendor, which fits "
                    "generic phishing rather than a targeted BEC attempt."
                ),
            },
            {
                "id": "c",
                "text": "Vishing",
                "correct": False,
                "rationale": (
                    "Incorrect. Vishing is conducted over voice calls. This attack is "
                    "delivered entirely by email with a malicious link, not a phone "
                    "call."
                ),
            },
            {
                "id": "d",
                "text": "Typosquatting",
                "correct": False,
                "rationale": (
                    "Incorrect. Typosquatting is registering domains with common "
                    "misspellings to catch users who mistype a URL. While the cloned login "
                    "page might use a similar domain, the attack described is the "
                    "deceptive email campaign itself, which is phishing; typosquatting "
                    "describes only the domain-registration tactic."
                ),
            },
        ],
        "explanation": (
            "A mass, urgency-driven email impersonating a trusted vendor and linking to a "
            "fraudulent login page is phishing. BEC would require a narrowly targeted, "
            "spoofed-executive request rather than a distribution-list-wide vendor "
            "impersonation."
        ),
    },
    {
        "id": "nd1d-010",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Attack type identification",
        "stem": (
            "During an incident investigation, analysts determine that an attacker "
            "registered a rogue access point broadcasting the same SSID as the coffee "
            "shop's legitimate free Wi-Fi network, with a stronger signal, causing nearby "
            "laptops to auto-connect and route all traffic through the attacker's device "
            "for inspection and modification. Which attack is BEST described?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Evil twin",
                "correct": True,
                "rationale": (
                    "Correct. An evil twin is a rogue access point that impersonates a "
                    "legitimate network's SSID, luring victims to connect so the attacker "
                    "can intercept and manipulate their traffic — exactly what is "
                    "described."
                ),
            },
            {
                "id": "b",
                "text": "Bluejacking",
                "correct": False,
                "rationale": (
                    "Incorrect. Bluejacking is sending unsolicited messages to nearby "
                    "Bluetooth devices; it has nothing to do with impersonating a Wi-Fi "
                    "access point."
                ),
            },
            {
                "id": "c",
                "text": "Deauthentication attack",
                "correct": False,
                "rationale": (
                    "Incorrect. A deauthentication attack forcibly disconnects clients "
                    "from a legitimate access point, often as a precursor to an evil "
                    "twin attack, but this scenario describes clients connecting to a "
                    "rogue AP rather than being forcibly disconnected."
                ),
            },
            {
                "id": "d",
                "text": "Bluesnarfing",
                "correct": False,
                "rationale": (
                    "Incorrect. Bluesnarfing is unauthorized theft of data from a device "
                    "over a Bluetooth connection, not the impersonation of a Wi-Fi "
                    "network's SSID."
                ),
            },
        ],
        "explanation": (
            "A rogue AP mimicking a legitimate SSID to intercept victim traffic is an "
            "evil twin attack. Deauthentication is often used beforehand to force clients "
            "off the real network, but the scenario here is the impersonation itself."
        ),
    },
    # ── 1.2 CIA triad and non-repudiation ────────────────────────────────────
    {
        "id": "nd1d-011",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "CIA triad and non-repudiation",
        "stem": (
            "A manufacturing plant's programmable logic controller (PLC) receives a "
            "flood of malformed Modbus packets that crash its control process, halting "
            "the assembly line for four hours even though no configuration values were "
            "altered and no data left the network. Which security objective was PRIMARILY "
            "violated?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Availability",
                "correct": True,
                "rationale": (
                    "Correct. The malformed packets crashed the control process and "
                    "halted operations, denying legitimate use of the system — this is a "
                    "direct violation of availability, the assurance that systems remain "
                    "accessible and functioning when needed."
                ),
            },
            {
                "id": "b",
                "text": "Confidentiality",
                "correct": False,
                "rationale": (
                    "Incorrect. No data left the network, so there was no unauthorized "
                    "disclosure of information; confidentiality was not the objective "
                    "harmed."
                ),
            },
            {
                "id": "c",
                "text": "Integrity",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario states no configuration values were altered, "
                    "so the accuracy and trustworthiness of the PLC's data was not "
                    "compromised; the impact was a denial of service, not data "
                    "tampering."
                ),
            },
            {
                "id": "d",
                "text": "Non-repudiation",
                "correct": False,
                "rationale": (
                    "Incorrect. Non-repudiation concerns the ability to prove an action "
                    "was performed by a specific party and prevent denial of that action. "
                    "A crash caused by a packet flood does not involve disputing who "
                    "performed an action."
                ),
            },
        ],
        "explanation": (
            "Denial-of-service conditions that crash a system or halt operations without "
            "altering data or exposing information primarily violate Availability, one of "
            "the three pillars of the CIA triad."
        ),
    },
    {
        "id": "nd1d-012",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "CIA triad and non-repudiation",
        "stem": (
            "A law firm requires every partner to digitally sign settlement agreements "
            "using a private key held on a hardware token, and the resulting signature is "
            "cryptographically bound to the exact document contents and timestamped by a "
            "trusted timestamp authority. A partner later denies having approved a "
            "specific settlement figure. Which security property allows the firm to "
            "refute that denial?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Non-repudiation",
                "correct": True,
                "rationale": (
                    "Correct. Non-repudiation provides proof of the origin and integrity "
                    "of an action such that the signer cannot credibly deny having "
                    "performed it. The hardware-token-bound digital signature, tied to "
                    "the exact document and timestamped, is designed to deliver exactly "
                    "this assurance."
                ),
            },
            {
                "id": "b",
                "text": "Confidentiality",
                "correct": False,
                "rationale": (
                    "Incorrect. Confidentiality protects the settlement agreement's "
                    "contents from unauthorized disclosure; it does not address whether "
                    "the partner can deny signing it."
                ),
            },
            {
                "id": "c",
                "text": "Availability",
                "correct": False,
                "rationale": (
                    "Incorrect. Availability concerns whether the signed document and "
                    "signing system remain accessible when needed; it has no bearing on "
                    "proving who signed the document."
                ),
            },
            {
                "id": "d",
                "text": "Authentication",
                "correct": False,
                "rationale": (
                    "Incorrect. Authentication verified the partner's identity at the "
                    "moment of signing, but by itself it does not create durable, "
                    "provable evidence that survives a later denial — the binding "
                    "signature and timestamp providing that durable proof is "
                    "non-repudiation."
                ),
            },
        ],
        "explanation": (
            "A digital signature cryptographically bound to document content, generated "
            "with a private key only the signer controls, and timestamped, provides "
            "non-repudiation — the inability for the signer to later deny performing the "
            "signing action."
        ),
    },
    # ── 1.2 Deception and disruption technologies ────────────────────────────
    {
        "id": "nd1d-013",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Deception and disruption technologies",
        "stem": (
            "A security team publishes a decoy internal wiki page titled "
            "\"VPN_Root_Credentials_DoNotShare\" that no legitimate employee workflow ever "
            "links to or opens, configured to fire an immediate SOC alert the moment the "
            "page is viewed. Which technique is this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Honeyfile / honeytoken",
                "correct": True,
                "rationale": (
                    "Correct. A decoy document with an enticing name that no legitimate "
                    "process accesses, monitored to trigger an alert on access, is a "
                    "honeyfile (a form of honeytoken) used to detect unauthorized "
                    "reconnaissance or lateral movement."
                ),
            },
            {
                "id": "b",
                "text": "Honeypot",
                "correct": False,
                "rationale": (
                    "Incorrect. A honeypot is a decoy system or service designed to "
                    "attract and study attacker interaction. This is a single decoy "
                    "document, not an entire simulated system, making honeyfile the more "
                    "precise term."
                ),
            },
            {
                "id": "c",
                "text": "Honeynet",
                "correct": False,
                "rationale": (
                    "Incorrect. A honeynet is a full network of interconnected decoy "
                    "systems. A single alerting wiki page is far narrower in scope than a "
                    "honeynet."
                ),
            },
            {
                "id": "d",
                "text": "DNS sinkhole",
                "correct": False,
                "rationale": (
                    "Incorrect. A DNS sinkhole redirects malicious domain resolutions to a "
                    "controlled server to disrupt malware communication; it is unrelated "
                    "to a decoy document designed to bait and detect unauthorized "
                    "viewers."
                ),
            },
        ],
        "explanation": (
            "A single decoy artifact with an enticing name, monitored for unauthorized "
            "access, is a honeyfile/honeytoken — narrower in scope than a honeypot (a "
            "full decoy system) or honeynet (a decoy network)."
        ),
    },
    {
        "id": "nd1d-014",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Deception and disruption technologies",
        "stem": (
            "A threat intelligence team configures an internal DNS resolver so that any "
            "query for a domain known to be malware command-and-control infrastructure is "
            "answered with the IP address of an internal logging server instead of the "
            "attacker's real server, preventing infected hosts from ever reaching the "
            "actual C2 while capturing which hosts attempted the query. Which technique is "
            "this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "DNS sinkhole",
                "correct": True,
                "rationale": (
                    "Correct. A DNS sinkhole intercepts resolution of known-malicious "
                    "domains and redirects them to a controlled server, simultaneously "
                    "disrupting the malware's communication and identifying infected "
                    "hosts — exactly what is described."
                ),
            },
            {
                "id": "b",
                "text": "Honeynet",
                "correct": False,
                "rationale": (
                    "Incorrect. A honeynet is a network of decoy systems designed to "
                    "attract attackers for observation, not a DNS-layer redirection "
                    "technique used to disrupt malware communications."
                ),
            },
            {
                "id": "c",
                "text": "Bogon filtering",
                "correct": False,
                "rationale": (
                    "Incorrect. Bogon filtering blocks traffic from IP address ranges that "
                    "should never appear on the public internet (unallocated or "
                    "reserved space); it has nothing to do with redirecting DNS lookups "
                    "for known-malicious domains."
                ),
            },
            {
                "id": "d",
                "text": "Honeytoken",
                "correct": False,
                "rationale": (
                    "Incorrect. A honeytoken is a decoy piece of data (credential, file, "
                    "record) used as a tripwire. This scenario describes DNS-layer "
                    "redirection of malicious domain lookups, which is a sinkhole, not a "
                    "planted decoy artifact."
                ),
            },
        ],
        "explanation": (
            "Redirecting resolution of malicious domains to a controlled server both "
            "disrupts malware C2 communication and reveals infected hosts — this is the "
            "defining function of a DNS sinkhole."
        ),
    },
    # ── 1.2 Gap analysis ──────────────────────────────────────────────────────
    {
        "id": "nd1d-015",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Gap analysis",
        "stem": (
            "Ahead of a cyber-insurance renewal, a risk manager compares the "
            "organization's current backup, MFA, and endpoint-detection practices against "
            "the insurer's minimum underwriting requirements and produces a document "
            "listing exactly which requirements are unmet and what remediation each one "
            "needs. Which activity was performed?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Gap analysis",
                "correct": True,
                "rationale": (
                    "Correct. Comparing current-state controls against a defined set of "
                    "required controls (the insurer's underwriting requirements) and "
                    "documenting the specific shortfalls and remediation needed is the "
                    "definition of a gap analysis."
                ),
            },
            {
                "id": "b",
                "text": "Business impact analysis",
                "correct": False,
                "rationale": (
                    "Incorrect. A business impact analysis quantifies the operational and "
                    "financial impact of a disruption to prioritize recovery, such as "
                    "calculating RTOs and RPOs; it does not compare current controls "
                    "against a required baseline."
                ),
            },
            {
                "id": "c",
                "text": "Vulnerability assessment",
                "correct": False,
                "rationale": (
                    "Incorrect. A vulnerability assessment identifies technical "
                    "weaknesses in systems (e.g., missing patches, misconfigurations) "
                    "through scanning, not a documentation-based comparison against an "
                    "insurer's policy requirements."
                ),
            },
            {
                "id": "d",
                "text": "Penetration test",
                "correct": False,
                "rationale": (
                    "Incorrect. A penetration test actively attempts to exploit "
                    "vulnerabilities to demonstrate real-world impact; it does not compare "
                    "documented practices against a checklist of insurer requirements."
                ),
            },
        ],
        "explanation": (
            "A gap analysis measures the difference between an organization's current "
            "security posture and a target state (regulation, framework, or contractual "
            "requirement) and documents specific deficiencies to remediate."
        ),
    },
    {
        "id": "nd1d-016",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Gap analysis",
        "stem": (
            "During a gap analysis against the CIS Critical Security Controls, a security "
            "analyst finds that the organization has already purchased and licensed a "
            "capable DLP platform, but it was never configured to monitor outbound email "
            "attachments as CIS Control 3 requires. Which remediation approach BEST "
            "closes this specific gap with the LEAST additional cost?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Configure the existing DLP platform's outbound email policies rather than procuring a new tool",
                "correct": True,
                "rationale": (
                    "Correct. Because the organization already owns a capable DLP "
                    "platform, the gap is a configuration deficiency, not a missing "
                    "capability. Enabling and tuning the existing tool's outbound "
                    "email-monitoring policies closes the gap without new procurement "
                    "cost."
                ),
            },
            {
                "id": "b",
                "text": "Procure a new, dedicated email-security gateway with built-in DLP",
                "correct": False,
                "rationale": (
                    "Incorrect. Purchasing a redundant new tool ignores the fact that a "
                    "capable DLP platform is already licensed and simply needs to be "
                    "configured; this option is unnecessarily costly for the identified "
                    "gap."
                ),
            },
            {
                "id": "c",
                "text": "Accept the risk and document it in the risk register without further action",
                "correct": False,
                "rationale": (
                    "Incorrect. Risk acceptance is inappropriate here because a low-cost, "
                    "readily available remediation (enabling existing functionality) "
                    "exists; accepting the risk unnecessarily leaves a closeable gap "
                    "open."
                ),
            },
            {
                "id": "d",
                "text": "Transfer the risk by purchasing a cyber-insurance rider covering data exfiltration",
                "correct": False,
                "rationale": (
                    "Incorrect. Risk transfer through insurance does not close a control "
                    "gap that already has a simple, low-cost technical fix; it would leave "
                    "outbound email attachments unmonitored."
                ),
            },
        ],
        "explanation": (
            "Effective gap remediation starts by checking whether existing, "
            "already-licensed tools can be configured to meet the requirement before "
            "recommending new spend, risk acceptance, or risk transfer."
        ),
    },
    # ── 1.2 Physical security ─────────────────────────────────────────────────
    {
        "id": "nd1d-017",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Physical security",
        "stem": (
            "A colocation data center wants to ensure that if its badge-access system "
            "loses network connectivity to the central authentication server, the "
            "electronic locks default to a locked state rather than granting free entry, "
            "even though this could momentarily delay legitimate staff. Which principle "
            "does this locking behavior reflect?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Fail-closed (fail-secure)",
                "correct": True,
                "rationale": (
                    "Correct. Fail-closed (fail-secure) design ensures a control defaults "
                    "to the more restrictive, secure state during a failure — here, "
                    "locking the door rather than allowing unrestricted entry when "
                    "connectivity is lost."
                ),
            },
            {
                "id": "b",
                "text": "Fail-open",
                "correct": False,
                "rationale": (
                    "Incorrect. Fail-open would mean the lock defaults to an unlocked "
                    "state during failure to prioritize accessibility (often used for "
                    "life-safety egress); the scenario explicitly describes the opposite "
                    "behavior — the door stays locked."
                ),
            },
            {
                "id": "c",
                "text": "Fault tolerance",
                "correct": False,
                "rationale": (
                    "Incorrect. Fault tolerance refers to a system's ability to continue "
                    "operating despite a component failure (e.g., redundant power "
                    "supplies), not the specific security-versus-availability tradeoff "
                    "chosen for a lock's failure state."
                ),
            },
            {
                "id": "d",
                "text": "Defense in depth",
                "correct": False,
                "rationale": (
                    "Incorrect. Defense in depth refers to layering multiple, independent "
                    "controls; it does not describe the specific behavior of a single "
                    "lock defaulting to locked during a connectivity failure."
                ),
            },
        ],
        "explanation": (
            "A lock that defaults to locked during a failure is fail-closed/fail-secure, "
            "prioritizing confidentiality and integrity over availability — the opposite "
            "of fail-open designs typically reserved for fire egress doors."
        ),
    },
    {
        "id": "nd1d-018",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Physical security",
        "stem": (
            "A semiconductor fab's cleanroom entrance uses a sequence of two "
            "interlocked doors, where the outer door must fully close and lock before the "
            "inner door will unlock, and only one door can ever be open at a time. Which "
            "control is BEST described?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Access control vestibule (mantrap)",
                "correct": True,
                "rationale": (
                    "Correct. An access control vestibule uses interlocked doors where "
                    "only one door can be open at a time, preventing tailgating and "
                    "controlling airflow/contamination between zones — matching the "
                    "described two-door interlock exactly."
                ),
            },
            {
                "id": "b",
                "text": "Faraday cage",
                "correct": False,
                "rationale": (
                    "Incorrect. A Faraday cage blocks electromagnetic signals from "
                    "entering or leaving a space; it has nothing to do with an interlocked "
                    "double-door entry sequence."
                ),
            },
            {
                "id": "c",
                "text": "Bollard array",
                "correct": False,
                "rationale": (
                    "Incorrect. Bollards are vehicle-barrier posts that stop "
                    "vehicle-ramming attacks; they do not control pedestrian entry through "
                    "interlocked doors."
                ),
            },
            {
                "id": "d",
                "text": "Turnstile",
                "correct": False,
                "rationale": (
                    "Incorrect. A turnstile is a single rotating barrier allowing one "
                    "person through per authorized pass; it does not involve two "
                    "interlocked doors where only one can be open at a time."
                ),
            },
        ],
        "explanation": (
            "A two-door interlock where only one door opens at a time is a classic access "
            "control vestibule (mantrap), used both to prevent tailgating and, in "
            "cleanroom contexts, to control particulate/airflow between zones."
        ),
    },
    # ── 1.2 Zero Trust architecture ──────────────────────────────────────────
    {
        "id": "nd1d-019",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Zero Trust architecture",
        "stem": (
            "In a NIST SP 800-207 Zero Trust architecture, after the Policy Decision "
            "Point approves an access request, which component is responsible for "
            "actually establishing, monitoring, and ultimately terminating the "
            "connection between the subject and the requested resource?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Policy Enforcement Point",
                "correct": True,
                "rationale": (
                    "Correct. The Policy Enforcement Point (PEP) sits in the data plane "
                    "and is responsible for enabling, monitoring, and terminating the "
                    "actual connection between subject and resource based on the "
                    "decision handed down by the Policy Decision Point."
                ),
            },
            {
                "id": "b",
                "text": "Policy Engine",
                "correct": False,
                "rationale": (
                    "Incorrect. The Policy Engine is the component within the Policy "
                    "Decision Point that calculates the trust score and ultimate access "
                    "decision; it does not itself enforce or monitor the live "
                    "connection."
                ),
            },
            {
                "id": "c",
                "text": "Policy Administrator",
                "correct": False,
                "rationale": (
                    "Incorrect. The Policy Administrator, also part of the Policy "
                    "Decision Point, executes the Policy Engine's decision by generating "
                    "session-specific authentication tokens or credentials and "
                    "communicating with the PEP — it does not directly monitor or "
                    "terminate the ongoing data-plane connection."
                ),
            },
            {
                "id": "d",
                "text": "Subject database",
                "correct": False,
                "rationale": (
                    "Incorrect. The subject database is a data source used by the Policy "
                    "Engine to evaluate identity attributes during the decision process; "
                    "it plays no role in establishing or monitoring the live "
                    "connection."
                ),
            },
        ],
        "explanation": (
            "In the NIST 800-207 model, the control plane (Policy Engine + Policy "
            "Administrator) decides whether access is allowed, while the Policy "
            "Enforcement Point in the data plane carries out that decision by actually "
            "establishing, monitoring, and terminating the connection."
        ),
    },
    {
        "id": "nd1d-020",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Zero Trust architecture",
        "stem": (
            "A streaming media company implements a Zero Trust program in which every "
            "microservice must present a short-lived, cryptographically signed identity "
            "certificate to every other microservice it calls, regardless of whether both "
            "services run inside the same trusted data center network segment. Which "
            "Zero Trust principle does this MOST directly reflect?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Never trust, always verify — eliminating implicit trust zones",
                "correct": True,
                "rationale": (
                    "Correct. Requiring mutual, cryptographic verification between every "
                    "microservice call — even within the same network segment — "
                    "eliminates the assumption that anything inside the perimeter is "
                    "inherently trustworthy, which is the core Zero Trust tenet."
                ),
            },
            {
                "id": "b",
                "text": "Defense in depth through layered perimeter firewalls",
                "correct": False,
                "rationale": (
                    "Incorrect. This scenario explicitly removes reliance on network "
                    "segment/perimeter trust in favor of per-request identity "
                    "verification, which is the opposite of relying on layered "
                    "perimeter firewalls as the primary control."
                ),
            },
            {
                "id": "c",
                "text": "Least privilege applied only to human user accounts",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario describes service-to-service (workload) "
                    "identity verification, not access controls scoped to human user "
                    "accounts; least privilege for humans is a related but distinct "
                    "concept not depicted here."
                ),
            },
            {
                "id": "d",
                "text": "Network segmentation as the sole control boundary",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario shows verification occurring even between "
                    "services already inside the same segment, demonstrating that "
                    "segmentation alone is explicitly NOT treated as sufficient — "
                    "contradicting this option."
                ),
            },
        ],
        "explanation": (
            "Zero Trust replaces implicit trust based on network location with continuous, "
            "explicit verification of every request — including workload-to-workload "
            "calls inside a traditionally trusted segment."
        ),
    },
    # ── 1.3 Change management ────────────────────────────────────────────────
    {
        "id": "nd1d-021",
        "domain": 1,
        "objective": "1.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Change management",
        "stem": (
            "A network engineer submits a request to modify core routing policy during "
            "next month's maintenance window. Before the CAB will approve it, which "
            "document MUST the engineer provide that specifically describes the exact "
            "steps to return the network to its prior working state if the change causes "
            "an outage?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Backout (rollback) plan",
                "correct": True,
                "rationale": (
                    "Correct. A backout plan documents the precise steps required to "
                    "revert a change and restore the previous known-good state if the "
                    "change fails or causes unintended impact — exactly what the CAB is "
                    "requiring here."
                ),
            },
            {
                "id": "b",
                "text": "Business impact analysis",
                "correct": False,
                "rationale": (
                    "Incorrect. A business impact analysis quantifies the consequences of "
                    "a disruption to critical processes for recovery planning; it does not "
                    "describe the specific technical steps to undo a change."
                ),
            },
            {
                "id": "c",
                "text": "Service level agreement",
                "correct": False,
                "rationale": (
                    "Incorrect. An SLA defines expected service performance and "
                    "availability commitments between parties; it does not contain "
                    "technical rollback steps for a specific configuration change."
                ),
            },
            {
                "id": "d",
                "text": "Data retention policy",
                "correct": False,
                "rationale": (
                    "Incorrect. A data retention policy governs how long data is kept "
                    "before disposal; it is unrelated to reverting a failed network "
                    "change."
                ),
            },
        ],
        "explanation": (
            "Change management requires a documented backout/rollback plan before "
            "approval so that, if a change causes unexpected impact, the team can quickly "
            "and reliably restore the prior working configuration."
        ),
    },
    {
        "id": "nd1d-022",
        "domain": 1,
        "objective": "1.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Change management",
        "stem": (
            "A DevOps team's request for change (RFC) to migrate a customer-facing API "
            "to a new authentication library lists the maintenance window, the rollback "
            "steps, and the CAB's approval signature, but omits any list of which "
            "downstream services and customer integrations currently depend on the "
            "existing authentication flow. Which consequence is MOST likely if the CAB "
            "approves the RFC as submitted?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Dependent integrations that were never identified could break during the migration because their reliance on the old flow was never assessed",
                "correct": True,
                "rationale": (
                    "Correct. Without an impact analysis identifying downstream "
                    "dependencies, the team has no visibility into which integrations "
                    "rely on the current authentication flow, so those integrations could "
                    "silently fail during or after the migration with no advance "
                    "mitigation planned."
                ),
            },
            {
                "id": "b",
                "text": "The change cannot be rolled back if it fails, since rollback steps were omitted from the RFC",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario states the RFC does include rollback "
                    "(backout) steps; the missing element is the impact analysis of "
                    "downstream dependencies, not the rollback plan."
                ),
            },
            {
                "id": "c",
                "text": "The maintenance window will be automatically extended by the CAB to compensate for the missing information",
                "correct": False,
                "rationale": (
                    "Incorrect. A CAB does not automatically extend a maintenance window "
                    "to compensate for missing documentation; an incomplete RFC risks "
                    "unplanned impact during the originally scheduled window, not an "
                    "automatic extension."
                ),
            },
            {
                "id": "d",
                "text": "The change becomes exempt from future CAB review because it was already approved once",
                "correct": False,
                "rationale": (
                    "Incorrect. Approval of one RFC does not exempt future related "
                    "changes from CAB review; each subsequent change still requires its "
                    "own evaluation, and this option has no bearing on the risk created "
                    "by omitting the dependency impact analysis."
                ),
            },
        ],
        "explanation": (
            "An RFC's impact analysis is what identifies downstream systems and "
            "customers dependent on the component being changed. Omitting it means "
            "those dependencies are never assessed, risking undetected breakage during "
            "the migration even when rollback steps and a maintenance window are "
            "documented."
        ),
    },
    # ── 1.4 Blockchain and open public ledger ────────────────────────────────
    {
        "id": "nd1d-023",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Blockchain and open public ledger",
        "stem": (
            "A diamond wholesaler consortium wants a shared ledger recording every "
            "custody transfer of a certified stone from mine to retailer, such that any "
            "single participant's attempt to retroactively alter a past transfer record "
            "is immediately detectable by all other participants because it would break "
            "the cryptographic chain linking each block to the one before it. Which "
            "property of the underlying technology provides this tamper-evidence?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Each block contains a cryptographic hash of the previous block, so altering any historical block invalidates every subsequent hash",
                "correct": True,
                "rationale": (
                    "Correct. Blockchain tamper-evidence comes from each block embedding "
                    "a hash of the prior block's contents; changing any historical record "
                    "changes its hash, which no longer matches what the next block "
                    "references, cascading a detectable mismatch through the entire "
                    "chain."
                ),
            },
            {
                "id": "b",
                "text": "A central administrator digitally signs every block before it is added to the ledger",
                "correct": False,
                "rationale": (
                    "Incorrect. A central authority signing every block describes a "
                    "centralized, permissioned signing model, not the decentralized, "
                    "hash-linked structure that makes a distributed ledger tamper-evident "
                    "among many independent participants."
                ),
            },
            {
                "id": "c",
                "text": "Records are encrypted at rest using a symmetric key shared by all participants",
                "correct": False,
                "rationale": (
                    "Incorrect. Symmetric-key encryption at rest protects confidentiality "
                    "of stored data but does not, by itself, provide tamper-evidence "
                    "through chained cryptographic linkage between records."
                ),
            },
            {
                "id": "d",
                "text": "Each participant stores an independent, unlinked copy of only their own transactions",
                "correct": False,
                "rationale": (
                    "Incorrect. Storing only unlinked, individual transaction copies "
                    "would not create the cross-block cryptographic dependency needed to "
                    "detect retroactive tampering; the defining feature is the chained "
                    "hash linkage across the shared, replicated ledger."
                ),
            },
        ],
        "explanation": (
            "Blockchain's tamper-evidence comes from chaining blocks via cryptographic "
            "hashes — altering any past block changes its hash and breaks the link to "
            "subsequent blocks, making retroactive edits immediately detectable across "
            "the distributed ledger."
        ),
    },
    {
        "id": "nd1d-024",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Blockchain and open public ledger",
        "stem": (
            "A group of regional utility companies wants to jointly track carbon-credit "
            "transfers on a shared ledger, but requires that only their twelve pre-vetted "
            "member organizations be allowed to validate new blocks, while the public may "
            "still view transaction history for transparency reporting. Which ledger "
            "model BEST fits this requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Permissioned (consortium) blockchain",
                "correct": True,
                "rationale": (
                    "Correct. A permissioned consortium blockchain restricts block "
                    "validation rights to a defined set of pre-approved members while "
                    "still allowing broader read access, matching the requirement of "
                    "twelve vetted validators with public transparency."
                ),
            },
            {
                "id": "b",
                "text": "Fully public, permissionless blockchain",
                "correct": False,
                "rationale": (
                    "Incorrect. A permissionless blockchain allows anyone to participate "
                    "in validating blocks (e.g., via proof-of-work mining), which "
                    "conflicts with the requirement that only twelve vetted members may "
                    "validate."
                ),
            },
            {
                "id": "c",
                "text": "Private, single-organization ledger",
                "correct": False,
                "rationale": (
                    "Incorrect. A private, single-organization ledger is controlled "
                    "entirely by one entity; the scenario explicitly involves multiple "
                    "independent utility companies jointly validating transactions, which "
                    "requires a multi-party consortium model, not a single-owner "
                    "private ledger."
                ),
            },
            {
                "id": "d",
                "text": "Centralized relational database with role-based access control",
                "correct": False,
                "rationale": (
                    "Incorrect. A centralized database relies on one trusted operator and "
                    "does not provide the decentralized, cryptographically verifiable "
                    "consensus among independent member organizations that a consortium "
                    "blockchain is specifically chosen to deliver."
                ),
            },
        ],
        "explanation": (
            "A permissioned consortium blockchain restricts validation to a defined "
            "group of trusted members while optionally allowing public read access — "
            "distinct from fully public permissionless chains, single-owner private "
            "ledgers, or a plain centralized database."
        ),
    },
    # ── 1.4 Certificates ──────────────────────────────────────────────────────
    {
        "id": "nd1d-025",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Certificates",
        "stem": (
            "A hotel chain operates dozens of subdomains (booking.example.com, "
            "loyalty.example.com, spa.example.com) all hosted behind the same load "
            "balancer and wants a single certificate that secures every current and "
            "future subdomain without issuing a separate certificate each time a new "
            "subdomain launches. Which certificate type BEST meets this need?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Wildcard certificate",
                "correct": True,
                "rationale": (
                    "Correct. A wildcard certificate (e.g., issued for *.example.com) "
                    "secures an arbitrary, unlimited number of first-level subdomains "
                    "under a single domain with one certificate, exactly matching the "
                    "requirement to cover current and future subdomains without "
                    "reissuing."
                ),
            },
            {
                "id": "b",
                "text": "Self-signed certificate",
                "correct": False,
                "rationale": (
                    "Incorrect. A self-signed certificate is not issued by a trusted "
                    "public CA and would trigger browser trust warnings for customers; it "
                    "also does not inherently provide subdomain-wildcard coverage."
                ),
            },
            {
                "id": "c",
                "text": "Code-signing certificate",
                "correct": False,
                "rationale": (
                    "Incorrect. A code-signing certificate verifies the authenticity and "
                    "integrity of executable software, not the identity of a web "
                    "server's TLS endpoint across multiple subdomains."
                ),
            },
            {
                "id": "d",
                "text": "Single-domain (SAN with one name) certificate reissued for each new subdomain",
                "correct": False,
                "rationale": (
                    "Incorrect. Reissuing a new single-domain certificate every time a "
                    "subdomain launches is exactly the operational burden the hotel chain "
                    "wants to avoid; a wildcard certificate eliminates that repeated "
                    "reissuance."
                ),
            },
        ],
        "explanation": (
            "A wildcard certificate covers unlimited subdomains under one domain with a "
            "single certificate, avoiding the need to issue and manage a new certificate "
            "for every new subdomain — though it does concentrate risk since a compromised "
            "wildcard private key exposes every covered subdomain."
        ),
    },
    {
        "id": "nd1d-026",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Certificates",
        "stem": (
            "A financial services firm's TLS clients need to verify certificate "
            "revocation status without transmitting the specific certificate's serial "
            "number to a third-party OCSP responder, which would otherwise let the "
            "responder infer which websites a given client is visiting. Which mechanism "
            "addresses this privacy concern while still delivering timely revocation "
            "status during the TLS handshake?"
        ),
        "options": [
            {
                "id": "a",
                "text": "OCSP stapling",
                "correct": True,
                "rationale": (
                    "Correct. With OCSP stapling, the web server itself periodically "
                    "queries the OCSP responder and \"staples\" the signed, time-stamped "
                    "response to the TLS handshake it sends to clients. The client never "
                    "contacts the OCSP responder directly, eliminating the privacy leak "
                    "of exposing browsing destinations to that third party."
                ),
            },
            {
                "id": "b",
                "text": "Downloading and checking the full Certificate Revocation List (CRL) for every connection",
                "correct": False,
                "rationale": (
                    "Incorrect. Full CRL downloads avoid contacting an OCSP responder per "
                    "connection but are large, infrequently updated, and impose "
                    "significant bandwidth/latency overhead on every client — they do not "
                    "provide the timely, low-overhead status stapling provides."
                ),
            },
            {
                "id": "c",
                "text": "Certificate pinning",
                "correct": False,
                "rationale": (
                    "Incorrect. Certificate pinning hardcodes an expected public key or "
                    "certificate to prevent MITM attacks with rogue CA-issued "
                    "certificates; it does not address real-time revocation status "
                    "checking or the OCSP privacy issue described."
                ),
            },
            {
                "id": "d",
                "text": "Extended Validation (EV) certificates",
                "correct": False,
                "rationale": (
                    "Incorrect. EV certificates provide a higher level of identity "
                    "vetting for the certificate subject during issuance; they do not "
                    "change how or whether revocation status is queried during the TLS "
                    "handshake."
                ),
            },
        ],
        "explanation": (
            "OCSP stapling moves the revocation-status query from the client to the "
            "server, which attaches a signed, cached OCSP response to its own TLS "
            "handshake — improving both performance and client privacy compared to "
            "clients directly querying the OCSP responder."
        ),
    },
    # ── 1.4 Cryptographic hardware ───────────────────────────────────────────
    {
        "id": "nd1d-027",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Cryptographic hardware",
        "stem": (
            "A gaming console manufacturer solders a dedicated chip onto every "
            "motherboard that generates and seals disk-encryption keys to that specific "
            "device's measured boot state, refusing to release the keys if any boot-stage "
            "firmware hash does not match the expected value, thereby preventing the "
            "encrypted drive from being read if moved to another console. Which "
            "technology is this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Trusted Platform Module (TPM)",
                "correct": True,
                "rationale": (
                    "Correct. A TPM is a dedicated hardware chip that seals cryptographic "
                    "keys to the device's measured boot state, releasing them only when "
                    "the boot chain's measurements match expected values — exactly the "
                    "behavior described for binding keys to a specific device."
                ),
            },
            {
                "id": "b",
                "text": "Hardware security module (HSM)",
                "correct": False,
                "rationale": (
                    "Incorrect. An HSM is typically a standalone, high-throughput "
                    "cryptographic appliance used for centralized key management and "
                    "signing (often in data centers), not a chip soldered to a "
                    "consumer device's motherboard that binds keys to that specific "
                    "device's measured boot state."
                ),
            },
            {
                "id": "c",
                "text": "Secure enclave in the main application processor",
                "correct": False,
                "rationale": (
                    "Incorrect. A secure enclave is an isolated execution environment "
                    "within the main SoC used for tasks like biometric matching; the "
                    "scenario specifically describes a dedicated, separate chip performing "
                    "measured-boot key sealing, which is the defining TPM function."
                ),
            },
            {
                "id": "d",
                "text": "USB security key (FIDO2 token)",
                "correct": False,
                "rationale": (
                    "Incorrect. A USB FIDO2 security key is a removable authentication "
                    "device a user carries and inserts; it is not a soldered, "
                    "device-bound chip that seals disk-encryption keys to a measured boot "
                    "state."
                ),
            },
        ],
        "explanation": (
            "A TPM's core function is sealing keys to a device's measured boot state, "
            "releasing them only if the boot chain is unaltered — this binds encrypted "
            "storage to that specific physical device."
        ),
    },
    {
        "id": "nd1d-028",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Cryptographic hardware",
        "stem": (
            "A stock exchange's clearinghouse needs a dedicated appliance capable of "
            "performing tens of thousands of ECDSA signing operations per second to "
            "authorize trade settlements, must be FIPS 140-2 Level 3 validated, and must "
            "physically zeroize all stored keys if the chassis is tampered with or "
            "opened. Which solution BEST fits these requirements?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A dedicated hardware security module (HSM)",
                "correct": True,
                "rationale": (
                    "Correct. A dedicated HSM is purpose-built for very high-volume "
                    "cryptographic operations, offers FIPS 140-2 Level 3 tamper-resistant "
                    "validation, and physically zeroizes stored keys on detected "
                    "tampering — precisely matching the clearinghouse's throughput and "
                    "tamper-response requirements."
                ),
            },
            {
                "id": "b",
                "text": "A TPM embedded on each settlement server's motherboard",
                "correct": False,
                "rationale": (
                    "Incorrect. A TPM is designed for low-throughput operations like "
                    "sealing boot-time keys on a single device; it cannot deliver the "
                    "tens-of-thousands-of-operations-per-second throughput a "
                    "clearinghouse's signing workload requires."
                ),
            },
            {
                "id": "c",
                "text": "A software-based key vault running as a virtual machine",
                "correct": False,
                "rationale": (
                    "Incorrect. A software-only key vault cannot provide FIPS 140-2 "
                    "Level 3 hardware tamper-resistance or physical zeroization on chassis "
                    "intrusion, both of which require dedicated hardware."
                ),
            },
            {
                "id": "d",
                "text": "A YubiKey-style USB security token issued to each administrator",
                "correct": False,
                "rationale": (
                    "Incorrect. A USB security token is designed for individual user "
                    "authentication, not for centralized, extremely high-throughput "
                    "transaction signing with chassis-level tamper zeroization."
                ),
            },
        ],
        "explanation": (
            "High-throughput, tamper-responsive, FIPS 140-2 Level 3-validated "
            "cryptographic operations at data-center scale are the defining use case for "
            "a dedicated HSM, distinct from lower-throughput TPMs or single-user USB "
            "tokens."
        ),
    },
    # ── 1.4 Cryptographic hardware and key-management tools ─────────────────
    {
        "id": "nd1d-029",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Cryptographic hardware and key-management tools",
        "stem": (
            "A software-as-a-service company wants its microservices to request "
            "database decryption keys at runtime via API calls, with every key request "
            "automatically logged, keys automatically rotated on a schedule without "
            "developer intervention, and access controlled through fine-grained IAM "
            "policies rather than any physical device shipped to the data center. Which "
            "solution BEST meets these requirements?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A cloud-based key management service (KMS)",
                "correct": True,
                "rationale": (
                    "Correct. A cloud KMS provides API-driven key retrieval, automatic "
                    "logging of every cryptographic operation, scheduled automatic key "
                    "rotation, and fine-grained IAM-based access control — all without "
                    "requiring physical hardware provisioning, matching every requirement "
                    "listed."
                ),
            },
            {
                "id": "b",
                "text": "A physical HSM appliance shipped to and racked in the company's own data center",
                "correct": False,
                "rationale": (
                    "Incorrect. The requirement explicitly excludes any physical device "
                    "shipped to the data center; a cloud KMS delivers the needed "
                    "capabilities without that physical hardware dependency."
                ),
            },
            {
                "id": "c",
                "text": "A shared spreadsheet listing each microservice's decryption key, access-controlled via a shared drive permission",
                "correct": False,
                "rationale": (
                    "Incorrect. A spreadsheet provides no automated rotation, no "
                    "API-driven runtime retrieval, and no reliable per-request audit "
                    "logging — none of the automation and access-control requirements are "
                    "met."
                ),
            },
            {
                "id": "d",
                "text": "Hardcoding each key directly into the microservice's source code repository",
                "correct": False,
                "rationale": (
                    "Incorrect. Hardcoding keys in source code is a severe security "
                    "anti-pattern that provides no rotation, no centralized logging, and "
                    "no fine-grained access control, directly contradicting every stated "
                    "requirement."
                ),
            },
        ],
        "explanation": (
            "A cloud KMS is purpose-built for API-driven, auditable, automatically "
            "rotated key retrieval governed by IAM policy — without requiring physical "
            "hardware deployment, unlike a rack-mounted HSM."
        ),
    },
    {
        "id": "nd1d-030",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Cryptographic hardware and key-management tools",
        "stem": (
            "A healthcare SaaS provider is designing key-management practices to protect "
            "patient records encrypted at rest. Which TWO of the following are "
            "recognized key-management best practices the design should incorporate? "
            "(Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Encrypt each record's data-encryption key (DEK) with a separate key-encryption key (KEK) stored in a hardened KMS, rather than storing DEKs in plaintext",
                "correct": True,
                "rationale": (
                    "Correct. Envelope encryption — protecting a DEK with a KEK stored in "
                    "a hardened, access-controlled KMS — is a widely recognized key-"
                    "management best practice that limits exposure if the encrypted data "
                    "store itself is breached."
                ),
            },
            {
                "id": "b",
                "text": "Rotate encryption keys on a defined schedule and immediately upon suspected compromise",
                "correct": True,
                "rationale": (
                    "Correct. Scheduled and event-driven key rotation limits the amount "
                    "of data exposed by any single compromised key and is a core "
                    "key-management best practice, especially critical for regulated "
                    "healthcare data."
                ),
            },
            {
                "id": "c",
                "text": "Store the master encryption key alongside the encrypted database in the same storage bucket for faster access during recovery",
                "correct": False,
                "rationale": (
                    "Incorrect. Storing the master key with the data it protects defeats "
                    "the purpose of encryption — anyone who obtains the storage bucket "
                    "obtains both the ciphertext and the key needed to decrypt it, which "
                    "is a well-known anti-pattern, not a best practice."
                ),
            },
            {
                "id": "d",
                "text": "Grant every application service account permanent, unrestricted access to all encryption keys to simplify development",
                "correct": False,
                "rationale": (
                    "Incorrect. This violates least privilege and separation of duties; "
                    "broad, permanent key access increases blast radius if any single "
                    "service account is compromised, which is the opposite of sound "
                    "key-management practice."
                ),
            },
            {
                "id": "e",
                "text": "Disable all audit logging of key usage to reduce storage costs",
                "correct": False,
                "rationale": (
                    "Incorrect. Disabling audit logging removes the ability to detect "
                    "unauthorized key use or investigate incidents, directly undermining "
                    "accountability required for regulated patient data."
                ),
            },
        ],
        "explanation": (
            "Sound key-management design uses envelope encryption (DEK protected by a "
            "KEK in a hardened KMS), scheduled/event-driven rotation, least-privilege "
            "access, and full audit logging — never co-locating keys with the data they "
            "protect or granting unrestricted permanent access."
        ),
    },
    # ── 1.4 Hashing and salting ───────────────────────────────────────────────
    {
        "id": "nd1d-031",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Hashing and salting",
        "stem": (
            "A forensic examiner computes the SHA-256 hash of a seized hard drive image "
            "immediately after acquisition and again just before presenting the evidence "
            "in court, confirming both values match exactly. Which property is this "
            "process PRIMARILY demonstrating?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Data integrity of the forensic image",
                "correct": True,
                "rationale": (
                    "Correct. Comparing hash values computed at acquisition and again "
                    "before presentation verifies the image has not been altered — this "
                    "demonstrates data integrity, a critical requirement for maintaining "
                    "evidentiary chain of custody."
                ),
            },
            {
                "id": "b",
                "text": "Confidentiality of the drive's contents",
                "correct": False,
                "rationale": (
                    "Incorrect. Hashing does not protect data from disclosure; a hash "
                    "value reveals nothing about confidentiality controls and does not "
                    "encrypt the underlying data."
                ),
            },
            {
                "id": "c",
                "text": "Non-repudiation of the examiner's actions",
                "correct": False,
                "rationale": (
                    "Incorrect. Non-repudiation requires a mechanism (such as a digital "
                    "signature bound to an identity) proving who performed an action; a "
                    "plain hash comparison alone verifies the data's integrity, not who "
                    "handled it."
                ),
            },
            {
                "id": "d",
                "text": "Key stretching resistance to brute-force attacks",
                "correct": False,
                "rationale": (
                    "Incorrect. Key stretching applies to password-hashing algorithms "
                    "designed to slow brute-force attempts (e.g., PBKDF2, bcrypt); SHA-256 "
                    "used here for evidence integrity verification is not being applied "
                    "as a password key-stretching function."
                ),
            },
        ],
        "explanation": (
            "Matching hash values computed at two points in time confirm the data was "
            "not altered between those points — this is data integrity verification, "
            "essential to preserving forensic chain of custody."
        ),
    },
    {
        "id": "nd1d-032",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Hashing and salting",
        "stem": (
            "A security architect reviews a legacy authentication system and finds it "
            "stores passwords as unsalted MD5 hashes. An attacker who steals the database "
            "can instantly identify every user who shares the password \"Summer2024!\" "
            "because their hash values are identical, and can also use precomputed lookup "
            "tables to reverse many hashes in seconds. Which remediation MOST directly "
            "addresses BOTH weaknesses described?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Replace the scheme with a salted, memory-hard algorithm such as bcrypt or Argon2",
                "correct": True,
                "rationale": (
                    "Correct. Adding a unique, random salt per user ensures identical "
                    "passwords no longer produce identical hashes, defeating both "
                    "identical-hash correlation and precomputed rainbow-table lookups. "
                    "Using a memory-hard algorithm like bcrypt or Argon2 additionally "
                    "resists fast GPU/ASIC brute-forcing, addressing both weaknesses "
                    "simultaneously."
                ),
            },
            {
                "id": "b",
                "text": "Keep MD5 but increase the password minimum length requirement to 16 characters",
                "correct": False,
                "rationale": (
                    "Incorrect. Longer passwords alone do not add a per-user salt, so "
                    "identical passwords would still produce identical MD5 hashes, and "
                    "MD5 remains fast and precomputation-vulnerable regardless of "
                    "password length."
                ),
            },
            {
                "id": "c",
                "text": "Encrypt the existing MD5 hash column with a single, shared AES key",
                "correct": False,
                "rationale": (
                    "Incorrect. Encrypting the hash column protects the database at rest "
                    "but does nothing to prevent identical plaintext passwords from "
                    "producing identical hash values once decrypted, and does not address "
                    "MD5's inherent speed and precomputation vulnerabilities."
                ),
            },
            {
                "id": "d",
                "text": "Switch from MD5 to SHA-256 without adding a salt",
                "correct": False,
                "rationale": (
                    "Incorrect. SHA-256 is cryptographically stronger than MD5 but is "
                    "still a fast, general-purpose hash without salting; identical "
                    "passwords would still yield identical hashes, and rainbow-table-style "
                    "precomputation attacks remain feasible against an unsalted scheme."
                ),
            },
        ],
        "explanation": (
            "Salting ensures identical plaintext passwords never produce identical stored "
            "hashes, and a slow, memory-hard algorithm like bcrypt or Argon2 resists both "
            "precomputed lookup tables and brute-force cracking — together resolving both "
            "weaknesses of the legacy unsalted MD5 scheme."
        ),
    },
    # ── 1.4 Obfuscation techniques ────────────────────────────────────────────
    {
        "id": "nd1d-033",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Obfuscation techniques",
        "stem": (
            "A mobile game studio's build pipeline transforms every meaningful class and "
            "method name in the compiled Android APK into short, meaningless identifiers "
            "such as \"c0.a\" and \"c0.b\", and restructures the control flow with "
            "opaque predicates, specifically to slow down a competitor attempting to "
            "reverse-engineer the game's anti-cheat logic. Which technique is this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Code obfuscation",
                "correct": True,
                "rationale": (
                    "Correct. Renaming identifiers to meaningless strings and inserting "
                    "opaque control-flow structures to hinder human and automated "
                    "reverse-engineering, while preserving functional behavior, is the "
                    "definition of code obfuscation."
                ),
            },
            {
                "id": "b",
                "text": "Data masking",
                "correct": False,
                "rationale": (
                    "Incorrect. Data masking replaces sensitive data values (like SSNs or "
                    "card numbers) with realistic but fictitious substitutes for "
                    "non-production use; it does not describe transforming compiled code "
                    "structure to resist reverse-engineering."
                ),
            },
            {
                "id": "c",
                "text": "Tokenization",
                "correct": False,
                "rationale": (
                    "Incorrect. Tokenization substitutes sensitive data values with "
                    "non-sensitive surrogate tokens mapped in a secure vault; it is a "
                    "data-protection technique unrelated to obscuring compiled "
                    "application code."
                ),
            },
            {
                "id": "d",
                "text": "Steganography",
                "correct": False,
                "rationale": (
                    "Incorrect. Steganography hides data within another file (such as an "
                    "image) so its existence is concealed; it does not describe "
                    "renaming code identifiers or restructuring control flow within an "
                    "application binary."
                ),
            },
        ],
        "explanation": (
            "Obfuscation transforms code (renaming identifiers, adding opaque control "
            "flow) to make analysis difficult while preserving behavior — distinct from "
            "data masking/tokenization (protecting data values) and steganography (hiding "
            "data's existence)."
        ),
    },
    {
        "id": "nd1d-034",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Obfuscation techniques",
        "stem": (
            "During a digital forensics investigation, an analyst extracts an audio "
            "file from a suspect's phone and, after spectral analysis, finds an "
            "embedded text message hidden within inaudible frequency components of the "
            "waveform, invisible to casual playback and undetectable without specialized "
            "analysis tools. Which technique did the suspect MOST likely use?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Steganography",
                "correct": True,
                "rationale": (
                    "Correct. Steganography conceals the very existence of a message "
                    "within another medium (here, an audio file's inaudible frequency "
                    "components) so that it is undetectable without specialized analysis "
                    "— exactly what is described."
                ),
            },
            {
                "id": "b",
                "text": "Symmetric encryption",
                "correct": False,
                "rationale": (
                    "Incorrect. Encryption transforms data into unreadable ciphertext but "
                    "does not hide the fact that a hidden message exists; here the "
                    "message's very presence was concealed within the audio, which is "
                    "steganography, not encryption."
                ),
            },
            {
                "id": "c",
                "text": "Hashing",
                "correct": False,
                "rationale": (
                    "Incorrect. Hashing produces a fixed-size digest for integrity "
                    "verification and is not reversible to recover an original message; "
                    "it cannot be used to embed and later extract a hidden text message "
                    "within audio."
                ),
            },
            {
                "id": "d",
                "text": "Data masking",
                "correct": False,
                "rationale": (
                    "Incorrect. Data masking substitutes sensitive values with realistic "
                    "fake ones for non-production environments; it does not describe "
                    "hiding a message within an audio file's frequency components."
                ),
            },
        ],
        "explanation": (
            "Embedding a hidden message within another file's data (audio frequencies, "
            "image pixels) so its existence is concealed is steganography, distinct from "
            "encryption (which hides content but not existence) or masking/hashing."
        ),
    },
    # ── 1.4 Symmetric vs asymmetric encryption ───────────────────────────────
    {
        "id": "nd1d-035",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Symmetric vs asymmetric encryption",
        "stem": (
            "A satellite ground station needs to encrypt a continuous, high-bandwidth "
            "telemetry downlink between two facilities that have already exchanged a "
            "shared secret through an out-of-band courier process, and CPU overhead must "
            "be minimized because the receiving hardware has limited processing power. "
            "Which type of encryption BEST fits this requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Symmetric encryption",
                "correct": True,
                "rationale": (
                    "Correct. Symmetric algorithms such as AES are computationally "
                    "efficient and well suited for high-throughput, low-overhead bulk "
                    "data encryption once both parties already share a secret key — "
                    "exactly the situation described with the courier-delivered shared "
                    "secret and limited processing power."
                ),
            },
            {
                "id": "b",
                "text": "Asymmetric encryption",
                "correct": False,
                "rationale": (
                    "Incorrect. Asymmetric encryption is computationally expensive and "
                    "far slower for bulk data compared to symmetric ciphers; it is "
                    "typically used for key exchange or digital signatures, not for "
                    "encrypting a continuous high-bandwidth stream on limited hardware."
                ),
            },
            {
                "id": "c",
                "text": "Hashing",
                "correct": False,
                "rationale": (
                    "Incorrect. Hashing is a one-way function used for integrity "
                    "verification, not for encrypting and later decrypting a data stream; "
                    "it cannot be used to protect confidentiality of telemetry that must "
                    "be recovered by the receiver."
                ),
            },
            {
                "id": "d",
                "text": "Obfuscation",
                "correct": False,
                "rationale": (
                    "Incorrect. Obfuscation makes data or code harder to understand but "
                    "provides no cryptographic confidentiality guarantee and is not "
                    "designed for securing a continuous high-bandwidth data stream "
                    "between two facilities."
                ),
            },
        ],
        "explanation": (
            "Once a shared secret already exists, symmetric encryption is the efficient "
            "choice for high-throughput, low-overhead bulk data protection — asymmetric "
            "encryption is reserved for key exchange or signatures due to its much higher "
            "computational cost."
        ),
    },
    {
        "id": "nd1d-036",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Symmetric vs asymmetric encryption",
        "stem": (
            "A cross-border legal firm needs to send confidential case files to outside "
            "counsel with whom it has never previously shared any secret key material "
            "over any channel, and the recipient must be able to independently verify "
            "that the file genuinely originated from the firm and was not altered in "
            "transit. Which TWO asymmetric-cryptography operations, used together, "
            "satisfy BOTH requirements? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Encrypt the file (or a symmetric key protecting it) using the recipient's public key so only the recipient's private key can decrypt it",
                "correct": True,
                "rationale": (
                    "Correct. Encrypting with the recipient's public key ensures only "
                    "the holder of the corresponding private key can decrypt the file, "
                    "solving the confidentiality requirement without any prior shared "
                    "secret."
                ),
            },
            {
                "id": "b",
                "text": "Digitally sign the file using the firm's private key so the recipient can verify authenticity and integrity with the firm's public key",
                "correct": True,
                "rationale": (
                    "Correct. A digital signature created with the sender's private key "
                    "lets any recipient verify, using the sender's public key, both that "
                    "the file originated from the firm and that it was not altered — "
                    "satisfying the authenticity/integrity requirement."
                ),
            },
            {
                "id": "c",
                "text": "Encrypt the file using the firm's own private key so anyone can decrypt it with the firm's public key",
                "correct": False,
                "rationale": (
                    "Incorrect. Encrypting with the sender's private key so anyone with "
                    "the public key can decrypt provides no confidentiality at all — "
                    "that pattern is how signatures work (proving origin), not how "
                    "confidentiality is achieved; it would let anyone read the file."
                ),
            },
            {
                "id": "d",
                "text": "Share a pre-agreed AES key over an unencrypted email to speed up the exchange",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario explicitly states no secret key material has "
                    "ever been shared, and transmitting a symmetric key over unencrypted "
                    "email would expose it to interception, defeating confidentiality "
                    "entirely."
                ),
            },
            {
                "id": "e",
                "text": "Hash the file with MD5 and send the hash alongside the file for the recipient to compare",
                "correct": False,
                "rationale": (
                    "Incorrect. A bare hash sent alongside the file provides no "
                    "authentication of origin (anyone could recompute and replace both "
                    "the file and hash) and MD5 is cryptographically broken; this does "
                    "not satisfy either the confidentiality or the authenticity "
                    "requirement."
                ),
            },
        ],
        "explanation": (
            "Asymmetric cryptography solves both problems without any prior shared "
            "secret: encrypting with the recipient's public key provides confidentiality, "
            "while signing with the sender's private key (verified against the sender's "
            "public key) provides authenticity and integrity."
        ),
    },
]

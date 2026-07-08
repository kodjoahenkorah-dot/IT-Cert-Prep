"""
CompTIA Security+ (SY0-701) Domain 1: General Security Concepts — Set C
36 exam-quality questions covering objectives 1.1 through 1.4.
"""

QUESTIONS = [
    # ── 1.1 Security control categories ─────────────────────────────────────
    {
        "id": "nd1c-001",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security control categories",
        "stem": (
            "A SOC's SOAR platform automatically revokes a compromised user's OAuth "
            "tokens and disables the account within seconds of a correlated SIEM alert, "
            "with no analyst approval required for this specific playbook. Which "
            "security control CATEGORY does this automated playbook represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Technical",
                "correct": True,
                "rationale": (
                    "Correct. The playbook is technology automatically enforcing an "
                    "action without human execution, which is the definition of a "
                    "technical control."
                ),
            },
            {
                "id": "b",
                "text": "Operational",
                "correct": False,
                "rationale": (
                    "Incorrect. Operational controls are recurring, people-executed "
                    "procedures. This action is fully automated with no human carrying "
                    "out the task, which rules out operational."
                ),
            },
            {
                "id": "c",
                "text": "Managerial",
                "correct": False,
                "rationale": (
                    "Incorrect. Managerial controls are governance-level policy "
                    "decisions (e.g., requiring a SOAR capability to exist); the "
                    "automated playbook itself is the technology carrying out that "
                    "governance intent."
                ),
            },
            {
                "id": "d",
                "text": "Physical",
                "correct": False,
                "rationale": (
                    "Incorrect. Physical controls protect tangible assets. Revoking "
                    "tokens and disabling an account is a logical, not physical, action."
                ),
            },
        ],
        "explanation": (
            "Automated, technology-enforced actions such as a SOAR playbook revoking "
            "credentials are Technical controls, distinct from the Managerial policy "
            "that mandated the capability or the Operational tasks staff perform "
            "manually."
        ),
    },
    {
        "id": "nd1c-002",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Security control categories",
        "stem": (
            "Before any new cloud workload can go into production, corporate "
            "governance requires the business unit owner to formally document and "
            "sign an acceptance of residual risk that remains after existing controls "
            "have been applied. Which security control CATEGORY does this sign-off "
            "requirement represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Managerial",
                "correct": True,
                "rationale": (
                    "Correct. A governance-mandated risk-acceptance requirement, "
                    "established as organizational policy before deployment, is a "
                    "managerial (administrative) control."
                ),
            },
            {
                "id": "b",
                "text": "Operational",
                "correct": False,
                "rationale": (
                    "Incorrect. Operational controls are recurring, day-to-day tasks "
                    "carried out by staff (e.g., patch deployment); this is a "
                    "governance-level policy decision defining who must approve risk "
                    "before go-live, not a routine execution task."
                ),
            },
            {
                "id": "c",
                "text": "Technical",
                "correct": False,
                "rationale": (
                    "Incorrect. No technology enforces or automates this sign-off; it "
                    "is a documented governance requirement, not a technical control."
                ),
            },
            {
                "id": "d",
                "text": "Physical",
                "correct": False,
                "rationale": (
                    "Incorrect. Physical controls protect tangible assets. Nothing "
                    "about a risk-acceptance sign-off involves physical protections."
                ),
            },
        ],
        "explanation": (
            "Managerial controls set governance-level requirements — such as "
            "mandating formal risk acceptance before production deployment — that "
            "guide, but are distinct from, the technical and operational controls "
            "that carry out day-to-day security work."
        ),
    },

    # ── 1.1 Security control types ──────────────────────────────────────────
    {
        "id": "nd1c-003",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security control types",
        "stem": (
            "A retailer configures its point-of-sale terminals' USB controllers to "
            "only enumerate devices matching an approved hardware ID whitelist, "
            "physically preventing any unauthorized USB device from ever being "
            "recognized by the terminal. Which control TYPE BEST describes this "
            "configuration?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Preventive",
                "correct": True,
                "rationale": (
                    "Correct. The whitelist stops unauthorized devices from ever being "
                    "recognized, blocking the incident before it can occur — the "
                    "defining trait of a preventive control."
                ),
            },
            {
                "id": "b",
                "text": "Detective",
                "correct": False,
                "rationale": (
                    "Incorrect. A detective control would identify and log an "
                    "unauthorized device after the fact; this configuration actively "
                    "blocks the device from ever being recognized."
                ),
            },
            {
                "id": "c",
                "text": "Deterrent",
                "correct": False,
                "rationale": (
                    "Incorrect. A deterrent only discourages an attacker through "
                    "perceived risk; this control technically blocks unauthorized "
                    "devices regardless of the attacker's intent."
                ),
            },
            {
                "id": "d",
                "text": "Compensating",
                "correct": False,
                "rationale": (
                    "Incorrect. A compensating control substitutes for a primary "
                    "control that cannot be implemented. This whitelist is the primary "
                    "control itself, not a substitute for one that is infeasible."
                ),
            },
        ],
        "explanation": (
            "Blocking unauthorized USB devices from ever enumerating is a Preventive "
            "control, since it stops the incident before it can occur — distinct from "
            "detective, deterrent, or compensating controls."
        ),
    },
    {
        "id": "nd1c-004",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Security control types",
        "stem": (
            "A hospital posts a sign at the data center door stating: 'All visitors "
            "must be escorted by IT staff at all times, per Policy SEC-114.' The sign "
            "does not physically lock the door, and nothing alerts security if it is "
            "ignored. Which control TYPE BEST describes this sign?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Directive",
                "correct": True,
                "rationale": (
                    "Correct. A directive control mandates or directs required "
                    "behavior in line with policy — exactly what a signage requirement "
                    "to be escorted per named policy does — without itself physically "
                    "enforcing, blocking, or recording compliance."
                ),
            },
            {
                "id": "b",
                "text": "Preventive",
                "correct": False,
                "rationale": (
                    "Incorrect. The sign does not physically stop entry; it merely "
                    "instructs required behavior, which is the hallmark of a directive "
                    "control rather than a preventive one."
                ),
            },
            {
                "id": "c",
                "text": "Deterrent",
                "correct": False,
                "rationale": (
                    "Incorrect. A deterrent primarily discourages malicious actors by "
                    "signaling perceived risk (e.g., 'monitored by CCTV'). This sign "
                    "instead mandates a specific compliance procedure tied to a named "
                    "policy for all visitors, which is directive."
                ),
            },
            {
                "id": "d",
                "text": "Detective",
                "correct": False,
                "rationale": (
                    "Incorrect. Nothing about the sign records, logs, or alerts on "
                    "non-compliance after the fact, ruling out a detective function."
                ),
            },
        ],
        "explanation": (
            "Directive controls mandate a required course of action tied to policy "
            "(e.g., escort requirements, acceptable-use signage) without physically "
            "preventing, merely discouraging, or detecting violations — distinguishing "
            "them from preventive, deterrent, and detective types."
        ),
    },

    # ── 1.1 Security control categories and types ───────────────────────────
    {
        "id": "nd1c-005",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security control categories and types",
        "stem": (
            "A next-generation firewall automatically drops any packet whose payload "
            "matches a known malware signature before it reaches the internal "
            "network, with no human review required. Which CATEGORY and TYPE pairing "
            "BEST classifies this behavior?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Technical category / Preventive type",
                "correct": True,
                "rationale": (
                    "Correct. Technology automatically enforces the rule (technical), "
                    "and dropping the malicious packet before it reaches the network "
                    "stops the incident from occurring (preventive)."
                ),
            },
            {
                "id": "b",
                "text": "Technical category / Detective type",
                "correct": False,
                "rationale": (
                    "Incorrect. The firewall drops (blocks) the packet rather than "
                    "merely identifying and logging it after delivery, which rules out "
                    "detective and points to preventive."
                ),
            },
            {
                "id": "c",
                "text": "Operational category / Preventive type",
                "correct": False,
                "rationale": (
                    "Incorrect. This action is executed automatically by technology, "
                    "not carried out by staff as a recurring manual procedure, ruling "
                    "out operational."
                ),
            },
            {
                "id": "d",
                "text": "Managerial category / Corrective type",
                "correct": False,
                "rationale": (
                    "Incorrect. This is neither a governance-level policy decision "
                    "(managerial) nor a restoration after an incident (corrective) — "
                    "it is an automated technical block before any harm occurs."
                ),
            },
        ],
        "explanation": (
            "Every control has both a category (how it's implemented) and a type "
            "(what it accomplishes). An automated, signature-based block before "
            "delivery is Technical category, Preventive type."
        ),
    },
    {
        "id": "nd1c-006",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Security control categories and types",
        "stem": (
            "Each night, a shift supervisor walks the perimeter fence line and "
            "manually compares its current condition against a reference photograph "
            "taken during the last inspection, filing an anomaly report for any "
            "damage or breach found. Which CATEGORY and TYPE pairing BEST classifies "
            "this nightly walk-and-compare activity?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Operational category / Detective type",
                "correct": True,
                "rationale": (
                    "Correct. A person manually performing a recurring inspection "
                    "procedure is operational, and comparing current conditions "
                    "against a baseline to identify issues after they occur is "
                    "detective."
                ),
            },
            {
                "id": "b",
                "text": "Physical category / Preventive type",
                "correct": False,
                "rationale": (
                    "Incorrect. The fence itself is a physical/preventive barrier, but "
                    "the described activity is the supervisor's manual, recurring "
                    "inspection and comparison — an operational, detective task, not "
                    "the tangible barrier control."
                ),
            },
            {
                "id": "c",
                "text": "Managerial category / Corrective type",
                "correct": False,
                "rationale": (
                    "Incorrect. This is not a governance-level policy decision, and "
                    "filing a report identifies damage rather than restoring or "
                    "repairing it, which rules out corrective."
                ),
            },
            {
                "id": "d",
                "text": "Technical category / Compensating type",
                "correct": False,
                "rationale": (
                    "Incorrect. No technology automates this walk-and-compare "
                    "activity, and nothing indicates it substitutes for an infeasible "
                    "primary control."
                ),
            },
        ],
        "explanation": (
            "A manually performed, recurring inspection that identifies issues after "
            "they occur is Operational category, Detective type — distinct from the "
            "physical fence itself, which is a separate preventive control."
        ),
    },

    # ── 1.2 AAA framework ────────────────────────────────────────────────────
    {
        "id": "nd1c-007",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "AAA framework",
        "stem": (
            "A cloud access policy grants a finance analyst access to the "
            "general-ledger application only when ALL of the following are "
            "simultaneously true: the request originates from a corporate-managed "
            "laptop, the connection originates from an approved country, and the "
            "request occurs between 6 a.m. and 8 p.m. local time. Which access "
            "control model is being enforced?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Attribute-Based Access Control (ABAC)",
                "correct": True,
                "rationale": (
                    "Correct. ABAC evaluates multiple dynamic attributes — device "
                    "posture, geolocation, and time — in combination to render an "
                    "access decision, exactly as described."
                ),
            },
            {
                "id": "b",
                "text": "Role-Based Access Control (RBAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. RBAC grants access based on job role or group "
                    "membership alone; it does not natively evaluate a combination of "
                    "device posture, location, and time attributes."
                ),
            },
            {
                "id": "c",
                "text": "Mandatory Access Control (MAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. MAC enforces access using fixed classification labels "
                    "and clearances, not dynamic contextual attributes like time of "
                    "day and connection location."
                ),
            },
            {
                "id": "d",
                "text": "Discretionary Access Control (DAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. DAC lets the resource owner grant access at their own "
                    "discretion; this scenario describes a centrally enforced rule "
                    "engine evaluating multiple attributes, not owner discretion."
                ),
            },
        ],
        "explanation": (
            "ABAC is defined by evaluating multiple dynamic attributes (device, "
            "location, time, etc.) together to make an access decision — distinct "
            "from role-based, label-based (MAC), or owner-discretionary (DAC) models."
        ),
    },
    {
        "id": "nd1c-008",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "AAA framework",
        "stem": (
            "A network team wants to centralize authentication, authorization, and "
            "accounting for administrative logins to all switches and routers, and "
            "needs a client-server protocol purpose-built for this AAA function. "
            "Which TWO of the following are dedicated AAA protocols suitable for "
            "network device administration? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "TACACS+",
                "correct": True,
                "rationale": (
                    "Correct. TACACS+ is a purpose-built AAA protocol that encrypts "
                    "the full packet payload over TCP and separates authentication, "
                    "authorization, and accounting — a common choice for network "
                    "device administration."
                ),
            },
            {
                "id": "b",
                "text": "RADIUS",
                "correct": True,
                "rationale": (
                    "Correct. RADIUS is a dedicated AAA protocol combining "
                    "authentication and authorization into a UDP response and "
                    "providing accounting, and can also be used for device "
                    "administration."
                ),
            },
            {
                "id": "c",
                "text": "Kerberos",
                "correct": False,
                "rationale": (
                    "Incorrect. Kerberos is a ticket-based authentication protocol; it "
                    "does not itself provide the authorization and accounting "
                    "functions for network device administration the way TACACS+ and "
                    "RADIUS do."
                ),
            },
            {
                "id": "d",
                "text": "LDAP",
                "correct": False,
                "rationale": (
                    "Incorrect. LDAP is a directory access protocol used to query or "
                    "bind against a directory service; it is not a dedicated AAA "
                    "protocol providing accounting for device administration."
                ),
            },
            {
                "id": "e",
                "text": "SAML",
                "correct": False,
                "rationale": (
                    "Incorrect. SAML is a federation/SSO assertion protocol used "
                    "primarily for web-based identity exchange, not a network device "
                    "administration AAA protocol."
                ),
            },
        ],
        "explanation": (
            "TACACS+ and RADIUS are the two dedicated AAA protocols used to "
            "centralize authentication, authorization, and accounting for network "
            "device administration, distinct from Kerberos (authentication only), "
            "LDAP (directory access), and SAML (web federation)."
        ),
    },

    # ── 1.2 Attack type identification ──────────────────────────────────────
    {
        "id": "nd1c-009",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Attack type identification",
        "stem": (
            "An attacker scatters several USB flash drives labeled 'Q3 Layoffs — "
            "Confidential' in the parking lot of a corporate office, hoping an "
            "employee will plug one into a workstation and unknowingly execute "
            "embedded malware. Which social engineering technique is BEST described?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Baiting",
                "correct": True,
                "rationale": (
                    "Correct. Baiting lures a victim into a harmful action using an "
                    "enticing physical item — here, a labeled USB drive left to be "
                    "found and plugged in."
                ),
            },
            {
                "id": "b",
                "text": "Pretexting",
                "correct": False,
                "rationale": (
                    "Incorrect. Pretexting relies on a fabricated scenario or persona "
                    "built through direct interaction (a call, email, or conversation); "
                    "this attack simply left a physical lure for someone to discover, "
                    "with no interactive fabricated story involved."
                ),
            },
            {
                "id": "c",
                "text": "Tailgating",
                "correct": False,
                "rationale": (
                    "Incorrect. Tailgating is physically following an authorized "
                    "person through an access-controlled entry point; nothing in this "
                    "scenario involves physical entry."
                ),
            },
            {
                "id": "d",
                "text": "Watering hole attack",
                "correct": False,
                "rationale": (
                    "Incorrect. A watering hole attack compromises a legitimate "
                    "website frequented by the target group; this attack instead "
                    "plants physical media in a location the target might find."
                ),
            },
        ],
        "explanation": (
            "Baiting uses an enticing physical or digital lure (like a labeled USB "
            "drive) to trigger a harmful action — distinct from pretexting "
            "(fabricated interactive scenario), tailgating (physical entry), and "
            "watering hole attacks (compromised website)."
        ),
    },
    {
        "id": "nd1c-010",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Attack type identification",
        "stem": (
            "A victim's mobile carrier account is fraudulently ported to a new SIM "
            "card after an attacker, using the victim's stolen personal details, "
            "convinces a call-center representative to transfer the phone number. "
            "The victim then stops receiving SMS-based one-time passcodes, which the "
            "attacker intercepts and uses to reset the victim's banking password. "
            "Which attack technique enabled the MFA bypass?"
        ),
        "options": [
            {
                "id": "a",
                "text": "SIM swapping",
                "correct": True,
                "rationale": (
                    "Correct. SIM swapping is fraudulently porting a victim's phone "
                    "number to an attacker-controlled SIM, allowing interception of "
                    "SMS-based one-time passcodes — exactly as described."
                ),
            },
            {
                "id": "b",
                "text": "Smishing",
                "correct": False,
                "rationale": (
                    "Incorrect. Smishing involves sending a fraudulent SMS to trick "
                    "the victim into acting; here, the compromise occurred through a "
                    "fraudulent carrier account transfer, not a deceptive text message "
                    "sent to the victim."
                ),
            },
            {
                "id": "c",
                "text": "Session hijacking",
                "correct": False,
                "rationale": (
                    "Incorrect. Session hijacking steals or reuses an existing active "
                    "session token; the attacker here intercepted OTPs by redirecting "
                    "the phone number itself, not by hijacking a live session."
                ),
            },
            {
                "id": "d",
                "text": "Credential stuffing",
                "correct": False,
                "rationale": (
                    "Incorrect. Credential stuffing uses previously breached "
                    "username/password pairs to gain access; the initial compromise "
                    "here came from social-engineering the carrier, not from reused "
                    "credentials."
                ),
            },
        ],
        "explanation": (
            "SIM swapping fraudulently transfers a victim's phone number to an "
            "attacker-controlled device, defeating SMS-based MFA — distinct from "
            "smishing, session hijacking, and credential stuffing."
        ),
    },

    # ── 1.2 CIA triad and non-repudiation ────────────────────────────────────
    {
        "id": "nd1c-011",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "CIA triad and non-repudiation",
        "stem": (
            "A misconfigured cloud storage bucket permits public read access to a "
            "folder containing 40,000 customers' names and Social Security numbers "
            "for three hours before being discovered and locked down. Forensic "
            "review confirms no files were altered or deleted during the exposure "
            "window. Which security objective was violated?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Confidentiality",
                "correct": True,
                "rationale": (
                    "Correct. Unauthorized public exposure of sensitive personal data "
                    "is a violation of confidentiality, regardless of whether the data "
                    "was altered."
                ),
            },
            {
                "id": "b",
                "text": "Integrity",
                "correct": False,
                "rationale": (
                    "Incorrect. Forensic review confirmed no files were modified or "
                    "deleted, ruling out an integrity violation."
                ),
            },
            {
                "id": "c",
                "text": "Availability",
                "correct": False,
                "rationale": (
                    "Incorrect. Nothing indicates authorized users lost access to the "
                    "data; the issue was unauthorized visibility, not lost access."
                ),
            },
            {
                "id": "d",
                "text": "Non-repudiation",
                "correct": False,
                "rationale": (
                    "Incorrect. Non-repudiation concerns proving who performed an "
                    "action to prevent denial of it; this scenario describes "
                    "unauthorized disclosure, not a dispute over authorship of an "
                    "action."
                ),
            },
        ],
        "explanation": (
            "Unauthorized disclosure of sensitive data — even without any "
            "modification — is specifically a confidentiality violation within the "
            "CIA triad."
        ),
    },
    {
        "id": "nd1c-012",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "CIA triad and non-repudiation",
        "stem": (
            "A vendor publishes the SHA-256 hash of a firmware update on its "
            "website. Before installing the update on production routers, the "
            "network team computes the hash of the downloaded file and finds it does "
            "not match the published value, so they discard the file rather than "
            "install it. Which security objective did this hash comparison protect?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Integrity",
                "correct": True,
                "rationale": (
                    "Correct. Comparing the computed hash against the published value "
                    "detects unauthorized modification or corruption of the file "
                    "before installation — the definition of protecting integrity."
                ),
            },
            {
                "id": "b",
                "text": "Confidentiality",
                "correct": False,
                "rationale": (
                    "Incorrect. Hash comparison doesn't control who can view the "
                    "firmware file; it only verifies whether the file's contents match "
                    "what was published, which is an integrity check."
                ),
            },
            {
                "id": "c",
                "text": "Availability",
                "correct": False,
                "rationale": (
                    "Incorrect. This is not about ensuring the update remains "
                    "accessible; it is about verifying the downloaded copy wasn't "
                    "altered or corrupted."
                ),
            },
            {
                "id": "d",
                "text": "Non-repudiation",
                "correct": False,
                "rationale": (
                    "Incorrect. Non-repudiation would require binding the file to the "
                    "publisher's identity via a digital signature to prove origin; a "
                    "simple hash-value match/mismatch check only confirms whether the "
                    "content was altered, which is integrity."
                ),
            },
        ],
        "explanation": (
            "A hash-value comparison detects unauthorized modification and thus "
            "protects integrity, distinct from confidentiality, availability, or the "
            "origin-proof role of non-repudiation (which requires a signature)."
        ),
    },

    # ── 1.2 Deception and disruption technologies ───────────────────────────
    {
        "id": "nd1c-013",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Deception and disruption technologies",
        "stem": (
            "A security team stands up a fully isolated web application that mimics "
            "the company's production customer login portal, complete with fake "
            "account data, deployed specifically to attract and study attacker "
            "behavior without exposing any real system. Which technique is this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Honeypot",
                "correct": True,
                "rationale": (
                    "Correct. A honeypot is a single standalone decoy system deployed "
                    "to attract and study attacker interaction without risking real "
                    "assets."
                ),
            },
            {
                "id": "b",
                "text": "Honeynet",
                "correct": False,
                "rationale": (
                    "Incorrect. A honeynet is an entire network of multiple "
                    "interconnected decoy systems used to observe broader attacker "
                    "movement, not a single standalone decoy application."
                ),
            },
            {
                "id": "c",
                "text": "Honeyfile",
                "correct": False,
                "rationale": (
                    "Incorrect. A honeyfile is a decoy document monitored for being "
                    "opened, not an entire mimicked login application."
                ),
            },
            {
                "id": "d",
                "text": "Honeytoken",
                "correct": False,
                "rationale": (
                    "Incorrect. A honeytoken is a fake embedded credential or data "
                    "value monitored for reuse elsewhere, not a full mimicked "
                    "application."
                ),
            },
        ],
        "explanation": (
            "A honeypot is a single decoy system built to attract and study "
            "attackers — distinct from a honeynet (a full decoy network), a "
            "honeyfile (a decoy document), or a honeytoken (a decoy credential)."
        ),
    },
    {
        "id": "nd1c-014",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Deception and disruption technologies",
        "stem": (
            "A security team wants to detect two different scenarios: (1) any "
            "employee who opens a decoy spreadsheet named "
            "'Layoff_List_2026_CONFIDENTIAL.xlsx' that no legitimate business process "
            "ever touches, and (2) any use, anywhere on the internet, of a "
            "non-functional AWS access key intentionally left inside a public code "
            "repository. Which TWO deception techniques should be deployed to cover "
            "these two scenarios, respectively? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Honeyfile",
                "correct": True,
                "rationale": (
                    "Correct. A honeyfile is a decoy document planted to trigger an "
                    "alert when opened, directly addressing scenario 1."
                ),
            },
            {
                "id": "b",
                "text": "Honeytoken",
                "correct": True,
                "rationale": (
                    "Correct. A honeytoken is a fake credential or data value "
                    "monitored for use elsewhere, directly addressing scenario 2."
                ),
            },
            {
                "id": "c",
                "text": "Honeynet",
                "correct": False,
                "rationale": (
                    "Incorrect. An entire network of decoy systems is unnecessary and "
                    "does not address either the single decoy file or the embedded "
                    "fake credential described here."
                ),
            },
            {
                "id": "d",
                "text": "Honeypot",
                "correct": False,
                "rationale": (
                    "Incorrect. A honeypot is a full decoy system meant to attract "
                    "broad interaction; neither scenario calls for a mimicked system, "
                    "but rather a specific file and a specific embedded credential."
                ),
            },
            {
                "id": "e",
                "text": "Tarpit",
                "correct": False,
                "rationale": (
                    "Incorrect. A tarpit slows down an attacker's active connection; "
                    "it does not detect file-open events or credential reuse."
                ),
            },
        ],
        "explanation": (
            "A honeyfile detects unauthorized access to a specific decoy document, "
            "while a honeytoken detects misuse of a specific fake credential planted "
            "elsewhere — two distinct deception techniques matched to two distinct "
            "detection goals."
        ),
    },

    # ── 1.2 Gap analysis ─────────────────────────────────────────────────────
    {
        "id": "nd1c-015",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Gap analysis",
        "stem": (
            "While preparing for a PCI DSS assessment, a security analyst discovers "
            "the organization performs vulnerability scans only annually, while the "
            "standard requires quarterly internal and external scans. The analyst "
            "documents this shortfall along with a target date to begin quarterly "
            "scanning. Which process produced this documentation?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Gap analysis",
                "correct": True,
                "rationale": (
                    "Correct. Comparing current practice (annual scanning) against a "
                    "required standard (quarterly scanning) and documenting a "
                    "remediation target date is exactly a gap analysis."
                ),
            },
            {
                "id": "b",
                "text": "Business impact analysis",
                "correct": False,
                "rationale": (
                    "Incorrect. A BIA identifies critical business functions and "
                    "quantifies downtime tolerances (RTO/RPO), not a comparison of "
                    "current practice against a compliance requirement."
                ),
            },
            {
                "id": "c",
                "text": "Vulnerability assessment",
                "correct": False,
                "rationale": (
                    "Incorrect. A vulnerability assessment scans systems for technical "
                    "weaknesses; this scenario compares a scanning CADENCE against a "
                    "compliance requirement, which is a gap analysis, not the scan "
                    "itself."
                ),
            },
            {
                "id": "d",
                "text": "Tabletop exercise",
                "correct": False,
                "rationale": (
                    "Incorrect. A tabletop exercise is a discussion-based simulation "
                    "of incident response; it is unrelated to comparing current "
                    "practice to a compliance standard."
                ),
            },
        ],
        "explanation": (
            "Gap analysis measures current state against a required target "
            "(regulation, standard, or policy) and documents a remediation timeline "
            "— distinct from a BIA, a vulnerability assessment, or a tabletop "
            "exercise."
        ),
    },
    {
        "id": "nd1c-016",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Gap analysis",
        "stem": (
            "A new state privacy regulation requires breach notification within 72 "
            "hours and log retention of at least one year. A compliance team builds "
            "a matrix listing each requirement, the organization's current "
            "capability (a 45-day notification process, 30-day log retention), and "
            "assigns an owner and deadline to close each shortfall. Which activity "
            "does this matrix represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Gap analysis",
                "correct": True,
                "rationale": (
                    "Correct. Listing each regulatory requirement alongside current "
                    "capability and assigning remediation owners and deadlines is "
                    "exactly the output of a gap analysis."
                ),
            },
            {
                "id": "b",
                "text": "Risk register",
                "correct": False,
                "rationale": (
                    "Incorrect. A risk register catalogs identified risks generally "
                    "with likelihood and impact scores; this matrix specifically "
                    "compares current state to a named regulation's requirements, "
                    "which is a gap analysis."
                ),
            },
            {
                "id": "c",
                "text": "Data classification scheme",
                "correct": False,
                "rationale": (
                    "Incorrect. A classification scheme labels data sensitivity "
                    "levels; it does not compare current controls to regulatory "
                    "requirements."
                ),
            },
            {
                "id": "d",
                "text": "Business continuity plan",
                "correct": False,
                "rationale": (
                    "Incorrect. A BCP addresses maintaining operations during "
                    "disruption; it is unrelated to comparing current capability "
                    "against regulatory deadlines."
                ),
            },
        ],
        "explanation": (
            "Gap analysis directly produces a comparison of current state against a "
            "target requirement (here, a privacy regulation) with assigned "
            "remediation owners and deadlines — distinct from a risk register, "
            "classification scheme, or BCP."
        ),
    },

    # ── 1.2 Physical security ────────────────────────────────────────────────
    {
        "id": "nd1c-017",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Physical security",
        "stem": (
            "A defense contractor's Sensitive Compartmented Information Facility "
            "(SCIF) is constructed with copper mesh embedded in the walls, ceiling, "
            "and floor to prevent electromagnetic signals — including cellular and "
            "Wi-Fi transmissions — from entering or leaving the room. Which physical "
            "control is being described?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Faraday cage",
                "correct": True,
                "rationale": (
                    "Correct. A Faraday cage uses a conductive enclosure to passively "
                    "block electromagnetic signals from entering or leaving a "
                    "shielded space — exactly what the embedded copper mesh provides."
                ),
            },
            {
                "id": "b",
                "text": "Access control vestibule",
                "correct": False,
                "rationale": (
                    "Incorrect. A vestibule (mantrap) controls the physical passage of "
                    "people through a doorway; it does not shield a room from RF "
                    "signals."
                ),
            },
            {
                "id": "c",
                "text": "Air-gapped network",
                "correct": False,
                "rationale": (
                    "Incorrect. Air-gapping is a network-isolation practice with no "
                    "physical or logical network connection; it does not describe RF "
                    "shielding of a physical room's walls, ceiling, and floor."
                ),
            },
            {
                "id": "d",
                "text": "Signal jammer",
                "correct": False,
                "rationale": (
                    "Incorrect. A jammer actively transmits noise to disrupt signals "
                    "in a given area; the embedded copper mesh instead passively "
                    "shields and blocks signals via a conductive enclosure — a "
                    "different mechanism than active jamming."
                ),
            },
        ],
        "explanation": (
            "A Faraday cage passively blocks electromagnetic signals using a "
            "conductive enclosure — distinct from a mantrap (controls people), "
            "air-gapping (network isolation), or active signal jamming."
        ),
    },
    {
        "id": "nd1c-018",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Physical security",
        "stem": (
            "A bank vault's electronic lock is engineered so that during a power "
            "failure, the bolt remains mechanically engaged and the door stays "
            "locked, requiring a manual key override by an authorized manager — even "
            "though this configuration would violate fire code if applied to a "
            "general office emergency exit. Which term describes this locking "
            "behavior?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Fail-secure (fail-closed)",
                "correct": True,
                "rationale": (
                    "Correct. Fail-secure locks default to a LOCKED state when power "
                    "or control is lost, prioritizing asset protection over emergency "
                    "egress — exactly the vault's behavior."
                ),
            },
            {
                "id": "b",
                "text": "Fail-safe",
                "correct": False,
                "rationale": (
                    "Incorrect. Fail-safe locks default to UNLOCKED on power loss to "
                    "prioritize life-safety egress — the opposite of the vault's "
                    "described behavior."
                ),
            },
            {
                "id": "c",
                "text": "Fail-open",
                "correct": False,
                "rationale": (
                    "Incorrect. Fail-open is functionally the same as fail-safe — the "
                    "lock defaults to unlocked on power loss — which is the opposite "
                    "of the vault remaining locked."
                ),
            },
            {
                "id": "d",
                "text": "Fail-secure that automatically unlocks during any fire alarm",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario specifies the vault requires manual key "
                    "override only, with no automatic unlocking during an alarm "
                    "condition, contradicting this option's added automatic-unlock "
                    "behavior."
                ),
            },
        ],
        "explanation": (
            "Fail-secure (fail-closed) locks remain locked on power loss, "
            "prioritizing confidentiality/asset protection — the opposite of "
            "fail-safe (fail-open) locks, which default to unlocked to prioritize "
            "emergency egress."
        ),
    },

    # ── 1.2 Zero Trust architecture ──────────────────────────────────────────
    {
        "id": "nd1c-019",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Zero Trust architecture",
        "stem": (
            "In a NIST SP 800-207 Zero Trust deployment, once the Policy Engine and "
            "Policy Administrator authorize a session, which component sits in the "
            "DATA plane and is directly responsible for establishing, monitoring, "
            "and terminating the connection between the subject and the resource?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Policy Enforcement Point (PEP)",
                "correct": True,
                "rationale": (
                    "Correct. The PEP is the data-plane gateway that establishes, "
                    "monitors, and terminates the actual connection per the control "
                    "plane's decision."
                ),
            },
            {
                "id": "b",
                "text": "Policy Engine (PE)",
                "correct": False,
                "rationale": (
                    "Incorrect. The PE resides in the control plane and evaluates "
                    "policy to render the access decision; it does not itself sit "
                    "inline enforcing the live data-plane connection."
                ),
            },
            {
                "id": "c",
                "text": "Policy Administrator (PA)",
                "correct": False,
                "rationale": (
                    "Incorrect. The PA is also a control-plane component that "
                    "generates the session-specific instructions; it does not sit "
                    "inline carrying the actual traffic in the data plane."
                ),
            },
            {
                "id": "d",
                "text": "Identity Provider (IdP)",
                "correct": False,
                "rationale": (
                    "Incorrect. The IdP is an external data source supplying identity "
                    "attributes to the Policy Engine; it is not a defined 800-207 "
                    "data-plane component that enforces the live session."
                ),
            },
        ],
        "explanation": (
            "NIST SP 800-207 places the Policy Engine and Policy Administrator in "
            "the control plane (decide and communicate), while the Policy "
            "Enforcement Point sits in the data plane, directly establishing, "
            "monitoring, and terminating the connection."
        ),
    },
    {
        "id": "nd1c-020",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Zero Trust architecture",
        "stem": (
            "A Zero Trust program grants a third-party contractor access to exactly "
            "the three SaaS applications required for a two-week project, "
            "automatically revokes that access at the contract's end date, and "
            "re-validates the need for continued access every seven days while the "
            "contract is active. Which Zero Trust principle is BEING enforced by "
            "this time-bound, minimal-scope access grant?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Least privilege / just-in-time access",
                "correct": True,
                "rationale": (
                    "Correct. Granting only the minimum required access, scoped to "
                    "the project's duration and periodically re-validated, is the "
                    "least-privilege and just-in-time access principle."
                ),
            },
            {
                "id": "b",
                "text": "Microsegmentation",
                "correct": False,
                "rationale": (
                    "Incorrect. Microsegmentation isolates network zones with "
                    "granular policy enforcement between segments; it does not "
                    "describe scoping and time-limiting an individual's access "
                    "rights."
                ),
            },
            {
                "id": "c",
                "text": "Continuous verification",
                "correct": False,
                "rationale": (
                    "Incorrect. Continuous verification re-authenticates and "
                    "re-validates trust signals (identity, device posture) on every "
                    "request. This scenario specifically describes minimizing scope "
                    "and duration of granted access, which is least privilege/JIT."
                ),
            },
            {
                "id": "d",
                "text": "Implicit trust zone elimination",
                "correct": False,
                "rationale": (
                    "Incorrect. This describes removing trusted network segments or "
                    "perimeters generally, not the specific practice of scoping and "
                    "time-limiting a contractor's individual access rights."
                ),
            },
        ],
        "explanation": (
            "Least privilege and just-in-time access grant only the minimum "
            "necessary access for the minimum necessary duration, with periodic "
            "re-validation — distinct from microsegmentation, continuous "
            "verification, or eliminating implicit trust zones."
        ),
    },

    # ── 1.3 Change management ────────────────────────────────────────────────
    {
        "id": "nd1c-021",
        "domain": 1,
        "objective": "1.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Change management",
        "stem": (
            "Two weeks after a normal change to core routing policy is implemented, "
            "the change manager convenes a meeting to compare the change's actual "
            "outcomes against the success criteria documented in the original "
            "Request for Change, confirming the change achieved its intended goal "
            "without unintended side effects. Which element of the change "
            "management process does this meeting represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Post-implementation review",
                "correct": True,
                "rationale": (
                    "Correct. Comparing actual outcomes against documented success "
                    "criteria after a change has been live for a period of time is "
                    "the post-implementation review."
                ),
            },
            {
                "id": "b",
                "text": "Impact analysis",
                "correct": False,
                "rationale": (
                    "Incorrect. Impact analysis is performed BEFORE approval to "
                    "anticipate risk; this meeting evaluates ACTUAL outcomes after "
                    "the change was already implemented."
                ),
            },
            {
                "id": "c",
                "text": "Backout plan validation",
                "correct": False,
                "rationale": (
                    "Incorrect. A backout plan documents how to reverse a failed "
                    "change; this meeting confirms success against criteria, not "
                    "testing or executing a rollback procedure."
                ),
            },
            {
                "id": "d",
                "text": "Change Advisory Board approval",
                "correct": False,
                "rationale": (
                    "Incorrect. CAB approval occurs before implementation to "
                    "authorize the change; this meeting occurs afterward to validate "
                    "results."
                ),
            },
        ],
        "explanation": (
            "A post-implementation review compares actual results against the "
            "documented success criteria after a change has been live — distinct "
            "from the earlier impact analysis, backout plan, and CAB approval steps."
        ),
    },
    {
        "id": "nd1c-022",
        "domain": 1,
        "objective": "1.3",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Change management",
        "stem": (
            "A network team is drafting a Request for Change to modify core "
            "firewall ACLs during next month's scheduled maintenance window. Which "
            "TWO of the following should be completed and documented BEFORE the "
            "Change Advisory Board reviews the request? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "An impact/risk analysis describing affected systems and potential business consequences",
                "correct": True,
                "rationale": (
                    "Correct. Impact analysis must be completed before CAB review so "
                    "the board can weigh the anticipated risk when deciding whether to "
                    "approve the change."
                ),
            },
            {
                "id": "b",
                "text": "A documented backout/rollback plan describing how to reverse the change if it fails",
                "correct": True,
                "rationale": (
                    "Correct. A backout plan must be prepared in advance so the CAB "
                    "can confirm a safe reversal path exists before authorizing "
                    "implementation."
                ),
            },
            {
                "id": "c",
                "text": "A post-implementation review report confirming the change met its success criteria",
                "correct": False,
                "rationale": (
                    "Incorrect. This report can only be produced AFTER the change has "
                    "been implemented and observed, not before CAB review."
                ),
            },
            {
                "id": "d",
                "text": "Final production change logs showing the completed configuration",
                "correct": False,
                "rationale": (
                    "Incorrect. These logs are generated during or after "
                    "implementation, not prepared in advance of CAB approval."
                ),
            },
            {
                "id": "e",
                "text": "A verbal agreement from a peer engineer with no written record",
                "correct": False,
                "rationale": (
                    "Incorrect. Informal, undocumented approval does not satisfy the "
                    "documented governance requirements of the change management "
                    "process."
                ),
            },
        ],
        "explanation": (
            "Before CAB review, a Request for Change must include a completed "
            "impact/risk analysis and a documented backout plan — both prepared in "
            "advance, unlike the post-implementation review or production logs, "
            "which follow implementation."
        ),
    },

    # ── 1.4 Blockchain and open public ledger ────────────────────────────────
    {
        "id": "nd1c-023",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Blockchain and open public ledger",
        "stem": (
            "A consortium of hospitals wants a shared, tamper-evident ledger of "
            "medical device provenance records, but requires that only the "
            "consortium's ten pre-vetted member hospitals be allowed to validate and "
            "add new transaction blocks — the general public should not be able to "
            "participate in consensus. Which blockchain implementation model BEST "
            "satisfies this requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Permissioned (private/consortium) blockchain",
                "correct": True,
                "rationale": (
                    "Correct. A permissioned blockchain restricts participation in "
                    "consensus to pre-approved members while still providing a "
                    "decentralized, tamper-evident ledger among them."
                ),
            },
            {
                "id": "b",
                "text": "Public blockchain",
                "correct": False,
                "rationale": (
                    "Incorrect. A public blockchain allows any participant to join "
                    "and validate transactions, which does not restrict consensus to "
                    "only the ten vetted hospitals."
                ),
            },
            {
                "id": "c",
                "text": "Centralized relational database with digital signatures",
                "correct": False,
                "rationale": (
                    "Incorrect. A centralized database still relies on a single "
                    "trusted operator, lacking the decentralized, multi-party "
                    "consensus a distributed ledger provides among the vetted "
                    "members."
                ),
            },
            {
                "id": "d",
                "text": "Public blockchain with role-based smart contract access",
                "correct": False,
                "rationale": (
                    "Incorrect. Restricting smart-contract execution does not "
                    "restrict WHO can validate and append new blocks to the "
                    "underlying chain, which remains open to the public in this "
                    "option."
                ),
            },
        ],
        "explanation": (
            "A permissioned (private/consortium) blockchain restricts block "
            "validation to a defined set of pre-vetted members while retaining "
            "decentralized, tamper-evident consensus — distinct from a fully public "
            "blockchain or a centralized database."
        ),
    },
    {
        "id": "nd1c-024",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Blockchain and open public ledger",
        "stem": (
            "A multi-party supply chain consortium is evaluating blockchain "
            "technology for tracking shipment custody. Which TWO of the following "
            "are properties that a blockchain-based distributed ledger actually "
            "provides in this use case? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Tamper-evidence through cryptographic hash-chaining of blocks",
                "correct": True,
                "rationale": (
                    "Correct. Each block cryptographically references the prior "
                    "block, making retroactive alteration detectable — a core "
                    "blockchain property."
                ),
            },
            {
                "id": "b",
                "text": "Decentralized trust via multi-party consensus, removing reliance on one central authority",
                "correct": True,
                "rationale": (
                    "Correct. Consensus is validated across multiple participating "
                    "nodes rather than a single trusted operator, which is the "
                    "defining decentralization benefit."
                ),
            },
            {
                "id": "c",
                "text": "Automatic confidentiality of all transaction details from every participating node",
                "correct": False,
                "rationale": (
                    "Incorrect. Most blockchain ledgers are transparent to "
                    "participants by design; confidentiality of contents is not an "
                    "inherent property and typically requires additional encryption "
                    "layered on top."
                ),
            },
            {
                "id": "d",
                "text": "Elimination of the need for any participant to manage private keys",
                "correct": False,
                "rationale": (
                    "Incorrect. Participants still must securely generate, store, and "
                    "manage private keys to sign transactions; blockchain does not "
                    "remove key-management responsibility."
                ),
            },
            {
                "id": "e",
                "text": "Automatic regulatory compliance certification for the consortium",
                "correct": False,
                "rationale": (
                    "Incorrect. A ledger's technical properties do not by themselves "
                    "certify compliance with any regulation; that requires separate "
                    "governance and audit processes."
                ),
            },
        ],
        "explanation": (
            "Blockchain provides tamper-evidence (hash-chaining) and decentralized "
            "trust (multi-party consensus) — it does not inherently provide "
            "confidentiality, eliminate key management, or certify regulatory "
            "compliance."
        ),
    },

    # ── 1.4 Certificates ──────────────────────────────────────────────────────
    {
        "id": "nd1c-025",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Certificates",
        "stem": (
            "A mobile banking app hard-codes the expected public key of its backend "
            "API server. During TLS negotiation, the app rejects the connection if "
            "the presented certificate's public key does not exactly match the "
            "hard-coded value — even if the certificate was issued and signed by a "
            "CA the device's OS trusts. Which technique is the app using?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Certificate/public key pinning",
                "correct": True,
                "rationale": (
                    "Correct. Pinning hard-codes an expected certificate or public "
                    "key in the client and rejects any presented certificate that "
                    "doesn't match, even one signed by a trusted CA."
                ),
            },
            {
                "id": "b",
                "text": "OCSP stapling",
                "correct": False,
                "rationale": (
                    "Incorrect. OCSP stapling provides real-time revocation status "
                    "attached to the handshake; it doesn't involve comparing the "
                    "presented key against a hard-coded expected value."
                ),
            },
            {
                "id": "c",
                "text": "Certificate transparency",
                "correct": False,
                "rationale": (
                    "Incorrect. Certificate transparency is a public logging system "
                    "for issued certificates; it is not a client-side hard-coded key "
                    "comparison mechanism."
                ),
            },
            {
                "id": "d",
                "text": "Wildcard certificate validation",
                "correct": False,
                "rationale": (
                    "Incorrect. Wildcard validation concerns matching a hostname "
                    "pattern across subdomains, not comparing the actual key material "
                    "against a pinned value."
                ),
            },
        ],
        "explanation": (
            "Certificate/public key pinning hard-codes an expected key in the "
            "client to defeat MITM attacks even from a compromised or fraudulently "
            "issued trusted-CA certificate — distinct from OCSP stapling, "
            "certificate transparency, and wildcard validation."
        ),
    },
    {
        "id": "nd1c-026",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Certificates",
        "stem": (
            "A browser trusts a website's leaf certificate because it can "
            "cryptographically link that certificate, through one intermediate CA's "
            "signature, up to a root CA certificate already embedded in the "
            "operating system's trusted store. What is this hierarchical linkage "
            "BEST called?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Chain of trust",
                "correct": True,
                "rationale": (
                    "Correct. The chain of trust is the hierarchical linkage from a "
                    "leaf certificate through intermediate CAs up to a trusted root, "
                    "which browsers validate to establish trust."
                ),
            },
            {
                "id": "b",
                "text": "Certificate revocation list",
                "correct": False,
                "rationale": (
                    "Incorrect. A CRL is a list of revoked certificates; it has "
                    "nothing to do with the hierarchical signing linkage between "
                    "leaf, intermediate, and root certificates."
                ),
            },
            {
                "id": "c",
                "text": "Certificate signing request",
                "correct": False,
                "rationale": (
                    "Incorrect. A CSR is the request a subject submits to a CA to "
                    "obtain a certificate; it does not describe the trust hierarchy "
                    "validated by the browser."
                ),
            },
            {
                "id": "d",
                "text": "Key escrow",
                "correct": False,
                "rationale": (
                    "Incorrect. Key escrow is a third-party key-recovery arrangement, "
                    "unrelated to how a browser validates a certificate's issuance "
                    "hierarchy."
                ),
            },
        ],
        "explanation": (
            "The chain of trust links a leaf certificate through intermediate CAs "
            "to a trusted root, allowing browsers to validate a certificate's "
            "authenticity — distinct from a CRL, a CSR, or key escrow."
        ),
    },

    # ── 1.4 Cryptographic hardware ───────────────────────────────────────────
    {
        "id": "nd1c-027",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Cryptographic hardware",
        "stem": (
            "To eliminate phishing-based credential theft for privileged accounts, "
            "an organization issues each admin a small USB device that generates a "
            "public/private key pair on-device, never exposes the private key "
            "outside the hardware, and requires a physical touch to complete each "
            "authentication challenge. Which technology is this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "FIDO2/WebAuthn hardware security key",
                "correct": True,
                "rationale": (
                    "Correct. A FIDO2/WebAuthn hardware security key generates an "
                    "on-device key pair, never exposes the private key, and requires "
                    "a physical touch to complete authentication challenges — exactly "
                    "as described."
                ),
            },
            {
                "id": "b",
                "text": "Trusted Platform Module (TPM)",
                "correct": False,
                "rationale": (
                    "Incorrect. A TPM is soldered to a single device's motherboard "
                    "for platform boot integrity and local key sealing, not a "
                    "portable, touch-activated authentication token an admin carries "
                    "and inserts across systems."
                ),
            },
            {
                "id": "c",
                "text": "Hardware Security Module (HSM)",
                "correct": False,
                "rationale": (
                    "Incorrect. An HSM is an appliance-scale device for centralized, "
                    "high-volume cryptographic operations, not a small personal USB "
                    "authentication token."
                ),
            },
            {
                "id": "d",
                "text": "Smart card with contact reader",
                "correct": False,
                "rationale": (
                    "Incorrect. A smart card typically requires a PIN entered into a "
                    "reader with middleware and is a distinct form factor and "
                    "interaction model from a touch-activated USB security key "
                    "generating on-device key pairs for FIDO2 challenges."
                ),
            },
        ],
        "explanation": (
            "FIDO2/WebAuthn hardware security keys generate and retain private keys "
            "on-device and require a physical touch for authentication — distinct "
            "from a TPM (fixed to one motherboard), an HSM (appliance-scale), or a "
            "smart card (PIN/reader-based)."
        ),
    },
    {
        "id": "nd1c-028",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Cryptographic hardware",
        "stem": (
            "A federal agency issues each employee a PIV card containing an "
            "embedded microchip that generates and stores an asymmetric key pair "
            "used for both building door access and workstation login; the private "
            "key is designed to never be extractable from the chip. Which "
            "technology is described?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Smart card",
                "correct": True,
                "rationale": (
                    "Correct. A smart (PIV) card embeds a chip that generates and "
                    "stores a non-extractable key pair, used for physical and logical "
                    "access — exactly as described."
                ),
            },
            {
                "id": "b",
                "text": "Trusted Platform Module (TPM)",
                "correct": False,
                "rationale": (
                    "Incorrect. A TPM is fixed to a single computer's motherboard, "
                    "not a portable, employee-carried card used for both building and "
                    "workstation access across multiple systems."
                ),
            },
            {
                "id": "c",
                "text": "Hardware Security Module (HSM)",
                "correct": False,
                "rationale": (
                    "Incorrect. An HSM is a centralized appliance for enterprise-scale "
                    "cryptographic operations, not a personal, portable identity "
                    "card."
                ),
            },
            {
                "id": "d",
                "text": "Secure Enclave",
                "correct": False,
                "rationale": (
                    "Incorrect. A Secure Enclave is an isolated co-processor within a "
                    "single device (e.g., a smartphone), not a separate, portable "
                    "card carried between multiple systems."
                ),
            },
        ],
        "explanation": (
            "A smart card (such as a PIV card) embeds a chip that generates and "
            "retains a non-extractable key pair for portable physical and logical "
            "access — distinct from a TPM, an HSM, or a Secure Enclave."
        ),
    },

    # ── 1.4 Cryptographic hardware and key-management tools ─────────────────
    {
        "id": "nd1c-029",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Cryptographic hardware and key-management tools",
        "stem": (
            "Company policy requires that a securely stored recovery copy of every "
            "employee's full-disk encryption key be retained by the IT security "
            "team, so data can still be recovered if an employee forgets their "
            "passphrase or leaves the company unexpectedly. Which key-management "
            "practice is this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Key escrow",
                "correct": True,
                "rationale": (
                    "Correct. Key escrow is retaining a recoverable copy of a key "
                    "with a trusted party so data can be recovered even if the "
                    "original key holder is unavailable — exactly as described."
                ),
            },
            {
                "id": "b",
                "text": "Key stretching",
                "correct": False,
                "rationale": (
                    "Incorrect. Key stretching increases the computational cost of "
                    "deriving a key from a password to resist brute-force attacks; it "
                    "doesn't involve retaining a recoverable copy of a key with a "
                    "third party."
                ),
            },
            {
                "id": "c",
                "text": "Key wrapping",
                "correct": False,
                "rationale": (
                    "Incorrect. Key wrapping encrypts one key using another key (a "
                    "KEK) for secure storage or transport; it doesn't describe "
                    "retaining a recovery copy for organizational access after an "
                    "employee leaves."
                ),
            },
            {
                "id": "d",
                "text": "Certificate pinning",
                "correct": False,
                "rationale": (
                    "Incorrect. Certificate pinning hard-codes an expected "
                    "certificate/key for validation purposes; it is unrelated to "
                    "retaining recovery copies of disk-encryption keys."
                ),
            },
        ],
        "explanation": (
            "Key escrow retains a recoverable copy of a key with a trusted party "
            "for recovery purposes — distinct from key stretching (slowing "
            "derivation), key wrapping (encrypting a key with another key), and "
            "certificate pinning (client-side validation)."
        ),
    },
    {
        "id": "nd1c-030",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Cryptographic hardware and key-management tools",
        "stem": (
            "A cloud KMS encrypts each newly generated data-encryption key (DEK) "
            "using a separate, tightly access-controlled key-encryption key (KEK) "
            "before storing the DEK alongside the encrypted data, so the DEK is "
            "never persisted or transmitted in plaintext. Which technique does this "
            "describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Key wrapping (envelope encryption)",
                "correct": True,
                "rationale": (
                    "Correct. Key wrapping (envelope encryption) encrypts a DEK with "
                    "a separate KEK so the DEK is never stored or transmitted in "
                    "plaintext — exactly as described."
                ),
            },
            {
                "id": "b",
                "text": "Key escrow",
                "correct": False,
                "rationale": (
                    "Incorrect. Key escrow involves retaining a recoverable copy of a "
                    "key with a trusted third party for recovery purposes, not "
                    "encrypting one key with another for storage."
                ),
            },
            {
                "id": "c",
                "text": "Key stretching",
                "correct": False,
                "rationale": (
                    "Incorrect. Key stretching adds computational rounds to slow "
                    "password-to-key derivation; it does not describe encrypting one "
                    "cryptographic key using another."
                ),
            },
            {
                "id": "d",
                "text": "Certificate pinning",
                "correct": False,
                "rationale": (
                    "Incorrect. Certificate pinning is a client-side validation "
                    "technique comparing presented certificates/keys against a "
                    "hard-coded expected value, unrelated to encrypting a DEK with a "
                    "KEK."
                ),
            },
        ],
        "explanation": (
            "Key wrapping (envelope encryption) protects a data-encryption key by "
            "encrypting it with a separate key-encryption key — distinct from key "
            "escrow (recovery copies), key stretching (slowing derivation), and "
            "certificate pinning (client-side validation)."
        ),
    },

    # ── 1.4 Hashing and salting ───────────────────────────────────────────────
    {
        "id": "nd1c-031",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Hashing and salting",
        "stem": (
            "A security architect increases the PBKDF2 iteration count used for "
            "password hashing from 10,000 to 600,000 rounds, specifically to "
            "increase the computational time required for each hash attempt and "
            "slow down offline brute-force attacks against stolen hash values. "
            "Which technique is being applied?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Key stretching",
                "correct": True,
                "rationale": (
                    "Correct. Key stretching applies repeated rounds of computation "
                    "to increase the time required per hash attempt, directly "
                    "slowing brute-force attacks against stolen hashes."
                ),
            },
            {
                "id": "b",
                "text": "Salting",
                "correct": False,
                "rationale": (
                    "Incorrect. Salting adds a unique random value per password to "
                    "defeat precomputed rainbow tables and ensure identical passwords "
                    "hash differently; it does not by itself increase the "
                    "computational rounds per hash attempt."
                ),
            },
            {
                "id": "c",
                "text": "Peppering",
                "correct": False,
                "rationale": (
                    "Incorrect. Peppering adds a secret, application-wide value "
                    "(often stored separately from the hash) to the input before "
                    "hashing; it doesn't describe increasing the iteration count."
                ),
            },
            {
                "id": "d",
                "text": "Hash truncation",
                "correct": False,
                "rationale": (
                    "Incorrect. Truncation shortens the output digest length, which "
                    "would weaken rather than strengthen resistance to brute-force "
                    "attacks."
                ),
            },
        ],
        "explanation": (
            "Key stretching increases the computational work (iteration count) "
            "required to derive a hash, directly slowing brute-force attempts — "
            "distinct from salting (uniqueness), peppering (secret application-wide "
            "value), or truncation (shortening output)."
        ),
    },
    {
        "id": "nd1c-032",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Hashing and salting",
        "stem": (
            "A payment API requires every request to include a value computed by "
            "hashing the request body together with a secret key shared only "
            "between the client and server, allowing the server to verify both that "
            "the request wasn't altered in transit and that it originated from a "
            "holder of the shared secret. Which construct is being used?"
        ),
        "options": [
            {
                "id": "a",
                "text": "HMAC (Hash-based Message Authentication Code)",
                "correct": True,
                "rationale": (
                    "Correct. HMAC combines a hash function with a shared secret key "
                    "to provide both integrity and authenticity of the message — "
                    "exactly as described."
                ),
            },
            {
                "id": "b",
                "text": "Salted hash",
                "correct": False,
                "rationale": (
                    "Incorrect. A salted hash combines a password with a random salt "
                    "to defeat rainbow tables; it doesn't use a shared secret key to "
                    "authenticate the origin and integrity of an API request."
                ),
            },
            {
                "id": "c",
                "text": "Digital signature",
                "correct": False,
                "rationale": (
                    "Incorrect. A digital signature uses an asymmetric private key to "
                    "sign data, verified with the corresponding public key; this "
                    "scenario describes a shared SECRET key common to both parties, "
                    "which is the symmetric HMAC construct, not asymmetric signing."
                ),
            },
            {
                "id": "d",
                "text": "Rainbow table",
                "correct": False,
                "rationale": (
                    "Incorrect. A rainbow table is a precomputed lookup structure "
                    "used to crack hashes, not a construct for generating a keyed "
                    "integrity/authenticity value."
                ),
            },
        ],
        "explanation": (
            "HMAC combines a hash function with a shared secret key to provide "
            "keyed integrity and authenticity — distinct from a salted hash "
            "(password storage), a digital signature (asymmetric, proves origin via "
            "private key), or a rainbow table (a cracking tool)."
        ),
    },

    # ── 1.4 Obfuscation techniques ────────────────────────────────────────────
    {
        "id": "nd1c-033",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Obfuscation techniques",
        "stem": (
            "Malware analysts find that a sample's command-and-control domain "
            "strings are encoded in the binary using a simple, publicly documented "
            "single-byte XOR scheme with no secret key — the string is only "
            "readable after applying the same known XOR operation used to encode "
            "it, and anyone who identifies the pattern can reverse it without any "
            "additional secret. Which technique BEST describes this string-hiding "
            "method, and why is it NOT considered encryption?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Obfuscation — reversible by anyone who discovers the technique, since no secret key is required",
                "correct": True,
                "rationale": (
                    "Correct. Obfuscation hides data or logic from casual inspection "
                    "but is reversible by anyone who discovers the method, since it "
                    "relies on no secret key — exactly this XOR scheme."
                ),
            },
            {
                "id": "b",
                "text": "Encryption — because the strings are unreadable without applying a decoding transformation",
                "correct": False,
                "rationale": (
                    "Incorrect. Unreadability alone doesn't make something "
                    "encryption; encryption specifically requires a secret key "
                    "controlling reversibility, which is absent here since the XOR "
                    "scheme uses no secret key."
                ),
            },
            {
                "id": "c",
                "text": "Hashing — because the strings undergo a mathematical transformation before storage",
                "correct": False,
                "rationale": (
                    "Incorrect. Hashing is a one-way function that cannot be reversed "
                    "to recover the original input; this string-hiding is explicitly "
                    "reversible, ruling out hashing."
                ),
            },
            {
                "id": "d",
                "text": "Tokenization — because the original strings are replaced with substitute values",
                "correct": False,
                "rationale": (
                    "Incorrect. Tokenization replaces sensitive values with unrelated "
                    "surrogate tokens tracked in a secure vault, not with an "
                    "XOR-transformed version of the same value reversible via a known "
                    "public algorithm."
                ),
            },
        ],
        "explanation": (
            "Obfuscation hides data or code logic using a technique that is "
            "reversible by anyone who discovers it, since no secret key is "
            "required — distinguishing it from encryption (requires a secret key), "
            "hashing (one-way), and tokenization (vault-based substitution)."
        ),
    },
    {
        "id": "nd1c-034",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Obfuscation techniques",
        "stem": (
            "A call-center application displays only the last four digits of a "
            "customer's stored Social Security number to live agents in real time, "
            "while the complete SSN remains encrypted at rest in the database and "
            "is fully unmasked only for a small number of authorized backend batch "
            "jobs. Which technique is being applied to the agent-facing display?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Dynamic data masking",
                "correct": True,
                "rationale": (
                    "Correct. Dynamic data masking obscures sensitive data at the "
                    "point of display in real time while leaving the underlying "
                    "stored value intact for authorized processes — exactly as "
                    "described."
                ),
            },
            {
                "id": "b",
                "text": "Static data masking",
                "correct": False,
                "rationale": (
                    "Incorrect. Static masking permanently replaces sensitive values "
                    "with altered ones in a separate copy of the data (e.g., a "
                    "QA/test database); here the underlying full SSN is preserved "
                    "unaltered at rest and only obscured at the point of display in "
                    "real time."
                ),
            },
            {
                "id": "c",
                "text": "Tokenization",
                "correct": False,
                "rationale": (
                    "Incorrect. Tokenization replaces the actual value with an "
                    "unrelated surrogate token requiring a separate vault lookup to "
                    "reverse; here the true value is stored intact and merely "
                    "partially hidden on-screen, not substituted by a token."
                ),
            },
            {
                "id": "d",
                "text": "Hashing",
                "correct": False,
                "rationale": (
                    "Incorrect. Hashing is a one-way transformation that cannot be "
                    "reversed to reveal the original digits; the scenario requires "
                    "the full SSN to still be retrievable and unmaskable by "
                    "authorized batch jobs, which a hash could not support."
                ),
            },
        ],
        "explanation": (
            "Dynamic data masking obscures sensitive fields at the point of display "
            "in real time while preserving the true underlying value for authorized "
            "use — distinct from static masking (permanent, separate copy), "
            "tokenization (vault-based substitution), and hashing (one-way, "
            "irreversible)."
        ),
    },

    # ── 1.4 Symmetric vs asymmetric encryption ───────────────────────────────
    {
        "id": "nd1c-035",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Symmetric vs asymmetric encryption",
        "stem": (
            "A TLS 1.3 web server uses a freshly generated, ephemeral "
            "Diffie-Hellman key pair for every new client session, discarding the "
            "ephemeral private key once the session's symmetric keys are derived. "
            "As a result, if the server's long-term certificate private key is "
            "later compromised, an attacker who recorded past encrypted sessions "
            "still cannot decrypt them. Which security property does this ephemeral "
            "key exchange provide?"
        ),
        "options": [
            {
                "id": "a",
                "text": "(Perfect) forward secrecy",
                "correct": True,
                "rationale": (
                    "Correct. Forward secrecy ensures that compromise of a long-term "
                    "key does not expose past session keys, because ephemeral "
                    "session keys are discarded after use — exactly as described."
                ),
            },
            {
                "id": "b",
                "text": "Non-repudiation",
                "correct": False,
                "rationale": (
                    "Incorrect. Non-repudiation proves who performed an action and "
                    "prevents denial of it; it has no bearing on whether past "
                    "recorded sessions remain protected after a later key "
                    "compromise."
                ),
            },
            {
                "id": "c",
                "text": "Key escrow",
                "correct": False,
                "rationale": (
                    "Incorrect. Key escrow is the deliberate retention of a "
                    "recoverable key copy by a third party, which is the opposite of "
                    "the ephemeral, discard-after-use behavior described."
                ),
            },
            {
                "id": "d",
                "text": "Certificate pinning",
                "correct": False,
                "rationale": (
                    "Incorrect. Certificate pinning validates a presented "
                    "certificate/key against a hard-coded expected value; it doesn't "
                    "describe protecting past sessions from a later long-term key "
                    "compromise."
                ),
            },
        ],
        "explanation": (
            "Ephemeral key exchange (e.g., ephemeral Diffie-Hellman) provides "
            "forward secrecy, protecting past session traffic even if a long-term "
            "key is later compromised — distinct from non-repudiation, key escrow, "
            "or certificate pinning."
        ),
    },
    {
        "id": "nd1c-036",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Symmetric vs asymmetric encryption",
        "stem": (
            "Two branch offices need to establish a shared AES-256 key for a "
            "site-to-site VPN tunnel. Rather than transmitting the key over any "
            "network, a courier hand-delivers an encrypted USB drive containing the "
            "key to both locations. Which inherent LIMITATION of symmetric "
            "encryption does this manual courier process illustrate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The secure key-distribution problem — the same secret key must reach both parties without interception",
                "correct": True,
                "rationale": (
                    "Correct. Symmetric encryption requires both parties to possess "
                    "the identical secret key, creating a distribution challenge — "
                    "exactly why a courier is used instead of transmitting the key "
                    "over the network."
                ),
            },
            {
                "id": "b",
                "text": "Slow computational performance compared to asymmetric algorithms",
                "correct": False,
                "rationale": (
                    "Incorrect. Symmetric algorithms like AES are actually much "
                    "FASTER than asymmetric algorithms; this scenario illustrates a "
                    "distribution challenge, not a performance limitation."
                ),
            },
            {
                "id": "c",
                "text": "Inability to provide confidentiality for bulk data",
                "correct": False,
                "rationale": (
                    "Incorrect. Symmetric encryption is well-suited to protecting "
                    "bulk data confidentiality once a key is shared; the scenario "
                    "doesn't describe a confidentiality failure, only the challenge "
                    "of distributing the key itself."
                ),
            },
            {
                "id": "d",
                "text": "Lack of support for authentication of the communicating parties",
                "correct": False,
                "rationale": (
                    "Incorrect. While symmetric encryption alone doesn't provide "
                    "non-repudiation, the scenario specifically illustrates the "
                    "challenge of getting a shared secret to both parties safely, not "
                    "an authentication limitation."
                ),
            },
        ],
        "explanation": (
            "Symmetric encryption's core limitation is secure key distribution — "
            "both parties must obtain the identical secret key without "
            "interception — distinct from performance, bulk-data confidentiality, "
            "or authentication considerations."
        ),
    },
]

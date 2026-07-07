"""
CompTIA Security+ (SY0-701) Domain 1: General Security Concepts — Set B
36 exam-quality questions covering objectives 1.1 through 1.4.
"""

QUESTIONS = [
    # ── 1.1 Security control categories ─────────────────────────────────────
    {
        "id": "nd1b-001",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security control categories",
        "stem": (
            "Executive leadership formally signs a written data-retention policy, "
            "documented in the corporate governance charter, mandating that customer "
            "records be purged seven years after account closure. Which control CATEGORY "
            "does this signed policy itself represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Managerial",
                "correct": True,
                "rationale": (
                    "Correct. Managerial (administrative) controls are governance-level "
                    "decisions captured in policy; a leadership-approved retention policy in "
                    "the governance charter is exactly this kind of oversight artifact."
                ),
            },
            {
                "id": "b",
                "text": "Operational",
                "correct": False,
                "rationale": (
                    "Incorrect. Operational controls are the recurring, people-executed "
                    "activities that carry out policy (e.g., staff actually purging the "
                    "records each quarter), not the governance decision that created the "
                    "requirement."
                ),
            },
            {
                "id": "c",
                "text": "Technical",
                "correct": False,
                "rationale": (
                    "Incorrect. No technology is enforcing this requirement; it is a "
                    "leadership-approved policy decision, not an automated system control."
                ),
            },
            {
                "id": "d",
                "text": "Physical",
                "correct": False,
                "rationale": (
                    "Incorrect. Physical controls protect tangible assets; a written "
                    "retention policy has no physical component."
                ),
            },
        ],
        "explanation": (
            "Managerial controls set direction through governance-approved policy. The "
            "people who later execute the purge on a schedule perform an operational "
            "control; the policy itself is managerial."
        ),
    },
    {
        "id": "nd1b-002",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Security control categories",
        "stem": (
            "Every 90 days, a systems administrator manually compares each employee's "
            "current system entitlements against their job title in HR records and revokes "
            "any access that no longer applies, following a documented checklist. Which "
            "control CATEGORY BEST describes this recurring entitlement review?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Operational",
                "correct": True,
                "rationale": (
                    "Correct. A recurring, people-executed procedure carried out on a "
                    "schedule using a documented checklist is the definition of an "
                    "operational control."
                ),
            },
            {
                "id": "b",
                "text": "Managerial",
                "correct": False,
                "rationale": (
                    "Incorrect. Managerial describes the governance decision requiring "
                    "periodic access reviews, not the administrator's actual hands-on "
                    "execution of that review each quarter."
                ),
            },
            {
                "id": "c",
                "text": "Technical",
                "correct": False,
                "rationale": (
                    "Incorrect. Nothing here is automated by a system; a human is manually "
                    "comparing records and revoking access, which is not a technology-"
                    "enforced control."
                ),
            },
            {
                "id": "d",
                "text": "Physical",
                "correct": False,
                "rationale": (
                    "Incorrect. Physical controls involve tangible assets; an entitlement "
                    "review against HR records has no physical component."
                ),
            },
        ],
        "explanation": (
            "Operational controls are the day-to-day, human-driven procedures that "
            "implement governance policy — distinct from the managerial policy that "
            "required the review in the first place."
        ),
    },

    # ── 1.1 Security control types ──────────────────────────────────────────
    {
        "id": "nd1b-003",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security control types",
        "stem": (
            "A retail chain posts prominent signage at every entrance reading \"This store "
            "is under 24-hour video surveillance,\" intended primarily to discourage a "
            "would-be shoplifter from attempting theft in the first place, independent of "
            "whether cameras are actually recording. Which control TYPE BEST describes the "
            "signage?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Deterrent",
                "correct": True,
                "rationale": (
                    "Correct. A deterrent control discourages a potential threat actor from "
                    "attempting an action by creating a psychological disincentive — exactly "
                    "the purpose of the surveillance signage."
                ),
            },
            {
                "id": "b",
                "text": "Preventive",
                "correct": False,
                "rationale": (
                    "Incorrect. A preventive control physically or logically stops the act "
                    "from occurring; a sign does not physically block theft, it only "
                    "discourages the attempt."
                ),
            },
            {
                "id": "c",
                "text": "Detective",
                "correct": False,
                "rationale": (
                    "Incorrect. Detective controls identify that an incident occurred (e.g., "
                    "the actual camera footage). The question specifies the sign's purpose "
                    "is to discourage the attempt, not to detect one after the fact."
                ),
            },
            {
                "id": "d",
                "text": "Directive",
                "correct": False,
                "rationale": (
                    "Incorrect. Directive controls mandate or direct behavior, typically for "
                    "insiders following internal policy (e.g., an employee handbook rule). "
                    "This signage targets external potential offenders through discouragement, "
                    "not an internal mandate."
                ),
            },
        ],
        "explanation": (
            "Deterrent controls discourage a threat actor from attempting an act, distinct "
            "from preventive controls that physically stop it, detective controls that "
            "identify it afterward, and directive controls that mandate internal behavior."
        ),
    },
    {
        "id": "nd1b-004",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Security control types",
        "stem": (
            "A hospital's acceptable use policy requires every employee to explicitly "
            "acknowledge, and then follow, a documented procedure to report a lost or "
            "stolen device to the help desk within one hour of discovery. Which control "
            "TYPE BEST describes this policy requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Directive",
                "correct": True,
                "rationale": (
                    "Correct. A directive control mandates specific behavior through policy "
                    "or procedure that personnel are required to follow — exactly what this "
                    "acknowledged reporting requirement does."
                ),
            },
            {
                "id": "b",
                "text": "Preventive",
                "correct": False,
                "rationale": (
                    "Incorrect. This requirement does not stop a device from being lost in "
                    "the first place; it mandates a specific response behavior after the "
                    "fact, which is a directive control, not a preventive one."
                ),
            },
            {
                "id": "c",
                "text": "Corrective",
                "correct": False,
                "rationale": (
                    "Incorrect. Corrective controls act to remediate or restore after an "
                    "incident (e.g., remotely wiping the lost device). The policy mandating "
                    "employees follow the reporting procedure is directive; the actual wipe "
                    "action would be corrective."
                ),
            },
            {
                "id": "d",
                "text": "Compensating",
                "correct": False,
                "rationale": (
                    "Incorrect. Compensating controls substitute for a primary control that "
                    "cannot be implemented. Nothing indicates this reporting requirement is "
                    "replacing an infeasible control."
                ),
            },
        ],
        "explanation": (
            "Directive controls mandate specific behavior through policy, typically aimed "
            "at internal personnel — distinct from preventive controls that block an event, "
            "and corrective controls that remediate after one."
        ),
    },

    # ── 1.1 Security control categories and types ───────────────────────────
    {
        "id": "nd1b-005",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security control categories and types",
        "stem": (
            "A bank installs reinforced concrete bollards along the sidewalk in front of "
            "its lobby entrance specifically to physically stop a vehicle from ramming "
            "through the glass storefront before it can reach the building. Which CATEGORY "
            "and TYPE pairing BEST classifies the bollards?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Physical category / Preventive type",
                "correct": True,
                "rationale": (
                    "Correct. Bollards are tangible physical hardware (Physical category) "
                    "that physically stop the vehicle before it reaches the building "
                    "(Preventive type)."
                ),
            },
            {
                "id": "b",
                "text": "Physical category / Deterrent type",
                "correct": False,
                "rationale": (
                    "Incorrect. Bollards do not merely discourage an attempt — they "
                    "physically block the vehicle from reaching the target, which is the "
                    "defining trait of preventive, not deterrent."
                ),
            },
            {
                "id": "c",
                "text": "Technical category / Preventive type",
                "correct": False,
                "rationale": (
                    "Incorrect. Bollards are tangible physical hardware, not a "
                    "logic-enforced technology control; the category is Physical, not "
                    "Technical."
                ),
            },
            {
                "id": "d",
                "text": "Managerial category / Directive type",
                "correct": False,
                "rationale": (
                    "Incorrect. This is not a governance policy decision, nor a mandate "
                    "directing personnel behavior — it is a tangible barrier that "
                    "physically stops a vehicle."
                ),
            },
        ],
        "explanation": (
            "Bollards are a classic Physical/Preventive control: tangible hardware that "
            "physically blocks an attack from succeeding, distinct from a merely "
            "discouraging deterrent."
        ),
    },
    {
        "id": "nd1b-006",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Security control categories and types",
        "stem": (
            "Following a malware incident, IT staff manually restore a compromised server "
            "from a known-good backup image and reapply the latest patches before "
            "reconnecting it to the network, per the incident response runbook. Which "
            "CATEGORY and TYPE pairing BEST classifies this restoration activity?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Operational category / Corrective type",
                "correct": True,
                "rationale": (
                    "Correct. Staff manually performing the restoration is an operational "
                    "activity, and restoring the server to a known-good state after an "
                    "incident is a corrective function."
                ),
            },
            {
                "id": "b",
                "text": "Technical category / Corrective type",
                "correct": False,
                "rationale": (
                    "Incorrect. The restoration is carried out manually by IT staff "
                    "following a runbook, not automatically enforced by technology, so the "
                    "category is Operational, not Technical."
                ),
            },
            {
                "id": "c",
                "text": "Operational category / Detective type",
                "correct": False,
                "rationale": (
                    "Incorrect. Detective controls identify that an incident occurred; "
                    "restoring the server from backup actively remediates the damage, which "
                    "is corrective, not merely detective."
                ),
            },
            {
                "id": "d",
                "text": "Managerial category / Preventive type",
                "correct": False,
                "rationale": (
                    "Incorrect. This is not a governance-level policy decision, and it "
                    "occurs after the incident rather than preventing it from happening."
                ),
            },
        ],
        "explanation": (
            "Manually restoring a system to a known-good state after an incident is an "
            "Operational/Corrective control — people-executed and remediation-focused, "
            "distinct from automated technical enforcement or pre-incident prevention."
        ),
    },

    # ── 1.2 AAA framework ────────────────────────────────────────────────────
    {
        "id": "nd1b-007",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "AAA framework",
        "stem": (
            "In a Windows Active Directory domain, a workstation presents a time-stamped "
            "ticket-granting ticket, issued by a Key Distribution Center at initial logon, "
            "to request individual service tickets for specific network resources without "
            "re-entering the user's credentials. Which authentication protocol is in use?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Kerberos",
                "correct": True,
                "rationale": (
                    "Correct. Kerberos issues a time-stamped ticket-granting ticket from a "
                    "Key Distribution Center, which the client then presents to obtain "
                    "service tickets for individual resources without re-authenticating."
                ),
            },
            {
                "id": "b",
                "text": "RADIUS",
                "correct": False,
                "rationale": (
                    "Incorrect. RADIUS is a network access AAA protocol used for things "
                    "like VPN and Wi-Fi authentication over UDP; it does not issue "
                    "ticket-granting tickets from a Key Distribution Center."
                ),
            },
            {
                "id": "c",
                "text": "TACACS+",
                "correct": False,
                "rationale": (
                    "Incorrect. TACACS+ is used primarily for device administration AAA "
                    "(e.g., router/switch CLI access) over TCP; it has no concept of a "
                    "ticket-granting ticket or Key Distribution Center."
                ),
            },
            {
                "id": "d",
                "text": "SAML",
                "correct": False,
                "rationale": (
                    "Incorrect. SAML is an XML-based federation protocol used to exchange "
                    "identity assertions between an identity provider and a web service "
                    "provider; it does not describe a KDC-issued ticket-granting ticket."
                ),
            },
        ],
        "explanation": (
            "Kerberos is uniquely defined by its ticket-granting ticket issued by a Key "
            "Distribution Center, distinguishing it from RADIUS/TACACS+ (network/device "
            "access AAA) and SAML (web federation)."
        ),
    },
    {
        "id": "nd1b-008",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "AAA framework",
        "stem": (
            "A VPN concentrator records the exact timestamp, session duration, and total "
            "bytes transferred for every remote employee's connection, feeding this data "
            "into a billing and compliance reporting system. Which element of the AAA "
            "framework does this recording function represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Accounting",
                "correct": True,
                "rationale": (
                    "Correct. Accounting is the AAA function that logs resource usage — "
                    "session time, duration, and data transferred — for billing, capacity "
                    "planning, and auditing purposes."
                ),
            },
            {
                "id": "b",
                "text": "Authentication",
                "correct": False,
                "rationale": (
                    "Incorrect. Authentication verifies the user's identity at connection "
                    "time; it does not itself track ongoing session duration or bytes "
                    "transferred for billing purposes."
                ),
            },
            {
                "id": "c",
                "text": "Authorization",
                "correct": False,
                "rationale": (
                    "Incorrect. Authorization determines what an authenticated user is "
                    "permitted to access; it does not record usage metrics like session "
                    "duration or bandwidth consumed."
                ),
            },
            {
                "id": "d",
                "text": "Non-repudiation",
                "correct": False,
                "rationale": (
                    "Incorrect. Non-repudiation is a broader security property proving a "
                    "party cannot deny an action; it is not one of the three AAA "
                    "functions and is not specifically the usage-logging function described."
                ),
            },
        ],
        "explanation": (
            "Accounting is the third pillar of AAA, responsible for logging session "
            "metrics such as duration and bytes transferred — distinct from authentication "
            "(identity verification) and authorization (permission granting)."
        ),
    },

    # ── 1.2 Attack type identification ──────────────────────────────────────
    {
        "id": "nd1b-009",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Attack type identification",
        "stem": (
            "An attacker purchases a bulk list of phone numbers and sends text messages "
            "claiming the recipient's bank account has been locked, with a link to a "
            "fraudulent look-alike banking site to \"verify\" account details. Which attack "
            "technique is BEST described?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Smishing",
                "correct": True,
                "rationale": (
                    "Correct. Smishing is phishing conducted via SMS text message, exactly "
                    "as described — a fraudulent text with a malicious link."
                ),
            },
            {
                "id": "b",
                "text": "Vishing",
                "correct": False,
                "rationale": (
                    "Incorrect. Vishing is voice/phone-call-based social engineering; this "
                    "attack was conducted entirely through text messages, not a phone call."
                ),
            },
            {
                "id": "c",
                "text": "Whaling",
                "correct": False,
                "rationale": (
                    "Incorrect. Whaling targets a specific senior executive with tailored, "
                    "high-value context; this is a mass, untargeted text message sent to a "
                    "purchased bulk list, not a targeted executive attack."
                ),
            },
            {
                "id": "d",
                "text": "Pharming",
                "correct": False,
                "rationale": (
                    "Incorrect. Pharming redirects users to a fraudulent site through DNS "
                    "or hosts-file manipulation without any message being sent; here the "
                    "victim is lured via a text message link, not a passive DNS redirect."
                ),
            },
        ],
        "explanation": (
            "Smishing is phishing delivered via SMS. It is distinguished from vishing "
            "(voice), whaling (targeted executive), and pharming (DNS-based redirection "
            "without a lure message)."
        ),
    },
    {
        "id": "nd1b-010",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Attack type identification",
        "stem": (
            "A threat actor compromises a niche online forum frequented almost exclusively "
            "by aerospace engineers and embeds malicious JavaScript that only executes "
            "exploit code when it detects the visitor's IP address belongs to a known "
            "defense contractor's network. Which attack technique is BEST described?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Watering hole attack",
                "correct": True,
                "rationale": (
                    "Correct. A watering hole attack compromises a website the target group "
                    "is known to frequent and waits for victims to visit, often with "
                    "conditional logic to target only the intended organization."
                ),
            },
            {
                "id": "b",
                "text": "Supply chain attack",
                "correct": False,
                "rationale": (
                    "Incorrect. A supply chain attack compromises a trusted vendor or "
                    "software component that is then distributed to customers; a general "
                    "industry forum is not a vendor relationship or software supply chain."
                ),
            },
            {
                "id": "c",
                "text": "Typosquatting",
                "correct": False,
                "rationale": (
                    "Incorrect. Typosquatting relies on registering domains with misspelled "
                    "names similar to a legitimate site to catch mistyped URLs; this attack "
                    "compromised the legitimate, correctly-spelled forum itself."
                ),
            },
            {
                "id": "d",
                "text": "Business email compromise (BEC)",
                "correct": False,
                "rationale": (
                    "Incorrect. BEC involves fraudulent email impersonation to solicit "
                    "wire transfers or data; no email or impersonation is involved in this "
                    "browser-based, IP-conditional exploit delivery."
                ),
            },
        ],
        "explanation": (
            "A watering hole attack targets a site the victim group is known to frequent, "
            "distinguishing it from supply chain compromise (trusted vendor), "
            "typosquatting (lookalike domains), and BEC (email impersonation fraud)."
        ),
    },

    # ── 1.2 CIA triad and non-repudiation ────────────────────────────────────
    {
        "id": "nd1b-011",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "CIA triad and non-repudiation",
        "stem": (
            "A volumetric DDoS attack floods a hospital's patient portal for six hours, "
            "preventing clinicians from accessing scheduling data, though no data was "
            "viewed, altered, or exfiltrated during the attack. Which security objective "
            "was violated?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Availability",
                "correct": True,
                "rationale": (
                    "Correct. Preventing authorized users from accessing a system or data "
                    "when needed is precisely a violation of availability."
                ),
            },
            {
                "id": "b",
                "text": "Integrity",
                "correct": False,
                "rationale": (
                    "Incorrect. Integrity concerns unauthorized modification of data; the "
                    "scenario explicitly states no data was altered."
                ),
            },
            {
                "id": "c",
                "text": "Confidentiality",
                "correct": False,
                "rationale": (
                    "Incorrect. Confidentiality concerns unauthorized viewing of data; the "
                    "scenario explicitly states no data was viewed or exfiltrated."
                ),
            },
            {
                "id": "d",
                "text": "Non-repudiation",
                "correct": False,
                "rationale": (
                    "Incorrect. Non-repudiation concerns proving who performed an action; "
                    "the scenario is about a service outage, not a dispute over "
                    "attribution of an action."
                ),
            },
        ],
        "explanation": (
            "A DDoS attack that denies access without altering or exposing data is a "
            "textbook availability violation, distinct from integrity, confidentiality, or "
            "non-repudiation."
        ),
    },
    {
        "id": "nd1b-012",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "CIA triad and non-repudiation",
        "stem": (
            "A disgruntled employee uses a shared administrative account, with no "
            "individual logins, to alter three vendor payment records the night before a "
            "financial audit. Because three different administrators share that one "
            "account with no per-user logging, investigators cannot determine which "
            "specific person made the changes. Which TWO security properties were MOST "
            "directly compromised? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Integrity",
                "correct": True,
                "rationale": (
                    "Correct. The payment records were altered without authorization, "
                    "which is a direct violation of data integrity."
                ),
            },
            {
                "id": "b",
                "text": "Non-repudiation",
                "correct": True,
                "rationale": (
                    "Correct. Because the account is shared with no individual "
                    "accountability, investigators cannot attribute the change to a "
                    "specific person — the definition of a non-repudiation failure."
                ),
            },
            {
                "id": "c",
                "text": "Confidentiality",
                "correct": False,
                "rationale": (
                    "Incorrect. Nothing indicates unauthorized viewing of data occurred; "
                    "the issue described is unauthorized alteration and lack of "
                    "attribution, not disclosure."
                ),
            },
            {
                "id": "d",
                "text": "Availability",
                "correct": False,
                "rationale": (
                    "Incorrect. The records remain accessible — they were altered, not "
                    "deleted or made inaccessible to authorized users."
                ),
            },
            {
                "id": "e",
                "text": "Authentication",
                "correct": False,
                "rationale": (
                    "Incorrect. Authentication is an AAA process, not one of the security "
                    "objectives compromised by this outcome; the weak shared-account "
                    "practice is a root-cause control failure, not itself the property "
                    "that was violated."
                ),
            },
        ],
        "explanation": (
            "Unauthorized alteration of records violates integrity, and the shared "
            "account's lack of individual attribution defeats non-repudiation — two "
            "distinct properties, neither of which is confidentiality or availability."
        ),
    },

    # ── 1.2 Deception and disruption technologies ───────────────────────────
    {
        "id": "nd1b-013",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Deception and disruption technologies",
        "stem": (
            "A security team deploys a single, fully isolated, intentionally vulnerable "
            "RDP server in the DMZ, disconnected from any production system, purely to "
            "observe and study attacker tools and techniques after compromise. Which "
            "technique is this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Honeypot",
                "correct": True,
                "rationale": (
                    "Correct. A honeypot is a single decoy system deliberately made "
                    "attractive and vulnerable to lure and study attacker behavior in "
                    "isolation from production."
                ),
            },
            {
                "id": "b",
                "text": "Honeynet",
                "correct": False,
                "rationale": (
                    "Incorrect. A honeynet is an entire network of multiple interconnected "
                    "decoy systems used to observe lateral movement; the scenario describes "
                    "a single standalone decoy server."
                ),
            },
            {
                "id": "c",
                "text": "Honeytoken",
                "correct": False,
                "rationale": (
                    "Incorrect. A honeytoken is a fake credential or data value monitored "
                    "for misuse elsewhere, not an entire decoy system that attackers log "
                    "into and interact with."
                ),
            },
            {
                "id": "d",
                "text": "Honeyfile",
                "correct": False,
                "rationale": (
                    "Incorrect. A honeyfile is a single decoy document monitored for "
                    "unauthorized access, not a full standalone decoy server system."
                ),
            },
        ],
        "explanation": (
            "A single, isolated, intentionally vulnerable decoy system is a honeypot — "
            "distinct from a honeynet (multiple interconnected decoys), honeytoken (fake "
            "credential), and honeyfile (fake document)."
        ),
    },
    {
        "id": "nd1b-014",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Deception and disruption technologies",
        "stem": (
            "To frustrate credential-stuffing bots, a web application intentionally "
            "introduces an incrementally increasing multi-second delay before responding "
            "to each failed login attempt originating from the same source IP address, "
            "wasting the attacker's time and compute resources. Which technique is this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Tarpit",
                "correct": True,
                "rationale": (
                    "Correct. A tarpit intentionally slows down or stalls an attacker's "
                    "connection or requests to waste their time and resources, exactly as "
                    "described."
                ),
            },
            {
                "id": "b",
                "text": "Honeypot",
                "correct": False,
                "rationale": (
                    "Incorrect. A honeypot is a decoy system meant to lure and be "
                    "interacted with; this describes a delay mechanism applied to the real "
                    "login endpoint, not a separate decoy system."
                ),
            },
            {
                "id": "c",
                "text": "DNS sinkhole",
                "correct": False,
                "rationale": (
                    "Incorrect. A DNS sinkhole redirects malicious domain resolutions to a "
                    "controlled destination; it does not describe throttling login "
                    "responses on a web application."
                ),
            },
            {
                "id": "d",
                "text": "Fake telemetry",
                "correct": False,
                "rationale": (
                    "Incorrect. Fake telemetry feeds false data to mislead an attacker's "
                    "reconnaissance; it does not describe an escalating response delay "
                    "mechanism against login attempts."
                ),
            },
        ],
        "explanation": (
            "A tarpit deliberately slows down malicious connections to waste attacker "
            "resources — distinct from honeypots (decoy systems), DNS sinkholes (domain "
            "redirection), and fake telemetry (deceptive data)."
        ),
    },

    # ── 1.2 Gap analysis ─────────────────────────────────────────────────────
    {
        "id": "nd1b-015",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Gap analysis",
        "stem": (
            "After adopting a new customer data-handling standard, a privacy team compares "
            "its current data-retention and encryption practices against the standard's "
            "requirements and publishes a report listing exactly which controls are "
            "missing and target dates for remediation. Which process was performed?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Gap analysis",
                "correct": True,
                "rationale": (
                    "Correct. Comparing current practices against a target standard and "
                    "documenting deficiencies with a remediation timeline is the definition "
                    "of a gap analysis."
                ),
            },
            {
                "id": "b",
                "text": "Business impact analysis",
                "correct": False,
                "rationale": (
                    "Incorrect. A BIA identifies critical functions and quantifies downtime "
                    "impact (RTO/RPO), not a comparison of current controls against a named "
                    "standard's requirements."
                ),
            },
            {
                "id": "c",
                "text": "Penetration test",
                "correct": False,
                "rationale": (
                    "Incorrect. A penetration test actively attempts to exploit weaknesses; "
                    "this scenario is a documentation-based comparative review, not active "
                    "exploitation."
                ),
            },
            {
                "id": "d",
                "text": "Tabletop exercise",
                "correct": False,
                "rationale": (
                    "Incorrect. A tabletop exercise is a discussion-based simulation of an "
                    "incident response scenario, not a comparison of controls against a "
                    "compliance standard."
                ),
            },
        ],
        "explanation": (
            "Gap analysis measures current state against a desired target (a standard, "
            "framework, or regulation) and produces a prioritized remediation roadmap — "
            "distinct from a BIA, penetration test, or tabletop exercise."
        ),
    },
    {
        "id": "nd1b-016",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Gap analysis",
        "stem": (
            "During a framework-comparison exercise, a CISO discovers that the "
            "organization already owns and has licensed encryption-at-rest technology "
            "capable of satisfying a required control, but staff never enabled it because "
            "no documented procedure ever assigned anyone the responsibility to do so. "
            "Which type of gap does this MOST accurately represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Operational gap",
                "correct": True,
                "rationale": (
                    "Correct. The required technical capability already exists; what is "
                    "missing is the process and assigned responsibility to use it, which is "
                    "an operational (process) gap rather than a technology gap."
                ),
            },
            {
                "id": "b",
                "text": "Technical gap",
                "correct": False,
                "rationale": (
                    "Incorrect. A technical gap means the required technology or capability "
                    "does not exist. Here the encryption capability is already licensed and "
                    "available — the deficiency is procedural, not technological."
                ),
            },
            {
                "id": "c",
                "text": "Business gap",
                "correct": False,
                "rationale": (
                    "Incorrect. A business gap reflects misalignment between security "
                    "controls and overall business objectives or strategy; this scenario "
                    "describes a missing operational procedure for using existing "
                    "technology, not a strategic misalignment."
                ),
            },
            {
                "id": "d",
                "text": "Physical gap",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no tangible/physical security deficiency described; "
                    "the issue is entirely about missing process ownership for enabling "
                    "existing software."
                ),
            },
        ],
        "explanation": (
            "Gap analysis distinguishes technical gaps (missing capability) from "
            "operational gaps (missing process/ownership despite having the capability) — "
            "a nuance frequently tested at the expert level."
        ),
    },

    # ── 1.2 Physical security ────────────────────────────────────────────────
    {
        "id": "nd1b-017",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Physical security",
        "stem": (
            "A network closet's electronic strike lock is wired so that, if building power "
            "is lost, the door automatically unlocks to comply with fire and life-safety "
            "code rather than remaining locked. Which term describes this locking behavior?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Fail-safe (fails unlocked to prioritize life safety)",
                "correct": True,
                "rationale": (
                    "Correct. A fail-safe lock defaults to an unlocked state on power loss, "
                    "prioritizing occupant egress and life safety over strict physical "
                    "security."
                ),
            },
            {
                "id": "b",
                "text": "Fail-secure (fails locked to prioritize asset protection)",
                "correct": False,
                "rationale": (
                    "Incorrect. A fail-secure lock remains locked during a power outage to "
                    "protect assets, the opposite of the automatic-unlock behavior described "
                    "in this fire-code scenario."
                ),
            },
            {
                "id": "c",
                "text": "Fail-open network access control",
                "correct": False,
                "rationale": (
                    "Incorrect. Fail-open/fail-closed terminology is typically applied to "
                    "network devices like firewalls, not physical door locks; the correct "
                    "physical security term for a door defaulting to unlocked is fail-safe."
                ),
            },
            {
                "id": "d",
                "text": "Piggybacking prevention",
                "correct": False,
                "rationale": (
                    "Incorrect. Piggybacking prevention concerns stopping an unauthorized "
                    "person from following an authorized person through a door, which is "
                    "unrelated to how the lock behaves during a power failure."
                ),
            },
        ],
        "explanation": (
            "Fail-safe locks default to unlocked on power loss (life safety priority); "
            "fail-secure locks default to locked (asset protection priority). Fail-open/"
            "fail-closed is the analogous but distinct terminology used for network "
            "devices."
        ),
    },
    {
        "id": "nd1b-018",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Physical security",
        "stem": (
            "A bank branch installs reinforced concrete planters, indistinguishable from "
            "ordinary landscaping, along the sidewalk in front of its glass storefront "
            "specifically to stop a vehicle-ramming attack without visibly signaling a "
            "security measure to pedestrians. Which control BEST describes these planters?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Disguised bollards",
                "correct": True,
                "rationale": (
                    "Correct. These planters function as bollards — engineered to stop "
                    "vehicles — while being aesthetically disguised as ordinary landscaping "
                    "rather than an obvious security barrier."
                ),
            },
            {
                "id": "b",
                "text": "Access control vestibule (mantrap)",
                "correct": False,
                "rationale": (
                    "Incorrect. A mantrap regulates single-person pedestrian entry through "
                    "an interlocked pair of doors; it has no role in stopping a "
                    "vehicle-ramming attack against a storefront."
                ),
            },
            {
                "id": "c",
                "text": "Perimeter fencing",
                "correct": False,
                "rationale": (
                    "Incorrect. Fencing typically marks and restricts a property boundary "
                    "over a wide perimeter; it is not the targeted, vehicle-stopping barrier "
                    "placed directly in front of a specific storefront described here."
                ),
            },
            {
                "id": "d",
                "text": "Warning signage",
                "correct": False,
                "rationale": (
                    "Incorrect. Signage is a deterrent that relies on communicating a "
                    "warning; the planters physically stop the vehicle and are explicitly "
                    "designed NOT to look like a security measure at all."
                ),
            },
        ],
        "explanation": (
            "Disguised bollards provide preventive, vehicle-stopping physical security "
            "while blending into the landscape — distinct from mantraps (pedestrian "
            "access control), fencing (perimeter boundary), and signage (deterrent "
            "communication)."
        ),
    },

    # ── 1.2 Zero Trust architecture ──────────────────────────────────────────
    {
        "id": "nd1b-019",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Zero Trust architecture",
        "stem": (
            "In a Zero Trust deployment, a remote employee's laptop must pass a fresh "
            "check of patch level, EDR agent status, and disk-encryption state at EVERY "
            "individual resource request, rather than being trusted for the remainder of "
            "the session after one initial login. Which Zero Trust principle is BEST "
            "illustrated?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Continuous validation",
                "correct": True,
                "rationale": (
                    "Correct. Continuous validation (\"never trust, always verify\") "
                    "requires re-evaluating trust for every request rather than granting "
                    "durable trust after a single login — exactly what is described."
                ),
            },
            {
                "id": "b",
                "text": "Implicit trust zone",
                "correct": False,
                "rationale": (
                    "Incorrect. An implicit trust zone is the legacy perimeter-based concept "
                    "Zero Trust eliminates; the scenario describes the opposite — no request "
                    "is implicitly trusted regardless of network location."
                ),
            },
            {
                "id": "c",
                "text": "Single sign-on (SSO)",
                "correct": False,
                "rationale": (
                    "Incorrect. SSO allows one authentication event to grant access across "
                    "multiple systems; the scenario explicitly re-checks posture at every "
                    "request instead of relying on a single durable authentication."
                ),
            },
            {
                "id": "d",
                "text": "Least privilege",
                "correct": False,
                "rationale": (
                    "Incorrect. Least privilege concerns limiting the scope of granted "
                    "permissions to only what is necessary, not the frequency or timing of "
                    "re-evaluating trust for each request."
                ),
            },
        ],
        "explanation": (
            "Continuous validation is a core Zero Trust tenet: every request is "
            "independently evaluated rather than relying on trust established once at "
            "login — distinct from implicit trust, SSO, and least privilege."
        ),
    },
    {
        "id": "nd1b-020",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Zero Trust architecture",
        "stem": (
            "As part of a Zero Trust redesign, an organization divides its data center "
            "into many small, isolated policy zones so that even two servers on the same "
            "physical VLAN must mutually authenticate and be explicitly authorized before "
            "one can communicate with the other. Which term BEST describes this design?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Microsegmentation",
                "correct": True,
                "rationale": (
                    "Correct. Microsegmentation creates many small, granular policy zones "
                    "down to the individual workload level, requiring explicit "
                    "authentication and authorization even for east-west traffic within the "
                    "same traditional network segment."
                ),
            },
            {
                "id": "b",
                "text": "Traditional VLAN segmentation",
                "correct": False,
                "rationale": (
                    "Incorrect. Traditional VLAN segmentation groups hosts into broad "
                    "logical segments and implicitly trusts traffic within the same VLAN — "
                    "the opposite of requiring mutual authentication between hosts on the "
                    "same VLAN."
                ),
            },
            {
                "id": "c",
                "text": "Macrosegmentation",
                "correct": False,
                "rationale": (
                    "Incorrect. Macrosegmentation refers to large-scale separation between "
                    "broad zones (e.g., production vs. development networks), not the "
                    "fine-grained, per-workload isolation described here."
                ),
            },
            {
                "id": "d",
                "text": "Software-defined WAN (SD-WAN)",
                "correct": False,
                "rationale": (
                    "Incorrect. SD-WAN optimizes and manages wide-area network connectivity "
                    "between sites; it does not describe granular intra-data-center, "
                    "workload-level authentication policy."
                ),
            },
        ],
        "explanation": (
            "Microsegmentation enforces granular, workload-level policy boundaries that "
            "eliminate implicit trust even within a single traditional network segment — "
            "distinct from coarse VLAN or macro-level segmentation."
        ),
    },

    # ── 1.3 Change management ────────────────────────────────────────────────
    {
        "id": "nd1b-021",
        "domain": 1,
        "objective": "1.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Change management",
        "stem": (
            "An IT team deploys a routine, low-risk DNS record update using a documented, "
            "previously tested procedure that the Change Advisory Board has pre-approved "
            "for repeated use, so no case-by-case CAB review is required each time it is "
            "performed. Which change type was used?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Standard change",
                "correct": True,
                "rationale": (
                    "Correct. Standard changes are low-risk, well-understood, pre-approved "
                    "changes that follow a documented, repeatable procedure without "
                    "requiring individual CAB review each time."
                ),
            },
            {
                "id": "b",
                "text": "Normal change",
                "correct": False,
                "rationale": (
                    "Incorrect. Normal changes require case-by-case CAB review and approval "
                    "before implementation; this DNS update was explicitly pre-approved for "
                    "repeated use without individual review."
                ),
            },
            {
                "id": "c",
                "text": "Emergency change",
                "correct": False,
                "rationale": (
                    "Incorrect. Emergency changes are expedited responses to a critical "
                    "incident requiring retrospective review; nothing indicates this DNS "
                    "update was made in response to an active incident."
                ),
            },
            {
                "id": "d",
                "text": "Unauthorized change",
                "correct": False,
                "rationale": (
                    "Incorrect. This change followed a documented, CAB-sanctioned process; "
                    "an unauthorized change lacks any governance oversight or approval "
                    "pathway."
                ),
            },
        ],
        "explanation": (
            "Standard changes are routine, low-risk, and pre-approved for repeated use, "
            "distinguishing them from normal changes (individual CAB review each time), "
            "emergency changes (incident-driven), and unauthorized changes (no governance)."
        ),
    },
    {
        "id": "nd1b-022",
        "domain": 1,
        "objective": "1.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Change management",
        "stem": (
            "Before presenting a proposed migration to a new email platform to the Change "
            "Advisory Board, a project team documents the anticipated downtime, the "
            "departments affected, dependent systems, and the estimated business risk if "
            "the migration fails. Which element of the change management process does this "
            "documentation represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Impact analysis",
                "correct": True,
                "rationale": (
                    "Correct. Impact analysis assesses the anticipated technical and "
                    "business consequences of a proposed change — downtime, affected "
                    "systems and departments, and risk — before it goes to the CAB for "
                    "approval."
                ),
            },
            {
                "id": "b",
                "text": "Backout plan",
                "correct": False,
                "rationale": (
                    "Incorrect. A backout plan documents how to reverse the change if it "
                    "fails during implementation; this scenario describes assessing "
                    "anticipated impact beforehand, not the reversal procedure."
                ),
            },
            {
                "id": "c",
                "text": "Request for Change (RFC)",
                "correct": False,
                "rationale": (
                    "Incorrect. The RFC is the initial submission proposing the change and "
                    "its justification; the detailed downtime/impact/risk assessment "
                    "described here is a distinct supporting artifact — the impact "
                    "analysis — not the RFC itself."
                ),
            },
            {
                "id": "d",
                "text": "Post-implementation review",
                "correct": False,
                "rationale": (
                    "Incorrect. A post-implementation review occurs AFTER the change is "
                    "deployed to verify success; this documentation is prepared BEFORE CAB "
                    "review to inform the approval decision."
                ),
            },
        ],
        "explanation": (
            "Impact analysis evaluates anticipated downtime, affected stakeholders, and "
            "risk before CAB approval — distinct from the backout plan, the initial RFC, "
            "and the later post-implementation review."
        ),
    },

    # ── 1.4 Blockchain and open public ledger ────────────────────────────────
    {
        "id": "nd1b-023",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Blockchain and open public ledger",
        "stem": (
            "A consortium of shipping companies requires every participating node to "
            "independently validate a new block of transactions using computational "
            "proof-of-work before it can be appended to the shared ledger, so that no "
            "single participant can unilaterally agree on or rewrite the transaction "
            "history alone. Which blockchain feature is PRIMARILY responsible for enabling "
            "this network-wide agreement without a central authority?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Consensus mechanism",
                "correct": True,
                "rationale": (
                    "Correct. A consensus mechanism, such as proof-of-work, is the process "
                    "by which distributed, mutually distrusting nodes agree on the valid "
                    "state of the ledger without relying on a central authority."
                ),
            },
            {
                "id": "b",
                "text": "Immutability",
                "correct": False,
                "rationale": (
                    "Incorrect. Immutability describes the resulting property that "
                    "accepted blocks cannot later be altered; it is the OUTCOME of "
                    "consensus and hash-chaining, not the mechanism that produces network-"
                    "wide agreement in the first place."
                ),
            },
            {
                "id": "c",
                "text": "Hash chaining",
                "correct": False,
                "rationale": (
                    "Incorrect. Hash chaining links each block to the previous one to make "
                    "tampering detectable, but it does not, by itself, determine how "
                    "independent nodes agree on which new block is valid."
                ),
            },
            {
                "id": "d",
                "text": "Smart contract execution",
                "correct": False,
                "rationale": (
                    "Incorrect. Smart contracts are self-executing code triggered by "
                    "on-chain conditions; they have no role in how nodes reach agreement on "
                    "the validity of new blocks."
                ),
            },
        ],
        "explanation": (
            "The consensus mechanism (e.g., proof-of-work) is what allows distributed "
            "nodes to agree on ledger state without central authority; immutability and "
            "hash chaining describe resulting tamper-evidence properties, not the "
            "agreement process itself."
        ),
    },
    {
        "id": "nd1b-024",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Blockchain and open public ledger",
        "stem": (
            "A logistics company automatically releases payment to a supplier the instant "
            "IoT sensors confirm a shipment container has been delivered and its GPS "
            "coordinates match the destination, using self-executing code stored on the "
            "blockchain with no human approval step. Which term BEST describes this "
            "self-executing code?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Smart contract",
                "correct": True,
                "rationale": (
                    "Correct. A smart contract is self-executing code stored on a "
                    "blockchain that automatically performs an action, such as releasing "
                    "payment, once predefined on-chain conditions are met."
                ),
            },
            {
                "id": "b",
                "text": "Consensus mechanism",
                "correct": False,
                "rationale": (
                    "Incorrect. A consensus mechanism is how nodes agree on the validity of "
                    "new blocks; it does not describe the conditional, self-executing "
                    "payment-release logic itself."
                ),
            },
            {
                "id": "c",
                "text": "Distributed ledger",
                "correct": False,
                "rationale": (
                    "Incorrect. A distributed ledger is the underlying shared record store "
                    "across nodes; it is not the self-executing conditional code that "
                    "triggers the payment action."
                ),
            },
            {
                "id": "d",
                "text": "Cryptocurrency wallet",
                "correct": False,
                "rationale": (
                    "Incorrect. A wallet stores and manages a party's cryptographic keys "
                    "and balances; it does not itself contain the conditional logic that "
                    "automatically triggers payment based on sensor and GPS data."
                ),
            },
        ],
        "explanation": (
            "Smart contracts are self-executing code that automatically carry out actions "
            "once on-chain conditions are satisfied — distinct from the consensus "
            "mechanism, the distributed ledger itself, and a cryptocurrency wallet."
        ),
    },

    # ── 1.4 Certificates ──────────────────────────────────────────────────────
    {
        "id": "nd1b-025",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Certificates",
        "stem": (
            "A company's security policy explicitly prohibits wildcard certificates "
            "because a single compromised wildcard private key would expose every current "
            "and future subdomain. The company still needs one certificate covering three "
            "specific, named hosts: www.example.com, mail.example.com, and vpn.example.com. "
            "Which certificate type BEST satisfies this requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "SAN (Subject Alternative Name) certificate",
                "correct": True,
                "rationale": (
                    "Correct. A SAN certificate explicitly enumerates a limited, named list "
                    "of hostnames it covers, satisfying the multi-host requirement without "
                    "the broad blast radius of a wildcard."
                ),
            },
            {
                "id": "b",
                "text": "Wildcard certificate",
                "correct": False,
                "rationale": (
                    "Incorrect. A wildcard certificate covers any first-level subdomain "
                    "and is exactly the broad, blast-radius-expanding certificate type the "
                    "policy explicitly prohibits."
                ),
            },
            {
                "id": "c",
                "text": "Self-signed certificate",
                "correct": False,
                "rationale": (
                    "Incorrect. A self-signed certificate is not issued by a trusted CA and "
                    "would trigger trust warnings for public-facing hosts; it does not "
                    "address the requirement of covering multiple named hosts under a "
                    "trusted chain."
                ),
            },
            {
                "id": "d",
                "text": "Extended Validation (EV) certificate",
                "correct": False,
                "rationale": (
                    "Incorrect. EV describes the rigor of the identity-vetting process, "
                    "not whether a certificate can cover multiple explicitly named hosts; "
                    "it does not by itself solve the multi-hostname requirement."
                ),
            },
        ],
        "explanation": (
            "SAN certificates list explicit, named hostnames, limiting the blast radius of "
            "a compromised key compared to a wildcard — a distinction increasingly "
            "important in high-security environments that ban wildcards."
        ),
    },
    {
        "id": "nd1b-026",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Certificates",
        "stem": (
            "A CA revokes a compromised intermediate certificate immediately after "
            "discovering its private key was stolen. Investigators later find that browsers "
            "relying on locally cached CRL data from a week earlier continued trusting "
            "certificates issued by that intermediate for several additional days after "
            "revocation. Which TWO factors MOST directly contributed to this delayed "
            "recognition? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "CRLs are published on a periodic schedule rather than updated in real time",
                "correct": True,
                "rationale": (
                    "Correct. CRLs are distributed at defined publication intervals, so a "
                    "revocation that occurs between publications will not be reflected "
                    "until the next scheduled update."
                ),
            },
            {
                "id": "b",
                "text": "The affected clients relied on locally cached revocation data instead of querying a live source",
                "correct": True,
                "rationale": (
                    "Correct. Using stale, locally cached CRL data instead of checking a "
                    "current source means the client remains unaware of a revocation that "
                    "occurred after the cache was last refreshed."
                ),
            },
            {
                "id": "c",
                "text": "OCSP stapling was enabled on the affected web servers",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario states clients relied on cached CRL data, not "
                    "OCSP; OCSP stapling would actually provide fresher, server-attached "
                    "revocation status, not delay it, so it does not explain the described "
                    "outcome."
                ),
            },
            {
                "id": "d",
                "text": "The intermediate certificate used ECDSA instead of RSA",
                "correct": False,
                "rationale": (
                    "Incorrect. The signature algorithm used by the certificate has no "
                    "bearing on how or when revocation status propagates to clients."
                ),
            },
            {
                "id": "e",
                "text": "Certificate Transparency logging was disabled for the intermediate",
                "correct": False,
                "rationale": (
                    "Incorrect. Certificate Transparency logs improve visibility into "
                    "certificate issuance for monitoring and detection purposes; they do "
                    "not control how quickly revocation status reaches relying clients."
                ),
            },
        ],
        "explanation": (
            "Revocation-checking delays stem from the periodic, non-real-time nature of "
            "CRL publication combined with clients trusting stale cached data — distinct "
            "from unrelated factors like signature algorithm or Certificate Transparency."
        ),
    },

    # ── 1.4 Cryptographic hardware ───────────────────────────────────────────
    {
        "id": "nd1b-027",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Cryptographic hardware",
        "stem": (
            "A smartphone's fingerprint-matching algorithm and biometric template storage "
            "run entirely within an isolated co-processor separate from the main "
            "operating system, so that even if the OS is fully compromised by malware, the "
            "biometric template itself cannot be extracted. Which technology is this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Secure Enclave",
                "correct": True,
                "rationale": (
                    "Correct. A Secure Enclave is an isolated processor environment within "
                    "a device specifically used to protect sensitive operations like "
                    "biometric matching and storage from a compromised main OS."
                ),
            },
            {
                "id": "b",
                "text": "Trusted Platform Module (TPM)",
                "correct": False,
                "rationale": (
                    "Incorrect. A TPM is typically a discrete chip found on laptop/desktop "
                    "motherboards used for boot integrity measurement and key sealing; "
                    "mobile devices isolate biometric processing using a Secure Enclave-"
                    "style co-processor, not the TPM specification."
                ),
            },
            {
                "id": "c",
                "text": "Hardware Security Module (HSM)",
                "correct": False,
                "rationale": (
                    "Incorrect. An HSM is an appliance-scale device for centralized, "
                    "high-volume cryptographic operations; it is not the embedded, on-"
                    "device co-processor that isolates a single phone's biometric matching."
                ),
            },
            {
                "id": "d",
                "text": "Key Management System (KMS)",
                "correct": False,
                "rationale": (
                    "Incorrect. A KMS is a centralized software service for managing key "
                    "lifecycle across an organization; it is not an isolated hardware "
                    "co-processor embedded within a single mobile device."
                ),
            },
        ],
        "explanation": (
            "A Secure Enclave is a device-embedded isolated processor protecting sensitive "
            "operations like biometrics from a compromised OS — distinct from a "
            "motherboard TPM, appliance-scale HSM, or software-based KMS."
        ),
    },
    {
        "id": "nd1b-028",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Cryptographic hardware",
        "stem": (
            "An enterprise needs a centralized cryptographic appliance capable of tens of "
            "thousands of RSA signing operations per second for its certificate authority, "
            "which can be clustered with identical appliances for high availability and "
            "logically partitioned so several business units can isolate their own keys "
            "within the same physical device. Which technology BEST meets this requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Hardware Security Module (HSM)",
                "correct": True,
                "rationale": (
                    "Correct. Enterprise HSMs are appliance-grade devices built for "
                    "high-volume signing throughput, clustering for high availability, and "
                    "logical partitioning to isolate multiple tenants' keys."
                ),
            },
            {
                "id": "b",
                "text": "Trusted Platform Module (TPM)",
                "correct": False,
                "rationale": (
                    "Incorrect. A TPM is a low-throughput chip built into a single "
                    "endpoint's motherboard for local boot integrity and key sealing; it "
                    "cannot cluster or support the tens-of-thousands-per-second signing "
                    "volume described."
                ),
            },
            {
                "id": "c",
                "text": "Secure Enclave",
                "correct": False,
                "rationale": (
                    "Incorrect. Secure Enclave technology isolates operations within a "
                    "single device's own processor; it is not deployed as a clustered, "
                    "multi-tenant enterprise appliance for CA-scale signing operations."
                ),
            },
            {
                "id": "d",
                "text": "Software-based key vault",
                "correct": False,
                "rationale": (
                    "Incorrect. A software-only vault lacks the dedicated hardware "
                    "cryptographic acceleration and appliance-grade partitioning needed for "
                    "this signing volume and multi-tenant isolation requirement."
                ),
            },
        ],
        "explanation": (
            "HSMs are purpose-built for high-throughput, clustered, multi-tenant "
            "cryptographic operations at enterprise CA scale — distinct from TPMs, Secure "
            "Enclaves, and software-only key vaults."
        ),
    },

    # ── 1.4 Cryptographic hardware and key-management tools ─────────────────
    {
        "id": "nd1b-029",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Cryptographic hardware and key-management tools",
        "stem": (
            "A DevOps team wants application services to retrieve decryption keys at "
            "runtime through API calls, with every key request automatically logged, keys "
            "automatically rotated every 90 days without developer involvement, and the "
            "ability to instantly revoke a compromised key across all consuming services. "
            "Which solution BEST satisfies these requirements?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Key Management System (KMS)",
                "correct": True,
                "rationale": (
                    "Correct. A KMS provides API-based key retrieval, automated rotation "
                    "scheduling, audit logging of every key request, and centralized "
                    "revocation across all consuming applications."
                ),
            },
            {
                "id": "b",
                "text": "Hardware Security Module (HSM)",
                "correct": False,
                "rationale": (
                    "Incorrect. While a KMS may use an HSM underneath for physical key "
                    "storage, the described lifecycle functions — API retrieval, scheduled "
                    "rotation, logging, and revocation — are the defining functions of the "
                    "KMS layer, not the HSM hardware itself."
                ),
            },
            {
                "id": "c",
                "text": "Trusted Platform Module (TPM)",
                "correct": False,
                "rationale": (
                    "Incorrect. A TPM seals keys to a single endpoint's motherboard for "
                    "local boot integrity; it does not provide API-based key retrieval "
                    "across multiple distributed application services."
                ),
            },
            {
                "id": "d",
                "text": "Certificate Authority (CA)",
                "correct": False,
                "rationale": (
                    "Incorrect. A CA issues and signs digital certificates; it does not "
                    "provide the generic runtime key-retrieval, rotation, and revocation "
                    "service described for application-level decryption keys."
                ),
            },
        ],
        "explanation": (
            "A KMS is defined by its key-lifecycle management capabilities — API "
            "retrieval, rotation, logging, and revocation — distinct from the underlying "
            "HSM hardware, a device-bound TPM, or a certificate-issuing CA."
        ),
    },
    {
        "id": "nd1b-030",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Cryptographic hardware and key-management tools",
        "stem": (
            "An organization is designing the key-management architecture for a new PKI "
            "deployment. Which TWO of the following are core responsibilities that a Key "
            "Management System (KMS) is specifically expected to provide? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Automated key rotation on a defined schedule",
                "correct": True,
                "rationale": (
                    "Correct. Scheduling and automatically executing key rotation is a "
                    "core, defining lifecycle-management function of a KMS."
                ),
            },
            {
                "id": "b",
                "text": "Centralized audit logging of key usage and access requests",
                "correct": True,
                "rationale": (
                    "Correct. Logging every key access and usage event for audit purposes "
                    "is a core KMS responsibility, supporting compliance and forensics."
                ),
            },
            {
                "id": "c",
                "text": "Physically tamper-responsive zeroization circuitry",
                "correct": False,
                "rationale": (
                    "Incorrect. Tamper-responsive zeroization is a physical hardware "
                    "characteristic of devices like HSMs, not a function the KMS software "
                    "management layer itself provides."
                ),
            },
            {
                "id": "d",
                "text": "Boot-time firmware and OS integrity measurement",
                "correct": False,
                "rationale": (
                    "Incorrect. Measuring boot-time firmware/OS integrity is the specific "
                    "role of a TPM on an individual endpoint, not a responsibility of an "
                    "organization-wide KMS."
                ),
            },
            {
                "id": "e",
                "text": "Issuing X.509 identity certificates to end users",
                "correct": False,
                "rationale": (
                    "Incorrect. Issuing and signing X.509 certificates is the role of a "
                    "Certificate Authority, a distinct PKI component from the key-lifecycle "
                    "management functions of a KMS."
                ),
            },
        ],
        "explanation": (
            "A KMS's core responsibilities are software-layer key-lifecycle functions — "
            "rotation and audit logging — distinct from the physical tamper-response of an "
            "HSM, the boot-measurement role of a TPM, and the certificate-issuance role of "
            "a CA."
        ),
    },

    # ── 1.4 Hashing and salting ───────────────────────────────────────────────
    {
        "id": "nd1b-031",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Hashing and salting",
        "stem": (
            "Two malware samples submitted to a sandbox differ in their binary content by "
            "only a single byte, yet their computed SHA-256 hash values are completely "
            "different, sharing no discernible pattern. Which property of cryptographic "
            "hash functions is demonstrated?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Avalanche effect",
                "correct": True,
                "rationale": (
                    "Correct. The avalanche effect means even a tiny change in input "
                    "(here, a single byte) produces a drastically different, unrelated "
                    "output hash — exactly what is observed."
                ),
            },
            {
                "id": "b",
                "text": "Determinism",
                "correct": False,
                "rationale": (
                    "Incorrect. Determinism means the SAME input always produces the SAME "
                    "output; it describes consistency for identical inputs, not the large "
                    "output difference caused by a small input change."
                ),
            },
            {
                "id": "c",
                "text": "Collision resistance",
                "correct": False,
                "rationale": (
                    "Incorrect. Collision resistance means it is computationally infeasible "
                    "to find two DIFFERENT inputs that produce the SAME hash output; this "
                    "scenario shows two different inputs correctly producing different "
                    "outputs, which does not test collision resistance."
                ),
            },
            {
                "id": "d",
                "text": "Pre-image resistance",
                "correct": False,
                "rationale": (
                    "Incorrect. Pre-image resistance means it is infeasible to reverse a "
                    "hash to recover its original input; this scenario is about forward "
                    "hashing behavior of two known inputs, not reversing a hash."
                ),
            },
        ],
        "explanation": (
            "The avalanche effect ensures small input changes cause large, unpredictable "
            "output changes — distinct from determinism (same input, same output), "
            "collision resistance, and pre-image resistance."
        ),
    },
    {
        "id": "nd1b-032",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Hashing and salting",
        "stem": (
            "A legacy authentication system stores password hashes using a single, static "
            "salt value hardcoded directly in the application's source code and shared by "
            "every user account. Why does this design fail to deliver the security benefit "
            "normally expected from salting?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Identical passwords still produce identical hashes across all users, and an attacker who obtains the hardcoded salt can build a rainbow table specific to it",
                "correct": True,
                "rationale": (
                    "Correct. Salting's benefit depends on each user having a unique, "
                    "unpredictable salt; a single shared salt means identical passwords "
                    "still collide, and once the salt is known (e.g., via source code "
                    "leakage or decompilation), an attacker can precompute a targeted "
                    "rainbow table for it."
                ),
            },
            {
                "id": "b",
                "text": "It is still fully effective because attackers can never discover the salt value",
                "correct": False,
                "rationale": (
                    "Incorrect. A salt hardcoded in application source code is not secret "
                    "and can readily be discovered through code review, decompilation, or "
                    "leakage, undermining this assumption."
                ),
            },
            {
                "id": "c",
                "text": "It provides equivalent protection to unique per-user random salting as long as the hash algorithm is strong",
                "correct": False,
                "rationale": (
                    "Incorrect. No matter how strong the underlying hash algorithm is, a "
                    "shared static salt still allows identical passwords to produce "
                    "identical hashes and enables a salt-specific precomputed attack, which "
                    "unique per-user salting specifically prevents."
                ),
            },
            {
                "id": "d",
                "text": "It only weakens protection against online brute-force attacks, not offline attacks",
                "correct": False,
                "rationale": (
                    "Incorrect. A shared static salt primarily weakens protection against "
                    "offline attacks, such as precomputed rainbow tables against a stolen "
                    "hash dump, which is the opposite of what this option claims."
                ),
            },
        ],
        "explanation": (
            "Salting only delivers its intended benefit when each user's salt is unique "
            "and unpredictable; a single hardcoded, shared salt collapses back into "
            "effectively unsalted hashing once the salt value is discovered."
        ),
    },

    # ── 1.4 Obfuscation techniques ────────────────────────────────────────────
    {
        "id": "nd1b-033",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Obfuscation techniques",
        "stem": (
            "A software vendor's build process renames all internal function and variable "
            "names in a compiled mobile app to meaningless strings such as \"a1b2\" and "
            "inserts redundant dead-code branches, specifically to make it harder for "
            "anyone to reverse-engineer the app's logic. Which technique is this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Code obfuscation",
                "correct": True,
                "rationale": (
                    "Correct. Code obfuscation deliberately alters code structure — such as "
                    "meaningless naming and dead-code insertion — to make reverse "
                    "engineering more difficult while preserving functional behavior."
                ),
            },
            {
                "id": "b",
                "text": "Tokenization",
                "correct": False,
                "rationale": (
                    "Incorrect. Tokenization replaces sensitive data values with "
                    "non-sensitive surrogate tokens tracked in a vault; it does not describe "
                    "altering a program's internal code structure."
                ),
            },
            {
                "id": "c",
                "text": "Steganography",
                "correct": False,
                "rationale": (
                    "Incorrect. Steganography hides data within an unrelated carrier file, "
                    "such as an image; it does not describe renaming functions or inserting "
                    "dead code within a program's own source."
                ),
            },
            {
                "id": "d",
                "text": "Encryption",
                "correct": False,
                "rationale": (
                    "Incorrect. Encryption transforms data into ciphertext requiring a key "
                    "to reverse; obfuscated code remains directly executable without any "
                    "decryption key, which distinguishes it from encryption."
                ),
            },
        ],
        "explanation": (
            "Code obfuscation intentionally makes source or compiled code difficult to "
            "understand while preserving its functionality — distinct from tokenization, "
            "steganography, and encryption."
        ),
    },
    {
        "id": "nd1b-034",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Obfuscation techniques",
        "stem": (
            "A QA team needs a non-production copy of the customer database for load "
            "testing. Which TWO characteristics MUST the resulting dataset have to satisfy "
            "proper data masking for this use case? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Masked values retain a realistic format and data type so applications continue to function correctly during testing",
                "correct": True,
                "rationale": (
                    "Correct. Effective masking preserves the format and type of the "
                    "original data (e.g., valid-looking account numbers) so the application "
                    "under test continues to behave realistically."
                ),
            },
            {
                "id": "b",
                "text": "The masked values cannot be reversed to recover the original sensitive data",
                "correct": True,
                "rationale": (
                    "Correct. Proper data masking is a one-way transformation; unlike "
                    "tokenization, there is no vault or key that allows recovering the "
                    "original values from the masked dataset."
                ),
            },
            {
                "id": "c",
                "text": "Masked values are retrievable from a secure vault mapping table when the original is needed",
                "correct": False,
                "rationale": (
                    "Incorrect. Retrieval via a secure vault mapping table describes "
                    "tokenization, not masking; masking is intended to be one-way and "
                    "irreversible for non-production use."
                ),
            },
            {
                "id": "d",
                "text": "Masking must use a shared encryption key retained by the QA team for future decryption",
                "correct": False,
                "rationale": (
                    "Incorrect. Requiring a retained decryption key contradicts the "
                    "intended irreversibility of masking and instead describes encryption, "
                    "which is a different, reversible technique."
                ),
            },
            {
                "id": "e",
                "text": "Each masked field must use a unique cryptographic salt, as in password hashing",
                "correct": False,
                "rationale": (
                    "Incorrect. Per-record salting is a technique specific to password "
                    "hashing to defeat rainbow tables; it is not a requirement for producing "
                    "realistic, irreversible masked test data."
                ),
            },
        ],
        "explanation": (
            "Data masking for non-production testing must preserve realistic format while "
            "remaining irreversible — distinct from tokenization's vault-based "
            "reversibility, encryption's key-based reversibility, and password salting."
        ),
    },

    # ── 1.4 Symmetric vs asymmetric encryption ───────────────────────────────
    {
        "id": "nd1b-035",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Symmetric vs asymmetric encryption",
        "stem": (
            "A messaging application must let User A send an encrypted message that only "
            "User B can decrypt, even though A and B have never previously exchanged any "
            "shared secret over any channel. Which type of encryption SHOULD be used to "
            "encrypt this message?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Asymmetric encryption using User B's public key",
                "correct": True,
                "rationale": (
                    "Correct. Asymmetric encryption allows anyone to encrypt data using the "
                    "recipient's publicly available key, such that only the holder of the "
                    "corresponding private key can decrypt it — requiring no prior shared "
                    "secret."
                ),
            },
            {
                "id": "b",
                "text": "Symmetric encryption with a pre-shared key",
                "correct": False,
                "rationale": (
                    "Incorrect. Symmetric encryption requires both parties to already "
                    "possess the same secret key; the scenario explicitly states no shared "
                    "secret has ever been exchanged."
                ),
            },
            {
                "id": "c",
                "text": "Hashing the message with SHA-256",
                "correct": False,
                "rationale": (
                    "Incorrect. Hashing is a one-way function that provides integrity "
                    "verification, not confidentiality; it cannot be reversed to recover "
                    "the original message and therefore cannot be used to send an "
                    "encrypted, decryptable message."
                ),
            },
            {
                "id": "d",
                "text": "HMAC with a shared secret key",
                "correct": False,
                "rationale": (
                    "Incorrect. HMAC provides message authentication and integrity, not "
                    "confidentiality, and also requires a pre-shared secret key that the "
                    "scenario states does not exist."
                ),
            },
        ],
        "explanation": (
            "Asymmetric encryption uniquely allows confidential communication without any "
            "prior shared secret, using the recipient's public key — distinct from "
            "symmetric encryption (requires a pre-shared key) and hashing/HMAC (no "
            "confidentiality)."
        ),
    },
    {
        "id": "nd1b-036",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Symmetric vs asymmetric encryption",
        "stem": (
            "A file-sharing service encrypts each uploaded file with a freshly generated "
            "AES-256 key unique to that file, then encrypts that AES key itself using the "
            "recipient's RSA public key before storing both the encrypted file and the "
            "encrypted key together. Which term BEST describes this overall design?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Hybrid (envelope) encryption",
                "correct": True,
                "rationale": (
                    "Correct. Hybrid encryption combines fast symmetric encryption for the "
                    "bulk data (AES) with asymmetric encryption used only to protect the "
                    "much smaller symmetric key (RSA) — exactly the design described."
                ),
            },
            {
                "id": "b",
                "text": "Pure asymmetric encryption",
                "correct": False,
                "rationale": (
                    "Incorrect. The bulk file itself is encrypted with AES, a symmetric "
                    "algorithm; RSA is used only to wrap the much smaller AES key, so this "
                    "is not purely asymmetric encryption of the file."
                ),
            },
            {
                "id": "c",
                "text": "Pure symmetric encryption",
                "correct": False,
                "rationale": (
                    "Incorrect. RSA, an asymmetric algorithm, is used to protect the AES "
                    "key itself, so the design is not purely symmetric."
                ),
            },
            {
                "id": "d",
                "text": "Key stretching",
                "correct": False,
                "rationale": (
                    "Incorrect. Key stretching (e.g., PBKDF2, bcrypt) strengthens a "
                    "low-entropy password/key against brute-force attacks; it is unrelated "
                    "to combining symmetric bulk encryption with asymmetric key wrapping."
                ),
            },
        ],
        "explanation": (
            "Hybrid (envelope) encryption uses symmetric encryption for efficient bulk "
            "data protection and asymmetric encryption to securely wrap the small "
            "symmetric key — distinct from pure symmetric, pure asymmetric, or key "
            "stretching."
        ),
    },
]

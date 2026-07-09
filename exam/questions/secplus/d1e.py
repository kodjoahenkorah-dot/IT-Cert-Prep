"""
CompTIA Security+ (SY0-701) Domain 1: General Security Concepts — Set E
34 exam-quality questions covering objectives 1.1 through 1.4.
"""

QUESTIONS = [
    # ── 1.1 Security control categories / types ─────────────────────────────
    {
        "id": "nd1e-001",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security control categories",
        "stem": (
            "A university's endpoint protection platform automatically quarantines any "
            "workstation the moment it detects a process behaving like ransomware, killing "
            "network connectivity to that host without any analyst involvement. Which "
            "security control CATEGORY does this automated quarantine represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Technical",
                "correct": True,
                "rationale": (
                    "Correct. The quarantine is enforced entirely through software logic "
                    "running on the endpoint agent, with no human decision in the loop — "
                    "the defining trait of a technical (logical) control."
                ),
            },
            {
                "id": "b",
                "text": "Managerial",
                "correct": False,
                "rationale": (
                    "Incorrect. Managerial controls are governance decisions, such as the "
                    "policy mandating endpoint protection be deployed campus-wide, not the "
                    "software's automated enforcement action itself."
                ),
            },
            {
                "id": "c",
                "text": "Operational",
                "correct": False,
                "rationale": (
                    "Incorrect. Operational controls are carried out by people performing "
                    "day-to-day tasks, such as an analyst manually isolating a host; here the "
                    "isolation happens automatically with no human step."
                ),
            },
            {
                "id": "d",
                "text": "Physical",
                "correct": False,
                "rationale": (
                    "Incorrect. Physical controls protect tangible assets and spaces (locks, "
                    "badges, fencing). Killing a host's network access is a logical action, "
                    "not a physical one."
                ),
            },
        ],
        "explanation": (
            "Control category answers HOW a control is carried out. Software that "
            "automatically enforces a rule — here, isolating a ransomware-infected host — is "
            "a technical control, distinct from the managerial policy behind it or an "
            "operational process a human would perform manually."
        ),
    },
    {
        "id": "nd1e-002",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Security control categories",
        "stem": (
            "A newly hired CISO drafts and gets executive sign-off on a formal information "
            "security policy that sets the organization's overall risk appetite and assigns "
            "accountability for each control domain to named executives. Which control "
            "CATEGORY does this policy document represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Managerial",
                "correct": True,
                "rationale": (
                    "Correct. Managerial (administrative) controls consist of governance "
                    "activities — policies, standards, and risk-appetite decisions made by "
                    "leadership — exactly what this signed policy establishes."
                ),
            },
            {
                "id": "b",
                "text": "Operational",
                "correct": False,
                "rationale": (
                    "Incorrect. Operational controls are the routine procedures staff "
                    "perform daily (e.g., patch cycles). Setting enterprise risk appetite and "
                    "executive accountability is a governance decision, not a routine task."
                ),
            },
            {
                "id": "c",
                "text": "Technical",
                "correct": False,
                "rationale": (
                    "Incorrect. Technical controls are enforced through technology (firewalls, "
                    "encryption). A signed governance policy contains no technological "
                    "enforcement mechanism."
                ),
            },
            {
                "id": "d",
                "text": "Physical",
                "correct": False,
                "rationale": (
                    "Incorrect. Physical controls protect tangible assets. This policy is a "
                    "governance document with no physical protection component."
                ),
            },
        ],
        "explanation": (
            "Executive-approved policies that establish risk appetite and accountability are "
            "managerial controls — strategic governance decisions, distinct from the "
            "operational procedures or technical mechanisms used to carry them out."
        ),
    },
    {
        "id": "nd1e-003",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security control types",
        "stem": (
            "After a data-exfiltration incident, a manufacturer configures its DLP platform "
            "to automatically block any outbound email containing a pattern matching a "
            "credit card number, stopping the message before it leaves the mail gateway. "
            "Which control TYPE does this DLP rule BEST represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Preventive",
                "correct": True,
                "rationale": (
                    "Correct. Blocking the message before it ever leaves the organization "
                    "stops the incident from occurring at all, which is the definition of a "
                    "preventive control."
                ),
            },
            {
                "id": "b",
                "text": "Detective",
                "correct": False,
                "rationale": (
                    "Incorrect. A detective control would identify and log a violation after "
                    "it happened; here the email never leaves, so nothing is merely detected "
                    "— it is actively stopped."
                ),
            },
            {
                "id": "c",
                "text": "Corrective",
                "correct": False,
                "rationale": (
                    "Incorrect. Corrective controls remediate damage after an incident has "
                    "occurred. Blocking the outbound message prevents the incident, so there "
                    "is nothing left to correct."
                ),
            },
            {
                "id": "d",
                "text": "Compensating",
                "correct": False,
                "rationale": (
                    "Incorrect. A compensating control substitutes for a primary control that "
                    "cannot be implemented. This DLP rule is the primary control itself, not "
                    "a substitute."
                ),
            },
        ],
        "explanation": (
            "Control type describes WHEN/HOW a control acts relative to an event. Stopping "
            "the sensitive data from leaving the network before transmission completes is "
            "preventive, not merely detective or corrective."
        ),
    },
    {
        "id": "nd1e-004",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Security control types",
        "stem": (
            "A theme park's cybersecurity team requires that, if ransomware ever encrypts a "
            "kiosk's local drive, the affected kiosk automatically reimages itself from a "
            "known-good golden snapshot stored on an isolated management VLAN, and that this "
            "event is logged for the after-action review board. Which TWO control TYPES does "
            "this automated reimaging process BEST represent? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Corrective",
                "correct": True,
                "rationale": (
                    "Correct. Reimaging the kiosk from a known-good snapshot restores the "
                    "system to a working state after the incident, which is the definition of "
                    "a corrective control."
                ),
            },
            {
                "id": "b",
                "text": "Detective",
                "correct": True,
                "rationale": (
                    "Correct. The event must first be logged and identified for the "
                    "after-action review board to examine, which is a detective function "
                    "occurring alongside the remediation."
                ),
            },
            {
                "id": "c",
                "text": "Preventive",
                "correct": False,
                "rationale": (
                    "Incorrect. The ransomware already encrypted the drive before reimaging "
                    "began; nothing stopped the initial compromise, so this is not preventive."
                ),
            },
            {
                "id": "d",
                "text": "Deterrent",
                "correct": False,
                "rationale": (
                    "Incorrect. Nothing about an automated reimaging response discourages an "
                    "attacker from attempting the attack in the first place."
                ),
            },
            {
                "id": "e",
                "text": "Compensating",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no indication a primary control was infeasible and "
                    "being substituted; reimaging is a direct corrective response to the "
                    "ransomware event."
                ),
            },
        ],
        "explanation": (
            "A single response can satisfy multiple control types. Automatically restoring "
            "a kiosk after encryption is corrective, while logging the event for review is "
            "detective — but neither preventive nor deterrent, since the compromise already "
            "occurred."
        ),
    },
    # ── 1.1 Security control categories and types ───────────────────────────
    {
        "id": "nd1e-005",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Security control categories and types",
        "stem": (
            "A pharmaceutical company cannot immediately patch a legacy SCADA controller "
            "that lacks vendor support, so it instead places the controller behind a "
            "dedicated firewall that permits traffic only from one engineering workstation "
            "and logs every session for daily manual review by the OT security team. Which "
            "control CATEGORY and TYPE BEST describes this firewall segmentation?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Technical, compensating",
                "correct": True,
                "rationale": (
                    "Correct. The firewall is enforced through technology (technical), and "
                    "because it substitutes for the patching that cannot be applied to the "
                    "unsupported controller, it functions as a compensating control."
                ),
            },
            {
                "id": "b",
                "text": "Technical, preventive",
                "correct": False,
                "rationale": (
                    "Incorrect. While the firewall is technical, calling it purely preventive "
                    "ignores that its specific purpose is to stand in for the missing patch — "
                    "the defining trait of a compensating control in this exact scenario."
                ),
            },
            {
                "id": "c",
                "text": "Operational, compensating",
                "correct": False,
                "rationale": (
                    "Incorrect. The firewall itself is a piece of technology enforcing rules "
                    "automatically; it is a technical control. The daily manual log review is "
                    "operational, but that is not what is being assessed here."
                ),
            },
            {
                "id": "d",
                "text": "Managerial, compensating",
                "correct": False,
                "rationale": (
                    "Incorrect. Managerial controls are governance/policy decisions. Deploying "
                    "and configuring an actual firewall appliance is a technical action, not a "
                    "governance one."
                ),
            },
        ],
        "explanation": (
            "The firewall enforces restriction automatically (technical) and exists "
            "specifically because the preferred control — patching — cannot be applied, "
            "making it compensating rather than simply preventive."
        ),
    },
    {
        "id": "nd1e-006",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security control categories and types",
        "stem": (
            "An airport requires every ground-crew vehicle to pass through a raised steel "
            "wedge barrier embedded in the tarmac that physically prevents entry onto the "
            "runway apron unless a valid RFID credential lowers it. Which control CATEGORY "
            "and TYPE BEST describes this wedge barrier?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Physical, preventive",
                "correct": True,
                "rationale": (
                    "Correct. The barrier is a tangible physical device that stops "
                    "unauthorized vehicles from entering before an incident can occur, "
                    "making it both a physical control and preventive in type."
                ),
            },
            {
                "id": "b",
                "text": "Physical, detective",
                "correct": False,
                "rationale": (
                    "Incorrect. A detective control would record or alert on an entry attempt "
                    "after the fact; this barrier physically blocks the vehicle from entering "
                    "at all, which is preventive."
                ),
            },
            {
                "id": "c",
                "text": "Technical, preventive",
                "correct": False,
                "rationale": (
                    "Incorrect. Although RFID logic controls the barrier, the control itself "
                    "is a physical, tangible barrier stopping vehicle movement — its category "
                    "is physical, not technical."
                ),
            },
            {
                "id": "d",
                "text": "Physical, deterrent",
                "correct": False,
                "rationale": (
                    "Incorrect. A deterrent only discourages; it does not physically stop "
                    "movement. Because the wedge barrier actually blocks the vehicle, it is "
                    "preventive rather than merely deterrent."
                ),
            },
        ],
        "explanation": (
            "Raised barriers, bollards, and mantraps are tangible obstacles that physically "
            "stop unauthorized access before it happens, making them physical, preventive "
            "controls."
        ),
    },
    # ── 1.2 AAA framework ─────────────────────────────────────────────────
    {
        "id": "nd1e-007",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "AAA framework",
        "stem": (
            "A university's wireless network requires students to enter their campus "
            "credentials at login, after which the RADIUS server assigns the device to a "
            "VLAN corresponding to the student's declared major, and every session's start "
            "time, IP address, and data volume is written to a billing-reconciliation log. "
            "Which AAA element does the VLAN assignment by declared major represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Authorization",
                "correct": True,
                "rationale": (
                    "Correct. Determining which network resources (VLAN) an already-"
                    "authenticated student may use is the definition of authorization — "
                    "granting the appropriate level of access."
                ),
            },
            {
                "id": "b",
                "text": "Authentication",
                "correct": False,
                "rationale": (
                    "Incorrect. Authentication is verifying the student's identity via "
                    "credentials, which already occurred before the VLAN was assigned."
                ),
            },
            {
                "id": "c",
                "text": "Accounting",
                "correct": False,
                "rationale": (
                    "Incorrect. Accounting is the logging of session data (start time, IP, "
                    "volume) for the billing log — a separate step from deciding which VLAN "
                    "to place the student on."
                ),
            },
            {
                "id": "d",
                "text": "Identification",
                "correct": False,
                "rationale": (
                    "Incorrect. Identification is the initial claim of identity (e.g., "
                    "presenting a username), which precedes both authentication and "
                    "authorization and is not what determines VLAN placement."
                ),
            },
        ],
        "explanation": (
            "The AAA framework separates authentication (proving identity), authorization "
            "(granting appropriate access after identity is confirmed), and accounting "
            "(logging usage). Assigning network access based on attributes is authorization."
        ),
    },
    {
        "id": "nd1e-008",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "AAA framework",
        "stem": (
            "A managed security provider is choosing between RADIUS and TACACS+ to "
            "centralize authentication, authorization, and accounting for administrative "
            "access to hundreds of client routers and switches. Which TWO statements "
            "correctly distinguish TACACS+ from RADIUS in this use case? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "TACACS+ encrypts the entire packet payload, while RADIUS encrypts only the password field.",
                "correct": True,
                "rationale": (
                    "Correct. TACACS+ encrypts the full body of each packet in transit, "
                    "whereas RADIUS by default encrypts only the password attribute, leaving "
                    "other data such as usernames visible."
                ),
            },
            {
                "id": "b",
                "text": "TACACS+ separates authentication, authorization, and accounting into distinct processes, while RADIUS combines authentication and authorization.",
                "correct": True,
                "rationale": (
                    "Correct. TACACS+ treats AAA as three separable processes, enabling "
                    "granular per-command authorization for device administration; RADIUS "
                    "combines authentication and authorization into a single response."
                ),
            },
            {
                "id": "c",
                "text": "TACACS+ uses UDP for transport, while RADIUS uses TCP.",
                "correct": False,
                "rationale": (
                    "Incorrect. This is reversed — TACACS+ uses TCP (typically port 49) for "
                    "reliable delivery, while RADIUS uses UDP."
                ),
            },
            {
                "id": "d",
                "text": "TACACS+ is primarily used for authenticating end-user Wi-Fi clients, while RADIUS is reserved exclusively for administrative device logins.",
                "correct": False,
                "rationale": (
                    "Incorrect. This reverses the typical use cases — TACACS+ is favored for "
                    "granular, command-level administrative access to network devices, while "
                    "RADIUS is the common choice for end-user network/VPN/Wi-Fi "
                    "authentication."
                ),
            },
            {
                "id": "e",
                "text": "RADIUS provides granular, per-command authorization on network devices, which TACACS+ cannot do.",
                "correct": False,
                "rationale": (
                    "Incorrect. This is backwards — TACACS+ is well known for granular, "
                    "per-command authorization on infrastructure devices, a capability RADIUS "
                    "does not natively provide."
                ),
            },
        ],
        "explanation": (
            "Key TACACS+ vs. RADIUS distinctions for centralized device administration: "
            "TACACS+ encrypts the full packet body over TCP and separates AAA into distinct "
            "processes, enabling granular per-command authorization; RADIUS encrypts only "
            "the password over UDP and combines authentication with authorization, and is "
            "better suited to end-user network access scenarios."
        ),
    },
    # ── 1.2 Attack type identification ───────────────────────────────────
    {
        "id": "nd1e-009",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Attack type identification",
        "stem": (
            "A property management company's help desk receives a phone call from someone "
            "claiming to be the regional facilities director, urgently requesting a password "
            "reset for a building-access portal account because he is 'locked out during an "
            "active fire-alarm test.' The caller knows the director's employee ID and correct "
            "office location. Which attack technique is BEST illustrated by this call?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Vishing",
                "correct": True,
                "rationale": (
                    "Correct. A voice-based phone call used to socially engineer a help-desk "
                    "employee into performing an unauthorized action, using urgency and "
                    "impersonation, is the defining characteristic of vishing."
                ),
            },
            {
                "id": "b",
                "text": "Pretexting",
                "correct": False,
                "rationale": (
                    "Incorrect. Pretexting is the fabricated scenario/persona used to justify "
                    "the request — accurately describing part of the attack — but the exam-"
                    "tested term for the phone-call delivery mechanism itself is vishing."
                ),
            },
            {
                "id": "c",
                "text": "Smishing",
                "correct": False,
                "rationale": (
                    "Incorrect. Smishing is phishing conducted via SMS text message; this "
                    "attack was delivered through a live voice phone call, not a text."
                ),
            },
            {
                "id": "d",
                "text": "Whaling",
                "correct": False,
                "rationale": (
                    "Incorrect. Whaling specifically targets senior executives (e.g., a CEO) "
                    "as the victim of the attack. Here, the help-desk agent is the victim being "
                    "manipulated, not an executive."
                ),
            },
        ],
        "explanation": (
            "Vishing is voice-based social engineering. While the caller also used a "
            "pretext, the SY0-701 exam distinguishes vishing (the phone-call vector) from "
            "smishing (SMS) and whaling (executive-targeted phishing)."
        ),
    },
    {
        "id": "nd1e-010",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Attack type identification",
        "stem": (
            "Security analysts discover that an attacker registered dozens of domain names "
            "differing from the company's real domain by a single transposed or substituted "
            "character (e.g., 'examp1e.com' instead of 'example.com') and used them to host "
            "near-identical copies of the company's login page. Which technique is BEST "
            "illustrated by the domain registrations themselves?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Typosquatting",
                "correct": True,
                "rationale": (
                    "Correct. Registering domains that closely resemble a legitimate domain "
                    "through character substitution or transposition, intended to catch users "
                    "who mistype the real address, is the definition of typosquatting."
                ),
            },
            {
                "id": "b",
                "text": "Domain hijacking",
                "correct": False,
                "rationale": (
                    "Incorrect. Domain hijacking involves an attacker taking unauthorized "
                    "control of the victim's OWN legitimately registered domain; here, the "
                    "attacker registered separate, new lookalike domains instead."
                ),
            },
            {
                "id": "c",
                "text": "DNS poisoning",
                "correct": False,
                "rationale": (
                    "Incorrect. DNS poisoning corrupts cached resolver records to redirect "
                    "legitimate queries; nothing here indicates any resolver cache was "
                    "tampered with — the attacker simply registered new domains outright."
                ),
            },
            {
                "id": "d",
                "text": "Pharming",
                "correct": False,
                "rationale": (
                    "Incorrect. Pharming redirects traffic away from a legitimate site "
                    "without the victim's action, typically via DNS or hosts-file tampering. "
                    "This scenario relies on the victim actively mistyping a URL, not a "
                    "redirect mechanism."
                ),
            },
        ],
        "explanation": (
            "Registering lookalike domains that exploit common typing mistakes is "
            "typosquatting, distinct from domain hijacking (stealing the real domain), DNS "
            "poisoning (corrupting cache records), and pharming (silent redirection)."
        ),
    },
    # ── 1.2 CIA triad and non-repudiation ────────────────────────────────
    {
        "id": "nd1e-011",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "CIA triad and non-repudiation",
        "stem": (
            "A ride-sharing company's dispatch database is not breached, but a "
            "misconfigured load balancer begins silently dropping 40% of driver "
            "location-update packets during peak hours, causing the app to display stale, "
            "inaccurate driver positions to riders for two hours. Which element of the CIA "
            "triad is PRIMARILY impacted?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Integrity",
                "correct": True,
                "rationale": (
                    "Correct. The displayed location data no longer accurately reflects "
                    "reality because updates are silently lost, meaning the data's accuracy "
                    "and trustworthiness — integrity — is compromised, even though nothing "
                    "was maliciously altered."
                ),
            },
            {
                "id": "b",
                "text": "Confidentiality",
                "correct": False,
                "rationale": (
                    "Incorrect. No unauthorized party viewed or obtained data. The problem is "
                    "that the data shown is stale and inaccurate, not that it was disclosed."
                ),
            },
            {
                "id": "c",
                "text": "Availability",
                "correct": False,
                "rationale": (
                    "Incorrect. The app itself remains reachable and functional throughout — "
                    "riders can still open it and see (inaccurate) driver positions. The "
                    "service was not rendered unavailable."
                ),
            },
            {
                "id": "d",
                "text": "Non-repudiation",
                "correct": False,
                "rationale": (
                    "Incorrect. Non-repudiation concerns proving who performed an action so "
                    "they cannot deny it; dropped packets causing stale data have nothing to "
                    "do with attributing or disputing an action."
                ),
            },
        ],
        "explanation": (
            "Even without malicious intent, silently dropped or corrupted updates that "
            "cause displayed data to no longer reflect reality is an integrity failure — "
            "the data's accuracy and trustworthiness are what is impacted."
        ),
    },
    {
        "id": "nd1e-012",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "CIA triad and non-repudiation",
        "stem": (
            "A construction firm requires every subcontractor change order to be submitted "
            "through a portal that timestamps the submission, records the submitter's "
            "authenticated identity, and generates a cryptographic signature over the "
            "document using the submitter's individually issued private key, so the firm can "
            "later prove in arbitration exactly who submitted which change order. Which "
            "security concept does this portal design PRIMARILY provide?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Non-repudiation",
                "correct": True,
                "rationale": (
                    "Correct. Binding a document to an individually issued private-key "
                    "signature, tied to an authenticated identity and timestamp, prevents the "
                    "submitter from later denying they submitted it — the definition of "
                    "non-repudiation."
                ),
            },
            {
                "id": "b",
                "text": "Confidentiality",
                "correct": False,
                "rationale": (
                    "Incorrect. Confidentiality is about restricting who can read the "
                    "document's contents; nothing in the scenario describes encrypting the "
                    "change order to prevent unauthorized viewing."
                ),
            },
            {
                "id": "c",
                "text": "Availability",
                "correct": False,
                "rationale": (
                    "Incorrect. Availability concerns ensuring the portal and data remain "
                    "accessible when needed; the scenario's focus is proving authorship for "
                    "arbitration, not uptime."
                ),
            },
            {
                "id": "d",
                "text": "Obfuscation",
                "correct": False,
                "rationale": (
                    "Incorrect. Obfuscation deliberately makes data or code harder to "
                    "understand; digitally signing a change order for attribution is the "
                    "opposite goal of hiding meaning."
                ),
            },
        ],
        "explanation": (
            "A per-user digital signature tied to authenticated identity and timestamp "
            "exists specifically to prevent later denial of authorship — non-repudiation — "
            "which is distinct from the CIA triad's confidentiality, integrity, and "
            "availability properties."
        ),
    },
    # ── 1.2 Certificates ──────────────────────────────────────────────────
    {
        "id": "nd1e-013",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Certificates",
        "stem": (
            "An internal engineering wiki, accessible only from the corporate LAN, presents "
            "a TLS certificate that the browser flags as untrusted because the issuing CA is "
            "not in the public trust store, even though the certificate's subject name and "
            "expiration date are both valid. IT confirms the certificate was issued by the "
            "company's own internal PKI. What is the MOST appropriate way to resolve the "
            "browser warning for employee devices?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Distribute the internal root CA's certificate to employee devices via group policy so it is trusted enterprise-wide.",
                "correct": True,
                "rationale": (
                    "Correct. Pushing the internal CA's root certificate into each device's "
                    "trusted root store via centralized management lets devices validate the "
                    "chain properly without weakening security or bypassing warnings."
                ),
            },
            {
                "id": "b",
                "text": "Instruct employees to click through the browser's certificate warning each time they access the wiki.",
                "correct": False,
                "rationale": (
                    "Incorrect. Training users to routinely dismiss certificate warnings "
                    "trains them to ignore a control that also protects against real "
                    "man-in-the-middle attacks, creating a dangerous habit."
                ),
            },
            {
                "id": "c",
                "text": "Reconfigure the wiki server to serve traffic over plain HTTP instead of HTTPS.",
                "correct": False,
                "rationale": (
                    "Incorrect. Removing encryption entirely to avoid a certificate warning "
                    "eliminates confidentiality and integrity protection for the traffic, "
                    "trading one problem for a far worse one."
                ),
            },
            {
                "id": "d",
                "text": "Purchase a publicly trusted wildcard certificate for the internal wiki's hostname.",
                "correct": False,
                "rationale": (
                    "Incorrect. Public CAs will not issue certificates for internal, non-"
                    "publicly-resolvable hostnames, and doing so is unnecessary cost when the "
                    "organization already operates its own internal PKI for internal-only "
                    "resources."
                ),
            },
        ],
        "explanation": (
            "The correct fix for internally issued certificates is to distribute the "
            "internal CA's root certificate to managed devices so the chain of trust "
            "resolves properly, rather than training users to bypass warnings or removing "
            "encryption."
        ),
    },
    {
        "id": "nd1e-014",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Certificates",
        "stem": (
            "A retailer's e-commerce site is issued a new TLS certificate after its old one "
            "is compromised. The security team wants clients to be able to verify current "
            "revocation status of the compromised certificate WITHOUT requiring every client "
            "to make a real-time query to the CA at each connection. Which TWO approaches "
            "achieve this? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Enable OCSP stapling so the web server periodically fetches a signed revocation response and attaches it directly to the TLS handshake.",
                "correct": True,
                "rationale": (
                    "Correct. OCSP stapling shifts the OCSP query to the server, which caches "
                    "and attaches ('staples') a timestamped, signed revocation status to the "
                    "handshake, so clients get current status without querying the CA "
                    "themselves at every connection."
                ),
            },
            {
                "id": "b",
                "text": "Publish the certificate to a Certificate Revocation List (CRL) that clients can periodically download and cache.",
                "correct": True,
                "rationale": (
                    "Correct. A CRL is a periodically published, downloadable list of revoked "
                    "certificate serial numbers that clients can cache locally, avoiding a "
                    "live per-connection query to the CA."
                ),
            },
            {
                "id": "c",
                "text": "Require every client browser to query the CA's OCSP responder directly on each new TLS connection.",
                "correct": False,
                "rationale": (
                    "Incorrect. This is the exact live per-connection OCSP query model the "
                    "requirement explicitly seeks to avoid, and it also creates latency and "
                    "privacy concerns."
                ),
            },
            {
                "id": "d",
                "text": "Shorten the certificate's validity period to one hour so it expires before revocation status matters.",
                "correct": False,
                "rationale": (
                    "Incorrect. Extremely short validity periods are operationally impractical "
                    "for a public e-commerce site and do not actually communicate revocation "
                    "status to clients that already cached the certificate."
                ),
            },
            {
                "id": "e",
                "text": "Pin the compromised certificate's public key in the browser so future connections automatically trust it.",
                "correct": False,
                "rationale": (
                    "Incorrect. Pinning a compromised key would force clients to keep trusting "
                    "the very certificate that needs to be treated as revoked — the opposite "
                    "of the desired outcome."
                ),
            },
        ],
        "explanation": (
            "Both OCSP stapling and CRLs let clients learn revocation status without an "
            "unavoidable live per-connection query to the CA — stapling via a server-cached, "
            "signed response, and CRLs via a periodically downloaded, cached list."
        ),
    },
    # ── 1.2 Change management ────────────────────────────────────────────
    {
        "id": "nd1e-015",
        "domain": 1,
        "objective": "1.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Change management",
        "stem": (
            "A network engineer wants to submit a request for change to migrate a legacy "
            "VPN concentrator to a new appliance. The Change Advisory Board's template "
            "requires the engineer to specify what steps will be taken if the migration "
            "causes unexpected outages so service can be restored to the prior working "
            "state. Which change-management element is being requested?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Rollback plan",
                "correct": True,
                "rationale": (
                    "Correct. A rollback plan documents the specific steps to revert to the "
                    "last known-good configuration if a change causes unexpected problems — "
                    "exactly what is being requested here."
                ),
            },
            {
                "id": "b",
                "text": "Maintenance window",
                "correct": False,
                "rationale": (
                    "Incorrect. A maintenance window defines WHEN the change may be performed "
                    "to minimize business impact; it does not describe how to undo a failed "
                    "change."
                ),
            },
            {
                "id": "c",
                "text": "Impact analysis",
                "correct": False,
                "rationale": (
                    "Incorrect. Impact analysis assesses what systems and stakeholders would "
                    "be affected BY the change before it happens, not the steps to reverse it "
                    "if something goes wrong."
                ),
            },
            {
                "id": "d",
                "text": "Stakeholder analysis",
                "correct": False,
                "rationale": (
                    "Incorrect. Stakeholder analysis identifies who needs to approve or be "
                    "notified about the change; it has nothing to do with restoring service "
                    "after a failed implementation."
                ),
            },
        ],
        "explanation": (
            "The specific documentation of how to revert to the prior working state after a "
            "failed change is the rollback (backout) plan, a required element of a complete "
            "request for change."
        ),
    },
    {
        "id": "nd1e-016",
        "domain": 1,
        "objective": "1.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Change management",
        "stem": (
            "A retailer's e-commerce platform team wants to deploy an urgent code fix to "
            "stop an active checkout-page defacement, bypassing the standard two-week CAB "
            "review cycle. Which change-management process is MOST appropriate for this "
            "situation?"
        ),
        "options": [
            {
                "id": "a",
                "text": "An emergency change process with expedited approval and mandatory retrospective documentation",
                "correct": True,
                "rationale": (
                    "Correct. An emergency change process exists precisely for active, "
                    "business-impacting incidents, allowing expedited approval from a limited "
                    "set of authorized approvers while still requiring the change to be "
                    "documented and reviewed after the fact."
                ),
            },
            {
                "id": "b",
                "text": "A standard change following the full two-week CAB review cycle",
                "correct": False,
                "rationale": (
                    "Incorrect. Waiting two weeks while an active defacement continues to harm "
                    "customers and brand reputation is operationally unacceptable; the "
                    "standard cycle is for routine, non-urgent changes."
                ),
            },
            {
                "id": "c",
                "text": "Deploying the fix with no documentation since the situation is time-critical",
                "correct": False,
                "rationale": (
                    "Incorrect. Even emergency changes must be documented, typically through "
                    "retrospective review, to maintain an audit trail and allow lessons "
                    "learned to be captured; skipping documentation entirely is never "
                    "appropriate."
                ),
            },
            {
                "id": "d",
                "text": "A pre-approved standard change template used for routine, low-risk, recurring tasks",
                "correct": False,
                "rationale": (
                    "Incorrect. Pre-approved standard changes are reserved for well-understood, "
                    "repeatable, low-risk tasks (e.g., routine DNS updates), not for an "
                    "unplanned emergency response to an active security incident."
                ),
            },
        ],
        "explanation": (
            "Active, business-impacting incidents call for the emergency change process, "
            "which expedites approval while still requiring retrospective documentation — "
            "unlike standard changes (full CAB cycle) or pre-approved templates (routine, "
            "low-risk tasks)."
        ),
    },
    # ── 1.2 Deception and disruption technologies ────────────────────────
    {
        "id": "nd1e-017",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Deception and disruption technologies",
        "stem": (
            "A managed detection provider deploys an entire subnet of fake servers, fake "
            "workstations, and fake network shares that mimic a client's production "
            "environment in realistic detail, isolated from any real system, specifically to "
            "study attacker tools and techniques once they begin interacting with the "
            "environment. Which deception technology is BEST described?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Honeynet",
                "correct": True,
                "rationale": (
                    "Correct. A honeynet is a network of multiple interconnected decoy "
                    "systems (not just one host) designed to look like a real production "
                    "environment, used to observe attacker behavior across a broader, "
                    "realistic simulated network."
                ),
            },
            {
                "id": "b",
                "text": "Honeypot",
                "correct": False,
                "rationale": (
                    "Incorrect. A honeypot is a single decoy system. Here, an entire subnet of "
                    "multiple interconnected fake servers and workstations is described, which "
                    "is the broader honeynet concept."
                ),
            },
            {
                "id": "c",
                "text": "Honeyfile",
                "correct": False,
                "rationale": (
                    "Incorrect. A honeyfile is a single decoy document planted to detect "
                    "unauthorized access; this scenario describes decoy infrastructure at the "
                    "network level, not a document."
                ),
            },
            {
                "id": "d",
                "text": "DNS sinkhole",
                "correct": False,
                "rationale": (
                    "Incorrect. A DNS sinkhole redirects malicious domain lookups to a "
                    "controlled destination to disrupt malware communication; it does not "
                    "involve building an entire decoy network for attackers to explore."
                ),
            },
        ],
        "explanation": (
            "An entire simulated network of multiple decoy hosts is a honeynet, distinguished "
            "from a single decoy host (honeypot), a decoy document (honeyfile), or a "
            "disruption tool that redirects malicious DNS queries (sinkhole)."
        ),
    },
    # ── 1.2 Gap analysis ──────────────────────────────────────────────────
    {
        "id": "nd1e-018",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Gap analysis",
        "stem": (
            "An energy utility preparing to align with the NERC CIP standard documents each "
            "required control, identifies which ones the organization already satisfies "
            "through existing SCADA network segmentation and logging, and produces a "
            "prioritized list of unmet requirements along with estimated remediation cost "
            "for each. What is this activity BEST described as?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Gap analysis",
                "correct": True,
                "rationale": (
                    "Correct. Comparing current-state controls against a required framework's "
                    "controls, identifying what is already satisfied versus what is missing, "
                    "and prioritizing remediation is the definition of a gap analysis."
                ),
            },
            {
                "id": "b",
                "text": "Business impact analysis",
                "correct": False,
                "rationale": (
                    "Incorrect. A business impact analysis quantifies the operational and "
                    "financial impact of a disruption to specific processes (e.g., RTO/RPO), "
                    "not a comparison of current controls to a compliance framework."
                ),
            },
            {
                "id": "c",
                "text": "Vulnerability assessment",
                "correct": False,
                "rationale": (
                    "Incorrect. A vulnerability assessment scans systems for exploitable "
                    "technical weaknesses; this scenario is a broader comparison of control "
                    "coverage against a regulatory standard, not a technical scan."
                ),
            },
            {
                "id": "d",
                "text": "Penetration test",
                "correct": False,
                "rationale": (
                    "Incorrect. A penetration test actively attempts to exploit systems to "
                    "validate defenses; nothing here describes active exploitation, only a "
                    "documentation-based comparison against a standard."
                ),
            },
        ],
        "explanation": (
            "Systematically comparing current controls against a required standard's "
            "controls and identifying unmet requirements is a gap analysis, distinct from a "
            "BIA (impact of disruption), a vulnerability assessment (technical scanning), or "
            "a penetration test (active exploitation)."
        ),
    },
    {
        "id": "nd1e-019",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Gap analysis",
        "stem": (
            "During a gap analysis against the NIST Cybersecurity Framework, a security "
            "analyst finds that the organization already operates a fully implemented, "
            "well-tuned SIEM capable of satisfying the framework's 'Detect' function "
            "requirements, but has no documented procedure at all for the 'Respond' "
            "function's communication requirements. What should the analyst do with this "
            "finding?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Document the SIEM as satisfying the Detect requirement and add the missing Respond communication procedure to a prioritized remediation roadmap.",
                "correct": True,
                "rationale": (
                    "Correct. The core output of a gap analysis is a roadmap capturing both "
                    "what already meets requirements (avoiding redundant spend) and what is "
                    "missing, prioritized for remediation — exactly this action."
                ),
            },
            {
                "id": "b",
                "text": "Replace the existing SIEM with a new product because the framework was not originally designed around it.",
                "correct": False,
                "rationale": (
                    "Incorrect. The SIEM already satisfies the Detect function; replacing a "
                    "working, compliant tool wastes budget and does nothing to close the "
                    "actual gap in the Respond function."
                ),
            },
            {
                "id": "c",
                "text": "Conclude the organization is fully compliant since the Detect function is well covered.",
                "correct": False,
                "rationale": (
                    "Incorrect. A significant gap remains in the Respond function; declaring "
                    "full compliance while ignoring a known, documented gap defeats the "
                    "purpose of performing the gap analysis."
                ),
            },
            {
                "id": "d",
                "text": "Postpone documenting the Respond gap until the next audit cycle, since Detect is already strong.",
                "correct": False,
                "rationale": (
                    "Incorrect. Gap analyses exist to surface actionable findings immediately; "
                    "deferring known gaps rather than adding them to a remediation roadmap "
                    "undermines the process and delays risk reduction."
                ),
            },
        ],
        "explanation": (
            "A gap analysis should credit existing controls that already meet a requirement "
            "and translate unmet requirements into a prioritized remediation roadmap — not "
            "trigger unnecessary tool replacement or premature compliance claims."
        ),
    },
    # ── 1.2 Physical security ─────────────────────────────────────────────
    {
        "id": "nd1e-020",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Physical security",
        "stem": (
            "A television network's on-air broadcast control room requires staff to badge in "
            "at an outer door, then wait inside a small chamber with a second locked door "
            "that will not open until the first door has fully closed, and only one person's "
            "weight is detected on the interior floor sensor. Which physical security "
            "control is being described?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Mantrap",
                "correct": True,
                "rationale": (
                    "Correct. A mantrap is a small, interlocked double-door chamber that only "
                    "releases the second door after the first closes and verifies a single "
                    "occupant, specifically to prevent tailgating into a sensitive area."
                ),
            },
            {
                "id": "b",
                "text": "Bollard",
                "correct": False,
                "rationale": (
                    "Incorrect. A bollard is a short, sturdy vertical post used to stop "
                    "vehicle intrusion; it has nothing to do with an interlocked pedestrian "
                    "access chamber."
                ),
            },
            {
                "id": "c",
                "text": "Faraday cage",
                "correct": False,
                "rationale": (
                    "Incorrect. A Faraday cage blocks electromagnetic signals from entering or "
                    "leaving a space; it does not control physical foot traffic through "
                    "interlocked doors."
                ),
            },
            {
                "id": "d",
                "text": "Access control vestibule signage",
                "correct": False,
                "rationale": (
                    "Incorrect. Signage alone has no physical enforcement mechanism; the "
                    "scenario describes an active interlocking mechanism with a weight sensor, "
                    "not a sign."
                ),
            },
        ],
        "explanation": (
            "An interlocked double-door chamber that enforces single-person passage — "
            "verified here by a weight sensor — is a mantrap (also called an access control "
            "vestibule), designed specifically to defeat tailgating."
        ),
    },
    {
        "id": "nd1e-021",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Physical security",
        "stem": (
            "A national archive storing irreplaceable historical documents installs a gas-"
            "based fire suppression system in the storage vault instead of a traditional "
            "water sprinkler system. Which requirement is this design decision PRIMARILY "
            "intended to satisfy?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Suppressing fire without water damage that would destroy the irreplaceable paper documents",
                "correct": True,
                "rationale": (
                    "Correct. Clean-agent gas suppression systems extinguish fire by removing "
                    "heat or oxygen without discharging water, protecting sensitive, "
                    "irreplaceable materials from the water damage a sprinkler system would "
                    "cause."
                ),
            },
            {
                "id": "b",
                "text": "Reducing the archive's electricity costs compared to a sprinkler system",
                "correct": False,
                "rationale": (
                    "Incorrect. Cost of electricity is unrelated to the choice between a "
                    "sprinkler and gas suppression system; the decision is driven by asset "
                    "protection, not utility expense."
                ),
            },
            {
                "id": "c",
                "text": "Providing electromagnetic shielding for the documents",
                "correct": False,
                "rationale": (
                    "Incorrect. Fire suppression systems have no electromagnetic shielding "
                    "function; that would require a Faraday cage, an unrelated control."
                ),
            },
            {
                "id": "d",
                "text": "Meeting a badge-access requirement for the vault entrance",
                "correct": False,
                "rationale": (
                    "Incorrect. Badge access controls who may enter the vault; it is a "
                    "separate physical control from fire suppression method and does not "
                    "explain the choice of gas over water."
                ),
            },
        ],
        "explanation": (
            "Gas-based (clean-agent) suppression is chosen over water sprinklers specifically "
            "to protect irreplaceable or highly sensitive physical assets — like archival "
            "documents or server equipment — from water damage during a fire event."
        ),
    },
    # ── 1.2 Zero Trust architecture ──────────────────────────────────────
    {
        "id": "nd1e-022",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Zero Trust architecture",
        "stem": (
            "In a NIST SP 800-207 Zero Trust architecture, a subject (user/device) sends an "
            "access request that is evaluated by the Policy Engine using threat intelligence "
            "and identity signals, and the Policy Administrator generates the session-specific "
            "credentials or configuration needed to grant access. Which component then "
            "sits between the subject and the enterprise resource, enforcing the "
            "Policy Administrator's decision on every packet?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Policy Enforcement Point",
                "correct": True,
                "rationale": (
                    "Correct. The Policy Enforcement Point (PEP) is the component that sits "
                    "in the data plane, directly between the subject and the resource, "
                    "enabling, monitoring, and terminating the connection according to the "
                    "Policy Administrator's instructions."
                ),
            },
            {
                "id": "b",
                "text": "Policy Engine",
                "correct": False,
                "rationale": (
                    "Incorrect. The Policy Engine is the decision-making component in the "
                    "control plane that evaluates trust algorithms; it does not sit inline "
                    "enforcing traffic between subject and resource."
                ),
            },
            {
                "id": "c",
                "text": "Policy Administrator",
                "correct": False,
                "rationale": (
                    "Incorrect. The Policy Administrator generates the session credentials or "
                    "commands the PEP to establish or shut down the connection; it operates in "
                    "the control plane, not directly in the traffic path."
                ),
            },
            {
                "id": "d",
                "text": "Certificate authority",
                "correct": False,
                "rationale": (
                    "Incorrect. A CA is a supporting PKI component that issues certificates; "
                    "it is not one of the three core NIST 800-207 Zero Trust logical "
                    "components and does not enforce per-session access."
                ),
            },
        ],
        "explanation": (
            "NIST SP 800-207 defines the Policy Engine and Policy Administrator as control-"
            "plane decision-makers, while the Policy Enforcement Point sits in the data "
            "plane, directly gating traffic between the subject and the resource."
        ),
    },
    {
        "id": "nd1e-023",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Zero Trust architecture",
        "stem": (
            "A software company is redesigning its internal network around Zero Trust "
            "principles instead of a traditional perimeter-based model. Which TWO of the "
            "following changes reflect core Zero Trust principles? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Re-authenticate and re-authorize every access request based on current context, regardless of whether the device is already inside the corporate network.",
                "correct": True,
                "rationale": (
                    "Correct. Zero Trust replaces implicit trust based on network location "
                    "with continuous, context-based verification of every request, whether "
                    "the device is 'inside' or 'outside' the traditional perimeter."
                ),
            },
            {
                "id": "b",
                "text": "Segment the network into small policy zones so lateral movement between resources requires separate authorization for each hop.",
                "correct": True,
                "rationale": (
                    "Correct. Microsegmentation limits an attacker's ability to move laterally "
                    "after an initial compromise by requiring distinct authorization decisions "
                    "at each segment boundary, a core Zero Trust practice."
                ),
            },
            {
                "id": "c",
                "text": "Grant any device that successfully connects to the internal VPN full, unrestricted access to all internal resources.",
                "correct": False,
                "rationale": (
                    "Incorrect. This describes the implicit-trust perimeter model Zero Trust "
                    "explicitly rejects — access should never be granted broadly just because "
                    "a device reached the internal network."
                ),
            },
            {
                "id": "d",
                "text": "Trust a user's session for the remainder of the business day once their identity has been verified at initial login.",
                "correct": False,
                "rationale": (
                    "Incorrect. Zero Trust requires continuous evaluation, not a single "
                    "point-in-time verification that is then trusted indefinitely for hours "
                    "afterward."
                ),
            },
            {
                "id": "e",
                "text": "Rely on the firewall at the network edge as the sole checkpoint for access decisions.",
                "correct": False,
                "rationale": (
                    "Incorrect. A single perimeter checkpoint is the traditional castle-and-"
                    "moat model Zero Trust is designed to replace with distributed, "
                    "per-resource verification."
                ),
            },
        ],
        "explanation": (
            "Zero Trust principles include continuous, context-aware verification of every "
            "request and microsegmentation to limit lateral movement — rejecting the older "
            "model of implicit trust once a device is inside the perimeter or has "
            "authenticated once."
        ),
    },
    # ── 1.4 Blockchain and open public ledger ────────────────────────────
    {
        "id": "nd1e-024",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Blockchain and open public ledger",
        "stem": (
            "An art auction house wants to record the ownership history of high-value "
            "physical paintings on a distributed ledger, such that any attempt to alter a "
            "past ownership-transfer record would require recomputing every subsequent "
            "block's cryptographic hash and would be immediately detectable by all "
            "participating nodes. Which property of blockchain technology is BEING RELIED ON "
            "here?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Immutability through cryptographic chaining of blocks",
                "correct": True,
                "rationale": (
                    "Correct. Each block's hash incorporates the previous block's hash, so "
                    "altering any historical record breaks the chain and requires "
                    "recalculating every subsequent hash — a computationally infeasible and "
                    "immediately detectable act, which is what provides immutability."
                ),
            },
            {
                "id": "b",
                "text": "Confidentiality through end-to-end encryption of all ledger entries",
                "correct": False,
                "rationale": (
                    "Incorrect. Public blockchains are generally transparent and readable by "
                    "all participants; the scenario describes tamper-evidence, not hiding the "
                    "content of the ownership records from view."
                ),
            },
            {
                "id": "c",
                "text": "Centralized control by the auction house over all record modifications",
                "correct": False,
                "rationale": (
                    "Incorrect. Blockchain's value here comes from decentralization — no "
                    "single participant, including the auction house, can unilaterally alter "
                    "records — the opposite of centralized control."
                ),
            },
            {
                "id": "d",
                "text": "Automatic reversal of fraudulent transactions by network consensus",
                "correct": False,
                "rationale": (
                    "Incorrect. Blockchains do not automatically reverse recorded transactions; "
                    "once committed and confirmed, records are treated as permanent, which is "
                    "the point of the immutability property being described."
                ),
            },
        ],
        "explanation": (
            "The cryptographic chaining of block hashes is what makes historical records "
            "tamper-evident and effectively immutable — altering one record cascades "
            "detectable changes through every subsequent block."
        ),
    },
    # ── 1.4 Cryptographic hardware ───────────────────────────────────────
    {
        "id": "nd1e-025",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Cryptographic hardware",
        "stem": (
            "A laptop manufacturer builds every device with a dedicated cryptoprocessor "
            "chip soldered to the motherboard that generates and seals a disk-encryption key "
            "to the measured state of the boot firmware, refusing to release the key if the "
            "boot chain has been tampered with. Which technology is BEING DESCRIBED?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Trusted Platform Module (TPM)",
                "correct": True,
                "rationale": (
                    "Correct. A TPM is a dedicated hardware cryptoprocessor that seals keys "
                    "to a measured boot state, releasing them only if the platform's boot "
                    "integrity measurements match expected values — exactly this behavior."
                ),
            },
            {
                "id": "b",
                "text": "Hardware security module (HSM)",
                "correct": False,
                "rationale": (
                    "Incorrect. An HSM is a standalone, typically rack-mounted or removable "
                    "appliance for centralized high-volume key operations (e.g., for a CA); it "
                    "is not the small, motherboard-soldered chip that seals disk-encryption "
                    "keys to boot-state measurements on an individual laptop."
                ),
            },
            {
                "id": "c",
                "text": "Secure enclave within the main CPU die",
                "correct": False,
                "rationale": (
                    "Incorrect. A secure enclave (e.g., on some mobile SoCs) is an isolated "
                    "region within the main processor, not a discrete, separately soldered "
                    "chip; the scenario specifically describes a dedicated chip on the "
                    "motherboard."
                ),
            },
            {
                "id": "d",
                "text": "Hardware token (USB security key)",
                "correct": False,
                "rationale": (
                    "Incorrect. A hardware token is a removable, user-carried device used "
                    "primarily for authentication; it is not a permanently soldered "
                    "motherboard chip performing boot-state-sealed disk encryption."
                ),
            },
        ],
        "explanation": (
            "A soldered, motherboard-integrated chip that seals encryption keys to measured "
            "boot integrity is a Trusted Platform Module (TPM), distinct from an HSM "
            "(centralized appliance), a secure enclave (isolated CPU region), or a removable "
            "hardware token."
        ),
    },
    {
        "id": "nd1e-026",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Cryptographic hardware",
        "stem": (
            "A cryptocurrency exchange needs to generate and store the private keys "
            "protecting customer cold-storage wallets on a FIPS 140-2 Level 3 validated "
            "appliance capable of tens of thousands of signing operations per second, with "
            "keys that can never be exported in plaintext. Which device BEST satisfies this "
            "requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A hardware security module (HSM)",
                "correct": True,
                "rationale": (
                    "Correct. An HSM is purpose-built for high-throughput cryptographic "
                    "operations at FIPS-validated assurance levels, generating and storing "
                    "keys in tamper-resistant hardware that never exposes private key "
                    "material in plaintext outside the device."
                ),
            },
            {
                "id": "b",
                "text": "A Trusted Platform Module (TPM) on each exchange server",
                "correct": False,
                "rationale": (
                    "Incorrect. A TPM is designed for low-throughput, device-bound operations "
                    "like sealing a single machine's disk-encryption key, not for tens of "
                    "thousands of signing operations per second across a shared service."
                ),
            },
            {
                "id": "c",
                "text": "A software-based key vault running on a general-purpose virtual machine",
                "correct": False,
                "rationale": (
                    "Incorrect. A software-only vault on a general-purpose VM cannot meet the "
                    "FIPS 140-2 Level 3 tamper-resistant hardware requirement, since keys "
                    "could potentially be extracted if the underlying host is compromised."
                ),
            },
            {
                "id": "d",
                "text": "A USB security key issued to each administrator",
                "correct": False,
                "rationale": (
                    "Incorrect. A USB security key is designed for individual user "
                    "authentication, not for centralized, high-volume cryptographic signing "
                    "operations on behalf of an entire exchange platform."
                ),
            },
        ],
        "explanation": (
            "High-volume, FIPS-validated key generation and signing with keys that never "
            "leave tamper-resistant hardware is the defining use case for an HSM, distinct "
            "from a TPM (single-device, lower-throughput) or software-only key storage."
        ),
    },
    # ── 1.4 Cryptographic hardware and key-management tools ─────────────
    {
        "id": "nd1e-027",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Cryptographic hardware and key-management tools",
        "stem": (
            "A media streaming company stores content-encryption keys in a cloud provider's "
            "managed key-management service, which automatically rotates each key on a "
            "90-day schedule, enforces granular IAM policies over which services may use "
            "each key, and records every encrypt/decrypt call in an immutable audit log. "
            "Which capability is this service PRIMARILY providing?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Centralized key lifecycle management with access control and auditability",
                "correct": True,
                "rationale": (
                    "Correct. Automated rotation, granular access policies, and audit logging "
                    "of every cryptographic operation together describe centralized key "
                    "lifecycle management — the core function of a managed KMS."
                ),
            },
            {
                "id": "b",
                "text": "Data masking of sensitive fields before storage",
                "correct": False,
                "rationale": (
                    "Incorrect. Data masking substitutes sensitive values with altered or "
                    "fictional data; the scenario describes managing encryption keys "
                    "themselves, not transforming the underlying data values."
                ),
            },
            {
                "id": "c",
                "text": "Steganographic embedding of keys inside media files",
                "correct": False,
                "rationale": (
                    "Incorrect. Steganography hides data within other files; nothing in the "
                    "scenario describes concealing keys inside media content — the keys are "
                    "managed openly within the KMS with logging and access controls."
                ),
            },
            {
                "id": "d",
                "text": "Code obfuscation of the encryption algorithm's implementation",
                "correct": False,
                "rationale": (
                    "Incorrect. Obfuscation hides the logic of code from analysis; the "
                    "scenario describes key rotation, access policy, and audit logging, none "
                    "of which relate to hiding algorithm implementation details."
                ),
            },
        ],
        "explanation": (
            "Automated rotation, IAM-based access control, and audit logging of every "
            "cryptographic operation are hallmarks of centralized key lifecycle management "
            "provided by a managed key-management service (KMS)."
        ),
    },
    {
        "id": "nd1e-028",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Cryptographic hardware and key-management tools",
        "stem": (
            "An organization's PKI policy requires that whenever a data-encryption key (DEK) "
            "is generated to encrypt bulk file storage, that DEK itself must immediately be "
            "encrypted using a separate, tightly access-controlled master key before being "
            "written to disk alongside the encrypted data. Which key-management concept is "
            "BEING DESCRIBED?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Key wrapping (envelope encryption) using a key-encryption key",
                "correct": True,
                "rationale": (
                    "Correct. Encrypting a data-encryption key with a separate, more tightly "
                    "controlled key-encryption key before storage — so the DEK is never "
                    "stored in plaintext — is the definition of key wrapping, also called "
                    "envelope encryption."
                ),
            },
            {
                "id": "b",
                "text": "Key stretching to slow brute-force attacks against passwords",
                "correct": False,
                "rationale": (
                    "Incorrect. Key stretching applies additional computational rounds to "
                    "password-based keys to resist brute forcing; it does not describe "
                    "encrypting one key with another before storage."
                ),
            },
            {
                "id": "c",
                "text": "Perfect forward secrecy through ephemeral session keys",
                "correct": False,
                "rationale": (
                    "Incorrect. Perfect forward secrecy ensures past session keys cannot be "
                    "derived if a long-term key is later compromised; it concerns session "
                    "key generation, not wrapping a stored DEK with a master key."
                ),
            },
            {
                "id": "d",
                "text": "Key escrow for legal recovery purposes",
                "correct": False,
                "rationale": (
                    "Incorrect. Key escrow involves depositing a copy of a key with a trusted "
                    "third party for recovery or legal access; the scenario describes "
                    "protecting the DEK at rest through wrapping, not depositing a copy with "
                    "an external party."
                ),
            },
        ],
        "explanation": (
            "Encrypting a data-encryption key with a separate key-encryption key before "
            "storage is key wrapping (envelope encryption), a common practice to avoid ever "
            "storing a DEK in plaintext."
        ),
    },
    # ── 1.4 Hashing and salting ───────────────────────────────────────────
    {
        "id": "nd1e-029",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Hashing and salting",
        "stem": (
            "A digital evidence unit downloads a suspect's cloud-storage account contents "
            "and computes an MD5 checksum of the complete dataset the moment it is acquired. "
            "Months later, before presenting the evidence in court, the examiner recomputes "
            "the checksum and confirms it matches exactly. What is this checksum comparison "
            "PRIMARILY intended to demonstrate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "That the evidence has not been altered since acquisition",
                "correct": True,
                "rationale": (
                    "Correct. A matching hash computed at acquisition and again before "
                    "presentation demonstrates the bit-for-bit integrity of the evidence — "
                    "that it has not been modified during storage or transfer — which is "
                    "essential for admissibility."
                ),
            },
            {
                "id": "b",
                "text": "That the data was encrypted before storage",
                "correct": False,
                "rationale": (
                    "Incorrect. A hash checksum verifies integrity, not confidentiality; it "
                    "provides no information about whether the underlying data was ever "
                    "encrypted."
                ),
            },
            {
                "id": "c",
                "text": "That the suspect's identity has been verified",
                "correct": False,
                "rationale": (
                    "Incorrect. Hashing the acquired data has nothing to do with authenticating "
                    "the suspect's identity; it only confirms the dataset itself is unchanged."
                ),
            },
            {
                "id": "d",
                "text": "That the data is compressed to save storage space",
                "correct": False,
                "rationale": (
                    "Incorrect. Computing a hash does not compress or reduce the size of the "
                    "underlying data; it produces a fixed-length fingerprint used solely for "
                    "integrity verification."
                ),
            },
        ],
        "explanation": (
            "In digital forensics, matching hash values computed at acquisition and later "
            "confirm the evidence's integrity — that it has not been tampered with — which "
            "is required to maintain chain of custody and admissibility."
        ),
    },
    {
        "id": "nd1e-030",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Hashing and salting",
        "stem": (
            "A social media startup's authentication database is breached, and investigators "
            "find that although each password hash was generated with a unique, randomly "
            "generated salt, the salts were stored as plaintext in the SAME database table "
            "as the corresponding hashes. Given this, which statement BEST describes the "
            "resulting security posture?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The unique salts still prevent efficient reuse of precomputed rainbow tables, even though the salts themselves were exposed.",
                "correct": True,
                "rationale": (
                    "Correct. A salt's purpose is to defeat precomputed rainbow tables and "
                    "prevent identical passwords from producing identical hashes across "
                    "users, not to remain secret. Salts are meant to be stored alongside "
                    "hashes, so their exposure does not eliminate this protection, though the "
                    "attacker can still attempt slower per-account brute-force attacks."
                ),
            },
            {
                "id": "b",
                "text": "The breach is equivalent to having no salt at all, since the salts were exposed alongside the hashes.",
                "correct": False,
                "rationale": (
                    "Incorrect. Salts are designed to be non-secret and stored with the hash "
                    "by design; their exposure does not eliminate their per-account, "
                    "anti-rainbow-table benefit, unlike a scenario with no salting at all "
                    "where identical passwords always share identical hashes."
                ),
            },
            {
                "id": "c",
                "text": "The unique salts alone guarantee attackers cannot recover any passwords through brute-force attempts.",
                "correct": False,
                "rationale": (
                    "Incorrect. Salting does not prevent brute-force or dictionary attacks "
                    "against an individual hash — it only prevents efficient reuse across "
                    "many accounts and precomputed tables; weak passwords can still be "
                    "cracked per-account."
                ),
            },
            {
                "id": "d",
                "text": "Storing the salts in plaintext violates their intended purpose and should have used the same encryption as the hashes.",
                "correct": False,
                "rationale": (
                    "Incorrect. Salts are, by design, not secret and are intentionally stored "
                    "in plaintext alongside the hash; encrypting them is not standard practice "
                    "and is not what makes salting effective."
                ),
            },
        ],
        "explanation": (
            "Salts are not meant to be secret; their value comes from being unique per "
            "account, which defeats precomputed rainbow tables and prevents identical "
            "passwords from producing identical hashes — protection that persists even when "
            "salts are stored, and exposed, in plaintext."
        ),
    },
    # ── 1.4 Obfuscation techniques ────────────────────────────────────────
    {
        "id": "nd1e-031",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Obfuscation techniques",
        "stem": (
            "A ride-sharing app's backend logs display a driver's phone number to customer-"
            "support agents as '(555) ***-**89' so agents can confirm they are viewing the "
            "correct record without seeing the full number, while the complete number remains "
            "stored in an encrypted field accessible only to the billing system. Which "
            "technique is BEST illustrated by the support agent's partially hidden view?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Data masking",
                "correct": True,
                "rationale": (
                    "Correct. Displaying only a portion of a sensitive field while the full "
                    "value remains protected elsewhere is data masking — reducing exposure "
                    "for staff who only need partial information to do their job."
                ),
            },
            {
                "id": "b",
                "text": "Tokenization",
                "correct": False,
                "rationale": (
                    "Incorrect. Tokenization replaces the entire sensitive value with an "
                    "unrelated surrogate token mapped in a separate vault; here, a portion of "
                    "the real phone number itself is still shown, which is masking, not "
                    "full substitution with a token."
                ),
            },
            {
                "id": "c",
                "text": "Hashing",
                "correct": False,
                "rationale": (
                    "Incorrect. Hashing produces a fixed-length, one-way digest that would not "
                    "resemble a partially readable phone number at all; the scenario shows "
                    "real digits, just partially concealed."
                ),
            },
            {
                "id": "d",
                "text": "Steganography",
                "correct": False,
                "rationale": (
                    "Incorrect. Steganography hides data within an unrelated carrier file "
                    "(e.g., an image); it does not describe displaying a partially redacted "
                    "value in a support agent's interface."
                ),
            },
        ],
        "explanation": (
            "Showing only part of a sensitive value (like the last two digits of a phone "
            "number) while the full value stays protected is data masking, distinct from "
            "tokenization (full substitution with a surrogate), hashing (one-way digest), "
            "or steganography (hiding data in another file)."
        ),
    },
    {
        "id": "nd1e-032",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Obfuscation techniques",
        "stem": (
            "During incident response, malware analysts discover that a sample decodes its "
            "command-and-control server address at runtime by XOR-ing an embedded byte "
            "array against a single-byte key stored elsewhere in the binary, only revealing "
            "the readable domain name in memory once the process executes. Which technique "
            "is the malware author using?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Obfuscation of strings to evade static analysis",
                "correct": True,
                "rationale": (
                    "Correct. Encoding the C2 domain so it is unreadable in the binary on "
                    "disk, and only decoding it at runtime, is a classic obfuscation "
                    "technique used to defeat static analysis tools that scan for readable "
                    "strings and known-bad domain indicators."
                ),
            },
            {
                "id": "b",
                "text": "Hashing of the command-and-control domain for integrity verification",
                "correct": False,
                "rationale": (
                    "Incorrect. Hashing is one-way and cannot be reversed to recover the "
                    "original domain; the malware needs the actual domain name to connect, so "
                    "it uses a reversible XOR encoding, not a hash."
                ),
            },
            {
                "id": "c",
                "text": "Tokenization of the domain to comply with data protection regulations",
                "correct": False,
                "rationale": (
                    "Incorrect. Tokenization is a data-protection technique used to protect "
                    "sensitive data with an unrelated surrogate value in legitimate systems; "
                    "it is not applicable to malware hiding a C2 address from analysts."
                ),
            },
            {
                "id": "d",
                "text": "Digital signing of the payload to prove authenticity",
                "correct": False,
                "rationale": (
                    "Incorrect. Digital signing verifies authorship and integrity using "
                    "asymmetric keys; XOR-encoding a string to hide it from static analysis is "
                    "unrelated to signing a payload."
                ),
            },
        ],
        "explanation": (
            "Encoding strings so they are unreadable until decoded at runtime is a common "
            "obfuscation technique malware authors use to evade static-analysis detection of "
            "known-bad indicators like C2 domains."
        ),
    },
    # ── 1.4 Symmetric vs asymmetric encryption ───────────────────────────
    {
        "id": "nd1e-033",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Symmetric vs asymmetric encryption",
        "stem": (
            "An IoT sensor network transmits several megabytes of telemetry data per second "
            "from thousands of field devices to a central aggregator, and the devices have "
            "extremely limited CPU and battery capacity. The devices have already established "
            "shared secret keys with the aggregator through an out-of-band provisioning "
            "process. Which encryption approach is MOST appropriate for the ongoing telemetry "
            "traffic?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Symmetric encryption using the pre-shared keys",
                "correct": True,
                "rationale": (
                    "Correct. With shared keys already established and CPU/battery severely "
                    "constrained, symmetric encryption's low computational overhead makes it "
                    "the appropriate choice for high-throughput, resource-limited telemetry "
                    "transmission."
                ),
            },
            {
                "id": "b",
                "text": "Asymmetric encryption of every telemetry packet using each device's individual key pair",
                "correct": False,
                "rationale": (
                    "Incorrect. Asymmetric encryption's significant computational overhead "
                    "makes it poorly suited for high-volume, continuous data on devices with "
                    "extremely limited CPU and battery capacity, and it is unnecessary since "
                    "shared keys already exist."
                ),
            },
            {
                "id": "c",
                "text": "Hashing each telemetry packet instead of encrypting it",
                "correct": False,
                "rationale": (
                    "Incorrect. Hashing provides integrity verification, not confidentiality; "
                    "it does not protect the telemetry data from being read by an eavesdropper, "
                    "which encryption is needed for."
                ),
            },
            {
                "id": "d",
                "text": "Transmitting the data in plaintext since the devices already trust the aggregator",
                "correct": False,
                "rationale": (
                    "Incorrect. Trusting the aggregator does not protect data in transit from "
                    "interception by third parties on the network path; encryption is still "
                    "required regardless of the trust relationship between endpoints."
                ),
            },
        ],
        "explanation": (
            "Once a shared secret exists, symmetric encryption's efficiency makes it ideal "
            "for high-throughput, resource-constrained scenarios — asymmetric encryption is "
            "reserved for key exchange or digital signatures, not bulk data protection on "
            "constrained devices."
        ),
    },
    {
        "id": "nd1e-034",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Symmetric vs asymmetric encryption",
        "stem": (
            "A software vendor needs to digitally sign its application updates so that "
            "customers' devices can verify both the authenticity of the publisher and that "
            "the update file has not been altered since it was signed. Which key should the "
            "vendor use to generate the signature, and which key should customer devices use "
            "to verify it?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The vendor signs with its own private key; devices verify using the vendor's public key.",
                "correct": True,
                "rationale": (
                    "Correct. Signing must use the private key, which only the vendor "
                    "possesses, so a valid signature proves origin; anyone can then verify it "
                    "using the corresponding, freely distributed public key."
                ),
            },
            {
                "id": "b",
                "text": "The vendor signs with its public key; devices verify using the vendor's private key.",
                "correct": False,
                "rationale": (
                    "Incorrect. This reverses the roles. If signing used the public key, "
                    "anyone possessing that same public key could forge a valid signature, "
                    "defeating the purpose of proving authenticity."
                ),
            },
            {
                "id": "c",
                "text": "The vendor and every customer device share the same symmetric key used for both signing and verification.",
                "correct": False,
                "rationale": (
                    "Incorrect. A shared symmetric key does not provide non-repudiation, "
                    "since any device holding the same key could also produce a valid "
                    "signature; digital signatures require the asymmetric private/public "
                    "key pair model instead."
                ),
            },
            {
                "id": "d",
                "text": "The vendor signs with a randomly generated one-time key that is discarded and never shared with devices.",
                "correct": False,
                "rationale": (
                    "Incorrect. If the signing key is discarded and never shared, no device "
                    "could ever verify the signature; a persistent, distributable public key "
                    "must correspond to the private key used for signing."
                ),
            },
        ],
        "explanation": (
            "Digital signatures rely on the signer using their private key to sign a hash of "
            "the content, while anyone can verify authenticity and integrity using the "
            "corresponding, freely distributed public key — the roles cannot be reversed or "
            "replaced with a shared symmetric key without losing non-repudiation."
        ),
    },
]

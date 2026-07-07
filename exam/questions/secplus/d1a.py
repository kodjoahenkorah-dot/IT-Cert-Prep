"""
CompTIA Security+ (SY0-701) Domain 1: General Security Concepts — Set A
36 exam-quality questions covering objectives 1.1 through 1.4.
"""

QUESTIONS = [
    # ── 1.1 Security control categories ─────────────────────────────────────
    {
        "id": "nd1a-001",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security control categories",
        "stem": (
            "A retail company's IT department deploys a next-generation firewall that "
            "inspects encrypted traffic and automatically blocks connections to known "
            "malicious IP addresses before they reach internal servers. Which security "
            "control CATEGORY does this firewall represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Technical",
                "correct": True,
                "rationale": (
                    "Correct. Technical (logical) controls are implemented through "
                    "technology that automatically enforces rules — exactly what the "
                    "firewall does here."
                ),
            },
            {
                "id": "b",
                "text": "Managerial",
                "correct": False,
                "rationale": (
                    "Incorrect. Managerial controls are governance-level decisions, such as "
                    "the policy requiring a firewall to be deployed, not the technology "
                    "itself performing the enforcement."
                ),
            },
            {
                "id": "c",
                "text": "Operational",
                "correct": False,
                "rationale": (
                    "Incorrect. Operational controls are day-to-day, people-executed "
                    "procedures (e.g., manually reviewing firewall logs); the firewall's "
                    "automated blocking is a technical control, not a human process."
                ),
            },
            {
                "id": "d",
                "text": "Physical",
                "correct": False,
                "rationale": (
                    "Incorrect. Physical controls protect tangible assets (locks, fences, "
                    "guards). A firewall is a logical/technical control regardless of the "
                    "physical hardware it runs on."
                ),
            },
        ],
        "explanation": (
            "Control category describes HOW a control is implemented. A firewall enforcing "
            "rules automatically is a Technical control, distinct from the Managerial policy "
            "that required it or the Operational process of reviewing its logs."
        ),
    },
    {
        "id": "nd1a-002",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Security control categories",
        "stem": (
            "A board of directors approves an annual policy requiring the security team to "
            "conduct an enterprise-wide risk assessment to prioritize security investments "
            "for the coming fiscal year. Which control CATEGORY does this risk-assessment "
            "requirement represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Managerial",
                "correct": True,
                "rationale": (
                    "Correct. Managerial (administrative) controls are governance-level "
                    "decisions and planning activities — a board-approved policy driving "
                    "risk-based investment prioritization is a governance function."
                ),
            },
            {
                "id": "b",
                "text": "Operational",
                "correct": False,
                "rationale": (
                    "Incorrect. Operational controls are the routine, people-executed "
                    "day-to-day tasks (e.g., patching, awareness training). Strategic, "
                    "governance-driven risk-assessment planning to guide investment is a "
                    "managerial function, not a recurring operational task."
                ),
            },
            {
                "id": "c",
                "text": "Technical",
                "correct": False,
                "rationale": (
                    "Incorrect. No technology enforces this requirement; it is a policy "
                    "decision made by governance, not a technical implementation."
                ),
            },
            {
                "id": "d",
                "text": "Physical",
                "correct": False,
                "rationale": (
                    "Incorrect. Physical controls involve tangible protections; this is a "
                    "governance/planning requirement with no physical component."
                ),
            },
        ],
        "explanation": (
            "Managerial controls set direction and policy at the governance level (risk "
            "assessments, security policy, oversight). Operational controls are the "
            "recurring, people-driven activities that carry out that policy day to day."
        ),
    },

    # ── 1.1 Security control types ──────────────────────────────────────────
    {
        "id": "nd1a-003",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security control types",
        "stem": (
            "A legacy medical device runs an unsupported OS and cannot be patched due to "
            "vendor certification requirements. To reduce risk, the security team places "
            "the device on an isolated VLAN with enhanced monitoring, reachable only "
            "through a hardened jump box, specifically because patching is not an option. "
            "Which control TYPE BEST describes this isolation and monitoring?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Compensating",
                "correct": True,
                "rationale": (
                    "Correct. A compensating control is an alternative safeguard used when "
                    "the primary control (patching) cannot be implemented. Isolating the "
                    "device and restricting access substitutes for the missing patch."
                ),
            },
            {
                "id": "b",
                "text": "Preventive",
                "correct": False,
                "rationale": (
                    "Incorrect. VLAN isolation does restrict access, but in this scenario it "
                    "is explicitly deployed as a substitute for a control that cannot be "
                    "applied (patching), which is the defining characteristic of a "
                    "compensating control rather than a general preventive one."
                ),
            },
            {
                "id": "c",
                "text": "Detective",
                "correct": False,
                "rationale": (
                    "Incorrect. Enhanced monitoring alone would be detective, but the "
                    "combined measure — isolation plus restricted access implemented in "
                    "place of patching — is classified by its purpose: compensating for an "
                    "infeasible primary control."
                ),
            },
            {
                "id": "d",
                "text": "Corrective",
                "correct": False,
                "rationale": (
                    "Incorrect. Corrective controls act after an incident to restore or "
                    "remediate. This control is proactive and ongoing, not a response to an "
                    "incident that has already occurred."
                ),
            },
        ],
        "explanation": (
            "Compensating controls exist specifically to address risk when a required "
            "control (here, patching) cannot be implemented, distinguishing them from "
            "general preventive, detective, or corrective controls."
        ),
    },
    {
        "id": "nd1a-004",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Security control types",
        "stem": (
            "A retail bank installs PTZ cameras with visible signage at every branch "
            "entrance, recording continuously to a secured off-site server; loss "
            "prevention reviews the recordings weekly. Which TWO control types does this "
            "CCTV camera system BEST represent? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Deterrent",
                "correct": True,
                "rationale": (
                    "Correct. Visible cameras discourage would-be attackers from acting in "
                    "the first place, which is the definition of a deterrent control."
                ),
            },
            {
                "id": "b",
                "text": "Detective",
                "correct": True,
                "rationale": (
                    "Correct. The continuous recordings allow incidents to be identified and "
                    "documented after they occur during the weekly review, which is the "
                    "definition of a detective control."
                ),
            },
            {
                "id": "c",
                "text": "Preventive",
                "correct": False,
                "rationale": (
                    "Incorrect. Cameras do not physically stop an incident from occurring — "
                    "they discourage and document, but nothing about the camera itself "
                    "blocks an attacker who is undeterred."
                ),
            },
            {
                "id": "d",
                "text": "Corrective",
                "correct": False,
                "rationale": (
                    "Incorrect. Corrective controls restore or remediate after an incident; "
                    "reviewing footage does not itself repair damage or restore operations."
                ),
            },
            {
                "id": "e",
                "text": "Compensating",
                "correct": False,
                "rationale": (
                    "Incorrect. Compensating controls substitute for an infeasible primary "
                    "control; nothing in the scenario indicates the cameras are replacing a "
                    "control that could not be implemented."
                ),
            },
        ],
        "explanation": (
            "A single control can satisfy multiple types simultaneously. Visible, recording "
            "CCTV is a classic example of a control that is both deterrent (discourages) "
            "and detective (documents after the fact), but not preventive, corrective, or "
            "compensating."
        ),
    },

    # ── 1.1 Security control categories and types ───────────────────────────
    {
        "id": "nd1a-005",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security control categories and types",
        "stem": (
            "A company's policy requires data owners to approve access requests, but "
            "exception requests for unpatched legacy servers must be logged and manually "
            "reviewed by staff each month to catch any lingering unauthorized access. "
            "Which CATEGORY and TYPE pairing correctly classifies the monthly exception-log "
            "review itself?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Operational category / Detective type",
                "correct": True,
                "rationale": (
                    "Correct. Staff manually performing a recurring review is an operational "
                    "activity, and identifying issues after the fact from logs is a "
                    "detective function."
                ),
            },
            {
                "id": "b",
                "text": "Managerial category / Preventive type",
                "correct": False,
                "rationale": (
                    "Incorrect. Managerial describes the governance decision to require "
                    "exception approvals, not the recurring log review carried out by staff; "
                    "reviewing logs after the fact detects issues rather than preventing them."
                ),
            },
            {
                "id": "c",
                "text": "Technical category / Corrective type",
                "correct": False,
                "rationale": (
                    "Incorrect. No technology automatically performs this review — it is "
                    "done by people. Detection is also distinct from correction, which "
                    "implies restoring or fixing damage after impact."
                ),
            },
            {
                "id": "d",
                "text": "Physical category / Compensating type",
                "correct": False,
                "rationale": (
                    "Incorrect. This is not a tangible physical control, and it is not "
                    "substituting for a control that could not be implemented."
                ),
            },
        ],
        "explanation": (
            "Every control can be classified along two independent axes: category (how it "
            "is implemented — technical, managerial, operational, physical) and type (what "
            "it accomplishes — preventive, detective, corrective, deterrent, compensating, "
            "directive). A manual monthly log review is Operational/Detective."
        ),
    },
    {
        "id": "nd1a-006",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Security control categories and types",
        "stem": (
            "An ISP automatically reroutes a client's inbound traffic through a redundant "
            "scrubbing center the instant its systems detect a volumetric DDoS in progress, "
            "restoring normal routing once traffic returns to baseline. Which CATEGORY and "
            "TYPE pairing BEST describes this scrubbing-center failover?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Technical category / Corrective type",
                "correct": True,
                "rationale": (
                    "Correct. The rerouting is executed automatically by infrastructure "
                    "(technical), and it is triggered only once an attack is already "
                    "detected in progress, acting to restore normal service — the defining "
                    "trait of a corrective control."
                ),
            },
            {
                "id": "b",
                "text": "Technical category / Preventive type",
                "correct": False,
                "rationale": (
                    "Incorrect. The reroute activates only after detection of an active "
                    "attack, meaning the incident has already begun; a preventive control "
                    "would stop the incident from starting at all."
                ),
            },
            {
                "id": "c",
                "text": "Operational category / Corrective type",
                "correct": False,
                "rationale": (
                    "Incorrect. The rerouting is executed automatically by the scrubbing "
                    "infrastructure itself, not manually carried out by staff following a "
                    "day-to-day procedure, so the category is Technical, not Operational."
                ),
            },
            {
                "id": "d",
                "text": "Managerial category / Detective type",
                "correct": False,
                "rationale": (
                    "Incorrect. This is neither a governance/policy decision (managerial) "
                    "nor a mere identification of the event (detective) — the system "
                    "actively reroutes traffic to restore availability."
                ),
            },
        ],
        "explanation": (
            "Automated failover that responds to an in-progress attack to restore service "
            "is a Technical/Corrective control. Preventive controls stop incidents before "
            "they start; corrective controls act during or after to limit and reverse harm."
        ),
    },

    # ── 1.2 AAA framework ────────────────────────────────────────────────────
    {
        "id": "nd1a-007",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "AAA framework",
        "stem": (
            "A network administrator configures a wireless authentication server so that "
            "only the password portion of user credentials is encrypted in transit, and "
            "the authentication and authorization decisions are combined into a single "
            "response packet using UDP. Which AAA protocol is being used?"
        ),
        "options": [
            {
                "id": "a",
                "text": "RADIUS",
                "correct": True,
                "rationale": (
                    "Correct. RADIUS encrypts only the password, uses UDP, and combines "
                    "authentication and authorization into a single response — exactly as "
                    "described."
                ),
            },
            {
                "id": "b",
                "text": "TACACS+",
                "correct": False,
                "rationale": (
                    "Incorrect. TACACS+ encrypts the entire packet payload over TCP and "
                    "separates authentication, authorization, and accounting into distinct "
                    "exchanges — the opposite of the behavior described."
                ),
            },
            {
                "id": "c",
                "text": "Kerberos",
                "correct": False,
                "rationale": (
                    "Incorrect. Kerberos uses ticket-based authentication issued by a Key "
                    "Distribution Center; it does not describe this password-only encryption "
                    "or combined-response behavior of a network access AAA protocol."
                ),
            },
            {
                "id": "d",
                "text": "LDAP",
                "correct": False,
                "rationale": (
                    "Incorrect. LDAP is a directory access protocol used to query or bind "
                    "against a directory service; it does not define the AAA accounting "
                    "behavior or transport characteristics described here."
                ),
            },
        ],
        "explanation": (
            "RADIUS (UDP, password-only encryption, combined authn/authz) contrasts with "
            "TACACS+ (TCP, full payload encryption, separated AAA functions) — a frequently "
            "tested distinction on the exam."
        ),
    },
    {
        "id": "nd1a-008",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "AAA framework",
        "stem": (
            "A financial firm implements an access model where every file inherits a "
            "top-secret/secret/confidential label, and only users whose clearance and "
            "need-to-know match that label can open the file — even the file's owner "
            "cannot alter these permissions. Which authorization model is in use?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Mandatory Access Control (MAC)",
                "correct": True,
                "rationale": (
                    "Correct. MAC enforces access based on centrally assigned labels and "
                    "clearances that the resource owner cannot override — exactly what is "
                    "described."
                ),
            },
            {
                "id": "b",
                "text": "Discretionary Access Control (DAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. DAC lets the resource owner control permissions at their "
                    "discretion; here the owner explicitly cannot alter access, which rules "
                    "out DAC."
                ),
            },
            {
                "id": "c",
                "text": "Role-Based Access Control (RBAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. RBAC assigns permissions based on job role, not on "
                    "classification labels compared against a user's clearance level."
                ),
            },
            {
                "id": "d",
                "text": "Attribute-Based Access Control (ABAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. ABAC evaluates a broader, dynamic set of attributes (time, "
                    "location, device posture, etc.). While classification could be one "
                    "input, the scenario specifically describes a fixed clearance-vs-label "
                    "comparison enforced centrally, which is the defining trait of MAC."
                ),
            },
        ],
        "explanation": (
            "MAC is defined by centrally enforced labels/clearances that even the data "
            "owner cannot override — distinguishing it from DAC (owner-controlled), RBAC "
            "(role-based), and the more general, attribute-driven ABAC."
        ),
    },

    # ── 1.2 Attack type identification ──────────────────────────────────────
    {
        "id": "nd1a-009",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Attack type identification",
        "stem": (
            "An attacker sends a fraudulent email to a company's CFO, spoofed to appear "
            "from the CEO, requesting an urgent wire transfer to close a confidential "
            "acquisition before the end of business. Which attack technique is BEST "
            "described?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Whaling",
                "correct": True,
                "rationale": (
                    "Correct. Whaling is spear phishing specifically targeting a senior "
                    "executive (the CFO) with highly tailored, high-value business context "
                    "(an acquisition wire transfer)."
                ),
            },
            {
                "id": "b",
                "text": "Spear phishing",
                "correct": False,
                "rationale": (
                    "Incorrect. Spear phishing targets a specific individual generally, but "
                    "the more precise term for an attack aimed at a senior executive using "
                    "tailored, high-stakes business context is whaling."
                ),
            },
            {
                "id": "c",
                "text": "Vishing",
                "correct": False,
                "rationale": (
                    "Incorrect. Vishing is voice/phone-based social engineering; this attack "
                    "was conducted entirely via email."
                ),
            },
            {
                "id": "d",
                "text": "Pretexting",
                "correct": False,
                "rationale": (
                    "Incorrect. Pretexting is the broader technique of fabricating a "
                    "scenario to build trust across various channels. While a pretext is "
                    "present, the most precise classification for this executive-targeted "
                    "spoofed-email fraud is whaling."
                ),
            },
        ],
        "explanation": (
            "Phishing (mass) narrows to spear phishing (targeted individual) and further to "
            "whaling (targeted senior executive with high-value context) — the exam expects "
            "the MOST specific correct term."
        ),
    },
    {
        "id": "nd1a-010",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Attack type identification",
        "stem": (
            "During a forensic review, investigators find that an attacker first sent "
            "fraudulent ARP replies to redirect a victim's traffic through the attacker's "
            "laptop, then used that vantage point to alter DNS responses returned to the "
            "victim, redirecting a banking session to a fraudulent look-alike site. Which "
            "TWO attack techniques are demonstrated? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "ARP poisoning",
                "correct": True,
                "rationale": (
                    "Correct. The attacker sent fraudulent ARP replies to redirect LAN "
                    "traffic to their own machine, which is ARP poisoning."
                ),
            },
            {
                "id": "b",
                "text": "DNS poisoning",
                "correct": True,
                "rationale": (
                    "Correct. The attacker altered DNS responses returned to the victim to "
                    "redirect the banking session, which is DNS poisoning."
                ),
            },
            {
                "id": "c",
                "text": "VLAN hopping",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no evidence the attacker exploited 802.1Q trunking "
                    "to cross VLAN boundaries; the redirection was achieved through ARP and "
                    "DNS manipulation on the same segment."
                ),
            },
            {
                "id": "d",
                "text": "Session replay",
                "correct": False,
                "rationale": (
                    "Incorrect. No previously captured session tokens were replayed; the "
                    "attacker manipulated live DNS responses in real time, not a replay of "
                    "prior traffic."
                ),
            },
            {
                "id": "e",
                "text": "Downgrade attack",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no evidence of forcing the use of a weaker "
                    "protocol or cipher version; the described techniques are traffic "
                    "redirection, not protocol downgrading."
                ),
            },
        ],
        "explanation": (
            "This scenario chains two distinct on-path techniques: ARP poisoning to gain a "
            "man-in-the-middle position on the LAN, followed by DNS poisoning to redirect "
            "the victim's traffic to a fraudulent destination."
        ),
    },

    # ── 1.2 CIA triad and non-repudiation ────────────────────────────────────
    {
        "id": "nd1a-011",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "CIA triad and non-repudiation",
        "stem": (
            "A hospital's file integrity monitoring tool alerts that a patient record was "
            "modified outside of the EHR application's normal write process, though no "
            "unauthorized viewing of the record was detected. Which security objective was "
            "violated?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Integrity",
                "correct": True,
                "rationale": (
                    "Correct. Unauthorized modification of data — regardless of whether it "
                    "was viewed — is a violation of integrity."
                ),
            },
            {
                "id": "b",
                "text": "Confidentiality",
                "correct": False,
                "rationale": (
                    "Incorrect. Confidentiality is violated when unauthorized parties view "
                    "data. The alert concerns unauthorized modification, and no unauthorized "
                    "viewing was detected."
                ),
            },
            {
                "id": "c",
                "text": "Availability",
                "correct": False,
                "rationale": (
                    "Incorrect. Nothing in the scenario indicates the record became "
                    "inaccessible to authorized users."
                ),
            },
            {
                "id": "d",
                "text": "Non-repudiation",
                "correct": False,
                "rationale": (
                    "Incorrect. Non-repudiation concerns proving who performed an action to "
                    "prevent denial of that action; the scenario describes detection of an "
                    "unauthorized change, not a dispute over who performed a legitimate one."
                ),
            },
        ],
        "explanation": (
            "Unauthorized modification of data, detected independent of disclosure, is "
            "specifically an integrity violation within the CIA triad."
        ),
    },
    {
        "id": "nd1a-012",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "CIA triad and non-repudiation",
        "stem": (
            "An organization requires that every electronically signed contract embed a "
            "cryptographic signature generated with the signer's private key and stores a "
            "tamper-evident audit log of the signing session. A signer later claims they "
            "never approved the contract. Which security property allows the organization "
            "to refute this claim?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Non-repudiation",
                "correct": True,
                "rationale": (
                    "Correct. The combination of a private-key digital signature and a "
                    "tamper-evident audit trail proves both origin and occurrence of the "
                    "signing action, preventing the signer from credibly denying it."
                ),
            },
            {
                "id": "b",
                "text": "Integrity",
                "correct": False,
                "rationale": (
                    "Incorrect. Integrity confirms the contract was not altered after "
                    "signing, but by itself does not prove WHO performed the signing action "
                    "— that specific proof is the role of non-repudiation."
                ),
            },
            {
                "id": "c",
                "text": "Confidentiality",
                "correct": False,
                "rationale": (
                    "Incorrect. Confidentiality protects the contract from unauthorized "
                    "viewing; it has no bearing on refuting a denial of authorship."
                ),
            },
            {
                "id": "d",
                "text": "Authentication",
                "correct": False,
                "rationale": (
                    "Incorrect. Authentication verifies identity at the time of login or "
                    "signing, but alone does not provide durable, tamper-evident proof "
                    "tying that identity to a specific past action that survives a later "
                    "denial — that combination is specifically non-repudiation."
                ),
            },
        ],
        "explanation": (
            "Non-repudiation combines proof of origin (digital signature via private key) "
            "with tamper-evident records so a party cannot later deny having performed an "
            "action, going beyond what authentication or integrity alone provide."
        ),
    },

    # ── 1.2 Deception and disruption technologies ───────────────────────────
    {
        "id": "nd1a-013",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Deception and disruption technologies",
        "stem": (
            "A SOC analyst places a document named \"2026_Executive_Salaries.xlsx\" on a "
            "file share that no legitimate business process ever accesses, configured to "
            "trigger a SIEM alert the instant it is opened. Which technique is this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Honeyfile",
                "correct": True,
                "rationale": (
                    "Correct. A honeyfile is a decoy document planted to attract "
                    "unauthorized access; opening it triggers an alert, revealing insider "
                    "or attacker activity."
                ),
            },
            {
                "id": "b",
                "text": "Honeypot",
                "correct": False,
                "rationale": (
                    "Incorrect. A honeypot is an entire decoy system or service designed to "
                    "attract broad attacker interaction, not a single planted file used to "
                    "detect access to specific data."
                ),
            },
            {
                "id": "c",
                "text": "Honeytoken",
                "correct": False,
                "rationale": (
                    "Incorrect. A honeytoken is typically a fake credential, API key, or "
                    "embedded data value monitored for misuse elsewhere, not a standalone "
                    "lure document monitored for being opened."
                ),
            },
            {
                "id": "d",
                "text": "DNS sinkhole",
                "correct": False,
                "rationale": (
                    "Incorrect. A DNS sinkhole redirects malicious domain resolutions; it "
                    "does not describe a planted file monitored for file-open events."
                ),
            },
        ],
        "explanation": (
            "A honeyfile is a decoy file placed to detect unauthorized access, distinct "
            "from a honeypot (decoy system), honeytoken (decoy credential/data value), or "
            "DNS sinkhole (malicious domain redirection)."
        ),
    },
    {
        "id": "nd1a-014",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Deception and disruption technologies",
        "stem": (
            "A threat intelligence team embeds fake AWS access keys inside a public GitHub "
            "repository's configuration file to detect whether the repository has been "
            "scraped and the credentials misused elsewhere. Which technique is this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Honeytoken",
                "correct": True,
                "rationale": (
                    "Correct. A honeytoken is a fake credential or data value planted so "
                    "that its use anywhere else immediately signals compromise."
                ),
            },
            {
                "id": "b",
                "text": "Honeyfile",
                "correct": False,
                "rationale": (
                    "Incorrect. A honeyfile is a decoy document meant to trigger an alert "
                    "when opened; here the monitored value is a fake credential being USED "
                    "elsewhere, not a file simply being opened."
                ),
            },
            {
                "id": "c",
                "text": "Honeynet",
                "correct": False,
                "rationale": (
                    "Incorrect. A honeynet is an entire network of decoy systems used to "
                    "observe attacker lateral movement, not a single embedded fake "
                    "credential."
                ),
            },
            {
                "id": "d",
                "text": "Tarpit",
                "correct": False,
                "rationale": (
                    "Incorrect. A tarpit slows down or stalls an attacker's active "
                    "connection; it does not describe a passively planted fake credential "
                    "used for detection."
                ),
            },
        ],
        "explanation": (
            "Honeytokens are fake credentials or data values whose use elsewhere reveals a "
            "breach — distinct from honeyfiles (decoy documents), honeynets (decoy "
            "networks), and tarpits (connection-slowing disruption)."
        ),
    },

    # ── 1.2 Gap analysis ─────────────────────────────────────────────────────
    {
        "id": "nd1a-015",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Gap analysis",
        "stem": (
            "Following a merger, a security team compares its current password, "
            "encryption, and logging controls against the ISO/IEC 27001 Annex A control "
            "set required by the acquired subsidiary's contracts, then produces a report "
            "listing deficiencies and prioritized remediation milestones. Which process was "
            "performed?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Gap analysis",
                "correct": True,
                "rationale": (
                    "Correct. Comparing the current control posture against a target "
                    "framework and documenting deficiencies with a remediation roadmap is "
                    "the definition of a gap analysis."
                ),
            },
            {
                "id": "b",
                "text": "Business impact analysis",
                "correct": False,
                "rationale": (
                    "Incorrect. A BIA identifies critical business functions and quantifies "
                    "downtime impact (RTO/RPO), not a comparison of current controls against "
                    "a compliance framework."
                ),
            },
            {
                "id": "c",
                "text": "Vulnerability assessment",
                "correct": False,
                "rationale": (
                    "Incorrect. A vulnerability assessment scans systems for technical "
                    "weaknesses; this scenario compares governance and control posture "
                    "against a named framework, which is a gap analysis."
                ),
            },
            {
                "id": "d",
                "text": "Penetration test",
                "correct": False,
                "rationale": (
                    "Incorrect. A penetration test actively exploits weaknesses to validate "
                    "exploitability; the scenario describes a comparative documentation "
                    "review, not active exploitation."
                ),
            },
        ],
        "explanation": (
            "Gap analysis measures current state against a desired target state (a "
            "framework, regulation, or policy) and produces a prioritized remediation "
            "roadmap — distinct from a BIA, vulnerability assessment, or penetration test."
        ),
    },
    {
        "id": "nd1a-016",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Gap analysis",
        "stem": (
            "A CISO wants to determine which specific NIST CSF subcategories the "
            "organization already satisfies and which require new investment before the "
            "next audit cycle, in order to build next year's remediation roadmap. Which "
            "artifact is the DIRECT output of this activity?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Gap analysis report",
                "correct": True,
                "rationale": (
                    "Correct. Comparing current control coverage against the NIST CSF "
                    "baseline and producing a prioritized remediation roadmap is exactly "
                    "the output of a gap analysis."
                ),
            },
            {
                "id": "b",
                "text": "Risk register entry",
                "correct": False,
                "rationale": (
                    "Incorrect. A risk register catalogs identified risks with likelihood "
                    "and impact scores generally; it is not the specific comparative "
                    "artifact produced by measuring controls against a named framework "
                    "baseline."
                ),
            },
            {
                "id": "c",
                "text": "Business continuity plan",
                "correct": False,
                "rationale": (
                    "Incorrect. A BCP addresses continuity of operations during disruption "
                    "and is unrelated to comparing controls against a compliance framework."
                ),
            },
            {
                "id": "d",
                "text": "Vendor risk assessment scorecard",
                "correct": False,
                "rationale": (
                    "Incorrect. Vendor risk assessments evaluate third parties, not the "
                    "organization's own control posture against a framework."
                ),
            },
        ],
        "explanation": (
            "Gap analysis directly produces a report comparing current controls to a "
            "target framework baseline and a prioritized roadmap — a distinct artifact from "
            "a risk register, BCP, or vendor risk scorecard."
        ),
    },

    # ── 1.2 Physical security ────────────────────────────────────────────────
    {
        "id": "nd1a-017",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Physical security",
        "stem": (
            "A data center wants to stop an unauthorized person from following an "
            "authenticated employee through the server room's only entrance immediately "
            "after the employee badges in. Which control is the BEST fit?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Access control vestibule (mantrap)",
                "correct": True,
                "rationale": (
                    "Correct. A mantrap requires one door to close and verify before the "
                    "next opens, physically preventing more than one person from passing "
                    "through per credential."
                ),
            },
            {
                "id": "b",
                "text": "Proximity badge reader with PIN pad",
                "correct": False,
                "rationale": (
                    "Incorrect. Requiring badge plus PIN strengthens authentication of the "
                    "first person but does nothing to stop a second, unauthenticated person "
                    "from following through the same open door."
                ),
            },
            {
                "id": "c",
                "text": "Security guard stationed at the entrance",
                "correct": False,
                "rationale": (
                    "Incorrect. A guard can challenge suspicious individuals but, without a "
                    "physical interlock, cannot reliably stop a fast tailgater from slipping "
                    "through a normal single door, especially during high-traffic periods."
                ),
            },
            {
                "id": "d",
                "text": "CCTV camera at the entrance",
                "correct": False,
                "rationale": (
                    "Incorrect. A camera records the tailgating event for later "
                    "investigation but does not physically prevent the second person from "
                    "entering."
                ),
            },
        ],
        "explanation": (
            "Tailgating is defeated by an access control vestibule (mantrap), which "
            "physically enforces one person per authenticated credential — a preventive "
            "control, unlike badge readers, guards, or cameras alone."
        ),
    },
    {
        "id": "nd1a-018",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Physical security",
        "stem": (
            "A server room's badge log shows valid entries for an employee during a week "
            "the employee was confirmed on approved leave per HR records. No alarms "
            "triggered and no forced entry was evident. Which control would have MOST "
            "directly detected this specific type of misuse in real time?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Video surveillance correlated with the badge access log",
                "correct": True,
                "rationale": (
                    "Correct. Correlating footage with the badge log would reveal that the "
                    "badge was used by someone other than the assigned employee, exposing "
                    "badge cloning or loan misuse in real time."
                ),
            },
            {
                "id": "b",
                "text": "Motion-activated lighting",
                "correct": False,
                "rationale": (
                    "Incorrect. Motion lighting merely illuminates areas upon detected "
                    "movement; it does not identify or record WHO used the badge."
                ),
            },
            {
                "id": "c",
                "text": "A mantrap at the entrance",
                "correct": False,
                "rationale": (
                    "Incorrect. A mantrap regulates single-person entry per credential but "
                    "does not verify identity — it would not reveal that the person using "
                    "the badge wasn't the actual assigned employee, only that one body "
                    "passed through per swipe."
                ),
            },
            {
                "id": "d",
                "text": "A perimeter fence with signage",
                "correct": False,
                "rationale": (
                    "Incorrect. Perimeter fencing addresses outsider access to the property "
                    "boundary, not identity verification of who used an already-valid badge "
                    "inside the facility."
                ),
            },
        ],
        "explanation": (
            "Badge logs alone confirm a credential was used, not who physically used it. "
            "Correlating video surveillance with access logs is the control that directly "
            "detects badge misuse by verifying the identity of the person using it."
        ),
    },

    # ── 1.2 Zero Trust architecture ──────────────────────────────────────────
    {
        "id": "nd1a-019",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Zero Trust architecture",
        "stem": (
            "In a Zero Trust architecture built per NIST SP 800-207, which component "
            "evaluates a device's health, user identity, and threat intelligence data to "
            "render an allow/deny decision for a specific access request?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Policy Engine (PE)",
                "correct": True,
                "rationale": (
                    "Correct. The Policy Engine evaluates identity, device posture, and "
                    "threat intelligence against policy to make the actual grant/deny "
                    "decision."
                ),
            },
            {
                "id": "b",
                "text": "Policy Administrator (PA)",
                "correct": False,
                "rationale": (
                    "Incorrect. The PA establishes or terminates the communication path "
                    "based on the PE's decision — it executes and communicates the "
                    "decision but does not itself evaluate policy data to render it."
                ),
            },
            {
                "id": "c",
                "text": "Policy Enforcement Point (PEP)",
                "correct": False,
                "rationale": (
                    "Incorrect. The PEP is the data-plane gateway that physically allows or "
                    "blocks traffic per instructions received; it does not evaluate "
                    "identity, device, or threat data itself."
                ),
            },
            {
                "id": "d",
                "text": "Policy Decision Point (PDP)",
                "correct": False,
                "rationale": (
                    "Incorrect. The PDP is the overarching logical grouping of the Policy "
                    "Engine and Policy Administrator in NIST SP 800-207 terminology; the "
                    "specific sub-component that evaluates the data points to make the "
                    "actual decision is the Policy Engine."
                ),
            },
        ],
        "explanation": (
            "NIST SP 800-207 defines the control plane as the Policy Engine (evaluates and "
            "decides) plus the Policy Administrator (communicates the decision), with the "
            "Policy Enforcement Point in the data plane carrying it out."
        ),
    },
    {
        "id": "nd1a-020",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Zero Trust architecture",
        "stem": (
            "In the NIST SP 800-207 Zero Trust model, which TWO components together make "
            "up the CONTROL PLANE responsible for deciding whether to grant access? "
            "(Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Policy Engine",
                "correct": True,
                "rationale": (
                    "Correct. The Policy Engine evaluates access requests against policy "
                    "and is part of the control plane."
                ),
            },
            {
                "id": "b",
                "text": "Policy Administrator",
                "correct": True,
                "rationale": (
                    "Correct. The Policy Administrator translates the Policy Engine's "
                    "decision into instructions and is part of the control plane."
                ),
            },
            {
                "id": "c",
                "text": "Policy Enforcement Point",
                "correct": False,
                "rationale": (
                    "Incorrect. The PEP resides in the data plane; it enforces decisions "
                    "made by the control plane rather than deciding them."
                ),
            },
            {
                "id": "d",
                "text": "Identity Provider (IdP)",
                "correct": False,
                "rationale": (
                    "Incorrect. An IdP supplies identity assertions/attributes as an input "
                    "data source to the Policy Engine, but it is not one of the two named "
                    "control-plane components in the 800-207 model."
                ),
            },
            {
                "id": "e",
                "text": "SIEM",
                "correct": False,
                "rationale": (
                    "Incorrect. A SIEM may feed threat intelligence and context into the "
                    "Policy Engine but is not one of the defined control-plane components "
                    "in the model."
                ),
            },
        ],
        "explanation": (
            "The control plane in NIST SP 800-207 consists of the Policy Engine (decides) "
            "and Policy Administrator (communicates the decision); the Policy Enforcement "
            "Point sits in the data plane and carries the decision out."
        ),
    },

    # ── 1.3 Change management ────────────────────────────────────────────────
    {
        "id": "nd1a-021",
        "domain": 1,
        "objective": "1.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Change management",
        "stem": (
            "A production database outage occurs at 2 a.m. A DBA applies a configuration "
            "change to restore service without prior Change Advisory Board review, then "
            "documents the change and business justification the next morning for "
            "retrospective approval. Which change type was used?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Emergency change",
                "correct": True,
                "rationale": (
                    "Correct. Emergency changes are expedited to resolve critical incidents "
                    "and require retrospective review and documentation, exactly as "
                    "described."
                ),
            },
            {
                "id": "b",
                "text": "Standard change",
                "correct": False,
                "rationale": (
                    "Incorrect. Standard changes are pre-approved, low-risk, routine changes "
                    "(e.g., password resets); an ad hoc production fix during an active "
                    "outage requiring after-the-fact review is not pre-approved or routine."
                ),
            },
            {
                "id": "c",
                "text": "Normal change",
                "correct": False,
                "rationale": (
                    "Incorrect. Normal changes go through the full CAB approval process "
                    "BEFORE implementation; this change bypassed prior CAB approval due to "
                    "the urgency of restoring service."
                ),
            },
            {
                "id": "d",
                "text": "Unauthorized change",
                "correct": False,
                "rationale": (
                    "Incorrect. An unauthorized change lacks any governance oversight or "
                    "documentation. Here the DBA followed the defined emergency-change "
                    "process, including retrospective documentation and review — a "
                    "controlled, sanctioned pathway."
                ),
            },
        ],
        "explanation": (
            "Emergency changes allow expedited implementation during critical incidents but "
            "still require documentation and retrospective review, distinguishing them from "
            "both routine standard changes and fully unauthorized changes."
        ),
    },
    {
        "id": "nd1a-022",
        "domain": 1,
        "objective": "1.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Change management",
        "stem": (
            "A CAB approves a planned firewall rule change for the upcoming Saturday "
            "maintenance window. Before implementation, the network engineer is required "
            "to document the exact steps to revert the firewall to its prior configuration "
            "if the change causes unexpected outages. Which element of the change "
            "management process does this represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Backout/rollback plan",
                "correct": True,
                "rationale": (
                    "Correct. A backout plan documents how to reverse a change if it causes "
                    "problems, prepared in advance of implementation exactly as described."
                ),
            },
            {
                "id": "b",
                "text": "Impact analysis",
                "correct": False,
                "rationale": (
                    "Incorrect. Impact analysis assesses the anticipated technical, "
                    "business, and security risk of a proposed change BEFORE approval; "
                    "documenting how to reverse an implemented change is the distinct "
                    "backout plan."
                ),
            },
            {
                "id": "c",
                "text": "Request for Change (RFC)",
                "correct": False,
                "rationale": (
                    "Incorrect. The RFC is the initial documentation proposing the change "
                    "and its justification, submitted before CAB review — not the reversal "
                    "procedure prepared for use during implementation."
                ),
            },
            {
                "id": "d",
                "text": "Post-change review",
                "correct": False,
                "rationale": (
                    "Incorrect. The post-change review occurs AFTER implementation to "
                    "verify success; the reversal steps prepared in advance in case of "
                    "failure are the backout plan."
                ),
            },
        ],
        "explanation": (
            "A backout/rollback plan is a required artifact prepared before implementation, "
            "distinct from the earlier RFC and impact analysis and the later post-change "
            "review."
        ),
    },

    # ── 1.4 Blockchain and open public ledger ────────────────────────────────
    {
        "id": "nd1a-023",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Blockchain and open public ledger",
        "stem": (
            "A certificate authority publishes every issued TLS certificate to a publicly "
            "auditable, append-only log where each entry cryptographically references the "
            "previous entry, allowing anyone to detect if a log entry was retroactively "
            "altered. Which security property is provided PRIMARILY by this hash-chaining "
            "of entries?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Integrity",
                "correct": True,
                "rationale": (
                    "Correct. Hash-chaining entries makes any retroactive alteration "
                    "detectable, which is tamper-evidence — a direct expression of "
                    "integrity."
                ),
            },
            {
                "id": "b",
                "text": "Confidentiality",
                "correct": False,
                "rationale": (
                    "Incorrect. The log is explicitly public and openly auditable — the "
                    "design provides no confidentiality; its purpose is transparency, not "
                    "secrecy."
                ),
            },
            {
                "id": "c",
                "text": "Availability",
                "correct": False,
                "rationale": (
                    "Incorrect. Hash chaining detects tampering; it does not, by itself, "
                    "ensure the log remains accessible or resilient to outages — that "
                    "depends on replication/decentralization, not the hashing scheme."
                ),
            },
            {
                "id": "d",
                "text": "Non-repudiation",
                "correct": False,
                "rationale": (
                    "Incorrect. Non-repudiation would require binding entries to a signer's "
                    "private key to prove WHO issued a specific entry. The question asks "
                    "what the hash-chaining mechanism itself provides, which is "
                    "tamper-evidence (integrity), not proof of origin."
                ),
            },
        ],
        "explanation": (
            "Hash-chaining links each entry to the prior one, making retroactive tampering "
            "detectable — an integrity property distinct from confidentiality, "
            "availability, or the origin-proof role of non-repudiation."
        ),
    },
    {
        "id": "nd1a-024",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Blockchain and open public ledger",
        "stem": (
            "A supply-chain security team wants component provenance records to be "
            "resistant to a single warehouse employee unilaterally altering historical "
            "records, while still allowing any partner in a multi-organization consortium "
            "to independently verify the full history without relying on a central "
            "authority. Which design BEST satisfies this requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A decentralized, hash-chained ledger distributed across consortium nodes",
                "correct": True,
                "rationale": (
                    "Correct. No single point of control exists, and any alteration would "
                    "break the hash chain, immediately detectable by any node — satisfying "
                    "both tamper-resistance and independent, decentralized verification."
                ),
            },
            {
                "id": "b",
                "text": "A single organization-hosted relational database with role-based access control",
                "correct": False,
                "rationale": (
                    "Incorrect. A centralized database, even with RBAC, still allows a "
                    "privileged insider (e.g., a DBA at the hosting org) to alter historical "
                    "rows without independent verification by all partners — exactly what "
                    "the requirement rules out."
                ),
            },
            {
                "id": "c",
                "text": "A digitally signed PDF audit trail emailed to each partner after each transaction",
                "correct": False,
                "rationale": (
                    "Incorrect. Signed PDFs prove the origin of each individual document but "
                    "do not provide a continuously linked, tamper-evident chain across all "
                    "historical records, nor consortium-wide independent verification "
                    "without trusting the distributor."
                ),
            },
            {
                "id": "d",
                "text": "A weekly encrypted backup of the provenance database sent to a third-party escrow service",
                "correct": False,
                "rationale": (
                    "Incorrect. Backups protect against data loss but don't provide "
                    "real-time, decentralized, cryptographically linked verification of the "
                    "full historical record by all consortium members."
                ),
            },
        ],
        "explanation": (
            "A decentralized blockchain distributes trust across consortium nodes and uses "
            "hash-chaining so that any alteration is independently detectable by all "
            "parties, without relying on a single trusted central authority."
        ),
    },

    # ── 1.4 Certificates ──────────────────────────────────────────────────────
    {
        "id": "nd1a-025",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Certificates",
        "stem": (
            "A user visits an internal HR portal and the browser flags the certificate as "
            "untrusted because it was signed by the same server that hosts the site, "
            "rather than by a recognized public CA. Which type of certificate is in use?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Self-signed certificate",
                "correct": True,
                "rationale": (
                    "Correct. A self-signed certificate is signed by the same entity that "
                    "issued it, so it does not chain to a trusted root and browsers flag it "
                    "as untrusted."
                ),
            },
            {
                "id": "b",
                "text": "Wildcard certificate",
                "correct": False,
                "rationale": (
                    "Incorrect. A wildcard certificate secures a domain and its first-level "
                    "subdomains and is typically still issued and signed by a trusted CA; it "
                    "would not, by itself, cause an untrusted-signer warning."
                ),
            },
            {
                "id": "c",
                "text": "Domain Validated (DV) certificate",
                "correct": False,
                "rationale": (
                    "Incorrect. A DV certificate is issued by a trusted public CA after "
                    "verifying only domain ownership; it still chains to a trusted root, so "
                    "browsers would not flag it as untrusted."
                ),
            },
            {
                "id": "d",
                "text": "SAN (Subject Alternative Name) certificate",
                "correct": False,
                "rationale": (
                    "Incorrect. A SAN certificate covers multiple hostnames but, like DV, is "
                    "normally issued and signed by a trusted CA — the defining issue here is "
                    "who signed it, not how many names it covers."
                ),
            },
        ],
        "explanation": (
            "Browsers flag certificates as untrusted based on the signing chain of trust, "
            "not on scope (wildcard/SAN) or validation level (DV/OV/EV). A self-signed "
            "certificate lacks any trusted root chain."
        ),
    },
    {
        "id": "nd1a-026",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Certificates",
        "stem": (
            "A large enterprise wants TLS clients to receive real-time certificate "
            "revocation status without each client independently querying the CA's OCSP "
            "responder during every handshake, which creates latency and load on the CA. "
            "Which mechanism BEST addresses this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "OCSP stapling",
                "correct": True,
                "rationale": (
                    "Correct. With OCSP stapling, the server itself periodically queries the "
                    "responder and attaches (staples) the signed response to the TLS "
                    "handshake, giving clients real-time status without each client "
                    "querying the CA directly."
                ),
            },
            {
                "id": "b",
                "text": "Certificate Revocation List (CRL)",
                "correct": False,
                "rationale": (
                    "Incorrect. A CRL is a periodically published, often large list of "
                    "revoked certificates; it is less real-time than OCSP and still requires "
                    "clients to fetch and parse a growing list, which doesn't remove "
                    "client-side lookup overhead the way stapling does."
                ),
            },
            {
                "id": "c",
                "text": "Certificate pinning",
                "correct": False,
                "rationale": (
                    "Incorrect. Certificate pinning hard-codes an expected certificate or "
                    "key in the client to prevent MITM with fraudulent certificates; it does "
                    "not provide revocation status at all."
                ),
            },
            {
                "id": "d",
                "text": "Standard OCSP without stapling",
                "correct": False,
                "rationale": (
                    "Incorrect. Standard OCSP still requires each individual client to query "
                    "the CA's responder directly for every handshake, which is precisely the "
                    "load and latency problem the scenario wants eliminated."
                ),
            },
        ],
        "explanation": (
            "OCSP stapling shifts the revocation-status query from every client to the "
            "server itself, which caches and attaches the signed response — reducing load "
            "on the CA compared to CRLs or unstapled OCSP."
        ),
    },

    # ── 1.4 Cryptographic hardware ───────────────────────────────────────────
    {
        "id": "nd1a-027",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Cryptographic hardware",
        "stem": (
            "A company requires that BitLocker's disk-encryption keys be sealed to a "
            "specific hardware root of trust soldered to the laptop motherboard, and that "
            "the boot process cryptographically validate each stage before releasing the "
            "key. Which technology satisfies BOTH requirements?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Trusted Platform Module (TPM)",
                "correct": True,
                "rationale": (
                    "Correct. The TPM is soldered to the motherboard, seals keys to that "
                    "specific device, and supports secure boot measurement — exactly what "
                    "is described."
                ),
            },
            {
                "id": "b",
                "text": "Hardware Security Module (HSM)",
                "correct": False,
                "rationale": (
                    "Incorrect. An HSM is typically an external appliance or PCIe device "
                    "used for centralized, high-volume cryptographic operations (e.g., CA "
                    "signing keys); it is not the soldered-motherboard chip that seals "
                    "BitLocker keys and measures boot stages for a single endpoint."
                ),
            },
            {
                "id": "c",
                "text": "Secure Enclave",
                "correct": False,
                "rationale": (
                    "Incorrect. Secure Enclave refers to an isolated CPU execution "
                    "environment primarily used for tasks like biometric data protection; "
                    "it is not the term for the Windows BitLocker boot-measurement chip, "
                    "which is specifically the TPM."
                ),
            },
            {
                "id": "d",
                "text": "Hardware key management system (KMS) appliance",
                "correct": False,
                "rationale": (
                    "Incorrect. A KMS manages the lifecycle of keys across an organization; "
                    "it isn't a per-device soldered chip that measures boot integrity for a "
                    "single endpoint's disk encryption."
                ),
            },
        ],
        "explanation": (
            "The TPM is a motherboard-soldered chip specifically designed for platform key "
            "sealing and secure-boot measurement, distinguishing it from appliance-scale "
            "HSMs, processor Secure Enclaves, and enterprise KMS services."
        ),
    },
    {
        "id": "nd1a-028",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Cryptographic hardware",
        "stem": (
            "A payment processor needs a FIPS 140-2 Level 3 validated appliance to generate "
            "and store the root signing keys for its internal CA, capable of very "
            "high-volume signing operations while remaining tamper-responsive (zeroizing "
            "keys if physical intrusion is detected). Which technology BEST meets this "
            "requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Hardware Security Module (HSM)",
                "correct": True,
                "rationale": (
                    "Correct. HSMs are appliance-grade, FIPS 140-2/3 Level 3+ validated "
                    "devices built for high-volume cryptographic operations and "
                    "tamper-responsive key storage — exactly what CAs use for root keys."
                ),
            },
            {
                "id": "b",
                "text": "Trusted Platform Module (TPM)",
                "correct": False,
                "rationale": (
                    "Incorrect. A TPM is a low-throughput chip embedded in a single "
                    "endpoint's motherboard designed for boot integrity and local key "
                    "sealing; it is not built for the high-volume, appliance-grade signing "
                    "operations of a CA's root key infrastructure."
                ),
            },
            {
                "id": "c",
                "text": "Secure Enclave",
                "correct": False,
                "rationale": (
                    "Incorrect. Secure Enclave technology isolates operations within a "
                    "single device's processor and is not deployed as a standalone "
                    "tamper-responsive appliance for enterprise CA root key operations."
                ),
            },
            {
                "id": "d",
                "text": "Software-based key vault with disk encryption",
                "correct": False,
                "rationale": (
                    "Incorrect. A software-only vault, even encrypted, lacks the physical "
                    "tamper-responsiveness (zeroization) and FIPS 140-2 Level 3 hardware "
                    "validation explicitly required by the scenario."
                ),
            },
        ],
        "explanation": (
            "HSMs are the appliance-grade, tamper-responsive, FIPS-validated hardware used "
            "specifically to protect CA root signing keys at high transaction volume — "
            "unlike TPMs, Secure Enclaves, or software-only vaults."
        ),
    },

    # ── 1.4 Cryptographic hardware and key-management tools ─────────────────
    {
        "id": "nd1a-029",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Cryptographic hardware and key-management tools",
        "stem": (
            "A cloud-native company stores encryption keys in a managed service that "
            "automatically rotates keys on a defined schedule, logs every cryptographic "
            "operation for audit purposes, and enforces separation of duties between key "
            "administrators and application developers who merely reference key IDs. "
            "Which solution is being described?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Key Management System (KMS)",
                "correct": True,
                "rationale": (
                    "Correct. Automatic rotation scheduling, audit logging, and separation "
                    "of duties between key custodians and key users are the defining "
                    "lifecycle-management functions of a KMS."
                ),
            },
            {
                "id": "b",
                "text": "Hardware Security Module (HSM)",
                "correct": False,
                "rationale": (
                    "Incorrect. While many KMS offerings use an HSM underneath for storage, "
                    "the scenario specifically describes lifecycle management functions — "
                    "rotation scheduling, audit logging, duty separation — which are the "
                    "defining functions of a KMS layer, not the HSM hardware itself."
                ),
            },
            {
                "id": "c",
                "text": "Certificate Authority (CA)",
                "correct": False,
                "rationale": (
                    "Incorrect. A CA issues and signs certificates; it does not describe "
                    "automatic key rotation scheduling and developer/administrator role "
                    "separation for general-purpose encryption keys."
                ),
            },
            {
                "id": "d",
                "text": "Secure Enclave",
                "correct": False,
                "rationale": (
                    "Incorrect. A Secure Enclave isolates operations within a device's own "
                    "processor; it does not describe a centralized cloud service managing "
                    "rotation, logging, and duty separation across an organization's keys."
                ),
            },
        ],
        "explanation": (
            "A KMS is defined by its key-lifecycle management capabilities — rotation, "
            "audit logging, and separation of duties — distinct from the underlying HSM "
            "hardware, a CA's certificate-issuance role, or a processor's Secure Enclave."
        ),
    },
    {
        "id": "nd1a-030",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Cryptographic hardware and key-management tools",
        "stem": (
            "An organization's PKI policy requires that the private key used to sign the "
            "root CA certificate never touch a general-purpose server, remain offline "
            "except during scheduled signing ceremonies, and be protected by "
            "hardware-enforced tamper response. Day-to-day TLS certificate issuance for "
            "internal services must use a separate intermediate CA whose keys support much "
            "higher transaction volume without a signing ceremony each time. Which "
            "combination of tools BEST satisfies both requirements?"
        ),
        "options": [
            {
                "id": "a",
                "text": "An offline HSM for the root CA key and an online, FIPS-validated HSM for the intermediate CA",
                "correct": True,
                "rationale": (
                    "Correct. Keeping the root CA's HSM offline except during ceremonies "
                    "satisfies the root key isolation requirement, while a separate online "
                    "HSM for the intermediate CA supports high-volume day-to-day issuance."
                ),
            },
            {
                "id": "b",
                "text": "A single online HSM shared by both the root and intermediate CA",
                "correct": False,
                "rationale": (
                    "Incorrect. Keeping the root CA key online contradicts the explicit "
                    "requirement that it remain offline except during scheduled ceremonies; "
                    "sharing one online HSM for both violates that isolation requirement."
                ),
            },
            {
                "id": "c",
                "text": "A TPM for the root CA and a KMS for the intermediate CA",
                "correct": False,
                "rationale": (
                    "Incorrect. A TPM is designed for single-endpoint boot integrity and key "
                    "sealing, not for CA root-key ceremonies requiring dedicated offline "
                    "tamper-responsive hardware at appliance scale; a general KMS also "
                    "typically lacks the appliance-grade signing throughput a dedicated "
                    "intermediate HSM provides."
                ),
            },
            {
                "id": "d",
                "text": "A software key vault for the root CA and an HSM for the intermediate CA",
                "correct": False,
                "rationale": (
                    "Incorrect. A software-only vault does not provide the hardware-enforced "
                    "tamper response required for the root CA's most sensitive key, "
                    "regardless of being kept offline."
                ),
            },
        ],
        "explanation": (
            "Best-practice PKI design keeps the root CA's HSM offline except during signing "
            "ceremonies, while a separate online, appliance-grade HSM handles the "
            "intermediate CA's higher-volume issuance workload."
        ),
    },

    # ── 1.4 Hashing and salting ───────────────────────────────────────────────
    {
        "id": "nd1a-031",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Hashing and salting",
        "stem": (
            "A penetration tester recovers a database dump of password hashes and observes "
            "that several users with the identical password \"Winter2026!\" have completely "
            "different stored hash values. Which practice MOST likely explains this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Salting",
                "correct": True,
                "rationale": (
                    "Correct. A unique random salt added per user before hashing causes "
                    "identical passwords to produce different stored hash values."
                ),
            },
            {
                "id": "b",
                "text": "Use of HMAC",
                "correct": False,
                "rationale": (
                    "Incorrect. HMAC combines a hash with a shared secret key for message "
                    "authentication; it isn't the standard mechanism explaining per-user "
                    "unique hashes for identical passwords in a password-storage database "
                    "— that is the specific purpose of salting."
                ),
            },
            {
                "id": "c",
                "text": "Use of a stronger hash algorithm (e.g., SHA-256 instead of MD5)",
                "correct": False,
                "rationale": (
                    "Incorrect. Switching hash algorithms alone doesn't cause identical "
                    "inputs to produce different outputs; the same algorithm applied to the "
                    "same unsalted password always yields the same digest, regardless of "
                    "algorithm strength."
                ),
            },
            {
                "id": "d",
                "text": "Key stretching alone (e.g., increased bcrypt cost factor)",
                "correct": False,
                "rationale": (
                    "Incorrect. Increasing the work factor raises computational cost per "
                    "hash but does not, by itself, cause identical passwords to produce "
                    "different digests — the per-user randomization observed here is "
                    "attributable to salting."
                ),
            },
        ],
        "explanation": (
            "Salting adds a unique, random value per user before hashing, ensuring "
            "identical passwords never produce identical stored hashes and defeating "
            "rainbow table attacks."
        ),
    },
    {
        "id": "nd1a-032",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Hashing and salting",
        "stem": (
            "A security architect must select a password storage algorithm for a new "
            "authentication system that is intentionally slow and memory-hard to resist "
            "GPU/ASIC-accelerated cracking, and was the winner of the Password Hashing "
            "Competition. Which algorithm should be selected?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Argon2",
                "correct": True,
                "rationale": (
                    "Correct. Argon2 was the winner of the Password Hashing Competition and "
                    "is specifically designed to be memory-hard to resist GPU/ASIC "
                    "acceleration."
                ),
            },
            {
                "id": "b",
                "text": "bcrypt",
                "correct": False,
                "rationale": (
                    "Incorrect. bcrypt is also slow and widely recommended for password "
                    "storage, but it is not the Password Hashing Competition winner and is "
                    "not memory-hard to the same degree as Argon2, which was specifically "
                    "selected as the PHC winner for GPU/ASIC resistance."
                ),
            },
            {
                "id": "c",
                "text": "SHA-256 with a random salt",
                "correct": False,
                "rationale": (
                    "Incorrect. SHA-256 is a fast, general-purpose cryptographic hash "
                    "designed for speed; being fast makes it a poor choice for password "
                    "storage regardless of salting, since it doesn't resist brute-force "
                    "acceleration the way purpose-built slow algorithms do."
                ),
            },
            {
                "id": "d",
                "text": "HMAC-SHA256",
                "correct": False,
                "rationale": (
                    "Incorrect. HMAC-SHA256 provides keyed message integrity/authentication "
                    "using a fast hash; it is not a memory-hard, intentionally slow "
                    "password-hashing algorithm and was not a PHC entrant or winner."
                ),
            },
        ],
        "explanation": (
            "Argon2 was purpose-built and selected as the Password Hashing Competition "
            "winner for its memory-hard, GPU/ASIC-resistant design — a stronger fit than "
            "bcrypt, fast general-purpose hashes, or HMAC."
        ),
    },

    # ── 1.4 Obfuscation techniques ────────────────────────────────────────────
    {
        "id": "nd1a-033",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Obfuscation techniques",
        "stem": (
            "A payment gateway replaces customers' 16-digit credit card numbers with "
            "randomly generated 16-digit surrogate values stored in a secure vault mapping "
            "table, so that if the transaction database is breached, the stolen values "
            "cannot be used to reconstruct the original card numbers without separate "
            "access to the vault. Which technique is this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Tokenization",
                "correct": True,
                "rationale": (
                    "Correct. Tokenization replaces sensitive data with a non-sensitive "
                    "surrogate token tracked in a secure vault, with no mathematical "
                    "relationship to the original value."
                ),
            },
            {
                "id": "b",
                "text": "Encryption",
                "correct": False,
                "rationale": (
                    "Incorrect. Encryption is mathematically reversible with the correct "
                    "key and produces ciphertext, not a randomly generated, unrelated "
                    "surrogate value stored in a separate vault mapping."
                ),
            },
            {
                "id": "c",
                "text": "Data masking",
                "correct": False,
                "rationale": (
                    "Incorrect. Data masking typically replaces sensitive data with "
                    "realistic-but-fake values for non-production environments like dev/"
                    "test, not for protecting live production transaction data via a "
                    "reversible vault lookup used at the point of sale."
                ),
            },
            {
                "id": "d",
                "text": "Hashing",
                "correct": False,
                "rationale": (
                    "Incorrect. Hashing is a one-way, deterministic function producing a "
                    "fixed digest; it doesn't support the reversible vault-based retrieval "
                    "of the original card number needed for legitimate business functions "
                    "like refunds."
                ),
            },
        ],
        "explanation": (
            "Tokenization substitutes sensitive data with an unrelated surrogate value "
            "retrievable only via a secure vault — the standard PCI DSS technique for "
            "protecting cardholder data, distinct from encryption, masking, or hashing."
        ),
    },
    {
        "id": "nd1a-034",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Obfuscation techniques",
        "stem": (
            "A researcher extracts an image file from a suspect's laptop and, after "
            "running steganalysis tools, discovers hidden exfiltrated source code embedded "
            "in the least significant bits of the image's pixel data, undetectable through "
            "normal visual inspection or standard DLP keyword scanning. Which technique did "
            "the attacker use to exfiltrate the data?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Steganography",
                "correct": True,
                "rationale": (
                    "Correct. Steganography hides the existence of data within an innocuous "
                    "carrier file, such as embedding it in the least-significant bits of an "
                    "image."
                ),
            },
            {
                "id": "b",
                "text": "Tokenization",
                "correct": False,
                "rationale": (
                    "Incorrect. Tokenization substitutes sensitive data with a non-sensitive "
                    "token tracked in a vault; it does not involve hiding data within the "
                    "bit-level structure of a carrier file such as an image."
                ),
            },
            {
                "id": "c",
                "text": "Data masking",
                "correct": False,
                "rationale": (
                    "Incorrect. Data masking creates realistic fake data for non-production "
                    "use; it does not describe embedding actual exfiltrated content covertly "
                    "inside another file's pixel data."
                ),
            },
            {
                "id": "d",
                "text": "Code obfuscation",
                "correct": False,
                "rationale": (
                    "Incorrect. Code obfuscation makes source or compiled code difficult to "
                    "reverse-engineer by altering its structure; it does not describe hiding "
                    "data inside an unrelated carrier file's least-significant bits, which "
                    "is specifically steganography."
                ),
            },
        ],
        "explanation": (
            "Steganography conceals the existence of data within a carrier file (e.g., an "
            "image's least-significant bits) — distinct from tokenization, data masking, "
            "and code obfuscation, which each serve different purposes."
        ),
    },

    # ── 1.4 Symmetric vs asymmetric encryption ───────────────────────────────
    {
        "id": "nd1a-035",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Symmetric vs asymmetric encryption",
        "stem": (
            "A VPN gateway needs to encrypt a high-throughput bulk data stream between two "
            "data centers with minimal CPU overhead, after the endpoints have already "
            "exchanged a shared secret using a key-exchange protocol. Which type of "
            "algorithm SHOULD be used for the bulk data encryption itself?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Symmetric encryption (e.g., AES-256-GCM)",
                "correct": True,
                "rationale": (
                    "Correct. Symmetric algorithms are fast and efficient, making them "
                    "suitable for high-throughput bulk data encryption once a shared key "
                    "has been established."
                ),
            },
            {
                "id": "b",
                "text": "Asymmetric encryption (e.g., RSA-4096)",
                "correct": False,
                "rationale": (
                    "Incorrect. Asymmetric algorithms are computationally expensive and "
                    "impractical for high-throughput bulk data encryption; they are used "
                    "for key exchange and signing, not for encrypting the ongoing bulk data "
                    "stream itself."
                ),
            },
            {
                "id": "c",
                "text": "Hashing (e.g., SHA-256)",
                "correct": False,
                "rationale": (
                    "Incorrect. Hashing is a one-way integrity function, not a reversible "
                    "encryption method; it cannot be used to encrypt and decrypt the bulk "
                    "data stream for confidentiality."
                ),
            },
            {
                "id": "d",
                "text": "Elliptic Curve Diffie-Hellman (ECDH)",
                "correct": False,
                "rationale": (
                    "Incorrect. ECDH is a key-exchange mechanism used to establish the "
                    "shared secret, already completed per the stem; it is not used to "
                    "encrypt the ongoing bulk data payload itself."
                ),
            },
        ],
        "explanation": (
            "TLS and VPNs use hybrid encryption: an asymmetric key-exchange establishes a "
            "shared secret, and a fast symmetric algorithm (e.g., AES-GCM) then handles "
            "high-throughput bulk data encryption."
        ),
    },
    {
        "id": "nd1a-036",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Symmetric vs asymmetric encryption",
        "stem": (
            "A developer needs to select asymmetric algorithms suitable for generating a "
            "digital signature that provides non-repudiation for signed software updates. "
            "Which TWO of the following are appropriate asymmetric SIGNATURE algorithms? "
            "(Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "RSA",
                "correct": True,
                "rationale": (
                    "Correct. RSA can be used for both encryption and digital signatures, "
                    "making it a valid asymmetric signature algorithm."
                ),
            },
            {
                "id": "b",
                "text": "ECDSA",
                "correct": True,
                "rationale": (
                    "Correct. ECDSA (Elliptic Curve Digital Signature Algorithm) is "
                    "purpose-built for generating digital signatures."
                ),
            },
            {
                "id": "c",
                "text": "Diffie-Hellman (DH)",
                "correct": False,
                "rationale": (
                    "Incorrect. DH is a key-exchange protocol used to establish a shared "
                    "secret between two parties; it is not designed to produce digital "
                    "signatures."
                ),
            },
            {
                "id": "d",
                "text": "AES",
                "correct": False,
                "rationale": (
                    "Incorrect. AES is a symmetric encryption algorithm used for bulk data "
                    "confidentiality; it is not asymmetric and cannot produce a digital "
                    "signature."
                ),
            },
            {
                "id": "e",
                "text": "ECDH",
                "correct": False,
                "rationale": (
                    "Incorrect. ECDH (Elliptic Curve Diffie-Hellman) is a key-exchange "
                    "variant, analogous to DH, not a signature algorithm — it establishes "
                    "shared secrets, not signs data."
                ),
            },
        ],
        "explanation": (
            "RSA and ECDSA are asymmetric algorithms designed to produce digital "
            "signatures for non-repudiation, distinct from key-exchange-only protocols "
            "(DH, ECDH) and symmetric encryption (AES)."
        ),
    },
]

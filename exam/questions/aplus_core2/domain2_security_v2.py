"""
CompTIA A+ Core 2 (220-1202) — Domain 2: Security  (v2 expansion)
38 brand-new exam-quality questions covering objectives 2.1 through 2.10.
IDs: c2d2v2-001 through c2d2v2-038
"""

QUESTIONS = [
    # ── 2.1 Physical Security ────────────────────────────────────────────────
    {
        "id": "c2d2v2-001",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Physical security",
        "stem": (
            "A financial institution hosts a server room inside a larger office floor. "
            "The server room door uses a numeric keypad lock. An attacker watches from "
            "a nearby desk as a technician types the six-digit code and then enters the "
            "room. Which attack technique has been used, and what control would BEST "
            "prevent it?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Shoulder surfing; install a privacy screen/shield around the keypad and enforce code-entry awareness training",
                "correct": True,
                "rationale": (
                    "Correct. Shoulder surfing is observing credentials or PINs by watching "
                    "from a distance or angle. Privacy shields on keypads and awareness "
                    "training (checking surroundings before entering codes) are the targeted "
                    "preventive controls."
                ),
            },
            {
                "id": "b",
                "text": "Tailgating; implement a mantrap so only one person enters per code entry",
                "correct": False,
                "rationale": (
                    "Incorrect. The attacker observed the code — they have not yet followed "
                    "anyone through the door. The attack is shoulder surfing (credential "
                    "observation). A mantrap prevents unauthorized physical entry after "
                    "a credential is already known."
                ),
            },
            {
                "id": "c",
                "text": "Vishing; enforce a callback verification policy for all remote access requests",
                "correct": False,
                "rationale": (
                    "Incorrect. Vishing is voice-based social engineering over a phone call. "
                    "The scenario is purely physical — visual observation of a PIN being "
                    "entered."
                ),
            },
            {
                "id": "d",
                "text": "Dumpster diving; shred all printed keypad codes before disposal",
                "correct": False,
                "rationale": (
                    "Incorrect. Dumpster diving recovers discarded physical documents. "
                    "Observing someone type a code in real time is shoulder surfing, "
                    "not dumpster diving."
                ),
            },
        ],
        "explanation": (
            "Shoulder surfing targets PINs, passwords, or codes through direct visual "
            "observation. Countermeasures include physical privacy shields on keypads, "
            "baffles that narrow the viewing angle, and user training to block the keypad "
            "with their body. Mantraps address tailgating, which is a different vector."
        ),
    },
    {
        "id": "c2d2v2-002",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Physical security",
        "stem": (
            "A retail chain's point-of-sale terminals are unattended at closing time. "
            "Management wants to prevent physical removal of the terminals without "
            "adding network-level controls. Which physical security control is MOST "
            "appropriate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Cable locks anchoring each terminal to the counter",
                "correct": True,
                "rationale": (
                    "Correct. Cable locks (equipment locks) directly prevent physical "
                    "removal of hardware by tethering devices to an immovable surface. "
                    "They are the appropriate preventive physical control for device theft."
                ),
            },
            {
                "id": "b",
                "text": "Geofencing the terminals via MDM",
                "correct": False,
                "rationale": (
                    "Incorrect. Geofencing triggers alerts or locks when a device leaves "
                    "a defined geographic area — a detective/reactive control, not a "
                    "physical preventive one. It does not stop the terminal from being "
                    "physically taken."
                ),
            },
            {
                "id": "c",
                "text": "Configure full-disk encryption on the terminals",
                "correct": False,
                "rationale": (
                    "Incorrect. Encryption protects data confidentiality if a device is "
                    "stolen but does not prevent the hardware from being physically removed. "
                    "The requirement is to prevent removal, not only protect data."
                ),
            },
            {
                "id": "d",
                "text": "Place a security guard at each terminal overnight",
                "correct": False,
                "rationale": (
                    "Incorrect. A security guard can deter or respond to theft but is not "
                    "a cost-effective, always-on physical control for this scenario. Cable "
                    "locks provide passive, continuous prevention."
                ),
            },
        ],
        "explanation": (
            "Equipment cable locks are the direct physical control for preventing device "
            "removal. Encryption protects data post-theft. Geofencing detects after removal. "
            "Guards are expensive and not continuously reliable. For unattended hardware "
            "security, cable locks are the exam-tested answer."
        ),
    },
    {
        "id": "c2d2v2-003",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Physical security",
        "stem": (
            "A company badges its employees for building access but notices contractors "
            "are sometimes let in by employees holding the door open as a courtesy. "
            "Which COMBINATION of controls BEST addresses this vulnerability?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Access control vestibule (mantrap) plus security awareness training on tailgating policy",
                "correct": True,
                "rationale": (
                    "Correct. A mantrap (access control vestibule) is the technical preventive "
                    "control that physically stops more than one person from entering per "
                    "badge swipe. Security awareness training addresses the human courtesy "
                    "behavior that enables tailgating. Both together form defense-in-depth."
                ),
            },
            {
                "id": "b",
                "text": "CCTV cameras at each entrance plus a motion sensor alarm",
                "correct": False,
                "rationale": (
                    "Incorrect. Both cameras and motion alarms are detective/reactive controls; "
                    "they record or alert after the tailgating occurs but do not prevent the "
                    "unauthorized person from entering in the first place."
                ),
            },
            {
                "id": "c",
                "text": "Installing bollards at building entrances",
                "correct": False,
                "rationale": (
                    "Incorrect. Bollards are designed to stop vehicle ramming of the "
                    "building's exterior. They do not address pedestrian tailgating through "
                    "badge-controlled doors."
                ),
            },
            {
                "id": "d",
                "text": "Issuing visitor badges that expire at end of day",
                "correct": False,
                "rationale": (
                    "Incorrect. Visitor badges track who should be in the building but "
                    "do not prevent an employee from physically holding a door for someone. "
                    "The root cause is the human behavior at controlled doors, addressed "
                    "by a mantrap and training."
                ),
            },
        ],
        "explanation": (
            "Tailgating (piggybacking) combines a technical failure (no mantrap) with a "
            "human failure (courtesy door-holding). The most complete solution layers a "
            "mantrap (prevents physical bypass) with security awareness training (changes "
            "the behavior enabling the attack)."
        ),
    },
    # ── 2.2 Logical Security ─────────────────────────────────────────────────
    {
        "id": "c2d2v2-004",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Logical security & Active Directory",
        "stem": (
            "A hospital IT policy requires that no single nurse can both administer a "
            "controlled substance AND document its administration in the EHR system "
            "without a second nurse verifying. Which security principle does this policy "
            "implement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Separation of duties",
                "correct": True,
                "rationale": (
                    "Correct. Separation of duties (SoD) requires that critical tasks be "
                    "divided among multiple individuals so that no one person can complete "
                    "a sensitive process alone — reducing fraud and error risk. Requiring "
                    "two nurses for controlled substance administration and documentation "
                    "is a textbook SoD implementation."
                ),
            },
            {
                "id": "b",
                "text": "Principle of least privilege",
                "correct": False,
                "rationale": (
                    "Incorrect. Least privilege restricts each user to the minimum access "
                    "needed for their role. The scenario is about dividing a process between "
                    "two people, which is separation of duties, not a permission-restriction "
                    "principle."
                ),
            },
            {
                "id": "c",
                "text": "Account lockout policy",
                "correct": False,
                "rationale": (
                    "Incorrect. Account lockout policies disable accounts after failed "
                    "authentication attempts. They have no relationship to the workflow "
                    "division described."
                ),
            },
            {
                "id": "d",
                "text": "Mandatory access control (MAC)",
                "correct": False,
                "rationale": (
                    "Incorrect. MAC is a classification-based access model enforced by the "
                    "system (e.g., government security labels). The scenario describes a "
                    "workflow control requiring two people, which is separation of duties."
                ),
            },
        ],
        "explanation": (
            "Separation of duties ensures that critical, sensitive, or fraud-prone processes "
            "require involvement from more than one individual. This limits the ability of "
            "a single actor to commit and conceal errors or malfeasance. Least privilege "
            "restricts what a single person can access; SoD restricts what one person can "
            "accomplish alone."
        ),
    },
    {
        "id": "c2d2v2-005",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Logical security & Active Directory",
        "stem": (
            "An IT administrator wants to ensure that when a user in Active Directory is "
            "disabled after resignation, that account can no longer authenticate to domain "
            "resources, but the account's group memberships and settings are preserved for "
            "auditing. Which AD action accomplishes this without permanently deleting the account?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Disable the AD account",
                "correct": True,
                "rationale": (
                    "Correct. Disabling an AD account immediately prevents authentication "
                    "while retaining all account attributes, group memberships, and history "
                    "for audit or potential reactivation. This is the standard off-boarding "
                    "action before eventual deletion after a retention period."
                ),
            },
            {
                "id": "b",
                "text": "Remove the account from all security groups",
                "correct": False,
                "rationale": (
                    "Incorrect. Removing group memberships revokes access to group-controlled "
                    "resources but the account itself remains enabled. A determined individual "
                    "with the credentials could still log in with whatever default user rights "
                    "remain. Disabling the account is the correct action."
                ),
            },
            {
                "id": "c",
                "text": "Delete the account from Active Directory",
                "correct": False,
                "rationale": (
                    "Incorrect. Deleting the account prevents authentication but also "
                    "destroys the account attributes, group membership history, and SID, "
                    "which are needed for audit trails. Deletion is typically deferred; "
                    "disabling is the immediate action."
                ),
            },
            {
                "id": "d",
                "text": "Reset the account password to a random string",
                "correct": False,
                "rationale": (
                    "Incorrect. Resetting the password prevents the former employee from "
                    "using their known credentials, but the account remains active. If "
                    "the former employee has another authentication mechanism (cached "
                    "credentials, smart card), they could still log in."
                ),
            },
        ],
        "explanation": (
            "Disabling an Active Directory account is the immediate step when an employee "
            "leaves. It blocks all authentication instantly while preserving account data "
            "for compliance and audit purposes. Full deletion is typically done after a "
            "defined retention period (e.g., 30–90 days) following verification that no "
            "resources depend on the account's SID."
        ),
    },
    {
        "id": "c2d2v2-006",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Logical security & Active Directory",
        "stem": (
            "A company uses a software token app on employees' smartphones for VPN MFA. "
            "A new employee asks why the six-digit code changes every 30 seconds. "
            "Which technology correctly explains this behavior?"
        ),
        "options": [
            {
                "id": "a",
                "text": "TOTP (Time-based One-Time Password) derives the code from the shared secret and the current time interval",
                "correct": True,
                "rationale": (
                    "Correct. TOTP (RFC 6238) generates a code by hashing a shared secret "
                    "combined with the current Unix time divided into 30-second windows. "
                    "Both the server and the authenticator app compute the same value "
                    "independently, requiring no network communication."
                ),
            },
            {
                "id": "b",
                "text": "HOTP (HMAC-based One-Time Password) derives the code from a counter that increments every 30 seconds on the server",
                "correct": False,
                "rationale": (
                    "Incorrect. HOTP uses an event counter (incremented each time a code "
                    "is generated or validated), not a time interval. HOTP codes do not "
                    "expire on a fixed 30-second clock — they expire when used or when "
                    "the counter advances."
                ),
            },
            {
                "id": "c",
                "text": "The VPN server pushes a new code to the app every 30 seconds via an encrypted channel",
                "correct": False,
                "rationale": (
                    "Incorrect. TOTP apps generate codes locally without any server "
                    "push. The app and server share a pre-provisioned secret and "
                    "independently compute the same value based on time. No network "
                    "connectivity is needed for code generation."
                ),
            },
            {
                "id": "d",
                "text": "The SMS gateway sends a new one-time code to the app every 30 seconds",
                "correct": False,
                "rationale": (
                    "Incorrect. Authenticator apps generate codes locally using TOTP; "
                    "they do not receive codes via SMS. SMS OTP is a separate authentication "
                    "mechanism and is not used by standard TOTP authenticator apps."
                ),
            },
        ],
        "explanation": (
            "TOTP (RFC 6238) is a time-synchronized OTP algorithm. A shared secret is "
            "provisioned once (typically via QR code). Each 30-second window, both the "
            "authenticator app and the server compute HMAC-SHA1(secret, floor(time/30)). "
            "HOTP uses an event counter instead of time. TOTP codes are valid for the "
            "current window and often one adjacent window to account for clock drift."
        ),
    },
    {
        "id": "c2d2v2-007",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Logical security & Active Directory",
        "stem": (
            "A help desk technician logs in as a local administrator on every workstation "
            "he touches to speed up troubleshooting. A security auditor flags this as a "
            "policy violation. Which risk does this practice MOST directly create?"
        ),
        "options": [
            {
                "id": "a",
                "text": "If any workstation runs malicious code while the technician is logged in as admin, the malware inherits full administrative rights on that system",
                "correct": True,
                "rationale": (
                    "Correct. Running with administrative privileges at all times means "
                    "any code executed during that session — including triggered malware — "
                    "runs with elevated rights. This violates least privilege and significantly "
                    "increases the blast radius of a compromise."
                ),
            },
            {
                "id": "b",
                "text": "The admin account password becomes cached on every workstation, creating credential exposure",
                "correct": False,
                "rationale": (
                    "Incorrect. While credential caching is a secondary risk, it is not "
                    "the PRIMARY concern CompTIA tests here. The main least-privilege "
                    "violation risk is that malware executed under an admin session gains "
                    "admin rights."
                ),
            },
            {
                "id": "c",
                "text": "The technician bypasses Group Policy Object enforcement on managed machines",
                "correct": False,
                "rationale": (
                    "Incorrect. Local admin access does not bypass GPOs applied at the domain "
                    "level. GPOs are enforced by the OS regardless of the logged-in account "
                    "type for domain-joined machines."
                ),
            },
            {
                "id": "d",
                "text": "UAC prompts are suppressed, slowing down the technician's workflow",
                "correct": False,
                "rationale": (
                    "Incorrect. UAC prompts being bypassed is a symptom of running as admin, "
                    "but this actually speeds up the technician's workflow (fewer prompts) "
                    "rather than creating a risk. The security risk is the elevated privilege "
                    "exposure, not a workflow issue."
                ),
            },
        ],
        "explanation": (
            "The principle of least privilege requires that users — including IT staff — "
            "operate with the minimum permissions needed for their current task. Running "
            "as local admin for routine work means any process spawned in that session "
            "(browser, email attachment, script) inherits admin rights. Best practice is "
            "to use a standard account for daily tasks and elevate via UAC only when needed."
        ),
    },
    # ── 2.3 Wireless Security ────────────────────────────────────────────────
    {
        "id": "c2d2v2-008",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Wireless security protocols",
        "stem": (
            "A technician audits a coffee shop's free Wi-Fi and finds the router is "
            "broadcasting its SSID, uses an open (no encryption) network, and the "
            "admin web interface is reachable from connected clients. Which change "
            "provides the MOST security improvement for customers connecting to this network?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Enable WPA2 or WPA3 encryption with a shared passphrase",
                "correct": True,
                "rationale": (
                    "Correct. Enabling WPA2/WPA3 encryption protects the wireless "
                    "traffic between clients and the AP from eavesdropping. An open "
                    "network allows anyone in range to capture all traffic in plaintext. "
                    "Encryption is the most impactful single improvement for customer "
                    "data security."
                ),
            },
            {
                "id": "b",
                "text": "Disable SSID broadcast so the network is hidden",
                "correct": False,
                "rationale": (
                    "Incorrect. Hiding the SSID is security through obscurity — tools "
                    "can still discover hidden SSIDs through passive monitoring. It "
                    "does not encrypt traffic at all; customers connecting to a 'hidden' "
                    "open network are still fully exposed to eavesdropping."
                ),
            },
            {
                "id": "c",
                "text": "Change the admin password on the router",
                "correct": False,
                "rationale": (
                    "Incorrect. Changing the admin password hardens the router management "
                    "interface but does nothing to protect traffic between customers and "
                    "the AP. The highest-impact customer-facing improvement is encryption."
                ),
            },
            {
                "id": "d",
                "text": "Enable MAC address filtering to allow only known device MACs",
                "correct": False,
                "rationale": (
                    "Incorrect. MAC filtering is impractical for a public coffee shop "
                    "with constantly changing customers. Furthermore, MAC addresses "
                    "are transmitted in plaintext and are trivially spoofed, making "
                    "this control easily bypassed."
                ),
            },
        ],
        "explanation": (
            "An open (unencrypted) Wi-Fi network allows passive packet capture of all "
            "customer traffic. Enabling WPA2 or WPA3 with a PSK is the single largest "
            "security improvement. MAC filtering is impractical and easily defeated. SSID "
            "hiding provides no encryption benefit. Admin password changes are important "
            "but affect only router management, not customer traffic."
        ),
    },
    {
        "id": "c2d2v2-009",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Wireless security protocols",
        "stem": (
            "A company's WPA2-Enterprise deployment uses PEAP-MSCHAPv2 as the inner EAP "
            "method. A security engineer notes that the wireless clients are not validating "
            "the RADIUS server's certificate. Which attack does this misconfiguration "
            "enable?"
        ),
        "options": [
            {
                "id": "a",
                "text": "An evil twin attack where a rogue RADIUS server captures MSCHAPv2 credentials from unsuspecting clients",
                "correct": True,
                "rationale": (
                    "Correct. If clients do not validate the RADIUS server certificate, "
                    "a rogue AP paired with a rogue RADIUS server (evil twin) can complete "
                    "the PEAP tunnel and receive the client's MSCHAPv2 credentials. Without "
                    "server certificate validation, clients cannot distinguish the real "
                    "RADIUS server from an attacker's server."
                ),
            },
            {
                "id": "b",
                "text": "A deauthentication (DoS) flood attack against associated clients",
                "correct": False,
                "rationale": (
                    "Incorrect. Deauth flooding is a Wi-Fi denial-of-service attack that "
                    "disconnects clients by spoofing management frames. It is unrelated "
                    "to RADIUS certificate validation and does not capture credentials."
                ),
            },
            {
                "id": "c",
                "text": "A WPS PIN brute-force attack bypassing WPA2-Enterprise",
                "correct": False,
                "rationale": (
                    "Incorrect. WPS PIN attacks target WPS (Wi-Fi Protected Setup) on "
                    "PSK networks. WPA2-Enterprise does not use WPS. The vulnerability "
                    "here is in the EAP authentication path, not WPS."
                ),
            },
            {
                "id": "d",
                "text": "A replay attack where captured TOTP codes are reused on the RADIUS server",
                "correct": False,
                "rationale": (
                    "Incorrect. TOTP replay attacks are relevant to VPN or web authentication, "
                    "not PEAP-MSCHAPv2 inner authentication. MSCHAPv2 uses challenge-response, "
                    "not time-based tokens."
                ),
            },
        ],
        "explanation": (
            "PEAP wraps the inner authentication method (MSCHAPv2) inside a TLS tunnel. "
            "If clients skip server certificate verification, they cannot confirm the "
            "TLS tunnel terminates at the legitimate RADIUS server. An attacker's rogue "
            "AP + RADIUS server can complete PEAP, exposing MSCHAPv2 credentials that "
            "are then vulnerable to offline dictionary attacks. Fix: configure clients "
            "to validate the RADIUS server certificate and pin to the correct CA."
        ),
    },
    {
        "id": "c2d2v2-010",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Wireless security protocols",
        "stem": (
            "An administrator is setting up guest Wi-Fi at a branch office. Guests should "
            "be able to reach the internet but must be completely isolated from the "
            "corporate LAN segment. Which feature of a modern SOHO/enterprise router "
            "achieves this isolation?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Guest network VLAN with inter-VLAN routing blocked between the guest and corporate segments",
                "correct": True,
                "rationale": (
                    "Correct. A guest network VLAN logically separates guest traffic "
                    "from corporate traffic. Blocking inter-VLAN routing (or enforcing "
                    "ACLs between segments) ensures guests can reach the internet "
                    "gateway but cannot communicate with corporate hosts. This is "
                    "standard segmentation practice."
                ),
            },
            {
                "id": "b",
                "text": "Disable SSID broadcast on the corporate network only",
                "correct": False,
                "rationale": (
                    "Incorrect. Hiding the corporate SSID does not isolate the guest "
                    "segment from the corporate LAN at the network layer. A guest device "
                    "could still potentially reach corporate hosts if no routing/firewall "
                    "separation exists."
                ),
            },
            {
                "id": "c",
                "text": "Enable WPA3 on the guest network",
                "correct": False,
                "rationale": (
                    "Incorrect. WPA3 improves the security of the wireless connection "
                    "itself but does not create LAN-level isolation between the guest "
                    "network and the corporate network once traffic reaches the wired "
                    "infrastructure."
                ),
            },
            {
                "id": "d",
                "text": "Assign guest devices a different DHCP scope only",
                "correct": False,
                "rationale": (
                    "Incorrect. Using a different DHCP scope (IP subnet) for guests "
                    "is a component of segmentation, but without enforced routing "
                    "restrictions or VLANs, a guest could still route to the corporate "
                    "subnet. VLAN separation with blocked inter-VLAN routing provides "
                    "actual isolation."
                ),
            },
        ],
        "explanation": (
            "Guest network isolation requires both a separate VLAN (logical separation) "
            "and blocked inter-VLAN routing (enforcement layer). Many consumer/SOHO routers "
            "implement this automatically with a 'guest network' feature. On enterprise "
            "gear, separate VLANs with ACLs between them achieve the same result. "
            "Encryption and SSID settings do not provide LAN isolation."
        ),
    },
    # ── 2.4 Malware ──────────────────────────────────────────────────────────
    {
        "id": "c2d2v2-011",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Malware types & removal",
        "stem": (
            "A user receives a pop-up while browsing that states: 'CRITICAL VIRUS DETECTED! "
            "Your PC is infected with 47 viruses. Click here to purchase SecurityShield Pro "
            "to remove them immediately.' The user's legitimate antivirus shows no threats. "
            "Which malware type does this pop-up represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Scareware (rogue antivirus)",
                "correct": True,
                "rationale": (
                    "Correct. Scareware presents false security alerts to frighten users "
                    "into purchasing fake antivirus software or clicking a malicious link. "
                    "Rogue antivirus is the specific category of scareware that mimics "
                    "legitimate security software."
                ),
            },
            {
                "id": "b",
                "text": "Ransomware",
                "correct": False,
                "rationale": (
                    "Incorrect. Ransomware encrypts files and demands payment for decryption. "
                    "The scenario shows a fake alert with no actual encryption or real files "
                    "being held hostage. The goal is to deceive the user into purchasing "
                    "fake software, not to pay for encrypted data recovery."
                ),
            },
            {
                "id": "c",
                "text": "Spyware",
                "correct": False,
                "rationale": (
                    "Incorrect. Spyware silently collects user data (keystrokes, browsing "
                    "habits, credentials) without the user's knowledge. It does not generate "
                    "alarming pop-up messages or attempt to sell software."
                ),
            },
            {
                "id": "d",
                "text": "Adware",
                "correct": False,
                "rationale": (
                    "Incorrect. Adware displays advertising (often browser redirects and "
                    "pop-up ads) to generate revenue. While scareware may look like an ad, "
                    "the specific pattern — fake threat alert urging purchase of security "
                    "software — is scareware/rogue antivirus, a more precise classification."
                ),
            },
        ],
        "explanation": (
            "Scareware manipulates users through fear by displaying false security warnings. "
            "Rogue antivirus is a subcategory that mimics legitimate security tools to collect "
            "payment or install actual malware. Ransomware involves real encryption and "
            "extortion. Spyware operates silently. The pop-up attempting to sell fake software "
            "is the defining scareware characteristic."
        ),
    },
    {
        "id": "c2d2v2-012",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Malware types & removal",
        "stem": (
            "After removing malware from a Windows 10 workstation, a technician wants "
            "to prevent the malware from re-infecting through existing System Restore "
            "points, then verify the system is clean going forward. Which TWO-STEP "
            "sequence from the CompTIA malware removal process is CORRECT for this "
            "phase?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Re-enable System Restore and create a new clean restore point; then schedule recurring antivirus scans with updated definitions",
                "correct": True,
                "rationale": (
                    "Correct. After successful remediation (step 4), the process calls for: "
                    "(5) schedule scans / update definitions, then (6) re-enable System Restore "
                    "and create a new clean restore point. The question asks about the post-"
                    "remediation phase — re-enabling System Restore with a clean point and "
                    "scheduling scans are the correct sequential actions at this stage."
                ),
            },
            {
                "id": "b",
                "text": "Quarantine the system on the network; then disable System Restore",
                "correct": False,
                "rationale": (
                    "Incorrect. Quarantine (step 2) and disabling System Restore (step 3) "
                    "are PRE-remediation steps. The question asks about post-removal actions "
                    "to prevent re-infection and verify cleanliness."
                ),
            },
            {
                "id": "c",
                "text": "Educate the end user first; then re-enable System Restore",
                "correct": False,
                "rationale": (
                    "Incorrect. End user education is step 7 — the final step. Re-enabling "
                    "System Restore (step 6) comes before end user education. The order "
                    "matters on the CompTIA exam."
                ),
            },
            {
                "id": "d",
                "text": "Run the antivirus scan again; then identify and research malware symptoms",
                "correct": False,
                "rationale": (
                    "Incorrect. Re-identifying and researching symptoms (step 1) is a "
                    "pre-removal step. Running another scan is reasonable but the CompTIA "
                    "process puts scheduling/updating (step 5) and restoring System Restore "
                    "(step 6) as the post-remediation sequence, not another identification loop."
                ),
            },
        ],
        "explanation": (
            "CompTIA malware removal step sequence post-remediation: "
            "(4) Remediate (scan/remove) → "
            "(5) Schedule scans, update definitions → "
            "(6) Re-enable System Restore, create new clean restore point → "
            "(7) Educate end user. "
            "Disabling System Restore before removal prevents malware hiding in restore "
            "points; re-enabling after with a new point ensures clean recovery capability."
        ),
    },
    {
        "id": "c2d2v2-013",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Malware types & removal",
        "stem": (
            "An organization's DNS server logs show that workstations on the network are "
            "regularly resolving unusual domain names that follow a pattern of randomly "
            "generated subdomain strings (e.g., xk3m9pqz.example.com). No data exfiltration "
            "is visible on traditional network monitors. Which malware behavior does this "
            "MOST likely indicate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "DNS tunneling used for command-and-control (C2) communication by a botnet or RAT",
                "correct": True,
                "rationale": (
                    "Correct. DNS tunneling encodes data or C2 commands within DNS query "
                    "and response packets. Because DNS traffic is rarely blocked at the "
                    "perimeter and not inspected by basic monitors, it is a stealthy "
                    "exfiltration and C2 channel. Random subdomain patterns are a "
                    "signature of DNS-based C2 or data exfiltration."
                ),
            },
            {
                "id": "b",
                "text": "A cryptominer generating new wallet addresses for each mining connection",
                "correct": False,
                "rationale": (
                    "Incorrect. Cryptominers connect to mining pools over standard protocols "
                    "(TCP/Stratum). While they may query unusual domains, the specific pattern "
                    "of high-frequency random subdomain queries is characteristic of DNS "
                    "tunneling/C2, not crypto mining."
                ),
            },
            {
                "id": "c",
                "text": "A keylogger periodically sending captured keystrokes via email",
                "correct": False,
                "rationale": (
                    "Incorrect. Keyloggers typically exfiltrate via SMTP or HTTP, not through "
                    "random DNS queries. The random subdomain pattern in DNS logs is not "
                    "consistent with keylogger email-based exfiltration."
                ),
            },
            {
                "id": "d",
                "text": "A worm scanning the network for new hosts to infect via DNS lookups",
                "correct": False,
                "rationale": (
                    "Incorrect. Worm propagation via network scanning typically involves "
                    "port scans (TCP/UDP) to find vulnerable services, not high-volume "
                    "random subdomain DNS queries. DNS scanning for hosts uses normal "
                    "reverse lookup patterns, not randomized subdomains."
                ),
            },
        ],
        "explanation": (
            "DNS tunneling abuses the DNS protocol to carry arbitrary data (C2 instructions, "
            "exfiltrated content) by encoding it in subdomain strings of DNS queries. "
            "Because DNS is needed for normal operations and rarely deeply inspected, "
            "this technique is highly evasive. Detection relies on monitoring for abnormal "
            "query frequency, entropy of subdomain strings, and long TXT record responses. "
            "Tools like Iodine implement DNS tunneling; C2 frameworks like Cobalt Strike "
            "support DNS beaconing."
        ),
    },
    {
        "id": "c2d2v2-014",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Malware types & removal",
        "stem": (
            "A user's files have been encrypted and a ransom note is displayed demanding "
            "payment in cryptocurrency within 72 hours for the decryption key. The "
            "technician confirms the infection is ransomware. According to CompTIA "
            "best practices, what should the technician do IMMEDIATELY after identifying "
            "the ransomware?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Quarantine (isolate) the infected system from the network",
                "correct": True,
                "rationale": (
                    "Correct. Step 2 in the CompTIA malware removal process is quarantine. "
                    "Ransomware can spread laterally across network shares and mapped drives. "
                    "Immediate network isolation contains the infection and prevents it from "
                    "encrypting additional systems or network storage."
                ),
            },
            {
                "id": "b",
                "text": "Pay the ransom immediately to obtain the decryption key",
                "correct": False,
                "rationale": (
                    "Incorrect. Paying the ransom is not a CompTIA-recommended action and "
                    "does not guarantee key delivery. It also funds criminal operations and "
                    "marks the victim as willing to pay. Isolation and recovery from backup "
                    "are the preferred responses."
                ),
            },
            {
                "id": "c",
                "text": "Run a full antivirus scan from within the infected OS",
                "correct": False,
                "rationale": (
                    "Incorrect. Running an AV scan without first quarantining allows the "
                    "ransomware to continue encrypting files, potentially spread over the "
                    "network, and the scan itself may be incomplete if the ransomware is "
                    "still active. Quarantine must come first."
                ),
            },
            {
                "id": "d",
                "text": "Restore files from the most recent backup without quarantining first",
                "correct": False,
                "rationale": (
                    "Incorrect. Restoring files without quarantine would allow active "
                    "ransomware to immediately re-encrypt the restored files. Isolation "
                    "is always the prerequisite before any recovery action."
                ),
            },
        ],
        "explanation": (
            "CompTIA's malware removal process step 2 is quarantine: disconnect the system "
            "from the network to contain spread. Ransomware actively propagates to network "
            "shares and connected drives. Paying ransom is never recommended. Scanning or "
            "restoring without quarantine allows the active infection to continue or "
            "re-encrypt data immediately."
        ),
    },
    {
        "id": "c2d2v2-015",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Malware types & removal",
        "stem": (
            "A technician discovers a Windows workstation infected with a polymorphic "
            "virus. Which TWO characteristics of a polymorphic virus make it harder "
            "to detect than a standard virus? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "It mutates its code with each replication, changing its signature so static AV signature scans may miss it",
                "correct": True,
                "rationale": (
                    "Correct. Polymorphic malware rewrites its own code each time it "
                    "replicates, altering the binary signature. Signature-based antivirus "
                    "that relies on matching known byte patterns cannot detect variants "
                    "it has never seen."
                ),
            },
            {
                "id": "b",
                "text": "It uses a mutation engine to encrypt its payload differently on each infection while retaining the same malicious function",
                "correct": True,
                "rationale": (
                    "Correct. The mutation engine changes the encryption/obfuscation "
                    "of the payload each generation. The functional behavior (the malicious "
                    "code) remains the same, but the binary representation changes — "
                    "evading signature detection."
                ),
            },
            {
                "id": "c",
                "text": "It spreads autonomously across the network without user interaction",
                "correct": False,
                "rationale": (
                    "Incorrect. Autonomous network propagation without user interaction "
                    "is the characteristic of a worm, not specifically of a polymorphic "
                    "virus. A virus attaches to files and requires a host file to spread."
                ),
            },
            {
                "id": "d",
                "text": "It encrypts user files and demands a ransom for the decryption key",
                "correct": False,
                "rationale": (
                    "Incorrect. Encrypting user files for ransom is ransomware behavior. "
                    "A polymorphic virus mutates its own code structure; it does not "
                    "necessarily encrypt user data for extortion purposes."
                ),
            },
        ],
        "explanation": (
            "Polymorphic malware defeats signature-based detection by continuously mutating "
            "its binary representation while preserving its payload behavior. Each generation "
            "has a different signature hash. Heuristic and behavior-based detection engines "
            "are more effective against polymorphic threats because they analyze behavior "
            "rather than static byte patterns."
        ),
    },
    # ── 2.5 Social Engineering / Attacks ─────────────────────────────────────
    {
        "id": "c2d2v2-016",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Social engineering & attacks",
        "stem": (
            "An attacker calls a company's receptionist, claims to be from the IT helpdesk, "
            "and says there is an urgent security incident requiring the receptionist's "
            "credentials to fix the problem remotely. The receptionist provides the "
            "credentials. This attack MOST specifically illustrates which concept?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Pretexting",
                "correct": True,
                "rationale": (
                    "Correct. Pretexting is the creation of a fabricated scenario (a pretext) "
                    "to manipulate a target into divulging information or performing an action. "
                    "The attacker invented a false IT identity and an urgent situation to "
                    "extract credentials — this is the defining characteristic of pretexting."
                ),
            },
            {
                "id": "b",
                "text": "Vishing",
                "correct": False,
                "rationale": (
                    "Incorrect. Vishing is the medium (voice/phone call), not the technique. "
                    "While this attack is delivered via phone (vishing), the technique being "
                    "tested is the fabricated scenario used to manipulate the victim, "
                    "which is pretexting. On the CompTIA exam, pretexting is the more "
                    "precise answer when a false scenario is created."
                ),
            },
            {
                "id": "c",
                "text": "Spear phishing",
                "correct": False,
                "rationale": (
                    "Incorrect. Spear phishing is a targeted email-based attack. This "
                    "scenario uses a phone call, and the specific technique — building "
                    "a false credibility scenario — is pretexting."
                ),
            },
            {
                "id": "d",
                "text": "Tailgating",
                "correct": False,
                "rationale": (
                    "Incorrect. Tailgating is a physical access attack where an unauthorized "
                    "person follows an authorized person through a secure door. No physical "
                    "access is involved in this scenario."
                ),
            },
        ],
        "explanation": (
            "Pretexting involves creating a fictional scenario (the 'pretext') that appears "
            "plausible and compelling enough to manipulate a target into disclosing information "
            "or performing an action. While the delivery mechanism here is a phone call "
            "(vishing), 'pretexting' is the CompTIA term for the fabrication of a false "
            "identity/scenario. Both terms may appear in answers — pretexting is the "
            "technique; vishing is the channel."
        ),
    },
    {
        "id": "c2d2v2-017",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Social engineering & attacks",
        "stem": (
            "A user receives an email that appears to come from their bank with the "
            "From: address 'no-reply@firstnational-secure.com' (not the bank's real domain "
            "firstnational.com). The email contains a link to a login page with a valid "
            "padlock icon. Which attack technique does this represent, and what should the "
            "user do?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Phishing using a lookalike domain; the user should verify the sender's full domain and navigate to the bank's real URL manually rather than clicking the link",
                "correct": True,
                "rationale": (
                    "Correct. This is a phishing email using a spoofed lookalike domain "
                    "('firstnational-secure.com' vs 'firstnational.com'). The padlock icon "
                    "only indicates TLS encryption — attackers can obtain certificates for "
                    "their fake domains too. The user should manually type the bank's "
                    "known URL rather than clicking the email link."
                ),
            },
            {
                "id": "b",
                "text": "Legitimate bank email; the padlock icon confirms the site is the real bank",
                "correct": False,
                "rationale": (
                    "Incorrect. The padlock (TLS certificate) confirms the connection is "
                    "encrypted and the domain name matches the certificate — but it only "
                    "authenticates 'firstnational-secure.com', NOT the real bank. Attackers "
                    "routinely obtain TLS certificates for lookalike phishing domains."
                ),
            },
            {
                "id": "c",
                "text": "Vishing attack conducted via email",
                "correct": False,
                "rationale": (
                    "Incorrect. Vishing is voice phishing conducted over telephone calls. "
                    "Email-based deception using lookalike domains is phishing (or spear "
                    "phishing if targeted)."
                ),
            },
            {
                "id": "d",
                "text": "On-path attack intercepting the bank's real email",
                "correct": False,
                "rationale": (
                    "Incorrect. An on-path (MitM) attack intercepts and potentially alters "
                    "traffic between two parties. The scenario describes a spoofed email "
                    "originating from the attacker's server, not intercepted bank email."
                ),
            },
        ],
        "explanation": (
            "Lookalike (typosquat) domains are a common phishing technique. TLS/padlock "
            "status only proves the connection is encrypted with a certificate matching "
            "the URL displayed — not that the URL is the legitimate organization. Users "
            "must verify the full domain name, not just look for the padlock. Navigating "
            "directly to the bank's known URL eliminates link-click risks."
        ),
    },
    {
        "id": "c2d2v2-018",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Social engineering & attacks",
        "stem": (
            "An attacker sends targeted SMS messages to employees claiming to be the IT "
            "department and asking them to click a link to reset their VPN password "
            "before end of business or lose access. Which specific attack type is this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Smishing",
                "correct": True,
                "rationale": (
                    "Correct. Smishing (SMS phishing) uses text messages as the phishing "
                    "vector. Attackers send deceptive SMS messages impersonating trusted "
                    "entities to trick victims into clicking links or providing credentials."
                ),
            },
            {
                "id": "b",
                "text": "Vishing",
                "correct": False,
                "rationale": (
                    "Incorrect. Vishing uses voice calls, not SMS text messages. While "
                    "both exploit the phone as a channel, vishing is voice-based and "
                    "smishing is SMS-based."
                ),
            },
            {
                "id": "c",
                "text": "Spear phishing",
                "correct": False,
                "rationale": (
                    "Incorrect. Spear phishing is a targeted email attack. While this "
                    "is targeted (employees), the delivery channel is SMS, which makes "
                    "it smishing. If the question mentioned email, spear phishing would "
                    "be the correct term."
                ),
            },
            {
                "id": "d",
                "text": "Whaling",
                "correct": False,
                "rationale": (
                    "Incorrect. Whaling specifically targets high-value executives (C-suite). "
                    "This attack is directed at general employees via SMS — the channel "
                    "and target profile identify it as smishing, not whaling."
                ),
            },
        ],
        "explanation": (
            "Phishing attack channels: email = phishing/spear phishing/whaling; "
            "voice/phone = vishing; SMS = smishing. Urgency ('reset by end of business') "
            "is a common social engineering pressure tactic used across all channels. "
            "The SMS delivery channel is the distinguishing characteristic that makes "
            "this smishing."
        ),
    },
    {
        "id": "c2d2v2-019",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Social engineering & attacks",
        "stem": (
            "A penetration tester drops several USB drives labeled 'Q3 Salary Data – "
            "Confidential' in the company parking lot. Within an hour, three employees "
            "have plugged the drives into their workstations. Which social engineering "
            "technique is the tester demonstrating?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Baiting",
                "correct": True,
                "rationale": (
                    "Correct. Baiting uses a physical lure (the labeled USB drive) to "
                    "entice victims into taking a security-compromising action "
                    "(plugging in an unknown drive). The attacker exploits human curiosity "
                    "or greed with a tempting label."
                ),
            },
            {
                "id": "b",
                "text": "Tailgating",
                "correct": False,
                "rationale": (
                    "Incorrect. Tailgating involves physically following someone through "
                    "a controlled entrance. No physical access to restricted areas is "
                    "involved; the attack vector is an untrusted USB drive."
                ),
            },
            {
                "id": "c",
                "text": "Dumpster diving",
                "correct": False,
                "rationale": (
                    "Incorrect. Dumpster diving recovers sensitive information from "
                    "discarded materials. The tester is planting drives to trick employees, "
                    "not searching through trash for information."
                ),
            },
            {
                "id": "d",
                "text": "Shoulder surfing",
                "correct": False,
                "rationale": (
                    "Incorrect. Shoulder surfing involves visually observing what someone "
                    "types or views. The scenario involves physical USB drives and human "
                    "curiosity exploitation, which is baiting."
                ),
            },
        ],
        "explanation": (
            "Baiting is a social engineering technique that uses physical or digital lures "
            "to manipulate victims. USB baiting (sometimes called 'USB drop attack') "
            "exploits human curiosity. A malicious USB drive can run AutoRun payloads, "
            "HID (BadUSB) attacks, or simply contain malware that executes when opened. "
            "Security awareness training should explicitly warn employees never to plug "
            "in unknown drives."
        ),
    },
    {
        "id": "c2d2v2-020",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Social engineering & attacks",
        "stem": (
            "An attacker gains access to a company's internal forum and posts a message "
            "that includes a malicious script. When other employees view the post in their "
            "browsers, the script runs and steals their session cookies. Which web "
            "application attack is this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Stored (persistent) cross-site scripting (XSS)",
                "correct": True,
                "rationale": (
                    "Correct. Stored XSS occurs when malicious script is permanently "
                    "saved in the application database (e.g., a forum post) and served "
                    "to all users who view that content. It executes in victims' browsers "
                    "in the context of the trusted site, enabling session cookie theft."
                ),
            },
            {
                "id": "b",
                "text": "SQL injection",
                "correct": False,
                "rationale": (
                    "Incorrect. SQL injection manipulates database queries through input "
                    "fields. The scenario involves script execution in victims' browsers "
                    "when viewing content, which is XSS — a client-side attack, not a "
                    "database manipulation attack."
                ),
            },
            {
                "id": "c",
                "text": "Reflected (non-persistent) cross-site scripting (XSS)",
                "correct": False,
                "rationale": (
                    "Incorrect. Reflected XSS requires each victim to click a specially "
                    "crafted link containing the malicious script, which the server "
                    "'reflects' back. In this scenario, the script is stored in the forum "
                    "post and executes for any user who views it — that is stored XSS."
                ),
            },
            {
                "id": "d",
                "text": "Cross-site request forgery (CSRF)",
                "correct": False,
                "rationale": (
                    "Incorrect. CSRF tricks a victim's browser into making unauthorized "
                    "state-changing requests (e.g., transfers) using the victim's existing "
                    "authenticated session — it exploits the site's trust of the user. "
                    "XSS exploits the user's trust of the site by injecting scripts. "
                    "The scenario describes script execution for session cookie theft, "
                    "which is XSS."
                ),
            },
        ],
        "explanation": (
            "XSS attack types: Stored (persistent) — script saved in database, serves to "
            "all visitors of the affected page. Reflected (non-persistent) — script in a "
            "URL parameter, reflected back to a single victim who clicks the malicious link. "
            "DOM-based — script manipulates the page's DOM on the client side. Session "
            "cookie theft via stored XSS is a classic attack. HttpOnly cookies and Content "
            "Security Policy (CSP) are key mitigations."
        ),
    },
    # ── 2.6 Windows OS Security Settings / NTFS ───────────────────────────────
    {
        "id": "c2d2v2-021",
        "domain": 2,
        "objective": "2.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "NTFS vs share permissions",
        "stem": (
            "UserA is a member of both the Accounting group (share permission: Change) "
            "and the Managers group (share permission: Read) on a shared folder. UserA's "
            "NTFS permission on the same folder is Read. UserA accesses the folder over "
            "the network. What is UserA's effective permission?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Read — the most restrictive combination of cumulative share permissions and NTFS permissions applies",
                "correct": True,
                "rationale": (
                    "Correct. Cumulative share permissions: Change + Read = Change "
                    "(most permissive of the combined group share permissions). NTFS: Read. "
                    "Over the network, effective = most restrictive of (cumulative share) vs "
                    "(NTFS) = most restrictive of Change vs Read = Read."
                ),
            },
            {
                "id": "b",
                "text": "Change — the most permissive share permission applies when the user belongs to multiple groups",
                "correct": False,
                "rationale": (
                    "Incorrect. Cumulative share permissions are indeed Change (the "
                    "combination of Change and Read), but the NTFS permissions must also "
                    "be intersected for network access. NTFS is Read, which is more "
                    "restrictive than Change, so the effective network permission is Read."
                ),
            },
            {
                "id": "c",
                "text": "Full Control — permissions from all groups are added together",
                "correct": False,
                "rationale": (
                    "Incorrect. NTFS and share permissions are not simply added together. "
                    "First, permissions within each system accumulate per group membership, "
                    "then the two permission systems are intersected (most restrictive wins) "
                    "for network access."
                ),
            },
            {
                "id": "d",
                "text": "No access — conflicting permissions between groups result in denial",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no explicit Deny in the scenario. Multiple Allow "
                    "permissions from different groups accumulate (most permissive among "
                    "them), then the share/NTFS intersection reduces to the most restrictive "
                    "allow — which is Read, not a denial."
                ),
            },
        ],
        "explanation": (
            "Step 1 — Cumulative share permissions: User is in Accounting (Change) AND "
            "Managers (Read). Multiple group shares accumulate to the most permissive: Change. "
            "Step 2 — Cumulative NTFS: Read only. "
            "Step 3 — Network effective = most restrictive of (Change) and (Read) = Read. "
            "Locally (logging in directly), only NTFS applies: Read. "
            "Explicit Deny always overrides Allow regardless of accumulation."
        ),
    },
    {
        "id": "c2d2v2-022",
        "domain": 2,
        "objective": "2.6",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "NTFS vs share permissions",
        "stem": (
            "A folder on an NTFS volume has the share permission 'Full Control' for "
            "Everyone. Within the folder, an individual file has explicit NTFS Deny Read "
            "for UserB. UserB attempts to access the file over the network. What happens?"
        ),
        "options": [
            {
                "id": "a",
                "text": "UserB is denied access — explicit NTFS Deny overrides all Allow permissions, including the Full Control share permission",
                "correct": True,
                "rationale": (
                    "Correct. An explicit Deny always overrides any Allow, in both NTFS "
                    "and share permission models. Even though the share grants Full Control "
                    "to Everyone, the NTFS explicit Deny Read for UserB takes precedence, "
                    "resulting in denial."
                ),
            },
            {
                "id": "b",
                "text": "UserB gets Full Control because the share permission overrides NTFS Deny when accessing over the network",
                "correct": False,
                "rationale": (
                    "Incorrect. Share permissions never override NTFS explicit Deny. "
                    "The 'most restrictive wins' rule for network access means explicit "
                    "Deny in either system results in denial, regardless of the other "
                    "system's Allow."
                ),
            },
            {
                "id": "c",
                "text": "UserB gets Read access because the Everyone share permission overrides the individual file NTFS setting",
                "correct": False,
                "rationale": (
                    "Incorrect. Share permissions grant access up to the share level; "
                    "they do not override NTFS explicit Deny. The explicit Deny Read "
                    "on the file's NTFS ACL takes precedence."
                ),
            },
            {
                "id": "d",
                "text": "UserB gets the permissions of the parent folder because the file inherits share permissions",
                "correct": False,
                "rationale": (
                    "Incorrect. Files inherit NTFS permissions from the parent folder by "
                    "default unless explicitly set otherwise, but an explicit NTFS Deny "
                    "set directly on the file is not an inherited permission — it is "
                    "explicit and overrides all Allow grants."
                ),
            },
        ],
        "explanation": (
            "NTFS Deny is absolute: an explicit Deny entry in an ACL overrides any Allow, "
            "whether from the same file's ACE, a parent folder, or the share permissions. "
            "The intersection of share and NTFS for network access always applies, and "
            "explicit Deny wins regardless of permissive share settings. This is a "
            "critical exam distinction."
        ),
    },
    {
        "id": "c2d2v2-023",
        "domain": 2,
        "objective": "2.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "NTFS vs share permissions",
        "stem": (
            "An administrator moves a folder from C:\\Data (NTFS volume) to D:\\Archive "
            "(a different NTFS volume). Before the move, the folder had custom NTFS "
            "permissions. After the move, a user reports they can no longer access it. "
            "What happened to the folder's NTFS permissions?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The folder inherited the permissions of the D:\\Archive destination folder, replacing the original custom permissions",
                "correct": True,
                "rationale": (
                    "Correct. Moving a folder to a DIFFERENT NTFS volume is functionally "
                    "a copy-then-delete operation. On copy, the object inherits the "
                    "destination folder's permissions. The original custom permissions "
                    "are not retained."
                ),
            },
            {
                "id": "b",
                "text": "The folder retained its original custom permissions because it was moved within NTFS",
                "correct": False,
                "rationale": (
                    "Incorrect. Retaining original permissions on a move only applies when "
                    "moving within the SAME NTFS volume. Moving to a DIFFERENT volume "
                    "behaves like a copy (inherits destination permissions) followed by "
                    "deletion of the source."
                ),
            },
            {
                "id": "c",
                "text": "All permissions were stripped and the folder became inaccessible to all users",
                "correct": False,
                "rationale": (
                    "Incorrect. Permissions are not stripped; the folder inherits the "
                    "destination's permissions. The user lost access because the destination "
                    "folder's inherited permissions may not include that user, not because "
                    "all permissions were removed."
                ),
            },
            {
                "id": "d",
                "text": "The folder's permissions were merged with those of D:\\Archive",
                "correct": False,
                "rationale": (
                    "Incorrect. NTFS does not merge source and destination permissions "
                    "on a move. The resulting object inherits only the destination's "
                    "permissions."
                ),
            },
        ],
        "explanation": (
            "NTFS move rules: Same volume move → permissions retained. "
            "Different volume move → treated as copy + delete → inherits destination "
            "permissions. Same rule applies to files. This is a common source of "
            "accidental permission changes when reorganizing data across volumes."
        ),
    },
    # ── 2.6 Windows Security Settings ────────────────────────────────────────
    {
        "id": "c2d2v2-024",
        "domain": 2,
        "objective": "2.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows security settings",
        "stem": (
            "A Windows 10 workstation is configured so that the local administrator "
            "account is disabled and all user accounts require a password of at least "
            "12 characters with complexity requirements, and accounts lock after 5 failed "
            "attempts. These settings are configured via what Windows tool for local "
            "policy enforcement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Local Security Policy (secpol.msc)",
                "correct": True,
                "rationale": (
                    "Correct. Local Security Policy (secpol.msc) provides a GUI to configure "
                    "local account policies (password length, complexity, lockout thresholds), "
                    "local user rights, and security options on standalone or workgroup machines. "
                    "On domain machines, GPOs can override local policy."
                ),
            },
            {
                "id": "b",
                "text": "Windows Defender Security Center",
                "correct": False,
                "rationale": (
                    "Incorrect. Windows Defender Security Center (now Windows Security) "
                    "manages antivirus, firewall, and device health features. It does not "
                    "configure password complexity, lockout policies, or account settings."
                ),
            },
            {
                "id": "c",
                "text": "Device Manager (devmgmt.msc)",
                "correct": False,
                "rationale": (
                    "Incorrect. Device Manager manages hardware drivers and device "
                    "configurations. It has no role in account or security policy settings."
                ),
            },
            {
                "id": "d",
                "text": "Task Scheduler",
                "correct": False,
                "rationale": (
                    "Incorrect. Task Scheduler automates execution of programs and scripts "
                    "at defined times or triggers. It is not a security policy tool."
                ),
            },
        ],
        "explanation": (
            "secpol.msc (Local Security Policy) is the correct Windows tool for configuring "
            "local password policy, account lockout policy, audit policy, user rights, "
            "and security options on a standalone workstation. On domain-joined machines, "
            "these same settings are typically managed through Active Directory Group Policy "
            "Objects (GPOs), which override local policy."
        ),
    },
    {
        "id": "c2d2v2-025",
        "domain": 2,
        "objective": "2.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows security settings",
        "stem": (
            "A Windows administrator wants to audit all failed logon attempts to a "
            "workstation and review the log entries later. Which Windows tool or feature "
            "stores these audit events and where are they found?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Windows Event Viewer — Security log stores logon failure events (Event ID 4625)",
                "correct": True,
                "rationale": (
                    "Correct. When audit policy for logon events is enabled (via Local "
                    "Security Policy or GPO), failed logon attempts are written to the "
                    "Security event log, viewable in Event Viewer. Event ID 4625 is "
                    "specifically the failed logon event."
                ),
            },
            {
                "id": "b",
                "text": "Windows Defender logs — threat detection events are stored in the Application log",
                "correct": False,
                "rationale": (
                    "Incorrect. Windows Defender logs antivirus/threat detection events, "
                    "not authentication events. Logon failures are security events recorded "
                    "in the Security log, not the Defender or Application logs."
                ),
            },
            {
                "id": "c",
                "text": "Task Manager — the Performance tab records failed logon spikes",
                "correct": False,
                "rationale": (
                    "Incorrect. Task Manager displays real-time system performance "
                    "metrics (CPU, memory, network). It does not log or store security "
                    "events such as failed logon attempts."
                ),
            },
            {
                "id": "d",
                "text": "Registry Editor — failed logon counts are stored under HKLM\\SECURITY\\SAM",
                "correct": False,
                "rationale": (
                    "Incorrect. While the SAM hive holds account lockout counters, it "
                    "is not an auditable event log. Detailed logon failure audit records "
                    "with timestamps and user context are stored in the Security event log."
                ),
            },
        ],
        "explanation": (
            "Windows security auditing records events to the Security log in Event Viewer. "
            "Audit Logon Events must be enabled in Local Security Policy or GPO to capture "
            "Event ID 4625 (failed logon) and 4624 (successful logon). The Security log "
            "is the authoritative source for authentication auditing on Windows systems."
        ),
    },
    {
        "id": "c2d2v2-026",
        "domain": 2,
        "objective": "2.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows security settings",
        "stem": (
            "An organization's security policy prohibits the use of removable media on "
            "workstations. A technician needs to enforce this policy on all domain-joined "
            "Windows machines centrally. Which approach BEST accomplishes this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Configure a Group Policy Object to disable access to removable storage devices and link it to the appropriate OU",
                "correct": True,
                "rationale": (
                    "Correct. GPO includes a 'Removable Storage Access' policy under "
                    "Computer Configuration that can deny read/write to removable disks "
                    "for all machines in the targeted OU. This is the scalable, centralized "
                    "enforcement mechanism for domain-joined machines."
                ),
            },
            {
                "id": "b",
                "text": "Physically remove USB ports from each workstation",
                "correct": False,
                "rationale": (
                    "Incorrect. While physically removing USB ports would work, it is "
                    "impractical at scale, irreversible, and prevents legitimate USB "
                    "use cases (keyboards, mice). GPO provides a policy-based, "
                    "manageable solution."
                ),
            },
            {
                "id": "c",
                "text": "Deploy antivirus with USB scan-on-insert on each machine",
                "correct": False,
                "rationale": (
                    "Incorrect. Antivirus scanning on USB insert scans for malware but "
                    "does not prohibit removable media access. The policy requires "
                    "blocking all removable media use, not just scanning it."
                ),
            },
            {
                "id": "d",
                "text": "Train employees not to use USB drives",
                "correct": False,
                "rationale": (
                    "Incorrect. Training is a compensating administrative control but is "
                    "not a technical enforcement mechanism. Users can still plug in drives "
                    "regardless of training. The policy requires enforceable technical "
                    "controls."
                ),
            },
        ],
        "explanation": (
            "Group Policy's 'Removable Storage Access' policies (under Computer Configuration "
            "→ Administrative Templates → System → Removable Storage Access) allow "
            "administrators to deny read/write access to USB drives, CD/DVD, and other "
            "removable media classes across all machines in an OU. This is the scalable, "
            "policy-compliant solution for domain environments."
        ),
    },
    # ── 2.6 BitLocker & EFS ───────────────────────────────────────────────────
    {
        "id": "c2d2v2-027",
        "domain": 2,
        "objective": "2.6",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "BitLocker & encryption (EFS)",
        "stem": (
            "A Windows 10 workstation has BitLocker enabled with TPM-only authentication. "
            "An attacker with physical access boots the machine normally and it unlocks "
            "automatically. The attacker then logs in with stolen credentials. How should "
            "the BitLocker configuration be changed to mitigate physical access risk from "
            "this scenario?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Enable BitLocker with TPM + PIN pre-boot authentication so the drive cannot be unlocked without the correct PIN even with the TPM present",
                "correct": True,
                "rationale": (
                    "Correct. TPM-only BitLocker unlocks automatically on the machine it "
                    "was configured on — it only prevents the drive from being read on a "
                    "different machine. Adding a pre-boot PIN (or USB key) requires a second "
                    "factor at boot, so even an attacker with the physical device and stolen "
                    "OS credentials cannot bypass the pre-boot step."
                ),
            },
            {
                "id": "b",
                "text": "Enable EFS on the user's Documents folder as an additional layer",
                "correct": False,
                "rationale": (
                    "Incorrect. EFS protects specific files when the drive is accessed "
                    "outside the OS, tied to the user certificate. But in this scenario "
                    "the attacker has stolen OS credentials and can log in as the user, "
                    "gaining access to EFS-decrypted files. The root issue is the lack of "
                    "pre-boot authentication."
                ),
            },
            {
                "id": "c",
                "text": "Migrate from BitLocker to EFS for the entire volume",
                "correct": False,
                "rationale": (
                    "Incorrect. EFS is a file/folder encryption tool, not a full-volume "
                    "encryption solution. It cannot encrypt the OS volume. BitLocker with "
                    "TPM+PIN is the correct full-volume pre-boot authentication solution."
                ),
            },
            {
                "id": "d",
                "text": "Enable Secure Boot and disable the boot menu to prevent alternate OS booting",
                "correct": False,
                "rationale": (
                    "Incorrect. Secure Boot prevents unsigned OS code from running and "
                    "is a complementary control, but it does not require a second factor "
                    "for BitLocker unlock. TPM-only BitLocker still auto-unlocks after "
                    "Secure Boot validates the boot chain. The additional authentication "
                    "factor (PIN) is still needed."
                ),
            },
        ],
        "explanation": (
            "TPM-only BitLocker provides encryption against offline attacks (removing "
            "the drive and attaching it to another machine). However, it auto-unlocks "
            "on the original machine. Adding a pre-boot PIN (TPM+PIN mode) requires "
            "knowledge of the PIN at every boot, providing a second factor that physical "
            "possession of the device alone cannot satisfy."
        ),
    },
    {
        "id": "c2d2v2-028",
        "domain": 2,
        "objective": "2.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "BitLocker & encryption (EFS)",
        "stem": (
            "A user's Windows laptop was encrypted with EFS. The user profile was "
            "corrupted and had to be deleted. IT rebuilt the profile. Now the user "
            "reports they cannot open their EFS-encrypted files. Why, and what is "
            "the CORRECT recovery path?"
        ),
        "options": [
            {
                "id": "a",
                "text": "EFS encryption keys are tied to the user's certificate stored in their profile; deleting the profile deleted the keys. The files can only be recovered using a previously exported EFS certificate/private key or a Data Recovery Agent (DRA) certificate",
                "correct": True,
                "rationale": (
                    "Correct. EFS uses a public/private key pair stored in the user's "
                    "certificate store (part of the profile). Deleting the profile without "
                    "exporting the certificate first destroys the decryption key. Recovery "
                    "requires either a backup of the user's EFS certificate and private key "
                    "or a configured Data Recovery Agent (DRA) certificate on the system."
                ),
            },
            {
                "id": "b",
                "text": "The NTFS permissions were reset when the profile was deleted; re-assign Full Control to the new profile",
                "correct": False,
                "rationale": (
                    "Incorrect. This is an encryption key loss problem, not an NTFS "
                    "permissions problem. Re-assigning NTFS permissions does not recover "
                    "the EFS private key needed to decrypt the files. The user owns the "
                    "files but cannot decrypt them without the private key."
                ),
            },
            {
                "id": "c",
                "text": "Re-enable EFS on the files by right-clicking Properties > Advanced > Encrypt contents",
                "correct": False,
                "rationale": (
                    "Incorrect. The files are already encrypted. Re-enabling the checkbox "
                    "would attempt to re-encrypt them, but without the original private "
                    "key, the current encrypted content cannot be read. This does not "
                    "solve the key loss problem."
                ),
            },
            {
                "id": "d",
                "text": "BitLocker recovery key can be used to decrypt EFS files if the drive key is available",
                "correct": False,
                "rationale": (
                    "Incorrect. BitLocker and EFS are independent encryption systems. "
                    "BitLocker encrypts the volume; EFS encrypts individual files within "
                    "the volume using user-specific certificates. BitLocker recovery keys "
                    "cannot decrypt EFS-encrypted files."
                ),
            },
        ],
        "explanation": (
            "EFS is certificate-based encryption tied to a specific user profile's private "
            "key. Best practice: export and back up the EFS certificate before any profile "
            "changes, and configure a Domain Data Recovery Agent (DRA) via Group Policy "
            "so administrators can recover encrypted files. Without the original private "
            "key or a DRA, EFS-encrypted files are permanently inaccessible."
        ),
    },
    # ── 2.7 Mobile/Embedded Device Security ──────────────────────────────────
    {
        "id": "c2d2v2-029",
        "domain": 2,
        "objective": "2.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile/embedded device security",
        "stem": (
            "An employee roots their Android corporate phone to install an app not "
            "available in the Play Store. The company's MDM policy detects this and "
            "marks the device as non-compliant. Which security risk does rooting a "
            "corporate device PRIMARILY introduce?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Rooting bypasses the OS security model, allowing apps to access kernel-level resources and other apps' data, including corporate container data",
                "correct": True,
                "rationale": (
                    "Correct. Rooting (Android) / jailbreaking (iOS) removes the OS sandbox "
                    "that enforces app isolation. A rooted device can run apps with superuser "
                    "privileges, potentially reading or exfiltrating data from MDM-managed "
                    "containers that rely on OS-level enforcement for isolation."
                ),
            },
            {
                "id": "b",
                "text": "The device can no longer receive carrier software updates",
                "correct": False,
                "rationale": (
                    "Incorrect. While rooting can interfere with OTA updates, the primary "
                    "security concern is the loss of OS-enforced app sandboxing and privilege "
                    "separation, not the update mechanism."
                ),
            },
            {
                "id": "c",
                "text": "GPS location tracking becomes unavailable for the MDM solution",
                "correct": False,
                "rationale": (
                    "Incorrect. Rooting does not necessarily disable GPS. The primary "
                    "security risk is elevated privilege access and breakdown of the OS "
                    "security sandbox."
                ),
            },
            {
                "id": "d",
                "text": "The MDM profile is automatically removed from the device",
                "correct": False,
                "rationale": (
                    "Incorrect. MDM detection of root/jailbreak may trigger a compliance "
                    "action (quarantine, wipe), but the primary security risk driving that "
                    "policy is the OS security boundary violation, not the MDM profile "
                    "removal itself."
                ),
            },
        ],
        "explanation": (
            "Android's security model relies on user-space isolation enforced by the Linux "
            "kernel (UID-based app separation) and the SELinux MAC policy. Rooting grants "
            "superuser access, breaking these enforcement boundaries. MDM container security "
            "(e.g., Android Work Profile, Samsung Knox) depends on the OS enforcing separation "
            "between managed and unmanaged partitions — rooting can circumvent these controls."
        ),
    },
    {
        "id": "c2d2v2-030",
        "domain": 2,
        "objective": "2.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile/embedded device security",
        "stem": (
            "A company issues company-owned iOS devices to field staff. IT wants to "
            "ensure that if a device is lost, all apps, accounts, and data installed "
            "by the MDM solution can be removed without affecting the user's personal "
            "Apple ID or personal apps. Which MDM feature accomplishes this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Selective (corporate) wipe via MDM-managed profile removal",
                "correct": True,
                "rationale": (
                    "Correct. A selective wipe removes only the MDM-managed profile, "
                    "associated apps, accounts, and corporate data from the device. "
                    "Personal Apple ID content, purchased apps, and personal data are "
                    "left intact. This is designed for exactly this BYOD or corporate-owned "
                    "co-use scenario."
                ),
            },
            {
                "id": "b",
                "text": "Full device wipe (factory reset via MDM)",
                "correct": False,
                "rationale": (
                    "Incorrect. A full device wipe erases everything — both corporate "
                    "and personal data. The requirement is to preserve the user's personal "
                    "Apple ID content, so selective wipe is the appropriate action."
                ),
            },
            {
                "id": "c",
                "text": "Remote lock the device until it is recovered",
                "correct": False,
                "rationale": (
                    "Incorrect. Remote lock prevents unauthorized access to a found device "
                    "but does not remove corporate data. If the device is not recovered, "
                    "corporate data remains on it indefinitely."
                ),
            },
            {
                "id": "d",
                "text": "Revoke the user's corporate email certificate",
                "correct": False,
                "rationale": (
                    "Incorrect. Revoking the email certificate prevents new email "
                    "authentication but does not remove existing emails, corporate apps, "
                    "or other managed data already on the device."
                ),
            },
        ],
        "explanation": (
            "Selective wipe removes the MDM enrollment profile and all managed content "
            "(corporate apps distributed via MDM, managed accounts, managed documents). "
            "On iOS, the User Enrollment model specifically separates managed Apple ID space "
            "from personal Apple ID space. Full wipe is appropriate only when no personal "
            "content exists or the device cannot be recovered."
        ),
    },
    {
        "id": "c2d2v2-031",
        "domain": 2,
        "objective": "2.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile/embedded device security",
        "stem": (
            "A retail company installs IoT-based environmental sensors throughout their "
            "warehouse. These sensors communicate over Wi-Fi but cannot be patched or "
            "enrolled in MDM. The security team must allow sensor data to reach the "
            "cloud dashboard while minimizing risk to the corporate LAN. What is the "
            "BEST network architecture decision?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Place all IoT sensors on an isolated VLAN with internet access only to the required cloud endpoint, completely separated from the corporate LAN",
                "correct": True,
                "rationale": (
                    "Correct. Network segmentation via a dedicated IoT VLAN confines any "
                    "compromise of unpatched sensors to that isolated segment. Firewall ACLs "
                    "restrict the IoT VLAN to the minimum required connectivity (cloud dashboard "
                    "endpoint), preventing lateral movement to corporate systems."
                ),
            },
            {
                "id": "b",
                "text": "Connect all sensors to the corporate LAN segment and use host-based firewalls on corporate workstations",
                "correct": False,
                "rationale": (
                    "Incorrect. Placing unpatched IoT devices on the corporate LAN introduces "
                    "unmanaged attack surface directly to corporate assets. Host-based firewalls "
                    "on workstations do not prevent an IoT compromise from being used to "
                    "probe and attack adjacent LAN devices."
                ),
            },
            {
                "id": "c",
                "text": "Enroll the sensors in MDM and enforce policy compliance before allowing network access",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario explicitly states the sensors cannot be enrolled "
                    "in MDM. This option is not feasible for this device class."
                ),
            },
            {
                "id": "d",
                "text": "Disable wireless on the sensors and use only wired PoE connections on the corporate switch",
                "correct": False,
                "rationale": (
                    "Incorrect. Switching from Wi-Fi to wired does not address the "
                    "segmentation problem — unpatched sensors on the same network segment "
                    "as corporate systems remain a risk regardless of the physical media."
                ),
            },
        ],
        "explanation": (
            "IoT segmentation is the standard security architecture for unmanageable devices. "
            "A dedicated IoT VLAN with strict egress filtering (only cloud dashboard endpoints "
            "allowed) limits the blast radius if a sensor is compromised. This is consistent "
            "with network segmentation best practices and the concept of compensating controls "
            "for devices that cannot be patched or enrolled."
        ),
    },
    # ── 2.8 Data Destruction & Disposal ──────────────────────────────────────
    {
        "id": "c2d2v2-032",
        "domain": 2,
        "objective": "2.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Data destruction & disposal",
        "stem": (
            "A company is retiring a batch of SSDs that held sensitive customer PII. "
            "A technician performs a standard multi-pass overwrite (the same method "
            "used for HDDs) and declares them sanitized. Why is this approach potentially "
            "insufficient for SSDs?"
        ),
        "options": [
            {
                "id": "a",
                "text": "SSD wear-leveling and over-provisioning may retain copies of data in sectors that the OS-level overwrite never addresses",
                "correct": True,
                "rationale": (
                    "Correct. SSDs use wear-leveling algorithms that map logical blocks to "
                    "different physical cells over time. Over-provisioned (reserved) cells "
                    "are invisible to the OS. An OS-level overwrite writes to the logical "
                    "address space but may not reach all physical cells that held the data, "
                    "leaving residual copies that a forensic tool reading the raw NAND "
                    "could potentially recover."
                ),
            },
            {
                "id": "b",
                "text": "Multi-pass overwrite is too slow for SSDs, creating unreliable write results",
                "correct": False,
                "rationale": (
                    "Incorrect. Speed is not the reason multi-pass overwrite is insufficient "
                    "for SSDs. The issue is architectural: wear-leveling hides physical cells "
                    "from the logical address space the OS writes to."
                ),
            },
            {
                "id": "c",
                "text": "SSDs use magnetic storage like HDDs but with faster access times",
                "correct": False,
                "rationale": (
                    "Incorrect. SSDs use NAND flash memory, not magnetic storage. This "
                    "factual error is the basis of a common misconception. The lack of "
                    "magnetic media also means degaussing is ineffective on SSDs."
                ),
            },
            {
                "id": "d",
                "text": "The DoD 5220.22-M standard requires seven passes for SSDs, not three",
                "correct": False,
                "rationale": (
                    "Incorrect. Pass count does not resolve the wear-leveling problem. "
                    "Even seven passes through the logical address space may not overwrite "
                    "all physical cells. The recommended SSD sanitization methods are "
                    "manufacturer-provided Secure Erase (ATA), crypto-erase, or physical "
                    "destruction."
                ),
            },
        ],
        "explanation": (
            "SSDs present unique sanitization challenges due to wear-leveling and "
            "over-provisioning. The recommended approaches for SSD sanitization are: "
            "(1) Manufacturer ATA Secure Erase command (issues a built-in erase to all "
            "cells including over-provisioned), (2) Cryptographic erase (if drive is "
            "self-encrypting, destroy the encryption key), or (3) Physical destruction. "
            "Standard multi-pass software overwrites are unreliable for SSDs."
        ),
    },
    {
        "id": "c2d2v2-033",
        "domain": 2,
        "objective": "2.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Data destruction & disposal",
        "stem": (
            "A technician is preparing a self-encrypting drive (SED) for redeployment "
            "to a new user. The drive currently contains the previous user's data "
            "encrypted with the drive's built-in AES hardware. Which sanitization "
            "method is MOST efficient and provides cryptographic assurance that the "
            "previous data is unrecoverable?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Cryptographic erase — rekey the drive by generating a new encryption key, making all previously encrypted data undecryptable",
                "correct": True,
                "rationale": (
                    "Correct. A cryptographic erase (crypto-erase) replaces the drive's "
                    "internal encryption key (Data Encryption Key). All existing encrypted "
                    "data becomes permanently unreadable because the key needed to decrypt "
                    "it no longer exists. This is instantaneous, preserves the drive "
                    "hardware, and is approved by NIST SP 800-88 for SEDs."
                ),
            },
            {
                "id": "b",
                "text": "Seven-pass DoD overwrite to ensure all sectors are zeroed",
                "correct": False,
                "rationale": (
                    "Incorrect. A multi-pass overwrite is time-consuming and, for SEDs, "
                    "unnecessary — crypto-erase is faster, equally or more effective, and "
                    "recommended by NIST 800-88 for self-encrypting drives. The overwrite "
                    "still faces the SSD wear-leveling problem if the SED is flash-based."
                ),
            },
            {
                "id": "c",
                "text": "Degauss the drive before redeployment",
                "correct": False,
                "rationale": (
                    "Incorrect. Degaussing destroys the magnetic servo structure on HDDs "
                    "and renders them unusable. It has no effect on flash-based SSDs (which "
                    "are not magnetic), and even for magnetic HDDs, degaussing would destroy "
                    "the drive rather than prepare it for redeployment."
                ),
            },
            {
                "id": "d",
                "text": "Perform a full Windows format before reassigning to the new user",
                "correct": False,
                "rationale": (
                    "Incorrect. A Windows format (even a full format) writes to the logical "
                    "address space and cannot guarantee all physical cells are overwritten "
                    "on flash-based drives. For a SED, crypto-erase is the correct and "
                    "most efficient sanitization method."
                ),
            },
        ],
        "explanation": (
            "NIST SP 800-88 recognizes cryptographic erasure as an approved sanitization "
            "method for SEDs. By destroying or replacing the Data Encryption Key (DEK), "
            "all data on the drive becomes cryptographically irretrievable — even if the "
            "raw NAND cells are read directly. This is the fastest and most complete "
            "method for SEDs intended for reuse."
        ),
    },
    {
        "id": "c2d2v2-034",
        "domain": 2,
        "objective": "2.8",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Data destruction & disposal",
        "stem": (
            "A healthcare organization needs to destroy 200 HDDs that held patient "
            "records. The drives are no longer functional but must be provably destroyed "
            "to meet HIPAA requirements. Which TWO items are MOST important when "
            "contracting with a third-party destruction vendor?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Certificate of destruction listing drive serial numbers and the method used, provided by the vendor after completion",
                "correct": True,
                "rationale": (
                    "Correct. A certificate of destruction is the required compliance "
                    "documentation for HIPAA and other regulations. It should itemize "
                    "each destroyed asset (serial numbers), destruction method, date, "
                    "and vendor attestation."
                ),
            },
            {
                "id": "b",
                "text": "Chain of custody documentation tracking the drives from removal to destruction",
                "correct": True,
                "rationale": (
                    "Correct. Chain of custody ensures an auditable record of who possessed "
                    "the drives at each step from removal through transport to destruction. "
                    "This prevents drives from going missing and demonstrates due diligence "
                    "to regulators."
                ),
            },
            {
                "id": "c",
                "text": "Confirmation that the vendor performed a three-pass overwrite before shredding",
                "correct": False,
                "rationale": (
                    "Incorrect. For non-functional drives or drives targeted for physical "
                    "destruction, software overwrite before shredding is unnecessary and "
                    "often not possible. The physical destruction itself is the disposal "
                    "method; certificate and chain of custody are the documentation requirements."
                ),
            },
            {
                "id": "d",
                "text": "Proof that the vendor returned the drives to the organization after destruction",
                "correct": False,
                "rationale": (
                    "Incorrect. A vendor returning remnants of destroyed drives is not "
                    "a standard requirement. The certificate of destruction, not physical "
                    "remnants, is the compliance documentation. Some organizations do "
                    "request witness destruction or video evidence, but return of material "
                    "is not a standard HIPAA-related requirement."
                ),
            },
        ],
        "explanation": (
            "For regulated industries (HIPAA, PCI-DSS, SOX), third-party media destruction "
            "requires: (1) Certificate of destruction — itemized, signed document from "
            "the vendor, and (2) Chain of custody — documented transfer of the media "
            "from the organization to the vendor. These two documents together provide "
            "the audit trail required for regulatory compliance."
        ),
    },
    # ── 2.9 SOHO Network Security ─────────────────────────────────────────────
    {
        "id": "c2d2v2-035",
        "domain": 2,
        "objective": "2.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SOHO network security",
        "stem": (
            "A home user wants to prevent their children from accessing specific "
            "categories of websites (gambling, adult content) on any device connected "
            "to the home network without installing software on each device. Which "
            "SOHO router feature BEST achieves this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Content filtering / parental controls configured in the router's firmware",
                "correct": True,
                "rationale": (
                    "Correct. Most modern SOHO routers include built-in content filtering "
                    "or parental controls that block categories of websites at the DNS or "
                    "HTTP level for all devices on the network. This requires no per-device "
                    "software installation, satisfying the stated requirement."
                ),
            },
            {
                "id": "b",
                "text": "Enable WPA3 encryption on the wireless network",
                "correct": False,
                "rationale": (
                    "Incorrect. WPA3 encrypts the wireless connection but has no mechanism "
                    "for filtering web content by category. Encryption and content filtering "
                    "are separate functions."
                ),
            },
            {
                "id": "c",
                "text": "Configure port forwarding for HTTP and HTTPS to block outbound access",
                "correct": False,
                "rationale": (
                    "Incorrect. Port forwarding directs inbound traffic to internal hosts; "
                    "it is not a mechanism for filtering outbound traffic by content "
                    "category. Misconfiguring port forwarding could expose internal "
                    "services to the internet."
                ),
            },
            {
                "id": "d",
                "text": "Place all devices in the DMZ segment",
                "correct": False,
                "rationale": (
                    "Incorrect. Placing devices in the DMZ exposes them directly to "
                    "inbound internet traffic — the opposite of restricting access. A DMZ "
                    "is for hosting internet-facing services, not for blocking outbound "
                    "content for clients."
                ),
            },
        ],
        "explanation": (
            "Router-based content filtering (parental controls) applies URL category blocking "
            "at the network level, covering all connected devices without per-device agents. "
            "Many routers also support integration with DNS-based filtering services "
            "(e.g., OpenDNS FamilyShield) for more granular control. This is the scalable, "
            "device-agnostic solution for home content control."
        ),
    },
    {
        "id": "c2d2v2-036",
        "domain": 2,
        "objective": "2.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SOHO network security",
        "stem": (
            "A small business owner has a single internet connection and uses a SOHO "
            "router. The owner wants to view logs showing which websites employees "
            "visit and how much bandwidth each device uses. Which router feature "
            "provides this visibility?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Traffic logging / bandwidth monitoring in the router's administration interface",
                "correct": True,
                "rationale": (
                    "Correct. SOHO routers with traffic logging and bandwidth monitoring "
                    "features log DNS queries, HTTP requests (for non-HTTPS sites), and "
                    "per-device data usage statistics. This provides the required visibility "
                    "from a single, centralized management point."
                ),
            },
            {
                "id": "b",
                "text": "Configure a static IP for each device",
                "correct": False,
                "rationale": (
                    "Incorrect. Static IP assignment ensures consistent IP-to-device "
                    "mapping (useful for identifying devices in logs) but does not by "
                    "itself generate browsing logs or bandwidth reports."
                ),
            },
            {
                "id": "c",
                "text": "Enable MAC address filtering",
                "correct": False,
                "rationale": (
                    "Incorrect. MAC filtering controls which devices are permitted to "
                    "connect to the network. It does not log traffic or produce bandwidth "
                    "reports."
                ),
            },
            {
                "id": "d",
                "text": "Upgrade to WPA3 enterprise mode",
                "correct": False,
                "rationale": (
                    "Incorrect. WPA3 enterprise mode improves wireless authentication "
                    "security. It does not provide web browsing logs or bandwidth "
                    "utilization reports."
                ),
            },
        ],
        "explanation": (
            "Many SOHO routers include built-in traffic analysis, DNS query logging, and "
            "bandwidth monitoring. For more comprehensive visibility, some organizations "
            "use dedicated features like router-based syslog output to a logging server, "
            "or DNS-level logging through services like Pi-hole. Consistent IP addresses "
            "(via DHCP reservations) improve the usefulness of per-device log entries."
        ),
    },
    # ── 2.10 Browser Security ─────────────────────────────────────────────────
    {
        "id": "c2d2v2-037",
        "domain": 2,
        "objective": "2.10",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Browser security",
        "stem": (
            "A corporate policy requires all end-user browsers to block third-party "
            "cookies, prevent automatic browser extension installation, and enforce "
            "safe search settings across all managed workstations. Which approach "
            "allows IT to enforce these browser settings at scale without configuring "
            "each machine manually?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Deploy browser-specific Group Policy Administrative Templates (ADMX) through Active Directory GPO",
                "correct": True,
                "rationale": (
                    "Correct. Major browsers (Chrome, Edge, Firefox) provide ADMX "
                    "administrative templates that expose browser settings as Group Policy "
                    "settings. GPOs can enforce cookie policies, disable extension sideloading, "
                    "and configure safe search across all domain-joined machines centrally."
                ),
            },
            {
                "id": "b",
                "text": "Email instructions to each employee explaining how to configure browser settings manually",
                "correct": False,
                "rationale": (
                    "Incorrect. Email instructions rely on users voluntarily applying "
                    "settings and cannot enforce compliance. Users may configure settings "
                    "incorrectly or revert them. Technical enforcement via GPO is required."
                ),
            },
            {
                "id": "c",
                "text": "Install a browser extension on each machine that enforces the policy",
                "correct": False,
                "rationale": (
                    "Incorrect. A browser extension can be removed or disabled by users "
                    "with sufficient rights, and deploying per-machine is exactly what "
                    "the question asks to avoid. GPO provides enforceable, managed policy."
                ),
            },
            {
                "id": "d",
                "text": "Configure settings in the browser once on one machine and export the browser profile",
                "correct": False,
                "rationale": (
                    "Incorrect. Exporting and manually importing a browser profile requires "
                    "touching each machine and users can modify profiles afterward. GPO "
                    "provides centrally enforced, continuously re-applied settings."
                ),
            },
        ],
        "explanation": (
            "Browser ADMX templates extend Group Policy to control browser behavior on "
            "domain-joined machines. Microsoft Edge and Google Chrome both provide official "
            "ADMX files. Policies are re-applied at each GPO refresh interval, preventing "
            "user override. This is the scalable enterprise browser management approach "
            "tested by CompTIA A+ Core 2."
        ),
    },
    {
        "id": "c2d2v2-038",
        "domain": 2,
        "objective": "2.10",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Browser security",
        "stem": (
            "A user's browser has been behaving strangely: the default search engine "
            "changed without permission, new toolbars appeared, and the home page "
            "redirects to an unfamiliar site. Which TWO actions should the technician "
            "take FIRST to remediate this browser hijacking? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Scan the system with updated anti-malware software to detect and remove the hijacking software",
                "correct": True,
                "rationale": (
                    "Correct. Browser hijacking is typically caused by PUPs (potentially "
                    "unwanted programs), adware, or malware that modifies browser settings. "
                    "An updated anti-malware scan is the first technical remediation step "
                    "to identify and remove the offending software."
                ),
            },
            {
                "id": "b",
                "text": "Review and remove suspicious browser extensions, toolbars, and plugins from the browser's extension manager",
                "correct": True,
                "rationale": (
                    "Correct. Malicious extensions and toolbars directly cause browser "
                    "hijacking symptoms. Removing them from the browser's extension "
                    "manager eliminates the mechanism of the hijack and restores correct "
                    "browser behavior."
                ),
            },
            {
                "id": "c",
                "text": "Clear only the browser cache without checking installed extensions",
                "correct": False,
                "rationale": (
                    "Incorrect. Clearing the cache removes temporary files but does not "
                    "remove installed malicious extensions or address changes to browser "
                    "settings (home page, default search). The hijacking software remains "
                    "active."
                ),
            },
            {
                "id": "d",
                "text": "Reinstall the operating system to ensure complete removal",
                "correct": False,
                "rationale": (
                    "Incorrect. OS reinstallation is a last resort for severe infections. "
                    "Browser hijacking caused by extensions or PUPs can be remediated "
                    "without a full OS reinstall. Scanning with anti-malware and removing "
                    "the extensions are the appropriate first steps."
                ),
            },
        ],
        "explanation": (
            "Browser hijacking symptoms (changed home page, search engine, new toolbars) "
            "are caused by malicious or unwanted software installed as extensions/plugins or "
            "through PUPs bundled with freeware. First-response steps: (1) anti-malware scan "
            "to detect the PUP/adware, (2) manual inspection and removal of unknown extensions "
            "from the browser. After removal, reset the home page and default search engine "
            "to desired settings. OS reinstall is reserved for unremovable rootkit-level infections."
        ),
    },
]

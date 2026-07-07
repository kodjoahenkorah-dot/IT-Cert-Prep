"""
CompTIA A+ Core 2 (220-1202) — Domain 2: Security  (v3b)
32 exam-quality questions — IDs c2d2v3b-001 through c2d2v3b-032.
All scenarios are original and distinct from domain2_security.py and domain2_security_v3a.py.
"""

QUESTIONS = [
    # ── 2.1 Physical Security ────────────────────────────────────────────────
    {
        "id": "c2d2v3b-001",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Physical security",
        "stem": (
            "A financial services company is relocating its server room to a new building. "
            "The security manager wants to ensure that only authorized personnel can enter "
            "the server room and that every entry is logged with a timestamp and the "
            "identity of the person who entered. Which physical access control technology "
            "BEST meets both requirements?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Smart card badge reader with an integrated audit log",
                "correct": True,
                "rationale": (
                    "Correct. A smart card badge reader authenticates the cardholder's "
                    "identity (via certificate on the chip) and automatically records a "
                    "timestamped entry event to an audit log, satisfying both the access "
                    "restriction and the identity-linked logging requirements."
                ),
            },
            {
                "id": "b",
                "text": "Combination lock with a shared PIN known to authorized staff",
                "correct": False,
                "rationale": (
                    "Incorrect. A shared-PIN combination lock does not log individual "
                    "identities — anyone who knows the code can enter, and there is no "
                    "per-person audit trail."
                ),
            },
            {
                "id": "c",
                "text": "CCTV camera positioned above the server room door",
                "correct": False,
                "rationale": (
                    "Incorrect. CCTV records video but does not actively restrict access "
                    "or automatically create a timestamped identity log. Reviewing footage "
                    "to identify individuals is manual and after the fact."
                ),
            },
            {
                "id": "d",
                "text": "Motion detector alarm inside the server room",
                "correct": False,
                "rationale": (
                    "Incorrect. A motion alarm detects presence after unauthorized access "
                    "has already occurred. It does not restrict entry or log identity-linked "
                    "events."
                ),
            },
        ],
        "explanation": (
            "Smart card badge readers authenticate each user individually (using certificate "
            "or magnetic-stripe data) and write a timestamped, user-attributed record to an "
            "access log each time the door is opened. Shared PINs cannot distinguish who "
            "entered; cameras provide video but not automatic structured logs; motion alarms "
            "are detective, not preventive or logging controls."
        ),
    },
    {
        "id": "c2d2v3b-002",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Physical security",
        "stem": (
            "A technician arrives at a customer's site to perform scheduled maintenance. "
            "The customer's receptionist is unavailable, so an employee the technician has "
            "never met offers to escort them directly to the server room. Which security "
            "principle is being tested in this scenario, and what should the technician do?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Verify identity through an established contact before proceeding; do not enter secured areas based solely on an unverified employee's offer",
                "correct": True,
                "rationale": (
                    "Correct. This scenario tests whether the technician will bypass visitor "
                    "identity verification and escort policy. Best practice is to wait for a "
                    "verified point of contact, confirm authorization through a known channel "
                    "(phone or email to the scheduling contact), and not rely on an unverified "
                    "employee's word alone."
                ),
            },
            {
                "id": "b",
                "text": "Follow the employee immediately, since employees can be trusted by default",
                "correct": False,
                "rationale": (
                    "Incorrect. Trusting any employee without verification is the exact "
                    "behavior a social engineer exploits. The identity of both the visitor "
                    "and their escort should be verified through established procedures."
                ),
            },
            {
                "id": "c",
                "text": "Proceed if the employee shows a company ID badge, since that constitutes sufficient authentication",
                "correct": False,
                "rationale": (
                    "Incorrect. An ID badge confirms employment but does not confirm "
                    "that the employee is authorized to escort visitors to the server room, "
                    "nor does it confirm the technician's own access authorization has been "
                    "verified by the organization."
                ),
            },
            {
                "id": "d",
                "text": "Begin work immediately to minimize downtime; document the access deviation in the service ticket afterward",
                "correct": False,
                "rationale": (
                    "Incorrect. Documenting a policy deviation after the fact does not "
                    "prevent the security breach. If the 'employee' is an attacker using "
                    "social engineering, access to the server room has already been granted."
                ),
            },
        ],
        "explanation": (
            "Visitor escort policies exist specifically to prevent unauthorized individuals "
            "from accessing sensitive areas. A technician should always wait for verification "
            "from a known, scheduled contact before entering restricted areas. This scenario "
            "is a classic pretext where social engineers exploit the desire to be helpful "
            "and avoid delaying work."
        ),
    },
    {
        "id": "c2d2v3b-003",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Physical security",
        "stem": (
            "A corporate security policy requires that employees sitting at workstations "
            "in open-plan offices prevent people walking past from seeing sensitive "
            "information on their screens. Which physical security control directly "
            "addresses this threat?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Privacy screen filter applied to each monitor",
                "correct": True,
                "rationale": (
                    "Correct. A privacy screen filter narrows the viewing angle of the "
                    "display so that it is only clearly visible to the person directly "
                    "in front of it. This directly prevents passers-by from reading the "
                    "screen — the definition of the shoulder-surfing prevention control."
                ),
            },
            {
                "id": "b",
                "text": "Screen lock timeout configured to activate after 5 minutes of inactivity",
                "correct": False,
                "rationale": (
                    "Incorrect. A screen lock timeout protects an unattended workstation "
                    "after the user walks away. It does not prevent someone walking past "
                    "from seeing information while the user is actively working."
                ),
            },
            {
                "id": "c",
                "text": "Reducing monitor brightness to the lowest comfortable setting",
                "correct": False,
                "rationale": (
                    "Incorrect. Reducing brightness may slightly reduce visibility but is "
                    "not a security control and is impractical. It does not enforce a "
                    "restricted viewing angle the way a privacy filter does."
                ),
            },
            {
                "id": "d",
                "text": "Positioning all desks facing the wall so screens face away from walkways",
                "correct": False,
                "rationale": (
                    "Incorrect. Desk positioning may help but is an architectural/layout "
                    "change, not a control that can be applied to existing workstations. "
                    "Privacy screen filters are the direct, device-level control for this "
                    "threat."
                ),
            },
        ],
        "explanation": (
            "Shoulder surfing is the attack of visually observing someone's screen or "
            "keyboard. Privacy screen filters (polarized film overlays) are the specific "
            "physical control that restricts the viewing angle to directly in front of "
            "the screen. Screen locks protect idle sessions; neither brightness reduction "
            "nor desk orientation is a scalable security control."
        ),
    },
    # ── 2.2 Logical Security / Active Directory ──────────────────────────────
    {
        "id": "c2d2v3b-004",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Logical security & Active Directory",
        "stem": (
            "An IT administrator needs to ensure that all domain user accounts are "
            "automatically locked out after three failed login attempts within a "
            "ten-minute window, and remain locked until an admin manually unlocks "
            "them. Which Group Policy path contains the settings to configure this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Computer Configuration > Windows Settings > Security Settings > Account Policies > Account Lockout Policy",
                "correct": True,
                "rationale": (
                    "Correct. The Account Lockout Policy within Account Policies (under "
                    "Computer Configuration) contains the Account Lockout Threshold, "
                    "Observation Window, and Duration settings that control exactly this "
                    "behavior. Setting Duration to 0 requires admin unlock."
                ),
            },
            {
                "id": "b",
                "text": "User Configuration > Administrative Templates > System > Logon",
                "correct": False,
                "rationale": (
                    "Incorrect. The System > Logon administrative template controls "
                    "logon scripts, cached credentials display, and similar UX settings "
                    "— not account lockout thresholds or durations."
                ),
            },
            {
                "id": "c",
                "text": "Computer Configuration > Windows Settings > Security Settings > Local Policies > Security Options",
                "correct": False,
                "rationale": (
                    "Incorrect. Security Options contains interactive logon messages, "
                    "UAC behavior, and shutdown policies — not the account lockout "
                    "threshold or observation window settings."
                ),
            },
            {
                "id": "d",
                "text": "Computer Configuration > Administrative Templates > Windows Components > Windows Logon Options",
                "correct": False,
                "rationale": (
                    "Incorrect. Windows Logon Options (under Administrative Templates) "
                    "controls features like the fast user switching UI. Account lockout "
                    "is a security policy under Account Policies, not an administrative "
                    "template."
                ),
            },
        ],
        "explanation": (
            "Account lockout policy is configured under Computer Configuration > Windows "
            "Settings > Security Settings > Account Policies > Account Lockout Policy in "
            "Group Policy. The three key settings are: Account Lockout Threshold (failed "
            "attempts before lockout), Account Lockout Duration (0 = admin must unlock), "
            "and Reset Account Lockout Counter After (the observation window)."
        ),
    },
    {
        "id": "c2d2v3b-005",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Logical security & Active Directory",
        "stem": (
            "A company's security policy requires that no single person in the accounts "
            "payable department can both create a new vendor record AND approve payments "
            "to that vendor. Which security principle does this policy implement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Separation of duties",
                "correct": True,
                "rationale": (
                    "Correct. Separation of duties requires that no single individual "
                    "can complete a critical, fraud-enabling transaction alone. Splitting "
                    "vendor creation and payment approval between different roles prevents "
                    "embezzlement by requiring collusion of at least two people."
                ),
            },
            {
                "id": "b",
                "text": "Principle of least privilege",
                "correct": False,
                "rationale": (
                    "Incorrect. Least privilege limits each user to only the access "
                    "needed for their role. While related, the specific division of a "
                    "single task across multiple people to prevent fraud is separation "
                    "of duties, not least privilege."
                ),
            },
            {
                "id": "c",
                "text": "Defense in depth",
                "correct": False,
                "rationale": (
                    "Incorrect. Defense in depth layers multiple security controls so "
                    "that defeat of one does not compromise the whole. The scenario "
                    "describes dividing a specific business process — this is separation "
                    "of duties."
                ),
            },
            {
                "id": "d",
                "text": "Need to know",
                "correct": False,
                "rationale": (
                    "Incorrect. Need to know restricts information access to those who "
                    "require it for their specific job function. The scenario describes "
                    "dividing task authority within the same department — separation of "
                    "duties."
                ),
            },
        ],
        "explanation": (
            "Separation of duties (SoD) divides sensitive tasks so that completing a "
            "fraudulent transaction requires collusion between multiple individuals. "
            "Classic examples: the person who can create vendors cannot approve payments; "
            "the person who writes checks cannot also sign them. This is distinct from "
            "least privilege (minimum necessary access per role)."
        ),
    },
    {
        "id": "c2d2v3b-006",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Logical security & Active Directory",
        "stem": (
            "A user's Active Directory account is showing as locked out repeatedly "
            "throughout the day even though the user claims they are entering the correct "
            "password. The user has no other devices they know of. Which is the MOST "
            "likely cause to investigate first?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A scheduled task, mapped drive, or service running under the user's credentials with an outdated password",
                "correct": True,
                "rationale": (
                    "Correct. Repeated automated lockouts while the user is successfully "
                    "logging in manually strongly suggest a background process (service, "
                    "scheduled task, or persistent mapped drive) is trying to authenticate "
                    "with the user's old password after a password change, generating "
                    "repeated failed attempts."
                ),
            },
            {
                "id": "b",
                "text": "The domain controller's Kerberos service is failing to issue tickets",
                "correct": False,
                "rationale": (
                    "Incorrect. A Kerberos service failure would prevent ALL users from "
                    "authenticating, not just this specific user. The pattern of targeted, "
                    "repeated lockouts points to a credential-caching source specific to "
                    "this account."
                ),
            },
            {
                "id": "c",
                "text": "The user is the victim of an ongoing brute-force password attack from the internet",
                "correct": False,
                "rationale": (
                    "Incorrect. An internet-sourced brute force attack is possible but "
                    "less likely than a misconfigured service with stale credentials in "
                    "an internal domain environment. The first investigation step should "
                    "target internal causes (services, tasks) before external attack."
                ),
            },
            {
                "id": "d",
                "text": "The account lockout threshold is set too low and is triggering on mistyped usernames",
                "correct": False,
                "rationale": (
                    "Incorrect. A low threshold could cause lockouts more easily, but it "
                    "would not cause repeated lockouts throughout the day unless something "
                    "is actively trying to authenticate. The root cause is still a "
                    "source generating repeated failed attempts, most likely a stale-"
                    "credential service."
                ),
            },
        ],
        "explanation": (
            "Repeated account lockouts during an active workday, despite the user knowing "
            "their password, almost always indicate a background process (Windows service, "
            "scheduled task, RDP session, mapped network drive) that cached the old password. "
            "The Microsoft Lockout and Administration Tools (LockoutStatus.exe) and security "
            "event log (Event ID 4625) help identify the source machine and process."
        ),
    },
    # ── 2.3 Wireless Security ────────────────────────────────────────────────
    {
        "id": "c2d2v3b-007",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Wireless security protocols",
        "stem": (
            "A hospital IT team audits its wireless infrastructure and discovers that "
            "all access points are configured to broadcast the SSID 'HospitalNet'. "
            "The security officer recommends disabling SSID broadcast. A senior engineer "
            "argues that hiding the SSID provides very little security value. Which "
            "response BEST supports the senior engineer's position?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The SSID is still transmitted in probe request and probe response frames from clients, so it can be captured with passive wireless sniffing tools",
                "correct": True,
                "rationale": (
                    "Correct. Even with broadcast disabled, the SSID appears in client "
                    "probe requests (when devices search for the network) and is transmitted "
                    "during association. Tools like Wireshark or Kismet trivially capture "
                    "it. Hiding the SSID is security through obscurity — it adds no real "
                    "cryptographic protection."
                ),
            },
            {
                "id": "b",
                "text": "Hiding the SSID forces clients to use WPA3, improving encryption strength",
                "correct": False,
                "rationale": (
                    "Incorrect. SSID broadcast status is independent of the encryption "
                    "protocol used. Hiding the SSID does not force or change the encryption "
                    "mode of the access point."
                ),
            },
            {
                "id": "c",
                "text": "Disabling SSID broadcast prevents MAC address spoofing by unauthorized clients",
                "correct": False,
                "rationale": (
                    "Incorrect. MAC address spoofing is independent of SSID broadcast "
                    "status. An attacker who discovers the SSID (trivially, via passive "
                    "capture) can still spoof a valid MAC address to associate."
                ),
            },
            {
                "id": "d",
                "text": "Hidden SSIDs are incompatible with WPA2, requiring the network to fall back to WEP",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no incompatibility between hidden SSIDs and "
                    "WPA2. Access points can simultaneously hide the SSID and use any "
                    "encryption protocol."
                ),
            },
        ],
        "explanation": (
            "SSID suppression (hiding broadcast) is a common misconception as a meaningful "
            "security control. The SSID is still exposed in management frames exchanged "
            "during client association and in client probe requests. Any wireless scanner "
            "can reveal hidden SSIDs in seconds. Strong encryption (WPA2/WPA3) and network "
            "access controls (802.1X) provide actual security."
        ),
    },
    {
        "id": "c2d2v3b-008",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Wireless security protocols",
        "stem": (
            "An enterprise deploys WPA2-Enterprise with EAP-TLS. Unlike PEAP, EAP-TLS "
            "requires clients to present a certificate during authentication. Which security "
            "advantage does EAP-TLS provide over PEAP-MSCHAPv2 in this environment?"
        ),
        "options": [
            {
                "id": "a",
                "text": "EAP-TLS performs mutual authentication: both the client and the RADIUS server validate each other's certificates, preventing rogue RADIUS server attacks",
                "correct": True,
                "rationale": (
                    "Correct. EAP-TLS requires both the client to present a valid certificate "
                    "and the RADIUS server to present a valid certificate. This mutual "
                    "authentication eliminates rogue server attacks; neither side accepts "
                    "the other without valid PKI credentials. PEAP-MSCHAPv2 authenticates "
                    "the server only, leaving clients potentially vulnerable if they do not "
                    "verify the server cert."
                ),
            },
            {
                "id": "b",
                "text": "EAP-TLS uses a shorter key length than PEAP, making authentication faster on low-power devices",
                "correct": False,
                "rationale": (
                    "Incorrect. EAP-TLS does not use shorter keys — it uses standard TLS "
                    "with certificates. Speed is not the distinguishing advantage of "
                    "EAP-TLS over PEAP; mutual authentication is."
                ),
            },
            {
                "id": "c",
                "text": "EAP-TLS eliminates the need for a RADIUS server by performing peer-to-peer authentication",
                "correct": False,
                "rationale": (
                    "Incorrect. EAP-TLS still requires a RADIUS server as the "
                    "authentication server. The client certificate is validated against "
                    "the RADIUS server's trusted CA store."
                ),
            },
            {
                "id": "d",
                "text": "EAP-TLS allows users to authenticate with a username and password instead of a certificate for flexibility",
                "correct": False,
                "rationale": (
                    "Incorrect. This describes PEAP-MSCHAPv2, not EAP-TLS. EAP-TLS "
                    "specifically requires client-side certificates — username/password "
                    "authentication is not used in EAP-TLS."
                ),
            },
        ],
        "explanation": (
            "EAP-TLS provides the strongest WPA2-Enterprise authentication because it "
            "mandates certificate-based mutual authentication: the RADIUS server verifies "
            "the client's certificate, and the client verifies the server's certificate. "
            "PEAP-MSCHAPv2 only authenticates the server (via certificate) while the "
            "client uses username/password inside the TLS tunnel — a weaker model if users "
            "fail to verify the server certificate."
        ),
    },
    # ── 2.4 Malware ──────────────────────────────────────────────────────────
    {
        "id": "c2d2v3b-009",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Malware types & removal",
        "stem": (
            "A user reports that their browser's homepage has been changed without their "
            "knowledge, search results now include dozens of advertisements, and a new "
            "toolbar they did not install has appeared. The computer is otherwise functional. "
            "Which malware category BEST describes this infection?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Potentially Unwanted Program (PUP) / adware",
                "correct": True,
                "rationale": (
                    "Correct. Adware (often bundled as a PUP) modifies browser settings "
                    "(homepage, search engine), injects advertisements into browsing "
                    "sessions, and installs toolbars. Unlike ransomware or spyware, its "
                    "primary goal is ad revenue generation, and the system remains "
                    "functional."
                ),
            },
            {
                "id": "b",
                "text": "Ransomware",
                "correct": False,
                "rationale": (
                    "Incorrect. Ransomware encrypts files and demands payment. The "
                    "scenario describes browser modifications and advertisements with "
                    "no file encryption or ransom demand — these are adware characteristics."
                ),
            },
            {
                "id": "c",
                "text": "Rootkit",
                "correct": False,
                "rationale": (
                    "Incorrect. A rootkit provides persistent, hidden privileged access "
                    "and conceals itself from the OS. Browser toolbar and homepage changes "
                    "are visible user-level changes — not the stealthy kernel-level "
                    "concealment that defines a rootkit."
                ),
            },
            {
                "id": "d",
                "text": "Keylogger",
                "correct": False,
                "rationale": (
                    "Incorrect. A keylogger records keystrokes silently and exfiltrates "
                    "them. It does not modify browser settings or display advertisements."
                ),
            },
        ],
        "explanation": (
            "Adware and PUPs are characterized by browser hijacking (homepage/search engine "
            "changes), unwanted toolbars, and injected advertisements. They are often "
            "bundled with free software and the user may have technically consented to "
            "installation in a bundled EULA. Unlike ransomware or rootkits, the system "
            "continues functioning normally."
        ),
    },
    {
        "id": "c2d2v3b-010",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Malware types & removal",
        "stem": (
            "An attacker compromises hundreds of home computers by exploiting an unpatched "
            "vulnerability. The attacker now remotely controls all of them from a central "
            "server. Later, the attacker uses all of these machines simultaneously to send "
            "millions of spam emails. What term describes the collection of compromised "
            "machines under the attacker's control?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Botnet",
                "correct": True,
                "rationale": (
                    "Correct. A botnet is a network of compromised systems ('bots' or "
                    "'zombies') under the centralized control of a command-and-control (C2) "
                    "server. Botnets are used for spam campaigns, DDoS attacks, credential "
                    "stuffing, and other large-scale malicious operations."
                ),
            },
            {
                "id": "b",
                "text": "Worm",
                "correct": False,
                "rationale": (
                    "Incorrect. A worm is the type of malware that self-replicates across "
                    "networks. The collection of machines the worm has compromised and that "
                    "are being used collectively for malicious purposes is specifically "
                    "called a botnet."
                ),
            },
            {
                "id": "c",
                "text": "Trojan",
                "correct": False,
                "rationale": (
                    "Incorrect. A Trojan is a malware delivery mechanism that disguises "
                    "itself as legitimate software. Individual machines may have been "
                    "compromised via a Trojan, but the network of controlled machines "
                    "collectively is the botnet."
                ),
            },
            {
                "id": "d",
                "text": "Spyware",
                "correct": False,
                "rationale": (
                    "Incorrect. Spyware collects information from infected systems. A "
                    "group of compromised systems used collectively by an attacker for "
                    "operational tasks is a botnet, regardless of the initial infection "
                    "mechanism."
                ),
            },
        ],
        "explanation": (
            "A botnet consists of many compromised machines ('bots') controlled by a "
            "threat actor via a command-and-control (C2) infrastructure. They enable "
            "large-scale attacks (spam, DDoS, credential stuffing) that would be "
            "impossible from a single machine. Individual bots often run legitimate "
            "services while performing malicious tasks in the background."
        ),
    },
    {
        "id": "c2d2v3b-011",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Malware types & removal",
        "stem": (
            "After a malware infection is cleaned and the system is restored to production, "
            "which TWO post-remediation actions in the CompTIA 7-step process must occur "
            "in sequence before the end user can be considered fully educated and the "
            "ticket closed? (Choose the answer reflecting the correct pair in the correct order.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Re-enable System Restore and create a new restore point, THEN educate the end user",
                "correct": True,
                "rationale": (
                    "Correct. The CompTIA process: step 6 is re-enable System Restore "
                    "and create a clean restore point; step 7 is educate the end user. "
                    "These are the final two steps performed in this exact order."
                ),
            },
            {
                "id": "b",
                "text": "Educate the end user, THEN re-enable System Restore and create a restore point",
                "correct": False,
                "rationale": (
                    "Incorrect. The order is reversed. System Restore re-enablement (step 6) "
                    "precedes end-user education (step 7) in the CompTIA process."
                ),
            },
            {
                "id": "c",
                "text": "Schedule future scans and update definitions, THEN quarantine the system again",
                "correct": False,
                "rationale": (
                    "Incorrect. Quarantine occurs near the beginning of the process (step 2), "
                    "not after remediation is complete. Scheduling scans (step 5) is correct "
                    "post-remediation, but re-quarantining after cleaning is not a step."
                ),
            },
            {
                "id": "d",
                "text": "Perform a full backup, THEN educate the end user",
                "correct": False,
                "rationale": (
                    "Incorrect. While backing up post-cleanup is good practice, it is not "
                    "a numbered step in the CompTIA 7-step malware removal process. The "
                    "post-remediation sequence is: schedule scans > re-enable Restore > "
                    "educate user."
                ),
            },
        ],
        "explanation": (
            "The CompTIA 7-step malware removal process ends with: "
            "(5) Schedule scans and update definitions, "
            "(6) Re-enable System Restore / create a restore point, "
            "(7) Educate the end user. "
            "Steps 6 and 7 form the correct final pair, in that order."
        ),
    },
    {
        "id": "c2d2v3b-012",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Malware types & removal",
        "stem": (
            "A user clicks a link in an email and is taken to a webpage that looks "
            "exactly like their bank's login page. They enter their credentials and "
            "are then redirected to the real bank site. Their credentials were captured "
            "by the attacker. Which malware-adjacent technique does this webpage represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Credential-harvesting phishing site (spoofed login page)",
                "correct": True,
                "rationale": (
                    "Correct. A spoofed login page that captures credentials and then "
                    "redirects to the legitimate site is a credential-harvesting phishing "
                    "technique. The transparent redirect makes the user believe the "
                    "login succeeded, delaying detection."
                ),
            },
            {
                "id": "b",
                "text": "Ransomware delivery via drive-by download",
                "correct": False,
                "rationale": (
                    "Incorrect. A drive-by download silently downloads and installs malware "
                    "when a page is visited. The scenario describes credential capture via "
                    "a fake form, not malware installation."
                ),
            },
            {
                "id": "c",
                "text": "Rootkit installed via a browser exploit",
                "correct": False,
                "rationale": (
                    "Incorrect. A rootkit requires code execution on the victim system. "
                    "The scenario involves a fake webpage collecting typed credentials — "
                    "no code is installed on the user's machine."
                ),
            },
            {
                "id": "d",
                "text": "Cryptominer injected into browser memory",
                "correct": False,
                "rationale": (
                    "Incorrect. A browser-based cryptominer uses the victim's CPU for "
                    "mining without capturing login credentials. The scenario is credential "
                    "theft via a fake login form."
                ),
            },
        ],
        "explanation": (
            "Phishing-based credential harvesting uses a spoofed login page that captures "
            "username and password, then redirects the user to the legitimate site. The "
            "seamless redirect creates the illusion of a successful login, preventing "
            "immediate suspicion. This is one of the most common account compromise "
            "techniques. Multi-factor authentication limits the damage even when credentials "
            "are stolen."
        ),
    },
    # ── 2.5 Social Engineering / Attacks ─────────────────────────────────────
    {
        "id": "c2d2v3b-013",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Social engineering & attacks",
        "stem": (
            "A user receives a text message appearing to be from their bank stating: "
            "'Your account has been flagged for suspicious activity. Call 1-800-555-0199 "
            "immediately to avoid account suspension.' The phone number does not belong "
            "to the bank. When called, a recorded message asks for account number and PIN. "
            "Which attack combination is this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Smishing followed by vishing",
                "correct": True,
                "rationale": (
                    "Correct. The initial text message is smishing (SMS-based phishing). "
                    "When the victim calls the number, they are subjected to vishing "
                    "(voice-based phishing via the fake recorded phone system). This "
                    "two-stage approach is a common real-world attack pattern."
                ),
            },
            {
                "id": "b",
                "text": "Spear phishing followed by pretexting",
                "correct": False,
                "rationale": (
                    "Incorrect. Spear phishing is targeted email. The initial message is "
                    "via SMS (smishing). Pretexting is an element of the attack (the fake "
                    "security alert), but the delivery vectors are specifically smishing "
                    "and vishing."
                ),
            },
            {
                "id": "c",
                "text": "Pharming followed by whaling",
                "correct": False,
                "rationale": (
                    "Incorrect. Pharming redirects web traffic via DNS/hosts file "
                    "manipulation. Whaling targets high-value executives. Neither "
                    "describes SMS messages to a general user and a fake phone number."
                ),
            },
            {
                "id": "d",
                "text": "Vishing followed by smishing",
                "correct": False,
                "rationale": (
                    "Incorrect. The order is reversed. The SMS text message (smishing) "
                    "arrives first and drives the victim to call the fraudulent number "
                    "(vishing). Smishing initiates, vishing harvests."
                ),
            },
        ],
        "explanation": (
            "Multi-channel social engineering attacks are increasingly common. In this "
            "pattern, an SMS (smishing) message creates urgency and directs the victim to "
            "a fraudulent phone number. When called, the fake IVR system (vishing) "
            "harvests account credentials. The urgency and authority (bank account "
            "suspension threat) are classic social engineering psychological triggers."
        ),
    },
    {
        "id": "c2d2v3b-014",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Social engineering & attacks",
        "stem": (
            "An attacker registers the domain 'micros0ft-support.com' (with a zero "
            "instead of the letter 'o') and sends emails from that domain to employees "
            "claiming to offer Windows update support. Employees who do not carefully "
            "inspect the sender address may believe the email is from Microsoft. "
            "Which attack technique is being used?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Typosquatting (URL hijacking)",
                "correct": True,
                "rationale": (
                    "Correct. Typosquatting registers domain names that closely resemble "
                    "legitimate brands using common misspellings, character substitutions "
                    "(like 0 for o), or similar-looking characters. Victims who don't "
                    "scrutinize the domain are deceived into trusting malicious content."
                ),
            },
            {
                "id": "b",
                "text": "DNS poisoning",
                "correct": False,
                "rationale": (
                    "Incorrect. DNS poisoning corrupts a DNS resolver's cache to redirect "
                    "legitimate domain lookups to malicious IPs. The attack here uses a "
                    "legitimately registered lookalike domain — no DNS poisoning is involved."
                ),
            },
            {
                "id": "c",
                "text": "ARP spoofing",
                "correct": False,
                "rationale": (
                    "Incorrect. ARP spoofing associates the attacker's MAC address with a "
                    "legitimate IP on a LAN segment to intercept traffic. The described "
                    "attack uses a fake lookalike domain name, not ARP manipulation."
                ),
            },
            {
                "id": "d",
                "text": "Session hijacking",
                "correct": False,
                "rationale": (
                    "Incorrect. Session hijacking takes over an authenticated web session "
                    "by stealing a session token. The scenario describes a domain name "
                    "deception technique before any session is established."
                ),
            },
        ],
        "explanation": (
            "Typosquatting (URL hijacking) involves registering domain names that exploit "
            "likely typographical errors or character substitutions users might make "
            "(e.g., micros0ft vs microsoft, g00gle vs google). Combined with phishing "
            "emails, it makes fraudulent sites appear legitimate. Users should always "
            "verify the exact domain in the address bar."
        ),
    },
    {
        "id": "c2d2v3b-015",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Social engineering & attacks",
        "stem": (
            "An attacker successfully intercepts the TLS-encrypted traffic between a "
            "remote employee's laptop and the company's VPN concentrator by inserting "
            "themselves between the two endpoints, decrypting traffic with a fraudulent "
            "certificate, then re-encrypting it to forward to the real server. The "
            "employee's browser shows no certificate warning because the attacker's "
            "certificate was issued by a compromised trusted CA. Which attack is described?"
        ),
        "options": [
            {
                "id": "a",
                "text": "On-path (man-in-the-middle) attack exploiting a compromised certificate authority",
                "correct": True,
                "rationale": (
                    "Correct. An on-path (MITM) attack positions the attacker between "
                    "client and server. Using a certificate issued by a compromised "
                    "trusted CA allows the attacker to terminate TLS on both ends without "
                    "triggering browser warnings — the most dangerous MITM variant."
                ),
            },
            {
                "id": "b",
                "text": "DDoS attack against the VPN concentrator",
                "correct": False,
                "rationale": (
                    "Incorrect. A DDoS floods a target with traffic to deny availability. "
                    "The scenario describes traffic interception with decryption — an "
                    "on-path (MITM) attack aimed at confidentiality, not availability."
                ),
            },
            {
                "id": "c",
                "text": "Pharming attack redirecting DNS to a malicious server",
                "correct": False,
                "rationale": (
                    "Incorrect. Pharming can be an initial step to redirect traffic, but "
                    "the described mechanism — inserting between endpoints and re-encrypting "
                    "with a CA-issued certificate — is the defining characteristic of an "
                    "on-path MITM attack."
                ),
            },
            {
                "id": "d",
                "text": "Replay attack using captured authentication tokens",
                "correct": False,
                "rationale": (
                    "Incorrect. A replay attack reuses previously captured valid "
                    "authentication data. The scenario describes real-time interception "
                    "and decryption of live traffic — on-path MITM."
                ),
            },
        ],
        "explanation": (
            "An on-path (MITM) attack intercepts communications in real time. When the "
            "attacker holds a certificate signed by a trusted CA (through CA compromise or "
            "a rogue CA added to the trust store), TLS interception is invisible to the "
            "browser. Certificate Transparency logs and certificate pinning are defenses "
            "against this advanced variant."
        ),
    },
    {
        "id": "c2d2v3b-016",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Social engineering & attacks",
        "stem": (
            "A network administrator notices that the company website's login page is "
            "receiving thousands of automated login attempts per minute with different "
            "username/password pairs sourced from a publicly leaked credential database. "
            "Which attack type is this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Credential stuffing",
                "correct": True,
                "rationale": (
                    "Correct. Credential stuffing uses previously leaked username/password "
                    "pairs (from other breaches) to attempt logins on a target site, "
                    "exploiting the fact that many people reuse passwords. It differs from "
                    "brute force in that it uses real credential pairs rather than "
                    "exhaustive guessing."
                ),
            },
            {
                "id": "b",
                "text": "Brute force attack",
                "correct": False,
                "rationale": (
                    "Incorrect. Brute force systematically tries all possible password "
                    "combinations. Credential stuffing uses specific known username/password "
                    "pairs from leaked databases — targeted pairs, not exhaustive "
                    "combinations."
                ),
            },
            {
                "id": "c",
                "text": "Dictionary attack",
                "correct": False,
                "rationale": (
                    "Incorrect. A dictionary attack tries common words and phrases as "
                    "passwords for a given username. Credential stuffing pairs specific "
                    "usernames with their actual leaked passwords from previous breaches."
                ),
            },
            {
                "id": "d",
                "text": "Password spraying",
                "correct": False,
                "rationale": (
                    "Incorrect. Password spraying tries one or a few common passwords "
                    "against many accounts to avoid lockout. Credential stuffing uses "
                    "specific matched username/password pairs and attempts many pairs "
                    "per account."
                ),
            },
        ],
        "explanation": (
            "Credential stuffing exploits password reuse: attackers obtain leaked "
            "username/password databases from past breaches and automatically test them "
            "against other services. High success rates occur when users reuse passwords "
            "across sites. Defenses include MFA, breach password detection (checking "
            "HIBP), and bot-detection CAPTCHAs."
        ),
    },
    # ── 2.6 Windows OS Security Settings ─────────────────────────────────────
    {
        "id": "c2d2v3b-017",
        "domain": 2,
        "objective": "2.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows security settings",
        "stem": (
            "A Windows 10 machine is used by multiple local accounts. The IT team wants "
            "to ensure that when any user locks the screen, a second user cannot log in "
            "and view the locked user's session. Which Windows feature enforces this "
            "separation of user sessions at the screen-lock level?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Fast User Switching with individual session isolation",
                "correct": True,
                "rationale": (
                    "Correct. Fast User Switching allows multiple users to have active "
                    "sessions simultaneously; when one user locks their screen, the "
                    "Windows Welcome/Login screen allows a second user to log in without "
                    "the first user's session being exposed. Each session is isolated in "
                    "its own security context."
                ),
            },
            {
                "id": "b",
                "text": "BitLocker full-disk encryption",
                "correct": False,
                "rationale": (
                    "Incorrect. BitLocker encrypts the volume at rest and protects against "
                    "offline access when the machine is powered off. It does not manage "
                    "session isolation between logged-in users on a running system."
                ),
            },
            {
                "id": "c",
                "text": "NTFS permissions set to deny other users access to the Desktop folder",
                "correct": False,
                "rationale": (
                    "Incorrect. NTFS permissions control file system access but do not "
                    "prevent a second user from logging in while the first's session is "
                    "locked, nor do they isolate the running sessions themselves."
                ),
            },
            {
                "id": "d",
                "text": "Disabling the Guest account in Local Users and Groups",
                "correct": False,
                "rationale": (
                    "Incorrect. Disabling the Guest account prevents unauthenticated or "
                    "guest-level access. It does not govern how active sessions are "
                    "isolated from each other when the screen is locked."
                ),
            },
        ],
        "explanation": (
            "Windows Fast User Switching allows multiple users to maintain simultaneous "
            "active sessions. Each session runs in its own isolated security context. "
            "When a user locks their screen, others can log in via the lock/logon screen "
            "without seeing the first user's desktop. This is distinct from logoff, which "
            "terminates the session entirely."
        ),
    },
    {
        "id": "c2d2v3b-018",
        "domain": 2,
        "objective": "2.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "NTFS vs share permissions",
        "stem": (
            "A user with Modify NTFS permission on a file moves that file from Folder A "
            "to Folder B on the SAME NTFS volume. Folder B has an ACL where only "
            "Administrators have Full Control and no other users have permissions. "
            "What are the file's NTFS permissions after the move?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The file retains its original permissions from Folder A, not inheriting Folder B's ACL",
                "correct": True,
                "rationale": (
                    "Correct. When a file is MOVED within the same NTFS volume, it retains "
                    "its original explicit permissions. It does not inherit the destination "
                    "folder's permissions. This differs from a copy operation, which always "
                    "inherits the destination's permissions."
                ),
            },
            {
                "id": "b",
                "text": "The file inherits Folder B's ACL (Administrators only)",
                "correct": False,
                "rationale": (
                    "Incorrect. Permission inheritance on move applies when the file is "
                    "moved to a DIFFERENT NTFS volume (which is treated as copy + delete). "
                    "Within the same volume, the original permissions are retained."
                ),
            },
            {
                "id": "c",
                "text": "The file loses all permissions and becomes inaccessible to all users",
                "correct": False,
                "rationale": (
                    "Incorrect. A same-volume move preserves the file's existing explicit "
                    "permissions. No permissions are lost or blanked during a same-volume "
                    "NTFS move."
                ),
            },
            {
                "id": "d",
                "text": "The file's permissions are merged: both Folder A's original ACL and Folder B's ACL apply",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no merging of ACLs during a file move. The file "
                    "either retains original permissions (same-volume move) or inherits "
                    "destination permissions (cross-volume move or copy). No blending occurs."
                ),
            },
        ],
        "explanation": (
            "NTFS move/copy rules: "
            "MOVE (same NTFS volume) — file retains its original explicit permissions. "
            "MOVE (different NTFS volume) — treated as copy then delete; inherits "
            "destination permissions. "
            "COPY (any location) — always inherits destination folder's permissions. "
            "This is a commonly tested CompTIA A+ distinction."
        ),
    },
    {
        "id": "c2d2v3b-019",
        "domain": 2,
        "objective": "2.6",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "BitLocker & encryption (EFS)",
        "stem": (
            "An employee encrypts a sensitive folder using EFS on her Windows 10 workstation. "
            "She is then promoted and given a new domain account. When she logs in with "
            "the new account and tries to open the encrypted files, access is denied. "
            "No data recovery agent (DRA) has been configured. Which is the MOST accurate "
            "explanation for why she cannot access the files?"
        ),
        "options": [
            {
                "id": "a",
                "text": "EFS encryption is tied to her old user certificate; the new account does not possess the private key needed to decrypt the files",
                "correct": True,
                "rationale": (
                    "Correct. EFS encrypts a symmetric file encryption key (FEK) using "
                    "the user's public key certificate. Decryption requires the matching "
                    "private key, which is stored in the user profile. The new account "
                    "has a different certificate/key pair and no access to the old "
                    "private key, so it cannot decrypt."
                ),
            },
            {
                "id": "b",
                "text": "The NTFS permissions were reset when the account changed, blocking access",
                "correct": False,
                "rationale": (
                    "Incorrect. While NTFS permissions could prevent access, the question "
                    "specifies the denial is after promotion with a new account. The EFS "
                    "certificate mismatch is the precise cause of the access denial when "
                    "EFS is used."
                ),
            },
            {
                "id": "c",
                "text": "EFS is disabled for promoted accounts by Group Policy",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no GPO behavior that specifically disables EFS "
                    "access for promoted accounts. The access denial stems from the "
                    "cryptographic relationship between the encrypted data and the user's "
                    "original certificate."
                ),
            },
            {
                "id": "d",
                "text": "BitLocker encrypted the drive after the EFS files were created, making them double-encrypted and inaccessible",
                "correct": False,
                "rationale": (
                    "Incorrect. BitLocker and EFS can coexist. BitLocker encrypts the "
                    "volume transparently below the file system level; once the drive is "
                    "unlocked, EFS operates normally. Double encryption does not cause "
                    "the access denial described."
                ),
            },
        ],
        "explanation": (
            "EFS uses asymmetric cryptography: the file's FEK is encrypted with the "
            "user's public key and stored in the file's Data Decryption Field (DDF). "
            "Decryption requires the corresponding private key from the user's certificate "
            "store. A new domain account has a completely different certificate/key pair. "
            "Best practice is to export the EFS certificate before account changes, or "
            "configure a Data Recovery Agent (DRA) for organizational access recovery."
        ),
    },
    {
        "id": "c2d2v3b-020",
        "domain": 2,
        "objective": "2.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows security settings",
        "stem": (
            "A Windows 10 workstation is shared among three employees working different "
            "shifts. Security policy requires that each user can only access their own "
            "files and that no user can install software or modify system settings. "
            "Which account type should each of the three employees use?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Standard User account",
                "correct": True,
                "rationale": (
                    "Correct. Standard User accounts cannot install software or modify "
                    "system-level settings. They can run existing applications and access "
                    "their own files in their profile but are restricted from privileged "
                    "operations — exactly matching the stated requirements."
                ),
            },
            {
                "id": "b",
                "text": "Local Administrator account",
                "correct": False,
                "rationale": (
                    "Incorrect. Local Administrator has full control over the machine, "
                    "including software installation and system modification. This violates "
                    "both stated restrictions."
                ),
            },
            {
                "id": "c",
                "text": "Guest account",
                "correct": False,
                "rationale": (
                    "Incorrect. The Guest account has the fewest privileges, does not "
                    "persist session data, and is intended for temporary/anonymous access "
                    "— not for regular shift employees who need persistent personal file "
                    "storage."
                ),
            },
            {
                "id": "d",
                "text": "Power User account",
                "correct": False,
                "rationale": (
                    "Incorrect. The Power User group (legacy) had elevated rights above "
                    "Standard User and could install some software. This exceeds the "
                    "required privilege level. In modern Windows, Power Users have "
                    "essentially the same rights as Standard Users, but the question "
                    "targets the correct named type."
                ),
            },
        ],
        "explanation": (
            "Standard User is the correct account type for day-to-day use under a "
            "least-privilege model: users can run applications and access their own profile "
            "data but cannot install software, change system settings, or access other "
            "users' files without explicit permission. This is the CompTIA-recommended "
            "baseline for shared workstations."
        ),
    },
    # ── 2.7 Mobile/Embedded Device Security ──────────────────────────────────
    {
        "id": "c2d2v3b-021",
        "domain": 2,
        "objective": "2.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile/embedded device security",
        "stem": (
            "A user installs an unofficial app on their Android phone by downloading "
            "an APK from a third-party website rather than from the Google Play Store. "
            "Which mobile security risk does this practice primarily introduce compared "
            "to installing from the official app store?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The app bypasses the Google Play Protect malware scanning process, increasing risk of installing malicious code",
                "correct": True,
                "rationale": (
                    "Correct. Sideloading (installing APKs from unofficial sources) "
                    "bypasses Google Play's vetting and Play Protect scanning. Malicious "
                    "apps that would be rejected or detected in the Play Store can be "
                    "distributed as sideloaded APKs, dramatically increasing malware "
                    "installation risk."
                ),
            },
            {
                "id": "b",
                "text": "Sideloaded apps always require root access, permanently weakening OS security",
                "correct": False,
                "rationale": (
                    "Incorrect. Sideloading (enabling 'Unknown Sources') does not require "
                    "root access. It simply allows installation outside the Play Store. "
                    "Rooting is a separate, more invasive modification."
                ),
            },
            {
                "id": "c",
                "text": "The app cannot access the internet because it is not registered in the Play Store",
                "correct": False,
                "rationale": (
                    "Incorrect. Internet access is controlled by Android permissions, not "
                    "by whether an app came from the Play Store. A sideloaded app with "
                    "internet permission can communicate freely."
                ),
            },
            {
                "id": "d",
                "text": "Sideloaded apps are automatically sandboxed away from the OS kernel",
                "correct": False,
                "rationale": (
                    "Incorrect. Android's sandbox model applies to all apps regardless "
                    "of installation source. The security risk of sideloading is not the "
                    "absence of sandboxing, but the absence of Play Store vetting and "
                    "Play Protect scanning."
                ),
            },
        ],
        "explanation": (
            "Sideloading bypasses the app store's malware review and runtime scanning. "
            "Google Play Protect scans apps both at installation and periodically for known "
            "malware. Third-party APKs skip this layer entirely. Organizations manage this "
            "risk through MDM policies that disallow Unknown Sources or restrict app "
            "installation to approved sources."
        ),
    },
    {
        "id": "c2d2v3b-022",
        "domain": 2,
        "objective": "2.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile/embedded device security",
        "stem": (
            "A company's MDM policy enforces full-device encryption on all enrolled "
            "smartphones. An employee's phone is confiscated by customs at an "
            "international border crossing, and officials attempt to access the data. "
            "The employee has a strong 12-character PIN. Which statement BEST describes "
            "the protection the encryption provides in this scenario?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Device encryption renders the storage unreadable without the correct PIN/passphrase; the data is protected if the attacker cannot bypass the PIN",
                "correct": True,
                "rationale": (
                    "Correct. Full-device encryption ensures that storage media is "
                    "cryptographically unreadable without the correct decryption credential. "
                    "If the PIN is strong and not compelled, the data remains protected "
                    "even if the device is physically removed or the storage chip is "
                    "accessed directly."
                ),
            },
            {
                "id": "b",
                "text": "Encryption is automatically bypassed when law enforcement presents official credentials",
                "correct": False,
                "rationale": (
                    "Incorrect. Device encryption does not have a law-enforcement bypass "
                    "built into the cryptographic mechanism. Access requires the decryption "
                    "key/PIN or a court order compelling disclosure, not a technical bypass."
                ),
            },
            {
                "id": "c",
                "text": "Encryption only protects data when the device is powered off; once powered on and unlocked, data is not protected",
                "correct": False,
                "rationale": (
                    "Incorrect. Encryption protects data at rest regardless of power state. "
                    "Once unlocked (PIN entered), the OS decrypts data in memory as needed "
                    "— but the risk scenario here (physical confiscation) involves the "
                    "device being powered off and the storage accessed directly."
                ),
            },
            {
                "id": "d",
                "text": "MDM enrollment invalidates encryption if the device is disconnected from the corporate network",
                "correct": False,
                "rationale": (
                    "Incorrect. Device encryption operates independently of network "
                    "connectivity. The encryption keys are stored on-device (often in "
                    "a secure enclave or TPM-equivalent); MDM enrollment does not affect "
                    "the encryption status when offline."
                ),
            },
        ],
        "explanation": (
            "Full-device encryption (Android FDE/FBE, iOS data protection) ensures that "
            "storage contents are cryptographically protected when the device is locked. "
            "Physically removing the storage or chip-off forensics is defeated by "
            "encryption if the decryption key (derived from the PIN/passphrase) is not "
            "available. A strong, unique PIN is essential; weak PINs can be brute-forced."
        ),
    },
    {
        "id": "c2d2v3b-023",
        "domain": 2,
        "objective": "2.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile/embedded device security",
        "stem": (
            "A company security policy prohibits employees from jailbreaking or rooting "
            "their mobile devices enrolled in MDM. An employee's iPhone is detected by "
            "the MDM as having been jailbroken. Which security concern BEST justifies "
            "this policy restriction?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Jailbreaking removes iOS security sandbox restrictions, allowing apps to access data and system resources they should not be permitted to reach",
                "correct": True,
                "rationale": (
                    "Correct. Jailbreaking (iOS) and rooting (Android) bypass the "
                    "operating system's security model, removing the app sandbox and "
                    "allowing apps with root/superuser access to access any file, process, "
                    "or hardware on the device. This defeats the security controls that "
                    "protect corporate data stored in MDM-managed containers."
                ),
            },
            {
                "id": "b",
                "text": "Jailbreaking increases battery consumption, reducing device availability for work tasks",
                "correct": False,
                "rationale": (
                    "Incorrect. While jailbreaking may affect battery life, that is an "
                    "operational concern, not a security justification. The security "
                    "rationale is the removal of OS security controls."
                ),
            },
            {
                "id": "c",
                "text": "Jailbroken devices cannot connect to Wi-Fi, making mobile work impossible",
                "correct": False,
                "rationale": (
                    "Incorrect. Jailbroken devices retain full Wi-Fi connectivity. "
                    "This statement is factually incorrect."
                ),
            },
            {
                "id": "d",
                "text": "Jailbreaking voids the device warranty, creating a financial liability for the company",
                "correct": False,
                "rationale": (
                    "Incorrect. Warranty implications are a concern but represent a "
                    "financial, not a security, risk. The policy restriction is security-"
                    "motivated: jailbreaking undermines the MDM's ability to enforce "
                    "security policies and compromises data protection."
                ),
            },
        ],
        "explanation": (
            "Jailbreaking (iOS) and rooting (Android) remove the OS-enforced security "
            "sandbox, granting apps superuser (root) access. This allows malicious apps "
            "to read MDM-protected corporate data containers, bypass screen lock, extract "
            "encryption keys, and circumvent MDM controls. MDM solutions typically detect "
            "jailbreak/root status and can quarantine or wipe non-compliant devices."
        ),
    },
    # ── 2.8 Data Destruction & Disposal ──────────────────────────────────────
    {
        "id": "c2d2v3b-024",
        "domain": 2,
        "objective": "2.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Data destruction & disposal",
        "stem": (
            "A company is retiring a fleet of solid-state drives (SSDs) that stored "
            "confidential customer data. The IT manager wants to ensure the data is "
            "unrecoverable while keeping the drives functional for potential resale. "
            "Which method is MOST appropriate for SSDs in this scenario?"
        ),
        "options": [
            {
                "id": "a",
                "text": "ATA Secure Erase command (manufacturer's secure erase tool)",
                "correct": True,
                "rationale": (
                    "Correct. The ATA Secure Erase (SE) command — executed through the "
                    "drive's own firmware — cryptographically resets and sanitizes all "
                    "flash cells, including those in the drive's over-provisioning area. "
                    "This is the recommended method for SSD sanitization that preserves "
                    "drive functionality for reuse per NIST 800-88."
                ),
            },
            {
                "id": "b",
                "text": "Multi-pass overwrite using a software wiping tool (e.g., DoD 5220.22-M)",
                "correct": False,
                "rationale": (
                    "Incorrect. Multi-pass overwriting is effective for HDDs but unreliable "
                    "for SSDs. SSDs use wear leveling and over-provisioning, meaning some "
                    "flash cells that contain data may not be overwritten by software "
                    "tools. ATA Secure Erase handles the entire drive including hidden "
                    "areas."
                ),
            },
            {
                "id": "c",
                "text": "Degaussing the drives",
                "correct": False,
                "rationale": (
                    "Incorrect. Degaussing uses a magnetic field to destroy magnetic "
                    "media. SSDs use flash memory, which is not magnetic — degaussing "
                    "has no effect on SSD data and does not destroy it."
                ),
            },
            {
                "id": "d",
                "text": "Quick format and reinstall the OS on each drive",
                "correct": False,
                "rationale": (
                    "Incorrect. A quick format removes only the file system metadata; "
                    "actual data on the NAND cells remains and is recoverable with "
                    "forensic tools. This is never acceptable for confidential data "
                    "sanitization."
                ),
            },
        ],
        "explanation": (
            "SSDs require different sanitization than HDDs due to wear leveling and "
            "over-provisioning areas that are inaccessible to the OS. The ATA Secure "
            "Erase command instructs the drive's firmware to sanitize all storage cells "
            "including those hidden from the OS. NIST SP 800-88 recommends this method "
            "for SSD sanitization when drives are to be reused. Degaussing is ineffective "
            "on flash memory."
        ),
    },
    {
        "id": "c2d2v3b-025",
        "domain": 2,
        "objective": "2.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Data destruction & disposal",
        "stem": (
            "A healthcare organization needs to dispose of printed patient records in "
            "compliance with HIPAA. The records contain full names, diagnosis codes, "
            "and Social Security numbers. Which disposal method is required?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Cross-cut shredding of all documents before disposal",
                "correct": True,
                "rationale": (
                    "Correct. Cross-cut shredding (also called confetti or micro-cut "
                    "shredding) renders paper documents unreadable and unreconstruct-ible. "
                    "HIPAA requires that PHI (Protected Health Information) on paper be "
                    "shredded or otherwise rendered unreadable/unreconstruc-table prior "
                    "to disposal. Strip-cut shredding is less secure."
                ),
            },
            {
                "id": "b",
                "text": "Place records in a locked recycling bin for standard paper recycling",
                "correct": False,
                "rationale": (
                    "Incorrect. Standard recycling — even in a locked bin — does not "
                    "render the documents unreadable. Unshredded PHI in recycling bins "
                    "is a HIPAA violation and constitutes dumpster diving vulnerability."
                ),
            },
            {
                "id": "c",
                "text": "Mark records as 'Confidential' and file them in a locked storage room indefinitely",
                "correct": False,
                "rationale": (
                    "Incorrect. Indefinite retention of records no longer needed is not "
                    "disposal. HIPAA has specific retention and destruction requirements; "
                    "when records are no longer needed and are to be disposed of, physical "
                    "destruction (shredding) is required."
                ),
            },
            {
                "id": "d",
                "text": "Burn records in an open container outside the facility",
                "correct": False,
                "rationale": (
                    "Incorrect. While incineration can destroy documents, open burning "
                    "is typically prohibited by local environmental regulations. Shredding "
                    "by a certified HIPAA-compliant shredding service is the standard "
                    "compliant method."
                ),
            },
        ],
        "explanation": (
            "HIPAA's Privacy Rule (45 CFR 164.310(d)(2)(i)) requires covered entities to "
            "render PHI unusable, unreadable, or indecipherable when disposing of physical "
            "media containing PHI. For paper, cross-cut shredding is the standard method. "
            "Many organizations use certified on-site or off-site shredding services with "
            "certificates of destruction."
        ),
    },
    # ── 2.9 SOHO Network Security ─────────────────────────────────────────────
    {
        "id": "c2d2v3b-026",
        "domain": 2,
        "objective": "2.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SOHO network security",
        "stem": (
            "A small office manager calls a technician because their SOHO router's "
            "admin panel is accessible from the internet and someone has logged in and "
            "changed settings. The router was using the factory-default credentials. "
            "After restoring the configuration, which TWO changes are the MOST critical "
            "to prevent recurrence? (Choose the single BEST answer representing the "
            "essential pair.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Change the default administrator credentials AND disable remote management (WAN-side admin access)",
                "correct": True,
                "rationale": (
                    "Correct. The attack succeeded because (1) default credentials were "
                    "in use and (2) remote WAN management was enabled. Changing the "
                    "admin password eliminates the credential vector; disabling remote "
                    "management removes the attack surface entirely. Both changes are "
                    "required to prevent recurrence."
                ),
            },
            {
                "id": "b",
                "text": "Enable UPnP and increase DHCP lease time",
                "correct": False,
                "rationale": (
                    "Incorrect. UPnP creates additional security risks by allowing "
                    "devices to open ports automatically. Increasing DHCP lease time "
                    "has no effect on remote management access. Neither addresses the "
                    "actual attack vector."
                ),
            },
            {
                "id": "c",
                "text": "Change the SSID to a non-default name and enable guest network isolation",
                "correct": False,
                "rationale": (
                    "Incorrect. Changing the SSID removes model fingerprinting and guest "
                    "isolation improves LAN segmentation, but neither prevents an attacker "
                    "with internet access from exploiting WAN-accessible admin panel with "
                    "default credentials."
                ),
            },
            {
                "id": "d",
                "text": "Configure MAC address filtering and set DHCP reservations for all LAN devices",
                "correct": False,
                "rationale": (
                    "Incorrect. MAC filtering and DHCP reservations manage LAN access. "
                    "They have no effect on WAN-side remote management access, which was "
                    "the actual attack vector in this scenario."
                ),
            },
        ],
        "explanation": (
            "Remote management enabled on the WAN interface combined with default credentials "
            "is one of the most dangerous SOHO router configurations. The two essential "
            "remediations are: (1) change default admin credentials immediately, and "
            "(2) disable WAN-side (remote) management so the admin interface is only "
            "accessible from the local LAN. Most SOHO routers should never have remote "
            "management enabled."
        ),
    },
    {
        "id": "c2d2v3b-027",
        "domain": 2,
        "objective": "2.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SOHO network security",
        "stem": (
            "A home user wants to prevent their smart TV, wireless printer, and IoT "
            "thermostat from communicating directly with their laptop or NAS storage "
            "device on the same Wi-Fi network. Which SOHO router feature accomplishes "
            "this without creating a separate SSID?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Client isolation (AP isolation / wireless client isolation)",
                "correct": True,
                "rationale": (
                    "Correct. Client isolation (also called AP isolation or wireless "
                    "isolation) prevents wireless clients on the same SSID from "
                    "communicating directly with each other while still allowing them "
                    "to reach the internet/router. It does not require a second SSID."
                ),
            },
            {
                "id": "b",
                "text": "Enabling WPA3 encryption on the access point",
                "correct": False,
                "rationale": (
                    "Incorrect. WPA3 improves encryption strength for wireless traffic "
                    "between clients and the AP. It does not prevent wireless clients "
                    "from communicating with each other on the same network."
                ),
            },
            {
                "id": "c",
                "text": "Disabling DHCP and assigning static IP addresses to all devices",
                "correct": False,
                "rationale": (
                    "Incorrect. Static IP addresses have no effect on whether clients "
                    "can communicate with each other. Layer 2 communication between "
                    "wireless clients is controlled by AP isolation, not IP addressing."
                ),
            },
            {
                "id": "d",
                "text": "Creating a guest SSID for IoT devices",
                "correct": False,
                "rationale": (
                    "Incorrect. A guest SSID would require putting IoT devices on a "
                    "separate SSID — but the question specifically asks for a solution "
                    "that works without a separate SSID. Client isolation achieves "
                    "this on the same SSID."
                ),
            },
        ],
        "explanation": (
            "Client (AP) isolation is a SOHO router/AP feature that prevents wireless "
            "stations associated with the same SSID from communicating with each other "
            "at Layer 2. All client traffic is forced through the router rather than "
            "being switched directly. This provides lateral movement protection for "
            "IoT devices without requiring VLAN configuration or a second SSID."
        ),
    },
]

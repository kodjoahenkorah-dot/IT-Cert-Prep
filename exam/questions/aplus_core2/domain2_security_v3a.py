"""
CompTIA A+ Core 2 (220-1202) — Domain 2: Security  (v3)
47 exam-quality questions — IDs c2d2v3-001 through c2d2v3-047.
"""

QUESTIONS = [
    # ── 2.1 Physical Security ────────────────────────────────────────────────
    {
        "id": "c2d2v3-001",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Physical security",
        "stem": (
            "A retail store manager notices that employees are allowing customers to "
            "follow them into the stockroom by holding the door open out of courtesy. "
            "Management wants a technology control that physically enforces one-person-at-a-"
            "time entry without relying on employee vigilance. Which control BEST satisfies "
            "this requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Access control vestibule (mantrap) at the stockroom entrance",
                "correct": True,
                "rationale": (
                    "Correct. An access control vestibule uses two interlocking doors: "
                    "the second door will not open until the first is fully closed and "
                    "the credential is re-verified, physically preventing more than one "
                    "person from passing through per authentication event."
                ),
            },
            {
                "id": "b",
                "text": "Badge reader on the stockroom door",
                "correct": False,
                "rationale": (
                    "Incorrect. A badge reader grants access on credential validation but "
                    "does not physically prevent a second person from stepping through the "
                    "open door behind the badge holder — the courtesy-hold problem persists."
                ),
            },
            {
                "id": "c",
                "text": "Motion-activated alarm inside the stockroom",
                "correct": False,
                "rationale": (
                    "Incorrect. A motion alarm detects presence after the fact but cannot "
                    "prevent an unauthorized person from entering in the first place."
                ),
            },
            {
                "id": "d",
                "text": "Security guard posted at the stockroom entrance",
                "correct": False,
                "rationale": (
                    "Incorrect. A guard can enforce the policy but relies on human vigilance "
                    "— the same weakness that already exists. A mantrap is a technological, "
                    "not procedural, control that removes the human-error element."
                ),
            },
        ],
        "explanation": (
            "The access control vestibule (mantrap) is the only listed control that "
            "physically enforces single-person passage independent of employee behavior. "
            "Badge readers, guards, and alarms all have enforcement gaps when courtesy "
            "hold is the root problem."
        ),
    },
    {
        "id": "c2d2v3-002",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Physical security",
        "stem": (
            "A data center audit reveals that server racks are accessible from the cold "
            "aisle to anyone who enters the building. The facility already uses perimeter "
            "fencing and a badge reader at the main entrance. Which security model concept "
            "does the LACK of rack-level locks violate, and what control should be added?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Defense in depth is violated; individual locking rack cabinets should be added as an additional layer",
                "correct": True,
                "rationale": (
                    "Correct. Defense in depth layers multiple independent controls so that "
                    "defeating one (e.g., social engineering past the badge reader) does not "
                    "grant unrestricted access. Locking rack cabinets add a third physical "
                    "layer inside the perimeter and building badge layers."
                ),
            },
            {
                "id": "b",
                "text": "Least privilege is violated; user accounts should be restricted to read-only",
                "correct": False,
                "rationale": (
                    "Incorrect. Least privilege governs logical/software access rights, "
                    "not physical hardware access. The gap described is a physical security "
                    "layering problem."
                ),
            },
            {
                "id": "c",
                "text": "Separation of duties is violated; two employees should be required to access a rack",
                "correct": False,
                "rationale": (
                    "Incorrect. Separation of duties prevents a single person from completing "
                    "a critical process alone (for fraud prevention). The issue here is "
                    "unrestricted physical rack access — a defense-in-depth gap, not a "
                    "separation of duties problem."
                ),
            },
            {
                "id": "d",
                "text": "Need-to-know is violated; a new policy document should be issued to staff",
                "correct": False,
                "rationale": (
                    "Incorrect. Need-to-know is an information access principle. The problem "
                    "is that there is no physical barrier at the rack — a policy document "
                    "alone cannot provide that control."
                ),
            },
        ],
        "explanation": (
            "Defense in depth requires layered physical controls: perimeter fence, building "
            "access control, and then rack/cabinet locks. Bypassing any outer layer still "
            "leaves inner layers. Adding locking cabinets closes the gap that exists when "
            "someone gains building entry by other means."
        ),
    },
    {
        "id": "c2d2v3-003",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Physical security",
        "stem": (
            "A property manager wants to verify the identity of every visitor before "
            "allowing them into a secure research lab, and keep a log of all entries. "
            "The lab has no automated badge system. Which physical security measure BEST "
            "meets both requirements?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Staffed reception desk with visitor sign-in log and escort policy",
                "correct": True,
                "rationale": (
                    "Correct. A staffed reception with a sign-in log verifies identity via "
                    "government ID, creates an audit trail of entries, and an escort policy "
                    "ensures visitors are supervised — meeting both stated requirements "
                    "without requiring an automated badge system."
                ),
            },
            {
                "id": "b",
                "text": "Biometric fingerprint scanner on the lab door",
                "correct": False,
                "rationale": (
                    "Incorrect. A biometric scanner authenticates enrolled individuals but "
                    "cannot verify the identity of visitors who have not had their biometrics "
                    "enrolled in advance, and does not fulfill the visitor log requirement for "
                    "non-enrolled guests."
                ),
            },
            {
                "id": "c",
                "text": "CCTV cameras at all building entrances",
                "correct": False,
                "rationale": (
                    "Incorrect. CCTV cameras record who entered but do not actively verify "
                    "identity before granting access, nor do they create a real-time visitor "
                    "log as required."
                ),
            },
            {
                "id": "d",
                "text": "Proximity card readers on all internal doors",
                "correct": False,
                "rationale": (
                    "Incorrect. Proximity card readers work for enrolled badge holders, not "
                    "external visitors who have not been issued badges. They do not satisfy "
                    "the visitor identity verification and logging requirement."
                ),
            },
        ],
        "explanation": (
            "For visitor management without automated systems, a staffed reception with "
            "manual sign-in and government ID check is the standard control. It provides "
            "both identity verification and an auditable entry log. Biometrics and badge "
            "readers require prior enrollment, making them unsuitable for ad hoc visitors."
        ),
    },
    # ── 2.2 Logical Security / Active Directory ──────────────────────────────
    {
        "id": "c2d2v3-004",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Logical security & Active Directory",
        "stem": (
            "A domain administrator must ensure that all Windows 10 domain computers "
            "display a legal warning banner before the Windows logon dialog appears. "
            "Which is the MOST efficient way to deploy this across 300 computers?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Configure the Interactive logon: Message text and title settings in a GPO applied to the Computers OU",
                "correct": True,
                "rationale": (
                    "Correct. The 'Interactive logon: Message text for users attempting to "
                    "log on' and companion title policy settings, deployed via a GPO linked "
                    "to the OU containing computer accounts, automatically push the banner "
                    "to all 300 machines without touching each one individually."
                ),
            },
            {
                "id": "b",
                "text": "Edit the registry manually on each computer under HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon",
                "correct": False,
                "rationale": (
                    "Incorrect. Manual registry edits achieve the same result but require "
                    "touching all 300 machines individually — not efficient and introduces "
                    "human error risk. GPO is the scalable enterprise method."
                ),
            },
            {
                "id": "c",
                "text": "Send an email to all users instructing them to configure the banner in their user profiles",
                "correct": False,
                "rationale": (
                    "Incorrect. Logon banners are system-level settings, not user-profile "
                    "settings. Users cannot configure pre-logon messages, and relying on "
                    "user action guarantees inconsistency."
                ),
            },
            {
                "id": "d",
                "text": "Use a login script assigned to each user account to display a message box",
                "correct": False,
                "rationale": (
                    "Incorrect. Login scripts run after logon, not before the logon dialog. "
                    "A legal notice banner must appear before credential entry — which "
                    "requires a machine-level GPO setting, not a post-logon script."
                ),
            },
        ],
        "explanation": (
            "Pre-logon banners are configured via Computer Configuration > Windows Settings > "
            "Security Settings > Local Policies > Security Options in GPO. This is the "
            "authoritative, scalable method for domain environments. Manual registry edits "
            "and login scripts are either impractical at scale or executed at the wrong point "
            "in the logon sequence."
        ),
    },
    {
        "id": "c2d2v3-005",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Logical security & Active Directory",
        "stem": (
            "An IT admin creates a new Active Directory security group called 'Finance-Read' "
            "and adds it to the ACL of a shared folder with Read permission. She then adds "
            "user JSmith to both the 'Finance-Read' group (Read) and the 'Finance-Edit' "
            "group (Modify). JSmith accesses the folder over the network. The share "
            "permission is Full Control for Everyone. What is JSmith's effective NTFS "
            "permission on the folder?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Modify — NTFS permissions accumulate across group memberships, and Modify is the highest NTFS right JSmith holds",
                "correct": True,
                "rationale": (
                    "Correct. NTFS permissions are cumulative across group memberships: "
                    "JSmith has Read (from Finance-Read) AND Modify (from Finance-Edit). "
                    "The effective NTFS permission is the union — Modify (which includes Read). "
                    "The share is Full Control for Everyone, which is less restrictive than "
                    "Modify, so the network effective permission is also Modify."
                ),
            },
            {
                "id": "b",
                "text": "Read — the most restrictive NTFS group permission applies",
                "correct": False,
                "rationale": (
                    "Incorrect. NTFS Allow permissions accumulate (are combined), not "
                    "restricted to the lowest. The most-restrictive rule applies when "
                    "comparing NTFS vs. share permissions over the network, not among "
                    "multiple Allow NTFS entries."
                ),
            },
            {
                "id": "c",
                "text": "Full Control — the share permission of Full Control for Everyone overrides NTFS",
                "correct": False,
                "rationale": (
                    "Incorrect. Share permissions do not override NTFS; the effective "
                    "network permission is the more restrictive of the two. Modify (NTFS) "
                    "is more restrictive than Full Control (share), so the result is Modify."
                ),
            },
            {
                "id": "d",
                "text": "No Access — conflicting permissions always result in denial",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no explicit Deny in this scenario. Conflicting "
                    "Allow levels resolve to the cumulative NTFS permission (Modify) "
                    "intersected with the share permission (Full Control), yielding Modify."
                ),
            },
        ],
        "explanation": (
            "Key rules: (1) NTFS Allow permissions from multiple groups are CUMULATIVE "
            "(union). (2) Over the network, effective access = more restrictive of "
            "(combined NTFS) and (combined share). Here combined NTFS = Modify, share = "
            "Full Control. Modify is more restrictive, so the answer is Modify."
        ),
    },
    {
        "id": "c2d2v3-006",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Logical security & Active Directory",
        "stem": (
            "A user calls the help desk saying she can no longer log into the domain after "
            "returning from a three-week vacation. Her password has not expired. Which is the "
            "MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The account was disabled due to inactivity under an account lockout or idle-account policy",
                "correct": True,
                "rationale": (
                    "Correct. Many organizations configure Active Directory to automatically "
                    "disable accounts that have been inactive for a defined number of days "
                    "(e.g., 30 days). After a three-week absence without login activity, an "
                    "idle-account policy could have disabled the account."
                ),
            },
            {
                "id": "b",
                "text": "The user's password complexity requirement was increased and now fails validation",
                "correct": False,
                "rationale": (
                    "Incorrect. A password complexity change would not lock out an existing "
                    "password mid-session; it would only apply when the user next changes "
                    "their password. The existing password would still work."
                ),
            },
            {
                "id": "c",
                "text": "The domain controller is offline and cannot authenticate any users",
                "correct": False,
                "rationale": (
                    "Incorrect. If the DC were offline, all domain users would be unable "
                    "to log in, not just this specific user. The scenario describes a "
                    "single-user issue."
                ),
            },
            {
                "id": "d",
                "text": "Kerberos ticket lifetime expired and a new ticket cannot be obtained",
                "correct": False,
                "rationale": (
                    "Incorrect. Kerberos ticket lifetimes (typically 10 hours) are refreshed "
                    "at each logon attempt. An expired ticket would not prevent a new logon — "
                    "it would simply trigger issuance of a new TGT."
                ),
            },
        ],
        "explanation": (
            "Active Directory can enforce account-inactivity policies that disable accounts "
            "not used within a set window. After three weeks away, this policy is the most "
            "likely culprit when the password is confirmed valid. The admin should check "
            "whether the account shows as disabled in ADUC."
        ),
    },
    # ── 2.3 Wireless Security ────────────────────────────────────────────────
    {
        "id": "c2d2v3-007",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Wireless security protocols",
        "stem": (
            "A technician discovers that a SOHO access point was left configured with WEP "
            "encryption. A colleague argues that WEP is fine because it still encrypts "
            "traffic. Which response BEST explains why WEP must be replaced immediately?"
        ),
        "options": [
            {
                "id": "a",
                "text": "WEP uses static, short IVs with RC4, making it trivially crackable in minutes with freely available tools regardless of key length",
                "correct": True,
                "rationale": (
                    "Correct. WEP's fatal flaw is its 24-bit Initialization Vector (IV) "
                    "space, which is exhausted quickly on a busy network. IV reuse exposes "
                    "the keystream to attack; tools like Aircrack-ng can crack WEP keys in "
                    "under two minutes from captured packets — making encryption meaningless."
                ),
            },
            {
                "id": "b",
                "text": "WEP does not encrypt traffic at all; it only hides the SSID",
                "correct": False,
                "rationale": (
                    "Incorrect. WEP does apply RC4-based encryption to the data payload. "
                    "The problem is not that encryption is absent, but that the encryption "
                    "implementation is so weak it provides no practical security."
                ),
            },
            {
                "id": "c",
                "text": "WEP requires a RADIUS server and is incompatible with SOHO routers",
                "correct": False,
                "rationale": (
                    "Incorrect. WEP is a pre-shared key protocol and does not require RADIUS. "
                    "RADIUS is an enterprise authentication component used with 802.1X."
                ),
            },
            {
                "id": "d",
                "text": "WEP only supports 2.4 GHz and must be upgraded for 5 GHz Wi-Fi support",
                "correct": False,
                "rationale": (
                    "Incorrect. WEP's weakness is cryptographic, not frequency-based. "
                    "Band selection is independent of the encryption protocol in use."
                ),
            },
        ],
        "explanation": (
            "WEP (Wired Equivalent Privacy) is definitively broken due to IV reuse "
            "vulnerabilities in its RC4 implementation. The 24-bit IV space is reused "
            "frequently enough on active networks that statistical analysis recovers the "
            "key rapidly. Replace with WPA2 (AES-CCMP) or WPA3 immediately."
        ),
    },
    {
        "id": "c2d2v3-008",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Wireless security protocols",
        "stem": (
            "A network administrator configures a new access point and selects WPA2-Personal "
            "with a passphrase. A security consultant recommends enabling 802.11w (Management "
            "Frame Protection). Which specific attack does 802.11w primarily defend against?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Deauthentication (deauth) flood attacks that forcibly disconnect clients",
                "correct": True,
                "rationale": (
                    "Correct. 802.11w (Protected Management Frames, PMF) cryptographically "
                    "protects management frames — including deauthentication and disassociation "
                    "frames — preventing attackers from injecting spoofed deauth packets to "
                    "disconnect clients and capture the re-association handshake."
                ),
            },
            {
                "id": "b",
                "text": "Offline dictionary attacks against the captured WPA2 four-way handshake",
                "correct": False,
                "rationale": (
                    "Incorrect. Dictionary attacks against the PSK handshake are mitigated by "
                    "strong passphrase choice and WPA3-SAE, not by 802.11w. PMF protects "
                    "management frame integrity, not the PSK key exchange itself."
                ),
            },
            {
                "id": "c",
                "text": "Rogue DHCP servers assigning incorrect gateway addresses to clients",
                "correct": False,
                "rationale": (
                    "Incorrect. Rogue DHCP attacks are mitigated by DHCP snooping on the "
                    "switch, not by 802.11w. PMF operates at the wireless management frame "
                    "layer."
                ),
            },
            {
                "id": "d",
                "text": "Evil twin access points stealing credentials via a captive portal",
                "correct": False,
                "rationale": (
                    "Incorrect. Evil twin attacks use a rogue AP with the same SSID. While "
                    "802.11w can make certain management frame spoofing harder, evil twin "
                    "prevention relies primarily on network monitoring and 802.1X with "
                    "certificate validation, not PMF."
                ),
            },
        ],
        "explanation": (
            "IEEE 802.11w (PMF) adds cryptographic integrity to management frames. The "
            "primary threat it counters is deauthentication floods, where an attacker "
            "sends spoofed deauth frames to disconnect clients. Without PMF, any radio "
            "device can forge these frames since they were previously unauthenticated."
        ),
    },
    {
        "id": "c2d2v3-009",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Wireless security protocols",
        "stem": (
            "A small business has a single SSID that both employees and walk-in customers "
            "use. The owner wants to isolate customer devices from the internal file server "
            "while keeping one AP. Which SOHO wireless feature accomplishes this isolation?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Guest network / SSID isolation on the access point",
                "correct": True,
                "rationale": (
                    "Correct. A guest network creates a second SSID mapped to an isolated "
                    "network segment (often a separate VLAN). Client isolation prevents "
                    "guest devices from communicating with internal LAN resources or other "
                    "wireless clients on the guest SSID."
                ),
            },
            {
                "id": "b",
                "text": "Disabling SSID broadcast for the employee network",
                "correct": False,
                "rationale": (
                    "Incorrect. Hiding the SSID makes it less visible but does not create "
                    "network isolation. Determined users can still find and join a hidden "
                    "SSID, and it does not prevent customers from accessing the file server "
                    "if they are on the same network segment."
                ),
            },
            {
                "id": "c",
                "text": "Enabling MAC address filtering to block unknown devices",
                "correct": False,
                "rationale": (
                    "Incorrect. MAC filtering is easily bypassed by MAC spoofing and requires "
                    "ongoing administration for all customer devices. It does not provide "
                    "network-level isolation between customers and internal resources."
                ),
            },
            {
                "id": "d",
                "text": "Configuring a longer DHCP lease time for internal devices",
                "correct": False,
                "rationale": (
                    "Incorrect. DHCP lease duration affects IP address retention time only. "
                    "It provides no network segmentation or isolation between device classes."
                ),
            },
        ],
        "explanation": (
            "A guest SSID with client isolation creates a logically separate network: "
            "guest devices receive internet access but are blocked from reaching the "
            "internal LAN (including file servers). This is a standard SOHO AP feature. "
            "MAC filtering and hidden SSIDs are weak controls that do not achieve isolation."
        ),
    },
    # ── 2.4 Malware ──────────────────────────────────────────────────────────
    {
        "id": "c2d2v3-010",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Malware types & removal",
        "stem": (
            "A user's desktop wallpaper has been replaced with a message demanding payment "
            "in cryptocurrency to recover files. Attempting to open any .docx or .xlsx file "
            "results in an error stating the file is corrupted. Which malware type is "
            "responsible, and which characteristic distinguishes it from other malware?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Ransomware — it encrypts user files and extorts payment for the decryption key",
                "correct": True,
                "rationale": (
                    "Correct. Ransomware encrypts victim files and demands payment (often "
                    "cryptocurrency) in exchange for the decryption key. The encrypted files "
                    "appearing 'corrupted' and the ransom wallpaper are canonical ransomware "
                    "indicators."
                ),
            },
            {
                "id": "b",
                "text": "Spyware — it monitors user behavior and displays payment demands",
                "correct": False,
                "rationale": (
                    "Incorrect. Spyware silently collects user data (keystrokes, browsing) "
                    "and exfiltrates it. It does not encrypt files or demand ransom payments."
                ),
            },
            {
                "id": "c",
                "text": "Trojan — it disguises as a legitimate program and corrupts files when activated",
                "correct": False,
                "rationale": (
                    "Incorrect. A Trojan is defined by its delivery method (masquerading as "
                    "legitimate software), not its payload type. The payload here — file "
                    "encryption with a ransom demand — specifically classifies the infection "
                    "as ransomware regardless of how it was delivered."
                ),
            },
            {
                "id": "d",
                "text": "Boot sector virus — it infects the MBR and prevents OS access until payment",
                "correct": False,
                "rationale": (
                    "Incorrect. A boot sector virus infects the MBR/VBR and may prevent "
                    "booting, but the described scenario shows the OS running normally with "
                    "specific user files encrypted — the hallmark of ransomware, not a "
                    "boot virus."
                ),
            },
        ],
        "explanation": (
            "Ransomware is uniquely identified by: (1) encryption of user data, making files "
            "inaccessible; (2) a ransom demand with payment instructions; (3) a promise of "
            "a decryption key upon payment. Prevention relies on offline backups; recovery "
            "without paying requires viable backup restoration."
        ),
    },
    {
        "id": "c2d2v3-011",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Malware types & removal",
        "stem": (
            "A technician is following the CompTIA best-practice malware removal process. "
            "The malware has been identified and the machine quarantined. System Restore has "
            "been disabled. After running updated malware removal tools, the infection is "
            "gone. Which step should the technician perform NEXT?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Schedule future scans and update antivirus definitions",
                "correct": True,
                "rationale": (
                    "Correct. The CompTIA 7-step order after successful remediation (step 4) "
                    "is: step 5 — schedule scans and update AV definitions, then step 6 — "
                    "re-enable System Restore and create a new restore point, then step 7 — "
                    "educate the end user. Scheduling scans/updating definitions comes "
                    "immediately after remediation."
                ),
            },
            {
                "id": "b",
                "text": "Educate the end user about safe computing practices",
                "correct": False,
                "rationale": (
                    "Incorrect. End-user education is the final step (step 7), performed "
                    "after scans are scheduled/definitions updated and System Restore is "
                    "re-enabled."
                ),
            },
            {
                "id": "c",
                "text": "Re-enable System Restore and create a clean restore point",
                "correct": False,
                "rationale": (
                    "Incorrect. Re-enabling System Restore is step 6, which comes after "
                    "scheduling scans and updating definitions (step 5). Doing it immediately "
                    "after remediation skips a step."
                ),
            },
            {
                "id": "d",
                "text": "Restore all encrypted files from a backup",
                "correct": False,
                "rationale": (
                    "Incorrect. File restoration from backup may be needed for ransomware "
                    "scenarios, but it is not listed as the next step in the CompTIA "
                    "7-step malware removal process after remediation."
                ),
            },
        ],
        "explanation": (
            "CompTIA 7-step malware removal: (1) Identify/investigate, (2) Quarantine, "
            "(3) Disable System Restore, (4) Remediate, (5) Schedule scans/update defs, "
            "(6) Re-enable System Restore/create restore point, (7) Educate end user. "
            "After step 4, step 5 is next."
        ),
    },
    {
        "id": "c2d2v3-012",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Malware types & removal",
        "stem": (
            "After a successful malware removal, the technician re-enables System Restore "
            "and creates a new restore point. The user then reports the malware symptoms "
            "have returned. Which is the MOST likely explanation?"
        ),
        "options": [
            {
                "id": "a",
                "text": "An older infected restore point was used and re-infected the system",
                "correct": True,
                "rationale": (
                    "Correct. If System Restore was not properly purged of infected "
                    "snapshots before re-enabling, Windows could have automatically restored "
                    "a prior state containing malware — or the user manually rolled back. "
                    "This is exactly why disabling System Restore before remediation is "
                    "step 3 of the CompTIA process."
                ),
            },
            {
                "id": "b",
                "text": "The antivirus definitions were not updated before scanning",
                "correct": False,
                "rationale": (
                    "Incorrect. If definitions were not updated, the initial scan might miss "
                    "the malware — but the question states remediation was successful. The "
                    "return of symptoms after a successful clean points to re-infection from "
                    "a restore point, not a missed initial detection."
                ),
            },
            {
                "id": "c",
                "text": "The quarantine step was omitted, allowing network re-infection",
                "correct": False,
                "rationale": (
                    "Incorrect. Network re-infection is possible if quarantine was skipped, "
                    "but the scenario states all steps were followed including quarantine. "
                    "The most specific explanation for return after re-enabling System "
                    "Restore is a contaminated restore point."
                ),
            },
            {
                "id": "d",
                "text": "The malware evolved and re-infected through a zero-day exploit",
                "correct": False,
                "rationale": (
                    "Incorrect. While possible in theory, zero-day re-infection occurring "
                    "immediately after a restore point creation is not the most likely "
                    "explanation. The timing with System Restore re-enablement strongly "
                    "points to a restore-point re-infection."
                ),
            },
        ],
        "explanation": (
            "Malware can hide in System Restore snapshots. The CompTIA process instructs "
            "turning off System Restore (which purges all restore points) BEFORE "
            "remediation specifically to prevent this re-infection vector. If the "
            "infected snapshot persists and is applied after cleanup, the malware returns."
        ),
    },
    {
        "id": "c2d2v3-013",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Malware types & removal",
        "stem": (
            "A worm is detected propagating across a corporate network through an "
            "unpatched SMB vulnerability. The worm does not require any user interaction "
            "to spread. Which characteristic BEST distinguishes a worm from a virus?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A worm self-replicates across networks without attaching to a host file or requiring user interaction",
                "correct": True,
                "rationale": (
                    "Correct. The defining characteristic of a worm is autonomous network "
                    "self-propagation — it finds and exploits vulnerabilities to copy itself "
                    "to new hosts without needing to attach to an existing file or be "
                    "executed by a user."
                ),
            },
            {
                "id": "b",
                "text": "A worm always encrypts files on the victim system; a virus does not",
                "correct": False,
                "rationale": (
                    "Incorrect. File encryption is a ransomware payload characteristic, not "
                    "a defining feature of worms. A worm is defined by its propagation "
                    "mechanism, not its payload."
                ),
            },
            {
                "id": "c",
                "text": "A worm requires the user to execute an infected file to spread",
                "correct": False,
                "rationale": (
                    "Incorrect. This describes a virus, not a worm. The scenario explicitly "
                    "states no user interaction is required — the hallmark of worm propagation."
                ),
            },
            {
                "id": "d",
                "text": "A worm replaces system binaries with malicious versions to gain kernel access",
                "correct": False,
                "rationale": (
                    "Incorrect. Replacing system binaries for persistent kernel access "
                    "describes rootkit behavior, not the defining characteristic of a worm."
                ),
            },
        ],
        "explanation": (
            "Worm vs. virus: a virus requires a host file and user execution to spread; "
            "a worm independently exploits network vulnerabilities to replicate. "
            "The WannaCry and NotPetya examples are famous network-propagating worms "
            "that used the EternalBlue SMB exploit — no user action required."
        ),
    },
    # ── 2.5 Social Engineering ───────────────────────────────────────────────
    {
        "id": "c2d2v3-014",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Social engineering & attacks",
        "stem": (
            "A threat actor calls an employee posing as a vendor tech support engineer. "
            "Using information gathered from the company's LinkedIn page, the attacker "
            "convinces the employee to install a remote-access tool 'to fix a critical "
            "server issue.' Which social engineering technique is the attacker using?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Vishing combined with pretexting",
                "correct": True,
                "rationale": (
                    "Correct. Vishing (voice phishing) is the phone-based attack vector. "
                    "Pretexting is the fabricated scenario (vendor tech support needing "
                    "remote access) used to manipulate the target. Using LinkedIn data is "
                    "open-source intelligence (OSINT) that makes the pretext credible."
                ),
            },
            {
                "id": "b",
                "text": "Spear phishing",
                "correct": False,
                "rationale": (
                    "Incorrect. Spear phishing uses targeted email, not a phone call. "
                    "The attack vector here is voice — qualifying it as vishing, not "
                    "spear phishing."
                ),
            },
            {
                "id": "c",
                "text": "Tailgating",
                "correct": False,
                "rationale": (
                    "Incorrect. Tailgating is a physical access attack — following someone "
                    "through a door. No physical access is involved in this scenario."
                ),
            },
            {
                "id": "d",
                "text": "Shoulder surfing",
                "correct": False,
                "rationale": (
                    "Incorrect. Shoulder surfing involves visually observing a target's "
                    "screen or keyboard. This attack is conducted over the phone, not "
                    "through physical observation."
                ),
            },
        ],
        "explanation": (
            "Pretexting is the creation of a fabricated scenario to manipulate someone "
            "into taking action. Combined with vishing (phone-based delivery), it is a "
            "powerful social engineering method. OSINT from LinkedIn adds authenticity. "
            "The result is the user installing malware believing they are helping IT."
        ),
    },
    {
        "id": "c2d2v3-015",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Social engineering & attacks",
        "stem": (
            "An attacker sends an email to a specific software developer at a defense "
            "contractor, referencing her current project by name and her manager's name. "
            "The email contains a malicious PDF attachment disguised as a project update. "
            "This attack is BEST classified as:"
        ),
        "options": [
            {
                "id": "a",
                "text": "Spear phishing",
                "correct": True,
                "rationale": (
                    "Correct. Spear phishing is highly targeted email phishing directed at "
                    "a specific individual or organization, using personalized details to "
                    "increase credibility. It differs from generic phishing (mass, "
                    "untargeted) and whaling (C-suite executives)."
                ),
            },
            {
                "id": "b",
                "text": "Whaling",
                "correct": False,
                "rationale": (
                    "Incorrect. Whaling targets senior executives (C-suite/high-value). "
                    "This target is a developer — not described as an executive — so spear "
                    "phishing is the more precise classification."
                ),
            },
            {
                "id": "c",
                "text": "Generic phishing",
                "correct": False,
                "rationale": (
                    "Incorrect. Generic phishing is mass and untargeted. The use of the "
                    "developer's project name and manager's name demonstrates targeted "
                    "reconnaissance, elevating this to spear phishing."
                ),
            },
            {
                "id": "d",
                "text": "Smishing",
                "correct": False,
                "rationale": (
                    "Incorrect. Smishing is phishing delivered via SMS text message. "
                    "The attack vector here is email."
                ),
            },
        ],
        "explanation": (
            "Phishing taxonomy: Generic phishing = mass email. Spear phishing = targeted "
            "email at a specific individual. Whaling = spear phishing targeting executives. "
            "Vishing = voice. Smishing = SMS. The scenario's personalization without "
            "executive targeting = spear phishing."
        ),
    },
    {
        "id": "c2d2v3-016",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Social engineering & attacks",
        "stem": (
            "A company's receptionist receives a call from someone claiming to be the "
            "head of IT, demanding the visitor Wi-Fi password immediately because 'an "
            "important client meeting starts in two minutes.' The receptionist feels "
            "pressured to comply. Which social engineering principle is the attacker "
            "exploiting?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Urgency and authority",
                "correct": True,
                "rationale": (
                    "Correct. The attacker creates urgency ('two minutes') to prevent "
                    "the target from thinking critically, and invokes authority ('head of "
                    "IT') to make refusal feel inappropriate. These are two of the core "
                    "social engineering psychological manipulation techniques."
                ),
            },
            {
                "id": "b",
                "text": "Scarcity",
                "correct": False,
                "rationale": (
                    "Incorrect. Scarcity implies a limited supply creating demand "
                    "(e.g., 'only one slot left'). The scenario uses time pressure and "
                    "authority, not resource scarcity."
                ),
            },
            {
                "id": "c",
                "text": "Consensus/social proof",
                "correct": False,
                "rationale": (
                    "Incorrect. Social proof means 'everyone else is doing it.' The "
                    "attacker here uses authority and time pressure, not peer behavior "
                    "as justification."
                ),
            },
            {
                "id": "d",
                "text": "Reciprocity",
                "correct": False,
                "rationale": (
                    "Incorrect. Reciprocity involves doing something for the target first "
                    "to create an obligation to return the favor. The scenario involves "
                    "no prior favor — only authority and time pressure."
                ),
            },
        ],
        "explanation": (
            "Social engineering principles include urgency, authority, scarcity, social "
            "proof, reciprocity, liking, and familiarity. Urgency bypasses critical "
            "thinking; authority exploits deference. Combining them is highly effective "
            "and is a common pattern in telephone-based social engineering."
        ),
    },
    {
        "id": "c2d2v3-017",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Social engineering & attacks",
        "stem": (
            "An employee receives an SMS text message that appears to be from her bank, "
            "asking her to click a link to verify a suspicious transaction. The link "
            "leads to a fake login page. Which attack type is this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Smishing",
                "correct": True,
                "rationale": (
                    "Correct. Smishing (SMS phishing) is phishing conducted via SMS text "
                    "messages. The attacker impersonates a trusted institution and includes "
                    "a malicious link to harvest credentials — delivered by text, not email."
                ),
            },
            {
                "id": "b",
                "text": "Vishing",
                "correct": False,
                "rationale": (
                    "Incorrect. Vishing uses voice calls. This attack uses SMS text "
                    "messages — that is smishing."
                ),
            },
            {
                "id": "c",
                "text": "Spear phishing",
                "correct": False,
                "rationale": (
                    "Incorrect. Spear phishing is targeted email-based phishing. While "
                    "this message may be targeted, the delivery channel is SMS, "
                    "making it smishing specifically."
                ),
            },
            {
                "id": "d",
                "text": "Pharming",
                "correct": False,
                "rationale": (
                    "Incorrect. Pharming redirects users from legitimate URLs to malicious "
                    "sites by poisoning DNS or host files — without any user clicking a "
                    "fraudulent link. The user here is tricked via a link in a text message."
                ),
            },
        ],
        "explanation": (
            "Attack vector taxonomy: Email = phishing/spear phishing/whaling. "
            "Voice = vishing. SMS = smishing. The bank impersonation via text message "
            "with a credential-harvesting link is the canonical smishing example."
        ),
    },
    {
        "id": "c2d2v3-018",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Social engineering & attacks",
        "stem": (
            "An attacker floods a company's web server with traffic from thousands of "
            "compromised hosts simultaneously, making the website unavailable to "
            "legitimate users. Which attack type is described?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Distributed Denial of Service (DDoS)",
                "correct": True,
                "rationale": (
                    "Correct. A DDoS attack uses multiple distributed sources (a botnet of "
                    "compromised hosts) to flood a target with traffic, exhausting its "
                    "resources and denying service to legitimate users."
                ),
            },
            {
                "id": "b",
                "text": "On-path (man-in-the-middle) attack",
                "correct": False,
                "rationale": (
                    "Incorrect. An on-path attack intercepts and potentially alters "
                    "communications between two parties. It does not involve flooding a "
                    "server with traffic to deny service."
                ),
            },
            {
                "id": "c",
                "text": "SQL injection",
                "correct": False,
                "rationale": (
                    "Incorrect. SQL injection manipulates database queries by injecting "
                    "malicious input. It does not involve multiple compromised hosts "
                    "flooding a server with traffic."
                ),
            },
            {
                "id": "d",
                "text": "Zero-day exploit",
                "correct": False,
                "rationale": (
                    "Incorrect. A zero-day exploit targets an unpatched vulnerability. "
                    "The scenario describes traffic volume overwhelming a server — "
                    "the mechanism of a DDoS attack."
                ),
            },
        ],
        "explanation": (
            "DDoS uses a distributed botnet to generate traffic volume that overwhelms "
            "the target. Single-source DoS is from one host; DDoS uses many. Defenses "
            "include CDN scrubbing, rate limiting, anycast routing, and ISP-level "
            "upstream filtering."
        ),
    },
    {
        "id": "c2d2v3-019",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Social engineering & attacks",
        "stem": (
            "A penetration tester leaves several USB drives labeled 'Q3 Salary Data' in "
            "the company parking lot. Within an hour, three employees have plugged the "
            "drives into their workstations. Which attack technique is the tester "
            "demonstrating?"
        ),
        "options": [
            {
                "id": "a",
                "text": "USB baiting (removable media drop attack)",
                "correct": True,
                "rationale": (
                    "Correct. A USB drop (baiting) attack relies on human curiosity — "
                    "employees plug in found drives, executing any malware pre-loaded "
                    "on the device. The enticing label ('Salary Data') is the lure "
                    "that exploits curiosity and self-interest."
                ),
            },
            {
                "id": "b",
                "text": "Dumpster diving",
                "correct": False,
                "rationale": (
                    "Incorrect. Dumpster diving involves searching through discarded "
                    "materials. The tester here is planting devices, not searching trash."
                ),
            },
            {
                "id": "c",
                "text": "Shoulder surfing",
                "correct": False,
                "rationale": (
                    "Incorrect. Shoulder surfing involves watching someone's screen or "
                    "keyboard. No observation of active sessions is involved here."
                ),
            },
            {
                "id": "d",
                "text": "Tailgating",
                "correct": False,
                "rationale": (
                    "Incorrect. Tailgating is following someone through a secured door. "
                    "The attack here exploits curiosity with planted removable media, "
                    "not physical access to a building."
                ),
            },
        ],
        "explanation": (
            "USB drop/baiting exploits human curiosity. Attackers pre-load drives with "
            "auto-run malware or malicious files and leave them in high-traffic areas. "
            "Enticing labels increase pickup rates. Mitigation: disable AutoRun, enforce "
            "USB port policies via GPO, and train employees not to plug in found media."
        ),
    },
    # ── 2.6 Windows OS Security Settings ─────────────────────────────────────
    {
        "id": "c2d2v3-020",
        "domain": 2,
        "objective": "2.6",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "NTFS vs share permissions",
        "stem": (
            "User TBrown is a member of two groups: 'Accounting' (NTFS: Modify on folder F) "
            "and 'Auditors' (NTFS: Read on folder F). There is also an explicit Deny Write "
            "permission assigned directly to TBrown's user account on folder F. The share "
            "permission grants 'Everyone' Full Control. TBrown accesses folder F over the "
            "network. What is TBrown's effective permission?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Read only — the explicit Deny Write removes Write from the Modify grant, leaving Read and Execute",
                "correct": True,
                "rationale": (
                    "Correct. Step 1: Combined NTFS permissions from groups: Modify (includes "
                    "Read, Write, Execute) + Read = Modify. Step 2: Explicit Deny Write on "
                    "TBrown's account overrides all Allow grants for Write. Modify minus "
                    "Write = Read & Execute (effectively Read for a user). Step 3: Share is "
                    "Full Control, so the NTFS result (Read+Execute) is the effective network "
                    "permission."
                ),
            },
            {
                "id": "b",
                "text": "Modify — explicit Deny only applies to local access, not network access",
                "correct": False,
                "rationale": (
                    "Incorrect. NTFS Deny permissions apply regardless of access method "
                    "(local or network). Deny Write removes write capability in all contexts."
                ),
            },
            {
                "id": "c",
                "text": "No Access — any Deny on an account blocks all access to the folder",
                "correct": False,
                "rationale": (
                    "Incorrect. A Deny Write does not deny all access; it specifically "
                    "removes the Write permission. The user still retains Read and Execute "
                    "from the remaining Allow grants."
                ),
            },
            {
                "id": "d",
                "text": "Full Control — the share permission Full Control supersedes NTFS Deny",
                "correct": False,
                "rationale": (
                    "Incorrect. Share permissions never override NTFS permissions. The "
                    "more restrictive of the two applies, and NTFS Deny permissions "
                    "always take precedence over Allow regardless of share settings."
                ),
            },
        ],
        "explanation": (
            "Key rules: (1) NTFS Allow permissions accumulate across groups. (2) Explicit "
            "Deny always overrides Allow for the specific denied permission. (3) Deny Write "
            "removes only the Write bit from Modify, leaving Read+Execute. (4) Share "
            "Full Control is less restrictive than NTFS Read+Execute, so network effective "
            "= Read+Execute."
        ),
    },
]

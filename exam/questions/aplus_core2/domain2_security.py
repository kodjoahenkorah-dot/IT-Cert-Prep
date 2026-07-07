"""
CompTIA A+ Core 2 (220-1202) — Domain 2: Security
44 exam-quality questions covering objectives 2.1 through 2.10.
"""

QUESTIONS = [
    # ── 2.1 Physical Security ────────────────────────────────────────────────
    {
        "id": "c2d2-001",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Physical security",
        "stem": (
            "A corporate building recently experienced an incident where an unauthorized "
            "person followed an employee through a secured door immediately after badge "
            "swipe. Which physical security control is specifically designed to prevent "
            "this type of attack?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Access control vestibule (mantrap)",
                "correct": True,
                "rationale": (
                    "Correct. An access control vestibule (mantrap) requires one door to "
                    "close and verify before the next door opens, preventing tailgating by "
                    "allowing only one person through at a time."
                ),
            },
            {
                "id": "b",
                "text": "Magnetometer at the entrance",
                "correct": False,
                "rationale": (
                    "Incorrect. A magnetometer detects metal objects (weapons) but does not "
                    "prevent tailgating because it does not control entry of multiple people "
                    "on a single credential."
                ),
            },
            {
                "id": "c",
                "text": "Video surveillance cameras",
                "correct": False,
                "rationale": (
                    "Incorrect. Video surveillance records and may deter tailgating after the "
                    "fact but does not actively prevent a second person from slipping through "
                    "behind a badge holder."
                ),
            },
            {
                "id": "d",
                "text": "Motion sensor alarm",
                "correct": False,
                "rationale": (
                    "Incorrect. Motion sensors detect movement in an area but do not stop a "
                    "tailgating event from occurring at a door — they trigger an alarm after "
                    "movement is detected, not before."
                ),
            },
        ],
        "explanation": (
            "Tailgating (piggybacking) is defeated by an access control vestibule (mantrap): "
            "a small buffer zone with two interlocking doors. The first door must be secured "
            "before the second opens, ensuring only one validated individual passes through "
            "at a time. Camera systems and alarms are detective, not preventive, controls "
            "for this specific threat."
        ),
    },
    {
        "id": "c2d2-002",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Physical security",
        "stem": (
            "A data center manager needs to prevent vehicles from ramming into the building's "
            "exterior walls to protect equipment inside. Which physical security measure is "
            "the BEST choice for this specific threat?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Bollards installed around the perimeter",
                "correct": True,
                "rationale": (
                    "Correct. Bollards are short, sturdy vertical posts designed to stop or "
                    "redirect vehicles. They are the industry-standard control for vehicle "
                    "ramming threats against buildings."
                ),
            },
            {
                "id": "b",
                "text": "Chain-link perimeter fence",
                "correct": False,
                "rationale": (
                    "Incorrect. A standard chain-link fence deters casual intruders on foot "
                    "but provides little resistance to a vehicle ramming attack."
                ),
            },
            {
                "id": "c",
                "text": "Security guard at the entrance",
                "correct": False,
                "rationale": (
                    "Incorrect. A guard can verify identity and monitor activity but cannot "
                    "physically stop a vehicle traveling at speed toward the building."
                ),
            },
            {
                "id": "d",
                "text": "Alarm system triggered by impact sensors",
                "correct": False,
                "rationale": (
                    "Incorrect. An impact alarm would trigger after a vehicle hits the building, "
                    "providing no preventive protection against the physical damage caused by "
                    "ramming."
                ),
            },
        ],
        "explanation": (
            "Bollards are crash-rated posts embedded in the ground around building perimeters. "
            "They are the correct answer whenever the threat is vehicle-based physical attack. "
            "Fences deter foot traffic; guards and alarms are not capable of stopping a "
            "moving vehicle before impact."
        ),
    },
    {
        "id": "c2d2-003",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Physical security",
        "stem": (
            "An employee's laptop was stolen from a shared conference room while she stepped "
            "out briefly. Which physical security control, if implemented, would have been "
            "MOST effective at preventing the theft of the device itself?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Cable lock anchoring the laptop to the conference table",
                "correct": True,
                "rationale": (
                    "Correct. An equipment cable lock (Kensington-style) physically tethers "
                    "the device to an immovable object, directly preventing opportunistic "
                    "theft of the hardware."
                ),
            },
            {
                "id": "b",
                "text": "BitLocker full-disk encryption enabled on the laptop",
                "correct": False,
                "rationale": (
                    "Incorrect. BitLocker protects data confidentiality if the device is "
                    "stolen but does nothing to prevent the theft of the hardware itself."
                ),
            },
            {
                "id": "c",
                "text": "Badge reader on the conference room door",
                "correct": False,
                "rationale": (
                    "Incorrect. A badge reader controls access to the room but the theft "
                    "occurred by someone who may have already been authorized in the building; "
                    "it would not stop someone already inside from taking the device."
                ),
            },
            {
                "id": "d",
                "text": "Video surveillance covering the conference room",
                "correct": False,
                "rationale": (
                    "Incorrect. Camera footage can help identify the thief after the fact but "
                    "is a detective control, not a preventive one, and would not stop the "
                    "theft from occurring."
                ),
            },
        ],
        "explanation": (
            "Equipment locks (cable locks) are the direct preventive control for device "
            "theft. BitLocker addresses data confidentiality post-theft. Badge readers and "
            "cameras provide access control and investigation capability but do not physically "
            "restrain the hardware."
        ),
    },
    # ── 2.2 Logical Security ─────────────────────────────────────────────────
    {
        "id": "c2d2-004",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Logical security & Active Directory",
        "stem": (
            "A new accountant needs to run a payroll application, access the payroll network "
            "share, and read HR reports. She does not need administrative rights to any "
            "system. The IT admin places her account only in the Payroll security group and "
            "the HR-Reports security group, and assigns those groups the specific permissions "
            "they require. Which security principle does this BEST illustrate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Principle of least privilege",
                "correct": True,
                "rationale": (
                    "Correct. Least privilege means users are granted the minimum permissions "
                    "necessary to perform their job functions and no more. Assigning only "
                    "the required group memberships implements this principle directly."
                ),
            },
            {
                "id": "b",
                "text": "Separation of duties",
                "correct": False,
                "rationale": (
                    "Incorrect. Separation of duties divides a task among multiple people "
                    "so no single person can complete a critical process alone (e.g., one "
                    "person enters payments, another approves). That concept is not illustrated "
                    "here."
                ),
            },
            {
                "id": "c",
                "text": "Defense in depth",
                "correct": False,
                "rationale": (
                    "Incorrect. Defense in depth refers to layering multiple security "
                    "controls so that failure of one does not compromise the whole — not "
                    "the specific assignment of minimal permissions."
                ),
            },
            {
                "id": "d",
                "text": "Role-based access control (RBAC) only",
                "correct": False,
                "rationale": (
                    "Incorrect. Placing users into groups is an implementation of RBAC, but "
                    "the underlying principle that drives limiting the groups to only what is "
                    "needed is least privilege. RBAC is a mechanism; least privilege is the "
                    "overarching principle the question asks for."
                ),
            },
        ],
        "explanation": (
            "The principle of least privilege dictates that an entity should have only the "
            "access rights required for its legitimate purpose. RBAC via security groups is "
            "a common implementation mechanism, but the governing security principle is "
            "least privilege."
        ),
    },
    {
        "id": "c2d2-005",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Logical security & Active Directory",
        "stem": (
            "An administrator wants all domain-joined Windows laptops to automatically map "
            "a specific network drive, install approved software at startup, and enforce a "
            "screensaver lock timeout — without touching each machine individually. Which "
            "Active Directory feature should the administrator use?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Group Policy Objects (GPOs) linked to an Organizational Unit",
                "correct": True,
                "rationale": (
                    "Correct. GPOs linked to an OU allow administrators to push settings, "
                    "scripts, and software configurations to all computers and users in that "
                    "OU automatically at logon/startup, covering all three requirements."
                ),
            },
            {
                "id": "b",
                "text": "Folder redirection configured in the user's home folder setting",
                "correct": False,
                "rationale": (
                    "Incorrect. Folder redirection moves special folders (Desktop, Documents) "
                    "to a network location. It does not install software or enforce screensaver "
                    "policies."
                ),
            },
            {
                "id": "c",
                "text": "Login script assigned in user account properties",
                "correct": False,
                "rationale": (
                    "Incorrect. A login script can map drives and run commands at logon, but "
                    "it cannot enforce machine-level policies like screensaver timeouts, and "
                    "managing individual user scripts does not scale as well as GPOs."
                ),
            },
            {
                "id": "d",
                "text": "Security group membership with ACL modifications",
                "correct": False,
                "rationale": (
                    "Incorrect. Security groups with ACLs control resource access permissions "
                    "but do not push settings, install software, or configure system behavior "
                    "on domain machines."
                ),
            },
        ],
        "explanation": (
            "Group Policy Objects (GPOs) are the correct AD mechanism for centrally managing "
            "computer and user configurations across an OU. They handle software deployment, "
            "drive mapping (via GPO preferences), and policy enforcement (screensaver, "
            "password, etc.) without per-machine manual configuration."
        ),
    },
    {
        "id": "c2d2-006",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Logical security & Active Directory",
        "stem": (
            "A company requires that remote VPN access use something the user knows AND "
            "a time-based one-time password generated by an app on their smartphone, but "
            "NOT SMS codes because the security team considers SIM-swapping a risk. "
            "Which authentication combination satisfies this requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Password + TOTP authenticator app (soft token)",
                "correct": True,
                "rationale": (
                    "Correct. A password (something you know) combined with a TOTP "
                    "authenticator app (a soft token — something you have on the device) "
                    "satisfies MFA without using SMS, eliminating the SIM-swap risk."
                ),
            },
            {
                "id": "b",
                "text": "Password + SMS one-time code",
                "correct": False,
                "rationale": (
                    "Incorrect. SMS OTP is explicitly excluded by the security team due to "
                    "SIM-swapping vulnerability, where an attacker ports the victim's phone "
                    "number to intercept the code."
                ),
            },
            {
                "id": "c",
                "text": "Username + password only",
                "correct": False,
                "rationale": (
                    "Incorrect. Username and password alone is single-factor authentication "
                    "(something you know). The requirement is for a second factor."
                ),
            },
            {
                "id": "d",
                "text": "Password + hard token key fob (HOTP)",
                "correct": False,
                "rationale": (
                    "Incorrect. A hard token HOTP key fob does satisfy MFA and avoids SMS, "
                    "but the question specifies the second factor is generated by an app on "
                    "their smartphone, which describes a soft token / TOTP authenticator app, "
                    "not a physical hardware fob."
                ),
            },
        ],
        "explanation": (
            "MFA requires at least two factor categories. A password is 'something you know'; "
            "a TOTP authenticator app is a soft token representing 'something you have'. "
            "SMS OTP is also 'something you have' but is vulnerable to SIM swapping. "
            "Hard tokens are physical devices and would not be described as an app on a phone."
        ),
    },
    # ── 2.3 Wireless Security ────────────────────────────────────────────────
    {
        "id": "c2d2-007",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Wireless security protocols",
        "stem": (
            "A security audit finds that several legacy wireless access points still use "
            "TKIP for encryption. Which is the PRIMARY reason TKIP is considered insecure "
            "compared to AES-CCMP used in WPA2/WPA3?"
        ),
        "options": [
            {
                "id": "a",
                "text": "TKIP uses RC4 with per-packet keys that have known cryptographic weaknesses, while AES-CCMP uses a stronger block cipher with integrity checking",
                "correct": True,
                "rationale": (
                    "Correct. TKIP was designed as a stopgap fix over WEP's broken RC4. "
                    "Although it adds per-packet keying and MIC, the underlying RC4 cipher "
                    "has known weaknesses. AES-CCMP uses the AES block cipher in CCM mode "
                    "providing confidentiality and data integrity far superior to TKIP."
                ),
            },
            {
                "id": "b",
                "text": "TKIP operates only on the 5 GHz band, limiting coverage compared to AES",
                "correct": False,
                "rationale": (
                    "Incorrect. TKIP/WPA operation is not band-specific; both 2.4 GHz and "
                    "5 GHz radios can run TKIP. Band selection is independent of encryption "
                    "protocol."
                ),
            },
            {
                "id": "c",
                "text": "TKIP does not support pre-shared keys, making enterprise deployment difficult",
                "correct": False,
                "rationale": (
                    "Incorrect. TKIP (WPA-Personal) does support PSK-based authentication. "
                    "The security flaw is cryptographic weakness, not an absence of PSK support."
                ),
            },
            {
                "id": "d",
                "text": "TKIP requires a RADIUS server while AES-CCMP can operate without one",
                "correct": False,
                "rationale": (
                    "Incorrect. TKIP in WPA-Personal mode does NOT require RADIUS; RADIUS is "
                    "an enterprise authentication component independent of the encryption "
                    "algorithm choice."
                ),
            },
        ],
        "explanation": (
            "TKIP wraps RC4 with per-packet keying and a Message Integrity Code (Michael) to "
            "patch WEP, but RC4 has well-documented cryptographic flaws. AES-CCMP uses the "
            "AES block cipher in Counter Mode with CBC-MAC (CCM), providing both "
            "confidentiality and cryptographic integrity far stronger than anything TKIP "
            "offers. WPA2 mandates AES-CCMP; WPA3 additionally requires SAE."
        ),
    },
    {
        "id": "c2d2-008",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Wireless security protocols",
        "stem": (
            "A university IT team is deploying enterprise Wi-Fi so that each student "
            "authenticates with their individual domain credentials rather than a shared "
            "passphrase. Wireless clients send credentials to a central authentication "
            "server. Which protocol combination correctly describes this architecture?"
        ),
        "options": [
            {
                "id": "a",
                "text": "WPA2-Enterprise with 802.1X and RADIUS",
                "correct": True,
                "rationale": (
                    "Correct. WPA2-Enterprise uses 802.1X as the framework that causes "
                    "clients to authenticate to a RADIUS server using individual credentials "
                    "(EAP-based), eliminating the shared PSK."
                ),
            },
            {
                "id": "b",
                "text": "WPA2-Personal with MAC filtering",
                "correct": False,
                "rationale": (
                    "Incorrect. WPA2-Personal uses a shared pre-shared key (PSK). MAC "
                    "filtering is easily spoofed and is not per-user credential authentication."
                ),
            },
            {
                "id": "c",
                "text": "WPA3-SAE with TACACS+",
                "correct": False,
                "rationale": (
                    "Incorrect. WPA3-SAE (Simultaneous Authentication of Equals) is a personal "
                    "mode improvement replacing PSK. TACACS+ is a device administration "
                    "protocol (primarily for network gear management), not the standard "
                    "wireless client authentication protocol. RADIUS is the correct server "
                    "component for 802.1X wireless."
                ),
            },
            {
                "id": "d",
                "text": "WEP with TACACS+ for legacy compatibility",
                "correct": False,
                "rationale": (
                    "Incorrect. WEP is completely broken cryptographically and should never "
                    "be deployed. TACACS+ is not used for end-user wireless authentication."
                ),
            },
        ],
        "explanation": (
            "WPA2-Enterprise leverages 802.1X (port-based access control) to require "
            "individual authentication. The AP acts as an authenticator, forwarding "
            "credentials to a RADIUS authentication server. TACACS+ serves a similar "
            "AAA function but is used for network device administration, not end-user "
            "Wi-Fi access."
        ),
    },
    {
        "id": "c2d2-009",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Wireless security protocols",
        "stem": (
            "A wireless network administrator needs to upgrade from WPA2-Personal to WPA3. "
            "Which feature of WPA3-Personal provides forward secrecy that WPA2-Personal "
            "does NOT provide?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Simultaneous Authentication of Equals (SAE) replaces PSK, generating unique session keys so captured traffic cannot be decrypted even if the passphrase is later revealed",
                "correct": True,
                "rationale": (
                    "Correct. SAE (Dragonfly key exchange) derives unique per-session keys "
                    "even from the same passphrase, providing forward secrecy. In WPA2-PSK, "
                    "someone who captures the four-way handshake and later learns the PSK "
                    "can decrypt all recorded traffic."
                ),
            },
            {
                "id": "b",
                "text": "WPA3 increases the passphrase length to 256 characters, making brute-force impossible",
                "correct": False,
                "rationale": (
                    "Incorrect. WPA3 does not impose a specific maximum passphrase length as "
                    "its security improvement. The security gain is the SAE key exchange "
                    "mechanism, not passphrase length."
                ),
            },
            {
                "id": "c",
                "text": "WPA3 uses TKIP instead of AES to avoid patent-encumbered algorithms",
                "correct": False,
                "rationale": (
                    "Incorrect. WPA3 mandates AES-GCMP-256 (or at minimum AES-CCMP-128) and "
                    "explicitly removes TKIP. This statement is the opposite of the truth."
                ),
            },
            {
                "id": "d",
                "text": "WPA3 requires a RADIUS server for all deployments, eliminating shared secrets",
                "correct": False,
                "rationale": (
                    "Incorrect. WPA3-Personal still operates without a RADIUS server; it uses "
                    "SAE with a passphrase. WPA3-Enterprise is the mode that uses RADIUS."
                ),
            },
        ],
        "explanation": (
            "Forward secrecy means that disclosure of a long-term secret (the passphrase) "
            "does not allow decryption of previously captured sessions. WPA3's SAE key "
            "exchange (Dragonfly) achieves this by deriving ephemeral session keys. "
            "WPA2-PSK is vulnerable to offline dictionary attacks against captured "
            "handshakes."
        ),
    },
    # ── 2.4 Malware ──────────────────────────────────────────────────────────
    {
        "id": "c2d2-010",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Malware types & removal",
        "stem": (
            "A user reports that their PC is extremely slow and the CPU sits at 90–100% "
            "utilization even when idle. Task Manager shows an unfamiliar process consuming "
            "most of the CPU. The machine has no obvious ransom demand or data-theft "
            "symptoms. Which malware type BEST matches this description?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Cryptominer",
                "correct": True,
                "rationale": (
                    "Correct. Cryptominers (cryptojackers) consume massive CPU/GPU resources "
                    "to mine cryptocurrency for the attacker. The victim sees extreme "
                    "slowdown with no ransom demand or obvious data theft."
                ),
            },
            {
                "id": "b",
                "text": "Ransomware",
                "correct": False,
                "rationale": (
                    "Incorrect. Ransomware encrypts files and displays a payment demand. "
                    "High CPU alone without a ransom message does not match typical ransomware "
                    "behavior (which is often very fast then idle after encryption)."
                ),
            },
            {
                "id": "c",
                "text": "Keylogger",
                "correct": False,
                "rationale": (
                    "Incorrect. Keyloggers capture keystrokes silently with very low "
                    "CPU overhead by design — their goal is to be invisible. Extreme "
                    "CPU usage is not a keylogger characteristic."
                ),
            },
            {
                "id": "d",
                "text": "Boot sector virus",
                "correct": False,
                "rationale": (
                    "Incorrect. A boot sector virus loads before the OS and may cause "
                    "startup issues or file system corruption, but continuous 90%+ CPU "
                    "utilization from an unknown running process in Task Manager is not "
                    "its signature."
                ),
            },
        ],
        "explanation": (
            "Cryptominers are characterized by abnormally high CPU/GPU utilization from "
            "a hidden process. Unlike ransomware, there is no user notification; the "
            "attacker profits from compute cycles rather than data. Keyloggers are "
            "designed to be stealthy with minimal resource use."
        ),
    },
    {
        "id": "c2d2-011",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Malware types & removal",
        "stem": (
            "A technician suspects a rootkit infection on a Windows workstation. Standard "
            "antivirus scans from within the running OS report no threats, but anomalies "
            "persist. What is the MOST appropriate next step consistent with best practices "
            "for rootkit remediation?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Boot from a known-good external bootable antivirus/rescue environment to scan the drive offline",
                "correct": True,
                "rationale": (
                    "Correct. Rootkits hook into the OS kernel to hide themselves from "
                    "running scans. Booting from a trusted external media bypasses the "
                    "compromised OS, allowing the scanner to see the file system unfiltered "
                    "by the rootkit's hooks."
                ),
            },
            {
                "id": "b",
                "text": "Run Windows Defender full scan from within the infected OS",
                "correct": False,
                "rationale": (
                    "Incorrect. Running a scan from inside the compromised OS is exactly "
                    "what a rootkit defeats — it intercepts OS calls and hides malicious "
                    "files from the running scanner."
                ),
            },
            {
                "id": "c",
                "text": "Restore the most recent backup and consider the system clean",
                "correct": False,
                "rationale": (
                    "Incorrect. Restoring a backup without first understanding when the "
                    "rootkit was introduced could restore an already-infected state. Also, "
                    "the best-practice remediation process calls for scanning before restore "
                    "or reinstallation."
                ),
            },
            {
                "id": "d",
                "text": "Disable System Restore and rerun the in-OS antivirus scan",
                "correct": False,
                "rationale": (
                    "Incorrect. Disabling System Restore (to prevent malware from hiding "
                    "in restore points) is a step in the malware removal process but does "
                    "not help when the antivirus itself is blinded by the rootkit. The "
                    "offline boot approach is needed first."
                ),
            },
        ],
        "explanation": (
            "Rootkits operate below (or alongside) the OS to conceal themselves. Any "
            "scan running on top of the infected kernel is subject to the rootkit's "
            "interception. Booting from a trusted, external rescue environment scans "
            "the storage directly without the malicious OS hooks interfering."
        ),
    },
    {
        "id": "c2d2-012",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Malware types & removal",
        "stem": (
            "A technician follows the CompTIA-recommended seven-step malware removal "
            "process. After identifying and researching the malware, which step comes "
            "IMMEDIATELY before running the remediation tools to remove the malware?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Quarantine the infected system and disable System Restore / create a restore point",
                "correct": True,
                "rationale": (
                    "Correct. The CompTIA 7-step process is: (1) Investigate/identify, "
                    "(2) Quarantine infected systems, (3) Disable System Restore / create "
                    "restore point, (4) Remediate (scan/remove), (5) Schedule scans / "
                    "update definitions, (6) Re-enable System Restore / restore point, "
                    "(7) Educate end user. Quarantine and disabling System Restore both "
                    "precede the actual removal step."
                ),
            },
            {
                "id": "b",
                "text": "Educate the end user about safe browsing habits",
                "correct": False,
                "rationale": (
                    "Incorrect. User education is the FINAL step (step 7) in the CompTIA "
                    "malware removal process, performed after the system is clean and "
                    "restored to normal operation."
                ),
            },
            {
                "id": "c",
                "text": "Schedule future antivirus scans and update definitions",
                "correct": False,
                "rationale": (
                    "Incorrect. Scheduling scans and updating definitions is step 5, which "
                    "occurs AFTER remediation (step 4), not before it."
                ),
            },
            {
                "id": "d",
                "text": "Re-enable System Restore and create a new restore point",
                "correct": False,
                "rationale": (
                    "Incorrect. Re-enabling System Restore is step 6, which comes after "
                    "remediation and scan scheduling — near the end of the process, not "
                    "before removal."
                ),
            },
        ],
        "explanation": (
            "CompTIA A+ malware removal best-practice order: "
            "1) Identify/investigate & research malware symptoms; "
            "2) Quarantine infected systems; "
            "3) Disable System Restore (Windows) / create a restore point; "
            "4) Remediate — run updated AV/AM tools to remove; "
            "5) Schedule scans, update definitions; "
            "6) Re-enable System Restore, create new restore point; "
            "7) Educate end user. "
            "Quarantine and disabling System Restore (steps 2–3) always precede remediation."
        ),
    },
    {
        "id": "c2d2-013",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Malware types & removal",
        "stem": (
            "A user downloads what appears to be a free video editing program from a "
            "third-party site. After installation, bank credentials begin appearing in "
            "the attacker's logs. The program functions normally from the user's "
            "perspective. Which malware category BEST describes this threat?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Trojan",
                "correct": True,
                "rationale": (
                    "Correct. A Trojan disguises itself as legitimate software. The user "
                    "willingly installs it, not knowing it contains a hidden malicious payload "
                    "(in this case, credential stealing / spyware functionality). The program "
                    "appearing to work normally is the Trojan characteristic."
                ),
            },
            {
                "id": "b",
                "text": "Virus",
                "correct": False,
                "rationale": (
                    "Incorrect. A virus self-replicates by attaching to other files. The "
                    "scenario describes a standalone program with a hidden payload, not "
                    "a self-replicating file infector."
                ),
            },
            {
                "id": "c",
                "text": "Worm",
                "correct": False,
                "rationale": (
                    "Incorrect. A worm self-propagates across networks without user action "
                    "or host file attachment. The scenario requires user installation, "
                    "characteristic of a Trojan, not a worm."
                ),
            },
            {
                "id": "d",
                "text": "Ransomware",
                "correct": False,
                "rationale": (
                    "Incorrect. Ransomware encrypts data and demands payment. No encryption "
                    "or ransom demand appears in the scenario — only silent credential theft."
                ),
            },
        ],
        "explanation": (
            "A Trojan horse presents as benign software (the apparent video editor) while "
            "executing a hidden malicious function (credential theft). The key distinguisher "
            "from a virus is the absence of self-replication. From a worm: installation "
            "requires user action. From ransomware: no extortion component."
        ),
    },
    # ── 2.5 Social Engineering / Attacks ─────────────────────────────────────
    {
        "id": "c2d2-014",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Social engineering & attacks",
        "stem": (
            "A CFO receives a highly personalized email that references her name, the "
            "company's pending merger, and her direct reports. The email requests urgent "
            "wire transfer of $500,000. This attack is BEST classified as:"
        ),
        "options": [
            {
                "id": "a",
                "text": "Whaling",
                "correct": True,
                "rationale": (
                    "Correct. Whaling is a form of spear phishing that specifically targets "
                    "high-value individuals (executives, C-suite) with highly personalized "
                    "content. The CFO is the 'big fish' — hence 'whaling'."
                ),
            },
            {
                "id": "b",
                "text": "Vishing",
                "correct": False,
                "rationale": (
                    "Incorrect. Vishing is voice phishing — conducted over a phone call, "
                    "not email. The attack vector here is email."
                ),
            },
            {
                "id": "c",
                "text": "Generic phishing",
                "correct": False,
                "rationale": (
                    "Incorrect. Generic phishing uses broad, non-personalized messages "
                    "sent to many recipients. This attack is highly targeted and personalized, "
                    "which elevates it to whaling."
                ),
            },
            {
                "id": "d",
                "text": "Impersonation",
                "correct": False,
                "rationale": (
                    "Incorrect. While impersonation is a component (the attacker pretends "
                    "to be someone trusted), impersonation as a standalone term typically "
                    "describes in-person or phone identity masquerade. The email-based, "
                    "executive-targeting nature makes whaling the most precise classification."
                ),
            },
        ],
        "explanation": (
            "Whaling targets senior executives (C-suite) with tailored content to authorize "
            "large financial transfers or sensitive actions. It is a subcategory of spear "
            "phishing. Vishing is voice-based. Generic phishing is mass and untargeted. "
            "Impersonation can overlap but whaling is the specific, exam-tested term here."
        ),
    },
    {
        "id": "c2d2-015",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Social engineering & attacks",
        "stem": (
            "An attacker sets up a wireless access point with the same SSID and stronger "
            "signal than the legitimate corporate AP. Employees unknowingly connect to it, "
            "allowing the attacker to intercept all traffic. This attack is called:"
        ),
        "options": [
            {
                "id": "a",
                "text": "Evil twin",
                "correct": True,
                "rationale": (
                    "Correct. An evil twin is a rogue AP that mimics a legitimate AP's SSID "
                    "with a stronger signal, causing clients to connect to the attacker's "
                    "network — enabling on-path (man-in-the-middle) interception."
                ),
            },
            {
                "id": "b",
                "text": "On-path (man-in-the-middle) attack",
                "correct": False,
                "rationale": (
                    "Incorrect. On-path attack describes what the attacker accomplishes after "
                    "clients connect (intercepting traffic), but the setup described — a "
                    "cloned SSID rogue AP — is specifically called an evil twin. Evil twin "
                    "is the more precise term for this wireless attack vector."
                ),
            },
            {
                "id": "c",
                "text": "Spoofing",
                "correct": False,
                "rationale": (
                    "Incorrect. Spoofing involves forging an identity (IP, MAC, email). "
                    "While the evil twin spoofs the SSID, the exam-tested name for this "
                    "specific wireless rogue AP attack scenario is evil twin."
                ),
            },
            {
                "id": "d",
                "text": "DDoS",
                "correct": False,
                "rationale": (
                    "Incorrect. A DDoS floods a target with traffic to cause a denial of "
                    "service. This scenario involves traffic interception, not a flooding "
                    "attack."
                ),
            },
        ],
        "explanation": (
            "An evil twin attack deploys a rogue AP that clones the SSID (and optionally the "
            "BSSID) of a legitimate network. The stronger signal hijacks clients, then the "
            "attacker performs an on-path interception. Evil twin is the specific name; "
            "on-path is the consequence."
        ),
    },
    {
        "id": "c2d2-016",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Social engineering & attacks",
        "stem": (
            "An attacker submits the input `' OR '1'='1` into a web application's username "
            "field and gains access without a valid password. Which attack type is this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "SQL injection",
                "correct": True,
                "rationale": (
                    "Correct. SQL injection inserts malicious SQL syntax into an input field "
                    "to manipulate the database query. `' OR '1'='1` is the classic SQL "
                    "injection payload that makes the WHERE clause always evaluate to true, "
                    "bypassing authentication."
                ),
            },
            {
                "id": "b",
                "text": "Cross-site scripting (XSS)",
                "correct": False,
                "rationale": (
                    "Incorrect. XSS injects malicious scripts (typically JavaScript) into "
                    "web pages viewed by other users to steal session cookies or perform "
                    "actions on their behalf. It does not manipulate database queries."
                ),
            },
            {
                "id": "c",
                "text": "Brute force",
                "correct": False,
                "rationale": (
                    "Incorrect. Brute force systematically tries all possible passwords. "
                    "The scenario shows a single crafted string that exploits improper input "
                    "handling — that is injection, not brute force."
                ),
            },
            {
                "id": "d",
                "text": "Dictionary attack",
                "correct": False,
                "rationale": (
                    "Incorrect. A dictionary attack tries common words as passwords. "
                    "The payload `' OR '1'='1` is SQL syntax, not a guessed password."
                ),
            },
        ],
        "explanation": (
            "SQL injection exploits insufficient input sanitization to alter a database "
            "query's logic. The classic `' OR '1'='1` payload terminates the expected "
            "string and appends a condition that is always true, returning all records "
            "and bypassing authentication. Proper parameterized queries / prepared "
            "statements prevent this attack."
        ),
    },
    {
        "id": "c2d2-017",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Social engineering & attacks",
        "stem": (
            "A threat actor exploits a vulnerability in a widely deployed library the same "
            "day the vendor discovers and publicly discloses it — before any patch is "
            "available. Which term describes this attack?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Zero-day exploit",
                "correct": True,
                "rationale": (
                    "Correct. A zero-day exploit targets a vulnerability on (or before) the "
                    "day it is known to the vendor, meaning zero days have elapsed for a "
                    "patch to be developed and deployed."
                ),
            },
            {
                "id": "b",
                "text": "Insider threat",
                "correct": False,
                "rationale": (
                    "Incorrect. An insider threat originates from a person with authorized "
                    "access to organizational systems (employee, contractor). The scenario "
                    "describes an external exploit of a software vulnerability."
                ),
            },
            {
                "id": "c",
                "text": "Brute force",
                "correct": False,
                "rationale": (
                    "Incorrect. Brute force involves exhausting all possible credential "
                    "combinations. The scenario involves exploiting a specific software "
                    "vulnerability, which is entirely different."
                ),
            },
            {
                "id": "d",
                "text": "On-path attack",
                "correct": False,
                "rationale": (
                    "Incorrect. An on-path attack positions the attacker between two "
                    "communicating parties to intercept or alter data. The described "
                    "scenario is a software vulnerability exploitation."
                ),
            },
        ],
        "explanation": (
            "Zero-day refers to the time gap — zero days — between the vulnerability's "
            "discovery/disclosure and the attacker's exploitation. Because no patch "
            "exists yet, defenders have no signature-based protection. These are among "
            "the most dangerous attack types."
        ),
    },
    {
        "id": "c2d2-018",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Social engineering & attacks",
        "stem": (
            "A company discards printed org charts and internal memos in unsecured recycling "
            "bins outside the building. An attacker retrieves this information to plan a "
            "targeted social engineering attack. Which threat is BEST illustrated?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Dumpster diving",
                "correct": True,
                "rationale": (
                    "Correct. Dumpster diving is the act of searching through discarded "
                    "materials (trash, recycling) to find sensitive information that can "
                    "be exploited. Org charts and internal documents are classic targets."
                ),
            },
            {
                "id": "b",
                "text": "Shoulder surfing",
                "correct": False,
                "rationale": (
                    "Incorrect. Shoulder surfing involves looking over someone's shoulder "
                    "to observe what they type or view on screen. It requires physical "
                    "proximity to an active session, not recovering discarded documents."
                ),
            },
            {
                "id": "c",
                "text": "Tailgating",
                "correct": False,
                "rationale": (
                    "Incorrect. Tailgating is physically following an authorized person "
                    "through a secured entrance. No physical access to the building is "
                    "described in this scenario."
                ),
            },
            {
                "id": "d",
                "text": "Phishing",
                "correct": False,
                "rationale": (
                    "Incorrect. Phishing uses deceptive electronic communication (email, "
                    "text) to trick users. Recovering physical documents from trash is "
                    "dumpster diving."
                ),
            },
        ],
        "explanation": (
            "Dumpster diving exploits improper disposal of sensitive physical materials. "
            "The countermeasure is cross-cut shredding of all documents containing "
            "organizational, personal, or technical data before disposal. "
            "Shoulder surfing requires visual observation of active screens."
        ),
    },
    {
        "id": "c2d2-019",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Social engineering & attacks",
        "stem": (
            "An organization runs Windows XP on several manufacturing floor machines "
            "because the specialized control software is not compatible with newer OS "
            "versions. Microsoft no longer releases patches for Windows XP. Which "
            "vulnerability category do these systems represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "End-of-life (EOL) / unpatched OS",
                "correct": True,
                "rationale": (
                    "Correct. Windows XP reached end of life in 2014. EOL operating systems "
                    "no longer receive security patches, meaning known vulnerabilities will "
                    "never be remediated by the vendor — a critical ongoing risk."
                ),
            },
            {
                "id": "b",
                "text": "Zero-day vulnerability",
                "correct": False,
                "rationale": (
                    "Incorrect. Zero-day refers to a newly discovered vulnerability with no "
                    "patch yet available. XP's vulnerabilities are well-documented and have "
                    "been known for years — they are simply unpatched by design (EOL)."
                ),
            },
            {
                "id": "c",
                "text": "BYOD policy violation",
                "correct": False,
                "rationale": (
                    "Incorrect. BYOD refers to employees bringing personal devices to work. "
                    "These are company-owned, organization-deployed machines, not personal "
                    "devices."
                ),
            },
            {
                "id": "d",
                "text": "Non-compliant system",
                "correct": False,
                "rationale": (
                    "Incorrect. While non-compliant is related, the most precise "
                    "CompTIA-tested term for a system whose OS vendor no longer provides "
                    "patches is 'end-of-life'. Non-compliant is a broader policy term; "
                    "EOL specifically addresses the no-patch status."
                ),
            },
        ],
        "explanation": (
            "End-of-life (EOL) operating systems receive no further security patches from "
            "the vendor. Every vulnerability discovered after EOL remains permanently "
            "exploitable on those systems. Compensating controls (network isolation, "
            "application whitelisting) are often used when EOL systems cannot be replaced."
        ),
    },
    # ── 2.6 Windows OS Security Settings ─────────────────────────────────────
    {
        "id": "c2d2-020",
        "domain": 2,
        "objective": "2.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "NTFS vs share permissions",
        "stem": (
            "A file has NTFS permission 'Modify' for a user, but the shared folder it lives "
            "in grants that user only 'Read' via share permissions. The user accesses it "
            "over the network. What is the user's effective permission?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Read — the most restrictive of the combined share and NTFS permissions applies over the network",
                "correct": True,
                "rationale": (
                    "Correct. When accessed over the network, the effective permission is "
                    "the MORE restrictive of the (cumulative) share and NTFS permissions. "
                    "Share=Read is more restrictive than NTFS=Modify, so the user gets Read."
                ),
            },
            {
                "id": "b",
                "text": "Modify — NTFS always overrides share permissions",
                "correct": False,
                "rationale": (
                    "Incorrect. NTFS does not override share permissions over the network; "
                    "the more restrictive of the two wins. Locally (not over the share), "
                    "only NTFS applies."
                ),
            },
            {
                "id": "c",
                "text": "Full Control — permissions are added together",
                "correct": False,
                "rationale": (
                    "Incorrect. Share and NTFS permissions are not summed; the more "
                    "restrictive set is the effective access across the network."
                ),
            },
            {
                "id": "d",
                "text": "No access — conflicting permissions deny all",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no explicit Deny here; conflicting allow levels "
                    "resolve to the most restrictive allow (Read), not to no access."
                ),
            },
        ],
        "explanation": (
            "Over the network, effective permission = the more restrictive of (combined share) "
            "and (combined NTFS). Locally, only NTFS applies. An explicit Deny always "
            "overrides Allow regardless of the other permission level."
        ),
    },
    {
        "id": "c2d2-021",
        "domain": 2,
        "objective": "2.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "NTFS vs share permissions",
        "stem": (
            "A file with NTFS permissions of 'Read' for UserA is copied from a shared "
            "network folder to a local NTFS folder on the same computer. What happens "
            "to the file's NTFS permissions after the copy?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The file inherits the permissions of the destination folder",
                "correct": True,
                "rationale": (
                    "Correct. When a file is COPIED to a new NTFS location, it inherits the "
                    "permissions of the destination folder. The source permissions are not "
                    "preserved."
                ),
            },
            {
                "id": "b",
                "text": "The file retains its original NTFS permissions from the source",
                "correct": False,
                "rationale": (
                    "Incorrect. Retaining original permissions occurs when a file is MOVED "
                    "within the same NTFS volume, not when it is copied. A copy always "
                    "inherits the destination's permissions."
                ),
            },
            {
                "id": "c",
                "text": "The file loses all permissions and becomes accessible to everyone",
                "correct": False,
                "rationale": (
                    "Incorrect. Copying does not remove all permissions; the file adopts "
                    "the destination folder's inherited permissions, which may or may not "
                    "be permissive depending on how that folder is set up."
                ),
            },
            {
                "id": "d",
                "text": "The file's permissions are merged with the destination folder's permissions",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no merging of source and destination permissions "
                    "on copy. The copy operation results in the destination folder's "
                    "inherited permissions applying to the new file."
                ),
            },
        ],
        "explanation": (
            "NTFS copy/move permission rules: "
            "COPY (any volume or within same volume): inherits destination permissions. "
            "MOVE within the same NTFS volume: retains original permissions. "
            "MOVE to a different NTFS volume: inherits destination permissions (treated "
            "as a copy then delete)."
        ),
    },
    {
        "id": "c2d2-022",
        "domain": 2,
        "objective": "2.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows security settings",
        "stem": (
            "A standard user on Windows 10 attempts to install software and is presented "
            "with a prompt asking for administrator credentials. After the credentials are "
            "entered, the installation proceeds. Which Windows security feature produced "
            "this prompt?"
        ),
        "options": [
            {
                "id": "a",
                "text": "User Account Control (UAC)",
                "correct": True,
                "rationale": (
                    "Correct. UAC prompts for elevation when a user without administrative "
                    "rights attempts a privileged action. A standard user sees a credential "
                    "prompt (over-the-shoulder consent) rather than a simple yes/no dialog."
                ),
            },
            {
                "id": "b",
                "text": "Windows Defender Firewall",
                "correct": False,
                "rationale": (
                    "Incorrect. Windows Defender Firewall manages network traffic and may "
                    "prompt about network access for new programs, but it does not produce "
                    "the administrator credential prompt for software installation."
                ),
            },
            {
                "id": "c",
                "text": "BitLocker",
                "correct": False,
                "rationale": (
                    "Incorrect. BitLocker is a disk encryption feature. It does not generate "
                    "credential prompts for software installation."
                ),
            },
            {
                "id": "d",
                "text": "NTFS permission enforcement",
                "correct": False,
                "rationale": (
                    "Incorrect. NTFS permissions control file/folder access. While NTFS "
                    "may deny writes to system directories, the interactive credential "
                    "elevation dialog is specifically UAC behavior."
                ),
            },
        ],
        "explanation": (
            "User Account Control (UAC) implements the principle of least privilege by "
            "running applications at standard user rights even for local admins (admin "
            "approval mode). A standard user attempting a privileged action sees an "
            "over-the-shoulder (OTS) credential prompt asking for admin credentials."
        ),
    },
    {
        "id": "c2d2-023",
        "domain": 2,
        "objective": "2.6",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "BitLocker & encryption (EFS)",
        "stem": (
            "A sales executive uses a USB flash drive to carry sensitive contracts between "
            "offices. The company wants to encrypt the drive so data is protected if the "
            "drive is lost, without requiring the destination PC to be domain-joined. "
            "Which Windows encryption feature is MOST appropriate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "BitLocker To Go",
                "correct": True,
                "rationale": (
                    "Correct. BitLocker To Go extends BitLocker encryption to removable "
                    "drives (USB flash drives, external HDDs). The drive can be unlocked "
                    "with a password on any Windows system — no domain membership required."
                ),
            },
            {
                "id": "b",
                "text": "EFS (Encrypting File System)",
                "correct": False,
                "rationale": (
                    "Incorrect. EFS encrypts individual files/folders tied to a specific "
                    "user's certificate on a specific NTFS volume. EFS-encrypted files on "
                    "a removable drive cannot be decrypted on another PC without the "
                    "certificate — and FAT32/exFAT USB drives don't support EFS at all."
                ),
            },
            {
                "id": "c",
                "text": "BitLocker (full volume) on the USB drive",
                "correct": False,
                "rationale": (
                    "Incorrect. Standard BitLocker is designed for fixed drives with TPM "
                    "integration. BitLocker TO GO is the specific feature for removable "
                    "storage. Selecting 'BitLocker' generically is a less precise answer "
                    "than 'BitLocker To Go'."
                ),
            },
            {
                "id": "d",
                "text": "Windows Information Protection (WIP)",
                "correct": False,
                "rationale": (
                    "Incorrect. WIP (formerly EDP) is an MDM-based data protection policy "
                    "for managed devices, not a standalone encryption tool for removable "
                    "drives used across arbitrary Windows machines."
                ),
            },
        ],
        "explanation": (
            "BitLocker To Go was introduced to address exactly this scenario: removable "
            "media encryption without requiring NTFS (works with FAT32 and exFAT) and "
            "without requiring domain membership. A password unlocks the drive on any "
            "compatible Windows PC. EFS is NTFS-only and certificate-tied to a specific "
            "user profile."
        ),
    },
    {
        "id": "c2d2-024",
        "domain": 2,
        "objective": "2.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows security settings",
        "stem": (
            "Which Windows local user account type has the FEWEST default privileges and "
            "is intended for temporary or guest access without a persistent profile between "
            "sessions?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Guest",
                "correct": True,
                "rationale": (
                    "Correct. The Guest account has the most restricted privileges of the "
                    "built-in account types. It cannot install software, change settings, "
                    "or access other users' files, and session data does not persist."
                ),
            },
            {
                "id": "b",
                "text": "Standard User",
                "correct": False,
                "rationale": (
                    "Incorrect. A Standard User has more rights than a Guest — standard "
                    "users have a persistent profile and can run most applications. They "
                    "are still restricted from administrative tasks."
                ),
            },
            {
                "id": "c",
                "text": "Power User",
                "correct": False,
                "rationale": (
                    "Incorrect. Power User (legacy) had elevated rights above Standard "
                    "User, including the ability to install some software. This is more "
                    "privileged than a Standard User, not fewer."
                ),
            },
            {
                "id": "d",
                "text": "Administrator",
                "correct": False,
                "rationale": (
                    "Incorrect. Administrator has the highest local privileges and full "
                    "control over the system — the opposite of the fewest privileges."
                ),
            },
        ],
        "explanation": (
            "Windows built-in accounts in order of increasing privilege: "
            "Guest < Standard User < Power User (legacy) < Administrator. "
            "Guest is disabled by default for security and provides the most restricted, "
            "non-persistent access. The Power User group is largely deprecated in modern "
            "Windows but still appears on CompTIA exams."
        ),
    },
    # ── 2.7 Mobile/Embedded Device Security ──────────────────────────────────
    {
        "id": "c2d2-025",
        "domain": 2,
        "objective": "2.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile/embedded device security",
        "stem": (
            "A corporate smartphone containing sensitive email and CRM data is reported "
            "stolen. The device is enrolled in the company's MDM solution. Which action "
            "should the IT administrator take FIRST to protect the data on the device?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Issue a remote wipe command through the MDM console",
                "correct": True,
                "rationale": (
                    "Correct. A remote wipe erases all data on the device, preventing "
                    "unauthorized access to sensitive corporate information. This is the "
                    "primary and most immediate data-protection action for a stolen enrolled device."
                ),
            },
            {
                "id": "b",
                "text": "Disable the employee's Active Directory account",
                "correct": False,
                "rationale": (
                    "Incorrect. Disabling the AD account prevents new logins to corporate "
                    "systems but does not erase data already on the device. The device "
                    "itself still holds cached email and CRM data."
                ),
            },
            {
                "id": "c",
                "text": "Use the locator app to track the device's GPS coordinates",
                "correct": False,
                "rationale": (
                    "Incorrect. While locating the device may help law enforcement recover "
                    "it, this does not protect the data immediately. A remote wipe provides "
                    "immediate data protection."
                ),
            },
            {
                "id": "d",
                "text": "Change the user's email password",
                "correct": False,
                "rationale": (
                    "Incorrect. Changing the email password prevents future email sync "
                    "but does not erase existing email already cached on the stolen device, "
                    "leaving that data exposed."
                ),
            },
        ],
        "explanation": (
            "Remote wipe is the immediate data protection response for a stolen MDM-enrolled "
            "device. It erases all data (or, in a selective wipe, only corporate data) "
            "regardless of the device's current lock state. Locator apps, AD account "
            "changes, and password resets do not address data already resident on the device."
        ),
    },
    {
        "id": "c2d2-026",
        "domain": 2,
        "objective": "2.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile/embedded device security",
        "stem": (
            "A company allows employees to use personal smartphones to access corporate "
            "email (BYOD). The security policy requires that corporate data be segmented "
            "from personal data and that IT can wipe only corporate data without affecting "
            "personal content. Which MDM capability fulfills this requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Containerization / selective wipe via MDM profile",
                "correct": True,
                "rationale": (
                    "Correct. MDM containerization creates a secure, managed partition for "
                    "corporate apps and data. A selective (corporate) wipe removes only the "
                    "managed container, leaving personal data intact — satisfying both "
                    "requirements."
                ),
            },
            {
                "id": "b",
                "text": "Full device remote wipe",
                "correct": False,
                "rationale": (
                    "Incorrect. A full remote wipe erases the entire device including "
                    "personal data. BYOD policies typically require selective wipe to "
                    "avoid destroying employees' personal information."
                ),
            },
            {
                "id": "c",
                "text": "Device encryption enforcement",
                "correct": False,
                "rationale": (
                    "Incorrect. Device encryption protects data at rest but does not "
                    "create the separation between corporate and personal data, nor does "
                    "it enable selective wipe."
                ),
            },
            {
                "id": "d",
                "text": "Screen lock enforcement with a complex PIN",
                "correct": False,
                "rationale": (
                    "Incorrect. Enforcing a screen lock prevents unauthorized physical "
                    "access but does not segment or selectively remove corporate data."
                ),
            },
        ],
        "explanation": (
            "BYOD MDM policies often use containerization (e.g., Android for Work / Work "
            "Profile, Apple MDM profiles) to sandbox corporate apps and data. A selective "
            "wipe removes only the managed container, preserving personal data. Full wipe "
            "would violate employee privacy expectations under a BYOD program."
        ),
    },
    {
        "id": "c2d2-027",
        "domain": 2,
        "objective": "2.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile/embedded device security",
        "stem": (
            "A hospital deploys smart IV pumps connected to the clinical network via Wi-Fi. "
            "The pumps run a proprietary embedded OS that cannot be updated. Which is the "
            "MOST important security concern these devices introduce?"
        ),
        "options": [
            {
                "id": "a",
                "text": "IoT/embedded devices with unpatched firmware create persistent vulnerabilities on the clinical network",
                "correct": True,
                "rationale": (
                    "Correct. IoT/embedded medical devices often run firmware that cannot "
                    "be updated by end users. Unpatched vulnerabilities in these devices "
                    "create a permanent attack surface on any network segment they occupy, "
                    "which is especially critical in healthcare."
                ),
            },
            {
                "id": "b",
                "text": "The devices consume too much bandwidth, degrading network performance",
                "correct": False,
                "rationale": (
                    "Incorrect. While network performance is an operational concern, it is "
                    "not a security concern. The unpatched, unupdatable OS is the primary "
                    "security issue."
                ),
            },
            {
                "id": "c",
                "text": "The pumps do not support screen locks, allowing unauthorized physical interaction",
                "correct": False,
                "rationale": (
                    "Incorrect. Physical interaction controls are a concern but secondary "
                    "to the network-level vulnerability introduced by unpatched embedded OS "
                    "on network-connected devices."
                ),
            },
            {
                "id": "d",
                "text": "The devices are not enrolled in MDM and cannot receive policy enforcement",
                "correct": False,
                "rationale": (
                    "Incorrect. MDM enrollment is a factor, but the fundamental issue is "
                    "the inability to patch an EOL/proprietary OS, leaving known "
                    "vulnerabilities permanently open."
                ),
            },
        ],
        "explanation": (
            "Networked IoT and embedded medical devices with non-updatable firmware "
            "represent EOL-like vulnerability exposure on the network. Compensating "
            "controls include network segmentation (isolating the devices on a dedicated "
            "VLAN), strict firewall rules between segments, and behavior monitoring."
        ),
    },
    # ── 2.8 Data Destruction & Disposal ──────────────────────────────────────
    {
        "id": "c2d2-028",
        "domain": 2,
        "objective": "2.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Data destruction & disposal",
        "stem": (
            "A government contractor must dispose of HDDs containing classified data. "
            "The drives must be rendered completely unrecoverable — even forensic recovery "
            "should be impossible. Which method BEST meets this requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Degaussing followed by physical shredding",
                "correct": True,
                "rationale": (
                    "Correct. Degaussing uses a powerful magnetic field to destroy the "
                    "magnetic domains on the platters, making data unreadable. Shredding "
                    "then physically destroys the platters. Together they ensure no "
                    "forensic recovery is possible — meeting the highest classification "
                    "disposal standards."
                ),
            },
            {
                "id": "b",
                "text": "Low-level format (zero-fill) of the drives",
                "correct": False,
                "rationale": (
                    "Incorrect. A low-level / zero-fill overwrite can be sufficient for "
                    "unclassified data, but for classified data, advanced forensic "
                    "techniques (e.g., magnetic force microscopy) can potentially recover "
                    "overwritten data. Physical destruction is required for the highest "
                    "assurance."
                ),
            },
            {
                "id": "c",
                "text": "Standard format and donate the drives for recycling",
                "correct": False,
                "rationale": (
                    "Incorrect. A standard (high-level) format only removes the file "
                    "system metadata; data remains on the platters and is trivially "
                    "recoverable. This is never acceptable for classified data disposal."
                ),
            },
            {
                "id": "d",
                "text": "Enable BitLocker and then delete the encryption key",
                "correct": False,
                "rationale": (
                    "Incorrect. Crypto-erase (deleting the encryption key) is an accepted "
                    "method for SSD disposal, but for classified HDDs requiring certifiable "
                    "destruction with a physical evidence trail, physical destruction methods "
                    "are required by most government standards (NIST 800-88)."
                ),
            },
        ],
        "explanation": (
            "For classified media, physical destruction is the gold standard. Degaussing "
            "destroys magnetic data; shredding destroys the physical medium. A certificate "
            "of destruction provides the required audit trail. Low-level overwrites and "
            "crypto-erase are acceptable for lower-classification or SSD scenarios but not "
            "for the highest assurance requirement described."
        ),
    },
    {
        "id": "c2d2-029",
        "domain": 2,
        "objective": "2.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Data destruction & disposal",
        "stem": (
            "A company is donating used laptops to a nonprofit. The laptops held sensitive "
            "HR data. The drives are traditional HDDs. Which preparation step BEST ensures "
            "data cannot be recovered while allowing the drives to be reused in the donated "
            "systems?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Perform a multi-pass overwrite (DoD 5220.22-M or similar) on each drive",
                "correct": True,
                "rationale": (
                    "Correct. A multi-pass overwrite (data wiping / secure erase) repeatedly "
                    "overwrites all sectors, making data recovery extremely difficult while "
                    "preserving the drive hardware for reuse. This balances security and "
                    "repurposing goals."
                ),
            },
            {
                "id": "b",
                "text": "Perform a standard (quick) format of each drive",
                "correct": False,
                "rationale": (
                    "Incorrect. A quick format removes only the file table; data remains "
                    "on the disk and is easily recovered with free tools. This is not "
                    "acceptable for drives that held sensitive data."
                ),
            },
            {
                "id": "c",
                "text": "Drill through each drive platter to destroy them physically",
                "correct": False,
                "rationale": (
                    "Incorrect. Physical drilling destroys the drive and makes it unusable. "
                    "The requirement is to reuse the drives in donated laptops, so "
                    "destruction is not appropriate here."
                ),
            },
            {
                "id": "d",
                "text": "Degauss the drives before donating",
                "correct": False,
                "rationale": (
                    "Incorrect. Degaussing destroys the drive's servo tracks along with the "
                    "data, rendering a traditional HDD unusable afterward. The drive cannot "
                    "be reused after degaussing."
                ),
            },
        ],
        "explanation": (
            "When repurposing HDDs, data wiping (overwrite) is the correct approach: it "
            "sanitizes data while preserving the drive for continued use. Degaussing and "
            "drilling are destruction methods (not repurposing). A standard format leaves "
            "data readily recoverable."
        ),
    },
    {
        "id": "c2d2-030",
        "domain": 2,
        "objective": "2.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Data destruction & disposal",
        "stem": (
            "After a third-party vendor destroys a batch of decommissioned hard drives "
            "on behalf of a financial institution, what document should the institution "
            "receive to prove the drives were properly destroyed and satisfy audit "
            "requirements?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Certificate of destruction",
                "correct": True,
                "rationale": (
                    "Correct. A certificate of destruction is the formal document provided "
                    "by the destruction vendor, listing drive serial numbers and the method "
                    "of destruction. It satisfies regulatory audit trails (HIPAA, PCI-DSS, "
                    "SOX, etc.)."
                ),
            },
            {
                "id": "b",
                "text": "Chain of custody log",
                "correct": False,
                "rationale": (
                    "Incorrect. A chain of custody log tracks who handled the media "
                    "throughout the process, but the final document confirming destruction "
                    "occurred is the certificate of destruction. Chain of custody is part "
                    "of the evidence handling process, not the disposal certification."
                ),
            },
            {
                "id": "c",
                "text": "Data sanitization report",
                "correct": False,
                "rationale": (
                    "Incorrect. A sanitization report typically accompanies a software wipe "
                    "or overwrite, not physical destruction. The CompTIA-tested term for "
                    "physical destruction verification is certificate of destruction."
                ),
            },
            {
                "id": "d",
                "text": "Asset disposal receipt",
                "correct": False,
                "rationale": (
                    "Incorrect. An asset disposal receipt is a general inventory/accounting "
                    "document. It does not specifically certify the method or completeness "
                    "of data destruction required for compliance."
                ),
            },
        ],
        "explanation": (
            "A certificate of destruction is the required documentation for physical "
            "media destruction. It typically lists asset tags, serial numbers, destruction "
            "method, date, and is signed by the destroying party. Financial, healthcare, "
            "and government regulators often require this document for compliance."
        ),
    },
    # ── 2.9 SOHO Network Security ─────────────────────────────────────────────
    {
        "id": "c2d2-031",
        "domain": 2,
        "objective": "2.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SOHO network security",
        "stem": (
            "A small business installs a new SOHO wireless router. Which TWO initial "
            "configuration changes are the MOST critical to perform before connecting "
            "it to production? (Choose the single BEST answer representing the top "
            "priority pair.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Change the default administrator password and change the default SSID",
                "correct": True,
                "rationale": (
                    "Correct. Leaving the default admin password allows anyone on the LAN "
                    "to take full control of the router. The default SSID often reveals the "
                    "router model/vendor, aiding targeted attacks. These two changes are the "
                    "most universally cited initial SOHO hardening steps."
                ),
            },
            {
                "id": "b",
                "text": "Enable UPnP and configure port forwarding",
                "correct": False,
                "rationale": (
                    "Incorrect. UPnP allows devices to automatically open ports — a security "
                    "risk that should typically be disabled, not enabled. Port forwarding "
                    "is a specific configuration need, not a baseline security step."
                ),
            },
            {
                "id": "c",
                "text": "Enable SSID broadcast and set the channel to auto",
                "correct": False,
                "rationale": (
                    "Incorrect. SSID broadcast is already enabled by default; enabling "
                    "it is not a hardening step. Channel auto-selection is an operational "
                    "optimization, not a security configuration."
                ),
            },
            {
                "id": "d",
                "text": "Configure DHCP reservations and enable guest network",
                "correct": False,
                "rationale": (
                    "Incorrect. DHCP reservations are useful but not a first-priority "
                    "security step. Enabling a guest network without first changing the "
                    "admin password would expose the router to management compromise."
                ),
            },
        ],
        "explanation": (
            "Default credentials are the leading cause of SOHO router compromise. After "
            "changing the admin password, changing the SSID removes vendor fingerprinting. "
            "Subsequent hardening includes disabling UPnP, enabling WPA2/WPA3, updating "
            "firmware, and configuring firewall rules."
        ),
    },
    {
        "id": "c2d2-032",
        "domain": 2,
        "objective": "2.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SOHO network security",
        "stem": (
            "A home office user wants to host an internal web server accessible from the "
            "internet on port 443. She has a static WAN IP and wants to keep the server "
            "off the main LAN segment. Which SOHO firewall/router feature achieves this "
            "network isolation for the server while still allowing external HTTPS access?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Place the server in a screened subnet (DMZ) and configure port forwarding/mapping for port 443 to that segment",
                "correct": True,
                "rationale": (
                    "Correct. A screened subnet (DMZ) isolates the public-facing server from "
                    "the internal LAN. Port forwarding maps inbound WAN port 443 traffic to "
                    "the server's LAN/DMZ IP. This is the standard architecture for safely "
                    "hosting internet-accessible services."
                ),
            },
            {
                "id": "b",
                "text": "Enable UPnP so the web server can automatically open port 443",
                "correct": False,
                "rationale": (
                    "Incorrect. UPnP automates port opening but provides no network "
                    "segmentation. The server would remain on the main LAN, and UPnP "
                    "itself is a security risk that should generally be disabled."
                ),
            },
            {
                "id": "c",
                "text": "Assign the server a DHCP reservation and expose it on the main LAN",
                "correct": False,
                "rationale": (
                    "Incorrect. A DHCP reservation gives the server a consistent IP but "
                    "places it on the main LAN with no isolation. If the server is "
                    "compromised, the attacker has direct LAN access."
                ),
            },
            {
                "id": "d",
                "text": "Disable the firewall entirely to allow all inbound traffic",
                "correct": False,
                "rationale": (
                    "Incorrect. Disabling the firewall exposes every device on the network "
                    "to inbound internet traffic — a severe security risk with no isolation "
                    "benefit."
                ),
            },
        ],
        "explanation": (
            "A screened subnet (DMZ) creates an isolated network zone between the internet "
            "and the internal LAN for publicly accessible servers. Port forwarding (port "
            "mapping) directs inbound WAN traffic on specific ports to the DMZ server's "
            "address. This limits blast radius if the server is compromised."
        ),
    },
    {
        "id": "c2d2-033",
        "domain": 2,
        "objective": "2.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SOHO network security",
        "stem": (
            "A SOHO router's firmware has not been updated in three years. A newly published "
            "CVE describes a remote code execution vulnerability in the router's web "
            "management interface. Which action should be taken FIRST?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Apply the manufacturer's firmware update immediately",
                "correct": True,
                "rationale": (
                    "Correct. Firmware updates patch known vulnerabilities including the "
                    "published CVE. Keeping router firmware current is a fundamental SOHO "
                    "security practice and the most direct remediation for the stated CVE."
                ),
            },
            {
                "id": "b",
                "text": "Change the SSID to hide the router model from attackers",
                "correct": False,
                "rationale": (
                    "Incorrect. Changing the SSID obscures the model name but does not "
                    "patch the vulnerability. A determined attacker can fingerprint the "
                    "router regardless, and the RCE flaw remains exploitable."
                ),
            },
            {
                "id": "c",
                "text": "Disable wireless and use wired-only connections",
                "correct": False,
                "rationale": (
                    "Incorrect. If the CVE is in the web management interface (accessible "
                    "from LAN), disabling wireless does not eliminate the attack surface. "
                    "Patching is the correct remediation."
                ),
            },
            {
                "id": "d",
                "text": "Enable MAC address filtering to restrict connected devices",
                "correct": False,
                "rationale": (
                    "Incorrect. MAC filtering restricts which devices can associate with "
                    "the wireless network but does not patch the RCE vulnerability in the "
                    "management interface. MAC addresses are also easily spoofed."
                ),
            },
        ],
        "explanation": (
            "Firmware updates are the primary remediation for router CVEs. Obscuring "
            "identifiers and adjusting access policies are secondary measures that do not "
            "fix the underlying vulnerability. Always check the manufacturer's site for "
            "firmware updates when a CVE is published for network equipment."
        ),
    },
    # ── 2.10 Browser Security ─────────────────────────────────────────────────
    {
        "id": "c2d2-034",
        "domain": 2,
        "objective": "2.10",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Browser security",
        "stem": (
            "A user visits a banking website and the browser displays a padlock icon with "
            "the message 'Certificate expired' in the address bar. Which is the MOST "
            "appropriate action?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Do not proceed; an expired certificate cannot be verified as trustworthy and may indicate a security problem",
                "correct": True,
                "rationale": (
                    "Correct. An expired TLS certificate means the site's identity cannot "
                    "be cryptographically verified for the current time period. Banking "
                    "sites should always have valid certificates; proceeding exposes the "
                    "user to potential MITM or fraudulent site risk."
                ),
            },
            {
                "id": "b",
                "text": "Click 'Proceed anyway' since the padlock icon means the connection is still encrypted",
                "correct": False,
                "rationale": (
                    "Incorrect. The padlock indicates a TLS connection attempt, but an "
                    "expired certificate means identity verification has failed. Encryption "
                    "alone does not prove the server is who it claims to be — an attacker's "
                    "server can also offer TLS."
                ),
            },
            {
                "id": "c",
                "text": "Clear the browser cache and retry, as this is likely a local caching issue",
                "correct": False,
                "rationale": (
                    "Incorrect. Browser cache does not cause a certificate expiration "
                    "warning. The certificate's validity period is checked against the "
                    "current date on the server's certificate — a cache clear will not "
                    "fix an expired cert."
                ),
            },
            {
                "id": "d",
                "text": "Disable TLS verification in browser settings to access the site",
                "correct": False,
                "rationale": (
                    "Incorrect. Disabling TLS verification removes the browser's ability "
                    "to validate any server certificate, leaving all HTTPS connections "
                    "unverified — a severe security degradation that should never be done."
                ),
            },
        ],
        "explanation": (
            "A valid, unexpired TLS certificate from a trusted CA is required to establish "
            "the authenticity of an HTTPS site. For a banking site, any certificate error "
            "should result in not proceeding. Encryption (the padlock) without valid "
            "identity verification does not protect against impersonation attacks."
        ),
    },
    {
        "id": "c2d2-035",
        "domain": 2,
        "objective": "2.10",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Browser security",
        "stem": (
            "A user downloads a browser extension from an unfamiliar website rather than "
            "the browser's official extension store. The site provides a SHA-256 hash of "
            "the file. Which step should the user perform BEFORE installing the extension "
            "to verify file integrity?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Compute the SHA-256 hash of the downloaded file and compare it to the hash published on the site",
                "correct": True,
                "rationale": (
                    "Correct. Hash verification confirms the downloaded file was not "
                    "tampered with in transit. If the computed hash matches the published "
                    "hash, file integrity is confirmed. This is the standard integrity "
                    "verification step for software downloaded from untrusted sources."
                ),
            },
            {
                "id": "b",
                "text": "Scan the file with antivirus software only",
                "correct": False,
                "rationale": (
                    "Incorrect. Antivirus scanning detects known malware signatures but "
                    "does not verify that the file matches what the author published. "
                    "A file can be clean by AV scan yet still be a modified/substituted "
                    "version. Hash verification is specifically for integrity checking."
                ),
            },
            {
                "id": "c",
                "text": "Check that the website uses HTTPS before downloading",
                "correct": False,
                "rationale": (
                    "Incorrect. HTTPS ensures the connection is encrypted and the domain "
                    "is authenticated, but it does not verify the integrity of individual "
                    "files served. A compromised or malicious HTTPS site can still serve "
                    "modified files."
                ),
            },
            {
                "id": "d",
                "text": "Install the extension and monitor for unusual behavior",
                "correct": False,
                "rationale": (
                    "Incorrect. Installing first and watching for problems is reactive "
                    "and risky — a malicious extension could exfiltrate data or perform "
                    "actions before suspicious behavior is noticed. Verification must "
                    "happen before installation."
                ),
            },
        ],
        "explanation": (
            "Hash verification (comparing the file's computed hash against a known-good "
            "published hash) confirms file integrity — that the file has not been altered. "
            "HTTPS verifies transport security. AV scanning detects known malware. Neither "
            "substitute for hash verification when the specific concern is file tampering "
            "or substitution."
        ),
    },
    {
        "id": "c2d2-036",
        "domain": 2,
        "objective": "2.10",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Browser security",
        "stem": (
            "A user wants to research medical information on a shared public computer "
            "without their browsing history, cookies, or form data being saved locally "
            "after the session. Which browser feature should they use?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Private/Incognito browsing mode",
                "correct": True,
                "rationale": (
                    "Correct. Private/Incognito mode prevents the browser from storing "
                    "history, cookies, cached content, and form data locally after the "
                    "session ends. This is the correct feature for the described use case."
                ),
            },
            {
                "id": "b",
                "text": "Clear browsing cache after every page load",
                "correct": False,
                "rationale": (
                    "Incorrect. Manually clearing cache is cumbersome and error-prone. "
                    "It also does not prevent history or cookies from being written "
                    "during the session — Private mode accomplishes this automatically "
                    "and comprehensively."
                ),
            },
            {
                "id": "c",
                "text": "Enable browser sync to store browsing data in the cloud",
                "correct": False,
                "rationale": (
                    "Incorrect. Browser sync uploads browsing data (history, passwords, "
                    "bookmarks) to the user's cloud account — the opposite of privacy on "
                    "a shared computer."
                ),
            },
            {
                "id": "d",
                "text": "Install an ad blocker extension",
                "correct": False,
                "rationale": (
                    "Incorrect. Ad blockers block advertising trackers, but they do not "
                    "prevent local storage of browsing history, cookies, or form data."
                ),
            },
        ],
        "explanation": (
            "Private/Incognito browsing mode creates a temporary session that does not "
            "persist history, cookies, or form data on the local machine after closing "
            "the window. Note: it does NOT make the user anonymous to websites, ISPs, "
            "or network monitors — it only prevents local data storage."
        ),
    },
    # ── Multiple Response Questions ──────────────────────────────────────────
    {
        "id": "c2d2-037",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Malware types & removal",
        "stem": (
            "A technician is following the CompTIA best-practice malware removal process. "
            "Which THREE of the following steps are performed BEFORE running antivirus "
            "remediation tools? (Choose THREE.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Quarantine the infected system from the network",
                "correct": True,
                "rationale": (
                    "Correct. Quarantine (step 2) is performed before remediation to "
                    "prevent the malware from spreading to other systems."
                ),
            },
            {
                "id": "b",
                "text": "Disable System Restore on the infected machine",
                "correct": True,
                "rationale": (
                    "Correct. Disabling System Restore (step 3) prevents malware from "
                    "hiding in restore points and re-infecting after removal."
                ),
            },
            {
                "id": "c",
                "text": "Identify and research the malware symptoms",
                "correct": True,
                "rationale": (
                    "Correct. Identifying and researching the malware (step 1) is the "
                    "first action — you must understand what you're dealing with before "
                    "taking action."
                ),
            },
            {
                "id": "d",
                "text": "Schedule recurring antivirus scans",
                "correct": False,
                "rationale": (
                    "Incorrect. Scheduling scans (step 5) occurs AFTER remediation "
                    "(step 4), not before it."
                ),
            },
        ],
        "explanation": (
            "The seven CompTIA malware removal steps in order: "
            "(1) Investigate/identify & research malware symptoms, "
            "(2) Quarantine infected systems, "
            "(3) Disable System Restore / create restore point, "
            "(4) Remediate (scan and remove), "
            "(5) Schedule scans / update definitions, "
            "(6) Re-enable System Restore / new restore point, "
            "(7) Educate end user. "
            "Steps 1–3 all precede remediation."
        ),
    },
    {
        "id": "c2d2-038",
        "domain": 2,
        "objective": "2.6",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Windows security settings",
        "stem": (
            "A Windows 10 workstation needs to be hardened for a high-security environment. "
            "Which TWO of the following actions directly improve security against "
            "unauthorized access to data on the device if it is physically stolen? "
            "(Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Enable BitLocker full-disk encryption with a PIN pre-boot requirement",
                "correct": True,
                "rationale": (
                    "Correct. BitLocker encrypts the entire volume. Requiring a PIN at "
                    "pre-boot means even removing the drive and putting it in another "
                    "machine cannot read the data without the PIN and/or TPM."
                ),
            },
            {
                "id": "b",
                "text": "Enable EFS on folders containing sensitive documents",
                "correct": True,
                "rationale": (
                    "Correct. EFS encrypts files at the NTFS level tied to the user's "
                    "certificate. If the drive is stolen and connected to another machine, "
                    "the EFS-encrypted files cannot be read without the certificate."
                ),
            },
            {
                "id": "c",
                "text": "Create a complex password for the local administrator account",
                "correct": False,
                "rationale": (
                    "Incorrect. A complex password protects against online login but does "
                    "not protect data if the drive is physically removed and accessed "
                    "outside the OS environment. Encryption is needed for that threat."
                ),
            },
            {
                "id": "d",
                "text": "Enable Windows Defender Firewall for all network profiles",
                "correct": False,
                "rationale": (
                    "Incorrect. Windows Firewall protects against network-based attacks. "
                    "It provides no protection when the device is stolen and the drive "
                    "accessed outside the OS."
                ),
            },
        ],
        "explanation": (
            "Against the physical theft/drive-removal threat, encryption is the required "
            "control. BitLocker encrypts the entire volume; EFS encrypts specific files. "
            "Passwords and firewalls protect against online/network threats but not against "
            "offline physical access to the storage medium."
        ),
    },
    {
        "id": "c2d2-039",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Social engineering & attacks",
        "stem": (
            "A penetration tester is assessing a company's physical and digital security. "
            "Which THREE of the following actions represent social engineering attack "
            "techniques as defined by CompTIA A+? (Choose THREE.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Calling the help desk while impersonating the CEO and requesting an emergency password reset",
                "correct": True,
                "rationale": (
                    "Correct. This is vishing combined with impersonation — using a phone "
                    "call and a false identity to manipulate staff into taking a security-relevant "
                    "action."
                ),
            },
            {
                "id": "b",
                "text": "Following an employee through a badge-controlled door without using a badge",
                "correct": True,
                "rationale": (
                    "Correct. This is tailgating — a social engineering physical attack "
                    "that exploits politeness or inattention to bypass physical access "
                    "controls."
                ),
            },
            {
                "id": "c",
                "text": "Sending mass emails purporting to be from IT asking all employees to reset their passwords via a link",
                "correct": True,
                "rationale": (
                    "Correct. This is phishing — a social engineering attack delivered via "
                    "email that deceives recipients into taking an action that compromises "
                    "their credentials."
                ),
            },
            {
                "id": "d",
                "text": "Running a port scan against the company's web servers to identify open services",
                "correct": False,
                "rationale": (
                    "Incorrect. A port scan is a technical reconnaissance activity, not a "
                    "social engineering attack. Social engineering manipulates people, not "
                    "systems directly."
                ),
            },
        ],
        "explanation": (
            "Social engineering exploits human psychology rather than technical "
            "vulnerabilities. CompTIA A+ identifies: phishing (email deception), vishing "
            "(voice deception), impersonation (false identity), tailgating (physical "
            "access exploitation), shoulder surfing, dumpster diving, and evil twin. "
            "Port scanning is a technical, not social, attack."
        ),
    },
    {
        "id": "c2d2-040",
        "domain": 2,
        "objective": "2.9",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "SOHO network security",
        "stem": (
            "A small business owner asks a technician to harden their SOHO wireless "
            "network. Which TWO of the following are wireless-specific security "
            "configurations the technician should apply? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Disable SSID broadcast to prevent the network name from appearing in wireless scans",
                "correct": True,
                "rationale": (
                    "Correct. Disabling SSID broadcast is a wireless-specific hardening "
                    "step. While not a strong control (SSIDs can be discovered through "
                    "passive monitoring of association frames), it is a CompTIA-listed "
                    "wireless security configuration."
                ),
            },
            {
                "id": "b",
                "text": "Configure WPA3 or WPA2 encryption with AES (not TKIP)",
                "correct": True,
                "rationale": (
                    "Correct. Setting strong wireless encryption (WPA2/WPA3 with AES) "
                    "is a fundamental wireless-specific security requirement. TKIP is "
                    "deprecated and should not be used."
                ),
            },
            {
                "id": "c",
                "text": "Enable UPnP for automatic port management",
                "correct": False,
                "rationale": (
                    "Incorrect. UPnP is a security risk because it allows devices to "
                    "automatically open ports without administrator awareness. It should "
                    "be disabled, not enabled, as a hardening step."
                ),
            },
            {
                "id": "d",
                "text": "Assign the router a static WAN IP address",
                "correct": False,
                "rationale": (
                    "Incorrect. A static WAN IP is useful for hosting services but is not "
                    "a wireless-specific security configuration — it is a WAN connectivity "
                    "setting applicable to any router regardless of wireless."
                ),
            },
        ],
        "explanation": (
            "Wireless-specific SOHO hardening includes: change SSID from default, disable "
            "SSID broadcast, use WPA2/WPA3 with AES encryption, disable guest network if "
            "not needed, and set channel appropriately. UPnP and static WAN IP are not "
            "wireless-specific controls."
        ),
    },
    {
        "id": "c2d2-041",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Logical security & Active Directory",
        "stem": (
            "An organization is implementing MFA. Which TWO of the following represent "
            "authentication factors from DIFFERENT factor categories, satisfying MFA "
            "requirements? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "A password (something you know) and a fingerprint scan (something you are)",
                "correct": True,
                "rationale": (
                    "Correct. Password = knowledge factor; fingerprint = inherence (biometric) "
                    "factor. These are two distinct MFA categories."
                ),
            },
            {
                "id": "b",
                "text": "A smart card (something you have) and a PIN (something you know)",
                "correct": True,
                "rationale": (
                    "Correct. Smart card = possession factor; PIN = knowledge factor. "
                    "Two distinct categories — this is how smart card + PIN authentication "
                    "satisfies MFA."
                ),
            },
            {
                "id": "c",
                "text": "A password and a security question answer (both something you know)",
                "correct": False,
                "rationale": (
                    "Incorrect. Both a password and a security question answer are knowledge "
                    "factors. Using two factors from the same category is not MFA — it is "
                    "two-step verification within a single factor category."
                ),
            },
            {
                "id": "d",
                "text": "An SMS code and a TOTP authenticator code (both something you have)",
                "correct": False,
                "rationale": (
                    "Incorrect. Both SMS codes and TOTP codes are possession factors "
                    "(delivered to or generated by something you have — a phone). Using "
                    "two possession factors does not satisfy the multi-factor requirement "
                    "of different categories."
                ),
            },
        ],
        "explanation": (
            "MFA requires authentication from two or more DIFFERENT factor categories: "
            "knowledge (something you know), possession (something you have), and inherence "
            "(something you are/biometrics). Using two factors from the same category "
            "(e.g., two passwords) does not constitute true MFA."
        ),
    },
    {
        "id": "c2d2-042",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Physical security",
        "stem": (
            "A new office building is being planned. The security architect must implement "
            "controls to protect staff in the parking area at night. Which TWO of the "
            "following physical security measures specifically address personal safety "
            "in that environment? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Adequate lighting throughout the parking area",
                "correct": True,
                "rationale": (
                    "Correct. Lighting is a CompTIA-listed physical security control for "
                    "staff safety. Adequate lighting deters criminal activity and improves "
                    "visibility for both staff and surveillance cameras in the parking area."
                ),
            },
            {
                "id": "b",
                "text": "Video surveillance cameras with coverage of the parking area",
                "correct": True,
                "rationale": (
                    "Correct. Video surveillance is a physical security control that "
                    "deters and records incidents in the parking area, providing both "
                    "deterrence and evidentiary capability for staff safety incidents."
                ),
            },
            {
                "id": "c",
                "text": "Installing bollards around the office building entrance",
                "correct": False,
                "rationale": (
                    "Incorrect. Bollards protect against vehicle ramming of the building "
                    "structure. While valuable, they address structural security, not "
                    "personal safety for staff in the parking area specifically."
                ),
            },
            {
                "id": "d",
                "text": "Implementing an access control vestibule at the main building entrance",
                "correct": False,
                "rationale": (
                    "Incorrect. An access control vestibule controls building entry and "
                    "prevents tailgating into the facility. It does not address safety "
                    "risks in the outdoor parking area."
                ),
            },
        ],
        "explanation": (
            "CompTIA A+ 2.1 lists lighting and video surveillance as physical security "
            "controls relevant to staff safety. Lighting deters criminal activity and aids "
            "camera effectiveness. Cameras provide deterrence and recording for parking lot "
            "safety incidents. Bollards and vestibules address different threat vectors."
        ),
    },
    # ── Additional Single-Answer Questions ─────────────────────────────────────
    {
        "id": "c2d2-043",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Wireless security protocols",
        "stem": (
            "A network administrator is configuring a RADIUS server for WPA2-Enterprise. "
            "The admin must choose between RADIUS and TACACS+. Which statement BEST "
            "differentiates RADIUS from TACACS+ in the context of wireless authentication?"
        ),
        "options": [
            {
                "id": "a",
                "text": "RADIUS is the standard for 802.1X wireless client authentication; TACACS+ is primarily used for network device (router/switch) administrative access control",
                "correct": True,
                "rationale": (
                    "Correct. RADIUS (RFC 2865) is the protocol used by 802.1X for "
                    "end-user wireless authentication. TACACS+ (Cisco proprietary, now "
                    "RFC 8907) is designed for device administration AAA — controlling "
                    "who can log into routers and switches to manage them."
                ),
            },
            {
                "id": "b",
                "text": "TACACS+ encrypts only the password; RADIUS encrypts the entire packet",
                "correct": False,
                "rationale": (
                    "Incorrect. This is actually reversed: RADIUS encrypts only the "
                    "password field; TACACS+ encrypts the entire packet body. However, "
                    "this nuance about encryption scope does not answer the wireless "
                    "authentication use case question."
                ),
            },
            {
                "id": "c",
                "text": "RADIUS uses TCP port 49; TACACS+ uses UDP ports 1812/1813",
                "correct": False,
                "rationale": (
                    "Incorrect. The ports are reversed: TACACS+ uses TCP port 49; RADIUS "
                    "uses UDP ports 1812 (authentication) and 1813 (accounting). Also, "
                    "port numbers don't answer the use-case differentiation question."
                ),
            },
            {
                "id": "d",
                "text": "Both RADIUS and TACACS+ are interchangeable for 802.1X wireless authentication",
                "correct": False,
                "rationale": (
                    "Incorrect. They are not interchangeable. While technically TACACS+ "
                    "could authenticate users, 802.1X infrastructure and access points "
                    "are designed and tested to work with RADIUS. TACACS+ is the "
                    "device administration protocol."
                ),
            },
        ],
        "explanation": (
            "RADIUS: UDP 1812/1813, encrypts only password, standard for 802.1X/wireless "
            "end-user authentication. TACACS+: TCP 49, encrypts entire body, used for "
            "network device (CLI) administrative authentication and command authorization. "
            "For WPA2-Enterprise wireless, RADIUS is correct."
        ),
    },
    {
        "id": "c2d2-044",
        "domain": 2,
        "objective": "2.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile/embedded device security",
        "stem": (
            "A technician is reviewing mobile device security policies. The policy states "
            "that after five consecutive failed unlock attempts, the device should "
            "automatically perform a factory reset. Which security feature implements "
            "this behavior on a managed mobile device?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Failed login attempt threshold with remote/automatic wipe enforced via MDM policy",
                "correct": True,
                "rationale": (
                    "Correct. MDM policies can enforce a maximum failed-attempt threshold "
                    "after which the device automatically wipes/factory resets. This "
                    "combines the screen lock feature with an automatic wipe policy to "
                    "protect against brute-force unlock attempts."
                ),
            },
            {
                "id": "b",
                "text": "Screen lock with a biometric fingerprint only",
                "correct": False,
                "rationale": (
                    "Incorrect. A biometric screen lock prevents unauthorized access but "
                    "does not define what happens after repeated failures. Biometrics "
                    "alone don't trigger automated wipes without a configured policy."
                ),
            },
            {
                "id": "c",
                "text": "Device encryption with AES-256",
                "correct": False,
                "rationale": (
                    "Incorrect. Device encryption protects data at rest but has no bearing "
                    "on failed unlock attempt handling or automatic reset behavior."
                ),
            },
            {
                "id": "d",
                "text": "Locator app with GPS tracking enabled",
                "correct": False,
                "rationale": (
                    "Incorrect. A locator app tracks the device's geographic location. "
                    "It does not enforce failed-attempt thresholds or trigger factory resets."
                ),
            },
        ],
        "explanation": (
            "MDM platforms (such as Microsoft Intune, Jamf, VMware Workspace ONE) can "
            "enforce a device compliance policy that specifies the maximum number of "
            "failed PIN/password unlock attempts before an automatic factory reset (wipe) "
            "is triggered. This is distinct from a manual remote wipe — it happens "
            "autonomously on the device based on the policy threshold."
        ),
    },
]

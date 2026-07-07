"""
CompTIA A+ Core 2 (220-1202) — Domain 2: Security
Study notes following Professor Messer's 220-1202 playlist order.
"""

NOTES = [
    {
        "domain": 2,
        "topic": "Physical security",
        "objective": "2.1",
        "video": "Physical Security",
        "study_topics": ["Physical security"],
        "body": (
            "<p>Physical security is the first line of defense against unauthorized access to "
            "systems and data. No software control matters if an attacker can walk up to a server.</p>"
            "<h4>Access Control Mechanisms</h4>"
            "<ul>"
            "<li><strong>Mantraps (access control vestibules):</strong> Double-door entry system; "
            "only one door opens at a time, trapping intruders between doors.</li>"
            "<li><strong>Badge readers / smart cards:</strong> Proximity or contact cards authenticate "
            "users before granting physical access.</li>"
            "<li><strong>Biometrics:</strong> Fingerprint, retina scan, facial recognition — something "
            "you are. Difficult to forge but can have false positive/negative rates.</li>"
            "<li><strong>Key fobs / hardware tokens:</strong> One-time password (OTP) generators used "
            "with PIN for two-factor physical + logical access.</li>"
            "<li><strong>Locks:</strong> Cable locks secure laptops; server racks use keyed locks; "
            "cipher locks use keypad codes.</li>"
            "</ul>"
            "<h4>Surveillance &amp; Detection</h4>"
            "<ul>"
            "<li><strong>CCTV:</strong> Closed-circuit TV for monitoring and recording. Deterrent "
            "and forensic evidence.</li>"
            "<li><strong>Motion sensors:</strong> Infrared or microwave detection for after-hours "
            "alerting.</li>"
            "<li><strong>Guards:</strong> Human deterrent; can respond to alarms.</li>"
            "<li><strong>Lighting:</strong> Proper illumination deters intruders and improves camera "
            "effectiveness.</li>"
            "</ul>"
            "<h4>Equipment Protection</h4>"
            "<ul>"
            "<li><strong>Faraday cage:</strong> Metal enclosure that blocks electromagnetic signals, "
            "preventing wireless eavesdropping or EMP damage.</li>"
            "<li><strong>Safe:</strong> Protects portable media and documents.</li>"
            "<li><strong>USB data blocker:</strong> Allows charging only — blocks data pins to prevent "
            "juice jacking.</li>"
            "</ul>"
        ),
        "key_points": [
            "Mantrap (access control vestibule) keeps one door locked until the other closes.",
            "Biometrics = something you ARE; tokens = something you HAVE.",
            "USB data blockers prevent juice-jacking at public charging stations.",
            "Faraday cages block all RF signals — used in forensic labs and SCIF rooms.",
            "CCTV provides deterrence AND forensic evidence after an incident.",
        ],
    },
    {
        "domain": 2,
        "topic": "Logical security & Active Directory",
        "objective": "2.2",
        "video": "Logical Security",
        "study_topics": ["Logical security & Active Directory"],
        "body": (
            "<p>Logical security controls protect systems and data through software-enforced policies "
            "rather than physical barriers.</p>"
            "<h4>Active Directory (AD)</h4>"
            "<ul>"
            "<li><strong>Domain:</strong> Central authentication database managed by a Domain "
            "Controller (DC). Users log in once and access all authorized network resources "
            "(Single Sign-On).</li>"
            "<li><strong>Group Policy Objects (GPO):</strong> Applied to OUs, sites, or the entire "
            "domain to enforce settings — password policy, desktop lockdown, software deployment.</li>"
            "<li><strong>Organizational Units (OU):</strong> Logical containers within AD for grouping "
            "users, computers, and groups; GPOs are linked to OUs.</li>"
            "<li><strong>Security groups:</strong> Used to assign permissions to shared resources. "
            "Users inherit permissions from group membership.</li>"
            "</ul>"
            "<h4>Authentication Factors</h4>"
            "<table border='1' cellpadding='4'>"
            "<tr><th>Factor</th><th>Type</th><th>Example</th></tr>"
            "<tr><td>Something you know</td><td>Knowledge</td><td>Password, PIN</td></tr>"
            "<tr><td>Something you have</td><td>Possession</td><td>Smart card, OTP token</td></tr>"
            "<tr><td>Something you are</td><td>Inherence</td><td>Fingerprint, retina</td></tr>"
            "<tr><td>Somewhere you are</td><td>Location</td><td>GPS geofencing</td></tr>"
            "</table>"
            "<h4>Access Control Models</h4>"
            "<ul>"
            "<li><strong>DAC (Discretionary):</strong> Owner controls permissions — standard Windows "
            "NTFS model.</li>"
            "<li><strong>MAC (Mandatory):</strong> OS enforces labels (Top Secret, Secret); used in "
            "government/military.</li>"
            "<li><strong>RBAC (Role-Based):</strong> Permissions assigned to roles, users assigned to "
            "roles — common in enterprise.</li>"
            "</ul>"
            "<h4>Other Logical Controls</h4>"
            "<ul>"
            "<li><strong>Principle of least privilege:</strong> Grant only the minimum access needed.</li>"
            "<li><strong>Account lockout policy:</strong> Locks account after N failed login attempts.</li>"
            "<li><strong>Software-based MDM:</strong> Enforces policies on mobile devices.</li>"
            "</ul>"
        ),
        "key_points": [
            "AD Domain Controller centralizes authentication; GPOs enforce policy.",
            "MFA combines two or more different factors (not two of the same type).",
            "DAC = owner decides; MAC = OS/labels decide; RBAC = roles decide.",
            "Least privilege minimizes the blast radius of a compromised account.",
            "GPOs can push settings, install software, and restrict Control Panel access.",
        ],
    },
    {
        "domain": 2,
        "topic": "Wireless security protocols",
        "objective": "2.3",
        "video": "Wireless Security",
        "study_topics": ["Wireless security protocols"],
        "body": (
            "<p>Wireless networks are inherently broadcast-based, so strong encryption and "
            "authentication protocols are essential.</p>"
            "<h4>Protocol Comparison</h4>"
            "<table border='1' cellpadding='4'>"
            "<tr><th>Protocol</th><th>Encryption</th><th>Key Length</th><th>Notes</th></tr>"
            "<tr><td>WEP</td><td>RC4</td><td>40/104-bit</td><td>Broken — do NOT use</td></tr>"
            "<tr><td>WPA (TKIP)</td><td>RC4 + TKIP</td><td>128-bit</td><td>Deprecated, vulnerable</td></tr>"
            "<tr><td>WPA2</td><td>AES-CCMP</td><td>128-bit</td><td>Current standard; CCMP = strong</td></tr>"
            "<tr><td>WPA3</td><td>AES-GCMP / SAE</td><td>128/192-bit</td><td>SAE replaces PSK handshake</td></tr>"
            "</table>"
            "<h4>WPA2 vs WPA3 Key Differences</h4>"
            "<ul>"
            "<li><strong>WPA2 Personal:</strong> Pre-shared key (PSK). Vulnerable to offline dictionary "
            "attacks if handshake is captured.</li>"
            "<li><strong>WPA3 Personal:</strong> Simultaneous Authentication of Equals (SAE) — "
            "Dragonfly handshake provides forward secrecy; resistant to offline attacks.</li>"
            "<li><strong>WPA2/WPA3 Enterprise:</strong> Uses 802.1X with a RADIUS server for "
            "individual user authentication; no shared key.</li>"
            "</ul>"
            "<h4>Enterprise Authentication Servers</h4>"
            "<ul>"
            "<li><strong>RADIUS:</strong> Remote Authentication Dial-In User Service. UDP-based "
            "(ports 1812/1813). Encrypts only the password field in the packet.</li>"
            "<li><strong>TACACS+:</strong> Cisco proprietary. TCP-based (port 49). Encrypts the "
            "entire authentication payload. Separates Authentication, Authorization, Accounting (AAA).</li>"
            "<li><strong>802.1X:</strong> Port-based Network Access Control (NAC). Supplicant → "
            "Authenticator → Authentication Server flow.</li>"
            "</ul>"
            "<h4>Other Wireless Security Concepts</h4>"
            "<ul>"
            "<li><strong>SSID hiding:</strong> Security through obscurity — not effective alone.</li>"
            "<li><strong>MAC filtering:</strong> Easily spoofed; minor deterrent only.</li>"
            "<li><strong>Captive portal:</strong> Redirects unauthenticated guests to a login page.</li>"
            "<li><strong>WPS vulnerabilities:</strong> PIN brute-force (Reaver attack). Disable WPS.</li>"
            "</ul>"
        ),
        "key_points": [
            "WEP is broken — crackable in minutes. Never use it.",
            "WPA2 uses AES-CCMP; WPA uses deprecated RC4/TKIP.",
            "WPA3 SAE (Dragonfly) prevents offline dictionary attacks and provides forward secrecy.",
            "RADIUS uses UDP and encrypts only the password; TACACS+ uses TCP and encrypts everything.",
            "802.1X = port-based NAC; requires supplicant, authenticator, and auth server.",
            "Disable WPS — the 8-digit PIN is brute-forceable.",
        ],
    },
    {
        "domain": 2,
        "topic": "Malware types & removal",
        "objective": "2.4",
        "video": "Malware",
        "study_topics": ["Malware types & removal"],
        "body": (
            "<p>Malware (malicious software) is any program designed to damage, disrupt, or gain "
            "unauthorized access to a system.</p>"
            "<h4>Common Malware Types</h4>"
            "<ul>"
            "<li><strong>Virus:</strong> Attaches to a legitimate file; requires user action to "
            "spread. Boot sector viruses infect the MBR.</li>"
            "<li><strong>Worm:</strong> Self-replicates across networks without user interaction. "
            "Consumes bandwidth.</li>"
            "<li><strong>Trojan:</strong> Disguised as legitimate software. Creates backdoors for "
            "attackers. RAT (Remote Access Trojan) provides full remote control.</li>"
            "<li><strong>Ransomware:</strong> Encrypts files and demands payment for the decryption "
            "key. Backup offline to recover.</li>"
            "<li><strong>Spyware:</strong> Silently monitors user activity and sends data to attacker.</li>"
            "<li><strong>Adware:</strong> Displays unwanted ads; often bundled with free software.</li>"
            "<li><strong>Rootkit:</strong> Hides itself and other malware at the OS or kernel level. "
            "Very difficult to detect — may require offline scan or OS reinstall.</li>"
            "<li><strong>Keylogger:</strong> Records keystrokes to capture passwords and sensitive data.</li>"
            "<li><strong>Botnet / Bot:</strong> Compromised machine (zombie) controlled by a C2 "
            "server; used for DDoS, spam, crypto-mining.</li>"
            "<li><strong>Cryptominer:</strong> Uses victim's CPU/GPU resources to mine cryptocurrency.</li>"
            "<li><strong>Fileless malware:</strong> Lives in memory (PowerShell, WMI); no file written "
            "to disk, evades traditional AV.</li>"
            "</ul>"
            "<h4>Malware Removal — 7-Step Process</h4>"
            "<ol>"
            "<li><strong>Investigate and verify</strong> malware symptoms (pop-ups, slow performance, "
            "unknown processes).</li>"
            "<li><strong>Quarantine</strong> the infected system — disconnect from the network to "
            "prevent spread.</li>"
            "<li><strong>Disable System Restore</strong> (Windows) — prevents malware from hiding in "
            "restore points.</li>"
            "<li><strong>Remediate</strong> — update AV definitions and run a full scan in Safe Mode; "
            "use multiple scanners (Malwarebytes + AV).</li>"
            "<li><strong>Schedule scans and run updates</strong> — ensure OS and AV are fully patched.</li>"
            "<li><strong>Enable System Restore and create a restore point</strong> — creates a clean "
            "baseline post-cleanup.</li>"
            "<li><strong>Educate the end user</strong> — explain how the infection occurred and how "
            "to avoid recurrence.</li>"
            "</ol>"
        ),
        "key_points": [
            "Virus needs user action to spread; worm self-replicates automatically.",
            "Rootkits hide at kernel level — may require bootable offline scanner or OS reinstall.",
            "Ransomware recovery requires offline backups — never pay if you can restore.",
            "7-step removal: Investigate → Quarantine → Disable SR → Remediate → Update → Re-enable SR → Educate.",
            "Fileless malware runs in memory (PowerShell/WMI), leaving no file on disk.",
            "Botnets turn compromised machines into C2-controlled zombies for DDoS or spam.",
        ],
    },
    {
        "domain": 2,
        "topic": "Social engineering & attacks",
        "objective": "2.5",
        "video": "Social Engineering",
        "study_topics": ["Social engineering & attacks"],
        "body": (
            "<p>Social engineering exploits human psychology rather than technical vulnerabilities to "
            "gain unauthorized access or information.</p>"
            "<h4>Phishing Variants</h4>"
            "<ul>"
            "<li><strong>Phishing:</strong> Mass email campaign impersonating a legitimate entity to "
            "steal credentials or deliver malware.</li>"
            "<li><strong>Spear phishing:</strong> Targeted phishing customized for a specific person "
            "or organization using personal details.</li>"
            "<li><strong>Whaling:</strong> Spear phishing targeting senior executives (CEO, CFO) — "
            "high-value targets.</li>"
            "<li><strong>Vishing:</strong> Voice phishing — phone calls pretending to be bank, IRS, "
            "or IT support to extract information.</li>"
            "<li><strong>Smishing:</strong> SMS phishing — malicious links sent via text message.</li>"
            "</ul>"
            "<h4>In-Person &amp; Physical Attacks</h4>"
            "<ul>"
            "<li><strong>Tailgating / Piggybacking:</strong> Following an authorized person through a "
            "secured door without badging in. Mantraps and employee training mitigate this.</li>"
            "<li><strong>Shoulder surfing:</strong> Observing a user's screen or keyboard to capture "
            "PINs or passwords. Privacy screens mitigate.</li>"
            "<li><strong>Dumpster diving:</strong> Retrieving discarded documents, drives, or hardware "
            "to find sensitive data. Mitigation: shred documents, degauss/wipe drives.</li>"
            "<li><strong>Impersonation:</strong> Pretending to be IT support, a vendor, or a new "
            "employee to gain access.</li>"
            "</ul>"
            "<h4>Technical Social Engineering</h4>"
            "<ul>"
            "<li><strong>Evil twin:</strong> Rogue Wi-Fi access point with the same SSID as a "
            "legitimate network, capturing all traffic. Always verify network authenticity; use VPN.</li>"
            "<li><strong>Man-in-the-middle (MITM):</strong> Attacker secretly intercepts and relays "
            "communications between two parties.</li>"
            "<li><strong>Pretexting:</strong> Creating a fabricated scenario (pretext) to manipulate "
            "a victim into divulging information.</li>"
            "</ul>"
            "<h4>Mitigation Strategies</h4>"
            "<ul>"
            "<li>Security awareness training — users are the last line of defense.</li>"
            "<li>Verify caller identity before providing any information.</li>"
            "<li>Enforce a clean-desk policy and document shredding.</li>"
            "<li>Use MFA so stolen credentials alone are insufficient.</li>"
            "</ul>"
        ),
        "key_points": [
            "Whaling = spear phishing targeting executives (CEO/CFO).",
            "Vishing = voice phishing; smishing = SMS phishing.",
            "Evil twin creates a rogue AP matching a legitimate SSID — use VPNs on public Wi-Fi.",
            "Tailgating bypasses physical access controls — mantraps and training are countermeasures.",
            "Dumpster diving: shred all documents; wipe/degauss all storage media before disposal.",
            "Pretexting = fabricating a believable backstory to manipulate the victim.",
        ],
    },
    {
        "domain": 2,
        "topic": "Windows security settings",
        "objective": "2.6",
        "video": "Windows Security Settings",
        "study_topics": ["Windows security settings"],
        "body": (
            "<p>Windows provides a layered set of built-in security tools accessible from the Control "
            "Panel, Settings app, and administrative consoles.</p>"
            "<h4>User Account Control (UAC)</h4>"
            "<p>UAC prompts for elevation when administrative actions are requested. Prevents malware "
            "from silently gaining admin rights. Settings range from 'Always notify' to 'Never notify' "
            "(disabled). Standard users receive a credential prompt; admins see a consent prompt.</p>"
            "<h4>Windows Defender &amp; Windows Security</h4>"
            "<ul>"
            "<li><strong>Windows Defender Antivirus:</strong> Real-time protection, scheduled scans, "
            "cloud-delivered protection.</li>"
            "<li><strong>Windows Defender Firewall:</strong> Host-based firewall with inbound/outbound "
            "rules per network profile (Domain, Private, Public).</li>"
            "<li><strong>Windows Security Center:</strong> Unified dashboard for AV, firewall, "
            "SmartScreen, and device health.</li>"
            "</ul>"
            "<h4>Local Security Policy &amp; Group Policy</h4>"
            "<ul>"
            "<li><strong>secpol.msc:</strong> Local Security Policy — password complexity, account "
            "lockout, audit policy, user rights.</li>"
            "<li><strong>gpedit.msc:</strong> Local Group Policy Editor — broader set of computer and "
            "user configuration options.</li>"
            "<li><strong>Password policy:</strong> Minimum length, complexity, history, maximum age.</li>"
            "<li><strong>Account lockout:</strong> Lockout threshold, duration, and reset counter.</li>"
            "</ul>"
            "<h4>Windows Defender Credential Guard &amp; Device Guard</h4>"
            "<ul>"
            "<li><strong>Credential Guard:</strong> Uses virtualization-based security (VBS) to "
            "isolate and protect credential hashes from pass-the-hash attacks.</li>"
            "<li><strong>Device Guard:</strong> Enforces code integrity policy — only signed, trusted "
            "code can run.</li>"
            "</ul>"
            "<h4>Other Key Settings</h4>"
            "<ul>"
            "<li><strong>Screen lock / timeout:</strong> Auto-lock after inactivity (Win+L to lock "
            "immediately).</li>"
            "<li><strong>Secure Boot:</strong> UEFI feature verifying bootloader signatures before "
            "loading the OS.</li>"
            "<li><strong>SmartScreen:</strong> Warns about unrecognized apps and malicious websites.</li>"
            "</ul>"
        ),
        "key_points": [
            "UAC separates standard user and admin tokens — prevents silent privilege escalation.",
            "secpol.msc sets password policy, account lockout, and audit settings locally.",
            "Windows Defender Firewall has three profiles: Domain, Private, and Public.",
            "Credential Guard uses VBS to protect NTLM hashes from pass-the-hash attacks.",
            "Secure Boot (UEFI) verifies bootloader signatures to block rootkits at boot.",
            "SmartScreen filters warn users about unrecognized downloads and phishing sites.",
        ],
    },
    {
        "domain": 2,
        "topic": "NTFS vs share permissions",
        "objective": "2.6",
        "video": "Windows Security Settings",
        "study_topics": ["NTFS vs share permissions"],
        "body": (
            "<p>Windows uses two separate permission systems: NTFS permissions (applied to the file "
            "system) and Share permissions (applied to network shares). Understanding how they "
            "interact is critical for the exam.</p>"
            "<h4>Share Permissions</h4>"
            "<p>Set via the Sharing tab. Apply <em>only</em> when a resource is accessed over the "
            "network. Three levels: <strong>Read</strong>, <strong>Change</strong>, and "
            "<strong>Full Control</strong>. Completely bypassed for local access.</p>"
            "<h4>NTFS Permissions</h4>"
            "<p>Set via the Security tab. Apply to <em>both local and network access</em>. Granular "
            "permissions: Full Control, Modify, Read &amp; Execute, List Folder Contents, Read, "
            "Write. Can be set on individual files as well as folders.</p>"
            "<h4>How Permissions Combine Over the Network</h4>"
            "<p>When a user connects over the network, Windows evaluates <em>both</em> permission "
            "sets and applies the <strong>more restrictive</strong> of the combined results:</p>"
            "<ol>"
            "<li>Calculate the user's <em>effective NTFS permissions</em> (union of all group NTFS "
            "permissions).</li>"
            "<li>Calculate the user's <em>effective Share permissions</em> (union of all group share "
            "permissions).</li>"
            "<li>The final effective access = intersection (most restrictive) of steps 1 and 2.</li>"
            "</ol>"
            "<p><strong>Example:</strong> NTFS = Full Control, Share = Read → effective network "
            "access = <strong>Read</strong>.</p>"
            "<h4>Explicit Deny</h4>"
            "<p>An explicit <strong>Deny</strong> overrides any Allow — even if the user is in "
            "another group that grants access. Deny should be used sparingly and only when "
            "intentional.</p>"
            "<h4>Inheritance</h4>"
            "<p>NTFS permissions are inherited from parent folders by default. Inheritance can be "
            "disabled (broken) on a specific folder to set unique permissions.</p>"
            "<h4>Move vs. Copy Behavior</h4>"
            "<table border='1' cellpadding='4'>"
            "<tr><th>Operation</th><th>Same Volume</th><th>Different Volume</th></tr>"
            "<tr><td><strong>Copy</strong></td><td>Inherits destination permissions</td>"
            "<td>Inherits destination permissions</td></tr>"
            "<tr><td><strong>Move (same volume)</strong></td><td>Retains original NTFS permissions</td>"
            "<td>N/A</td></tr>"
            "<tr><td><strong>Move (cross-volume)</strong></td><td>N/A</td>"
            "<td>Inherits destination permissions (functionally a copy + delete)</td></tr>"
            "</table>"
            "<p>Key rule: <em>Copy always inherits. Move within same volume retains. Move across "
            "volumes inherits.</em></p>"
        ),
        "key_points": [
            "Share permissions apply ONLY over the network; NTFS permissions apply locally AND over the network.",
            "Over the network: the MORE RESTRICTIVE of combined Share and NTFS permissions wins.",
            "Effective NTFS = union of all group NTFS permissions; same for Share permissions.",
            "Explicit Deny overrides any Allow, regardless of other group memberships.",
            "Copy (same or cross-volume) → inherits destination NTFS permissions.",
            "Move within same volume → retains original NTFS permissions.",
            "Move across volumes → inherits destination NTFS permissions (treated as copy + delete).",
        ],
    },
    {
        "domain": 2,
        "topic": "BitLocker & encryption (EFS)",
        "objective": "2.7",
        "video": "Data Encryption",
        "study_topics": ["BitLocker & encryption (EFS)"],
        "body": (
            "<p>Windows provides two built-in file/disk encryption technologies: BitLocker for "
            "full-volume encryption and EFS for file-level encryption.</p>"
            "<h4>BitLocker Drive Encryption</h4>"
            "<ul>"
            "<li>Encrypts entire volumes (OS drive, data drives, removable drives via BitLocker To Go).</li>"
            "<li>Uses <strong>AES-128 or AES-256</strong> by default.</li>"
            "<li>Requires a <strong>TPM 1.2+</strong> chip to store the encryption key securely. "
            "Can also use a USB startup key or PIN as additional factors.</li>"
            "<li><strong>Recovery key:</strong> 48-digit numeric key stored in AD, Microsoft account, "
            "printed, or on USB — required if BitLocker can't authenticate at boot.</li>"
            "<li><strong>BitLocker To Go:</strong> Encrypts removable USB drives; readable on "
            "non-BitLocker systems with the password.</li>"
            "<li>Protects against data theft from a stolen laptop — attacker cannot read the drive "
            "by booting another OS.</li>"
            "</ul>"
            "<h4>TPM (Trusted Platform Module)</h4>"
            "<ul>"
            "<li>Hardware chip that stores cryptographic keys, certificates, and measurements.</li>"
            "<li>Validates the boot environment (PCR measurements) to detect tampering before "
            "releasing the BitLocker key.</li>"
            "<li>TPM 2.0 required for Windows 11.</li>"
            "</ul>"
            "<h4>EFS (Encrypting File System)</h4>"
            "<ul>"
            "<li>NTFS feature that encrypts individual files or folders at the file system level.</li>"
            "<li>Transparent to the owner — files open normally when logged in with the right account.</li>"
            "<li>Keys tied to the user's certificate/private key. If the profile is lost or "
            "certificate deleted, files are unrecoverable without a <strong>Data Recovery Agent "
            "(DRA)</strong>.</li>"
            "<li>EFS-encrypted files show in green in Windows Explorer.</li>"
            "<li>Limitation: EFS does not protect against theft of the running machine when the "
            "user is logged in.</li>"
            "</ul>"
            "<h4>BitLocker vs. EFS Comparison</h4>"
            "<table border='1' cellpadding='4'>"
            "<tr><th>Feature</th><th>BitLocker</th><th>EFS</th></tr>"
            "<tr><td>Scope</td><td>Entire volume</td><td>Individual files/folders</td></tr>"
            "<tr><td>Requires TPM</td><td>Recommended</td><td>No</td></tr>"
            "<tr><td>Works when OS is offline</td><td>Yes</td><td>No</td></tr>"
            "<tr><td>Key storage</td><td>TPM / recovery key</td><td>User certificate</td></tr>"
            "</table>"
        ),
        "key_points": [
            "BitLocker encrypts full volumes; EFS encrypts individual files/folders.",
            "BitLocker requires TPM to bind the key to the hardware platform.",
            "BitLocker recovery key is 48 digits — store in AD or Microsoft account.",
            "BitLocker To Go encrypts removable USB drives.",
            "EFS keys are tied to the user's certificate — losing the cert = losing the data without a DRA.",
            "EFS files appear green in Windows Explorer.",
            "TPM 2.0 is required for Windows 11.",
        ],
    },
    {
        "domain": 2,
        "topic": "Mobile/embedded device security",
        "objective": "2.8",
        "video": "Mobile Device Security",
        "study_topics": ["Mobile/embedded device security"],
        "body": (
            "<p>Mobile and embedded devices introduce unique security challenges due to portability, "
            "diverse OS ecosystems, and IoT integration.</p>"
            "<h4>Mobile Device Management (MDM)</h4>"
            "<ul>"
            "<li><strong>MDM / MAM:</strong> Mobile Device Management manages entire devices; Mobile "
            "Application Management manages only corporate apps on BYOD devices.</li>"
            "<li><strong>Enrollment:</strong> Device registers with the MDM server and receives a "
            "configuration profile (over-the-air provisioning).</li>"
            "<li><strong>Policies enforced:</strong> Screen lock, PIN/biometric requirements, "
            "encryption, app whitelist/blacklist, camera disable, remote wipe.</li>"
            "<li><strong>Remote wipe:</strong> MDM can factory reset a lost/stolen device; selective "
            "wipe removes only corporate data (BYOD friendly).</li>"
            "</ul>"
            "<h4>BYOD vs. COPE vs. CYOD</h4>"
            "<ul>"
            "<li><strong>BYOD (Bring Your Own Device):</strong> Employee uses personal device — "
            "lower cost, privacy concerns.</li>"
            "<li><strong>COPE (Corporate-Owned, Personally Enabled):</strong> Company owns device, "
            "allows personal use.</li>"
            "<li><strong>CYOD (Choose Your Own Device):</strong> Employee picks from an approved list.</li>"
            "</ul>"
            "<h4>Mobile Security Threats</h4>"
            "<ul>"
            "<li><strong>Rooting / Jailbreaking:</strong> Removes OS vendor restrictions. Voids "
            "warranty; bypasses security controls; increases malware risk.</li>"
            "<li><strong>Sideloading:</strong> Installing APKs outside the official app store — "
            "risk of malicious apps.</li>"
            "<li><strong>Shoulder surfing:</strong> Screen privacy filters mitigate.</li>"
            "<li><strong>Bluetooth threats:</strong> Bluejacking (unsolicited messages), Bluesnarfing "
            "(unauthorized data access). Keep Bluetooth non-discoverable when not in use.</li>"
            "</ul>"
            "<h4>Embedded / IoT Security</h4>"
            "<ul>"
            "<li>Default credentials must always be changed immediately.</li>"
            "<li>Firmware updates patch known vulnerabilities.</li>"
            "<li>Network segmentation: place IoT devices on an isolated VLAN.</li>"
            "<li>Disable unused ports, services, and protocols.</li>"
            "</ul>"
        ),
        "key_points": [
            "MDM enforces screen lock, encryption, remote wipe, and app policies on mobile devices.",
            "Remote wipe factory-resets a lost device; selective wipe removes only corporate data.",
            "Rooting/jailbreaking bypasses OS security controls and voids warranty.",
            "Bluesnarfing = unauthorized data theft via Bluetooth; keep BT non-discoverable when idle.",
            "IoT devices should use unique passwords, updated firmware, and a segmented VLAN.",
            "MAM manages only apps on BYOD devices without controlling the entire device.",
        ],
    },
    {
        "domain": 2,
        "topic": "Data destruction & disposal",
        "objective": "2.9",
        "video": "Data Destruction",
        "study_topics": ["Data destruction & disposal"],
        "body": (
            "<p>Proper data destruction ensures that sensitive information cannot be recovered from "
            "retired media. Method selection depends on media type and required assurance level.</p>"
            "<h4>Physical Destruction Methods</h4>"
            "<ul>"
            "<li><strong>Shredding:</strong> Industrial shredder reduces HDDs, optical media, and "
            "paper to small particles. Renders media completely unreadable.</li>"
            "<li><strong>Degaussing:</strong> Exposes magnetic media (HDDs, LTO tapes) to a powerful "
            "magnetic field, randomizing magnetic domains and destroying data. <em>Does NOT work on "
            "SSDs, flash, or optical media.</em></li>"
            "<li><strong>Incineration:</strong> Burning media at high temperature. Used for "
            "classified materials; requires documented chain of custody.</li>"
            "<li><strong>Drilling / Puncturing:</strong> Drilling through platters of HDDs or chips "
            "of SSDs. Quick physical method for small quantities.</li>"
            "</ul>"
            "<h4>Software-Based Methods</h4>"
            "<ul>"
            "<li><strong>Overwriting / Wiping:</strong> Writing random data (zeros, ones, or random "
            "patterns) over all sectors. DoD 5220.22-M standard specifies multiple passes. "
            "Effective for HDDs; less certain for SSDs due to wear-leveling.</li>"
            "<li><strong>Low-level format:</strong> Performed by the drive firmware; rewrites all "
            "sectors to factory state. More thorough than OS-level format.</li>"
            "<li><strong>Crypto-shredding:</strong> If data was encrypted, securely deleting the "
            "encryption key renders ciphertext unrecoverable without physical destruction.</li>"
            "</ul>"
            "<h4>Media-Specific Considerations</h4>"
            "<table border='1' cellpadding='4'>"
            "<tr><th>Media Type</th><th>Effective Methods</th></tr>"
            "<tr><td>HDD (magnetic)</td><td>Degauss, shred, overwrite, drill</td></tr>"
            "<tr><td>SSD / Flash</td><td>Crypto-shredding, shred, drill (degaussing ineffective)</td></tr>"
            "<tr><td>Optical (CD/DVD)</td><td>Shred, incinerate (degaussing ineffective)</td></tr>"
            "<tr><td>Paper</td><td>Cross-cut shred, incinerate</td></tr>"
            "</table>"
            "<h4>Certificate of Destruction</h4>"
            "<p>A formal document issued by a third-party destruction vendor confirming that "
            "specified media has been destroyed. Includes serial numbers, destruction method, date, "
            "and technician signature. Required for HIPAA, PCI-DSS, and other compliance frameworks. "
            "Essential for audit trails and legal defensibility.</p>"
        ),
        "key_points": [
            "Degaussing works ONLY on magnetic media (HDDs, tapes) — ineffective on SSDs and optical.",
            "Shredding and incineration are the most thorough physical destruction methods.",
            "Certificate of destruction provides legal proof of compliance for HIPAA, PCI-DSS, etc.",
            "Crypto-shredding: delete the encryption key to render encrypted data unrecoverable.",
            "Overwriting (DoD 5220.22-M) is effective for HDDs but unreliable for SSDs due to wear-leveling.",
            "Standard OS delete/format does NOT securely erase data — forensic tools can recover it.",
        ],
    },
    {
        "domain": 2,
        "topic": "SOHO network security",
        "objective": "2.10",
        "video": "SOHO Network Security",
        "study_topics": ["SOHO network security"],
        "body": (
            "<p>Small Office/Home Office (SOHO) networks require proper configuration to resist "
            "common attacks. The SOHO router/firewall is the primary perimeter control.</p>"
            "<h4>Router / Firewall Hardening</h4>"
            "<ul>"
            "<li><strong>Change default credentials:</strong> Default admin username/password is "
            "publicly known — change immediately on setup.</li>"
            "<li><strong>Firmware updates:</strong> Regularly update router firmware to patch "
            "known vulnerabilities.</li>"
            "<li><strong>Disable remote management:</strong> Turn off WAN-side admin access unless "
            "absolutely required. Use HTTPS if enabled.</li>"
            "<li><strong>Disable UPnP:</strong> Universal Plug and Play can automatically open "
            "firewall ports — a significant security risk in SOHO environments.</li>"
            "<li><strong>Firewall rules:</strong> Implicit deny all inbound by default. Allow only "
            "required ports/services (principle of least access).</li>"
            "</ul>"
            "<h4>Network Segmentation</h4>"
            "<ul>"
            "<li><strong>Guest network / VLAN:</strong> Isolate guest users and IoT devices from "
            "the main corporate/private network. Guests can reach the internet but not internal "
            "resources.</li>"
            "<li><strong>DMZ:</strong> Demilitarized Zone hosts public-facing servers (web, email) "
            "between two firewalls; compromise of the DMZ host doesn't expose the internal network.</li>"
            "</ul>"
            "<h4>SOHO Wireless Security</h4>"
            "<ul>"
            "<li>Use WPA3 (or WPA2-AES minimum) — never WEP or WPA-TKIP.</li>"
            "<li>Strong, unique Wi-Fi passphrase (12+ characters, mixed character types).</li>"
            "<li>Disable WPS — vulnerable to brute-force PIN attack.</li>"
            "<li>Consider MAC filtering as a minor additional deterrent (easily bypassed by spoofing).</li>"
            "</ul>"
            "<h4>Content Filtering &amp; Parental Controls</h4>"
            "<ul>"
            "<li><strong>Content filtering:</strong> Blocks categories of websites (adult, gambling, "
            "known malware domains) at the router or DNS level (e.g., DNS-based filtering with "
            "Cisco Umbrella or Pi-hole).</li>"
            "<li><strong>Parental controls:</strong> Schedule-based and category-based restrictions "
            "on specific devices or all clients.</li>"
            "</ul>"
            "<h4>Port Forwarding vs. DMZ Host</h4>"
            "<p><strong>Port forwarding</strong> maps specific external ports to an internal IP — "
            "surgical and preferred. <strong>DMZ host</strong> forwards ALL ports to one internal "
            "device — convenient but exposes that device completely; avoid unless necessary.</p>"
        ),
        "key_points": [
            "Always change default router credentials — default passwords are publicly documented.",
            "Disable UPnP and WPS on SOHO routers — both create automatic security holes.",
            "Guest VLAN isolates IoT and visitor traffic from the primary internal network.",
            "DMZ hosts public-facing servers between two firewalls, limiting internal exposure.",
            "Port forwarding is preferred over DMZ host — DMZ host exposes ALL ports.",
            "Content filtering at DNS level (Pi-hole, Umbrella) blocks malware domains network-wide.",
        ],
    },
    {
        "domain": 2,
        "topic": "Browser security",
        "objective": "2.11",
        "video": "Browser Security",
        "study_topics": ["Browser security"],
        "body": (
            "<p>Web browsers are the primary interface to the internet and a major attack surface. "
            "Proper browser configuration reduces the risk of drive-by downloads, tracking, and "
            "credential theft.</p>"
            "<h4>Browser Hardening Settings</h4>"
            "<ul>"
            "<li><strong>Keep browser updated:</strong> Browser vendors release frequent security "
            "patches. Enable automatic updates.</li>"
            "<li><strong>Extensions / Plug-ins:</strong> Remove unnecessary extensions — each adds "
            "attack surface. Use only well-known extensions from official stores.</li>"
            "<li><strong>Pop-up blocker:</strong> Prevents malicious pop-ups and click-jacking.</li>"
            "<li><strong>Ad blocker:</strong> Blocks malvertising (malicious advertising).</li>"
            "<li><strong>Password manager:</strong> Avoids password reuse; resistant to keyloggers "
            "on phishing sites (autofill won't fill wrong domain).</li>"
            "</ul>"
            "<h4>HTTPS and Certificate Validation</h4>"
            "<ul>"
            "<li><strong>HTTPS (TLS):</strong> Encrypts traffic between browser and server; "
            "authenticates the server via a certificate. Look for the padlock icon.</li>"
            "<li><strong>Certificate errors:</strong> Expired, self-signed, or mismatched "
            "certificates should never be clicked through — possible MITM attack.</li>"
            "<li><strong>HSTS (HTTP Strict Transport Security):</strong> Server instructs browser "
            "to only connect via HTTPS for a defined period; prevents downgrade attacks.</li>"
            "</ul>"
            "<h4>Cookies and Tracking</h4>"
            "<ul>"
            "<li><strong>Session cookies:</strong> Expire when browser closes; hold session tokens.</li>"
            "<li><strong>Persistent cookies:</strong> Stored long-term; used for remember-me and "
            "tracking.</li>"
            "<li><strong>Third-party cookies:</strong> Set by domains other than the one visited; "
            "used for cross-site tracking. Block or restrict in privacy settings.</li>"
            "<li><strong>Browser fingerprinting:</strong> Websites identify users via browser "
            "config, fonts, canvas rendering without cookies.</li>"
            "</ul>"
            "<h4>Security Features</h4>"
            "<ul>"
            "<li><strong>Safe Browsing / SmartScreen:</strong> Google and Microsoft maintain lists "
            "of known phishing and malware URLs; warn users before visiting.</li>"
            "<li><strong>InPrivate / Incognito mode:</strong> Does NOT make browsing anonymous — "
            "only prevents local history storage. ISP and employer can still see traffic.</li>"
            "<li><strong>Content Security Policy (CSP):</strong> HTTP header that restricts which "
            "scripts/resources a page may load; mitigates XSS attacks.</li>"
            "<li><strong>Same-origin policy:</strong> Browser prevents scripts from one origin "
            "reading content from a different origin.</li>"
            "</ul>"
        ),
        "key_points": [
            "Keep browsers updated — most drive-by exploits target unpatched browser vulnerabilities.",
            "Certificate errors (expired, mismatched) may indicate a MITM attack — do not proceed.",
            "InPrivate/Incognito only blocks local history; traffic is still visible to ISP/employer.",
            "Third-party cookies enable cross-site tracking — restrict or block in privacy settings.",
            "HSTS prevents SSL stripping/downgrade attacks by enforcing HTTPS at the browser level.",
            "Safe Browsing (Chrome) and SmartScreen (Edge/IE) warn about known phishing/malware URLs.",
            "Remove unused extensions — each extension can access page content and poses a risk.",
        ],
    },
]

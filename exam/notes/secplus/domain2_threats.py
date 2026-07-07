"""
CompTIA Security+ (SY0-701) — Domain 2: Threats, Vulnerabilities, and Mitigations
Original study notes; not copied from any copyrighted source.
"""

NOTES = [
    {
        "domain": 2,
        "topic": "Threat actors",
        "objective": "2.1",
        "video": "Threat Actors",
        "study_topics": ["Threat actors"],
        "body": (
            "<p>A <strong>threat actor</strong> is any entity that poses a risk to an "
            "organization's assets. Understanding who they are, what resources they have, "
            "and why they attack helps defenders prioritize controls.</p>"
            "<h3>Categories</h3>"
            "<ul>"
            "<li><strong>Nation-state / APT</strong> — Government-sponsored groups with "
            "high sophistication, virtually unlimited funding, and long dwell times. "
            "Motivations: espionage, sabotage, geopolitical goals. Example: attacks on "
            "critical infrastructure.</li>"
            "<li><strong>Unskilled attacker (script kiddie)</strong> — Uses pre-built "
            "tools without deep knowledge. Low sophistication, opportunistic, motivated "
            "by notoriety or curiosity.</li>"
            "<li><strong>Hacktivist</strong> — Attacks driven by ideology, politics, or "
            "social causes. May use DDoS, defacement, or data leaks. Resources vary.</li>"
            "<li><strong>Insider threat</strong> — Current or former employees, "
            "contractors, or partners. May be intentional (disgruntled, financial gain) "
            "or unintentional (negligent). Hardest to detect due to legitimate access.</li>"
            "<li><strong>Organized crime</strong> — Financially motivated criminal groups. "
            "High sophistication, use ransomware, fraud, data theft. Operate like "
            "businesses with specialization.</li>"
            "<li><strong>Shadow IT</strong> — Unauthorized hardware/software/services "
            "adopted by employees without IT approval. Not a malicious actor per se, but "
            "creates unmanaged attack surface and compliance risk.</li>"
            "</ul>"
            "<h3>Key Attributes</h3>"
            "<ul>"
            "<li><strong>Sophistication</strong>: skill level and tooling capability</li>"
            "<li><strong>Resources / funding</strong>: budget, infrastructure, personnel</li>"
            "<li><strong>Intent / motivation</strong>: financial, ideological, espionage, revenge</li>"
            "<li><strong>Internal vs. external</strong>: insiders bypass perimeter controls</li>"
            "</ul>"
        ),
        "key_points": [
            "Nation-state actors have the highest resources and sophistication.",
            "Insider threats are dangerous because they already have legitimate access.",
            "Organized crime is primarily financially motivated; ransomware is a common tool.",
            "Shadow IT creates unmanaged risk without malicious intent from users.",
            "Script kiddies are low-skill but can still cause damage with available tools.",
            "Motivation is a key differentiator: espionage, financial gain, ideology, notoriety.",
        ],
    },
    {
        "domain": 2,
        "topic": "Threat vectors and attack surfaces",
        "objective": "2.1",
        "video": "Threat Vectors and Attack Surfaces",
        "study_topics": ["Threat vectors and attack surfaces"],
        "body": (
            "<p>A <strong>threat vector</strong> is the path or method an attacker uses "
            "to gain unauthorized access. The <strong>attack surface</strong> is the "
            "total set of possible entry points exposed to potential attackers.</p>"
            "<h3>Common Threat Vectors</h3>"
            "<ul>"
            "<li><strong>Email</strong> — Phishing, malicious attachments, business email "
            "compromise. One of the most heavily exploited vectors.</li>"
            "<li><strong>Removable media</strong> — USB drives, optical discs used to "
            "deliver malware or exfiltrate data (e.g., Stuxnet).</li>"
            "<li><strong>Network / wireless</strong> — Exploitation of open ports, "
            "unpatched services, rogue access points, or unsecured Wi-Fi.</li>"
            "<li><strong>Supply chain</strong> — Compromising a vendor or software "
            "component that is trusted by the target (e.g., SolarWinds).</li>"
            "<li><strong>Social media</strong> — Used for reconnaissance, phishing links, "
            "or impersonation.</li>"
            "<li><strong>Cloud services</strong> — Misconfigured S3 buckets, over-privileged "
            "IAM roles, unsecured APIs.</li>"
            "<li><strong>Direct physical access</strong> — Tailgating, stolen hardware, "
            "dumpster diving.</li>"
            "<li><strong>Software vulnerabilities</strong> — Unpatched OS or application "
            "flaws exploited remotely or locally.</li>"
            "</ul>"
            "<h3>Reducing the Attack Surface</h3>"
            "<ul>"
            "<li>Disable unused services and ports.</li>"
            "<li>Remove unnecessary software and accounts.</li>"
            "<li>Apply principle of least privilege.</li>"
            "<li>Segment networks to limit lateral movement.</li>"
            "<li>Monitor and inventory all assets (shadow IT included).</li>"
            "</ul>"
        ),
        "key_points": [
            "Email is the most common initial attack vector for most threat actors.",
            "Supply chain attacks compromise trusted third parties to reach the ultimate target.",
            "Attack surface reduction: disable unneeded services, apply least privilege.",
            "Removable media can bypass network-based controls entirely.",
            "Cloud misconfigurations are a growing vector as workloads shift off-premises.",
        ],
    },
    {
        "domain": 2,
        "topic": "Social engineering",
        "objective": "2.2",
        "video": "Social Engineering",
        "study_topics": ["Social engineering"],
        "body": (
            "<p><strong>Social engineering</strong> manipulates human psychology rather "
            "than technical vulnerabilities to gain access or information. Most attacks "
            "begin with a social engineering component.</p>"
            "<h3>Key Techniques</h3>"
            "<ul>"
            "<li><strong>Phishing</strong> — Mass fraudulent emails impersonating "
            "legitimate entities to steal credentials or deliver malware.</li>"
            "<li><strong>Spear phishing</strong> — Targeted phishing aimed at a specific "
            "individual or organization using personalized details.</li>"
            "<li><strong>Whaling</strong> — Spear phishing directed at executives "
            "(C-suite) for high-value targets.</li>"
            "<li><strong>Vishing</strong> — Voice phishing via phone calls. Attacker "
            "impersonates tech support, banks, or government agencies.</li>"
            "<li><strong>Smishing</strong> — Phishing delivered via SMS text messages "
            "containing malicious links or requests.</li>"
            "<li><strong>Pretexting</strong> — Creating a fabricated scenario (pretext) "
            "to build trust and extract information (e.g., posing as an auditor).</li>"
            "<li><strong>Business Email Compromise (BEC)</strong> — Attackers "
            "impersonate executives or vendors via email to authorize fraudulent wire "
            "transfers or data disclosures.</li>"
            "<li><strong>Watering hole</strong> — Compromising a website frequented by "
            "the target group; victims are infected when they visit.</li>"
            "<li><strong>Typosquatting</strong> — Registering domains similar to "
            "legitimate sites (e.g., g00gle.com) to capture typo victims.</li>"
            "<li><strong>Tailgating / piggybacking</strong> — Following authorized "
            "personnel through secured doors.</li>"
            "</ul>"
            "<h3>Psychological Principles Exploited</h3>"
            "<p>Authority, urgency, scarcity, social proof, familiarity, intimidation.</p>"
        ),
        "key_points": [
            "Phishing is mass; spear phishing is targeted; whaling targets executives.",
            "Vishing uses voice; smishing uses SMS text messages.",
            "BEC causes billions in fraud annually by impersonating trusted parties via email.",
            "Watering hole attacks compromise trusted sites visited by the target group.",
            "Pretexting fabricates a believable scenario to lower the victim's guard.",
            "Typosquatting relies on users mistyping a URL to land on a malicious clone.",
        ],
    },
    {
        "domain": 2,
        "topic": "Application vulnerabilities",
        "objective": "2.3",
        "video": "Application Vulnerabilities",
        "study_topics": ["Application vulnerabilities"],
        "body": (
            "<p>Application vulnerabilities arise from software design flaws, coding "
            "errors, or insecure configurations. They are a primary target because "
            "applications handle sensitive data and are often internet-facing.</p>"
            "<h3>Common Vulnerability Classes</h3>"
            "<ul>"
            "<li><strong>Buffer overflow</strong> — Writing beyond allocated memory "
            "boundaries, potentially overwriting control data and executing arbitrary "
            "code. Mitigations: ASLR, DEP/NX, stack canaries.</li>"
            "<li><strong>Race condition / TOCTOU</strong> — Exploiting the gap between "
            "time-of-check and time-of-use to alter state mid-operation.</li>"
            "<li><strong>Improper input validation</strong> — Accepting untrusted data "
            "without sanitization, enabling injection and overflow attacks.</li>"
            "<li><strong>Improper error handling</strong> — Verbose error messages "
            "revealing stack traces, paths, or version info useful to attackers.</li>"
            "<li><strong>Insecure defaults</strong> — Default credentials, open ports, "
            "or unnecessary features enabled out of the box.</li>"
            "<li><strong>Injection flaws</strong> — Inserting malicious code/commands "
            "into interpreted contexts (SQL, OS, LDAP, XML).</li>"
            "<li><strong>Memory leaks</strong> — Unreleased memory leading to DoS via "
            "resource exhaustion.</li>"
            "<li><strong>Integer overflow</strong> — Arithmetic wrap-around causing "
            "unexpected behavior.</li>"
            "<li><strong>API vulnerabilities</strong> — Broken object-level authorization, "
            "lack of rate limiting, excessive data exposure in API responses.</li>"
            "</ul>"
            "<h3>Mitigation Approaches</h3>"
            "<p>Secure SDLC, static/dynamic code analysis (SAST/DAST), fuzz testing, "
            "peer code reviews, patching, WAF deployment, and principle of least privilege "
            "for service accounts.</p>"
        ),
        "key_points": [
            "Buffer overflows overwrite adjacent memory; mitigated by ASLR, DEP, and canaries.",
            "TOCTOU race conditions exploit a timing gap between check and use.",
            "Improper error handling leaks system information useful for reconnaissance.",
            "Injection attacks (SQL, OS, LDAP) stem from lack of input validation.",
            "Secure SDLC integrates security testing (SAST, DAST, fuzz) throughout development.",
            "API vulnerabilities are a growing class: over-exposure and broken authorization.",
        ],
    },
    {
        "domain": 2,
        "topic": "Web application vulnerabilities",
        "objective": "2.3",
        "video": "Web Application Vulnerabilities",
        "study_topics": ["Web application vulnerabilities"],
        "body": (
            "<p>Web applications are exposed to the internet and process untrusted input, "
            "making them high-value targets. The OWASP Top 10 catalogs the most critical "
            "web application security risks.</p>"
            "<h3>SQL Injection (SQLi)</h3>"
            "<p>Malicious SQL inserted into input fields is executed by the back-end "
            "database. Types: in-band (classic), blind, out-of-band. Consequences: data "
            "exfiltration, authentication bypass, database modification. Mitigation: "
            "parameterized queries / prepared statements, ORM, least-privilege DB accounts, WAF.</p>"
            "<h3>Cross-Site Scripting (XSS)</h3>"
            "<ul>"
            "<li><strong>Reflected XSS</strong> — Malicious script included in a URL "
            "is reflected back and executed in the victim's browser.</li>"
            "<li><strong>Stored XSS</strong> — Script persisted in the server (database, "
            "comment field) and executed for every visitor.</li>"
            "<li><strong>DOM-based XSS</strong> — Client-side script manipulates the "
            "DOM with attacker-controlled data without a server round-trip.</li>"
            "</ul>"
            "<p>Mitigation: output encoding, Content Security Policy (CSP), input validation.</p>"
            "<h3>Cross-Site Request Forgery (CSRF)</h3>"
            "<p>Tricks an authenticated user's browser into sending an unintended request "
            "to a trusted site. The server processes it because the session cookie is "
            "automatically sent. Mitigation: anti-CSRF tokens (synchronizer token pattern), "
            "SameSite cookie attribute, re-authentication for sensitive actions.</p>"
            "<h3>Other Web Vulnerabilities</h3>"
            "<ul>"
            "<li><strong>Directory traversal</strong> — Using ../ sequences to access "
            "files outside the web root.</li>"
            "<li><strong>Insecure direct object reference (IDOR)</strong> — Accessing "
            "objects by manipulating reference IDs without authorization checks.</li>"
            "<li><strong>Clickjacking</strong> — Embedding a target page in an iframe "
            "to capture hidden clicks. Mitigation: X-Frame-Options, CSP frame-ancestors.</li>"
            "</ul>"
        ),
        "key_points": [
            "SQLi is prevented by parameterized queries, not just input filtering.",
            "Stored XSS is more dangerous than reflected XSS as it affects every visitor.",
            "CSRF exploits the browser's automatic cookie transmission to forge requests.",
            "Anti-CSRF tokens must be unpredictable and validated server-side.",
            "Directory traversal uses ../ sequences to escape the intended file path.",
            "IDOR occurs when authorization is not checked on object access by ID.",
        ],
    },
    {
        "domain": 2,
        "topic": "Mobile vulnerabilities",
        "objective": "2.3",
        "video": "Mobile Vulnerabilities",
        "study_topics": ["Mobile vulnerabilities"],
        "body": (
            "<p>Mobile devices introduce unique vulnerabilities due to their portability, "
            "diverse app ecosystems, and tendency to connect to untrusted networks.</p>"
            "<h3>Platform-Specific Risks</h3>"
            "<ul>"
            "<li><strong>Jailbreaking (iOS) / Rooting (Android)</strong> — Removing "
            "manufacturer security controls allows sideloading and bypasses sandboxing, "
            "greatly expanding the attack surface.</li>"
            "<li><strong>Sideloading</strong> — Installing apps outside official stores "
            "bypasses vetting and can introduce malware.</li>"
            "<li><strong>Malicious apps</strong> — Even app store apps may request "
            "excessive permissions; third-party stores carry higher risk.</li>"
            "</ul>"
            "<h3>Network-Based Risks</h3>"
            "<ul>"
            "<li><strong>Rogue / evil twin Wi-Fi</strong> — Attacker creates an AP with "
            "the same SSID as a trusted network to intercept traffic.</li>"
            "<li><strong>Bluetooth attacks</strong> — Bluejacking (unsolicited messages), "
            "bluesnarfing (unauthorized data access), bluebugging (full device control).</li>"
            "<li><strong>SMS / MMS attacks</strong> — Smishing, malicious links in texts, "
            "SIM swapping to hijack phone numbers and bypass SMS-based MFA.</li>"
            "</ul>"
            "<h3>Data Storage and App Security</h3>"
            "<ul>"
            "<li>Sensitive data stored in plaintext on device or in backups.</li>"
            "<li>Insecure inter-app communication via intents (Android) or URL schemes.</li>"
            "<li>Excessive permissions granted by users (camera, location, contacts).</li>"
            "</ul>"
            "<h3>Mobile Device Management (MDM)</h3>"
            "<p>MDM/EMM solutions enforce encryption, remote wipe, containerization of "
            "corporate data, and prevent unauthorized configuration changes.</p>"
        ),
        "key_points": [
            "Jailbreaking/rooting removes OS security controls and expands attack surface.",
            "Sideloading bypasses app store vetting, increasing malware risk.",
            "Evil twin attacks serve as a man-in-the-middle for all device traffic.",
            "SIM swapping hijacks a phone number to defeat SMS-based MFA.",
            "Bluesnarfing is unauthorized data access over Bluetooth.",
            "MDM enforces policy, encryption, and enables remote wipe on mobile devices.",
        ],
    },
    {
        "domain": 2,
        "topic": "Virtualization vulnerabilities",
        "objective": "2.3",
        "video": "Virtualization Vulnerabilities",
        "study_topics": ["Virtualization vulnerabilities"],
        "body": (
            "<p>Virtualization and cloud environments introduce new attack vectors "
            "beyond traditional physical infrastructure. A single compromised hypervisor "
            "can expose all guest VMs.</p>"
            "<h3>Hypervisor Attacks</h3>"
            "<ul>"
            "<li><strong>VM escape</strong> — Attacker exploits a hypervisor vulnerability "
            "to break out of a guest VM and gain access to the hypervisor or other VMs. "
            "Severity: critical — one escape compromises all co-tenants.</li>"
            "<li><strong>Hyperjacking</strong> — Installing a rogue hypervisor beneath the "
            "legitimate OS, giving the attacker total control while remaining invisible.</li>"
            "</ul>"
            "<h3>VM-to-VM Attacks</h3>"
            "<ul>"
            "<li><strong>VM sprawl</strong> — Uncontrolled proliferation of VMs creates "
            "unmanaged, unpatched systems that expand the attack surface.</li>"
            "<li><strong>Noisy neighbor / side-channel</strong> — Shared hardware allows "
            "timing or cache side-channel attacks (e.g., Spectre, Meltdown) between VMs.</li>"
            "</ul>"
            "<h3>Container Vulnerabilities</h3>"
            "<ul>"
            "<li>Containers share the host kernel; a kernel exploit may affect all containers.</li>"
            "<li>Container escape analogous to VM escape.</li>"
            "<li>Image vulnerabilities: running outdated or unsigned base images.</li>"
            "<li>Misconfigured orchestration (e.g., exposed Kubernetes API server).</li>"
            "</ul>"
            "<h3>Cloud-Specific Concerns</h3>"
            "<ul>"
            "<li>Misconfigured security groups, IAM over-privilege, lack of encryption "
            "at rest/in transit.</li>"
            "<li>Shared responsibility model confusion — customer vs. provider obligations.</li>"
            "</ul>"
        ),
        "key_points": [
            "VM escape is critical: a successful escape exposes the hypervisor and all guests.",
            "Hyperjacking installs a rogue hypervisor underneath the legitimate OS.",
            "VM sprawl creates unmanaged, unpatched attack surface within the environment.",
            "Side-channel attacks (Spectre/Meltdown) exploit shared hardware between VMs.",
            "Containers share the host kernel; a kernel exploit can affect all containers.",
            "Shared responsibility model: understanding what the cloud provider secures vs. the customer.",
        ],
    },
    {
        "domain": 2,
        "topic": "Cryptographic attacks",
        "objective": "2.3",
        "video": "Cryptographic Attacks",
        "study_topics": ["Cryptographic attacks"],
        "body": (
            "<p>Cryptographic attacks target weaknesses in encryption algorithms, "
            "implementations, or key management to expose plaintext or forge data.</p>"
            "<h3>Algorithm and Key Attacks</h3>"
            "<ul>"
            "<li><strong>Brute force</strong> — Exhaustively trying all possible keys. "
            "Defense: sufficiently long keys (AES-128+, RSA-2048+).</li>"
            "<li><strong>Birthday attack</strong> — Exploiting the birthday paradox to "
            "find hash collisions faster than brute force. Affects weak hash functions; "
            "defense: use SHA-256 or stronger.</li>"
            "<li><strong>Hash collision</strong> — Finding two different inputs that "
            "produce the same hash digest. MD5 and SHA-1 are considered broken for "
            "collision resistance.</li>"
            "<li><strong>Rainbow table</strong> — Pre-computed table of hash values used "
            "to reverse hash lookups. Defense: salt passwords before hashing.</li>"
            "<li><strong>Pass-the-hash (PtH)</strong> — Using a captured NTLM hash "
            "directly for authentication without knowing the plaintext password.</li>"
            "</ul>"
            "<h3>Protocol and Implementation Attacks</h3>"
            "<ul>"
            "<li><strong>Downgrade attack</strong> — Forcing a connection to use a weaker "
            "protocol or cipher suite (e.g., POODLE forcing SSLv3).</li>"
            "<li><strong>Meet-in-the-middle</strong> — Attack on double encryption "
            "schemes (e.g., 2DES) by encrypting from one end and decrypting from the "
            "other simultaneously.</li>"
            "<li><strong>Replay attack</strong> — Capturing and re-transmitting valid "
            "authentication data. Defense: nonces, timestamps, sequence numbers.</li>"
            "<li><strong>Side-channel attack</strong> — Analyzing power consumption, "
            "timing, or electromagnetic emissions to infer key material.</li>"
            "</ul>"
            "<h3>Key Management Issues</h3>"
            "<p>Weak or reused keys, improper certificate validation, and predictable "
            "random number generators undermine otherwise sound algorithms.</p>"
        ),
        "key_points": [
            "Birthday attacks find hash collisions; use SHA-256+ to mitigate.",
            "Rainbow tables reverse unsalted hashes; salting defeats them.",
            "Pass-the-hash uses a captured hash for authentication — no plaintext needed.",
            "Downgrade attacks force weaker ciphers; mitigate with protocol minimums (TLS 1.2+).",
            "Replay attacks reuse captured credentials; nonces and timestamps prevent this.",
            "Side-channel attacks target implementation artifacts, not the algorithm itself.",
        ],
    },
    {
        "domain": 2,
        "topic": "Malware types",
        "objective": "2.4",
        "video": "Malware Types",
        "study_topics": ["Malware types"],
        "body": (
            "<p>Malware is any software designed to harm or exploit systems. "
            "Different malware types have distinct behaviors, propagation methods, "
            "and goals.</p>"
            "<h3>Common Malware Types</h3>"
            "<ul>"
            "<li><strong>Ransomware</strong> — Encrypts victim files and demands payment "
            "for the decryption key. Modern variants use double extortion (also threaten "
            "to publish data). Defense: offline backups, patching, MFA.</li>"
            "<li><strong>Trojan</strong> — Disguised as legitimate software to trick users "
            "into executing it. Establishes backdoors or drops additional payloads. "
            "Does not self-replicate.</li>"
            "<li><strong>Worm</strong> — Self-replicating malware that spreads across "
            "networks without user interaction, exploiting vulnerabilities. "
            "Example: WannaCry used EternalBlue.</li>"
            "<li><strong>Rootkit</strong> — Hides itself and other malware by modifying "
            "the OS or firmware. Kernel-level rootkits are extremely difficult to detect. "
            "Defense: secure boot, integrity monitoring, reinstallation.</li>"
            "<li><strong>Logic bomb</strong> — Malicious code that executes when a "
            "specific condition is met (date/time, user action). Often planted by "
            "insiders.</li>"
            "<li><strong>Spyware</strong> — Secretly monitors user activity and "
            "exfiltrates information (browsing, credentials) to a third party.</li>"
            "<li><strong>Keylogger</strong> — Records keystrokes to capture credentials, "
            "PINs, and sensitive input. Can be software or hardware-based.</li>"
            "<li><strong>Adware</strong> — Displays unwanted ads; some variants cross "
            "into spyware behavior.</li>"
            "<li><strong>Botnet / bot</strong> — Compromised systems (bots) controlled "
            "by a command-and-control (C2) server; used for DDoS, spam, or credential "
            "stuffing.</li>"
            "<li><strong>Fileless malware</strong> — Lives in memory or abuses legitimate "
            "tools (PowerShell, WMI) to evade file-based detection.</li>"
            "</ul>"
        ),
        "key_points": [
            "Ransomware encrypts data; double extortion also threatens to leak stolen data.",
            "Worms self-replicate across networks; trojans require user execution.",
            "Rootkits hide in the OS or firmware and are hard to detect without integrity tools.",
            "Logic bombs trigger on a condition; often used by insider threats.",
            "Keyloggers capture keystrokes; can be hardware (USB) or software-based.",
            "Fileless malware uses legitimate OS tools to avoid file-based AV detection.",
        ],
    },
    {
        "domain": 2,
        "topic": "Network attacks",
        "objective": "2.4",
        "video": "Network Attacks",
        "study_topics": ["Network attacks"],
        "body": (
            "<p>Network attacks target communication infrastructure and protocols to "
            "disrupt services, intercept data, or gain unauthorized access.</p>"
            "<h3>Denial of Service</h3>"
            "<ul>"
            "<li><strong>DoS</strong> — Single source floods a target with traffic or "
            "exploits a vulnerability to exhaust resources.</li>"
            "<li><strong>DDoS</strong> — Coordinated attack from many sources (botnet). "
            "Types: volumetric (UDP flood), protocol (SYN flood), application-layer "
            "(HTTP flood / slowloris).</li>"
            "<li><strong>Amplification attack</strong> — Small spoofed query elicits a "
            "large response directed at the victim (DNS, NTP amplification).</li>"
            "</ul>"
            "<h3>Interception and Spoofing</h3>"
            "<ul>"
            "<li><strong>Man-in-the-Middle (MitM)</strong> — Attacker positions between "
            "two parties to intercept and possibly alter traffic.</li>"
            "<li><strong>ARP poisoning</strong> — Sending fake ARP replies to associate "
            "the attacker's MAC with a legitimate IP on the LAN.</li>"
            "<li><strong>DNS poisoning / hijacking</strong> — Corrupting DNS cache to "
            "redirect traffic to malicious servers. Defense: DNSSEC.</li>"
            "<li><strong>BGP hijacking</strong> — Malicious BGP announcements re-route "
            "internet traffic through attacker-controlled routers.</li>"
            "</ul>"
            "<h3>Password and Credential Attacks (Network Context)</h3>"
            "<ul>"
            "<li><strong>Brute force</strong> — Systematically trying all credential "
            "combinations against a login interface.</li>"
            "<li><strong>Password spraying</strong> — Trying a small set of common "
            "passwords across many accounts to avoid lockout thresholds.</li>"
            "<li><strong>Credential stuffing</strong> — Using breached username/password "
            "pairs against other services, exploiting password reuse.</li>"
            "</ul>"
            "<h3>Other Network Attacks</h3>"
            "<ul>"
            "<li><strong>VLAN hopping</strong> — Double-tagging or switch spoofing to "
            "access traffic on a different VLAN.</li>"
            "<li><strong>On-path attack</strong> — Synonym for MitM, SY0-701 preferred "
            "terminology.</li>"
            "</ul>"
        ),
        "key_points": [
            "DDoS uses botnets; types include volumetric, protocol, and application-layer.",
            "Amplification attacks use small spoofed requests to generate large responses.",
            "ARP poisoning redirects LAN traffic through the attacker for MitM.",
            "DNS poisoning redirects users to fake servers; DNSSEC mitigates this.",
            "Password spraying avoids account lockout by using few passwords across many accounts.",
            "Credential stuffing exploits password reuse from prior data breaches.",
        ],
    },
    {
        "domain": 2,
        "topic": "Physical attacks",
        "objective": "2.4",
        "video": "Physical Attacks",
        "study_topics": ["Physical attacks"],
        "body": (
            "<p>Physical attacks bypass logical controls by directly accessing hardware, "
            "cabling, or facilities. No network security tool prevents an attacker who "
            "can physically reach a system.</p>"
            "<h3>Access Control Bypass</h3>"
            "<ul>"
            "<li><strong>Tailgating / piggybacking</strong> — Following an authorized "
            "person through a secured door without using own credentials. Prevented by "
            "mantraps, security awareness training, and enforcing badge policy.</li>"
            "<li><strong>Badge cloning</strong> — Copying RFID/proximity card data to "
            "gain building access. Mitigated by encrypted credential cards (e.g., MIFARE "
            "DESFire).</li>"
            "</ul>"
            "<h3>Hardware Attacks</h3>"
            "<ul>"
            "<li><strong>USB / malicious hardware</strong> — Devices like the USB Rubber "
            "Ducky emulate HID keyboards to execute payloads automatically. "
            "Defense: disable USB ports, use device control software.</li>"
            "<li><strong>Evil maid attack</strong> — Attacker with brief physical access "
            "installs a hardware keylogger, bootkit, or modifies firmware while the "
            "owner is away.</li>"
            "<li><strong>Cold boot attack</strong> — Rapidly freezing RAM preserves "
            "encryption keys in memory; dumped after rebooting to attacker's OS. "
            "Defense: pre-boot authentication, memory encryption.</li>"
            "</ul>"
            "<h3>Environmental and Infrastructure</h3>"
            "<ul>"
            "<li><strong>Dumpster diving</strong> — Recovering sensitive documents or "
            "hardware from trash. Defense: shredding, degaussing, destruction policies.</li>"
            "<li><strong>Eavesdropping / shoulder surfing</strong> — Visual observation "
            "of screens or keyboards in public spaces.</li>"
            "<li><strong>Cable tapping</strong> — Physical interception of network or "
            "power cabling.</li>"
            "</ul>"
        ),
        "key_points": [
            "Tailgating bypasses electronic access controls through social manipulation.",
            "Mantraps (airlock vestibules) prevent tailgating at high-security entries.",
            "USB HID attacks automate keystrokes and can deploy payloads instantly.",
            "Evil maid attacks require only brief unattended access to compromise a device.",
            "Cold boot attacks extract encryption keys from chilled, residual RAM.",
            "Dumpster diving recovers useful information; shredding and destruction policies mitigate it.",
        ],
    },
    {
        "domain": 2,
        "topic": "Indicators of malicious activity",
        "objective": "2.4",
        "video": "Indicators of Malicious Activity",
        "study_topics": ["Indicators of malicious activity"],
        "body": (
            "<p><strong>Indicators of Compromise (IoCs)</strong> are forensic artifacts "
            "that suggest a system or network has been breached. Recognizing them enables "
            "timely incident response.</p>"
            "<h3>Host-Based Indicators</h3>"
            "<ul>"
            "<li>Unexpected processes or services running (especially at startup).</li>"
            "<li>New user accounts or privilege escalations not authorized.</li>"
            "<li>Modified system files or altered file hashes (integrity violations).</li>"
            "<li>Disabled or cleared security logs (log tampering).</li>"
            "<li>Unexpected outbound connections from the host.</li>"
            "<li>High CPU/memory usage with no clear cause (mining malware, C2 beaconing).</li>"
            "</ul>"
            "<h3>Network-Based Indicators</h3>"
            "<ul>"
            "<li>Unusual traffic volumes or patterns (DDoS precursor, exfiltration).</li>"
            "<li>Connections to known-bad IPs or domains (threat intelligence feeds).</li>"
            "<li>DNS queries to newly registered or non-corporate domains.</li>"
            "<li>Beaconing — periodic, regular outbound connections to a C2 server.</li>"
            "<li>Traffic on unusual ports or protocols not approved in policy.</li>"
            "<li>Large data transfers leaving the network (potential exfiltration).</li>"
            "</ul>"
            "<h3>Account and Authentication Indicators</h3>"
            "<ul>"
            "<li>Multiple failed logon attempts (brute force / spraying).</li>"
            "<li>Logins from unusual geographies or at unusual hours.</li>"
            "<li>Impossible travel — same account authenticated from two distant locations "
            "within a short timeframe.</li>"
            "</ul>"
            "<h3>Indicators of Attack (IoA)</h3>"
            "<p>IoAs focus on attacker behaviors and TTPs (MITRE ATT&amp;CK) rather than "
            "static artifacts, enabling earlier detection before a breach is confirmed.</p>"
        ),
        "key_points": [
            "IoCs are post-compromise artifacts; IoAs are behavioral indicators for earlier detection.",
            "Log tampering (cleared logs) is itself a strong indicator of malicious activity.",
            "C2 beaconing appears as periodic, regular outbound traffic patterns.",
            "Impossible travel flags same-account logins from geographically distant locations.",
            "Large unexpected data transfers may indicate exfiltration underway.",
            "MITRE ATT&CK maps adversary TTPs; useful for threat hunting and detection engineering.",
        ],
    },
    {
        "domain": 2,
        "topic": "Mitigation techniques",
        "objective": "2.5",
        "video": "Mitigation Techniques",
        "study_topics": ["Mitigation techniques"],
        "body": (
            "<p>Mitigation techniques reduce the probability or impact of a threat "
            "exploiting a vulnerability. Defense-in-depth applies multiple, overlapping "
            "controls so no single failure is catastrophic.</p>"
            "<h3>Network Segmentation and Access Control</h3>"
            "<ul>"
            "<li><strong>VLANs and micro-segmentation</strong> — Isolate systems to "
            "limit lateral movement after a compromise.</li>"
            "<li><strong>Zero Trust</strong> — Never implicitly trust any user or device; "
            "verify continuously using identity, device health, and context.</li>"
            "<li><strong>Least privilege</strong> — Grant only permissions needed for a "
            "task; revoke when no longer needed.</li>"
            "</ul>"
            "<h3>Endpoint and Application Controls</h3>"
            "<ul>"
            "<li><strong>Patching</strong> — Timely application of security patches "
            "closes known vulnerabilities.</li>"
            "<li><strong>Application allow-listing</strong> — Only approved executables "
            "run; blocks unknown malware.</li>"
            "<li><strong>EDR / XDR</strong> — Endpoint Detection and Response provides "
            "behavioral analysis and response capabilities beyond signature-based AV.</li>"
            "</ul>"
            "<h3>Data Protection</h3>"
            "<ul>"
            "<li><strong>Encryption at rest and in transit</strong> — Protects data "
            "confidentiality even if storage or network is compromised.</li>"
            "<li><strong>DLP</strong> — Data Loss Prevention tools inspect and block "
            "unauthorized data transfers.</li>"
            "<li><strong>Backups (3-2-1 rule)</strong> — 3 copies, 2 media types, "
            "1 offsite (and ideally 1 offline/immutable). Critical for ransomware recovery.</li>"
            "</ul>"
            "<h3>Security Awareness</h3>"
            "<p>User training reduces the effectiveness of social engineering. "
            "Phishing simulations, security policies, and clear reporting procedures "
            "build a security-aware culture.</p>"
        ),
        "key_points": [
            "Defense-in-depth layers controls so no single failure leads to full compromise.",
            "Zero Trust assumes breach and verifies every access request regardless of origin.",
            "Least privilege limits blast radius when an account is compromised.",
            "Application allow-listing blocks unknown executables including novel malware.",
            "3-2-1 backup rule ensures recovery capability against ransomware and disasters.",
            "EDR provides behavioral detection and response beyond signature-based antivirus.",
        ],
    },
    {
        "domain": 2,
        "topic": "Hardening",
        "objective": "2.5",
        "video": "Hardening",
        "study_topics": ["Hardening"],
        "body": (
            "<p><strong>Hardening</strong> is the process of reducing a system's attack "
            "surface by eliminating unnecessary services, enforcing secure configurations, "
            "and applying security baselines.</p>"
            "<h3>OS Hardening</h3>"
            "<ul>"
            "<li>Remove or disable unused services, ports, and protocols.</li>"
            "<li>Apply vendor-recommended security baselines (CIS Benchmarks, DISA STIGs).</li>"
            "<li>Enable host-based firewall; restrict inbound and outbound traffic.</li>"
            "<li>Enable audit logging and forward logs to a SIEM.</li>"
            "<li>Configure automatic updates or a patch management process.</li>"
            "<li>Enable screensaver lock and session timeouts.</li>"
            "</ul>"
            "<h3>Application Hardening</h3>"
            "<ul>"
            "<li>Change default credentials immediately upon deployment.</li>"
            "<li>Remove or disable default accounts and sample content.</li>"
            "<li>Disable or restrict debug interfaces and verbose error output in production.</li>"
            "<li>Use secure configuration management (IaC, configuration drift detection).</li>"
            "</ul>"
            "<h3>Network Device Hardening</h3>"
            "<ul>"
            "<li>Disable unused switch ports; place them in an unused VLAN.</li>"
            "<li>Enable port security and 802.1X authentication.</li>"
            "<li>Use SSH instead of Telnet; HTTPS instead of HTTP for management.</li>"
            "<li>Disable CDP/LLDP where not required; limit management plane access.</li>"
            "</ul>"
            "<h3>Mobile and IoT Hardening</h3>"
            "<ul>"
            "<li>Enforce MDM policies: encryption, remote wipe, app restrictions.</li>"
            "<li>Change default IoT credentials; isolate IoT devices on a separate VLAN.</li>"
            "<li>Keep firmware updated; disable unused features (Bluetooth, Telnet).</li>"
            "</ul>"
        ),
        "key_points": [
            "CIS Benchmarks and DISA STIGs provide authoritative hardening configurations.",
            "Disable or remove unused services, ports, and accounts to reduce attack surface.",
            "Change default credentials on every device and application before deployment.",
            "Configuration drift detection ensures systems stay in their hardened state.",
            "SSH over Telnet, HTTPS over HTTP — always use encrypted management protocols.",
            "IoT devices should be isolated on a dedicated VLAN and have firmware kept current.",
        ],
    },
    {
        "domain": 2,
        "topic": "Authentication factors and protocols",
        "objective": "2.4",
        "video": "Authentication Factors and Protocols",
        "study_topics": ["Authentication factors and protocols"],
        "body": (
            "<p>Authentication verifies the identity of a user or device. Strong "
            "authentication combines multiple independent factors, making credential "
            "theft insufficient for access.</p>"
            "<h3>Authentication Factors</h3>"
            "<table>"
            "<tr><th>Factor</th><th>Category</th><th>Examples</th></tr>"
            "<tr><td>Something you know</td><td>Knowledge</td>"
            "<td>Password, PIN, security question</td></tr>"
            "<tr><td>Something you have</td><td>Possession</td>"
            "<td>Smart card, hardware token (TOTP), phone (push notification)</td></tr>"
            "<tr><td>Something you are</td><td>Inherence</td>"
            "<td>Fingerprint, retina scan, facial recognition, voice</td></tr>"
            "<tr><td>Somewhere you are</td><td>Location</td>"
            "<td>Geolocation, network location (IP range)</td></tr>"
            "<tr><td>Something you do</td><td>Behavior</td>"
            "<td>Typing cadence, gait analysis</td></tr>"
            "</table>"
            "<h3>MFA and Key Concepts</h3>"
            "<ul>"
            "<li><strong>MFA</strong> requires two or more factors from <em>different</em> "
            "categories. Two passwords = not MFA.</li>"
            "<li><strong>TOTP</strong> (Time-based One-Time Password) generates codes "
            "synchronized to time (RFC 6238). HOTP is counter-based.</li>"
            "<li><strong>FIDO2 / WebAuthn / Passkeys</strong> — Phishing-resistant "
            "passwordless authentication using public-key cryptography bound to the "
            "device and origin.</li>"
            "</ul>"
            "<h3>Authentication Protocols</h3>"
            "<ul>"
            "<li><strong>Kerberos</strong> — Ticket-based protocol using a KDC (AS + TGS). "
            "Default for Active Directory. Vulnerable to pass-the-ticket and "
            "Kerberoasting.</li>"
            "<li><strong>NTLM</strong> — Challenge-response; older and weaker than "
            "Kerberos. Vulnerable to pass-the-hash and relay attacks.</li>"
            "<li><strong>LDAP / LDAPS</strong> — Directory access; LDAPS encrypts with "
            "TLS. Use LDAPS to prevent credential interception.</li>"
            "<li><strong>RADIUS / TACACS+</strong> — AAA protocols. RADIUS encrypts only "
            "password; TACACS+ encrypts full payload and separates AAA functions.</li>"
            "<li><strong>SAML / OAuth 2.0 / OIDC</strong> — Federated identity and SSO. "
            "SAML is XML-based; OIDC adds identity layer on top of OAuth 2.0.</li>"
            "</ul>"
        ),
        "key_points": [
            "MFA requires factors from different categories; two passwords do not qualify.",
            "FIDO2/WebAuthn passkeys are phishing-resistant due to origin-bound key pairs.",
            "Kerberos uses a KDC and tickets; vulnerable to pass-the-ticket and Kerberoasting.",
            "NTLM is vulnerable to pass-the-hash; prefer Kerberos in Windows environments.",
            "TACACS+ encrypts the entire payload and separates auth, authz, and accounting.",
            "RADIUS encrypts only the password field; TACACS+ is preferred for device AAA.",
        ],
    },
    {
        "domain": 2,
        "topic": "Log sources and investigative questions",
        "objective": "2.5",
        "video": "Log Sources and Investigative Questions",
        "study_topics": ["Log sources and investigative questions"],
        "body": (
            "<p>Logs provide the evidence trail needed to detect, investigate, and "
            "respond to security incidents. Centralized logging via a SIEM enables "
            "correlation across sources.</p>"
            "<h3>Key Log Sources</h3>"
            "<ul>"
            "<li><strong>System / OS logs</strong> — Login events (success/failure), "
            "privilege changes, service starts/stops, system errors.</li>"
            "<li><strong>Application logs</strong> — Authentication events, errors, "
            "transactions, and user actions within applications.</li>"
            "<li><strong>Security device logs</strong> — Firewall allow/deny records, "
            "IDS/IPS alerts, WAF events, proxy logs, VPN connections.</li>"
            "<li><strong>Network logs</strong> — NetFlow/IPFIX (traffic metadata), "
            "DNS query logs, DHCP assignments, switch/router logs.</li>"
            "<li><strong>Endpoint logs</strong> — EDR telemetry: process creation, "
            "file modifications, registry changes, network connections.</li>"
            "<li><strong>Authentication logs</strong> — Active Directory event logs "
            "(Event IDs: 4624 successful logon, 4625 failed logon, 4740 account lockout, "
            "4672 privilege use, 4648 explicit credentials).</li>"
            "<li><strong>Cloud logs</strong> — AWS CloudTrail, Azure Activity Log, "
            "GCP Audit Logs: API calls, configuration changes, access events.</li>"
            "</ul>"
            "<h3>Investigative Questions (5 W's)</h3>"
            "<ul>"
            "<li><strong>Who</strong> — Which user/account/IP initiated the activity?</li>"
            "<li><strong>What</strong> — What resources were accessed or modified?</li>"
            "<li><strong>When</strong> — Timeline of events (use UTC/synchronized NTP).</li>"
            "<li><strong>Where</strong> — Source and destination systems/locations.</li>"
            "<li><strong>Why</strong> — Intent and business justification (or lack thereof).</li>"
            "</ul>"
            "<p>Log integrity is critical: forward logs to an immutable, centralized SIEM "
            "immediately so that tampering on the source system does not destroy evidence.</p>"
        ),
        "key_points": [
            "Centralize logs in a SIEM for correlation; local logs can be tampered with.",
            "Windows Event IDs: 4624 (logon), 4625 (failed logon), 4740 (lockout), 4672 (privilege).",
            "NetFlow provides traffic metadata (flows) without capturing payload content.",
            "DNS logs can reveal C2 beaconing and domain generation algorithm (DGA) activity.",
            "Use NTP-synchronized timestamps across all sources for reliable event timelines.",
            "Cloud audit logs (CloudTrail, Azure Activity) are essential in cloud investigations.",
        ],
    },
    {
        "domain": 2,
        "topic": "Vulnerability scan and assessment result classification",
        "objective": "2.5",
        "video": "Vulnerability Scan and Assessment Results",
        "study_topics": ["Vulnerability scan and assessment result classification"],
        "body": (
            "<p>Vulnerability scans and assessments produce findings that must be "
            "classified, prioritized, and acted upon. Understanding result classification "
            "prevents both complacency and wasted effort.</p>"
            "<h3>Result Classification Matrix</h3>"
            "<table>"
            "<tr><th>Finding</th><th>Vulnerability Present?</th><th>Scanner Says?</th>"
            "<th>Meaning</th></tr>"
            "<tr><td><strong>True Positive (TP)</strong></td><td>Yes</td><td>Positive</td>"
            "<td>Real vulnerability correctly identified — act on it.</td></tr>"
            "<tr><td><strong>True Negative (TN)</strong></td><td>No</td><td>Negative</td>"
            "<td>No vulnerability and scanner correctly reports none — ideal clean result.</td></tr>"
            "<tr><td><strong>False Positive (FP)</strong></td><td>No</td><td>Positive</td>"
            "<td>Scanner reports a vulnerability that does not actually exist — "
            "wastes analyst time; tune scanner rules.</td></tr>"
            "<tr><td><strong>False Negative (FN)</strong></td><td>Yes</td><td>Negative</td>"
            "<td>Real vulnerability missed by the scanner — most dangerous; "
            "may lead to unaddressed risk.</td></tr>"
            "</table>"
            "<h3>Vulnerability Prioritization</h3>"
            "<ul>"
            "<li><strong>CVSS score</strong> — Common Vulnerability Scoring System "
            "rates severity 0–10 (Low, Medium, High, Critical) based on exploitability "
            "and impact metrics.</li>"
            "<li><strong>EPSS</strong> — Exploit Prediction Scoring System estimates "
            "the probability of exploitation in the wild within 30 days.</li>"
            "<li><strong>CVE / NVD</strong> — Standardized vulnerability identifiers and "
            "the National Vulnerability Database.</li>"
            "<li>Context matters: asset criticality, network exposure, available exploits, "
            "and business impact refine priority beyond raw CVSS score.</li>"
            "</ul>"
            "<h3>Scan Types</h3>"
            "<ul>"
            "<li><strong>Credentialed scan</strong> — Uses valid credentials for deeper "
            "inspection; fewer false positives, more accurate results.</li>"
            "<li><strong>Non-credentialed scan</strong> — External view; faster but "
            "more false positives and misses internal configuration issues.</li>"
            "<li><strong>Agent-based scan</strong> — Software agent on endpoint "
            "provides continuous, low-network-impact assessment.</li>"
            "</ul>"
        ),
        "key_points": [
            "False negatives are the most dangerous: a real vulnerability goes undetected.",
            "False positives waste analyst time; credentialed scans reduce them significantly.",
            "CVSS rates severity 0-10; EPSS estimates likelihood of exploitation in the wild.",
            "Credentialed scans produce more accurate results than non-credentialed scans.",
            "Asset criticality and business context should refine CVSS-based prioritization.",
            "CVE identifiers (e.g., CVE-2024-XXXXX) link vulnerabilities across tools and databases.",
        ],
    },
]

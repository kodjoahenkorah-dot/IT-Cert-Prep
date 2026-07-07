"""
CompTIA Security+ (SY0-701) Domain 4: Security Operations
Original study notes — not copied from any copyrighted source.
"""

NOTES = [
    {
        "domain": 4,
        "topic": "Hardening and Secure Baselines",
        "objective": "4.1",
        "video": "Hardening Targets",
        "study_topics": ["Hardening & secure baselines"],
        "body": (
            "<p><strong>Hardening</strong> is the process of reducing a system's attack surface by "
            "removing unnecessary services, closing unused ports, applying patches, and enforcing "
            "strong configuration settings. A <strong>secure baseline</strong> is a documented "
            "minimum-security configuration that all systems of a given type must meet before "
            "deployment.</p>"
            "<h4>Common hardening actions</h4>"
            "<ul>"
            "<li><strong>Patch management</strong> — apply OS, firmware, and application updates promptly.</li>"
            "<li><strong>Disable unnecessary services/ports</strong> — every open port is a potential entry point.</li>"
            "<li><strong>Remove default credentials</strong> — change factory passwords on every device.</li>"
            "<li><strong>Least-privilege accounts</strong> — run services under low-privilege service accounts.</li>"
            "<li><strong>Host-based firewall</strong> — whitelist only required inbound/outbound traffic.</li>"
            "<li><strong>Encryption at rest and in transit</strong> — enable full-disk encryption and TLS.</li>"
            "<li><strong>Application whitelisting</strong> — only approved executables may run.</li>"
            "<li><strong>Secure BIOS/UEFI</strong> — set firmware password and enable Secure Boot.</li>"
            "</ul>"
            "<h4>Baseline sources</h4>"
            "<ul>"
            "<li>CIS Benchmarks (Center for Internet Security)</li>"
            "<li>DISA STIGs (Security Technical Implementation Guides)</li>"
            "<li>Vendor security guides (Microsoft SCT, NIST SP 800-70)</li>"
            "</ul>"
            "<p>Baselines are typically enforced via Group Policy, configuration management tools "
            "(Ansible, Puppet, Chef), or MDM profiles and are periodically validated through "
            "configuration audits and vulnerability scans.</p>"
        ),
        "key_points": [
            "Hardening reduces attack surface by disabling unused features and services.",
            "Secure baselines define minimum-security configurations for each system type.",
            "CIS Benchmarks and DISA STIGs are widely used baseline standards.",
            "Configuration management tools enforce baselines at scale.",
            "Patch management is a foundational hardening activity.",
        ],
    },
    {
        "domain": 4,
        "topic": "Mobile Device Management",
        "objective": "4.1",
        "video": "Mobile Device Management",
        "study_topics": ["Mobile device management"],
        "body": (
            "<p><strong>Mobile Device Management (MDM)</strong> allows organizations to centrally "
            "configure, monitor, and secure smartphones, tablets, and laptops. It is a core "
            "component of <strong>Unified Endpoint Management (UEM)</strong>.</p>"
            "<h4>Key MDM capabilities</h4>"
            "<ul>"
            "<li><strong>Remote wipe</strong> — erase device data if lost or stolen (full or selective).</li>"
            "<li><strong>Containerization</strong> — separate corporate and personal data on BYOD devices.</li>"
            "<li><strong>Enforce passcodes and biometrics</strong> — require screen-lock with complexity rules.</li>"
            "<li><strong>Certificate deployment</strong> — push Wi-Fi and VPN certificates automatically.</li>"
            "<li><strong>App management (MAM)</strong> — whitelist/blacklist apps, push mandatory apps.</li>"
            "<li><strong>Geofencing / geolocation</strong> — restrict or enforce policies based on location.</li>"
            "<li><strong>Compliance enforcement</strong> — quarantine jailbroken/rooted devices.</li>"
            "</ul>"
            "<h4>Deployment models</h4>"
            "<table border='1' cellpadding='4'>"
            "<tr><th>Model</th><th>Ownership</th><th>Control level</th></tr>"
            "<tr><td>BYOD</td><td>Employee</td><td>Low — container only</td></tr>"
            "<tr><td>COPE</td><td>Corporate, personal use allowed</td><td>Medium</td></tr>"
            "<tr><td>CYOD</td><td>Employee chooses from approved list</td><td>Medium-high</td></tr>"
            "<tr><td>Corporate-only</td><td>Corporate</td><td>Full</td></tr>"
            "</table>"
            "<p>MDM agents connect to the MDM server over secure channels. Enrollment can be "
            "automated via Apple DEP/ABM, Android Zero-Touch, or Windows Autopilot.</p>"
        ),
        "key_points": [
            "MDM centralizes policy enforcement across mobile and endpoint devices.",
            "Remote wipe protects data on lost or stolen devices.",
            "Containerization keeps corporate data separate on BYOD devices.",
            "BYOD, COPE, CYOD, and corporate-only are the four ownership models.",
            "Jailbroken or rooted devices should be flagged as non-compliant by MDM.",
        ],
    },
    {
        "domain": 4,
        "topic": "Wireless Security",
        "objective": "4.1",
        "video": "Wireless Security",
        "study_topics": ["Wireless security"],
        "body": (
            "<p>Securing wireless networks requires the right encryption protocol, strong "
            "authentication, and protection against rogue devices.</p>"
            "<h4>Encryption protocols (evolution)</h4>"
            "<ul>"
            "<li><strong>WEP</strong> — deprecated; RC4-based, easily cracked in minutes.</li>"
            "<li><strong>WPA</strong> — TKIP encryption, improved over WEP but still weak.</li>"
            "<li><strong>WPA2</strong> — AES-CCMP; current minimum standard. Vulnerable to KRACK.</li>"
            "<li><strong>WPA3</strong> — SAE (Simultaneous Authentication of Equals) replaces PSK "
            "handshake; forward secrecy; protected management frames mandatory.</li>"
            "</ul>"
            "<h4>Authentication modes</h4>"
            "<ul>"
            "<li><strong>Personal (PSK)</strong> — shared passphrase; suitable for home/small business.</li>"
            "<li><strong>Enterprise (802.1X)</strong> — RADIUS server authenticates individual users "
            "via EAP methods (EAP-TLS, PEAP, EAP-TTLS).</li>"
            "</ul>"
            "<h4>Common wireless threats and mitigations</h4>"
            "<ul>"
            "<li><strong>Evil twin / rogue AP</strong> — deploy WIDS; use certificate-based 802.1X.</li>"
            "<li><strong>Deauth attack</strong> — WPA3 protected management frames mitigate this.</li>"
            "<li><strong>Disassociation attack</strong> — same mitigation as deauth.</li>"
            "<li><strong>SSID broadcast</strong> — hiding SSID offers minimal security (security through obscurity).</li>"
            "<li><strong>War driving</strong> — scanning for open/weak APs from a vehicle.</li>"
            "</ul>"
            "<p>Additional best practices: segment guest Wi-Fi on a separate VLAN, use certificate "
            "pinning for enterprise EAP, and perform periodic RF site surveys.</p>"
        ),
        "key_points": [
            "WPA3 with SAE is the current recommended wireless security standard.",
            "802.1X Enterprise mode authenticates each user individually via RADIUS.",
            "WEP is completely broken and must never be used.",
            "Protected management frames (WPA3) defend against deauth/disassociation attacks.",
            "Rogue APs and evil twins are detected with a Wireless Intrusion Detection System (WIDS).",
        ],
    },
    {
        "domain": 4,
        "topic": "Application Security",
        "objective": "4.1",
        "video": "Application Security",
        "study_topics": ["Application security"],
        "body": (
            "<p><strong>Application security</strong> encompasses all practices that protect software "
            "throughout the Software Development Life Cycle (SDLC) and in production.</p>"
            "<h4>Secure SDLC practices</h4>"
            "<ul>"
            "<li><strong>Threat modeling</strong> — identify threats early (STRIDE: Spoofing, Tampering, "
            "Repudiation, Information Disclosure, DoS, Elevation of Privilege).</li>"
            "<li><strong>Static Application Security Testing (SAST)</strong> — analyzes source code "
            "without running the app (white-box).</li>"
            "<li><strong>Dynamic Application Security Testing (DAST)</strong> — tests running application "
            "for vulnerabilities (black-box).</li>"
            "<li><strong>Software Composition Analysis (SCA)</strong> — scans third-party/open-source "
            "libraries for known CVEs.</li>"
            "<li><strong>Code signing</strong> — ensures code integrity and authenticates the publisher.</li>"
            "</ul>"
            "<h4>Runtime protections</h4>"
            "<ul>"
            "<li><strong>Input validation</strong> — reject unexpected data; prevent injection attacks.</li>"
            "<li><strong>Web Application Firewall (WAF)</strong> — filters HTTP traffic for OWASP Top 10 attacks.</li>"
            "<li><strong>Content Security Policy (CSP)</strong> — mitigates XSS via browser-enforced header.</li>"
            "<li><strong>Sandboxing</strong> — isolate application execution environment.</li>"
            "<li><strong>Fuzzing</strong> — send random/malformed input to discover crashes and bugs.</li>"
            "</ul>"
            "<h4>Common vulnerabilities (OWASP Top 10)</h4>"
            "<ul>"
            "<li>SQL injection, XSS, broken authentication, insecure deserialization, SSRF.</li>"
            "</ul>"
        ),
        "key_points": [
            "SAST analyzes source code statically; DAST tests the running application.",
            "Input validation is the primary defense against injection attacks.",
            "A WAF filters malicious HTTP requests at the application layer.",
            "STRIDE is a threat-modeling framework used during design.",
            "Software Composition Analysis identifies vulnerable open-source dependencies.",
        ],
    },
    {
        "domain": 4,
        "topic": "Asset Management",
        "objective": "4.2",
        "video": "Asset Management",
        "study_topics": ["Asset management"],
        "body": (
            "<p><strong>Asset management</strong> is the process of tracking and maintaining an accurate "
            "inventory of all hardware, software, and data assets throughout their lifecycle — from "
            "acquisition through decommissioning.</p>"
            "<h4>Asset inventory components</h4>"
            "<ul>"
            "<li><strong>Hardware assets</strong> — servers, workstations, networking gear, mobile devices.</li>"
            "<li><strong>Software assets</strong> — licenses, versions, patch levels; tracked via CMDB.</li>"
            "<li><strong>Data assets</strong> — classification levels (public, internal, confidential, restricted).</li>"
            "<li><strong>Cloud assets</strong> — virtual machines, containers, storage buckets.</li>"
            "</ul>"
            "<h4>Asset lifecycle</h4>"
            "<ol>"
            "<li><strong>Procurement</strong> — verify supply chain integrity; record asset details.</li>"
            "<li><strong>Deployment</strong> — apply baseline configuration before placing into service.</li>"
            "<li><strong>Operations</strong> — continuous monitoring, patching, and vulnerability scanning.</li>"
            "<li><strong>Decommissioning</strong> — sanitize media before disposal (NIST 800-88 guidelines).</li>"
            "</ol>"
            "<h4>Key concepts</h4>"
            "<ul>"
            "<li><strong>Configuration Management Database (CMDB)</strong> — central repository for asset "
            "records and relationships.</li>"
            "<li><strong>Asset tagging</strong> — physical labels (barcodes, RFID) for hardware tracking.</li>"
            "<li><strong>Shadow IT</strong> — unauthorized assets represent a risk; network scanning helps discover them.</li>"
            "<li><strong>License management</strong> — under-licensing creates legal risk; over-licensing wastes budget.</li>"
            "</ul>"
        ),
        "key_points": [
            "You cannot protect what you do not know about — asset inventory is foundational.",
            "A CMDB stores asset records and tracks relationships between configuration items.",
            "The asset lifecycle runs from procurement through secure decommissioning.",
            "Shadow IT assets bypass security controls and must be discovered and managed.",
            "Data assets must be classified to apply appropriate protection controls.",
        ],
    },
    {
        "domain": 4,
        "topic": "Vulnerability Management and CVSS",
        "objective": "4.3",
        "video": "Vulnerability Management",
        "study_topics": ["Vulnerability management & CVSS"],
        "body": (
            "<p><strong>Vulnerability management</strong> is a continuous cycle of discovering, "
            "prioritizing, remediating, and verifying vulnerabilities across the environment.</p>"
            "<h4>Vulnerability management cycle</h4>"
            "<ol>"
            "<li><strong>Discovery/Scan</strong> — credentialed and non-credentialed scans (Nessus, Qualys, OpenVAS).</li>"
            "<li><strong>Prioritization</strong> — score vulnerabilities; consider asset criticality and exploit availability.</li>"
            "<li><strong>Remediation</strong> — patch, reconfigure, or deploy compensating controls.</li>"
            "<li><strong>Verification</strong> — rescan to confirm the fix was effective.</li>"
            "<li><strong>Reporting</strong> — track metrics (mean time to remediate, vulnerability density).</li>"
            "</ol>"
            "<h4>CVSS (Common Vulnerability Scoring System)</h4>"
            "<p>CVSS v3.1 provides a 0–10 numeric score with three metric groups:</p>"
            "<ul>"
            "<li><strong>Base score</strong> — intrinsic characteristics: Attack Vector, Attack Complexity, "
            "Privileges Required, User Interaction, Scope, Confidentiality/Integrity/Availability impact. "
            "This score is fixed and does not change over time.</li>"
            "<li><strong>Temporal score</strong> — factors that change over time: exploit code maturity, "
            "remediation level, report confidence. Lowers or raises the base score.</li>"
            "<li><strong>Environmental score</strong> — organization-specific context: modified base metrics "
            "and security requirements. Allows tailoring to the local environment.</li>"
            "</ul>"
            "<p>Severity ratings: Critical (9.0–10.0), High (7.0–8.9), Medium (4.0–6.9), Low (0.1–3.9), None (0.0).</p>"
            "<h4>Related standards</h4>"
            "<ul>"
            "<li><strong>CVE</strong> — unique identifier for a specific vulnerability.</li>"
            "<li><strong>NVD</strong> — NIST's database enriching CVEs with CVSS scores.</li>"
            "<li><strong>EPSS</strong> — Exploit Prediction Scoring System; probability of exploitation within 30 days.</li>"
            "</ul>"
        ),
        "key_points": [
            "CVSS base score reflects intrinsic severity; temporal and environmental scores refine it.",
            "Credentialed scans provide deeper visibility than unauthenticated scans.",
            "Prioritize by combining CVSS score with asset criticality and exploit availability.",
            "CVE is a unique identifier; NVD provides enrichment including CVSS scores.",
            "EPSS estimates the probability a vulnerability will be exploited in the near term.",
        ],
    },
    {
        "domain": 4,
        "topic": "SIEM and Security Monitoring",
        "objective": "4.4",
        "video": "Security Information and Event Management",
        "study_topics": ["SIEM & monitoring"],
        "body": (
            "<p>A <strong>Security Information and Event Management (SIEM)</strong> platform aggregates "
            "log data from across the environment, correlates events, and generates alerts for potential "
            "security incidents.</p>"
            "<h4>Core SIEM functions</h4>"
            "<ul>"
            "<li><strong>Log aggregation</strong> — collect and normalize logs from diverse sources.</li>"
            "<li><strong>Event correlation</strong> — link related events across systems to identify attack patterns.</li>"
            "<li><strong>Alerting</strong> — trigger notifications when correlation rules match.</li>"
            "<li><strong>Dashboards and reporting</strong> — visualize security posture and compliance metrics.</li>"
            "<li><strong>Retention</strong> — store logs long-term for forensic investigation and compliance.</li>"
            "</ul>"
            "<h4>Detection approaches</h4>"
            "<ul>"
            "<li><strong>Signature/rule-based</strong> — matches known attack patterns (low false negatives, "
            "misses novel threats).</li>"
            "<li><strong>Anomaly/behavior-based</strong> — establishes a baseline and flags deviations "
            "(higher false positive rate but detects unknowns).</li>"
            "<li><strong>Threat intelligence integration</strong> — enrich events with IOC feeds (IP reputation, "
            "domain blocklists, file hashes).</li>"
            "</ul>"
            "<h4>SOAR integration</h4>"
            "<p><strong>Security Orchestration, Automation, and Response (SOAR)</strong> extends SIEM by "
            "automating repetitive tasks: blocking IPs, resetting accounts, opening tickets. SOAR uses "
            "playbooks to execute consistent, auditable response workflows.</p>"
            "<h4>Key metrics</h4>"
            "<ul>"
            "<li>Mean Time to Detect (MTTD)</li>"
            "<li>Mean Time to Respond (MTTR)</li>"
            "<li>False positive rate</li>"
            "</ul>"
        ),
        "key_points": [
            "SIEM aggregates, correlates, and alerts on security events from multiple sources.",
            "Signature-based detection misses novel threats; anomaly-based catches unknowns but has more false positives.",
            "SOAR automates response actions via playbooks, reducing analyst workload.",
            "Log retention supports forensic investigations and regulatory compliance.",
            "MTTD and MTTR are key performance indicators for a SOC.",
        ],
    },
    {
        "domain": 4,
        "topic": "Log Data Sources",
        "objective": "4.4",
        "video": "Log Sources",
        "study_topics": ["Log data sources"],
        "body": (
            "<p>Effective monitoring depends on ingesting the right log sources. Each source provides "
            "a different view of activity across the environment.</p>"
            "<h4>Common log sources</h4>"
            "<table border='1' cellpadding='4'>"
            "<tr><th>Source</th><th>What it captures</th></tr>"
            "<tr><td>Firewall / NGFW</td><td>Allow/deny decisions, NAT translations, application traffic</td></tr>"
            "<tr><td>IDS/IPS</td><td>Signature matches, anomalous traffic, blocked attacks</td></tr>"
            "<tr><td>Windows Event Log</td><td>Logon events (4624/4625), privilege use, process creation</td></tr>"
            "<tr><td>Syslog (Linux/Unix)</td><td>Auth events (/var/log/auth.log), application logs, kernel messages</td></tr>"
            "<tr><td>DNS logs</td><td>Query/response records; useful for detecting DNS tunneling and C2 domains</td></tr>"
            "<tr><td>DHCP logs</td><td>IP address assignments; correlate IPs to hostnames at a point in time</td></tr>"
            "<tr><td>Web server logs</td><td>HTTP requests, user agents, response codes, referrers</td></tr>"
            "<tr><td>Proxy / URL filter</td><td>Outbound HTTP/S traffic with user attribution</td></tr>"
            "<tr><td>NetFlow / IPFIX</td><td>Network flow metadata (src/dst IP, port, bytes) — no payload content</td></tr>"
            "<tr><td>VPN logs</td><td>Remote access connections, authentication events</td></tr>"
            "<tr><td>EDR / endpoint</td><td>Process execution, file creation, registry changes, network connections</td></tr>"
            "<tr><td>Cloud audit logs</td><td>AWS CloudTrail, Azure Activity Log — API calls, resource changes</td></tr>"
            "</table>"
            "<p>Log sources should use a common timestamp (NTP-synchronized) and be forwarded via "
            "syslog or API to the SIEM. <strong>Log integrity</strong> can be protected with "
            "write-once storage or cryptographic chaining.</p>"
        ),
        "key_points": [
            "DNS logs are valuable for detecting C2 communications and DNS tunneling.",
            "DHCP logs correlate IP addresses to hostnames for forensic timeline reconstruction.",
            "NetFlow captures traffic metadata without payload — useful for volume/behavior analysis.",
            "Windows Event IDs 4624 and 4625 track successful and failed logon attempts.",
            "Cloud audit logs (CloudTrail, Activity Log) record all API and management-plane actions.",
        ],
    },
    {
        "domain": 4,
        "topic": "Email Security — SPF, DKIM, and DMARC",
        "objective": "4.4",
        "video": "Email Security",
        "study_topics": ["Email security (SPF/DKIM/DMARC)"],
        "body": (
            "<p>Three DNS-based mechanisms work together to authenticate email and prevent spoofing, "
            "phishing, and domain impersonation.</p>"
            "<h4>SPF — Sender Policy Framework</h4>"
            "<p>A DNS TXT record listing IP addresses and mail servers authorized to send email on "
            "behalf of a domain. The receiving mail server checks the envelope sender's domain against "
            "the SPF record. If the sending IP is not listed, the check fails. SPF alone does not "
            "protect the visible From: header.</p>"
            "<h4>DKIM — DomainKeys Identified Mail</h4>"
            "<p>Adds a cryptographic signature to the email header using a private key held by the "
            "sending server. The receiving server retrieves the corresponding public key from DNS and "
            "verifies the signature. DKIM proves message integrity and that the sending domain "
            "authorized the message. It survives forwarding better than SPF.</p>"
            "<h4>DMARC — Domain-based Message Authentication, Reporting &amp; Conformance</h4>"
            "<p>DMARC ties SPF and DKIM together and adds a policy for handling failures. Key elements:</p>"
            "<ul>"
            "<li><strong>Alignment</strong> — the domain in the visible From: header must align with the "
            "SPF-authenticated or DKIM-signed domain.</li>"
            "<li><strong>Policy options</strong>: <code>p=none</code> (monitor only), "
            "<code>p=quarantine</code> (send to spam), <code>p=reject</code> (block delivery).</li>"
            "<li><strong>Reporting</strong> — DMARC sends aggregate (RUA) and forensic (RUF) reports "
            "to the domain owner for visibility.</li>"
            "</ul>"
            "<h4>Additional email security controls</h4>"
            "<ul>"
            "<li><strong>S/MIME</strong> — end-to-end encryption and signing of message content.</li>"
            "<li><strong>Secure Email Gateway (SEG)</strong> — filters spam, malware, and phishing.</li>"
            "<li><strong>Anti-spoofing headers</strong> — X-Originating-IP, Received chain analysis.</li>"
            "</ul>"
        ),
        "key_points": [
            "SPF lists authorized sending IPs in DNS; protects the envelope sender domain.",
            "DKIM cryptographically signs email headers; proves message integrity and sender authorization.",
            "DMARC enforces alignment between the visible From: domain and SPF/DKIM results.",
            "DMARC p=reject is the strongest policy — failed messages are blocked entirely.",
            "DMARC aggregate reports (RUA) give visibility into who is sending email as your domain.",
        ],
    },
    {
        "domain": 4,
        "topic": "EDR, XDR, and Data Loss Prevention",
        "objective": "4.4",
        "video": "Endpoint Detection and Response",
        "study_topics": ["EDR/XDR & DLP"],
        "body": (
            "<p><strong>Endpoint Detection and Response (EDR)</strong> provides deep visibility into "
            "endpoint activity, enabling real-time threat detection and rapid investigation.</p>"
            "<h4>EDR capabilities</h4>"
            "<ul>"
            "<li>Continuous process, file, network, and registry telemetry collection.</li>"
            "<li>Behavioral detection of fileless malware, living-off-the-land techniques (LOLBins).</li>"
            "<li>Automated threat containment (isolate host from network).</li>"
            "<li>Threat hunting — proactive querying of telemetry for IOCs and TTPs.</li>"
            "<li>Forensic evidence collection (memory dumps, timeline analysis).</li>"
            "</ul>"
            "<h4>XDR — Extended Detection and Response</h4>"
            "<p>XDR extends EDR by correlating telemetry across endpoints, network, email, cloud, and "
            "identity. It provides a unified investigation interface and reduces alert fatigue by "
            "stitching related events into a single incident view.</p>"
            "<h4>DLP — Data Loss Prevention</h4>"
            "<p>DLP solutions inspect and control data in motion, at rest, and in use to prevent "
            "unauthorized exfiltration of sensitive information.</p>"
            "<ul>"
            "<li><strong>Network DLP</strong> — monitors and blocks sensitive data leaving via email, "
            "web, FTP, etc. (inline proxy or out-of-band).</li>"
            "<li><strong>Endpoint DLP</strong> — controls copy-to-USB, print, clipboard, screen capture.</li>"
            "<li><strong>Cloud DLP / CASB</strong> — enforces policies on data stored in SaaS and IaaS.</li>"
            "</ul>"
            "<p>DLP uses <strong>content inspection</strong> (regex patterns for SSNs, PCI data, PHI) "
            "and <strong>contextual analysis</strong> (who, what device, what destination) to make "
            "allow/block/quarantine decisions.</p>"
        ),
        "key_points": [
            "EDR collects continuous endpoint telemetry and enables real-time detection and response.",
            "XDR correlates data across endpoints, network, email, and cloud for unified detection.",
            "DLP prevents sensitive data from leaving the organization through policy enforcement.",
            "Endpoint DLP controls USB, print, and clipboard actions on managed devices.",
            "EDR can isolate a compromised host from the network while preserving forensic state.",
        ],
    },
    {
        "domain": 4,
        "topic": "Access Control Models",
        "objective": "4.6",
        "video": "Access Control",
        "study_topics": ["Access control models"],
        "body": (
            "<p>Access control models define rules for granting or denying subjects (users/processes) "
            "access to objects (files/resources). The Security+ exam tests the four primary models.</p>"
            "<h4>Mandatory Access Control (MAC)</h4>"
            "<p>The operating system enforces access based on <strong>labels</strong> (classification "
            "levels: Top Secret, Secret, Confidential, Unclassified). Users cannot change permissions. "
            "Used in high-security government and military environments. Example: SELinux, Trusted Solaris.</p>"
            "<h4>Discretionary Access Control (DAC)</h4>"
            "<p>The <strong>resource owner</strong> sets permissions at their discretion. Most common "
            "model in everyday operating systems (Windows NTFS ACLs, Linux file permissions). Flexible "
            "but subject to user error and social engineering.</p>"
            "<h4>Role-Based Access Control (RBAC)</h4>"
            "<p>Access is assigned to <strong>roles</strong>, and users are assigned to roles. "
            "Simplifies administration — when job function changes, update the role assignment, not "
            "individual permissions. Common in enterprise directories and applications.</p>"
            "<h4>Attribute-Based Access Control (ABAC)</h4>"
            "<p>Access decisions are based on <strong>attributes</strong> of the subject (department, "
            "clearance), resource (sensitivity label, type), and environment (time of day, location). "
            "Very fine-grained and dynamic. Used in NGAC (Next Generation AC) and cloud IAM policies.</p>"
            "<h4>Rule-Based Access Control</h4>"
            "<p>Access is determined by a set of <strong>administrator-defined rules</strong> (e.g., "
            "firewall ACLs: allow TCP port 443 from subnet X). Rules apply to all subjects equally "
            "regardless of identity.</p>"
            "<h4>Key principle</h4>"
            "<p><strong>Least privilege</strong> — grant only the minimum access required to perform "
            "job functions. Combined with <strong>need-to-know</strong>, it limits blast radius.</p>"
        ),
        "key_points": [
            "MAC uses system-enforced labels; users cannot override permissions.",
            "DAC lets the resource owner set permissions — flexible but risky.",
            "RBAC assigns permissions to roles; users inherit access via role membership.",
            "ABAC makes access decisions based on attributes of user, resource, and environment.",
            "Rule-based AC (firewall ACLs) applies rules to all subjects equally.",
            "Least privilege limits the damage from compromised accounts.",
        ],
    },
    {
        "domain": 4,
        "topic": "Multifactor Authentication",
        "objective": "4.6",
        "video": "Multifactor Authentication",
        "study_topics": ["Multifactor authentication"],
        "body": (
            "<p><strong>Multifactor Authentication (MFA)</strong> requires two or more distinct "
            "authentication factors, making credential theft alone insufficient to gain access. "
            "The four factor categories are:</p>"
            "<table border='1' cellpadding='4'>"
            "<tr><th>Factor</th><th>Category</th><th>Examples</th></tr>"
            "<tr><td>Something you <strong>know</strong></td><td>Knowledge</td>"
            "<td>Password, PIN, security questions</td></tr>"
            "<tr><td>Something you <strong>have</strong></td><td>Possession</td>"
            "<td>Hardware token (TOTP), smart card, OTP app, push notification</td></tr>"
            "<tr><td>Something you <strong>are</strong></td><td>Inherence / biometrics</td>"
            "<td>Fingerprint, facial recognition, iris scan, voice pattern</td></tr>"
            "<tr><td>Somewhere you <strong>are</strong></td><td>Location</td>"
            "<td>GPS geolocation, IP-based restriction, network context</td></tr>"
            "</table>"
            "<h4>Common MFA implementations</h4>"
            "<ul>"
            "<li><strong>TOTP</strong> — Time-based One-Time Password (RFC 6238); generated by apps "
            "like Google Authenticator; valid for ~30 seconds.</li>"
            "<li><strong>HOTP</strong> — HMAC-based OTP (counter-based); does not expire by time.</li>"
            "<li><strong>Push notifications</strong> — user approves login on registered device "
            "(e.g., Duo, Okta Verify); vulnerable to MFA fatigue attacks.</li>"
            "<li><strong>Hardware tokens</strong> — RSA SecurID, YubiKey (FIDO2/WebAuthn); phishing-resistant.</li>"
            "<li><strong>SMS OTP</strong> — weakest form; vulnerable to SIM swapping and SS7 attacks.</li>"
            "</ul>"
            "<h4>Phishing-resistant MFA</h4>"
            "<p>FIDO2/WebAuthn and smart cards are considered phishing-resistant because authentication "
            "is bound to the specific origin (domain), preventing credential relay attacks.</p>"
        ),
        "key_points": [
            "MFA requires two or more factors from different categories (know/have/are/where).",
            "TOTP generates a time-limited code; HOTP uses a counter — both are HMAC-based.",
            "SMS OTP is the weakest MFA form due to SIM swapping and SS7 vulnerabilities.",
            "FIDO2/WebAuthn (hardware security keys) is phishing-resistant MFA.",
            "MFA fatigue attacks exploit push-based MFA by bombarding users with approve requests.",
        ],
    },
    {
        "domain": 4,
        "topic": "Federation and Single Sign-On (SAML, OAuth, OpenID Connect)",
        "objective": "4.6",
        "video": "Federation and SSO",
        "study_topics": ["Federation & SSO (SAML/OAuth)"],
        "body": (
            "<p><strong>Federation</strong> allows identities from one organization or system to be "
            "trusted by another, enabling <strong>Single Sign-On (SSO)</strong> across organizational "
            "boundaries without synchronizing passwords.</p>"
            "<h4>SAML 2.0 — Security Assertion Markup Language</h4>"
            "<p>XML-based standard for exchanging authentication and authorization data between an "
            "<strong>Identity Provider (IdP)</strong> and a <strong>Service Provider (SP)</strong>. "
            "Widely used for enterprise SSO to web applications. The IdP issues signed XML assertions "
            "that the SP trusts. Supports SP-initiated and IdP-initiated flows.</p>"
            "<h4>OAuth 2.0</h4>"
            "<p>An authorization framework (not authentication) that allows a user to grant a "
            "third-party application limited access to their resources without sharing credentials. "
            "Issues access tokens (Bearer tokens). Common grant types: Authorization Code (most secure, "
            "uses PKCE), Client Credentials (machine-to-machine), Implicit (deprecated).</p>"
            "<h4>OpenID Connect (OIDC)</h4>"
            "<p>An identity layer built on top of OAuth 2.0 that adds <strong>authentication</strong>. "
            "Issues an <strong>ID token</strong> (JWT) that identifies the authenticated user in addition "
            "to the access token. Used for consumer and enterprise SSO (Google, Microsoft, Okta).</p>"
            "<h4>Key terms</h4>"
            "<ul>"
            "<li><strong>IdP</strong> — holds user identities and performs authentication.</li>"
            "<li><strong>SP / Relying Party</strong> — trusts the IdP and provides the service.</li>"
            "<li><strong>JWT</strong> — JSON Web Token; compact, URL-safe signed token format.</li>"
            "<li><strong>PKCE</strong> — Proof Key for Code Exchange; prevents authorization code interception.</li>"
            "</ul>"
        ),
        "key_points": [
            "SAML uses XML assertions for enterprise SSO between IdP and SP.",
            "OAuth 2.0 is an authorization framework — it grants access, not proves identity.",
            "OpenID Connect adds an identity layer to OAuth 2.0, enabling authentication.",
            "The Authorization Code flow with PKCE is the most secure OAuth grant type.",
            "Federation extends trust across organizational boundaries without password synchronization.",
        ],
    },
    {
        "domain": 4,
        "topic": "Privileged Access Management",
        "objective": "4.6",
        "video": "Privileged Access Management",
        "study_topics": ["Privileged access management"],
        "body": (
            "<p><strong>Privileged Access Management (PAM)</strong> controls, monitors, and audits "
            "access to privileged accounts — those with elevated permissions such as domain admins, "
            "root accounts, service accounts, and database administrators.</p>"
            "<h4>Core PAM capabilities</h4>"
            "<ul>"
            "<li><strong>Privileged account discovery</strong> — identify all privileged accounts "
            "including shared, service, and embedded credentials.</li>"
            "<li><strong>Credential vaulting</strong> — store privileged passwords in an encrypted "
            "vault; users check out credentials and never see the actual password (just-in-time).</li>"
            "<li><strong>Session recording</strong> — record all privileged sessions (keystrokes, video) "
            "for audit and forensic purposes.</li>"
            "<li><strong>Just-in-Time (JIT) access</strong> — grant elevated privileges only when needed "
            "and revoke automatically after a defined period.</li>"
            "<li><strong>Password rotation</strong> — automatically rotate privileged passwords after "
            "each use or on a schedule to prevent credential reuse.</li>"
            "</ul>"
            "<h4>Principle of least privilege for admins</h4>"
            "<ul>"
            "<li><strong>Separate admin accounts</strong> — administrators use a standard account for "
            "daily tasks and a separate privileged account only when needed.</li>"
            "<li><strong>Privileged Access Workstations (PAW)</strong> — dedicated hardened systems "
            "used exclusively for administrative tasks; no web browsing or email.</li>"
            "<li><strong>Break-glass accounts</strong> — emergency accounts with credentials stored "
            "offline or in a sealed envelope; access is audited and alarmed.</li>"
            "</ul>"
            "<p>PAM significantly reduces the risk from insider threats and reduces the blast radius "
            "when an attacker compromises a standard user account.</p>"
        ),
        "key_points": [
            "PAM vaults store privileged passwords and issue them on a just-in-time basis.",
            "Session recording provides a full audit trail of all privileged activity.",
            "JIT access eliminates standing privileges, reducing the window of exposure.",
            "Privileged Access Workstations (PAWs) are hardened systems used only for admin tasks.",
            "Automatic password rotation after each use prevents credential reuse attacks.",
        ],
    },
    {
        "domain": 4,
        "topic": "Automation and Security Orchestration",
        "objective": "4.7",
        "video": "Automation and Scripting",
        "study_topics": ["Automation & orchestration"],
        "body": (
            "<p>Automation reduces manual effort, improves consistency, and accelerates response times "
            "in security operations. <strong>Security Orchestration, Automation, and Response (SOAR)</strong> "
            "platforms formalize this through playbooks.</p>"
            "<h4>Benefits of automation in security</h4>"
            "<ul>"
            "<li><strong>Speed</strong> — automated containment (blocking IPs, isolating hosts) occurs "
            "in seconds vs. minutes/hours manually.</li>"
            "<li><strong>Consistency</strong> — playbooks ensure every incident of the same type is "
            "handled the same way, reducing human error.</li>"
            "<li><strong>Scalability</strong> — handle high alert volumes without proportionally increasing staff.</li>"
            "<li><strong>Auditability</strong> — automated actions are logged, supporting compliance and forensics.</li>"
            "</ul>"
            "<h4>Common automation use cases</h4>"
            "<ul>"
            "<li>Auto-block malicious IPs on firewall/proxy when threat intel feed triggers.</li>"
            "<li>Automatically disable compromised user account after brute-force detection.</li>"
            "<li>Create and route ITSM tickets (ServiceNow, Jira) for confirmed incidents.</li>"
            "<li>Enrich alerts with threat intelligence (VirusTotal lookups, WHOIS data).</li>"
            "<li>Scan newly deployed cloud instances for compliance drift.</li>"
            "<li>Rotate credentials after privilege escalation detection.</li>"
            "</ul>"
            "<h4>Infrastructure as Code (IaC) security</h4>"
            "<p>Terraform, CloudFormation, and Ansible templates define infrastructure configuration. "
            "Scanning IaC files for misconfigurations before deployment (shift-left security) prevents "
            "cloud misconfiguration vulnerabilities at scale.</p>"
            "<h4>Risk of automation</h4>"
            "<p>Poorly written playbooks can cause false-positive lockouts or outages. Human review "
            "checkpoints should be included for high-impact automated actions.</p>"
        ),
        "key_points": [
            "SOAR playbooks automate incident response tasks consistently and at scale.",
            "Auto-blocking, account disabling, and ticket creation are common SOAR use cases.",
            "IaC scanning (shift-left) detects cloud misconfigurations before deployment.",
            "Automation improves speed and consistency but must include safeguards for high-impact actions.",
            "Every automated action should be logged for audit and forensic purposes.",
        ],
    },
    {
        "domain": 4,
        "topic": "Incident Response Process",
        "objective": "4.8",
        "video": "Incident Response",
        "study_topics": ["Incident response process"],
        "body": (
            "<p>The <strong>incident response (IR)</strong> process provides a structured approach for "
            "detecting, containing, and recovering from security incidents. The NIST SP 800-61 framework "
            "defines six phases:</p>"
            "<ol>"
            "<li><strong>Preparation</strong> — establish the IR team, create and test the IR plan, "
            "deploy monitoring tools, train staff, identify critical assets, establish communication "
            "channels and escalation procedures.</li>"
            "<li><strong>Detection and Analysis</strong> — identify potential incidents via alerts, "
            "user reports, or threat hunting. Determine scope, severity, and attack vector. Document "
            "findings in an incident ticket. Declare an incident if thresholds are met.</li>"
            "<li><strong>Containment</strong> — limit further damage. Short-term containment (isolate "
            "host, block IP) followed by long-term containment (rebuild systems, patch). Preserve "
            "forensic evidence before wiping.</li>"
            "<li><strong>Eradication</strong> — remove the root cause: delete malware, close the "
            "exploited vulnerability, remove unauthorized accounts, rotate compromised credentials.</li>"
            "<li><strong>Recovery</strong> — restore systems to normal operations from clean backups. "
            "Monitor closely for signs of re-infection. Validate that systems are fully functional.</li>"
            "<li><strong>Lessons Learned (Post-Incident Activity)</strong> — conduct a post-incident "
            "review (within ~2 weeks). Document what happened, what worked, what failed, and update "
            "the IR plan and detection rules accordingly.</li>"
            "</ol>"
            "<h4>Incident classification</h4>"
            "<ul>"
            "<li><strong>Event</strong> — any observable occurrence in a system.</li>"
            "<li><strong>Incident</strong> — an event that violates security policy or causes harm.</li>"
            "<li><strong>IOC</strong> — Indicator of Compromise; observable artifact suggesting intrusion.</li>"
            "</ul>"
            "<h4>IR team roles</h4>"
            "<ul>"
            "<li>Incident Commander, Security Analyst, Forensic Analyst, Legal/HR, Communications lead.</li>"
            "</ul>"
        ),
        "key_points": [
            "The six NIST IR phases are: Preparation, Detection/Analysis, Containment, Eradication, Recovery, Lessons Learned.",
            "Preservation of forensic evidence must occur before containment actions that alter system state.",
            "Eradication removes the root cause; recovery restores normal operations.",
            "Lessons learned improve the IR plan and detection capabilities for future incidents.",
            "An event becomes an incident when it violates security policy or causes actual harm.",
        ],
    },
    {
        "domain": 4,
        "topic": "Digital Forensics and Chain of Custody",
        "objective": "4.8",
        "video": "Digital Forensics",
        "study_topics": ["Digital forensics", "Digital forensics and chain-of-custody process"],
        "body": (
            "<p><strong>Digital forensics</strong> is the process of collecting, preserving, analyzing, "
            "and presenting digital evidence in a legally admissible manner.</p>"
            "<h4>Order of volatility (most to least volatile)</h4>"
            "<ol>"
            "<li>CPU registers and cache</li>"
            "<li>RAM and running processes</li>"
            "<li>Network connections and routing tables</li>"
            "<li>Temporary file system / swap space</li>"
            "<li>Non-volatile storage (hard drives, SSDs)</li>"
            "<li>Logs stored on remote servers</li>"
            "<li>Archival media (backup tapes, optical discs)</li>"
            "</ol>"
            "<p>Always collect evidence in order from most volatile to least volatile.</p>"
            "<h4>Chain of custody</h4>"
            "<p>A documented record tracking who collected, handled, transferred, and examined each "
            "piece of evidence from collection through court presentation. It must be unbroken to "
            "ensure admissibility. Elements include: description of evidence, date/time of collection, "
            "collector identity, location collected, signatures of all custodians.</p>"
            "<h4>Evidence integrity</h4>"
            "<ul>"
            "<li><strong>Write blocker</strong> — hardware or software device that prevents any writes "
            "to original media during acquisition.</li>"
            "<li><strong>Forensic image</strong> — bit-for-bit copy of storage media (dd, FTK Imager).</li>"
            "<li><strong>Hashing</strong> — MD5 or SHA-256 hash computed on acquisition; re-verified "
            "before analysis to prove evidence was not altered.</li>"
            "</ul>"
            "<h4>Legal hold</h4>"
            "<p>A directive to preserve all potentially relevant data when litigation or investigation "
            "is reasonably anticipated. Overrides normal retention/deletion schedules.</p>"
            "<h4>Key forensic concepts</h4>"
            "<ul>"
            "<li><strong>Locard's Exchange Principle</strong> — every contact leaves a trace.</li>"
            "<li><strong>eDiscovery</strong> — legal process of identifying and producing electronically stored information.</li>"
            "<li><strong>Steganography</strong> — hiding data within other files (images, audio).</li>"
            "</ul>"
        ),
        "key_points": [
            "Collect evidence from most volatile (RAM) to least volatile (archival media).",
            "Chain of custody documents every person who handles evidence to ensure admissibility.",
            "A write blocker prevents evidence contamination during disk imaging.",
            "Hash the forensic image at acquisition and re-verify before analysis.",
            "Legal hold preserves data when litigation is anticipated, overriding deletion schedules.",
        ],
    },
    {
        "domain": 4,
        "topic": "Malware Classification",
        "objective": "4.8",
        "video": "Malware",
        "study_topics": ["Malware classification"],
        "body": (
            "<p>Understanding malware types helps analysts identify behavior, assess impact, and select "
            "appropriate countermeasures.</p>"
            "<table border='1' cellpadding='4'>"
            "<tr><th>Type</th><th>Description</th><th>Key characteristic</th></tr>"
            "<tr><td>Virus</td><td>Attaches to a host file; spreads when the file is executed</td>"
            "<td>Requires human action to propagate</td></tr>"
            "<tr><td>Worm</td><td>Self-replicating; spreads across networks without user interaction</td>"
            "<td>Autonomous propagation (e.g., WannaCry, Slammer)</td></tr>"
            "<tr><td>Trojan</td><td>Disguised as legitimate software; delivers hidden payload</td>"
            "<td>No self-replication; relies on social engineering</td></tr>"
            "<tr><td>Ransomware</td><td>Encrypts victim files and demands payment for the decryption key</td>"
            "<td>Monetization via cryptocurrency; double-extortion variants exfiltrate data first</td></tr>"
            "<tr><td>Rootkit</td><td>Hides its presence by modifying OS kernel or firmware</td>"
            "<td>Kernel-mode rootkits are very hard to detect/remove</td></tr>"
            "<tr><td>Backdoor / RAT</td><td>Provides persistent remote access to the attacker</td>"
            "<td>Remote Access Trojan (RAT) combines trojan delivery with backdoor capability</td></tr>"
            "<tr><td>Spyware</td><td>Silently monitors user activity; exfiltrates data</td>"
            "<td>Keyloggers are a subset; often bundled with adware</td></tr>"
            "<tr><td>Adware</td><td>Displays unwanted advertisements; may track browsing</td>"
            "<td>Usually not destructive but degrades user experience</td></tr>"
            "<tr><td>Botnet / Bot</td><td>Compromised host controlled by a C2 server as part of a larger network</td>"
            "<td>Used for DDoS, spam, credential stuffing</td></tr>"
            "<tr><td>Fileless malware</td><td>Lives entirely in memory; uses LOLBins (PowerShell, WMI)</td>"
            "<td>Leaves no files on disk; evades traditional AV</td></tr>"
            "<tr><td>Logic bomb</td><td>Malicious code triggered by a specific event or date</td>"
            "<td>Often planted by insiders; activates on termination date</td></tr>"
            "<tr><td>Keylogger</td><td>Records keystrokes to capture credentials</td>"
            "<td>Can be hardware or software-based</td></tr>"
            "</table>"
        ),
        "key_points": [
            "Worms self-propagate; viruses require a host file and human execution.",
            "Ransomware encrypts data and demands payment; double-extortion also exfiltrates data.",
            "Rootkits hide malware presence by subverting the OS kernel.",
            "Fileless malware resides in memory and uses LOLBins, evading file-based AV.",
            "A logic bomb is triggered by a specific condition (date, event) and is often insider-planted.",
        ],
    },
    {
        "domain": 4,
        "topic": "Port and Protocol Security",
        "objective": "4.1",
        "video": "Ports and Protocols",
        "study_topics": ["Port and protocol security"],
        "body": (
            "<p>Understanding standard ports and protocols is essential for configuring firewalls, "
            "detecting anomalous traffic, and hardening systems.</p>"
            "<h4>Key ports to know for Security+</h4>"
            "<table border='1' cellpadding='4'>"
            "<tr><th>Port(s)</th><th>Protocol</th><th>Notes</th></tr>"
            "<tr><td>20/21</td><td>FTP</td><td>Cleartext; use SFTP (22) or FTPS (990) instead</td></tr>"
            "<tr><td>22</td><td>SSH / SFTP / SCP</td><td>Encrypted; preferred for remote admin and file transfer</td></tr>"
            "<tr><td>23</td><td>Telnet</td><td>Cleartext; replace with SSH</td></tr>"
            "<tr><td>25</td><td>SMTP</td><td>Email submission/relay; use 587 (STARTTLS) or 465 (SMTPS)</td></tr>"
            "<tr><td>53</td><td>DNS</td><td>UDP/TCP; DNS over HTTPS (DoH) encrypts queries</td></tr>"
            "<tr><td>80</td><td>HTTP</td><td>Cleartext web; redirect to 443</td></tr>"
            "<tr><td>110/995</td><td>POP3 / POP3S</td><td>Email retrieval; 995 is encrypted</td></tr>"
            "<tr><td>143/993</td><td>IMAP / IMAPS</td><td>Email retrieval; 993 is encrypted</td></tr>"
            "<tr><td>389/636</td><td>LDAP / LDAPS</td><td>Directory services; 636 uses TLS</td></tr>"
            "<tr><td>443</td><td>HTTPS</td><td>TLS-encrypted web traffic</td></tr>"
            "<tr><td>445</td><td>SMB</td><td>Windows file sharing; disable if not needed; WannaCry vector</td></tr>"
            "<tr><td>514</td><td>Syslog</td><td>UDP; use 6514 for TLS-encrypted syslog</td></tr>"
            "<tr><td>1433</td><td>MS SQL</td><td>Restrict to application servers only</td></tr>"
            "<tr><td>1812/1813</td><td>RADIUS</td><td>Authentication / accounting</td></tr>"
            "<tr><td>3306</td><td>MySQL</td><td>Database; firewall to app tier only</td></tr>"
            "<tr><td>3389</td><td>RDP</td><td>Remote Desktop; restrict to VPN/jump server; frequent attack target</td></tr>"
            "<tr><td>5060/5061</td><td>SIP / SIPS</td><td>VoIP signaling; 5061 is TLS</td></tr>"
            "</table>"
            "<p>Security best practices: block all ports by default; allow only what is necessary "
            "(implicit deny). Use encrypted alternatives for cleartext protocols. Expose management "
            "interfaces (SSH, RDP) only through a VPN or jump server, not directly to the internet.</p>"
        ),
        "key_points": [
            "Replace cleartext protocols: FTP→SFTP, Telnet→SSH, HTTP→HTTPS, LDAP→LDAPS.",
            "RDP (3389) and SMB (445) are high-value attack targets; restrict access strictly.",
            "Implicit deny — block all traffic by default and allow only what is required.",
            "DNS (53) should be monitored for tunneling; consider DNS over HTTPS for privacy.",
            "RADIUS (1812/1813) provides centralized AAA for network access control.",
        ],
    },
    {
        "domain": 4,
        "topic": "Penetration Testing Phases",
        "objective": "4.3",
        "video": "Penetration Testing",
        "study_topics": ["Penetration testing phases"],
        "body": (
            "<p><strong>Penetration testing</strong> is a simulated, authorized cyberattack used to "
            "identify exploitable vulnerabilities before real attackers do. It differs from a "
            "vulnerability scan — a pen test actively exploits findings.</p>"
            "<h4>Pen test types by knowledge</h4>"
            "<ul>"
            "<li><strong>Black box</strong> — tester has no prior knowledge; simulates an external attacker.</li>"
            "<li><strong>White box</strong> — full knowledge of architecture, source code, credentials; "
            "most thorough.</li>"
            "<li><strong>Gray box</strong> — partial knowledge; simulates an insider or authenticated user.</li>"
            "</ul>"
            "<h4>Penetration testing phases</h4>"
            "<ol>"
            "<li><strong>Planning / Reconnaissance</strong> — define scope and rules of engagement (ROE); "
            "gather OSINT (passive recon via WHOIS, LinkedIn, Shodan) and active recon (DNS enumeration, "
            "port scanning).</li>"
            "<li><strong>Scanning / Enumeration</strong> — identify open ports, running services, OS "
            "versions, and potential vulnerabilities (Nmap, Nessus, Nikto).</li>"
            "<li><strong>Exploitation</strong> — attempt to exploit discovered vulnerabilities to gain "
            "access (Metasploit, manual exploits, social engineering).</li>"
            "<li><strong>Post-Exploitation</strong> — escalate privileges, move laterally, establish "
            "persistence, and demonstrate the blast radius of a breach.</li>"
            "<li><strong>Reporting</strong> — document all findings with severity ratings, evidence, "
            "and remediation recommendations; deliver executive summary and technical report.</li>"
            "<li><strong>Cleanup / Remediation Validation</strong> — remove test artifacts; optionally "
            "retest to verify remediations are effective.</li>"
            "</ol>"
            "<h4>Related assessments</h4>"
            "<ul>"
            "<li><strong>Red team</strong> — covert, goal-based adversary simulation; tests detection "
            "and response, not just vulnerabilities.</li>"
            "<li><strong>Blue team</strong> — defenders who detect and respond.</li>"
            "<li><strong>Purple team</strong> — collaborative red/blue exercise to improve defenses.</li>"
            "<li><strong>Bug bounty</strong> — crowd-sourced vulnerability disclosure program with defined scope.</li>"
            "</ul>"
        ),
        "key_points": [
            "Pen testing actively exploits vulnerabilities; a vulnerability scan only identifies them.",
            "Rules of engagement (ROE) define scope, timing, and authorized techniques.",
            "The five core phases are: Planning/Recon, Scanning, Exploitation, Post-Exploitation, Reporting.",
            "Black box simulates an external attacker; white box provides full knowledge for deeper testing.",
            "Red team exercises test detection and response capabilities, not just vulnerability presence.",
        ],
    },
]

"""
CCNA 200-301 Domain 5: Security Fundamentals
Study notes covering all exam objectives in this domain.
"""

NOTES = [
    {
        "domain": 5,
        "topic": "Security concepts (threats/vulnerabilities)",
        "objective": "5.1",
        "video": "Security Threats and Vulnerabilities",
        "study_topics": ["Security concepts (threats/vulnerabilities)"],
        "body": (
            "<p>Network security begins with understanding the threat landscape. "
            "A <strong>threat</strong> is any potential danger to an asset, while a "
            "<strong>vulnerability</strong> is a weakness that a threat actor can exploit. "
            "A <strong>risk</strong> is the likelihood that a threat will exploit a vulnerability "
            "and cause harm.</p>"
            "<p><strong>Common attack categories:</strong></p>"
            "<ul>"
            "<li><strong>Malware</strong> – malicious software including viruses (attach to files), "
            "worms (self-replicate across networks), Trojans (disguised as legitimate software), "
            "ransomware (encrypts data for ransom), and spyware.</li>"
            "<li><strong>Social engineering</strong> – manipulating people rather than systems. "
            "Phishing (email), vishing (voice), smishing (SMS), and pretexting are key subtypes.</li>"
            "<li><strong>DoS / DDoS</strong> – Denial-of-Service floods a target with traffic to "
            "exhaust resources. Distributed DoS uses botnets to amplify the attack.</li>"
            "<li><strong>Man-in-the-Middle (MitM)</strong> – attacker intercepts and possibly alters "
            "traffic between two parties, often via ARP poisoning or rogue access points.</li>"
            "<li><strong>Password attacks</strong> – brute force, dictionary attacks, and credential "
            "stuffing attempt to obtain valid credentials.</li>"
            "<li><strong>Reconnaissance</strong> – passive (OSINT, packet sniffing) or active "
            "(port scanning, ping sweeps) intelligence gathering before an attack.</li>"
            "<li><strong>Privilege escalation</strong> – gaining higher access than initially "
            "authorized, either vertically (user to admin) or horizontally (user to user).</li>"
            "<li><strong>SQL injection / buffer overflow</strong> – application-layer exploits that "
            "abuse poor input validation.</li>"
            "</ul>"
            "<p><strong>Key concepts:</strong> The CIA triad — Confidentiality, Integrity, and "
            "Availability — forms the foundation of security goals. "
            "Defense-in-depth (layered security) ensures no single control is a single point of "
            "failure.</p>"
        ),
        "key_points": [
            "Threat = potential danger; Vulnerability = weakness; Risk = likelihood of exploit causing harm.",
            "CIA triad: Confidentiality, Integrity, Availability.",
            "Phishing is the most common social-engineering vector on the CCNA exam.",
            "DoS exhausts resources; DDoS uses botnets to scale the attack.",
            "MitM attacks can exploit ARP poisoning or rogue wireless APs.",
            "Defense-in-depth uses multiple overlapping security controls.",
        ],
    },
    {
        "domain": 5,
        "topic": "Security program elements",
        "objective": "5.2",
        "video": "Security Program Elements",
        "study_topics": ["Security program elements"],
        "body": (
            "<p>A comprehensive security program combines people, processes, and technology to "
            "protect organizational assets.</p>"
            "<p><strong>Core program elements:</strong></p>"
            "<ul>"
            "<li><strong>User awareness training</strong> – educates employees on recognizing "
            "phishing, safe browsing, password hygiene, and acceptable-use policies. Human error "
            "remains the leading cause of breaches.</li>"
            "<li><strong>Security policies</strong> – formal written rules governing acceptable use, "
            "password requirements, data classification, incident response, and change management.</li>"
            "<li><strong>Data classification</strong> – categorizes data by sensitivity (e.g., public, "
            "internal, confidential, restricted) to apply appropriate controls.</li>"
            "<li><strong>Vulnerability management</strong> – regular scanning, patch management, and "
            "remediation to close known weaknesses before attackers exploit them.</li>"
            "<li><strong>Incident response (IR)</strong> – a documented process: Preparation, "
            "Identification, Containment, Eradication, Recovery, and Lessons Learned (PICERL).</li>"
            "<li><strong>Physical security</strong> – locks, badge access, security cameras, and "
            "mantraps prevent unauthorized physical access to network equipment.</li>"
            "<li><strong>Principle of least privilege</strong> – users and services receive only the "
            "minimum permissions required for their role.</li>"
            "<li><strong>Separation of duties</strong> – critical tasks require more than one person "
            "to prevent fraud or error by a single individual.</li>"
            "<li><strong>Logging and monitoring</strong> – SIEM platforms aggregate logs from network "
            "devices, endpoints, and applications to detect and investigate anomalies.</li>"
            "</ul>"
            "<p>Security programs are cyclical: plan, implement, monitor, and improve. Regular "
            "audits and penetration tests validate that controls remain effective over time.</p>"
        ),
        "key_points": [
            "User awareness training reduces the human-factor risk from phishing and social engineering.",
            "Incident response phases: Preparation, Identification, Containment, Eradication, Recovery, Lessons Learned.",
            "Principle of least privilege limits the blast radius of a compromised account.",
            "Separation of duties requires multiple people for sensitive operations.",
            "SIEM aggregates logs from many sources to enable centralized monitoring.",
            "Physical security is part of a complete security program — locks and badge access protect hardware.",
        ],
    },
    {
        "domain": 5,
        "topic": "Device access control (passwords)",
        "objective": "5.3",
        "video": "Device Access Control",
        "study_topics": ["Device access control (passwords)"],
        "body": (
            "<p>Cisco IOS devices provide several lines of access that must be secured to prevent "
            "unauthorized configuration changes.</p>"
            "<p><strong>Access lines and their passwords:</strong></p>"
            "<ul>"
            "<li><strong>Console line (line con 0)</strong> – physical console port; secured with "
            "<code>password</code> and <code>login</code> commands, or <code>login local</code> "
            "for local username/password pairs.</li>"
            "<li><strong>AUX line (line aux 0)</strong> – auxiliary port for modem access; should "
            "be disabled when not needed (<code>no exec</code>).</li>"
            "<li><strong>VTY lines (line vty 0 4)</strong> – virtual terminal lines used for Telnet "
            "and SSH remote access. Always restrict with an access-class ACL.</li>"
            "<li><strong>Enable password</strong> – legacy command stored in plaintext; replaced by "
            "<code>enable secret</code>.</li>"
            "<li><strong>Enable secret</strong> – stored as a salted MD5 hash (type 5) by default; "
            "protects privileged EXEC mode.</li>"
            "</ul>"
            "<p><strong>Password encryption:</strong></p>"
            "<ul>"
            "<li><code>service password-encryption</code> – applies a weak Cisco type-7 Vigenere "
            "cipher to all plaintext passwords in the running config. Not strong cryptography — "
            "easily reversed — but better than cleartext.</li>"
            "<li>Enable secret uses MD5 (type 5); newer IOS versions support SHA-256 (type 8) and "
            "scrypt (type 9) for stronger hashing.</li>"
            "</ul>"
            "<p><strong>Banner messages:</strong> <code>banner motd</code> provides a legal-warning "
            "banner displayed before login. Required to establish that unauthorized access is "
            "prohibited; banners with \"Welcome\" wording can void prosecutions.</p>"
            "<p><strong>Exec timeout:</strong> <code>exec-timeout 5 0</code> on VTY/console lines "
            "automatically logs out idle sessions after 5 minutes, limiting exposure from "
            "unattended terminals.</p>"
        ),
        "key_points": [
            "Always use 'enable secret' instead of 'enable password' — secret is hashed, password is plaintext.",
            "'service password-encryption' applies weak type-7 obfuscation to line passwords; not truly secure.",
            "Console (con 0), AUX (aux 0), and VTY (vty 0 4) lines each require individual password configuration.",
            "'login local' uses the local username database; 'login' uses the line password.",
            "Use 'exec-timeout' to disconnect idle sessions automatically.",
            "Banner MOTD should contain a legal warning — avoid welcoming language.",
        ],
    },
    {
        "domain": 5,
        "topic": "Password policies & MFA",
        "objective": "5.4",
        "video": "Password Policies and MFA",
        "study_topics": ["Password policies & MFA"],
        "body": (
            "<p>Strong authentication relies on well-crafted password policies and supplementary "
            "factors to ensure only authorized users gain access.</p>"
            "<p><strong>Password policy best practices:</strong></p>"
            "<ul>"
            "<li><strong>Minimum length</strong> – industry guidance (NIST SP 800-63B) recommends "
            "at least 8 characters for user accounts; 15+ for privileged accounts.</li>"
            "<li><strong>Complexity</strong> – mix of uppercase, lowercase, digits, and special "
            "characters reduces brute-force susceptibility.</li>"
            "<li><strong>Password history</strong> – prevents reuse of recent passwords (e.g., "
            "last 12 passwords).</li>"
            "<li><strong>Maximum age / expiration</strong> – forces periodic rotation; however, "
            "NIST 800-63B now advises against arbitrary expiration unless compromise is suspected.</li>"
            "<li><strong>Account lockout</strong> – disables an account after a set number of "
            "failed attempts to thwart brute-force attacks.</li>"
            "</ul>"
            "<p><strong>Multi-Factor Authentication (MFA):</strong> Requires two or more of the "
            "following factor categories:</p>"
            "<ul>"
            "<li><strong>Something you know</strong> – password, PIN, security question.</li>"
            "<li><strong>Something you have</strong> – hardware token (RSA SecurID), smart card, "
            "mobile authenticator app (TOTP/HOTP).</li>"
            "<li><strong>Something you are</strong> – biometrics: fingerprint, retina scan, "
            "facial recognition.</li>"
            "</ul>"
            "<p>MFA dramatically reduces account-takeover risk because a stolen password alone is "
            "insufficient. Two-Factor Authentication (2FA) is the most common MFA implementation. "
            "On Cisco devices, MFA is typically enforced via AAA (RADIUS/TACACS+) integration with "
            "an identity provider.</p>"
            "<p><strong>Single Sign-On (SSO)</strong> allows users to authenticate once and access "
            "multiple services, reducing password fatigue while centralizing authentication controls.</p>"
        ),
        "key_points": [
            "MFA categories: something you know, something you have, something you are.",
            "2FA is a subset of MFA requiring exactly two factors.",
            "Account lockout policies defend against brute-force and dictionary attacks.",
            "NIST 800-63B discourages mandatory periodic password rotation without evidence of compromise.",
            "On Cisco devices, MFA is enforced through AAA integration (RADIUS/TACACS+) with an identity provider.",
            "SSO reduces password fatigue; centralizing auth makes policy enforcement easier.",
        ],
    },
    {
        "domain": 5,
        "topic": "IPsec VPNs",
        "objective": "5.5",
        "video": "IPsec VPNs",
        "study_topics": ["IPsec VPNs"],
        "body": (
            "<p>IPsec (Internet Protocol Security) is a suite of protocols that provides "
            "confidentiality, integrity, and authentication for IP traffic, commonly used to "
            "build site-to-site and remote-access VPNs.</p>"
            "<p><strong>IPsec protocols:</strong></p>"
            "<ul>"
            "<li><strong>AH (Authentication Header, protocol 51)</strong> – provides data integrity "
            "and origin authentication but no encryption. Rarely used alone.</li>"
            "<li><strong>ESP (Encapsulating Security Payload, protocol 50)</strong> – provides "
            "encryption, integrity, and optional authentication. The preferred IPsec protocol.</li>"
            "</ul>"
            "<p><strong>IPsec modes:</strong></p>"
            "<ul>"
            "<li><strong>Transport mode</strong> – encrypts/authenticates only the payload; original "
            "IP header is preserved. Used for host-to-host communication.</li>"
            "<li><strong>Tunnel mode</strong> – encapsulates the entire original IP packet inside a "
            "new IP packet. Standard mode for VPN gateways (site-to-site).</li>"
            "</ul>"
            "<p><strong>IKE (Internet Key Exchange):</strong> Automates the negotiation of security "
            "associations (SAs) and key exchange.</p>"
            "<ul>"
            "<li><strong>IKEv1 Phase 1</strong> – establishes the ISAKMP SA (management channel) "
            "using main mode (6 messages, more secure) or aggressive mode (3 messages, faster but "
            "less secure).</li>"
            "<li><strong>IKEv1 Phase 2</strong> – negotiates the IPsec SA (data channel) using "
            "quick mode.</li>"
            "<li><strong>IKEv2</strong> – simplified exchange, built-in NAT traversal (NAT-T on "
            "UDP 4500), better support for mobility (MOBIKE). Preferred for new deployments.</li>"
            "</ul>"
            "<p><strong>VPN types on CCNA:</strong></p>"
            "<ul>"
            "<li><strong>Site-to-site VPN</strong> – connects two networks permanently via IPsec "
            "tunnel between routers/firewalls. Transparent to end users.</li>"
            "<li><strong>Remote-access VPN</strong> – individual clients connect to the corporate "
            "network using Cisco AnyConnect (SSL/TLS or IKEv2) or legacy IPsec clients.</li>"
            "<li><strong>GRE over IPsec</strong> – GRE tunnels support routing protocols; IPsec "
            "adds encryption since GRE itself provides none.</li>"
            "</ul>"
        ),
        "key_points": [
            "ESP (protocol 50) provides encryption + integrity; AH (protocol 51) provides integrity only.",
            "Tunnel mode wraps the entire original packet — standard for site-to-site VPNs.",
            "Transport mode protects only the payload — used for host-to-host.",
            "IKEv1 uses two phases; IKEv2 is simpler, supports NAT-T (UDP 4500), and is preferred.",
            "Site-to-site VPNs connect networks; remote-access VPNs connect individual users.",
            "GRE over IPsec is needed when routing protocols must traverse an encrypted tunnel.",
        ],
    },
    {
        "domain": 5,
        "topic": "Access control lists (ACLs)",
        "objective": "5.6",
        "video": "ACLs",
        "study_topics": [
            "Access control lists (ACLs)",
            "ACL placement & wildcard masks",
            "Standard vs Extended ACL — number ranges and matching criteria",
        ],
        "body": (
            "<p>Access Control Lists (ACLs) are ordered sets of permit/deny rules applied to "
            "router interfaces to filter traffic. Cisco IOS processes ACL entries top-down and "
            "stops at the first match. Every ACL has an implicit <strong>deny any</strong> at "
            "the end — traffic not explicitly permitted is dropped.</p>"
            "<p><strong>Standard vs Extended ACLs:</strong></p>"
            "<table border='1' cellpadding='4' cellspacing='0'>"
            "<tr><th>Feature</th><th>Standard ACL</th><th>Extended ACL</th></tr>"
            "<tr><td>Number range</td><td>1–99, 1300–1999</td><td>100–199, 2000–2699</td></tr>"
            "<tr><td>Matching criteria</td><td>Source IP address only</td>"
            "<td>Source IP, destination IP, protocol (IP/TCP/UDP/ICMP), source port, dest port "
            "(5-tuple)</td></tr>"
            "<tr><td>Recommended placement</td><td>As close to the destination as possible</td>"
            "<td>As close to the source as possible</td></tr>"
            "<tr><td>Named ACL support</td><td>Yes</td><td>Yes</td></tr>"
            "</table>"
            "<p><strong>Placement rationale:</strong> Standard ACLs match only source IP, so "
            "placing them near the destination prevents blocking traffic to other destinations. "
            "Extended ACLs specify both source and destination, so placing them near the source "
            "stops unwanted traffic early, conserving bandwidth.</p>"
            "<p><strong>Wildcard masks</strong> are the inverse of a subnet mask and tell the "
            "router which bits to ignore when matching an address:</p>"
            "<ul>"
            "<li>Subnet mask <code>255.255.255.0</code> (/24) → wildcard <code>0.0.0.255</code> "
            "(ignore last octet — match any host in the /24).</li>"
            "<li>Subnet mask <code>255.255.255.252</code> (/30) → wildcard <code>0.0.0.3</code>.</li>"
            "<li><code>host 10.1.1.1</code> is shorthand for <code>10.1.1.1 0.0.0.0</code> "
            "(exact match).</li>"
            "<li><code>any</code> is shorthand for <code>0.0.0.0 255.255.255.255</code> "
            "(match everything).</li>"
            "</ul>"
            "<p><strong>Applying ACLs to interfaces:</strong> Use <code>ip access-group "
            "&lt;ACL&gt; in|out</code> on the interface. Only one ACL per direction per interface "
            "is allowed. <em>In</em> filters traffic arriving on the interface; <em>out</em> "
            "filters traffic leaving.</p>"
            "<p><strong>Named ACLs</strong> (<code>ip access-list standard|extended NAME</code>) "
            "allow descriptive names and permit deleting individual entries by sequence number, "
            "which numbered ACLs do not support without rewriting the entire list.</p>"
        ),
        "key_points": [
            "Standard ACL numbers: 1–99 and 1300–1999; match source IP only; place near destination.",
            "Extended ACL numbers: 100–199 and 2000–2699; match full 5-tuple; place near source.",
            "Wildcard mask is the bitwise inverse of the subnet mask — a 0 bit means 'must match', a 1 bit means 'ignore'.",
            "'host x.x.x.x' = wildcard 0.0.0.0; 'any' = wildcard 255.255.255.255.",
            "Implicit deny any at the end of every ACL drops unmatched traffic.",
            "Only one ACL per interface per direction (in or out).",
            "Named ACLs allow deletion of individual entries by sequence number.",
        ],
    },
    {
        "domain": 5,
        "topic": "Port security",
        "objective": "5.7",
        "video": "Port Security",
        "study_topics": ["Port security"],
        "body": (
            "<p>Port security is a Cisco Catalyst switch feature that restricts which MAC addresses "
            "may communicate through a switchport, defending against MAC flooding attacks and "
            "unauthorized device connections.</p>"
            "<p><strong>Configuration requirements:</strong> Port security can only be configured "
            "on access or trunk ports that have been manually set (<code>switchport mode access</code> "
            "or <code>switchport mode trunk</code>). Dynamic/auto ports are not supported.</p>"
            "<p><strong>Key parameters:</strong></p>"
            "<ul>"
            "<li><strong>Maximum MAC addresses</strong> – <code>switchport port-security maximum "
            "&lt;N&gt;</code> sets how many MAC addresses are allowed (default 1).</li>"
            "<li><strong>Allowed MAC addresses</strong> – configured statically with "
            "<code>switchport port-security mac-address &lt;MAC&gt;</code>, or learned dynamically, "
            "or using <strong>sticky</strong>.</li>"
            "<li><strong>Sticky MAC learning</strong> – <code>switchport port-security mac-address "
            "sticky</code> causes the switch to dynamically learn MAC addresses and write them "
            "into the running configuration as static entries, persisting if saved to startup-config.</li>"
            "</ul>"
            "<p><strong>Violation modes</strong> (what happens when an unauthorized MAC is detected):</p>"
            "<table border='1' cellpadding='4' cellspacing='0'>"
            "<tr><th>Mode</th><th>Drops frames?</th><th>Sends syslog/SNMP?</th><th>Shuts port down?</th></tr>"
            "<tr><td><strong>Protect</strong></td><td>Yes</td><td>No</td><td>No</td></tr>"
            "<tr><td><strong>Restrict</strong></td><td>Yes</td><td>Yes</td><td>No</td></tr>"
            "<tr><td><strong>Shutdown</strong> (default)</td><td>Yes</td><td>Yes</td><td>Yes — err-disabled</td></tr>"
            "</table>"
            "<p>When a port enters <strong>err-disabled</strong> state (shutdown violation), it must "
            "be recovered manually (<code>shutdown</code> then <code>no shutdown</code>) or "
            "automatically via <code>errdisable recovery cause psecure-violation</code>.</p>"
            "<p><strong>Verification commands:</strong></p>"
            "<ul>"
            "<li><code>show port-security interface &lt;if&gt;</code> – shows violation mode, "
            "max MACs, current count, and last violation MAC.</li>"
            "<li><code>show port-security address</code> – lists all secure MAC addresses.</li>"
            "</ul>"
        ),
        "key_points": [
            "Port security requires manually configured access or trunk ports — not dynamic.",
            "Default maximum MAC addresses per port is 1.",
            "Sticky MAC learning converts dynamically learned addresses into static entries in the running-config.",
            "Protect: silently drops violations (no logging). Restrict: drops + logs. Shutdown (default): err-disables the port.",
            "An err-disabled port must be manually re-enabled with 'shutdown' then 'no shutdown', or via errdisable recovery.",
            "'show port-security interface' verifies violation mode, max MACs, and last violating MAC address.",
        ],
    },
    {
        "domain": 5,
        "topic": "DHCP snooping & DAI",
        "objective": "5.8",
        "video": "DHCP Snooping and DAI",
        "study_topics": ["DHCP snooping & DAI"],
        "body": (
            "<p><strong>DHCP Snooping</strong> is a Layer 2 security feature that protects against "
            "rogue DHCP servers and DHCP starvation attacks by filtering DHCP messages on "
            "untrusted ports.</p>"
            "<p><strong>How it works:</strong></p>"
            "<ul>"
            "<li>Switch ports are designated as <em>trusted</em> (uplinks to legitimate DHCP servers "
            "or other switches) or <em>untrusted</em> (end-user ports — default).</li>"
            "<li>DHCP server replies (OFFER, ACK, NAK) received on untrusted ports are dropped.</li>"
            "<li>Client messages (DISCOVER, REQUEST) on untrusted ports are rate-limited and "
            "validated — e.g., the source MAC in the Ethernet frame must match the chaddr field "
            "in the DHCP packet.</li>"
            "<li>Builds a <strong>DHCP snooping binding table</strong> (IP ↔ MAC ↔ VLAN ↔ port ↔ "
            "lease time) from observed DHCP ACKs.</li>"
            "</ul>"
            "<p><strong>Configuration:</strong></p>"
            "<ul>"
            "<li><code>ip dhcp snooping</code> – enables globally.</li>"
            "<li><code>ip dhcp snooping vlan &lt;VID&gt;</code> – enables per VLAN.</li>"
            "<li><code>ip dhcp snooping trust</code> – marks an interface as trusted.</li>"
            "<li><code>ip dhcp snooping limit rate &lt;N&gt;</code> – rate-limits DHCP on untrusted ports.</li>"
            "</ul>"
            "<p><strong>Dynamic ARP Inspection (DAI)</strong> uses the DHCP snooping binding table "
            "to validate ARP packets, protecting against ARP poisoning / MitM attacks.</p>"
            "<ul>"
            "<li>On untrusted ports, the switch intercepts ARP requests and replies, checks the "
            "sender IP and MAC against the binding table, and drops invalid ARPs.</li>"
            "<li>Trusted ports (uplinks) bypass DAI inspection.</li>"
            "<li><code>ip arp inspection vlan &lt;VID&gt;</code> – enables DAI per VLAN.</li>"
            "<li><code>ip arp inspection trust</code> – marks an interface as trusted for DAI.</li>"
            "<li>Hosts with static IPs (no DHCP entry) need an explicit ARP ACL for DAI to permit "
            "their traffic.</li>"
            "</ul>"
            "<p>Together, DHCP snooping and DAI form a complementary defense: snooping prevents "
            "fake DHCP servers and builds the binding table; DAI uses that table to stop ARP "
            "spoofing.</p>"
        ),
        "key_points": [
            "DHCP snooping blocks DHCP server messages (OFFER/ACK) on untrusted ports.",
            "DHCP snooping builds a binding table: IP, MAC, VLAN, port, lease time.",
            "Enable globally with 'ip dhcp snooping', then per VLAN with 'ip dhcp snooping vlan'.",
            "DAI validates ARP packets against the DHCP snooping binding table to prevent ARP poisoning.",
            "Both features classify ports as trusted (uplinks) or untrusted (end-user ports).",
            "Static-IP hosts need ARP ACLs to pass DAI validation since they have no binding table entry.",
        ],
    },
    {
        "domain": 5,
        "topic": "AAA (RADIUS vs TACACS+)",
        "objective": "5.9",
        "video": "AAA RADIUS and TACACS+",
        "study_topics": ["AAA (RADIUS vs TACACS+)"],
        "body": (
            "<p><strong>AAA</strong> (Authentication, Authorization, Accounting) is a framework for "
            "controlling access to network resources:</p>"
            "<ul>"
            "<li><strong>Authentication</strong> – verifies who the user is (password/certificate).</li>"
            "<li><strong>Authorization</strong> – determines what the user is allowed to do.</li>"
            "<li><strong>Accounting</strong> – logs what the user did (commands executed, session "
            "duration, bytes transferred).</li>"
            "</ul>"
            "<p><strong>RADIUS vs TACACS+:</strong></p>"
            "<table border='1' cellpadding='4' cellspacing='0'>"
            "<tr><th>Feature</th><th>RADIUS</th><th>TACACS+</th></tr>"
            "<tr><td>Developer</td><td>IETF (open standard)</td><td>Cisco (proprietary)</td></tr>"
            "<tr><td>Transport protocol</td><td>UDP (ports 1812/1813 or 1645/1646)</td>"
            "<td>TCP (port 49)</td></tr>"
            "<tr><td>Payload encryption</td><td>Encrypts the password field only</td>"
            "<td>Encrypts the entire payload</td></tr>"
            "<tr><td>AAA separation</td><td>Combines authentication and authorization</td>"
            "<td>Separates authentication, authorization, and accounting</td></tr>"
            "<tr><td>Primary use case</td><td>Network access (802.1X, VPN, wireless)</td>"
            "<td>Device administration (CLI access to routers/switches)</td></tr>"
            "<tr><td>Multiprotocol support</td><td>Limited</td><td>Full (AppleTalk, IPX, etc.)</td></tr>"
            "</table>"
            "<p><strong>Cisco IOS AAA configuration overview:</strong></p>"
            "<ul>"
            "<li><code>aaa new-model</code> – enables AAA globally (replaces legacy line commands).</li>"
            "<li><code>radius server &lt;NAME&gt;</code> or <code>tacacs server &lt;NAME&gt;</code> "
            "– defines server parameters (address, key).</li>"
            "<li><code>aaa authentication login default group tacacs+ local</code> – tries TACACS+ "
            "first; falls back to local database if server unreachable.</li>"
            "<li><code>aaa authorization exec default group tacacs+ local</code> – controls what "
            "exec privileges are granted.</li>"
            "<li><code>aaa accounting exec default start-stop group tacacs+</code> – logs exec "
            "session start and stop.</li>"
            "</ul>"
            "<p>For enterprise device administration, TACACS+ is preferred because it encrypts "
            "all traffic and provides granular per-command authorization. RADIUS is preferred for "
            "network access authentication (Wi-Fi, VPN, 802.1X).</p>"
        ),
        "key_points": [
            "AAA = Authentication (who?), Authorization (what can they do?), Accounting (what did they do?).",
            "RADIUS uses UDP (1812/1813); encrypts only the password field; combines authn and authz.",
            "TACACS+ uses TCP (49); encrypts the entire payload; separates authn, authz, and accounting.",
            "TACACS+ is Cisco proprietary and preferred for device (CLI) administration.",
            "RADIUS is an open standard preferred for network access control (802.1X, VPN, Wi-Fi).",
            "'aaa new-model' must be enabled before configuring AAA methods on Cisco IOS.",
        ],
    },
    {
        "domain": 5,
        "topic": "Wireless security (WPA2/WPA3)",
        "objective": "5.10",
        "video": "Wireless Security WPA2 and WPA3",
        "study_topics": [
            "Wireless security (WPA2/WPA3)",
            "WPA2 vs WPA3 wireless security features",
        ],
        "body": (
            "<p>Wireless networks are inherently exposed to the open air, making strong encryption "
            "and authentication protocols essential. The Wi-Fi Protected Access (WPA) family "
            "replaced the broken WEP and WPA standards.</p>"
            "<p><strong>WPA2 (802.11i):</strong></p>"
            "<ul>"
            "<li><strong>Encryption</strong>: AES-CCMP (Counter Mode with CBC-MAC Protocol) — "
            "a strong 128-bit block cipher replacing the TKIP stopgap.</li>"
            "<li><strong>Personal mode (WPA2-PSK)</strong>: Uses a pre-shared key (passphrase). "
            "Susceptible to offline dictionary attacks if the 4-way handshake is captured.</li>"
            "<li><strong>Enterprise mode (WPA2-802.1X)</strong>: Each user authenticates with "
            "unique credentials via EAP over RADIUS. More secure; no shared secret.</li>"
            "<li><strong>TKIP</strong>: An older, weaker cipher included for backward compatibility; "
            "deprecated and should not be used.</li>"
            "</ul>"
            "<p><strong>WPA3 (Wi-Fi Alliance, 2018):</strong></p>"
            "<ul>"
            "<li><strong>Personal mode (WPA3-SAE)</strong>: Replaces PSK with Simultaneous "
            "Authentication of Equals (SAE / Dragonfly handshake). Provides forward secrecy and "
            "resistance to offline dictionary attacks — each authentication generates unique "
            "session keys.</li>"
            "<li><strong>Enterprise mode (WPA3-Enterprise)</strong>: Optional 192-bit security "
            "suite using GCMP-256 and SHA-384 for higher-security environments.</li>"
            "<li><strong>OWE (Opportunistic Wireless Encryption)</strong>: Encrypts traffic on "
            "open networks (e.g., coffee shop hotspots) without requiring a password.</li>"
            "<li><strong>Easy Connect (DPP)</strong>: Simplifies onboarding of IoT devices that "
            "lack a keyboard, using QR codes.</li>"
            "</ul>"
            "<p><strong>Comparison summary:</strong></p>"
            "<table border='1' cellpadding='4' cellspacing='0'>"
            "<tr><th>Feature</th><th>WPA2</th><th>WPA3</th></tr>"
            "<tr><td>Personal authentication</td><td>PSK (passphrase)</td><td>SAE (Dragonfly)</td></tr>"
            "<tr><td>Forward secrecy</td><td>No</td><td>Yes</td></tr>"
            "<tr><td>Encryption (personal)</td><td>AES-CCMP (128-bit)</td><td>AES-CCMP (128-bit)</td></tr>"
            "<tr><td>Offline dictionary attack resistance</td><td>No</td><td>Yes</td></tr>"
            "<tr><td>Open network encryption</td><td>No</td><td>Yes (OWE)</td></tr>"
            "<tr><td>Enterprise max security</td><td>128-bit AES</td><td>192-bit GCMP-256</td></tr>"
            "</table>"
            "<p>For the CCNA exam, know that WPA2-Enterprise uses 802.1X/EAP with RADIUS, and "
            "WPA3-Personal uses SAE instead of PSK to prevent offline attacks.</p>"
        ),
        "key_points": [
            "WPA2 personal uses PSK; WPA2 enterprise uses 802.1X/EAP with RADIUS.",
            "WPA2 encrypts with AES-CCMP (128-bit); TKIP is deprecated.",
            "WPA3 personal replaces PSK with SAE (Dragonfly), providing forward secrecy and offline-attack resistance.",
            "WPA3 enterprise supports optional 192-bit (GCMP-256) security mode.",
            "OWE (WPA3) encrypts traffic on open/public networks without a password.",
            "WPA2-PSK is vulnerable to offline dictionary attacks if the 4-way handshake is captured.",
        ],
    },
    {
        "domain": 5,
        "topic": "SSH configuration steps on a Cisco IOS router",
        "objective": "5.11",
        "video": "SSH Configuration",
        "study_topics": ["SSH configuration steps on a Cisco IOS router"],
        "body": (
            "<p>Telnet sends all data — including passwords — in plaintext. SSH (Secure Shell) "
            "provides encrypted remote management and should replace Telnet on all Cisco devices. "
            "SSH version 2 is strongly preferred over SSHv1 due to improved security.</p>"
            "<p><strong>SSH configuration steps (in order):</strong></p>"
            "<ol>"
            "<li><strong>Set the hostname</strong> (required for key generation):<br>"
            "<code>hostname R1</code></li>"
            "<li><strong>Set the IP domain name</strong> (used with hostname to create the RSA "
            "key label):<br>"
            "<code>ip domain-name example.com</code></li>"
            "<li><strong>Generate the RSA key pair</strong> (minimum 1024 bits; 2048 recommended "
            "for SSHv2):<br>"
            "<code>crypto key generate rsa modulus 2048</code></li>"
            "<li><strong>Force SSHv2</strong> (optional but recommended):<br>"
            "<code>ip ssh version 2</code></li>"
            "<li><strong>Create a local user account</strong> (required if using <code>login local</code>):<br>"
            "<code>username admin privilege 15 secret StrongPass1!</code></li>"
            "<li><strong>Configure VTY lines</strong>:<br>"
            "<code>line vty 0 4</code><br>"
            "<code>&nbsp;login local</code> — authenticate using the local username database.<br>"
            "<code>&nbsp;transport input ssh</code> — permit SSH only (blocks Telnet).</li>"
            "</ol>"
            "<p><strong>Optional but useful SSH hardening:</strong></p>"
            "<ul>"
            "<li><code>ip ssh authentication-retries 3</code> – limit failed login attempts.</li>"
            "<li><code>ip ssh time-out 60</code> – disconnect unauthenticated sessions after "
            "60 seconds.</li>"
            "<li><code>access-class &lt;ACL&gt; in</code> on VTY lines – restrict SSH access "
            "to specific source IPs.</li>"
            "</ul>"
            "<p><strong>Verification:</strong></p>"
            "<ul>"
            "<li><code>show ip ssh</code> – confirms SSH version, timeout, and authentication "
            "retry settings.</li>"
            "<li><code>show ssh</code> – lists active SSH sessions.</li>"
            "<li><code>show crypto key mypubkey rsa</code> – displays the generated RSA key.</li>"
            "</ul>"
            "<p><strong>Key requirement:</strong> Both a hostname (other than the default "
            "\"Router\") and an IP domain name must be set before <code>crypto key generate rsa</code> "
            "will succeed, because the key label is formed as <em>hostname.domain-name</em>.</p>"
        ),
        "key_points": [
            "SSH requires a hostname and IP domain name before 'crypto key generate rsa' will work.",
            "Use 'crypto key generate rsa modulus 2048' — 2048-bit key is required for SSHv2.",
            "'ip ssh version 2' forces SSHv2 only.",
            "On VTY lines: 'login local' uses the local user database; 'transport input ssh' blocks Telnet.",
            "'show ip ssh' verifies SSH is enabled and shows the configured version.",
            "Apply an access-class ACL on VTY lines to restrict management access to known IP addresses.",
        ],
    },
]

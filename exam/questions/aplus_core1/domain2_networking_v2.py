QUESTIONS = [
    # ── 2.1  Ports & Protocols ──────────────────────────────────────────────
    {
        "id": "a1d2v2-001",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Ports & protocols",
        "stem": (
            "A technician captures traffic on a corporate network and observes unencrypted "
            "file transfers on TCP 21. Management wants to replace this with an encrypted "
            "alternative that still uses the FTP command structure but tunnels it through SSH. "
            "Which protocol and default port should replace it?"
        ),
        "options": [
            {
                "id": "a",
                "text": "SFTP on TCP 22",
                "correct": True,
                "rationale": (
                    "Correct. SFTP (SSH File Transfer Protocol) is a completely independent "
                    "protocol that runs over an SSH session on TCP 22. It provides encrypted "
                    "file transfer and is the direct encrypted replacement for FTP when an "
                    "SSH-based channel is required."
                ),
            },
            {
                "id": "b",
                "text": "FTPS on TCP 990",
                "correct": False,
                "rationale": (
                    "Incorrect. FTPS (FTP Secure) adds TLS/SSL encryption to FTP on TCP 990 "
                    "(implicit) or TCP 21 (explicit). While it encrypts FTP, it does NOT tunnel "
                    "FTP through SSH — it uses TLS, not SSH, for its encryption layer."
                ),
            },
            {
                "id": "c",
                "text": "TFTP on UDP 69",
                "correct": False,
                "rationale": (
                    "Incorrect. TFTP (Trivial File Transfer Protocol) on UDP 69 provides a "
                    "simplified, unauthenticated file transfer and offers no encryption whatsoever. "
                    "It is not a replacement for FTP in secure contexts."
                ),
            },
            {
                "id": "d",
                "text": "SCP on TCP 443",
                "correct": False,
                "rationale": (
                    "Incorrect. SCP (Secure Copy Protocol) does use SSH, but it runs on TCP 22, "
                    "not TCP 443. TCP 443 is HTTPS. Additionally, SCP uses a simpler shell-level "
                    "copy mechanism rather than FTP's command structure."
                ),
            },
        ],
        "explanation": (
            "SFTP (SSH File Transfer Protocol) uses TCP 22 and provides fully encrypted file "
            "transfer over an SSH session. It is unrelated to FTP at the protocol level, despite "
            "the name similarity. FTPS adds TLS to FTP (TCP 21 or 990) and is an alternative, "
            "but uses TLS not SSH. TFTP (UDP 69) has no security features whatsoever."
        ),
    },
    {
        "id": "a1d2v2-002",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Ports & protocols",
        "stem": (
            "An administrator is configuring a Windows server to allow centralized "
            "authentication against an Active Directory domain using LDAP over TLS (LDAPS). "
            "The firewall must be updated to allow this traffic. Which port should be opened?"
        ),
        "options": [
            {
                "id": "a",
                "text": "TCP 636",
                "correct": True,
                "rationale": (
                    "Correct. LDAPS (LDAP over SSL/TLS) uses TCP 636 for encrypted directory "
                    "service queries. Standard unencrypted LDAP uses TCP 389."
                ),
            },
            {
                "id": "b",
                "text": "TCP 389",
                "correct": False,
                "rationale": (
                    "Incorrect. TCP 389 is standard unencrypted LDAP. The question specifically "
                    "asks for LDAPS (LDAP over TLS), which runs on TCP 636."
                ),
            },
            {
                "id": "c",
                "text": "TCP 443",
                "correct": False,
                "rationale": (
                    "Incorrect. TCP 443 is HTTPS (HTTP over TLS). While both LDAPS and HTTPS "
                    "use TLS encryption, they are separate protocols on separate ports."
                ),
            },
            {
                "id": "d",
                "text": "UDP 88",
                "correct": False,
                "rationale": (
                    "Incorrect. UDP 88 is Kerberos, the authentication protocol used alongside "
                    "LDAP in Active Directory. It is not the port for LDAPS."
                ),
            },
        ],
        "explanation": (
            "LDAP port reference: TCP 389 = standard LDAP (cleartext); TCP 636 = LDAPS "
            "(LDAP over TLS, encrypted). UDP 88 is Kerberos authentication. TCP 443 is "
            "HTTPS. In Active Directory environments, LDAP is used for directory lookups "
            "while Kerberos handles ticket-based authentication."
        ),
    },
    {
        "id": "a1d2v2-003",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Ports & protocols",
        "stem": (
            "A penetration tester scans an internal host and finds TCP 3389 open and "
            "accepting connections. The client machines on this network are Windows 10 "
            "workstations. Which service is almost certainly running, and what is the "
            "PRIMARY security risk of exposing this port directly to the internet?"
        ),
        "options": [
            {
                "id": "a",
                "text": "RDP (Remote Desktop Protocol); brute-force credential attacks and exploitation of RDP vulnerabilities such as BlueKeep",
                "correct": True,
                "rationale": (
                    "Correct. TCP 3389 is RDP. Exposing RDP directly to the internet invites "
                    "automated brute-force attacks against user credentials and targeted "
                    "exploitation of RDP vulnerabilities (e.g., CVE-2019-0708 'BlueKeep'). "
                    "RDP should be placed behind a VPN or RDP Gateway, not exposed publicly."
                ),
            },
            {
                "id": "b",
                "text": "HTTPS; session hijacking due to weak TLS cipher suites",
                "correct": False,
                "rationale": (
                    "Incorrect. HTTPS uses TCP 443, not TCP 3389. Session hijacking of web "
                    "sessions is a web application threat unrelated to the port identified."
                ),
            },
            {
                "id": "c",
                "text": "SSH; password sniffing because SSH version 1 transmits in cleartext",
                "correct": False,
                "rationale": (
                    "Incorrect. SSH uses TCP 22, not TCP 3389. Additionally, SSH encrypts "
                    "all traffic and does not transmit passwords in cleartext in any version."
                ),
            },
            {
                "id": "d",
                "text": "VNC; denial-of-service because VNC consumes excessive bandwidth",
                "correct": False,
                "rationale": (
                    "Incorrect. VNC commonly uses TCP 5900. TCP 3389 is specific to Microsoft "
                    "RDP. Bandwidth consumption is not the primary security risk for an "
                    "exposed remote access port."
                ),
            },
        ],
        "explanation": (
            "TCP 3389 is Microsoft RDP (Remote Desktop Protocol). Exposing RDP directly to "
            "the internet is a well-known attack vector. Attackers scan for open port 3389, "
            "then attempt credential brute force or exploit RDP vulnerabilities. Best "
            "practice: restrict RDP to VPN-connected users only, use Network Level "
            "Authentication (NLA), and enable account lockout policies."
        ),
    },
    {
        "id": "a1d2v2-004",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Ports & protocols",
        "stem": (
            "A sysadmin configures a network device to forward authentication requests "
            "to a centralized server that validates user credentials and returns access "
            "policies. The protocol used must encrypt the entire payload and is commonly "
            "used with Cisco routers and switches for AAA (Authentication, Authorization, "
            "and Accounting). Which protocol and port does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "TACACS+ on TCP 49",
                "correct": True,
                "rationale": (
                    "Correct. TACACS+ (Terminal Access Controller Access Control System Plus) "
                    "uses TCP 49 and encrypts the entire packet payload. It is Cisco's preferred "
                    "AAA protocol for managing access to network device CLIs."
                ),
            },
            {
                "id": "b",
                "text": "RADIUS on UDP 1812/1813",
                "correct": False,
                "rationale": (
                    "Incorrect. RADIUS uses UDP 1812 (authentication) and 1813 (accounting). "
                    "It encrypts only the password field, not the entire packet, making it less "
                    "secure than TACACS+ for device administration. RADIUS is more commonly "
                    "used for network access (Wi-Fi, VPN) authentication."
                ),
            },
            {
                "id": "c",
                "text": "Kerberos on UDP 88",
                "correct": False,
                "rationale": (
                    "Incorrect. Kerberos on UDP 88 is the ticket-based authentication protocol "
                    "used in Microsoft Active Directory and MIT Kerberos environments. It is not "
                    "used for Cisco device AAA."
                ),
            },
            {
                "id": "d",
                "text": "LDAP on TCP 389",
                "correct": False,
                "rationale": (
                    "Incorrect. LDAP on TCP 389 is a directory service query protocol, not an "
                    "AAA framework for network device authentication. It does not provide "
                    "the authorization and accounting functions described."
                ),
            },
        ],
        "explanation": (
            "TACACS+ (TCP 49) vs. RADIUS (UDP 1812/1813): TACACS+ encrypts the full body "
            "of every packet and separates authentication, authorization, and accounting into "
            "independent transactions — preferred for managing network device (router/switch) "
            "CLI access. RADIUS encrypts only the password and combines authentication and "
            "authorization — preferred for network access control (VPN, 802.1X Wi-Fi)."
        ),
    },
    {
        "id": "a1d2v2-005",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Ports & protocols",
        "stem": (
            "A web developer is troubleshooting why a browser is being redirected from "
            "http://www.shop.example.com to https://www.shop.example.com automatically. "
            "The initial HTTP request goes to a well-known port, and the HTTPS connection "
            "uses a different well-known port. Which two ports are involved in this redirect?"
        ),
        "options": [
            {
                "id": "a",
                "text": "TCP 80 (HTTP) redirected to TCP 443 (HTTPS)",
                "correct": True,
                "rationale": (
                    "Correct. HTTP uses TCP 80; HTTPS uses TCP 443. The server receives the "
                    "unencrypted request on TCP 80, responds with a 301/302 redirect to the "
                    "HTTPS URL, and the browser reconnects on TCP 443."
                ),
            },
            {
                "id": "b",
                "text": "TCP 8080 (HTTP alternate) redirected to TCP 8443 (HTTPS alternate)",
                "correct": False,
                "rationale": (
                    "Incorrect. TCP 8080 and 8443 are common alternate/development ports for "
                    "HTTP and HTTPS respectively, but they are not the well-known (IANA default) "
                    "ports for these protocols."
                ),
            },
            {
                "id": "c",
                "text": "UDP 80 (HTTP) redirected to UDP 443 (HTTPS)",
                "correct": False,
                "rationale": (
                    "Incorrect. HTTP and HTTPS use TCP, not UDP. While HTTP/3 uses QUIC over "
                    "UDP 443, traditional HTTP/1.1 and HTTP/2 use TCP. The scenario describes "
                    "a standard web redirect."
                ),
            },
            {
                "id": "d",
                "text": "TCP 21 (FTP) redirected to TCP 22 (SFTP)",
                "correct": False,
                "rationale": (
                    "Incorrect. TCP 21 is FTP and TCP 22 is SSH/SFTP. These are file transfer "
                    "protocols, not web browser protocols. A browser HTTP-to-HTTPS redirect "
                    "involves ports 80 and 443."
                ),
            },
        ],
        "explanation": (
            "HTTP = TCP 80; HTTPS = TCP 443. An HTTP-to-HTTPS redirect (HSTS or server-side "
            "redirect) is one of the most common web security implementations. The server "
            "listens on TCP 80, receives the initial request, and returns a redirect response "
            "pointing the browser to the same URL with https://, which connects on TCP 443."
        ),
    },
    {
        "id": "a1d2v2-006",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Ports & protocols",
        "stem": (
            "A network administrator configures a TFTP server to deploy OS images to "
            "network devices via PXE boot. A firewall between the TFTP server and clients "
            "must be updated. TFTP uses a well-known port for the initial request, "
            "then negotiates a data port. Which initial port and transport does TFTP use?"
        ),
        "options": [
            {
                "id": "a",
                "text": "UDP 69",
                "correct": True,
                "rationale": (
                    "Correct. TFTP (Trivial File Transfer Protocol) uses UDP 69 for the initial "
                    "connection request. After the request, both client and server use "
                    "randomly negotiated ephemeral UDP ports for the data transfer."
                ),
            },
            {
                "id": "b",
                "text": "TCP 69",
                "correct": False,
                "rationale": (
                    "Incorrect. TFTP uses UDP, not TCP. Its design intentionally omits the "
                    "overhead of TCP (no connection handshake, no acknowledgment of delivery "
                    "at the transport layer) to remain simple and lightweight."
                ),
            },
            {
                "id": "c",
                "text": "TCP 21",
                "correct": False,
                "rationale": (
                    "Incorrect. TCP 21 is the FTP control channel. FTP is a full-featured "
                    "file transfer protocol with authentication. TFTP is a separate, simpler, "
                    "unauthenticated protocol that uses UDP 69."
                ),
            },
            {
                "id": "d",
                "text": "UDP 161",
                "correct": False,
                "rationale": (
                    "Incorrect. UDP 161 is the SNMP agent port used for network monitoring "
                    "polls, not file transfers. TFTP uses UDP 69."
                ),
            },
        ],
        "explanation": (
            "TFTP (Trivial File Transfer Protocol) uses UDP 69 for initial requests. It is "
            "a minimal, unauthenticated protocol used for bootstrapping — PXE boot, network "
            "device firmware/config transfer, and VoIP phone provisioning. After the server "
            "receives a request on UDP 69, subsequent data blocks are exchanged on dynamically "
            "allocated UDP ports. Because TFTP lacks authentication, it must be restricted to "
            "trusted network segments."
        ),
    },
    # ── 2.2  Networking Hardware ────────────────────────────────────────────
    {
        "id": "a1d2v2-007",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Networking hardware",
        "stem": (
            "A technician notices that two switches connected by two redundant links are "
            "causing broadcast storms that bring the entire network down. No configuration "
            "changes were made to the switches. Which protocol, when enabled, would prevent "
            "the loops while preserving redundancy?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Spanning Tree Protocol (STP / IEEE 802.1D)",
                "correct": True,
                "rationale": (
                    "Correct. STP (IEEE 802.1D) and its faster successor RSTP (802.1W) detect "
                    "Layer 2 loops among switches and logically block one of the redundant "
                    "ports, eliminating the loop while keeping the link available for failover."
                ),
            },
            {
                "id": "b",
                "text": "OSPF (Open Shortest Path First)",
                "correct": False,
                "rationale": (
                    "Incorrect. OSPF is a Layer 3 dynamic routing protocol that selects optimal "
                    "routes between routers. It does not operate at Layer 2 and cannot prevent "
                    "Layer 2 broadcast storms caused by switch loops."
                ),
            },
            {
                "id": "c",
                "text": "VLAN trunking with 802.1Q",
                "correct": False,
                "rationale": (
                    "Incorrect. 802.1Q VLAN tagging on trunk links does not prevent Layer 2 "
                    "loops. Without STP, a loop between trunk-connected switches will still "
                    "cause a broadcast storm in each VLAN."
                ),
            },
            {
                "id": "d",
                "text": "LACP (Link Aggregation Control Protocol)",
                "correct": False,
                "rationale": (
                    "Incorrect. LACP (IEEE 802.3ad) bonds multiple physical links into a single "
                    "logical link for increased bandwidth. It does not prevent loops in "
                    "topologies where links connect different switch pairs in a ring."
                ),
            },
        ],
        "explanation": (
            "STP (IEEE 802.1D) and RSTP (802.1W) are Layer 2 protocols that use a root-bridge "
            "election and port state machine (blocking, listening, learning, forwarding) to "
            "eliminate loops in switched networks. Without STP, redundant switch links create "
            "endless broadcast frame circulation that saturates all links — a broadcast storm. "
            "Modern networks prefer RSTP (sub-second convergence) or MSTP for VLAN-aware loop "
            "prevention."
        ),
    },
    {
        "id": "a1d2v2-008",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Networking hardware",
        "stem": (
            "A network engineer needs to connect two buildings 300 meters apart. Copper "
            "Ethernet is limited to 100 meters per segment. The buildings already have "
            "existing single-mode fiber runs. Which device installed at each building "
            "end would allow the Ethernet switches to communicate over the fiber without "
            "replacing the switches?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Fiber media converter (copper-to-fiber Ethernet converter)",
                "correct": True,
                "rationale": (
                    "Correct. A media converter (also called a fiber-to-Ethernet converter) "
                    "transparently converts 100BASE-TX or 1000BASE-T copper Ethernet to fiber "
                    "optic signals (100BASE-FX or 1000BASE-LX), allowing existing copper-port "
                    "switches to communicate over the fiber run."
                ),
            },
            {
                "id": "b",
                "text": "PoE injector",
                "correct": False,
                "rationale": (
                    "Incorrect. A PoE injector adds electrical power to a copper Ethernet cable "
                    "for powered devices like IP cameras and phones. It does not convert copper "
                    "Ethernet to fiber optic signals."
                ),
            },
            {
                "id": "c",
                "text": "Wireless bridge (802.11 point-to-point link)",
                "correct": False,
                "rationale": (
                    "Incorrect. A wireless bridge would provide inter-building connectivity "
                    "without physical cabling, but the scenario states existing fiber runs are "
                    "already in place. A media converter is the correct solution for utilizing "
                    "installed fiber infrastructure."
                ),
            },
            {
                "id": "d",
                "text": "Patch panel with Cat 6a cable run across buildings",
                "correct": False,
                "rationale": (
                    "Incorrect. Cat 6a supports a maximum of 100 meters per Ethernet segment. "
                    "A 300-meter copper run would exceed this limit and result in signal "
                    "degradation. The fiber runs already in place are the correct medium."
                ),
            },
        ],
        "explanation": (
            "Media converters extend Ethernet beyond the 100-meter copper limit by converting "
            "electrical Ethernet signals to optical signals for transmission over multimode or "
            "single-mode fiber. A pair of media converters (one at each end) allows existing "
            "copper-port switches to interconnect over fiber without hardware upgrades. "
            "Single-mode fiber can extend Ethernet 10 km or more with appropriate transceivers."
        ),
    },
    {
        "id": "a1d2v2-009",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Networking hardware",
        "stem": (
            "A managed switch port shows an amber/orange link LED instead of the expected "
            "green. Devices connected to this port experience intermittent connectivity. "
            "A cable tester confirms the cable is good. The switch CLI shows the port "
            "negotiated 10 Mbps half-duplex instead of the expected 100 Mbps full-duplex. "
            "What is the MOST likely cause of the duplex/speed mismatch?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The connected device NIC has its speed/duplex manually set to a fixed value that does not match the switch port's auto-negotiation",
                "correct": True,
                "rationale": (
                    "Correct. A duplex mismatch most commonly occurs when one end is manually "
                    "set (hard-coded) and the other uses auto-negotiation. Auto-negotiating "
                    "to a fixed-duplex partner defaults to half-duplex per IEEE 802.3 spec, "
                    "causing collisions and poor performance at 100 Mbps."
                ),
            },
            {
                "id": "b",
                "text": "The switch port needs to be upgraded from Fast Ethernet to Gigabit Ethernet",
                "correct": False,
                "rationale": (
                    "Incorrect. The symptom is a duplex mismatch at 10 Mbps half-duplex. "
                    "Upgrading to Gigabit Ethernet would not resolve a duplex mismatch caused "
                    "by a mis-configured NIC."
                ),
            },
            {
                "id": "c",
                "text": "The switch is forwarding frames using store-and-forward mode instead of cut-through mode",
                "correct": False,
                "rationale": (
                    "Incorrect. Switching mode (store-and-forward vs. cut-through) affects "
                    "latency slightly but does not cause a speed/duplex negotiation failure "
                    "or produce the amber LED indication."
                ),
            },
            {
                "id": "d",
                "text": "The VLAN assignment on the port is incorrect, causing inter-VLAN routing failures",
                "correct": False,
                "rationale": (
                    "Incorrect. An incorrect VLAN assignment affects which broadcast domain "
                    "the port belongs to and would cause routing failures, not a 10 Mbps "
                    "half-duplex speed/duplex negotiation result."
                ),
            },
        ],
        "explanation": (
            "A duplex mismatch (one end full-duplex, the other half-duplex) is a classic "
            "symptom of mixing hard-coded NIC/port settings with auto-negotiation. IEEE 802.3 "
            "specifies that when auto-negotiation is used and the partner does not respond with "
            "an advertisement, the port falls back to 10 Mbps half-duplex (or 100 Mbps half "
            "if parallel detection senses 100). Best practice: either set both ends to "
            "auto-negotiate or hard-code the same speed/duplex on both ends."
        ),
    },
    # ── 2.3  PoE ───────────────────────────────────────────────────────────
    {
        "id": "a1d2v2-010",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "PoE",
        "stem": (
            "A network engineer is deploying 802.3bt Type 3 (PoE++) capable access points "
            "throughout a conference center. Each AP requires 51 W of power. The planned "
            "PoE switch has 24 ports with a total PoE power budget of 740 W. How many APs "
            "can be powered simultaneously before the switch's PoE budget is exhausted?"
        ),
        "options": [
            {
                "id": "a",
                "text": "14 APs",
                "correct": True,
                "rationale": (
                    "Correct. 740 W ÷ 51 W per AP = 14.5, which means 14 APs can be fully "
                    "powered before exceeding the 740 W budget. A 15th AP would require "
                    "765 W total, exceeding the budget."
                ),
            },
            {
                "id": "b",
                "text": "24 APs",
                "correct": False,
                "rationale": (
                    "Incorrect. Powering all 24 ports at 51 W each would require 1,224 W, "
                    "which far exceeds the 740 W PoE budget. Port count does not equal "
                    "simultaneous PoE port availability."
                ),
            },
            {
                "id": "c",
                "text": "48 APs",
                "correct": False,
                "rationale": (
                    "Incorrect. 48 is not achievable with a 24-port switch and far exceeds "
                    "what a 740 W budget could support. This answer ignores both port count "
                    "and power budget constraints."
                ),
            },
            {
                "id": "d",
                "text": "12 APs",
                "correct": False,
                "rationale": (
                    "Incorrect. 12 APs × 51 W = 612 W, leaving 128 W of unused budget. "
                    "The correct calculation allows for 14 APs (14 × 51 = 714 W), "
                    "remaining within the 740 W limit."
                ),
            },
        ],
        "explanation": (
            "PoE budget calculation: Divide the total switch PoE watt budget by the per-port "
            "watt requirement of each powered device. 740 ÷ 51 = 14.5, rounded down = 14. "
            "IEEE 802.3bt (PoE++) Type 3 supports up to 60 W at the switch port; Type 4 "
            "supports up to 100 W. Always account for cable loss — the device receives "
            "slightly less than what the port supplies. Oversubscribing a PoE budget causes "
            "devices to power off unpredictably."
        ),
    },
    # ── 2.3  Wireless Standards ──────────────────────────────────────────────
    {
        "id": "a1d2v2-011",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Wireless standards",
        "stem": (
            "A warehouse environment uses battery-powered IoT inventory sensors that "
            "transmit small data packets every 30 minutes. The network team wants a "
            "low-power, mesh-capable wireless standard that can support hundreds of "
            "sensors on a single coordinator at ranges of 10–100 meters. Which technology "
            "is MOST appropriate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Zigbee (IEEE 802.15.4)",
                "correct": True,
                "rationale": (
                    "Correct. Zigbee (IEEE 802.15.4) is a low-power, low-data-rate mesh "
                    "networking protocol designed for IoT and sensor networks. It supports "
                    "mesh topologies with hundreds of nodes, operates at 2.4 GHz, and is "
                    "optimized for battery-powered devices with infrequent transmissions."
                ),
            },
            {
                "id": "b",
                "text": "802.11ax (Wi-Fi 6)",
                "correct": False,
                "rationale": (
                    "Incorrect. Wi-Fi 6 is designed for high-throughput client devices. "
                    "Its power consumption, complexity, and cost are far higher than needed "
                    "for simple IoT sensors transmitting small packets every 30 minutes."
                ),
            },
            {
                "id": "c",
                "text": "Bluetooth Classic (IEEE 802.15.1)",
                "correct": False,
                "rationale": (
                    "Incorrect. Bluetooth Classic is designed for point-to-point or small "
                    "piconet connections (up to 7 active slaves) with moderate power use. "
                    "It does not support large-scale mesh networks of hundreds of nodes."
                ),
            },
            {
                "id": "d",
                "text": "LTE (4G cellular)",
                "correct": False,
                "rationale": (
                    "Incorrect. LTE requires a carrier SIM, cellular infrastructure, and "
                    "ongoing data plan costs. It consumes significantly more power than Zigbee "
                    "and is not appropriate for hundreds of in-building IoT sensors."
                ),
            },
        ],
        "explanation": (
            "Zigbee (IEEE 802.15.4) is the standard choice for low-power, low-data-rate IoT "
            "mesh networks — think smart home sensors, industrial IoT, and warehouse inventory "
            "systems. It uses 2.4 GHz, supports mesh routing (up to ~65,000 nodes theoretically), "
            "and has ultra-low sleep-mode power draw for battery longevity. Z-Wave is a "
            "competing low-power mesh standard at 908 MHz (US). Bluetooth LE/Mesh is another "
            "option but Zigbee has broader industrial IoT adoption for sensor networks."
        ),
    },
    {
        "id": "a1d2v2-012",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Wireless standards",
        "stem": (
            "An 802.11ax access point is deployed in a dense apartment building. Residents "
            "on the same floor report slower Wi-Fi speeds even though signal strength is "
            "excellent. Analysis shows multiple neighboring APs using the same 5 GHz channel. "
            "Which 802.11ax feature reduces performance degradation caused by transmissions "
            "from overlapping neighboring BSS (Basic Service Sets) on the same channel?"
        ),
        "options": [
            {
                "id": "a",
                "text": "BSS Coloring",
                "correct": True,
                "rationale": (
                    "Correct. BSS Coloring (introduced in 802.11ax) assigns a color identifier "
                    "to each BSS. Devices can distinguish between frames from their own BSS "
                    "and frames from a neighboring BSS on the same channel, allowing spatial "
                    "reuse — devices can transmit simultaneously when the interfering signal "
                    "is from a different BSS color."
                ),
            },
            {
                "id": "b",
                "text": "Beamforming",
                "correct": False,
                "rationale": (
                    "Incorrect. Beamforming directs the antenna signal toward a specific client "
                    "to improve SNR for that client. While it reduces signal spread to "
                    "unintended directions, it does not specifically address co-channel "
                    "interference from neighboring BSSs."
                ),
            },
            {
                "id": "c",
                "text": "MIMO (Multiple Input, Multiple Output)",
                "correct": False,
                "rationale": (
                    "Incorrect. MIMO uses multiple antennas to increase throughput and reliability "
                    "for individual clients. It does not address co-channel interference or "
                    "differentiate signals from neighboring access points."
                ),
            },
            {
                "id": "d",
                "text": "WPA3 SAE (Simultaneous Authentication of Equals)",
                "correct": False,
                "rationale": (
                    "Incorrect. WPA3 SAE is a security protocol improvement for authentication, "
                    "replacing PSK handshakes. It is a security feature, not a radio frequency "
                    "management or interference mitigation feature."
                ),
            },
        ],
        "explanation": (
            "BSS Coloring is an 802.11ax (Wi-Fi 6) feature that marks each Basic Service Set "
            "with a 6-bit 'color' in every frame. When a station detects a frame with a "
            "different BSS color, it can assess the RSSI level and — if below a threshold — "
            "treat it as spatial reuse and transmit concurrently rather than deferring. "
            "This significantly improves efficiency in dense deployments where co-channel "
            "interference from neighboring APs was a major bottleneck in previous standards."
        ),
    },
    {
        "id": "a1d2v2-013",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Wi-Fi channels & frequencies",
        "stem": (
            "A wireless administrator notices that the 5 GHz access point on channel 100 "
            "occasionally drops all clients for approximately 60 seconds before reconnecting "
            "them on a different channel. The AP and clients are all functioning correctly "
            "with no hardware faults. What is the MOST likely cause of this behavior?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Dynamic Frequency Selection (DFS) — the AP detected radar and vacated the channel as required by regulation",
                "correct": True,
                "rationale": (
                    "Correct. Channel 100 is a DFS channel (U-NII-2e). Regulations require "
                    "Wi-Fi APs on DFS channels to monitor for radar signals and vacate the "
                    "channel within 10 seconds if radar is detected. The AP then selects a "
                    "new channel, causing a client re-association period of up to 60 seconds."
                ),
            },
            {
                "id": "b",
                "text": "Channel 100 is not legal for 5 GHz Wi-Fi use in the United States",
                "correct": False,
                "rationale": (
                    "Incorrect. Channel 100 is a legal 5 GHz channel in the US (UNII-2e band). "
                    "It is subject to DFS requirements but is not prohibited."
                ),
            },
            {
                "id": "c",
                "text": "The AP's WPA2 TKIP cipher is causing periodic re-keying disconnections",
                "correct": False,
                "rationale": (
                    "Incorrect. WPA2 TKIP re-keying occurs in the background and does not cause "
                    "all clients to disconnect for 60 seconds. The 60-second channel change "
                    "pattern is characteristic of DFS radar detection, not cipher re-keying."
                ),
            },
            {
                "id": "d",
                "text": "The 5 GHz channel 100 overlaps with 2.4 GHz channels, causing periodic interference",
                "correct": False,
                "rationale": (
                    "Incorrect. The 5 GHz and 2.4 GHz bands are completely separate frequency "
                    "ranges with no overlap. Channel 100 (5.500 GHz) cannot overlap with any "
                    "2.4 GHz channels."
                ),
            },
        ],
        "explanation": (
            "DFS (Dynamic Frequency Selection) is mandated by the FCC and other regulators on "
            "UNII-2 (52-64) and UNII-2e (100-140) channels to protect airport, weather, and "
            "military radar systems. When an AP detects a radar pulse pattern, it must vacate "
            "the channel within 10 seconds (Channel Move Time) and avoid it for 30 minutes "
            "(Non-Occupancy Period). This triggers a client outage as the AP switches channels "
            "and clients must re-associate. To avoid this, use non-DFS channels (UNII-1 or "
            "UNII-3: 36-48, 149-165) in radar-dense environments like airports."
        ),
    },
    {
        "id": "a1d2v2-014",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Wireless standards",
        "stem": (
            "A project manager's new laptop has a Bluetooth 5.0 adapter and needs to "
            "wirelessly connect a keyboard, mouse, and headset simultaneously. The "
            "manager is concerned about the reliable transmission range. What is the "
            "approximate maximum operating range for a typical Bluetooth Class 2 device?"
        ),
        "options": [
            {
                "id": "a",
                "text": "10 meters",
                "correct": True,
                "rationale": (
                    "Correct. Bluetooth Class 2 devices (most consumer peripherals: keyboards, "
                    "mice, headsets) are limited to approximately 10 meters (33 feet) range. "
                    "Class 1 devices can reach up to 100 meters; Class 3 is limited to ~1 meter."
                ),
            },
            {
                "id": "b",
                "text": "100 meters",
                "correct": False,
                "rationale": (
                    "Incorrect. 100 meters is the Class 1 Bluetooth range (used in industrial "
                    "and specialized equipment with higher transmit power). Standard consumer "
                    "peripherals use Class 2 at approximately 10 meters."
                ),
            },
            {
                "id": "c",
                "text": "1 meter",
                "correct": False,
                "rationale": (
                    "Incorrect. 1 meter is the Class 3 Bluetooth range, used in devices "
                    "requiring extremely short-range proximity operation. Consumer peripherals "
                    "are Class 2 (~10 m)."
                ),
            },
            {
                "id": "d",
                "text": "300 meters",
                "correct": False,
                "rationale": (
                    "Incorrect. 300 meters far exceeds any standard Bluetooth class range. "
                    "While Bluetooth 5.0 improved range in Long Range mode, typical Class 2 "
                    "consumer peripherals operate within 10 meters under normal conditions."
                ),
            },
        ],
        "explanation": (
            "Bluetooth power class ranges: Class 1 = up to 100 mW, ~100 m; "
            "Class 2 = up to 2.5 mW, ~10 m (most consumer peripherals); "
            "Class 3 = up to 1 mW, ~1 m. Bluetooth 5.0 introduced a Long Range mode using "
            "coded PHY that can extend range significantly at lower data rates, but typical "
            "HID devices (keyboards, mice, headsets) still operate as Class 2 at ~10 m."
        ),
    },
    # ── 2.4  Network Services ────────────────────────────────────────────────
    {
        "id": "a1d2v2-015",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network services",
        "stem": (
            "Users in a branch office report that browsing popular websites is slow during "
            "peak hours but improves significantly mid-morning once caches are populated. "
            "A technician identifies a device in the network path that stores copies of "
            "frequently requested web content locally to reduce WAN bandwidth consumption "
            "and improve response times. Which device is responsible for this behavior?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Forward proxy server (web proxy/cache)",
                "correct": True,
                "rationale": (
                    "Correct. A forward proxy/cache server sits between internal clients and "
                    "the internet, caching frequently requested web content. Subsequent requests "
                    "for cached content are served locally, reducing WAN usage and improving "
                    "response times. The slow initial load occurs while the cache is being "
                    "populated."
                ),
            },
            {
                "id": "b",
                "text": "Reverse proxy server",
                "correct": False,
                "rationale": (
                    "Incorrect. A reverse proxy sits in front of web servers to serve content "
                    "on their behalf (often for load balancing or SSL termination). It caches "
                    "content for external clients accessing internal servers, not internal "
                    "clients accessing external websites."
                ),
            },
            {
                "id": "c",
                "text": "Content Delivery Network (CDN) edge node",
                "correct": False,
                "rationale": (
                    "Incorrect. A CDN edge node is operated by the content provider to cache "
                    "content geographically close to end users globally. It is not a device "
                    "the branch office network administrator controls or configures."
                ),
            },
            {
                "id": "d",
                "text": "DNS resolver with TTL caching",
                "correct": False,
                "rationale": (
                    "Incorrect. A DNS resolver caches DNS name-to-IP mappings to avoid "
                    "repeated queries. It does not cache web page content or reduce the "
                    "bandwidth needed to transfer web data."
                ),
            },
        ],
        "explanation": (
            "A forward proxy (web cache) is deployed at branch offices to cache HTTP/HTTPS "
            "content retrieved from the internet. Once content is cached, subsequent requests "
            "are served locally without WAN traversal, reducing bandwidth costs and latency. "
            "The first access (cache miss) is slow; subsequent accesses (cache hits) are fast. "
            "Solutions like Squid Proxy are common open-source implementations."
        ),
    },
    {
        "id": "a1d2v2-016",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network services",
        "stem": (
            "An IT director requires all internet-bound web traffic from corporate "
            "workstations to be inspected for malware and policy violations before reaching "
            "the internet, without installing software agents on each workstation. "
            "The solution must intercept traffic transparently. Which network device "
            "implements this function?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Inline web content filter / transparent proxy",
                "correct": True,
                "rationale": (
                    "Correct. A transparent (inline) proxy intercepts outbound HTTP/HTTPS "
                    "traffic at the network perimeter without requiring client configuration. "
                    "It inspects requests for malware and policy violations (URL filtering, "
                    "content categories) and blocks or allows traffic accordingly."
                ),
            },
            {
                "id": "b",
                "text": "Intrusion Detection System (IDS)",
                "correct": False,
                "rationale": (
                    "Incorrect. An IDS passively monitors network traffic and generates alerts "
                    "but does not block or inspect/decrypt web traffic inline. It cannot "
                    "enforce content filtering policies without an inline IPS."
                ),
            },
            {
                "id": "c",
                "text": "RADIUS server",
                "correct": False,
                "rationale": (
                    "Incorrect. A RADIUS server handles authentication and authorization for "
                    "network access (Wi-Fi, VPN, 802.1X). It does not inspect or filter "
                    "web content."
                ),
            },
            {
                "id": "d",
                "text": "NTP (Network Time Protocol) server",
                "correct": False,
                "rationale": (
                    "Incorrect. NTP synchronizes system clocks across network devices. It "
                    "has no role in web content inspection or traffic filtering."
                ),
            },
        ],
        "explanation": (
            "A transparent web proxy / content filter intercepts outbound traffic at the "
            "network gateway, applying URL filtering, SSL inspection (HTTPS decryption), "
            "and malware scanning. Unlike a standard proxy, clients require no manual "
            "proxy configuration — traffic is redirected at the network layer (typically by "
            "the firewall or router) to the proxy. Commercial examples include Cisco "
            "Umbrella, Zscaler, and Palo Alto Prisma."
        ),
    },
    # ── 2.5  SOHO Networks / IP Addressing ──────────────────────────────────
    {
        "id": "a1d2v2-017",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "IPv4 addressing & APIPA",
        "stem": (
            "A network is assigned the block 172.16.32.0/20. A technician needs to "
            "identify the valid host range and broadcast address for this subnet. "
            "Which answer correctly identifies the last usable host address and the "
            "broadcast address?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Last host: 172.16.47.254 | Broadcast: 172.16.47.255",
                "correct": True,
                "rationale": (
                    "Correct. /20 means 12 host bits (2^12 = 4096 addresses). Starting at "
                    "172.16.32.0, the block spans 172.16.32.0 – 172.16.47.255. The broadcast "
                    "address is 172.16.47.255 and the last usable host is 172.16.47.254."
                ),
            },
            {
                "id": "b",
                "text": "Last host: 172.16.32.254 | Broadcast: 172.16.32.255",
                "correct": False,
                "rationale": (
                    "Incorrect. This would be the range for a /24 (255.255.255.0) subnet, "
                    "which has only 256 addresses. A /20 has 4096 addresses and spans multiple "
                    "third-octet values from .32 to .47."
                ),
            },
            {
                "id": "c",
                "text": "Last host: 172.16.63.254 | Broadcast: 172.16.63.255",
                "correct": False,
                "rationale": (
                    "Incorrect. This would be the range for 172.16.32.0/18, which has 16,384 "
                    "addresses ending at 172.16.63.255. /20 has only 4,096 addresses, ending "
                    "at 172.16.47.255."
                ),
            },
            {
                "id": "d",
                "text": "Last host: 172.16.39.254 | Broadcast: 172.16.39.255",
                "correct": False,
                "rationale": (
                    "Incorrect. 172.16.39.255 would be the broadcast for 172.16.39.0/24. "
                    "A /20 subnet starting at 172.16.32.0 spans 32 through 47 in the third "
                    "octet, not just through 39."
                ),
            },
        ],
        "explanation": (
            "/20 subnet calculation: 32 - 20 = 12 host bits; block size = 2^12 = 4096. "
            "Starting network: 172.16.32.0. "
            "Ending broadcast: 172.16.32.0 + 4095 = 172.16.47.255 (32 + 16 - 1 = 47 in "
            "the third octet; fourth octet rolls to 255). "
            "Subnet mask: 255.255.240.0. "
            "Valid hosts: 172.16.32.1 – 172.16.47.254."
        ),
    },
    {
        "id": "a1d2v2-018",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "IPv4 addressing & APIPA",
        "stem": (
            "A technician adds a second NIC to a workstation for a direct crossover "
            "connection to a lab device. The second NIC is configured for DHCP, but "
            "no DHCP server is present on the crossover link. After 60 seconds the "
            "second NIC shows an IP address of 169.254.212.45. The technician wants "
            "to communicate with the lab device, which also has an APIPA address. "
            "What subnet mask does APIPA assign to all self-assigned addresses?"
        ),
        "options": [
            {
                "id": "a",
                "text": "255.255.0.0 (/16)",
                "correct": True,
                "rationale": (
                    "Correct. APIPA (Automatic Private IP Addressing) always assigns addresses "
                    "in the 169.254.0.0/16 range with a subnet mask of 255.255.0.0. Both "
                    "devices will be on the same /16 link-local subnet and can communicate "
                    "directly once their APIPA addresses are on the same segment."
                ),
            },
            {
                "id": "b",
                "text": "255.255.255.0 (/24)",
                "correct": False,
                "rationale": (
                    "Incorrect. APIPA does not use a /24 mask. The entire 169.254.0.0/16 range "
                    "is used as a single flat subnet with a /16 mask so that any two APIPA "
                    "devices on the same physical segment can communicate directly."
                ),
            },
            {
                "id": "c",
                "text": "255.0.0.0 (/8)",
                "correct": False,
                "rationale": (
                    "Incorrect. /8 (255.0.0.0) is a Class A mask. APIPA uses the specific "
                    "169.254.0.0/16 range with a 255.255.0.0 mask as defined by RFC 3927."
                ),
            },
            {
                "id": "d",
                "text": "255.255.255.128 (/25)",
                "correct": False,
                "rationale": (
                    "Incorrect. 255.255.255.128 is a /25 mask used in CIDR subnetting. "
                    "APIPA uses a /16 mask and is defined exclusively within the 169.254.0.0 "
                    "block per RFC 3927."
                ),
            },
        ],
        "explanation": (
            "RFC 3927 defines APIPA (link-local addressing) for IPv4 in the 169.254.0.0/16 "
            "block (169.254.1.0 – 169.254.254.255 for hosts; .0.0 and .255.255 reserved). "
            "The subnet mask is always 255.255.0.0 (/16). Hosts select a random address in "
            "the range and use ARP to verify uniqueness before assigning it. Two APIPA-assigned "
            "devices on the same physical link can communicate with each other but have no "
            "default gateway and cannot reach other networks."
        ),
    },
    {
        "id": "a1d2v2-019",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "IPv4 addressing & APIPA",
        "stem": (
            "A company needs to subnet 192.168.5.0/24 into segments that each support "
            "exactly 30 hosts. Which subnet mask should be used, and how many equal-sized "
            "subnets will be created?"
        ),
        "options": [
            {
                "id": "a",
                "text": "255.255.255.224 (/27); 8 subnets of 30 usable hosts each",
                "correct": True,
                "rationale": (
                    "Correct. /27 (255.255.255.224) borrows 3 bits from the Class C host "
                    "portion: 2^3 = 8 subnets. Each subnet has 2^5 = 32 addresses, minus "
                    "2 = 30 usable hosts — exactly meeting the requirement."
                ),
            },
            {
                "id": "b",
                "text": "255.255.255.192 (/26); 4 subnets of 62 usable hosts each",
                "correct": False,
                "rationale": (
                    "Incorrect. /26 provides 62 usable hosts per subnet — more than required. "
                    "The question asks for subnets that support exactly 30 hosts, which "
                    "requires /27 (30 usable hosts per subnet)."
                ),
            },
            {
                "id": "c",
                "text": "255.255.255.240 (/28); 16 subnets of 14 usable hosts each",
                "correct": False,
                "rationale": (
                    "Incorrect. /28 provides only 14 usable hosts per subnet, which is "
                    "insufficient for 30 hosts. /27 is the correct minimum mask to support "
                    "exactly 30 hosts."
                ),
            },
            {
                "id": "d",
                "text": "255.255.255.128 (/25); 2 subnets of 126 usable hosts each",
                "correct": False,
                "rationale": (
                    "Incorrect. /25 provides 126 usable hosts per subnet — far more than "
                    "needed for 30 hosts. Using /25 would waste address space compared to "
                    "the correctly sized /27."
                ),
            },
        ],
        "explanation": (
            "To find the right subnet for 30 hosts: the host bits needed = ceiling(log2(30+2)) "
            "= 5 bits (2^5 = 32 addresses, 30 usable). Prefix = 32 - 5 = /27. "
            "Mask = 255.255.255.224. Borrowed bits from /24 = 3, so 2^3 = 8 subnets. "
            "Subnets: .0, .32, .64, .96, .128, .160, .192, .224 — each with 30 usable hosts."
        ),
    },
    # ── 2.5  DHCP ────────────────────────────────────────────────────────────
    {
        "id": "a1d2v2-020",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "DHCP",
        "stem": (
            "A help desk technician receives calls from multiple users saying their PCs "
            "obtained the address 192.168.100.1 — the same IP address the router uses — "
            "which is causing network conflicts. Investigation reveals an unauthorized "
            "consumer router was plugged into the corporate network with its DHCP server "
            "enabled. What is this type of rogue device called, and what is the immediate "
            "remediation?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Rogue DHCP server; disable the unauthorized router's DHCP service or remove it from the network, and enable DHCP snooping on the switch",
                "correct": True,
                "rationale": (
                    "Correct. An unauthorized device running a DHCP server is called a rogue "
                    "DHCP server. It hands out incorrect IP configuration (wrong gateway, DNS, "
                    "or duplicate IPs), causing network disruption. DHCP snooping on the "
                    "managed switch limits DHCP server responses to authorized ports only."
                ),
            },
            {
                "id": "b",
                "text": "ARP poisoning attack; deploy a VLAN on the switch to isolate the affected hosts",
                "correct": False,
                "rationale": (
                    "Incorrect. ARP poisoning manipulates the ARP table to redirect traffic "
                    "at Layer 2, not issue false DHCP leases. The described scenario — an "
                    "unauthorized device distributing IP addresses — is specifically a rogue "
                    "DHCP server problem."
                ),
            },
            {
                "id": "c",
                "text": "DHCP starvation attack; increase the DHCP scope size to accommodate additional clients",
                "correct": False,
                "rationale": (
                    "Incorrect. DHCP starvation involves an attacker exhausting the DHCP scope "
                    "by requesting many leases. The described problem is a rogue server issuing "
                    "conflicting addresses, not scope exhaustion. Increasing scope size would "
                    "not fix the issue."
                ),
            },
            {
                "id": "d",
                "text": "IP address conflict from a misconfigured static assignment; audit all static IP assignments in the DHCP exclusion range",
                "correct": False,
                "rationale": (
                    "Incorrect. While IP conflicts can result from overlapping static "
                    "assignments, the root cause here is an unauthorized DHCP server "
                    "distributing the router's own IP as a client address. Auditing "
                    "exclusion ranges would not eliminate the rogue device."
                ),
            },
        ],
        "explanation": (
            "A rogue DHCP server is any unauthorized device (typically a consumer router "
            "or virtual machine with DHCP enabled) that responds to DHCP Discover broadcasts "
            "before the legitimate server. It issues incorrect IP configuration to clients, "
            "causing connectivity failures and potential traffic interception. Mitigation: "
            "remove or disable the rogue device; enable DHCP snooping on managed switches "
            "to allow DHCP responses only from authorized (trusted) uplink ports."
        ),
    },
    {
        "id": "a1d2v2-021",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "DHCP",
        "stem": (
            "A DHCP server is configured with a scope of 192.168.50.1–192.168.50.200 "
            "and a lease time of 8 hours. A laptop checked out at 9:00 AM is returned "
            "and powered off at 1:00 PM. At what time will the IP address be available "
            "for reassignment to another device, assuming the laptop does not send a "
            "DHCP Release before shutdown?"
        ),
        "options": [
            {
                "id": "a",
                "text": "5:00 PM — 8 hours after the lease was issued at 9:00 AM",
                "correct": True,
                "rationale": (
                    "Correct. A DHCP lease runs for its full duration from issuance regardless "
                    "of whether the client is online. If no DHCP Release message is sent, the "
                    "server holds the address reserved for 8 hours from 9:00 AM, releasing it "
                    "at 5:00 PM when the lease expires."
                ),
            },
            {
                "id": "b",
                "text": "1:00 PM — immediately when the laptop is powered off",
                "correct": False,
                "rationale": (
                    "Incorrect. The DHCP server has no mechanism to detect that the client "
                    "powered off without sending a Release message. The lease remains active "
                    "in the server's database until expiration."
                ),
            },
            {
                "id": "c",
                "text": "3:00 PM — 50% of the lease time after the laptop went offline",
                "correct": False,
                "rationale": (
                    "Incorrect. The T1 (50% lease time renewal timer) is a client-side timer "
                    "used by a connected client to attempt lease renewal, not an address "
                    "reclamation trigger on the server side when the client is absent."
                ),
            },
            {
                "id": "d",
                "text": "9:00 AM the next day — DHCP servers hold released addresses for 24 hours",
                "correct": False,
                "rationale": (
                    "Incorrect. DHCP servers do not automatically hold all expired addresses "
                    "for 24 hours. The lease expires at the configured lease duration "
                    "(8 hours) from the time it was issued."
                ),
            },
        ],
        "explanation": (
            "A DHCP lease expires at the issue time plus the lease duration. The server will "
            "not reclaim the IP address until the lease expires unless the client explicitly "
            "sends a DHCPRELEASE message. Shorter lease times reduce wasted address space "
            "in environments with high device turnover (conference rooms, guest Wi-Fi). "
            "Longer leases reduce DHCP traffic but mean abandoned addresses remain reserved "
            "longer."
        ),
    },
    # ── 2.5  IPv6 ────────────────────────────────────────────────────────────
    {
        "id": "a1d2v2-022",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "IPv6 addressing",
        "stem": (
            "A technician is reviewing IPv6 addresses on a dual-stack server and finds "
            "three addresses: fe80::1, fd00::1, and 2001:db8::1. Which address type "
            "is fd00::1, and can it be routed across the public internet?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Unique Local Address (ULA, fc00::/7); NOT routable on the public internet — analogous to IPv4 RFC 1918 private addresses",
                "correct": True,
                "rationale": (
                    "Correct. fd00::/8 falls within the ULA prefix fc00::/7 (fc00:: – fdff::). "
                    "ULA addresses are used for internal/private IPv6 networks and are not "
                    "routed on the public internet, similar to IPv4 private ranges like "
                    "10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16."
                ),
            },
            {
                "id": "b",
                "text": "Global Unicast Address; fully routable on the public internet",
                "correct": False,
                "rationale": (
                    "Incorrect. Global unicast addresses use the 2000::/3 range (2000:: – 3fff::). "
                    "fd00:: begins with 'fd' which is within the ULA range fc00::/7, not the "
                    "global unicast range."
                ),
            },
            {
                "id": "c",
                "text": "Link-local address; valid only on the directly connected link",
                "correct": False,
                "rationale": (
                    "Incorrect. Link-local addresses use the fe80::/10 prefix. fd00::1 starts "
                    "with 'fd', placing it in the ULA range, not the link-local range."
                ),
            },
            {
                "id": "d",
                "text": "Multicast address; used for one-to-many group communication",
                "correct": False,
                "rationale": (
                    "Incorrect. IPv6 multicast addresses use the ff00::/8 prefix. fd00::1 "
                    "does not begin with 'ff', so it is not a multicast address."
                ),
            },
        ],
        "explanation": (
            "IPv6 address type identification by prefix: "
            "fe80::/10 = Link-local (auto-configured, non-routable beyond local link); "
            "fc00::/7 (fd00::/8 most common) = Unique Local Address (ULA, private/non-internet-routable); "
            "2000::/3 = Global Unicast (internet-routable); "
            "ff00::/8 = Multicast; "
            "::1/128 = Loopback."
        ),
    },
    # ── 2.5  DNS Records ─────────────────────────────────────────────────────
    {
        "id": "a1d2v2-023",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "DNS records",
        "stem": (
            "A security tool performs a reverse DNS lookup on a suspicious IP address "
            "203.0.113.88 to determine the associated hostname. Which DNS record type "
            "maps an IP address back to a hostname, and in which special DNS zone are "
            "these records stored?"
        ),
        "options": [
            {
                "id": "a",
                "text": "PTR record; stored in the in-addr.arpa reverse lookup zone",
                "correct": True,
                "rationale": (
                    "Correct. PTR (Pointer) records map IP addresses to hostnames for reverse "
                    "DNS lookups. They are stored in the in-addr.arpa zone for IPv4 (and "
                    "ip6.arpa for IPv6). The query for 203.0.113.88 looks up "
                    "88.113.0.203.in-addr.arpa."
                ),
            },
            {
                "id": "b",
                "text": "CNAME record; stored in the forward lookup zone",
                "correct": False,
                "rationale": (
                    "Incorrect. A CNAME record creates an alias from one hostname to another "
                    "hostname in a forward lookup zone. It does not map IP addresses to "
                    "hostnames and is not used for reverse DNS."
                ),
            },
            {
                "id": "c",
                "text": "A record; stored in the reverse lookup zone",
                "correct": False,
                "rationale": (
                    "Incorrect. An A record maps a hostname to an IPv4 address (forward lookup). "
                    "It is not used for reverse DNS lookups. The PTR record is the record type "
                    "for reverse lookups."
                ),
            },
            {
                "id": "d",
                "text": "SRV record; stored in the service discovery zone",
                "correct": False,
                "rationale": (
                    "Incorrect. SRV (Service) records specify the location of services "
                    "(hostname and port) for protocols like SIP and XMPP. They are forward "
                    "lookup records and are unrelated to IP-to-hostname reverse lookups."
                ),
            },
        ],
        "explanation": (
            "Reverse DNS (rDNS) uses PTR records stored in the in-addr.arpa zone (IPv4) "
            "or ip6.arpa zone (IPv6). The IP address is reversed and appended with "
            ".in-addr.arpa for the query. For 203.0.113.88, the PTR query is for "
            "88.113.0.203.in-addr.arpa. Reverse DNS is used in spam filtering, security "
            "investigations, and some server-to-server protocols that verify hostname "
            "matching."
        ),
    },
    {
        "id": "a1d2v2-024",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "DNS records",
        "stem": (
            "A DevOps engineer wants to create a DNS alias so that 'api.example.com' "
            "points to 'prod-lb.us-east.cloud.example.com' without hardcoding an IP "
            "address. The alias must automatically follow the target hostname if its "
            "IP changes. Which DNS record type is correct, and what is a key restriction "
            "on its use at the zone apex (root of a domain)?"
        ),
        "options": [
            {
                "id": "a",
                "text": "CNAME record; CNAME records cannot be placed at the zone apex (e.g., example.com itself) because RFC prohibits coexistence with SOA/NS records",
                "correct": True,
                "rationale": (
                    "Correct. A CNAME maps one hostname to another and automatically follows "
                    "the target. By RFC 1034, a CNAME cannot coexist with other record types "
                    "at the same label — at the zone apex (example.com), NS and SOA records "
                    "are required, making a bare CNAME there illegal. 'api.example.com' is a "
                    "subdomain and can use CNAME."
                ),
            },
            {
                "id": "b",
                "text": "A record; A records cannot be used for subdomains, only for the zone apex",
                "correct": False,
                "rationale": (
                    "Incorrect. A records can be used at any hostname level, including "
                    "subdomains. However, an A record stores a fixed IP — if the target "
                    "IP changes, the A record must be manually updated. The engineer wants "
                    "automatic following of the target hostname, which CNAME provides."
                ),
            },
            {
                "id": "c",
                "text": "MX record; MX records alias hostnames and are the correct choice for load balancing subdomains",
                "correct": False,
                "rationale": (
                    "Incorrect. MX records designate mail exchange servers for a domain. "
                    "They are not general-purpose hostname aliases and cannot be used to "
                    "point a subdomain to another hostname for non-mail services."
                ),
            },
            {
                "id": "d",
                "text": "TXT record; TXT records store arbitrary text including hostname aliases",
                "correct": False,
                "rationale": (
                    "Incorrect. TXT records store free-form text data (SPF, DKIM, domain "
                    "verification). They are not resolved as hostname aliases and do not "
                    "cause DNS resolvers to follow them for IP address lookups."
                ),
            },
        ],
        "explanation": (
            "CNAME (Canonical Name) records alias one DNS name to another. Key rules: "
            "(1) A CNAME target must be a hostname, not an IP. (2) A CNAME cannot be placed "
            "at the zone apex because NS and SOA records are required there and cannot coexist "
            "with a CNAME. To alias the apex, DNS providers offer proprietary 'ALIAS' or "
            "'ANAME' record types that behave like CNAME but are resolved server-side."
        ),
    },
    # ── 2.6  VLAN / VPN ─────────────────────────────────────────────────────
    {
        "id": "a1d2v2-025",
        "domain": 2,
        "objective": "2.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "VLAN/VPN",
        "stem": (
            "A technician configures two switches connected by a trunk link. Switch A "
            "uses native VLAN 1 and Switch B uses native VLAN 10 on the trunk port. "
            "Untagged frames sent from Switch A's native VLAN 1 arrive on Switch B's "
            "trunk port and are placed into VLAN 10. What security vulnerability does "
            "this misconfiguration create?"
        ),
        "options": [
            {
                "id": "a",
                "text": "VLAN hopping via native VLAN mismatch; traffic from VLAN 1 on Switch A is forwarded into VLAN 10 on Switch B, bypassing VLAN isolation",
                "correct": True,
                "rationale": (
                    "Correct. When trunk ports on two switches have mismatched native VLANs, "
                    "untagged frames from one switch's native VLAN are interpreted as belonging "
                    "to the other switch's native VLAN, effectively bridging two separate "
                    "VLANs. This is a VLAN hopping vulnerability. Native VLANs must match "
                    "on both ends of a trunk."
                ),
            },
            {
                "id": "b",
                "text": "Broadcast storm; mismatched native VLANs cause STP to fail and create switching loops",
                "correct": False,
                "rationale": (
                    "Incorrect. STP loop detection is independent of native VLAN configuration. "
                    "A native VLAN mismatch does not directly cause STP failure or broadcast "
                    "storms; it causes traffic leakage between VLANs."
                ),
            },
            {
                "id": "c",
                "text": "IP address conflict; both VLANs share the same IP subnet when native VLANs differ",
                "correct": False,
                "rationale": (
                    "Incorrect. Native VLAN mismatch is a Layer 2 issue concerning frame "
                    "tagging. It does not inherently merge IP subnets, though the resulting "
                    "traffic leakage could cause routing anomalies at Layer 3."
                ),
            },
            {
                "id": "d",
                "text": "MAC flooding; the switch CAM table overflows when native VLAN tags conflict",
                "correct": False,
                "rationale": (
                    "Incorrect. MAC flooding is a different attack where an attacker sends "
                    "many frames with random source MACs to overflow the CAM table and force "
                    "the switch to flood traffic. It is not related to native VLAN mismatch."
                ),
            },
        ],
        "explanation": (
            "IEEE 802.1Q native VLAN: untagged frames on a trunk link are assigned to the "
            "native VLAN. If both ends of a trunk do not share the same native VLAN, "
            "untagged frames from one side are placed in a different VLAN on the other side, "
            "allowing traffic to cross VLAN boundaries. Cisco best practice: change the "
            "native VLAN on all trunks to an unused VLAN and tag all traffic (no native VLAN "
            "in production), or at minimum ensure native VLAN matches on both trunk ends."
        ),
    },
    {
        "id": "a1d2v2-026",
        "domain": 2,
        "objective": "2.6",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "VLAN/VPN",
        "stem": (
            "A network administrator is configuring IPSec VPN between two branch offices. "
            "The security team requires that the VPN tunnel encrypt the entire IP packet, "
            "including the original IP header, so that source and destination addresses "
            "are hidden from network sniffers. Which IPSec mode achieves this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Tunnel mode — encapsulates the entire original IP packet inside a new IP packet with a new header",
                "correct": True,
                "rationale": (
                    "Correct. IPSec Tunnel mode wraps the entire original IP packet (header + "
                    "payload) inside a new outer IP packet. The original source and destination "
                    "IPs are encrypted and invisible to external observers. Tunnel mode is "
                    "standard for site-to-site VPNs between gateways."
                ),
            },
            {
                "id": "b",
                "text": "Transport mode — encrypts only the IP payload, leaving the original IP header intact",
                "correct": False,
                "rationale": (
                    "Incorrect. IPSec Transport mode encrypts only the payload (TCP/UDP data) "
                    "and leaves the original IP header in plaintext. Source and destination IPs "
                    "remain visible to anyone monitoring the wire — not meeting the stated "
                    "requirement."
                ),
            },
            {
                "id": "c",
                "text": "AH (Authentication Header) mode — provides integrity but does not encrypt any portion of the packet",
                "correct": False,
                "rationale": (
                    "Incorrect. IPSec AH provides data integrity and authentication but "
                    "explicitly provides NO encryption of any content. It would not satisfy "
                    "the encryption requirement."
                ),
            },
            {
                "id": "d",
                "text": "GRE mode — encapsulates packets in a GRE header, providing encryption by default",
                "correct": False,
                "rationale": (
                    "Incorrect. GRE (Generic Routing Encapsulation) is a tunneling protocol "
                    "that encapsulates packets but does NOT encrypt them by default. GRE is "
                    "often used with IPSec (GRE over IPSec) but GRE alone provides no "
                    "security."
                ),
            },
        ],
        "explanation": (
            "IPSec Modes: Transport mode encrypts the payload only, exposing original IP "
            "headers — used for host-to-host communication. Tunnel mode encrypts the entire "
            "original packet and adds a new outer header — used for gateway-to-gateway "
            "(site-to-site) VPNs where endpoint IP addresses must be hidden. "
            "IPSec protocols: ESP (Encapsulating Security Payload) provides encryption + "
            "authentication; AH (Authentication Header) provides integrity/authentication "
            "only, no encryption."
        ),
    },
    # ── 2.7  Internet Connection Types ──────────────────────────────────────
    {
        "id": "a1d2v2-027",
        "domain": 2,
        "objective": "2.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Internet connection types",
        "stem": (
            "A small business is evaluating internet service options. Their ISP offers "
            "a connection with download speeds up to 150 Mbps and upload speeds up to "
            "20 Mbps over the existing coaxial TV cable infrastructure. No new cabling "
            "is needed. Which technology is this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Cable modem (DOCSIS)",
                "correct": True,
                "rationale": (
                    "Correct. DOCSIS (Data Over Cable Service Interface Specification) "
                    "delivers broadband internet over existing coaxial TV cable infrastructure. "
                    "It is asymmetric — download speeds are typically much higher than upload "
                    "speeds. DOCSIS 3.1 supports up to 10 Gbps down / 1 Gbps up."
                ),
            },
            {
                "id": "b",
                "text": "ADSL (Asymmetric Digital Subscriber Line)",
                "correct": False,
                "rationale": (
                    "Incorrect. ADSL uses copper telephone lines (PSTN), not coaxial TV cable. "
                    "ADSL also has lower top speeds (typically up to ~24 Mbps down / 3 Mbps "
                    "up for ADSL2+) compared to the 150 Mbps described."
                ),
            },
            {
                "id": "c",
                "text": "FTTH (Fiber to the Home)",
                "correct": False,
                "rationale": (
                    "Incorrect. FTTH requires installation of new fiber optic cabling to "
                    "the premises. The scenario states no new cabling is needed, and the "
                    "existing infrastructure is coaxial cable."
                ),
            },
            {
                "id": "d",
                "text": "Fixed wireless access (FWA)",
                "correct": False,
                "rationale": (
                    "Incorrect. Fixed wireless access uses radio frequency signals (typically "
                    "4G LTE or 5G) transmitted to a rooftop antenna — it does not use "
                    "existing coaxial TV cable infrastructure."
                ),
            },
        ],
        "explanation": (
            "DOCSIS (cable modem technology) transmits broadband internet over coaxial "
            "infrastructure originally built for cable television. Because it shares the "
            "downstream spectrum with TV channels, it is inherently asymmetric (higher "
            "download than upload). DOCSIS 3.0 supports ~1 Gbps down; DOCSIS 3.1 extends "
            "to 10 Gbps down / 1 Gbps up using OFDM techniques."
        ),
    },
    {
        "id": "a1d2v2-028",
        "domain": 2,
        "objective": "2.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Internet connection types",
        "stem": (
            "A sales representative works from a hotel room and needs to securely access "
            "the corporate intranet. The hotel provides only public Wi-Fi. The IT "
            "department wants the representative to use a technology that creates an "
            "encrypted channel over the untrusted hotel Wi-Fi to protect all corporate "
            "traffic. Which technology should the representative use?"
        ),
        "options": [
            {
                "id": "a",
                "text": "SSL/TLS VPN client (remote access VPN)",
                "correct": True,
                "rationale": (
                    "Correct. A remote access VPN (SSL/TLS or IPSec-based) creates an "
                    "encrypted tunnel from the representative's laptop to the corporate "
                    "VPN gateway, protecting all traffic traversing the untrusted hotel "
                    "Wi-Fi. SSL VPNs typically use TCP 443 and are rarely blocked by hotel "
                    "firewalls."
                ),
            },
            {
                "id": "b",
                "text": "WPA3-Enterprise wireless authentication",
                "correct": False,
                "rationale": (
                    "Incorrect. WPA3-Enterprise is an authentication protocol for connecting "
                    "to a Wi-Fi network, not a VPN solution. The representative cannot control "
                    "what the hotel's Wi-Fi network uses. Even with WPA3, traffic on the hotel "
                    "network beyond the AP could be unprotected."
                ),
            },
            {
                "id": "c",
                "text": "HTTPS-only browsing with certificate pinning",
                "correct": False,
                "rationale": (
                    "Incorrect. HTTPS protects individual web sessions but does not encrypt "
                    "all corporate traffic (e.g., SMB file access, email over non-HTTPS "
                    "protocols). A full VPN is needed for complete tunnel protection."
                ),
            },
            {
                "id": "d",
                "text": "Satellite internet modem bypass to avoid hotel Wi-Fi",
                "correct": False,
                "rationale": (
                    "Incorrect. Bringing a satellite modem to a hotel room is impractical "
                    "and does not address the requirement to use existing hotel connectivity "
                    "securely. A VPN is the standard solution for secure remote access."
                ),
            },
        ],
        "explanation": (
            "Remote access VPN (SSL/TLS or IPSec) creates an encrypted tunnel over any "
            "untrusted network (hotel Wi-Fi, public hotspots). All traffic is encrypted "
            "before leaving the device and decrypted at the corporate VPN gateway. "
            "SSL VPNs on TCP 443 are rarely blocked. IPSec VPNs use UDP 500 (IKE) and "
            "may be blocked by strict firewalls, making SSL VPN more reliable for road "
            "warriors in public environments."
        ),
    },
    # ── 2.7  Network Types ───────────────────────────────────────────────────
    {
        "id": "a1d2v2-029",
        "domain": 2,
        "objective": "2.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network types (LAN/WAN/PAN)",
        "stem": (
            "A university campus spans 12 buildings within a 2-mile radius. Each "
            "building has its own LAN, and the buildings are interconnected via the "
            "university's privately owned fiber ring. This interconnected network of "
            "multiple LANs within a geographically limited campus area is classified "
            "as which network type?"
        ),
        "options": [
            {
                "id": "a",
                "text": "MAN (Metropolitan Area Network)",
                "correct": True,
                "rationale": (
                    "Correct. A MAN connects multiple LANs within a metropolitan or campus "
                    "area (typically 1–50 km). A university campus fiber ring interconnecting "
                    "buildings is a classic MAN example. MANs may use fiber, 802.11 point-to-"
                    "point, or carrier Ethernet circuits."
                ),
            },
            {
                "id": "b",
                "text": "WAN (Wide Area Network)",
                "correct": False,
                "rationale": (
                    "Incorrect. A WAN spans large geographic distances (cities, countries, "
                    "continents) and typically uses leased carrier circuits. A 2-mile university "
                    "campus with privately owned fiber is a MAN, not a WAN."
                ),
            },
            {
                "id": "c",
                "text": "LAN (Local Area Network)",
                "correct": False,
                "rationale": (
                    "Incorrect. A LAN is limited to a single building or floor. The interconnection "
                    "of 12 buildings extends beyond a single LAN. Each building's network "
                    "is an individual LAN; together they form a MAN."
                ),
            },
            {
                "id": "d",
                "text": "PAN (Personal Area Network)",
                "correct": False,
                "rationale": (
                    "Incorrect. A PAN covers a very short range (typically less than 10 meters) "
                    "for personal device connectivity. A 2-mile campus network is not a PAN "
                    "by any definition."
                ),
            },
        ],
        "explanation": (
            "Network scope classifications: PAN < 10 m (Bluetooth, USB); LAN = single "
            "building/floor; CAN (Campus Area Network) = multiple buildings on campus "
            "(sometimes used interchangeably with MAN in academic contexts); "
            "MAN = metropolitan/city area 1-50 km; WAN = long-distance, multi-city. "
            "The CompTIA A+ exam uses MAN to describe campus or city-scale private "
            "interconnects and WAN for carrier-provided long-distance connections."
        ),
    },
    # ── 2.8  Copper & Fiber Cabling ──────────────────────────────────────────
    {
        "id": "a1d2v2-030",
        "domain": 2,
        "objective": "2.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Copper & fiber cabling",
        "stem": (
            "A data center technician is installing 40GbE direct-attach copper (DAC) "
            "cables between top-of-rack switches and servers. The cables use which "
            "connector type on each end, and what is the maximum recommended length "
            "for passive DAC cables in this application?"
        ),
        "options": [
            {
                "id": "a",
                "text": "QSFP+ connectors; maximum ~7 meters for passive DAC",
                "correct": True,
                "rationale": (
                    "Correct. 40GbE DAC cables use QSFP+ (Quad Small Form-factor Pluggable+) "
                    "connectors on both ends. Passive direct-attach copper cables are "
                    "cost-effective for short intra-rack distances, typically up to 5–7 meters. "
                    "Active DAC cables extend this to ~15 meters."
                ),
            },
            {
                "id": "b",
                "text": "RJ-45 connectors; maximum 100 meters",
                "correct": False,
                "rationale": (
                    "Incorrect. RJ-45 is the connector for copper twisted-pair Ethernet "
                    "(10/100/1000BASE-T, 10GBASE-T). 40GbE DAC cables use QSFP+ form-factor "
                    "connectors, not RJ-45. The 100-meter limit applies to 10GBase-T/Cat6a, "
                    "not 40GbE DAC."
                ),
            },
            {
                "id": "c",
                "text": "LC fiber connectors; maximum 10 km for single-mode",
                "correct": False,
                "rationale": (
                    "Incorrect. LC connectors are used for fiber optic cables, not direct-attach "
                    "copper. DAC cables use electrical signals, not optical. The 10 km figure "
                    "applies to single-mode fiber transceivers."
                ),
            },
            {
                "id": "d",
                "text": "SFP+ connectors; maximum 100 meters",
                "correct": False,
                "rationale": (
                    "Incorrect. SFP+ is the form factor for 10GbE connections, not 40GbE. "
                    "40GbE uses QSFP+ (4x10G lanes). Additionally, passive DAC cables are "
                    "limited to ~7 meters, not 100 meters."
                ),
            },
        ],
        "explanation": (
            "Direct-attach copper (DAC) cables are twinaxial copper assemblies with "
            "integrated transceivers (the connector is fixed to the cable). They are "
            "used for short, high-speed connections within data center racks and rows. "
            "Form factors: SFP/SFP+ for 1/10GbE; QSFP+/QSFP28 for 40/100GbE. "
            "Passive DAC: up to ~7 m. Active DAC: up to ~15 m. Beyond that, optical "
            "transceivers with fiber cabling are required."
        ),
    },
    {
        "id": "a1d2v2-031",
        "domain": 2,
        "objective": "2.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Copper & fiber cabling",
        "stem": (
            "A technician is documenting an existing fiber installation and identifies "
            "two types of fiber in the building: orange-jacketed cable and yellow-jacketed "
            "cable. Which type of fiber does each color represent, and what is the primary "
            "operational difference between them?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Orange = multimode fiber (MMF); yellow = single-mode fiber (SMF). MMF supports shorter distances at lower cost; SMF supports longer distances (10 km+) with laser transceivers",
                "correct": True,
                "rationale": (
                    "Correct. TIA-568 color standards: orange (or aqua for OM3/OM4) jacket = "
                    "multimode fiber; yellow jacket = single-mode fiber. MMF uses LEDs or "
                    "VCSELs and is limited to ~550 m (OM3 at 10G) to 2 km. SMF uses laser "
                    "light and supports 10 km or more depending on transceiver type."
                ),
            },
            {
                "id": "b",
                "text": "Orange = single-mode fiber; yellow = multimode fiber",
                "correct": False,
                "rationale": (
                    "Incorrect. The color assignment is reversed. Orange or aqua cable is "
                    "multimode fiber; yellow cable is single-mode fiber per TIA-568 and "
                    "general industry convention."
                ),
            },
            {
                "id": "c",
                "text": "Orange = Cat 6a Ethernet; yellow = Cat 5e Ethernet. Both are copper twisted pair",
                "correct": False,
                "rationale": (
                    "Incorrect. Cat 6a and Cat 5e are copper twisted-pair cables, not fiber. "
                    "The color coding described (orange and yellow) specifically identifies "
                    "fiber types in TIA-568 standards."
                ),
            },
            {
                "id": "d",
                "text": "Orange = plenum-rated fiber; yellow = riser-rated fiber. Both are multimode",
                "correct": False,
                "rationale": (
                    "Incorrect. Orange and yellow jacket colors in fiber installations indicate "
                    "fiber type (multimode vs. single-mode), not the fire-rating (plenum vs. "
                    "riser). A fiber cable can be any of these types AND have a plenum or "
                    "riser rating separately."
                ),
            },
        ],
        "explanation": (
            "TIA-568 fiber jacket color convention: Orange = OM1/OM2 multimode (62.5/50 µm core); "
            "Aqua = OM3/OM4 multimode (50 µm, optimized for VCSEL lasers); "
            "Yellow = OS1/OS2 single-mode (9 µm core). "
            "SMF (yellow) has a much narrower core, limiting modal dispersion and allowing "
            "laser light to travel 10 km+ with minimal signal loss. MMF (orange/aqua) uses "
            "larger cores suitable for LED/VCSEL light sources at shorter distances."
        ),
    },
    # ── 2.8  T568A/B Wiring ──────────────────────────────────────────────────
    {
        "id": "a1d2v2-032",
        "domain": 2,
        "objective": "2.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "T568A/B wiring",
        "stem": (
            "A technician is called to troubleshoot a newly terminated Cat 5e run. "
            "A cable certifier shows that pin 1 at one end connects to pin 3 at the "
            "other end, and pin 2 connects to pin 6. Pins 3-8 are wired straight through. "
            "The client expected a standard patch cable. What wiring error was made?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The technician accidentally wired one end as T568A and the other as T568B, creating a crossover cable",
                "correct": True,
                "rationale": (
                    "Correct. The T568A standard places the green pair on pins 1/2 and orange "
                    "on 3/6. T568B places orange on 1/2 and green on 3/6. Mixing standards "
                    "swaps pins 1↔3 and 2↔6 — exactly the result described — creating a "
                    "crossover cable instead of a patch cable."
                ),
            },
            {
                "id": "b",
                "text": "The technician reversed the entire cable (pin 1 to pin 8, pin 2 to pin 7, etc.), creating a rollover cable",
                "correct": False,
                "rationale": (
                    "Incorrect. A rollover (console) cable reverses ALL 8 pins (1↔8, 2↔7, "
                    "3↔6, 4↔5). The fault described only swaps pins 1↔3 and 2↔6, which is "
                    "specific to the T568A/T568B orange-green pair swap."
                ),
            },
            {
                "id": "c",
                "text": "The cable has a split pair; pins 1 and 3 share a common pair wire, causing crosstalk",
                "correct": False,
                "rationale": (
                    "Incorrect. A split pair error occurs when wires from two different twisted "
                    "pairs are incorrectly paired together (e.g., using one wire from the "
                    "orange pair and one from the green pair on pins 1 and 2). This would "
                    "not produce the pin-to-pin mapping described."
                ),
            },
            {
                "id": "d",
                "text": "The cable is wired as a T568C standard, which swaps the blue and brown pairs",
                "correct": False,
                "rationale": (
                    "Incorrect. T568C is not an ANSI/TIA-568 standard. The two legitimate "
                    "T568 wiring standards are A and B. The described pin swap (1↔3, 2↔6) "
                    "is the result of mixing T568A and T568B, creating a crossover cable."
                ),
            },
        ],
        "explanation": (
            "T568A pin assignments: 1=W/G, 2=G, 3=W/O, 4=B, 5=W/B, 6=O, 7=W/Br, 8=Br. "
            "T568B pin assignments: 1=W/O, 2=O, 3=W/G, 4=B, 5=W/B, 6=G, 7=W/Br, 8=Br. "
            "The ONLY difference is that the green and orange pairs are swapped. "
            "A crossover cable = T568A on one end + T568B on the other. "
            "A straight-through (patch) cable = same standard (A or B) on both ends."
        ),
    },
    # ── Multiple Response Questions ──────────────────────────────────────────
    {
        "id": "a1d2v2-033",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Ports & protocols",
        "stem": (
            "A firewall administrator is creating outbound rules for a new email server "
            "that needs to send email to external recipients and allow clients to retrieve "
            "mail securely. Which TWO ports must be opened outbound to support sending "
            "email to other mail servers and encrypted retrieval by clients using IMAPS? "
            "(Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "TCP 25 (SMTP — for sending email to other mail servers)",
                "correct": True,
                "rationale": (
                    "Correct. SMTP on TCP 25 is the protocol used for mail server-to-mail "
                    "server message relay. The outbound firewall must allow TCP 25 for the "
                    "mail server to deliver messages to external recipients' mail servers."
                ),
            },
            {
                "id": "b",
                "text": "TCP 993 (IMAPS — IMAP over TLS for secure client mail retrieval)",
                "correct": True,
                "rationale": (
                    "Correct. IMAPS (IMAP Secure) uses TCP 993 (IMAP over implicit TLS). "
                    "Clients connecting to retrieve email securely use TCP 993. The firewall "
                    "must allow inbound TCP 993 to the mail server (and outbound TCP 993 "
                    "if clients are behind the same firewall)."
                ),
            },
            {
                "id": "c",
                "text": "TCP 110 (POP3 — for client mail retrieval without encryption)",
                "correct": False,
                "rationale": (
                    "Incorrect. The question specifies secure (encrypted) client retrieval "
                    "using IMAPS. TCP 110 is standard POP3, which is unencrypted. IMAPS on "
                    "TCP 993 is the required secure retrieval protocol."
                ),
            },
            {
                "id": "d",
                "text": "TCP 23 (Telnet — for remote server administration)",
                "correct": False,
                "rationale": (
                    "Incorrect. Telnet on TCP 23 provides unencrypted remote CLI access "
                    "and has no role in email transmission or retrieval. Remote server "
                    "administration should use SSH (TCP 22), not Telnet."
                ),
            },
        ],
        "explanation": (
            "Email port reference: SMTP = TCP 25 (server-to-server relay); "
            "SMTP submission = TCP 587 (client-to-server with STARTTLS); "
            "SMTPS = TCP 465 (implicit TLS); "
            "IMAP = TCP 143 (plaintext); IMAPS = TCP 993 (TLS); "
            "POP3 = TCP 110 (plaintext); POP3S = TCP 995 (TLS). "
            "The exam expects knowledge of both the plain and encrypted port variants."
        ),
    },
    {
        "id": "a1d2v2-034",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "IPv4 addressing & APIPA",
        "stem": (
            "A network administrator is troubleshooting IP connectivity issues and runs "
            "ipconfig /all on a Windows workstation. The output shows an IPv4 address "
            "of 169.254.45.200 and no default gateway. Which TWO conclusions can be "
            "drawn from this output? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "The workstation failed to obtain an IP address from a DHCP server and self-assigned an APIPA address",
                "correct": True,
                "rationale": (
                    "Correct. APIPA addresses (169.254.0.0/16) are automatically assigned by "
                    "Windows when DHCP discovery fails after multiple retries. This confirms "
                    "the workstation could not communicate with a DHCP server."
                ),
            },
            {
                "id": "b",
                "text": "The workstation cannot communicate with devices outside its local subnet, including the internet",
                "correct": True,
                "rationale": (
                    "Correct. APIPA addresses are link-local and non-routable. No default "
                    "gateway is assigned with APIPA, so the workstation can only communicate "
                    "with other devices on the same physical link that also have APIPA addresses "
                    "in the 169.254.0.0/16 range."
                ),
            },
            {
                "id": "c",
                "text": "The DHCP server's address scope is exhausted and no addresses remain",
                "correct": False,
                "rationale": (
                    "Incorrect. Scope exhaustion is one possible reason for DHCP failure, but "
                    "it is not the only one. Other causes include: the workstation not being "
                    "physically connected to the network, the NIC being faulty, a misconfigured "
                    "DHCP relay agent, or the DHCP service being stopped. This conclusion "
                    "cannot be determined from ipconfig alone."
                ),
            },
            {
                "id": "d",
                "text": "The workstation has been assigned a valid public IP address by the ISP",
                "correct": False,
                "rationale": (
                    "Incorrect. 169.254.x.x is an IANA-reserved, link-local non-routable "
                    "address range. It is never a valid public internet IP address and was "
                    "never assigned by an ISP."
                ),
            },
        ],
        "explanation": (
            "169.254.0.0/16 is the APIPA range (RFC 3927). Key APIPA facts: "
            "(1) Self-assigned when DHCP fails; (2) No default gateway; (3) Non-routable "
            "beyond the local link; (4) Two APIPA devices on the same segment CAN ping each "
            "other; (5) ARP is used to detect address conflicts before assignment. "
            "Troubleshooting: check physical connection, switch port, DHCP service status, "
            "and DHCP scope capacity."
        ),
    },
    {
        "id": "a1d2v2-035",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Wireless standards",
        "stem": (
            "A company is upgrading its wireless infrastructure and comparing 802.11n "
            "(Wi-Fi 4) to 802.11ax (Wi-Fi 6). Which TWO capabilities does 802.11ax "
            "introduce that are NOT present in 802.11n? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "OFDMA (Orthogonal Frequency Division Multiple Access) for simultaneous multi-user channel access",
                "correct": True,
                "rationale": (
                    "Correct. OFDMA is introduced in 802.11ax and allows a single AP to "
                    "serve multiple clients simultaneously within the same channel by dividing "
                    "it into sub-channels (resource units). 802.11n uses OFDM, which serves "
                    "one client per transmission."
                ),
            },
            {
                "id": "b",
                "text": "Target Wake Time (TWT) to schedule client sleep/wake intervals for improved battery life",
                "correct": True,
                "rationale": (
                    "Correct. TWT (Target Wake Time) is an 802.11ax feature that allows the "
                    "AP to schedule when clients must be awake to receive/send data. IoT and "
                    "mobile devices can sleep for longer intervals, significantly improving "
                    "battery life. TWT is not present in 802.11n."
                ),
            },
            {
                "id": "c",
                "text": "MIMO (Multiple Input, Multiple Output) antenna technology",
                "correct": False,
                "rationale": (
                    "Incorrect. MIMO was introduced in 802.11n (Wi-Fi 4). 802.11ax improves "
                    "upon it with up/downlink MU-MIMO and more spatial streams, but MIMO itself "
                    "is not new in 802.11ax."
                ),
            },
            {
                "id": "d",
                "text": "Support for the 5 GHz frequency band",
                "correct": False,
                "rationale": (
                    "Incorrect. 802.11n (Wi-Fi 4) already introduced dual-band operation "
                    "supporting both 2.4 GHz and 5 GHz. The 5 GHz band is not a new feature "
                    "introduced by 802.11ax."
                ),
            },
        ],
        "explanation": (
            "802.11ax (Wi-Fi 6) key new features compared to 802.11n: "
            "OFDMA (multi-user sub-channel access), "
            "uplink and downlink MU-MIMO (up to 8x8 vs 4x4 in 11n), "
            "Target Wake Time (TWT), "
            "BSS Coloring (co-channel interference management), "
            "1024-QAM modulation (vs 64-QAM in 11n), "
            "and Wi-Fi 6E adds the 6 GHz band. "
            "The practical result: Wi-Fi 6 is dramatically better in dense deployments."
        ),
    },
    {
        "id": "a1d2v2-036",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Networking hardware",
        "stem": (
            "A network administrator is configuring Layer 3 switching in the data center "
            "to enable inter-VLAN routing without a dedicated router. Which TWO statements "
            "correctly describe how a Layer 3 switch differs from a standard Layer 2 switch? "
            "(Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "A Layer 3 switch can route IP packets between VLANs using Switched Virtual Interfaces (SVIs) without a separate router",
                "correct": True,
                "rationale": (
                    "Correct. A Layer 3 (multilayer) switch has built-in routing capability. "
                    "SVIs (Switched Virtual Interfaces) are Layer 3 interfaces assigned to "
                    "VLANs, acting as the default gateway for hosts in each VLAN. Traffic "
                    "between VLANs is routed in hardware at line rate."
                ),
            },
            {
                "id": "b",
                "text": "A Layer 3 switch can run routing protocols such as OSPF or EIGRP to dynamically exchange routes with other routers",
                "correct": True,
                "rationale": (
                    "Correct. Layer 3 switches support dynamic routing protocols (OSPF, "
                    "EIGRP, BGP in some enterprise models) just like dedicated routers. They "
                    "can participate in the routed network as a full routing peer."
                ),
            },
            {
                "id": "c",
                "text": "A Layer 3 switch uses a separate routing processor that is slower than hardware-based MAC forwarding",
                "correct": False,
                "rationale": (
                    "Incorrect. A key advantage of Layer 3 switches is that routing decisions "
                    "are performed in hardware (ASICs) at line rate — comparable to Layer 2 "
                    "forwarding speeds. Software-routed (process-switched) forwarding on "
                    "traditional routers is far slower by comparison."
                ),
            },
            {
                "id": "d",
                "text": "A Layer 3 switch cannot support VLANs; VLANs require a Layer 2 switch",
                "correct": False,
                "rationale": (
                    "Incorrect. A Layer 3 switch is a superset of a Layer 2 switch — it "
                    "supports all Layer 2 features including VLANs, STP, and MAC forwarding, "
                    "plus adds Layer 3 routing capability. It does not lose VLAN support "
                    "by adding routing."
                ),
            },
        ],
        "explanation": (
            "A Layer 3 (multilayer) switch combines a full-featured Layer 2 switch with "
            "hardware-accelerated IP routing. Key use: inter-VLAN routing (router-on-a-stick "
            "alternative) via SVIs (Switched Virtual Interfaces). Advantages over a router "
            "for inter-VLAN routing: faster (ASIC-based, line rate), cheaper per-port at "
            "scale, and eliminates the router bottleneck on trunk links."
        ),
    },
    {
        "id": "a1d2v2-037",
        "domain": 2,
        "objective": "2.8",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Copper & fiber cabling",
        "stem": (
            "A facilities manager is documenting the structured cabling in a building. "
            "Which TWO statements correctly describe the maximum segment lengths for "
            "standard copper Ethernet cabling under TIA-568 specifications? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Cat 5e and Cat 6 both support a maximum horizontal run of 90 meters from patch panel to wall plate, with an additional 10 meters allowed for patch cables and equipment cords",
                "correct": True,
                "rationale": (
                    "Correct. TIA-568 specifies a 90-meter maximum for the permanent link "
                    "(horizontal cable from patch panel to wall outlet) plus up to 10 meters "
                    "combined for patch cords at both ends — totaling 100 meters maximum "
                    "channel length. This applies to all Cat 5e and Cat 6 1000BASE-T "
                    "installations."
                ),
            },
            {
                "id": "b",
                "text": "Cat 6a supports 10GBASE-T at the full 100-meter channel length, whereas Cat 6 is limited to approximately 55 meters for 10GBASE-T",
                "correct": True,
                "rationale": (
                    "Correct. Cat 6 can support 10GBASE-T but only up to ~55 meters due to "
                    "alien crosstalk (ANEXT) limitations. Cat 6a adds additional shielding "
                    "and tighter specifications to support 10GBASE-T at the full 100-meter "
                    "channel length."
                ),
            },
            {
                "id": "c",
                "text": "Cat 5e supports 10 Gbps Ethernet (10GBASE-T) at distances up to 100 meters",
                "correct": False,
                "rationale": (
                    "Incorrect. Cat 5e is specified only for 1000BASE-T (1 Gbps) at 100 meters. "
                    "It cannot reliably support 10GBASE-T at any practical distance because "
                    "it lacks the bandwidth (250 MHz for Cat 6 vs 100 MHz for Cat 5e) and "
                    "alien crosstalk control required."
                ),
            },
            {
                "id": "d",
                "text": "Cat 6 can be extended beyond 100 meters by adding a repeater hub to amplify the signal",
                "correct": False,
                "rationale": (
                    "Incorrect. Ethernet repeater hubs are obsolete Layer 1 devices. To extend "
                    "an Ethernet segment beyond 100 meters, a switch or media converter must "
                    "be used — not a repeater hub. A switch regenerates the digital signal "
                    "properly, whereas a hub merely amplifies the analog signal."
                ),
            },
        ],
        "explanation": (
            "TIA-568 copper segment lengths: 90 m permanent link + 10 m patch cords = "
            "100 m maximum channel. This applies to Cat 5e, Cat 6, Cat 6a, and Cat 8. "
            "Speed tiers: Cat 5e = 1 Gbps (100 m); Cat 6 = 1 Gbps (100 m), 10 Gbps (~55 m); "
            "Cat 6a = 10 Gbps (100 m); Cat 8 = 25/40 Gbps (30 m, data center only). "
            "To extend beyond 100 m, use a switch, fiber media converter, or fiber run."
        ),
    },
    {
        "id": "a1d2v2-038",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "VLAN/VPN",
        "stem": (
            "A network security architect is hardening the switching infrastructure. "
            "Which TWO of the following switch security features specifically protect "
            "against Layer 2 attacks? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "DHCP snooping — blocks rogue DHCP server responses on untrusted switch ports",
                "correct": True,
                "rationale": (
                    "Correct. DHCP snooping is a Layer 2 security feature that classifies "
                    "switch ports as trusted (uplinks to legitimate DHCP servers) or untrusted "
                    "(client ports). DHCP server responses on untrusted ports are dropped, "
                    "preventing rogue DHCP server attacks."
                ),
            },
            {
                "id": "b",
                "text": "Dynamic ARP Inspection (DAI) — validates ARP packets against the DHCP snooping binding table to prevent ARP poisoning",
                "correct": True,
                "rationale": (
                    "Correct. Dynamic ARP Inspection inspects ARP packets on untrusted ports "
                    "and checks them against the DHCP snooping binding table (IP-to-MAC-to-port "
                    "mappings). ARP replies with invalid IP-MAC bindings are dropped, preventing "
                    "ARP poisoning / man-in-the-middle attacks."
                ),
            },
            {
                "id": "c",
                "text": "IPSec with AES-256 encryption on all inter-VLAN traffic",
                "correct": False,
                "rationale": (
                    "Incorrect. IPSec operates at Layer 3 and protects IP-level traffic. "
                    "It is not a Layer 2 switch security feature. DHCP snooping and DAI "
                    "are specifically Layer 2 (data link layer) controls implemented on the "
                    "switch itself."
                ),
            },
            {
                "id": "d",
                "text": "ACLs on router interfaces to block external SSH brute-force attempts",
                "correct": False,
                "rationale": (
                    "Incorrect. Router ACLs blocking SSH brute force are a Layer 3/4 perimeter "
                    "security control. They protect router management interfaces from external "
                    "attacks, not Layer 2 switch-specific threats like ARP poisoning or "
                    "rogue DHCP servers."
                ),
            },
        ],
        "explanation": (
            "Layer 2 switch security features: "
            "DHCP Snooping — prevents rogue DHCP; builds IP/MAC binding table; "
            "Dynamic ARP Inspection (DAI) — prevents ARP poisoning, uses DHCP snooping table; "
            "Port Security — limits MAC addresses per port, prevents MAC flooding; "
            "802.1X Port Authentication — authenticates devices before allowing network access; "
            "Storm Control — limits broadcast/multicast/unknown unicast traffic rates. "
            "These features work at the Ethernet (Layer 2) level on the switch itself."
        ),
    },
]

QUESTIONS = [
    # ── 2.1  Ports & Protocols ──────────────────────────────────────────────
    {
        "id": "a1d2-001",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Ports & protocols",
        "stem": (
            "A security audit flags outbound traffic on TCP 23 leaving the corporate network. "
            "Management wants to immediately replace it with an encrypted alternative that uses "
            "the same style of remote CLI access. Which protocol and port should be substituted?"
        ),
        "options": [
            {
                "id": "a",
                "text": "SSH on TCP 22",
                "correct": True,
                "rationale": (
                    "Correct. SSH (Secure Shell) on TCP 22 provides encrypted remote command-line "
                    "access and is the direct encrypted replacement for Telnet (TCP 23)."
                ),
            },
            {
                "id": "b",
                "text": "RDP on TCP 3389",
                "correct": False,
                "rationale": (
                    "Incorrect. RDP provides graphical remote-desktop sessions, not a command-line "
                    "shell equivalent. It also uses TCP 3389, not 22."
                ),
            },
            {
                "id": "c",
                "text": "SFTP on TCP 22",
                "correct": False,
                "rationale": (
                    "Incorrect. SFTP is a file-transfer protocol that runs over SSH; while it uses "
                    "TCP 22, it is not a remote CLI shell substitute for Telnet."
                ),
            },
            {
                "id": "d",
                "text": "HTTPS on TCP 443",
                "correct": False,
                "rationale": (
                    "Incorrect. HTTPS encrypts web traffic on TCP 443 and does not provide "
                    "interactive command-line remote access."
                ),
            },
        ],
        "explanation": (
            "Telnet (TCP 23) transmits credentials and data in cleartext. SSH (TCP 22) was "
            "designed as its encrypted replacement, providing an authenticated, encrypted "
            "interactive shell session. Every organization should disable Telnet and use SSH "
            "for remote CLI management."
        ),
    },
    {
        "id": "a1d2-002",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Ports & protocols",
        "stem": (
            "A mail server administrator needs to configure the server so that mobile clients "
            "can retrieve email while leaving copies on the server for synchronization across "
            "multiple devices. Which protocol and default port should be configured on the server?"
        ),
        "options": [
            {
                "id": "a",
                "text": "IMAP on TCP 143",
                "correct": True,
                "rationale": (
                    "Correct. IMAP (Internet Message Access Protocol) on TCP 143 leaves messages "
                    "on the server and supports multi-device synchronization, unlike POP3 which "
                    "downloads and typically deletes messages from the server."
                ),
            },
            {
                "id": "b",
                "text": "POP3 on TCP 110",
                "correct": False,
                "rationale": (
                    "Incorrect. POP3 on TCP 110 downloads messages to the client and by default "
                    "deletes them from the server, making multi-device synchronization impossible."
                ),
            },
            {
                "id": "c",
                "text": "SMTP on TCP 25",
                "correct": False,
                "rationale": (
                    "Incorrect. SMTP on TCP 25 is used for sending/relaying outbound mail, not "
                    "for clients to retrieve incoming messages."
                ),
            },
            {
                "id": "d",
                "text": "LDAP on TCP 389",
                "correct": False,
                "rationale": (
                    "Incorrect. LDAP on TCP 389 is a directory services protocol used for "
                    "authentication and directory lookups, not email retrieval."
                ),
            },
        ],
        "explanation": (
            "IMAP (TCP 143) keeps messages on the server and synchronizes state (read/unread, "
            "folders) across all connected clients. POP3 (TCP 110) is simpler but designed for "
            "single-device use; SMTP (TCP 25) is for sending mail; LDAP (TCP 389) handles "
            "directory services."
        ),
    },
    {
        "id": "a1d2-003",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Ports & protocols",
        "stem": (
            "A network technician needs to allow Windows file-sharing (SMB) traffic through a "
            "firewall between two internal VLANs. The firewall currently blocks all inter-VLAN "
            "traffic. Which TCP port must be opened to enable modern SMB/CIFS file sharing?"
        ),
        "options": [
            {
                "id": "a",
                "text": "TCP 445",
                "correct": True,
                "rationale": (
                    "Correct. Modern SMB (SMB2/SMB3 / CIFS) uses TCP 445 directly over TCP/IP "
                    "without requiring NetBIOS. This is the port required for Windows file and "
                    "print sharing in current environments."
                ),
            },
            {
                "id": "b",
                "text": "TCP 139",
                "correct": False,
                "rationale": (
                    "Incorrect. TCP 139 is the older NetBIOS Session Service port used by legacy "
                    "SMB-over-NetBIOS. Modern Windows environments primarily use TCP 445; "
                    "opening 139 alone is insufficient for SMB2/3."
                ),
            },
            {
                "id": "c",
                "text": "UDP 137",
                "correct": False,
                "rationale": (
                    "Incorrect. UDP 137 is NetBIOS Name Service, used for name resolution in "
                    "older NetBIOS environments. It does not carry file-sharing data."
                ),
            },
            {
                "id": "d",
                "text": "TCP 389",
                "correct": False,
                "rationale": (
                    "Incorrect. TCP 389 is LDAP, used for directory service queries, not for "
                    "SMB file sharing."
                ),
            },
        ],
        "explanation": (
            "SMB2 and SMB3 (the protocols behind Windows CIFS file sharing) operate over TCP 445 "
            "directly, bypassing the older NetBIOS layer. Legacy environments also used TCP 139 "
            "(NetBIOS Session) and UDP 137-138 (NetBIOS Name/Datagram), but modern deployments "
            "require TCP 445. Firewalls must permit TCP 445 for inter-VLAN Windows file sharing."
        ),
    },
    {
        "id": "a1d2-004",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Ports & protocols",
        "stem": (
            "A network monitoring system uses SNMP to poll managed devices for interface "
            "statistics and receive unsolicited alerts when thresholds are exceeded. Which "
            "ports must be allowed on the firewall to support both polling and trap reception? "
            "(Select the correct pair.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "UDP 161 for polling and UDP 162 for traps",
                "correct": True,
                "rationale": (
                    "Correct. SNMP managers poll agents on UDP 161; agents send unsolicited trap "
                    "notifications to the manager on UDP 162. Both use UDP."
                ),
            },
            {
                "id": "b",
                "text": "TCP 161 for polling and TCP 162 for traps",
                "correct": False,
                "rationale": (
                    "Incorrect. SNMP uses UDP, not TCP. While SNMPv3 can optionally use TCP in "
                    "some implementations, the standard and exam-relevant transport for SNMP is UDP."
                ),
            },
            {
                "id": "c",
                "text": "UDP 161 for traps and UDP 162 for polling",
                "correct": False,
                "rationale": (
                    "Incorrect. The ports are reversed. UDP 161 is for manager-to-agent queries "
                    "(polling); UDP 162 is for agent-to-manager traps, not the other way around."
                ),
            },
            {
                "id": "d",
                "text": "UDP 514 for polling and UDP 161 for traps",
                "correct": False,
                "rationale": (
                    "Incorrect. UDP 514 is the syslog port used for event logging, not SNMP "
                    "polling. SNMP polling uses UDP 161 and traps use UDP 162."
                ),
            },
        ],
        "explanation": (
            "SNMP (Simple Network Management Protocol) uses UDP for low-overhead polling. "
            "Managers query agents on UDP 161; agents send autonomous trap messages to managers "
            "on UDP 162. Syslog uses UDP 514 and is a separate logging mechanism."
        ),
    },
    {
        "id": "a1d2-005",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Ports & protocols",
        "stem": (
            "A technician wants to verify that DNS is functioning for an internal server by "
            "querying the DNS server directly from a Windows command prompt. DNS operates "
            "primarily over which transport and port?"
        ),
        "options": [
            {
                "id": "a",
                "text": "UDP 53 for most queries; TCP 53 for zone transfers and large responses",
                "correct": True,
                "rationale": (
                    "Correct. DNS uses UDP 53 for standard queries (fast, low overhead). It falls "
                    "back to TCP 53 for responses exceeding 512 bytes and for zone transfers "
                    "between DNS servers."
                ),
            },
            {
                "id": "b",
                "text": "TCP 53 exclusively for all DNS operations",
                "correct": False,
                "rationale": (
                    "Incorrect. DNS does not use TCP exclusively. Standard queries use UDP 53 "
                    "because of lower overhead; TCP 53 is reserved for zone transfers and "
                    "oversized responses."
                ),
            },
            {
                "id": "c",
                "text": "UDP 67 for queries and TCP 68 for responses",
                "correct": False,
                "rationale": (
                    "Incorrect. UDP 67 and 68 are DHCP server and client ports, respectively. "
                    "They have nothing to do with DNS."
                ),
            },
            {
                "id": "d",
                "text": "UDP 53 only; TCP is never used for DNS",
                "correct": False,
                "rationale": (
                    "Incorrect. TCP 53 is legitimately used for DNS zone transfers and when "
                    "responses exceed the UDP limit. Stating TCP is never used is factually wrong."
                ),
            },
        ],
        "explanation": (
            "DNS (Domain Name System) uses UDP 53 for the vast majority of client queries due "
            "to speed. TCP 53 is used when a response is too large for UDP (over 512 bytes in "
            "traditional DNS, or the EDNS0 extended limit) and for DNS zone transfers between "
            "authoritative servers. Firewalls protecting DNS servers must allow both UDP and "
            "TCP on port 53."
        ),
    },
    {
        "id": "a1d2-006",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Ports & protocols",
        "stem": (
            "An administrator is setting up a new DHCP server and notices that DHCP Discover "
            "messages are broadcast by clients. A new client PC sends a DHCP Discover to obtain "
            "an IP address. Which source and destination ports does this initial broadcast use?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Source UDP 68, Destination UDP 67",
                "correct": True,
                "rationale": (
                    "Correct. DHCP clients send Discover messages from UDP port 68 (DHCP client) "
                    "to UDP port 67 (DHCP server) as a broadcast. The server replies from UDP 67 "
                    "to UDP 68."
                ),
            },
            {
                "id": "b",
                "text": "Source UDP 67, Destination UDP 68",
                "correct": False,
                "rationale": (
                    "Incorrect. UDP 67 is the server port; the server uses 67 as its source when "
                    "replying. The client (Discover) initiates from UDP 68 toward UDP 67."
                ),
            },
            {
                "id": "c",
                "text": "Source TCP 68, Destination TCP 67",
                "correct": False,
                "rationale": (
                    "Incorrect. DHCP uses UDP, not TCP, because it operates before a client has "
                    "an IP address and needs broadcast capability."
                ),
            },
            {
                "id": "d",
                "text": "Source UDP 53, Destination UDP 67",
                "correct": False,
                "rationale": (
                    "Incorrect. UDP 53 is the DNS port. DHCP clients use UDP 68 as the source "
                    "port for all DHCP messages."
                ),
            },
        ],
        "explanation": (
            "DHCP uses UDP because the client has no IP address yet and must broadcast. "
            "The DHCP client port is UDP 68 (source on Discover/Request, destination on "
            "Offer/Ack). The DHCP server port is UDP 67 (destination on Discover/Request, "
            "source on Offer/Ack). Remembering '67 server, 68 client' is essential for A+."
        ),
    },
    # ── 2.2  Networking Hardware ────────────────────────────────────────────
    {
        "id": "a1d2-007",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Networking hardware",
        "stem": (
            "A company is deploying 20 IP cameras in a warehouse. No AC outlets are near the "
            "mounting locations, but Cat 6 cable runs have been installed to each camera. "
            "The cameras are 802.3af compliant and draw 12 W each. The existing unmanaged "
            "switch does NOT support PoE. What is the MOST cost-effective solution to power "
            "the cameras without replacing the switch?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Install a PoE injector at each camera location to add power to the existing Cat 6 runs",
                "correct": True,
                "rationale": (
                    "Correct. A PoE injector (also called a midspan) is placed between the "
                    "non-PoE switch and each camera, injecting DC power onto the cable. This "
                    "avoids replacing the switch and is cost-effective for a moderate number "
                    "of devices."
                ),
            },
            {
                "id": "b",
                "text": "Replace the unmanaged switch with a managed PoE switch rated for 802.3at",
                "correct": False,
                "rationale": (
                    "Incorrect. While this would work and is common in new deployments, it is "
                    "not the most cost-effective solution since it requires replacing functional "
                    "infrastructure. PoE injectors preserve the existing switch."
                ),
            },
            {
                "id": "c",
                "text": "Use a PoE splitter at the switch to separate power and data before sending over Cat 6",
                "correct": False,
                "rationale": (
                    "Incorrect. A PoE splitter is placed at the powered device end to separate "
                    "PoE power into a barrel connector for non-PoE devices. It does not add PoE "
                    "capability to a non-PoE switch port."
                ),
            },
            {
                "id": "d",
                "text": "Run 802.3bt cabling to the cameras to carry both data and power",
                "correct": False,
                "rationale": (
                    "Incorrect. 802.3bt is a PoE standard (not a cabling type) that defines "
                    "higher power delivery. Cabling type (Cat 6) does not determine PoE capability; "
                    "the switch or injector must supply the power."
                ),
            },
        ],
        "explanation": (
            "PoE injectors (midspan devices) add PoE capability to individual non-PoE switch "
            "ports, making them the most economical retrofit when replacing a switch is "
            "unnecessary. 802.3af delivers up to 15.4 W per port (12.95 W at device); "
            "802.3at (PoE+) delivers up to 30 W; 802.3bt (PoE++) up to 90 W. Splitters are "
            "used at the far end to power non-PoE devices from a PoE source."
        ),
    },
    {
        "id": "a1d2-008",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Networking hardware",
        "stem": (
            "A technician troubleshooting a network finds that every device connected to a "
            "particular network segment experiences collisions and degraded performance as more "
            "hosts are added. All devices are connected to a central device that does not "
            "perform frame filtering or MAC address learning. Which device is causing the issue?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Hub",
                "correct": True,
                "rationale": (
                    "Correct. A hub is a Layer 1 device that repeats all received signals to "
                    "every port, creating a single collision domain. As more devices are added, "
                    "collisions increase and performance degrades proportionally."
                ),
            },
            {
                "id": "b",
                "text": "Unmanaged switch",
                "correct": False,
                "rationale": (
                    "Incorrect. An unmanaged switch learns MAC addresses and forwards frames "
                    "only to the appropriate port, segmenting collision domains. It does not "
                    "cause the described collision behavior."
                ),
            },
            {
                "id": "c",
                "text": "Managed switch",
                "correct": False,
                "rationale": (
                    "Incorrect. A managed switch also performs MAC address learning and creates "
                    "per-port collision domains, preventing the collision problem described."
                ),
            },
            {
                "id": "d",
                "text": "Access point in infrastructure mode",
                "correct": False,
                "rationale": (
                    "Incorrect. An 802.11 access point in infrastructure mode acts as a bridge "
                    "and does manage MAC-level frame forwarding; while the wireless medium has "
                    "its own contention issues (CSMA/CA), it is not the device described."
                ),
            },
        ],
        "explanation": (
            "A hub operates at OSI Layer 1 and is a simple electrical signal repeater. It "
            "creates one large collision domain — every device competes for the same bandwidth "
            "using CSMA/CD. Switches replaced hubs because they perform MAC learning and create "
            "a separate collision domain per port, virtually eliminating collisions on "
            "full-duplex links."
        ),
    },
    {
        "id": "a1d2-009",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Networking hardware",
        "stem": (
            "An enterprise is redesigning its data center and wants to decouple the network "
            "control plane from the forwarding plane so that a centralized controller can "
            "programmatically manage traffic flows across heterogeneous switches. Which "
            "networking paradigm should be implemented?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Software-Defined Networking (SDN)",
                "correct": True,
                "rationale": (
                    "Correct. SDN separates the control plane (centralized controller making "
                    "routing/switching decisions) from the data plane (switches forwarding "
                    "packets), allowing programmatic, vendor-agnostic network management "
                    "through APIs such as OpenFlow."
                ),
            },
            {
                "id": "b",
                "text": "VLAN trunking with 802.1Q",
                "correct": False,
                "rationale": (
                    "Incorrect. 802.1Q VLAN trunking segments broadcast domains but does not "
                    "separate control and forwarding planes or enable centralized programmatic "
                    "control across heterogeneous hardware."
                ),
            },
            {
                "id": "c",
                "text": "Spanning Tree Protocol (STP)",
                "correct": False,
                "rationale": (
                    "Incorrect. STP prevents Layer 2 loops in redundant topologies but does not "
                    "centralize control-plane logic or decouple it from forwarding hardware."
                ),
            },
            {
                "id": "d",
                "text": "Network Address Translation (NAT)",
                "correct": False,
                "rationale": (
                    "Incorrect. NAT translates private IP addresses to public addresses for "
                    "internet connectivity. It is a Layer 3 function unrelated to SDN's "
                    "control/data-plane separation."
                ),
            },
        ],
        "explanation": (
            "Software-Defined Networking (SDN) abstracts the network control plane into a "
            "centralized software controller, which communicates with forwarding hardware "
            "(switches, routers) via southbound APIs like OpenFlow. This enables dynamic, "
            "policy-driven traffic engineering across multi-vendor environments — a key "
            "concept in modern data-center and cloud networking."
        ),
    },
    {
        "id": "a1d2-010",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "PoE",
        "stem": (
            "A technician needs to power a new VoIP phone that requires 25 W of continuous "
            "power. The existing switch supports IEEE 802.3af PoE on all ports. Why will the "
            "switch port be unable to power the phone, and what standard is needed?"
        ),
        "options": [
            {
                "id": "a",
                "text": "802.3af delivers a maximum of 15.4 W at the switch port (12.95 W at the device); 802.3at (PoE+) delivering up to 30 W is required",
                "correct": True,
                "rationale": (
                    "Correct. IEEE 802.3af (PoE) provides up to 15.4 W at the port and "
                    "approximately 12.95 W at the powered device after cable loss. A 25 W device "
                    "requires 802.3at (PoE+), which delivers up to 30 W at the port."
                ),
            },
            {
                "id": "b",
                "text": "802.3af only supports two-pair (Mode A) power delivery; upgrading to four-pair cabling is required",
                "correct": False,
                "rationale": (
                    "Incorrect. The limitation is maximum wattage, not the number of pairs. "
                    "802.3af uses two pairs; 802.3bt uses four pairs for even higher power, but "
                    "the issue here is that 802.3af's 15.4 W ceiling is below the 25 W requirement."
                ),
            },
            {
                "id": "c",
                "text": "802.3af requires Cat 6a cabling; Cat 5e runs cannot carry PoE at any power level",
                "correct": False,
                "rationale": (
                    "Incorrect. 802.3af operates over Cat 3 or better cabling. Cabling category "
                    "is not the constraint here — the wattage limit is."
                ),
            },
            {
                "id": "d",
                "text": "802.3af is a wireless standard and cannot deliver power over Ethernet cabling",
                "correct": False,
                "rationale": (
                    "Incorrect. 802.3af is an IEEE wired Ethernet standard (IEEE 802.3 family) "
                    "for Power over Ethernet. 802.11 standards govern wireless Ethernet."
                ),
            },
        ],
        "explanation": (
            "IEEE 802.3af (PoE): up to 15.4 W at port, ~12.95 W at device. "
            "IEEE 802.3at (PoE+): up to 30 W at port, ~25.5 W at device. "
            "IEEE 802.3bt (PoE++): Type 3 up to 60 W, Type 4 up to 100 W at port. "
            "Always match the standard to the device's power requirement when deploying PoE."
        ),
    },
    # ── 2.3  Wireless Standards ──────────────────────────────────────────────
    {
        "id": "a1d2-011",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Wireless standards",
        "stem": (
            "A technician is deploying Wi-Fi in a high-density auditorium where hundreds of "
            "devices will connect simultaneously. The organization wants the highest possible "
            "throughput and improved performance in congested environments. The APs and all "
            "client devices support the latest 802.11 standard. Which standard should be selected?"
        ),
        "options": [
            {
                "id": "a",
                "text": "802.11ax (Wi-Fi 6/6E)",
                "correct": True,
                "rationale": (
                    "Correct. 802.11ax (Wi-Fi 6, Wi-Fi 6E) introduces OFDMA, MU-MIMO (up to "
                    "8x8), BSS Coloring, and Target Wake Time specifically to improve efficiency "
                    "and throughput in high-density environments, making it the best choice."
                ),
            },
            {
                "id": "b",
                "text": "802.11ac (Wi-Fi 5)",
                "correct": False,
                "rationale": (
                    "Incorrect. 802.11ac (Wi-Fi 5) offers high single-client throughput via "
                    "MU-MIMO (downlink only) and operates on 5 GHz, but lacks the OFDMA and "
                    "BSS Coloring features of 802.11ax that specifically address dense deployments."
                ),
            },
            {
                "id": "c",
                "text": "802.11n (Wi-Fi 4)",
                "correct": False,
                "rationale": (
                    "Incorrect. 802.11n (Wi-Fi 4) supports 2.4 and 5 GHz and introduced "
                    "MIMO, but its maximum throughput (~600 Mbps) and lack of OFDMA make it "
                    "inferior to 802.11ax for dense deployments."
                ),
            },
            {
                "id": "d",
                "text": "802.11a",
                "correct": False,
                "rationale": (
                    "Incorrect. 802.11a is a legacy standard offering up to 54 Mbps on 5 GHz. "
                    "It has no MU-MIMO or OFDMA, making it wholly unsuitable for high-density "
                    "modern deployments."
                ),
            },
        ],
        "explanation": (
            "802.11ax (Wi-Fi 6) uses OFDMA to serve multiple clients simultaneously within a "
            "single channel, BSS Coloring to reduce co-channel interference, and up to 8x8 "
            "MU-MIMO in both uplink and downlink directions. Wi-Fi 6E extends into the 6 GHz "
            "band. These features make 802.11ax dramatically better than prior standards in "
            "high-density scenarios like stadiums, conference centers, and open offices."
        ),
    },
    {
        "id": "a1d2-012",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Wi-Fi channels & frequencies",
        "stem": (
            "A SOHO network experiences significant 2.4 GHz Wi-Fi interference from neighboring "
            "networks. A wireless survey shows channels 2, 3, 4, 5, 7, 8, 9, 10, and 11 are "
            "heavily used by neighbors. Which channel(s) should the technician configure to "
            "avoid overlapping with the heavily used channels?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Channel 1 only",
                "correct": True,
                "rationale": (
                    "Correct. In the 2.4 GHz band, only channels 1, 6, and 11 are non-overlapping "
                    "in North America. Channel 11 is heavily occupied in this scenario; channels "
                    "2-5 overlap with channel 1 and 6; channels 7-10 overlap with 6 and 11. "
                    "Channel 1 is the only non-overlapping choice not heavily used."
                ),
            },
            {
                "id": "b",
                "text": "Channel 3",
                "correct": False,
                "rationale": (
                    "Incorrect. Channel 3 overlaps with channels 1 and 6 in the 2.4 GHz band "
                    "and is listed as already heavily occupied by neighbors."
                ),
            },
            {
                "id": "c",
                "text": "Channel 6",
                "correct": False,
                "rationale": (
                    "Incorrect. While channel 6 is one of the three non-overlapping channels, "
                    "the scenario states channels 7-10 are heavily used, and channel 6 partially "
                    "overlaps with channels 3-9; more importantly, it is not non-overlapping with "
                    "the specifically stated heavy channels the way channel 1 clearly stands apart."
                ),
            },
            {
                "id": "d",
                "text": "Channel 14",
                "correct": False,
                "rationale": (
                    "Incorrect. Channel 14 is only available in Japan for 802.11b and is not "
                    "usable in North America. It is not a valid selection for a SOHO deployment."
                ),
            },
        ],
        "explanation": (
            "The 2.4 GHz band has 11 usable channels in North America (14 in Japan), but only "
            "channels 1, 6, and 11 are non-overlapping (each 22 MHz wide, spaced 25 MHz apart). "
            "All other channels overlap with at least one of these three. When channels 6 and 11 "
            "are occupied, channel 1 is the correct choice to minimize interference."
        ),
    },
    {
        "id": "a1d2-013",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Wireless standards",
        "stem": (
            "A site survey reveals that a manufacturing floor's wireless network suffers from "
            "substantial co-channel interference between access points on 5 GHz. The current "
            "APs support 802.11ac Wave 2. The technician wants to maximize available "
            "non-overlapping channels to reduce inter-AP interference. How many non-overlapping "
            "20 MHz channels are available in the 5 GHz band in the United States (including "
            "UNII-1, UNII-2, UNII-2e, and UNII-3)?"
        ),
        "options": [
            {
                "id": "a",
                "text": "25 non-overlapping 20 MHz channels",
                "correct": True,
                "rationale": (
                    "Correct. The 5 GHz U-NII bands in the US provide 25 non-overlapping 20 MHz "
                    "channels across UNII-1 (36, 40, 44, 48), UNII-2A (52, 56, 60, 64), "
                    "UNII-2C/2e (100, 104, 108, 112, 116, 120, 124, 128, 132, 136, 140, 144), "
                    "and UNII-3 (149, 153, 157, 161, 165). This contrasts sharply with the "
                    "2.4 GHz band's only 3 non-overlapping channels."
                ),
            },
            {
                "id": "b",
                "text": "3 non-overlapping 20 MHz channels",
                "correct": False,
                "rationale": (
                    "Incorrect. Three non-overlapping channels (1, 6, 11) is the count for the "
                    "2.4 GHz band, not the 5 GHz band."
                ),
            },
            {
                "id": "c",
                "text": "11 non-overlapping 20 MHz channels",
                "correct": False,
                "rationale": (
                    "Incorrect. Eleven is the total number of channels available in the 2.4 GHz "
                    "band in North America (of which only 3 are non-overlapping). The 5 GHz band "
                    "offers far more."
                ),
            },
            {
                "id": "d",
                "text": "8 non-overlapping 20 MHz channels",
                "correct": False,
                "rationale": (
                    "Incorrect. Eight channels represents roughly the UNII-1 and UNII-3 bands "
                    "only. Including UNII-2 and UNII-2e expands the count to 25."
                ),
            },
        ],
        "explanation": (
            "The 5 GHz band's much larger spectrum provides 25 non-overlapping 20 MHz channels "
            "in the US, compared to only 3 in the 2.4 GHz band. This makes 5 GHz far superior "
            "for dense AP deployments. Note that UNII-2 and UNII-2e channels require DFS "
            "(Dynamic Frequency Selection) to avoid interference with radar systems."
        ),
    },
    {
        "id": "a1d2-014",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Wireless standards",
        "stem": (
            "A hospital wants to implement a patient-wristband tracking system and also allow "
            "contactless payment at kiosks. Both systems require very short-range, low-power "
            "wireless communication (under 20 cm). Which two wireless technologies are MOST "
            "appropriate? (Choose the answer that identifies both correctly.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "RFID for wristband tracking; NFC for contactless payment",
                "correct": True,
                "rationale": (
                    "Correct. RFID (Radio Frequency Identification) is used in asset and patient "
                    "tracking tags. NFC (Near Field Communication) operates at 13.56 MHz over "
                    "~4 cm and is the standard for contactless payments (Apple Pay, tap-to-pay). "
                    "Both are appropriate and distinct technologies."
                ),
            },
            {
                "id": "b",
                "text": "Bluetooth LE for wristband tracking; Wi-Fi Direct for contactless payment",
                "correct": False,
                "rationale": (
                    "Incorrect. Bluetooth LE works up to ~100 m and Wi-Fi Direct up to ~200 m — "
                    "neither is designed for the sub-20 cm proximity required, and Wi-Fi Direct "
                    "is not a payment standard."
                ),
            },
            {
                "id": "c",
                "text": "NFC for wristband tracking; Zigbee for contactless payment",
                "correct": False,
                "rationale": (
                    "Incorrect. While NFC could theoretically track wristbands, RFID is the "
                    "industry-standard technology for asset/patient tags. Zigbee is a mesh "
                    "networking protocol (not a payment standard) used in IoT, not contactless "
                    "payment."
                ),
            },
            {
                "id": "d",
                "text": "802.11ax for wristband tracking; Bluetooth 5 for contactless payment",
                "correct": False,
                "rationale": (
                    "Incorrect. 802.11ax is a long-range Wi-Fi standard. Bluetooth 5 supports "
                    "up to 40 m — neither is designed for sub-20 cm proximity use cases like "
                    "wristband scanning or contactless payment."
                ),
            },
        ],
        "explanation": (
            "RFID uses electromagnetic fields to automatically identify and track tags attached "
            "to objects; passive tags have no battery and work at short range, making them ideal "
            "for wristband or asset tracking. NFC is a subset of RFID technology standardized "
            "at 13.56 MHz with a maximum range of about 4 cm, optimized for secure contactless "
            "transactions and data exchange between devices."
        ),
    },
    {
        "id": "a1d2-015",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Wireless standards",
        "stem": (
            "A small office has an older 802.11n access point that supports only 2.4 GHz. "
            "A new employee's laptop lists 'Wi-Fi 5' in its network adapter properties. "
            "The laptop associates with the AP but achieves only ~150 Mbps instead of the "
            "expected higher throughput. What is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Wi-Fi 5 (802.11ac) operates exclusively on 5 GHz; the laptop is falling back to 802.11n on 2.4 GHz",
                "correct": True,
                "rationale": (
                    "Correct. 802.11ac (Wi-Fi 5) only operates on the 5 GHz band. Since the AP "
                    "is 802.11n/2.4 GHz only, the laptop must use 802.11n compatibility mode "
                    "on 2.4 GHz, limiting speeds to 802.11n rates (~150 Mbps with one spatial "
                    "stream on 2.4 GHz)."
                ),
            },
            {
                "id": "b",
                "text": "The laptop's Wi-Fi adapter is defective because Wi-Fi 5 should work on 2.4 GHz",
                "correct": False,
                "rationale": (
                    "Incorrect. 802.11ac is not defective; it is designed to operate only on "
                    "5 GHz by specification. The laptop correctly falls back to 802.11n/2.4 GHz."
                ),
            },
            {
                "id": "c",
                "text": "The 2.4 GHz channel width is set to 40 MHz, halving available bandwidth",
                "correct": False,
                "rationale": (
                    "Incorrect. A 40 MHz channel on 2.4 GHz would actually increase, not decrease, "
                    "throughput compared to 20 MHz. It does not explain the fallback from Wi-Fi 5 "
                    "speeds."
                ),
            },
            {
                "id": "d",
                "text": "WPA3 encryption overhead is throttling the connection speed",
                "correct": False,
                "rationale": (
                    "Incorrect. WPA3 does not cause measurable throughput reduction on modern "
                    "hardware. The throughput limitation is a consequence of band/standard "
                    "mismatch, not encryption overhead."
                ),
            },
        ],
        "explanation": (
            "IEEE 802.11ac (Wi-Fi 5) was defined exclusively for the 5 GHz band, unlike "
            "802.11n which supports both 2.4 and 5 GHz. When a Wi-Fi 5 client connects to a "
            "2.4 GHz-only AP, it negotiates 802.11n (or earlier) mode. Upgrading to a dual-band "
            "or tri-band AP supporting 5 GHz is necessary to achieve Wi-Fi 5 speeds."
        ),
    },
    {
        "id": "a1d2-016",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Wireless standards",
        "stem": (
            "An organization is evaluating WPA3-Enterprise for a new wireless deployment. "
            "A security architect notes that WPA2's TKIP cipher has known vulnerabilities "
            "and should be avoided. WPA3 mandates which encryption standard and what key "
            "length to eliminate TKIP weaknesses?"
        ),
        "options": [
            {
                "id": "a",
                "text": "AES-128 (CCMP) as the minimum cipher; WPA3-Enterprise optionally mandates AES-192 in 192-bit mode",
                "correct": True,
                "rationale": (
                    "Correct. WPA3 requires AES-based CCMP (Counter Mode with CBC-MAC Protocol) "
                    "and completely removes TKIP support. WPA3-Enterprise offers a 192-bit "
                    "security mode using AES-256-GCMP for environments requiring higher assurance."
                ),
            },
            {
                "id": "b",
                "text": "TKIP with a 256-bit key as the minimum cipher",
                "correct": False,
                "rationale": (
                    "Incorrect. TKIP (Temporal Key Integrity Protocol) is explicitly deprecated "
                    "and not permitted in WPA3. WPA3 removes TKIP entirely in favor of AES-based "
                    "ciphers."
                ),
            },
            {
                "id": "c",
                "text": "3DES-128 with CCMP key wrapping",
                "correct": False,
                "rationale": (
                    "Incorrect. 3DES is not used in 802.11 wireless security standards. "
                    "Wi-Fi security uses AES; 3DES appears in legacy VPN and encrypted "
                    "protocols like older TLS versions."
                ),
            },
            {
                "id": "d",
                "text": "WEP with a 128-bit shared key",
                "correct": False,
                "rationale": (
                    "Incorrect. WEP (Wired Equivalent Privacy) is a completely broken legacy "
                    "protocol deprecated years before WPA3. WPA3 offers the highest current "
                    "security and bears no relation to WEP."
                ),
            },
        ],
        "explanation": (
            "WPA3 was ratified in 2018 and mandates AES/CCMP, eliminating the vulnerable "
            "RC4-based TKIP used in WPA/WEP. WPA3-Personal uses SAE (Simultaneous "
            "Authentication of Equals) replacing PSK handshakes. WPA3-Enterprise adds a "
            "192-bit security mode using AES-256-GCMP and SHA-384 for government/financial "
            "environments."
        ),
    },
    # ── 2.4  Network Services ────────────────────────────────────────────────
    {
        "id": "a1d2-017",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network services",
        "stem": (
            "A company wants a single appliance that combines a firewall, IPS/IDS, "
            "antivirus gateway, web content filtering, and VPN into one device to reduce "
            "hardware complexity at branch offices. Which appliance category meets this requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Unified Threat Management (UTM) appliance",
                "correct": True,
                "rationale": (
                    "Correct. A UTM appliance integrates multiple security functions — firewall, "
                    "IPS/IDS, antivirus, web filtering, and VPN — into a single device. It is "
                    "the standard solution for branch-office security consolidation."
                ),
            },
            {
                "id": "b",
                "text": "Spam gateway",
                "correct": False,
                "rationale": (
                    "Incorrect. A spam gateway (email security gateway) filters inbound and "
                    "outbound email for spam and malware. It does not provide firewall, IPS, "
                    "or VPN functionality."
                ),
            },
            {
                "id": "c",
                "text": "Load balancer",
                "correct": False,
                "rationale": (
                    "Incorrect. A load balancer distributes traffic across multiple servers to "
                    "ensure availability and performance. It is not a security-focused multi-function "
                    "device."
                ),
            },
            {
                "id": "d",
                "text": "Proxy server",
                "correct": False,
                "rationale": (
                    "Incorrect. A proxy server intermediates client requests (often for caching "
                    "or content filtering), but does not natively incorporate IPS, antivirus, "
                    "or VPN capabilities."
                ),
            },
        ],
        "explanation": (
            "UTM (Unified Threat Management) consolidates network security functions into a "
            "single managed platform. It typically includes stateful firewall, VPN, intrusion "
            "prevention, antivirus/anti-malware gateway, web filtering, and spam filtering. "
            "This reduces cost, complexity, and management overhead compared to deploying each "
            "function as a separate appliance."
        ),
    },
    {
        "id": "a1d2-018",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network services",
        "stem": (
            "A company's web servers frequently become overwhelmed during peak traffic, "
            "causing some servers to fail while others remain underutilized. The operations "
            "team wants to distribute incoming HTTP/HTTPS requests across multiple identical "
            "web servers to maximize availability and prevent overload. Which network appliance "
            "should be deployed?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Load balancer",
                "correct": True,
                "rationale": (
                    "Correct. A load balancer distributes incoming client requests across a pool "
                    "of backend servers using algorithms such as round-robin, least connections, "
                    "or weighted distribution, preventing any single server from being overwhelmed."
                ),
            },
            {
                "id": "b",
                "text": "Reverse proxy",
                "correct": False,
                "rationale": (
                    "Incorrect. While a reverse proxy can provide load-balancing features, it "
                    "is primarily described as an intermediary that handles client requests on "
                    "behalf of servers. The device explicitly designed and marketed for server "
                    "load distribution is the load balancer."
                ),
            },
            {
                "id": "c",
                "text": "UTM appliance",
                "correct": False,
                "rationale": (
                    "Incorrect. A UTM appliance focuses on security (firewall, IPS, AV, VPN) "
                    "and is not designed to distribute web traffic across server pools."
                ),
            },
            {
                "id": "d",
                "text": "Managed switch with VLAN trunking",
                "correct": False,
                "rationale": (
                    "Incorrect. VLAN trunking segments network traffic but does not intelligently "
                    "distribute application-layer requests across multiple servers."
                ),
            },
        ],
        "explanation": (
            "Load balancers operate at Layer 4 (transport) or Layer 7 (application) to "
            "distribute incoming connections across a server farm. They monitor server health "
            "and remove failed nodes from the pool, dramatically improving web application "
            "availability and scalability."
        ),
    },
    {
        "id": "a1d2-019",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network services",
        "stem": (
            "A company's syslog server collects logs from routers, switches, and firewalls. "
            "A network event causes a router to send syslog messages to the server. "
            "Which default port and transport does syslog use?"
        ),
        "options": [
            {
                "id": "a",
                "text": "UDP 514",
                "correct": True,
                "rationale": (
                    "Correct. Traditional syslog (RFC 3164) uses UDP 514. UDP is used because "
                    "syslog is a one-way, fire-and-forget notification; delivery confirmation "
                    "is not built in. Newer RFC 5424 (syslog over TLS) uses TCP 6514."
                ),
            },
            {
                "id": "b",
                "text": "TCP 514",
                "correct": False,
                "rationale": (
                    "Incorrect. Classic syslog uses UDP 514. TCP 514 is not the standard syslog "
                    "port. TCP 6514 is used for encrypted syslog over TLS (RFC 5425)."
                ),
            },
            {
                "id": "c",
                "text": "UDP 161",
                "correct": False,
                "rationale": (
                    "Incorrect. UDP 161 is the SNMP agent port for polling, not syslog. "
                    "SNMP and syslog are separate logging/monitoring mechanisms."
                ),
            },
            {
                "id": "d",
                "text": "TCP 162",
                "correct": False,
                "rationale": (
                    "Incorrect. UDP 162 is the SNMP trap port. It is not related to syslog "
                    "and uses UDP, not TCP."
                ),
            },
        ],
        "explanation": (
            "Syslog is the de facto standard for network device logging. Traditional syslog "
            "uses UDP 514 for simplicity and low overhead — messages are sent without "
            "acknowledgment. For environments requiring reliable, encrypted log delivery, "
            "TLS syslog (RFC 5425) uses TCP 6514. A syslog server aggregates messages from "
            "many devices for centralized analysis and alerting."
        ),
    },
    # ── 2.5  SOHO Networks, IP Addressing ───────────────────────────────────
    {
        "id": "a1d2-020",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "IPv4 addressing & APIPA",
        "stem": (
            "A workstation configured for DHCP shows an IP address of 169.254.18.7 and "
            "cannot reach the internet or other LAN hosts. Other devices on the same switch "
            "get 192.168.1.x addresses normally. What is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The client could not reach a DHCP server and self-assigned an APIPA address",
                "correct": True,
                "rationale": (
                    "Correct. 169.254.0.0/16 is the APIPA range a host assigns itself when no "
                    "DHCP server responds. Since other hosts get leases, the issue is this "
                    "client's path to DHCP (cable, port, NIC) rather than the DHCP server."
                ),
            },
            {
                "id": "b",
                "text": "The DHCP scope ran out of addresses for the entire subnet",
                "correct": False,
                "rationale": (
                    "Incorrect. If the scope were exhausted, other new clients would also fail "
                    "to get leases. Since other devices receive 192.168.1.x addresses normally, "
                    "the scope is not exhausted."
                ),
            },
            {
                "id": "c",
                "text": "The workstation has been assigned a valid public IP address",
                "correct": False,
                "rationale": (
                    "Incorrect. 169.254.x.x is a link-local APIPA address and is non-routable, "
                    "not a public IP address."
                ),
            },
            {
                "id": "d",
                "text": "The default gateway is misconfigured on the router",
                "correct": False,
                "rationale": (
                    "Incorrect. An APIPA address means the host never obtained any DHCP "
                    "configuration. A router gateway misconfiguration would not cause a host "
                    "to self-assign 169.254.x.x."
                ),
            },
        ],
        "explanation": (
            "APIPA (Automatic Private IP Addressing) assigns a 169.254.0.0/16 address when "
            "a DHCP client receives no response. When only one host shows an APIPA address "
            "while others lease normally, suspect that host's physical connectivity to the "
            "DHCP server: check NIC, cable, and switch port."
        ),
    },
    {
        "id": "a1d2-021",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "IPv4 addressing & APIPA",
        "stem": (
            "A technician is given the network 192.168.10.0 with a subnet mask of "
            "255.255.255.192. How many usable host addresses are available per subnet, "
            "and how many subnets does this mask create from the Class C base?"
        ),
        "options": [
            {
                "id": "a",
                "text": "62 usable hosts per subnet; 4 subnets",
                "correct": True,
                "rationale": (
                    "Correct. /26 (255.255.255.192) borrows 2 bits from the host portion of a "
                    "Class C, creating 2^2 = 4 subnets. Each subnet has 2^6 = 64 addresses, "
                    "minus 2 (network and broadcast) = 62 usable hosts."
                ),
            },
            {
                "id": "b",
                "text": "30 usable hosts per subnet; 8 subnets",
                "correct": False,
                "rationale": (
                    "Incorrect. 30 usable hosts corresponds to /27 (255.255.255.224, 8 subnets "
                    "from a Class C). 255.255.255.192 is /26, giving 62 usable hosts and 4 subnets."
                ),
            },
            {
                "id": "c",
                "text": "126 usable hosts per subnet; 2 subnets",
                "correct": False,
                "rationale": (
                    "Incorrect. 126 usable hosts corresponds to /25 (255.255.255.128), which "
                    "borrows only 1 bit for 2 subnets of 126 hosts each. /26 gives 62 hosts."
                ),
            },
            {
                "id": "d",
                "text": "14 usable hosts per subnet; 16 subnets",
                "correct": False,
                "rationale": (
                    "Incorrect. 14 usable hosts corresponds to /28 (255.255.255.240), "
                    "which borrows 4 bits for 16 subnets. 255.255.255.192 is /26."
                ),
            },
        ],
        "explanation": (
            "Subnet mask 255.255.255.192 = /26. For a Class C (/24 base): borrowed bits = "
            "26-24 = 2, so 2^2 = 4 subnets. Host bits remaining = 32-26 = 6, so 2^6-2 = 62 "
            "usable hosts per subnet. The four subnets are .0, .64, .128, and .192."
        ),
    },
    {
        "id": "a1d2-022",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "IPv6 addressing",
        "stem": (
            "A technician examines a workstation and finds its IPv6 address begins with "
            "fe80::. The workstation cannot reach any resources outside the local network "
            "segment. What does this address indicate, and what is required for internet "
            "connectivity?"
        ),
        "options": [
            {
                "id": "a",
                "text": "fe80::/10 is a link-local address auto-configured on every IPv6 interface; a global unicast address (2000::/3) obtained via SLAAC or DHCPv6 is required for external routing",
                "correct": True,
                "rationale": (
                    "Correct. fe80::/10 is the IPv6 link-local prefix automatically assigned "
                    "to every IPv6-capable interface using the EUI-64 method or random IID. "
                    "Link-local addresses are non-routable beyond the local link. A global "
                    "unicast address (prefix 2000::/3) is required for internet communication."
                ),
            },
            {
                "id": "b",
                "text": "fe80:: is an APIPA equivalent for IPv6, meaning DHCPv6 is unavailable",
                "correct": False,
                "rationale": (
                    "Incorrect. Unlike IPv4 APIPA (169.254.x.x), IPv6 link-local (fe80::) is "
                    "a normal, always-present address on all IPv6 interfaces — it does not "
                    "indicate a failure to reach a DHCPv6 server."
                ),
            },
            {
                "id": "c",
                "text": "fe80:: is a global unicast address that should be routable; the default gateway is missing",
                "correct": False,
                "rationale": (
                    "Incorrect. fe80::/10 is explicitly defined as a link-local range and is "
                    "never routable beyond the local link, regardless of gateway configuration."
                ),
            },
            {
                "id": "d",
                "text": "fe80:: addresses are only assigned by DHCPv6 and indicate a DHCP lease was received",
                "correct": False,
                "rationale": (
                    "Incorrect. Link-local (fe80::) addresses are auto-configured by the "
                    "interface itself using EUI-64 or random IID — they do not require DHCPv6."
                ),
            },
        ],
        "explanation": (
            "Every IPv6 interface automatically configures a link-local address in the "
            "fe80::/10 range. This address is used for neighbor discovery and local "
            "communication only. For internet connectivity, the host must obtain a global "
            "unicast address (2000::/3) via SLAAC (Stateless Address Autoconfiguration) "
            "using Router Advertisements, or from a DHCPv6 server."
        ),
    },
    {
        "id": "a1d2-023",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "DHCP",
        "stem": (
            "A network administrator wants to ensure that a specific server always receives "
            "the same IP address from the DHCP server based on its MAC address, without "
            "manually configuring a static IP on the server itself. Which DHCP feature "
            "should be configured?"
        ),
        "options": [
            {
                "id": "a",
                "text": "DHCP reservation (static mapping)",
                "correct": True,
                "rationale": (
                    "Correct. A DHCP reservation maps a specific MAC address to a fixed IP "
                    "address in the DHCP server's database. The client still uses DHCP to "
                    "obtain its address dynamically, but always receives the same reserved IP."
                ),
            },
            {
                "id": "b",
                "text": "DHCP exclusion range",
                "correct": False,
                "rationale": (
                    "Incorrect. A DHCP exclusion range prevents the server from assigning "
                    "certain IP addresses from the scope (e.g., to protect addresses already "
                    "manually assigned), but does not map a specific MAC to a specific IP."
                ),
            },
            {
                "id": "c",
                "text": "DHCP scope option 003 (default gateway)",
                "correct": False,
                "rationale": (
                    "Incorrect. DHCP scope option 003 sends the default gateway address to "
                    "all clients in the scope. It does not create a MAC-to-IP mapping."
                ),
            },
            {
                "id": "d",
                "text": "Static IP address configured on the server's NIC",
                "correct": False,
                "rationale": (
                    "Incorrect. Configuring a static IP directly on the NIC removes the server "
                    "from DHCP management and requires manual configuration on the server. The "
                    "question specifically asks for a method that does not require changing the "
                    "server's network settings."
                ),
            },
        ],
        "explanation": (
            "A DHCP reservation (also called a static mapping or IP-MAC binding) allows the "
            "DHCP server to always issue the same IP address to a device identified by its "
            "MAC address. This is preferred over manual static IP assignment for servers "
            "that need predictable addresses while remaining centrally managed via DHCP."
        ),
    },
    {
        "id": "a1d2-024",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "DNS records",
        "stem": (
            "An organization's email administrator wants to prevent spammers from sending "
            "emails that appear to come from the company's domain. The administrator publishes "
            "a DNS TXT record that lists all authorized mail servers by IP address/range. "
            "Which anti-spoofing mechanism is this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "SPF (Sender Policy Framework)",
                "correct": True,
                "rationale": (
                    "Correct. SPF is published as a DNS TXT record in the format "
                    "'v=spf1 ...' and specifies which mail servers are authorized to send "
                    "email on behalf of the domain. Receiving mail servers check this record "
                    "to validate the sender."
                ),
            },
            {
                "id": "b",
                "text": "DKIM (DomainKeys Identified Mail)",
                "correct": False,
                "rationale": (
                    "Incorrect. DKIM uses a cryptographic signature in the email header and "
                    "publishes a public key as a DNS TXT record. It verifies message integrity "
                    "and sender authenticity but does not list authorized sending IPs."
                ),
            },
            {
                "id": "c",
                "text": "DMARC (Domain-based Message Authentication, Reporting, and Conformance)",
                "correct": False,
                "rationale": (
                    "Incorrect. DMARC builds on SPF and DKIM by specifying a policy for what "
                    "to do when those checks fail (quarantine, reject, or none). It is not "
                    "itself the record that lists authorized mail server IPs."
                ),
            },
            {
                "id": "d",
                "text": "MX (Mail Exchanger) record",
                "correct": False,
                "rationale": (
                    "Incorrect. An MX record identifies which mail servers should receive "
                    "incoming email for a domain. It does not list authorized outbound sending "
                    "servers or prevent spoofing."
                ),
            },
        ],
        "explanation": (
            "SPF (Sender Policy Framework) is a DNS TXT record that enumerates IP addresses "
            "and ranges authorized to send mail for a domain (e.g., 'v=spf1 ip4:203.0.113.0/24 "
            "include:_spf.google.com ~all'). Receiving servers validate inbound mail against "
            "this record to detect spoofed senders. DKIM adds a cryptographic signature; "
            "DMARC provides policy enforcement and reporting using SPF and DKIM results."
        ),
    },
    {
        "id": "a1d2-025",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "DNS records",
        "stem": (
            "A company is migrating its website to a new hosting provider. The new host "
            "provides an IP address of 203.0.113.55 for the web server. The technician "
            "must update DNS so that www.company.com resolves to the new IP. Which DNS "
            "record type should be created?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A record mapping www.company.com to 203.0.113.55",
                "correct": True,
                "rationale": (
                    "Correct. An A (Address) record maps a hostname to an IPv4 address. "
                    "Creating an A record for www.company.com pointing to 203.0.113.55 is "
                    "the correct action."
                ),
            },
            {
                "id": "b",
                "text": "AAAA record mapping www.company.com to 203.0.113.55",
                "correct": False,
                "rationale": (
                    "Incorrect. An AAAA record maps a hostname to an IPv6 address. "
                    "203.0.113.55 is an IPv4 address; an A record is required."
                ),
            },
            {
                "id": "c",
                "text": "CNAME record mapping www.company.com to 203.0.113.55",
                "correct": False,
                "rationale": (
                    "Incorrect. A CNAME (Canonical Name) record creates an alias from one "
                    "hostname to another hostname, not to an IP address. CNAME targets must "
                    "be domain names, not raw IP addresses."
                ),
            },
            {
                "id": "d",
                "text": "MX record mapping www.company.com to 203.0.113.55",
                "correct": False,
                "rationale": (
                    "Incorrect. MX records designate mail exchangers for a domain, not web "
                    "server IP addresses. MX records also point to hostnames, not IPs directly."
                ),
            },
        ],
        "explanation": (
            "DNS record types: A = IPv4 address mapping; AAAA = IPv6 address mapping; "
            "CNAME = hostname alias to another hostname; MX = mail exchanger (hostname) "
            "for a domain; TXT = free-text records (SPF, DKIM, DMARC, domain verification); "
            "PTR = reverse lookup (IP to hostname)."
        ),
    },
    {
        "id": "a1d2-026",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "VLAN/VPN",
        "stem": (
            "A technician is configuring a managed switch to separate voice and data traffic "
            "for VoIP phones. Each desk has one Ethernet port that connects to both a phone "
            "and a PC. The phone should be on VLAN 20 (voice) and the PC on VLAN 10 (data). "
            "Which switch port configuration achieves this without adding additional cabling?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Configure the port as an access port on VLAN 10 with VLAN 20 as the voice VLAN",
                "correct": True,
                "rationale": (
                    "Correct. Cisco and most managed switch vendors support a 'voice VLAN' "
                    "feature on access ports. The port passes untagged data traffic on the "
                    "access VLAN (VLAN 10) while the phone negotiates a tagged voice VLAN "
                    "(VLAN 20) via CDP/LLDP-MED. The PC connected through the phone's "
                    "built-in switch receives untagged VLAN 10 traffic."
                ),
            },
            {
                "id": "b",
                "text": "Configure the port as a trunk port carrying both VLAN 10 and VLAN 20 with 802.1Q tagging for all frames",
                "correct": False,
                "rationale": (
                    "Incorrect. A fully trunked port would require the PC to understand and "
                    "process 802.1Q tags, which standard PCs do not do. The voice VLAN "
                    "feature correctly handles tagging at the phone while leaving PC traffic "
                    "untagged."
                ),
            },
            {
                "id": "c",
                "text": "Configure separate access ports for the phone and PC using a patch panel to split the single cable",
                "correct": False,
                "rationale": (
                    "Incorrect. A single Ethernet cable cannot be split into two full-duplex "
                    "connections using a patch panel. The voice VLAN feature is the designed "
                    "solution for this scenario."
                ),
            },
            {
                "id": "d",
                "text": "Place both the phone and PC on VLAN 20 and use QoS to prioritize voice packets",
                "correct": False,
                "rationale": (
                    "Incorrect. QoS can prioritize voice traffic, but placing both devices on "
                    "the same VLAN does not provide the required network segmentation and "
                    "eliminates the isolation benefit of a dedicated voice VLAN."
                ),
            },
        ],
        "explanation": (
            "The voice VLAN feature (supported on Cisco, HP, and most enterprise switches) "
            "allows a single port to carry both an untagged data VLAN (for the PC) and a "
            "tagged voice VLAN (for the IP phone). The phone learns the voice VLAN ID via "
            "CDP or LLDP-MED and tags its own traffic. The PC passes through the phone's "
            "built-in data port and sees only untagged data VLAN traffic."
        ),
    },
    # ── 2.6  Network Configuration Concepts ─────────────────────────────────
    {
        "id": "a1d2-027",
        "domain": 2,
        "objective": "2.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "VLAN/VPN",
        "stem": (
            "A remote employee needs secure access to corporate file shares over the internet. "
            "The IT policy requires all remote traffic to traverse the corporate firewall for "
            "inspection, even when the employee accesses public internet sites. Which VPN "
            "configuration meets this policy requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Full-tunnel VPN (full routing through the corporate gateway)",
                "correct": True,
                "rationale": (
                    "Correct. Full-tunnel VPN routes ALL remote client traffic through the "
                    "corporate VPN gateway, allowing the firewall to inspect both corporate "
                    "and internet-bound traffic. This fulfills the policy requirement."
                ),
            },
            {
                "id": "b",
                "text": "Split-tunnel VPN (only corporate traffic sent through the VPN)",
                "correct": False,
                "rationale": (
                    "Incorrect. Split tunneling sends only traffic destined for corporate "
                    "networks through the VPN; internet traffic goes directly from the client "
                    "without inspection by the corporate firewall, violating the policy."
                ),
            },
            {
                "id": "c",
                "text": "Site-to-site VPN between the employee's home router and the corporate firewall",
                "correct": False,
                "rationale": (
                    "Incorrect. A site-to-site VPN is designed to connect two fixed networks "
                    "(e.g., branch offices), not individual remote employees. It also does not "
                    "inherently route all internet traffic through the corporate firewall."
                ),
            },
            {
                "id": "d",
                "text": "SSL/TLS VPN portal providing browser-only access",
                "correct": False,
                "rationale": (
                    "Incorrect. An SSL VPN portal (clientless) limits access to browser-based "
                    "applications and does not route all network traffic through the corporate "
                    "firewall as a full-tunnel client VPN does."
                ),
            },
        ],
        "explanation": (
            "Full-tunnel (or 'full routing') VPN sends all client traffic through the corporate "
            "gateway — both corporate resource access and internet browsing. This allows the "
            "corporate firewall and security appliances to inspect all traffic. Split tunneling "
            "is more efficient (reduces VPN load) but bypasses corporate security controls for "
            "non-corporate traffic."
        ),
    },
    {
        "id": "a1d2-028",
        "domain": 2,
        "objective": "2.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "DNS records",
        "stem": (
            "A company uses an internal DNS server for name resolution of internal hostnames "
            "and an external DNS for publicly accessible records. A workstation can resolve "
            "public websites but not internal server names like 'fileserver.corp.local'. "
            "What is the MOST likely misconfiguration?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The workstation is configured to use the external public DNS server instead of the internal DNS server",
                "correct": True,
                "rationale": (
                    "Correct. Internal hostnames (like corp.local) exist only in the internal "
                    "DNS zone and are not published externally. If the workstation queries "
                    "an external DNS (e.g., 8.8.8.8), it cannot resolve internal names."
                ),
            },
            {
                "id": "b",
                "text": "The internal DNS server is missing a forwarder to the external DNS",
                "correct": False,
                "rationale": (
                    "Incorrect. A missing forwarder would cause external resolution to fail, "
                    "not internal. The workstation can already resolve public websites, so "
                    "external DNS is working. The problem is internal DNS resolution."
                ),
            },
            {
                "id": "c",
                "text": "The DHCP server is not providing an IP address to the workstation",
                "correct": False,
                "rationale": (
                    "Incorrect. The workstation can resolve public names and presumably access "
                    "the internet, so it has a valid IP address. DHCP is not the issue."
                ),
            },
            {
                "id": "d",
                "text": "The internal fileserver is not broadcasting its name via LLMNR",
                "correct": False,
                "rationale": (
                    "Incorrect. While LLMNR can resolve local names, the primary resolution "
                    "mechanism for corp.local names should be internal DNS, not LLMNR. The "
                    "root cause is the workstation pointing at an external DNS server."
                ),
            },
        ],
        "explanation": (
            "Split DNS (internal vs. external DNS) is common in corporate environments. "
            "Internal DNS zones (like .corp.local or .internal) are not published to public "
            "DNS. Workstations must be configured (typically via DHCP option 006) to use the "
            "internal DNS server as their primary resolver, with the internal server forwarding "
            "unresolved queries to external DNS for public names."
        ),
    },
    # ── 2.7  Internet Connection Types & Network Types ───────────────────────
    {
        "id": "a1d2-029",
        "domain": 2,
        "objective": "2.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Internet connection types",
        "stem": (
            "A rural business location has no cable, fiber, or DSL infrastructure available. "
            "The business requires a broadband connection with download speeds above 25 Mbps "
            "and is willing to accept higher latency. Which internet connection technology is "
            "MOST appropriate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Geostationary satellite (e.g., traditional satellite broadband)",
                "correct": True,
                "rationale": (
                    "Correct. Satellite internet is available anywhere with a clear view of the "
                    "sky, making it viable for rural areas with no terrestrial infrastructure. "
                    "Geostationary satellite provides broadband speeds but with high latency "
                    "(500-600 ms RTT) due to the ~35,786 km orbital altitude."
                ),
            },
            {
                "id": "b",
                "text": "DOCSIS cable modem",
                "correct": False,
                "rationale": (
                    "Incorrect. DOCSIS cable internet requires coaxial cable infrastructure "
                    "from a cable provider. If cable infrastructure is unavailable, a cable "
                    "modem cannot be used regardless of DOCSIS version."
                ),
            },
            {
                "id": "c",
                "text": "ADSL over copper telephone lines",
                "correct": False,
                "rationale": (
                    "Incorrect. ADSL requires existing copper telephone line infrastructure "
                    "(PSTN/POTS). If DSL is listed as unavailable in the scenario, this "
                    "option is not viable."
                ),
            },
            {
                "id": "d",
                "text": "ONT fiber connection",
                "correct": False,
                "rationale": (
                    "Incorrect. An ONT (Optical Network Terminal) connects fiber-to-the-premises "
                    "(FTTP/FTTH). Fiber infrastructure is explicitly unavailable in the scenario."
                ),
            },
        ],
        "explanation": (
            "Satellite internet is the traditional solution for locations without any "
            "terrestrial broadband infrastructure. Geostationary satellite services offer "
            "broadband speeds (typically 25-100+ Mbps down) but with latency of 500-600 ms "
            "due to the distance to orbit. Low-Earth orbit (LEO) satellite services (e.g., "
            "Starlink) provide lower latency (20-50 ms) and are increasingly common alternatives."
        ),
    },
    {
        "id": "a1d2-030",
        "domain": 2,
        "objective": "2.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Internet connection types",
        "stem": (
            "A fiber ISP provides a connection that converts optical signals to electrical "
            "Ethernet signals at the customer premises, allowing a standard router to connect "
            "to the fiber network. Which device performs this conversion?"
        ),
        "options": [
            {
                "id": "a",
                "text": "ONT (Optical Network Terminal)",
                "correct": True,
                "rationale": (
                    "Correct. An ONT (also called an ONU — Optical Network Unit) is the "
                    "subscriber-side device in a fiber-to-the-premises (FTTP/FTTH) network "
                    "that converts optical signals from the ISP's fiber to electrical Ethernet "
                    "for connection to a router or switch."
                ),
            },
            {
                "id": "b",
                "text": "Cable modem",
                "correct": False,
                "rationale": (
                    "Incorrect. A cable modem converts DOCSIS signals from coaxial cable to "
                    "Ethernet. It is used with cable TV infrastructure, not fiber optic ISP "
                    "connections."
                ),
            },
            {
                "id": "c",
                "text": "DSL modem",
                "correct": False,
                "rationale": (
                    "Incorrect. A DSL modem converts DSL signals over copper telephone lines "
                    "to Ethernet. DSL uses copper, not fiber optic cabling."
                ),
            },
            {
                "id": "d",
                "text": "Media converter",
                "correct": False,
                "rationale": (
                    "Incorrect. While a media converter can convert between fiber and copper "
                    "signals, it is a generic LAN device, not the ISP-specific subscriber "
                    "device used in FTTP/FTTH networks. The ISP-specific term is ONT."
                ),
            },
        ],
        "explanation": (
            "In fiber-to-the-home (FTTH) or fiber-to-the-premises (FTTP) deployments using "
            "GPON or XGS-PON technology, the ONT (Optical Network Terminal) is the demarcation "
            "device at the customer location. It terminates the optical fiber from the ISP's "
            "distribution network and provides one or more RJ-45 Ethernet ports for the "
            "customer's router."
        ),
    },
    {
        "id": "a1d2-031",
        "domain": 2,
        "objective": "2.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network types (LAN/WAN/PAN)",
        "stem": (
            "A hospital connects its imaging equipment, storage arrays, and backup systems "
            "using a dedicated high-speed network that is separate from the general patient "
            "and administrative network. This dedicated network is optimized for block-level "
            "data storage access using Fibre Channel or iSCSI. What type of network is this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "SAN (Storage Area Network)",
                "correct": True,
                "rationale": (
                    "Correct. A SAN is a specialized high-speed network that provides block-level "
                    "storage access using Fibre Channel or iSCSI, typically connecting servers "
                    "to shared storage arrays. It is isolated from general-purpose LAN traffic."
                ),
            },
            {
                "id": "b",
                "text": "WLAN (Wireless Local Area Network)",
                "correct": False,
                "rationale": (
                    "Incorrect. A WLAN uses wireless 802.11 technology for client connectivity. "
                    "It is not used for high-speed block-level storage access."
                ),
            },
            {
                "id": "c",
                "text": "MAN (Metropolitan Area Network)",
                "correct": False,
                "rationale": (
                    "Incorrect. A MAN connects networks across a city or metropolitan area. "
                    "It is a geographic scope designation, not a storage-specific network type."
                ),
            },
            {
                "id": "d",
                "text": "PAN (Personal Area Network)",
                "correct": False,
                "rationale": (
                    "Incorrect. A PAN is a very short-range network (typically Bluetooth or USB) "
                    "for personal devices like headsets and keyboards. It has no relevance to "
                    "storage networking."
                ),
            },
        ],
        "explanation": (
            "Network type scope summary: PAN (Personal Area Network) — Bluetooth/USB, < 10 m; "
            "LAN (Local Area Network) — single building/floor; WLAN — wireless LAN; "
            "MAN (Metropolitan Area Network) — city/campus; WAN (Wide Area Network) — "
            "geographically dispersed; SAN (Storage Area Network) — block-level storage "
            "using Fibre Channel or iSCSI, isolated from general-purpose traffic."
        ),
    },
    # ── 2.8  Cabling & Connectors ────────────────────────────────────────────
    {
        "id": "a1d2-032",
        "domain": 2,
        "objective": "2.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Copper & fiber cabling",
        "stem": (
            "A technician is running Ethernet cable through an air-handling space above the "
            "ceiling tiles (plenum space). Building codes require cable in this location to "
            "have specific fire-resistance properties. Which cable type must be used?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Plenum-rated (CMP) cable with low-smoke, low-toxicity insulation",
                "correct": True,
                "rationale": (
                    "Correct. Plenum-rated cable (CMP — Communications Multipurpose Plenum) "
                    "uses a special low-smoke, low-toxicity jacket required by NEC (National "
                    "Electrical Code) for installation in plenum air-handling spaces. Standard "
                    "PVC cable would release toxic fumes in a fire."
                ),
            },
            {
                "id": "b",
                "text": "Riser-rated (CMR) cable",
                "correct": False,
                "rationale": (
                    "Incorrect. Riser-rated (CMR) cable is approved for vertical runs between "
                    "floors (inside conduit or riser shafts) where the plenum standard is not "
                    "required. CMR is not sufficient for plenum air spaces."
                ),
            },
            {
                "id": "c",
                "text": "Direct burial (CMX) cable",
                "correct": False,
                "rationale": (
                    "Incorrect. Direct burial cable is designed for underground installation "
                    "with UV and moisture resistance. It is not rated for plenum air-handling "
                    "spaces."
                ),
            },
            {
                "id": "d",
                "text": "Standard Cat 6 UTP with PVC jacket",
                "correct": False,
                "rationale": (
                    "Incorrect. Standard PVC-jacketed cable releases toxic halogen gases when "
                    "burned and is prohibited by NEC in plenum spaces. Cat 6 can have a "
                    "plenum rating (CMP), but standard PVC Cat 6 cannot be used."
                ),
            },
        ],
        "explanation": (
            "NEC Article 800 requires plenum-rated (CMP) cable in air-handling plenum spaces "
            "because HVAC systems circulate air through these spaces — toxic cable fumes would "
            "spread throughout the building in a fire. Plenum cable uses FEP or low-smoke PVC "
            "jacket materials. The hierarchy is CMP (plenum) > CMR (riser) > CMG/CM (general) "
            "> CMX (residential/outdoor)."
        ),
    },
    {
        "id": "a1d2-033",
        "domain": 2,
        "objective": "2.8",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "T568A/B wiring",
        "stem": (
            "A technician crimps an RJ-45 connector onto a patch cable using T568B wiring on "
            "one end. To create a crossover cable for direct PC-to-PC connection on older "
            "equipment that does not support Auto-MDI/MDIX, what wiring standard must be used "
            "on the opposite end, and which pairs are crossed?"
        ),
        "options": [
            {
                "id": "a",
                "text": "T568A on the opposite end; pairs 2 (orange) and 3 (green) are crossed, swapping TX and RX",
                "correct": True,
                "rationale": (
                    "Correct. A crossover cable uses T568B on one end and T568A on the other. "
                    "This swaps pins 1/2 (TX) with pins 3/6 (RX), crossing the transmit pair "
                    "of one device to the receive pair of the other. T568A uses green on 1/2 "
                    "and orange on 3/6; T568B uses orange on 1/2 and green on 3/6."
                ),
            },
            {
                "id": "b",
                "text": "T568B on the opposite end; only the shield wires are crossed",
                "correct": False,
                "rationale": (
                    "Incorrect. A T568B-to-T568B cable is a straight-through patch cable. "
                    "Crossing only shield wires has no functional meaning in Ethernet; "
                    "the TX/RX data pairs must be crossed."
                ),
            },
            {
                "id": "c",
                "text": "T568A on both ends; pins 4/5 and 7/8 are crossed",
                "correct": False,
                "rationale": (
                    "Incorrect. T568A on both ends is a valid straight-through cable configuration "
                    "in some environments, not a crossover. Pins 4/5 and 7/8 carry the unused "
                    "pairs in 100BASE-TX and are not crossed in a standard Ethernet crossover."
                ),
            },
            {
                "id": "d",
                "text": "T568B on both ends with a gender changer adapter to reverse the connection",
                "correct": False,
                "rationale": (
                    "Incorrect. A gender changer does not cross TX and RX pairs. Only proper "
                    "T568A/T568B wiring can create the pin-level TX/RX crossover required."
                ),
            },
        ],
        "explanation": (
            "A crossover cable has T568A on one end and T568B on the other. The difference "
            "between the two standards is that orange and green pairs are swapped: "
            "T568B pin 1=W/O, 2=O, 3=W/G, 6=G; T568A pin 1=W/G, 2=G, 3=W/O, 6=O. "
            "This swaps the 10/100 Ethernet TX pair (1/2) with the RX pair (3/6). "
            "Modern switches and NICs with Auto-MDI/MDIX negotiate the crossing automatically, "
            "making crossover cables largely obsolete."
        ),
    },
    {
        "id": "a1d2-034",
        "domain": 2,
        "objective": "2.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Copper & fiber cabling",
        "stem": (
            "An engineer is designing a 10GBase-T infrastructure for a new data center floor. "
            "The maximum cable runs will be 90 meters. Which minimum cable category is required "
            "to support 10 Gbps over this distance?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Cat 6a (augmented Category 6)",
                "correct": True,
                "rationale": (
                    "Correct. Cat 6a is rated for 10GBase-T up to 100 meters. Cat 6 supports "
                    "10 Gbps but only to 55 meters (in low-crosstalk environments). For 90-meter "
                    "runs at 10 Gbps, Cat 6a (or better) is required."
                ),
            },
            {
                "id": "b",
                "text": "Cat 6 (standard Category 6)",
                "correct": False,
                "rationale": (
                    "Incorrect. Cat 6 supports 10GBase-T only up to approximately 55 meters "
                    "due to alien crosstalk limitations. A 90-meter run requires Cat 6a or "
                    "better."
                ),
            },
            {
                "id": "c",
                "text": "Cat 5e (enhanced Category 5)",
                "correct": False,
                "rationale": (
                    "Incorrect. Cat 5e is rated for 1000BASE-T (1 Gbps) at 100 meters. "
                    "It cannot reliably support 10GBase-T at any practical distance."
                ),
            },
            {
                "id": "d",
                "text": "Cat 7 is the only category that supports 10 Gbps",
                "correct": False,
                "rationale": (
                    "Incorrect. Cat 7 does support 10 Gbps (and beyond), but Cat 6a is the "
                    "minimum required standard and is far more commonly deployed. Cat 7 uses "
                    "non-standard GG45 or TERA connectors in its fully shielded form."
                ),
            },
        ],
        "explanation": (
            "10GBase-T Ethernet over copper requires: Cat 6a (or Cat 7) for runs up to 100 m. "
            "Cat 6 can handle 10 Gbps only to ~55 m due to alien crosstalk (ANEXT). "
            "Cat 5e supports 1 Gbps (1000BASE-T) at 100 m. For a data center with 90-meter "
            "runs, Cat 6a is the correct minimum specification."
        ),
    },
    {
        "id": "a1d2-035",
        "domain": 2,
        "objective": "2.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Copper & fiber cabling",
        "stem": (
            "A field technician needs to connect two buildings 800 meters apart with a "
            "network link. Copper Ethernet is insufficient at this distance. The technician "
            "chooses a single-mode fiber solution. Which fiber connector type is MOST commonly "
            "used in enterprise single-mode fiber patch panels and transceivers due to its "
            "small form factor and push-pull latch mechanism?"
        ),
        "options": [
            {
                "id": "a",
                "text": "LC (Lucent Connector)",
                "correct": True,
                "rationale": (
                    "Correct. LC connectors use a push-pull latch (RJ-45 style latch) and have "
                    "a 1.25 mm ferrule, half the diameter of SC. LC is the dominant enterprise "
                    "connector for SFP and SFP+ transceivers and high-density patch panels."
                ),
            },
            {
                "id": "b",
                "text": "SC (Subscriber Connector)",
                "correct": False,
                "rationale": (
                    "Incorrect. SC connectors use a push-pull coupling with a 2.5 mm ferrule "
                    "and are common in telecommunications and older installations, but LC has "
                    "displaced SC in modern enterprise data center and SFP transceiver applications "
                    "due to its smaller size."
                ),
            },
            {
                "id": "c",
                "text": "ST (Straight Tip)",
                "correct": False,
                "rationale": (
                    "Incorrect. ST connectors use a bayonet-style twist-and-lock mechanism and "
                    "a 2.5 mm ferrule. They are found in older multimode installations and are "
                    "rarely used in modern enterprise single-mode deployments."
                ),
            },
            {
                "id": "d",
                "text": "FC (Ferrule Connector)",
                "correct": False,
                "rationale": (
                    "Incorrect. FC connectors use a threaded screw-lock mechanism and are "
                    "primarily used in high-vibration environments and test equipment — not "
                    "in typical enterprise patch panels or SFP transceivers."
                ),
            },
        ],
        "explanation": (
            "Fiber connector quick reference: LC — small form factor (1.25 mm ferrule), "
            "push-pull latch, standard in SFP/SFP+ transceivers; SC — square body, push-pull, "
            "2.5 mm ferrule, common in telecom; ST — round, bayonet lock, 2.5 mm ferrule, "
            "legacy multimode; FC — threaded, 2.5 mm ferrule, test equipment/vibration "
            "environments. Single-mode fiber supports runs up to ~10 km or more depending "
            "on transceiver type."
        ),
    },
    # ── Multiple Response Questions ──────────────────────────────────────────
    {
        "id": "a1d2-036",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Ports & protocols",
        "stem": (
            "A security administrator is reviewing firewall rules to ensure only necessary "
            "ports are open. Which TWO ports and protocols listed below use UDP as their "
            "primary transport? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "DHCP (ports 67/68)",
                "correct": True,
                "rationale": (
                    "Correct. DHCP uses UDP on ports 67 (server) and 68 (client) because it "
                    "operates via broadcast before a client has an IP address, requiring the "
                    "connectionless, broadcast-capable nature of UDP."
                ),
            },
            {
                "id": "b",
                "text": "SNMP (ports 161/162)",
                "correct": True,
                "rationale": (
                    "Correct. SNMP uses UDP 161 for manager-to-agent polling queries and "
                    "UDP 162 for agent-to-manager trap notifications. UDP is used for its "
                    "low overhead in network management polling."
                ),
            },
            {
                "id": "c",
                "text": "SMTP (port 25)",
                "correct": False,
                "rationale": (
                    "Incorrect. SMTP uses TCP 25 for reliable, connection-oriented delivery "
                    "of email between mail servers. Email delivery requires acknowledgment "
                    "of successful receipt, necessitating TCP."
                ),
            },
            {
                "id": "d",
                "text": "RDP (port 3389)",
                "correct": False,
                "rationale": (
                    "Incorrect. RDP (Remote Desktop Protocol) primarily uses TCP 3389 for "
                    "reliable remote desktop session data. While RDP has a UDP mode in some "
                    "implementations for media streaming, its primary transport is TCP."
                ),
            },
        ],
        "explanation": (
            "UDP vs. TCP by protocol: DHCP = UDP 67/68; DNS = primarily UDP 53; "
            "SNMP = UDP 161/162; TFTP = UDP 69; syslog = UDP 514. "
            "Connection-oriented protocols using TCP: FTP (20/21), SSH (22), Telnet (23), "
            "SMTP (25), HTTP (80), POP3 (110), IMAP (143), HTTPS (443), RDP (3389), "
            "SMB (445), LDAP (389)."
        ),
    },
    {
        "id": "a1d2-037",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "IPv4 addressing & APIPA",
        "stem": (
            "A network technician is configuring IP addressing for a new office. The private "
            "IPv4 address ranges defined in RFC 1918 must be used for internal hosts. "
            "Which TWO of the following IP addresses are valid RFC 1918 private addresses? "
            "(Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "10.200.15.100",
                "correct": True,
                "rationale": (
                    "Correct. 10.0.0.0/8 (10.0.0.0 – 10.255.255.255) is one of the three "
                    "RFC 1918 private address ranges. 10.200.15.100 falls within this range."
                ),
            },
            {
                "id": "b",
                "text": "172.20.5.45",
                "correct": True,
                "rationale": (
                    "Correct. 172.16.0.0/12 (172.16.0.0 – 172.31.255.255) is the second "
                    "RFC 1918 private range. 172.20.5.45 falls within 172.16–172.31."
                ),
            },
            {
                "id": "c",
                "text": "169.254.50.10",
                "correct": False,
                "rationale": (
                    "Incorrect. 169.254.0.0/16 is the APIPA link-local range (RFC 3927), not "
                    "an RFC 1918 private address. APIPA is self-assigned when DHCP fails and "
                    "is not routable."
                ),
            },
            {
                "id": "d",
                "text": "198.51.100.22",
                "correct": False,
                "rationale": (
                    "Incorrect. 198.51.100.0/24 is an IANA-reserved documentation range "
                    "(RFC 5737), not an RFC 1918 private address. It is used in examples "
                    "and documentation, similar to 192.0.2.0/24 and 203.0.113.0/24."
                ),
            },
        ],
        "explanation": (
            "RFC 1918 private address ranges: 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16. "
            "These are non-routable on the public internet and are used for internal networks "
            "behind NAT. 169.254.0.0/16 is APIPA (RFC 3927). Documentation/test ranges "
            "(192.0.2.0/24, 198.51.100.0/24, 203.0.113.0/24) are defined by RFC 5737."
        ),
    },
    {
        "id": "a1d2-038",
        "domain": 2,
        "objective": "2.8",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Copper & fiber cabling",
        "stem": (
            "A technician is installing network cabling in a new building and must select "
            "the correct cable type for each scenario. Which TWO cabling characteristics "
            "describe STP (Shielded Twisted Pair) compared to UTP (Unshielded Twisted Pair)? "
            "(Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "STP includes metallic foil or braided shielding around the pairs or cable core to reduce EMI",
                "correct": True,
                "rationale": (
                    "Correct. STP cables use foil shielding (F/UTP), braided shielding (S/FTP), "
                    "or individual pair shielding (U/FTP) to reduce electromagnetic interference "
                    "from external sources such as motors, fluorescent lights, and radio equipment."
                ),
            },
            {
                "id": "b",
                "text": "STP requires proper grounding at both ends to be effective; improper grounding can increase noise",
                "correct": True,
                "rationale": (
                    "Correct. STP shields must be grounded at both ends to drain induced EMI "
                    "to ground. An ungrounded or improperly grounded shield can act as an antenna "
                    "and actually increase interference — a common installation mistake."
                ),
            },
            {
                "id": "c",
                "text": "STP is less expensive and easier to install than UTP",
                "correct": False,
                "rationale": (
                    "Incorrect. STP is more expensive than UTP due to additional shielding "
                    "materials and is more difficult to install because it requires grounded "
                    "connectors and careful handling to maintain shield continuity."
                ),
            },
            {
                "id": "d",
                "text": "STP supports longer maximum cable runs than UTP at the same data rate",
                "correct": False,
                "rationale": (
                    "Incorrect. STP and UTP have the same maximum segment length specifications "
                    "(e.g., 100 m for 1000BASE-T). The shielding reduces EMI susceptibility "
                    "but does not extend the maximum cable run distance."
                ),
            },
        ],
        "explanation": (
            "STP vs. UTP: STP adds metallic shielding (foil, braid, or combination) to "
            "reduce external EMI and crosstalk. STP is required in high-EMI environments "
            "(factories, hospitals with MRI). STP is more expensive, less flexible, requires "
            "grounded connectors, and must be properly grounded at both ends. UTP is cheaper, "
            "easier to install, and sufficient for most office environments."
        ),
    },
    {
        "id": "a1d2-039",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Wireless standards",
        "stem": (
            "A wireless network administrator is planning a Wi-Fi deployment and must "
            "understand the capabilities of 802.11ac (Wi-Fi 5). Which TWO statements "
            "accurately describe 802.11ac? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "802.11ac operates exclusively on the 5 GHz band",
                "correct": True,
                "rationale": (
                    "Correct. 802.11ac (Wi-Fi 5) is defined only for the 5 GHz band. Unlike "
                    "802.11n, which supports both 2.4 and 5 GHz, 802.11ac does not operate "
                    "on 2.4 GHz."
                ),
            },
            {
                "id": "b",
                "text": "802.11ac supports downlink MU-MIMO allowing simultaneous transmission to multiple clients",
                "correct": True,
                "rationale": (
                    "Correct. 802.11ac Wave 2 introduced downlink MU-MIMO (Multi-User, "
                    "Multiple Input, Multiple Output) supporting up to 4 simultaneous spatial "
                    "streams to different clients, improving efficiency in multi-client environments."
                ),
            },
            {
                "id": "c",
                "text": "802.11ac supports the 6 GHz band for additional spectrum",
                "correct": False,
                "rationale": (
                    "Incorrect. The 6 GHz band is supported by 802.11ax (Wi-Fi 6E), not "
                    "802.11ac. Wi-Fi 6E was the first standard to utilize the 6 GHz spectrum."
                ),
            },
            {
                "id": "d",
                "text": "802.11ac uses OFDMA to serve multiple clients within a single channel simultaneously",
                "correct": False,
                "rationale": (
                    "Incorrect. OFDMA (Orthogonal Frequency Division Multiple Access) was "
                    "introduced in 802.11ax (Wi-Fi 6). 802.11ac uses OFDM but not OFDMA."
                ),
            },
        ],
        "explanation": (
            "802.11ac (Wi-Fi 5): 5 GHz only, OFDM, channel widths up to 160 MHz, "
            "up to 8x8 MIMO (Wave 2 adds downlink MU-MIMO up to 4 streams), max theoretical "
            "throughput ~6.9 Gbps. 802.11ax (Wi-Fi 6) added OFDMA, uplink MU-MIMO, and "
            "6 GHz support (Wi-Fi 6E)."
        ),
    },
    {
        "id": "a1d2-040",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Networking hardware",
        "stem": (
            "A network administrator is evaluating whether to deploy managed or unmanaged "
            "switches in a new branch office. Which TWO features are available on managed "
            "switches but NOT on unmanaged switches? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "VLAN configuration to segment broadcast domains",
                "correct": True,
                "rationale": (
                    "Correct. VLAN support requires managed switch firmware that allows "
                    "administrators to assign ports to specific VLANs and configure 802.1Q "
                    "trunking. Unmanaged switches have no VLAN capability."
                ),
            },
            {
                "id": "b",
                "text": "Port mirroring (SPAN) for network traffic analysis",
                "correct": True,
                "rationale": (
                    "Correct. Port mirroring (Switch Port ANalyzer / SPAN) copies traffic "
                    "from one or more ports to a designated monitor port for analysis by a "
                    "packet capture tool. This requires management software and is only "
                    "available on managed switches."
                ),
            },
            {
                "id": "c",
                "text": "MAC address learning and forwarding table population",
                "correct": False,
                "rationale": (
                    "Incorrect. All switches — managed and unmanaged — automatically learn "
                    "MAC addresses and populate a forwarding table (CAM table). This is a "
                    "fundamental Layer 2 switching function, not an exclusive managed feature."
                ),
            },
            {
                "id": "d",
                "text": "Full-duplex operation on each port",
                "correct": False,
                "rationale": (
                    "Incorrect. Full-duplex operation is supported by both managed and "
                    "unmanaged switches. Auto-negotiation of speed and duplex is standard on "
                    "virtually all modern Ethernet switches regardless of manageability."
                ),
            },
        ],
        "explanation": (
            "Managed switches provide administrative control via CLI, web GUI, or SNMP, "
            "enabling features such as VLANs (802.1Q), STP/RSTP, port mirroring (SPAN), "
            "QoS/CoS, link aggregation (LACP), port security, SNMP monitoring, and "
            "firmware updates. Unmanaged switches perform basic Layer 2 forwarding (MAC "
            "learning, full-duplex, auto-negotiation) with no configuration capability."
        ),
    },
]

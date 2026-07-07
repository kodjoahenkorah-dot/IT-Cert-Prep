"""Domain 1 — Network Fundamentals v2 (Cisco CCNA 200-301).

40 brand-new scenario-based questions complementing domain1_network_fundamentals.py.
All questions are original; none paraphrase the existing bank.
study_topic labels match exactly those used in the v1 file.
"""

QUESTIONS = [
    # ------------------------------------------------------------------ 1.1 components
    {
        "id": "cd1v2-001",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network components",
        "stem": (
            "A network engineer must choose between deploying autonomous APs and lightweight APs "
            "for a 500-user corporate campus that requires seamless Layer 3 roaming and centralized "
            "RF spectrum management. Which statement BEST justifies the lightweight AP choice?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Lightweight APs offload control-plane functions to a WLC, enabling centralized "
                    "RF management, seamless client roaming, and policy enforcement without "
                    "per-AP configuration"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Lightweight (CAPWAP) APs delegate authentication, RF management, "
                    "roaming decisions, and policy to the WLC. This centralization is exactly what "
                    "enables coordinated RF and seamless Layer 3 roaming at scale."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Autonomous APs share client session state with each other directly, "
                    "providing centralized RF management without a controller"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Autonomous APs are self-contained and do not share session state "
                    "with each other. Each AP manages its own RF independently, making coordinated "
                    "RF management difficult without a controller."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Lightweight APs operate as independent devices and do not require any "
                    "management infrastructure"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Lightweight APs are dependent on a WLC for control-plane functions; "
                    "without the controller, they cannot pass traffic. Autonomous APs are the "
                    "independent option."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Autonomous APs use CAPWAP tunnels to a WLC, while lightweight APs do not "
                    "need tunneling"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This reverses the architecture. Lightweight APs use CAPWAP tunnels "
                    "to a WLC; autonomous APs require no controller and no CAPWAP."
                ),
            },
        ],
        "explanation": (
            "In the split-MAC/lightweight model, CAPWAP tunnels carry control and (optionally) "
            "data traffic to the WLC, which makes all RF and roaming decisions centrally. "
            "Autonomous APs are self-managing, making large-scale RF coordination and seamless "
            "roaming impractical."
        ),
    },
    {
        "id": "cd1v2-002",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network components",
        "stem": (
            "A service-provider data center uses a single high-end router with multiple "
            "virtual routing instances so that Customer A's 10.0.0.0/8 routes never interfere "
            "with Customer B's identical 10.0.0.0/8 routes on the same physical box. "
            "Which network component feature enables this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Virtual Routing and Forwarding (VRF)",
                "correct": True,
                "rationale": (
                    "Correct. VRF creates multiple, fully isolated routing and forwarding instances "
                    "on one physical router. Each customer gets its own routing table, allowing "
                    "overlapping address spaces without conflict."
                ),
            },
            {
                "id": "b",
                "text": "VLAN trunking (802.1Q)",
                "correct": False,
                "rationale": (
                    "Incorrect. 802.1Q VLANs segment Layer 2 broadcast domains but do not isolate "
                    "Layer 3 routing tables. Two customers with the same IP prefixes in different "
                    "VLANs would still conflict in the same routing table."
                ),
            },
            {
                "id": "c",
                "text": "EtherChannel (LACP)",
                "correct": False,
                "rationale": (
                    "Incorrect. EtherChannel bundles physical links for bandwidth and redundancy; "
                    "it has no role in routing-table isolation."
                ),
            },
            {
                "id": "d",
                "text": "Spanning Tree Protocol (STP)",
                "correct": False,
                "rationale": (
                    "Incorrect. STP prevents Layer 2 loops by blocking redundant switch ports; "
                    "it does not create separate routing tables."
                ),
            },
        ],
        "explanation": (
            "VRF partitions the router into logically independent routing/forwarding instances. "
            "Each VRF has its own RIB and FIB, so overlapping address spaces coexist without "
            "conflict — the foundational technology for MPLS VPN and multi-tenant services."
        ),
    },
    {
        "id": "cd1v2-003",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Network components",
        "stem": (
            "A security administrator wants to inspect and filter traffic at Layers 3 through 7, "
            "including application identification and intrusion prevention, between an internal LAN "
            "and the DMZ. Which network component is BEST suited for this role?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Next-generation firewall (NGFW)",
                "correct": True,
                "rationale": (
                    "Correct. An NGFW combines traditional stateful packet inspection with deep "
                    "packet inspection, application identification, URL filtering, and IPS — "
                    "exactly the multi-layer inspection needed between a LAN and DMZ."
                ),
            },
            {
                "id": "b",
                "text": "Layer 2 access switch",
                "correct": False,
                "rationale": (
                    "Incorrect. A Layer 2 switch forwards frames by MAC address and cannot "
                    "inspect application-layer content or provide IPS functionality."
                ),
            },
            {
                "id": "c",
                "text": "Wireless LAN controller",
                "correct": False,
                "rationale": (
                    "Incorrect. A WLC manages wireless APs and client associations; it is not a "
                    "traffic inspection or firewall device."
                ),
            },
            {
                "id": "d",
                "text": "Layer 3 switch",
                "correct": False,
                "rationale": (
                    "Incorrect. A Layer 3 switch routes between VLANs efficiently but applies "
                    "only basic ACL filtering, not application-layer inspection or IPS."
                ),
            },
        ],
        "explanation": (
            "NGFWs (e.g., Cisco Firepower) enforce policy at Layers 3-7: stateful firewall, "
            "application visibility, URL categories, IPS signatures. Traditional firewalls and "
            "L3 switches lack application-layer awareness and intrusion-prevention capabilities."
        ),
    },
    # ------------------------------------------------------------------ 1.2 topologies
    {
        "id": "cd1v2-004",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network topologies",
        "stem": (
            "A WAN designer connects three branch offices to a headquarters site where every "
            "branch-to-branch path must transit the HQ router. No direct branch-to-branch links "
            "exist. Which WAN topology does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Hub-and-spoke (star)",
                "correct": True,
                "rationale": (
                    "Correct. In a hub-and-spoke topology, all spokes (branches) connect only to "
                    "the hub (HQ). Branch-to-branch traffic must traverse the hub because there "
                    "are no direct spoke-to-spoke links."
                ),
            },
            {
                "id": "b",
                "text": "Full mesh",
                "correct": False,
                "rationale": (
                    "Incorrect. A full mesh provides a direct link between every pair of sites, "
                    "so branch-to-branch traffic would not need to transit HQ."
                ),
            },
            {
                "id": "c",
                "text": "Partial mesh",
                "correct": False,
                "rationale": (
                    "Incorrect. A partial mesh has some but not all direct site-to-site links. "
                    "The scenario has zero direct branch-to-branch links, which is the defining "
                    "characteristic of hub-and-spoke, not partial mesh."
                ),
            },
            {
                "id": "d",
                "text": "Spine-leaf",
                "correct": False,
                "rationale": (
                    "Incorrect. Spine-leaf is a data-center fabric topology — leaves connect only "
                    "to spines, not to WAN branches. The terminology and context differ entirely."
                ),
            },
        ],
        "explanation": (
            "Hub-and-spoke (star): one central hub with spokes radiating to it; all spoke-to-spoke "
            "traffic transits the hub. Simple and inexpensive but introduces hub as a single point "
            "of failure and can bottleneck hub-transited traffic. Contrast with full or partial "
            "mesh, which add direct spoke-to-spoke links."
        ),
    },
    {
        "id": "cd1v2-005",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network topologies",
        "stem": (
            "In a spine-leaf data-center fabric, a network architect wants to add capacity. "
            "Which action achieves this WITHOUT changing the existing leaf switches or the "
            "number of tiers?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Add a new spine switch and connect every existing leaf to it, distributing "
                    "east-west traffic across more uplinks via ECMP"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Adding a spine increases the number of uplinks each leaf has and "
                    "allows ECMP to spread traffic across more paths, increasing bandwidth without "
                    "adding tiers or modifying leaf switches' cabling to each other."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Connect leaf switches directly to each other to create shorter paths"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Leaf-to-leaf connections violate the spine-leaf design rule and "
                    "would create an irregular topology that complicates ECMP and predictable "
                    "latency — a key advantage of spine-leaf."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Add a third tier (aggregation layer) between the spines and leaves"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Introducing a third tier turns the design into a three-tier "
                    "hierarchy and defeats the two-tier uniform-latency benefit of spine-leaf."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Enable Spanning Tree on the spines to block redundant uplinks and "
                    "prevent loops"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Spine-leaf uses L3 ECMP precisely to avoid STP blocking; enabling "
                    "STP to block links would remove capacity instead of adding it."
                ),
            },
        ],
        "explanation": (
            "Spine-leaf scales horizontally: add spine switches and cable every leaf to each new "
            "spine, then ECMP spreads traffic evenly. This preserves two-tier design and "
            "predictable any-to-any latency while increasing east-west bandwidth."
        ),
    },
    # ------------------------------------------------------------------ 1.3 cabling
    {
        "id": "cd1v2-006",
        "domain": 1,
        "objective": "1.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Cabling & interfaces",
        "stem": (
            "A storage area network requires 10 Gbps links between servers and a top-of-rack "
            "switch that are all within the same rack (< 3 m apart). The solution must minimize "
            "cost while meeting reach and speed requirements. Which media type is BEST?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Direct-attach copper (DAC) Twinax cable with SFP+ transceivers",
                "correct": True,
                "rationale": (
                    "Correct. DAC Twinax with SFP+ is the most cost-effective 10 Gbps solution "
                    "for short intra-rack runs (typically up to ~7 m passive, longer active). "
                    "It avoids the expense of optical transceivers and fiber while meeting the "
                    "3 m requirement."
                ),
            },
            {
                "id": "b",
                "text": "Cat 5e UTP with RJ45 at 10 Gbps",
                "correct": False,
                "rationale": (
                    "Incorrect. Cat 5e is rated to 1 Gbps (100 m) or 10 Gbps only up to ~45 m "
                    "under ideal conditions, and real-world performance is unreliable for 10GBase-T "
                    "at 10 Gbps. Cat 6a is the copper standard for 10GBase-T."
                ),
            },
            {
                "id": "c",
                "text": "Single-mode fiber (SMF) with LC connectors",
                "correct": False,
                "rationale": (
                    "Incorrect. SMF is optimized for long-distance (km) runs and uses expensive "
                    "laser transceivers. Using SMF for a 3 m intra-rack link is technically "
                    "possible but unnecessarily expensive."
                ),
            },
            {
                "id": "d",
                "text": "Coaxial (thick Ethernet) cable",
                "correct": False,
                "rationale": (
                    "Incorrect. Thick Ethernet coax (10Base5) is an obsolete technology that "
                    "operates at only 10 Mbps and is not used in modern data center cabling."
                ),
            },
        ],
        "explanation": (
            "For 10 Gbps at very short distances inside a rack, DAC (passive or active Twinax) "
            "with SFP+ is the standard cost-effective choice. Fiber (MMF/SMF) is used for "
            "longer or inter-rack/row runs; Cat 6a copper for 10GBase-T is also an option "
            "but bulkier and generates more heat."
        ),
    },
    {
        "id": "cd1v2-007",
        "domain": 1,
        "objective": "1.3",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Cabling & interfaces",
        "stem": (
            "An engineer needs to connect a laptop to a Cisco router's console port for out-of-band "
            "management. The laptop has a USB-A port only. Which cable or adapter combination "
            "is required?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A USB-to-RJ45 console (rollover) cable, with the RJ45 end plugging into the router console port",
                "correct": True,
                "rationale": (
                    "Correct. Cisco console ports use RJ45. A USB-to-RJ45 console cable (rollover "
                    "pinout) connects the laptop's USB-A port to the router's RJ45 console port "
                    "and emulates a serial (COM) connection via a built-in USB serial chip."
                ),
            },
            {
                "id": "b",
                "text": "A straight-through Cat 6 Ethernet cable from the laptop NIC to the console port",
                "correct": False,
                "rationale": (
                    "Incorrect. The console port is not an Ethernet data port. Connecting via "
                    "the laptop's NIC to the console port would do nothing; a rollover cable "
                    "to a serial/console adapter is required."
                ),
            },
            {
                "id": "c",
                "text": "A crossover Ethernet cable to the router's Ethernet management port",
                "correct": False,
                "rationale": (
                    "Incorrect. This describes in-band management via the Ethernet management port, "
                    "not out-of-band console access. The question specifies using the console port."
                ),
            },
            {
                "id": "d",
                "text": "A fiber patch cable with an SFP adapter inserted into the console port",
                "correct": False,
                "rationale": (
                    "Incorrect. Console ports do not accept SFP transceivers or fiber. Console "
                    "access requires a serial/rollover connection to the RJ45 console port."
                ),
            },
        ],
        "explanation": (
            "Out-of-band console access to Cisco devices uses a rollover cable (all 8 wires "
            "reversed) terminated in RJ45 on the device side and DB9 or USB on the PC side. "
            "Modern cables integrate a USB-to-serial chip, providing a virtual COM port on "
            "the laptop."
        ),
    },
    # ------------------------------------------------------------------ 1.4 troubleshooting interfaces
    {
        "id": "cd1v2-008",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Interface/cable troubleshooting",
        "stem": (
            "A Cisco switch port shows the following counters in 'show interfaces Gi0/2': "
            "input errors: 4521, CRC: 4521, giants: 0, runts: 0, no buffer: 0. "
            "The interface is up/up and the cable was recently replaced. "
            "Which is the MOST likely root cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A damaged or low-quality Ethernet cable causing physical bit errors",
                "correct": True,
                "rationale": (
                    "Correct. CRC errors on an up/up interface, especially after a recent cable "
                    "replacement, strongly suggest a damaged, improperly terminated, or "
                    "sub-standard cable causing signal corruption. The receiver computes a "
                    "different CRC than the sender, indicating bit errors in transit."
                ),
            },
            {
                "id": "b",
                "text": "A duplex mismatch causing late collisions",
                "correct": False,
                "rationale": (
                    "Incorrect. A duplex mismatch produces 'late collisions' and 'output errors,' "
                    "not primarily CRC errors. The counters shown are all CRC (input errors), "
                    "pointing to a physical/signal problem, not a duplex negotiation failure."
                ),
            },
            {
                "id": "c",
                "text": "MTU mismatch between the switch and the connected device",
                "correct": False,
                "rationale": (
                    "Incorrect. MTU mismatches cause fragmentation or dropped oversized frames, "
                    "which would appear as 'giants' or discards rather than CRC errors indicating "
                    "corrupted bits."
                ),
            },
            {
                "id": "d",
                "text": "The switch port is administratively shut down",
                "correct": False,
                "rationale": (
                    "Incorrect. A shut-down port shows 'administratively down/down' with no "
                    "traffic counters incrementing. An up/up port with rising CRC errors is active "
                    "but experiencing physical signal corruption."
                ),
            },
        ],
        "explanation": (
            "CRC errors (input errors) on an up/up interface indicate physical layer corruption: "
            "damaged cable, bad connector, improper termination, or EMI. Duplex mismatch produces "
            "late collisions; giants/runts indicate oversized/undersized frames; no buffer means "
            "congestion. High CRC = fix the physical media first."
        ),
    },
    {
        "id": "cd1v2-009",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Interface/cable troubleshooting",
        "stem": (
            "An interface shows 'Serial0/0/0 is down, line protocol is down (disabled)'. "
            "Which is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The interface has been manually shut down with the 'shutdown' command",
                "correct": True,
                "rationale": (
                    "Correct. 'Down/down (disabled)' on a serial interface indicates it was "
                    "administratively shut down. IOS appends '(disabled)' to show it is not just "
                    "a physical failure but an administrative action."
                ),
            },
            {
                "id": "b",
                "text": "The remote end has no clock rate configured on a DCE interface",
                "correct": False,
                "rationale": (
                    "Incorrect. A missing clock rate causes 'down/down' (without 'disabled') on "
                    "the DTE side, because the physical layer cannot synchronize. The '(disabled)' "
                    "keyword specifically indicates admin shutdown."
                ),
            },
            {
                "id": "c",
                "text": "Keepalive messages have timed out on the link",
                "correct": False,
                "rationale": (
                    "Incorrect. Keepalive failures cause 'up/line protocol down' (Layer 1 is fine, "
                    "Layer 2 is not), not 'down/down (disabled)' which is an administrative state."
                ),
            },
            {
                "id": "d",
                "text": "The wrong encapsulation type is configured",
                "correct": False,
                "rationale": (
                    "Incorrect. Encapsulation mismatch causes 'up/line protocol down' (Layer 1 "
                    "up, Layer 2 can't establish). 'Down/down (disabled)' means admin shutdown."
                ),
            },
        ],
        "explanation": (
            "IOS interface states: 'administratively down/down' = 'shutdown' was issued; "
            "'down/down' = physical failure (no cable, no clock); 'up/down' = Layer 1 OK but "
            "Layer 2 failing (encap, keepalives); 'up/up' = fully operational. "
            "The '(disabled)' notation on some IOS versions specifically denotes admin shutdown."
        ),
    },
    # ------------------------------------------------------------------ 1.5 TCP/UDP
    {
        "id": "cd1v2-010",
        "domain": 1,
        "objective": "1.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "TCP vs UDP",
        "stem": (
            "A packet capture shows a TCP segment with the SYN and FIN flags both set to 1 "
            "simultaneously. What should a correctly implemented TCP stack do with this segment?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Discard it, because a valid TCP segment cannot have SYN and FIN set simultaneously",
                "correct": True,
                "rationale": (
                    "Correct. RFC 793 and subsequent TCP standards do not define a valid use for "
                    "SYN+FIN together. This is an illegal flag combination used in some OS "
                    "fingerprinting and firewall-evasion techniques. A correct TCP implementation "
                    "should discard such segments."
                ),
            },
            {
                "id": "b",
                "text": "Open and immediately close the connection in a single segment exchange",
                "correct": False,
                "rationale": (
                    "Incorrect. TCP connection setup (SYN, SYN-ACK, ACK) and teardown (FIN, "
                    "FIN-ACK, ACK) are separate sequences. A single SYN+FIN segment does not "
                    "accomplish both; it is an invalid combination that should be dropped."
                ),
            },
            {
                "id": "c",
                "text": "Treat it as a SYN only and initiate a new connection, ignoring FIN",
                "correct": False,
                "rationale": (
                    "Incorrect. A conforming stack should not arbitrarily ignore one of two "
                    "simultaneously set flags. The correct action is to discard the invalid segment."
                ),
            },
            {
                "id": "d",
                "text": "Respond with a RST segment to reset any existing connection",
                "correct": False,
                "rationale": (
                    "Incorrect. While some stacks may send RST, the primary mandated behavior for "
                    "an unrecognized/illegal flag combination in a new connection context is to "
                    "discard (not accept and reset), as accepting it could allow exploitation."
                ),
            },
        ],
        "explanation": (
            "SYN and FIN cannot logically coexist: SYN initiates a connection while FIN terminates "
            "one. This illegal combination is used in Xmas-style and OS-fingerprinting scans. "
            "RFC-compliant stacks silently drop the segment. Firewalls and IDS/IPS flag it "
            "as suspicious."
        ),
    },
    {
        "id": "cd1v2-011",
        "domain": 1,
        "objective": "1.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "TCP vs UDP",
        "stem": (
            "A client initiates a TCP connection to a server. The server's TCP receive window "
            "advertisement drops from 65535 to 1024 bytes over several exchanges. "
            "What does this indicate, and how does it affect the sender?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The server's receive buffer is filling up; the sender must limit "
                    "unacknowledged data in flight to 1024 bytes, slowing throughput"
                ),
                "correct": True,
                "rationale": (
                    "Correct. The TCP receive window represents how much data the receiver can "
                    "buffer. A shrinking window means the buffer is filling (slow application "
                    "consumption). The sender must not exceed the advertised window size, "
                    "reducing its send rate and thus throughput."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The server is increasing its processing speed; a smaller window "
                    "means faster ACKs"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A smaller receive window means less buffer space available, "
                    "indicating a slower consumer, not a faster one. It restricts the sender."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The sender's congestion window has been exceeded and TCP is in "
                    "slow-start mode"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The receive window is advertised by the receiver, not the sender. "
                    "The congestion window (cwnd) is a sender-side concept; both can constrain "
                    "throughput but this question describes the receiver's window shrinking."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The server is advertising that it can now accept only 1024 "
                    "simultaneous connections"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The window size is measured in bytes of buffer space for data, "
                    "not in the number of connections. Simultaneous connections are managed by "
                    "the listen backlog, a separate parameter."
                ),
            },
        ],
        "explanation": (
            "TCP flow control: the receiver advertises its available buffer space in the window "
            "field. The sender may not have more unacknowledged bytes outstanding than the "
            "advertised window. A window shrinking to 1024 bytes means the application is "
            "not draining the buffer quickly, so the sender's effective throughput is capped."
        ),
    },
    {
        "id": "cd1v2-012",
        "domain": 1,
        "objective": "1.5",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "TCP vs UDP",
        "stem": (
            "Which TWO application-layer protocols use UDP as their transport? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "DNS (port 53) for standard name resolution queries",
                "correct": True,
                "rationale": (
                    "Correct. DNS uses UDP/53 for typical query-response exchanges because the "
                    "small payload and low latency of UDP are preferred. TCP/53 is used only "
                    "for zone transfers or responses exceeding 512 bytes."
                ),
            },
            {
                "id": "b",
                "text": "SNMP (port 161) for agent polling",
                "correct": True,
                "rationale": (
                    "Correct. SNMP uses UDP/161 for manager-to-agent polling (Get/Set) and "
                    "UDP/162 for agent traps. The connectionless model suits the periodic, "
                    "fire-and-forget nature of SNMP operations."
                ),
            },
            {
                "id": "c",
                "text": "SMTP (port 25) for email relay",
                "correct": False,
                "rationale": (
                    "Incorrect. SMTP uses TCP/25 for reliable delivery of email messages between "
                    "mail servers; a TCP connection with acknowledgments is required."
                ),
            },
            {
                "id": "d",
                "text": "HTTPS (port 443) for encrypted web traffic",
                "correct": False,
                "rationale": (
                    "Incorrect. Traditional HTTPS uses TCP/443 with TLS. HTTP/3 uses QUIC "
                    "(UDP-based), but HTTPS on UDP/443 refers to QUIC, not the standard "
                    "TLS-over-TCP HTTPS."
                ),
            },
            {
                "id": "e",
                "text": "SSH (port 22) for remote management",
                "correct": False,
                "rationale": (
                    "Incorrect. SSH uses TCP/22 for reliable, ordered, encrypted sessions. "
                    "SSH requires TCP's connection-oriented properties."
                ),
            },
        ],
        "explanation": (
            "UDP-based protocols include DNS (53), DHCP (67/68), TFTP (69), NTP (123), "
            "SNMP (161/162), RIP (520), and real-time media (RTP). TCP-based protocols include "
            "HTTP(S), SSH, FTP, SMTP, Telnet, and BGP, among others."
        ),
    },
    # ------------------------------------------------------------------ 1.6 subnetting
    {
        "id": "cd1v2-013",
        "domain": 1,
        "objective": "1.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "IPv4 subnetting",
        "stem": (
            "A host has the IP address 192.168.50.130/27. "
            "What is the broadcast address of its subnet?"
        ),
        "options": [
            {
                "id": "a",
                "text": "192.168.50.159",
                "correct": True,
                "rationale": (
                    "Correct. /27 has a block size of 32 (256 - 224). Starting from 0, subnets: "
                    ".0, .32, .64, .96, .128, .160... Address .130 falls in the .128 subnet "
                    "(.128 to .159). Network: .128, broadcast: .159, usable: .129-.158."
                ),
            },
            {
                "id": "b",
                "text": "192.168.50.191",
                "correct": False,
                "rationale": (
                    "Incorrect. .191 is the broadcast of the next /27 subnet (.160-.191). "
                    "Address .130 belongs to the .128 subnet, whose broadcast is .159."
                ),
            },
            {
                "id": "c",
                "text": "192.168.50.255",
                "correct": False,
                "rationale": (
                    "Incorrect. .255 would be the broadcast of a /24 or the .224 /27 subnet. "
                    "For a /27 containing .130, the subnet is .128 with broadcast .159."
                ),
            },
            {
                "id": "d",
                "text": "192.168.50.135",
                "correct": False,
                "rationale": (
                    "Incorrect. .135 is a usable host address within the .128/27 subnet, "
                    "not the broadcast. The broadcast is always the last address: .159."
                ),
            },
        ],
        "explanation": (
            "/27 mask = 255.255.255.224, block size = 32. Subnets at .0, .32, .64, .96, .128, "
            ".160, .192, .224. Address .130 is in the .128 block: "
            "network .128, broadcast .159 (128 + 32 - 1), usable .129-.158."
        ),
    },
    {
        "id": "cd1v2-014",
        "domain": 1,
        "objective": "1.6",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "IPv4 subnetting",
        "stem": (
            "You are given 172.20.0.0/16 and must create subnets using VLSM in this order: "
            "Subnet A needs 2000 hosts, Subnet B needs 500 hosts, Subnet C needs 100 hosts. "
            "What prefix length should you assign to Subnet A to use the minimum number of "
            "host bits while satisfying the requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "/21 (2046 usable hosts)",
                "correct": True,
                "rationale": (
                    "Correct. 2000 hosts require 11 host bits (2^11 - 2 = 2046 >= 2000). "
                    "32 - 11 = /21. A /22 gives only 2^10 - 2 = 1022 usable hosts, "
                    "which is too few."
                ),
            },
            {
                "id": "b",
                "text": "/22 (1022 usable hosts)",
                "correct": False,
                "rationale": (
                    "Incorrect. /22 provides 2^10 - 2 = 1022 usable hosts, which does not "
                    "satisfy the 2000-host requirement."
                ),
            },
            {
                "id": "c",
                "text": "/20 (4094 usable hosts)",
                "correct": False,
                "rationale": (
                    "Incorrect. /20 gives 2^12 - 2 = 4094 usable hosts. While it fits 2000 "
                    "hosts, it uses 12 host bits when only 11 are needed — it does not use "
                    "the minimum host bits."
                ),
            },
            {
                "id": "d",
                "text": "/23 (510 usable hosts)",
                "correct": False,
                "rationale": (
                    "Incorrect. /23 provides only 2^9 - 2 = 510 usable hosts, far fewer "
                    "than the required 2000."
                ),
            },
        ],
        "explanation": (
            "VLSM best practice: allocate the largest subnets first. For 2000 hosts: "
            "2^10 - 2 = 1022 (too small), 2^11 - 2 = 2046 (fits). 32 - 11 = /21. "
            "Assign 172.20.0.0/21 to Subnet A (172.20.0.0 - 172.20.7.255), then carve "
            "subsequent subnets from the remaining space."
        ),
    },
    {
        "id": "cd1v2-015",
        "domain": 1,
        "objective": "1.6",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "IPv4 subnetting",
        "stem": (
            "A network administrator needs a summary route to advertise exactly the following "
            "subnets and no others: 10.4.0.0/24, 10.5.0.0/24, 10.6.0.0/24, 10.7.0.0/24. "
            "Which summary route should be advertised?"
        ),
        "options": [
            {
                "id": "a",
                "text": "10.4.0.0/22",
                "correct": True,
                "rationale": (
                    "Correct. The third-octet values are 4, 5, 6, 7 — a range of 4, which is "
                    "block size 4 in that octet. Block size 4 in the third octet = /22 "
                    "(255.255.252.0). 10.4.0.0/22 spans 10.4.0.0 - 10.7.255.255, covering "
                    "exactly those four /24s."
                ),
            },
            {
                "id": "b",
                "text": "10.4.0.0/23",
                "correct": False,
                "rationale": (
                    "Incorrect. /23 covers only two /24s: 10.4.0.0 and 10.5.0.0 "
                    "(10.4.0.0 - 10.5.255.255). It does not include 10.6.0.0 or 10.7.0.0."
                ),
            },
            {
                "id": "c",
                "text": "10.0.0.0/21",
                "correct": False,
                "rationale": (
                    "Incorrect. 10.0.0.0/21 covers 10.0.0.0 - 10.7.255.255, which includes "
                    "10.0.0.0/24 through 10.7.0.0/24 — eight /24s, not just the four specified."
                ),
            },
            {
                "id": "d",
                "text": "10.4.0.0/21",
                "correct": False,
                "rationale": (
                    "Incorrect. 10.4.0.0/21 covers 10.4.0.0 - 10.11.255.255 (block 8 in the "
                    "third octet), which includes eight /24s — overly broad, advertising more "
                    "than the specified four networks."
                ),
            },
        ],
        "explanation": (
            "Route summarization: find the common bits. Third-octet values 4 (00000100), "
            "5 (00000101), 6 (00000110), 7 (00000111) share 5 high bits. The summary prefix "
            "is /16 + 5 = not quite — more precisely, the block size is 4 in the third octet, "
            "which corresponds to borrowing 2 bits from the third octet: /16 + 6 = /22. "
            "10.4.0.0/22 covers exactly .4.x.x through .7.x.x."
        ),
    },
    {
        "id": "cd1v2-016",
        "domain": 1,
        "objective": "1.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "IPv4 subnetting",
        "stem": (
            "Host A: 10.20.30.40/20. Host B: 10.20.45.10/20. "
            "Are these hosts on the same subnet?"
        ),
        "options": [
            {
                "id": "a",
                "text": "No — Host A is in 10.20.32.0/20 and Host B is in 10.20.48.0/20, different subnets",
                "correct": True,
                "rationale": (
                    "Correct. /20 has block size 16 in the third octet (256 - 240 = 16). "
                    "Subnets: third-octet boundaries at 0, 16, 32, 48, 64... "
                    "Host A (.30) is in 10.20.32.0/20 (32-47); "
                    "Host B (.45) is in 10.20.48.0/20 (48-63). Different subnets."
                ),
            },
            {
                "id": "b",
                "text": "Yes — both addresses share the same first two octets (10.20), so they are on the same subnet",
                "correct": False,
                "rationale": (
                    "Incorrect. The /20 mask affects the third octet as well. Sharing the first "
                    "two octets alone does not mean the same /20 subnet; the block boundaries "
                    "within the third octet determine subnet membership."
                ),
            },
            {
                "id": "c",
                "text": "Yes — both are within 10.20.0.0/20",
                "correct": False,
                "rationale": (
                    "Incorrect. 10.20.0.0/20 covers only 10.20.0.0 - 10.20.15.255. Neither "
                    ".30 nor .45 in the third octet is in this range."
                ),
            },
            {
                "id": "d",
                "text": "No — they are in different /24 networks so they cannot be in the same /20",
                "correct": False,
                "rationale": (
                    "Incorrect. A /20 spans multiple /24s by definition, so being in different "
                    "/24s does not automatically mean different /20s. The answer is correct that "
                    "they are in different subnets, but the reasoning given here is flawed."
                ),
            },
        ],
        "explanation": (
            "/20 mask = 255.255.240.0, block size 16 in third octet. "
            "Boundaries: .0, .16, .32, .48, .64... "
            "10.20.30.x falls in .32 block (10.20.32.0 - 10.20.47.255). "
            "10.20.45.x falls in .48 block (10.20.48.0 - 10.20.63.255). "
            "Different subnets — they need a router to communicate."
        ),
    },
    {
        "id": "cd1v2-017",
        "domain": 1,
        "objective": "1.6",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "IPv4 subnetting",
        "stem": (
            "Using the address space 192.168.10.0/24, a network engineer must create at least "
            "14 subnets each supporting at least 10 hosts. Which subnet mask satisfies BOTH "
            "constraints simultaneously using the same prefix throughout?"
        ),
        "options": [
            {
                "id": "a",
                "text": "/28 (255.255.255.240) — 16 subnets, 14 usable hosts each",
                "correct": True,
                "rationale": (
                    "Correct. Borrowing 4 bits from a /24 yields 2^4 = 16 subnets (>= 14). "
                    "4 remaining host bits give 2^4 - 2 = 14 usable hosts per subnet (>= 10). "
                    "Both constraints are satisfied simultaneously."
                ),
            },
            {
                "id": "b",
                "text": "/27 (255.255.255.224) — 8 subnets, 30 usable hosts each",
                "correct": False,
                "rationale": (
                    "Incorrect. Borrowing 3 bits from a /24 gives only 8 subnets, which does "
                    "not meet the 'at least 14 subnets' requirement."
                ),
            },
            {
                "id": "c",
                "text": "/29 (255.255.255.248) — 32 subnets, 6 usable hosts each",
                "correct": False,
                "rationale": (
                    "Incorrect. /29 gives 32 subnets (meets >= 14) but only 2^3 - 2 = 6 usable "
                    "hosts per subnet (does not meet >= 10). Both constraints must be met."
                ),
            },
            {
                "id": "d",
                "text": "/26 (255.255.255.192) — 4 subnets, 62 usable hosts each",
                "correct": False,
                "rationale": (
                    "Incorrect. /26 gives only 4 subnets from a /24, far fewer than the "
                    "required 14, even though host capacity (62) is ample."
                ),
            },
        ],
        "explanation": (
            "For a /24, borrowing n subnet bits gives 2^n subnets and (8-n) host bits. "
            "Need: 2^n >= 14 AND 2^(8-n) - 2 >= 10. "
            "n=4: 2^4=16 subnets OK; 2^4-2=14 hosts OK. Both met. "
            "n=3: 8 subnets too few. n=5: 32 subnets OK but only 6 hosts per subnet — fails."
        ),
    },
    # ------------------------------------------------------------------ 1.7 private/NAT
    {
        "id": "cd1v2-018",
        "domain": 1,
        "objective": "1.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Private addressing & NAT",
        "stem": (
            "A Cisco router is configured for PAT (overload NAT) with a single public IP. "
            "100 internal hosts are accessing the internet simultaneously. "
            "Which mechanism allows all 100 hosts to share the one public IP address?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "PAT uses unique source port numbers to distinguish each host's sessions, "
                    "mapping each internal private-IP:port pair to the public-IP:unique-port"
                ),
                "correct": True,
                "rationale": (
                    "Correct. PAT (Port Address Translation / NAT overload) extends NAT by "
                    "adding source port tracking. Each internal host's session gets a unique "
                    "public-side port number, allowing thousands of sessions to share one "
                    "public IP address."
                ),
            },
            {
                "id": "b",
                "text": (
                    "PAT assigns each host a different public IP from a pool of 100 addresses"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. That describes standard dynamic NAT with an address pool, "
                    "not PAT. PAT specifically enables many-to-one mapping using a single "
                    "public IP differentiated by port numbers."
                ),
            },
            {
                "id": "c",
                "text": (
                    "PAT fragments each host's packets so they interleave transparently "
                    "on the public IP"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. PAT does not use fragmentation. It uses Layer 4 port-number "
                    "multiplexing to distinguish sessions, leaving IP packets intact (not "
                    "fragmented)."
                ),
            },
            {
                "id": "d",
                "text": (
                    "PAT uses VLAN tags to separate each host's traffic on the public side"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. VLAN tags are Layer 2 LAN constructs. PAT operates at Layer 3/4 "
                    "and uses port numbers, not VLAN tags, to multiplex sessions."
                ),
            },
        ],
        "explanation": (
            "PAT (overload NAT): the router translates each inside host's source "
            "private-IP:source-port to a common public-IP:unique-source-port. Return traffic "
            "carries the same public-port, allowing the router to reverse-map it to the "
            "correct internal host. Up to ~65535 concurrent sessions per public IP are possible."
        ),
    },
    {
        "id": "cd1v2-019",
        "domain": 1,
        "objective": "1.7",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Private addressing & NAT",
        "stem": (
            "Which TWO statements correctly describe limitations or characteristics of NAT? "
            "(Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "NAT breaks end-to-end IP connectivity, complicating protocols that embed "
                    "IP addresses in the payload (e.g., FTP active mode, SIP)"
                ),
                "correct": True,
                "rationale": (
                    "Correct. NAT modifies IP headers but not always application-layer payloads. "
                    "Protocols like FTP (active mode) and SIP embed IP addresses in the data, "
                    "which NAT may not update, breaking the session unless ALGs handle it."
                ),
            },
            {
                "id": "b",
                "text": (
                    "NAT can make it difficult to trace a specific session back to an internal "
                    "host because many hosts share a public IP"
                ),
                "correct": True,
                "rationale": (
                    "Correct. With PAT, multiple internal hosts share a single public IP, "
                    "making attribution of external-facing traffic to a specific internal host "
                    "difficult without NAT translation table logs."
                ),
            },
            {
                "id": "c",
                "text": "NAT provides cryptographic encryption of all translated sessions",
                "correct": False,
                "rationale": (
                    "Incorrect. NAT translates addresses; it provides no encryption. Encryption "
                    "is a function of IPsec, TLS, or other security protocols."
                ),
            },
            {
                "id": "d",
                "text": "NAT allows all RFC 1918 addresses to be routed natively on the public internet",
                "correct": False,
                "rationale": (
                    "Incorrect. NAT translates private addresses to public ones precisely because "
                    "RFC 1918 addresses cannot be routed on the internet — NAT solves this, "
                    "it does not make private addresses routable."
                ),
            },
            {
                "id": "e",
                "text": "NAT inherently prevents all inbound attacks from the internet",
                "correct": False,
                "rationale": (
                    "Incorrect. NAT's stateful table blocks unsolicited inbound sessions as a "
                    "side effect, but it is not a security feature and should not be relied upon "
                    "as a firewall. It does not inspect or block malicious traffic in responses."
                ),
            },
        ],
        "explanation": (
            "NAT breaks end-to-end IP transparency (problematic for embedded-IP protocols), "
            "complicates logging/attribution, and is not a security mechanism. "
            "It does not encrypt, and RFC 1918 addresses remain non-routable without "
            "translation. NAT was a workaround for IPv4 address exhaustion, not a "
            "security solution."
        ),
    },
    # ------------------------------------------------------------------ 1.8/1.9 IPv6
    {
        "id": "cd1v2-020",
        "domain": 1,
        "objective": "1.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "IPv6 addressing",
        "stem": (
            "Which of the following is the correct compressed form of the IPv6 address "
            "2001:0DB8:0000:0001:0000:0000:0000:0001?"
        ),
        "options": [
            {
                "id": "a",
                "text": "2001:db8:0:1::1",
                "correct": True,
                "rationale": (
                    "Correct. Steps: drop leading zeros per hextet (0DB8 -> db8, 0001 -> 1); "
                    "the longest consecutive run of all-zero hextets is hextets 5-7 (three zeros) "
                    "— replace with '::'; hextets 3-4 (0:1) stay as '0:1' "
                    "(hextet 3 is a single zero, hextet 4 is 1). Result: 2001:db8:0:1::1."
                ),
            },
            {
                "id": "b",
                "text": "2001:db8::1:0:0:0:1",
                "correct": False,
                "rationale": (
                    "Incorrect. The '::' here incorrectly substitutes after hextet 2, but "
                    "hextet 3 is 0000 and hextet 4 is 0001 — not all-zero. The consecutive "
                    "zeros are in positions 5-7, not immediately after hextet 2."
                ),
            },
            {
                "id": "c",
                "text": "2001:db8:0:1:0:0:0:1",
                "correct": False,
                "rationale": (
                    "Incorrect. Leading zeros are removed but the consecutive zero hextets "
                    "(positions 5-7) are not compressed with '::'. This is valid but not "
                    "fully compressed."
                ),
            },
            {
                "id": "d",
                "text": "2001:db8::1::1",
                "correct": False,
                "rationale": (
                    "Incorrect. '::' may appear at most once in an IPv6 address. Using it twice "
                    "makes the address ambiguous and syntactically invalid."
                ),
            },
        ],
        "explanation": (
            "IPv6 compression: (1) remove leading zeros in each hextet; "
            "(2) replace the longest run of consecutive all-zero hextets with '::' exactly once. "
            "Hextets 5, 6, 7 are all zero (three hextets) — longest run. "
            "Hextet 3 is '0' (single zero, stays); hextet 4 is '1'. "
            "Full address: 2001:db8:0:1::1."
        ),
    },
    {
        "id": "cd1v2-021",
        "domain": 1,
        "objective": "1.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "IPv6 addressing",
        "stem": (
            "An ISP assigns a company the prefix 2001:db8:abcd::/48. The company wants to "
            "create subnets using the standard /64 prefix length. "
            "How many /64 subnets can the company create from this /48?"
        ),
        "options": [
            {
                "id": "a",
                "text": "65536 (2^16)",
                "correct": True,
                "rationale": (
                    "Correct. From a /48 to a /64, there are 64 - 48 = 16 bits available for "
                    "subnetting. 2^16 = 65,536 possible /64 subnets."
                ),
            },
            {
                "id": "b",
                "text": "256 (2^8)",
                "correct": False,
                "rationale": (
                    "Incorrect. 2^8 = 256 would result from 8 subnet bits (e.g., /48 to /56), "
                    "not from /48 to /64."
                ),
            },
            {
                "id": "c",
                "text": "16 (2^4)",
                "correct": False,
                "rationale": (
                    "Incorrect. 2^4 = 16 corresponds to only 4 subnet bits, not the 16 bits "
                    "between /48 and /64."
                ),
            },
            {
                "id": "d",
                "text": "4294967296 (2^32)",
                "correct": False,
                "rationale": (
                    "Incorrect. 2^32 would require 32 subnet bits, which would take a /48 "
                    "to /80, not /64."
                ),
            },
        ],
        "explanation": (
            "IPv6 subnetting: bits available = new prefix - original prefix = 64 - 48 = 16. "
            "Number of subnets = 2^16 = 65,536. Each /64 subnet still has 2^64 possible "
            "interface addresses — the enormous scale of IPv6 addressing."
        ),
    },
    {
        "id": "cd1v2-022",
        "domain": 1,
        "objective": "1.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "IPv6 address types",
        "stem": (
            "A host receives a Router Advertisement with the 'M' (Managed Address Configuration) "
            "flag set. What should the host do to obtain its IPv6 address?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Contact a DHCPv6 server for a stateful address assignment",
                "correct": True,
                "rationale": (
                    "Correct. The M flag in an RA tells hosts to use stateful DHCPv6 (like "
                    "IPv4 DHCP) to obtain their IPv6 address, prefix, and other config from "
                    "a DHCPv6 server."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Use SLAAC to self-configure an address from the advertised prefix "
                    "and its own EUI-64 interface ID"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. SLAAC (Stateless Address Autoconfiguration) occurs when the "
                    "A (Autonomous) flag is set in the RA prefix option. The M flag specifically "
                    "overrides SLAAC in favor of stateful DHCPv6."
                ),
            },
            {
                "id": "c",
                "text": "Use only its link-local address and send a Router Solicitation",
                "correct": False,
                "rationale": (
                    "Incorrect. Link-local addresses are always auto-configured regardless of "
                    "RA flags; the M flag provides additional direction to use DHCPv6 for a "
                    "global unicast address."
                ),
            },
            {
                "id": "d",
                "text": "Ignore the RA and wait for an ARP broadcast",
                "correct": False,
                "rationale": (
                    "Incorrect. IPv6 replaces ARP with NDP. Ignoring an RA would leave the "
                    "host without guidance on address configuration; following the M flag "
                    "and contacting DHCPv6 is the correct response."
                ),
            },
        ],
        "explanation": (
            "IPv6 RA flags: A flag (in prefix option) = use SLAAC; M flag = use stateful "
            "DHCPv6 for address; O flag = use DHCPv6 for other config (DNS, etc.) but not "
            "address. When M=1, hosts use stateful DHCPv6 to get their global unicast "
            "address from a server."
        ),
    },
    {
        "id": "cd1v2-023",
        "domain": 1,
        "objective": "1.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "IPv6 address types",
        "stem": (
            "Which IPv6 address type is MOST comparable to IPv4 RFC 1918 private addresses, "
            "allowing organizations to use internal addresses that are not globally routed?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Unique Local Address (ULA), prefix fc00::/7 (commonly fd00::/8 for locally assigned)",
                "correct": True,
                "rationale": (
                    "Correct. ULAs (fc00::/7, practically fdxx::/48 with a random 40-bit "
                    "global ID) are IPv6's equivalent of RFC 1918: not globally routed, used "
                    "internally, and should not be advertised to the internet."
                ),
            },
            {
                "id": "b",
                "text": "Link-local address (fe80::/10)",
                "correct": False,
                "rationale": (
                    "Incorrect. Link-local addresses are scoped to a single link and auto-"
                    "configured on every interface. Unlike RFC 1918, they cannot be used across "
                    "multiple subnets within an organization."
                ),
            },
            {
                "id": "c",
                "text": "Global unicast address (2000::/3)",
                "correct": False,
                "rationale": (
                    "Incorrect. Global unicast addresses are publicly routable on the internet — "
                    "the IPv6 equivalent of public IPv4 addresses, not private ones."
                ),
            },
            {
                "id": "d",
                "text": "Multicast address (ff00::/8)",
                "correct": False,
                "rationale": (
                    "Incorrect. Multicast addresses are for one-to-many communication, not for "
                    "unicast host addressing. They have no relationship to RFC 1918."
                ),
            },
        ],
        "explanation": (
            "ULA (fc00::/7): the 'fd' prefix is locally assigned, with a random 40-bit Global ID "
            "to minimize collision probability. ULAs are internal, non-globally-routed, and "
            "comparable to RFC 1918. Unlike RFC 1918 + NAT, IPv6 normally provides global "
            "unicast addresses directly and does not require NAT."
        ),
    },
    {
        "id": "cd1v2-024",
        "domain": 1,
        "objective": "1.9",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "IPv6 address types",
        "stem": (
            "A router interface has the IPv6 address 2001:db8::1/64 and also the auto-generated "
            "link-local address fe80::1. An OSPFv3 neighbor relationship forms using which "
            "source address, and why?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "fe80::1 (link-local), because OSPFv3 uses link-local addresses as "
                    "next-hops and for neighbor adjacency on the local link"
                ),
                "correct": True,
                "rationale": (
                    "Correct. OSPFv3 forms neighbor relationships using link-local addresses. "
                    "Hello packets are sourced from and sent to link-local addresses "
                    "(ff02::5 for all OSPF routers). Global unicast addresses appear in LSAs "
                    "but not in the adjacency formation process."
                ),
            },
            {
                "id": "b",
                "text": (
                    "2001:db8::1 (global unicast), because OSPFv3 requires globally routable "
                    "addresses for neighbor formation"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. OSPFv3 deliberately uses link-local addresses for neighbor "
                    "adjacency — a key architectural difference from OSPFv2. Global unicast "
                    "addresses are not required for OSPFv3 hello packets."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The address with the highest numeric value, selected automatically "
                    "by OSPFv3"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. OSPFv3 does not choose the 'highest' address for adjacency. "
                    "The Router ID is a separate concept (32-bit, like IPv4); the source "
                    "address for OSPFv3 hellos is always link-local."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Either address, selected by the administrator using the 'ipv6 ospf "
                    "neighbor' command"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. OSPFv3 neighbor formation uses link-local addresses by "
                    "protocol design, not by administrator choice. The 'ipv6 ospf neighbor' "
                    "command specifies a neighbor's link-local address for point-to-point "
                    "links, not which local source to use."
                ),
            },
        ],
        "explanation": (
            "OSPFv3 runs natively over IPv6 and uses link-local (fe80::/10) addresses "
            "for all neighbor adjacency formation and hello multicast (ff02::5, ff02::6). "
            "This means OSPFv3 works even without a global unicast address on an interface, "
            "a key design feature inherited from IPv6's link-local requirement."
        ),
    },
    # ------------------------------------------------------------------ 1.10 client verify
    {
        "id": "cd1v2-025",
        "domain": 1,
        "objective": "1.10",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Client IP verification",
        "stem": (
            "A user reports being able to ping the default gateway (192.168.1.1) from their "
            "PC (192.168.1.50) but unable to reach any external websites or external IPs. "
            "Which is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A routing or NAT issue beyond the gateway — the gateway cannot forward packets to the internet",
                "correct": True,
                "rationale": (
                    "Correct. Successful gateway ping confirms Layer 1-3 local connectivity "
                    "is fine. Failure to reach external destinations points to a problem at or "
                    "beyond the gateway: ISP link down, missing default route, NAT misconfiguration, "
                    "or upstream failure."
                ),
            },
            {
                "id": "b",
                "text": "The PC has no IP address configured",
                "correct": False,
                "rationale": (
                    "Incorrect. The PC can ping the gateway (192.168.1.1) successfully, which "
                    "proves it has a valid IP address configured on the local subnet."
                ),
            },
            {
                "id": "c",
                "text": "The subnet mask on the PC is wrong",
                "correct": False,
                "rationale": (
                    "Incorrect. A wrong subnet mask would typically prevent the PC from "
                    "successfully pinging even the local gateway. A successful gateway ping "
                    "implies the mask is correct for local communication."
                ),
            },
            {
                "id": "d",
                "text": "The PC's NIC is faulty",
                "correct": False,
                "rationale": (
                    "Incorrect. A faulty NIC would prevent any network communication. The "
                    "successful gateway ping rules out a NIC failure."
                ),
            },
        ],
        "explanation": (
            "Troubleshooting path: ping loopback (127.0.0.1) -> ping own IP -> ping gateway "
            "-> ping external IP -> ping external hostname. Success at gateway but failure "
            "externally isolates the problem to routing/NAT/ISP beyond the gateway, not "
            "local PC configuration."
        ),
    },
    {
        "id": "cd1v2-026",
        "domain": 1,
        "objective": "1.10",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Client IP verification",
        "stem": (
            "A Windows PC can ping external IP addresses (e.g., 8.8.8.8) successfully but "
            "cannot browse to websites by name (e.g., www.example.com). "
            "Which is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "DNS resolution is failing — the PC cannot resolve hostnames to IP addresses",
                "correct": True,
                "rationale": (
                    "Correct. Successful ping by IP proves IP routing and connectivity are "
                    "working. Failure to reach sites by name with working IP connectivity "
                    "isolates the fault to DNS: wrong DNS server, DNS server unreachable, "
                    "or DNS server not responding."
                ),
            },
            {
                "id": "b",
                "text": "The default gateway is misconfigured",
                "correct": False,
                "rationale": (
                    "Incorrect. A misconfigured gateway would prevent pinging external IPs "
                    "like 8.8.8.8. Since external IP pings succeed, the gateway is correctly "
                    "configured and reachable."
                ),
            },
            {
                "id": "c",
                "text": "The PC's subnet mask is incorrect",
                "correct": False,
                "rationale": (
                    "Incorrect. A wrong subnet mask would disrupt local and potentially external "
                    "routing for all traffic. Successful external IP pings rule out a mask problem."
                ),
            },
            {
                "id": "d",
                "text": "The web browser is corrupted",
                "correct": False,
                "rationale": (
                    "Incorrect. While a browser issue could prevent browsing, the correct "
                    "network-layer diagnosis — confirmed by the ping test — is DNS failure. "
                    "A networking professional would fix DNS before blaming the browser."
                ),
            },
        ],
        "explanation": (
            "The diagnostic isolation: ping IP works = routing/NAT/connectivity OK. "
            "Name resolution fails = DNS issue. Check 'ipconfig /all' for DNS server "
            "addresses, then test with 'nslookup www.example.com'. Fix: correct DNS IP, "
            "ensure DNS server is reachable, or restore DNS service."
        ),
    },
    # ------------------------------------------------------------------ 1.11 wireless
    {
        "id": "cd1v2-027",
        "domain": 1,
        "objective": "1.11",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Wireless principles",
        "stem": (
            "A wireless engineer notices that 5 GHz clients have consistently higher throughput "
            "than 2.4 GHz clients on the same AP. Which combination of factors BEST explains this?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "5 GHz has more non-overlapping channels and less interference from "
                    "consumer devices (microwaves, Bluetooth), allowing higher data rates"
                ),
                "correct": True,
                "rationale": (
                    "Correct. The 5 GHz band offers many more non-overlapping channels "
                    "(20+ in the U-NII bands vs. 3 at 2.4 GHz) and far less interference "
                    "from non-Wi-Fi devices. Less contention and cleaner spectrum allow "
                    "clients to achieve higher modulation rates and throughput."
                ),
            },
            {
                "id": "b",
                "text": (
                    "2.4 GHz radio waves carry more data per Hz because of their lower frequency"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Data-carrying capacity (bits/Hz) depends on modulation and "
                    "channel conditions, not raw frequency. Lower frequency does not inherently "
                    "carry more data — in fact, 2.4 GHz's congested spectrum reduces effective "
                    "throughput."
                ),
            },
            {
                "id": "c",
                "text": (
                    "5 GHz APs always transmit at higher power, giving each client more signal"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Regulatory limits cap transmit power per band; 5 GHz actually "
                    "has shorter range than 2.4 GHz at the same power due to higher free-space "
                    "path loss. Higher throughput comes from channel availability, not power."
                ),
            },
            {
                "id": "d",
                "text": (
                    "5 GHz clients automatically use full-duplex communication, "
                    "unlike 2.4 GHz clients"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Wi-Fi is half-duplex in both bands; clients cannot "
                    "simultaneously transmit and receive on the same channel regardless "
                    "of band."
                ),
            },
        ],
        "explanation": (
            "5 GHz advantages: more non-overlapping channels (reducing co-channel interference), "
            "less congestion from non-Wi-Fi devices, and wider channel widths (40/80/160 MHz) "
            "increasing throughput. Trade-off: shorter range due to higher path loss. "
            "2.4 GHz: longer range but only 3 non-overlapping channels and heavy interference."
        ),
    },
    {
        "id": "cd1v2-028",
        "domain": 1,
        "objective": "1.11",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Wireless principles",
        "stem": (
            "A client is associated to an AP at a high signal strength but experiencing low "
            "throughput and high retransmissions. Other clients on a different AP are performing "
            "normally. Which wireless issue is MOST likely?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Co-channel interference or a hidden node causing excessive CSMA/CA collisions on that AP's channel",
                "correct": True,
                "rationale": (
                    "Correct. High signal, high retransmissions, and low throughput on one AP "
                    "while others are fine points to a channel-level problem: a neighboring AP "
                    "on the same channel (co-channel interference) or hidden nodes cause "
                    "excessive collisions/deferrals, driving retransmissions without the client "
                    "seeing a weak signal."
                ),
            },
            {
                "id": "b",
                "text": "The client's NIC is damaged, causing poor signal reception",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario states high signal strength, which rules out a "
                    "damaged NIC or poor reception. A hardware issue would show low RSSI."
                ),
            },
            {
                "id": "c",
                "text": "The AP is out of IP addresses in its DHCP pool",
                "correct": False,
                "rationale": (
                    "Incorrect. DHCP pool exhaustion would prevent new clients from getting "
                    "IP addresses, not cause retransmissions on an already-associated, "
                    "connected client."
                ),
            },
            {
                "id": "d",
                "text": "The client is too far from the AP and needs a repeater",
                "correct": False,
                "rationale": (
                    "Incorrect. Distance and weak signal are excluded by the 'high signal "
                    "strength' finding. Retransmissions with high signal are a medium-access "
                    "or interference issue, not a coverage issue."
                ),
            },
        ],
        "explanation": (
            "Retransmissions with strong signal indicate medium-contention problems: "
            "co-channel interference (overlapping AP cells on the same channel fighting for "
            "airtime) or hidden nodes (devices that cannot hear each other, leading to "
            "collisions at the AP). Solutions include changing channels, adjusting power/cell "
            "size, or enabling RTS/CTS for hidden node mitigation."
        ),
    },
    {
        "id": "cd1v2-029",
        "domain": 1,
        "objective": "1.11",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Wireless principles",
        "stem": (
            "What is the purpose of the BSS (Basic Service Set) and the BSSID in a Wi-Fi network?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A BSS is a single AP and its associated clients; the BSSID is the AP's "
                    "radio MAC address that uniquely identifies that cell"
                ),
                "correct": True,
                "rationale": (
                    "Correct. One BSS = one AP + its associated clients. The BSSID is the MAC "
                    "address of the AP's radio interface and uniquely identifies the BSS, "
                    "distinguishing it from other APs even broadcasting the same SSID."
                ),
            },
            {
                "id": "b",
                "text": (
                    "A BSS is a network of APs connected without a controller; "
                    "the BSSID is the WLC's IP address"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A network of APs covering a larger area is an ESS (Extended "
                    "Service Set). The BSSID is the AP radio's MAC address, not the WLC's IP."
                ),
            },
            {
                "id": "c",
                "text": (
                    "A BSS is a mesh of peer-to-peer client devices; "
                    "the BSSID is the SSID encryption key"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A peer-to-peer client mesh is an IBSS (Independent BSS / "
                    "ad-hoc mode). The BSSID is a MAC address, never an encryption key."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The BSS and BSSID are synonymous with the SSID and serve "
                    "the same identification purpose"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The SSID is the human-readable network name; the BSSID is the "
                    "AP radio's MAC address. Multiple APs can share the same SSID but each "
                    "has a unique BSSID."
                ),
            },
        ],
        "explanation": (
            "WLAN terminology: BSS = one AP + its associated clients, identified by the BSSID "
            "(AP radio MAC). SSID = network name (can span multiple BSSs in an ESS). "
            "ESS = multiple APs with the same SSID for roaming. IBSS = ad-hoc mode, "
            "no AP. Clients use BSSID to stay associated to a specific AP."
        ),
    },
    # ------------------------------------------------------------------ 1.12 virtualization
    {
        "id": "cd1v2-030",
        "domain": 1,
        "objective": "1.12",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Virtualization & containers",
        "stem": (
            "A company runs a Type 1 hypervisor on a physical server. A Type 2 hypervisor "
            "is being considered for a developer workstation. Which statement BEST "
            "distinguishes the two?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A Type 1 (bare-metal) hypervisor runs directly on hardware with no host OS, "
                    "offering better performance and isolation; a Type 2 (hosted) hypervisor "
                    "runs as an application on top of a host OS"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Type 1 hypervisors (VMware ESXi, Hyper-V, KVM on bare metal) run "
                    "directly on hardware, giving VMs low-latency hardware access and strong "
                    "isolation — preferred for production servers. Type 2 (VMware Workstation, "
                    "VirtualBox) runs on a host OS, adding overhead — acceptable for developer "
                    "workstations."
                ),
            },
            {
                "id": "b",
                "text": (
                    "A Type 2 hypervisor is faster because the host OS optimizes "
                    "hardware access for VMs"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Adding a host OS layer (Type 2) introduces overhead, making "
                    "Type 2 generally slower than Type 1 bare-metal hypervisors for production "
                    "workloads."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Both types require a host OS underneath for hardware abstraction"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Type 1 hypervisors require no underlying host OS — they are "
                    "the OS-equivalent for the hardware. Only Type 2 requires a pre-existing "
                    "host OS."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Type 1 hypervisors can only run one VM at a time for performance reasons"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Type 1 hypervisors are designed to run many VMs simultaneously "
                    "and are specifically deployed in data centers to consolidate dozens or "
                    "hundreds of VMs on one physical host."
                ),
            },
        ],
        "explanation": (
            "Hypervisor types: Type 1 (bare-metal) = direct hardware control, no host OS, "
            "used in data centers (ESXi, Hyper-V, KVM). Type 2 (hosted) = application on "
            "host OS, adds overhead, used for dev/test (VirtualBox, VMware Workstation). "
            "Both abstract hardware and run multiple guest VMs."
        ),
    },
    {
        "id": "cd1v2-031",
        "domain": 1,
        "objective": "1.12",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Virtualization & containers",
        "stem": (
            "An organization wants to migrate its on-premises application servers to a cloud "
            "model where the cloud provider manages the OS, runtime, and middleware, and the "
            "organization only manages its application code and data. Which cloud service "
            "model matches this requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Platform as a Service (PaaS)",
                "correct": True,
                "rationale": (
                    "Correct. PaaS provides a managed platform (OS, runtime, middleware, "
                    "database) so developers focus on application code and data only. The "
                    "cloud provider handles patching, scaling, and infrastructure."
                ),
            },
            {
                "id": "b",
                "text": "Infrastructure as a Service (IaaS)",
                "correct": False,
                "rationale": (
                    "Incorrect. With IaaS, the customer manages the OS, middleware, and "
                    "applications; only the hardware/network/hypervisor is provider-managed. "
                    "The organization would still need to manage the OS and runtime."
                ),
            },
            {
                "id": "c",
                "text": "Software as a Service (SaaS)",
                "correct": False,
                "rationale": (
                    "Incorrect. SaaS delivers complete applications to end users (e.g., "
                    "Office 365, Salesforce). The organization has no control over application "
                    "code — but the scenario requires the organization to manage its own code."
                ),
            },
            {
                "id": "d",
                "text": "Network as a Service (NaaS)",
                "correct": False,
                "rationale": (
                    "Incorrect. NaaS provides network connectivity and transport as a service. "
                    "It does not include application platform or middleware management."
                ),
            },
        ],
        "explanation": (
            "Cloud service models — management responsibility: "
            "IaaS: provider=hardware+hypervisor, customer=OS+middleware+app+data. "
            "PaaS: provider=hardware+hypervisor+OS+middleware, customer=app+data. "
            "SaaS: provider=everything, customer=data/configuration only. "
            "PaaS is the 'deploy code only' model."
        ),
    },
    # ------------------------------------------------------------------ 1.13 switching
    {
        "id": "cd1v2-032",
        "domain": 1,
        "objective": "1.13",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Switching concepts / MAC table",
        "stem": (
            "An attacker sends a continuous flood of frames with randomly generated, never-"
            "repeated source MAC addresses into a switch port. What is the likely impact on "
            "the switch?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The switch's MAC address table fills up (CAM table overflow); "
                    "subsequent frames with unknown MACs are flooded out all ports, "
                    "allowing the attacker to intercept traffic"
                ),
                "correct": True,
                "rationale": (
                    "Correct. This is a MAC flooding attack. The switch learns a fake MAC per "
                    "frame, quickly exhausting the finite CAM table. Once full, new unknown "
                    "unicast destinations are flooded like broadcasts, turning the switch into "
                    "a hub and exposing all traffic to the attacker."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The switch immediately blocks the attacking port using storm control"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Storm control limits broadcast/multicast/unknown-unicast "
                    "traffic rates, but standard storm control is not specifically designed to "
                    "detect MAC flooding from unique source MACs. Port security is the relevant "
                    "countermeasure."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The switch drops all frames once the CAM table is full, stopping "
                    "all network traffic until it reboots"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Most switches do not drop all frames when the CAM table is "
                    "full; instead, they continue flooding frames with unknown destinations, "
                    "which is the mechanism of the attack."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The switch automatically enables port security to limit MAC addresses "
                    "per port"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Port security is not auto-enabled; it must be manually "
                    "configured. Without it, the switch has no mechanism to limit the number "
                    "of MAC addresses learned on a port."
                ),
            },
        ],
        "explanation": (
            "MAC flooding (CAM overflow) attack: flood the switch with frames having unique "
            "random source MACs to exhaust the CAM table. The switch then floods all unknown "
            "unicast, becoming a hub and enabling passive sniffing. Mitigation: port security "
            "('switchport port-security maximum N') to limit MACs per port and shut/restrict "
            "violating ports."
        ),
    },
    {
        "id": "cd1v2-033",
        "domain": 1,
        "objective": "1.13",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Switching concepts / MAC table",
        "stem": (
            "A switch is running Rapid PVST+. Which port state directly forwards traffic "
            "and participates in the active topology?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Forwarding",
                "correct": True,
                "rationale": (
                    "Correct. In RSTP (802.1w) and Rapid PVST+, the Forwarding state is the "
                    "active state where a port sends and receives data frames and participates "
                    "in MAC learning. It is the operational 'normal' state."
                ),
            },
            {
                "id": "b",
                "text": "Listening",
                "correct": False,
                "rationale": (
                    "Incorrect. Listening is an 802.1D (classic STP) state — ports participate "
                    "in BPDU exchange but do not forward data or learn MACs. RSTP reduces these "
                    "transitional states."
                ),
            },
            {
                "id": "c",
                "text": "Discarding",
                "correct": False,
                "rationale": (
                    "Incorrect. The Discarding state in RSTP is a non-forwarding state that "
                    "combines the 802.1D Blocking/Listening roles. Ports in Discarding do not "
                    "pass data frames."
                ),
            },
            {
                "id": "d",
                "text": "Learning",
                "correct": False,
                "rationale": (
                    "Incorrect. In the Learning state, a port builds the MAC address table "
                    "from incoming frames but does not yet forward data. It transitions to "
                    "Forwarding after the learning period."
                ),
            },
        ],
        "explanation": (
            "RSTP port states: Discarding (no data, may participate in BPDUs), "
            "Learning (builds MAC table, no data forwarding), Forwarding (fully active — "
            "learns MACs and forwards data). RSTP consolidates classic STP's five states "
            "(Blocking, Listening, Learning, Forwarding, Disabled) into three."
        ),
    },
    {
        "id": "cd1v2-034",
        "domain": 1,
        "objective": "1.13",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Switching concepts / MAC table",
        "stem": (
            "Which TWO types of frames does a switch always flood out all ports in the same "
            "VLAN (except the ingress port), regardless of the MAC address table? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Broadcast frames (destination MAC FF:FF:FF:FF:FF:FF)",
                "correct": True,
                "rationale": (
                    "Correct. Broadcast frames are always flooded within a VLAN — this is the "
                    "definition of a broadcast domain. No MAC table lookup can direct a broadcast "
                    "to a single port."
                ),
            },
            {
                "id": "b",
                "text": "Unknown unicast frames (destination MAC not in the MAC table)",
                "correct": True,
                "rationale": (
                    "Correct. When the destination MAC is not in the table, the switch cannot "
                    "make a forwarding decision and floods the frame within the VLAN to discover "
                    "the destination — the fundamental source of the 'unknown unicast flood.'"
                ),
            },
            {
                "id": "c",
                "text": "Known unicast frames (destination MAC exists in the MAC table)",
                "correct": False,
                "rationale": (
                    "Incorrect. Known unicast frames are forwarded only to the specific port "
                    "mapped to that destination MAC — this is the entire efficiency benefit "
                    "of switching over hubs."
                ),
            },
            {
                "id": "d",
                "text": "Tagged 802.1Q management frames from the native VLAN",
                "correct": False,
                "rationale": (
                    "Incorrect. Management/control frames are handled according to their own "
                    "protocols. Native VLAN frames are not inherently flooded to all ports; "
                    "their forwarding follows the MAC table like any other unicast frame."
                ),
            },
            {
                "id": "e",
                "text": "ICMP echo replies destined for a known host",
                "correct": False,
                "rationale": (
                    "Incorrect. If the destination MAC of an ICMP echo reply is in the table, "
                    "the switch forwards it to the known port only, not floods. Flooding only "
                    "happens for unknown unicast, broadcast, or multicast."
                ),
            },
        ],
        "explanation": (
            "A switch floods within a VLAN (all ports except ingress) for: "
            "(1) Broadcasts (FF:FF:FF:FF:FF:FF), "
            "(2) Unknown unicast (destination MAC not in table), "
            "(3) Multicast (unless IGMP snooping filters it). "
            "Known unicast is forwarded to the single mapped port — this is the core "
            "efficiency advantage of a switch over a hub."
        ),
    },
    # Additional mixed-topic questions to reach 40
    {
        "id": "cd1v2-035",
        "domain": 1,
        "objective": "1.6",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "IPv4 subnetting",
        "stem": (
            "A network engineer has 10.0.0.0/8 to allocate with VLSM. She assigns "
            "10.0.0.0/9 to Site A. What is the first subnet available for the next "
            "allocation after Site A's block, and what is its maximum prefix?"
        ),
        "options": [
            {
                "id": "a",
                "text": "10.128.0.0/9 is the next contiguous block; the maximum prefix usable from it without overlap is /9",
                "correct": True,
                "rationale": (
                    "Correct. A /9 has a block size of 128 in the second octet. "
                    "10.0.0.0/9 covers 10.0.0.0 - 10.127.255.255. The next block of the "
                    "same size is 10.128.0.0/9 (10.128.0.0 - 10.255.255.255). Subnets of "
                    "/9 or smaller can be carved from this space without overlap."
                ),
            },
            {
                "id": "b",
                "text": "10.0.128.0/9 is the next block",
                "correct": False,
                "rationale": (
                    "Incorrect. /9 changes the boundary at the second octet, not the third. "
                    "10.0.0.0/9 spans the entire .0.x.x to .127.x.x range. The next block "
                    "starts at 10.128.0.0 in the second octet."
                ),
            },
            {
                "id": "c",
                "text": "10.1.0.0/8 is the next available network",
                "correct": False,
                "rationale": (
                    "Incorrect. The allocation is within the 10.0.0.0/8 space; the next /9 "
                    "inside /8 is 10.128.0.0/9, not a new /8 outside the assigned space."
                ),
            },
            {
                "id": "d",
                "text": "10.64.0.0/10 is the smallest next available block",
                "correct": False,
                "rationale": (
                    "Incorrect. 10.64.0.0/10 is within the 10.0.0.0/9 block (which covers "
                    "10.0.0.0 - 10.127.255.255) and would overlap with Site A's allocation. "
                    "It is not available for a new allocation."
                ),
            },
        ],
        "explanation": (
            "10.0.0.0/9 mask = 255.128.0.0; block size = 128 in the second octet. "
            "Range: 10.0.0.0 - 10.127.255.255. Next contiguous /9: 10.128.0.0 - 10.255.255.255. "
            "VLSM assigns the largest needed subnet first, then allocates smaller subnets "
            "from remaining space, always staying within non-overlapping boundaries."
        ),
    },
    {
        "id": "cd1v2-036",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network components",
        "stem": (
            "An enterprise deploys Cisco SD-Access with a fabric underlay and overlay. "
            "Which statement BEST describes the role of the control plane node in this solution?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The control plane node runs LISP to map endpoint identifiers (EIDs) "
                    "to routing locators (RLOCs), telling fabric nodes where to send "
                    "encapsulated traffic for any endpoint"
                ),
                "correct": True,
                "rationale": (
                    "Correct. In SD-Access, the control plane node uses LISP as the mapping "
                    "system. Edge nodes register endpoints' EIDs, and the control plane node "
                    "resolves EID-to-RLOC mappings, directing VXLAN-encapsulated traffic "
                    "across the fabric to the correct edge node."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The control plane node is the physical switch that connects "
                    "all end devices in the fabric"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The physical devices connecting end hosts are edge nodes "
                    "(access layer). The control plane node is a logical/software function "
                    "(often on the border or a dedicated device) running LISP mapping, "
                    "not an access switch."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The control plane node encrypts all user traffic traversing "
                    "the fabric overlay"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Encryption in SD-Access fabrics (MACsec or IPsec) is handled "
                    "by the data plane in the fabric nodes, not the LISP control plane node."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The control plane node is Cisco DNA Center, which directly "
                    "forwards all packets"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. DNA Center is the management and orchestration platform "
                    "(Northbound), not the data-plane or LISP control-plane node. The "
                    "control plane function runs on fabric nodes designated as map servers."
                ),
            },
        ],
        "explanation": (
            "SD-Access fabric layers: underlay (routed IP network, typically IS-IS), "
            "overlay (VXLAN encapsulation for data plane, LISP for control plane). "
            "The control plane node acts as the LISP Map Server/Resolver: edge nodes "
            "register their endpoints' EIDs; when an edge node needs to reach an unknown "
            "endpoint it queries the control plane node for the RLOC (edge node IP)."
        ),
    },
    {
        "id": "cd1v2-037",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Network topologies",
        "stem": (
            "Which topology provides the HIGHEST redundancy and the MOST available paths "
            "between any two nodes, at the cost of the greatest number of links?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Full mesh",
                "correct": True,
                "rationale": (
                    "Correct. In a full mesh, every node connects directly to every other node. "
                    "This provides maximum redundancy (multiple paths between any pair) but "
                    "requires n(n-1)/2 links — costly and complex to manage at scale."
                ),
            },
            {
                "id": "b",
                "text": "Hub-and-spoke (star)",
                "correct": False,
                "rationale": (
                    "Incorrect. Hub-and-spoke provides only one path between any two spoke "
                    "nodes (through the hub) and is the least redundant; the hub is a single "
                    "point of failure."
                ),
            },
            {
                "id": "c",
                "text": "Ring",
                "correct": False,
                "rationale": (
                    "Incorrect. A ring provides exactly two paths between any pair of nodes. "
                    "A single link failure splits the ring and eliminates one path — less "
                    "redundant than full mesh."
                ),
            },
            {
                "id": "d",
                "text": "Partial mesh",
                "correct": False,
                "rationale": (
                    "Incorrect. A partial mesh has redundant paths for some but not all nodes, "
                    "providing more redundancy than hub-and-spoke but less than full mesh, "
                    "with fewer links than full mesh."
                ),
            },
        ],
        "explanation": (
            "Full mesh: n nodes require n(n-1)/2 links; every pair has a direct path. "
            "Maximum redundancy and minimum hop count, but link count grows as O(n^2), "
            "making it impractical for large networks. "
            "Partial mesh balances cost and redundancy. Hub-and-spoke minimizes links "
            "but centralizes all paths through one node."
        ),
    },
    {
        "id": "cd1v2-038",
        "domain": 1,
        "objective": "1.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "IPv6 address types",
        "stem": (
            "A host with IPv6 address 2001:db8::a/64 needs to communicate with another host "
            "at 2001:db8::b/64 on the same link. Which ICMPv6 message type does the first "
            "host send to resolve the target's Layer 2 address, and to which destination "
            "does it send it?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Neighbor Solicitation (NS), sent to the target's solicited-node "
                    "multicast address (ff02::1:ffxx:xxxx)"
                ),
                "correct": True,
                "rationale": (
                    "Correct. IPv6 Neighbor Discovery replaces ARP. To resolve a link-layer "
                    "address, the source sends an ICMPv6 Neighbor Solicitation (type 135) to "
                    "the target's solicited-node multicast address, derived from the last 24 "
                    "bits of the target's IPv6 address. The target replies with a Neighbor "
                    "Advertisement (type 136)."
                ),
            },
            {
                "id": "b",
                "text": (
                    "ARP Request, broadcast to FF:FF:FF:FF:FF:FF at Layer 2"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. ARP is an IPv4 mechanism. IPv6 uses ICMPv6 Neighbor Discovery "
                    "Protocol (NDP) with Neighbor Solicitation/Advertisement messages — ARP "
                    "does not exist in IPv6."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Router Solicitation (RS), sent to ff02::2 (all routers) "
                    "to find the next hop"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Router Solicitation is for discovering default gateways "
                    "(sent to ff02::2), not for resolving a neighbor's Layer 2 address on "
                    "the same link."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Echo Request (ping), sent to the target's link-local address "
                    "to trigger an ARP-like response"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. An ICMPv6 Echo Request tests reachability (like ping) but "
                    "does not resolve Layer 2 addresses. The L2 address must already be known "
                    "or resolved via Neighbor Solicitation before the ping can even be sent."
                ),
            },
        ],
        "explanation": (
            "NDP replaces ARP in IPv6. L2 address resolution: "
            "Neighbor Solicitation (NS, ICMPv6 type 135) is sent to the solicited-node "
            "multicast address ff02::1:ff + last 24 bits of target IPv6. "
            "The target responds with a Neighbor Advertisement (NA, type 136) containing "
            "its link-layer (MAC) address. This is more efficient than ARP's link-wide broadcast."
        ),
    },
    {
        "id": "cd1v2-039",
        "domain": 1,
        "objective": "1.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Cabling & interfaces",
        "stem": (
            "A campus distribution switch shows an interface as '1000BASE-T, media type is "
            "twisted pair'. The connected access switch is 1 Gbps capable. The link negotiates "
            "to 100 Mbps/full-duplex. Which is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "One or both interfaces have speed manually set to 100 Mbps, preventing autonegotiation from reaching 1 Gbps",
                "correct": True,
                "rationale": (
                    "Correct. 1000BASE-T requires both ends to autonegotiate; it cannot be "
                    "manually forced to 1 Gbps using 'speed 1000' on a standard copper "
                    "interface in some IOS versions — but more commonly, if one end is "
                    "hardcoded to 100 Mbps, autonegotiation on the other end falls back to "
                    "the highest commonly supported speed (100 Mbps), never reaching 1 Gbps."
                ),
            },
            {
                "id": "b",
                "text": "The cable is Cat 5e which cannot support 1 Gbps",
                "correct": False,
                "rationale": (
                    "Incorrect. Cat 5e supports 1000BASE-T (Gigabit Ethernet) up to 100 m. "
                    "A Cat 5e cable is not a limiting factor for 1 Gbps on a typical campus run."
                ),
            },
            {
                "id": "c",
                "text": "The SFP transceiver is rated for 100 Mbps only",
                "correct": False,
                "rationale": (
                    "Incorrect. The interface description states '1000BASE-T, media type is "
                    "twisted pair' — this is a built-in RJ45 copper port, not an SFP module. "
                    "SFP transceivers are used for fiber or modular copper ports."
                ),
            },
            {
                "id": "d",
                "text": "The switch's backplane is saturated, throttling the link to 100 Mbps",
                "correct": False,
                "rationale": (
                    "Incorrect. Backplane congestion causes packet drops or queuing, not "
                    "link-speed negotiation downgrade. The physical negotiated speed is "
                    "a Layer 1 function independent of backplane load."
                ),
            },
        ],
        "explanation": (
            "1000BASE-T (Gigabit Ethernet on copper) requires autonegotiation — both ends "
            "must participate. If one end is manually set to 100 Mbps, the autonegotiating "
            "end falls back to the highest mutually supported speed (100 Mbps). "
            "Fix: set both ends to 'speed auto' and 'duplex auto', or both to matching "
            "values. Check 'show interfaces' for speed and duplex negotiation."
        ),
    },
    {
        "id": "cd1v2-040",
        "domain": 1,
        "objective": "1.10",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Client IP verification",
        "stem": (
            "A technician uses 'ipconfig /all' on a Windows PC and sees: "
            "IP: 10.1.1.100, Mask: 255.255.255.0, Gateway: 10.1.1.1, "
            "DNS: 10.1.1.200, DHCP: Yes, Lease obtained. "
            "The user cannot reach the server at 10.1.2.50. "
            "Which TWO commands should the technician run NEXT to narrow down the fault? "
            "(Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "ping 10.1.1.1 (test connectivity to the default gateway)",
                "correct": True,
                "rationale": (
                    "Correct. Pinging the gateway tests Layer 3 local connectivity. If this "
                    "fails, the issue is on the local segment (PC config, switch, or gateway). "
                    "If it succeeds, the problem is beyond the gateway (routing, ACL, server)."
                ),
            },
            {
                "id": "b",
                "text": "ping 10.1.2.50 (test connectivity to the destination server)",
                "correct": True,
                "rationale": (
                    "Correct. Pinging the target server tests end-to-end IP reachability. "
                    "Combined with the gateway ping result, this helps isolate whether the "
                    "failure is local, at the router/routing table, or at the destination."
                ),
            },
            {
                "id": "c",
                "text": "ipconfig /release followed by ipconfig /renew to reset the DHCP lease",
                "correct": False,
                "rationale": (
                    "Incorrect. The lease is already obtained and the IP configuration looks "
                    "correct. Renewing DHCP would not help diagnose a routing or connectivity "
                    "problem to a different subnet; it should only be done if the addressing "
                    "itself is suspected."
                ),
            },
            {
                "id": "d",
                "text": "Reinstall the network adapter driver",
                "correct": False,
                "rationale": (
                    "Incorrect. The PC has obtained a valid DHCP lease and has a complete IP "
                    "configuration, indicating the NIC and driver are functional. Driver "
                    "reinstallation is not a useful next step for diagnosing a routing problem."
                ),
            },
            {
                "id": "e",
                "text": "traceroute 10.1.2.50 to show the path and identify where packets stop",
                "correct": False,
                "rationale": (
                    "Incorrect. While traceroute is valuable, the question asks which TWO "
                    "commands to run NEXT as immediate narrowing steps. The logical sequence "
                    "is first ping gateway, then ping destination; traceroute is a follow-on "
                    "tool once basic pings confirm or deny reachability. Between the five "
                    "options, ping gateway and ping destination are the correct 'next two.'"
                ),
            },
        ],
        "explanation": (
            "Structured troubleshooting: (1) ping 127.0.0.1 (loopback/stack) — implied OK "
            "since ipconfig /all shows config; (2) ping own IP (10.1.1.100); "
            "(3) ping gateway (10.1.1.1) — tests local segment; "
            "(4) ping destination (10.1.2.50) — tests routing to remote subnet. "
            "These steps systematically isolate local vs. remote failures before using "
            "traceroute or deeper tools."
        ),
    },
]

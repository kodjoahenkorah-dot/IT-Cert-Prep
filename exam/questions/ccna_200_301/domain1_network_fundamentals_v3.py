"""Domain 1 — Network Fundamentals v3 (Cisco CCNA 200-301).

45 brand-new scenario-based questions covering objectives 1.1-1.13.
Misconception-targeting distractors; subnetting/VLSM/IPv6 math verified.
"""

QUESTIONS = [
    # --------------------------------------------------------- 1.1 Network components
    {
        "id": "cd1v3-001",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network components",
        "stem": (
            "A hospital deploys 802.11ax APs managed by a WLC. The security team requires "
            "that client traffic be inspected by a next-generation firewall before reaching "
            "any server VLAN. Traffic from lightweight APs arrives at the WLC via CAPWAP "
            "tunnels. Which forwarding mode must be configured on the WLC so that client "
            "frames exit the WLC onto a switch trunk port and can be directed to the firewall?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Local (central switching) mode, where the WLC decapsulates CAPWAP and bridges client traffic onto the wired network",
                "correct": True,
                "rationale": "Correct. In central (local) switching mode the WLC decapsulates CAPWAP traffic from APs and bridges it onto the wired LAN, where it can then be directed to an NGFW before reaching server VLANs.",
            },
            {
                "id": "b",
                "text": "FlexConnect local switching mode, where traffic exits the AP directly onto the local switch without passing through the WLC",
                "correct": False,
                "rationale": "Incorrect. FlexConnect local switching forwards client traffic locally at the AP's switch, bypassing the WLC — traffic would not pass centrally through an NGFW in that path.",
            },
            {
                "id": "c",
                "text": "Monitor mode, where the AP passively scans all channels for rogue detection",
                "correct": False,
                "rationale": "Incorrect. Monitor mode is an AP role for WIDS/rogue scanning; the AP in this mode does not serve client associations at all.",
            },
            {
                "id": "d",
                "text": "Sniffer mode, where the AP captures 802.11 frames and forwards them to a packet analyzer",
                "correct": False,
                "rationale": "Incorrect. Sniffer mode captures raw 802.11 frames for analysis; it does not carry live client data traffic through the WLC to the firewall.",
            },
        ],
        "explanation": (
            "Central (local) switching: all AP client traffic tunnels via CAPWAP to the WLC, "
            "which decapsulates and bridges it onto the distribution switch. This allows a "
            "centrally placed NGFW to inspect all wireless traffic. FlexConnect local switching "
            "keeps traffic at the branch AP, suitable when WAN bandwidth is limited but not for "
            "centralized inspection."
        ),
    },
    {
        "id": "cd1v3-002",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network components",
        "stem": (
            "An enterprise switches from traditional device-by-device CLI management to an "
            "intent-based networking model. An engineer defines a policy that all IoT devices "
            "must be placed in a quarantine VLAN with internet access only. The controller "
            "automatically translates this into per-device configurations. Which plane does "
            "the controller use to push these configurations to the physical devices?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The southbound interface (SBI) — APIs such as NETCONF/RESTCONF or OpenFlow that the controller uses to program device data/control planes",
                "correct": True,
                "rationale": "Correct. In SDN/IBN architectures, the controller uses its southbound interfaces (NETCONF, RESTCONF, OpenFlow, etc.) to push configuration and flow rules down to physical devices.",
            },
            {
                "id": "b",
                "text": "The northbound interface (NBI) — REST APIs that applications use to communicate policy intentions to the controller",
                "correct": False,
                "rationale": "Incorrect. Northbound interfaces face upward toward applications and orchestration tools that instruct the controller; southbound interfaces face the physical network devices.",
            },
            {
                "id": "c",
                "text": "The management plane — out-of-band SSH sessions initiated by each device to pull its own config",
                "correct": False,
                "rationale": "Incorrect. The management plane handles device access (SSH, SNMP); an intent-based controller actively pushes policy via southbound APIs rather than devices pulling via SSH.",
            },
            {
                "id": "d",
                "text": "The control plane — routing protocol updates that carry policy information to neighboring devices",
                "correct": False,
                "rationale": "Incorrect. Routing protocol updates carry reachability information, not arbitrary policy translations; the controller uses southbound APIs to program device behavior.",
            },
        ],
        "explanation": (
            "SDN controllers expose northbound APIs to applications and use southbound interfaces "
            "(NETCONF, RESTCONF, OpenFlow, gRPC) to program the data and control planes of physical "
            "devices. Intent is abstracted at the northbound level and realized at the network device "
            "level via the southbound interface."
        ),
    },
    {
        "id": "cd1v3-003",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Network components",
        "stem": (
            "A branch office has a single device providing routing, switching, firewall, and "
            "wireless AP functionality. An engineer needs to add a second WAN connection for "
            "redundancy. The device has no additional WAN interface card. What type of device "
            "is this, and why does it limit WAN expansion compared with a dedicated router?"
        ),
        "options": [
            {
                "id": "a",
                "text": "An integrated services router (ISR) without available WAN NIM slots; dedicated routers offer additional module bays for WAN interface cards",
                "correct": True,
                "rationale": "Correct. SOHO/small-branch multifunction routers (including compact ISRs) often have limited or no modular WAN expansion slots; a dedicated modular router provides NIM/WAN card bays for adding interfaces.",
            },
            {
                "id": "b",
                "text": "A Layer 3 switch; it cannot route traffic at all and must be replaced with a router",
                "correct": False,
                "rationale": "Incorrect. A multifunction branch device performs routing; a Layer 3 switch does route but is LAN-focused — neither description matches the stated limitation accurately.",
            },
            {
                "id": "c",
                "text": "A wireless LAN controller; WLCs do not support WAN interfaces",
                "correct": False,
                "rationale": "Incorrect. The device described provides routing, switching, firewall, and AP functions — that is a multifunction router/gateway, not a dedicated WLC.",
            },
            {
                "id": "d",
                "text": "A firewall appliance; firewalls cannot route between VLANs",
                "correct": False,
                "rationale": "Incorrect. Modern firewalls often perform inter-VLAN routing; the device described is a multifunction router/gateway, not solely a firewall.",
            },
        ],
        "explanation": (
            "SOHO/compact multifunction devices consolidate many functions but sacrifice modularity. "
            "Dedicated modular routers provide WAN interface card slots (NIM, EHWIC, etc.) for "
            "expanding connectivity. When WAN redundancy is needed and no module slots exist, "
            "replacement or an external dedicated router is required."
        ),
    },
    # --------------------------------------------------------- 1.2 Network topologies
    {
        "id": "cd1v3-004",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network topologies",
        "stem": (
            "A company operates a WAN connecting a hub site to eight branch offices. Each "
            "branch communicates with the hub but never directly with other branches. A "
            "link failure at one branch should not affect any other branch. Which WAN "
            "topology fits this design, and what is its primary disadvantage?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Hub-and-spoke (star); if the hub site fails, all branch-to-branch communication through the hub also fails",
                "correct": True,
                "rationale": "Correct. Hub-and-spoke places all branches as spokes connected only to a central hub. A branch link failure is isolated; however, the hub is a single point of failure for all inter-branch paths.",
            },
            {
                "id": "b",
                "text": "Full mesh; every node connects to every other, maximizing resilience with no single point of failure",
                "correct": False,
                "rationale": "Incorrect. Full mesh connects every site to every other site — branches would connect directly to each other, which does not match the described branch-to-hub-only requirement.",
            },
            {
                "id": "c",
                "text": "Partial mesh; provides some direct branch-to-branch links to reduce hub dependency",
                "correct": False,
                "rationale": "Incorrect. Partial mesh includes some direct branch links; the described design has none — it is hub-and-spoke.",
            },
            {
                "id": "d",
                "text": "Ring topology; each branch connects to two neighbors, providing path redundancy",
                "correct": False,
                "rationale": "Incorrect. A ring connects sites in a circular chain; the scenario describes branches connecting only to the hub, not to each other in sequence.",
            },
        ],
        "explanation": (
            "Hub-and-spoke (star WAN): all branches connect exclusively to the hub, so branch "
            "failures are isolated. The hub is a single point of failure — if it goes down, all "
            "inter-branch traffic (which must traverse the hub) is disrupted. Redundant hub "
            "devices or partial-mesh upgrades can mitigate this."
        ),
    },
    {
        "id": "cd1v3-005",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Network topologies",
        "stem": (
            "An engineer is documenting a physical vs. logical topology. The network uses "
            "a physical star (all cables run to a central switch), but Spanning Tree has "
            "blocked one uplink, so some VLANs follow a different path. Which statement "
            "is accurate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The physical topology is a star; the logical topology (active traffic path after STP) may form a different tree shape with some links inactive",
                "correct": True,
                "rationale": "Correct. Physical topology describes how cables and devices are connected physically; logical topology describes how traffic actually flows. STP blocking changes the active logical path without changing physical cabling.",
            },
            {
                "id": "b",
                "text": "Physical and logical topologies are always identical in an Ethernet LAN",
                "correct": False,
                "rationale": "Incorrect. They can differ significantly; STP blocking, tunneling (e.g., GRE), and VPNs are common examples where logical paths differ from physical connections.",
            },
            {
                "id": "c",
                "text": "STP changes the physical topology by cutting the cable on blocked ports",
                "correct": False,
                "rationale": "Incorrect. STP places ports in a blocking state in software; no physical cable is cut or disconnected.",
            },
            {
                "id": "d",
                "text": "The logical topology is always a ring when STP is in use",
                "correct": False,
                "rationale": "Incorrect. STP builds a loop-free tree, not a ring, as the logical active topology.",
            },
        ],
        "explanation": (
            "Physical topology = physical cable/device layout. Logical topology = how data "
            "actually flows. A physical star with STP blocking creates a logical tree that "
            "differs from the physical connectivity. Understanding both is critical for "
            "troubleshooting and design."
        ),
    },
    {
        "id": "cd1v3-006",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network topologies",
        "stem": (
            "A data center network team is adding capacity. They need to add more servers "
            "without redesigning the entire fabric. The chosen topology allows new leaf "
            "switches to be added simply by connecting them to all existing spine switches. "
            "What is this topology, and what scaling constraint still exists?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Spine-leaf; the number of leaf switches is bounded by the port count of the spine switches",
                "correct": True,
                "rationale": "Correct. Spine-leaf scales by adding leaf switches connected to all spines. The limit is the port density of the spine layer — each new leaf requires one port on every spine switch.",
            },
            {
                "id": "b",
                "text": "Three-tier campus; new access switches connect to any distribution switch with no constraint",
                "correct": False,
                "rationale": "Incorrect. The described add-new-leaf-to-all-spines pattern is characteristic of spine-leaf, not a three-tier campus where access switches connect to two distribution switches.",
            },
            {
                "id": "c",
                "text": "Full mesh; every new switch connects to all existing switches, with no port-count limit",
                "correct": False,
                "rationale": "Incorrect. Full mesh grows as n(n-1)/2 links — actually the most port-intensive topology. The described pattern (connect only to spines) is spine-leaf.",
            },
            {
                "id": "d",
                "text": "Ring topology; new switches insert into the ring between two existing nodes",
                "correct": False,
                "rationale": "Incorrect. A ring inserts new nodes between existing ones; spine-leaf connects every new leaf to every spine, which is the described behavior.",
            },
        ],
        "explanation": (
            "In spine-leaf, a new leaf switch is added by connecting it to every spine. This "
            "provides uniform any-leaf-to-any-leaf latency. The scaling ceiling is the spine "
            "port count — when spine ports are exhausted, super-spines or new spines must be "
            "added, which requires touching all leaves."
        ),
    },
    # --------------------------------------------------------- 1.3 Cabling & interfaces
    {
        "id": "cd1v3-007",
        "domain": 1,
        "objective": "1.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Cabling & interfaces",
        "stem": (
            "A 40 Gbps connection must be made between two ToR switches 80 meters apart "
            "within the same data center row. Which media type is the BEST fit, balancing "
            "cost and reach?"
        ),
        "options": [
            {
                "id": "a",
                "text": "OM4 multimode fiber with a 40GBASE-SR4 transceiver",
                "correct": True,
                "rationale": "Correct. OM4 multimode fiber supports 40GBASE-SR4 up to 150 m, easily covering 80 m. It is less expensive than single-mode and well-suited to intra-data-center distances.",
            },
            {
                "id": "b",
                "text": "Cat 6a UTP copper",
                "correct": False,
                "rationale": "Incorrect. Cat 6a supports 10 Gbps at up to 100 m but does not support 40 Gbps natively; 40 Gbps Ethernet over copper (40GBASE-T) requires Cat 8 and is limited to ~30 m.",
            },
            {
                "id": "c",
                "text": "Single-mode fiber with a 40GBASE-LR4 transceiver",
                "correct": False,
                "rationale": "Incorrect. 40GBASE-LR4 on single-mode reaches 10 km — far more than needed for 80 m. It works but is significantly more expensive than OM4 multimode for this short distance.",
            },
            {
                "id": "d",
                "text": "Coaxial cable with a direct-attach connector",
                "correct": False,
                "rationale": "Incorrect. Coaxial cable is not used for 40 Gbps Ethernet switch interconnects; direct-attach copper (DAC) twinax cables can reach ~5 m, not 80 m.",
            },
        ],
        "explanation": (
            "For short data-center runs (up to ~150 m), OM4 multimode with SR (short-range) "
            "transceivers is the cost-effective choice. Single-mode fiber is reserved for longer "
            "runs. Direct-attach copper (DAC/TwinAx) is cheaper still but limited to ~7 m. "
            "Cat 6a/8 copper tops out at 10 Gbps or short-reach 40GBASE-T."
        ),
    },
    {
        "id": "cd1v3-008",
        "domain": 1,
        "objective": "1.3",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Cabling & interfaces",
        "stem": (
            "An engineer terminates a new run of Cat 6 UTP using the T568B wiring standard "
            "on both ends. A laptop plugged into the jack cannot communicate with the switch. "
            "The switch port shows 'up/up' after the engineer uses a cable tester that "
            "reports 'pass — straight-through.' The laptop NIC link light is also on. "
            "Which additional factor should the engineer check FIRST?"
        ),
        "options": [
            {
                "id": "a",
                "text": "VLAN assignment on the switch port — the port may be in the wrong VLAN or shutdown at Layer 2/3",
                "correct": True,
                "rationale": "Correct. Physical connectivity (Layer 1) is confirmed by the link lights and cable tester. The next troubleshooting step is Layer 2: VLAN membership, port mode, or an access VLAN mismatch preventing communication.",
            },
            {
                "id": "b",
                "text": "Re-terminate the cable with T568A on one end to create a crossover",
                "correct": False,
                "rationale": "Incorrect. A laptop-to-switch connection is an unlike-device connection requiring a straight-through cable; T568B/T568B is correct (Auto-MDIX would handle crossover anyway). The cable tester already confirms continuity.",
            },
            {
                "id": "c",
                "text": "Replace the Cat 6 cable with Cat 6a for higher bandwidth",
                "correct": False,
                "rationale": "Incorrect. Cat 6 supports 1 Gbps at 100 m which is sufficient; the physical layer is already passing the cable test. This is a Layer 2/3 issue.",
            },
            {
                "id": "d",
                "text": "Check whether the cable exceeds 100 m, as longer runs cause signal attenuation",
                "correct": False,
                "rationale": "Incorrect. Both the link light and the cable tester pass indicate signal integrity is fine; attenuation is not the issue here.",
            },
        ],
        "explanation": (
            "Troubleshoot bottom-up: Layer 1 is confirmed (link lights up, cable tester pass). "
            "Move to Layer 2: verify the switch port is not shut, is in the correct VLAN, and "
            "the correct port mode (access/trunk). VLAN misconfiguration is a very common cause "
            "of failed communication on physically good links."
        ),
    },
    # --------------------------------------------------------- 1.4 Interface/cable troubleshooting
    {
        "id": "cd1v3-009",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Interface/cable troubleshooting",
        "stem": (
            "A 'show interfaces GigabitEthernet0/0' output shows: input errors 4821, "
            "CRC 4819, frame 2, runts 0, giants 0, output errors 0. The link is up/up. "
            "What is the MOST likely root cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A physical layer problem on the receive path — damaged cable, bad connector, or failing transceiver causing bit errors and CRC failures",
                "correct": True,
                "rationale": "Correct. High CRC and input errors on an up/up interface indicate bit corruption on the receive path. Common causes: damaged cable, dirty/bent fiber connector, failing transceiver, or EMI. Output errors being zero confirms the local transmit path is healthy.",
            },
            {
                "id": "b",
                "text": "A duplex mismatch causing late collisions on the half-duplex side",
                "correct": False,
                "rationale": "Incorrect. A duplex mismatch primarily manifests as late collisions (not CRC errors) on the half-duplex side. CRC errors dominate here, pointing to physical bit corruption rather than duplex issues.",
            },
            {
                "id": "c",
                "text": "An MTU mismatch causing giants to be dropped",
                "correct": False,
                "rationale": "Incorrect. Giants (oversized frames) would appear in the giant counter; it shows 0 here. MTU mismatches appear as giants or fragmentation, not primarily CRC errors.",
            },
            {
                "id": "d",
                "text": "High CPU utilization on the router causing output queue drops",
                "correct": False,
                "rationale": "Incorrect. CPU-related output drops appear as output errors or output drops; output errors are 0 here. The problem is on the input/receive side.",
            },
        ],
        "explanation": (
            "CRC errors on input = corrupted frames received. Since output errors are zero, the "
            "local transmitter is fine. Focus on the receive path: cable condition, connector "
            "cleanliness (fiber), transceiver health, or EMI on the link. Replace the cable or "
            "transceiver and retest."
        ),
    },
    {
        "id": "cd1v3-010",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Interface/cable troubleshooting",
        "stem": (
            "After replacing an SFP transceiver on a switch, 'show interfaces Gi1/0/1' shows "
            "'GigabitEthernet1/0/1 is administratively down, line protocol is down.' "
            "Pinging the neighboring router fails. What is the FIRST action to take?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Issue 'no shutdown' on the interface — it is administratively disabled",
                "correct": True,
                "rationale": "Correct. 'Administratively down' means a 'shutdown' command was applied (possibly to safely swap the SFP). Issue 'no shutdown' to bring it up before further troubleshooting.",
            },
            {
                "id": "b",
                "text": "Replace the SFP again — a new transceiver should never show administratively down",
                "correct": False,
                "rationale": "Incorrect. 'Administratively down' is a software state from a 'shutdown' command, unrelated to the SFP hardware. Replacing the SFP again wastes time.",
            },
            {
                "id": "c",
                "text": "Check the routing table for a missing default route",
                "correct": False,
                "rationale": "Incorrect. The interface is administratively down — there is no Layer 1 or Layer 2 link to carry any routing traffic. Fix the interface state first.",
            },
            {
                "id": "d",
                "text": "Verify the IP address configuration on the interface",
                "correct": False,
                "rationale": "Incorrect. IP configuration is irrelevant while the interface is administratively down; bring it up first, then verify addressing.",
            },
        ],
        "explanation": (
            "An 'administratively down' state means 'shutdown' is configured. It is common to "
            "shut a port before swapping SFPs. After replacement, 'no shutdown' must be issued. "
            "Always resolve the lowest OSI layer issue first before investigating higher layers."
        ),
    },
    {
        "id": "cd1v3-011",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Interface/cable troubleshooting",
        "stem": (
            "A switch port connected to an IP phone shows incrementing output drops and "
            "input errors. Which TWO actions would MOST likely address these symptoms? "
            "(Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Configure QoS queuing on the switch port to prioritize voice traffic and reduce output drops",
                "correct": True,
                "rationale": "Correct. Output drops indicate the transmit queue is full; configuring QoS (priority queuing for voice) ensures voice frames are dequeued first, reducing drops for time-sensitive traffic.",
            },
            {
                "id": "b",
                "text": "Replace or re-seat the cable to address physical layer bit errors causing input errors",
                "correct": True,
                "rationale": "Correct. Input errors (especially CRC) point to a physical problem on the receive path. Replacing or re-seating the cable eliminates connector or cable damage as a cause.",
            },
            {
                "id": "c",
                "text": "Upgrade to a higher-bandwidth WAN circuit to reduce congestion",
                "correct": False,
                "rationale": "Incorrect. The issue is on a local switch port to an IP phone, not a WAN circuit. Upgrading WAN bandwidth does not fix local switch port queue drops or physical errors.",
            },
            {
                "id": "d",
                "text": "Configure NAT overload on the switch to reduce address table entries",
                "correct": False,
                "rationale": "Incorrect. NAT is a Layer 3 address-translation feature and has no effect on switch port output queuing or physical-layer input errors.",
            },
        ],
        "explanation": (
            "Two separate issues: output drops = queuing congestion, addressed by QoS. Input "
            "errors = physical layer corruption, addressed by cable/connector inspection. "
            "Always treat Layer 1 problems independently from Layer 2/3 queuing problems."
        ),
    },
    # --------------------------------------------------------- 1.5 TCP vs UDP
    {
        "id": "cd1v3-012",
        "domain": 1,
        "objective": "1.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "TCP vs UDP",
        "stem": (
            "A network engineer captures a session and sees that after a burst of dropped "
            "segments the sender reduces its transmit rate then gradually increases it again "
            "in an additive manner. Which TCP mechanism is operating?"
        ),
        "options": [
            {
                "id": "a",
                "text": "TCP congestion control (slow start / congestion avoidance) — TCP interprets packet loss as congestion and cuts its congestion window, then grows it linearly",
                "correct": True,
                "rationale": "Correct. TCP congestion control: on detecting loss, TCP halves (or resets) the congestion window, then uses additive increase (one MSS per RTT in congestion avoidance) to probe for available bandwidth — the classic AIMD sawtooth behavior.",
            },
            {
                "id": "b",
                "text": "TCP flow control — the receiver's advertised window shrank to zero",
                "correct": False,
                "rationale": "Incorrect. Flow control is receiver-driven via the advertised window; it limits the sender based on receiver buffer space. Congestion control is sender-driven based on network conditions (loss/delay).",
            },
            {
                "id": "c",
                "text": "UDP retransmission — UDP resends datagrams when the network recovers",
                "correct": False,
                "rationale": "Incorrect. UDP has no retransmission or congestion control mechanisms; this behavior is uniquely TCP.",
            },
            {
                "id": "d",
                "text": "TCP Nagle algorithm — small segments are coalesced to reduce overhead",
                "correct": False,
                "rationale": "Incorrect. The Nagle algorithm buffers small outgoing segments to reduce overhead; it does not cause a rate-reduction response to packet loss.",
            },
        ],
        "explanation": (
            "TCP congestion control (e.g., CUBIC, Reno): on loss, multiplicative decrease "
            "(halve cwnd or reset to ssthresh); then additive increase (grow by 1 MSS/RTT). "
            "This AIMD behavior produces the 'sawtooth' bandwidth graph. Flow control, by "
            "contrast, uses the receive window advertised by the far end."
        ),
    },
    {
        "id": "cd1v3-013",
        "domain": 1,
        "objective": "1.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "TCP vs UDP",
        "stem": (
            "A network monitoring application uses SNMP to poll device MIB counters every "
            "60 seconds, sending a small request and expecting a single reply. Which "
            "transport is used, and why is this appropriate for polling traffic?"
        ),
        "options": [
            {
                "id": "a",
                "text": "UDP (port 161 for SNMP queries); the low overhead and stateless nature suit infrequent small requests where occasional loss is acceptable",
                "correct": True,
                "rationale": "Correct. SNMP GET/GETNEXT uses UDP port 161. UDP's lack of connection setup is efficient for short, infrequent polls; if a reply is lost, the NMS simply polls again at the next interval.",
            },
            {
                "id": "b",
                "text": "TCP (port 161); SNMP uses TCP to guarantee every poll response is delivered",
                "correct": False,
                "rationale": "Incorrect. Standard SNMPv1/v2c uses UDP port 161. Some SNMPv3 implementations can use TCP, but UDP is the default and the expected CCNA answer.",
            },
            {
                "id": "c",
                "text": "UDP (port 514); SNMP shares the syslog UDP port",
                "correct": False,
                "rationale": "Incorrect. UDP port 514 is syslog, not SNMP. SNMP polls use UDP port 161; traps use UDP port 162.",
            },
            {
                "id": "d",
                "text": "TCP (port 162); SNMP traps require guaranteed delivery via TCP",
                "correct": False,
                "rationale": "Incorrect. SNMP traps use UDP port 162 (not TCP, and not the poll port 161). TCP port 162 is not the standard.",
            },
        ],
        "explanation": (
            "SNMP port summary: UDP/161 = SNMP queries (GET, GETNEXT, GETBULK, SET); "
            "UDP/162 = SNMP traps/informs. UDP suits SNMP polling: lightweight, no "
            "per-query connection overhead. Missed polls can simply be retried next cycle."
        ),
    },
    {
        "id": "cd1v3-014",
        "domain": 1,
        "objective": "1.5",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "TCP vs UDP",
        "stem": (
            "An application opens a TCP connection to a web server on port 443. The client "
            "sends a FIN segment after downloading a file. Which sequence correctly "
            "describes a graceful TCP connection teardown?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Client FIN -> Server ACK -> Server FIN -> Client ACK (four-way teardown)",
                "correct": True,
                "rationale": "Correct. TCP teardown: initiator sends FIN; receiver ACKs; receiver then sends its own FIN when done; initiator ACKs. Each side closes independently, enabling half-close.",
            },
            {
                "id": "b",
                "text": "Client RST -> Server RST (immediate reset, both sides)",
                "correct": False,
                "rationale": "Incorrect. RST is an abrupt connection reset, not a graceful teardown. A graceful close uses FIN/ACK exchanges.",
            },
            {
                "id": "c",
                "text": "Client FIN-ACK -> Server FIN-ACK (two-way simultaneous close)",
                "correct": False,
                "rationale": "Incorrect. While simultaneous close is theoretically possible, the standard graceful teardown is the four-step FIN/ACK sequence, not a simultaneous two-step exchange.",
            },
            {
                "id": "d",
                "text": "Client SYN -> Server SYN-ACK -> Client ACK -> Client FIN (teardown begins during handshake)",
                "correct": False,
                "rationale": "Incorrect. SYN/SYN-ACK/ACK is connection establishment, not teardown. Teardown begins after data transfer, using FIN segments.",
            },
        ],
        "explanation": (
            "TCP graceful teardown (four-way): FIN from initiator, ACK from receiver, "
            "FIN from receiver (when its send buffer is empty), final ACK from initiator. "
            "TIME_WAIT state follows to handle any delayed segments. RST provides an abrupt "
            "close without this handshake."
        ),
    },
    # --------------------------------------------------------- 1.6 IPv4 subnetting
    {
        "id": "cd1v3-015",
        "domain": 1,
        "objective": "1.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "IPv4 subnetting",
        "stem": (
            "A host has IP address 192.168.100.130 with subnet mask 255.255.255.128. "
            "What are the network address, broadcast address, and number of usable hosts?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Network 192.168.100.128, broadcast 192.168.100.255, 126 usable hosts",
                "correct": True,
                "rationale": "Correct. Mask 255.255.255.128 = /25, block size 128. Subnets: .0 and .128. Address .130 is in the .128 subnet. Network .128, broadcast .255, usable .129-.254 = 126 hosts (2^7 - 2).",
            },
            {
                "id": "b",
                "text": "Network 192.168.100.0, broadcast 192.168.100.127, 126 usable hosts",
                "correct": False,
                "rationale": "Incorrect. The .0/25 subnet covers .0-.127; address .130 is above .127 and falls in the second subnet (.128-.255), not the first.",
            },
            {
                "id": "c",
                "text": "Network 192.168.100.128, broadcast 192.168.100.191, 62 usable hosts",
                "correct": False,
                "rationale": "Incorrect. Broadcast .191 would indicate a /26 (block 64); the mask here is /25 (block 128), giving broadcast .255.",
            },
            {
                "id": "d",
                "text": "Network 192.168.100.128, broadcast 192.168.100.255, 254 usable hosts",
                "correct": False,
                "rationale": "Incorrect. 254 usable hosts belongs to a /24; a /25 provides only 126 usable hosts.",
            },
        ],
        "explanation": (
            "/25 (255.255.255.128): block size = 256 - 128 = 128. Two subnets per /24: .0/25 "
            "(.0-.127) and .128/25 (.128-.255). Address .130 is in .128/25. Network .128, "
            "broadcast .255, usable .129-.254 = 126 hosts."
        ),
    },
    {
        "id": "cd1v3-016",
        "domain": 1,
        "objective": "1.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "IPv4 subnetting",
        "stem": (
            "An ISP assigns a customer the block 203.0.113.64/28. How many usable host "
            "addresses are available, and what is the broadcast address?"
        ),
        "options": [
            {
                "id": "a",
                "text": "14 usable hosts; broadcast 203.0.113.79",
                "correct": True,
                "rationale": "Correct. /28 = block 16 (256-240). The subnet starting at .64 spans .64-.79. Network .64, broadcast .79, usable .65-.78 = 14 hosts (2^4 - 2).",
            },
            {
                "id": "b",
                "text": "14 usable hosts; broadcast 203.0.113.95",
                "correct": False,
                "rationale": "Incorrect. .95 would be the broadcast of the NEXT /28 block starting at .80; the .64/28 subnet ends at .79.",
            },
            {
                "id": "c",
                "text": "30 usable hosts; broadcast 203.0.113.95",
                "correct": False,
                "rationale": "Incorrect. 30 usable hosts and a .95 broadcast match a /27 (block 32) starting at .64, not a /28.",
            },
            {
                "id": "d",
                "text": "16 usable hosts; broadcast 203.0.113.79",
                "correct": False,
                "rationale": "Incorrect. 16 is the total address count including network and broadcast; usable is 16 - 2 = 14.",
            },
        ],
        "explanation": (
            "/28: 4 host bits, block 16. Network .64, addresses .64-.79, broadcast .79. "
            "Usable = 2^4 - 2 = 14. Always subtract 2 (network + broadcast) from total "
            "block size to get usable host count."
        ),
    },
    {
        "id": "cd1v3-017",
        "domain": 1,
        "objective": "1.6",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "IPv4 subnetting",
        "stem": (
            "Using VLSM on 10.0.0.0/8, you must allocate subnets for: LAN-A (500 hosts), "
            "LAN-B (100 hosts), LAN-C (50 hosts), and one point-to-point WAN link. "
            "Starting from 10.0.0.0 and allocating largest-first, what prefix is assigned "
            "to LAN-B (the second allocation)?"
        ),
        "options": [
            {
                "id": "a",
                "text": "10.0.2.0/25",
                "correct": True,
                "rationale": "Correct. LAN-A (500 hosts) needs 9 host bits: /23 (510 usable). First allocation: 10.0.0.0/23 (.0.0-.1.255). LAN-B (100 hosts) needs 7 host bits: /25 (126 usable). Next available block aligned to /25 boundary after 10.0.0.0/23 is 10.0.2.0/25.",
            },
            {
                "id": "b",
                "text": "10.0.2.0/24",
                "correct": False,
                "rationale": "Incorrect. /24 gives 254 usable hosts — more than needed for 100 hosts; /25 (126) is the smallest mask meeting the requirement, conserving address space per VLSM principles.",
            },
            {
                "id": "c",
                "text": "10.0.0.0/25",
                "correct": False,
                "rationale": "Incorrect. 10.0.0.0/25 overlaps with the first allocation (10.0.0.0/23). VLSM allocations must not overlap.",
            },
            {
                "id": "d",
                "text": "10.0.2.0/26",
                "correct": False,
                "rationale": "Incorrect. /26 provides only 62 usable hosts, insufficient for 100 hosts.",
            },
        ],
        "explanation": (
            "VLSM largest-first: LAN-A 500 hosts -> /23 (2^9-2=510) -> 10.0.0.0/23 occupies "
            ".0.0-.1.255. LAN-B 100 hosts -> /25 (2^7-2=126) -> next aligned /25 block is "
            "10.0.2.0/25 (.2.0-.2.127). Always pick smallest sufficient mask and start from "
            "the next available aligned address."
        ),
    },
    {
        "id": "cd1v3-018",
        "domain": 1,
        "objective": "1.6",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "IPv4 subnetting",
        "stem": (
            "Which single summary route most efficiently aggregates 172.16.8.0/24, "
            "172.16.9.0/24, 172.16.10.0/24, and 172.16.11.0/24, covering exactly "
            "those four networks?"
        ),
        "options": [
            {
                "id": "a",
                "text": "172.16.8.0/22",
                "correct": True,
                "rationale": "Correct. The third octet values 8-11 span 4 (/24s). Block size 4 in the third octet = /22. 172.16.8.0/22 covers 172.16.8.0-172.16.11.255 — exactly the four networks.",
            },
            {
                "id": "b",
                "text": "172.16.8.0/23",
                "correct": False,
                "rationale": "Incorrect. /23 block size 2 covers .8 and .9 only (172.16.8.0-172.16.9.255); it misses .10 and .11.",
            },
            {
                "id": "c",
                "text": "172.16.8.0/21",
                "correct": False,
                "rationale": "Incorrect. /21 block size 8 covers .8-.15 (eight /24s), including .12-.15 beyond the desired four.",
            },
            {
                "id": "d",
                "text": "172.16.0.0/20",
                "correct": False,
                "rationale": "Incorrect. /20 block size 16 in the third octet covers .0-.15 (sixteen /24s) — far too broad.",
            },
        ],
        "explanation": (
            "Summarization: find the common bits. Third octet: 8=00001000, 9=00001001, "
            "10=00001010, 11=00001011. Common prefix: 000010xx = 22 bits total. "
            "172.16.8.0/22 exactly covers .8-.11."
        ),
    },
    {
        "id": "cd1v3-019",
        "domain": 1,
        "objective": "1.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "IPv4 subnetting",
        "stem": (
            "An engineer is given 192.168.50.0/24 and must create exactly 8 equal subnets. "
            "Which mask must be used, and how many usable hosts does each subnet support?"
        ),
        "options": [
            {
                "id": "a",
                "text": "/27 (255.255.255.224); 30 usable hosts per subnet",
                "correct": True,
                "rationale": "Correct. To create 8 subnets from a /24 you need 3 subnet bits (2^3=8). /24 + 3 = /27 (block 32). Each /27 has 5 host bits: 2^5 - 2 = 30 usable hosts.",
            },
            {
                "id": "b",
                "text": "/26 (255.255.255.192); 62 usable hosts per subnet",
                "correct": False,
                "rationale": "Incorrect. /26 uses 2 subnet bits (2^2=4 subnets), producing only 4 subnets, not 8.",
            },
            {
                "id": "c",
                "text": "/28 (255.255.255.240); 14 usable hosts per subnet",
                "correct": False,
                "rationale": "Incorrect. /28 uses 4 subnet bits giving 16 subnets, not exactly 8 (though it would work if 'at least 8' was the requirement; the question says exactly 8).",
            },
            {
                "id": "d",
                "text": "/27 (255.255.255.224); 32 usable hosts per subnet",
                "correct": False,
                "rationale": "Incorrect. A /27 block has 32 total addresses; subtract 2 (network + broadcast) = 30 usable, not 32.",
            },
        ],
        "explanation": (
            "Subnetting a /24 into 8 equal parts: 2^3 = 8 subnets -> borrow 3 bits -> "
            "/27 (mask 255.255.255.224, block 32). Host bits remaining = 5. "
            "Usable = 2^5 - 2 = 30. Subnets: .0, .32, .64, .96, .128, .160, .192, .224."
        ),
    },
    {
        "id": "cd1v3-020",
        "domain": 1,
        "objective": "1.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "IPv4 subnetting",
        "stem": (
            "Two hosts — 10.1.1.50/27 and 10.1.1.70/27 — need to communicate without "
            "routing. Are they on the same subnet?"
        ),
        "options": [
            {
                "id": "a",
                "text": "No; .50 is in the 10.1.1.32/27 subnet and .70 is in the 10.1.1.64/27 subnet",
                "correct": True,
                "rationale": "Correct. /27 block size = 32. Subnets: .0, .32, .64, .96... .50 falls in .32-.63 (subnet .32); .70 falls in .64-.95 (subnet .64). They are in different subnets and cannot communicate without a router.",
            },
            {
                "id": "b",
                "text": "Yes; both are in the 10.1.1.0/27 subnet",
                "correct": False,
                "rationale": "Incorrect. The .0/27 subnet covers .0-.31; .50 and .70 are both beyond .31.",
            },
            {
                "id": "c",
                "text": "Yes; both are in the 10.1.1.64/27 subnet",
                "correct": False,
                "rationale": "Incorrect. .64/27 covers .64-.95; .50 is in .32-.63 (the .32 subnet), not .64-.95.",
            },
            {
                "id": "d",
                "text": "Yes; both have the same /27 mask so they are always on the same subnet",
                "correct": False,
                "rationale": "Incorrect. The same mask does not imply the same subnet; the network address is determined by ANDing the IP with the mask. Different IPs with the same mask can be in different subnets.",
            },
        ],
        "explanation": (
            "/27, block 32: subnets .0/27 (.0-.31), .32/27 (.32-.63), .64/27 (.64-.95), "
            ".96/27 (.96-.127)... .50 AND 255.255.255.224 = .32 (subnet .32/27). "
            ".70 AND 255.255.255.224 = .64 (subnet .64/27). Different subnets; routing required."
        ),
    },
    # --------------------------------------------------------- 1.7 Private addressing & NAT
    {
        "id": "cd1v3-021",
        "domain": 1,
        "objective": "1.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Private addressing & NAT",
        "stem": (
            "A company uses PAT (NAT overload) to allow 200 internal hosts to share a "
            "single public IP address. Which field in the translated packet uniquely "
            "identifies each internal session?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The source TCP/UDP port number in the translated packet",
                "correct": True,
                "rationale": "Correct. PAT maps each internal host:port pair to the same public IP but a unique source port. The port number (Layer 4) is the distinguishing factor, allowing one IP to multiplex hundreds of simultaneous sessions.",
            },
            {
                "id": "b",
                "text": "The TTL value in the IP header",
                "correct": False,
                "rationale": "Incorrect. TTL decrements at each hop and is not used by PAT to distinguish sessions; it is a routing/loop-prevention field.",
            },
            {
                "id": "c",
                "text": "The destination IP address",
                "correct": False,
                "rationale": "Incorrect. Multiple hosts may reach the same destination; the destination IP alone cannot distinguish between sessions from different internal hosts to the same server.",
            },
            {
                "id": "d",
                "text": "The VLAN tag in the Ethernet frame",
                "correct": False,
                "rationale": "Incorrect. VLAN tags are Layer 2 and are stripped before the packet enters the internet. PAT operates at Layer 3/4 and uses port numbers.",
            },
        ],
        "explanation": (
            "PAT (NAT overload): source IP -> public IP, source port -> unique translated port. "
            "The NAT table maps (private IP:port) <-> (public IP:translated_port). Up to ~65,000 "
            "simultaneous sessions per public IP. The Layer 4 source port is the multiplexing key."
        ),
    },
    {
        "id": "cd1v3-022",
        "domain": 1,
        "objective": "1.7",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Private addressing & NAT",
        "stem": (
            "Which TWO are true about the 192.168.0.0/16 address space? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "It is defined as private by RFC 1918 and not routable on the public internet",
                "correct": True,
                "rationale": "Correct. 192.168.0.0/16 is one of three RFC 1918 private ranges; ISPs filter it from the public internet.",
            },
            {
                "id": "b",
                "text": "It spans addresses 192.168.0.0 through 192.168.255.255",
                "correct": True,
                "rationale": "Correct. 192.168.0.0/16 covers all addresses with the first two octets 192.168, i.e., 192.168.0.0-192.168.255.255.",
            },
            {
                "id": "c",
                "text": "It is routable by default between ISPs as a legacy allocation",
                "correct": False,
                "rationale": "Incorrect. RFC 1918 addresses are explicitly non-routable on the public internet; ISPs drop packets sourced from or destined to these ranges.",
            },
            {
                "id": "d",
                "text": "It includes 192.168.256.0 as a valid subnet",
                "correct": False,
                "rationale": "Incorrect. Octets are 0-255; 256 is invalid. 192.168.0.0/16 ends at 192.168.255.255.",
            },
        ],
        "explanation": (
            "RFC 1918 defines three private ranges: 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16. "
            "The 192.168/16 block spans .0.0-.255.255 and is commonly used in SOHO and enterprise "
            "LANs. All are non-routable on the public internet without NAT."
        ),
    },
    {
        "id": "cd1v3-023",
        "domain": 1,
        "objective": "1.7",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Private addressing & NAT",
        "stem": (
            "A router's NAT table shows an entry mapping inside local 10.1.1.5:1500 to "
            "inside global 203.0.113.10:2100. A return packet arrives at the router with "
            "destination 203.0.113.10:2100. What does the router do with it?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Translates the destination to 10.1.1.5:1500 and forwards it to the inside host",
                "correct": True,
                "rationale": "Correct. The NAT table maps (inside global 203.0.113.10:2100) back to (inside local 10.1.1.5:1500). The router rewrites the destination IP:port and forwards the packet inside.",
            },
            {
                "id": "b",
                "text": "Drops the packet because it is destined for the router's own public IP",
                "correct": False,
                "rationale": "Incorrect. The router checks the NAT table before deciding to deliver locally or translate; a matching NAT entry triggers translation, not a drop.",
            },
            {
                "id": "c",
                "text": "Forwards the packet as-is to 10.1.1.5 without changing the destination port",
                "correct": False,
                "rationale": "Incorrect. PAT translates both IP and port; the destination is rewritten to the inside local address AND original port number.",
            },
            {
                "id": "d",
                "text": "Sends an ICMP unreachable message because 203.0.113.10 is the outside interface",
                "correct": False,
                "rationale": "Incorrect. The router does not send an ICMP unreachable for a packet matching a NAT entry on its outside interface; it performs the reverse translation.",
            },
        ],
        "explanation": (
            "PAT reverse translation: inbound packet to (outside IP:port) matches the NAT table "
            "entry; router rewrites destination to (inside local IP:original port) and routes it "
            "to the internal host. This is the 'inside global -> inside local' translation."
        ),
    },
    # --------------------------------------------------------- 1.8 IPv6 addressing
    {
        "id": "cd1v3-024",
        "domain": 1,
        "objective": "1.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "IPv6 addressing",
        "stem": (
            "Which is the correct fully compressed form of "
            "FE80:0000:0000:0000:020C:29FF:FE7A:1B3D?"
        ),
        "options": [
            {
                "id": "a",
                "text": "FE80::20C:29FF:FE7A:1B3D",
                "correct": True,
                "rationale": "Correct. The three all-zero hextets after FE80 are replaced by '::'; leading zeros in 020C are dropped to 20C, giving FE80::20C:29FF:FE7A:1B3D.",
            },
            {
                "id": "b",
                "text": "FE80:0:0:0:20C:29FF:FE7A:1B3D",
                "correct": False,
                "rationale": "Incorrect. This drops leading zeros per hextet but does not apply '::' compression to the consecutive zero hextets — not fully compressed.",
            },
            {
                "id": "c",
                "text": "FE80::020C:29FF:FE7A:1B3D",
                "correct": False,
                "rationale": "Incorrect. Leading zeros within 020C must be dropped to 20C; this form retains the leading zero and is not fully compressed.",
            },
            {
                "id": "d",
                "text": "FE80::20C:29FF::1B3D",
                "correct": False,
                "rationale": "Incorrect. '::' appears twice, which is invalid — '::' may only be used once in an IPv6 address.",
            },
        ],
        "explanation": (
            "Two IPv6 compression rules applied together: "
            "(1) remove leading zeros in each hextet; "
            "(2) replace one contiguous group of all-zero hextets with '::'. "
            "FE80:0000:0000:0000:020C:29FF:FE7A:1B3D -> FE80::20C:29FF:FE7A:1B3D."
        ),
    },
    {
        "id": "cd1v3-025",
        "domain": 1,
        "objective": "1.8",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "IPv6 addressing",
        "stem": (
            "How many IPv6 addresses does a /64 prefix provide, and why is /64 the "
            "standard boundary for host subnets?"
        ),
        "options": [
            {
                "id": "a",
                "text": "2^64 addresses (~1.8 × 10^19); /64 is standard so the lower 64 bits can hold EUI-64 interface IDs and SLAAC works without manual configuration",
                "correct": True,
                "rationale": "Correct. A /64 leaves 64 bits for the interface ID. This is required for SLAAC (Stateless Address Autoconfiguration) using EUI-64, which generates the interface ID from the MAC. 2^64 ≈ 1.8 × 10^19 addresses per subnet.",
            },
            {
                "id": "b",
                "text": "2^32 addresses; /64 provides the same count as the entire IPv4 address space",
                "correct": False,
                "rationale": "Incorrect. 2^32 is the IPv4 address space; a /64 prefix has 2^64 host addresses, vastly larger.",
            },
            {
                "id": "c",
                "text": "128 addresses; /64 means 64 host bits giving 128 addresses",
                "correct": False,
                "rationale": "Incorrect. /64 means 64 host bits remain, providing 2^64 (not 64 or 128) addresses.",
            },
            {
                "id": "d",
                "text": "2^64 addresses; /64 is used because it is the maximum IPv6 subnet size",
                "correct": False,
                "rationale": "Incorrect. /64 is not the maximum — prefixes can be shorter (e.g., /48, /32). /64 is standard for host subnets specifically because it accommodates EUI-64 SLAAC, not because it is the largest possible.",
            },
        ],
        "explanation": (
            "IPv6 uses /64 for host-facing subnets: the upper 64 bits identify the network "
            "(prefix), the lower 64 bits are the interface ID. SLAAC generates the interface "
            "ID via EUI-64 or random generation. With 2^64 ≈ 1.84 × 10^19 addresses per "
            "subnet, exhaustion is not a concern."
        ),
    },
    # --------------------------------------------------------- 1.9 IPv6 address types
    {
        "id": "cd1v3-026",
        "domain": 1,
        "objective": "1.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "IPv6 address types",
        "stem": (
            "An engineer assigns 2001:db8:cafe:1::1/64 to a router interface. What type "
            "of IPv6 address is this, and can it be routed across the public internet?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Global unicast address (2000::/3); yes, it is publicly routable on the internet",
                "correct": True,
                "rationale": "Correct. 2001:db8::/32 is a documentation prefix within the global unicast range (2000::/3). In production, addresses in 2000::/3 are globally routable. (2001:db8:: specifically is documentation-only by RFC 3849 — but the address type and routing property question is answered correctly.)",
            },
            {
                "id": "b",
                "text": "Unique local address (fc00::/7); it is private and not routable on the internet",
                "correct": False,
                "rationale": "Incorrect. Unique local addresses start with fc00::/7 (fd00:: range); 2001:: falls within 2000::/3 global unicast.",
            },
            {
                "id": "c",
                "text": "Link-local address (fe80::/10); only valid on the local link",
                "correct": False,
                "rationale": "Incorrect. Link-local addresses begin with fe80::/10; 2001:: is a global unicast prefix.",
            },
            {
                "id": "d",
                "text": "Anycast address; it is shared among multiple interfaces",
                "correct": False,
                "rationale": "Incorrect. Anycast addresses are drawn from the unicast space and assigned identically to multiple interfaces; an address is not inherently anycast based on its prefix alone.",
            },
        ],
        "explanation": (
            "IPv6 address type identification by prefix: 2000::/3 = global unicast (publicly "
            "routable); fc00::/7 = unique local (private); fe80::/10 = link-local; ff00::/8 = "
            "multicast. 2001:db8::/32 is the documentation sub-range of global unicast."
        ),
    },
    {
        "id": "cd1v3-027",
        "domain": 1,
        "objective": "1.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "IPv6 address types",
        "stem": (
            "A host sends a Neighbor Solicitation (NS) message to resolve the MAC address "
            "of another host on the same link. To which special IPv6 address does it send "
            "the NS, and how is that address derived?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The solicited-node multicast address ff02::1:ff<last 24 bits of target IP>; derived from the last 24 bits of the target's IPv6 address",
                "correct": True,
                "rationale": "Correct. NDP Neighbor Solicitation is sent to the solicited-node multicast address, formed by appending the last 24 bits of the target's IPv6 address to ff02::1:ff00::/104. This limits NS to a small group of nodes, unlike ARP's broadcast.",
            },
            {
                "id": "b",
                "text": "ff02::2 (all routers); the default router resolves all addresses",
                "correct": False,
                "rationale": "Incorrect. ff02::2 is the all-routers multicast address; Neighbor Solicitation for address resolution uses the solicited-node multicast address, not ff02::2.",
            },
            {
                "id": "c",
                "text": "ff02::1 (all nodes); NDP broadcasts to everyone like ARP",
                "correct": False,
                "rationale": "Incorrect. IPv6 does not use broadcast; NDP uses solicited-node multicast which targets only nodes sharing the same last 24 bits — far more efficient than all-nodes.",
            },
            {
                "id": "d",
                "text": "The target's link-local address directly; NDP skips multicast for unicast targets",
                "correct": False,
                "rationale": "Incorrect. The link-local address is exactly what is being resolved; sending to it would require already knowing what NDP is trying to discover. NS uses solicited-node multicast.",
            },
        ],
        "explanation": (
            "NDP replaces ARP using solicited-node multicast: ff02::1:ff + last 24 bits of "
            "target address. Only hosts sharing those 24 bits join that group, making NS "
            "much more targeted than IPv4 ARP broadcast. Neighbor Advertisement (NA) is "
            "the reply carrying the MAC."
        ),
    },
    {
        "id": "cd1v3-028",
        "domain": 1,
        "objective": "1.9",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "IPv6 address types",
        "stem": (
            "A host is configured with fd00:acad:1:1::50/64. What type of IPv6 address "
            "is this, and what is its intended use?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Unique local address; for use within a private organization's network, not routable on the public internet",
                "correct": True,
                "rationale": "Correct. fd00::/8 falls within fc00::/7 (unique local). The 'fd' prefix (1111 1101) indicates a locally assigned unique local address, the IPv6 equivalent of RFC 1918 private addressing.",
            },
            {
                "id": "b",
                "text": "Global unicast address; routable on the public internet",
                "correct": False,
                "rationale": "Incorrect. fd00:: begins with 1111 1101 binary — it falls in the fc00::/7 unique local range, not 2000::/3 global unicast.",
            },
            {
                "id": "c",
                "text": "Link-local address; only valid on the attached network segment",
                "correct": False,
                "rationale": "Incorrect. Link-local addresses start with fe80::/10. fd00:: is unique local, which has site-wide (not just link-local) scope.",
            },
            {
                "id": "d",
                "text": "Anycast address; assigned to multiple interfaces for load balancing",
                "correct": False,
                "rationale": "Incorrect. fd00:: is unique local unicast; anycast is a function assigned from the unicast space and identified by how it is configured, not by prefix alone.",
            },
        ],
        "explanation": (
            "IPv6 unique local (fc00::/7): fc00::/8 centrally assigned (rarely used), "
            "fd00::/8 locally defined (most common). They are the private/RFC-1918 "
            "equivalent in IPv6: site-scoped, not globally routable. Unlike RFC 1918, "
            "they are typically globally unique due to a random 40-bit global ID."
        ),
    },
    {
        "id": "cd1v3-029",
        "domain": 1,
        "objective": "1.9",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "IPv6 address types",
        "stem": (
            "Which TWO statements accurately describe IPv6 SLAAC "
            "(Stateless Address Autoconfiguration)? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "A host generates its interface ID from a modified EUI-64 of its MAC or using a random value, then combines it with the /64 prefix advertised in the Router Advertisement",
                "correct": True,
                "rationale": "Correct. SLAAC: host learns the /64 prefix from the RA, generates an interface ID (EUI-64 or RFC 7217 stable/random), and combines them to form a /128 global unicast address.",
            },
            {
                "id": "b",
                "text": "No DHCP server is required; the host configures its IP address automatically from RA information",
                "correct": True,
                "rationale": "Correct. SLAAC is 'stateless' — no DHCPv6 server assigns or tracks addresses. The router's RA provides the prefix, and the host self-generates the full address.",
            },
            {
                "id": "c",
                "text": "SLAAC assigns a /128 prefix to the host and requires manual DNS configuration",
                "correct": False,
                "rationale": "Incorrect. The router advertises a /64 prefix (not /128); the host self-assigns a /128 address from it. DNS can be provided via RDNSS option in the RA (RFC 8106) without DHCPv6.",
            },
            {
                "id": "d",
                "text": "SLAAC requires a stateful DHCPv6 server to track all assigned addresses",
                "correct": False,
                "rationale": "Incorrect. SLAAC is explicitly stateless — no server tracks address assignments. Stateful DHCPv6 is a separate mechanism used when centralized address management is needed.",
            },
        ],
        "explanation": (
            "SLAAC (RFC 4862): router sends RA with the /64 prefix (triggered by RS or "
            "periodically). Host generates interface ID (EUI-64 or random) and forms a "
            "full /128 address. No server involvement — hence 'stateless.' DNS info can "
            "come from RA RDNSS options or separate stateless DHCPv6."
        ),
    },
    # --------------------------------------------------------- 1.10 Client IP verification
    {
        "id": "cd1v3-030",
        "domain": 1,
        "objective": "1.10",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Client IP verification",
        "stem": (
            "A Windows 10 PC obtains IP 10.0.1.100/24, gateway 10.0.1.1. The user can "
            "ping 10.0.1.1 but cannot reach 8.8.8.8 or any website. Which command run "
            "on the PC would BEST distinguish between a routing problem and a DNS problem?"
        ),
        "options": [
            {
                "id": "a",
                "text": "ping 8.8.8.8 — if this succeeds but browsing fails, DNS is the problem; if it also fails, routing/firewall is the issue",
                "correct": True,
                "rationale": "Correct. Pinging 8.8.8.8 by IP bypasses DNS entirely. If it succeeds, IP connectivity is fine and DNS is the fault. If it fails, the issue is routing, firewall, or the path to the internet — not DNS.",
            },
            {
                "id": "b",
                "text": "ipconfig /release — releases the IP to check whether DHCP is responding",
                "correct": False,
                "rationale": "Incorrect. The host already has correct IP/gateway and can reach the gateway, so DHCP is not the issue. Releasing the address breaks connectivity further without diagnosing routing vs. DNS.",
            },
            {
                "id": "c",
                "text": "tracert 10.0.1.1 — traces the path to the default gateway",
                "correct": False,
                "rationale": "Incorrect. The user can already ping the gateway; tracing to it confirms what is already known. The problem is beyond the gateway.",
            },
            {
                "id": "d",
                "text": "netstat -an — shows all active connections and listening ports",
                "correct": False,
                "rationale": "Incorrect. netstat shows socket state but does not distinguish between a routing failure and a DNS failure for external connectivity.",
            },
        ],
        "explanation": (
            "Layer-by-layer isolation: ping by IP = test Layer 3 connectivity without DNS. "
            "If 'ping 8.8.8.8' works, DNS is broken. If it fails, routing/firewall is the "
            "issue. This single test cleanly splits the two most common causes of 'internet "
            "down' complaints on a PC with a valid IP and gateway."
        ),
    },
    {
        "id": "cd1v3-031",
        "domain": 1,
        "objective": "1.10",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Client IP verification",
        "stem": (
            "A macOS laptop shows IP address 10.0.0.50, subnet mask 255.255.255.0, and "
            "router (default gateway) 10.0.0.1 in System Preferences. Which CLI command "
            "on macOS would show the same information from the terminal?"
        ),
        "options": [
            {
                "id": "a",
                "text": "ifconfig en0",
                "correct": True,
                "rationale": "Correct. macOS uses 'ifconfig' (or 'ifconfig en0' for the primary Ethernet/Wi-Fi interface) to display interface IP addresses, subnet masks, and MAC addresses. 'netstat -rn' shows the routing table including the default gateway.",
            },
            {
                "id": "b",
                "text": "ipconfig /all",
                "correct": False,
                "rationale": "Incorrect. 'ipconfig /all' is a Windows command; it is not available on macOS.",
            },
            {
                "id": "c",
                "text": "show ip interface brief",
                "correct": False,
                "rationale": "Incorrect. That is Cisco IOS CLI syntax for routers and switches, not a macOS terminal command.",
            },
            {
                "id": "d",
                "text": "ip address show",
                "correct": False,
                "rationale": "Incorrect. 'ip address show' (from the iproute2 package) is a Linux command; macOS uses 'ifconfig' by default, not iproute2.",
            },
        ],
        "explanation": (
            "Per-OS IP verification commands: Windows = 'ipconfig /all'; Linux = 'ip addr show' "
            "or 'ifconfig'; macOS = 'ifconfig' or 'networksetup -getinfo <interface>'; "
            "Cisco IOS = 'show ip interface brief'. macOS and Linux both have 'ifconfig' "
            "but macOS does not have iproute2 by default."
        ),
    },
    # --------------------------------------------------------- 1.11 Wireless principles
    {
        "id": "cd1v3-032",
        "domain": 1,
        "objective": "1.11",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Wireless principles",
        "stem": (
            "An 802.11ac (Wi-Fi 5) AP supports 80 MHz channel bonding. A nearby AP on "
            "an overlapping channel causes co-channel interference. An engineer suggests "
            "moving to the 5 GHz band and using 20 MHz channels to maximize the number "
            "of non-overlapping channels. Which statement about 5 GHz is correct?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The 5 GHz band offers up to ~24 non-overlapping 20 MHz channels in North America (UNII-1, -2, -2e, -3), far more than 2.4 GHz",
                "correct": True,
                "rationale": "Correct. The 5 GHz band has many more non-overlapping 20 MHz channels (approximately 24 in North America with DFS channels included) compared to 2.4 GHz's 3. Using narrower channels maximizes co-existence of APs.",
            },
            {
                "id": "b",
                "text": "The 5 GHz band has exactly 3 non-overlapping channels, the same as 2.4 GHz",
                "correct": False,
                "rationale": "Incorrect. The 2.4 GHz band has 3 non-overlapping 20 MHz channels; 5 GHz has far more (up to ~24 non-overlapping 20 MHz channels in North America).",
            },
            {
                "id": "c",
                "text": "802.11ac requires 160 MHz channels and cannot use 20 MHz",
                "correct": False,
                "rationale": "Incorrect. 802.11ac (Wi-Fi 5) supports 20, 40, 80, and optional 160 MHz channel widths; 20 MHz is valid.",
            },
            {
                "id": "d",
                "text": "5 GHz provides greater range than 2.4 GHz due to lower frequency propagation",
                "correct": False,
                "rationale": "Incorrect. Higher frequency (5 GHz) has shorter range and more path loss through walls than lower frequency (2.4 GHz). 2.4 GHz propagates farther.",
            },
        ],
        "explanation": (
            "5 GHz advantages: many more non-overlapping channels (~24 at 20 MHz vs. 3 at "
            "2.4 GHz), less crowded, higher throughput. Disadvantage: shorter range, more "
            "attenuation through obstacles. 802.11ac (Wi-Fi 5) and 802.11ax (Wi-Fi 6) "
            "operate primarily in 5 GHz (Wi-Fi 6 also in 2.4 GHz)."
        ),
    },
    {
        "id": "cd1v3-033",
        "domain": 1,
        "objective": "1.11",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Wireless principles",
        "stem": (
            "A wireless client is roaming between two APs on the same WLC. The client "
            "moves from AP1 to AP2. Which statement about the roam is correct when both "
            "APs are managed by the same WLC (intra-controller roam)?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The client's IP address, session state, and security context are preserved by the WLC; the client does not need to re-authenticate or obtain a new IP",
                "correct": True,
                "rationale": "Correct. In an intra-controller roam the WLC maintains all client state. The client re-associates to AP2 but the WLC preserves IP address, VLAN, and security credentials — the roam is seamless.",
            },
            {
                "id": "b",
                "text": "The client must perform a full 802.1X re-authentication and DHCP request after associating to AP2",
                "correct": False,
                "rationale": "Incorrect. A full re-authentication is required only for inter-controller roams in certain configurations or when fast roaming (802.11r) is not in use with external AAA. Intra-controller roaming preserves state.",
            },
            {
                "id": "c",
                "text": "The two APs negotiate directly with each other to transfer the client session, bypassing the WLC",
                "correct": False,
                "rationale": "Incorrect. In a centralized (local mode) deployment, all client state is held at the WLC, not the APs. APs do not communicate client session state directly to each other.",
            },
            {
                "id": "d",
                "text": "Roaming between APs on the same WLC is not possible; clients must reconnect from scratch",
                "correct": False,
                "rationale": "Incorrect. Intra-controller roaming is seamless and is one of the key benefits of centralized WLC architecture.",
            },
        ],
        "explanation": (
            "Intra-controller roam (same WLC): WLC holds all session context. The client "
            "re-associates to the new AP; WLC updates the AP-to-client mapping and seamlessly "
            "continues the session. Inter-controller roaming requires mobility tunneling "
            "between WLCs (mobility group) for seamless handoff."
        ),
    },
    {
        "id": "cd1v3-034",
        "domain": 1,
        "objective": "1.11",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Wireless principles",
        "stem": (
            "Which 802.11 mechanism allows an AP to detect that two stations cannot hear "
            "each other, and what problem does it address?"
        ),
        "options": [
            {
                "id": "a",
                "text": "RTS/CTS (Request to Send / Clear to Send); it addresses the hidden node problem where two clients cannot detect each other's transmissions and collide at the AP",
                "correct": True,
                "rationale": "Correct. RTS/CTS: client sends RTS to AP; AP replies with CTS heard by all nearby stations, including those that cannot hear the original client. This reserves the medium and prevents hidden-node collisions.",
            },
            {
                "id": "b",
                "text": "CSMA/CA; it allows collisions to be detected after they occur and schedules retransmissions",
                "correct": False,
                "rationale": "Incorrect. CSMA/CA avoids collisions through backoff and carrier sensing, but cannot detect hidden nodes (which by definition cannot hear each other). RTS/CTS specifically addresses hidden nodes.",
            },
            {
                "id": "c",
                "text": "Beacon frames; the AP broadcasts its presence so all stations know the medium is busy",
                "correct": False,
                "rationale": "Incorrect. Beacons advertise the BSS (SSID, capabilities, timing); they do not reserve the medium for specific transmissions or address hidden nodes.",
            },
            {
                "id": "d",
                "text": "MIMO; multiple antennas allow the AP to hear both hidden nodes simultaneously",
                "correct": False,
                "rationale": "Incorrect. MIMO uses multiple antennas for spatial multiplexing and diversity gain; it does not resolve the hidden node problem, which is a MAC-layer issue.",
            },
        ],
        "explanation": (
            "Hidden node: Station A and Station C cannot hear each other but both reach AP B. "
            "Without RTS/CTS they may transmit simultaneously, colliding at the AP. "
            "RTS/CTS: A sends RTS to B; B's CTS reaches C; C defers. This virtual carrier "
            "sense (NAV) prevents the collision."
        ),
    },
    # --------------------------------------------------------- 1.12 Virtualization & containers
    {
        "id": "cd1v3-035",
        "domain": 1,
        "objective": "1.12",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Virtualization & containers",
        "stem": (
            "A cloud provider runs hundreds of VMs on a physical server. Suddenly one VM "
            "becomes unstable and consumes 100% CPU. Which hypervisor feature prevents "
            "this from starving other VMs of CPU resources?"
        ),
        "options": [
            {
                "id": "a",
                "text": "CPU resource reservations and limits configured on the hypervisor (e.g., vCPU shares/limits) isolate each VM's CPU consumption",
                "correct": True,
                "rationale": "Correct. Type 1 hypervisors (ESXi, Hyper-V, KVM) enforce CPU scheduling with shares, reservations, and limits per VM. A runaway VM hitting its CPU limit cannot consume resources beyond its allocation.",
            },
            {
                "id": "b",
                "text": "Containers on the same host are unaffected because they use a separate kernel",
                "correct": False,
                "rationale": "Incorrect. The question is about VMs; and containers share the host kernel — a runaway container can affect others without cgroup limits. This answer conflates VMs and containers.",
            },
            {
                "id": "c",
                "text": "The NIC teaming configuration limits network bandwidth, which indirectly reduces CPU usage",
                "correct": False,
                "rationale": "Incorrect. NIC teaming provides network redundancy and throughput; it does not directly limit compute CPU consumption of a runaway VM.",
            },
            {
                "id": "d",
                "text": "VLANs isolate the runaway VM's traffic so its CPU load does not affect other VMs",
                "correct": False,
                "rationale": "Incorrect. VLANs provide Layer 2 network segmentation; they have no effect on compute resource (CPU/memory) contention between VMs on the same physical host.",
            },
        ],
        "explanation": (
            "Hypervisor resource management: CPU shares determine relative priority; "
            "reservations guarantee a minimum; limits cap maximum consumption. These "
            "hypervisor scheduler controls prevent one VM's workload from starving others, "
            "ensuring isolation of compute resources."
        ),
    },
    {
        "id": "cd1v3-036",
        "domain": 1,
        "objective": "1.12",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Virtualization & containers",
        "stem": (
            "A network engineer must provision an isolated routing instance on a Cisco "
            "router for a new customer whose address space (10.0.0.0/8) overlaps with an "
            "existing customer. Adding the new customer's routes to the global routing "
            "table would cause conflicts. Which technology resolves this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "VRF (Virtual Routing and Forwarding); each customer gets its own routing table, enabling overlapping prefixes to coexist on one router",
                "correct": True,
                "rationale": "Correct. VRF creates isolated routing/forwarding instances per customer. Each VRF has its own RIB and FIB, so identical prefixes in different VRFs do not conflict.",
            },
            {
                "id": "b",
                "text": "NAT; translating each customer's addresses to unique public IPs prevents table conflicts",
                "correct": False,
                "rationale": "Incorrect. NAT translates addresses at the border but does not create separate routing tables; overlapping routes in the same table still conflict.",
            },
            {
                "id": "c",
                "text": "VLAN trunking; assigning each customer to a different VLAN resolves Layer 3 route conflicts",
                "correct": False,
                "rationale": "Incorrect. VLANs separate Layer 2 segments; without VRF, inter-VLAN routes still go into a single routing table, which does not resolve overlapping prefix conflicts.",
            },
            {
                "id": "d",
                "text": "Route summarization; aggregating each customer's routes removes duplicates",
                "correct": False,
                "rationale": "Incorrect. Route summarization reduces table size but cannot make overlapping, identical prefixes coexist for different customers in the same routing table.",
            },
        ],
        "explanation": (
            "VRF (Virtual Routing and Forwarding) is the solution for overlapping address "
            "spaces on shared infrastructure. Each VRF is a separate routing instance with "
            "its own routing and forwarding tables. MPLS VPN extends this across a service "
            "provider backbone using VRF-Lite on CE/PE routers."
        ),
    },
    {
        "id": "cd1v3-037",
        "domain": 1,
        "objective": "1.12",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Virtualization & containers",
        "stem": (
            "What is the primary difference between a Type 1 (bare-metal) hypervisor and "
            "a Type 2 (hosted) hypervisor?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A Type 1 hypervisor runs directly on hardware without a host OS, providing better performance and isolation; a Type 2 runs atop a host OS and relies on it for hardware access",
                "correct": True,
                "rationale": "Correct. Type 1 (bare-metal): VMware ESXi, Microsoft Hyper-V, KVM — installs directly on hardware, no host OS, lowest latency. Type 2 (hosted): VMware Workstation, VirtualBox — runs as an application on a host OS, higher overhead.",
            },
            {
                "id": "b",
                "text": "A Type 1 hypervisor can only run one VM at a time; Type 2 can run many",
                "correct": False,
                "rationale": "Incorrect. Type 1 is designed for dense multi-VM workloads in production; it is not limited to one VM. The distinction is the presence/absence of a host OS.",
            },
            {
                "id": "c",
                "text": "Type 2 is always faster because it uses the host OS drivers for hardware optimization",
                "correct": False,
                "rationale": "Incorrect. Type 2 is generally slower due to host OS overhead; Type 1 has direct hardware access and better performance.",
            },
            {
                "id": "d",
                "text": "Type 1 hypervisors require containers to run VMs; Type 2 runs VMs natively",
                "correct": False,
                "rationale": "Incorrect. Both types run VMs directly; containers are a separate virtualization paradigm and are not required by Type 1 hypervisors.",
            },
        ],
        "explanation": (
            "Type 1 (bare-metal): runs on hardware, manages resources directly — production "
            "data centers. Type 2 (hosted): runs on a general-purpose OS — developer workstations. "
            "Type 1 provides lower latency, better isolation, and scales to enterprise workloads; "
            "Type 2 is simpler to set up for lab/development use."
        ),
    },
    # --------------------------------------------------------- 1.13 Switching concepts / MAC table
    {
        "id": "cd1v3-038",
        "domain": 1,
        "objective": "1.13",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Switching concepts / MAC table",
        "stem": (
            "A switch receives thousands of frames per second with random source MAC "
            "addresses (a MAC flooding attack). What is the MOST likely consequence on "
            "an unprotected switch?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The MAC table overflows; the switch fails open and floods all frames out all ports like a hub, exposing traffic to all connected hosts",
                "correct": True,
                "rationale": "Correct. When the CAM/MAC table is full, the switch cannot learn new entries. Frames with unknown destinations (now all new MACs) are flooded everywhere — effectively turning the switch into a hub and enabling a sniffing attack.",
            },
            {
                "id": "b",
                "text": "The switch crashes and requires a reboot to clear the MAC table",
                "correct": False,
                "rationale": "Incorrect. Most switches do not crash from a full MAC table; they enter fail-open mode (flooding), continuing to forward but without per-destination intelligence.",
            },
            {
                "id": "c",
                "text": "The switch drops all traffic because it cannot verify source MACs",
                "correct": False,
                "rationale": "Incorrect. A switch in flooding mode does not drop traffic; it forwards frames out all ports. Dropping is not the default fail behavior.",
            },
            {
                "id": "d",
                "text": "Spanning Tree activates to block the attack ports automatically",
                "correct": False,
                "rationale": "Incorrect. STP responds to topology changes (BPDUs), not MAC flooding attacks. Port security (not STP) is the mitigation for CAM overflow attacks.",
            },
        ],
        "explanation": (
            "MAC flooding attack (e.g., macof tool): fills the CAM table with bogus entries; "
            "legitimate entries are evicted; switch floods all unicast frames — attacker "
            "can capture all traffic on shared segments. Mitigation: port security with "
            "'maximum MAC addresses' limit per port."
        ),
    },
    {
        "id": "cd1v3-039",
        "domain": 1,
        "objective": "1.13",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Switching concepts / MAC table",
        "stem": (
            "Exhibit: A switch has the following MAC table entry: "
            "VLAN 10, MAC 0050.7966.6800, Port Gi0/1, Type DYNAMIC. "
            "A frame arrives on Gi0/2 destined for 0050.7966.6800 in VLAN 10. "
            "What does the switch do?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Forwards the frame out Gi0/1 only (known unicast forwarding)",
                "correct": True,
                "rationale": "Correct. The destination MAC is in the MAC table mapped to Gi0/1 in VLAN 10. This is a known unicast: the switch forwards the frame out Gi0/1 only, without flooding.",
            },
            {
                "id": "b",
                "text": "Floods the frame out all ports in VLAN 10 except Gi0/2",
                "correct": False,
                "rationale": "Incorrect. Flooding occurs only for unknown destinations. This MAC is known (in the table), so the switch forwards to the specific port.",
            },
            {
                "id": "c",
                "text": "Drops the frame because the destination and source ports differ",
                "correct": False,
                "rationale": "Incorrect. Switches forward between different ports; that is their purpose. There is no rule dropping a frame because source and destination ports differ.",
            },
            {
                "id": "d",
                "text": "Forwards the frame out Gi0/2 back to the sender because the destination is on VLAN 10",
                "correct": False,
                "rationale": "Incorrect. A switch never forwards a frame back out the same port it arrived on; the destination MAC lookup points to Gi0/1, not back to Gi0/2.",
            },
        ],
        "explanation": (
            "Switch forwarding decision: look up destination MAC in CAM for the frame's VLAN. "
            "If found (known unicast), forward out the specific port. If not found, flood all "
            "ports in the VLAN except ingress. This example: destination known on Gi0/1, "
            "frame arrives on Gi0/2 — forward to Gi0/1 only."
        ),
    },
    {
        "id": "cd1v3-040",
        "domain": 1,
        "objective": "1.13",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Switching concepts / MAC table",
        "stem": (
            "An engineer types 'mac address-table static 00AA.BBCC.DD01 vlan 10 "
            "interface Gi0/3' on a Cisco switch. What is the effect and how does it "
            "differ from a dynamic entry?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The MAC is permanently mapped to Gi0/3 in VLAN 10; it will never age out and cannot be overwritten by a dynamically learned entry from a different port",
                "correct": True,
                "rationale": "Correct. Static MAC entries do not age out and cannot be overwritten by dynamic learning. They provide security and predictability for fixed devices like servers.",
            },
            {
                "id": "b",
                "text": "The entry ages out after 300 seconds like a dynamic entry",
                "correct": False,
                "rationale": "Incorrect. Static entries do not age out; 300-second aging applies only to dynamically learned entries.",
            },
            {
                "id": "c",
                "text": "The switch floods frames to 00AA.BBCC.DD01 out all ports because it distrusts static entries",
                "correct": False,
                "rationale": "Incorrect. Static entries are trusted and used for forwarding decisions; the switch forwards frames to the specified port, not flood them.",
            },
            {
                "id": "d",
                "text": "The command only takes effect after the switch is reloaded",
                "correct": False,
                "rationale": "Incorrect. Static MAC address table entries take effect immediately; no reload is required.",
            },
        ],
        "explanation": (
            "Static MAC entries: manually configured, permanent (survive aging), not overwritten "
            "by dynamic learning, survive reboots if saved in running-config. Dynamic entries: "
            "learned from source MACs, aged out after 300 s by default, can be overwritten "
            "if the device moves to another port."
        ),
    },
    # --------------------------------------------------------- Mixed / Additional
    {
        "id": "cd1v3-041",
        "domain": 1,
        "objective": "1.6",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "IPv4 subnetting",
        "stem": (
            "A host 172.31.255.200/20 — what is its subnet's network address and broadcast?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Network 172.31.240.0, broadcast 172.31.255.255",
                "correct": True,
                "rationale": "Correct. /20 in the third octet: mask 255.255.240.0, block size 16. Third-octet multiples of 16: 0, 16, 32, ..., 224, 240. .255 falls in the .240 block. Network 172.31.240.0, broadcast 172.31.255.255 (240 + 16 - 1 = 255 in third octet, all 1s in fourth).",
            },
            {
                "id": "b",
                "text": "Network 172.31.248.0, broadcast 172.31.255.255",
                "correct": False,
                "rationale": "Incorrect. .248 in the third octet would be the network address for a /21 (block 8). For /20 (block 16), .255 lands in the .240 block.",
            },
            {
                "id": "c",
                "text": "Network 172.31.255.0, broadcast 172.31.255.255",
                "correct": False,
                "rationale": "Incorrect. This would imply a /24 mask; the prefix is /20, so the block spans 16 values in the third octet — the network starts at .240, not .255.",
            },
            {
                "id": "d",
                "text": "Network 172.31.240.0, broadcast 172.31.240.255",
                "correct": False,
                "rationale": "Incorrect. A /20 block of 16 in the third octet spans .240.0 to .255.255, so the broadcast is .255.255, not .240.255.",
            },
        ],
        "explanation": (
            "/20 = 255.255.240.0. Block size in third octet = 256 - 240 = 16. "
            "Subnets: .0.0/20, .16.0/20, ..., .240.0/20, .256 (wraps). "
            "172.31.255.200: third octet 255 falls in the .240 block (240 <= 255 < 256). "
            "Network 172.31.240.0, broadcast 172.31.255.255."
        ),
    },
    {
        "id": "cd1v3-042",
        "domain": 1,
        "objective": "1.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "IPv6 address types",
        "stem": (
            "An IPv6 router receives a packet destined for FF02::9. What type of address "
            "is FF02::9, and what does the router do with the packet?"
        ),
        "options": [
            {
                "id": "a",
                "text": "FF02::9 is a link-local multicast address (RIPng all-routers); the router delivers it only to processes listening on that multicast group on the receiving interface",
                "correct": True,
                "rationale": "Correct. FF02::/16 is the link-local multicast scope. FF02::9 is the RIPng all-routers multicast group. The router delivers the packet to local processes subscribed to FF02::9; it does not forward it to other links.",
            },
            {
                "id": "b",
                "text": "FF02::9 is a global unicast address; the router forwards it toward the destination in the routing table",
                "correct": False,
                "rationale": "Incorrect. FF::anything is multicast (ff00::/8). Multicast scope FF02:: is link-local and is not forwarded by routers beyond the local link.",
            },
            {
                "id": "c",
                "text": "FF02::9 is an anycast address shared among all routers; it is forwarded to the nearest router",
                "correct": False,
                "rationale": "Incorrect. FF02:: is multicast, not anycast. Anycast addresses come from the unicast space; they are not identified by the FF prefix.",
            },
            {
                "id": "d",
                "text": "FF02::9 is a broadcast equivalent; it is delivered to every host on the internet",
                "correct": False,
                "rationale": "Incorrect. IPv6 has no broadcast. FF02::9 is link-local multicast, confined to the local link and delivered only to subscribing nodes.",
            },
        ],
        "explanation": (
            "IPv6 multicast well-known link-local groups (FF02::): ::1 all-nodes, ::2 all-routers, "
            "::5 OSPFv3 all-routers, ::6 OSPFv3 DRs, ::9 RIPng, ::a EIGRP, ::fb mDNS. "
            "Scope FF02 = link-local; packets are never forwarded beyond the link."
        ),
    },
    {
        "id": "cd1v3-043",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Network topologies",
        "stem": (
            "Which TWO characteristics apply to WAN topologies that use MPLS "
            "provider infrastructure? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Customer sites appear logically fully meshed even though each site connects to the provider with a single access link",
                "correct": True,
                "rationale": "Correct. MPLS/VPN creates a full logical mesh between all CE sites; any-to-any routing is handled by the provider's PE routers via MP-BGP and label-switched paths.",
            },
            {
                "id": "b",
                "text": "The service provider manages the core routing infrastructure; the customer manages only the CE router",
                "correct": True,
                "rationale": "Correct. In MPLS VPN the SP controls P and PE devices and the label-switching core; the customer is responsible only for the CE (customer edge) router and its configuration.",
            },
            {
                "id": "c",
                "text": "Each site must directly connect to every other site with a dedicated physical circuit",
                "correct": False,
                "rationale": "Incorrect. That describes a true physical full mesh. MPLS provides a logical full mesh over a shared provider infrastructure with only single access links per site.",
            },
            {
                "id": "d",
                "text": "MPLS eliminates all routing protocols; only switching by MAC addresses is used in the core",
                "correct": False,
                "rationale": "Incorrect. MPLS uses routing protocols (LDP, RSVP, MP-BGP) for label distribution and VRF routing; MAC-based forwarding is Layer 2 switching, not MPLS.",
            },
        ],
        "explanation": (
            "MPLS Layer 3 VPN: each CE connects to a PE via a single link. The SP core "
            "uses label switching (not customer IP routing) to forward packets. VRFs on PE "
            "routers separate customers. MP-BGP distributes VPN routes, creating a logical "
            "full mesh with only one access link per site."
        ),
    },
    {
        "id": "cd1v3-044",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Network components",
        "stem": (
            "Which TWO functions does a next-generation firewall (NGFW) provide that a "
            "traditional stateful firewall does NOT? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Application-layer (Layer 7) visibility and control — identifying and blocking specific apps regardless of port",
                "correct": True,
                "rationale": "Correct. NGFWs perform deep packet inspection to identify applications by behavior/signatures, not just port numbers, enabling policy at the application layer.",
            },
            {
                "id": "b",
                "text": "Integrated intrusion prevention system (IPS) inspecting traffic for exploit signatures",
                "correct": True,
                "rationale": "Correct. NGFWs integrate IPS engines to inspect packet payloads for known attack signatures, blocking exploits inline — traditional stateful firewalls only check state and ports.",
            },
            {
                "id": "c",
                "text": "Stateful packet inspection tracking TCP session state tables",
                "correct": False,
                "rationale": "Incorrect. Stateful inspection is a feature of traditional stateful firewalls as well; it is not exclusive to NGFWs.",
            },
            {
                "id": "d",
                "text": "NAT (Network Address Translation) for inside-to-outside address mapping",
                "correct": False,
                "rationale": "Incorrect. NAT is performed by traditional firewalls and routers alike; it is not a next-generation-only feature.",
            },
        ],
        "explanation": (
            "NGFW = traditional stateful firewall + Layer 7 app control + integrated IPS + "
            "user/identity awareness + SSL inspection + malware detection. Traditional stateful "
            "firewalls: only port/protocol and connection state. The distinguishing NGFW "
            "capabilities are L7 visibility and inline IPS."
        ),
    },
    {
        "id": "cd1v3-045",
        "domain": 1,
        "objective": "1.11",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Wireless principles",
        "stem": (
            "An engineer compares 802.11n (Wi-Fi 4) and 802.11ac (Wi-Fi 5). Which "
            "statement BEST distinguishes them?"
        ),
        "options": [
            {
                "id": "a",
                "text": "802.11ac operates exclusively in the 5 GHz band and supports wider channels (up to 160 MHz) and MU-MIMO, whereas 802.11n operates in both 2.4 GHz and 5 GHz with channels up to 40 MHz and only SU-MIMO",
                "correct": True,
                "rationale": "Correct. 802.11ac (Wi-Fi 5) is 5 GHz-only, supports up to 160 MHz channels, 256-QAM, and downlink MU-MIMO. 802.11n (Wi-Fi 4) supports 2.4 and 5 GHz, up to 40 MHz channels, 64-QAM, and SU-MIMO only.",
            },
            {
                "id": "b",
                "text": "802.11n is 5 GHz-only; 802.11ac added 2.4 GHz support for backward compatibility",
                "correct": False,
                "rationale": "Incorrect. The relationship is reversed: 802.11n supports both bands; 802.11ac is 5 GHz-only.",
            },
            {
                "id": "c",
                "text": "802.11ac uses OFDMA to allow multiple clients to transmit simultaneously; 802.11n does not",
                "correct": False,
                "rationale": "Incorrect. OFDMA is a feature of 802.11ax (Wi-Fi 6), not 802.11ac. 802.11ac uses OFDM (not OFDMA).",
            },
            {
                "id": "d",
                "text": "Both standards have an identical maximum channel width of 80 MHz",
                "correct": False,
                "rationale": "Incorrect. 802.11n max channel width is 40 MHz; 802.11ac supports up to 80 MHz mandatory and 160 MHz optional.",
            },
        ],
        "explanation": (
            "Wi-Fi standard comparison: 802.11n (Wi-Fi 4): 2.4/5 GHz, 40 MHz max, 64-QAM, "
            "SU-MIMO, ~600 Mbps max. 802.11ac (Wi-Fi 5): 5 GHz only, 80/160 MHz, 256-QAM, "
            "downlink MU-MIMO, ~6.9 Gbps max. 802.11ax (Wi-Fi 6): 2.4/5 GHz, OFDMA, "
            "uplink/downlink MU-MIMO, 1024-QAM."
        ),
    },
]

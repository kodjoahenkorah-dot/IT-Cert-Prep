"""
CCNA 200-301 – Domain 2: Network Access (v3)
40 new practice questions covering objectives 2.1 – 2.9.
IDs: cd2v3-001 through cd2v3-040
"""

QUESTIONS = [
    # -------------------------------------------------------------------------
    # 2.1 – VLANs
    # -------------------------------------------------------------------------
    {
        "id": "cd2v3-001",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "VLANs",
        "stem": (
            "A Cisco switch has the following configuration on Gi0/3:\n\n"
            "  switchport mode access\n"
            "  switchport access vlan 50\n\n"
            "An administrator issues 'show vlan brief' and sees that Gi0/3 is listed under VLAN 1, "
            "not VLAN 50. Which condition MOST likely explains this discrepancy?"
        ),
        "options": [
            {
                "id": "a",
                "text": "VLAN 50 does not exist in the switch's VLAN database.",
                "correct": True,
                "rationale": (
                    "Correct. When 'switchport access vlan 50' is configured but VLAN 50 has not been "
                    "created (via 'vlan 50' in global config or via VTP), the port remains associated "
                    "with its configured VLAN in running-config but 'show vlan brief' lists only active "
                    "VLANs. Some IOS versions revert the port to VLAN 1 in the display when the target "
                    "VLAN is inactive. The fix is to create VLAN 50 with 'vlan 50'."
                ),
            },
            {
                "id": "b",
                "text": "The port must be shut down and re-enabled for the VLAN assignment to take effect.",
                "correct": False,
                "rationale": (
                    "Incorrect. VLAN assignments on access ports take effect immediately without "
                    "requiring a port bounce. The issue is that the VLAN itself does not exist in "
                    "the VLAN database, not a timing or activation issue."
                ),
            },
            {
                "id": "c",
                "text": "The switch is in VTP transparent mode and cannot accept VLAN assignments above VLAN 20.",
                "correct": False,
                "rationale": (
                    "Incorrect. VTP transparent mode has no restriction on VLAN numbers. Switches in "
                    "transparent mode maintain their own local VLAN database and can create VLANs in "
                    "the normal range (1–1005) without restriction."
                ),
            },
            {
                "id": "d",
                "text": "VLAN 50 is in the extended range and requires a different configuration command.",
                "correct": False,
                "rationale": (
                    "Incorrect. VLAN 50 is in the normal VLAN range (1–1005) and is configured with "
                    "the same commands as any other VLAN. Extended range VLANs are 1006–4094."
                ),
            },
        ],
        "explanation": (
            "When 'switchport access vlan X' references a VLAN that has not been created in the VLAN "
            "database, the port's association may not appear under VLAN X in 'show vlan brief'. Always "
            "create the VLAN first ('vlan X' in global config) before assigning ports. In VTP client "
            "mode, VLANs are created via the VTP server; in server or transparent mode, they must be "
            "created locally."
        ),
    },
    {
        "id": "cd2v3-002",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "VLANs",
        "stem": (
            "A Layer 3 switch has SVIs for VLAN 10 (10.1.10.1/24) and VLAN 20 (10.1.20.1/24) with "
            "'ip routing' enabled. A host in VLAN 10 (10.1.10.50) sends a packet to 10.1.20.75. "
            "The host's default gateway is 10.1.10.1. Which statement BEST describes how the packet "
            "is forwarded on the Layer 3 switch?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The packet is received on the VLAN 10 SVI, routed to the VLAN 20 SVI, "
                    "and forwarded out the appropriate Layer 2 port in VLAN 20."
                ),
                "correct": True,
                "rationale": (
                    "Correct. The Layer 3 switch receives the frame on the VLAN 10 SVI interface, "
                    "performs a routing lookup, finds 10.1.20.0/24 connected via the VLAN 20 SVI, "
                    "and re-frames the packet with the destination MAC of 10.1.20.75 (learned via "
                    "ARP) before forwarding it out a physical port in VLAN 20."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The packet is flooded to all ports in VLAN 10 and VLAN 20 until the destination "
                    "MAC is resolved."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The Layer 3 switch performs routing, not flooding, for inter-VLAN "
                    "traffic. Flooding occurs at Layer 2 for unknown unicast destinations within a "
                    "single VLAN, not across VLANs during a routing decision."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The packet is dropped because the VLAN 10 SVI and VLAN 20 SVI are on different "
                    "subnets and cannot communicate without an external router."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The purpose of the Layer 3 switch with 'ip routing' and SVIs is to "
                    "route between VLANs internally without an external router. This is a fully "
                    "functional inter-VLAN routing configuration."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The packet is encapsulated in a CAPWAP tunnel and forwarded to the WLC for "
                    "centralized routing."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. CAPWAP tunnels are used between lightweight wireless APs and WLCs, "
                    "not for inter-VLAN routing on a Layer 3 switch. This scenario involves wired "
                    "VLANs and a Layer 3 switch."
                ),
            },
        ],
        "explanation": (
            "Inter-VLAN routing on a Layer 3 switch uses SVIs as virtual routed interfaces, one per "
            "VLAN. With 'ip routing' enabled, the switch acts as a router: it receives frames on the "
            "source VLAN SVI, performs a Layer 3 lookup, and forwards to the destination VLAN SVI. "
            "The ARP table maps destination IPs to MACs within each VLAN for the final Layer 2 delivery."
        ),
    },
    {
        "id": "cd2v3-003",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "VLANs",
        "stem": (
            "An engineer is configuring router-on-a-stick (ROAS) for inter-VLAN routing between "
            "VLAN 10 and VLAN 20. The router subinterface configuration is:\n\n"
            "  interface Gi0/0.10\n"
            "   encapsulation dot1q 10\n"
            "   ip address 172.16.10.1 255.255.255.0\n\n"
            "  interface Gi0/0.20\n"
            "   encapsulation dot1q 20\n"
            "   ip address 172.16.20.1 255.255.255.0\n\n"
            "Hosts in VLAN 10 can ping each other but cannot reach VLAN 20 hosts. "
            "The switch trunk port allows VLANs 10 and 20. What is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The physical interface Gi0/0 is missing an IP address.",
                "correct": False,
                "rationale": (
                    "Incorrect. In a ROAS configuration, the physical interface (Gi0/0) should NOT "
                    "have an IP address. Subinterfaces carry the IP addresses. The physical interface "
                    "simply needs to be administratively up with 'no shutdown'."
                ),
            },
            {
                "id": "b",
                "text": "The physical interface Gi0/0 has not been brought up with 'no shutdown'.",
                "correct": True,
                "rationale": (
                    "Correct. If the physical interface Gi0/0 is administratively down, all "
                    "subinterfaces (Gi0/0.10 and Gi0/0.20) are also down regardless of their "
                    "individual configuration. The most common ROAS oversight is forgetting 'no "
                    "shutdown' on the parent physical interface, which brings down all subinterfaces."
                ),
            },
            {
                "id": "c",
                "text": "Subinterface numbers must match the VLAN ID exactly; using .10 and .20 is not supported.",
                "correct": False,
                "rationale": (
                    "Incorrect. Subinterface numbers do not need to match VLAN IDs. The 'encapsulation "
                    "dot1q' command binds the subinterface to the VLAN. Using matching numbers (.10 for "
                    "VLAN 10) is a best practice convention, not a requirement."
                ),
            },
            {
                "id": "d",
                "text": "Router-on-a-stick only supports a maximum of one VLAN per physical interface.",
                "correct": False,
                "rationale": (
                    "Incorrect. The entire purpose of ROAS is to route between multiple VLANs using "
                    "subinterfaces on a single physical interface. There is no one-VLAN limit; multiple "
                    "subinterfaces can be created on a single physical interface."
                ),
            },
        ],
        "explanation": (
            "In a router-on-a-stick configuration, the parent physical interface must be 'no shutdown' "
            "even though it has no IP address. All subinterfaces inherit the state of the physical "
            "interface: if the parent is down, all subinterfaces go down. This is the classic ROAS "
            "troubleshooting gotcha. Verify with 'show interfaces Gi0/0' and 'show interfaces Gi0/0.10'."
        ),
    },
    {
        "id": "cd2v3-004",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "VLANs",
        "stem": (
            "Which TWO statements about VTP (VLAN Trunking Protocol) version 2 are correct? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "A VTP transparent mode switch forwards VTP advertisements it receives without processing them.",
                "correct": True,
                "rationale": (
                    "Correct. VTP transparent switches forward VTP summary and subset advertisements "
                    "received on trunk ports to other switches, but do not synchronize their own VLAN "
                    "database with the received information. They maintain an independent local VLAN database."
                ),
            },
            {
                "id": "b",
                "text": "VTP version 2 synchronizes extended-range VLANs (1006–4094) across the VTP domain.",
                "correct": False,
                "rationale": (
                    "Incorrect. VTP version 2 only synchronizes normal-range VLANs (1–1005). Extended-range "
                    "VLANs (1006–4094) require VTP version 3 to be propagated via VTP. On switches using "
                    "VTP v1/v2, extended VLANs are stored in the running-config, not the vlan.dat file."
                ),
            },
            {
                "id": "c",
                "text": "The VTP configuration revision number resets to 0 when a switch is changed from server to transparent mode and back to server mode.",
                "correct": True,
                "rationale": (
                    "Correct. Changing a switch's VTP mode to transparent resets the revision number to 0. "
                    "This is a common technique used to safely add a switch to a VTP domain without "
                    "risking a 'VTP bomb' (overwriting the production VLAN database with a stale higher "
                    "revision number)."
                ),
            },
            {
                "id": "d",
                "text": "VTP client mode switches can create and delete VLANs locally without affecting the VTP domain.",
                "correct": False,
                "rationale": (
                    "Incorrect. VTP client mode switches cannot create or delete VLANs locally. "
                    "Only VTP server mode switches can create, modify, and delete VLANs in the domain. "
                    "Clients receive and apply the VLAN database from the server."
                ),
            },
        ],
        "explanation": (
            "VTP version 2 key facts: Server mode can create/delete VLANs and propagates changes. "
            "Client mode receives and applies changes, cannot create VLANs locally. Transparent mode "
            "forwards VTP but uses its own local database. Revision number resets to 0 when switching "
            "to transparent mode — use this to safely introduce a new switch. VTPv2 only handles "
            "normal-range VLANs; use VTPv3 for extended-range VLAN propagation."
        ),
    },
    # -------------------------------------------------------------------------
    # 2.2 – Trunking & 802.1Q
    # -------------------------------------------------------------------------
    {
        "id": "cd2v3-005",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Trunking & 802.1Q",
        "stem": (
            "An engineer configures two switches with the following trunk commands:\n\n"
            "SW1 Gi0/1:\n"
            "  switchport trunk encapsulation dot1q\n"
            "  switchport mode trunk\n"
            "  switchport trunk native vlan 10\n\n"
            "SW2 Gi0/1:\n"
            "  switchport trunk encapsulation dot1q\n"
            "  switchport mode trunk\n"
            "  switchport trunk native vlan 10\n\n"
            "Later, a PC in VLAN 10 is connected to SW1 Gi0/2 (access port, VLAN 10). "
            "The PC can reach hosts in VLAN 10 on SW2 but notices that inter-VLAN traffic "
            "from VLAN 10 to VLAN 20 is being routed WITHOUT traversing the router. "
            "What is the security concern with this topology?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The native VLAN (10) is also a production data VLAN, so untagged traffic bypasses VLAN access controls.",
                "correct": True,
                "rationale": (
                    "Correct. Using a production data VLAN (VLAN 10) as the native VLAN is a security "
                    "risk. Native VLAN traffic is sent untagged across the trunk. An attacker in VLAN 10 "
                    "can exploit this to craft double-tagged frames targeting other VLANs, or untagged "
                    "traffic may be misrouted. Best practice is to use a dedicated, unused native VLAN."
                ),
            },
            {
                "id": "b",
                "text": "The trunk is using 802.1Q instead of ISL, which does not support the native VLAN concept.",
                "correct": False,
                "rationale": (
                    "Incorrect. 802.1Q does support the native VLAN concept — untagged frames belong to "
                    "the native VLAN. ISL is a deprecated Cisco-proprietary protocol that encapsulates "
                    "all frames and has no native VLAN. The security concern is about native VLAN assignment."
                ),
            },
            {
                "id": "c",
                "text": "Both switches must use different native VLANs to prevent STP loops.",
                "correct": False,
                "rationale": (
                    "Incorrect. Native VLANs must MATCH on both ends of a trunk to avoid native VLAN "
                    "mismatch issues. Using different native VLANs creates a mismatch, not a solution. "
                    "STP loop prevention is unrelated to native VLAN assignment."
                ),
            },
            {
                "id": "d",
                "text": "The configuration will cause the trunk to err-disable because VLAN 10 is used as both access and native.",
                "correct": False,
                "rationale": (
                    "Incorrect. Using a production VLAN as the native VLAN does not cause err-disable. "
                    "The trunk will function normally at the protocol level; the concern is a security "
                    "and design best-practice issue, not a technical failure."
                ),
            },
        ],
        "explanation": (
            "Best practice: never use a production VLAN as the native VLAN. Use a dedicated, unused "
            "VLAN (e.g., VLAN 999) as the native VLAN on all trunks. This prevents double-tagging "
            "VLAN hopping attacks and ensures that untagged frames (management or legacy) do not "
            "mix with production user traffic. Also consider tagging the native VLAN with "
            "'vlan dot1q tag native' to eliminate untagged frames entirely."
        ),
    },
    {
        "id": "cd2v3-006",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Trunking & 802.1Q",
        "stem": (
            "SW1 Gi0/1 is configured with 'switchport mode dynamic auto'. SW2 Gi0/1 is also "
            "configured with 'switchport mode dynamic auto'. A host in VLAN 20 on SW1 cannot "
            "reach a host in VLAN 20 on SW2 even though both are in the same VLAN. "
            "Which statement BEST explains the problem?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Both ports are in 'dynamic auto' mode, so neither initiates trunking and the link operates as an access link.",
                "correct": True,
                "rationale": (
                    "Correct. 'Dynamic auto' mode only forms a trunk if the other side actively "
                    "requests it. When both sides are 'dynamic auto', neither initiates, and the link "
                    "becomes an access link (typically VLAN 1). VLAN 20 traffic is not forwarded "
                    "across an access link unless both sides are in VLAN 20, which they are not "
                    "in a default inter-switch scenario."
                ),
            },
            {
                "id": "b",
                "text": "DTP requires a password to negotiate trunking; without it, both ports stay in access mode.",
                "correct": False,
                "rationale": (
                    "Incorrect. DTP does not require a password. The 'dynamic auto' + 'dynamic auto' "
                    "combination simply results in neither side initiating trunking, defaulting to "
                    "access mode — no password is involved."
                ),
            },
            {
                "id": "c",
                "text": "VLAN 20 is not in the allowed VLAN list because DTP removes non-default VLANs.",
                "correct": False,
                "rationale": (
                    "Incorrect. DTP negotiates the trunking mode (trunk vs. access), not the allowed "
                    "VLAN list. The allowed VLAN list defaults to all VLANs (1-4094) on a trunk. "
                    "The problem is that no trunk is forming at all."
                ),
            },
            {
                "id": "d",
                "text": "Both switches must have the same VTP domain name for DTP to successfully negotiate a trunk.",
                "correct": False,
                "rationale": (
                    "Incorrect. DTP negotiates trunking independently of VTP domain membership. "
                    "The root cause here is the auto+auto combination, not VTP domain mismatch."
                ),
            },
        ],
        "explanation": (
            "DTP mode matrix for 'dynamic auto' + 'dynamic auto': neither side initiates, resulting "
            "in an access port. The link will be up at Layer 1/2 but will only carry one VLAN "
            "(the access VLAN, default VLAN 1). VLAN 20 traffic will not traverse the link. "
            "Fix: set at least one side to 'trunk' or 'dynamic desirable'. Best practice: "
            "use static 'switchport mode trunk' with 'switchport nonegotiate' on inter-switch links."
        ),
    },
    {
        "id": "cd2v3-007",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Trunking & 802.1Q",
        "stem": (
            "A network engineer reviews the following output:\n\n"
            "SW1# show interfaces Gi0/1 trunk\n"
            "Port      Mode         Encapsulation  Status       Native vlan\n"
            "Gi0/1     on           802.1q         not-trunking  1\n\n"
            "SW1 Gi0/1 is configured with 'switchport mode trunk'. What is the MOST likely "
            "reason the port shows 'not-trunking' status?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The native VLAN is VLAN 1, which prevents the port from entering trunking state.",
                "correct": False,
                "rationale": (
                    "Incorrect. VLAN 1 as the native VLAN is the default and does not prevent trunking. "
                    "Native VLAN 1 is a security concern but not a functional problem for trunk formation."
                ),
            },
            {
                "id": "b",
                "text": "The far-end switch port is configured as an access port, preventing trunk negotiation.",
                "correct": True,
                "rationale": (
                    "Correct. If SW1's port is set to 'trunk' but the far-end port is configured as "
                    "'access' (or is an end-host port), the trunk cannot form. 'Status: not-trunking' "
                    "with 'Mode: on' on the local side indicates the other end is not accepting trunk "
                    "frames or is explicitly configured as an access port."
                ),
            },
            {
                "id": "c",
                "text": "The 'switchport trunk encapsulation dot1q' command was not issued before 'switchport mode trunk'.",
                "correct": False,
                "rationale": (
                    "Incorrect. The output shows 'Encapsulation: 802.1q', confirming the encapsulation "
                    "is configured. On switches that support only 802.1Q (no ISL), the encapsulation "
                    "may be set automatically. The encapsulation is not the issue here."
                ),
            },
            {
                "id": "d",
                "text": "DTP has been disabled with 'switchport nonegotiate', causing the trunk to fail.",
                "correct": False,
                "rationale": (
                    "Incorrect. 'switchport nonegotiate' disables DTP but does not prevent a static "
                    "trunk from forming when both ends are configured with 'switchport mode trunk'. "
                    "The port is set to 'on' (static trunk), which does not rely on DTP."
                ),
            },
        ],
        "explanation": (
            "A trunk port showing 'not-trunking' despite 'mode on' indicates the far end is not "
            "configured for trunking. This happens when the connected device is an end-host, or when "
            "the far-end switch port is explicitly configured as 'switchport mode access'. "
            "Verify with 'show cdp neighbors detail' to confirm the far-end device/port and check "
            "its switchport configuration."
        ),
    },
    {
        "id": "cd2v3-008",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Trunking & 802.1Q",
        "stem": (
            "An 802.1Q frame arrives on a trunk port. The frame has no 802.1Q tag (it is untagged). "
            "The trunk port has 'switchport trunk native vlan 25' configured. "
            "In which VLAN does the switch place this untagged frame?"
        ),
        "options": [
            {
                "id": "a",
                "text": "VLAN 1, because untagged frames always belong to the default VLAN.",
                "correct": False,
                "rationale": (
                    "Incorrect. VLAN 1 is the default native VLAN only when no native VLAN is configured. "
                    "When 'switchport trunk native vlan 25' is configured, untagged frames received on "
                    "that trunk are placed in VLAN 25, not VLAN 1."
                ),
            },
            {
                "id": "b",
                "text": "VLAN 25, because that is the configured native VLAN for this trunk port.",
                "correct": True,
                "rationale": (
                    "Correct. On an 802.1Q trunk, untagged frames are assigned to the native VLAN. "
                    "Since the native VLAN is configured as VLAN 25, any untagged frame arriving on "
                    "this trunk is placed into VLAN 25."
                ),
            },
            {
                "id": "c",
                "text": "The frame is dropped because all frames on a trunk port must be tagged with 802.1Q.",
                "correct": False,
                "rationale": (
                    "Incorrect. 802.1Q trunks specifically allow one untagged VLAN — the native VLAN. "
                    "Untagged frames are not dropped; they are associated with the native VLAN. "
                    "Only if 'vlan dot1q tag native' is configured are native VLAN frames required to be tagged."
                ),
            },
            {
                "id": "d",
                "text": "The frame is flooded to all VLANs in the allowed list because its VLAN cannot be determined.",
                "correct": False,
                "rationale": (
                    "Incorrect. The native VLAN configuration explicitly defines where untagged frames "
                    "belong. There is no ambiguity — the frame is placed in the native VLAN. "
                    "Flooding to all VLANs does not occur."
                ),
            },
        ],
        "explanation": (
            "The 802.1Q native VLAN is the single VLAN on a trunk that sends and receives frames "
            "without an 802.1Q tag. Both ends of the trunk must agree on the native VLAN; a mismatch "
            "causes frames to be placed in the wrong VLAN. The 'switchport trunk native vlan' command "
            "overrides the default of VLAN 1. To enforce tagging on all frames (including native VLAN), "
            "use global command 'vlan dot1q tag native'."
        ),
    },
    # -------------------------------------------------------------------------
    # 2.3 – CDP & LLDP
    # -------------------------------------------------------------------------
    {
        "id": "cd2v3-009",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "CDP & LLDP",
        "stem": (
            "A network administrator issues 'show lldp neighbors detail' and sees a neighbor with "
            "the System Capabilities field showing 'B, R' and the Enabled Capabilities showing 'B'. "
            "What does this output indicate about the neighbor device?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The device is capable of being both a bridge and a router, but is currently operating only as a bridge.",
                "correct": True,
                "rationale": (
                    "Correct. LLDP System Capabilities TLV has two fields: 'capabilities' (what the "
                    "device is capable of) and 'enabled capabilities' (what is currently active). "
                    "'B' = Bridge (switch), 'R' = Router. The device is capable of both but currently "
                    "only the Bridge function is enabled, suggesting routing is disabled or not licensed."
                ),
            },
            {
                "id": "b",
                "text": "The device is a router with both BGP and OSPF routing protocols enabled.",
                "correct": False,
                "rationale": (
                    "Incorrect. The LLDP System Capabilities letters 'B' and 'R' stand for Bridge and "
                    "Router respectively, not routing protocol types. BGP and OSPF are not indicated "
                    "in LLDP capability advertisements."
                ),
            },
            {
                "id": "c",
                "text": "The device is a backup router; 'B' indicates it is in standby mode via HSRP.",
                "correct": False,
                "rationale": (
                    "Incorrect. LLDP capability flags are standardized IEEE 802.1AB TLVs and are not "
                    "related to HSRP states. 'B' in LLDP capabilities means Bridge (Layer 2 switching "
                    "device), not backup or HSRP standby."
                ),
            },
            {
                "id": "d",
                "text": "The device supports 802.1Q bridging but the 'R' flag is an error indicating a misconfigured LLDP TLV.",
                "correct": False,
                "rationale": (
                    "Incorrect. 'R' is a valid LLDP System Capability flag meaning Router. "
                    "It is not an error. The capabilities field accurately reflects what the device "
                    "supports and what is currently enabled."
                ),
            },
        ],
        "explanation": (
            "LLDP (IEEE 802.1AB) System Capabilities TLV advertises device roles using standardized "
            "bit flags: B=Bridge, R=Router, T=Telephone, D=DOCSIS Cable Device, H=Host, W=WLAN AP, "
            "P=Repeater, C=Customer VLAN, S=S-VLAN. Two subfields: 'System Capabilities' (what the "
            "device supports) and 'Enabled Capabilities' (what is active). Useful for topology "
            "discovery in multi-vendor environments."
        ),
    },
    {
        "id": "cd2v3-010",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "CDP & LLDP",
        "stem": (
            "An engineer wants to disable CDP on a specific interface facing an untrusted network "
            "segment while keeping CDP operational on all other switch interfaces. "
            "Which command accomplishes this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "SW1(config)# no cdp run",
                "correct": False,
                "rationale": (
                    "Incorrect. 'no cdp run' is a global command that disables CDP on ALL interfaces "
                    "of the switch. The requirement is to disable CDP only on a specific interface."
                ),
            },
            {
                "id": "b",
                "text": "SW1(config-if)# no cdp enable",
                "correct": True,
                "rationale": (
                    "Correct. 'no cdp enable' is an interface-level command that disables CDP on a "
                    "specific interface while leaving CDP active globally and on all other interfaces. "
                    "This is the recommended practice for interfaces connected to untrusted networks."
                ),
            },
            {
                "id": "c",
                "text": "SW1(config-if)# cdp disable",
                "correct": False,
                "rationale": (
                    "Incorrect. 'cdp disable' is not a valid Cisco IOS command. The correct "
                    "interface-level command to disable CDP is 'no cdp enable'."
                ),
            },
            {
                "id": "d",
                "text": "SW1(config-if)# no cdp advertise-v2",
                "correct": False,
                "rationale": (
                    "Incorrect. 'no cdp advertise-v2' disables CDPv2 advertisements on the interface "
                    "but does not completely disable CDP. CDPv1 advertisements would still be sent. "
                    "The correct command to fully disable CDP per-interface is 'no cdp enable'."
                ),
            },
        ],
        "explanation": (
            "CDP security best practice: disable CDP globally on switches that face untrusted "
            "networks ('no cdp run'), or selectively disable it per interface using 'no cdp enable' "
            "in interface configuration mode. CDP reveals device platform, IOS version, IP addresses, "
            "and VLAN information — valuable to an attacker performing network reconnaissance. "
            "Apply 'no cdp enable' to all WAN, DMZ, and customer-facing interfaces."
        ),
    },
    {
        "id": "cd2v3-011",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "CDP & LLDP",
        "stem": (
            "A network engineer issues 'show cdp neighbors' and sees a neighbor on Gi0/2 with "
            "Device ID 'SW-DIST-01', Platform 'cisco WS-C3850-48P', and Capability 'R S I'. "
            "What do the capability codes 'R S I' indicate about SW-DIST-01?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The device is a Router, a Switch, and an IGMP snooping device.",
                "correct": False,
                "rationale": (
                    "Incorrect. 'I' in CDP capability codes does not stand for IGMP snooping. "
                    "CDP uses specific single-letter codes: R=Router, T=Trans Bridge, B=Source Route "
                    "Bridge, S=Switch, H=Host, I=IGMP, r=Repeater, P=Phone, D=Remotely Managed, "
                    "C=CVTA, M=Two-port Mac Relay."
                ),
            },
            {
                "id": "b",
                "text": "The device is a Router, a Switch, and supports IGMP (multicast) capabilities.",
                "correct": True,
                "rationale": (
                    "Correct. In CDP capability codes: R=Router, S=Switch (Layer 2), I=IGMP. "
                    "The Cisco 3850 is a Layer 3 switch, so it advertises Router (routing capable), "
                    "Switch (Layer 2), and I (IGMP snooping/multicast capability)."
                ),
            },
            {
                "id": "c",
                "text": "The device is in Routing mode, Switching mode, and Idle mode simultaneously.",
                "correct": False,
                "rationale": (
                    "Incorrect. CDP capability codes describe device capabilities and features, not "
                    "operational states. There is no 'Idle' capability code. The codes describe what "
                    "the device is and what it supports."
                ),
            },
            {
                "id": "d",
                "text": "The device is a Redundant Switch with Intelligent routing and requires special configuration.",
                "correct": False,
                "rationale": (
                    "Incorrect. CDP capability codes are standardized and 'R S I' specifically means "
                    "Router, Switch, and IGMP. There is no 'Redundant' or 'Intelligent' capability code."
                ),
            },
        ],
        "explanation": (
            "CDP capability codes: R = Router, T = Trans Bridge, B = Source Route Bridge, S = Switch, "
            "H = Host, I = IGMP (multicast/IGMP snooping capable), r = Repeater, P = Phone, "
            "D = Remotely Managed Device, C = CVTA, M = Two-port Mac Relay. Layer 3 switches "
            "commonly show 'R S I' indicating routing, switching, and IGMP capabilities."
        ),
    },
    # -------------------------------------------------------------------------
    # 2.4 – EtherChannel
    # -------------------------------------------------------------------------
    {
        "id": "cd2v3-012",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "EtherChannel",
        "stem": (
            "An engineer configures a Layer 3 EtherChannel between two distribution switches. "
            "After configuration, the port-channel interface is up but no routing occurs. "
            "The configuration on SW1 is:\n\n"
            "  interface Port-channel1\n"
            "   ip address 10.0.0.1 255.255.255.252\n\n"
            "  interface range Gi0/1-2\n"
            "   channel-group 1 mode active\n\n"
            "What is the MOST likely missing configuration on the member interfaces?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The member interfaces need 'switchport mode trunk' to carry tagged VLANs.",
                "correct": False,
                "rationale": (
                    "Incorrect. A Layer 3 EtherChannel uses routed (no switchport) member interfaces, "
                    "not trunk interfaces. Trunk configuration is for Layer 2 EtherChannels."
                ),
            },
            {
                "id": "b",
                "text": "The member interfaces need 'no switchport' to operate as Layer 3 routed ports.",
                "correct": True,
                "rationale": (
                    "Correct. For a Layer 3 EtherChannel, member interfaces must be configured with "
                    "'no switchport' to convert them from Layer 2 switch ports to Layer 3 routed ports. "
                    "The IP address is assigned to the Port-channel interface, and the member ports "
                    "must be routed ports. Without 'no switchport', they remain Layer 2 ports."
                ),
            },
            {
                "id": "c",
                "text": "The Port-channel interface needs 'no shutdown' to activate routing.",
                "correct": False,
                "rationale": (
                    "Incorrect. While 'no shutdown' is needed if the interface is administratively down, "
                    "the stem states the port-channel is up. The missing element is 'no switchport' on "
                    "the member interfaces to make the channel a Layer 3 interface."
                ),
            },
            {
                "id": "d",
                "text": "The 'ip routing' command must be added under the Port-channel interface.",
                "correct": False,
                "rationale": (
                    "Incorrect. 'ip routing' is a global command, not an interface command. "
                    "It must be issued in global configuration mode, not on a specific interface. "
                    "However, the primary missing element is 'no switchport' on the member interfaces."
                ),
            },
        ],
        "explanation": (
            "Layer 3 EtherChannel configuration requires: (1) 'no switchport' on each physical "
            "member interface to convert them to routed ports, (2) 'channel-group X mode' on each "
            "member, (3) IP address on the Port-channel logical interface (not on physical members), "
            "and (4) 'ip routing' globally enabled. Without 'no switchport', the interfaces remain "
            "Layer 2 and cannot support the Layer 3 port-channel."
        ),
    },
    {
        "id": "cd2v3-013",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "EtherChannel",
        "stem": (
            "A 4-link LACP EtherChannel is configured between SW1 and SW2. Each link is 1 Gbps. "
            "An engineer observes that all traffic between two specific hosts always uses the "
            "same single physical link in the bundle, even though other links are idle. "
            "Which statement BEST explains this behavior?"
        ),
        "options": [
            {
                "id": "a",
                "text": "LACP has elected one link as the 'hot active' link and only uses other links when it fails.",
                "correct": False,
                "rationale": (
                    "Incorrect. LACP does not elect a 'hot active' link that carries all traffic. "
                    "All links in a bundle are active. The load-balancing algorithm determines which "
                    "link each flow uses."
                ),
            },
            {
                "id": "b",
                "text": (
                    "EtherChannel load-balancing hashes traffic to physical links based on a configured "
                    "algorithm (e.g., src-dst-mac); two hosts with the same hash value always use the same link."
                ),
                "correct": True,
                "rationale": (
                    "Correct. EtherChannel does NOT round-robin per-packet. It uses a hash algorithm "
                    "(configurable via 'port-channel load-balance') based on source/destination MAC, "
                    "IP, or port. Two hosts that hash to the same value will always use the same "
                    "physical link. This is by design — per-flow consistency prevents out-of-order delivery."
                ),
            },
            {
                "id": "c",
                "text": "STP has blocked three of the four links to prevent loops, leaving only one forwarding.",
                "correct": False,
                "rationale": (
                    "Incorrect. STP treats all links in an EtherChannel bundle as a single logical "
                    "link on the port-channel interface. STP does not block individual member links "
                    "within an already-formed EtherChannel."
                ),
            },
            {
                "id": "d",
                "text": "The four links have formed an active/standby pair; two links are active and two are in hot-standby.",
                "correct": False,
                "rationale": (
                    "Incorrect. LACP can place some links in hot-standby if more than 8 links are "
                    "configured (LACP maximum active links). With only 4 links, all 4 should be "
                    "active and forwarding. The observed behavior is explained by hash-based load balancing."
                ),
            },
        ],
        "explanation": (
            "EtherChannel load balancing uses a hash of traffic attributes (MAC, IP, TCP/UDP port, "
            "or combination) to assign flows to physical links. The hash is deterministic: the same "
            "source-destination pair always maps to the same link, ensuring per-flow ordering. "
            "Configure with 'port-channel load-balance {src-mac|dst-mac|src-dst-mac|src-ip|dst-ip|"
            "src-dst-ip|src-port|dst-port|src-dst-port}'. Verify with 'show etherchannel load-balance'."
        ),
    },
    {
        "id": "cd2v3-014",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "EtherChannel",
        "stem": (
            "An engineer sees the following in 'show etherchannel summary':\n\n"
            "Group  Port-channel  Protocol    Ports\n"
            "1      Po1(SU)       LACP        Gi0/1(P)  Gi0/2(P)  Gi0/3(I)\n\n"
            "What does the 'I' flag on Gi0/3 indicate, and what is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "'I' means the interface is inactive due to physical link failure.",
                "correct": False,
                "rationale": (
                    "Incorrect. A physical link failure would show 'D' (down) on the member interface, "
                    "not 'I'. The 'I' flag has a specific meaning related to EtherChannel configuration."
                ),
            },
            {
                "id": "b",
                "text": "'I' means stand-alone; Gi0/3 is not bundled, most likely due to a configuration mismatch with the other member ports.",
                "correct": True,
                "rationale": (
                    "Correct. The 'I' flag means 'stand-alone' — the interface is not bundled into "
                    "the port-channel. This typically occurs when the interface has a configuration "
                    "that does not match the other bundled members (e.g., different speed, duplex, "
                    "VLAN, or trunk settings), causing the switch to exclude it from the bundle."
                ),
            },
            {
                "id": "c",
                "text": "'I' means the interface is idle and will be added to the bundle when traffic increases.",
                "correct": False,
                "rationale": (
                    "Incorrect. EtherChannel does not have an 'idle' state that activates based on "
                    "traffic load. All eligible member interfaces are either bundled (P) or excluded. "
                    "'I' stands for stand-alone, indicating a configuration issue."
                ),
            },
            {
                "id": "d",
                "text": "'I' means the interface has been individually configured with 'no channel-group'.",
                "correct": False,
                "rationale": (
                    "Incorrect. If 'no channel-group' were issued, the interface would not appear in "
                    "the EtherChannel summary at all. The 'I' flag indicates the interface IS assigned "
                    "to the channel-group but cannot be bundled due to a configuration incompatibility."
                ),
            },
        ],
        "explanation": (
            "EtherChannel member port flags: P=bundled/active, D=down, I=stand-alone (excluded from "
            "bundle due to incompatible configuration), s=suspended (port is in the channel-group "
            "but suspended due to configuration error), H=hot-standby (LACP max active links exceeded), "
            "u=unsuitable for bundling. 'I' (stand-alone) is diagnosed by comparing the Gi0/3 "
            "configuration against the bundled members (Gi0/1, Gi0/2)."
        ),
    },
    {
        "id": "cd2v3-015",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "EtherChannel",
        "stem": (
            "Which TWO requirements must be met for physical interfaces to be successfully "
            "bundled into a Layer 2 EtherChannel on a Cisco IOS switch? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "All member interfaces must have the same speed and duplex settings.",
                "correct": True,
                "rationale": (
                    "Correct. EtherChannel requires all physical member interfaces to operate at the "
                    "same speed and duplex. Mismatched speed or duplex between member ports on the "
                    "same switch will prevent the ports from being bundled."
                ),
            },
            {
                "id": "b",
                "text": "All member interfaces must be connected to the same remote switch.",
                "correct": False,
                "rationale": (
                    "Incorrect. While this is typical for a standard EtherChannel, Cisco supports "
                    "Multi-chassis EtherChannel (MEC) technologies like VSS and StackWise where members "
                    "can connect to different physical chassis. The requirement for standard EtherChannel "
                    "is matching local port configurations, not the remote switch topology."
                ),
            },
            {
                "id": "c",
                "text": "All member interfaces must have the same access VLAN (if access ports) or the same trunk settings (if trunk ports).",
                "correct": True,
                "rationale": (
                    "Correct. Layer 2 EtherChannel requires that all member interfaces on the same "
                    "switch have identical Layer 2 configurations: same switchport mode, same access "
                    "VLAN (for access ports), or same native VLAN and allowed VLANs (for trunk ports)."
                ),
            },
            {
                "id": "d",
                "text": "LACP must be used; static 'on' mode is not supported for Layer 2 EtherChannel.",
                "correct": False,
                "rationale": (
                    "Incorrect. Layer 2 EtherChannel supports three modes: LACP (active/passive), "
                    "PAgP (desirable/auto), and static 'on'. All three are valid. LACP is preferred "
                    "for interoperability and link management, but 'on' mode is fully supported."
                ),
            },
        ],
        "explanation": (
            "Layer 2 EtherChannel bundling requirements for member ports on the same switch: "
            "same speed, same duplex, same switchport mode (access/trunk), same VLAN configuration "
            "(access VLAN or native+allowed VLANs for trunks), same STP port configuration. "
            "Mismatches result in 'I' (stand-alone) or 'u' (unsuitable) flags. Verify with "
            "'show etherchannel summary' and compare member port configs."
        ),
    },
    # -------------------------------------------------------------------------
    # 2.5 – Spanning Tree (RPVST+)
    # -------------------------------------------------------------------------
    {
        "id": "cd2v3-016",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Spanning Tree (RPVST+)",
        "stem": (
            "In a Rapid PVST+ network, SW3 is a non-root switch with two uplinks:\n\n"
            "  - Gi0/1 to SW1 (root bridge): path cost 4\n"
            "  - Gi0/2 to SW2 (non-root): path cost 4, SW2's cost to root is 4\n\n"
            "What is the total root path cost via each port, and which becomes the root port?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Gi0/1 root path cost = 4; Gi0/2 root path cost = 8. Gi0/1 is the root port.",
                "correct": True,
                "rationale": (
                    "Correct. Root path cost is the cumulative cost from the local switch to the root. "
                    "Via Gi0/1 directly to SW1 (root): cost = 4. Via Gi0/2 to SW2 then to root: "
                    "SW3's link cost 4 + SW2's root path cost 4 = 8. Lower root path cost wins: "
                    "Gi0/1 (cost 4) becomes SW3's root port."
                ),
            },
            {
                "id": "b",
                "text": "Gi0/1 root path cost = 4; Gi0/2 root path cost = 4. MAC address breaks the tie.",
                "correct": False,
                "rationale": (
                    "Incorrect. Root path cost via Gi0/2 is SW3's link cost (4) plus SW2's root path "
                    "cost (4) = 8, not 4. The cost accumulates as the BPDU traverses additional hops. "
                    "SW2 advertises its root path cost in BPDUs, and SW3 adds its local link cost."
                ),
            },
            {
                "id": "c",
                "text": "Gi0/2 root path cost = 4; Gi0/1 root path cost = 8. Gi0/2 is the root port.",
                "correct": False,
                "rationale": (
                    "Incorrect. SW3 is directly connected to SW1 (root) via Gi0/1 with cost 4. "
                    "The path via SW2 (Gi0/2) adds SW2's root path cost (4) to SW3's link cost (4), "
                    "giving 8. Gi0/1 has the lower total root path cost."
                ),
            },
            {
                "id": "d",
                "text": "Both ports have equal root path costs because both are 1 Gbps links; STP will block one arbitrarily.",
                "correct": False,
                "rationale": (
                    "Incorrect. The local link costs are equal (both 4), but the total root path cost "
                    "accounts for ALL hops to the root. Via SW2, the cost includes SW2's own accumulated "
                    "path cost. The costs are not equal: Gi0/1=4, Gi0/2=8."
                ),
            },
        ],
        "explanation": (
            "STP root path cost is cumulative: each switch adds its local port cost to the cost "
            "advertised in the BPDU received from the upstream switch. SW2 sends BPDUs with root "
            "path cost 4; SW3 receives this on Gi0/2 and adds its local cost of 4 = total 8. "
            "SW1 (root) sends BPDUs with root path cost 0; SW3 adds local cost 4 = total 4. "
            "Default 802.1t costs: 10Mbps=100, 100Mbps=19, 1Gbps=4, 10Gbps=2."
        ),
    },
    {
        "id": "cd2v3-017",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Spanning Tree (RPVST+)",
        "stem": (
            "An engineer issues 'spanning-tree vlan 10 priority 4096' on SW1. The current root "
            "bridge for VLAN 10 has bridge priority 8192. What will happen after the command "
            "takes effect?"
        ),
        "options": [
            {
                "id": "a",
                "text": "SW1 becomes the root bridge because 4096 is lower than the current root's 8192.",
                "correct": True,
                "rationale": (
                    "Correct. STP root election uses the lowest bridge ID (priority + MAC). "
                    "SW1's new priority of 4096 is lower than the current root's 8192. SW1 will "
                    "send BPDUs claiming to be the root, and after the current root receives them, "
                    "it will yield and SW1 will be elected root for VLAN 10."
                ),
            },
            {
                "id": "b",
                "text": "The command is rejected because 4096 is not a valid STP priority value.",
                "correct": False,
                "rationale": (
                    "Incorrect. STP priority values must be multiples of 4096, ranging from 0 to "
                    "61440. The value 4096 is a valid priority. The full bridge priority for VLAN 10 "
                    "would be 4096 + 10 (VLAN ID) = 4106."
                ),
            },
            {
                "id": "c",
                "text": "SW1 becomes root only after the current root bridge fails.",
                "correct": False,
                "rationale": (
                    "Incorrect. When SW1 advertises a lower bridge ID, it triggers immediate STP "
                    "reconvergence. The current root will receive SW1's superior BPDUs and cease "
                    "claiming root status. A root failure is not required."
                ),
            },
            {
                "id": "d",
                "text": "Both SW1 and the current root declare themselves root, causing a STP storm.",
                "correct": False,
                "rationale": (
                    "Incorrect. STP is designed to handle multiple switches claiming root. Each switch "
                    "compares received BPDUs against its own. Switches that receive a superior BPDU "
                    "(lower bridge ID) stop claiming root and forward the superior BPDU. No storm occurs."
                ),
            },
        ],
        "explanation": (
            "STP priority must be in multiples of 4096 (0, 4096, 8192, 12288, ..., 61440). The "
            "full bridge priority = configured priority + VLAN ID (extended system ID). When SW1 "
            "advertises a bridge ID lower than the current root's, STP converges and elects SW1 "
            "as root. All non-root switches recalculate their root ports and designated ports. "
            "Convergence takes seconds in Rapid PVST+."
        ),
    },
    {
        "id": "cd2v3-018",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "STP port roles & states",
        "stem": (
            "In Rapid PVST+, when a non-root switch SW3 loses its root port connection, which port "
            "role immediately begins the transition to forwarding state to restore connectivity "
            "to the root bridge?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The backup port transitions to forwarding state.",
                "correct": False,
                "rationale": (
                    "Incorrect. A backup port provides a redundant path to a segment where the same "
                    "switch already has a designated port. It does NOT take over as root port when "
                    "the root port fails."
                ),
            },
            {
                "id": "b",
                "text": "The alternate port transitions to the root port role and begins the convergence process.",
                "correct": True,
                "rationale": (
                    "Correct. In Rapid PVST+, the alternate port is a discarding port that has "
                    "received a superior BPDU from another switch (a path to the root via a different "
                    "path). When the root port fails, the alternate port immediately becomes the new "
                    "root port and rapidly transitions to forwarding, enabling fast convergence."
                ),
            },
            {
                "id": "c",
                "text": "The designated port on the same switch transitions to become the new root port.",
                "correct": False,
                "rationale": (
                    "Incorrect. Designated ports forward traffic toward downstream hosts and segments. "
                    "They do not become root ports. The root port is always the port with the best "
                    "path to the root bridge."
                ),
            },
            {
                "id": "d",
                "text": "The switch floods a topology change notification and waits for the root bridge to assign a new root port.",
                "correct": False,
                "rationale": (
                    "Incorrect. RSTP does not have a centralized root-port assignment mechanism. "
                    "Each switch independently selects its own root port based on BPDUs. The alternate "
                    "port transitions autonomously without waiting for the root bridge."
                ),
            },
        ],
        "explanation": (
            "Rapid PVST+ (RSTP) port role definitions: Root port = best path to root (forwarding); "
            "Alternate port = backup path to root, maintained in discarding state. When the root port "
            "fails, the alternate port with the next-best path becomes the new root port and transitions "
            "rapidly to forwarding (sub-second in ideal conditions). This is fundamentally faster than "
            "classic STP which required MaxAge + ForwardDelay timers."
        ),
    },
    {
        "id": "cd2v3-019",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "PortFast & BPDU Guard",
        "stem": (
            "A switch port connected to a workstation has been err-disabled due to BPDU Guard. "
            "The administrator removes the unauthorized switch and wants to restore the port. "
            "Which TWO methods can restore the port? (Choose the option that correctly lists BOTH.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Manually issue 'shutdown' then 'no shutdown' on the interface, OR configure 'errdisable recovery cause bpduguard'.",
                "correct": True,
                "rationale": (
                    "Correct. An err-disabled port can be recovered in two ways: (1) manually by "
                    "issuing 'shutdown' then 'no shutdown' on the interface, or (2) automatically "
                    "using 'errdisable recovery cause bpduguard' (with optional 'errdisable recovery "
                    "interval' to set the retry timer, default 300 seconds). Both are valid recovery methods."
                ),
            },
            {
                "id": "b",
                "text": "Issue 'no spanning-tree bpduguard enable' on the interface, then it auto-recovers.",
                "correct": False,
                "rationale": (
                    "Incorrect. Removing BPDU Guard configuration does not automatically recover an "
                    "already err-disabled port. The port must be manually bounced (shutdown/no shutdown) "
                    "or use errdisable recovery even after removing BPDU Guard."
                ),
            },
            {
                "id": "c",
                "text": "Reboot the switch to clear all err-disabled states, OR reconfigure the port as a trunk port.",
                "correct": False,
                "rationale": (
                    "Incorrect. A switch reboot would clear err-disabled states, but it is highly "
                    "disruptive and not a recommended recovery method. Reconfiguring as a trunk does "
                    "not recover the err-disabled port; the err-disabled state must be cleared first."
                ),
            },
            {
                "id": "d",
                "text": "Issue 'clear spanning-tree bpduguard interface Gi0/x' to reset the port state.",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no 'clear spanning-tree bpduguard' command in Cisco IOS. "
                    "Err-disabled recovery uses 'shutdown/no shutdown' or the 'errdisable recovery' "
                    "global configuration mechanism."
                ),
            },
        ],
        "explanation": (
            "BPDU Guard err-disables a port when a BPDU is received on a PortFast-enabled port. "
            "Recovery options: (1) Manual: 'interface Gi0/x' then 'shutdown' then 'no shutdown'; "
            "(2) Automatic: 'errdisable recovery cause bpduguard' in global config, with optional "
            "'errdisable recovery interval <seconds>' (default 300s). Always confirm the unauthorized "
            "switch has been removed before recovering the port."
        ),
    },
    {
        "id": "cd2v3-020",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "PortFast & BPDU Guard",
        "stem": (
            "A network engineer wants to enable BPDU Guard on all PortFast-enabled ports globally, "
            "without having to configure each port individually. Which command accomplishes this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "spanning-tree bpduguard default",
                "correct": False,
                "rationale": (
                    "Incorrect. 'spanning-tree bpduguard default' is not a valid Cisco IOS global "
                    "configuration command. BPDU Guard is enabled globally using a different syntax."
                ),
            },
            {
                "id": "b",
                "text": "spanning-tree portfast bpduguard default",
                "correct": True,
                "rationale": (
                    "Correct. 'spanning-tree portfast bpduguard default' enables BPDU Guard globally "
                    "on all ports that have PortFast enabled (either by 'spanning-tree portfast' "
                    "interface command or by 'spanning-tree portfast default'). It does not enable "
                    "BPDU Guard on ports without PortFast."
                ),
            },
            {
                "id": "c",
                "text": "spanning-tree bpduguard enable",
                "correct": False,
                "rationale": (
                    "Incorrect. 'spanning-tree bpduguard enable' is an interface-level command, "
                    "not a global command. It enables BPDU Guard only on the specific interface "
                    "where it is entered, not globally."
                ),
            },
            {
                "id": "d",
                "text": "spanning-tree portfast default bpduguard",
                "correct": False,
                "rationale": (
                    "Incorrect. The valid command syntax is 'spanning-tree portfast bpduguard default', "
                    "not 'spanning-tree portfast default bpduguard'. Keyword order matters in Cisco IOS."
                ),
            },
        ],
        "explanation": (
            "Two global PortFast/BPDU Guard commands: 'spanning-tree portfast default' enables "
            "PortFast on all non-trunk access ports. 'spanning-tree portfast bpduguard default' "
            "enables BPDU Guard on all ports that have PortFast active. These are separate commands "
            "and can be used together. Interface-level commands ('spanning-tree portfast', "
            "'spanning-tree bpduguard enable') override or supplement global settings."
        ),
    },
    # -------------------------------------------------------------------------
    # 2.6 – Wireless architectures & AP modes
    # -------------------------------------------------------------------------
    {
        "id": "cd2v3-021",
        "domain": 2,
        "objective": "2.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Wireless architectures & AP modes",
        "stem": (
            "A wireless engineer needs to deploy an AP that will be used exclusively for RF "
            "spectrum analysis and detecting rogue APs and clients. The AP should NOT serve "
            "any wireless clients. Which AP mode should be configured?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Sniffer mode",
                "correct": False,
                "rationale": (
                    "Incorrect. Sniffer mode captures 802.11 frames and forwards them to a protocol "
                    "analyzer (e.g., Wireshark/OmniPeek). While it is a passive mode, it is designed "
                    "for packet capture, not for rogue detection and RF spectrum analysis."
                ),
            },
            {
                "id": "b",
                "text": "Monitor mode",
                "correct": True,
                "rationale": (
                    "Correct. Monitor mode dedicates the AP to passive scanning. It does not serve "
                    "wireless clients. The AP continuously scans all channels, detecting rogue APs, "
                    "rogue clients, and ad hoc networks, and reporting to the WLC for WIPS (Wireless "
                    "Intrusion Prevention System) functions."
                ),
            },
            {
                "id": "c",
                "text": "FlexConnect mode",
                "correct": False,
                "rationale": (
                    "Incorrect. FlexConnect mode is for branch office APs that need to serve clients "
                    "locally even when the WLC is unreachable. It actively serves wireless clients "
                    "and does not perform dedicated monitoring."
                ),
            },
            {
                "id": "d",
                "text": "Local mode with WIPS enabled",
                "correct": False,
                "rationale": (
                    "Incorrect. Local mode APs serve clients and also perform off-channel scanning "
                    "during brief intervals (RRM). However, if the requirement is exclusively for "
                    "monitoring with no client service, Monitor mode is the correct answer. Local "
                    "mode primarily serves clients."
                ),
            },
        ],
        "explanation": (
            "Cisco lightweight AP modes: Local (default, serves clients + brief off-channel scanning); "
            "Monitor (passive scanning only, no client service, used for WIPS/rogue detection); "
            "Sniffer (captures 802.11 frames, sends to protocol analyzer, no client service); "
            "FlexConnect (branch AP with local switching capability); Bridge (wireless bridge/mesh); "
            "SE-Connect (CleanAir spectrum analysis). Monitor mode is the correct choice for "
            "dedicated WIPS and rogue detection deployments."
        ),
    },
    {
        "id": "cd2v3-022",
        "domain": 2,
        "objective": "2.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Wireless architectures & AP modes",
        "stem": (
            "A company is expanding its wireless network and needs to provide outdoor wireless "
            "coverage between two buildings approximately 500 meters apart. No wired cabling "
            "can be run between buildings. Which AP mode is designed for this use case?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Autonomous mode with WDS (Wireless Distribution System)",
                "correct": False,
                "rationale": (
                    "Incorrect. While WDS on autonomous APs can create wireless bridges, the question "
                    "is about Cisco lightweight AP modes. The correct lightweight AP mode for wireless "
                    "bridging between buildings is Bridge mode."
                ),
            },
            {
                "id": "b",
                "text": "Bridge mode (outdoor mesh/bridge)",
                "correct": True,
                "rationale": (
                    "Correct. Cisco lightweight AP Bridge mode (also called outdoor bridge mode) "
                    "creates point-to-point or point-to-multipoint wireless links between locations. "
                    "It is designed for building-to-building connectivity without physical cabling, "
                    "using directional antennas for long-range links."
                ),
            },
            {
                "id": "c",
                "text": "FlexConnect mode with local switching",
                "correct": False,
                "rationale": (
                    "Incorrect. FlexConnect is for branch office APs serving wireless clients with "
                    "local switching when WLC connectivity is unreliable. It is not designed to "
                    "create wireless bridges between buildings."
                ),
            },
            {
                "id": "d",
                "text": "Monitor mode with CAPWAP tunneling",
                "correct": False,
                "rationale": (
                    "Incorrect. Monitor mode is for passive RF scanning and WIPS. It does not forward "
                    "data traffic and cannot create a building-to-building wireless link."
                ),
            },
        ],
        "explanation": (
            "Cisco lightweight AP Bridge mode creates wireless infrastructure links: point-to-point "
            "(two APs linking two buildings) or point-to-multipoint (one root bridge AP to multiple "
            "non-root bridge APs). Mesh mode extends this for multi-hop outdoor coverage. Bridge "
            "mode APs are typically deployed with directional antennas and operate under WLC management. "
            "Not to be confused with 'WGB' (Workgroup Bridge) mode for connecting wired-only clients."
        ),
    },
    {
        "id": "cd2v3-023",
        "domain": 2,
        "objective": "2.6",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Wireless architectures & AP modes",
        "stem": (
            "A lightweight AP in Local mode is connected to an access switch. The AP receives "
            "its IP address from DHCP option 43 pointing to the WLC IP. The AP successfully "
            "joins the WLC and begins serving clients. A client associates and is assigned "
            "VLAN 30 (192.168.30.0/24). Which statement accurately describes the data path "
            "for this client's traffic in Local mode?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Client traffic is tunneled via CAPWAP (UDP 5247) from the AP to the WLC, "
                    "where it exits onto the wired network in VLAN 30."
                ),
                "correct": True,
                "rationale": (
                    "Correct. In Local mode, all client data traffic is encapsulated in CAPWAP data "
                    "tunnels (UDP 5247) between the AP and the WLC. The WLC de-encapsulates the "
                    "traffic and forwards it onto the wired network in the appropriate VLAN "
                    "(VLAN 30) via its distribution system interface. The AP does NOT switch "
                    "client traffic locally."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Client traffic is switched locally at the AP directly into VLAN 30 on the "
                    "access switch, bypassing the WLC for data forwarding."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Local switching (traffic switched at the AP without going through "
                    "the WLC) is a feature of FlexConnect mode, not Local mode. In Local mode, "
                    "ALL client data traverses the CAPWAP tunnel to the WLC."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Client traffic is forwarded natively on the wired network as VLAN 30 tagged "
                    "frames directly from the AP's Ethernet port."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Lightweight APs in Local mode do not forward VLAN-tagged client "
                    "frames directly onto the wired network. The AP encapsulates client traffic "
                    "in CAPWAP and sends it to the WLC. The access switch port connecting to the "
                    "AP is typically an access port (or trunk with AP management VLAN)."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Client traffic is routed by the AP using its integrated IP routing table "
                    "before being forwarded to the WLC."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Lightweight APs do not perform IP routing. They are Layer 2 "
                    "devices that tunnel client frames to the WLC. All routing decisions are made "
                    "by the network infrastructure (Layer 3 switches, routers) after the WLC "
                    "delivers traffic to the wired network."
                ),
            },
        ],
        "explanation": (
            "In Cisco WLC Local mode (centralized switching), all client data is CAPWAP-tunneled "
            "(UDP 5247) to the WLC. The WLC maps each WLAN to a dynamic interface (VLAN) and "
            "forwards traffic onto the wired network via its distribution system port (trunk). "
            "The AP's wired uplink to the switch is typically an access port in the AP management "
            "VLAN. This centralized model enables consistent policy enforcement but requires "
            "sufficient WLC capacity and reliable WLC connectivity."
        ),
    },
    {
        "id": "cd2v3-024",
        "domain": 2,
        "objective": "2.6",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Wireless architectures & AP modes",
        "stem": (
            "Which TWO statements accurately describe the Cisco FlexConnect AP mode? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "In FlexConnect connected state, the AP can switch client traffic locally without sending it to the WLC.",
                "correct": True,
                "rationale": (
                    "Correct. FlexConnect mode supports local switching: client data is switched "
                    "directly at the AP into the local wired network, not tunneled to the WLC. "
                    "This reduces latency and WAN bandwidth consumption at branch sites."
                ),
            },
            {
                "id": "b",
                "text": "In FlexConnect standalone state (WLC unreachable), the AP cannot authenticate new clients under any circumstances.",
                "correct": False,
                "rationale": (
                    "Incorrect. FlexConnect can be configured with local authentication to continue "
                    "authenticating clients even when the WLC is unreachable. For PSK WLANs, the AP "
                    "can authenticate clients locally. For 802.1X WLANs, a local RADIUS server can "
                    "be configured for standalone authentication."
                ),
            },
            {
                "id": "c",
                "text": "FlexConnect requires the AP to be in the same Layer 2 domain as the WLC.",
                "correct": False,
                "rationale": (
                    "Incorrect. FlexConnect is specifically designed for APs at REMOTE sites separated "
                    "from the WLC by Layer 3 networks (WAN). The CAPWAP control tunnel traverses the "
                    "WAN. No Layer 2 adjacency to the WLC is required."
                ),
            },
            {
                "id": "d",
                "text": "FlexConnect groups allow multiple APs at the same site to share VLAN and ACL configurations and support local authentication.",
                "correct": True,
                "rationale": (
                    "Correct. FlexConnect groups are a WLC feature that groups multiple FlexConnect "
                    "APs at the same site. Groups enable shared local authentication databases, "
                    "consistent VLAN-to-WLAN mappings, and coordinated standalone behavior when "
                    "the WLC is unreachable."
                ),
            },
        ],
        "explanation": (
            "FlexConnect key features: (1) Local switching — client data stays at the branch, "
            "reducing WAN bandwidth; (2) Local authentication — branch APs can authenticate clients "
            "when WLC is down using cached credentials or local RADIUS; (3) FlexConnect groups — "
            "coordinate settings across multiple APs at the same site; (4) Works across Layer 3 WAN "
            "links — CAPWAP control plane traverses WAN for management. Compare to Local mode where "
            "all data and control go to WLC."
        ),
    },
    # -------------------------------------------------------------------------
    # 2.7 / 2.8 – WLC management access
    # -------------------------------------------------------------------------
    {
        "id": "cd2v3-025",
        "domain": 2,
        "objective": "2.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "WLC management access",
        "stem": (
            "A Cisco WLC has the following interfaces configured:\n\n"
            "  - Management interface: 192.168.1.10/24, VLAN 10\n"
            "  - AP-Manager interface: 192.168.1.11/24, VLAN 10\n"
            "  - Dynamic interface 'Corp': 192.168.20.1/24, VLAN 20\n\n"
            "The network engineer enables LAG on the WLC. What happens to the AP-Manager interface "
            "when LAG is enabled?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The AP-Manager interface is deleted; in LAG mode, the management interface handles AP CAPWAP traffic.",
                "correct": True,
                "rationale": (
                    "Correct. When LAG is enabled on a Cisco WLC, the AP-Manager interface is "
                    "removed. The management interface takes over AP CAPWAP control and data "
                    "functions. In non-LAG mode with multiple physical ports, multiple AP-Manager "
                    "interfaces can be created for load distribution. LAG eliminates this need by "
                    "bundling all ports into one logical link."
                ),
            },
            {
                "id": "b",
                "text": "The AP-Manager interface is moved to VLAN 20 to separate it from management traffic.",
                "correct": False,
                "rationale": (
                    "Incorrect. LAG does not change the VLAN assignment of any WLC interface. "
                    "The effect of LAG on the AP-Manager is its removal, not a VLAN reassignment."
                ),
            },
            {
                "id": "c",
                "text": "The AP-Manager interface stays active but is now load-balanced across all LAG member ports.",
                "correct": False,
                "rationale": (
                    "Incorrect. The AP-Manager interface is deleted when LAG is enabled, not "
                    "preserved. The management interface absorbs its functions."
                ),
            },
            {
                "id": "d",
                "text": "The AP-Manager interface requires a separate VLAN when LAG is enabled.",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no AP-Manager interface at all when LAG is enabled on a "
                    "Cisco WLC. The management interface handles all AP communication."
                ),
            },
        ],
        "explanation": (
            "Cisco WLC LAG behavior: When LAG is enabled, all physical ports are bundled and only "
            "ONE AP-Manager interface exists — actually the AP-Manager is removed and the management "
            "interface handles AP CAPWAP. In non-LAG mode, you can create multiple AP-Manager "
            "interfaces (one per physical port) for distributing AP load. Enabling/disabling LAG "
            "requires a WLC reboot to take effect."
        ),
    },
    {
        "id": "cd2v3-026",
        "domain": 2,
        "objective": "2.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "WLC management access",
        "stem": (
            "An engineer needs to verify which lightweight APs are currently joined to a Cisco WLC "
            "and check their operational status. Which WLC GUI navigation path provides this information?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Monitor > Summary",
                "correct": False,
                "rationale": (
                    "Incorrect. Monitor > Summary provides a high-level overview of the WLC including "
                    "client count, AP count, and alerts, but does not provide individual AP join status "
                    "and detailed operational state."
                ),
            },
            {
                "id": "b",
                "text": "Wireless > Access Points > All APs",
                "correct": True,
                "rationale": (
                    "Correct. In the Cisco WLC GUI, 'Wireless > Access Points > All APs' displays "
                    "the list of all joined APs with their name, MAC, IP, model, mode, status "
                    "(Registered/Not Joined), and associated controller. This is the primary location "
                    "for AP operational status verification."
                ),
            },
            {
                "id": "c",
                "text": "Security > AAA > RADIUS > Authentication",
                "correct": False,
                "rationale": (
                    "Incorrect. The Security > AAA section configures authentication servers for "
                    "client and management authentication. It does not show AP join status."
                ),
            },
            {
                "id": "d",
                "text": "Management > SNMP > Trap Receivers",
                "correct": False,
                "rationale": (
                    "Incorrect. The SNMP Trap Receivers page configures where the WLC sends SNMP "
                    "traps. It does not display AP join status or operational state."
                ),
            },
        ],
        "explanation": (
            "Cisco WLC GUI navigation for key tasks: AP join status = Wireless > Access Points > "
            "All APs; WLAN configuration = WLANs; Client status = Monitor > Clients; "
            "RF information = Monitor > Cisco CleanAir or Monitor > Rogues; "
            "Management access settings = Management > Summary. "
            "Knowing the WLC GUI navigation is directly tested on the CCNA exam."
        ),
    },
    {
        "id": "cd2v3-027",
        "domain": 2,
        "objective": "2.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "WLC management access",
        "stem": (
            "A network administrator wants to prevent unauthorized access to the Cisco WLC web GUI "
            "by restricting management access to a specific subnet (10.10.10.0/24). "
            "Which WLC configuration feature accomplishes this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Configure a CPU ACL under Security > Access Control Lists and apply it to the management interface.",
                "correct": True,
                "rationale": (
                    "Correct. A CPU ACL (also called a Management Frame Protection ACL or controller "
                    "ACL) on the WLC restricts traffic destined for the WLC's CPU — including HTTP, "
                    "HTTPS, SSH, Telnet, and SNMP management traffic. It is applied globally to "
                    "control which source IP addresses can reach the WLC management plane."
                ),
            },
            {
                "id": "b",
                "text": "Configure a WLAN ACL on each SSID to block management traffic from wireless clients.",
                "correct": False,
                "rationale": (
                    "Incorrect. WLAN ACLs (also called FlexConnect ACLs or client policy ACLs) filter "
                    "traffic from wireless clients, not from wired management stations. They apply to "
                    "client data, not to WLC management access from the wired network."
                ),
            },
            {
                "id": "c",
                "text": "Enable RADIUS MAC filtering on the management interface to whitelist the admin workstation.",
                "correct": False,
                "rationale": (
                    "Incorrect. RADIUS MAC filtering is used to authenticate wireless clients based "
                    "on MAC address, not to restrict wired management access to the WLC. It does not "
                    "filter management plane access by subnet."
                ),
            },
            {
                "id": "d",
                "text": "Apply an interface ACL on the upstream switch's SVI for the WLC management VLAN.",
                "correct": False,
                "rationale": (
                    "Incorrect. While applying an ACL on the upstream switch can filter access to "
                    "the WLC management VLAN, the question asks about a WLC configuration feature. "
                    "The CPU ACL is the WLC-native mechanism for management access restriction."
                ),
            },
        ],
        "explanation": (
            "Cisco WLC CPU ACLs (configured under Security > Access Control Lists, then applied via "
            "Security > CPU Access Control List) restrict access to the WLC's management plane. "
            "They filter traffic destined for the WLC CPU including SSH, HTTPS, Telnet, SNMP, and "
            "CAPWAP control. A properly configured CPU ACL permits only management subnets and AP "
            "networks, denying all others. This is distinct from client traffic ACLs."
        ),
    },
    {
        "id": "cd2v3-028",
        "domain": 2,
        "objective": "2.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "WLC management access",
        "stem": (
            "An engineer is configuring a new Cisco WLC and runs the initial configuration wizard "
            "via the console. After completing the wizard, which interface type is created that "
            "provides the primary in-band management access to the WLC?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Service port interface",
                "correct": False,
                "rationale": (
                    "Incorrect. The service port interface is a dedicated out-of-band management "
                    "interface on a physically separate port. It is not the primary in-band "
                    "management interface and is not used for AP CAPWAP or regular data traffic."
                ),
            },
            {
                "id": "b",
                "text": "Management interface",
                "correct": True,
                "rationale": (
                    "Correct. The management interface is the WLC's primary in-band management "
                    "interface. It carries WLC GUI/SSH/SNMP access, AP CAPWAP control plane traffic, "
                    "and in LAG mode also AP data. It is configured during the initial setup wizard "
                    "with an IP address, subnet mask, default gateway, and VLAN assignment."
                ),
            },
            {
                "id": "c",
                "text": "Dynamic interface",
                "correct": False,
                "rationale": (
                    "Incorrect. Dynamic interfaces are user-defined interfaces that map WLANs to "
                    "VLANs. They carry wireless client data traffic, not WLC management traffic. "
                    "You create dynamic interfaces after initial setup for each WLAN/VLAN pair."
                ),
            },
            {
                "id": "d",
                "text": "AP-Manager interface",
                "correct": False,
                "rationale": (
                    "Incorrect. The AP-Manager interface handles AP CAPWAP join and data traffic "
                    "(in non-LAG mode), but it is not the primary management interface for "
                    "administrator access. The management interface serves both management "
                    "and (in LAG mode) AP traffic."
                ),
            },
        ],
        "explanation": (
            "Cisco WLC interface types: Management interface (primary in-band management + AP CAPWAP "
            "in LAG mode); AP-Manager interface (AP CAPWAP in non-LAG mode, one per physical port); "
            "Dynamic interfaces (one per WLAN/VLAN, carries wireless client data); Virtual interface "
            "(DHCP relay, web auth redirect, L3 roaming, uses non-routable IP like 1.1.1.1); "
            "Service port interface (out-of-band management on dedicated physical port)."
        ),
    },
    {
        "id": "cd2v3-029",
        "domain": 2,
        "objective": "2.8",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "WLC management access",
        "stem": (
            "Which TWO features does the Cisco WLC virtual interface support? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "DHCP relay agent for wireless clients",
                "correct": True,
                "rationale": (
                    "Correct. The WLC virtual interface acts as the DHCP relay agent for wireless "
                    "clients. It forwards DHCP requests from clients to the configured DHCP server. "
                    "The virtual interface IP (typically a non-routable address like 1.1.1.1) is "
                    "used as the gateway IP (giaddr) in relayed DHCP packets."
                ),
            },
            {
                "id": "b",
                "text": "Layer 3 web authentication redirect for guest clients",
                "correct": True,
                "rationale": (
                    "Correct. When Layer 3 web authentication is configured, the WLC virtual interface "
                    "IP is used as the redirect destination. Clients attempting to access the network "
                    "are redirected to the virtual interface address which presents the web login portal."
                ),
            },
            {
                "id": "c",
                "text": "Primary in-band management access for SSH and HTTPS GUI",
                "correct": False,
                "rationale": (
                    "Incorrect. Primary in-band management (SSH, HTTPS GUI) uses the management "
                    "interface, not the virtual interface. The virtual interface is not used for "
                    "administrator management access."
                ),
            },
            {
                "id": "d",
                "text": "AP CAPWAP tunnel termination point for all joined APs",
                "correct": False,
                "rationale": (
                    "Incorrect. AP CAPWAP tunnels terminate on the management interface (or AP-Manager "
                    "interface in non-LAG deployments). The virtual interface handles DHCP relay "
                    "and web auth, not AP join/CAPWAP."
                ),
            },
        ],
        "explanation": (
            "The WLC virtual interface serves two key functions: (1) DHCP relay — acts as the relay "
            "agent for wireless client DHCP requests; (2) Layer 3 web authentication — used as the "
            "redirect IP for guest captive portal. The virtual interface is assigned a non-routable "
            "IP (commonly 1.1.1.1 or 192.0.2.1) since it is not a real gateway; it is a logical "
            "function endpoint on the WLC."
        ),
    },
    # -------------------------------------------------------------------------
    # 2.9 – WLAN GUI configuration
    # -------------------------------------------------------------------------
    {
        "id": "cd2v3-030",
        "domain": 2,
        "objective": "2.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "WLAN GUI configuration",
        "stem": (
            "An engineer creates a new WLAN on a Cisco WLC for guest users. The SSID is 'Guest-WiFi', "
            "and the security should use Layer 3 web authentication with a redirect to an external "
            "web server. Which combination of WLC GUI settings is required?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Layer 2 Security: None; Layer 3 Security: Web Policy (Authentication), "
                    "with the external web server URL configured."
                ),
                "correct": True,
                "rationale": (
                    "Correct. For external web authentication (captive portal) on a guest WLAN: "
                    "Layer 2 Security is set to 'None' (open wireless, no WPA), and Layer 3 Security "
                    "is set to 'Web Policy' with 'Authentication' selected. The external web server "
                    "URL is configured in the Web Auth section. Clients associate openly then are "
                    "redirected to the captive portal for credentials."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Layer 2 Security: WPA+WPA2 with PSK; Layer 3 Security: Web Policy (Authentication). "
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Combining WPA2-PSK with web authentication is unusual for guest "
                    "deployments and would require clients to first enter a PSK, then authenticate "
                    "via web. Standard guest web auth uses Layer 2 Security: None (open SSID) "
                    "with Layer 3 web authentication."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Layer 2 Security: None; Layer 3 Security: IPsec with pre-shared key."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. IPsec with PSK under Layer 3 security is not a web authentication "
                    "mechanism. Web authentication for guest users uses the 'Web Policy' option under "
                    "Layer 3 security, not IPsec."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Layer 2 Security: WPA+WPA2 with 802.1X; Layer 3 Security: None. "
                    "Configure a RADIUS server with a guest account."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. WPA2 with 802.1X is enterprise authentication requiring certificate "
                    "or credential per user via RADIUS/EAP. It is not the typical mechanism for "
                    "guest web authentication. Web auth (Layer 3) provides a browser-based login "
                    "experience suitable for guests."
                ),
            },
        ],
        "explanation": (
            "Guest web authentication on Cisco WLC: Layer 2 Security = None (clients associate "
            "without WPA credentials), Layer 3 Security = Web Policy > Authentication. An internal "
            "or external web server URL can be specified. The WLC redirects unauthenticated clients "
            "to the portal via the virtual interface. After successful web login, the WLC places "
            "the client in the guest dynamic interface/VLAN."
        ),
    },
    {
        "id": "cd2v3-031",
        "domain": 2,
        "objective": "2.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "WLAN GUI configuration",
        "stem": (
            "On a Cisco WLC, an engineer configures WLAN ID 5 with SSID 'Corp-Voice' mapped to "
            "dynamic interface 'voice-vlan' (VLAN 40). The WLAN is enabled but wireless VoIP "
            "phones cannot receive IP addresses. Wired hosts in VLAN 40 get DHCP addresses "
            "successfully. What is the MOST likely WLC configuration issue?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The WLAN needs to be mapped to the management interface instead of a dynamic interface.",
                "correct": False,
                "rationale": (
                    "Incorrect. WLANs should be mapped to dynamic interfaces (one per VLAN), not the "
                    "management interface. Mapping all WLANs to the management interface is a "
                    "misconfiguration that would mix wireless client traffic with management traffic."
                ),
            },
            {
                "id": "b",
                "text": "The DHCP server IP address is not configured on the dynamic interface 'voice-vlan' on the WLC.",
                "correct": True,
                "rationale": (
                    "Correct. Each WLC dynamic interface must have the DHCP server IP address "
                    "configured so the WLC virtual interface can relay DHCP requests from wireless "
                    "clients in that VLAN to the correct DHCP server. Without this, DHCP relay fails "
                    "and wireless clients cannot obtain IP addresses even if wired clients in the "
                    "same VLAN use a local switch relay or direct DHCP."
                ),
            },
            {
                "id": "c",
                "text": "The WLAN must use WPA2-PSK for VoIP phones; open security prevents DHCP from working.",
                "correct": False,
                "rationale": (
                    "Incorrect. Security mode (WPA2-PSK, 802.1X, or open) has no bearing on DHCP "
                    "functionality. A phone can fail to get DHCP regardless of security configuration "
                    "if the DHCP relay is not properly set up on the WLC dynamic interface."
                ),
            },
            {
                "id": "d",
                "text": "The QoS profile must be set to 'Platinum' before DHCP is allowed on voice WLANs.",
                "correct": False,
                "rationale": (
                    "Incorrect. QoS profiles control traffic prioritization and have no relationship "
                    "to DHCP functionality. DHCP operates at Layer 3 and is independent of QoS marking."
                ),
            },
        ],
        "explanation": (
            "Cisco WLC dynamic interface configuration requires the DHCP server IP to be specified "
            "so the WLC can relay DHCP Discover/Request packets from wireless clients to the DHCP "
            "server. The WLC virtual interface acts as the relay agent (giaddr in DHCP packets). "
            "Without the DHCP server IP on the dynamic interface, DHCP relay fails silently. "
            "Configure under: Controller > Interfaces > [interface name] > DHCP Server IP Address."
        ),
    },
    {
        "id": "cd2v3-032",
        "domain": 2,
        "objective": "2.9",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "WLAN GUI configuration",
        "stem": (
            "A wireless engineer configures a new WLAN on a Cisco WLC and enables 'Band Select'. "
            "A client that supports both 2.4 GHz and 5 GHz bands associates to the 2.4 GHz radio "
            "immediately. Which statement BEST explains why Band Select did not steer the client "
            "to 5 GHz?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Band Select only works with WPA3; the WLAN must be upgraded from WPA2 to use it.",
                "correct": False,
                "rationale": (
                    "Incorrect. Band Select is independent of the security configuration and works "
                    "with WPA2, WPA3, open, and other security modes. It is an RF management feature, "
                    "not a security feature."
                ),
            },
            {
                "id": "b",
                "text": "Band Select works by suppressing 2.4 GHz probe responses; the client may have sent only one probe before associating, not reaching the suppression threshold.",
                "correct": True,
                "rationale": (
                    "Correct. Band Select works by suppressing (delaying) probe responses on 2.4 GHz "
                    "for dual-band capable clients, hoping they will associate to 5 GHz instead. "
                    "It requires the client to send multiple probe requests to identify it as dual-band. "
                    "If the client sends only a single probe or associates very quickly, Band Select "
                    "may not have time to steer it. Also, Band Select cannot force clients; it can "
                    "only delay 2.4 GHz responses."
                ),
            },
            {
                "id": "c",
                "text": "Band Select requires the AP to have a third radio dedicated to band steering; without it, the feature is inactive.",
                "correct": False,
                "rationale": (
                    "Incorrect. Band Select is a software-based feature that works on standard dual-band "
                    "APs by manipulating probe responses. No additional hardware or third radio is required."
                ),
            },
            {
                "id": "d",
                "text": "Band Select requires both radios to use the same SSID; configuring separate SSIDs per band disables it.",
                "correct": False,
                "rationale": (
                    "Incorrect. Band Select works when both radios broadcast the same SSID, which is "
                    "the typical WLC configuration. Separate SSIDs per band would simply allow clients "
                    "to choose by SSID, which is a different approach. The failure is due to client "
                    "probe behavior, not SSID configuration."
                ),
            },
        ],
        "explanation": (
            "Cisco Band Select (also called Band Steering on some vendors) uses probe response "
            "suppression on 2.4 GHz to encourage dual-band clients to join 5 GHz. The WLC tracks "
            "how many times a client probes on 2.4 GHz; only after meeting a threshold does it "
            "suppress 2.4 GHz responses. Limitations: (1) clientsmust send multiple probes, "
            "(2) clients ultimately choose which band to use, (3) it only works at association "
            "time — once associated it has no effect. Configure under: WLAN > Advanced > Band Select."
        ),
    },
    {
        "id": "cd2v3-033",
        "domain": 2,
        "objective": "2.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "WLAN GUI configuration",
        "stem": (
            "On a Cisco WLC, an engineer navigates to WLANs > Edit > Security > Layer 2 and "
            "selects 'WPA+WPA2'. Under Auth Key Mgmt, which option must be selected to support "
            "clients using a shared passphrase (no 802.1X RADIUS server)?"
        ),
        "options": [
            {
                "id": "a",
                "text": "802.1X",
                "correct": False,
                "rationale": (
                    "Incorrect. 802.1X requires a RADIUS server for per-user/device authentication "
                    "using EAP. It does not use a shared passphrase. Selecting 802.1X would prevent "
                    "clients using a PSK from associating."
                ),
            },
            {
                "id": "b",
                "text": "PSK (Pre-Shared Key)",
                "correct": True,
                "rationale": (
                    "Correct. Under Auth Key Mgmt, selecting 'PSK' enables WPA2-Personal mode. "
                    "A shared passphrase is configured on the WLC and must be entered by connecting "
                    "clients. No RADIUS server is required. The WLC derives the Pairwise Master Key "
                    "from the passphrase during the 4-way handshake."
                ),
            },
            {
                "id": "c",
                "text": "CCKM (Cisco Centralized Key Management)",
                "correct": False,
                "rationale": (
                    "Incorrect. CCKM is a Cisco-proprietary fast re-authentication mechanism for "
                    "roaming clients that already have 802.1X credentials. It is not a replacement "
                    "for 802.1X/RADIUS and does not support PSK-based authentication."
                ),
            },
            {
                "id": "d",
                "text": "FT (Fast Transition / 802.11r)",
                "correct": False,
                "rationale": (
                    "Incorrect. 802.11r Fast Transition is a roaming optimization that speeds up "
                    "re-authentication when clients roam between APs. It can work with PSK or 802.1X "
                    "but it is not the authentication method itself — it is an enhancement to the "
                    "key exchange during roaming."
                ),
            },
        ],
        "explanation": (
            "WLC WLAN Security Layer 2 options: WPA+WPA2 with Auth Key Mgmt = PSK (WPA2-Personal, "
            "shared passphrase); Auth Key Mgmt = 802.1X (WPA2-Enterprise, RADIUS/EAP). PSK mode "
            "requires entering the passphrase in the WLC (minimum 8 characters, up to 63 for "
            "ASCII or 64 hex). No RADIUS server is needed. 802.1X requires RADIUS under "
            "Security > AAA > RADIUS > Authentication."
        ),
    },
    # -------------------------------------------------------------------------
    # Mixed objectives – final 7 questions to complete 40 total
    # -------------------------------------------------------------------------
    {
        "id": "cd2v3-034",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "STP port roles & states",
        "stem": (
            "In a Rapid PVST+ topology, SW2's Gi0/1 is a root port in forwarding state. "
            "An engineer connects a new switch SW4 to SW2's Gi0/2, and SW4's bridge ID is "
            "better than SW2's for VLAN 1 but worse than the current root's. "
            "What STP port role will SW2's Gi0/2 take after reconvergence?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Root port, because SW4 offers a better path to the current root than SW2's Gi0/1.",
                "correct": False,
                "rationale": (
                    "Incorrect. SW4's bridge ID is worse than the current root's bridge ID. Therefore, "
                    "SW4 does not provide a better path to the current root; the current root is still "
                    "reached via SW2's Gi0/1. Gi0/2 will not become a root port."
                ),
            },
            {
                "id": "b",
                "text": "Designated port, because SW2 is providing the best path to the root for the segment connecting to SW4.",
                "correct": True,
                "rationale": (
                    "Correct. After reconvergence, SW2's Gi0/2 becomes a designated port for the "
                    "segment between SW2 and SW4. SW2 has a better (lower) root path cost than SW4 "
                    "on that segment (SW2 is closer to the root than SW4). The designated port on "
                    "each segment is the switch port with the lowest root path cost to the root bridge."
                ),
            },
            {
                "id": "c",
                "text": "Alternate port, because SW4 sends BPDUs with a superior bridge ID on Gi0/2.",
                "correct": False,
                "rationale": (
                    "Incorrect. An alternate port receives a superior BPDU — meaning a BPDU with a "
                    "better path to the root than the local port can offer. SW4 has a worse bridge ID "
                    "than the current root; SW4's BPDUs are not superior to what SW2 already knows "
                    "about the root. SW2's Gi0/2 will be designated, not alternate."
                ),
            },
            {
                "id": "d",
                "text": "Backup port, because Gi0/2 is a second port on SW2 on the same network segment as Gi0/1.",
                "correct": False,
                "rationale": (
                    "Incorrect. A backup port exists when a switch has two ports on the SAME segment "
                    "(e.g., two ports connected to the same hub). Gi0/1 and Gi0/2 connect to different "
                    "switches/segments (root bridge and SW4), so a backup port role does not apply here."
                ),
            },
        ],
        "explanation": (
            "STP designated port election: on each network segment, the port with the lowest root "
            "path cost is the designated port. SW2 is closer to the root than SW4 (SW2's root path "
            "cost is lower). On the segment between SW2 and SW4, SW2's Gi0/2 becomes the designated "
            "port (forwarding) and SW4's connecting port becomes the root port (SW4 uses SW2 as its "
            "path to the root). SW4 cannot be root because its bridge ID is worse than the current root."
        ),
    },
    {
        "id": "cd2v3-035",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Spanning Tree (RPVST+)",
        "stem": (
            "Which TWO characteristics distinguish Rapid PVST+ from classic 802.1D PVST+? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Rapid PVST+ uses a proposal/agreement handshake to rapidly transition edge ports to forwarding state without timers.",
                "correct": True,
                "rationale": (
                    "Correct. Rapid PVST+ (RSTP) uses a proposal/agreement mechanism between adjacent "
                    "switches. When a port is elected designated, it sends a Proposal; the downstream "
                    "switch responds with an Agreement after synchronizing its ports. This allows rapid "
                    "forwarding state transitions without waiting for Forward Delay timers."
                ),
            },
            {
                "id": "b",
                "text": "Rapid PVST+ runs a separate STP instance per VLAN, while classic 802.1D PVST+ runs a single shared instance.",
                "correct": False,
                "rationale": (
                    "Incorrect. Both Rapid PVST+ and classic PVST+ run per-VLAN STP instances. "
                    "The 'PVST+' in both names stands for Per-VLAN Spanning Tree Plus. The difference "
                    "is the convergence mechanism (RSTP vs. classic 802.1D timers), not the per-VLAN "
                    "instance model."
                ),
            },
            {
                "id": "c",
                "text": "Rapid PVST+ generates and processes its own BPDUs on every port every Hello interval, instead of only forwarding BPDUs from the root.",
                "correct": True,
                "rationale": (
                    "Correct. In RSTP, every switch generates and sends BPDUs on all designated ports "
                    "every Hello interval (2 seconds), regardless of whether it is the root bridge. "
                    "In classic 802.1D, only the root generates BPDUs; non-root switches relay them. "
                    "This per-port BPDU generation enables faster failure detection."
                ),
            },
            {
                "id": "d",
                "text": "Rapid PVST+ uses 802.1Q for VLAN tagging on trunks, while classic PVST+ requires ISL encapsulation.",
                "correct": False,
                "rationale": (
                    "Incorrect. Both Rapid PVST+ and classic PVST+ support 802.1Q trunk encapsulation. "
                    "ISL is a deprecated protocol and is not required by either STP variant. "
                    "Encapsulation type is a trunk configuration choice, not tied to STP version."
                ),
            },
        ],
        "explanation": (
            "Key RSTP/Rapid PVST+ improvements over classic 802.1D: (1) Proposal/agreement handshake "
            "replaces Forward Delay timers for fast state transitions; (2) Each switch generates its "
            "own BPDUs every Hello (vs. only root in 802.1D), enabling rapid failure detection after "
            "3x Hello (6s); (3) Three port states (Discarding, Learning, Forwarding) vs. five in "
            "802.1D; (4) New port roles: Alternate and Backup for pre-calculated failover paths."
        ),
    },
    {
        "id": "cd2v3-036",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Trunking & 802.1Q",
        "stem": (
            "A switch has the following trunk configuration:\n\n"
            "  switchport trunk allowed vlan 10,20,30,40\n"
            "  switchport trunk native vlan 99\n\n"
            "An engineer issues:\n"
            "  switchport trunk allowed vlan remove 20\n\n"
            "A host in VLAN 20 connected to this switch's access port now cannot reach hosts "
            "in VLAN 20 on a remote switch. Hosts in VLANs 10, 30, and 40 are unaffected. "
            "What exactly occurred?"
        ),
        "options": [
            {
                "id": "a",
                "text": "VLAN 20 was deleted from the VLAN database by the 'remove' command.",
                "correct": False,
                "rationale": (
                    "Incorrect. 'switchport trunk allowed vlan remove 20' removes VLAN 20 only from "
                    "the trunk's allowed VLAN list. It does NOT delete VLAN 20 from the VLAN database. "
                    "Local VLAN 20 access ports still work within the same switch."
                ),
            },
            {
                "id": "b",
                "text": "VLAN 20 tagged frames are no longer forwarded across this trunk; VLAN 20 traffic is limited to this switch only.",
                "correct": True,
                "rationale": (
                    "Correct. Removing VLAN 20 from the trunk's allowed VLAN list means VLAN 20 "
                    "tagged frames will not traverse this trunk to remote switches. Local VLAN 20 "
                    "devices on the same switch can still communicate with each other (VLAN 20 "
                    "still exists in the VLAN database), but remote VLAN 20 hosts are unreachable."
                ),
            },
            {
                "id": "c",
                "text": "All VLANs are now blocked on the trunk because 'remove' without 'add' resets the allowed list to none.",
                "correct": False,
                "rationale": (
                    "Incorrect. The 'remove' keyword removes only the specified VLAN(s) from the "
                    "allowed list. It does not reset the entire list. VLANs 10, 30, and 40 remain "
                    "in the allowed list, which is why their connectivity is unaffected."
                ),
            },
            {
                "id": "d",
                "text": "The native VLAN changed to VLAN 20 as a result of removing it from the allowed list.",
                "correct": False,
                "rationale": (
                    "Incorrect. The native VLAN is set separately with 'switchport trunk native vlan' "
                    "and is not affected by changes to the allowed VLAN list. The native VLAN remains "
                    "VLAN 99 as configured."
                ),
            },
        ],
        "explanation": (
            "The 'switchport trunk allowed vlan remove X' command removes VLAN X from the trunk's "
            "allowed VLAN list without affecting the VLAN database or other port configurations. "
            "After removal, tagged VLAN X frames will not be forwarded or received on this trunk. "
            "Hosts in VLAN X on the same switch can still communicate locally (via Layer 2 switching) "
            "but cannot reach hosts in VLAN X on other switches connected via this trunk."
        ),
    },
    {
        "id": "cd2v3-037",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "VLANs",
        "stem": (
            "A network engineer needs to verify which VLANs are currently active and which switch "
            "ports belong to each VLAN. Which command provides a concise summary of this information "
            "on a Cisco IOS switch?"
        ),
        "options": [
            {
                "id": "a",
                "text": "show vlan brief",
                "correct": True,
                "rationale": (
                    "Correct. 'show vlan brief' displays a concise table listing each active VLAN, "
                    "its name, status (active/suspended/act/unsupported), and the access ports "
                    "assigned to it. It provides exactly the information needed to verify VLAN "
                    "existence and port membership."
                ),
            },
            {
                "id": "b",
                "text": "show interfaces vlan",
                "correct": False,
                "rationale": (
                    "Incorrect. 'show interfaces vlan X' shows the SVI (Layer 3 virtual interface) "
                    "status for a specific VLAN, including IP address and line protocol state. "
                    "It does not show which physical ports belong to a VLAN."
                ),
            },
            {
                "id": "c",
                "text": "show interfaces trunk",
                "correct": False,
                "rationale": (
                    "Incorrect. 'show interfaces trunk' shows trunk port details including allowed "
                    "VLANs, pruned VLANs, and active VLANs on trunk ports. It does not show the "
                    "port-to-VLAN assignment for access ports."
                ),
            },
            {
                "id": "d",
                "text": "show spanning-tree vlan",
                "correct": False,
                "rationale": (
                    "Incorrect. 'show spanning-tree vlan X' shows STP topology information for a "
                    "specific VLAN including root bridge, port roles, and port states. It does not "
                    "provide a summary of which ports are in which VLAN."
                ),
            },
        ],
        "explanation": (
            "'show vlan brief' is the go-to command for a VLAN membership summary. Key fields: "
            "VLAN ID, Name, Status, Ports. Note: trunk ports do NOT appear in 'show vlan brief' "
            "output — only access ports are listed under their assigned VLAN. Trunk ports and their "
            "VLAN configuration are shown by 'show interfaces trunk'. Both commands are frequently "
            "needed for troubleshooting VLAN connectivity."
        ),
    },
    {
        "id": "cd2v3-038",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "EtherChannel",
        "stem": (
            "An engineer is configuring a trunk EtherChannel using LACP between SW1 and SW2. "
            "After entering 'channel-group 1 mode active' on both switches' member interfaces, "
            "the engineer issues 'show etherchannel 1 detail' and sees the port-channel is up "
            "but the trunk is not passing VLAN 100 traffic. 'show interfaces trunk' shows VLAN 100 "
            "is allowed and active. What is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "VLAN 100 is VTP-pruned from the EtherChannel trunk.",
                "correct": True,
                "rationale": (
                    "Correct. The output of 'show interfaces trunk' has four sections. If VLAN 100 "
                    "is in 'allowed and active' but NOT in 'VLANs in spanning tree forwarding state "
                    "and not pruned', VTP pruning or manual pruning has removed it. The port-channel "
                    "itself is up and the EtherChannel is formed, but VLAN 100 frames are being "
                    "pruned and not forwarded."
                ),
            },
            {
                "id": "b",
                "text": "The EtherChannel member interfaces have different native VLANs, causing VLAN 100 to drop.",
                "correct": False,
                "rationale": (
                    "Incorrect. Member interfaces within an EtherChannel bundle must have the same "
                    "native VLAN; if they differ, the bundle would not form or member ports would "
                    "be suspended. The stem states the port-channel is up, so native VLAN mismatch "
                    "between member ports is not the issue."
                ),
            },
            {
                "id": "c",
                "text": "LACP requires static VLAN configuration; VLAN 100 must be created on both switches before LACP bundles the link.",
                "correct": False,
                "rationale": (
                    "Incorrect. LACP is a link aggregation protocol and has no interaction with VLAN "
                    "creation or management. The EtherChannel is already up (as stated), and the "
                    "trunk shows VLAN 100 as active, meaning VLAN 100 exists on both switches."
                ),
            },
            {
                "id": "d",
                "text": "The Port-channel interface needs 'switchport trunk allowed vlan add 100' to pass VLAN 100.",
                "correct": False,
                "rationale": (
                    "Incorrect. The stem states 'show interfaces trunk' shows VLAN 100 as allowed and "
                    "active — meaning VLAN 100 IS in the allowed list. The issue is that it is pruned "
                    "from the 'forwarding and not pruned' list, not that it is missing from the "
                    "allowed list."
                ),
            },
        ],
        "explanation": (
            "When 'show interfaces trunk' shows a VLAN in 'allowed and active' but NOT in 'VLANs in "
            "spanning tree forwarding state and not pruned', the VLAN is being pruned. This can be "
            "VTP pruning (enabled on the VTP server) or manual pruning ('switchport trunk pruning "
            "vlan X'). Fix with 'switchport trunk pruning vlan remove 100' on the pruned trunk or "
            "review VTP pruning settings. The EtherChannel port-channel status is unrelated."
        ),
    },
    {
        "id": "cd2v3-039",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "CDP & LLDP",
        "stem": (
            "A network engineer issues 'show cdp neighbors detail' on a router and sees a neighbor "
            "with two IP addresses listed: 10.1.1.2 and 172.16.5.1. The interface connecting them "
            "is shown as 'FastEthernet0/0'. What does the presence of two IP addresses in the CDP "
            "neighbor entry indicate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The neighbor has two IP addresses configured on its FastEthernet0/0 interface (primary and secondary).",
                "correct": False,
                "rationale": (
                    "Incorrect. CDP advertises all IP addresses of the neighbor device, not just the "
                    "address of the specific connecting interface. The two addresses likely belong to "
                    "different interfaces on the neighbor device, not secondary IPs on one interface."
                ),
            },
            {
                "id": "b",
                "text": "The neighbor device has multiple interfaces with IP addresses configured, and CDP advertises all of them.",
                "correct": True,
                "rationale": (
                    "Correct. CDP includes all configured IP addresses of the neighbor device in its "
                    "advertisement, regardless of which interface connects the two devices. The entry "
                    "in 'show cdp neighbors detail' lists all IP addresses of the neighbor, allowing "
                    "network operators to know the full reachability of that device."
                ),
            },
            {
                "id": "c",
                "text": "The neighbor has HSRP configured with a virtual IP and a physical IP on the same interface.",
                "correct": False,
                "rationale": (
                    "Incorrect. CDP does not advertise HSRP virtual IP addresses. It advertises the "
                    "physical interface IP addresses of the device. HSRP virtual IPs are not included "
                    "in CDP advertisements."
                ),
            },
            {
                "id": "d",
                "text": "The neighbor is dual-stacked (IPv4 and IPv6), and CDP is displaying both address families.",
                "correct": False,
                "rationale": (
                    "Incorrect. Both addresses shown (10.1.1.2 and 172.16.5.1) are IPv4 addresses. "
                    "While CDP does advertise IPv6 addresses via CDPv2, the scenario shows two IPv4 "
                    "addresses from different subnets, indicating different physical interfaces."
                ),
            },
        ],
        "explanation": (
            "CDP's 'show cdp neighbors detail' displays all IP addresses configured on the neighbor "
            "device across all interfaces. This is part of the CDP Address TLV which can contain "
            "multiple address entries. This is useful for discovering a device's full IP profile "
            "from a single neighbor entry. It is also a security concern — CDP reveals the complete "
            "IP addressing scheme of neighboring devices to any connected device."
        ),
    },
    {
        "id": "cd2v3-040",
        "domain": 2,
        "objective": "2.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "WLAN GUI configuration",
        "stem": (
            "A network engineer is using the Cisco WLC GUI to troubleshoot a wireless client "
            "that associated to an AP but is showing 'DHCP Required' status and cannot pass "
            "traffic. The WLAN has 'DHCP Required' enabled under the Advanced tab. "
            "Which condition would cause this client state?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The client associated successfully and received an IP address via DHCP.",
                "correct": False,
                "rationale": (
                    "Incorrect. A client that received an IP address via DHCP would be in 'RUN' state, "
                    "not 'DHCP Required'. The DHCP Required state persists until the WLC sees the "
                    "client obtain a DHCP-assigned IP address."
                ),
            },
            {
                "id": "b",
                "text": "The client associated but configured a static IP address instead of using DHCP, and 'DHCP Required' is enabled on the WLAN.",
                "correct": True,
                "rationale": (
                    "Correct. When 'DHCP Required' is enabled on a WLAN, the WLC requires clients "
                    "to obtain an IP address via DHCP before allowing them to pass traffic. A client "
                    "configured with a static IP will remain in 'DHCP Required' state because the "
                    "WLC never sees a DHCP ACK for that client, blocking all client data traffic."
                ),
            },
            {
                "id": "c",
                "text": "The client failed 802.1X authentication and is placed in DHCP quarantine.",
                "correct": False,
                "rationale": (
                    "Incorrect. 802.1X authentication failure would prevent the client from "
                    "associating to the WLAN at all (it would show authentication failure, not "
                    "'DHCP Required'). The 'DHCP Required' state applies to a client that has "
                    "already successfully associated and authenticated."
                ),
            },
            {
                "id": "d",
                "text": "The DHCP server is unreachable and the client is waiting for an IP address.",
                "correct": False,
                "rationale": (
                    "Incorrect. If the DHCP server is unreachable, the client would attempt DHCP "
                    "and eventually time out (potentially self-assigning a 169.254.x.x APIPA address). "
                    "The 'DHCP Required' status on the WLC means the WLC has not seen a DHCP lease "
                    "for this client — most commonly caused by a client using a static IP."
                ),
            },
        ],
        "explanation": (
            "The Cisco WLC 'DHCP Required' WLAN setting (Advanced tab) forces clients to obtain an "
            "IP via DHCP before being allowed to pass traffic. The WLC monitors DHCP traffic and "
            "transitions the client from 'DHCP Required' to 'RUN' state only after observing a "
            "successful DHCP ACK. Clients with static IPs never satisfy this requirement and are "
            "permanently blocked on WLANs with this setting enabled. Disable 'DHCP Required' or "
            "configure DHCP on the client to resolve."
        ),
    },
]


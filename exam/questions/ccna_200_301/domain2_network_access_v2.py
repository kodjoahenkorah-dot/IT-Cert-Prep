"""
CCNA 200-301 – Domain 2: Network Access  (Version 2)
38 brand-new practice questions covering objectives 2.1 – 2.9.
IDs: cd2v2-001 through cd2v2-038
"""

QUESTIONS = [
    # -------------------------------------------------------------------------
    # 2.1 – VLANs
    # -------------------------------------------------------------------------
    {
        "id": "cd2v2-001",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "VLANs",
        "stem": (
            "A network engineer issues the following commands on SW1:\n\n"
            "  vlan 100\n"
            "   name FINANCE\n"
            "  interface range Gi0/1 - 4\n"
            "   switchport mode access\n"
            "   switchport access vlan 100\n\n"
            "Later, 'show vlan brief' shows ports Gi0/1–Gi0/4 listed under VLAN 1, not VLAN 100. "
            "Which condition MOST likely explains this output?"
        ),
        "options": [
            {
                "id": "a",
                "text": "VLAN 100 was created in the VLAN database but must also be created in the running-config with 'vlan database' before ports can join it.",
                "correct": False,
                "rationale": (
                    "Incorrect. On Cisco IOS switches, 'vlan 100' in global configuration mode creates "
                    "the VLAN and stores it in vlan.dat. There is no need for a separate 'vlan database' "
                    "step on modern IOS."
                ),
            },
            {
                "id": "b",
                "text": "The interfaces are currently in trunk mode operationally, so they do not appear in the access VLAN column of 'show vlan brief'.",
                "correct": True,
                "rationale": (
                    "Correct. 'show vlan brief' only lists ports that are in access mode. If the "
                    "interfaces negotiated to trunk (e.g., connected to another switch with DTP enabled), "
                    "they will not appear in the VLAN 100 column — they will show their trunk status in "
                    "'show interfaces trunk' instead. The ports may be physically in trunk mode even "
                    "though 'switchport mode access' was configured if DTP overrode the setting due to a race condition or prior config."
                ),
            },
            {
                "id": "c",
                "text": "The 'interface range' command applied only to Gi0/1; the remaining ports retained their previous configuration.",
                "correct": False,
                "rationale": (
                    "Incorrect. 'interface range Gi0/1 - 4' applies subsequent commands to all four "
                    "interfaces simultaneously. A syntax error would have produced an error message."
                ),
            },
            {
                "id": "d",
                "text": "VLAN 100 was pruned by VTP and therefore ports assigned to it revert to VLAN 1.",
                "correct": False,
                "rationale": (
                    "Incorrect. VTP pruning removes a VLAN from a trunk's forwarding list; it does not "
                    "reassign access ports from one VLAN to another. Ports would remain assigned to "
                    "VLAN 100 even if it were pruned on trunks."
                ),
            },
        ],
        "explanation": (
            "'show vlan brief' only displays ports in active access mode. If a port is operating as a "
            "trunk (regardless of its configured mode), it will not appear in the VLAN column for any "
            "access VLAN. Always cross-check with 'show interfaces trunk' and "
            "'show interfaces Gi0/x switchport' to see the operational mode versus the configured mode."
        ),
    },
    {
        "id": "cd2v2-002",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "VLANs",
        "stem": (
            "A Cisco Layer 3 switch has an SVI for VLAN 10 (ip address 10.1.10.1/24) and an SVI for "
            "VLAN 20 (ip address 10.1.20.1/24). 'ip routing' is enabled. A host in VLAN 10 pings a "
            "host in VLAN 20 but receives no reply. 'show ip route' on the switch shows directly "
            "connected routes for both subnets. 'show interfaces vlan 10' shows the SVI is up/up. "
            "'show interfaces vlan 20' shows the SVI is down/down. What is the MOST likely cause "
            "for VLAN 20's SVI being down/down?"
        ),
        "options": [
            {
                "id": "a",
                "text": "VLAN 20 does not exist in the VLAN database or has no active access/trunk port assigned to it.",
                "correct": True,
                "rationale": (
                    "Correct. An SVI comes up only when the corresponding VLAN exists in the VLAN "
                    "database AND at least one port is assigned to that VLAN in an up state (either "
                    "as an access port in VLAN 20, or a trunk carrying VLAN 20 that is in forwarding). "
                    "Without an active port in VLAN 20, the SVI stays down/down."
                ),
            },
            {
                "id": "b",
                "text": "The SVI IP address conflicts with another device on the network.",
                "correct": False,
                "rationale": (
                    "Incorrect. An IP address conflict would not cause the SVI to show down/down at "
                    "Layer 1/Layer 2. The SVI line protocol state depends on the VLAN's active ports, "
                    "not on IP address conflicts."
                ),
            },
            {
                "id": "c",
                "text": "'ip routing' was enabled after the SVIs were created, requiring a reload to activate VLAN 20's SVI.",
                "correct": False,
                "rationale": (
                    "Incorrect. 'ip routing' takes effect immediately without a reload. It does not "
                    "affect whether individual SVIs come up or stay down."
                ),
            },
            {
                "id": "d",
                "text": "The SVI for VLAN 20 must be assigned a secondary IP address in addition to the primary address.",
                "correct": False,
                "rationale": (
                    "Incorrect. Secondary IP addresses are optional and have no bearing on whether "
                    "an SVI's line protocol is up or down. The SVI state depends on VLAN membership."
                ),
            },
        ],
        "explanation": (
            "A Switched Virtual Interface (SVI) line protocol goes up only when: (1) the VLAN exists "
            "in the local VLAN database, and (2) at least one port in that VLAN (access port assigned "
            "to it, or a trunk port carrying and forwarding that VLAN) is in an 'up' state. "
            "If VLAN 20 is missing from vlan.dat or has no active member port, 'interface vlan 20' "
            "remains down/down and inter-VLAN routing cannot occur for that subnet."
        ),
    },
    {
        "id": "cd2v2-003",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "VLANs",
        "stem": (
            "A network engineer needs to configure router-on-a-stick inter-VLAN routing between "
            "VLAN 30 (172.16.30.0/24) and VLAN 40 (172.16.40.0/24) using a router connected to a "
            "switch via a single physical link. Which set of commands on the router correctly "
            "creates the subinterfaces?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "interface Gi0/0.30\n"
                    " encapsulation dot1q 30\n"
                    " ip address 172.16.30.1 255.255.255.0\n"
                    "interface Gi0/0.40\n"
                    " encapsulation dot1q 40\n"
                    " ip address 172.16.40.1 255.255.255.0"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Router-on-a-stick uses logical subinterfaces on a single physical "
                    "interface. Each subinterface is assigned an encapsulation matching the VLAN tag "
                    "('encapsulation dot1q <vlan-id>') and an IP address serving as the default "
                    "gateway for hosts in that VLAN."
                ),
            },
            {
                "id": "b",
                "text": (
                    "interface Gi0/0\n"
                    " ip address 172.16.30.1 255.255.255.0\n"
                    " ip address 172.16.40.1 255.255.255.0 secondary"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A physical interface with secondary IP addresses does not distinguish "
                    "between 802.1Q-tagged VLANs. Without subinterfaces and 'encapsulation dot1q', "
                    "the router cannot process frames tagged for different VLANs on the same port."
                ),
            },
            {
                "id": "c",
                "text": (
                    "interface Gi0/0.30\n"
                    " switchport access vlan 30\n"
                    " ip address 172.16.30.1 255.255.255.0\n"
                    "interface Gi0/0.40\n"
                    " switchport access vlan 40\n"
                    " ip address 172.16.40.1 255.255.255.0"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. 'switchport' commands are used on switch ports, not on router "
                    "subinterfaces. Routers use 'encapsulation dot1q' on subinterfaces to associate "
                    "them with a VLAN tag."
                ),
            },
            {
                "id": "d",
                "text": (
                    "interface Gi0/0.30\n"
                    " encapsulation isl 30\n"
                    " ip address 172.16.30.1 255.255.255.0\n"
                    "interface Gi0/0.40\n"
                    " encapsulation isl 40\n"
                    " ip address 172.16.40.1 255.255.255.0"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. ISL (Inter-Switch Link) is a deprecated Cisco-proprietary trunking "
                    "encapsulation. Modern Cisco routers and switches use 802.1Q ('encapsulation dot1q'). "
                    "Many current platforms do not support ISL at all."
                ),
            },
        ],
        "explanation": (
            "Router-on-a-stick requires: (1) the switch port connected to the router configured as "
            "an 802.1Q trunk, and (2) router subinterfaces with 'encapsulation dot1q <vlan-id>' and "
            "an IP address acting as the VLAN's default gateway. The subinterface number does not "
            "have to match the VLAN ID, but matching them is a universal best practice for clarity."
        ),
    },
    {
        "id": "cd2v2-004",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "VLANs",
        "stem": (
            "A switch running VTP version 2 in transparent mode has VLANs 1, 10, 20, and 99 in its "
            "VLAN database. A VTP server with revision number 30 sends a VTP summary advertisement "
            "containing VLANs 1, 10, and 50. What happens to the transparent switch's VLAN database?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The transparent switch adopts the VTP server's VLAN list; VLANs 20 and 99 are deleted and VLAN 50 is added.",
                "correct": False,
                "rationale": (
                    "Incorrect. A switch in VTP transparent mode does NOT synchronize its VLAN database "
                    "from VTP advertisements. It only forwards VTP frames out its trunks; it does not "
                    "apply them locally."
                ),
            },
            {
                "id": "b",
                "text": "The transparent switch's VLAN database is unchanged; it forwards the VTP advertisement out its trunks without applying it.",
                "correct": True,
                "rationale": (
                    "Correct. VTP transparent mode switches ignore VTP advertisements for local VLAN "
                    "database synchronization. They forward (pass through) VTP frames to neighboring "
                    "switches, but their own VLAN database is only modified by local configuration "
                    "commands. VLANs 1, 10, 20, and 99 remain unchanged."
                ),
            },
            {
                "id": "c",
                "text": "The transparent switch drops the VTP advertisement and does not forward it, isolating downstream switches from VTP.",
                "correct": False,
                "rationale": (
                    "Incorrect. Transparent mode switches forward VTP advertisements received on trunk "
                    "ports out to other trunk ports. They do not drop them. Only if VTP is completely "
                    "disabled (VTP off mode in v3) would frames be dropped."
                ),
            },
            {
                "id": "d",
                "text": "The transparent switch stores the VTP advertisement as a backup and applies it only if it transitions to client mode.",
                "correct": False,
                "rationale": (
                    "Incorrect. Transparent mode switches do not cache VTP advertisements. They forward "
                    "them immediately and ignore them for local processing."
                ),
            },
        ],
        "explanation": (
            "VTP transparent mode: the switch maintains its own independent VLAN database configured "
            "locally; it never synchronizes with VTP server advertisements. However, it does forward "
            "received VTP frames out its trunk ports (pass-through), allowing VTP to propagate to "
            "downstream switches. This is the key difference from VTP off mode (v3), which drops VTP "
            "frames entirely."
        ),
    },
    # -------------------------------------------------------------------------
    # 2.2 – Trunking & 802.1Q
    # -------------------------------------------------------------------------
    {
        "id": "cd2v2-005",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Trunking & 802.1Q",
        "stem": (
            "An engineer wants to permanently disable DTP on a trunk port and prevent the switch "
            "from sending DTP frames. The port is connected to a non-Cisco device that does not "
            "understand DTP. Which command accomplishes this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "switchport mode trunk",
                "correct": False,
                "rationale": (
                    "Incorrect. 'switchport mode trunk' sets the port to permanent trunk mode but "
                    "still allows DTP frames to be sent. The port continues sending DTP advertisements "
                    "unless 'switchport nonegotiate' is also configured."
                ),
            },
            {
                "id": "b",
                "text": "switchport mode trunk\n switchport nonegotiate",
                "correct": True,
                "rationale": (
                    "Correct. 'switchport mode trunk' forces the port into permanent trunk mode, and "
                    "'switchport nonegotiate' suppresses DTP frame transmission. Together they create "
                    "a static, silent trunk — the recommended configuration for ports connected to "
                    "non-Cisco devices or where DTP is unwanted."
                ),
            },
            {
                "id": "c",
                "text": "no dtp\n switchport mode trunk",
                "correct": False,
                "rationale": (
                    "Incorrect. 'no dtp' is not a valid Cisco IOS command. The correct command to "
                    "disable DTP negotiation is 'switchport nonegotiate'."
                ),
            },
            {
                "id": "d",
                "text": "switchport mode dynamic auto",
                "correct": False,
                "rationale": (
                    "Incorrect. 'dynamic auto' enables DTP negotiation in a passive mode. It would "
                    "not form a trunk with a non-Cisco device and would send DTP frames, which is "
                    "the opposite of what is needed."
                ),
            },
        ],
        "explanation": (
            "'switchport nonegotiate' disables DTP on a port that is already set to trunk or access "
            "mode. It is required when connecting to non-Cisco devices (which do not understand DTP) "
            "or as a security hardening measure to prevent unauthorized trunk negotiation. The port "
            "must already be in 'mode trunk' or 'mode access' before 'nonegotiate' is accepted."
        ),
    },
    {
        "id": "cd2v2-006",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Trunking & 802.1Q",
        "stem": (
            "SW1 Gi0/0 trunk port shows the following from 'show interfaces Gi0/0 trunk':\n\n"
            "  Vlans allowed on trunk: 1-4094\n"
            "  Vlans allowed and active in management domain: 1,10,30,40\n"
            "  Vlans in spanning tree forwarding state and not pruned: 1,10,40\n\n"
            "An engineer confirms that VLAN 30 exists on SW1 and SW2 (the far-end switch). "
            "Hosts in VLAN 30 on SW2 cannot reach hosts in VLAN 30 on SW1. "
            "What should the engineer check FIRST?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Whether VTP pruning has pruned VLAN 30 from this trunk link.",
                "correct": True,
                "rationale": (
                    "Correct. VLAN 30 appears in 'active in management domain' (it exists and is "
                    "active) but is absent from 'in spanning tree forwarding state and not pruned'. "
                    "This pattern indicates the VLAN is pruned — either by VTP pruning or manual "
                    "'switchport trunk pruning vlan'. The engineer should check VTP pruning state "
                    "and manually verify with 'show interfaces trunk' on both ends."
                ),
            },
            {
                "id": "b",
                "text": "Whether VLAN 30 is missing from the allowed VLAN list on the trunk.",
                "correct": False,
                "rationale": (
                    "Incorrect. The first line shows 'Vlans allowed on trunk: 1-4094', which includes "
                    "VLAN 30. It is permitted on the trunk."
                ),
            },
            {
                "id": "c",
                "text": "Whether the trunk encapsulation is ISL instead of dot1q, causing VLAN 30 to be dropped.",
                "correct": False,
                "rationale": (
                    "Incorrect. If the encapsulation were mismatched, all VLANs would be affected, "
                    "not just VLAN 30. VLANs 1, 10, and 40 are forwarding normally."
                ),
            },
            {
                "id": "d",
                "text": "Whether the native VLAN on this trunk is set to VLAN 30, causing traffic to be forwarded untagged.",
                "correct": False,
                "rationale": (
                    "Incorrect. VLAN 30 being the native VLAN would cause its traffic to be sent "
                    "untagged, but it would still be forwarded. The real problem indicated by the "
                    "output is pruning, not the native VLAN setting."
                ),
            },
        ],
        "explanation": (
            "Reading 'show interfaces trunk' output: a VLAN listed in the second section (allowed and "
            "active) but absent from the third section (forwarding and not pruned) is being pruned. "
            "VTP pruning dynamically removes VLANs from trunks that have no downstream members. "
            "Manual pruning via 'switchport trunk pruning vlan' also suppresses forwarding. "
            "To restore: either disable VTP pruning globally or add VLAN 30 to the manual pruning "
            "allow list with 'switchport trunk pruning vlan add 30'."
        ),
    },
    {
        "id": "cd2v2-007",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Trunking & 802.1Q",
        "stem": (
            "A Cisco switch port is configured as follows:\n\n"
            "  switchport mode dynamic auto\n\n"
            "The port is connected to another switch port also configured as 'switchport mode "
            "dynamic auto'. What will be the resulting port mode, and why?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The port will become a trunk because both sides support trunking.",
                "correct": False,
                "rationale": (
                    "Incorrect. 'dynamic auto' is passive — it waits for the other side to initiate "
                    "trunking. When both sides are passive (auto + auto), neither sends DTP frames "
                    "proposing a trunk, so the link defaults to access mode."
                ),
            },
            {
                "id": "b",
                "text": "The port will remain in access mode because neither side initiates trunk negotiation.",
                "correct": True,
                "rationale": (
                    "Correct. DTP 'dynamic auto' ports are passive — they only form a trunk if the "
                    "other side is in 'trunk' or 'dynamic desirable' mode. When both sides are auto, "
                    "neither initiates, and the link comes up as an access link."
                ),
            },
            {
                "id": "c",
                "text": "The port enters err-disabled because two auto ports cannot coexist.",
                "correct": False,
                "rationale": (
                    "Incorrect. Two 'dynamic auto' ports connect without error; they simply negotiate "
                    "to access mode. No err-disabled condition results from DTP negotiation."
                ),
            },
            {
                "id": "d",
                "text": "DTP negotiation fails and each port independently chooses trunk or access mode based on its CDP neighbors.",
                "correct": False,
                "rationale": (
                    "Incorrect. DTP negotiation does not involve CDP. When DTP negotiates with two "
                    "auto peers, it successfully negotiates — to access mode, because neither side "
                    "proposes a trunk."
                ),
            },
        ],
        "explanation": (
            "DTP mode outcome matrix — Auto+Auto = Access; Auto+Desirable = Trunk; "
            "Desirable+Desirable = Trunk; Trunk+Auto = Trunk; Trunk+Desirable = Trunk; "
            "Trunk+Access = Mismatch (trunk forms but may cause issues); On+On = Trunk (no DTP); "
            "Access+any = Access. The critical exam point: auto+auto does NOT form a trunk."
        ),
    },
    {
        "id": "cd2v2-008",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Trunking & 802.1Q",
        "stem": (
            "An engineer must ensure that the native VLAN is always tagged on a specific trunk link "
            "to prevent double-tagging VLAN hopping. Which IOS command achieves this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "switchport trunk native vlan tag",
                "correct": False,
                "rationale": (
                    "Incorrect. 'switchport trunk native vlan tag' is not a valid Cisco IOS interface "
                    "command. Native VLAN tagging is controlled globally."
                ),
            },
            {
                "id": "b",
                "text": "vlan dot1q tag native (global configuration command)",
                "correct": True,
                "rationale": (
                    "Correct. The global command 'vlan dot1q tag native' forces the switch to add an "
                    "802.1Q tag to native VLAN frames on all trunk ports. This prevents double-tagging "
                    "attacks because the first switch will no longer strip an outer tag matching the "
                    "native VLAN — instead, it will recognize and process the tag normally."
                ),
            },
            {
                "id": "c",
                "text": "switchport trunk native vlan 1 tagged",
                "correct": False,
                "rationale": (
                    "Incorrect. 'switchport trunk native vlan 1 tagged' is not valid Cisco IOS syntax. "
                    "The 'tagged' keyword does not exist in this command context."
                ),
            },
            {
                "id": "d",
                "text": "no switchport trunk native vlan",
                "correct": False,
                "rationale": (
                    "Incorrect. 'no switchport trunk native vlan' returns the native VLAN to the "
                    "default (VLAN 1). It does not enable tagging of native VLAN frames."
                ),
            },
        ],
        "explanation": (
            "The global IOS command 'vlan dot1q tag native' causes all trunk ports on the switch to "
            "tag native VLAN frames with an 802.1Q header. Without this command, native VLAN frames "
            "are forwarded untagged, enabling double-tagging attacks. This command is a security "
            "best practice and must match on both ends of the trunk link to function correctly."
        ),
    },
    # -------------------------------------------------------------------------
    # 2.3 – CDP & LLDP
    # -------------------------------------------------------------------------
    {
        "id": "cd2v2-009",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "CDP & LLDP",
        "stem": (
            "A network engineer discovers that a Cisco router is not appearing in the LLDP neighbor "
            "table of an adjacent switch, even though LLDP is globally enabled on both devices with "
            "'lldp run'. The physical link is up. Which per-interface command on the router's "
            "connecting interface would explain the missing LLDP neighbor entry on the switch?"
        ),
        "options": [
            {
                "id": "a",
                "text": "no lldp transmit",
                "correct": True,
                "rationale": (
                    "Correct. Even with 'lldp run' globally enabled, 'no lldp transmit' on the "
                    "interface prevents the router from sending LLDP frames out that interface. "
                    "The switch would never receive an LLDP frame from the router and thus the "
                    "router would not appear in the switch's LLDP neighbor table."
                ),
            },
            {
                "id": "b",
                "text": "no lldp receive",
                "correct": False,
                "rationale": (
                    "Incorrect. 'no lldp receive' stops the interface from processing incoming LLDP "
                    "frames. The router would still transmit LLDP frames to the switch, so the router "
                    "WOULD appear in the switch's LLDP neighbor table. The reverse (switch in router's "
                    "table) would be affected."
                ),
            },
            {
                "id": "c",
                "text": "no cdp enable",
                "correct": False,
                "rationale": (
                    "Incorrect. 'no cdp enable' disables CDP on the interface. CDP and LLDP are "
                    "independent protocols. Disabling CDP has no effect on LLDP operation."
                ),
            },
            {
                "id": "d",
                "text": "lldp holdtime 0",
                "correct": False,
                "rationale": (
                    "Incorrect. 'lldp holdtime' is a global timer (not per-interface) that controls "
                    "how long neighbors keep LLDP entries. Setting it to 0 would cause neighbors to "
                    "immediately age out entries, but the command syntax and behavior described do "
                    "not directly explain the missing entry in the way 'no lldp transmit' does."
                ),
            },
        ],
        "explanation": (
            "LLDP has independent transmit and receive control per interface. 'no lldp transmit' "
            "stops outbound LLDP frames; 'no lldp receive' stops processing inbound LLDP frames. "
            "If a device does not transmit LLDP, it will not appear in any neighbor's LLDP table. "
            "If it does not receive, it will not build its own neighbor table entries but will still "
            "appear in neighbors' tables if it transmits."
        ),
    },
    {
        "id": "cd2v2-010",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "CDP & LLDP",
        "stem": (
            "An engineer needs to discover the management IP address of an adjacent device using "
            "only LLDP. Which command provides the remote device's IP address when LLDP is operating?"
        ),
        "options": [
            {
                "id": "a",
                "text": "show lldp neighbors",
                "correct": False,
                "rationale": (
                    "Incorrect. 'show lldp neighbors' provides a brief summary: Device ID, local "
                    "interface, hold time, capability, and port ID. It does NOT show the neighbor's "
                    "IP address."
                ),
            },
            {
                "id": "b",
                "text": "show lldp neighbors detail",
                "correct": True,
                "rationale": (
                    "Correct. 'show lldp neighbors detail' provides extended information about each "
                    "LLDP neighbor, including the management IP address (if the neighbor advertises "
                    "it via the Management Address TLV), system description, capabilities, and "
                    "interface information."
                ),
            },
            {
                "id": "c",
                "text": "show lldp interface",
                "correct": False,
                "rationale": (
                    "Incorrect. 'show lldp interface' shows per-interface LLDP status (tx/rx enabled "
                    "or disabled). It does not display neighbor information."
                ),
            },
            {
                "id": "d",
                "text": "show lldp traffic",
                "correct": False,
                "rationale": (
                    "Incorrect. 'show lldp traffic' displays LLDP frame statistics (frames sent, "
                    "received, errors). It contains no neighbor detail or IP address information."
                ),
            },
        ],
        "explanation": (
            "'show lldp neighbors' gives a summary table. 'show lldp neighbors detail' gives the full "
            "LLDP TLV set for each neighbor, including the management address TLV (IP address). "
            "This parallels CDP: 'show cdp neighbors detail' also shows IP addresses while the "
            "brief 'show cdp neighbors' does not. Knowing which commands provide which level of "
            "detail is a common exam question."
        ),
    },
    {
        "id": "cd2v2-011",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "CDP & LLDP",
        "stem": (
            "A security policy requires that no Cisco device information be shared with untrusted "
            "devices on a specific interface (Gi0/3) while preserving CDP on all other interfaces. "
            "Which command set achieves this on the switch?"
        ),
        "options": [
            {
                "id": "a",
                "text": "no cdp run",
                "correct": False,
                "rationale": (
                    "Incorrect. 'no cdp run' disables CDP globally on the switch, removing it from "
                    "ALL interfaces — not just Gi0/3. The requirement is to preserve CDP on other ports."
                ),
            },
            {
                "id": "b",
                "text": (
                    "interface Gi0/3\n"
                    " no cdp enable"
                ),
                "correct": True,
                "rationale": (
                    "Correct. 'no cdp enable' applied at the interface level disables CDP on that "
                    "specific interface while leaving it active on all others. This is the granular "
                    "per-interface CDP control command."
                ),
            },
            {
                "id": "c",
                "text": (
                    "interface Gi0/3\n"
                    " cdp disable"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. 'cdp disable' is not a valid Cisco IOS interface command. "
                    "The correct syntax is 'no cdp enable' to disable CDP on a specific interface."
                ),
            },
            {
                "id": "d",
                "text": (
                    "interface Gi0/3\n"
                    " no cdp advertise-v2"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. 'no cdp advertise-v2' disables CDPv2 advertisements but CDPv1 "
                    "frames would still be sent. This does not fully prevent CDP from revealing "
                    "device information."
                ),
            },
        ],
        "explanation": (
            "CDP can be controlled at two levels: globally ('no cdp run' / 'cdp run') and "
            "per-interface ('no cdp enable' / 'cdp enable'). For security on untrusted ports "
            "(uplinks to ISP, links to third-party devices, or access ports facing users), "
            "best practice is to disable CDP per-interface with 'no cdp enable', preventing "
            "the device from leaking platform, IOS version, and IP address information."
        ),
    },
    # -------------------------------------------------------------------------
    # 2.4 – EtherChannel
    # -------------------------------------------------------------------------
    {
        "id": "cd2v2-012",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "EtherChannel",
        "stem": (
            "An engineer configures a Layer 3 EtherChannel between two distribution switches. "
            "After configuration, 'show etherchannel summary' shows Po1(RU) with two member ports. "
            "What does 'RU' indicate about this port-channel?"
        ),
        "options": [
            {
                "id": "a",
                "text": "'R' = redundant link active, 'U' = unidirectional traffic only.",
                "correct": False,
                "rationale": (
                    "Incorrect. 'R' stands for Layer3 (routed) in the EtherChannel summary flags, "
                    "and 'U' stands for in-use (the bundle is active). Neither letter describes "
                    "redundancy or unidirectional traffic."
                ),
            },
            {
                "id": "b",
                "text": "'R' = Layer3 (routed port-channel), 'U' = in use (active and bundled).",
                "correct": True,
                "rationale": (
                    "Correct. In 'show etherchannel summary', port-channel flags are: S=Layer2, "
                    "R=Layer3, U=in-use (active), D=down. 'RU' means the port-channel is a Layer 3 "
                    "routed interface (created with 'no switchport' on the port-channel interface) "
                    "and is currently up and bundling member links."
                ),
            },
            {
                "id": "c",
                "text": "'R' = RSTP role (root port), 'U' = untagged VLAN forwarding.",
                "correct": False,
                "rationale": (
                    "Incorrect. RSTP port roles are not reflected in EtherChannel summary flags. "
                    "The flags in this output are specific to EtherChannel bundle status, not STP."
                ),
            },
            {
                "id": "d",
                "text": "'R' = LACP received PDUs, 'U' = unconfirmed — waiting for LACP response.",
                "correct": False,
                "rationale": (
                    "Incorrect. LACP PDU reception is not indicated by these flags. 'R' and 'U' in "
                    "'show etherchannel summary' are static status codes for the port-channel itself."
                ),
            },
        ],
        "explanation": (
            "EtherChannel summary port-channel flags: D=down, S=Layer2, R=Layer3, U=in use, "
            "M=not in use (minimum links not met). Member port flags: P=in port-channel, "
            "D=down, I=stand-alone, s=suspended, H=LACP hot-standby, u=unsuitable. "
            "'RU' on a port-channel indicates a functioning Layer 3 EtherChannel with IP address "
            "and routing capability, used between routers or Layer 3 switches."
        ),
    },
    {
        "id": "cd2v2-013",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "EtherChannel",
        "stem": (
            "SW1 has a three-link LACP EtherChannel to SW2 using Gi0/1, Gi0/2, and Gi0/3. "
            "The LACP system priority on SW1 is 100 and on SW2 is 200. SW1's port priorities are all "
            "128 (default). An engineer adds Gi0/4 as a fourth member to the port-channel on SW1. "
            "The physical switch port limit for this LACP bundle is 2 active links with 2 hot-standby. "
            "Which switch determines which ports are active and which are hot-standby?"
        ),
        "options": [
            {
                "id": "a",
                "text": "SW2, because it has the higher (worse) system priority and thus becomes the controlling system.",
                "correct": False,
                "rationale": (
                    "Incorrect. In LACP, the switch with the LOWER system priority is the controlling "
                    "(actor) system. SW1 (priority 100) has a lower value and therefore controls which "
                    "ports are active versus hot-standby."
                ),
            },
            {
                "id": "b",
                "text": "SW1, because it has the lower LACP system priority and is the controlling system.",
                "correct": True,
                "rationale": (
                    "Correct. LACP designates the switch with the lower system priority as the "
                    "controlling system. It chooses which member ports are active (bundled) and which "
                    "are in hot-standby (H flag) based on port priority then port number. SW1 (100) "
                    "controls the selection over SW2 (200)."
                ),
            },
            {
                "id": "c",
                "text": "Both switches negotiate equally; port selection is determined by the physical cable length.",
                "correct": False,
                "rationale": (
                    "Incorrect. Physical cable length has no relevance to LACP. Port selection is "
                    "deterministic based on system priority, then port priority, then port number."
                ),
            },
            {
                "id": "d",
                "text": "The first two ports connected (Gi0/1 and Gi0/2) are always active; later-connected ports are always standby regardless of priority.",
                "correct": False,
                "rationale": (
                    "Incorrect. Port selection uses LACP port priority (lower wins) and then port number, "
                    "not connection order. A port with a manually lowered priority can displace a "
                    "previously active port."
                ),
            },
        ],
        "explanation": (
            "LACP port selection uses: (1) system priority (lower wins = controlling system), "
            "(2) system MAC address (tiebreaker), (3) port priority on the controlling system "
            "(lower wins = active), (4) port number (tiebreaker). When more ports are eligible "
            "than the maximum active links, excess ports with higher priority/port number enter "
            "LACP Hot-Standby (H flag). They automatically become active if an active port fails."
        ),
    },
    {
        "id": "cd2v2-014",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "EtherChannel",
        "stem": (
            "A network engineer needs to configure PAgP EtherChannel between SW1 and SW2. "
            "SW1 uses 'channel-group 1 mode desirable'. Which mode on SW2 will FAIL to form "
            "the EtherChannel?"
        ),
        "options": [
            {
                "id": "a",
                "text": "channel-group 1 mode auto",
                "correct": False,
                "rationale": (
                    "Incorrect. PAgP desirable + auto is a valid combination. 'Desirable' initiates "
                    "PAgP PDUs and 'auto' responds, resulting in a formed EtherChannel."
                ),
            },
            {
                "id": "b",
                "text": "channel-group 1 mode desirable",
                "correct": False,
                "rationale": (
                    "Incorrect. PAgP desirable + desirable is valid. Both sides initiate PAgP "
                    "and negotiate a channel successfully."
                ),
            },
            {
                "id": "c",
                "text": "channel-group 1 mode on",
                "correct": True,
                "rationale": (
                    "Correct. 'On' mode enables the EtherChannel without any negotiation protocol. "
                    "When one side uses 'on' (no protocol) and the other uses 'desirable' (PAgP), "
                    "they are incompatible. 'On' mode ignores PAgP PDUs, and 'desirable' mode "
                    "requires PAgP acknowledgment, so the channel will NOT form."
                ),
            },
            {
                "id": "d",
                "text": "channel-group 1 mode passive",
                "correct": False,
                "rationale": (
                    "Incorrect. Wait — 'passive' is an LACP mode. PAgP uses 'auto' and 'desirable'. "
                    "If SW2 is configured with LACP 'passive', the protocol mismatch (PAgP vs LACP) "
                    "would also prevent formation, but 'passive' is not a valid PAgP mode. However, "
                    "among the given options, 'on' mode is the specific answer targeting the "
                    "negotiation protocol incompatibility scenario."
                ),
            },
        ],
        "explanation": (
            "EtherChannel negotiation protocol compatibility: PAgP modes (auto/desirable) work only "
            "with PAgP modes; LACP modes (active/passive) work only with LACP modes; 'on' mode "
            "works only with 'on'. Mixing negotiation protocols (PAgP with LACP or 'on' with any "
            "negotiation mode) will prevent the channel from forming. 'On+on' creates a channel "
            "without any negotiation, which is less fault-tolerant."
        ),
    },
    {
        "id": "cd2v2-015",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "EtherChannel",
        "stem": (
            "When configuring a Layer 2 EtherChannel, which TWO configurations applied to member "
            "ports on the SAME switch will cause IOS to flag them as 'unsuitable for bundling' "
            "(u flag) and prevent the port from joining the port-channel? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "One member port is a trunk with native VLAN 1; another member port is a trunk with native VLAN 99.",
                "correct": True,
                "rationale": (
                    "Correct. All member ports in an EtherChannel must have identical trunk "
                    "configurations, including native VLAN. A native VLAN mismatch between member "
                    "ports on the same switch causes IOS to mark the inconsistent port as unsuitable "
                    "(u) and exclude it from the bundle."
                ),
            },
            {
                "id": "b",
                "text": "The two member ports are on different line cards of the same chassis switch.",
                "correct": False,
                "rationale": (
                    "Incorrect. EtherChannel supports member ports across different modules or line "
                    "cards of the same chassis. This is a valid and common configuration that does not "
                    "make ports unsuitable for bundling."
                ),
            },
            {
                "id": "c",
                "text": "One member port has spanning-tree PortFast enabled; another does not.",
                "correct": True,
                "rationale": (
                    "Correct. STP settings on member ports must be consistent for the EtherChannel "
                    "to form properly. A PortFast mismatch between member ports is treated as an "
                    "inconsistency and can result in the port being flagged as unsuitable."
                ),
            },
            {
                "id": "d",
                "text": "The member ports use different physical cable types (fiber vs. copper) but the same speed.",
                "correct": False,
                "rationale": (
                    "Incorrect. EtherChannel does not restrict member ports by cable media type. "
                    "What matters is that the operational speed and duplex match. A fiber Gi0/1 and "
                    "a copper Gi0/2 running at the same speed/duplex can be in the same EtherChannel."
                ),
            },
        ],
        "explanation": (
            "IOS verifies that EtherChannel member ports have consistent Layer 2 configurations before "
            "bundling them. Parameters that must match for all member ports on a switch: switchport "
            "mode (access/trunk), access VLAN, trunk native VLAN, trunk allowed VLANs, STP settings "
            "(PortFast, guard modes), speed, and duplex. Inconsistent ports are marked 'u' (unsuitable) "
            "in 'show etherchannel summary' and are excluded from the bundle."
        ),
    },
    # -------------------------------------------------------------------------
    # 2.5 – Spanning Tree (RPVST+)
    # -------------------------------------------------------------------------
    {
        "id": "cd2v2-016",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Spanning Tree (RPVST+)",
        "stem": (
            "Three switches (SW1, SW2, SW3) are connected in a triangle. All run Rapid PVST+ for "
            "VLAN 10. SW1 is the root bridge. The link between SW2 and SW3 has a cost of 19 "
            "(100 Mbps). The links from SW1 to SW2 and from SW1 to SW3 both have a cost of 4 "
            "(1 Gbps). After STP converges, what is the role of the port on SW3 that connects to SW2?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Root port — it provides the best path from SW3 to the root via SW2.",
                "correct": False,
                "rationale": (
                    "Incorrect. SW3's root port is the direct link to SW1 (cost 4), not the path "
                    "through SW2 (cost 4+19=23). The direct path is lower cost."
                ),
            },
            {
                "id": "b",
                "text": "Alternate port — it is in discarding state as a backup path to the root.",
                "correct": True,
                "rationale": (
                    "Correct. SW3's direct link to SW1 (cost 4) is its root port. The path via SW2 "
                    "has a cumulative cost of 4+19=23, which is worse. The SW3–SW2 port receives "
                    "BPDUs from SW2 (a non-root switch) with a higher path cost, so SW3 places this "
                    "port in the alternate (discarding) role as a backup path to the root."
                ),
            },
            {
                "id": "c",
                "text": "Designated port — SW3 is responsible for forwarding on the SW2–SW3 segment.",
                "correct": False,
                "rationale": (
                    "Incorrect. For the SW2–SW3 link, the designated port is on SW2, not SW3. SW2 "
                    "has the superior BPDU (lower cumulative cost to root = 4) compared to SW3's "
                    "BPDU (cumulative cost from SW3 to root = 4). This requires tiebreaker analysis "
                    "but SW2's perspective towards SW3 wins the designated role. SW3's port is alternate."
                ),
            },
            {
                "id": "d",
                "text": "Backup port — there is a second path on SW3 to the same segment.",
                "correct": False,
                "rationale": (
                    "Incorrect. A backup port occurs when the same switch has two connections to the "
                    "same network segment (shared media or hub). In this topology, SW3 has only one "
                    "link to the SW2–SW3 segment, so it cannot have a backup port on that segment."
                ),
            },
        ],
        "explanation": (
            "STP port role selection: SW3's direct link to SW1 (cost 4) is the root port. For the "
            "SW2–SW3 link, both SW2 and SW3 claim designated role. SW2's root path cost (4) is less "
            "than SW3's root path cost (4) — wait, they are equal via their direct uplinks. "
            "Tiebreaker: lower sender bridge ID. Assuming SW2 wins, SW2 is designated on that link "
            "and SW3's port on that link becomes alternate (discarding). "
            "Key: alternate port = has received a superior BPDU from a neighbor, providing a backup root path."
        ),
    },
    {
        "id": "cd2v2-017",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Spanning Tree (RPVST+)",
        "stem": (
            "An engineer wants to change the root bridge for VLAN 50 from SW2 (priority 24576) "
            "to SW1, using the explicit priority method (not the 'root primary' macro). "
            "Which command on SW1 accomplishes this with the lowest valid priority that guarantees "
            "SW1 wins the election?"
        ),
        "options": [
            {
                "id": "a",
                "text": "spanning-tree vlan 50 priority 24575",
                "correct": False,
                "rationale": (
                    "Incorrect. STP priorities must be a multiple of 4096. A value of 24575 is not "
                    "a multiple of 4096 and IOS will reject this command with an error."
                ),
            },
            {
                "id": "b",
                "text": "spanning-tree vlan 50 priority 20480",
                "correct": True,
                "rationale": (
                    "Correct. 20480 is 4096 × 5 — a valid multiple of 4096 and lower than SW2's "
                    "24576. This guarantees SW1 wins the root election for VLAN 50. It is also "
                    "one increment (4096) below the current root's priority, which is the minimum "
                    "needed to guarantee election."
                ),
            },
            {
                "id": "c",
                "text": "spanning-tree vlan 50 priority 24576",
                "correct": False,
                "rationale": (
                    "Incorrect. Setting SW1 to the same priority as SW2 (24576) means the election "
                    "is decided by MAC address tiebreaker (lower MAC wins). This does not guarantee "
                    "SW1 becomes root — it depends on MAC addresses."
                ),
            },
            {
                "id": "d",
                "text": "spanning-tree vlan 50 priority 32768",
                "correct": False,
                "rationale": (
                    "Incorrect. 32768 is the default priority and is higher than SW2's 24576. "
                    "SW1 would LOSE the election with this priority."
                ),
            },
        ],
        "explanation": (
            "STP bridge priorities must be multiples of 4096 (0, 4096, 8192, 12288, 16384, 20480, "
            "24576, 28672, 32768, 36864, 40960, 45056, 49152, 53248, 57344, 61440). To guarantee "
            "winning the election, choose a value strictly lower than the current root's priority. "
            "20480 < 24576, so SW1 wins. Note: with PVST+ extended system ID, the actual bridge ID "
            "transmitted includes VLAN 50 added to the configured priority."
        ),
    },
    {
        "id": "cd2v2-018",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Spanning Tree (RPVST+)",
        "stem": (
            "A switch running Rapid PVST+ receives a BPDU on a point-to-point link from a neighbor "
            "with a better (lower) path cost to the root. The switch initiates a proposal. "
            "Which sequence CORRECTLY describes the Rapid PVST+ synchronization (proposal/agreement) "
            "mechanism used to rapidly transition a port to forwarding?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The upstream switch sends a Proposal BPDU → downstream switch blocks all "
                    "non-edge ports and sends Agreement BPDU → upstream switch transitions "
                    "designated port to forwarding immediately."
                ),
                "correct": True,
                "rationale": (
                    "Correct. The RSTP proposal/agreement handshake: (1) upstream designated port "
                    "sends a BPDU with the Proposal flag set; (2) the downstream switch synchronizes "
                    "— it places all its non-edge designated ports into discarding state to prevent "
                    "loops, then sends a BPDU with the Agreement flag back; (3) upstream immediately "
                    "transitions its designated port to forwarding. This replaces the 30-second "
                    "listen+learn delay of classic STP."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The downstream switch sends a Proposal BPDU → upstream switch acknowledges "
                    "with Agreement → both ports transition to forwarding after 15 seconds."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The Proposal is sent by the upstream DESIGNATED port, not the "
                    "downstream switch. The Agreement comes from the downstream switch. There is no "
                    "15-second wait — the forwarding transition is immediate upon receiving Agreement."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Both switches exchange topology change notifications (TCNs) → MAC tables are "
                    "flushed → ports transition to forwarding after the MaxAge timer expires."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This describes how classic STP handles topology changes — not the "
                    "RSTP proposal/agreement fast-transition mechanism. RSTP uses proposal/agreement "
                    "for local link transitions, not MaxAge waits."
                ),
            },
            {
                "id": "d",
                "text": (
                    "RSTP uses the same Listening → Learning → Forwarding sequence as classic STP "
                    "but with a reduced timer of 5 seconds per state transition."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. RSTP does not use the Listening state. Transitions happen via "
                    "proposal/agreement, bypassing the traditional timer-based state machine entirely "
                    "on point-to-point links."
                ),
            },
        ],
        "explanation": (
            "The RSTP proposal/agreement mechanism enables near-instantaneous convergence on "
            "point-to-point links. When a port is ready to become designated, it sends a Proposal. "
            "The receiving switch synchronizes by blocking all its non-edge ports (to prevent "
            "transient loops) and responds with an Agreement. This triggers immediate forwarding "
            "transition. The mechanism cascades hop-by-hop through the network for fast reconvergence."
        ),
    },
    {
        "id": "cd2v2-019",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "STP port roles & states",
        "stem": (
            "On a Rapid PVST+ switch, the uplink port (Gi0/24) connecting to the root bridge loses "
            "its link. The switch has an alternate port (Gi0/23) with the next-best path cost to "
            "the root. What happens to Gi0/23 under Rapid PVST+?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Gi0/23 transitions through Listening and Learning states before reaching Forwarding, taking up to 30 seconds.",
                "correct": False,
                "rationale": (
                    "Incorrect. Rapid PVST+ does not use the Listening state. More importantly, an "
                    "alternate port transitions directly to forwarding without going through Learning "
                    "because it has a pre-selected backup path — this is a key RSTP advantage."
                ),
            },
            {
                "id": "b",
                "text": "Gi0/23 immediately transitions from discarding to forwarding without additional negotiation because it is a pre-selected alternate port.",
                "correct": True,
                "rationale": (
                    "Correct. In RSTP, an alternate port holds a pre-calculated backup path to the "
                    "root. When the root port fails, the alternate port can immediately transition "
                    "to the root port role and move to forwarding state without waiting or "
                    "re-running the proposal/agreement protocol — this is the key fast-convergence "
                    "feature of RSTP alternate ports."
                ),
            },
            {
                "id": "c",
                "text": "Gi0/23 sends a Topology Change Notification (TCN) and waits for the root bridge to recalculate the topology.",
                "correct": False,
                "rationale": (
                    "Incorrect. RSTP handles topology changes locally. The switch does not wait for "
                    "the root bridge to recalculate. The alternate port transitions locally using "
                    "its cached BPDU information."
                ),
            },
            {
                "id": "d",
                "text": "Gi0/23 must first go through a proposal/agreement exchange with SW1 before forwarding.",
                "correct": False,
                "rationale": (
                    "Incorrect. Proposal/agreement is used when transitioning a DESIGNATED port to "
                    "forwarding. An alternate port transitioning to root port role does not require "
                    "a new proposal/agreement exchange — it uses the pre-selected BPDU information."
                ),
            },
        ],
        "explanation": (
            "RSTP alternate ports provide sub-second convergence upon root port failure. Because the "
            "alternate port has already received BPDUs from a different upstream switch and has been "
            "pre-validated as a loop-free backup path, it can immediately assume the root port role "
            "and begin forwarding when the primary root port fails. This is fundamentally different "
            "from classic STP, which requires MaxAge + Listen + Learn (up to 50 seconds)."
        ),
    },
    {
        "id": "cd2v2-020",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "PortFast & BPDU Guard",
        "stem": (
            "An engineer enters 'spanning-tree bpduguard enable' on interface Gi0/5 which has "
            "PortFast configured. A BPDU is received on Gi0/5 from a connected unmanaged switch. "
            "After the port goes err-disabled, which command sequence recovers the port WITHOUT "
            "waiting for the automatic errdisable recovery timer?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "interface Gi0/5\n"
                    " no shutdown"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. 'no shutdown' alone does not recover an err-disabled port. The port "
                    "must first be shut down ('shutdown') to clear the err-disabled state, then "
                    "brought back up with 'no shutdown'."
                ),
            },
            {
                "id": "b",
                "text": (
                    "interface Gi0/5\n"
                    " shutdown\n"
                    " no shutdown"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Manual recovery from err-disabled requires issuing 'shutdown' followed "
                    "by 'no shutdown' on the affected interface. This clears the err-disabled state "
                    "and brings the port back up. Note: if the root cause (BPDU source) is not "
                    "removed, the port will go err-disabled again immediately."
                ),
            },
            {
                "id": "c",
                "text": (
                    "no spanning-tree bpduguard enable on Gi0/5, then\n"
                    " spanning-tree bpduguard enable"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Toggling BPDU Guard does not recover an err-disabled port. "
                    "The physical port must be shut down and then brought back up."
                ),
            },
            {
                "id": "d",
                "text": (
                    "errdisable recovery cause bpduguard\n"
                    "errdisable recovery interval 30"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. These commands configure AUTOMATIC errdisable recovery with a timer, "
                    "not immediate manual recovery. The question specifically asks for the command "
                    "sequence that recovers the port without waiting for the automatic timer."
                ),
            },
        ],
        "explanation": (
            "An err-disabled port requires manual intervention: 'shutdown' followed by 'no shutdown' "
            "in interface configuration mode. This is the only way to clear err-disabled state "
            "immediately. Alternatively, 'errdisable recovery cause bpduguard' with an interval "
            "enables automatic recovery after a configurable delay (default 300 seconds). "
            "Best practice: remove the BPDU source before recovering the port to prevent re-triggering."
        ),
    },
    {
        "id": "cd2v2-021",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "PortFast & BPDU Guard",
        "stem": (
            "An engineer wants to enable BPDU Guard globally only on ports that have PortFast "
            "enabled. Which command enables BPDU Guard in this way?"
        ),
        "options": [
            {
                "id": "a",
                "text": "spanning-tree bpduguard enable (applied globally in global config mode)",
                "correct": False,
                "rationale": (
                    "Incorrect. 'spanning-tree bpduguard enable' is an interface-level command, not "
                    "a global command. It enables BPDU Guard only on the specific interface where "
                    "it is applied, regardless of PortFast status."
                ),
            },
            {
                "id": "b",
                "text": "spanning-tree portfast bpduguard default (applied globally in global config mode)",
                "correct": True,
                "rationale": (
                    "Correct. The global command 'spanning-tree portfast bpduguard default' enables "
                    "BPDU Guard automatically on all interfaces that have PortFast enabled (whether "
                    "via 'spanning-tree portfast' per-interface or 'spanning-tree portfast default' "
                    "globally). This is the recommended global approach for PortFast-enabled ports."
                ),
            },
            {
                "id": "c",
                "text": "spanning-tree guard bpdu default",
                "correct": False,
                "rationale": (
                    "Incorrect. 'spanning-tree guard bpdu default' is not a valid IOS command. "
                    "The 'spanning-tree guard' command is used for Root Guard and Loop Guard, "
                    "not BPDU Guard."
                ),
            },
            {
                "id": "d",
                "text": "spanning-tree bpduguard portfast",
                "correct": False,
                "rationale": (
                    "Incorrect. 'spanning-tree bpduguard portfast' is not a valid Cisco IOS command. "
                    "The correct global command is 'spanning-tree portfast bpduguard default'."
                ),
            },
        ],
        "explanation": (
            "Two ways to enable BPDU Guard: (1) Per-interface: 'spanning-tree bpduguard enable' under "
            "the interface — applies regardless of PortFast status; (2) Global: 'spanning-tree portfast "
            "bpduguard default' — applies only to interfaces with PortFast active. The global method "
            "is cleaner in large deployments and automatically protects all PortFast-enabled ports "
            "without per-interface configuration."
        ),
    },
    {
        "id": "cd2v2-022",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "STP port roles & states",
        "stem": (
            "On SW3, the following is observed:\n\n"
            "SW3# show spanning-tree vlan 10\n"
            "...\n"
            "Interface   Role  Sts   Cost    Prio.Nbr  Type\n"
            "Gi0/1       Desg  FWD   4       128.1     P2p\n"
            "Gi0/2       Root  FWD   4       128.2     P2p\n"
            "Gi0/3       Altn  BLK   4       128.3     P2p\n\n"
            "An engineer increases the STP port cost on Gi0/2 from 4 to 100. "
            "What is the MOST likely new role for Gi0/3 after STP reconverges?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Gi0/3 becomes the root port.",
                "correct": True,
                "rationale": (
                    "Correct. Gi0/2 was the root port (best path to root, cost 4). After increasing "
                    "Gi0/2's cost to 100, the path via Gi0/3 (cost 4) becomes cheaper. Gi0/3 had "
                    "been in alternate role because Gi0/2 was superior. Now Gi0/3 offers the best "
                    "path to the root, so it becomes the new root port."
                ),
            },
            {
                "id": "b",
                "text": "Gi0/3 becomes a designated port.",
                "correct": False,
                "rationale": (
                    "Incorrect. Gi0/3 was receiving a superior BPDU from a neighbor (which is why it "
                    "was in alternate/blocking role). With a better path cost than Gi0/2, Gi0/3 "
                    "becomes the root port, not a designated port."
                ),
            },
            {
                "id": "c",
                "text": "Gi0/3 remains in alternate/blocking state because port costs are evaluated globally.",
                "correct": False,
                "rationale": (
                    "Incorrect. Port cost changes directly affect STP path cost calculation. When "
                    "Gi0/2's cost increases to 100, Gi0/3's path (cost 4) becomes the better path "
                    "to the root, triggering a reconvergence that promotes Gi0/3."
                ),
            },
            {
                "id": "d",
                "text": "Gi0/2 goes err-disabled because the cost change creates a loop.",
                "correct": False,
                "rationale": (
                    "Incorrect. Changing the STP port cost does not cause err-disabled or loops. "
                    "STP reconverges by evaluating the new costs and electing new roles to maintain "
                    "a loop-free topology."
                ),
            },
        ],
        "explanation": (
            "STP root port election: the port with the lowest cumulative cost to the root bridge "
            "becomes the root port. When Gi0/2's cost rises from 4 to 100, its total path cost "
            "exceeds Gi0/3's path cost of 4. STP reconvergence promotes Gi0/3 from alternate "
            "to root port and may place Gi0/2 in alternate or designated role depending on "
            "topology. Changing port cost is a common exam technique for influencing STP path selection."
        ),
    },
    # -------------------------------------------------------------------------
    # 2.6 – Wireless architectures & AP modes
    # -------------------------------------------------------------------------
    {
        "id": "cd2v2-023",
        "domain": 2,
        "objective": "2.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Wireless architectures & AP modes",
        "stem": (
            "A wireless engineer is deploying APs in a large warehouse where no structured cabling "
            "is available and wiring new cable runs is cost-prohibitive. The APs must serve clients "
            "while using a wireless backhaul to connect back to the wired network. Which AP mode "
            "supports this deployment?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Local mode",
                "correct": False,
                "rationale": (
                    "Incorrect. Local mode requires a wired Ethernet connection to the distribution "
                    "system (switch). It cannot use a wireless backhaul and must have CAPWAP "
                    "connectivity over a physical cable."
                ),
            },
            {
                "id": "b",
                "text": "Mesh (Bridge) mode",
                "correct": True,
                "rationale": (
                    "Correct. Cisco wireless mesh/bridge mode allows APs to form a wireless backhaul "
                    "(using a separate radio or the same radio) to connect to a Root Access Point "
                    "(RAP) that has a wired uplink. Mesh Access Points (MAPs) then serve clients on "
                    "their remaining radio. This eliminates the need for wired cable runs to each AP."
                ),
            },
            {
                "id": "c",
                "text": "Monitor mode",
                "correct": False,
                "rationale": (
                    "Incorrect. Monitor mode dedicates the AP entirely to scanning for rogue devices "
                    "and wireless threats. It does not serve client data and would not solve the "
                    "cable-less coverage requirement."
                ),
            },
            {
                "id": "d",
                "text": "SE-Connect mode",
                "correct": False,
                "rationale": (
                    "Incorrect. SE-Connect mode is used for spectrum analysis — connecting the AP "
                    "to a Cisco Spectrum Expert application for RF interference analysis. It does "
                    "not serve clients or provide wireless backhaul."
                ),
            },
        ],
        "explanation": (
            "Cisco wireless mesh deploys two types of APs: Root Access Points (RAP) — directly "
            "connected to the wired network — and Mesh Access Points (MAP) — connected wirelessly "
            "to the RAP or other MAPs using the backhaul radio (usually 5 GHz). MAPs serve clients "
            "on the other radio (usually 2.4 GHz or another 5 GHz channel). This creates a "
            "self-healing, wireless distribution system without cabling every AP location."
        ),
    },
    {
        "id": "cd2v2-024",
        "domain": 2,
        "objective": "2.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Wireless architectures & AP modes",
        "stem": (
            "Which statement CORRECTLY describes how a Cisco lightweight AP discovers and joins a "
            "Wireless LAN Controller (WLC)?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The AP uses Cisco Discovery Protocol (CDP) to discover the WLC IP address from the directly connected switch, then opens a CAPWAP connection.",
                "correct": False,
                "rationale": (
                    "Incorrect. CDP is used for general neighbor discovery, not for AP-to-WLC "
                    "discovery. APs use dedicated CAPWAP discovery mechanisms to find a WLC."
                ),
            },
            {
                "id": "b",
                "text": "The AP uses a sequence of discovery methods including DHCP option 43, DNS resolution of 'CISCO-CAPWAP-CONTROLLER.local-domain', and broadcasting; it then evaluates candidate WLCs and joins the most suitable one.",
                "correct": True,
                "rationale": (
                    "Correct. Lightweight APs use multiple CAPWAP discovery methods in sequence: "
                    "(1) previously joined WLC (stored in NVRAM), (2) DHCP option 43 (WLC IP), "
                    "(3) DNS lookup of 'CISCO-CAPWAP-CONTROLLER.<domain>', (4) subnet broadcast, "
                    "(5) over-the-air provisioning. The AP collects discovery responses, then "
                    "selects the best WLC based on master WLC status, load, and configuration."
                ),
            },
            {
                "id": "c",
                "text": "The AP requires a static WLC IP address manually entered via the AP's console port before it can join a WLC.",
                "correct": False,
                "rationale": (
                    "Incorrect. While a WLC IP can be manually configured on an AP, it is not "
                    "required. DHCP option 43, DNS, and other automated discovery mechanisms allow "
                    "zero-touch provisioning without manual AP configuration."
                ),
            },
            {
                "id": "d",
                "text": "The AP broadcasts LWAPP discovery requests on UDP port 12222 and all WLCs respond; the AP joins the WLC with the lowest IP address.",
                "correct": False,
                "rationale": (
                    "Incorrect. LWAPP (UDP 12222/12223) is the predecessor to CAPWAP and is largely "
                    "deprecated. CAPWAP (UDP 5246/5247) is the current protocol. WLC selection is "
                    "not based on lowest IP address; it uses master controller status and load-based "
                    "algorithms."
                ),
            },
        ],
        "explanation": (
            "Cisco lightweight AP CAPWAP discovery order: (1) NVRAM — last joined WLC; "
            "(2) DHCP option 43 — WLC IP provided by DHCP server; (3) DNS — 'CISCO-CAPWAP-CONTROLLER'; "
            "(4) Local subnet broadcast; (5) Over-the-air provisioning from nearby APs. "
            "After discovery, the AP selects a WLC (master WLC first, then least-loaded), "
            "authenticates via X.509 certificates, and receives its configuration via CAPWAP."
        ),
    },
    {
        "id": "cd2v2-025",
        "domain": 2,
        "objective": "2.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Wireless architectures & AP modes",
        "stem": (
            "A wireless security team deploys APs in a dedicated mode to detect rogue access points "
            "and unauthorized wireless clients across all channels without serving any wireless data "
            "clients. Which AP mode is configured for this purpose?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Sniffer mode",
                "correct": False,
                "rationale": (
                    "Incorrect. Sniffer mode captures 802.11 frames on a single configured channel "
                    "and sends them to a remote Wireshark/protocol analyzer. It does not scan all "
                    "channels for rogues and is not the right tool for network-wide rogue detection."
                ),
            },
            {
                "id": "b",
                "text": "Monitor mode",
                "correct": True,
                "rationale": (
                    "Correct. Monitor mode dedicates the AP to scanning all 802.11 channels for rogue "
                    "APs, rogue clients, ad-hoc networks, and RF interference. The AP does not serve "
                    "client data in this mode. It reports findings to the WLC for WIPS (Wireless "
                    "Intrusion Prevention System) processing."
                ),
            },
            {
                "id": "c",
                "text": "FlexConnect mode",
                "correct": False,
                "rationale": (
                    "Incorrect. FlexConnect mode is for branch office deployments where APs need to "
                    "switch client traffic locally. It serves clients and does not perform dedicated "
                    "rogue scanning across all channels."
                ),
            },
            {
                "id": "d",
                "text": "Local mode with CleanAir",
                "correct": False,
                "rationale": (
                    "Incorrect. Local mode with CleanAir performs spectrum analysis on the AP's "
                    "operating channel while also serving clients. It does not dedicate the AP "
                    "to full-time multi-channel rogue scanning."
                ),
            },
        ],
        "explanation": (
            "Cisco AP modes for specialized functions: Monitor mode = full-time WIPS scanning (no "
            "client service); Sniffer mode = single-channel packet capture to Wireshark; "
            "SE-Connect = spectrum analysis to Cisco Spectrum Expert; Rogue Detector mode = "
            "listens on all channels for wired rogue APs by correlating wired/wireless MAC tables. "
            "Monitor mode is the correct answer for network-wide rogue detection and WIPS."
        ),
    },
    # -------------------------------------------------------------------------
    # 2.7 – WLC management access (physical infrastructure)
    # -------------------------------------------------------------------------
    {
        "id": "cd2v2-026",
        "domain": 2,
        "objective": "2.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "WLC management access",
        "stem": (
            "A network engineer is configuring a Cisco WLC for the first time. The WLC has "
            "a management interface and a service port interface. What is the PRIMARY purpose "
            "of the WLC service port interface, and which network should it connect to?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The service port carries CAPWAP tunnels to APs and should connect to the AP management VLAN.",
                "correct": False,
                "rationale": (
                    "Incorrect. CAPWAP tunnels use the WLC management interface, not the service port. "
                    "The service port is for out-of-band management, not AP communication."
                ),
            },
            {
                "id": "b",
                "text": "The service port provides out-of-band management access via a dedicated management network and is used for initial configuration and recovery when the management interface is unreachable.",
                "correct": True,
                "rationale": (
                    "Correct. The WLC service port is a dedicated out-of-band (OOB) management "
                    "interface. It connects to a separate management network (separate from the "
                    "data/AP network) and provides access when the in-band management interface "
                    "is unreachable. It is always active and does not carry AP or client data traffic."
                ),
            },
            {
                "id": "c",
                "text": "The service port is a redundant path for management traffic and automatically fails over from the management interface.",
                "correct": False,
                "rationale": (
                    "Incorrect. The service port does not automatically fail over from the management "
                    "interface. It is a separate, independently configured interface for out-of-band "
                    "access, not an automatic failover mechanism."
                ),
            },
            {
                "id": "d",
                "text": "The service port aggregates with the distribution system ports into a LAG bundle for increased bandwidth.",
                "correct": False,
                "rationale": (
                    "Incorrect. The service port is always a separate, independent 10/100 Ethernet "
                    "interface. It cannot be included in a LAG bundle with the distribution system "
                    "ports. The distribution system ports are what form the LAG."
                ),
            },
        ],
        "explanation": (
            "The Cisco WLC has two categories of physical ports: distribution system ports (carry AP "
            "CAPWAP, client data, and management traffic — these can be bundled into a LAG) and the "
            "service port (dedicated OOB management — always separate, typically 10/100, connects to "
            "an isolated management network). The service port allows access even when the main "
            "network is misconfigured or the management interface is unreachable."
        ),
    },
    {
        "id": "cd2v2-027",
        "domain": 2,
        "objective": "2.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "WLC management access",
        "stem": (
            "An engineer is configuring a switch port to connect an autonomous AP that has been "
            "configured with a single SSID mapped to VLAN 20. The AP handles 802.1Q tagging "
            "internally and sends tagged traffic to the switch. Which switch port configuration "
            "is MOST appropriate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Access port in VLAN 20.",
                "correct": False,
                "rationale": (
                    "Incorrect. If the AP sends 802.1Q-tagged frames (VLAN 20 tagged), the switch "
                    "access port would receive double-tagged frames or reject the tagged frame. "
                    "An access port does not process 802.1Q tags from connected devices."
                ),
            },
            {
                "id": "b",
                "text": "Trunk port allowing VLAN 20 with native VLAN set to the AP's management VLAN.",
                "correct": True,
                "rationale": (
                    "Correct. An autonomous AP configured for 802.1Q trunking sends tagged frames "
                    "for each VLAN/SSID. The switch port must be a trunk to accept and process these "
                    "tagged frames. The native VLAN on the trunk should match the AP's management "
                    "VLAN so that AP management traffic (untagged) reaches the correct VLAN."
                ),
            },
            {
                "id": "c",
                "text": "Access port in VLAN 1 with 'switchport voice vlan 20'.",
                "correct": False,
                "rationale": (
                    "Incorrect. The voice VLAN feature is for IP phones, not for wireless APs. "
                    "Using voice VLAN would not correctly handle VLAN 20 data traffic from the AP."
                ),
            },
            {
                "id": "d",
                "text": "Routed port with 'no switchport' and an IP address in the VLAN 20 subnet.",
                "correct": False,
                "rationale": (
                    "Incorrect. A routed port operates at Layer 3 and cannot carry 802.1Q-tagged "
                    "frames for client traffic. The AP needs a Layer 2 trunk connection to the switch."
                ),
            },
        ],
        "explanation": (
            "Autonomous APs supporting multiple SSIDs with 802.1Q trunking require trunk switch ports. "
            "Each SSID maps to a VLAN; the AP tags frames with the appropriate VLAN ID. The switch "
            "trunk must allow all the required VLANs. The native VLAN matches the AP's management "
            "VLAN (AP sends management traffic untagged). This contrasts with lightweight APs, which "
            "connect to access ports on the switch (the WLC handles all VLAN tagging centrally)."
        ),
    },
    {
        "id": "cd2v2-028",
        "domain": 2,
        "objective": "2.7",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "WLC management access",
        "stem": (
            "A Cisco WLC has LAG enabled with four physical distribution system ports bundled into "
            "a single port-channel. Which TWO statements CORRECTLY describe WLC LAG behavior? "
            "(Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "All WLC interfaces (management, AP-manager, dynamic client interfaces) share the single LAG bundle.",
                "correct": True,
                "rationale": (
                    "Correct. When LAG is enabled on a WLC, all distribution system physical ports "
                    "are bundled into one logical LAG. All WLC logical interfaces — management, "
                    "AP-manager, and dynamic (client) interfaces — use this single LAG bundle."
                ),
            },
            {
                "id": "b",
                "text": "Enabling or disabling LAG on the WLC requires a reboot to take effect.",
                "correct": True,
                "rationale": (
                    "Correct. LAG configuration on a Cisco WLC is not immediately active. Enabling "
                    "or disabling LAG requires saving the configuration and rebooting the WLC. "
                    "This is an important operational consideration during deployments."
                ),
            },
            {
                "id": "c",
                "text": "The WLC service port can be added to the LAG bundle for additional bandwidth.",
                "correct": False,
                "rationale": (
                    "Incorrect. The WLC service port is always separate and cannot be included in "
                    "the LAG bundle. Only the distribution system ports participate in LAG."
                ),
            },
            {
                "id": "d",
                "text": "WLC LAG uses PAgP as the negotiation protocol for compatibility with Cisco switches.",
                "correct": False,
                "rationale": (
                    "Incorrect. WLC LAG uses IEEE 802.3ad (LACP), not the Cisco-proprietary PAgP. "
                    "The connected switch port-channel must also be configured with LACP."
                ),
            },
        ],
        "explanation": (
            "WLC LAG key facts: uses IEEE 802.3ad/LACP (not PAgP); bundles all distribution system "
            "ports; all logical WLC interfaces (management, AP-manager, dynamic) share the bundle; "
            "enabling/disabling LAG requires a WLC reboot; the service port is always excluded from "
            "LAG. The switch must be configured with a matching LACP port-channel. LAG provides "
            "both redundancy and increased bandwidth for the WLC uplink."
        ),
    },
    # -------------------------------------------------------------------------
    # 2.8 – WLC management access (protocols and security)
    # -------------------------------------------------------------------------
    {
        "id": "cd2v2-029",
        "domain": 2,
        "objective": "2.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "WLC management access",
        "stem": (
            "An engineer configures a Cisco WLC to use RADIUS for 802.1X wireless client "
            "authentication. The WLC is configured with the RADIUS server IP and shared secret. "
            "When clients attempt 802.1X authentication, the WLC receives 'RADIUS server not "
            "responding' errors. The RADIUS server is reachable via ping from the WLC management "
            "interface. What is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The shared secret on the WLC does not match the shared secret configured on the RADIUS server for that WLC client.",
                "correct": True,
                "rationale": (
                    "Correct. RADIUS authentication requires a matching shared secret between the NAS "
                    "(WLC) and the RADIUS server. If the secret does not match, the RADIUS server "
                    "will silently discard the Access-Request (it cannot verify the authenticator), "
                    "causing the WLC to receive no response and report 'server not responding'."
                ),
            },
            {
                "id": "b",
                "text": "RADIUS uses TCP and the TCP session has been dropped; it must be re-established.",
                "correct": False,
                "rationale": (
                    "Incorrect. RADIUS uses UDP (ports 1812 for authentication, 1813 for accounting). "
                    "There is no TCP session to drop. Each RADIUS request is a UDP transaction."
                ),
            },
            {
                "id": "c",
                "text": "The WLC management interface must be in the same subnet as the RADIUS server for authentication to work.",
                "correct": False,
                "rationale": (
                    "Incorrect. The WLC can reach a RADIUS server in a different subnet as long as "
                    "routing is in place (which is confirmed by the successful ping). They do not "
                    "need to be in the same subnet."
                ),
            },
            {
                "id": "d",
                "text": "RADIUS authentication requires TACACS+ to be disabled first on the WLC.",
                "correct": False,
                "rationale": (
                    "Incorrect. RADIUS and TACACS+ can coexist on the WLC; they serve different "
                    "purposes (RADIUS for client auth, TACACS+ for admin auth). Neither requires "
                    "the other to be disabled."
                ),
            },
        ],
        "explanation": (
            "RADIUS shared secret mismatch causes the RADIUS server to silently drop packets — the "
            "server cannot authenticate the message authenticator field if the secret is wrong. "
            "The NAS (WLC) sees no response and reports the server as unreachable. This is a very "
            "common real-world issue. Always verify: (1) correct RADIUS server IP, (2) correct UDP "
            "ports (1812/1813), (3) WLC IP is in the RADIUS server's client list, (4) matching secret."
        ),
    },
    {
        "id": "cd2v2-030",
        "domain": 2,
        "objective": "2.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "WLC management access",
        "stem": (
            "A network administrator wants to access the Cisco WLC GUI from a remote workstation "
            "using the most secure in-band method. The WLC management interface has an IP of "
            "10.10.10.1. The workstation's browser navigates to 'http://10.10.10.1'. The browser "
            "receives a redirect. What does the WLC redirect the browser to, and why?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The WLC redirects HTTP to HTTPS (https://10.10.10.1) because HTTP access is disabled by default and HTTPS is required for encrypted management.",
                "correct": True,
                "rationale": (
                    "Correct. Cisco WLCs redirect HTTP to HTTPS by default. HTTPS (TLS-encrypted) is "
                    "the secure management method for the WLC GUI. The WLC automatically redirects "
                    "plain HTTP requests to HTTPS to ensure all management traffic is encrypted. "
                    "This behavior can be modified but HTTPS is always the recommended method."
                ),
            },
            {
                "id": "b",
                "text": "The WLC redirects HTTP to the console port because web management is disabled by default.",
                "correct": False,
                "rationale": (
                    "Incorrect. The console port is a physical interface and cannot be redirected "
                    "to from a browser. Web management (HTTPS GUI) is available on the WLC by "
                    "default on the management interface."
                ),
            },
            {
                "id": "c",
                "text": "The WLC redirects HTTP to the service port IP address for security isolation.",
                "correct": False,
                "rationale": (
                    "Incorrect. The WLC does not redirect management traffic from one interface to "
                    "another. HTTP is redirected to HTTPS on the same management IP address."
                ),
            },
            {
                "id": "d",
                "text": "The WLC redirects HTTP to a captive portal for guest authentication.",
                "correct": False,
                "rationale": (
                    "Incorrect. Captive portals are for wireless guest client authentication on "
                    "specific WLANs — they are not presented when an admin accesses the WLC "
                    "management interface from a wired workstation."
                ),
            },
        ],
        "explanation": (
            "The Cisco WLC automatically redirects HTTP (port 80) requests to HTTPS (port 443) for "
            "the management GUI. This ensures administrator credentials and session data are encrypted "
            "via TLS. The WLC management GUI is accessible over HTTPS; the redirect from HTTP is a "
            "built-in security behavior. SSH provides encrypted CLI access (alternative to HTTPS GUI)."
        ),
    },
    # -------------------------------------------------------------------------
    # 2.9 – WLAN GUI configuration
    # -------------------------------------------------------------------------
    {
        "id": "cd2v2-031",
        "domain": 2,
        "objective": "2.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "WLAN GUI configuration",
        "stem": (
            "On a Cisco WLC, an engineer creates a new WLAN for guest users. The SSID is "
            "'GUEST' and the engineer maps it to the 'Guest_Interface' dynamic interface (VLAN 99). "
            "The engineer wants guests to be redirected to a web login page before accessing the "
            "internet. Which security configuration should be applied to this WLAN?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Layer 2 Security: WPA+WPA2 with PSK",
                "correct": False,
                "rationale": (
                    "Incorrect. WPA2-PSK is a Layer 2 security mechanism that requires guests to "
                    "know a pre-shared key. It does not provide a web login page (captive portal) "
                    "for guest authentication."
                ),
            },
            {
                "id": "b",
                "text": "Layer 3 Security: Web Authentication (Web Auth)",
                "correct": True,
                "rationale": (
                    "Correct. Layer 3 Web Authentication (Web Auth) on a WLC redirects clients to "
                    "a login web page after they associate to the SSID. Clients associate without "
                    "Layer 2 credentials, then are presented with a captive portal. After successful "
                    "web login, the WLC allows them internet access. This is the standard guest "
                    "access model."
                ),
            },
            {
                "id": "c",
                "text": "Layer 2 Security: 802.1X with RADIUS",
                "correct": False,
                "rationale": (
                    "Incorrect. 802.1X requires a supplicant installed on the client device and "
                    "valid credentials known to a RADIUS server. This is not suitable for open "
                    "guest access where users should be redirected to a web login page."
                ),
            },
            {
                "id": "d",
                "text": "No Layer 2 and no Layer 3 security; leave the WLAN completely open.",
                "correct": False,
                "rationale": (
                    "Incorrect. An open WLAN with no security provides access to all users without "
                    "any authentication. While the WLAN would be open at Layer 2, no web redirect "
                    "would occur. Layer 3 Web Auth must be explicitly configured for captive portal."
                ),
            },
        ],
        "explanation": (
            "Guest WLANs typically use: Layer 2 Security = None (open association — no WPA key "
            "required), Layer 3 Security = Web Authentication. After associating, the client receives "
            "a DHCP address from the guest VLAN but all traffic is blocked until the web login is "
            "completed. The WLC intercepts HTTP and redirects to the login page. Web Auth can use "
            "the WLC's internal web page, a customized page, or an external web server."
        ),
    },
    {
        "id": "cd2v2-032",
        "domain": 2,
        "objective": "2.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "WLAN GUI configuration",
        "stem": (
            "On a Cisco WLC, a WLAN is configured with WPA2-PSK security. The WLAN is enabled "
            "and broadcasting its SSID. Users report they can see the SSID but cannot connect — "
            "authentication fails immediately. The engineer verifies that users are entering the "
            "correct passphrase. Which WLC WLAN setting is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The WLAN's radio policy is set to '802.11a only' but the client devices only support 802.11b/g (2.4 GHz).",
                "correct": False,
                "rationale": (
                    "Incorrect. A radio policy mismatch would prevent the client from seeing the SSID "
                    "in the first place (if the AP is only transmitting on 5 GHz). Since the client "
                    "can see the SSID, the radio is accessible."
                ),
            },
            {
                "id": "b",
                "text": "The WLAN's WPA2 encryption is set to TKIP, but the client's wireless adapter requires AES (CCMP) and will not negotiate TKIP.",
                "correct": True,
                "rationale": (
                    "Correct. Authentication can fail at the 4-way handshake if the encryption "
                    "cipher suite is incompatible. If the WLAN is configured for TKIP only and the "
                    "client requires AES, the cipher negotiation fails and the client cannot complete "
                    "authentication even with the correct passphrase. Modern WPA2 clients may reject TKIP."
                ),
            },
            {
                "id": "c",
                "text": "The WLAN's SSID broadcast is enabled; it should be disabled to allow clients to connect.",
                "correct": False,
                "rationale": (
                    "Incorrect. SSID broadcast (beacon) is irrelevant to authentication success. "
                    "Disabling SSID broadcast would make the SSID invisible, not fix authentication. "
                    "Hidden SSIDs also do not improve security."
                ),
            },
            {
                "id": "d",
                "text": "The WLAN status is set to 'Enabled' but requires the AP group to be restarted.",
                "correct": False,
                "rationale": (
                    "Incorrect. Enabling a WLAN does not require AP group restarts. If the SSID is "
                    "visible and clients can attempt connection, the WLAN is active on the APs. "
                    "The issue is in authentication, not WLAN availability."
                ),
            },
        ],
        "explanation": (
            "WPA2-PSK authentication failure despite correct passphrase often points to cipher suite "
            "incompatibility. The Cisco WLC allows configuring WPA2 with TKIP, AES (CCMP), or both. "
            "If only TKIP is selected and a client device is WPA2-only with AES requirement (or vice "
            "versa), the 4-way handshake will fail. Best practice: enable AES (CCMP) for WPA2, and "
            "optionally TKIP for WPA backward compatibility if needed."
        ),
    },
    {
        "id": "cd2v2-033",
        "domain": 2,
        "objective": "2.9",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "WLAN GUI configuration",
        "stem": (
            "A network engineer is configuring a new WLAN on a Cisco WLC. The WLAN uses 802.1X "
            "authentication. The engineer wants to prevent clients from roaming between APs while "
            "keeping their 802.1X sessions active (sticky client feature is enabled). The engineer "
            "also needs clients to obtain an IP address from a specific DHCP server and fail if "
            "they do not use DHCP. Which two WLC WLAN settings support these requirements?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Enable 'DHCP Required' under the WLAN Advanced tab; enable 'Client Exclusion' under Security tab.",
                "correct": False,
                "rationale": (
                    "Incorrect. 'DHCP Required' correctly forces clients to use DHCP. However, "
                    "'Client Exclusion' is not the sticky client feature — it excludes repeatedly "
                    "failing clients (security measure), not roaming clients."
                ),
            },
            {
                "id": "b",
                "text": "Enable 'DHCP Required' under the WLAN Advanced tab; enable 'Sticky Client' (also called Client Band Select) to prevent roaming.",
                "correct": False,
                "rationale": (
                    "Incorrect. Band Select steers dual-band clients to 5 GHz — it does not prevent "
                    "roaming between APs. 'Sticky client' behavior is a separate setting. Additionally, "
                    "preventing client roaming entirely is generally not recommended as it disrupts mobility."
                ),
            },
            {
                "id": "c",
                "text": "Enable 'DHCP Required' under the Advanced tab; configure the DHCP server IP under the dynamic interface mapped to this WLAN.",
                "correct": True,
                "rationale": (
                    "Correct. 'DHCP Required' on the WLAN Advanced tab forces all clients to use "
                    "DHCP — clients with static IPs are denied access. The DHCP server IP is "
                    "configured on the dynamic interface (VLAN interface) mapped to the WLAN, "
                    "directing DHCP requests to the correct server. Together, these enforce DHCP use "
                    "and point to the correct DHCP server."
                ),
            },
            {
                "id": "d",
                "text": "Configure 'IP Address Assignment: Manual' on the WLAN General tab to force a fixed IP range.",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no 'IP Address Assignment: Manual' option on the WLC WLAN "
                    "General tab. IP assignment for clients is controlled via DHCP server configuration "
                    "and the 'DHCP Required' option."
                ),
            },
        ],
        "explanation": (
            "Cisco WLC WLAN Advanced tab 'DHCP Required' setting: when enabled, any client that "
            "does not obtain an IP via DHCP is excluded from the WLAN. The DHCP server for a WLAN "
            "is configured on the dynamic interface (VLAN interface) to which the WLAN is mapped — "
            "under WLC > Controller > Interfaces. This ensures DHCP requests reach the correct "
            "server. 'DHCP Required' is commonly used in enterprise WLANs for IP address management."
        ),
    },
    {
        "id": "cd2v2-034",
        "domain": 2,
        "objective": "2.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "WLAN GUI configuration",
        "stem": (
            "An engineer is configuring a WLAN on a Cisco WLC for a Voice over Wi-Fi deployment. "
            "The engineer sets the QoS profile to 'Platinum' and enables WMM. A security audit "
            "requires that Protected Management Frames (PMF/802.11w) be mandatory on this WLAN. "
            "Where in the WLC GUI is PMF configured for a WLAN?"
        ),
        "options": [
            {
                "id": "a",
                "text": "WLAN > Advanced tab > 802.11w (PMF) section",
                "correct": False,
                "rationale": (
                    "Incorrect. PMF/802.11w is not configured under the Advanced tab in Cisco WLC "
                    "WLAN configuration. It is under the Security settings."
                ),
            },
            {
                "id": "b",
                "text": "WLAN > Security tab > Layer 2 > WPA+WPA2 > 802.11w (PMF) configuration",
                "correct": True,
                "rationale": (
                    "Correct. On the Cisco WLC, Protected Management Frames (802.11w/PMF) is "
                    "configured under the WLAN's Security tab > Layer 2 security section, within "
                    "the WPA/WPA2 configuration. It can be set to Disabled, Optional, or Required. "
                    "Setting it to 'Required' enforces PMF for all clients on the WLAN."
                ),
            },
            {
                "id": "c",
                "text": "WLAN > QoS tab > Management Frame Protection section",
                "correct": False,
                "rationale": (
                    "Incorrect. The QoS tab handles traffic priority (WMM, profiles, rate limiting). "
                    "PMF is a security feature configured under the Security tab, not QoS."
                ),
            },
            {
                "id": "d",
                "text": "WLC > Security > Management Frame Protection (global setting only; cannot be per-WLAN)",
                "correct": False,
                "rationale": (
                    "Incorrect. While Cisco WLC has infrastructure MFP (which is a global setting), "
                    "client PMF (802.11w) is configured per-WLAN under the WLAN Security > Layer 2 "
                    "settings. It can be enabled independently for each WLAN."
                ),
            },
        ],
        "explanation": (
            "802.11w (PMF — Protected Management Frames) protects management frames (deauthentication, "
            "disassociation) from spoofing attacks. On the Cisco WLC, client PMF is configured per-WLAN "
            "under Security > Layer 2 > WPA+WPA2 parameters. Three options: Disabled, Optional "
            "(clients can connect with or without PMF), Required (only PMF-capable clients allowed). "
            "WPA3 mandates PMF; WPA2-Enterprise deployments should set it to at least Optional."
        ),
    },
    # -------------------------------------------------------------------------
    # Additional questions balancing remaining study_topics
    # -------------------------------------------------------------------------
    {
        "id": "cd2v2-035",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Spanning Tree (RPVST+)",
        "stem": (
            "A network has four switches in a square topology (SW1–SW2–SW3–SW4–SW1) with "
            "redundant uplinks. All run Rapid PVST+. SW1 is the root bridge for all VLANs. "
            "Which TWO statements about the post-convergence STP topology are correct? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Every non-root switch will have exactly one root port.",
                "correct": True,
                "rationale": (
                    "Correct. Each non-root switch (SW2, SW3, SW4) has exactly one root port — the "
                    "port providing the lowest-cost path to the root bridge. This is a fundamental "
                    "STP rule regardless of topology."
                ),
            },
            {
                "id": "b",
                "text": "All ports on the root bridge (SW1) will be designated ports.",
                "correct": True,
                "rationale": (
                    "Correct. The root bridge always has all of its ports in the designated role "
                    "because it has the best path cost to itself (zero). All BPDUs originate from "
                    "the root bridge on its designated ports."
                ),
            },
            {
                "id": "c",
                "text": "In Rapid PVST+, blocking ports are called 'blocking' and do not forward any frames including BPDUs.",
                "correct": False,
                "rationale": (
                    "Incorrect. In RSTP, non-forwarding ports are called 'discarding' (not blocking). "
                    "Additionally, even discarding ports continue to receive and process BPDUs — "
                    "they just do not forward data frames."
                ),
            },
            {
                "id": "d",
                "text": "Exactly one redundant link in the topology will have one of its ports in discarding state to prevent a loop.",
                "correct": False,
                "rationale": (
                    "Incorrect. In a square topology with four equal links, only one port needs to "
                    "be in discarding state to break the loop. However, the question says 'exactly "
                    "one redundant link will have one port in discarding' — in a four-switch ring, "
                    "only one port (not link) needs to be discarding. The statement is imprecise "
                    "and potentially misleading, making options A and B the correct choices."
                ),
            },
        ],
        "explanation": (
            "STP convergence rules: (1) The root bridge has ALL ports as designated (forwarding). "
            "(2) Each non-root switch has EXACTLY ONE root port. (3) For each network segment, "
            "exactly one designated port is elected. (4) All remaining ports are in alternate "
            "(RSTP) or blocking (classic STP) state. In a four-switch ring, one link will have "
            "one alternate/discarding port to break the loop. RSTP calls non-forwarding ports "
            "'discarding', not 'blocking'."
        ),
    },
    {
        "id": "cd2v2-036",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "VLANs",
        "stem": (
            "A Cisco switch uses VTP version 2 in server mode. An engineer deletes VLAN 30 from "
            "the VTP server. What happens to switch ports that were previously assigned to VLAN 30 "
            "as access ports?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The ports automatically move to VLAN 1 (the default VLAN) and remain active.",
                "correct": False,
                "rationale": (
                    "Incorrect. Ports assigned to a deleted VLAN do NOT automatically move to VLAN 1. "
                    "They remain configured for VLAN 30 in the running-config, but the VLAN no longer "
                    "exists, so the ports become inactive (they will not forward or receive traffic)."
                ),
            },
            {
                "id": "b",
                "text": "The ports retain their VLAN 30 assignment in the configuration but become inactive because the VLAN does not exist.",
                "correct": True,
                "rationale": (
                    "Correct. When a VLAN is deleted, its entry is removed from vlan.dat. Any access "
                    "port still configured for that VLAN remains configured as 'switchport access vlan 30' "
                    "in the running-config, but becomes inactive — it will not pass traffic. The port "
                    "configuration is not automatically changed, but the VLAN no longer has an active "
                    "status, so ports assigned to it stop forwarding."
                ),
            },
            {
                "id": "c",
                "text": "The ports go err-disabled and require manual recovery.",
                "correct": False,
                "rationale": (
                    "Incorrect. Ports do not go err-disabled when their VLAN is deleted. They simply "
                    "become inactive (no traffic forwarding) because the VLAN database entry is gone. "
                    "The ports come back up automatically if VLAN 30 is recreated."
                ),
            },
            {
                "id": "d",
                "text": "The ports transition to trunk mode to preserve connectivity.",
                "correct": False,
                "rationale": (
                    "Incorrect. Ports do not automatically change their configured mode when a VLAN "
                    "is deleted. They remain as access ports configured for the now-missing VLAN."
                ),
            },
        ],
        "explanation": (
            "When a VLAN is deleted from the VLAN database (vlan.dat), ports assigned to that VLAN "
            "retain their 'switchport access vlan X' configuration but become inactive — they show "
            "as 'not connected' in 'show interfaces' and do not forward traffic. To restore service, "
            "re-create the VLAN (it automatically reactivates the ports) or reassign the ports to "
            "an existing VLAN. This behavior is a common source of outages when VLANs are accidentally deleted."
        ),
    },
    {
        "id": "cd2v2-037",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "EtherChannel",
        "stem": (
            "An engineer configures EtherChannel load-balancing on a Cisco catalyst switch with:\n\n"
            "  port-channel load-balance src-dst-ip\n\n"
            "The switch has a port-channel with four active LACP member links. Two servers send "
            "traffic to one destination IP at high volume, and the traffic from both servers "
            "travels only over a single member link, leaving the other three underutilized. "
            "What is the cause of this behavior?"
        ),
        "options": [
            {
                "id": "a",
                "text": "LACP only uses one active link at a time; the other links are in hot-standby.",
                "correct": False,
                "rationale": (
                    "Incorrect. LACP with multiple active links uses all of them simultaneously for "
                    "load balancing. Hot-standby ports are a separate concept for ports exceeding the "
                    "maximum active member count."
                ),
            },
            {
                "id": "b",
                "text": "The src-dst-ip hash of both servers' IPs to the same destination IP produces the same hash value, mapping both flows to the same physical link.",
                "correct": True,
                "rationale": (
                    "Correct. EtherChannel load balancing uses a hash function on the selected fields "
                    "(in this case, source+destination IP). If the same src-IP + dst-IP pair is used, "
                    "the same hash result occurs, and all such frames use the same physical link. "
                    "If two different source IPs hash to the same value against the same destination, "
                    "they also land on the same link. Hash-based load balancing is per-flow, not "
                    "per-packet, and can be uneven with similar traffic patterns."
                ),
            },
            {
                "id": "c",
                "text": "The port-channel interface has a bandwidth limitation that forces all traffic to one link.",
                "correct": False,
                "rationale": (
                    "Incorrect. The port-channel logical interface aggregates the bandwidth of all "
                    "member links. Load balancing distributes flows across all member links; there is "
                    "no artificial limitation forcing traffic to one link."
                ),
            },
            {
                "id": "d",
                "text": "STP is blocking three of the four EtherChannel links to prevent loops.",
                "correct": False,
                "rationale": (
                    "Incorrect. STP treats an EtherChannel as a single logical link. It does not "
                    "block individual member links within a properly formed port-channel."
                ),
            },
        ],
        "explanation": (
            "EtherChannel load balancing is hash-based and per-flow (not per-packet). All frames "
            "belonging to the same flow (same hash result) traverse the same physical link. This "
            "maintains frame ordering but can cause uneven distribution if traffic has low entropy "
            "(e.g., all flows share the same destination IP). Alternative algorithms include "
            "src-mac, dst-mac, src-dst-mac, src-ip, dst-ip, src-dst-port, etc. Choosing the "
            "algorithm with the most diverse values in your traffic is key to balanced distribution."
        ),
    },
    {
        "id": "cd2v2-038",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Trunking & 802.1Q",
        "stem": (
            "An engineer reviews switch configurations and finds a trunk port with the following:\n\n"
            "  switchport mode trunk\n"
            "  switchport trunk native vlan 1\n"
            "  switchport trunk allowed vlan 1,10,20,30\n\n"
            "Which TWO changes represent security hardening best practices for this trunk port? "
            "(Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Change the native VLAN from VLAN 1 to an unused dedicated VLAN (e.g., VLAN 999) that carries no user or management traffic.",
                "correct": True,
                "rationale": (
                    "Correct. Using VLAN 1 as the native VLAN is a security risk — VLAN 1 is the "
                    "default VLAN and may carry management traffic. Changing the native VLAN to an "
                    "unused, dedicated VLAN mitigates double-tagging VLAN hopping attacks and removes "
                    "VLAN 1 from the untagged (native) transmission path."
                ),
            },
            {
                "id": "b",
                "text": "Remove VLAN 1 from the allowed VLAN list on the trunk.",
                "correct": True,
                "rationale": (
                    "Correct. Removing VLAN 1 from the trunk's allowed VLAN list prevents VLAN 1 "
                    "traffic (including STP, CDP, VTP, and other control-plane traffic that defaults "
                    "to VLAN 1) from traversing this trunk unless explicitly required. This reduces "
                    "the attack surface and limits the blast radius if VLAN 1 is compromised."
                ),
            },
            {
                "id": "c",
                "text": "Enable DTP by setting the port to 'switchport mode dynamic desirable' to ensure the trunk is always formed.",
                "correct": False,
                "rationale": (
                    "Incorrect. Enabling DTP is a security anti-pattern. DTP allows an attacker to "
                    "negotiate a trunk by sending DTP frames. Security best practice is to use static "
                    "trunk mode with 'switchport nonegotiate' to disable DTP entirely."
                ),
            },
            {
                "id": "d",
                "text": "Change the allowed VLAN list to 'all' (1-4094) so that future VLANs are automatically carried.",
                "correct": False,
                "rationale": (
                    "Incorrect. Allowing all VLANs (1-4094) on a trunk is a security risk — it "
                    "unnecessarily exposes all VLANs, including future ones, on this trunk. Security "
                    "best practice is to explicitly allow only the VLANs needed on each trunk link."
                ),
            },
        ],
        "explanation": (
            "Trunk port security hardening best practices: (1) Change native VLAN from VLAN 1 to an "
            "unused, dedicated VLAN (prevents double-tagging attacks and keeps VLAN 1 off the "
            "untagged path); (2) Remove VLAN 1 from the allowed VLAN list (reduces default VLAN "
            "exposure); (3) Disable DTP with 'switchport nonegotiate' (prevents trunk negotiation "
            "attacks); (4) Explicitly allow only necessary VLANs (principle of least privilege); "
            "(5) Use 'vlan dot1q tag native' to force-tag native VLAN frames."
        ),
    },
]

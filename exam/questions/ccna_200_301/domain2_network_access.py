"""
CCNA 200-301 – Domain 2: Network Access
Practice questions covering objectives 2.1 – 2.9.
"""

QUESTIONS = [
    # -------------------------------------------------------------------------
    # 2.1 – VLANs (normal range), access ports, default VLAN, inter-VLAN
    # -------------------------------------------------------------------------
    {
        "id": "cd2-001",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "VLANs",
        "stem": (
            "A switch port is configured with the following commands:\n"
            "  switchport mode access\n"
            "  switchport access vlan 30\n"
            "  switchport voice vlan 40\n\n"
            "A PC and an IP phone share this port (phone connected to switch, PC connected to phone). "
            "Which statement BEST describes how traffic is handled?"
        ),
        "options": [
            {
                "id": "a",
                "text": "PC traffic is tagged with VLAN 30; phone traffic is tagged with VLAN 40 using 802.1Q.",
                "correct": True,
                "rationale": (
                    "Correct. When a voice VLAN is configured on an access port, the port operates as "
                    "a multi-VLAN access port. The phone sends its own voice traffic tagged with VLAN 40 "
                    "while the PC traffic is forwarded as untagged (VLAN 30). The phone understands CDP "
                    "or LLDP-MED announcements and tags its own frames with VLAN 40."
                ),
            },
            {
                "id": "b",
                "text": "Both PC and phone traffic are untagged and carried in VLAN 30.",
                "correct": False,
                "rationale": (
                    "Incorrect. The voice VLAN causes the phone to tag its traffic with VLAN 40; "
                    "only PC traffic passes through untagged in VLAN 30."
                ),
            },
            {
                "id": "c",
                "text": "The port transitions to trunk mode automatically to carry both VLANs.",
                "correct": False,
                "rationale": (
                    "Incorrect. The port stays in access mode. Voice VLAN support is a special "
                    "capability of access ports; it does not turn the port into a trunk."
                ),
            },
            {
                "id": "d",
                "text": "The configuration is invalid; a port cannot have both an access VLAN and a voice VLAN.",
                "correct": False,
                "rationale": (
                    "Incorrect. Cisco IOS explicitly supports configuring both 'switchport access vlan' "
                    "and 'switchport voice vlan' on the same access port to support IP phone deployments."
                ),
            },
        ],
        "explanation": (
            "An access port with a voice VLAN configured supports two VLANs simultaneously. "
            "The IP phone, upon receiving CDP or LLDP-MED voice VLAN information, tags its frames "
            "with the voice VLAN (802.1Q). PC frames are forwarded untagged in the data (access) VLAN. "
            "The port does not become a trunk; it remains an access port with special phone-awareness."
        ),
    },
    {
        "id": "cd2-002",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "VLANs",
        "stem": (
            "A network engineer issues 'show vlan brief' on a Cisco switch and notices that VLAN 1 "
            "shows all access ports that have NOT been explicitly assigned to a VLAN. A junior engineer "
            "wants to remove the unused access ports from VLAN 1 for security. Which approach is correct?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Assign unused ports to an unused VLAN (e.g., VLAN 999) that is not routed and shut them down.",
                "correct": True,
                "rationale": (
                    "Correct. Best practice is to assign unused ports to a 'black-hole' VLAN "
                    "that has no associated SVI or routing, and to administratively shut down those ports. "
                    "This prevents unauthorized devices from accessing VLAN 1."
                ),
            },
            {
                "id": "b",
                "text": "Delete VLAN 1 from the VLAN database using 'no vlan 1'.",
                "correct": False,
                "rationale": (
                    "Incorrect. VLAN 1 cannot be deleted from a Cisco switch's VLAN database. "
                    "It is the default VLAN and is always present."
                ),
            },
            {
                "id": "c",
                "text": "Issue 'no switchport access vlan' on each port to remove their VLAN assignment.",
                "correct": False,
                "rationale": (
                    "Incorrect. 'no switchport access vlan' returns a port to VLAN 1 (the default), "
                    "which is exactly the undesirable state being corrected."
                ),
            },
            {
                "id": "d",
                "text": "Configure the ports as trunk ports so they carry all VLANs, isolating them from VLAN 1 traffic.",
                "correct": False,
                "rationale": (
                    "Incorrect. Converting unused ports to trunks actually increases the attack surface "
                    "by allowing all VLANs to traverse those ports, making the security posture worse."
                ),
            },
        ],
        "explanation": (
            "VLAN 1 is the default VLAN and cannot be deleted. The recommended security practice "
            "is to assign unused ports to a dedicated, non-routed 'parking lot' VLAN and "
            "administratively shut them down. This prevents rogue devices from gaining access to "
            "the management VLAN or any production VLAN."
        ),
    },
    {
        "id": "cd2-003",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "VLANs",
        "stem": (
            "Inter-VLAN routing is required between VLAN 10 (192.168.10.0/24) and VLAN 20 (192.168.20.0/24). "
            "The network uses a Layer 3 switch. Which minimum configuration enables routing between the two VLANs "
            "on the Layer 3 switch?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Create SVIs for VLAN 10 and VLAN 20 with IP addresses, and enable 'ip routing' globally."
                ),
                "correct": True,
                "rationale": (
                    "Correct. On a Layer 3 switch, inter-VLAN routing requires SVIs (Switched Virtual "
                    "Interfaces) for each VLAN with appropriate IP addresses, and 'ip routing' must be "
                    "enabled globally to activate the routing function."
                ),
            },
            {
                "id": "b",
                "text": "Connect both VLANs to a router via separate physical interfaces on the router.",
                "correct": False,
                "rationale": (
                    "Incorrect. While this describes router-on-a-stick or traditional routing, the "
                    "question specifically states a Layer 3 switch is used. SVIs with 'ip routing' "
                    "is the correct approach for a Layer 3 switch."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Enable 'ip routing' globally; no SVIs are needed because the switch routes between "
                    "VLANs automatically once routing is enabled."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. 'ip routing' alone is insufficient. SVIs with IP addresses must be created "
                    "for each VLAN to give the switch a Layer 3 presence in each VLAN. Without SVIs, "
                    "the switch has no gateway address for hosts and no routing entry for those subnets."
                ),
            },
            {
                "id": "d",
                "text": "Create a routed port connecting VLAN 10 and VLAN 20 and assign a /30 address.",
                "correct": False,
                "rationale": (
                    "Incorrect. A routed port is a physical port configured with 'no switchport'; "
                    "it does not belong to a VLAN. You cannot use a single routed port to route "
                    "between two VLANs; SVIs are the appropriate mechanism."
                ),
            },
        ],
        "explanation": (
            "Layer 3 switches perform inter-VLAN routing via SVIs. Each SVI ('interface vlan X') "
            "is assigned an IP address that serves as the default gateway for hosts in that VLAN. "
            "The global command 'ip routing' activates the routing engine. Without both elements, "
            "traffic cannot be routed between VLANs on the switch itself."
        ),
    },
    {
        "id": "cd2-004",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "VLANs",
        "stem": (
            "Examine the following output from SW1:\n\n"
            "SW1# show interfaces Gi0/1 switchport\n"
            "Name: Gi0/1\n"
            "Switchport: Enabled\n"
            "Administrative Mode: static access\n"
            "Operational Mode: static access\n"
            "Administrative Trunking Encapsulation: dot1q\n"
            "Negotiation of Trunking: Off\n"
            "Access Mode VLAN: 50 (VLAN0050)\n"
            "Trunking Native Mode VLAN: 1 (default)\n"
            "Voice VLAN: 60\n\n"
            "A host connected to Gi0/1 is not communicating with hosts in VLAN 50 on other switches. "
            "VLAN 50 exists in the VLAN database on SW1. What is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "VLAN 50 is not in the allowed VLAN list on the uplink trunk to the other switches.",
                "correct": True,
                "rationale": (
                    "Correct. The access port itself is correctly assigned to VLAN 50. The most likely "
                    "cause of connectivity failure to other switches is that VLAN 50 has been removed "
                    "from the allowed VLAN list on the trunk port connecting SW1 to the rest of the network, "
                    "preventing VLAN 50 frames from traversing the trunk."
                ),
            },
            {
                "id": "b",
                "text": "The port is in the wrong operational mode; it should show 'trunk' not 'static access'.",
                "correct": False,
                "rationale": (
                    "Incorrect. For an end-host connection, 'static access' is the correct operational mode. "
                    "A trunk mode is used for switch-to-switch or switch-to-router connections, not for "
                    "connecting hosts."
                ),
            },
            {
                "id": "c",
                "text": "The voice VLAN 60 is conflicting with VLAN 50 and dropping data traffic.",
                "correct": False,
                "rationale": (
                    "Incorrect. A voice VLAN coexisting with a data VLAN on an access port is standard "
                    "practice and does not cause the data VLAN to drop traffic. They operate independently."
                ),
            },
            {
                "id": "d",
                "text": "VLAN 50 must be created on every switch in the network before traffic can pass.",
                "correct": False,
                "rationale": (
                    "Incorrect. While VLAN 50 should exist on each switch that needs to carry it, the "
                    "stem states VLAN 50 exists on SW1. The more precise and testable cause in this "
                    "scenario is the trunk's allowed VLAN list, which is a common misconfiguration."
                ),
            },
        ],
        "explanation": (
            "When a host in an access VLAN can communicate locally but not across the network, "
            "the typical culprit is the trunk's allowed VLAN list. By default all VLANs are allowed, "
            "but if 'switchport trunk allowed vlan' has been used to restrict VLANs, VLAN 50 may have "
            "been omitted. Verify with 'show interfaces trunk' on the uplink port."
        ),
    },
    # -------------------------------------------------------------------------
    # 2.2 – Interswitch connectivity: trunks, 802.1Q, native VLAN
    # -------------------------------------------------------------------------
    {
        "id": "cd2-005",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Trunking & 802.1Q",
        "stem": (
            "Two switches are connected by a trunk. SW1 has 'switchport trunk native vlan 99' but SW2 "
            "uses the default native VLAN on its trunk port. What is the MOST likely result?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A native VLAN mismatch is logged by CDP and traffic on the native VLAN may be "
                    "misforwarded between VLAN 99 and VLAN 1."
                ),
                "correct": True,
                "rationale": (
                    "Correct. CDP detects and logs a native VLAN mismatch. Because untagged frames are "
                    "placed into each switch's own native VLAN, frames SW1 sends untagged (VLAN 99) are "
                    "received by SW2 as VLAN 1, mixing the two VLANs — a security and connectivity issue."
                ),
            },
            {
                "id": "b",
                "text": "The trunk will not form at all and both ports go err-disabled.",
                "correct": False,
                "rationale": (
                    "Incorrect. A native VLAN mismatch does not bring the trunk down or err-disable the "
                    "ports; the trunk still forms and forwards tagged VLANs normally."
                ),
            },
            {
                "id": "c",
                "text": "All VLANs stop passing across the trunk.",
                "correct": False,
                "rationale": (
                    "Incorrect. Tagged VLAN traffic continues to pass; only untagged/native-VLAN "
                    "traffic is affected by the mismatch."
                ),
            },
            {
                "id": "d",
                "text": "DTP automatically changes SW2's native VLAN to 99 to resolve the mismatch.",
                "correct": False,
                "rationale": (
                    "Incorrect. DTP negotiates trunk formation (on/off/desirable/auto), not the native "
                    "VLAN. The native VLAN must be configured to match on both ends manually."
                ),
            },
        ],
        "explanation": (
            "On an 802.1Q trunk, untagged frames belong to the native VLAN. If the two ends disagree, "
            "each switch places untagged frames into its own native VLAN, effectively bridging two "
            "different VLANs. CDP flags this as a native VLAN mismatch via syslog. The trunk itself "
            "stays up and tagged VLANs are unaffected."
        ),
    },
    {
        "id": "cd2-006",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Trunking & 802.1Q",
        "stem": (
            "A network engineer enters the following on a switch port:\n\n"
            "  interface GigabitEthernet0/1\n"
            "   switchport trunk encapsulation dot1q\n"
            "   switchport mode trunk\n"
            "   switchport trunk allowed vlan 10,20,30\n\n"
            "Later, a host in VLAN 40 needs access through this trunk. The engineer issues:\n"
            "  switchport trunk allowed vlan add 40\n\n"
            "What would have happened if the engineer had instead issued:\n"
            "  switchport trunk allowed vlan 40\n"
            "(without 'add')?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Only VLAN 40 would be allowed on the trunk; VLANs 10, 20, and 30 would be removed.",
                "correct": True,
                "rationale": (
                    "Correct. 'switchport trunk allowed vlan 40' (without 'add') replaces the entire "
                    "allowed VLAN list with just VLAN 40, removing VLANs 10, 20, and 30. The 'add' "
                    "keyword appends to the existing list."
                ),
            },
            {
                "id": "b",
                "text": "VLAN 40 would be appended to the existing list; VLANs 10, 20, 30, and 40 would all be allowed.",
                "correct": False,
                "rationale": (
                    "Incorrect. Without the 'add' keyword, the command replaces (not appends to) the "
                    "current allowed VLAN list. The 'add' keyword must be specified to preserve existing VLANs."
                ),
            },
            {
                "id": "c",
                "text": "The command would be rejected because VLAN 40 was not yet created on the switch.",
                "correct": False,
                "rationale": (
                    "Incorrect. Cisco IOS accepts 'switchport trunk allowed vlan' commands for VLANs that "
                    "don't yet exist in the VLAN database; it will just not pass traffic for non-existent VLANs."
                ),
            },
            {
                "id": "d",
                "text": "The command would have no effect because the allowed list already covers all configured VLANs.",
                "correct": False,
                "rationale": (
                    "Incorrect. The command always takes effect and replaces the current list regardless of "
                    "the existing configuration."
                ),
            },
        ],
        "explanation": (
            "The 'switchport trunk allowed vlan' command has three key forms: the base form (replaces list), "
            "'add' (appends), and 'remove' (subtracts). Forgetting 'add' is a classic misconfiguration "
            "that silently removes all other VLANs from the trunk, causing widespread connectivity loss."
        ),
    },
    {
        "id": "cd2-007",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Trunking & 802.1Q",
        "stem": (
            "SW1 Gi0/1 is set to 'switchport mode dynamic desirable'. SW2 Gi0/1 is set to "
            "'switchport mode dynamic auto'. What will be the resulting port mode after DTP negotiation?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The link will form as a trunk.",
                "correct": True,
                "rationale": (
                    "Correct. 'dynamic desirable' actively tries to form a trunk. When paired with "
                    "'dynamic auto' (which passively accepts a trunk if the other side requests it), "
                    "DTP negotiation succeeds and the link becomes a trunk."
                ),
            },
            {
                "id": "b",
                "text": "The link will form as an access link.",
                "correct": False,
                "rationale": (
                    "Incorrect. An access link would result if both sides were 'dynamic auto' "
                    "(neither side initiates trunking) or one side were explicitly set to 'access'."
                ),
            },
            {
                "id": "c",
                "text": "The link will not form at all because neither side is set to a static mode.",
                "correct": False,
                "rationale": (
                    "Incorrect. DTP can negotiate trunk or access mode between dynamic ports. "
                    "The link will form; the question is what mode it will be in."
                ),
            },
            {
                "id": "d",
                "text": "SW1 will be in trunk mode but SW2 will stay in access mode, causing a mode mismatch.",
                "correct": False,
                "rationale": (
                    "Incorrect. DTP negotiation is mutual; if trunking is negotiated, both ports "
                    "transition to trunk mode together."
                ),
            },
        ],
        "explanation": (
            "DTP mode matrix: 'trunk' + any dynamic = trunk; 'dynamic desirable' + 'dynamic desirable' = trunk; "
            "'dynamic desirable' + 'dynamic auto' = trunk; 'dynamic auto' + 'dynamic auto' = access; "
            "'access' + any = access. Here, desirable + auto yields a trunk."
        ),
    },
    {
        "id": "cd2-008",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Trunking & 802.1Q",
        "stem": (
            "An engineer examines a trunk port with 'show interfaces Gi0/2 trunk' and sees:\n\n"
            "Port        Mode         Encapsulation  Status        Native vlan\n"
            "Gi0/2       on           802.1q         trunking      1\n\n"
            "Port        Vlans allowed on trunk\n"
            "Gi0/2       1-4094\n\n"
            "Port        Vlans allowed and active in management domain\n"
            "Gi0/2       1,10,20,30\n\n"
            "Port        Vlans in spanning tree forwarding state and not pruned\n"
            "Gi0/2       1,10,20\n\n"
            "VLAN 30 hosts are not receiving traffic from across this trunk. "
            "What is the MOST likely cause based on this output?"
        ),
        "options": [
            {
                "id": "a",
                "text": "VLAN 30 has been pruned from the trunk by VTP pruning or manual pruning.",
                "correct": True,
                "rationale": (
                    "Correct. The output shows VLAN 30 is allowed and active (appears in the third section) "
                    "but does NOT appear in the 'spanning tree forwarding state and not pruned' section. "
                    "This indicates VLAN 30 is either VTP-pruned or manually pruned on this trunk, "
                    "preventing frames from being forwarded."
                ),
            },
            {
                "id": "b",
                "text": "VLAN 30 is not in the allowed VLAN list on this trunk.",
                "correct": False,
                "rationale": (
                    "Incorrect. The second section shows 'Vlans allowed on trunk: 1-4094', which includes "
                    "VLAN 30. It is explicitly allowed."
                ),
            },
            {
                "id": "c",
                "text": "VLAN 30 does not exist in the VLAN database on this switch.",
                "correct": False,
                "rationale": (
                    "Incorrect. VLAN 30 appears in 'Vlans allowed and active in management domain', "
                    "confirming it exists in the VLAN database and is active."
                ),
            },
            {
                "id": "d",
                "text": "The trunk encapsulation is incorrect; ISL should be used instead of 802.1Q.",
                "correct": False,
                "rationale": (
                    "Incorrect. 802.1Q is the correct and current standard trunking encapsulation. "
                    "ISL is a deprecated Cisco-proprietary protocol and would not resolve this issue."
                ),
            },
        ],
        "explanation": (
            "The 'show interfaces trunk' output has four key sections. The last section — 'VLANs in "
            "spanning tree forwarding state and not pruned' — shows only VLANs actually forwarding "
            "traffic. If a VLAN is active but absent from this last section, it is pruned (by VTP "
            "pruning or 'switchport trunk pruning vlan') and traffic for that VLAN will not cross "
            "this trunk link."
        ),
    },
    # -------------------------------------------------------------------------
    # 2.3 – CDP and LLDP
    # -------------------------------------------------------------------------
    {
        "id": "cd2-009",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "CDP & LLDP",
        "stem": (
            "A network engineer issues 'show cdp neighbors detail' and sees a neighbor entry with "
            "'Platform: cisco WS-C3750X-48P'. The engineer then issues 'show lldp neighbors' and the "
            "same neighbor does NOT appear. Which explanation is MOST likely?"
        ),
        "options": [
            {
                "id": "a",
                "text": "LLDP is disabled globally or on the interface connecting to that neighbor.",
                "correct": True,
                "rationale": (
                    "Correct. LLDP is not enabled by default on Cisco IOS switches (CDP is). "
                    "If 'lldp run' has not been issued globally, or 'no lldp transmit' / 'no lldp receive' "
                    "has been issued on the interface, the neighbor will not appear in the LLDP table."
                ),
            },
            {
                "id": "b",
                "text": "The neighbor switch does not support LLDP because it is a Cisco device.",
                "correct": False,
                "rationale": (
                    "Incorrect. Cisco switches do support LLDP (IEEE 802.1AB). Both CDP and LLDP can run "
                    "simultaneously on Cisco devices. The issue is whether LLDP has been enabled."
                ),
            },
            {
                "id": "c",
                "text": "CDP and LLDP cannot discover the same neighbor simultaneously.",
                "correct": False,
                "rationale": (
                    "Incorrect. CDP and LLDP are independent protocols and can discover the same neighbor "
                    "simultaneously if both are enabled and running on both devices."
                ),
            },
            {
                "id": "d",
                "text": "LLDP hold-time has expired for the neighbor entry before the command was issued.",
                "correct": False,
                "rationale": (
                    "Incorrect. If LLDP were enabled and running, the neighbor would refresh its LLDP entry "
                    "periodically (default LLDP timer is 30 seconds, hold-time 120 seconds). A one-time "
                    "expiry would not explain a consistently missing entry."
                ),
            },
        ],
        "explanation": (
            "CDP is enabled by default on Cisco IOS devices. LLDP (IEEE 802.1AB) is NOT enabled by "
            "default and requires 'lldp run' globally and 'lldp transmit' / 'lldp receive' per interface "
            "(which are on by default once 'lldp run' is issued). If LLDP hasn't been turned on, "
            "neighbors will only appear via CDP."
        ),
    },
    {
        "id": "cd2-010",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "CDP & LLDP",
        "stem": (
            "Which TWO statements about CDP are accurate? (Choose TWO.)\n\n"
            "Note: This is a single-answer question — choose the ONE option that contains TWO correct statements."
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "CDP operates at Layer 2 and can discover neighbors across routed boundaries; "
                    "it uses IP multicast for delivery."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. CDP operates at Layer 2 (data link layer) and does NOT cross Layer 3 "
                    "boundaries (it is not routed). CDP uses a proprietary multicast MAC address "
                    "(01:00:0C:CC:CC:CC), not IP multicast."
                ),
            },
            {
                "id": "b",
                "text": (
                    "CDP is enabled by default on Cisco devices and advertises device type, IOS version, "
                    "IP address, and native VLAN, making it a potential security concern on untrusted ports."
                ),
                "correct": True,
                "rationale": (
                    "Correct. CDP is on by default and shares detailed device information including "
                    "platform, IOS version, IP address, and native VLAN. This is useful for management "
                    "but is a security risk on ports facing untrusted networks, where 'no cdp enable' "
                    "should be applied."
                ),
            },
            {
                "id": "c",
                "text": (
                    "CDP timers cannot be adjusted; the hold-time is always 3x the advertisement interval "
                    "and both are fixed in IOS."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. CDP timers are configurable. 'cdp timer' sets the advertisement interval "
                    "(default 60 seconds) and 'cdp holdtime' sets how long to keep an entry (default 180 "
                    "seconds). They are not fixed."
                ),
            },
            {
                "id": "d",
                "text": (
                    "CDP and LLDP share the same TLV format, so a Cisco device's CDP advertisements "
                    "can be received and decoded by non-Cisco LLDP-only devices."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. CDP is a Cisco-proprietary protocol with its own TLV structure, "
                    "incompatible with LLDP (IEEE 802.1AB). Non-Cisco devices that only speak LLDP "
                    "cannot decode CDP advertisements."
                ),
            },
        ],
        "explanation": (
            "CDP is Cisco-proprietary, Layer 2, non-routable, and enabled by default. It shares device "
            "details (platform, IOS, IP, VLAN) that are operationally useful but represent a security "
            "exposure on untrusted segments. LLDP is the IEEE standard equivalent (802.1AB) and must "
            "be enabled explicitly on Cisco IOS."
        ),
    },
    {
        "id": "cd2-011",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "CDP & LLDP",
        "stem": (
            "An engineer wants LLDP to transmit from a specific interface but not receive LLDP frames "
            "on that same interface. Which configuration accomplishes this?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "interface Gi0/1\n"
                    " lldp transmit\n"
                    " no lldp receive"
                ),
                "correct": True,
                "rationale": (
                    "Correct. LLDP transmit and receive are independently configurable per interface. "
                    "'lldp transmit' enables sending LLDP frames, and 'no lldp receive' disables "
                    "processing of incoming LLDP frames on that interface."
                ),
            },
            {
                "id": "b",
                "text": (
                    "lldp run\n"
                    "interface Gi0/1\n"
                    " lldp transmit-only"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. There is no 'lldp transmit-only' command in Cisco IOS. "
                    "Transmit and receive must be controlled with 'lldp transmit' and 'lldp receive' "
                    "(or their negations) separately."
                ),
            },
            {
                "id": "c",
                "text": (
                    "lldp run\n"
                    "interface Gi0/1\n"
                    " no lldp enable"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. 'no lldp enable' is not a valid Cisco IOS interface-level command. "
                    "LLDP is controlled per-interface with 'lldp transmit' and 'lldp receive'."
                ),
            },
            {
                "id": "d",
                "text": (
                    "lldp run transmit-only Gi0/1"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. 'lldp run' is a global command with no interface or directional "
                    "arguments. Interface-level LLDP control requires entering the interface "
                    "configuration mode."
                ),
            },
        ],
        "explanation": (
            "LLDP per-interface granularity allows independent control of transmit ('lldp transmit') "
            "and receive ('lldp receive'). By default, once 'lldp run' is issued globally, both "
            "transmit and receive are active on all interfaces. Using 'no lldp receive' on an interface "
            "disables LLDP frame processing in the inbound direction only."
        ),
    },
    # -------------------------------------------------------------------------
    # 2.4 – EtherChannel (LACP)
    # -------------------------------------------------------------------------
    {
        "id": "cd2-012",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "EtherChannel",
        "stem": (
            "An engineer configures a port-channel between SW1 and SW2 using LACP. SW1 is configured "
            "with 'channel-group 1 mode active' and SW2 is configured with 'channel-group 1 mode passive'. "
            "Will the EtherChannel form? Why or why not?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Yes. LACP 'active' initiates negotiation; 'passive' responds, so the channel forms.",
                "correct": True,
                "rationale": (
                    "Correct. In LACP, 'active' mode initiates LACP PDUs. 'Passive' mode responds to "
                    "LACP PDUs but does not initiate. Active + passive is a valid combination that "
                    "results in a formed EtherChannel."
                ),
            },
            {
                "id": "b",
                "text": "No. Both sides must be in 'active' mode for LACP to negotiate.",
                "correct": False,
                "rationale": (
                    "Incorrect. LACP requires at least one side to be 'active'. The combination of "
                    "active + passive is valid. The only invalid combination is passive + passive, "
                    "where neither side initiates."
                ),
            },
            {
                "id": "c",
                "text": "No. LACP only works if both sides use the same mode (either both active or both passive).",
                "correct": False,
                "rationale": (
                    "Incorrect. LACP active + active works, and active + passive works. "
                    "Passive + passive does NOT work because neither side sends LACP PDUs."
                ),
            },
            {
                "id": "d",
                "text": "Yes. 'Passive' on SW2 acts as the LACP master and controls the negotiation.",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no 'master' concept in LACP mode terminology. 'Passive' "
                    "simply means the port responds to LACP PDUs but does not originate them. "
                    "The channel forms because 'active' on SW1 initiates the exchange."
                ),
            },
        ],
        "explanation": (
            "LACP mode combinations: active + active = channel forms; active + passive = channel forms; "
            "passive + passive = channel does NOT form (neither initiates). PAgP equivalents are "
            "desirable (active-like) and auto (passive-like). For 'on' mode, both sides must use 'on' "
            "and no negotiation protocol is used."
        ),
    },
    {
        "id": "cd2-013",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "EtherChannel",
        "stem": (
            "A network engineer examines the following output:\n\n"
            "SW1# show etherchannel summary\n"
            "Flags: D - down  P - bundled in port-channel\n"
            "       I - stand-alone  s - suspended\n"
            "       H - Hot-standby (LACP only)\n"
            "       R - Layer3  S - Layer2\n"
            "       u - unsuitable for bundling\n"
            "       U - in use\n\n"
            "Group  Port-channel  Protocol    Ports\n"
            "------+-------------+-----------+---------------------------------------\n"
            "1      Po1(SD)        LACP        Gi0/1(D)   Gi0/2(D)\n\n"
            "What does the 'SD' flag on Po1 indicate, and what is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "'S' = Layer2, 'D' = down. The port-channel is Layer 2 but is down, "
                    "most likely because both member interfaces (Gi0/1 and Gi0/2) are down."
                ),
                "correct": True,
                "rationale": (
                    "Correct. In 'show etherchannel summary' output, 'S' means the port-channel is "
                    "Layer 2 (switched) and 'D' means it is down. The member ports Gi0/1 and Gi0/2 "
                    "both show 'D' (down), confirming that the channel is down because no member "
                    "interfaces are active."
                ),
            },
            {
                "id": "b",
                "text": "'S' = suspended, 'D' = desirable. The channel is suspended because mode mismatch.",
                "correct": False,
                "rationale": (
                    "Incorrect. 'S' in the port-channel flags means Layer2 (not suspended); the flag "
                    "for suspended member ports is lowercase 's'. 'D' in the port-channel flags means "
                    "down, not desirable."
                ),
            },
            {
                "id": "c",
                "text": "'S' = standby, 'D' = degraded. One port is active and one is in standby (LACP hot-standby).",
                "correct": False,
                "rationale": (
                    "Incorrect. 'H' is the flag for LACP Hot-standby, not 'S'. 'S' indicates Layer 2. "
                    "Also, 'D' means down, not degraded. Both member ports showing 'D' means they are "
                    "physically down."
                ),
            },
            {
                "id": "d",
                "text": "'SD' means the port-channel is in shutdown state due to an administrator 'shutdown' command.",
                "correct": False,
                "rationale": (
                    "Incorrect. 'SD' is two separate flags ('S' for Layer2 and 'D' for down). "
                    "A manually shut port-channel would still show 'D', but the cause here is "
                    "the member interfaces being physically down, as shown by their 'D' flags."
                ),
            },
        ],
        "explanation": (
            "The 'show etherchannel summary' output uses letter codes for port-channel and member port "
            "status. For port-channels: R=Layer3, S=Layer2, U=in-use, D=down. For member ports: "
            "P=bundled, D=down, I=stand-alone, s=suspended, H=hot-standby, u=unsuitable. "
            "Po1(SD) = Layer2 port-channel that is down because all member ports are also down."
        ),
    },
    {
        "id": "cd2-014",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "EtherChannel",
        "stem": (
            "When configuring a Layer 2 EtherChannel, which condition will PREVENT the port-channel "
            "from forming, even if LACP negotiation succeeds?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Member interfaces have mismatched speed/duplex settings on the two switches.",
                "correct": False,
                "rationale": (
                    "Incorrect. Speed and duplex mismatches prevent individual links from coming up, "
                    "but the EtherChannel itself requires matching configurations on the member ports "
                    "of the SAME switch. A link with mismatched speed/duplex simply won't form at L1."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Member interfaces on the same switch have different VLAN configurations "
                    "(e.g., one access port in VLAN 10 and another in VLAN 20)."
                ),
                "correct": True,
                "rationale": (
                    "Correct. All member interfaces in an EtherChannel must have identical Layer 2 "
                    "configurations: same mode (access or trunk), same access VLAN (if access), "
                    "same trunk settings (native VLAN, allowed VLANs) if trunk. Mismatched VLAN "
                    "configurations on member ports of the same switch will prevent bundling."
                ),
            },
            {
                "id": "c",
                "text": "The two switches use different LACP system priorities.",
                "correct": False,
                "rationale": (
                    "Incorrect. LACP system priority differences are resolved by LACP negotiation; "
                    "the switch with the lower system priority becomes the controlling system. "
                    "Different priorities do not prevent the channel from forming."
                ),
            },
            {
                "id": "d",
                "text": "One switch uses a port-channel number (e.g., Po1) different from the other switch (e.g., Po2).",
                "correct": False,
                "rationale": (
                    "Incorrect. The port-channel group number is locally significant. SW1 can use "
                    "group 1 and SW2 can use group 2; the LACP system IDs and port keys control "
                    "negotiation, not the local group number."
                ),
            },
        ],
        "explanation": (
            "EtherChannel member ports on the same switch must have identical Layer 2 configurations: "
            "same switchport mode (access/trunk), same access VLAN, and for trunks the same native "
            "VLAN and allowed VLAN list. Inconsistent member port configurations prevent the bundle "
            "from forming. IOS checks these parameters and will suspend mismatched ports."
        ),
    },
    {
        "id": "cd2-015",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "EtherChannel",
        "stem": (
            "Which TWO of the following are valid EtherChannel negotiation protocol and mode combinations "
            "that will successfully form a bundle? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "SW1: channel-group 1 mode on  /  SW2: channel-group 1 mode active",
                "correct": False,
                "rationale": (
                    "Incorrect. 'On' mode does not use any negotiation protocol. When one side is 'on', "
                    "the other side must also be 'on'. Mixing 'on' with LACP 'active' will NOT form "
                    "a channel because 'on' mode ignores LACP PDUs."
                ),
            },
            {
                "id": "b",
                "text": "SW1: channel-group 1 mode active  /  SW2: channel-group 1 mode active",
                "correct": True,
                "rationale": (
                    "Correct. LACP active + active is a valid combination. Both sides initiate LACP "
                    "PDUs and a channel forms successfully."
                ),
            },
            {
                "id": "c",
                "text": "SW1: channel-group 1 mode desirable  /  SW2: channel-group 1 mode auto",
                "correct": True,
                "rationale": (
                    "Correct. PAgP desirable + auto is valid. 'Desirable' initiates PAgP negotiation "
                    "and 'auto' responds, resulting in a formed EtherChannel."
                ),
            },
            {
                "id": "d",
                "text": "SW1: channel-group 1 mode passive  /  SW2: channel-group 1 mode passive",
                "correct": False,
                "rationale": (
                    "Incorrect. LACP passive + passive does not form a channel because neither side "
                    "initiates LACP PDUs. At least one side must be in 'active' mode."
                ),
            },
        ],
        "explanation": (
            "EtherChannel protocol modes: LACP (active/passive), PAgP (desirable/auto), and static (on). "
            "Valid pairings: LACP active+active, LACP active+passive; PAgP desirable+desirable, "
            "PAgP desirable+auto; static on+on. Invalid: passive+passive, auto+auto (for their respective "
            "protocols), and any mix of LACP with PAgP or 'on' with a protocol mode."
        ),
    },
    # -------------------------------------------------------------------------
    # 2.5 – Rapid PVST+ Spanning Tree: root election, port roles/states, PortFast, BPDU Guard
    # -------------------------------------------------------------------------
    {
        "id": "cd2-016",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Spanning Tree (RPVST+)",
        "stem": (
            "Four switches form a loop. Their bridge IDs for VLAN 1 are:\n\n"
            "  SW1: priority 32769, MAC 00:1A:2B:3C:4D:01\n"
            "  SW2: priority 28673, MAC 00:1A:2B:3C:4D:02\n"
            "  SW3: priority 32769, MAC 00:1A:2B:3C:4D:03\n"
            "  SW4: priority 32769, MAC 00:1A:2B:3C:4D:04\n\n"
            "Which switch is elected root bridge for VLAN 1?"
        ),
        "options": [
            {
                "id": "a",
                "text": "SW1, because it has the lowest MAC address among all switches.",
                "correct": False,
                "rationale": (
                    "Incorrect. Bridge ID comparison always starts with priority. SW1's priority of "
                    "32769 is higher than SW2's priority of 28673, so SW1 cannot win over SW2 "
                    "regardless of MAC address."
                ),
            },
            {
                "id": "b",
                "text": "SW2, because it has the lowest bridge priority.",
                "correct": True,
                "rationale": (
                    "Correct. Root bridge election uses the lowest bridge ID: priority is compared "
                    "first, then MAC address if priorities tie. SW2 has priority 28673, which is lower "
                    "than the 32769 shared by SW1, SW3, and SW4. SW2 is elected root."
                ),
            },
            {
                "id": "c",
                "text": "SW4, because it has the highest MAC address (last in the range), winning tiebreaker.",
                "correct": False,
                "rationale": (
                    "Incorrect. STP elects the switch with the LOWEST bridge ID as root. A higher MAC "
                    "address is a disadvantage, not an advantage, in STP tiebreaking."
                ),
            },
            {
                "id": "d",
                "text": "SW3, because its priority of 32769 is the extended system ID-adjusted value for VLAN 1, making it the true base priority of 32768.",
                "correct": False,
                "rationale": (
                    "Incorrect. The priority values shown ARE the effective bridge priorities (base priority "
                    "+ VLAN ID). SW3 has the same priority as SW1 and SW4 (32769), higher than SW2 (28673). "
                    "SW2 wins the election."
                ),
            },
        ],
        "explanation": (
            "Spanning Tree root bridge election uses the lowest Bridge ID = {priority, MAC}. "
            "Priority is compared first; only if they are equal is the MAC address used as tiebreaker "
            "(lower MAC wins). With Cisco PVST+/RPVST+, the bridge priority includes the VLAN ID "
            "as the extended system ID (e.g., base 32768 + VLAN 1 = 32769). SW2 with 28673 wins."
        ),
    },
    {
        "id": "cd2-017",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "STP port roles & states",
        "stem": (
            "On a non-root switch running Rapid PVST+, which port role is assigned to the single best "
            "port providing the lowest-cost path back toward the root bridge?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Designated port",
                "correct": False,
                "rationale": (
                    "Incorrect. A designated port is the port on each network segment that is closest "
                    "to the root bridge and forwards traffic toward hosts on that segment. "
                    "It is not the port on a non-root switch looking toward the root."
                ),
            },
            {
                "id": "b",
                "text": "Root port",
                "correct": True,
                "rationale": (
                    "Correct. Every non-root switch has exactly one root port — the port with the "
                    "lowest cumulative cost path to the root bridge. The root port is always in "
                    "forwarding state."
                ),
            },
            {
                "id": "c",
                "text": "Alternate port",
                "correct": False,
                "rationale": (
                    "Incorrect. An alternate port is a Rapid PVST+ concept — it is a port that has "
                    "received a superior BPDU from a neighbor and is blocked, providing a backup "
                    "path to the root. It is NOT the best path; that is the root port."
                ),
            },
            {
                "id": "d",
                "text": "Backup port",
                "correct": False,
                "rationale": (
                    "Incorrect. A backup port is a Rapid PVST+ port that provides a redundant path "
                    "to a segment where another port on the same switch is already designated. "
                    "It is in discarding state and not the primary path to the root."
                ),
            },
        ],
        "explanation": (
            "Rapid PVST+ port roles: Root port (best path to root, one per non-root switch, forwarding); "
            "Designated port (best port on each segment, forwarding); Alternate port (backup root port, "
            "discarding); Backup port (backup designated port on same segment, discarding). "
            "The all-important root port is the single port per switch on the shortest path to the root."
        ),
    },
    {
        "id": "cd2-018",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Spanning Tree (RPVST+)",
        "stem": (
            "In Rapid PVST+, a port is receiving BPDUs with a superior bridge ID from the root bridge. "
            "The neighbor then stops sending BPDUs entirely. How does Rapid PVST+ respond, and how does "
            "this differ from classic 802.1D STP?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Rapid PVST+ ages out the BPDU after 3x the Hello interval (6 seconds) and begins "
                    "reconvergence immediately; classic STP waits MaxAge (20 seconds) before acting."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Rapid PVST+ uses a per-port BPDU aging mechanism of 3x Hello (3 x 2s = 6s). "
                    "If a port misses 3 consecutive BPDUs, it considers the neighbor lost and triggers "
                    "rapid reconvergence. Classic 802.1D STP waits for the MaxAge timer (default 20s) "
                    "before discarding the stale BPDU and beginning the slow 30-50 second convergence."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Both Rapid PVST+ and classic STP wait 20 seconds (MaxAge) before reconverging; "
                    "the difference is only in subsequent port state transition speed."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. RSTP/Rapid PVST+ does NOT wait MaxAge. It detects failure within 3x "
                    "Hello (6s default) and reconverges much faster. MaxAge is used differently in RSTP."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Rapid PVST+ immediately flushes all MAC addresses and transitions the alternate "
                    "port to forwarding with no delay; classic STP does the same but slower."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. While RSTP reconverges faster using proposal/agreement, it still takes "
                    "some time (not 'immediately') and includes mechanisms to prevent loops. "
                    "The key difference is the BPDU aging timer comparison in the question."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Both protocols rely on the Hello timer alone; Rapid PVST+ is faster only because "
                    "its default Hello timer is 1 second versus 2 seconds in classic STP."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Rapid PVST+ uses the same default Hello timer of 2 seconds as classic "
                    "STP. The speed improvement comes from the 3x Hello aging (vs. MaxAge) and the "
                    "proposal/agreement mechanism for port state transitions."
                ),
            },
        ],
        "explanation": (
            "Classic 802.1D STP uses MaxAge (default 20s) to expire stale BPDUs before reconverging, "
            "then spends 15s in Listening + 15s in Learning (total up to 50s). Rapid PVST+ ages BPDUs "
            "in 3x Hello (6s) and uses a proposal/agreement handshake between switches to rapidly "
            "transition ports, achieving sub-second to low-second convergence in ideal conditions."
        ),
    },
    {
        "id": "cd2-019",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "PortFast & BPDU Guard",
        "stem": (
            "A switch port connected to a PC is configured with PortFast. An engineer then plugs a small "
            "unmanaged switch into that port. What is the risk, and how does BPDU Guard mitigate it?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The unmanaged switch generates BPDUs. With BPDU Guard enabled, the port is "
                    "err-disabled when a BPDU is received, preventing unauthorized switches from "
                    "participating in STP."
                ),
                "correct": True,
                "rationale": (
                    "Correct. PortFast skips Listening/Learning states and goes directly to Forwarding, "
                    "suitable for end-hosts. If a switch is connected, it sends BPDUs. "
                    "BPDU Guard detects BPDUs on a PortFast-enabled port and err-disables it, "
                    "protecting the STP topology from unauthorized switches."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The unmanaged switch does not send BPDUs, so BPDU Guard is irrelevant; "
                    "the real risk is a broadcast storm from the PortFast port."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Managed AND some unmanaged switches do generate BPDUs. Even if this "
                    "particular one doesn't, the risk is an accidental loop and STP topology disruption "
                    "from any device that does send BPDUs. BPDU Guard is the correct countermeasure."
                ),
            },
            {
                "id": "c",
                "text": (
                    "BPDU Guard places the port in VLAN blocking state, allowing traffic but preventing "
                    "the new switch from becoming root."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. BPDU Guard err-disables the port entirely (administratively shuts it "
                    "down), not just blocks it in STP. The port shows 'err-disabled' in 'show interfaces' "
                    "output and requires manual recovery or errdisable recovery."
                ),
            },
            {
                "id": "d",
                "text": (
                    "PortFast automatically disables itself when a BPDU is received, reverting the "
                    "port to normal STP operation without BPDU Guard being needed."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. In classic IOS, PortFast does operationally disable when a BPDU is "
                    "received — but this still allows the switch to participate in STP and potentially "
                    "disrupt the topology. BPDU Guard is needed to err-disable the port and prevent "
                    "any STP participation."
                ),
            },
        ],
        "explanation": (
            "PortFast is designed for end-host ports. When a switch is accidentally connected, it "
            "introduces BPDUs that can trigger STP reconvergence or even a topology change. "
            "BPDU Guard prevents this by immediately err-disabling the port when any BPDU is received. "
            "The err-disabled state is persistent — the port requires 'shutdown/no shutdown' or "
            "automatic errdisable recovery to come back up."
        ),
    },
    {
        "id": "cd2-020",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "STP port roles & states",
        "stem": (
            "During Rapid PVST+ operation, which port states are valid? (Select all that apply — "
            "choose the option that lists ONLY the valid Rapid PVST+ port states.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Discarding, Learning, Forwarding",
                "correct": True,
                "rationale": (
                    "Correct. Rapid PVST+ (RSTP) uses three port states: Discarding (combines the "
                    "original Disabled, Blocking, and Listening states), Learning, and Forwarding. "
                    "The classic Listening state is absorbed into Discarding in RSTP."
                ),
            },
            {
                "id": "b",
                "text": "Blocking, Listening, Learning, Forwarding, Disabled",
                "correct": False,
                "rationale": (
                    "Incorrect. These are the five port states of classic 802.1D STP. Rapid PVST+ "
                    "consolidates Disabled, Blocking, and Listening into a single Discarding state, "
                    "resulting in only three states."
                ),
            },
            {
                "id": "c",
                "text": "Blocking, Learning, Forwarding",
                "correct": False,
                "rationale": (
                    "Incorrect. This is a common misconception. While 'Blocking' is used in classic "
                    "STP, RSTP replaces it with 'Discarding'. The correct RSTP state for a non-forwarding "
                    "port is Discarding, not Blocking."
                ),
            },
            {
                "id": "d",
                "text": "Discarding, Listening, Learning, Forwarding",
                "correct": False,
                "rationale": (
                    "Incorrect. RSTP does not have a 'Listening' state. Listening is part of classic "
                    "802.1D STP. RSTP's three states are Discarding, Learning, and Forwarding."
                ),
            },
        ],
        "explanation": (
            "IEEE 802.1W (RSTP, implemented as Rapid PVST+ on Cisco) reduced the five classic STP "
            "port states to three: Discarding (port does not forward or learn, replaces Disabled/"
            "Blocking/Listening), Learning (learns MACs, does not forward), and Forwarding (fully "
            "operational). This simplification enables the faster proposal/agreement mechanism."
        ),
    },
    {
        "id": "cd2-021",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Spanning Tree (RPVST+)",
        "stem": (
            "SW1 is the root bridge for VLAN 10. SW2 has two uplinks to SW1: Gi0/1 (cost 4) and "
            "Gi0/2 (cost 4). SW2's Gi0/1 has bridge port ID 128.1 and SW2's Gi0/2 has bridge port ID 128.2. "
            "Which port is SW2's root port for VLAN 10, and what tiebreaker determined it?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Gi0/1 is the root port; tiebreaker was the lowest sender port ID from SW1.",
                "correct": False,
                "rationale": (
                    "Incorrect. When two ports on SW2 lead to the same upstream switch (SW1) with equal "
                    "cost, the tiebreaker is the RECEIVING switch's (SW2's) own lowest port ID, not the "
                    "sender's port ID. The sender port ID would matter if SW2 were receiving BPDUs from "
                    "two DIFFERENT upstream switches."
                ),
            },
            {
                "id": "b",
                "text": "Gi0/1 is the root port; tiebreaker was SW2's lowest receiving port ID (128.1 < 128.2).",
                "correct": True,
                "rationale": (
                    "Correct. STP path selection tiebreakers in order: (1) lowest root BID, (2) lowest "
                    "root path cost, (3) lowest sender BID, (4) lowest sender port ID. When two ports on "
                    "the same switch connect to the same upstream switch, tiebreakers 1-3 are equal. "
                    "The final tiebreaker is the local (receiving) port ID. Gi0/1 has port ID 128.1, "
                    "lower than 128.2, so Gi0/1 becomes the root port."
                ),
            },
            {
                "id": "c",
                "text": "Both ports share root port role because their costs are equal; STP load-balances between them.",
                "correct": False,
                "rationale": (
                    "Incorrect. STP never load-balances; exactly one port per switch per VLAN is the "
                    "root port. Equal costs trigger tiebreakers to select one winner."
                ),
            },
            {
                "id": "d",
                "text": "Gi0/2 is the root port because higher port numbers are preferred by STP.",
                "correct": False,
                "rationale": (
                    "Incorrect. STP prefers the LOWER port ID as a tiebreaker, not the higher. "
                    "Gi0/1 (port ID 128.1) wins over Gi0/2 (port ID 128.2)."
                ),
            },
        ],
        "explanation": (
            "STP root port selection uses four tiebreakers in sequence: lowest root BID, lowest root "
            "path cost, lowest sender BID, lowest sender port ID. When two ports on the same switch "
            "connect to the same upstream switch (equal cost, same sender), tiebreakers 1-3 tie. "
            "The local port with the lowest port ID (priority.port-number) wins. "
            "Default port priority is 128; the port number acts as the final tie-break."
        ),
    },
    {
        "id": "cd2-022",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "PortFast & BPDU Guard",
        "stem": (
            "An engineer configures PortFast globally with 'spanning-tree portfast default'. "
            "Which ports does this command affect?"
        ),
        "options": [
            {
                "id": "a",
                "text": "All switch ports, including trunk ports and port-channels.",
                "correct": False,
                "rationale": (
                    "Incorrect. 'spanning-tree portfast default' only applies PortFast to access ports. "
                    "Trunk ports and port-channels are excluded because they are expected to connect to "
                    "other switches where PortFast would be inappropriate."
                ),
            },
            {
                "id": "b",
                "text": "Only access ports; trunk ports are excluded from the global PortFast default.",
                "correct": True,
                "rationale": (
                    "Correct. The 'spanning-tree portfast default' global command enables PortFast on "
                    "all nontrunking access ports. Trunk ports are not affected and continue to "
                    "participate in normal STP negotiation."
                ),
            },
            {
                "id": "c",
                "text": "Only ports that have been manually configured with 'spanning-tree portfast' interface-level command.",
                "correct": False,
                "rationale": (
                    "Incorrect. The global command 'spanning-tree portfast default' enables PortFast on "
                    "all eligible access ports without requiring per-interface configuration. The "
                    "per-interface 'spanning-tree portfast' command is an alternative, not a requirement."
                ),
            },
            {
                "id": "d",
                "text": "Uplink ports only, to speed up root port election.",
                "correct": False,
                "rationale": (
                    "Incorrect. PortFast is designed for edge (host-facing) access ports, not uplinks. "
                    "Applying it to uplinks connected to other switches would risk STP topology issues."
                ),
            },
        ],
        "explanation": (
            "'spanning-tree portfast default' is a global shortcut that enables PortFast on all "
            "operational access ports — specifically ports in 'switchport mode access' or 'dynamic' "
            "mode when they come up as access. Trunk ports are explicitly excluded. PortFast on "
            "access ports eliminates the 30-second wait for hosts to get network access on connect."
        ),
    },
    # -------------------------------------------------------------------------
    # 2.6 – Wireless architectures and AP modes
    # -------------------------------------------------------------------------
    {
        "id": "cd2-023",
        "domain": 2,
        "objective": "2.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Wireless architectures & AP modes",
        "stem": (
            "A company is deploying wireless at a remote branch office that has intermittent WAN "
            "connectivity to the central Cisco WLC. Which AP mode allows the AP to continue serving "
            "wireless clients locally even when WLC connectivity is lost?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Local mode",
                "correct": False,
                "rationale": (
                    "Incorrect. In local mode (the default lightweight AP mode), all client data traffic "
                    "is tunneled through the CAPWAP tunnel to the WLC. If WLC connectivity is lost, "
                    "the AP cannot serve clients independently."
                ),
            },
            {
                "id": "b",
                "text": "FlexConnect mode",
                "correct": True,
                "rationale": (
                    "Correct. FlexConnect (formerly H-REAP) allows APs at remote/branch sites to "
                    "switch traffic locally and authenticate clients locally when the WLC is unreachable. "
                    "It provides resiliency for branch office deployments with unreliable WAN links."
                ),
            },
            {
                "id": "c",
                "text": "Monitor mode",
                "correct": False,
                "rationale": (
                    "Incorrect. Monitor mode dedicates the AP to scanning for rogue APs, clients, "
                    "and wireless intrusions. It does NOT serve client data traffic and cannot be "
                    "used as a solution for branch connectivity."
                ),
            },
            {
                "id": "d",
                "text": "Sniffer mode",
                "correct": False,
                "rationale": (
                    "Incorrect. Sniffer mode captures 802.11 frames and forwards them to a protocol "
                    "analyzer (like Wireshark). It does not serve wireless clients."
                ),
            },
        ],
        "explanation": (
            "FlexConnect mode is specifically designed for branch/remote office deployments. "
            "In 'connected state' (WLC reachable), the AP can switch traffic locally and authenticate "
            "centrally. In 'standalone state' (WLC unreachable), it can continue switching traffic "
            "locally and authenticating against a local authentication list. "
            "Local mode APs become non-functional for clients if the WLC CAPWAP tunnel drops."
        ),
    },
    {
        "id": "cd2-024",
        "domain": 2,
        "objective": "2.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Wireless architectures & AP modes",
        "stem": (
            "Which statement BEST describes the split-MAC architecture used by lightweight APs "
            "with a Cisco WLC?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The AP handles all 802.11 management frames (beacons, probes, association) and "
                    "all security/QoS processing; the WLC only monitors the RF environment."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. In a split-MAC architecture, the AP handles time-sensitive real-time "
                    "functions (beacons, probes, ACK, data encryption/decryption). The WLC handles "
                    "non-time-sensitive functions AND security/QoS policy, not just RF monitoring."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The AP handles real-time 802.11 functions (beacons, ACKs, data encryption) while "
                    "the WLC handles association, authentication, roaming, and RF management."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Split-MAC divides 802.11 MAC functions between the AP and WLC. "
                    "Time-sensitive functions (beacon generation, probe responses, ACKs, per-frame "
                    "encryption/decryption) stay on the AP. The WLC centrally manages association "
                    "requests, 802.1X authentication, roaming, and RF parameter management via CAPWAP."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The AP operates completely independently, using a WLC only for initial provisioning "
                    "and configuration updates pushed via CAPWAP."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This describes an autonomous AP scenario with a management system, not "
                    "a split-MAC lightweight AP. Lightweight APs require the WLC for ongoing operations, "
                    "not just initial provisioning."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Both the AP and the WLC independently maintain a full copy of the 802.11 MAC "
                    "state machine for redundancy, synchronizing state via CAPWAP keepalives."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Split-MAC is a division of labor, not a redundancy mechanism. "
                    "The two components handle different parts of the MAC; they are not independent "
                    "duplicates of the same function."
                ),
            },
        ],
        "explanation": (
            "The split-MAC architecture is the fundamental design of the Cisco Unified Wireless Network. "
            "CAPWAP (Control and Provisioning of Wireless Access Points) tunnels both control traffic "
            "and client data between the AP and WLC. Real-time 802.11 operations stay on the AP for "
            "performance; centralized management, security policy, and roaming are handled by the WLC. "
            "This enables consistent policy enforcement and simplified management of large AP deployments."
        ),
    },
    {
        "id": "cd2-025",
        "domain": 2,
        "objective": "2.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Wireless architectures & AP modes",
        "stem": (
            "A wireless engineer needs to place an AP in a mode that allows it to function as a "
            "standalone AP without a WLC, managing its own SSIDs, security, and radio configuration. "
            "Which AP mode should be used?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Autonomous mode",
                "correct": True,
                "rationale": (
                    "Correct. An autonomous AP contains full 802.11 MAC and management functionality "
                    "and operates independently without a WLC. It is configured directly via CLI, "
                    "Cisco Prime, or web GUI, and manages its own SSIDs, security, and RF parameters."
                ),
            },
            {
                "id": "b",
                "text": "FlexConnect mode",
                "correct": False,
                "rationale": (
                    "Incorrect. FlexConnect is a mode for lightweight APs that provides local switching "
                    "and survivability during WLC outages, but it still requires a WLC for initial join "
                    "and ongoing management. It is not a fully autonomous mode."
                ),
            },
            {
                "id": "c",
                "text": "Local mode with HA SSO",
                "correct": False,
                "rationale": (
                    "Incorrect. Local mode with HA SSO is used for high-availability failover between "
                    "two WLCs. It requires a WLC and is not an autonomous standalone operation."
                ),
            },
            {
                "id": "d",
                "text": "Bridge mode",
                "correct": False,
                "rationale": (
                    "Incorrect. Bridge mode (also called outdoor/mesh bridge mode) is used to create "
                    "wireless bridges between buildings or to form mesh networks. It still operates "
                    "under WLC control for mesh APs."
                ),
            },
        ],
        "explanation": (
            "Autonomous APs run a full IOS image and operate as self-contained wireless devices. "
            "They were the original Cisco wireless AP design. The shift to lightweight/split-MAC "
            "APs + WLC addressed scalability: managing hundreds of autonomous APs individually is "
            "impractical. Autonomous APs are still used in small deployments or where a WLC is not available."
        ),
    },
    # -------------------------------------------------------------------------
    # 2.7 – Physical infrastructure: AP, WLC, access/trunk ports, LAG
    # -------------------------------------------------------------------------
    {
        "id": "cd2-026",
        "domain": 2,
        "objective": "2.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "WLC management access",
        "stem": (
            "A Cisco WLC connects to a distribution switch. Multiple WLANs map to multiple VLANs. "
            "What is the CORRECT port configuration on the switch port connecting to the WLC's "
            "distribution system interface?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The switch port should be configured as an access port in the management VLAN.",
                "correct": False,
                "rationale": (
                    "Incorrect. An access port can carry only one VLAN. Since multiple WLANs map to "
                    "multiple VLANs, the WLC needs to carry multiple VLANs. A trunk port is required."
                ),
            },
            {
                "id": "b",
                "text": "The switch port should be configured as an 802.1Q trunk carrying all WLAN VLANs.",
                "correct": True,
                "rationale": (
                    "Correct. The WLC's distribution system port (physical or LAG) connects to the "
                    "switch as an 802.1Q trunk. Each WLAN is mapped to a VLAN/interface on the WLC, "
                    "and client traffic is tagged with the corresponding VLAN as it exits the WLC "
                    "toward the switch."
                ),
            },
            {
                "id": "c",
                "text": "The switch port should use PAgP EtherChannel to all WLC interfaces for redundancy.",
                "correct": False,
                "rationale": (
                    "Incorrect. Cisco WLCs use LAG (Link Aggregation using 802.3ad/LACP), not PAgP, "
                    "for port bundling. Also, the question asks about the switch port configuration type "
                    "(access vs. trunk), where trunk is the correct answer regardless of LAG."
                ),
            },
            {
                "id": "d",
                "text": "The switch port should be a routed port with an IP address in each WLAN subnet.",
                "correct": False,
                "rationale": (
                    "Incorrect. The WLC uses Layer 2 trunk connectivity to the switch. SVIs on the "
                    "Layer 3 switch (not on the connecting port) provide inter-VLAN routing. "
                    "The switch port to the WLC is a Layer 2 trunk port."
                ),
            },
        ],
        "explanation": (
            "In a Cisco WLC deployment, the WLC's distribution system port connects to a switch via "
            "an 802.1Q trunk. Each WLAN is associated with an 'interface' on the WLC that maps to "
            "a specific VLAN. Client traffic exits the WLC tagged with the correct VLAN and is "
            "carried across the trunk to the appropriate Layer 3 gateway (SVI) on the switch."
        ),
    },
    {
        "id": "cd2-027",
        "domain": 2,
        "objective": "2.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "WLC management access",
        "stem": (
            "A WLC has multiple physical ports. The network engineer wants to bundle them into a "
            "single logical link for redundancy and bandwidth. What feature must be configured on "
            "BOTH the WLC and the connected switch?"
        ),
        "options": [
            {
                "id": "a",
                "text": "PAgP EtherChannel, because WLCs use Cisco-proprietary protocols.",
                "correct": False,
                "rationale": (
                    "Incorrect. Cisco WLCs use IEEE 802.3ad LAG (LACP), not the Cisco-proprietary "
                    "PAgP protocol. The switch must also be configured with LACP to match."
                ),
            },
            {
                "id": "b",
                "text": "LAG (Link Aggregation Group) using 802.3ad/LACP on both the WLC and the switch.",
                "correct": True,
                "rationale": (
                    "Correct. Cisco WLCs support LAG using the IEEE 802.3ad standard (LACP). "
                    "When LAG is enabled on the WLC, all physical ports are bundled into a single "
                    "logical port-channel. The switch must be configured with a matching LACP "
                    "port-channel for the link to aggregate successfully."
                ),
            },
            {
                "id": "c",
                "text": "Port redundancy using WLC port mirroring to a standby physical port.",
                "correct": False,
                "rationale": (
                    "Incorrect. Port mirroring (SPAN) is used for traffic capture/monitoring, not "
                    "for link aggregation or redundancy. LAG is the correct mechanism."
                ),
            },
            {
                "id": "d",
                "text": "HSRP between the two WLC physical ports for gateway redundancy.",
                "correct": False,
                "rationale": (
                    "Incorrect. HSRP is a router redundancy protocol for default gateways, not a "
                    "physical port bundling mechanism. LAG bundles physical ports at Layer 2."
                ),
            },
        ],
        "explanation": (
            "Cisco WLCs support LAG (Link Aggregation Group) for port bundling. When LAG is enabled, "
            "all WLC distribution system ports form a single LAG bundle. The switch must be configured "
            "with a matching LACP port-channel. An important WLC LAG consideration: enabling/disabling "
            "LAG requires a WLC reboot. All WLC interfaces (management, AP-manager, dynamic) run "
            "over the single LAG."
        ),
    },
    {
        "id": "cd2-028",
        "domain": 2,
        "objective": "2.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "WLC management access",
        "stem": (
            "In a Cisco WLC deployment, lightweight APs communicate with the WLC using CAPWAP. "
            "Which TWO UDP ports are used by CAPWAP? (Choose the option listing both correct ports.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "UDP 5246 (control) and UDP 5247 (data)",
                "correct": True,
                "rationale": (
                    "Correct. CAPWAP uses UDP port 5246 for the control channel (AP-WLC management "
                    "and configuration) and UDP port 5247 for the data channel (tunneled client data "
                    "traffic in local/central switching mode)."
                ),
            },
            {
                "id": "b",
                "text": "UDP 1812 (control) and UDP 1813 (data)",
                "correct": False,
                "rationale": (
                    "Incorrect. UDP 1812 and 1813 are RADIUS Authentication and Accounting ports, "
                    "respectively. They are not CAPWAP ports."
                ),
            },
            {
                "id": "c",
                "text": "TCP 443 (control) and UDP 5246 (data)",
                "correct": False,
                "rationale": (
                    "Incorrect. CAPWAP uses UDP for both control and data, not TCP. TCP 443 is HTTPS "
                    "for the WLC web management interface."
                ),
            },
            {
                "id": "d",
                "text": "UDP 500 (control) and UDP 4500 (data)",
                "correct": False,
                "rationale": (
                    "Incorrect. UDP 500 and 4500 are used by IKE and IPsec NAT-T for VPN tunnels, "
                    "not for CAPWAP."
                ),
            },
        ],
        "explanation": (
            "CAPWAP (RFC 5415) uses two UDP ports: 5246 for the control plane (AP discovery, "
            "configuration, statistics) and 5247 for the data plane (encapsulated client data frames). "
            "CAPWAP replaced the proprietary LWAPP protocol (UDP 12222/12223 — also worth knowing). "
            "These ports must be permitted in any ACL or firewall between APs and the WLC."
        ),
    },
    # -------------------------------------------------------------------------
    # 2.8 – AP and WLC management access
    # -------------------------------------------------------------------------
    {
        "id": "cd2-029",
        "domain": 2,
        "objective": "2.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "WLC management access",
        "stem": (
            "A network engineer needs to provide centralized AAA for WLC administrator logins. "
            "Cisco's recommended approach is to use RADIUS or TACACS+. What is the key operational "
            "difference between TACACS+ and RADIUS for WLC management access?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "TACACS+ encrypts only the password in the access-request packet; "
                    "RADIUS encrypts the entire payload."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is the opposite of reality. RADIUS encrypts only the password "
                    "field in the Access-Request. TACACS+ encrypts the entire body of every packet "
                    "(except the header), providing more comprehensive encryption."
                ),
            },
            {
                "id": "b",
                "text": (
                    "TACACS+ uses TCP and separates authentication, authorization, and accounting; "
                    "RADIUS uses UDP and combines authentication and authorization in a single exchange."
                ),
                "correct": True,
                "rationale": (
                    "Correct. TACACS+ uses TCP port 49 and provides separate AAA services — each can "
                    "be handled independently, allowing granular command authorization. RADIUS uses UDP "
                    "(ports 1812/1813) and combines authentication and authorization in a single "
                    "Access-Request/Access-Accept exchange."
                ),
            },
            {
                "id": "c",
                "text": (
                    "RADIUS supports per-command authorization for device management; "
                    "TACACS+ is used only for 802.1X wireless client authentication."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. TACACS+ is typically used for per-command device management authorization "
                    "due to its AAA separation. RADIUS is commonly used for 802.1X client authentication. "
                    "The answer has these roles reversed."
                ),
            },
            {
                "id": "d",
                "text": (
                    "TACACS+ and RADIUS are functionally identical for WLC management; the choice "
                    "is purely vendor-dependent with no operational differences."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. TACACS+ and RADIUS have significant operational differences: transport "
                    "protocol (TCP vs. UDP), encryption scope, and AAA separation. These differences "
                    "affect their suitability for different use cases."
                ),
            },
        ],
        "explanation": (
            "TACACS+ (TCP/49, Cisco proprietary) encrypts the full packet body and provides separate "
            "authentication, authorization, and accounting services, making it ideal for device "
            "management with granular command-level authorization. RADIUS (UDP/1812-1813, open standard) "
            "combines auth+authz, encrypts only the password, and is preferred for wireless client "
            "802.1X authentication at scale."
        ),
    },
    {
        "id": "cd2-030",
        "domain": 2,
        "objective": "2.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "WLC management access",
        "stem": (
            "An engineer wants to access the WLC CLI for initial configuration. The WLC has not yet "
            "been configured with an IP address. Which management access method is available?"
        ),
        "options": [
            {
                "id": "a",
                "text": "SSH to the WLC management IP address.",
                "correct": False,
                "rationale": (
                    "Incorrect. SSH requires an IP address to be reachable. Without a configured "
                    "management IP, SSH cannot be established over the network."
                ),
            },
            {
                "id": "b",
                "text": "Console port access.",
                "correct": True,
                "rationale": (
                    "Correct. The console port provides out-of-band access that does not require "
                    "any network configuration. It is the only method available when the WLC has "
                    "no IP address configured, making it essential for initial setup."
                ),
            },
            {
                "id": "c",
                "text": "HTTP to the WLC's default factory IP of 192.168.1.1.",
                "correct": False,
                "rationale": (
                    "Incorrect. Cisco WLCs do not ship with a default factory IP address for "
                    "HTTP management access. The console port is used for initial configuration."
                ),
            },
            {
                "id": "d",
                "text": "Telnet to the WLC using the APIC-EM discovery protocol.",
                "correct": False,
                "rationale": (
                    "Incorrect. APIC-EM is a network management platform, not a protocol for "
                    "accessing unconfigured WLCs. Telnet requires IP connectivity, which is not "
                    "available on an unconfigured WLC."
                ),
            },
        ],
        "explanation": (
            "The console port is the mandatory starting point for WLC initial configuration. "
            "The initial setup wizard runs over the console to configure the management interface "
            "IP address, service port, and other basic parameters. Once IP is configured, "
            "SSH (recommended over Telnet for security) and HTTPS GUI access become available."
        ),
    },
    {
        "id": "cd2-031",
        "domain": 2,
        "objective": "2.8",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "WLC management access",
        "stem": (
            "Which TWO management access methods are available on a Cisco WLC that provide "
            "encrypted in-band management? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Telnet",
                "correct": False,
                "rationale": (
                    "Incorrect. Telnet transmits all data, including credentials, in plaintext. "
                    "It provides no encryption and is not recommended for secure management."
                ),
            },
            {
                "id": "b",
                "text": "SSH",
                "correct": True,
                "rationale": (
                    "Correct. SSH (Secure Shell) provides encrypted CLI access to the WLC over "
                    "the network. It encrypts all session data including credentials and commands."
                ),
            },
            {
                "id": "c",
                "text": "HTTP",
                "correct": False,
                "rationale": (
                    "Incorrect. HTTP transmits data in plaintext. While the WLC GUI may be accessible "
                    "via HTTP, it is not encrypted and is not a secure management method."
                ),
            },
            {
                "id": "d",
                "text": "HTTPS",
                "correct": True,
                "rationale": (
                    "Correct. HTTPS provides encrypted web-based GUI access to the WLC. "
                    "It uses TLS/SSL to encrypt all management traffic between the browser and the WLC."
                ),
            },
        ],
        "explanation": (
            "Cisco WLC supports multiple management access methods: Console (out-of-band, no "
            "encryption needed), Telnet (in-band, unencrypted — not recommended), SSH (in-band, "
            "encrypted CLI), HTTP (in-band, unencrypted GUI — not recommended), HTTPS (in-band, "
            "encrypted GUI). For secure management, SSH and HTTPS are the recommended in-band "
            "encrypted options."
        ),
    },
    # -------------------------------------------------------------------------
    # 2.9 – Wireless LAN GUI configuration
    # -------------------------------------------------------------------------
    {
        "id": "cd2-032",
        "domain": 2,
        "objective": "2.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "WLAN GUI configuration",
        "stem": (
            "A network engineer is creating a new WLAN on a Cisco WLC for corporate users. "
            "The security requirement is WPA2 with 802.1X authentication to a RADIUS server. "
            "In the WLC GUI, which security settings must be configured? (Choose the BEST answer.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Layer 2 Security: WPA+WPA2 with 802.1X; configure RADIUS server AAA settings.",
                "correct": True,
                "rationale": (
                    "Correct. In the Cisco WLC GUI, WLAN security is configured under the 'Security' "
                    "tab. For WPA2 with 802.1X, Layer 2 Security is set to 'WPA+WPA2', WPA2 Policy "
                    "is enabled, WPA2 Encryption is AES (CCMP), and Auth Key Mgmt is set to 802.1X. "
                    "The RADIUS server must also be added in the AAA section."
                ),
            },
            {
                "id": "b",
                "text": "Layer 2 Security: WPA+WPA2 with PSK; enter a pre-shared key for corporate users.",
                "correct": False,
                "rationale": (
                    "Incorrect. PSK (Pre-Shared Key) does not provide per-user authentication and "
                    "is not suitable for enterprise corporate deployments that require 802.1X. "
                    "The requirement specifies 802.1X, which uses a RADIUS server."
                ),
            },
            {
                "id": "c",
                "text": "Layer 3 Security: Web Authentication with RADIUS passthrough.",
                "correct": False,
                "rationale": (
                    "Incorrect. Web Authentication (web auth) is a Layer 3 mechanism typically used "
                    "for guest networks, not for WPA2/802.1X enterprise authentication. "
                    "WPA2/802.1X is a Layer 2 security setting."
                ),
            },
            {
                "id": "d",
                "text": "Layer 2 Security: Static WEP with RADIUS server key management.",
                "correct": False,
                "rationale": (
                    "Incorrect. WEP (Wired Equivalent Privacy) is a deprecated, cryptographically "
                    "broken security protocol. The requirement specifies WPA2, which uses TKIP "
                    "or AES/CCMP — not WEP."
                ),
            },
        ],
        "explanation": (
            "In Cisco WLC GUI WLAN configuration, the Security tab has Layer 2 and Layer 3 security. "
            "For WPA2-Enterprise (802.1X): Layer 2 Security = WPA+WPA2, enable WPA2 Policy with "
            "AES encryption, Auth Key Mgmt = 802.1X. A RADIUS server must be configured under "
            "Security > AAA > RADIUS > Authentication and referenced in the WLAN. This provides "
            "per-user authentication with RADIUS-assigned attributes."
        ),
    },
    {
        "id": "cd2-033",
        "domain": 2,
        "objective": "2.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "WLAN GUI configuration",
        "stem": (
            "When configuring a WLAN on a Cisco WLC, an engineer sets the QoS profile to 'Platinum'. "
            "What does this QoS profile primarily affect?"
        ),
        "options": [
            {
                "id": "a",
                "text": "It assigns DSCP EF (46) to all traffic on the WLAN, guaranteeing bandwidth for all users.",
                "correct": False,
                "rationale": (
                    "Incorrect. The WLC QoS profile sets the maximum 802.11e (WMM) priority class "
                    "for traffic entering the WLAN. It does not automatically mark all traffic with "
                    "DSCP EF or guarantee bandwidth — it sets the upper bound for the QoS treatment."
                ),
            },
            {
                "id": "b",
                "text": (
                    "It sets the maximum user priority allowed on the WLAN; Platinum allows voice-level "
                    "(WMM AC_VO) traffic and is used for VoIP WLANs."
                ),
                "correct": True,
                "rationale": (
                    "Correct. WLC QoS profiles (Platinum, Gold, Silver, Bronze) set the maximum "
                    "802.11e WMM access category (AC) for traffic on that WLAN. Platinum maps to "
                    "AC_VO (voice), the highest priority. It is recommended for voice/VoIP WLANs "
                    "so that voice frames receive preferential treatment."
                ),
            },
            {
                "id": "c",
                "text": "It enables DSCP trust on the WLAN so that client-marked DSCP values are preserved end-to-end.",
                "correct": False,
                "rationale": (
                    "Incorrect. By default, WLCs do not trust client DSCP markings. The QoS profile "
                    "sets the WMM priority for the WLAN, not DSCP trust behavior. DSCP trust must "
                    "be separately configured if needed."
                ),
            },
            {
                "id": "d",
                "text": "It applies rate limiting per client, with Platinum providing the highest maximum throughput.",
                "correct": False,
                "rationale": (
                    "Incorrect. QoS profiles on the WLC control traffic priority (WMM access categories), "
                    "not per-client rate limiting. Bandwidth contracts are configured separately in "
                    "the WLC QoS configuration for per-client rate limiting."
                ),
            },
        ],
        "explanation": (
            "Cisco WLC QoS profiles map to WMM (Wi-Fi Multimedia) access categories: "
            "Platinum = AC_VO (voice), Gold = AC_VI (video), Silver = AC_BE (best effort, default), "
            "Bronze = AC_BK (background). The profile sets the maximum WMM priority allowed for "
            "that WLAN. Platinum is recommended for VoIP SSIDs; using Platinum for data-only WLANs "
            "can cause voice quality issues if voice ACs are congested by data traffic."
        ),
    },
    {
        "id": "cd2-034",
        "domain": 2,
        "objective": "2.9",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "WLAN GUI configuration",
        "stem": (
            "A wireless engineer is configuring WPA3 on a new Cisco WLC WLAN. Which statement "
            "CORRECTLY describes a key security improvement of WPA3 over WPA2 in the personal (PSK) mode?"
        ),
        "options": [
            {
                "id": "a",
                "text": "WPA3-Personal uses SAE (Simultaneous Authentication of Equals) instead of PSK, eliminating offline dictionary attacks.",
                "correct": True,
                "rationale": (
                    "Correct. WPA3-Personal replaces the PSK four-way handshake with SAE (based on "
                    "Dragonfly key exchange). SAE provides forward secrecy and is resistant to offline "
                    "dictionary/brute-force attacks because the handshake does not expose a verifiable "
                    "hash of the passphrase."
                ),
            },
            {
                "id": "b",
                "text": "WPA3-Personal uses AES-256 encryption instead of the AES-128 (CCMP) used by WPA2.",
                "correct": False,
                "rationale": (
                    "Incorrect. WPA3-Personal still uses CCMP-128 (AES-128) as the default encryption. "
                    "WPA3-Enterprise can optionally use 192-bit (CNSA suite). The key improvement in "
                    "WPA3-Personal is the SAE key exchange, not a change in encryption strength."
                ),
            },
            {
                "id": "c",
                "text": "WPA3-Personal requires a RADIUS server for authentication, eliminating shared passwords.",
                "correct": False,
                "rationale": (
                    "Incorrect. WPA3-Personal still uses a shared passphrase (no RADIUS). "
                    "WPA3-Enterprise uses 802.1X with RADIUS. WPA3-Personal improves PSK security "
                    "through SAE, not by requiring per-user RADIUS authentication."
                ),
            },
            {
                "id": "d",
                "text": "WPA3-Personal introduces Protected Management Frames (PMF) as optional to reduce deauthentication attacks.",
                "correct": False,
                "rationale": (
                    "Incorrect. PMF (802.11w) was introduced with WPA2, not WPA3. In WPA3, PMF is "
                    "MANDATORY, not optional. The primary WPA3-Personal improvement is SAE over PSK."
                ),
            },
        ],
        "explanation": (
            "WPA3 (Wi-Fi Alliance 2018) key improvements: Personal mode uses SAE (Simultaneous "
            "Authentication of Equals / Dragonfly) instead of the 4-way handshake, providing "
            "forward secrecy and protection against offline dictionary attacks. Enterprise mode "
            "optionally supports 192-bit security (CNSA suite). Both modes mandate PMF (802.11w). "
            "WPA3 is backward compatible with WPA2 devices in transition mode."
        ),
    },
    {
        "id": "cd2-035",
        "domain": 2,
        "objective": "2.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "WLAN GUI configuration",
        "stem": (
            "On a Cisco WLC, an engineer navigates to WLANs > Edit > Advanced tab for a WLAN. "
            "Which configuration option is found in the Advanced tab that is NOT found in the General tab?"
        ),
        "options": [
            {
                "id": "a",
                "text": "SSID name and WLAN ID",
                "correct": False,
                "rationale": (
                    "Incorrect. The SSID (profile name) and WLAN ID are configured in the General tab "
                    "of the WLAN editor, not the Advanced tab."
                ),
            },
            {
                "id": "b",
                "text": "Coverage Hole Detection and client load balancing settings",
                "correct": True,
                "rationale": (
                    "Correct. Advanced WLAN settings include client load balancing (band select, "
                    "client balancing between APs), coverage hole detection, P2P blocking, "
                    "DHCP required, 7920 AP CAC, and other fine-tuning options not available on "
                    "the General tab."
                ),
            },
            {
                "id": "c",
                "text": "Interface/interface group assignment for the WLAN",
                "correct": False,
                "rationale": (
                    "Incorrect. The interface/interface group assignment (which VLAN/dynamic interface "
                    "the WLAN maps to) is configured in the General tab of the WLAN editor."
                ),
            },
            {
                "id": "d",
                "text": "WPA2 versus WPA3 security selection",
                "correct": False,
                "rationale": (
                    "Incorrect. Security settings (WPA2/WPA3, PSK, 802.1X, Layer 3 web auth) are "
                    "found in the Security tab of the WLAN editor, not the Advanced tab."
                ),
            },
        ],
        "explanation": (
            "The Cisco WLC WLAN editor has multiple tabs: General (SSID, status, interface, broadcast), "
            "Security (Layer 2: WPA2/3, Layer 3: web auth), QoS (profile, rate limiting, WMM), "
            "Policy-Mapping, and Advanced (load balancing, coverage hole detection, P2P blocking, "
            "DHCP required, off-channel scanning, mDNS, etc.). Understanding which options live "
            "in which tab is a common exam topic."
        ),
    },
    # -------------------------------------------------------------------------
    # Additional questions — mixed objectives to reach 40, deeper coverage
    # -------------------------------------------------------------------------
    {
        "id": "cd2-036",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Spanning Tree (RPVST+)",
        "stem": (
            "An engineer wants to make SW1 the root bridge for VLAN 20. The current root bridge "
            "has a bridge priority of 24576 for VLAN 20. SW1 currently has the default STP priority. "
            "Which command on SW1 will ensure it becomes and remains the root bridge for VLAN 20?"
        ),
        "options": [
            {
                "id": "a",
                "text": "spanning-tree vlan 20 priority 28672",
                "correct": False,
                "rationale": (
                    "Incorrect. A priority of 28672 is still higher than the current root's 24576. "
                    "SW1 would not win the root election with this priority."
                ),
            },
            {
                "id": "b",
                "text": "spanning-tree vlan 20 root primary",
                "correct": True,
                "rationale": (
                    "Correct. 'spanning-tree vlan 20 root primary' is a macro that automatically sets "
                    "SW1's priority to either 24576 or 4096 less than the current root's priority "
                    "(whichever results in SW1 winning). It ensures SW1 becomes the root bridge."
                ),
            },
            {
                "id": "c",
                "text": "spanning-tree vlan 20 priority 0",
                "correct": False,
                "rationale": (
                    "Incorrect. While priority 0 would make SW1 the root, 'spanning-tree vlan 20 "
                    "root primary' is the recommended approach. However, priority 0 is a technically "
                    "valid value. The 'root primary' macro is the exam-recommended best practice. "
                    "Note: priority must be in increments of 4096."
                ),
            },
            {
                "id": "d",
                "text": "spanning-tree vlan 20 forward-time 4",
                "correct": False,
                "rationale": (
                    "Incorrect. 'forward-time' adjusts the STP forwarding delay timer, not the bridge "
                    "priority. It does not influence root bridge election."
                ),
            },
        ],
        "explanation": (
            "'spanning-tree vlan X root primary' is a Cisco IOS macro command. It checks the current "
            "root's bridge priority and sets the local bridge priority to either 24576 or the current "
            "root's priority minus 4096 (whichever is lower), ensuring this switch wins the election. "
            "STP priorities must be multiples of 4096. The equivalent manual command would require "
            "knowing the current root's priority and calculating the correct value."
        ),
    },
    {
        "id": "cd2-037",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "VLANs",
        "stem": (
            "A switch is running VTP version 2 in server mode with VTP domain 'CAMPUS' and "
            "revision number 15. A new switch is added to the network with VTP client mode, "
            "VTP domain 'CAMPUS', but configuration revision number 22. What happens when "
            "the new switch is connected via a trunk port?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The VTP server's VLAN database (revision 15) is sent to the new client switch "
                    "and overwrites its higher revision number."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. VTP synchronization sends the database with the HIGHEST revision "
                    "number to other switches. The client switch with revision 22 has a higher "
                    "revision number, so its database propagates to the server."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The new client switch (revision 22) overwrites the VTP server's VLAN database "
                    "because it has a higher revision number, potentially deleting production VLANs."
                ),
                "correct": True,
                "rationale": (
                    "Correct. VTP version 2 propagates the VLAN database with the highest revision "
                    "number. The client at revision 22 beats the server at revision 15. This is the "
                    "classic 'VTP bomb' scenario where adding a used or misconfigured switch can "
                    "overwrite the production VLAN database, deleting VLANs and causing outages."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The two switches detect a revision number conflict and both go into transparent "
                    "mode to prevent database corruption."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. VTP does not have a conflict-resolution mechanism that triggers "
                    "transparent mode. The higher revision number simply wins, overwriting the "
                    "lower-revision database."
                ),
            },
            {
                "id": "d",
                "text": (
                    "VTP client mode prevents the new switch from advertising its VLAN database; "
                    "only VTP servers can send VTP advertisements."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. VTP clients forward VTP advertisements received from servers. However, "
                    "in this scenario the client has a higher revision number and its database is "
                    "propagated. This is a well-documented security/operational risk of VTP."
                ),
            },
        ],
        "explanation": (
            "The 'VTP bomb' is a real-world danger: any switch with the same VTP domain and a higher "
            "revision number will overwrite the VLAN database of all other switches in the domain "
            "when connected via a trunk. Mitigation strategies: use VTP version 3 (which has a "
            "primary server concept), reset the revision number to 0 before connecting new switches "
            "(change domain name and change back), or use VTP transparent mode."
        ),
    },
    {
        "id": "cd2-038",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "EtherChannel",
        "stem": (
            "An engineer is troubleshooting an EtherChannel that is not forming between SW1 and SW2. "
            "Which TWO misconfigurations would PREVENT the EtherChannel from forming? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "SW1 member ports are configured as trunk; SW2 member ports are configured as access.",
                "correct": True,
                "rationale": (
                    "Correct. All member ports in an EtherChannel must have the same Layer 2 "
                    "configuration. A mismatch between trunk and access mode on member ports "
                    "will prevent the bundle from forming."
                ),
            },
            {
                "id": "b",
                "text": "SW1 uses port-channel group 1; SW2 uses port-channel group 2.",
                "correct": False,
                "rationale": (
                    "Incorrect. Port-channel group numbers are locally significant and do not need "
                    "to match between the two switches. LACP uses system IDs and port keys "
                    "for negotiation, not group numbers."
                ),
            },
            {
                "id": "c",
                "text": "SW1 is configured with 'channel-group 1 mode passive'; SW2 is also configured with 'channel-group 1 mode passive'.",
                "correct": True,
                "rationale": (
                    "Correct. LACP passive + passive will NOT form an EtherChannel because neither "
                    "side initiates LACP PDUs. At least one side must be in 'active' mode."
                ),
            },
            {
                "id": "d",
                "text": "SW1 has LACP system priority 100; SW2 has LACP system priority 200.",
                "correct": False,
                "rationale": (
                    "Incorrect. Different LACP system priorities are resolved through LACP negotiation. "
                    "The switch with the lower system priority becomes the controlling system. "
                    "This does not prevent the EtherChannel from forming."
                ),
            },
        ],
        "explanation": (
            "EtherChannel formation requires: (1) compatible negotiation modes (not passive+passive "
            "or on+active/passive), and (2) matching Layer 2 parameters on member ports of the same "
            "switch (mode, VLAN assignments, trunk settings). LACP system priority differences and "
            "local port-channel group number differences do NOT prevent formation."
        ),
    },
    {
        "id": "cd2-039",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Trunking & 802.1Q",
        "stem": (
            "A security engineer is hardening switch configurations. They want to prevent VLAN "
            "hopping attacks by mitigating double-tagging. Which configuration change is the MOST "
            "effective countermeasure?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Enable BPDU Guard on all access ports.",
                "correct": False,
                "rationale": (
                    "Incorrect. BPDU Guard protects against unauthorized switches being connected to "
                    "access ports; it does not prevent double-tagging VLAN hopping attacks."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Change the native VLAN on all trunk ports to an unused VLAN ID (not VLAN 1) "
                    "and ensure no access ports are assigned to that native VLAN."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Double-tagging attacks exploit the native VLAN. An attacker sends frames "
                    "with two 802.1Q tags: the outer tag matching the native VLAN (stripped by the "
                    "first switch) and the inner tag for the target VLAN. By changing the native VLAN "
                    "to an unused, dedicated VLAN, the attack is prevented because the outer tag will "
                    "not match any VLAN with real traffic or end hosts."
                ),
            },
            {
                "id": "c",
                "text": "Enable DTP on all trunk ports to ensure proper trunking negotiation.",
                "correct": False,
                "rationale": (
                    "Incorrect. Enabling DTP does not prevent double-tagging. In fact, security best "
                    "practice recommends DISABLING DTP on trunk ports ('switchport nonegotiate') to "
                    "prevent unauthorized trunk formation."
                ),
            },
            {
                "id": "d",
                "text": "Apply port security with a maximum of 1 MAC address on trunk ports.",
                "correct": False,
                "rationale": (
                    "Incorrect. Port security limits MAC addresses per port and is designed for access "
                    "ports. It does not address or prevent double-tagging VLAN hopping on trunk ports."
                ),
            },
        ],
        "explanation": (
            "Double-tagging VLAN hopping relies on the native VLAN being the same as the attacker's "
            "access VLAN. The switch strips the outer tag (native VLAN) and forwards the frame with "
            "the inner tag to the target VLAN. Mitigations: (1) change native VLAN to an unused "
            "dedicated VLAN, (2) ensure no end hosts are on the native VLAN, (3) use 'vlan dot1q "
            "tag native' to tag native VLAN traffic. These prevent the outer tag from being stripped "
            "and reinjected into the target VLAN."
        ),
    },
    {
        "id": "cd2-040",
        "domain": 2,
        "objective": "2.6",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Wireless architectures & AP modes",
        "stem": (
            "Which TWO statements correctly describe the differences between a Cisco autonomous AP "
            "and a Cisco lightweight (CAPWAP) AP? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "An autonomous AP can be managed individually via CLI/SSH or a web browser "
                    "without requiring a central controller."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Autonomous APs contain full IOS and can be managed individually via "
                    "console, SSH, or HTTP/HTTPS. No WLC is required. This makes them suitable for "
                    "small deployments but difficult to scale."
                ),
            },
            {
                "id": "b",
                "text": (
                    "A lightweight AP requires a WLC to function; it joins the WLC via CAPWAP "
                    "and cannot serve clients independently in local mode."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Lightweight APs in local mode require the WLC for all management and "
                    "data forwarding. Without a CAPWAP tunnel to the WLC, the AP cannot serve "
                    "wireless clients (in local mode). FlexConnect mode provides limited survivability."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Lightweight APs use more powerful hardware than autonomous APs to handle "
                    "the additional processing overhead of the split-MAC architecture."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The split-MAC architecture actually offloads processing from the AP "
                    "to the WLC, potentially allowing lightweight APs to use simpler hardware. "
                    "Hardware capability is not a defining architectural difference."
                ),
            },
            {
                "id": "d",
                "text": (
                    "An autonomous AP uses CAPWAP to tunnel management traffic to a Cisco Prime "
                    "Infrastructure server, which serves as the central controller."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Autonomous APs do NOT use CAPWAP. Cisco Prime Infrastructure (or "
                    "older WCS) manages autonomous APs via SNMP/SSH/HTTP — standard management "
                    "protocols — not CAPWAP. CAPWAP is exclusively for lightweight APs and WLCs."
                ),
            },
        ],
        "explanation": (
            "The fundamental distinction: autonomous APs are self-contained with full IOS, managed "
            "individually, suitable for small deployments. Lightweight APs use split-MAC with CAPWAP "
            "to a WLC, enabling centralized management, consistent policy, seamless roaming, and "
            "scalability to thousands of APs. The trade-off is the requirement for a WLC and the "
            "CAPWAP infrastructure. FlexConnect bridges the gap for branch offices."
        ),
    },
]

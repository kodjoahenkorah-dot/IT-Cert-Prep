QUESTIONS = [
    {
        "id": "cd5-001",
        "domain": 5,
        "objective": "5.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "ACL placement & wildcard masks",
        "stem": (
            "A standard ACL must deny traffic from the 10.10.0.0/22 network. "
            "Which wildcard mask is correct?"
        ),
        "options": [
            {
                "id": "a",
                "text": "access-list 5 deny 10.10.0.0 0.0.3.255",
                "correct": True,
                "rationale": (
                    "Correct. A /22 covers 4 consecutive /24 blocks (10.10.0.0–10.10.3.255). "
                    "The wildcard mask is the inverse of the subnet mask 255.255.252.0, which is 0.0.3.255."
                ),
            },
            {
                "id": "b",
                "text": "access-list 5 deny 10.10.0.0 0.0.0.255",
                "correct": False,
                "rationale": (
                    "Incorrect. 0.0.0.255 is the wildcard for a /24, matching only 10.10.0.0–10.10.0.255, "
                    "not the full /22 range."
                ),
            },
            {
                "id": "c",
                "text": "access-list 5 deny 10.10.0.0 0.0.255.255",
                "correct": False,
                "rationale": (
                    "Incorrect. 0.0.255.255 corresponds to a /16 wildcard, which is far broader "
                    "than the intended /22 range."
                ),
            },
            {
                "id": "d",
                "text": "access-list 5 deny 10.10.0.0 255.255.252.0",
                "correct": False,
                "rationale": (
                    "Incorrect. ACLs require wildcard (inverse) masks, not subnet masks. "
                    "255.255.252.0 is the subnet mask itself and would not match the intended addresses correctly."
                ),
            },
        ],
        "explanation": (
            "To build a wildcard mask, subtract the subnet mask from 255.255.255.255. "
            "For /22 (255.255.252.0): 255.255.255.255 − 255.255.252.0 = 0.0.3.255. "
            "This wildcard matches all 1024 addresses in 10.10.0.0–10.10.3.255. "
            "Standard ACLs (1–99, 1300–1999) filter on source address only and should be "
            "placed close to the destination to avoid blocking traffic prematurely."
        ),
    },
    {
        "id": "cd5-002",
        "domain": 5,
        "objective": "5.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Access control lists (ACLs)",
        "stem": (
            "An extended ACL is applied inbound on the router's Gi0/0 interface (facing the internet). "
            "The ACL contains these entries in order:\n"
            "  10 permit tcp any 192.168.1.0 0.0.0.255 eq 443\n"
            "  20 deny tcp any 192.168.1.0 0.0.0.255 eq 80\n"
            "  30 permit ip any any\n\n"
            "A host on the internet sends an HTTP (port 80) packet to 192.168.1.50. "
            "What happens to the packet?"
        ),
        "options": [
            {
                "id": "a",
                "text": "It is denied by ACE 20 because port 80 does not match ACE 10 and ACE 20 explicitly denies TCP port 80 to 192.168.1.0/24.",
                "correct": True,
                "rationale": (
                    "Correct. ACE 10 checks for TCP destination port 443; the packet is port 80, so it does not match. "
                    "ACE 20 explicitly denies TCP port 80 to 192.168.1.0/24 — this packet matches and is dropped."
                ),
            },
            {
                "id": "b",
                "text": "It is permitted by ACE 30 because ACE 10 and 20 are for different ports.",
                "correct": False,
                "rationale": (
                    "Incorrect. ACLs are processed top-down and stop at the first match. "
                    "The packet matches ACE 20 (TCP port 80 to 192.168.1.0/24) before reaching ACE 30."
                ),
            },
            {
                "id": "c",
                "text": "It is dropped by the implicit deny at the end of the ACL.",
                "correct": False,
                "rationale": (
                    "Incorrect. The packet would be dropped, but not because of the implicit deny — "
                    "it is explicitly denied by ACE 20 before reaching the implicit deny at the end."
                ),
            },
            {
                "id": "d",
                "text": "It is permitted by ACE 10 because the destination IP matches 192.168.1.0/24.",
                "correct": False,
                "rationale": (
                    "Incorrect. ACE 10 also requires TCP destination port 443. The packet is destined for port 80, "
                    "so it does not match ACE 10."
                ),
            },
        ],
        "explanation": (
            "Extended ACLs are processed sequentially. ACE 10 requires TCP port 443 and does not match port 80. "
            "ACE 20 explicitly denies TCP port 80 to the 192.168.1.0/24 subnet, so the packet is dropped here. "
            "ACE 30 is never reached. Extended ACLs filter on source IP, destination IP, protocol, and port, "
            "and should be placed as close to the source as possible to conserve bandwidth."
        ),
    },
    {
        "id": "cd5-003",
        "domain": 5,
        "objective": "5.6",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "ACL placement & wildcard masks",
        "stem": (
            "A network engineer must restrict access so that only Host A (172.16.5.10) can telnet to Router R2. "
            "All other traffic must flow normally. The engineer creates a standard ACL. "
            "According to Cisco best practice, where should this ACL be applied?"
        ),
        "options": [
            {
                "id": "a",
                "text": "On the vty lines of R2 using 'access-class' in the inbound direction.",
                "correct": True,
                "rationale": (
                    "Correct. For controlling management access (Telnet/SSH) to the router itself, "
                    "the ACL is applied to the vty lines with 'access-class <acl> in'. "
                    "This restricts which source addresses can open a VTY session to the router."
                ),
            },
            {
                "id": "b",
                "text": "On the inbound interface of R2 facing Host A, using 'ip access-group' inbound.",
                "correct": False,
                "rationale": (
                    "Incorrect. While an interface ACL would limit source traffic, it would also block "
                    "all other traffic from that interface, not just Telnet. The correct mechanism for "
                    "restricting VTY access is 'access-class' on the VTY lines."
                ),
            },
            {
                "id": "c",
                "text": "On the outbound interface of the router closest to Host A, using 'ip access-group' outbound.",
                "correct": False,
                "rationale": (
                    "Incorrect. Standard ACLs applied outbound on an interface filter traffic leaving that interface "
                    "toward a destination network — they do not specifically restrict Telnet access to the router itself."
                ),
            },
            {
                "id": "d",
                "text": "On the inbound interface of R2 facing the core, using an extended ACL filtering TCP port 23.",
                "correct": False,
                "rationale": (
                    "Incorrect. Although an extended ACL could technically block Telnet traffic, best practice for "
                    "controlling VTY access is 'access-class' on the VTY lines. Using an interface ACL for this purpose "
                    "is cumbersome and could inadvertently block transit traffic."
                ),
            },
        ],
        "explanation": (
            "To control which hosts can Telnet or SSH into a router, apply a standard ACL to the VTY lines "
            "using 'line vty 0 4' → 'access-class <number> in'. This only controls who can open a management "
            "session to the router, without affecting routed traffic. An 'ip access-group' on an interface "
            "controls transit traffic, not VTY sessions to the router itself."
        ),
    },
    {
        "id": "cd5-004",
        "domain": 5,
        "objective": "5.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Access control lists (ACLs)",
        "stem": (
            "A network shows the following named ACL configuration:\n\n"
            "ip access-list extended BLOCK_FTP\n"
            " 10 deny tcp 10.0.0.0 0.255.255.255 any eq 21\n"
            " 20 deny tcp 10.0.0.0 0.255.255.255 any eq 20\n"
            " 30 permit ip any any\n\n"
            "interface GigabitEthernet0/1\n"
            " ip access-group BLOCK_FTP in\n\n"
            "Host 10.1.2.3 attempts an FTP control connection (TCP port 21) to 172.16.0.5. "
            "Host 192.168.1.1 attempts FTP to the same server. Which statement is correct?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The FTP from 10.1.2.3 is denied; the FTP from 192.168.1.1 is permitted.",
                "correct": True,
                "rationale": (
                    "Correct. ACE 10 denies TCP port 21 from any source in 10.0.0.0/8 (wildcard 0.255.255.255). "
                    "10.1.2.3 falls within that range and is denied. 192.168.1.1 is not in 10.0.0.0/8, "
                    "so it skips ACEs 10 and 20 and is permitted by ACE 30."
                ),
            },
            {
                "id": "b",
                "text": "Both FTP connections are denied by ACE 10.",
                "correct": False,
                "rationale": (
                    "Incorrect. ACE 10 only denies sources within 10.0.0.0/8. "
                    "192.168.1.1 does not fall in that range and is not matched by ACE 10."
                ),
            },
            {
                "id": "c",
                "text": "Both FTP connections are permitted because ACE 30 permits all IP traffic.",
                "correct": False,
                "rationale": (
                    "Incorrect. ACLs are evaluated top-down. 10.1.2.3 matches ACE 10 before reaching ACE 30 "
                    "and is denied. Only traffic that doesn't match earlier ACEs reaches ACE 30."
                ),
            },
            {
                "id": "d",
                "text": "The FTP from 10.1.2.3 is denied by the implicit deny; the FTP from 192.168.1.1 is permitted.",
                "correct": False,
                "rationale": (
                    "Incorrect. 10.1.2.3 is denied by the explicit ACE 10 (not the implicit deny at the end). "
                    "The implicit deny is only reached if no other ACE matches."
                ),
            },
        ],
        "explanation": (
            "Named extended ACLs function identically to numbered extended ACLs. Wildcard 0.255.255.255 "
            "in the second and third octets means those octets can be anything — so 10.x.x.x/8 is the "
            "matched range. 10.1.2.3 matches ACE 10 (denied). 192.168.1.1 does not match ACEs 10 or 20 "
            "and is permitted by ACE 30. Always remember the implicit 'deny ip any any' at the end of every ACL."
        ),
    },
    {
        "id": "cd5-005",
        "domain": 5,
        "objective": "5.6",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Access control lists (ACLs)",
        "stem": (
            "An engineer applies the following ACL outbound on interface Gi0/0:\n\n"
            "access-list 1 permit 10.1.1.0 0.0.0.255\n\n"
            "Which traffic is affected by the implicit deny at the end of this ACL?"
        ),
        "options": [
            {
                "id": "a",
                "text": "All traffic not sourced from 10.1.1.0/24 that attempts to leave Gi0/0.",
                "correct": True,
                "rationale": (
                    "Correct. Only traffic matching the explicit permit (source 10.1.1.0/24) is allowed out Gi0/0. "
                    "Every other source IP is denied by the implicit 'deny ip any any' appended to every ACL."
                ),
            },
            {
                "id": "b",
                "text": "All traffic entering Gi0/0 that is not sourced from 10.1.1.0/24.",
                "correct": False,
                "rationale": (
                    "Incorrect. The ACL is applied outbound, so it filters traffic leaving Gi0/0, not entering it."
                ),
            },
            {
                "id": "c",
                "text": "Only traffic destined for 10.1.1.0/24 that leaves Gi0/0.",
                "correct": False,
                "rationale": (
                    "Incorrect. Standard ACLs filter on source address only, not destination. "
                    "The implicit deny blocks traffic based on source IP, not destination IP."
                ),
            },
            {
                "id": "d",
                "text": "No traffic is affected because the implicit deny only applies to extended ACLs.",
                "correct": False,
                "rationale": (
                    "Incorrect. The implicit 'deny ip any any' applies to all ACLs — both standard and extended. "
                    "Every ACL on a Cisco router ends with an implicit deny-all."
                ),
            },
        ],
        "explanation": (
            "Every Cisco ACL, standard or extended, ends with an implicit 'deny ip any any'. "
            "When ACL 1 is applied outbound on Gi0/0, only packets whose source address falls in 10.1.1.0/24 "
            "are forwarded. All other source addresses hit the implicit deny and are dropped. "
            "This is why it is best practice to include at least one explicit 'permit' and understand "
            "the effect of the implicit deny when designing ACLs."
        ),
    },
    {
        "id": "cd5-006",
        "domain": 5,
        "objective": "5.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Port security",
        "stem": (
            "A switchport is configured as follows:\n\n"
            "interface FastEthernet0/3\n"
            " switchport mode access\n"
            " switchport access vlan 10\n"
            " switchport port-security maximum 2\n"
            " switchport port-security violation restrict\n"
            " switchport port-security mac-address sticky\n"
            " switchport port-security\n\n"
            "The port has learned one MAC address. A third MAC address appears on the port. "
            "What is the result?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Frames from the third MAC are dropped and a syslog message is generated, but the port remains up.",
                "correct": True,
                "rationale": (
                    "Correct. In 'restrict' violation mode, frames from violating MAC addresses are dropped, "
                    "a syslog/SNMP notification is sent, and the violation counter increments — but the port stays up."
                ),
            },
            {
                "id": "b",
                "text": "The port is placed into err-disabled state and must be manually recovered.",
                "correct": False,
                "rationale": (
                    "Incorrect. Err-disabled state is the behavior of the default 'shutdown' violation mode. "
                    "This port is configured with 'restrict', which does not shut down the port."
                ),
            },
            {
                "id": "c",
                "text": "Frames from the third MAC are dropped silently with no log messages generated.",
                "correct": False,
                "rationale": (
                    "Incorrect. Silent dropping without notification is the behavior of 'protect' mode. "
                    "'Restrict' mode also drops frames but additionally sends a syslog/SNMP alert."
                ),
            },
            {
                "id": "d",
                "text": "The sticky MAC table is cleared and all three MAC addresses must re-learn.",
                "correct": False,
                "rationale": (
                    "Incorrect. Port security does not clear the MAC table upon violation. "
                    "The already-learned sticky MACs remain; the violating frame is dropped per the configured violation mode."
                ),
            },
        ],
        "explanation": (
            "Port security violation modes: 'protect' drops violating frames silently; 'restrict' drops frames "
            "and increments counters/sends syslog; 'shutdown' (default) err-disables the port. "
            "With 'restrict', the port stays up and legitimate traffic from allowed MACs continues to flow. "
            "Sticky learning causes dynamically learned MACs to be written as static entries in the running config."
        ),
    },
    {
        "id": "cd5-007",
        "domain": 5,
        "objective": "5.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Port security",
        "stem": (
            "An engineer configures sticky MAC learning on Fa0/1 with a maximum of 1. "
            "After the device on Fa0/1 sends traffic, the engineer saves the running config. "
            "The switch is then rebooted, and a different device (different MAC) is plugged into Fa0/1. "
            "What happens assuming the default violation mode?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The port is err-disabled because the new MAC does not match the sticky MAC stored in startup-config.",
                "correct": True,
                "rationale": (
                    "Correct. Sticky MACs are saved to running-config (and startup-config after 'write memory'). "
                    "After reboot, the old sticky MAC is reloaded. The new device's MAC violates the maximum-1 limit, "
                    "triggering the default 'shutdown' violation, placing the port in err-disabled state."
                ),
            },
            {
                "id": "b",
                "text": "The port learns the new MAC as a new sticky entry because the old sticky MAC is cleared on reboot.",
                "correct": False,
                "rationale": (
                    "Incorrect. Sticky MACs are preserved across reboots when 'copy running-config startup-config' is issued. "
                    "The saved sticky entry persists after the reboot and the new MAC causes a violation."
                ),
            },
            {
                "id": "c",
                "text": "The port remains up and both MACs are allowed because sticky learning is dynamic.",
                "correct": False,
                "rationale": (
                    "Incorrect. The maximum is 1, so only one MAC address is permitted. "
                    "The presence of a second MAC triggers the configured violation action."
                ),
            },
            {
                "id": "d",
                "text": "The port drops frames from the new MAC silently because protect mode is the default.",
                "correct": False,
                "rationale": (
                    "Incorrect. The default violation mode is 'shutdown', not 'protect'. "
                    "Without explicit configuration of 'restrict' or 'protect', a violation err-disables the port."
                ),
            },
        ],
        "explanation": (
            "Sticky MAC addresses are stored in running-config. When saved with 'write memory' or "
            "'copy running-config startup-config', they survive a reboot. If a different device connects "
            "and its MAC does not match the saved sticky entry, port security treats it as a violation. "
            "The default violation mode is 'shutdown', which err-disables the port. To recover, an administrator "
            "must issue 'shutdown' then 'no shutdown' on the interface (or use 'errdisable recovery')."
        ),
    },
    {
        "id": "cd5-008",
        "domain": 5,
        "objective": "5.7",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Port security",
        "stem": (
            "The output of 'show port-security interface Gi1/0/5' shows:\n\n"
            "Port Security              : Enabled\n"
            "Port Status                : Secure-up\n"
            "Violation Mode             : Shutdown\n"
            "Aging Time                 : 0 mins\n"
            "Maximum MAC Addresses      : 3\n"
            "Total MAC Addresses        : 3\n"
            "Configured MAC Addresses   : 1\n"
            "Sticky MAC Addresses       : 2\n"
            "Last Source Address:Vlan   : 0050.7966.6800:10\n"
            "Security Violation Count   : 0\n\n"
            "A fourth device connects to Gi1/0/5. Which statement BEST describes the outcome?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The port is placed in err-disabled state because the fourth MAC exceeds the maximum of 3.",
                "correct": True,
                "rationale": (
                    "Correct. The port is at its maximum of 3 MAC addresses (1 configured + 2 sticky). "
                    "A fourth MAC triggers the 'shutdown' violation mode, err-disabling the port immediately."
                ),
            },
            {
                "id": "b",
                "text": "The fourth MAC is silently dropped because the port is in Secure-up state.",
                "correct": False,
                "rationale": (
                    "Incorrect. 'Secure-up' means port security is active and no violation has occurred yet. "
                    "With violation mode 'shutdown', a new MAC beyond the maximum will err-disable the port, not just drop frames."
                ),
            },
            {
                "id": "c",
                "text": "The oldest sticky MAC is aged out to make room for the fourth MAC.",
                "correct": False,
                "rationale": (
                    "Incorrect. Aging time is 0 (disabled). Sticky MACs do not age out unless aging is explicitly configured. "
                    "No aging occurs, so the maximum is enforced strictly."
                ),
            },
            {
                "id": "d",
                "text": "The fourth MAC replaces the configured static MAC address because sticky entries take precedence.",
                "correct": False,
                "rationale": (
                    "Incorrect. Static configured MACs are not replaced by sticky entries or new dynamic MACs. "
                    "The maximum limit is absolute; exceeding it triggers the violation action."
                ),
            },
        ],
        "explanation": (
            "The 'show port-security interface' output shows 3/3 MACs used: 1 statically configured, 2 sticky. "
            "With aging disabled, no MAC will be removed to make room. A fourth device will cause a violation, "
            "and the 'shutdown' mode err-disables the port. The Security Violation Count increments, "
            "and the port status changes to Secure-shutdown (err-disabled)."
        ),
    },
    {
        "id": "cd5-009",
        "domain": 5,
        "objective": "5.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "DHCP snooping & DAI",
        "stem": (
            "DHCP snooping is enabled on VLAN 10. Gi0/1 connects to a legitimate DHCP server. "
            "Gi0/2 connects to user workstations. The following commands are issued:\n\n"
            "ip dhcp snooping\n"
            "ip dhcp snooping vlan 10\n"
            "interface Gi0/1\n"
            " ip dhcp snooping trust\n\n"
            "A rogue DHCP server is attached to Gi0/2. What happens when it sends a DHCP OFFER?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The DHCP OFFER from the rogue server is dropped because Gi0/2 is an untrusted port.",
                "correct": True,
                "rationale": (
                    "Correct. DHCP snooping drops DHCP server messages (OFFER, ACK, NAK) received on untrusted ports. "
                    "Only trusted ports (Gi0/1) are allowed to forward such messages. Gi0/2 is untrusted by default."
                ),
            },
            {
                "id": "b",
                "text": "The DHCP OFFER is forwarded normally because DHCP snooping only inspects DISCOVER messages.",
                "correct": False,
                "rationale": (
                    "Incorrect. DHCP snooping inspects all DHCP message types. On untrusted ports, "
                    "it specifically drops server-originated messages: OFFER, ACK, and NAK."
                ),
            },
            {
                "id": "c",
                "text": "The DHCP OFFER is forwarded but logged as a snooping violation.",
                "correct": False,
                "rationale": (
                    "Incorrect. DHCP snooping does not forward and log — it drops the violating frames from untrusted ports. "
                    "Server-originated DHCP messages on untrusted ports are silently discarded."
                ),
            },
            {
                "id": "d",
                "text": "Gi0/2 is placed in err-disabled state when the rogue DHCP OFFER is detected.",
                "correct": False,
                "rationale": (
                    "Incorrect. DHCP snooping does not err-disable a port simply for receiving a rogue DHCP OFFER. "
                    "It drops the frame. The 'ip dhcp snooping limit rate' feature can trigger err-disable if the "
                    "rate threshold is exceeded, but that is not configured here."
                ),
            },
        ],
        "explanation": (
            "DHCP snooping distinguishes trusted (uplinks to real servers/switches) from untrusted ports. "
            "Untrusted ports are typically access ports facing end hosts. Any DHCP server message "
            "(OFFER, ACK, NAK) arriving on an untrusted port is dropped silently. "
            "The snooping binding table records {MAC, IP, VLAN, interface} from DHCP ACKs on trusted ports, "
            "and this table is then used by Dynamic ARP Inspection (DAI) for further protection."
        ),
    },
    {
        "id": "cd5-010",
        "domain": 5,
        "objective": "5.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "DHCP snooping & DAI",
        "stem": (
            "Dynamic ARP Inspection (DAI) is enabled on VLAN 20. "
            "A host with IP 192.168.20.50 and MAC 00:50:79:66:68:00 sends a gratuitous ARP claiming "
            "IP 192.168.20.1 (the default gateway's IP) maps to its own MAC. "
            "The DHCP snooping binding table shows 192.168.20.50 → 00:50:79:66:68:00 on Fa0/5 (untrusted). "
            "What does DAI do with this ARP packet?"
        ),
        "options": [
            {
                "id": "a",
                "text": "DAI drops the ARP because the IP-to-MAC mapping in the packet (192.168.20.1 → 00:50:79:66:68:00) does not match the DHCP snooping binding for that MAC.",
                "correct": True,
                "rationale": (
                    "Correct. DAI validates ARP packets on untrusted ports by checking the sender IP and MAC "
                    "against the DHCP snooping binding table. The binding table shows this MAC is bound to 192.168.20.50, "
                    "not 192.168.20.1. The mismatch causes DAI to drop the ARP as a spoofing attempt."
                ),
            },
            {
                "id": "b",
                "text": "DAI forwards the ARP because the source MAC is in the DHCP snooping binding table.",
                "correct": False,
                "rationale": (
                    "Incorrect. DAI does not simply verify that the MAC exists in the binding table — it verifies that "
                    "the sender IP in the ARP matches the IP bound to that MAC. A mismatch causes the ARP to be dropped."
                ),
            },
            {
                "id": "c",
                "text": "DAI forwards the ARP because gratuitous ARPs are always permitted.",
                "correct": False,
                "rationale": (
                    "Incorrect. Gratuitous ARPs receive no special treatment from DAI. They are subject to the same "
                    "IP-to-MAC binding validation as any other ARP packet received on untrusted ports."
                ),
            },
            {
                "id": "d",
                "text": "DAI places the port Fa0/5 in err-disabled state and drops all traffic.",
                "correct": False,
                "rationale": (
                    "Incorrect. By default, a single DAI violation drops the offending ARP packet but does not "
                    "err-disable the port. Port err-disable for DAI occurs only when the ARP rate limit is exceeded "
                    "(configured with 'ip arp inspection limit rate')."
                ),
            },
        ],
        "explanation": (
            "Dynamic ARP Inspection (DAI) protects against ARP spoofing/poisoning by validating ARP packets "
            "on untrusted ports against the DHCP snooping binding table. Both the sender IP and sender MAC "
            "in the ARP must match an entry in the binding table. If they do not match, the ARP is dropped. "
            "Trusted ports (typically uplinks) bypass DAI inspection. Static ARP ACLs can be used for "
            "devices with static IPs that don't appear in the DHCP binding table."
        ),
    },
    {
        "id": "cd5-011",
        "domain": 5,
        "objective": "5.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "AAA (RADIUS vs TACACS+)",
        "stem": (
            "A network administrator is choosing between RADIUS and TACACS+ for AAA. "
            "The primary requirement is granular command-level authorization for network engineers "
            "who log in to manage routers and switches. Which protocol is the better choice and why?"
        ),
        "options": [
            {
                "id": "a",
                "text": "TACACS+ because it separates authentication, authorization, and accounting into distinct processes and fully encrypts the packet payload, enabling per-command authorization.",
                "correct": True,
                "rationale": (
                    "Correct. TACACS+ (TCP port 49) separates AAA into three separate control exchanges and encrypts "
                    "the entire packet body. This architecture supports granular per-command authorization, "
                    "making it the preferred choice for device administration."
                ),
            },
            {
                "id": "b",
                "text": "RADIUS because it encrypts the entire packet payload and supports per-command authorization natively.",
                "correct": False,
                "rationale": (
                    "Incorrect. RADIUS (UDP ports 1812/1813) only encrypts the password field, not the entire payload. "
                    "RADIUS does not natively support per-command authorization; it is primarily designed for network access."
                ),
            },
            {
                "id": "c",
                "text": "RADIUS because it uses TCP and provides more reliable delivery for authorization requests.",
                "correct": False,
                "rationale": (
                    "Incorrect. RADIUS uses UDP (ports 1812 for authentication/authorization, 1813 for accounting). "
                    "It is TACACS+ that uses TCP port 49 for reliable transport."
                ),
            },
            {
                "id": "d",
                "text": "TACACS+ because it combines authentication and authorization into one exchange for faster processing.",
                "correct": False,
                "rationale": (
                    "Incorrect. TACACS+ separates authentication, authorization, and accounting — it does not combine them. "
                    "Separation is actually a key advantage of TACACS+ for flexibility and granular control."
                ),
            },
        ],
        "explanation": (
            "RADIUS vs TACACS+ comparison: RADIUS uses UDP (1812/1813), encrypts only the password, combines "
            "authentication and authorization, and is preferred for network access control (802.1X, VPN). "
            "TACACS+ uses TCP 49, encrypts the full packet, separates AAA into distinct exchanges, and supports "
            "per-command authorization — making it the standard for device administration in Cisco environments. "
            "Both support multi-vendor deployments but TACACS+ is Cisco-proprietary by origin."
        ),
    },
    {
        "id": "cd5-012",
        "domain": 5,
        "objective": "5.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "AAA (RADIUS vs TACACS+)",
        "stem": (
            "A company deploys 802.1X wired authentication for all employee workstations. "
            "The security team wants to use a single AAA server for both wired 802.1X access "
            "and VPN remote access authentication. Which AAA protocol is most appropriate, and why?"
        ),
        "options": [
            {
                "id": "a",
                "text": "RADIUS, because it is the standard protocol for network access control (802.1X and VPN), supported natively by most NAS devices and IEEE 802.1X implementations.",
                "correct": True,
                "rationale": (
                    "Correct. RADIUS is the industry standard for network access services (NAS), "
                    "including 802.1X (EAP over RADIUS) and VPN authentication. It is supported by all major vendors "
                    "and is the protocol required by IEEE 802.1X."
                ),
            },
            {
                "id": "b",
                "text": "TACACS+, because it encrypts the full packet and is therefore more secure for 802.1X.",
                "correct": False,
                "rationale": (
                    "Incorrect. While TACACS+ encrypts more of the packet, it is not the standard for 802.1X. "
                    "IEEE 802.1X specifically uses EAP carried over RADIUS. TACACS+ is designed for device administration, "
                    "not network access control."
                ),
            },
            {
                "id": "c",
                "text": "TACACS+, because it uses TCP which provides more reliable authentication for VPN connections.",
                "correct": False,
                "rationale": (
                    "Incorrect. While TACACS+ does use TCP, it is not the appropriate protocol for 802.1X or VPN "
                    "network access. RADIUS is the standard for these use cases regardless of transport differences."
                ),
            },
            {
                "id": "d",
                "text": "RADIUS, because it separates authentication and authorization, allowing independent policy control.",
                "correct": False,
                "rationale": (
                    "Incorrect. RADIUS actually combines authentication and authorization in the same packet exchange. "
                    "It is TACACS+ that separates them. However, RADIUS is still the correct choice here for 802.1X/VPN."
                ),
            },
        ],
        "explanation": (
            "RADIUS is the mandated protocol for 802.1X authentication (EAP is encapsulated in RADIUS). "
            "VPN gateways and wireless controllers also commonly use RADIUS for access authentication. "
            "TACACS+ is optimized for device (CLI) management with per-command authorization. "
            "When a single server must handle both 802.1X and VPN, RADIUS is the correct choice."
        ),
    },
    {
        "id": "cd5-013",
        "domain": 5,
        "objective": "5.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Device access control (passwords)",
        "stem": (
            "A router has the following configuration:\n\n"
            "enable password C1sc0\n"
            "enable secret Str0ng$ecret\n"
            "service password-encryption\n\n"
            "A user enters 'C1sc0' at the enable prompt. What happens?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Access is denied. The enable secret takes precedence over enable password when both are configured; only 'Str0ng$ecret' grants privileged access.",
                "correct": True,
                "rationale": (
                    "Correct. When both 'enable password' and 'enable secret' are configured, "
                    "the enable secret always takes precedence. The enable password is effectively ignored."
                ),
            },
            {
                "id": "b",
                "text": "Access is granted because 'service password-encryption' uses Type 7 encryption, which the router decrypts to validate 'C1sc0'.",
                "correct": False,
                "rationale": (
                    "Incorrect. 'Service password-encryption' applies Type 7 (weak, reversible) encryption to 'enable password', "
                    "but this does not change the precedence rule. Enable secret still takes precedence."
                ),
            },
            {
                "id": "c",
                "text": "Access is granted because either the enable password or enable secret can be used when both are configured.",
                "correct": False,
                "rationale": (
                    "Incorrect. Cisco IOS does not accept both passwords when both are configured. "
                    "The enable secret always overrides the enable password."
                ),
            },
            {
                "id": "d",
                "text": "The router accepts 'C1sc0' because service password-encryption creates a hash of both passwords and they collide.",
                "correct": False,
                "rationale": (
                    "Incorrect. 'Service password-encryption' uses Type 7 (Vigenere cipher) on enable password, "
                    "not a hash function. There is no collision scenario. Enable secret uses MD5 (Type 5) and takes precedence."
                ),
            },
        ],
        "explanation": (
            "When both 'enable password' and 'enable secret' are present, Cisco IOS uses only the enable secret. "
            "Enable secret uses MD5 (Type 5) hashing — far more secure than the Type 7 reversible cipher "
            "applied by 'service password-encryption'. Best practice: use 'enable secret' exclusively "
            "(or 'enable algorithm-type scrypt secret' for Type 9 in newer IOS versions) "
            "and remove 'enable password' entirely."
        ),
    },
    {
        "id": "cd5-014",
        "domain": 5,
        "objective": "5.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Device access control (passwords)",
        "stem": (
            "Which set of commands correctly configures a Cisco router to require local username/password "
            "authentication on all VTY lines, with SSH as the only allowed transport?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "username admin secret P@ssw0rd\n"
                    "line vty 0 4\n"
                    " login local\n"
                    " transport input ssh"
                ),
                "correct": True,
                "rationale": (
                    "Correct. 'username admin secret P@ssw0rd' creates a local user with an MD5-hashed password. "
                    "'login local' instructs the VTY line to use the local user database. "
                    "'transport input ssh' restricts VTY access to SSH only."
                ),
            },
            {
                "id": "b",
                "text": (
                    "username admin password P@ssw0rd\n"
                    "line vty 0 4\n"
                    " login\n"
                    " transport input ssh"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. 'login' (without 'local') uses a line-level password (set with 'password'), "
                    "not the local user database. 'username admin password' also uses weaker Type 7 storage "
                    "instead of MD5 ('secret')."
                ),
            },
            {
                "id": "c",
                "text": (
                    "username admin secret P@ssw0rd\n"
                    "line vty 0 4\n"
                    " login local\n"
                    " transport input telnet ssh"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. 'transport input telnet ssh' allows both Telnet and SSH. "
                    "The requirement is SSH only, so 'transport input ssh' must be used."
                ),
            },
            {
                "id": "d",
                "text": (
                    "username admin secret P@ssw0rd\n"
                    "line vty 0 4\n"
                    " login local\n"
                    " transport output ssh"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. 'transport output ssh' controls what protocols the router uses when initiating "
                    "outbound connections from the VTY line (e.g., SSH to another device). "
                    "To restrict incoming VTY sessions to SSH, use 'transport input ssh'."
                ),
            },
        ],
        "explanation": (
            "To require local database authentication on VTY lines: create user accounts with 'username <name> secret <pw>', "
            "then under 'line vty 0 4' use 'login local' (not just 'login') and 'transport input ssh'. "
            "'login local' checks the local username database; 'login' alone requires only the line password. "
            "Also required for SSH: 'ip domain-name', 'crypto key generate rsa', and 'ip ssh version 2'."
        ),
    },
    {
        "id": "cd5-015",
        "domain": 5,
        "objective": "5.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Device access control (passwords)",
        "stem": (
            "After issuing 'service password-encryption' on a router, an administrator views the running config and sees:\n\n"
            "username analyst password 7 0822455D0A16\n\n"
            "Which statement about this password is accurate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The Type 7 hash is a weak, reversible Vigenere cipher and can be decoded by freely available tools; 'username analyst secret' should be used instead.",
                "correct": True,
                "rationale": (
                    "Correct. Type 7 encryption (Vigenere cipher) is easily reversed by online tools and is not "
                    "considered cryptographically secure. Using 'username <name> secret <pw>' stores an MD5 (Type 5) hash, "
                    "which is significantly harder to crack."
                ),
            },
            {
                "id": "b",
                "text": "The Type 7 encoding is an irreversible SHA-256 hash that provides strong security.",
                "correct": False,
                "rationale": (
                    "Incorrect. Type 7 is not SHA-256 and is not irreversible. It is a simple Vigenere-based obfuscation "
                    "scheme that can be decoded easily. SHA-256 is used in Type 8/9 password storage."
                ),
            },
            {
                "id": "c",
                "text": "Service password-encryption applies MD5 hashing, equivalent to 'enable secret', providing strong protection.",
                "correct": False,
                "rationale": (
                    "Incorrect. Service password-encryption applies Type 7 (not MD5). MD5 hashing is used by 'enable secret' "
                    "and 'username <name> secret', which store Type 5 passwords."
                ),
            },
            {
                "id": "d",
                "text": "The password cannot be read from the running config because 'service password-encryption' hides it completely.",
                "correct": False,
                "rationale": (
                    "Incorrect. 'Service password-encryption' only obscures the password in the config; it does not "
                    "prevent it from being decoded. The Type 7 string can be trivially reversed."
                ),
            },
        ],
        "explanation": (
            "Type 7 passwords in Cisco IOS use a simple Vigenere cipher with a known key — they are trivially reversible "
            "using publicly available tools. 'Service password-encryption' protects against casual shoulder-surfing "
            "but not against anyone with access to the config file. For user account passwords, "
            "always use 'username <name> secret <pw>' (Type 5 MD5) or 'username <name> algorithm-type scrypt secret' "
            "(Type 9) for stronger protection."
        ),
    },
    {
        "id": "cd5-016",
        "domain": 5,
        "objective": "5.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Wireless security (WPA2/WPA3)",
        "stem": (
            "A company deploys WPA3-Personal on its guest wireless network. "
            "Which key exchange mechanism makes WPA3-Personal more resistant to offline dictionary attacks "
            "compared to WPA2-Personal?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Simultaneous Authentication of Equals (SAE), which replaces the Pre-Shared Key (PSK) handshake and provides forward secrecy.",
                "correct": True,
                "rationale": (
                    "Correct. WPA3-Personal replaces the PSK 4-way handshake with SAE (also called Dragonfly). "
                    "SAE is a zero-knowledge proof method that prevents offline dictionary attacks even if an attacker "
                    "captures the handshake, and it provides forward secrecy."
                ),
            },
            {
                "id": "b",
                "text": "AES-CCMP 256-bit encryption, which replaces TKIP and makes brute-force infeasible.",
                "correct": False,
                "rationale": (
                    "Incorrect. While WPA3 uses stronger encryption (AES-GCMP-256 in WPA3-Enterprise), "
                    "the protection against offline dictionary attacks specifically comes from the SAE key exchange, "
                    "not from the cipher suite itself."
                ),
            },
            {
                "id": "c",
                "text": "Protected Management Frames (PMF), which encrypts probe and beacon frames.",
                "correct": False,
                "rationale": (
                    "Incorrect. PMF (802.11w) is mandatory in WPA3 and protects management frames from spoofing/eavesdropping. "
                    "However, protection from offline dictionary attacks is specifically provided by the SAE key exchange."
                ),
            },
            {
                "id": "d",
                "text": "TKIP with a 256-bit key, which prevents key reinstallation attacks.",
                "correct": False,
                "rationale": (
                    "Incorrect. TKIP is deprecated and is not used in WPA3. WPA3 uses AES-based encryption. "
                    "Key reinstallation attacks (KRACK) target the 4-way handshake, which SAE replaces in WPA3-Personal."
                ),
            },
        ],
        "explanation": (
            "WPA3-Personal introduces Simultaneous Authentication of Equals (SAE) to replace WPA2's PSK handshake. "
            "SAE uses a Diffie-Hellman-based protocol where neither party reveals their password; instead they prove "
            "knowledge of it. This prevents offline dictionary attacks against captured handshakes and provides "
            "perfect forward secrecy. WPA3 also mandates PMF (802.11w) and does not support TKIP."
        ),
    },
    {
        "id": "cd5-017",
        "domain": 5,
        "objective": "5.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Wireless security (WPA2/WPA3)",
        "stem": (
            "A wireless network uses WPA2-Enterprise. Which authentication framework is used, "
            "and how does it differ from WPA2-PSK?"
        ),
        "options": [
            {
                "id": "a",
                "text": "WPA2-Enterprise uses 802.1X/EAP with an external RADIUS server for per-user authentication, whereas WPA2-PSK uses a single shared key for all users.",
                "correct": True,
                "rationale": (
                    "Correct. WPA2-Enterprise (802.1X mode) uses EAP carried over RADIUS for per-user credential-based "
                    "authentication. WPA2-PSK uses a single pre-shared key distributed to all users."
                ),
            },
            {
                "id": "b",
                "text": "WPA2-Enterprise uses TKIP encryption and WPA2-PSK uses AES-CCMP, making Enterprise less secure.",
                "correct": False,
                "rationale": (
                    "Incorrect. Both WPA2-Enterprise and WPA2-PSK use AES-CCMP for data encryption. "
                    "The difference is in the authentication mechanism, not the cipher suite."
                ),
            },
            {
                "id": "c",
                "text": "WPA2-Enterprise uses SAE (Dragonfly) for key exchange, providing forward secrecy not available in PSK.",
                "correct": False,
                "rationale": (
                    "Incorrect. SAE is the authentication method for WPA3-Personal, not WPA2-Enterprise. "
                    "WPA2-Enterprise uses the 802.1X/EAP framework."
                ),
            },
            {
                "id": "d",
                "text": "WPA2-Enterprise requires a certificate on the access point only; clients authenticate with username/password using TKIP.",
                "correct": False,
                "rationale": (
                    "Incorrect. WPA2-Enterprise uses AES-CCMP, not TKIP. Authentication can use various EAP methods "
                    "(EAP-TLS requires certificates on both sides; PEAP/EAP-TTLS use server certificates + client credentials). "
                    "It is not limited to AP-only certificates."
                ),
            },
        ],
        "explanation": (
            "WPA2-Enterprise uses IEEE 802.1X with Extensible Authentication Protocol (EAP) for authentication. "
            "A RADIUS server validates user credentials (or certificates). This enables per-user authentication, "
            "centralized policy enforcement, and individual session keys, unlike PSK where all users share one key. "
            "Common EAP types: EAP-TLS (certificates both sides), PEAP (server cert + MS-CHAPv2 password), "
            "EAP-TTLS. Both Enterprise and PSK modes use AES-CCMP for encryption in WPA2."
        ),
    },
    {
        "id": "cd5-018",
        "domain": 5,
        "objective": "5.10",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Wireless security (WPA2/WPA3)",
        "stem": (
            "An administrator is configuring a WLAN in Cisco WLC GUI using WPA2 PSK. "
            "Under the Security tab for the WLAN, the engineer selects WPA2 Policy with AES encryption. "
            "Which authentication key management (AKM) setting must be selected to enable PSK-based authentication?"
        ),
        "options": [
            {
                "id": "a",
                "text": "PSK under the Auth Key Mgmt section, which configures a pre-shared passphrase used to derive the Pairwise Master Key (PMK).",
                "correct": True,
                "rationale": (
                    "Correct. In the WLC GUI, selecting 'PSK' under Auth Key Mgmt configures the WLAN to use a "
                    "pre-shared key. The PSK is used with the SSID via PBKDF2 to derive the PMK, which seeds the "
                    "4-way handshake for per-session encryption keys."
                ),
            },
            {
                "id": "b",
                "text": "802.1X under the Auth Key Mgmt section, which enables local EAP authentication on the WLC.",
                "correct": False,
                "rationale": (
                    "Incorrect. Selecting 802.1X configures enterprise authentication using a RADIUS server, not PSK. "
                    "PSK mode requires the 'PSK' AKM option."
                ),
            },
            {
                "id": "c",
                "text": "CCKM (Cisco Centralized Key Management) under Auth Key Mgmt, which supports fast roaming with a shared key.",
                "correct": False,
                "rationale": (
                    "Incorrect. CCKM is a Cisco-proprietary fast roaming feature for 802.1X environments. "
                    "It is not used for PSK-based authentication."
                ),
            },
            {
                "id": "d",
                "text": "FT (Fast Transition) under Auth Key Mgmt, which enables 802.11r PSK fast BSS transition.",
                "correct": False,
                "rationale": (
                    "Incorrect. FT (802.11r) is a fast roaming mechanism. While FT-PSK is an option, "
                    "the basic WPA2-PSK configuration simply requires selecting 'PSK' as the AKM. "
                    "FT is an optional extension for roaming optimization."
                ),
            },
        ],
        "explanation": (
            "In Cisco WLC GUI, to configure WPA2 PSK: navigate to WLANs → select WLAN → Security → Layer 2 tab, "
            "set Layer 2 Security to 'WPA+WPA2', check WPA2 Policy, select AES cipher, and under Auth Key Mgmt "
            "check 'PSK' and enter the passphrase. The PMK is derived from PSK + SSID using PBKDF2 (4096 iterations). "
            "The 4-way handshake then derives PTK (pairwise transient key) for per-session unicast encryption."
        ),
    },
    {
        "id": "cd5-019",
        "domain": 5,
        "objective": "5.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "IPsec VPNs",
        "stem": (
            "Which statement correctly describes the difference between a site-to-site IPsec VPN "
            "and a remote access IPsec VPN in terms of tunnel establishment and endpoint types?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A site-to-site VPN connects two network gateways (routers/firewalls) with a permanent tunnel, while a remote access VPN connects individual client devices dynamically to a VPN concentrator.",
                "correct": True,
                "rationale": (
                    "Correct. Site-to-site IPsec VPNs are established between two fixed gateways (e.g., router-to-router) "
                    "and are typically always-on, connecting entire networks. Remote access VPNs are initiated by client "
                    "software on individual devices connecting to a VPN concentrator or firewall."
                ),
            },
            {
                "id": "b",
                "text": "Site-to-site VPNs use SSL/TLS for tunneling and remote access VPNs use IPsec IKEv2.",
                "correct": False,
                "rationale": (
                    "Incorrect. This is backwards. SSL VPN (e.g., Cisco AnyConnect TLS mode) is a common remote access "
                    "technology. Site-to-site VPNs typically use IPsec. However, both technologies can technically "
                    "use IPsec — the question is about the distinction between the two types."
                ),
            },
            {
                "id": "c",
                "text": "Remote access VPNs require a static public IP on the client, while site-to-site VPNs support dynamic IPs on one end.",
                "correct": False,
                "rationale": (
                    "Incorrect. Remote access VPN clients do not need static public IPs — they connect from dynamic "
                    "addresses. Site-to-site VPNs can use Dynamic DNS or IKEv2 features to handle dynamic IPs on one side."
                ),
            },
            {
                "id": "d",
                "text": "Site-to-site VPNs provide user authentication per session, while remote access VPNs authenticate only the gateway.",
                "correct": False,
                "rationale": (
                    "Incorrect. Remote access VPNs require per-user authentication (username/password, certificates, MFA). "
                    "Site-to-site VPNs authenticate the gateways using pre-shared keys or digital certificates, "
                    "not individual users."
                ),
            },
        ],
        "explanation": (
            "Site-to-site IPsec VPNs tunnel traffic between two network perimeter devices (routers, ASA/FTD firewalls), "
            "typically using IKEv1 or IKEv2 in main mode, connecting entire subnets transparently. "
            "Remote access VPNs use client software (Cisco AnyConnect, IPsec VPN client) on individual endpoints "
            "that connect on demand. IKEv2 with EAP is common for remote access with per-user authentication. "
            "Both use AH or ESP for packet-level protection; ESP with AES-256 and SHA-2 is the modern best practice."
        ),
    },
    {
        "id": "cd5-020",
        "domain": 5,
        "objective": "5.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "IPsec VPNs",
        "stem": (
            "In an IPsec site-to-site VPN, IKE Phase 1 establishes the ISAKMP SA. "
            "Which IPsec component is responsible for providing data confidentiality, "
            "data integrity, and anti-replay protection in the data plane (IKE Phase 2)?"
        ),
        "options": [
            {
                "id": "a",
                "text": "ESP (Encapsulating Security Payload) in tunnel mode, which encrypts and authenticates the inner IP packet.",
                "correct": True,
                "rationale": (
                    "Correct. ESP (protocol 50) provides confidentiality (encryption), integrity (HMAC), authentication, "
                    "and anti-replay protection. In tunnel mode (used for site-to-site VPNs), "
                    "it encapsulates the entire original IP packet with a new outer IP header."
                ),
            },
            {
                "id": "b",
                "text": "AH (Authentication Header) in tunnel mode, which encrypts the payload and provides integrity.",
                "correct": False,
                "rationale": (
                    "Incorrect. AH (protocol 51) provides integrity and authentication but does NOT provide encryption "
                    "(confidentiality). AH is also incompatible with NAT because it includes the outer IP header in its hash."
                ),
            },
            {
                "id": "c",
                "text": "IKEv2 in aggressive mode, which combines authentication and encryption in a single exchange.",
                "correct": False,
                "rationale": (
                    "Incorrect. IKEv2 (and IKEv1 aggressive mode) are Phase 1 mechanisms for establishing the control-plane SA. "
                    "Data plane encryption is handled by ESP in Phase 2 (IPsec SA)."
                ),
            },
            {
                "id": "d",
                "text": "GRE (Generic Routing Encapsulation), which tunnels multicast and routing protocol traffic with encryption.",
                "correct": False,
                "rationale": (
                    "Incorrect. GRE provides tunneling and supports multicast/routing protocols but does not natively "
                    "provide encryption, integrity, or authentication. GRE is often combined with IPsec (GRE over IPsec) "
                    "to add these security properties."
                ),
            },
        ],
        "explanation": (
            "IPsec uses two security protocols: AH (protocol 51) provides integrity and authentication only — no encryption. "
            "ESP (protocol 50) provides confidentiality, integrity, authentication, and anti-replay protection. "
            "For a VPN requiring confidentiality (data secrecy), ESP is required. "
            "In tunnel mode (site-to-site), the entire original packet is encapsulated; in transport mode (host-to-host), "
            "only the payload is protected. Modern IPsec VPNs use AES-256 for encryption and SHA-256/SHA-384 for HMAC."
        ),
    },
    {
        "id": "cd5-021",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security concepts (threats/vulnerabilities)",
        "stem": (
            "An attacker sends millions of SYN packets to a server without completing the TCP three-way handshake, "
            "exhausting the server's connection table and preventing legitimate connections. "
            "Which threat category and recommended mitigation BEST describe this scenario?"
        ),
        "options": [
            {
                "id": "a",
                "text": "SYN flood (DoS); mitigated using TCP SYN cookies, which allow the server to handle connections without allocating resources until the handshake completes.",
                "correct": True,
                "rationale": (
                    "Correct. A SYN flood is a Denial-of-Service (DoS) attack that exploits TCP's half-open connection state. "
                    "TCP SYN cookies encode connection state in the sequence number, allowing the server to defer "
                    "resource allocation until a valid ACK is received."
                ),
            },
            {
                "id": "b",
                "text": "Smurf attack (DDoS); mitigated by disabling IP-directed broadcasts on all routers.",
                "correct": False,
                "rationale": (
                    "Incorrect. A Smurf attack uses ICMP echo requests sent to a broadcast address with a spoofed victim "
                    "source IP. The scenario describes a SYN flood, not a Smurf attack."
                ),
            },
            {
                "id": "c",
                "text": "Session hijacking (Man-in-the-Middle); mitigated using TLS mutual authentication.",
                "correct": False,
                "rationale": (
                    "Incorrect. Session hijacking involves taking over an existing session, typically by stealing a session "
                    "token. The scenario describes resource exhaustion through incomplete TCP handshakes — a SYN flood."
                ),
            },
            {
                "id": "d",
                "text": "ARP poisoning; mitigated by enabling Dynamic ARP Inspection on the switch.",
                "correct": False,
                "rationale": (
                    "Incorrect. ARP poisoning involves sending fake ARP replies to poison ARP caches. "
                    "The scenario describes a TCP SYN flood attack."
                ),
            },
        ],
        "explanation": (
            "A SYN flood is a classic volumetric DoS attack exploiting TCP's 3-way handshake. "
            "The server allocates resources for each SYN (half-open connection), which the attacker never completes. "
            "Mitigations include: TCP SYN cookies (RFC 4987), firewall rate limiting, network-level filtering, "
            "and IPS/IDS rules. SYN flooding with spoofed source IPs from multiple hosts becomes a DDoS. "
            "Related: ICMP flood, UDP flood, and HTTP flood are other volumetric DoS variants."
        ),
    },
    {
        "id": "cd5-022",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security concepts (threats/vulnerabilities)",
        "stem": (
            "An attacker successfully exploits an unpatched buffer overflow in a web application, "
            "gains root access, and installs a persistent backdoor. "
            "Which terms BEST describe the attack chain components: the unpatched software flaw, "
            "the buffer overflow code used, and the root access gained?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Vulnerability (unpatched flaw), exploit (buffer overflow code), and threat (root access gained).",
                "correct": False,
                "rationale": (
                    "Incorrect. Root access gained is not a 'threat' — it is the impact or the result of a successful "
                    "exploit. A threat is an entity or event that could cause harm; root access is the realized consequence."
                ),
            },
            {
                "id": "b",
                "text": "Vulnerability (unpatched flaw), exploit (buffer overflow code), and impact/compromise (root access gained).",
                "correct": True,
                "rationale": (
                    "Correct. Vulnerability = the weakness (unpatched buffer overflow flaw). "
                    "Exploit = the code/technique used to leverage the vulnerability (buffer overflow payload). "
                    "Impact/compromise = the outcome (root access, backdoor installation). "
                    "This accurately reflects the CVE/CVSS framework terminology."
                ),
            },
            {
                "id": "c",
                "text": "Threat (unpatched flaw), vulnerability (buffer overflow code), and exploit (root access gained).",
                "correct": False,
                "rationale": (
                    "Incorrect. The unpatched flaw is a vulnerability (a weakness), not a threat. "
                    "The buffer overflow code is the exploit technique. Root access is the result/impact, not an exploit."
                ),
            },
            {
                "id": "d",
                "text": "Risk (unpatched flaw), attack vector (buffer overflow code), and vulnerability (root access gained).",
                "correct": False,
                "rationale": (
                    "Incorrect. Risk is the combination of probability and impact — not simply the unpatched flaw itself. "
                    "The unpatched flaw is a vulnerability. Root access is the impact, not a vulnerability."
                ),
            },
        ],
        "explanation": (
            "Security terminology: Vulnerability = a weakness that can be exploited (unpatched software, misconfiguration). "
            "Exploit = the specific technique, code, or procedure used to take advantage of a vulnerability. "
            "Threat = any potential danger (natural disaster, attacker, malware). "
            "Risk = likelihood × impact. Impact/Compromise = the actual outcome of a successful attack. "
            "Understanding these distinctions is essential for the CCNA Security Fundamentals domain."
        ),
    },
    {
        "id": "cd5-023",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security program elements",
        "stem": (
            "A social engineering attacker calls the help desk, claims to be the CFO, "
            "and demands an immediate password reset for the finance application. "
            "The help desk representative complies without verification. "
            "Which security control would have BEST prevented this breach?"
        ),
        "options": [
            {
                "id": "a",
                "text": "User awareness training that teaches employees to verify caller identity through out-of-band means (e.g., callback to a known number) before resetting credentials.",
                "correct": True,
                "rationale": (
                    "Correct. Pretexting/impersonation is a social engineering technique. User awareness training "
                    "teaches employees to recognize manipulation tactics and to verify requests through independent "
                    "channels before taking security-sensitive actions."
                ),
            },
            {
                "id": "b",
                "text": "Deploying an IDS/IPS to detect the social engineering phone call.",
                "correct": False,
                "rationale": (
                    "Incorrect. IDS/IPS monitors network traffic for attack signatures. They cannot detect telephone-based "
                    "social engineering attacks that exploit human behavior."
                ),
            },
            {
                "id": "c",
                "text": "Configuring stronger passwords with complexity requirements to prevent brute-force attacks.",
                "correct": False,
                "rationale": (
                    "Incorrect. Password complexity protects against password-guessing attacks. "
                    "In this scenario, the attacker didn't guess a password — they convinced a human to reset it. "
                    "The vulnerability is procedural and human, not technical."
                ),
            },
            {
                "id": "d",
                "text": "Enabling port security to restrict MAC addresses on the finance server's switch port.",
                "correct": False,
                "rationale": (
                    "Incorrect. Port security is a Layer 2 switch control. It is irrelevant to a phone-based "
                    "social engineering attack targeting the help desk procedure."
                ),
            },
        ],
        "explanation": (
            "Social engineering exploits human psychology rather than technical vulnerabilities. "
            "Pretexting (creating a false identity) and impersonation are common tactics. "
            "The primary defense is user awareness training combined with strict identity verification procedures "
            "(callback procedures, identity codes, ticketing system escalation). "
            "Physical security, technical controls, and policies are all important, "
            "but training is the most direct defense against human-targeted attacks."
        ),
    },
    {
        "id": "cd5-024",
        "domain": 5,
        "objective": "5.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Password policies & MFA",
        "stem": (
            "A company's security policy requires multi-factor authentication (MFA) for all remote access. "
            "An employee uses a password and receives a one-time code via SMS. "
            "Which authentication factors are being combined?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Something you know (password) and something you have (mobile phone receiving SMS OTP).",
                "correct": True,
                "rationale": (
                    "Correct. The password is 'something you know'. The mobile phone (possession of the physical device) "
                    "that receives the SMS OTP represents 'something you have'. Combining two different factor types "
                    "satisfies MFA requirements."
                ),
            },
            {
                "id": "b",
                "text": "Something you know (password) and something you are (SMS code).",
                "correct": False,
                "rationale": (
                    "Incorrect. 'Something you are' refers to biometrics (fingerprint, retina, voice). "
                    "An SMS code is 'something you have' (possession of the mobile device), not a biometric."
                ),
            },
            {
                "id": "c",
                "text": "Something you have (password) and something you know (SMS code).",
                "correct": False,
                "rationale": (
                    "Incorrect. The factors are swapped. A password is 'something you know' (memorized information). "
                    "The SMS code delivered to a physical device is 'something you have' (possession)."
                ),
            },
            {
                "id": "d",
                "text": "Two instances of 'something you know' because both are digital values the user must enter.",
                "correct": False,
                "rationale": (
                    "Incorrect. Using two passwords (even dynamically generated ones) would be two-step verification "
                    "using the same factor type — not true MFA. MFA requires factors from different categories. "
                    "An SMS OTP is 'something you have' because it is tied to physical device possession."
                ),
            },
        ],
        "explanation": (
            "The three MFA factor categories: (1) Something you know: passwords, PINs, security questions. "
            "(2) Something you have: hardware tokens, smart cards, mobile phones (SMS/TOTP apps), certificates. "
            "(3) Something you are: biometrics (fingerprint, facial recognition, iris scan). "
            "True MFA combines factors from at least two DIFFERENT categories. Two passwords = single-factor. "
            "Alternatives to passwords include certificates (something you have) and biometrics (something you are)."
        ),
    },
    {
        "id": "cd5-025",
        "domain": 5,
        "objective": "5.6",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "ACL placement & wildcard masks",
        "stem": (
            "A network has the topology: PC_A (192.168.1.0/24) --- R1 --- R2 --- Server_Farm (10.0.0.0/24). "
            "A standard ACL should deny PC_A's subnet from accessing Server_Farm. "
            "An engineer argues the ACL should go on R1's Gi0/0 interface (inbound, facing PC_A). "
            "Why is this placement suboptimal according to Cisco best practice?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Standard ACLs should be placed close to the destination (Server_Farm); placing it on R1 inbound could inadvertently block PC_A's traffic to other destinations via R1.",
                "correct": True,
                "rationale": (
                    "Correct. Cisco best practice places standard ACLs near the destination because they only filter "
                    "by source IP. If placed on R1 inbound (close to source), all traffic from PC_A — including "
                    "traffic to other networks — could be blocked, not just traffic to Server_Farm."
                ),
            },
            {
                "id": "b",
                "text": "Standard ACLs cannot be applied inbound; they can only be applied outbound on router interfaces.",
                "correct": False,
                "rationale": (
                    "Incorrect. Standard ACLs can be applied both inbound and outbound on router interfaces. "
                    "The issue is not the direction but the proximity to source vs. destination."
                ),
            },
            {
                "id": "c",
                "text": "R1 does not support standard ACLs; only extended ACLs are supported on interfaces facing end hosts.",
                "correct": False,
                "rationale": (
                    "Incorrect. Cisco IOS routers support standard ACLs on any interface in both directions. "
                    "There is no restriction on where standard ACLs can be applied by interface type or position."
                ),
            },
            {
                "id": "d",
                "text": "The ACL should use a subnet mask, not a wildcard mask, when placed near the source.",
                "correct": False,
                "rationale": (
                    "Incorrect. ACLs always use wildcard masks, regardless of placement. "
                    "The placement recommendation is about minimizing unintended traffic blocking, not mask syntax."
                ),
            },
        ],
        "explanation": (
            "Cisco ACL placement rules: Standard ACLs filter source IP only, so placing them close to the SOURCE "
            "risks blocking traffic to unintended destinations. Place standard ACLs CLOSE TO THE DESTINATION. "
            "Extended ACLs can specify both source and destination (and ports), so they can be placed close to "
            "the source without collateral damage. The ideal placement for the standard ACL here would be "
            "outbound on R2's interface facing Server_Farm (or inbound on R2's interface facing the server farm)."
        ),
    },
    {
        "id": "cd5-026",
        "domain": 5,
        "objective": "5.6",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Access control lists (ACLs)",
        "stem": (
            "An engineer needs to match ONLY the host 172.31.255.254 in an ACL entry. "
            "Which wildcard mask should be used?"
        ),
        "options": [
            {
                "id": "a",
                "text": "access-list 10 permit host 172.31.255.254",
                "correct": True,
                "rationale": (
                    "Correct. The keyword 'host' is equivalent to the wildcard mask 0.0.0.0, "
                    "which requires all 32 bits to match exactly. This matches only the single host 172.31.255.254."
                ),
            },
            {
                "id": "b",
                "text": "access-list 10 permit 172.31.255.254 0.0.0.255",
                "correct": False,
                "rationale": (
                    "Incorrect. Wildcard 0.0.0.255 matches any host in the 172.31.255.0–172.31.255.255 range (/24), "
                    "not just 172.31.255.254."
                ),
            },
            {
                "id": "c",
                "text": "access-list 10 permit 172.31.255.254 255.255.255.255",
                "correct": False,
                "rationale": (
                    "Incorrect. In wildcard mask syntax, 255.255.255.255 means ALL bits are 'don't care', "
                    "which would match every IP address (equivalent to 'permit any'). "
                    "To match a single host, the wildcard must be 0.0.0.0."
                ),
            },
            {
                "id": "d",
                "text": "access-list 10 permit 172.31.0.0 0.0.255.255",
                "correct": False,
                "rationale": (
                    "Incorrect. Wildcard 0.0.255.255 matches all addresses in 172.31.0.0–172.31.255.255 (/16), "
                    "which is an entire /16 range — far too broad for a single host match."
                ),
            },
        ],
        "explanation": (
            "To match a single host in an ACL, use either 'host <ip-address>' or '<ip-address> 0.0.0.0'. "
            "The wildcard 0.0.0.0 means every bit must match exactly. Contrast with 'any' (wildcard 255.255.255.255) "
            "which matches all addresses. The 'host' keyword is simply syntactic sugar for the 0.0.0.0 wildcard "
            "and is more readable in configurations."
        ),
    },
    {
        "id": "cd5-027",
        "domain": 5,
        "objective": "5.7",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "DHCP snooping & DAI",
        "stem": (
            "After enabling DHCP snooping on all VLANs, an administrator notices that clients "
            "behind a distribution switch are not receiving DHCP addresses from the core router's DHCP server. "
            "The access switch uplink to the distribution switch is Gi1/1. "
            "Which command resolves the issue?"
        ),
        "options": [
            {
                "id": "a",
                "text": "interface Gi1/1 → ip dhcp snooping trust",
                "correct": True,
                "rationale": (
                    "Correct. The uplink port facing the legitimate DHCP server (through the distribution switch) "
                    "must be marked as trusted. DHCP OFFERs/ACKs from the server are dropped on untrusted ports. "
                    "Marking Gi1/1 as trusted allows legitimate DHCP responses to pass."
                ),
            },
            {
                "id": "b",
                "text": "ip dhcp snooping information option (enable DHCP Option 82 insertion)",
                "correct": False,
                "rationale": (
                    "Incorrect. Option 82 insertion is a DHCP relay agent feature. While Option 82 misconfiguration "
                    "can cause issues, the most common cause of DHCP failure after enabling snooping is forgetting "
                    "to mark the uplink toward the DHCP server as trusted."
                ),
            },
            {
                "id": "c",
                "text": "ip dhcp snooping verify mac-address (disable MAC address verification)",
                "correct": False,
                "rationale": (
                    "Incorrect. 'ip dhcp snooping verify mac-address' (enabled by default) checks that the CHADDR "
                    "field in DHCP requests matches the source MAC in the Ethernet frame. "
                    "Disabling this is not the fix for the described problem."
                ),
            },
            {
                "id": "d",
                "text": "no ip dhcp snooping (disable snooping entirely to restore DHCP)",
                "correct": False,
                "rationale": (
                    "Incorrect. Disabling snooping would restore DHCP but eliminates the security protection. "
                    "The correct solution is to trust only the uplink port(s) toward legitimate DHCP servers, "
                    "maintaining snooping protection on all access ports."
                ),
            },
        ],
        "explanation": (
            "When DHCP snooping is first enabled, all ports are untrusted by default. DHCP server messages "
            "(OFFER, ACK, NAK) are dropped on untrusted ports. Uplink interfaces toward legitimate DHCP servers "
            "must be explicitly configured with 'ip dhcp snooping trust'. Forgetting to trust uplinks is the "
            "most common deployment mistake. Trunk ports to other switches carrying server traffic must also be trusted. "
            "Only access ports facing end users should remain untrusted."
        ),
    },
    {
        "id": "cd5-028",
        "domain": 5,
        "objective": "5.6",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Access control lists (ACLs)",
        "stem": (
            "Select TWO statements that are TRUE about standard numbered ACLs on Cisco IOS routers."
        ),
        "options": [
            {
                "id": "a",
                "text": "Standard ACLs can filter traffic based on source IP address, destination IP address, and TCP/UDP port number.",
                "correct": False,
                "rationale": (
                    "Incorrect. Standard ACLs filter ONLY by source IP address. Filtering by destination IP and "
                    "TCP/UDP port is the function of extended ACLs (numbered 100-199 or 2000-2699)."
                ),
            },
            {
                "id": "b",
                "text": "Standard numbered ACLs use numbers in the range 1-99 and 1300-1999.",
                "correct": True,
                "rationale": (
                    "Correct. Standard ACLs use the number ranges 1-99 (original) and 1300-1999 (expanded). "
                    "Extended ACLs use 100-199 and 2000-2699."
                ),
            },
            {
                "id": "c",
                "text": "An implicit 'deny ip any any' is appended to every ACL and matches all traffic not explicitly permitted.",
                "correct": True,
                "rationale": (
                    "Correct. Every Cisco ACL ends with an implicit 'deny ip any any'. Any packet that does not match "
                    "any explicit entry is silently dropped. This is why a 'permit any' is often needed at the end "
                    "of a restrictive ACL to allow non-targeted traffic."
                ),
            },
            {
                "id": "d",
                "text": "When a new ACE is added to a numbered ACL, it is inserted before existing entries in sequence order.",
                "correct": False,
                "rationale": (
                    "Incorrect. In classic numbered ACLs (not named/sequenced), new entries are always appended "
                    "to the end of the ACL. To insert entries in a specific position in numbered ACLs, "
                    "you must use the named ACL or IP named ACL sequence number editing feature. "
                    "With numbered ACLs edited in legacy mode, adding statements always appends them."
                ),
            },
        ],
        "explanation": (
            "Standard ACL key facts: (1) Number ranges: 1-99 and 1300-1999. (2) Filter source IP only. "
            "(3) Implicit deny-all at the end — always. (4) Numbered ACL entries are appended in order; "
            "to insert out-of-order, delete and recreate the ACL or use named ACL with sequence numbers. "
            "Named ACLs (ip access-list standard NAME) allow sequence-number-based insertion and deletion of individual entries."
        ),
    },
    {
        "id": "cd5-029",
        "domain": 5,
        "objective": "5.7",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Port security",
        "stem": (
            "Select TWO correct statements about port security violation modes on Cisco Catalyst switches."
        ),
        "options": [
            {
                "id": "a",
                "text": "In 'protect' mode, frames from violating MAC addresses are dropped and a syslog message is generated.",
                "correct": False,
                "rationale": (
                    "Incorrect. In 'protect' mode, violating frames are dropped but NO syslog message or SNMP trap "
                    "is generated. Syslog notification is the behavior of 'restrict' mode."
                ),
            },
            {
                "id": "b",
                "text": "In 'restrict' mode, violating frames are dropped and the security violation counter increments.",
                "correct": True,
                "rationale": (
                    "Correct. 'Restrict' mode drops frames from violating MAC addresses, increments the violation counter, "
                    "and sends a syslog/SNMP notification. The port remains operational."
                ),
            },
            {
                "id": "c",
                "text": "The default violation mode is 'shutdown', which places the port in err-disabled state when a violation occurs.",
                "correct": True,
                "rationale": (
                    "Correct. If no violation mode is configured, 'shutdown' is the default. A security violation "
                    "immediately err-disables the port, which must be manually recovered with 'shutdown/no shutdown' "
                    "or automatically via errdisable recovery."
                ),
            },
            {
                "id": "d",
                "text": "In 'shutdown' mode, only frames from the violating MAC are dropped; frames from permitted MACs continue to forward.",
                "correct": False,
                "rationale": (
                    "Incorrect. In 'shutdown' mode, the ENTIRE port is err-disabled, blocking ALL traffic — not just "
                    "frames from the violating MAC. This is distinct from 'protect' and 'restrict', "
                    "which drop only violating frames while allowing legitimate traffic."
                ),
            },
        ],
        "explanation": (
            "Port security violation mode comparison:\n"
            "- protect: drops violating frames, no notification, port stays up.\n"
            "- restrict: drops violating frames, increments counter, sends syslog/SNMP, port stays up.\n"
            "- shutdown (default): err-disables the entire port, sends syslog, counter increments.\n"
            "Recovery from err-disabled requires manual 'shutdown/no shutdown' or 'errdisable recovery cause psecure-violation'."
        ),
    },
    {
        "id": "cd5-030",
        "domain": 5,
        "objective": "5.8",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "AAA (RADIUS vs TACACS+)",
        "stem": (
            "Select TWO statements that accurately compare RADIUS and TACACS+ for AAA implementations."
        ),
        "options": [
            {
                "id": "a",
                "text": "RADIUS uses TCP port 49 for all AAA communications, providing reliable transport.",
                "correct": False,
                "rationale": (
                    "Incorrect. TCP port 49 is used by TACACS+, not RADIUS. "
                    "RADIUS uses UDP port 1812 for authentication/authorization and UDP port 1813 for accounting."
                ),
            },
            {
                "id": "b",
                "text": "TACACS+ encrypts the entire packet body, while RADIUS encrypts only the password field in the authentication request.",
                "correct": True,
                "rationale": (
                    "Correct. TACACS+ uses full-packet encryption (excluding the header) using a shared secret. "
                    "RADIUS only encrypts the User-Password attribute in Access-Request packets; "
                    "other attributes (username, AVPs) are sent in cleartext."
                ),
            },
            {
                "id": "c",
                "text": "RADIUS is preferred for network device (CLI) administration because it supports per-command authorization natively.",
                "correct": False,
                "rationale": (
                    "Incorrect. TACACS+ is preferred for device administration because it supports per-command "
                    "authorization. RADIUS combines authentication and authorization and does not natively support "
                    "granular command-level control."
                ),
            },
            {
                "id": "d",
                "text": "TACACS+ separates authentication, authorization, and accounting into independent AAA functions, allowing each to be handled by different servers or policies.",
                "correct": True,
                "rationale": (
                    "Correct. TACACS+ uses separate control exchanges for authentication, authorization, and accounting, "
                    "which allows independent policy control and even different servers for each function. "
                    "RADIUS combines authentication and authorization in a single exchange."
                ),
            },
        ],
        "explanation": (
            "RADIUS vs TACACS+ quick reference:\n"
            "RADIUS: UDP 1812 (auth/authz), UDP 1813 (accounting); encrypts password only; "
            "combines auth+authz; best for network access (802.1X, VPN, wireless).\n"
            "TACACS+: TCP 49; encrypts full body; separates auth/authz/acct; per-command authorization; "
            "best for device administration (router/switch CLI). "
            "Both support multi-vendor deployments but TACACS+ originated as Cisco-proprietary."
        ),
    },
]

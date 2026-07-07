QUESTIONS = [
    # ── cd5v2-001 ── ACL wildcard mask: /20 ───────────────────────────────────
    {
        "id": "cd5v2-001",
        "domain": 5,
        "objective": "5.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "ACL placement & wildcard masks",
        "stem": (
            "A network administrator must permit traffic from the 172.16.48.0/20 network "
            "in an extended ACL. Which wildcard mask correctly represents this prefix?"
        ),
        "options": [
            {
                "id": "a",
                "text": "0.0.15.255",
                "correct": True,
                "rationale": (
                    "Correct. A /20 mask is 255.255.240.0. Inverting each octet: "
                    "255-255=0, 255-255=0, 255-240=15, 255-0=255 → wildcard 0.0.15.255. "
                    "This matches all 4096 addresses in 172.16.48.0–172.16.63.255."
                ),
            },
            {
                "id": "b",
                "text": "0.0.7.255",
                "correct": False,
                "rationale": (
                    "Incorrect. Wildcard 0.0.7.255 is the inverse of /21 (255.255.248.0), "
                    "matching only 2048 addresses (172.16.48.0–172.16.55.255). "
                    "This is half the /20 range."
                ),
            },
            {
                "id": "c",
                "text": "0.0.255.255",
                "correct": False,
                "rationale": (
                    "Incorrect. 0.0.255.255 is the wildcard for a /16 (255.255.0.0), "
                    "which would match the entire 172.16.0.0/16 block — far broader than /20."
                ),
            },
            {
                "id": "d",
                "text": "0.0.0.255",
                "correct": False,
                "rationale": (
                    "Incorrect. 0.0.0.255 represents a /24 wildcard, matching only the single "
                    "/24 block 172.16.48.0–172.16.48.255, not the full /20 range."
                ),
            },
        ],
        "explanation": (
            "Wildcard mask = 255.255.255.255 minus the subnet mask. "
            "For /20 (255.255.240.0): 255-240=15 in the third octet, 255-0=255 in the fourth → 0.0.15.255. "
            "A /20 contains 2^12 = 4096 host addresses. "
            "The ACL entry would be: permit ip 172.16.48.0 0.0.15.255 any."
        ),
    },
    # ── cd5v2-002 ── ACL wildcard mask: non-contiguous /25 ───────────────────
    {
        "id": "cd5v2-002",
        "domain": 5,
        "objective": "5.6",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "ACL placement & wildcard masks",
        "stem": (
            "An engineer needs one ACL entry to match both 10.0.0.0/24 and 10.0.1.0/24 "
            "but NO other subnets. Which single ACL statement achieves this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "access-list 1 permit 10.0.0.0 0.0.1.255",
                "correct": True,
                "rationale": (
                    "Correct. Wildcard 0.0.1.255 means the third octet bit-0 can be 0 or 1 "
                    "while the fourth octet matches anything (0–255). This matches 10.0.0.0–10.0.1.255 "
                    "— exactly the two /24 blocks and nothing more."
                ),
            },
            {
                "id": "b",
                "text": "access-list 1 permit 10.0.0.0 0.0.0.255",
                "correct": False,
                "rationale": (
                    "Incorrect. Wildcard 0.0.0.255 matches only 10.0.0.0/24 (10.0.0.0–10.0.0.255). "
                    "10.0.1.0/24 would not be matched and would require a separate ACE."
                ),
            },
            {
                "id": "c",
                "text": "access-list 1 permit 10.0.0.0 0.0.3.255",
                "correct": False,
                "rationale": (
                    "Incorrect. Wildcard 0.0.3.255 matches four /24 blocks: 10.0.0.0–10.0.3.255 (/22), "
                    "which includes 10.0.2.0 and 10.0.3.0 beyond the requirement."
                ),
            },
            {
                "id": "d",
                "text": "access-list 1 permit 10.0.0.0 0.0.255.255",
                "correct": False,
                "rationale": (
                    "Incorrect. Wildcard 0.0.255.255 matches the entire 10.0.0.0/16 range "
                    "(10.0.0.0–10.0.255.255), which is far broader than the two /24 subnets required."
                ),
            },
        ],
        "explanation": (
            "When two contiguous same-size networks differ only in one bit, a single wildcard ACE can cover both. "
            "10.0.0.0 and 10.0.1.0 differ in bit 0 of the third octet. Setting that bit to 'don't care' (1) "
            "and the fourth octet fully to 'don't care' (255) gives wildcard 0.0.1.255, matching both /24s only. "
            "Choosing the correct summary wildcard requires binary analysis of the differing bit positions."
        ),
    },
    # ── cd5v2-003 ── ACLs: extended, deny ICMP ────────────────────────────────
    {
        "id": "cd5v2-003",
        "domain": 5,
        "objective": "5.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Access control lists (ACLs)",
        "stem": (
            "An engineer applies the following extended ACL inbound on Gi0/0 "
            "(connected to the 192.168.10.0/24 LAN):\n\n"
            "ip access-list extended LAN_FILTER\n"
            " 10 deny icmp 192.168.10.0 0.0.0.255 any\n"
            " 20 permit ip any any\n\n"
            "Host 192.168.10.5 pings 8.8.8.8. Host 10.0.0.1 pings 192.168.10.5. "
            "Which statement is correct?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The ping from 192.168.10.5 is dropped; the ping from 10.0.0.1 is permitted.",
                "correct": True,
                "rationale": (
                    "Correct. ACE 10 denies ICMP sourced from 192.168.10.0/24. "
                    "Host 192.168.10.5's ICMP echo is denied because it is applied inbound and the source matches. "
                    "Host 10.0.0.1 is not in 192.168.10.0/24, so ACE 10 does not match; ACE 20 permits the ICMP."
                ),
            },
            {
                "id": "b",
                "text": "Both pings are denied because ACE 10 matches all ICMP traffic on the interface.",
                "correct": False,
                "rationale": (
                    "Incorrect. ACE 10 specifies source 192.168.10.0 0.0.0.255 — it only matches ICMP sent from "
                    "that subnet. Traffic from 10.0.0.1 does not match ACE 10 and is permitted by ACE 20."
                ),
            },
            {
                "id": "c",
                "text": "Both pings are permitted because the ACL only evaluates outbound traffic.",
                "correct": False,
                "rationale": (
                    "Incorrect. The ACL is explicitly applied inbound on Gi0/0. It filters packets as they enter "
                    "the router interface from the LAN, so traffic from 192.168.10.0/24 is evaluated."
                ),
            },
            {
                "id": "d",
                "text": "The ping from 192.168.10.5 is permitted; the ping from 10.0.0.1 is denied by the implicit deny.",
                "correct": False,
                "rationale": (
                    "Incorrect. 192.168.10.5 matches ACE 10 (ICMP from 192.168.10.0/24) and is denied. "
                    "10.0.0.1 does not match ACE 10, skips to ACE 20 (permit ip any any), and is forwarded."
                ),
            },
        ],
        "explanation": (
            "Extended ACLs match on protocol, source IP+wildcard, destination IP+wildcard, and optionally port. "
            "Applied inbound on Gi0/0 (LAN side), ACE 10 drops ICMP only from 192.168.10.0/24 sources. "
            "Return ICMP replies (source from 8.8.8.8) entering from the WAN interface — a different interface — "
            "are not evaluated by this ACL. Always identify the interface direction when analyzing ACL behavior."
        ),
    },
    # ── cd5v2-004 ── ACLs: named ACL sequence editing ─────────────────────────
    {
        "id": "cd5v2-004",
        "domain": 5,
        "objective": "5.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Access control lists (ACLs)",
        "stem": (
            "An engineer needs to insert a new deny statement between sequence numbers 10 and 20 "
            "in an existing named extended ACL called CORP_FILTER. "
            "Which approach is correct on a Cisco IOS router?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Enter 'ip access-list extended CORP_FILTER' then add '15 deny tcp 10.5.0.0 0.0.0.255 any eq 23' to insert it between ACEs 10 and 20.",
                "correct": True,
                "rationale": (
                    "Correct. Named ACLs support sequence-number editing. Entering the ACL configuration mode "
                    "and specifying sequence number 15 inserts the new ACE between the existing entries at 10 and 20 "
                    "without deleting and recreating the entire ACL."
                ),
            },
            {
                "id": "b",
                "text": "Delete the ACL with 'no ip access-list extended CORP_FILTER', recreate all entries in the correct order.",
                "correct": False,
                "rationale": (
                    "Incorrect. While this would work, it is not the preferred method. Named ACLs support "
                    "in-place sequence-number insertion, avoiding the need to delete and fully recreate the ACL."
                ),
            },
            {
                "id": "c",
                "text": "Use 'ip access-list resequence CORP_FILTER 5 5' then add the new entry as sequence 15.",
                "correct": False,
                "rationale": (
                    "Incorrect. Resequencing (ip access-list resequence) renumbers existing entries and is useful "
                    "when entries are too close together to insert between them. If ACEs are at 10 and 20 already, "
                    "there is room for sequence 15 without resequencing first."
                ),
            },
            {
                "id": "d",
                "text": "Numbered ACLs and named ACLs both only allow appending new entries; sequence insertion requires IOS XE 16.x or later.",
                "correct": False,
                "rationale": (
                    "Incorrect. Named ACL sequence editing has been supported in Cisco IOS for many years. "
                    "It is NUMBERED ACLs (in legacy mode) that only allow appending. Named ACLs have always "
                    "supported sequence-based insertion and per-entry deletion."
                ),
            },
        ],
        "explanation": (
            "Named ACLs (ip access-list extended NAME or ip access-list standard NAME) support granular editing: "
            "individual entries can be deleted by sequence number ('no 15') and new entries can be inserted at any "
            "sequence number. Numbered ACLs in legacy (non-sequenced) mode only append entries. "
            "To insert between 10 and 20: enter the named ACL, type '15 deny ...' — IOS inserts it in order. "
            "'ip access-list resequence' is used when entries are spaced too closely (e.g., consecutive) to insert between."
        ),
    },
    # ── cd5v2-005 ── ACLs: reflexive ACL concept ──────────────────────────────
    {
        "id": "cd5v2-005",
        "domain": 5,
        "objective": "5.6",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Access control lists (ACLs)",
        "stem": (
            "A Cisco router is the only security device between an internal network and the internet. "
            "An engineer wants to permit only TCP sessions initiated from inside while blocking unsolicited "
            "inbound TCP from the internet, without using a stateful firewall or CBAC. "
            "Which IOS ACL feature provides this behavior?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Reflexive ACLs using 'reflect' and 'evaluate' keywords, which dynamically create temporary permit entries for return traffic matching established sessions.",
                "correct": True,
                "rationale": (
                    "Correct. Reflexive ACLs use 'permit tcp any any reflect SESSION_NAME' on outbound traffic "
                    "and 'evaluate SESSION_NAME' on the inbound ACL. When an inside host initiates a session, "
                    "a temporary dynamic ACE is created to allow the matching return traffic, then removed when "
                    "the session ends. This provides stateful-like filtering using only ACLs."
                ),
            },
            {
                "id": "b",
                "text": "Extended ACL with 'established' keyword, which permits TCP packets with ACK or RST bits set.",
                "correct": False,
                "rationale": (
                    "Incorrect. The 'established' keyword permits TCP with ACK or RST flags — but an attacker can "
                    "simply set the ACK bit to bypass this check. It does not track actual session state and is "
                    "less secure than reflexive ACLs."
                ),
            },
            {
                "id": "c",
                "text": "Standard ACL with 'dynamic' keyword applied inbound on the external interface.",
                "correct": False,
                "rationale": (
                    "Incorrect. Dynamic ACLs (Lock-and-Key) require a Telnet/SSH authentication before temporarily "
                    "permitting the authenticated host through. They are not designed for automatic session-based "
                    "return traffic filtering."
                ),
            },
            {
                "id": "d",
                "text": "Turbo ACL feature, which compiles ACLs into a lookup table for faster session matching.",
                "correct": False,
                "rationale": (
                    "Incorrect. Turbo ACL is a performance optimization feature that compiles ACL tables for faster "
                    "processing. It does not add session-tracking or dynamic permit functionality."
                ),
            },
        ],
        "explanation": (
            "Reflexive ACLs (IOS feature) provide session-tracking without CBAC or Zone-Based Firewall. "
            "Configuration: outbound ACL includes 'permit tcp inside_net any reflect MYSESS'; "
            "inbound ACL includes 'evaluate MYSESS'. When an outbound TCP flow is seen, a temporary "
            "inbound ACE is dynamically created matching the reverse 5-tuple. The ACE is removed on FIN/RST "
            "or timeout. The 'established' keyword is simpler but less secure (no real state tracking)."
        ),
    },
    # ── cd5v2-006 ── Port security: absolute maximum on trunk ─────────────────
    {
        "id": "cd5v2-006",
        "domain": 5,
        "objective": "5.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Port security",
        "stem": (
            "An engineer issues 'switchport port-security' on interface Gi0/1. "
            "No other port-security commands are entered. "
            "Which set of defaults applies to this interface?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Maximum 1 MAC address; violation mode: shutdown; MAC learning: dynamic (not sticky).",
                "correct": True,
                "rationale": (
                    "Correct. Cisco Catalyst switch port security defaults: maximum 1 allowed MAC, "
                    "violation mode shutdown, and dynamic (non-sticky) MAC learning. "
                    "Sticky must be explicitly configured with 'switchport port-security mac-address sticky'."
                ),
            },
            {
                "id": "b",
                "text": "Maximum 2 MAC addresses; violation mode: restrict; MAC learning: sticky.",
                "correct": False,
                "rationale": (
                    "Incorrect. The default maximum is 1 (not 2), the default violation mode is shutdown "
                    "(not restrict), and sticky is not enabled by default."
                ),
            },
            {
                "id": "c",
                "text": "Maximum 1 MAC address; violation mode: protect; MAC learning: dynamic.",
                "correct": False,
                "rationale": (
                    "Incorrect. The maximum of 1 is correct, but the default violation mode is shutdown, "
                    "not protect. Protect mode must be explicitly configured."
                ),
            },
            {
                "id": "d",
                "text": "Maximum 128 MAC addresses; violation mode: shutdown; MAC learning: sticky.",
                "correct": False,
                "rationale": (
                    "Incorrect. The default maximum is 1 allowed MAC, not 128. "
                    "Sticky MAC learning is also not the default — it must be explicitly enabled."
                ),
            },
        ],
        "explanation": (
            "Cisco port security defaults when only 'switchport port-security' is entered: "
            "maximum MAC addresses = 1; violation mode = shutdown (err-disables the port); "
            "MAC learning = dynamic (not sticky). These are the three most commonly tested defaults. "
            "The interface must already be in access mode ('switchport mode access') before port security "
            "can be enabled; port security is not supported on trunk or dynamic-auto/desirable ports."
        ),
    },
    # ── cd5v2-007 ── Port security: aging absolute vs inactivity ──────────────
    {
        "id": "cd5v2-007",
        "domain": 5,
        "objective": "5.7",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Port security",
        "stem": (
            "A switchport is configured with port security aging:\n\n"
            "switchport port-security maximum 3\n"
            "switchport port-security aging time 5\n"
            "switchport port-security aging type inactivity\n\n"
            "Three MAC addresses are currently in the secure MAC table. "
            "One of the hosts has been silent for 6 minutes. A fourth device connects. "
            "What happens?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The silent host's MAC is aged out, reducing the count to 2. The fourth device is learned, bringing the total to 3. No violation occurs.",
                "correct": True,
                "rationale": (
                    "Correct. With 'aging type inactivity', a secure MAC is removed from the table after it "
                    "has been idle (no frames received) for the configured aging time (5 minutes). "
                    "The host silent for 6 minutes exceeds the 5-minute threshold and is removed. "
                    "The fourth MAC fills the now-available slot without exceeding the maximum of 3."
                ),
            },
            {
                "id": "b",
                "text": "The fourth device triggers a violation because aging does not apply to dynamic secure MACs.",
                "correct": False,
                "rationale": (
                    "Incorrect. Aging applies to dynamically learned secure MACs (and sticky MACs when aging "
                    "type is configured). The inactivity timer removes the idle entry, making room for the new device."
                ),
            },
            {
                "id": "c",
                "text": "The port is err-disabled because the maximum is 3 and a fourth device is present.",
                "correct": False,
                "rationale": (
                    "Incorrect. Aging has already removed the idle MAC before the fourth device connects, "
                    "so the table has only 2 entries when the new device arrives. The maximum of 3 is not exceeded."
                ),
            },
            {
                "id": "d",
                "text": "All three existing MACs are aged out after 5 minutes regardless of activity.",
                "correct": False,
                "rationale": (
                    "Incorrect. The 'inactivity' aging type only removes MACs that have been inactive for the "
                    "configured period. The two hosts that are still sending traffic are NOT aged out. "
                    "The 'absolute' aging type (not configured here) would remove MACs after a fixed time regardless "
                    "of activity."
                ),
            },
        ],
        "explanation": (
            "Port security MAC aging types: 'absolute' — removes a secure MAC after the aging time regardless "
            "of activity (useful for periodically flushing entries). 'inactivity' — removes a secure MAC only "
            "after it has not sent any frames for the aging period (more lenient; keeps active devices). "
            "Aging allows dynamic slot recycling, making port security more flexible in environments "
            "with hot-desking or shared ports."
        ),
    },
    # ── cd5v2-008 ── Port security: recover err-disabled ─────────────────────
    {
        "id": "cd5v2-008",
        "domain": 5,
        "objective": "5.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Port security",
        "stem": (
            "Interface Fa0/10 is in err-disabled state due to a port security violation. "
            "An engineer wants to configure the switch to automatically recover the port "
            "after 120 seconds without manual intervention. "
            "Which global configuration command achieves this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "errdisable recovery cause psecure-violation\nerrdisable recovery interval 120",
                "correct": True,
                "rationale": (
                    "Correct. 'errdisable recovery cause psecure-violation' enables automatic recovery "
                    "for ports err-disabled due to port security violations. "
                    "'errdisable recovery interval 120' sets the recovery timer to 120 seconds. "
                    "After the interval, the switch re-enables the port."
                ),
            },
            {
                "id": "b",
                "text": "switchport port-security recover 120 (under the interface)",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no 'switchport port-security recover' interface command. "
                    "Automatic err-disabled recovery is configured globally with 'errdisable recovery cause' "
                    "and 'errdisable recovery interval'."
                ),
            },
            {
                "id": "c",
                "text": "spanning-tree portfast bpduguard recovery-interval 120",
                "correct": False,
                "rationale": (
                    "Incorrect. This is a BPDU Guard recovery command, not port security. "
                    "Each err-disable cause has its own 'errdisable recovery cause <reason>' command."
                ),
            },
            {
                "id": "d",
                "text": "interface Fa0/10 → shutdown → no shutdown (must be done manually each time)",
                "correct": False,
                "rationale": (
                    "Incorrect. Manual shutdown/no-shutdown does recover the port, but the question asks "
                    "for automatic recovery without manual intervention, which requires the global "
                    "'errdisable recovery' commands."
                ),
            },
        ],
        "explanation": (
            "Err-disabled automatic recovery: 'errdisable recovery cause <reason>' enables auto-recovery "
            "for a specific cause (psecure-violation, bpduguard, udld, etc.). "
            "'errdisable recovery interval <seconds>' sets the polling interval (default 300 seconds). "
            "After the timer expires, the switch attempts to bring the interface up. "
            "If the violation condition still exists, the port will be err-disabled again immediately. "
            "Verify with: 'show errdisable recovery'."
        ),
    },
    # ── cd5v2-009 ── DHCP snooping: Option 82 trust ───────────────────────────
    {
        "id": "cd5v2-009",
        "domain": 5,
        "objective": "5.7",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "DHCP snooping & DAI",
        "stem": (
            "DHCP snooping is enabled. Clients behind an access switch are receiving DHCP addresses "
            "successfully. However, clients behind a second access switch connected via an intermediate "
            "distribution switch are failing to get DHCP leases. Both uplinks on all switches are marked "
            "as trusted. The distribution switch has 'ip dhcp snooping information option' enabled (default). "
            "What is the MOST likely cause of the failure?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The core (or DHCP relay) router is dropping packets with DHCP Option 82, and 'no ip dhcp snooping information option allow-untrusted' must be configured on the intermediate switch.",
                "correct": False,
                "rationale": (
                    "Incorrect. The issue described is caused by Option 82 being inserted by the access switch "
                    "and then re-checked at the distribution switch. The correct fix is different."
                ),
            },
            {
                "id": "b",
                "text": "The distribution switch is dropping DHCP requests from the downstream access switch because Option 82 inserted by the downstream switch causes the distribution switch's snooping engine to drop packets arriving on an untrusted port that already contain Option 82.",
                "correct": True,
                "rationale": (
                    "Correct. When a downstream access switch inserts Option 82 and forwards the DHCP request "
                    "upward, the next DHCP snooping-enabled switch (distribution) sees Option 82 on an untrusted "
                    "uplink and drops it by default. The fix: 'ip dhcp snooping information option allow-untrusted' "
                    "on the distribution switch, or trust the inter-switch link."
                ),
            },
            {
                "id": "c",
                "text": "The DHCP server cannot process Option 82 fields and silently discards the requests.",
                "correct": False,
                "rationale": (
                    "Incorrect. Standard DHCP servers can process or ignore Option 82 without discarding requests. "
                    "The issue here is at the intermediate switch's DHCP snooping layer, not the server."
                ),
            },
            {
                "id": "d",
                "text": "The binding table on the distribution switch is full and cannot record new entries.",
                "correct": False,
                "rationale": (
                    "Incorrect. DHCP snooping binding table limits are rarely a cause of complete client failure "
                    "in a typical campus environment. The symptom described matches an Option 82 trust issue."
                ),
            },
        ],
        "explanation": (
            "DHCP snooping Option 82 (relay agent information) is inserted by the first snooping-enabled switch. "
            "When a downstream switch already inserts Option 82 and the distribution switch's snooping engine "
            "sees this option arriving on an untrusted port, it drops the packet (by default, snooping drops "
            "DHCP messages with Option 82 on untrusted ports if 'ip dhcp snooping information option' is enabled). "
            "Fix: 'ip dhcp snooping information option allow-untrusted' at the distribution switch, "
            "or mark the inter-switch link as trusted."
        ),
    },
    # ── cd5v2-010 ── DAI: ARP ACL for static hosts ────────────────────────────
    {
        "id": "cd5v2-010",
        "domain": 5,
        "objective": "5.7",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "DHCP snooping & DAI",
        "stem": (
            "DAI is enabled on VLAN 30. The default gateway (192.168.30.1) has a static IP "
            "and does not appear in the DHCP snooping binding table. "
            "Which command sequence allows the gateway's ARP packets to pass DAI validation?"
        ),
        "options": [
            {
                "id": "a",
                "text": "arp access-list GW_ARP\n permit ip host 192.168.30.1 mac host 0050.7966.0001\nip arp inspection filter GW_ARP vlan 30",
                "correct": True,
                "rationale": (
                    "Correct. A static ARP ACL bypasses the DHCP snooping binding table check for the specified "
                    "IP-to-MAC mapping. 'ip arp inspection filter <name> vlan <id>' applies the ARP ACL to VLAN 30, "
                    "allowing the gateway's ARP (which has no DHCP binding) to be validated and forwarded."
                ),
            },
            {
                "id": "b",
                "text": "ip dhcp snooping binding 0050.7966.0001 vlan 30 192.168.30.1 interface Gi0/1 expiry 86400",
                "correct": False,
                "rationale": (
                    "Incorrect. While manually adding a static DHCP snooping binding entry would also work, "
                    "the 'arp access-list' method is the documented Cisco best practice specifically for "
                    "devices with static IPs that need to pass DAI without DHCP bindings."
                ),
            },
            {
                "id": "c",
                "text": "ip arp inspection trust (on the gateway's port), which bypasses DAI for all ARP from that port.",
                "correct": False,
                "rationale": (
                    "Incorrect. Marking the gateway port as 'trusted' for DAI would bypass validation entirely "
                    "for that port — a security risk if the port connects to a shared segment. "
                    "The ARP ACL method is more targeted and secure."
                ),
            },
            {
                "id": "d",
                "text": "no ip arp inspection vlan 30 (disable DAI on VLAN 30 to allow the gateway's ARPs).",
                "correct": False,
                "rationale": (
                    "Incorrect. Disabling DAI entirely removes protection for all hosts on VLAN 30. "
                    "The correct solution is a targeted ARP ACL that allows only the specific gateway "
                    "IP-to-MAC mapping while keeping DAI active for all other traffic."
                ),
            },
        ],
        "explanation": (
            "Devices with statically configured IPs do not generate DHCP traffic and therefore have no entry "
            "in the DHCP snooping binding table. DAI would drop their ARP packets (legitimate) as unvalidated. "
            "Solution: create an ARP ACL that explicitly permits the known IP-MAC mapping, then apply it to "
            "the VLAN with 'ip arp inspection filter <name> vlan <id>'. "
            "Alternatively, a static DHCP snooping binding ('ip dhcp snooping binding') can be added manually."
        ),
    },
    # ── cd5v2-011 ── AAA: RADIUS ports and attributes ─────────────────────────
    {
        "id": "cd5v2-011",
        "domain": 5,
        "objective": "5.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "AAA (RADIUS vs TACACS+)",
        "stem": (
            "A network engineer is troubleshooting 802.1X authentication failures. "
            "A packet capture shows RADIUS Access-Request packets leaving the switch but no "
            "Access-Challenge or Access-Accept is received. The RADIUS server IP is correct. "
            "Which UDP ports must be permitted in the firewall ACL between the switch and the RADIUS server?"
        ),
        "options": [
            {
                "id": "a",
                "text": "UDP 1812 (authentication) and UDP 1813 (accounting)",
                "correct": True,
                "rationale": (
                    "Correct. Modern RADIUS uses UDP 1812 for authentication and authorization (Access-Request, "
                    "Access-Accept, Access-Reject, Access-Challenge) and UDP 1813 for accounting (Accounting-Request, "
                    "Accounting-Response). Both must be open between the NAS and RADIUS server."
                ),
            },
            {
                "id": "b",
                "text": "UDP 1645 (authentication) and UDP 1646 (accounting)",
                "correct": False,
                "rationale": (
                    "Incorrect. UDP 1645/1646 are the legacy RADIUS ports used by older implementations. "
                    "Modern RADIUS (RFC 2865/2866) uses 1812/1813. While some servers support both, "
                    "the standard ports are 1812/1813."
                ),
            },
            {
                "id": "c",
                "text": "TCP 49 (authentication) and UDP 1813 (accounting)",
                "correct": False,
                "rationale": (
                    "Incorrect. TCP 49 is the port used by TACACS+, not RADIUS. "
                    "RADIUS authentication uses UDP 1812."
                ),
            },
            {
                "id": "d",
                "text": "TCP 1812 (authentication) and TCP 1813 (accounting)",
                "correct": False,
                "rationale": (
                    "Incorrect. RADIUS uses UDP, not TCP. TCP 49 belongs to TACACS+. "
                    "Specifying TCP for RADIUS ports indicates confusion between the two protocols."
                ),
            },
        ],
        "explanation": (
            "RADIUS port reference: UDP 1812 = authentication + authorization (RFC 2865); "
            "UDP 1813 = accounting (RFC 2866). Legacy ports: UDP 1645/1646. "
            "TACACS+ uses TCP 49. For 802.1X troubleshooting, ensure firewall rules permit "
            "UDP 1812 bidirectionally between the NAD (switch/AP) and RADIUS server. "
            "The switch sends Access-Request on UDP 1812; the server replies on the same port to the source port."
        ),
    },
    # ── cd5v2-012 ── AAA: TACACS+ command authorization ──────────────────────
    {
        "id": "cd5v2-012",
        "domain": 5,
        "objective": "5.8",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "AAA (RADIUS vs TACACS+)",
        "stem": (
            "A Cisco ISE (Identity Services Engine) deployment uses TACACS+ for device administration. "
            "A junior engineer with privilege level 7 logs into a router but is blocked from running "
            "'show running-config' even though the IOS command requires only privilege level 5. "
            "No local AAA override is configured. What is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The TACACS+ authorization policy on ISE is denying 'show running-config' for this engineer's profile regardless of the IOS privilege level assignment.",
                "correct": True,
                "rationale": (
                    "Correct. With TACACS+ command authorization, ISE evaluates each command against the "
                    "authorization policy, not just the privilege level. A policy that does not explicitly "
                    "permit 'show running-config' will deny it, even if the IOS privilege level would normally allow it."
                ),
            },
            {
                "id": "b",
                "text": "The engineer's RADIUS group policy does not include the AV pair for 'show running-config'.",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario uses TACACS+ (not RADIUS) for device administration. "
                    "RADIUS does not support per-command authorization; TACACS+ does."
                ),
            },
            {
                "id": "c",
                "text": "The 'privilege exec level 5 show running-config' command is missing from the router configuration.",
                "correct": False,
                "rationale": (
                    "Incorrect. When TACACS+ command authorization is active, IOS defers the authorization "
                    "decision to the TACACS+ server, not to local privilege levels. The server-side policy "
                    "takes precedence over local privilege level assignment."
                ),
            },
            {
                "id": "d",
                "text": "Privilege level 7 does not permit any show commands; only privilege level 15 does.",
                "correct": False,
                "rationale": (
                    "Incorrect. IOS privilege levels 1–15 exist, and 'show running-config' is configurable "
                    "at any level. With TACACS+, per-command authorization overrides IOS privilege levels — "
                    "the issue is the ISE policy, not the IOS privilege system."
                ),
            },
        ],
        "explanation": (
            "TACACS+ command authorization allows the AAA server (ISE) to approve or deny individual CLI "
            "commands. When 'aaa authorization commands <level> default group tacacs+ local' is configured, "
            "every command entered at that privilege level is sent to ISE for approval. "
            "The ISE TACACS+ command authorization policy must explicitly permit commands "
            "(or use a catch-all permit). Commands not matched by a permit rule are denied. "
            "This is fundamentally different from RADIUS, which cannot do per-command authorization."
        ),
    },
    # ── cd5v2-013 ── AAA: local fallback ──────────────────────────────────────
    {
        "id": "cd5v2-013",
        "domain": 5,
        "objective": "5.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "AAA (RADIUS vs TACACS+)",
        "stem": (
            "A router is configured with:\n\n"
            "aaa new-model\n"
            "aaa authentication login default group tacacs+ local\n\n"
            "The TACACS+ server becomes unreachable. An admin tries to log in with local credentials. "
            "What happens?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The router attempts TACACS+ authentication first; if the server is unreachable (timeout), it falls back to the local user database.",
                "correct": True,
                "rationale": (
                    "Correct. The method list 'group tacacs+ local' specifies: try TACACS+ first. "
                    "If the server is unreachable (not if it returns a reject), fall back to the local database. "
                    "An admin with a local account can authenticate successfully when TACACS+ is down."
                ),
            },
            {
                "id": "b",
                "text": "Authentication fails completely because TACACS+ is unavailable and fallback is not configured.",
                "correct": False,
                "rationale": (
                    "Incorrect. The method list includes 'local' as the fallback after 'group tacacs+'. "
                    "Fallback IS configured — the 'local' keyword enables it."
                ),
            },
            {
                "id": "c",
                "text": "The router falls back to local credentials if TACACS+ returns an Access-Reject for any reason.",
                "correct": False,
                "rationale": (
                    "Incorrect. Fallback to the next method occurs only when the TACACS+ server is "
                    "UNREACHABLE (timeout/no response). If the server responds with an explicit reject "
                    "(wrong password), authentication fails immediately — the local database is NOT tried."
                ),
            },
            {
                "id": "d",
                "text": "The router ignores local credentials and locks out all users until TACACS+ is restored.",
                "correct": False,
                "rationale": (
                    "Incorrect. Including 'local' in the AAA method list explicitly enables local fallback "
                    "when TACACS+ is unreachable. This is a best practice to prevent complete lockout during "
                    "AAA server outages."
                ),
            },
        ],
        "explanation": (
            "AAA method list behavior: methods are tried in order. The next method is attempted ONLY if the "
            "current method's server does not respond (timeout). If a server responds with REJECT, "
            "authentication fails — no fallback occurs. This is critical: if an admin enters the wrong "
            "password and TACACS+ says 'reject', the local database is NOT tried. "
            "Always include 'local' or 'none' as the last method to prevent complete console lockout."
        ),
    },
    # ── cd5v2-014 ── Device access control: SSH hardening ────────────────────
    {
        "id": "cd5v2-014",
        "domain": 5,
        "objective": "5.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Device access control (passwords)",
        "stem": (
            "A network engineer runs 'show ip ssh' and sees:\n\n"
            "SSH Enabled - version 1.99\n"
            "Authentication timeout: 120 secs; Authentication retries: 3\n\n"
            "Which command forces the router to use ONLY SSHv2 and reject SSHv1 connections?"
        ),
        "options": [
            {
                "id": "a",
                "text": "ip ssh version 2",
                "correct": True,
                "rationale": (
                    "Correct. 'ip ssh version 2' restricts the SSH server to accept only SSHv2 connections. "
                    "Version 1.99 indicates compatibility mode (supports both v1 and v2). "
                    "Specifying version 2 explicitly disables SSHv1 support."
                ),
            },
            {
                "id": "b",
                "text": "crypto key generate rsa modulus 2048",
                "correct": False,
                "rationale": (
                    "Incorrect. Generating RSA keys enables SSH (and larger modulus improves security) "
                    "but does not restrict the version. 'ip ssh version 2' must be separately configured."
                ),
            },
            {
                "id": "c",
                "text": "transport input ssh version 2 (under the vty lines)",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no 'version 2' sub-option for 'transport input ssh'. "
                    "The version restriction is set globally with 'ip ssh version 2', "
                    "not under the vty line configuration."
                ),
            },
            {
                "id": "d",
                "text": "no ip ssh version 1",
                "correct": False,
                "rationale": (
                    "Incorrect. This is not a valid Cisco IOS command. The correct command to enforce SSHv2 "
                    "is 'ip ssh version 2' — not a negation of version 1."
                ),
            },
        ],
        "explanation": (
            "SSH version 1.99 means the router supports both SSHv1 and SSHv2. "
            "SSHv1 has known weaknesses (man-in-the-middle, weak integrity). "
            "To enforce SSHv2 only: 'ip ssh version 2'. "
            "Additional SSH hardening: 'ip ssh time-out 60' (reduce authentication timeout), "
            "'ip ssh authentication-retries 2' (reduce retry count), "
            "and RSA key size >= 2048 bits for adequate security."
        ),
    },
    # ── cd5v2-015 ── Device access control: console password ─────────────────
    {
        "id": "cd5v2-015",
        "domain": 5,
        "objective": "5.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Device access control (passwords)",
        "stem": (
            "A router has this configuration:\n\n"
            "line console 0\n"
            " login\n\n"
            "No 'password' command is configured under the console line. "
            "What happens when a user connects via the console cable?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The router prompts for a password but immediately rejects any entry because no line password is set; the console is effectively locked.",
                "correct": True,
                "rationale": (
                    "Correct. 'login' (without 'local') requires a line-level password set with the 'password' "
                    "command. If 'password' is missing, the router prompts for a password but cannot validate "
                    "any input — all entries are rejected. This effectively blocks console access."
                ),
            },
            {
                "id": "b",
                "text": "The user is granted access without any password prompt because 'login' without 'local' implies no authentication.",
                "correct": False,
                "rationale": (
                    "Incorrect. 'login' with no configured line password does NOT grant free access. "
                    "It prompts for a password but rejects everything because no password is defined. "
                    "To allow passwordless access, 'no login' must be configured."
                ),
            },
            {
                "id": "c",
                "text": "The router falls back to local username/password because no line password is configured.",
                "correct": False,
                "rationale": (
                    "Incorrect. Local fallback only occurs when 'login local' is configured. "
                    "'login' (without 'local') strictly uses the line password. No fallback mechanism exists "
                    "for a missing line password."
                ),
            },
            {
                "id": "d",
                "text": "The 'login' command is ignored and the user reaches EXEC mode immediately because the console line has no password.",
                "correct": False,
                "rationale": (
                    "Incorrect. The 'login' command is not ignored. The router will prompt for a password "
                    "and reject all entries when no line password is configured. 'login' must be explicitly "
                    "removed ('no login') to allow unauthenticated access."
                ),
            },
        ],
        "explanation": (
            "Console line authentication modes: 'no login' = no password required (unauthenticated access). "
            "'login' = requires the line-level password (set with 'password <pw>'); if no 'password' is configured, "
            "access is blocked because no password can match. 'login local' = checks the local username database. "
            "The correct fix if a line password is missing: either add 'password <pw>' or switch to 'login local'."
        ),
    },
    # ── cd5v2-016 ── Device access control: privilege levels ─────────────────
    {
        "id": "cd5v2-016",
        "domain": 5,
        "objective": "5.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Device access control (passwords)",
        "stem": (
            "An administrator runs 'username helpdesk privilege 5 secret HelpD3sk'. "
            "IOS has default privilege levels: 1 = user EXEC, 15 = privileged EXEC. "
            "When user 'helpdesk' logs in via SSH and enters the password, what IOS access level is granted "
            "WITHOUT any additional commands?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Privilege level 5 — the user enters a command prompt at level 5 directly, with access only to commands assigned to levels 1–5.",
                "correct": True,
                "rationale": (
                    "Correct. 'username helpdesk privilege 5' causes IOS to place the user directly into "
                    "privilege level 5 upon login without needing to enter 'enable'. "
                    "Commands available are those assigned to levels 1 through 5."
                ),
            },
            {
                "id": "b",
                "text": "Privilege level 1 — all local users start at level 1 and must type 'enable' to elevate.",
                "correct": False,
                "rationale": (
                    "Incorrect. Without a 'privilege' keyword in the username command, users default to level 1. "
                    "However, 'username helpdesk privilege 5' overrides this and directly places the user at level 5."
                ),
            },
            {
                "id": "c",
                "text": "Privilege level 15 — specifying any non-zero privilege grants full admin access.",
                "correct": False,
                "rationale": (
                    "Incorrect. The privilege level is exactly what is specified (5 in this case). "
                    "Level 15 requires explicit assignment or 'enable secret' elevation."
                ),
            },
            {
                "id": "d",
                "text": "Privilege level 5 but the user must still enter 'enable 5' and provide the level-5 password.",
                "correct": False,
                "rationale": (
                    "Incorrect. When 'privilege' is set in the username command, the user is placed directly "
                    "at that level on login — no separate 'enable' command is needed."
                ),
            },
        ],
        "explanation": (
            "IOS privilege levels 0–15: level 1 = default user EXEC; level 15 = full privileged EXEC. "
            "The 'username <name> privilege <level> secret <pw>' command assigns a default privilege level "
            "that takes effect immediately on login — no 'enable' required for that level. "
            "Specific commands can be assigned to custom levels with 'privilege exec level <n> <command>'. "
            "This mechanism supports role-based access without full TACACS+ command authorization."
        ),
    },
    # ── cd5v2-017 ── Wireless security: WPA2-TKIP deprecation ─────────────────
    {
        "id": "cd5v2-017",
        "domain": 5,
        "objective": "5.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Wireless security (WPA2/WPA3)",
        "stem": (
            "A legacy access point supports only WPA2 with TKIP encryption. "
            "A security audit flags this as a critical finding. "
            "Which statement BEST explains why TKIP is considered insecure for WPA2 deployments?"
        ),
        "options": [
            {
                "id": "a",
                "text": "TKIP is based on RC4 with per-packet key mixing. Known weaknesses in RC4 and practical attacks against TKIP (such as the Beck-Tews attack) allow partial decryption and injection of forged frames.",
                "correct": True,
                "rationale": (
                    "Correct. TKIP was a stop-gap improvement over WEP, reusing RC4 but adding per-packet key mixing "
                    "and a message integrity code (Michael MIC). However, attacks like Beck-Tews demonstrated "
                    "practical weaknesses in TKIP/RC4, enabling limited decryption and frame injection. "
                    "Wi-Fi Alliance deprecated TKIP in 2012; WPA2 should use AES-CCMP."
                ),
            },
            {
                "id": "b",
                "text": "TKIP uses a 40-bit static key that can be brute-forced in under an hour with modern hardware.",
                "correct": False,
                "rationale": (
                    "Incorrect. TKIP keys are 128 bits and use per-packet key mixing. The weakness is in the "
                    "RC4 algorithm and the TKIP Michael MIC, not a short static key."
                ),
            },
            {
                "id": "c",
                "text": "TKIP lacks any message integrity check, allowing bit-flipping attacks on plaintext.",
                "correct": False,
                "rationale": (
                    "Incorrect. TKIP includes a Message Integrity Code called Michael MIC. However, Michael MIC "
                    "itself has known weaknesses that the Beck-Tews attack exploits. WEP had no MIC; TKIP does but "
                    "an insufficient one."
                ),
            },
            {
                "id": "d",
                "text": "TKIP requires a certificate authority, which introduces complexity and a single point of failure.",
                "correct": False,
                "rationale": (
                    "Incorrect. TKIP does not require certificates. This description fits 802.1X/EAP-TLS, "
                    "not the TKIP encryption protocol itself."
                ),
            },
        ],
        "explanation": (
            "TKIP was designed as a 'software patch' for WEP hardware, reusing the RC4 cipher with improvements: "
            "128-bit per-packet key mixing, 48-bit IV (vs. 24-bit WEP), and the Michael MIC. "
            "Despite these improvements, RC4 has inherent statistical biases and Michael MIC has an exploitable "
            "weakness. The Beck-Tews attack (2008) showed TKIP frames could be partially decrypted. "
            "The Wi-Fi Alliance deprecated TKIP in 2012. All modern WPA2 and WPA3 deployments must use AES-CCMP."
        ),
    },
    # ── cd5v2-018 ── Wireless security: WPA3-Enterprise 192-bit mode ──────────
    {
        "id": "cd5v2-018",
        "domain": 5,
        "objective": "5.9",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Wireless security (WPA2/WPA3)",
        "stem": (
            "A government agency requires WPA3-Enterprise with 192-bit security mode for its classified network. "
            "Which cipher suite must be used in 192-bit mode, and what mandatory change applies to EAP methods?"
        ),
        "options": [
            {
                "id": "a",
                "text": "AES-GCMP-256 for data encryption; only EAP methods with 192-bit cryptographic strength are permitted (e.g., EAP-TLS with RSA-3072 or ECDSA-384).",
                "correct": True,
                "rationale": (
                    "Correct. WPA3-Enterprise 192-bit mode mandates AES-GCMP-256 for CCMP and requires EAP methods "
                    "that meet the 192-bit security level. EAP-TLS with RSA-3072 or EAP-TLS with ECDSA P-384 "
                    "are compliant. Weaker methods like PEAP-MSCHAPv2 are prohibited."
                ),
            },
            {
                "id": "b",
                "text": "AES-CCMP-128 for data encryption; PEAP-MSCHAPv2 must be replaced with EAP-TLS.",
                "correct": False,
                "rationale": (
                    "Incorrect. 192-bit mode requires AES-GCMP-256, not CCMP-128. CCMP-128 (AES-128) is the "
                    "standard for WPA2 and baseline WPA3-Enterprise."
                ),
            },
            {
                "id": "c",
                "text": "AES-CCMP-256 for data encryption; any 802.1X EAP method is acceptable in 192-bit mode.",
                "correct": False,
                "rationale": (
                    "Incorrect. 192-bit mode uses AES-GCMP-256 (Galois/Counter Mode Protocol), not CCMP-256. "
                    "Additionally, EAP method strength is constrained to 192-bit equivalent — not all EAP methods qualify."
                ),
            },
            {
                "id": "d",
                "text": "SAE (Dragonfly) replaces 802.1X in 192-bit mode for government use cases.",
                "correct": False,
                "rationale": (
                    "Incorrect. SAE is the authentication method for WPA3-Personal. "
                    "WPA3-Enterprise (including the 192-bit mode) continues to use 802.1X/EAP for authentication, "
                    "not SAE."
                ),
            },
        ],
        "explanation": (
            "WPA3-Enterprise 192-bit security mode (based on CNSA Suite for US government) specifies: "
            "AES-GCMP-256 for data encryption, HMAC-SHA-384 for key derivation/integrity, "
            "EAP-TLS with RSA-3072+ or ECDSA P-384 certificates, and ECDH P-384 for key exchange. "
            "Standard WPA3-Enterprise uses AES-CCMP-128. The 192-bit mode is optional and intended for "
            "environments with stringent national security requirements."
        ),
    },
    # ── cd5v2-019 ── IPsec VPNs: IKEv1 vs IKEv2 ──────────────────────────────
    {
        "id": "cd5v2-019",
        "domain": 5,
        "objective": "5.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "IPsec VPNs",
        "stem": (
            "A site-to-site VPN is failing to establish. The engineer suspects a mismatch in IKE Phase 1 parameters. "
            "In IKEv1 Main Mode, which parameters must match on BOTH peers for the ISAKMP SA to form?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Encryption algorithm, hash algorithm, Diffie-Hellman group, authentication method, and SA lifetime.",
                "correct": True,
                "rationale": (
                    "Correct. IKEv1 ISAKMP policy must match on both peers: encryption (e.g., AES-256), "
                    "hash/integrity (e.g., SHA-256), DH group, authentication method (pre-shared key or RSA signatures), "
                    "and SA lifetime. Any mismatch prevents Phase 1 from completing."
                ),
            },
            {
                "id": "b",
                "text": "Encryption algorithm, ACL (crypto map), and pre-shared key only.",
                "correct": False,
                "rationale": (
                    "Incorrect. Phase 1 requires matching the full ISAKMP policy (encryption, hash, DH group, "
                    "auth method, lifetime). The crypto ACL and pre-shared key are critical but incomplete answers. "
                    "The pre-shared key must match but is not negotiated in the ISAKMP policy itself."
                ),
            },
            {
                "id": "c",
                "text": "Transform set (ESP encryption and integrity), PFS group, and ACL.",
                "correct": False,
                "rationale": (
                    "Incorrect. Transform sets, PFS, and crypto ACLs are Phase 2 (IPsec SA) parameters. "
                    "Phase 1 (ISAKMP policy) negotiates encryption, hash, DH group, auth method, and lifetime."
                ),
            },
            {
                "id": "d",
                "text": "Local and remote tunnel endpoint IPs and the crypto map name.",
                "correct": False,
                "rationale": (
                    "Incorrect. Tunnel endpoint IPs must be reachable and correctly referenced, but they are not "
                    "Phase 1 negotiated parameters. The crypto map name is local and does not need to match the peer."
                ),
            },
        ],
        "explanation": (
            "IKEv1 Phase 1 negotiates the ISAKMP SA using these parameters (must match): "
            "1) Encryption algorithm (DES/3DES/AES-128/AES-256), "
            "2) Hash/integrity (MD5/SHA-1/SHA-256), "
            "3) Authentication method (pre-shared key / RSA-sig), "
            "4) Diffie-Hellman group (1/2/5/14/19...), "
            "5) SA lifetime (seconds). "
            "Phase 2 (IPsec SA) negotiates the transform set (ESP/AH, encryption, integrity), PFS group, "
            "and ACL (interesting traffic). Debug with 'debug crypto isakmp' and 'debug crypto ipsec'."
        ),
    },
    # ── cd5v2-020 ── IPsec VPNs: GRE over IPsec vs VTI ───────────────────────
    {
        "id": "cd5v2-020",
        "domain": 5,
        "objective": "5.5",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "IPsec VPNs",
        "stem": (
            "A network engineer must build a site-to-site VPN that also carries OSPF routing protocol updates "
            "between two branches. The engineer considers two options: (A) GRE over IPsec and (B) IPsec VTI. "
            "Which statement correctly differentiates these two approaches?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Both GRE over IPsec and IPsec VTI support dynamic routing protocols. GRE over IPsec requires a separate GRE tunnel interface AND a crypto map; IPsec VTI uses a tunnel interface with 'tunnel mode ipsec ipv4' and does not need a separate crypto map.",
                "correct": True,
                "rationale": (
                    "Correct. GRE/IPsec: GRE encapsulates multicast/routing traffic; IPsec (via crypto map) "
                    "encrypts the GRE packets. Two layers of encapsulation. VTI: 'interface tunnel X' with "
                    "'tunnel mode ipsec ipv4' creates a routable, IPsec-encrypted interface directly, "
                    "without a crypto map. Both support dynamic routing over the tunnel."
                ),
            },
            {
                "id": "b",
                "text": "GRE over IPsec supports dynamic routing protocols; IPsec VTI does not because it uses a crypto ACL that blocks routing protocol multicast.",
                "correct": False,
                "rationale": (
                    "Incorrect. IPsec VTI does support dynamic routing protocols. The VTI interface acts as "
                    "a point-to-point link, and routing protocols (OSPF, EIGRP) run directly over it. "
                    "There is no crypto ACL with VTI; all traffic entering the tunnel interface is encrypted."
                ),
            },
            {
                "id": "c",
                "text": "IPsec VTI requires GRE encapsulation to support multicast; otherwise, routing protocols cannot run over it.",
                "correct": False,
                "rationale": (
                    "Incorrect. IPsec VTI supports multicast natively when configured correctly (e.g., OSPF over VTI). "
                    "GRE is not required for VTI to carry routing protocols."
                ),
            },
            {
                "id": "d",
                "text": "Only GRE over IPsec encrypts the tunnel; IPsec VTI authenticates packets but does not encrypt them.",
                "correct": False,
                "rationale": (
                    "Incorrect. IPsec VTI provides full ESP encryption (confidentiality, integrity, anti-replay). "
                    "Both approaches encrypt traffic; VTI is often simpler to configure and more efficient "
                    "because it avoids the dual-encapsulation overhead of GRE/IPsec."
                ),
            },
        ],
        "explanation": (
            "GRE over IPsec: GRE tunnel (protocol 47) carries multicast + routing protocols; "
            "crypto map encrypts the outer GRE+IP packet with ESP. Two config objects required: tunnel interface + crypto map. "
            "IPsec VTI: single interface with 'tunnel mode ipsec ipv4' (or ipv6). "
            "IPsec profile attached to the tunnel interface. All routed traffic (including OSPF multicast) "
            "is automatically encrypted. VTI is the modern preferred approach for site-to-site VPNs on IOS."
        ),
    },
    # ── cd5v2-021 ── Security concepts: phishing vs spear phishing ────────────
    {
        "id": "cd5v2-021",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security concepts (threats/vulnerabilities)",
        "stem": (
            "An attacker sends emails to every employee at a company, disguised as an IT help-desk "
            "notice about a mandatory password reset, with a link to a fake login portal. "
            "Separately, another attacker researches a specific VP on LinkedIn and sends a "
            "personalized email pretending to be the CEO requesting a wire transfer. "
            "How are these attacks correctly classified?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The mass email is a phishing attack; the targeted VP email is spear phishing (also known as whaling when targeting executives).",
                "correct": True,
                "rationale": (
                    "Correct. Phishing = mass undirected emails. Spear phishing = targeted attack using "
                    "personalized information about the victim. When the target is a high-value executive "
                    "(CEO, CFO, VP), spear phishing is specifically called 'whaling'."
                ),
            },
            {
                "id": "b",
                "text": "Both are phishing attacks; the difference is only in the quality of the fake website.",
                "correct": False,
                "rationale": (
                    "Incorrect. The critical distinction is targeting and personalization. Mass undirected = phishing. "
                    "Targeted with personalized research = spear phishing/whaling. This is not about website quality."
                ),
            },
            {
                "id": "c",
                "text": "The mass email is vishing; the VP email is phishing.",
                "correct": False,
                "rationale": (
                    "Incorrect. Vishing is voice/phone-based social engineering. Both attacks described use email, "
                    "making them phishing variants, not vishing."
                ),
            },
            {
                "id": "d",
                "text": "Both are spear phishing attacks because both impersonate a trusted entity.",
                "correct": False,
                "rationale": (
                    "Incorrect. Impersonating a trusted entity is common to all phishing types. "
                    "The distinguishing factor for spear phishing is targeted personalization using OSINT "
                    "about the specific victim, not present in the mass email campaign."
                ),
            },
        ],
        "explanation": (
            "Phishing taxonomy: Phishing = untargeted mass email with malicious links/attachments. "
            "Spear phishing = targeted at a specific individual or organization using research (LinkedIn, company websites). "
            "Whaling = spear phishing targeting C-level executives. Business Email Compromise (BEC) = "
            "impersonating executives via email for financial fraud (the wire transfer scenario). "
            "Vishing = voice (phone) phishing. Smishing = SMS phishing."
        ),
    },
    # ── cd5v2-022 ── Security concepts: man-in-the-middle ────────────────────
    {
        "id": "cd5v2-022",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security concepts (threats/vulnerabilities)",
        "stem": (
            "An attacker on the same VLAN as two hosts poisons their ARP caches so that both hosts "
            "send traffic through the attacker's machine before it reaches the real destination. "
            "The attacker can read and modify the traffic in transit. "
            "Which attack type and Layer 2 mitigation BEST match this scenario?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Man-in-the-middle via ARP poisoning; mitigated by Dynamic ARP Inspection (DAI) on the switch.",
                "correct": True,
                "rationale": (
                    "Correct. ARP cache poisoning allows an attacker to intercept and modify traffic between two "
                    "hosts (MitM). DAI validates ARP packets against the DHCP snooping binding table, dropping "
                    "forged ARP replies that map IP addresses to the attacker's MAC."
                ),
            },
            {
                "id": "b",
                "text": "Replay attack; mitigated by implementing IPsec with anti-replay protection.",
                "correct": False,
                "rationale": (
                    "Incorrect. A replay attack involves retransmitting previously captured legitimate packets. "
                    "The described attack is ARP poisoning enabling a man-in-the-middle — the attacker intercepts "
                    "live traffic in real time, not replaying old packets."
                ),
            },
            {
                "id": "c",
                "text": "MAC flooding; mitigated by DHCP snooping on the access switch.",
                "correct": False,
                "rationale": (
                    "Incorrect. MAC flooding overwhelms the CAM table to force the switch into hub behavior, "
                    "broadcasting all frames. DHCP snooping prevents rogue DHCP servers. "
                    "Neither matches this ARP poisoning / MitM scenario."
                ),
            },
            {
                "id": "d",
                "text": "IP spoofing; mitigated by unicast reverse path forwarding (uRPF) on the router.",
                "correct": False,
                "rationale": (
                    "Incorrect. IP spoofing involves falsifying source IP addresses in packets. "
                    "ARP poisoning operates at Layer 2 and targets MAC address resolution, not IP source fields. "
                    "uRPF is a router-level control, not effective against Layer 2 ARP attacks."
                ),
            },
        ],
        "explanation": (
            "ARP poisoning MitM: attacker sends gratuitous ARP replies mapping victim IPs to attacker's MAC. "
            "Both victims update their ARP caches and forward traffic through the attacker. "
            "DAI prevents this by checking each ARP reply against the DHCP snooping binding table "
            "(IP-MAC-port-VLAN mapping). Complementary controls: static ARP entries (not scalable), "
            "private VLANs, and end-to-end encryption (TLS) to mitigate data exposure even if MitM succeeds."
        ),
    },
    # ── cd5v2-023 ── Security concepts: zero-day vs known vulnerability ────────
    {
        "id": "cd5v2-023",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security concepts (threats/vulnerabilities)",
        "stem": (
            "A threat intelligence report warns of active exploitation of a recently disclosed "
            "vulnerability for which no vendor patch currently exists. "
            "Which term accurately describes this vulnerability, and what is the BEST immediate mitigation?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Zero-day vulnerability; best immediate mitigation is to apply compensating controls such as IPS signatures, WAF rules, or network segmentation until a patch is released.",
                "correct": True,
                "rationale": (
                    "Correct. A zero-day is a vulnerability that is publicly known (or actively exploited) "
                    "but for which no vendor patch yet exists. Since patching is impossible, compensating controls "
                    "(IPS blocking, WAF, ACL-based network segmentation, disabling the vulnerable feature) "
                    "are the best available mitigations."
                ),
            },
            {
                "id": "b",
                "text": "Known vulnerability (CVE); best mitigation is immediate patching.",
                "correct": False,
                "rationale": (
                    "Incorrect. A known vulnerability with an available patch is not a zero-day. "
                    "The scenario specifies NO vendor patch exists, distinguishing it as a zero-day. "
                    "Patching is not possible when no patch has been released."
                ),
            },
            {
                "id": "c",
                "text": "APT (Advanced Persistent Threat); best mitigation is enhanced endpoint detection and response (EDR).",
                "correct": False,
                "rationale": (
                    "Incorrect. APT describes a threat actor category (nation-state, organized crime) — not a "
                    "specific type of vulnerability. The question describes a vulnerability characteristic (no patch). "
                    "EDR is useful but not the primary immediate mitigation."
                ),
            },
            {
                "id": "d",
                "text": "Logic bomb; best mitigation is code review of all recently deployed scripts.",
                "correct": False,
                "rationale": (
                    "Incorrect. A logic bomb is malicious code triggered by a specific condition embedded by an "
                    "insider. This scenario describes an externally known vulnerability actively exploited by threat actors."
                ),
            },
        ],
        "explanation": (
            "Zero-day timeline: vulnerability discovered (day 0) → actively exploited before vendor is aware "
            "or can issue a patch. Once a patch is available, it is no longer a true zero-day (though unpatched "
            "systems remain at risk). Compensating controls during zero-day windows: "
            "IPS/IDS signatures targeting exploit patterns, WAF rules, disabling vulnerable services, "
            "increasing monitoring, and network micro-segmentation. Apply the vendor patch immediately once available."
        ),
    },
    # ── cd5v2-024 ── Security program elements: data classification ────────────
    {
        "id": "cd5v2-024",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security program elements",
        "stem": (
            "A security team is building a data classification policy. "
            "Which of the following BEST describes the purpose of data classification in a security program?"
        ),
        "options": [
            {
                "id": "a",
                "text": "To assign sensitivity labels to data assets so that appropriate security controls (access restrictions, encryption, retention) can be applied based on the data's value and risk.",
                "correct": True,
                "rationale": (
                    "Correct. Data classification assigns labels (e.g., Public, Internal, Confidential, Restricted/Top Secret) "
                    "that determine which security controls apply. Higher-sensitivity data receives stronger access controls, "
                    "encryption requirements, and handling procedures."
                ),
            },
            {
                "id": "b",
                "text": "To identify which network segments carry the most traffic to prioritize QoS policies.",
                "correct": False,
                "rationale": (
                    "Incorrect. QoS traffic prioritization is a network engineering function, not data classification. "
                    "Data classification focuses on the sensitivity and value of data content, not network traffic volume."
                ),
            },
            {
                "id": "c",
                "text": "To inventory all hardware assets and assign replacement costs for insurance purposes.",
                "correct": False,
                "rationale": (
                    "Incorrect. This describes asset inventory or hardware lifecycle management. "
                    "Data classification applies to data/information assets, not physical hardware."
                ),
            },
            {
                "id": "d",
                "text": "To enforce ACLs that restrict which IP addresses can access the file servers.",
                "correct": False,
                "rationale": (
                    "Incorrect. ACL-based access control is a technical control that may be informed by data classification, "
                    "but it is not the purpose of data classification itself. Classification defines what protection level is needed; "
                    "ACLs are one mechanism to enforce it."
                ),
            },
        ],
        "explanation": (
            "Data classification programs typically use 3–4 sensitivity tiers: "
            "Public → Internal/Private → Confidential → Restricted/Top Secret. "
            "Each tier defines: who can access the data, how it must be stored (encrypted or not), "
            "how it can be transmitted, and retention/destruction requirements. "
            "The classification label drives the selection of appropriate technical and administrative controls. "
            "Without classification, organizations apply uniform (often inadequate) controls to all data."
        ),
    },
    # ── cd5v2-025 ── Security program elements: defense in depth ──────────────
    {
        "id": "cd5v2-025",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security program elements",
        "stem": (
            "A security architect proposes layering firewalls, IDS/IPS, network segmentation, "
            "endpoint antivirus, and user training together. An executive asks why multiple controls are needed "
            "instead of one best-of-breed solution. Which security principle BEST justifies the layered approach?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Defense in depth — multiple overlapping security controls ensure that if one layer is bypassed or fails, additional layers continue to protect the asset.",
                "correct": True,
                "rationale": (
                    "Correct. Defense in depth (layered security) assumes no single control is perfect. "
                    "By stacking controls at different layers (network, host, application, human), "
                    "an attacker who bypasses one layer still faces additional barriers."
                ),
            },
            {
                "id": "b",
                "text": "Principle of least privilege — each device should have only the access it needs, reducing the attack surface.",
                "correct": False,
                "rationale": (
                    "Incorrect. Least privilege governs access rights assigned to users and systems. "
                    "The layered multi-control approach described is defense in depth, not least privilege."
                ),
            },
            {
                "id": "c",
                "text": "Separation of duties — security tasks should be split among multiple teams so no single person can bypass controls.",
                "correct": False,
                "rationale": (
                    "Incorrect. Separation of duties is an administrative control preventing a single individual "
                    "from completing all steps of a sensitive process. The multiple technical layers described "
                    "represent defense in depth, not separation of duties."
                ),
            },
            {
                "id": "d",
                "text": "Non-repudiation — logging on multiple devices ensures an attacker's actions cannot be denied.",
                "correct": False,
                "rationale": (
                    "Incorrect. Non-repudiation ensures that an action cannot be denied by the party who performed it, "
                    "typically through logging and digital signatures. This is only one component of the broader "
                    "defense-in-depth strategy, not the principle that justifies multiple overlapping controls."
                ),
            },
        ],
        "explanation": (
            "Defense in depth (also 'layered security') is a security design principle derived from military strategy. "
            "Key idea: no single control is foolproof. Controls layered at different tiers (perimeter, network, "
            "host, application, data, user) create multiple failure points for an attacker to overcome. "
            "CCNA Security Fundamentals tests this principle alongside least privilege, need-to-know, "
            "separation of duties, and job rotation."
        ),
    },
    # ── cd5v2-026 ── Password policies & MFA: TOTP vs HOTP ───────────────────
    {
        "id": "cd5v2-026",
        "domain": 5,
        "objective": "5.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Password policies & MFA",
        "stem": (
            "An organization deploys a soft-token MFA app that generates a new 6-digit code every 30 seconds "
            "synchronized with the server clock. A second organization uses a hardware token that generates "
            "a new code each time the user presses a button, regardless of time. "
            "Which OTP standards do these represent respectively?"
        ),
        "options": [
            {
                "id": "a",
                "text": "TOTP (Time-Based OTP, RFC 6238) for the 30-second app; HOTP (HMAC-Based OTP, RFC 4226) for the button-press hardware token.",
                "correct": True,
                "rationale": (
                    "Correct. TOTP (RFC 6238) generates OTPs using the current time as the counter, typically refreshing "
                    "every 30 seconds. HOTP (RFC 4226) generates OTPs using an incrementing counter triggered by each "
                    "button press (event-based). Both are 'something you have' MFA factors."
                ),
            },
            {
                "id": "b",
                "text": "HOTP for the 30-second app; TOTP for the button-press hardware token.",
                "correct": False,
                "rationale": (
                    "Incorrect. This is reversed. TOTP = time-synchronized (30-second rolling codes). "
                    "HOTP = event-driven (counter increments per button press). The time-based app is TOTP."
                ),
            },
            {
                "id": "c",
                "text": "Both use TOTP; the hardware token uses a shorter time window (15 seconds) triggered by the button.",
                "correct": False,
                "rationale": (
                    "Incorrect. A button-press hardware token that generates a code per button press is event-based "
                    "(HOTP), not time-based. The button press increments the internal counter, not a timer."
                ),
            },
            {
                "id": "d",
                "text": "S/KEY for the 30-second app; RSA SecurID for the hardware token (both proprietary, no RFC standard).",
                "correct": False,
                "rationale": (
                    "Incorrect. S/KEY is a different OTP scheme (hash chains). RSA SecurID uses TOTP. "
                    "The modern open standards are TOTP (RFC 6238) and HOTP (RFC 4226), both IETF-standardized."
                ),
            },
        ],
        "explanation": (
            "OTP standards: HOTP (RFC 4226) = HMAC-SHA1(secret, counter); counter increments per event (button press). "
            "TOTP (RFC 6238) = HOTP where the counter is derived from current time (floor(Unix_time / 30)). "
            "TOTP codes change every 30 seconds and require clock synchronization (NTP). "
            "HOTP codes are valid until used; counter drift can cause synchronization issues. "
            "Both are widely used: Google Authenticator, Cisco Duo, and Authy implement TOTP."
        ),
    },
    # ── cd5v2-027 ── Password policies & MFA: password complexity ─────────────
    {
        "id": "cd5v2-027",
        "domain": 5,
        "objective": "5.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Password policies & MFA",
        "stem": (
            "A security policy mandates minimum 12-character passwords with complexity. "
            "A Cisco router is configured with:\n\n"
            "security passwords min-length 12\n\n"
            "An administrator attempts to set a 12-character password 'aabbccddee11' for a local user. "
            "Which statement is accurate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "'security passwords min-length' only enforces the minimum length; it does not enforce character complexity (mixed case, symbols). The 12-character password is accepted.",
                "correct": True,
                "rationale": (
                    "Correct. The 'security passwords min-length' command enforces only the minimum length. "
                    "IOS does not natively enforce complexity rules (mixed case, numbers, symbols) with this command alone. "
                    "The password 'aabbccddee11' meets the 12-character minimum and is accepted."
                ),
            },
            {
                "id": "b",
                "text": "The password is rejected because 'security passwords min-length' also requires at least one uppercase letter, one symbol, and one number.",
                "correct": False,
                "rationale": (
                    "Incorrect. 'security passwords min-length' enforces only length, not complexity. "
                    "Complexity enforcement in IOS requires a separate feature or external AAA server policy."
                ),
            },
            {
                "id": "c",
                "text": "The password is rejected because 'aabbccddee11' contains repeated characters, which violates the default Cisco complexity policy.",
                "correct": False,
                "rationale": (
                    "Incorrect. Cisco IOS does not have a built-in repeated-character policy enforced by "
                    "'security passwords min-length'. Repeated character restrictions are typically enforced "
                    "by external AAA servers or application-level password policies."
                ),
            },
            {
                "id": "d",
                "text": "The password is rejected because IOS requires a minimum of 14 characters when 'security passwords min-length 12' is configured.",
                "correct": False,
                "rationale": (
                    "Incorrect. The command sets the minimum to exactly 12 characters. IOS enforces whatever "
                    "length value is specified; there is no hidden override to 14 characters."
                ),
            },
        ],
        "explanation": (
            "'security passwords min-length <n>': global command that prevents any password on the router "
            "(console, VTY, user accounts) from being set shorter than n characters. "
            "It does NOT enforce complexity (uppercase, symbols, digits). "
            "For complexity enforcement in Cisco IOS, use the 'aaa password-complexity' feature available "
            "in some IOS versions, or offload password policy enforcement to a TACACS+/RADIUS server. "
            "NIST SP 800-63B (2017) now recommends length over complexity as the primary password control."
        ),
    },
    # ── cd5v2-028 ── MR: ACLs: two true statements ────────────────────────────
    {
        "id": "cd5v2-028",
        "domain": 5,
        "objective": "5.6",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Access control lists (ACLs)",
        "stem": (
            "Select TWO statements that are TRUE about extended ACLs on Cisco IOS routers."
        ),
        "options": [
            {
                "id": "a",
                "text": "Extended ACLs use numbers in the range 100–199 and 2000–2699.",
                "correct": True,
                "rationale": (
                    "Correct. Extended numbered ACLs use ranges 100–199 (original) and 2000–2699 (expanded). "
                    "Standard ACLs use 1–99 and 1300–1999."
                ),
            },
            {
                "id": "b",
                "text": "Extended ACLs should be placed as close to the SOURCE as possible to minimize unnecessary traffic traversal.",
                "correct": True,
                "rationale": (
                    "Correct. Because extended ACLs can specify both source AND destination (plus protocol/port), "
                    "placing them near the source prevents unwanted traffic from traversing the network before being dropped, "
                    "conserving bandwidth. Standard ACLs (source-only) should be near the destination."
                ),
            },
            {
                "id": "c",
                "text": "Extended ACLs can filter on source IP only and require a separate standard ACL for destination filtering.",
                "correct": False,
                "rationale": (
                    "Incorrect. Extended ACLs natively filter on source IP, destination IP, protocol, and port "
                    "number — all in a single ACE. No separate standard ACL is needed for destination filtering."
                ),
            },
            {
                "id": "d",
                "text": "Extended ACLs do not have an implicit deny; traffic is forwarded by default if no ACE matches.",
                "correct": False,
                "rationale": (
                    "Incorrect. ALL Cisco ACLs — standard and extended — end with an implicit 'deny ip any any'. "
                    "Unmatched traffic is dropped, not forwarded."
                ),
            },
        ],
        "explanation": (
            "Extended ACL key facts: (1) Numbered ranges: 100–199 and 2000–2699. "
            "(2) Match criteria: source IP, destination IP, protocol (IP/TCP/UDP/ICMP...), source port, destination port. "
            "(3) Placement: close to the source to prevent unwanted traffic from traversing the network. "
            "(4) Implicit deny-all at the end — same as standard ACLs. "
            "Named extended ACLs (ip access-list extended NAME) support sequence-number editing."
        ),
    },
    # ── cd5v2-029 ── MR: Port security two true statements ───────────────────
    {
        "id": "cd5v2-029",
        "domain": 5,
        "objective": "5.7",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Port security",
        "stem": (
            "Select TWO statements that are TRUE about port security sticky MAC addresses on Cisco Catalyst switches."
        ),
        "options": [
            {
                "id": "a",
                "text": "Sticky MAC addresses are stored in the running-configuration and can be saved to startup-config with 'copy running-config startup-config'.",
                "correct": True,
                "rationale": (
                    "Correct. Dynamically learned sticky MACs are converted to static entries in the running-config "
                    "under the interface configuration. They persist across reboots only if explicitly saved to startup-config."
                ),
            },
            {
                "id": "b",
                "text": "Sticky MAC addresses are automatically deleted when the switch reboots, requiring re-learning on the next boot.",
                "correct": False,
                "rationale": (
                    "Incorrect. Sticky MACs persist across reboots IF saved to startup-config. "
                    "If not saved, they are lost on reboot. The behavior depends on whether 'write memory' was issued."
                ),
            },
            {
                "id": "c",
                "text": "Enabling sticky MAC learning with 'switchport port-security mac-address sticky' converts any currently dynamically learned secure MACs to sticky entries.",
                "correct": True,
                "rationale": (
                    "Correct. When sticky learning is enabled, any MACs already in the secure MAC table (dynamically learned) "
                    "are immediately converted to sticky (static) entries and written to the running-config."
                ),
            },
            {
                "id": "d",
                "text": "Sticky MAC learning works on both access and trunk interfaces without any additional commands.",
                "correct": False,
                "rationale": (
                    "Incorrect. Port security (including sticky MAC) is supported only on access and voice VLAN ports. "
                    "Port security is NOT supported on trunk ports or dynamic (auto/desirable) mode ports."
                ),
            },
        ],
        "explanation": (
            "Sticky MAC learning behavior: when enabled, dynamically learned MACs become 'sticky' "
            "(appear as 'switchport port-security mac-address sticky <mac>' in running-config). "
            "They are NOT in startup-config until explicitly saved with 'copy running-config startup-config' "
            "or 'write memory'. Without saving, a reboot clears sticky MACs and they must be re-learned. "
            "Port security is supported on access and voice ports only — not trunk or EtherChannel ports."
        ),
    },
    # ── cd5v2-030 ── MR: DHCP snooping two true ──────────────────────────────
    {
        "id": "cd5v2-030",
        "domain": 5,
        "objective": "5.7",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "DHCP snooping & DAI",
        "stem": (
            "Select TWO statements that are TRUE about DHCP snooping on Cisco Catalyst switches."
        ),
        "options": [
            {
                "id": "a",
                "text": "DHCP snooping must be enabled globally AND per-VLAN for it to take effect on any interface.",
                "correct": True,
                "rationale": (
                    "Correct. DHCP snooping requires two commands: 'ip dhcp snooping' (global enable) and "
                    "'ip dhcp snooping vlan <vlan-id>' (per-VLAN enable). Both are required. "
                    "Enabling only one has no effect."
                ),
            },
            {
                "id": "b",
                "text": "All switch ports are untrusted by default when DHCP snooping is enabled; trusted ports must be explicitly configured.",
                "correct": True,
                "rationale": (
                    "Correct. DHCP snooping treats all ports as untrusted by default. Only ports toward legitimate "
                    "DHCP servers or other trusted switches should be marked trusted with 'ip dhcp snooping trust'. "
                    "Access ports facing clients must remain untrusted."
                ),
            },
            {
                "id": "c",
                "text": "DHCP ACK packets from trusted ports are silently dropped because snooping only permits DISCOVER and REQUEST messages.",
                "correct": False,
                "rationale": (
                    "Incorrect. Trusted ports are allowed to forward ALL DHCP message types, including OFFER and ACK. "
                    "Only untrusted ports have server messages (OFFER, ACK, NAK) dropped. "
                    "Trusted ports bypass DHCP snooping filtering."
                ),
            },
            {
                "id": "d",
                "text": "The DHCP snooping binding table is automatically synchronized between all switches in the campus without any additional configuration.",
                "correct": False,
                "rationale": (
                    "Incorrect. The DHCP snooping binding table is local to each switch. There is no automatic "
                    "campus-wide synchronization. DAI on each switch uses its own local binding table."
                ),
            },
        ],
        "explanation": (
            "DHCP snooping configuration checklist: "
            "(1) 'ip dhcp snooping' — global enable. "
            "(2) 'ip dhcp snooping vlan <x>' — enable per VLAN. "
            "(3) 'ip dhcp snooping trust' on uplinks to DHCP servers/distribution switches. "
            "(4) Optionally: 'ip dhcp snooping limit rate <pps>' to rate-limit DHCP on access ports. "
            "The binding table ({MAC, IP, VLAN, interface}) is populated from DHCP ACKs on trusted ports "
            "and is used by DAI for ARP validation."
        ),
    },
    # ── cd5v2-031 ── MR: AAA two true ─────────────────────────────────────────
    {
        "id": "cd5v2-031",
        "domain": 5,
        "objective": "5.8",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "AAA (RADIUS vs TACACS+)",
        "stem": (
            "Select TWO statements that are TRUE about configuring AAA with 'aaa new-model' on a Cisco IOS router."
        ),
        "options": [
            {
                "id": "a",
                "text": "Entering 'aaa new-model' immediately enables AAA and overrides the existing 'login' command on VTY lines — the router may use the default AAA authentication list for all lines.",
                "correct": True,
                "rationale": (
                    "Correct. 'aaa new-model' activates AAA globally and immediately applies the default AAA "
                    "authentication method list ('default') to all lines including console and VTY. "
                    "If the default list requires TACACS+ and the server is unreachable with no local fallback, "
                    "the router can be locked out. Always configure fallback before enabling aaa new-model."
                ),
            },
            {
                "id": "b",
                "text": "The 'aaa authentication login' method list named 'default' automatically applies to all lines unless a specific named list is explicitly applied to those lines.",
                "correct": True,
                "rationale": (
                    "Correct. The 'default' AAA method list applies to all lines that do not have a specific "
                    "named method list applied. Custom method lists (e.g., 'aaa authentication login CONSOLEAUTH') "
                    "must be explicitly applied under the relevant line configuration."
                ),
            },
            {
                "id": "c",
                "text": "'aaa new-model' can be entered and removed at any time without affecting live VTY sessions.",
                "correct": False,
                "rationale": (
                    "Incorrect. Enabling or disabling 'aaa new-model' has immediate effect on authentication "
                    "behavior. Removing it while relying on AAA for authentication can lock administrators out. "
                    "Always plan AAA changes carefully, preferably via the console."
                ),
            },
            {
                "id": "d",
                "text": "RADIUS and TACACS+ server groups cannot be mixed in the same 'aaa authentication login' method list.",
                "correct": False,
                "rationale": (
                    "Incorrect. A single method list can reference multiple server groups and fallback methods: "
                    "'aaa authentication login default group radius group tacacs+ local' is valid and tries "
                    "each method in order."
                ),
            },
        ],
        "explanation": (
            "'aaa new-model' enables Cisco's AAA framework. Key behaviors: "
            "(1) The 'default' method list applies to all unassigned lines automatically. "
            "(2) Named method lists override 'default' only on lines where they are explicitly applied. "
            "(3) Enabling AAA while connected remotely without a fallback (local) can cause lockout. "
            "Best practice: configure local fallback first, then apply AAA to VTY, then test before configuring console. "
            "Multiple server groups and fallback methods can coexist in one method list."
        ),
    },
    # ── cd5v2-032 ── Wildcard mask: host and any keywords ─────────────────────
    {
        "id": "cd5v2-032",
        "domain": 5,
        "objective": "5.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "ACL placement & wildcard masks",
        "stem": (
            "An ACL contains:\n\n"
            "access-list 101 deny tcp host 10.1.1.1 any eq 22\n"
            "access-list 101 permit ip any any\n\n"
            "Host 10.1.1.1 attempts to open an SSH connection (TCP port 22) to 172.16.0.5. "
            "Host 10.1.1.2 attempts SSH to the same destination. "
            "Host 10.1.1.1 attempts HTTP (port 80) to 172.16.0.5. "
            "Which traffic is permitted?"
        ),
        "options": [
            {
                "id": "a",
                "text": "SSH from 10.1.1.2 and HTTP from 10.1.1.1 are permitted; SSH from 10.1.1.1 is denied.",
                "correct": True,
                "rationale": (
                    "Correct. ACE 1 denies TCP port 22 only from source 'host 10.1.1.1' (0.0.0.0 wildcard). "
                    "10.1.1.2 does not match 'host 10.1.1.1', so it falls through to ACE 2 (permit ip any any) and is allowed. "
                    "10.1.1.1 HTTP (port 80) does not match the 'eq 22' condition in ACE 1, so it is also permitted by ACE 2."
                ),
            },
            {
                "id": "b",
                "text": "All three are denied because ACE 1 denies all TCP from any source to port 22.",
                "correct": False,
                "rationale": (
                    "Incorrect. ACE 1 specifies 'host 10.1.1.1' (single host only). 10.1.1.2 is a different host "
                    "and is not matched. ACE 1 also specifies 'eq 22' — HTTP (port 80) from 10.1.1.1 does not match."
                ),
            },
            {
                "id": "c",
                "text": "All three are permitted because ACE 2 'permit ip any any' overrides ACE 1.",
                "correct": False,
                "rationale": (
                    "Incorrect. ACLs are processed top-down and stop at the first match. "
                    "SSH from 10.1.1.1 matches ACE 1 first and is denied before reaching ACE 2."
                ),
            },
            {
                "id": "d",
                "text": "SSH from 10.1.1.1 and 10.1.1.2 are denied; HTTP from 10.1.1.1 is permitted.",
                "correct": False,
                "rationale": (
                    "Incorrect. ACE 1 targets only 'host 10.1.1.1'. 10.1.1.2 is not matched by ACE 1 "
                    "and is permitted by ACE 2. Only SSH from 10.1.1.1 is denied."
                ),
            },
        ],
        "explanation": (
            "The 'host' keyword in an ACL is equivalent to a 0.0.0.0 wildcard — matches exactly one IP. "
            "'any' is equivalent to 0.0.0.0 255.255.255.255 — matches all IPs. "
            "'eq 22' matches only TCP destination port 22 (SSH). "
            "Three independent evaluations: "
            "(1) 10.1.1.1 SSH: matches ACE 1 → DENY. "
            "(2) 10.1.1.2 SSH: misses ACE 1 (wrong host), hits ACE 2 → PERMIT. "
            "(3) 10.1.1.1 HTTP: misses ACE 1 (wrong port), hits ACE 2 → PERMIT."
        ),
    },
    # ── cd5v2-033 ── Security program elements: incident response ─────────────
    {
        "id": "cd5v2-033",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security program elements",
        "stem": (
            "A SOC analyst confirms that ransomware is actively encrypting files on a workstation connected "
            "to the corporate LAN. Per the incident response plan, what is the FIRST action the analyst "
            "should take to limit the blast radius?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Isolate (contain) the infected workstation by removing it from the network — disconnect the switch port or disable the port via CLI — to prevent lateral spread.",
                "correct": True,
                "rationale": (
                    "Correct. Containment is the first active step after detection and verification in the NIST "
                    "incident response lifecycle (Prepare → Detect/Analyze → Contain → Eradicate → Recover). "
                    "Isolating the host prevents ransomware from spreading to network shares or other endpoints."
                ),
            },
            {
                "id": "b",
                "text": "Immediately reimage the workstation to remove the ransomware and restore normal operations.",
                "correct": False,
                "rationale": (
                    "Incorrect. Reimaging (eradication/recovery) comes after containment and evidence collection. "
                    "Immediate reimaging before containment allows the ransomware to potentially spread, "
                    "and destroys forensic evidence needed to understand the attack vector."
                ),
            },
            {
                "id": "c",
                "text": "Pay the ransom to minimize downtime and recover the encryption keys.",
                "correct": False,
                "rationale": (
                    "Incorrect. Paying the ransom is a last-resort business decision — never a first technical response step. "
                    "It funds criminal activity, does not guarantee key delivery, and does not remove the malware."
                ),
            },
            {
                "id": "d",
                "text": "Run a full antivirus scan on the workstation to identify and quarantine the ransomware before taking any network action.",
                "correct": False,
                "rationale": (
                    "Incorrect. Running a scan while the workstation remains connected allows continued spreading "
                    "to network shares. Network isolation (containment) must come before local remediation actions "
                    "to limit the blast radius."
                ),
            },
        ],
        "explanation": (
            "NIST SP 800-61 Incident Response phases: (1) Preparation, (2) Detection and Analysis, "
            "(3) Containment → Eradication → Recovery, (4) Post-Incident Activity. "
            "For active ransomware: Contain first (network isolation), then collect forensic evidence "
            "(memory dump, disk image if possible), then eradicate (reimage/restore from backup), "
            "then recover (bring back to production). Contain before eradicate to prevent spread and preserve evidence."
        ),
    },
    # ── cd5v2-034 ── IPsec VPNs: AH incompatible with NAT ────────────────────
    {
        "id": "cd5v2-034",
        "domain": 5,
        "objective": "5.5",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "IPsec VPNs",
        "stem": (
            "A remote worker's IPsec VPN uses AH (Authentication Header) in transport mode. "
            "The worker is behind a home router performing NAT. The VPN fails to establish connectivity. "
            "Which explanation BEST describes why AH is incompatible with NAT, and what should be used instead?"
        ),
        "options": [
            {
                "id": "a",
                "text": "AH covers the outer IP header in its integrity hash (including the source IP). NAT changes the source IP, invalidating the AH integrity check. ESP should be used instead, with NAT-T (UDP port 4500) to encapsulate ESP within UDP.",
                "correct": True,
                "rationale": (
                    "Correct. AH (protocol 51) computes its HMAC over the outer IP header. When NAT modifies the "
                    "source IP address, the receiving peer recomputes the HMAC and finds a mismatch — the AH integrity "
                    "check fails and the packet is dropped. ESP (protocol 50) does not include the outer IP header "
                    "in its integrity computation. NAT-T encapsulates ESP in UDP 4500 for NAT traversal."
                ),
            },
            {
                "id": "b",
                "text": "AH does not support encryption, so NAT devices cannot decode the payload to perform address translation.",
                "correct": False,
                "rationale": (
                    "Incorrect. NAT does not need to decrypt the payload — it only modifies IP headers. "
                    "The failure is because AH includes the outer IP header in its integrity check, "
                    "and NAT's modification of the IP invalidates the hash. Lack of encryption is a separate issue."
                ),
            },
            {
                "id": "c",
                "text": "NAT changes the destination port, causing AH to fail its transport-layer integrity check.",
                "correct": False,
                "rationale": (
                    "Incorrect. Basic NAT (not PAT) changes IP addresses. AH fails because the SOURCE IP is changed, "
                    "not because of port changes. Even with static NAT changing only the IP, AH would fail."
                ),
            },
            {
                "id": "d",
                "text": "AH uses UDP, which is stateful and requires symmetric routing; NAT breaks symmetric routing.",
                "correct": False,
                "rationale": (
                    "Incorrect. AH is a network-layer protocol (IP protocol number 51), not UDP. "
                    "The NAT incompatibility is specifically due to AH's inclusion of the outer IP header in its HMAC, "
                    "not routing asymmetry."
                ),
            },
        ],
        "explanation": (
            "AH (Authentication Header, protocol 51) provides integrity and authentication. Its HMAC covers "
            "the immutable fields of the outer IP header (including source IP). "
            "NAT rewrites the source IP → AH HMAC mismatch → packet dropped. "
            "ESP (Encapsulating Security Payload, protocol 50) does NOT include the outer IP header in its HMAC, "
            "so NAT address changes do not break ESP integrity. "
            "NAT-T (NAT Traversal, RFC 3947): both peers detect NAT in IKE, then encapsulate ESP in UDP port 4500 "
            "to traverse NAT devices. IKE itself moves from UDP 500 to UDP 4500 when NAT is detected."
        ),
    },
]

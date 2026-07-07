# CCNA 200-301 Performance-Based Questions (PBQs)
# 16 questions across 6 domains
# Types: pbq_matching (6), pbq_categorize (5), pbq_ordering (5)

QUESTIONS = [
    # ─── pbq_matching ──────────────────────────────────────────────────────────

    {
        "id": "cpbq-001",
        "domain": 3,
        "objective": "3.2",
        "type": "pbq_matching",
        "difficulty": "hard",
        "study_topic": "Administrative distance",
        "stem": (
            "A router receives updates for the same prefix from multiple sources. "
            "Match each routing source to its Cisco default administrative distance."
        ),
        "prompts": [
            {"id": "p1", "text": "Directly connected interface"},
            {"id": "p2", "text": "Static route (via next-hop or exit interface)"},
            {"id": "p3", "text": "EIGRP (internal)"},
            {"id": "p4", "text": "OSPF"},
            {"id": "p5", "text": "RIP"},
            {"id": "p6", "text": "EIGRP (external)"},
        ],
        "targets": [
            {"id": "t1", "text": "0"},
            {"id": "t2", "text": "1"},
            {"id": "t3", "text": "90"},
            {"id": "t4", "text": "110"},
            {"id": "t5", "text": "120"},
            {"id": "t6", "text": "170"},
            {"id": "t7", "text": "200"},  # distractor: iBGP
        ],
        "answer": {
            "p1": "t1",
            "p2": "t2",
            "p3": "t3",
            "p4": "t4",
            "p5": "t5",
            "p6": "t6",
        },
        "rationales": {
            "p1": "Directly connected routes carry AD 0 — the router trusts its own interfaces above all else.",
            "p2": "Static routes default to AD 1, just above connected, making them highly preferred.",
            "p3": "Internal EIGRP has AD 90. External EIGRP is 170 — a common exam distractor.",
            "p4": "OSPF has AD 110, higher than EIGRP internal but lower than RIP.",
            "p5": "RIP has AD 120, reflecting its age and hop-count-only metric.",
            "p6": "External EIGRP (redistributed routes) carries AD 170, far less trusted than internal EIGRP.",
        },
        "explanation": (
            "Default Cisco ADs: Connected 0, Static 1, eBGP 20, EIGRP internal 90, OSPF 110, "
            "IS-IS 115, RIP 120, EIGRP external 170, iBGP 200. The router installs only the "
            "lowest-AD route for a given prefix in the RIB. '200' (iBGP) is the distractor here."
        ),
    },

    {
        "id": "cpbq-002",
        "domain": 1,
        "objective": "1.1",
        "type": "pbq_matching",
        "difficulty": "hard",
        "study_topic": "OSI model layers, PDUs, and representative protocols",
        "stem": (
            "Match each protocol or device to its PRIMARY OSI layer of operation."
        ),
        "prompts": [
            {"id": "p1", "text": "IP (Internet Protocol)"},
            {"id": "p2", "text": "IEEE 802.3 Ethernet framing"},
            {"id": "p3", "text": "TCP segment"},
            {"id": "p4", "text": "TLS/SSL encryption"},
            {"id": "p5", "text": "HTTP"},
            {"id": "p6", "text": "Hub (repeater)"},
        ],
        "targets": [
            {"id": "t1", "text": "Layer 1 – Physical"},
            {"id": "t2", "text": "Layer 2 – Data Link"},
            {"id": "t3", "text": "Layer 3 – Network"},
            {"id": "t4", "text": "Layer 4 – Transport"},
            {"id": "t5", "text": "Layer 5 – Session"},
            {"id": "t6", "text": "Layer 6 – Presentation"},
            {"id": "t7", "text": "Layer 7 – Application"},
        ],
        "answer": {
            "p1": "t3",
            "p2": "t2",
            "p3": "t4",
            "p4": "t6",
            "p5": "t7",
            "p6": "t1",
        },
        "rationales": {
            "p1": "IP operates at Layer 3 (Network), providing logical addressing and routing.",
            "p2": "IEEE 802.3 defines the Ethernet frame format — Layer 2 (Data Link), specifically the MAC sublayer.",
            "p3": "TCP segments are the PDU at Layer 4 (Transport), providing reliable, ordered delivery.",
            "p4": "TLS performs encryption/decryption and data formatting — Layer 6 (Presentation).",
            "p5": "HTTP is an application-layer protocol — Layer 7.",
            "p6": "A hub simply repeats electrical signals with no frame awareness — Layer 1 (Physical).",
        },
        "explanation": (
            "OSI PDUs by layer: bits (L1), frames (L2), packets (L3), segments (L4). "
            "Switches operate at L2, routers at L3, and multilayer switches span L2-L3. "
            "TLS is the classic L6 example; exam questions sometimes try to place it at L4 or L7."
        ),
    },

    {
        "id": "cpbq-003",
        "domain": 1,
        "objective": "1.5",
        "type": "pbq_matching",
        "difficulty": "hard",
        "study_topic": "TCP/UDP well-known port numbers",
        "stem": (
            "A network engineer is writing ACL permit statements. "
            "Match each application protocol to its correct well-known destination port number."
        ),
        "prompts": [
            {"id": "p1", "text": "SSH"},
            {"id": "p2", "text": "DNS"},
            {"id": "p3", "text": "HTTPS"},
            {"id": "p4", "text": "SNMP (agent polling)"},
            {"id": "p5", "text": "NTP"},
            {"id": "p6", "text": "Syslog"},
        ],
        "targets": [
            {"id": "t1", "text": "22/TCP"},
            {"id": "t2", "text": "23/TCP"},       # distractor: Telnet
            {"id": "t3", "text": "53/UDP (and TCP)"},
            {"id": "t4", "text": "123/UDP"},
            {"id": "t5", "text": "161/UDP"},
            {"id": "t6", "text": "443/TCP"},
            {"id": "t7", "text": "514/UDP"},
        ],
        "answer": {
            "p1": "t1",
            "p2": "t3",
            "p3": "t6",
            "p4": "t5",
            "p5": "t4",
            "p6": "t7",
        },
        "rationales": {
            "p1": "SSH uses TCP port 22; it replaced Telnet (port 23) as the secure management protocol.",
            "p2": "DNS uses port 53, primarily UDP for queries but TCP for zone transfers and large responses.",
            "p3": "HTTPS (HTTP over TLS) uses TCP port 443.",
            "p4": "SNMP agent listens on UDP port 161; the manager sends GET/SET requests to this port.",
            "p5": "NTP uses UDP port 123 to synchronize clocks between client and server.",
            "p6": "Syslog traditionally uses UDP port 514 to send log messages to a syslog server.",
        },
        "explanation": (
            "Key ports to memorize: SSH 22, Telnet 23, SMTP 25, DNS 53, DHCP 67/68, HTTP 80, "
            "HTTPS 443, SNMP 161/162, Syslog 514 UDP, TFTP 69 UDP, NTP 123 UDP. "
            "Port 23 (Telnet) is the classic distractor against SSH (22)."
        ),
    },

    {
        "id": "cpbq-004",
        "domain": 2,
        "objective": "2.4",
        "type": "pbq_matching",
        "difficulty": "hard",
        "study_topic": "Spanning Tree Protocol terminology",
        "stem": (
            "A network engineer is troubleshooting STP in a switched network. "
            "Match each STP term to its correct definition."
        ),
        "prompts": [
            {"id": "p1", "text": "Root Bridge"},
            {"id": "p2", "text": "Root Port"},
            {"id": "p3", "text": "Designated Port"},
            {"id": "p4", "text": "Non-Designated (Blocked) Port"},
            {"id": "p5", "text": "BPDU Guard"},
        ],
        "targets": [
            {"id": "t1", "text": "The switch with the lowest Bridge ID elected to be the STP focal point for the topology."},
            {"id": "t2", "text": "The port on a non-root switch that provides the best (lowest cost) path toward the root bridge."},
            {"id": "t3", "text": "The port on each network segment that forwards traffic toward the root bridge on that segment."},
            {"id": "t4", "text": "A port placed in Blocking state to prevent loops; does not forward data frames."},
            {"id": "t5", "text": "A PortFast feature that err-disables a port if a BPDU is received, preventing rogue switches."},
            {"id": "t6", "text": "A feature that prevents STP topology changes from aging out the CAM table prematurely."},  # distractor: TCN guard
        ],
        "answer": {
            "p1": "t1",
            "p2": "t2",
            "p3": "t3",
            "p4": "t4",
            "p5": "t5",
        },
        "rationales": {
            "p1": "The Root Bridge is the switch with the lowest Bridge ID (priority + MAC); all other switches calculate paths relative to it.",
            "p2": "Each non-root switch has exactly one Root Port — the port with the lowest cumulative path cost to the root.",
            "p3": "A Designated Port is the forwarding port on each LAN segment; the root bridge has all ports designated.",
            "p4": "Non-designated ports are in Blocking state; they receive BPDUs but discard all data frames to break loops.",
            "p5": "BPDU Guard immediately err-disables PortFast-enabled ports upon BPDU receipt, protecting against unauthorized switches.",
        },
        "explanation": (
            "STP port roles: Root Port (best path to root), Designated Port (best port per segment), "
            "Alternate/Backup (RSTP). BPDU Guard is enabled on PortFast ports (access ports toward end hosts). "
            "The distractor t6 describes TCN (Topology Change Notification) dampening, not BPDU Guard."
        ),
    },

    {
        "id": "cpbq-005",
        "domain": 3,
        "objective": "3.5",
        "type": "pbq_matching",
        "difficulty": "hard",
        "study_topic": "First Hop Redundancy Protocols (HSRP, VRRP, GLBP)",
        "stem": (
            "A network engineer is comparing FHRP implementations. "
            "Match each FHRP term or feature to its correct description."
        ),
        "prompts": [
            {"id": "p1", "text": "HSRP Active router"},
            {"id": "p2", "text": "HSRP virtual MAC address format"},
            {"id": "p3", "text": "VRRP Master router"},
            {"id": "p4", "text": "GLBP AVG"},
            {"id": "p5", "text": "GLBP load-balancing advantage"},
        ],
        "targets": [
            {"id": "t1", "text": "The router currently forwarding traffic for the virtual IP; elected by highest priority (default 100), then highest real IP."},
            {"id": "t2", "text": "0000.0c07.acXX — where XX is the HSRP group number in hex."},
            {"id": "t3", "text": "The router owning the virtual IP in VRRP; elected by highest priority (default 100); can be the IP owner (priority 255)."},
            {"id": "t4", "text": "Active Virtual Gateway — assigns virtual MACs to AVFs and responds to ARP for the virtual IP."},
            {"id": "t5", "text": "Multiple AVFs can simultaneously forward traffic, providing true per-host load balancing — unlike HSRP/VRRP."},
            {"id": "t6", "text": "0000.5e00.01XX — used by VRRP groups."},  # distractor
        ],
        "answer": {
            "p1": "t1",
            "p2": "t2",
            "p3": "t3",
            "p4": "t4",
            "p5": "t5",
        },
        "rationales": {
            "p1": "HSRP Active router handles all traffic for the virtual IP; elected via priority then real IP tiebreak.",
            "p2": "HSRP virtual MAC is 0000.0c07.acXX (group in hex); e.g., group 1 = 0000.0c07.ac01.",
            "p3": "VRRP Master owns the virtual IP; if a router IS the IP owner its priority auto-sets to 255.",
            "p4": "GLBP AVG manages the group, distributes virtual MACs (0007.b400.XXYY) to AVFs for load sharing.",
            "p5": "GLBP allows multiple Active Virtual Forwarders (AVFs), so different hosts use different next-hops — true load balancing.",
        },
        "explanation": (
            "HSRP (Cisco proprietary) uses Active/Standby; VRRP (RFC 5798) uses Master/Backup and allows real-IP owner "
            "as master; GLBP (Cisco proprietary) adds load balancing via multiple AVFs. "
            "VRRP virtual MAC: 0000.5e00.01XX. HSRP virtual MAC: 0000.0c07.acXX."
        ),
    },

    {
        "id": "cpbq-006",
        "domain": 5,
        "objective": "5.6",
        "type": "pbq_matching",
        "difficulty": "hard",
        "study_topic": "Standard vs Extended ACL — number ranges and matching criteria",
        "stem": (
            "An engineer must apply ACLs to a router running IOS. "
            "Match each ACL characteristic to its correct ACL type."
        ),
        "prompts": [
            {"id": "p1", "text": "Numbered ACL range 1–99 and 1300–1999"},
            {"id": "p2", "text": "Numbered ACL range 100–199 and 2000–2699"},
            {"id": "p3", "text": "Filters only on source IP address"},
            {"id": "p4", "text": "Can match source IP, destination IP, protocol, and port number"},
            {"id": "p5", "text": "Should be placed as close to the DESTINATION as possible"},
            {"id": "p6", "text": "Should be placed as close to the SOURCE as possible"},
        ],
        "targets": [
            {"id": "t1", "text": "Standard ACL"},
            {"id": "t2", "text": "Extended ACL"},
        ],
        "answer": {
            "p1": "t1",
            "p2": "t2",
            "p3": "t1",
            "p4": "t2",
            "p5": "t1",
            "p6": "t2",
        },
        "rationales": {
            "p1": "Standard IP ACLs use numbers 1–99 (classic) and 1300–1999 (expanded range).",
            "p2": "Extended IP ACLs use numbers 100–199 (classic) and 2000–2699 (expanded range).",
            "p3": "Standard ACLs match on source IP only — they have no destination or protocol fields.",
            "p4": "Extended ACLs can match source/destination IP, L4 protocol (TCP/UDP/ICMP), and port numbers.",
            "p5": "Because standard ACLs only match source IP (no destination granularity), place them near the destination to avoid accidentally blocking traffic to other destinations.",
            "p6": "Extended ACLs match both source and destination, so place them near the source to drop traffic early and save bandwidth.",
        },
        "explanation": (
            "Standard ACL = source IP only, placed near destination. "
            "Extended ACL = src+dst IP + protocol + ports, placed near source. "
            "Named ACLs can be standard or extended. Wildcard masks are the inverse of subnet masks."
        ),
    },

    # ─── pbq_categorize ────────────────────────────────────────────────────────

    {
        "id": "cpbq-007",
        "domain": 1,
        "objective": "1.9",
        "type": "pbq_categorize",
        "difficulty": "hard",
        "study_topic": "IPv6 address type classification",
        "stem": (
            "Classify each IPv6 address by its type based on its prefix."
        ),
        "categories": [
            {"id": "c1", "text": "Global unicast (2000::/3)"},
            {"id": "c2", "text": "Link-local (fe80::/10)"},
            {"id": "c3", "text": "Unique local (fc00::/7)"},
            {"id": "c4", "text": "Multicast (ff00::/8)"},
            {"id": "c5", "text": "Loopback / Unspecified"},
        ],
        "items": [
            {"id": "i1", "text": "2001:db8:1:1::10/64"},
            {"id": "i2", "text": "fe80::c001:1ff:fe00:0"},
            {"id": "i3", "text": "fd12:3456:789a::1/48"},
            {"id": "i4", "text": "ff02::2"},
            {"id": "i5", "text": "::1"},
            {"id": "i6", "text": "2600:1901:0:bbc1::"},
        ],
        "answer": {
            "i1": "c1",
            "i2": "c2",
            "i3": "c3",
            "i4": "c4",
            "i5": "c5",
            "i6": "c1",
        },
        "rationales": {
            "i1": "2001:db8::/32 is within 2000::/3 (global unicast). It is the documentation prefix (RFC 3849) but categorically global unicast.",
            "i2": "fe80:: falls within fe80::/10 (link-local). EUI-64-derived addresses use this prefix and are auto-configured.",
            "i3": "fd12:: falls within fd00::/8, a subset of fc00::/7 (unique local). The 'fd' prefix indicates locally assigned unique local.",
            "i4": "ff02::2 is the all-routers multicast address on the local link; ff00::/8 denotes multicast.",
            "i5": "::1 is the IPv6 loopback address (equivalent to 127.0.0.1 in IPv4); :: (all zeros) is the unspecified address.",
            "i6": "2600:: is within 2000::/3 — a ARIN-assigned global unicast prefix used by Google.",
        },
        "explanation": (
            "IPv6 type prefixes: Global unicast 2000::/3, Link-local fe80::/10, "
            "Unique local fc00::/7 (fc=centrally assigned [reserved], fd=locally assigned), "
            "Multicast ff00::/8, Loopback ::1, Unspecified ::. "
            "There is no broadcast in IPv6; ff02::1 (all-nodes) and ff02::2 (all-routers) replace broadcast functions."
        ),
    },

    {
        "id": "cpbq-008",
        "domain": 4,
        "objective": "4.8",
        "type": "pbq_categorize",
        "difficulty": "hard",
        "study_topic": "Syslog severity levels",
        "stem": (
            "A NOC engineer reviews syslog messages. "
            "Classify each syslog keyword/description into its correct severity level number."
        ),
        "categories": [
            {"id": "c1", "text": "Severity 0 – Emergency"},
            {"id": "c2", "text": "Severity 2 – Critical"},
            {"id": "c3", "text": "Severity 3 – Error"},
            {"id": "c4", "text": "Severity 5 – Notice"},
            {"id": "c5", "text": "Severity 6 – Informational"},
            {"id": "c6", "text": "Severity 7 – Debugging"},
        ],
        "items": [
            {"id": "i1", "text": "System is unusable; hardware failure causing full outage"},
            {"id": "i2", "text": "Critical conditions: core dump, severe resource exhaustion"},
            {"id": "i3", "text": "Error conditions: interface down, route flap error"},
            {"id": "i4", "text": "Normal but significant: interface status changes logged to console"},
            {"id": "i5", "text": "Informational: ACL hit counters, OSPF neighbor formed"},
            {"id": "i6", "text": "Debug-level: detailed packet trace output from 'debug ip packet'"},
        ],
        "answer": {
            "i1": "c1",
            "i2": "c2",
            "i3": "c3",
            "i4": "c4",
            "i5": "c5",
            "i6": "c6",
        },
        "rationales": {
            "i1": "Severity 0 (Emergency): system unusable — the most severe level.",
            "i2": "Severity 2 (Critical): critical conditions such as core dumps or severe resource exhaustion. Severity 1 (Alert) requires immediate action.",
            "i3": "Severity 3 (Error): error conditions such as interface state changes to down or routing errors.",
            "i4": "Severity 5 (Notice): normal but significant conditions. Interface up/down state changes often log at this level by default on IOS.",
            "i5": "Severity 6 (Informational): general operational messages such as OSPF adjacency formation.",
            "i6": "Severity 7 (Debugging): the most verbose level, generated only when debug commands are active.",
        },
        "explanation": (
            "Syslog severity 0–7: 0=Emergency, 1=Alert, 2=Critical, 3=Error, 4=Warning, "
            "5=Notice, 6=Informational, 7=Debugging. Lower number = higher severity. "
            "Cisco IOS default console logging level is Debugging (7); default buffer logging is Debugging; "
            "'logging trap' sets the level sent to a syslog server. "
            "Mnemonic: Every Awful Cisco Engineer Will Notice Interesting Details."
        ),
    },

    {
        "id": "cpbq-009",
        "domain": 5,
        "objective": "5.9",
        "type": "pbq_categorize",
        "difficulty": "hard",
        "study_topic": "WPA2 vs WPA3 wireless security features",
        "stem": (
            "A wireless engineer is comparing WPA2 and WPA3 security capabilities. "
            "Classify each feature or characteristic under the correct Wi-Fi security standard."
        ),
        "categories": [
            {"id": "c1", "text": "WPA2 only"},
            {"id": "c2", "text": "WPA3 only"},
            {"id": "c3", "text": "Both WPA2 and WPA3"},
        ],
        "items": [
            {"id": "i1", "text": "Uses CCMP (AES-128) as the mandatory encryption cipher"},
            {"id": "i2", "text": "Simultaneous Authentication of Equals (SAE) replaces the 4-way handshake PSK exchange"},
            {"id": "i3", "text": "Vulnerable to offline dictionary attacks if the 4-way handshake is captured"},
            {"id": "i4", "text": "Provides forward secrecy via SAE, protecting past sessions if the key is later compromised"},
            {"id": "i5", "text": "Supports 802.1X / EAP enterprise authentication mode"},
            {"id": "i6", "text": "OWE (Opportunistic Wireless Encryption) for open networks"},
        ],
        "answer": {
            "i1": "c3",
            "i2": "c2",
            "i3": "c1",
            "i4": "c2",
            "i5": "c3",
            "i6": "c2",
        },
        "rationales": {
            "i1": "Both WPA2 and WPA3 mandate AES-based CCMP (128-bit) as the minimum cipher; WPA3-Enterprise adds GCMP-256 in 192-bit mode.",
            "i2": "SAE (Simultaneous Authentication of Equals, aka Dragonfly handshake) is introduced in WPA3-Personal, replacing WPA2's PSK 4-way handshake.",
            "i3": "WPA2-Personal is susceptible to offline dictionary/brute-force attacks because a captured 4-way handshake can be tested against password guesses without network contact.",
            "i4": "SAE in WPA3 provides perfect forward secrecy (PFS) — each session uses a unique PMK derived via Diffie-Hellman, so compromising one key does not expose past sessions.",
            "i5": "Both WPA2-Enterprise and WPA3-Enterprise support 802.1X/EAP for RADIUS-based authentication.",
            "i6": "OWE is a WPA3 feature that encrypts open/public Wi-Fi traffic without requiring a shared passphrase.",
        },
        "explanation": (
            "WPA3 improvements over WPA2: SAE handshake (resists offline attacks + forward secrecy), "
            "OWE for open networks, 192-bit security mode for enterprise, and Management Frame Protection (MFP) mandatory. "
            "WPA2 and WPA3 both use 802.1X/EAP for enterprise and AES-CCMP as baseline cipher."
        ),
    },

    {
        "id": "cpbq-010",
        "domain": 6,
        "objective": "6.3",
        "type": "pbq_categorize",
        "difficulty": "hard",
        "study_topic": "REST API HTTP methods mapped to CRUD operations",
        "stem": (
            "A network automation engineer is writing scripts against a REST API. "
            "Classify each HTTP method under its corresponding CRUD operation."
        ),
        "categories": [
            {"id": "c1", "text": "Create"},
            {"id": "c2", "text": "Read"},
            {"id": "c3", "text": "Update"},
            {"id": "c4", "text": "Delete"},
        ],
        "items": [
            {"id": "i1", "text": "GET"},
            {"id": "i2", "text": "POST"},
            {"id": "i3", "text": "PUT"},
            {"id": "i4", "text": "DELETE"},
            {"id": "i5", "text": "PATCH"},
        ],
        "answer": {
            "i1": "c2",
            "i2": "c1",
            "i3": "c3",
            "i4": "c4",
            "i5": "c3",
        },
        "rationales": {
            "i1": "GET retrieves a resource (or list of resources) without modifying server state — pure Read.",
            "i2": "POST creates a new resource; the server assigns the resource identifier.",
            "i3": "PUT replaces (full update) an existing resource at a specified URI — Update.",
            "i4": "DELETE removes the specified resource — Delete.",
            "i5": "PATCH applies a partial update to an existing resource — a subset of Update (alongside PUT).",
        },
        "explanation": (
            "REST CRUD mapping: GET=Read, POST=Create, PUT=full Update (replace), PATCH=partial Update, DELETE=Delete. "
            "PUT is idempotent (same request yields same result); POST is not. "
            "Cisco DNA Center, NSO, and Meraki APIs all follow REST conventions. "
            "HTTP status codes: 200 OK, 201 Created, 204 No Content, 400 Bad Request, 401 Unauthorized, 404 Not Found."
        ),
    },

    {
        "id": "cpbq-011",
        "domain": 6,
        "objective": "6.6",
        "type": "pbq_categorize",
        "difficulty": "hard",
        "study_topic": "JSON data types",
        "stem": (
            "An engineer is parsing a JSON payload from a network controller REST API. "
            "Classify each JSON value by its correct JSON data type."
        ),
        "categories": [
            {"id": "c1", "text": "String"},
            {"id": "c2", "text": "Number"},
            {"id": "c3", "text": "Boolean"},
            {"id": "c4", "text": "Array"},
            {"id": "c5", "text": "Object"},
            {"id": "c6", "text": "Null"},
        ],
        "items": [
            {"id": "i1", "text": '"GigabitEthernet0/1"'},
            {"id": "i2", "text": "1500"},
            {"id": "i3", "text": "true"},
            {"id": "i4", "text": '["10.0.0.1", "10.0.0.2", "10.0.0.3"]'},
            {"id": "i5", "text": '{"interface": "Gi0/1", "mtu": 1500}'},
            {"id": "i6", "text": "null"},
        ],
        "answer": {
            "i1": "c1",
            "i2": "c2",
            "i3": "c3",
            "i4": "c4",
            "i5": "c5",
            "i6": "c6",
        },
        "rationales": {
            "i1": 'A value enclosed in double quotes is a JSON String (e.g., "GigabitEthernet0/1").',
            "i2": "A bare numeric literal (integer or float, no quotes) is a JSON Number (e.g., 1500).",
            "i3": "JSON Boolean values are the lowercase literals true or false.",
            "i4": "A comma-separated list inside square brackets [] is a JSON Array (ordered collection).",
            "i5": "A set of key/value pairs inside curly braces {} is a JSON Object (unordered map).",
            "i6": "The literal null represents an absent or unknown value in JSON.",
        },
        "explanation": (
            "JSON defines six types: String (double-quoted), Number (integer or float), "
            "Boolean (true/false lowercase), Array ([]), Object ({}), and null. "
            "JSON keys must always be strings. Unlike Python, JSON booleans are lowercase (true/false not True/False). "
            "REST APIs return structured JSON; understanding types is essential for parsing with Python or Ansible."
        ),
    },

    # ─── pbq_ordering ──────────────────────────────────────────────────────────

    {
        "id": "cpbq-012",
        "domain": 2,
        "objective": "2.4",
        "type": "pbq_ordering",
        "difficulty": "hard",
        "study_topic": "802.1D Spanning Tree port state transitions",
        "stem": (
            "A switch port connected to another switch is activated. "
            "Arrange the 802.1D STP port states in the order the port transitions through them, from first to last."
        ),
        "items": [
            {"id": "i1", "text": "Blocking"},
            {"id": "i2", "text": "Listening"},
            {"id": "i3", "text": "Learning"},
            {"id": "i4", "text": "Forwarding"},
        ],
        "answer": ["i1", "i2", "i3", "i4"],
        "rationales": {
            "i1": "Blocking (20 s max wait): receives BPDUs, no data forwarding, no MAC learning. Prevents loops immediately on port activation.",
            "i2": "Listening (15 s Forward Delay): participates in STP election (sends/receives BPDUs), still no MAC learning or data forwarding.",
            "i3": "Learning (15 s Forward Delay): builds the MAC address table from incoming frames but still does not forward data.",
            "i4": "Forwarding: fully operational — sends and receives data frames, continues MAC learning and BPDU processing.",
        },
        "explanation": (
            "802.1D classic STP port states in order: Blocking → Listening → Learning → Forwarding. "
            "Total convergence time ≈ 50 s (20 s max age + 15 s listening + 15 s learning). "
            "Disabled is an administrative state (not part of normal transition). "
            "RSTP (802.1w) collapses Blocking+Listening into Discarding and converges in <1 s via Proposal/Agreement."
        ),
    },

    {
        "id": "cpbq-013",
        "domain": 3,
        "objective": "3.4",
        "type": "pbq_ordering",
        "difficulty": "hard",
        "study_topic": "OSPF neighbor state machine",
        "stem": (
            "Two OSPF routers connected via a point-to-point serial link are forming an adjacency from scratch. "
            "Arrange the OSPF neighbor states in the correct order from initial to fully converged."
        ),
        "items": [
            {"id": "i1", "text": "Down"},
            {"id": "i2", "text": "Init"},
            {"id": "i3", "text": "2-Way"},
            {"id": "i4", "text": "Exstart"},
            {"id": "i5", "text": "Exchange"},
            {"id": "i6", "text": "Loading"},
            {"id": "i7", "text": "Full"},
        ],
        "answer": ["i1", "i2", "i3", "i4", "i5", "i6", "i7"],
        "rationales": {
            "i1": "Down: no Hello packets received from the neighbor; initial state or Hello timer expired.",
            "i2": "Init: a Hello has been received from the neighbor, but the local router's RID is NOT yet listed in that Hello (one-way communication).",
            "i3": "2-Way: each router sees its own RID in the neighbor's Hello (bidirectional communication). DR/BDR election occurs here on multi-access networks.",
            "i4": "Exstart: master/slave relationship is negotiated using DBD packets; higher RID becomes master and initializes sequence numbers.",
            "i5": "Exchange: routers exchange DBD (Database Descriptor) summaries of their LSDBs.",
            "i6": "Loading: LSR (Link State Request) and LSU (Link State Update) packets exchange full LSA details for entries flagged as missing or stale.",
            "i7": "Full: LSDBs are synchronized; the adjacency is complete and SPF can be run.",
        },
        "explanation": (
            "OSPF neighbor states: Down → Attempt (NBMA only) → Init → 2-Way → Exstart → Exchange → Loading → Full. "
            "On point-to-point links, adjacency reaches Full for all neighbors. "
            "On broadcast/NBMA, non-DR/BDR routers stop at 2-Way with each other but reach Full with DR and BDR. "
            "Stuck in Exstart/Exchange usually indicates MTU mismatch."
        ),
    },

    {
        "id": "cpbq-014",
        "domain": 4,
        "objective": "4.3",
        "type": "pbq_ordering",
        "difficulty": "hard",
        "study_topic": "DHCP DORA message sequence",
        "stem": (
            "A client PC connected to a switch boots and needs to obtain an IP address via DHCP. "
            "Arrange the four DHCP messages in the correct order they are exchanged between the client and server."
        ),
        "items": [
            {"id": "i1", "text": "DHCP Discover (client → broadcast)"},
            {"id": "i2", "text": "DHCP Offer (server → client)"},
            {"id": "i3", "text": "DHCP Request (client → broadcast)"},
            {"id": "i4", "text": "DHCP Acknowledge (server → client)"},
        ],
        "answer": ["i1", "i2", "i3", "i4"],
        "rationales": {
            "i1": "Discover: the client broadcasts a DHCPDISCOVER (src 0.0.0.0, dst 255.255.255.255) to locate available DHCP servers.",
            "i2": "Offer: each DHCP server responds with a DHCPOFFER containing an available IP address, subnet mask, gateway, and lease time.",
            "i3": "Request: the client broadcasts a DHCPREQUEST selecting one offer (broadcast so other servers know their offer was declined) and asking for formal assignment.",
            "i4": "Acknowledge: the chosen server responds with a DHCPACK confirming the lease. If the address is no longer available, it sends a DHCPNAK.",
        },
        "explanation": (
            "DHCP DORA: Discover → Offer → Request → Acknowledge. "
            "All four messages travel over UDP (client port 68, server port 67). "
            "Discover and Request are broadcasts (dst 255.255.255.255) so they are forwarded by ip helper-address when the server is on a different subnet. "
            "DHCPNAK causes the client to restart the process; DHCPRELEASE frees the lease early."
        ),
    },

    {
        "id": "cpbq-015",
        "domain": 5,
        "objective": "5.3",
        "type": "pbq_ordering",
        "difficulty": "hard",
        "study_topic": "SSH configuration steps on a Cisco IOS router",
        "stem": (
            "An engineer must configure SSHv2 on a Cisco IOS router that currently has no hostname, "
            "no domain name, and no RSA keys. Arrange the configuration steps in the correct order, first to last."
        ),
        "items": [
            {"id": "i1", "text": "hostname R1"},
            {"id": "i2", "text": "ip domain-name example.com"},
            {"id": "i3", "text": "crypto key generate rsa modulus 2048"},
            {"id": "i4", "text": "ip ssh version 2"},
            {"id": "i5", "text": "username admin privilege 15 secret Cisco123!"},
            {"id": "i6", "text": "line vty 0 4 → login local → transport input ssh"},
        ],
        "answer": ["i1", "i2", "i3", "i4", "i5", "i6"],
        "rationales": {
            "i1": "A unique hostname must be set first; it is embedded in the RSA key label (hostname.domainname).",
            "i2": "The IP domain name is required before generating RSA keys; it forms the second part of the key label.",
            "i3": "RSA keys can only be generated after hostname and domain-name are configured. Modulus 2048 bits meets SSHv2 requirements (minimum 768 bits).",
            "i4": "'ip ssh version 2' is set after the RSA keys exist; IOS will refuse the command without keys.",
            "i5": "A local username/password must be created before configuring the vty lines to use local authentication.",
            "i6": "'login local' references the local user database and 'transport input ssh' disables Telnet access on vty lines.",
        },
        "explanation": (
            "SSH prerequisite chain: hostname → domain-name → RSA key (hostname+domain used in key label) → "
            "ip ssh version 2 → local user → vty login local + transport input ssh. "
            "Without a hostname and domain-name, 'crypto key generate rsa' fails. "
            "Use 'show ip ssh' to verify SSH is enabled and the version. "
            "Best practice: modulus ≥ 2048 bits; disable Telnet with 'transport input ssh' only."
        ),
    },

    {
        "id": "cpbq-016",
        "domain": 6,
        "objective": "6.1",
        "type": "pbq_ordering",
        "difficulty": "hard",
        "study_topic": "Network automation and controller-based architecture concepts",
        "stem": (
            "A network engineer is troubleshooting a Python script that uses the Cisco DNA Center REST API "
            "to push a new VLAN to a switch. Arrange the REST API interaction steps in the correct logical order."
        ),
        "items": [
            {"id": "i1", "text": "Send POST /dna/system/api/v1/auth/token with Base64-encoded credentials to obtain an auth token"},
            {"id": "i2", "text": "Include the token in the 'X-Auth-Token' header of subsequent API requests"},
            {"id": "i3", "text": "Send GET /dna/intent/api/v1/network-device to retrieve the device ID for the target switch"},
            {"id": "i4", "text": "Send POST /dna/intent/api/v1/template-programmer/template/deploy (or CLI template endpoint) with the VLAN config payload and device ID"},
            {"id": "i5", "text": "Poll GET /dna/intent/api/v1/task/{taskId} until status is 'SUCCESS' or 'FAILURE'"},
            {"id": "i6", "text": "Verify the VLAN appears on the switch using GET /dna/intent/api/v1/interface or a show command via the Command Runner API"},
        ],
        "answer": ["i1", "i2", "i3", "i4", "i5", "i6"],
        "rationales": {
            "i1": "Authentication is always first: obtain a session token by POSTing credentials to the auth endpoint.",
            "i2": "All subsequent DNA Center API calls require the token in the X-Auth-Token HTTP header for authorization.",
            "i3": "Before targeting a device, retrieve its unique device ID from the inventory API.",
            "i4": "Deploy the configuration change (VLAN addition) to the identified device using the appropriate template or CLI endpoint.",
            "i5": "DNA Center returns a taskId for asynchronous operations; poll the task endpoint until the task completes to detect errors.",
            "i6": "After success, validate the change was applied correctly by querying interface/VLAN state via the API or Command Runner.",
        },
        "explanation": (
            "Cisco DNA Center REST API flow: Authenticate (get token) → Use token in X-Auth-Token header → "
            "Query inventory for device IDs → Push config change → Poll async task → Verify. "
            "DNA Center uses role-based access (RBAC) and all API calls use HTTPS to the controller. "
            "This reflects the controller-based (SDN) model where the controller (DNA Center) is the northbound API "
            "and manages the underlay devices via southbound protocols (NETCONF/RESTCONF/CLI)."
        ),
    },
]

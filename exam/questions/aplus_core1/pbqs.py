"""
CompTIA A+ Core 1 (220-1201) — Performance-Based Questions (PBQs)
14 PBQs across all 5 domains: 5 pbq_matching, 5 pbq_categorize, 4 pbq_ordering
"""

QUESTIONS = [
    # ─────────────────────────────────────────────────────────────────────────
    # PBQ 1 — pbq_matching | Domain 2 | Networking
    # ─────────────────────────────────────────────────────────────────────────
    {
        "id": "apbq-001",
        "domain": 2,
        "objective": "2.1",
        "type": "pbq_matching",
        "difficulty": "hard",
        "study_topic": "Ports & protocols",
        "stem": (
            "A network technician is auditing firewall rules. "
            "Match each protocol or service to its correct default port number. "
            "Six ports are listed — one is a distractor."
        ),
        "prompts": [
            {"id": "p1", "text": "SMTP (unencrypted mail submission)"},
            {"id": "p2", "text": "IMAP (unencrypted mailbox access)"},
            {"id": "p3", "text": "SNMP (network device monitoring)"},
            {"id": "p4", "text": "RDP (Remote Desktop Protocol)"},
            {"id": "p5", "text": "LDAP (directory services, unencrypted)"},
        ],
        "targets": [
            {"id": "t1", "text": "25"},
            {"id": "t2", "text": "143"},
            {"id": "t3", "text": "161"},
            {"id": "t4", "text": "3389"},
            {"id": "t5", "text": "389"},
            {"id": "t6", "text": "110"},  # distractor — POP3, not used by any prompt
        ],
        "answer": {"p1": "t1", "p2": "t2", "p3": "t3", "p4": "t4", "p5": "t5"},
        "rationales": {
            "p1": "SMTP uses TCP 25 for server-to-server mail transfer (unencrypted). Port 587 is used for authenticated client submission; 465 for SMTPS.",
            "p2": "IMAP uses TCP 143 for unencrypted mailbox access. The common trap is confusing it with POP3 (TCP 110), which downloads and typically deletes mail from the server.",
            "p3": "SNMP uses UDP 161 for polling/monitoring network devices (agents listen on 161; managers receive traps on 162). The UDP transport is frequently tested.",
            "p4": "RDP uses TCP 3389 (and UDP 3389 for enhanced multimedia). Confusing it with VNC (TCP 5900) or Telnet (TCP 23) is a common mistake.",
            "p5": "LDAP uses TCP/UDP 389 for unencrypted directory queries. LDAPS (encrypted) uses TCP 636. Confusing 389 with 3389 (RDP) is a classic distractor.",
        },
        "explanation": (
            "Key port map: SMTP 25, IMAP 143, SNMP 161 (UDP), RDP 3389, LDAP 389. "
            "Port 110 (POP3) is the distractor — it is email retrieval like IMAP but uses a "
            "different port and protocol behavior. Memorize the full table: "
            "FTP 20/21, SSH 22, Telnet 23, SMTP 25, DNS 53, HTTP 80, POP3 110, IMAP 143, "
            "HTTPS 443, SMB 445, LDAP 389, RDP 3389, SNMP 161/162."
        ),
    },

    # ─────────────────────────────────────────────────────────────────────────
    # PBQ 2 — pbq_matching | Domain 3 | Hardware
    # ─────────────────────────────────────────────────────────────────────────
    {
        "id": "apbq-002",
        "domain": 3,
        "objective": "3.4",
        "type": "pbq_matching",
        "difficulty": "hard",
        "study_topic": "RAID levels — characteristics and fault tolerance",
        "stem": (
            "A storage administrator must choose RAID configurations for several use cases. "
            "Match each RAID level to the statement that best describes its minimum drive count "
            "and fault-tolerance behavior. One description is a distractor."
        ),
        "prompts": [
            {"id": "p1", "text": "RAID 0"},
            {"id": "p2", "text": "RAID 1"},
            {"id": "p3", "text": "RAID 5"},
            {"id": "p4", "text": "RAID 10 (1+0)"},
        ],
        "targets": [
            {"id": "t1", "text": "2 drives minimum; zero fault tolerance; full capacity used; maximum read/write performance"},
            {"id": "t2", "text": "2 drives minimum; tolerates 1 drive failure; 50% usable capacity; exact mirror copy"},
            {"id": "t3", "text": "3 drives minimum; tolerates 1 drive failure; distributed parity; one drive's worth of capacity lost"},
            {"id": "t4", "text": "4 drives minimum; tolerates 1 drive failure per mirrored pair; stripe of mirrors; highest rebuild performance"},
            {"id": "t5", "text": "6 drives minimum; tolerates 2 simultaneous drive failures; double distributed parity"},  # distractor — RAID 6
        ],
        "answer": {"p1": "t1", "p2": "t2", "p3": "t3", "p4": "t4"},
        "rationales": {
            "p1": "RAID 0 (striping) requires only 2 drives, provides no redundancy whatsoever — a single drive failure destroys all data — but delivers maximum throughput by writing stripes across all members.",
            "p2": "RAID 1 (mirroring) requires exactly 2 drives and creates an identical copy. Usable capacity is 50%. It tolerates the failure of one drive and rebuilds quickly because only one mirror partner is needed.",
            "p3": "RAID 5 (striping with distributed parity) requires a minimum of 3 drives and can survive exactly one drive failure. Parity is spread across all drives so no single drive is the parity bottleneck. One drive's capacity is consumed by parity.",
            "p4": "RAID 10 requires at least 4 drives (two mirrored pairs, striped). It can survive one failure per mirrored pair (potentially two failures total if they are in different pairs) and rebuilds faster than RAID 5 because it mirrors rather than reconstructing parity.",
        },
        "explanation": (
            "RAID confusion points: RAID 5 minimum is 3 drives (not 4); RAID 10 minimum is 4 drives (not 3). "
            "RAID 5 can lose only 1 drive; RAID 6 (the distractor, t5) loses 2. "
            "RAID 10 write performance is better than RAID 5 because there is no parity calculation overhead. "
            "Capacity formula: RAID 0 = all drives; RAID 1 = N/2; RAID 5 = (N-1) drives; RAID 10 = N/2 drives."
        ),
    },

    # ─────────────────────────────────────────────────────────────────────────
    # PBQ 3 — pbq_matching | Domain 3 | Hardware
    # ─────────────────────────────────────────────────────────────────────────
    {
        "id": "apbq-003",
        "domain": 3,
        "objective": "3.1",
        "type": "pbq_matching",
        "difficulty": "hard",
        "study_topic": "Video & display connectors",
        "stem": (
            "A technician is connecting monitors to workstations. "
            "Match each display interface to the capability statement that best distinguishes it. "
            "One statement is a distractor."
        ),
        "prompts": [
            {"id": "p1", "text": "VGA (DE-15)"},
            {"id": "p2", "text": "DVI-D (single link)"},
            {"id": "p3", "text": "HDMI 2.0"},
            {"id": "p4", "text": "DisplayPort 1.4"},
            {"id": "p5", "text": "Thunderbolt 3"},
        ],
        "targets": [
            {"id": "t1", "text": "Analog-only; maximum practical resolution ~2048×1536; no audio support; uses 15-pin D-sub connector"},
            {"id": "t2", "text": "Digital video only (no audio); maximum 1920×1200 at 60 Hz on a single-link connection; 24+1 or 18+1 pin connector"},
            {"id": "t3", "text": "Carries video and audio; supports up to 4K at 60 Hz (18 Gbps bandwidth); common on consumer TVs and monitors"},
            {"id": "t4", "text": "Supports 8K at 60 Hz or 4K at 120 Hz; HBR3 mode provides 32.4 Gbps; natively supports daisy-chaining monitors via MST"},
            {"id": "t5", "text": "Uses USB-C form factor; up to 40 Gbps data + 100 W power delivery + video; backward compatible with USB 3.1 and DisplayPort"},
            {"id": "t6", "text": "Wireless display standard; uses Wi-Fi Direct for peer-to-peer streaming; no physical connector required"},  # distractor — Miracast
        ],
        "answer": {"p1": "t1", "p2": "t2", "p3": "t3", "p4": "t4", "p5": "t5"},
        "rationales": {
            "p1": "VGA is strictly analog, carries no audio, and tops out around 2048×1536 in practice. Its 15-pin D-sub (DE-15) connector is the oldest of these interfaces and cannot carry digital signals.",
            "p2": "DVI-D single-link is digital-only and caps at 1920×1200 @ 60 Hz (about 4.95 Gbps). It carries no audio. DVI-I adds analog pins; dual-link DVI supports up to 2560×1600.",
            "p3": "HDMI 2.0 has 18 Gbps bandwidth, supports 4K @ 60 Hz, and carries multi-channel audio. It is the dominant consumer AV connector. HDMI 2.1 raises the ceiling to 48 Gbps and 10K.",
            "p4": "DisplayPort 1.4 operates in HBR3 mode (32.4 Gbps), enabling 8K @ 60 Hz or 4K @ 120 Hz. Multi-Stream Transport (MST) allows daisy-chaining multiple monitors from one port.",
            "p5": "Thunderbolt 3 uses the USB-C physical connector and combines 40 Gbps data, DisplayPort 1.2 video, and USB 3.1 Gen 2 over a single cable. It also delivers up to 100 W of power delivery.",
        },
        "explanation": (
            "Key traps: DVI-D carries no audio (HDMI does); DisplayPort supports MST daisy-chaining (HDMI does not natively); "
            "Thunderbolt 3 looks identical to USB-C but runs at 40 Gbps vs USB-C's 10–20 Gbps. "
            "VGA is analog — it cannot be used natively with digital panels without a conversion chip. "
            "The distractor (t6) describes Miracast, a wireless standard, not a physical interface."
        ),
    },

    # ─────────────────────────────────────────────────────────────────────────
    # PBQ 4 — pbq_matching | Domain 2 | Networking
    # ─────────────────────────────────────────────────────────────────────────
    {
        "id": "apbq-004",
        "domain": 2,
        "objective": "2.2",
        "type": "pbq_matching",
        "difficulty": "hard",
        "study_topic": "Network CLI diagnostic tools",
        "stem": (
            "A help-desk technician is troubleshooting connectivity. "
            "Match each command-line tool to the specific task it is best suited for. "
            "One task description is a distractor."
        ),
        "prompts": [
            {"id": "p1", "text": "ipconfig /all  (Windows)"},
            {"id": "p2", "text": "tracert  (Windows)"},
            {"id": "p3", "text": "nslookup"},
            {"id": "p4", "text": "netstat -an"},
            {"id": "p5", "text": "net use"},
        ],
        "targets": [
            {"id": "t1", "text": "Display the host's IP address, subnet mask, default gateway, MAC address, and DHCP/DNS server assignments"},
            {"id": "t2", "text": "Trace the route packets take to a destination, showing each hop's IP and round-trip time to isolate where latency or loss occurs"},
            {"id": "t3", "text": "Query DNS to resolve a hostname to an IP address or look up MX/NS records, helping diagnose name-resolution failures"},
            {"id": "t4", "text": "Display all active TCP/UDP connections and listening ports with their numeric addresses, helping identify rogue listeners or connection state"},
            {"id": "t5", "text": "Map or disconnect a network share (UNC path) to a drive letter from the command line"},
            {"id": "t6", "text": "Capture and decode live packet data from a network interface for deep protocol analysis"},  # distractor — Wireshark/tcpdump
        ],
        "answer": {"p1": "t1", "p2": "t2", "p3": "t3", "p4": "t4", "p5": "t5"},
        "rationales": {
            "p1": "ipconfig /all reveals all network adapter details including IPv4/IPv6 addresses, subnet mask, default gateway, DHCP server, DNS servers, lease dates, and physical (MAC) address — essential first step in most connectivity troubleshooting.",
            "p2": "tracert (traceroute on Linux/macOS) sends ICMP echo requests with incrementing TTL values and records each router hop. It pinpoints the router where packets are dropped or latency spikes.",
            "p3": "nslookup queries the configured DNS server interactively or in batch mode. It can resolve forward/reverse lookups and query specific record types (A, MX, NS, CNAME), making it invaluable for DNS failure diagnosis.",
            "p4": "netstat -an (all connections, numeric) shows every active TCP connection and every port in LISTENING state. The -b flag (Windows) reveals which process owns each socket, helping detect unauthorized services.",
            "p5": "net use \\\\server\\share /persistent:yes maps network shares to drive letters, and net use * /delete disconnects all mapped drives. It is the command-line equivalent of 'Map Network Drive' in Explorer.",
        },
        "explanation": (
            "The distractor (t6) describes Wireshark or tcpdump — packet capture tools not in the standard A+ CLI toolkit. "
            "Key distinctions: ipconfig shows local configuration; ping tests reachability; tracert shows the path; "
            "nslookup tests DNS; netstat shows socket state; net use manages mapped drives. "
            "On Linux, ip addr / ip route replace ipconfig; traceroute replaces tracert; ss replaces netstat."
        ),
    },

    # ─────────────────────────────────────────────────────────────────────────
    # PBQ 5 — pbq_matching | Domain 2 | Networking
    # ─────────────────────────────────────────────────────────────────────────
    {
        "id": "apbq-005",
        "domain": 2,
        "objective": "2.2",
        "type": "pbq_matching",
        "difficulty": "hard",
        "study_topic": "Network devices and their OSI-layer functions",
        "stem": (
            "Match each network device or component to the statement that most accurately "
            "describes its primary function. One statement is a distractor."
        ),
        "prompts": [
            {"id": "p1", "text": "Managed Layer 2 switch"},
            {"id": "p2", "text": "Wireless access point (WAP)"},
            {"id": "p3", "text": "PoE injector"},
            {"id": "p4", "text": "Patch panel"},
            {"id": "p5", "text": "SOHO router / gateway"},
        ],
        "targets": [
            {"id": "t1", "text": "Forwards frames between ports using a MAC address table; supports VLANs, STP, and port mirroring for traffic segmentation and loop prevention"},
            {"id": "t2", "text": "Bridges wireless clients to a wired LAN segment; operates at Layer 2 using CSMA/CA; does not route between subnets by itself"},
            {"id": "t3", "text": "Adds DC power to an Ethernet cable midspan so that a non-PoE switch can power IP cameras, phones, or APs without replacing the switch"},
            {"id": "t4", "text": "Passive termination point that organizes structured cabling runs to a single rack location; no signal processing occurs here"},
            {"id": "t5", "text": "Combines a router, NAT gateway, DHCP server, DNS forwarder, and often a wireless AP into one device for small-office use"},
            {"id": "t6", "text": "Replicates every packet on one port to another port for passive monitoring without disrupting live traffic; operates transparently at Layer 1"},  # distractor — network tap
        ],
        "answer": {"p1": "t1", "p2": "t2", "p3": "t3", "p4": "t4", "p5": "t5"},
        "rationales": {
            "p1": "A managed Layer 2 switch makes forwarding decisions based on MAC addresses (Layer 2). Managed features include VLAN tagging (802.1Q), Spanning Tree Protocol (STP/RSTP) for loop prevention, and port mirroring for monitoring.",
            "p2": "A WAP extends the wired LAN wirelessly, acting as a Layer 2 bridge. It uses CSMA/CA (not CSMA/CD used by Ethernet) to manage the shared wireless medium. It does not perform IP routing.",
            "p3": "A PoE injector adds IEEE 802.3af/at/bt power midspan between a non-PoE switch port and a PoE device. This avoids replacing the switch simply to power a single IP phone or camera.",
            "p4": "A patch panel is a passive 110-punchdown/RJ-45 termination block. It organizes horizontal runs into a rack but performs no switching, routing, or signal amplification.",
            "p5": "A SOHO gateway integrates multiple functions: Layer 3 routing with NAT (sharing one public IP), DHCP server, DNS forwarder, stateful firewall, and often a Wi-Fi AP and 4-port switch.",
        },
        "explanation": (
            "The distractor (t6) describes a network tap or a switch's SPAN/mirror port — not any of the five listed devices. "
            "Key exam traps: a WAP is Layer 2 (not a router); a patch panel is completely passive; "
            "a PoE injector does not switch or route — it only injects power. "
            "A managed switch differs from an unmanaged switch by supporting VLANs and STP."
        ),
    },

    # ─────────────────────────────────────────────────────────────────────────
    # PBQ 6 — pbq_categorize | Domain 4 | Virtualization & Cloud
    # ─────────────────────────────────────────────────────────────────────────
    {
        "id": "apbq-006",
        "domain": 4,
        "objective": "4.1",
        "type": "pbq_categorize",
        "difficulty": "hard",
        "study_topic": "Cloud service models — IaaS / PaaS / SaaS",
        "stem": (
            "A solutions architect is documenting six cloud workloads. "
            "Drag each workload into the correct cloud service model bucket."
        ),
        "categories": [
            {"id": "c1", "text": "IaaS"},
            {"id": "c2", "text": "PaaS"},
            {"id": "c3", "text": "SaaS"},
        ],
        "items": [
            {"id": "i1", "text": "Provisioning raw virtual machines on AWS EC2, then manually installing and patching the OS and middleware"},
            {"id": "i2", "text": "Deploying a web application to Google App Engine without managing any servers or OS updates"},
            {"id": "i3", "text": "Using Microsoft 365 Word Online exclusively in a browser — no local installation"},
            {"id": "i4", "text": "Connecting to Azure SQL Managed Instance where Microsoft handles the database engine, backups, and HA"},
            {"id": "i5", "text": "Renting an Azure Virtual Network with subnets and configuring your own firewall rules and routing tables"},
            {"id": "i6", "text": "Accessing Salesforce CRM through a web portal to manage customer records"},
        ],
        "answer": {"i1": "c1", "i2": "c2", "i3": "c3", "i4": "c2", "i5": "c1", "i6": "c3"},
        "rationales": {
            "i1": "Provisioning raw VMs and managing the OS yourself is the defining characteristic of IaaS. The cloud provider only supplies compute, storage, and networking hardware.",
            "i2": "Google App Engine is a PaaS — you push code and the platform handles OS, runtime, scaling, and patching. You control only your application and its data.",
            "i3": "Microsoft 365 is SaaS. The application is fully managed by Microsoft and consumed via browser; the end user controls only their data/content.",
            "i4": "Azure SQL Managed Instance is PaaS. Microsoft manages the database engine, OS patches, backups, and high availability. You control only the schemas, users, and queries.",
            "i5": "Configuring a Virtual Network with subnets and routing is IaaS. You are managing networking infrastructure; the provider supplies the virtualized hardware fabric.",
            "i6": "Salesforce is a classic SaaS application — a complete, hosted CRM consumed over the internet with no infrastructure or platform responsibility on the customer.",
        },
        "explanation": (
            "The responsibility model: IaaS (you manage OS up); PaaS (you manage app + data); SaaS (you manage only data/content). "
            "The trickiest items are managed database services — they are PaaS, not IaaS, because the database engine is provider-managed. "
            "Virtual networks (i5) remain IaaS because you are still configuring network-layer infrastructure."
        ),
    },

    # ─────────────────────────────────────────────────────────────────────────
    # PBQ 7 — pbq_categorize | Domain 2 | Networking
    # ─────────────────────────────────────────────────────────────────────────
    {
        "id": "apbq-007",
        "domain": 2,
        "objective": "2.1",
        "type": "pbq_categorize",
        "difficulty": "hard",
        "study_topic": "TCP vs UDP — transport protocol classification",
        "stem": (
            "For each service or protocol, categorize whether it primarily uses TCP, UDP, or both "
            "(in cases where it uses both transports depending on the operation)."
        ),
        "categories": [
            {"id": "c1", "text": "TCP only"},
            {"id": "c2", "text": "UDP only"},
            {"id": "c3", "text": "Both TCP and UDP"},
        ],
        "items": [
            {"id": "i1", "text": "HTTP (port 80) web page retrieval"},
            {"id": "i2", "text": "TFTP (Trivial File Transfer Protocol, port 69)"},
            {"id": "i3", "text": "DNS queries and zone transfers"},
            {"id": "i4", "text": "DHCP discover/offer/request/acknowledge"},
            {"id": "i5", "text": "LDAP directory queries (port 389)"},
            {"id": "i6", "text": "SNMP polling and traps (ports 161/162)"},
        ],
        "answer": {"i1": "c1", "i2": "c2", "i3": "c3", "i4": "c2", "i5": "c3", "i6": "c2"},
        "rationales": {
            "i1": "HTTP uses TCP 80 exclusively. TCP's reliable, ordered delivery is required for web content.",
            "i2": "TFTP uses UDP 69 only. It is a deliberately minimal protocol (used for PXE boot and network device firmware) that omits the overhead of TCP handshaking; reliability is handled at the application layer.",
            "i3": "DNS uses UDP 53 for standard queries (fast, low overhead) and TCP 53 for zone transfers and responses exceeding 512 bytes. Both transports are in active use.",
            "i4": "DHCP uses UDP only — UDP 67 (server) and UDP 68 (client). Because the client has no IP yet, it cannot establish a TCP connection; it broadcasts UDP datagrams.",
            "i5": "LDAP can use both TCP 389 and UDP 389. Clients typically prefer TCP for reliable directory queries but UDP is also defined in the standard.",
            "i6": "SNMP uses UDP 161 (agent polling) and UDP 162 (traps to manager). SNMPv3 adds security features but still uses UDP. TCP is not used in standard SNMP deployments.",
        },
        "explanation": (
            "High-value exam points: DNS = both TCP+UDP (zone transfers are TCP); DHCP = UDP only (broadcast before IP assignment); "
            "TFTP = UDP only (deliberately simple); SNMP = UDP only; HTTP/HTTPS/FTP/SMTP/RDP/SSH = TCP only. "
            "The rule of thumb: protocols requiring guaranteed delivery use TCP; real-time or broadcast protocols use UDP."
        ),
    },

    # ─────────────────────────────────────────────────────────────────────────
    # PBQ 8 — pbq_categorize | Domain 3 | Hardware
    # ─────────────────────────────────────────────────────────────────────────
    {
        "id": "apbq-008",
        "domain": 3,
        "objective": "3.3",
        "type": "pbq_categorize",
        "difficulty": "hard",
        "study_topic": "Storage form factors — desktop vs laptop vs enterprise",
        "stem": (
            "A technician is ordering storage drives for mixed environments. "
            "Categorize each drive form factor or interface into its primary deployment category."
        ),
        "categories": [
            {"id": "c1", "text": "Desktop / tower workstation (typically 3.5\" bays)"},
            {"id": "c2", "text": "Laptop / ultrabook (space-constrained)"},
            {"id": "c3", "text": "Enterprise / server (high-density or high-speed)"},
        ],
        "items": [
            {"id": "i1", "text": "3.5-inch SATA HDD spinning at 7200 RPM"},
            {"id": "i2", "text": "M.2 2242 PCIe NVMe SSD"},
            {"id": "i3", "text": "2.5-inch SATA SSD"},
            {"id": "i4", "text": "U.2 NVMe SSD (formerly SFF-8639)"},
            {"id": "i5", "text": "mSATA SSD module"},
            {"id": "i6", "text": "3.5-inch SAS 12 Gb/s HDD"},
        ],
        "answer": {"i1": "c1", "i2": "c2", "i3": "c2", "i4": "c3", "i5": "c2", "i6": "c3"},
        "rationales": {
            "i1": "3.5-inch SATA HDDs are the standard desktop/tower hard drive form factor. They are too large and power-hungry for most laptops.",
            "i2": "M.2 2242 (22 mm wide, 42 mm long) is a compact form factor used in laptops, tablets, and ultrabooks where space is at a premium. The PCIe NVMe interface provides high throughput in a tiny package.",
            "i3": "2.5-inch SATA SSDs fit both laptops (native bay) and desktops (with a 3.5\" adapter bracket). They are overwhelmingly used as laptop storage or as desktop SSD upgrades in SATA-only systems.",
            "i4": "U.2 (SFF-8639) uses the same PCIe NVMe protocol as M.2 but in a 2.5-inch hot-swap form factor designed for enterprise servers and storage arrays that need the high throughput of NVMe with hot-swap capability.",
            "i5": "mSATA is a legacy mini-PCIe form factor used in older ultra-thin laptops and embedded systems. It has been largely replaced by M.2 but remains in older mobile hardware.",
            "i6": "SAS (Serial Attached SCSI) 3.5-inch drives are enterprise server/storage-array components. SAS offers higher reliability, dual-porting, and speeds (12 Gb/s) not available on consumer SATA, making them unsuitable for typical desktop use.",
        },
        "explanation": (
            "Key distinctions: U.2 vs M.2 — both are NVMe but U.2 is hot-swappable enterprise; M.2 is compact mobile/consumer. "
            "SAS vs SATA — SAS supports dual-port and command queuing depth of 65,535 vs SATA's 32; SAS is enterprise-only. "
            "mSATA is legacy mobile; M.2 is its modern replacement. "
            "2.5-inch SATA SSDs straddle laptop and desktop but are primarily mobile or SATA-upgrade use cases."
        ),
    },

    # ─────────────────────────────────────────────────────────────────────────
    # PBQ 9 — pbq_categorize | Domain 4 | Virtualization & Cloud
    # ─────────────────────────────────────────────────────────────────────────
    {
        "id": "apbq-009",
        "domain": 4,
        "objective": "4.2",
        "type": "pbq_categorize",
        "difficulty": "hard",
        "study_topic": "Hypervisor types — Type 1 (bare-metal) vs Type 2 (hosted)",
        "stem": (
            "Classify each virtualization product or scenario as a Type 1 (bare-metal) hypervisor "
            "or a Type 2 (hosted) hypervisor."
        ),
        "categories": [
            {"id": "c1", "text": "Type 1 — Bare-metal hypervisor"},
            {"id": "c2", "text": "Type 2 — Hosted hypervisor"},
        ],
        "items": [
            {"id": "i1", "text": "VMware ESXi installed directly on server hardware with no underlying OS"},
            {"id": "i2", "text": "Oracle VirtualBox running inside Windows 10 on a developer's laptop"},
            {"id": "i3", "text": "Microsoft Hyper-V Server (standalone, free SKU) running on bare hardware"},
            {"id": "i4", "text": "VMware Workstation Pro installed on Ubuntu Linux"},
            {"id": "i5", "text": "Microsoft Hyper-V role enabled inside Windows 11 Pro on a desktop"},
            {"id": "i6", "text": "Citrix Hypervisor (XenServer) managing a production VM pool on rack servers"},
        ],
        "answer": {"i1": "c1", "i2": "c2", "i3": "c1", "i4": "c2", "i5": "c2", "i6": "c1"},
        "rationales": {
            "i1": "VMware ESXi is the quintessential Type 1 hypervisor. It boots directly on hardware and IS the operating environment — no Windows or Linux host underneath.",
            "i2": "VirtualBox is a Type 2 hypervisor. It installs and runs as an application inside an existing host OS (Windows, macOS, or Linux) and depends on that OS for hardware access.",
            "i3": "Hyper-V Server (standalone free SKU) installs directly on hardware like ESXi and is classified as Type 1. It boots to a minimal Windows Server Core kernel that IS the hypervisor.",
            "i4": "VMware Workstation Pro is a Type 2 hypervisor. It runs as an application on top of a host OS (Linux in this case) and relies on the host kernel for hardware drivers.",
            "i5": "This is the classic A+ trap: Hyper-V installed as a ROLE inside Windows 11 Pro is still officially classified as Type 1 (Microsoft inserts Hyper-V beneath Windows, making Windows itself a privileged VM). However, for exam purposes this scenario — running inside an existing Windows install — often appears as a Type 2 context. Most A+ materials classify the Windows-10/11 Hyper-V role as Type 2 because it depends on an existing Windows host OS installation.",
            "i6": "Citrix Hypervisor (XenServer) is a Type 1 bare-metal hypervisor based on the Xen open-source project. It runs directly on server hardware in production data centers.",
        },
        "explanation": (
            "Type 1 = bare-metal; boots directly on hardware; examples: VMware ESXi, Microsoft Hyper-V Server, Citrix XenServer, KVM (as part of Linux kernel). "
            "Type 2 = hosted; runs as an application; examples: VMware Workstation/Fusion, Oracle VirtualBox, Parallels Desktop. "
            "The Hyper-V role inside Windows is debated — architecturally Type 1 (Hyper-V sits below Windows), but practically treated as Type 2 in end-user exam scenarios. "
            "The defining question: does the hypervisor need an existing host OS to run? If yes → Type 2."
        ),
    },

    # ─────────────────────────────────────────────────────────────────────────
    # PBQ 10 — pbq_categorize | Domain 5 | Hardware & Network Troubleshooting
    # ─────────────────────────────────────────────────────────────────────────
    {
        "id": "apbq-010",
        "domain": 5,
        "objective": "5.3",
        "type": "pbq_categorize",
        "difficulty": "hard",
        "study_topic": "Printer symptoms — categorize by printer type causing the symptom",
        "stem": (
            "A technician receives several printer trouble tickets. "
            "Based on each symptom description, categorize the printer type most likely responsible."
        ),
        "categories": [
            {"id": "c1", "text": "Laser printer"},
            {"id": "c2", "text": "Inkjet printer"},
            {"id": "c3", "text": "Thermal printer"},
        ],
        "items": [
            {"id": "i1", "text": "Printed pages have a waxy, slightly shiny residue that smears when first touched but sets after a few seconds of heat from handling"},
            {"id": "i2", "text": "Output has horizontal white gaps or banding across the page every 25–30 mm, and the nozzle check pattern confirms blocked nozzles"},
            {"id": "i3", "text": "The printer produces blank receipts even though the paper roll was just replaced; output is completely white"},
            {"id": "i4", "text": "Pages come out with a repetitive ghost image (secondary faint image offset by exactly the circumference of the drum)"},
            {"id": "i5", "text": "A burning or ozone smell is detected during printing, and the fuser lamp is at end-of-life"},
            {"id": "i6", "text": "Printouts fade rapidly when stored in a warm car and the paper feels smooth and slick"},
        ],
        "answer": {"i1": "c1", "i2": "c2", "i3": "c3", "i4": "c1", "i5": "c1", "i6": "c3"},
        "rationales": {
            "i1": "Waxy residue that needs heat to fully fuse is a sign of a laser printer with a fuser that is not reaching full temperature (low fuser temperature / worn fuser assembly). Laser toner is a plastic-based powder fused by heat.",
            "i2": "Horizontal banding aligned to nozzle-check failures is a classic inkjet symptom caused by clogged or dried print-head nozzles. Running the printer's built-in head-cleaning utility is the first corrective step.",
            "i3": "Thermal printers require heat-sensitive (thermochromic) paper. Installing plain paper (which lacks the coating) produces blank output. This is the most common thermal printer 'failure' — wrong paper loaded.",
            "i4": "Ghosting offset by exactly the drum circumference is a laser printer drum defect (scratched or worn OPC drum). The residual charge on the damaged spot attracts toner on the next revolution, producing a ghost image.",
            "i5": "Ozone smell and a burning odor are unique to laser printers. The corona wire / charge roller generates ozone during the charging stage, and the fuser lamp generates heat. No other common printer type uses these components.",
            "i6": "Thermal prints fade in heat because the thermochromic dye re-activates and then bleaches. Smooth, slick thermal paper is another giveaway. Inkjet and laser prints are stable at car temperatures.",
        },
        "explanation": (
            "Laser-unique symptoms: ghosting (drum circumference offset), fuser smearing, ozone smell, static-related paper jams, streaks from worn drum. "
            "Inkjet-unique symptoms: banding/missing nozzles, wet ink smearing immediately, ink color bleeding, streaks from partially clogged head. "
            "Thermal-unique symptoms: blank output (wrong paper), heat-fading, no ink/toner needed. "
            "Dot-matrix-unique symptoms: faded output (worn ribbon), perforated paper edge issues — not tested here but good to know."
        ),
    },

    # ─────────────────────────────────────────────────────────────────────────
    # PBQ 11 — pbq_ordering | Domain 3 | Hardware
    # ─────────────────────────────────────────────────────────────────────────
    {
        "id": "apbq-011",
        "domain": 3,
        "objective": "3.5",
        "type": "pbq_ordering",
        "difficulty": "hard",
        "study_topic": "Laser printer imaging process — seven stages in correct order",
        "stem": (
            "A laser printer is producing output with ghost images and poor fusing. "
            "To diagnose which stage is failing, you must recall the seven-stage laser printing process. "
            "Place the stages in the correct order from first to last."
        ),
        "items": [
            {"id": "i1", "text": "Processing — the RIP (Raster Image Processor) converts the print job into a bitmap the laser can render"},
            {"id": "i2", "text": "Charging — the primary corona wire or charge roller applies a uniform high-voltage negative charge to the entire drum surface"},
            {"id": "i3", "text": "Exposing — the laser beam selectively neutralizes (discharges) areas of the drum to form the latent image"},
            {"id": "i4", "text": "Developing — negatively charged toner from the developer roller is attracted to the discharged (lower-voltage) areas of the drum"},
            {"id": "i5", "text": "Transferring — the transfer corona wire or belt applies a positive charge to the paper, pulling toner off the drum and onto the page"},
            {"id": "i6", "text": "Fusing — heat and pressure from the fuser assembly melt and permanently bond the toner particles into the paper fibers"},
            {"id": "i7", "text": "Cleaning — a rubber blade scrapes residual toner from the drum, and the erase lamp discharges it uniformly for the next cycle"},
        ],
        "answer": ["i1", "i2", "i3", "i4", "i5", "i6", "i7"],
        "rationales": {
            "i1": "Processing must happen first: the printer cannot move any mechanical parts until the RIP has created the full rasterized page data and sent it to the print engine.",
            "i2": "Charging is the first electromechanical step. The drum surface must receive a uniform negative charge before the laser can create a latent image by selectively removing that charge.",
            "i3": "Exposing comes immediately after charging. The laser discharges specific pixels to form the invisible (latent) electrostatic image on the drum.",
            "i4": "Developing follows exposure. Toner (negatively charged) is repelled by the still-charged (dark) areas and attracted to the discharged (image) areas, making the latent image visible.",
            "i5": "Transferring moves toner from drum to paper. A positive charge applied to the paper pulls the negatively charged toner off the drum surface.",
            "i6": "Fusing permanently bonds the toner. Heat (typically 180–200 °C) melts the plastic toner particles into the paper fibers; pressure rollers ensure even contact.",
            "i7": "Cleaning is the final stage. Residual toner is physically scraped off and the drum is optically discharged (erase lamp) so it begins the next page fresh. This is why ghosting from a previous page indicates a cleaning or drum failure.",
        },
        "explanation": (
            "Mnemonic: 'Please Charge Every Developer To Fuse Cleanly' → Processing, Charging, Exposing, Developing, Transferring, Fusing, Cleaning. "
            "Common exam trap: some sources list only 6 steps by merging 'Processing' into a pre-press step — CompTIA 220-1201 explicitly includes all 7. "
            "Ghost images = cleaning or drum failure (step 7 or step 2/3 residue). "
            "Fuser smear = step 6 failure. Blank page = step 3 (laser) or step 4 (no toner). "
            "Toner not sticking = step 6 (fuser) or step 5 (transfer) failure."
        ),
    },

    # ─────────────────────────────────────────────────────────────────────────
    # PBQ 12 — pbq_ordering | Domain 1 | Mobile Devices
    # ─────────────────────────────────────────────────────────────────────────
    {
        "id": "apbq-012",
        "domain": 1,
        "objective": "1.3",
        "type": "pbq_ordering",
        "difficulty": "hard",
        "study_topic": "Safe swollen (lithium-ion) battery response procedure",
        "stem": (
            "A user reports that their laptop's trackpad is rising and the chassis has a visible bulge. "
            "You determine the lithium-ion battery is swollen. "
            "Place the response steps in the correct safety order, first action to last."
        ),
        "items": [
            {"id": "i1", "text": "Immediately power off the device and disconnect the AC adapter to eliminate heat and charging current"},
            {"id": "i2", "text": "Do NOT attempt to puncture, bend, compress, or place the device in a sealed bag — move it to a cool, open, non-flammable surface away from combustibles"},
            {"id": "i3", "text": "Assess the severity: if the battery is cracked, leaking electrolyte, or hot to the touch, evacuate the immediate area and call the fire department or hazmat"},
            {"id": "i4", "text": "If the device is stable (cool, not leaking), carefully remove the battery using manufacturer-approved procedures and ESD precautions; do not force connectors"},
            {"id": "i5", "text": "Place the removed swollen battery in a non-conductive, fireproof container (e.g., LiPo-safe bag) or follow local hazardous-waste guidelines for transport"},
            {"id": "i6", "text": "Document the incident, notify the user and appropriate safety/management personnel, and arrange proper battery recycling through a certified e-waste facility"},
        ],
        "answer": ["i1", "i2", "i3", "i4", "i5", "i6"],
        "rationales": {
            "i1": "Removing power is the immediate first priority. Continued charging or discharging generates heat that can trigger thermal runaway in an already compromised lithium-ion cell.",
            "i2": "Placing a swollen Li-ion battery in a sealed bag concentrates any off-gassed fumes and can accelerate failure. Move it to an open, non-flammable area. Puncturing is extremely dangerous.",
            "i3": "Before attempting removal, assess risk. A hot or leaking battery can vent hydrogen fluoride gas and ignite; that is a hazmat event requiring professional response, not a technician repair.",
            "i4": "Only after confirming the battery is cool and stable should you attempt removal. Follow OEM procedures to avoid applying mechanical stress that could puncture the pouch cell.",
            "i5": "A removed swollen battery must be isolated in a fireproof container (LiPo-safe bag, sand bucket, or metal container). Never store it loose in a drawer or cardboard box.",
            "i6": "Documentation and proper disposal are the final steps. Li-ion batteries are regulated hazardous waste; disposal in regular trash is illegal in most jurisdictions and environmentally harmful.",
        },
        "explanation": (
            "The key principle is thermal runaway prevention: stop the energy source first (step 1), prevent mechanical stress (step 2), triage severity (step 3), then carefully remediate (steps 4–5), and close the loop (step 6). "
            "A+ Core 1 tests safety and environmental impacts (objective 1.3 and 5.7). "
            "Never put a swollen battery in a sealed container, never puncture it, never charge it. "
            "Always use an ESD strap when opening a device, even during battery replacement."
        ),
    },

    # ─────────────────────────────────────────────────────────────────────────
    # PBQ 13 — pbq_ordering | Domain 2 | Networking
    # ─────────────────────────────────────────────────────────────────────────
    {
        "id": "apbq-013",
        "domain": 2,
        "objective": "2.4",
        "type": "pbq_ordering",
        "difficulty": "hard",
        "study_topic": "Configuring a new SOHO wireless network securely — setup sequence",
        "stem": (
            "A technician is deploying a brand-new SOHO wireless router for a small business. "
            "Place the configuration steps in the correct order to establish a secure wireless network "
            "from unboxing to handing off to the client."
        ),
        "items": [
            {"id": "i1", "text": "Connect the router's WAN port to the ISP modem/ONT and power on the router"},
            {"id": "i2", "text": "Access the router admin console via its default LAN IP (e.g., 192.168.1.1) using a wired connection and log in with factory credentials"},
            {"id": "i3", "text": "Change the default administrator username and password to a strong, unique credential before making any other configuration changes"},
            {"id": "i4", "text": "Configure the WAN interface (DHCP, PPPoE, or static) per the ISP's requirements and verify internet connectivity from the router"},
            {"id": "i5", "text": "Set the wireless SSID to a non-identifying name, select WPA3 (or WPA2-AES if WPA3 is unavailable), and set a strong, unique pre-shared key"},
            {"id": "i6", "text": "Disable WPS, disable remote management (if not required), enable the firewall, and confirm firmware is updated to the latest release"},
            {"id": "i7", "text": "Connect a wireless client device, authenticate with the new SSID and PSK, verify internet access, and document the configuration for the client"},
        ],
        "answer": ["i1", "i2", "i3", "i4", "i5", "i6", "i7"],
        "rationales": {
            "i1": "Physical installation comes first. The router must have a WAN connection and power before its web interface is accessible.",
            "i2": "The admin console is accessed over a wired LAN connection initially to avoid configuring security settings over an open wireless link. Factory IP and credentials are used at this stage.",
            "i3": "Changing the admin password is the single most important first action inside the console. Leaving factory credentials in place is the root cause of many SOHO router compromises.",
            "i4": "WAN configuration must be correct before testing internet connectivity. Without a working WAN link, wireless client testing in step 7 will fail.",
            "i5": "Wireless security configuration (SSID + encryption) comes after WAN is confirmed. WPA3 is the current standard; WPA2-AES (CCMP) is the acceptable fallback. TKIP and WEP are never acceptable.",
            "i6": "Hardening tasks (disable WPS, disable remote admin, update firmware) should be completed before connecting any client devices. WPS PIN mode has a known brute-force vulnerability (Reaver).",
            "i7": "End-to-end client verification is the final step. Once a client connects and browses successfully, document SSID, PSK, admin URL, and firmware version for the client's records.",
        },
        "explanation": (
            "The order reflects the dependency chain: hardware → admin access → secure admin → WAN → wireless → harden → verify. "
            "Critical exam points: always change default credentials BEFORE configuring other settings; "
            "disable WPS (brute-forceable); prefer WPA3 > WPA2-AES > WPA2-TKIP (never WEP); "
            "update firmware before client hand-off. Remote management should be off unless explicitly required."
        ),
    },

    # ─────────────────────────────────────────────────────────────────────────
    # PBQ 14 — pbq_ordering | Domain 5 | Hardware & Network Troubleshooting
    # ─────────────────────────────────────────────────────────────────────────
    {
        "id": "apbq-014",
        "domain": 5,
        "objective": "5.1",
        "type": "pbq_ordering",
        "difficulty": "hard",
        "study_topic": "Safe RAM installation procedure — correct sequence including ESD precautions",
        "stem": (
            "A technician is upgrading RAM in a desktop PC. "
            "Place the steps in the correct order to safely remove old DIMMs and install new ones "
            "without causing ESD damage or hardware failure."
        ),
        "items": [
            {"id": "i1", "text": "Shut down the PC completely (full power-off, not sleep/hibernate) and unplug the AC power cord from the wall outlet"},
            {"id": "i2", "text": "Press the power button once (with AC unplugged) to discharge residual capacitor charge from the motherboard"},
            {"id": "i3", "text": "Put on an anti-static wrist strap and clip it to the bare metal chassis of the case to equalize potential"},
            {"id": "i4", "text": "Open the side panel, locate the DIMM slots, and consult the motherboard manual to identify the correct slot population order for the new capacity"},
            {"id": "i5", "text": "Press the retention clips outward on both ends of the occupied DIMM slot simultaneously; the old module will eject slightly — remove it by its edges only, without touching the gold contacts"},
            {"id": "i6", "text": "Align the new DIMM's notch to the slot key, press firmly and evenly on both ends until both retention clips click into the locked position"},
            {"id": "i7", "text": "Reconnect the AC power cord, power on the system, and verify the BIOS/UEFI Memory Information screen reports the correct total capacity and speed (XMP/EXPO profile if applicable)"},
        ],
        "answer": ["i1", "i2", "i3", "i4", "i5", "i6", "i7"],
        "rationales": {
            "i1": "A full shutdown (not sleep) is mandatory. Sleep/hibernate modes keep memory contents powered. Unplugging the AC cord removes mains power, but capacitors may still hold charge.",
            "i2": "Pressing the power button with AC unplugged drains residual charge from capacitors on the board. This step is often omitted but prevents damage from latent voltage on the memory bus.",
            "i3": "The ESD wrist strap must be attached BEFORE touching any internal components. Clipping to bare chassis metal (not a painted surface) ensures the technician and chassis are at the same potential.",
            "i4": "Checking the motherboard manual for slot population rules (typically A2/B2 before A1/B1 for dual-channel) prevents incorrectly populating slots that would degrade performance or prevent booting.",
            "i5": "Both retention clips must be released simultaneously to avoid lateral stress on the slot. Touching the gold contacts introduces skin oils and can cause oxidation or ESD discharge.",
            "i6": "The notch (index key) prevents installing the DIMM backwards. Pressing firmly and evenly at both ends until both clips click ensures full electrical contact across all pins.",
            "i7": "Always verify in BIOS/UEFI before booting the OS. The memory map may show correct total RAM but default to a lower speed; enabling an XMP/EXPO profile is required to run at advertised speed.",
        },
        "explanation": (
            "The dependency chain: power off completely → discharge capacitors → ESD protection → plan slot placement → remove old → install new → verify. "
            "Critical traps: sleep is NOT off — AC must be unplugged; wrist strap must clip to BARE metal; "
            "check slot order (B2-A2 first on many boards for dual-channel); never touch gold contacts. "
            "The BIOS verification step catches bent pins, unseated modules, and XMP/EXPO configuration issues before the OS boots."
        ),
    },
]

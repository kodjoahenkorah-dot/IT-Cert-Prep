"""
CompTIA A+ Core 1 (220-1201) — Domain 2: Networking
Study notes following Professor Messer's playlist order for Domain 2.
"""

NOTES = [
    {
        "domain": 2,
        "topic": "Ports & protocols",
        "objective": "2.1",
        "video": "Introduction to IP",
        "study_topics": ["Ports & protocols"],
        "body": (
            "<p><strong>Ports</strong> are logical endpoints (0–65535) that identify specific "
            "services on a host. Ports 0–1023 are <em>well-known</em>; 1024–49151 are "
            "<em>registered</em>; 49152–65535 are <em>dynamic/ephemeral</em>.</p>"
            "<table border='1' cellpadding='4' cellspacing='0'>"
            "<tr><th>Port(s)</th><th>Protocol</th><th>Transport</th></tr>"
            "<tr><td>20/21</td><td>FTP (data/control)</td><td>TCP</td></tr>"
            "<tr><td>22</td><td>SSH / SFTP / SCP</td><td>TCP</td></tr>"
            "<tr><td>23</td><td>Telnet (cleartext)</td><td>TCP</td></tr>"
            "<tr><td>25</td><td>SMTP (email send)</td><td>TCP</td></tr>"
            "<tr><td>53</td><td>DNS</td><td>UDP (TCP for zone transfers)</td></tr>"
            "<tr><td>67/68</td><td>DHCP (server/client)</td><td>UDP</td></tr>"
            "<tr><td>80</td><td>HTTP</td><td>TCP</td></tr>"
            "<tr><td>110</td><td>POP3 (email retrieve)</td><td>TCP</td></tr>"
            "<tr><td>143</td><td>IMAP (email sync)</td><td>TCP</td></tr>"
            "<tr><td>161/162</td><td>SNMP (poll/trap)</td><td>UDP</td></tr>"
            "<tr><td>389</td><td>LDAP (directory)</td><td>TCP/UDP</td></tr>"
            "<tr><td>443</td><td>HTTPS (TLS)</td><td>TCP</td></tr>"
            "<tr><td>445</td><td>SMB (file sharing)</td><td>TCP</td></tr>"
            "<tr><td>3389</td><td>RDP (remote desktop)</td><td>TCP</td></tr>"
            "</table>"
            "<p>Key exam tip: <strong>Telnet (23)</strong> and <strong>FTP (21)</strong> transmit "
            "credentials in plaintext — always prefer SSH (22) and SFTP. DHCP uses <em>broadcasts</em> "
            "on UDP 67/68, which is why routers must be configured as DHCP relay agents across subnets.</p>"
        ),
        "key_points": [
            "FTP: 20 (data), 21 (control) — TCP",
            "SSH/SFTP/SCP all use port 22 — TCP",
            "Telnet port 23 is cleartext and insecure",
            "SMTP port 25; POP3 port 110; IMAP port 143",
            "DNS port 53: UDP for queries, TCP for zone transfers",
            "DHCP: server listens on 67, client on 68 — UDP",
            "HTTP 80; HTTPS 443; SMB 445; RDP 3389",
            "SNMP: 161 (poll), 162 (trap) — UDP",
            "LDAP port 389 for directory services",
        ],
    },
    {
        "domain": 2,
        "topic": "Networking hardware",
        "objective": "2.2",
        "video": "Network Devices",
        "study_topics": ["Networking hardware"],
        "body": (
            "<p>Understanding physical and logical networking hardware is fundamental to the A+ exam.</p>"
            "<ul>"
            "<li><strong>Hub:</strong> Layer 1 device; repeats frames out all ports — creates one collision domain. "
            "Largely obsolete.</li>"
            "<li><strong>Switch:</strong> Layer 2 device; forwards frames using MAC address table. "
            "Each port is its own collision domain. Managed switches support VLANs and STP.</li>"
            "<li><strong>Router:</strong> Layer 3 device; routes packets between networks using IP addresses "
            "and a routing table. Performs NAT for home/SOHO networks.</li>"
            "<li><strong>Wireless Access Point (WAP):</strong> Connects wireless clients to a wired LAN; "
            "operates at Layer 2. A wireless router combines a WAP, switch, and router.</li>"
            "<li><strong>Modem:</strong> Modulates/demodulates signals (cable, DSL, fiber ONT). "
            "Bridges the ISP network to your LAN.</li>"
            "<li><strong>Firewall:</strong> Filters traffic by rules (packet filtering, stateful inspection, "
            "or application-layer). Can be hardware or software.</li>"
            "<li><strong>Patch panel:</strong> Passive termination point for structured cabling; connects "
            "wall jacks to switch ports via patch cables.</li>"
            "<li><strong>PoE switch / injector:</strong> Delivers DC power over Ethernet cable to devices "
            "like WAPs, IP cameras, and VoIP phones.</li>"
            "<li><strong>NIC (Network Interface Card):</strong> Provides a MAC address and physical interface "
            "(RJ-45, SFP, Wi-Fi) for a device.</li>"
            "<li><strong>Repeater / media converter:</strong> Extends cable distances; media converters "
            "translate between copper and fiber.</li>"
            "</ul>"
            "<p>Exam focus: know which OSI layer each device operates at and what function it performs.</p>"
        ),
        "key_points": [
            "Hub = Layer 1, single collision domain, all ports share bandwidth",
            "Switch = Layer 2, MAC table, each port = separate collision domain",
            "Router = Layer 3, IP routing between networks, performs NAT",
            "WAP = Layer 2, bridges wireless clients to wired LAN",
            "Firewall = filters traffic; can operate at multiple layers",
            "Patch panel = passive cable management, no data processing",
            "PoE switch or injector powers devices like cameras and WAPs over Cat5e/6",
        ],
    },
    {
        "domain": 2,
        "topic": "Wireless standards",
        "objective": "2.3",
        "video": "Wireless Standards",
        "study_topics": ["Wireless standards"],
        "body": (
            "<p>The IEEE 802.11 family defines wireless LAN standards. Key standards for the A+ exam:</p>"
            "<table border='1' cellpadding='4' cellspacing='0'>"
            "<tr><th>Standard</th><th>Frequency</th><th>Max Speed</th><th>Notable Features</th></tr>"
            "<tr><td>802.11a</td><td>5 GHz</td><td>54 Mbps</td><td>Less interference, shorter range</td></tr>"
            "<tr><td>802.11b</td><td>2.4 GHz</td><td>11 Mbps</td><td>First popular standard; prone to interference</td></tr>"
            "<tr><td>802.11g</td><td>2.4 GHz</td><td>54 Mbps</td><td>Backward-compatible with 802.11b</td></tr>"
            "<tr><td>802.11n (Wi-Fi 4)</td><td>2.4 / 5 GHz</td><td>600 Mbps</td><td>MIMO, channel bonding</td></tr>"
            "<tr><td>802.11ac (Wi-Fi 5)</td><td>5 GHz</td><td>~3.5 Gbps</td><td>MU-MIMO, beamforming, 80/160 MHz channels</td></tr>"
            "<tr><td>802.11ax (Wi-Fi 6/6E)</td><td>2.4/5/6 GHz</td><td>~9.6 Gbps</td><td>OFDMA, BSS Coloring, improved density</td></tr>"
            "</table>"
            "<p><strong>Bluetooth</strong> (IEEE 802.15) operates at 2.4 GHz with a range of ~10 m (Class 2). "
            "Used for PANs (keyboards, mice, headsets). <strong>NFC</strong> works within ~4 cm for contactless "
            "payments and device pairing. <strong>RFID</strong> uses radio frequencies to identify tags — common "
            "in asset tracking and access badges.</p>"
            "<p>Exam tip: Wi-Fi 5 (802.11ac) is 5 GHz only. Wi-Fi 6E extends to the 6 GHz band for less "
            "congestion. Higher frequency = higher speed but shorter range and less wall penetration.</p>"
        ),
        "key_points": [
            "802.11a: 5 GHz, 54 Mbps — less interference, shorter range",
            "802.11b: 2.4 GHz, 11 Mbps — oldest common standard",
            "802.11g: 2.4 GHz, 54 Mbps — backward-compatible with b",
            "802.11n (Wi-Fi 4): dual-band, up to 600 Mbps, MIMO",
            "802.11ac (Wi-Fi 5): 5 GHz only, MU-MIMO, beamforming, ~3.5 Gbps",
            "802.11ax (Wi-Fi 6/6E): OFDMA, up to 9.6 Gbps, 6 GHz band added in 6E",
            "Bluetooth (802.15): 2.4 GHz, ~10 m range — PAN devices",
            "Higher frequency = faster speed, shorter range, less penetration",
        ],
    },
    {
        "domain": 2,
        "topic": "Wi-Fi channels & frequencies",
        "objective": "2.3",
        "video": "Wireless Standards",
        "study_topics": ["Wi-Fi channels & frequencies"],
        "body": (
            "<p>Wi-Fi uses specific frequency channels within licensed bands. Understanding channel "
            "overlap is critical for troubleshooting interference.</p>"
            "<p><strong>2.4 GHz band:</strong> Channels 1–14 (US uses 1–11). Each channel is 22 MHz wide "
            "with only 5 MHz separation, causing significant overlap. "
            "<strong>Channels 1, 6, and 11 are non-overlapping</strong> — always use these three to avoid "
            "co-channel interference in dense deployments. A poorly configured neighbor AP on channel 4 "
            "will interfere with both channel 1 and 6.</p>"
            "<p><strong>5 GHz band:</strong> Many more non-overlapping channels (36, 40, 44, 48, 52, 56, "
            "60, 64, 100–165). Channels can be bonded: 40 MHz (2 channels), 80 MHz (4 channels), or "
            "160 MHz (8 channels) — wider channels = more throughput but fewer available channels.</p>"
            "<p><strong>6 GHz band (Wi-Fi 6E):</strong> Adds channels 1–233 (US: ~59 non-overlapping "
            "20 MHz channels), greatly reducing congestion.</p>"
            "<p>Exam tips:</p>"
            "<ul>"
            "<li>2.4 GHz: non-overlapping = <strong>1, 6, 11</strong></li>"
            "<li>5 GHz: more channels, less crowded, better for high-throughput</li>"
            "<li>Use a Wi-Fi analyzer to detect channel congestion before configuring an AP</li>"
            "<li>SSID broadcast can be disabled, but this is security through obscurity — MAC filtering "
            "is also weak; use WPA3 or WPA2 instead</li>"
            "</ul>"
        ),
        "key_points": [
            "2.4 GHz non-overlapping channels: 1, 6, and 11",
            "2.4 GHz has 11 usable channels in the US, all 22 MHz wide",
            "5 GHz has many non-overlapping channels; supports 40/80/160 MHz bonding",
            "Wi-Fi 6E adds the 6 GHz band for ~59 non-overlapping 20 MHz channels",
            "Use a Wi-Fi analyzer to find the least congested channel",
            "Channel bonding increases throughput but reduces number of usable channels",
        ],
    },
    {
        "domain": 2,
        "topic": "IPv4 addressing & APIPA",
        "objective": "2.4",
        "video": "Introduction to IP",
        "study_topics": ["IPv4 addressing & APIPA"],
        "body": (
            "<p>IPv4 uses 32-bit addresses written in dotted-decimal (e.g., <code>192.168.1.100</code>). "
            "An IP address has two parts: the <strong>network</strong> portion and the <strong>host</strong> "
            "portion, defined by the subnet mask.</p>"
            "<p><strong>Address classes (classful — know for exam context):</strong></p>"
            "<ul>"
            "<li>Class A: 1.0.0.0–126.255.255.255, default mask /8 (255.0.0.0)</li>"
            "<li>Class B: 128.0.0.0–191.255.255.255, default mask /16 (255.255.0.0)</li>"
            "<li>Class C: 192.0.0.0–223.255.255.255, default mask /24 (255.255.255.0)</li>"
            "<li>127.x.x.x = loopback (localhost)</li>"
            "</ul>"
            "<p><strong>Private (RFC 1918) ranges:</strong></p>"
            "<ul>"
            "<li>10.0.0.0/8</li>"
            "<li>172.16.0.0–172.31.255.255 (/12)</li>"
            "<li>192.168.0.0/16</li>"
            "</ul>"
            "<p><strong>APIPA (Automatic Private IP Addressing):</strong> When a host cannot reach a DHCP "
            "server, Windows automatically assigns a link-local address in the range "
            "<code>169.254.0.1–169.254.255.254</code> with mask <code>255.255.0.0</code>. APIPA addresses "
            "allow communication only on the local subnet — no internet access. Seeing a 169.254.x.x address "
            "is a classic symptom of a DHCP failure.</p>"
            "<p>Subnet mask in CIDR notation: /24 = 255.255.255.0 (256 IPs, 254 usable hosts). The network "
            "address (all host bits 0) and broadcast (all host bits 1) are not assignable.</p>"
        ),
        "key_points": [
            "IPv4 is 32-bit, dotted-decimal notation",
            "Class A /8, Class B /16, Class C /24 (default masks)",
            "Loopback: 127.0.0.1; Private: 10.x.x.x, 172.16-31.x.x, 192.168.x.x",
            "APIPA range: 169.254.0.1–169.254.255.254 — assigned when DHCP fails",
            "APIPA allows local subnet communication only — no routing to internet",
            "Seeing 169.254.x.x = DHCP server unreachable",
            "Network address (all 0s) and broadcast (all 1s) are not usable host addresses",
        ],
    },
    {
        "domain": 2,
        "topic": "IPv6 addressing",
        "objective": "2.4",
        "video": "IPv6 Overview",
        "study_topics": ["IPv6 addressing"],
        "body": (
            "<p>IPv6 uses <strong>128-bit addresses</strong> written as eight groups of four hexadecimal "
            "digits separated by colons, e.g., <code>2001:0db8:85a3:0000:0000:8a2e:0370:7334</code>.</p>"
            "<p><strong>Shortening rules:</strong></p>"
            "<ul>"
            "<li>Leading zeros in a group can be omitted: <code>0db8</code> → <code>db8</code></li>"
            "<li>One contiguous run of all-zero groups can be replaced with <code>::</code> (only once)</li>"
            "<li>Example: <code>2001:db8::1</code></li>"
            "</ul>"
            "<p><strong>Address types:</strong></p>"
            "<ul>"
            "<li><strong>Unicast:</strong> Single interface. <em>Global unicast</em> (2000::/3) = routable "
            "on the internet. <em>Link-local</em> (fe80::/10) = auto-configured, local segment only.</li>"
            "<li><strong>Multicast:</strong> ff00::/8 — delivers to multiple interfaces simultaneously. "
            "Replaces IPv4 broadcast.</li>"
            "<li><strong>Anycast:</strong> One address shared by multiple interfaces; packet delivered to "
            "the nearest one (routing metric).</li>"
            "</ul>"
            "<p><strong>Special addresses:</strong> <code>::1</code> = loopback (equivalent to 127.0.0.1). "
            "<code>::</code> = unspecified address.</p>"
            "<p><strong>EUI-64:</strong> A method to auto-generate the 64-bit interface ID from a 48-bit "
            "MAC address by inserting <code>FFFE</code> in the middle and flipping bit 7.</p>"
            "<p>IPv6 eliminates NAT because every device can have a globally routable address. "
            "DHCPv6 or SLAAC (Stateless Address Autoconfiguration) handles address assignment.</p>"
        ),
        "key_points": [
            "IPv6 = 128-bit, written as 8 hex groups separated by colons",
            ":: replaces one or more consecutive all-zero groups (used once only)",
            "Global unicast: 2000::/3 — publicly routable",
            "Link-local: fe80::/10 — auto-configured, local segment only",
            "Multicast: ff00::/8 — replaces IPv4 broadcast",
            "Loopback: ::1",
            "EUI-64 generates interface ID from 48-bit MAC address",
            "SLAAC allows stateless auto-configuration without DHCPv6",
        ],
    },
    {
        "domain": 2,
        "topic": "DHCP",
        "objective": "2.4",
        "video": "DHCP Overview",
        "study_topics": ["DHCP"],
        "body": (
            "<p><strong>DHCP (Dynamic Host Configuration Protocol)</strong> automatically assigns IP "
            "configuration to clients using a four-step process called <strong>DORA</strong>:</p>"
            "<ol>"
            "<li><strong>Discover:</strong> Client broadcasts to find DHCP server (UDP src 68, dst 67)</li>"
            "<li><strong>Offer:</strong> Server unicasts/broadcasts an available IP lease offer</li>"
            "<li><strong>Request:</strong> Client broadcasts acceptance of the offered IP</li>"
            "<li><strong>Acknowledge:</strong> Server confirms the lease; client configures its interface</li>"
            "</ol>"
            "<p><strong>DHCP provides:</strong></p>"
            "<ul>"
            "<li>IP address and subnet mask</li>"
            "<li>Default gateway</li>"
            "<li>DNS server address(es)</li>"
            "<li>Lease duration</li>"
            "</ul>"
            "<p><strong>Key DHCP concepts:</strong></p>"
            "<ul>"
            "<li><strong>Scope:</strong> The range of IP addresses the server can assign</li>"
            "<li><strong>Exclusion:</strong> IP addresses within the scope reserved for static assignment</li>"
            "<li><strong>Reservation:</strong> Binding a specific IP to a device's MAC address</li>"
            "<li><strong>Lease time:</strong> Duration before the client must renew (default often 8 days)</li>"
            "<li><strong>DHCP Relay Agent:</strong> Forwards DHCP broadcasts across routers to a central server</li>"
            "</ul>"
            "<p>A <strong>rogue DHCP server</strong> can hand out incorrect gateway/DNS information — a "
            "common man-in-the-middle attack vector. Use DHCP snooping on managed switches to prevent this.</p>"
        ),
        "key_points": [
            "DORA: Discover → Offer → Request → Acknowledge",
            "DHCP uses UDP ports 67 (server) and 68 (client)",
            "DHCP provides: IP, subnet mask, default gateway, DNS server, lease time",
            "Scope = pool of assignable addresses; exclusions reserve static IPs",
            "Reservation = static assignment tied to a device's MAC address",
            "DHCP relay agent forwards broadcasts across routed networks",
            "Rogue DHCP servers = man-in-the-middle risk; mitigate with DHCP snooping",
        ],
    },
    {
        "domain": 2,
        "topic": "DNS records",
        "objective": "2.4",
        "video": "DNS Overview",
        "study_topics": ["DNS records"],
        "body": (
            "<p><strong>DNS (Domain Name System)</strong> resolves human-readable hostnames to IP addresses. "
            "It operates on port 53 (UDP for queries, TCP for zone transfers).</p>"
            "<p><strong>Key DNS record types:</strong></p>"
            "<table border='1' cellpadding='4' cellspacing='0'>"
            "<tr><th>Record</th><th>Purpose</th><th>Example</th></tr>"
            "<tr><td><strong>A</strong></td><td>Maps hostname → IPv4 address</td><td>www.example.com → 93.184.216.34</td></tr>"
            "<tr><td><strong>AAAA</strong></td><td>Maps hostname → IPv6 address</td><td>www.example.com → 2606:2800::1</td></tr>"
            "<tr><td><strong>CNAME</strong></td><td>Alias; points one name to another</td><td>ftp.example.com → www.example.com</td></tr>"
            "<tr><td><strong>MX</strong></td><td>Mail exchanger; directs email delivery</td><td>example.com → mail.example.com (priority 10)</td></tr>"
            "<tr><td><strong>TXT</strong></td><td>Arbitrary text; used for SPF, DKIM, DMARC</td><td>v=spf1 include:... -all</td></tr>"
            "<tr><td><strong>PTR</strong></td><td>Reverse lookup; IP → hostname</td><td>34.216.184.93.in-addr.arpa → www.example.com</td></tr>"
            "<tr><td><strong>NS</strong></td><td>Authoritative nameservers for a domain</td><td>example.com → ns1.example.com</td></tr>"
            "<tr><td><strong>SOA</strong></td><td>Start of Authority; zone metadata</td><td>Serial, refresh, retry, expire</td></tr>"
            "</table>"
            "<p><strong>Email authentication TXT records:</strong></p>"
            "<ul>"
            "<li><strong>SPF:</strong> Lists authorized mail servers for a domain</li>"
            "<li><strong>DKIM:</strong> Cryptographic signature verifying email origin</li>"
            "<li><strong>DMARC:</strong> Policy instructing receivers what to do with failed SPF/DKIM</li>"
            "</ul>"
            "<p>DNS uses a hierarchical, distributed structure: root → TLD (.com) → authoritative nameservers. "
            "Local DNS caching reduces query traffic; TTL (Time To Live) controls cache duration.</p>"
        ),
        "key_points": [
            "A record: hostname to IPv4; AAAA record: hostname to IPv6",
            "CNAME: alias one name to another (cannot point to an IP directly)",
            "MX record: mail exchanger for the domain; lower priority number = preferred",
            "TXT records carry SPF, DKIM, and DMARC email authentication data",
            "PTR record: reverse DNS lookup (IP to hostname)",
            "NS records identify authoritative nameservers for a zone",
            "DNS queries use UDP port 53; zone transfers use TCP port 53",
            "TTL controls how long DNS records are cached",
        ],
    },
    {
        "domain": 2,
        "topic": "VLAN/VPN",
        "objective": "2.5",
        "video": "VLANs and VPNs",
        "study_topics": ["VLAN/VPN"],
        "body": (
            "<p><strong>VLAN (Virtual LAN):</strong> Logically segments a physical network into separate "
            "broadcast domains using managed switches. VLANs improve security, reduce broadcast traffic, "
            "and simplify management without requiring separate physical infrastructure.</p>"
            "<ul>"
            "<li><strong>Access port:</strong> Carries traffic for a single VLAN; used for end devices</li>"
            "<li><strong>Trunk port:</strong> Carries traffic for multiple VLANs between switches using "
            "<strong>802.1Q tagging</strong>; a 4-byte tag is inserted in the Ethernet frame header</li>"
            "<li><strong>Native VLAN:</strong> Traffic on a trunk port that is sent untagged (default VLAN 1 "
            "— best practice: change it)</li>"
            "<li>Inter-VLAN routing requires a Layer 3 device (router or Layer 3 switch)</li>"
            "</ul>"
            "<p><strong>VPN (Virtual Private Network):</strong> Creates an encrypted tunnel over a public "
            "network (internet) to securely connect remote users or sites.</p>"
            "<ul>"
            "<li><strong>Site-to-site VPN:</strong> Connects two LANs permanently (e.g., branch to HQ); "
            "uses IPSec</li>"
            "<li><strong>Client-to-site (Remote access) VPN:</strong> Individual user connects to corporate "
            "network; uses SSL/TLS (OpenVPN, Cisco AnyConnect) or IPSec</li>"
            "<li><strong>Split tunneling:</strong> Only corporate traffic goes through VPN; internet traffic "
            "goes direct — reduces VPN load but may be a security risk</li>"
            "</ul>"
            "<p>VPN protocols include <strong>IPSec</strong> (AH + ESP), <strong>L2TP/IPSec</strong>, "
            "<strong>OpenVPN</strong> (SSL/TLS), and <strong>WireGuard</strong> (modern, fast).</p>"
        ),
        "key_points": [
            "VLAN = logical network segmentation on a managed switch using 802.1Q",
            "Access port: one VLAN; trunk port: multiple VLANs (tagged with 802.1Q)",
            "Native VLAN is untagged on trunk — change from default VLAN 1 for security",
            "Inter-VLAN routing needs a Layer 3 device (router or L3 switch)",
            "Site-to-site VPN: connects two networks permanently (IPSec)",
            "Remote access VPN: individual users connect to corporate LAN (SSL/TLS or IPSec)",
            "Split tunneling: only corporate traffic through VPN; internet goes direct",
        ],
    },
    {
        "domain": 2,
        "topic": "Internet connection types",
        "objective": "2.6",
        "video": "Internet Connection Types",
        "study_topics": ["Internet connection types"],
        "body": (
            "<p>Different technologies connect homes and businesses to the internet, each with "
            "distinct characteristics:</p>"
            "<table border='1' cellpadding='4' cellspacing='0'>"
            "<tr><th>Type</th><th>Medium</th><th>Speed</th><th>Notes</th></tr>"
            "<tr><td><strong>Cable</strong></td><td>Coaxial (DOCSIS)</td><td>Up to 1 Gbps+</td>"
            "<td>Shared bandwidth with neighbors; asymmetric</td></tr>"
            "<tr><td><strong>DSL</strong></td><td>Phone line (twisted pair)</td><td>1–100 Mbps</td>"
            "<td>Distance-limited; ADSL asymmetric, VDSL faster</td></tr>"
            "<tr><td><strong>Fiber (FTTH/FTTP)</strong></td><td>Fiber optic</td><td>Up to 10 Gbps+</td>"
            "<td>Symmetric speeds possible; least interference</td></tr>"
            "<tr><td><strong>Satellite</strong></td><td>Radio (geostationary/LEO)</td><td>25–200 Mbps</td>"
            "<td>High latency (GEO ~600ms); LEO (Starlink) ~20-40ms</td></tr>"
            "<tr><td><strong>Cellular (4G/5G)</strong></td><td>Radio</td><td>10 Mbps–multi-Gbps</td>"
            "<td>Mobile; 5G mmWave very fast, short range</td></tr>"
            "<tr><td><strong>Fixed wireless</strong></td><td>Radio (point-to-point)</td><td>Varies</td>"
            "<td>Line-of-sight required; rural deployments</td></tr>"
            "<tr><td><strong>Dial-up</strong></td><td>PSTN phone line</td><td>56 Kbps max</td>"
            "<td>Legacy; uses analog modem</td></tr>"
            "<tr><td><strong>ISDN</strong></td><td>Phone line (digital)</td><td>128 Kbps (BRI)</td>"
            "<td>Legacy digital; replaced by DSL/fiber</td></tr>"
            "</table>"
            "<p><strong>Fiber optic</strong> uses a ONT (Optical Network Terminal) to convert light signals "
            "to Ethernet. Cable uses a DOCSIS cable modem. DSL uses a DSL modem connected to a phone line "
            "with a <em>splitter</em> to separate voice and data.</p>"
        ),
        "key_points": [
            "Cable: coaxial/DOCSIS, shared bandwidth, asymmetric (faster down than up)",
            "DSL: phone line, distance-limited; ADSL asymmetric, VDSL faster",
            "Fiber (FTTH): fastest, symmetric possible, uses ONT at premises",
            "Satellite: high latency (GEO); LEO (Starlink) reduces latency to ~20-40ms",
            "Cellular 4G/5G: mobile; 5G mmWave = very high speed, very short range",
            "Fixed wireless: point-to-point radio, requires line-of-sight",
            "Dial-up: 56 Kbps analog — legacy; ISDN: 128 Kbps digital — legacy",
        ],
    },
    {
        "domain": 2,
        "topic": "Network types (LAN/WAN/PAN)",
        "objective": "2.7",
        "video": "Network Types",
        "study_topics": ["Network types (LAN/WAN/PAN)"],
        "body": (
            "<p>Networks are classified by geographic scope and purpose:</p>"
            "<table border='1' cellpadding='4' cellspacing='0'>"
            "<tr><th>Type</th><th>Scope</th><th>Description</th></tr>"
            "<tr><td><strong>PAN</strong></td><td>Personal (~1–10 m)</td>"
            "<td>Personal Area Network; Bluetooth/NFC devices around a person</td></tr>"
            "<tr><td><strong>LAN</strong></td><td>Local (building/floor)</td>"
            "<td>Local Area Network; Ethernet/Wi-Fi; single organization control</td></tr>"
            "<tr><td><strong>WLAN</strong></td><td>Local (wireless)</td>"
            "<td>Wireless LAN using 802.11 standards</td></tr>"
            "<tr><td><strong>MAN</strong></td><td>Metro (city)</td>"
            "<td>Metropolitan Area Network; connects multiple LANs across a city</td></tr>"
            "<tr><td><strong>WAN</strong></td><td>Wide (country/global)</td>"
            "<td>Wide Area Network; connects geographically distant sites; uses leased lines, MPLS, internet</td></tr>"
            "<tr><td><strong>SAN</strong></td><td>Storage network</td>"
            "<td>Storage Area Network; high-speed network for storage devices (Fibre Channel, iSCSI)</td></tr>"
            "<tr><td><strong>CAN</strong></td><td>Campus</td>"
            "<td>Campus Area Network; multiple buildings on a campus connected via fiber</td></tr>"
            "</table>"
            "<p>Additional relevant concepts:</p>"
            "<ul>"
            "<li><strong>SOHO:</strong> Small Office/Home Office network — typically a wireless router "
            "with 4-port switch, NAT, DHCP, and basic firewall built in</li>"
            "<li><strong>Intranet:</strong> Private internal web accessible only within an organization</li>"
            "<li><strong>Extranet:</strong> Extends intranet access to trusted external partners via VPN</li>"
            "</ul>"
        ),
        "key_points": [
            "PAN: ~10 m, personal devices, Bluetooth/NFC",
            "LAN: building/floor, Ethernet or Wi-Fi, single organization",
            "WLAN: wireless LAN using 802.11",
            "MAN: metropolitan, spans a city",
            "WAN: wide area, connects geographically distant sites (internet, MPLS, leased lines)",
            "SAN: dedicated high-speed storage network (Fibre Channel, iSCSI)",
            "SOHO router combines WAP, switch, router, NAT, DHCP, and firewall",
        ],
    },
    {
        "domain": 2,
        "topic": "Copper & fiber cabling",
        "objective": "2.8",
        "video": "Network Cabling",
        "study_topics": ["Copper & fiber cabling"],
        "body": (
            "<p><strong>Copper cabling — Twisted Pair (UTP/STP):</strong></p>"
            "<table border='1' cellpadding='4' cellspacing='0'>"
            "<tr><th>Category</th><th>Max Speed</th><th>Max Bandwidth</th><th>Notes</th></tr>"
            "<tr><td>Cat 5</td><td>100 Mbps</td><td>100 MHz</td><td>100BASE-TX; largely obsolete</td></tr>"
            "<tr><td>Cat 5e</td><td>1 Gbps</td><td>100 MHz</td><td>1000BASE-T; most common legacy install</td></tr>"
            "<tr><td>Cat 6</td><td>1 Gbps (10G to 55m)</td><td>250 MHz</td><td>Tighter twist, optional spline</td></tr>"
            "<tr><td>Cat 6A</td><td>10 Gbps</td><td>500 MHz</td><td>10GBASE-T to 100m; heavier/thicker</td></tr>"
            "<tr><td>Cat 7</td><td>10 Gbps</td><td>600 MHz</td><td>Individually shielded pairs (SSTP)</td></tr>"
            "<tr><td>Cat 8</td><td>25/40 Gbps</td><td>2000 MHz</td><td>Data center, max 30m</td></tr>"
            "</table>"
            "<p><strong>Coaxial cable:</strong> RG-6 (TV/cable internet), RG-59 (CCTV). Uses F-type or BNC "
            "connectors. More interference-resistant than UTP.</p>"
            "<p><strong>Fiber optic cabling:</strong></p>"
            "<ul>"
            "<li><strong>Single-mode (SMF):</strong> Narrow core (~9 µm), laser light, very long distance "
            "(km), typically yellow jacket</li>"
            "<li><strong>Multi-mode (MMF):</strong> Wider core (50 or 62.5 µm), LED or VCSEL, shorter "
            "distance (up to ~550m for OM3/OM4), orange or aqua jacket</li>"
            "</ul>"
            "<p>Fiber connectors: <strong>LC</strong> (small form factor, common), <strong>SC</strong> "
            "(push-pull, square), <strong>ST</strong> (bayonet twist-lock, older). "
            "Fiber is immune to EMI, supports very long runs, and is more secure (no signal radiation).</p>"
        ),
        "key_points": [
            "Cat 5e: 1 Gbps / 100 MHz; Cat 6: 1 Gbps (10G to 55m) / 250 MHz",
            "Cat 6A: 10 Gbps to 100m / 500 MHz — best choice for new installs",
            "Cat 8: 25/40 Gbps, data center use, max 30m",
            "UTP = unshielded twisted pair; STP/FTP = shielded variants",
            "Single-mode fiber: long distance (km), laser, ~9µm core, yellow jacket",
            "Multi-mode fiber: shorter distance (up to ~550m), LED, 50/62.5µm core, orange/aqua",
            "Fiber connectors: LC (small), SC (push-pull), ST (bayonet twist)",
            "Fiber is immune to EMI and cannot be tapped easily",
        ],
    },
    {
        "domain": 2,
        "topic": "T568A/B wiring",
        "objective": "2.8",
        "video": "Network Cabling",
        "study_topics": ["T568A/B wiring"],
        "body": (
            "<p>T568A and T568B are the two wiring standards for terminating RJ-45 connectors on "
            "Cat 5e/6/6A cables. The difference is the position of the orange and green wire pairs.</p>"
            "<table border='1' cellpadding='4' cellspacing='0'>"
            "<tr><th>Pin</th><th>T568A</th><th>T568B</th></tr>"
            "<tr><td>1</td><td>White/Green</td><td>White/Orange</td></tr>"
            "<tr><td>2</td><td>Green</td><td>Orange</td></tr>"
            "<tr><td>3</td><td>White/Orange</td><td>White/Green</td></tr>"
            "<tr><td>4</td><td>Blue</td><td>Blue</td></tr>"
            "<tr><td>5</td><td>White/Blue</td><td>White/Blue</td></tr>"
            "<tr><td>6</td><td>Orange</td><td>Green</td></tr>"
            "<tr><td>7</td><td>White/Brown</td><td>White/Brown</td></tr>"
            "<tr><td>8</td><td>Brown</td><td>Brown</td></tr>"
            "</table>"
            "<p><strong>Cable types based on wiring:</strong></p>"
            "<ul>"
            "<li><strong>Straight-through (patch) cable:</strong> Both ends wired the same standard "
            "(T568B/T568B or T568A/T568A). Connects unlike devices: PC to switch, switch to router.</li>"
            "<li><strong>Crossover cable:</strong> One end T568A, other end T568B. Connects like devices: "
            "PC to PC, switch to switch (legacy — modern devices use Auto-MDIX to detect automatically).</li>"
            "<li><strong>Rollover (console) cable:</strong> Pins reversed end-to-end; connects a PC serial "
            "port to a router/switch console port (Cisco devices).</li>"
            "</ul>"
            "<p>Exam tip: <strong>T568B is the most common</strong> wiring standard in US commercial "
            "installations. Auto-MDIX on modern switches eliminates the need to use crossover cables. "
            "Always use consistent standards throughout an installation.</p>"
        ),
        "key_points": [
            "T568A: Green pair on pins 1/2; T568B: Orange pair on pins 1/2",
            "T568B is the most common US commercial standard",
            "Straight-through cable: same standard on both ends — unlike device connections",
            "Crossover cable: T568A one end, T568B other — like device connections (legacy)",
            "Auto-MDIX on modern switches detects cable type automatically",
            "Rollover/console cable: pins fully reversed; used for Cisco console access",
            "Pins 1, 2, 3, 6 carry data in 100BASE-TX/1000BASE-T; all 8 used in gigabit",
        ],
    },
    {
        "domain": 2,
        "topic": "PoE",
        "objective": "2.8",
        "video": "PoE",
        "study_topics": ["PoE"],
        "body": (
            "<p><strong>Power over Ethernet (PoE)</strong> delivers DC electrical power along with data "
            "over standard Ethernet cabling (Cat 5e or higher), eliminating the need for separate power "
            "supplies for network devices.</p>"
            "<p><strong>PoE standards:</strong></p>"
            "<table border='1' cellpadding='4' cellspacing='0'>"
            "<tr><th>Standard</th><th>IEEE</th><th>Max Power (per port)</th><th>Use Cases</th></tr>"
            "<tr><td>PoE</td><td>802.3af</td><td>15.4W (12.95W at device)</td>"
            "<td>VoIP phones, basic WAPs</td></tr>"
            "<tr><td>PoE+</td><td>802.3at</td><td>30W (25.5W at device)</td>"
            "<td>PTZ cameras, faster WAPs</td></tr>"
            "<tr><td>PoE++ (Type 3)</td><td>802.3bt</td><td>60W</td>"
            "<td>Video conferencing, multi-radio WAPs</td></tr>"
            "<tr><td>PoE++ (Type 4)</td><td>802.3bt</td><td>100W</td>"
            "<td>Laptops, thin clients</td></tr>"
            "</table>"
            "<p><strong>Delivery methods:</strong></p>"
            "<ul>"
            "<li><strong>Endspan (PoE switch):</strong> Power integrated into the switch — simplest "
            "approach for new installs</li>"
            "<li><strong>Midspan (PoE injector):</strong> Inline device inserted between a non-PoE switch "
            "and the powered device — adds PoE capability without replacing the switch</li>"
            "</ul>"
            "<p>Exam tips: PoE requires the PSE (Power Sourcing Equipment — the switch/injector) to "
            "negotiate with the PD (Powered Device) before supplying power to avoid damaging non-PoE "
            "devices. Cat 5e minimum cabling required for PoE.</p>"
        ),
        "key_points": [
            "PoE (802.3af): 15.4W — VoIP phones, basic WAPs",
            "PoE+ (802.3at): 30W — PTZ cameras, higher-power WAPs",
            "PoE++ (802.3bt): 60W (Type 3) or 100W (Type 4) — laptops, video conferencing",
            "PSE = Power Sourcing Equipment (switch or injector); PD = Powered Device",
            "Endspan: PoE switch; Midspan: inline PoE injector between switch and device",
            "Requires Cat 5e or higher cabling",
            "Negotiation before power delivery prevents damaging non-PoE equipment",
        ],
    },
    {
        "domain": 2,
        "topic": "Network services",
        "objective": "2.4",
        "video": "Network Services",
        "study_topics": ["Network services"],
        "body": (
            "<p>Core network services provide the infrastructure that IP networks depend on:</p>"
            "<ul>"
            "<li><strong>DNS (Domain Name System):</strong> Resolves hostnames to IP addresses. "
            "Runs on port 53. Hierarchical: root → TLD → authoritative → resolver.</li>"
            "<li><strong>DHCP (Dynamic Host Configuration Protocol):</strong> Automatically assigns IP "
            "configuration (IP, mask, gateway, DNS). Port 67/68 UDP.</li>"
            "<li><strong>NTP (Network Time Protocol):</strong> Synchronizes clocks across network devices. "
            "Port 123 UDP. Critical for certificate validation, log correlation, Kerberos authentication.</li>"
            "<li><strong>SNMP (Simple Network Management Protocol):</strong> Monitors and manages network "
            "devices. Agent on device responds to manager polls (port 161) and sends traps (port 162). "
            "SNMPv3 adds encryption and authentication.</li>"
            "<li><strong>Syslog:</strong> Centralized logging service. UDP port 514 (TCP for reliability). "
            "Devices send log messages to a syslog server.</li>"
            "<li><strong>LDAP (Lightweight Directory Access Protocol):</strong> Accesses directory services "
            "like Active Directory. Port 389 (636 for LDAPS with TLS).</li>"
            "<li><strong>SMB (Server Message Block):</strong> Windows file/printer sharing. Port 445 TCP. "
            "Replaced NetBIOS/CIFS.</li>"
            "<li><strong>AAA (Authentication, Authorization, Accounting):</strong> Framework for network "
            "access control. RADIUS (port 1812/1813 UDP) and TACACS+ (port 49 TCP) are common protocols.</li>"
            "</ul>"
        ),
        "key_points": [
            "DNS: port 53, resolves names to IPs",
            "DHCP: ports 67/68 UDP, auto IP configuration — DORA process",
            "NTP: port 123 UDP, time synchronization — critical for Kerberos and logs",
            "SNMP: port 161 (poll), 162 (trap) UDP; SNMPv3 adds encryption",
            "Syslog: port 514, centralized logging",
            "LDAP: port 389 (636 for LDAPS), directory access",
            "SMB: port 445 TCP, Windows file/printer sharing",
            "RADIUS: ports 1812/1813 UDP — AAA for network access",
        ],
    },
    {
        "domain": 2,
        "topic": "Network devices and their OSI-layer functions",
        "objective": "2.2",
        "video": "Network Devices",
        "study_topics": ["Network devices and their OSI-layer functions"],
        "body": (
            "<p>The OSI (Open Systems Interconnection) model has 7 layers. Network devices operate "
            "at specific layers which determine what information they process:</p>"
            "<table border='1' cellpadding='4' cellspacing='0'>"
            "<tr><th>Layer</th><th>Name</th><th>Device/Protocol</th><th>PDU</th></tr>"
            "<tr><td>7</td><td>Application</td><td>Proxy firewall, WAF, application gateway</td><td>Data</td></tr>"
            "<tr><td>6</td><td>Presentation</td><td>SSL/TLS encryption, compression</td><td>Data</td></tr>"
            "<tr><td>5</td><td>Session</td><td>NetBIOS, RPC, session management</td><td>Data</td></tr>"
            "<tr><td>4</td><td>Transport</td><td>TCP/UDP, load balancer (some)</td><td>Segment/Datagram</td></tr>"
            "<tr><td>3</td><td>Network</td><td>Router, L3 switch, packet filter firewall</td><td>Packet</td></tr>"
            "<tr><td>2</td><td>Data Link</td><td>Switch, WAP, bridge, NIC</td><td>Frame</td></tr>"
            "<tr><td>1</td><td>Physical</td><td>Hub, repeater, cable, media converter</td><td>Bits</td></tr>"
            "</table>"
            "<p><strong>Key exam associations:</strong></p>"
            "<ul>"
            "<li><strong>Hub:</strong> Layer 1 — repeats bits to all ports</li>"
            "<li><strong>Switch:</strong> Layer 2 — uses MAC addresses (frames)</li>"
            "<li><strong>Router:</strong> Layer 3 — uses IP addresses (packets)</li>"
            "<li><strong>Multilayer switch (L3 switch):</strong> Layers 2 and 3 — switches and routes</li>"
            "<li><strong>Firewall:</strong> Can operate at Layers 3–7 depending on type</li>"
            "<li><strong>WAP:</strong> Layer 2 — bridges wireless to wired (MAC addresses)</li>"
            "</ul>"
            "<p>OSI mnemonic (top to bottom): <em>All People Seem To Need Data Processing</em> "
            "(Application, Presentation, Session, Transport, Network, Data Link, Physical).</p>"
        ),
        "key_points": [
            "Layer 1 (Physical): hub, repeater, cable, media converter — bits",
            "Layer 2 (Data Link): switch, WAP, bridge — MAC addresses, frames",
            "Layer 3 (Network): router, L3 switch — IP addresses, packets",
            "Layer 4 (Transport): TCP/UDP — segments/datagrams, end-to-end delivery",
            "Layers 5–7: session, presentation, application — data",
            "Firewall can operate at L3 (packet filter), L4 (stateful), or L7 (application proxy)",
            "OSI mnemonic: All People Seem To Need Data Processing (7→1)",
        ],
    },
    {
        "domain": 2,
        "topic": "Network CLI diagnostic tools",
        "objective": "2.9",
        "video": "Network Command Line Tools",
        "study_topics": ["Network CLI diagnostic tools"],
        "body": (
            "<p>Command-line tools are essential for diagnosing network connectivity issues on the A+ exam:</p>"
            "<ul>"
            "<li><strong><code>ping</code>:</strong> Tests ICMP reachability to a host. "
            "<code>ping 8.8.8.8</code> tests internet connectivity. "
            "A failed ping to the gateway suggests a local network problem.</li>"
            "<li><strong><code>tracert</code> (Windows) / <code>traceroute</code> (Linux):</strong> "
            "Shows each hop along the path to a destination using TTL-expiring packets. "
            "Identifies where packets stop or slow down.</li>"
            "<li><strong><code>ipconfig</code> (Windows) / <code>ifconfig</code> / <code>ip addr</code> (Linux):</strong> "
            "Displays current IP configuration. "
            "<code>ipconfig /all</code> shows MAC, DHCP server, lease info. "
            "<code>ipconfig /release</code> and <code>/renew</code> forces DHCP renewal.</li>"
            "<li><strong><code>nslookup</code>:</strong> Queries DNS servers. "
            "<code>nslookup google.com</code> resolves a hostname; can target a specific DNS server.</li>"
            "<li><strong><code>netstat</code>:</strong> Displays active TCP connections, listening ports, "
            "and statistics. <code>netstat -an</code> shows all connections and listening ports.</li>"
            "<li><strong><code>arp -a</code>:</strong> Displays the ARP cache (IP-to-MAC mappings) on "
            "the local host.</li>"
            "<li><strong><code>route print</code> / <code>netstat -r</code>:</strong> Displays the "
            "local routing table.</li>"
            "<li><strong><code>net</code>:</strong> Windows command for network shares, users, "
            "services (<code>net use</code>, <code>net view</code>).</li>"
            "<li><strong><code>pathping</code> (Windows):</strong> Combines ping and tracert, "
            "shows packet loss per hop over time.</li>"
            "</ul>"
        ),
        "key_points": [
            "ping: tests ICMP reachability; failed ping to gateway = local network issue",
            "tracert/traceroute: shows hop-by-hop path; identifies where connectivity breaks",
            "ipconfig /all: shows full IP config, MAC, DHCP server, lease info",
            "ipconfig /release && /renew: forces DHCP re-lease",
            "nslookup: DNS resolution testing; can specify alternate DNS server",
            "netstat -an: shows all TCP/UDP connections and listening ports",
            "arp -a: displays IP-to-MAC mapping cache on local host",
            "pathping: combines ping + tracert with per-hop packet loss statistics",
        ],
    },
    {
        "domain": 2,
        "topic": "TCP vs UDP — transport protocol classification",
        "objective": "2.1",
        "video": "Introduction to IP",
        "study_topics": ["TCP vs UDP — transport protocol classification"],
        "body": (
            "<p>TCP and UDP are the two main Layer 4 (Transport layer) protocols. Knowing which "
            "applications use each is critical for the A+ exam.</p>"
            "<table border='1' cellpadding='4' cellspacing='0'>"
            "<tr><th>Feature</th><th>TCP</th><th>UDP</th></tr>"
            "<tr><td>Connection</td><td>Connection-oriented (3-way handshake: SYN, SYN-ACK, ACK)</td>"
            "<td>Connectionless</td></tr>"
            "<tr><td>Reliability</td><td>Guaranteed delivery, retransmission on loss</td>"
            "<td>No guarantee, no retransmission</td></tr>"
            "<tr><td>Ordering</td><td>Sequenced — data arrives in order</td><td>No ordering</td></tr>"
            "<tr><td>Speed</td><td>Slower (overhead of ACKs, handshake)</td>"
            "<td>Faster (low overhead)</td></tr>"
            "<tr><td>Use cases</td><td>Web (HTTP/HTTPS), email, file transfer, SSH, RDP</td>"
            "<td>DNS queries, DHCP, streaming, VoIP, SNMP, online gaming</td></tr>"
            "</table>"
            "<p><strong>TCP three-way handshake:</strong> Client → SYN → Server; "
            "Server → SYN-ACK → Client; Client → ACK → Server. Connection is now established.</p>"
            "<p><strong>TCP teardown (four-way):</strong> FIN, FIN-ACK, FIN, FIN-ACK.</p>"
            "<p><strong>Key protocol-transport mappings:</strong></p>"
            "<ul>"
            "<li>TCP: HTTP, HTTPS, FTP, SSH, Telnet, SMTP, POP3, IMAP, LDAP, SMB, RDP</li>"
            "<li>UDP: DNS (queries), DHCP, SNMP, TFTP, NTP, Syslog, VoIP (RTP)</li>"
            "<li>Both: DNS (zone transfers use TCP)</li>"
            "</ul>"
        ),
        "key_points": [
            "TCP: connection-oriented, reliable, ordered, slower — uses 3-way handshake",
            "UDP: connectionless, unreliable, faster — no handshake overhead",
            "TCP 3-way handshake: SYN → SYN-ACK → ACK",
            "TCP: HTTP, HTTPS, FTP, SSH, Telnet, SMTP, POP3, IMAP, SMB, RDP, LDAP",
            "UDP: DNS queries, DHCP, SNMP, TFTP, NTP, Syslog, VoIP/RTP",
            "DNS uses UDP for queries, TCP for zone transfers (both)",
            "Choose TCP when reliability matters; UDP when speed matters (streaming, gaming)",
        ],
    },
    {
        "domain": 2,
        "topic": "Configuring a new SOHO wireless network securely — setup sequence",
        "objective": "2.10",
        "video": "Configuring a SOHO Network",
        "study_topics": ["Configuring a new SOHO wireless network securely — setup sequence"],
        "body": (
            "<p>Setting up a SOHO (Small Office/Home Office) wireless router securely requires "
            "following a logical sequence of steps. The A+ exam tests this procedurally:</p>"
            "<ol>"
            "<li><strong>Change default admin credentials:</strong> Log in to the router admin interface "
            "(typically 192.168.1.1 or 192.168.0.1) and change the default username and password "
            "immediately to prevent unauthorized access.</li>"
            "<li><strong>Update firmware:</strong> Apply the latest firmware to patch known "
            "vulnerabilities before deploying.</li>"
            "<li><strong>Configure WAN settings:</strong> Set connection type (DHCP from ISP, PPPoE, "
            "static IP) to establish internet connectivity.</li>"
            "<li><strong>Configure LAN/DHCP:</strong> Set a private IP range for the LAN, configure "
            "DHCP scope, set exclusions/reservations as needed.</li>"
            "<li><strong>Set a strong SSID:</strong> Use a non-identifying SSID (don't broadcast your "
            "name/address). Avoid default SSID names that reveal router model.</li>"
            "<li><strong>Disable SSID broadcast (optional):</strong> Obscures the network but does not "
            "provide true security — determined attackers can still find hidden SSIDs.</li>"
            "<li><strong>Configure wireless security — use WPA3 or WPA2:</strong> Never use WEP (broken) "
            "or WPA (deprecated). WPA2-AES (CCMP) is minimum acceptable; WPA3 preferred. "
            "Set a strong passphrase (12+ chars, mixed types).</li>"
            "<li><strong>Change default channel:</strong> Use channels 1, 6, or 11 on 2.4 GHz; "
            "select a clear channel on 5 GHz.</li>"
            "<li><strong>Disable WPS:</strong> Wi-Fi Protected Setup has known PIN brute-force "
            "vulnerabilities — disable it.</li>"
            "<li><strong>Enable firewall / disable unnecessary services:</strong> Disable remote "
            "management, UPnP (if not needed), and unused ports.</li>"
            "<li><strong>Configure guest network:</strong> Isolate IoT and guest devices on a separate "
            "SSID/VLAN to protect the primary LAN.</li>"
            "</ol>"
            "<p><strong>Security standards reference:</strong> WEP → broken (RC4); "
            "WPA → TKIP (deprecated); WPA2 → AES/CCMP (acceptable); WPA3 → SAE (best).</p>"
        ),
        "key_points": [
            "Step 1: Change default admin username and password immediately",
            "Step 2: Update router firmware before deployment",
            "Use WPA3 (preferred) or WPA2-AES — never WEP or WPA/TKIP",
            "Disable WPS — vulnerable to PIN brute-force attacks",
            "Change default SSID — don't reveal router model or personal info",
            "Use channels 1, 6, or 11 on 2.4 GHz to avoid interference",
            "Enable guest network to isolate IoT and untrusted devices",
            "Disable remote management, UPnP, and unused services",
            "WPA2 uses AES/CCMP; WPA3 uses SAE (Simultaneous Authentication of Equals)",
        ],
    },
]

"""
CCNA 200-301 Domain 4: IP Services
Study notes covering exam objectives for domain 4.
"""

NOTES = [
    {
        "domain": 4,
        "topic": "NAT and PAT",
        "objective": "4.1",
        "video": "NAT",
        "study_topics": ["NAT/PAT"],
        "body": (
            "<p><strong>Network Address Translation (NAT)</strong> allows a router to translate "
            "private (RFC 1918) IP addresses to public routable addresses, conserving public IP "
            "space and providing a layer of address hiding.</p>"
            "<p><strong>Key address terminology:</strong></p>"
            "<ul>"
            "<li><strong>Inside Local</strong> – the private IP address assigned to an inside host "
            "(e.g., 192.168.1.10). This is how the inside host identifies itself.</li>"
            "<li><strong>Inside Global</strong> – the public IP address that represents the inside "
            "host to the outside world (e.g., 203.0.113.5).</li>"
            "<li><strong>Outside Global</strong> – the actual IP address of the remote/destination "
            "host on the internet.</li>"
            "<li><strong>Outside Local</strong> – how the outside host appears to the inside "
            "network (usually the same as Outside Global unless twice-NAT is used).</li>"
            "</ul>"
            "<p><strong>Static NAT</strong> creates a permanent one-to-one mapping between an "
            "inside local and an inside global address. Used for servers that must always be "
            "reachable via the same public IP.<br>"
            "Config: <code>ip nat inside source static 192.168.1.10 203.0.113.5</code></p>"
            "<p><strong>Dynamic NAT</strong> maps inside addresses to a pool of public addresses "
            "on a first-come, first-served basis.</p>"
            "<p><strong>PAT (Port Address Translation / NAT Overload)</strong> maps many inside "
            "local addresses to a single inside global address by tracking unique source port "
            "numbers. This is the most common form used in SOHO and enterprise edge routers.<br>"
            "Config example using an interface: "
            "<code>ip nat inside source list ACL_NAME interface GigabitEthernet0/0 overload</code></p>"
            "<p>Apply <code>ip nat inside</code> on LAN-facing interfaces and "
            "<code>ip nat outside</code> on WAN-facing interfaces.</p>"
        ),
        "key_points": [
            "Inside Local = private IP of inside host; Inside Global = public IP seen by outside world.",
            "Static NAT = 1-to-1 permanent mapping; dynamic NAT = pool-based; PAT = many-to-one using ports.",
            "PAT (overload) is the most scalable NAT type and is widely deployed.",
            "Mark LAN interface 'ip nat inside' and WAN interface 'ip nat outside'.",
            "NAT hides internal topology and helps conserve IPv4 address space.",
        ],
    },
    {
        "domain": 4,
        "topic": "NTP (Network Time Protocol)",
        "objective": "4.2",
        "video": "NTP",
        "study_topics": ["NTP"],
        "body": (
            "<p><strong>Network Time Protocol (NTP)</strong> synchronizes clocks across network "
            "devices, which is critical for log correlation, certificate validity, and "
            "authentication protocols such as Kerberos.</p>"
            "<p><strong>Stratum</strong> indicates a device's distance from an authoritative time "
            "source:</p>"
            "<ul>"
            "<li><strong>Stratum 0</strong> – atomic clocks, GPS receivers (reference clock, not "
            "reachable via NTP directly).</li>"
            "<li><strong>Stratum 1</strong> – NTP server directly connected to a stratum-0 source.</li>"
            "<li><strong>Stratum 2</strong> – synchronizes from a stratum-1 server, and so on.</li>"
            "<li>Stratum 15 is the maximum valid stratum; stratum 16 means unsynchronized.</li>"
            "</ul>"
            "<p>Each hop adds one stratum level. Lower stratum = closer to the authoritative "
            "source = more accurate.</p>"
            "<p><strong>NTP modes on Cisco IOS:</strong></p>"
            "<ul>"
            "<li><code>ntp server &lt;IP&gt;</code> – configures the device as an NTP client "
            "pointing to an upstream server.</li>"
            "<li><code>ntp master &lt;stratum&gt;</code> – makes the device an authoritative NTP "
            "server for lower-stratum peers (useful when no internet access is available).</li>"
            "<li><code>ntp peer &lt;IP&gt;</code> – symmetric active peer relationship "
            "(both devices can sync to each other).</li>"
            "</ul>"
            "<p>NTP uses UDP port 123. Use <code>show ntp status</code> and "
            "<code>show ntp associations</code> to verify synchronization.</p>"
            "<p>NTP authentication using MD5 keys can prevent rogue time sources from injecting "
            "incorrect time data.</p>"
        ),
        "key_points": [
            "Stratum 0 = atomic/GPS reference; each downstream hop increments stratum by 1.",
            "Stratum 16 means the device is not synchronized.",
            "'ntp server <IP>' makes a Cisco device an NTP client; 'ntp master' makes it authoritative.",
            "NTP uses UDP port 123.",
            "Accurate time is essential for log correlation, certificates, and Kerberos authentication.",
        ],
    },
    {
        "domain": 4,
        "topic": "DHCP and DNS Roles",
        "objective": "4.3",
        "video": "DHCP and DNS",
        "study_topics": ["DHCP & DNS roles"],
        "body": (
            "<p><strong>DHCP (Dynamic Host Configuration Protocol)</strong> automatically provides "
            "IP configuration to hosts, removing the need for manual static addressing. A DHCP "
            "server typically provides: IP address, subnet mask, default gateway, and DNS server "
            "addresses.</p>"
            "<p><strong>Cisco IOS DHCP server configuration:</strong></p>"
            "<ul>"
            "<li><code>ip dhcp pool NAME</code> – creates a pool.</li>"
            "<li><code>network 192.168.1.0 255.255.255.0</code> – defines the address range.</li>"
            "<li><code>default-router 192.168.1.1</code> – sets the gateway.</li>"
            "<li><code>dns-server 8.8.8.8</code> – sets the DNS server.</li>"
            "<li><code>ip dhcp excluded-address 192.168.1.1 192.168.1.10</code> – reserves addresses "
            "for static assignment.</li>"
            "</ul>"
            "<p><strong>DNS (Domain Name System)</strong> translates human-readable hostnames "
            "(e.g., www.example.com) into IP addresses. It functions as the internet's distributed "
            "directory service.</p>"
            "<p><strong>DNS hierarchy:</strong> Root (.) → Top-Level Domain (.com, .org) → "
            "Second-Level Domain (example.com) → Subdomain/host.</p>"
            "<p><strong>Common DNS record types:</strong></p>"
            "<ul>"
            "<li><strong>A</strong> – maps hostname to IPv4 address.</li>"
            "<li><strong>AAAA</strong> – maps hostname to IPv6 address.</li>"
            "<li><strong>CNAME</strong> – alias pointing to another hostname.</li>"
            "<li><strong>MX</strong> – mail exchanger record.</li>"
            "<li><strong>PTR</strong> – reverse DNS lookup (IP to hostname).</li>"
            "</ul>"
            "<p>DNS uses UDP port 53 for queries and TCP port 53 for zone transfers.</p>"
        ),
        "key_points": [
            "DHCP provides IP address, mask, default gateway, and DNS server to clients automatically.",
            "Use 'ip dhcp excluded-address' to prevent DHCP from assigning addresses reserved for static use.",
            "DNS translates FQDNs to IP addresses; uses UDP/TCP port 53.",
            "A record = IPv4, AAAA = IPv6, CNAME = alias, MX = mail, PTR = reverse lookup.",
            "A Cisco router can act as both a DHCP server and a DNS forwarder.",
        ],
    },
    {
        "domain": 4,
        "topic": "DHCP Relay (ip helper-address)",
        "objective": "4.3",
        "video": "DHCP Relay",
        "study_topics": ["DHCP relay (ip helper-address)"],
        "body": (
            "<p>DHCP uses broadcast messages (Discover and Request). Routers do not forward "
            "broadcasts by default, so clients on a different subnet from the DHCP server would "
            "never receive a response. The <strong>DHCP relay agent</strong> (also called IP helper) "
            "solves this by converting the client's broadcast into a unicast packet forwarded to "
            "the DHCP server.</p>"
            "<p><strong>Configuration:</strong> Apply <code>ip helper-address &lt;DHCP-server-IP&gt;</code> "
            "on the <em>router interface facing the client subnet</em> (the interface that receives "
            "the broadcast). The router then forwards the request as a unicast to the DHCP server, "
            "inserting the client's subnet information so the server can assign an appropriate "
            "address.</p>"
            "<pre><code>interface GigabitEthernet0/1\n"
            " ip address 192.168.10.1 255.255.255.0\n"
            " ip helper-address 10.0.0.5</code></pre>"
            "<p>In this example, 10.0.0.5 is the centralized DHCP server. When a client on "
            "192.168.10.0/24 broadcasts a DHCP Discover, the router relays it as a unicast to "
            "10.0.0.5, including the Gateway IP Address (giaddr) field set to the router's "
            "interface address. The server uses giaddr to determine which pool to allocate from.</p>"
            "<p><code>ip helper-address</code> also relays several other UDP services by default "
            "including TFTP (69), DNS (53), Time (37), NetBIOS (137/138), and TACACS (49). "
            "You can restrict relaying using access lists.</p>"
            "<p>Verify with <code>show ip interface GigabitEthernet0/1</code> which lists the "
            "helper address if configured.</p>"
        ),
        "key_points": [
            "DHCP uses broadcasts; 'ip helper-address' converts the broadcast to unicast so it can cross routers.",
            "Configure 'ip helper-address' on the router interface closest to the DHCP clients.",
            "The giaddr field tells the DHCP server which subnet the client is on.",
            "By default, ip helper-address relays several UDP protocols beyond just DHCP.",
            "'show ip interface <intf>' confirms the helper address is applied.",
        ],
    },
    {
        "domain": 4,
        "topic": "DHCP DORA Message Sequence",
        "objective": "4.3",
        "video": "DHCP DORA",
        "study_topics": ["DHCP DORA message sequence"],
        "body": (
            "<p>When a client needs an IP address, it follows the <strong>DORA</strong> four-step "
            "process with the DHCP server:</p>"
            "<ol>"
            "<li><strong>Discover</strong> – The client broadcasts a DHCPDISCOVER message "
            "(src: 0.0.0.0, dst: 255.255.255.255) to find available DHCP servers. The client "
            "has no IP address at this point.</li>"
            "<li><strong>Offer</strong> – One or more DHCP servers respond with a DHCPOFFER, "
            "proposing an IP address, lease duration, subnet mask, gateway, and DNS server. "
            "This is also typically a broadcast.</li>"
            "<li><strong>Request</strong> – The client broadcasts a DHCPREQUEST to formally "
            "request the offered address (and implicitly decline other offers). The broadcast "
            "informs all servers which offer was accepted.</li>"
            "<li><strong>Acknowledge</strong> – The selected server sends a DHCPACK confirming "
            "the lease. The client can now use the assigned IP configuration.</li>"
            "</ol>"
            "<p><strong>Memory aid:</strong> <em>D-O-R-A</em> — like a dancer going through "
            "steps: Discover, Offer, Request, Acknowledge.</p>"
            "<p><strong>Lease renewal:</strong> When 50% of the lease time expires, the client "
            "sends a DHCPREQUEST unicast to renew. If the server does not respond, the client "
            "tries again at 87.5%. If still no response, the client broadcasts a new Discover.</p>"
            "<p><strong>DHCPNAK</strong> – Sent by the server to reject a Request (e.g., if the "
            "offered address is no longer available), forcing the client to restart DORA.</p>"
            "<p><strong>DHCPRELEASE</strong> – Sent by the client to voluntarily return an "
            "address before the lease expires.</p>"
            "<p>All DORA messages use UDP: client source port 68, server destination port 67.</p>"
        ),
        "key_points": [
            "DORA: Discover → Offer → Request → Acknowledge.",
            "Discover and Request are client broadcasts; Offer and Acknowledge may also be broadcasts.",
            "Client uses UDP port 68; DHCP server uses UDP port 67.",
            "At 50% lease expiry the client attempts unicast renewal; at 87.5% it broadcasts again.",
            "DHCPNAK forces the client to restart DORA; DHCPRELEASE returns the address early.",
        ],
    },
    {
        "domain": 4,
        "topic": "SNMP (Simple Network Management Protocol)",
        "objective": "4.4",
        "video": "SNMP",
        "study_topics": ["SNMP"],
        "body": (
            "<p><strong>SNMP</strong> is used to monitor and manage network devices. It operates "
            "using a manager/agent model:</p>"
            "<ul>"
            "<li><strong>NMS (Network Management Station)</strong> – the manager that queries "
            "agents and receives notifications.</li>"
            "<li><strong>Agent</strong> – software running on the managed device (router, switch, "
            "server) that responds to queries and sends traps.</li>"
            "<li><strong>MIB (Management Information Base)</strong> – a hierarchical database of "
            "objects that can be monitored or configured, identified by OIDs "
            "(Object Identifiers).</li>"
            "</ul>"
            "<p><strong>SNMP versions:</strong></p>"
            "<ul>"
            "<li><strong>SNMPv1</strong> – original version, community-string authentication "
            "(plaintext), limited security.</li>"
            "<li><strong>SNMPv2c</strong> – improved performance and error handling; still uses "
            "plaintext community strings.</li>"
            "<li><strong>SNMPv3</strong> – adds authentication (MD5/SHA) and encryption "
            "(DES/AES). Three security levels: noAuthNoPriv, authNoPriv, authPriv. Recommended "
            "for production.</li>"
            "</ul>"
            "<p><strong>Key SNMP operations:</strong></p>"
            "<ul>"
            "<li><strong>Get / GetNext / GetBulk</strong> – NMS reads values from agent MIB.</li>"
            "<li><strong>Set</strong> – NMS writes a value to agent MIB (changes config).</li>"
            "<li><strong>Trap</strong> – Agent sends unsolicited notification to NMS "
            "(unreliable, no acknowledgment).</li>"
            "<li><strong>Inform</strong> – like a Trap but the NMS acknowledges receipt "
            "(more reliable, SNMPv2c/v3).</li>"
            "</ul>"
            "<p>SNMP uses UDP port 161 for Get/Set operations and UDP port 162 for traps/informs.</p>"
        ),
        "key_points": [
            "SNMP manager (NMS) queries agents; agents respond and send unsolicited traps.",
            "MIB is the database of manageable objects; each object has an OID.",
            "SNMPv1/v2c use plaintext community strings; SNMPv3 adds authentication and encryption.",
            "Trap = unreliable agent-to-manager alert; Inform = reliable (acknowledged) alert.",
            "SNMP uses UDP 161 (queries) and UDP 162 (traps/informs).",
        ],
    },
    {
        "domain": 4,
        "topic": "Syslog Severity Levels",
        "objective": "4.5",
        "video": "Syslog",
        "study_topics": ["Syslog severity levels"],
        "body": (
            "<p><strong>Syslog</strong> is the standard protocol for sending log messages from "
            "network devices to a centralized syslog server. It uses UDP port 514 by default "
            "(TCP is also supported for reliability). Each message carries a <em>severity level</em> "
            "that indicates the urgency of the event.</p>"
            "<p><strong>Syslog Severity Levels (0–7):</strong></p>"
            "<table border='1' cellpadding='4' cellspacing='0'>"
            "<tr><th>Level</th><th>Keyword</th><th>Description</th></tr>"
            "<tr><td>0</td><td>Emergency</td><td>System is unusable</td></tr>"
            "<tr><td>1</td><td>Alert</td><td>Immediate action required</td></tr>"
            "<tr><td>2</td><td>Critical</td><td>Critical hardware/software failure</td></tr>"
            "<tr><td>3</td><td>Error</td><td>Error conditions</td></tr>"
            "<tr><td>4</td><td>Warning</td><td>Warning conditions</td></tr>"
            "<tr><td>5</td><td>Notice / Notification</td><td>Normal but significant events</td></tr>"
            "<tr><td>6</td><td>Informational</td><td>Informational messages</td></tr>"
            "<tr><td>7</td><td>Debugging</td><td>Detailed debug output</td></tr>"
            "</table>"
            "<p><strong>Key rule:</strong> Lower number = higher severity. 0 (Emergency) is the "
            "most critical; 7 (Debugging) is the least.</p>"
            "<p><strong>Mnemonic:</strong> <em>\"Every Awesome Cisco Engineer Will Need Ice Daily\"</em> "
            "→ Emergency, Alert, Critical, Error, Warning, Notice, Informational, Debugging.</p>"
            "<p><strong>logging trap N</strong> – sets the severity threshold for messages sent "
            "to the syslog server. The router sends messages at severity N <em>and all lower "
            "numbered (more severe) levels</em>. For example, <code>logging trap 4</code> sends "
            "levels 0, 1, 2, 3, and 4 (Emergency through Warning).</p>"
            "<p>Other useful commands: <code>logging host &lt;IP&gt;</code> sets the syslog "
            "server; <code>logging buffered</code> stores logs in router RAM; "
            "<code>logging console</code> controls console output level.</p>"
        ),
        "key_points": [
            "8 severity levels: 0=Emergency (most severe) through 7=Debugging (least severe).",
            "Mnemonic: 'Every Awesome Cisco Engineer Will Need Ice Daily' (0–7).",
            "Lower number = higher severity; 0 is most critical.",
            "'logging trap N' sends messages at level N and all lower-numbered (more severe) levels.",
            "Syslog uses UDP 514 by default; 'logging host <IP>' directs logs to a syslog server.",
        ],
    },
    {
        "domain": 4,
        "topic": "QoS: Classification, Marking, and Queuing",
        "objective": "4.6",
        "video": "QoS",
        "study_topics": ["QoS (classification/marking/queuing)"],
        "body": (
            "<p><strong>Quality of Service (QoS)</strong> refers to mechanisms that manage "
            "bandwidth, delay, jitter, and packet loss to ensure that high-priority traffic "
            "(like VoIP or video) receives preferential treatment over lower-priority traffic.</p>"
            "<p><strong>QoS steps (the QoS toolbox):</strong></p>"
            "<ul>"
            "<li><strong>Classification</strong> – identifying and grouping traffic. Can be "
            "done by source/destination IP, protocol, port number, DSCP value, or using "
            "NBAR (deep packet inspection to identify applications).</li>"
            "<li><strong>Marking</strong> – tagging packets so downstream devices can quickly "
            "classify without deep inspection. Common marking fields:"
            "<ul>"
            "<li><strong>DSCP (Differentiated Services Code Point)</strong> – 6 bits in the "
            "IP header. Common values: EF (46) for VoIP, AF (assured forwarding), CS classes.</li>"
            "<li><strong>CoS (Class of Service)</strong> – 3 bits in the 802.1Q VLAN tag "
            "(Layer 2, only on trunk/access links that carry 802.1Q).</li>"
            "<li><strong>IP Precedence</strong> – older 3-bit field in IP header (superseded "
            "by DSCP).</li>"
            "</ul></li>"
            "<li><strong>Queuing / Scheduling</strong> – managing which packets are sent first "
            "when a link is congested. Common queuing methods:"
            "<ul>"
            "<li><strong>FIFO</strong> – first in, first out; no prioritization (default).</li>"
            "<li><strong>PQ (Priority Queuing)</strong> – strict priority; low-priority queues "
            "can starve if high-priority queue is always full.</li>"
            "<li><strong>CBWFQ (Class-Based Weighted Fair Queuing)</strong> – guarantees "
            "minimum bandwidth per class.</li>"
            "<li><strong>LLQ (Low Latency Queuing)</strong> – CBWFQ plus a strict priority "
            "queue; recommended for VoIP.</li>"
            "</ul></li>"
            "</ul>"
            "<p><strong>Policing vs. Shaping:</strong> Policing drops or re-marks traffic that "
            "exceeds a rate; shaping buffers excess traffic and sends it later (smoothing "
            "bursts).</p>"
            "<p>QoS is configured using Cisco's <strong>MQC (Modular QoS CLI)</strong>: "
            "class-map → policy-map → service-policy.</p>"
        ),
        "key_points": [
            "QoS manages bandwidth, delay, jitter, and loss for prioritized traffic delivery.",
            "Classification identifies traffic; marking tags it (DSCP in IP header, CoS in 802.1Q).",
            "DSCP EF (46) is used for VoIP; AF classes for other high-priority traffic.",
            "LLQ = CBWFQ + strict priority queue; best practice for real-time traffic like VoIP.",
            "Policing drops excess traffic; shaping buffers and delays it.",
            "MQC: class-map (match traffic) → policy-map (define actions) → service-policy (apply to interface).",
        ],
    },
    {
        "domain": 4,
        "topic": "SSH Remote Access",
        "objective": "4.7",
        "video": "SSH",
        "study_topics": ["SSH remote access"],
        "body": (
            "<p><strong>SSH (Secure Shell)</strong> provides encrypted remote management of "
            "Cisco devices over TCP port 22. It replaces insecure Telnet (TCP 23) which sends "
            "all data including passwords in plaintext.</p>"
            "<p><strong>SSH prerequisites on Cisco IOS:</strong></p>"
            "<ol>"
            "<li>Set a hostname (not the default 'Router'): <code>hostname &lt;NAME&gt;</code></li>"
            "<li>Set a domain name: <code>ip domain-name &lt;example.com&gt;</code></li>"
            "<li>Generate RSA keys (minimum 1024 bits for SSH v2, 2048 recommended):<br>"
            "<code>crypto key generate rsa modulus 2048</code></li>"
            "<li>Create a local user account: "
            "<code>username admin privilege 15 secret &lt;password&gt;</code></li>"
            "<li>Enable SSH version 2: <code>ip ssh version 2</code></li>"
            "<li>Configure VTY lines to use SSH and local authentication:<br>"
            "<code>line vty 0 15</code><br>"
            "<code> transport input ssh</code><br>"
            "<code> login local</code></li>"
            "</ol>"
            "<p><strong>SSH v1 vs. v2:</strong> SSH version 2 is more secure due to stronger "
            "integrity checking and does not share the same key for both host authentication and "
            "encryption. Always use SSHv2.</p>"
            "<p><strong>Verification commands:</strong></p>"
            "<ul>"
            "<li><code>show ip ssh</code> – shows SSH version and status.</li>"
            "<li><code>show ssh</code> – shows active SSH sessions.</li>"
            "</ul>"
            "<p>Setting <code>transport input ssh</code> (without 'telnet') prevents Telnet "
            "connections on VTY lines, enforcing encrypted access only.</p>"
            "<p>Use <code>ip ssh time-out</code> and <code>ip ssh authentication-retries</code> "
            "to harden against brute-force attempts.</p>"
        ),
        "key_points": [
            "SSH uses TCP port 22 and encrypts all data; Telnet (TCP 23) sends data in plaintext.",
            "SSH requires: hostname, domain name, RSA keys (≥1024 bits), and local credentials.",
            "'ip ssh version 2' enforces the more secure SSHv2.",
            "'transport input ssh' on VTY lines disables Telnet and allows SSH only.",
            "'show ip ssh' and 'show ssh' verify SSH configuration and active sessions.",
        ],
    },
    {
        "domain": 4,
        "topic": "TFTP and FTP",
        "objective": "4.8",
        "video": "TFTP and FTP",
        "study_topics": ["TFTP/FTP"],
        "body": (
            "<p><strong>TFTP (Trivial File Transfer Protocol)</strong> and "
            "<strong>FTP (File Transfer Protocol)</strong> are used to transfer files such as "
            "IOS images and configuration files to/from Cisco devices.</p>"
            "<p><strong>TFTP:</strong></p>"
            "<ul>"
            "<li>Uses UDP port 69 — lightweight and connectionless.</li>"
            "<li>No authentication, no directory listing, no encryption.</li>"
            "<li>Used for simple transfers in trusted/lab environments (IOS upgrades, config "
            "backup).</li>"
            "<li>Example: <code>copy tftp flash</code> – copies an IOS image from a TFTP server "
            "to the router's flash memory.</li>"
            "<li>Example: <code>copy running-config tftp</code> – backs up the running config.</li>"
            "</ul>"
            "<p><strong>FTP:</strong></p>"
            "<ul>"
            "<li>Uses TCP port 21 for control (commands) and TCP port 20 for data (active mode).</li>"
            "<li>Supports authentication (username/password), directory browsing, and multiple "
            "transfer modes.</li>"
            "<li>More feature-rich than TFTP but still sends credentials in plaintext — "
            "use SFTP or SCP for secure transfers.</li>"
            "<li>IOS can act as an FTP client: <code>ip ftp username &lt;user&gt;</code> and "
            "<code>ip ftp password &lt;pass&gt;</code> set credentials; then "
            "<code>copy ftp://server/file flash:</code> downloads a file.</li>"
            "</ul>"
            "<p><strong>Comparison:</strong></p>"
            "<table border='1' cellpadding='4' cellspacing='0'>"
            "<tr><th>Feature</th><th>TFTP</th><th>FTP</th></tr>"
            "<tr><td>Transport</td><td>UDP 69</td><td>TCP 20/21</td></tr>"
            "<tr><td>Authentication</td><td>None</td><td>Username/Password</td></tr>"
            "<tr><td>Directory listing</td><td>No</td><td>Yes</td></tr>"
            "<tr><td>Reliability</td><td>Unreliable (UDP)</td><td>Reliable (TCP)</td></tr>"
            "<tr><td>Security</td><td>None</td><td>Plaintext creds</td></tr>"
            "</table>"
        ),
        "key_points": [
            "TFTP uses UDP port 69; simple, no authentication — suitable for trusted lab environments.",
            "FTP uses TCP port 21 (control) and TCP port 20 (data in active mode).",
            "FTP supports authentication and directory listing; TFTP does not.",
            "'copy tftp flash' and 'copy running-config tftp' are common TFTP operations on IOS.",
            "Neither TFTP nor standard FTP encrypts data; use SCP/SFTP for secure transfers.",
        ],
    },
]

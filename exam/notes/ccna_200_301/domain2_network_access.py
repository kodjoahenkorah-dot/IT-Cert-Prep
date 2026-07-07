"""
CCNA 200-301 Domain 2: Network Access
Comprehensive study notes — original content, not copied from any copyrighted source.
"""

NOTES = [
    {
        "domain": 2,
        "topic": "VLANs",
        "objective": "2.1",
        "video": "VLANs",
        "study_topics": ["VLANs"],
        "body": (
            "<p>A <strong>VLAN (Virtual LAN)</strong> is a logical grouping of devices on a Layer 2 network, "
            "independent of physical location. VLANs segment broadcast domains, improving security and performance.</p>"
            "<p><strong>Key VLAN types:</strong></p>"
            "<ul>"
            "<li><strong>Data VLAN</strong> — carries user-generated traffic.</li>"
            "<li><strong>Voice VLAN</strong> — dedicated to VoIP traffic, enabling QoS prioritization.</li>"
            "<li><strong>Management VLAN</strong> — used for switch management (SSH/Telnet/SNMP). Should not be VLAN 1.</li>"
            "<li><strong>Native VLAN</strong> — untagged traffic on an 802.1Q trunk. Both ends must match to avoid mismatches.</li>"
            "<li><strong>Default VLAN</strong> — VLAN 1 on Cisco switches; all ports belong to it by default.</li>"
            "</ul>"
            "<p><strong>VLAN ranges:</strong></p>"
            "<ul>"
            "<li>Normal range: 1–1005 (stored in flash:vlan.dat)</li>"
            "<li>Extended range: 1006–4094 (requires VTP transparent mode or VTP version 3)</li>"
            "</ul>"
            "<p><strong>Access port configuration:</strong></p>"
            "<pre>switchport mode access\nswitchport access vlan 10</pre>"
            "<p><strong>Voice VLAN on an access port:</strong></p>"
            "<pre>switchport mode access\nswitchport access vlan 10\nswitchport voice vlan 20</pre>"
            "<p>VLANs are stored locally on each switch. VTP (VLAN Trunking Protocol) can propagate VLAN "
            "definitions, but is not required. Inter-VLAN routing requires either a router-on-a-stick "
            "configuration or a Layer 3 switch with SVIs (Switched Virtual Interfaces).</p>"
            "<p><strong>Show commands:</strong></p>"
            "<ul>"
            "<li><code>show vlan brief</code> — lists VLANs and assigned ports</li>"
            "<li><code>show interfaces switchport</code> — shows mode and VLAN assignment per interface</li>"
            "</ul>"
        ),
        "key_points": [
            "VLANs create separate broadcast domains on a single physical switch.",
            "VLAN 1 is the default VLAN and native VLAN on Cisco switches; best practice is to change both.",
            "Normal-range VLANs (1–1005) are stored in vlan.dat; extended-range (1006–4094) requires VTP transparent or v3.",
            "Access ports belong to a single VLAN; voice VLAN can be added for IP phones.",
            "Inter-VLAN routing requires a Layer 3 device (router or L3 switch with SVIs).",
            "Management VLAN should be a dedicated VLAN, not VLAN 1, for security.",
        ],
    },
    {
        "domain": 2,
        "topic": "Trunking & 802.1Q",
        "objective": "2.1",
        "video": "Trunking & 802.1Q",
        "study_topics": ["Trunking & 802.1Q"],
        "body": (
            "<p>A <strong>trunk link</strong> carries traffic from multiple VLANs between switches, routers, "
            "or between a switch and a router. The IEEE <strong>802.1Q</strong> standard defines how VLAN "
            "tags are inserted into Ethernet frames.</p>"
            "<p><strong>802.1Q Frame Tagging:</strong> A 4-byte tag is inserted into the Ethernet frame "
            "header between the Source MAC address and the EtherType field. The tag contains:</p>"
            "<ul>"
            "<li><strong>TPID</strong> (Tag Protocol Identifier) — 0x8100, identifies the frame as 802.1Q tagged.</li>"
            "<li><strong>PCP</strong> (Priority Code Point) — 3 bits for QoS (Class of Service).</li>"
            "<li><strong>DEI</strong> (Drop Eligible Indicator) — 1 bit.</li>"
            "<li><strong>VID</strong> (VLAN Identifier) — 12 bits, supports VLANs 0–4095.</li>"
            "</ul>"
            "<p><strong>Native VLAN:</strong> Frames on the native VLAN traverse the trunk <em>untagged</em>. "
            "Both sides of a trunk must agree on the native VLAN; a mismatch causes a CDP warning and can "
            "create a security vulnerability (VLAN hopping). The native VLAN should be changed from VLAN 1.</p>"
            "<p><strong>Trunk Configuration on Cisco IOS:</strong></p>"
            "<pre>switchport mode trunk\nswitchport trunk encapsulation dot1q\nswitchport trunk native vlan 99\nswitchport trunk allowed vlan 10,20,30,99</pre>"
            "<p><strong>DTP (Dynamic Trunking Protocol)</strong> negotiates trunk formation automatically. "
            "Modes: <em>dynamic auto</em> (passive) and <em>dynamic desirable</em> (active). "
            "Best practice is to disable DTP with <code>switchport nonegotiate</code> on trunk ports.</p>"
            "<p><strong>Router-on-a-Stick:</strong> A router with subinterfaces, each tagged for a VLAN, "
            "provides inter-VLAN routing over a single trunk link:</p>"
            "<pre>interface G0/0.10\n encapsulation dot1q 10\n ip address 192.168.10.1 255.255.255.0</pre>"
            "<p><strong>Show commands:</strong></p>"
            "<ul>"
            "<li><code>show interfaces trunk</code> — displays trunk ports, allowed VLANs, and native VLAN.</li>"
            "<li><code>show interfaces switchport</code> — shows encapsulation and trunking mode.</li>"
            "</ul>"
        ),
        "key_points": [
            "802.1Q inserts a 4-byte tag into the Ethernet frame to identify the VLAN.",
            "The native VLAN is sent untagged across a trunk; mismatched native VLANs cause connectivity and security issues.",
            "DTP should be disabled on production trunk ports using 'switchport nonegotiate'.",
            "Trunk ports carry multiple VLANs; use 'switchport trunk allowed vlan' to restrict which VLANs traverse the trunk.",
            "Router-on-a-stick uses subinterfaces with 802.1Q encapsulation for inter-VLAN routing.",
            "ISL (Cisco proprietary) is legacy; 802.1Q is the current standard for VLAN tagging.",
        ],
    },
    {
        "domain": 2,
        "topic": "CDP & LLDP",
        "objective": "2.3",
        "video": "CDP & LLDP",
        "study_topics": ["CDP & LLDP"],
        "body": (
            "<p><strong>CDP (Cisco Discovery Protocol)</strong> is a Cisco-proprietary Layer 2 protocol "
            "that enables Cisco devices to discover directly connected neighbors. It operates on the data "
            "link layer and is media- and protocol-independent.</p>"
            "<p><strong>CDP key facts:</strong></p>"
            "<ul>"
            "<li>Enabled globally and per-interface by default on Cisco devices.</li>"
            "<li>Sends advertisements every <strong>60 seconds</strong>; hold time is <strong>180 seconds</strong>.</li>"
            "<li>Advertises: device ID, IP addresses, platform, capabilities, IOS version, native VLAN, duplex.</li>"
            "<li>Disable globally: <code>no cdp run</code>; disable per interface: <code>no cdp enable</code>.</li>"
            "</ul>"
            "<p><strong>CDP show commands:</strong></p>"
            "<ul>"
            "<li><code>show cdp neighbors</code> — summarizes neighbor device ID, local/remote ports, capabilities, platform.</li>"
            "<li><code>show cdp neighbors detail</code> — adds IP addresses and IOS version.</li>"
            "<li><code>show cdp</code> — shows global CDP timer and hold-time settings.</li>"
            "</ul>"
            "<p><strong>LLDP (Link Layer Discovery Protocol)</strong> is the IEEE 802.1AB open standard "
            "equivalent of CDP. It is vendor-neutral and supported across multi-vendor environments.</p>"
            "<p><strong>LLDP key facts:</strong></p>"
            "<ul>"
            "<li>Disabled by default on Cisco devices; must be enabled with <code>lldp run</code>.</li>"
            "<li>Sends advertisements every <strong>30 seconds</strong>; hold time is <strong>120 seconds</strong>.</li>"
            "<li>Can be configured to transmit only (<code>lldp transmit</code>) or receive only (<code>lldp receive</code>) per interface.</li>"
            "<li>Carries TLVs (Type-Length-Values): chassis ID, port ID, TTL, system name, capabilities, management address.</li>"
            "</ul>"
            "<p><strong>LLDP show commands:</strong></p>"
            "<ul>"
            "<li><code>show lldp neighbors</code> — summarizes LLDP neighbor information.</li>"
            "<li><code>show lldp neighbors detail</code> — detailed LLDP neighbor info including IP.</li>"
            "</ul>"
            "<p><strong>Security note:</strong> Both CDP and LLDP can reveal network topology to attackers; "
            "disable on interfaces facing untrusted networks (e.g., user-facing ports, internet links).</p>"
        ),
        "key_points": [
            "CDP is Cisco-proprietary; LLDP (802.1AB) is the open-standard equivalent.",
            "CDP is on by default; LLDP is off by default on Cisco devices.",
            "CDP timer: 60s / hold-time: 180s. LLDP timer: 30s / hold-time: 120s.",
            "CDP/LLDP operate at Layer 2 and discover only directly connected neighbors.",
            "Disable CDP/LLDP on untrusted interfaces to prevent topology disclosure.",
            "'show cdp neighbors detail' reveals neighbor IP addresses and IOS version.",
        ],
    },
    {
        "domain": 2,
        "topic": "EtherChannel",
        "objective": "2.2",
        "video": "EtherChannel",
        "study_topics": ["EtherChannel"],
        "body": (
            "<p><strong>EtherChannel</strong> bundles multiple physical Ethernet links into a single logical "
            "interface, providing increased bandwidth and redundancy while preventing Spanning Tree from "
            "blocking redundant links. From STP's perspective, the bundle appears as one link.</p>"
            "<p><strong>EtherChannel protocols:</strong></p>"
            "<ul>"
            "<li><strong>LACP (Link Aggregation Control Protocol)</strong> — IEEE 802.3ad/802.1AX, open standard. "
            "Modes: <em>active</em> (initiates negotiation) and <em>passive</em> (responds only). "
            "Active–active or active–passive will form a channel; passive–passive will not.</li>"
            "<li><strong>PAgP (Port Aggregation Protocol)</strong> — Cisco proprietary. "
            "Modes: <em>desirable</em> (initiates) and <em>auto</em> (responds). "
            "Desirable–desirable or desirable–auto will form a channel; auto–auto will not.</li>"
            "<li><strong>Static (On mode)</strong> — no negotiation protocol; both sides must be set to <em>on</em>. "
            "On–on forms a channel; on with LACP/PAgP will not.</li>"
            "</ul>"
            "<p><strong>Requirements for EtherChannel formation:</strong> All member ports must have matching "
            "speed, duplex, VLAN mode (access or trunk), allowed VLANs, native VLAN, and STP port settings.</p>"
            "<p><strong>Configuration example (LACP):</strong></p>"
            "<pre>interface range G0/1 - 2\n channel-group 1 mode active\ninterface port-channel 1\n switchport mode trunk</pre>"
            "<p><strong>Load balancing:</strong> Traffic is distributed across member links using a hash of "
            "selectable parameters: source/destination MAC, IP address, or TCP/UDP port. "
            "Configure with: <code>port-channel load-balance src-dst-mac</code></p>"
            "<p><strong>EtherChannel provides up to 8 active links</strong> (LACP supports 8 active + 8 standby).</p>"
            "<p><strong>Show commands:</strong></p>"
            "<ul>"
            "<li><code>show etherchannel summary</code> — displays port-channel status and member ports.</li>"
            "<li><code>show etherchannel port-channel</code> — detailed port-channel information.</li>"
            "<li><code>show interfaces port-channel 1</code> — logical interface statistics.</li>"
            "</ul>"
        ),
        "key_points": [
            "EtherChannel bundles up to 8 links into one logical interface; STP sees it as a single link.",
            "LACP (IEEE 802.3ad) modes: active/passive. PAgP (Cisco) modes: desirable/auto.",
            "All member ports must match in speed, duplex, VLAN configuration, and STP settings.",
            "Static 'on' mode requires both sides set to 'on'; mixing 'on' with LACP/PAgP prevents channel formation.",
            "Load balancing is based on a configurable hash (MAC, IP, or port-based).",
            "'show etherchannel summary' is the key verification command.",
        ],
    },
    {
        "domain": 2,
        "topic": "Spanning Tree Protocol",
        "objective": "2.4",
        "video": "Spanning Tree (RPVST+)",
        "study_topics": [
            "Spanning Tree (RPVST+)",
            "STP port roles & states",
            "802.1D Spanning Tree port state transitions",
            "Spanning Tree Protocol terminology",
        ],
        "body": (
            "<p><strong>Spanning Tree Protocol (STP)</strong> prevents Layer 2 loops in switched networks "
            "by placing redundant ports into a blocking state, creating a loop-free logical topology.</p>"
            "<h4>STP Versions</h4>"
            "<ul>"
            "<li><strong>802.1D STP</strong> — original standard; one instance for all VLANs; slow convergence (30–50 s).</li>"
            "<li><strong>PVST+</strong> — Cisco enhancement; per-VLAN STP instance; allows load balancing across VLANs.</li>"
            "<li><strong>802.1w RSTP</strong> — Rapid STP; much faster convergence (1–2 s); backwards compatible with 802.1D.</li>"
            "<li><strong>RPVST+ (Rapid Per-VLAN Spanning Tree Plus)</strong> — Cisco default on modern switches; "
            "runs an independent RSTP instance per VLAN, combining fast convergence with per-VLAN flexibility.</li>"
            "<li><strong>802.1s MST</strong> — Multiple Spanning Tree; maps multiple VLANs to fewer STP instances.</li>"
            "</ul>"
            "<h4>Root Bridge Election</h4>"
            "<p>The switch with the <strong>lowest Bridge ID</strong> becomes the root bridge. "
            "Bridge ID = <em>Priority</em> (16-bit) + <em>MAC address</em> (48-bit). "
            "Default priority is <strong>32768</strong> (+ VLAN ID in PVST+/RPVST+). "
            "To influence root election: <code>spanning-tree vlan 10 priority 4096</code> or "
            "<code>spanning-tree vlan 10 root primary</code> (sets priority to 24576 or lower).</p>"
            "<h4>Port Roles</h4>"
            "<table border='1' cellpadding='4'>"
            "<tr><th>Role</th><th>Description</th></tr>"
            "<tr><td><strong>Root Port (RP)</strong></td><td>Non-root switch port with lowest cost path to root bridge. One per non-root switch.</td></tr>"
            "<tr><td><strong>Designated Port (DP)</strong></td><td>Port that forwards traffic toward the root on each segment. One per segment.</td></tr>"
            "<tr><td><strong>Non-Designated / Alternate Port</strong></td><td>Blocking port; prevents loops. In RSTP called Alternate or Backup.</td></tr>"
            "</table>"
            "<p>All ports on the root bridge are designated ports.</p>"
            "<h4>Path Cost</h4>"
            "<p>STP uses port cost to determine the best path to the root. Default costs: "
            "10 Gbps = 2, 1 Gbps = 4, 100 Mbps = 19, 10 Mbps = 100 (short path cost values).</p>"
            "<h4>802.1D Port States (5 states)</h4>"
            "<table border='1' cellpadding='4'>"
            "<tr><th>State</th><th>Duration</th><th>Forwards Data?</th><th>Learns MACs?</th></tr>"
            "<tr><td>Blocking</td><td>Max Age: 20 s</td><td>No</td><td>No</td></tr>"
            "<tr><td>Listening</td><td>Forward Delay: 15 s</td><td>No</td><td>No</td></tr>"
            "<tr><td>Learning</td><td>Forward Delay: 15 s</td><td>No</td><td>Yes</td></tr>"
            "<tr><td>Forwarding</td><td>Normal operation</td><td>Yes</td><td>Yes</td></tr>"
            "<tr><td>Disabled</td><td>Administratively off</td><td>No</td><td>No</td></tr>"
            "</table>"
            "<p>Total 802.1D convergence time (Blocking → Forwarding) = up to <strong>50 seconds</strong> "
            "(20 s Max Age + 15 s Listening + 15 s Learning).</p>"
            "<h4>RSTP Port States (3 states) and Roles</h4>"
            "<p>RSTP consolidates 802.1D states into three: <strong>Discarding</strong> (combines Blocking/Listening/Disabled), "
            "<strong>Learning</strong>, and <strong>Forwarding</strong>. "
            "RSTP adds the <em>Alternate</em> port (backup to root port) and <em>Backup</em> port (redundant designated port on a shared segment). "
            "RSTP uses proposal/agreement handshake for rapid convergence without relying on timers.</p>"
            "<h4>Key STP Terminology</h4>"
            "<ul>"
            "<li><strong>BPDU (Bridge Protocol Data Unit)</strong> — STP control messages; sent every 2 s (Hello Time).</li>"
            "<li><strong>Hello Time</strong> — 2 seconds (interval between BPDUs from root).</li>"
            "<li><strong>Max Age</strong> — 20 seconds (how long a port stores a BPDU before discarding).</li>"
            "<li><strong>Forward Delay</strong> — 15 seconds (time spent in Listening and Learning states each).</li>"
            "<li><strong>Bridge ID</strong> — priority + MAC address; lowest wins root election.</li>"
            "<li><strong>Root Cost</strong> — accumulated cost from a switch to the root bridge.</li>"
            "</ul>"
        ),
        "key_points": [
            "Root bridge is elected by lowest Bridge ID (priority + MAC); default priority is 32768.",
            "802.1D has 5 port states: Blocking, Listening, Learning, Forwarding, Disabled; convergence up to 50 s.",
            "RSTP (802.1w) has 3 states: Discarding, Learning, Forwarding; converges in ~1–2 s via proposal/agreement.",
            "RPVST+ (Cisco default) runs a separate RSTP instance per VLAN, enabling per-VLAN load balancing.",
            "Port roles: Root Port (best path to root), Designated Port (forwarding on segment), Alternate/Non-Designated (blocking).",
            "All ports on the root bridge are designated ports in forwarding state.",
            "STP timers: Hello=2s, Max Age=20s, Forward Delay=15s.",
            "Use 'spanning-tree vlan X root primary' or a lower priority to influence root bridge election.",
        ],
    },
    {
        "domain": 2,
        "topic": "PortFast & BPDU Guard",
        "objective": "2.4",
        "video": "PortFast & BPDU Guard",
        "study_topics": ["PortFast & BPDU Guard"],
        "body": (
            "<p><strong>PortFast</strong> and <strong>BPDU Guard</strong> are Cisco STP enhancements "
            "designed for access ports connected to end devices (PCs, printers, servers).</p>"
            "<h4>PortFast</h4>"
            "<p>PortFast causes a port to immediately transition from Blocking to Forwarding, "
            "bypassing the Listening and Learning states. This eliminates the 30-second delay that "
            "would otherwise prevent devices from obtaining DHCP leases or logging in immediately after "
            "connecting.</p>"
            "<p><strong>When to use:</strong> Only on access ports connected to end devices — never on "
            "ports connected to other switches or hubs, as this could create a temporary loop.</p>"
            "<p><strong>Configuration:</strong></p>"
            "<ul>"
            "<li>Per-interface: <code>spanning-tree portfast</code></li>"
            "<li>Global default for all access ports: <code>spanning-tree portfast default</code></li>"
            "</ul>"
            "<p>PortFast ports still send and receive BPDUs. If a BPDU arrives on a PortFast port, "
            "the port reverts to normal STP operation (unless BPDU Guard is also enabled).</p>"
            "<h4>BPDU Guard</h4>"
            "<p>BPDU Guard protects the network by <strong>err-disabling</strong> a PortFast-enabled port "
            "if any BPDU is received on it. This prevents unauthorized switches or hubs from being "
            "connected and potentially altering the STP topology.</p>"
            "<p><strong>Configuration:</strong></p>"
            "<ul>"
            "<li>Per-interface: <code>spanning-tree bpduguard enable</code></li>"
            "<li>Global (applies to all PortFast-enabled ports): <code>spanning-tree portfast bpduguard default</code></li>"
            "</ul>"
            "<p>When a port is err-disabled, it must be manually re-enabled or configured with "
            "<code>errdisable recovery cause bpduguard</code> for automatic recovery.</p>"
            "<h4>BPDU Filter</h4>"
            "<p><strong>BPDU Filter</strong> stops a port from sending or processing BPDUs. "
            "Unlike BPDU Guard (which err-disables), BPDU Filter simply suppresses BPDUs. "
            "Use with caution — globally applied BPDU Filter still listens for BPDUs and disables PortFast "
            "if one is received, but interface-level BPDU Filter completely ignores BPDUs and can cause loops.</p>"
            "<h4>Root Guard</h4>"
            "<p><strong>Root Guard</strong> prevents a port from becoming a root port. If a superior BPDU "
            "is received on a Root Guard–enabled port, the port is placed in a <em>root-inconsistent</em> "
            "state (effectively blocking), protecting the current root bridge placement.</p>"
            "<pre>spanning-tree guard root</pre>"
            "<p><strong>Verification:</strong></p>"
            "<ul>"
            "<li><code>show spanning-tree</code> — shows port roles, states, and PortFast status.</li>"
            "<li><code>show interfaces status err-disabled</code> — shows err-disabled ports.</li>"
            "</ul>"
        ),
        "key_points": [
            "PortFast skips Listening and Learning states, allowing immediate forwarding — use only on end-device access ports.",
            "BPDU Guard err-disables a port if any BPDU is received; protects against unauthorized switch connections.",
            "Best practice: enable both PortFast and BPDU Guard on all access ports facing end devices.",
            "Global PortFast: 'spanning-tree portfast default'; global BPDU Guard: 'spanning-tree portfast bpduguard default'.",
            "Err-disabled ports require manual recovery or configured 'errdisable recovery' to come back up.",
            "Root Guard prevents ports from becoming root ports by blocking superior BPDUs (root-inconsistent state).",
            "BPDU Filter suppresses BPDUs; interface-level application can cause loops — use carefully.",
        ],
    },
    {
        "domain": 2,
        "topic": "Wireless Architectures & AP Modes",
        "objective": "2.6",
        "video": "Wireless architectures & AP modes",
        "study_topics": ["Wireless architectures & AP modes"],
        "body": (
            "<p>Cisco wireless networks can be deployed in several architectures depending on scale, "
            "management needs, and features required.</p>"
            "<h4>Wireless AP Deployment Architectures</h4>"
            "<table border='1' cellpadding='4'>"
            "<tr><th>Architecture</th><th>Description</th><th>Use Case</th></tr>"
            "<tr><td><strong>Autonomous AP</strong></td><td>Self-contained; all WLAN functions performed locally on the AP. "
            "Managed individually via CLI or GUI. No WLC required.</td>"
            "<td>Small deployments; no central management.</td></tr>"
            "<tr><td><strong>Lightweight AP (LWAP)</strong></td><td>Split-MAC architecture: AP handles real-time RF functions "
            "(beacons, ACKs, encryption); WLC handles management, roaming, security, QoS. "
            "AP and WLC communicate via <strong>CAPWAP</strong> tunnels (UDP 5246/5247).</td>"
            "<td>Medium to large enterprise deployments.</td></tr>"
            "<tr><td><strong>FlexConnect AP</strong></td><td>A lightweight AP that can locally switch traffic and perform "
            "authentication even when WLC connectivity is lost (<em>standalone mode</em>). "
            "In <em>connected mode</em>, operates like a standard LWAP.</td>"
            "<td>Branch offices with unreliable WAN to WLC.</td></tr>"
            "</table>"
            "<h4>Split-MAC (CAPWAP) Architecture Detail</h4>"
            "<p>In lightweight mode, the MAC functions are split between the AP and the WLC:</p>"
            "<ul>"
            "<li><strong>AP handles:</strong> Beacons, probe responses, frame encryption/decryption, ACKs, real-time 802.11 functions.</li>"
            "<li><strong>WLC handles:</strong> Authentication, association decisions, roaming, RF management, security policies.</li>"
            "</ul>"
            "<p>CAPWAP uses two tunnels: a <strong>control tunnel</strong> (UDP 5246, DTLS encrypted) and a "
            "<strong>data tunnel</strong> (UDP 5247, optionally encrypted). All client data is tunneled to the WLC "
            "for central switching (unless FlexConnect local switching is used).</p>"
            "<h4>AP Modes in Lightweight Deployment</h4>"
            "<ul>"
            "<li><strong>Local mode</strong> — default; serves clients while scanning off-channels for rogue APs and interference.</li>"
            "<li><strong>Monitor mode</strong> — dedicated to passive scanning; does not serve clients.</li>"
            "<li><strong>Sniffer mode</strong> — captures 802.11 frames and sends to a protocol analyzer (e.g., Wireshark).</li>"
            "<li><strong>Rogue Detector mode</strong> — correlates rogue AP reports by monitoring wired network.</li>"
            "<li><strong>SE-Connect mode</strong> — dedicated spectrum analysis (CleanAir).</li>"
            "<li><strong>Bridge/Mesh mode</strong> — provides wireless backhaul or point-to-point links.</li>"
            "</ul>"
            "<h4>Wireless Frequency Bands</h4>"
            "<p>802.11a/n/ac use <strong>5 GHz</strong>; 802.11b/g/n use <strong>2.4 GHz</strong>. "
            "802.11ax (Wi-Fi 6) operates on both bands. 2.4 GHz has longer range but more interference; "
            "5 GHz has shorter range but more channels and less congestion.</p>"
        ),
        "key_points": [
            "Autonomous APs are self-contained and managed individually; no WLC needed.",
            "Lightweight APs (LWAPs) use split-MAC with CAPWAP tunnels to a WLC (UDP 5246 control, 5247 data).",
            "FlexConnect APs can switch traffic locally and authenticate clients when WLC connectivity is lost.",
            "CAPWAP control tunnel is DTLS-encrypted; data tunnel encryption is optional.",
            "In local mode, the AP serves clients and performs background scanning for rogues.",
            "Monitor mode dedicates the AP entirely to passive scanning — no client traffic.",
            "WLC handles roaming, RF management, authentication, and security policies in centralized deployments.",
        ],
    },
    {
        "domain": 2,
        "topic": "WLC Management Access",
        "objective": "2.7",
        "video": "WLC management access",
        "study_topics": ["WLC management access"],
        "body": (
            "<p>A <strong>Wireless LAN Controller (WLC)</strong> centralizes management of lightweight APs "
            "and WLANs. The WLC provides multiple management access interfaces.</p>"
            "<h4>WLC Management Interfaces</h4>"
            "<table border='1' cellpadding='4'>"
            "<tr><th>Interface</th><th>Purpose</th></tr>"
            "<tr><td><strong>Management Interface</strong></td><td>Primary IP interface for management traffic (GUI, SSH, SNMP, RADIUS). "
            "Also used for in-band management and CAPWAP control communications.</td></tr>"
            "<tr><td><strong>AP-Manager Interface</strong></td><td>Manages CAPWAP AP communications (legacy; in newer WLC versions merged into management interface).</td></tr>"
            "<tr><td><strong>Virtual Interface</strong></td><td>Used for DHCP relay, web authentication (WebAuth), and mobility anchoring. Uses a non-routable IP (e.g., 192.0.2.1).</td></tr>"
            "<tr><td><strong>Service Port Interface</strong></td><td>Out-of-band management via a dedicated physical port. Used for initial setup or recovery; not connected to the data network.</td></tr>"
            "<tr><td><strong>Dynamic Interfaces</strong></td><td>Map WLANs to VLANs; each WLAN can be tied to a different VLAN/subnet.</td></tr>"
            "</table>"
            "<h4>Management Access Methods</h4>"
            "<ul>"
            "<li><strong>HTTP/HTTPS GUI</strong> — web-based dashboard; HTTPS recommended. Navigate to the management IP in a browser.</li>"
            "<li><strong>SSH / Telnet</strong> — CLI access; SSH is preferred for security.</li>"
            "<li><strong>Console</strong> — direct physical access via console cable for initial configuration or recovery.</li>"
            "<li><strong>SNMP</strong> — used for monitoring and integration with NMS platforms.</li>"
            "<li><strong>TACACS+ / RADIUS</strong> — AAA for WLC admin authentication.</li>"
            "</ul>"
            "<h4>WLC Port Types</h4>"
            "<ul>"
            "<li><strong>Distribution System Port</strong> — standard trunk port connecting WLC to the wired network; carries CAPWAP and VLAN traffic.</li>"
            "<li><strong>Service Port</strong> — out-of-band management; connects to a dedicated management network.</li>"
            "<li><strong>Redundancy Port</strong> — connects two WLCs for high availability (HA SSO).</li>"
            "</ul>"
            "<h4>WLC High Availability</h4>"
            "<p>Cisco WLCs support <strong>SSO (Stateful Switchover)</strong> HA pairs where a standby WLC "
            "takes over active duties without AP reassociation. APs maintain their CAPWAP sessions "
            "through the failover.</p>"
            "<p><strong>Key verification:</strong> From the WLC GUI — Monitor &gt; Summary shows AP count, "
            "client count, and interface status.</p>"
        ),
        "key_points": [
            "WLC Management Interface is the primary in-band IP for GUI, SSH, SNMP, and CAPWAP control.",
            "Service Port provides out-of-band management via a dedicated physical port separate from data traffic.",
            "Virtual Interface is used for DHCP relay and web authentication; uses a placeholder non-routable IP.",
            "Dynamic Interfaces map WLANs to specific VLANs on the wired network.",
            "HTTPS and SSH are preferred over HTTP/Telnet for secure WLC management.",
            "Distribution system ports on the WLC connect as trunks to carry multiple VLANs.",
            "WLC SSO HA allows failover without AP re-joining (CAPWAP sessions are maintained).",
        ],
    },
    {
        "domain": 2,
        "topic": "WLAN GUI Configuration",
        "objective": "2.7",
        "video": "WLAN GUI configuration",
        "study_topics": ["WLAN GUI configuration"],
        "body": (
            "<p>The Cisco WLC graphical interface provides a centralized method to create and manage WLANs. "
            "Understanding the GUI workflow is important for the CCNA exam.</p>"
            "<h4>Creating a WLAN — GUI Workflow</h4>"
            "<p>Navigate to <strong>WLANs &gt; Create New &gt; Go</strong>. Key fields to configure:</p>"
            "<ol>"
            "<li><strong>Profile Name</strong> — internal label for the WLAN.</li>"
            "<li><strong>SSID</strong> — the name broadcast to wireless clients.</li>"
            "<li><strong>WLAN ID</strong> — unique numeric ID (1–512 on Cisco WLC).</li>"
            "<li><strong>Status</strong> — Enabled/Disabled toggle for the WLAN.</li>"
            "</ol>"
            "<h4>WLAN Configuration Tabs</h4>"
            "<table border='1' cellpadding='4'>"
            "<tr><th>Tab</th><th>Key Settings</th></tr>"
            "<tr><td><strong>General</strong></td><td>SSID, Status, Interface/Interface Group (maps WLAN to a dynamic interface/VLAN), Radio Policy (2.4/5 GHz/both), Broadcast SSID toggle.</td></tr>"
            "<tr><td><strong>Security &gt; Layer 2</strong></td><td>Layer 2 security: None, WPA+WPA2, 802.1X, Static WEP (legacy). WPA2-Personal uses PSK; WPA2-Enterprise uses 802.1X/RADIUS.</td></tr>"
            "<tr><td><strong>Security &gt; Layer 3</strong></td><td>Web Policy (Web Authentication/Web Passthrough) for captive portal; VPN passthrough.</td></tr>"
            "<tr><td><strong>Security &gt; AAA Servers</strong></td><td>Assign RADIUS servers for 802.1X or MAC authentication.</td></tr>"
            "<tr><td><strong>QoS</strong></td><td>WLAN QoS profile: Platinum (voice), Gold (video), Silver (best effort), Bronze (background).</td></tr>"
            "<tr><td><strong>Advanced</strong></td><td>FlexConnect local switching, DHCP required, DHCP server override, P2P blocking, load balancing, band select, client exclusion.</td></tr>"
            "</table>"
            "<h4>Security Options Summary</h4>"
            "<ul>"
            "<li><strong>WPA2-Personal (PSK)</strong> — pre-shared key; suitable for small networks; configured under Layer 2 security.</li>"
            "<li><strong>WPA2-Enterprise (802.1X)</strong> — uses RADIUS server for per-user authentication; more secure.</li>"
            "<li><strong>Web Authentication</strong> — Layer 3 redirect to a login page; often used for guest networks.</li>"
            "</ul>"
            "<h4>Applying the WLAN to an AP Group</h4>"
            "<p>After creating a WLAN, it must be associated with an <strong>AP Group</strong> to determine "
            "which APs broadcast the SSID. Default AP Group applies the WLAN to all APs. Custom AP Groups "
            "restrict SSIDs to specific APs.</p>"
            "<p><strong>Verification:</strong> Monitor &gt; Clients shows associated wireless clients per WLAN; "
            "Monitor &gt; Access Points shows AP status and WLAN associations.</p>"
        ),
        "key_points": [
            "WLANs are created under WLANs > Create New in the WLC GUI; each WLAN gets a Profile Name, SSID, and WLAN ID.",
            "The Interface field on the General tab maps the WLAN to a dynamic interface (VLAN) for client traffic.",
            "Layer 2 security options: None, WPA+WPA2 (PSK or 802.1X), Static WEP (legacy).",
            "WPA2-Personal uses a PSK; WPA2-Enterprise uses 802.1X with a RADIUS server.",
            "Layer 3 security (Web Authentication) provides captive portal for guest access.",
            "QoS profiles: Platinum (voice) > Gold (video) > Silver (best effort) > Bronze (background).",
            "AP Groups control which APs broadcast a given SSID; the default group includes all APs.",
            "FlexConnect local switching is enabled per WLAN under the Advanced tab.",
        ],
    },
]

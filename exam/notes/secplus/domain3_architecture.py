"""
CompTIA Security+ (SY0-701) Domain 3: Security Architecture
Original study notes — not reproduced from any copyrighted source.
"""

NOTES = [
    {
        "domain": 3,
        "topic": "Cloud Architecture",
        "objective": "3.1",
        "video": "Cloud Architecture",
        "study_topics": ["Cloud architecture", "Serverless and cloud architecture"],
        "body": (
            "<p>Cloud computing delivers on-demand IT resources over a network, typically the internet. "
            "The three primary <strong>service models</strong> are:</p>"
            "<ul>"
            "<li><strong>IaaS (Infrastructure as a Service)</strong> — provider supplies virtualised compute, storage, "
            "and networking; customer manages OS and above (e.g., AWS EC2, Azure VMs).</li>"
            "<li><strong>PaaS (Platform as a Service)</strong> — provider manages the underlying infrastructure and "
            "runtime; customer deploys applications (e.g., Heroku, Azure App Service).</li>"
            "<li><strong>SaaS (Software as a Service)</strong> — provider manages everything; customer consumes the "
            "application (e.g., Microsoft 365, Salesforce).</li>"
            "</ul>"
            "<p><strong>Deployment models:</strong> Public (shared multi-tenant), Private (single-org), Hybrid "
            "(mixed), Community (shared by similar orgs).</p>"
            "<p><strong>Serverless / Function-as-a-Service (FaaS)</strong> — code executes in stateless, ephemeral "
            "containers triggered by events. The provider manages all infrastructure. Examples: AWS Lambda, Azure "
            "Functions. Security considerations include cold-start attacks, over-privileged function roles, insecure "
            "dependencies, and event-injection attacks.</p>"
            "<p><strong>Shared responsibility model</strong>: Security responsibilities shift between customer and "
            "provider depending on the service model. In IaaS the customer secures the OS and up; in SaaS the "
            "provider secures nearly everything. Always clarify what the customer must protect.</p>"
            "<p><strong>Key cloud security controls:</strong> CASB (Cloud Access Security Broker), cloud-native "
            "security groups, identity federation, encryption of data in transit and at rest, and least-privilege "
            "IAM roles.</p>"
        ),
        "key_points": [
            "IaaS / PaaS / SaaS differ in how much the customer vs. provider manages.",
            "Serverless (FaaS) runs ephemeral code; customer never manages servers.",
            "Shared responsibility model defines security ownership by service model.",
            "CASB provides visibility and policy enforcement for cloud services.",
            "Hybrid and multi-cloud introduce complexity in access control and data governance.",
        ],
    },
    {
        "domain": 3,
        "topic": "SDN and Logical Segmentation",
        "objective": "3.1",
        "video": "SDN and Logical Segmentation",
        "study_topics": ["SDN and logical segmentation"],
        "body": (
            "<p><strong>Software-Defined Networking (SDN)</strong> decouples the control plane (routing decisions) "
            "from the data plane (packet forwarding). A centralised SDN controller programs forwarding rules across "
            "all devices, enabling rapid, policy-driven network changes.</p>"
            "<p><strong>SDN security benefits:</strong> Micro-segmentation without re-cabling, dynamic firewall "
            "rule updates, east-west traffic inspection inside the data centre, faster response to incidents.</p>"
            "<p><strong>Logical segmentation techniques:</strong></p>"
            "<ul>"
            "<li><strong>VLANs</strong> — Layer 2 broadcast domains that isolate traffic on the same physical "
            "switch. VLAN hopping is a known attack (double-tagging or rogue switch).</li>"
            "<li><strong>Subnets</strong> — Layer 3 division enforced by routers/firewalls.</li>"
            "<li><strong>DMZ (Demilitarised Zone)</strong> — a buffer network between the internet and the internal "
            "LAN hosting public-facing services (web servers, mail relays).</li>"
            "<li><strong>East-West vs North-South traffic</strong> — north-south is traffic entering/leaving the "
            "data centre; east-west is lateral traffic between servers. SDN/micro-segmentation addresses east-west "
            "threats that perimeter firewalls miss.</li>"
            "</ul>"
            "<p><strong>Intranet / Extranet:</strong> An intranet is a private internal network; an extranet extends "
            "controlled access to trusted external partners.</p>"
            "<p><strong>Zero Trust micro-segmentation</strong> enforces per-workload access policies so that a "
            "compromised server cannot freely communicate laterally.</p>"
        ),
        "key_points": [
            "SDN separates control plane from data plane via a centralised controller.",
            "VLANs provide Layer 2 isolation; subnets provide Layer 3 isolation.",
            "DMZ hosts public-facing servers in a buffer zone between internet and LAN.",
            "East-west (lateral) traffic requires internal segmentation, not just perimeter controls.",
            "VLAN hopping attacks exploit trunk misconfiguration; disable unused ports and use native VLAN 1 carefully.",
        ],
    },
    {
        "domain": 3,
        "topic": "Microservices and Containerization",
        "objective": "3.1",
        "video": "Microservices and Containerization",
        "study_topics": ["Microservices and containerization"],
        "body": (
            "<p><strong>Microservices</strong> decompose a monolithic application into small, independently "
            "deployable services that communicate over APIs (typically REST or gRPC). Each service has its own "
            "codebase, database, and deployment lifecycle.</p>"
            "<p><strong>Security implications:</strong> Larger attack surface (many APIs), inter-service "
            "authentication (service mesh / mTLS), secret management per service, and API gateway controls.</p>"
            "<p><strong>Containers</strong> package an application with its dependencies in an isolated user-space "
            "environment. They share the host OS kernel, making them lighter than VMs but with a smaller isolation "
            "boundary.</p>"
            "<p><strong>Container security concerns:</strong></p>"
            "<ul>"
            "<li>Image security — use signed, minimal base images; scan for CVEs before deployment.</li>"
            "<li>Runtime security — restrict capabilities, drop root, use read-only filesystems.</li>"
            "<li>Container escape — vulnerability allowing a process to break out of the container namespace.</li>"
            "<li>Orchestration security — Kubernetes RBAC, network policies, secrets management (e.g., HashiCorp "
            "Vault or Kubernetes Secrets).</li>"
            "</ul>"
            "<p><strong>Container vs VM isolation:</strong> VMs have a hypervisor providing stronger isolation; "
            "containers share the kernel, so a kernel exploit could compromise all containers on the host.</p>"
            "<p><strong>CI/CD pipeline security:</strong> Shift-left security; scan images in pipelines, sign "
            "artifacts, enforce policy gates before production deployment.</p>"
        ),
        "key_points": [
            "Microservices communicate over APIs; secure each service independently.",
            "Containers share the host kernel — weaker isolation than VMs.",
            "Scan container images for vulnerabilities before deployment.",
            "Use Kubernetes RBAC and network policies to limit lateral movement.",
            "mTLS between microservices ensures mutual authentication and encryption.",
        ],
    },
    {
        "domain": 3,
        "topic": "Zero Trust / SASE",
        "objective": "3.1",
        "video": "Zero Trust / SASE",
        "study_topics": ["Zero Trust / SASE"],
        "body": (
            "<p><strong>Zero Trust</strong> is a security model based on the principle of <em>never trust, always "
            "verify</em>. No user, device, or network segment is trusted by default, even if inside the corporate "
            "perimeter.</p>"
            "<p><strong>Zero Trust pillars:</strong></p>"
            "<ul>"
            "<li>Identity — verify every user with strong authentication (MFA, passwordless).</li>"
            "<li>Device — assess device health/posture before granting access.</li>"
            "<li>Network — micro-segment and encrypt all traffic.</li>"
            "<li>Application — apply least-privilege access per application.</li>"
            "<li>Data — classify and protect data regardless of location.</li>"
            "</ul>"
            "<p><strong>NIST 800-207</strong> defines the seven tenets of Zero Trust Architecture (ZTA), including "
            "continuous verification and dynamic policy enforcement.</p>"
            "<p><strong>SASE (Secure Access Service Edge)</strong> — a cloud-delivered architecture that combines "
            "network connectivity (SD-WAN) with security services (CASB, SWG, ZTNA, FWaaS) in a single cloud "
            "platform. Coined by Gartner.</p>"
            "<p><strong>ZTNA (Zero Trust Network Access)</strong> — replaces traditional VPN by granting access "
            "only to specific applications rather than the entire network, based on identity and context.</p>"
            "<p><strong>Key differences — VPN vs ZTNA:</strong> VPN grants broad network access after "
            "authentication; ZTNA grants per-application access based on continuous policy evaluation.</p>"
            "<p>Implementing Zero Trust requires identity provider integration, device health attestation, "
            "continuous monitoring, and logging.</p>"
        ),
        "key_points": [
            "Zero Trust: never trust, always verify — applies inside and outside the perimeter.",
            "SASE converges SD-WAN with cloud-native security (CASB, SWG, ZTNA, FWaaS).",
            "ZTNA grants per-app access vs. VPN's broad network access.",
            "Continuous verification means authentication and authorisation are re-evaluated per session/request.",
            "NIST 800-207 is the foundational Zero Trust Architecture document.",
        ],
    },
    {
        "domain": 3,
        "topic": "Network Appliances",
        "objective": "3.2",
        "video": "Network Appliances",
        "study_topics": ["Network appliances"],
        "body": (
            "<p>Network appliances are dedicated hardware or virtual devices that perform specific security or "
            "networking functions.</p>"
            "<table border='1' cellpadding='4' cellspacing='0'>"
            "<tr><th>Appliance</th><th>Function</th></tr>"
            "<tr><td><strong>Jump server / Bastion host</strong></td><td>Hardened gateway for administrative "
            "access to internal systems; all admin sessions route through it for logging and control.</td></tr>"
            "<tr><td><strong>Proxy server</strong></td><td>Intermediary for client requests. Forward proxy hides "
            "client identity; reverse proxy hides server identity. Content filtering and caching are common "
            "uses.</td></tr>"
            "<tr><td><strong>Load balancer</strong></td><td>Distributes traffic across multiple servers; can "
            "terminate TLS and perform health checks. Helps with availability and mitigates some DoS.</td></tr>"
            "<tr><td><strong>IDS / IPS</strong></td><td>Intrusion Detection System (passive — alerts); Intrusion "
            "Prevention System (inline — blocks). Both use signature, anomaly, and heuristic detection.</td></tr>"
            "<tr><td><strong>Sensors / Collectors</strong></td><td>Capture flow data (NetFlow/IPFIX) or full "
            "packet captures for SIEM analysis.</td></tr>"
            "<tr><td><strong>Network TAP</strong></td><td>Hardware device providing a copy of network traffic to "
            "monitoring tools without introducing a point of failure.</td></tr>"
            "<tr><td><strong>Aggregation switch</strong></td><td>Consolidates traffic from access-layer switches "
            "upward; may enforce trunking and VLAN policies.</td></tr>"
            "</table>"
            "<p><strong>Inline vs. passive:</strong> Inline appliances (IPS, next-gen firewall) can block traffic "
            "but add latency; passive appliances (IDS, TAP) cannot block but do not affect traffic flow.</p>"
        ),
        "key_points": [
            "Jump/bastion host centralises and logs privileged administrative access.",
            "Forward proxy protects clients; reverse proxy protects servers.",
            "IDS alerts only; IPS is inline and can block traffic in real time.",
            "Network TAPs provide passive, non-disruptive traffic copies for monitoring.",
            "Load balancers improve availability and can perform TLS offloading.",
        ],
    },
    {
        "domain": 3,
        "topic": "Firewalls",
        "objective": "3.2",
        "video": "Firewalls",
        "study_topics": ["Firewalls"],
        "body": (
            "<p>A <strong>firewall</strong> controls traffic between network segments based on rules. Firewalls "
            "operate at different OSI layers and offer varying levels of inspection.</p>"
            "<table border='1' cellpadding='4' cellspacing='0'>"
            "<tr><th>Type</th><th>Layer</th><th>Key Features</th></tr>"
            "<tr><td><strong>Packet filter</strong></td><td>L3/L4</td><td>Stateless; inspects IP headers and TCP/"
            "UDP ports. Fast but limited; cannot track connection state.</td></tr>"
            "<tr><td><strong>Stateful firewall</strong></td><td>L4</td><td>Tracks connection state table; allows "
            "return traffic automatically. Most common traditional firewall.</td></tr>"
            "<tr><td><strong>Application-layer (proxy) firewall</strong></td><td>L7</td><td>Deep packet inspection "
            "of application protocols (HTTP, FTP, DNS). Breaks and re-establishes connections.</td></tr>"
            "<tr><td><strong>NGFW (Next-Generation Firewall)</strong></td><td>L7</td><td>Combines stateful "
            "inspection with IPS, application identification, user-identity awareness, SSL/TLS inspection, and "
            "threat intelligence feeds.</td></tr>"
            "<tr><td><strong>UTM (Unified Threat Management)</strong></td><td>L7</td><td>All-in-one appliance: "
            "firewall + IPS + antivirus + web filter + VPN + DLP. Common in SMB environments.</td></tr>"
            "<tr><td><strong>WAF (Web Application Firewall)</strong></td><td>L7</td><td>Protects web applications "
            "from OWASP Top 10 attacks (SQLi, XSS, CSRF). Can operate in detection or prevention mode. Commonly "
            "deployed as a reverse proxy.</td></tr>"
            "</table>"
            "<p><strong>ACL rules</strong> are processed top-down; first match wins. Always end with an implicit "
            "deny-all.</p>"
            "<p><strong>Firewall deployment zones:</strong> External (internet), DMZ (public services), Internal "
            "(LAN). Traffic from internet to DMZ is permitted on specific ports; internal-to-DMZ is restricted; "
            "internet-to-internal is blocked.</p>"
            "<p><strong>Screened subnet</strong> (modern term for DMZ) uses two firewalls — one facing the internet "
            "and one facing the internal network — to create the buffer zone.</p>"
        ),
        "key_points": [
            "Packet-filter firewalls are stateless (L3/L4); stateful firewalls track connection state (L4).",
            "NGFW operates at L7 with application awareness, IPS, and TLS inspection.",
            "WAF targets web-app attacks (SQLi, XSS) and sits in front of web servers.",
            "UTM bundles multiple security functions in one appliance, popular in SMB.",
            "ACL rules are first-match; place more specific rules before general ones and end with deny-all.",
            "Screened subnet (DMZ) uses two firewalls to create a buffer zone for public services.",
        ],
    },
    {
        "domain": 3,
        "topic": "Port Security and 802.1X",
        "objective": "3.2",
        "video": "Port Security and 802.1X",
        "study_topics": ["Port security and 802.1X"],
        "body": (
            "<p><strong>Port security</strong> is a Layer 2 switch feature that limits which MAC addresses can "
            "communicate on a switchport.</p>"
            "<ul>"
            "<li><strong>Static MAC</strong> — manually configured allowed MAC(s).</li>"
            "<li><strong>Dynamic (sticky) MAC</strong> — first MAC learned is remembered and saved to config.</li>"
            "<li><strong>Violation actions:</strong> Shutdown (disables port — most secure), Restrict (drops "
            "packets, increments counter), Protect (drops silently).</li>"
            "</ul>"
            "<p>Port security mitigates MAC flooding attacks, which overflow the CAM table and force a switch to "
            "behave like a hub.</p>"
            "<p><strong>IEEE 802.1X</strong> is the standard for <em>port-based Network Access Control (NAC)</em>. "
            "It authenticates devices and users before allowing LAN/WLAN access.</p>"
            "<p><strong>802.1X components:</strong></p>"
            "<ul>"
            "<li><strong>Supplicant</strong> — the client device requesting access.</li>"
            "<li><strong>Authenticator</strong> — the switch or wireless AP that controls port access.</li>"
            "<li><strong>Authentication Server</strong> — typically a RADIUS server that validates credentials.</li>"
            "</ul>"
            "<p><strong>EAP (Extensible Authentication Protocol)</strong> carries authentication messages between "
            "supplicant and RADIUS. Common EAP types: EAP-TLS (certificate-based, most secure), PEAP (wraps EAP "
            "in TLS tunnel, password inside), EAP-TTLS, EAP-FAST.</p>"
            "<p><strong>NAC (Network Access Control)</strong> extends 802.1X with posture assessment — checking "
            "that the endpoint meets security policy (patched OS, AV enabled) before granting access. Non-compliant "
            "devices are placed in a quarantine VLAN for remediation.</p>"
        ),
        "key_points": [
            "Port security restricts switch ports by MAC address; violation modes: shutdown, restrict, protect.",
            "MAC flooding fills the CAM table, causing the switch to broadcast all frames.",
            "802.1X uses supplicant / authenticator / RADIUS server for port-based access control.",
            "EAP-TLS is the most secure EAP type (mutual certificate authentication); PEAP is most common.",
            "NAC adds posture checking; non-compliant endpoints land in a quarantine/remediation VLAN.",
        ],
    },
    {
        "domain": 3,
        "topic": "Secure Communication (VPN / TLS / IPSec)",
        "objective": "3.2",
        "video": "Secure Communication (VPN/TLS/IPSec)",
        "study_topics": ["Secure communication (VPN/TLS/IPSec)"],
        "body": (
            "<p>Secure communication protocols protect data <em>in transit</em> across untrusted networks.</p>"
            "<p><strong>TLS (Transport Layer Security)</strong> — successor to SSL; operates at the session/transport "
            "layer. Provides confidentiality (symmetric encryption), integrity (HMAC), and authentication "
            "(certificates). TLS 1.3 (current standard) removes weak cipher suites and speeds up handshake to 1-RTT. "
            "TLS 1.0/1.1 are deprecated.</p>"
            "<p><strong>IPsec</strong> — a suite of protocols securing IP communications at Layer 3. Two main "
            "protocols:</p>"
            "<ul>"
            "<li><strong>AH (Authentication Header)</strong> — provides integrity and authentication for the IP "
            "packet (including the IP header in tunnel mode) but <em>no confidentiality</em> (no encryption).</li>"
            "<li><strong>ESP (Encapsulating Security Payload)</strong> — provides confidentiality (encryption), "
            "integrity, and authentication for the payload. Most commonly used.</li>"
            "</ul>"
            "<p><strong>IPsec modes:</strong></p>"
            "<ul>"
            "<li><strong>Transport mode</strong> — encrypts/authenticates only the payload; original IP header "
            "preserved. Used for host-to-host communication.</li>"
            "<li><strong>Tunnel mode</strong> — encrypts the entire original packet and adds a new IP header. Used "
            "for site-to-site VPNs.</li>"
            "</ul>"
            "<p><strong>IKE (Internet Key Exchange)</strong> — negotiates and manages IPsec SAs (Security "
            "Associations). IKEv2 is the current standard and supports MOBIKE for roaming.</p>"
            "<p><strong>VPN types:</strong></p>"
            "<ul>"
            "<li><strong>Site-to-site VPN</strong> — connects two networks (IPsec tunnel mode). Always-on.</li>"
            "<li><strong>Remote-access VPN</strong> — individual clients connect to the corporate network. Uses "
            "SSL/TLS (e.g., OpenVPN) or IPsec.</li>"
            "<li><strong>Split tunnel</strong> — only traffic destined for corporate resources goes through the "
            "VPN; internet traffic exits locally. Reduces load but reduces visibility.</li>"
            "<li><strong>Full tunnel</strong> — all traffic routes through VPN. Greater security and monitoring.</li>"
            "</ul>"
        ),
        "key_points": [
            "TLS 1.3 is the current standard; TLS 1.0/1.1 are deprecated.",
            "IPsec AH = integrity/auth only (no encryption); ESP = encryption + integrity + auth.",
            "IPsec transport mode: payload only; tunnel mode: full packet (used for site-to-site VPN).",
            "IKE/IKEv2 negotiates IPsec Security Associations and keys.",
            "Split-tunnel VPN sends only corporate traffic through VPN; full-tunnel sends all traffic.",
        ],
    },
    {
        "domain": 3,
        "topic": "Failure Modes",
        "objective": "3.2",
        "video": "Failure Modes",
        "study_topics": ["Failure modes"],
        "body": (
            "<p>When a security device or system fails, its behavior can be <strong>fail-open</strong> or "
            "<strong>fail-closed (fail-secure)</strong>. The correct choice depends on whether availability or "
            "security is the priority.</p>"
            "<table border='1' cellpadding='4' cellspacing='0'>"
            "<tr><th>Mode</th><th>Behavior on Failure</th><th>Priority</th><th>Example</th></tr>"
            "<tr><td><strong>Fail-open</strong></td><td>Traffic/access is <em>allowed</em> through when the "
            "device fails.</td><td>Availability</td><td>A firewall that fails open keeps network connectivity "
            "but removes security controls — traffic bypasses inspection.</td></tr>"
            "<tr><td><strong>Fail-closed / Fail-secure</strong></td><td>Traffic/access is <em>blocked</em> when "
            "the device fails.</td><td>Security</td><td>An IPS that fails closed drops all traffic — network is "
            "down but no unfiltered traffic passes.</td></tr>"
            "</table>"
            "<p><strong>Design considerations:</strong></p>"
            "<ul>"
            "<li>Safety-critical systems (industrial controls, hospital networks) often prefer fail-safe (fail-open "
            "for physical safety, fail-closed for information security).</li>"
            "<li>High-security environments (government, finance) typically require fail-closed.</li>"
            "<li>High-availability environments (e-commerce, hospitals) may tolerate fail-open to prevent "
            "outages.</li>"
            "</ul>"
            "<p><strong>Fault tolerance</strong> mechanisms (redundancy, clustering, HA pairs) reduce the "
            "likelihood of failure. Active-active clusters share load; active-passive clusters have a standby "
            "that takes over on failure.</p>"
            "<p>The failure mode should be documented in the security policy and tested during disaster recovery "
            "exercises.</p>"
        ),
        "key_points": [
            "Fail-open allows traffic on failure (prioritises availability).",
            "Fail-closed/fail-secure blocks traffic on failure (prioritises security).",
            "The correct mode depends on whether availability or security is the higher priority.",
            "Active-active clusters share load; active-passive have a hot standby.",
            "Test failure modes during disaster recovery and tabletop exercises.",
        ],
    },
    {
        "domain": 3,
        "topic": "Attack Surface Reduction",
        "objective": "3.2",
        "video": "Attack Surface Reduction",
        "study_topics": ["Attack surface reduction"],
        "body": (
            "<p>The <strong>attack surface</strong> is the total set of points where an unauthorised user could "
            "attempt to enter or extract data from an environment. Reducing it minimises exposure.</p>"
            "<p><strong>Techniques:</strong></p>"
            "<ul>"
            "<li><strong>Hardening</strong> — remove or disable unnecessary services, ports, protocols, and "
            "accounts. Apply OS and application benchmarks (CIS Benchmarks).</li>"
            "<li><strong>Principle of least privilege</strong> — grant only the minimum access needed. Reduces "
            "impact of compromised credentials.</li>"
            "<li><strong>Network segmentation</strong> — limit which systems can communicate. Prevents lateral "
            "movement after a breach.</li>"
            "<li><strong>Patch management</strong> — promptly apply security updates to eliminate known "
            "vulnerabilities.</li>"
            "<li><strong>Disabling default credentials</strong> — change or remove vendor defaults on all "
            "devices.</li>"
            "<li><strong>Application allow-listing</strong> — permit only approved software to execute, blocking "
            "unknown or malicious code.</li>"
            "<li><strong>Port/protocol management</strong> — close unused ports via firewall ACLs and host-based "
            "firewalls.</li>"
            "<li><strong>Removing legacy systems</strong> — decommission end-of-life systems that cannot be "
            "patched.</li>"
            "</ul>"
            "<p><strong>Digital footprint reduction:</strong> Limit publicly discoverable information (DNS records, "
            "banner information, job postings revealing technology stack) that attackers can use during "
            "reconnaissance.</p>"
            "<p><strong>Deception technologies</strong> (honeypots, honeynets) do not reduce the attack surface "
            "but provide early warning when attackers probe decoy assets.</p>"
        ),
        "key_points": [
            "Attack surface = all points where attackers can try to enter or extract data.",
            "Hardening removes unnecessary services, ports, and accounts (use CIS Benchmarks).",
            "Least privilege limits the blast radius of a compromised account.",
            "Application allow-listing blocks unapproved software execution.",
            "Reducing digital footprint limits reconnaissance value for attackers.",
        ],
    },
    {
        "domain": 3,
        "topic": "Data Classification",
        "objective": "3.3",
        "video": "Data Classification",
        "study_topics": ["Data classification", "Data classification levels"],
        "body": (
            "<p><strong>Data classification</strong> assigns labels to data based on its sensitivity and the "
            "impact of unauthorised disclosure. Proper classification drives appropriate security controls.</p>"
            "<p><strong>Government / Military classification levels (example):</strong></p>"
            "<table border='1' cellpadding='4' cellspacing='0'>"
            "<tr><th>Level</th><th>Description</th></tr>"
            "<tr><td><strong>Top Secret</strong></td><td>Unauthorised disclosure could cause exceptionally grave "
            "damage to national security.</td></tr>"
            "<tr><td><strong>Secret</strong></td><td>Serious damage to national security.</td></tr>"
            "<tr><td><strong>Confidential</strong></td><td>Damage to national security.</td></tr>"
            "<tr><td><strong>Unclassified</strong></td><td>No damage expected; may be publicly released.</td></tr>"
            "</table>"
            "<p><strong>Commercial / Corporate classification levels (example):</strong></p>"
            "<table border='1' cellpadding='4' cellspacing='0'>"
            "<tr><th>Level</th><th>Description</th></tr>"
            "<tr><td><strong>Confidential / Restricted</strong></td><td>Highly sensitive; trade secrets, PII, "
            "financial data.</td></tr>"
            "<tr><td><strong>Internal / Private</strong></td><td>For internal use; not for public "
            "release.</td></tr>"
            "<tr><td><strong>Public</strong></td><td>Approved for public release; minimal controls "
            "needed.</td></tr>"
            "</table>"
            "<p><strong>Data owner</strong> — senior leader accountable for a data set; defines classification and "
            "acceptable use.</p>"
            "<p><strong>Data custodian / steward</strong> — technical staff who implement the controls specified "
            "by the data owner.</p>"
            "<p><strong>Labelling and handling</strong>: Classified data must be labelled consistently (header/ "
            "footer on documents, metadata tags on files) and handled per policy (storage, transmission, "
            "disposal).</p>"
            "<p><strong>Re-classification</strong>: Data may be downgraded or upgraded as its sensitivity changes "
            "over time.</p>"
        ),
        "key_points": [
            "Classification levels match controls to data sensitivity.",
            "Government: Top Secret → Secret → Confidential → Unclassified.",
            "Commercial: Confidential/Restricted → Internal/Private → Public.",
            "Data owner sets policy; data custodian implements technical controls.",
            "Labels must be consistent; handling procedures enforced throughout data lifecycle.",
        ],
    },
    {
        "domain": 3,
        "topic": "Data States",
        "objective": "3.3",
        "video": "Data States",
        "study_topics": ["Data states"],
        "body": (
            "<p>Data exists in one of three states, each requiring different security controls.</p>"
            "<table border='1' cellpadding='4' cellspacing='0'>"
            "<tr><th>State</th><th>Description</th><th>Primary Controls</th></tr>"
            "<tr><td><strong>Data at Rest</strong></td><td>Stored on a medium: hard drive, SSD, tape, database, "
            "cloud storage, USB drive.</td>"
            "<td>Full-disk encryption (FDE), file/folder encryption (EFS), database encryption (TDE), DRM, "
            "physical access controls.</td></tr>"
            "<tr><td><strong>Data in Transit</strong></td><td>Moving across a network: internet, LAN, WAN, "
            "wireless link.</td>"
            "<td>TLS, IPsec, SSH, HTTPS, VPN. Prevents eavesdropping and MITM attacks.</td></tr>"
            "<tr><td><strong>Data in Use</strong></td><td>Actively being processed by the CPU or resident in "
            "RAM/cache.</td>"
            "<td>Access controls, memory encryption (e.g., AMD SEV, Intel TDX), secure enclaves (Intel SGX), "
            "DLP endpoint agents, process isolation.</td></tr>"
            "</table>"
            "<p><strong>Data in use</strong> is the hardest state to protect because decrypted data must be "
            "available to the processor. Memory-scraping malware, cold-boot attacks, and speculative execution "
            "vulnerabilities (Spectre, Meltdown) target data in use.</p>"
            "<p><strong>Encryption at rest examples:</strong> BitLocker (Windows FDE), FileVault (macOS), "
            "LUKS (Linux), AWS S3 server-side encryption, TDE in SQL Server/Oracle.</p>"
            "<p><strong>Rights Management</strong>: DRM/IRM can persist protection across all states by "
            "embedding access controls in the document itself.</p>"
        ),
        "key_points": [
            "At rest: stored data — protect with FDE, TDE, file encryption.",
            "In transit: moving data — protect with TLS, IPsec, VPN.",
            "In use: data being processed — hardest to protect; use memory encryption, secure enclaves.",
            "Cold-boot and memory-scraping attacks target data in use.",
            "DRM/IRM embeds persistent protection that follows data across all states.",
        ],
    },
    {
        "domain": 3,
        "topic": "Data Protection Methods",
        "objective": "3.3",
        "video": "Data Protection Methods",
        "study_topics": ["Data protection methods"],
        "body": (
            "<p>Multiple complementary methods protect sensitive data throughout its lifecycle.</p>"
            "<ul>"
            "<li><strong>Encryption</strong> — transforms plaintext to ciphertext using a key. Symmetric "
            "(AES-256) for bulk data; asymmetric (RSA, ECC) for key exchange and signatures.</li>"
            "<li><strong>Hashing</strong> — one-way function producing a fixed-size digest for integrity "
            "verification. SHA-256 and SHA-3 are current standards; MD5 and SHA-1 are deprecated.</li>"
            "<li><strong>DLP (Data Loss Prevention)</strong> — software that monitors, detects, and blocks "
            "unauthorised data transfers. Can operate at the network level (NDLP) or endpoint (EDLP).</li>"
            "<li><strong>IRM / DRM (Information/Digital Rights Management)</strong> — controls how documents are "
            "accessed, edited, printed, or forwarded after distribution.</li>"
            "<li><strong>Data masking</strong> — replaces sensitive data with realistic but fictitious data. "
            "Used in dev/test environments. Masking is persistent and the original data is not retrievable "
            "from the masked value.</li>"
            "<li><strong>Tokenization</strong> — replaces sensitive values with a non-sensitive token. "
            "A separate token vault maps tokens back to originals. Original data is not exposed during "
            "processing.</li>"
            "<li><strong>Anonymisation</strong> — irreversibly removes PII so data cannot be linked to an "
            "individual. Stronger than pseudonymisation.</li>"
            "<li><strong>Pseudonymisation</strong> — replaces identifiers with pseudonyms; can be reversed with "
            "the mapping key.</li>"
            "<li><strong>Segmentation and need-to-know</strong> — restrict who can access sensitive data, "
            "limiting exposure.</li>"
            "</ul>"
        ),
        "key_points": [
            "Encryption (AES-256) protects confidentiality; hashing (SHA-256) protects integrity.",
            "DLP monitors and blocks unauthorised data transfers at network and endpoint.",
            "Masking replaces real data with fake data for dev/test — original is not recoverable.",
            "Tokenization replaces values with tokens; originals stored in a secure vault.",
            "Anonymisation is irreversible; pseudonymisation is reversible with the mapping key.",
        ],
    },
    {
        "domain": 3,
        "topic": "Tokenization and Masking",
        "objective": "3.3",
        "video": "Tokenization and Masking",
        "study_topics": ["Tokenization and masking"],
        "body": (
            "<p><strong>Tokenization</strong> and <strong>data masking</strong> are both data de-identification "
            "techniques, but they work differently and suit different use cases.</p>"
            "<p><strong>Tokenization</strong>:</p>"
            "<ul>"
            "<li>Replaces a sensitive value (e.g., a credit card number) with a randomly generated, meaningless "
            "token.</li>"
            "<li>The mapping between token and original value is stored in a separate, secured <em>token vault</em>."
            "</li>"
            "<li>The original data is never transmitted to downstream systems — only the token is.</li>"
            "<li>Reversible by authorised systems that query the vault.</li>"
            "<li>Common use: PCI-DSS compliance, storing payment card data.</li>"
            "</ul>"
            "<p><strong>Data Masking</strong>:</p>"
            "<ul>"
            "<li>Replaces real data with structurally similar but fictitious values (e.g., real SSN → fake SSN "
            "of the same format).</li>"
            "<li><strong>Static masking</strong> — creates a masked copy of a database for use in dev/test; "
            "original production data is untouched.</li>"
            "<li><strong>Dynamic masking</strong> — masks data in real time as it is returned by a query, without "
            "altering the stored data.</li>"
            "<li>Not reversible — the original value cannot be recovered from the masked value.</li>"
            "</ul>"
            "<p><strong>Format-preserving encryption (FPE)</strong> — an encryption technique that keeps the "
            "output in the same format as the input (e.g., encrypts a 16-digit card number to another 16-digit "
            "number). Sometimes used alongside tokenization.</p>"
            "<p><strong>Key distinctions for the exam:</strong> Tokenization uses a vault for reversal; masking "
            "has no vault and is not reversible. Both reduce the risk of exposing real data in lower-trust "
            "environments.</p>"
        ),
        "key_points": [
            "Tokenization uses a secure vault to map tokens to real values — reversible.",
            "Masking produces fictitious data with the same format — not reversible.",
            "Static masking creates a masked database copy; dynamic masking masks query results in real time.",
            "Tokenization is widely used for PCI-DSS card-data compliance.",
            "Format-preserving encryption maintains data format while providing cryptographic protection.",
        ],
    },
    {
        "domain": 3,
        "topic": "Recovery Sites",
        "objective": "3.4",
        "video": "Recovery Sites",
        "study_topics": ["Recovery sites"],
        "body": (
            "<p>Recovery sites are alternate facilities that organisations use to restore operations after a "
            "disaster. They differ in cost, readiness, and recovery time.</p>"
            "<table border='1' cellpadding='4' cellspacing='0'>"
            "<tr><th>Site Type</th><th>Infrastructure</th><th>Data</th><th>RTO</th><th>Cost</th></tr>"
            "<tr><td><strong>Hot site</strong></td><td>Fully equipped, powered, and operational — mirrors "
            "production.</td><td>Real-time or near-real-time replication.</td><td>Minutes to hours.</td>"
            "<td>Highest.</td></tr>"
            "<tr><td><strong>Warm site</strong></td><td>Partially equipped — hardware present but may need "
            "configuration.</td><td>Periodic backups; some data lag.</td><td>Hours to days.</td>"
            "<td>Moderate.</td></tr>"
            "<tr><td><strong>Cold site</strong></td><td>Facility only — power, HVAC, connectivity but no "
            "equipment.</td><td>Backups must be restored on procured hardware.</td><td>Days to weeks.</td>"
            "<td>Lowest.</td></tr>"
            "<tr><td><strong>Mobile site</strong></td><td>Self-contained trailer or portable unit that can be "
            "deployed to any location.</td><td>Varies.</td><td>Hours to days after delivery.</td>"
            "<td>Variable.</td></tr>"
            "<tr><td><strong>Cloud site</strong></td><td>Virtual infrastructure spun up on-demand in the "
            "cloud.</td><td>Cloud-replicated data.</td><td>Minutes to hours.</td><td>Pay-as-you-use.</td></tr>"
            "</table>"
            "<p><strong>Geographic considerations:</strong> Recovery sites should be far enough from the primary "
            "site to avoid the same regional disaster (hurricane, earthquake) but close enough for practical "
            "operation. Typical guidance: at least 50-100 miles separation for regional threats.</p>"
            "<p><strong>RTO (Recovery Time Objective)</strong> — maximum acceptable time to restore operations. "
            "<strong>RPO (Recovery Point Objective)</strong> — maximum acceptable data loss measured in time "
            "(how old can the backup be?).</p>"
        ),
        "key_points": [
            "Hot site: fully operational, highest cost, lowest RTO (minutes to hours).",
            "Warm site: partially equipped, moderate cost, RTO hours to days.",
            "Cold site: facility only, lowest cost, highest RTO (days to weeks).",
            "Geographic separation prevents a single regional disaster from affecting both sites.",
            "RTO = time to restore; RPO = acceptable data loss (time since last backup).",
        ],
    },
    {
        "domain": 3,
        "topic": "Backups and Replication",
        "objective": "3.4",
        "video": "Backups and Replication",
        "study_topics": ["Backups and replication"],
        "body": (
            "<p>Backups and replication are core resilience mechanisms that protect against data loss.</p>"
            "<p><strong>Backup types:</strong></p>"
            "<table border='1' cellpadding='4' cellspacing='0'>"
            "<tr><th>Type</th><th>What is copied</th><th>Restore complexity</th><th>Speed</th></tr>"
            "<tr><td><strong>Full</strong></td><td>All data.</td><td>Simplest (one tape/set).</td>"
            "<td>Slowest to back up.</td></tr>"
            "<tr><td><strong>Incremental</strong></td><td>Data changed since the <em>last backup</em> "
            "(full or incremental).</td><td>Requires full + all incrementals.</td>"
            "<td>Fastest to back up.</td></tr>"
            "<tr><td><strong>Differential</strong></td><td>Data changed since the <em>last full</em> "
            "backup.</td><td>Requires full + latest differential only.</td>"
            "<td>Grows over time until next full.</td></tr>"
            "<tr><td><strong>Snapshot</strong></td><td>Point-in-time copy (often copy-on-write at storage "
            "layer).</td><td>Fast restore.</td><td>Near-instant, storage-efficient.</td></tr>"
            "</table>"
            "<p><strong>3-2-1 backup rule:</strong> 3 copies, on 2 different media types, with 1 copy "
            "offsite.</p>"
            "<p><strong>Replication</strong> — continuously synchronises data to a secondary location. Supports "
            "a lower RPO than periodic backups.</p>"
            "<ul>"
            "<li><strong>Synchronous replication</strong> — write is committed only after the secondary "
            "acknowledges it. Zero data loss. Higher latency.</li>"
            "<li><strong>Asynchronous replication</strong> — write is committed locally first, then replicated. "
            "Lower latency; small data-loss window (RPO &gt; 0).</li>"
            "</ul>"
            "<p><strong>Backup security:</strong> Encrypt backups at rest and in transit; test restores "
            "regularly; protect backup media from physical theft; store offsite copies securely.</p>"
        ),
        "key_points": [
            "Full backup: all data; incremental: since last backup; differential: since last full.",
            "Restore order: full + incrementals (all); or full + latest differential only.",
            "3-2-1 rule: 3 copies, 2 media types, 1 offsite.",
            "Synchronous replication = zero data loss; asynchronous = low latency with small RPO window.",
            "Always test restores — an untested backup is not a reliable backup.",
        ],
    },
    {
        "domain": 3,
        "topic": "High Availability and Virtualization",
        "objective": "3.4",
        "video": "High Availability",
        "study_topics": ["High availability", "Virtualization and high availability"],
        "body": (
            "<p><strong>High availability (HA)</strong> ensures systems remain operational with minimal downtime. "
            "It is measured as a percentage of uptime (e.g., 99.999% = &quot;five nines&quot; ≈ 5.26 minutes "
            "downtime/year).</p>"
            "<p><strong>HA techniques:</strong></p>"
            "<ul>"
            "<li><strong>Clustering</strong> — multiple servers share a workload. Active-active: all nodes "
            "handle traffic. Active-passive: standby takes over on failure.</li>"
            "<li><strong>Load balancing</strong> — distributes requests across server pools; detects failed "
            "nodes and removes them.</li>"
            "<li><strong>Geographic redundancy</strong> — workloads span multiple data centres or cloud "
            "availability zones.</li>"
            "<li><strong>Redundant networking</strong> — multiple uplinks, NIC bonding/teaming, redundant "
            "switches/routers.</li>"
            "</ul>"
            "<p><strong>Virtualization</strong> abstracts physical hardware, enabling multiple virtual machines "
            "(VMs) to run on one host. Security implications:</p>"
            "<ul>"
            "<li><strong>Hypervisor types:</strong> Type 1 (bare-metal, e.g., VMware ESXi, Hyper-V) runs "
            "directly on hardware; Type 2 (hosted, e.g., VirtualBox) runs on an OS.</li>"
            "<li><strong>VM escape</strong> — exploit allowing a VM process to break out of the hypervisor "
            "and access the host or other VMs. Critical vulnerability.</li>"
            "<li><strong>VM sprawl</strong> — uncontrolled proliferation of VMs, increasing attack surface "
            "and management complexity.</li>"
            "<li><strong>Snapshot rollback</strong> — revert a VM to a known-good state for rapid recovery.</li>"
            "<li><strong>Live migration (vMotion)</strong> — move a running VM between hosts; migration "
            "traffic must be encrypted.</li>"
            "</ul>"
            "<p><strong>SPOF (Single Point of Failure)</strong> — any component whose failure causes the entire "
            "system to fail. HA design eliminates SPOFs through redundancy.</p>"
        ),
        "key_points": [
            "Five nines (99.999%) availability ≈ 5.26 minutes downtime per year.",
            "Active-active clustering: all nodes serve traffic; active-passive: standby on failover.",
            "Type 1 hypervisors run on bare metal; Type 2 run on a host OS.",
            "VM escape is a critical vulnerability allowing code to break out of a VM.",
            "Eliminate SPOFs with redundant power, network, and compute.",
        ],
    },
    {
        "domain": 3,
        "topic": "Resilience Testing",
        "objective": "3.4",
        "video": "Resilience Testing",
        "study_topics": ["Resilience testing"],
        "body": (
            "<p><strong>Resilience testing</strong> validates that systems can withstand, recover from, and "
            "adapt to adverse conditions. It encompasses several overlapping disciplines.</p>"
            "<ul>"
            "<li><strong>Tabletop exercises</strong> — discussion-based simulation where stakeholders walk "
            "through a disaster scenario. Low cost, no actual systems affected.</li>"
            "<li><strong>Simulation / drill</strong> — guided exercise that mimics an incident without fully "
            "activating the recovery plan.</li>"
            "<li><strong>Parallel test</strong> — recovery systems are activated and tested alongside production; "
            "production remains live.</li>"
            "<li><strong>Full interruption test</strong> — production is actually shut down and recovery systems "
            "take over. Highest confidence; highest risk.</li>"
            "<li><strong>Failover test</strong> — intentionally trigger a failover to verify HA systems work "
            "as expected.</li>"
            "<li><strong>Chaos engineering</strong> — deliberately inject failures (e.g., Netflix Chaos Monkey) "
            "into production-like systems to discover weaknesses.</li>"
            "<li><strong>Load / stress testing</strong> — verify performance under peak and beyond-peak load "
            "conditions.</li>"
            "</ul>"
            "<p><strong>BCP / DRP testing lifecycle:</strong> Plan → Test → Review → Update → Repeat. "
            "Without regular testing, plans become stale and may fail during a real event.</p>"
            "<p><strong>Metrics used in resilience:</strong> RTO, RPO, MTTR (Mean Time To Repair/Recover), "
            "MTBF (Mean Time Between Failures).</p>"
        ),
        "key_points": [
            "Tabletop: discussion only; simulation: guided drill; parallel: both systems run; full interruption: production goes down.",
            "Full interruption test gives highest confidence but carries highest operational risk.",
            "Chaos engineering proactively injects failures to find weaknesses before attackers do.",
            "MTTR measures recovery speed; MTBF measures reliability between failures.",
            "Plans must be tested regularly and updated after each exercise or real incident.",
        ],
    },
    {
        "domain": 3,
        "topic": "Power Resilience",
        "objective": "3.4",
        "video": "Power Resilience",
        "study_topics": ["Power resilience"],
        "body": (
            "<p>Power disruption is one of the most common causes of unplanned downtime. Layered power "
            "resilience ensures continuous operation during outages, fluctuations, and surges.</p>"
            "<p><strong>Power protection components:</strong></p>"
            "<ul>"
            "<li><strong>UPS (Uninterruptible Power Supply)</strong> — battery-backed device that provides "
            "immediate power during short outages and conditions power (surge/sag protection). Gives time to "
            "initiate a graceful shutdown or for a generator to start.</li>"
            "<li><strong>Generator</strong> — diesel or gas-powered generator for extended outages. Typically "
            "starts within 10-30 seconds; UPS bridges the gap.</li>"
            "<li><strong>PDU (Power Distribution Unit)</strong> — distributes conditioned power to racks; "
            "may include remote monitoring and switching.</li>"
            "<li><strong>Redundant power supplies</strong> — dual PSUs in servers; each on a separate circuit/ "
            "UPS to eliminate SPOF.</li>"
            "<li><strong>Diverse power feeds</strong> — power from two separate utility substations or "
            "circuits.</li>"
            "</ul>"
            "<p><strong>Power threats:</strong></p>"
            "<ul>"
            "<li><strong>Blackout</strong> — complete power loss.</li>"
            "<li><strong>Brownout</strong> — prolonged under-voltage.</li>"
            "<li><strong>Surge / spike</strong> — momentary over-voltage.</li>"
            "<li><strong>Sag / dip</strong> — momentary under-voltage.</li>"
            "<li><strong>EMI (Electromagnetic Interference)</strong> — can corrupt data on unshielded lines.</li>"
            "</ul>"
            "<p>Data centres typically target <strong>2N redundancy</strong> (twice the required capacity) "
            "for critical power systems.</p>"
        ),
        "key_points": [
            "UPS provides immediate battery backup and power conditioning.",
            "Generator handles extended outages; UPS bridges the startup gap (10-30 seconds).",
            "Dual PSUs on separate circuits eliminate server-level power SPOF.",
            "2N power redundancy means twice the capacity is available for failover.",
            "Brownout (low voltage) can be as damaging as a full blackout to equipment.",
        ],
    },
    {
        "domain": 3,
        "topic": "Multi-Cloud and Platform Diversity",
        "objective": "3.1",
        "video": "Multi-Cloud and Platform Diversity",
        "study_topics": ["Multi-cloud and platform diversity"],
        "body": (
            "<p><strong>Multi-cloud</strong> is the use of cloud services from two or more cloud providers "
            "(e.g., AWS + Azure + GCP). <strong>Platform diversity</strong> extends this to include different "
            "OS, hardware, hypervisor, or software vendors.</p>"
            "<p><strong>Benefits of multi-cloud / platform diversity:</strong></p>"
            "<ul>"
            "<li><strong>Vendor independence</strong> — avoids lock-in to a single provider; can negotiate "
            "pricing and switch providers.</li>"
            "<li><strong>Resilience</strong> — a cloud provider outage does not take down all workloads.</li>"
            "<li><strong>Best-of-breed services</strong> — choose the best service from each provider "
            "(e.g., AWS ML services + Azure Active Directory).</li>"
            "<li><strong>Regulatory compliance</strong> — some regulations require geographic or vendor "
            "distribution of data.</li>"
            "</ul>"
            "<p><strong>Security challenges:</strong></p>"
            "<ul>"
            "<li>Expanded attack surface — more accounts, consoles, and APIs to secure.</li>"
            "<li>Inconsistent security controls — each provider has different IAM, logging, and security "
            "tooling.</li>"
            "<li>Visibility — requires cloud-agnostic SIEM or CSPM (Cloud Security Posture Management) for "
            "unified monitoring.</li>"
            "<li>Identity federation — managing identities across multiple clouds requires a central IdP.</li>"
            "</ul>"
            "<p><strong>CSPM tools</strong> (e.g., Prisma Cloud, Wiz) continuously assess cloud configurations "
            "for misconfigurations and compliance violations across providers.</p>"
        ),
        "key_points": [
            "Multi-cloud uses two or more cloud providers to avoid vendor lock-in and increase resilience.",
            "Platform diversity reduces the risk of a single vulnerability affecting all systems.",
            "CSPM tools provide unified security posture visibility across cloud providers.",
            "Inconsistent IAM and logging across providers is a major management challenge.",
            "Central identity provider (IdP) with federation simplifies multi-cloud identity management.",
        ],
    },
    {
        "domain": 3,
        "topic": "ICS/SCADA and Embedded Systems",
        "objective": "3.1",
        "video": "ICS/SCADA and Embedded Systems",
        "study_topics": ["ICS/SCADA and embedded systems"],
        "body": (
            "<p><strong>Operational Technology (OT)</strong> refers to hardware and software that monitors and "
            "controls physical processes — distinct from IT, which processes information.</p>"
            "<p><strong>ICS (Industrial Control Systems)</strong> — umbrella term for systems controlling "
            "industrial processes.</p>"
            "<p><strong>SCADA (Supervisory Control and Data Acquisition)</strong> — large-scale ICS used in "
            "utilities (power grids, water treatment, oil pipelines). Collects data from remote sensors and "
            "issues control commands.</p>"
            "<p><strong>PLC (Programmable Logic Controller)</strong> — industrial computer that directly controls "
            "physical equipment based on programmed logic. Often the target of ICS malware (e.g., Stuxnet "
            "targeted PLCs).</p>"
            "<p><strong>Embedded systems</strong> — purpose-built computing devices with fixed functions: medical "
            "devices, vehicle ECUs, industrial sensors, smart meters.</p>"
            "<p><strong>Security challenges in ICS/SCADA/embedded:</strong></p>"
            "<ul>"
            "<li><strong>Legacy systems</strong> — many run outdated, unpatched OS (Windows XP, proprietary RTOSs)"
            " that cannot be patched without vendor involvement.</li>"
            "<li><strong>Availability priority</strong> — shutting down for maintenance may not be acceptable "
            "(24/7 operations).</li>"
            "<li><strong>Air gap</strong> — traditionally isolated from corporate/internet networks; increasingly "
            "connected for remote monitoring, increasing exposure.</li>"
            "<li><strong>Limited resources</strong> — CPU, memory, and power constraints prevent traditional "
            "security agents.</li>"
            "<li><strong>Physical consequences</strong> — a cyberattack can cause equipment damage or human "
            "safety incidents.</li>"
            "</ul>"
            "<p><strong>ICS security controls:</strong> Network segmentation (Purdue model), data diodes, "
            "unidirectional security gateways, anomaly detection (Dragos, Claroty), strict change management.</p>"
        ),
        "key_points": [
            "SCADA controls large-scale physical infrastructure; PLCs execute control logic directly.",
            "ICS/embedded systems prioritise availability — downtime may have safety consequences.",
            "Legacy, unpatched OS is a major vulnerability in OT environments.",
            "Air-gapped networks are increasingly connected, expanding the attack surface.",
            "Purdue model and network segmentation separate enterprise IT from OT networks.",
        ],
    },
    {
        "domain": 3,
        "topic": "IoT Security",
        "objective": "3.1",
        "video": "IoT Security",
        "study_topics": ["IoT security"],
        "body": (
            "<p><strong>IoT (Internet of Things)</strong> refers to internet-connected physical devices — smart "
            "TVs, thermostats, cameras, wearables, medical devices, industrial sensors.</p>"
            "<p><strong>IoT security challenges:</strong></p>"
            "<ul>"
            "<li><strong>Default credentials</strong> — devices often ship with default usernames/passwords "
            "that are rarely changed (targeted by Mirai botnet).</li>"
            "<li><strong>Limited update mechanisms</strong> — many devices lack OTA (over-the-air) update "
            "capability or users never apply updates.</li>"
            "<li><strong>Weak or absent encryption</strong> — some devices transmit data in plaintext.</li>"
            "<li><strong>Large scale</strong> — millions of devices; difficult to inventory and manage.</li>"
            "<li><strong>Physical access</strong> — devices deployed in publicly accessible locations are "
            "vulnerable to tampering.</li>"
            "<li><strong>Constrained resources</strong> — limited CPU/RAM/power prevents full security "
            "stacks.</li>"
            "</ul>"
            "<p><strong>IoT security controls:</strong></p>"
            "<ul>"
            "<li>Network segmentation — place IoT devices on dedicated VLANs, isolated from corporate "
            "systems.</li>"
            "<li>Change default credentials immediately upon deployment.</li>"
            "<li>Firmware updates — establish a process to keep device firmware current.</li>"
            "<li>Disable unused features and open ports.</li>"
            "<li>Use a dedicated IoT security platform or gateway for monitoring and policy enforcement.</li>"
            "</ul>"
            "<p><strong>Relevant frameworks:</strong> NIST IR 8259 (IoT device cybersecurity), ETSI EN 303 645 "
            "(consumer IoT security standard).</p>"
        ),
        "key_points": [
            "IoT devices often ship with default credentials — change them immediately.",
            "Segment IoT devices on separate VLANs isolated from critical systems.",
            "Mirai botnet demonstrated how default-credential IoT devices can be weaponised at scale.",
            "Limited resources on IoT devices constrain available security controls.",
            "NIST IR 8259 provides IoT cybersecurity capability baseline recommendations.",
        ],
    },
    {
        "domain": 3,
        "topic": "Architecture Trade-Offs",
        "objective": "3.1",
        "video": "Architecture Trade-offs",
        "study_topics": ["Architecture trade-offs"],
        "body": (
            "<p>Security architects must balance competing requirements. No design is perfect — every decision "
            "involves trade-offs.</p>"
            "<p><strong>Common trade-off dimensions:</strong></p>"
            "<table border='1' cellpadding='4' cellspacing='0'>"
            "<tr><th>Dimension</th><th>Trade-off</th></tr>"
            "<tr><td><strong>Security vs Availability</strong></td><td>Strict controls (fail-closed, deep "
            "inspection) can slow or block access. Relaxing controls improves availability but increases "
            "risk.</td></tr>"
            "<tr><td><strong>Security vs Performance</strong></td><td>Encryption and DPI add latency. "
            "Hardware acceleration (HSMs, ASIC-based firewalls) can mitigate but add cost.</td></tr>"
            "<tr><td><strong>Security vs Cost</strong></td><td>More controls = higher cost. Risk-based "
            "prioritisation aligns spending with actual risk level.</td></tr>"
            "<tr><td><strong>Usability vs Security</strong></td><td>Complex passwords, MFA, and strict DLP "
            "reduce user productivity. Poor usability leads to user workarounds that create new risks.</td></tr>"
            "<tr><td><strong>On-premises vs Cloud</strong></td><td>On-prem gives more control; cloud offers "
            "scalability and managed services but requires trust in the provider.</td></tr>"
            "<tr><td><strong>Centralised vs Distributed</strong></td><td>Centralised control simplifies "
            "management but creates a SPOF; distributed is resilient but harder to manage.</td></tr>"
            "</table>"
            "<p><strong>Risk-based approach:</strong> Decisions should be grounded in formal risk assessment — "
            "quantifying likelihood and impact, then applying controls proportional to risk.</p>"
            "<p><strong>Defence in depth</strong> acknowledges that no single control is perfect; layering "
            "multiple controls ensures that failure of one does not lead to complete compromise.</p>"
        ),
        "key_points": [
            "Every architectural decision involves trade-offs — security vs. availability, cost, performance, usability.",
            "Risk-based prioritisation aligns security investment with actual threat likelihood and impact.",
            "Defence in depth layers multiple controls so no single failure causes total compromise.",
            "Poor usability drives workarounds; consider user experience when designing controls.",
            "Centralised management simplifies oversight but creates a SPOF; distributed is resilient but complex.",
        ],
    },
    {
        "domain": 3,
        "topic": "Third-Party Agreement Types",
        "objective": "3.6",
        "video": "Third-Party Agreement Types",
        "study_topics": ["Third-party agreement types"],
        "body": (
            "<p>When organisations work with third parties (vendors, partners, suppliers), formal agreements "
            "define responsibilities, expectations, and security obligations.</p>"
            "<table border='1' cellpadding='4' cellspacing='0'>"
            "<tr><th>Agreement</th><th>Purpose</th></tr>"
            "<tr><td><strong>SLA (Service Level Agreement)</strong></td><td>Defines the minimum acceptable "
            "service metrics (uptime %, response time, support hours). Includes remedies for non-compliance "
            "(credits, termination).</td></tr>"
            "<tr><td><strong>MOU (Memorandum of Understanding)</strong></td><td>Informal, non-binding document "
            "expressing intent to work together. Common between government agencies.</td></tr>"
            "<tr><td><strong>MOA (Memorandum of Agreement)</strong></td><td>More formal than MOU; establishes "
            "binding commitments but without the specificity of a contract.</td></tr>"
            "<tr><td><strong>NDA (Non-Disclosure Agreement)</strong></td><td>Protects confidential information "
            "shared between parties. Can be one-way or mutual.</td></tr>"
            "<tr><td><strong>BPA (Business Partnership Agreement)</strong></td><td>Defines terms of a business "
            "relationship including IP ownership, profit sharing, and liability.</td></tr>"
            "<tr><td><strong>ISA (Interconnection Security Agreement)</strong></td><td>Governs technical and "
            "security requirements for connecting two organisations' networks (common in government/federal "
            "contexts).</td></tr>"
            "<tr><td><strong>MSA (Master Service Agreement)</strong></td><td>Framework contract covering "
            "general terms; individual engagements governed by separate SOWs.</td></tr>"
            "<tr><td><strong>SOW (Statement of Work)</strong></td><td>Defines specific deliverables, timelines, "
            "and costs for a specific project within an MSA.</td></tr>"
            "</table>"
            "<p><strong>Vendor risk management:</strong> Before engaging a vendor, conduct due diligence "
            "(security questionnaires, right-to-audit clauses, SOC 2 reports). Include security requirements "
            "in contracts and ensure vendors comply with your data handling policies.</p>"
        ),
        "key_points": [
            "SLA: measurable service commitments with remedies for non-compliance.",
            "MOU: non-binding intent; MOA: binding commitment (less formal than a contract).",
            "NDA: protects confidential information shared between parties.",
            "ISA: governs network interconnection security requirements between organisations.",
            "Include right-to-audit clauses and security requirements in vendor contracts.",
        ],
    },
    {
        "domain": 3,
        "topic": "Change Management Workflow",
        "objective": "3.6",
        "video": "Change Management Workflow",
        "study_topics": ["Change management workflow"],
        "body": (
            "<p><strong>Change management</strong> is a structured process that controls modifications to IT "
            "systems and configurations. Uncontrolled changes are a leading cause of outages and security "
            "incidents.</p>"
            "<p><strong>Typical change management workflow:</strong></p>"
            "<ol>"
            "<li><strong>Change request (CR)</strong> — initiator documents the proposed change, rationale, "
            "affected systems, and rollback plan.</li>"
            "<li><strong>Impact assessment</strong> — technical team analyses risk, resource requirements, "
            "and potential side effects. Security review is included.</li>"
            "<li><strong>CAB review (Change Advisory Board)</strong> — stakeholders review and approve, "
            "reject, or defer the change. Emergency changes may follow an expedited path.</li>"
            "<li><strong>Scheduling</strong> — change is planned for a maintenance window to minimise "
            "operational impact.</li>"
            "<li><strong>Implementation</strong> — change is applied in a controlled manner, often with "
            "a testing phase (dev → staging → production).</li>"
            "<li><strong>Verification / testing</strong> — confirm the change achieved its objective and "
            "did not cause regressions.</li>"
            "<li><strong>Documentation</strong> — update asset inventories, configuration baselines, and "
            "runbooks.</li>"
            "<li><strong>Post-implementation review (PIR)</strong> — evaluate whether the change was "
            "successful and identify lessons learned.</li>"
            "</ol>"
            "<p><strong>Security relevance:</strong> Change management prevents unauthorised modifications "
            "(integrity), ensures patches are applied consistently, and maintains an audit trail. "
            "<strong>Version control</strong> and <strong>configuration baselines</strong> support change "
            "management by tracking what the authorised state of a system is.</p>"
            "<p><strong>Emergency change</strong> — a high-priority change that bypasses the normal CAB cycle "
            "but is reviewed retrospectively.</p>"
        ),
        "key_points": [
            "Change management prevents uncontrolled modifications that cause outages and security gaps.",
            "CAB (Change Advisory Board) reviews and approves changes before implementation.",
            "Every change requires a rollback plan in case implementation fails.",
            "Emergency changes bypass normal approval but are reviewed after the fact.",
            "Configuration baselines document the authorised state; deviations are detected via audits.",
        ],
    },
]

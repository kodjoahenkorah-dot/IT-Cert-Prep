"""
Cisco CCNA 200-301 — Domain 6: Automation and Programmability
Question bank v2 (25 questions).
"""

QUESTIONS = [
    # ------------------------------------------------------------------ #
    # 6.1 / 6.2  Automation impact / Traditional vs controller-based
    # ------------------------------------------------------------------ #
    {
        "id": "cd6v2-001",
        "domain": 6,
        "objective": "6.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Automation impact",
        "stem": (
            "A service provider operates 2,000 routers. Each router requires "
            "a monthly ACL update that currently takes a technician 15 minutes "
            "per device via CLI. After deploying a network automation platform, "
            "the same update is applied to all 2,000 routers in under 10 minutes. "
            "A junior engineer claims automation also eliminates configuration "
            "drift. Which statement BEST explains why automation reduces "
            "configuration drift?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Automation replaces the running configuration with a blank "
                    "template each cycle, ensuring no legacy settings survive."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Erasing the entire running configuration each "
                    "cycle would disrupt service. Automation tools apply only "
                    "the defined desired-state changes while preserving other "
                    "configuration, and they detect deviations from the source "
                    "of truth."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Automation continuously compares the device configuration "
                    "against a versioned source of truth and remediates any "
                    "detected deviation, ensuring all devices converge to the "
                    "same desired state."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Configuration drift occurs when manual, ad-hoc "
                    "changes diverge from the intended baseline. Automation "
                    "tools (e.g., Ansible, Puppet) store desired state in a "
                    "version-controlled repository and can run continuously or "
                    "periodically to detect and correct any out-of-band changes, "
                    "keeping all devices consistent."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Automation locks device CLIs so that no engineer can make "
                    "manual changes after the first automated deployment."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Most automation platforms do not physically lock "
                    "the CLI. Engineers can still access the CLI; the reduction "
                    "in drift comes from automated enforcement and reconciliation, "
                    "not CLI lockout."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Automation converts all device configurations to read-only "
                    "files stored on the controller, preventing any future "
                    "configuration changes."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Automation stores desired-state definitions in "
                    "version control (e.g., Git), but configurations are not "
                    "made read-only on devices. Changes are still possible and "
                    "are managed through the automation pipeline."
                ),
            },
        ],
        "explanation": (
            "Configuration drift occurs when device configurations deviate from "
            "the intended baseline due to untracked manual changes. Automation "
            "reduces drift by: (1) applying changes uniformly from a single "
            "source of truth, (2) running idempotent enforcement to detect and "
            "correct deviations, and (3) providing an audit trail. This is "
            "fundamentally different from CLI management where each device "
            "may receive slightly different commands from different engineers."
        ),
    },
    {
        "id": "cd6v2-002",
        "domain": 6,
        "objective": "6.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Traditional vs controller-based",
        "stem": (
            "An enterprise currently uses a traditional network where each "
            "router independently runs OSPF to build routing tables. The "
            "enterprise is evaluating migration to a controller-based WAN "
            "solution (SD-WAN). An engineer states: 'With SD-WAN, the "
            "controller can apply centralized traffic-engineering policies "
            "that individual routers cannot implement on their own.' "
            "Which architectural reason BEST explains this advantage?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Traditional routers have smaller TCAM tables and cannot "
                    "store enough routes to implement traffic engineering."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. TCAM size is a hardware limitation unrelated "
                    "to the architectural difference between distributed and "
                    "controller-based control planes. SD-WAN's advantage is "
                    "not about TCAM capacity."
                ),
            },
            {
                "id": "b",
                "text": (
                    "A centralized controller has a global view of all WAN "
                    "paths, application SLAs, and link utilization, enabling "
                    "policies that require cross-site awareness that no single "
                    "distributed router possesses."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Distributed control planes (OSPF, BGP) make "
                    "decisions based on local topology information and protocol "
                    "metrics. A centralized SD-WAN controller aggregates "
                    "real-time telemetry from all sites, enabling application-"
                    "aware routing, SLA-based path selection, and load balancing "
                    "across all WAN paths — capabilities impossible for any "
                    "single distributed router."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Controller-based networks use faster hardware ASICs than "
                    "traditional routers, allowing more complex policy "
                    "calculations."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The advantage is architectural (centralized "
                    "global visibility), not hardware speed. Traditional routers "
                    "can have equally fast or faster ASICs for data-plane "
                    "forwarding."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Traditional OSPF networks do not support encryption, "
                    "so traffic engineering cannot be applied securely."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. OSPF supports authentication and encrypted "
                    "adjacencies. The inability to do centralized traffic "
                    "engineering in traditional networks is an architectural "
                    "limitation of distributed control planes, not an "
                    "encryption limitation."
                ),
            },
        ],
        "explanation": (
            "Traditional distributed control planes give each router a local "
            "view of the topology. A centralized controller aggregates global "
            "state (all paths, all link metrics, all application performance "
            "data) and applies policies that span the entire network — something "
            "no individual router in a distributed model can do. This is the "
            "fundamental architectural advantage of controller-based networking "
            "for traffic engineering and intent-based policy."
        ),
    },
    {
        "id": "cd6v2-003",
        "domain": 6,
        "objective": "6.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Automation impact",
        "stem": (
            "A network operations team is evaluating automation ROI. The manager "
            "asks which operational risk is MOST directly mitigated by replacing "
            "CLI-based device provisioning with an infrastructure-as-code (IaC) "
            "automation pipeline."
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Physical hardware failure, because automation platforms "
                    "include redundant compute nodes."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Automation platforms address software and "
                    "configuration management, not physical hardware failures. "
                    "Hardware redundancy is a separate design concern."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Human transcription error — a copy-paste or typing mistake "
                    "that introduces an incorrect ACL entry or interface "
                    "parameter across dozens of devices."
                ),
                "correct": True,
                "rationale": (
                    "Correct. The most direct risk mitigated by automation "
                    "is human error. When an engineer manually types the same "
                    "configuration on 50 devices, each keystroke is an "
                    "opportunity for a mistake. IaC defines configuration "
                    "once in a template, which the automation tool applies "
                    "identically to all devices, eliminating per-device "
                    "transcription errors."
                ),
            },
            {
                "id": "c",
                "text": (
                    "BGP route oscillation, because automation tools can "
                    "automatically tune BGP timers based on real-time "
                    "convergence analysis."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. BGP route oscillation is a protocol-stability "
                    "issue addressed by tuning route reflectors, route dampening, "
                    "and timers — not by automation pipelines per se. While "
                    "automation can deploy such configurations, it is not the "
                    "primary risk mitigated."
                ),
            },
            {
                "id": "d",
                "text": (
                    "DDoS attacks targeting the management plane, because "
                    "automation platforms include built-in rate limiting for "
                    "management traffic."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. DDoS protection is a security feature, not "
                    "an inherent capability of configuration-automation pipelines. "
                    "Automation tools focus on configuration consistency and "
                    "deployment speed, not traffic scrubbing."
                ),
            },
        ],
        "explanation": (
            "Infrastructure-as-code automation's primary operational benefit is "
            "eliminating human transcription errors introduced during manual CLI "
            "management. Secondary benefits include speed, repeatability, "
            "auditability (version control), and rapid rollback. The exam "
            "frequently tests understanding of what automation specifically "
            "addresses vs. what it does not replace."
        ),
    },
    # ------------------------------------------------------------------ #
    # 6.3  SDN architecture
    # ------------------------------------------------------------------ #
    {
        "id": "cd6v2-004",
        "domain": 6,
        "objective": "6.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "SDN architecture (overlay/underlay/fabric)",
        "stem": (
            "A network engineer is deploying Cisco SD-Access in a campus. "
            "The IS-IS routing protocol is running between all fabric nodes "
            "to provide IP reachability. LISP is used as the control-plane "
            "protocol for endpoint location, and VXLAN encapsulates traffic "
            "between edge nodes. An application team asks: 'Which layer "
            "carries our application traffic between buildings?' "
            "Which answer is CORRECT?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The IS-IS layer, because IS-IS routed packets carry all "
                    "application traffic directly across the campus."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. IS-IS is the underlay routing protocol that "
                    "provides IP reachability between fabric nodes. Application "
                    "traffic is not forwarded as bare IP routed by IS-IS — it "
                    "is encapsulated inside VXLAN tunnels that traverse the "
                    "IS-IS underlay."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The VXLAN overlay layer, which encapsulates application "
                    "traffic inside UDP/IP headers and carries it across the "
                    "IS-IS underlay between fabric edge nodes."
                ),
                "correct": True,
                "rationale": (
                    "Correct. In SD-Access, VXLAN is the data-plane overlay. "
                    "Application traffic is encapsulated in VXLAN (UDP port 4789) "
                    "at the ingress edge node and de-encapsulated at the egress "
                    "edge node. The IS-IS underlay simply transports the outer "
                    "IP/UDP packet. LISP handles endpoint-to-location mapping "
                    "in the control plane but does not carry application data."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The LISP layer, because LISP carries endpoint traffic "
                    "between RLOC addresses across the fabric."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. LISP is the control-plane protocol in SD-Access. "
                    "It maps endpoint identifiers (EID) to routing locators "
                    "(RLOC) so the fabric knows where to send traffic — but LISP "
                    "itself does not carry the application data. VXLAN is the "
                    "data-plane encapsulation."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The management plane, because DNA Center tunnels all "
                    "application traffic through its management VRF."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The management plane handles device management "
                    "traffic (telemetry, NETCONF, SSH). Application traffic "
                    "traverses the VXLAN overlay data plane, completely separate "
                    "from the management plane."
                ),
            },
        ],
        "explanation": (
            "SD-Access three-layer model: (1) Underlay — IS-IS routed fabric "
            "providing IP connectivity between all fabric nodes. (2) Overlay "
            "control plane — LISP maps endpoint IDs to routing locators. "
            "(3) Overlay data plane — VXLAN (UDP 4789) encapsulates and "
            "transports application traffic. DNA Center orchestrates all three. "
            "Application traffic rides the VXLAN overlay, not IS-IS or LISP."
        ),
    },
    {
        "id": "cd6v2-005",
        "domain": 6,
        "objective": "6.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SDN architecture (control/data plane)",
        "stem": (
            "In a pure OpenFlow SDN deployment, a new flow arrives at a switch "
            "and does not match any entry in the flow table. Which sequence of "
            "events CORRECTLY describes what happens next?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The switch drops the packet and generates an ICMP "
                    "Unreachable message back to the source."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. OpenFlow switches do not default to dropping "
                    "unmatched packets and sending ICMP unreachable. The standard "
                    "behavior is to send the packet to the controller via a "
                    "Packet-In message so the controller can make a forwarding "
                    "decision."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The switch buffers the packet and sends a Packet-In message "
                    "to the SDN controller; the controller installs a flow entry "
                    "and sends a Packet-Out or Flow-Mod message back to the "
                    "switch."
                ),
                "correct": True,
                "rationale": (
                    "Correct. In OpenFlow, a table-miss (no matching flow entry) "
                    "triggers a Packet-In message from the switch to the "
                    "controller. The controller evaluates the packet, decides on "
                    "an action, and responds with either a Packet-Out (to forward "
                    "this one packet) or a Flow-Mod (to install a rule for future "
                    "packets of the same flow). This is the core control-plane "
                    "interaction in OpenFlow SDN."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The switch runs its local Spanning Tree Protocol to "
                    "determine the correct outgoing port and forwards the "
                    "packet independently."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. In a pure OpenFlow SDN environment, the switch's "
                    "local control-plane protocols (STP, routing) are replaced "
                    "by the centralized controller. The switch does not "
                    "independently run STP to resolve unmatched flows."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The switch floods the packet out all ports using the "
                    "traditional MAC learning algorithm until a response "
                    "is received."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Traditional MAC flooding is a data-plane behavior "
                    "of standard Layer 2 switches. An OpenFlow switch delegates "
                    "the unmatched-flow decision to the controller, which may "
                    "instruct flooding as one option, but the switch does not "
                    "independently flood by default."
                ),
            },
        ],
        "explanation": (
            "OpenFlow control-plane interaction for table-miss: (1) Ingress "
            "switch checks the flow table — no match. (2) Switch sends Packet-In "
            "to the controller over the secure OpenFlow channel. (3) Controller "
            "processes the packet and responds with Flow-Mod (install rule) or "
            "Packet-Out (one-time forward). This interaction is the essence of "
            "SDN's centralized control plane — all forwarding decisions flow "
            "through the controller."
        ),
    },
    {
        "id": "cd6v2-006",
        "domain": 6,
        "objective": "6.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Northbound/southbound APIs",
        "stem": (
            "A company's IT service management (ITSM) platform automatically "
            "opens a DNA Center REST API call when a change ticket is approved, "
            "provisioning a new user VLAN across the fabric. Simultaneously, "
            "DNA Center uses NETCONF to push the VLAN configuration to all "
            "fabric edge switches. "
            "Which statement CORRECTLY categorizes both API interactions?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Both are southbound API interactions because both result "
                    "in device configuration changes."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The API direction is determined by the "
                    "architectural position relative to the controller, not "
                    "by whether a device is ultimately configured. The ITSM "
                    "platform is above the controller (northbound); the switches "
                    "are below (southbound)."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The ITSM-to-DNA Center REST call is a northbound API "
                    "interaction; the DNA Center-to-switch NETCONF call is a "
                    "southbound API interaction."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Northbound APIs expose the controller's capabilities "
                    "to applications, orchestration platforms, and service "
                    "management tools above the controller. Southbound APIs "
                    "connect the controller to the managed network devices below. "
                    "ITSM → DNA Center = NBI (REST). DNA Center → switches = "
                    "SBI (NETCONF)."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The ITSM-to-DNA Center call is an eastbound API because "
                    "ITSM and DNA Center are peer systems; the DNA Center-to-"
                    "switch call is a southbound API."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. East/westbound APIs describe controller-to-"
                    "controller federation, not application-to-controller "
                    "communication. The ITSM platform is an application consumer "
                    "of the controller's northbound API."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The ITSM-to-DNA Center call is a southbound API because "
                    "ITSM sits at a higher organizational layer and pushes "
                    "policies down; the DNA Center-to-switch call is a "
                    "northbound API."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The terms northbound and southbound are defined "
                    "relative to the SDN controller, not organizational hierarchy. "
                    "Anything above the controller (applications, ITSM) is "
                    "northbound; anything below (network devices) is southbound."
                ),
            },
        ],
        "explanation": (
            "SDN API reference point is always the controller: Northbound = "
            "above the controller (applications, orchestrators, ITSM, scripts). "
            "Southbound = below the controller (network devices). East/West = "
            "peer controllers. ITSM calling DNA Center REST API = NBI. "
            "DNA Center calling NETCONF on switches = SBI."
        ),
    },
    {
        "id": "cd6v2-007",
        "domain": 6,
        "objective": "6.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Northbound/southbound APIs",
        "stem": (
            "RESTCONF is described as a RESTful alternative to NETCONF for "
            "model-driven device programmability. Which statement CORRECTLY "
            "distinguishes RESTCONF from NETCONF?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "RESTCONF uses SSH as its transport, while NETCONF uses "
                    "HTTPS, making NETCONF more suitable for web-based "
                    "automation tools."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The transports are reversed: NETCONF uses SSH "
                    "(TCP port 830), and RESTCONF uses HTTPS (TCP 443). "
                    "RESTCONF is the HTTP-based interface, making it more "
                    "accessible for web tools and REST libraries."
                ),
            },
            {
                "id": "b",
                "text": (
                    "RESTCONF uses HTTP operations (GET/POST/PUT/PATCH/DELETE) "
                    "over HTTPS and supports JSON or XML encoding of YANG data, "
                    "while NETCONF uses XML-encoded RPC messages over SSH."
                ),
                "correct": True,
                "rationale": (
                    "Correct. RESTCONF (RFC 8040) maps YANG-modeled data to "
                    "HTTP resources, using standard REST methods and supporting "
                    "both JSON and XML payloads over HTTPS. NETCONF (RFC 6241) "
                    "uses XML-encoded RPC operations (get-config, edit-config, "
                    "commit) over an SSH session on port 830."
                ),
            },
            {
                "id": "c",
                "text": (
                    "RESTCONF supports candidate datastores and configuration "
                    "commit/rollback, while NETCONF only supports the running "
                    "datastore."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. It is the other way around. NETCONF supports "
                    "candidate, running, and startup datastores with commit and "
                    "rollback capabilities. RESTCONF primarily targets the "
                    "running datastore and does not natively support candidate "
                    "datastore transactions."
                ),
            },
            {
                "id": "d",
                "text": (
                    "RESTCONF and NETCONF use identical transport and encoding "
                    "but differ only in the YANG modules they support."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. RESTCONF and NETCONF differ significantly in "
                    "transport (HTTPS vs. SSH), encoding (JSON/XML vs. XML only), "
                    "and operational model (REST resource semantics vs. RPC). "
                    "Both can use the same YANG models, but they are not "
                    "identical in transport or encoding."
                ),
            },
        ],
        "explanation": (
            "NETCONF vs. RESTCONF: NETCONF — SSH transport (port 830), XML "
            "encoding, RPC-based (get-config, edit-config, commit), supports "
            "candidate/running/startup datastores, transactions with rollback. "
            "RESTCONF — HTTPS transport (port 443), JSON or XML, HTTP verbs "
            "(GET/POST/PUT/PATCH/DELETE), maps YANG to URL resources. Both use "
            "YANG data models but offer different interfaces for operators vs. "
            "developers."
        ),
    },
    # ------------------------------------------------------------------ #
    # 6.4  Cisco DNA Center
    # ------------------------------------------------------------------ #
    {
        "id": "cd6v2-008",
        "domain": 6,
        "objective": "6.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Cisco DNA Center",
        "stem": (
            "A security architect needs to enforce a policy that prevents "
            "the Finance user group from accessing the Engineering server "
            "segment without creating per-device ACLs on every switch. "
            "The campus uses Cisco SD-Access managed by DNA Center. "
            "Which DNA Center feature provides this capability?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "IP Source Guard on every access-layer switch port assigned "
                    "to Finance users."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. IP Source Guard prevents IP spoofing on a port "
                    "but does not enforce inter-segment group-based access "
                    "policies between user groups. It is not a DNA Center "
                    "feature for group segmentation."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Group-Based Policy (GBP) / TrustSec Scalable Group Tags "
                    "(SGTs), where DNA Center assigns SGTs to user groups and "
                    "the fabric enforces tag-based policies without per-device "
                    "ACL management."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Cisco SD-Access and DNA Center use Group-Based "
                    "Policy with Scalable Group Tags. Users are tagged at the "
                    "point of authentication; fabric devices enforce allow/deny "
                    "policies based on source/destination SGT pairs via the "
                    "Group-Based Policy matrix — without requiring ACLs on every "
                    "individual switch."
                ),
            },
            {
                "id": "c",
                "text": (
                    "DHCP snooping pools that assign Finance users an IP "
                    "subnet blocked by router ACLs at the distribution layer."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. DHCP snooping is a security feature that prevents "
                    "rogue DHCP servers. Subnet-based ACLs at the distribution "
                    "layer are a traditional (non-SD-Access) approach that "
                    "requires per-device ACL management — exactly what the "
                    "question is trying to avoid."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Dynamic ARP Inspection (DAI) configured on all VLANs used "
                    "by Finance and Engineering groups."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. DAI prevents ARP spoofing attacks; it does not "
                    "enforce inter-group access policy. It is a Layer 2 security "
                    "feature unrelated to user-group segmentation."
                ),
            },
        ],
        "explanation": (
            "Cisco SD-Access Group-Based Policy uses Scalable Group Tags (SGTs) "
            "assigned to users at 802.1X authentication. The DNA Center policy "
            "matrix defines which SGT-to-SGT combinations are permitted or denied. "
            "Fabric nodes enforce these policies at the VXLAN level using "
            "group-based ACLs (GBACLs), eliminating the need to manage "
            "traditional ACLs on every switch — one of SD-Access's key "
            "operational advantages."
        ),
    },
    {
        "id": "cd6v2-009",
        "domain": 6,
        "objective": "6.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Cisco DNA Center",
        "stem": (
            "A NOC engineer is using Cisco DNA Center Assurance. A switch "
            "in Building B is showing multiple client connectivity issues. "
            "DNA Center Assurance automatically correlates DHCP failures, "
            "authentication timeouts, and poor RF signal data to identify a "
            "root cause. Which DNA Center functional domain provides this "
            "capability?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Design — DNA Center's network design module correlates "
                    "site hierarchy and client issues."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The Design module in DNA Center is used to "
                    "define the network hierarchy (sites, floors, buildings), "
                    "IP address management, and templates. It does not perform "
                    "real-time telemetry correlation or root-cause analysis."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Assurance — DNA Center's network intelligence module "
                    "collects streaming telemetry, correlates events across "
                    "multiple domains, and performs AI/ML-driven root-cause "
                    "analysis."
                ),
                "correct": True,
                "rationale": (
                    "Correct. DNA Center Assurance ingests streaming telemetry "
                    "from network devices and wireless controllers. It uses "
                    "machine learning and correlation algorithms to link seemingly "
                    "separate events (DHCP failure, AAA timeout, low RSSI) to "
                    "a common root cause, enabling proactive issue resolution "
                    "that reactive SNMP polling cannot provide."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Provision — the provisioning module applies templates "
                    "and detects misconfigurations that cause client failures."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The Provision module deploys configurations "
                    "to devices. While misconfigurations can cause client "
                    "issues, real-time correlation of DHCP, authentication, "
                    "and RF telemetry for root-cause analysis is an Assurance "
                    "capability."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Platform — the DNA Center platform API gateway aggregates "
                    "events from third-party tools for root-cause analysis."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The DNA Center Platform module provides the "
                    "northbound REST API, webhooks, and integration with third-"
                    "party systems. Root-cause analysis of network events is "
                    "performed by the Assurance module using native telemetry."
                ),
            },
        ],
        "explanation": (
            "DNA Center functional domains: Design (hierarchy, IPAM, templates), "
            "Provision (deploy configs to devices), Policy (group-based access, "
            "QoS), Assurance (telemetry, health scoring, root-cause analysis), "
            "Platform (northbound APIs, integrations). For real-time correlation "
            "and root-cause analysis of client connectivity issues, Assurance "
            "is the relevant domain."
        ),
    },
    # ------------------------------------------------------------------ #
    # 6.5  REST APIs — HTTP verbs, CRUD, status codes, statelessness
    # ------------------------------------------------------------------ #
    {
        "id": "cd6v2-010",
        "domain": 6,
        "objective": "6.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "REST APIs (HTTP verbs/CRUD)",
        "stem": (
            "A network automation script needs to completely replace an "
            "existing OSPF neighbor policy object at the URI "
            "/api/v2/routing/ospf/neighbor/5 with a new definition. "
            "The script will send the entire new object in the request body. "
            "Which HTTP method and expected success code are CORRECT?"
        ),
        "options": [
            {
                "id": "a",
                "text": "POST with status 201 Created.",
                "correct": False,
                "rationale": (
                    "Incorrect. POST creates a new resource at a server-chosen "
                    "URI. Since the resource already exists at a known URI "
                    "(/neighbor/5), the correct method for full replacement "
                    "is PUT, not POST."
                ),
            },
            {
                "id": "b",
                "text": "PUT with status 200 OK or 204 No Content.",
                "correct": True,
                "rationale": (
                    "Correct. PUT replaces the entire resource at the specified "
                    "URI with the request body. Since the full object is being "
                    "sent and the URI is known, PUT is the correct idempotent "
                    "method for full replacement. Success is indicated by 200 OK "
                    "(with response body) or 204 No Content (no body)."
                ),
            },
            {
                "id": "c",
                "text": "PATCH with status 201 Created.",
                "correct": False,
                "rationale": (
                    "Incorrect. PATCH applies a partial modification, not a full "
                    "replacement. Additionally, 201 Created is returned for POST "
                    "when a new resource is created — not for PATCH of an "
                    "existing resource."
                ),
            },
            {
                "id": "d",
                "text": "DELETE followed by POST, with status 201 Created.",
                "correct": False,
                "rationale": (
                    "Incorrect. DELETE + POST is a two-step non-atomic approach "
                    "that creates a window of time where the resource does not "
                    "exist. PUT achieves atomic full replacement in a single "
                    "idempotent call."
                ),
            },
        ],
        "explanation": (
            "REST CRUD mapping: Create = POST (201), Read = GET (200), Full "
            "Replace = PUT (200/204), Partial Update = PATCH (200/204), "
            "Delete = DELETE (200/204). PUT is idempotent: sending the same "
            "PUT request multiple times produces the same resource state. Use "
            "PUT when the client knows the resource URI and is sending the "
            "complete new representation."
        ),
    },
    {
        "id": "cd6v2-011",
        "domain": 6,
        "objective": "6.5",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "REST APIs (HTTP verbs/CRUD)",
        "stem": (
            "A script sends the following REST request to a network controller:\n\n"
            "    DELETE /api/v1/interfaces/Gi0%2F1 HTTP/1.1\n"
            "    X-Auth-Token: valid_token_xyz\n\n"
            "The server responds with HTTP 403. What does this MOST likely "
            "indicate, and what action should the script take?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The token is expired; the script should re-authenticate "
                    "and obtain a new token before retrying."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. An expired or missing token returns HTTP 401 "
                    "Unauthorized. HTTP 403 Forbidden means the client IS "
                    "authenticated (the token is valid) but lacks sufficient "
                    "privilege to perform this specific action."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The resource does not exist; the script should verify "
                    "the interface name and retry with the correct URI."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A non-existent resource returns HTTP 404 Not "
                    "Found. HTTP 403 Forbidden indicates the resource exists "
                    "and the client is known, but the authorization check "
                    "failed for this operation."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The authenticated user has insufficient privileges to "
                    "delete interface objects; the script (or its service "
                    "account) needs a role with write/delete permission on "
                    "the interfaces resource."
                ),
                "correct": True,
                "rationale": (
                    "Correct. HTTP 403 Forbidden means authentication succeeded "
                    "(the token is valid and identifies the user) but the server's "
                    "authorization check denied the request. For a DELETE on "
                    "an interface object, the service account likely lacks a "
                    "network-admin or write role. The fix is to grant the "
                    "appropriate RBAC role, not to re-authenticate."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The server experienced a database error; the script should "
                    "retry the DELETE request with exponential backoff."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Server-side errors are indicated by 5xx codes "
                    "(e.g., 500 Internal Server Error, 503 Service Unavailable). "
                    "HTTP 403 is a client-side authorization failure that will "
                    "not be resolved by retrying — the underlying privilege "
                    "issue must be corrected first."
                ),
            },
        ],
        "explanation": (
            "HTTP status code distinctions: 401 Unauthorized = not authenticated "
            "(or credentials invalid/expired). 403 Forbidden = authenticated but "
            "not authorized for this resource/action. 404 Not Found = resource "
            "does not exist. 5xx = server error. A 403 on DELETE means the "
            "caller's role/permissions do not include delete rights on the "
            "target resource — an RBAC issue, not an authentication issue."
        ),
    },
    {
        "id": "cd6v2-012",
        "domain": 6,
        "objective": "6.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "REST APIs (statelessness/data encoding)",
        "stem": (
            "A developer is building a network automation tool using a REST API. "
            "She notices that every API call must include the X-Auth-Token header "
            "even though she authenticated successfully in a previous request. "
            "A colleague argues this is inefficient. Which REST constraint "
            "BEST explains why the token must be re-sent with every request?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Uniform Interface — all requests must look identical so "
                    "the server can parse them consistently."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Uniform Interface is a REST constraint about "
                    "consistent resource identification and manipulation through "
                    "representations. It does not specifically explain why "
                    "authentication must be re-included in every request."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Statelessness — the server stores no client session state "
                    "between requests, so every request must be self-contained "
                    "and include all information needed to process it, including "
                    "authentication credentials."
                ),
                "correct": True,
                "rationale": (
                    "Correct. REST's statelessness constraint (from Roy Fielding's "
                    "dissertation) requires that no session state be held on the "
                    "server between requests. The server cannot remember that "
                    "a client authenticated in a prior call, so each request "
                    "must carry its own authentication context (token, API key, "
                    "etc.)."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Layered System — intermediate proxies and load balancers "
                    "require the token in each request to route to the correct "
                    "server."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The Layered System constraint allows intermediaries "
                    "between client and server. While load balancers may benefit "
                    "from stateless requests, the fundamental reason for re-sending "
                    "authentication in each request is the statelessness constraint, "
                    "not the layered-system constraint."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Code on Demand — the server requires tokens in each response "
                    "to authorize the client to execute downloaded scripts."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Code on Demand is an optional REST constraint "
                    "allowing servers to send executable code (e.g., JavaScript) "
                    "to clients. It is unrelated to authentication token "
                    "requirements in API requests."
                ),
            },
        ],
        "explanation": (
            "REST statelessness (one of six REST constraints): the server must "
            "not store client session state. Every request must be self-contained, "
            "including authentication (token/key), resource identifiers, and "
            "any required parameters. This improves scalability (any server "
            "replica can handle any request) and visibility (intermediaries "
            "can see the complete request), at the cost of slightly larger "
            "request payloads."
        ),
    },
    {
        "id": "cd6v2-013",
        "domain": 6,
        "objective": "6.5",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "REST APIs (HTTP verbs/CRUD)",
        "stem": (
            "A script sends a REST API call to retrieve device inventory from "
            "Cisco DNA Center:\n\n"
            "    GET /dna/intent/api/v1/network-device HTTP/1.1\n"
            "    X-Auth-Token: <valid_token>\n\n"
            "The response body is a JSON array of device objects. The script "
            "must extract only devices where 'reachabilityStatus' is 'Reachable'. "
            "Which approach is CORRECT given that REST APIs are stateless?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Issue a separate authenticated GET request for each device "
                    "and let the server remember the filter from the first request."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. REST statelessness means the server retains no "
                    "filter state between requests. Each request is independent; "
                    "the server cannot remember a filter set in a previous call."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Parse the full JSON response locally in the script and "
                    "filter objects where 'reachabilityStatus' == 'Reachable', "
                    "or use a query parameter such as "
                    "?reachabilityStatus=Reachable if the API supports it — "
                    "including the X-Auth-Token in each request."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Because the API is stateless, filtering is either "
                    "done client-side by parsing the response, or server-side "
                    "using query parameters in a self-contained request. There "
                    "is no server-side session that remembers prior filters. "
                    "Each request must include the auth token independently."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Establish a WebSocket session so the server can push only "
                    "reachable devices without re-sending the entire list."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. WebSockets are a different protocol that provides "
                    "persistent, bidirectional connections and is not a standard "
                    "REST mechanism. DNA Center's REST inventory API is a "
                    "stateless request/response model, not a streaming WebSocket."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Use a DELETE request with a filter body to remove "
                    "unreachable devices from the response before the GET "
                    "returns the filtered list."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. DELETE removes resources from the server — it "
                    "does not filter GET responses. GET retrieves resources; "
                    "filtering is done via query parameters or client-side "
                    "parsing of the response."
                ),
            },
        ],
        "explanation": (
            "REST statelessness in practice: the server never maintains request "
            "context between calls. All filtering, authentication, and parameters "
            "must be included in each individual request. For DNA Center inventory "
            "filtering: (1) use query parameters in the GET URL if the API "
            "supports them (?reachabilityStatus=Reachable), or (2) retrieve "
            "the full list and filter client-side in Python using a list "
            "comprehension or similar construct."
        ),
    },
    # ------------------------------------------------------------------ #
    # 6.6  Configuration management — Ansible, Puppet, Chef
    # ------------------------------------------------------------------ #
    {
        "id": "cd6v2-014",
        "domain": 6,
        "objective": "6.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Configuration management (Ansible/Puppet/Chef)",
        "stem": (
            "An engineer writes the following Ansible task in a playbook:\n\n"
            "    - name: Ensure NTP server is configured\n"
            "      cisco.ios.ios_ntp_global:\n"
            "        config:\n"
            "          servers:\n"
            "            - server: 192.0.2.123\n"
            "        state: merged\n\n"
            "The playbook is executed five times. After the fifth execution, "
            "how many NTP server entries for 192.0.2.123 exist in the device "
            "configuration, and why?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Five entries, because Ansible appends a new entry each "
                    "time the task runs."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Ansible modules for Cisco IOS (from the "
                    "cisco.ios collection) are designed to be idempotent. "
                    "The module checks whether 192.0.2.123 is already in the "
                    "NTP configuration; if it is, the task reports 'ok' and "
                    "makes no change."
                ),
            },
            {
                "id": "b",
                "text": (
                    "One entry, because the Ansible ios_ntp_global module is "
                    "idempotent — it checks the existing configuration state "
                    "and only applies changes when the desired state differs "
                    "from the current state."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Idempotency is a fundamental Ansible property. "
                    "The ios_ntp_global module with state: merged checks whether "
                    "the NTP server already exists. If present, it takes no action. "
                    "Running the playbook five times results in exactly the same "
                    "configuration as running it once — one NTP server entry."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Zero entries, because 'state: merged' first deletes "
                    "all existing NTP servers before applying the new list."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. 'state: merged' adds or updates configuration "
                    "without removing existing entries. 'state: replaced' or "
                    "'state: overridden' would be used to remove existing "
                    "entries not in the specified list."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The result is unpredictable because Ansible does not "
                    "guarantee idempotency for network device modules."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Cisco IOS network resource modules in the "
                    "cisco.ios collection are explicitly designed to be "
                    "idempotent, checking device state before making changes. "
                    "This is a documented and testable guarantee."
                ),
            },
        ],
        "explanation": (
            "Ansible idempotency for network modules: resource modules "
            "(ios_ntp_global, ios_vlans, etc.) follow a get-diff-apply pattern: "
            "(1) gather current device state, (2) compute the diff between "
            "desired and current, (3) apply only the changes needed. If the "
            "desired state already matches the current state, no CLI commands "
            "are sent and the task returns 'ok' rather than 'changed'."
        ),
    },
    {
        "id": "cd6v2-015",
        "domain": 6,
        "objective": "6.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Configuration management (Ansible/Puppet/Chef)",
        "stem": (
            "A network team is debating whether to use Puppet or Chef for "
            "configuration management. A senior engineer states: 'Both Puppet "
            "and Chef require a software agent running on each managed node.' "
            "Which additional characteristic do Puppet and Chef SHARE that "
            "distinguishes them from Ansible?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Both Puppet and Chef use YAML-formatted playbooks to "
                    "define desired state, identical to Ansible."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Ansible uses YAML playbooks. Puppet uses its "
                    "own declarative DSL (Puppet language, .pp files). Chef "
                    "uses Ruby-based cookbooks and recipes. Neither uses "
                    "YAML playbooks in the Ansible sense."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Both Puppet and Chef use a pull model in which the agent "
                    "on the managed node periodically contacts the master/server "
                    "to retrieve and enforce configuration."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Both Puppet and Chef are pull-model systems: the "
                    "Puppet agent polls the Puppet master (default every 30 min) "
                    "and the Chef client polls the Chef server to retrieve "
                    "catalogs/cookbooks and enforce local state. Ansible uses "
                    "a push model where the control node initiates connections "
                    "to managed nodes."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Both Puppet and Chef are agentless and use SSH as their "
                    "primary transport, like Ansible."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Puppet and Chef are agent-based. Ansible is the "
                    "agentless tool in the set. Puppet and Chef require client "
                    "software installed on managed nodes."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Both Puppet and Chef are push-based, sending configuration "
                    "from the master directly to managed nodes via encrypted "
                    "SSH sessions."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Puppet and Chef are pull-based, not push-based. "
                    "The nodes initiate connections to the server to retrieve "
                    "their configuration catalogs. This is the opposite of "
                    "Ansible's push model."
                ),
            },
        ],
        "explanation": (
            "Configuration management comparison: Ansible — agentless, push "
            "(control node initiates via SSH/API), YAML playbooks. Puppet — "
            "agent-based, pull (Puppet agent polls master ~every 30 min), "
            "Puppet DSL (.pp files). Chef — agent-based, pull (Chef client "
            "polls Chef server), Ruby cookbooks/recipes. The two shared "
            "characteristics of Puppet and Chef that differ from Ansible are: "
            "agent-based and pull model."
        ),
    },
    {
        "id": "cd6v2-016",
        "domain": 6,
        "objective": "6.6",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Configuration management (Ansible/Puppet/Chef)",
        "stem": (
            "An Ansible playbook for configuring 100 Cisco routers fails on "
            "router #47 due to an SSH timeout. The engineer re-runs the "
            "playbook immediately. Which outcome BEST describes what happens "
            "to routers 1–46 that were successfully configured in the first run?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Routers 1–46 receive duplicate configuration entries "
                    "because Ansible re-applies the configuration without "
                    "checking current state."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Ansible network resource modules are idempotent. "
                    "On the second run, the module checks current device state "
                    "and finds routers 1–46 already in the desired state, so "
                    "no changes are applied — no duplicates are created."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Routers 1–46 report 'ok' (no changes) because Ansible's "
                    "idempotent modules detect that the desired state is already "
                    "present; only router 47 (and 48–100 if not yet reached) "
                    "receive actual changes."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Idempotency means the second run is safe to execute "
                    "on all 100 routers. Routers 1–46 already have the correct "
                    "configuration, so the module reports 'ok' without making "
                    "changes. Router 47 will be retried and routers 48–100 will "
                    "be newly configured. This makes automation re-runnable "
                    "without side effects."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The engineer must use 'ansible-playbook --skip-tags' to "
                    "manually exclude routers 1–46 from the second run to "
                    "prevent configuration corruption."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Because Ansible modules are idempotent, there "
                    "is no need to manually exclude already-configured devices. "
                    "Re-running the full playbook is safe — successfully configured "
                    "devices will simply report 'ok' with no changes applied."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Ansible automatically rolls back routers 1–46 to their "
                    "pre-playbook state before retrying from the beginning."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Ansible does not perform automatic rollback of "
                    "successful tasks when a later task fails. Rollback requires "
                    "explicit 'block/rescue' logic or separate rollback playbooks. "
                    "The default behavior is to continue from where the failure "
                    "occurred on a re-run."
                ),
            },
        ],
        "explanation": (
            "Idempotency makes automation re-runnable: because Ansible modules "
            "check current device state before applying changes, re-executing "
            "a playbook on already-configured devices produces 'ok' (no change) "
            "rather than 'changed' (config applied). This is critical for "
            "fault recovery — the engineer can simply re-run the full playbook "
            "after fixing the connectivity issue on router 47, without worrying "
            "about corrupting already-correct configurations."
        ),
    },
    # ------------------------------------------------------------------ #
    # 6.7  JSON — syntax, data types, valid vs. invalid
    # ------------------------------------------------------------------ #
    {
        "id": "cd6v2-017",
        "domain": 6,
        "objective": "6.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "JSON data format",
        "stem": (
            "A Python script uses json.loads() to parse the following "
            "response from a network controller API:\n\n"
            "    {\n"
            "        \"site\": \"HQ\",\n"
            "        \"vlans\": [\n"
            "            {\"id\": 10, \"name\": \"Data\", \"active\": true},\n"
            "            {\"id\": 20, \"name\": \"Voice\", \"active\": false}\n"
            "        ],\n"
            "        \"managed\": null\n"
            "    }\n\n"
            "After parsing, which Python expression evaluates to False "
            "WITHOUT raising an exception?"
        ),
        "options": [
            {
                "id": "a",
                "text": "data['vlans'][0]['active'] == False",
                "correct": False,
                "rationale": (
                    "Incorrect. data['vlans'][0]['active'] is True (JSON true "
                    "maps to Python True). The expression True == False evaluates "
                    "to False — however, this would NOT raise an exception, "
                    "so this is a plausible answer. But the intended trick is "
                    "that index 0 is the 'Data' VLAN where active is true. "
                    "Comparing True == False gives False. So this expression "
                    "DOES evaluate to False without exception, but option B is "
                    "more precisely targeting the second VLAN's active field "
                    "which is directly False."
                ),
            },
            {
                "id": "b",
                "text": "data['vlans'][1]['active']",
                "correct": True,
                "rationale": (
                    "Correct. data['vlans'][1] is the second VLAN object "
                    "{'id': 20, 'name': 'Voice', 'active': False}. Accessing "
                    "['active'] returns Python's False (JSON false maps directly "
                    "to Python False). This expression evaluates to False without "
                    "raising an exception."
                ),
            },
            {
                "id": "c",
                "text": "data['vlans']['Voice']['active']",
                "correct": False,
                "rationale": (
                    "Incorrect. 'vlans' is a JSON array (Python list), not a "
                    "dictionary. Accessing it with string key 'Voice' raises a "
                    "TypeError. List elements must be accessed by integer index."
                ),
            },
            {
                "id": "d",
                "text": "data['managed'] == None",
                "correct": False,
                "rationale": (
                    "Incorrect (it does evaluate to True, not False). JSON null "
                    "maps to Python None. None == None is True. Also, Pythonic "
                    "style uses 'is None' rather than '== None', but neither "
                    "raises an exception. However, this evaluates to True, "
                    "not False."
                ),
            },
        ],
        "explanation": (
            "JSON-to-Python type mapping: object → dict, array → list, "
            "string → str, number → int/float, true → True, false → False, "
            "null → None. After json.loads(), arrays are Python lists accessed "
            "by zero-based integer index; objects are dicts accessed by string "
            "key. data['vlans'][1]['active'] = the Voice VLAN's active field = "
            "Python False."
        ),
    },
    {
        "id": "cd6v2-018",
        "domain": 6,
        "objective": "6.7",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "JSON data format",
        "stem": (
            "Which of the following JSON snippets contains a syntax error "
            "that would cause json.loads() in Python to raise a ValueError?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "{\"router\": \"R1\", \"neighbors\": [], \"bgp_as\": 65001}"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect (this IS valid JSON). An empty array [] is valid, "
                    "and bgp_as is a correctly unquoted integer. All keys are "
                    "double-quoted strings. No syntax error."
                ),
            },
            {
                "id": "b",
                "text": (
                    "{\"interface\": \"Gi0/0\", \"shutdown\": False}"
                ),
                "correct": True,
                "rationale": (
                    "Correct — this IS invalid JSON. JSON booleans must be "
                    "lowercase: 'false' (not 'False'). 'False' with a capital F "
                    "is Python syntax, not JSON syntax. json.loads() would raise "
                    "a ValueError (json.JSONDecodeError) because 'False' is not "
                    "a recognized JSON value."
                ),
            },
            {
                "id": "c",
                "text": (
                    "{\"vlan\": 100, \"name\": \"Prod\", \"tagged\": true}"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect (this IS valid JSON). 'true' (lowercase) is the "
                    "correct JSON boolean literal. All keys are quoted, vlan is "
                    "an unquoted integer. This is syntactically correct JSON."
                ),
            },
            {
                "id": "d",
                "text": (
                    "{\"prefix\": \"10.0.0.0/8\", \"metric\": 0, "
                    "\"redistribute\": null}"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect (this IS valid JSON). 'null' (lowercase) is the "
                    "correct JSON null literal, 0 is a valid number, and all "
                    "keys are double-quoted strings. No syntax error."
                ),
            },
        ],
        "explanation": (
            "JSON is case-sensitive for its literal values. The valid literals "
            "are: true, false, null — all lowercase. Python programmers commonly "
            "mistake Python's True/False/None for JSON's true/false/null. "
            "Other common JSON syntax errors: single-quoted strings, unquoted "
            "keys, trailing commas after the last element. Always use json.dumps() "
            "to serialize Python to JSON (it converts True→true, False→false, "
            "None→null automatically)."
        ),
    },
    {
        "id": "cd6v2-019",
        "domain": 6,
        "objective": "6.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "JSON data format",
        "stem": (
            "A network controller returns the following JSON to an automation "
            "script:\n\n"
            "    {\n"
            "        \"links\": [\n"
            "            {\"src\": \"SW1\", \"dst\": \"SW2\", \"capacity\": 10},\n"
            "            {\"src\": \"SW2\", \"dst\": \"SW3\", \"capacity\": 1},\n"
            "            {\"src\": \"SW1\", \"dst\": \"SW3\", \"capacity\": 10}\n"
            "        ]\n"
            "    }\n\n"
            "The script must build a list of all link sources where capacity "
            "equals 10. Which Python expression produces [\"SW1\", \"SW1\"]?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "[link['src'] for link in data['links'] "
                    "if link['capacity'] == 10]"
                ),
                "correct": True,
                "rationale": (
                    "Correct. This Python list comprehension iterates over all "
                    "objects in the 'links' array and selects the 'src' field "
                    "for any link where 'capacity' equals the integer 10. "
                    "This produces ['SW1', 'SW1'] — the sources of the two "
                    "10-Gbps links."
                ),
            },
            {
                "id": "b",
                "text": (
                    "[link['src'] for link in data['links'] "
                    "if link['capacity'] == '10']"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. In the JSON, 'capacity' is a number (integer 10), "
                    "not a string. Comparing with '10' (a Python string) would "
                    "never match because 10 (int) != '10' (str). The list "
                    "comprehension would produce an empty list."
                ),
            },
            {
                "id": "c",
                "text": (
                    "[data['links']['capacity'] == 10]"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. data['links'] is a Python list, not a dictionary. "
                    "Accessing it with string key 'capacity' raises a TypeError. "
                    "Each element of the list must be accessed by integer index "
                    "or iterated."
                ),
            },
            {
                "id": "d",
                "text": (
                    "data['links'][0]['src'] + data['links'][2]['src']"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This would produce the string 'SW1SW1' (string "
                    "concatenation) rather than a list ['SW1', 'SW1']. The "
                    "question asks for a list, and this approach is also "
                    "hardcoded to specific indices rather than filtering "
                    "by capacity."
                ),
            },
        ],
        "explanation": (
            "Working with parsed JSON in Python: json.loads() converts JSON "
            "arrays to Python lists and JSON objects to Python dicts. JSON "
            "numbers without quotes are Python ints or floats. List "
            "comprehensions with conditional filters are the idiomatic way "
            "to extract matching elements. Always compare JSON numbers to "
            "Python numbers (int/float), not strings, to avoid type mismatch."
        ),
    },
    # ------------------------------------------------------------------ #
    # Multiple-response questions (4 total, spread across topics)
    # ------------------------------------------------------------------ #
    {
        "id": "cd6v2-020",
        "domain": 6,
        "objective": "6.5",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "REST APIs (HTTP verbs/CRUD)",
        "stem": (
            "Select TWO statements that are TRUE about HTTP DELETE requests "
            "in a REST API for network resource management."
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A successful DELETE that removes a resource and returns "
                    "no response body should return HTTP 204 No Content."
                ),
                "correct": True,
                "rationale": (
                    "Correct. HTTP 204 No Content is a standard success response "
                    "for DELETE (and some PUT/PATCH) when the operation succeeds "
                    "but there is no content to return in the response body. "
                    "HTTP 200 OK is also acceptable if the server returns a "
                    "confirmation body."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Sending the same DELETE request for an already-deleted "
                    "resource is guaranteed to always return HTTP 204, because "
                    "DELETE is idempotent."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. DELETE is idempotent in the sense that deleting "
                    "an already-deleted resource leaves the server in the same "
                    "state (resource absent). However, most REST APIs return "
                    "HTTP 404 Not Found on the second DELETE because the resource "
                    "no longer exists. Idempotency refers to the server state "
                    "outcome, not the HTTP response code."
                ),
            },
            {
                "id": "c",
                "text": (
                    "A DELETE request does not require an authentication token "
                    "because it does not retrieve sensitive data."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. REST APIs require authentication for all operations "
                    "including DELETE, which is often the most privileged operation. "
                    "Omitting the auth token on DELETE will typically return "
                    "HTTP 401 Unauthorized. The statelessness constraint means "
                    "every request must carry authentication."
                ),
            },
            {
                "id": "d",
                "text": (
                    "DELETE requests target a specific resource URI (e.g., "
                    "/api/v1/vlans/10) and do not include a request body in "
                    "most REST API implementations."
                ),
                "correct": True,
                "rationale": (
                    "Correct. DELETE operations identify the resource to be "
                    "removed via the URI, not a request body. While the HTTP "
                    "specification does not prohibit a body on DELETE, most "
                    "REST APIs and network controllers do not use one — the URI "
                    "alone identifies the resource."
                ),
            },
        ],
        "explanation": (
            "HTTP DELETE semantics: (1) The target resource is identified by "
            "URI. (2) Successful deletion with no response body → 204 No Content; "
            "with body → 200 OK. (3) Deleting a non-existent resource typically "
            "returns 404 (although the end-state — resource absent — is the same, "
            "hence DELETE is considered idempotent in the RFC). (4) Authentication "
            "is always required for REST API calls — no exceptions."
        ),
    },
    {
        "id": "cd6v2-021",
        "domain": 6,
        "objective": "6.3",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "SDN architecture (overlay/underlay/fabric)",
        "stem": (
            "Select TWO characteristics that describe the UNDERLAY network "
            "in a Cisco SD-Access fabric."
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The underlay provides IP reachability between all fabric "
                    "nodes using a routed protocol such as IS-IS."
                ),
                "correct": True,
                "rationale": (
                    "Correct. The SD-Access underlay is a fully routed IP network "
                    "(Cisco recommends IS-IS or OSPF) that provides connectivity "
                    "between all fabric nodes — edge, border, and control-plane "
                    "nodes. This IP reachability is what allows VXLAN tunnels "
                    "(the overlay) to form between fabric nodes."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The underlay encapsulates endpoint traffic in VXLAN "
                    "headers to provide virtual network segmentation."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. VXLAN encapsulation is an overlay function. "
                    "The underlay carries the outer IP/UDP VXLAN packets as "
                    "ordinary IP packets but does not itself perform VXLAN "
                    "encapsulation — that is done by fabric edge nodes."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The underlay network is a routed access design where all "
                    "fabric switches have Layer 3 connectivity to adjacent nodes, "
                    "eliminating spanning tree in the fabric."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Cisco SD-Access uses a routed access underlay "
                    "design. All fabric links are routed (Layer 3) point-to-point "
                    "connections, which eliminates Spanning Tree Protocol (STP) "
                    "from the fabric core. This is a significant operational "
                    "simplification compared to traditional Layer 2 campus designs."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The underlay is managed by LISP, which maps endpoint "
                    "MAC addresses to their physical switch locations."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. LISP is the SD-Access control-plane protocol "
                    "for the overlay — it maps endpoint identifiers (EIDs, which "
                    "are IP or MAC addresses) to routing locators (RLOCs, which "
                    "are fabric node IP addresses). LISP operates at the overlay "
                    "control plane, not the underlay."
                ),
            },
        ],
        "explanation": (
            "SD-Access underlay characteristics: (1) Fully routed IP network "
            "(IS-IS recommended for fast convergence), no STP in the fabric. "
            "(2) Provides IP reachability between all fabric nodes. (3) Carries "
            "VXLAN-encapsulated overlay traffic as ordinary IP/UDP packets. "
            "Overlay characteristics: VXLAN data plane + LISP control plane, "
            "managed by DNA Center. Keeping underlay and overlay roles distinct "
            "is a key CCNA exam topic."
        ),
    },
    {
        "id": "cd6v2-022",
        "domain": 6,
        "objective": "6.6",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Configuration management (Ansible/Puppet/Chef)",
        "stem": (
            "Select TWO statements that are TRUE about Chef when used for "
            "infrastructure configuration management."
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Chef uses a pull model: the Chef client on each managed "
                    "node periodically contacts the Chef server to retrieve "
                    "and apply cookbooks."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Chef is pull-based. The Chef client (agent) runs "
                    "on each managed node and contacts the Chef server at regular "
                    "intervals (chef-client runs) to download the latest "
                    "cookbooks and recipes and enforce the desired state locally."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Chef is agentless — it connects to managed nodes over SSH "
                    "from a central workstation without requiring any software "
                    "on the nodes."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Chef requires the Chef client (chef-client) "
                    "to be installed on each managed node. Agentless SSH-based "
                    "operation is Ansible's model, not Chef's."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Chef configuration logic is written in Ruby-based cookbooks "
                    "and recipes, not YAML playbooks."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Chef uses Ruby as its domain-specific language. "
                    "Configuration logic is organized into cookbooks (collections "
                    "of recipes, attributes, templates, and resources). This "
                    "distinguishes Chef from Ansible (YAML playbooks) and Puppet "
                    "(Puppet DSL .pp manifests)."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Chef uses a push model — the Chef server proactively "
                    "distributes new cookbooks to all registered nodes "
                    "immediately upon upload."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Chef is pull-based. The Chef server does not "
                    "proactively push cookbooks. Nodes pull on their own schedule "
                    "(triggered by chef-client runs). Chef Push Jobs is an add-on "
                    "that can trigger on-demand runs, but the default model is pull."
                ),
            },
        ],
        "explanation": (
            "Chef summary for CCNA: Agent-based (chef-client on each node), "
            "pull model (nodes poll Chef server), Ruby-based cookbooks and "
            "recipes, requires Chef server infrastructure. Compare: Puppet = "
            "agent-based + pull + Puppet DSL. Ansible = agentless + push + "
            "YAML. Understanding agent/agentless and push/pull for all three "
            "tools is heavily tested."
        ),
    },
    {
        "id": "cd6v2-023",
        "domain": 6,
        "objective": "6.7",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "JSON data format",
        "stem": (
            "Select TWO statements that are TRUE about JSON syntax rules "
            "as defined in RFC 8259."
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "JSON object keys must always be strings enclosed in "
                    "double quotes; single-quoted keys or unquoted keys are "
                    "not valid JSON."
                ),
                "correct": True,
                "rationale": (
                    "Correct. RFC 8259 specifies that all JSON object member "
                    "names (keys) must be strings, and strings must be enclosed "
                    "in double quotation marks. Single quotes and unquoted keys "
                    "are valid JavaScript but invalid JSON."
                ),
            },
            {
                "id": "b",
                "text": (
                    "JSON supports comments using the // or /* */ syntax "
                    "to document configuration intent."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. JSON does NOT support comments. RFC 8259 "
                    "explicitly excludes comments from the JSON specification. "
                    "Adding // or /* */ comments to a JSON document makes it "
                    "invalid and will cause a parse error. This is a common "
                    "misconception for engineers coming from YAML (which does "
                    "support # comments)."
                ),
            },
            {
                "id": "c",
                "text": (
                    "A trailing comma after the last element of a JSON array "
                    "or the last key-value pair of a JSON object is not "
                    "permitted and causes a parse error."
                ),
                "correct": True,
                "rationale": (
                    "Correct. JSON does not allow trailing commas. The last "
                    "element in an array or the last member in an object must "
                    "not be followed by a comma. For example, "
                    "[\"a\", \"b\",] is invalid JSON. This is another common "
                    "error for developers accustomed to JavaScript or Python."
                ),
            },
            {
                "id": "d",
                "text": (
                    "JSON arrays are unordered collections, so parsers may "
                    "return elements in any sequence."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. JSON ARRAYS are ordered — elements maintain "
                    "their defined sequence. It is JSON OBJECTS (key-value "
                    "pairs) that are technically unordered per the specification "
                    "(though most parsers preserve insertion order). Arrays "
                    "are always ordered and zero-indexed."
                ),
            },
        ],
        "explanation": (
            "Critical JSON rules (RFC 8259): (1) Keys must be double-quoted "
            "strings. (2) No comments supported. (3) No trailing commas. "
            "(4) Boolean literals are lowercase: true/false. (5) Null literal "
            "is lowercase: null. (6) Arrays are ordered (zero-indexed); objects "
            "are unordered key-value pairs. (7) Strings use double quotes only."
        ),
    },
    # ------------------------------------------------------------------ #
    # Additional coverage — rounding out study topics
    # ------------------------------------------------------------------ #
    {
        "id": "cd6v2-024",
        "domain": 6,
        "objective": "6.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Traditional vs controller-based",
        "stem": (
            "A large enterprise currently manages its WAN using traditional "
            "per-device MPLS configurations. The team is evaluating Cisco "
            "SD-WAN (Viptela). A colleague argues: 'SD-WAN is just MPLS "
            "with a web GUI.' Which statement MOST accurately refutes this "
            "claim by identifying a fundamental architectural difference?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "SD-WAN encrypts all traffic with IPsec, while MPLS "
                    "transmits traffic in plaintext."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. While SD-WAN typically applies IPsec encryption "
                    "over public internet transports, MPLS can also be used "
                    "with encryption. Encryption is a feature difference, not "
                    "the fundamental architectural difference."
                ),
            },
            {
                "id": "b",
                "text": (
                    "In traditional MPLS, each PE router makes independent "
                    "forwarding decisions using distributed control plane "
                    "protocols (LDP, BGP). SD-WAN centralizes policy and path "
                    "selection in a vSmart controller, enabling application-aware "
                    "routing and centralized policy enforcement across all edges."
                ),
                "correct": True,
                "rationale": (
                    "Correct. This is the fundamental architectural difference. "
                    "Traditional MPLS uses distributed control planes (LDP for "
                    "label distribution, BGP for VPN route exchange) on each "
                    "PE router. Cisco SD-WAN centralizes policy in the vSmart "
                    "controller, which distributes OMP routes and policies to "
                    "edge vEdge/cEdge routers — enabling centralized application-"
                    "aware routing, SLA-based path selection, and zero-touch "
                    "provisioning that traditional MPLS cannot provide."
                ),
            },
            {
                "id": "c",
                "text": (
                    "SD-WAN eliminates the need for any routing protocol, "
                    "while MPLS requires LDP and BGP on every device."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. SD-WAN uses OMP (Overlay Management Protocol) "
                    "as its control-plane protocol between vEdge routers and "
                    "the vSmart controller. It does not eliminate routing "
                    "protocols; it replaces traditional distributed protocols "
                    "with a centralized overlay routing protocol."
                ),
            },
            {
                "id": "d",
                "text": (
                    "SD-WAN supports VLANs while traditional MPLS does not, "
                    "making SD-WAN more suitable for campus networks."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Both MPLS and SD-WAN can carry VLAN-tagged "
                    "traffic. VLAN support is not the differentiating factor "
                    "between traditional MPLS WAN and SD-WAN architectures."
                ),
            },
        ],
        "explanation": (
            "Traditional MPLS WAN vs. Cisco SD-WAN: MPLS uses distributed "
            "control planes (LDP, BGP VPNv4) on each PE, with per-device "
            "configuration. SD-WAN centralizes policy in the vSmart controller "
            "(control plane) and the vBond orchestrator (onboarding); vEdge/"
            "cEdge routers implement the data plane. The result is centralized "
            "application-aware routing, SLA policies, and zero-touch provisioning "
            "that distributed MPLS cannot match."
        ),
    },
    {
        "id": "cd6v2-025",
        "domain": 6,
        "objective": "6.5",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "REST APIs (statelessness/data encoding)",
        "stem": (
            "A network automation script sends the following REST API request "
            "to a controller:\n\n"
            "    POST /api/v2/config/push HTTP/1.1\n"
            "    Content-Type: application/json\n"
            "    Accept: application/json\n"
            "    X-Auth-Token: tok_abc\n\n"
            "    {\n"
            "        \"devices\": [\"R1\", \"R2\"],\n"
            "        \"template\": \"ntp-baseline\"\n"
            "    }\n\n"
            "The server returns HTTP 202. What does this status code indicate?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The resource was created successfully and is immediately "
                    "available at the URI specified in the Location header."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. HTTP 201 Created indicates a new resource was "
                    "created and is available. HTTP 202 Accepted is a different "
                    "status code meaning the request was received but processing "
                    "is not yet complete."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The request has been accepted for processing, but the "
                    "configuration push to R1 and R2 has not yet completed — "
                    "the script should poll a status endpoint to determine "
                    "when the operation finishes."
                ),
                "correct": True,
                "rationale": (
                    "Correct. HTTP 202 Accepted means the server received and "
                    "validated the request but the action is being performed "
                    "asynchronously. For long-running operations like pushing "
                    "configuration to multiple devices, controllers return 202 "
                    "immediately with a task/job ID. The client polls a status "
                    "endpoint (e.g., /api/v2/tasks/{task_id}) to track completion."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The server partially processed the request — R1 was "
                    "configured successfully but R2 failed."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. HTTP 207 Multi-Status (used in WebDAV) or a "
                    "custom response body would indicate partial success. "
                    "HTTP 202 Accepted simply means the request was accepted "
                    "for asynchronous processing — it does not indicate partial "
                    "success or failure."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The request body was syntactically valid but the server "
                    "needs additional parameters; the script should resend "
                    "with more detail."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A request requiring additional parameters would "
                    "return HTTP 400 Bad Request or 422 Unprocessable Entity. "
                    "HTTP 202 Accepted indicates the request was sufficient and "
                    "accepted — processing just hasn't completed yet."
                ),
            },
        ],
        "explanation": (
            "HTTP 202 Accepted is used for asynchronous operations: the server "
            "received the request and will process it, but cannot guarantee "
            "completion by the time it responds. Common in network automation "
            "APIs where device provisioning is time-consuming. The response "
            "typically includes a task or job ID so the client can poll a "
            "status endpoint. Compare: 200 OK (sync success), 201 Created "
            "(resource created), 202 Accepted (async accepted), 204 No Content "
            "(sync success, no body)."
        ),
    },
]

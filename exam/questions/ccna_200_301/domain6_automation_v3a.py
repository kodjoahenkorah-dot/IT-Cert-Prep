"""
Cisco CCNA 200-301 — Domain 6: Automation and Programmability
Question bank v3 (40 questions).
"""

QUESTIONS = [
    # ------------------------------------------------------------------ #
    # 6.1  Automation impact
    # ------------------------------------------------------------------ #
    {
        "id": "cd6v3-001",
        "domain": 6,
        "objective": "6.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Automation impact",
        "stem": (
            "A large enterprise currently requires three engineers to spend two "
            "days each quarter manually auditing interface descriptions on 400 "
            "routers via CLI. After deploying a network automation platform, the "
            "same audit is completed in 12 minutes by a single script. Beyond "
            "speed, which ADDITIONAL operational benefit does automation provide "
            "in this scenario?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The automation platform replaces the need for OSPF because "
                    "routing decisions are now made centrally."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Automation tools that audit or configure devices "
                    "do not replace routing protocols. OSPF still runs on the "
                    "devices; automation merely interacts with device configuration "
                    "and state."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The script applies a uniform audit standard to every device, "
                    "eliminating human inconsistency where different engineers "
                    "might check or record results differently."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Automation enforces consistency: every device is "
                    "checked with the same logic, recorded in the same format, and "
                    "subjected to the same criteria — eliminating per-engineer "
                    "variation and documentation drift."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Automation permanently locks interface descriptions so that "
                    "no engineer can modify them via CLI in the future."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Automation tools audit or configure but do not "
                    "inherently lock CLI access. Access control is a separate "
                    "concern handled by AAA policies."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Automation increases device CPU utilization by 30%, which "
                    "improves routing convergence speed."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Increased CPU utilization is a potential cost of "
                    "automation, not a benefit. Routing convergence is governed by "
                    "protocol timers and topology, not automation CPU load."
                ),
            },
        ],
        "explanation": (
            "Automation benefits go beyond speed: consistency (every device "
            "treated identically), repeatability (same result each run), "
            "auditability (structured logs), and reduced human error. The "
            "elimination of per-engineer variation is a key operational "
            "improvement often overlooked when focusing only on time savings."
        ),
    },
    {
        "id": "cd6v3-002",
        "domain": 6,
        "objective": "6.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Automation impact",
        "stem": (
            "After a network team implements Ansible playbooks to enforce a "
            "standard security baseline on all switches, they discover that a "
            "junior engineer had manually changed a banner message on 12 switches "
            "six months ago. The playbooks corrected all 12 switches back to the "
            "standard within seconds. Which automation concept does this "
            "illustrate?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Orchestration — multiple tools working together to complete "
                    "a complex multi-step workflow."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Orchestration refers to coordinating multiple "
                    "automation systems or workflows. The scenario describes a "
                    "single playbook detecting and correcting drift on individual "
                    "devices."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Configuration drift remediation — automation detects and "
                    "corrects devices that have diverged from the desired state."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Configuration drift occurs when devices deviate from "
                    "the intended baseline (often through manual changes). "
                    "Automation tools like Ansible remediate drift by comparing "
                    "current state to desired state and correcting discrepancies."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Southbound API programming — the controller pushed an "
                    "OpenFlow rule to suppress unauthorized banner changes."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario uses Ansible playbooks, not an SDN "
                    "controller southbound API. Banners are device configuration "
                    "items, not flow table entries."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Zero-touch provisioning — devices automatically download "
                    "their configuration from a DHCP server at boot."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Zero-touch provisioning (ZTP) is an initial "
                    "device bootstrap process. The scenario involves ongoing "
                    "compliance enforcement against existing running devices."
                ),
            },
        ],
        "explanation": (
            "Configuration drift is a major operational problem in large networks: "
            "manual changes accumulate over time, creating inconsistency and "
            "security gaps. Automation tools (Ansible, Puppet, Chef) solve this "
            "by continuously enforcing desired state and automatically correcting "
            "any drift detected — a capability impossible with manual CLI management."
        ),
    },
    # ------------------------------------------------------------------ #
    # 6.2  Traditional vs controller-based
    # ------------------------------------------------------------------ #
    {
        "id": "cd6v3-003",
        "domain": 6,
        "objective": "6.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Traditional vs controller-based",
        "stem": (
            "A network engineer manages 200 access switches using CLI templates "
            "applied via a jump server. A colleague proposes migrating to a "
            "controller-based architecture. The engineer argues that the current "
            "approach is sufficient because devices still converge independently. "
            "Which statement BEST identifies the limitation the engineer is "
            "overlooking?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Traditional CLI management prevents devices from running "
                    "Spanning Tree Protocol, which a controller enables."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. STP runs on devices regardless of management "
                    "approach. CLI management does not disable STP."
                ),
            },
            {
                "id": "b",
                "text": (
                    "CLI template management lacks a real-time network-wide "
                    "visibility and assurance layer — when a change causes a "
                    "problem, pinpointing the affected device requires manual "
                    "investigation across all 200 switches."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Controller-based platforms like Cisco DNA Center "
                    "provide end-to-end network assurance, telemetry correlation, "
                    "and automated root-cause analysis. CLI template management "
                    "provides no real-time assurance plane — issues must be "
                    "manually investigated device by device."
                ),
            },
            {
                "id": "c",
                "text": (
                    "CLI management prevents VLAN creation on access switches "
                    "unless a controller approves each change via RADIUS."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. CLI management allows full device configuration "
                    "including VLANs. RADIUS is an AAA protocol unrelated to VLAN "
                    "provisioning approval."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Traditional networks cannot support IP routing, so a "
                    "controller is required to provide Layer 3 forwarding."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Traditional networks fully support IP routing. "
                    "Layer 3 forwarding is a device capability, not a controller "
                    "dependency."
                ),
            },
        ],
        "explanation": (
            "Beyond consistency and speed, controller-based architectures provide "
            "a network assurance plane: continuous telemetry collection, anomaly "
            "detection, and automated root-cause analysis. Traditional CLI "
            "management provides no equivalent — operators must manually SSH to "
            "each device to investigate issues, a significant operational "
            "limitation at scale."
        ),
    },
    {
        "id": "cd6v3-004",
        "domain": 6,
        "objective": "6.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Traditional vs controller-based",
        "stem": (
            "Which statement CORRECTLY describes how a controller-based network "
            "handles a new network-wide QoS policy compared to a traditional "
            "network?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "In both models the engineer must configure each device "
                    "individually; the controller simply provides a GUI wrapper "
                    "around individual SSH sessions."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A true controller-based network programs devices "
                    "via APIs and abstracts the per-device configuration. It is "
                    "not merely a GUI over SSH sessions."
                ),
            },
            {
                "id": "b",
                "text": (
                    "In a controller-based network the engineer defines the QoS "
                    "intent once in the controller; the controller translates it "
                    "into device-specific commands and deploys them simultaneously "
                    "across all devices via southbound APIs."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Controller-based architectures separate intent from "
                    "implementation. The engineer expresses what they want (e.g., "
                    "prioritize voice traffic) and the controller generates and "
                    "pushes device-specific configurations via NETCONF, REST, or "
                    "OpenFlow to all devices at once."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Traditional networks use SNMP traps to automatically "
                    "propagate QoS policies from the NMS to all devices, matching "
                    "the controller capability."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. SNMP traps are notifications sent from devices to "
                    "the NMS, not configuration push mechanisms. SNMP SET can "
                    "configure devices but lacks the policy abstraction and "
                    "orchestration of a controller."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Controller-based networks require the engineer to write "
                    "OpenFlow rules manually for each QoS class and device, "
                    "which is more complex than CLI."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A key goal of controller-based networking is "
                    "abstraction — the operator works at the policy/intent level, "
                    "not at the level of individual flow rules."
                ),
            },
        ],
        "explanation": (
            "The controller-based model separates intent (what you want) from "
            "mechanism (how to configure each device). In traditional networking, "
            "every device requires individual configuration. Controllers absorb "
            "the translation complexity, deploy changes uniformly, and maintain "
            "consistency — making large-scale policy changes practical."
        ),
    },
    # ------------------------------------------------------------------ #
    # 6.3  SDN architecture
    # ------------------------------------------------------------------ #
    {
        "id": "cd6v3-005",
        "domain": 6,
        "objective": "6.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SDN architecture (control/data plane)",
        "stem": (
            "In a pure SDN environment, a network device receives a packet for "
            "destination 10.1.1.1 but has no matching flow entry in its flow "
            "table. Which sequence of events occurs?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The device runs its local OSPF process, calculates a path, "
                    "installs a route, and forwards the packet without contacting "
                    "the controller."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. In pure SDN the control plane (including routing "
                    "decisions) is centralized in the controller. The device does "
                    "not run an independent OSPF process."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The device sends a packet-in message to the SDN controller, "
                    "the controller computes the forwarding action, and installs "
                    "a flow entry on the device via a packet-out or flow-mod "
                    "message."
                ),
                "correct": True,
                "rationale": (
                    "Correct. In OpenFlow-based SDN, when a device has no "
                    "matching flow entry (a 'table miss'), it sends a packet-in "
                    "message to the controller. The controller decides the action "
                    "and replies with a flow-mod to install a new entry and/or a "
                    "packet-out to forward this specific packet."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The device drops the packet and logs an ICMP unreachable "
                    "message to the source, because flow tables cannot be updated "
                    "at runtime."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. SDN flow tables are updated dynamically by the "
                    "controller. A table miss triggers controller consultation, "
                    "not a permanent drop."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The device floods the packet out all ports to ensure delivery, "
                    "similar to how a Layer 2 switch handles an unknown unicast."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. While flooding is a possible controller-instructed "
                    "action for specific cases, the standard SDN response to a "
                    "table miss is to consult the controller, not to flood all "
                    "Layer 3 packets."
                ),
            },
        ],
        "explanation": (
            "In OpenFlow SDN, a table miss (no matching flow entry) triggers a "
            "packet-in message to the controller. The controller then installs "
            "a flow-mod entry on the device for future packets matching that "
            "flow, and sends a packet-out to handle the current packet. This "
            "reactive flow installation is fundamental to how SDN data-plane "
            "devices interact with the centralized control plane."
        ),
    },
    {
        "id": "cd6v3-006",
        "domain": 6,
        "objective": "6.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SDN architecture (overlay/underlay/fabric)",
        "stem": (
            "In a Cisco SD-Access deployment, which component serves as the "
            "CONTROL PLANE for the overlay, mapping endpoint identifiers (EIDs) "
            "to routing locators (RLOCs) so that fabric edge nodes know where "
            "to tunnel traffic?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "VXLAN — it encapsulates endpoint traffic and provides "
                    "the mapping database."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. VXLAN is the data-plane encapsulation protocol "
                    "used to tunnel traffic across the underlay. It does not "
                    "provide the EID-to-RLOC mapping function."
                ),
            },
            {
                "id": "b",
                "text": (
                    "LISP (Locator/ID Separation Protocol) — it maintains the "
                    "map server/map resolver database that maps endpoint addresses "
                    "to fabric node RLOCs."
                ),
                "correct": True,
                "rationale": (
                    "Correct. In SD-Access, LISP serves as the overlay control "
                    "plane. LISP separates endpoint identity (EID, e.g., host IP) "
                    "from location (RLOC, fabric edge node IP). The map server "
                    "and map resolver hold the EID-to-RLOC mappings that edge "
                    "nodes query to determine where to send VXLAN-encapsulated "
                    "traffic."
                ),
            },
            {
                "id": "c",
                "text": (
                    "IS-IS — it runs on all fabric nodes and calculates "
                    "underlay paths between edge nodes."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. IS-IS (or OSPF) provides the underlay routing — "
                    "IP reachability between fabric nodes. It is not the overlay "
                    "control plane responsible for EID-to-RLOC mapping."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Cisco DNA Center — it forwards every packet in real time "
                    "by looking up endpoint locations in its dashboard."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. DNA Center is the management and orchestration "
                    "plane, not the per-packet forwarding or mapping lookup plane. "
                    "It configures the fabric but does not participate in "
                    "real-time packet forwarding decisions."
                ),
            },
        ],
        "explanation": (
            "SD-Access overlay control plane: LISP provides EID-to-RLOC mapping. "
            "Overlay data plane: VXLAN encapsulates traffic between fabric nodes. "
            "Underlay: IP routing (IS-IS) provides reachability between RLOCs. "
            "DNA Center orchestrates the entire fabric but is not in the packet "
            "forwarding path."
        ),
    },
    {
        "id": "cd6v3-007",
        "domain": 6,
        "objective": "6.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Northbound/southbound APIs",
        "stem": (
            "A Cisco DNA Center installation uses NETCONF over SSH to push "
            "interface configurations to IOS-XE switches, while a custom "
            "operations dashboard calls DNA Center's REST API to display "
            "network health metrics. Which statement CORRECTLY maps these "
            "communications to their SDN interface types?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Both are northbound interfaces because they both use "
                    "HTTP-based transport."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. NETCONF uses SSH (not HTTP), and the interface "
                    "type is determined by the position in the SDN stack, not "
                    "the transport protocol. NETCONF to switches is a southbound "
                    "interface."
                ),
            },
            {
                "id": "b",
                "text": (
                    "NETCONF to switches = southbound interface; REST API to "
                    "DNA Center from the dashboard = northbound interface."
                ),
                "correct": True,
                "rationale": (
                    "Correct. In SDN architecture, southbound interfaces go from "
                    "the controller down to network devices (NETCONF/YANG to "
                    "IOS-XE switches). Northbound interfaces go from the "
                    "controller up to applications (the operations dashboard "
                    "calling DNA Center's REST API)."
                ),
            },
            {
                "id": "c",
                "text": (
                    "NETCONF to switches = northbound interface; REST API "
                    "from dashboard = southbound interface."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The directions are reversed. 'North' points toward "
                    "applications/orchestrators above the controller; 'south' "
                    "points toward network devices below the controller."
                ),
            },
            {
                "id": "d",
                "text": (
                    "NETCONF to switches = eastbound interface; REST API from "
                    "dashboard = westbound interface."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. East/westbound interfaces describe communication "
                    "between peer SDN controllers (horizontal). NETCONF to devices "
                    "and REST to applications are vertical interfaces (south and "
                    "north, respectively)."
                ),
            },
        ],
        "explanation": (
            "SDN interface classification: NBI (northbound) — controller to "
            "applications/orchestrators, typically REST/gRPC. SBI (southbound) "
            "— controller to network devices, using NETCONF, RESTCONF, OpenFlow, "
            "or CLI. East/westbound — between peer controllers. The axis is "
            "vertical (above/below controller) for NBI/SBI and horizontal for "
            "east/west."
        ),
    },
    {
        "id": "cd6v3-008",
        "domain": 6,
        "objective": "6.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SDN architecture (control/data plane)",
        "stem": (
            "A network engineer states: 'In our SD-WAN deployment, the vSmart "
            "controller distributes OMP routes and policies to all vEdge routers, "
            "but the actual encrypted tunnels carry user traffic between vEdge "
            "devices directly.' Which two SDN planes does this statement describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Management plane (vSmart distributing policies) and "
                    "data plane (vEdge tunnels)."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The vSmart controller distributing routing "
                    "information and policies is the CONTROL plane function, "
                    "not the management plane. The management plane handles "
                    "device configuration and monitoring (vManage in SD-WAN)."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Control plane (vSmart distributing OMP routes/policies) "
                    "and data plane (vEdge-to-vEdge tunnels carrying user traffic)."
                ),
                "correct": True,
                "rationale": (
                    "Correct. In Cisco SD-WAN: the control plane is the vSmart "
                    "controller distributing OMP (Overlay Management Protocol) "
                    "routes, policies, and keys. The data plane is the encrypted "
                    "IPsec/GRE tunnels between vEdge routers that carry actual "
                    "user traffic — the controller is not in the data path."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Data plane (vSmart forwarding packets) and control plane "
                    "(vEdge tunnels computing routing)."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. vSmart does not forward user data packets — it "
                    "is the control plane. vEdge tunnels carry user traffic — "
                    "they ARE the data plane. The roles are reversed in this "
                    "option."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Overlay (vSmart) and underlay (vEdge tunnels)."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Overlay/underlay terminology describes the "
                    "virtual vs. physical network layers, not the control/data "
                    "plane function separation described in the scenario."
                ),
            },
        ],
        "explanation": (
            "Cisco SD-WAN planes: Control plane = vSmart (OMP route/policy "
            "distribution). Data plane = vEdge-to-vEdge IPsec tunnels. "
            "Management plane = vManage (configuration, monitoring). "
            "Orchestration plane = vBond (onboarding). The controller is "
            "explicitly out of the data path — vEdges forward traffic directly "
            "to each other."
        ),
    },
    # ------------------------------------------------------------------ #
    # 6.4  Cisco DNA Center
    # ------------------------------------------------------------------ #
    {
        "id": "cd6v3-009",
        "domain": 6,
        "objective": "6.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Cisco DNA Center",
        "stem": (
            "An engineer uses Cisco DNA Center to onboard a new Catalyst 9300 "
            "switch into an existing SD-Access fabric. During onboarding, DNA "
            "Center automatically pushes the underlay IP addressing, IS-IS "
            "configuration, LISP, and VXLAN settings to the switch. What DNA "
            "Center function is being performed?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Network assurance — DNA Center is verifying that the switch "
                    "meets the health threshold."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Network assurance is the monitoring and "
                    "troubleshooting function. Pushing fabric configuration "
                    "to a new device is provisioning, not assurance."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Device provisioning (Day-N provisioning) — DNA Center is "
                    "configuring the device to join the existing fabric by "
                    "pushing all required underlay and overlay configuration."
                ),
                "correct": True,
                "rationale": (
                    "Correct. DNA Center's provisioning workflow (Day-0/Day-N) "
                    "automates the configuration of devices into the SD-Access "
                    "fabric. It generates and deploys device-specific IS-IS, "
                    "LISP, and VXLAN configurations based on the fabric design, "
                    "removing the need for manual per-device CLI."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Northbound API call — DNA Center is receiving instructions "
                    "from an external orchestration system to configure the switch."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A northbound API call is how an external system "
                    "talks to DNA Center. The scenario describes DNA Center "
                    "pushing config to a network device via its southbound "
                    "interface — that is provisioning."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Telemetry streaming — DNA Center is collecting streaming "
                    "state data from the switch to build a network topology map."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Telemetry streaming collects operational data "
                    "from running devices. The scenario describes configuration "
                    "being pushed to a device during fabric onboarding."
                ),
            },
        ],
        "explanation": (
            "DNA Center automates the entire device lifecycle: PnP (Day-0 "
            "zero-touch provisioning), fabric provisioning (Day-1 adding device "
            "to SD-Access), and Day-N ongoing policy changes. When onboarding "
            "a switch into SD-Access, DNA Center pushes all required underlay "
            "(IS-IS, IP addressing) and overlay (LISP, VXLAN) configuration "
            "automatically via NETCONF/YANG southbound."
        ),
    },
    {
        "id": "cd6v3-010",
        "domain": 6,
        "objective": "6.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Cisco DNA Center",
        "stem": (
            "A network operations team wants to integrate their IT service "
            "management (ITSM) ticketing system with Cisco DNA Center so that "
            "approved change tickets automatically trigger network provisioning "
            "workflows. Which DNA Center capability enables this integration?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "DNA Center's southbound NETCONF interface, which allows "
                    "the ITSM system to push YANG data models directly to "
                    "network devices."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The southbound interface connects DNA Center to "
                    "network devices, not to external IT systems. The ITSM system "
                    "is an application above DNA Center, which requires a "
                    "northbound interface."
                ),
            },
            {
                "id": "b",
                "text": (
                    "DNA Center's northbound REST API, which allows external "
                    "systems like ITSM platforms to trigger provisioning workflows "
                    "programmatically."
                ),
                "correct": True,
                "rationale": (
                    "Correct. DNA Center exposes a documented REST API (northbound "
                    "interface) that external systems — including ITSM, IPAM, "
                    "or custom scripts — can call to trigger network workflows, "
                    "retrieve inventory, or push policy changes. This API-driven "
                    "integration is a key enterprise use case for DNA Center."
                ),
            },
            {
                "id": "c",
                "text": (
                    "DNA Center's SNMP trap receiver, which accepts structured "
                    "change notifications from the ITSM system."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. SNMP traps are sent FROM network devices TO "
                    "management systems to notify of events. DNA Center does not "
                    "use SNMP traps as an integration mechanism for external "
                    "IT systems to trigger workflows."
                ),
            },
            {
                "id": "d",
                "text": (
                    "DNA Center's CLI template engine, where ITSM tickets are "
                    "converted to Jinja2 templates and manually uploaded by "
                    "an engineer."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. CLI templates exist in DNA Center but require "
                    "manual engineer involvement. The question asks for automated "
                    "integration — which requires the programmatic northbound "
                    "REST API, not a manual template upload process."
                ),
            },
        ],
        "explanation": (
            "DNA Center's northbound REST API is its integration point for "
            "external systems. Organizations connect ITSM (ServiceNow, Jira), "
            "IPAM (Infoblox), or custom dashboards to DNA Center's REST API "
            "to automate end-to-end workflows: ticket approved → API call → "
            "DNA Center provisions network. This is called closed-loop "
            "automation and is a key differentiator of controller-based "
            "architectures."
        ),
    },
    # ------------------------------------------------------------------ #
    # 6.5  REST APIs
    # ------------------------------------------------------------------ #
    {
        "id": "cd6v3-011",
        "domain": 6,
        "objective": "6.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "REST APIs (HTTP verbs/CRUD)",
        "stem": (
            "A script currently retrieves a firewall ACL object using:\n\n"
            "    GET /api/v2/acl/101\n\n"
            "The team now wants to completely replace ACL 101's content with a "
            "new rule set (all existing rules discarded, new rules applied). "
            "Which HTTP method and URI should the script use?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "POST /api/v2/acl/101 with the new rule set in the body."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. POST creates a new resource. Sending POST to an "
                    "existing resource URI may create a subordinate resource or "
                    "return an error; it is not the standard method for full "
                    "replacement of an existing resource."
                ),
            },
            {
                "id": "b",
                "text": (
                    "PUT /api/v2/acl/101 with the complete new rule set in "
                    "the body."
                ),
                "correct": True,
                "rationale": (
                    "Correct. PUT replaces the entire resource at the specified "
                    "URI with the body of the request. It is idempotent: sending "
                    "the same PUT multiple times leaves the resource in the same "
                    "final state. This is the correct method for a full resource "
                    "replacement."
                ),
            },
            {
                "id": "c",
                "text": (
                    "PATCH /api/v2/acl/101 with only the new rules that differ "
                    "from the existing ACL."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. PATCH applies a partial update, merging changes "
                    "with the existing resource. It would not discard existing "
                    "rules — only modify specified ones. Full replacement requires "
                    "PUT."
                ),
            },
            {
                "id": "d",
                "text": (
                    "DELETE /api/v2/acl/101 followed by POST /api/v2/acl with "
                    "the new rules."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. DELETE + POST achieves the functional goal but is "
                    "non-atomic — another system could access the resource between "
                    "the DELETE and POST. PUT atomically replaces the resource and "
                    "is the correct single-operation approach."
                ),
            },
        ],
        "explanation": (
            "REST CRUD mapping: PUT = full resource replacement (idempotent). "
            "PATCH = partial update. POST = create new resource. For 'discard "
            "everything and replace with this new content,' PUT at the resource "
            "URI is correct. The client must send the complete desired "
            "representation in the PUT body."
        ),
    },
    {
        "id": "cd6v3-012",
        "domain": 6,
        "objective": "6.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "REST APIs (HTTP verbs/CRUD)",
        "stem": (
            "A network automation script sends a DELETE request to remove a "
            "static route object from a controller:\n\n"
            "    DELETE /api/v1/routes/static/192.168.10.0_24\n\n"
            "The server responds with HTTP 404. What does this response indicate?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The route was successfully deleted and no longer exists on "
                    "the controller."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. HTTP 204 No Content or 200 OK indicates successful "
                    "deletion. HTTP 404 means the resource was not found — it "
                    "cannot be deleted because it does not exist at that URI."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The static route resource 192.168.10.0/24 does not exist "
                    "on the controller, so there is nothing to delete."
                ),
                "correct": True,
                "rationale": (
                    "Correct. HTTP 404 Not Found means the server could not "
                    "locate a resource at the specified URI. Either the route "
                    "never existed, was already deleted, or the URI is incorrect. "
                    "No deletion occurred."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The client is not authorized to delete routes; the "
                    "administrator must grant DELETE permissions."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Authorization failures return HTTP 403 Forbidden "
                    "(authenticated but not allowed) or 401 Unauthorized "
                    "(not authenticated). HTTP 404 means the resource was not "
                    "found, not that the operation was denied."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The controller experienced an internal error while "
                    "processing the delete operation."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Internal server errors return HTTP 500. HTTP 404 "
                    "is a client-side error — the resource was not found, not a "
                    "server processing failure."
                ),
            },
        ],
        "explanation": (
            "HTTP 404 Not Found: the resource URI does not match any existing "
            "resource on the server. For a DELETE, this means there is nothing "
            "to delete at that location. Successful deletion returns 200 OK "
            "(with response body) or 204 No Content (no body). Know the full "
            "status code set: 200, 201, 204, 400, 401, 403, 404, 500."
        ),
    },
    {
        "id": "cd6v3-013",
        "domain": 6,
        "objective": "6.5",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "REST APIs (HTTP verbs/CRUD)",
        "stem": (
            "A developer is writing a Python script to interact with a network "
            "controller REST API. The script must authenticate and then retrieve "
            "device inventory. Examine the following pseudocode:\n\n"
            "    Step 1: POST /api/auth/token  (body: username/password)\n"
            "            → response: {\"token\": \"eyJhbGc...\"}\n\n"
            "    Step 2: GET /api/v1/devices\n"
            "            Headers: {\"Authorization\": \"Bearer eyJhbGc...\"}\n\n"
            "Which statement BEST explains why Step 1 is required before Step 2?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "REST APIs are stateful, so the server stores the session "
                    "after Step 1 and automatically authenticates Step 2 without "
                    "requiring the token header."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. REST is stateless — the server stores no session "
                    "between requests. That is precisely WHY the token must be "
                    "included in every subsequent request."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Because REST is stateless, the server stores no session "
                    "context between requests. The token obtained in Step 1 must "
                    "be included in every subsequent request so the server can "
                    "authenticate each call independently."
                ),
                "correct": True,
                "rationale": (
                    "Correct. REST statelessness means each request is "
                    "self-contained. Step 1 exchanges credentials for a token. "
                    "Step 2 (and all future requests) must carry that token in "
                    "the Authorization header because the server holds no memory "
                    "of the Step 1 authentication."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Step 1 is needed only once per TCP connection; once the "
                    "connection is established, subsequent GET requests on the "
                    "same TCP session are automatically trusted."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. TCP connection persistence (HTTP keep-alive) is "
                    "a transport-layer optimization unrelated to authentication. "
                    "Each HTTP request must independently carry authentication "
                    "credentials regardless of TCP connection state."
                ),
            },
            {
                "id": "d",
                "text": (
                    "POST is always required before GET in REST APIs because "
                    "servers reject GET requests that are not preceded by a "
                    "POST to the same base URL."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. There is no REST rule requiring POST before GET. "
                    "The reason for Step 1 is specific to token-based "
                    "authentication, not a general HTTP sequencing requirement."
                ),
            },
        ],
        "explanation": (
            "REST statelessness is fundamental: no server-side session state is "
            "maintained between requests. Token-based authentication (JWT/Bearer) "
            "is the stateless solution — the client obtains a token via POST, "
            "then includes it in every subsequent request. The server validates "
            "the token on each request independently, with no dependency on "
            "prior interactions."
        ),
    },
    {
        "id": "cd6v3-014",
        "domain": 6,
        "objective": "6.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "REST APIs (statelessness/data encoding)",
        "stem": (
            "A REST API endpoint returns the following response header:\n\n"
            "    Content-Type: application/json\n\n"
            "A second endpoint returns:\n\n"
            "    Content-Type: application/xml\n\n"
            "A client script needs to process both responses. Which statement "
            "is TRUE about how REST APIs handle data encoding?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "REST APIs are required by specification to use only JSON; "
                    "XML responses indicate a non-RESTful implementation."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The REST architectural style does not mandate "
                    "any specific data format. REST APIs commonly support JSON, "
                    "XML, plain text, or other formats. The format is negotiated "
                    "via Accept/Content-Type headers."
                ),
            },
            {
                "id": "b",
                "text": (
                    "REST APIs can use multiple data formats; the Content-Type "
                    "header indicates the format of the response body, and the "
                    "client uses the Accept header in its request to specify "
                    "preferred formats."
                ),
                "correct": True,
                "rationale": (
                    "Correct. REST is format-agnostic. Clients signal preferred "
                    "formats via the Accept request header "
                    "(e.g., Accept: application/json). Servers indicate the "
                    "actual response format via Content-Type. Many APIs support "
                    "both JSON and XML content negotiation."
                ),
            },
            {
                "id": "c",
                "text": (
                    "XML is the required encoding for southbound API protocols "
                    "and JSON is required for northbound APIs; mixing them "
                    "violates REST constraints."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. While NETCONF traditionally uses XML encoding, "
                    "this is not a REST constraint. RESTCONF (a REST-based "
                    "southbound protocol) supports both JSON and XML. There is "
                    "no REST rule linking north/south direction to encoding format."
                ),
            },
            {
                "id": "d",
                "text": (
                    "A script can only process one Content-Type per session; it "
                    "must reconnect to switch between JSON and XML endpoints."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A script can process different Content-Types in "
                    "different requests within the same session. The client simply "
                    "parses each response according to the Content-Type header "
                    "returned by that specific response."
                ),
            },
        ],
        "explanation": (
            "REST is format-agnostic: JSON is dominant in modern APIs, but XML, "
            "YAML, and plain text are all valid. Content negotiation uses two "
            "headers: Accept (client preference in request) and Content-Type "
            "(actual format in response). NETCONF uses XML; RESTCONF supports "
            "both JSON and XML. CCNA candidates should know that JSON is the "
            "most common REST encoding but not the only one."
        ),
    },
    {
        "id": "cd6v3-015",
        "domain": 6,
        "objective": "6.5",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "REST APIs (HTTP verbs/CRUD)",
        "stem": (
            "A REST API call returns HTTP 403 Forbidden. A colleague suggests "
            "the fix is to re-authenticate and get a new token. The engineer "
            "disagrees. Who is correct, and why?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The colleague is correct — 403 and 401 both indicate "
                    "authentication problems, so re-authenticating will resolve "
                    "both."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. HTTP 401 and 403 are distinct: 401 = authentication "
                    "failure (fix: re-authenticate). 403 = authorization failure "
                    "(the client IS authenticated but lacks permission). "
                    "Re-authenticating with the same credentials will still return "
                    "403 because the problem is role/permission, not identity."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The engineer is correct — 403 means the client is "
                    "authenticated but does not have permission for that resource; "
                    "re-authentication with the same credentials will not fix it, "
                    "as the account needs elevated privileges."
                ),
                "correct": True,
                "rationale": (
                    "Correct. HTTP 403 Forbidden: the server understood the "
                    "request and identified the client (authentication succeeded) "
                    "but the client's account lacks authorization for that "
                    "resource or action. Resolution requires granting the account "
                    "the needed role/permission, not re-authentication."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Neither is correct — 403 indicates a malformed request "
                    "body, so the fix is to correct the JSON syntax."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Malformed request bodies return HTTP 400 Bad "
                    "Request. HTTP 403 Forbidden is an authorization error, "
                    "not a syntax error."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Neither is correct — 403 means the server is unavailable "
                    "due to maintenance; the client should retry after a delay."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Server unavailability returns HTTP 503 Service "
                    "Unavailable or 504 Gateway Timeout. HTTP 403 is a "
                    "client-side authorization error."
                ),
            },
        ],
        "explanation": (
            "Critical distinction: HTTP 401 Unauthorized = authentication failure "
            "(no or invalid credentials) → fix by re-authenticating. "
            "HTTP 403 Forbidden = authorization failure (valid credentials but "
            "insufficient permissions) → fix by granting appropriate role/scope. "
            "Re-authenticating with the same credentials will still return 403 "
            "if the account lacks the required permission."
        ),
    },
    # ------------------------------------------------------------------ #
    # 6.6  Configuration management
    # ------------------------------------------------------------------ #
    {
        "id": "cd6v3-016",
        "domain": 6,
        "objective": "6.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Configuration management (Ansible/Puppet/Chef)",
        "stem": (
            "An Ansible playbook task is written to configure 'ntp server "
            "192.0.2.1' on a Cisco IOS router. The task runs successfully. "
            "An engineer runs the same playbook again two days later without "
            "any changes. Which outcome is expected, and which Ansible property "
            "explains it?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Ansible adds a second 'ntp server 192.0.2.1' entry because "
                    "it always appends configuration lines without checking "
                    "existing state."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Ansible's IOS modules check current device state "
                    "before making changes. If the desired configuration is already "
                    "present, the task reports 'ok' and makes no changes — "
                    "this is idempotency."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Ansible reports 'ok' (no change) for the NTP task because "
                    "the desired state is already present — demonstrating "
                    "idempotency."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Ansible tasks are designed to be idempotent: before "
                    "applying a configuration, the module checks if the device "
                    "already has the desired state. If 'ntp server 192.0.2.1' is "
                    "already configured, the task reports 'ok' and skips the "
                    "change, ensuring no duplicates or disruption."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Ansible removes the existing NTP configuration and "
                    "re-applies it to ensure the configuration is current."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Ansible does not remove and re-apply existing "
                    "correct configuration. It checks state and only makes changes "
                    "when the current state differs from the desired state."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Ansible fails with an error because it detects a duplicate "
                    "configuration attempt on the device."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Ansible does not fail on re-runs when the desired "
                    "state is already present. It gracefully reports 'ok' and "
                    "moves on — this is the idempotent behavior."
                ),
            },
        ],
        "explanation": (
            "Idempotency is a key Ansible property: running the same playbook "
            "multiple times produces the same result as running it once. Ansible "
            "IOS/network modules compare desired state to current state before "
            "making changes. If the device already has the correct config, the "
            "task reports 'ok' (unchanged). Only tasks that need to change "
            "something report 'changed'."
        ),
    },
    {
        "id": "cd6v3-017",
        "domain": 6,
        "objective": "6.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Configuration management (Ansible/Puppet/Chef)",
        "stem": (
            "A network team is evaluating Puppet for managing 500 network "
            "devices. The security team requires that management traffic be "
            "encrypted and that devices use certificates for mutual "
            "authentication with the management server. Which Puppet "
            "characteristic satisfies the security team's requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Puppet uses plain-text SSH like Ansible, so no additional "
                    "security configuration is needed."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Puppet does not primarily use SSH. Puppet agent "
                    "communicates with the Puppet master over TLS (formerly SSL) "
                    "using certificates. Ansible uses SSH."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Puppet agent-to-master communication uses TLS with "
                    "certificate-based mutual authentication — the Puppet CA "
                    "signs certificates for both the master and each agent, "
                    "satisfying encryption and mutual auth requirements."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Puppet uses a built-in Certificate Authority (CA). "
                    "Each Puppet agent presents a signed certificate to the Puppet "
                    "master, and the master's certificate is verified by the agent. "
                    "All communication is TLS-encrypted. This mutual certificate "
                    "authentication is a key Puppet security feature."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Puppet encrypts traffic using SNMPv3 authPriv mode, which "
                    "provides both authentication and encryption."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Puppet does not use SNMP. Puppet agent-master "
                    "communication uses TLS over TCP port 8140, not SNMP."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Puppet uses the NETCONF protocol over SSH port 830 for all "
                    "agent-to-master communication."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. NETCONF over SSH (port 830) is used between "
                    "an SDN controller/automation tool and network devices — not "
                    "for Puppet agent-to-master communication, which uses its "
                    "own TLS-based protocol on port 8140."
                ),
            },
        ],
        "explanation": (
            "Puppet security model: TLS with mutual certificate authentication "
            "on TCP port 8140. The Puppet CA issues signed certs to all agents; "
            "agents and master mutually verify each other's certificates on each "
            "connection. Chef similarly uses TLS. Ansible uses SSH for encryption "
            "and key-based or password authentication — no internal CA required."
        ),
    },
    {
        "id": "cd6v3-018",
        "domain": 6,
        "objective": "6.6",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Configuration management (Ansible/Puppet/Chef)",
        "stem": (
            "A Chef administrator writes a recipe that ensures a specific "
            "user account exists on all managed Linux servers. The recipe is "
            "uploaded to the Chef server. Which component is responsible for "
            "actually EXECUTING the recipe and enforcing the desired state on "
            "each server?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The Chef workstation, which connects to each server via "
                    "SSH and runs the recipe remotely."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The Chef workstation is used by administrators "
                    "to write and upload cookbooks to the Chef server. It does "
                    "not connect to managed nodes to run recipes. The chef-client "
                    "(agent) on each node does that."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The chef-client (agent) installed on each managed node, "
                    "which periodically pulls the run-list from the Chef server "
                    "and enforces the desired state locally."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Chef uses a pull model: the chef-client agent on "
                    "each managed node periodically checks in with the Chef server, "
                    "downloads its assigned run-list (cookbooks/recipes), compiles "
                    "a resource collection, and converges the node to the desired "
                    "state. The execution is local on the node."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The Chef server, which pushes the recipe via SSH to each "
                    "managed node and executes it remotely."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The Chef server stores cookbooks and node "
                    "metadata but does not push or execute recipes. It is the "
                    "chef-client on each node that pulls from the server and "
                    "runs the recipe locally."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The Knife tool, which is executed from the workstation and "
                    "directly applies the recipe to all nodes simultaneously."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Knife is a command-line tool for interacting with "
                    "the Chef server (uploading cookbooks, managing nodes, etc.), "
                    "not for executing recipes on nodes. The chef-client agent "
                    "handles execution."
                ),
            },
        ],
        "explanation": (
            "Chef architecture: Workstation (admin creates cookbooks) → "
            "Chef Server (stores cookbooks, node data) → "
            "chef-client agent on each node (pulls run-list from server, "
            "converges node). The pull model means the chef-client runs on a "
            "schedule (default every 30 min), downloads its run-list, and "
            "enforces desired state locally. Compare to Ansible: no agent, "
            "control node pushes via SSH."
        ),
    },
    {
        "id": "cd6v3-019",
        "domain": 6,
        "objective": "6.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Configuration management (Ansible/Puppet/Chef)",
        "stem": (
            "An engineer wants to use Ansible to configure a Cisco IOS-XE router "
            "without installing any software on the router. The router is "
            "reachable on the network. What does the engineer need to configure "
            "on the router to allow Ansible to connect?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Install the Ansible agent package on the router's flash "
                    "memory and enable it with 'service ansible-agent'."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Ansible is agentless — no software is installed "
                    "on managed devices. This is Ansible's defining characteristic "
                    "for network device management."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Enable SSH on the router (ip ssh version 2), create a "
                    "local user with privilege 15, and ensure the router is "
                    "reachable from the Ansible control node."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Ansible connects to Cisco IOS-XE devices over SSH "
                    "without requiring an agent. The router needs SSHv2 enabled, "
                    "a reachable management IP, and valid credentials. Ansible "
                    "then uses the ios_* or cisco.ios collection modules to "
                    "send CLI commands over the SSH connection."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Enable NETCONF on the router and install pynetconf on "
                    "the router's embedded Python interpreter."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. NETCONF can be used by some Ansible modules "
                    "(netconf_* modules), but the core requirement for most Cisco "
                    "IOS Ansible tasks is SSH. Additionally, 'pynetconf' is "
                    "installed on the Ansible control node, not on the router."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Configure SNMP read-write community strings on the router "
                    "so Ansible can push configuration via SNMP SET operations."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Ansible does not use SNMP for Cisco IOS "
                    "configuration. SNMP SET is limited and insecure. Ansible "
                    "uses SSH-based connections for IOS device management."
                ),
            },
        ],
        "explanation": (
            "Ansible network automation for Cisco IOS: agentless, uses SSH. "
            "Router requirements: SSHv2 enabled, management IP reachable, valid "
            "credentials configured. Ansible control node runs playbooks using "
            "cisco.ios collection modules that log in via SSH, send CLI commands, "
            "and parse output — all without any agent on the router. Compare "
            "to Puppet/Chef which require agent software on managed hosts."
        ),
    },
    {
        "id": "cd6v3-020",
        "domain": 6,
        "objective": "6.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Configuration management (Ansible/Puppet/Chef)",
        "stem": (
            "Which configuration management tool uses a domain-specific "
            "declarative language (DSL) called the Puppet language (formerly "
            "Puppet DSL) to describe the desired state of managed resources, "
            "rather than YAML playbooks or Ruby-based recipes?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Ansible",
                "correct": False,
                "rationale": (
                    "Incorrect. Ansible uses YAML-formatted playbooks, not the "
                    "Puppet DSL. Ansible's human-readable YAML syntax is one of "
                    "its design goals."
                ),
            },
            {
                "id": "b",
                "text": "Chef",
                "correct": False,
                "rationale": (
                    "Incorrect. Chef uses Ruby-based DSL in 'recipes' and "
                    "'cookbooks'. Chef configuration is written as Ruby code, "
                    "not the Puppet language DSL."
                ),
            },
            {
                "id": "c",
                "text": "Puppet",
                "correct": True,
                "rationale": (
                    "Correct. Puppet uses its own declarative DSL (the Puppet "
                    "language) in 'manifests' (.pp files) to describe desired "
                    "resource states. For example: package { 'ntp': ensure => "
                    "installed }. This DSL is distinct from YAML (Ansible) and "
                    "Ruby (Chef)."
                ),
            },
            {
                "id": "d",
                "text": "Terraform",
                "correct": False,
                "rationale": (
                    "Incorrect. Terraform uses HCL (HashiCorp Configuration "
                    "Language), not the Puppet DSL. Terraform is also an "
                    "infrastructure-as-code tool focused on provisioning, not "
                    "a configuration management tool in the Puppet/Chef/Ansible "
                    "sense."
                ),
            },
        ],
        "explanation": (
            "Configuration management tool language summary: "
            "Ansible = YAML playbooks. "
            "Puppet = Puppet DSL (declarative, .pp manifest files). "
            "Chef = Ruby DSL (recipes in cookbooks). "
            "Knowing which tool uses which language and file format is a "
            "standard CCNA automation exam topic."
        ),
    },
]

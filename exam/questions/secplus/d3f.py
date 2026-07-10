"""CompTIA Security+ (SY0-701) practice question bank — Domain 3, file F.

26 scenario-driven questions (23 multiple_choice + 3 multiple_response)
covering study_topic labels listed under domain 3 in ``_topic_labels.json``.
"""

from __future__ import annotations

QUESTIONS = [
    # ------------------------------------------------------------------ #
    # Architecture trade-offs (3.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3f-001",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Architecture trade-offs",
        "stem": (
            "A video-streaming startup is choosing an architecture for its "
            "user-authentication service. Option A is active-active across two "
            "geographically separate data centers, which doubles infrastructure "
            "spend but keeps the service available even if an entire data "
            "center fails. Option B is a single primary data center with a cold "
            "standby, which costs far less but requires manual failover and "
            "roughly 45 minutes of downtime. The CFO has capped the "
            "infrastructure budget increase at 15%, an amount Option A would "
            "exceed. Which statement BEST reflects the trade-off the company "
            "must accept?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Choosing the cold-standby design trades a lower, "
                    "budget-compliant infrastructure cost for reduced "
                    "availability, since a data-center failure will produce an "
                    "extended outage while failover is performed manually"
                ),
                "correct": True,
                "rationale": (
                    "Correct. This accurately states the trade-off: staying "
                    "within the 15% budget cap means accepting the cold "
                    "standby's ~45-minute manual-failover downtime instead of "
                    "active-active's near-continuous availability."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The active-active design should be chosen because it "
                    "both meets the 15% budget cap and eliminates downtime "
                    "entirely"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Active-active doubles infrastructure spend, "
                    "which explicitly exceeds the 15% cap — it cannot satisfy "
                    "both the budget constraint and the availability goal "
                    "simultaneously."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Cold standby eliminates single points of failure just as "
                    "effectively as active-active, making the two designs "
                    "functionally equivalent for availability purposes"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A cold standby still requires manual "
                    "intervention and a lengthy failover window, meaning the "
                    "primary site remains a real single point of failure until "
                    "someone acts — the two designs are not equivalent."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Active-active architectures cannot span multiple "
                    "geographic regions, so Option A is not technically "
                    "feasible as described"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Active-active deployments across geographically "
                    "separate sites are a standard, well-established pattern; "
                    "the limiting factor here is budget, not technical "
                    "feasibility."
                ),
            },
        ],
        "explanation": (
            "Architecture trade-off questions hinge on identifying which "
            "resource is being exchanged for which benefit. Here, the binding "
            "budget constraint forces a trade of availability (fast, automatic "
            "failover) for cost, which only the cold-standby design satisfies."
        ),
    },
    # ------------------------------------------------------------------ #
    # Cloud architecture (3.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3f-002",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Cloud architecture",
        "stem": (
            "A smart-manufacturing facility's robotic assembly line must make "
            "collision-avoidance decisions within 10 milliseconds — far faster "
            "than a round trip to the company's cloud region would allow — "
            "while aggregated production metrics can tolerate being sent to the "
            "cloud for long-term analytics with no strict latency requirement. "
            "Which architecture BEST addresses the latency-sensitive "
            "decision-making while still leveraging the cloud for analytics?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Edge/fog computing, deploying local compute nodes on or "
                    "near the factory floor for time-critical decisions, while "
                    "forwarding only aggregated, less time-sensitive data to "
                    "the cloud"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Edge/fog computing places processing physically "
                    "close to the data source to meet sub-millisecond-scale "
                    "latency requirements, while still using the cloud for "
                    "workloads that can tolerate network round-trip delay."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Migrate all processing, including collision-avoidance, to "
                    "the nearest available cloud region to minimize latency"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Even the nearest cloud region's WAN round-trip "
                    "latency will typically still exceed a strict 10-millisecond "
                    "budget, which is why edge processing — not merely a "
                    "closer region — is required."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Use a content delivery network (CDN) to cache the "
                    "collision-avoidance decision logic closer to the factory"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. CDNs cache static web content for faster "
                    "delivery to end users; they are not designed to execute "
                    "real-time industrial control-loop compute."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Increase the factory's WAN bandwidth to the cloud to "
                    "reduce latency"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Bandwidth increases throughput, not round-trip "
                    "latency, which is dominated by physical distance and "
                    "network hops — more bandwidth would not meet a 10ms "
                    "decision deadline."
                ),
            },
        ],
        "explanation": (
            "Edge/fog computing exists specifically to satisfy latency "
            "requirements that a centralized cloud region cannot meet, while "
            "still allowing less time-sensitive data to be forwarded to the "
            "cloud for analytics — a bandwidth increase or closer region "
            "cannot substitute for local processing."
        ),
    },
    # ------------------------------------------------------------------ #
    # ICS/SCADA and embedded systems (3.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3f-003",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "ICS/SCADA and embedded systems",
        "stem": (
            "A municipal water treatment facility's SCADA historian sits on the "
            "OT network and must periodically share production data with a "
            "corporate business-intelligence system on the IT network. Which "
            "architecture BEST protects the ICS environment from an IT-side "
            "compromise while still allowing the required data flow?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Create a segmented DMZ between the OT and IT networks "
                    "(consistent with the Purdue model), where the historian "
                    "replicates data outward to a broker in the DMZ, with no "
                    "direct IT-to-OT connections permitted"
                ),
                "correct": True,
                "rationale": (
                    "Correct. An OT/IT DMZ lets data flow out of the ICS "
                    "environment to a broker that IT systems can query, "
                    "without ever opening a direct path from the IT network "
                    "into the OT network where an IT compromise could reach "
                    "control systems."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Directly connect the corporate BI system to the OT "
                    "historian across a firewall rule that allows only the "
                    "specific database port"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Even a narrowly scoped port rule still creates "
                    "a direct path from the IT network into the OT network, "
                    "meaning a compromised IT host could reach the historian "
                    "directly — exactly what the design should prevent."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Establish a VPN tunnel allowing corporate IT users to "
                    "connect directly into the OT network for read-only query "
                    "access"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A VPN into the OT network still extends the IT "
                    "network's trust and attack surface directly into the "
                    "control environment, and compromised IT credentials could "
                    "be used to establish that same tunnel."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Remove network segmentation between OT and IT entirely "
                    "and rely on host-based antivirus running on the historian"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Eliminating segmentation removes the primary "
                    "layer of defense protecting the ICS environment, and "
                    "antivirus alone cannot compensate for a flat, unsegmented "
                    "network architecture."
                ),
            },
        ],
        "explanation": (
            "The Purdue-model DMZ pattern is the standard architecture for "
            "sharing data between OT and IT networks: it allows necessary data "
            "to flow outward through a broker while ensuring no direct "
            "connection ever originates from the IT side into the ICS "
            "environment."
        ),
    },
    # ------------------------------------------------------------------ #
    # IoT security (3.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3f-004",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "IoT security",
        "stem": (
            "Security researchers extract the firmware from a single smart "
            "irrigation valve controller sold by an agritech vendor and find a "
            "single, shared cloud API key embedded in every unit the vendor has "
            "ever shipped, used by each device to authenticate to the vendor's "
            "control-plane API. Because the key is identical across all "
            "deployed units, extracting it from one device grants control over "
            "every customer's irrigation valves worldwide. Which design change "
            "would MOST directly fix this specific flaw?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Provision each device with its own unique cryptographic "
                    "identity or credential (such as a per-device certificate "
                    "or key issued during manufacturing or first boot) instead "
                    "of a single shared secret embedded in the firmware image"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Unique per-device credentials mean that "
                    "extracting the key from one unit only compromises that "
                    "one device, eliminating the single point of catastrophic, "
                    "fleet-wide compromise created by a shared secret."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Encrypt the firmware image itself so the embedded key "
                    "cannot be extracted by researchers"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Firmware encryption raises the bar for "
                    "extraction but does not fix the underlying architectural "
                    "flaw — every device would still share the exact same "
                    "credential, so a single leaked build or extracted key "
                    "still compromises the entire fleet."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Require customers to change their vendor account password "
                    "every 90 days"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This addresses customer account passwords, an "
                    "unrelated credential; the flaw described is a shared "
                    "device-to-cloud API key, which a customer password policy "
                    "does not touch."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Rate-limit the number of API calls each device can make "
                    "per minute"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Rate limiting slows abuse but does not address "
                    "the root cause: an attacker using the valid shared key "
                    "would still authenticate successfully and could control "
                    "devices within the allowed rate."
                ),
            },
        ],
        "explanation": (
            "A single credential shared across an entire IoT device fleet is a "
            "critical design flaw because compromising any one unit "
            "compromises every unit; unique, per-device identity is the "
            "standard fix, not obfuscation or usage throttling."
        ),
    },
    # ------------------------------------------------------------------ #
    # Microservices and containerization (3.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3f-005",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Microservices and containerization",
        "stem": (
            "A container security review of a CI/CD build cluster finds two "
            "issues: (1) build containers mount the host's Docker socket "
            "(/var/run/docker.sock) so builds can create sibling containers, "
            "giving any process inside a build container root-equivalent "
            "control over the host's container runtime; and (2) several "
            "application pods run with hostPID and hostNetwork enabled, "
            "letting them see and interact with every process and network "
            "interface on the underlying host node. Which TWO changes would "
            "MOST directly remediate these two specific findings? (Select "
            "two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Remove the Docker socket mount from build containers, "
                    "using a rootless or sandboxed build strategy instead of "
                    "docker-in-docker via the host socket"
                ),
                "correct": True,
                "rationale": (
                    "Correct. This directly remediates finding 1 by removing "
                    "the build container's root-equivalent path to the host's "
                    "container runtime."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Disable hostPID and hostNetwork on the affected pods so "
                    "they run in their own isolated namespaces like standard "
                    "workloads"
                ),
                "correct": True,
                "rationale": (
                    "Correct. This directly remediates finding 2 by removing "
                    "the pods' visibility into and interaction with the host's "
                    "process table and network interfaces."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Increase the CPU and memory resource limits on the build "
                    "containers to speed up builds"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Resource limits affect performance, not the "
                    "socket-mount or host-namespace exposure described in "
                    "either finding."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Enable horizontal pod autoscaling for the application "
                    "pods"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Autoscaling addresses capacity and "
                    "availability, not the host-level exposure created by "
                    "hostPID/hostNetwork or the Docker socket mount."
                ),
            },
            {
                "id": "e",
                "text": (
                    "Add a network policy default-denying all pod-to-pod "
                    "traffic in the cluster"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A default-deny network policy helps limit "
                    "lateral movement between pods, but it does nothing about "
                    "a mounted Docker socket or host-namespace sharing, which "
                    "are host-level exposures rather than pod-to-pod traffic "
                    "issues."
                ),
            },
        ],
        "explanation": (
            "Removing the Docker socket mount and disabling hostPID/"
            "hostNetwork each map directly to one of the two findings; "
            "resource tuning, autoscaling, and pod-to-pod network policy all "
            "address different concerns and leave both host-level exposures "
            "in place."
        ),
    },
    # ------------------------------------------------------------------ #
    # Serverless and cloud architecture (3.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3f-006",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Serverless and cloud architecture",
        "stem": (
            "A photo-processing serverless function automatically triggers "
            "whenever a new object is uploaded to a cloud storage bucket. The "
            "bucket's resource policy currently allows uploads from any "
            "authenticated account in the cloud provider, not just the "
            "company's own accounts. A researcher demonstrates that a crafted "
            "object uploaded from an unrelated account triggers the function "
            "and causes it to throw unhandled errors while processing "
            "untrusted input. Which change MOST directly reduces the risk "
            "illustrated here?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Restrict the bucket's resource policy so only the "
                    "company's own trusted accounts or upload services can "
                    "write objects that trigger the function, and validate "
                    "object metadata and content before processing it"
                ),
                "correct": True,
                "rationale": (
                    "Correct. This closes the actual trust-boundary gap — "
                    "any authenticated account being able to trigger the "
                    "function — while input validation adds defense in depth "
                    "against unexpected or malicious object content."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Increase the function's concurrency limit so it can "
                    "handle more simultaneous malicious uploads without "
                    "throwing errors"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Raising concurrency lets more untrusted "
                    "invocations run in parallel; it does nothing to restrict "
                    "who can trigger the function in the first place and "
                    "could worsen the exposure."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Add a scheduled (cron) trigger instead of an "
                    "event-driven trigger so the function runs independently "
                    "of uploads"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Changing to a polling trigger does not "
                    "address the bucket's overly permissive resource policy "
                    "that allows untrusted accounts to write triggering "
                    "objects at all."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Grant the function's execution role full administrative "
                    "permissions so it can handle any unexpected object type "
                    "gracefully"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Broadening permissions increases the blast "
                    "radius of a successful exploit rather than reducing risk, "
                    "and does not address the untrusted trigger source."
                ),
            },
        ],
        "explanation": (
            "The real gap is a trust-boundary failure in the storage "
            "bucket's resource policy allowing any authenticated account to "
            "trigger the function; scoping that policy to trusted sources, "
            "combined with input validation, addresses the root cause rather "
            "than symptoms."
        ),
    },
    # ------------------------------------------------------------------ #
    # Virtualization and high availability (3.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3f-007",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Virtualization and high availability",
        "stem": (
            "A virtualization host is configured to overcommit memory, "
            "allowing the sum of all guest VMs' assigned RAM to exceed the "
            "host's 256 GB of physical RAM, relying on the hypervisor's memory "
            "ballooning and page-sharing to reclaim space as needed. During a "
            "period when all guest VMs simultaneously experience high memory "
            "demand, several VMs begin swapping to disk and become "
            "unresponsive, taking a customer-facing application offline. "
            "Which change BEST balances the cost benefit of memory "
            "overcommitment with high availability for this critical "
            "workload?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Reserve guaranteed, non-overcommitted memory specifically "
                    "for the critical customer-facing VM, while allowing "
                    "overcommitment to continue for lower-priority VMs on the "
                    "same host"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A memory reservation guarantees the critical VM "
                    "always has real physical RAM available and cannot be "
                    "forced into swapping, while preserving the cost savings "
                    "of overcommitment for less critical workloads."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Disable memory overcommitment entirely across the entire "
                    "host, provisioning 1:1 physical memory for every VM "
                    "regardless of criticality"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This eliminates the cost benefit of "
                    "overcommitment for every VM on the host, not just the "
                    "critical one, when a targeted reservation would achieve "
                    "the same protection more efficiently."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Increase the swap file size available to the hypervisor "
                    "so ballooning has more room to operate"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Swapping to disk is the actual performance "
                    "problem causing unresponsiveness; providing more swap "
                    "space would allow more swapping to occur, not prevent "
                    "the slowdown."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Migrate the critical VM to a Type 2 hosted hypervisor to "
                    "isolate it from overcommitment"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A Type 2 hypervisor does not inherently solve "
                    "memory overcommitment and adds the attack surface of a "
                    "full underlying host OS, making it an inappropriate fix "
                    "for this specific problem."
                ),
            },
        ],
        "explanation": (
            "Targeted memory reservations let a critical VM keep its "
            "high-availability guarantees while the rest of the host still "
            "benefits from overcommitment's cost savings — a more precise fix "
            "than disabling overcommitment everywhere or adding more swap."
        ),
    },
    # ------------------------------------------------------------------ #
    # Attack surface reduction (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3f-008",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Attack surface reduction",
        "stem": (
            "A vulnerability scan reveals a database server listening on its "
            "default port 1433, reachable from the entire corporate /16 "
            "subnet, even though only three specific application servers ever "
            "need to query it. Which action MOST directly reduces the "
            "server's attack surface?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Restrict access with a host-based or network ACL/"
                    "firewall rule allowing only the three specific "
                    "application server IPs to reach port 1433"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Narrowing the set of hosts that can reach the "
                    "database directly reduces the number of exposed entry "
                    "points to only what is actually required."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Change the database's listening port to a non-standard "
                    "value to make it harder to find"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is security through obscurity: it does "
                    "not reduce the number of hosts on the /16 that can still "
                    "reach the service once its new port is discovered "
                    "through a scan."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Enable database auditing to log all connection attempts "
                    "for later review"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Auditing provides detection and forensic "
                    "value after the fact, but it does not reduce the number "
                    "of hosts able to reach the exposed service."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Require TLS encryption for all connections to the "
                    "database"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Encrypting the channel protects data in "
                    "transit but does not reduce how many hosts on the subnet "
                    "can reach and attempt to authenticate to the database."
                ),
            },
        ],
        "explanation": (
            "Attack surface reduction means limiting exposure to only what "
            "is necessary; a scoped ACL restricting reachability to the "
            "specific required hosts achieves this directly, unlike "
            "obscurity, auditing, or encryption, which address different "
            "concerns."
        ),
    },
    # ------------------------------------------------------------------ #
    # Change management workflow (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3f-009",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Change management workflow",
        "stem": (
            "An audit finds that a developer who writes a code change is also "
            "the same person who approves that exact change and pushes it "
            "directly to production, with no second party ever reviewing it. "
            "The auditor flags this as a control weakness even though no "
            "incidents have occurred. Which principle does this practice "
            "violate?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Separation of duties — the person implementing a change "
                    "should not also be its sole approver, since independent "
                    "review of both necessity and risk is what prevents "
                    "mistakes or malicious changes from reaching production "
                    "unchecked"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Change management requires that approval "
                    "authority be separate from implementation authority so "
                    "that an independent party evaluates the change before it "
                    "reaches production."
                ),
            },
            {
                "id": "b",
                "text": (
                    "This is not a genuine control weakness as long as the "
                    "developer is experienced and the change is small"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Separation of duties should apply regardless "
                    "of the developer's experience level or the perceived "
                    "size of the change; both factors are subjective and "
                    "don't eliminate the risk of unchecked self-approval."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The fix is to require the developer to write more "
                    "detailed commit messages describing the change"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Better documentation improves traceability "
                    "but does not introduce the independent review that "
                    "separation of duties requires."
                ),
            },
            {
                "id": "d",
                "text": (
                    "This risk is fully mitigated as long as the developer "
                    "tests the change in a staging environment first, since "
                    "staging testing removes the need for independent "
                    "approval"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Staging tests verify functionality, not "
                    "whether the change should be approved by someone other "
                    "than its author; independent approval remains a "
                    "distinct, necessary control."
                ),
            },
        ],
        "explanation": (
            "Separation of duties in change management ensures that no "
            "single individual can both implement and approve a production "
            "change unchecked; documentation quality and pre-deployment "
            "testing are valuable but do not substitute for independent "
            "review."
        ),
    },
    # ------------------------------------------------------------------ #
    # Failure modes (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3f-010",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Failure modes",
        "stem": (
            "A freight logistics company's inline email security gateway "
            "scans all outbound attachments for malware before messages leave "
            "the network. Leadership has determined that a multi-hour halt in "
            "outbound email during peak shipping season would cause far "
            "greater financial harm than the small residual risk of a brief "
            "window of unscanned outbound mail during a gateway failure. How "
            "should the gateway's failure behavior be configured, and what is "
            "the accepted trade-off?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Fail-open, allowing outbound mail to continue flowing "
                    "unscanned if the gateway fails, accepting a temporary "
                    "increase in the risk of unscanned attachments leaving "
                    "the network in exchange for preserving mail availability"
                ),
                "correct": True,
                "rationale": (
                    "Correct. This matches the stated priority: continued "
                    "mail flow during peak season outweighs the brief "
                    "increased risk of an unscanned outbound message during a "
                    "device failure."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Fail-closed, blocking all outbound mail if the gateway "
                    "fails, guaranteeing no unscanned attachment ever leaves "
                    "the network"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Fail-closed would halt outbound email during "
                    "peak shipping season on any gateway failure, directly "
                    "contradicting the stated priority of preserving mail "
                    "availability."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Configure active-active clustering for the gateway, "
                    "which by itself removes the need to define a failure "
                    "mode"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Clustering reduces the likelihood of a total "
                    "failure but each node still needs a defined failure "
                    "behavior; it does not eliminate the need to choose "
                    "fail-open or fail-closed."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Configure the gateway in passive tap mode, which "
                    "continues scanning without ever blocking mail flow"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Passive tap mode means the device is not "
                    "actually inline and cannot block anything even during "
                    "normal operation, which contradicts the scenario's "
                    "description of an inline gateway that scans before mail "
                    "leaves the network."
                ),
            },
        ],
        "explanation": (
            "When continued business operation is explicitly prioritized "
            "over a temporary security gap, an inline security appliance "
            "should be configured to fail-open rather than fail-closed."
        ),
    },
    # ------------------------------------------------------------------ #
    # Firewalls (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3f-011",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Firewalls",
        "stem": (
            "A US-only regional credit union has no customers, employees, or "
            "business operations outside North America, yet its perimeter "
            "firewall logs show credential-stuffing login attempts against its "
            "online banking portal originating from IP ranges in several "
            "countries where it has zero legitimate business. Which firewall "
            "capability would MOST efficiently reduce this specific class of "
            "attack traffic without requiring per-IP rule maintenance?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Geo-IP/geolocation-based filtering, blocking inbound "
                    "traffic from entire countries or regions outside the "
                    "credit union's legitimate customer base, updated "
                    "automatically via a maintained geo-IP database"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Geo-IP filtering blocks broad swaths of "
                    "irrelevant geographic traffic at the firewall without "
                    "requiring the ongoing maintenance of individual IP rules "
                    "as attackers rotate addresses."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Increase the account lockout threshold after failed "
                    "login attempts"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is an application-layer control that "
                    "does not reduce the volume of attack traffic reaching "
                    "the firewall, and a looser threshold could even increase "
                    "successful credential-stuffing attempts."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Implement NAT to hide the true internal IP addresses of "
                    "the banking application servers"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. NAT does not filter inbound traffic by "
                    "geographic origin, and the servers must remain publicly "
                    "reachable for legitimate customers regardless of NAT."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Add individual firewall deny rules for each specific "
                    "attacking IP address as they're identified in the logs"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is reactive, does not scale, and "
                    "directly conflicts with the requirement to avoid "
                    "per-IP rule maintenance, since attackers can trivially "
                    "rotate to new source addresses."
                ),
            },
        ],
        "explanation": (
            "Geo-IP filtering is the standard firewall capability for "
            "efficiently blocking traffic from entire regions with no "
            "legitimate business relationship, avoiding the unscalable "
            "burden of maintaining individual IP-based rules."
        ),
    },
    # ------------------------------------------------------------------ #
    # Network appliances (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3f-012",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Network appliances",
        "stem": (
            "A security operations center wants to feed copies of all network "
            "traffic crossing a core switch to three separate monitoring "
            "tools — an IDS, a packet-capture appliance, and a NetFlow "
            "collector — simultaneously, without adding latency to production "
            "traffic and without configuring a separate SPAN port on the "
            "switch for each individual tool. Which appliance BEST fulfills "
            "this need?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A network packet broker (TAP aggregator) that receives "
                    "one copied traffic feed and replicates/distributes it to "
                    "multiple monitoring tools"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A packet broker is purpose-built to take a "
                    "single aggregated traffic feed and fan it out to "
                    "multiple analysis tools, removing the need for a "
                    "dedicated SPAN port per tool."
                ),
            },
            {
                "id": "b",
                "text": (
                    "A forward proxy, configured to relay traffic to each "
                    "monitoring tool in sequence"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A forward proxy mediates outbound client "
                    "requests to the internet; it is not designed to "
                    "replicate and distribute copied network traffic to "
                    "monitoring tools."
                ),
            },
            {
                "id": "c",
                "text": (
                    "A reverse proxy placed in front of the monitoring tools"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A reverse proxy fronts and load-balances "
                    "requests to backend servers; it has no role in "
                    "replicating a copy of network traffic to multiple "
                    "passive monitoring tools."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Additional SPAN ports on the switch, one dedicated to "
                    "each of the three tools"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is exactly the per-tool SPAN port "
                    "approach the requirement explicitly seeks to avoid, and "
                    "it adds switch CPU/backplane overhead as more mirrored "
                    "sessions are configured."
                ),
            },
        ],
        "explanation": (
            "A network packet broker (TAP aggregator) is the appliance "
            "purpose-built to replicate one traffic feed to many monitoring "
            "tools simultaneously, distinct from proxies and from simply "
            "adding more SPAN ports."
        ),
    },
    # ------------------------------------------------------------------ #
    # Port security and 802.1X (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3f-013",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Port security and 802.1X",
        "stem": (
            "An attacker on a compromised workstation sends forged ARP "
            "replies claiming to own the default gateway's IP address, "
            "causing other hosts on the same VLAN to send their traffic to "
            "the attacker's machine instead (an on-path attack). 802.1X is "
            "already deployed and successfully authenticating all connected "
            "devices. Which additional switch-level control specifically "
            "prevents this ARP-spoofing attack?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Dynamic ARP Inspection (DAI), which validates ARP "
                    "packets against a trusted binding table built from DHCP "
                    "snooping and drops ARP replies that don't match a "
                    "legitimate IP-to-MAC binding"
                ),
                "correct": True,
                "rationale": (
                    "Correct. DAI specifically inspects and validates ARP "
                    "traffic against known-good IP-to-MAC bindings, dropping "
                    "forged ARP replies like the one described."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Increasing the 802.1X re-authentication interval so "
                    "devices are checked more frequently"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. 802.1X authenticates device/port access; it "
                    "does not validate the content of ARP traffic already "
                    "flowing on a port after authentication succeeds."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Enabling port security to limit the number of MAC "
                    "addresses allowed per port"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The attacker's own device is already "
                    "legitimately authenticated on its own port; limiting "
                    "MAC counts per port does not validate ARP packet "
                    "content or prevent it from claiming another IP's MAC "
                    "binding."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Configuring 802.1X to use MAC Authentication Bypass "
                    "(MAB) as the primary authentication method"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. MAB is a fallback authentication method for "
                    "devices that cannot run an 802.1X supplicant; it has no "
                    "bearing on ARP spoofing occurring after a device is "
                    "already authenticated."
                ),
            },
        ],
        "explanation": (
            "Dynamic ARP Inspection is the switch-level control specifically "
            "designed to detect and drop forged ARP traffic, addressing a "
            "risk that port-based authentication controls like 802.1X and "
            "MAB do not cover."
        ),
    },
    # ------------------------------------------------------------------ #
    # SDN and logical segmentation (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3f-014",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SDN and logical segmentation",
        "stem": (
            "A company hosts a public-facing web server that must be "
            "reachable from the internet and also needs to query an internal "
            "database server that must never be directly reachable from the "
            "internet. Which network design BEST achieves this?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Place the web server in a screened subnet (DMZ) bounded "
                    "by firewalls, allowing only the specific necessary "
                    "traffic from the DMZ to the internal database segment, "
                    "with the internal network never directly exposed to the "
                    "internet"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A screened subnet isolates the internet-facing "
                    "server in its own segment, allowing tightly controlled "
                    "traffic to the internal database while keeping the "
                    "internal network itself unreachable from the internet."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Place both the web server and the database on the same "
                    "internal VLAN as user workstations for simplicity"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This directly exposes the internal network "
                    "and database to compromise if the internet-facing web "
                    "server is breached, with no segmentation between them."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Give the web server a direct route to the internal "
                    "database VLAN with no firewall between them, since both "
                    "are company-owned assets"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Common ownership does not eliminate risk; "
                    "with no boundary control, a compromised internet-facing "
                    "web server would have unrestricted access to the "
                    "internal database segment."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Host the web server directly in the internal network "
                    "and open only port 443 inbound on the perimeter firewall"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This still places an internet-facing server "
                    "inside the internal network itself, exposing the "
                    "internal segment directly rather than isolating the "
                    "public-facing component in its own DMZ layer."
                ),
            },
        ],
        "explanation": (
            "A screened subnet (DMZ) is the standard logical segmentation "
            "pattern for isolating an internet-facing server from an "
            "internal network that must never be directly reachable from the "
            "internet."
        ),
    },
    # ------------------------------------------------------------------ #
    # Secure communication (VPN/TLS/IPSec) (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3f-015",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Secure communication (VPN/TLS/IPSec)",
        "stem": (
            "A financial services web application still accepts TLS 1.0 and "
            "TLS 1.1 connections alongside TLS 1.3 for backward compatibility "
            "with a small number of legacy client devices. A security "
            "assessment demonstrates that an on-path attacker can force a "
            "negotiation down to TLS 1.0, which uses weaker cipher suites "
            "vulnerable to known exploits. Which change eliminates this "
            "downgrade risk while retaining strong TLS support?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Disable support for TLS 1.0 and TLS 1.1 entirely on the "
                    "server, allowing only TLS 1.2 and TLS 1.3, so there is "
                    "no weaker protocol version left for an attacker to "
                    "negotiate down to"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Removing support for the weaker protocol "
                    "versions entirely closes the downgrade path, since an "
                    "attacker cannot force negotiation to a version the "
                    "server no longer offers."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Configure the server to prefer TLS 1.3 while still "
                    "allowing TLS 1.0/1.1 as a fallback"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Merely preferring the strongest version does "
                    "not prevent an on-path attacker from actively "
                    "interfering with negotiation to force the still-enabled "
                    "weaker versions."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Increase the TLS session cache timeout so fewer "
                    "renegotiations occur"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Session cache timeout is unrelated to which "
                    "protocol versions are permitted during the initial "
                    "handshake and does not close the downgrade path."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Require client-certificate authentication for all TLS "
                    "connections"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Mutual TLS authenticates client identity but "
                    "does not prevent negotiation down to a weaker, still-"
                    "enabled protocol version."
                ),
            },
        ],
        "explanation": (
            "The only way to eliminate a protocol-downgrade attack is to "
            "remove support for the vulnerable protocol versions entirely; "
            "preference ordering, session caching, and client authentication "
            "do not close the downgrade path."
        ),
    },
    # ------------------------------------------------------------------ #
    # Zero Trust / SASE (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3f-016",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Zero Trust / SASE",
        "stem": (
            "A company's security team is rewriting its access-control "
            "philosophy around Zero Trust principles as defined in NIST SP "
            "800-207. Which TWO statements correctly describe core Zero "
            "Trust principles? (Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "No user, device, or network location is trusted by "
                    "default — including traffic that originates from inside "
                    "the corporate network perimeter — every access request "
                    "must be explicitly verified"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Zero Trust explicitly rejects implicit trust "
                    "based on network location, treating internal traffic "
                    "with the same scrutiny as external traffic."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Access decisions should be made per-session or "
                    "per-request based on the minimum privilege necessary for "
                    "that specific resource, evaluated continuously rather "
                    "than granted permanently at initial login"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Continuous, least-privilege, per-request "
                    "evaluation — rather than a one-time login granting "
                    "persistent trust — is a core Zero Trust tenet."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Once a device successfully authenticates and joins the "
                    "internal network, it should be implicitly trusted for "
                    "the remainder of its connection to reduce authentication "
                    "overhead"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Granting persistent implicit trust after "
                    "initial authentication directly contradicts Zero "
                    "Trust's requirement for continuous verification."
                ),
            },
            {
                "id": "d",
                "text": (
                    "A strong perimeter firewall is sufficient on its own to "
                    "achieve Zero Trust, since all internal traffic behind it "
                    "can be considered secure"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This describes the traditional perimeter-"
                    "based trust model that Zero Trust was specifically "
                    "designed to replace."
                ),
            },
            {
                "id": "e",
                "text": (
                    "Zero Trust applies only to remote or external users; "
                    "internal on-premises users connecting from the corporate "
                    "LAN are exempt from continuous verification"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This contradicts the core tenet that no "
                    "location — including the internal LAN — is implicitly "
                    "trusted."
                ),
            },
        ],
        "explanation": (
            "Zero Trust is defined by the elimination of implicit, "
            "location-based trust and by continuous, least-privilege "
            "evaluation of every access request; perimeter-only defenses and "
            "persistent post-login trust are exactly what it replaces."
        ),
    },
    # ------------------------------------------------------------------ #
    # Data classification (3.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3f-017",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Data classification",
        "stem": (
            "A university maintains two datasets: (1) anonymized aggregate "
            "survey results intended for public academic publication, with no "
            "way to re-identify individual respondents, and (2) an unredacted "
            "roster containing students' names and Social Security numbers "
            "used for financial aid processing. Which classification pairing "
            "is MOST appropriate?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Dataset 1 should be classified Public, since it carries "
                    "no re-identification risk and is intended for public "
                    "release; Dataset 2 should be classified Confidential or "
                    "Restricted, since it contains regulated PII whose "
                    "disclosure could enable identity theft"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Classification should reflect actual "
                    "disclosure impact: the anonymized dataset has none, "
                    "warranting Public, while the SSN roster carries severe "
                    "harm potential, warranting the organization's highest "
                    "sensitivity tier."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Both datasets should be classified Internal, since both "
                    "originate from the same university system"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A single blanket classification based on "
                    "origin ignores the very different actual sensitivity and "
                    "disclosure impact of each dataset."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Dataset 1 should be classified Confidential because it "
                    "involves survey participants; Dataset 2 should be "
                    "classified Public because financial aid records are "
                    "administrative rather than academic"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This reverses the correct assignments — the "
                    "anonymized dataset has no re-identification risk, while "
                    "unredacted SSNs are precisely the kind of regulated data "
                    "that should never be classified Public."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Data classification only applies to data stored "
                    "electronically, so a printed roster used by financial "
                    "aid staff does not require a classification label"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Classification requirements apply to data "
                    "based on its sensitivity, regardless of the medium or "
                    "format in which it is stored or handled."
                ),
            },
        ],
        "explanation": (
            "Classification decisions must be driven by actual disclosure "
            "impact for each specific dataset, not by its source system or "
            "storage medium; regulated PII like unredacted SSNs warrants the "
            "highest sensitivity tier while genuinely anonymized data can be "
            "public."
        ),
    },
    # ------------------------------------------------------------------ #
    # Data protection methods (3.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3f-018",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Data protection methods",
        "stem": (
            "A ride-share company encrypts its entire database volume "
            "containing driver background-check results using full-disk/"
            "volume-level encryption at rest. An internal audit finds that "
            "any application service account with basic database read access "
            "can query the plaintext background-check fields once the volume "
            "is mounted and the database is running. Which additional control "
            "gap does this reveal?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Volume-level encryption alone doesn't restrict who can "
                    "read decrypted data once the database is online; "
                    "granular access controls, column-level protection, or "
                    "masking on the specific sensitive fields are also needed"
                ),
                "correct": True,
                "rationale": (
                    "Correct. At-rest encryption protects data if the "
                    "physical volume or backup is stolen, but once the "
                    "database is mounted and running, additional "
                    "least-privilege access controls on the sensitive fields "
                    "are required to limit who can read them."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The database should be re-encrypted using a stronger "
                    "algorithm, since the current algorithm is inadequate"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Nothing in the finding suggests the "
                    "encryption algorithm itself is weak; the gap is that "
                    "access to the decrypted, running data isn't restricted "
                    "by field-level permissions."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Full-disk encryption is unnecessary once the OS itself "
                    "enforces file permissions"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. At-rest encryption remains valuable for "
                    "scenarios like physical theft of drives or stolen "
                    "backups, independent of OS file permissions; this "
                    "finding doesn't make it unnecessary."
                ),
            },
            {
                "id": "d",
                "text": (
                    "This finding indicates the encryption keys must be "
                    "rotated immediately"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Key rotation addresses a different concern "
                    "(potential key compromise) and does not address the "
                    "access-control gap that lets any service account read "
                    "the plaintext once the database is running."
                ),
            },
        ],
        "explanation": (
            "Encryption at rest and access control address different "
            "layers of protection: at-rest encryption protects stored, "
            "unmounted data, while granular, least-privilege access controls "
            "are required to limit exposure once the data is decrypted and "
            "the database is actively running."
        ),
    },
    # ------------------------------------------------------------------ #
    # Data states (3.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3f-019",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Data states",
        "stem": (
            "A real-time fraud-scoring platform decrypts customer transaction "
            "data in server memory to run its scoring model, then re-encrypts "
            "the results before writing them back to disk. A security review "
            "is concerned that an attacker with root access to the underlying "
            "host — or a malicious cloud administrator — could scrape "
            "plaintext data directly from the process's memory while scoring "
            "is in progress. Which control specifically protects data in this "
            "state (data in use)?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Confidential computing using a hardware-based trusted "
                    "execution environment (TEE)/secure enclave, which keeps "
                    "data encrypted even while being actively processed in "
                    "memory, so it is never exposed in plaintext to the host "
                    "OS or a privileged administrator"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Confidential computing is specifically "
                    "designed to protect data in use, ensuring plaintext is "
                    "never exposed even to someone with root or "
                    "administrator-level access to the underlying host."
                ),
            },
            {
                "id": "b",
                "text": (
                    "TLS 1.3 encrypting all API traffic into and out of the "
                    "platform"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. TLS protects data in transit across the "
                    "network; it has no effect on plaintext exposure while "
                    "data is actively being processed in the server's memory."
                ),
            },
            {
                "id": "c",
                "text": (
                    "AES-256 encryption of the database volume where results "
                    "are ultimately stored"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This protects data at rest on disk; it does "
                    "nothing to prevent plaintext exposure in memory while "
                    "the data is actively being scored."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Role-based access control (RBAC) restricting which "
                    "employees can query the database"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. RBAC governs authorized access to stored "
                    "data, not memory-level exposure during active "
                    "processing, and it would not stop a privileged "
                    "administrator or root-level attacker as described."
                ),
            },
        ],
        "explanation": (
            "Each data state requires a distinct control: TLS protects data "
            "in transit, disk encryption protects data at rest, and "
            "confidential computing/TEEs are the control specifically "
            "designed to protect data in use from exposure even to "
            "privileged host access."
        ),
    },
    # ------------------------------------------------------------------ #
    # Tokenization and masking (3.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3f-020",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Tokenization and masking",
        "stem": (
            "A payment processor needs a technique that replaces credit card "
            "primary account numbers (PANs) in its transaction database with "
            "a non-sensitive substitute value that can later be reversed back "
            "to the original PAN by an authorized lookup against a secure "
            "vault, so that recurring billing can still function. Which "
            "technique fits this requirement, as opposed to a technique that "
            "simply displays only the last four digits and cannot be "
            "reversed?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Tokenization — replaces the PAN with a token mapped in a "
                    "secure vault, reversible by authorized lookup, unlike "
                    "masking, which only obscures the displayed digits and is "
                    "not designed to be reversed"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Tokenization is specifically designed to be "
                    "reversible through an authorized vault lookup, "
                    "supporting a legitimate future need like recurring "
                    "billing, unlike masking."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Data masking, because it permanently and irreversibly "
                    "protects the data from any future reconstruction"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This accurately describes masking, but "
                    "irreversibility is the opposite of what's needed — "
                    "masking cannot support recurring billing, which requires "
                    "recovering the original PAN."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Hashing with a fixed salt, because hash values can "
                    "always be reversed back to the original PAN using the "
                    "same salt"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is factually wrong — hashing is a "
                    "one-way function and cannot be reversed back to the "
                    "original value regardless of salt, making it unsuitable "
                    "for a requirement that needs later recovery."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Symmetric encryption of the entire database column "
                    "using AES-256 in ECB mode"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. ECB mode is a known-poor choice for "
                    "structured data like card numbers because identical "
                    "plaintext blocks produce identical ciphertext, leaking "
                    "patterns; this also doesn't match the vault-lookup "
                    "substitute-value pattern the requirement describes."
                ),
            },
        ],
        "explanation": (
            "Tokenization is purpose-built for cases requiring authorized, "
            "reversible recovery of an original sensitive value through a "
            "secure vault, distinguishing it from masking (irreversible), "
            "hashing (one-way), and poorly chosen encryption modes."
        ),
    },
    # ------------------------------------------------------------------ #
    # Backups and replication (3.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3f-021",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Backups and replication",
        "stem": (
            "A company replicates nightly backups from its primary data "
            "center to a DR site connected only by a low-bandwidth satellite "
            "link. Transferring a full 2 TB backup image each night "
            "consistently fails to complete before the link's daily "
            "maintenance window closes. Which replication approach would "
            "MOST reduce the data volume transferred each night while still "
            "keeping the DR copy current?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Block-level (change-block) incremental replication, "
                    "transferring only the disk blocks that changed since the "
                    "last replication cycle rather than the full image each "
                    "time"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Block-level incremental replication only "
                    "sends the changed blocks, dramatically reducing the "
                    "nightly transfer volume compared to shipping a full 2 TB "
                    "image every time."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Switch to full backups twice per day to catch up on the "
                    "transfer backlog"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This doubles the bandwidth demand on an "
                    "already-constrained link, making the problem worse "
                    "rather than better."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Compress the backup images using a lossy compression "
                    "algorithm before transfer"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Lossy compression discards data, which is "
                    "unacceptable for backups that must be restorable "
                    "exactly; only lossless compression could be considered, "
                    "and even that alone doesn't match the reduction "
                    "block-level replication provides for mostly-unchanged "
                    "data."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Increase the backup retention period from 30 to 90 days"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Retention period affects how long backups "
                    "are stored, not how much data is transferred nightly; "
                    "it would increase storage needs without addressing the "
                    "transfer bottleneck."
                ),
            },
        ],
        "explanation": (
            "Block-level incremental replication is specifically designed "
            "to minimize data transferred over constrained links by sending "
            "only changed blocks, unlike more frequent full backups, lossy "
            "compression, or retention policy changes, none of which reduce "
            "nightly transfer volume correctly."
        ),
    },
    # ------------------------------------------------------------------ #
    # High availability (3.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3f-022",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "High availability",
        "stem": (
            "An application's high-availability design directs all read "
            "queries to a pool of asynchronously replicated read-replica "
            "database nodes to reduce load on the primary write node. Users "
            "report that immediately after updating their profile, the "
            "change is not reflected when the page reloads a split second "
            "later, though it appears correctly moments after. Which "
            "characteristic of this HA design explains the behavior, and is "
            "it a defect?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "This is expected read-after-write inconsistency caused "
                    "by asynchronous replication lag between the primary and "
                    "its read replicas — not a system defect, but an "
                    "accepted trade-off of this scaling design; if "
                    "unacceptable, sensitive read-after-write paths would "
                    "need to be routed to the primary node instead"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Asynchronous replication introduces a brief "
                    "propagation delay by design; this behavior is an "
                    "expected trade-off of using async read replicas, not a "
                    "malfunction, and the fix is routing sensitive reads to "
                    "the primary rather than assuming failure."
                ),
            },
            {
                "id": "b",
                "text": (
                    "This indicates the read replicas have failed and should "
                    "immediately be removed from the load-balancing pool"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The replicas are functioning normally; "
                    "asynchronous replication lag is not the same as a "
                    "replica failure, and removing healthy replicas would "
                    "needlessly reduce read capacity."
                ),
            },
            {
                "id": "c",
                "text": (
                    "This indicates a split-brain condition between the "
                    "primary and replica nodes"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Split-brain describes multiple nodes "
                    "independently believing they are primary and accepting "
                    "conflicting writes; this scenario is a one-directional "
                    "replication lag on reads, a different phenomenon "
                    "entirely."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Synchronous replication is already in use, so this "
                    "behavior is unexpected and indicates data corruption"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario explicitly states the "
                    "replication is asynchronous, and nothing described "
                    "suggests any data was actually corrupted or lost — only "
                    "briefly delayed in propagation."
                ),
            },
        ],
        "explanation": (
            "Asynchronous read-replica architectures trade strict "
            "consistency for read scalability; the resulting brief "
            "read-after-write lag is an expected characteristic of the "
            "design, distinct from replica failure, split-brain, or data "
            "corruption."
        ),
    },
    # ------------------------------------------------------------------ #
    # Power resilience (3.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3f-023",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Power resilience",
        "stem": (
            "A rack audit finds that a critical database server has dual "
            "redundant power supplies as designed, but both power cords are "
            "plugged into the same power distribution unit (PDU), which is "
            "fed by a single upstream circuit. When that circuit's breaker "
            "trips during a maintenance error, the server loses power "
            "completely despite having two power supplies. Which change "
            "corrects this design flaw?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Connect each of the server's two power supplies to a "
                    "separate PDU, each fed by an independent upstream "
                    "circuit, so that a single circuit or PDU failure cannot "
                    "take down both supplies simultaneously"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Dual power supplies only provide real "
                    "redundancy if each is fed from an independent power "
                    "path; connecting both cords to the same PDU/circuit "
                    "defeats that redundancy entirely, as this incident "
                    "demonstrated."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Add a third redundant power supply to the server for "
                    "additional protection"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Adding another power supply does not fix the "
                    "root cause if all three cords remain plugged into the "
                    "same PDU and circuit — the single point of failure "
                    "persists."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Replace the PDU with a higher-amperage model to prevent "
                    "the breaker from tripping"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This may reduce the chance of this specific "
                    "trip, but the design flaw remains: any future failure "
                    "upstream of that single PDU or circuit would still take "
                    "down both supplies at once."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Schedule maintenance work only during off-peak hours to "
                    "reduce the chance of accidental breaker trips"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This reduces the odds of this particular "
                    "type of incident but does not eliminate the underlying "
                    "single point of failure created by sharing one PDU and "
                    "circuit."
                ),
            },
        ],
        "explanation": (
            "Redundant power supplies only deliver true resilience when "
            "each is fed from an independent PDU and upstream circuit; "
            "sharing a single power path — regardless of PDU capacity or "
            "maintenance timing — reintroduces the single point of failure "
            "the redundant supplies were meant to eliminate."
        ),
    },
    # ------------------------------------------------------------------ #
    # Recovery sites (3.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3f-024",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Recovery sites",
        "stem": (
            "A company's primary production environment runs in a single "
            "public cloud provider's us-east region. As its disaster recovery "
            "strategy, it provisions a warm site in the same provider's "
            "us-west region, reasoning that the geographic distance satisfies "
            "disaster-recovery requirements. During a global outage of that "
            "provider's identity and authentication control plane — which "
            "affects all of the provider's regions simultaneously — the "
            "company finds it cannot manage or fail over to either region. "
            "What flaw does this reveal in the recovery site strategy?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The DR site depended on the same cloud provider's "
                    "shared global control-plane services as the primary, so "
                    "a provider-wide outage affected both sites "
                    "simultaneously; true resilience against provider-wide "
                    "failures requires diversifying providers, not just "
                    "regions"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Regional separation only protects against "
                    "regional disasters; a shared global control plane (such "
                    "as identity/authentication services) can fail across "
                    "every region of a single provider at once, which region "
                    "diversity alone does not address."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The warm site should have been located in the same "
                    "region as the primary to reduce replication latency"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Placing the DR site in the same region "
                    "eliminates geographic disaster protection entirely and "
                    "contradicts the basic purpose of a recovery site; this "
                    "does not address the control-plane dependency issue "
                    "either."
                ),
            },
            {
                "id": "c",
                "text": (
                    "This flaw only affects hot sites, not warm sites, so "
                    "switching to a warm-site model would have prevented it"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario already describes a warm site; "
                    "the control-plane dependency issue is unrelated to "
                    "whether the site is hot, warm, or cold — it stems from "
                    "using the same provider for both sites."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Regulatory data sovereignty rules were violated by "
                    "using two regions of the same provider"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Nothing in the scenario describes a data "
                    "sovereignty or regulatory violation; the failure "
                    "described is an availability issue caused by a shared "
                    "provider-wide control plane, not a compliance issue."
                ),
            },
        ],
        "explanation": (
            "Choosing a DR site in a different region of the same cloud "
            "provider only protects against regional disasters, not against "
            "failures in services the provider operates globally across all "
            "regions; guarding against provider-wide outages requires true "
            "platform/provider diversity for the recovery site."
        ),
    },
    # ------------------------------------------------------------------ #
    # Resilience testing (3.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3f-025",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Resilience testing",
        "stem": (
            "A compliance auditor wants to distinguish resilience-testing "
            "methods that are purely discussion- or document-based and never "
            "involve technically exercising any system, from methods that "
            "involve actually executing technical recovery actions against "
            "systems, even if not in full production. Which TWO of the "
            "following are purely discussion/document-based and do NOT "
            "involve technically exercising any system? (Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Tabletop exercise — a verbal walkthrough of roles and "
                    "decisions during a hypothetical incident, with no "
                    "systems touched"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A tabletop exercise is discussion-based only; "
                    "participants talk through their response without "
                    "interacting with any live or test system."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Checklist/document review — confirming the DR plan's "
                    "documentation is current and complete, with no systems "
                    "touched"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A checklist review is a passive document "
                    "verification activity that never involves technically "
                    "exercising any system."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Simulation test — technically injecting a mock incident "
                    "into an isolated, non-production copy of the "
                    "environment and exercising real recovery actions"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A simulation test involves genuine technical "
                    "actions against an isolated environment, which is not "
                    "purely discussion/document-based."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Parallel test — the DR site actually processes "
                    "production data alongside the primary without cutting "
                    "over"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A parallel test technically exercises the DR "
                    "environment by having it actively process real data, "
                    "which goes beyond discussion or document review."
                ),
            },
            {
                "id": "e",
                "text": (
                    "Full interruption (live) failover test — actually "
                    "cutting production traffic over to the DR site"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A full interruption test is the most "
                    "technically hands-on form of resilience testing, "
                    "actually shifting live traffic — the opposite of a "
                    "discussion-only activity."
                ),
            },
        ],
        "explanation": (
            "Tabletop exercises and checklist reviews are both discussion/"
            "document-based activities that never touch a live or test "
            "system, distinguishing them from simulation, parallel, and full "
            "interruption tests, all of which involve genuine technical "
            "recovery actions."
        ),
    },
    # ------------------------------------------------------------------ #
    # Third-party agreement types (3.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3f-026",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Third-party agreement types",
        "stem": (
            "Two companies are beginning preliminary discussions about a "
            "potential future partnership. Before either side is willing to "
            "share proprietary technical specifications and pricing models "
            "during these early talks, they want a legal agreement obligating "
            "both parties not to disclose or use each other's shared "
            "information outside the discussions — without yet committing "
            "either company to any service, purchase, or partnership terms. "
            "Which agreement type BEST fits this specific need?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Non-disclosure agreement (NDA)",
                "correct": True,
                "rationale": (
                    "Correct. An NDA is the agreement purpose-built to "
                    "create a legally binding confidentiality obligation for "
                    "information exchanged during preliminary discussions, "
                    "without committing either party to any service, "
                    "purchase, or partnership terms."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Memorandum of understanding (MOU), since it is the "
                    "standard first document exchanged before any formal "
                    "agreement"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. An MOU documents mutual intent and general "
                    "goals between parties, but its purpose is different "
                    "from creating a legally binding confidentiality "
                    "obligation, which is what's explicitly required here."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Service level agreement (SLA), establishing measurable "
                    "performance commitments before either party commits to "
                    "a service"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. No service has been defined yet at this "
                    "preliminary stage, and SLAs address performance metrics "
                    "and uptime commitments, not confidentiality of shared "
                    "information."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Business partnership agreement (BPA), formally defining "
                    "ownership and financial responsibilities of the "
                    "still-hypothetical partnership"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is premature — the companies have not "
                    "committed to a partnership yet, only to preliminary "
                    "confidential discussions, so defining ownership and "
                    "financial responsibilities does not fit this stage."
                ),
            },
        ],
        "explanation": (
            "An NDA is the specific agreement type for protecting "
            "confidential information exchanged during early, non-binding "
            "discussions, distinct from an MOU's statement of intent, an "
            "SLA's performance commitments, or a BPA's formal partnership "
            "terms."
        ),
    },
]

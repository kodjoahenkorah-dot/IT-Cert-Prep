"""CompTIA Security+ (SY0-701) practice question bank — Domain 3, file D.

40 scenario-driven questions (36 multiple_choice + 4 multiple_response)
covering every study_topic label listed under domain 3 in
``_topic_labels.json``.
"""

from __future__ import annotations

QUESTIONS = [
    # ------------------------------------------------------------------ #
    # Architecture trade-offs (3.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3d-001",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Architecture trade-offs",
        "stem": (
            "A software vendor is deciding between a single-tenant architecture, "
            "in which each customer receives a dedicated database and application "
            "instance, and a multi-tenant architecture, in which many customers "
            "share the same database schema with logical separation by tenant ID. "
            "Which trade-off BEST justifies choosing the multi-tenant model?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Multi-tenancy lowers per-customer operating cost and lets a "
                    "single patch or update apply to every customer at once, at "
                    "the cost of a shared-fate blast radius if a tenant-isolation "
                    "control fails"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Multi-tenant architectures achieve economies of "
                    "scale — one codebase, one patch cycle — but trade away the "
                    "hard isolation of single-tenant deployments, so a flaw in "
                    "the isolation logic can expose or affect many customers at "
                    "once."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Single-tenant architecture is always cheaper to operate "
                    "because it eliminates the need for logical separation logic"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Single-tenant deployments are generally more "
                    "expensive to operate at scale, since every customer requires "
                    "its own dedicated infrastructure and patch cycle rather than "
                    "sharing one."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Multi-tenant architecture provides stronger data isolation "
                    "between customers than single-tenant architecture"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The opposite is true — single-tenant deployments "
                    "provide the strongest isolation because each customer has "
                    "entirely separate infrastructure; multi-tenancy relies on "
                    "logical controls that can fail."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Single-tenant architecture scales more elastically to "
                    "sudden spikes in the number of new customers"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Provisioning a full dedicated stack for every new "
                    "customer is slower and less elastic than onboarding a new "
                    "tenant into an existing shared multi-tenant platform."
                ),
            },
        ],
        "explanation": (
            "Single-tenant vs. multi-tenant is a classic isolation-versus-"
            "efficiency trade-off: single-tenancy maximizes isolation at higher "
            "cost, while multi-tenancy maximizes cost efficiency and operational "
            "simplicity at the cost of shared-fate risk if isolation controls "
            "fail."
        ),
    },
    # ------------------------------------------------------------------ #
    # Cloud architecture (3.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3d-002",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Cloud architecture",
        "stem": (
            "A defense agency must process classified workloads with full "
            "physical and logical control over the underlying infrastructure, "
            "but still wants the operational benefits of virtualization, "
            "self-service provisioning, and resource pooling that cloud "
            "computing offers. Which cloud deployment model BEST meets this "
            "need?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Private cloud",
                "correct": True,
                "rationale": (
                    "Correct. A private cloud is provisioned for exclusive use "
                    "by a single organization, giving it full physical and "
                    "logical control while still delivering cloud-style "
                    "virtualization, pooling, and self-service benefits."
                ),
            },
            {
                "id": "b",
                "text": "Public cloud",
                "correct": False,
                "rationale": (
                    "Incorrect. A public cloud is shared infrastructure owned "
                    "and operated by a third-party provider, which does not give "
                    "the agency the exclusive physical and logical control this "
                    "classified workload requires."
                ),
            },
            {
                "id": "c",
                "text": "Community cloud",
                "correct": False,
                "rationale": (
                    "Incorrect. A community cloud is shared among multiple "
                    "organizations with common concerns, which still does not "
                    "give any single organization exclusive control of the "
                    "infrastructure."
                ),
            },
            {
                "id": "d",
                "text": "Hybrid cloud",
                "correct": False,
                "rationale": (
                    "Incorrect. A hybrid cloud mixes private and public "
                    "components; the requirement here is exclusive control over "
                    "all infrastructure, with no described need to burst into "
                    "public cloud resources."
                ),
            },
        ],
        "explanation": (
            "Private cloud is the only deployment model that provides an "
            "organization exclusive physical and logical control of the "
            "infrastructure while still delivering the elasticity and "
            "self-service characteristics of cloud computing."
        ),
    },
    {
        "id": "nd3d-003",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Cloud architecture",
        "stem": (
            "A security review of a SaaS CRM platform finds that a customer's "
            "employees can occasionally view records belonging to a different "
            "tenant. The root cause is a flawed authorization check inside the "
            "vendor's application code, not any configuration made by either "
            "customer. Under the cloud shared responsibility model, which party "
            "is responsible for remediating this specific issue?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The SaaS provider",
                "correct": True,
                "rationale": (
                    "Correct. In the SaaS model, the provider owns and operates "
                    "the application code, including authorization logic; a "
                    "flaw in that code is squarely the provider's responsibility "
                    "to fix, not the customer's."
                ),
            },
            {
                "id": "b",
                "text": "The affected customer whose data was exposed",
                "correct": False,
                "rationale": (
                    "Incorrect. SaaS customers have no access to or control "
                    "over the vendor's application source code, so they cannot "
                    "remediate a flaw in the vendor's authorization logic."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Both parties equally, since shared responsibility always "
                    "splits duties 50/50 regardless of service model"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Shared responsibility is not a fixed 50/50 "
                    "split — the dividing line shifts with the service model, "
                    "and in SaaS the provider retains responsibility for "
                    "application-layer logic."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The infrastructure provider hosting the underlying compute "
                    "that the SaaS platform runs on"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The underlying IaaS/PaaS provider is only "
                    "responsible for the layers it manages (hardware, "
                    "hypervisor, and possibly runtime); it has no control over "
                    "the SaaS vendor's own application authorization code."
                ),
            },
        ],
        "explanation": (
            "In SaaS, the provider manages everything from the infrastructure "
            "up through the application itself, so application-layer defects "
            "such as broken tenant-isolation authorization checks are the "
            "provider's responsibility to remediate."
        ),
    },
    # ------------------------------------------------------------------ #
    # ICS/SCADA and embedded systems (3.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3d-004",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "ICS/SCADA and embedded systems",
        "stem": (
            "A data center's building automation system (BAS) controls cooling "
            "and fire suppression using BACnet, a protocol with no native "
            "authentication or encryption. The BAS vendor states that any "
            "software modification, including installing a security agent or "
            "changing the protocol, voids the equipment warranty. Which "
            "compensating control BEST reduces risk without violating the "
            "warranty terms?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Place the BAS on an isolated network segment with a "
                    "firewall enforcing strict access control lists that permit "
                    "only the specific hosts and protocols required"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Network segmentation with tightly scoped ACLs is "
                    "a compensating control that reduces exposure of the "
                    "unauthenticated, unencrypted BACnet traffic without "
                    "touching the BAS software or firmware, preserving the "
                    "warranty."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Install a host-based security agent directly on the BAS "
                    "controller to monitor for anomalous BACnet commands"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Installing any agent on the controller is a "
                    "software modification that the vendor states will void "
                    "the warranty."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Replace BACnet with a TLS-encrypted proprietary protocol "
                    "on the BAS controller"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Changing the protocol the controller uses is "
                    "exactly the kind of modification the vendor says voids the "
                    "warranty, and the embedded controller likely cannot support "
                    "TLS at all."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Disconnect the BAS from the network entirely so it cannot "
                    "be reached remotely"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Full disconnection breaks the BAS's required "
                    "monitoring and control functionality; the goal is to "
                    "reduce risk while preserving legitimate operational "
                    "connectivity, which segmentation achieves and full "
                    "isolation does not."
                ),
            },
        ],
        "explanation": (
            "When a vendor prohibits modifying legacy or embedded control "
            "systems, network-level compensating controls — segmentation and "
            "strict firewall ACLs — reduce exposure without touching the "
            "protected device itself."
        ),
    },
    # ------------------------------------------------------------------ #
    # IoT security (3.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3d-005",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "IoT security",
        "stem": (
            "A logistics company deploys thousands of battery-powered "
            "Bluetooth Low Energy (BLE) asset tags to track pallets in its "
            "warehouses. The tags lack the compute capacity for standard TLS, "
            "and firmware updates are pushed over the air (OTA) from a central "
            "gateway. A review finds that OTA update packages are not signed, "
            "so any device that can reach the gateway can push arbitrary "
            "firmware to the tags. Which control BEST mitigates this specific "
            "risk?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Require every OTA firmware package to be cryptographically "
                    "signed by the manufacturer, and have the tags verify the "
                    "signature before installing an update"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Code signing lets the low-power tags verify "
                    "firmware authenticity and integrity with a lightweight "
                    "signature check, directly preventing malicious or "
                    "unauthorized firmware from being accepted."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Move the BLE gateway onto its own network segment, "
                    "isolated from the corporate LAN"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Segmentation limits lateral movement into the "
                    "corporate network but does nothing to stop an attacker "
                    "within BLE range of the gateway from pushing unsigned "
                    "firmware to the tags themselves."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Replace all BLE asset tags with Wi-Fi-connected tags that "
                    "can support a full TLS stack"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is operationally impractical at this scale "
                    "and, more importantly, does not address the actual root "
                    "cause — unsigned firmware packages — regardless of the "
                    "radio technology used."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Disable over-the-air firmware updates entirely so tags can "
                    "never receive new firmware",
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This eliminates the attack vector but also "
                    "eliminates the ability to deploy legitimate security "
                    "patches, which is not the best trade-off when signing "
                    "achieves the same protection without losing update "
                    "capability."
                ),
            },
        ],
        "explanation": (
            "For resource-constrained IoT devices that cannot support full TLS, "
            "cryptographic code signing of firmware updates is the standard, "
            "lightweight control that preserves the ability to patch while "
            "preventing unauthorized firmware installation."
        ),
    },
    # ------------------------------------------------------------------ #
    # Microservices and containerization (3.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3d-006",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Microservices and containerization",
        "stem": (
            "A company has dozens of independently developed microservices, "
            "each implementing its own authentication, rate limiting, and "
            "request logging inconsistently. Which architecture addition would "
            "BEST centralize and standardize these north-south, cross-cutting "
            "concerns without requiring changes to each microservice's "
            "business logic?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Place an API gateway in front of the microservices to "
                    "enforce consistent authentication, rate limiting, and "
                    "logging for all inbound requests"
                ),
                "correct": True,
                "rationale": (
                    "Correct. An API gateway centralizes cross-cutting, "
                    "client-facing concerns like authentication, throttling, "
                    "and logging in one place, so individual services no "
                    "longer need to implement them inconsistently."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Require every microservice team to independently "
                    "reimplement authentication, rate limiting, and logging "
                    "using a shared internal coding standard"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This still requires touching every "
                    "microservice's code and relies on manual consistency, "
                    "which is exactly the inconsistency problem the "
                    "organization already has."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Deploy a network-layer stateful firewall between the "
                    "internet and the microservices cluster"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A network firewall filters traffic based on IP "
                    "addresses and ports; it cannot enforce application-layer "
                    "authentication, per-client rate limiting, or structured "
                    "request logging."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Increase the replica count of each microservice to "
                    "distribute request load more evenly",
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Adding replicas improves availability and "
                    "throughput but has no bearing on standardizing "
                    "authentication, rate limiting, or logging behavior."
                ),
            },
        ],
        "explanation": (
            "An API gateway is the standard architectural pattern for "
            "centralizing client-facing, cross-cutting concerns across many "
            "microservices without modifying each service's own code."
        ),
    },
    {
        "id": "nd3d-007",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Microservices and containerization",
        "stem": (
            "A platform engineering team is defining container security "
            "standards for a new microservices platform. Which THREE practices "
            "are consistent with a defense-in-depth container security "
            "architecture? (Select three.)"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Run containers as non-root users with a read-only root "
                    "filesystem wherever possible"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Non-root execution and a read-only filesystem "
                    "limit what an attacker can do even if a container is "
                    "compromised, reducing the impact of a container escape "
                    "attempt."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Scan container images for known-vulnerable packages "
                    "before they are pushed to the registry"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Scanning images before they reach the registry "
                    "prevents known-vulnerable software from ever being "
                    "deployed, addressing supply-chain risk early."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Enforce network policies that default-deny pod-to-pod "
                    "traffic unless explicitly allowed"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Default-deny network policies implement "
                    "least-privilege microsegmentation between pods, limiting "
                    "lateral movement if one container is compromised."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Grant every container the same broad service account so "
                    "any container can call any internal API if needed"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This violates least privilege — a single "
                    "compromised container would inherit access to every "
                    "internal API, dramatically increasing the blast radius of "
                    "an incident."
                ),
            },
            {
                "id": "e",
                "text": (
                    "Embed long-lived cloud credentials directly in the "
                    "container image for convenience during deployment"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Baking long-lived credentials into an image "
                    "exposes them to anyone with registry access and makes "
                    "rotation difficult; credentials should be injected at "
                    "runtime from a secrets manager instead."
                ),
            },
        ],
        "explanation": (
            "Defense-in-depth for containers combines least-privilege runtime "
            "configuration (non-root, read-only filesystem), supply-chain "
            "hygiene (image scanning), and network microsegmentation (default-"
            "deny policies) — not broad shared credentials or embedded secrets, "
            "both of which expand the blast radius of a single compromise."
        ),
    },
    # ------------------------------------------------------------------ #
    # Serverless and cloud architecture (3.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3d-008",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Serverless and cloud architecture",
        "stem": (
            "An attacker repeatedly invokes a public, unauthenticated "
            "serverless API endpoint that performs expensive image-processing "
            "computation, causing the company's cloud bill to spike "
            "dramatically overnight even though the application never went "
            "down or returned errors. Which control BEST addresses this "
            "specific risk?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Require authentication on the endpoint and configure "
                    "concurrency limits and throttling on the function"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Requiring authentication removes anonymous "
                    "access, and concurrency/throttling limits cap how much "
                    "compute (and cost) any caller can trigger — directly "
                    "addressing this 'denial of wallet' style abuse."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Increase the function's memory allocation so each "
                    "invocation completes faster"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Increasing memory typically increases cost per "
                    "invocation and does nothing to stop unauthorized, repeated "
                    "invocation of the function."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Migrate the function's code from an interpreted language "
                    "to a compiled language to reduce cold-start latency"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Cold-start latency is unrelated to unauthorized "
                    "invocation volume and would not prevent or reduce the "
                    "cost impact of repeated abusive calls."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Enable additional CloudWatch-style logging on the "
                    "function for the next billing cycle"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Additional logging provides visibility after "
                    "the fact but does not prevent the abuse or reduce costs "
                    "already being incurred."
                ),
            },
        ],
        "explanation": (
            "Unauthenticated, unthrottled serverless functions are vulnerable "
            "to economic denial-of-service ('denial of wallet') attacks; "
            "requiring authentication and enforcing concurrency/rate limits "
            "are the direct mitigations."
        ),
    },
    # ------------------------------------------------------------------ #
    # Virtualization and high availability (3.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3d-009",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Virtualization and high availability",
        "stem": (
            "An administrator live-migrates a running VM between two "
            "hypervisor hosts to perform maintenance without downtime. A "
            "security review finds that the live-migration traffic — which "
            "includes an in-memory copy of the VM's RAM — traverses the same "
            "unencrypted management network segment used for iSCSI storage "
            "traffic and is visible to other administrators on that segment. "
            "Which control BEST protects the confidentiality of this "
            "migration traffic?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Isolate live-migration traffic onto a dedicated, "
                    "encrypted network path separate from other management "
                    "and storage traffic"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A dedicated, encrypted migration network "
                    "prevents other administrators or hosts on the shared "
                    "management segment from capturing the in-memory contents "
                    "of the VM as it migrates."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Enable compression on the live-migration stream to reduce "
                    "the amount of data transferred"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Compression reduces bandwidth usage and "
                    "migration time, but a compressed stream is still readable "
                    "by anyone capturing it — it does nothing for "
                    "confidentiality."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Take a snapshot of the VM immediately before initiating "
                    "the migration"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A pre-migration snapshot supports rollback if "
                    "the migration fails; it has no effect on whether the "
                    "migration traffic itself is exposed on the network."
                ),
            },
            {
                "id": "d",
                "text": "Disable live migration entirely across the cluster",
                "correct": False,
                "rationale": (
                    "Incorrect. Disabling live migration eliminates the "
                    "exposure but also eliminates the maintenance-without-"
                    "downtime capability the organization relies on, which is "
                    "not the best trade-off when isolating and encrypting the "
                    "traffic solves the problem directly."
                ),
            },
        ],
        "explanation": (
            "Live-migration traffic contains sensitive in-memory VM state and "
            "must be isolated onto a dedicated, encrypted network path — "
            "reusing a shared, unencrypted management/storage segment exposes "
            "that memory content to anyone who can observe the segment."
        ),
    },
    # ------------------------------------------------------------------ #
    # Attack surface reduction (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3d-010",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Attack surface reduction",
        "stem": (
            "A company's public API gateway exposes 40 endpoints. A review "
            "finds that 15 of them are deprecated, undocumented, and no longer "
            "called by any current client application, yet remain active and "
            "reachable from the internet. Which action BEST reduces the "
            "attack surface here?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Decommission and remove the 15 unused endpoints",
                "correct": True,
                "rationale": (
                    "Correct. Removing code and endpoints that serve no "
                    "current business purpose eliminates that exposure "
                    "entirely, which is the definition of reducing attack "
                    "surface rather than merely mitigating risk on it."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Add detailed logging to the 15 endpoints so any use is "
                    "recorded"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Logging improves visibility after an attack "
                    "attempt but does not reduce the number of exposed, "
                    "exploitable endpoints available to an attacker."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Apply rate limiting to the 15 endpoints to slow down "
                    "automated abuse"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Rate limiting reduces the speed of abuse "
                    "against endpoints that remain reachable; it does not "
                    "reduce the attack surface, since the vulnerable, unused "
                    "code paths are still live."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Require an API key for the 15 endpoints while leaving "
                    "them otherwise unchanged"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Adding authentication reduces casual abuse "
                    "but still leaves unnecessary, unmaintained code exposed "
                    "and reachable, which is a smaller improvement than "
                    "removing it outright."
                ),
            },
        ],
        "explanation": (
            "Attack surface reduction means eliminating unnecessary exposure "
            "outright wherever possible; decommissioning unused, undocumented "
            "endpoints removes the exposure entirely rather than just adding "
            "monitoring or throttling around it."
        ),
    },
    # ------------------------------------------------------------------ #
    # Change management workflow (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3d-011",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Change management workflow",
        "stem": (
            "During a post-incident review, the security team discovers a "
            "firewall rule in production that does not match anything "
            "documented in the CMDB or any approved change record, and no one "
            "can explain when or why it was added. Which change management "
            "practice, if followed consistently, would BEST have prevented "
            "this discrepancy from going unnoticed?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Regular configuration audits that reconcile live device "
                    "configurations against the CMDB and flag undocumented "
                    "changes"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Periodic reconciliation between actual "
                    "configuration state and the documented baseline is the "
                    "specific practice that catches undocumented, out-of-"
                    "process changes like this one."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Requiring dual approval only for changes explicitly "
                    "labeled as emergency changes"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This addresses emergency-change governance but "
                    "does nothing to detect a routine, silent change that was "
                    "never submitted through the change process at all."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Storing meeting minutes from the change advisory board "
                    "(CAB) in a shared document repository"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Archiving CAB minutes documents what was "
                    "formally approved but does not detect changes made "
                    "entirely outside the formal process, which is what "
                    "happened here."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Placing infrastructure automation scripts under version "
                    "control in a source code repository"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Version control helps track changes made "
                    "through the automation tooling itself, but a rule added "
                    "manually and out-of-band, as described, would not be "
                    "captured unless configurations are actively reconciled "
                    "against the documented baseline."
                ),
            },
        ],
        "explanation": (
            "Undocumented configuration drift is caught by routine "
            "configuration audits that compare the live environment against "
            "the CMDB/change records — approval workflows and version control "
            "alone do not detect changes made entirely outside the process."
        ),
    },
    # ------------------------------------------------------------------ #
    # Failure modes (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3d-012",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Failure modes",
        "stem": (
            "An e-commerce company deploys an inline web application firewall "
            "(WAF) in front of its checkout page. During a Black Friday "
            "traffic surge, the WAF's rule-processing engine becomes "
            "overloaded. Company policy states that completing sales "
            "transactions takes priority above all else during this specific "
            "period. Which failure mode should the WAF be configured to use "
            "during an overload condition?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Fail open",
                "correct": True,
                "rationale": (
                    "Correct. Fail-open lets traffic continue passing through "
                    "an overloaded inline device rather than blocking it, "
                    "which matches the stated business priority of keeping "
                    "checkout transactions completing even at reduced security "
                    "inspection."
                ),
            },
            {
                "id": "b",
                "text": "Fail closed",
                "correct": False,
                "rationale": (
                    "Incorrect. Fail-closed would block all checkout traffic "
                    "the instant the WAF becomes overloaded, directly "
                    "contradicting the stated policy of prioritizing "
                    "transaction completion."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Automatically restart the WAF service each time it "
                    "becomes overloaded"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Restarting an overloaded service does not "
                    "resolve sustained overload during a traffic surge and "
                    "would cause a brief but real interruption, which is "
                    "inconsistent with the availability priority."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Remove the WAF from the traffic path permanently going "
                    "forward"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Permanently removing the WAF eliminates its "
                    "protection year-round to solve a temporary, seasonal "
                    "overload problem, which is a disproportionate and "
                    "unnecessary response."
                ),
            },
        ],
        "explanation": (
            "Inline security devices must be explicitly configured to fail "
            "open or fail closed based on which matters more in a given "
            "context — availability or security. Here, the stated business "
            "priority during the surge calls for fail-open."
        ),
    },
    {
        "id": "nd3d-013",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Failure modes",
        "stem": (
            "A payment microservice calls a third-party fraud-scoring API "
            "synchronously before approving each transaction. When the "
            "third-party API becomes slow and unresponsive, requests to it "
            "pile up and block threads in the payment service, eventually "
            "exhausting its thread pool and making the entire payment service "
            "unavailable — even for transactions that do not require fraud "
            "scoring. Which architecture pattern BEST prevents this cascading "
            "failure?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A circuit breaker pattern that detects the failing "
                    "dependency, stops sending it new requests after a "
                    "threshold of failures, and falls back to a default "
                    "behavior"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A circuit breaker trips after the fraud-scoring "
                    "API starts failing or timing out, stopping new calls from "
                    "consuming threads and letting the payment service "
                    "continue operating using a fallback path."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Increase the payment service's thread pool size so it can "
                    "absorb more simultaneous blocked calls"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A larger thread pool only delays the point of "
                    "exhaustion; it does not address the root cause of threads "
                    "blocking on a slow dependency and will still eventually "
                    "saturate under sustained failure."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Add a second, redundant instance of the payment service "
                    "behind a load balancer"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Every instance would independently make the "
                    "same blocking calls to the failing dependency and "
                    "eventually exhaust its own thread pool too, so simple "
                    "horizontal scaling does not solve a cascading dependency "
                    "failure."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Move the fraud-scoring API call from a synchronous call "
                    "to a nightly batch job with no other changes"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Deferring fraud scoring to a nightly batch "
                    "means transactions would be approved without any fraud "
                    "check for up to 24 hours, trading a resilience problem "
                    "for an unacceptable fraud-control gap."
                ),
            },
        ],
        "explanation": (
            "The circuit breaker pattern is the standard resilience mechanism "
            "for preventing a single slow or failing dependency from "
            "cascading into a total outage of the calling service."
        ),
    },
    # ------------------------------------------------------------------ #
    # Firewalls (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3d-014",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Firewalls",
        "stem": (
            "A firewall administrator inherits a rule base with more than "
            "2,000 rules accumulated over a decade. Many rules reference "
            "decommissioned servers and conflict with one another; some "
            "intended-allow rules never take effect because a broader deny "
            "rule positioned above them matches first. Which practice BEST "
            "addresses this problem?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Perform a periodic rule-base review to identify and "
                    "remove shadowed, orphaned, and conflicting rules, and "
                    "reorder rules from most specific to least specific"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Regular rule-base audits find rules that are "
                    "shadowed by broader rules above them, reference "
                    "decommissioned assets, or conflict with other rules — "
                    "and reordering by specificity ensures intended-allow "
                    "rules actually take effect."
                ),
            },
            {
                "id": "b",
                "text": "Append all new rules to the very end of the rule base",
                "correct": False,
                "rationale": (
                    "Incorrect. Appending to the end does not fix the existing "
                    "shadowing problem and, on a first-match firewall, new "
                    "rules placed after a broad deny may never be evaluated at "
                    "all."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Replace the existing firewall with a newer hardware model "
                    "with a faster rule-processing engine"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Faster hardware processes the same "
                    "misconfigured, conflicting rule set more quickly; it does "
                    "not fix the underlying shadowing and rule-ordering "
                    "problem."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Convert every rule to a permit-all rule to guarantee "
                    "nothing is unintentionally blocked"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This eliminates the availability symptom by "
                    "eliminating all filtering, defeating the purpose of "
                    "having a firewall and dramatically increasing risk."
                ),
            },
        ],
        "explanation": (
            "Firewall rule bases require periodic review to remove shadowed, "
            "orphaned, and conflicting rules and to keep more specific rules "
            "ordered ahead of broader ones so intended policy is actually "
            "enforced."
        ),
    },
    {
        "id": "nd3d-015",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Firewalls",
        "stem": (
            "A company migrates a three-tier web application to a public "
            "cloud IaaS environment. Instead of deploying and patching a "
            "traditional virtual firewall appliance at the edge of its "
            "virtual network, the security team wants to enforce filtering at "
            "each individual instance based on its specific role (web, app, "
            "or database), using the cloud provider's native constructs. "
            "Which control BEST meets this requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Cloud-native security groups applied per instance, with "
                    "rules scoped to each tier's specific role"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Security groups are stateful, instance-level "
                    "virtual firewalls native to the cloud platform, letting "
                    "the team enforce role-specific filtering per tier without "
                    "deploying or patching any additional appliance."
                ),
            },
            {
                "id": "b",
                "text": (
                    "A single network access control list (NACL) applied "
                    "uniformly to the entire subnet"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A single subnet-wide NACL is stateless and "
                    "applies the same rules to every instance in the subnet, "
                    "which does not provide the per-role differentiation the "
                    "team needs across web, app, and database tiers."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Deploy a dedicated third-party next-generation firewall "
                    "appliance inside the virtual network"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This directly contradicts the stated "
                    "requirement to avoid deploying and patching an "
                    "additional appliance."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Manually configure host-based iptables rules on every "
                    "instance and maintain them individually"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Manually managing per-host firewall rules "
                    "across every instance requires ongoing patching and "
                    "configuration management overhead, which is less "
                    "cloud-native and harder to maintain consistently than "
                    "provider-managed security groups."
                ),
            },
        ],
        "explanation": (
            "Cloud-native security groups provide stateful, per-instance, "
            "role-based filtering without the deployment or patching burden "
            "of a dedicated firewall appliance, matching the stated "
            "requirement precisely."
        ),
    },
    # ------------------------------------------------------------------ #
    # Network appliances (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3d-016",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network appliances",
        "stem": (
            "A company wants to hide the internal IP addresses and server "
            "software banners of its backend web servers from the internet, "
            "while also caching frequently requested static content to "
            "reduce load on those backend servers. Which network appliance "
            "BEST accomplishes both goals?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Reverse proxy",
                "correct": True,
                "rationale": (
                    "Correct. A reverse proxy sits in front of backend "
                    "servers, terminating client connections itself so "
                    "internal addresses and server banners are never directly "
                    "exposed, and it can cache static content to offload the "
                    "backend."
                ),
            },
            {
                "id": "b",
                "text": "Forward proxy",
                "correct": False,
                "rationale": (
                    "Incorrect. A forward proxy sits in front of internal "
                    "clients making outbound requests to the internet; it does "
                    "not sit in front of servers to hide or cache their "
                    "responses to inbound requests."
                ),
            },
            {
                "id": "c",
                "text": (
                    "A Layer 3 router applying access control lists to inbound "
                    "traffic"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A router with ACLs can filter traffic by IP "
                    "and port but does not terminate connections, hide server "
                    "banners, or cache content the way a reverse proxy does."
                ),
            },
            {
                "id": "d",
                "text": "Network intrusion prevention system (NIPS)",
                "correct": False,
                "rationale": (
                    "Incorrect. A NIPS inspects traffic for known attack "
                    "signatures and can block malicious traffic, but it does "
                    "not hide server identity or provide content caching."
                ),
            },
        ],
        "explanation": (
            "A reverse proxy is purpose-built to sit in front of backend "
            "servers, masking their identity from clients and optionally "
            "caching content to reduce backend load."
        ),
    },
    {
        "id": "nd3d-017",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Network appliances",
        "stem": (
            "A security team wants to feed a full copy of all traffic on a "
            "heavily saturated 10 Gbps core switch link to an IDS sensor. "
            "Using a SPAN/mirror port on the switch, they observe that during "
            "peak utilization the switch drops some mirrored packets and "
            "occasionally forwards copies with altered timing, because the "
            "switch's control-plane CPU deprioritizes mirroring under load. "
            "Which appliance BEST solves this specific problem?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A passive network TAP inserted inline on the link, "
                    "providing the IDS a dedicated, full-fidelity copy of all "
                    "traffic"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A network TAP is dedicated hardware that "
                    "duplicates every bit on the link without relying on "
                    "switch CPU resources, so it does not drop or degrade "
                    "copies under load the way a SPAN port can."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Raise the priority of the SPAN session in the switch's "
                    "configuration"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Priority settings can help somewhat, but SPAN "
                    "mirroring is fundamentally a secondary, best-effort "
                    "function competing for the same switch CPU and backplane "
                    "resources — it does not eliminate the resource "
                    "contention that causes drops under sustained heavy load."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Replace full packet mirroring with sampled NetFlow "
                    "records sent to the IDS"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. NetFlow provides flow metadata, not full "
                    "packet payloads, so the IDS would lose the deep packet "
                    "inspection capability it needs — this solves the "
                    "resource problem by discarding the very data required."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Move the IDS inline on the link instead of using mirrored "
                    "traffic"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Placing the IDS inline introduces it as a new "
                    "single point of failure and potential latency bottleneck "
                    "on a 10 Gbps core link; it does not address the described "
                    "packet-mirroring fidelity problem, and a passive TAP "
                    "solves that problem without this added risk."
                ),
            },
        ],
        "explanation": (
            "Network TAPs are purpose-built, passive hardware that copies "
            "every bit on a link without contending for switch CPU resources, "
            "making them the correct fix when SPAN/mirror ports drop or "
            "degrade copies under sustained heavy load."
        ),
    },
    # ------------------------------------------------------------------ #
    # Port security and 802.1X (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3d-018",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Port security and 802.1X",
        "stem": (
            "A conference room switchport is configured with sticky port "
            "security that allows only the first-learned MAC address, "
            "shutting the port down on a violation. An attacker unplugs the "
            "legitimate laptop, spoofs its MAC address on their own device, "
            "and successfully connects through the same port. Which control, "
            "if added, would BEST prevent this specific bypass?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Replace MAC-based port security with 802.1X port-based "
                    "authentication using EAP-TLS certificates"
                ),
                "correct": True,
                "rationale": (
                    "Correct. 802.1X with EAP-TLS authenticates the device "
                    "using a certificate the attacker's device does not "
                    "possess, unlike a MAC address, which is trivially spoofed "
                    "by an attacker who can observe it."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Lower the port security violation threshold from one MAC "
                    "address to zero"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A zero-MAC threshold would simply shut the "
                    "port down for any device, including legitimate ones; it "
                    "does not distinguish a spoofed MAC address from a "
                    "genuine one."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Increase the port security aging timer so learned MAC "
                    "addresses persist longer"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A longer aging timer does not prevent an "
                    "attacker from spoofing an already-learned MAC address; it "
                    "only changes how long that (spoofable) address remains "
                    "authorized."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Disable the switchport entirely when the room is not in "
                    "scheduled use"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This reduces the window of opportunity but "
                    "does not fix the underlying weakness that MAC-based "
                    "identity can be spoofed whenever the port is active."
                ),
            },
        ],
        "explanation": (
            "Sticky MAC-based port security identifies a device only by an "
            "easily spoofed MAC address; 802.1X certificate-based "
            "authentication verifies device identity cryptographically, which "
            "an attacker cannot forge simply by observing traffic."
        ),
    },
    # ------------------------------------------------------------------ #
    # SDN and logical segmentation (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3d-019",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SDN and logical segmentation",
        "stem": (
            "A retailer's point-of-sale terminals and corporate workstations "
            "currently share a single flat VLAN. PCI DSS requires isolating "
            "card-processing terminals from the rest of the corporate "
            "network, but the retailer cannot afford to recable hundreds of "
            "stores or deploy new physical switches. Which approach BEST "
            "achieves this isolation quickly?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Use SDN-based microsegmentation to push tag- or group-"
                    "based policies from a centralized controller that "
                    "isolate POS traffic regardless of physical topology"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Software-defined microsegmentation decouples "
                    "policy enforcement from physical cabling, letting the "
                    "retailer isolate POS terminals via centrally pushed "
                    "policy without touching physical switches at every "
                    "store."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Physically recable and install new dedicated switches "
                    "for POS terminals at each store"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is explicitly excluded by the stated "
                    "budget and logistics constraint of not being able to "
                    "recable or deploy new hardware at hundreds of stores."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Continue relying on the existing flat VLAN without "
                    "adding any additional segmentation controls"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is the current, insufficient state that "
                    "fails the PCI DSS isolation requirement and does nothing "
                    "to address it."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Disable all inter-VLAN routing across the entire network"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Blanket disabling of inter-VLAN routing would "
                    "break legitimate communication needed by other business "
                    "functions and is not a targeted isolation of POS "
                    "traffic specifically."
                ),
            },
        ],
        "explanation": (
            "SDN-based microsegmentation lets policy be enforced logically "
            "and centrally, achieving the required isolation of card-"
            "processing systems without the cost and time of re-cabling "
            "physical infrastructure at every location."
        ),
    },
    {
        "id": "nd3d-020",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "SDN and logical segmentation",
        "stem": (
            "Which THREE of the following are genuine security benefits of "
            "adopting a Software-Defined Networking (SDN) architecture, in "
            "which the control plane is decoupled from the data plane? "
            "(Select three.)"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Centralized policy management enables rapid, API-driven "
                    "reconfiguration of network segmentation without "
                    "physically touching individual devices"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Decoupling control from data plane lets policy "
                    "changes be pushed programmatically to many switches at "
                    "once, rather than requiring manual per-device "
                    "reconfiguration."
                ),
            },
            {
                "id": "b",
                "text": (
                    "A compromised host can be quarantined almost instantly "
                    "by pushing a new flow rule network-wide from the "
                    "controller"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Because the controller governs flow rules "
                    "across the fabric, an incident responder can isolate a "
                    "compromised host in seconds without visiting individual "
                    "switches."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Decoupling the control plane from the data plane "
                    "provides centralized visibility and consistent policy "
                    "enforcement across many physical switches"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A single logical control plane gives "
                    "administrators one consistent view and enforcement point "
                    "for policy across the entire fabric, instead of "
                    "reconciling separate configurations on each device."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The SDN controller becoming a single high-value target "
                    "means its compromise could affect segmentation across the "
                    "entire network"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect as a benefit — this statement is true, but it "
                    "describes a risk introduced by centralization, not a "
                    "security benefit of the architecture."
                ),
            },
            {
                "id": "e",
                "text": (
                    "Centralizing enforcement in the controller eliminates the "
                    "need for any ongoing security monitoring of the network"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. No architecture eliminates the need for "
                    "monitoring; the controller enforces policy but does not "
                    "replace detection and response capabilities."
                ),
            },
        ],
        "explanation": (
            "SDN's genuine security benefits stem from centralized, "
            "programmatic policy management and enforcement — rapid "
            "reconfiguration, fast quarantine, and consistent visibility — "
            "while controller compromise is a risk of centralization, not a "
            "benefit, and monitoring is still required."
        ),
    },
    # ------------------------------------------------------------------ #
    # Secure communication (VPN/TLS/IPSec) (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3d-021",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Secure communication (VPN/TLS/IPSec)",
        "stem": (
            "Remote employees connect to internal resources over a full-"
            "tunnel VPN. To reduce backhaul costs and latency for video-"
            "conferencing traffic, the security team is considering enabling "
            "split tunneling so only corporate-destined traffic transits the "
            "VPN and everything else goes directly to the internet. Which "
            "risk BEST justifies caution before making this change?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The user's device would have simultaneous, unmonitored "
                    "direct internet access and an active tunnel into the "
                    "corporate network, creating a potential pivot point if "
                    "the device is compromised"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Split tunneling removes corporate inspection "
                    "from the device's non-corporate traffic while the device "
                    "still has an active path into internal resources, so a "
                    "compromise via the unmonitored path can pivot straight "
                    "into the corporate network."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Split tunneling significantly increases the VPN "
                    "gateway's CPU load compared to full tunneling"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Split tunneling reduces the volume of traffic "
                    "the VPN gateway must process, since non-corporate "
                    "traffic bypasses it entirely — it does not increase "
                    "gateway load."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Split tunneling requires deploying an additional external "
                    "certificate authority"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Enabling split tunneling is a routing "
                    "configuration change on the VPN client/concentrator and "
                    "has no inherent requirement for a new certificate "
                    "authority."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Split tunneling is fundamentally incompatible with "
                    "multifactor authentication on the VPN"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. MFA authenticates the VPN session itself and "
                    "operates independently of whether all or only some "
                    "traffic is routed through that session."
                ),
            },
        ],
        "explanation": (
            "Split tunneling's main security trade-off is that it removes "
            "corporate visibility and inspection from the portion of traffic "
            "that bypasses the tunnel, while the device retains a live path "
            "into the internal network — a risk full tunneling avoids."
        ),
    },
    {
        "id": "nd3d-022",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Secure communication (VPN/TLS/IPSec)",
        "stem": (
            "A company enforces mutual TLS (mTLS) between internal "
            "microservices using client certificates issued by an internal "
            "CA. A compromised service's certificate is revoked immediately, "
            "but the compromised service continues successfully "
            "establishing new mTLS connections to other services for several "
            "hours, until each service's locally cached certificate "
            "revocation list (CRL) refreshes. Which change would BEST reduce "
            "this exposure window going forward?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Switch from periodically cached CRLs to real-time "
                    "revocation checking, such as OCSP stapling, on every "
                    "connection attempt"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Real-time revocation checking eliminates the "
                    "delay inherent in a locally cached CRL, so a revoked "
                    "certificate is rejected on the next connection attempt "
                    "rather than after a stale cache expires."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Increase the validity period of issued client "
                    "certificates to reduce reissuance overhead"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A longer certificate validity period has no "
                    "effect on how quickly revocation is recognized, and it "
                    "would actually extend how long a compromised certificate "
                    "remains generally usable if revocation checking is "
                    "delayed."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Require every service to re-authenticate its mTLS "
                    "session once every 24 hours instead of using persistent "
                    "connections"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A fixed 24-hour re-authentication window is "
                    "still far longer than the several-hour exposure the "
                    "organization is trying to eliminate, and it does not fix "
                    "the root cause of stale revocation data."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Move from certificate-based mTLS to shared pre-shared "
                    "keys between services"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Pre-shared keys are harder to rotate and "
                    "revoke individually per service than certificates, and "
                    "this change would make targeted revocation of a single "
                    "compromised service more difficult, not less."
                ),
            },
        ],
        "explanation": (
            "Cached CRLs introduce a revocation-propagation delay; real-time "
            "checks such as OCSP stapling close that exposure window by "
            "verifying certificate status on every connection rather than "
            "relying on a periodically refreshed local cache."
        ),
    },
    # ------------------------------------------------------------------ #
    # Zero Trust / SASE (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3d-023",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Zero Trust / SASE",
        "stem": (
            "A company implementing a Zero Trust architecture separates its "
            "access control system into two logical components. One "
            "component continuously evaluates trust signals — identity, "
            "device health, location, and behavior — and renders an allow/"
            "deny decision for every resource request. The other component "
            "sits directly in the communication path between the subject and "
            "the resource and only carries out whatever decision it "
            "receives. Which term describes the second component?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Policy Enforcement Point (PEP)",
                "correct": True,
                "rationale": (
                    "Correct. In the NIST Zero Trust model, the Policy "
                    "Enforcement Point sits in the data plane, directly in the "
                    "communication path, and enforces whatever decision the "
                    "Policy Decision Point renders — it does not make "
                    "decisions itself."
                ),
            },
            {
                "id": "b",
                "text": "Policy Decision Point (PDP)",
                "correct": False,
                "rationale": (
                    "Incorrect. The Policy Decision Point is the component "
                    "described first — the one that continuously evaluates "
                    "trust signals and renders the decision, not the one that "
                    "sits in the path and enforces it."
                ),
            },
            {
                "id": "c",
                "text": "Certificate authority (CA)",
                "correct": False,
                "rationale": (
                    "Incorrect. A certificate authority issues and validates "
                    "digital certificates; it plays no role in enforcing "
                    "real-time access decisions in the data path."
                ),
            },
            {
                "id": "d",
                "text": "Security information and event management (SIEM)",
                "correct": False,
                "rationale": (
                    "Incorrect. A SIEM aggregates and correlates logs for "
                    "detection and analysis; it does not sit inline enforcing "
                    "access decisions on live traffic."
                ),
            },
        ],
        "explanation": (
            "NIST's Zero Trust Architecture separates the control plane "
            "(Policy Engine and Policy Administrator, together forming the "
            "Policy Decision Point) from the data plane component that "
            "enforces decisions inline — the Policy Enforcement Point."
        ),
    },
    {
        "id": "nd3d-024",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Zero Trust / SASE",
        "stem": (
            "A company manages a patchwork of separate appliances and cloud "
            "subscriptions — a secure web gateway, a CASB, a firewall, and a "
            "VPN concentrator — each with its own management console and "
            "inconsistent policy enforcement across office and remote users. "
            "Which architecture would BEST consolidate these functions into a "
            "single, cloud-delivered, identity-aware platform with "
            "consistent policy regardless of user location?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Secure Access Service Edge (SASE)",
                "correct": True,
                "rationale": (
                    "Correct. SASE converges networking and security "
                    "functions — including SWG, CASB, firewall-as-a-service, "
                    "and ZTNA — into a single cloud-delivered platform with "
                    "unified, identity-aware policy enforcement for all "
                    "users."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Deploy an additional on-premises next-generation "
                    "firewall at every office to add another layer of "
                    "overlapping inspection"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This adds yet another separately managed "
                    "appliance rather than consolidating the existing "
                    "patchwork into one platform, worsening the inconsistency "
                    "problem."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Adopt a cloud access security broker (CASB) as the sole "
                    "replacement for all of the listed tools"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A CASB alone addresses visibility and control "
                    "over cloud application usage but does not replace "
                    "firewall, secure web gateway, or remote-access "
                    "functionality — it is too narrow in scope."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Build a full-mesh, site-to-site VPN connecting every "
                    "office directly to every other office"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A VPN mesh only addresses site-to-site "
                    "connectivity; it does not provide identity-aware, "
                    "cloud-delivered, consistently enforced security policy "
                    "for individual remote users."
                ),
            },
        ],
        "explanation": (
            "SASE is specifically designed to converge disparate networking "
            "and security point products into one cloud-delivered, identity-"
            "aware platform, delivering consistent policy enforcement "
            "regardless of where a user connects from."
        ),
    },
    # ------------------------------------------------------------------ #
    # Data classification (3.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3d-025",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Data classification",
        "stem": (
            "A law firm classifies documents using the labels Public, "
            "Internal, Confidential, and Privileged. Draft settlement "
            "negotiation documents covered by attorney-client privilege — "
            "whose disclosure outside the case team could waive that "
            "privilege and harm the client's legal position — are currently "
            "stored on a shared drive accessible to all paralegals firm-"
            "wide. Which classification level should apply, and what access "
            "control does it require?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Privileged, restricted to only the specific attorneys "
                    "and paralegals assigned to that case, with access "
                    "logging"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Documents whose exposure could waive legal "
                    "privilege and directly harm the client warrant the "
                    "firm's highest classification level and access limited "
                    "strictly to the assigned case team, not all paralegals "
                    "firm-wide."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Confidential, since that label is sufficient for any "
                    "sensitive legal document regardless of privilege"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Confidential is a lower tier than Privileged "
                    "in this firm's scheme and does not reflect the "
                    "heightened, case-team-only access control required when "
                    "privilege-waiver risk exists."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Internal, since the documents are only ever meant to be "
                    "seen within the firm"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Internal-level access, as currently applied "
                    "(all paralegals firm-wide), is far too broad for "
                    "documents that carry privilege-waiver and client-harm "
                    "risk if exposed beyond the assigned case team."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Public, since the documents will eventually be "
                    "referenced during litigation"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Draft settlement negotiation documents are "
                    "not intended for open disclosure and are the opposite of "
                    "Public classification."
                ),
            },
        ],
        "explanation": (
            "Classification levels should map directly to the harm that "
            "disclosure would cause; documents whose exposure could waive "
            "attorney-client privilege and damage a client's position "
            "warrant the strictest label and tightest, need-to-know access."
        ),
    },
    # ------------------------------------------------------------------ #
    # Data protection methods (3.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3d-026",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Data protection methods",
        "stem": (
            "A financial analytics company processes highly sensitive "
            "trading data in memory on multi-tenant public cloud VMs. The "
            "data is already encrypted at rest and encrypted in transit, but "
            "the company is concerned that a malicious cloud administrator "
            "or a co-located tenant exploiting a hypervisor vulnerability "
            "could read the sensitive data while it is actively being "
            "processed in RAM. Which technology BEST addresses protecting "
            "data specifically while it is in use?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Confidential computing using a hardware-based trusted "
                    "execution environment (TEE) / secure enclave"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Confidential computing processes data inside a "
                    "hardware-isolated enclave that encrypts memory contents "
                    "even from the hypervisor and host administrator, "
                    "directly addressing protection of data in use."
                ),
            },
            {
                "id": "b",
                "text": "Full-disk encryption on the underlying VM storage",
                "correct": False,
                "rationale": (
                    "Incorrect. Full-disk encryption protects data at rest on "
                    "the storage medium; it provides no protection once data "
                    "is decrypted into memory for active processing."
                ),
            },
            {
                "id": "c",
                "text": "TLS 1.3 for all API calls to the analytics service",
                "correct": False,
                "rationale": (
                    "Incorrect. TLS protects data in transit between systems; "
                    "it has already been implemented per the scenario and "
                    "does nothing to protect data once it is being processed "
                    "in memory on a host."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Database-level column encryption applied to the sensitive "
                    "trading fields"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Column-level encryption protects data at rest "
                    "in the database, but the values are decrypted into "
                    "plaintext in memory during active processing, which is "
                    "exactly the exposure window in question."
                ),
            },
        ],
        "explanation": (
            "Data at rest and in transit were already addressed in this "
            "scenario; confidential computing with hardware-based trusted "
            "execution environments is the technology specifically designed "
            "to protect data while it is actively being processed in "
            "memory."
        ),
    },
    {
        "id": "nd3d-027",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Data protection methods",
        "stem": (
            "Which TWO of the following are legitimate techniques for "
            "protecting data specifically while it is in use (actively being "
            "processed in memory), as opposed to at rest or in transit? "
            "(Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Confidential computing using hardware-based secure "
                    "enclaves"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Secure enclaves keep data encrypted in memory "
                    "and isolated from the host OS and hypervisor during "
                    "active processing, directly protecting data in use."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Homomorphic encryption, which allows computation to be "
                    "performed directly on ciphertext without ever decrypting "
                    "it"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Homomorphic encryption lets a system compute on "
                    "encrypted data and produce an encrypted result, meaning "
                    "the plaintext is never exposed even during processing."
                ),
            },
            {
                "id": "c",
                "text": "TLS 1.3 applied to all internal and external API traffic",
                "correct": False,
                "rationale": (
                    "Incorrect. TLS protects data while it is in transit "
                    "between systems, not while it is being processed in "
                    "memory on a host."
                ),
            },
            {
                "id": "d",
                "text": "AES-256 full-disk encryption on all storage volumes",
                "correct": False,
                "rationale": (
                    "Incorrect. Full-disk encryption protects data at rest on "
                    "storage media; it provides no protection once the data "
                    "is decrypted into memory for processing."
                ),
            },
            {
                "id": "e",
                "text": (
                    "Tokenization that replaces sensitive values with a "
                    "non-sensitive token before the data is stored in the "
                    "database"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Tokenization protects the stored (at-rest) "
                    "representation of data; the real value must still be "
                    "used in plaintext during active computation unless "
                    "combined with an in-use protection technique."
                ),
            },
        ],
        "explanation": (
            "Data-in-use protection is a distinct category from at-rest and "
            "in-transit protections; confidential computing (secure "
            "enclaves) and homomorphic encryption are the two techniques "
            "designed specifically to protect data during active "
            "processing."
        ),
    },
    # ------------------------------------------------------------------ #
    # Data states (3.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3d-028",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Data states",
        "stem": (
            "A company encrypts its database files at rest using full-disk "
            "encryption and encrypts all customer-facing web traffic using "
            "TLS. During its nightly ETL process, a batch job pulls customer "
            "records from the production database and writes them, "
            "completely unencrypted, across an internal network segment to a "
            "reporting data warehouse. A packet capture on that internal "
            "segment would reveal customer PII in cleartext. Which data "
            "state is currently NOT being protected in this workflow?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Data in transit",
                "correct": True,
                "rationale": (
                    "Correct. The unencrypted internal transfer of records "
                    "from the production database to the reporting warehouse "
                    "is data moving across a network — data in transit — and "
                    "it is the one state left unprotected in this workflow."
                ),
            },
            {
                "id": "b",
                "text": "Data at rest",
                "correct": False,
                "rationale": (
                    "Incorrect. Data at rest is already protected in this "
                    "scenario via full-disk encryption on the database files; "
                    "that is not the gap being described."
                ),
            },
            {
                "id": "c",
                "text": "Data in use",
                "correct": False,
                "rationale": (
                    "Incorrect. Data in use refers to data actively being "
                    "processed in memory; a packet capture on the network "
                    "segment would not reveal that state, only data actively "
                    "moving across the wire."
                ),
            },
            {
                "id": "d",
                "text": "Data at destination",
                "correct": False,
                "rationale": (
                    "Incorrect. This is not one of the three recognized data "
                    "states (at rest, in transit, and in use)."
                ),
            },
        ],
        "explanation": (
            "The three recognized data states are at rest, in transit, and "
            "in use. Here, at-rest storage and external transit are already "
            "protected, but the internal ETL transfer moves PII across the "
            "network in cleartext — an unprotected data-in-transit gap."
        ),
    },
    # ------------------------------------------------------------------ #
    # Tokenization and masking (3.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3d-029",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Tokenization and masking",
        "stem": (
            "A retailer wants its analytics team to run aggregate queries "
            "and joins across a de-identified copy of the customer database "
            "(for example, grouping orders by customer over time) without "
            "ever exposing real customer names or emails. The same customer "
            "must map to the exact same de-identified value in every table "
            "for the necessary joins to work correctly. Which approach BEST "
            "meets this requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Consistent, deterministic tokenization that always maps "
                    "a given customer identifier to the same token everywhere "
                    "it appears"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Deterministic tokenization guarantees the same "
                    "input always produces the same token across every table, "
                    "which preserves the ability to join records on the "
                    "de-identified value while never exposing the real "
                    "identifier."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Salted hashing of the customer identifier, using a newly "
                    "generated random salt independently in each table"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A different random salt per table produces a "
                    "different hash output for the same customer in each "
                    "table, breaking the ability to join records across "
                    "tables."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Static data masking that generates a new random masked "
                    "value each time a query touches the table"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Generating a new random value on every access "
                    "means the same customer would appear as a different "
                    "value each time, making cross-table joins on that value "
                    "impossible."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Format-preserving encryption without a fixed key, so "
                    "ciphertext output changes each time the same value is "
                    "encrypted"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Without a fixed key, encrypting the same "
                    "customer identifier produces different ciphertext each "
                    "time, which — like the other distractors — breaks the "
                    "consistency needed for joins."
                ),
            },
        ],
        "explanation": (
            "Analytics use cases that need to join de-identified records "
            "across tables require a deterministic mapping — the same "
            "underlying value must always produce the same de-identified "
            "value — which only consistent, deterministic tokenization "
            "reliably provides."
        ),
    },
    {
        "id": "nd3d-030",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Tokenization and masking",
        "stem": (
            "A retailer's tokenization system issues the same token for a "
            "given card number to every internal system that touches it, "
            "including the loyalty rewards platform, the returns-processing "
            "system, and the core payment settlement system. An audit finds "
            "that the loyalty rewards platform — which only ever needs a "
            "stable reference value and has no legitimate need for the real "
            "card number — is able to call the token vault's detokenization "
            "API and retrieve the actual card number. Which change would "
            "BEST address this finding?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Restrict detokenization API access to only the specific "
                    "systems with a genuine business need to recover the real "
                    "card number, such as the settlement system"
                ),
                "correct": True,
                "rationale": (
                    "Correct. The actual gap is that detokenization "
                    "capability is not scoped by business need — restricting "
                    "which systems can call the detokenization API enforces "
                    "least privilege directly on the finding described."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Replace tokenization with masking across all systems, "
                    "including the payment settlement system"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Masking would prevent the settlement system "
                    "from recovering the real card number it legitimately "
                    "needs to complete transactions, breaking a required "
                    "business function."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Rotate the token vault's encryption key on a recurring "
                    "schedule"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Key rotation is good hygiene but does not "
                    "address the access-control gap that lets an "
                    "unauthorized system call the detokenization API in the "
                    "first place."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Issue a different token for the same card number to each "
                    "system that touches it"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Using per-system tokens can reduce blast "
                    "radius in some designs, but it does not by itself "
                    "restrict which systems are authorized to call the "
                    "detokenization API — the loyalty platform could still "
                    "detokenize its own token if that access is left "
                    "unrestricted."
                ),
            },
        ],
        "explanation": (
            "Tokenization systems must scope detokenization rights to only "
            "the systems that genuinely need the original sensitive value; "
            "granting universal detokenization access, as found here, "
            "violates least privilege regardless of how the tokens "
            "themselves are generated."
        ),
    },
    # ------------------------------------------------------------------ #
    # Backups and replication (3.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3d-031",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Backups and replication",
        "stem": (
            "A company performs a full backup every Sunday night and "
            "incremental backups every other night, with each incremental "
            "capturing only data changed since the previous backup (full or "
            "incremental). On Friday morning, administrators discover that "
            "Wednesday night's incremental backup file is corrupted and "
            "unreadable. Which statement is accurate regarding a restore "
            "attempted that day?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Only data through Tuesday can be restored, because "
                    "Thursday's incremental depends on Wednesday's now-"
                    "unreadable incremental in the restore chain"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Incremental backups form a dependency chain "
                    "from the last full backup forward; a corrupted link in "
                    "that chain makes every subsequent incremental unusable, "
                    "limiting the restore to the last good point before the "
                    "corruption."
                ),
            },
            {
                "id": "b",
                "text": (
                    "All data through Thursday night can still be restored "
                    "normally, because each incremental backup is fully "
                    "independent of the others"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Incremental backups are not independent of "
                    "one another — each depends on all prior incrementals "
                    "since the last full backup, which is exactly why "
                    "Wednesday's corruption breaks the chain."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Only Wednesday's data is unrecoverable; every other "
                    "day's data remains fully restorable"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This ignores the chain dependency of "
                    "incremental backups — Thursday's incremental cannot be "
                    "applied without Wednesday's, so Thursday's data is lost "
                    "as well, not just Wednesday's."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Switching to a differential backup scheme going forward "
                    "would have made no difference to this specific risk, "
                    "since differential backups depend on all previous "
                    "differentials just like incrementals"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This mischaracterizes differential backups — "
                    "each differential depends only on the last full backup, "
                    "not on other differentials, so a single corrupted "
                    "differential would not break subsequent restores the "
                    "way a corrupted incremental does."
                ),
            },
        ],
        "explanation": (
            "Incremental backups depend on an unbroken chain back to the "
            "last full backup; a single corrupted incremental breaks every "
            "later incremental in that chain, whereas differential backups "
            "each depend only on the last full backup and are more resilient "
            "to a single corrupted file."
        ),
    },
    {
        "id": "nd3d-032",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Backups and replication",
        "stem": (
            "A company encrypts all backup media using AES-256 with a "
            "unique key generated per backup job. During a disaster recovery "
            "test, administrators retrieve the backup tapes from the "
            "offsite vendor but discover the encryption keys were stored "
            "only on the primary production key management server, which "
            "was destroyed in the same disaster that necessitated the "
            "restore. Which practice would BEST have prevented this "
            "outcome?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Escrow and replicate backup encryption keys to a "
                    "separate, geographically distant location independent "
                    "of the primary production environment"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Backup encryption keys must be recoverable "
                    "independently of the primary environment; escrowing them "
                    "to a distant, separate location ensures they survive a "
                    "disaster that destroys the primary site."
                ),
            },
            {
                "id": "b",
                "text": "Increase the frequency of backup jobs from nightly to hourly",
                "correct": False,
                "rationale": (
                    "Incorrect. More frequent backups reduce data loss "
                    "(RPO) but do nothing to address the fact that the "
                    "encryption keys themselves were lost along with the "
                    "primary site."
                ),
            },
            {
                "id": "c",
                "text": "Use a longer AES key length for backup encryption",
                "correct": False,
                "rationale": (
                    "Incorrect. Key length affects cryptographic strength, "
                    "not key availability; a longer key would have been "
                    "equally unrecoverable if only stored on the destroyed "
                    "server."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Store the encryption keys on the same backup tapes as "
                    "the data they protect, for convenience"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Storing keys alongside the data they encrypt "
                    "defeats the purpose of encryption entirely — anyone who "
                    "obtains the tapes would also obtain the keys needed to "
                    "decrypt them."
                ),
            },
        ],
        "explanation": (
            "Encrypted backups are only as recoverable as their encryption "
            "keys; key management for backups must include independent, "
            "geographically separate escrow so a disaster at the primary "
            "site does not also destroy the ability to decrypt the backups "
            "it necessitated restoring."
        ),
    },
    # ------------------------------------------------------------------ #
    # High availability (3.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3d-033",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "High availability",
        "stem": (
            "A company's HA design uses two identical application servers "
            "behind a load balancer configured in active-passive mode: the "
            "passive node stays fully provisioned and powered on, mirroring "
            "configuration, but receives no live traffic unless the active "
            "node fails. Which BEST describes the primary trade-off of this "
            "design compared to an active-active design?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Active-passive wastes the passive node's capacity during "
                    "normal operation in exchange for simpler, conflict-free "
                    "failover, while active-active uses all capacity but "
                    "requires more complex state synchronization"
                ),
                "correct": True,
                "rationale": (
                    "Correct. This is the fundamental trade-off between the "
                    "two designs: active-passive sacrifices utilization for "
                    "simplicity, while active-active improves utilization at "
                    "the cost of needing to keep concurrently serving nodes "
                    "synchronized."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Active-passive always provides a lower recovery time "
                    "objective (RTO) than active-active"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Active-active typically provides a lower RTO "
                    "than active-passive, since traffic is already being "
                    "served by multiple nodes and does not need to wait for a "
                    "passive node to be brought fully online."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Active-passive designs never require the passive node to "
                    "be kept current with configuration changes made to the "
                    "active node"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The passive node must still be kept in sync "
                    "with the active node's configuration to fail over "
                    "correctly; neglecting this is a common cause of failed "
                    "failovers."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Active-active designs cannot serve traffic to more than "
                    "one client at a time"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Active-active designs are specifically built "
                    "to serve multiple clients concurrently across all active "
                    "nodes; this statement misrepresents the model entirely."
                ),
            },
        ],
        "explanation": (
            "Active-passive and active-active represent a classic "
            "utilization-versus-complexity trade-off in HA design: "
            "active-passive is simpler but leaves capacity idle, while "
            "active-active uses all capacity but requires synchronizing "
            "state across concurrently serving nodes."
        ),
    },
    {
        "id": "nd3d-034",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "High availability",
        "stem": (
            "A security architect reviews a three-tier application and "
            "identifies these components: a single load balancer appliance, "
            "an active-active pair of web servers, a single database server "
            "with no replica, and a DNS record pointing to one static, "
            "highly available IP address managed by the cloud provider. "
            "Which TWO of these represent single points of failure that "
            "should be remediated first? (Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "The single load balancer appliance",
                "correct": True,
                "rationale": (
                    "Correct. With only one load balancer, its failure takes "
                    "down access to both web servers even though the web "
                    "tier itself is redundant, making it a genuine single "
                    "point of failure."
                ),
            },
            {
                "id": "b",
                "text": "The single database server with no replica",
                "correct": True,
                "rationale": (
                    "Correct. A database with no replica means its failure "
                    "causes a complete outage of data access for the "
                    "application, with no automatic failover target "
                    "available."
                ),
            },
            {
                "id": "c",
                "text": "The active-active pair of web servers",
                "correct": False,
                "rationale": (
                    "Incorrect. An active-active pair is, by definition, "
                    "already redundant — the loss of one server still leaves "
                    "the other serving traffic, so it is not a single point "
                    "of failure."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The DNS record pointing to a single, cloud-provider-"
                    "managed highly available IP address"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. As described, the underlying IP address is "
                    "itself managed as highly available by the cloud "
                    "provider, so this does not represent an unaddressed "
                    "single point of failure the way the unreplicated load "
                    "balancer and database do."
                ),
            },
        ],
        "explanation": (
            "A single point of failure is any component whose failure alone "
            "takes down the system, despite redundancy elsewhere; here, the "
            "sole load balancer and the sole database server both fit that "
            "definition, while the redundant web tier and the already-"
            "highly-available DNS target do not."
        ),
    },
    # ------------------------------------------------------------------ #
    # Multi-cloud and platform diversity (3.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3d-035",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Multi-cloud and platform diversity",
        "stem": (
            "A security architect notes that every layer of the company's "
            "defenses — perimeter firewall, endpoint protection, and email "
            "security gateway — is built entirely on products from a single "
            "vendor. A zero-day vulnerability in that vendor's core "
            "detection engine could simultaneously blind every layer of "
            "defense at once. Which principle BEST addresses this risk?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Platform diversity — deploying complementary security "
                    "controls from different vendors at different layers to "
                    "avoid a single-vendor security monoculture"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Using different vendors at different layers "
                    "means a single vendor's zero-day cannot simultaneously "
                    "blind every layer of defense, directly addressing the "
                    "risk described."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Standardizing entirely on one vendor across every layer "
                    "to simplify management and support contracts"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This describes the current state that "
                    "created the risk in the first place — a single-vendor "
                    "monoculture — rather than a mitigation for it."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Increasing the frequency of signature updates from the "
                    "existing vendor"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. More frequent updates from the same vendor "
                    "do not address the risk that a flaw in that vendor's "
                    "core detection engine affects every layer built on it "
                    "simultaneously."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Negotiating a stricter service level agreement (SLA) "
                    "with the existing vendor for faster patch delivery"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A faster patch SLA reduces exposure time but "
                    "does not eliminate the underlying architectural risk "
                    "that one vendor's failure can compromise every defensive "
                    "layer at once."
                ),
            },
        ],
        "explanation": (
            "Relying on a single vendor across every defensive layer "
            "creates a security monoculture; deliberate platform diversity "
            "ensures a single vendor's flaw cannot simultaneously compromise "
            "the entire defense-in-depth stack."
        ),
    },
    # ------------------------------------------------------------------ #
    # Power resilience (3.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3d-036",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Power resilience",
        "stem": (
            "A data center's diesel generator can run for 8 hours on its "
            "onboard fuel tank, but planners are concerned that a regional "
            "disaster could cause a utility outage lasting several days. "
            "Which arrangement BEST ensures continuous power beyond the "
            "onboard tank's runtime?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A fuel resupply contract with a vendor that guarantees "
                    "priority emergency delivery to extend generator runtime "
                    "indefinitely"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A guaranteed-priority fuel resupply contract "
                    "directly addresses the multi-day runtime gap, since the "
                    "generator can keep running as long as fuel keeps being "
                    "delivered."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Adding a second uninterruptible power supply (UPS) unit "
                    "identical to the existing one"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A UPS bridges only the brief gap until the "
                    "generator starts; it has no meaningful battery capacity "
                    "for sustaining power over days and does not solve a "
                    "multi-day fuel shortfall."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Installing a larger automatic transfer switch (ATS) to "
                    "reduce the transfer time between utility and generator "
                    "power"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The ATS transfer speed affects only the "
                    "momentary switchover between power sources; it does not "
                    "extend how long the generator can run once its onboard "
                    "fuel is depleted."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Scheduling more frequent generator load-bank testing"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Load-bank testing verifies the generator "
                    "performs reliably under load; it validates readiness but "
                    "does not increase the amount of fuel available during an "
                    "extended outage."
                ),
            },
        ],
        "explanation": (
            "When onboard generator fuel capacity is shorter than a "
            "plausible outage duration, the gap is closed through logistics "
            "— a guaranteed fuel resupply arrangement — not through UPS "
            "capacity, transfer switch speed, or testing frequency, none of "
            "which extend total runtime."
        ),
    },
    # ------------------------------------------------------------------ #
    # Recovery sites (3.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3d-037",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Recovery sites",
        "stem": (
            "A small business has a recovery time objective (RTO) of two "
            "weeks and a very constrained budget. It contracts for a "
            "facility that provides only floor space, power, and "
            "connectivity, with no pre-installed servers and no continuously "
            "replicated data — hardware must be procured and data restored "
            "from offsite backups only after a disaster is formally "
            "declared. Which type of recovery site is this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Cold site",
                "correct": True,
                "rationale": (
                    "Correct. A cold site provides only the basic facility — "
                    "space, power, and connectivity — with no pre-installed "
                    "equipment or replicated data, matching both the long "
                    "RTO and the tight budget described."
                ),
            },
            {
                "id": "b",
                "text": "Warm site",
                "correct": False,
                "rationale": (
                    "Incorrect. A warm site includes some pre-installed "
                    "hardware and periodically updated data, which would "
                    "shorten the RTO and increase the cost well beyond what "
                    "is described here."
                ),
            },
            {
                "id": "c",
                "text": "Hot site",
                "correct": False,
                "rationale": (
                    "Incorrect. A hot site is a fully mirrored, continuously "
                    "synchronized duplicate environment offering a near-zero "
                    "RTO, requiring far more budget than this small business "
                    "has available."
                ),
            },
            {
                "id": "d",
                "text": "Reciprocal site",
                "correct": False,
                "rationale": (
                    "Incorrect. A reciprocal arrangement is a mutual-aid "
                    "agreement with another organization to use each other's "
                    "facilities, not a contracted facility providing only "
                    "space, power, and connectivity as described here."
                ),
            },
        ],
        "explanation": (
            "Cold, warm, and hot sites represent increasing cost and "
            "decreasing RTO; a facility offering only bare space, power, and "
            "connectivity — with hardware procurement and data restoration "
            "happening after disaster declaration — is a cold site."
        ),
    },
    {
        "id": "nd3d-038",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Recovery sites",
        "stem": (
            "A German company selects a disaster recovery site operated by a "
            "cloud provider in the United States specifically to ensure the "
            "DR site is geographically far from its primary Frankfurt data "
            "center. Legal review flags that failing over to this site would "
            "move EU citizens' personal data outside the European Economic "
            "Area, triggering GDPR cross-border transfer restrictions. Which "
            "change BEST resolves this specific conflict while still "
            "providing adequate geographic separation from the primary "
            "site?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Select a DR site in a different EU/EEA member state that "
                    "is still geographically distant from Frankfurt"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Choosing a site in another EU/EEA country "
                    "preserves meaningful geographic separation from "
                    "Frankfurt while keeping personal data within the EEA, "
                    "resolving the GDPR cross-border transfer conflict "
                    "directly."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Encrypt the data before replicating it to the U.S. site, "
                    "with no other changes to the arrangement"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Encryption alone does not satisfy GDPR's "
                    "restrictions on where and under what legal safeguards "
                    "personal data may be processed outside the EEA; it does "
                    "not resolve the underlying jurisdictional conflict by "
                    "itself."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Obtain individual consent from each affected EU citizen "
                    "for the cross-border transfer to the U.S. site"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Collecting individual consent from every "
                    "affected data subject at disaster recovery scale is "
                    "impractical and is not a reliable or scalable legal "
                    "basis for this kind of large-scale operational data "
                    "transfer."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Rely on the cloud provider's general terms of service "
                    "stating that it takes data security seriously"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Generic marketing language in a terms-of-"
                    "service document provides no specific legal safeguard "
                    "or basis for a GDPR-compliant cross-border transfer of "
                    "personal data."
                ),
            },
        ],
        "explanation": (
            "Geographic separation requirements for DR sites must be "
            "balanced against data residency and cross-border transfer "
            "regulations; choosing a distant site within the same "
            "regulatory region satisfies both concerns at once."
        ),
    },
    # ------------------------------------------------------------------ #
    # Multi-cloud and platform diversity / High availability continued —
    # Resilience testing (3.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3d-039",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Resilience testing",
        "stem": (
            "A DR team wants to validate its ransomware runbook by having "
            "each responder actually perform their assigned technical "
            "actions — running real detection queries, actually isolating a "
            "subset of lab systems from the network, and restoring data from "
            "backup onto isolated hardware — but explicitly without touching "
            "or disrupting any production system. Which type of resilience "
            "test does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A functional exercise (simulation test) that exercises "
                    "real hands-on actions in an isolated environment without "
                    "affecting production"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A functional exercise goes beyond discussion "
                    "and has responders actually carry out their technical "
                    "actions, but does so in an isolated or simulated "
                    "environment specifically to avoid touching production "
                    "— exactly as described."
                ),
            },
            {
                "id": "b",
                "text": (
                    "A tabletop exercise where stakeholders discuss their "
                    "roles verbally without performing any technical actions"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A tabletop exercise is discussion-only, with "
                    "no hands-on technical actions performed, which "
                    "contradicts the scenario's description of responders "
                    "actually running queries and restoring data."
                ),
            },
            {
                "id": "c",
                "text": (
                    "A full-scale live test that actually executes the "
                    "runbook against production systems"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario explicitly avoids touching or "
                    "disrupting production systems, which is the defining "
                    "characteristic of a full-scale/live production test — "
                    "the opposite of what is described here."
                ),
            },
            {
                "id": "d",
                "text": (
                    "A parallel test in which the DR site processes a live "
                    "copy of production data concurrently with the primary "
                    "site"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A parallel test specifically involves "
                    "processing live production data concurrently at the DR "
                    "site to validate it under real load, which does not "
                    "match this scenario's isolated lab-only approach."
                ),
            },
        ],
        "explanation": (
            "Resilience/DR tests range from discussion-only tabletop "
            "exercises, to hands-on functional exercises performed in an "
            "isolated environment, to parallel tests using live data "
            "alongside production, to full-scale tests that actually "
            "disrupt production — this scenario's isolated, hands-on "
            "approach is a functional exercise."
        ),
    },
    # ------------------------------------------------------------------ #
    # Third-party agreement types (3.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3d-040",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Third-party agreement types",
        "stem": (
            "Two companies in early, exploratory talks about a potential "
            "joint venture want to document their mutual intent to "
            "collaborate and each party's general expectations, before any "
            "legally binding financial commitments or detailed terms are "
            "finalized. Which document BEST fits this stage of the "
            "relationship?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Memorandum of Understanding (MOU)",
                "correct": True,
                "rationale": (
                    "Correct. An MOU is a non-binding document expressing "
                    "mutual intent and general expectations between parties, "
                    "which is exactly appropriate for early-stage, "
                    "exploratory discussions before binding terms are set."
                ),
            },
            {
                "id": "b",
                "text": "Service level agreement (SLA)",
                "correct": False,
                "rationale": (
                    "Incorrect. An SLA defines specific, measurable "
                    "performance commitments such as uptime and response "
                    "times — far too detailed and binding for an early "
                    "exploratory-stage relationship with no finalized terms."
                ),
            },
            {
                "id": "c",
                "text": "Business partnership agreement (BPA)",
                "correct": False,
                "rationale": (
                    "Incorrect. A BPA is a legally binding document defining "
                    "formal partnership terms such as ownership and financial "
                    "responsibilities, which is premature at this early, "
                    "non-binding exploratory stage."
                ),
            },
            {
                "id": "d",
                "text": "Master service agreement (MSA)",
                "correct": False,
                "rationale": (
                    "Incorrect. An MSA establishes the ongoing binding terms "
                    "governing future work between parties, which does not "
                    "match a relationship still in exploratory, non-binding "
                    "talks."
                ),
            },
        ],
        "explanation": (
            "A Memorandum of Understanding is the standard non-binding "
            "document used to record mutual intent and general expectations "
            "during early-stage discussions, before parties commit to the "
            "binding, detailed terms found in agreements like an SLA, BPA, "
            "or MSA."
        ),
    },
]

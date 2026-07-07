"""CompTIA Security+ (SY0-701) practice question bank — Domain 3, file B.

40 scenario-driven questions (36 multiple_choice + 4 multiple_response)
covering every study_topic label listed under domain 3 in
``_topic_labels.json``. Scenarios are distinct from d3a.py.
"""

from __future__ import annotations

QUESTIONS = [
    # ------------------------------------------------------------------ #
    # Architecture trade-offs (3.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3b-001",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Architecture trade-offs",
        "stem": (
            "A fintech firm is redesigning a monolithic trading platform. The "
            "architecture team proposes splitting it into loosely coupled "
            "microservices communicating over the network instead of in-process "
            "function calls. Which trade-off BEST justifies this redesign?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Decomposing the platform trades increased network hops and "
                    "inter-service latency for the ability to contain a "
                    "compromise or failure to a single service and patch or "
                    "scale that service independently of the rest"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Microservices isolate blast radius and allow "
                    "independent patching/scaling, at the cost of added "
                    "network complexity and latency between services — the "
                    "core trade-off this redesign accepts."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Keeping the platform as a single monolith reduces the "
                    "number of network hops between components, which is why "
                    "the redesign should proceed"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This describes an advantage of staying "
                    "monolithic, not a reason to move to microservices — it "
                    "argues against the proposed redesign, not for it."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Splitting the monolith into many microservices reduces "
                    "the total number of network-facing interfaces that must "
                    "be defended"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The opposite is true: each new microservice "
                    "typically exposes its own network-facing interface, "
                    "increasing rather than decreasing the total attack "
                    "surface that must be defended."
                ),
            },
            {
                "id": "d",
                "text": (
                    "A monolithic deployment lets individual business "
                    "functions be updated and released independently without "
                    "coordinated, all-at-once releases"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is backwards — independent, uncoordinated "
                    "releases per function are a benefit of microservices, "
                    "while a monolith typically requires a single coordinated "
                    "build and release of the entire application."
                ),
            },
        ],
        "explanation": (
            "Moving from a monolith to microservices is a classic isolation-"
            "versus-complexity trade-off: it contains the blast radius of a "
            "single compromised or failed component and allows independent "
            "patch/scale cycles, at the cost of added network hops, latency, "
            "and a larger set of network-facing interfaces."
        ),
    },
    # ------------------------------------------------------------------ #
    # Cloud architecture (3.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3b-002",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Cloud architecture",
        "stem": (
            "Several regional hospital systems want to jointly fund and share "
            "a cloud research-data platform. Access must be limited to member "
            "hospitals bound by the same HIPAA-aligned governance policy, and "
            "the platform must never be exposed to the general public or to "
            "organizations outside the consortium. Which cloud deployment "
            "model BEST fits this requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Community cloud",
                "correct": True,
                "rationale": (
                    "Correct. A community cloud is shared by a defined group "
                    "of organizations with common regulatory and governance "
                    "requirements, exactly matching the hospital consortium's "
                    "need for a shared but non-public, HIPAA-aligned platform."
                ),
            },
            {
                "id": "b",
                "text": "Public cloud",
                "correct": False,
                "rationale": (
                    "Incorrect. A public cloud is available to any customer "
                    "of the provider, directly violating the requirement that "
                    "the platform never be exposed outside the consortium."
                ),
            },
            {
                "id": "c",
                "text": "Private cloud dedicated to a single hospital",
                "correct": False,
                "rationale": (
                    "Incorrect. A single-tenant private cloud would not allow "
                    "the multiple hospital systems to jointly share the "
                    "platform as described."
                ),
            },
            {
                "id": "d",
                "text": "Hybrid cloud connecting one hospital's on-premises data center to a public cloud",
                "correct": False,
                "rationale": (
                    "Incorrect. Hybrid describes connecting private and public "
                    "environments for one organization; it does not describe "
                    "a platform jointly shared and governed by multiple "
                    "independent hospital systems."
                ),
            },
        ],
        "explanation": (
            "Community cloud is the deployment model purpose-built for a "
            "defined set of organizations with shared compliance and "
            "governance needs to jointly use infrastructure without opening "
            "it to the public or connecting it to any single tenant's private "
            "environment."
        ),
    },
    {
        "id": "nd3b-003",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Cloud architecture",
        "stem": (
            "A security team learns employees have been uploading sensitive "
            "spreadsheets to a personal, unsanctioned file-sharing SaaS "
            "application that IT never approved. The team needs visibility "
            "into which cloud applications — sanctioned and unsanctioned — are "
            "in use across the organization and wants to enforce data loss "
            "prevention policies uniformly across all of them. Which tool BEST "
            "meets this need?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Cloud access security broker (CASB)",
                "correct": True,
                "rationale": (
                    "Correct. A CASB sits between users and cloud services to "
                    "discover shadow IT usage and enforce consistent security "
                    "and DLP policy across both sanctioned and unsanctioned "
                    "SaaS applications."
                ),
            },
            {
                "id": "b",
                "text": "Secure web gateway (SWG) enforcing only URL category filtering",
                "correct": False,
                "rationale": (
                    "Incorrect. A category-filtering SWG can block or allow "
                    "sites by classification, but it does not provide the "
                    "cloud-application-level visibility and granular DLP "
                    "policy enforcement a CASB is purpose-built to deliver."
                ),
            },
            {
                "id": "c",
                "text": "Web application firewall (WAF) protecting the corporate website",
                "correct": False,
                "rationale": (
                    "Incorrect. A WAF protects an organization's own "
                    "internet-facing web application from inbound attacks; it "
                    "has no visibility into outbound employee use of "
                    "third-party SaaS applications."
                ),
            },
            {
                "id": "d",
                "text": "API gateway placed in front of internal microservices",
                "correct": False,
                "rationale": (
                    "Incorrect. An API gateway manages and secures traffic to "
                    "an organization's own internal APIs; it does not monitor "
                    "or govern employee use of external SaaS applications."
                ),
            },
        ],
        "explanation": (
            "A CASB is specifically designed to discover shadow IT SaaS usage "
            "and apply uniform DLP and security policy across both approved "
            "and unapproved cloud applications, unlike SWGs, WAFs, or API "
            "gateways, which address different traffic flows."
        ),
    },
    # ------------------------------------------------------------------ #
    # ICS/SCADA and embedded systems (3.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3b-004",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "ICS/SCADA and embedded systems",
        "stem": (
            "A water treatment facility's HMI communicates with PLCs using "
            "Modbus, a protocol with no built-in authentication or encryption "
            "by design. A penetration test shows an attacker on the OT segment "
            "could inject fraudulent Modbus write commands to a PLC. The "
            "protocol itself cannot be modified or replaced. Which control is "
            "MOST appropriate?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Deploy a protocol-aware industrial firewall between the "
                    "HMI and PLC network that allow-lists only legitimate "
                    "Modbus function codes and source/destination pairs"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Since Modbus itself cannot be secured, a "
                    "protocol-aware ICS firewall that inspects and "
                    "allow-lists legitimate commands and endpoints is the "
                    "standard compensating control for insecure-by-design OT "
                    "protocols."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Enable TLS encryption directly within the Modbus protocol "
                    "stack on each PLC"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Standard Modbus has no native support for TLS "
                    "encryption, and legacy PLCs generally cannot be modified "
                    "to add it, making this infeasible given the stated "
                    "constraint."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Require multifactor authentication before any HMI "
                    "operator can log into the workstation"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. MFA on the HMI workstation is a reasonable "
                    "access control, but it does nothing to stop an attacker "
                    "already on the OT network segment from directly "
                    "injecting unauthenticated Modbus commands to the PLC."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Replace the PLCs with general-purpose servers running a "
                    "modern, patchable operating system"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is a disproportionate, costly, and "
                    "operationally risky overhaul of safety-critical control "
                    "hardware and does not address the underlying insecure "
                    "protocol used for HMI-to-PLC communication."
                ),
            },
        ],
        "explanation": (
            "When an OT protocol like Modbus is insecure by design and cannot "
            "be changed, the standard mitigation is a protocol-aware "
            "industrial firewall that allow-lists legitimate commands and "
            "endpoints, since encryption or wholesale hardware replacement is "
            "not feasible."
        ),
    },
    # ------------------------------------------------------------------ #
    # IoT security (3.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3b-005",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "IoT security",
        "stem": (
            "Employees have been connecting personally purchased smart "
            "cameras and voice assistants to the corporate wireless network "
            "without IT's knowledge. These devices routinely phone home to "
            "manufacturer cloud servers overseas. Which control set BEST "
            "addresses this shadow IoT risk going forward?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Deploy network access control (NAC) with device "
                    "fingerprinting to automatically detect and quarantine "
                    "unauthorized IoT devices onto an isolated segment with "
                    "restricted outbound access"
                ),
                "correct": True,
                "rationale": (
                    "Correct. NAC with device fingerprinting detects "
                    "unmanaged devices as they connect and can automatically "
                    "quarantine them to a restricted segment, directly "
                    "addressing unauthorized shadow IoT devices phoning home "
                    "to unknown destinations."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Publish an acceptable use policy prohibiting personal "
                    "IoT devices on the corporate network"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A policy alone relies on voluntary compliance "
                    "and has no technical enforcement mechanism to actually "
                    "detect or stop devices already connecting to the "
                    "network."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Increase the wireless network's signal strength to cover "
                    "more of the building"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Improving wireless coverage is unrelated to "
                    "detecting or controlling unauthorized device access and "
                    "would not reduce this risk at all."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Require all wireless clients to use WPA2-Personal with a "
                    "single shared passphrase distributed to all employees"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A single shared passphrase still allows any "
                    "device that knows it — including unauthorized personal "
                    "IoT gadgets — to join the same network, and provides no "
                    "way to distinguish or isolate them."
                ),
            },
        ],
        "explanation": (
            "NAC with device fingerprinting and automatic quarantine is the "
            "standard technical control for identifying and containing "
            "unauthorized shadow IoT devices, unlike policy-only, coverage, "
            "or shared-passphrase approaches that do not enforce or "
            "distinguish device identity."
        ),
    },
    # ------------------------------------------------------------------ #
    # Microservices and containerization (3.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3b-006",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Microservices and containerization",
        "stem": (
            "A company running dozens of containerized microservices needs "
            "all service-to-service (east-west) traffic within the cluster to "
            "be mutually authenticated and encrypted, without requiring each "
            "development team to add TLS logic to their own application "
            "code. Which architecture BEST satisfies this requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A service mesh with sidecar proxies that transparently "
                    "enforce mutual TLS (mTLS) between services"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A service mesh injects sidecar proxies "
                    "alongside each service to transparently handle mTLS "
                    "encryption and mutual authentication for east-west "
                    "traffic, requiring no changes to application code."
                ),
            },
            {
                "id": "b",
                "text": (
                    "A web application firewall (WAF) placed in front of the "
                    "cluster's ingress controller"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A WAF at ingress inspects north-south traffic "
                    "entering the cluster from outside; it has no visibility "
                    "into or effect on internal service-to-service traffic."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Require each development team to individually implement "
                    "TLS libraries within their service's own codebase"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is exactly what the requirement says to "
                    "avoid — burdening every team with adding and maintaining "
                    "TLS logic in their own application code."
                ),
            },
            {
                "id": "d",
                "text": (
                    "An API gateway authenticating external client requests "
                    "before they enter the cluster"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. An API gateway secures external client access "
                    "to the cluster's exposed APIs; it does not encrypt or "
                    "authenticate traffic between internal services."
                ),
            },
        ],
        "explanation": (
            "A service mesh with sidecar proxies is the architecture "
            "purpose-built to transparently enforce mTLS for east-west "
            "microservice traffic without requiring per-service code changes, "
            "unlike WAFs or API gateways, which secure north-south traffic at "
            "the cluster boundary."
        ),
    },
    {
        "id": "nd3b-007",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Microservices and containerization",
        "stem": (
            "A container supply-chain audit finds two issues: (1) build "
            "pipelines pull base images from unverified public registries "
            "with no signature validation, and (2) database credentials are "
            "baked directly into image layers during the build. Which TWO "
            "remediations MOST directly address these two specific findings? "
            "(Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Require cryptographic image signing and verification, "
                    "pulling only from a trusted private registry"
                ),
                "correct": True,
                "rationale": (
                    "Correct. This directly remediates the finding of pulling "
                    "unverified images from untrusted public registries."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Inject secrets at runtime from a secrets manager or "
                    "orchestrator-managed secret store instead of embedding "
                    "them in image layers"
                ),
                "correct": True,
                "rationale": (
                    "Correct. This directly remediates the finding of "
                    "credentials baked into image layers by removing them "
                    "from the image entirely and supplying them only at "
                    "runtime."
                ),
            },
            {
                "id": "c",
                "text": "Deploy a WAF in front of the ingress controller",
                "correct": False,
                "rationale": (
                    "Incorrect. A WAF filters external web traffic reaching "
                    "the cluster; it does nothing to validate image "
                    "provenance or remove hardcoded secrets from image "
                    "layers."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Enforce Kubernetes network policies restricting "
                    "pod-to-pod traffic"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Network policies limit lateral traffic at "
                    "runtime; they do not address unverified image sources "
                    "or credentials baked into image layers during the "
                    "build."
                ),
            },
            {
                "id": "e",
                "text": "Increase the resource limits (CPU/memory) assigned to each pod",
                "correct": False,
                "rationale": (
                    "Incorrect. Resource limits affect performance and "
                    "stability, not image provenance or secret handling."
                ),
            },
        ],
        "explanation": (
            "Image signing/trusted-registry enforcement and runtime secret "
            "injection map directly to the two supply-chain findings — "
            "unverified image sources and hardcoded credentials — while a "
            "WAF, network policies, and resource limits address unrelated "
            "runtime concerns."
        ),
    },
    # ------------------------------------------------------------------ #
    # Serverless and cloud architecture (3.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3b-008",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Serverless and cloud architecture",
        "stem": (
            "A serverless function that only needs to read objects from one "
            "specific S3 bucket is instead assigned an execution role with "
            "write access to every bucket in the account and broad "
            "administrative permissions. A code-injection vulnerability in "
            "the function is later discovered. Which change would have MOST "
            "reduced the impact of exploiting that vulnerability?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Scope the function's execution role to only the specific "
                    "read action on the one bucket it actually requires"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Applying least privilege to the execution role "
                    "limits what an attacker who compromises the function "
                    "through code injection can actually do, directly "
                    "reducing blast radius."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Increase the function's memory allocation to improve "
                    "execution performance"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Memory allocation affects performance only "
                    "and has no bearing on the permissions available to an "
                    "attacker who compromises the function."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Move the function's code from a public repository to a "
                    "private one"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Repository visibility protects source code "
                    "confidentiality but does nothing to limit what an "
                    "already-exploited running function's overly broad IAM "
                    "role can do."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Increase the function's maximum execution timeout to "
                    "allow more complex operations to complete"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Execution timeout controls how long a "
                    "function may run; it is unrelated to the scope of "
                    "permissions granted to the function's execution role."
                ),
            },
        ],
        "explanation": (
            "Serverless functions should follow least privilege on their "
            "execution role/identity; an overly broad role turns any code-"
            "level compromise of the function into an account-wide incident, "
            "which memory, repository visibility, or timeout settings do "
            "nothing to prevent."
        ),
    },
    # ------------------------------------------------------------------ #
    # Virtualization and high availability (3.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3b-009",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Virtualization and high availability",
        "stem": (
            "An internal audit finds dozens of unpatched, unmanaged virtual "
            "machines running in the data center. Developers created them "
            "ad hoc for testing over the past two years, none were ever "
            "recorded in the CMDB, and no one currently knows which teams "
            "still need them. Which practice would MOST effectively prevent "
            "this situation from recurring?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Implement formal VM lifecycle governance requiring "
                    "registration, an owner, and an expiration/review date at "
                    "creation time, with periodic audits to decommission "
                    "orphaned VMs"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Lifecycle governance with mandatory "
                    "registration, ownership, and periodic review directly "
                    "prevents VM sprawl by ensuring every VM is tracked and "
                    "eventually decommissioned if unused."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Increase the physical host's CPU and memory capacity so "
                    "additional VMs can be created without performance "
                    "concerns"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Adding capacity makes it easier to create "
                    "even more untracked VMs; it does nothing to address the "
                    "lack of governance and tracking that caused the sprawl."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Switch from a Type 1 to a Type 2 hypervisor to simplify "
                    "VM management for developers"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Hypervisor type affects the isolation and "
                    "attack surface between guest and host, not whether VMs "
                    "are tracked, owned, or eventually decommissioned."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Configure all VMs in an active-active high-availability "
                    "cluster to eliminate single points of failure"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Active-active clustering improves "
                    "availability of running workloads; it does not address "
                    "the governance gap that let unmanaged, unpatched VMs "
                    "accumulate unnoticed."
                ),
            },
        ],
        "explanation": (
            "VM sprawl is a governance failure, not a capacity, hypervisor, "
            "or availability problem — it is prevented by requiring "
            "registration, ownership, and periodic lifecycle review of every "
            "VM created."
        ),
    },
    # ------------------------------------------------------------------ #
    # Attack surface reduction (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3b-010",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Attack surface reduction",
        "stem": (
            "A cloud team maintains a golden VM image used to spin up every "
            "new application server. The image still includes sample "
            "applications, a demo administrator account, and verbose debug "
            "error pages left over from the vendor's default installation. "
            "Every new server therefore inherits these by default. Which "
            "action MOST effectively reduces the attack surface of ALL future "
            "instances?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Harden the golden image itself by removing the sample "
                    "applications, disabling the demo account, and turning "
                    "off verbose debug output before it is used as a template"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Fixing the golden image at the source ensures "
                    "every future instance is provisioned clean, eliminating "
                    "the unnecessary attack surface permanently rather than "
                    "repeatedly after each deployment."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Deploy a network intrusion detection system (IDS) to "
                    "monitor traffic to each new instance"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Monitoring can detect misuse of the sample "
                    "applications or demo account, but does not remove them "
                    "from every instance created from the image."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Require administrators to manually remove the sample "
                    "applications and demo account from each new instance "
                    "after it is provisioned"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is reactive, error-prone, and does not "
                    "scale — every new instance will still be born insecure "
                    "unless someone remembers the manual cleanup step every "
                    "single time."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Add a WAF in front of each new instance to filter "
                    "malicious HTTP requests"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A WAF can help filter some malicious traffic, "
                    "but it does not eliminate the unnecessary sample "
                    "applications, demo account, or debug output baked into "
                    "every instance."
                ),
            },
        ],
        "explanation": (
            "Hardening the golden image itself eliminates the unnecessary "
            "attack surface at the source, so every instance provisioned "
            "from it going forward is clean by default — a far more scalable "
            "fix than monitoring, manual per-instance cleanup, or filtering "
            "traffic after the fact."
        ),
    },
    # ------------------------------------------------------------------ #
    # Change management workflow (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3b-011",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Change management workflow",
        "stem": (
            "A change advisory board approved a routine database schema "
            "change based only on the requester's description, without "
            "anyone formally assessing which downstream applications "
            "depended on the affected tables. After implementation, three "
            "unrelated reporting applications broke. Which step in the "
            "change management workflow was skipped, and directly caused this "
            "outcome?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Impact analysis identifying systems and stakeholders affected by the change",
                "correct": True,
                "rationale": (
                    "Correct. Impact analysis is the workflow step that "
                    "identifies which downstream systems and stakeholders "
                    "depend on the item being changed; skipping it is exactly "
                    "why the schema change's ripple effects on the reporting "
                    "applications went undetected."
                ),
            },
            {
                "id": "b",
                "text": "Formal CAB approval of the change request",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario states the CAB did approve the "
                    "change — the failure was that the approval was made "
                    "without adequate impact analysis, not that approval "
                    "itself was skipped."
                ),
            },
            {
                "id": "c",
                "text": "Documentation of the change in the change management system after implementation",
                "correct": False,
                "rationale": (
                    "Incorrect. Post-implementation documentation records what "
                    "was done; it does not prevent unforeseen downstream "
                    "breakage, which stems from a missing pre-implementation "
                    "impact assessment."
                ),
            },
            {
                "id": "d",
                "text": "Scheduling the change during an approved maintenance window",
                "correct": False,
                "rationale": (
                    "Incorrect. Maintenance-window scheduling controls when a "
                    "change occurs, not whether its downstream dependencies "
                    "were properly assessed beforehand."
                ),
            },
        ],
        "explanation": (
            "A thorough impact analysis identifying affected systems and "
            "stakeholders is meant to catch exactly this kind of unforeseen "
            "downstream breakage before a change is approved and "
            "implemented; skipping it, not skipping approval or "
            "documentation, is what caused the outage."
        ),
    },
    # ------------------------------------------------------------------ #
    # Failure modes (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3b-012",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Failure modes",
        "stem": (
            "An electronic badge-access lock secures a server room door. Fire "
            "and building safety codes require that, during a power loss or "
            "fire alarm, the door unlock automatically so occupants are never "
            "trapped, even though this creates a brief window where the room "
            "is physically unsecured. How should the lock's failure mode be "
            "configured?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Fail-safe, unlocking the door automatically on power loss or alarm",
                "correct": True,
                "rationale": (
                    "Correct. Fail-safe configurations prioritize life safety "
                    "by unlocking during a power failure or fire alarm, "
                    "matching the building code requirement described, even "
                    "though it briefly leaves the room physically unsecured."
                ),
            },
            {
                "id": "b",
                "text": "Fail-secure, keeping the door locked during power loss to protect the server room",
                "correct": False,
                "rationale": (
                    "Incorrect. Fail-secure prioritizes asset protection over "
                    "life safety by remaining locked during a power failure, "
                    "which would violate the stated fire/life-safety code "
                    "requirement to allow evacuation."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Active-active redundant lock controllers to eliminate any "
                    "single point of failure in the access system"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is a high-availability design choice for "
                    "the access control system, not a definition of how the "
                    "lock behaves when it does fail."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Remove electronic locking entirely and rely on a "
                    "traditional physical key at all times"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This abandons electronic access logging and "
                    "control entirely and does not address the specific "
                    "power-loss/fire-alarm failure behavior the scenario asks "
                    "about."
                ),
            },
        ],
        "explanation": (
            "When life safety and fire code requirements outweigh the risk of "
            "a brief physical security gap, electronic locks should be "
            "configured fail-safe (unlocking on failure), the opposite of "
            "fail-secure, which is used when asset protection outweighs "
            "safety."
        ),
    },
    {
        "id": "nd3b-013",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Failure modes",
        "stem": (
            "A K-12 school district's inline web content filter is legally "
            "required under the Children's Internet Protection Act (CIPA) to "
            "block inappropriate content for all student internet access at "
            "all times, as a condition of federal E-rate funding, even if "
            "this means blocking internet access entirely during an outage. "
            "How should the content filter's failure mode be configured?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Fail-closed, blocking all internet traffic if the filter fails",
                "correct": True,
                "rationale": (
                    "Correct. Fail-closed halts all traffic if the device "
                    "fails, ensuring students are never left with unfiltered "
                    "internet access — matching the compliance requirement "
                    "that filtering must apply at all times."
                ),
            },
            {
                "id": "b",
                "text": "Fail-open, allowing internet traffic to continue unfiltered if the filter fails",
                "correct": False,
                "rationale": (
                    "Incorrect. Fail-open would allow unfiltered internet "
                    "access during a failure, directly violating the CIPA "
                    "requirement that content filtering apply at all times."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Passive (tap/monitor) placement logging traffic for later "
                    "review without blocking anything in real time"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A passive tap cannot block content at all, "
                    "which fails the CIPA requirement to actively filter "
                    "inappropriate content in real time, not merely log it "
                    "afterward."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Load-balance content filtering across two independent "
                    "appliances to reduce the chance either one fails"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is a high-availability design choice "
                    "that reduces the likelihood of failure, but it does not "
                    "by itself specify what should happen to traffic if a "
                    "failure occurs regardless."
                ),
            },
        ],
        "explanation": (
            "When a legal or compliance mandate requires continuous "
            "filtering or inspection with zero tolerance for gaps, an inline "
            "device should be configured fail-closed, unlike scenarios where "
            "availability is prioritized over a brief security gap."
        ),
    },
    # ------------------------------------------------------------------ #
    # Firewalls (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3b-014",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Firewalls",
        "stem": (
            "A company needs to expose a public-facing web server to the "
            "internet while ensuring that, even if the web server is "
            "compromised, an attacker cannot directly reach the internal "
            "corporate network behind it. Which network architecture BEST "
            "achieves this?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A screened subnet (DMZ) placing the web server between "
                    "two firewalls, with separate rule sets governing "
                    "internet-to-DMZ and DMZ-to-internal traffic"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A screened subnet isolates the public-facing "
                    "server in its own zone with independently controlled "
                    "firewall rules on each side, so a compromised web server "
                    "still cannot freely reach the internal network."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Place the web server directly on the internal corporate "
                    "network with a single firewall performing NAT to expose "
                    "it to the internet"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Placing the internet-facing server directly "
                    "on the internal network means a compromise of that "
                    "server gives an attacker direct access to internal "
                    "systems, exactly what must be prevented."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Deploy a jump server that administrators use to manage "
                    "the web server remotely"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A jump server secures administrative access "
                    "paths into a segment; it does not by itself create the "
                    "isolated zone needed to contain a compromised "
                    "internet-facing web server."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Use a VPN concentrator to encrypt all traffic between "
                    "the internet and the web server"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Encrypting traffic in transit protects "
                    "confidentiality but does nothing to prevent a compromised "
                    "web server from reaching the internal network once an "
                    "attacker has code execution on it."
                ),
            },
        ],
        "explanation": (
            "A screened subnet (DMZ) with independent firewall rule sets on "
            "each side is the standard architecture for exposing a public "
            "server while containing the blast radius of its compromise away "
            "from the internal network."
        ),
    },
    {
        "id": "nd3b-015",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Firewalls",
        "stem": (
            "An administrator adds a new firewall rule explicitly allowing "
            "traffic from a partner's IP range to a specific application "
            "port. After saving the ruleset, traffic from that partner is "
            "still blocked. Review shows the new rule was appended to the "
            "bottom of the ruleset, below an existing broad \"deny all\" rule. "
            "What is the MOST likely cause, and correct fix?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Firewalls evaluate rules top-down and stop at the first "
                    "match; the new allow rule must be moved above the "
                    "broader deny-all rule to take effect"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Most firewalls process rules sequentially and "
                    "apply the first matching rule; a broad deny-all rule "
                    "positioned above a more specific allow rule will always "
                    "match first and block the traffic, so the specific rule "
                    "must be placed above it."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The firewall's rule cache must be manually cleared before "
                    "any newly added rule can take effect"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is not the general cause of a newly "
                    "added rule being ineffective; the described symptom — a "
                    "specific rule placed below a broad deny — is a rule "
                    "ordering issue, not a caching issue."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The firewall does not support allow rules for "
                    "partner/external IP ranges and only permits internal "
                    "traffic"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Standard firewalls fully support allow rules "
                    "for any source IP range, including external partners; "
                    "this is not a product limitation but a rule-ordering "
                    "mistake."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The rule needs to specify a stateful protocol instead of "
                    "a stateless one for the traffic to pass"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Statefulness relates to how a firewall tracks "
                    "connection sessions, not whether a specific allow rule "
                    "is evaluated before a broader deny rule positioned above "
                    "it in the ruleset."
                ),
            },
        ],
        "explanation": (
            "Firewall rulesets are typically evaluated top-down with a "
            "first-match action; a specific allow rule placed below a broad "
            "deny-all rule will never be reached, so correct rule ordering — "
            "not caching, product limitations, or statefulness — is the fix."
        ),
    },
    # ------------------------------------------------------------------ #
    # Network appliances (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3b-016",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network appliances",
        "stem": (
            "A company wants to control and log exactly which external "
            "websites internal employees are permitted to visit, applying a "
            "single centralized content-filtering and logging policy to all "
            "outbound web requests from the corporate LAN. Which appliance "
            "BEST fulfills this requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Forward proxy",
                "correct": True,
                "rationale": (
                    "Correct. A forward proxy sits between internal clients "
                    "and the internet, allowing centralized filtering, "
                    "logging, and control of outbound web requests before "
                    "they leave the network."
                ),
            },
            {
                "id": "b",
                "text": "Reverse proxy",
                "correct": False,
                "rationale": (
                    "Incorrect. A reverse proxy sits in front of internal "
                    "servers to mediate inbound requests from external "
                    "clients; it does not control or filter outbound requests "
                    "made by internal employees."
                ),
            },
            {
                "id": "c",
                "text": "Load balancer",
                "correct": False,
                "rationale": (
                    "Incorrect. A load balancer distributes inbound traffic "
                    "across multiple backend servers; it has no role in "
                    "filtering or logging employees' outbound web browsing."
                ),
            },
            {
                "id": "d",
                "text": "VPN concentrator",
                "correct": False,
                "rationale": (
                    "Incorrect. A VPN concentrator terminates encrypted "
                    "remote-access tunnels; it does not provide centralized "
                    "content filtering or logging of general web browsing "
                    "traffic."
                ),
            },
        ],
        "explanation": (
            "A forward proxy is the appliance purpose-built to centrally "
            "control, filter, and log outbound web traffic from internal "
            "clients to the internet, unlike reverse proxies, load "
            "balancers, or VPN concentrators, which serve different traffic "
            "flows."
        ),
    },
    {
        "id": "nd3b-017",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Network appliances",
        "stem": (
            "Backend web servers behind a load balancer are experiencing high "
            "CPU utilization because each one must perform a full TLS "
            "handshake and decrypt every incoming HTTPS connection "
            "individually. The security team still requires that traffic "
            "between the load balancer and the backend servers remain "
            "encrypted. Which load balancer feature BEST resolves the CPU "
            "issue while meeting that requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "TLS termination/offloading at the load balancer, "
                    "re-encrypting traffic before forwarding it to the "
                    "backend servers"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Offloading TLS to the load balancer removes the "
                    "handshake and decryption burden from each backend "
                    "server, and re-encrypting before forwarding preserves "
                    "encryption on the backend leg as required."
                ),
            },
            {
                "id": "b",
                "text": (
                    "TLS termination/offloading at the load balancer, "
                    "forwarding traffic to the backend servers in plaintext"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Forwarding traffic in plaintext to the "
                    "backend violates the requirement that traffic between "
                    "the load balancer and the servers remain encrypted."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Configure the load balancer in pure Layer 4 pass-through "
                    "mode, forwarding encrypted packets to the backend "
                    "servers unmodified"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. In pass-through mode, the backend servers "
                    "still individually perform the full TLS handshake and "
                    "decryption for every connection, which does not resolve "
                    "the CPU issue at all."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Increase the number of backend web servers behind the "
                    "load balancer to spread the TLS workload further"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Adding more servers reduces the load per "
                    "server somewhat but does not eliminate the root cause — "
                    "every server still individually performs TLS handshakes "
                    "— and is a more costly workaround than offloading."
                ),
            },
        ],
        "explanation": (
            "TLS offloading at the load balancer, with re-encryption before "
            "forwarding to backend servers, removes the CPU-intensive "
            "handshake burden from every backend server while still "
            "satisfying the requirement that backend traffic remain "
            "encrypted."
        ),
    },
    # ------------------------------------------------------------------ #
    # Port security and 802.1X (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3b-018",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Port security and 802.1X",
        "stem": (
            "An attacker plugs a small unmanaged switch into an unattended "
            "office wall jack and connects several unauthorized laptops "
            "through it, all reachable via the single switchport. The company "
            "wants each wall jack to learn only a small, fixed number of MAC "
            "addresses and automatically disable the port if that limit is "
            "exceeded. Which control BEST achieves this?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Switch port security configured with a maximum MAC "
                    "address count per port and a shutdown violation action"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Port security's MAC address limiting feature "
                    "restricts how many MAC addresses a single port will "
                    "learn and can automatically shut the port down when a "
                    "rogue switch introduces more devices than the limit "
                    "allows."
                ),
            },
            {
                "id": "b",
                "text": (
                    "802.1X certificate-based authentication with dynamic "
                    "VLAN assignment"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. 802.1X authenticates the identity of a "
                    "connecting device but does not, by itself, limit or "
                    "count how many MAC addresses a physical port will "
                    "learn — that is the specific function of port security."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Port mirroring (SPAN) configured on the switchport to "
                    "capture traffic for later analysis"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Port mirroring only copies traffic for "
                    "monitoring; it does not limit MAC addresses or disable "
                    "the port automatically."
                ),
            },
            {
                "id": "d",
                "text": (
                    "A site-to-site VPN tunnel terminating at each office wall "
                    "jack"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. VPN tunnels secure traffic between networks "
                    "over untrusted links; they have no relevance to "
                    "controlling how many devices connect to a local wired "
                    "switchport."
                ),
            },
        ],
        "explanation": (
            "Switch port security's MAC address limiting and violation "
            "action is the Layer 2 control purpose-built to stop exactly this "
            "kind of rogue-switch device flooding on a single port, distinct "
            "from 802.1X's identity-based authentication."
        ),
    },
    # ------------------------------------------------------------------ #
    # SDN and logical segmentation (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3b-019",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SDN and logical segmentation",
        "stem": (
            "A software-defined data center must extend a single tenant's "
            "Layer 2 broadcast domain across virtual machines hosted in racks "
            "in three different physical data centers, which are connected "
            "to each other only through Layer 3 IP routing. Re-cabling for "
            "direct Layer 2 connectivity is not possible. Which technology "
            "BEST achieves this?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "VXLAN overlay networking, encapsulating Layer 2 frames "
                    "inside Layer 3 UDP packets to extend the broadcast "
                    "domain across routed infrastructure"
                ),
                "correct": True,
                "rationale": (
                    "Correct. VXLAN is specifically designed to tunnel "
                    "Layer 2 traffic over a Layer 3 network, allowing a "
                    "tenant's broadcast domain to logically span physically "
                    "separate, routed data centers without any recabling."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Traditional 802.1Q VLAN trunking between the data center "
                    "switches"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Standard VLAN trunking operates at Layer 2 "
                    "and does not natively traverse Layer 3 routed links "
                    "between separate physical sites without additional "
                    "tunneling technology."
                ),
            },
            {
                "id": "c",
                "text": (
                    "IPSec tunnel mode between routers at each data center"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. IPSec tunnel mode encrypts and encapsulates "
                    "IP packets for secure Layer 3 transit; it does not "
                    "extend a Layer 2 broadcast domain across sites."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Static routing configured manually between each data "
                    "center's Layer 3 boundary"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Static routing moves Layer 3 traffic between "
                    "networks but does not preserve or extend a Layer 2 "
                    "broadcast domain across those routed boundaries."
                ),
            },
        ],
        "explanation": (
            "VXLAN overlay networking is the standard SDN technology for "
            "extending Layer 2 segments across Layer 3 routed infrastructure "
            "between physically separate sites, which VLAN trunking, IPSec, "
            "and static routing cannot accomplish on their own."
        ),
    },
    {
        "id": "nd3b-020",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "SDN and logical segmentation",
        "stem": (
            "In a large SDN deployment, all switching and routing behavior "
            "across the fabric is governed by flow rules pushed from a "
            "single centralized SDN controller. A security architect notes "
            "that compromising this one controller would let an attacker "
            "push malicious flow rules to every switch in the fabric "
            "simultaneously. Which architectural control BEST addresses this "
            "specific risk?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Tightly restrict and harden access to the SDN "
                    "controller — placing it on an isolated out-of-band "
                    "management network with strict RBAC — and deploy "
                    "controller redundancy so a single compromised or failed "
                    "instance cannot control the entire fabric"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Because the controller is the single "
                    "authoritative brain of the fabric, hardening and "
                    "isolating access to it, combined with redundancy, "
                    "directly reduces the impact of the controller itself "
                    "being compromised."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Replace SDN with traditional per-device VLAN "
                    "configuration to eliminate the controller entirely"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This eliminates the operational and scaling "
                    "benefits SDN was adopted for in the first place, "
                    "reverting to slow, manual, error-prone per-device "
                    "configuration rather than addressing controller "
                    "security specifically."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Increase the number of physical switches in the fabric "
                    "to distribute the impact of any single flow rule"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Adding more switches does not reduce the "
                    "risk — a compromised controller can still push malicious "
                    "flow rules to every switch in the larger fabric just as "
                    "easily."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Encrypt all data-plane traffic between end hosts using "
                    "IPSec"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Encrypting host-to-host data-plane traffic "
                    "protects confidentiality of that traffic but does "
                    "nothing to prevent a compromised controller from pushing "
                    "malicious flow rules that redirect, drop, or duplicate "
                    "traffic fabric-wide."
                ),
            },
        ],
        "explanation": (
            "Since the SDN controller is the single point of authority over "
            "the entire fabric's data plane, hardening and isolating access "
            "to it and adding controller redundancy is the appropriate "
            "mitigation for controller-compromise risk, not abandoning SDN, "
            "adding switches, or encrypting unrelated host traffic."
        ),
    },
    # ------------------------------------------------------------------ #
    # Secure communication (VPN/TLS/IPSec) (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3b-021",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Secure communication (VPN/TLS/IPSec)",
        "stem": (
            "A site-to-site IPSec VPN is currently configured to use only the "
            "Authentication Header (AH) protocol, which provides integrity "
            "and origin authentication for each packet but does not encrypt "
            "the payload. Regulatory requirements now mandate that the "
            "traffic also be kept confidential from anyone who can capture it "
            "in transit. Which change is required?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Switch to Encapsulating Security Payload (ESP), which "
                    "provides both encryption and authentication/integrity"
                ),
                "correct": True,
                "rationale": (
                    "Correct. ESP provides both confidentiality (encryption) "
                    "and authentication/integrity, unlike AH, which offers "
                    "authentication and integrity only — exactly closing the "
                    "confidentiality gap the regulation requires."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Continue using AH, since it already provides adequate "
                    "protection for regulated data in transit"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. AH never encrypts the payload under any "
                    "configuration, so it cannot satisfy a confidentiality "
                    "requirement no matter how it is deployed."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Switch from IPSec tunnel mode to transport mode to add "
                    "encryption"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Tunnel versus transport mode determines what "
                    "portion of the packet is encapsulated, not whether "
                    "encryption is applied at all — that distinction is "
                    "governed by the AH versus ESP protocol choice."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Add a GRE tunnel on top of the existing AH configuration"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. GRE provides encapsulation and routing "
                    "flexibility but no encryption of its own, so layering it "
                    "on top of AH still leaves the traffic unencrypted."
                ),
            },
        ],
        "explanation": (
            "Within IPSec, ESP is the protocol that provides confidentiality "
            "through encryption in addition to authentication and integrity, "
            "while AH provides authentication and integrity only — the "
            "protocol choice, not the tunnel/transport mode, determines "
            "whether payload encryption is applied."
        ),
    },
    {
        "id": "nd3b-022",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Secure communication (VPN/TLS/IPSec)",
        "stem": (
            "A partner integration requires that an API client application "
            "and the API server each cryptographically verify the other "
            "party's identity using X.509 certificates before any API call is "
            "permitted — standard one-way TLS, where only the server proves "
            "its identity to the client, is not sufficient. Which "
            "configuration satisfies this requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Mutual TLS (mTLS), requiring both client and server certificates",
                "correct": True,
                "rationale": (
                    "Correct. Mutual TLS extends the standard TLS handshake "
                    "so both the client and the server present and validate "
                    "certificates, providing the bidirectional identity "
                    "verification the requirement calls for."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Standard one-way TLS with an extended validation (EV) "
                    "server certificate"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. An EV certificate strengthens the level of "
                    "identity vetting behind the server's certificate, but "
                    "one-way TLS still only authenticates the server to the "
                    "client, not the client to the server."
                ),
            },
            {
                "id": "c",
                "text": (
                    "IPSec tunnel mode between the client and the server"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. IPSec tunnel mode secures network-to-network "
                    "traffic and is not the mechanism used for authenticating "
                    "individual application-layer API clients and servers to "
                    "each other via certificates."
                ),
            },
            {
                "id": "d",
                "text": (
                    "A shared API key transmitted in the HTTP request header "
                    "over standard TLS"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A shared API key is a bearer-token credential, "
                    "not certificate-based cryptographic identity "
                    "verification, and it does not authenticate the server "
                    "to the client at all."
                ),
            },
        ],
        "explanation": (
            "Mutual TLS (mTLS) is the standard mechanism for requiring both "
            "parties in a connection to present and validate certificates, "
            "satisfying bidirectional identity verification that standard "
            "one-way TLS, IPSec, or API keys do not provide."
        ),
    },
    # ------------------------------------------------------------------ #
    # Zero Trust / SASE (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3b-023",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Zero Trust / SASE",
        "stem": (
            "In a Zero Trust deployment, a user successfully authenticates "
            "with MFA at 9 a.m. and begins a session. At 9:45 a.m., the "
            "user's device posture check fails after malware disables its "
            "endpoint agent, and shortly after, the user's traffic begins "
            "originating from a new, unrecognized geographic location. "
            "Without any new login attempt, the system automatically forces "
            "step-up authentication and then terminates the session. Which "
            "Zero Trust principle does this behavior demonstrate?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Continuous, adaptive evaluation of risk signals "
                    "throughout the session, rather than trusting a session "
                    "indefinitely after a single successful login"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Zero Trust does not treat authentication as a "
                    "one-time event; it continuously re-evaluates identity, "
                    "device posture, and contextual risk signals throughout "
                    "the session and can force re-authentication or "
                    "termination when risk increases, exactly as described."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Implicit trust granted to any session that has already "
                    "passed MFA once, regardless of later changes in risk"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This describes the opposite of what happened "
                    "and the opposite of Zero Trust — the scenario shows "
                    "trust being actively revoked mid-session in response to "
                    "new risk, not extended indefinitely after one login."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Perimeter-based trust, where any traffic originating "
                    "from inside the corporate network is automatically "
                    "trusted"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This describes traditional perimeter-based "
                    "security, which Zero Trust explicitly rejects; the "
                    "scenario shows evaluation based on device posture and "
                    "context, not network location."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Full-tunnel VPN routing, ensuring all traffic passes "
                    "through a central inspection point"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Full-tunnel VPN routing is a traffic-routing "
                    "configuration and does not describe the continuous, "
                    "risk-based re-evaluation of an already-established "
                    "session shown in the scenario."
                ),
            },
        ],
        "explanation": (
            "Continuous, adaptive verification of identity, device posture, "
            "and context throughout a session — not just at initial login — "
            "is a core Zero Trust principle, directly demonstrated by the "
            "system's automatic step-up authentication and termination in "
            "response to new risk signals."
        ),
    },
    {
        "id": "nd3b-024",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Zero Trust / SASE",
        "stem": (
            "A security architect is comparing Zero Trust Network Access "
            "(ZTNA) to the organization's legacy full-tunnel client VPN for "
            "remote access. Which TWO characteristics genuinely distinguish "
            "ZTNA from the traditional VPN? (Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "ZTNA grants access to individual, specific applications "
                    "rather than placing the user on the broader network "
                    "segment"
                ),
                "correct": True,
                "rationale": (
                    "Correct. ZTNA brokers access on a per-application basis, "
                    "unlike a traditional VPN, which typically places the "
                    "remote user's device onto the internal network segment "
                    "with broader reachability."
                ),
            },
            {
                "id": "b",
                "text": (
                    "ZTNA continuously re-verifies identity, device posture, "
                    "and context for each access request rather than trusting "
                    "the session after a single initial login"
                ),
                "correct": True,
                "rationale": (
                    "Correct. ZTNA evaluates trust continuously per request/"
                    "session based on identity, device, and context signals, "
                    "in contrast to a traditional VPN, which generally trusts "
                    "the connection for its full duration after the initial "
                    "authentication."
                ),
            },
            {
                "id": "c",
                "text": (
                    "ZTNA encrypts traffic between the client and the "
                    "destination, while a traditional VPN does not"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Both ZTNA and a traditional VPN encrypt the "
                    "connection; encryption itself is not the distinguishing "
                    "characteristic between the two."
                ),
            },
            {
                "id": "d",
                "text": (
                    "ZTNA requires a dedicated hardware VPN concentrator at "
                    "the network perimeter to terminate connections"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This describes a traditional VPN's typical "
                    "architecture; ZTNA is generally delivered as a "
                    "cloud-based broker service rather than requiring a "
                    "perimeter hardware concentrator."
                ),
            },
            {
                "id": "e",
                "text": (
                    "ZTNA assigns the remote client a routable IP address on "
                    "the internal corporate LAN, just like a traditional VPN"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This describes traditional VPN behavior; "
                    "ZTNA specifically avoids placing the remote device onto "
                    "the internal network, brokering only application-level "
                    "access instead."
                ),
            },
        ],
        "explanation": (
            "ZTNA's defining differences from a traditional VPN are its "
            "application-level (rather than network-level) access grants and "
            "its continuous, per-request re-verification of trust — not "
            "encryption itself, which both approaches provide, and not "
            "architectural traits like perimeter concentrators or LAN IP "
            "assignment that describe the legacy VPN model instead."
        ),
    },
    # ------------------------------------------------------------------ #
    # Data classification (3.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3b-025",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Data classification",
        "stem": (
            "A SaaS company classifies data using the labels Public, "
            "Internal, Confidential, and Restricted. Stored payment card "
            "numbers fall within PCI DSS scope, and only a small, named "
            "fraud-and-finance team may access them on a strict need-to-know "
            "basis; unauthorized exposure would trigger PCI penalties and "
            "card-brand fines. Which classification should this card data "
            "receive?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Restricted",
                "correct": True,
                "rationale": (
                    "Correct. Restricted is reserved for data limited to a "
                    "narrow, named group on strict need-to-know with severe "
                    "regulatory consequences on exposure — matching PCI-"
                    "scoped card data exactly."
                ),
            },
            {
                "id": "b",
                "text": "Confidential",
                "correct": False,
                "rationale": (
                    "Incorrect. Confidential suits many sensitive business "
                    "records, but this scheme reserves a stricter "
                    "\"Restricted\" tier specifically for data limited to a "
                    "narrow, named group — a tighter control than "
                    "Confidential's broader business need-to-know typically "
                    "allows."
                ),
            },
            {
                "id": "c",
                "text": "Internal",
                "correct": False,
                "rationale": (
                    "Incorrect. Internal data is intended for general "
                    "employee use, far too permissive for regulated PCI-"
                    "scoped cardholder data with strict access limitations."
                ),
            },
            {
                "id": "d",
                "text": "Public",
                "correct": False,
                "rationale": (
                    "Incorrect. Public data carries no disclosure risk at "
                    "all, the opposite of regulated payment card data subject "
                    "to PCI DSS."
                ),
            },
        ],
        "explanation": (
            "When a classification scheme includes a tier explicitly "
            "reserved for the narrowest, named-individual, need-to-know "
            "access, regulated data like PCI-scoped card numbers with severe "
            "financial and legal impact belongs at that highest (Restricted) "
            "tier."
        ),
    },
    # ------------------------------------------------------------------ #
    # Data protection methods (3.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3b-026",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Data protection methods",
        "stem": (
            "A US-based healthcare SaaS provider must ensure that EU patient "
            "data is processed and stored only on servers physically located "
            "within the European Union, in order to comply with data "
            "sovereignty requirements. Which control BEST enforces this?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Geographic restrictions (geofencing) enforced through "
                    "cloud provider region locking, ensuring EU patient data "
                    "is only stored and processed in EU data center regions"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Geographic restrictions/region locking "
                    "directly enforces where data is physically stored and "
                    "processed, which is precisely what a data sovereignty "
                    "requirement demands."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Column-level encryption of the patient data, with keys "
                    "managed by a US-based KMS"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Encryption protects confidentiality but does "
                    "not control the physical location where the data is "
                    "stored or processed, which is the specific requirement "
                    "here."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Tokenizing the patient data before storing it in any "
                    "region"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Tokenization substitutes surrogate values for "
                    "sensitive data but says nothing about where the "
                    "underlying data or vault physically resides, so it does "
                    "not satisfy a location-based sovereignty requirement."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Role-based access control restricting which employees "
                    "may view the patient data"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Access control governs who may view the data "
                    "regardless of where it is stored; it does not address "
                    "the requirement that the data physically reside within "
                    "EU borders."
                ),
            },
        ],
        "explanation": (
            "Geographic restrictions/geofencing through cloud region locking "
            "is the control that directly enforces data sovereignty "
            "requirements about physical data location, unlike encryption, "
            "tokenization, or access control, which address different "
            "protection goals."
        ),
    },
    {
        "id": "nd3b-027",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Data protection methods",
        "stem": (
            "A defense contractor must ensure that (1) a set of highly "
            "sensitive design files can only be decrypted and opened by "
            "devices physically located within approved, badge-controlled "
            "corporate office buildings, and (2) even among employees inside "
            "those buildings, access to the files is further restricted "
            "based on each employee's specific job role. Which TWO data "
            "protection methods, used together, satisfy BOTH requirements? "
            "(Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Geographic restrictions (geofencing) tied to the "
                    "device's verified physical location, required before "
                    "decryption is permitted"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Geofencing directly enforces the requirement "
                    "that files can only be decrypted by devices physically "
                    "located within the approved office buildings."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Role-based permission restrictions, granting access to "
                    "the files only to job roles that require them"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Role-based permission restrictions directly "
                    "satisfy the requirement that access be further limited "
                    "by an employee's specific job role, even among those "
                    "physically on-site."
                ),
            },
            {
                "id": "c",
                "text": "One-way hashing of the design files",
                "correct": False,
                "rationale": (
                    "Incorrect. Hashing is irreversible and would prevent "
                    "authorized employees from ever opening or viewing the "
                    "original design files at all, which does not meet a "
                    "usability requirement to view them under the right "
                    "conditions."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Static masking of the design files for all internal "
                    "users"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Static masking permanently obscures data for "
                    "display or non-production use; it is not designed to "
                    "let authorized on-site employees view the real design "
                    "files at all."
                ),
            },
            {
                "id": "e",
                "text": (
                    "Labeling the files \"Restricted\" in the data "
                    "classification scheme"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Classification labeling documents intended "
                    "handling requirements but provides no actual "
                    "enforcement mechanism for location-based decryption or "
                    "role-based access on its own."
                ),
            },
        ],
        "explanation": (
            "Geofencing enforces the physical-location decryption "
            "requirement, while role-based permission restrictions enforce "
            "the additional job-role-based access limitation — together "
            "satisfying both stated requirements, unlike hashing, masking, "
            "or classification labeling alone, none of which enforce either "
            "condition."
        ),
    },
    # ------------------------------------------------------------------ #
    # Data states (3.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3b-028",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Data states",
        "stem": (
            "A company ships weekly backup tapes containing unencrypted "
            "customer records via courier to an offsite storage vendor. "
            "During transport, the tapes are never connected to any network. "
            "Which data state applies to this customer data while the tapes "
            "are in the courier's vehicle, and which protection is MOST "
            "appropriate?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Data at rest — the data is stored on the tape medium "
                    "the entire time, so full tape/media encryption should be "
                    "applied regardless of physical transport"
                ),
                "correct": True,
                "rationale": (
                    "Correct. \"Data in transit\" specifically refers to data "
                    "actively moving across a network; data stored on a "
                    "physical medium remains \"data at rest\" even while that "
                    "medium is being physically relocated, so tape/media "
                    "encryption is the appropriate control."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Data in transit — the tapes are physically moving "
                    "between locations, so TLS should be enabled to protect "
                    "them during the courier trip"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Data in transit refers to data moving across "
                    "a network connection; the tapes are not connected to any "
                    "network during physical transport, and TLS has no "
                    "relevance to protecting data stored on an offline "
                    "medium."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Data in use — the data is actively being read by the "
                    "courier's tracking systems, so memory encryption should "
                    "be applied"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Data in use refers to data actively being "
                    "processed in memory by an application; the tapes are "
                    "simply being physically transported, not processed."
                ),
            },
            {
                "id": "d",
                "text": (
                    "No data state classification applies to offline physical "
                    "media, so no additional protection is necessary"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. All stored data has an applicable state "
                    "(data at rest) and the scenario explicitly states the "
                    "tapes are unencrypted, representing a real exposure risk "
                    "if the tapes are lost or stolen in transit."
                ),
            },
        ],
        "explanation": (
            "Data on a physical medium — such as a backup tape — remains "
            "classified as data at rest even while it is being physically "
            "relocated, since \"data in transit\" specifically describes "
            "network transmission; the correct protection is encrypting the "
            "media itself."
        ),
    },
    # ------------------------------------------------------------------ #
    # Tokenization and masking (3.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3b-029",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Tokenization and masking",
        "stem": (
            "A payment processor's vault-based tokenization system, which "
            "stores a lookup table mapping tokens to real card numbers, has "
            "become a performance bottleneck as transaction volume has grown "
            "into the millions per day, and the vault is difficult to scale "
            "horizontally. Which change addresses this while preserving the "
            "ability to detokenize when authorized?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Migrate to vaultless tokenization, which algorithmically "
                    "generates and reverses tokens using a cryptographic key "
                    "rather than a centralized lookup table"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Vaultless tokenization eliminates the central "
                    "lookup table bottleneck by deriving tokens "
                    "algorithmically from a key, allowing it to scale far "
                    "more easily while still supporting authorized "
                    "detokenization."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Switch from tokenization to one-way hashing of the card "
                    "numbers to eliminate the vault lookup entirely"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Hashing is irreversible, so authorized "
                    "detokenization for legitimate business needs like "
                    "refunds would no longer be possible at all."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Increase the vault's lookup table refresh interval to "
                    "reduce database write frequency"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This does not address the fundamental "
                    "architectural bottleneck of a centralized lookup table "
                    "under heavy transaction volume; it only marginally "
                    "reduces write frequency."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Replace tokenization with static data masking of the "
                    "card numbers"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Static masking is irreversible by design, "
                    "which would eliminate the payment processor's ability "
                    "to ever recover the original card number, unlike "
                    "tokenization."
                ),
            },
        ],
        "explanation": (
            "Vaultless tokenization removes the centralized lookup-table "
            "bottleneck by generating and reversing tokens algorithmically, "
            "preserving authorized reversibility at much greater scale than "
            "vault-based tokenization, unlike hashing or masking, which are "
            "irreversible."
        ),
    },
    {
        "id": "nd3b-030",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Tokenization and masking",
        "stem": (
            "A QA team refreshes its test database nightly from a masked "
            "copy of production. The same customer_id value appears in "
            "several related tables (orders, invoices, support tickets), and "
            "the masked value must be identical everywhere that customer_id "
            "appears so that foreign-key joins across tables continue to "
            "work correctly in testing. Which masking approach is required?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Deterministic masking, where the same input value always "
                    "produces the same masked output"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Deterministic masking guarantees that every "
                    "occurrence of the same original customer_id maps to the "
                    "same masked value across every table, preserving "
                    "referential integrity for foreign-key joins."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Random (non-deterministic) masking, generating a new "
                    "masked value each time a value is masked"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Random masking would produce a different "
                    "masked value for the same customer_id in each table, "
                    "breaking the foreign-key relationships the QA tests "
                    "depend on."
                ),
            },
            {
                "id": "c",
                "text": (
                    "One-way salted hashing of the customer_id in each table "
                    "independently"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Using a unique salt in each table would "
                    "produce different hash outputs for the same customer_id "
                    "across tables, which also breaks referential integrity, "
                    "and hashing does not preserve a realistic format the way "
                    "masking does."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Dynamic masking applied only at query time based on the "
                    "requesting user's role"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Dynamic masking is designed to control what a "
                    "given user sees on display in production, not to "
                    "produce a permanently consistent, referentially intact "
                    "data set for a refreshed non-production QA database."
                ),
            },
        ],
        "explanation": (
            "Deterministic masking is required whenever masked values must "
            "remain consistent across related tables to preserve foreign-key "
            "relationships, unlike random masking, per-table salted hashing, "
            "or query-time dynamic masking, none of which guarantee "
            "consistent output for the same input value."
        ),
    },
    # ------------------------------------------------------------------ #
    # Backups and replication (3.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3b-031",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Backups and replication",
        "stem": (
            "Ransomware encrypted a company's production file servers and, "
            "because the backup NAS appliance was continuously mounted and "
            "writable from the production network, the ransomware also "
            "encrypted every backup stored on it. Which change would MOST "
            "effectively prevent this from happening again?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Maintain immutable, offline or air-gapped backup copies "
                    "(e.g., object-lock/WORM storage) that are not "
                    "continuously writable from the production network"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Immutable, offline, or air-gapped backups "
                    "cannot be altered or encrypted by ransomware that has "
                    "compromised the production network, since they are not "
                    "continuously reachable or writable from it."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Increase the frequency of incremental backups to the "
                    "same NAS appliance to shrink the potential data-loss "
                    "window"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. More frequent backups to the same "
                    "continuously writable NAS would still be encrypted by "
                    "ransomware just as easily — the root problem is "
                    "reachability, not backup frequency."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Replicate production data in real time to a hot DR site "
                    "using synchronous replication"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Synchronous replication would faithfully "
                    "propagate the ransomware's encryption to the DR site "
                    "almost immediately, since it mirrors every write in "
                    "near real time."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Take more frequent snapshots on the same NAS appliance "
                    "throughout the day"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. If the NAS itself remains continuously "
                    "writable from the compromised production network, "
                    "additional snapshots stored on it are still exposed to "
                    "the same ransomware attack."
                ),
            },
        ],
        "explanation": (
            "Ransomware resilience for backups requires immutable, offline, "
            "or air-gapped copies that are not continuously reachable and "
            "writable from production, since simply increasing backup or "
            "snapshot frequency, or replicating in real time, do not remove "
            "the backup from the ransomware's reach."
        ),
    },
    {
        "id": "nd3b-032",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Backups and replication",
        "stem": (
            "A financial firm is legally required to retain certain backup "
            "archives for seven years, with the ability to restore any given "
            "month-end and year-end state, while minimizing the total number "
            "of long-term full backup copies that must be stored offsite. "
            "Which backup rotation scheme BEST fits this requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Grandfather-father-son (GFS) rotation, retaining daily "
                    "backups short-term, weekly backups longer, and monthly/"
                    "yearly full archives for the full retention period"
                ),
                "correct": True,
                "rationale": (
                    "Correct. GFS rotation is specifically designed to "
                    "retain a manageable set of daily, weekly, and long-term "
                    "monthly/yearly full backups, allowing restoration of any "
                    "required month-end or year-end state while minimizing "
                    "the total number of long-term full copies stored."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Continuous data protection (CDP), journaling every "
                    "transaction in real time indefinitely"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. CDP is designed for fine-grained recovery of "
                    "very recent changes, not for efficiently managing "
                    "long-term, multi-year archival retention with minimal "
                    "storage of full copies."
                ),
            },
            {
                "id": "c",
                "text": (
                    "A full backup performed and retained every single day "
                    "for the entire seven-year period"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Storing a full backup every day for seven "
                    "years produces an enormous, unnecessary volume of "
                    "long-term full copies, directly conflicting with the "
                    "requirement to minimize them."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Incremental-only backups with no periodic full backup "
                    "ever taken"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Restoring any specific month-end or year-end "
                    "state from an endless chain of incrementals with no "
                    "periodic full backup becomes impractical and "
                    "increasingly fragile over a seven-year span."
                ),
            },
        ],
        "explanation": (
            "Grandfather-father-son rotation is the standard scheme for "
            "long-term, multi-year archival retention, efficiently "
            "preserving recoverable month-end and year-end states while "
            "minimizing the number of long-term full copies compared to "
            "daily fulls, endless incrementals, or CDP."
        ),
    },
    # ------------------------------------------------------------------ #
    # High availability (3.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3b-033",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "High availability",
        "stem": (
            "A web tier has three redundant application servers, but all "
            "traffic passes through a single load balancer. The security "
            "architect notes that the load balancer itself is now a single "
            "point of failure for the entire tier. Which design change BEST "
            "resolves this?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Deploy a second load balancer in an active-passive pair "
                    "using a heartbeat protocol (e.g., VRRP) and a shared "
                    "floating virtual IP, so the standby takes over "
                    "automatically if the active load balancer fails"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Pairing load balancers with a heartbeat "
                    "protocol and floating VIP eliminates the load balancer "
                    "itself as a single point of failure, automatically "
                    "failing over without manual intervention."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Add a fourth redundant application server behind the "
                    "existing single load balancer"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Adding more backend application servers does "
                    "nothing to address the load balancer itself remaining a "
                    "single point of failure for the entire tier."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Enable session persistence (sticky sessions) on the "
                    "existing load balancer"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Session persistence addresses keeping a "
                    "user's requests pinned to the same backend server; it "
                    "does not provide redundancy for the load balancer "
                    "device itself."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Reduce the load balancer's health check interval so "
                    "unhealthy backend servers are detected faster"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Faster health checks improve detection of "
                    "unhealthy backend servers, but do nothing to protect "
                    "against the load balancer itself failing."
                ),
            },
        ],
        "explanation": (
            "High availability must be designed at every tier, including the "
            "load balancer itself; a redundant active-passive load balancer "
            "pair with a heartbeat protocol and floating VIP eliminates it as "
            "a single point of failure, unlike changes to the backend "
            "servers or health check timing."
        ),
    },
    {
        "id": "nd3b-034",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "High availability",
        "stem": (
            "A two-node active-passive database cluster loses its "
            "inter-node heartbeat link due to a network partition. Both "
            "nodes, unable to confirm the other's status, independently "
            "conclude they are the sole surviving primary and both begin "
            "accepting writes, resulting in data corruption. Which "
            "architecture change BEST prevents this from recurring?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Add a third quorum/witness node whose vote is required "
                    "to determine which node becomes primary during a "
                    "network partition"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A quorum/witness node breaks the tie during a "
                    "network partition, ensuring only one node can achieve a "
                    "majority vote and become primary, directly preventing "
                    "this split-brain scenario."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Switch the cluster from active-passive to active-active "
                    "so both nodes process writes simultaneously by design"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This would make simultaneous writes to both "
                    "nodes the intended behavior rather than an error "
                    "condition, but without proper conflict resolution or "
                    "quorum it does not prevent the underlying data "
                    "corruption risk during a partition."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Reduce the heartbeat check interval so node failures "
                    "are detected more quickly"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A faster heartbeat interval does not resolve "
                    "the ambiguity of a full network partition — both nodes "
                    "would still independently and mistakenly conclude they "
                    "are the sole primary, just slightly faster."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Increase the number of standby replicas to five nodes "
                    "for additional redundancy"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Simply adding more passive replicas without "
                    "a quorum mechanism does not solve the split-brain "
                    "problem and could make the ambiguity worse if multiple "
                    "nodes lose contact with each other."
                ),
            },
        ],
        "explanation": (
            "A quorum or witness node is the standard architectural control "
            "for preventing split-brain conditions in a cluster during a "
            "network partition, since it provides the tie-breaking vote "
            "needed to ensure only one node becomes primary — something "
            "faster heartbeats or additional replicas alone cannot achieve."
        ),
    },
    # ------------------------------------------------------------------ #
    # Multi-cloud and platform diversity (3.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3b-035",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Multi-cloud and platform diversity",
        "stem": (
            "After a competitor's website became completely unreachable for "
            "several hours because its sole DNS provider suffered an outage, "
            "a company's architecture team decides its primary and secondary "
            "authoritative DNS service should be hosted with two different, "
            "unrelated DNS providers rather than two servers from the same "
            "provider. Which principle does this decision reflect?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Platform diversity — using unrelated vendors for a "
                    "critical function so a single provider's platform-wide "
                    "outage or vulnerability cannot take down the entire "
                    "service"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Platform diversity intentionally spreads a "
                    "critical function like DNS across unrelated vendors so "
                    "that one provider's outage, bug, or vulnerability "
                    "cannot simultaneously affect every instance of the "
                    "service."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Redundant power feeds, ensuring DNS servers remain "
                    "powered during a utility outage"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Power resilience addresses electrical supply "
                    "to physical equipment; it has nothing to do with "
                    "choosing unrelated DNS service providers."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Data classification, ensuring DNS records are labeled "
                    "according to sensitivity"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Data classification concerns labeling data "
                    "by sensitivity for handling purposes, which is unrelated "
                    "to selecting diverse infrastructure vendors for "
                    "resilience."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Tokenization, substituting DNS records with non-"
                    "sensitive surrogate values"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Tokenization protects sensitive data values; "
                    "it is not applicable to DNS resolution infrastructure "
                    "or vendor selection decisions."
                ),
            },
        ],
        "explanation": (
            "Deliberately using unrelated vendors for a critical function so "
            "that no single provider's outage can take down the entire "
            "service is the platform diversity principle, distinct from "
            "power resilience, data classification, or tokenization."
        ),
    },
    # ------------------------------------------------------------------ #
    # Power resilience (3.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3b-036",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Power resilience",
        "stem": (
            "A data center's local utility grid produces frequent, brief "
            "voltage sags and surges throughout the day — never a full "
            "outage — that are gradually degrading sensitive server power "
            "supplies. A standby (offline) UPS has a small switchover delay "
            "before it engages its battery, during which the sag or surge "
            "still briefly reaches connected equipment. Which power control "
            "is MOST appropriate?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A double-conversion (online) UPS that continuously "
                    "conditions all incoming power rather than switching over "
                    "only when a problem is detected"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A double-conversion UPS continuously rectifies "
                    "and re-inverts all incoming power, providing constant "
                    "conditioning with no switchover gap — directly "
                    "addressing frequent brief sags and surges that a "
                    "standby UPS's switchover delay would otherwise let "
                    "through."
                ),
            },
            {
                "id": "b",
                "text": (
                    "A diesel generator sized for extended runtime, sized to "
                    "handle multi-day outages"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A generator addresses sustained full outages "
                    "and takes time to start; it does nothing to smooth out "
                    "frequent brief voltage sags and surges that never "
                    "amount to a full utility failure."
                ),
            },
            {
                "id": "c",
                "text": (
                    "A basic surge protector strip installed at each server "
                    "rack"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A simple surge protector offers only minimal "
                    "transient protection and does nothing to condition "
                    "power during voltage sags, which require active "
                    "regulation rather than passive surge clamping alone."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The existing standby (offline) UPS, since its battery "
                    "already provides backup power during any power event"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario states the standby UPS's brief "
                    "switchover delay still lets the sag or surge reach "
                    "equipment before the battery engages, which is exactly "
                    "the ongoing damage the online UPS design eliminates."
                ),
            },
        ],
        "explanation": (
            "For frequent brief power-quality problems like sags and surges "
            "rather than full outages, a double-conversion (online) UPS that "
            "continuously conditions power outperforms a standby UPS's "
            "switchover-delay design, a generator meant for sustained "
            "outages, or a basic surge protector."
        ),
    },
    # ------------------------------------------------------------------ #
    # Recovery sites (3.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3b-037",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Recovery sites",
        "stem": (
            "A small nonprofit with virtually no IT budget runs nearly "
            "identical infrastructure and software to a sister nonprofit in "
            "another city. The two organizations agree to host each other's "
            "small set of non-critical systems if either suffers a disaster, "
            "accepting the uncertainty of relying on a partner's goodwill and "
            "available capacity in exchange for essentially no ongoing cost. "
            "Which recovery site strategy does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A reciprocal (mutual aid) agreement between the two "
                    "organizations"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A reciprocal agreement is the low/no-cost "
                    "recovery strategy where two similarly equipped "
                    "organizations agree to host each other's systems during "
                    "a disaster, explicitly accepting reliability uncertainty "
                    "in exchange for minimal cost — matching this nonprofit's "
                    "budget constraint exactly."
                ),
            },
            {
                "id": "b",
                "text": "A dedicated warm site leased and maintained by the nonprofit",
                "correct": False,
                "rationale": (
                    "Incorrect. A warm site requires ongoing lease and "
                    "infrastructure costs that a nonprofit with virtually no "
                    "IT budget could not sustain, making it a poor fit here."
                ),
            },
            {
                "id": "c",
                "text": "A fully redundant hot site with continuous synchronization",
                "correct": False,
                "rationale": (
                    "Incorrect. A hot site is the most expensive recovery "
                    "option and is entirely impractical given the nonprofit's "
                    "essentially nonexistent IT budget."
                ),
            },
            {
                "id": "d",
                "text": (
                    "A cold site purchased and equipped independently by the "
                    "nonprofit"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Even a cold site requires procuring and "
                    "maintaining dedicated facility space and eventual "
                    "hardware costs, which still exceeds what the scenario "
                    "describes as available, unlike the essentially free "
                    "reciprocal arrangement."
                ),
            },
        ],
        "explanation": (
            "A reciprocal (mutual aid) agreement is the standard recovery "
            "strategy for organizations with minimal budget that are willing "
            "to accept reliability uncertainty in exchange for near-zero "
            "ongoing cost, unlike warm, hot, or independently maintained cold "
            "sites, which all require dedicated investment."
        ),
    },
    {
        "id": "nd3b-038",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Recovery sites",
        "stem": (
            "A cloud-native company wants its disaster recovery strategy to "
            "keep only the minimal core infrastructure — such as a "
            "continuously replicated database — running in a secondary cloud "
            "region at low ongoing cost, with the ability to rapidly "
            "provision and scale up the full application stack around that "
            "core only if a disaster is formally declared. Which DR strategy "
            "does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Pilot light",
                "correct": True,
                "rationale": (
                    "Correct. A pilot light strategy keeps only the minimal "
                    "core components (such as replicated data) running "
                    "continuously in the DR environment at low cost, "
                    "allowing the rest of the stack to be rapidly scaled up "
                    "around that core when a disaster is declared."
                ),
            },
            {
                "id": "b",
                "text": "Multi-site active-active",
                "correct": False,
                "rationale": (
                    "Incorrect. Active-active runs the full application "
                    "stack live in both regions simultaneously at all times, "
                    "which is far more costly than keeping only a minimal "
                    "core running as described."
                ),
            },
            {
                "id": "c",
                "text": "Cold site",
                "correct": False,
                "rationale": (
                    "Incorrect. A cold site provides basic facility and "
                    "connectivity with no pre-installed data or systems "
                    "running at all, unlike the continuously replicated core "
                    "component described in the scenario."
                ),
            },
            {
                "id": "d",
                "text": "Warm standby with a full, but idle, duplicate application stack",
                "correct": False,
                "rationale": (
                    "Incorrect. A full warm standby duplicate stack that "
                    "remains idle costs significantly more to maintain than "
                    "keeping only the minimal core (like a replicated "
                    "database) running, which is the specific low-cost "
                    "approach described."
                ),
            },
        ],
        "explanation": (
            "Pilot light is the cloud DR strategy that keeps only essential "
            "core components continuously running at minimal cost, enabling "
            "rapid scale-up of the full stack around that core during a "
            "declared disaster — distinct from the higher-cost active-active "
            "or full warm standby models, and the much slower cold site."
        ),
    },
    # ------------------------------------------------------------------ #
    # Resilience testing (3.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3b-039",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Resilience testing",
        "stem": (
            "A disaster recovery program includes two additional validation "
            "activities: (1) the DR site processes a live copy of production "
            "data concurrently with the primary site, with results compared "
            "for accuracy, but user traffic is never actually cut over to it; "
            "and (2) a mock ransomware payload is technically detonated "
            "inside an isolated, non-production sandbox clone of the "
            "environment to test detection and containment tooling. Which "
            "TWO resilience testing types are being described, respectively? "
            "(Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Parallel test",
                "correct": True,
                "rationale": (
                    "Correct. A parallel test runs the DR environment "
                    "alongside production using live data for comparison "
                    "without ever cutting live user traffic over to it — "
                    "matching activity 1."
                ),
            },
            {
                "id": "b",
                "text": "Simulation test",
                "correct": True,
                "rationale": (
                    "Correct. A simulation test technically injects a mock "
                    "incident into an isolated, non-production copy of the "
                    "environment to validate detection and response tooling "
                    "— matching activity 2."
                ),
            },
            {
                "id": "c",
                "text": "Tabletop exercise",
                "correct": False,
                "rationale": (
                    "Incorrect. A tabletop exercise is a purely discussion-"
                    "based walkthrough with no live systems, data "
                    "processing, or technical injection involved, matching "
                    "neither described activity."
                ),
            },
            {
                "id": "d",
                "text": "Full failover (live) test",
                "correct": False,
                "rationale": (
                    "Incorrect. A full failover test actually cuts live "
                    "production traffic over to the secondary site, which "
                    "activity 1 explicitly states does not happen."
                ),
            },
            {
                "id": "e",
                "text": (
                    "Checklist review, where teams individually confirm "
                    "document currency without technical testing"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A checklist review is a passive document "
                    "check with no live data processing or technical "
                    "injection, matching neither described activity."
                ),
            },
        ],
        "explanation": (
            "Parallel tests validate DR output against live production data "
            "without cutting traffic over, while simulation tests technically "
            "inject a mock incident into an isolated non-production copy — "
            "distinct from tabletop exercises, full failover tests, or "
            "passive checklist reviews, which represent different levels of "
            "technical rigor."
        ),
    },
    # ------------------------------------------------------------------ #
    # Third-party agreement types (3.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3b-040",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Third-party agreement types",
        "stem": (
            "A company is contracting with a SaaS vendor and needs a "
            "document that legally obligates the vendor to specific, "
            "measurable uptime and incident-response-time commitments, with "
            "defined service credits or penalties if those metrics are not "
            "met. Which agreement type BEST fulfills this need?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Service level agreement (SLA)",
                "correct": True,
                "rationale": (
                    "Correct. An SLA is the document specifically designed "
                    "to define measurable performance metrics, such as "
                    "uptime and response times, along with penalties or "
                    "credits for failing to meet them."
                ),
            },
            {
                "id": "b",
                "text": "Master service agreement (MSA)",
                "correct": False,
                "rationale": (
                    "Incorrect. An MSA establishes the overall legal "
                    "framework and general terms governing the business "
                    "relationship (such as payment terms, liability, and "
                    "confidentiality), but it typically does not itself "
                    "specify measurable performance metrics — those are "
                    "usually defined in an accompanying SLA."
                ),
            },
            {
                "id": "c",
                "text": "Memorandum of understanding (MOU)",
                "correct": False,
                "rationale": (
                    "Incorrect. An MOU documents mutual intent and general "
                    "goals between parties but is typically non-binding and "
                    "does not define enforceable, measurable performance "
                    "metrics with penalties."
                ),
            },
            {
                "id": "d",
                "text": "Non-disclosure agreement (NDA)",
                "correct": False,
                "rationale": (
                    "Incorrect. An NDA protects confidential information "
                    "exchanged between parties; it does not address service "
                    "performance metrics or uptime commitments at all."
                ),
            },
        ],
        "explanation": (
            "An SLA is the agreement type purpose-built to define "
            "measurable performance commitments and associated penalties, "
            "distinct from an MSA's broader governing framework, a "
            "non-binding MOU, or a confidentiality-focused NDA."
        ),
    },
]

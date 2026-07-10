"""CompTIA Security+ (SY0-701) practice question bank — Domain 3, file F.

42 scenario-driven questions (38 multiple_choice + 4 multiple_response)
covering every study_topic label listed under domain 3 in
``_topic_labels.json``.
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
            "A regional insurance company's claims-processing platform runs on "
            "physical servers purchased outright and housed in a company-owned "
            "data center. Leadership is evaluating a migration to a cloud IaaS "
            "provider. Which trade-off BEST supports migrating to the cloud model?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Cloud IaaS lets the company convert a large capital "
                    "expenditure into an elastic operating expense and rapidly "
                    "provision additional compute during claims surges, such as "
                    "after a hurricane, at the cost of reduced direct control "
                    "over the underlying hardware"
                ),
                "correct": True,
                "rationale": (
                    "Correct. This is the classic cost/elasticity trade-off "
                    "cloud IaaS offers over owned hardware: rapid, on-demand "
                    "scaling during demand spikes in exchange for less direct "
                    "control of the physical infrastructure."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Owning physical servers outright provides stronger "
                    "long-term cost predictability with no dependency on a "
                    "third party"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is a genuine advantage of staying "
                    "on-premises, not an argument for migrating to the cloud, "
                    "so it does not support the decision being evaluated."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Cloud IaaS eliminates the company's responsibility for "
                    "patching and securing the guest operating system"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Under the IaaS shared responsibility model the "
                    "customer still patches and secures the guest OS; the "
                    "provider is responsible only for the underlying hardware, "
                    "virtualization layer, and facilities."
                ),
            },
            {
                "id": "d",
                "text": (
                    "On-premises hardware provides better elasticity to handle "
                    "sudden spikes in claims volume after a natural disaster"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This reverses the actual advantage — rapid "
                    "elastic scaling is a hallmark benefit of cloud "
                    "infrastructure, not fixed, self-owned hardware."
                ),
            },
        ],
        "explanation": (
            "Migrating to cloud IaaS trades reduced direct hardware control for "
            "elastic, on-demand capacity and converts capital expense into "
            "operating expense — the opposite claims (patch-free OS, superior "
            "on-prem elasticity, on-prem cost predictability as a migration "
            "driver) misstate the shared responsibility model or the actual "
            "direction of the trade-off."
        ),
    },
    {
        "id": "nd3f-002",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Architecture trade-offs",
        "stem": (
            "A hospital's radiology PACS (picture archiving and communication "
            "system) vendor has certified the application to run only on an "
            "end-of-life operating system version. Replacing the OS would void "
            "the vendor's support contract, but the OS no longer receives "
            "security patches. Which statement BEST describes the architectural "
            "trade-off the hospital is making by continuing to run the "
            "certified but unpatched configuration?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The hospital is trading patch availability and increased "
                    "vulnerability exposure for continued vendor-supported "
                    "functionality of a clinically critical system"
                ),
                "correct": True,
                "rationale": (
                    "Correct. This is precisely the trade-off described: "
                    "keeping vendor certification and support means forgoing "
                    "security patches, increasing the system's vulnerability "
                    "exposure over time."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Running an end-of-life OS improves system responsiveness "
                    "because fewer background patching processes compete for "
                    "resources"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Any marginal performance benefit from skipping "
                    "patch cycles is not the relevant trade-off; the real "
                    "consequence is accumulating unpatched vulnerabilities on a "
                    "system that stores protected health information."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The hospital eliminates ease-of-recovery concerns because "
                    "the vendor guarantees rollback support for the certified "
                    "configuration"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Vendor certification of an OS version is not "
                    "the same as a recovery or rollback guarantee, and the "
                    "scenario states nothing about such a guarantee."
                ),
            },
            {
                "id": "d",
                "text": (
                    "This is purely a cost trade-off, since compliance "
                    "requirements do not apply to medical imaging systems"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. PACS systems store protected health "
                    "information and are squarely within HIPAA's scope, so "
                    "compliance exposure is very much part of the risk, not "
                    "purely a cost issue."
                ),
            },
        ],
        "explanation": (
            "Vendor-certified but unpatchable software is a recurring "
            "architecture trade-off: functionality and support continuity "
            "purchased at the price of growing, unremediated vulnerability "
            "exposure on a system that also carries regulatory data-protection "
            "obligations."
        ),
    },
    # ------------------------------------------------------------------ #
    # Cloud architecture (3.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3f-003",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Cloud architecture",
        "stem": (
            "A finance team provisions new virtual machines for month-end "
            "batch processing directly through a cloud provider's self-service "
            "portal, without submitting a request to the IT provisioning team "
            "or waiting for human approval. Which NIST-defined essential "
            "characteristic of cloud computing does this MOST directly "
            "represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "On-demand self-service",
                "correct": True,
                "rationale": (
                    "Correct. On-demand self-service is the NIST characteristic "
                    "describing a consumer's ability to unilaterally provision "
                    "computing capabilities without requiring human interaction "
                    "with the provider."
                ),
            },
            {
                "id": "b",
                "text": "Resource pooling",
                "correct": False,
                "rationale": (
                    "Incorrect. Resource pooling describes the provider serving "
                    "multiple tenants from a shared pool of physical resources; "
                    "it does not describe the finance team's ability to "
                    "provision without submitting a request."
                ),
            },
            {
                "id": "c",
                "text": "Rapid elasticity",
                "correct": False,
                "rationale": (
                    "Incorrect. Rapid elasticity refers to resources scaling up "
                    "or down automatically to match demand; the scenario "
                    "describes a manual provisioning request, not automatic "
                    "scaling."
                ),
            },
            {
                "id": "d",
                "text": "Measured service",
                "correct": False,
                "rationale": (
                    "Incorrect. Measured service refers to usage being "
                    "metered and billed transparently; it does not describe "
                    "the self-service provisioning workflow in the scenario."
                ),
            },
        ],
        "explanation": (
            "The scenario describes a user directly requesting resources with "
            "no human approval step — the textbook definition of on-demand "
            "self-service, distinct from resource pooling, elasticity, or "
            "metering."
        ),
    },
    {
        "id": "nd3f-004",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Cloud architecture",
        "stem": (
            "A development team deploys its application to a managed "
            "platform-as-a-service (PaaS) offering, where the cloud provider "
            "automatically patches the underlying operating system, runtime, "
            "and container orchestration layer. Under the PaaS shared "
            "responsibility model, which task remains the CUSTOMER's "
            "responsibility?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Securing the application code, configuring authentication "
                    "and authorization logic, and protecting the data the "
                    "application processes"
                ),
                "correct": True,
                "rationale": (
                    "Correct. In PaaS, the provider manages the platform "
                    "beneath the application, but the customer always remains "
                    "responsible for the application layer: code, access "
                    "control logic, and data."
                ),
            },
            {
                "id": "b",
                "text": "Patching the guest operating system kernel",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario explicitly states the provider "
                    "patches the OS in this PaaS offering; this would only be "
                    "the customer's job under an IaaS model."
                ),
            },
            {
                "id": "c",
                "text": "Maintaining the container orchestration control plane",
                "correct": False,
                "rationale": (
                    "Incorrect. The provider manages the orchestration layer "
                    "in a PaaS offering, per the scenario, so this is not the "
                    "customer's responsibility here."
                ),
            },
            {
                "id": "d",
                "text": "Replacing failed physical storage hardware",
                "correct": False,
                "rationale": (
                    "Incorrect. Physical hardware maintenance is always the "
                    "cloud provider's responsibility in any cloud service "
                    "model, including PaaS."
                ),
            },
        ],
        "explanation": (
            "PaaS shifts OS, runtime, and orchestration responsibility to the "
            "provider, but application code, identity/access logic, and data "
            "protection always remain the customer's responsibility regardless "
            "of service model."
        ),
    },
    # ------------------------------------------------------------------ #
    # ICS/SCADA and embedded systems (3.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3f-005",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "ICS/SCADA and embedded systems",
        "stem": (
            "A semiconductor fabrication plant's industrial control system "
            "(ICS) network is air-gapped from the corporate IT network to "
            "protect fragile, timing-sensitive wafer-processing PLCs. "
            "Engineers periodically need to load new recipe files onto the "
            "PLCs using an engineering workstation. Which practice BEST "
            "maintains the air gap's security benefit while still allowing "
            "recipe updates?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Transfer recipe files using a dedicated, single-purpose "
                    "media-transfer workstation that scans removable media for "
                    "malware before any file crosses into the ICS network"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A dedicated, scanned transfer station lets "
                    "necessary data cross the boundary in a controlled, "
                    "inspected way without creating a persistent network path "
                    "into the isolated ICS segment."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Install a permanent VPN tunnel between the corporate "
                    "network and the ICS network so engineers can transfer "
                    "files directly"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A permanent tunnel defeats the entire purpose "
                    "of the air gap by creating a continuous network path from "
                    "corporate IT into the sensitive ICS environment."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Allow engineers to connect personal laptops directly to "
                    "the PLC network temporarily during update windows"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Unmanaged personal laptops are an unvetted, "
                    "high-risk vector for introducing malware directly into "
                    "the isolated PLC network."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Configure the ICS firewall to allow only outbound "
                    "connections from the PLC network to corporate file shares"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Any persistent firewall rule connecting the "
                    "two networks reintroduces exactly the kind of network "
                    "path the air gap was designed to eliminate, regardless of "
                    "directionality."
                ),
            },
        ],
        "explanation": (
            "A single-purpose, malware-scanning transfer workstation preserves "
            "an air gap's isolation while still allowing controlled, "
            "inspected data movement — unlike permanent tunnels, unmanaged "
            "personal devices, or firewall rules that reconnect the two "
            "networks."
        ),
    },
    # ------------------------------------------------------------------ #
    # IoT security (3.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3f-006",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "IoT security",
        "stem": (
            "A farming cooperative deploys 500 soil-moisture IoT sensors "
            "across several fields. An assessment finds that all sensors ship "
            "with the same hardcoded administrative password, communicate "
            "over unencrypted Wi-Fi, and cannot receive firmware updates after "
            "installation. Which limitation is the MOST fundamental barrier to "
            "remediating this deployment's security long-term?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The devices lack any firmware-update mechanism, so "
                    "vulnerabilities discovered after deployment — including "
                    "the hardcoded password — can never be patched in place "
                    "and require full hardware replacement"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Without any update path, no future vulnerability "
                    "can be remediated in place; this makes the lack of a "
                    "firmware-update mechanism the root barrier, since it also "
                    "prevents ever fixing the hardcoded password issue."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The devices use unencrypted Wi-Fi, which can be fixed "
                    "simply by adding WPA3 support to the existing access "
                    "points"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is a real weakness but is comparatively "
                    "fixable and does not address the hardcoded password or "
                    "the total inability to patch the devices going forward."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The devices are physically distributed across open "
                    "fields, making them susceptible to theft"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Physical exposure is a real risk but is not "
                    "the most fundamental barrier to remediating the security "
                    "issues described; theft risk exists independently of "
                    "patchability."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The hardcoded password is identical across all units, "
                    "which increases the blast radius of any single "
                    "compromised sensor"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This correctly describes a consequence of the "
                    "shared password, but it is the lack of an update "
                    "mechanism that prevents that consequence from ever being "
                    "fixed."
                ),
            },
        ],
        "explanation": (
            "The inability to receive firmware updates is the root cause that "
            "makes every other finding — the hardcoded password, the shared "
            "credential blast radius — permanently unfixable without physical "
            "hardware replacement, a hallmark limitation of many low-cost IoT "
            "devices."
        ),
    },
    # ------------------------------------------------------------------ #
    # Microservices and containerization (3.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3f-007",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Microservices and containerization",
        "stem": (
            "A platform engineering team runs many mutually untrusted "
            "customers' containers on shared Kubernetes worker nodes. "
            "Standard Linux namespaces and cgroups provide isolation, but a "
            "proof-of-concept shows that a malicious container could exploit "
            "a kernel vulnerability to affect the host and neighboring "
            "containers, since all containers on a node share the same "
            "kernel. Which architectural change would MOST directly address "
            "this specific risk?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Replace the default container runtime with a sandboxed "
                    "runtime, such as gVisor or Kata Containers, that "
                    "isolates each container from the shared host kernel"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Sandboxed runtimes intercept syscalls or run "
                    "each container inside a lightweight VM, directly removing "
                    "the shared-kernel exposure that the proof-of-concept "
                    "exploited."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Enforce Kubernetes network policies to restrict "
                    "pod-to-pod traffic"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Network policies restrict lateral network "
                    "traffic between pods; they do nothing to prevent a kernel "
                    "exploit that bypasses the network entirely by attacking "
                    "the shared kernel directly."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Require signed container images from a trusted registry "
                    "before deployment"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Image signing is a supply-chain integrity "
                    "control that verifies image provenance; it does not "
                    "isolate a running container from the host kernel at "
                    "runtime."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Run vulnerability scans against container images before "
                    "deployment"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Pre-deployment scanning catches known CVEs in "
                    "image contents but does not add runtime isolation between "
                    "a container and the shared host kernel."
                ),
            },
        ],
        "explanation": (
            "A sandboxed/microVM-based container runtime directly removes the "
            "shared-kernel attack surface, whereas network policies, image "
            "signing, and vulnerability scanning address different concerns "
            "(lateral traffic, provenance, and known CVEs) and would not have "
            "stopped this kernel-level escape."
        ),
    },
    {
        "id": "nd3f-008",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Microservices and containerization",
        "stem": (
            "A container supply-chain review recommends hardening the way "
            "base images are sourced and consumed. Which THREE practices "
            "BEST reduce the risk that a compromised or tampered base image "
            "reaches production? (Select three.)"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Pin base images to a specific, immutable content digest "
                    "rather than a mutable tag such as \"latest\""
                ),
                "correct": True,
                "rationale": (
                    "Correct. Pinning to an immutable digest guarantees the "
                    "exact same, verified image content is used every time, "
                    "preventing silent substitution of a tampered image behind "
                    "a mutable tag."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Scan container images for known vulnerabilities as a "
                    "required gate in the CI/CD pipeline before publishing"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Mandatory vulnerability scanning before "
                    "publishing catches known-vulnerable or malicious "
                    "components before they reach production."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Require cryptographic signing of images and verify "
                    "signatures before allowing deployment"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Signature verification at deploy time ensures "
                    "only images from trusted, verified sources are ever "
                    "run, blocking tampered or unauthorized images."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Increase the number of running replicas of each "
                    "container to improve fault tolerance"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Replica count improves availability and fault "
                    "tolerance; it has no effect on whether the image content "
                    "running in those replicas is trustworthy."
                ),
            },
            {
                "id": "e",
                "text": "Enable verbose debug logging inside every running container",
                "correct": False,
                "rationale": (
                    "Incorrect. Verbose logging aids troubleshooting and can "
                    "even risk leaking secrets; it does not verify or protect "
                    "the integrity of the base image supply chain."
                ),
            },
            {
                "id": "f",
                "text": (
                    "Configure the container orchestrator to auto-restart any "
                    "container that crashes"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Auto-restart is a resilience feature for "
                    "handling crashes; it has no bearing on preventing a "
                    "tampered image from being deployed in the first place."
                ),
            },
        ],
        "explanation": (
            "Digest pinning, mandatory vulnerability scanning, and signature "
            "verification together close the paths by which a tampered base "
            "image could silently reach production, while replica counts, "
            "verbose logging, and auto-restart address availability or "
            "troubleshooting, not supply-chain integrity."
        ),
    },
    # ------------------------------------------------------------------ #
    # Serverless and cloud architecture (3.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3f-009",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Serverless and cloud architecture",
        "stem": (
            "A startup's public-facing API is implemented entirely as "
            "serverless functions that scale automatically and bill per "
            "invocation. An attacker discovers an unauthenticated endpoint "
            "and issues a massive volume of requests, driving the company's "
            "cloud bill up dramatically without ever taking the API offline. "
            "Which risk is this attack MOST specifically exploiting?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The unlimited automatic scaling of serverless functions "
                    "economically amplifies a request-flooding attack into a "
                    "\"denial of wallet\" event even though availability is "
                    "unaffected"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Because serverless platforms auto-scale and "
                    "bill per invocation, an attacker can keep the service "
                    "available while inflating costs enormously — the "
                    "well-known \"denial of wallet\" risk unique to this "
                    "billing/scaling model."
                ),
            },
            {
                "id": "b",
                "text": (
                    "A cold-start vulnerability in the function runtime that "
                    "allows arbitrary code execution"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Cold start refers to the latency of "
                    "initializing an idle function instance; it is a "
                    "performance characteristic, not a code-execution "
                    "vulnerability, and does not explain a billing spike."
                ),
            },
            {
                "id": "c",
                "text": (
                    "An insecure direct object reference in the function's "
                    "business logic"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. IDOR is an authorization flaw that exposes "
                    "unauthorized data by manipulating object references; "
                    "nothing in the scenario describes accessing unauthorized "
                    "data objects, only high-volume flooding."
                ),
            },
            {
                "id": "d",
                "text": (
                    "A misconfigured API gateway that fails to terminate TLS "
                    "correctly"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A TLS termination misconfiguration would "
                    "affect connection security, not explain a cost-driven "
                    "flooding attack against an unauthenticated endpoint."
                ),
            },
        ],
        "explanation": (
            "Serverless architectures' automatic, near-unlimited scaling "
            "combined with per-invocation billing creates a distinct "
            "\"denial of wallet\" risk: an attacker can flood an endpoint "
            "without causing an outage, instead inflating operating costs."
        ),
    },
    # ------------------------------------------------------------------ #
    # Virtualization and high availability (3.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3f-010",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Virtualization and high availability",
        "stem": (
            "A cloud hosting provider oversubscribes physical CPU cores "
            "across many tenant virtual machines on the same hypervisor host "
            "to maximize utilization. A customer reports that their VM's "
            "performance degrades unpredictably whenever other tenants on the "
            "same host run CPU-intensive batch jobs. Which term BEST "
            "describes the underlying architectural cause of this problem?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The \"noisy neighbor\" effect from CPU resource "
                    "contention in a multi-tenant, oversubscribed hypervisor "
                    "host"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Oversubscribed, shared physical CPU resources "
                    "mean one tenant's heavy workload can degrade another "
                    "co-located tenant's performance — the classic noisy "
                    "neighbor problem in multi-tenant virtualization."
                ),
            },
            {
                "id": "b",
                "text": (
                    "VM escape, allowing one tenant to access another "
                    "tenant's resources directly"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. VM escape describes a security breach where "
                    "code escapes VM isolation to access the hypervisor or "
                    "other VMs; the scenario describes performance "
                    "degradation from resource contention, not a breach."
                ),
            },
            {
                "id": "c",
                "text": (
                    "VM sprawl from uncontrolled provisioning of unused "
                    "virtual machines"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. VM sprawl refers to the proliferation of "
                    "unmanaged, forgotten virtual machines over time, not "
                    "performance contention between actively running tenant "
                    "workloads."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The hypervisor is a type 2 (hosted) hypervisor "
                    "introducing host OS overhead"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Commercial multi-tenant hosting providers "
                    "almost universally run type 1 (bare-metal) hypervisors, "
                    "and the described symptom is caused by CPU "
                    "oversubscription, not hypervisor type."
                ),
            },
        ],
        "explanation": (
            "CPU oversubscription in a shared, multi-tenant hypervisor "
            "produces the noisy neighbor effect, a distinct concept from VM "
            "escape (a security breach), VM sprawl (unmanaged proliferation), "
            "or hypervisor type overhead."
        ),
    },
    {
        "id": "nd3f-011",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Virtualization and high availability",
        "stem": (
            "A company's virtualization cluster is configured so that if a "
            "physical hypervisor host fails, the virtual machines that were "
            "running on it are automatically detected as down and restarted "
            "on other healthy hosts in the cluster within a few minutes, "
            "without administrator intervention. Which capability does this "
            "describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Host-level high availability (HA) clustering that "
                    "monitors host heartbeats and automatically restarts "
                    "affected VMs on other hosts"
                ),
                "correct": True,
                "rationale": (
                    "Correct. HA clustering is exactly this behavior: "
                    "detecting a failed host via heartbeat loss and "
                    "automatically restarting its VMs elsewhere, with a brief "
                    "restart-driven interruption."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Live migration that moves a running VM between hosts "
                    "with no service interruption"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Live migration is a planned, proactive "
                    "operation that moves a still-running VM with zero "
                    "downtime; it does not apply after a host has already "
                    "failed."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Fault tolerance providing a continuously mirrored, "
                    "zero-downtime shadow VM"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Fault tolerance keeps a live, lockstep "
                    "secondary instance running continuously so there is no "
                    "restart or downtime at all — a stricter guarantee than "
                    "the few-minutes restart described in the scenario."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Load balancing that distributes new connection requests "
                    "across multiple active VMs"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Load balancing distributes traffic among "
                    "already-running instances; it does not detect a failed "
                    "host or restart VMs that were running on it."
                ),
            },
        ],
        "explanation": (
            "Automatic detection of a failed host followed by restarting its "
            "VMs elsewhere is host-level HA clustering — distinct from live "
            "migration (proactive, zero-downtime), fault tolerance (continuous "
            "lockstep mirroring with no restart), and load balancing "
            "(distributing traffic among running instances)."
        ),
    },
    # ------------------------------------------------------------------ #
    # Attack surface reduction (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3f-012",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Attack surface reduction",
        "stem": (
            "An auditor finds that production servers built from a company's "
            "VM template have 15 optional operating system features and 6 "
            "listening services enabled that no application on those servers "
            "actually uses. Which action BEST reduces the attack surface of "
            "these servers?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Disable the unused optional features and stop the unused "
                    "listening services on each server"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Removing unnecessary features and services "
                    "eliminates code paths and open ports that serve no "
                    "business function but could otherwise be exploited, "
                    "directly reducing the attack surface."
                ),
            },
            {
                "id": "b",
                "text": "Deploy additional intrusion detection sensors to monitor the servers",
                "correct": False,
                "rationale": (
                    "Incorrect. Additional monitoring improves detection of "
                    "an attack after the fact; it does not reduce the number "
                    "of exploitable services and features actually exposed."
                ),
            },
            {
                "id": "c",
                "text": "Increase logging verbosity on the affected servers",
                "correct": False,
                "rationale": (
                    "Incorrect. More verbose logs aid investigation but do "
                    "not remove any unnecessary running services or features "
                    "from the attack surface."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Implement network segmentation to isolate the servers "
                    "from the rest of the network"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Segmentation limits the blast radius if these "
                    "servers are compromised, but it does not reduce the "
                    "number of unnecessary services and features exposed on "
                    "the servers themselves."
                ),
            },
        ],
        "explanation": (
            "Attack surface reduction means removing unneeded functionality "
            "— disabling unused features and services directly shrinks what "
            "an attacker can target, unlike detection, logging, or "
            "segmentation controls that address different layers of defense."
        ),
    },
    # ------------------------------------------------------------------ #
    # Change management workflow (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3f-013",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Change management workflow",
        "stem": (
            "An organization's change management policy defines three "
            "categories: standard (pre-approved, low-risk, repeatable), "
            "normal (requires case-by-case change advisory board review), and "
            "emergency (expedited approval after the fact). A system "
            "administrator wants to apply a routine, well-tested TLS "
            "certificate renewal that the organization performs monthly "
            "using a documented, repeatable procedure. Which change category "
            "is MOST appropriate?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Standard change, because it is a low-risk, pre-approved, "
                    "repeatable procedure that does not need case-by-case "
                    "board review"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A routine, well-tested, monthly procedure is "
                    "exactly the profile of a standard change: pre-approved "
                    "and repeatable, so it can be executed under the standing "
                    "authorization rather than re-reviewed every time."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Emergency change, because certificates must be renewed "
                    "quickly to avoid an outage"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The emergency category is for unplanned, "
                    "urgent changes needed to resolve an active incident; a "
                    "scheduled, routine monthly renewal is neither unplanned "
                    "nor urgent."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Normal change, requiring full change advisory board "
                    "review each time it recurs"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Requiring full board review for a well-"
                    "understood, low-risk, repeatable task is unnecessarily "
                    "inefficient and is exactly what the standard change "
                    "category exists to avoid."
                ),
            },
            {
                "id": "d",
                "text": (
                    "No change record is required because certificate "
                    "renewal is routine maintenance"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Even standard, pre-approved changes must "
                    "still be logged and tracked in the change management "
                    "system; \"routine\" does not mean undocumented."
                ),
            },
        ],
        "explanation": (
            "Standard changes exist precisely for low-risk, repeatable, "
            "pre-approved procedures like a routine certificate renewal, "
            "avoiding both the inefficiency of full board review and the "
            "mischaracterization of a scheduled task as an emergency, while "
            "still requiring documentation."
        ),
    },
    # ------------------------------------------------------------------ #
    # Failure modes (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3f-014",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Failure modes",
        "stem": (
            "An e-commerce checkout service calls a third-party fraud-scoring "
            "API before approving each transaction. During a scoring-API "
            "outage, transactions cannot be scored. The security team must "
            "decide whether the checkout service should fail open (approve "
            "transactions without a fraud score) or fail closed (decline all "
            "transactions) during the outage. For a retailer whose primary "
            "business risk is large-scale payment fraud losses rather than "
            "lost sales during brief outages, which configuration is MOST "
            "appropriate?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Fail closed — decline transactions during the outage, "
                    "because it prioritizes minimizing fraud losses over "
                    "transaction availability"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Given the stated priority of minimizing fraud "
                    "losses over short-term sales availability, failing "
                    "closed prevents unscored, potentially fraudulent "
                    "transactions from being approved during the outage."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Fail open — approve transactions during the outage, "
                    "because maintaining sales availability is always the "
                    "higher priority for e-commerce"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This directly contradicts the retailer's "
                    "stated risk priority, which is minimizing fraud losses, "
                    "not maximizing short-term transaction availability."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Fail open, but only for repeat customers with a prior "
                    "successful purchase history"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This still exposes the retailer to fraud "
                    "risk, since a repeat-customer account can itself be "
                    "compromised, and it does not actually resolve the "
                    "fail-open/fail-closed decision required during the "
                    "outage."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Load balance transactions across two independent "
                    "instances of the same third-party fraud-scoring API to "
                    "avoid a single point of failure"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is a redundancy improvement for the "
                    "future, but it does not address the immediate decision "
                    "of how the checkout service should behave right now "
                    "during the current outage."
                ),
            },
        ],
        "explanation": (
            "Fail-open versus fail-closed is a direct trade-off between "
            "availability and security; when fraud losses are the dominant "
            "business risk, failing closed during a scoring outage is the "
            "appropriate choice, not fail-open, a conditional fail-open "
            "workaround, or an unrelated redundancy fix."
        ),
    },
    {
        "id": "nd3f-015",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Failure modes",
        "stem": (
            "A company's public-facing domain resolves through a single "
            "third-party DNS hosting provider. When that provider suffered a "
            "regional outage, the company's website, API, and email became "
            "completely unreachable even though the company's own servers "
            "remained fully operational. Which architectural change BEST "
            "eliminates this single point of failure?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Configure secondary, redundant authoritative DNS hosting "
                    "with a second, independent DNS provider so records "
                    "remain resolvable if one provider fails"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Using two independent authoritative DNS "
                    "providers directly eliminates the single point of "
                    "failure that caused the outage, since queries can still "
                    "be resolved by the surviving provider."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Increase the TTL (time to live) value on all DNS "
                    "records so cached responses last longer during an outage"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Longer TTLs only delay impact for clients "
                    "that already have a cached response; new lookups and "
                    "expired caches still fail entirely during the outage, "
                    "so this does not fix the underlying single point of "
                    "failure."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Add more application servers behind the existing load "
                    "balancer"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The outage was caused by DNS resolution "
                    "failing, not by insufficient application server "
                    "capacity, so adding servers does not address the actual "
                    "cause."
                ),
            },
            {
                "id": "d",
                "text": "Purchase a wildcard TLS certificate for all subdomains",
                "correct": False,
                "rationale": (
                    "Incorrect. A wildcard certificate addresses TLS "
                    "coverage for subdomains and has no relationship to DNS "
                    "resolution availability."
                ),
            },
        ],
        "explanation": (
            "Relying on a single DNS provider is a classic single point of "
            "failure; secondary DNS with an independent provider eliminates "
            "it, while longer TTLs, more application servers, and TLS "
            "certificates all fail to address the root cause."
        ),
    },
    # ------------------------------------------------------------------ #
    # Firewalls (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3f-016",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Firewalls",
        "stem": (
            "A security architect notices that a traditional stateful "
            "firewall permits all outbound TCP/443 traffic, which "
            "unintentionally allows employees to use unsanctioned peer-to-"
            "peer file-sharing and remote-access tools that tunnel over "
            "HTTPS on port 443, indistinguishable from legitimate web "
            "browsing at the port/protocol level. Which firewall capability "
            "would MOST directly allow the organization to block the "
            "unwanted applications specifically while still permitting "
            "normal HTTPS web browsing?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A next-generation firewall (NGFW) with application-layer "
                    "identification and control that classifies and blocks "
                    "traffic by application signature, independent of port "
                    "number"
                ),
                "correct": True,
                "rationale": (
                    "Correct. NGFW application identification inspects "
                    "traffic content to determine the actual application in "
                    "use, allowing the firewall to distinguish and block the "
                    "unwanted tools even though they share port 443 with "
                    "legitimate browsing."
                ),
            },
            {
                "id": "b",
                "text": (
                    "A stateless packet-filtering firewall with additional "
                    "TCP/443 deny rules"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Blocking TCP/443 outright would also block "
                    "all legitimate HTTPS web browsing, since a port-based "
                    "rule cannot distinguish between the two types of traffic "
                    "sharing that port."
                ),
            },
            {
                "id": "c",
                "text": "A circuit-level gateway proxy",
                "correct": False,
                "rationale": (
                    "Incorrect. A circuit-level gateway validates session "
                    "handshake legitimacy at a lower layer; it does not "
                    "inspect application-layer content to identify the "
                    "specific application generating the traffic."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Increasing the stateful firewall's connection timeout "
                    "values"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Connection timeout settings control how long "
                    "idle sessions remain open; they have no bearing on "
                    "identifying or blocking specific applications."
                ),
            },
        ],
        "explanation": (
            "Only application-layer identification, a hallmark NGFW "
            "capability, can distinguish applications tunneling over the "
            "same port and protocol — port-based rules, circuit-level "
            "gateways, and timeout settings cannot make that distinction."
        ),
    },
    {
        "id": "nd3f-017",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Firewalls",
        "stem": (
            "After a phishing-compromised laptop was used to move laterally "
            "and infect a dozen other internal workstations on the same flat "
            "network, the incident review finds the organization relies "
            "exclusively on a single perimeter next-generation firewall "
            "(NGFW) at the internet edge, with no filtering between internal "
            "workstations. Which control would BEST have limited the lateral "
            "spread of this specific incident?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Host-based firewalls on each workstation combined with "
                    "internal network segmentation to restrict east-west "
                    "traffic between peer endpoints"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Because the compromise spread through internal, "
                    "east-west traffic between workstations, only "
                    "host-based firewalls and internal segmentation that "
                    "restrict peer-to-peer traffic could have contained the "
                    "spread."
                ),
            },
            {
                "id": "b",
                "text": "Upgrading the perimeter NGFW to a higher-throughput model",
                "correct": False,
                "rationale": (
                    "Incorrect. A perimeter firewall inspects north-south "
                    "traffic entering and leaving the network; a "
                    "higher-throughput model does nothing to filter traffic "
                    "moving between internal workstations."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Adding additional deny rules for outbound internet "
                    "traffic on the perimeter firewall"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The lateral spread occurred entirely inside "
                    "the network between workstations; outbound internet "
                    "rules at the perimeter have no effect on that internal "
                    "traffic."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Enabling TLS decryption and inspection on the perimeter "
                    "firewall for outbound HTTPS traffic"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. TLS inspection at the perimeter examines "
                    "traffic leaving the network to the internet, not "
                    "traffic that stays entirely inside the network between "
                    "workstations."
                ),
            },
        ],
        "explanation": (
            "A single perimeter firewall provides no visibility into "
            "east-west traffic between internal hosts; only host-based "
            "firewalls plus internal segmentation address lateral movement "
            "like the incident described, unlike upgrades or rule changes "
            "made only at the perimeter."
        ),
    },
    # ------------------------------------------------------------------ #
    # Network appliances (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3f-018",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network appliances",
        "stem": (
            "A media company's video-on-demand website experiences a "
            "massive volumetric DDoS attack that saturates its single data "
            "center's internet uplink, making the site completely "
            "unreachable even though the origin web servers themselves never "
            "became overloaded. Which network appliance/service deployment "
            "would MOST effectively prevent a recurrence of this specific "
            "failure?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A cloud-based content delivery network (CDN) with "
                    "distributed points of presence and built-in DDoS "
                    "scrubbing that absorbs volumetric traffic before it "
                    "reaches the single uplink"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A distributed CDN with DDoS scrubbing absorbs "
                    "volumetric traffic across many points of presence, "
                    "preventing the flood from ever concentrating on the "
                    "single saturated uplink."
                ),
            },
            {
                "id": "b",
                "text": (
                    "An additional internal load balancer distributing "
                    "traffic across more origin web servers"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The origin servers were never overloaded; "
                    "the failure was the uplink itself being saturated, "
                    "which an internal load balancer does nothing to "
                    "address."
                ),
            },
            {
                "id": "c",
                "text": (
                    "A host-based intrusion detection system (HIDS) on each "
                    "origin web server"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. HIDS detects host-level intrusions on "
                    "individual servers; it has no capability to mitigate a "
                    "network-layer volumetric flood saturating the uplink."
                ),
            },
            {
                "id": "d",
                "text": (
                    "A higher-throughput stateful firewall at the data "
                    "center edge"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A single stateful firewall at the same data "
                    "center still shares the same saturated uplink and can "
                    "itself become an additional bottleneck under a massive "
                    "volumetric flood."
                ),
            },
        ],
        "explanation": (
            "Only a geographically distributed CDN with dedicated DDoS "
            "scrubbing capacity addresses volumetric uplink saturation; "
            "internal load balancers, host-based IDS, and a single "
            "on-premises firewall all remain limited by the same saturated "
            "single-site uplink."
        ),
    },
    {
        "id": "nd3f-019",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network appliances",
        "stem": (
            "A company has dozens of internal microservices that each "
            "independently implement their own authentication, rate "
            "limiting, and request logging, leading to inconsistent security "
            "enforcement across the environment. Which network appliance "
            "deployment would MOST effectively centralize and standardize "
            "these cross-cutting security functions for all north-south API "
            "traffic entering the environment?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "An API gateway placed in front of all microservices to "
                    "centrally enforce authentication, rate limiting, and "
                    "logging policies"
                ),
                "correct": True,
                "rationale": (
                    "Correct. An API gateway is purpose-built to centralize "
                    "these cross-cutting concerns for incoming API traffic, "
                    "enforcing consistent policy in one place rather than in "
                    "each individual microservice."
                ),
            },
            {
                "id": "b",
                "text": "A host-based firewall on each microservice's container",
                "correct": False,
                "rationale": (
                    "Incorrect. A per-container host-based firewall still "
                    "requires separate configuration on each service and "
                    "does not centralize or standardize authentication, rate "
                    "limiting, or logging."
                ),
            },
            {
                "id": "c",
                "text": "A network tap mirroring traffic to a monitoring appliance",
                "correct": False,
                "rationale": (
                    "Incorrect. A network tap only provides passive traffic "
                    "visibility for monitoring; it cannot enforce "
                    "authentication or rate-limiting policy on live "
                    "requests."
                ),
            },
            {
                "id": "d",
                "text": "A layer 2 switch with port security enabled",
                "correct": False,
                "rationale": (
                    "Incorrect. A layer 2 switch operates far below the "
                    "application layer and has no capability to perform "
                    "API-level authentication, rate limiting, or logging."
                ),
            },
        ],
        "explanation": (
            "An API gateway is the network appliance designed to centralize "
            "cross-cutting API security functions, unlike per-container "
            "firewalls, passive taps, or layer 2 switches, none of which can "
            "enforce application-layer policy consistently."
        ),
    },
    # ------------------------------------------------------------------ #
    # Port security and 802.1X (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3f-020",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Port security and 802.1X",
        "stem": (
            "A company enforces 802.1X on every access-layer switchport, but "
            "a fleet of older network printers cannot run an 802.1X "
            "supplicant and therefore fail authentication and lose network "
            "connectivity when the policy is enabled. Which approach BEST "
            "allows these specific devices to connect securely without "
            "disabling 802.1X for the rest of the network?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Configure MAC authentication bypass (MAB) on the "
                    "printer ports as a fallback so devices without an "
                    "802.1X supplicant can still authenticate using their "
                    "known MAC address"
                ),
                "correct": True,
                "rationale": (
                    "Correct. MAB lets non-802.1X-capable devices "
                    "authenticate via a known MAC address through the same "
                    "RADIUS infrastructure, preserving centralized "
                    "authentication without disabling 802.1X elsewhere."
                ),
            },
            {
                "id": "b",
                "text": "Disable 802.1X enforcement globally across all access switchports",
                "correct": False,
                "rationale": (
                    "Incorrect. This removes port-based authentication "
                    "protection for the entire network to accommodate a "
                    "small number of devices, rather than targeting the fix "
                    "to only the affected printer ports."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Place the printers on the guest VLAN with restricted "
                    "internet-only access"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Printers typically need access to internal "
                    "print servers and users, not just the internet, and "
                    "this does not solve the underlying requirement for "
                    "authenticated network access."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Configure sticky port security with a static MAC "
                    "address allow-list on the printer ports instead of "
                    "802.1X"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Static sticky port security learns and "
                    "limits MAC addresses locally on the switch but lacks "
                    "the centralized, dynamic authentication and policy "
                    "assignment that MAB provides through the existing "
                    "RADIUS/802.1X infrastructure."
                ),
            },
        ],
        "explanation": (
            "MAC authentication bypass is the standard fallback for devices "
            "that cannot run an 802.1X supplicant, preserving centralized "
            "authentication for those ports rather than disabling 802.1X "
            "network-wide, isolating devices onto a mismatched VLAN, or "
            "relying on standalone static port security."
        ),
    },
    # ------------------------------------------------------------------ #
    # SDN and logical segmentation (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3f-021",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SDN and logical segmentation",
        "stem": (
            "In a software-defined networking (SDN) deployment, the "
            "centralized SDN controller communicates with switches using a "
            "southbound API (such as OpenFlow) to push forwarding rules, and "
            "with orchestration and management tools using a northbound "
            "API. A security review is MOST concerned about which risk that "
            "is unique to this centralized control-plane architecture?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Compromise of the SDN controller itself would give an "
                    "attacker the ability to reprogram forwarding behavior "
                    "across the entire network it manages, making the "
                    "controller a high-value, centralized target"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Because the controller centrally directs "
                    "forwarding behavior for all managed switches, "
                    "compromising it gives an attacker sweeping control over "
                    "the network — the defining centralized-control-plane "
                    "risk in SDN."
                ),
            },
            {
                "id": "b",
                "text": (
                    "SDN inherently encrypts all data-plane traffic between "
                    "switches by default, so the primary remaining risk is "
                    "physical cable tapping"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. SDN does not automatically encrypt "
                    "data-plane traffic between switches by default; this "
                    "misstates SDN's properties and understates the "
                    "controller compromise risk."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Southbound APIs are used only for network monitoring "
                    "and cannot modify forwarding behavior"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Southbound APIs like OpenFlow are precisely "
                    "how the controller pushes and modifies forwarding rules "
                    "to switches; they are not limited to passive "
                    "monitoring."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Because control and data planes are separated, a "
                    "compromised switch can independently reprogram the "
                    "entire network's forwarding rules"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This reverses SDN's architecture: switches "
                    "in SDN are relatively simple forwarders that follow "
                    "controller instructions, so a compromised switch cannot "
                    "independently reprogram the network the way a "
                    "compromised controller could."
                ),
            },
        ],
        "explanation": (
            "SDN's centralized control plane concentrates network-wide "
            "control in the controller, making its compromise the most "
            "consequential risk — unlike the other options, which either "
            "misstate SDN's encryption defaults, southbound API function, or "
            "reverse the controller/switch relationship."
        ),
    },
    {
        "id": "nd3f-022",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "SDN and logical segmentation",
        "stem": (
            "A retailer's cardholder-data workloads run as virtual machines "
            "that are frequently migrated between hosts by the orchestration "
            "platform, which assigns them new IP addresses after each "
            "migration. Traditional VLAN-based segmentation, which enforces "
            "policy based on static IP address ranges, breaks every time a "
            "workload migrates. Which approach BEST solves this specific "
            "problem?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Software-defined micro-segmentation that enforces "
                    "policy based on workload identity or tags rather than "
                    "static IP addresses, so rules follow the workload "
                    "automatically after migration"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Identity- or tag-based micro-segmentation ties "
                    "policy to the workload itself rather than a static IP "
                    "range, so protection follows the workload across "
                    "migrations without manual reconfiguration."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Assign a larger, single flat VLAN to all cardholder-"
                    "data workloads so IP changes never cross a VLAN "
                    "boundary"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This eliminates meaningful segmentation "
                    "entirely, worsening the security posture and violating "
                    "least privilege for cardholder data, rather than "
                    "solving the migration problem."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Disable dynamic migration for cardholder-data workloads "
                    "so IP addresses never change"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This sacrifices operational flexibility and "
                    "may not be feasible for maintenance or load balancing; "
                    "it works around the problem rather than solving policy "
                    "enforcement for a dynamic environment."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Configure static NAT mappings that translate every "
                    "workload back to the same fixed IP regardless of which "
                    "host it runs on"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is operationally fragile and does not "
                    "scale to frequent migrations, and it still does not "
                    "address policy enforcement directly tied to workload "
                    "identity."
                ),
            },
        ],
        "explanation": (
            "Identity-based micro-segmentation decouples policy from "
            "static IP addressing, directly solving the problem of policy "
            "breaking on migration — unlike flattening the VLAN, freezing "
            "migrations, or fragile static NAT workarounds."
        ),
    },
    # ------------------------------------------------------------------ #
    # Secure communication (VPN/TLS/IPSec) (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3f-023",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Secure communication (VPN/TLS/IPSec)",
        "stem": (
            "Two servers within the same data center need to encrypt "
            "traffic exchanged directly between each other using IPSec, "
            "without needing to encapsulate and route traffic through a "
            "gateway, since both endpoints are the actual communicating "
            "hosts. Which IPSec mode is MOST appropriate for this "
            "host-to-host scenario, and why?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Transport mode, because it encrypts only the payload of "
                    "each IP packet while leaving the original IP header "
                    "intact, which is efficient for direct host-to-host "
                    "communication"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Transport mode is designed for direct "
                    "end-to-end communication between the actual "
                    "communicating hosts, encrypting only the payload rather "
                    "than adding gateway encapsulation overhead."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Tunnel mode, because it encrypts the entire original IP "
                    "packet and encapsulates it inside a new packet, which "
                    "is designed for gateway-to-gateway site-to-site "
                    "connections"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Tunnel mode is a real IPSec mode, but it is "
                    "purpose-built for gateway-to-gateway site-to-site VPNs, "
                    "not for direct host-to-host traffic where the "
                    "communicating hosts are the endpoints themselves."
                ),
            },
            {
                "id": "c",
                "text": (
                    "IKEv1 aggressive mode, because it completes the key "
                    "exchange in fewer round trips"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Aggressive mode is a key-exchange "
                    "negotiation option, not a data-encapsulation mode, and "
                    "it is also considered less secure because it exposes "
                    "identity information during negotiation."
                ),
            },
            {
                "id": "d",
                "text": (
                    "ESP in null-encryption mode, because authentication "
                    "alone is sufficient for internal data center traffic"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Null encryption provides authentication and "
                    "integrity but no confidentiality, leaving the traffic "
                    "exposed, which does not meet the implied requirement to "
                    "encrypt the traffic."
                ),
            },
        ],
        "explanation": (
            "IPSec transport mode is designed for direct host-to-host "
            "encryption between the actual communicating endpoints, while "
            "tunnel mode fits gateway-to-gateway VPNs, aggressive mode is a "
            "key-exchange option rather than a data mode, and null "
            "encryption provides no confidentiality."
        ),
    },
    {
        "id": "nd3f-024",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Secure communication (VPN/TLS/IPSec)",
        "stem": (
            "A mobile banking app's engineering team wants to ensure that "
            "even if an attacker installs a rogue root certificate authority "
            "(CA) on a customer's compromised or jailbroken device and "
            "performs a machine-in-the-middle proxy, the app will still "
            "refuse to trust the attacker's forged TLS certificate for the "
            "bank's API domain. Which technique BEST achieves this?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Certificate pinning, which hardcodes the expected "
                    "certificate or public key in the app so it rejects any "
                    "certificate not matching the pin, even one issued by a "
                    "trusted root CA"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Certificate pinning validates the server "
                    "certificate against a pinned value baked into the app, "
                    "so it will reject a forged certificate even if that "
                    "certificate chains to a rogue CA the device has been "
                    "tricked into trusting."
                ),
            },
            {
                "id": "b",
                "text": "Enabling TLS 1.3 instead of TLS 1.2 for all API connections",
                "correct": False,
                "rationale": (
                    "Incorrect. A newer TLS version improves cipher strength "
                    "and handshake privacy, but it does not prevent a device "
                    "from trusting an attacker-installed rogue root CA."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Using OCSP stapling to check the certificate's "
                    "revocation status"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. OCSP stapling checks whether an otherwise-"
                    "trusted certificate has been revoked; it does not stop "
                    "a device from trusting a rogue root CA in the first "
                    "place."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Enforcing mutual TLS so the server also authenticates "
                    "the client's certificate"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Mutual TLS protects the server from "
                    "unauthorized clients, but it does not stop the client "
                    "app from trusting a forged server certificate signed by "
                    "a rogue installed CA."
                ),
            },
        ],
        "explanation": (
            "Certificate pinning is the technique specifically designed to "
            "defeat rogue-CA-based interception by validating against a "
            "known-good certificate or key rather than trusting any "
            "certificate the device's trust store accepts — TLS version, "
            "OCSP stapling, and mutual TLS all address different threats."
        ),
    },
    # ------------------------------------------------------------------ #
    # Zero Trust / SASE (3.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3f-025",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Zero Trust / SASE",
        "stem": (
            "A company's Zero Trust architecture continuously evaluates "
            "device posture signals — patch level, disk encryption status, "
            "and EDR agent health — even after a user has been granted "
            "access to a resource. Thirty minutes into an authenticated "
            "session, a user's laptop reports that its disk encryption was "
            "disabled. The policy engine immediately terminates the user's "
            "active session to the sensitive file share. Which Zero Trust "
            "principle does this behavior MOST directly demonstrate?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Continuous, adaptive evaluation of trust rather than a "
                    "one-time authentication decision, allowing access to be "
                    "revoked in real time when risk posture changes "
                    "mid-session"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Zero Trust treats trust as continuously "
                    "re-evaluated rather than granted once at login; the "
                    "scenario shows exactly this — a posture change during "
                    "an active session triggers immediate revocation."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The principle of least privilege, which limits a "
                    "user's access to only the minimum resources needed for "
                    "their role"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Least privilege concerns the scope of access "
                    "granted, not the ongoing, real-time re-evaluation of an "
                    "already-granted session that the scenario describes."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Micro-segmentation, which restricts lateral movement "
                    "between network segments"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Micro-segmentation is a network-layer "
                    "isolation control; it does not explain the policy "
                    "engine's real-time reaction to a posture-signal change "
                    "mid-session."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Multi-factor authentication, which requires more than "
                    "one credential type at login"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. MFA strengthens the initial authentication "
                    "event; it does not by itself explain a mid-session "
                    "revocation triggered by a later change in device "
                    "posture."
                ),
            },
        ],
        "explanation": (
            "Continuous, adaptive trust evaluation — not a one-time login "
            "decision — is what allows a Zero Trust policy engine to revoke "
            "an active session the moment risk posture changes, distinct "
            "from least privilege, micro-segmentation, or MFA."
        ),
    },
    {
        "id": "nd3f-026",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Zero Trust / SASE",
        "stem": (
            "A security architect is designing a SASE (Secure Access "
            "Service Edge) rollout to replace branch office MPLS circuits "
            "and site-to-site VPNs. Which THREE capabilities are core, "
            "cloud-delivered components that SASE converges into a single "
            "platform? (Select three.)"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "SD-WAN for intelligent, application-aware routing of "
                    "branch traffic"
                ),
                "correct": True,
                "rationale": (
                    "Correct. SD-WAN is one of the core networking "
                    "components SASE converges to intelligently route branch "
                    "traffic, often replacing costly dedicated circuits."
                ),
            },
            {
                "id": "b",
                "text": (
                    "A cloud-delivered secure web gateway (SWG) for "
                    "inspecting and filtering web traffic"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A cloud-delivered SWG is a core SASE security "
                    "component that inspects and filters web traffic from "
                    "any location without requiring on-premises hardware."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Zero Trust Network Access (ZTNA) for identity- and "
                    "context-based access to applications"
                ),
                "correct": True,
                "rationale": (
                    "Correct. ZTNA is a core SASE component that grants "
                    "application access based on identity and context "
                    "rather than network location, replacing traditional "
                    "VPN access."
                ),
            },
            {
                "id": "d",
                "text": (
                    "A dedicated MPLS circuit purchased from a telecom "
                    "carrier for each branch"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. SASE is specifically positioned to reduce or "
                    "replace dependency on costly dedicated MPLS circuits, "
                    "not to converge them as a core component."
                ),
            },
            {
                "id": "e",
                "text": (
                    "A physical firewall appliance shipped to and racked at "
                    "every branch office"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. SASE shifts security enforcement to the "
                    "cloud edge rather than requiring dedicated hardware "
                    "appliances at every branch location."
                ),
            },
            {
                "id": "f",
                "text": (
                    "A locally hosted RADIUS server at each branch for "
                    "Wi-Fi authentication"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. SASE centralizes and cloud-delivers policy "
                    "enforcement rather than requiring standalone local "
                    "infrastructure at each branch."
                ),
            },
        ],
        "explanation": (
            "SASE converges SD-WAN, a cloud-delivered SWG, and ZTNA into a "
            "single cloud platform, specifically to reduce dependence on "
            "dedicated circuits and per-branch hardware, not to converge "
            "those legacy components themselves."
        ),
    },
    # ------------------------------------------------------------------ #
    # Data classification (3.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3f-027",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Data classification",
        "stem": (
            "A company deploys an automated data classification tool that "
            "scans documents and emails, then applies sensitivity labels "
            "(Public, Internal, Confidential, Restricted) based on detected "
            "content patterns such as national ID numbers and financial "
            "account numbers. Once the \"Restricted\" label is applied to a "
            "file, it automatically triggers encryption, disables external "
            "sharing, and restricts printing. Which statement BEST describes "
            "the security value of this labeling scheme?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The classification label acts as metadata that drives "
                    "automated enforcement of handling controls proportional "
                    "to the data's sensitivity, without relying on manual "
                    "user judgment for every file"
                ),
                "correct": True,
                "rationale": (
                    "Correct. This is exactly the value shown: the label "
                    "itself is metadata that automatically triggers "
                    "appropriate technical controls, removing dependence on "
                    "each user consistently applying the right protection "
                    "manually."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The label alone provides confidentiality protection "
                    "equivalent to encryption, so no additional controls are "
                    "required once a file is labeled \"Restricted\""
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The label is just metadata; it is the "
                    "controls the label triggers, such as encryption, that "
                    "actually provide protection — an unlabeled or "
                    "mislabeled file would have none of that protection."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Classification labels are useful only for regulatory "
                    "audit reporting and have no effect on the technical "
                    "controls applied to a file"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This contradicts the scenario, which "
                    "explicitly shows the label triggering encryption and "
                    "sharing restrictions, not merely serving a reporting "
                    "function."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Because the tool applies labels automatically, manual "
                    "review of classification decisions is no longer "
                    "necessary for any file"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Automated classification tools can "
                    "misclassify content, so a manual review or override "
                    "process is still generally needed for edge cases; "
                    "treating automation as infallible is a flawed "
                    "assumption."
                ),
            },
        ],
        "explanation": (
            "The genuine security value of classification labels is that "
            "they drive automatic, proportional enforcement of handling "
            "controls — the label is not protection by itself, is not "
            "purely for reporting, and does not eliminate the need for "
            "occasional manual review."
        ),
    },
    # ------------------------------------------------------------------ #
    # Data protection methods (3.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3f-028",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Data protection methods",
        "stem": (
            "A streaming media company holds licensing agreements that only "
            "permit certain movies to be streamed to users physically "
            "located within the United States. Which data protection method "
            "should the company implement to enforce this legal requirement "
            "at the platform level?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Geographic restrictions (geofencing/geolocation-based "
                    "access control) that block or allow content delivery "
                    "based on the requesting device's detected location"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Geographic restrictions are the data "
                    "protection method purpose-built to allow or block "
                    "access based on a requester's physical location, "
                    "directly matching the licensing requirement described."
                ),
            },
            {
                "id": "b",
                "text": "Field-level tokenization of the video content metadata",
                "correct": False,
                "rationale": (
                    "Incorrect. Tokenization replaces sensitive data values "
                    "with non-sensitive tokens; it does not control where "
                    "content can be streamed based on physical location."
                ),
            },
            {
                "id": "c",
                "text": "Data masking of user account records",
                "correct": False,
                "rationale": (
                    "Incorrect. Masking obscures displayed data values for "
                    "privacy purposes; it does not address media licensing "
                    "or location-based streaming enforcement."
                ),
            },
            {
                "id": "d",
                "text": "At-rest encryption of the video file library",
                "correct": False,
                "rationale": (
                    "Incorrect. Encryption at rest protects stored files "
                    "from unauthorized access if the storage is breached, "
                    "but it does not restrict streaming based on a viewer's "
                    "geographic location."
                ),
            },
        ],
        "explanation": (
            "Geographic restrictions are the correct control for enforcing "
            "location-based licensing terms; tokenization, masking, and "
            "at-rest encryption all protect data confidentiality but do not "
            "enforce location-based access."
        ),
    },
    {
        "id": "nd3f-029",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Data protection methods",
        "stem": (
            "A cloud security team is hardening a cloud object storage "
            "bucket that holds sensitive customer PII. Which THREE controls "
            "together provide the MOST effective defense-in-depth "
            "protection for this data at rest? (Select three.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Enable server-side encryption using customer-managed encryption keys",
                "correct": True,
                "rationale": (
                    "Correct. Encryption at rest with customer-managed keys "
                    "protects the confidentiality of the stored PII and "
                    "gives the organization control over key lifecycle and "
                    "revocation."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Apply a least-privilege bucket policy that blocks "
                    "public access and grants access only to specific "
                    "authorized roles"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A least-privilege access policy that blocks "
                    "public access directly prevents unauthorized parties "
                    "from reaching the bucket in the first place."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Enable detailed access logging and alerting on the "
                    "bucket to detect unauthorized or anomalous access "
                    "attempts"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Access logging and alerting provide detection "
                    "capability, completing a defense-in-depth approach "
                    "alongside prevention (access policy) and confidentiality "
                    "(encryption) controls."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Enable static website hosting on the bucket so the "
                    "data can be served directly to end users"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Enabling static website hosting increases "
                    "exposure by making the bucket a public web endpoint, "
                    "the opposite of protecting sensitive PII."
                ),
            },
            {
                "id": "e",
                "text": (
                    "Enable object versioning solely to reduce long-term "
                    "storage costs"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Versioning helps with recovery from "
                    "accidental deletion or overwrite, but this option "
                    "misstates its purpose and is not itself a "
                    "confidentiality or access-control protection for the "
                    "PII."
                ),
            },
            {
                "id": "f",
                "text": (
                    "Configure the bucket as a caching origin for a public "
                    "content delivery network (CDN)"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This would further distribute and expose "
                    "the sensitive data to a wide public content delivery "
                    "network, the opposite of protecting sensitive PII."
                ),
            },
        ],
        "explanation": (
            "Encryption, least-privilege access policy, and access logging "
            "together provide confidentiality, prevention, and detection — "
            "the pillars of defense-in-depth — while static hosting, "
            "cost-motivated versioning, and public CDN caching all increase "
            "exposure or fail to protect the data."
        ),
    },
    # ------------------------------------------------------------------ #
    # Data states (3.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3f-030",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Data states",
        "stem": (
            "A genomics research consortium wants a cloud partner to run "
            "proprietary analysis algorithms against sensitive patient "
            "genomic data, but contractual terms prohibit the cloud "
            "partner's own administrators from ever being able to view the "
            "unencrypted data, even while the computation is actively "
            "running in memory. Which technology BEST protects data in this "
            "specific state (data in use)?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A hardware-based trusted execution environment (TEE), "
                    "or confidential computing enclave, that keeps data "
                    "encrypted in memory and isolated from the hypervisor "
                    "and cloud administrator access during active processing"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Confidential computing enclaves are "
                    "specifically designed to protect data while it is "
                    "actively being processed in memory, isolating it from "
                    "even privileged administrators of the host system."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Transport Layer Security (TLS) for all data transferred "
                    "to and from the cloud partner"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. TLS protects data in transit only; it does "
                    "nothing to protect data while it is being actively "
                    "processed in memory during the computation."
                ),
            },
            {
                "id": "c",
                "text": (
                    "AES-256 encryption of the data at rest in cloud storage"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Encryption at rest protects stored data, but "
                    "the values must be decrypted to run the analysis, which "
                    "is exactly the exposure window the requirement is "
                    "trying to close."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Database column-level encryption applied before the "
                    "data is uploaded"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This protects the stored representation of "
                    "the data, but the values must still be decrypted in "
                    "memory to run the analysis, defeating the requirement "
                    "that administrators never see unencrypted data during "
                    "processing."
                ),
            },
        ],
        "explanation": (
            "Only a hardware-based TEE/confidential computing enclave "
            "protects data in use, the state in which it is actively being "
            "processed; TLS and at-rest/column-level encryption protect "
            "different data states (in transit and at rest) but leave data "
            "exposed once it must be decrypted for computation."
        ),
    },
    # ------------------------------------------------------------------ #
    # Tokenization and masking (3.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3f-031",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Tokenization and masking",
        "stem": (
            "A retailer's legacy point-of-sale software validates that a "
            "16-digit card number field passes a Luhn checksum before "
            "accepting a transaction record, and the software cannot be "
            "modified. The retailer wants to replace real card numbers with "
            "tokens throughout its systems, but the tokens must still pass "
            "the legacy software's Luhn validation. Which tokenization "
            "approach BEST satisfies this constraint?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Format-preserving tokenization that generates tokens "
                    "matching the original data's length, character set, and "
                    "Luhn-valid structure so legacy systems continue to "
                    "function without modification"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Format-preserving tokenization is specifically "
                    "designed to generate substitute values that pass the "
                    "same format and checksum validation as the original "
                    "data, letting unmodifiable legacy systems keep working."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Non-format-preserving tokenization using randomly "
                    "generated alphanumeric strings of arbitrary length"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Tokens of arbitrary length and character set "
                    "would fail the legacy software's fixed-format and Luhn "
                    "checksum validation, breaking compatibility."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Static data masking that permanently overwrites the "
                    "card number field with asterisks in a copy of the "
                    "database"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Static masking is used to de-identify data "
                    "in non-production copies; it does not generate usable "
                    "substitute values that can flow through a live "
                    "production transaction process."
                ),
            },
            {
                "id": "d",
                "text": "Hashing the card number with SHA-256 before storage",
                "correct": False,
                "rationale": (
                    "Incorrect. A hash is a fixed-length digest that does "
                    "not preserve the original numeric format or pass a "
                    "Luhn checksum, and hashing is also not reversible to "
                    "retrieve the original value when needed."
                ),
            },
        ],
        "explanation": (
            "Format-preserving tokenization is the only option that "
            "produces substitute values compatible with a legacy system's "
            "fixed format and checksum validation, unlike arbitrary tokens, "
            "static masking of a database copy, or a non-reversible hash."
        ),
    },
    {
        "id": "nd3f-032",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Tokenization and masking",
        "stem": (
            "A hospital's electronic health record system is queried "
            "directly by many different roles — physicians, billing clerks, "
            "and researchers — through the same underlying patient "
            "database. The hospital wants physicians to see full patient "
            "records, billing clerks to see only fields relevant to billing "
            "with diagnosis codes hidden, and researchers to see de-"
            "identified records, all without maintaining three separate "
            "copies of the database. Which approach BEST achieves this?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Dynamic data masking applied at query time that returns "
                    "different masked or unmasked views of the same "
                    "underlying data based on the requesting user's role"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Dynamic data masking evaluates the requesting "
                    "user's role at query time and returns an appropriately "
                    "masked or unmasked view from the single live database, "
                    "exactly matching the three-role requirement."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Static data masking applied once to create a "
                    "permanently de-identified copy of the database for all "
                    "three roles to share"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A single, permanently de-identified static "
                    "copy cannot simultaneously give physicians full access "
                    "and researchers de-identified access; static masking "
                    "produces one fixed view, not three different role-based "
                    "views."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Full-database encryption at rest with a single shared "
                    "decryption key"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A single shared decryption key would give "
                    "all three roles either full access or no access, not "
                    "the differentiated, role-based views the hospital "
                    "needs."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Tokenization of all patient identifiers with a single "
                    "global token vault"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Tokenization substitutes identifiers "
                    "uniformly for all consumers; it does not by itself "
                    "provide three different role-based views of the "
                    "remaining clinical and billing fields within the same "
                    "live database."
                ),
            },
        ],
        "explanation": (
            "Dynamic data masking is uniquely suited to producing multiple, "
            "simultaneous role-based views from one live database, unlike "
            "static masking (one fixed copy), uniform full-database "
            "encryption, or uniform tokenization."
        ),
    },
    # ------------------------------------------------------------------ #
    # Backups and replication (3.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3f-033",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Backups and replication",
        "stem": (
            "A trading firm's compliance requirement mandates a recovery "
            "point objective (RPO) of no more than 30 seconds for its "
            "order-matching database, meaning at most 30 seconds of "
            "transactions can ever be lost in a failure. Which backup or "
            "replication approach BEST meets this RPO?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Continuous data protection (CDP) that journals every "
                    "write in near real time, allowing recovery to almost "
                    "any point in time within seconds of a failure"
                ),
                "correct": True,
                "rationale": (
                    "Correct. CDP's near-real-time, continuous journaling is "
                    "the only approach listed capable of limiting potential "
                    "data loss to a matter of seconds, satisfying the "
                    "30-second RPO."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Nightly full backups scheduled during a low-traffic "
                    "maintenance window"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Nightly backups could lose up to nearly 24 "
                    "hours of transactions, far exceeding a 30-second RPO."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Weekly full backups with daily incremental backups"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Daily incremental granularity still allows "
                    "up to a full day of potential data loss, far exceeding "
                    "the 30-second requirement."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Asynchronous replication to a secondary site with a "
                    "typical replication lag of several minutes"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Asynchronous replication's inherent lag of "
                    "several minutes still exceeds the 30-second RPO "
                    "requirement; synchronous or CDP-level replication would "
                    "be needed."
                ),
            },
        ],
        "explanation": (
            "Only continuous data protection can realistically limit "
            "potential data loss to seconds, meeting a 30-second RPO; "
            "nightly backups, weekly/daily backup schedules, and "
            "asynchronous replication all leave gaps of minutes to a full "
            "day."
        ),
    },
    {
        "id": "nd3f-034",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Backups and replication",
        "stem": (
            "A small manufacturing firm stores two backup copies of its ERP "
            "database: one on a second internal disk array in the same "
            "server rack, and one on a NAS device in the same building. "
            "During an electrical fire in the server room, both backup "
            "copies were destroyed along with the production system. Which "
            "principle of the 3-2-1 backup rule did this design violate?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The requirement to keep at least one copy offsite, in a "
                    "physically separate location from the primary site"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Both backup copies were in the same building "
                    "as production, so a single localized disaster destroyed "
                    "everything — exactly the failure the offsite-copy "
                    "requirement is meant to prevent."
                ),
            },
            {
                "id": "b",
                "text": "The requirement to keep at least three total copies of the data",
                "correct": False,
                "rationale": (
                    "Incorrect. The firm had three total copies — "
                    "production plus two backups — which satisfies the "
                    "\"3\" count; the failure was about location, not the "
                    "number of copies."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The requirement to use at least two different backup "
                    "software vendors"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The 3-2-1 rule specifies two different "
                    "storage media types, not two different software "
                    "vendors, so this misstates the rule."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The requirement to test restores at least twice per "
                    "year"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Restore testing is a separate resilience-"
                    "testing best practice, not part of the 3-2-1 rule "
                    "itself, and it was not the described cause of the "
                    "total loss."
                ),
            },
        ],
        "explanation": (
            "The 3-2-1 rule requires 3 total copies, on 2 different media "
            "types, with 1 copy offsite; the firm satisfied the copy count "
            "but kept both backups in the same building as production, "
            "violating the offsite requirement and losing everything in one "
            "localized event."
        ),
    },
    # ------------------------------------------------------------------ #
    # High availability (3.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3f-035",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "High availability",
        "stem": (
            "A company's SLA with a cloud provider guarantees 99.99% "
            "(\"four nines\") availability for a critical API. Over the "
            "past 12 months, the API was unavailable for a cumulative total "
            "of 1 hour and 45 minutes. Which conclusion is accurate?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The provider violated the SLA, because 99.99% "
                    "availability permits only about 52 minutes of downtime "
                    "per year, and the actual downtime far exceeded that"
                ),
                "correct": True,
                "rationale": (
                    "Correct. 99.99% ('four nines') annual availability "
                    "corresponds to roughly 52 minutes of allowable downtime "
                    "per year; 1 hour 45 minutes is more than double that "
                    "budget, so the SLA was violated."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The provider met the SLA, because 1 hour and 45 "
                    "minutes of downtime in a year is well within typical "
                    "enterprise availability expectations"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. \"Typical expectations\" is vague and does "
                    "not reflect the specific numeric 99.99% commitment, "
                    "which permits far less downtime than what actually "
                    "occurred."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The provider met the SLA, because 99.99% availability "
                    "corresponds to roughly 8.7 hours of allowable downtime "
                    "per year"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This misstates the math; approximately 8.7 "
                    "hours of allowable annual downtime corresponds to "
                    "99.9% ('three nines'), not 99.99%."
                ),
            },
            {
                "id": "d",
                "text": (
                    "SLA availability percentages apply only to planned "
                    "maintenance windows, so unplanned outages like this one "
                    "do not count against the guarantee"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. SLA uptime commitments generally measure "
                    "total unavailability, and unplanned outages are "
                    "precisely what such SLAs are designed to bound, unless "
                    "specific maintenance exclusions are separately "
                    "negotiated."
                ),
            },
        ],
        "explanation": (
            "99.99% annual availability allows only about 52 minutes of "
            "downtime per year; 1 hour 45 minutes of actual downtime is a "
            "clear SLA violation, while the other options misapply the "
            "'nines' math or mischaracterize what the SLA covers."
        ),
    },
    {
        "id": "nd3f-036",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "High availability",
        "stem": (
            "A security architect is redesigning a critical web "
            "application's infrastructure to maximize availability. Which "
            "THREE design choices would MOST effectively increase the "
            "application's availability? (Select three.)"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Deploy redundant application and database instances "
                    "across multiple availability zones so no single zone "
                    "failure takes down the service"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Distributing redundant instances across "
                    "multiple availability zones ensures a single zone "
                    "failure does not take the entire service down."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Implement automated health checks and failover so "
                    "traffic is redirected away from failed instances within "
                    "seconds, without waiting for a human to notice"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Automated detection and failover minimizes "
                    "downtime by responding to failures far faster than a "
                    "human could, directly increasing availability."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Eliminate identified single points of failure, such as "
                    "a single load balancer or single network path, by "
                    "adding redundant instances of each"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Removing single points of failure at every "
                    "layer, including load balancers and network paths, is "
                    "fundamental to a highly available design."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Consolidate the entire application onto one large, "
                    "powerful physical server to simplify management"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Consolidating onto a single server creates a "
                    "single point of failure; vertical scaling on one host "
                    "does not improve availability and may worsen it."
                ),
            },
            {
                "id": "e",
                "text": (
                    "Require an on-call engineer to manually detect outages "
                    "by watching a dashboard and manually restart failed "
                    "instances"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Manual detection and response is slower and "
                    "less reliable than automated failover, increasing "
                    "downtime rather than reducing it."
                ),
            },
            {
                "id": "f",
                "text": (
                    "Store the only backup copy of the database on the same "
                    "physical host as the production database for faster "
                    "restores"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A co-located single backup copy is destroyed "
                    "along with production in a host-level failure, "
                    "reducing rather than improving resilience."
                ),
            },
        ],
        "explanation": (
            "Multi-zone redundancy, automated failover, and eliminating "
            "single points of failure are the core pillars of high "
            "availability design, while consolidating onto one server, "
            "relying on manual detection, and co-locating the only backup "
            "copy all undermine availability."
        ),
    },
    # ------------------------------------------------------------------ #
    # Multi-cloud and platform diversity (3.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3f-037",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Multi-cloud and platform diversity",
        "stem": (
            "A security architect recommends that critical DNS resolution "
            "services be split across two different DNS software vendors on "
            "different underlying platforms, rather than running every DNS "
            "server on the same vendor's software. Which risk does this "
            "platform diversity specifically mitigate?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A single vendor-specific zero-day vulnerability or "
                    "software defect simultaneously compromising or "
                    "crashing every DNS server in the environment at once"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Platform diversity specifically defends "
                    "against correlated, common-mode failures: a single "
                    "vendor's zero-day cannot take down servers running a "
                    "different vendor's software."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The financial cost of licensing DNS software from a "
                    "single vendor"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This describes a cost or vendor-lock-in "
                    "concern, not the technical, correlated-failure risk "
                    "that platform diversity is specifically intended to "
                    "mitigate in this scenario."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The need to negotiate more favorable contract terms "
                    "with a single vendor"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is a procurement or business "
                    "consideration, not the resilience risk that running two "
                    "different software platforms addresses."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The risk that a single vendor will discontinue product "
                    "support in the future"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is a legitimate long-term planning "
                    "concern, but it is not the specific failure/"
                    "vulnerability risk that platform diversity is being "
                    "used to mitigate in this scenario."
                ),
            },
        ],
        "explanation": (
            "Platform diversity primarily defends against a single "
            "vendor-specific defect or zero-day causing a correlated, "
            "simultaneous outage across all instances — a distinct benefit "
            "from cost, negotiating leverage, or long-term support "
            "concerns."
        ),
    },
    # ------------------------------------------------------------------ #
    # Power resilience (3.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3f-038",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Power resilience",
        "stem": (
            "A data center evaluates two UPS technologies to bridge the gap "
            "between a utility power failure and generator startup: a "
            "battery-based UPS that can sustain full load for about 15 "
            "minutes, and a flywheel-based UPS that can sustain full load "
            "for only about 30 seconds but requires far less maintenance and "
            "has no chemical battery to degrade or dispose of. The "
            "facility's diesel generators reliably reach full output within "
            "20 seconds of a power failure. Which UPS choice is MOST "
            "appropriate for this facility?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The flywheel UPS, because it comfortably bridges the "
                    "20-second gap until generator startup while avoiding "
                    "the maintenance burden and disposal concerns of battery "
                    "chemistry"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Since the generator reliably reaches full "
                    "output within 20 seconds, the flywheel's roughly "
                    "30-second capacity is sufficient, making it the more "
                    "efficient choice given its lower maintenance burden."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The battery UPS, because 15 minutes of runtime is "
                    "always safer than 30 seconds regardless of how quickly "
                    "the generator starts"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This ignores the stated 20-second generator "
                    "startup time; the flywheel's shorter runtime is already "
                    "sufficient, so the extra battery runtime mainly adds "
                    "unnecessary cost and maintenance in this specific "
                    "scenario."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Neither UPS is necessary since the diesel generator "
                    "alone can respond within 20 seconds"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A UPS is still required to bridge the power "
                    "gap during the 20 seconds before the generator reaches "
                    "full output; without one, there would be a power "
                    "interruption during that window."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The battery UPS, because flywheel UPS systems cannot "
                    "supply enough instantaneous power to support an entire "
                    "data center's full load"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Flywheel UPS systems are a proven technology "
                    "commonly used at full data center load capacity for "
                    "short bridge durations; the limiting factor is "
                    "duration, not instantaneous power capacity."
                ),
            },
        ],
        "explanation": (
            "Given a reliable 20-second generator startup, a flywheel UPS's "
            "roughly 30-second runtime is sufficient and avoids battery "
            "maintenance and disposal overhead, making it the more "
            "appropriate choice over an oversized battery UPS or forgoing a "
            "UPS entirely."
        ),
    },
    # ------------------------------------------------------------------ #
    # Recovery sites (3.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3f-039",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Recovery sites",
        "stem": (
            "A manufacturer's business continuity plan sets a recovery time "
            "objective (RTO) of 6 hours for its ERP system, and management "
            "wants to avoid the very high ongoing cost of maintaining a "
            "fully mirrored, always-on hot site. Which recovery site "
            "strategy BEST balances this RTO requirement against cost?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A warm site with pre-installed hardware and "
                    "periodically updated data that can be brought fully "
                    "online within a few hours, without the continuous "
                    "full-time replication cost of a hot site"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A warm site's few-hour activation time "
                    "comfortably meets a 6-hour RTO while avoiding the "
                    "continuous, high ongoing cost of a fully mirrored hot "
                    "site."
                ),
            },
            {
                "id": "b",
                "text": (
                    "A cold site with empty floor space, power, and "
                    "connectivity, where hardware and data must be procured "
                    "and restored from backups after a disruption occurs"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Cold sites typically take days to weeks to "
                    "become operational, which would likely miss a 6-hour "
                    "RTO."
                ),
            },
            {
                "id": "c",
                "text": (
                    "A hot site with real-time data mirroring and fully "
                    "redundant, immediately available production capacity"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A hot site easily meets the RTO but is the "
                    "highest-cost option, which contradicts the stated goal "
                    "of avoiding that ongoing cost when it is not strictly "
                    "required."
                ),
            },
            {
                "id": "d",
                "text": (
                    "A reciprocal agreement with a business partner to use "
                    "each other's data centers in an emergency, with no "
                    "dedicated equipment reserved in advance"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Reciprocal agreements carry significant "
                    "uncertainty around available capacity and readiness at "
                    "the time of an actual disaster, making a reliable "
                    "6-hour RTO commitment unlikely."
                ),
            },
        ],
        "explanation": (
            "A warm site meets a moderate 6-hour RTO without the continuous "
            "high cost of a hot site, while a cold site is typically too "
            "slow, a hot site is unnecessarily expensive, and a reciprocal "
            "agreement is too uncertain to reliably guarantee the RTO."
        ),
    },
    {
        "id": "nd3f-040",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Recovery sites",
        "stem": (
            "A cloud-native company wants a disaster recovery strategy where "
            "only the most critical core components — a minimal database "
            "replica and networking configuration — run continuously in a "
            "secondary cloud region, while the remaining application servers "
            "are defined as infrastructure-as-code templates that can be "
            "rapidly launched and scaled up only when a disaster is "
            "declared. Which DR architecture pattern does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Pilot light, where a minimal core set of systems runs "
                    "continuously and the rest of the environment is "
                    "scripted to launch on demand during a declared disaster"
                ),
                "correct": True,
                "rationale": (
                    "Correct. This matches the pilot light pattern exactly: "
                    "a small always-on core (database replica and "
                    "networking) with the remaining infrastructure launched "
                    "from templates only when needed."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Hot site / multi-site active-active, where full "
                    "production capacity runs simultaneously in both regions "
                    "at all times"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This describes a fully running duplicate "
                    "environment at all times, not a minimal always-on core "
                    "with the rest launched on demand as described."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Cold site, where no infrastructure exists in the "
                    "secondary region until a disaster occurs"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This contradicts the scenario, which "
                    "explicitly keeps a minimal database replica and "
                    "networking running continuously in the secondary "
                    "region."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Reciprocal agreement, where two organizations agree to "
                    "host each other's workloads during a disaster"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This describes an arrangement between two "
                    "separate organizations, not a single company's own "
                    "multi-region cloud architecture."
                ),
            },
        ],
        "explanation": (
            "Pilot light keeps a minimal, always-on core running while the "
            "rest of the environment is defined as code and launched on "
            "demand — distinct from a fully active hot site, an entirely "
            "empty cold site, or a cross-organization reciprocal "
            "agreement."
        ),
    },
    # ------------------------------------------------------------------ #
    # Resilience testing (3.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3f-041",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Resilience testing",
        "stem": (
            "An airline's disaster recovery team wants to verify that its "
            "secondary data center can actually take over live production "
            "reservation processing, not just that the runbook reads "
            "correctly on paper. However, actually failing over the real "
            "production system carries a risk of a nationwide booking "
            "outage if the test does not go as planned. Which test type "
            "lets the team validate real failover mechanics while "
            "minimizing the risk of disrupting live production ticket "
            "sales?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A parallel test, in which the secondary site processes "
                    "a copy of live transactions simultaneously alongside "
                    "production, without production traffic actually being "
                    "cut over"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A parallel test exercises the actual technical "
                    "failover mechanics against real transaction data while "
                    "leaving live production traffic untouched, minimizing "
                    "risk to real ticket sales."
                ),
            },
            {
                "id": "b",
                "text": (
                    "A full interruption test, in which production traffic "
                    "is completely cut over to the secondary site"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is the higher-risk approach the team is "
                    "specifically trying to avoid, since a failed cutover "
                    "could cause the very nationwide outage they want to "
                    "prevent."
                ),
            },
            {
                "id": "c",
                "text": (
                    "A tabletop exercise, in which the team discusses the "
                    "runbook steps in a conference room without touching any "
                    "systems"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A tabletop exercise validates the plan's "
                    "logic and communication, but does not exercise the "
                    "actual technical failover mechanics, which is what the "
                    "team needs to verify."
                ),
            },
            {
                "id": "d",
                "text": (
                    "A checklist review, in which the DR documentation is "
                    "read and updated for accuracy"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is a paper-only review that does not "
                    "test whether the failover mechanics actually work in "
                    "practice."
                ),
            },
        ],
        "explanation": (
            "A parallel test is the resilience test type that exercises "
            "genuine failover mechanics against real data without cutting "
            "over live production, unlike a full interruption test (highest "
            "risk), a tabletop exercise, or a paper checklist review "
            "(neither of which touches real systems)."
        ),
    },
    # ------------------------------------------------------------------ #
    # Third-party agreement types (3.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd3f-042",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Third-party agreement types",
        "stem": (
            "A company has a signed master service agreement (MSA) with an "
            "IT consulting firm that establishes general legal terms, "
            "payment terms, and confidentiality obligations governing their "
            "overall business relationship. The company now wants to engage "
            "the firm for a specific six-week network redesign project with "
            "a defined scope, deliverables, timeline, and price. Which "
            "additional document is MOST appropriate for this specific "
            "engagement?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A statement of work (SOW) that defines the specific "
                    "scope, deliverables, timeline, and cost for this "
                    "particular project under the existing MSA"
                ),
                "correct": True,
                "rationale": (
                    "Correct. An SOW is the document specifically designed "
                    "to define the scope, deliverables, timeline, and price "
                    "of an individual project or engagement conducted under "
                    "an existing MSA's general terms."
                ),
            },
            {
                "id": "b",
                "text": (
                    "A new master service agreement replacing the existing "
                    "one for this project"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The existing MSA already establishes the "
                    "overarching legal terms; renegotiating an entirely new "
                    "MSA for a single project is unnecessary and "
                    "inefficient."
                ),
            },
            {
                "id": "c",
                "text": (
                    "A memorandum of understanding (MOU) outlining the "
                    "general intent to collaborate"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. An MOU is a non-binding, high-level "
                    "statement of intent typically used in early "
                    "discussions, not a binding document defining specific "
                    "deliverables and cost for an active engagement already "
                    "governed by an MSA."
                ),
            },
            {
                "id": "d",
                "text": (
                    "A business partnership agreement (BPA) defining joint "
                    "ownership of the resulting network infrastructure"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A BPA defines joint ownership and financial "
                    "responsibility in a business partnership or joint "
                    "venture; this is a standard vendor engagement, not a "
                    "joint venture, and ownership is not the issue "
                    "described."
                ),
            },
        ],
        "explanation": (
            "A statement of work is the correct instrument for defining a "
            "specific project's scope, deliverables, and cost under an "
            "existing MSA, unlike renegotiating the MSA itself, a "
            "non-binding MOU, or a BPA meant for joint-venture ownership "
            "arrangements."
        ),
    },
]

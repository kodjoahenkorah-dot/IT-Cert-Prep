"""
CompTIA A+ Core 1 (220-1201) — Domain 4: Virtualization and Cloud Computing
Study notes following Professor Messer's playlist order.
"""

NOTES = [
    {
        "domain": 4,
        "topic": "Cloud service models",
        "objective": "4.1",
        "video": "Cloud Models",
        "study_topics": [
            "Cloud service models",
            "Cloud service models — IaaS / PaaS / SaaS",
        ],
        "body": (
            "<p>Cloud service models define which layers of a computing stack "
            "the provider manages versus what the customer is responsible for.</p>"
            "<ul>"
            "<li><strong>IaaS (Infrastructure as a Service):</strong> The provider "
            "supplies virtualized hardware — compute, storage, and networking. The "
            "customer manages the OS, middleware, runtime, and applications. Examples: "
            "Amazon EC2, Microsoft Azure VMs, Google Compute Engine. Best for teams "
            "needing full OS-level control without owning physical hardware.</li>"
            "<li><strong>PaaS (Platform as a Service):</strong> The provider manages "
            "the OS, runtime, and middleware. The customer only manages applications "
            "and data. Examples: Heroku, Google App Engine, Azure App Service. Best "
            "for developers who want to focus on code without worrying about "
            "infrastructure.</li>"
            "<li><strong>SaaS (Software as a Service):</strong> The provider manages "
            "everything — infrastructure, platform, and the application itself. The "
            "customer just uses the software through a browser or thin client. "
            "Examples: Microsoft 365, Google Workspace, Salesforce. No installation "
            "or maintenance required by the user.</li>"
            "</ul>"
            "<p><strong>Responsibility split summary:</strong></p>"
            "<table border='1' cellpadding='4'>"
            "<tr><th>Layer</th><th>IaaS</th><th>PaaS</th><th>SaaS</th></tr>"
            "<tr><td>Application</td><td>Customer</td><td>Customer</td><td>Provider</td></tr>"
            "<tr><td>Data</td><td>Customer</td><td>Customer</td><td>Provider</td></tr>"
            "<tr><td>Runtime / OS</td><td>Customer</td><td>Provider</td><td>Provider</td></tr>"
            "<tr><td>Hardware / Network</td><td>Provider</td><td>Provider</td><td>Provider</td></tr>"
            "</table>"
        ),
        "key_points": [
            "IaaS: customer manages OS and up; provider manages hardware.",
            "PaaS: customer manages application and data only.",
            "SaaS: provider manages everything; customer just uses the app.",
            "Moving from IaaS → PaaS → SaaS shifts more responsibility to the provider.",
        ],
    },
    {
        "domain": 4,
        "topic": "Cloud deployment models",
        "objective": "4.1",
        "video": "Cloud Models",
        "study_topics": ["Cloud deployment models"],
        "body": (
            "<p>Cloud deployment models describe <em>who owns and controls</em> the "
            "cloud infrastructure and who can access it.</p>"
            "<ul>"
            "<li><strong>Public cloud:</strong> Infrastructure is owned and operated by "
            "a third-party provider (AWS, Azure, GCP) and shared across multiple "
            "organizations (multi-tenant). Resources are provisioned on demand over the "
            "internet. Lowest upfront cost but least control over physical security.</li>"
            "<li><strong>Private cloud:</strong> Infrastructure is dedicated to a single "
            "organization. It may be on-premises or hosted by a third party, but it is "
            "not shared. Offers the highest control and security; common in government "
            "and finance. Higher cost to build and maintain.</li>"
            "<li><strong>Hybrid cloud:</strong> Combines public and private cloud "
            "environments connected by technology that allows data and applications to "
            "move between them. Enables 'cloud bursting' — overflow workloads shift to "
            "the public cloud when private capacity is exhausted.</li>"
            "<li><strong>Community cloud:</strong> Shared infrastructure used exclusively "
            "by a group of organizations with common concerns (e.g., compliance, mission, "
            "security requirements). Examples: government agencies sharing a FedRAMP cloud, "
            "healthcare consortia sharing a HIPAA-compliant platform. Cost is shared among "
            "members.</li>"
            "</ul>"
            "<p>The exam may ask you to identify the correct model given a scenario — "
            "watch for keywords like 'single organization' (private), 'on-demand shared' "
            "(public), 'overflow to public' (hybrid), and 'shared among similar entities' "
            "(community).</p>"
        ),
        "key_points": [
            "Public: multi-tenant, provider-owned, internet-accessible.",
            "Private: single-tenant, dedicated infrastructure, highest control.",
            "Hybrid: mix of public and private; supports cloud bursting.",
            "Community: shared by organizations with common regulatory or mission needs.",
        ],
    },
    {
        "domain": 4,
        "topic": "Cloud characteristics",
        "objective": "4.1",
        "video": "Cloud Characteristics",
        "study_topics": ["Cloud characteristics"],
        "body": (
            "<p>The NIST definition of cloud computing identifies five essential "
            "characteristics that distinguish true cloud services from traditional hosting.</p>"
            "<ul>"
            "<li><strong>Rapid elasticity:</strong> Resources can be provisioned and "
            "released quickly — sometimes automatically — to scale with demand. From the "
            "consumer's perspective, capacity appears unlimited and can be purchased at "
            "any time in any quantity.</li>"
            "<li><strong>Metered / measured service:</strong> Resource usage (storage, "
            "compute, bandwidth) is monitored, measured, and billed. Customers pay only "
            "for what they consume, similar to a utility bill. This enables cost "
            "transparency for both provider and customer.</li>"
            "<li><strong>Broad network access:</strong> Services are accessible over "
            "the network through standard mechanisms (browsers, mobile apps, APIs), "
            "enabling use from diverse client platforms (phones, tablets, laptops).</li>"
            "<li><strong>Resource pooling:</strong> Provider resources are pooled to "
            "serve multiple customers using a multi-tenant model. Physical and virtual "
            "resources are dynamically assigned and reassigned; customers typically have "
            "no control over the exact location of resources.</li>"
            "<li><strong>On-demand self-service:</strong> A consumer can provision "
            "compute resources (server time, storage) automatically without requiring "
            "human interaction with the provider.</li>"
            "</ul>"
            "<p>Additional exam-relevant characteristics:</p>"
            "<ul>"
            "<li><strong>High availability (HA):</strong> Cloud platforms are designed "
            "with redundancy so services remain accessible even when individual components "
            "fail. HA is typically expressed as a percentage uptime SLA (e.g., 99.9%).</li>"
            "<li><strong>Scalability:</strong> Vertical scaling (scale up) adds more "
            "resources to an existing instance; horizontal scaling (scale out) adds more "
            "instances. Cloud makes both approaches easier than on-prem.</li>"
            "<li><strong>File synchronization:</strong> Cloud storage services (OneDrive, "
            "Google Drive, iCloud) keep files consistent across multiple devices in real "
            "time, which is a practical benefit for end users.</li>"
            "</ul>"
        ),
        "key_points": [
            "Rapid elasticity: scale up/down quickly; capacity appears unlimited.",
            "Metered service: pay per use, like a utility.",
            "On-demand self-service: provision resources without calling a human.",
            "High availability: redundancy ensures uptime; expressed as % SLA.",
            "Scalability: vertical (bigger instance) vs. horizontal (more instances).",
            "File synchronization: cloud drives keep files consistent across devices.",
        ],
    },
    {
        "domain": 4,
        "topic": "VDI/DaaS",
        "objective": "4.1",
        "video": "Desktop Virtualization",
        "study_topics": ["VDI/DaaS"],
        "body": (
            "<p><strong>Virtual Desktop Infrastructure (VDI)</strong> hosts desktop "
            "operating system instances on centralized servers in a data center. End "
            "users connect to their personal virtual desktop over the network using a "
            "thin client, zero client, or standard PC with remote desktop software "
            "(e.g., VMware Horizon, Citrix Virtual Apps and Desktops).</p>"
            "<p><strong>How VDI works:</strong></p>"
            "<ol>"
            "<li>A hypervisor on a server runs many desktop VMs simultaneously.</li>"
            "<li>Each user session is isolated in its own VM with dedicated OS, apps, "
            "and user profile.</li>"
            "<li>The user sees only the remote screen; processing happens on the server.</li>"
            "</ol>"
            "<p><strong>Desktop as a Service (DaaS)</strong> is VDI delivered as a "
            "cloud service — the provider owns and manages the hypervisors and hardware. "
            "The organization subscribes on a per-seat basis. Examples: Amazon WorkSpaces, "
            "Windows 365 Cloud PC, Citrix DaaS.</p>"
            "<p><strong>Benefits of VDI/DaaS:</strong></p>"
            "<ul>"
            "<li>Centralized management — patch once, update all desktops instantly.</li>"
            "<li>Improved security — data stays in the data center, not on endpoint devices.</li>"
            "<li>Support for BYOD scenarios — users can work from any device.</li>"
            "<li>Easy disaster recovery — desktops are not tied to physical hardware.</li>"
            "</ul>"
            "<p><strong>Drawbacks:</strong> Requires reliable, low-latency network; "
            "poor experience if bandwidth is limited. Higher server hardware investment "
            "for on-prem VDI.</p>"
        ),
        "key_points": [
            "VDI: desktop OS instances run on centralized servers; users connect remotely.",
            "DaaS: VDI delivered as a cloud subscription service (e.g., Amazon WorkSpaces).",
            "Thin/zero clients are common endpoints for VDI environments.",
            "Data stays in the data center — reduces risk from lost or stolen devices.",
            "Requires reliable, low-latency network for a good user experience.",
        ],
    },
    {
        "domain": 4,
        "topic": "Hypervisor types",
        "objective": "4.2",
        "video": "Client-side Virtualization",
        "study_topics": [
            "Hypervisor types",
            "Hypervisor types — Type 1 (bare-metal) vs Type 2 (hosted)",
        ],
        "body": (
            "<p>A <strong>hypervisor</strong> (also called a Virtual Machine Monitor, VMM) "
            "is software that creates and manages virtual machines (VMs), allocating "
            "physical hardware resources to each guest OS.</p>"
            "<h4>Type 1 — Bare-Metal Hypervisor</h4>"
            "<p>Runs directly on the physical hardware without a host operating system "
            "underneath. It <em>is</em> the operating layer. Because there is no "
            "general-purpose OS between the hypervisor and the hardware, overhead is "
            "minimal and performance is high.</p>"
            "<ul>"
            "<li><strong>Examples:</strong> VMware ESXi, Microsoft Hyper-V (server role), "
            "Citrix XenServer, KVM (Linux kernel-based)</li>"
            "<li><strong>Use cases:</strong> Data centers, enterprise servers, cloud "
            "provider infrastructure</li>"
            "<li><strong>Advantages:</strong> Lower overhead, better performance, more "
            "secure (smaller attack surface without a full host OS)</li>"
            "</ul>"
            "<h4>Type 2 — Hosted Hypervisor</h4>"
            "<p>Runs as an application on top of an existing host operating system "
            "(Windows, macOS, Linux). The host OS mediates access to hardware, so "
            "there is more overhead compared to Type 1.</p>"
            "<ul>"
            "<li><strong>Examples:</strong> Oracle VirtualBox, VMware Workstation, "
            "VMware Fusion (macOS), Parallels Desktop</li>"
            "<li><strong>Use cases:</strong> Developer workstations, labs, testing, "
            "personal use</li>"
            "<li><strong>Advantages:</strong> Easy to install on an existing machine; "
            "no dedicated hardware required</li>"
            "</ul>"
            "<table border='1' cellpadding='4'>"
            "<tr><th>Feature</th><th>Type 1 (Bare-Metal)</th><th>Type 2 (Hosted)</th></tr>"
            "<tr><td>Runs on</td><td>Directly on hardware</td><td>On top of host OS</td></tr>"
            "<tr><td>Performance</td><td>High</td><td>Lower (host OS overhead)</td></tr>"
            "<tr><td>Typical environment</td><td>Server / data center</td><td>Desktop / workstation</td></tr>"
            "<tr><td>Examples</td><td>ESXi, Hyper-V</td><td>VirtualBox, VMware Workstation</td></tr>"
            "</table>"
        ),
        "key_points": [
            "Type 1 runs directly on hardware — no host OS (e.g., ESXi, Hyper-V).",
            "Type 2 runs as an app on a host OS (e.g., VirtualBox, VMware Workstation).",
            "Type 1 has lower overhead and is used in enterprise/data center environments.",
            "Type 2 is easier to set up on an existing workstation for dev and testing.",
            "Both types allow multiple guest OSes to run simultaneously on one machine.",
        ],
    },
    {
        "domain": 4,
        "topic": "VM use cases",
        "objective": "4.2",
        "video": "Client-side Virtualization",
        "study_topics": ["VM use cases"],
        "body": (
            "<p>Virtual machines serve a wide variety of practical purposes in both "
            "enterprise and individual settings. The A+ exam expects familiarity with "
            "common scenarios:</p>"
            "<ul>"
            "<li><strong>Sandbox / testing environment:</strong> Run untrusted software, "
            "malware analysis, or new application testing in an isolated VM. If the VM "
            "is compromised or corrupted, the host remains unaffected. Snapshots allow "
            "quick rollback to a clean state.</li>"
            "<li><strong>Application compatibility:</strong> Run legacy applications "
            "that require an older OS (e.g., Windows XP) on modern hardware without "
            "maintaining a separate physical machine.</li>"
            "<li><strong>Cross-platform development and testing:</strong> Developers can "
            "run Windows, Linux, and macOS VMs on a single workstation to test software "
            "across platforms.</li>"
            "<li><strong>Server consolidation:</strong> Replace many underutilized "
            "physical servers with VMs on fewer, more powerful hosts — reducing hardware "
            "costs, power consumption, and data center footprint.</li>"
            "<li><strong>Disaster recovery / business continuity:</strong> VMs are "
            "encapsulated in files that can be backed up, replicated, and quickly "
            "restored on alternative hardware.</li>"
            "<li><strong>Training and education:</strong> Provide students or trainees "
            "with isolated environments that can be reset between sessions.</li>"
            "<li><strong>Security research:</strong> Analyze malware or vulnerabilities "
            "in an environment that can be cleanly destroyed afterward.</li>"
            "</ul>"
            "<p>Key concept: <strong>snapshots</strong> capture the VM state at a point "
            "in time, enabling rapid rollback — critical for testing and recovery scenarios.</p>"
        ),
        "key_points": [
            "Sandboxing: isolate untrusted software from the host system.",
            "Legacy app support: run old OSes on modern hardware without extra machines.",
            "Server consolidation: fewer physical servers, lower cost and power usage.",
            "Snapshots allow instant rollback to a known-good state.",
            "Disaster recovery: VMs stored as files can be migrated or restored quickly.",
        ],
    },
    {
        "domain": 4,
        "topic": "VM resource requirements",
        "objective": "4.2",
        "video": "Client-side Virtualization",
        "study_topics": ["VM resource requirements"],
        "body": (
            "<p>Running virtual machines places real demands on the host system. "
            "Proper hardware planning is essential to avoid performance problems.</p>"
            "<ul>"
            "<li><strong>CPU:</strong> Each VM requires virtual CPUs (vCPUs). The host "
            "processor must have enough cores (and ideally hardware virtualization "
            "support — Intel VT-x or AMD-V) to run guest VMs efficiently. Hardware "
            "virtualization extensions must be enabled in UEFI/BIOS.</li>"
            "<li><strong>RAM:</strong> Every running VM consumes a portion of host RAM "
            "for its guest OS and applications. Running out of host RAM forces the "
            "hypervisor to use disk-based swap, causing severe performance degradation. "
            "Rule of thumb: total assigned VM RAM should not exceed physical RAM.</li>"
            "<li><strong>Storage:</strong> VMs use disk image files (e.g., .vmdk, .vhd, "
            ".vdi). Storage must accommodate the OS, applications, and data for every VM. "
            "SSDs dramatically improve VM performance compared to spinning HDDs due to "
            "random I/O demands.</li>"
            "<li><strong>Network:</strong> Virtual NICs (vNICs) connect VMs to the "
            "network via virtual switches on the host. Sufficient host NIC bandwidth is "
            "needed when many VMs share a single physical NIC.</li>"
            "<li><strong>GPU (graphics):</strong> VMs running graphically intensive "
            "workloads may need GPU pass-through or a dedicated virtual GPU (vGPU) for "
            "acceptable performance.</li>"
            "</ul>"
            "<p><strong>Key settings to verify before creating VMs:</strong></p>"
            "<ul>"
            "<li>Intel VT-x / AMD-V enabled in UEFI/BIOS</li>"
            "<li>Sufficient free RAM beyond host OS needs</li>"
            "<li>Adequate free disk space (consider thin vs. thick provisioning)</li>"
            "</ul>"
        ),
        "key_points": [
            "Enable Intel VT-x or AMD-V in UEFI/BIOS for hardware-assisted virtualization.",
            "RAM is the most common bottleneck — each VM needs dedicated memory.",
            "SSD storage significantly improves VM I/O performance over HDD.",
            "Each VM has virtual NICs connecting through virtual switches on the host.",
            "Thin provisioning allocates disk on demand; thick provisioning pre-allocates.",
        ],
    },
    {
        "domain": 4,
        "topic": "Client-side virtualization security",
        "objective": "4.2",
        "video": "Client-side Virtualization",
        "study_topics": ["Client-side virtualization security"],
        "body": (
            "<p>Virtualization introduces unique security considerations that go beyond "
            "securing traditional physical machines.</p>"
            "<ul>"
            "<li><strong>VM escape:</strong> A vulnerability where malware running inside "
            "a guest VM breaks out and interacts with the host OS or hypervisor. This is "
            "a serious threat; keeping hypervisor software updated is critical.</li>"
            "<li><strong>VM sprawl:</strong> Uncontrolled proliferation of VMs — because "
            "creating VMs is easy, organizations can end up with hundreds of forgotten, "
            "unpatched VMs. Each abandoned VM is a potential attack surface. Implement "
            "VM lifecycle policies and decommission unused VMs.</li>"
            "<li><strong>Snapshot security:</strong> Snapshots capture the full VM state "
            "including OS vulnerabilities. A VM restored from an old snapshot may be "
            "missing security patches, making it instantly vulnerable. Always patch after "
            "restoring a snapshot.</li>"
            "<li><strong>Guest OS patching:</strong> Each VM requires its own patching "
            "cycle. The hypervisor does not automatically patch guest OSes — each must be "
            "maintained like a physical machine.</li>"
            "<li><strong>Network segmentation:</strong> VMs should be placed on "
            "appropriate virtual network segments. A compromised VM on the same virtual "
            "switch as production systems can conduct lateral movement attacks.</li>"
            "<li><strong>Host security:</strong> Because all VMs share the same physical "
            "host, compromising the host (or hypervisor) compromises every VM on it. "
            "Harden the host OS and limit access to the hypervisor management console.</li>"
            "<li><strong>Shared resources risks:</strong> VMs on the same host share CPU "
            "cache, memory bus, and other hardware. Side-channel attacks (e.g., Spectre, "
            "Meltdown) exploit these shared resources to leak data between VMs.</li>"
            "</ul>"
        ),
        "key_points": [
            "VM escape: malware breaks out of the VM to interact with the host — keep hypervisors patched.",
            "VM sprawl: uncontrolled VM creation leaves unpatched attack surfaces.",
            "Snapshots preserve vulnerabilities — patch immediately after restoring.",
            "Each guest OS needs its own independent patch management.",
            "Segment VM networks to limit lateral movement if one VM is compromised.",
            "Side-channel attacks (Spectre/Meltdown) can leak data between co-hosted VMs.",
        ],
    },
]

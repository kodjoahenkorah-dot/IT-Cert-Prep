"""
Microsoft Azure Fundamentals (AZ-900) Domain 2: Describe Azure architecture and services
Study notes aligned to the official exam skills outline.
"""

NOTES = [
    {
        "domain": 2,
        "topic": "Regions, availability zones, and region pairs",
        "objective": "2.1",
        "video": "Describe the core architectural components of Azure",
        "study_topics": ["Regions, availability zones, and region pairs"],
        "body": (
            "<p>Azure&rsquo;s physical infrastructure is organized so you can place "
            "resources close to users and survive different kinds of failure.</p>"
            "<ul>"
            "<li><strong>Region</strong> &mdash; A set of datacenters deployed within a "
            "defined latency boundary and connected by a dedicated low-latency network. "
            "When you deploy most resources you choose a region.</li>"
            "<li><strong>Availability zones</strong> &mdash; Physically separate "
            "datacenters <em>within</em> a single region, each with independent power, "
            "cooling, and networking. Enabled regions have a minimum of three zones. They "
            "protect against a <em>datacenter</em> failure. A <strong>zonal</strong> "
            "service is pinned to a specific zone; a <strong>zone-redundant</strong> "
            "service is spread automatically across zones.</li>"
            "<li><strong>Region pairs</strong> &mdash; Most regions are paired with another "
            "region in the <em>same geography</em>, at least 300 miles apart, to support "
            "<em>disaster recovery</em>. Planned platform updates are rolled out to paired "
            "regions sequentially (one at a time) to minimize downtime.</li>"
            "<li><strong>Sovereign / special regions</strong> &mdash; Isolated instances "
            "such as <em>Azure Government</em> and <em>Azure China</em> (operated by "
            "21Vianet) exist for compliance and <em>data residency</em> needs.</li>"
            "</ul>"
            "<p>Choosing a region affects latency, feature availability, price, and where "
            "your data physically resides (data residency and sovereignty).</p>"
            "<p><strong>Exam tip:</strong> Availability zones protect against a "
            "<em>datacenter</em> failure inside one region; region pairs protect against a "
            "<em>regional</em> failure and enable DR. Zones are within a region, at least "
            "three; pairs are at least 300 miles apart in the same geography.</p>"
        ),
        "key_points": [
            "Region = datacenters within a latency-defined boundary; you pick one when deploying.",
            "Availability zones = physically separate datacenters in a region (min 3), protecting against datacenter failure.",
            "Zonal = pinned to one zone; zone-redundant = spread across zones automatically.",
            "Region pairs = two regions in the same geography, >=300 miles apart, for DR; updates roll out sequentially.",
            "Sovereign regions (Azure Government, Azure China via 21Vianet) address compliance and data residency.",
        ],
    },
    {
        "domain": 2,
        "topic": "Subscriptions, resource groups, and management groups",
        "objective": "2.1",
        "video": "Describe Azure management infrastructure",
        "study_topics": ["Subscriptions, resource groups, and management groups"],
        "body": (
            "<p>Azure organizes resources in a management hierarchy: <strong>management "
            "group &rarr; subscription &rarr; resource group &rarr; resource</strong>. "
            "Governance applied higher up inherits downward.</p>"
            "<ul>"
            "<li><strong>Resource group</strong> &mdash; A logical container for resources. "
            "Every resource lives in <em>exactly one</em> resource group. Resource groups "
            "<em>cannot</em> be nested. Deleting a resource group deletes everything inside "
            "it. A resource can be in a <em>different region</em> than its resource "
            "group.</li>"
            "<li><strong>Subscription</strong> &mdash; A unit of billing and a boundary of "
            "access and management. A subscription is linked to a single Microsoft Entra "
            "tenant. Organizations use multiple subscriptions to separate billing or "
            "workloads and to work around limits.</li>"
            "<li><strong>Management group</strong> &mdash; A container that organizes "
            "multiple subscriptions so you can apply governance (Azure Policy, RBAC) once "
            "and have it inherit to all subscriptions beneath it. Management groups can be "
            "nested (up to roughly six levels deep).</li>"
            "</ul>"
            "<p><strong>Exam tip:</strong> A resource belongs to one resource group; "
            "resource groups are not nestable and deleting one deletes its contents. A "
            "subscription is the billing/access boundary tied to one Entra tenant; "
            "management groups sit above subscriptions to apply inherited governance.</p>"
        ),
        "key_points": [
            "Hierarchy: management group -> subscription -> resource group -> resource.",
            "A resource lives in exactly one resource group; resource groups cannot be nested.",
            "Deleting a resource group deletes all resources in it; resources may sit in a different region than the group.",
            "A subscription is a billing and access boundary linked to one Microsoft Entra tenant.",
            "Management groups organize many subscriptions and apply Policy/RBAC that inherits downward (nest up to ~6 levels).",
        ],
    },
    {
        "domain": 2,
        "topic": "Azure compute services (VMs, App Service, containers, Functions)",
        "objective": "2.2",
        "video": "Describe Azure compute and networking services",
        "study_topics": ["Azure compute (VMs, App Service, containers, Functions)"],
        "body": (
            "<p>Azure offers several compute options, trading control for convenience:</p>"
            "<ul>"
            "<li><strong>Virtual Machines (IaaS)</strong> &mdash; Full control over the OS "
            "and software. <em>VM Scale Sets</em> deploy and autoscale a group of identical "
            "VMs; <em>availability sets</em> spread VMs across fault and update domains to "
            "protect against hardware failures and maintenance within a datacenter.</li>"
            "<li><strong>Azure App Service (PaaS)</strong> &mdash; Hosts web apps, REST "
            "APIs, and mobile back ends without managing the underlying servers.</li>"
            "<li><strong>Containers</strong> &mdash; <em>Azure Container Instances (ACI)</em> "
            "run single containers quickly with the least overhead; <em>Azure Kubernetes "
            "Service (AKS)</em> orchestrates many containers at scale.</li>"
            "<li><strong>Azure Functions</strong> &mdash; Serverless, event-driven code. You "
            "write a function triggered by an event and are billed per execution "
            "(consumption), with no servers to manage.</li>"
            "<li><strong>Azure Virtual Desktop</strong> &mdash; Cloud-hosted Windows "
            "desktops and apps, including multi-session Windows for many users.</li>"
            "</ul>"
            "<p>Pick VMs when you need full OS control or lift-and-shift; App Service to "
            "host an app without managing servers; ACI for a quick single container and AKS "
            "for orchestration; Functions for short, event-driven tasks.</p>"
            "<p><strong>Exam tip:</strong> &ldquo;Serverless, pay per execution, "
            "event-driven&rdquo; = Azure Functions. Single container fast = ACI; "
            "orchestration at scale = AKS. Full OS control = Virtual Machines.</p>"
        ),
        "key_points": [
            "VMs (IaaS) give full OS control; Scale Sets autoscale identical VMs; availability sets use fault/update domains.",
            "Azure App Service (PaaS) hosts web apps and APIs without managing servers.",
            "ACI runs simple single containers; AKS orchestrates containers at scale.",
            "Azure Functions is serverless and event-driven, billed per execution.",
            "Azure Virtual Desktop delivers cloud-hosted, multi-session Windows desktops.",
        ],
    },
    {
        "domain": 2,
        "topic": "Azure networking (VNet, peering, VPN, ExpressRoute, DNS)",
        "objective": "2.2",
        "video": "Describe Azure compute and networking services",
        "study_topics": ["Azure networking (VNet, peering, VPN, ExpressRoute, DNS)"],
        "body": (
            "<p>Azure networking connects resources privately and links Azure to "
            "on-premises networks.</p>"
            "<ul>"
            "<li><strong>Virtual Network (VNet)</strong> &mdash; A private network in a "
            "region, subdivided into subnets, in which your resources communicate "
            "securely.</li>"
            "<li><strong>VNet peering</strong> &mdash; Connects two VNets over the Microsoft "
            "backbone (regional or global). Peering is <em>non-transitive</em> &mdash; if A "
            "peers with B and B with C, A cannot reach C through B.</li>"
            "<li><strong>VPN Gateway</strong> &mdash; Encrypted site-to-site or "
            "point-to-site tunnels over the <em>public internet</em>.</li>"
            "<li><strong>ExpressRoute</strong> &mdash; A private, dedicated connection "
            "through a connectivity provider that <em>does not traverse the public "
            "internet</em>, offering greater reliability, throughput, and consistent "
            "latency.</li>"
            "<li><strong>Azure DNS</strong> &mdash; Hosts your DNS zones and resolves names "
            "using Azure&rsquo;s infrastructure. It does <em>not</em> register or sell "
            "domain names.</li>"
            "</ul>"
            "<p>Supporting services: <em>public vs private endpoints</em> control exposure; "
            "<em>network security groups (NSGs)</em> filter inbound/outbound traffic; "
            "<em>Azure Bastion</em> provides secure RDP/SSH without public IPs; "
            "<em>Load Balancer</em> distributes traffic at layer 4, while "
            "<em>Application Gateway</em> works at layer 7 and includes a web application "
            "firewall (WAF).</p>"
            "<p><strong>Exam tip:</strong> VPN Gateway rides the public internet "
            "(encrypted); ExpressRoute is private and never touches the public internet. "
            "VNet peering is non-transitive. Azure DNS hosts zones but does not register "
            "domains.</p>"
        ),
        "key_points": [
            "A VNet is a private, regional network divided into subnets for your resources.",
            "VNet peering links VNets over the Microsoft backbone and is non-transitive.",
            "VPN Gateway = encrypted tunnels over the public internet; ExpressRoute = private, dedicated, off the public internet.",
            "Azure DNS hosts DNS zones but does not register/sell domain names.",
            "NSGs filter traffic, Bastion gives RDP/SSH without public IPs, Load Balancer is L4 vs Application Gateway L7 with WAF.",
        ],
    },
    {
        "domain": 2,
        "topic": "Azure storage services and redundancy",
        "objective": "2.3",
        "video": "Describe Azure storage services",
        "study_topics": ["Azure storage services and redundancy"],
        "body": (
            "<p>An <strong>Azure storage account</strong> is the top-level container that "
            "holds the core data services:</p>"
            "<ul>"
            "<li><strong>Blob storage</strong> &mdash; Massively scalable storage for "
            "unstructured objects. Access tiers balance storage vs access cost: "
            "<em>hot</em> (frequent), <em>cool</em>, <em>cold</em>, and <em>archive</em>. "
            "Archive is offline, cheapest to store but most expensive/slow to access, and "
            "must be rehydrated (which can take hours).</li>"
            "<li><strong>Azure Files</strong> &mdash; Fully managed SMB and NFS file shares "
            "you can mount; <em>Azure File Sync</em> keeps on-premises servers in sync with "
            "a share.</li>"
            "<li><strong>Queue storage</strong> and <strong>Table storage</strong> &mdash; "
            "Messaging between components and NoSQL key/value data.</li>"
            "<li><strong>Managed disks</strong> &mdash; Block storage for virtual "
            "machines.</li>"
            "</ul>"
            "<p><strong>Redundancy</strong> determines what failure your data survives:</p>"
            "<ul>"
            "<li><strong>LRS</strong> &mdash; Three copies within a single datacenter.</li>"
            "<li><strong>ZRS</strong> &mdash; Copies across availability zones in one "
            "region.</li>"
            "<li><strong>GRS</strong> &mdash; LRS plus asynchronous copy to the paired "
            "region.</li>"
            "<li><strong>GZRS</strong> &mdash; ZRS plus a copy in the paired region.</li>"
            "<li><strong>RA-</strong> variants (RA-GRS, RA-GZRS) add <em>read access</em> to "
            "the secondary region.</li>"
            "</ul>"
            "<p><strong>Exam tip:</strong> Match redundancy to the failure to survive: LRS "
            "= a disk/rack, ZRS = a whole datacenter/zone, GRS/GZRS = a whole region. "
            "&ldquo;RA-&rdquo; means you can read the secondary copy. Archive tier is "
            "cheapest to store but slow and costly to retrieve.</p>"
        ),
        "key_points": [
            "A storage account holds Blob, Files, Queue, Table data and managed disks.",
            "Blob access tiers: hot, cool, cold, archive; archive is offline, cheapest to store, hours to rehydrate.",
            "Azure Files provides managed SMB/NFS shares; File Sync syncs on-prem servers.",
            "Redundancy: LRS (one datacenter), ZRS (zones in a region), GRS (paired region), GZRS (zones + paired region).",
            "RA- variants add read access to the secondary region; pick redundancy by the failure you must survive.",
        ],
    },
    {
        "domain": 2,
        "topic": "Migration and file movement (Azure Migrate, Data Box, AzCopy)",
        "objective": "2.3",
        "video": "Describe Azure migration and file movement options",
        "study_topics": ["Migration and file movement (Azure Migrate, Data Box, AzCopy)"],
        "body": (
            "<p>Azure provides tools for moving both workloads and files into (and out of) "
            "the cloud.</p>"
            "<ul>"
            "<li><strong>Azure Migrate</strong> &mdash; A central hub to discover, assess, "
            "and migrate servers, databases, web apps, and virtual desktops to Azure, with "
            "tracking throughout the migration.</li>"
            "<li><strong>Azure Data Box</strong> &mdash; A rugged physical appliance "
            "(around 80&nbsp;TB usable) shipped to you for <em>offline</em> bulk data "
            "transfer, both into and out of Azure. Ideal when network transfer would be too "
            "slow or expensive.</li>"
            "<li><strong>AzCopy</strong> &mdash; A command-line tool that copies blobs and "
            "files to and from storage accounts over the network.</li>"
            "<li><strong>Azure Storage Explorer</strong> &mdash; A graphical (GUI) app to "
            "manage and move storage data.</li>"
            "<li><strong>Azure File Sync</strong> &mdash; Synchronizes an on-premises file "
            "server with Azure Files.</li>"
            "</ul>"
            "<p>Choose <em>online</em> tools (AzCopy, Storage Explorer, File Sync) when you "
            "have adequate bandwidth; choose the <em>offline</em> Data Box for very large "
            "datasets or limited connectivity.</p>"
            "<p><strong>Exam tip:</strong> Migrating servers/databases &rarr; Azure Migrate. "
            "Shipping terabytes offline on a physical device &rarr; Data Box. Scripted "
            "command-line copy of blobs/files &rarr; AzCopy.</p>"
        ),
        "key_points": [
            "Azure Migrate is the central hub to discover, assess, and migrate servers, databases, web apps, and VDI.",
            "Azure Data Box is a rugged ~80 TB appliance for offline bulk transfer into and out of Azure.",
            "AzCopy is a command-line tool for copying blobs and files over the network.",
            "Azure Storage Explorer is a GUI for managing storage; Azure File Sync syncs on-prem servers with Azure Files.",
            "Choose online transfer for adequate bandwidth, offline Data Box for very large data or limited connectivity.",
        ],
    },
    {
        "domain": 2,
        "topic": "Microsoft Entra ID and authentication (SSO, MFA, passwordless)",
        "objective": "2.4",
        "video": "Describe Azure identity, access, and security",
        "study_topics": ["Microsoft Entra ID and authentication (SSO, MFA, passwordless)"],
        "body": (
            "<p><strong>Microsoft Entra ID</strong> (formerly Azure Active Directory) is "
            "Microsoft&rsquo;s cloud-based identity and access management service. It stores "
            "users and groups in a <em>tenant</em> and is the basis for single sign-on to "
            "Azure, Microsoft 365, and thousands of SaaS applications.</p>"
            "<ul>"
            "<li><strong>Authentication vs authorization</strong> &mdash; "
            "<em>Authentication (AuthN)</em> proves <em>who you are</em>; "
            "<em>authorization (AuthZ)</em> determines <em>what you are allowed to "
            "do</em>.</li>"
            "<li><strong>Single sign-on (SSO)</strong> &mdash; Sign in once and access many "
            "applications without re-entering credentials.</li>"
            "<li><strong>Multifactor authentication (MFA)</strong> &mdash; Requires two or "
            "more factors: something you <em>know</em> (password/PIN), something you "
            "<em>have</em> (phone, token), or something you <em>are</em> "
            "(biometric).</li>"
            "<li><strong>Passwordless</strong> &mdash; Sign in without a password using "
            "<em>Windows Hello</em>, the <em>Microsoft Authenticator</em> app, or "
            "<em>FIDO2</em> security keys.</li>"
            "<li><strong>Microsoft Entra Domain Services</strong> &mdash; A managed domain "
            "that lets you join VMs to a domain without deploying your own domain "
            "controllers.</li>"
            "</ul>"
            "<p><strong>Exam tip:</strong> Entra ID = cloud identity (renamed from Azure "
            "Active Directory). AuthN is who you are; AuthZ is what you can do. MFA needs "
            "two or more <em>different</em> factor categories &mdash; two passwords do not "
            "count.</p>"
        ),
        "key_points": [
            "Microsoft Entra ID (formerly Azure AD) is cloud identity and access management using tenants, users, and groups.",
            "It underpins single sign-on to Azure, Microsoft 365, and thousands of SaaS apps.",
            "Authentication (AuthN) proves who you are; authorization (AuthZ) decides what you can do.",
            "MFA combines two or more factors: something you know, have, or are.",
            "Passwordless options include Windows Hello, Microsoft Authenticator, and FIDO2 keys; Entra Domain Services offers a managed domain.",
        ],
    },
    {
        "domain": 2,
        "topic": "Conditional Access and external identities",
        "objective": "2.4",
        "video": "Describe Azure identity, access, and security",
        "study_topics": ["Conditional Access and external identities"],
        "body": (
            "<p><strong>Conditional Access</strong> is a Microsoft Entra feature that "
            "enforces <em>if-then</em> policies at sign-in. It gathers <em>signals</em> "
            "&mdash; the user or group, location (IP), device, application being accessed, "
            "and real-time sign-in risk &mdash; and then makes a <em>decision</em>: allow "
            "access, block it, or grant access only if extra requirements are met (for "
            "example, require MFA or a compliant device).</p>"
            "<p>Example: &ldquo;If a user signs in from an unfamiliar location, then require "
            "multifactor authentication.&rdquo; This lets organizations balance security "
            "with usability rather than applying one blanket rule to everyone.</p>"
            "<p><strong>External identities</strong> let people outside your organization "
            "use your resources or apps:</p>"
            "<ul>"
            "<li><strong>B2B (business-to-business)</strong> &mdash; Invite external "
            "partners in as <em>guest users</em> so they can collaborate using their own "
            "credentials.</li>"
            "<li><strong>B2C (business-to-consumer)</strong> &mdash; A customer-facing "
            "identity solution for consumer applications, where users sign up and sign in to "
            "your app.</li>"
            "</ul>"
            "<p><strong>Exam tip:</strong> Conditional Access = signal-driven if-then "
            "policies that can require MFA or block access. B2B = external partners as "
            "guests; B2C = consumer/customer sign-in for your apps.</p>"
        ),
        "key_points": [
            "Conditional Access enforces if-then policies based on signals like user, location, device, app, and sign-in risk.",
            "Decisions can allow, block, or require additional controls such as MFA or a compliant device.",
            "It balances security and usability instead of a single blanket rule.",
            "B2B external identities invite partners as guest users using their own credentials.",
            "B2C provides customer-facing identity for consumer-facing applications.",
        ],
    },
    {
        "domain": 2,
        "topic": "Azure role-based access control (RBAC)",
        "objective": "2.4",
        "video": "Describe Azure identity, access, and security",
        "study_topics": ["Azure RBAC"],
        "body": (
            "<p><strong>Azure role-based access control (RBAC)</strong> grants access by "
            "<em>assigning a role</em> to a <em>security principal</em> at a "
            "<em>scope</em>. Every role assignment has three parts:</p>"
            "<ul>"
            "<li><strong>Security principal</strong> &mdash; A user, group, service "
            "principal, or managed identity.</li>"
            "<li><strong>Role definition</strong> &mdash; A collection of permissions. "
            "Common built-in roles: <em>Owner</em> (full access, including delegating "
            "access to others), <em>Contributor</em> (manage resources but "
            "<em>cannot</em> grant access to others), and <em>Reader</em> (view "
            "only).</li>"
            "<li><strong>Scope</strong> &mdash; Where the access applies: management group, "
            "subscription, resource group, or an individual resource.</li>"
            "</ul>"
            "<p>Assignments <em>inherit downward</em> &mdash; a role granted at a "
            "subscription applies to the resource groups and resources beneath it. RBAC is "
            "<em>additive</em>: your effective permissions are the <em>union</em> of all "
            "your role assignments. Follow the <strong>principle of least privilege</strong> "
            "by granting the narrowest role at the narrowest scope needed.</p>"
            "<p><strong>Exam tip:</strong> Owner can delegate access; Contributor can manage "
            "but not grant access; Reader can only view. Assign roles at the lowest scope "
            "necessary, and remember permissions inherit down the hierarchy.</p>"
        ),
        "key_points": [
            "RBAC assigns a role to a security principal (user, group, service principal, managed identity) at a scope.",
            "Scopes are management group, subscription, resource group, or individual resource.",
            "Built-in roles: Owner (full + delegate), Contributor (manage but not delegate), Reader (view only).",
            "Role assignments inherit down the hierarchy and are additive (the union of assignments).",
            "Apply least privilege: grant the narrowest role at the narrowest scope required.",
        ],
    },
    {
        "domain": 2,
        "topic": "Zero Trust and defense in depth",
        "objective": "2.4",
        "video": "Describe Azure identity, access, and security",
        "study_topics": ["Zero Trust and defense in depth"],
        "body": (
            "<p><strong>Zero Trust</strong> is a security model that assumes no user or "
            "device is trustworthy simply because of where it sits on the network. Its "
            "guiding principles are:</p>"
            "<ul>"
            "<li><strong>Verify explicitly</strong> &mdash; Always authenticate and "
            "authorize using all available signals.</li>"
            "<li><strong>Use least-privilege access</strong> &mdash; Give just enough "
            "access, just in time.</li>"
            "<li><strong>Assume breach</strong> &mdash; Operate as if an attacker is already "
            "present; segment, verify, and monitor everything.</li>"
            "</ul>"
            "<p><strong>Defense in depth</strong> layers multiple, independent security "
            "controls so that no single layer is a single point of failure. The layers, "
            "from outside in, are typically: <em>physical</em>, <em>identity &amp; "
            "access</em>, <em>perimeter</em>, <em>network</em>, <em>compute</em>, "
            "<em>application</em>, and <em>data</em>. If one layer is breached, the next "
            "still stands. <em>Data</em> is the innermost layer and the thing ultimately "
            "being protected.</p>"
            "<p><strong>Exam tip:</strong> Zero Trust = &ldquo;never trust based on network "
            "location; verify explicitly, least privilege, assume breach.&rdquo; Defense in "
            "depth = layered controls; the innermost layer is <em>data</em>.</p>"
        ),
        "key_points": [
            "Zero Trust principles: verify explicitly, use least-privilege access, and assume breach.",
            "Zero Trust never grants trust based on network location alone.",
            "Defense in depth uses multiple independent layers so no single layer is a single point of failure.",
            "Layers outside-in: physical, identity & access, perimeter, network, compute, application, data.",
            "Data is the innermost layer and the ultimate thing being protected.",
        ],
    },
    {
        "domain": 2,
        "topic": "Microsoft Defender for Cloud",
        "objective": "2.4",
        "video": "Describe Azure identity, access, and security",
        "study_topics": ["Microsoft Defender for Cloud"],
        "body": (
            "<p><strong>Microsoft Defender for Cloud</strong> is a tool for monitoring and "
            "strengthening the security posture of your environments. It combines two "
            "capabilities:</p>"
            "<ul>"
            "<li><strong>Cloud security posture management (CSPM)</strong> &mdash; "
            "Continuously assesses your resources, provides a <em>Secure Score</em>, and "
            "offers prioritized <em>security recommendations</em> and regulatory "
            "<em>compliance</em> dashboards.</li>"
            "<li><strong>Cloud workload protection (CWPP)</strong> &mdash; Provides threat "
            "detection and advanced protection for specific resource types through "
            "<em>Defender plans</em> you enable per resource type.</li>"
            "</ul>"
            "<p>Defender for Cloud covers not just Azure but also <em>on-premises</em> and "
            "<em>other clouds</em> (hybrid and multicloud), giving a single view of your "
            "security state across environments.</p>"
            "<p><strong>Exam tip:</strong> Defender for Cloud gives you a <em>Secure "
            "Score</em>, security recommendations, compliance dashboards, and threat "
            "protection &mdash; across Azure, on-premises, and other clouds. Advanced "
            "protection is turned on per resource type via Defender plans.</p>"
        ),
        "key_points": [
            "Microsoft Defender for Cloud combines posture management (CSPM) and workload protection (CWPP).",
            "It provides a Secure Score, security recommendations, and regulatory compliance dashboards.",
            "It delivers threat detection and protection for workloads.",
            "Coverage spans Azure, on-premises, and other clouds (hybrid and multicloud).",
            "Defender plans enable advanced protection per resource type.",
        ],
    },
]

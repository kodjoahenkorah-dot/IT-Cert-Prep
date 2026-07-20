"""
Microsoft Azure Fundamentals (AZ-900) Domain 1: Describe cloud concepts
Study notes aligned to the official exam skills outline.
"""

NOTES = [
    {
        "domain": 1,
        "topic": "Cloud computing and the shared responsibility model",
        "objective": "1.1",
        "video": "Describe cloud computing",
        "study_topics": ["Cloud computing and shared responsibility"],
        "body": (
            "<p><strong>Cloud computing</strong> is the delivery of computing services "
            "&mdash; servers, storage, databases, networking, software, and analytics "
            "&mdash; over the internet (&ldquo;the cloud&rdquo;), paying only for what you "
            "use. It lets organizations avoid buying and maintaining their own physical "
            "datacenters and hardware.</p>"
            "<p><strong>The shared responsibility model</strong> defines who secures and "
            "manages what &mdash; you (the customer) or the cloud provider (Microsoft). "
            "Responsibility shifts depending on the service model:</p>"
            "<ul>"
            "<li><strong>Always the customer&rsquo;s responsibility</strong>, in every "
            "model: your <em>information and data</em>, <em>devices</em> (mobile and PCs), "
            "and <em>accounts and identities</em>.</li>"
            "<li><strong>Always the provider&rsquo;s responsibility</strong>, in every "
            "model: the <em>physical hosts</em>, <em>physical network</em>, and "
            "<em>physical datacenter</em>.</li>"
            "<li><strong>Varies by model</strong> (operating system, network controls, "
            "applications, identity infrastructure): the customer owns more in IaaS and "
            "progressively less as you move to PaaS and then SaaS.</li>"
            "</ul>"
            "<p>Think of it as renting: renting an unfurnished house (IaaS) means you "
            "furnish and maintain almost everything inside; a serviced apartment (PaaS) "
            "handles the building and utilities while you bring your belongings; a hotel "
            "(SaaS) manages nearly everything and you just use the room.</p>"
            "<p><strong>Exam tip:</strong> Data, devices, and identities/accounts are "
            "<em>always</em> yours to protect &mdash; even in SaaS. Physical datacenter, "
            "hosts, and physical network are <em>always</em> Microsoft&rsquo;s.</p>"
        ),
        "key_points": [
            "Cloud computing = renting IT services over the internet, pay-as-you-go.",
            "Shared responsibility splits security/management duties between customer and provider.",
            "Customer ALWAYS owns: data, devices, and accounts/identities.",
            "Provider ALWAYS owns: physical datacenter, physical network, physical hosts.",
            "The middle layers (OS, apps, network controls) shift from customer (IaaS) toward provider (SaaS).",
        ],
    },
    {
        "domain": 1,
        "topic": "Cloud deployment models (public, private, hybrid)",
        "objective": "1.1",
        "video": "Describe cloud deployment models",
        "study_topics": ["Cloud deployment models (public/private/hybrid)"],
        "body": (
            "<p>A <strong>deployment model</strong> describes where the cloud resources "
            "live and who has access to them.</p>"
            "<ul>"
            "<li><strong>Public cloud</strong> &mdash; Services are owned and operated by "
            "a third-party provider (like Microsoft Azure) and delivered over the public "
            "internet. Infrastructure is shared among many organizations (multi-tenant). "
            "No capital expense, high scalability, but less control over the underlying "
            "hardware.</li>"
            "<li><strong>Private cloud</strong> &mdash; Cloud resources used exclusively by "
            "a single organization. It can be hosted in the organization&rsquo;s own "
            "on-premises datacenter <em>or</em> hosted for it by a third party. Offers the "
            "most control and can meet strict regulatory or data-residency requirements, "
            "but the organization bears more cost and management.</li>"
            "<li><strong>Hybrid cloud</strong> &mdash; Combines public and private (or "
            "on-premises), connecting them so workloads and data can move between them. "
            "Provides flexibility: keep sensitive workloads private while bursting to the "
            "public cloud for extra capacity, or gradually migrate.</li>"
            "</ul>"
            "<p>A related term is <strong>multi-cloud</strong> (using more than one public "
            "cloud provider). Azure Arc and Azure VMware Solution help manage hybrid and "
            "multi-cloud environments.</p>"
            "<p><strong>Exam tip:</strong> A private cloud is defined by <em>exclusive "
            "single-organization use</em>, NOT by location &mdash; it can still be hosted "
            "by a third party. If a scenario mixes on-premises/private with public cloud, "
            "the answer is hybrid.</p>"
        ),
        "key_points": [
            "Public: shared, provider-owned, over the internet; most scalable, least control.",
            "Private: exclusive to one organization; can be on-prem OR third-party hosted.",
            "Hybrid: connects public + private/on-prem so workloads span both.",
            "Private cloud is about exclusive use, not physical location.",
            "Hybrid suits regulatory data residency + burst capacity + gradual migration.",
        ],
    },
    {
        "domain": 1,
        "topic": "Consumption-based model and CapEx vs OpEx",
        "objective": "1.1",
        "video": "Describe the consumption-based model",
        "study_topics": ["Consumption model and CapEx vs OpEx"],
        "body": (
            "<p>Cloud pricing uses a <strong>consumption-based model</strong>: you pay only "
            "for the resources you actually use, with no up-front cost and no charge for "
            "capacity you don&rsquo;t consume. You can scale up or down and stop paying "
            "when you deprovision a resource.</p>"
            "<p><strong>CapEx vs OpEx:</strong></p>"
            "<ul>"
            "<li><strong>Capital Expenditure (CapEx)</strong> &mdash; A large up-front "
            "purchase of physical infrastructure (servers, datacenter buildout) that is "
            "then depreciated over time. Typical of on-premises. Requires predicting "
            "capacity in advance.</li>"
            "<li><strong>Operational Expenditure (OpEx)</strong> &mdash; Ongoing "
            "pay-as-you-go spending on services you consume, expensed immediately. Typical "
            "of cloud. No up-front hardware purchase; no need to predict demand precisely.</li>"
            "</ul>"
            "<p>Benefits of the consumption model: no up-front capital cost, no over- or "
            "under-provisioning, pay for what you use, and the ability to stop paying for "
            "resources you no longer need.</p>"
            "<p><strong>Exam tip:</strong> Buying physical servers = CapEx. Paying a monthly "
            "Azure bill for what you consumed = OpEx. Moving to the cloud generally shifts "
            "spending from CapEx to OpEx.</p>"
        ),
        "key_points": [
            "Consumption-based = pay only for what you use, no up-front cost.",
            "CapEx = large up-front purchase of infrastructure (on-prem style).",
            "OpEx = ongoing pay-as-you-go operating spend (cloud style).",
            "Cloud removes the need to predict capacity in advance.",
            "Deprovisioning a resource stops its charges.",
        ],
    },
    {
        "domain": 1,
        "topic": "Benefits of cloud (HA, scalability, elasticity, reliability, DR)",
        "objective": "1.2",
        "video": "Describe the benefits of high availability and scalability",
        "study_topics": ["Cloud benefits (HA, scalability, elasticity, DR)"],
        "body": (
            "<p>The cloud provides several benefits the exam expects you to distinguish:</p>"
            "<ul>"
            "<li><strong>High availability (HA)</strong> &mdash; Keeping services running "
            "with minimal downtime, usually expressed as an uptime percentage in an SLA "
            "(e.g., 99.9%). Achieved with redundancy such as availability zones.</li>"
            "<li><strong>Scalability</strong> &mdash; The ability to add resources to meet "
            "demand. <em>Vertical scaling (scale up/down)</em> means increasing/decreasing "
            "the power of an instance (bigger VM). <em>Horizontal scaling (scale out/in)</em> "
            "means adding/removing instances (more VMs).</li>"
            "<li><strong>Elasticity</strong> &mdash; Automatically adding or removing "
            "resources as demand changes, so you pay only for what you need moment to "
            "moment. (Scalability is the <em>capability</em>; elasticity is doing it "
            "<em>automatically</em> in response to load.)</li>"
            "<li><strong>Reliability</strong> &mdash; The ability of a system to recover "
            "from failures and continue functioning, supported by the cloud&rsquo;s "
            "distributed, redundant design.</li>"
            "<li><strong>Predictability</strong> &mdash; Predictable <em>performance</em> "
            "(scale to maintain user experience) and predictable <em>cost</em> (tools to "
            "forecast and control spend).</li>"
            "<li><strong>Disaster recovery (DR)</strong> &mdash; Restoring service after a "
            "major outage, using geographically distributed regions and region pairs, "
            "backups, and replication.</li>"
            "<li><strong>Agility</strong> &mdash; Rapidly provisioning resources; "
            "<strong>geo-distribution</strong> &mdash; deploying apps/data close to users "
            "worldwide.</li>"
            "</ul>"
            "<p><strong>Exam tip:</strong> <em>Scalability</em> is the ability to grow; "
            "<em>elasticity</em> is automatic scaling with demand. <em>Availability</em> = "
            "uptime now; <em>reliability</em> = recovering from failure over time. Adding "
            "more VMs is horizontal (out); a bigger VM is vertical (up).</p>"
        ),
        "key_points": [
            "High availability = minimal downtime, expressed as an SLA uptime %.",
            "Vertical scaling = up/down (bigger/smaller instance); horizontal = out/in (more/fewer instances).",
            "Elasticity = automatic scaling in response to demand.",
            "Reliability = recover from failures; availability = stay up now.",
            "DR uses geo-distribution and region pairs; agility = fast provisioning.",
        ],
    },
    {
        "domain": 1,
        "topic": "Cloud service types (IaaS, PaaS, SaaS)",
        "objective": "1.3",
        "video": "Describe cloud service types",
        "study_topics": ["Cloud service types (IaaS/PaaS/SaaS)"],
        "body": (
            "<p><strong>Service types</strong> describe how much the provider manages "
            "versus how much you manage. From most customer control to least:</p>"
            "<ul>"
            "<li><strong>IaaS (Infrastructure as a Service)</strong> &mdash; You rent the "
            "infrastructure (virtual machines, storage, networking). You manage the OS, "
            "patching, applications, and runtime; the provider manages the physical "
            "hardware and virtualization. <em>Most flexibility, most management "
            "responsibility.</em> Example: Azure Virtual Machines. Good for lift-and-shift "
            "migrations and full control over the OS.</li>"
            "<li><strong>PaaS (Platform as a Service)</strong> &mdash; The provider manages "
            "the OS, runtime, and middleware; you provide and manage your application code "
            "and data. <em>A managed platform so developers focus on building, not "
            "servers.</em> Examples: Azure App Service, Azure SQL Database. Serverless "
            "(e.g., Azure Functions) is often discussed as part of PaaS.</li>"
            "<li><strong>SaaS (Software as a Service)</strong> &mdash; The provider manages "
            "essentially everything; you just use a finished application over the internet "
            "and manage your data, users, and access. <em>Least management "
            "responsibility.</em> Example: Microsoft 365.</li>"
            "</ul>"
            "<p>Matching scenarios: full control / migrate existing servers &rarr; IaaS; "
            "host an app without managing servers &rarr; PaaS; ready-to-use software "
            "&rarr; SaaS.</p>"
            "<p><strong>Exam tip:</strong> Remember the management gradient &mdash; IaaS "
            "(you manage the OS up), PaaS (you manage the app/data), SaaS (you manage just "
            "your data and users). VMs = IaaS, App Service = PaaS, Microsoft 365 = SaaS.</p>"
        ),
        "key_points": [
            "IaaS: rent infrastructure (VMs); you manage OS + apps; most control.",
            "PaaS: managed platform (App Service, Azure SQL DB); you bring code/data.",
            "SaaS: finished software (Microsoft 365); provider manages almost everything.",
            "Management responsibility decreases IaaS -> PaaS -> SaaS.",
            "Serverless (Azure Functions) is generally categorized under PaaS.",
        ],
    },
]

"""
Microsoft Azure Fundamentals (AZ-900) Domain 3: Describe Azure management and governance
Original study notes — not reproduced from any copyrighted source.
"""

NOTES = [
    {
        "domain": 3,
        "topic": "Cost Factors and the Pricing & TCO Calculators",
        "objective": "3.1",
        "video": "Plan and manage costs in Azure",
        "study_topics": ["Cost factors and pricing/TCO calculators"],
        "body": (
            "<p>In Azure&rsquo;s consumption model you generally pay only for what you use, so understanding the "
            "<strong>factors that affect cost</strong> is essential:</p>"
            "<ul>"
            "<li><strong>Resource type and size/SKU</strong> &mdash; a larger VM or a premium storage tier costs more.</li>"
            "<li><strong>Consumption/usage</strong> &mdash; how much compute, storage, and other services you actually consume.</li>"
            "<li><strong>Location/region</strong> &mdash; prices vary by region, so the same resource can cost different amounts in different datacenters.</li>"
            "<li><strong>Network traffic</strong> &mdash; outbound (egress) data transfer is typically billed, while inbound (ingress) traffic is generally free.</li>"
            "<li><strong>Subscription type, Azure Marketplace third-party products, and maintenance</strong> also influence the bill.</li>"
            "</ul>"
            "<p>You can reduce cost with commitments: <strong>reserved instances</strong> and <strong>savings plans</strong> "
            "discount committed usage (up to roughly <strong>72%</strong> versus pay-as-you-go). Note that a "
            "<em>deallocated</em> VM stops compute charges, but its attached <strong>disks still bill</strong> for storage.</p>"
            "<p>Two free planning tools help you estimate spend:</p>"
            "<ul>"
            "<li><strong>Pricing calculator</strong> &mdash; estimate the cost of <em>new</em> Azure services you plan to deploy.</li>"
            "<li><strong>Total Cost of Ownership (TCO) calculator</strong> &mdash; compare your current on-premises costs against Azure to estimate migration savings.</li>"
            "</ul>"
            "<p><strong>Exam tip:</strong> Remember the split &rarr; <em>Pricing</em> calculator estimates new cloud deployments; "
            "<em>TCO</em> calculator compares on-premises versus Azure. Also recall that egress traffic is billed but ingress usually is not.</p>"
        ),
        "key_points": [
            "Cost drivers: resource type/SKU, usage, region, network egress, subscription type, and Marketplace products.",
            "Outbound (egress) data transfer is billed; inbound (ingress) is generally free.",
            "Reservations and savings plans discount committed usage by up to ~72%.",
            "A deallocated VM stops compute charges, but its disks keep incurring storage costs.",
            "Pricing calculator = estimate NEW services; TCO calculator = compare on-premises vs Azure.",
        ],
    },
    {
        "domain": 3,
        "topic": "Microsoft Cost Management and Resource Tags",
        "objective": "3.1",
        "video": "Monitor and optimize spend with Cost Management",
        "study_topics": ["Cost Management and tags"],
        "body": (
            "<p><strong>Microsoft Cost Management</strong> is a suite of tools that helps you monitor, allocate, and "
            "optimize your Azure spend. Its main capabilities are:</p>"
            "<ul>"
            "<li><strong>Cost analysis</strong> &mdash; visualize and break down spending by service, resource group, tag, and more.</li>"
            "<li><strong>Budgets</strong> and <strong>budget alerts</strong> &mdash; set spending thresholds and get notified when you approach them. "
            "Important: alerts <em>notify</em> you but do <strong>not</strong> automatically stop or delete resources by default.</li>"
            "<li><strong>Exports</strong> &mdash; schedule cost data exports for external reporting and analysis.</li>"
            "</ul>"
            "<p><strong>Resource tags</strong> are name/value metadata pairs you apply to resources, resource groups, and subscriptions. "
            "They help you organize resources and report on costs (for example, tagging by department, environment, or cost center). "
            "Key facts to remember:</p>"
            "<ul>"
            "<li>Tags are <strong>not inherited</strong> by default &mdash; a tag on a resource group does not automatically flow to the resources inside it.</li>"
            "<li>You can <strong>require or apply tags</strong> automatically by using <strong>Azure Policy</strong>.</li>"
            "</ul>"
            "<p><strong>Exam tip:</strong> A budget alert only sends a notification &mdash; it will not shut anything down. "
            "And when a scenario mentions grouping cost by department or environment, the answer is usually <em>tags</em>.</p>"
        ),
        "key_points": [
            "Cost Management provides cost analysis, budgets, budget alerts, and exports.",
            "Budget alerts notify you but do NOT automatically stop or delete resources.",
            "Tags are name/value pairs used to organize resources and report on costs.",
            "Tags are NOT inherited by default from a resource group or subscription.",
            "Azure Policy can enforce or apply required tags across resources.",
        ],
    },
    {
        "domain": 3,
        "topic": "Azure Policy",
        "objective": "3.2",
        "video": "Enforce standards with Azure Policy",
        "study_topics": ["Azure Policy"],
        "body": (
            "<p><strong>Azure Policy</strong> helps you enforce organizational standards and assess compliance at scale. "
            "It continuously evaluates your resources and reports which ones are compliant or non-compliant.</p>"
            "<p>The building blocks are:</p>"
            "<ul>"
            "<li><strong>Policy definition</strong> &mdash; a single rule with an <em>effect</em>, such as <strong>audit</strong> (flag it) or <strong>deny</strong> (block creation).</li>"
            "<li><strong>Initiative</strong> &mdash; a group of related policy definitions treated as one unit.</li>"
            "<li><strong>Assignment</strong> &mdash; applying a policy or initiative to a <strong>scope</strong> (management group, subscription, or resource group).</li>"
            "</ul>"
            "<p>Azure Policy provides a <strong>compliance dashboard</strong>, can <strong>auto-remediate</strong> non-compliant "
            "resources, and assignments <strong>inherit down</strong> the management hierarchy to child scopes.</p>"
            "<p>Do not confuse Azure Policy with <strong>RBAC</strong>: Azure Policy governs <em>what</em> resources and properties are "
            "allowed (for example, only certain regions or SKUs), while <strong>RBAC</strong> governs <em>who</em> can perform actions.</p>"
            "<p><strong>Exam tip:</strong> If a question asks how to ensure resources are only deployed in approved regions or with required "
            "tags, the answer is <em>Azure Policy</em>. &ldquo;Who can do what&rdquo; is RBAC; &ldquo;what is allowed&rdquo; is Policy.</p>"
        ),
        "key_points": [
            "Azure Policy enforces standards and assesses compliance at scale.",
            "Definitions have effects like audit and deny; initiatives group definitions.",
            "Assignments apply at a scope and inherit down the hierarchy.",
            "Provides a compliance dashboard and can auto-remediate non-compliant resources.",
            "Policy = what resources/properties are allowed; RBAC = who can do what.",
        ],
    },
    {
        "domain": 3,
        "topic": "Resource Locks",
        "objective": "3.2",
        "video": "Protect resources with locks",
        "study_topics": ["Resource locks"],
        "body": (
            "<p><strong>Resource locks</strong> protect your Azure resources from accidental change or deletion. "
            "There are two lock types:</p>"
            "<ul>"
            "<li><strong>Delete (CanNotDelete)</strong> &mdash; you can still read and modify the resource, but you cannot delete it.</li>"
            "<li><strong>ReadOnly</strong> &mdash; you can read the resource, but you cannot modify or delete it.</li>"
            "</ul>"
            "<p>Key behaviors to remember:</p>"
            "<ul>"
            "<li>Locks apply to <strong>all users</strong>, including subscription <strong>Owners</strong> &mdash; they are not a per-user permission.</li>"
            "<li>Locks are <strong>inherited</strong> by child resources within the locked scope.</li>"
            "<li>You must <strong>remove the lock</strong> before you can perform the blocked action.</li>"
            "</ul>"
            "<p>Resource locks complement other governance controls: <strong>Azure Policy</strong> enforces standards, and "
            "<strong>backups</strong> protect data, while locks specifically guard against accidental modification or deletion.</p>"
            "<p><strong>Exam tip:</strong> A <em>Delete</em> lock still allows changes but blocks deletion; a <em>ReadOnly</em> lock blocks "
            "both changes and deletion. Because locks affect even Owners, you must remove the lock first to complete a blocked operation.</p>"
        ),
        "key_points": [
            "Two lock types: Delete (CanNotDelete) and ReadOnly.",
            "Delete lock allows read/modify but blocks deletion; ReadOnly blocks modify and delete.",
            "Locks apply to all users, including Owners, and are inherited by child resources.",
            "You must remove a lock before performing the blocked action.",
            "Locks complement Azure Policy and backups as a governance safeguard.",
        ],
    },
    {
        "domain": 3,
        "topic": "Microsoft Purview",
        "objective": "3.2",
        "video": "Govern your data with Microsoft Purview",
        "study_topics": ["Microsoft Purview"],
        "body": (
            "<p><strong>Microsoft Purview</strong> is a unified <strong>data governance and compliance</strong> solution. "
            "Where Azure Policy and locks govern your <em>resources</em>, Purview governs your <strong>data estate</strong>.</p>"
            "<p>At the fundamentals level, remember that Purview helps you:</p>"
            "<ul>"
            "<li>Build a <strong>data map and catalog</strong> and track <strong>data lineage</strong> across your environment.</li>"
            "<li>Cover data spanning <strong>on-premises, multicloud, and SaaS</strong> sources.</li>"
            "<li><strong>Discover, classify, and govern</strong> data so you know what you have and where it lives.</li>"
            "<li>Support <strong>risk and compliance management</strong> across the organization.</li>"
            "</ul>"
            "<p>Purview gives you a single place to understand and manage sensitive information across a sprawling, multi-source "
            "data landscape, which is increasingly important for regulatory compliance.</p>"
            "<p><strong>Exam tip:</strong> When a question is about governing, discovering, or classifying <em>data</em> "
            "(not compute resources), the answer is <em>Microsoft Purview</em>.</p>"
        ),
        "key_points": [
            "Microsoft Purview is a unified data governance and compliance solution.",
            "Provides a data map/catalog and lineage across your data estate.",
            "Covers on-premises, multicloud, and SaaS data sources.",
            "Helps discover, classify, and govern data and manage risk/compliance.",
            "Purview governs DATA; Azure Policy and locks govern RESOURCES.",
        ],
    },
    {
        "domain": 3,
        "topic": "Azure Arc",
        "objective": "3.3",
        "video": "Extend Azure management with Azure Arc",
        "study_topics": ["Azure Arc"],
        "body": (
            "<p><strong>Azure Arc</strong> extends Azure management and governance to resources that live "
            "<strong>outside Azure</strong> &mdash; in your own datacenter (on-premises) and in other clouds.</p>"
            "<p>With Azure Arc you can <em>project</em> external resources into Azure so they appear in Azure Resource Manager and can be "
            "managed alongside native Azure resources. Arc supports:</p>"
            "<ul>"
            "<li><strong>Servers</strong> (Windows and Linux machines, wherever they run).</li>"
            "<li><strong>Kubernetes clusters</strong> running anywhere.</li>"
            "<li>Certain <strong>Azure data services</strong> running outside Azure.</li>"
            "</ul>"
            "<p>Once projected, you can apply consistent controls from a single control plane: <strong>Azure Policy</strong>, "
            "<strong>RBAC</strong>, <strong>tags</strong>, and <strong>monitoring</strong> &mdash; giving you one place to govern a hybrid or "
            "multicloud estate.</p>"
            "<p><strong>Exam tip:</strong> If the scenario involves managing on-premises or other-cloud resources <em>with the same Azure "
            "tools</em>, the answer is <em>Azure Arc</em>.</p>"
        ),
        "key_points": [
            "Azure Arc extends Azure management to resources outside Azure (on-premises and other clouds).",
            "Supports servers, Kubernetes clusters, and some Azure data services.",
            "Projects external resources into Azure Resource Manager as a single control plane.",
            "Lets you apply Azure Policy, RBAC, tags, and monitoring consistently.",
            "Answer for hybrid/multicloud governance with native Azure tooling.",
        ],
    },
    {
        "domain": 3,
        "topic": "Infrastructure as Code and ARM Templates",
        "objective": "3.3",
        "video": "Deploy with ARM templates and Bicep",
        "study_topics": ["Infrastructure as code and ARM templates"],
        "body": (
            "<p><strong>Infrastructure as Code (IaC)</strong> means managing and provisioning infrastructure through "
            "<strong>declarative configuration files</strong> rather than manual clicks. This gives you deployments that are "
            "<strong>repeatable, consistent, and versionable</strong> (stored in source control).</p>"
            "<p><strong>Azure Resource Manager (ARM)</strong> is the deployment and management layer for Azure. Every request &mdash; "
            "whether it comes from the portal, the CLI, PowerShell, or the REST API &mdash; goes through ARM, which "
            "<strong>authenticates and authorizes</strong> it before acting.</p>"
            "<p><strong>ARM templates</strong> are declarative <strong>JSON</strong> files that describe the resources you want. They are:</p>"
            "<ul>"
            "<li><strong>Idempotent</strong> &mdash; deploying the same template repeatedly yields the same result.</li>"
            "<li>Able to deploy <strong>many resources with dependencies</strong> in the correct order.</li>"
            "<li><strong>Validated</strong> before deployment to catch errors early.</li>"
            "</ul>"
            "<p><strong>Bicep</strong> is a simpler, more readable declarative language that <em>transpiles</em> to ARM JSON, offering the "
            "same capabilities with cleaner syntax.</p>"
            "<p><strong>Exam tip:</strong> Remember that <em>everything</em> routes through ARM, ARM templates are declarative JSON and "
            "idempotent, and Bicep is the friendlier language that compiles down to ARM JSON.</p>"
        ),
        "key_points": [
            "IaC uses declarative config files for repeatable, consistent, versionable deployments.",
            "Azure Resource Manager (ARM) receives and authorizes every request (portal, CLI, PowerShell, REST).",
            "ARM templates are declarative JSON, idempotent, and validated before deployment.",
            "Templates can deploy many resources with dependencies handled automatically.",
            "Bicep is a simpler declarative language that transpiles to ARM JSON.",
        ],
    },
    {
        "domain": 3,
        "topic": "Azure Portal, CLI, PowerShell, and Cloud Shell",
        "objective": "3.3",
        "video": "Choose the right Azure management tool",
        "study_topics": ["Azure portal, CLI, PowerShell, and Cloud Shell"],
        "body": (
            "<p>Azure offers several tools to create and manage resources, each suited to different needs:</p>"
            "<ul>"
            "<li><strong>Azure portal</strong> &mdash; a web-based graphical user interface (GUI); great for one-off tasks and visual exploration.</li>"
            "<li><strong>Azure CLI</strong> &mdash; a cross-platform command-line tool using <code>az</code> commands; scriptable for automation.</li>"
            "<li><strong>Azure PowerShell</strong> &mdash; the <strong>Az module</strong> of cmdlets for those who prefer PowerShell scripting.</li>"
            "<li><strong>Azure Cloud Shell</strong> &mdash; a browser-based shell (choose <strong>Bash</strong> or <strong>PowerShell</strong>) with tools "
            "pre-installed and <strong>no local setup</strong>, backed by persistent storage for your files.</li>"
            "<li><strong>Azure mobile app</strong> &mdash; monitor and manage resources from a phone.</li>"
            "</ul>"
            "<p>Choose a <strong>GUI</strong> (portal) for one-off or visual work, and <strong>CLI or PowerShell</strong> for automation and "
            "repeatability. Regardless of which tool you use, all of them ultimately call <strong>Azure Resource Manager (ARM)</strong>.</p>"
            "<p><strong>Exam tip:</strong> Cloud Shell is the <em>browser-based</em> option that needs no local install and offers both Bash and "
            "PowerShell. For repeatable automation, pick CLI or PowerShell over the portal.</p>"
        ),
        "key_points": [
            "Azure portal is the web-based GUI, ideal for one-off and visual tasks.",
            "Azure CLI (az) and Azure PowerShell (Az module) are scriptable for automation.",
            "Cloud Shell is a browser-based Bash/PowerShell shell with tools pre-installed and persistent storage.",
            "No local setup is needed for Cloud Shell; a mobile app is also available.",
            "All tools ultimately route their requests through Azure Resource Manager (ARM).",
        ],
    },
    {
        "domain": 3,
        "topic": "Azure Advisor",
        "objective": "3.4",
        "video": "Optimize with Azure Advisor",
        "study_topics": ["Azure Advisor"],
        "body": (
            "<p><strong>Azure Advisor</strong> is a <strong>free</strong> service that analyzes your configurations and usage, then "
            "provides <strong>personalized recommendations</strong> to follow best practices and optimize your deployments.</p>"
            "<p>Recommendations are organized into <strong>five categories</strong>, aligned to the pillars of a well-architected environment:</p>"
            "<ul>"
            "<li><strong>Reliability</strong> &mdash; improve the continuity of your business-critical applications.</li>"
            "<li><strong>Security</strong> &mdash; detect threats and vulnerabilities (integrated with Microsoft Defender for Cloud).</li>"
            "<li><strong>Performance</strong> &mdash; improve the speed and responsiveness of your applications.</li>"
            "<li><strong>Cost</strong> &mdash; reduce overall spending by identifying idle or underused resources.</li>"
            "<li><strong>Operational Excellence</strong> &mdash; improve process and workflow efficiency and manageability.</li>"
            "</ul>"
            "<p>Advisor presents these as an actionable dashboard so you can quickly see and apply improvements.</p>"
            "<p><strong>Exam tip:</strong> Memorize the five categories &rarr; <em>Reliability, Security, Performance, Cost, and Operational "
            "Excellence</em>. Advisor is free, and its security recommendations tie into Defender for Cloud.</p>"
        ),
        "key_points": [
            "Azure Advisor is free and gives personalized best-practice recommendations.",
            "Five categories: Reliability, Security, Performance, Cost, and Operational Excellence.",
            "Helps optimize deployments across reliability, security, performance, and cost.",
            "Security recommendations integrate with Microsoft Defender for Cloud.",
            "Presented as an actionable dashboard of prioritized improvements.",
        ],
    },
    {
        "domain": 3,
        "topic": "Azure Service Health",
        "objective": "3.4",
        "video": "Track availability with Azure Service Health",
        "study_topics": ["Azure Service Health"],
        "body": (
            "<p><strong>Azure Service Health</strong> gives you a <strong>personalized</strong> view of the health of the Azure services and "
            "regions you actually use &mdash; unlike the public Azure status page, which shows only global information.</p>"
            "<p>It brings together three areas:</p>"
            "<ul>"
            "<li><strong>Azure status</strong> &mdash; a global view of major, widespread outages affecting all of Azure.</li>"
            "<li><strong>Service Health</strong> &mdash; a personalized view of <em>service issues, planned maintenance, and health advisories</em> "
            "that affect the services and regions you use.</li>"
            "<li><strong>Resource Health</strong> &mdash; the health of your <em>specific</em> resources (for example, an individual VM).</li>"
            "</ul>"
            "<p>You can configure <strong>alerts</strong> to be notified of relevant events, and review <strong>issue history</strong> and "
            "root-cause analyses after an incident.</p>"
            "<p><strong>Exam tip:</strong> The public Azure status page is global and impersonal; <em>Service Health</em> is the personalized view "
            "of issues affecting <em>your</em> services, and <em>Resource Health</em> drills down to an individual resource.</p>"
        ),
        "key_points": [
            "Service Health gives a personalized view of the services and regions you use.",
            "Three areas: Azure status (global), Service Health (your services), Resource Health (your resource).",
            "Covers service issues, planned maintenance, and health advisories.",
            "Configurable alerts notify you of relevant events; issue history aids root-cause analysis.",
            "Contrast with the public Azure status page, which is global and not personalized.",
        ],
    },
    {
        "domain": 3,
        "topic": "Azure Monitor (Log Analytics, Alerts, Application Insights)",
        "objective": "3.4",
        "video": "Observe everything with Azure Monitor",
        "study_topics": ["Azure Monitor (Log Analytics, alerts, Application Insights)"],
        "body": (
            "<p><strong>Azure Monitor</strong> is a full-stack monitoring platform that collects, analyzes, and acts on "
            "<strong>metrics</strong> and <strong>logs</strong> from Azure, on-premises, and other clouds.</p>"
            "<p>Its key components are:</p>"
            "<ul>"
            "<li><strong>Log Analytics</strong> &mdash; a workspace where you query collected log data using <strong>KQL</strong> "
            "(Kusto Query Language).</li>"
            "<li><strong>Alerts</strong> and <strong>action groups</strong> &mdash; alerts fire when a condition is met, and action groups define "
            "the response (email, SMS, webhook, or automation).</li>"
            "<li><strong>Application Insights</strong> &mdash; application performance monitoring (APM) for live web apps, tracking availability, "
            "response times, failures, and dependencies.</li>"
            "</ul>"
            "<p>Azure Monitor also underpins features such as <strong>autoscale</strong> and customizable <strong>dashboards</strong>, giving you a "
            "single observability platform.</p>"
            "<p><strong>Exam tip:</strong> Match the piece to the job &rarr; <em>Log Analytics</em> queries logs with KQL, <em>Application "
            "Insights</em> monitors application performance, and <em>alerts</em> (with action groups) trigger notifications or automated responses.</p>"
        ),
        "key_points": [
            "Azure Monitor collects metrics and logs from Azure, on-premises, and other clouds.",
            "Log Analytics is the workspace for querying log data with KQL.",
            "Alerts with action groups trigger email, SMS, webhook, or automation responses.",
            "Application Insights provides APM for live web apps (availability, latency, failures, dependencies).",
            "Underpins autoscale and dashboards as a unified observability platform.",
        ],
    },
    {
        "domain": 3,
        "topic": "SLAs and the Service Lifecycle",
        "objective": "3.4",
        "video": "Understand SLAs and service lifecycle",
        "study_topics": ["SLAs and service lifecycle"],
        "body": (
            "<p>A <strong>Service Level Agreement (SLA)</strong> is Microsoft&rsquo;s formal, financially backed commitment to a service&rsquo;s "
            "uptime and connectivity (for example, <strong>99.9%</strong>). If Microsoft misses the target, you may receive "
            "<strong>service credits</strong>.</p>"
            "<p>Important SLA concepts:</p>"
            "<ul>"
            "<li>Adding <strong>redundancy</strong> (for example, deploying across availability zones) raises your effective availability.</li>"
            "<li>A <strong>composite (combined) SLA</strong> for chained, dependent services is <em>lower</em> than any single component &mdash; "
            "you <strong>multiply</strong> them (e.g., 99.9% &times; 99.9% &asymp; 99.8%).</li>"
            "<li>Rough downtime budgets: <strong>99.9%</strong> &asymp; ~43 minutes/month; <strong>99.99%</strong> &asymp; ~4 minutes/month.</li>"
            "</ul>"
            "<p>The <strong>service lifecycle</strong> also matters: features in <strong>private or public preview</strong> have "
            "<strong>no SLA</strong> and are not intended for production. Once a service reaches <strong>General Availability (GA)</strong>, it has a "
            "full SLA and support. Track changes through the Azure updates page.</p>"
            "<p><strong>Exam tip:</strong> Preview = no SLA, not for production; GA = full SLA. And remember composite SLAs go <em>down</em> "
            "when services depend on each other, because you multiply the percentages.</p>"
        ),
        "key_points": [
            "An SLA is Microsoft's financially backed uptime commitment, with service credits if missed.",
            "More redundancy raises effective availability.",
            "Composite SLA of chained dependent services is lower than any single one (multiply them).",
            "99.9% is ~43 min/month downtime; 99.99% is ~4 min/month.",
            "Preview features have no SLA and are not for production; GA has full SLA and support.",
        ],
    },
]

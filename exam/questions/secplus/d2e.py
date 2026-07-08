"""Security+ SY0-701 practice questions — Domain 2 (Threats, Vulnerabilities,
and Mitigations), batch E.

40 scenario-driven questions (36 multiple_choice + 4 multiple_response)
covering every study_topic label listed under domain 2 in
``_topic_labels.json``.
"""

from __future__ import annotations

QUESTIONS = [
    # ------------------------------------------------------------------ #
    # Threat actors (2.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2e-001",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Threat actors",
        "stem": (
            "A managed service provider (MSP) that supports 40 small business "
            "clients discovers that a single vulnerable remote monitoring and "
            "management (RMM) tool was used to simultaneously push ransomware to "
            "15 client networks overnight. Each affected client receives a separate "
            "ransom note demanding a cryptocurrency payment scaled to that "
            "company's size, and a dark-web leak site threatens to publish stolen "
            "files from any client that does not pay within 10 days. Which threat "
            "actor is MOST likely responsible?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Organized crime (ransomware-as-a-service affiliate)",
                "correct": True,
                "rationale": (
                    "Correct. Mass-scale extortion through a shared supply-chain "
                    "foothold, per-victim ransom demands scaled to ability to pay, "
                    "and a leak site to pressure payment are hallmarks of a "
                    "financially motivated, RaaS-affiliated organized crime "
                    "operation."
                ),
            },
            {
                "id": "b",
                "text": "Nation-state advanced persistent threat",
                "correct": False,
                "rationale": (
                    "Incorrect. Nation-state APTs generally avoid noisy, "
                    "simultaneous encryption events with public ransom demands; "
                    "their goal is sustained access and intelligence, not "
                    "monetized extortion of small businesses."
                ),
            },
            {
                "id": "c",
                "text": "Hacktivist collective",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no ideological message, cause, or public "
                    "statement attached to the incident — only a financial demand, "
                    "which is inconsistent with hacktivism's attention-seeking, "
                    "cause-driven motive."
                ),
            },
            {
                "id": "d",
                "text": "Insider threat",
                "correct": False,
                "rationale": (
                    "Incorrect. The attack originated through a shared third-party "
                    "RMM tool affecting many unrelated clients at once, not through "
                    "abuse of one organization's internal, trusted access."
                ),
            },
        ],
        "explanation": (
            "Simultaneous, scaled-to-size ransom demands across many victims plus "
            "a leak-site extortion threat point to a financially motivated "
            "organized crime group operating a ransomware-as-a-service affiliate "
            "model through a compromised supply-chain tool."
        ),
    },
    {
        "id": "nd2e-002",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Threat actors",
        "stem": (
            "A small municipal library's website is defaced using a well-known, "
            "unpatched content management system plugin exploit that has been "
            "publicly posted on GitHub for over a year. The attacker leaves a "
            "message bragging about the compromise and posts screenshots to a "
            "public hacking forum for recognition. No data was stolen, no ransom "
            "was demanded, and no political or social message was included. Which "
            "threat actor classification BEST fits this activity?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Unskilled attacker (script kiddie)",
                "correct": True,
                "rationale": (
                    "Correct. Reliance on a publicly available, pre-built exploit "
                    "against a low-value target, combined with bragging for social "
                    "clout rather than profit or ideology, is the defining "
                    "signature of an unskilled attacker."
                ),
            },
            {
                "id": "b",
                "text": "Hacktivist",
                "correct": False,
                "rationale": (
                    "Incorrect. Hacktivism requires an ideological or political "
                    "message driving the attack; this defacement carries only a "
                    "boast about the compromise itself, with no cause attached."
                ),
            },
            {
                "id": "c",
                "text": "Organized crime",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no financial motive, ransom demand, or "
                    "data monetization — organized crime groups act for profit, "
                    "not public bragging rights."
                ),
            },
            {
                "id": "d",
                "text": "Nation-state actor",
                "correct": False,
                "rationale": (
                    "Incorrect. Use of a year-old, publicly posted exploit against "
                    "a small municipal library, followed by public bragging, is "
                    "inconsistent with the stealth, custom tooling, and strategic "
                    "targeting typical of nation-state operations."
                ),
            },
        ],
        "explanation": (
            "Off-the-shelf, publicly known exploits used against a low-value "
            "target purely for bragging rights and social recognition, with no "
            "financial, political, or strategic motive, are the classic fingerprint "
            "of an unskilled attacker (script kiddie)."
        ),
    },
    # ------------------------------------------------------------------ #
    # Social engineering (2.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2e-003",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Social engineering",
        "stem": (
            "An HR coordinator receives a phone call from someone claiming to be "
            "the direct manager of a new remote hire who started the previous "
            "week. The caller accurately states the new hire's employee ID, exact "
            "start date, and job title — details scraped from a public "
            "\"welcome to the team\" post the new hire made on social media — and "
            "asks HR to rush a change to the new hire's direct-deposit bank "
            "account before the next pay run, citing a bank account error. Which "
            "technique is the caller using to establish credibility for the "
            "request, independent of the phone as a delivery channel?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Pretexting",
                "correct": True,
                "rationale": (
                    "Correct. The caller fabricates a believable persona (the "
                    "new hire's manager) and backs it with researched, accurate "
                    "details to construct a credible scenario that lowers HR's "
                    "guard — the defining trait of pretexting."
                ),
            },
            {
                "id": "b",
                "text": "Vishing",
                "correct": False,
                "rationale": (
                    "Incorrect. Vishing describes the voice-call delivery "
                    "channel itself; the question asks specifically what "
                    "technique makes the request credible, which is the "
                    "fabricated, researched persona (pretexting), not the fact "
                    "that it arrived by phone."
                ),
            },
            {
                "id": "c",
                "text": "Business email compromise",
                "correct": False,
                "rationale": (
                    "Incorrect. No email was used or spoofed at any point in "
                    "this interaction; the attack was conducted entirely by "
                    "phone."
                ),
            },
            {
                "id": "d",
                "text": "Whaling",
                "correct": False,
                "rationale": (
                    "Incorrect. Whaling targets a senior executive specifically; "
                    "here the target is an HR coordinator, and the impersonated "
                    "figure (a line manager) is not a C-suite executive."
                ),
            },
        ],
        "explanation": (
            "Building a fabricated but researched, plausible scenario and "
            "identity — a fake manager armed with accurate personal details — to "
            "manipulate a target into acting is pretexting; vishing only "
            "describes the phone as the delivery mechanism, not the technique."
        ),
    },
    {
        "id": "nd2e-004",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Social engineering",
        "stem": (
            "A network of dozens of coordinated, recently created social media "
            "accounts begins posting that a competitor's infant formula product "
            "is contaminated, timed precisely to coincide with that competitor's "
            "national product launch. The claims are false, and investigators "
            "trace several of the accounts to a marketing contractor working for "
            "a rival formula manufacturer. Which social engineering attack "
            "technique does this BEST describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Disinformation campaign",
                "correct": True,
                "rationale": (
                    "Correct. Deliberately fabricated, false claims spread "
                    "through coordinated accounts, timed for competitive "
                    "advantage and traced back to an interested party, is the "
                    "definition of disinformation — knowingly false information "
                    "spread with intent to deceive."
                ),
            },
            {
                "id": "b",
                "text": "Watering hole attack",
                "correct": False,
                "rationale": (
                    "Incorrect. A watering hole attack compromises a website "
                    "frequented by a target group to deliver malware; no site "
                    "compromise or malware delivery is described here, only "
                    "false claims spread via social media."
                ),
            },
            {
                "id": "c",
                "text": "Brand impersonation",
                "correct": False,
                "rationale": (
                    "Incorrect. Brand impersonation involves posing as a "
                    "trusted, recognizable brand to deceive victims; here the "
                    "attacker is attacking a rival's reputation, not "
                    "impersonating that rival's brand identity."
                ),
            },
            {
                "id": "d",
                "text": "Pretexting",
                "correct": False,
                "rationale": (
                    "Incorrect. Pretexting involves a fabricated persona used to "
                    "directly manipulate a specific target into an action; this "
                    "scenario is a broad public messaging campaign, not a "
                    "targeted, invented identity used against one victim."
                ),
            },
        ],
        "explanation": (
            "Deliberately false claims spread through coordinated accounts for "
            "competitive or reputational gain, and traced to an interested party, "
            "is disinformation — distinct from misinformation (unintentional), "
            "watering hole attacks (site compromise), and pretexting (a "
            "fabricated persona used on a specific target)."
        ),
    },
    {
        "id": "nd2e-005",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Social engineering",
        "stem": (
            "Several employees report seeing a pop-up ad on a normally reputable "
            "news website while browsing during lunch. Clicking \"Update Media "
            "Player Now\" silently began downloading a file in the background. "
            "Separately, the news site's own security team confirms the site was "
            "compromised for a three-week window, during which malicious code was "
            "inserted that served the fake update prompt only to visitors whose IP "
            "addresses matched the company's known corporate ranges, before being "
            "removed. Which TWO terms BEST describe this attack? (Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Watering hole attack",
                "correct": True,
                "rationale": (
                    "Correct. Compromising a legitimate site known to be visited "
                    "by the target organization, and serving malicious content "
                    "specifically to that organization's IP ranges, is the "
                    "defining pattern of a watering hole attack."
                ),
            },
            {
                "id": "b",
                "text": "Malvertising",
                "correct": True,
                "rationale": (
                    "Correct. The malicious payload was delivered through a "
                    "deceptive ad/pop-up prompt (a fake software-update banner) "
                    "injected into the compromised page, which is the mechanism "
                    "of malvertising."
                ),
            },
            {
                "id": "c",
                "text": "Typosquatting",
                "correct": False,
                "rationale": (
                    "Incorrect. Typosquatting relies on a lookalike misspelled "
                    "domain name; here employees visited the genuine, correctly "
                    "spelled news site, which had itself been compromised."
                ),
            },
            {
                "id": "d",
                "text": "Business email compromise",
                "correct": False,
                "rationale": (
                    "Incorrect. No email was involved at any stage; the entire "
                    "attack occurred through a compromised website visited "
                    "directly by employees."
                ),
            },
            {
                "id": "e",
                "text": "Brand impersonation",
                "correct": False,
                "rationale": (
                    "Incorrect. The attacker did not impersonate the news "
                    "outlet's brand elsewhere — the outlet's own real site was "
                    "compromised and used as-is to reach a targeted audience."
                ),
            },
        ],
        "explanation": (
            "Selectively serving malicious content only to a target "
            "organization's IP ranges via a compromised, legitimately visited "
            "site is a watering hole attack, and the fake update pop-up used to "
            "deliver the payload is malvertising — no lookalike domain, email, or "
            "brand impersonation is present."
        ),
    },
    # ------------------------------------------------------------------ #
    # Threat vectors and attack surfaces (2.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2e-006",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Threat vectors and attack surfaces",
        "stem": (
            "During due diligence for an acquisition, a security assessment of "
            "the target company's network finds a legacy warehouse inventory "
            "scanner appliance still configured with the administrator password "
            "printed directly in its factory installation manual, and the "
            "appliance is reachable from the general corporate VLAN with no "
            "additional access restriction. Which threat vector does this "
            "finding represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Default credentials",
                "correct": True,
                "rationale": (
                    "Correct. A factory-set, publicly documented password that "
                    "was never changed after deployment is the textbook "
                    "definition of a default-credentials threat vector."
                ),
            },
            {
                "id": "b",
                "text": "Open service port",
                "correct": False,
                "rationale": (
                    "Incorrect. The finding does not describe an unnecessary "
                    "network service or listening port being exposed — the "
                    "specific weakness identified is the unchanged, documented "
                    "administrator password itself."
                ),
            },
            {
                "id": "c",
                "text": "Unsupported system",
                "correct": False,
                "rationale": (
                    "Incorrect. Although the appliance is legacy, the assessment "
                    "did not cite lack of vendor support or missing patches as "
                    "the issue — it specifically flagged the unchanged factory "
                    "password."
                ),
            },
            {
                "id": "d",
                "text": "Removable device",
                "correct": False,
                "rationale": (
                    "Incorrect. No removable media, USB device, or portable "
                    "storage is described anywhere in this scenario."
                ),
            },
        ],
        "explanation": (
            "A never-changed, publicly documented factory password reachable "
            "from the general network is a classic default-credentials exposure, "
            "distinct from an open port, unsupported system, or removable-device "
            "vector."
        ),
    },
    {
        "id": "nd2e-007",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Threat vectors and attack surfaces",
        "stem": (
            "A contractor plugs a personal USB webcam into a conference room PC "
            "to join a video call. Three days later, endpoint protection flags "
            "the same PC's USB controller enumerating a human interface device "
            "(HID) that begins injecting rapid, scripted keystrokes to open a "
            "command prompt and download a payload, even though no new physical "
            "device was connected that day. Which threat vector introduced this "
            "exposure?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Removable device",
                "correct": True,
                "rationale": (
                    "Correct. A USB peripheral that secretly contains "
                    "keystroke-injection ('BadUSB'-style) firmware, later "
                    "triggering on its own to type malicious commands, is a "
                    "removable-device threat vector."
                ),
            },
            {
                "id": "b",
                "text": "Unsecure network",
                "correct": False,
                "rationale": (
                    "Incorrect. Nothing in the scenario involves network "
                    "traffic, Wi-Fi, or a shared network as the initial entry "
                    "point — the compromise came through a physically connected "
                    "USB peripheral."
                ),
            },
            {
                "id": "c",
                "text": "Supply chain",
                "correct": False,
                "rationale": (
                    "Incorrect. Supply chain vectors involve compromise "
                    "introduced through a trusted vendor's hardware, software, "
                    "or update process before it reaches the organization; here "
                    "an unvetted personal device was plugged in directly by a "
                    "visitor, which is a removable-device exposure, not a "
                    "vendor-trust failure."
                ),
            },
            {
                "id": "d",
                "text": "Vulnerable software",
                "correct": False,
                "rationale": (
                    "Incorrect. The compromise stems from a malicious physical "
                    "peripheral emulating a keyboard, not from an unpatched or "
                    "flawed software application."
                ),
            },
        ],
        "explanation": (
            "An unvetted personal USB peripheral that later emulates a keyboard "
            "to inject commands is a removable-device threat vector — distinct "
            "from network, supply chain, or software vulnerability vectors."
        ),
    },
    # ------------------------------------------------------------------ #
    # Application vulnerabilities (2.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2e-008",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Application vulnerabilities",
        "stem": (
            "A financial trading application exposes an inter-process "
            "communication (IPC) named pipe with no authentication. Researchers "
            "demonstrate that any local process — even one with no relationship "
            "to the trading application — can write arbitrary shellcode directly "
            "into the trading application's address space through this pipe and "
            "force it to execute, without exploiting any memory-safety bug "
            "inside the trading application's own code. Which vulnerability "
            "class does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Memory injection",
                "correct": True,
                "rationale": (
                    "Correct. Writing and executing arbitrary code inside a "
                    "running process's address space through an unauthenticated "
                    "interface — rather than through a coding flaw in the "
                    "target itself — is the definition of memory injection."
                ),
            },
            {
                "id": "b",
                "text": "Buffer overflow",
                "correct": False,
                "rationale": (
                    "Incorrect. A buffer overflow requires oversized input "
                    "overrunning a fixed-size memory structure inside the "
                    "vulnerable application's own code; the scenario explicitly "
                    "states no such coding flaw was exploited."
                ),
            },
            {
                "id": "c",
                "text": "Race condition (TOC/TOU)",
                "correct": False,
                "rationale": (
                    "Incorrect. No timing gap between a check and a subsequent "
                    "use of a resource is described — the pipe simply lacks "
                    "authentication entirely, at any point in time."
                ),
            },
            {
                "id": "d",
                "text": "Insecure deserialization",
                "correct": False,
                "rationale": (
                    "Incorrect. No serialized object or data structure is being "
                    "reconstructed from untrusted input; raw shellcode is being "
                    "written directly into process memory via an unauthenticated "
                    "IPC channel."
                ),
            },
        ],
        "explanation": (
            "Injecting and executing arbitrary code within another process's "
            "memory space via an unauthenticated interface, without exploiting "
            "a coding flaw in the target itself, is the hallmark of memory "
            "injection."
        ),
    },
    {
        "id": "nd2e-009",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Application vulnerabilities",
        "stem": (
            "A widely used PDF-editing application checks for new versions over "
            "plain HTTP and installs whatever the update server returns without "
            "verifying a digital signature. Researchers demonstrate that an "
            "on-path attacker can respond to the update check with a trojanized "
            "installer, which the application silently downloads and runs with "
            "the logged-in user's privileges, believing it to be an official "
            "update. Which application vulnerability does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Malicious update",
                "correct": True,
                "rationale": (
                    "Correct. An application's own unsigned, unauthenticated "
                    "update mechanism being hijacked to deliver and execute "
                    "attacker-controlled code is precisely the malicious-update "
                    "vulnerability class."
                ),
            },
            {
                "id": "b",
                "text": "Buffer overflow",
                "correct": False,
                "rationale": (
                    "Incorrect. No oversized input overwriting a fixed memory "
                    "structure is involved; the entire installer package is "
                    "swapped and run through a trusted, but unverified, update "
                    "channel."
                ),
            },
            {
                "id": "c",
                "text": "Insecure deserialization",
                "correct": False,
                "rationale": (
                    "Incorrect. The application is not reconstructing objects "
                    "from untrusted serialized data; it is executing a "
                    "full replacement installer received over an unverified "
                    "update channel."
                ),
            },
            {
                "id": "d",
                "text": "Race condition (TOC/TOU)",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no gap between checking and using a "
                    "resource being exploited here — the fundamental flaw is "
                    "the complete lack of signature verification on the update "
                    "itself, regardless of timing."
                ),
            },
        ],
        "explanation": (
            "An unsigned, plaintext update mechanism that can be hijacked by an "
            "on-path attacker to deliver and execute a trojanized installer is "
            "the malicious-update application vulnerability."
        ),
    },
    {
        "id": "nd2e-010",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Application vulnerabilities",
        "stem": (
            "A privileged backup script running as root first checks that a "
            "target log file is owned by the expected service account, then "
            "opens that same path for writing a moment later. A low-privileged "
            "user scripts a loop that replaces the file with a symbolic link to "
            "/etc/shadow in the brief interval between the ownership check and "
            "the write, causing the backup process to overwrite /etc/shadow's "
            "contents. Which vulnerability class was exploited?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Race condition (time-of-check to time-of-use)",
                "correct": True,
                "rationale": (
                    "Correct. Swapping the target file for a symlink during the "
                    "window between the privileged script's check and its "
                    "subsequent use of the file is a textbook TOC/TOU race "
                    "condition."
                ),
            },
            {
                "id": "b",
                "text": "Buffer overflow",
                "correct": False,
                "rationale": (
                    "Incorrect. No oversized input or memory-boundary violation "
                    "is involved; the attack exploits timing between a "
                    "permission check and a file operation, not memory "
                    "corruption."
                ),
            },
            {
                "id": "c",
                "text": "Malicious update",
                "correct": False,
                "rationale": (
                    "Incorrect. No software update or patch mechanism is "
                    "involved in this attack; it exploits a timing gap in a "
                    "backup script's file-handling logic."
                ),
            },
            {
                "id": "d",
                "text": "Memory injection",
                "correct": False,
                "rationale": (
                    "Incorrect. No code is written into or executed within "
                    "another process's memory space; the attack manipulates the "
                    "filesystem between a check and a subsequent privileged "
                    "operation."
                ),
            },
        ],
        "explanation": (
            "Exploiting the gap between when a privileged process checks a "
            "resource and when it actually uses it — by swapping in a symlink "
            "during that window — is the classic time-of-check to time-of-use "
            "(TOC/TOU) race condition."
        ),
    },
    # ------------------------------------------------------------------ #
    # Mobile vulnerabilities (2.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2e-011",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Mobile vulnerabilities",
        "stem": (
            "A corporate MDM report shows that a sales representative's Android "
            "phone has the \"install unknown apps\" permission enabled for a "
            "file-manager application. Using that permission, the user installed "
            "a game APK downloaded directly from a forum rather than the official "
            "app store; the game now requests accessibility-service permissions "
            "unusual for a simple game. Which mobile vulnerability does this "
            "represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Side loading",
                "correct": True,
                "rationale": (
                    "Correct. Installing an application from outside the "
                    "official, vetted app store by granting a permission that "
                    "bypasses the store's review process is the definition of "
                    "side loading."
                ),
            },
            {
                "id": "b",
                "text": "Jailbreaking",
                "correct": False,
                "rationale": (
                    "Incorrect. Jailbreaking involves removing the OS "
                    "manufacturer's sandboxing and code-signing restrictions at "
                    "the system level; this scenario describes installing an "
                    "app from an unofficial source, not defeating the device's "
                    "underlying security model."
                ),
            },
            {
                "id": "c",
                "text": "Zero-day exploitation",
                "correct": False,
                "rationale": (
                    "Incorrect. No unknown or unpatched vulnerability is being "
                    "exploited; the user simply installed an app through a "
                    "legitimate but unofficial installation path they enabled "
                    "themselves."
                ),
            },
            {
                "id": "d",
                "text": "Malicious update",
                "correct": False,
                "rationale": (
                    "Incorrect. This was an initial, deliberate installation of "
                    "a new application from a forum, not a compromised update "
                    "to an already-installed, trusted app."
                ),
            },
        ],
        "explanation": (
            "Installing applications from outside the official app store by "
            "enabling an \"unknown sources\" style permission is side loading, "
            "distinct from jailbreaking (which removes OS-level restrictions "
            "entirely)."
        ),
    },
    {
        "id": "nd2e-012",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile vulnerabilities",
        "stem": (
            "An MDM console flags that a corporate iPhone is failing its "
            "attestation check. Further inspection shows the device now has a "
            "third-party package manager installed and allows full browsing of "
            "the root filesystem — capabilities normally blocked entirely by "
            "iOS's sandboxing. Which mobile vulnerability does this indicate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Jailbreaking",
                "correct": True,
                "rationale": (
                    "Correct. Removing iOS's built-in sandboxing and "
                    "code-signing restrictions to gain root filesystem access "
                    "and install an unofficial package manager is precisely "
                    "what jailbreaking does on iOS devices."
                ),
            },
            {
                "id": "b",
                "text": "Rooting",
                "correct": False,
                "rationale": (
                    "Incorrect. Rooting is the equivalent term used for "
                    "obtaining privileged system access on Android devices; the "
                    "device described here is an iPhone, where the correct term "
                    "for this exact behavior is jailbreaking."
                ),
            },
            {
                "id": "c",
                "text": "Side loading",
                "correct": False,
                "rationale": (
                    "Incorrect. Side loading refers to installing an "
                    "application from outside the official app store while the "
                    "OS's normal security sandbox remains intact; here the "
                    "sandbox itself has been fully removed, granting root "
                    "filesystem access."
                ),
            },
            {
                "id": "d",
                "text": "Malicious update",
                "correct": False,
                "rationale": (
                    "Incorrect. No compromised software update is described; "
                    "the device's own OS-level restrictions were deliberately "
                    "circumvented, which is a jailbreak, not an update "
                    "hijacking."
                ),
            },
        ],
        "explanation": (
            "Circumventing iOS's sandbox to gain root filesystem access and "
            "install unofficial package managers is jailbreaking; the identical "
            "concept on Android devices is called rooting, making it a close but "
            "platform-incorrect distractor here."
        ),
    },
    # ------------------------------------------------------------------ #
    # Virtualization vulnerabilities (2.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2e-013",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Virtualization vulnerabilities",
        "stem": (
            "A cloud database-as-a-service provider discovers that a customer's "
            "isolated instance, running a vulnerable hypervisor driver, was used "
            "to directly read process memory belonging to a completely different "
            "customer's virtual machine hosted on the same physical server — "
            "without ever crossing a network boundary or authenticating to the "
            "other customer's system. Which virtualization vulnerability does "
            "this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "VM escape",
                "correct": True,
                "rationale": (
                    "Correct. Breaking out of a VM's isolation boundary through "
                    "a hypervisor flaw to access another tenant's VM directly, "
                    "without going over the network, is the definition of a "
                    "VM escape."
                ),
            },
            {
                "id": "b",
                "text": "Resource reuse",
                "correct": False,
                "rationale": (
                    "Incorrect. Resource reuse describes recovering leftover "
                    "data from storage or memory that was previously allocated "
                    "to another tenant and not properly cleared; this scenario "
                    "describes an active hypervisor exploit crossing the "
                    "isolation boundary in real time, not leftover residual "
                    "data."
                ),
            },
            {
                "id": "c",
                "text": "Malicious update",
                "correct": False,
                "rationale": (
                    "Incorrect. No software update mechanism is involved; the "
                    "compromise exploits a driver flaw in the hypervisor's "
                    "handling of guest isolation."
                ),
            },
            {
                "id": "d",
                "text": "Side loading",
                "correct": False,
                "rationale": (
                    "Incorrect. Side loading is a mobile-device vulnerability "
                    "related to installing apps from unofficial sources and "
                    "does not apply to server-based virtualization or "
                    "hypervisor isolation."
                ),
            },
        ],
        "explanation": (
            "Using a hypervisor-level flaw to break out of one VM's isolation "
            "boundary and directly access another tenant's VM memory is a VM "
            "escape, distinct from resource reuse, which involves leftover "
            "residual data rather than an active isolation breach."
        ),
    },
    {
        "id": "nd2e-014",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Virtualization vulnerabilities",
        "stem": (
            "A penetration tester provisions a brand-new virtual machine in a "
            "public cloud environment and, without ever writing anything to "
            "disk, recovers fragments of a previous tenant's database "
            "credentials still present in the freshly allocated but not yet "
            "zeroed system memory. Which virtualization vulnerability does this "
            "demonstrate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Resource reuse",
                "correct": True,
                "rationale": (
                    "Correct. Recovering a previous tenant's data from memory "
                    "or storage that was reallocated to a new tenant without "
                    "being properly cleared is precisely the resource-reuse "
                    "vulnerability."
                ),
            },
            {
                "id": "b",
                "text": "VM escape",
                "correct": False,
                "rationale": (
                    "Incorrect. No hypervisor isolation boundary was actively "
                    "crossed to reach another running VM; the data was simply "
                    "found sitting in memory allocated to the new tenant's own "
                    "instance."
                ),
            },
            {
                "id": "c",
                "text": "Data remanence on decommissioned physical media",
                "correct": False,
                "rationale": (
                    "Incorrect. This is a closely related concept, but the "
                    "specific term for leftover data surfacing across "
                    "different cloud tenants sharing reallocated virtual "
                    "resources — rather than recovering data from a disposed "
                    "physical disk — is resource reuse."
                ),
            },
            {
                "id": "d",
                "text": "Jailbreaking",
                "correct": False,
                "rationale": (
                    "Incorrect. Jailbreaking applies to mobile device OS "
                    "sandbox restrictions, not to cloud virtual machine memory "
                    "allocation."
                ),
            },
        ],
        "explanation": (
            "Recovering a prior tenant's data from newly allocated, "
            "not-yet-cleared memory or storage in a multi-tenant cloud "
            "environment is resource reuse — a related but distinct concept "
            "from decommissioned physical media remanence and from an active "
            "VM escape."
        ),
    },
    # ------------------------------------------------------------------ #
    # Vulnerability scan and assessment result classification (2.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2e-015",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Vulnerability scan and assessment result classification",
        "stem": (
            "A vulnerability scanner flags an internal custom API server as "
            "vulnerable to a well-known Apache Struts remote code execution CVE, "
            "based solely on the server's HTTP response banner. The security "
            "team confirms the server does not run Apache Struts anywhere in "
            "its stack; a previous administrator had manually edited the banner "
            "to read \"Apache Struts 2.3\" as an internal joke. How should this "
            "scan result be classified?"
        ),
        "options": [
            {
                "id": "a",
                "text": "False positive",
                "correct": True,
                "rationale": (
                    "Correct. The scanner reported a vulnerability that does "
                    "not actually exist, based on a misleading banner string — "
                    "the definition of a false positive."
                ),
            },
            {
                "id": "b",
                "text": "True positive",
                "correct": False,
                "rationale": (
                    "Incorrect. A true positive requires the reported "
                    "vulnerability to actually be present; the team confirmed "
                    "Apache Struts is not even installed on the server."
                ),
            },
            {
                "id": "c",
                "text": "False negative",
                "correct": False,
                "rationale": (
                    "Incorrect. A false negative describes a real vulnerability "
                    "that the scanner failed to detect and did not report; here "
                    "the scanner did generate a finding, which turned out to be "
                    "incorrect."
                ),
            },
            {
                "id": "d",
                "text": "True negative",
                "correct": False,
                "rationale": (
                    "Incorrect. A true negative means the scanner correctly "
                    "reported no vulnerability where none existed; here the "
                    "scanner actively reported a finding, which was then "
                    "disproven."
                ),
            },
        ],
        "explanation": (
            "A finding that the scanner reported but that further investigation "
            "disproves — here because a customized banner string, not an actual "
            "Struts installation, triggered the signature — is a false "
            "positive."
        ),
    },
    {
        "id": "nd2e-016",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Vulnerability scan and assessment result classification",
        "stem": (
            "A quarterly vulnerability scan of a legacy SCADA subnet reports zero "
            "findings. Six months later, that subnet is compromised through an "
            "unpatched vulnerability that had already been publicly documented "
            "for two years and was present on the affected system during the "
            "earlier scan window. Investigation shows the scanning platform was "
            "never granted credentials or routed network access to that VLAN. "
            "How should the earlier \"zero findings\" scan result be "
            "classified?"
        ),
        "options": [
            {
                "id": "a",
                "text": "False negative",
                "correct": True,
                "rationale": (
                    "Correct. A real, exploitable vulnerability existed on the "
                    "subnet during the scan window, but the scanner failed to "
                    "detect and report it because it never had visibility into "
                    "that VLAN — the definition of a false negative."
                ),
            },
            {
                "id": "b",
                "text": "True negative",
                "correct": False,
                "rationale": (
                    "Incorrect. A true negative would mean the vulnerability "
                    "genuinely did not exist at the time of the scan; here the "
                    "vulnerability had already been present and publicly known "
                    "for two years."
                ),
            },
            {
                "id": "c",
                "text": "False positive",
                "correct": False,
                "rationale": (
                    "Incorrect. A false positive requires the scanner to have "
                    "reported a finding that turned out to be inaccurate; this "
                    "scan reported nothing at all for that subnet."
                ),
            },
            {
                "id": "d",
                "text": "True positive",
                "correct": False,
                "rationale": (
                    "Incorrect. A true positive requires the scanner to have "
                    "correctly reported an existing vulnerability; the scan "
                    "produced zero findings due to lack of access to the "
                    "subnet."
                ),
            },
        ],
        "explanation": (
            "A vulnerability that genuinely existed but went unreported because "
            "the scanner lacked access or visibility to the affected asset is a "
            "false negative — a coverage gap rather than a truly clean result."
        ),
    },
    # ------------------------------------------------------------------ #
    # Web application vulnerabilities (2.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2e-017",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Web application vulnerabilities",
        "stem": (
            "A hospital's patient portal displays lab results using a URL "
            "pattern of https://portal.example.com/records?patientId=1042. A "
            "logged-in patient manually changes the value to 1043 in the address "
            "bar and, without any additional authentication prompt or access "
            "check, successfully views another patient's private lab results "
            "using their own valid session. Which vulnerability does this "
            "represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Insecure direct object reference (broken access control)",
                "correct": True,
                "rationale": (
                    "Correct. The application fails to verify that the "
                    "authenticated user is actually authorized to view the "
                    "specific record referenced by the ID parameter, allowing "
                    "simple ID substitution to expose another user's data."
                ),
            },
            {
                "id": "b",
                "text": "Cross-site request forgery",
                "correct": False,
                "rationale": (
                    "Incorrect. CSRF involves tricking a victim's browser into "
                    "submitting an unwanted request from another site; here the "
                    "patient deliberately and directly edits the URL in their "
                    "own browser session — no forged cross-site request is "
                    "involved."
                ),
            },
            {
                "id": "c",
                "text": "SQL injection",
                "correct": False,
                "rationale": (
                    "Incorrect. No malformed query syntax or database "
                    "manipulation is described; the patient ID parameter is "
                    "simply a valid integer that the application fails to "
                    "authorize against the logged-in user."
                ),
            },
            {
                "id": "d",
                "text": "Session hijacking",
                "correct": False,
                "rationale": (
                    "Incorrect. The patient is using their own legitimate, "
                    "unmodified session the entire time; no other user's "
                    "session token was stolen or reused."
                ),
            },
        ],
        "explanation": (
            "Substituting a reference value in a URL to access another user's "
            "data, with the application never verifying object-level "
            "authorization, is an insecure direct object reference / broken "
            "access control flaw."
        ),
    },
    {
        "id": "nd2e-018",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Web application vulnerabilities",
        "stem": (
            "While logged into their online banking session in one browser tab, "
            "a user visits an unrelated forum in another tab. The forum page "
            "contains a hidden, auto-submitting HTML form that silently POSTs a "
            "funds-transfer request to the bank's website, using the browser's "
            "still-valid banking session cookie, without any script executing on "
            "the bank's own site and without the user knowingly interacting with "
            "the form. Which vulnerability does this exploit?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Cross-site request forgery (CSRF)",
                "correct": True,
                "rationale": (
                    "Correct. Forcing a victim's browser to submit an "
                    "unintended, state-changing request to a site where they "
                    "are already authenticated, by riding on their valid "
                    "session cookie from an unrelated page, is the definition "
                    "of CSRF."
                ),
            },
            {
                "id": "b",
                "text": "Cross-site scripting (XSS)",
                "correct": False,
                "rationale": (
                    "Incorrect. XSS requires attacker-controlled script to "
                    "execute in the context of the vulnerable (bank) site; here "
                    "no script runs on the bank's site at all — only a form "
                    "submission is forged from a completely separate page."
                ),
            },
            {
                "id": "c",
                "text": "Server-side request forgery (SSRF)",
                "correct": False,
                "rationale": (
                    "Incorrect. SSRF tricks a server into making an unintended "
                    "request on the attacker's behalf; here it is the victim's "
                    "own browser, not a server, that is tricked into sending "
                    "the request."
                ),
            },
            {
                "id": "d",
                "text": "Clickjacking",
                "correct": False,
                "rationale": (
                    "Incorrect. Clickjacking relies on deceptive UI overlays "
                    "that trick a user into clicking something they did not "
                    "intend to click; this attack requires no user click at "
                    "all — the malicious form submits itself automatically."
                ),
            },
        ],
        "explanation": (
            "A forged, automatically submitted request that abuses a victim's "
            "existing authenticated session on another site — with no script "
            "execution on the target site and no user interaction required — is "
            "cross-site request forgery."
        ),
    },
    {
        "id": "nd2e-019",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Web application vulnerabilities",
        "stem": (
            "A penetration test report on an online shopping site's login form "
            "lists two separate findings:\n\n"
            "Finding 1 — Submitting a username of admin' -- with a blank "
            "password field grants the tester full administrative access.\n\n"
            "Finding 2 — The login form returns the distinct message "
            "\"Invalid username\" when a nonexistent account is entered, but "
            "\"Invalid password\" when a real account name is entered with the "
            "wrong password, allowing valid account names to be enumerated.\n\n"
            "Which TWO vulnerabilities are demonstrated by Finding 1 and "
            "Finding 2, respectively? (Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "SQL injection",
                "correct": True,
                "rationale": (
                    "Correct. Injecting SQL comment syntax (admin' --) into the "
                    "username field to bypass password validation entirely "
                    "demonstrates a classic authentication-bypass SQL injection "
                    "flaw (Finding 1)."
                ),
            },
            {
                "id": "b",
                "text": "Username enumeration via verbose error handling",
                "correct": True,
                "rationale": (
                    "Correct. Returning distinct error messages that reveal "
                    "whether a submitted username exists allows an attacker to "
                    "build a list of valid accounts to target (Finding 2)."
                ),
            },
            {
                "id": "c",
                "text": "Cross-site scripting",
                "correct": False,
                "rationale": (
                    "Incorrect. Neither finding involves injecting or executing "
                    "a script in a victim's browser; both findings involve "
                    "backend query manipulation and error-message disclosure."
                ),
            },
            {
                "id": "d",
                "text": "Session fixation",
                "correct": False,
                "rationale": (
                    "Incorrect. Neither finding describes an attacker forcing "
                    "or predicting a victim's session identifier before "
                    "authentication."
                ),
            },
            {
                "id": "e",
                "text": "Insecure deserialization",
                "correct": False,
                "rationale": (
                    "Incorrect. Neither finding involves reconstructing "
                    "application objects from untrusted serialized data; both "
                    "relate to the login form's query handling and error "
                    "messaging."
                ),
            },
        ],
        "explanation": (
            "Bypassing authentication with injected SQL comment syntax is SQL "
            "injection, while distinct error messages that reveal valid account "
            "names constitute username enumeration through verbose error "
            "handling — two separate, commonly paired login-form weaknesses."
        ),
    },
    # ------------------------------------------------------------------ #
    # Authentication factors and protocols (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2e-020",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Authentication factors and protocols",
        "stem": (
            "A packet capture from an internal network segment shows an "
            "application performing LDAP simple bind authentication to the "
            "corporate directory in cleartext over port 389, without StartTLS or "
            "LDAPS, exposing the service account's full password to anyone "
            "monitoring that segment. Which weakness BEST explains this "
            "exposure?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Use of an unencrypted authentication protocol",
                "correct": True,
                "rationale": (
                    "Correct. Performing an LDAP simple bind over plaintext "
                    "port 389 without StartTLS or LDAPS transmits credentials "
                    "unencrypted, exposing them to anyone able to observe the "
                    "segment."
                ),
            },
            {
                "id": "b",
                "text": "Insufficient password complexity",
                "correct": False,
                "rationale": (
                    "Incorrect. No evidence about the password's length or "
                    "complexity is given; the issue is that the password was "
                    "transmitted in cleartext, regardless of how complex it "
                    "was."
                ),
            },
            {
                "id": "c",
                "text": "Missing multifactor authentication",
                "correct": False,
                "rationale": (
                    "Incorrect. The exposure described is the interception of "
                    "the credential in transit, which would occur even if a "
                    "second factor were required afterward; the core flaw is "
                    "the unencrypted transport of the bind credential."
                ),
            },
            {
                "id": "d",
                "text": "Account lockout not configured",
                "correct": False,
                "rationale": (
                    "Incorrect. Nothing in the scenario involves repeated "
                    "failed login attempts or brute forcing; a single "
                    "cleartext credential was passively captured on the wire."
                ),
            },
        ],
        "explanation": (
            "Transmitting LDAP simple-bind credentials over an unencrypted "
            "channel exposes the password in plaintext to anyone monitoring the "
            "segment, regardless of password strength, MFA, or lockout policy."
        ),
    },
    {
        "id": "nd2e-021",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Authentication factors and protocols",
        "stem": (
            "A user's hardware TOTP token and password are both used correctly "
            "to log in from an unfamiliar foreign IP address. Investigation "
            "reveals that an attacker briefly had physical access to a spare, "
            "unassigned TOTP token stored in an unlocked drawer and "
            "photographed its QR-code provisioning secret before it was issued "
            "to the user, later using that secret to generate valid codes "
            "independently. Which factor explains why multifactor "
            "authentication failed to prevent this compromise?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The TOTP shared secret (seed) was physically exposed, "
                    "letting the attacker independently generate valid codes"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Because the underlying seed was photographed "
                    "before issuance, the attacker can compute the same "
                    "time-based codes as the legitimate token holder, "
                    "effectively cloning the \"something you have\" factor "
                    "without ever possessing the physical token during login."
                ),
            },
            {
                "id": "b",
                "text": "The attacker performed a SIM-swap attack",
                "correct": False,
                "rationale": (
                    "Incorrect. No cellular carrier, phone number, or SMS-based "
                    "one-time code is involved anywhere in this scenario; the "
                    "second factor is a hardware TOTP token whose seed was "
                    "physically copied."
                ),
            },
            {
                "id": "c",
                "text": "The attacker used a Kerberos golden ticket",
                "correct": False,
                "rationale": (
                    "Incorrect. No Kerberos ticket-granting ticket forgery or "
                    "domain-controller key theft is described; this compromise "
                    "involves cloning a TOTP token's provisioning secret."
                ),
            },
            {
                "id": "d",
                "text": "The organization only required single-factor authentication",
                "correct": False,
                "rationale": (
                    "Incorrect. MFA was in fact required and both factors were "
                    "presented correctly; the flaw is that the second factor "
                    "itself was compromised at provisioning time, not that MFA "
                    "was absent."
                ),
            },
        ],
        "explanation": (
            "Photographing a TOTP token's QR provisioning secret allows an "
            "attacker to independently generate valid codes, defeating the "
            "\"something you have\" factor even though MFA was properly "
            "enforced and both credentials were entered correctly."
        ),
    },
    # ------------------------------------------------------------------ #
    # Cryptographic attacks (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2e-022",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Cryptographic attacks",
        "stem": (
            "A software vendor's file-integrity process publishes an MD5 "
            "checksum alongside each installer download. A researcher "
            "deliberately crafts two different installer files — one benign and "
            "one containing a hidden backdoor — engineered so that both produce "
            "the exact same MD5 hash. After the vendor publishes the checksum "
            "for the benign file, the researcher swaps in the backdoored file, "
            "which still matches the published hash. Which cryptographic attack "
            "does this demonstrate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Collision attack",
                "correct": True,
                "rationale": (
                    "Correct. Deliberately engineering two different inputs "
                    "that produce an identical hash output, then substituting "
                    "one for the other, is a collision attack against the weak "
                    "hash function."
                ),
            },
            {
                "id": "b",
                "text": "Birthday attack",
                "correct": False,
                "rationale": (
                    "Incorrect. A birthday attack is the general probabilistic "
                    "method for finding any two inputs that collide faster than "
                    "brute force; here the researcher deliberately engineered "
                    "two specific, pre-chosen files to collide, which is "
                    "described as a collision attack in this context."
                ),
            },
            {
                "id": "c",
                "text": "Downgrade attack",
                "correct": False,
                "rationale": (
                    "Incorrect. No protocol version negotiation or forced "
                    "fallback to a weaker algorithm during a handshake is "
                    "involved; the weakness exploited is MD5's susceptibility "
                    "to engineered hash collisions."
                ),
            },
            {
                "id": "d",
                "text": "Pass-the-hash attack",
                "correct": False,
                "rationale": (
                    "Incorrect. No authentication hash is being captured and "
                    "replayed to log into a system; this attack targets file "
                    "integrity verification, not credential authentication."
                ),
            },
        ],
        "explanation": (
            "Engineering two different files to share the same MD5 hash so one "
            "can be substituted for the other while still matching a published "
            "checksum is a collision attack on the weak hash algorithm."
        ),
    },
    {
        "id": "nd2e-023",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Cryptographic attacks",
        "stem": (
            "An attacker positioned on the network forces a legacy VPN client "
            "to abandon its IKEv2/AES-256 negotiation and fall back to an older "
            "PPTP configuration still enabled \"for compatibility,\" then "
            "captures and breaks the weak MS-CHAPv2 authentication exchange "
            "used by PPTP to recover the user's credentials. Which "
            "cryptographic attack does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Downgrade attack",
                "correct": True,
                "rationale": (
                    "Correct. Forcing a connection to abandon a strong protocol "
                    "and negotiate down to a weaker, legacy one (PPTP/MS-CHAPv2) "
                    "that can then be broken is the definition of a downgrade "
                    "attack."
                ),
            },
            {
                "id": "b",
                "text": "Collision attack",
                "correct": False,
                "rationale": (
                    "Incorrect. No two inputs are being engineered to produce "
                    "matching hash values; the attack instead forces "
                    "negotiation down to a weaker protocol version."
                ),
            },
            {
                "id": "c",
                "text": "Birthday attack",
                "correct": False,
                "rationale": (
                    "Incorrect. No probabilistic search for hash collisions is "
                    "described; the weakness exploited is protocol fallback to "
                    "PPTP, not a hash collision."
                ),
            },
            {
                "id": "d",
                "text": "Replay attack",
                "correct": False,
                "rationale": (
                    "Incorrect. The attacker does not capture and later resend "
                    "a prior legitimate session; they actively force a new "
                    "negotiation to use a weaker protocol in real time."
                ),
            },
        ],
        "explanation": (
            "Forcing a client to abandon a strong protocol in favor of a "
            "weaker, legacy one that can then be broken is a downgrade attack, "
            "distinct from collision, birthday, and replay attacks."
        ),
    },
    # ------------------------------------------------------------------ #
    # Indicators of malicious activity (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2e-024",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Indicators of malicious activity",
        "stem": (
            "Authentication logs show a user's account successfully logging in "
            "from New York at 9:00 a.m. and then successfully logging in from "
            "Tokyo at 9:20 a.m. — two sequential, non-overlapping logins that "
            "are physically impossible given commercial flight times. The user "
            "confirms they never left New York and did not use a VPN. Which "
            "indicator BEST describes this finding?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Impossible travel",
                "correct": True,
                "rationale": (
                    "Correct. Two sequential logins from geographically "
                    "distant locations within a time window too short for "
                    "actual physical travel is the definition of impossible "
                    "travel."
                ),
            },
            {
                "id": "b",
                "text": "Concurrent session usage",
                "correct": False,
                "rationale": (
                    "Incorrect. Concurrent session usage describes overlapping, "
                    "simultaneously active sessions from different locations; "
                    "these two logins were sequential and 20 minutes apart, "
                    "not simultaneous."
                ),
            },
            {
                "id": "c",
                "text": "Resource consumption",
                "correct": False,
                "rationale": (
                    "Incorrect. No abnormal CPU, bandwidth, or resource usage "
                    "is described; the indicator here is purely geographic and "
                    "time-based."
                ),
            },
            {
                "id": "d",
                "text": "Blocked content",
                "correct": False,
                "rationale": (
                    "Incorrect. No content filtering, DLP block, or denied "
                    "access event is described; both logins succeeded."
                ),
            },
        ],
        "explanation": (
            "Sequential successful logins from locations too far apart to "
            "travel between in the elapsed time is impossible travel, distinct "
            "from concurrent session usage, which requires overlapping "
            "simultaneous sessions."
        ),
    },
    {
        "id": "nd2e-025",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Indicators of malicious activity",
        "stem": (
            "A vulnerability management dashboard shows that a group of 12 "
            "servers received and applied a critical security patch at "
            "3:14 a.m. on a Tuesday — well outside the organization's "
            "documented maintenance windows, which occur only on weekend "
            "nights — and no corresponding change ticket exists for the "
            "activity. Which indicator BEST describes this finding?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Out-of-cadence patching",
                "correct": True,
                "rationale": (
                    "Correct. Patching activity occurring outside the "
                    "organization's documented, expected schedule and without "
                    "an associated change record is the definition of "
                    "out-of-cadence patching, which may indicate unauthorized "
                    "change or an attacker closing the vulnerability they used."
                ),
            },
            {
                "id": "b",
                "text": "Missing logs",
                "correct": False,
                "rationale": (
                    "Incorrect. The patch activity is fully logged and visible "
                    "in the dashboard; nothing indicates a gap or absence of "
                    "log data."
                ),
            },
            {
                "id": "c",
                "text": "Resource inaccessibility",
                "correct": False,
                "rationale": (
                    "Incorrect. No system became unreachable or unavailable in "
                    "this scenario; the concern is the unexpected timing of a "
                    "successful patch application."
                ),
            },
            {
                "id": "d",
                "text": "Account lockout",
                "correct": False,
                "rationale": (
                    "Incorrect. No failed login attempts or account lockouts "
                    "are described anywhere in this finding."
                ),
            },
        ],
        "explanation": (
            "Patching that occurs outside the documented maintenance schedule "
            "with no change record is out-of-cadence patching, a red flag "
            "warranting investigation into who or what applied the change."
        ),
    },
    {
        "id": "nd2e-026",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Indicators of malicious activity",
        "stem": (
            "During a single incident window, a SOC dashboard shows two "
            "correlated findings:\n\n"
            "(1) The Windows Security event log on one domain controller is "
            "completely missing all entries between 01:15 and 02:45, while "
            "every other domain controller shows normal, continuous logging "
            "for that same period.\n\n"
            "(2) An internal file server suddenly becomes unreachable from the "
            "rest of the network and stops responding to ICMP pings, even "
            "though the hypervisor console still shows the VM as powered on "
            "and healthy.\n\n"
            "Which TWO indicators are demonstrated by these findings, "
            "respectively? (Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Missing logs",
                "correct": True,
                "rationale": (
                    "Correct. A gap in the security event log on one domain "
                    "controller, while peer domain controllers log normally "
                    "for the same period, is the definition of missing logs — "
                    "often indicating tampering to hide activity."
                ),
            },
            {
                "id": "b",
                "text": "Resource inaccessibility",
                "correct": True,
                "rationale": (
                    "Correct. A system that is powered on and shows as "
                    "healthy at the hypervisor level but is unreachable over "
                    "the network is the definition of resource inaccessibility."
                ),
            },
            {
                "id": "c",
                "text": "Impossible travel",
                "correct": False,
                "rationale": (
                    "Incorrect. No login geography or account authentication "
                    "location data is involved in either finding."
                ),
            },
            {
                "id": "d",
                "text": "Concurrent session usage",
                "correct": False,
                "rationale": (
                    "Incorrect. Neither finding describes simultaneous, "
                    "overlapping account sessions from different sources."
                ),
            },
            {
                "id": "e",
                "text": "Out-of-cadence patching",
                "correct": False,
                "rationale": (
                    "Incorrect. Neither finding describes a patch or update "
                    "being applied; one is a log gap, the other is a "
                    "connectivity failure."
                ),
            },
        ],
        "explanation": (
            "A gap in one system's security logs while peers log normally is "
            "missing logs, and a powered-on but network-unreachable host is "
            "resource inaccessibility — two distinct indicators drawn directly "
            "from the two described facts."
        ),
    },
    # ------------------------------------------------------------------ #
    # Log sources and investigative questions (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2e-027",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log sources and investigative questions",
        "stem": (
            "Investigators cannot recover the body content of deleted messages "
            "from a compromised mailbox, but they can still determine that the "
            "account sent 47 messages with large attachments to an unfamiliar "
            "external address over a two-hour window, based solely on preserved "
            "sender, recipient, timestamp, and attachment-size information — "
            "even though the message content itself is gone. Which data source "
            "provided this insight?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Metadata",
                "correct": True,
                "rationale": (
                    "Correct. Envelope-level information such as sender, "
                    "recipient, timestamps, and attachment size that persists "
                    "independently of message content is metadata, and it "
                    "remains available even after the body content is deleted."
                ),
            },
            {
                "id": "b",
                "text": "Firewall log",
                "correct": False,
                "rationale": (
                    "Incorrect. A firewall log would show network-level "
                    "connection details such as source/destination IP and "
                    "port, not per-message sender, recipient, and attachment "
                    "size information."
                ),
            },
            {
                "id": "c",
                "text": "Endpoint log",
                "correct": False,
                "rationale": (
                    "Incorrect. Endpoint logs record activity occurring on a "
                    "specific device (process execution, file access); the "
                    "information described here is preserved at the message "
                    "level within the mail system, not on an endpoint."
                ),
            },
            {
                "id": "d",
                "text": "Intrusion detection system (IDS) log",
                "correct": False,
                "rationale": (
                    "Incorrect. An IDS log would record alerts on suspicious "
                    "traffic patterns, not detailed per-message envelope "
                    "attributes like recipient and attachment size."
                ),
            },
        ],
        "explanation": (
            "Envelope-level details — sender, recipient, timestamps, and "
            "attachment size — that survive even after message content is "
            "deleted are metadata, distinct from firewall, endpoint, or IDS "
            "logs."
        ),
    },
    {
        "id": "nd2e-028",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log sources and investigative questions",
        "stem": (
            "An analyst must determine precisely which internal host initiated "
            "a suspicious outbound connection to a known command-and-control IP "
            "address. Because the network uses NAT, the perimeter firewall's "
            "traffic log only shows the connection using the single translated "
            "public IP address and port, with no internal host identity "
            "recorded in that entry. Which log source should the analyst "
            "correlate next to map the translated address back to the "
            "originating internal host?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Firewall NAT/session translation log",
                "correct": True,
                "rationale": (
                    "Correct. The firewall's NAT or session translation table "
                    "records the mapping between each internal source IP:port "
                    "and the translated public IP:port used for outbound "
                    "connections, allowing the analyst to trace the connection "
                    "back to the originating host."
                ),
            },
            {
                "id": "b",
                "text": "DNS query log",
                "correct": False,
                "rationale": (
                    "Incorrect. DNS logs would show which internal host "
                    "resolved a domain name to an IP address, but they do not "
                    "record the NAT translation mapping needed to identify "
                    "which host owns a specific translated connection entry."
                ),
            },
            {
                "id": "c",
                "text": "Application log",
                "correct": False,
                "rationale": (
                    "Incorrect. Application logs record activity within a "
                    "specific software application, not network-layer address "
                    "translation performed by the perimeter firewall."
                ),
            },
            {
                "id": "d",
                "text": "Intrusion prevention system (IPS) alert log",
                "correct": False,
                "rationale": (
                    "Incorrect. An IPS alert log may confirm that suspicious "
                    "traffic was flagged, but it does not necessarily contain "
                    "the internal-to-external NAT mapping needed to identify "
                    "the originating host."
                ),
            },
        ],
        "explanation": (
            "When a firewall's traffic log only shows a translated public "
            "IP:port, the NAT/session translation log is the specific source "
            "that maps that translation back to the originating internal host."
        ),
    },
    # ------------------------------------------------------------------ #
    # Malware types (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2e-029",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Malware types",
        "stem": (
            "A user's antivirus is silently disabled with no alert generated. "
            "Investigators find a hidden process that captures every keystroke "
            "typed on the system and exfiltrates it nightly via encoded DNS TXT "
            "record queries. No screen captures, webcam activity, or browsing "
            "history collection is found — only keystroke logs that correlate "
            "exactly with the timing of the user's banking site logins. Which "
            "malware type BEST matches this behavior?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Keylogger",
                "correct": True,
                "rationale": (
                    "Correct. Malware whose sole observed function is "
                    "capturing keystrokes — timed specifically to credential "
                    "entry on a banking site, with no screen capture or "
                    "browsing-habit collection — is precisely a keylogger."
                ),
            },
            {
                "id": "b",
                "text": "Spyware",
                "correct": False,
                "rationale": (
                    "Incorrect. Spyware is the broader category that can "
                    "include browsing-habit tracking, screen capture, and "
                    "other surveillance beyond keystrokes; the scenario "
                    "describes a narrower, keystroke-only capability that is "
                    "more precisely classified as a keylogger."
                ),
            },
            {
                "id": "c",
                "text": "Rootkit",
                "correct": False,
                "rationale": (
                    "Incorrect. Nothing indicates the malware is subverting "
                    "OS-level tools to hide files or processes from standard "
                    "utilities; the described, tested behavior is keystroke "
                    "capture, not concealment mechanics."
                ),
            },
            {
                "id": "d",
                "text": "Trojan",
                "correct": False,
                "rationale": (
                    "Incorrect. Trojan describes a delivery/disguise method "
                    "(malware posing as legitimate software), not the "
                    "malware's functional behavior once running; the question "
                    "asks about the observed capability, which is keystroke "
                    "capture."
                ),
            },
        ],
        "explanation": (
            "Malware whose specific, observed capability is capturing "
            "keystrokes tied to credential entry — without broader "
            "surveillance features — is best classified as a keylogger, a more "
            "specific term than the broader spyware category."
        ),
    },
    {
        "id": "nd2e-030",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Malware types",
        "stem": (
            "A forensic disk image shows that the operating system's own "
            "process-listing and file-browsing utilities never display a "
            "particular process or its containing directory. Raw performance "
            "counters, however, clearly show that process actively consuming "
            "CPU cycles, and the directory's contents become fully visible when "
            "the disk is mounted offline on a separate, clean machine. Which "
            "malware type BEST explains why the OS's own tools fail to reveal "
            "the artifact while offline analysis does not?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Rootkit",
                "correct": True,
                "rationale": (
                    "Correct. Malware that subverts the operating system's own "
                    "APIs so that standard tools running on the live system "
                    "cannot see it, while the artifact remains fully visible "
                    "under offline or out-of-band analysis, is the defining "
                    "trait of a rootkit."
                ),
            },
            {
                "id": "b",
                "text": "Logic bomb",
                "correct": False,
                "rationale": (
                    "Incorrect. A logic bomb is malware that lies dormant until "
                    "a specific condition or trigger is met; no such "
                    "condition-based payload activation is described here — "
                    "the defining behavior is active concealment from OS "
                    "tools."
                ),
            },
            {
                "id": "c",
                "text": "Bloatware",
                "correct": False,
                "rationale": (
                    "Incorrect. Bloatware refers to unwanted but generally "
                    "non-concealed, often preinstalled software that consumes "
                    "resources; it does not actively hide itself from the "
                    "operating system's own management tools."
                ),
            },
            {
                "id": "d",
                "text": "Trojan",
                "correct": False,
                "rationale": (
                    "Incorrect. Trojan describes a disguise-based delivery "
                    "method, not the specific OS-level concealment capability "
                    "being tested here, which is the hallmark of a rootkit."
                ),
            },
        ],
        "explanation": (
            "Subverting the operating system's own tools so a malicious "
            "process and its files are invisible to live analysis, yet fully "
            "visible offline, is the defining signature of a rootkit."
        ),
    },
    {
        "id": "nd2e-031",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Malware types",
        "stem": (
            "A newly imaged fleet of laptops arrives from the OEM with a dozen "
            "preinstalled trial applications and vendor utilities that users "
            "cannot easily uninstall. Months later, one of these unused, "
            "unremovable utilities is found to contain a critical, unpatched "
            "vulnerability that becomes the entry point for a compromise, even "
            "though no employee ever opened or used that utility. Which term "
            "BEST classifies the original preinstalled-software problem, "
            "separate from the later exploit that used it as an entry point?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Bloatware",
                "correct": True,
                "rationale": (
                    "Correct. Unwanted, often unremovable software preinstalled "
                    "by a vendor that consumes resources and needlessly "
                    "expands the attack surface — without necessarily being "
                    "malicious on its own — is bloatware."
                ),
            },
            {
                "id": "b",
                "text": "Trojan",
                "correct": False,
                "rationale": (
                    "Incorrect. The utilities were openly, visibly preinstalled "
                    "under their real vendor branding rather than disguised as "
                    "something else, which is what distinguishes bloatware "
                    "from a trojan."
                ),
            },
            {
                "id": "c",
                "text": "Logic bomb",
                "correct": False,
                "rationale": (
                    "Incorrect. No dormant, condition-triggered malicious "
                    "payload is described; the utility was an ordinary, "
                    "unremoved preinstalled application later exploited "
                    "through an unrelated vulnerability."
                ),
            },
            {
                "id": "d",
                "text": "Rootkit",
                "correct": False,
                "rationale": (
                    "Incorrect. Nothing indicates the utility actively hid "
                    "itself from OS tools; it was a visible, known, but simply "
                    "unremoved preinstalled application."
                ),
            },
        ],
        "explanation": (
            "Unwanted, hard-to-remove vendor-preinstalled software that "
            "expands the attack surface — even without itself being malicious "
            "— is classified as bloatware, distinct from the later exploit "
            "that leveraged it."
        ),
    },
    # ------------------------------------------------------------------ #
    # Network attacks (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2e-032",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network attacks",
        "stem": (
            "A company's public-facing domain suddenly begins resolving to an "
            "attacker-controlled IP address for every service — web, mail, and "
            "VPN — simultaneously. Investigation shows the domain registrar "
            "account was accessed using stolen credentials, and the domain's "
            "nameserver records were changed at the registrar level; the "
            "organization's own authoritative DNS server was never touched or "
            "compromised. Which network attack does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Domain hijacking",
                "correct": True,
                "rationale": (
                    "Correct. Gaining control of a domain's registration or "
                    "registrar account and altering its nameserver records to "
                    "redirect all associated services is the definition of "
                    "domain hijacking."
                ),
            },
            {
                "id": "b",
                "text": "DNS cache poisoning",
                "correct": False,
                "rationale": (
                    "Incorrect. Cache poisoning injects forged records into a "
                    "resolver's cache while the authoritative source remains "
                    "unchanged; here the authoritative nameserver records "
                    "themselves were legitimately changed via a compromised "
                    "registrar account."
                ),
            },
            {
                "id": "c",
                "text": "On-path attack",
                "correct": False,
                "rationale": (
                    "Incorrect. No attacker is intercepting or altering live "
                    "traffic between two communicating parties; the domain's "
                    "own DNS delegation was changed at the source."
                ),
            },
            {
                "id": "d",
                "text": "Distributed denial-of-service (DDoS) attack",
                "correct": False,
                "rationale": (
                    "Incorrect. No flood of traffic or service-overwhelming "
                    "volume is described; services remain available, just "
                    "redirected to attacker infrastructure."
                ),
            },
        ],
        "explanation": (
            "Changing a domain's nameserver records via a compromised "
            "registrar account — redirecting every associated service at once "
            "— is domain hijacking, distinct from cache poisoning, which "
            "targets a resolver's cache rather than the authoritative "
            "registration itself."
        ),
    },
    {
        "id": "nd2e-033",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Network attacks",
        "stem": (
            "Packet captures show an attacker capturing a valid NTLM "
            "authentication exchange between a workstation and a file server "
            "during the morning. Later that same day, the attacker replays the "
            "exact captured hash and response values, unmodified, to "
            "successfully authenticate to a different server on the same "
            "segment — without ever cracking the underlying password. Which "
            "network attack does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Credential replay (pass-the-hash)",
                "correct": True,
                "rationale": (
                    "Correct. Reusing a captured authentication hash value "
                    "directly, without ever cracking it into a plaintext "
                    "password, to authenticate elsewhere is a pass-the-hash "
                    "credential replay attack."
                ),
            },
            {
                "id": "b",
                "text": "On-path attack",
                "correct": False,
                "rationale": (
                    "Incorrect. An on-path attack requires actively "
                    "intercepting and often altering live traffic between two "
                    "parties in real time; here the attacker captured a past "
                    "exchange and reused it hours later against a different "
                    "target."
                ),
            },
            {
                "id": "c",
                "text": "Downgrade attack",
                "correct": False,
                "rationale": (
                    "Incorrect. No protocol negotiation was forced to fall "
                    "back to a weaker version; the standard NTLM exchange was "
                    "simply captured and reused as-is."
                ),
            },
            {
                "id": "d",
                "text": "Kerberoasting",
                "correct": False,
                "rationale": (
                    "Incorrect. Kerberoasting involves requesting a Kerberos "
                    "service ticket and cracking it offline to recover a "
                    "service account password; this scenario involves directly "
                    "reusing a captured NTLM hash, not requesting or cracking "
                    "a Kerberos ticket."
                ),
            },
        ],
        "explanation": (
            "Directly reusing a previously captured authentication hash to log "
            "in elsewhere, without cracking it, is credential replay via "
            "pass-the-hash — distinct from on-path interception, protocol "
            "downgrade, and Kerberoasting."
        ),
    },
    {
        "id": "nd2e-034",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network attacks",
        "stem": (
            "Every day between 2:00 and 2:15 p.m., all Wi-Fi clients throughout "
            "a warehouse simultaneously lose connectivity. A spectrum analyzer "
            "shows a strong, continuous broadband noise signal spanning the "
            "entire 2.4 GHz band during that exact window, rather than a burst "
            "of targeted 802.11 management frames aimed at specific clients. "
            "If this interference is intentional and malicious, which wireless "
            "network attack does this signature MOST closely match?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Jamming",
                "correct": True,
                "rationale": (
                    "Correct. Continuous, broadband RF noise across an entire "
                    "frequency band that disrupts all clients simultaneously, "
                    "rather than targeting individual devices with crafted "
                    "frames, is the signature of RF jamming."
                ),
            },
            {
                "id": "b",
                "text": "Deauthentication attack",
                "correct": False,
                "rationale": (
                    "Incorrect. A deauthentication attack sends targeted "
                    "802.11 management frames to disconnect specific clients "
                    "or access points; the scenario explicitly describes "
                    "continuous broadband noise instead of targeted frames."
                ),
            },
            {
                "id": "c",
                "text": "Evil twin attack",
                "correct": False,
                "rationale": (
                    "Incorrect. An evil twin attack involves a rogue access "
                    "point impersonating a legitimate network to lure clients "
                    "into connecting; no rogue AP or client association is "
                    "described here, only broadband signal interference."
                ),
            },
            {
                "id": "d",
                "text": "Bluejacking",
                "correct": False,
                "rationale": (
                    "Incorrect. Bluejacking involves sending unsolicited "
                    "messages over Bluetooth to nearby devices; this scenario "
                    "describes 2.4 GHz Wi-Fi band-wide interference, not "
                    "Bluetooth messaging."
                ),
            },
        ],
        "explanation": (
            "Continuous, broadband RF noise disrupting all clients across an "
            "entire band is the signature of jamming, distinct from the "
            "targeted management frames used in deauthentication attacks."
        ),
    },
    # ------------------------------------------------------------------ #
    # Physical attacks (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2e-035",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Physical attacks",
        "stem": (
            "Badge logs show an employee's contactless access card was used to "
            "enter a secure server room at 2:00 a.m. At that exact time, the "
            "employee's own account shows them logged into the corporate VPN "
            "from their home, and CCTV footage of the server room door shows an "
            "unfamiliar individual holding a small handheld device near the "
            "card reader just before the door unlocked. Which physical attack "
            "does this MOST likely indicate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "RFID cloning",
                "correct": True,
                "rationale": (
                    "Correct. A badge's credential data captured with a "
                    "handheld proximity reader/skimmer and then replayed to "
                    "unlock a door — while the legitimate cardholder is "
                    "verifiably elsewhere — is the signature of RFID cloning."
                ),
            },
            {
                "id": "b",
                "text": "Tailgating",
                "correct": False,
                "rationale": (
                    "Incorrect. Tailgating involves an unauthorized person "
                    "following an authorized person through a held-open door "
                    "without presenting any credential; here the badge itself "
                    "was actively read and used to unlock the door."
                ),
            },
            {
                "id": "c",
                "text": "Environmental attack",
                "correct": False,
                "rationale": (
                    "Incorrect. No manipulation of temperature, humidity, or "
                    "facility environmental controls is described; the attack "
                    "targets the access-control credential itself."
                ),
            },
            {
                "id": "d",
                "text": "Shoulder surfing",
                "correct": False,
                "rationale": (
                    "Incorrect. Shoulder surfing involves visually observing a "
                    "PIN, password, or credential entry; no PIN or password "
                    "was observed here — a contactless card's data was "
                    "captured and cloned."
                ),
            },
        ],
        "explanation": (
            "A contactless badge's data captured via a nearby handheld reader "
            "and replayed to unlock a door — while the real cardholder is "
            "verifiably elsewhere — is RFID cloning, distinct from tailgating, "
            "which requires no credential capture at all."
        ),
    },
    {
        "id": "nd2e-036",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Physical attacks",
        "stem": (
            "An individual with brief, unmonitored physical access to a data "
            "center's raised-floor plenum adjusts an HVAC sensor's calibration "
            "so it under-reports the actual room temperature by 15 degrees. "
            "Over the following two weeks, several racks of equipment begin "
            "shutting down from thermal overload during peak load, even though "
            "the building management system continuously displays \"normal\" "
            "temperature readings throughout. Which physical attack category "
            "BEST describes this technique?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Environmental attack",
                "correct": True,
                "rationale": (
                    "Correct. Physically tampering with environmental "
                    "monitoring or control equipment — here, an HVAC "
                    "sensor — to induce equipment failure while masking the "
                    "true condition is an environmental physical attack."
                ),
            },
            {
                "id": "b",
                "text": "Brute-force physical attack",
                "correct": False,
                "rationale": (
                    "Incorrect. A brute-force physical attack involves "
                    "forcibly defeating a lock or barrier to gain entry; this "
                    "scenario assumes access was already available and "
                    "involves manipulating environmental sensors, not forcing "
                    "entry."
                ),
            },
            {
                "id": "c",
                "text": "RFID cloning",
                "correct": False,
                "rationale": (
                    "Incorrect. No access-control credential was captured or "
                    "replayed; the attack manipulates an HVAC sensor's "
                    "calibration."
                ),
            },
            {
                "id": "d",
                "text": "Denial-of-service attack",
                "correct": False,
                "rationale": (
                    "Incorrect. Equipment failure is the eventual impact of "
                    "this attack, but the specific physical attack technique "
                    "category being tested — tampering with an environmental "
                    "control sensor — is an environmental attack, not the "
                    "resulting network-layer impact classification."
                ),
            },
        ],
        "explanation": (
            "Deliberately manipulating environmental monitoring equipment, "
            "such as an HVAC sensor's calibration, to cause hidden equipment "
            "failure is classified as an environmental physical attack."
        ),
    },
    # ------------------------------------------------------------------ #
    # Hardening (2.5)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2e-037",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Hardening",
        "stem": (
            "A post-deployment audit of newly provisioned servers finds each "
            "one still has the operating system's default sample web "
            "application, a bundled FTP client, and three unused scripting "
            "language runtimes installed — none of which are required by the "
            "actual production application. Months later, a critical "
            "vulnerability is discovered in one of the unused runtimes, and an "
            "attacker exploits it even though no application on the server "
            "ever actively used that runtime. Which hardening step, applied at "
            "deployment, would have BEST prevented this outcome?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Removal of unnecessary software",
                "correct": True,
                "rationale": (
                    "Correct. Uninstalling default sample applications, "
                    "clients, and runtimes that are not required for the "
                    "server's actual function reduces the installed attack "
                    "surface, regardless of whether that software is being "
                    "actively used."
                ),
            },
            {
                "id": "b",
                "text": "Disabling unused ports and protocols",
                "correct": False,
                "rationale": (
                    "Incorrect. This addresses network-listening services "
                    "exposed on the network, not locally installed but idle "
                    "software packages sitting on disk; the exploited runtime "
                    "was never described as listening on a network port."
                ),
            },
            {
                "id": "c",
                "text": "Host-based firewall configuration",
                "correct": False,
                "rationale": (
                    "Incorrect. A host-based firewall filters network traffic "
                    "to and from the host; it would not prevent local "
                    "exploitation of an installed but unused software runtime "
                    "that doesn't rely on inbound network access."
                ),
            },
            {
                "id": "d",
                "text": "Default password changes",
                "correct": False,
                "rationale": (
                    "Incorrect. No credential or default password issue is "
                    "described; the exposure came from unnecessary installed "
                    "software components, not from an unchanged default "
                    "password."
                ),
            },
        ],
        "explanation": (
            "Uninstalling unneeded default components at deployment time "
            "reduces the installed attack surface, preventing later exploits "
            "of software that was never even actively used."
        ),
    },
    {
        "id": "nd2e-038",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Hardening",
        "stem": (
            "An endpoint is compromised by a malicious script that attempts to "
            "open dozens of new outbound connections to sequential IP "
            "addresses on port 4444 within seconds. A locally installed agent "
            "on the host detects this anomalous connection-behavior pattern in "
            "real time and automatically terminates the offending process and "
            "blocks further connections — all without any signature update or "
            "cloud lookup. Which hardening control provided this specific "
            "behavioral, host-level blocking capability?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Host-based intrusion prevention system (HIPS)",
                "correct": True,
                "rationale": (
                    "Correct. Detecting anomalous behavior patterns in real "
                    "time and automatically terminating the process and "
                    "blocking activity — without relying on signatures — is "
                    "the defining capability of a host-based intrusion "
                    "prevention system."
                ),
            },
            {
                "id": "b",
                "text": "Host-based firewall",
                "correct": False,
                "rationale": (
                    "Incorrect. A standard host-based firewall enforces static "
                    "allow/deny rules based on port and address, but does not "
                    "perform behavioral anomaly detection or automatically "
                    "terminate a misbehaving process the way HIPS does."
                ),
            },
            {
                "id": "c",
                "text": "Endpoint antivirus signature detection",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario explicitly states the blocking "
                    "occurred without any signature update, ruling out "
                    "traditional signature-based antivirus detection as the "
                    "mechanism."
                ),
            },
            {
                "id": "d",
                "text": "Disabling of unused ports and protocols",
                "correct": False,
                "rationale": (
                    "Incorrect. This is a static configuration change made in "
                    "advance, not a real-time behavioral response that "
                    "actively detects and terminates an in-progress malicious "
                    "process."
                ),
            },
        ],
        "explanation": (
            "Real-time detection of anomalous behavior and automatic blocking "
            "of an in-progress attack, without relying on signatures, is the "
            "distinguishing capability of a host-based intrusion prevention "
            "system, as opposed to a static host-based firewall."
        ),
    },
    # ------------------------------------------------------------------ #
    # Mitigation techniques (2.5)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2e-039",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mitigation techniques",
        "stem": (
            "After a malware outbreak caused by employees running unauthorized "
            "executables downloaded from email attachments, a security team "
            "implements a control that permits only a specific, cryptographically "
            "signed set of approved applications to execute on endpoints. Any "
            "unrecognized binary — even one that antivirus does not flag as "
            "malicious — is blocked from running by default. Which mitigation "
            "technique has been implemented?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Application allow listing",
                "correct": True,
                "rationale": (
                    "Correct. Permitting only a defined, approved set of "
                    "signed applications to run, and blocking everything else "
                    "by default regardless of antivirus flagging, is "
                    "application allow listing."
                ),
            },
            {
                "id": "b",
                "text": "Antivirus signature detection",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario explicitly contrasts this control "
                    "with antivirus flagging, noting unrecognized binaries are "
                    "blocked \"even if not flagged as malicious\" — the "
                    "control here is a default-deny execution policy, not "
                    "signature-based detection."
                ),
            },
            {
                "id": "c",
                "text": "Host-based firewall",
                "correct": False,
                "rationale": (
                    "Incorrect. A host-based firewall controls network traffic "
                    "to and from the host; it does not govern which local "
                    "executables are permitted to run."
                ),
            },
            {
                "id": "d",
                "text": "Least privilege",
                "correct": False,
                "rationale": (
                    "Incorrect. Least privilege limits the permissions and "
                    "access rights an account or process holds; it does not by "
                    "itself define which specific applications are permitted "
                    "to execute."
                ),
            },
        ],
        "explanation": (
            "A default-deny policy that permits only a defined, signed set of "
            "approved applications to run — independent of antivirus flagging "
            "— is application allow listing."
        ),
    },
    {
        "id": "nd2e-040",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Mitigation techniques",
        "stem": (
            "Following a breach in which a compromised web server in the DMZ "
            "was used to pivot laterally into the finance VLAN and access an "
            "unpatched file server that had been decommissioned in name only "
            "but left powered on, the security team's remediation plan "
            "includes:\n\n"
            "(1) Deploying firewall rules between the DMZ and internal VLANs "
            "that block all traffic except explicitly required ports.\n\n"
            "(2) Powering off and physically removing the abandoned file "
            "server from the network entirely, since it no longer serves any "
            "business purpose.\n\n"
            "Which TWO mitigation techniques are represented by these two "
            "remediation steps, respectively? (Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Segmentation",
                "correct": True,
                "rationale": (
                    "Correct. Restricting traffic between network zones (DMZ "
                    "and internal VLANs) to only explicitly required ports is "
                    "network segmentation, limiting lateral movement between "
                    "zones (Step 1)."
                ),
            },
            {
                "id": "b",
                "text": "Decommissioning",
                "correct": True,
                "rationale": (
                    "Correct. Powering off and permanently removing an asset "
                    "that no longer serves a business purpose is "
                    "decommissioning, eliminating the unpatched attack surface "
                    "entirely (Step 2)."
                ),
            },
            {
                "id": "c",
                "text": "Isolation",
                "correct": False,
                "rationale": (
                    "Incorrect. Isolation typically refers to quarantining a "
                    "single specific compromised host away from the rest of "
                    "the network; the firewall rules described here restrict "
                    "traffic between entire network zones, which is "
                    "segmentation, not isolation of one host."
                ),
            },
            {
                "id": "d",
                "text": "Patching",
                "correct": False,
                "rationale": (
                    "Incorrect. No patch was applied to the file server — it "
                    "was removed from the network entirely rather than being "
                    "updated."
                ),
            },
            {
                "id": "e",
                "text": "Least privilege",
                "correct": False,
                "rationale": (
                    "Incorrect. Neither remediation step involves adjusting "
                    "account or process permission levels; both are network "
                    "architecture and asset-lifecycle actions."
                ),
            },
        ],
        "explanation": (
            "Restricting traffic between network zones is segmentation, and "
            "permanently removing an unneeded, unpatched asset from the "
            "network is decommissioning — two distinct mitigation techniques "
            "matched to the two described remediation steps."
        ),
    },
]

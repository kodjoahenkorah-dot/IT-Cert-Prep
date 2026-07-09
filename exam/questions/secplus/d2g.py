"""Security+ SY0-701 practice questions — Domain 2 (Threats, Vulnerabilities,
and Mitigations), batch G.

39 scenario-driven questions (35 multiple_choice + 4 multiple_response)
covering every study_topic label listed under domain 2 in
``_topic_labels.json``.
"""

from __future__ import annotations

QUESTIONS = [
    # ------------------------------------------------------------------ #
    # Threat actors (2.1)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2g-001",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Threat actors",
        "stem": (
            "A regional power-grid operator's SCADA historian servers are "
            "found to have been accessed by an intruder who used custom-built "
            "tooling exploiting an undocumented detail of the operator's "
            "proprietary equipment protocol. The intrusion persisted for "
            "eleven months with no observed impact until a scheduled firmware "
            "audit uncovered it, and the timeline correlates with escalating "
            "diplomatic tension between the operator's home country and a "
            "rival nation. Which threat actor is MOST likely responsible?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Nation-state actor",
                "correct": True,
                "rationale": (
                    "Correct. Deep, protocol-specific custom tooling, "
                    "extraordinary patience over nearly a year with no "
                    "observed impact, targeting of critical infrastructure, "
                    "and a timeline tied to geopolitical tension are the "
                    "hallmark signature of a well-resourced nation-state "
                    "operation."
                ),
            },
            {
                "id": "b",
                "text": "Organized crime",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no ransom demand, extortion, or "
                    "monetization attempt; profit-driven criminal groups "
                    "rarely invest in undocumented protocol research with no "
                    "financial payoff."
                ),
            },
            {
                "id": "c",
                "text": "Hacktivist",
                "correct": False,
                "rationale": (
                    "Incorrect. Hacktivism is defined by public, ideological "
                    "messaging intended to draw attention to a cause; this "
                    "intrusion was covert and produced no public statement or "
                    "defacement."
                ),
            },
            {
                "id": "d",
                "text": "Unskilled attacker",
                "correct": False,
                "rationale": (
                    "Incorrect. Building custom tooling around an "
                    "undocumented, proprietary protocol detail requires deep "
                    "expertise and resources far beyond an unskilled "
                    "attacker's reliance on off-the-shelf scripts."
                ),
            },
        ],
        "explanation": (
            "Patient, protocol-specific custom tooling against critical "
            "infrastructure, timed to geopolitical tension and producing no "
            "public claim, points to a nation-state actor rather than a "
            "profit-driven, ideological, or low-skill actor."
        ),
    },
    {
        "id": "nd2g-002",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Threat actors",
        "stem": (
            "A post on a closed cybercrime forum offers verified "
            "administrative RDP credentials to a mid-sized hospital's network "
            "for $1,200. The seller has a documented history of similar "
            "access sales and works alongside separate forum members who "
            "specialize in ransomware deployment, victim negotiation, and "
            "laundering cryptocurrency payments once a buyer closes the deal. "
            "Which threat actor classification BEST describes the seller's "
            "role?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Organized crime (an initial access broker within a "
                    "structured criminal ecosystem)"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A repeat seller of network access working "
                    "alongside specialists in deployment, negotiation, and "
                    "laundering describes a structured, profit-driven "
                    "criminal supply chain — the defining trait of organized "
                    "crime."
                ),
            },
            {
                "id": "b",
                "text": "Nation-state actor",
                "correct": False,
                "rationale": (
                    "Incorrect. Selling access to any paying buyer for a "
                    "flat fee, with no espionage or strategic objective, is "
                    "inconsistent with a nation-state's typically covert, "
                    "mission-driven operations."
                ),
            },
            {
                "id": "c",
                "text": "Hacktivist",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no ideological cause or public "
                    "statement involved; the transaction is purely financial."
                ),
            },
            {
                "id": "d",
                "text": "Shadow IT",
                "correct": False,
                "rationale": (
                    "Incorrect. Shadow IT describes an internal employee's "
                    "unsanctioned technology use, not an external criminal "
                    "seller monetizing stolen access on a forum."
                ),
            },
        ],
        "explanation": (
            "A repeat access seller operating alongside specialized "
            "criminal collaborators for ransomware, negotiation, and money "
            "laundering describes organized crime, not a state actor, "
            "ideological group, or an internal governance failure."
        ),
    },
    # ------------------------------------------------------------------ #
    # Social engineering (2.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2g-003",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Social engineering",
        "stem": (
            "During a live video conference call, an employee sees what "
            "appears to be the CFO, with the CFO's face and voice, urgently "
            "requesting an emergency wire transfer to close an acquisition "
            "before markets close. Subtle unnatural blinking and a slight "
            "audio-to-video sync delay prompt the employee to end the call "
            "and phone the CFO's known number directly, who confirms no such "
            "call ever took place. Which social engineering technique was "
            "used?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Impersonation, carried out through real-time deepfake "
                    "video and voice synthesis"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Synthesizing a real executive's likeness and "
                    "voice to convincingly pose as that person on a live call "
                    "is impersonation, here enabled by deepfake technology."
                ),
            },
            {
                "id": "b",
                "text": "Vishing",
                "correct": False,
                "rationale": (
                    "Incorrect. Vishing describes voice-only phone-based "
                    "social engineering; this attack used a synthesized "
                    "live video feed of the executive's face, going beyond a "
                    "voice-only phone call."
                ),
            },
            {
                "id": "c",
                "text": "Business email compromise",
                "correct": False,
                "rationale": (
                    "Incorrect. No email account was compromised or spoofed; "
                    "the entire attack occurred over a live video conference "
                    "call."
                ),
            },
            {
                "id": "d",
                "text": "Watering hole attack",
                "correct": False,
                "rationale": (
                    "Incorrect. No legitimate website frequented by the "
                    "victim was compromised; this was a direct, real-time "
                    "impersonation attempt."
                ),
            },
        ],
        "explanation": (
            "Synthesizing a real person's face and voice in real time to "
            "convincingly pose as them on a video call is impersonation "
            "enabled by deepfake technology, distinct from voice-only "
            "vishing, email-based BEC, or a compromised website."
        ),
    },
    {
        "id": "nd2g-004",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Social engineering",
        "stem": (
            "A procurement employee receives a phone call from someone "
            "claiming to be a state licensing auditor who says the "
            "company's contractor license will be suspended within the hour "
            "unless outstanding 'verification documents' are emailed "
            "immediately. The caller references specific internal purchase "
            "order numbers to sound credible and repeatedly stresses that "
            "hesitation will be reported to the employee's supervisor. Which "
            "TWO psychological principles are being MOST heavily leveraged? "
            "(Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Urgency",
                "correct": True,
                "rationale": (
                    "Correct. The one-hour suspension deadline is designed "
                    "to force a rushed decision before the employee can "
                    "verify the caller's legitimacy."
                ),
            },
            {
                "id": "b",
                "text": "Authority",
                "correct": True,
                "rationale": (
                    "Correct. Posing as a government licensing auditor with "
                    "power to suspend the company's license, and threatening "
                    "to escalate to the employee's supervisor, invokes "
                    "perceived official authority to compel compliance."
                ),
            },
            {
                "id": "c",
                "text": "Scarcity",
                "correct": False,
                "rationale": (
                    "Incorrect. Scarcity relies on a limited quantity or "
                    "availability (e.g., 'only 3 spots left'), not a "
                    "suspension deadline tied to authority."
                ),
            },
            {
                "id": "d",
                "text": "Consensus/social proof",
                "correct": False,
                "rationale": (
                    "Incorrect. No claim is made that other employees or "
                    "peers have already complied; the pressure comes from "
                    "authority and urgency, not peer behavior."
                ),
            },
            {
                "id": "e",
                "text": "Familiarity/liking",
                "correct": False,
                "rationale": (
                    "Incorrect. The caller builds credibility through "
                    "referenced PO numbers and claimed authority, not "
                    "through rapport, friendliness, or an existing "
                    "relationship."
                ),
            },
        ],
        "explanation": (
            "A hard deadline paired with an official-sounding role and an "
            "escalation threat combines urgency and authority — the two "
            "principles doing the actual psychological work here, not "
            "scarcity, social proof, or likability."
        ),
    },
    {
        "id": "nd2g-005",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Social engineering",
        "stem": (
            "An email spoofed from the lookalike domain "
            "\"genera1counsel-legal.com\" (a numeral '1' replacing the "
            "letter 'l') is sent only to the company's three regional vice "
            "presidents, falsely claiming each is personally named in a "
            "pending lawsuit and must wire a confidential settlement payment "
            "within 24 hours to avoid personal liability, bypassing the "
            "standard finance approval workflow. Which social engineering "
            "attack does this represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Whaling",
                "correct": True,
                "rationale": (
                    "Correct. Deliberately narrow targeting of only three "
                    "named senior executives with a high-stakes, personally "
                    "threatening pretext is the defining trait of whaling — "
                    "phishing aimed specifically at high-value individuals."
                ),
            },
            {
                "id": "b",
                "text": "Business email compromise",
                "correct": False,
                "rationale": (
                    "Incorrect. BEC typically relies on a compromised or "
                    "highly convincing spoof of an established, trusted "
                    "business relationship, often targeting broader finance "
                    "staff; the giveaway here is the intentionally narrow "
                    "targeting of three senior executives, which points more "
                    "specifically to whaling."
                ),
            },
            {
                "id": "c",
                "text": "Typosquatting",
                "correct": False,
                "rationale": (
                    "Incorrect. Typosquatting describes only the "
                    "lookalike-domain mechanic used to deliver the message; "
                    "it does not capture the full attack pattern of a "
                    "narrowly targeted, high-stakes campaign against senior "
                    "executives."
                ),
            },
            {
                "id": "d",
                "text": "Vishing",
                "correct": False,
                "rationale": (
                    "Incorrect. The attack was delivered entirely by email, "
                    "not a phone call."
                ),
            },
        ],
        "explanation": (
            "Narrowly targeting a small number of specific senior "
            "executives with a personalized, high-stakes pretext is whaling; "
            "the lookalike domain is only the delivery mechanism, and no "
            "compromised business mailbox or phone call is involved."
        ),
    },
    # ------------------------------------------------------------------ #
    # Threat vectors and attack surfaces (2.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2g-006",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Threat vectors and attack surfaces",
        "stem": (
            "A public job-application portal allows candidates to upload a "
            "resume in DOCX, PDF, or DOC format. An attacker submits a "
            "macro-enabled DOTM template file renamed with a .doc extension. "
            "When an HR reviewer opens the file and clicks 'Enable Editing,' "
            "an embedded VBA macro downloads and executes a second-stage "
            "payload. Which attack vector did the attacker exploit to "
            "deliver the initial payload?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A file-based vector through an unrestricted "
                    "public-facing upload feature"
                ),
                "correct": True,
                "rationale": (
                    "Correct. The portal accepted an attacker-controlled "
                    "file with disguised content and no effective type or "
                    "content validation, delivering the payload as a file "
                    "through a public upload feature."
                ),
            },
            {
                "id": "b",
                "text": "A message-based vector",
                "correct": False,
                "rationale": (
                    "Incorrect. Delivery occurred through a website upload "
                    "form, not an email or SMS message."
                ),
            },
            {
                "id": "c",
                "text": "A removable media vector",
                "correct": False,
                "rationale": (
                    "Incorrect. No physical media such as a USB drive was "
                    "ever involved; the file was submitted online."
                ),
            },
            {
                "id": "d",
                "text": "An unsecure network vector",
                "correct": False,
                "rationale": (
                    "Incorrect. No network protocol weakness was exploited; "
                    "the exposure is the upload feature's failure to "
                    "restrict file type and content."
                ),
            },
        ],
        "explanation": (
            "A weaponized file accepted through a public upload feature "
            "with no effective content restrictions is a file-based attack "
            "vector, not a message, removable-media, or network-based one."
        ),
    },
    {
        "id": "nd2g-007",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Threat vectors and attack surfaces",
        "stem": (
            "A company's customer-support portal embeds a live-chat widget "
            "by loading a JavaScript file directly from the chat vendor's "
            "CDN. The vendor's CDN account is later compromised, and the "
            "served JavaScript file is modified to capture every keystroke "
            "typed into the support portal's forms, including a payment "
            "field, without any change to the support portal's own code or "
            "servers. Which attack surface was exploited?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A supply chain (third-party vendor) attack surface",
                "correct": True,
                "rationale": (
                    "Correct. The support portal's own systems were never "
                    "touched; the compromise occurred in a trusted "
                    "third-party vendor's infrastructure that the portal "
                    "relies on and pulls code from directly."
                ),
            },
            {
                "id": "b",
                "text": "A removable media attack surface",
                "correct": False,
                "rationale": (
                    "Incorrect. No physical media was involved in this "
                    "web-based compromise."
                ),
            },
            {
                "id": "c",
                "text": "An unsecure network attack surface",
                "correct": False,
                "rationale": (
                    "Incorrect. Data was captured through malicious "
                    "JavaScript executing in the victim's browser, not "
                    "through a network eavesdropping weakness."
                ),
            },
            {
                "id": "d",
                "text": "A default credentials attack surface",
                "correct": False,
                "rationale": (
                    "Incorrect. No credential is described; the vendor's "
                    "own account was compromised through means unrelated to "
                    "the support portal, which simply trusted the vendor's "
                    "code."
                ),
            },
        ],
        "explanation": (
            "Malicious code delivered through a trusted third-party "
            "vendor's compromised infrastructure, with no change to the "
            "portal's own systems, is a supply chain attack surface."
        ),
    },
    # ------------------------------------------------------------------ #
    # Application vulnerabilities (2.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2g-008",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Application vulnerabilities",
        "stem": (
            "Endpoint forensics on a compromised server show that a "
            "legitimate, digitally signed svchost.exe process was launched "
            "in a suspended state, had its original executable image "
            "unmapped from memory, and had malicious code written into the "
            "now-empty memory region before the process was resumed — "
            "allowing the malicious code to run under the identity and "
            "privileges of a trusted system process. Which application "
            "vulnerability class does this technique exploit?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Memory injection",
                "correct": True,
                "rationale": (
                    "Correct. Writing malicious code directly into a "
                    "process's memory space and executing it there — as "
                    "process hollowing does — is memory injection."
                ),
            },
            {
                "id": "b",
                "text": "Buffer overflow",
                "correct": False,
                "rationale": (
                    "Incorrect. No bounds-checking failure or data overrun "
                    "occurred; the attacker deliberately replaced process "
                    "memory content using legitimate process-creation APIs, "
                    "not by overflowing a buffer."
                ),
            },
            {
                "id": "c",
                "text": "Race condition (TOC/TOU)",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no time-of-check/time-of-use gap "
                    "being exploited between two operations."
                ),
            },
            {
                "id": "d",
                "text": "Malicious update",
                "correct": False,
                "rationale": (
                    "Incorrect. No software update mechanism was involved; "
                    "the payload was injected into an already-running "
                    "process, not delivered as a trojanized update package."
                ),
            },
        ],
        "explanation": (
            "Process hollowing — unmapping a legitimate process's memory "
            "and writing malicious code into it — is a textbook memory "
            "injection technique, distinct from buffer overflow, race "
            "conditions, or malicious updates."
        ),
    },
    {
        "id": "nd2g-009",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Application vulnerabilities",
        "stem": (
            "A company's internal Python package, named 'acmepay-utils', is "
            "hosted only on a private internal package index and has never "
            "been published publicly. During a routine build, the CI/CD "
            "pipeline's package installer is reconfigured to also check the "
            "public PyPI index, where an attacker has since published a "
            "package with the identical name and a higher version number "
            "than the internal one. The installer automatically resolves "
            "and installs the attacker's public package, running its "
            "embedded install script and exfiltrating the pipeline's cloud "
            "deployment secrets. Which application vulnerability BEST "
            "describes what allowed this to happen?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A malicious update (dependency confusion) "
                    "supply-chain vulnerability"
                ),
                "correct": True,
                "rationale": (
                    "Correct. The build pipeline was tricked into "
                    "installing an attacker-published package instead of "
                    "the trusted internal one because the resolver favored "
                    "a higher version number from an untrusted public "
                    "source — the classic dependency confusion attack "
                    "against the software update/build process."
                ),
            },
            {
                "id": "b",
                "text": "A race condition (TOC/TOU)",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no gap between checking and using "
                    "a resource; the resolver simply chose the wrong "
                    "package source based on version-number logic."
                ),
            },
            {
                "id": "c",
                "text": "A buffer overflow",
                "correct": False,
                "rationale": (
                    "Incorrect. No memory bounds-checking failure occurred; "
                    "the compromise happened entirely at the package "
                    "resolution and installation level."
                ),
            },
            {
                "id": "d",
                "text": "Memory injection",
                "correct": False,
                "rationale": (
                    "Incorrect. No running process's memory was directly "
                    "altered; the malicious code arrived through a "
                    "trusted-seeming install/update process instead."
                ),
            },
        ],
        "explanation": (
            "Publishing an identically named, higher-versioned package to "
            "a public registry so an automated build process installs it "
            "instead of the intended private package is a malicious "
            "update/supply-chain (dependency confusion) attack."
        ),
    },
    {
        "id": "nd2g-010",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Application vulnerabilities",
        "stem": (
            "A researcher analyzing a VPN client discovers that its "
            "certificate-parsing routine copies the Common Name field from "
            "a presented X.509 certificate into a fixed 64-byte stack "
            "buffer using a function that performs no length checking. By "
            "presenting a malicious VPN gateway certificate with a 400-byte "
            "Common Name containing crafted shellcode, the researcher "
            "overwrites the function's return address and achieves "
            "arbitrary code execution on the client. Which application "
            "vulnerability was exploited?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Buffer overflow",
                "correct": True,
                "rationale": (
                    "Correct. Copying oversized, attacker-controlled data "
                    "into a fixed-size buffer with no length check, "
                    "overwriting the return address, is a classic stack "
                    "buffer overflow."
                ),
            },
            {
                "id": "b",
                "text": "Race condition (TOC/TOU)",
                "correct": False,
                "rationale": (
                    "Incorrect. No gap between checking and using a "
                    "resource is exploited; the flaw is a missing length "
                    "check during a single copy operation."
                ),
            },
            {
                "id": "c",
                "text": "Malicious update",
                "correct": False,
                "rationale": (
                    "Incorrect. No software update mechanism was involved; "
                    "the vulnerability was triggered by a malicious "
                    "certificate presented during a connection."
                ),
            },
            {
                "id": "d",
                "text": "Memory injection",
                "correct": False,
                "rationale": (
                    "Incorrect. The attacker did not inject code into an "
                    "already-running process through process manipulation; "
                    "the code path was corrupted through an unchecked, "
                    "oversized copy into a fixed-size buffer, the defining "
                    "trait of a buffer overflow."
                ),
            },
        ],
        "explanation": (
            "An unchecked copy of attacker-controlled, oversized data into "
            "a fixed-size stack buffer that overwrites the return address "
            "is a buffer overflow, not a race condition, malicious update, "
            "or memory injection."
        ),
    },
    # ------------------------------------------------------------------ #
    # Mobile vulnerabilities (2.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2g-011",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile vulnerabilities",
        "stem": (
            "A user plugs their phone into an ordinary-looking USB charging "
            "cable borrowed from a colleague. Within seconds of connecting, "
            "the phone's terminal app opens and begins typing commands as "
            "though from a physical keyboard, with no user interaction and "
            "no on-screen prompt about the connection type. Which BEST "
            "explains what happened?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The cable contains embedded HID-emulation hardware "
                    "that injects keystrokes once connected"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A weaponized cable with hidden "
                    "keyboard-emulation hardware can autonomously type "
                    "commands the instant it is plugged in, with no data-"
                    "transfer prompt or user action required."
                ),
            },
            {
                "id": "b",
                "text": "Juice jacking transferred malware over the data pins",
                "correct": False,
                "rationale": (
                    "Incorrect. Juice jacking transfers data/malware over "
                    "the USB data pins through the phone's normal USB "
                    "stack, which typically involves some device-side "
                    "prompt or trust action; here, keystrokes began "
                    "instantly with no such prompt, consistent with a "
                    "cable that itself behaves as a keyboard peripheral."
                ),
            },
            {
                "id": "c",
                "text": "Bluesnarfing extracted data over Bluetooth",
                "correct": False,
                "rationale": (
                    "Incorrect. No Bluetooth pairing or connection is "
                    "involved; the phone was connected by a physical wired "
                    "cable."
                ),
            },
            {
                "id": "d",
                "text": "The phone was jailbroken",
                "correct": False,
                "rationale": (
                    "Incorrect. Nothing indicates the device's OS "
                    "restrictions were removed; the malicious behavior "
                    "originated entirely from the peripheral hardware."
                ),
            },
        ],
        "explanation": (
            "A cable with embedded HID-emulation hardware can act as a "
            "keyboard and inject keystrokes the moment it is connected, "
            "distinct from juice jacking's data-transfer mechanism, "
            "Bluetooth-based bluesnarfing, or a jailbreak."
        ),
    },
    {
        "id": "nd2g-012",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile vulnerabilities",
        "stem": (
            "An Android banking app is found to display a pixel-perfect "
            "fake login overlay whenever the legitimate banking app is "
            "opened, capturing credentials before silently passing them "
            "through to the real app. Investigation traces this to a game "
            "app, sideloaded from a third-party store, that requested and "
            "was granted Accessibility Service permissions. Which "
            "vulnerability BEST explains the credential theft?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A screen-overlay attack enabled by an app abusing "
                    "granted Accessibility Service permissions"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Accessibility Service permissions grant an "
                    "app the ability to observe screen content and draw "
                    "over other apps; a malicious app abusing this "
                    "capability can display a convincing fake login overlay "
                    "on top of a legitimate app."
                ),
            },
            {
                "id": "b",
                "text": "SIM swapping",
                "correct": False,
                "rationale": (
                    "Incorrect. No carrier account takeover or phone number "
                    "port is described; the theft occurred entirely through "
                    "an on-device overlay."
                ),
            },
            {
                "id": "c",
                "text": "Bluesnarfing",
                "correct": False,
                "rationale": (
                    "Incorrect. No Bluetooth-based data theft is involved."
                ),
            },
            {
                "id": "d",
                "text": "Juice jacking",
                "correct": False,
                "rationale": (
                    "Incorrect. No USB charging connection is described; "
                    "the attack occurred entirely through an installed "
                    "app's abused permissions."
                ),
            },
        ],
        "explanation": (
            "Excessive Accessibility Service permissions granted to a "
            "sideloaded app enabled a screen-overlay credential-theft "
            "attack, unrelated to SIM swapping, bluesnarfing, or juice "
            "jacking."
        ),
    },
    # ------------------------------------------------------------------ #
    # Virtualization vulnerabilities (2.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2g-013",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Virtualization vulnerabilities",
        "stem": (
            "A shared GPU cluster used for machine-learning training "
            "allocates the same physical graphics card to sequential "
            "customer jobs without clearing the card's video memory (VRAM) "
            "between allocations. A customer's newly started training job "
            "crashes, and the resulting core dump contains recognizable "
            "fragments of a different customer's proprietary model weights "
            "that were never cleared from VRAM by the previous job. Which "
            "virtualization vulnerability does this illustrate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Resource reuse",
                "correct": True,
                "rationale": (
                    "Correct. Sensitive data from a prior tenant's use of "
                    "shared virtualized hardware persisted and became "
                    "accessible to the next tenant because the resource "
                    "(VRAM) was not sanitized between allocations — data "
                    "remanence in a reused resource."
                ),
            },
            {
                "id": "b",
                "text": "VM escape",
                "correct": False,
                "rationale": (
                    "Incorrect. No code executed outside its assigned "
                    "VM/container boundary or gained host-level access; the "
                    "issue is leftover data in a shared hardware resource, "
                    "not a boundary escape."
                ),
            },
            {
                "id": "c",
                "text": "Live migration interception",
                "correct": False,
                "rationale": (
                    "Incorrect. No VM migration process occurred; the data "
                    "leak came from unsanitized shared GPU memory."
                ),
            },
            {
                "id": "d",
                "text": "VM sprawl",
                "correct": False,
                "rationale": (
                    "Incorrect. This is not a case of unmanaged or orphaned "
                    "VMs; a single properly tracked hardware resource was "
                    "reused without sanitization."
                ),
            },
        ],
        "explanation": (
            "Failing to clear a shared physical resource's memory between "
            "tenants is resource reuse (data remanence), distinct from a "
            "VM escape, migration interception, or VM sprawl."
        ),
    },
    {
        "id": "nd2g-014",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Virtualization vulnerabilities",
        "stem": (
            "A cloud provider's security team discovers that a customer's "
            "VM was able to send specially crafted commands to the "
            "hypervisor's emulated virtual floppy disk controller, "
            "triggering a buffer overflow in the emulation code itself and "
            "allowing the VM to execute arbitrary code directly on the host "
            "hypervisor, affecting every other VM on that host. Which "
            "virtualization vulnerability does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "VM escape",
                "correct": True,
                "rationale": (
                    "Correct. Exploiting a flaw in the hypervisor's device "
                    "emulation code to execute code on the host, outside "
                    "the guest VM's boundary and affecting other tenants, "
                    "is the definition of a VM escape."
                ),
            },
            {
                "id": "b",
                "text": "Resource reuse",
                "correct": False,
                "rationale": (
                    "Incorrect. No leftover data from a prior tenant was "
                    "recovered; this is a live boundary-breaking exploit "
                    "against emulation code, not a data-remanence issue."
                ),
            },
            {
                "id": "c",
                "text": "VM sprawl",
                "correct": False,
                "rationale": (
                    "Incorrect. This scenario has nothing to do with "
                    "unmanaged or orphaned VM inventory."
                ),
            },
            {
                "id": "d",
                "text": "Live migration interception",
                "correct": False,
                "rationale": (
                    "Incorrect. No migration traffic was captured; the "
                    "exploit targeted the virtual device emulation code "
                    "directly."
                ),
            },
        ],
        "explanation": (
            "A guest VM exploiting a hypervisor device-emulation flaw to "
            "execute code on the host, impacting every other VM, is a VM "
            "escape, not resource reuse, sprawl, or migration interception."
        ),
    },
    # ------------------------------------------------------------------ #
    # Vulnerability scan and assessment result classification (2.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2g-015",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability scan and assessment result classification",
        "stem": (
            "A vulnerability scanner flags a critical, unpatched OpenSSL "
            "remote code execution vulnerability on a Linux application "
            "server, based on the version string returned in the service "
            "banner. The security team manually confirms, via the OS "
            "package manager, that the vendor backported the security fix "
            "into the currently installed package without changing the "
            "reported version string, and confirms with a targeted exploit "
            "attempt that the server is not actually exploitable. How "
            "should this finding be classified?"
        ),
        "options": [
            {
                "id": "a",
                "text": "False positive",
                "correct": True,
                "rationale": (
                    "Correct. The scanner reported a vulnerability that "
                    "manual verification, including a failed exploit "
                    "attempt, confirms does not actually exist on this "
                    "server."
                ),
            },
            {
                "id": "b",
                "text": "True positive",
                "correct": False,
                "rationale": (
                    "Incorrect. Manual verification disproved the finding; "
                    "a true positive requires the vulnerability to actually "
                    "be present and exploitable."
                ),
            },
            {
                "id": "c",
                "text": "False negative",
                "correct": False,
                "rationale": (
                    "Incorrect. A false negative is a real vulnerability "
                    "the scanner failed to report; here the scanner "
                    "over-reported a vulnerability that does not actually "
                    "exist."
                ),
            },
            {
                "id": "d",
                "text": "True negative",
                "correct": False,
                "rationale": (
                    "Incorrect. A true negative requires the scanner to "
                    "report no vulnerability where none exists; this "
                    "scanner did report a vulnerability, incorrectly."
                ),
            },
        ],
        "explanation": (
            "A backported fix that leaves the version banner unchanged "
            "causes a scanner to flag a vulnerability that manual testing "
            "disproves — a false positive, not a true positive, false "
            "negative, or true negative."
        ),
    },
    {
        "id": "nd2g-016",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Vulnerability scan and assessment result classification",
        "stem": (
            "A quarterly vulnerability scan report shows zero findings for "
            "every host in a subnet. A post-scan review of the scanning "
            "tool's job log reveals that the scan credential for that "
            "subnet had expired three days before the scan ran, causing the "
            "scanner to silently skip authenticated testing and exclude "
            "every host in that subnet entirely — though the summary report "
            "listed the subnet as 'completed' with no findings. Six weeks "
            "later, one of those hosts is compromised through a "
            "vulnerability that a properly authenticated scan would have "
            "detected. How should the original 'zero findings' result for "
            "that subnet be classified?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Neither a true negative nor a false negative — the "
                    "hosts were never actually tested, so no valid result "
                    "exists for them"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A true or false negative both presuppose that "
                    "the scanner actually examined the host; here, the "
                    "expired credential caused the hosts to be silently "
                    "skipped, so 'zero findings' reflects an untested scope, "
                    "not a valid assessment result."
                ),
            },
            {
                "id": "b",
                "text": (
                    "A false negative, because a real vulnerability existed "
                    "and was not reported"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A false negative requires the scanner to "
                    "have actually examined the host and missed the flaw; "
                    "here the hosts were skipped entirely due to the "
                    "credential failure, so no test was ever performed to "
                    "fail."
                ),
            },
            {
                "id": "c",
                "text": (
                    "A true negative, because no vulnerability was "
                    "reported and the compromise happened on a different "
                    "schedule"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A true negative requires the scanner to "
                    "correctly find no vulnerabilities where none exist; a "
                    "vulnerability did exist and was never assessed at all."
                ),
            },
            {
                "id": "d",
                "text": (
                    "A true positive, because the scan job ultimately "
                    "completed and produced a report"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Job completion status does not equal a "
                    "valid finding; the report reflects an untested scope, "
                    "not an accurate assessment of the hosts' security "
                    "posture."
                ),
            },
        ],
        "explanation": (
            "A scan that silently skips hosts due to an expired credential "
            "produces no valid true/false positive/negative result at all "
            "for those hosts — the finding must be recognized as an "
            "untested coverage gap, not misclassified as a false negative "
            "or true negative."
        ),
    },
    # ------------------------------------------------------------------ #
    # Web application vulnerabilities (2.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2g-017",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Web application vulnerabilities",
        "stem": (
            "A web application uses a server-side templating engine to "
            "render user-supplied 'display name' fields. A tester submits a "
            "display name of \"{{7*7}}\" and observes the rendered page "
            "shows '49' instead of the literal text. Building on this, the "
            "tester submits a payload that reaches the templating engine's "
            "underlying configuration object and calls a method capable of "
            "executing OS commands, achieving full remote code execution on "
            "the server. Which web application vulnerability was exploited?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Server-side template injection (SSTI)",
                "correct": True,
                "rationale": (
                    "Correct. The server itself evaluated user input as "
                    "template expression code, ultimately reaching a method "
                    "that executed OS commands — the defining behavior of "
                    "server-side template injection."
                ),
            },
            {
                "id": "b",
                "text": "Reflected cross-site scripting (XSS)",
                "correct": False,
                "rationale": (
                    "Incorrect. XSS causes a victim's browser to execute "
                    "attacker-supplied script client-side; here the server "
                    "evaluated the input as template code and executed it "
                    "server-side, achieving remote code execution on the "
                    "server itself."
                ),
            },
            {
                "id": "c",
                "text": "Server-side request forgery (SSRF)",
                "correct": False,
                "rationale": (
                    "Incorrect. No request was induced from the server to "
                    "another internal or external resource; exploitation "
                    "occurred entirely through template expression "
                    "evaluation."
                ),
            },
            {
                "id": "d",
                "text": "XML external entity (XXE) injection",
                "correct": False,
                "rationale": (
                    "Incorrect. No XML parser or DOCTYPE/entity declaration "
                    "is involved; the vulnerable component is a template "
                    "rendering engine, not an XML parser."
                ),
            },
        ],
        "explanation": (
            "Confirming code evaluation with {{7*7}} and then reaching an "
            "executable method through the template engine's object model "
            "is server-side template injection, distinct from XSS, SSRF, "
            "or XXE."
        ),
    },
    {
        "id": "nd2g-018",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Web application vulnerabilities",
        "stem": (
            "A single-page application's GraphQL API leaves introspection "
            "enabled in production. A researcher queries the schema and "
            "discovers an undocumented adminDeleteUser mutation. The "
            "researcher, authenticated only as a standard non-administrative "
            "user, successfully calls this mutation and deletes another "
            "user's account, because the API validates that the caller is "
            "authenticated but never checks whether the caller holds "
            "administrative privileges before executing the mutation. Which "
            "vulnerability BEST explains why the deletion succeeded?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Broken access control (missing function-level authorization)",
                "correct": True,
                "rationale": (
                    "Correct. The API confirmed the caller was logged in but "
                    "never verified the caller was authorized to invoke an "
                    "administrative function — a missing function-level "
                    "authorization check, a form of broken access control."
                ),
            },
            {
                "id": "b",
                "text": "Cross-site request forgery (CSRF)",
                "correct": False,
                "rationale": (
                    "Incorrect. The researcher made a deliberate, "
                    "authenticated direct call; no victim's browser was "
                    "tricked into submitting a forged request."
                ),
            },
            {
                "id": "c",
                "text": "Server-side request forgery (SSRF)",
                "correct": False,
                "rationale": (
                    "Incorrect. No request was forced against an "
                    "internal-only resource on the server's behalf; the "
                    "researcher directly and intentionally called an "
                    "exposed mutation."
                ),
            },
            {
                "id": "d",
                "text": "XML external entity (XXE) injection",
                "correct": False,
                "rationale": (
                    "Incorrect. GraphQL uses JSON-based queries, not XML, "
                    "and no entity or DOCTYPE parsing is involved."
                ),
            },
        ],
        "explanation": (
            "Enforcing authentication but not authorization on a "
            "privileged mutation is broken access control (missing "
            "function-level authorization), not CSRF, SSRF, or XXE."
        ),
    },
    # ------------------------------------------------------------------ #
    # Authentication factors and protocols (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2g-019",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Authentication factors and protocols",
        "stem": (
            "A company deploys fingerprint scanners on server room doors. "
            "After employees repeatedly complain about failed scans "
            "requiring multiple attempts, the administrator lowers the "
            "sensor's minimum match-confidence threshold to make scans "
            "succeed more easily. Security shortly afterward notices a rise "
            "in successful unlocks from fingerprints that do not fully "
            "match any enrolled template. Which biometric metric increased "
            "as a direct result of this change?"
        ),
        "options": [
            {
                "id": "a",
                "text": "False acceptance rate (FAR)",
                "correct": True,
                "rationale": (
                    "Correct. Lowering the match-confidence threshold makes "
                    "the sensor more tolerant of imperfect matches, "
                    "increasing the rate at which non-matching (unauthorized) "
                    "fingerprints are incorrectly accepted — the FAR."
                ),
            },
            {
                "id": "b",
                "text": "False rejection rate (FRR)",
                "correct": False,
                "rationale": (
                    "Incorrect. FRR is the rate at which legitimate, "
                    "enrolled users are incorrectly denied; lowering the "
                    "match threshold reduces FRR (fewer failed scans for "
                    "legitimate users), it does not increase it."
                ),
            },
            {
                "id": "c",
                "text": "Crossover error rate (CER)",
                "correct": False,
                "rationale": (
                    "Incorrect. The CER is the fixed point where FAR and "
                    "FRR are equal for a given sensor and algorithm; "
                    "shifting the threshold moves the operating point away "
                    "from that point rather than raising the CER itself."
                ),
            },
            {
                "id": "d",
                "text": "Throughput rate",
                "correct": False,
                "rationale": (
                    "Incorrect. Throughput describes how many users can be "
                    "processed per unit time, unrelated to the match-"
                    "accuracy tradeoff described here."
                ),
            },
        ],
        "explanation": (
            "Loosening a biometric sensor's match threshold to reduce "
            "false rejections directly increases the false acceptance "
            "rate — the classic FAR/FRR tradeoff, not a change to the CER "
            "itself or to throughput."
        ),
    },
    {
        "id": "nd2g-020",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Authentication factors and protocols",
        "stem": (
            "An attacker who has already extracted a specific application "
            "service account's NTLM password hash forges a Kerberos service "
            "ticket (TGS) for that one application entirely offline, "
            "without ever sending a ticket-granting-ticket request or a "
            "service-ticket request to the domain controller. The forged "
            "ticket grants access only to that single service, and domain "
            "controller logs show no corresponding authentication events "
            "for the intrusion. Which attack technique was used?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Silver ticket attack",
                "correct": True,
                "rationale": (
                    "Correct. Forging a service ticket offline using a "
                    "specific service account's hash, limited to that one "
                    "service and never touching the domain controller, is "
                    "a silver ticket attack."
                ),
            },
            {
                "id": "b",
                "text": "Golden ticket attack",
                "correct": False,
                "rationale": (
                    "Incorrect. A golden ticket is forged using the krbtgt "
                    "account's hash, granting unrestricted domain-wide "
                    "access as any user to any resource — not access "
                    "limited to a single specific service."
                ),
            },
            {
                "id": "c",
                "text": "Kerberoasting",
                "correct": False,
                "rationale": (
                    "Incorrect. Kerberoasting requests legitimate TGS "
                    "tickets from the domain controller for offline "
                    "cracking, which would generate visible TGS request "
                    "events in domain controller logs — the opposite of "
                    "what is described here."
                ),
            },
            {
                "id": "d",
                "text": "Pass-the-ticket",
                "correct": False,
                "rationale": (
                    "Incorrect. Pass-the-ticket reuses a stolen, "
                    "previously issued valid ticket; this attacker forged "
                    "an entirely new ticket from a stolen hash rather than "
                    "stealing and replaying an existing one."
                ),
            },
        ],
        "explanation": (
            "Forging a service-limited ticket offline from a single "
            "service account's hash, with no domain controller interaction, "
            "is a silver ticket attack, distinct from a golden ticket, "
            "Kerberoasting, or pass-the-ticket."
        ),
    },
    # ------------------------------------------------------------------ #
    # Cryptographic attacks (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2g-021",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Cryptographic attacks",
        "stem": (
            "A researcher testing a vendor's proprietary encryption API "
            "discovers that the API will encrypt any plaintext value the "
            "researcher submits and return the resulting ciphertext. By "
            "systematically submitting a series of plaintext values of "
            "their own choosing and analyzing the resulting ciphertext "
            "patterns, the researcher deduces enough of the cipher's "
            "internal key schedule to fully break the encryption scheme. "
            "Which type of cryptographic attack does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Chosen-plaintext attack",
                "correct": True,
                "rationale": (
                    "Correct. The researcher freely chose arbitrary "
                    "plaintext values and submitted them to an active "
                    "encryption function to observe the resulting "
                    "ciphertext — the defining trait of a chosen-plaintext "
                    "attack."
                ),
            },
            {
                "id": "b",
                "text": "Known-plaintext attack",
                "correct": False,
                "rationale": (
                    "Incorrect. A known-plaintext attack relies on "
                    "plaintext/ciphertext pairs the attacker happens to "
                    "have obtained, not on the attacker's ability to freely "
                    "select and submit arbitrary plaintext of their own "
                    "choosing to an active encryption function."
                ),
            },
            {
                "id": "c",
                "text": "Birthday attack",
                "correct": False,
                "rationale": (
                    "Incorrect. A birthday attack exploits hash collision "
                    "probability, not chosen input/output pairs from an "
                    "encryption function."
                ),
            },
            {
                "id": "d",
                "text": "Downgrade attack",
                "correct": False,
                "rationale": (
                    "Incorrect. No weaker protocol or cipher was "
                    "negotiated; the full-strength cipher was analyzed "
                    "directly through its chosen-input behavior."
                ),
            },
        ],
        "explanation": (
            "Freely submitting chosen plaintext to an encryption oracle "
            "and analyzing the resulting ciphertext to break the cipher is "
            "a chosen-plaintext attack, distinct from a known-plaintext, "
            "birthday, or downgrade attack."
        ),
    },
    {
        "id": "nd2g-022",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Cryptographic attacks",
        "stem": (
            "An attacker who obtained a leaked database of password hashes "
            "runs cracking software against it using a 14-million-entry "
            "list of common passwords and their typical variations (e.g., "
            "'Summer2024!', 'Summer2024#'), recovering 40% of the passwords "
            "within an hour. The attacker never once attempted to "
            "authenticate to the live system during this process. Which "
            "type of attack was performed?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Offline dictionary attack",
                "correct": True,
                "rationale": (
                    "Correct. Running cracking software against a curated "
                    "wordlist and its variations, entirely offline against "
                    "stolen hashes, is an offline dictionary attack."
                ),
            },
            {
                "id": "b",
                "text": "Online brute-force attack",
                "correct": False,
                "rationale": (
                    "Incorrect. The attempts never contacted the live "
                    "authentication system; all guessing occurred offline "
                    "against the stolen hash file."
                ),
            },
            {
                "id": "c",
                "text": "Rainbow table attack",
                "correct": False,
                "rationale": (
                    "Incorrect. A rainbow table uses precomputed "
                    "hash-to-plaintext lookup tables rather than hashing "
                    "each wordlist entry at attack time; this attacker "
                    "actively ran cracking software against a curated "
                    "wordlist, not a precomputed table lookup."
                ),
            },
            {
                "id": "d",
                "text": "Password spraying",
                "correct": False,
                "rationale": (
                    "Incorrect. Password spraying tries one or a few common "
                    "passwords across many different accounts on a live "
                    "system to avoid lockouts; this attack tried millions "
                    "of candidate passwords offline against already-stolen "
                    "hashes."
                ),
            },
        ],
        "explanation": (
            "Running cracking software against a curated wordlist and its "
            "mutations, entirely offline against stolen hashes, is an "
            "offline dictionary attack, not brute force, a rainbow table "
            "lookup, or password spraying."
        ),
    },
    # ------------------------------------------------------------------ #
    # Indicators of malicious activity (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2g-023",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Indicators of malicious activity",
        "stem": (
            "Employees across the finance department report that no one "
            "can open any file on a shared network drive; every attempt "
            "returns an 'access denied — file in use by another process' "
            "error. No files have changed extension, no ransom note is "
            "present, and the file server's CPU and memory utilization "
            "remain within normal ranges. Which indicator of malicious "
            "activity is present?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Resource inaccessibility",
                "correct": True,
                "rationale": (
                    "Correct. Files that legitimate users can no longer "
                    "open, with no other confirmed indicator yet, describes "
                    "resource inaccessibility — a resource that is present "
                    "but unavailable for normal use."
                ),
            },
            {
                "id": "b",
                "text": "Resource consumption",
                "correct": False,
                "rationale": (
                    "Incorrect. CPU and memory usage are explicitly normal; "
                    "nothing indicates a process is consuming excessive "
                    "system resources."
                ),
            },
            {
                "id": "c",
                "text": "Concurrent session usage",
                "correct": False,
                "rationale": (
                    "Incorrect. No evidence of multiple simultaneous logins "
                    "on one account is described."
                ),
            },
            {
                "id": "d",
                "text": "Blocked content",
                "correct": False,
                "rationale": (
                    "Incorrect. Nothing indicates a security control is "
                    "actively blocking inbound or outbound content; users "
                    "simply cannot access files that appear to be locked."
                ),
            },
        ],
        "explanation": (
            "Files that exist but cannot be opened by any user, with "
            "normal CPU/memory usage and no other confirmed symptom yet, "
            "is resource inaccessibility, not resource consumption, "
            "concurrent session abuse, or blocked content."
        ),
    },
    {
        "id": "nd2g-024",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Indicators of malicious activity",
        "stem": (
            "A threat intelligence analyst finds a listing on a well-known "
            "ransomware group's dark-web leak site naming the company, "
            "displaying a countdown timer, and showing ten sample file "
            "names allegedly stolen from internal file shares. At the time "
            "the listing is discovered, the organization's EDR platform "
            "and SIEM have not generated a single related alert. Which "
            "indicator of malicious activity does the leak-site listing "
            "represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Published/documented",
                "correct": True,
                "rationale": (
                    "Correct. External evidence of a compromise — such as "
                    "a public leak-site posting — that surfaces before, or "
                    "independent of, internal detection is the "
                    "published/documented indicator category."
                ),
            },
            {
                "id": "b",
                "text": "Blocked content",
                "correct": False,
                "rationale": (
                    "Incorrect. A leak-site posting is not a record of a "
                    "security control blocking traffic."
                ),
            },
            {
                "id": "c",
                "text": "Impossible travel",
                "correct": False,
                "rationale": (
                    "Incorrect. No login location anomaly is described."
                ),
            },
            {
                "id": "d",
                "text": "Out-of-cycle logging",
                "correct": False,
                "rationale": (
                    "Incorrect. This describes activity appearing outside "
                    "a normal maintenance or logging schedule, not external "
                    "publication of stolen data on a leak site."
                ),
            },
        ],
        "explanation": (
            "Evidence of a breach appearing on a public leak site, "
            "independent of internal alerting, is the published/documented "
            "indicator category, not blocked content, impossible travel, "
            "or out-of-cycle logging."
        ),
    },
    {
        "id": "nd2g-025",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Indicators of malicious activity",
        "stem": (
            "A SOC reviews a suspected compromise and finds two facts: (1) "
            "a scheduled task was created and executed at 3:47 a.m., a time "
            "when no maintenance window is scheduled and no change ticket "
            "exists; and (2) the Windows Security event log on the same "
            "host shows a gap with zero recorded events between 3:40 a.m. "
            "and 4:10 a.m., despite the system being powered on and active "
            "per network flow logs. Which TWO indicator categories are "
            "present? (Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Out-of-cycle logging",
                "correct": True,
                "rationale": (
                    "Correct. Activity — task creation and execution — "
                    "occurring outside any approved maintenance window or "
                    "change ticket is out-of-cycle logging."
                ),
            },
            {
                "id": "b",
                "text": "Missing logs",
                "correct": True,
                "rationale": (
                    "Correct. A 30-minute gap with zero recorded events on "
                    "an active, powered-on host indicates logs were "
                    "cleared or logging was disabled — a missing logs "
                    "indicator."
                ),
            },
            {
                "id": "c",
                "text": "Impossible travel",
                "correct": False,
                "rationale": (
                    "Incorrect. No login location or geographic anomaly is "
                    "described."
                ),
            },
            {
                "id": "d",
                "text": "Concurrent session usage",
                "correct": False,
                "rationale": (
                    "Incorrect. No simultaneous active sessions on one "
                    "account are described."
                ),
            },
            {
                "id": "e",
                "text": "Blocked content",
                "correct": False,
                "rationale": (
                    "Incorrect. Neither fact describes a security control "
                    "blocking inbound or outbound content."
                ),
            },
        ],
        "explanation": (
            "An unscheduled task execution outside any approved window is "
            "out-of-cycle logging, and a 30-minute gap of zero events on an "
            "active host is missing logs — together suggesting log "
            "tampering to hide unauthorized activity, not impossible "
            "travel, concurrent sessions, or blocked content."
        ),
    },
    # ------------------------------------------------------------------ #
    # Log sources and investigative questions (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2g-026",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log sources and investigative questions",
        "stem": (
            "Investigators need to recover the full command-line arguments "
            "used to launch a malicious process that has already exited, "
            "but the host never had an EDR agent installed. Which native "
            "Windows log source is MOST likely to still contain this "
            "information, provided the appropriate audit policy was "
            "enabled beforehand?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The Security event log, specifically event ID 4688 "
                    "with command-line process auditing enabled"
                ),
                "correct": True,
                "rationale": (
                    "Correct. When command-line process auditing is "
                    "enabled via Group Policy, Windows records the full "
                    "command line for each new process in Security event "
                    "ID 4688 — a native source that persists even without "
                    "an EDR agent."
                ),
            },
            {
                "id": "b",
                "text": "The DNS client log",
                "correct": False,
                "rationale": (
                    "Incorrect. This log records name resolution activity, "
                    "not process execution details."
                ),
            },
            {
                "id": "c",
                "text": "The Windows Firewall log",
                "correct": False,
                "rationale": (
                    "Incorrect. This log records allowed/blocked network "
                    "connections by IP and port, not process command-line "
                    "arguments."
                ),
            },
            {
                "id": "d",
                "text": "The Print Service operational log",
                "correct": False,
                "rationale": (
                    "Incorrect. This log records print job activity, "
                    "unrelated to process execution."
                ),
            },
        ],
        "explanation": (
            "With command-line process auditing enabled, native Security "
            "event ID 4688 captures full process command lines without "
            "requiring an EDR agent — DNS, firewall, and print logs do not "
            "record this information."
        ),
    },
    {
        "id": "nd2g-027",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log sources and investigative questions",
        "stem": (
            "During a ransomware investigation on a compromised file "
            "server, investigators need to determine which specific file "
            "across dozens of shares was encrypted first, in order to "
            "identify the entry point and timeline of the attack. Which "
            "log source is MOST useful for this purpose?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "File and object access audit logs (e.g., Windows "
                    "Security event ID 4663) showing write/modify "
                    "timestamps per file"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Per-file object access audit logs record "
                    "exactly which account modified which file and when, "
                    "allowing investigators to reconstruct the precise "
                    "order in which files were encrypted."
                ),
            },
            {
                "id": "b",
                "text": "DHCP lease logs",
                "correct": False,
                "rationale": (
                    "Incorrect. These record IP address assignments, not "
                    "file modification activity."
                ),
            },
            {
                "id": "c",
                "text": "Switch port VLAN assignment logs",
                "correct": False,
                "rationale": (
                    "Incorrect. These record network segmentation "
                    "configuration, not file-level activity."
                ),
            },
            {
                "id": "d",
                "text": "Certificate transparency logs",
                "correct": False,
                "rationale": (
                    "Incorrect. These record public TLS certificate "
                    "issuance, unrelated to internal file server activity."
                ),
            },
        ],
        "explanation": (
            "Reconstructing the exact order files were modified requires "
            "per-file object access audit logs, not DHCP, switch "
            "configuration, or certificate transparency logs."
        ),
    },
    # ------------------------------------------------------------------ #
    # Malware types (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2g-028",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Malware types",
        "stem": (
            "A user discovers a hidden application running on their phone "
            "with no visible icon or entry in the app list. The app "
            "continuously reports the phone's GPS location, call history, "
            "and text message content to a remote server, and requires no "
            "further interaction to keep operating. The app was installed "
            "by an acquaintance who had brief physical access to the "
            "unlocked device. Which malware type is this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Spyware",
                "correct": True,
                "rationale": (
                    "Correct. Covertly and continuously monitoring and "
                    "exfiltrating a broad range of personal data — "
                    "location, calls, and messages — without the user's "
                    "knowledge is spyware."
                ),
            },
            {
                "id": "b",
                "text": "Keylogger",
                "correct": False,
                "rationale": (
                    "Incorrect. A keylogger specifically captures "
                    "keystrokes; this app reports location, call logs, and "
                    "message content broadly, a wider surveillance scope "
                    "than keystroke capture alone."
                ),
            },
            {
                "id": "c",
                "text": "Remote access trojan (RAT)",
                "correct": False,
                "rationale": (
                    "Incorrect. A RAT gives an attacker interactive, "
                    "real-time control of the device; this app passively "
                    "reports data on its own, with no indication of an "
                    "attacker actively operating the device."
                ),
            },
            {
                "id": "d",
                "text": "Adware",
                "correct": False,
                "rationale": (
                    "Incorrect. Adware generates unwanted advertisements; "
                    "this app generates no ads and instead covertly "
                    "exfiltrates personal data."
                ),
            },
        ],
        "explanation": (
            "Broad, continuous covert monitoring and exfiltration of "
            "personal data is spyware, distinct from a narrower keylogger, "
            "an interactively controlled RAT, or ad-generating adware."
        ),
    },
    {
        "id": "nd2g-029",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Malware types",
        "stem": (
            "Forensic analysis of an attack against a media company's "
            "newsroom systems shows that malware overwrote the master boot "
            "record and randomly corrupted file contents across every "
            "attached drive on dozens of workstations simultaneously. No "
            "ransom note was ever displayed, no encryption key exists to "
            "recover the data, and payment was never demanded. Which "
            "malware type BEST fits this behavior?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Wiper malware",
                "correct": True,
                "rationale": (
                    "Correct. Irreversible, destructive corruption of data "
                    "and boot records with no ransom demand and no path to "
                    "recovery is the defining trait of wiper malware."
                ),
            },
            {
                "id": "b",
                "text": "Ransomware",
                "correct": False,
                "rationale": (
                    "Incorrect. Ransomware encrypts data reversibly and "
                    "demands payment for a decryption key; here data was "
                    "destructively and irreversibly corrupted with no "
                    "ransom demand and no possibility of recovery even if "
                    "payment were offered."
                ),
            },
            {
                "id": "c",
                "text": "Logic bomb",
                "correct": False,
                "rationale": (
                    "Incorrect. A logic bomb is malicious code that lies "
                    "dormant until a specific trigger condition is met; "
                    "nothing here indicates a delayed trigger — the "
                    "destructive activity occurred directly and "
                    "simultaneously as the payload's entire purpose."
                ),
            },
            {
                "id": "d",
                "text": "Rootkit",
                "correct": False,
                "rationale": (
                    "Incorrect. A rootkit is designed to hide the presence "
                    "of malware or an attacker for stealth and persistence; "
                    "this payload's purpose was overt, immediate mass "
                    "destruction, not concealment."
                ),
            },
        ],
        "explanation": (
            "Irreversible mass data destruction with no ransom demand and "
            "no recovery path is wiper malware, not ransomware, a logic "
            "bomb, or a rootkit."
        ),
    },
    {
        "id": "nd2g-030",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Malware types",
        "stem": (
            "Forensic analysis of a compromised workstation identifies two "
            "separate hidden processes running simultaneously: Process A "
            "silently logs every keystroke typed by the user to a local "
            "encrypted file, with no observed network transmission. "
            "Process B uses idle CPU cycles to mine cryptocurrency, and "
            "automatically throttles its own CPU usage to near zero "
            "whenever Task Manager or a similar monitoring tool is opened, "
            "to avoid detection. Which TWO malware types are present on "
            "this workstation? (Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Keylogger (Process A)",
                "correct": True,
                "rationale": (
                    "Correct. A process that captures and stores every "
                    "keystroke typed by the user is a keylogger."
                ),
            },
            {
                "id": "b",
                "text": "Cryptomining malware/cryptojacking (Process B)",
                "correct": True,
                "rationale": (
                    "Correct. A process that hijacks idle CPU cycles to "
                    "mine cryptocurrency for the attacker's benefit is "
                    "cryptomining malware (cryptojacking)."
                ),
            },
            {
                "id": "c",
                "text": "Ransomware",
                "correct": False,
                "rationale": (
                    "Incorrect. No files were encrypted for ransom by "
                    "either process."
                ),
            },
            {
                "id": "d",
                "text": "Worm",
                "correct": False,
                "rationale": (
                    "Incorrect. Nothing indicates either process is "
                    "self-propagating to other hosts."
                ),
            },
            {
                "id": "e",
                "text": "Rootkit",
                "correct": False,
                "rationale": (
                    "Incorrect. While Process B evades detection by "
                    "throttling itself, this alone is not the same as a "
                    "rootkit's defining trait of subverting the OS's own "
                    "reporting mechanisms to hide files or processes "
                    "entirely — the process here remains visible, just "
                    "resource-throttled."
                ),
            },
        ],
        "explanation": (
            "A keystroke-capturing process is a keylogger and a "
            "CPU-hijacking mining process is cryptomining malware — two "
            "distinct, coexisting malware types, not ransomware, a worm, "
            "or a rootkit."
        ),
    },
    # ------------------------------------------------------------------ #
    # Network attacks (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2g-031",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Network attacks",
        "stem": (
            "An attacker on the same network segment as an established, "
            "unencrypted Telnet session between an administrator and a "
            "legacy network switch predicts the session's next valid TCP "
            "sequence number and injects a crafted packet matching that "
            "sequence number, taking over the session and issuing commands "
            "as the administrator — without ever needing the "
            "administrator's password. Which network attack was performed?"
        ),
        "options": [
            {
                "id": "a",
                "text": "TCP session hijacking (sequence number prediction)",
                "correct": True,
                "rationale": (
                    "Correct. Predicting a session's valid TCP sequence "
                    "number and injecting a matching packet to take over an "
                    "already-established session is TCP session hijacking."
                ),
            },
            {
                "id": "b",
                "text": "ARP spoofing",
                "correct": False,
                "rationale": (
                    "Incorrect. No forged ARP replies or MAC address table "
                    "manipulation is described; the attacker exploited "
                    "predictable TCP sequence numbers directly."
                ),
            },
            {
                "id": "c",
                "text": "SYN flood",
                "correct": False,
                "rationale": (
                    "Incorrect. A SYN flood exhausts connection resources "
                    "with unanswered half-open connections; here, an "
                    "already-established legitimate session was taken "
                    "over, not flooded."
                ),
            },
            {
                "id": "d",
                "text": "DNS cache poisoning",
                "correct": False,
                "rationale": (
                    "Incorrect. No DNS resolution was manipulated; the "
                    "attack targeted an active TCP session directly."
                ),
            },
        ],
        "explanation": (
            "Predicting and injecting a matching TCP sequence number into "
            "an existing session is TCP session hijacking, distinct from "
            "ARP spoofing, a SYN flood, or DNS cache poisoning."
        ),
    },
    {
        "id": "nd2g-032",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network attacks",
        "stem": (
            "A facilities employee, frustrated by weak wireless coverage in "
            "the warehouse, buys a consumer-grade access point and plugs it "
            "into an open wall jack on the corporate wired network. The "
            "device is configured with its own default manufacturer SSID, "
            "no encryption, and no security review, allowing any nearby "
            "device to connect directly to the internal network without a "
            "password. Which risk does this introduce?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A rogue access point",
                "correct": True,
                "rationale": (
                    "Correct. An unauthorized access point connected to "
                    "the wired network without security review, bypassing "
                    "normal wireless controls, is a rogue access point."
                ),
            },
            {
                "id": "b",
                "text": "An evil twin",
                "correct": False,
                "rationale": (
                    "Incorrect. An evil twin specifically impersonates the "
                    "SSID of an existing legitimate network to deceive "
                    "users into connecting; this device broadcasts its own "
                    "unrelated default SSID and was not deployed to "
                    "impersonate anything."
                ),
            },
            {
                "id": "c",
                "text": "A deauthentication attack",
                "correct": False,
                "rationale": (
                    "Incorrect. No frames were sent to forcibly disconnect "
                    "any client from a legitimate access point."
                ),
            },
            {
                "id": "d",
                "text": "Bluejacking",
                "correct": False,
                "rationale": (
                    "Incorrect. Bluejacking involves sending unsolicited "
                    "Bluetooth messages, unrelated to an unauthorized Wi-Fi "
                    "access point wired into the network."
                ),
            },
        ],
        "explanation": (
            "An unauthorized, unreviewed access point plugged into the "
            "wired network — broadcasting its own default SSID rather than "
            "impersonating an existing one — is a rogue access point, not "
            "an evil twin, deauthentication attack, or bluejacking."
        ),
    },
    {
        "id": "nd2g-033",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Network attacks",
        "stem": (
            "A workstation on a subnet begins routing all traffic destined "
            "for a partner subnet through an unauthorized host after "
            "receiving a series of forged ICMP redirect messages "
            "instructing it to use a 'better route.' At the same time, "
            "packet captures on the same segment show the legitimate "
            "gateway's IP address being mapped to two different MAC "
            "addresses that alternate every few seconds. Which TWO on-path "
            "(man-in-the-middle) techniques are being used together to "
            "position the attacker's host between the workstation and its "
            "destinations? (Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "ICMP redirect",
                "correct": True,
                "rationale": (
                    "Correct. Forged ICMP redirect messages instructing a "
                    "host to route traffic through an attacker-controlled "
                    "next hop is an ICMP redirect attack."
                ),
            },
            {
                "id": "b",
                "text": "ARP spoofing",
                "correct": True,
                "rationale": (
                    "Correct. The gateway's IP address alternating between "
                    "two different MAC addresses on the same segment "
                    "indicates forged ARP replies mapping the gateway's IP "
                    "to the attacker's MAC address."
                ),
            },
            {
                "id": "c",
                "text": "DNS cache poisoning",
                "correct": False,
                "rationale": (
                    "Incorrect. No DNS resolver response was manipulated; "
                    "both indicators target routing and address-resolution "
                    "mechanisms directly, not DNS."
                ),
            },
            {
                "id": "d",
                "text": "Rogue DHCP server",
                "correct": False,
                "rationale": (
                    "Incorrect. No anomalous DHCP lease or configuration "
                    "is described; the workstation's existing "
                    "configuration was manipulated after the fact via "
                    "ICMP and ARP, not through a malicious DHCP offer."
                ),
            },
            {
                "id": "e",
                "text": "Evil twin",
                "correct": False,
                "rationale": (
                    "Incorrect. No wireless SSID impersonation is "
                    "described; this is a wired-segment, layer 2/3 attack."
                ),
            },
        ],
        "explanation": (
            "Forged ICMP redirects manipulating the routing table and "
            "forged ARP replies manipulating the gateway's MAC mapping are "
            "being used together to position the attacker on-path, not "
            "DNS poisoning, a rogue DHCP server, or an evil twin."
        ),
    },
    # ------------------------------------------------------------------ #
    # Physical attacks (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2g-034",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Physical attacks",
        "stem": (
            "A delivery contractor carrying a large stack of boxes "
            "approaches a secure entrance just as an employee's badge "
            "unlocks the door. The employee, recognizing the contractor "
            "from previous visits, deliberately holds the door open for "
            "them without checking any credential. Investigators later "
            "determine the individual was not an approved contractor. "
            "Which physical social engineering technique BEST describes "
            "this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Piggybacking",
                "correct": True,
                "rationale": (
                    "Correct. The employee knowingly and voluntarily held "
                    "the door open for the individual — deliberate, "
                    "consenting access-sharing is piggybacking."
                ),
            },
            {
                "id": "b",
                "text": "Tailgating",
                "correct": False,
                "rationale": (
                    "Incorrect. Tailgating occurs when an unauthorized "
                    "person follows an authorized person through a secured "
                    "door without that person's knowledge or consent; here "
                    "the employee knowingly held the door, which is "
                    "piggybacking."
                ),
            },
            {
                "id": "c",
                "text": "Shoulder surfing",
                "correct": False,
                "rationale": (
                    "Incorrect. No observation of credentials or PIN entry "
                    "is described."
                ),
            },
            {
                "id": "d",
                "text": "Dumpster diving",
                "correct": False,
                "rationale": (
                    "Incorrect. No searching through discarded materials "
                    "is described."
                ),
            },
        ],
        "explanation": (
            "An employee knowingly holding the door open for someone "
            "without checking credentials is piggybacking (consenting), "
            "distinct from tailgating (unaware), shoulder surfing, or "
            "dumpster diving."
        ),
    },
    {
        "id": "nd2g-035",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Physical attacks",
        "stem": (
            "An individual with brief, unmonitored physical access to a "
            "network closet disables the trigger mechanism on the room's "
            "clean-agent fire suppression system. Weeks later, a small "
            "electrical fire breaks out in the same closet, and because "
            "the suppression system never activates, the fire causes "
            "extensive damage to networking equipment that the system "
            "should have prevented. Which category of physical attack does "
            "the initial tampering represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Environmental attack (tampering with facility "
                    "environmental/safety controls)"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Deliberately disabling a facility's fire "
                    "suppression system to allow later physical damage is "
                    "an environmental attack against building safety "
                    "controls."
                ),
            },
            {
                "id": "b",
                "text": "Tailgating",
                "correct": False,
                "rationale": (
                    "Incorrect. No following someone through a secured "
                    "door is described; the individual already had access "
                    "and tampered with a system."
                ),
            },
            {
                "id": "c",
                "text": "RFID cloning",
                "correct": False,
                "rationale": (
                    "Incorrect. No access card was cloned; the individual "
                    "already had physical access."
                ),
            },
            {
                "id": "d",
                "text": "Brute-force entry",
                "correct": False,
                "rationale": (
                    "Incorrect. No forced entry through a lock or barrier "
                    "is described; the individual already had access and "
                    "tampered with an environmental control system."
                ),
            },
        ],
        "explanation": (
            "Disabling a fire suppression system to enable later physical "
            "damage is an environmental attack on facility safety "
            "controls, not tailgating, RFID cloning, or brute-force entry."
        ),
    },
    # ------------------------------------------------------------------ #
    # Hardening (2.5)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2g-036",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Hardening",
        "stem": (
            "A physical security audit of a branch office wiring closet "
            "finds that 30 of the switch's 48 ports have no device "
            "connected, yet remain administratively enabled, assigned to "
            "the same VLAN as production workstations, and have no port "
            "security or 802.1X authentication configured. Which "
            "hardening action would BEST reduce the risk this "
            "configuration presents?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Administratively disable unused switch ports and "
                    "enable port security/802.1X authentication on active "
                    "ports"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Disabling unused ports and requiring "
                    "authentication on active ones directly closes off the "
                    "unattended, unauthenticated physical network access "
                    "this configuration creates."
                ),
            },
            {
                "id": "b",
                "text": "Increase the VLAN's DHCP lease duration",
                "correct": False,
                "rationale": (
                    "Incorrect. Lease duration has no bearing on whether "
                    "an unauthorized device plugged into an open port can "
                    "reach the network."
                ),
            },
            {
                "id": "c",
                "text": "Enable SNMP monitoring on the switch",
                "correct": False,
                "rationale": (
                    "Incorrect. Monitoring can help detect a connection "
                    "after the fact but does not itself reduce the attack "
                    "surface created by open, unauthenticated ports."
                ),
            },
            {
                "id": "d",
                "text": "Upgrade the switch's firmware to the latest version",
                "correct": False,
                "rationale": (
                    "Incorrect. Firmware currency addresses known software "
                    "vulnerabilities, not the specific exposure created by "
                    "unused, unrestricted physical ports."
                ),
            },
        ],
        "explanation": (
            "Disabling unused ports and enforcing port-level "
            "authentication removes the open physical attack surface "
            "directly; DHCP lease timing, SNMP monitoring, and firmware "
            "updates do not address this specific exposure."
        ),
    },
    {
        "id": "nd2g-037",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Hardening",
        "stem": (
            "A vulnerability assessment of a newly commissioned SQL "
            "database server finds the default administrative 'sa' "
            "account still enabled with a blank password, along with a "
            "bundled sample demonstration database that ships with the "
            "product by default. Which action represents the BEST "
            "hardening response?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Disable or rename the default administrative account, "
                    "enforce a strong password, and remove the unused "
                    "sample database and any other default features"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Removing default accounts, enforcing strong "
                    "authentication, and eliminating unnecessary bundled "
                    "features directly closes off the unauthenticated "
                    "access and unneeded attack surface this server "
                    "presents."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Enable transparent data encryption for the sample "
                    "database only"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Encrypting data at rest does nothing to "
                    "close off the unauthenticated, blank-password default "
                    "account, which remains the primary exposure."
                ),
            },
            {
                "id": "c",
                "text": "Configure the database to allow connections only over TLS",
                "correct": False,
                "rationale": (
                    "Incorrect. Encrypting the connection in transit does "
                    "not address a blank-password administrative account "
                    "that can still authenticate over that encrypted "
                    "channel."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Schedule more frequent vulnerability scans of the "
                    "database server"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Increasing scan frequency improves "
                    "detection cadence but does not itself remediate the "
                    "exposed default account and unnecessary sample data."
                ),
            },
        ],
        "explanation": (
            "Removing or securing default accounts and eliminating "
            "bundled sample data/features is the direct hardening fix; "
            "encryption at rest, encryption in transit, and more frequent "
            "scanning each address a different concern without closing "
            "off the blank-password default account."
        ),
    },
    # ------------------------------------------------------------------ #
    # Mitigation techniques (2.5)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2g-038",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mitigation techniques",
        "stem": (
            "After a previous breach went undetected for several months, a "
            "security team deploys a set of decoy file shares and fake "
            "privileged-looking service accounts throughout the internal "
            "network. These decoys serve no legitimate business purpose "
            "and are configured to generate an immediate, high-priority "
            "alert the instant any account interacts with them. Which "
            "mitigation technique has the team implemented?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Deception technology (honeypots/honeytokens)",
                "correct": True,
                "rationale": (
                    "Correct. Decoy resources with no legitimate purpose, "
                    "deployed specifically to lure and generate an alert "
                    "on unauthorized interaction, is deception technology "
                    "— honeypots and honeytokens."
                ),
            },
            {
                "id": "b",
                "text": "Network segmentation",
                "correct": False,
                "rationale": (
                    "Incorrect. No network boundaries or access-control "
                    "zones were created; decoy assets were placed to lure "
                    "and detect attacker interaction."
                ),
            },
            {
                "id": "c",
                "text": "Least privilege",
                "correct": False,
                "rationale": (
                    "Incorrect. No changes were made to legitimate "
                    "accounts' actual permission levels."
                ),
            },
            {
                "id": "d",
                "text": "Patch management",
                "correct": False,
                "rationale": (
                    "Incorrect. No software vulnerabilities were "
                    "remediated; this technique focuses on early detection "
                    "of an attacker already inside the network."
                ),
            },
        ],
        "explanation": (
            "Deploying decoy shares and accounts to lure and detect "
            "attacker interaction is deception technology, not network "
            "segmentation, least privilege, or patch management."
        ),
    },
    {
        "id": "nd2g-039",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mitigation techniques",
        "stem": (
            "A courier transporting a box of backup tapes between two data "
            "centers loses the box in transit. The tapes contained a full, "
            "unencrypted database backup including customer Social "
            "Security numbers. Which mitigation would have MOST reduced "
            "the impact of this incident?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Encrypting backup data at rest before it leaves the "
                    "data center"
                ),
                "correct": True,
                "rationale": (
                    "Correct. If the backup data had been encrypted before "
                    "leaving the facility, the lost tapes would not have "
                    "exposed readable customer data, directly reducing the "
                    "impact of the loss."
                ),
            },
            {
                "id": "b",
                "text": "Increasing the frequency of backup jobs",
                "correct": False,
                "rationale": (
                    "Incorrect. More frequent backups would only create "
                    "more unencrypted copies at risk, without addressing "
                    "the actual exposure of sensitive data in transit."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Requiring multifactor authentication for backup "
                    "system administrators"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. MFA protects against unauthorized login to "
                    "the backup system; it does nothing to protect data "
                    "already extracted onto physical, unencrypted tape "
                    "media that was physically lost."
                ),
            },
            {
                "id": "d",
                "text": "Implementing a longer backup retention period",
                "correct": False,
                "rationale": (
                    "Incorrect. Retention period governs how long backups "
                    "are kept, not whether their contents are protected if "
                    "the physical media is lost."
                ),
            },
        ],
        "explanation": (
            "Encrypting backup data at rest before it ever leaves the "
            "facility is the mitigation that directly neutralizes the "
            "impact of lost physical media; backup frequency, "
            "administrator MFA, and retention period do not."
        ),
    },
]

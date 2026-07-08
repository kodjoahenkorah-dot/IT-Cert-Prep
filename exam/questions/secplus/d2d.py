"""Security+ SY0-701 practice questions — Domain 2 (Threats, Vulnerabilities,
and Mitigations), batch D.

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
        "id": "nd2d-001",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Threat actors",
        "stem": (
            "A dark-web forum post offers a set of verified, working VPN credentials "
            "for a mid-sized manufacturer, along with a network diagram, to the highest "
            "bidder. The seller states they have no interest in using the access "
            "themselves and will not deal with buyers who cannot pay in "
            "cryptocurrency within 24 hours. Which threat actor BEST describes the "
            "seller?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Organized crime (initial access broker)",
                "correct": True,
                "rationale": (
                    "Correct. Monetizing stolen access by auctioning it to the "
                    "highest-paying buyer, with no ideological or espionage motive and "
                    "a clear demand for fast cryptocurrency payment, is the signature "
                    "of a financially driven organized-crime access broker."
                ),
            },
            {
                "id": "b",
                "text": "Nation-state actor",
                "correct": False,
                "rationale": (
                    "Incorrect. A nation-state actor pursuing this target would exploit "
                    "the access directly for intelligence or sabotage, not auction it "
                    "publicly to an anonymous buyer for cash."
                ),
            },
            {
                "id": "c",
                "text": "Hacktivist",
                "correct": False,
                "rationale": (
                    "Incorrect. Hacktivists act on ideological grievances and typically "
                    "publicize or use access to make a statement, not sell it quietly "
                    "for profit."
                ),
            },
            {
                "id": "d",
                "text": "Unskilled attacker (script kiddie)",
                "correct": False,
                "rationale": (
                    "Incorrect. Obtaining verified working credentials and a network "
                    "diagram, then operating a structured sales process, reflects "
                    "organized capability far beyond a low-skill opportunist."
                ),
            },
        ],
        "explanation": (
            "Selling verified access to the highest cryptocurrency-paying bidder, with "
            "no interest in using it personally, is the profit-driven pattern of an "
            "organized-crime initial access broker rather than a state, ideological, "
            "or low-skill actor."
        ),
    },
    {
        "id": "nd2d-002",
        "domain": 2,
        "objective": "2.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Threat actors",
        "stem": (
            "During a period of heightened diplomatic tension between two countries, "
            "a power-grid operator's SCADA historian servers are wiped by malware that "
            "used a previously unknown zero-day exploit and left no ransom note or "
            "data-theft evidence — only destroyed configuration data timed to trigger "
            "during a national holiday. Which threat actor is MOST likely responsible?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Nation-state actor",
                "correct": True,
                "rationale": (
                    "Correct. A zero-day exploit, precise timing tied to a geopolitical "
                    "event, and a destructive (sabotage) rather than financial or "
                    "attention-seeking goal are consistent with a well-funded, "
                    "state-sponsored operation against critical infrastructure."
                ),
            },
            {
                "id": "b",
                "text": "Organized crime group",
                "correct": False,
                "rationale": (
                    "Incorrect. Organized crime seeks monetary gain, typically through "
                    "ransom or data resale; pure destruction with no extortion attempt "
                    "does not fit a profit motive."
                ),
            },
            {
                "id": "c",
                "text": "Hacktivist",
                "correct": False,
                "rationale": (
                    "Incorrect. Hacktivists usually claim credit publicly to advance a "
                    "cause; a silent, precisely timed zero-day sabotage operation "
                    "against grid infrastructure exceeds typical hacktivist tooling and "
                    "lacks any public statement."
                ),
            },
            {
                "id": "d",
                "text": "Insider threat",
                "correct": False,
                "rationale": (
                    "Incorrect. Nothing here points to a current or former employee; a "
                    "zero-day exploit against SCADA historians is an external, "
                    "highly resourced technical capability."
                ),
            },
        ],
        "explanation": (
            "Zero-day tooling, geopolitical timing, and destructive sabotage without "
            "any financial or publicity motive are the classic fingerprints of a "
            "nation-state actor targeting critical infrastructure."
        ),
    },
    # ------------------------------------------------------------------ #
    # Threat vectors and attack surfaces (2.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2d-003",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Threat vectors and attack surfaces",
        "stem": (
            "An attacker's reconnaissance scripts specifically search the internet for "
            "print servers still running an operating system version that reached "
            "end-of-life three major releases ago, because the vendor has confirmed no "
            "future patches will ever be released for it, regardless of severity. "
            "Which attack vector is being deliberately targeted?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Unsupported systems and applications",
                "correct": True,
                "rationale": (
                    "Correct. Deliberately hunting for software the vendor will never "
                    "patch again targets the permanent, unfixable attack surface "
                    "created by running unsupported/end-of-life systems."
                ),
            },
            {
                "id": "b",
                "text": "Default credentials",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario describes targeting outdated, unpatchable "
                    "software versions, not devices left with vendor-set default "
                    "usernames and passwords."
                ),
            },
            {
                "id": "c",
                "text": "Removable media",
                "correct": False,
                "rationale": (
                    "Incorrect. No physical media (USB drives, external disks) is "
                    "involved; this is a remote, internet-facing software targeting "
                    "campaign."
                ),
            },
            {
                "id": "d",
                "text": "Supply chain compromise",
                "correct": False,
                "rationale": (
                    "Incorrect. A supply-chain attack subverts a trusted vendor's "
                    "software or update process before it reaches the victim; here the "
                    "attacker is simply exploiting software the victim never updated, "
                    "not a tampered vendor delivery."
                ),
            },
        ],
        "explanation": (
            "Software that a vendor has confirmed will never be patched again "
            "represents a permanent unsupported-systems-and-applications attack "
            "surface, which is exactly what the reconnaissance is targeting."
        ),
    },
    {
        "id": "nd2d-004",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Threat vectors and attack surfaces",
        "stem": (
            "An internet-wide scanning service identifies a cloud-hosted server with "
            "its in-memory database management port reachable from any address with no "
            "authentication configured. An attacker connects directly to that port and "
            "writes a malicious cron-job entry into the database's configuration to "
            "obtain a shell on the underlying host. Which attack vector was exploited "
            "to gain the initial foothold?"
        ),
        "options": [
            {
                "id": "a",
                "text": "An open, unauthenticated network service/port",
                "correct": True,
                "rationale": (
                    "Correct. A management service exposed to the entire internet with "
                    "no authentication is an open-port/unsecured-service attack vector; "
                    "the attacker connected directly to it without needing to bypass "
                    "any credential."
                ),
            },
            {
                "id": "b",
                "text": "Removable device",
                "correct": False,
                "rationale": (
                    "Incorrect. No physical media was involved; the attacker connected "
                    "remotely over the network to an exposed service."
                ),
            },
            {
                "id": "c",
                "text": "Message-based vector",
                "correct": False,
                "rationale": (
                    "Incorrect. No email, SMS, or chat message was used to deliver a "
                    "malicious link or attachment; the compromise occurred through "
                    "direct network access to an exposed port."
                ),
            },
            {
                "id": "d",
                "text": "Image-based vector",
                "correct": False,
                "rationale": (
                    "Incorrect. No malicious image file or steganographic payload is "
                    "described; the attacker interacted directly with an exposed "
                    "database service."
                ),
            },
        ],
        "explanation": (
            "An unauthenticated management port reachable from the entire internet is "
            "a classic open-service attack vector, allowing direct interaction with no "
            "credential bypass required."
        ),
    },
    {
        "id": "nd2d-005",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Threat vectors and attack surfaces",
        "stem": (
            "A breach timeline reconstruction shows the following sequence: (1) an "
            "employee received an email containing a link to a fake \"invoice viewer\" "
            "site; (2) clicking the link caused the browser to silently trigger a flaw "
            "in a PDF-rendering browser extension that had not been updated in two "
            "years; (3) the resulting code execution gave the attacker an initial "
            "foothold used for lateral movement. Which TWO attack vectors were "
            "exploited to gain that foothold? (Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Message-based vector",
                "correct": True,
                "rationale": (
                    "Correct. The email delivering the malicious link is a "
                    "message-based vector — the initial delivery mechanism that got "
                    "the victim to click."
                ),
            },
            {
                "id": "b",
                "text": "Vulnerable software",
                "correct": True,
                "rationale": (
                    "Correct. The two-year-unpatched PDF-rendering browser extension "
                    "is the vulnerable-software vector that the visited page actually "
                    "exploited to execute code."
                ),
            },
            {
                "id": "c",
                "text": "Removable device",
                "correct": False,
                "rationale": (
                    "Incorrect. No USB drive or other physical removable media appears "
                    "anywhere in this timeline."
                ),
            },
            {
                "id": "d",
                "text": "Supply chain compromise",
                "correct": False,
                "rationale": (
                    "Incorrect. No vendor update mechanism or third-party software "
                    "delivery pipeline was subverted; the extension was simply left "
                    "unpatched by the end user, not tampered with by its vendor."
                ),
            },
            {
                "id": "e",
                "text": "Default credentials",
                "correct": False,
                "rationale": (
                    "Incorrect. No login or factory-set password was involved at any "
                    "step of this compromise."
                ),
            },
        ],
        "explanation": (
            "The email link is the message-based delivery vector, and the outdated "
            "browser extension it silently exploited is the vulnerable-software "
            "vector; no removable media, supply chain, or credential issue is "
            "described."
        ),
    },
    # ------------------------------------------------------------------ #
    # Social engineering (2.2)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2d-006",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Social engineering",
        "stem": (
            "An attacker poses as a technical recruiter on a professional networking "
            "site and, over several weeks, conducts a convincing multi-round "
            "\"interview process\" with an employee, culminating in a final take-home "
            "coding assessment that instructs the candidate to clone a private "
            "repository and run its setup script on their corporate laptop. The script "
            "installs a backdoor. Which social engineering technique BEST describes "
            "the attacker's approach?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Pretexting",
                "correct": True,
                "rationale": (
                    "Correct. Fabricating an entire false scenario — a recruiter and a "
                    "legitimate-seeming multi-week hiring process — to build trust "
                    "before asking the target to run untrusted code is a textbook "
                    "long-form pretexting operation."
                ),
            },
            {
                "id": "b",
                "text": "Typosquatting",
                "correct": False,
                "rationale": (
                    "Incorrect. Typosquatting relies on a misspelled or lookalike "
                    "domain to trick users who mistype a URL; no such domain confusion "
                    "is described here."
                ),
            },
            {
                "id": "c",
                "text": "Watering hole attack",
                "correct": False,
                "rationale": (
                    "Incorrect. A watering hole attack compromises a website the "
                    "victims already visit and waits for them to arrive; this attacker "
                    "actively built a personal, fabricated relationship with one target."
                ),
            },
            {
                "id": "d",
                "text": "Tailgating",
                "correct": False,
                "rationale": (
                    "Incorrect. Tailgating is a physical-access technique of following "
                    "someone through a secured door; this attack is entirely remote and "
                    "social/digital."
                ),
            },
        ],
        "explanation": (
            "A fabricated, drawn-out recruiter/interview scenario built specifically "
            "to earn trust before asking the victim to execute code is a long-con "
            "pretexting attack, distinct from domain-spoofing, compromised-website, or "
            "physical-access techniques."
        ),
    },
    {
        "id": "nd2d-007",
        "domain": 2,
        "objective": "2.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Social engineering",
        "stem": (
            "An attacker cold-calls dozens of employees at a company offering free "
            "\"PC performance tuning.\" Most hang up, but a few days later, one "
            "employee whose laptop has genuinely been running slowly calls the same "
            "number back asking for help. The caller remotely connects, appears to fix "
            "the issue, and in the process installs a remote access tool. Which social "
            "engineering technique BEST describes this attack?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Quid pro quo",
                "correct": True,
                "rationale": (
                    "Correct. The attacker offers a service (\"free tuning\") in "
                    "exchange for the victim initiating contact and granting remote "
                    "access — an even trade of a favor for access — which defines a "
                    "quid pro quo attack."
                ),
            },
            {
                "id": "b",
                "text": "Baiting",
                "correct": False,
                "rationale": (
                    "Incorrect. Baiting lures a victim with a tempting physical or "
                    "digital object (like an infected USB drive left in the open) that "
                    "the victim retrieves and uses on their own; no such planted object "
                    "is involved here."
                ),
            },
            {
                "id": "c",
                "text": "Watering hole attack",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no compromised website that the targets "
                    "routinely visit; the attacker made direct outbound phone calls."
                ),
            },
            {
                "id": "d",
                "text": "Whaling",
                "correct": False,
                "rationale": (
                    "Incorrect. Whaling specifically targets senior executives with "
                    "highly tailored attacks; this is an untargeted, mass cold-calling "
                    "campaign aimed at any employee."
                ),
            },
        ],
        "explanation": (
            "Offering a favor (free tech support) to entice the victim to voluntarily "
            "make contact and grant access in return is the defining exchange of a "
            "quid pro quo social engineering attack."
        ),
    },
    # ------------------------------------------------------------------ #
    # Application vulnerabilities (2.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2d-008",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Application vulnerabilities",
        "stem": (
            "Endpoint forensics show that a malicious DLL was written into a temp "
            "folder and then loaded directly into the address space of an already-"
            "running, trusted process (explorer.exe) using a documented Windows API "
            "call, rather than being launched as its own separate executable. The "
            "malicious code then executed under that trusted process's identity, "
            "evading a security tool that only inspects newly launched processes. "
            "Which vulnerability class does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Memory injection",
                "correct": True,
                "rationale": (
                    "Correct. Loading malicious code directly into the memory space of "
                    "an already-running, trusted process to execute under its identity "
                    "and evade process-based detection is the defining behavior of "
                    "memory injection."
                ),
            },
            {
                "id": "b",
                "text": "Buffer overflow",
                "correct": False,
                "rationale": (
                    "Incorrect. A buffer overflow overruns a fixed-size memory "
                    "allocation with oversized input; this scenario describes "
                    "deliberately loading code into another process's address space "
                    "via a supported API, not overrunning a buffer."
                ),
            },
            {
                "id": "c",
                "text": "Race condition (TOCTOU)",
                "correct": False,
                "rationale": (
                    "Incorrect. A TOCTOU flaw exploits a timing gap between checking "
                    "and using a resource; nothing here involves a check-then-use "
                    "timing window."
                ),
            },
            {
                "id": "d",
                "text": "Insecure deserialization",
                "correct": False,
                "rationale": (
                    "Incorrect. Deserialization flaws involve reconstructing objects "
                    "from untrusted serialized data; this attack injects executable "
                    "code directly into a running process's memory instead."
                ),
            },
        ],
        "explanation": (
            "Injecting code into the memory space of a legitimate, already-running "
            "process so it executes under that process's trusted identity is the "
            "textbook definition of memory injection, distinct from overflow, race "
            "condition, or deserialization flaws."
        ),
    },
    {
        "id": "nd2d-009",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Application vulnerabilities",
        "stem": (
            "A widely used log-analysis agent auto-updates itself nightly from its "
            "vendor's distribution servers. Investigators later determine the vendor's "
            "code-signing key was stolen and used to sign a trojanized build that was "
            "pushed through the normal update channel, silently creating backdoor "
            "accounts on roughly 4,000 customer servers overnight. Which application "
            "vulnerability class does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Malicious update",
                "correct": True,
                "rationale": (
                    "Correct. A legitimately signed but attacker-modified update "
                    "delivered through the software's own trusted update mechanism is "
                    "the defining pattern of a malicious update vulnerability."
                ),
            },
            {
                "id": "b",
                "text": "Buffer overflow",
                "correct": False,
                "rationale": (
                    "Incorrect. No oversized input overrunning a memory buffer is "
                    "described; the compromise occurred through a tampered, "
                    "properly-signed software update, not an input-length flaw."
                ),
            },
            {
                "id": "c",
                "text": "Insecure deserialization",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no evidence of the agent reconstructing "
                    "attacker-controlled serialized objects; the payload arrived via "
                    "the standard auto-update process."
                ),
            },
            {
                "id": "d",
                "text": "Resource exhaustion",
                "correct": False,
                "rationale": (
                    "Incorrect. Nothing describes degraded performance or availability "
                    "from excessive resource consumption; the impact here is "
                    "unauthorized backdoor accounts, not a denial of service."
                ),
            },
        ],
        "explanation": (
            "A stolen signing key used to push a trojanized build through the "
            "software's own legitimate auto-update mechanism is the hallmark of a "
            "malicious update vulnerability, distinct from overflow, deserialization, "
            "or resource-exhaustion flaws."
        ),
    },
    {
        "id": "nd2d-010",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Application vulnerabilities",
        "stem": (
            "A web application's \"search filter\" feature lets users supply a custom "
            "regular expression. A tester submits a pattern containing deeply nested, "
            "overlapping quantifiers; the worker thread handling that single request "
            "pins one CPU core at 100% for over ten minutes trying to evaluate every "
            "possible match combination, making the application unresponsive to new "
            "requests on that worker. Which vulnerability does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Resource exhaustion (catastrophic regex backtracking)",
                "correct": True,
                "rationale": (
                    "Correct. A specially crafted pattern that forces exponential "
                    "backtracking on the regex engine, consuming CPU until the "
                    "application can no longer serve requests, is a classic algorithmic-"
                    "complexity resource exhaustion (ReDoS) vulnerability."
                ),
            },
            {
                "id": "b",
                "text": "Buffer overflow",
                "correct": False,
                "rationale": (
                    "Incorrect. No memory buffer is overrun or return address "
                    "corrupted; the impact is CPU consumption from algorithmic "
                    "complexity, not an out-of-bounds memory write."
                ),
            },
            {
                "id": "c",
                "text": "Race condition (TOCTOU)",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no check-then-use timing gap between two "
                    "operations on a shared resource; a single request's regex "
                    "evaluation is causing the slowdown."
                ),
            },
            {
                "id": "d",
                "text": "Memory injection",
                "correct": False,
                "rationale": (
                    "Incorrect. No code is being loaded into another process's address "
                    "space; the regex engine is simply consuming excessive CPU "
                    "evaluating the submitted pattern."
                ),
            },
        ],
        "explanation": (
            "A crafted input that drives an algorithm into exponential-time behavior, "
            "exhausting CPU and denying service to other requests, is a resource "
            "exhaustion vulnerability (specifically catastrophic regex backtracking), "
            "not a memory-corruption, timing, or injection flaw."
        ),
    },
    # ------------------------------------------------------------------ #
    # Web application vulnerabilities (2.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2d-011",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Web application vulnerabilities",
        "stem": (
            "A company's login flow accepts a \"redirect\" query parameter and, after "
            "successful authentication, forwards the browser to whatever URL that "
            "parameter contains, without validating it against a list of internal "
            "destinations. An attacker emails employees a link that points to the "
            "real, trusted login domain but sets the redirect parameter to an "
            "attacker-controlled site that mimics the post-login dashboard and "
            "harvests re-entered credentials. Which vulnerability made this possible?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Open redirect",
                "correct": True,
                "rationale": (
                    "Correct. Forwarding users to an arbitrary, attacker-supplied "
                    "destination after a legitimate step — with no validation against "
                    "an allow-list — is exactly what an open redirect vulnerability "
                    "enables, letting attackers hide malicious destinations behind a "
                    "trusted domain."
                ),
            },
            {
                "id": "b",
                "text": "Cross-site request forgery (CSRF)",
                "correct": False,
                "rationale": (
                    "Incorrect. CSRF forces a victim's browser to submit an unwanted "
                    "state-changing request using their existing session; this attack "
                    "instead abuses a redirect parameter to send the victim to a "
                    "phishing page, with no forged request submitted."
                ),
            },
            {
                "id": "c",
                "text": "Reflected cross-site scripting (XSS)",
                "correct": False,
                "rationale": (
                    "Incorrect. No script payload is being reflected and executed in "
                    "the victim's browser; the attack relies purely on an unvalidated "
                    "destination URL."
                ),
            },
            {
                "id": "d",
                "text": "Server-side request forgery (SSRF)",
                "correct": False,
                "rationale": (
                    "Incorrect. SSRF tricks the server itself into making an "
                    "unauthorized request; here it is the victim's own browser being "
                    "redirected, not the server issuing a request on the attacker's "
                    "behalf."
                ),
            },
        ],
        "explanation": (
            "An unvalidated redirect parameter that forwards authenticated users to "
            "any attacker-chosen destination — abused to disguise a phishing page "
            "behind a trusted login domain — is an open redirect vulnerability, "
            "distinct from CSRF, XSS, or SSRF."
        ),
    },
    {
        "id": "nd2d-012",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Web application vulnerabilities",
        "stem": (
            "A tester builds a webpage containing a large, eye-catching \"Claim your "
            "prize\" button. Positioned directly beneath it, at zero opacity, is an "
            "invisible iframe loading a logged-in victim's banking site, precisely "
            "aligned so the victim's click on the visible button actually lands on the "
            "banking site's \"Enable international transfers\" toggle. Which attack "
            "does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Clickjacking (UI redress attack)",
                "correct": True,
                "rationale": (
                    "Correct. Overlaying an invisible, functional element from another "
                    "site beneath a decoy button so the victim's click is silently "
                    "redirected to perform an unintended action is the defining "
                    "technique of clickjacking."
                ),
            },
            {
                "id": "b",
                "text": "Cross-site request forgery (CSRF)",
                "correct": False,
                "rationale": (
                    "Incorrect. CSRF forges a request without requiring the victim to "
                    "visually interact with the target site's real interface at all; "
                    "here the victim is tricked into directly clicking the genuine, "
                    "rendered banking control hidden beneath a decoy."
                ),
            },
            {
                "id": "c",
                "text": "Reflected cross-site scripting (XSS)",
                "correct": False,
                "rationale": (
                    "Incorrect. No injected script is reflected back and executed in "
                    "the browser; the attack relies purely on visual layering of a "
                    "legitimate page, not script injection."
                ),
            },
            {
                "id": "d",
                "text": "Session fixation",
                "correct": False,
                "rationale": (
                    "Incorrect. Session fixation forces a victim to use a "
                    "known/attacker-supplied session identifier; nothing here involves "
                    "manipulating the victim's session ID."
                ),
            },
        ],
        "explanation": (
            "Layering an invisible, fully functional iframe from a trusted site "
            "beneath a decoy button so a victim's genuine click is hijacked to perform "
            "an unintended action on the real site is the definition of clickjacking, "
            "distinct from CSRF, XSS, or session fixation."
        ),
    },
    # ------------------------------------------------------------------ #
    # Mobile vulnerabilities (2.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2d-013",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile vulnerabilities",
        "stem": (
            "A mobile device management console shows that a corporate Android "
            "device's \"Install unknown apps\" permission was enabled for a messaging "
            "app, and shortly afterward an APK was installed directly from a link in a "
            "chat message, entirely outside the organization's managed app store. The "
            "app subsequently exfiltrates the device's contact list. Which mobile "
            "vulnerability does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Sideloading",
                "correct": True,
                "rationale": (
                    "Correct. Installing an application from a source outside the "
                    "official/managed app store, enabled by granting an app permission "
                    "to install unknown packages, is the definition of sideloading."
                ),
            },
            {
                "id": "b",
                "text": "Jailbreaking",
                "correct": False,
                "rationale": (
                    "Incorrect. Jailbreaking (or rooting) removes the OS vendor's "
                    "built-in restrictions at a system level; this scenario describes "
                    "installing an app through a permitted, unmanaged-store "
                    "installation path, not defeating OS-level protections."
                ),
            },
            {
                "id": "c",
                "text": "SIM swapping",
                "correct": False,
                "rationale": (
                    "Incorrect. SIM swapping involves an attacker fraudulently "
                    "porting a victim's phone number to a new SIM; no carrier or phone "
                    "number takeover is described here."
                ),
            },
            {
                "id": "d",
                "text": "Bluesnarfing",
                "correct": False,
                "rationale": (
                    "Incorrect. Bluesnarfing steals data over an unauthorized "
                    "Bluetooth connection; this compromise occurred through a locally "
                    "installed application obtained via a chat link, not Bluetooth."
                ),
            },
        ],
        "explanation": (
            "Installing an app from outside the managed app store after enabling the "
            "\"unknown sources\" permission is sideloading, distinct from jailbreaking, "
            "SIM swapping, or Bluetooth-based attacks."
        ),
    },
    {
        "id": "nd2d-014",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile vulnerabilities",
        "stem": (
            "A traveler plugs a personal phone into a public USB charging kiosk at an "
            "airport gate to top up the battery. Shortly after, unfamiliar "
            "applications appear on the device and previously stored photos begin "
            "syncing to an unknown cloud account. Which mobile attack MOST likely "
            "occurred?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Juice jacking",
                "correct": True,
                "rationale": (
                    "Correct. A public USB charging port that carries data lines as "
                    "well as power can be used to install malware or exfiltrate data "
                    "when a device is plugged in for charging — the defining risk of "
                    "juice jacking."
                ),
            },
            {
                "id": "b",
                "text": "SIM swapping",
                "correct": False,
                "rationale": (
                    "Incorrect. SIM swapping requires the attacker to socially "
                    "engineer a carrier into porting the victim's number to a new SIM; "
                    "no phone number takeover or loss of cellular service is described."
                ),
            },
            {
                "id": "c",
                "text": "Bluesnarfing",
                "correct": False,
                "rationale": (
                    "Incorrect. Bluesnarfing exploits an unsecured Bluetooth "
                    "connection; the compromise here occurred through a wired USB "
                    "charging connection, not a wireless Bluetooth link."
                ),
            },
            {
                "id": "d",
                "text": "Sideloading",
                "correct": False,
                "rationale": (
                    "Incorrect. Sideloading requires the user to knowingly install an "
                    "app from an unofficial source; here, malicious activity occurred "
                    "automatically through the physical charging connection itself."
                ),
            },
        ],
        "explanation": (
            "A compromised public USB charging port that abuses the data pins to "
            "install malware or exfiltrate data while a device charges is the defining "
            "scenario of juice jacking, not SIM swapping, Bluesnarfing, or sideloading."
        ),
    },
    # ------------------------------------------------------------------ #
    # Virtualization vulnerabilities (2.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2d-015",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Virtualization vulnerabilities",
        "stem": (
            "Researchers demonstrate that a process running inside one tenant's VM can "
            "infer bytes of a cryptographic key being used by a completely separate "
            "tenant's VM on the same physical host, purely by repeatedly measuring how "
            "long it takes to access shared CPU cache lines while the victim VM "
            "performs decryption — without ever executing code inside the victim VM or "
            "crossing the hypervisor's memory-isolation boundary. Which virtualization "
            "vulnerability does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Side-channel (cache-timing) attack across co-resident VMs",
                "correct": True,
                "rationale": (
                    "Correct. Inferring secret data by measuring timing variations in "
                    "a physically shared resource (CPU cache), without breaching the "
                    "hypervisor's isolation boundary or executing code in the victim "
                    "VM, is the hallmark of a cross-tenant side-channel attack."
                ),
            },
            {
                "id": "b",
                "text": "VM escape",
                "correct": False,
                "rationale": (
                    "Incorrect. VM escape requires code executing inside the victim's "
                    "VM boundary or hypervisor to break out of isolation; here, the "
                    "attacker never crosses that boundary and only observes shared "
                    "hardware timing."
                ),
            },
            {
                "id": "c",
                "text": "Data remanence",
                "correct": False,
                "rationale": (
                    "Incorrect. Data remanence involves recovering residual data left "
                    "behind on storage or memory after it was supposedly cleared; this "
                    "attack observes live timing behavior in real time, not leftover "
                    "data."
                ),
            },
            {
                "id": "d",
                "text": "Hyperjacking",
                "correct": False,
                "rationale": (
                    "Incorrect. Hyperjacking involves installing a rogue hypervisor "
                    "beneath the legitimate one to control every guest VM; no rogue "
                    "hypervisor is described here, only a passive timing measurement."
                ),
            },
        ],
        "explanation": (
            "Deriving secret information from timing variations in a shared physical "
            "resource like CPU cache, without breaching hypervisor isolation, is a "
            "side-channel (cache-timing) attack — distinct from a true VM escape, "
            "data remanence, or hyperjacking."
        ),
    },
    {
        "id": "nd2d-016",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Virtualization vulnerabilities",
        "stem": (
            "An attacker who has gained access to a hypervisor's management network "
            "passively captures an unencrypted live VM migration stream as a "
            "production database VM is moved between physical hosts for maintenance. "
            "Because the migration traffic includes the VM's full memory contents in "
            "the clear, the attacker recovers plaintext database credentials that were "
            "cached in RAM at the moment of migration. Which virtualization "
            "vulnerability does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Interception of unencrypted live VM migration traffic",
                "correct": True,
                "rationale": (
                    "Correct. Live migration transfers a running VM's full memory "
                    "state between hosts; if that management-plane traffic is not "
                    "encrypted, anyone with access to the migration network can "
                    "capture in-memory secrets, exactly as described."
                ),
            },
            {
                "id": "b",
                "text": "VM escape",
                "correct": False,
                "rationale": (
                    "Incorrect. VM escape involves breaking out of a VM's isolation to "
                    "reach the hypervisor or other guests; this attack instead "
                    "passively sniffs network traffic between hosts, without ever "
                    "executing code inside the VM."
                ),
            },
            {
                "id": "c",
                "text": "VM sprawl",
                "correct": False,
                "rationale": (
                    "Incorrect. VM sprawl refers to unmanaged, unaccounted-for virtual "
                    "machines accumulating over time; this scenario involves a known, "
                    "actively managed production VM being migrated, not an "
                    "unauthorized or forgotten instance."
                ),
            },
            {
                "id": "d",
                "text": "Data remanence",
                "correct": False,
                "rationale": (
                    "Incorrect. Data remanence describes residual data recoverable "
                    "from storage after deletion; here the data is captured live, in "
                    "transit, during an active migration, not recovered afterward from "
                    "reused storage."
                ),
            },
        ],
        "explanation": (
            "Sniffing an unencrypted live-migration data stream on the hypervisor "
            "management network to capture a VM's in-memory secrets is a distinct "
            "virtualization risk from VM escape, VM sprawl, or data remanence."
        ),
    },
    # ------------------------------------------------------------------ #
    # Vulnerability scan and assessment result classification (2.3)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2d-017",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability scan and assessment result classification",
        "stem": (
            "A DAST scanner flags a critical reflected XSS finding on a support-ticket "
            "form's \"subject\" parameter. Manual review of the rendered HTML source "
            "shows the application HTML-entity-encodes every character of that "
            "parameter before output, and the payload does not execute in any browser "
            "the team tests. How should this scan result be classified?"
        ),
        "options": [
            {
                "id": "a",
                "text": "False positive",
                "correct": True,
                "rationale": (
                    "Correct. The scanner reported a vulnerability that manual "
                    "verification proves is not actually exploitable because the "
                    "output is properly encoded — the definition of a false positive."
                ),
            },
            {
                "id": "b",
                "text": "True positive",
                "correct": False,
                "rationale": (
                    "Incorrect. A true positive requires the finding to be confirmed "
                    "exploitable; here, manual testing shows the payload cannot "
                    "execute due to proper output encoding."
                ),
            },
            {
                "id": "c",
                "text": "False negative",
                "correct": False,
                "rationale": (
                    "Incorrect. A false negative is a real vulnerability the scanner "
                    "missed entirely; here the scanner did report a finding — the "
                    "issue is that the finding itself does not hold up under manual "
                    "verification."
                ),
            },
            {
                "id": "d",
                "text": "True negative",
                "correct": False,
                "rationale": (
                    "Incorrect. A true negative means no finding was reported and none "
                    "exists; the scanner did produce a finding here, it was simply "
                    "inaccurate."
                ),
            },
        ],
        "explanation": (
            "A reported vulnerability that manual verification disproves — because "
            "the output is safely encoded and the payload cannot execute — is a false "
            "positive, not a true positive, false negative, or true negative."
        ),
    },
    {
        "id": "nd2d-018",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vulnerability scan and assessment result classification",
        "stem": (
            "A scan reports an unauthenticated critical remote code execution "
            "vulnerability on a legacy VPN appliance. The security team manually "
            "replicates the published exploit in an isolated lab against an identical "
            "appliance build and successfully obtains a root shell without any "
            "credentials. How should this finding be classified?"
        ),
        "options": [
            {
                "id": "a",
                "text": "True positive",
                "correct": True,
                "rationale": (
                    "Correct. The scanner's finding was independently confirmed "
                    "exploitable through manual reproduction, achieving unauthenticated "
                    "root access — a true positive requiring immediate remediation."
                ),
            },
            {
                "id": "b",
                "text": "False positive",
                "correct": False,
                "rationale": (
                    "Incorrect. A false positive would mean the manual test failed to "
                    "reproduce the issue; here the exploit succeeded and was fully "
                    "confirmed."
                ),
            },
            {
                "id": "c",
                "text": "False negative",
                "correct": False,
                "rationale": (
                    "Incorrect. A false negative describes a real vulnerability the "
                    "scan failed to report; this vulnerability was reported and then "
                    "confirmed, not missed."
                ),
            },
            {
                "id": "d",
                "text": "True negative",
                "correct": False,
                "rationale": (
                    "Incorrect. A true negative means no vulnerability was reported "
                    "and none exists; here a critical, confirmed vulnerability is "
                    "present."
                ),
            },
        ],
        "explanation": (
            "A scan finding that is independently and successfully reproduced through "
            "manual exploitation is a confirmed true positive, not a false positive, "
            "false negative, or true negative."
        ),
    },
    {
        "id": "nd2d-019",
        "domain": 2,
        "objective": "2.3",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Vulnerability scan and assessment result classification",
        "stem": (
            "A quarterly scan report lists four findings, each with a manual "
            "verification outcome:\n\n"
            "Finding 1 — Critical SQL injection on /login; manual testing confirms "
            "full data exfiltration is possible.\n"
            "Finding 2 — Medium outdated JavaScript library banner; manual review "
            "shows the vendor backported the fix and no exploitable code path "
            "remains.\n"
            "Finding 3 — High missing patch on a print-spooler service; manual "
            "exploitation succeeds, crashing the spooler and executing arbitrary "
            "code.\n"
            "Finding 4 — Critical exposed database port; manual review shows the host "
            "was decommissioned months ago and the port is unreachable from any "
            "network.\n\n"
            "Which TWO findings are true positives requiring remediation? "
            "(Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Finding 1 (SQL injection)",
                "correct": True,
                "rationale": (
                    "Correct. Manual testing confirmed real, exploitable data "
                    "exfiltration, making this a true positive that must be remediated."
                ),
            },
            {
                "id": "b",
                "text": "Finding 2 (outdated library banner)",
                "correct": False,
                "rationale": (
                    "Incorrect. The scanner's version-banner check was inaccurate — "
                    "the fix was backported and no exploitable path exists, making "
                    "this a false positive, not a true positive."
                ),
            },
            {
                "id": "c",
                "text": "Finding 3 (print-spooler patch)",
                "correct": True,
                "rationale": (
                    "Correct. Manual exploitation succeeded and achieved arbitrary "
                    "code execution, confirming this is a genuine, exploitable "
                    "vulnerability requiring remediation."
                ),
            },
            {
                "id": "d",
                "text": "Finding 4 (exposed database port)",
                "correct": False,
                "rationale": (
                    "Incorrect. The host is decommissioned and unreachable, so the "
                    "reported port exposure does not actually exist in the current "
                    "environment — a false positive rather than a true positive."
                ),
            },
        ],
        "explanation": (
            "Only findings independently confirmed as real and exploitable through "
            "manual verification (SQL injection and the print-spooler flaw) are true "
            "positives; the outdated-banner and decommissioned-host findings are false "
            "positives despite the scanner's severity rating."
        ),
    },
    # ------------------------------------------------------------------ #
    # Indicators of malicious activity (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2d-020",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Indicators of malicious activity",
        "stem": (
            "Within a two-minute window, 40 Active Directory accounts lock out "
            "simultaneously. Each lockout was preceded by exactly five failed login "
            "attempts originating from the same internal workstation, and every "
            "affected user insists they never entered a wrong password during that "
            "time. No password policy or account changes were made by IT. Which "
            "indicator of malicious activity is this MOST consistent with?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Account lockout from an internal password-guessing attempt",
                "correct": True,
                "rationale": (
                    "Correct. A single internal host rapidly attempting logins against "
                    "many accounts, driving each one to its lockout threshold, "
                    "indicates a compromised internal system running an automated "
                    "credential-guessing attack against multiple users."
                ),
            },
            {
                "id": "b",
                "text": "Impossible travel",
                "correct": False,
                "rationale": (
                    "Incorrect. Impossible travel describes successful logins from "
                    "geographically implausible locations in a short time span; this "
                    "scenario involves failed attempts and lockouts from a single "
                    "internal source, not travel-distance anomalies."
                ),
            },
            {
                "id": "c",
                "text": "Concurrent session usage",
                "correct": False,
                "rationale": (
                    "Incorrect. Concurrent session usage refers to one account being "
                    "actively used from two places at once; here, accounts are being "
                    "locked out by failed attempts, not simultaneously active sessions."
                ),
            },
            {
                "id": "d",
                "text": "Resource consumption",
                "correct": False,
                "rationale": (
                    "Incorrect. Resource consumption indicators involve abnormal CPU, "
                    "memory, or bandwidth usage; this scenario centers on "
                    "authentication failures and lockouts, not system resource load."
                ),
            },
        ],
        "explanation": (
            "A single internal source driving many accounts to their lockout "
            "threshold with failed logins the legitimate users never attempted is a "
            "mass account-lockout indicator of an internal credential-guessing attack."
        ),
    },
    {
        "id": "nd2d-021",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Indicators of malicious activity",
        "stem": (
            "Web proxy logs show a single workstation generating thousands of "
            "\"blocked — malware signature match\" entries per day for three "
            "consecutive days, each attempting to reach known command-and-control "
            "infrastructure every few seconds. Antivirus scans on the workstation "
            "report no threats, and the user reports nothing unusual. Which indicator "
            "of malicious activity is this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Blocked content indicating an active, undetected infection",
                "correct": True,
                "rationale": (
                    "Correct. A high volume of repeated, automatically blocked "
                    "connection attempts to known-malicious infrastructure — despite a "
                    "clean local antivirus scan — indicates malware is actively "
                    "beaconing on the host and is simply being stopped at the network "
                    "boundary rather than removed."
                ),
            },
            {
                "id": "b",
                "text": "Resource inaccessibility",
                "correct": False,
                "rationale": (
                    "Incorrect. Resource inaccessibility describes legitimate "
                    "resources becoming unavailable to authorized users (e.g., during "
                    "ransomware or DoS); this scenario is about outbound connections "
                    "being blocked, not resources being denied to the user."
                ),
            },
            {
                "id": "c",
                "text": "Impossible travel",
                "correct": False,
                "rationale": (
                    "Incorrect. Impossible travel involves authentication from "
                    "geographically implausible locations; no login activity is "
                    "described here at all."
                ),
            },
            {
                "id": "d",
                "text": "Missing logs",
                "correct": False,
                "rationale": (
                    "Incorrect. The proxy logs are present and complete, clearly "
                    "recording every blocked attempt; nothing is missing from the log "
                    "record."
                ),
            },
        ],
        "explanation": (
            "Repeated, proxy-blocked outbound attempts to known C2 infrastructure — "
            "despite a clean antivirus scan — is a blocked-content indicator revealing "
            "an infection the endpoint tool failed to detect."
        ),
    },
    # ------------------------------------------------------------------ #
    # Malware types (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2d-022",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Malware types",
        "stem": (
            "An antivirus vendor examines malware samples recovered from 50 infected "
            "hosts. All 50 samples exhibit identical malicious behavior, but every "
            "sample has a completely different file hash and byte-level signature, "
            "because the malware re-encrypts its own body with a newly generated key "
            "and appends a matching decryption routine each time it propagates. Which "
            "malware characteristic does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Polymorphism",
                "correct": True,
                "rationale": (
                    "Correct. Re-encrypting the malicious payload with a new key on "
                    "each infection — while the underlying functionality and a "
                    "matching decryptor stay effectively the same — is the defining "
                    "behavior of polymorphic malware, designed to defeat static "
                    "signature-based detection."
                ),
            },
            {
                "id": "b",
                "text": "Metamorphism",
                "correct": False,
                "rationale": (
                    "Incorrect. Metamorphic malware rewrites and restructures its own "
                    "underlying code logic on each generation (without relying on "
                    "encryption/decryption), producing genuinely different code paths; "
                    "this sample instead reuses the same logic wrapped in a new "
                    "encryption layer, which is polymorphism."
                ),
            },
            {
                "id": "c",
                "text": "Ransomware",
                "correct": False,
                "rationale": (
                    "Incorrect. Nothing describes files being encrypted for ransom or "
                    "a extortion demand; the malware is encrypting its own code to "
                    "evade detection, not victim data."
                ),
            },
            {
                "id": "d",
                "text": "Rootkit",
                "correct": False,
                "rationale": (
                    "Incorrect. A rootkit hides its presence by subverting OS-level "
                    "components; this scenario describes signature evasion through "
                    "self-re-encryption, not concealment via kernel or system "
                    "manipulation."
                ),
            },
        ],
        "explanation": (
            "Self-re-encrypting each generation with a new key while keeping the same "
            "decryptor and functionality is polymorphism, distinguished from "
            "metamorphism (which rewrites the code logic itself), ransomware, and "
            "rootkits."
        ),
    },
    {
        "id": "nd2d-023",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Malware types",
        "stem": (
            "An incident review of a compromised server finds: (1) a legitimate, "
            "commercially signed remote-monitoring-and-management (RMM) tool was "
            "installed with no approved change ticket; (2) the tool grants full "
            "remote desktop control, keystroke capture, and file transfer to an "
            "external operator; (3) it maintains a persistent outbound connection to "
            "an external relay server; and (4) it was manually added to the "
            "antivirus exclusion list shortly after installation. Which TWO "
            "classifications BEST describe what occurred? (Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Remote access trojan (RAT) capability",
                "correct": True,
                "rationale": (
                    "Correct. Full remote control, keystroke capture, file transfer, "
                    "and a persistent outbound connection to an external operator are "
                    "exactly the capabilities of a remote access trojan, regardless of "
                    "whether the underlying binary is a commercial tool."
                ),
            },
            {
                "id": "b",
                "text": "Living-off-the-land technique",
                "correct": True,
                "rationale": (
                    "Correct. Abusing a legitimate, signed administrative tool already "
                    "trusted in the environment — rather than deploying custom "
                    "malware — and manipulating the antivirus exclusion list to avoid "
                    "detection is a classic living-off-the-land approach."
                ),
            },
            {
                "id": "c",
                "text": "Rootkit",
                "correct": False,
                "rationale": (
                    "Incorrect. Nothing describes kernel-level concealment or "
                    "modification of OS components to hide the tool's presence; it was "
                    "simply excluded from antivirus scanning, not hidden at the system "
                    "level."
                ),
            },
            {
                "id": "d",
                "text": "Worm",
                "correct": False,
                "rationale": (
                    "Incorrect. No self-propagation to other hosts without user or "
                    "operator action is described; this activity is confined to "
                    "attacker-directed remote control of a single compromised server."
                ),
            },
            {
                "id": "e",
                "text": "Logic bomb",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no dormant, condition-triggered payload "
                    "waiting for a specific date or event; the tool is actively used "
                    "for ongoing, real-time remote access."
                ),
            },
        ],
        "explanation": (
            "Full remote control and a persistent external connection match RAT "
            "capability, while abusing a trusted, already-installed administrative "
            "tool and its antivirus exclusion list — instead of deploying new "
            "custom malware — is living off the land; no propagation, kernel "
            "concealment, or dormant trigger is described."
        ),
    },
    # ------------------------------------------------------------------ #
    # Network attacks (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2d-024",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Network attacks",
        "stem": (
            "A penetration tester sends a victim a link that forces the victim's OS to "
            "automatically attempt SMB authentication to an attacker-controlled share. "
            "The tester's tool captures that live NTLM authentication attempt and, in "
            "real time, forwards it to authenticate to an unrelated file server before "
            "the exchange expires — gaining access without ever cracking or offline-"
            "reusing the credential material. Which attack does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Relay attack (SMB/NTLM relay)",
                "correct": True,
                "rationale": (
                    "Correct. Forwarding a captured, live authentication exchange in "
                    "real time to a different target — rather than storing and reusing "
                    "it later — is the defining behavior of a relay attack."
                ),
            },
            {
                "id": "b",
                "text": "Pass-the-hash",
                "correct": False,
                "rationale": (
                    "Incorrect. Pass-the-hash reuses a previously extracted, static "
                    "NTLM hash (typically dumped from memory) to authenticate later, "
                    "on the attacker's own schedule; this attack instead relays a "
                    "live, in-progress authentication attempt in real time."
                ),
            },
            {
                "id": "c",
                "text": "ARP spoofing",
                "correct": False,
                "rationale": (
                    "Incorrect. ARP spoofing poisons a local segment's MAC-to-IP "
                    "mappings to intercept traffic; this attack instead lures the "
                    "victim's OS into initiating authentication to an "
                    "attacker-controlled endpoint and relays it, with no ARP "
                    "manipulation described."
                ),
            },
            {
                "id": "d",
                "text": "Replay attack",
                "correct": False,
                "rationale": (
                    "Incorrect. A replay attack retransmits a previously captured, "
                    "identical exchange later for the same purpose; here the "
                    "authentication attempt is forwarded live, to a different target, "
                    "as it happens — not stored and replayed afterward."
                ),
            },
        ],
        "explanation": (
            "Forwarding a live, in-progress NTLM authentication attempt in real time "
            "to a different target server is a relay attack, distinct from "
            "pass-the-hash (offline reuse of a static hash), ARP spoofing, or a "
            "delayed replay of a stored exchange."
        ),
    },
    {
        "id": "nd2d-025",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network attacks",
        "stem": (
            "A tester sends spoofed 802.11 management frames instructing a target "
            "laptop to disconnect from its legitimate wireless access point. The "
            "frames are sent repeatedly, timed so that whenever the laptop tries to "
            "reconnect it instead associates with the tester's rogue access point "
            "broadcasting the identical SSID at a stronger signal. Which specific "
            "technique is being used to forcibly disconnect the laptop?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Deauthentication attack",
                "correct": True,
                "rationale": (
                    "Correct. Sending spoofed 802.11 deauthentication frames to force "
                    "a client off its current access point — so it is available to "
                    "associate with a rogue AP instead — is the specific mechanism "
                    "described."
                ),
            },
            {
                "id": "b",
                "text": "RF jamming",
                "correct": False,
                "rationale": (
                    "Incorrect. RF jamming floods the radio frequency with noise to "
                    "disrupt all nearby wireless communication indiscriminately; this "
                    "attack instead sends targeted, spoofed management frames to one "
                    "specific client."
                ),
            },
            {
                "id": "c",
                "text": "Evil twin",
                "correct": False,
                "rationale": (
                    "Incorrect. The evil twin is the rogue access point itself, "
                    "already described separately in the scenario; the question asks "
                    "specifically about the technique used to force the disconnect "
                    "that enables the victim to join it."
                ),
            },
            {
                "id": "d",
                "text": "Bluejacking",
                "correct": False,
                "rationale": (
                    "Incorrect. Bluejacking sends unsolicited messages over Bluetooth; "
                    "this attack operates entirely over 802.11 Wi-Fi management "
                    "frames, not Bluetooth."
                ),
            },
        ],
        "explanation": (
            "Spoofed 802.11 deauthentication frames selectively forcing one client "
            "off its legitimate AP — distinct from broadband jamming, the rogue AP "
            "itself, or Bluetooth-based attacks — is a deauthentication attack."
        ),
    },
    # ------------------------------------------------------------------ #
    # Physical attacks (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2d-026",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Physical attacks",
        "stem": (
            "A traveling executive leaves a company laptop, powered off and "
            "unencrypted, in a hotel room while attending dinner. Housekeeping staff "
            "access the room during that window. Days later, credentials belonging "
            "only to that executive appear in use from an unfamiliar location, and a "
            "later inspection finds a small inline hardware device connected between "
            "the laptop's keyboard cable and its port. Which physical attack does this "
            "describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Evil maid attack",
                "correct": True,
                "rationale": (
                    "Correct. Brief, unsupervised physical access to an unattended "
                    "device — used to install a persistent hardware implant such as an "
                    "inline keystroke logger — is the defining scenario of an evil "
                    "maid attack."
                ),
            },
            {
                "id": "b",
                "text": "Tailgating",
                "correct": False,
                "rationale": (
                    "Incorrect. Tailgating involves following an authorized person "
                    "through a secured entry point; this attack instead involves "
                    "someone with routine access to the room installing a hardware "
                    "implant on an unattended device."
                ),
            },
            {
                "id": "c",
                "text": "Dumpster diving",
                "correct": False,
                "rationale": (
                    "Incorrect. Dumpster diving recovers discarded information from "
                    "trash or recycling; nothing here involves searching discarded "
                    "materials."
                ),
            },
            {
                "id": "d",
                "text": "Shoulder surfing",
                "correct": False,
                "rationale": (
                    "Incorrect. Shoulder surfing involves directly observing a "
                    "victim's screen or keypad entry in person; here the laptop was "
                    "powered off and unattended, and the compromise came from a "
                    "physically installed hardware device, not visual observation."
                ),
            },
        ],
        "explanation": (
            "Using brief, seemingly routine physical access to an unattended, "
            "powered-off device to install a persistent hardware keystroke logger is "
            "the classic evil maid attack, distinct from tailgating, dumpster diving, "
            "or shoulder surfing."
        ),
    },
    {
        "id": "nd2d-027",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Physical attacks",
        "stem": (
            "An auditor demonstrates that a server room's mechanical pin-tumbler door "
            "lock can be opened in under 10 seconds using a specially cut key and a "
            "sharp strike to set the pins without the correct key ever being used. "
            "Because the door's badge reader is a separate system from the mechanical "
            "lock, the badge log shows no entry at all for the time of the "
            "demonstration. Which physical attack technique did the auditor use?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Lock bumping",
                "correct": True,
                "rationale": (
                    "Correct. Using a specially cut key with a sharp strike to force "
                    "pins into alignment without the true key is lock bumping, a "
                    "well-known mechanical lock bypass technique that leaves no "
                    "electronic access record."
                ),
            },
            {
                "id": "b",
                "text": "Tailgating",
                "correct": False,
                "rationale": (
                    "Incorrect. Tailgating relies on following an authorized person "
                    "through an open door; the auditor instead defeated the mechanical "
                    "lock directly and alone."
                ),
            },
            {
                "id": "c",
                "text": "Badge cloning",
                "correct": False,
                "rationale": (
                    "Incorrect. Badge cloning captures and replicates a proximity "
                    "card's credential to fool an RFID reader; this attack bypassed "
                    "the mechanical lock entirely and never interacted with the badge "
                    "reader."
                ),
            },
            {
                "id": "d",
                "text": "Dumpster diving",
                "correct": False,
                "rationale": (
                    "Incorrect. Dumpster diving involves recovering discarded "
                    "materials from trash; no such activity is described here."
                ),
            },
        ],
        "explanation": (
            "Rapidly defeating a pin-tumbler lock with a bump key and a sharp strike — "
            "leaving no trace in the separate electronic badge log — is lock bumping, "
            "distinct from tailgating, badge cloning, or dumpster diving, and "
            "highlights the gap of a mechanical lock not integrated with the access-"
            "control/alarm system."
        ),
    },
    {
        "id": "nd2d-028",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Physical attacks",
        "stem": (
            "A warehouse's loading-dock door uses an electronic strike plate that only "
            "reports a \"door held open\" alert to the security system. An intruder "
            "uses a hydraulic jack to physically pry the door frame apart until the "
            "strike plate itself breaks free of the wall, bypassing the lock "
            "mechanism entirely without ever holding the door open long enough to "
            "trigger an alert. Which category of physical attack does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Forced/brute-force entry",
                "correct": True,
                "rationale": (
                    "Correct. Using mechanical force to physically destroy or "
                    "dislodge a door's locking hardware — rather than defeating the "
                    "lock mechanism with finesse — is a forced or brute-force entry "
                    "attack, and it exploited a sensor that only detects prolonged "
                    "open states, not structural forcing."
                ),
            },
            {
                "id": "b",
                "text": "Lock bumping",
                "correct": False,
                "rationale": (
                    "Incorrect. Lock bumping is a finesse technique that manipulates "
                    "the internal pins of a lock using a specially cut key; this "
                    "attack instead used raw mechanical force to physically destroy "
                    "the door frame and strike plate."
                ),
            },
            {
                "id": "c",
                "text": "Tailgating",
                "correct": False,
                "rationale": (
                    "Incorrect. Tailgating requires following an authorized person "
                    "through a door being legitimately opened; this intrusion involved "
                    "physically destroying the door hardware while unaccompanied."
                ),
            },
            {
                "id": "d",
                "text": "Environmental sabotage",
                "correct": False,
                "rationale": (
                    "Incorrect. Environmental sabotage targets HVAC, power, or fire-"
                    "suppression systems; this attack targeted the physical door and "
                    "locking hardware directly, not an environmental control system."
                ),
            },
        ],
        "explanation": (
            "Using mechanical force to physically destroy a door's locking hardware, "
            "exploiting a sensor gap that only flags prolonged open states, is a "
            "forced/brute-force entry attack, distinct from the finesse of lock "
            "bumping, tailgating, or environmental sabotage."
        ),
    },
    # ------------------------------------------------------------------ #
    # Cryptographic attacks (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2d-029",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Cryptographic attacks",
        "stem": (
            "An attacker intercepts a set of encrypted backup files from a legacy "
            "proprietary system. Separately, the attacker obtains an unencrypted copy "
            "of one of those exact files from an old, unpatched backup share. By "
            "comparing that known unencrypted file to its corresponding intercepted "
            "ciphertext, the attacker derives the encryption key and uses it to "
            "decrypt every other backup encrypted with the same key. Which "
            "cryptographic attack does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Known-plaintext attack",
                "correct": True,
                "rationale": (
                    "Correct. Deriving the key by comparing an already-known, "
                    "unencrypted file to its corresponding ciphertext — without "
                    "choosing what gets encrypted — is the definition of a "
                    "known-plaintext attack."
                ),
            },
            {
                "id": "b",
                "text": "Chosen-plaintext attack",
                "correct": False,
                "rationale": (
                    "Incorrect. A chosen-plaintext attack requires the attacker to "
                    "submit arbitrary plaintext of their choosing to the encryption "
                    "process and observe the resulting ciphertext; here the attacker "
                    "merely found a pre-existing plaintext copy, not chosen or "
                    "submitted it for encryption."
                ),
            },
            {
                "id": "c",
                "text": "Brute-force attack",
                "correct": False,
                "rationale": (
                    "Incorrect. A brute-force attack tries every possible key without "
                    "using any known plaintext-ciphertext relationship; this attack "
                    "instead directly leverages a matched plaintext/ciphertext pair to "
                    "derive the key."
                ),
            },
            {
                "id": "d",
                "text": "Birthday attack",
                "correct": False,
                "rationale": (
                    "Incorrect. A birthday attack exploits hash collision probability "
                    "to find two inputs producing the same digest; this scenario "
                    "involves recovering an encryption key from a matched plaintext "
                    "and ciphertext, not a hash collision."
                ),
            },
        ],
        "explanation": (
            "Recovering a key by comparing an already-known plaintext file to its "
            "matching intercepted ciphertext — without the attacker choosing what was "
            "encrypted — is a known-plaintext attack, distinct from chosen-plaintext, "
            "brute-force, or birthday attacks."
        ),
    },
    {
        "id": "nd2d-030",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Cryptographic attacks",
        "stem": (
            "A web application's session-token decryption endpoint returns one generic "
            "error message when the decrypted padding is invalid and a different, "
            "distinct error message when the padding is valid but the content is "
            "malformed. An attacker submits thousands of modified ciphertext guesses "
            "and, by observing which of the two error messages each guess triggers, "
            "iteratively decrypts an entire session token byte-by-byte without ever "
            "learning the encryption key. Which attack does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Padding oracle attack",
                "correct": True,
                "rationale": (
                    "Correct. Exploiting a system that reveals, through distinguishable "
                    "error responses, whether decrypted padding is valid — allowing an "
                    "attacker to decrypt ciphertext byte-by-byte without the key — is "
                    "precisely a padding oracle attack."
                ),
            },
            {
                "id": "b",
                "text": "Downgrade attack",
                "correct": False,
                "rationale": (
                    "Incorrect. A downgrade attack forces a connection to negotiate a "
                    "weaker protocol or cipher suite; this attack instead abuses "
                    "distinguishable error messages from padding validation, with no "
                    "protocol negotiation involved."
                ),
            },
            {
                "id": "c",
                "text": "Replay attack",
                "correct": False,
                "rationale": (
                    "Incorrect. A replay attack resubmits a previously valid, "
                    "unmodified message to repeat its effect; here the attacker is "
                    "submitting thousands of deliberately modified ciphertext guesses "
                    "to extract information from error responses, not replaying an "
                    "unaltered message."
                ),
            },
            {
                "id": "d",
                "text": "Known-plaintext attack",
                "correct": False,
                "rationale": (
                    "Incorrect. A known-plaintext attack requires an existing matched "
                    "plaintext/ciphertext pair; here the attacker has no known "
                    "plaintext at all and instead leverages an error-message side "
                    "channel to decrypt data incrementally."
                ),
            },
        ],
        "explanation": (
            "Using distinguishable error responses from padding validation to "
            "incrementally decrypt ciphertext without ever learning the key is a "
            "padding oracle attack, distinct from a protocol downgrade, replay, or "
            "known-plaintext attack."
        ),
    },
    {
        "id": "nd2d-031",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Cryptographic attacks",
        "stem": (
            "A researcher demonstrates an attack against a WPA2 wireless network by "
            "replaying message three of the four-way handshake to a connected client. "
            "This forces the client to reinstall an encryption key it is already "
            "using, resetting its nonce/packet-counter back to an initial value. Once "
            "the nonce is reused, the researcher is able to decrypt intercepted "
            "packets by exploiting the resulting repeated keystream. Which attack "
            "does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Key-reinstallation attack (nonce/IV reuse)",
                "correct": True,
                "rationale": (
                    "Correct. Forcing a client to reinstall an already-in-use "
                    "encryption key by replaying a handshake message — resetting its "
                    "nonce counter and causing keystream reuse that enables decryption "
                    "— is the defining mechanism of a key-reinstallation attack."
                ),
            },
            {
                "id": "b",
                "text": "Downgrade attack",
                "correct": False,
                "rationale": (
                    "Incorrect. A downgrade attack forces negotiation of a weaker "
                    "protocol version or cipher suite entirely; this attack instead "
                    "manipulates the handshake to force key/nonce reuse within the "
                    "same protocol and cipher, not a switch to a weaker one."
                ),
            },
            {
                "id": "c",
                "text": "Rainbow table attack",
                "correct": False,
                "rationale": (
                    "Incorrect. A rainbow table attack uses precomputed hash-to-"
                    "plaintext mappings to reverse password hashes offline; nothing "
                    "here involves password hash cracking, only live manipulation of "
                    "the key-exchange handshake."
                ),
            },
            {
                "id": "d",
                "text": "Evil twin",
                "correct": False,
                "rationale": (
                    "Incorrect. An evil twin is a rogue access point impersonating a "
                    "legitimate one; this attack instead targets the client's existing, "
                    "legitimate connection by manipulating handshake messages, with no "
                    "rogue AP involved."
                ),
            },
        ],
        "explanation": (
            "Replaying a handshake message to force reinstallation of an already-used "
            "encryption key — resetting the nonce and enabling keystream reuse — is a "
            "key-reinstallation (nonce/IV reuse) attack, distinct from a protocol "
            "downgrade, rainbow table attack, or evil twin."
        ),
    },
    # ------------------------------------------------------------------ #
    # Log sources and investigative questions (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2d-032",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log sources and investigative questions",
        "stem": (
            "A malicious connection from an internal IP address was logged at a "
            "specific timestamp, but that IP address is dynamically assigned and has "
            "been used by several different laptops throughout the day as they join "
            "and leave the wired network. Investigators need to determine exactly "
            "which physical device (by MAC address) held that IP address at the "
            "moment the malicious connection occurred. Which log source will BEST "
            "answer this question?"
        ),
        "options": [
            {
                "id": "a",
                "text": "DHCP server lease logs",
                "correct": True,
                "rationale": (
                    "Correct. DHCP lease logs record which MAC address was assigned "
                    "each IP address and for what time window, making them the "
                    "authoritative source for mapping a dynamically assigned IP back "
                    "to a specific physical device at a given moment."
                ),
            },
            {
                "id": "b",
                "text": "Firewall logs",
                "correct": False,
                "rationale": (
                    "Incorrect. Firewall logs record connection details such as source "
                    "and destination IPs and ports, but they do not track which "
                    "physical device held a dynamic IP address at a given time."
                ),
            },
            {
                "id": "c",
                "text": "DNS query logs",
                "correct": False,
                "rationale": (
                    "Incorrect. DNS logs record which hostnames were resolved by which "
                    "IP addresses; they do not map an IP address to the physical "
                    "device (MAC address) that was using it at a specific time."
                ),
            },
            {
                "id": "d",
                "text": "NetFlow records",
                "correct": False,
                "rationale": (
                    "Incorrect. NetFlow records summarize traffic volume and "
                    "conversations between IP addresses; they do not provide the "
                    "IP-to-MAC-address lease mapping needed to identify the specific "
                    "device."
                ),
            },
        ],
        "explanation": (
            "Only DHCP lease logs record the precise mapping between a dynamically "
            "assigned IP address, the MAC address it was leased to, and the exact "
            "time window of that assignment."
        ),
    },
    {
        "id": "nd2d-033",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Log sources and investigative questions",
        "stem": (
            "A public-facing web application crashes intermittently several times a "
            "day. The web server's standard access logs show only successful "
            "\"200 OK\" entries around each crash time, giving no indication of what "
            "triggered the fault. Which log source will BEST reveal the specific "
            "malformed request or internal error condition that caused the crash?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Application/error logs",
                "correct": True,
                "rationale": (
                    "Correct. Access logs record only the request line and response "
                    "status, not internal processing details; the application's own "
                    "error/debug logs capture stack traces, exceptions, and the "
                    "specific condition that caused the crash."
                ),
            },
            {
                "id": "b",
                "text": "Firewall logs",
                "correct": False,
                "rationale": (
                    "Incorrect. Firewall logs record allow/deny decisions at the "
                    "network perimeter; they contain no insight into an "
                    "application's internal processing errors or crash causes."
                ),
            },
            {
                "id": "c",
                "text": "DNS logs",
                "correct": False,
                "rationale": (
                    "Incorrect. DNS logs record name resolution requests; they have no "
                    "visibility into what happens after a request reaches the web "
                    "application."
                ),
            },
            {
                "id": "d",
                "text": "NetFlow records",
                "correct": False,
                "rationale": (
                    "Incorrect. NetFlow records summarize traffic volume between IP "
                    "addresses and ports; they do not capture application-level error "
                    "details or the content of individual requests."
                ),
            },
        ],
        "explanation": (
            "Because access logs only show that a request succeeded at the HTTP "
            "level, the application's own error/debug logs are the log source that "
            "will actually reveal the internal fault condition behind the crash."
        ),
    },
    # ------------------------------------------------------------------ #
    # Authentication factors and protocols (2.4)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2d-034",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Authentication factors and protocols",
        "stem": (
            "An attacker who already possesses a user's valid password triggers dozens "
            "of push-based MFA approval requests to the user's phone between 1 a.m. "
            "and 2 a.m., minutes apart. After repeatedly dismissing them, the "
            "exhausted user finally taps \"Approve\" just to stop the notifications, "
            "unknowingly granting the attacker access. Which attack does this "
            "describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "MFA fatigue (push bombing)",
                "correct": True,
                "rationale": (
                    "Correct. Repeatedly bombarding a user with push-based MFA "
                    "prompts until they approve one out of exhaustion or annoyance — "
                    "rather than defeating the MFA mechanism technically — is the "
                    "defining behavior of an MFA fatigue (push bombing) attack."
                ),
            },
            {
                "id": "b",
                "text": "Pass-the-hash",
                "correct": False,
                "rationale": (
                    "Incorrect. Pass-the-hash reuses a captured password hash to "
                    "authenticate directly; here the attacker already has the "
                    "password and instead exploits user fatigue with repeated MFA "
                    "prompts to bypass the second factor."
                ),
            },
            {
                "id": "c",
                "text": "Golden ticket attack",
                "correct": False,
                "rationale": (
                    "Incorrect. A golden ticket forges a Kerberos ticket-granting "
                    "ticket using a stolen krbtgt account hash for persistent domain "
                    "access; no Kerberos ticket forgery is involved in this "
                    "push-notification exhaustion scenario."
                ),
            },
            {
                "id": "d",
                "text": "SIM swapping",
                "correct": False,
                "rationale": (
                    "Incorrect. SIM swapping fraudulently transfers a victim's phone "
                    "number to an attacker-controlled SIM; here the legitimate user "
                    "still receives and interacts with the push notifications on "
                    "their own device."
                ),
            },
        ],
        "explanation": (
            "Repeatedly sending push-based MFA prompts until the user approves one out "
            "of exhaustion is MFA fatigue (push bombing), distinct from pass-the-hash, "
            "golden ticket forgery, or SIM swapping."
        ),
    },
    {
        "id": "nd2d-035",
        "domain": 2,
        "objective": "2.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Authentication factors and protocols",
        "stem": (
            "Forensic analysis finds that an attacker extracted a still-valid Kerberos "
            "service ticket (TGS) directly from one compromised workstation's memory. "
            "Without ever learning the associated account's password or NTLM hash, the "
            "attacker injected that exact ticket into a session on a second, unrelated "
            "workstation and used it to access the specific file share the ticket was "
            "originally scoped for, before its normal lifetime expired. Which attack "
            "does this describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Pass-the-ticket attack",
                "correct": True,
                "rationale": (
                    "Correct. Extracting a legitimately issued, still-valid Kerberos "
                    "ticket from memory and reusing it on a different system — without "
                    "ever cracking a password or hash — is the defining mechanism of a "
                    "pass-the-ticket attack."
                ),
            },
            {
                "id": "b",
                "text": "Pass-the-hash attack",
                "correct": False,
                "rationale": (
                    "Incorrect. Pass-the-hash reuses a captured NTLM password hash to "
                    "authenticate; here the attacker reused an already-issued Kerberos "
                    "ticket directly and never obtained or used a password hash."
                ),
            },
            {
                "id": "c",
                "text": "Golden ticket attack",
                "correct": False,
                "rationale": (
                    "Incorrect. A golden ticket is a forged TGT built using the "
                    "domain's stolen krbtgt hash, granting unlimited persistent access "
                    "to any resource without normal ticket expiration; this attack "
                    "instead reused one legitimately issued, time-limited ticket "
                    "scoped to a specific share."
                ),
            },
            {
                "id": "d",
                "text": "Kerberoasting",
                "correct": False,
                "rationale": (
                    "Incorrect. Kerberoasting requests service tickets for accounts "
                    "with service principal names in order to crack their passwords "
                    "offline; here no cracking occurred — the attacker directly reused "
                    "a stolen, already-valid ticket."
                ),
            },
        ],
        "explanation": (
            "Extracting and reusing one legitimately issued, time-limited Kerberos "
            "service ticket on a different host — with no password, hash, or "
            "krbtgt-based forgery involved — is a pass-the-ticket attack, distinct "
            "from pass-the-hash, a golden ticket, or kerberoasting."
        ),
    },
    # ------------------------------------------------------------------ #
    # Hardening (2.5)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2d-036",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Hardening",
        "stem": (
            "A security baseline audit finds that all 500 workstations in a fleet "
            "share the exact same local Administrator password, set once during "
            "imaging and never rotated since. Once an attacker compromises the local "
            "Administrator account on any single workstation, they can immediately "
            "authenticate as local Administrator on every other workstation in the "
            "fleet. Which hardening technique BEST addresses this specific weakness?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Deploy a solution that randomizes and rotates each local "
                "Administrator password uniquely per device",
                "correct": True,
                "rationale": (
                    "Correct. Assigning each workstation a unique, regularly rotated "
                    "local Administrator password eliminates the ability to reuse one "
                    "compromised local credential across the entire fleet, directly "
                    "closing the lateral-movement path described."
                ),
            },
            {
                "id": "b",
                "text": "Disable the local Administrator account on every workstation",
                "correct": False,
                "rationale": (
                    "Incorrect. Local support and recovery processes on many fleets "
                    "still depend on a functioning local Administrator account; simply "
                    "disabling it fleet-wide does not address the underlying "
                    "shared-password weakness and can break legitimate maintenance "
                    "workflows."
                ),
            },
            {
                "id": "c",
                "text": "Segment workstations onto separate VLANs by department",
                "correct": False,
                "rationale": (
                    "Incorrect. Network segmentation limits traffic paths between "
                    "segments but does not change the fact that the identical local "
                    "Administrator credential still works on every workstation within "
                    "reach of an attacker."
                ),
            },
            {
                "id": "d",
                "text": "Require users to change their own domain password every 30 "
                "days",
                "correct": False,
                "rationale": (
                    "Incorrect. Domain user password rotation has no effect on the "
                    "separate, shared local Administrator account, which is the "
                    "credential actually being reused across the fleet."
                ),
            },
        ],
        "explanation": (
            "Uniquely randomizing and rotating each device's local Administrator "
            "password is the hardening technique that directly eliminates fleet-wide "
            "reuse of a single compromised local credential."
        ),
    },
    {
        "id": "nd2d-037",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Hardening",
        "stem": (
            "An assessment of remote-worker laptops finds that full-disk encryption "
            "is enabled, but Secure Boot is disabled and the encryption key protector "
            "is stored in a software-only keystore rather than bound to the device's "
            "TPM. Investigators demonstrate that a stolen laptop's drive can be "
            "removed, mounted on another machine, and its encryption key recovered "
            "from that unprotected keystore. Which hardening action would BEST close "
            "this gap?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Enable Secure Boot and bind the disk-encryption key protector "
                "to the device's TPM",
                "correct": True,
                "rationale": (
                    "Correct. Binding the encryption key to the TPM, protected by a "
                    "verified Secure Boot chain, ensures the key can only be released "
                    "on that specific, unmodified hardware and boot state — preventing "
                    "the drive from being removed and its key recovered on another "
                    "machine."
                ),
            },
            {
                "id": "b",
                "text": "Enforce a screensaver lock after 5 minutes of inactivity",
                "correct": False,
                "rationale": (
                    "Incorrect. A screensaver lock only protects against someone "
                    "accessing an unattended, powered-on session; it has no effect on "
                    "an offline attack where the drive is physically removed and "
                    "mounted elsewhere."
                ),
            },
            {
                "id": "c",
                "text": "Enroll the laptop in mobile device management (MDM) only",
                "correct": False,
                "rationale": (
                    "Incorrect. MDM enrollment can enforce policy compliance but does "
                    "not, by itself, change how or where the encryption key protector "
                    "is stored; the software-only keystore remains recoverable offline."
                ),
            },
            {
                "id": "d",
                "text": "Physically disable all USB ports on the laptop",
                "correct": False,
                "rationale": (
                    "Incorrect. Disabling USB ports prevents certain removable-media "
                    "attacks but does nothing to protect an encryption key stored in an "
                    "unprotected software keystore when the drive itself is removed."
                ),
            },
        ],
        "explanation": (
            "Binding the disk-encryption key to a TPM through a verified Secure Boot "
            "chain is the hardening step that prevents the key from being recoverable "
            "once the drive is removed from its original hardware — a screensaver "
            "lock, MDM enrollment alone, or disabling USB ports do not address this "
            "offline key-extraction weakness."
        ),
    },
    # ------------------------------------------------------------------ #
    # Mitigation techniques (2.5)
    # ------------------------------------------------------------------ #
    {
        "id": "nd2d-038",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mitigation techniques",
        "stem": (
            "A post-incident review finds that although critical patches are "
            "consistently approved within 48 hours of release, they are not actually "
            "installed for 45 or more days because engineers apply them manually, "
            "server by server, on an ad hoc schedule. Multiple servers were "
            "compromised by an actively exploited vulnerability three weeks after a "
            "patch for it had already been approved. Which mitigation technique would "
            "MOST effectively close this gap going forward?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Automated, scheduled patch deployment (configuration "
                "enforcement)",
                "correct": True,
                "rationale": (
                    "Correct. Automating patch deployment on a defined, enforced "
                    "schedule directly eliminates the manual, ad hoc delay that left "
                    "an already-approved patch uninstalled for over 45 days."
                ),
            },
            {
                "id": "b",
                "text": "Move to a strict quarterly manual patch cycle",
                "correct": False,
                "rationale": (
                    "Incorrect. A quarterly cycle would make the delay between "
                    "approval and installation even longer, worsening rather than "
                    "solving the problem described."
                ),
            },
            {
                "id": "c",
                "text": "Segment servers into additional network zones",
                "correct": False,
                "rationale": (
                    "Incorrect. Segmentation can reduce blast radius but does not "
                    "address the actual root cause here — the slow, manual patch "
                    "installation process itself."
                ),
            },
            {
                "id": "d",
                "text": "Deploy application allow-listing on all servers",
                "correct": False,
                "rationale": (
                    "Incorrect. Allow-listing controls which executables can run but "
                    "does not close the gap between patch approval and actual "
                    "installation, which is the specific failure described."
                ),
            },
        ],
        "explanation": (
            "Automating patch deployment on an enforced schedule directly closes the "
            "gap between approval and installation, while a slower manual cycle, "
            "segmentation, or allow-listing do not address the actual root cause of "
            "the delay."
        ),
    },
    {
        "id": "nd2d-039",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Mitigation techniques",
        "stem": (
            "Despite mandatory push-based MFA on every account, an attacker used an "
            "adversary-in-the-middle reverse-proxy phishing kit to capture both a "
            "user's password and the live session cookie issued immediately after the "
            "user approved the MFA push, then replayed that session cookie to bypass "
            "the MFA step entirely on subsequent access. Which mitigation would MOST "
            "effectively prevent this specific bypass technique from succeeding "
            "again?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Deploy phishing-resistant authentication (FIDO2/WebAuthn "
                "hardware security keys)",
                "correct": True,
                "rationale": (
                    "Correct. FIDO2/WebAuthn authentication cryptographically binds "
                    "the login to the legitimate site's origin, so a reverse-proxy "
                    "phishing kit cannot relay the challenge to a fake domain the way "
                    "it can with push notifications or OTP codes — directly defeating "
                    "this AiTM bypass technique."
                ),
            },
            {
                "id": "b",
                "text": "Require a longer, more complex password",
                "correct": False,
                "rationale": (
                    "Incorrect. Password complexity does not stop an "
                    "adversary-in-the-middle proxy from capturing whatever password "
                    "the user types and relaying it, or from stealing the resulting "
                    "session cookie afterward."
                ),
            },
            {
                "id": "c",
                "text": "Increase the frequency of push-based MFA prompts",
                "correct": False,
                "rationale": (
                    "Incorrect. The attacker already captured the session cookie "
                    "issued after a legitimate push approval; sending more push "
                    "prompts does nothing to prevent the proxy from relaying and "
                    "capturing the resulting session."
                ),
            },
            {
                "id": "d",
                "text": "Switch from push notifications to SMS-based one-time "
                "passcodes",
                "correct": False,
                "rationale": (
                    "Incorrect. SMS OTP codes are just as easily relayed through an "
                    "adversary-in-the-middle proxy as push approvals are; this switch "
                    "would not close the phishing-relay gap that enabled the bypass."
                ),
            },
        ],
        "explanation": (
            "Only phishing-resistant, origin-bound authentication like FIDO2/WebAuthn "
            "prevents an adversary-in-the-middle proxy from relaying the challenge and "
            "stealing the resulting session — password complexity, more frequent "
            "push prompts, and SMS OTP are all still vulnerable to the same relay "
            "technique."
        ),
    },
    {
        "id": "nd2d-040",
        "domain": 2,
        "objective": "2.5",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Mitigation techniques",
        "stem": (
            "A tabletop review of a recent ransomware incident finds that a single "
            "compromised workstation was able to reach and encrypt files on every "
            "network share the company operates, and that the organization's only "
            "backup copies were stored on that same reachable network segment and "
            "were also encrypted by the malware. Which TWO mitigation techniques "
            "would MOST effectively reduce the impact of a similar future incident? "
            "(Select two.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Network segmentation limiting each workstation's reach to "
                "only the shares its users actually require",
                "correct": True,
                "rationale": (
                    "Correct. Restricting reachability so a single compromised "
                    "workstation cannot touch every share on the network directly "
                    "limits the blast radius of a future ransomware outbreak."
                ),
            },
            {
                "id": "b",
                "text": "Offline or immutable backups isolated from the production "
                "network",
                "correct": True,
                "rationale": (
                    "Correct. Storing backups offline or in an immutable, isolated "
                    "location ensures they cannot be reached and encrypted by malware "
                    "that compromises the production network, guaranteeing a clean "
                    "recovery source."
                ),
            },
            {
                "id": "c",
                "text": "Increasing the frequency of vulnerability scans",
                "correct": False,
                "rationale": (
                    "Incorrect. More frequent scanning improves detection of "
                    "vulnerabilities but does nothing to limit how far a compromised "
                    "workstation can reach or to protect backups from being encrypted "
                    "alongside production data."
                ),
            },
            {
                "id": "d",
                "text": "Deploying an intrusion detection system in monitor-only mode",
                "correct": False,
                "rationale": (
                    "Incorrect. A monitor-only IDS can alert on suspicious activity "
                    "but takes no action to actually block lateral spread or protect "
                    "backup data from encryption, so it would not reduce impact."
                ),
            },
            {
                "id": "e",
                "text": "Requiring longer password expiration intervals",
                "correct": False,
                "rationale": (
                    "Incorrect. Password expiration policy has no bearing on how "
                    "widely ransomware can spread across shares or on whether backups "
                    "survive the attack."
                ),
            },
        ],
        "explanation": (
            "Limiting each workstation's network reach to only the shares it needs, "
            "combined with offline/immutable backups isolated from production, "
            "directly reduces both the blast radius of a ransomware outbreak and "
            "guarantees a clean recovery path — more frequent scanning, "
            "monitor-only detection, and password policy changes do not address "
            "either weakness."
        ),
    },
]
